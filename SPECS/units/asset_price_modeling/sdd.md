# Unit SDD: asset_price_modeling

## 1) Deliverables
- Scripts: `scripts/asset_price_modeling/*.py`
- Notebooks: `notebooks/asset_price_modeling/*.ipynb`

## 2) Script set
- `symmetric_random_walk.py`
- `brownian_motion.py`
- `geometric_brownian_motion.py`
- `drift_volatility_estimation.py`
- `jump_diffusion.py`

## 3) Notebook set
- `asset_price_modeling_standalone_simple.ipynb`
- `asset_price_modeling_standalone.ipynb`

## 4) Validation
- Every script runs directly via `python scripts/asset_price_modeling/<file>.py`.
- Drift/volatility script uses representative US stock data.

## 5) Rules
- Function-first implementation.
- No sample defaults in function definitions.
- Terminal-runnable scripts.
