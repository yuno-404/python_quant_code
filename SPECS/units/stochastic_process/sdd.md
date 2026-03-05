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

## 2) Data and formulas
- Use lag range `-(N-1)` to `N-1` for full correlations.
- Use denominator `N` for sequence-style correlation formulas.
- For stock tasks, fetch 2025 close-price sequences and convert to returns
  before correlation/covariance (document chosen convention in script header).

Core formulas to show in notebook (LaTeX):

$$
\mu_X = \frac{1}{N} \sum_{i=0}^{N-1} X_i
$$

$$
R_{XX}(k) = \frac{1}{N} \sum_{i=0}^{N-1+k} X_{i+k} X_i,
\quad
k = -(N-1),\ldots,(N-1)
$$

$$
R_{XY}(k) = \frac{1}{N} \sum_{i=0}^{N-1+k} X_{i+k} Y_i,
\quad
k = -(N-1),\ldots,(N-1)
$$

$$
\Sigma = \frac{1}{N}(X-\bar{X})^\top(X-\bar{X})
$$

## 2b) Requirement mapping table

| list.txt requirement | Script | Notebook section | Test file |
| --- | --- | --- | --- |
| One sequence mean + autocorrelation | `stochastic_process_sequence_mean_autocorrelation.py` | Section 1 | `tests/stochastic_process/test_sequence_mean_autocorrelation.py` |
| Two sequences auto/cross-correlation | `stochastic_process_two_sequence_correlation.py` | Section 2 | `tests/stochastic_process/test_two_sequence_correlation.py` |
| Weakly correlated US stocks A,B (2025) | `stochastic_process_weak_stock_cross_correlation_2025.py` | Section 3 | `tests/stochastic_process/test_stock_cross_correlation_2025.py` |
| Strongly correlated US stocks C,D (2025) | `stochastic_process_strong_stock_cross_correlation_2025.py` | Section 4 | `tests/stochastic_process/test_stock_cross_correlation_2025.py` |
| Covariance matrix of A,B,C,D (2025) | `stochastic_process_covariance_matrix_2025.py` | Section 5 | `tests/stochastic_process/test_covariance_matrix_2025.py` |

## 3) Notebook plan
- File: `notebooks/stochastic_process/stochastic_process_walkthrough.ipynb`
- Sections:
  1) one-sequence mean/autocorr
  2) two-sequence auto/cross-corr
  3) weak-stock pair cross-corr (2025)
  4) strong-stock pair cross-corr (2025)
  5) A/B/C/D covariance matrix
- Notebook must integrate the five script logics in one file and display formulas as LaTeX.
- Deliver notebook with executed outputs and charts visible.

## 4) Validation and quality
- Scripts must run directly from terminal.
- Clearly print selected tickers and sample window for stock scripts.
- Keep comments concise; explain only key equations and assumptions.
- Inherit global constraints from `SPECS/SDD.md` -> `Development Constraints (GBM-style)`.

## 5) Task tracking rules
- Update `SPECS/units/stochastic_process/task.md` first.
- Keep one primary `in_progress` task at a time.
- Required fields per task: `status`, `progress`, `updated_at`.
