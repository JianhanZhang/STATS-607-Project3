import time
import numpy as np
from src.simulation_optimized import run_simulations_sequential, run_simulations_parallel

if __name__ == "__main__":
    # ----------------- RUN THE PARALLELIZED SIMULATIONS -----------------
    wall_start = time.perf_counter()
    cpu_start = time.process_time()
    # Experiment 1: Reproduce Table 2 in the generalized tetrad test paper
    parameters_list = [
        [0, 0, 0], # Setting I
        [0.1, 0.2, 0], # Setting II(a)
        [0.3, 0.4, 0], # Setting II(b)
        [0, 0, 0.15], # Setting III(a)
        [0, 0, 0.3] # Setting III(b)
    ]
    run_simulations_parallel(num_replications=1000, num_samples_list=[500, 1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    # Experiment 2: Fix beta_2 = delta = 0, and vary alpha_2
    parameters_list = []
    for alpha_2 in np.arange(0, 1.0, 0.1):
        parameters_list.append([alpha_2, 0, 0])
    run_simulations_parallel(num_replications=100, num_samples_list=[1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    # Experiment 3: Fix alpha_2 = delta = 0, and vary beta_2
    parameters_list = []
    for beta_2 in np.arange(0, 1.0, 0.1):
        parameters_list.append([0, beta_2, 0])
    run_simulations_parallel(num_replications=100, num_samples_list=[1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    # Experiment 4: Fix alpha_2 = beta_2 = 0, and vary delta
    parameters_list = []
    for delta in np.arange(0, 1.0, 0.1):
        parameters_list.append([0, 0, delta])
    run_simulations_parallel(num_replications=100, num_samples_list=[1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    wall_end = time.perf_counter()
    cpu_end = time.process_time()

    with open("profiling/results/comparison/profiling_parallelization_comparison.txt", "w") as f:
        f.write("Parallelized simulations\n")
        f.write(f"Wall-clock time: {wall_end - wall_start:.4f} seconds\n")
        f.write(f"CPU time:        {cpu_end - cpu_start:.4f} seconds\n")

    # ----------------- RUN THE SEQUENTIAL SIMULATIONS -----------------

    wall_start = time.perf_counter()
    cpu_start = time.process_time()
    # Experiment 1: Reproduce Table 2 in the generalized tetrad test paper
    parameters_list = [
        [0, 0, 0], # Setting I
        [0.1, 0.2, 0], # Setting II(a)
        [0.3, 0.4, 0], # Setting II(b)
        [0, 0, 0.15], # Setting III(a)
        [0, 0, 0.3] # Setting III(b)
    ]
    run_simulations_sequential(num_replications=1000, num_samples_list=[500, 1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    # Experiment 2: Fix beta_2 = delta = 0, and vary alpha_2
    parameters_list = []
    for alpha_2 in np.arange(0, 1.0, 0.1):
        parameters_list.append([alpha_2, 0, 0])
    run_simulations_sequential(num_replications=100, num_samples_list=[1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    # Experiment 3: Fix alpha_2 = delta = 0, and vary beta_2
    parameters_list = []
    for beta_2 in np.arange(0, 1.0, 0.1):
        parameters_list.append([0, beta_2, 0])
    run_simulations_sequential(num_replications=100, num_samples_list=[1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    # Experiment 4: Fix alpha_2 = beta_2 = 0, and vary delta
    parameters_list = []
    for delta in np.arange(0, 1.0, 0.1):
        parameters_list.append([0, 0, delta])
    run_simulations_sequential(num_replications=100, num_samples_list=[1000], parameters_list=parameters_list, alpha=0.05, start_seed=1, raw_path=None)

    wall_end = time.perf_counter()
    cpu_end = time.process_time()

    with open("profiling/results/comparison/profiling_parallelization_comparison.txt", "a") as f:
        f.write("\nSequential simulations\n")
        f.write(f"Wall-clock time: {wall_end - wall_start:.4f} seconds\n")
        f.write(f"CPU time:        {cpu_end - cpu_start:.4f} seconds\n")