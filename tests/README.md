# tests

Automated tests for script-first workflow.

## Structure
- Keep tests grouped by unit folder.
- Current unit folder: `tests/stochastic_process/`.
- Use one test file per feature area (not one flat global test file).

## Scope rules
- Tests must validate behavior required by `SPECS/list.txt`.
- Prefer testing reusable computation helpers from scripts.
- Keep tests deterministic and fast.
