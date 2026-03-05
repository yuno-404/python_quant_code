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


def test_sequence_mean_and_autocorrelation():
    module = load_module(
        "scripts/stochastic_process/stochastic_process_sequence_mean_autocorrelation.py"
    )
    sequence = np.array([1.0, -2.0, 4.0, 2.0])
    mean_value, lags, autocorr = module.mean_and_autocorrelation_full_lag(sequence)

    expected_lags = np.arange(-(sequence.size - 1), sequence.size)
    expected_autocorr = np.correlate(sequence, sequence, mode="full") / sequence.size

    assert mean_value == np.mean(sequence)
    assert np.array_equal(lags, expected_lags)
    assert np.allclose(autocorr, expected_autocorr)
