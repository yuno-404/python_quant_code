# Cross-correlation of a weakly correlated US stock pair (2025).
# Uses log returns: r_t = log(S_t / S_{t-1})
# A = XOM (Energy), B = JNJ (Healthcare) -- different sectors, low correlation expected.
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
    a_ticker = "XOM"
    b_ticker = "JNJ"
    returns = fetch_2025_log_returns([a_ticker, b_ticker])
    x = returns[a_ticker].to_numpy(float)
    y = returns[b_ticker].to_numpy(float)
    lags, r_ab = cross_correlation_full_lag(x, y)

    print(f"A={a_ticker}, B={b_ticker}")
    print(f"2025 return samples: {x.size}")
    print(f"Corr(A,B): {np.corrcoef(x, y)[0, 1]:.4f}")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.stem(lags, r_ab, basefmt=" ")
    ax.set(
        title=f"Cross-correlation R_AB(k): {a_ticker} vs {b_ticker} (2025)",
        xlabel="Lag k",
        ylabel="R_AB(k)",
    )
    ax.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
