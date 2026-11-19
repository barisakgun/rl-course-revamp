#!/usr/bin/env python3
"""Check the numbers in Claude's step-1 suggestion for Week 6
(analysis/lecture_suggestions/deep_q_learning_claude.md).

    python3 scripts/check_deep_q_learning_claude.py

1. 6.1 worked trace (A12-A13): a three-position corridor with two actions and q-hat(s, a, w) = w_a . (1, position).
   One DQN loop: act, store, sample a minibatch, build targets from the target weights (with a terminal
   transition), TD errors, loss, one minibatch step, and the target-network copy. Also what the same targets
   would be if they were computed from the online weights, and the missing-terminal-mask bug.
2. 6.1 target-network motivation (A08-A09): the Week 5 fragment I02 (v-hat = (w, 2w), reward 0, gamma = 0.9,
   alpha = 0.1, w = 10), updated with a target that moves every step versus a target frozen for C = 5 updates.
3. 6.1 replay motivation (A05): one shared weight, two groups of samples with targets +1 and -1, alpha = 0.5,
   presented in blocks versus mixed.
4. 6.2 maximization bias (B02-B03, B05): exact expectations for coin-flip estimates (+1 or -1 around the true
   value), single estimator versus double estimator; expected maximum of n standard normal estimates.
5. 6.2 one table, three targets (B05-B07): the max of each estimate row, the two cross-evaluations, and the DQN
   and Double DQN targets from the same rows; a three-transition minibatch with a terminal transition.
6. Book Example 6.7 (Figure 6.5): Q-learning versus Double Q-learning, fraction of left actions from A.
   The book does not state the number of actions in B; 10 is this script's choice.
7. Mnih et al. (2015) replay / target-network ablation (Extended Data Table 3): ratios and conditional gains.
8. Slide-minute sums of the step-1 proposal (historical, hard-coded; not the current deck).
9. Cross-review of ChatGPT's two-row trace.
10. 6.1 study slide after V11-B (instructor, 2026-11-17): the last two transitions of the corridor, rows 2 and 3
    (samples 4 and 5 of section 1), with one update per transition (alpha 0.1, the minibatch's 0.3/3 per row) in
    both orders, against the single minibatch step. Labels stay fixed (target weights).
11. The saved deck's slide targets: sums the 'Target: N min' lines of visible slides, split at D00.
"""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np

# ---------------------------------------------------------------------------------------------------------------
print("1. 6.1 worked trace: corridor, positions 1-3, goal G to the right of 3 (terminal), wall to the left of 1")
GAMMA = F(1, 2)
ALPHA = F(3, 10)          # minibatch of 3, mean gradient: alpha / 3 = 0.1 per sample


def x(pos):
    return (F(1), F(pos))


def q(w, pos, a):
    return sum(wi * xi for wi, xi in zip(w[a], x(pos)))


w = {'L': (F(1, 10), F(1, 10)), 'R': (F(0), F(2, 10))}          # online weights
w_minus = {'L': (F(0), F(1, 10)), 'R': (F(1, 10), F(1, 10))}    # target weights

for name, ww in (('online w', w), ('target w-', w_minus)):
    print(f"   {name}: " + "; ".join(
        f"pos {p}: L {float(q(ww, p, 'L')):.2f}, R {float(q(ww, p, 'R')):.2f}" for p in (1, 2, 3)))

# act in position 3
greedy = max('LR', key=lambda a: q(w, 3, a))
print(f"   act: position 3, greedy action {greedy}; transition (3, R, +1, G, done) is stored as number 5")
buffer = {1: (1, 'R', F(0), 2, False), 2: (2, 'L', F(0), 1, False), 3: (1, 'L', F(0), 1, False),
          4: (2, 'R', F(0), 3, False), 5: (3, 'R', F(1), 4, True)}
batch = [2, 4, 5]


def target(ww, r, s2, done, mask=True):
    boot = max(q(ww, s2, a) for a in 'LR')
    return r + GAMMA * boot * (0 if (done and mask) else 1)


deltas = {}
for j in batch:
    s, a, r, s2, done = buffer[j]
    U = target(w_minus, r, s2, done)
    deltas[j] = U - q(w, s, a)
    print(f"   sample {j}: ({s}, {a}, {float(r):+.0f}, {'G' if done else s2}{', done' if done else ''})  "
          f"target {float(U):.3f}  prediction {float(q(w, s, a)):.2f}  TD error {float(deltas[j]):+.2f}")
