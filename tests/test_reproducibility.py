'''Implement unit tests for reproducibility.'''

import numpy as np
from src.simulation import run_one_simulation
from src.simulation_optimized import run_one_simulation as run_one_simulation_optimized

def test_simulation_reproducibility_original():
    '''Test whether the same random seed results in the same simulation results for the original implementation.'''
    results_first = run_one_simulation(num_samples=100, alpha_2=0.1, beta_2=0.1, delta=0.1, seed=2026)
    results_second = run_one_simulation(num_samples=100, alpha_2=0.1, beta_2=0.1, delta=0.1, seed=2026)

    assert results_first['classical'] == results_second['classical']
    assert results_first['generalized_gmm'] == results_second['generalized_gmm']
    assert results_first['generalized_psmd'] == results_second['generalized_psmd']

def test_simulation_reproducibility_optimized():
    '''Test whether the same random seed results in the same simulation results for the optimized implementation.'''
    results_first = run_one_simulation_optimized(num_samples=100, alpha_2=0.1, beta_2=0.1, delta=0.1, seed=2026)
    results_second = run_one_simulation_optimized(num_samples=100, alpha_2=0.1, beta_2=0.1, delta=0.1, seed=2026)

    assert results_first['classical'] == results_second['classical']
    assert results_first['generalized_gmm'] == results_second['generalized_gmm']
    assert results_first['generalized_psmd'] == results_second['generalized_psmd']