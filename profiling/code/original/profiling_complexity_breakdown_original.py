import csv
import time
from pathlib import Path
from cProfile import Profile
from pstats import Stats, SortKey
from src.simulation import run_one_simulation

output_dir = Path("profiling/results/original")
output_dir.mkdir(parents=True, exist_ok=True)

sample_sizes = [1000, 2000, 5000, 10000]

runtime_results = []
for run_id, n in enumerate(sample_sizes, start=1):
    start = time.perf_counter()

    with Profile() as profiler:
        run_one_simulation(
            num_samples=n,
            alpha_2=0.1,
            beta_2=0.1,
            delta=0.1,
            seed=607
        )

    elapsed = time.perf_counter() - start
    prefix = f"run_{run_id}_n_{n}"
    profiler.dump_stats(output_dir / f"{prefix}.prof")

    with open(output_dir / f"{prefix}.txt", "w") as f:
        f.write(f"Sample size: {n}\n")
        f.write(f"Total runtime: {elapsed:.6f} seconds\n\n")

        f.write("--- Sorted by total internal time ---\n")
        Stats(profiler, stream=f).sort_stats(
            SortKey.TIME
        ).print_stats()

        f.write("\n--- Sorted by cumulative time ---\n")
        Stats(profiler, stream=f).sort_stats(
            SortKey.CUMULATIVE
        ).print_stats()

    runtime_results.append({
        "run_id": run_id,
        "num_samples": n,
        "runtime_seconds": elapsed
    })

    print(f"Run {run_id}: n={n}, runtime={elapsed:.4f}s")

with open(output_dir / "runtime_summary_original.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["run_id", "num_samples", "runtime_seconds"]
    )
    writer.writeheader()
    writer.writerows(runtime_results)