loss = sum(d * d for d in deltas.values()) / (2 * len(batch))
print(f"   loss = mean of half squared errors = {float(loss):.4f}")
print(f"   missing terminal mask on sample 5: target would be {float(target(w_minus, F(1), 4, True, mask=False)):.3f}"
      " (the network still outputs numbers for the input 'position 4')")
print(f"   target outputs at the goal encoded as position 4 (R02): L {float(q(w_minus, 4, 'L')):.2f},"
      f" R {float(q(w_minus, 4, 'R')):.2f}")

w_new = {a: tuple(w[a]) for a in 'LR'}
for j in batch:
    s, a, *_ = buffer[j]
    w_new[a] = tuple(wi + ALPHA / len(batch) * deltas[j] * xi for wi, xi in zip(w_new[a], x(s)))
for a in 'LR':
    print(f"   w_{a}: {tuple(float(v) for v in w[a])} -> {tuple(round(float(v), 4) for v in w_new[a])}")
print("   online predictions after the step: " + "; ".join(
    f"pos {p}: L {float(q(w_new, p, 'L')):.2f}, R {float(q(w_new, p, 'R')):.2f}" for p in (1, 2, 3)))
assert q(w_new, 2, 'R') > q(w, 2, 'R') and deltas[4] < 0     # outvoted through the shared weights
s, a, r, s2, done = buffer[4]
print(f"   target of sample 4 (2, R, 0, 3): from w- before and after the step {float(target(w_minus, r, s2, done)):.3f}"
      f" (unchanged); from online weights before {float(target(w, r, s2, done)):.3f},"
      f" after {float(target(w_new, r, s2, done)):.3f}; after the copy w- <- w it becomes"
      f" {float(target(w_new, r, s2, done)):.3f}")

# ---------------------------------------------------------------------------------------------------------------
print("\n2. Target moving every step versus frozen for C = 5 (Week 5 I02: v-hat = (w, 2w), gamma 0.9, alpha 0.1)")
g, al, C = 0.9, 0.1, 5
w_on, w_fr, w_tg = 10.0, 10.0, 10.0
rows = []
for k in range(1, 16):
    w_on += al * (g * 2 * w_on - w_on)
    w_fr += al * (g * 2 * w_tg - w_fr)
    note = ''
    if k % C == 0:
        w_tg = w_fr
        note = f'  copy: frozen target becomes {g * 2 * w_tg:.3f}'
    rows.append((k, w_on, w_fr, note))
for k, a_, b_, note in rows:
    if k in (1, 2, 5, 6, 10, 15):
        print(f"   update {k:2d}: moving target w = {a_:.3f};  frozen target w = {b_:.3f}{note}")
print(f"   moving target: factor {1 + al * (2 * g - 1):.2f} per update. Frozen: within a period w approaches the"
      f" fixed target 2*gamma*w- = 1.8 w-; one period multiplies w by {1.8 - 0.8 * (1 - al) ** C:.4f}"
      f" (five moving-target updates: {(1 + al * (2 * g - 1)) ** C:.4f})")

# ---------------------------------------------------------------------------------------------------------------
print("\n3. Blocks versus mixed samples: one shared weight, targets +1 (group A) and -1 (group B), alpha 0.5")
wb, trace = 0.0, []
for y in [1] * 4 + [-1] * 4:
    wb += 0.5 * (y - wb)
    trace.append(wb)
print("   blocks AAAA BBBB: " + ", ".join(f"{v:+.4f}" for v in trace))
print(f"   after the B block the error on group A is {1 - trace[-1]:.4f}; best single weight is 0 (error 1 on each)")
wm, trace = 0.0, []
for _ in range(4):
    wm += 0.5 * ((1 - wm) + (-1 - wm)) / 2
    trace.append(wm)
print("   mixed minibatches {A, B}: " + ", ".join(f"{v:+.4f}" for v in trace))

# Controlled version (shared review R01): the same four size-two updates in both conditions; only the order differs.
wc, trace = 0.0, []
for pair in ((1, 1), (1, 1), (-1, -1), (-1, -1)):
    wc += 0.5 * sum(y - wc for y in pair) / 2
    trace.append(wc)
