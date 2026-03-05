import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def simulate_brownian_motion(n_steps, horizon, n_paths, start, seed):
    """Simulate standard Brownian motion (Wiener process) paths."""
    # dt is the size of each discrete time step
    dt = horizon / n_steps

    # Increments are i.i.d. Normal(0, sqrt(dt)), the defining property of
    # Brownian motion: W(t+dt) - W(t) ~ N(0, dt)
    increments = np.random.default_rng(seed).normal(
        0.0, np.sqrt(dt), (n_paths, n_steps)
    )

    # Cumulative sum of increments gives the Wiener process path;
    # prepend 0 so that W(0) = start
    return start + np.insert(np.cumsum(increments, axis=1), 0, 0, axis=1)


# --- Run simulation and plot ---
n_steps, horizon = 252, 1.0
time_axis = np.linspace(0.0, horizon, n_steps + 1)

bm_paths = simulate_brownian_motion(
    n_steps=n_steps, horizon=horizon, n_paths=6, start=0.0, seed=42
)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(time_axis, bm_paths.T, linewidth=1.4)
ax.set(title="Brownian Motion", xlabel="Time", ylabel="$W(t)$")
ax.grid(True, linestyle="--", linewidth=0.5)
plt.show()
