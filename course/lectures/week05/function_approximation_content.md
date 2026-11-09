# Function approximation — first-render content

> **Historical (frozen at the first render, 2026-11-09).** Input to the first render only; not maintained. The PPTX `course/lectures/week05/function_approximation_claude.pptx` is the teaching source from that render on. Current status: [deck decisions](../../../decisions/lectures/function_approximation.md).

**Shared.** Prepared by ChatGPT, 2026-11-08, under workflow step 4. The deck's only current status and accepted/open choices are in the [deck decisions](../../../decisions/lectures/function_approximation.md). Findings and responses belong in the [shared review](../../../analysis/lecture_suggestions/function_approximation_review.md). This file is input to the first render only; freeze it at that render. The saved PPTX then becomes the teaching source. Do not rebuild over an instructor-edited deck.

## Renderer handoff

- One deck, `function_approximation_claude.pptx`, with a visible boundary at G00 between sessions **5.1: Linear approximation and semi-gradients** and **5.2: Approximation instability**. Follow the established course design.
- Use the order below, consolidating D1–D9. Preserve stable IDs in notes. A suffixed ID is a continuation within the parent's time, not extra teaching time. Every slide needs its time, source, essential cues and answer in the notes.
- Render **both** alternatives for each instructor choice. The title and notes must say **Alt A** or **Alt B**, with the choice named: “5.1 example”, “geometry”, or “5.2 divergence”. These are three independent choices; an Alt A label does not select all three. Do not silently select, delete or hide an alternative before the instructor reviews it. The delivery routes below count only one alternative per choice.
- Geometry P1 is `G03-A`; geometry P2 is `G03-B`. They share G02 and G04. P1 naturally follows the grid example; P2 naturally accompanies the landmark/complete-two-state route. G02 supplies the grid information even on the landmark route. Do not add P3, the generic three-dimensional projection figure.
- **O1 remains open:** 13-minute geometry route, with an 8-minute fallback specified below. **O3 remains open:** instructor review of the fragment variants, the complete example's data-selection rule, and the growth visual. The precise labels/caveats below prevent mathematical misstatements without claiming the instructor has settled these teaching choices. The required Baird panel follows either divergence alternative.
- Native reuse comes from [old deck 6, Value Function Approximation](<../../../sources/current_course/6 - Value Function Approximation.pptx>) (“old Pn” = PPTX slide n, including hidden slides). Copy specified diagrams, equations or figures natively where possible, then apply the edits below. Keep no stale notes. [Its PDF](<../../../sources/current_course/6 - Value Function Approximation.pdf>) has different page numbers.
- Equations below are the correctness specification. Follow the [notation guide](../../notation_guide.md): bold vectors, lower-case estimates with hats, superscript policy marks, reward index `t+1`, ∇ with respect to **w**, VE(**w**), **x**(s,a). Use μ only for on-policy state weighting. In one-weight examples **w** = (w); w has no time subscript. Coordinates use “column” and “row”. Do not introduce Π or the book's fixed-point matrices.
- Remove old P30 Q-Pacman; P37–40 average reward; P48/P51–55 gradient-TD detail; P62–74 least squares; P59 backward traces; and repeated P6/P60 motivation/recaps. P57–58 are source pointers for Week 6, not slides here. No new reading, assessment or exam-bridge claim. The book and external courses below are preparation references.

## Timing and route order

5.1 common order is F00–F11 → **F12-A/F12a-A/F13-A** or **F12-B/F12a-B/F13-B** → F14–F18. Continue to G00 only in session 5.2.

| 5.1 IDs | Minutes |
| --- | ---: |
| F00, F01, F02, F03, F04 | 0.5 + 2 + 3 + 3 + 2 |
| F05, F06, F07 | 3 + 3 + 3 |
| F08, F08a | 3.5 + 1.5 |
| F09, F10, F11 | 3 + 3 + 2 |
| F12-A, F12a-A, F13-A | 3 + 5 + 6 = 14 |
| F12-B, F12a-B, F13-B (instead) | 3 + 6 + 6 = 15 |
| F14, F15, F15a, F16, F17, F18 | 2 + 2 + 2 + 2 + 2 + 2 |
| **Targets, grid / landmark route** | **58.5 / 59.5** |

5.2 common opening: G00 (0.5), G01 (2), G02 → one G03 picture → G04.

| Geometry route | G02 | G03-A or G03-B | G04 | Total |
| --- | ---: | ---: | ---: | ---: |
| Full | 5 | 6 | 2 | 13 |
| Short | 3 | 4 | 1 | 8 |

Then use one divergence route and the common ending:

