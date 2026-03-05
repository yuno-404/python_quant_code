# Unit Spec: stochastic_process

## 1) Goal
Implement the Stochastic Processes program list from the project brief as
standalone scripts plus one paired notebook.

## 2) Program list (must match brief)
1. Accept an arbitrary user-input sequence, compute mean, and display
   autocorrelation.
2. Accept two arbitrary user-input sequences, display both autocorrelations
   and their cross-correlation.
3. Pick two weakly correlated US stocks A and B (year 2025), plot
   cross-correlation.
4. Pick two strongly correlated US stocks C and D (year 2025), plot
   cross-correlation.
5. Compute covariance matrix of A, B, C, and D.

## 3) Deliverables
- Scripts under `scripts/stochastic_process/`
- Notebook under `notebooks/stochastic_process/`
- Unit task board updates in `SPECS/units/stochastic_process/task.md`

## 4) Style and constraints
- Function-first implementation (no class requirement).
- Function definitions avoid sample default values when explicit input is needed.
- Add comments only for non-obvious math and assumptions.
- Use representative real market data for stock-based tasks.

## 5) Acceptance criteria
- All five program items have runnable scripts.
- Stock-correlation scripts use 2025 data and print selected tickers.
- Covariance-matrix script uses A, B, C, D from the same data window.
- One paired notebook explains formulas -> code -> figures for this unit.
