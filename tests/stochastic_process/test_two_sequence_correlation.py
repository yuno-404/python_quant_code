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


def test_two_sequence_auto_and_cross_correlation():
    module = load_module(
        "scripts/stochastic_process/stochastic_process_two_sequence_correlation.py"
    )
    x = np.array([1.0, -2.0, 4.0, 2.0])
    y = np.array([-2.0, 3.0, 1.0, 5.0])

    lags, r_xx = module.autocorrelation_full_lag(x)
    _, r_yy = module.autocorrelation_full_lag(y)
    _, r_xy = module.cross_correlation_full_lag(x, y)

    expected_lags = np.arange(-(x.size - 1), x.size)
    assert np.array_equal(lags, expected_lags)
    assert np.allclose(r_xx, np.correlate(x, x, mode="full") / x.size)
    assert np.allclose(r_yy, np.correlate(y, y, mode="full") / y.size)
    assert np.allclose(r_xy, np.correlate(x, y, mode="full") / x.size)
