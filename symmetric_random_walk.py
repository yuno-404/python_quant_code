import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def simulate_symmetric_random_walk(n_steps, n_paths, start, seed):
    """Simulate symmetric random walk paths."""
    rng = np.random.default_rng(seed)

    # Each increment is +1 or -1 with equal probability (fair coin flip)
    increments = rng.choice(np.array([-1.0, 1.0]), size=(n_paths, n_steps))

    # Cumulative sum converts independent increments into walk positions
    cumulative = np.cumsum(increments, axis=1)

    # Prepend the starting value so output has (n_steps + 1) columns
    start_col = np.full((n_paths, 1), float(start))
    return np.concatenate([start_col, float(start) + cumulative], axis=1)


# --- Run simulation and plot ---
rw_paths = simulate_symmetric_random_walk(n_steps=200, n_paths=6, start=0.0, seed=7)

fig, ax = plt.subplots(figsize=(10, 4))
for i in range(rw_paths.shape[0]):
    ax.plot(rw_paths[i], linewidth=1.4)
ax.set(title="Symmetric Random Walk", xlabel="Step", ylabel="$M_k$")
ax.grid(True, linestyle="--", linewidth=0.5)
plt.show()
