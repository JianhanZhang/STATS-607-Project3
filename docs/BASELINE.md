# Baseline Metrics Document for STATS 607 Project 3

This document contains information about the computational costs of the simulation study before being optimized.

## Runtime of Entire Simulation Study

The total runtime of the entire simulation study (including all settings and experiments) is 14887 seconds.

## Profiler Results

I ran a single experiment by running `run_one_simulation(num_samples=10000, alpha_2=0.1, beta_2=0.1, delta=0.1, seed=607)` and used `cProfile` to profile the run. The results are summarized below (with the help be ChatGPT based on the original baseline profile results from `cProfile`):

### Overview

**Function calls:** 2,005,170 total (2,005,122 primitive calls).  
**Profiled runtime:** 11.890 seconds.  
**Sort order:** Internal time (`tottime`), descending.  
**Source:** Original baseline profile, all 322 function rows preserved in their original order. The original profile results can be found in `profiling/results/original/profiling_bottleneck_original.txt`.

### Column definitions

- `ncalls`: Number of calls (the `total/primitive` notation appears for recursive calls).
- `tottime (s)`: Time in the function itself, excluding calls to other functions.
- `tottime/call (s)`: Average internal time per call.
- `cumtime (s)`: Cumulative time in the function and all subfunctions it calls.
- `cumtime/call (s)`: Average cumulative time per call.
- `filename:lineno(function)`: Function location as printed by the profiler (full paths retained).

### Complete profiler table

