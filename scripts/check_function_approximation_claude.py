#!/usr/bin/env python3
"""Check the numbers in Claude's step-1 suggestion for Week 5
(analysis/lecture_suggestions/function_approximation_claude.md).

    python3 scripts/check_function_approximation_claude.py

1. The 2x2 grid of the bellman/mc_td/model_free_control decks (B03: (1,1) start bottom-left, (2,1) bottom-right,
   (1,2) top-left, (2,2) goal; intended move 0.8, each perpendicular slip 0.1, walls keep the agent in place;
   +1 on goal entry, -0.04 otherwise, gamma = 0.5), evaluated for always-right (B21) and for the improved policy
   (up, right, up) (B21r).
2. 5.1 worked activity: features x(s) = (1, d(s)), d = Manhattan distance to the goal. Two semi-gradient TD(0)
   updates from w = (0.6, -0.2) with alpha = 0.1, and what they do to a cell that was never visited.
3. Representation: whether (1, d) can represent each policy's values; a sufficient feature set (1, top, right).
4. 5.2 projection on the same grid (3 states, 2 weights, as in book Figure 11.3): on-policy distribution mu for
   always-right, the mu-weighted best fit (what gradient MC approaches) and the TD fixed point (book eq. 9.12),
   with their VE; a check that the TD fixed point satisfies v = Pi B v.
5. 5.2 divergence: the w -> 2w fragment (book section 11.2), alpha = 0.1, gamma = 1 as in old VFA slide 43,
   and the three one-element changes to the deadly triad (on-policy exit transition, Monte Carlo target,
   tabular features). Also the gamma > 0.5 threshold.
6. Baird's counterexample (book Figure 11.1, eq. 11.9): semi-gradient expected (DP) updates under the uniform
   distribution versus the on-policy distribution.
"""
from fractions import Fraction as F
import numpy as np

ACTIONS = ['up', 'right', 'down', 'left']
MOVE = {'up': (0, 1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0)}
PERP = {'up': ('left', 'right'), 'down': ('left', 'right'), 'left': ('up', 'down'), 'right': ('up', 'down')}
CELLS = [(1, 1), (2, 1), (1, 2)]
GOAL = (2, 2)
GAMMA = F(1, 2)


def step(s, d):
    x, y = s[0] + MOVE[d][0], s[1] + MOVE[d][1]
    return (x, y) if 1 <= x <= 2 and 1 <= y <= 2 else s


def outcomes(s, a):
    out = {}
    for d, p in ((a, F(8, 10)), (PERP[a][0], F(1, 10)), (PERP[a][1], F(1, 10))):
        s2 = step(s, d)
        out[s2] = out.get(s2, 0) + p
    return out


def reward(s2):
    return F(1) if s2 == GOAL else F(-4, 100)


