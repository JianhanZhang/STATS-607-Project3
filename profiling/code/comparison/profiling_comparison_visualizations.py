"""Benchmark existing tetrad simulation functions and plot empirical scaling.

Run from the repository root, e.g.:
    python -m profiling.code.comparison.profiling_comparison_visualizations
    python -m profiling.code.comparison.profiling_comparison_visualizations --quick
    python -m profiling.code.comparison.profiling_comparison_visualizations --plot-only

Both figures use log-log axes. Dashed power-law fits summarize observed
finite-range scaling; they are NOT proofs of asymptotic algorithmic complexity.

Original output paths and filenames are retained under
``profiling/results/comparison``. Timing includes data generation; parallel
timings also include worker startup and result collection.
"""

import argparse
import time
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter, FixedLocator, NullFormatter
import numpy as np
import pandas as pd

# Reuse exactly the public simulation functions already in this project.
from src.simulation import (
    run_one_simulation as run_one_original,
    run_simulations as run_many_original,
)
from src.simulation_optimized import (
    run_one_simulation as run_one_optimized,
    run_simulations_sequential as run_many_optimized_sequential,
    run_simulations_parallel as run_many_optimized_parallel,
)

ALPHA_2 = 0.1
BETA_2 = 0.2
DELTA = 0.0
ALPHA = 0.05
START_SEED = 607

SINGLE_METHODS = [
    ("Original", run_one_original),
    ("Optimized", run_one_optimized),
]

# This third curve isolates the benefit of parallelism from the benefit of
# algorithmic changes, using the project's own optimized sequential runner.
MULTI_METHODS = [
    ("Original sequential", run_many_original),
    ("Optimized sequential", run_many_optimized_sequential),
    ("Optimized parallel", run_many_optimized_parallel),
]


# ---- Benchmarking -------------------------------------------------------

def elapsed_seconds(func, **kwargs):
    start = time.perf_counter()
    func(**kwargs)
    return time.perf_counter() - start


def benchmark_one_replication(sample_sizes, seeds, output_dir):
    """Time one full replication (DGP + all three tests) for each n."""
    records = []
    for n in sample_sizes:
        for i, seed in enumerate(seeds):
            # Rotate order to reduce the effect of systematic warm-up bias.
            methods = SINGLE_METHODS[i % len(SINGLE_METHODS):] + SINGLE_METHODS[:i % len(SINGLE_METHODS)]
            for method, func in methods:
                elapsed = elapsed_seconds(
                    func,
                    num_samples=n,
                    alpha_2=ALPHA_2,
                    beta_2=BETA_2,
                    delta=DELTA,
                    seed=seed,
                )
                records.append({
                    "num_samples": n,
                    "seed": seed,
                    "implementation": method,
                    "wall_seconds": elapsed,
                })
                print(
                    f"Single replication: n={n:<5} seed={seed} "
                    f"{method}: {elapsed:.3f}s", flush=True
                )

    df = pd.DataFrame.from_records(records)
    df.to_csv(output_dir / "profiling_single_rep_vs_sample_size.csv", index=False)
    return df


def benchmark_multiple_replications(replication_counts, trials, fixed_n,
                                    n_workers, output_dir):
    """Time R replications of one fixed DGP, including scheduler overhead."""
    records = []
    for reps in replication_counts:
        for trial in range(trials):
            rotation = trial % len(MULTI_METHODS)
            methods = MULTI_METHODS[rotation:] + MULTI_METHODS[:rotation]
            for method, func in methods:
                kwargs = dict(
                    num_replications=reps,
                    num_samples_list=[fixed_n],
                    parameters_list=[[ALPHA_2, BETA_2, DELTA]],
                    alpha=ALPHA,
                    start_seed=START_SEED,
                    raw_path=None,
                )
                if method == "Optimized parallel":
                    kwargs["n_workers"] = n_workers

                elapsed = elapsed_seconds(func, **kwargs)
                records.append({
                    "num_replications": reps,
                    "sample_size": fixed_n,
                    "trial": trial + 1,
                    "implementation": method,
                    "n_workers": n_workers if method == "Optimized parallel" else 1,
                    "wall_seconds": elapsed,
                })
                print(
                    f"Replications: R={reps:<5} trial={trial + 1} "
                    f"{method}: {elapsed:.3f}s", flush=True
                )

    df = pd.DataFrame.from_records(records)
    df.to_csv(output_dir / "profiling_multiple_reps_vs_replication_count.csv", index=False)
    return df


