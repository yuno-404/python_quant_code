# Compute the mean and full-lag autocorrelation function of a user-input sequence.
# mu_X = (1/N) * sum(X_i),  R_XX(k) = (1/N) * sum(X_{i+k} * X_i)
# Reference: Stochastic_Process.md, "Computing Time Averages"

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def parse_sequence(text):
    return np.fromstring(text.replace(",", " "), sep=" ")


def mean_and_autocorrelation_full_lag(x):
    x_array = np.asarray(x, dtype=float)
    n_samples = x_array.size
    lags = np.arange(-(n_samples - 1), n_samples)
    # np.correlate with mode="full" computes sum(X_{i+k} * X_i); divide by N
    values = np.correlate(x_array, x_array, mode="full") / n_samples
    return float(np.mean(x_array)), lags, values


if __name__ == "__main__":
    sequence_text = input("Enter sequence values separated by spaces: ")
    sequence = parse_sequence(sequence_text)
    mean_value, lags, autocorr = mean_and_autocorrelation_full_lag(sequence)

    print("Mean:", mean_value)
    print("Autocorrelation:", np.array2string(autocorr, precision=4))

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.stem(lags, autocorr, basefmt=" ")
    ax.set(
        title="Autocorrelation of Input Sequence",
        xlabel="Lag k",
        ylabel="R_xx(k)",
    )
    ax.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
