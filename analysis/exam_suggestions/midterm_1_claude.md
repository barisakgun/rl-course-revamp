# Midterm 1 — Claude's initial suggestion (step 1)

Maintenance after cross-review (2026-11-02): provenance fixes from ChatGPT's review only; questions unchanged. Responses to R01–R06 are in the shared review.

Claude, 2026-11-02. Git-ignored until the exam has been held. Workflow: `docs/exam_workflow.md` (adopted 2026-11-02). Status:
`decisions/exams/midterm_1.md`. Format and coverage: `decisions/grading_decisions.md` (`midterm_1`): 1.1–3.2, 100
minutes, separate slot, closed book with a supplied equation sheet, one short written or true/false λ-return item.

Inputs: accepted decks (text views of `introduction` 60b76c83…, `mdp_values` cb460398…, `bellman` ec28bf43…, `mc_td`
b4ca75d4…), `decisions/topic_decisions.yaml`, `course/notation_guide.md`, previous midterm 1s (Fall 19, Spring 21,
Spring 23, Spring 25). Every numerical answer below was checked with exact fractions (script in Claude's scratchpad;
re-run on request).

## 1. What is examinable

Live material only; zero-time appendix slides (bellman BA1, visible; mc_td MTX–MTA1, hidden), optional unscheduled slides (mc_td 43–44)
and readings are out.

| Session | Examinable (mastery) | Not examinable |
| --- | --- | --- |
| 1.1 formulate | Agent/environment, reward vs return, observation vs state, exploration/exploitation, formulating a problem (explain, analyze) | RL application history (I02) beyond recognition |
| 1.2 mdp_values | History H_t, agent state S_t = f(H_t), Markov property, ℳ/𝒯/ℛ and reading a dynamics table, ℛ(s,a) as expectation, deterministic vs stochastic policy, discounted return and recursion, episodic/terminal vs continuing, deadlines and time in the state, v^π and q^π as expected returns (explain, analyze) | POMDP solvers, abstraction theory |
| 2.1 bellman | q^π from v^π, Bellman expectation equations, a fixed policy's linear system, iterative policy evaluation, the contraction idea, optimal values and Bellman optimality equations (derive, analyze) | Matrix-form solution, complexity derivations beyond the slide's statements |
| 2.2 improvement | Greedy improvement, the improvement argument, PI, VI, Q-value iteration, policy extraction, PI/VI trade-offs, reward sensitivity, GPI (derive, analyze) | Asynchronous DP beyond one sentence; certification beyond B24r |
| 3.1 mc_td | First/every-visit MC, incremental mean and constant α, TD(0) target and error, sampling vs bootstrapping, on/off-policy and online/offline distinctions (explain, derive, analyze); average reward vs discounted return (exposure: recognize/explain) | Differential values or average-reward algorithms |
| 3.2 returns | Bias/variance of targets, batch MC vs batch TD (certainty equivalence), n-step targets and their timing, reading the n/α plot, evaluation claims (explain, derive, analyze); forward λ-return (one short item at its 3.2 scope); backward view (existence only) | λ-return calculation beyond the 3.2 activity; eligibility traces; trace algorithms |

`implement` mastery cannot be established by a written exam, and A1 is not yet due, so no question assumes it.

## 2. Delta against previous midterm 1s

| Old question | Decision | Reason |
| --- | --- | --- |
| Spring 25 Q1 (Europa MDP formulation, 31 pts) | **Adapt**: new scenario, 22 pts | Keep the open formulation question. Its "which algorithm" part assumed function approximation; now limited to DP vs sampled experience. Add observation/state and reward-design reasoning, which the redesigned 1.1–1.2 and B26 stress. |
| Spring 25 Q2 (cool/warm DP: IPE, VI, optimal policy, 28 pts) | **Adapt**: new MDP and numbers, 32 pts | Same skills, plus the Bellman linear system and one PI round (2.1–2.2 activities). |
| Spring 23 Q2 / Spring 21 Q2 (grid VI, policy extraction) | **Keep pattern** inside Q2 | |
| Spring 25 Q3a–c, Spring 21 Q3 (MC Q-value prediction), Spring 21 TD Q-prediction | **Adapt** to state values, 30 pts | The course predicts v^π in 3.1–3.2; MC/TD on Q waits for Week 4. |
| Spring 25 Q3d (SARSA), Spring 23 Q3c (Q-learning) | **Cut** | Week 4, not covered this semester. |
| Spring 25 Q4, Spring 23 Q4 (linear features, SARSA weights) | **Cut** | Week 5. |
| Fall 19 Q (eligibility values, backward TD(λ)) | **Cut** | Backward view is existence-only. |
| Spring 23 Q5 (REINFORCE) | **Cut** | Week 7. |
| New | **Add** Q4: eight true/false items with one-line justification, 16 pts | Covers conceptual points that previous exams left out (bias of the TD target, improvement theorem, extraction from v^* vs q^*, evaluation claims, λ weights). |

