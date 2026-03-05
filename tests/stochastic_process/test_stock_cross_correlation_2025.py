from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np


def load_module(relative_path):
    root = Path(__file__).resolve().parents[2]
    module_path = root / relative_path
    spec = spec_from_file_location(module_path.stem, module_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_stock_cross_correlation_helpers_match_formula():
    weak_module = load_module(
        "scripts/stochastic_process/stochastic_process_weak_stock_cross_correlation_2025.py"
    )
    strong_module = load_module(
        "scripts/stochastic_process/stochastic_process_strong_stock_cross_correlation_2025.py"
    )
    x = np.array([0.01, -0.02, 0.03, 0.01, -0.01])
    y = np.array([0.00, -0.01, 0.02, 0.02, -0.02])

    lags_weak, values_weak = weak_module.cross_correlation_full_lag(x, y)
    lags_strong, values_strong = strong_module.cross_correlation_full_lag(x, y)
    expected_lags = np.arange(-(x.size - 1), x.size)
    expected_values = np.correlate(x, y, mode="full") / x.size

    assert np.array_equal(lags_weak, expected_lags)
    assert np.array_equal(lags_strong, expected_lags)
    assert np.allclose(values_weak, expected_values)
    assert np.allclose(values_strong, expected_values)
