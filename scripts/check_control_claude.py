#!/usr/bin/env python3
"""Check the numbers in Claude's step-1 suggestion for Week 4 (analysis/lecture_suggestions/model_free_control_claude.md).

    python3 scripts/check_control_claude.py

1. The 2x2 grid of the bellman/mc_td decks (B03: (1,1) start bottom-left, (2,1) bottom-right, (1,2) top-left,
   (2,2) goal; intended move 0.8, each perpendicular slip 0.1, walls keep the agent in place; +1 on goal entry,
   -0.04 otherwise, gamma = 0.5): q*, the always-right q-values used in the greedy lock-in example, the
   epsilon-greedy (epsilon = 0.1) optimum that constant-epsilon Sarsa approaches, and the one-transition
   Sarsa / Q-learning comparison.
2. Cliff walking (book Example 6.6: 4x12 grid, -1 per step, -100 and back to start on entering the cliff,
   undiscounted, epsilon = 0.1): exact expected return from the start when following epsilon-greedy around
   the edge (optimal) path and around the safe path, and the best epsilon-greedy policy (Sarsa's limit with
   constant epsilon, book section 5.4 'moved inside the environment' construction).
3. Cross-review of ChatGPT's suggestion (analysis/lecture_suggestions/model_free_control_review.md): its
   epsilon-greedy probabilities, MC-bridge returns, grid and cliff target snapshots, the cliff fall's action value
   under the reset rule, and whether always-left on the 2x2 grid can ever terminate.
"""
from fractions import Fraction as F
import numpy as np

ACTIONS = ['up', 'right', 'down', 'left']
MOVE = {'up': (0, 1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0)}
PERP = {'up': ('left', 'right'), 'down': ('left', 'right'), 'left': ('up', 'down'), 'right': ('up', 'down')}

# ---------------------------------------------------------------- 1. 2x2 grid
CELLS = [(1, 1), (2, 1), (1, 2)]
GOAL = (2, 2)
gamma = 0.5


def step2(s, d):
    x, y = s[0] + MOVE[d][0], s[1] + MOVE[d][1]
    return (x, y) if 1 <= x <= 2 and 1 <= y <= 2 else s


def outcomes2(s, a):
    out = {}
    for d, p in ((a, 0.8), (PERP[a][0], 0.1), (PERP[a][1], 0.1)):
        s2 = step2(s, d)
        out[s2] = out.get(s2, 0) + p
    return out


def reward2(s2):
    return 1.0 if s2 == GOAL else -0.04


def q_from_v(v):
    return {(s, a): sum(p * (reward2(s2) + gamma * (0 if s2 == GOAL else v[s2]))
                        for s2, p in outcomes2(s, a).items()) for s in CELLS for a in ACTIONS}


def evaluate(pi):  # pi[s] = {a: prob}
    n = len(CELLS); A = np.eye(n); b = np.zeros(n)
    for i, s in enumerate(CELLS):
        for a, pa in pi[s].items():
            for s2, p in outcomes2(s, a).items():
                b[i] += pa * p * reward2(s2)
                if s2 != GOAL:
                    A[i, CELLS.index(s2)] -= gamma * pa * p
    v = np.linalg.solve(A, b)
    return {s: v[i] for i, s in enumerate(CELLS)}


def eps_greedy(greedy, eps):
    return {s: {a: (1 - eps + eps / 4 if a == greedy[s] else eps / 4) for a in ACTIONS} for s in CELLS}


v = {s: 0.0 for s in CELLS}
for _ in range(500):
    q = q_from_v(v)
    v = {s: max(q[s, a] for a in ACTIONS) for s in CELLS}
qstar = q_from_v(v)
print('2x2 grid q* (gamma 0.5):')
for s in CELLS:
    print('  ', s, {a: round(qstar[s, a], 5) for a in ACTIONS})

v_right = evaluate({s: {'right': 1.0} for s in CELLS})
q_right = q_from_v(v_right)
print('always-right values (B08a/B21):', {s: round(x, 5) for s, x in v_right.items()})
print('  q^right((2,1),right) =', round(q_right[(2, 1), 'right'], 5), ' q^right((2,1),up) =',
      round(q_right[(2, 1), 'up'], 5))

# best epsilon-greedy policy (epsilon-soft optimum) by enumerating the 64 deterministic greedy choices
eps = 0.1
best = None
for g in __import__('itertools').product(ACTIONS, repeat=3):
    greedy = dict(zip(CELLS, g))
    val = evaluate(eps_greedy(greedy, eps))
    key = tuple(round(val[s], 9) for s in CELLS)
    if best is None or key[0] > best[0][0] + 1e-12:
        best = (key, greedy)
print('best epsilon-greedy (eps 0.1) greedy actions:', best[1], ' values', [round(x, 5) for x in best[0]])
pol_opt = {(1, 1): 'up', (2, 1): 'up', (1, 2): 'right'}
print('  eps-greedy around (up, up, right):', {s: round(x, 5) for s, x in evaluate(eps_greedy(pol_opt, eps)).items()})

# One-transition comparison (snapshot table; numbers chosen for the slide, not learned values)
Q12 = {'up': 0.45, 'right': 0.85, 'down': 0.25, 'left': 0.36}  # (1,2) row: q* rounded to 2 places
Q11_up, alpha, R = 0.20, 0.5, -0.04
sarsa_target = R + gamma * Q12['down']  # exploratory next action A' = down
ql_target = R + gamma * max(Q12.values())
print('transition (1,1), up, -0.04, (1,2); A\' = down (exploratory)')
print('  Sarsa target', round(sarsa_target, 4), '-> Q', round(Q11_up + alpha * (sarsa_target - Q11_up), 4))
print('  Q-learning target', round(ql_target, 4), '-> Q', round(Q11_up + alpha * (ql_target - Q11_up), 4))
print('  terminal transition (1,2), right, +1, goal: both targets 1.0')