# ---- Log-log empirical scaling fits and figures ------------------------

def fit_empirical_power_law(x, times):
    """Fit log(t) = intercept + slope * log(x); return slope, scale, R^2."""
    x = np.asarray(x, dtype=float)
    times = np.asarray(times, dtype=float)
    if len(x) < 2 or len(np.unique(x)) < 2:
        return None
    if not (np.all(np.isfinite(x)) and np.all(x > 0) and
            np.all(np.isfinite(times)) and np.all(times > 0)):
        raise ValueError("Log-log fitting requires finite positive x and timings.")

    log_x, log_t = np.log(x), np.log(times)
    slope, intercept = np.polyfit(log_x, log_t, 1)
    log_predicted = intercept + slope * log_x
    residual_sum_squares = np.sum((log_t - log_predicted) ** 2)
    total_sum_squares = np.sum((log_t - log_t.mean()) ** 2)
    r_squared = (
        1 - residual_sum_squares / total_sum_squares
        if total_sum_squares > 0 else float("nan")
    )
    return float(slope), float(np.exp(intercept)), float(r_squared)


def plot_median_runtime(df, x_col, plot_title, x_label, output_stem,
                        output_dir, labels):
    """Log-log figure with measured medians and fitted power-law trend lines.

    A fitted slope p describes the empirical relationship t ~ x**p over the
    observed range only, not the theoretical/asymptotic complexity.
    """
    if df.empty:
        raise ValueError("Timing CSV contains no observations.")

    summary = (
        df.groupby([x_col, "implementation"], as_index=False)["wall_seconds"]
        .median()
    )
    fig, ax = plt.subplots(figsize=(9, 5.8))
    markers = ["o", "s", "^"]
    linestyles = ["-", "-", "-"]
    fit_records = []

    for i, method in enumerate(labels):
        group = summary.loc[summary["implementation"] == method].sort_values(x_col)
        if group.empty:
            print(f"Warning: no data for {method!r}; skipping this curve.")
            continue

        x = group[x_col].to_numpy(dtype=float)
        y = group["wall_seconds"].to_numpy(dtype=float)
        if np.any(x <= 0) or np.any(y <= 0):
            raise ValueError("All x values and measured runtimes must be positive for log-log plots.")

        fitted = fit_empirical_power_law(x, y)
        line_label = method
        if fitted is not None:
            exponent, scale, r_squared = fitted
            line_label += f"  (empirical slope = {exponent:.2f})"
            fit_records.append({
                "figure": output_stem,
                "implementation": method,
                "x_parameter": x_col,
                "n_points": len(x),
                "empirical_exponent": exponent,
                "power_law_scale": scale,
                "log_log_r_squared": r_squared,
            })

        measured_line, = ax.loglog(
            x, y,
            marker=markers[i % len(markers)],
            linestyle=linestyles[i % len(linestyles)],
            linewidth=2,
            markersize=6,
            label=line_label,
        )

        if fitted is not None:
            fit_x = np.geomspace(x.min(), x.max(), 200)
            fit_y = scale * fit_x ** exponent
            ax.loglog(
                fit_x, fit_y,
                linestyle="--",
                linewidth=1.6,
                alpha=0.8,
                color=measured_line.get_color(),
                label="_nolegend_",
            )
            print(
                f"{output_stem} | {method}: empirical exponent={exponent:.3f}, "
                f"log-log R^2={r_squared:.3f}", flush=True
            )

    ax.set_title(plot_title)
    ax.set_xlabel(x_label)
    ax.set_ylabel("Median wall-clock runtime (seconds)")
    tick_values = sorted(summary[x_col].unique())
    ax.xaxis.set_major_locator(FixedLocator(tick_values))
    ax.xaxis.set_major_formatter(FixedFormatter([f"{int(v):,}" for v in tick_values]))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.grid(True, which="major", alpha=0.35)
    ax.grid(True, which="minor", alpha=0.12)
    ax.legend(loc="best", fontsize=9)
    ax.text(
        0.01, -0.21,
        "Solid lines: measured medians. Dashed lines: fitted power laws. "
        "Slopes describe only the tested range.",
        transform=ax.transAxes,
        fontsize=8.5,
        va="top",
    )
    fig.subplots_adjust(bottom=0.25)

    # Preserve the original image output filenames and paths.
    fig.savefig(output_dir / f"{output_stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / f"{output_stem}.pdf", bbox_inches="tight")
    plt.close(fig)
    return pd.DataFrame(fit_records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quick", action="store_true",
        help="Small two-point benchmark for checking the script (slopes not reliable)",
    )
    parser.add_argument(
        "--plot-only", action="store_true",
        help="Redraw figures from existing timing CSV files without rerunning simulations",
    )
    parser.add_argument(
        "--workers", type=int, default=4,
        help="Number of worker processes in optimized parallel runs",
    )
    parser.add_argument(
        "--fixed-n", type=int, default=100,
        help="Fixed sample size for Figure 2",
    )
    parser.add_argument(
        "--output-dir", type=Path,
        default=Path("profiling/results/comparison"),
    )
    args = parser.parse_args()
    if args.workers < 1 or args.fixed_n < 1:
        parser.error("--workers and --fixed-n must be positive")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    if args.plot_only:
        df_one = pd.read_csv(
            args.output_dir / "profiling_single_rep_vs_sample_size.csv"
        )
        df_multi = pd.read_csv(
            args.output_dir / "profiling_multiple_reps_vs_replication_count.csv"
        )
        # Reflect actual recorded settings, not command-line defaults.
        fixed_n_values = df_multi["sample_size"].unique()
        if len(fixed_n_values) != 1:
            raise ValueError("Plot-only requires one fixed sample size in the multiple-replications CSV.")
        fixed_n = int(fixed_n_values[0])
        workers = df_multi.loc[
            df_multi["implementation"] == "Optimized parallel", "n_workers"
        ].unique()
        n_workers = int(workers[0]) if len(workers) == 1 else args.workers
    else:
        sample_sizes = [50, 100] if args.quick else [100, 250, 500, 1000, 2000]
        seeds = [607] if args.quick else [607, 608, 609]
        rep_counts = [5, 10] if args.quick else [5, 10, 25, 50, 100]
        trials = 1 if args.quick else 3

        # Warm both implementations so library initialization is excluded.
        for _, fn in SINGLE_METHODS:
            fn(num_samples=40, alpha_2=ALPHA_2, beta_2=BETA_2,
               delta=DELTA, seed=START_SEED)

        df_one = benchmark_one_replication(sample_sizes, seeds, args.output_dir)
        df_multi = benchmark_multiple_replications(
            rep_counts, trials, args.fixed_n, args.workers, args.output_dir
        )
        fixed_n = args.fixed_n
        n_workers = args.workers

    fit_one = plot_median_runtime(
        df_one, x_col="num_samples",
        plot_title="One Simulation Replication: Runtime vs. Sample Size (log-log)",
        x_label="Sample size (n)",
        output_stem="runtime_vs_sample_size",
        output_dir=args.output_dir,
        labels=[name for name, _ in SINGLE_METHODS],
    )
    fit_multi = plot_median_runtime(
        df_multi, x_col="num_replications",
        plot_title=f"Runtime vs. Replications (log-log; n={fixed_n}, workers={n_workers})",
        x_label="Number of replications (R)",
        output_stem="runtime_vs_replications",
        output_dir=args.output_dir,
        labels=[name for name, _ in MULTI_METHODS],
    )
    # Additional machine-readable estimates; existing CSV and image names unchanged.
    pd.concat([fit_one, fit_multi], ignore_index=True).to_csv(
        args.output_dir / "empirical_scaling_estimates.csv", index=False
    )
    print(f"Saved CSVs and PNG/PDF figures to {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