| 5.2 route | Divergence order and minutes | Ending order and minutes | Session total |
| --- | --- | --- | ---: |
| Alt A, full geometry | I02 (3), I03 (5), I04 (8, including I05's feedback), I06 (4, including G09), I07 (8) | G10 (3), G11 (2, G12 in notes), G13 (6), G14 (2), G15 (1.5) | **58** |
| Alt A, short geometry | I02 (3), I03 (5), I04 (8), I05 (4), I06 (4, including G09), I07 (8) | G10 (3), G11 (2), G12 (1), G13 (6), G14 (2), G15 (1.5) | **58** |
| Alt B, full geometry | G05 (7), G06 (3), **G08 (4), G07 (7)**, G09 (2) | G10 (3), G11 (4), G12 (2), G13 (6), G14 (2), G15 (2) | **57.5** |
| Alt B, short geometry | Same as previous row | Same as previous row | **52.5** |

I05 is a renderable feedback continuation: in Alt A/full geometry its content is delivered within I04's eight minutes; in Alt A/short geometry it has its own four minutes. G12 remains renderable for the applicable routes. Group each divergence alternative together in the file/deck; stable IDs need not sort numerically (G08 precedes G07 to define the triad before the intervention question).

**Time check.** Accepted planning allocations remain 58 + 58. Configured usable time is 70 × 0.85 = 59.5 per session. D8 permits 5.1's 58.5/59.5 targets; no route exceeds 59.5 or the 63-minute delivery allowance. Week totals range from 111 to 117.5 against 119 usable minutes. Targets include student work and essential spoken notes; duplicate alternatives are not additive. Arithmetic does not establish classroom feasibility. The tightest route is Alt A/full geometry: protect I04/I07 and G13; the short geometry route restores separate multiplier discussion. Unused time on Alt B/short geometry is feedback/buffer, not permission for another topic.

## Source register for preparation and reuse

- Old deck 6 is the substantial base: P4–11, P13–22, P25–29, P31–35, P41, P43–47; precise uses and corrections follow per slide. P24's convergence claims are replaced. P49–50 inform the geometry explanation only; their figure is not rendered.
- [Sutton & Barto](../../../sources/RLbook2020.pdf): §§9.2–9.4, printed 199–207 / PDF221–229; §9.5, printed 210–222 / PDF232–244; §9.7, printed 223 onward / PDF245 onward; §10.1, printed 243–246 / PDF265–268; §§11.2–11.4, printed 260–269 / PDF282–291. Book Figure 11.2 **right panel** is the expected DP-sweep demonstration, distinct from sampled off-policy TD.
- [Silver lecture 6](../../../sources/silver_rl/lectures/lecture-6-value-function-approximation-.pdf), PDF11–15 (features/gradients), PDF28–32 (instability); [CS234 lecture 4](../../../sources/stanford_cs234/lectures/lecture4post.pdf), PDF40–60 (approximation/triad); [CS285 lecture 8](../../../sources/berkeley_cs285/lectures/lec-8.pdf), PDF30–36 (fitting/instability bridge). These support explanation choices, not a new topic allocation.
- [Sutton on-policy prediction](../../../sources/sutton/18-19-onpolicy-prediction.pdf), PDF10–28; [on-policy control](../../../sources/sutton/20-onpolicy-control.pdf), PDF4–10; [off-policy approximation](../../../sources/sutton/26-offpolicy.pdf), PDF2–11; [Abbeel lecture 2](../../../sources/foundations-deep-rl-abbeel/l2-deep-q-learning.pdf), PDF14–17 and 19–29. Reuse the old course's Mountain Car figures, not an added external algorithm sequence.
- [Old Spring 2025 Midterm 1](../../../sources/current_course/exams/spring25/mt1/IntroToRLSpring25MT1.pdf), Q4, PDF12–13: source for the landmark-feature calculation. This provenance does **not** imply current midterm coverage.
- Continuity: accepted Week 4 decisions D10–D13. Expected SARSA is exposure; do not teach a new approximate Expected SARSA algorithm. Recall the tabular convergence conditions, P08 “Learning from someone else's data,” and the closing P10 “From tables to generalization.” Weeks 1–4 remain done.

## F00 — Function approximation

**Time:** 0.5. **Reuse:** old P1 title layout; replace text.

**Display:** COMP438/538 Reinforcement Learning · **Function Approximation** · Barış Akgün · Fall 2026. Subtitle: **5.1 — Linear approximation and semi-gradients**.

**Notes:** One deck across two meetings. Today we replace independent table entries with shared weights.

## F01 — From tables to generalization

**Time:** 2. **Reuse:** old P3 recap, reduced to the equations below.

**Display**

\[
V(S_t)\leftarrow V(S_t)+\alpha[U_t-V(S_t)].
\]

- MC: the target is a return.
- TD: the target bootstraps from another estimate.
- A table update directly changes one entry. Can experience improve predictions at other states?

**Notes:** Recall Week 4's final question. Prediction still means estimating a fixed policy's values; control adds policy improvement later. Answer: shared parameters can transfer an update across states, for better or worse.

## F02 — Too many states, too little experience

**Time:** 3. **Reuse:** old P4–5 scale/Pacman illustrations; retain the Pacman board, remove unsupported numerical state-count claims.

**Display:** **Storage is only half the problem.** A large or continuous state space also makes repeated visits scarce. Similar situations may have related values. A representation decides which similarities matter.

**Question:** Two Pacman positions differ by one square. What information could make their values similar—or very different?

**Notes:** Invite food/ghost distances and obstacles. Nearby positions separated by a wall or a dangerous ghost need not have similar values. A table makes no direct cross-state parameter update; do not say it can never propagate information through TD backups.

## F03 — What must the approximator handle?

**Time:** 3. **Reuse:** old P8–9 list, reduced to the prompt and four requirements.

**Display:** **What would you use to predict value from a description of a state?** Then reveal: compact representation; updates from experience; generalization; useful gradients for updating weights.

**Notes:** About one minute brainstorming, then connect linear models/neural networks to supervised regression. RL adds correlated experience, action-dependent data and potentially changing targets. A differentiable model makes updates possible; it does not remove these problems. We begin with linear models so we can inspect the mechanism.

## F04 — A value estimate is now a function

**Time:** 2. **Reuse:** old P7 input/output diagram and equations; convert notation.

**Display**

\[
\hat v(s,\mathbf w)\approx v^\pi(s),\qquad
\hat q(s,a,\mathbf w)\approx q^\pi(s,a).
\]

State (or state and action) → **shared weights w** → predicted value. A network can alternatively output one value per discrete action. Typically many predictions share far fewer weights than a table has entries.

**Notes:** **w** is a vector of adjustable numbers, not a policy. The hat distinguishes a prediction from the true value. Fix π while developing prediction; no guarantee that all value functions fit this family. “Fewer weights” is a useful motivation, not a defining mathematical requirement.

## F05 — Which prediction errors matter?

**Time:** 3. **Reuse:** old P10 objective, corrected notation; book §9.2.

**Display**

\[
\mathrm{VE}(\mathbf w)=\sum_{s\in\mathcal S}\mu(s)
 [v^\pi(s)-\hat v(s,\mathbf w)]^2.
\]

μ(s): on-policy state weighting, summing to one. Shared weights may force a compromise: errors at heavily weighted states count more.

**Question:** Can a small average error hide a large error at a rarely visited state?

**Notes:** Yes. This is an evaluation objective, not a target we can directly observe. The distribution and representation are separate choices. For the grid later: episodes start at (1,1), and **every actual preterminal visit contributes**; this gives the physical-visit weighting declared in G02. It differs from first-visit sampling and from alternative discount-as-termination conventions. Do not derive occupancy weights here.

## F06 — If an oracle gave us the value

**Time:** 3. **Reuse:** old P11/P13 native squared-error/gradient equations; delete the assertion that sequential SGD equals one full-batch update.

**Display**

\[
\nabla_{\mathbf w}\frac12[v^\pi(s)-\hat v(s,\mathbf w)]^2
 =-[v^\pi(s)-\hat v(s,\mathbf w)]\nabla\hat v(s,\mathbf w),
\]
\[
\mathbf w\leftarrow\mathbf w+\alpha
 [v^\pi(s)-\hat v(s,\mathbf w)]\nabla\hat v(s,\mathbf w).
\]

**Prediction error × sensitivity to the weights.** Replace the inaccessible true value by a target from experience.

**Notes:** ∇ means gradient with respect to **w**, not state. Negative loss gradient gives the plus sign in the update. Sampling states with the chosen weights gives a stochastic-gradient route to the weighted objective. The half absorbs the factor two; no new objective symbol is needed.

## F07 — Monte Carlo supplies a target

**Time:** 3. **Reuse:** old P14 gradient-MC equation/box, shortened to this update; book §9.3.

**Display**

\[
U_t=G_t,\qquad
\mathbf w\leftarrow\mathbf w+\alpha[G_t-\hat v(S_t,\mathbf w)]
 \nabla\hat v(S_t,\mathbf w).
\]

Fixed-policy trajectories supply noisy return labels. Wait until the return is available; update the prediction toward it.

**Notes:** Every-visit gradient MC uses each visit's return, unlike the first-visit sample-average example in Week 3. State this distinction once. For a fixed policy the conditional mean return is v^π(s); appropriate sampling and step-size assumptions are needed for convergence. Linear models have a convex squared-error objective; nonlinear models do not inherit a global-optimum guarantee. Do not claim that constant-step MC converges exactly or that all nonlinear methods reach a local minimum.

## F08 — TD supplies a moving target

**Time:** 3.5. **Reuse:** old P15, retaining its terminology disclaimer but replacing the blanket linear-convergence sentence; book §9.3.

**Display**

\[
U_t=R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w),\qquad
\delta_t=U_t-\hat v(S_t,\mathbf w),
\]
\[
\mathbf w\leftarrow\mathbf w+\alpha\delta_t\nabla\hat v(S_t,\mathbf w).
\]

