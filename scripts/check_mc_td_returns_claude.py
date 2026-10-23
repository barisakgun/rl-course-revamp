#!/usr/bin/env python3
"""Check the numbers in Claude's step-1 suggestion for session 3.2
(analysis/lecture_suggestions/mc_td_returns_claude.md).

    python3 scripts/check_mc_td_returns_claude.py

1. 2x2 grid under always-right (bellman deck B03 model: intended direction 0.8, each perpendicular slip 0.1, walls
   leave the state unchanged; entry reward +1 at the goal, -0.04 otherwise; gamma = 0.5): exact values, and the
   n-step targets on 3.1's shared trajectory (1,1) -> (1,1) -> (1,2) -> goal, starting from the table TD(0) left
   after that episode in 3.1 (V(1,1) = -0.03, V(1,2) = 0.5, V(2,1) = 0).
2. The same table: expected n-step targets E[G_{t:t+n} | S_t = s] = ((B^pi)^n V)(s) and their worst-case error
   against v^pi, compared with gamma^n times the worst error of V (book eq. 7.3).
3. Book Example 6.4 (you are the predictor): batch MC and batch TD answers.
4. Book Example 6.2 (five-state random walk): true values, the first-episode question (book Exercise 6.3), and
   learning curves over 100 seeded runs with standard errors (single runs, mean, spread), for the evaluation block.
"""
from fractions import Fraction as F
import numpy as np

# 1. Grid model under always-right.
gamma, alpha = F(1, 2), F(1, 2)
step = F(-4, 100)
states = ['(1,1)', '(2,1)', '(1,2)']
# P[s] = list of (prob, next, reward); 'goal' is terminal with value 0.
P = {
    '(1,1)': [(F(8, 10), '(2,1)', step), (F(1, 10), '(1,2)', step), (F(1, 10), '(1,1)', step)],
    '(2,1)': [(F(9, 10), '(2,1)', step), (F(1, 10), 'goal', F(1))],
    '(1,2)': [(F(8, 10), 'goal', F(1)), (F(1, 10), '(1,2)', step), (F(1, 10), '(1,1)', step)],
}


def backup(V):
    W = {s: sum(p * (r + gamma * V[s2]) for p, s2, r in P[s]) for s in states}
    W['goal'] = F(0)
    return W


# Exact v^pi by solving the linear system.
A = np.eye(3)
b = np.zeros(3)
for i, s in enumerate(states):
    for p, s2, r in P[s]:
        b[i] += float(p * r)
        if s2 != 'goal':
            A[i, states.index(s2)] -= float(p * gamma)
v = dict(zip(states, np.linalg.solve(A, b)))
print('exact v^pi:', {s: round(x, 4) for s, x in v.items()}, ' (14/275, 32/275, 46/55 =',
      round(14 / 275, 4), round(32 / 275, 4), round(46 / 55, 4), ')')

S = ['(1,1)', '(1,1)', '(1,2)', 'goal']
R = [step, step, F(1)]  # R_1, R_2, R_3
T = 3
V0 = {'(1,1)': F(-3, 100), '(2,1)': F(0), '(1,2)': F(1, 2), 'goal': F(0)}


def n_step_target(t, n, V):
    """G_{t:t+n}; equals the complete return G_t when t + n >= T."""
    end = min(t + n, T)
    g = sum(gamma ** (k - t) * R[k] for k in range(t, end))
    if t + n < T:
        g += gamma ** n * V[S[t + n]]
    return g


print('\nn-step targets from the post-3.1 TD table (no updates in between):')
for t in range(T):
    print(f'  t={t} S_t={S[t]}:', {n: float(n_step_target(t, n, V0)) for n in (1, 2, 3, 4)})

# n = 2 online: S_t is updated at time t + n (or at termination), in order, with the table as it is then.
V = dict(V0)
log = []
for tau in range(T):  # tau = time whose state is updated
    when = min(tau + 2, T)
    g = n_step_target(tau, 2, V)
    old = V[S[tau]]
    V[S[tau]] = old + alpha * (g - old)
    log.append((tau, when, float(g), float(V[S[tau]])))
print('n=2 online updates (tau, made at time, target, new value):', log)

