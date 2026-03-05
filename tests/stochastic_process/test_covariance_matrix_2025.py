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


def test_covariance_matrix_2025_helper_matches_manual_formula():
    module = load_module(
        "scripts/stochastic_process/stochastic_process_covariance_matrix_2025.py"
    )
    data = np.array(
        [
            [0.01, 0.00, 0.02, 0.03],
            [0.02, -0.01, 0.01, 0.02],
            [0.00, 0.01, 0.03, 0.01],
            [0.01, 0.02, 0.00, 0.02],
        ]
    )

    centered = data - data.mean(axis=0)
    expected = (centered.T @ centered) / data.shape[0]
    actual = module.covariance_matrix(data)

    assert np.allclose(actual, expected)
