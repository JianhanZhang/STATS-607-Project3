'''Check for signs of numerical instability in the original code.'''

import warnings
from pathlib import Path
import numpy as np
import pandas as pd
from src.dgps import generate_data
from src.methods import ClassicalTetradTest, GeneralizedTetradTestGMM, GeneralizedTetradTestPSMD

output_dir = Path("profiling/results/original")
output_dir.mkdir(parents=True, exist_ok=True)

sample_sizes = [100, 500, 1000]
seeds = range(607, 612)

scenarios = {
    "null": (0, 0, 0),
    "nonlinear": (0.1, 0.2, 0),
    "alternative": (0, 0, 0.3),
    "extreme": (10, 10, 10),
}

methods = {
    "classical": ClassicalTetradTest,
    "gmm": GeneralizedTetradTestGMM,
    "psmd": GeneralizedTetradTestPSMD,
}

results = []

for n in sample_sizes:
    for scenario, (alpha_2, beta_2, delta) in scenarios.items():
        for seed in seeds:

            np.random.seed(seed)
            X, Y, Z, W, U = generate_data(
                n, alpha_2, beta_2, delta
            )

            for method_name, method_class in methods.items():

                p_value = np.nan
                exception_message = ""

                # Capture warnings
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")

                    with np.errstate(all="warn"):
                        try:
                            test = method_class(X, Y, Z, W)
                            p_value = float(test.compute_p_value())

                        except Exception as e:
                            exception_message = (
                                f"{type(e).__name__}: {e}"
                            )

                warning_messages = [
                    f"{w.category.__name__}: {w.message}"
                    for w in caught
                ]

                valid_pvalue = (
                    np.isfinite(p_value)
                    and 0 <= p_value <= 1
                )

                if exception_message:
                    status = "exception"
                elif not valid_pvalue:
                    status = "invalid_pvalue"
                elif warning_messages:
                    status = "warning"
                else:
                    status = "ok"

                results.append({
                    "num_samples": n,
                    "scenario": scenario,
                    "alpha_2": alpha_2,
                    "beta_2": beta_2,
                    "delta": delta,
                    "seed": seed,
                    "method": method_name,
                    "p_value": p_value,
                    "status": status,
                    "warning_count": len(warning_messages),
                    "warnings": " | ".join(warning_messages),
                    "exception": exception_message,
                })

                print(
                    f"n={n}, scenario={scenario}, "
                    f"seed={seed}, method={method_name}, "
                    f"status={status}"
                )

# Save detailed results
df = pd.DataFrame(results)
df.to_csv(output_dir / "stability_detailed_original.csv", index=False)

# Summarize frequency of numerical issues
df["problematic"] = df["status"] != "ok"

summary = (
    df.groupby(
        ["num_samples", "scenario", "method"],
        as_index=False
    )
    .agg(
        total_runs=("status", "size"),
        runs_with_issues=("problematic", "sum"),
        total_warnings=("warning_count", "sum"),
    )
)

summary["issue_rate"] = (
    summary["runs_with_issues"] / summary["total_runs"]
)

summary.to_csv(output_dir / "stability_summary_original.csv", index=False)

print("\nNumerical stability summary:")
print(summary.to_string(index=False))