print("   R01 controlled: four minibatches of two. AA, AA, BB, BB: " + ", ".join(f"{v:+.4f}" for v in trace)
      + "; AB, AB, AB, AB: +0.0000 each (deliberately balanced pairs)")
assert trace == [0.5, 0.75, -0.125, -0.5625]

# ---------------------------------------------------------------------------------------------------------------
print("\n4. Maximization bias: exact expectations with coin-flip estimates (true value +1 or -1 noise)")


def coin(true):
    """E[max of one estimate set], E[second set evaluated at the first set's argmax] (ties split evenly)."""
    n = len(true)
    e_max = e_dbl = F(0)
    for noise in product((-1, 1), repeat=n):
        est = [t + e for t, e in zip(true, noise)]
        p = F(1, 2 ** n)
        e_max += p * max(est)
        best = [i for i, v in enumerate(est) if v == max(est)]
        # the second, independent estimate of action i has mean true[i]
        e_dbl += p * sum(F(true[i]) for i in best) / len(best)
    return e_max, e_dbl


for true in ([0, 0], [0, 0, 0], [0, 0, 0, 0], [1, 0]):
    e_max, e_dbl = coin(true)
    print(f"   true values {true}: max of truth {max(true)}; E[max estimate] = {e_max} ({float(e_max):+.3f});"
          f" E[double estimate] = {e_dbl} ({float(e_dbl):+.3f})")
assert coin([0, 0]) == (F(1, 2), 0) and coin([1, 0]) == (F(5, 4), F(3, 4))

print("   expected maximum of n independent N(0, 1) estimates of a true value 0:")
zs = np.linspace(-8, 8, 160001)
pdf = np.exp(-zs ** 2 / 2) / math.sqrt(2 * math.pi)
cdf = np.array([0.5 * (1 + math.erf(z / math.sqrt(2))) for z in zs])
for n in (1, 2, 4, 10, 18):
    val = np.trapz(zs * n * cdf ** (n - 1) * pdf, zs)
    print(f"     n = {n:2d}: {val:.3f}")

# ---------------------------------------------------------------------------------------------------------------
print("\n5. One table, three targets (true values all 0; reward 0; gamma 0.9)")
Q1 = np.array([0.6, -0.3, -0.1])      # also read as the online network's outputs at s'
Q2 = np.array([-0.2, 0.4, -0.4])      # also read as the target network's outputs at s'
print(f"   max Q1 = {Q1.max():+.1f}, max Q2 = {Q2.max():+.1f}")
print(f"   Double Q-learning: Q2(argmax Q1) = {Q2[Q1.argmax()]:+.1f}, Q1(argmax Q2) = {Q1[Q2.argmax()]:+.1f}")
print(f"   DQN target = 0.9 * max over target outputs = {0.9 * Q2.max():+.2f}")
print(f"   Double DQN target = 0.9 * target output at online argmax = {0.9 * Q2[Q1.argmax()]:+.2f}")
print("   minibatch (gamma 0.9): r, done, online outputs, target outputs -> DQN target, Double DQN target")
mb = [(0.0, False, [1.0, 2.0, 1.5], [1.2, 1.4, 1.8]),
      (1.0, False, [0.5, 0.2, 0.1], [0.9, 0.3, 0.4]),
      (-1.0, True, [3.0, 1.0, 2.0], [2.0, 5.0, 1.0])]
for r, done, on, tg in mb:
    on, tg = np.array(on), np.array(tg)
    m = 0.0 if done else 1.0
    dqn = r + 0.9 * m * tg.max()
    ddqn = r + 0.9 * m * tg[on.argmax()]
    assert ddqn <= dqn + 1e-12
    print(f"     r {r:+.0f}, done {done!s:5}: DQN {dqn:+.2f}, Double DQN {ddqn:+.2f}")

# ---------------------------------------------------------------------------------------------------------------
print("\n6. Book Example 6.7: % left actions from A (epsilon 0.1, alpha 0.1, gamma 1; 10 actions in B is our choice)")


