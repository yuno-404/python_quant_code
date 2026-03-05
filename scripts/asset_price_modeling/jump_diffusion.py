import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")


def simulate_jump_diffusion(
    n_steps,
    horizon,
    n_paths,
    s0,
    drift,
    volatility,
    jump_intensity,
    jump_mean,
    jump_std,
    seed,
):
    """Simulate Merton jump-diffusion paths.

    Adds compound-Poisson jumps on top of GBM diffusion:
        dlog S = (alpha - 0.5*sigma^2 - lambda*kappa)*dt
                 + sigma*sqrt(dt)*Z + J
    where J is the sum of N~Poisson(lambda*dt) normal jumps.
    """
    dt = horizon / n_steps
    rng = np.random.default_rng(seed)

    # Continuous diffusion component: sigma * sqrt(dt) * Z
    diffusion = rng.normal(scale=volatility * np.sqrt(dt), size=(n_paths, n_steps))

    # Number of jumps in each time step follows Poisson(lambda * dt)
    n_jumps = rng.poisson(lam=jump_intensity * dt, size=(n_paths, n_steps))

    # Each jump size is Normal(jump_mean, jump_std); total jump component is
    # the sum of n_jumps independent draws, which is N(n*mu_J, sqrt(n)*sigma_J)
    jump_component = rng.normal(
        loc=n_jumps * jump_mean,
        scale=np.sqrt(n_jumps) * jump_std,
    )

    # kappa = E[exp(J_i)] - 1, used to compensate drift so that
    # the jump process does not shift the expected price level
    kappa = np.exp(jump_mean + 0.5 * jump_std**2) - 1.0
    drift_adjusted = drift - 0.5 * volatility**2 - jump_intensity * kappa

    # Combine drift, diffusion, and jumps into log-increments
    log_inc = drift_adjusted * dt + diffusion + jump_component
    log_paths = np.insert(np.cumsum(log_inc, axis=1), 0, 0, axis=1)

    return s0 * np.exp(log_paths)


# --- Run simulation: GBM (no jumps) vs jump diffusion ---
time_axis = np.linspace(0, 1.0, 252 + 1)

# Pure GBM for comparison (jump_intensity=0 turns off jumps)
gbm_paths = simulate_jump_diffusion(
    n_steps=252,
    horizon=1.0,
    n_paths=6,
    s0=100.0,
    drift=0.08,
    volatility=0.20,
    jump_intensity=0.0,
    jump_mean=0.0,
    jump_std=0.1,
    seed=42,
)

# Merton jump diffusion
jump_paths = simulate_jump_diffusion(
    n_steps=252,
    horizon=1.0,
    n_paths=6,
    s0=100.0,
    drift=0.08,
    volatility=0.20,
    jump_intensity=6.0,
    jump_mean=-0.03,
    jump_std=0.10,
    seed=42,
)

# --- Side-by-side plot ---
fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=True)
axes[0].plot(time_axis, gbm_paths.T, linewidth=1.3)
axes[1].plot(time_axis, jump_paths.T, linewidth=1.3)
axes[0].set_title("GBM (No Jumps)")
axes[1].set_title("Jump Diffusion")
for ax in axes:
    ax.set_xlabel("Time (years)")
    ax.grid(True, linestyle="--", linewidth=0.5)
axes[0].set_ylabel("Price")
plt.tight_layout()
plt.show()
