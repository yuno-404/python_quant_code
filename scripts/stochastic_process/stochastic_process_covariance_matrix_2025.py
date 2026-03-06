# Compute the covariance matrix of four US stocks A, B, C, D using 2025 log returns.
# Sigma = (1/N) * (X - X_bar)^T @ (X - X_bar)
# A = XOM, B = JNJ (weak pair), C = AAPL, D = MSFT (strong pair).
# Reference: Stochastic_Process.md, "Covariance Matrix"

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


def covariance_matrix(data):
    data_array = np.asarray(data, dtype=float)
    centered = data_array - np.mean(data_array, axis=0)
    n_samples = data_array.shape[0]
    # Sigma = (1/N) * (X - X_bar)^T @ (X - X_bar)
    return (centered.T @ centered) / n_samples


if __name__ == "__main__":
    a_ticker = "XOM"
    b_ticker = "JNJ"
    c_ticker = "AAPL"
    d_ticker = "MSFT"
    tickers = [a_ticker, b_ticker, c_ticker, d_ticker]

    returns = fetch_2025_log_returns(tickers)
    matrix = returns[tickers].to_numpy(float)
    cov = covariance_matrix(matrix)

    print("Tickers:", tickers)
    print("Covariance matrix (2025 log returns):")
    print(np.array2string(cov, precision=8))

    for i, ticker in enumerate(tickers):
        print(f"{['A', 'B', 'C', 'D'][i]} = {ticker}")

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cov, cmap="coolwarm", interpolation="nearest")
    ax.set_title("Covariance Matrix of A, B, C, D (2025)")
    ax.set_xticks(range(4), ["A", "B", "C", "D"])
    ax.set_yticks(range(4), ["A", "B", "C", "D"])
    # Annotate each cell with its numeric value
    for i in range(4):
        for j in range(4):
            ax.text(j, i, f"{cov[i, j]:.2e}", ha="center", va="center", fontsize=9)
    fig.colorbar(im, ax=ax, shrink=0.85)
    plt.tight_layout()
    plt.show()