# 2. Expected n-step targets and the gamma^n error bound.
err0 = max(abs(float(V0[s]) - v[s]) for s in states)
W = dict(V0)
print('\nworst error of V:', round(err0, 4))
for n in range(1, 6):
    W = backup(W)
    errn = max(abs(float(W[s]) - v[s]) for s in states)
    print(f'  n={n}: worst error of E[G_t:t+n] = {errn:.4f}  <=  gamma^n * {err0:.4f} = {0.5 ** n * err0:.4f}')

# 3. Example 6.4: eight episodes, no discounting.
episodes = [[('A', 0), ('B', 0)]] + [[('B', 1)]] * 6 + [[('B', 0)]]
retB = [ep[-1][1] for ep in episodes]
print('\nExample 6.4: batch MC V(B) =', F(sum(retB), len(retB)), ', V(A) = 0 (its one return is 0 + 0)')
print('  batch TD / certainty equivalence: A -> B with probability 1 and reward 0, so V(A) = V(B) =', F(6, 8))

# 4. Example 6.2: random walk A..E, start C, +1 on the right exit, gamma = 1, initial V = 0.5.
true = np.arange(1, 6) / 6
print('\nrandom walk true values:', np.round(true, 4))
print('Exercise 6.3: if the first episode exits left, TD(0) with alpha 0.1 changes only V(A), by 0.1*(0 + 0 - 0.5) =',
      0.1 * (0 - 0.5))


def run(method, a, episodes, rng):
    V = np.full(5, 0.5)
    errs = [np.sqrt(np.mean((V - true) ** 2))]
    for _ in range(episodes):
        s, traj = 2, []
        while True:
            s2 = s + (1 if rng.random() < 0.5 else -1)
            r = 1.0 if s2 == 5 else 0.0
            traj.append((s, r, s2))
            if method == 'TD':
                target = r + (0.0 if s2 in (-1, 5) else V[s2])
                V[s] += a * (target - V[s])
            if s2 in (-1, 5):
                break
            s = s2
        if method == 'MC':  # constant-alpha every-visit MC; gamma = 1 so G_t is the final reward
            G = traj[-1][1]
            for s_, _, _ in traj:
                V[s_] += a * (G - V[s_])
        errs.append(np.sqrt(np.mean((V - true) ** 2)))
    return np.array(errs)


# One declared protocol (review R34): every-visit constant-alpha MC and online TD(0); 100 runs per setting;
# TD runs use seeds 1000-1099 and MC runs seeds 2000-2099 for every alpha, so the two methods' run sets are
# independent and each quoted number below comes from exactly these runs. Intervals are pointwise normal-
# approximation 95% intervals for the MEAN RMS error at one episode, not bands containing 95% of single runs.
runs, eps = 100, 100
SEED = {'TD': 1000, 'MC': 2000}
curves = {}
for method, alphas in (('TD', (0.05, 0.1, 0.15)), ('MC', (0.01, 0.02, 0.03, 0.04))):
    for a in alphas:
        E = np.array([run(method, a, eps, np.random.default_rng(SEED[method] + k)) for k in range(runs)])
        curves[method, a] = E
        m, half = E.mean(0), 1.96 * E.std(0, ddof=1) / np.sqrt(runs)
        print(f'  {method} alpha={a}: mean RMS at episodes 10/50/100 = {m[10]:.3f}/{m[50]:.3f}/{m[100]:.3f}; '
              f'95% interval half-width for the mean at 100: {half[100]:.4f}; sd of single runs at 100: '
              f'{E[:, 100].std(ddof=1):.3f}')

# Descriptive cross-pair proportion: of the 100 x 100 pairs (one MC run, alpha 0.02; one TD run, alpha 0.1),
# the share in which the MC run ends with lower error. The pairs share runs, so this is NOT 10,000 independent
# trials; it describes how much single runs of the two methods overlap.
TDr, MCr = curves['TD', 0.1], curves['MC', 0.02]
print('\nInitial RMS error (V = 0.5):', round(float(TDr[0, 0]), 4))
for e in (25, 100):
    rev = np.mean(MCr[:, e][:, None] < TDr[:, e][None, :])
    print(f'episode {e}: cross-pair share with the MC run below the TD run = {rev:.4f}; '
          f'means TD {TDr[:, e].mean():.3f}, MC {MCr[:, e].mean():.3f}')
