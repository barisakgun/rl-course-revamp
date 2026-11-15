#!/usr/bin/env python3
"""Run the five experiments with your code (supplied; do not modify).

    python run_experiments.py

Writes ``results/results.json`` and the plots in ``results/``. The whole run
takes well under a minute on a laptop. The short answers in ``answers.md`` refer
to these outputs.
"""
import json
from pathlib import Path

import numpy as np

import control
import dp
import prediction
from rlhw import Constant, ExponentialDecay, make_env
from rlhw.data import load_dataset
from rlhw.drivers import (VisitRecorder, greedy_rollout, policy_evaluation, reachable_pairs,
                          run_prediction)
from rlhw.plotting import plot_paths, plot_prediction_errors, plot_training

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"

CONFIG = dict(
    e1=dict(layout="small", theta=1e-10),
    e2=dict(dataset="episodes_small.json", gamma=0.9, alphas=[0.05, 0.2], min_visits=10),
    e3=dict(layout="ledge", method="q_learning", alpha=0.1, n_episodes=200,
            runs=[dict(label="Q0 = 0, epsilon = 0", q0=0.0, epsilon=0.0),
                  dict(label="Q0 = +1, epsilon = 0", q0=1.0, epsilon=0.0),
                  dict(label="Q0 = 0, epsilon = 0.1", q0=0.0, epsilon=0.1),
                  # the same map with rewards in the style of the book's cliff example:
                  # -1 on every transition (also on reaching the goal), -100 for a pit
                  dict(label="Q0 = 0, epsilon = 0, book-style rewards", q0=0.0, epsilon=0.0,
                       rewards=dict(step_reward=-1.0, goal_reward=-1.0, pit_reward=-100.0))],
            coverage_at=[500, 2000], seed=0),
    e4=dict(layout="ledge", q0=1.0, alpha=0.1, epsilon=0.1, n_episodes=1000, seeds=list(range(10))),
    e5=dict(epsilon_start=0.1, epsilon_rate=0.9995),
)


def discounted(raw_returns, lengths, gamma):
    """Discounted return of each episode. Valid here because ``ledge`` gives a reward
    only on the last transition of an episode."""
    return [r * gamma ** (n - 1) for r, n in zip(raw_returns, lengths)]


def experiment_1():
    cfg = CONFIG["e1"]
    env = make_env(cfg["layout"]).unwrapped
    V, sweeps = dp.value_iteration(env.P, env.gamma, cfg["theta"])
    vi_policy = dp.policy_improvement(env.P, V, env.gamma)
    policy, V_pi, improvements, eval_sweeps = dp.policy_iteration(env.P, env.gamma, cfg["theta"])
    print("E1  value iteration:", sweeps, "sweeps;  policy iteration:", improvements,
          "improvement steps,", eval_sweeps, "evaluation sweeps")
    print(env.format_values(V))
    print(env.format_policy(policy))
    return dict(config=cfg, gamma=env.gamma, vi_values=V.tolist(), vi_sweeps=int(sweeps),
                vi_policy=[int(a) for a in vi_policy], pi_values=np.asarray(V_pi).tolist(),
                pi_policy=[int(a) for a in policy], pi_improvements=int(improvements),
                pi_evaluation_sweeps=int(eval_sweeps),
                max_value_difference=float(np.max(np.abs(V - V_pi))))


def experiment_2():
    cfg = CONFIG["e2"]
    layout, policy, episodes = load_dataset(HERE / "data" / cfg["dataset"])
    env = make_env(layout).unwrapped
    true_v, _ = policy_evaluation(env.P, policy, cfg["gamma"], 1e-12)
    # compare on the states the data visit at least `min_visits` times; a state the
    # policy never reaches cannot be learned from these episodes
    visits = np.bincount([t.state for ep in episodes for t in ep], minlength=env.n_states)
    states = [s for s in env.nonterminal_states() if visits[s] >= cfg["min_visits"]]
    curves, final = {}, {}
    for alpha in cfg["alphas"]:
        for method, kernel in (("mc", prediction.mc_update), ("td", prediction.td0_update)):
            label = f"{'MC' if method == 'mc' else 'TD(0)'}, alpha = {alpha}"
            V, errors = run_prediction(episodes, method, kernel, alpha, cfg["gamma"],
                                       env.n_states, true_v, states)
            curves[label], final[label] = errors, np.asarray(V).tolist()
    plot_prediction_errors(curves, OUT / "e2_prediction_errors.png",
                           "E2: MC and TD(0) on the same episodes")
    for label, errors in curves.items():
        print(f"E2  {label:22s} error after 10 / 100 / {len(errors)} episodes: "
              f"{errors[9]:.3f} / {errors[99]:.3f} / {errors[-1]:.3f}")
    return dict(config=cfg, compared_states=[int(s) for s in states], true_values=true_v.tolist(),
                errors=curves, final_values=final)


