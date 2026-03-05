import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def simulate_ar1_process(n_steps, phi, noise_std, seed):
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, noise_std, size=n_steps)

    x = np.zeros(n_steps, dtype=float)
    for t in range(1, n_steps):
        # AR(1): X_t = phi * X_{t-1} + epsilon_t
        x[t] = phi * x[t - 1] + noise[t]
    return x


def running_time_average(x):
    x_array = np.asarray(x, dtype=float)
    cumulative = np.cumsum(x_array)
    counts = np.arange(1, x_array.size + 1)
    return cumulative / counts


def time_autocorrelation_at_lag(x, lag):
    x_array = np.asarray(x, dtype=float)
    n_samples = x_array.size

    # Discrete-time equivalent of the time autocorrelation integral.
    return float(np.sum(x_array[lag:] * x_array[: n_samples - lag]) / n_samples)


n_steps = 2000
phi = 0.8
noise_std = 1.0
seed = 42

path = simulate_ar1_process(n_steps=n_steps, phi=phi, noise_std=noise_std, seed=seed)
running_mean = running_time_average(path)

lags = np.arange(0, 21)
time_auto = np.array([time_autocorrelation_at_lag(path, lag) for lag in lags])

print("Final running mean (T -> large):", round(float(running_mean[-1]), 4))
print("Time autocorrelation R_xx(0..20):")
print(np.array2string(time_auto, precision=4))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(running_mean, color="tab:blue")
axes[0].axhline(0.0, color="black", linestyle="--", linewidth=1.0)
axes[0].set_title("Running Time Average")
axes[0].set_xlabel("Sample index")
axes[0].set_ylabel("Average")
axes[0].grid(True, linestyle="--", linewidth=0.5)

axes[1].stem(lags, time_auto, basefmt=" ")
axes[1].set_title("Time Autocorrelation")
axes[1].set_xlabel("Lag k")
axes[1].set_ylabel("R_xx(k)")
axes[1].grid(True, linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