## 3. Draft exam (100 points, about 72 minutes of estimated student work)

Point split by session (approximate): 1.1–1.2 about 27, 2.1–2.2 about 36, 3.1–3.2 about 37, following the live
minutes (≈ 105 / 118 / 117).

### Q1. Formulating a tutoring problem (22 pts, ~15 min)

An online tutoring app runs a practice session of exactly 20 questions. Before each question it chooses a difficulty:
easy, medium or hard. After each question it sees only whether the answer was correct and how many seconds it took.
The student's actual skill is not visible, and it changes as the student practises. After the 20th question the
student takes a fixed 10-question test that the app does not choose.

- (a) **4 pts** — What are the actions? What is the observation O_t after each question?
  *Answer:* A_t ∈ {easy, medium, hard}. O_t = (correct or not, response time) for the last question. Accept added
  observed features (e.g. topic) if justified. **Mastery:** explain (1.1–1.2).
- (b) **6 pts** — Is the latest observation alone a good Markov state? Give two histories that end in the same
  observation but should lead to different choices. Propose an agent state S_t = f(H_t) and justify it.
  *Answer:* No. "Correct, 20 s" after ten correct hard answers vs after ten wrong easy ones implies different skill
  and a different best next difficulty. Example state: recent counts of correct answers per difficulty (or an
  estimated skill level), plus questions remaining (see d). Full credit needs the argument that the hidden skill
  must be inferred from the history. Perfect Markovness is not required; a justified approximation is. **Mastery:**
  analyze (1.2 M03–M05).
- (c) **6 pts** — Designer A gives +1 for every correct practice answer, 0 otherwise. Designer B gives a reward equal
  to the test score (0–10) after the session, 0 otherwise. For each design, describe a behaviour that maximizes
  expected return. Which matches the goal? What makes B harder to learn from?
  *Answer:* A rewards correct answers, so asking easy questions maximizes it while the student may learn little
  (the reward is satisfied, the goal is not). B rewards the outcome we care about but is delayed and sparse: one
  number after 20 decisions, so credit assignment is hard and learning needs many sessions. 2 pts per design,
  2 for the comparison. **Mastery:** analyze (1.1 reward/return, 2.2 B26 "what is optimal depends on the reward").
- (d) **4 pts** — Is the task episodic or continuing? Should the number of questions remaining be part of the
  state? Why?
  *Answer:* Episodic: the session ends after 20 questions (plus the test). Yes: with a deadline the best difficulty
  can depend on time left (e.g. hard questions pay off only if practice continues), so the same skill estimate
  with 2 vs 15 questions left can call for different actions. **Mastery:** analyze (1.2 M11).
- (e) **2 pts** — Could you compute a good policy with value iteration before any student uses the app? Why or
  why not?
  *Answer:* Not directly: VI needs 𝒯 and ℛ, i.e. how a student's answers and skill respond to each difficulty,
  which is unknown. Learning from sampled sessions (or first fitting a model) is needed. **Mastery:** explain
  (2.2 B28, 3.1 MT01–MT02).

### Q2. Espresso machine: Bellman equations, PI and VI (32 pts, ~28 min)

States clean (c) and dirty (d); terminal state broken. 𝒜(clean) = {brew}, 𝒜(dirty) = {brew, clean}. γ = 0.5. The
broken state has value 0.

| s | a | r | s′ | ℳ(s, a, r, s′) |
| --- | --- | --- | --- | --- |
| clean | brew | +2 | clean | 0.5 |
| clean | brew | +2 | dirty | 0.5 |
| dirty | brew | +2 | dirty | 0.4 |
| dirty | brew | −4 | broken | 0.6 |
| dirty | clean | 0 | clean | 1 |

