import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def simulate_gbm(n_steps, horizon, n_paths, s0, drift, volatility, seed):
    """Simulate Geometric Brownian Motion paths via the log-return scheme."""
    dt = horizon / n_steps

    # Standard normal draws driving the diffusion
    z = np.random.default_rng(seed).standard_normal((n_paths, n_steps))

    # Discretised log-return: (alpha - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z
    # The -0.5*sigma^2 term is Ito's correction so that E[S(t)] = s0*exp(alpha*t)
    log_inc = (drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z

    # Exponentiate cumulative log-returns to recover price paths
    return s0 * np.exp(np.insert(np.cumsum(log_inc, axis=1), 0, 0, axis=1))


# --- Run simulation and plot ---
gbm_paths = simulate_gbm(
    n_steps=252,
    horizon=1.0,
    n_paths=6,
    s0=100.0,
    drift=0.08,
    volatility=0.25,
    seed=42,
)

time_axis = np.linspace(0, 1.0, 253)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(time_axis, gbm_paths.T, linewidth=1.4)
ax.set(title="Geometric Brownian Motion", xlabel="Time (years)", ylabel="Price")
ax.grid(True, linestyle="--", linewidth=0.5)
plt.show()
