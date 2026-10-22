#!/usr/bin/env python3
"""Check the numbers in Claude's step-1 suggestion for session 3.1 (analysis/lecture_suggestions/mc_td_claude.md).

    python3 scripts/check_mc_td_claude.py

1. Shared 2x2-grid trajectory under always-right (bellman deck B03 model: entry reward +1 at the goal, -0.04
   otherwise, gamma = 0.5): returns, constant-alpha first-visit MC and TD(0) updates (alpha = 0.5, V = 0).
2. Recycling robot, continuing rescue model (mdp_values deck M02/M07): long-run state fractions, average reward
   r(pi) of the two familiar policies, discounted values for several gamma, and the identity
   sum_s mu(s) (1 - gamma) v(s) = r(pi) (book section 10.4; notes only).
3. Cross-review of ChatGPT's suggestion (analysis/lecture_suggestions/mc_td_review.md): its shared trajectory
   (1,1) -> (1,1) -> (1,2) -> goal, its fixed-snapshot n-step targets and its continuing service example.
"""
from fractions import Fraction as F
import numpy as np

# 1. Shared trajectory: (1,1) -right-> (2,1); (2,1) bumps and stays; (2,1) slips up into the goal.
gamma, alpha = F(1, 2), F(1, 2)
S = ['(1,1)', '(2,1)', '(2,1)', 'goal']
R = [F(-4, 100), F(-4, 100), F(1)]  # R_1, R_2, R_3
prob = F(8, 10) * F(9, 10) * F(1, 10)
G = [F(0)] * 4
for t in (2, 1, 0):
    G[t] = R[t] + gamma * G[t + 1]
print('trajectory probability', float(prob))
print('returns G_0, G_1, G_2:', [float(g) for g in G[:3]])

mc = {'(1,1)': F(0), '(2,1)': F(0), 'goal': F(0)}
seen = set()
for t in range(3):
    if S[t] not in seen:
        seen.add(S[t])
        mc[S[t]] += alpha * (G[t] - mc[S[t]])
print('first-visit MC, alpha 0.5:', {k: float(v) for k, v in mc.items() if k != 'goal'})

td = {'(1,1)': F(0), '(2,1)': F(0), 'goal': F(0)}
for episode in (1, 2):
    for t in range(3):
        delta = R[t] + gamma * td[S[t + 1]] - td[S[t]]
        td[S[t]] += alpha * delta
        if episode == 1:
            print(f'TD t={t}: delta={float(delta)}', {k: float(v) for k, v in td.items() if k != 'goal'})
    if episode == 1:
        print('TD after episode 1:', {k: float(v) for k, v in td.items() if k != 'goal'})
print('TD after the same episode again (notes only):', {k: float(v) for k, v in td.items() if k != 'goal'})
print('exact v^pi (bellman B08a/B21): (1,1) 14/275 =', 14 / 275, ' (2,1) 32/275 =', 32 / 275)


# 2. Recycling robot, continuing rescue model. States (high, low).
def policy_model(low_action):
    if low_action == 'search':
        P = np.array([[0.8, 0.2], [0.3, 0.7]]); r = np.array([2.0, 0.7 * 2 + 0.3 * -3])
    else:  # recharge at low
        P = np.array([[0.8, 0.2], [1.0, 0.0]]); r = np.array([2.0, 0.0])
    return P, r


for name, low in (('always search', 'search'), ('search high / recharge low', 'recharge')):
    P, r = policy_model(low)
    w, vec = np.linalg.eig(P.T)
    mu = np.real(vec[:, np.argmin(abs(w - 1))]); mu /= mu.sum()
    print(f'{name}: long-run fractions (high, low) = {mu.round(4)}, r(pi) = {mu @ r:.4f}')
    for g in (0.1, 0.3, 0.4, 0.5, 0.9):
        v = np.linalg.solve(np.eye(2) - g * P, r)
        print(f'   gamma {g}: v = {v.round(3)}, sum mu (1-gamma) v = {(1 - g) * mu @ v:.4f}')


# 3. ChatGPT's suggestion: trajectory (1,1) bumps (slip down) -> (1,1) slips up -> (1,2) -> goal.
S = ['(1,1)', '(1,1)', '(1,2)', 'goal']
prob = F(1, 10) * F(1, 10) * F(8, 10)
G = [F(0)] * 4
for t in (2, 1, 0):
    G[t] = R[t] + gamma * G[t + 1]
print('\nChatGPT trajectory probability', float(prob), 'returns', [float(g) for g in G[:3]],
      'every-visit sample mean (1,1)', float((G[0] + G[1]) / 2))
mc = {'(1,1)': F(0), '(1,2)': F(0), 'goal': F(0)}
seen = set()
for t in range(3):
    if S[t] not in seen:
        seen.add(S[t])
        mc[S[t]] += alpha * (G[t] - mc[S[t]])
td = {'(1,1)': F(0), '(1,2)': F(0), 'goal': F(0)}
for t in range(3):
    td[S[t]] += alpha * (R[t] + gamma * td[S[t + 1]] - td[S[t]])
print('first-visit MC', {k: float(v) for k, v in mc.items() if k != 'goal'},
      'TD', {k: float(v) for k, v in td.items() if k != 'goal'}, 'exact (1,2) 46/55 =', 46 / 55)
snap = {'(1,1)': F(2, 10), '(1,2)': F(4, 10), 'goal': F(0)}
print('n-step targets at t=0 from snapshot:', float(R[0] + gamma * snap[S[1]]),
      float(R[0] + gamma * R[1] + gamma ** 2 * snap[S[2]]), float(G[0]))
# Service example: steady 0.8 forever vs 0, 2, 0, 2, ... (periodic), from ready, gamma = 0.5.
print('service: r = 0.8 vs 1; discounted from ready', 0.8 / (1 - 0.5), sum(2 * 0.5 ** k for k in range(1, 200, 2)),
      '; E[R_t] for the alternating policy oscillates (0, 2), so only the time average exists')