- (a) **3 pts** — Compute ℛ(dirty, brew). Can a single transition ever give this reward?
  *Answer:* 0.4(2) + 0.6(−4) = −1.6. No: each transition gives +2 or −4; ℛ is an expectation. **Mastery:** explain
  (1.2 M08).
- (b) **7 pts** — Let π brew in both states. Write the Bellman expectation equations for v^π(clean) and
  v^π(dirty), and solve them.
  *Answer:* v^π(d) = −1.6 + 0.5[0.4 v^π(d)] ⇒ 0.8 v^π(d) = −1.6 ⇒ v^π(d) = −2.
  v^π(c) = 2 + 0.5[0.5 v^π(c) + 0.5 v^π(d)] ⇒ 0.75 v^π(c) = 2 − 0.5 = 1.5 ⇒ v^π(c) = 2.
  3 pts for the equations (terminal term zero, no reward counted twice), 4 for the solution. **Mastery:** derive
  (2.1 B06–B08a).
- (c) **5 pts** — Using v^π, compute q^π(dirty, brew) and q^π(dirty, clean). Give the greedy policy π′.
  *Answer:* q^π(d, brew) = v^π(d) = −2; q^π(d, clean) = 0 + 0.5(2) = 1. π′ brews at clean (only action) and cleans at
  dirty. **Mastery:** derive (2.2 B18).
- (d) **6 pts** — Evaluate π′ and show that policy iteration stops with π′. Is π′ optimal? Justify.
  *Answer:* v^{π′}(d) = 0.5 v^{π′}(c); v^{π′}(c) = 2 + 0.25 v^{π′}(c) + 0.25 v^{π′}(d) = 2 + 0.375 v^{π′}(c) ⇒
  v^{π′}(c) = 3.2, v^{π′}(d) = 1.6. Check: q^{π′}(d, brew) = −1.6 + 0.5(0.4)(1.6) = −1.28 < q^{π′}(d, clean) = 1.6,
  so the greedy policy is unchanged; with exact evaluation a stable policy satisfies the Bellman optimality
  equation, so π′ is optimal. (Both values rose: improvement theorem.) **Mastery:** derive, analyze (2.2 B19–B21r).
- (e) **8 pts** — Run two sweeps of value iteration from V_0 = 0. Show both action scores at dirty in each sweep
  and give the greedy action.
  *Answer:* Sweep 1: clean 2; dirty: brew −1.6, clean 0 → V_1 = (2, 0), greedy clean. Sweep 2: clean
  2 + 0.5(0.5·2 + 0.5·0) = 2.5; dirty: brew −1.6 + 0.5(0.4·0) = −1.6, clean 0 + 0.5(2) = 1 → V_2 = (2.5, 1),
  greedy clean. (Sweep 3 would give 2.875, 1.25; the limit is v^* = (3.2, 1.6).) **Mastery:** derive (2.2 B23–B24r).
- (f) **3 pts** — The greedy action at dirty was the same after sweeps 1 and 2. Does that alone prove the policy is
  optimal? Explain.
  *Answer:* No. V_2 ≠ v^*, and an unchanged greedy policy across sweeps is not a stopping rule: it can change later.
  Optimality follows from a full evaluation of that policy plus a stable improvement step, which is what (d) did.
  **Mastery:** analyze (2.2 B24r).

### Q3. Learning values from episodes (30 pts, ~22 min)

A fixed policy π is followed in an MDP with states A and B and a terminal state. The model is unknown. γ = 0.5.
Episode 1: A →(0) B →(2) A →(0) B →(4) terminal. Episode 2: A →(0) B →(1) terminal.

- (a) **4 pts** — Compute the return G_t at every time step of episode 1.
  *Answer:* G_3 = 4, G_2 = 0 + 0.5(4) = 2, G_1 = 2 + 0.5(2) = 3, G_0 = 0 + 0.5(3) = 1.5. **Mastery:** derive (1.2,
  3.1 MT05).
- (b) **6 pts** — Using both episodes, give the first-visit and every-visit MC estimates (sample means) of
  V(A) and V(B).
  *Answer:* Episode 2 returns: A 0.5, B 1. First-visit: V(A) = (1.5 + 0.5)/2 = 1, V(B) = (3 + 1)/2 = 2.
  Every-visit: V(A) = (1.5 + 2 + 0.5)/3 = 4/3, V(B) = (3 + 4 + 1)/3 = 8/3. **Mastery:** derive (3.1 MT06–MT07a).