def experiment_3():
    cfg = CONFIG["e3"]
    pairs = reachable_pairs(make_env(cfg["layout"]))
    runs = []
    for run in cfg["runs"]:
        rewards = run.get("rewards", {})
        env = VisitRecorder(make_env(cfg["layout"], **rewards))
        base = env.unwrapped
        q0 = control.init_q(base.n_states, base.n_actions, run["q0"], base.terminal_states)
        Q, raw, lengths = control.train(env, cfg["method"], base.gamma, Constant(run["epsilon"]),
                                        Constant(cfg["alpha"]), q0, cfg["n_episodes"], cfg["seed"])
        greedy = greedy_rollout(make_env(cfg["layout"], **rewards), Q, base.gamma)
        result = dict(
            label=run["label"], q0=run["q0"], epsilon=run["epsilon"],
            rewards=dict(step=base.step_reward, goal=base.goal_reward, pit=base.pit_reward),
            transitions=int(env.total_transitions), goal_entries=int(env.goal_entries),
            pit_entries=int(env.pit_entries), first_episode_reaching_goal=env.first_goal_episode,
            coverage={str(n): env.coverage(pairs, n) for n in cfg["coverage_at"]},
            greedy_reaches_goal=greedy["reached_goal"],
            greedy_moves=greedy["moves"] if greedy["reached_goal"] else None)
        runs.append(result)
        print(f"E3  {run['label']:40s} goal reached in {result['goal_entries']:3d} of "
              f"{cfg['n_episodes']} episodes; coverage after {cfg['coverage_at'][0]} transitions: "
              f"{result['coverage'][str(cfg['coverage_at'][0])]:.2f}; greedy path: "
              f"{'%d moves' % greedy['moves'] if greedy['reached_goal'] else 'goal not reached by the cap'}")
    return dict(config=cfg, reachable_pairs=len(pairs), runs=runs)


def control_comparison(tag, title, epsilon_schedule):
    cfg = CONFIG["e4"]
    out, curves_disc, curves_pit, paths = {}, {}, {}, {}
    for method, name in (("sarsa", "SARSA"), ("q_learning", "Q-learning")):
        per_seed, disc_runs, pit_runs = [], [], []
        for seed in cfg["seeds"]:
            env = VisitRecorder(make_env(cfg["layout"]))
            base = env.unwrapped
            q0 = control.init_q(base.n_states, base.n_actions, cfg["q0"], base.terminal_states)
            Q, raw, lengths = control.train(env, method, base.gamma, epsilon_schedule,
                                            Constant(cfg["alpha"]), q0, cfg["n_episodes"], seed)
            disc = discounted(raw, lengths, base.gamma)
            greedy = greedy_rollout(make_env(cfg["layout"]), Q, base.gamma)
            disc_runs.append(disc)
            pit_runs.append([1.0 if r < 0 else 0.0 for r in raw])
            per_seed.append(dict(
                seed=seed, transitions=int(env.total_transitions),
                training_pit_frequency=env.pit_entries / cfg["n_episodes"],
                training_mean_raw_return=float(np.mean(raw)),
                training_mean_discounted_return=float(np.mean(disc)),
                last_100_pit_frequency=float(np.mean(pit_runs[-1][-100:])),
                greedy_reaches_goal=greedy["reached_goal"], greedy_moves=greedy["moves"],
                greedy_raw_return=greedy["raw_return"],
                greedy_discounted_return=greedy["discounted_return"],
                greedy_path=greedy["states"]))
        curves_disc[name], curves_pit[name] = disc_runs, pit_runs
        paths[name] = per_seed[0]["greedy_path"]
        out[method] = dict(per_seed=per_seed)
        moves = [p["greedy_moves"] if p["greedy_reaches_goal"] else None for p in per_seed]
        print(f"{tag.upper()}  {name:11s} pits in the last 100 training episodes: "
              f"{np.mean([p['last_100_pit_frequency'] for p in per_seed]):.2f}; "
              f"greedy path moves per seed: {moves}")
    plot_training(curves_disc, OUT / f"{tag}_training_discounted_return.png",
                  f"{title}: discounted return while learning", "discounted return per episode")
    plot_training(curves_pit, OUT / f"{tag}_training_pit_frequency.png",
                  f"{title}: falls while learning", "fraction of episodes ending in a pit")
    plot_paths(make_env(cfg["layout"]), paths, OUT / f"{tag}_greedy_paths.png",
               f"{title}: greedy paths after training (seed {cfg['seeds'][0]})")
    return out


def main():
    OUT.mkdir(exist_ok=True)
    results = dict(e1=experiment_1(), e2=experiment_2(), e3=experiment_3())
    cfg4, cfg5 = CONFIG["e4"], CONFIG["e5"]
    results["e4"] = dict(config=cfg4, **control_comparison(
        "e4", "E4 (constant epsilon)", Constant(cfg4["epsilon"])))
    results["e5"] = dict(config=dict(cfg4, **cfg5), **control_comparison(
        "e5", "E5 (decaying epsilon)", ExponentialDecay(cfg5["epsilon_start"], cfg5["epsilon_rate"])))
    (OUT / "results.json").write_text(json.dumps(results, indent=1))
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