| ncalls | tottime (s) | tottime/call (s) | cumtime (s) | cumtime/call (s) | filename:lineno(function) |
|---:|---:|---:|---:|---:|---|
| 20000 | 4.629 | 0.000 | 6.195 | 0.000 | `src/methods.py:336(_compute_phi_s)` |
| 2 | 3.207 | 1.604 | 9.569 | 4.784 | `src/methods.py:383(_compute_sn)` |
| 80127 | 1.239 | 0.000 | 1.239 | 0.000 | `{method 'reduce' of 'numpy.ufunc' objects}` |
| 3 | 0.922 | 0.307 | 1.131 | 0.377 | `src/methods.py:617(_compute_delta_matrix)` |
| 1 | 0.754 | 0.754 | 0.900 | 0.900 | `src/methods.py:292(_compute_delta_matrix)` |
| 40034 | 0.250 | 0.000 | 0.270 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_shape_base_impl.py:607(column_stack)` |
| 2 | 0.217 | 0.108 | 1.080 | 0.540 | `src/methods.py:701(_compute_sn)` |
| 8 | 0.157 | 0.020 | 0.157 | 0.020 | `{method 'outer' of 'numpy.ufunc' objects}` |
| 60040 | 0.071 | 0.000 | 1.112 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_methods.py:115(_mean)` |
| 20004 | 0.068 | 0.000 | 0.068 | 0.000 | `src/methods.py:287(estimated_bridge_function)` |
| 20003 | 0.052 | 0.000 | 0.124 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:374(solve)` |
| 40000 | 0.049 | 0.000 | 0.057 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:170(ones)` |
| 60040 | 0.031 | 0.000 | 0.036 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_methods.py:73(_count_reduce_items)` |
| 2 | 0.020 | 0.010 | 0.020 | 0.010 | `src/methods.py:630(_compute_mgtn)` |
| 2 | 0.020 | 0.010 | 0.020 | 0.010 | `src/methods.py:305(_compute_mgtn)` |
| 20004 | 0.016 | 0.000 | 0.021 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_twodim_base_impl.py:178(eye)` |
| 20009 | 0.014 | 0.000 | 0.029 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:201(_commonType)` |
| 60003 | 0.013 | 0.000 | 1.123 | 0.000 | `{method 'mean' of 'numpy.ndarray' objects}` |
| 220131 | 0.012 | 0.000 | 0.012 | 0.000 | `{built-in method builtins.issubclass}` |
| 20035 | 0.010 | 0.000 | 0.265 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:66(_wrapreduction)` |
| 20024 | 0.009 | 0.000 | 0.275 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2342(sum)` |
| 40018 | 0.009 | 0.000 | 0.013 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:163(_makearray)` |
| 80171 | 0.009 | 0.000 | 0.009 | 0.000 | `{built-in method numpy.array}` |
| 100321 | 0.007 | 0.000 | 0.007 | 0.000 | `{built-in method builtins.isinstance}` |
| 140264 | 0.007 | 0.000 | 0.007 | 0.000 | `{built-in method numpy.asanyarray}` |
| 80041 | 0.007 | 0.000 | 0.007 | 0.000 | `{built-in method builtins.hasattr}` |
| 40018 | 0.006 | 0.000 | 0.006 | 0.000 | `{built-in method numpy.empty}` |
| 20013 | 0.006 | 0.000 | 0.012 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_ufunc_config.py:472(__enter__)` |
| 60027 | 0.006 | 0.000 | 0.009 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:168(isComplexType)` |
| 40034 | 0.006 | 0.000 | 0.015 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_shape_base_impl.py:603(_column_stack_dispatcher)` |
| 40034 | 0.006 | 0.000 | 0.009 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/shape_base.py:206(_arrays_for_stack_dispatcher)` |
| 80153 | 0.005 | 0.000 | 0.005 | 0.000 | `{method 'append' of 'list' objects}` |
| 40022 | 0.005 | 0.000 | 0.007 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:182(_realType)` |
| 60059 | 0.004 | 0.000 | 0.004 | 0.000 | `{built-in method numpy.lib.array_utils.normalize_axis_index}` |
| 20013 | 0.003 | 0.000 | 0.003 | 0.000 | `{built-in method numpy._core._multiarray_umath._make_extobj}` |
| 20015 | 0.003 | 0.000 | 0.003 | 0.000 | `{built-in method numpy.zeros}` |
| 20013 | 0.003 | 0.000 | 0.006 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_ufunc_config.py:488(__exit__)` |
| 20013 | 0.003 | 0.000 | 0.003 | 0.000 | `{method 'reset' of '_contextvars.ContextVar' objects}` |
| 20003 | 0.003 | 0.000 | 0.003 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:250(_assert_stacked_square)` |
| 40093 | 0.003 | 0.000 | 0.003 | 0.000 | `{method 'get' of 'dict' objects}` |
| 20083 | 0.003 | 0.000 | 0.003 | 0.000 | `{method 'astype' of 'numpy.ndarray' objects}` |
| 20013 | 0.002 | 0.000 | 0.002 | 0.000 | `{method 'set' of '_contextvars.ContextVar' objects}` |
| 40079 | 0.002 | 0.000 | 0.002 | 0.000 | `{built-in method builtins.getattr}` |
| 20017 | 0.002 | 0.000 | 0.002 | 0.000 | `{method '__array_wrap__' of 'numpy.ndarray' objects}` |
| 40105 | 0.002 | 0.000 | 0.002 | 0.000 | `{built-in method numpy.asarray}` |
| 40035 | 0.002 | 0.000 | 0.002 | 0.000 | `{built-in method _operator.index}` |
| 40014 | 0.002 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/multiarray.py:1088(copyto)` |
| 40054 | 0.002 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/multiarray.py:197(concatenate)` |
| 20063 | 0.002 | 0.000 | 0.002 | 0.000 | `{method 'items' of 'dict' objects}` |
| 4 | 0.002 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:2434(lstsq)` |
| 20013 | 0.001 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_ufunc_config.py:462(__init__)` |
| 20024 | 0.001 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2337(_sum_dispatcher)` |
| 20003 | 0.001 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:370(_solve_dispatcher)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `src/dgps.py:6(generate_data)` |
| 2 | 0.000 | 0.000 | 0.002 | 0.001 | `src/methods.py:548(_estimate_bridge_function)` |
| 30 | 0.000 | 0.000 | 0.001 | 0.000 | `src/methods.py:262(moment_function)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/polynomial/polynomial.py:1128(polyvander)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:119(_compute_covariance_of_sample_covariances)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1144(bmm_einsum)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/stats/_distn_infrastructure.py:2219(sf)` |
| 10 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:288(approx_derivative)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:2688(cov)` |
| 2 | 0.000 | 0.000 | 0.003 | 0.002 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:1345(_minimize_bfgs)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:634(einsum_path)` |
| 1 | 0.000 | 0.000 | 10.492 | 10.492 | `src/methods.py:432(compute_test_statistic)` |
| 1 | 0.000 | 0.000 | 1.396 | 1.396 | `src/methods.py:749(compute_test_statistic)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:447(_broadcast_to)` |
| 10 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:683(_dense_difference)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/function_base.py:27(linspace)` |
| 30 | 0.000 | 0.000 | 0.002 | 0.000 | `src/methods.py:272(gmm_objective)` |
| 37 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:3737(mean)` |
| 1 | 0.000 | 0.000 | 1.396 | 1.396 | `src/methods.py:776(compute_p_value)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:1666(svd)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:330(_greedy_path)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/stats/_continuous_distns.py:1658(_sf)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:445(_parse_einsum_input)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/stats/_distn_infrastructure.py:613(argsreduce)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'disable' of '_lsprof.Profiler' objects}` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:1546(resize)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:2170(pinv)` |
| 2 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1242(einsum)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/stats/_distn_infrastructure.py:1006(_argcheck)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/stats/_distn_infrastructure.py:1045(_open_support_mask)` |
| 17 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:1427(normalize_axis_tuple)` |
| 68 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'reshape' of 'numpy.ndarray' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:4923(trapezoid)` |
| 28 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:86(_wrapreduction_any_all)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:968(_parse_eq_to_batch_matmul)` |
| 15 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_dcsrch.py:269(_iterate)` |
| 30 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:541(__call__)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:1489(moveaxis)` |
| 1 | 0.000 | 0.000 | 11.890 | 11.890 | `src/simulation.py:11(run_one_simulation)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:602(bridge_function)` |
| 20 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:904(__call__)` |
| 14 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:90(_find_contraction)` |
| 2 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:218(__init__)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:517(_polynomial_basis)` |
| 55 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/shape_base.py:19(atleast_1d)` |
| 25/1 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method _abc._abc_subclasscheck}` |
| 7 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_dcsrch.py:201(__call__)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:14(_adjust_scheme_to_bounds)` |
| 19 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:195(vecnorm)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_array_api.py:497(xp_result_type)` |
| 10 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:35(__call__)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:1414(diff)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:224(_parse_possible_contraction)` |
| 32 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numerictypes.py:328(isdtype)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:2471(array_equal)` |
| 12 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:246(ones_like)` |
| 2 | 0.000 | 0.000 | 0.003 | 0.002 | `venv/lib/python3.14/site-packages/scipy/optimize/_minimize.py:54(minimize)` |
| 32 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numerictypes.py:309(_preprocess_dtype)` |
| 230 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.len}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1083(<genexpr>)` |
| 40 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_external/array_api_compat/numpy/_aliases.py:97(astype)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:206(_prepare_bounds)` |
| 1 | 0.000 | 0.000 | 10.492 | 10.492 | `src/methods.py:459(compute_p_value)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_external/array_api_extra/_delegation.py:35(atleast_nd)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:532(_polynomial_derivative_basis)` |
| 7 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_linesearch.py:108(scalar_search_wolfe1)` |
| 8 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_linesearch.py:94(derphi)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_twodim_base_impl.py:260(diag)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:588(broadcast_arrays)` |
| 31 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:48(_wrapfunc)` |
| 30 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:694(x_generator2)` |
| 2 | 0.000 | 0.000 | 0.003 | 0.002 | `src/methods.py:238(_estimate_bridge_function)` |
| 60 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_external/array_api_compat/common/_helpers.py:683(_check_device)` |
| 30 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:1917(ravel)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:520(_broadcast_shape)` |
| 12 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.min}` |
| 7 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_linesearch.py:37(line_search_wolfe1)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_external/array_api_compat/numpy/_aliases.py:70(asarray)` |
| 10 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:391(fun)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_dcsrch.py:502(dcstep)` |
| 7 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:1156(_line_search_wolfe12)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/pstats.py:107(__init__)` |
| 14 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'copy' of 'set' objects}` |
| 14 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.sorted}` |
| 12 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:371(_update_grad)` |
| 8 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_linesearch.py:90(phi)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:1708(diagonal)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method numpy.arange}` |
| 26 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:207(reshape)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:337(_update_x)` |
| 1 | 0.000 | 0.000 | 0.001 | 0.001 | `src/methods.py:178(compute_test_statistic)` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method numpy._core._multiarray_umath.c_einsum}` |
| 15 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2474(any)` |
| 22 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:360(_update_fun)` |
| 9 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:2112(place)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'any' of 'numpy.generic' objects}` |
| 24 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:375(iterable)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1125(_parse_output_order)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:57(__init__)` |
| 9 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method numpy._core._multiarray_umath._place}` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_external/array_api_compat/common/_helpers.py:149(is_torch_array)` |
| 52 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:936(copy)` |
| 36 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:61(_compute_size_by_dict)` |
| 11 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:3165(amax)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:88(_compute_covariance_matrix)` |
| 38 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'ravel' of 'numpy.ndarray' objects}` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/pstats.py:117(init)` |
| 10 | 0.000 | 0.000 | 0.002 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:397(grad)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/pstats.py:136(load_stats)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:451(average)` |
| 2 | 0.000 | 0.000 | 0.001 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:204(_prepare_scalar_function)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'all' of 'numpy.ndarray' objects}` |
| 32 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:1911(isscalar)` |
| 30 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:217(<genexpr>)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_array_api.py:76(_asarray)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:97(zeros_like)` |
| 13 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2586(all)` |
| 34 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:1476(<genexpr>)` |
| 32 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'update' of 'set' objects}` |
| 23 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_methods.py:64(_all)` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1080(<genexpr>)` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.sum}` |
| 15 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2469(_any_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:2615(norm)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'sum' of 'numpy.ndarray' objects}` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/getlimits.py:169(__new__)` |
| 1 | 0.000 | 0.000 | 0.001 | 0.001 | `src/methods.py:202(compute_p_value)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/enum.py:187(__get__)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:143(_compute_covariance_of_tetrad_differences)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:93(_eps_for_method)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `<string>:1(<lambda>)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/polynomial/polyutils.py:703(_as_int)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'split' of 'str' objects}` |
| 52 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:932(_copy_dispatcher)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:14(__init__)` |
| 55 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/shape_base.py:15(_atleast_1d_dispatcher)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:30(_sanity_check)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:575(__init__)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/cProfile.py:53(create_stats)` |
| 12 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1234(_einsum_dispatcher)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:23(_flop_count)` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/stats/_distn_infrastructure.py:1018(_get_support)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'clip' of 'numpy.generic' objects}` |
| 25/1 | 0.000 | 0.000 | 0.000 | 0.000 | `<frozen abc>:121(__subclasscheck__)` |
| 32 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_array_api_override.py:73(array_namespace)` |
| 7 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_dcsrch.py:174(__init__)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'all' of 'numpy.generic' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'diagonal' of 'numpy.ndarray' objects}` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_methods.py:96(_clip)` |
| 16 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.max}` |
| 18 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:270(<genexpr>)` |
| 37 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:3732(_mean_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_minimize.py:1134(standardize_constraints)` |
| 32 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'values' of 'dict' objects}` |
| 5 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_methods.py:55(_any)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'replace' of 'str' objects}` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method _functools.reduce}` |
| 34 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.callable}` |
| 38 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/multiarray.py:751(dot)` |
| 15 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'pop' of 'dict' objects}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:270(transpose)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'insert' of 'list' objects}` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'transpose' of 'numpy.ndarray' objects}` |
| 12 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'join' of 'str' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:3334(matmul)` |
| 30 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:1913(_ravel_dispatcher)` |
| 24 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.iter}` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:634(__call__)` |
| 16 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'pop' of 'list' objects}` |
| 7 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_linesearch.py:27(_check_c1_c2)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/shape_base.py:78(atleast_2d)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/typing.py:2308(cast)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/enum.py:1325(value)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:474(broadcast_to)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'count' of 'str' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method _abc._abc_instancecheck}` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_numdiff.py:898(__init__)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:288(_update_other_results)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:97(_compute_tetrad_differences)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numerictypes.py:418(issubdtype)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'dot' of 'numpy.ndarray' objects}` |
| 26 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:203(_reshape_dispatcher)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'squeeze' of 'numpy.ndarray' objects}` |
| 14 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method builtins.abs}` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:629(__exit__)` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:2452(_array_equal_dispatcher)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'isdisjoint' of 'set' objects}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:552(swapaxes)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'setdefault' of 'dict' objects}` |
| 13 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2581(_all_dispatcher)` |
| 12 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'keys' of 'dict' objects}` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method numpy.promote_types}` |
| 20 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:1542(_resize_dispatcher)` |
| 7 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1090(<genexpr>)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:3520(ndim)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:452(<genexpr>)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `src/methods.py:498(__init__)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'result_type' of 'numpy._core._multiarray_umath._array_converter' objects}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'swapaxes' of 'numpy.ndarray' objects}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `{method '__exit__' of 'numpy.nditer' objects}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1093(<genexpr>)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2245(clip)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:20(__init__)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numerictypes.py:230(issubclass_)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'flatten' of 'numpy.ndarray' objects}` |
| 11 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:3044(_max_dispatcher)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:238(_assert_2d)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:25(_maybe_view_as_subclass)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'as_arrays' of 'numpy._core._multiarray_umath._array_converter' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `<frozen abc>:117(__instancecheck__)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2122(shape)` |
| 14 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/multiarray.py:115(empty_like)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:614(__enter__)` |
| 9 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:2108(_place_dispatcher)` |
| 10 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/multiarray.py:406(where)` |
| 12 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:240(_ones_like_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'any' of 'numpy.ndarray' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'conjugate' of 'numpy.ndarray' objects}` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `{method '__enter__' of 'numpy.nditer' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_sparse.py:10(issparse)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'wrap' of 'numpy._core._multiarray_umath._array_converter' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:536(__init__)` |
| 8 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:1485(_moveaxis_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:265(_is_empty_2d)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{built-in method __new__ of type object at 0x10269d918}` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1100(<genexpr>)` |
| 11 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/multiarray.py:713(result_type)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'copy' of 'numpy.ndarray' objects}` |
| 5 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1084(<genexpr>)` |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:426(<lambda>)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:161(_check_positive_definite)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:436(<genexpr>)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'discard' of 'set' objects}` |
| 7 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:919(_call_callback_maybe_halt)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:244(_assert_stacked_2d)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:325(nfev)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'lower' of 'str' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/_lib/_util.py:947(__getattr__)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/_methods.py:47(_sum)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `<string>:2(_parse_args)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1101(<genexpr>)` |
| 5 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:1094(<genexpr>)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2118(_shape_dispatcher)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:2430(_lstsq_dispatcher)` |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:548(_swapaxes_dispatcher)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'upper' of 'str' objects}` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `{method 'conj' of 'numpy.ndarray' objects}` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:176(_check_unknown_options)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_differentiable_functions.py:329(ngev)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:2611(_norm_dispatcher)` |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:584(_broadcast_arrays_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/function_base.py:22(_linspace_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:1410(_diff_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:4919(_trapezoid_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:2166(_pinv_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:3330(_matmul_dispatcher)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_stride_tricks_impl.py:470(_broadcast_to_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/numeric.py:91(_zeros_like_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/linalg/_linalg.py:1662(_svd_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:299(hess)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/scipy/optimize/_optimize.py:88(_wrap_callback)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:2240(_clip_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:3516(_ndim_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_twodim_base_impl.py:256(_diag_dispatcher)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:2683(_cov_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/einsumfunc.py:624(_einsum_path_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/fromnumeric.py:1704(_diagonal_dispatcher)` |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/_core/shape_base.py:74(_atleast_2d_dispatcher)` |
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | `venv/lib/python3.14/site-packages/numpy/lib/_function_base_impl.py:446(_average_dispatcher)` |

*Note: Cumulative times overlap across parent/child functions and must not be summed to obtain total runtime.*

### Potential bottlenecks

- `_compute_phi_s()` in `GeneralizedTetradTestGMM` is called repeatedly for a large number of times, which leads to a high total runtime despite low per-call runtime.
- `_compute_sn()` in `GeneralizedTetradTestGMM` has high per-call runtime.
- `_compute_delta_matrix()` in both `GeneralizedTetradTestGMM` and `GeneralizedTetradTestPSMD` have moderate-to-high per-call runtime.
- `_compute_sn()` in `GeneralizedTetradTestPSMD` has moderate-to-high per-call runtime.

## Computational Complexity Analysis

In this section, we analyze the computational complexity of the code before optimization. We first evaluate the empirical computational complexity of a single simulation run. We then analyze the theoretical computational complexity of each of the potential bottleneck function identified in the previous section (except `compute_phi_s()` because its per-call runtime is low). Unless otherwise specified, "computational complexity" in the section refers to time complexity.

### Computational complexity of a single simulation run

We evaluate the empirical computational complexity of a single simulation run. To do this, we ran `run_one_simulation()` with `alpha_2=0.1, beta_2=0.1, delta=0.1` and vary `num_samples` in `[500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]`. Each `num_samples` value is run for three replications with different random seeds and record the median runtime. We then regression the log of the median runtime on the log of the value of `num_samples` (i.e. the sample size).

**Result:** The raw results is stored in `profiling/results/original/complexity_overall_raw_timings_original.csv`. Aggregated results can be found in `profiling/results/original/complexity_overall_summary_original.csv` (as a summary table) and `profiling/results/original/complxity_overall_plot_original.png` (as a summary plot). The fitted regression coefficient is approximately $0.85$, which indicates a complexity of approximatelty $O^{0.85}$ for a single simulation run as a function of the sample size. It is worth noting that this analysis applies to the particular range of sample sizes tested in this experiment; it generally does not hold across all possible sample sizes because, for example, some of the functions called have $O(n^2)$ theoretical complexity.

### Computational complexity of `_compute_sn()` in `GeneralizedTetradTestGMM`

We analyze the theoretical computational complexity of `_compute_sn()` in `GeneralizedTetradTestGMM`. Let $n$ denote the sample size and $m$ denote the number of grids for numerical integration (which is fixed at $m=10000$ in the current code). Then the computational complexity for each substep in the function is:

- *Select which bridge function to use:* $O(1)$.
- *Compute `residuals`:* $O(n)$.
- *Initialize `s_grid`:* $O(m)$.
- *Initialize `integrand`:* $O(m)$.
- *Compute the integrand:* There are a total of $m$ loops. Each loop takes $O(n)$ time. Therefore, the combined complexity is $O(mn)$.
- *Compute the integral using `np.trapezoid()`:* $O(m)$.
- *Return the final result:* $O(1)$.

Combining the above analysis, the total complexity of the function is $O(mn)$.

### Computational complexity of `_compute_delta_matrix()` in `GeneralizedTetradTestGMM` and `GeneralizedTetradTestPSMD`
_
We analyze the theoretical computational complexity of `_compute_delta_matrix()` `GeneralizedTetradTestGMM` and `GeneralizedTetradTestPSMD`. The function has the same implementation in the two classes, which allows us to analyze them together. Let $n$ denote the sample size. Then the computtaional complexity for each substep in the function is:

- *Compute `abs_diff_matrix`:* $O(n^2)$ as a result of using `np.subtract.outer()`.
- *Compute `term_1`:* $O(n^2)$.
- *Compute `term_2`:* $O(n^2)$.
- *Compute and return the final delta matrix:* $O(n^2)$.

Therefore, the combined computational complexity is $O(n^2)$.

### Computational complexity of `_compute_sn()` in `GeneralizedTetradTestPSMD`

We analyze the theoretical computational complexity of `_compute_sn()` in `GeneralizedTetradTestPSMD`. Let $n$ denote the sample size, $q$ denote the number of basis functions used to estimate the PSMD bridge (which is fixed at $q=4$ in the current code), and $m$ denote the number of points in `s_grid` (applicable only when `s_grid` is not `None`). Then the computational complexity of the function is $O(n^2q+nq^2+n^2)$ when `s_grid=None`, and is $O(m(nq+q^2)+nq)$ when `s_grid` is not `None`.

## Analysis of Numerical Stability

In this section, we analyze the condition and frequency of numerical issues observed during the simulation. We analyze three parameter settings

- **Null:** `alpha_2=0, beta_2=0, delta=0`.
- **Nonlinear:** `alpha_2=0.1, beta_2=0.2, delta=0`.
- **Alternative:** `alpha_2=0, beta_2=0, delta=0.3`.
- **Extreme:** `alpha_2=10, beta_2=10, delta=10`.

For each setting, we run each of `ClassicalTetradTest`, `GeneralizedTetradTestGMM`, and `GeneralizedTetradTestPSMD` under three different sample sizes: 100, 500, and 1000. We check for three signs of potential numerical instability: the existence of exceptions, the existence of warnings, and whether the final p-value is in the range $[0,1]$. Each combination of parameter setting, tetrad test method, and sample size is run for 5 replications with different random seeds, and, for each combination, we record the number of replications that have signs of numerical instability. 

**Result:** The detailed replication-specific results can be found in `profiling/results/original/stability_detailed_original.csv`. A summary of the results can be found in `profiling/stability_summary.csv`. Across all combinations of parameter setting, tetrad test method, and sample size, none of the replications encountered exceptions, warnings, or out-of-range p-values. This suggests that the original implementation does not show evidence of numerical instability according to the conditions tested.