- (c) **8 pts** — Apply TD(0) updates through episode 1 in time order with α = 0.5, starting from V = 0. Give
  each target and the table after each update. Why does V(A) end so much lower than the MC estimates?
  *Answer:* t=0: target 0 + 0.5(0) = 0, V(A) = 0. t=1: target 2 + 0.5(0) = 2, V(B) = 1. t=2: target
  0 + 0.5(1) = 0.5, V(A) = 0.25. t=3: target 4, V(B) = 1 + 0.5(3) = 2.5. A's targets bootstrap from B's estimate
  before B has learned from the large final reward; that reward reaches A only through later updates (and α < 1
  moves part of the way). **Mastery:** derive, explain (3.1 MT09–MT10).
- (d) **6 pts** — Take the fixed table V(A) = 1, V(B) = 2. For the visit at t = 0 of episode 1, compute the n-step
  targets for n = 1, 2 and 5. Why does n = 5 not use the table?
  *Answer:* G_{0:1} = 0 + 0.5 V(B) = 1. G_{0:2} = 0 + 0.5(2) + 0.25 V(A) = 1.25. G_{0:5} = G_0 = 1.5 because
  t + n ≥ T = 4: the episode ended, no continuation and no extra discounting. **Mastery:** derive (3.2 MT21–MT22a).
- (e) **6 pts** — New data, γ = 1: two episodes C →(+1) D →(0) terminal, and two episodes D →(+2) terminal. What
  do batch MC and batch TD(0) converge to for V(C) and V(D)? Which would you trust if you knew the process was
  Markov, and why might you doubt it here?
  *Answer:* Both: V(D) = (0 + 0 + 2 + 2)/4 = 1. Batch MC: V(C) = 1 (its observed returns). Batch TD: V(C) =
  1 + V(D) = 2. If Markov, TD's answer uses all four D outcomes (certainty equivalence). Here D gave 0 every time it
  followed C and 2 every time it started an episode, which hints that "D" may hide relevant history; then pooling
  D's outcomes can mislead. Two episodes per pattern is little evidence either way. **Mastery:** analyze (3.2
  MT18–MT19a).

### Q4. True or false, with a one-line justification (16 pts, ~7 min)

2 pts each: 1 for the verdict, 1 for a correct justification. No credit for a verdict without justification.

1. If a trajectory from s terminates, its return equals v^π(s). — **False**: one return is a sample; v^π averages
   returns (1.2 M14).
2. For a fixed policy in a finite MDP with bounded rewards and γ < 1, iterative policy evaluation converges to v^π
   from any initial table. — **True**: each sweep shrinks the largest error by at least γ (2.1 B13).
3. Given v^*, an optimal policy can be extracted without the model, whereas extracting it from q^* needs the model.
   — **False**: reversed; argmax_a q^*(s, a) needs no model, extraction from v^* needs ℛ and 𝒯 (2.1 B16, 2.2 B28).
4. If the current policy is not optimal, one greedy improvement step strictly increases the value of every
   nonterminal state. — **False**: values do not decrease anywhere and increase somewhere; some states can stay the
   same (2.2 B19).
5. For any value table V, the expected TD(0) target 𝔼_π[R_{t+1} + γV(S_{t+1}) ∣ S_t = s] equals v^π(s). — **False**:
   its bias is γ𝔼_π[V(S_{t+1}) − v^π(S_{t+1}) ∣ S_t = s]; the complete return's expectation is v^π(s) (3.2 MT16a).
6. In a continuing task, maximizing discounted return and maximizing average reward always prefer the same policy.
   — **False**: e.g. steady 0.8 per step vs alternating 0, 2 at γ = 0.5 (3.1 MT13a). *Exposure item.*
7. With three transitions left after time t (T − t = 3), the λ-return gives the complete return G_t weight
   (1 − λ)λ². — **False**: G_t gets all remaining weight, λ² (the shorter targets get 1 − λ and (1 − λ)λ). *The
   λ-return item (3.2 MTL2).*
8. In one run, every-visit MC ends with lower RMS error than TD(0) does in one run. This shows MC is the better
   method on this task. — **False**: single runs vary; compare many runs at comparably tuned settings and a stated
   budget (3.2 MTE1–MTE2).