def example_6_7(double, runs=10000, episodes=300, n_b=10, eps=0.1, alpha=0.1, seed=0):
    rng = np.random.default_rng(seed)
    k = 2 if double else 1
    QA = np.zeros((k, runs, 2))           # actions: 0 = left, 1 = right
    QB = np.zeros((k, runs, n_b))
    idx = np.arange(runs)
    left = np.zeros(episodes)

    def eps_greedy(values):
        noise = rng.random(values.shape) * 1e-9          # random tie-breaking
        greedy_a = (values + noise).argmax(axis=1)
        explore = rng.random(values.shape[0]) < eps
        return np.where(explore, rng.integers(values.shape[1], size=values.shape[0]), greedy_a)

    for ep in range(episodes):
        a = eps_greedy(QA.sum(axis=0))
        left[ep] = (a == 0).mean()
        upd = rng.integers(k, size=runs)                 # which table is updated
        oth = (k - 1) - upd if double else upd
        # transition from A: reward 0; left leads to B, right terminates
        # select with the table being updated (random tie-breaking)
        sel = (QB[upd, idx] + rng.random((runs, n_b)) * 1e-9).argmax(axis=1)
        boot = np.where(a == 0, QB[oth, idx, sel], 0.0)  # evaluate with the other table (same one if not double)
        QA[upd, idx, a] += alpha * (boot - QA[upd, idx, a])
        # transition from B for the runs that went left
        go = a == 0
        ab = eps_greedy(QB.sum(axis=0))
        r = rng.normal(-0.1, 1.0, size=runs)
        upd2 = rng.integers(k, size=runs)
        cur = QB[upd2, idx, ab]
        QB[upd2[go], idx[go], ab[go]] = (cur + alpha * (r - cur))[go]
    return left


for name, dbl in (('Q-learning', False), ('Double Q-learning', True)):
    lf = example_6_7(dbl)
    print(f"   {name:18s}: " + ", ".join(f"episode {e}: {100 * lf[e - 1]:.0f}%" for e in (1, 25, 100, 300))
          + f"; peak {100 * lf.max():.0f}% (optimal with epsilon 0.1 is 5%)")

# ---------------------------------------------------------------------------------------------------------------
print("\n7. Mnih et al. (2015) Extended Data Table 3, read from the paper (p. 12) on 2026-11-16 (Silver L6 p. 41 differs in decimals)")
abl = {'Breakout': (316.8, 240.7, 10.2, 3.2), 'Enduro': (1006.3, 831.4, 141.9, 29.1),
       'River Raid': (7446.6, 4102.8, 2867.7, 1453.0), 'Seaquest': (2894.4, 822.6, 1003.0, 275.8),
       'Space Invaders': (1088.9, 826.3, 373.2, 302.0)}
print("   columns: replay+target, replay only, target only, neither; then ratios to 'neither'")
for game, (both, rep, tgt, none) in abl.items():
    print(f"   {game:15s} {both:8.1f} {rep:8.1f} {tgt:8.1f} {none:8.1f}   x{both / none:5.1f} x{rep / none:5.1f}"
          f" x{tgt / none:5.1f}   replay-only > target-only: {rep > tgt}")
    print(f"   {'':15s} gain from replay with targets on {both - tgt:7.1f}; gain from targets with replay on {both - rep:7.1f}")

# ---------------------------------------------------------------------------------------------------------------
print("\n8. Slide-minute sums of Claude's step-1 proposal (historical; the saved deck's targets are in section 11)")
s61 = {'A00': 0.5, 'A01': 2, 'A02': 4, 'A03': 2, 'A04': 4, 'A05': 3, 'A06': 4, 'A07': 3, 'A08': 2, 'A09': 4,
       'A10': 3, 'A11': 3, 'A12': 8, 'A13': 6, 'A14': 2, 'A15': 3, 'A16': 2, 'A17': 2}
s62 = {'B00': 0.5, 'B01': 2, 'B01a': 3, 'B02': 4, 'B03': 3, 'B04': 3, 'B05': 3, 'B06': 3, 'B07': 4, 'B08': 4,
       'B09': 6, 'B10': 5, 'B11': 5, 'B12': 4, 'B13': 2, 'B14': 2}
print(f"   6.1 targets sum to {sum(s61.values())} (allocation 55, delivery allowance 63);"
      f" protected trace A12-A13 = {s61['A12'] + s61['A13']}")
print(f"   6.2 targets sum to {sum(s62.values())} (allocation 55, delivery allowance 63);"
      f" bias/Double block B02-B07 = {sum(s62[k] for k in ('B02', 'B03', 'B04', 'B05', 'B06', 'B07'))},"
      f" ablation block B08-B10 = {sum(s62[k] for k in ('B08', 'B09', 'B10'))}")

