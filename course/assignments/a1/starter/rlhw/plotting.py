"""Plots for the experiments (supplied; do not modify)."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402


def smooth(values, window):
    values = np.asarray(values, dtype=float)
    if len(values) < window:
        return values
    return np.convolve(values, np.ones(window) / window, mode="valid")


def plot_prediction_errors(curves, path, title):
    """``curves``: dict label -> list of root-mean-square errors, one per episode."""
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    for label, errors in curves.items():
        ax.plot(range(1, len(errors) + 1), errors, label=label, linewidth=1.4)
    ax.set_xlabel("episodes processed")
    ax.set_ylabel("root-mean-square error against the true values")
    ax.set_title(title)
    ax.set_ylim(bottom=0)
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_training(curves, path, title, ylabel, window=50):
    """``curves``: dict label -> array (n_seeds, n_episodes); plots the smoothed mean over seeds."""
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    for label, runs in curves.items():
        mean = smooth(np.mean(np.asarray(runs, dtype=float), axis=0), window)
        ax.plot(np.arange(len(mean)) + window, mean, label=label, linewidth=1.4)
    ax.set_xlabel(f"episode (mean over seeds, moving average over {window} episodes)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_paths(env, paths, path, title):
    """Draw greedy paths on the grid. ``paths``: dict label -> list of states."""
    base = env.unwrapped
    fig, ax = plt.subplots(figsize=(1.0 * base.n_cols + 1.5, 1.0 * base.n_rows + 1.2))
    for r in range(base.n_rows):
        for c in range(base.n_cols):
            ch = base.grid[r][c]
            color = {"P": "#d9d9d9", "G": "#bfe3c0", "#": "#555555", "S": "#fff2bf"}.get(ch, "white")
            ax.add_patch(plt.Rectangle((c, base.n_rows - 1 - r), 1, 1, facecolor=color,
                                       edgecolor="#999999", linewidth=0.8))
            if ch in "SGP":
                ax.text(c + 0.5, base.n_rows - 0.5 - r, {"S": "start", "G": "goal", "P": "pit"}[ch],
                        ha="center", va="center", fontsize=8, color="#444444")
    offsets = np.linspace(-0.12, 0.12, max(len(paths), 2))
    for (label, states), off in zip(paths.items(), offsets):
        xs = [s % base.n_cols + 0.5 + off for s in states]
        ys = [base.n_rows - 0.5 - s // base.n_cols + off for s in states]
        ax.plot(xs, ys, marker="o", markersize=3, linewidth=1.8, label=f"{label} ({len(states) - 1} moves)")
    ax.set_xlim(0, base.n_cols)
    ax.set_ylim(0, base.n_rows)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
