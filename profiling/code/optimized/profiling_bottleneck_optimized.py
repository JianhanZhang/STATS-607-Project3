'''Profile a typical single simulation run using the optimized code.'''

from cProfile import Profile
from pstats import Stats, SortKey
from src.simulation_optimized import run_one_simulation

with Profile() as profile:
    run_one_simulation(num_samples=10000, alpha_2=0.1, beta_2=0.1, delta=0.1, seed=607)

    (Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.TIME)
        .print_stats())

    with open("profiling/results/optimized/profiling_bottleneck_optimized.txt", "w") as f:
        stats = Stats(profile, stream=f)
        stats.sort_stats(SortKey.TIME)
        stats.print_stats()