'''Implement regression tests to make sure the optimization does not change test results. ClassicalTetradTest is not tested because it is not changed.'''

import numpy as np
from scipy.stats import chi2
from src.dgps import generate_data
from src.methods import ClassicalTetradTest, GeneralizedTetradTestGMM, GeneralizedTetradTestPSMD
from src.methods_optimized import ClassicalTetradTestOptimized, GeneralizedTetradTestGMMOptimized, GeneralizedTetradTestPSMDOptimized

# ---------- TEST THE TEST STATISTIC ----------
def test_regression_generalized_tetrad_gmm_statistic_null_n100():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the null setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_null_n100():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the null setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_nonlinear_n100():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the nonlinear setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_nonlinear_n100():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the nonlinear setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_alternative_n100():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the alternative setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_alternative_n100():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the alternative setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_extreme_n100():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the extreme setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_extreme_n100():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the extreme setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_null_n500():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the null setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_null_n500():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the null setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_nonlinear_n500():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the nonlinear setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_nonlinear_n500():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the nonlinear setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_alternative_n500():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the alternative setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_alternative_n500():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the alternative setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_gmm_statistic_extreme_n500():
    '''Test that generalized tetrad test with GMM gives the same test statistic before and after optimization in the extreme setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

def test_regression_generalized_tetrad_psmd_statistic_extreme_n500():
    '''Test that generalized tetrad test with PSMD gives the same test statistic before and after optimization in the extreme setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    statistic_original = test_original.compute_test_statistic()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    statistic_optimized = test_optimized.compute_test_statistic()

    assert np.isclose(statistic_original, statistic_optimized)

# ---------- TEST THE P-VALUE ----------

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_null_n100():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the null setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_null_n100():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the null setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_nonlinear_n100():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the nonlinear setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_nonlinear_n100():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the nonlinear setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_alternative_n100():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the alternative setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_alternative_n100():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the alternative setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_extreme_n100():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the extreme setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_extreme_n100():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the extreme setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_null_n500():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the null setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_null_n500():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the null setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_nonlinear_n500():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the nonlinear setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_nonlinear_n500():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the nonlinear setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_alternative_n500():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the alternative setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_alternative_n500():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the alternative setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_gmm_p_value_correctness_extreme_n500():
    '''Test that the generalized tetrad test with GMM gives the same p-values before and after optimization in the extreme setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

def test_regression_generalized_tetrad_test_psmd_p_value_correctness_extreme_n500():
    '''Test that the generalized tetrad test with PSMD gives the same p-values before and after optimization in the extreme setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    p_value_original = test_original.compute_p_value()
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)
    p_value_optimized = test_optimized.compute_p_value()

    assert np.isclose(p_value_original, p_value_optimized)

# ---------- TEST THE REJECTION DECISION ----------

def test_regression_generalized_tetrad_test_gmm_rejection_decision_null_n100():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the null setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_null_n100():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the null setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_nonlinear_n100():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the nonlinear setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_nonlinear_n100():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the nonlinear setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_alternative_n100():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the alternative setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_alternative_n100():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the alternative setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_extreme_n100():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the extreme setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_extreme_n100():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the extreme setting (n=100).'''
    X, Y, Z, W, U = generate_data(num_samples=100, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_null_n500():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the null setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_null_n500():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the null setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_nonlinear_n500():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the nonlinear setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_nonlinear_n500():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the nonlinear setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0.1, beta_2=0.2, delta=0)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_alternative_n500():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the alternative setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_alternative_n500():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the alternative setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=0, beta_2=0, delta=0.3)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_gmm_rejection_decision_extreme_n500():
    '''Test that the generalized tetrad test with GMM gives the same rejection decisions before and after optimization in the extreme setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestGMM(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestGMMOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)

def test_regression_generalized_tetrad_test_psmd_rejection_decision_extreme_n500():
    '''Test that the generalized tetrad test with PSMD gives the same rejection decisions before and after optimization in the extreme setting (n=500).'''
    X, Y, Z, W, U = generate_data(num_samples=500, alpha_2=10, beta_2=10, delta=10)
    test_original = GeneralizedTetradTestPSMD(X, Y, Z, W)
    test_optimized = GeneralizedTetradTestPSMDOptimized(X, Y, Z, W)

    assert test_original.reject(alpha=0.10) == test_optimized.reject(alpha=0.10)
    assert test_original.reject(alpha=0.05) == test_optimized.reject(alpha=0.05)
    assert test_original.reject(alpha=0.01) == test_optimized.reject(alpha=0.01)