def solve(M, b):
    """Exact Gaussian elimination over Fractions."""
    n = len(b)
    A = [list(M[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [A[r][k] - f * A[c][k] for k in range(n + 1)]
    return [A[i][n] / A[i][i] for i in range(n)]


def chain(policy):
    """Transition matrix among nonterminal cells and expected reward per cell, for a deterministic policy."""
    P = [[F(0)] * 3 for _ in CELLS]
    r = [F(0)] * 3
    for i, s in enumerate(CELLS):
        for s2, p in outcomes(s, policy[s]).items():
            r[i] += p * reward(s2)
            if s2 != GOAL:
                P[i][CELLS.index(s2)] += p
    return P, r


def evaluate(policy):
    P, r = chain(policy)
    M = [[(1 if i == j else 0) - GAMMA * P[i][j] for j in range(3)] for i in range(3)]
    return solve(M, r)


def show(label, vals):
    print(f'  {label}: ' + ', '.join(f'{s} {v} ≈ {float(v):.5f}' for s, v in zip(CELLS, vals)))


RIGHT = {s: 'right' for s in CELLS}
IMPROVED = {(1, 1): 'up', (2, 1): 'up', (1, 2): 'right'}
v_right = evaluate(RIGHT)
v_improved = evaluate(IMPROVED)
print('1. Grid values (gamma 1/2)')
show('always-right (B21)', v_right)
show('improved (up, right, up) (B21r)', v_improved)
assert v_right == [F(14, 275), F(32, 275), F(46, 55)]
assert v_improved == [F(199, 550), F(469, 550), F(469, 550)]

# ---------------------------------------------------------------- 2. worked TD updates
d = {s: abs(2 - s[0]) + abs(2 - s[1]) for s in CELLS}
x = {s: (F(1), F(d[s])) for s in CELLS}


def vhat(w, s):
    return F(0) if s == GOAL else sum(wi * xi for wi, xi in zip(w, x[s]))


alpha = F(1, 10)
w = (F(6, 10), F(-2, 10))
print('\n2. Worked semi-gradient TD(0) updates, x(s) = (1, d(s)), alpha 0.1, gamma 0.5')
print('  features:', {s: tuple(int(v) for v in x[s]) for s in CELLS})
print('  w0 =', [float(v) for v in w], ' v̂:', {s: float(vhat(w, s)) for s in CELLS})
transitions = [((1, 2), 'right', F(1), GOAL), ((2, 1), 'right', F(-4, 100), (2, 1))]
for label, (s, a, r_, s2) in zip('AB', transitions):
    before = {c: vhat(w, c) for c in CELLS}
    U = r_ + GAMMA * vhat(w, s2)
    delta = U - vhat(w, s)
    w = tuple(wi + alpha * delta * xi for wi, xi in zip(w, x[s]))
    print(f'  {label}: {s} {a} -> {s2}, R = {float(r_)}: U = {float(U)}, delta = {float(delta)}, '
          f'w = {[float(v) for v in w]}')
    print('     v̂ after:', {c: float(vhat(w, c)) for c in CELLS},
          ' change:', {c: float(vhat(w, c) - before[c]) for c in CELLS})
assert w == (F(63, 100), F(-17, 100))
print('  note: the change at the updated state is alpha * delta * |x(s)|^2, e.g. 0.1 * 0.6 * 2 = 0.12 at (1,2) in A')

# ---------------------------------------------------------------- 3. representation
print('\n3. Can x = (1, d) represent the values exactly?')
for label, v in (('always-right', v_right), ('improved', v_improved)):
    same = v[1] == v[2]
    print(f'  {label}: v(2,1) = {float(v[1]):.5f}, v(1,2) = {float(v[2]):.5f} -> '
          f'{"representable" if same else "NOT representable: (2,1) and (1,2) share d = 1"}')
x3 = {s: (F(1), F(1 if s[1] == 2 else 0), F(1 if s[0] == 2 else 0)) for s in CELLS}
w3 = solve([list(x3[s]) for s in CELLS], v_right)
print('  sufficient features (1, top, right): w =', [str(v) for v in w3], '(3 independent features, 3 states)')

# ---------------------------------------------------------------- 4. projection and TD fixed point
P, r = chain(RIGHT)
h = [F(1), F(0), F(0)]  # every episode starts in (1,1)
eta = solve([[(1 if i == j else 0) - P[j][i] for j in range(3)] for i in range(3)], h)  # book eq. 9.2
mu = [e / sum(eta) for e in eta]
print('\n4. On-policy distribution for always-right (book eq. 9.2-9.3)')
print('  expected visits per episode:', {s: f'{e} ≈ {float(e):.3f}' for s, e in zip(CELLS, eta)})
print('  mu:', {s: f'{m} ≈ {float(m):.3f}' for s, m in zip(CELLS, mu)})


def ve(w_):
    return sum(m * (vv - vhat(w_, s)) ** 2 for m, vv, s in zip(mu, v_right, CELLS))


# mu-weighted least squares (projection of v^pi onto span of features)
X = [list(x[s]) for s in CELLS]
G = [[sum(mu[k] * X[k][i] * X[k][j] for k in range(3)) for j in range(2)] for i in range(2)]
g = [sum(mu[k] * X[k][i] * v_right[k] for k in range(3)) for i in range(2)]
w_mc = solve(G, g)
# TD fixed point w_TD = A^{-1} b, A = sum_s mu(s) x(s) (x(s) - gamma sum_s' P x(s'))^T, b = sum_s mu(s) r(s) x(s)
Ex_next = [[sum(P[k][j] * X[j][i] for j in range(3)) for i in range(2)] for k in range(3)]
A = [[sum(mu[k] * X[k][i] * (X[k][j] - GAMMA * Ex_next[k][j]) for k in range(3)) for j in range(2)]
     for i in range(2)]
b = [sum(mu[k] * r[k] * X[k][i] for k in range(3)) for i in range(2)]
w_td = solve(A, b)
for label, ww in (('best fit Pi v^pi (gradient MC limit)', w_mc), ('TD fixed point (semi-gradient TD limit)', w_td)):
    print(f'  {label}: w = ({float(ww[0]):.4f}, {float(ww[1]):.4f}), v̂ = '
          + ', '.join(f'{s} {float(vhat(ww, s)):.4f}' for s in CELLS) + f', VE = {float(ve(ww)):.5f}')
print('  true v^pi:', ', '.join(f'{s} {float(v):.4f}' for s, v in zip(CELLS, v_right)))
assert ve(w_td) > ve(w_mc)
# check v_TD = Pi B v_TD: apply the Bellman backup, then the mu-weighted projection
v_td = [vhat(w_td, s) for s in CELLS]
Bv = [r[k] + GAMMA * sum(P[k][j] * v_td[j] for j in range(3)) for k in range(3)]
gB = [sum(mu[k] * X[k][i] * Bv[k] for k in range(3)) for i in range(2)]
assert solve(G, gB) == w_td
print('  check: projecting B^pi v_TD returns v_TD exactly (TD fixed point solves v = Pi B^pi v)')
print('  B^pi v_TD (one backup leaves the plane):', ', '.join(f'{float(v):.4f}' for v in Bv))

# expected semi-gradient TD updates under mu converge to w_TD; under another weighting the limit moves
wt = np.zeros(2)
An = np.array(A, dtype=float); bn = np.array(b, dtype=float)
for _ in range(20000):
    wt = wt + 0.1 * (bn - An @ wt)
print('  expected TD(0) iteration under mu, alpha 0.1, 20000 steps: w =', np.round(wt, 4))
print('  eigenvalues of A (positive real parts -> stable):', np.round(np.linalg.eigvals(An), 4))

# ---------------------------------------------------------------- 5. w -> 2w divergence and the triad
print('\n5. w -> 2w fragment (book 11.2; old VFA slide 43): R = 0, alpha 0.1, gamma 1, w0 = 10')
a5, g5 = 0.1, 1.0
w5 = 10.0
seq = [w5]
for _ in range(3):
    w5 = w5 + a5 * (0 + g5 * 2 * w5 - w5) * 1
    seq.append(round(w5, 4))
print('  repeated update on the w-state only:', seq, '(factor 1 + alpha(2 gamma - 1) =', 1 + a5 * (2 * g5 - 1), ')')
for gg in (0.4, 0.5, 0.6, 0.9, 0.99):
    print(f'    gamma {gg}: factor {1 + a5 * (2 * gg - 1):.3f}')
# change 1: on-policy, the 2w-state's own transition (to a terminal, R = 0) is also updated each episode
w5, seq = 10.0, [10.0]
for _ in range(3):
    w5 = w5 + a5 * (0 + g5 * 2 * w5 - w5) * 1   # w-state -> 2w-state
    w5 = w5 + a5 * (0 + 0 - 2 * w5) * 2           # 2w-state -> terminal
    seq.append(round(w5, 4))
print('  on-policy (exit 2w -> terminal also updated): per episode', seq, 'factor', round(1.1 * 0.6, 4))
for gg in (0.9,):
    print(f'    gamma {gg}: factor {(1 + a5 * (2 * gg - 1)) * (1 - 4 * a5):.3f}')
# change 2: Monte Carlo target (return = 0) instead of bootstrapping, still only the w-state updated
w5, seq = 10.0, [10.0]
for _ in range(3):
    w5 = w5 + a5 * (0 - w5) * 1
    seq.append(round(w5, 4))
print('  Monte Carlo target G = 0:', seq, 'factor', 1 - a5)
# change 3: tabular (one weight per state), still only the first state updated
wA, wB = 10.0, 20.0
seq = [wA]
for _ in range(3):
    wA = wA + a5 * (0 + g5 * wB - wA)
    seq.append(round(wA, 4))
print('  tabular weights (wA, wB) = (10, 20), only wA updated:', seq, '-> approaches gamma*wB =', g5 * wB)

# ---------------------------------------------------------------- 6. Baird
print("\n6. Baird's counterexample (book Figure 11.1-11.2, eq. 11.9): 7 states, 8 weights, gamma 0.99, R = 0")
Xb = np.zeros((7, 8))
for i in range(6):
    Xb[i, i] = 2; Xb[i, 7] = 1
Xb[6, 6] = 1; Xb[6, 7] = 2
gb = 0.99


def baird(weights, sweeps=1000, ab=0.01):
    wb = np.array([1, 1, 1, 1, 1, 1, 10, 1], dtype=float)
    for _ in range(sweeps):
        v = Xb @ wb
        target = gb * v[6]  # target policy: solid action -> state 7, reward 0
        wb = wb + ab * sum(weights[s] * (target - v[s]) * Xb[s] for s in range(7))
    return wb


uniform = np.full(7, 1 / 7)
onpolicy = np.array([0, 0, 0, 0, 0, 0, 1.0])
print('  uniform update distribution, 1000 sweeps: w =', np.round(baird(uniform), 2))
print('  on-policy distribution (state 7 only), 1000 sweeps: w =', np.round(baird(onpolicy), 2))
wb_u = baird(uniform, 1000)
assert abs(wb_u[7]) > 10

# ---------------------------------------------------------------- 7. cross-review (function_approximation_review.md)
print('\n7. Cross-review checks')
# R04: first-visit weighting for always-right from (1,1): probability each cell is visited at least once
p21 = F(8, 9) / (1 - F(1, 81))          # (1,1) -> (2,1) w.p. 8/9; via (1,2) -> (1,1) w.p. (1/9)(1/9)
p12 = F(1, 9)                            # (1,2) is reached only directly from (1,1)
fv = [F(1), p21, p12]
fv_mu = [f / sum(fv) for f in fv]
shared = (p21 * v_right[1] + p12 * v_right[2]) / (p21 + p12)
print('  R04 first-visit weights:', [round(float(m), 5) for m in fv_mu],
      f'shared prediction at distance 1: {float(shared):.5f} (all-visit best fit: {float(vhat(w_mc, (2, 1))):.5f})')
assert abs(float(shared) - 0.19548) < 1e-5
# ChatGPT I02-I07: two states L (x = 1), R (x = 2), deterministic left/right moves, R = 0, continuing gamma 0.9
gc, ac = 0.9, 0.1
lr = lambda w_: (0 + gc * 2 * w_ - w_) * 1      # L -> R contribution (error x feature)
rr = lambda w_: (0 + gc * 2 * w_ - 2 * w_) * 2  # R -> R contribution
w7, seq = 10.0, [10.0]
for _ in range(2):
    w7 = w7 + ac * (lr(w7) + rr(w7)) / 2
    seq.append(round(w7, 4))
print('  ChatGPT I04 balanced mean update:', seq, 'multiplier', 1 + 0.2 * ac,
      f'; threshold gamma > {5 / 6:.4f}; after 100 updates w = {10 * 1.02 ** 100:.1f}')
assert seq == [10.0, 10.2, 10.404]
print('  ChatGPT I07 target-distribution (R only) multiplier', 1 + ac * rr(1.0),
      '; MC fixed labels 0, equal weighting:', 1 + ac * ((0 - 1) * 1 + (0 - 2) * 2) / 2)
print('  ChatGPT I02 fragment, gamma 0.9: 10 ->', 10 + ac * lr(10.0))
# ChatGPT F10: old MT1 landmark features (x, y, |.| to (3,3), |.| to (4,2)), alpha 0.2, gamma 0.5, R = -0.1
feat = lambda s: np.array([s[0], s[1], abs(s[0] - 3) + abs(s[1] - 3), abs(s[0] - 4) + abs(s[1] - 2)], float)
wl = np.zeros(4)
for s, s2 in (((2, 1), (2, 2)), ((2, 2), (2, 3))):
    dl = -0.1 + 0.5 * wl @ feat(s2) - wl @ feat(s)
    wl = wl + 0.2 * dl * feat(s)
    print(f'  ChatGPT F10 update {s} -> {s2}: delta {dl:.4f}, w = {np.round(wl, 4)}')
assert np.allclose(wl, [-0.012, 0.008, -0.032, -0.032])

# ---------------------------------------------------------------- 8. geometry picture options (instructor item 4)
print('\n8. Geometry picture options')
# Picture 1: grid slice. With x = (1, steps to goal), (w1, w2) -> (v̂(1,1), shared value at (2,1)/(1,2)) is one-to-one,
# so the fit decouples: (1,1) is fitted exactly, and the shared value is projected onto the diagonal of the
# (v(2,1), v(1,2)) plane with weights mu(2,1), mu(1,2).
m21, m12 = mu[1], mu[2]
proj = lambda a, c: (m21 * a + m12 * c) / (m21 + m12)
euclid = (v_right[1] + v_right[2]) / 2
print(f'  v^pi in the slice: ({float(v_right[1]):.4f}, {float(v_right[2]):.4f}); mu-weighted foot on the diagonal: '
      f'{float(proj(v_right[1], v_right[2])):.4f}; unweighted (Euclidean) foot: {float(euclid):.4f}')
assert proj(v_right[1], v_right[2]) == vhat(w_mc, (2, 1))
print(f'  TD fixed point on the diagonal: {float(v_td[1]):.4f}; one backup B^pi v_TD in the slice: '
      f'({float(Bv[1]):.4f}, {float(Bv[2]):.4f}); its mu-weighted foot: {float(proj(Bv[1], Bv[2])):.4f}')
assert proj(Bv[1], Bv[2]) == v_td[1]
# Picture 2: ChatGPT's two-state construction (x(L) = 1, x(R) = 2, gamma 0.9, target always right) with a reward
# of +1 on R -> R, so that v^pi = (9, 10) is off the representable line {(w, 2w)}
vL, vR = 0.9 * 10, 1 / (1 - 0.9)
for label, (pL, pR) in (('equal state weights', (0.5, 0.5)), ('weights (0.1, 0.9)', (0.1, 0.9))):
    wfit = (pL * vL * 1 + pR * vR * 2) / (pL * 1 + pR * 4)
    print(f'  Picture 2, v^pi = ({vL:g}, {vR:g}); best fit with {label}: w = {wfit:.4f} -> ({wfit:.4f}, {2 * wfit:.4f})')
print('  Picture 2, on-policy TD fixed point (R only): 1 + 0.9(2w) - 2w = 0 -> w = 5 -> (5, 10)')
print('\nAll checks passed.')
