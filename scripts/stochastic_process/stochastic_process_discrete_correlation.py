import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def sample_mean(x):
    return float(np.mean(np.asarray(x, dtype=float)))


def autocorrelation_full_lag(x):
    x_array = np.asarray(x, dtype=float)
    n_samples = x_array.size
    lags = np.arange(-(n_samples - 1), n_samples)
    values = np.correlate(x_array, x_array, mode="full") / n_samples
    return lags, values


def cross_correlation_full_lag(x, y):
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)
    n_samples = x_array.size
    lags = np.arange(-(n_samples - 1), n_samples)
    values = np.correlate(x_array, y_array, mode="full") / n_samples
    return lags, values


# Lecture-note example vectors
x = np.array([1.0, -2.0, 4.0, 2.0])
y = np.array([-2.0, 3.0, 1.0, 5.0])

lags, r_xx = autocorrelation_full_lag(x)
_, r_xy = cross_correlation_full_lag(x, y)
_, r_yx = cross_correlation_full_lag(y, x)

print("X:", x)
print("Y:", y)
print("mu_X =", sample_mean(x))
print("R_XX =", np.array2string(r_xx, precision=2))
print("R_XY =", np.array2string(r_xy, precision=2))
print("R_YX =", np.array2string(r_yx, precision=2))

fig, axes = plt.subplots(1, 3, figsize=(13, 3.6), sharex=True)
axes[0].stem(lags, r_xx, basefmt=" ")
axes[0].set_title("Autocorrelation R_XX(k)")
axes[1].stem(lags, r_xy, basefmt=" ")
axes[1].set_title("Cross-correlation R_XY(k)")
axes[2].stem(lags, r_yx, basefmt=" ")
axes[2].set_title("Cross-correlation R_YX(k)")

for ax in axes:
    ax.set_xlabel("Lag k")
    ax.grid(True, linestyle="--", linewidth=0.5)
axes[0].set_ylabel("Correlation value")

plt.tight_layout()
plt.show()
