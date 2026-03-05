import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

plt.style.use("seaborn-v0_8")


def estimate_drift_and_volatility(prices, dt):
    """Return (alpha, sigma) — annualised drift and volatility from a price series.

    Uses the MLE-style estimator based on log-returns:
        r_j = log(S_{j+1} / S_j)
        sigma^2 = Var(r) / dt
        alpha   = Mean(r) / dt + 0.5 * sigma^2   (Ito correction)
    """
    # Log-returns: r_j = log(S_{j+1}) - log(S_j)
    returns = np.diff(np.log(prices))

    # Annualised variance (sample variance with ddof=1), floored at 0
    sigma2 = max(returns.var(ddof=1) / dt, 0.0)

    # Annualised drift includes the +0.5*sigma^2 Ito correction
    alpha = returns.mean() / dt + 0.5 * sigma2

    return alpha, np.sqrt(sigma2)


# --- Fetch real market data (AAPL, 2 years of monthly closes) ---
symbol = "AAPL"
dt = 1 / 12  # monthly data → dt = 1/12 year

hist = yf.Ticker(symbol).history(period="2y", interval="1mo", auto_adjust=True)
prices = hist["Close"].dropna().to_numpy(float)

# --- Estimate drift and volatility ---
alpha, sigma = estimate_drift_and_volatility(prices, dt)
returns = np.diff(np.log(prices))

print(f"Symbol: {symbol}  |  {prices.size} monthly data points")
print(f"Estimated annualised drift (alpha):      {alpha:.4f}")
print(f"Estimated annualised volatility (sigma): {sigma:.4f}")

# --- Plot: price path and log-return histogram ---
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(prices, color="tab:blue", linewidth=2.0, marker="o")
axes[1].hist(returns, bins=8, color="tab:green", alpha=0.85, edgecolor="black")

axes[0].set(
    title=f"Real {symbol} Monthly Close Path",
    xlabel="Month index",
    ylabel="Price (USD)",
)
axes[1].set(
    title="Monthly Log-Return Histogram",
    xlabel="Log Return",
    ylabel="Frequency",
)
for ax in axes:
    ax.grid(True, linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
