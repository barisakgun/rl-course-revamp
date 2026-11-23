"""Numbers for Claude's Week 7 (policy gradients) initial suggestion.

Claude-owned check script (analysis support, not curriculum state). Every number quoted in
analysis/lecture_suggestions/policy_gradients_claude.md comes from a section below.

Running example: the short corridor with switched actions (Sutton & Barto Example 13.1,
printed p. 323 / PDF p. 345). States 1, 2, 3 (nonterminal) and G. Reward -1 per step,
gamma = 1. In state 1, left does not move; in state 2 the actions are reversed. All states
look the same to the policy, so one probability p = pi(right) is used everywhere.

Policy: softmax in action preferences with x(s, right) = (1, 0), x(s, left) = (0, 1),
theta = (theta_R, theta_L), so p = sigmoid(theta_R - theta_L).

Run: python3 scripts/check_policy_gradients_claude.py
"""

from __future__ import annotations

import math

import numpy as np

RIGHT, LEFT = 0, 1
ACTIONS = (RIGHT, LEFT)
NAMES = {RIGHT: "R", LEFT: "L"}
TERMINAL = 3  # index of G; nonterminal states are 0, 1, 2 (= states 1, 2, 3 in the book)


def step(s: int, a: int) -> int:
    """Next state (0-based nonterminal indices, 3 = G)."""
    if s == 0:
        return 1 if a == RIGHT else 0
    if s == 1:  # switched actions
        return 0 if a == RIGHT else 2
    return TERMINAL if a == RIGHT else 1


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def values(p: float) -> np.ndarray:
    """v^pi for states 1, 2, 3 (gamma = 1, reward -1 per step)."""
    P = np.zeros((3, 3))
    for s in range(3):
        for a, pa in ((RIGHT, p), (LEFT, 1 - p)):
            s2 = step(s, a)
            if s2 != TERMINAL:
                P[s, s2] += pa
    return np.linalg.solve(np.eye(3) - P, -np.ones(3))


def visits(p: float) -> np.ndarray:
    """Expected number of visits to states 1, 2, 3 per episode, starting in state 1."""
    P = np.zeros((3, 3))
    for s in range(3):
        for a, pa in ((RIGHT, p), (LEFT, 1 - p)):
            s2 = step(s, a)
            if s2 != TERMINAL:
                P[s, s2] += pa
    e = np.array([1.0, 0.0, 0.0])
    return e @ np.linalg.inv(np.eye(3) - P)


def J(p: float) -> float:
    return float(values(p)[0])


def dJdp(p: float, h: float = 1e-6) -> float:
    return (J(p + h) - J(p - h)) / (2 * h)


def score(a: int, p: float) -> np.ndarray:
    """grad_theta ln pi(a), softmax with x(right) = (1, 0), x(left) = (0, 1)."""
    return np.array([1 - p, -(1 - p)]) if a == RIGHT else np.array([-p, p])


def q_values(p: float) -> np.ndarray:
    v = values(p)
    q = np.zeros((3, 2))
    for s in range(3):
        for a in ACTIONS:
            s2 = step(s, a)
            q[s, a] = -1 + (0.0 if s2 == TERMINAL else v[s2])
    return q


def sample_episode(p: float, rng: np.random.Generator, max_len: int = 10_000):
    s, traj = 0, []
    while s != TERMINAL and len(traj) < max_len:
        a = RIGHT if rng.random() < p else LEFT
        s2 = step(s, a)
        traj.append((s, a, -1.0, s2))
        s = s2
    return traj


def reinforce_estimate(traj, p: float, baseline=None) -> np.ndarray:
    """sum_t (G_t - b(S_t)) grad ln pi(A_t | S_t), theta fixed during the episode, gamma = 1."""
    T = len(traj)
    g = np.zeros(2)
    G = 0.0
    returns = [0.0] * T
    for t in range(T - 1, -1, -1):
        G += traj[t][2]
        returns[t] = G
    for t, (s, a, _, _) in enumerate(traj):
        b = 0.0 if baseline is None else baseline(s)
        g += (returns[t] - b) * score(a, p)
    return g


def section(title: str) -> None:
    print()
    print(f"§ {title}")
    print("-" * (len(title) + 2))


