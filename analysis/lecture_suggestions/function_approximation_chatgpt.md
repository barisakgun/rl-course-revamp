# Function approximation: independent initial suggestions

**Author:** ChatGPT, 2026-11-02. **Phase 7, workflow step 1 only.** This is an independent proposal for sessions 5.1–5.2, not accepted content or a first-render specification. Claude's Week 5 suggestions and AI-specific artifacts were not consulted. Weeks 1–4 are accepted as done; their shared decision records supply continuity only.

## Proposed next deck and session boundary

Recommend **one deck, `function_approximation`, spanning 5.1 `linear` and 5.2 `instability`**. The topic connects representation, the update it permits, and its failure modes; a visible session divider preserves the two distinct teaching tasks. This grouping is a proposal, not an accepted deck split. A separate DQN deck begins at 6.1.

- **5.1 ends** after students calculate a linear TD update, explain its effect on other states, diagnose missing information, and connect approximate values to the already-known control targets. They should know what is being fitted and why the update is a semi-gradient. Divergence is a question for the next session.
- **5.2 begins** with that question. Students work through a complete small divergent update, change the sampling distribution, and distinguish instability from representational error. Projection gets eight minutes of geometric intuition. Nonlinear approximation motivates 6.1 without introducing the DQN loop.
- Proposed slide targets: **58 + 58 minutes**, including explanation and worked reasoning. No carryover from Week 4 and no use of the optional 63-minute delivery allowance.

Authority: [topic decisions](../../decisions/topic_decisions.yaml), sessions `linear`, `instability`, `dqn_loop`, `dqn_diagnosis`; [lecture workflow](../../docs/lecture_workflow.md). The [generated session-source index](../../output/lectures/session_sources.md) was checked with `python3 scripts/build_session_sources.py --check` and is current. It locates evidence; it does not accept this proposal. A future shared deck decision file is the place for accepted choices and current deck status, once the workflow reaches instructor choices.

## Accepted commitments and continuity

| Commitment | Consequence for this suggestion |
| --- | --- |
| 5.1: 58 teaching minutes, no administration; prerequisite `control_practice`; feature-based TD update and missing-information diagnosis | Protect both calculation and diagnosis. Compress the feature catalogue, not these activities. |
| 5.2: 58 teaching minutes, no administration; prerequisite `linear`; a small divergent update and variation of one triad component | Make the sampling/update rule explicit and calculate the contrast. Full Baird analysis remains optional. |
| `approximation`: Core; derive, implement, analyze | Derive the update, trace the parameter mutation, and distinguish failure mechanisms. Nonlinear approximation supplies motivation, not a separate neural-network course. |
| `projection`: Exposure; explain; about eight minutes | Explain representable functions and fitting versus backing up. No projection matrix, projected-Bellman derivation, or gradient-TD algorithm. |
| A2: representation, instability, and a small DQN | Prepare the linear-update and diagnosis prerequisites only. A2 also depends on Week 6; no new task, release change, or completed-A2 prerequisite for Midterm 1. |
| Readings outside current planning | All source references below are instructor preparation. No required reading, reading-only examination dependency, or compensating video. |

See [assignment decisions, A2](../../decisions/assignment_decisions.md) and [reading decisions](../../decisions/reading_decisions.md).

Continuity from the accepted shared records:

- [MDP/value decisions](../../decisions/lectures/mdp_values.md): students have distinguished observations, histories and state information through the hidden-battery discussion. Reuse that distinction for a short feature-omission check, without changing the robot model.
- [Bellman decisions](../../decisions/lectures/bellman.md): Bellman backups and the discounted tabular error-contraction intuition are available. The 2×2 grid is a separate MDP from the larger grid, with entry rewards. Do not silently substitute new features, rewards or transitions into it.
- [MC/TD decisions](../../decisions/lectures/mc_td.md): MC, TD, n-step and a brief forward λ-return have been taught. Retrieve the target-versus-estimate distinction; do not re-teach return mixtures or introduce backward traces.
- [Control decisions](../../decisions/lectures/model_free_control.md), especially D6: SARSA and Q-learning establish behaviour versus target. **Importance sampling has not been introduced.** No ratio, correction derivation, or presumed IS prerequisite in Week 5. The Week 4 recording/delivery exception does not change Week 5's planning.

