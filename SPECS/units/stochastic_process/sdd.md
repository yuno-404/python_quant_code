# Unit SDD: stochastic_process

## 1) Script plan
Implement these scripts in `scripts/stochastic_process/`:

1. `stochastic_process_sequence_mean_autocorrelation.py`
   - input: one sequence from user
   - output: mean and autocorrelation plot
2. `stochastic_process_two_sequence_correlation.py`
   - input: two sequences from user
   - output: autocorr(X), autocorr(Y), cross-corr(X,Y)
3. `stochastic_process_weak_stock_cross_correlation_2025.py`
   - input: optional ticker override; default chosen weakly correlated pair
   - output: cross-correlation plot for 2025
4. `stochastic_process_strong_stock_cross_correlation_2025.py`
   - input: optional ticker override; default chosen strongly correlated pair
   - output: cross-correlation plot for 2025
5. `stochastic_process_covariance_matrix_2025.py`
   - input: four tickers A/B/C/D
   - output: covariance matrix print + heatmap

## 2) Existing script mapping
Current scripts already present:
- `stochastic_process_discrete_correlation.py`
- `stochastic_process_covariance_matrix.py`
- `stochastic_process_time_averages.py`
- `stochastic_process_stationarity_demo.py`

These cover lecture examples, but not yet all five brief items (especially
2025 stock correlation tasks and arbitrary user input handling).

## 3) Data and formulas
- Use lag range `-(N-1)` to `N-1` for full correlations.
- Use denominator `N` for sequence-style correlation formulas.
- For stock tasks, fetch 2025 close-price sequences and convert to returns
  before correlation/covariance (document chosen convention in script header).

## 4) Notebook plan
- File: `notebooks/stochastic_process/stochastic_process_walkthrough.ipynb`
- Sections:
  1) one-sequence mean/autocorr
  2) two-sequence auto/cross-corr
  3) weak-stock pair cross-corr (2025)
  4) strong-stock pair cross-corr (2025)
  5) A/B/C/D covariance matrix

## 5) Validation and quality
- Scripts must run directly from terminal.
- Clearly print selected tickers and sample window for stock scripts.
- Keep comments concise; explain only key equations and assumptions.

## 6) Task tracking rules
- Update `SPECS/units/stochastic_process/task.md` first.
- Keep one primary `in_progress` task at a time.
- Required fields per task: `status`, `progress`, `updated_at`.
