# Compute autocorrelation of two user-input sequences and their cross-correlation.
# R_XX(k) = (1/N) * sum(X_{i+k} * X_i)
# R_XY(k) = (1/N) * sum(X_{i+k} * Y_i)
# Reference: Stochastic_Process.md, "Computing Time Averages"

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def parse_sequence(text):
    return np.fromstring(text.replace(",", " "), sep=" ")


def autocorrelation_full_lag(x):
    x_array = np.asarray(x, dtype=float)
    n_samples = x_array.size
    lags = np.arange(-(n_samples - 1), n_samples)
    # R_XX(k): full-lag autocorrelation, normalized by N
    values = np.correlate(x_array, x_array, mode="full") / n_samples
    return lags, values


def cross_correlation_full_lag(x, y):
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)
    n_samples = x_array.size
    lags = np.arange(-(n_samples - 1), n_samples)
    # R_XY(k): full-lag cross-correlation, normalized by N
    values = np.correlate(x_array, y_array, mode="full") / n_samples
    return lags, values


if __name__ == "__main__":
    x_text = input("Enter sequence X values separated by spaces: ")
    y_text = input("Enter sequence Y values separated by spaces: ")
    x = parse_sequence(x_text)
    y = parse_sequence(y_text)

    lags, r_xx = autocorrelation_full_lag(x)
    _, r_yy = autocorrelation_full_lag(y)
    _, r_xy = cross_correlation_full_lag(x, y)

    print("R_xx:", np.array2string(r_xx, precision=4))
    print("R_yy:", np.array2string(r_yy, precision=4))
    print("R_xy:", np.array2string(r_xy, precision=4))

    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), sharex=True)
    axes[0].stem(lags, r_xx, basefmt=" ")
    axes[0].set_title("Autocorrelation R_xx(k)")
    axes[1].stem(lags, r_yy, basefmt=" ")
    axes[1].set_title("Autocorrelation R_yy(k)")
    axes[2].stem(lags, r_xy, basefmt=" ")
    axes[2].set_title("Cross-correlation R_xy(k)")
    for ax in axes:
        ax.set_xlabel("Lag k")
        ax.grid(True, linestyle="--", linewidth=0.5)
    axes[0].set_ylabel("Correlation value")
    plt.tight_layout()
    plt.show()
