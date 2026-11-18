# STATS-607-Project3

## Project Description

This repository reproduces the simulation study presented in Section 5 of the paper "A generalized tetrad constraint for testing conditional independence given a latent variable" [2]. The full paper can be found [here](https://arxiv.org/abs/2504.14173), and details about simulation objectives and settings implemented in this repository can be found in `ADEMP.md`.

The tetrad constraint is commonly used to test whether a collection of four variables are mutually independent conditional on a shared unobserved latent common cause. However, the classical tetrad test, proposed by [1], is only guaranteed to work when the underlying structural equation model is linear. The generalized tetrad constraint paper proposes a generalization of the classical tetrad test that is able to test the conditional independence in possibly nonlinear structural equation models.

The code in this repository is an optimized version of the code for Project 2.

## Setup Instructions

This project was developed using Python 3.14.7.

To set up the project, first clone the repository and move into the project directory.

```bash
git clone https://github.com/JianhanZhang/STATS-607-Project3.git
cd STATS-607-Project3
```

Once in the project directory, run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Testing

The following command runs the unit tests 

```bash
make test
```

## Running the Analysis

The following command runs the simulation and generates raw simulation results

```bash
make simulate
```

Running the above command should generate the following files:

- `results/raw/raw_results_table2.csv`
- `results/raw/raw_results_alpha2.csv`
- `results/raw/raw_results_beta2.csv`
- `results/raw/raw_results_delta.csv`

The following command aggregates the raw simulation results into summary tables

```bash
make analyze
```

Running the above command should generate the following files:

- `results/raw/results_table2.csv`
- `results/raw/results_alpha2.csv`
- `results/raw/results_beta2.csv`
- `results/raw/results_delta.csv`

The following command produces visualizations on the empirical distribution of p-values and on the 
empirical rejection rates under different data-generating parameters

```bash
make figures
```

Running the above command should generate the following files:

- `results/figures/plot_p_value_distribution.png`
- `results/figures/plot_rejection_rate_by_parameter_value.png`

Alternatively, the following command runs the simulation, produces raw results, aggregates the raw results, and 
makes the visualizations together. It generates all of the files mentioned above in one command.

```bash
make all
```

(Optionally) the following command removes previously generated result files and visualizations

```bash
make clean
```

## Profiling the Code

The following command runs profiling on a representative single simulation run

```bash
make profile
```

Running the above command should generate the following files:

- `profiling/results/original/profiling_bottleneck_original.txt`: profiling results for the original code.
- `profiling/results/optimized/profiling_bottleneck_optimized.txt`: profiling results for the optimized code.

The following command runs a computational complexity analysis of runtime vs sample size on a representative single simulation run

```bash
make complexity
```

Running the above command should generate the following files:

- `profiling/results/original/complexity_overall_raw_timings_original.csv`: raw results generated while running the complexity analysis on the original code.
- `profiling/results/original/complexity_overall_summary_original.csv`: Summary table of results of the complexity analysis for the original code.
- `profiling/results/original/complexity_overall_plot_original.png`: Summary plot of the results of the complexity analysis for the original code, with a regression line included.
- `profiling/results/optimized/complexity_overall_raw_timings_optimized.csv`: raw results generated while running the complexity analysis on the optimized code.
- `profiling/results/optimized/complexity_overall_summary_optimized.csv`: Summary table of results of the complexity analysis for the optimized code.
- `profiling/results/optimized/complexity_overall_plot_optimized.png`: Summary plot of the results of the complexity analysis for the optimized code, with a regression line included.

The following command runs a runtime comparison between the original code and optimized code.

```bash
make benchmark
```

Running the above command should generate the following files:

- `profiling/results/comparison/profiling_single_rep_vs_sample_size.csv`: raw results comparing runtime of a single simulation run vs sample size.
- `profiling/results/comparison/runtime_vs_sample_size.png`: plots comparing runtime of a single simulation run vs sample size, with a regression line; in `.png` format.
- `profiling/results/comparison/runtime_vs_sample_size.pdf`: plots comparing runtime of a single simulation run vs sample size, with a regression line; in `.pdf` format.
- `profiling/results/comparison/profiling_multiple_reps_vs_replication_count.csv`: raw results comparing runtime of a multiple simulation replications vs replication count.
- `profiling/results/comparison/runtime_vs_replications.png`: plots comparing runtime of a multiple simulation replications vs replication count, with a regression line; in `.png` format.
- `profiling/results/comparison/runtime_vs_replications.pdf`: plots comparing runtime of a multiple simulation replications vs replication count, with a regression line; in `.pdf` format.

The following command runs the full set of simulations using the optimized code and parallelization

```bash
make parallel
```

Running the above command should generate the following files:

- `results/raw/raw_results_table2_optimized.csv`
- `results/raw/raw_results_alpha2_optimized.csv`
- `results/raw/raw_results_beta2_optimized.csv`
- `results/raw/raw_results_delta_optimized.csv`

The following command runs a check for potential signs of numerical instability

```bash
make stability-check
```

Running the above command should generate the following files:

- `profiling/results/original/stability_detailed_original.csv`
- `profiling/results/original/stability_summary_original.csv`
- `profiling/results/optimized/stability_detailed_optimized.csv`
- `profiling/results/optimized/stability_summary_optimized.csv`

## Estimated Runtime

An estimated runtime of the full simulation using the original code is 14887 seconds (approximately 4 hours). Please note that the actual runtime should depend on the specific computing environment.

## Summary of Key Findings

Under relatively large samples, across the settings tested in the simulation, the generalized tetrad test with PSMD successfully controls the type I error rate under both linear and nonlinear data-generating mechanisms when the null is true and has power close to 1 under linear data-generating mechanisms when the null is false, while the classical tetrad test is sometimes unreliable when the data-generating mechanism is nonlinear. Moreover, the generalized tetrad test with PSMD appears to consistently maintain a low Type I error rate as we increase the degree of deviation from linearity.

## Declaration of AI Use:

Generative AI is involved in the workflow of this project. Its main contributions include:

1. I used AI to remind me of useful Python syntax and packages and debug my code.
2. The algorithmic improvements implemented in Optimization 2 was initially proposed by AI. I checked the correctness of the idea and adapted the idea to fit my current code structure.
3. I discussed with AI the implementation of some nuanced technical details of the optimizations. I checked the suggested implementations.
4. AI helped with the code for plotting and for summarizing and saving profiling results; general ideas regarding what to profile and what to plot are supplied by me. I checked AI's suggestions. 
5. AI helped with creating some docstrings. Where AI assistance is used, I read and modified the corresponding docstrings to make sure that the descriptions are clear and accurate.

## References

[1] Bollen, K. A. (1990). Outlier screening and a distribution-free test for vanishing tetrads. *Sociological Methods & Research*, 19(1), 80-92.

[2] Ying, N., Zhang, P., Luo, S., & Miao, W. (2025). A generalized tetrad constraint for testing conditional independence given a latent variable. *arXiv preprint arXiv:2504.14173*.