Alternative for item 7, if a written λ item is preferred: "For a three-transition episode from t = 0, give the weights
of G_{0:1}, G_{0:2} and G_0 in G_0^λ, and the targets at λ = 0 and λ = 1." (Answer: 1 − λ, (1 − λ)λ, λ²; the one-step
TD target; the complete return.)

### Time estimate

Q1 15, Q2 28, Q3 22, Q4 7: about 72 minutes, 72% of 100 (guideline: at most about 75%). Q2 is the largest risk; if
the cross-review finds it long, drop (f) or sweep 2 of (e).

## 4. Draft equation sheet (last page, unlabelled)

Notation-guide symbols only. Unlike the Spring 2025 sheet: P(s′|s, a) R(s, a, s′) → 𝒯, ℛ, ℳ; Q-learning and linear
approximation removed; MC, TD, n-step and λ-return added.

```latex
G_t \doteq R_{t+1}+\gamma R_{t+2}+\gamma^2 R_{t+3}+\cdots \qquad G_t = R_{t+1}+\gamma G_{t+1}
v^{\pi}(s)\doteq\mathbb{E}_{\pi}[G_t\mid S_t=s] \qquad q^{\pi}(s,a)\doteq\mathbb{E}_{\pi}[G_t\mid S_t=s,A_t=a]
\mathcal{R}(s,a)=\sum_{r,s'} r\,\mathcal{M}(s,a,r,s') \qquad \mathcal{T}(s,a,s')=\sum_r \mathcal{M}(s,a,r,s')
v^{\pi}(s)=\sum_{a}\pi(a\mid s)\,q^{\pi}(s,a) \qquad q^{\pi}(s,a)=\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\,v^{\pi}(s')
v^{\pi}(s)=\sum_{a}\pi(a\mid s)\big[\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\,v^{\pi}(s')\big]
v^{*}(s)=\max_{a}\big[\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\,v^{*}(s')\big]
q^{*}(s,a)=\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\max_{a'}q^{*}(s',a')
\pi'(s)=\arg\max_{a}\big[\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\,V(s')\big] \qquad \pi(s)=\arg\max_a Q(s,a)
V_{k+1}(s)\leftarrow\sum_{a}\pi(a\mid s)\big[\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\,V_k(s')\big]
V_{k+1}(s)\leftarrow\max_{a}\big[\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\,V_k(s')\big]
Q_{k+1}(s,a)\leftarrow\mathcal{R}(s,a)+\gamma\sum_{s'}\mathcal{T}(s,a,s')\max_{a'}Q_k(s',a')
V(s)\leftarrow V(s)+\tfrac{1}{N(s)}\,[G_t-V(s)] \qquad V(S_t)\leftarrow V(S_t)+\alpha\,[U_t-V(S_t)]
\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)
G_{t:t+n}=\sum_{i=1}^{n}\gamma^{i-1}R_{t+i}+\gamma^{n}V(S_{t+n})\ (t+n<T) \qquad G_{t:t+n}=G_t\ (t+n\ge T)
G_t^{\lambda}=(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}+\lambda^{T-t-1}G_t
```

Excluded: average reward (exposure only) and anything after 3.2.

## 5. Questions for the cross-review and the instructor

- **S1 (instructor): λ-return on the sheet.** With the finite λ-return on the sheet, Q4 item 7 becomes reading the
  weight off the formula. That still tests interpretation, but more weakly. Options: keep it (recommended: the sheet
  exists to remove memorization) or omit it from the sheet.
- **S2: Q2 resembles the recycling robot** (two charge-like states, a risky action, a corrective action). The skills
  are the same, the numbers and story are new, and the robot was never solved by DP in class. Acceptable, or prefer
  a grid?
- **S3: Iterative policy evaluation sweeps** are not computed numerically: Q2 uses a linear solve for π and VI sweeps
  for control (sweep mechanics), and Q4.2 covers convergence. Alternative: replace Q2(b) with two IPE sweeps
  (V_1 = (2, −1.6), V_2 = (2.1, −1.92)). This saves the solve but loses the Bellman linear system.
- **S4: 3.2 evaluation** is tested only by Q4.8 (2 pts) and the batch question. A short written protocol question
  (MTE2) is an option if time allows.
- **S5 (instructor): COMP 538** — same exam (current assumption) or an extra part?
- **S6: Q1 grading.** It is open-ended; the answers above are one acceptable set. The rubric needs the instructor's
  view on how much credit a defensible alternative state gets.