**Semi-gradient:** differentiate the current prediction; treat the target as fixed in this update. The target also depends on **w**. This is **not, in general, a true gradient method** for the value-error objective.

Small disclaimer: **“I might refer to these as gradient methods in class.”**

**Notes:** Bootstrap immediately instead of waiting for an episode. If differentiating the sampled half-squared TD error fully, the derivative also contains the next prediction's derivative; the displayed rule deliberately omits that part. Do not turn this into a residual-gradient derivation. Terminal continuation is zero. The formal name remains semi-gradient even with the instructor's shorthand.

## F08a — Semi-gradient TD: the loop

**Time:** 1.5, within F08's five-minute block. **Reuse:** old P16 native algorithm box; replace with the following loop.

**Display**

1. Initialize **w**; run the fixed policy π.
2. At nonterminal S_t, take A_t ∼ π(·∣S_t); observe R_{t+1}, S_{t+1}.
3. If terminal: U_t = R_{t+1}. Otherwise: U_t = R_{t+1} + γv̂(S_{t+1}, **w**).
4. Compute δ_t = U_t − v̂(S_t, **w**) and ∇v̂(S_t, **w**) using the **same pre-update weights**.
5. Update **w** ← **w** + αδ_t∇v̂(S_t, **w**). Continue, or restart after termination.

**Notes:** No terminal-state feature or gradient is needed. Ask which two predictions use the old weights: both current and next. This becomes the invariant in the numerical exercise.

## F09 — Linear in the weights

**Time:** 3. **Reuse:** old P17–18 native equations; convert f to **x** and replace old value notation.

**Display**

\[
\hat v(s,\mathbf w)=\mathbf w^\top\mathbf x(s)=\sum_{i=1}^{d}w_i x_i(s),
\qquad \nabla\hat v(s,\mathbf w)=\mathbf x(s),
\]
\[
\mathbf w\leftarrow\mathbf w+\alpha\delta_t\mathbf x(S_t).
\]

**Linear in w. Features may be nonlinear functions of the input.** A constant feature can supply an intercept.

**Notes:** A distance, square, tile indicator or cosine feature can be nonlinear in the raw state description while the value remains linear in the adjustable weights. One-hot features recover the tabular update. Each feature scales a component's change; a zero feature leaves that component unchanged.

## F10 — Features decide what the learner can distinguish

**Time:** 3. **Reuse:** old P19–20 feature/Pacman illustrations; replace f labels by x_i(s).

**Display:** Example features: a constant; distance to food; distance to a ghost; indicators for nearby danger. **Which distinctions have we thrown away?** Identical feature vectors force identical predictions for every **w**.

**Notes:** A useful feature must be computable from the agent's available information. Distance alone may omit walls or direction. Distinguish an omitted feature of a fully observed state from information unavailable in the observation. More weights cannot recover absent information without changing the inputs/state representation.

## F11 — How much should states share?

**Time:** 2. **Reuse:** old P21–22; keep one compact overlapping-tile diagram, not the original text catalogue.

**Display:** One-hot: one independent weight per state. Aggregation: one prediction per group. Overlapping tiles/coarse coding: nearby states share some active weights. RBFs: smooth local features. Fourier features: a fixed basis of oscillations.

**Visual:** Three small editable panels: independent cells; grouped cells; two offset tilings of a continuous input plane. Highlight one state and the active cells in both tilings.

**Notes:** Contrast one-hot with overlapping sharing. More flexible features can improve representability but change the update coupling too. RBF/Fourier are names and intuition only; no feature-engineering derivation or homework requirement. Delete old “any known function” claim and old assigned-reading instruction.

## F12-A — Alt A · Grid: two weights for three states

**Choice:** 5.1 example, Alt A. **Time:** 3. **Reuse:** new editable grid using the accepted earlier-course model; old P17–18 equation layout only.

**Display**

Top row: (1,2), (2,2) goal. Bottom row: (1,1) start, (2,1). Coordinates = (column,row). Policy: always right. γ = 0.5; α = 0.1. Goal entry: +1 total; other transitions: −0.04; terminal continuation: 0.

\[
\mathbf x(s)=(1,\text{Manhattan steps to goal})^\top,
\qquad \mathbf w=(0.6,-0.2)^\top.
\]

| State | Features | Initial prediction |
| --- | --- | ---: |
| (1,1) | (1,2) | 0.20 |
| (2,1) | (1,1) | 0.40 |
| (1,2) | (1,1) | 0.40 |

**Notes:** Alt A, 5.1 example. For reference values the full model is: intended direction 0.8, each perpendicular slip 0.1; walls leave the state unchanged. Students need only the supplied samples to update. The goal is not approximated. First identify the two aliased cells; they are distinct states with identical features.

## F12a-A — Alt A · Two samples pull shared weights

**Choice:** 5.1 example, Alt A. **Time:** 5. **Reuse:** new calculation table, staged reveals.

**Display initially:** Compute the target, TD error, new weights and all three predictions. Use the current weights for both predictions in each target.

- **Sample A:** (1,2), right, +1, goal.
- **Sample B:** (2,1), right, −0.04, (2,1), starting with the weights obtained from A. **A separately supplied sample, not the next transition after termination.**

**Reveal answers**

| Sample | U_t | δ_t | New weights | Predictions at (1,1), (2,1), (1,2) |
| --- | ---: | ---: | --- | --- |
| A | 1 | 0.6 | (0.66, −0.14) | (0.38, 0.52, 0.52) |
| B | −0.04 + 0.5(0.52) = 0.22 | −0.30 | (0.63, −0.17) | (0.29, 0.46, 0.46) |

**Notes:** Alt A, 5.1 example. Protect approximately three minutes of student calculation and two of feedback. A changes both components by +0.06; B changes both by −0.03. The nonvisited cells move too, and the start cell moves by three times the component increment. Sample B is possible because a right move meets the wall. Two samples are not evidence of convergence.

## F13-A — Alt A · Is the representation sufficient?

