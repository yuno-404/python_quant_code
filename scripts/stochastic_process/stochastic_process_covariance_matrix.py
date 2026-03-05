import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def covariance_matrix(data):
    data_array = np.asarray(data, dtype=float)

    # Columns are variables (X, Y, Z), rows are time observations.
    centered = data_array - np.mean(data_array, axis=0)
    n_samples = data_array.shape[0]
    return (centered.T @ centered) / n_samples


def correlation_matrix(data):
    cov = covariance_matrix(data)
    std = np.sqrt(np.diag(cov))
    return cov / np.outer(std, std)


# Lecture-note example vectors
x = np.array([1.0, 2.0, -1.0, 5.0, 1.0, 3.0, -1.0, 0.0])
y = np.array([2.0, 4.0, -1.0, 6.0, 0.0, 2.0, 0.0, -1.0])
z = np.array([-2.0, 0.0, 3.0, 0.0, 1.0, -1.0, 0.0, -2.0])

data = np.column_stack([x, y, z])
cov = covariance_matrix(data)
corr = correlation_matrix(data)

print("Covariance matrix Sigma:")
print(np.array2string(cov, precision=3))
print("\nCorrelation matrix Gamma:")
print(np.array2string(corr, precision=3))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

im0 = axes[0].imshow(cov, cmap="coolwarm")
axes[0].set_title("Covariance Matrix")
axes[0].set_xticks([0, 1, 2], ["X", "Y", "Z"])
axes[0].set_yticks([0, 1, 2], ["X", "Y", "Z"])
fig.colorbar(im0, ax=axes[0], shrink=0.85)

im1 = axes[1].imshow(corr, cmap="coolwarm", vmin=-1.0, vmax=1.0)
axes[1].set_title("Correlation Matrix")
axes[1].set_xticks([0, 1, 2], ["X", "Y", "Z"])
axes[1].set_yticks([0, 1, 2], ["X", "Y", "Z"])
fig.colorbar(im1, ax=axes[1], shrink=0.85)

plt.tight_layout()
plt.show()
