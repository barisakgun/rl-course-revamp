# Week 5 (`linear` and `instability`, sessions 5.1–5.2): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-11-02. Analysis only: nothing here is
accepted. It becomes historical after step 3. No deck decision file exists yet. The instructor's choices will go to
`decisions/lectures/<deck>.md`; E1 below proposes the deck name. I have not read any ChatGPT file for this deck.

**Scope of this file:**
- the full teaching sequences for 5.1 `linear` and 5.2 `instability`;
- the old-deck delta for the whole old deck `6 - Value Function Approximation.pptx`, which spans both sessions and
  goes beyond them;
- early choices the instructor may want to settle before the cross-review (E1–E9).

All numbers are checked by `scripts/check_function_approximation_claude.py`.

## Early choices for the instructor

These are the "reasons to pause" items (`docs/lecture_workflow.md`). Each has a recommendation; drafting continues
with the recommendation unless the instructor says otherwise.

| # | Choice | Recommendation | Alternative |
| --- | --- | --- | --- |
| E1 | Deck split and name | One deck for 5.1 and 5.2, as for Weeks 2–4. Name: `function_approximation` (the week's title). | `value_function_approximation` (old deck title, long), `linear` (first session id), or two decks. |
| E2 | 5.1 running example for the worked update and the diagnosis | **The 2×2 grid** (B03, γ = 0.5) under always-right, with two features x(s) = (1, distance to goal). Students know the exact values (14/275, 32/275, 46/55). Two of the three cells share a feature vector but have very different values (0.116 versus 0.836), so the diagnosis is built in. Three states and two weights is also exactly the book's geometry picture (Figure 11.3), so 5.2 can reuse it. | The old midterm's robot-and-landmarks features (Spring 2025 MT1 Q4; four features, no known values), or the book's 1000-state random walk with state aggregation (Example 9.1; a figure, no hand calculation). |
| E3 | Control with approximation (q̂, semi-gradient Sarsa and Q-learning) in 5.1 | **Keep it in 5.1: 6 minutes, F15–F16.** 5.2 needs Q-learning with approximation as the case with all three triad elements. 6.1 "DQN as approximate Q-learning" builds on the semi-gradient Q-learning update. | Move it to the opening of 6.1. 5.1 then gains 6 minutes for the diagnosis, and 6.1 loses them. |
| E4 | Projection depth (accepted: geometric intuition only, about 8 minutes, no projected-Bellman derivation) | G03–G04, 8 minutes: one picture on the grid (plane of representable values; v^π off the plane; best fit; backup leaves the plane, projection returns). Π and the μ-weighted distance are named in words and on the picture. No PBE, no gradient-TD objective. G02 (5 minutes) gives the numbers on the grid and counts as linear-TD convergence (`linear_function_approximation`), not as projection. | Count G02 inside the 8 minutes: merge G02–G04 into 8 minutes and drop the grid numbers to one table. |
| E5 | Baird's counterexample (accepted: full analysis optional) | One slide, 3 minutes: the MDP picture and the **DP-sweep panel** of book Figure 11.2 (the right panel). That panel needs no importance ratio (eq. 11.9), which keeps D6's "IS from Week 8" intact. A hidden appendix slide holds the feature details. | The left panel too (semi-gradient off-policy TD, eq. 11.2). It uses ρ_t, which students have not met, so it needs a "corrections come in Week 8" disclaimer. |
| E6 | Old-deck material outside the Week 5 scope | **Cut** from this deck: average reward with approximation (old 37–40); gradient TD (old 51–55); least squares, LSTD and LSPI (old 62–74). Gradient TD gets one spoken sentence and a book pointer (§11.7). LSTD is an unresolved optional mention in the offline unit (`least_squares_td`). Old 57 (incremental versus batch) is **offered to the Week 6 deck**, where replay needs it. | Hidden appendix slides for any of them. |
| E7 | Notation not in the guide | Needs approval before rendering (details under "Notation"): VE(w) for the value error; ∇ for the gradient; Π for the projection, in words or as a picture label only; ‖·‖_μ, words only. A name for the distance feature that avoids d, which the guide uses for the weight dimension. | Keep the old deck's J(w) for the objective. It clashes with the guide's J(**θ**) policy objective, so I advise against it. |
| E8 | Delivery allowance | 5.1 slide targets sum to 58.5 minutes, 0.5 above the 58-minute allocation. That is fine for delivery under the 63-minute allowance; the planning estimate is unchanged. 5.2 sums to 57.5. | Trim F11 (feature menu) to 1.5 minutes. |
| E9 | Second worked update (F12, transition B) | Keep it. Students compute it after update A, and it makes the "tug of war" between the two aliased cells visible. The scope's "one linear semi-gradient update" is read as one method, not one numerical step. | The instructor computes B live. That saves about 2 minutes of student time. |

## Accepted frame

From `decisions/topic_decisions.yaml` and `output/lectures/session_sources.md` §5.1–5.2.

**5.1 `linear` (Linear approximation and semi-gradients).** 58 teaching minutes (range 50–65), delivery allowance up
to 63.
- Worked activity: compute a feature-based TD update and diagnose missing information.
- Pacing note: feature menu compressed; preserve the distinction between representation and learning.
- Groups:
  - `approximation` (core; derive / implement / analyze; live): one linear semi-gradient update and one worked
    divergence demonstration; distinguish representation limitations from unstable learning. Nonlinear
    approximation motivates DQN; no separate neural-network course. Topics: `linear_function_approximation`,
    `feature_construction`, `semi_gradient_methods`, `approximation_instability`, `nonlinear_function_approximation`.
  - `formulation` (core; explain / analyze): distinguish observed information from a Markov state.

**5.2 `instability` (Approximation instability).** 58 teaching minutes (range 50–70).
- Worked activity: work through a small divergent update example; vary one part of the deadly triad.
- Pacing note: projection limited to about 8 minutes; full Baird analysis optional.
- Groups:
  - `approximation`;
  - `projection` (exposure; explain): geometric intuition only; no projected-Bellman derivation.

**Constraints from other decisions.**
- **No importance sampling** before 8.2 (`model_free_control` D6). The w → 2w example needs none: its first state has
  one action. Baird is shown with the DP-sweep panel (E5).
- **Gradient TD** is in no accepted group. It is not taught here; there is one pointer (E6).
- **LSTD** is unresolved and optional in the offline unit. It is not taught here (E6).
- **Expected Sarsa** is an extension. The book's semi-gradient off-policy action-value method (eq. 11.5) is Expected
  Sarsa, so it is not used.
- **Readings:** no student readings in current planning (`reading_decisions.md`). Book section pointers stay optional.
- **Midterms:** Midterm 1 does not cover Week 5 (decision log, 2026-11-02). The Midterm 2 coverage decision is open.

**Assessment link.** A2 (release Week 6, prerequisites `linear`, `instability`, `dqn_diagnosis`) task 1: "Implement
a linear semi-gradient update. Use supplied contrasting feature sets/data to distinguish a sufficient
representation, an insufficient representation, and an off-policy instability example." F09, F12–F14, G02 and
G05–G07 prepare those three cases directly, and G13 is a classification of the same three. A2's `exam_bridge` text
("Midterm 1 may assess only already-taught linear/instability reasoning") predates the 2026-11-02 coverage decision.
With Week 5 now outside Midterm 1, that line is moot for Fall 2026. I note this; I do not propose an edit.

## What students already have

- **The 2×2 grid** (`bellman` B03): (1,1) start bottom-left, (2,1) bottom-right, (1,2) top-left, (2,2) goal; 0.8/0.1/0.1
  moves; +1 on goal entry, −0.04 otherwise; γ = 0.5.
  - Always-right values (B21): 14/275 ≈ 0.051, 32/275 ≈ 0.116, 46/55 ≈ 0.836.
  - Improved policy (up, right, up) (B21r): 199/550 ≈ 0.362, 469/550 ≈ 0.853 at both (2,1) and (1,2).
- **The common update form** V ← V + α[U_t − V] with target U_t (`mc_td` MT07). MC, TD(0) and n-step targets; forward
  λ (3.2). Bias and variance of targets.
- **Week 4** (`model_free_control`):
  - Q(S_t, A_t) ← Q(S_t, A_t) + α[U_t − Q(S_t, A_t)] with the Sarsa and Q-learning targets;
  - behaviour b and target π;
  - on-policy (Sarsa) and off-policy (Q-learning) as behaviour versus target, without IS (D6);
  - cliff walking.
  - P10 ended with "a separate estimate for every state-action pair is impractical in large spaces. How can experience
    generalize?"
- **Week 1** (1.1/1.2): observation O_t versus state S_t; history H_t; representation as a design choice.
- **Entry background** (`config/course.yaml`): basic machine learning, linear algebra. Gradient descent and least
  squares are known, so the gradient-descent reminder is short.

## Is the old material substantial?

**Yes.** `6 - Value Function Approximation.pptx` (75 slides, 12 hidden) covers both sessions. It also covers material
outside them: average reward, gradient TD, least squares. The delta below starts from it; I did not need to ask.

## Central idea and the motivation thread

**5.1: one update form, now for weights.** Tables cannot scale, and they cannot generalize: what is learned about one
state says nothing about a similar one. A parameterized v̂(s, **w**) with far fewer weights than states does
generalize. One update moves many states, and that is the point.

The update keeps Week 3's shape:

  **w** ← **w** + α[U_t − v̂(S_t, **w**)] ∇v̂(S_t, **w**).

- With a Monte Carlo target this is true stochastic gradient descent on the value error.
- With a bootstrapped target it is not, because the target depends on **w** and we ignore that dependence. That is
  the "semi" in semi-gradient.
- For linear v̂ the gradient is the feature vector, and one-hot features give back exactly the tabular update.

**The two failure modes** are the thread across both sessions (pacing note, A2 task 1):
1. **Representation (5.1, G02).** The features cannot express the values, because two states that need different
   values look identical. Learning can be perfectly stable and still wrong. The fix is in the features.
2. **Instability (5.2).** The features may be fine, but bootstrapping, generalization and an off-policy update
   distribution together make the weights grow without bound. The fix is in the update: its distribution, its target
   or how it generalizes.

**Explicit motivation time** (memory "motivation first"; `bellman` retrospective).
- **5.1:** about 20 of 58.5 minutes go to "why" before "how":
  - F01–F05: why tables fail, what is hard about RL data, why weight the errors;
  - F08's first half: why we drop part of the gradient;
  - F10: what a feature must carry;
  - F14: two kinds of failure.
- **5.2:** about 15 of 57.5 minutes:
  - G01: what could go wrong;
  - G03–G04: a picture of why;
  - G06: why the fragment grows;
  - G09: which off-policy problem;
  - G12: why practice still works.

  The worked divergence is itself a "why" exercise.

## Teaching sequence for 5.1 `linear` (slide level, unpolished)

Slide IDs are proposals. Minutes are planning targets. "Old N" means `6 - Value Function Approximation.pptx` slide N in
PPTX numbering (the PDF omits the 12 hidden slides).

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| F00 | Title | Title Slide layout: course name; **Function Approximation** / instructor / Fall 2026. | deck title format | 0.5 |
| F01 | From tables to generalization | Callback to P10. Everything so far was a table: one entry per state or per state–action pair. Weeks 1–4 in one line each. | old 3 (rewritten), P10 | 2 |
| F02 | Why tables fail | (1) Too many states to store or visit: backgammon, Go, continuous control. (2) No generalization: old 5's Pacman states. Learning that one state is bad tells a table nothing about a nearly identical one. Question: "how many of these states would tabular Q-learning need to visit?" | old 4–5 (images), Silver L6 pp. 4–6, Abbeel L2 pp. 14–16 | 3 |
| F03 | What do we need from an approximator? | Brainstorm first (old 8's list in the click). Then what RL adds to supervised regression (old 9): correlated, non-i.i.d. data; data that depends on our actions; targets that move because they bootstrap and the policy changes; online updates. Restrict to differentiable approximators. Hold "moving targets" for F08 and 5.2. | old 8–9 (compressed), Silver L6 pp. 8–9 | 3 |
| F04 | Parameterized values | v̂(s, **w**) ≈ v^π(s), with **w** ∈ ℝ^d and d ≪ ∣𝒮∣. Old 7's input–output picture, with three forms: v̂(s, **w**); q̂(s, a, **w**); one output per action, which previews DQN. Key consequence: changing one weight changes many states' values. That is generalization; 5.2 shows its cost. | old 7, Silver L6 p. 7, book §9.1 printed 198 / PDF 220 | 2 |
| F05 | Which errors matter? | VE(**w**) = Σ_s μ(s)[v^π(s) − v̂(s, **w**)]². Why the weighting: with fewer weights than states we cannot be right everywhere, so we choose where. On-policy μ is the fraction of time spent in each state. Check: "which grid cell does always-right visit most?" Answer: (2,1), which bumps into the wall; 5.2 returns to this. | book §9.2 eq. 9.1 printed 199 / PDF 221, Sutton 18-19 p. 17 | 3 |
| F06 | Gradient descent with an oracle | Reminder of gradient descent, then the stochastic version on one sample (old 10–11 merged). If an oracle gave v^π(S_t): **w** ← **w** + α[v^π(S_t) − v̂(S_t, **w**)]∇v̂(S_t, **w**). Derive it live from ½ the squared error, one line. | old 10–11, 13 (equations reused, J → VE), book eqs. 9.4–9.5, CS234 L4 pp. 41–43 | 3 |
| F07 | No oracle: use a target | Replace v^π(S_t) with U_t: the general update (book 9.7). Monte Carlo U_t = G_t is unbiased, so this is true SGD and converges to a local optimum (global for linear). Link to MT07: with a table, ∇ is a one-hot vector and this is V ← V + α[U_t − V]. Question: "where have you seen this before?" | old 14, book eq. 9.7 and gradient MC box printed 202 / PDF 224, MT07 | 3 |
| F08 | Bootstrapping: the semi-gradient | U_t = R_{t+1} + γv̂(S_{t+1}, **w**) depends on **w**. Chain rule on ½[U_t − v̂(S_t, **w**)]²: the full gradient has a term from the target. Semi-gradient methods drop it and treat the target as a fixed label for this step. Why: (1) it is what we did in tables (Week 3); (2) it keeps TD's speed and online learning; (3) it converges reliably in the on-policy linear case (5.2). Cost: it is not gradient descent on any objective, which is what 5.2 exploits. Semi-gradient TD(0) box (book p. 203), v̂(terminal, ·) = 0 stated. Notes: the full-gradient alternative (residual gradient) exists and tends to be slow and to learn the wrong values (book §11.5); not taught. | old 15–16 (claims qualified), Sutton 18-19 p. 11 (chain-rule line), book §9.3 printed 202–203 / PDF 224–225 | 5 |
| F09 | Linear approximation | v̂(s, **w**) = **w**^⊤**x**(s) = Σ_i w_i x_i(s), so ∇v̂ = **x**(s). The update is α · δ_t · **x**(S_t): step size × TD error × features. One-hot **x** gives exactly tabular TD(0). State aggregation is the next step: one weight per group (book Example 9.1, picture only). The value changes at the updated state by αδ_t‖**x**‖², so feature scale acts like a step size; this matters in F12. | old 18 and 20 (f → **x**), old 21 bullet 1, book §9.4 eqs. 9.8–9.9 printed 204–205 / PDF 226–227, Silver L6 pp. 13–15 | 3 |
| F10 | Features: what must they carry? | Features are functions of the state chosen by the designer (old 18's Pacman list). Requirement: states that need different values must get different features, or no **w** can separate them. Link to 1.1: the observation is not always the state. Here the features are what the learner sees of the state; the transitions still happen on the true state. Old 22's "RL engineering" point: representation is part of the formulation, as in the project. | old 17–19, 22, book §9.5 opening, 1.1 observation/state | 3 |
| F11 | A compressed feature menu | One slide: one-hot and aggregation; coarse and tile coding (one picture: overlap gives generalization, the receptive-field width sets its breadth); radial basis functions; Fourier basis; learned features (F17). Book §9.5 for detail; no algorithmic coverage. | old 21, Sutton 18-19 pp. 22–27 (one figure), book §9.5 printed 210–222 / PDF 232–244 | 2 |
| F12 | **Your turn: one feature-based TD update** | **Protected (with F13): 14 minutes.** Grid, always-right, γ = 0.5, α = 0.1, x(s) = (1, distance to goal): (1,1) → (1, 2); (2,1) and (1,2) → (1, 1). **w** = (0.6, −0.2). (a) v̂ for the three cells: 0.2, 0.4, 0.4. (b) Transition A: (1,2), right, +1, goal. U = 1 (terminal value 0, not **w**^⊤**x**(goal)). δ = 0.6; **w** = (0.66, −0.14). (c) What happened at (2,1), which was never visited? 0.4 → 0.52, *away* from its true value 0.116. (1,1) went 0.2 → 0.38. (d) Transition B: (2,1), right, −0.04, (2,1) (bumps into the wall). U = 0.22; δ = −0.30; **w** = (0.63, −0.17); (1,2) drops back to 0.46. About 2 minutes setup, 4 minutes work, 2 minutes discussion. | constructed (`check_function_approximation_claude.py` §2), old MT1 Spring 2025 Q4 (format), A2 task 1 | 8 |
| F13 | **Your turn: diagnose** | (e) Why do A and B pull in opposite directions? (2,1) and (1,2) share a feature vector, but their true values are 0.116 and 0.836. (f) Can *any* **w** represent always-right's values with these features? No. (g) What information is missing, and which feature would you add? Which side of the goal you are on: "top row" or "right column". With (1, top, right), three independent features fit three states exactly. (h) Twist: under the improved policy (up, right, up), the two cells have the same value, 469/550. Then (1, distance) represents it exactly. Whether features suffice depends on the values to be represented, so it can change when the policy changes. About 3 minutes of work and 3 of discussion. | check script §3, book §9.5 | 6 |
| F14 | Two kinds of failure | Representation: the features cannot express the values. Learning is stable but stays wrong; fix the features (F13). Learning: the features are adequate, but the updates misbehave; that is 5.2. A2 asks you to tell these apart. | pacing note, A2 task 1 | 2 |
| F15 | Control with approximation | q̂(s, a, **w**) = **w**^⊤**x**(s, a), with features of the state–action pair, or one weight vector per action. The update is Week 4's with ∇q̂: **w** ← **w** + α[U_t − q̂(S_t, A_t, **w**)]∇q̂(S_t, A_t, **w**). Sarsa target R_{t+1} + γq̂(S_{t+1}, A_{t+1}, **w**); Q-learning target R_{t+1} + γ max_a q̂(S_{t+1}, a, **w**). Act ε-greedily on q̂. Semi-gradient Sarsa box (book p. 244, old 32). Q-learning box (old 35) on a hidden backup slide, used again in 5.2 and 6.1. Question (old 22): "what if the action is continuous?" The max becomes hard; this returns in Weeks 7–8. | old 22–29 condensed, 32, 35 (R_t → R_{t+1}, m → ∣𝒜(s)∣, Q̂^π → q̂), book §10.1 printed 243–244 / PDF 265–266, Silver L6 pp. 21–24 | 4 |
| F16 | It works: mountain car | Linear Sarsa with tile coding on mountain car: the cost-to-go figure (old 33) and the RBF variant (old 34) on click. Purpose: a continuous state space solved with a few thousand weights, and tile features chosen by the designer. | old 33–34, book Example 10.1 printed 244–246 / PDF 266–268, Sutton 20 pp. 4–10 | 2 |
| F17 | Nonlinear approximation: learned features | A neural network computes its own features. The update form is unchanged, with ∇ from backpropagation. The last layer is still linear in learned features (Sutton 18-19 p. 22). No neural-network course: this is the step to DQN in Week 6. Old 18's note. | old 18 (note), Sutton 18-19 pp. 8–9 and 22, book §9.7 opening, Abbeel L2 pp. 17–29 (one picture at most) | 2 |
| F18 | Summary and the question for 5.2 | One update form; MC is true SGD, TD is a semi-gradient; linear means step size × error × features; features must separate states whose values differ. Question (old 41): this converged on the grid with on-policy data. Does it always? What if the update distribution or the target changes? | old 31, 41 | 2 |

**Targets sum to 58.5 minutes** (check script header; E8). Protected: F12–F13 (14 minutes).

## Teaching sequence for 5.2 `instability` (slide level, unpolished)

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| G00 | Session opener | Section divider "Approximation instability" (same deck). | — | 0.5 |
| G01 | Recap and the question | The F12 update in one line. Today: where does linear TD settle, and when does it not settle at all? | old 41 | 2 |
| G02 | Where does linear TD settle? | Grid, always-right, x = (1, distance). μ = (9/82, 36/41, 1/82): the agent spends 88% of its time bumping at (2,1). Gradient MC approaches the best fit: v̂ = (0.051, 0.126, 0.126). Semi-gradient TD approaches the *TD fixed point*: v̂ = (0.021, 0.133, 0.133). True values: (0.051, 0.116, 0.836). Both runs are stable; both are badly wrong at (1,2), a representation limit (F13). μ makes that error cheap because (1,2) is rarely visited. VE is 0.00624 for the best fit and 0.00638 at the TD fixed point, so TD lands near, but not at, the best fit. Spoken: in continuing tasks, TD's VE is bounded by 1/(1 − γ) times the best (book 9.14). On-policy linear TD converges (old 24's claim fixed: to the TD fixed point, not to the VE optimum). | check script §4, book §9.4 eqs. 9.12 and 9.14 printed 206–208 / PDF 228–230, old 24 (fixed) | 5 |
| G03 | A picture: the plane of representable values | **Projection, part 1 (E4).** Three states mean each value function is a point in 3D. The two weights span a plane of representable v̂. v^π (always-right) lies off the plane. Projection Π is the closest point in the plane, with distance weighted by μ; that is where gradient MC goes. TD alternates a Bellman backup, which leaves the plane (B^π v_TD = (0.021, 0.124, 0.800)), with a projection back into it. The TD fixed point is where backup-then-project returns to the same point. Words and picture only: no PBE, no derivation. | book §11.4, Figure 11.3, printed 266–268 / PDF 288–290, old 49–50 (picture reused; "not for exams" label kept or replaced at the instructor's choice), CS285 L8 pp. 30–34 | 6 |
| G04 | When the loop can grow | **Projection, part 2.** The backup alone is a contraction (`bellman`: it brings values closer). With μ the on-policy distribution, backup-then-project is still a contraction, which is why on-policy linear TD is stable. With another weighting, the projection can stretch what the backup shrank, and repeated steps can grow. CS234's summary: "Bellman operators are contractions, but value function approximation fitting can be an expansion". The next slide shows this happening. | CS234 L4 p. 60, CS285 L8 pp. 33–36, book §§9.4 and 11.4 | 2 |
| G05 | **Your turn: a two-state fragment** | **Protected (G05–G07): 17 minutes.** Old 43 / book §11.2: two states with values w and 2w (features 1 and 2), one action, reward 0, w = 10, α = 0.1, γ = 1. Only this transition is ever updated: the behaviour policy leaves the second state by actions the target policy never takes, so those transitions are not used. Students compute three updates: 10 → 11 → 12.1 → 13.31. Each update raises the target too, so the TD error grows: 10, 11, 12.1. | old 43 (rebuilt as an exercise), book §11.2 printed 260–261 / PDF 282–283, check script §5 | 7 |
| G06 | Why it grows | δ = (2γ − 1)w, so w ← [1 + α(2γ − 1)]w. The factor exceeds 1 whenever γ > 0.5, for *any* α > 0: a smaller step only slows the growth. Book's intuition: on-policy, a promise of higher value must be kept by the next transition. Off-policy, the promise "can be made and then … forgotten and forgiven" (book p. 261, quote under 15 words). Ask: "which ingredients did we use?" | book p. 260–261, old 43 notes | 3 |
| G08 | The deadly triad | Function approximation (shared weights generalize); bootstrapping (targets use estimates); off-policy training (updates not distributed as the target policy would visit states). With all three, divergence is possible. Any two are safe. A DP sweep that updates all states uniformly counts as off-policy in this sense. The danger does not come from control, exploration or sampling: it appears in prediction and even in DP. Old 47's picture. | old 47, book §11.3 printed 264–266 / PDF 286–288, Sutton 26 pp. 6–7 | 4 |
| G07 | **Your turn: break one leg** | Groups each take one change and compute two rounds from w = 10. (i) **On-policy:** also update the second state's exit to a terminal with reward 0 (w ← w + α(0 − 2w) · 2). Per episode 10 → 6.6 → 4.356 (factor 0.66). (ii) **No bootstrapping:** Monte Carlo target G = 0. 10 → 9 → 8.1. (iii) **No generalization:** separate weights w_A = 10, w_B = 20, only w_A updated: 10 → 11 → 11.9. Bounded: w_A approaches γw_B = 20, wrong only because w_B is never corrected. Report back: which change cost what? On-policy restricts the data; MC gives up TD's speed (Week 3); tabular gives up generalization (F02). | check script §5, book §11.3 discussion | 7 |
| G09 | Two off-policy problems | Sutton's framing: (1) the *target* is about another policy, and corrections for that come in Week 8; (2) the *distribution of updates* differs from the target policy's, which is today's problem. Week 4's Q-learning needed no correction for (1) in one step, but with approximation it still has (2). | Sutton 26 p. 4, `model_free_control` C13/D6 | 2 |
| G10 | A complete example: Baird | The fragment is not a full MDP. Baird's is: 7 states, 8 weights, rewards 0, so v^π = 0 is exactly representable. Semi-gradient DP sweeps (expected updates, uniform weighting) still diverge. Book Figure 11.2, right panel (E5): after 1000 sweeps w_8 ≈ 335 (check script). The same sweeps weighted by the on-policy distribution do not. Hidden appendix: feature vectors and the left panel. | old 44, book Figures 11.1–11.2 printed 261–262 / PDF 283–284, Silver L6 pp. 28–29, check script §6 | 3 |
| G11 | What is guaranteed? | Old 46 and 56 fill-in tables, completed with the class. Prediction: on-policy MC and TD with table and linear features converge; TD with nonlinear may diverge; off-policy TD with linear may diverge. Control: Sarsa linear "chatters near a good solution"; Q-learning linear may diverge. Fixes: drop the off-policy MC row, which needs Week 8's ratios, or footnote it; add "converges = to the TD fixed point, not the best fit" (G02). | old 46, 56 (fixed), Silver L6 pp. 30 and 32 | 4 |
| G12 | Not all is lost | Instability is a possibility, not a certainty. When behaviour stays close to the target (ε-greedy), the book reports no known divergence of Q-learning but also no proof (book p. 263; as of 2018, stated with its date). Good representations and step-size control matter. Old 56's "may still fail to do what you want even if there is no divergence" → representation (F14). | old 45, 56 (bottom notes), book p. 263 | 2 |
| G13 | **Diagnose: representation or instability?** | Three supplied symptom panels, such as weight norm and VE against updates. (a) Sufficient features: VE → about 0. (b) Insufficient features, the grid with (1, distance): a stable plateau with error. (c) Baird or the fragment: weights grow. Students classify each and name the fix: features; distribution, target or step. This mirrors A2 task 1 without using its data. | A2 task 1, check script §§3, 4, 6 | 6 |
| G14 | Toward DQN | Q-learning with a neural network has all three triad elements. DQN's replay and target network (Week 6) are engineering responses; they reduce the problem without a guarantee. CS285: "Target networks really help! Replay buffers really help!" | CS285 L8 p. 36, book §11.3 | 2 |
| G15 | Summary | Linear on-policy TD converges, to the TD fixed point. Representation limits are stable but wrong. The deadly triad can make values diverge even in DP. Break one leg, or manage it in practice. | — | 2 |

Order note: G08 comes before G07 in the deck. Students identify the ingredients in G06 and name the triad in G08, then
break one leg in G07. The IDs keep the worked-activity block together for the cross-review.

**Targets sum to 57.5 minutes.** Protected: G05–G07 (17 minutes). Projection: G03–G04 (8 minutes; E4).

## Old-deck delta: `6 - Value Function Approximation.pptx`

PPTX numbering. H = hidden in the old deck.

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 1 | **Fix** | F00: new title format. |
| 2 (H), 36 (H), 42 (H), 61 (H) | **Cut** | Old administration, recap and an unfinished note. |
| 3 | **Fix** | F01: tighten; add the P10 callback. |
| 4–5 | **Keep** | F02: images and the scale argument. |
| 6 | **Cut** | Section divider; F04 opens the topic. |
| 7 | **Keep** | F04: input–output picture; "how do we represent s?" moved to F10. |
| 8–9 | **Keep, compress** | F03: brainstorm with the list on click; old 9's conditions shortened. The project-invitation sentence goes to the notes. |
| 10–11 | **Keep, merge** | F06: one slide (the gradient reminder is entry background). |
| 12 (H), 13 | **Keep 13, fix** | F06–F07: J(**w**) → VE(**w**) with μ (E7). "If you do this over all states…" goes to the notes. |
| 14 | **Keep** | F07: general SGD update; MC question kept; the MT07 link added. |
| 15–16 | **Keep, fix** | F08: "converge reliably in some cases" → "on-policy linear case"; R → R_{t+1}; s_t → S_t. Old 15's disclaimer ("I might call them gradient methods") kept in the notes. |
| 17–19 | **Keep, compress** | F10: Pacman features; f(s) → **x**(s); old 19's brainstorm examples go to the notes. |
| 20 | **Keep** | F09: linear update ("step-size × prediction error × feature value"). |
| 21 | **Keep, compress** | F09 (table lookup) and F11 (menu), with one tile-coding figure from book §9.5. |
| 22 | **Keep** | F10 (formulation link). |
| 23 (H), 24 | **Fix, move** | G02: "TD(0) converges to (around) the global optimum" is wrong for VE. It converges to the TD fixed point, within the 9.14 bound. MC claims kept. |
| 25 | **Keep, fix** | F15: GPI with q̂; m → ∣𝒜(s)∣; continuous-action question kept. |
| 26–27 | **Fix, compress** | F15. Old 27's update has an error: it writes the error as (Q̂ − **f**^⊤**w**), which is zero; it should be the target minus q̂. |
| 28 (H), 29, 31 | **Compress** | F15 and F18: the target list (R_t → R_{t+1}; "a*" max notation tidied). |
| 30 | **Optional** | Q-Pacman images: F02 or F15 if the instructor wants an extra visual (no time assigned). |
| 32 | **Keep** | F15: semi-gradient Sarsa box. |
| 33–34 | **Keep** | F16: mountain car figures. |
| 35 | **Keep (hidden backup)** | F15 backup: semi-gradient Q-learning box. "The double Q version is similar" goes to 6.2 (Double DQN), not here. |
| 37–40 | **Cut** | Average reward with approximation. The average-reward objective was 3.1's five-minute contrast; differential semi-gradient methods are not in scope. Old 40's "we lose the policy improvement theorem" idea survives as G11's control-table note. |
| 41 | **Keep** | F18 and G01: the question that links the sessions. |
| 43 | **Keep, rebuild** | G05–G07: the worked activity (same numbers: w = 10, α = 0.1, no discount); old notes used in G06. |
| 44 | **Keep** | G10 (DP panel only, E5). |
| 45 | **Keep, fix** | G12: "no counterexample that shows ε-greedy diverges" dated to the book (2018). |
| 46 | **Keep, fix** | G11: fill-in prediction table; off-policy MC row footnoted or dropped (needs ratios, Week 8). |
| 47 | **Keep** | G08: triad picture; "Can you break the triad?" becomes G07. |
| 48–50 | **Keep 49–50 picture, cut 48** | G03: geometry with ∣𝒮∣ = 3 and two weights, now on the grid. The "not for exams" label is the instructor's call. Old 48's TD-objective question is cut with gradient TD. |
| 51–55 | **Cut** | Gradient TD (not in accepted scope); one spoken pointer to book §11.7 in G11. |
| 56 | **Keep, fix** | G11–G12: control table ("Converges" for Sarsa linear → "chatters near"); bottom notes kept. |
| 57–58 (58 H) | **Move (offer)** | Incremental versus batch: offered to the Week 6 deck (replay buffer). |
| 59 (H), 60 | **Cut** | Eligibility-trace dimensions: backward view is existence-only (`backward_trace_mention`). |
| 62–74, 63 (H), 66 (H) | **Cut** | Least squares / LSTD / LSPI (E6). |
| 75 (H) | **Cut** | "Deep RL?" placeholder; F17 and G14 cover the bridge. |

**Teaching purpose of cut material** (workflow step 1):
- **Average reward:** the objective is already taught in 3.1. The approximation-specific version is outside every
  accepted group.
- **Gradient TD:** answers "can we keep all three triad elements?" That question is posed in G08 and answered with a
  pointer, because it is not in scope.
- **LSTD/LSPI:** sample-efficient batch fitting. Batch fitting comes back with replay in 6.1 and, optionally, LSTD in
  the offline unit.

## Notation

From `course/notation_guide.md` (Weeks 5–6 block): **w**, d, v̂(s, **w**), q̂(s, a, **w**), **x**(s), **x**_t, μ(s),
δ_t, U_t, B^π. Conversions from the old deck (O9 style):
- f(s) → **x**(s);
- V̂^π(s, w) → v̂(s, **w**);
- Q̂^π(s, a, w) → q̂(s, a, **w**);
- R / R_t → R_{t+1};
- s_t → S_t;
- m → ∣𝒜(s)∣;
- μ as the behaviour policy (Sutton slides) → b.

**Missing, needs approval (E7):**

| Item | Needed by | Proposal |
| --- | --- | --- |
| Value error | F05, G02, G13 | VE(**w**), the book's mean squared value error (the book writes it with an overbar). Not J(**w**), which would clash with J(**θ**). |
| Gradient | F06–F09, F15 | ∇v̂(s, **w**), gradient with respect to **w** (the book's notation; standard). |
| Projection and the μ-weighted distance | G03–G04 | Π as a picture label only, with "closest representable value function, distances weighted by μ" in words. No ‖·‖_μ formula on slides. |
| Distance feature | F12–F13, G02 | Avoid d, which is the weight dimension. Write the features in words, "(1, steps to goal)", and use the numeric vectors. No new symbol. |
| TD fixed point | G02–G03 | "TD fixed point" in words; **w**_TD only if needed. The book's A and b matrices are not shown: A clashes with the action. |

## Prerequisite and timing checks

- **No forward references.**
  - 5.1 uses only Weeks 1–4 and the entry background.
  - 5.2 uses Week 4's behaviour and target policies, not importance sampling.
  - The Baird DP panel needs no ρ.
  - The book's on-policy distribution formula (9.2–9.3) is not shown; μ is described as "fraction of time spent".
- **Worked activities protected:** F12–F13 (14 minutes) in 5.1; G05–G07 (17 minutes) in 5.2.
- **Projection:** G03–G04 = 8 minutes, as accepted. G02 (5) is linear-TD convergence; see E4.
- **Totals:** 5.1 targets sum to 58.5 (allocation 58; under the 63-minute delivery allowance; planning estimate
  unchanged). 5.2 targets sum to 57.5 (allocation 58).
- **Hidden workload:** none. No readings or videos are assigned; appendix and backup slides are optional.
- **Week 6 interface:**
  - 6.1 can assume q̂, the semi-gradient Q-learning target (F15), the deadly triad (G08) and "replay and target
    networks respond to it" (G14).
  - Old 57 (incremental versus batch) is offered to that deck.
  - 6.2's maximization bias is untouched.