**Choice:** 5.1 example, Alt A. **Time:** 6. **Reuse:** same grid/table, new exact reference values.

**Display**

| State | True v^π, always right | Prediction after B |
| --- | ---: | ---: |
| (1,1) | 0.05091 | 0.29 |
| (2,1) | 0.11636 | 0.46 |
| (1,2) | 0.83636 | 0.46 |

**Questions:** Can any two weights fit this policy's values exactly? What feature would let the two aliased cells differ? Does the answer necessarily stay the same if the policy changes?

**Reveal:** No exact fit for this policy: the last two values must be equal in our model. A constant, a top-row indicator and a right-column indicator distinguish the three nonterminal states. **Some value functions cannot be represented; whether this policy's can depends on the policy.**

**Notes:** Alt A, 5.1 example. Reference values were solved from the known model; the learner does not receive them as targets. Exact fractions are 14/275, 32/275, 46/55. For features (constant, top row, right column), exact weights are (14/275, 216/275, 18/275). To answer the policy-dependence question, reveal only after discussion: with up at (1,1) and (2,1), right at (1,2), true values are (199/550, 469/550, 469/550), which the original two features can fit, with weights (739/550, −270/550). This is a policy-specific symmetry, not a claim that two features represent every value function. No second policy-evaluation exercise is required.

## F12-B — Alt B · Landmark features

**Choice:** 5.1 example, Alt B. **Time:** 3. **Reuse:** old Spring 2025 Midterm 1 Q4, PDF12–13; recreate just the positions/landmarks needed here. Do not carry over its later reward diagram or exam labels.

**Display:** Separate robot example. Coordinates = (column,row). Landmarks at (3,3) and (4,2). Four features: column; row; Manhattan distance to (3,3); Manhattan distance to (4,2).

| State | **x**(s) |
| --- | --- |
| (2,1) | (2,1,3,3) |
| (2,2) | (2,2,2,2) |
| (2,3) | (2,3,1,3) |

Initialize four weights to zero. α = 0.2; γ = 0.5. Observe two **nonterminal** transitions: (2,1) → (2,2) → (2,3), each with reward −0.1.

**Notes:** Alt B, 5.1 example. Different task from the two-by-two grid; do not import its rewards. Mark landmarks and the path on an editable coordinate diagram. The four scalar features are x₁(s) through x₄(s), not a new symbol for distance.

## F12a-B — Alt B · Compute two weight updates

**Choice:** 5.1 example, Alt B. **Time:** 6. **Reuse:** new answer table grounded in Q4's feature construction.

**Display initially:** Compute U_t, δ_t and **w** after each sample. Before the second update, recompute **both** state predictions with the updated weights.

**Reveal answers**

| Sample | Current prediction | Next prediction | U_t | δ_t | New weights |
| --- | ---: | ---: | ---: | ---: | --- |
| First | 0 | 0 | −0.1 | −0.1 | (−0.04, −0.02, −0.06, −0.06) |
| Second | −0.36 | −0.38 | −0.29 | 0.07 | (−0.012, 0.008, −0.032, −0.032) |

**Notes:** Alt B, 5.1 example. Four minutes working/pair comparison; two feedback. First increment is −0.02(2,1,3,3); second is 0.014(2,2,2,2). A negative reward can accompany a positive TD error because the target is less negative than the current prediction. No claim about convergence or feature sufficiency follows from two updates.

## F13-B — Alt B · Missing information cannot be fitted

**Choice:** 5.1 example, Alt B. **Time:** 6. **Reuse:** new two-state diagnostic, distinct from both other tasks.

**Display:** Two fully observed states have **the same selected feature vector**. From one, the next transition terminates with +1; from the other, with −1. Both appear equally often.

**Questions:** Can the model fit both? What is the best common prediction? Would adding nonlinear layers with these same inputs solve it?

**Reveal:** The true values are +1 and −1. Any common prediction compromises; zero minimizes their equally weighted squared error, which is 1. A nonlinear function of identical inputs still gives identical outputs. Change the inputs to retain the distinguishing information.

**Notes:** Alt B, 5.1 example. Allow three minutes discussion and three feedback. If the distinguishing information is observed but discarded, retain it as a feature. If it is absent from the observation, a different state/history representation may be needed; no architecture can infer an unobservable distinction perfectly by adding capacity alone. This is representation insufficiency, not evidence that TD diverges.

## F14 — Representation and learning rule are different questions

**Time:** 2. **Reuse:** old P24's location, replacing its convergence claims with this distinction.

**Display:** **Can the model express the answer?** Examine features and true values. **Will this update find a useful answer?** Examine targets, data and update dynamics. Good representation alone does not answer the second question.

**Notes:** Use whichever example was selected. Leave convergence/fixed-point details for G02; do not duplicate them here. The two calculations showed how weights move, not their eventual behavior.

## F15 — Action values use the same machinery

**Time:** 2. **Reuse:** old P25–29/P31 equations. Fix P27's zero-error expression: target minus prediction, not prediction minus itself. Remove old P30 Q-Pacman.

**Display**

\[
\hat q(s,a,\mathbf w)=\mathbf w^\top\mathbf x(s,a),\qquad
\mathbf w\leftarrow\mathbf w+\alpha[U_t-\hat q(S_t,A_t,\mathbf w)]\nabla\hat q(S_t,A_t,\mathbf w).
\]

| Method | Nonterminal target U_t |
| --- | --- |
| Semi-gradient Sarsa | R_{t+1} + γq̂(S_{t+1}, A_{t+1}, **w**) |
| Approximate Q-learning | R_{t+1} + γ max_a q̂(S_{t+1}, a, **w**) |

**Terminal target: R_{t+1}.** In the linear case, the gradient is **x**(S_t,A_t).

**Notes:** The action is part of the prediction input (or selects an output). Recall Week 4's sampled-next-action versus greedy target; the behavior/target distinction survives replacement of the table. Expected SARSA was exposed there, but no extra approximate algorithm is added here. These equations are update rules, not tabular convergence guarantees.

## F15a — Semi-gradient Sarsa: keep the sampled next action

**Time:** 2. **Reuse:** old P32 native box; book §10.1. Replace notation and terminal branch with this specification.

**Display**

1. Initialize **w**. At an episode start S₀, choose A₀ ε-greedily from q̂(S₀,·,**w**).
2. Execute A_t; observe R_{t+1}, S_{t+1}.
3. If terminal, set U_t = R_{t+1}.
4. Otherwise choose A_{t+1} ε-greedily using the current weights, and set U_t = R_{t+1} + γq̂(S_{t+1},A_{t+1},**w**).
5. Update **w** ← **w** + α[U_t − q̂(S_t,A_t,**w**)]∇q̂(S_t,A_t,**w**), all quantities on the right evaluated before the update.
6. If nonterminal, **execute that same A_{t+1} next**. If terminal, restart.

