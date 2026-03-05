import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def simulate_ar1_process(n_steps, phi, noise_std, seed):
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, noise_std, size=n_steps)

    x = np.zeros(n_steps, dtype=float)
    for t in range(1, n_steps):
        x[t] = phi * x[t - 1] + noise[t]
    return x


def simulate_random_walk(n_steps, seed):
    rng = np.random.default_rng(seed)
    increments = rng.normal(0.0, 1.0, size=n_steps)
    return np.cumsum(increments)


def rolling_mean(x, window):
    kernel = np.ones(window) / window
    return np.convolve(x, kernel, mode="valid")


def rolling_variance(x, window):
    means = rolling_mean(x, window)
    means_sq = rolling_mean(x * x, window)
    return means_sq - means * means


n_steps = 800
window = 80

# AR(1) with |phi|<1 is weak-stationary after transient phase.
stationary_path = simulate_ar1_process(n_steps=n_steps, phi=0.7, noise_std=1.0, seed=7)

# Random walk variance grows with time, so it is non-stationary.
non_stationary_path = simulate_random_walk(n_steps=n_steps, seed=7)

ar1_mean = rolling_mean(stationary_path, window=window)
rw_mean = rolling_mean(non_stationary_path, window=window)
ar1_var = rolling_variance(stationary_path, window=window)
rw_var = rolling_variance(non_stationary_path, window=window)

fig, axes = plt.subplots(2, 2, figsize=(12, 7), sharex="col")

axes[0, 0].plot(stationary_path, color="tab:blue")
axes[0, 0].set_title("Stationary Example: AR(1) Path")
axes[0, 1].plot(non_stationary_path, color="tab:red")
axes[0, 1].set_title("Non-Stationary Example: Random Walk Path")

axes[1, 0].plot(ar1_mean, label="Rolling Mean", color="tab:blue")
axes[1, 0].plot(ar1_var, label="Rolling Variance", color="tab:green")
axes[1, 0].set_title("AR(1) Rolling Moments")

axes[1, 1].plot(rw_mean, label="Rolling Mean", color="tab:red")
axes[1, 1].plot(rw_var, label="Rolling Variance", color="tab:orange")
axes[1, 1].set_title("Random Walk Rolling Moments")

for ax in axes.ravel():
    ax.grid(True, linestyle="--", linewidth=0.5)
for ax in axes[1, :]:
    ax.set_xlabel("Sample index")
    ax.legend()

plt.tight_layout()
plt.show()