def main() -> None:
    # §1 ---------------------------------------------------------------------------------------
    section("1 Short corridor: J(p) = v(start)")
    for p in (0.05, 0.25, 0.5, 0.59, 0.75, 0.95):
        print(f"p = {p:4.2f}: J = {J(p):8.2f}   v(1..3) = {np.round(values(p), 2)}")
    grid = np.linspace(0.01, 0.99, 98001)
    Js = np.array([J(p) for p in grid])
    p_star = grid[Js.argmax()]
    exact = 2 - math.sqrt(2)  # book Exercise 13.1: optimum of J(p) (checked numerically below)
    print(f"best p (grid) = {p_star:.4f}; 2 - sqrt(2) = {exact:.4f}; J(best) = {Js.max():.2f}")
    for p in (0.3, 0.5, 0.7, 0.9):
        print(f"  closed form check: J({p}) = {J(p):.4f}, 2(p-2)/(p(1-p)) = {2 * (p - 2) / (p * (1 - p)):.4f}")
    print(f"epsilon-greedy, eps = 0.1: right-greedy p = 0.95 -> {J(0.95):.1f}; "
          f"left-greedy p = 0.05 -> {J(0.05):.1f}")
    print(f"dJ/dp at 0.5 = {dJdp(0.5):.2f} (positive: more right helps at 0.5)")
    print(f"dJ/dtheta at theta = (0, 0): dJ/dp * p(1-p) * (1, -1) = "
          f"{dJdp(0.5) * 0.25:.2f} * (1, -1)")

    # §2 ---------------------------------------------------------------------------------------
    section("2 One-step (one-state, two-action) example for the derivation")
    r_R, r_L, p = 2.0, 1.0, 0.5
    true_grad = (r_R - r_L) * p * (1 - p) * np.array([1, -1])
    est_R = r_R * score(RIGHT, p)
    est_L = r_L * score(LEFT, p)
    mean = p * est_R + (1 - p) * est_L
    print(f"rewards R = {r_R}, L = {r_L}; theta = (0, 0) -> p = {p}")
    print(f"score R = {score(RIGHT, p)}, score L = {score(LEFT, p)}")
    print(f"sample R -> {est_R}; sample L -> {est_L}; mean = {mean}; exact gradient = {true_grad}")
    var = p * (est_R[0] - mean[0]) ** 2 + (1 - p) * (est_L[0] - mean[0]) ** 2
    print(f"variance of the theta_R component, no baseline: {var:.4f}")
    for b in (1.0, 1.5):
        eR = (r_R - b) * score(RIGHT, p)
        eL = (r_L - b) * score(LEFT, p)
        m = p * eR + (1 - p) * eL
        v = p * (eR[0] - m[0]) ** 2 + (1 - p) * (eL[0] - m[0]) ** 2
        print(f"baseline b = {b}: sample R -> {eR}, sample L -> {eL}, mean = {m}, variance = {v:.4f}")

    # §3 ---------------------------------------------------------------------------------------
    section("3 Sampled REINFORCE update on the corridor (theta = (0, 0), p = 0.5, alpha = 0.1)")
    # Episode: 1 -R-> 2 -R-> 1 -R-> 2 -L-> 3 -R-> G (book's switched actions in state 2)
    acts = [RIGHT, RIGHT, RIGHT, LEFT, RIGHT]
    s, traj = 0, []
    for a in acts:
        s2 = step(s, a)
        traj.append((s, a, -1.0, s2))
        s = s2
    assert s == TERMINAL
    p = 0.5
    G = [-(len(traj) - t) for t in range(len(traj))]
    print(f"episode probability at p = 0.5: {0.5 ** len(traj):.4f}")
    total = np.zeros(2)
    for t, ((st, a, r, s2), g) in enumerate(zip(traj, G)):
        term = g * score(a, p)
        total += term
        s2n = "G" if s2 == TERMINAL else s2 + 1
        print(f"t={t}: S={st + 1} A={NAMES[a]} R={r:+.0f} S'={s2n}  G_t={g:+d}  "
              f"score={score(a, p)}  G_t*score={term}")
    print(f"sum = {total}; alpha * sum = {0.1 * total}")
    th = 0.1 * total
    print(f"new theta = {th}; new p = sigmoid({th[0] - th[1]:.2f}) = {sigmoid(th[0] - th[1]):.3f}")
    print(f"J before = {J(0.5):.2f}; J after = {J(sigmoid(th[0] - th[1])):.2f}")
    print("Same episode, constant baseline b = -3 (the episode's mean return):")
    total_b = sum((g + 3) * score(a, p) for (st, a, r, s2), g in zip(traj, G))
    print(f"  sum = {total_b}")
    vb = values(0.5)
    total_v = sum((g - vb[st]) * score(a, p) for (st, a, r, s2), g in zip(traj, G))
    print(f"  baseline v^pi(S_t) at p = 0.5 (v = {np.round(vb, 2)}): sum = {np.round(total_v, 2)}")

    # §4 ---------------------------------------------------------------------------------------
    section("4 Expected REINFORCE update equals the gradient (exact, p = 0.5)")
    for p in (0.3, 0.5, 0.7):
        eta, q = visits(p), q_values(p)
        expected = sum(eta[s] * sum((p if a == RIGHT else 1 - p) * q[s, a] * score(a, p)
                                    for a in ACTIONS) for s in range(3))
        grad = dJdp(p) * p * (1 - p) * np.array([1, -1])
        print(f"p = {p}: sum_s eta(s) sum_a pi q grad ln pi = {np.round(expected, 4)}; "
              f"dJ/dtheta = {np.round(grad, 4)}; visits = {np.round(eta, 2)}, "
              f"mean length = {eta.sum():.2f}")

    # §5 ---------------------------------------------------------------------------------------
    section("5 Variance of the single-episode estimate at p = 0.5 (simulation, 100,000 episodes)")
    rng = np.random.default_rng(7)
    p = 0.5
    v = values(p)
    eta = visits(p)
    c_mu = float((eta * v).sum() / eta.sum())  # mu-weighted average value (what a 1-weight MC baseline fits)
    baselines = {
        "none": None,
        f"constant J(p) = {J(p):.1f}": (lambda s: J(0.5)),
        f"constant mu-avg v = {c_mu:.2f}": (lambda s: c_mu),
        "state value v^pi(s)": (lambda s: v[s]),
    }
    episodes = [sample_episode(p, rng) for _ in range(100_000)]
    lengths = np.array([len(e) for e in episodes])
    print(f"episode length: mean {lengths.mean():.2f}, median {np.median(lengths):.0f}, "
          f"95th pct {np.percentile(lengths, 95):.0f}")
    print(f"exact gradient theta_R component: {dJdp(p) * 0.25:.3f}")
    for name, b in baselines.items():
        est = np.array([reinforce_estimate(e, p, b)[0] for e in episodes])
        frac_neg = (est < 0).mean()
        print(f"{name:32s} mean {est.mean():7.3f}  sd {est.std():7.2f}  "
              f"share pointing the wrong way {frac_neg:.2f}")

    # §6 ---------------------------------------------------------------------------------------
    section("6 Action values and advantages at p = 0.5")
    p = 0.5
    v, q = values(p), q_values(p)
    for s in range(3):
        print(f"state {s + 1}: v = {v[s]:6.2f}; q(R) = {q[s, RIGHT]:6.2f}, q(L) = {q[s, LEFT]:6.2f}; "
              f"A(R) = {q[s, RIGHT] - v[s]:+.2f}, A(L) = {q[s, LEFT] - v[s]:+.2f}")
    print("check: sum_a pi(a) A(s, a) = 0 in every state:",
          [round(p * (q[s, 0] - v[s]) + (1 - p) * (q[s, 1] - v[s]), 10) for s in range(3)])

    # §7 ---------------------------------------------------------------------------------------
    section("7 Critic-induced bias: one-step actor-critic, gamma = 1")
    print("Expected actor update  sum_s eta(s) sum_a pi(a) E[delta | s, a] grad ln pi(a)  (theta_R part)")
    print("delta = -1 + vhat(S') - vhat(S), vhat(G) = 0")
    print(f"{'p':>5} {'true dJ/dthR':>13} {'critic v^pi':>12} {'critic const c':>15} {'c':>8}")
    for p in (0.2, 0.4, 0.5, 0.59, 0.7, 0.8, 0.9):
        eta, v = visits(p), values(p)
        c = float((eta * v).sum() / eta.sum())  # MC fit of one weight; TD(0) fixed point is -E[T]

        def expected_update(vhat) -> float:
            tot = 0.0
            for s in range(3):
                for a in ACTIONS:
                    pa = p if a == RIGHT else 1 - p
                    s2 = step(s, a)
                    delta = -1 + (0.0 if s2 == TERMINAL else vhat(s2)) - vhat(s)
                    tot += eta[s] * pa * delta * score(a, p)[0]
            return tot

        true = dJdp(p) * p * (1 - p)
        print(f"{p:5.2f} {true:13.3f} {expected_update(lambda s: v[s]):12.3f} "
              f"{expected_update(lambda s: c):15.3f} {c:8.2f}")
    print("With the constant critic every delta is -1 except entering G: -1 - c.")
    for p in (0.5, 0.59, 0.9):
        print(f"  TD(0) fixed point of a one-weight critic at p = {p}: c = -E[T] = {-visits(p).sum():.2f} "
              f"(also negative, so the bias has the same sign)")
    print("Sampled episode of §3 with c = mu-avg value at p = 0.5:")
    p = 0.5
    eta, v = visits(p), values(p)
    c = float((eta * v).sum() / eta.sum())
    tot = np.zeros(2)
    for (st, a, r, s2) in traj:
        delta = -1 + (0.0 if s2 == TERMINAL else c) - c
        tot += delta * score(a, p)
        print(f"  S={st + 1} A={NAMES[a]} delta={delta:+.2f}")
    print(f"  sum delta * score = {np.round(tot, 2)}")

    # §8 ---------------------------------------------------------------------------------------
    section("8 Exact sd of the single-episode estimate at p = 0.5 (moment recursions; replaces the §5 sample sds)")
    p = 0.5
    trans = [(s, a, step(s, a)) for s in range(3) for a in ACTIONS]
    P = np.zeros((3, 3))
    for s, a, n in trans:
        if n != TERMINAL:
            P[s, n] += 0.5

    def at(x, n):
        return 0.0 if n == TERMINAL else x[n]

    def moment(f):
        return np.linalg.solve(np.eye(3) - P,
                               np.array([sum(0.5 * f(s, a, n) for (q, a, n) in trans if q == s) for s in range(3)]))

    L = moment(lambda s, a, n: 1.0)
    L2 = moment(lambda s, a, n: 1 + 2 * at(L, n))
    for name, b in (("none", (0, 0, 0)), ("constant -12", (-12,) * 3), ("v^pi", (-12, -10, -6))):
        k = {a: score(a, p)[0] for a in ACTIONS}
        ex = moment(lambda s, a, n: k[a] * (-1 - at(L, n) - b[s]))
        exl = moment(lambda s, a, n: k[a] * (-(1 + 2 * at(L, n) + at(L2, n)) - b[s] * (1 + at(L, n))) + at(ex, n))
        ex2 = moment(lambda s, a, n: k[a] ** 2 * ((1 + b[s]) ** 2 + 2 * (1 + b[s]) * at(L, n) + at(L2, n))
                     + 2 * k[a] * (-(1 + b[s]) * at(ex, n) - at(exl, n)))
        print(f"{name:14s} mean {ex[0]:.3f}  sd {math.sqrt(ex2[0] - ex[0] ** 2):.2f}")

    # §9 ---------------------------------------------------------------------------------------
    section("9 ChatGPT's two-step fork (gamma = 1/2, preference 0)")
    rew = {"U": (4, 2), "D": (2, 0)}
    nxt = {RIGHT: "U", LEFT: "D"}
    k = {RIGHT: 0.5, LEFT: -0.5}
    pairs = [(a, b) for a in ACTIONS for b in ACTIONS]

    def fork_J(th, g):
        q = sigmoid(th)
        pr = {RIGHT: q, LEFT: 1 - q}
        return sum(pr[a] * pr[b] * (2 + g * rew[nxt[a]][b]) for a, b in pairs)

    for g in (0.5, 1.0):
        print(f"exact dJ/dtheta, gamma = {g}: {(fork_J(1e-5, g) - fork_J(-1e-5, g)) / 2e-5:.4f}")
    print("mean full return   ", sum(0.25 * (2 + rew[nxt[a]][b] / 2) * (k[a] + k[b]) for a, b in pairs))
    print("mean with gamma^t  ", sum(0.25 * ((2 + rew[nxt[a]][b] / 2) * k[a] + rew[nxt[a]][b] / 2 * k[b]) for a, b in pairs))
    print("mean, gamma^t dropped", sum(0.25 * ((2 + rew[nxt[a]][b] / 2) * k[a] + rew[nxt[a]][b] * k[b]) for a, b in pairs))
    for v in ({"U": 3, "D": 1}, {"U": 0, "D": 1}, {"U": 0, "D": 3}):
        t0 = sum(0.25 * (2 + v[nxt[a]] / 2 - 3) * k[a] for a, b in pairs)
        t1 = sum(0.25 * 0.5 * (rew[nxt[a]][b] - v[nxt[a]]) * k[b] for a, b in pairs)
        print(f"critic {v}: start {t0:+.3f}, second {t1:+.3f}, total {t0 + t1:+.3f}")


if __name__ == "__main__":
    main()