**Notes:** Greedy ties are broken uniformly; exploratory choice is uniform over available actions. Do not draw another action after the update and pretend it was the one used in the Sarsa target. A changing policy makes this control, so fixed-policy prediction results do not by themselves guarantee control convergence.

## F16 — Mountain Car: a compact representation for continuous states

**Time:** 2. **Reuse:** old P33 problem illustration and cost-to-go figure; old P34 RBF figure as a second build. Preserve figure attribution. No new learning-curve comparison.

**Display:** State: **position and velocity**. Actions: push left, no push, push right. Reward: −1 per transition until the goal. The underpowered car must build momentum. **Linear Sarsa + tile-coded features.**

Figure caption: **Cost-to-go, −max_a q̂(s,a, w)**. Second build: **A different feature representation: radial basis functions.**

**Notes:** Explain the swing away from the goal before pointing to the value surface. Rename physical axes “position” and “velocity” to avoid clashing with **x**. Keep the inherited plot's axes/units faithful. The RBF figure illustrates another representation, not a controlled claim that one method performs better. Problem setting and figures only; no extra algorithm or implementation requirement.

## F17 — From fixed features to learned features

**Time:** 2. **Reuse:** old P8–9 approximator menu reduced to a small neural-network diagram; Abbeel L2 supports the connection.

**Display:** Fixed features → linear value head. Learned features → value head trained with the rest of the network. Richer models can express more structure; shared updates and moving targets remain.

**Notes:** A network's last layer can be linear while the complete function is nonlinear in all trainable weights. Learning features may address an inadequate fixed basis, but not information absent from the inputs. Neural value methods are motivated here; DQN mechanisms begin in Week 6.

## F18 — One update, many predictions

**Time:** 2. **Reuse:** new synthesis using F09's equation; do not copy old P60's target catalogue.

**Display:** Choose what the model can distinguish. Choose a target from experience. Update shared weights. Inspect both prediction quality and learning dynamics.

**Exit question:** If v^π can be represented exactly, must semi-gradient TD learn it?

**Notes:** Leave the answer as “not without further conditions”; session 5.2 supplies the counterexample. Mention only what today's calculation established: one sample changes multiple predictions. No assertion that the two-update example converged.

## G00 — Approximation instability

**Time:** 0.5. **Reuse:** title/section-divider style.

**Display:** **5.2 — Approximation instability**. Subtitle: **When sharing a value estimate changes the learning dynamics.**

**Notes:** Visible session boundary. Begin this slide at the second meeting, not as extra 5.1 material.

## G01 — Can a useful update become self-reinforcing?

**Time:** 2. **Reuse:** old P41 motivation, rewritten with the known update.

**Display**

\[
\mathbf w\leftarrow\mathbf w+\alpha
 [R_{t+1}+\gamma\hat v(S_{t+1},\mathbf w)-\hat v(S_t,\mathbf w)]\mathbf x(S_t).
\]

Changing **w** changes the current prediction **and** future targets. We need to distinguish a stable compromise from growing error.

**Notes:** Retrieve the three ingredients: shared features, bootstrap target, and the data on which updates are made. Terminal continuation remains zero. Recall Week 4's tabular convergence conditions; replacing the table changes their applicability.

## G02 — What would “converged” mean?

**Time:** 5 full / 3 short. **Reuse:** replace old P24's convergence slide; book §§9.2–9.4. New computed table.

**Display:** **Computed best fit and TD fixed point — not sampled learning curves.** Small grid inset: always right, γ = 0.5, features (1, steps to goal); goal entry +1, otherwise −0.04. Episodes start at (1,1); every actual preterminal visit contributes.

| State | μ(s) | True v^π | Best fit for VE | TD fixed point |
| --- | ---: | ---: | ---: | ---: |
| (1,1) | 9/82 | 0.05091 | 0.05091 | 0.02099 |
| (2,1) | 36/41 | 0.11636 | 0.12623 | 0.13319 |
| (1,2) | 1/82 | 0.83636 | 0.12623 | 0.13319 |
| Weighted squared error | | | **0.00624** | **0.00638** |

**Takeaway:** Linear on-policy TD can settle at a stable point that is not the minimum of VE. A constant step size generally produces fluctuations rather than exact convergence.

**Notes:** If 5.1 used landmarks, introduce the grid from this inset; do not assume students saw the alternate. The full transition/reward specification is in F12-A's notes. True values and both limiting fits are computed from that model, not inferred from two samples or a simulation. The rare upper-left cell contributes little to this objective despite a large error. Every-visit and first-visit weighting differ. Full route: ask students to locate the largest error and explain the compromise; short route: state those observations and preserve the table's distinction. The standard linear-TD bounds need their distribution/task assumptions; no theorem or numeric error bound is claimed for this episodic example here.

## G03-A — Alt A · Geometry: the grid's shared predictions

**Choice:** geometry P1, Alt A. **Time:** 6 full / 4 short. **Reuse:** new editable 2D chart from G02, using old P49–50 only as conceptual inspiration; do not import their 3D figure or error-vector labels.

**Display:** Axes: horizontal predicted value at (2,1), vertical predicted value at (1,2), both from 0 to 0.9. Equal aspect ratio. The representable pairs lie on the diagonal. **This is a coordinate view of a three-state model.**

Build the following marks, with short labels; offset the two nearby diagonal labels with leader lines:

| Build | Pair | Label |
| --- | --- | --- |
| 1 | diagonal | Same features → equal predictions |
| 2 | (0.11636, 0.83636) | True values |
| 3 | (0.47636, 0.47636) and (0.12623, 0.12623) | Equal-state best fit / on-policy-weighted best fit |
| 4 | (0.13319, 0.13319) | TD fixed point |
| 5 | (0.12394, 0.79971), arrow from TD point, then arrow back | Exact backup / weighted best fit of backup |

Small companion text/table: **The start-state coordinate is independent of this pair.** Its true and best-fit value is 0.05091; its TD value and backup at that fixed point are 0.02099.

Caption: **Exact backup-and-fit picture of a fixed point; not the path of one sampled TD update.**

**Notes:** Alt A, geometry. Each pair value is w₁+w₂; the start prediction is w₁+2w₂, so it can vary independently. Do not call this a slice with the start fixed at its true value, or say that the start is always fitted exactly. The on-policy pair weights have ratio 72:1, giving the near-horizontal-coordinate compromise; equal weights define a different objective. At the TD fixed point a full exact backup gives (0.02098701, 0.12393766, 0.79970909) in the three-state order; fitting that backup using μ returns the same TD predictions. Only this full-vector interpretation justifies the return arrow. Full route: explain all five builds. Short route: show builds 1–4, state the fixed-point interpretation without animating the backup arrows. Neither route teaches that each incremental TD step projects a whole value function.

## G03-B — Alt B · Geometry: one weight, two predictions

