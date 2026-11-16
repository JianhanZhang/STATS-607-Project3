'''Record the total runtime of a single simulation run against different sample sizes using the original code.'''

import time
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from src.simulation import run_one_simulation


def analyze_complexity(
    sample_sizes,
    num_replications=3,
    alpha_2=0.1,
    beta_2=0.1,
    delta=0.1,
    start_seed=607,
    output_dir="profiling/results/original",
):
    '''Analyze the empirical computational complexity of a single simulation run against different sample sizes using the original code.
    Regress the log of the median runtime against the log of the sample size to estimate the complexity exponent.

    Parameters:
    sample_sizes: List of sample sizes to test.
    num_replications: Number of times to replicate each simulation.
    alpha_2: Parameter for the simulation.
    beta_2: Parameter for the simulation.
    delta: Parameter for the simulation.
    start_seed: Starting seed for the replications.
    output_dir: Directory to save results.

    Returns:
    summary: DataFrame summarizing the runtimes for each sample size.
    regression: Result of the linear regression on the log-log scale.
    '''
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []

    # Record runtimes
    for n in sample_sizes:
        for i in range(num_replications):
            seed = start_seed + i

            start = time.perf_counter()

            run_one_simulation(
                num_samples=n,
                alpha_2=alpha_2,
                beta_2=beta_2,
                delta=delta,
                seed=seed,
            )

            runtime = time.perf_counter() - start

            results.append({
                "num_samples": n,
                "seed": seed,
                "runtime": runtime,
            })

            print(f"n={n}, seed={seed}, runtime={runtime:.4f}s")

    # Save individual runtimes
    df = pd.DataFrame(results)
    df.to_csv(output_dir / "complexity_overall_raw_timings_original.csv", index=False)

    # Step 2: Summarize runtimes at each n
    summary = (
        df.groupby("num_samples", as_index=False)
        .agg(
            mean_runtime=("runtime", "mean"),
            median_runtime=("runtime", "median"),
            std_runtime=("runtime", "std"),
        )
    )
    summary.to_csv(output_dir / "complexity_overall_summary_original.csv", index=False)

    # Step 3: Fit regression on the log scale
    log_n = np.log(summary["num_samples"])
    log_t = np.log(summary["median_runtime"])

    regression = linregress(log_n, log_t)

    print(f"Estimated complexity exponent: {regression.slope:.4f}")
    print(f"R-squared: {regression.rvalue**2:.4f}")

    # Step 4: Plot observed and fitted runtimes
    n_grid = np.geomspace(
        min(sample_sizes), max(sample_sizes), 200
    )
    fitted_runtime = (
        np.exp(regression.intercept)
        * n_grid ** regression.slope
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.loglog(
        summary["num_samples"],
        summary["median_runtime"],
        "o-",
        label="Observed median runtime",
    )
    ax.loglog(
        n_grid,
        fitted_runtime,
        "--",
        label=f"Fitted: O(n^{regression.slope:.2f})",
    )

    ax.set_xlabel("Sample size (n)")
    ax.set_ylabel("Runtime (seconds)")
    ax.set_title("Empirical Computational Complexity")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_dir / "complexity_overall_plot_original.png", dpi=300)
    plt.close(fig)

    return summary, regression


if __name__ == "__main__":
    summary, regression = analyze_complexity(
        sample_sizes=[500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 
                      5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],
        num_replications=3,
    )
