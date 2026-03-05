# Software Design Document (SDD)

## Core principles
- Each topic must deliver two outputs: one `.py` script and one `.ipynb` notebook.
- Use function-first style.
- Pass parameters explicitly and avoid sample defaults in function definitions.
- Add comments only for key math steps or non-obvious logic.
- Track every task with `status`, `progress`, and `updated_at`.

## Development Constraints
1. No Type Hints
   - Do not use Python type hint syntax (for example `: str`, `: float`, `-> np.ndarray`).
2. Happy-path Only
   - Assume all inputs are valid and correctly formatted.
   - Omit defensive checks, data validation, and exception handling.
3. Minimalist Core
   - Implement only the core logic needed to achieve the requested outcome.
   - Avoid over-engineering, unnecessary abstraction, and extra modularization.
4. Strict Scope
   - Implement only explicitly requested features.
   - Do not add helper utilities, extra helper functions, or additional flows unless requested.
5. Function-first with Single Core Function
   - Prefer one primary computation function per script; keep the rest of the script linear (params -> compute -> plot/output).
6. Vectorization-first
   - Prefer NumPy vectorized operations (for example `cumsum`, `exp`) over unnecessary Python loops.
7. Essential Comments Only
   - Keep only critical comments for non-obvious formulas or assumptions.
   - Remove explanatory comments for obvious steps.
8. Reproducibility
   - Use `np.random.default_rng(seed)` for randomness.
   - Keep `seed` explicit where simulation randomness is used.

## Global Documentation Governance
- Treat this section as a global rule for all units.
- Write stable implementation rules, formulas, and requirement mapping tables in `SPECS/units/<unit_name>/sdd.md`.
- Write execution progress, status updates, issue logs, and follow-up tasks in `SPECS/units/<unit_name>/task.md`.
- For cross-unit progress, maintain `SPECS/TASK.md`.
- For notebook-heavy units, formulas should appear in the final `.ipynb` as LaTeX, and the notebook should be an integrated executable walkthrough of required scripts.
- Update task docs before starting significant work and update them again after completion.

## Minimum folder structure

```text
scripts/<unit_name>/
notebooks/<unit_name>/
SPECS/units/<unit_name>/spec.md
SPECS/units/<unit_name>/sdd.md
SPECS/units/<unit_name>/task.md
```