**Choice:** geometry P2, Alt B. **Time:** 6 full / 4 short. **Reuse:** new editable line diagram; book §11.4 supplies the best-fit/fixed-point distinction.

**Display setup:** A separate two-state reward variant, **for this picture only**. π goes to R from either state. γ = 0.9. L → R reward 0; R → R reward **+1**. Predictions: v̂(L,w) = w, v̂(R,w) = 2w. True values: (9,10).

Axes: horizontal v(L), vertical v(R), equal physical unit scales, ranges 0–10 and 0–13. Representable line: (w,2w). Build the table's points with labels:

| Weighting/object | Pair |
| --- | --- |
| True values | (9,10) |
| Equal-state best fit | (5.8,11.6) |
| Best fit with state weights (0.1,0.9) | (5.10811,10.21622) |
| On-policy weighting μ = (0,1): best fit **and TD fixed point** | (5,10) |

Full-route final build: arrow from (5,10) to its exact backup (9,10), then back to its on-policy best fit (5,10). Caption: **Exact backup-and-fit picture, not one sampled TD update.**

**Notes:** Alt B, geometry. Define the two states here even if the complete divergence example follows later. The three weighting choices are **different objectives**. Do not use their different best fits as evidence that TD misses the best fit of the same objective. Here on-policy visits ultimately occur only at R; L has zero weight, and the TD fixed point also minimizes that on-policy objective. G02, separately, provides the same-objective example where TD and best fit differ. The true values satisfy 10 = 1 + 0.9(10), 9 = 0.9(10). For equal-state weights, minimize (9−w)²+(10−2w)² to get w = 5.8; for (0.1,0.9), w = 189/37. Full route: all points and arrows; short: omit backup arrows, retain explicit weighting labels. **Reset rewards to zero** before either divergence construction. The +1 reward is not used to establish divergence.

## G04 — A tabular guarantee does not transfer automatically

**Time:** 2 full / 1 short. **Reuse:** old P41 motivation and book §11.4, without a contraction proof.

**Display:** A Bellman backup and a best fit are different operations. The fit depends on both the function family and state weighting. **The tabular guarantee does not automatically survive fitting with a different state weighting.**

**Notes:** Week 2's discounted exact backup contracts differences between tables. The picture adds fitting in a particular weighted error measure; it does not prove the same statement for every approximate/sample-based update. Linear on-policy TD has stability results under appropriate conditions. Next: a concrete way different state frequencies and shared bootstrapped predictions can cause growth. No projection operator symbol, norm proof or gradient-TD algorithm.

## I02 — Alt A · A single update raises its own target

**Choice:** 5.2 divergence, Alt A. **Time:** 3. **Reuse:** old P43 two-state diagram, changing γ to 0.9 and deleting its threshold claim.

**Display:** **Mechanism fragment, not yet a complete process.** v̂(L,w) = w, v̂(R,w) = 2w; R_{t+1} = 0, γ = 0.9, α = 0.1, w = 10. Supply L → R.

\[
U_t=18,\quad\delta_t=8,\quad w\leftarrow10+0.1(8)(1)=10.8.
\]

Predictions move (10,20) → (10.8,21.6). The update raises the target state's prediction too.

**Notes:** Alt A, 5.2 divergence. Ask what happens when R is updated: an isolated transition cannot answer. The next slide completes the task and specifies exactly which updates are made. If G03-B was used, explicitly announce the switch to **all rewards zero**.

## I03 — Alt A · Complete the task and the update experiment

**Choice:** 5.2 divergence, Alt A. **Time:** 5. **Reuse:** extend old P43 diagram with editable action arrows and a data-rule box.

**Display**

- Two states L,R; two actions “go L”, “go R”. Each action deterministically reaches its named state from either state.
- Continuing task; **all rewards 0**, γ = 0.9. Thus v^π(L) = v^π(R) = 0, exactly representable by w = 0.
- Target π always chooses “go R”. Behavior b chooses each action with probability 1/2 at either state. Its stationary state frequencies are (1/2,1/2); the target's are (0,1).
- **Rule of this experiment:** retain target-action transitions and balance the two source states. Each update uses one L → R and one R → R. Compute both contributions using the **same saved w**, average them, then apply α = 0.1 once.

**Notes:** Alt A, 5.2 divergence; **C01 remains for instructor review**. This is an explicitly constructed mean-update experiment, not a generic prescription for off-policy learning. The symmetric behavior can supply both retained transitions; its other transitions are deliberately not used under this experiment's rule. Do not say all off-policy algorithms discard non-target actions. No importance ratio, correction derivation or new off-policy algorithm. Broader correction mechanisms belong to the accepted later off-policy unit. Distinguish the behavior's state frequencies from the target continuation used in both labels.

## I04 — Alt A · Work out the balanced update

**Choice:** 5.2 divergence, Alt A. **Time:** 8. **Reuse:** new editable exercise table.

**Display initially:** w = 10. Fill in both target-action transitions, average their **gradient-scaled errors**, and update once.

| Transition | Current prediction | Next prediction | Target | TD error | Gradient | Error × gradient |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| L → R | 10 | 20 | 18 | 8 | 1 | 8 |
| R → R | 20 | 20 | 18 | −2 | 2 | −4 |

Reveal: mean contribution = (8−4)/2 = 2; **w = 10.2**. Repeating from the new saved weight gives **10.404**.

**Notes:** Alt A, 5.2 divergence. Give about four minutes to work/pair-check, then feedback. Averaging raw TD errors or updating w between rows implements a different experiment. At general w, the two contributions are 0.8w and −0.4w; their mean is 0.2w. In the full-geometry route, reveal I05's recurrence during the remaining feedback time; it has no additional minutes. In the short route, leave the recurrence to the separately timed I05.

## I05 — Alt A · A small growth factor compounds

**Choice:** 5.2 divergence, Alt A. **Time:** within I04 in full route / 4 in short route. **Reuse:** new recurrence; old P43's threshold sentence omitted.

**Display**

\[
w\leftarrow w+\alpha(0.2w)=1.02w\quad(\gamma=0.9,\ \alpha=0.1).
\]

10 → 10.2 → 10.404 → … . True values stay zero. Both predictions grow in magnitude. A smaller positive step size slows growth in this experiment; it does not change its direction.

**Notes:** Alt A, 5.2 divergence. Only the numeric γ = 0.9 case is shown live, with no discount threshold. This is an exact deterministic mean recurrence, not a claim that every stochastic sample path grows monotonically. The Baird picture at G10 supplies the required larger-scale visual; **C02's visual preference remains for instructor review**. Do not add an unaccepted extra time block for a second growth chart.

## I06 — Alt A · Locate the three ingredients

**Choice:** 5.2 divergence, Alt A. **Time:** 4, includes the G09 callback. **Reuse:** old P47 triad graphic, corrected labels and no universal “any two are safe” conclusion.