# ---------------------------------------------------------------- 2. Cliff walking
W, H = 12, 4
START, CGOAL = (0, 0), (11, 0)
CLIFF = {(x, 0) for x in range(1, 11)}
STATES = [(x, y) for x in range(W) for y in range(H) if (x, y) not in CLIFF and (x, y) != CGOAL]


def cstep(s, a):
    x, y = min(max(s[0] + MOVE[a][0], 0), W - 1), min(max(s[1] + MOVE[a][1], 0), H - 1)
    if (x, y) in CLIFF:
        return START, -100.0
    return (x, y), -1.0


def cevaluate(pi):  # undiscounted; proper for epsilon-greedy policies that head to the goal
    n = len(STATES); A = np.eye(n); b = np.zeros(n); idx = {s: i for i, s in enumerate(STATES)}
    for s in STATES:
        for a, pa in pi[s].items():
            s2, r = cstep(s, a)
            b[idx[s]] += pa * r
            if s2 != CGOAL:
                A[idx[s], idx[s2]] -= pa
    x = np.linalg.solve(A, b)
    return {s: x[idx[s]] for s in STATES}


def ceps(greedy, e):
    return {s: {a: (1 - e + e / 4 if a == greedy[s] else e / 4) for a in ACTIONS} for s in STATES}


def path_policy(row):
    """Greedy actions: go up to `row`, right along it, then down at the last column."""
    g = {}
    for (x, y) in STATES:
        if x == W - 1:
            g[(x, y)] = 'down'
        elif y < row:
            g[(x, y)] = 'up'
        elif y > row:
            g[(x, y)] = 'down'
        else:
            g[(x, y)] = 'right'
    return g


for row, name in ((1, 'edge (optimal) path'), (2, 'middle path'), (3, 'safe path')):
    det = cevaluate({s: {a: 1.0} for s, a in path_policy(row).items()})[START]
    eg = cevaluate(ceps(path_policy(row), 0.1))[START]
    print(f'cliff {name}: greedy return {det:.0f}; epsilon-greedy (0.1) expected return {eg:.2f}')

# epsilon-soft optimum: value iteration on the environment with epsilon 'moved inside' (book section 5.4)
e = 0.1
V = {s: 0.0 for s in STATES}
for _ in range(5000):
    newV = {}
    for s in STATES:
        def qv(a):
            tot = 0.0
            for b_, pb in ((b_, (1 - e if b_ == a else 0) + e / 4) for b_ in ACTIONS):
                s2, r = cstep(s, b_)
                tot += pb * (r + (0 if s2 == CGOAL else V[s2]))
            return tot
        newV[s] = max(qv(a) for a in ACTIONS)
    V = newV
print(f'cliff best epsilon-greedy (0.1) expected return from start: {V[START]:.2f}')
print('cliff edge-step fall probability per step under epsilon 0.1: eps/|A| =', e / 4)

# ---------------------------------------------------------------- 3. Cross-review of ChatGPT's suggestion
# (analysis/lecture_suggestions/model_free_control_review.md)
print('--- cross-review checks')
print('eps-greedy, eps 0.2, 4 actions: greedy', 1 - 0.2 + 0.2 / 4, ' others', 0.2 / 4)
G = [0.0] * 4
for t, r in ((2, 1.0), (1, -0.04), (0, -0.04)):
    G[t] = r + gamma * G[t + 1]
print('right/right/right episode returns', [round(g, 4) for g in G[:3]], '(first-visit: Q((1,1),right)=G0, Q((1,2),right)=G2)')
q0, row = 0.1, {'right': 0.8, 'up': 0.2, 'down': 0.1, 'left': 0.0}
for name, nxt in (('Sarsa (A\'=up)', row['up']), ('Q-learning', max(row.values()))):
    u = -0.04 + gamma * nxt
    print(f'  ChatGPT C12 {name}: target {u:.3f} -> Q {q0 + 0.5 * (u - q0):.3f}')
for name, nxt in (('Sarsa (down=-100)', -100), ('Sarsa (down=-113)', -113), ('Q-learning (max -10)', -10)):
    u = -1 + nxt
    print(f'  cliff P03 {name}: target {u} -> Q {-20 + 0.5 * (u + 20)}')
Vstar = cevaluate({s: {a: 1.0} for s, a in path_policy(1).items()})
print('cliff q*(edge cell next to start, down) = -100 + v*(start) =', -100 + Vstar[START])

# always-left on the 2x2 grid: can an episode ever reach the goal?
reach, frontier = {(1, 1)}, [(1, 1)]
while frontier:
    s = frontier.pop()
    for s2 in outcomes2(s, 'left'):
        if s2 != GOAL and s2 not in reach:
            reach.add(s2); frontier.append(s2)
    if GOAL in outcomes2(s, 'left'):
        reach.add(GOAL)
print('always-left from (1,1) reaches:', sorted(reach, key=str), '-> goal reachable:', GOAL in reach)

# ChatGPT R15: action values of the best epsilon-greedy policy at its greedy actions vs q* (same pairs)
v_eps = evaluate(eps_greedy(pol_opt, eps))
q_eps = q_from_v(v_eps)
print('R15: q^pi_eps at greedy pairs:', {s: round(q_eps[s, pol_opt[s]], 6) for s in CELLS},
      ' q* at same pairs:', {s: round(qstar[s, pol_opt[s]], 6) for s in CELLS})
