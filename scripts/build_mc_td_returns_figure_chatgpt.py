#!/usr/bin/env python3
"""Shared 3.2 render asset: five-state prediction error, not a book reproduction.

Independent implementation for mc_td D13/D16. The first two seeds of each
method are selected for the individual-run panel before running the experiment.
No counterpart script is imported. Run from any directory with numpy/matplotlib.
"""
from pathlib import Path
import csv
import hashlib
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "course/lectures/week03/assets"
OUTPUT = ROOT / "output/lectures/week03"
STEM = "mc_td_returns_evaluation_chatgpt"
EPISODES = 100
RUNS = 100
# Explicitly fixed before inspecting outcomes. These are examples, not best alphas.
METHODS = {"TD(0)": (0.1, 1000), "MC": (0.02, 2000)}
SELECTED_RUN_INDICES = (0, 1)
TRUE = np.arange(1, 6, dtype=float) / 6


def experiment(method, alpha, seed):
    rng = np.random.default_rng(seed)
    values = np.full(7, 0.5)
    values[[0, 6]] = 0
    errors = [np.sqrt(np.mean((values[1:6] - TRUE) ** 2))]
    transitions = [0]
    updates = [0]
    for _ in range(EPISODES):
        state = 3
        visits = []
        steps = 0
        while state not in (0, 6):
            visits.append(state)
            successor = state + (-1 if rng.integers(0, 2) == 0 else 1)
            reward = float(successor == 6)
            if method == "TD(0)":
                values[state] += alpha * (reward + values[successor] - values[state])
            state = successor
            steps += 1
        if method == "MC":
            # gamma=1, rewards only at the right terminal: every visit's return
            # is the same final reward. Apply constant-alpha updates in visit order.
            for visited in visits:
                values[visited] += alpha * (reward - values[visited])
        errors.append(np.sqrt(np.mean((values[1:6] - TRUE) ** 2)))
        transitions.append(transitions[-1] + steps)
        updates.append(updates[-1] + steps)
        assert values[0] == values[6] == 0
        assert np.all((values >= 0) & (values <= 1))
    return np.array(errors), transitions, updates


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    arrays = {}
    records = []
    summary = {
        "description": "Course simulation of Example 6.2 task; not the book's data",
        "numpy_version": np.__version__, "generator": "numpy.default_rng (PCG64)",
        "episodes": EPISODES, "runs_per_method": RUNS,
        "gamma": 1, "initial_nonterminal_value": 0.5,
        "true_values": TRUE.tolist(), "start_state": "C",
        "rewards": "right terminal entry +1; all other transitions 0",
        "policy": "equal left/right probability", "terminal_continuation": 0,
        "mc": "constant-alpha every-visit; chronological updates after termination",
        "uncertainty": "mean +/- 1.96 * sample_sd(ddof=1) / sqrt(100); pointwise",
        "metric": "per-run root mean squared error over five states, then mean across runs",
        "selection": "first two declared seeds per method, before outcome inspection",
        "tuning": "none; two declared illustrative alpha values, no claim of optimal tuning",
        "methods": {},
    }
    for method, (alpha, first_seed) in METHODS.items():
        runs = []
        for seed in range(first_seed, first_seed + RUNS):
            errors, transitions, updates = experiment(method, alpha, seed)
            runs.append(errors)
            records.extend((method, alpha, seed, episode, float(error), transitions[episode], updates[episode])
                           for episode, error in enumerate(errors))
        errors = np.array(runs)
        mean = errors.mean(axis=0)
        half = 1.96 * errors.std(axis=0, ddof=1) / np.sqrt(RUNS)
        arrays[method] = (errors, mean, half)
        summary["methods"][method] = {
            "alpha": alpha, "seed_range": [first_seed, first_seed + RUNS - 1],
            "displayed_seeds": [first_seed + i for i in SELECTED_RUN_INDICES],
            "checkpoints": {str(e): {"mean": float(mean[e]), "half_width": float(half[e])}
                            for e in (0, 25, 100)},
        }
    for episode in (25, 100):
        _, td, td_half = arrays["TD(0)"]
        _, mc, mc_half = arrays["MC"]
        summary.setdefault("marginal_intervals_overlap", {})[str(episode)] = bool(
            max(td[episode] - td_half[episode], mc[episode] - mc_half[episode]) <=
            min(td[episode] + td_half[episode], mc[episode] + mc_half[episode]))
    csv_path = OUTPUT / f"{STEM}.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["method", "alpha", "seed", "episode", "rms_error", "cumulative_transitions", "cumulative_updates"])
        writer.writerows(records)
    summary["csv_sha256"] = hashlib.sha256(csv_path.read_bytes()).hexdigest()
    summary["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (OUTPUT / f"{STEM}.json").write_text(json.dumps(summary, indent=2) + "\n")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15, "svg.fonttype": "none"})
    fig, axes = plt.subplots(1, 2, figsize=(15, 5.3), constrained_layout=True, sharey=True)
    colors = {"TD(0)": "#245A95", "MC": "#C66B1B"}
    episodes = np.arange(EPISODES + 1)
    for method, (alpha, first_seed) in METHODS.items():
        errors, mean, half = arrays[method]
        color = colors[method]
        axes[0].plot(episodes, mean, color=color, lw=2.5, label=f"{method}, α = {alpha}")
        axes[0].fill_between(episodes, mean - half, mean + half, color=color, alpha=0.22)
        for i in SELECTED_RUN_INDICES:
            axes[1].plot(episodes, errors[i], color=color, lw=1.6,
                         linestyle="-" if i == 0 else "--", alpha=0.85,
                         label=f"{method}, seed {first_seed + i}")
    initial = float(np.sqrt(np.mean((0.5 - TRUE) ** 2)))
    assert abs(initial - np.sqrt(1 / 18)) < 1e-12
    for ax in axes:
        ax.axhline(initial, color="#666666", lw=1, ls=":")
        ax.set(xlim=(0, 100), ylim=(0, 0.38), xlabel="Training episodes")
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(frameon=False, loc="upper right", fontsize=12)
    axes[0].set_ylabel("RMS value error over five states")
    axes[0].set_title("Mean of 100 independent runs\nShading: pointwise 95% interval for the mean", fontsize=15)
    axes[1].set_title("Two preselected runs per method\nDotted line: initial error (0.236)", fontsize=15)
    for method in METHODS:
        errors = arrays[method][0]
        assert errors[list(SELECTED_RUN_INDICES)].max() <= 0.38, "Individual run is clipped"
    fig.savefig(ASSETS / f"{STEM}.svg")
    fig.savefig(ASSETS / f"{STEM}.png", dpi=180)
    plt.close(fig)
    print(json.dumps({"methods": summary["methods"], "overlap": summary["marginal_intervals_overlap"]}, indent=2))


if __name__ == "__main__":
    main()