**Display:** **Function approximation:** one weight couples L and R. **Bootstrapping:** predictions appear in the target. **Off-policy state weighting:** equal source-state updates differ from target-policy visits.

Two data questions: **Does the target represent the right continuation?** **Which states dominate the updates?**

**Notes:** Alt A, 5.2 divergence. The experiment makes target continuation exact, yet the state-frequency mismatch remains. Recall Week 4 P08: learning from someone else's data raises both questions. Neither question was solved generally by Week 4's Q-learning target. No correction formula. The deadly triad names a mechanism allowing failure, not a statement that every such method diverges or that any arbitrary pair of ingredients is safe.

## I07 — Alt A · Change one component, keep the task

**Choice:** 5.2 divergence, Alt A. **Time:** 8. **Reuse:** new two-column activity; use the same complete MDP, features, γ, α and initial w from I03.

**Display initially:** Predict the direction of the update for each separate intervention. The true value is still zero and the model can represent it.

| Change | Update data / target | Reveal |
| --- | --- | --- |
| Use target-policy stationary states | Only R → R; same bootstrap target | Contribution = (0.9·2w−2w)·2 = −0.4w; w ← 0.96w; 10 → 9.6 → 9.216 |
| Remove bootstrapping | Same balanced source states; replace both targets by their known zero returns | Mean contribution = [(-w)·1 + (-2w)·2]/2 = −2.5w; w ← 0.75w; 10 → 7.5 → 5.625 |

**Notes:** Alt A, 5.2 divergence. Four minutes discussion/calculation, four feedback. Each row separately changes one component of I03, not both at once. The first row is a stationary-distribution comparison; it is not a coverage guarantee for arbitrary other features or tasks. Here reducing the shared weight also corrects L. The second uses returns known to be zero because every reward is zero in the continuing discounted task; it does not require waiting for an infinite trajectory and is not a generic off-policy Monte Carlo estimator. These interventions explain this example; they are not a blanket convergence theorem.

## G05 — Alt B · Repeating a transition fragment

**Choice:** 5.2 divergence, Alt B. **Time:** 7. **Reuse:** old P43 diagram and its no-discount arithmetic; remove the discount-threshold sentence.

**Display:** **Mechanism fragment: only the shown transition is updated.** v̂(L,w) = w, v̂(R,w) = 2w. Reward 0, γ = 1, α = 0.1, initial w = 10. Repeatedly supply L → R.

**Question:** Compute three updates.

| Update | w before | Target | TD error | w after |
| --- | ---: | ---: | ---: | ---: |
| 1 | 10 | 20 | 10 | 11 |
| 2 | 11 | 22 | 11 | 12.1 |
| 3 | 12.1 | 24.2 | 12.1 | 13.31 |

**Notes:** Alt B, 5.2 divergence. Four minutes student calculation, three feedback. This preserves the original fragment's γ = 1 case; it is distinct from Alt A's complete γ = 0.9 experiment. Do not silently mix their numbers. Only L-source updates are supplied; the fragment alone says nothing about the complete target-policy continuation or subsequent corrections. In particular, do not infer an MC return before specifying a completion. If geometry P2 was used, reset rewards to zero explicitly.

## G06 — Alt B · Why does repeating it grow?

**Choice:** 5.2 divergence, Alt B. **Time:** 3. **Reuse:** old P43 sharing explanation, replacing its unqualified off-policy conclusion.

**Display:** Updating the prediction at L also raises the prediction at R. Repeating only this transition gives **10 → 11 → 12.1 → 13.31 → …**. Each increase raises the next label. **What additional updates would a complete task supply?**

**Notes:** Alt B, 5.2 divergence. Explain the repeated 10% increase in this numeric fragment, without adding a general discount-factor multiplier/threshold discussion. D7's accepted γ = 0.9 multiplier is displayed on Alt A's I05 only. The fragment is a mechanism illustration, not by itself a complete MDP divergence proof. Book §11.2 makes this limitation explicit. Do not say “behavior takes another action, therefore an off-policy algorithm ignores it” as a general fact.

## G08 — Alt B · The deadly triad

**Choice:** 5.2 divergence, Alt B. **Time:** 4. **Reuse:** old P47 graphic; placed before G07 deliberately.

**Display:** Function approximation · Bootstrapping · Off-policy learning. Shared predictions can affect their own targets, while the update distribution differs from the target policy's visits.

**Question:** Which part would you change to investigate the growth mechanism?

**Notes:** Alt B, 5.2 divergence. Identify the sharing and bootstrap in G05; its selective updates motivate the distribution question but do not specify a complete off-policy process. “Any two are safe” is not a theorem for arbitrary nonlinear models/algorithms. G07 uses explicitly different completions, and G10 supplies a complete counterexample. No universal prediction/control convergence table.

## G07 — Alt B · Three separate constructions

**Choice:** 5.2 divergence, Alt B. **Time:** 7. **Reuse:** new comparison table replacing an implied controlled ablation of old P43.

**Display heading:** **Separate illustrative constructions—not one unchanged-task experiment.**

| Construction | Complete assumptions / supplied updates | Reveal |
| --- | --- | --- |
| Add the terminal correction | Episodic L → R → terminal, all rewards 0, γ = 1; same features and α = 0.1; update both transitions in sequence each episode | L step multiplies w by 1.1; R terminal step by 0.6. Episode: w ← 0.66w, 10 → 6.6 → 4.356 |
| Fit known zero returns | A zero-reward terminating continuation gives return 0 at L; only L is regressed on this known label | w ← 0.9w, 10 → 9 → 8.1 |
| Use independent table entries | Only L → R updates; fixed V(R) = 20, V(L) initially 10; α = 0.1, γ = 1 | V(L) ← V(L) + 0.1[20−V(L)]; 10 → 11 → 11.9 → … → 20 |

**Question:** Which construction removes sharing, which removes the bootstrap label, and which adds a correction the fragment omitted?

**Notes:** Alt B, 5.2 divergence; **R03 remains for instructor review of this presentation**. Three minutes predict/discuss, four feedback. Answers: independent table removes sharing; zero-return regression removes bootstrapping; the completed episode supplies the R update. The first row changes the task completion as well as the data relative to the fragment, so it is not a controlled one-component ablation. The second's zero return is now justified, but it is not a generic off-policy MC rule. The third is bounded but can remain wrong because R is never corrected: missing coverage has not disappeared. The first row evaluates a proper episodic process at γ = 1, avoiding an undefined nonterminating return assumption.

## G09 — Two off-policy questions

**Time:** 2 in Alt B; integrated in I06 for Alt A. **Reuse:** old P41 motivation; callback to accepted Week 4 P08, without copying that deck.

**Display:** **Whose continuation is in the target?** **Whose state frequencies determine the updates?** Matching one does not automatically fix the other.