The existing grid remains continuity, not the source of a new multiweek example. Recommend the old course's landmark exercise and a separate, explicitly introduced two-state instability example below. These local example choices remain proposals for cross-review and instructor selection.

## Source basis and instructional use

The relevant old material is substantial: the approximation PPTX has **75 slides, 12 hidden**, while its PDF has **63 pages**. Below, **P** means the PPTX's one-based slide number and **PDF** means the exported page. The visible-slide mapping was checked against slide XML and PDF titles; important equations were also checked visually. These are reuse candidates, not instructions to overwrite any source deck.

| Source and provenance | Observed material and use in this proposal |
| --- | --- |
| [Old approximation PPTX](../../sources/current_course/6%20-%20Value%20Function%20Approximation.pptx) and [PDF](../../sources/current_course/6%20-%20Value%20Function%20Approximation.pdf), composite local baseline | Main base: scale/generalization, Pacman features, SGD/semi-gradient progression, control bridge, divergence and geometry. The delta below is against this material. |
| [Spring 2025 Midterm 1](../../sources/current_course/exams/spring25/mt1/IntroToRLSpring25MT1.pdf#page=12), pp. 12–13, dated 2025-04-28 | Actual assessment evidence: four landmark features and two TD weight updates. Adapt as live practice, not as a new exam commitment. |
| [Old Deep QL](../../sources/current_course/8%20-%20Deep%20QL.pdf#page=3), PDF3–5 | Explicit neural-value motivation and the constant-target convention. Supplies the handoff, while replay/target-network teaching stays in 6.1. |
| [Sutton & Barto, configured book](../../sources/RLbook2020.pdf) | §§9.2–9.4: prediction objective, MC/semi-gradient distinction and linear TD; §9.5: feature construction; §9.7: nonlinear motivation; §§11.2–11.4: divergence, triad, geometry. Precise pages accompany the mathematical choices below. |
| [Silver, Lecture 6](../../sources/silver_rl/lectures/lecture-6-value-function-approximation-.pdf), 2015 offering; [source URL](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-6-value-function-approximation-.pdf), local retrieval 2026-10-06 | PDF11–15 explicitly develop gradients, features, linear approximation and table lookup; PDF28–32 cover Baird and convergence comparisons. Keep the one-hot bridge; do not inherit an unqualified convergence checklist. |
| [CS234, Lecture 4 post-class slides](../../sources/stanford_cs234/lectures/lecture4post.pdf), Winter 2026; [source URL](https://web.stanford.edu/class/cs234/slides/lecture4post.pdf), retrieved 2026-10-06 | PDF40–54 motivate compact representation and replacing an oracle by MC/TD targets; PDF57–60 discuss control and instability. Useful motivation sequence. The TD expression on pp. 53–54 needs an explicit held-target convention if adapted; do not present its update as the full derivative through both occurrences of the weights. |
| [CS285, Lecture 8](../../sources/berkeley_cs285/lectures/lec-8.pdf), Spring 2026; [source URL](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-8.pdf), retrieved 2026-10-06 | PDF30–36 explicitly contrast tabular backups with fitted approximation and instability. Use the conceptual backup/fit distinction; the operator derivation is beyond this session's Exposure scope. |
| [CS224R Q-learning extra section](../../sources/stanford_cs224r/lectures/CS224R_Tutotial_Max.pdf), Spring 2026 discussion slides; [source URL](https://cs224r.stanford.edu/material/CS224R_Tutotial_Max.pdf), retrieved 2026-10-06 | PDF32 explicitly separates semi-gradient handling from using a target network. Useful for avoiding their conflation. PDF33–36's optimization and double-critic details are not additions to Week 5. This is tutorial evidence, not proof of mandatory main-lecture coverage. |
| [Sutton on-policy slides](../../sources/sutton/18-19-onpolicy-prediction.pdf), Fall 2017 CMPUT 366/609 | PDF10–21 explicitly develop parameterized prediction, state aggregation, the prediction objective and TD; PDF22–28 give feature constructions. Supports shared-feature generalization and the MC/TD distinction. Do not add another random-walk experiment merely because the source includes one. |
| [Sutton off-policy slides](../../sources/sutton/26-offpolicy.pdf), Fall 2017 CMPUT 366/609 | PDF2–8 distinguish target-policy predictions from the distribution of updated states and show instability even in prediction/planning. Use this distinction in words; skip its importance-sampling prerequisite and later gradient-TD derivations. |
| [Abbeel, Deep Q-learning](../../sources/foundations-deep-rl-abbeel/l2-deep-q-learning.pdf), Foundations of Deep RL, publication metadata points to 2021 | PDF14–17 explicitly motivate scaling/generalization and approximate Q-learning; PDF19–29 review neural networks. Use generalization motivation, not large state-count claims or an MLP/CNN/backpropagation lecture. |

External retrieval/offering metadata is in each `sources/<id>/lectures/index.json`. Local-baseline, Sutton and Abbeel files were inventoried on 2026-09-27; their manifests record existing-local provenance rather than an original download URL/date. That limitation is preserved. Coverage statements describe inspected material, not verified classroom time or a vote for inclusion. Teaching choices and minute estimates below are ChatGPT recommendations.

## Delta against the old approximation deck

| Action | Exact old references | Change, reason and destination of the teaching purpose |
| --- | --- | --- |
| Keep, tighten | P3–7 / PDF2–6 | Retain scale, the Pacman generalization question and value-function inputs/outputs. Remove the trace recap and say precisely that a tabular update does not directly change another entry. Distinguish dimensions of **w** from the vector itself when discussing compactness. |
| Compress and fix | P8–11 / PDF7–10 | Replace the approximator catalogue with linear features and a later neural alternative. Keep a short gradient refresher where needed for the update. Correlated samples and changing targets are RL challenges; differentiability alone does not solve them, and the Markov property does not imply independence. Minibatch/replay mechanics remain in 6.1. |
| Keep, reorder | P17–21 / PDF15–19 | Put features and linear values before the full gradient update. Preserve the one-hot/table-lookup bridge and one sentence on overlapping features. Omit Fourier/RBF construction and the old reading instruction. The purpose of the menu survives as a choice about which states share parameters. |
| Keep and qualify | P13–16, P20 / PDF11–14, PDF18 | Derive an update from a fixed numeric target, then substitute MC and TD targets. State why TD is semi-gradient. Remove the permission to call semi-gradients ordinary gradients. No implication that sequential SGD at changing weights equals one batch gradient step. |
| Keep within diagnosis | P22 / PDF20 | Representation must preserve task-relevant information. Use the missing-information activity instead of repeating a general project-engineering talk. |
| Fix | P24 / PDF21 (P23 is a hidden earlier version) | Replace “TD reaches the global optimum” with the distinction between the value-error optimum and the TD fixed point. On-policy linear TD has convergence results under their assumptions; it does not generally minimize value error. Book §9.4, printed pp. 205–207 / PDF227–229. No new proof sequence. |
| Compress; fix if reused | P25–29, P31–32, P35 / PDF22–25, PDF27–28, PDF31 (P28 hidden) | One approximate-Q bridge reuses SARSA/Q-learning targets and terminal handling. **P27's displayed error subtracts the linear prediction from that same prediction and is identically zero.** Replace its first term by the update target if that equation is reused. Avoid a second full control derivation/implementation. Continuous-action optimization belongs to Week 7; Double Q belongs to 6.2. |
| Omit live | P30, P33–34 / PDF26, PDF29–30 | Q-Pacman result and Mountain Car/tile/RBF demonstrations would add example setup. Pacman already motivates generalization; the landmark calculation demonstrates parameter sharing. No claim these sources were not taught. No live demo or student coding prerequisite. |
| Cut from this deck | P37–40 / PDF32–35 | Average reward's accepted brief contrast was in 3.1. Differential returns/updates and the claim that discounting becomes unhelpful are not Week 5 scope. Keep the useful representation-versus-stability question elsewhere; no new average-reward algorithm. |
| Keep and complete | P41, P43 / PDF36–37 | Preserve the question and the one-weight mechanism. Use γ = 0.9, rather than silently carrying “no discount” into a continuing task. Show the fragment's limitation, then give the complete sampling/update construction below. |
| Optional alternative | P44 / PDF38 | Baird is a complete source counterexample, but its seven states/eight parameters cost setup time. Recommend the smaller worked example as the default. Full Baird analysis remains optional, with no assumed homework or live minutes. |
| Replace | P45–46, P55–56 / PDF39–40, PDF49–50 | Drop the dated “no counterexample” claim about ε-greedy and the blanket convergence tables. Use a scoped statement about fixed-policy linear prediction and a diagnostic checklist. Removing off-policy sampling is not a universal guarantee for nonlinear control. |
| Keep and expand for reasoning | P47 / PDF41 | Name each triad component after students see the mechanism. Keep “can you break the triad?” as an actual calculation/discussion. All three create a risk; they do not force every run to diverge. |
| Compress to eight minutes | P48–51 / PDF42–45 | Reuse the idea of a representable subspace, with plain-language labels and a two-state picture if helpful. Drop the four-objective catalogue and formulas. In particular, do not carry over “MSBE = expectation of MSTDE”: squaring a conditional mean and averaging a squared sample are different. No projected-Bellman derivation. |
| Omit | P52–54 / PDF46–48 | Gradient TD and its variants are outside the accepted scope. Preserve the reason for seeking stable methods as the Week 6 handoff, without claiming DQN is gradient TD or has a general convergence guarantee. |
| Move the small bridge; omit the catalogue | P57, P60, P62–74 / PDF51–63; P58–59, P61, P63, P66, P75 hidden | Stored data, repeated fitting and minibatches can support 6.1's replay explanation; do not add a Week 5 batch-learning block. Least-squares prediction/control, LSTD/LSPI and their convergence tables have no accepted live placement and are omitted, not silently scheduled elsewhere. |
| Cut obsolete/duplicate material | P2, P12, P23, P28, P36, P42 and other hidden alternatives noted above | Old administration, recap and duplicate formulas do not consume teaching time. Hidden status is not evidence of current acceptance or assessment policy. |

Notation on reused slides follows the [shared guide](../../course/notation_guide.md): **x**(s) instead of f(s); **w** for value parameters; v̂/q̂ for approximations; v^π/q^π for true policy values; R_{t+1} for the observed reward; U_t and δ_t for target and error. Use **w**'s sole component w₁ in the one-dimensional example, rather than introducing ω. The Q bridge uses q̂ and its gradient, without adding a new state-action-feature symbol. Projection is labelled in words, without Π, D, a feature matrix or a new loss symbol. **No notation-guide change is needed for this proposal.**

## Proposed slide-level sequence

Units below are unpolished teaching suggestions, not exact slide copy, layouts or speaker notes. Minutes include the spoken reasoning and answers. Titles/IDs are provisional.

### 5.1 — Linear approximation and semi-gradients

| ID | Teaching purpose, source and check | Minutes |
| --- | --- | ---: |
| F01 | **The limit of a table.** Retrieve Week 4's Q entries and ask what an update tells us about an unvisited but similar state. P3–4. | 3 |
| F02 | **Generalization in Pacman.** Keep P5–7's concrete states and input/output choices. We need to share experience as well as save memory. Ask what should remain similar when one irrelevant detail changes. | 4 |
| F03 | **Features describe what the predictor can use.** P17–19. A feature is a measurable property; a vector collects them. Distinguish the available state information from the features chosen for prediction. Ask what a ghost-distance feature omits. | 4 |
| F04 | **Linear in the weights.** P20; book §9.4. Compute one weighted sum. Explain that the feature functions themselves may be nonlinear in raw measurements; “linear” describes dependence on **w**. | 4 |
| F05 | **Which states share an update?** P21; Silver PDF15. One-hot features recover a table. Shared/overlapping features generalize. Brief tile/coarse-coding illustration only, no construction algorithm. | 3 |
| F06 | **What would a good approximation mean?** P13; book §9.2, printed pp. 198–200 / PDF220–222. Begin with an oracle supplying true values, then average squared errors over states encountered under a fixed policy. Explain μ(s) as that on-policy weighting. Ask why fitting frequent states can sacrifice rare ones. | 4 |
| F07 | **Learning from a return instead of an oracle.** P10–14; book §9.3. Differentiate the squared error with a fixed target; use U_t = G_t for on-policy MC. The return is noisy, while the true value is unknown. | 4 |
| F08 | **Learning before the episode ends.** P15–16. Substitute the familiar TD target. Identify both appearances of **w** and explicitly hold the target fixed for this update. That omitted target dependence explains “semi-gradient.” | 4 |
| F09 | **The linear TD update.** P20. The prediction gradient is **x**(S_t), so the update is step size × TD error × features. Explain simultaneous component updates and zero continuation at a genuine terminal. | 3 |
| F10 | **Worked landmark update.** Old MT1 pp. 12–13. Students calculate features and the first update, inspect its effect on the next state's prediction, then work/check the second update. Protect calculation and feedback time; details below. | 9 |
| F11 | **Missing information or a difficult function?** P22 and Week 1 continuity. Diagnose two supplied states mapped to the same features but with different returns. Contrast omission of an available battery reading with an observation that never contained it. More training cannot recover an absent distinction from identical inputs. | 6 |
| F12 | **Approximate action values.** P7, P25–29. Replace the table entry by q̂; preserve SARSA's sampled successor action versus Q-learning's maximum. No second full derivation or control loop. Ask what becomes shared when parameters change. | 4 |
| F13 | **What convergence would and would not mean.** Correct P24 using book §9.4. A representable best fit need not be the true function; the on-policy linear TD limit need not be the least-value-error fit. Conditions concern sampling, features and step sizes. Preview the need to check learning dynamics. | 4 |
| F14 | **Boundary check.** Students explain target, error, feature vector and one effect on another state. End with “can accurate representation still learn unstably?” No divergence calculation yet. | 2 |
| | **Targets sum to** | **58** |

Core mathematical spine, to check the proposal's correctness rather than prescribe final equation slides:

- v̂(s, **w**) = **w**ᵀ**x**(s).
- With a held numeric target, differentiating ½[U_t − v̂(S_t, **w**)]² gives the update **w** ← **w** + α[U_t − v̂(S_t, **w**)]∇_**w**v̂(S_t, **w**).
- For TD, U_t = R_{t+1} + γv̂(S_{t+1}, **w**) and δ_t = U_t − v̂(S_t, **w**), all evaluated before changing **w**. Use U_t = R_{t+1} at a true terminal. Linear TD therefore updates **w** ← **w** + αδ_t**x**(S_t).
- Holding the target fixed for differentiation does **not** keep its numerical value fixed across subsequent updates. MC's fixed-policy return does not depend on the value weights; TD's bootstrapped target generally does. Semi-gradient is about ignored dependence, not simply about noisy or biased targets.

**F10 calculation candidate, directly adapted from old MT1 question 4.** Introduce this as a separate robot/landmark snapshot, not the accepted 2×2 grid. Features are the first coordinate, second coordinate, Manhattan distance to (3,3), and Manhattan distance to (4,2). At (2,1), (2,2), (2,3), the feature vectors are (2,1,3,3), (2,2,2,2), (2,3,1,3), respectively, written as columns. Observe the first two transitions with reward −0.1 each, γ = 0.5, α = 0.2, initially zero weights. Neither of these two transitions terminates; omit the old diagram's later +1 to avoid confusing it with the second observed reward.

- First update: U_t = −0.1, δ_t = −0.1, **w** = (−0.04, −0.02, −0.06, −0.06)ᵀ. The unupdated next state's prediction has nevertheless changed from 0 to −0.36 because the weights are shared.
- Second update, using those new weights consistently: current prediction −0.36; successor prediction −0.38; U_t = −0.29; δ_t = 0.07; **w** = (−0.012, 0.008, −0.032, −0.032)ᵀ.
- This is update arithmetic, not a claim that the feature set is sufficient or that two transitions establish convergence. Allocate about two minutes to features/setup, three to the first update, two to the second, and two to explanation/feedback.

**F11 diagnosis candidate.** Two fully observed nonterminal states have identical selected feature vectors but yield +1 and −1, respectively, before termination under the fixed policy. With equal frequency, a common prediction of zero is the best squared-error compromise and still wrong at both states. The issue persists even with exact return labels. If the distinguishing information exists in the input, revise the representation. If the observation itself omits relevant history/state information, a larger feedforward network with the same input cannot recreate it. Reuse the hidden-gauge question verbally; do not claim features must always be a complete Markov state merely to predict a particular policy's value accurately.

### 5.2 — Approximation instability

| ID | Teaching purpose, source and check | Minutes |
| --- | --- | ---: |
| I01 | **Representation and learning are different questions.** Retrieve the shared-weight update and the aliased-state diagnosis. Today the correct values will be exactly representable. P41. | 3 |
| I02 | **One update can increase its own target.** Adapt P43's features 1 and 2 with zero reward, γ = 0.9, α = 0.1, initial sole weight 10. Left prediction 10, right 20, target 18: the left-transition update takes the weight to 10.8 and raises the next target. Explicitly label this an MDP fragment, not yet a complete divergence demonstration. | 4 |
| I03 | **A complete two-state construction.** Specify both actions, both policies, the continuing task and the balanced update data below. The outgoing transition from the second state is included. Ask whose state frequencies determine the fit and whose action determines the target. | 6 |
| I04 | **Worked divergent updates.** Compute the two semi-gradient contributions from the same saved weight, average them, and update once. Obtain 10 → 10.2 → 10.404. Ask why the negative contribution does not cancel the positive one. | 9 |
| I05 | **The right answer is available.** Zero weights represent the exact zero values, yet the specified update grows away from them. Derive the multiplier 1 + 0.2α; making positive α smaller slows this recurrence without making it contract. This is a statement about this construction. | 4 |
| I06 | **The deadly triad.** P47; book §11.3. Identify shared approximation, bootstrapped targets and a state-update distribution different from the target policy's. Explain how the known behaviour/target distinction extends to which states get updated. Prediction already suffices; policy improvement is not needed. | 5 |
| I07 | **Change one component.** Keep the MDP, features, α and γ, but update from the target policy's stationary state distribution. Students compute the 0.96 multiplier and compare. Briefly contrast fixed zero-return targets. Explain the conditions and the limits of extrapolating this result. | 8 |
| I08 | **Representable value functions.** Simplify P49–50; book §11.4. A pair of state values is a point, and one shared weight restricts it to a line. “Projection” means the closest available fit under specified state weighting. Use words and geometry, no new operator notation. | 4 |
| I09 | **Fitting values versus fitting backups.** A fixed true-value point and a changing Bellman target are different fitting problems. Repeated backup and fitting need not inherit tabular contraction. Distinguish the picture from a claim that each stochastic TD step computes an exact projection. CS285 PDF32–36, book §11.4. | 4 |
| I10 | **Why nonlinear approximation is useful.** Old Deep QL PDF3–5; Abbeel PDF17, 25; book §9.7. Nonlinear models/learned features can represent relationships missed by a fixed linear feature model. They cannot distinguish identical inputs or guarantee stable bootstrapped learning. No architecture or backpropagation lesson. | 5 |
| I11 | **Diagnosis and the Week 6 handoff.** Compare insufficient features, adequate features with divergent updates, and richer models with moving targets. Ask what evidence would distinguish them. DQN retains these challenges; replay and target networks are next session's concrete mechanisms, not promised universal cures. | 4 |
| I12 | **Exit explanation.** Identify the triad in the example and explain why “use a smaller learning rate” or “use a bigger network” is not a complete diagnosis. | 2 |
| | **Targets sum to** | **58** |

**Complete divergence candidate (I03–I07).** This is a ChatGPT adaptation of the mechanism in old P43 and book §11.2, printed pp. 260–262 / PDF282–284, including the book's use of expected semi-gradient updates. It is **not Baird's counterexample or a verbatim book example**.

- Two states, called left and right. At either state, the action “go left” moves to left; “go right” moves to right. All rewards are zero. The task continues with γ = 0.9, so every true policy value is well-defined and zero.
- Target policy π always goes right. Behaviour b chooses either action with probability ½ at either state, giving stationary state frequencies ½ and ½. The target policy's stationary state frequency is entirely right.
- One parameter: **x**(left) = (1), **x**(right) = (2), hence the predictions are w₁ and 2w₁. Start with **w** = (10).
- Use a balanced pair of target-action transitions, one left → right and one right → right, both with reward zero. Such pairs can be supplied from behaviour data by retaining “go right” samples and balancing the originating states. Both target transitions have positive behaviour probability. This is an explicitly specified data/update construction, not an assertion that an uninterrupted behaviour trajectory supplies a balanced pair every two steps.
- At each iteration, calculate both contributions using the **same pre-update weights**, take their arithmetic mean, and apply α = 0.1 once. Equivalently, compute the exact expected semi-gradient update under equal state sampling and the deterministic target action. No importance ratio or general off-policy correction algorithm is required. This shows divergence of this deterministic mean-update procedure; it is not a claim that every random single-sample run follows the displayed numbers.

| Contribution at w₁ = 10 | Current value | Successor value | TD target | TD error | Error × current feature |
| --- | ---: | ---: | ---: | ---: | ---: |
| Left → right | 10 | 20 | 18 | 8 | 8 |
| Right → right | 20 | 20 | 18 | −2 | −4 |

The mean contribution is 2; the weight becomes 10 + 0.1(2) = 10.2. In general, the two contributions are 0.8w₁ and −0.4w₁, so each balanced update multiplies w₁ by **1 + 0.2α = 1.02**. Nonzero initial weights diverge in magnitude; zero is an exact but unstable solution. The fragment's threshold γ > 0.5 applies to repeating only its left transition. With both transitions included and equally weighted, the coefficient is (6γ − 5)/2, so the threshold is γ > 5/6. Do not mix these claims. The general threshold need not be taught live; it is a check on source adaptation.

For the protected one-component change, use the target policy's stationary distribution: only right → right contributes. The multiplier becomes **1 − 0.4α = 0.96**. It contracts to zero with the proposed α, and the left estimate follows through the shared parameter. This stationary comparison deliberately excludes an initial transient and is not a general coverage theorem. A second quick check can remove bootstrapping instead: all complete discounted returns are exactly zero, so fitting those fixed labels with equal state weighting gives multiplier **1 − 2.5α = 0.75**. Zero return is known here because every reward is zero; no infinite rollout must be collected. Keep that second contrast short, rather than deriving off-policy MC in general.

The example separates instability from insufficient expressiveness, target noise, a changing policy and neural-network complexity. It does not establish that the triad is the only cause of unstable optimization. On-policy nonlinear TD and badly chosen step sizes need their own qualifications; “break any side and everything converges” would be too strong.

**Projection scope.** Explain the nearest fit with a fixed set of state weights. For a genuinely unrepresentable pair of values, show its closest point on the representable line. Return to the distinction that the divergence example's zero point *is* on that line. MC fits return labels; TD uses estimates inside its targets and generally has a different limiting solution. Do not identify the mean semi-gradient update above with exact projected value iteration. Formal projection and alternative error objectives would displace the worked example and violate the accepted limit.

## Timing, workload and alternatives

| Check | Result and teaching judgement |
| --- | --- |
| Configured capacity | 70 × 0.85 = 59.5 usable minutes per session, no Week 5 administrative deduction. |
| Accepted allocations and proposed targets | 58 for 5.1 and 58 for 5.2; 116 total against 119 usable minutes. Each leaves 1.5 minutes inside usable capacity plus the configured 10.5-minute reserve, or 12 physical minutes. |
| Protected reasoning | 5.1: nine-minute parameter exercise and six-minute information diagnosis. 5.2: six-minute complete-example setup, nine-minute calculation, four-minute interpretation and eight-minute component variation. Geometry stays at eight. |
| Density risk | 5.1 introduces weights, features, an objective and a semi-gradient; 5.2 introduces the distinction between sampled states and target transitions. These are real conceptual costs. Exact arithmetic fit is not evidence of classroom fit. Confidence is medium pending cross-review/instructor judgement. |
| What funds the changes | The old feature/approximator menus, duplicate control derivations, Mountain Car setup, convergence tables, differential methods, gradient-TD and least-squares catalogue are compressed or omitted as mapped above. New reasoning stays within the accepted topic scope. |
| Prerequisites | Uses basic ML calculus/linear algebra and Weeks 1–4. No importance sampling, matrix projection, gradient-TD, neural-network implementation or completed A2. |
| Hidden workload | None added. No reading/video assignment, live training run, required appendix, extra homework or assessment change. |

Alternatives for the later choice, not additions to this sequence:

1. **Use Baird instead of the complete two-state construction.** Old P44 and book Figures 11.1–11.2 provide established provenance. Replace I03–I05's 19 minutes with its setup and one worked expected update; do not append seven-state analysis. It increases parameter bookkeeping and needs careful separation of the target transitions and sampled-state distribution. Recommend the smaller example unless cross-review finds a material problem.
2. **Use a two-feature arithmetic exercise instead of the four-feature old exam.** This can reduce arithmetic by about two minutes, but loses a useful direct connection to the old course's assessment. Use any saving for explaining shared updates/missing information, not additional feature families. Recommend retaining the old exercise initially.
3. **Two decks rather than one.** Splitting at F14/I01 changes packaging, not session content or minutes. Recommend a single topic deck with the explicit divider; no decision about later deck splits is implied.

If timing is tight in preparation, trim the feature-menu illustration or the second F10 calculation, while preserving at least one full update and F11's diagnosis. In 5.2, trim the second fixed-label contrast before the protected sampling-distribution comparison. Do not move unfinished reasoning into 6.1 or turn it into required reading. Any expansion toward 63 minutes needs its own reported delivery impact; this proposal does not spend that allowance.

## Open choices and stopping point

- Mutual cross-review should first challenge the complete two-state construction, its relation to off-policy sampling, and the clarity of the semi-gradient explanation. The numerical recurrences and old-exam updates were independently recomputed with exact rational arithmetic; they are not classroom-tested.
- After mutual review, the consequential instructor choices are the one-deck grouping and the worked-example choices, especially the completed two-state adaptation versus Baird. No new course-wide running example is assumed. No accepted decision is changed here.
- Evidence limits: external slides establish coverage, not exact teaching depth/time; local-source original retrieval provenance is incomplete; source PDFs contain some equations as images/annotations. Key old-slide corrections were checked against the PPTX text and rendered PDF pages. No source animations, linked demonstrations or student code were executed. No current-practice/SOTA claim is needed.
- **Next workflow step, when requested: one mutual cross-review in the shared review file.** Do not create the deck decision record as if these choices were accepted, produce render-ready content, or render a PPTX from this suggestion. This file is the only repository artifact authored in this step.
