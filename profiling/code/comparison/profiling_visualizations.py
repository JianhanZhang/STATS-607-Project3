"""Benchmark the existing tetrad simulation functions and save two runtime plots.

Place this file at the project root (alongside ``src/``), then run:
    python benchmark_optimization_visuals.py

For a quick end-to-end check:
    python benchmark_optimization_visuals.py --quick

All timings measure wall-clock time, including data generation. The multi-
replication parallel timings also include worker startup and result aggregation.
"""

import argparse
import time
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Directly reuse functions in the user's uploaded codebase.
from src.simulation import (
    run_one_simulation as run_one_original,
    run_simulations as run_many_original,
)
from src.simulation_optimized import (
    run_one_simulation as run_one_optimized,
    run_simulations_sequential as run_many_optimized_sequential,
    run_simulations_parallel as run_many_optimized_parallel,
)


# Keep the data-generating mechanism the same for every comparison.
ALPHA_2 = 0.1
BETA_2 = 0.2
DELTA = 0.0
ALPHA = 0.05
START_SEED = 607

SINGLE_METHODS = [
    ("Original", run_one_original),
    ("Optimized", run_one_optimized),
]

MULTI_METHODS = [
    ("Original sequential", run_many_original),
    ("Optimized parallel", run_many_optimized_parallel),
]


def elapsed_seconds(func, **kwargs):
    start = time.perf_counter()
    func(**kwargs)
    return time.perf_counter() - start


def benchmark_one_replication(sample_sizes, seeds, output_dir):
    """Figure 1: time to run ONE full replication, including all 3 tests."""
    records = []

    for n in sample_sizes:
        for i, seed in enumerate(seeds):
            # Alternate which implementation goes first to reduce order bias.
            methods = SINGLE_METHODS[i % 2 :] + SINGLE_METHODS[: i % 2]
            for method, func in methods:
                elapsed = elapsed_seconds(
                    func,
                    num_samples=n,
                    alpha_2=ALPHA_2,
                    beta_2=BETA_2,
                    delta=DELTA,
                    seed=seed,
                )
                records.append(
                    {"num_samples": n, "seed": seed,
                     "implementation": method, "wall_seconds": elapsed}
                )
                print(f"Single replication: n={n:<5} seed={seed} "
                      f"{method}: {elapsed:.3f}s", flush=True)

    df = pd.DataFrame.from_records(records)
    df.to_csv(output_dir / "profiling_single_rep_vs_sample_size.csv", index=False)
    return df


def benchmark_multiple_replications(replication_counts, trials, fixed_n,
                                    n_workers, output_dir):
    """Figure 2: time for R replications of ONE fixed DGP/sample size."""
    records = []

    for reps in replication_counts:
        for trial in range(trials):
            # Rotate order to reduce systematic warm-up/thermal effects.
            methods = MULTI_METHODS[trial % 3 :] + MULTI_METHODS[: trial % 3]
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
                records.append(
                    {"num_replications": reps, "sample_size": fixed_n,
                     "trial": trial + 1, "implementation": method,
                     "n_workers": n_workers if method == "Optimized parallel" else 1,
                     "wall_seconds": elapsed}
                )
                print(f"Replications: R={reps:<5} trial={trial + 1} "
                      f"{method}: {elapsed:.3f}s", flush=True)

    df = pd.DataFrame.from_records(records)
    df.to_csv(output_dir / "profiling_multiple_reps_vs_replication_count.csv", index=False)
    return df


def plot_median_runtime(df, x_col, plot_title, x_label, output_stem,
                        output_dir, labels):
    """Use median runtime of repeat measurements for each implementation."""
    summary = (
        df.groupby([x_col, "implementation"], as_index=False)["wall_seconds"]
        .median()
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    markers = ["o", "s", "^"]
    styles = ["-", "--", "-."]

    for i, method in enumerate(labels):
        group = summary[summary["implementation"] == method].sort_values(x_col)
        ax.plot(group[x_col], group["wall_seconds"], marker=markers[i],
                linestyle=styles[i], linewidth=2, label=method)

    ax.set_title(plot_title)
    ax.set_xlabel(x_label)
    ax.set_ylabel("Wall-clock runtime (seconds)")
    ax.set_xticks(sorted(summary[x_col].unique()))
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / f"{output_stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / f"{output_stem}.pdf", bbox_inches="tight")
    plt.close(fig)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true",
                        help="Use very small benchmark settings to check that the script runs")
    parser.add_argument("--workers", type=int, default=4,
                        help="Number of worker processes in optimized parallel runs")
    parser.add_argument("--fixed-n", type=int, default=100,
                        help="Fixed sample size for Figure 2")
    parser.add_argument("--output-dir", type=Path,
                        default=Path("profiling/results/comparison"))
    args = parser.parse_args()
    if args.workers < 1 or args.fixed_n < 1:
        parser.error("--workers and --fixed-n must be positive")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    sample_sizes = [50, 100] if args.quick else [100, 250, 500, 1000, 2000]
    seeds = [607] if args.quick else [607, 608, 609]
    rep_counts = [2, 4] if args.quick else [5, 10, 25, 50, 100]
    trials = 1 if args.quick else 3

    # Warm both implementations once so first-use library setup is not included.
    for _, fn in SINGLE_METHODS:
        fn(num_samples=40, alpha_2=ALPHA_2, beta_2=BETA_2,
           delta=DELTA, seed=START_SEED)

    df_one = benchmark_one_replication(sample_sizes, seeds, args.output_dir)
    plot_median_runtime(
        df_one, x_col="num_samples",
        plot_title="One Simulation Replication: Runtime vs. Sample Size",
        x_label="Sample size (n)", output_stem="runtime_vs_sample_size",
        output_dir=args.output_dir,
        labels=[name for name, _ in SINGLE_METHODS],
    )

    df_multi = benchmark_multiple_replications(
        rep_counts, trials, args.fixed_n, args.workers, args.output_dir
    )
    plot_median_runtime(
        df_multi, x_col="num_replications",
        plot_title=f"Total Runtime vs. Replications (n={args.fixed_n}, "
                   f"parallel workers={args.workers})",
        x_label="Number of replications",
        output_stem="runtime_vs_replications",
        output_dir=args.output_dir,
        labels=[name for name, _ in MULTI_METHODS],
    )
    print(f"Saved CSVs and PNG/PDF figures to {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