**Notes:** Week 4 identified the policy/data distinction and left general correction open. Approximation makes the state weighting matter because states share parameters. Do not say “Q-learning needs no correction” as an established general result. No importance-sampling ratio or gradient-TD machinery here.

## G10 — Baird: a complete counterexample

**Time:** 3, either route. **Reuse:** old P44's seven-state diagram (PDF38), checked against book Figure 11.1 (printed 261 / PDF283), and **Figure 11.2 right panel** (printed 262 / PDF284). Retain source attribution; exclude the sampled-TD/ratio panel.

**Display:** **Linear approximation + bootstrapping + different state weighting can diverge—even with exact expected updates.** All rewards zero; γ = 0.99. Target action leads to the lower state. Uniform updates over all seven source states differ from target-policy visits. Zero values are exactly representable.

Figure caption: **Synchronous expected semi-gradient DP sweeps; α = 0.01.** Weight subscripts in the figure are **components, not time steps**. Add the value check: **The lower state's prediction w₇ + 2w₈ grows too; this is not just redundant weights moving.**

**Notes:** Keep the original diagram's upper predictions 2w_i + w₈ (i = 1,…,6) and lower prediction w₇ + 2w₈. Initial components: all 1 except w₇ = 10. Each sweep averages the seven gradient-scaled exact target errors, using the same pre-sweep vector. The right panel shows weight growth over repeated sweeps. Because w₈ grows strongly while w₇ remains comparatively small, the lower predicted value grows away from its true value zero. There is no sampling noise or changing policy in this demonstration. Do not introduce the behavior-action probabilities, importance ratios, a full feature matrix or another hand derivation. Distinguish this complete expected-update example from the fragment and from each path's two-state numerical parameters.

## G11 — State convergence claims with their conditions

**Time:** 2 Alt A / 4 Alt B. **Reuse:** replace old P24/P46 and any blanket prediction/control table; book §§9.3–9.4, 11.2–11.3.

**Display**

- **Linear gradient MC, fixed policy:** with appropriate sampling and step sizes, minimizes the weighted value-error objective; the best fit may still be wrong.
- **Linear on-policy semi-gradient TD, fixed policy:** under its conditions, approaches a TD fixed point; generally not the minimum of VE.
- **Off-policy linear TD:** can diverge, as just shown.
- **Nonlinear approximation / approximate control:** do not inherit the tabular guarantees merely by replacing a table with a function.

**Notes:** Alt A: quick synthesis; Alt B: ask students to explain the distinction between the first two rows. Suitable sampling, boundedness/regularity and step sizes matter; singular features may leave weights nonunique even when predictions are determined. A constant step size generally leaves noise. Do not promise global optimality for nonlinear MC, generic stability for nonlinear on-policy TD, or convergence of changing-policy approximate Sarsa/Q-learning from a fixed-policy theorem. The “any two” discussion in the linear setting is not an unconditional guarantee across arbitrary algorithms. In the Alt A/full route, add G12's short reassurance within these two minutes.

## G12 — Possible failure is not inevitable failure

**Time:** notes within G11 for Alt A/full; 1 Alt A/short; 2 Alt B. **Reuse:** old P45 heading only; delete its historical “no counterexample” and broad Q-learning claims.

**Display:** Counterexamples reveal missing guarantees and failure mechanisms. They do not say every approximate learner fails. Inspect representations, targets, update data and actual value error.

**Notes:** Smaller steps may reduce noise, but cannot reverse the positive mean-growth direction in I05. More expressive features may fix representation error, but do not automatically fix unstable updates. No present-day practice or research-status claim is needed to make this point.

## G13 — Diagnose three experiments

**Time:** 6, protected in every route. **Reuse:** new table; independently computed examples, not empirical performance claims.

**Display initially:** **Constructed examples: reference values are known.** Match each case to sufficient representation, insufficient representation, or unstable learning. What evidence distinguishes them?

| Case | Construction | Weight behavior | Value error |
| --- | --- | --- | --- |
| 1 | Always-right grid, one-hot features; on-policy expected TD | Finite fixed-point weights equal (0.05091, 0.11636, 0.83636) | Computed fixed-point VE = **0** |
| 2 | Same grid, same data weighting and expected TD; features (1, steps to goal) | Finite fixed-point weights (0.24540, −0.11221) | Computed fixed-point VE = **0.00638**; best possible VE = **0.00624** |
| 3 | Separate complete two-state task: zero rewards, γ = 0.9, v̂ = (w,2w), balanced target-action mean updates, α = 0.1 | w = **10 → 10.2 → 10.404** | Equally weighted squared value error = **250 → 260.1 → 270.60804** |

**Reveal answer:** 1: sufficient and stable here. 2: a representation error floor, plus the small TD-versus-best-fit difference. 3: unstable updates although w = 0 represents the exact answer.

**Notes:** Two minutes inspect, two discuss, two feedback. Cases 1–2 are a matched comparison: same grid/model, γ = 0.5, on-policy every-visit weighting from G02, expected TD with α = 0.1; only features differ. Their entries are **computed fixed points**, not claims about a finite noisy run. Case 3 is explicitly a different task. If Alt B was taught, briefly supply the full construction: two actions go to their named states, π always goes R, behavior chooses each with probability 1/2; balance retained L→R and R→R samples and average their contributions using the same w. At general w these are 0.8w and −0.4w, giving w ← 1.02w. This is enough to interpret the supplied data; no second worked derivation. Its error uses equal state weights, not μ: [(w−0)²+(2w−0)²]/2 = 2.5w². Show value error next to weights so changing parameter magnitudes alone is never the diagnosis. A plateau in a real finite run could also mean slow learning/noise; the known reference and analytic best fit distinguish this constructed case. Do not infer instability from poor return alone.

## G14 — Toward deep value learning

**Time:** 2. **Reuse:** old P57–58 as a future pointer only; no copied batch-method or least-squares slide.

**Display:** We want richer value functions, reusable experience and more stable targets. Next: **DQN—how the learning loop changes when a network estimates action values.**

**Notes:** F17 already motivated learned features; do not repeat the neural-network introduction. Preview replay and a separate target network as mechanisms to examine in 6.1, without equations or a claim that they eliminate all deadly-triad failures. No new required reading or assignment promise.

## G15 — Separate three questions

**Time:** 1.5 Alt A / 2 Alt B. **Reuse:** new synthesis.

**Display:** **Can it represent the answer?** **Which errors/data does it prioritize?** **Do the updates approach a useful answer?**

Exit check: “The true values are representable, the rewards are zero, and the updates use exact expectations. Is divergence ruled out?”

**Notes:** No: Baird and the complete two-state mean-update construction show otherwise. If Alt B was taught, Baird is the primary full-process evidence. Projection was explanatory exposure; the calculations to retain are semi-gradient updates and the selected divergence/intervention activity. End here; no out-of-scope appendix is added.
