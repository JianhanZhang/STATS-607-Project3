PYTHON ?= python3
RAW_DIR := results/raw
FIG_DIR := results/figures

.PHONY: all simulate analyze figures test clean

all:
	$(MAKE) simulate
	$(MAKE) analyze
	$(MAKE) figures

simulate:
	mkdir -p $(RAW_DIR)
	$(PYTHON) -m src.simulation

analyze:
	$(PYTHON) -m src.analyze

figures:
	mkdir -p $(FIG_DIR)
	$(PYTHON) -m src.visualization

test:
	$(PYTHON) -m pytest

clean:
	rm -f $(RAW_DIR)/raw_results_*.csv $(RAW_DIR)/results_*.csv
	rm -f $(FIG_DIR)/*.png $(FIG_DIR)/*.pdf

profile:
	$(PYTHON) -m profiling.code.original.profiling_bottleneck_original
	$(PYTHON) -m profiling.code.optimized.profiling_bottleneck_optimized

complexity:
	$(PYTHON) -m profiling.code.original.profiling_complexity_overall_original
	$(PYTHON) -m profiling.code.optimized.profiling_complexity_overall_optimized

benchmark:
	$(PYTHON) -m profiling.code.comparison.profiling_comparison_visualizations

parallel:
	$(PYTHON) -m src.simulation_optimized

stability-check:
	$(PYTHON) -m profiling.code.original.profiling_instability_original
	$(PYTHON) -m profiling.code.optimized.profiling_instability_optimized