# ---------------------------------------------------------------------------------------------------------------
print("\n9. Cross-review of ChatGPT's two-row trace (shared review C01): gamma 0.5, step size 0.1, batch mean")
g = 0.5
on_succ, tg_succ = np.array([4.0, 2.0]), np.array([2.0, 6.0])        # (left, right) at row 1's successor
U = [1 + g * tg_succ.max(), -1.0]
d = [U[0] - 2.0, U[1] - 0.0]
print(f"   DQN targets {U}, errors {d}, loss {sum(x_ * x_ for x_ in d) / 4}; Double DQN target for row 1:"
      f" {1 + g * tg_succ[on_succ.argmax()]}")
db_left, db_right = 0.1 * (d[0] + 0) / 2, 0.1 * (0 + d[1]) / 2       # row 1 took left, row 2 took right
print(f"   head-bias steps if only the two output biases are trainable: left {db_left:+.2f}, right {db_right:+.2f}")
on_new = on_succ + np.array([db_left, db_right])
print(f"   online outputs at the successor: {on_succ} -> {on_new}")
print(f"   row 1 label from online weights: {1 + g * on_succ.max()} -> {1 + g * on_new.max()};"
      f" from target weights: {U[0]} before and after the step; after a copy: {1 + g * on_new.max()}")

# ---------------------------------------------------------------------------------------------------------------
print("\n10. Study slide: one update per transition on the last two transitions (samples 4 and 5 of section 1)")
print("    V11-B left head, minibatch mean: (0.1, 0.1) + 0.3/3 * (-0.2) * (1, 2) ="
      f" {tuple(round(float(v), 4) for v in w_new['L'])}")


def per_transition(order, alpha):
    wr = w['R']
    for j in order:
        s, a, r, s2, done = buffer[j]
        U = target(w_minus, r, s2, done)                       # labels from w-: fixed through these updates
        err = U - sum(wi * xi for wi, xi in zip(wr, x(s)))
        wr = tuple(wi + alpha * err * xi for wi, xi in zip(wr, x(s)))
        print(f"      after sample {j} ({s}, {a}): TD error {float(err):+.3f}, w_R = {tuple(round(float(v), 4) for v in wr)},"
              f" R at 2 = {float(wr[0] + 2 * wr[1]):.3f}, R at 3 = {float(wr[0] + 3 * wr[1]):.3f}")
    return wr


for order, alpha in (((4, 5), F(1, 10)), ((5, 4), F(1, 10)), ((4, 5), F(3, 10))):
    print(f"    order {order}, alpha {float(alpha)} per update:")
    per_transition(order, alpha)
print(f"    one minibatch step (alpha 0.3, mean of 3): w_R = {tuple(round(float(v), 4) for v in w_new['R'])},"
      f" R at 2 = {float(q(w_new, 2, 'R')):.3f}, R at 3 = {float(q(w_new, 3, 'R')):.3f}")
print("    row 2's and row 3's parts of the minibatch step at position 2:"
      f" {float(ALPHA / 3 * deltas[4] * 5):+.2f} and {float(ALPHA / 3 * deltas[5] * (1 + 2 * 3)):+.2f}")
print("    note: alpha 0.1 with features (1, 3) gives alpha * |x|^2 = 1, so a single update lands exactly on the label")

# ---------------------------------------------------------------------------------------------------------------
print("\n11. Saved deck: visible slides' 'Target' minutes (6.1 before D00, 6.2 from D00 on)")
import re
from pathlib import Path
from pptx import Presentation
deck = Presentation(Path(__file__).resolve().parent.parent / 'course/lectures/week06/deep_q_learning_claude.pptx')
sums, session = {'6.1': 0.0, '6.2': 0.0}, '6.1'
for s in deck.slides:
    if s._element.cSld.get('name') == 'D00':
        session = '6.2'
    if s._element.get('show') == '0' or not s.has_notes_slide:
        continue
    m = re.search(r'Target: ([\d.]+) min', s.notes_slide.notes_text_frame.text)
    sums[session] += float(m.group(1)) if m else 0
print(f"    6.1: {sums['6.1']:g} min; 6.2: {sums['6.2']:g} min (delivery allowance 63 per session)")

