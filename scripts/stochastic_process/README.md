# Stochastic Process Standalone Scripts

Standalone scripts aligned to `SPECS/list.txt` requirements.
Based on `Stochastic_Process/Stochastic_Process.md`.

## Scripts

- `stochastic_process_sequence_mean_autocorrelation.py`
  - Accept a user-input sequence, compute mean and full-lag autocorrelation
- `stochastic_process_two_sequence_correlation.py`
  - Accept two user-input sequences, compute autocorrelation and cross-correlation
- `stochastic_process_weak_stock_cross_correlation_2025.py`
  - Cross-correlation of weakly correlated US stocks A (XOM) and B (JNJ) for 2025
- `stochastic_process_strong_stock_cross_correlation_2025.py`
  - Cross-correlation of strongly correlated US stocks C (AAPL) and D (MSFT) for 2025
- `stochastic_process_covariance_matrix_2025.py`
  - Covariance matrix of A, B, C, D using 2025 log returns

## Run

```bash
python scripts/stochastic_process/stochastic_process_sequence_mean_autocorrelation.py
python scripts/stochastic_process/stochastic_process_two_sequence_correlation.py
python scripts/stochastic_process/stochastic_process_weak_stock_cross_correlation_2025.py
python scripts/stochastic_process/stochastic_process_strong_stock_cross_correlation_2025.py
python scripts/stochastic_process/stochastic_process_covariance_matrix_2025.py
```

## Dependencies

```bash
pip install numpy matplotlib yfinance
```
