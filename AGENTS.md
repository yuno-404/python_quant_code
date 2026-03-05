# AGENTS.md

Repository agent instructions for `C:\Users\ynche\python_quant_code`.

## 1) Project Intent
- This repo is script-first for quantitative finance education.
- Primary deliverables per topic:
  - one standalone `.py` script
  - one paired `.ipynb` notebook
- Main script folders:
  - `scripts/asset_price_modeling/`
  - `scripts/stochastic_process/`
- Main notebook folders:
  - `notebooks/asset_price_modeling/`
  - `notebooks/stochastic_process/`

## 2) External Rule Files Check
- `.cursorrules`: not found
- `.cursor/rules/`: not found
- `.github/copilot-instructions.md`: not found

If these appear later, treat them as additional policy inputs.

## 3) Environment Setup
```bash
python -m venv .venv
. .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install numpy matplotlib yfinance pytest ruff
```

## 4) Build / Run Commands
No package build step is required right now; run scripts directly.

Asset price modeling:
```bash
python scripts/asset_price_modeling/symmetric_random_walk.py
python scripts/asset_price_modeling/brownian_motion.py
python scripts/asset_price_modeling/geometric_brownian_motion.py
python scripts/asset_price_modeling/drift_volatility_estimation.py
python scripts/asset_price_modeling/jump_diffusion.py
```

Stochastic process:
```bash
python scripts/stochastic_process/stochastic_process_sequence_mean_autocorrelation.py
python scripts/stochastic_process/stochastic_process_two_sequence_correlation.py
python scripts/stochastic_process/stochastic_process_weak_stock_cross_correlation_2025.py
python scripts/stochastic_process/stochastic_process_strong_stock_cross_correlation_2025.py
python scripts/stochastic_process/stochastic_process_covariance_matrix_2025.py
```

Headless plotting (CI-safe):
```bash
MPLBACKEND=Agg python scripts/stochastic_process/stochastic_process_sequence_mean_autocorrelation.py
```

## 5) Lint / Format Commands
```bash
python -m ruff check scripts notebooks tests
python -m ruff format scripts tests
```

## 6) Test Commands
Use pytest when tests are present.

Run all tests:
```bash
python -m pytest -q
```

Run one file:
```bash
python -m pytest tests/test_example.py -q
```

Run a single test (important pattern):
```bash
python -m pytest tests/test_example.py::test_some_behavior -q
```

Run by keyword:
```bash
python -m pytest -k "stochastic and not slow" -q
```

## 7) Core Code Style
- Follow PEP 8.
- Prefer clarity over dense one-liners.
- Keep line length around 88 where practical.
- Use ASCII unless existing file already uses Unicode.
- Keep educational flow obvious: input -> compute -> output/plot.

## 8) Imports
- Import at top of file.
- Group order: stdlib, third-party, local.
- Separate groups with blank lines.
- Avoid wildcard imports.
- Remove unused imports before finishing.

## 9) Formatting and Layout
- Use 4 spaces indentation.
- Keep functions focused and short when practical.
- Prefer guard clauses over deeply nested conditionals.
- Use explicit intermediate variables when they improve readability.
- Add comments only for non-obvious math or assumptions.

## 10) Types and Signatures
- Function-first approach is preferred.
- Add type hints on reusable functions when feasible.
- Keep function parameters explicit.
- For instructor-facing scripts, avoid sample default values in function definitions
  when explicit input passing is required.

## 11) Naming Conventions
- Files/modules: `snake_case.py`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Notebook names should include unit/topic for easy discovery.

## 12) Error Handling
- Validate input dimensions and numeric assumptions in reusable helpers.
- Raise specific exceptions (`ValueError`, `TypeError`) with actionable messages.
- Do not silently swallow exceptions.
- For network operations (for example `yfinance`), fail clearly and explain context.

## 13) Numerical and Reproducibility Rules
- Use `numpy.random.default_rng(seed)`.
- Expose and pass `seed` explicitly for simulations.
- Document units (`dt`, horizon, annualization basis) near formulas.
- For tests, use tolerance-aware comparisons (`pytest.approx`, `np.allclose`).

## 14) Notebook / Script Consistency
- Keep formulas in notebooks aligned with script calculations.
- If script logic changes, update paired notebook section.
- Prefer notebook section pattern: formula -> code -> figure.

## 15) Git Workflow Safety
- Dual remotes:
  - `private`: `https://github.com/yuno-404/quantforme.git`
  - `public`: `https://github.com/yuno-404/python_quant_code.git`
- Mandatory pre-push document: `PUSH_WORKFLOW.md`
- Before any push, read and follow `PUSH_WORKFLOW.md`.
- Default development push target is private.
- Use explicit push commands:
```bash
git push private HEAD
git push public HEAD
```
- Never push to public unless explicitly requested.

## 16) Agent Completion Checklist
Before finalizing work:
1. Run relevant scripts/tests.
2. Run `ruff check` on changed Python files.
3. Verify `git status` has only intended changes.
4. Report what was changed and what was validated.
