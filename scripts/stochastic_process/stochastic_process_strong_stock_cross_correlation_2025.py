# Cross-correlation of a strongly correlated US stock pair (2025).
# Uses log returns: r_t = log(S_t / S_{t-1})
# C = AAPL, D = MSFT -- both large-cap tech, high correlation expected.
# Reference: Stochastic_Process.md, "Cross Correlation"

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

plt.style.use("seaborn-v0_8")


def fetch_2025_log_returns(tickers):
    close = yf.download(
        tickers,
        start="2025-01-01",
        end="2026-01-01",
        auto_adjust=True,
        progress=False,
    )["Close"]
    # Log return: r_t = log(S_t / S_{t-1})
    return np.log(close / close.shift(1)).dropna()


def cross_correlation_full_lag(x, y):
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)
    n_samples = x_array.size
    lags = np.arange(-(n_samples - 1), n_samples)
    # R_XY(k): full-lag cross-correlation, normalized by N
    values = np.correlate(x_array, y_array, mode="full") / n_samples
    return lags, values


if __name__ == "__main__":
    c_ticker = "AAPL"
    d_ticker = "MSFT"
    returns = fetch_2025_log_returns([c_ticker, d_ticker])
    x = returns[c_ticker].to_numpy(float)
    y = returns[d_ticker].to_numpy(float)
    lags, r_cd = cross_correlation_full_lag(x, y)

    print(f"C={c_ticker}, D={d_ticker}")
    print(f"2025 return samples: {x.size}")
    print(f"Corr(C,D): {np.corrcoef(x, y)[0, 1]:.4f}")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.stem(lags, r_cd, basefmt=" ")
    ax.set(
        title=f"Cross-correlation R_CD(k): {c_ticker} vs {d_ticker} (2025)",
        xlabel="Lag k",
        ylabel="R_CD(k)",
    )
    ax.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
