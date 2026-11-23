# Week 7 (`reinforce` and `baseline`, sessions 7.1–7.2): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-11-21. Analysis only: nothing here is
accepted. It becomes historical after step 3. No deck decision file exists yet. The instructor's choices will go to
`decisions/lectures/<deck>.md`; E1 below proposes the deck name. I have not read any ChatGPT file for this deck.

**Scope of this file:**
- the teaching sequences for 7.1 `reinforce` and 7.2 `baseline`;
- the old-deck delta for `7 - Policy Space Methods.pptx` (68 slides, 7 hidden) and the Week 7-relevant slides of
  `9 - Deep PG.pptx` (44 slides). `7 - Policy Space Methods_old.pptx` is an earlier copy of the same deck with no
  extra content, so it is not compared separately;
- early choices for the instructor (E1–E13).

All numbers are checked by `scripts/check_policy_gradients_claude.py` (§ numbers below refer to its sections).

## Early choices for the instructor

Each has a recommendation; drafting continues with the recommendation unless the instructor says otherwise.

| # | Choice | Recommendation | Alternative |
| --- | --- | --- | --- |
| E1 | Deck split and name | One deck for 7.1 and 7.2, as in Weeks 2–6. Name: `policy_gradients`. 7.2 ends on the critic's motivation, and 8.1 builds the actor–critic, so the week boundary is also a content boundary. | One deck for 7.1–8.1 (brainstorming Q2's grouping); `policy_search`. |
| E2 | Running example | **The book's short corridor with switched actions (Example 13.1) in both sessions.** One parameter p = π(right) in every state. It gives: the stochastic-policy motivation (best p ≈ 0.59, J ≈ −11.6, against −44 and −82 for ε-greedy), the sampled REINFORCE update (7.1/7.2), the baseline's variance effect, the advantage table and the critic-bias demonstration. The book uses it for REINFORCE (Fig. 13.1) and the baseline (Fig. 13.2), so students can read along. | Silver's aliased gridworld (old 8–10) for the motivation and a separate small example for the estimator. Two examples to set up instead of one. |
| E3 | Old aliased gridworld (old 8–10) | **Cut**, replaced by the corridor (same lesson, with numbers). Rock-paper-scissors (old 7) stays as one line. | Keep one merged slide as the intuitive opener ("a deterministic policy is stuck forever"), +2 minutes in 7.1. |
| E4 | Order in 7.1 | **The accepted segment order**: a 4-minute "why learn a policy" opener, then the 10-minute history (black-box search over engineered policy parameters: CEM, finite differences, AIBO), then stochastic parameterization, then the derivation. The history ends on "these methods ignore which actions were taken when"; the stochastic, differentiable policy is what lets us look inside. | The old deck's order: parameterization and objective first (old 11–16), CEM and finite differences after. |
| E5 | Derivation route (accepted: score-function and reward-to-go derivation, 40 min) | **One step first, then whole episodes.** (1) One-state, two-action case: log-derivative trick, students check the estimator's mean against the exact gradient. (2) Episode probability: the dynamics factors drop out of ∇ln. (3) Causality: rewards before t do not depend on A_t, giving reward-to-go G_t. (4) The policy gradient theorem stated as the general form of the same result, without proof. Same route as CS285 L5, CS224R L3 and Abbeel L3; old 40's "trajectory version (on the board)" becomes slides. | The book's route: prove the policy gradient theorem (box p. 325), then derive REINFORCE from it (pp. 326–327). About 10 more minutes; the proof uses unrolling notation students have not seen. |
| E6 | Discounting in the estimator | Derive with γ = 1 (the corridor and the book's text use γ = 1). Show the discounted estimator in the book's exact form, γ^t G_t ∇ln π. Notes: most implementations drop γ^t; that version weights late steps more and is not the exact gradient of J. **A3 needs the same convention**: its tests catch "discount" errors (`decisions/assignment_decisions.md` A3 starter). | Teach the common form G_t ∇ln π (no γ^t) and put the exact form in the notes. |
| E7 | Estimator form | **Per-episode sum with θ fixed during the episode**: ĝ = Σ_t G_t ∇ln π(A_t ∣ S_t, **θ**), then one step. This is what deep-RL code and A3 do. The book's box (θ updated inside the step loop) is shown once and its difference stated in the notes. | The book's per-step form as the main algorithm. |
| E8 | History segment content (accepted scope: "no mathematics or algorithms") | CEM, finite differences and the AIBO example **in words and pictures**. The finite-difference formula (old 24–25) moves to the notes. | Keep old 24's formula on the slide. That is a scope change to `policy_history` and needs an explicit decision. |
| E9 | Critic-bias demonstration (accepted 7.2 segment: motivate a learned critic and its bias) | **The corridor with a critic that sees the same aliased features**, v̂(s) = c for all s (the book's own baseline in Fig. 13.2 is this single weight). As a baseline it is harmless. Used inside a one-step TD error, it credits only the last action of each episode, and the expected update pushes p up at every p, past the optimum 0.59 (§7). | Old 59's qualitative statement only (2 minutes, no numbers). |
| E10 | Old slides outside the accepted scope: compatible function approximation (old 60–63), critics and actors at different time scales and trace-based versions (old 54–58) | **Cut.** Optional: a hidden appendix with one pointer each (Sutton et al. 2000 for compatible approximation; book §13.6 for traces), as in `deep_q_learning` D7. Not taught, no minutes. | Cut with no appendix. |
| E11 | Old slides that belong to Week 8 | Move: Q actor-critic and A2C (old 49–52) to 8.1; off-policy gradient (Deep PG 11–12) and step sizes (Deep PG 13–15) to 8.2. | — |
| E12 | Notation not in the guide | Needs approval before rendering (details under "Notation"): h(s, a, **θ**), ln, ĝ, the episode's probability without τ, μ(s, **θ**) and σ(s, **θ**) for the Gaussian, α_**θ** and α_**w**, A^π(s, a), ℛ(a) in the one-step case. | Use τ for an episode as CS285 does; τ is already the Polyak rate (O5). |
| E13 | Delivery allowance | 7.1 slide targets sum to 61.5 (allocation 59): fine for delivery under the 63-minute allowance, planning estimate unchanged. The extra time is the opener's motivation (P01–P02). 7.2 sums to 54.5 (allocation 54) plus 5 administrative minutes. | Drop P02 to 1.5 minutes and S01 to 2: 7.1 = 59. |

## Accepted frame

From `decisions/topic_decisions.yaml` and `output/lectures/session_sources.md` §7.1–7.2.

**7.1 `reinforce` (Policy-search history and REINFORCE).** 59 teaching minutes (range 55–68). Requires 3.2
`returns` and 5.1 `linear`.
- Worked activity: historical overview, then the parameterized policy and the score-function/reward-to-go
  derivation; the sampled example is finished in the next session.
- Feasibility note: the ten-minute history is retained; moving the sample calculation avoids reducing baseline/critic
  depth.
- Segments: history 10 (`policy_history_live_minutes`); stochastic parameterization and continuous actions 9;
  score-function and reward-to-go derivation 40.
- Groups:
  - `policy_history` (exposure; recognize): ten-minute overview of gradient-free search and finite differences, no
    mathematics or algorithms. Topics: `policy_search`, `cross_entropy_method`, `finite_difference_policy_gradient`.
  - `policy_estimators` (core; derive / implement / analyze): derive score-function REINFORCE and the baseline
    identity (and, in 8.1, the actor-critic target and GAE). Implement REINFORCE with a baseline or a simple
    actor-critic.
  - `formulation` (core): stochastic policy parameterization revisited.

**7.2 `baseline` (Sampled gradients, baselines and critic motivation).** 54 teaching minutes (range 50–65) plus 5
administrative minutes. Requires 7.1.
- Worked activity: finish the gradient example, baseline identity and variance reasoning; advantage and critic
  motivation.
- Feasibility note: the 5 administrative minutes stay separate; brief psychology comments replace narration inside
  examples.
- Segments: finish the sampled example 8; baseline identity and variance/evaluation example 22; advantage
  interpretation 12; motivate a learned critic and its bias 12.
- Groups: `policy_estimators`; `evaluation` (core; analyze); `psychology_connections` (exposure; recognize). 7.2 is
  the only remaining placement of the psychology connection (`mc_td` D3 removed the 3.1 one).

**Constraints from other decisions.**
- **No importance sampling** before 8.2 (`model_free_control` D6). Old Deep PG 11–12 (off-policy gradient) moves to
  8.2.
- **No backward-view mathematics** (`backward_trace_math: false`); the existence mention is in 8.1.
- **Average reward** has its 5 minutes in 3.1. The continuing-task objective appears in one notes line only.
- **No hedging on slides** (2026-11-12): conditions and "this is not…" statements are in the notes column below,
  marked "Notes:".
- **Readings:** none assigned in current planning. Book Chapter 13 pointers stay optional.
- **Week 6 handoff:** 6.2 ended (D13) with continuous actions as one motivation and recorded that Week 7 must state the
  others: stochastic policies (aliasing, games), a policy simpler than its value function, smooth changes of the policy
  (`analysis/phase7_brainstorming.md`, 2026-11-18). P02 does this.

**Assessment link.**
- **A3** (release Week 8, due late Week 11; prerequisites `baseline`, `actor_gae`, `ratios`):

  | A3 element | Prepared by |
  | --- | --- |
  | REINFORCE with reward-to-go | D05–D06, D08; the sampled update B02 |
  | Action-independent learned baseline | B05, B08, B12 |
  | "Accidental baseline gradient" test | B12 (the baseline has its own loss; its value enters the policy update as a constant) |
  | Sign and discount tests | D01 (ascent), D06 (γ^t, E6), D08 notes (loss = −Σ G_t ln π in code) |
  | Terminal handling | D05, B02 (G_t ends at T; no value after the terminal state) |
  | Baseline/no-baseline comparison at a fixed interaction budget, multi-seed | B09 |

- **Midterm 2** (A3 `exam_bridge`: modify a return/baseline/ratio in a small example and predict the consequence;
  A3 notes: score-function/baseline derivation stays in the midterm path). The old Spring 2025 MT2 Q1 asked for the
  score of a Poisson policy and one actor/critic update. D04's "derive a score for a given distribution" and B05/B07
  prepare those question types.

The lecture uses the book's corridor, so it does not hand out A3's environment or its result.

## What students already have

- **Weeks 1–2:** stochastic policies π(a ∣ s); v^π, q^π; Bellman expectation equations; the 2×2 grid.
- **Week 3:** returns G_t (U = r at termination), Monte Carlo prediction, bias and variance of targets, n-step
  targets; average reward (5 minutes).
- **Week 4:** on- and off-policy learning; ε-greedy; Q-learning; the one-step target needs no correction.
- **Week 5:** features **x**(s), **x**(s, a); semi-gradient updates; aliased cells (F12-A: two states with identical
  features) and the question "is the representation sufficient?" (F13-A).
- **Week 6:** DQN; replay requires an off-policy method; one output per discrete action; D13: "with continuous actions
  there is no list to take the max over". Advantage was not taught (dueling networks were cut, D7/D17 extensions slide
  names them only).
- **Entry background:** basic machine learning (gradients, maximum likelihood, softmax classifiers). D02's
  log-derivative trick is new as a tool; the softmax itself is not.

## Is the old material substantial?

**Yes.** `7 - Policy Space Methods.pptx` covers both sessions: motivation (3–10), parameterization and objective
(11–16), CEM and finite differences (17–28), the likelihood-ratio derivation and REINFORCE (31–41), baselines and the
advantage (44–46), the critic and its bias (48, 59). Its derivation stops at the one-step case and states the policy
gradient theorem; the trajectory version was "on the board" (old 40), so D05–D06 are new slides. The old deck has no
worked calculation; all "Your turn" slides are new. I did not need to ask.

## Central idea and the motivation thread

**7.1: change the policy so that good episodes become more likely.** We cannot differentiate the environment, but we
can differentiate the probability that our own policy chose what it chose. The score ∇ln π(A_t ∣ S_t, **θ**) points
toward making the chosen action more likely. REINFORCE moves along it, weighted by what followed (G_t). Three steps
make this precise: one decision (D02–D03), one episode with the dynamics dropping out (D05), and causality (D06).

**7.2: the same estimate, less noise, and what it costs to reduce it further.**
1. One episode can point the wrong way (B02: p goes from 0.5 to 0.25 although the best p is 0.59).
2. Subtracting a baseline that does not depend on the action leaves the mean unchanged and can cut the noise (B05–B07).
3. With b = v^π the weight becomes the advantage: better or worse than this policy's usual (B10–B11).
4. Learning v̂ and bootstrapping with it lowers variance further, but a wrong critic biases the direction (B14–B16).
   That is 8.1's starting point.

**Explicit motivation time** (memory "motivation first").
- **7.1:** about 16 of 61.5 minutes: P01–P02 (why a policy), H05 (why look inside), S01 (why stochastic, in numbers),
  D01 (why the gradient is hard), D03's surprise (a positive reward that pushes toward the worse action).
- **7.2:** about 12 of 54.5: B03 (why every action went down), B04 (how noisy), B08 (why not an action-dependent
  baseline), B14 (why bootstrap), B16 (what goes wrong).

## Teaching sequence for 7.1 `reinforce` (slide level, unpolished)

Slide IDs are proposals. Minutes are planning targets. "Old N" means `7 - Policy Space Methods.pptx` slide N in PPTX
numbering (the PDF omits hidden slides 2, 26, 32, 42, 64–66). "DPG N" is `9 - Deep PG.pptx`.

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| P00 | Title | Title Slide layout: course name; **Policy Gradients** / instructor / Fall 2026. | deck title format; old 1 | 0.5 |
| P01 | From choosing actions to learning a policy | Week 6's D13 in one line (continuous actions: no list to take a max over). Old 3's value-based recap compressed to one line: so far the policy was implicit, read off q̂ by greedy or ε-greedy selection. Today: write the policy down with parameters **θ** and improve **θ** directly. Old 5's value/policy/actor-critic picture. | old 3 (compressed), 4, 5; Week 6 D13 | 1.5 |
| P02 | Why learn a policy directly? | Four reasons (Week 6 D17 commitment): (1) continuous or large action sets; (2) the best policy can be stochastic: aliased states (Week 5 F12-A), games such as rock-paper-scissors (old 7); (3) the policy can be simpler than its value function (Tetris; book p. 324); (4) small parameter changes give small policy changes, where an argmax can flip (book p. 324). Plus prior knowledge in the policy's form (book p. 324: "often the most important reason"). Costs, from old 6: local optima, noisy evaluation. Notes: (4) is the reason stronger convergence results exist for policy-gradient methods (book p. 324), under step-size conditions; old 6's "better convergence properties" without that condition is not used. | old 6 (fixed), 7; book §13.1–13.2 printed 322–324 / PDF 344–346; Silver L7 pp. 3–11; Week 6 D13, D17 | 2.5 |
| H01 | Policy search: treat J as a black box | Segment 1 (**history, 10 minutes**). A policy with a few engineered parameters (AIBO's gait has 12). Run it, measure the return, change the parameters, keep what works. Old 30's black-box vs white-box picture. No formula. | old 11, 17, 23, 30; CS234 L5 pp. 24–45 | 2 |
| H02 | Cross-entropy method | Old 17–20 merged, in words: sample parameter vectors from a distribution, run each, keep the best fraction, refit the distribution to them, repeat. Abbeel–Schulman tutorial pictures (old 18–19). Old 20's "simple; short episodes, small parameter spaces". Notes: Tetris results with CEM (Szita and Lőrincz 2006; not in local sources, verify before naming numbers). | old 17–20; Abbeel–Schulman NeurIPS 2016 tutorial (as cited on old 18) | 3 |
| H03 | Finite differences | Old 24–25 in words (E8): nudge one parameter, rerun, compare the returns; one extra set of runs per parameter. Noisy and slow; old 25's fix: reuse the same random seed for both runs (why: the difference then reflects the parameter, not the luck). Notes: the formula ∂J/∂θ_k ≈ [J(**θ** + ε**u**_k) − J(**θ**)]/ε, d + 1 evaluations; works for non-differentiable policies (old 25). | old 24–25 (formula to notes); Silver L7 pp. 13–15 | 2 |
| H04 | Learning to walk: AIBO | Old 27–28: Kohl and Stone (ICRA 2004), finite-difference policy gradient on real robots, field traversal time as the return, 12 parameters, video. | old 27–28 | 2 |
| H05 | Why look inside? | One slide: black-box methods use one number per run. They ignore which actions were taken, in which states, and when the rewards came. Question: what would we need in order to use that information? Answer: a policy whose action probabilities we can differentiate. Notes: evolution strategies remain in use at scale (Salimans et al. 2017, arXiv 1703.03864; not local, verify); no claim about which family is better. | old 22, 31; CS285 L5 pp. 3–12 | 1 |
| S01 | Why stochastic: the short corridor | Segment 2 (**parameterization and continuous actions, 9 minutes**). Book Example 13.1: three states and a goal, −1 per step, state 2 swaps left and right, all states look the same to the agent, so one probability p of "right" in every state. Show J(p) (book figure). ε-greedy (ε = 0.1) can only pick p = 0.95 (J = −44.2) or 0.05 (J = −82.1); the best is p ≈ 0.59 with J ≈ −11.66 (§1). Ask first: why can't "always right" work? (State 2 sends it back to state 1 forever.) Notes: exact optimum 2 − √2 (book Exercise 13.1); J(p) = 2(p − 2)/[p(1 − p)] (§1). | book Example 13.1 printed 323 / PDF 345; §1 | 3 |
| S02 | Softmax in action preferences | π(a ∣ s, **θ**) = e^{h(s,a,**θ**)} / Σ_b e^{h(s,b,**θ**)}, h linear: h = **θ**^⊤**x**(s, a), or a network's outputs (old 14, DPG 8). The corridor in this form: **x**(s, right) = (1, 0), **x**(s, left) = (0, 1), so p = 1/(1 + e^{−(θ_R − θ_L)}). Preferences are not values: they can grow without bound, so the policy can approach a deterministic one, which ε-greedy cannot (book pp. 322–323). | old 12–14 (fixed); DPG 8; book eqs. 13.2–13.3, printed 322–323 | 3 |
| S03 | Continuous actions: a Gaussian policy | π(a ∣ s, **θ**) = normal density with mean μ(s, **θ**) and standard deviation σ(s, **θ**); μ linear or a network, σ = exp(·) to keep it positive (old 15; book §13.7). Check (old 41, the inverted pendulum): the action is a torque; what are μ and σ functions of, and what does a large σ do? (Explore more.) Notes: one-dimensional action only; DPG 8's multivariate case and its "do not learn Σ" remark are Week 8–9 material. | old 15, 41; DPG 8; book §13.7 printed 335–337 / PDF 357–359; CS285 L5 pp. 3–12 | 3 |
| D01 | The objective and why its gradient is hard | Segment 3 (**derivation, 40 minutes**). J(**θ**) = v^{π_**θ**}(s_0) = 𝔼[G_0] (old 16, episodic start value); ascent: **θ** ← **θ** + α ĝ, ĝ an estimate of ∇J(**θ**) (old 21; fix "negative direction"). Old 22's question: why is this harder than Week 5's gradient? Answer: **θ** changes the actions and therefore which states are visited, and the environment's response is unknown (book p. 324–326). Notes: continuing tasks use average reward (3.1); old 16's other objectives are not taught. | old 4, 16, 21–22 (fixed); book §13.2 printed 324–326 | 3 |
| D02 | One decision: the log-derivative trick | One state, two actions, expected reward ℛ(a): J = Σ_a π(a ∣ **θ**) ℛ(a). ∇J = Σ_a ∇π(a ∣ **θ**) ℛ(a) = Σ_a π(a ∣ **θ**) ∇ln π(a ∣ **θ**) ℛ(a) = 𝔼[∇ln π(A ∣ **θ**) R], using ∇ln x = ∇x / x. A sum we cannot evaluate becomes an average we can sample. Name: ∇ln π is the **score** (the book calls it the eligibility vector). Fix old 33: in this one-step problem the state distribution does not depend on **θ** at all; old 33's "hidden assumption" line is replaced. | old 33–34 (fixed); CS285 L5 pp. 3–12; CS224R L3 pp. 8–9; book p. 327–328 | 4 |
| D03 | **Your turn: check the trick by hand** | **Protected (D03–D04 calculations): 9 minutes with D04.** Two actions, ℛ(R) = 2, ℛ(L) = 1, **θ** = (0, 0), so p = 0.5. (a) Scores: R → (0.5, −0.5), L → (−0.5, 0.5). (b) Single-sample estimates: R → (1, −1), L → (−0.5, 0.5). (c) Their average: (0.25, −0.25) = the exact gradient (§2). (d) Puzzle: sampling L, with a positive reward, pushes toward L. Why is the update still right on average? (The push toward R is larger and equally often.) This puzzle returns in 7.2 (B06). | constructed (§2) | 5 |
| D04 | Scores of common policies | Softmax, linear preferences: ∇ln π(a ∣ s, **θ**) = **x**(s, a) − Σ_b π(b ∣ s, **θ**)**x**(s, b) (old 36; book eq. 13.9): the chosen action's features minus their average. Two-action corridor case: (1 − p, −(1 − p)) for right, (−p, p) for left. Gaussian (old 37): (a − μ(s, **θ**)) **x**(s) / σ² for the mean parameters: push the mean toward actions that did well. Exam-style check: given a new distribution, derive its score (Spring 2025 MT2 used a Poisson policy). | old 36–37; book eq. 13.9 and §13.7; `exams/spring25/mt2` Q1(a) | 4 |
| D05 | From one decision to an episode | Pr{episode ∣ **θ**} = Pr{S_0} Π_t π(A_t ∣ S_t, **θ**) ℳ(S_t, A_t, R_{t+1}, S_{t+1}). The logarithm turns the product into a sum; the start and ℳ terms do not contain **θ** and drop out of the gradient. Result: ∇J = 𝔼[G_0 Σ_t ∇ln π(A_t ∣ S_t, **θ**)] (γ = 1). No model needed (old 34: "model-free"). Old 40's board derivation, now on slides. Notes: requires the episode to end (finite T); with stochastic rewards ℳ carries them, still free of **θ**. | old 34, 40; CS285 L5 pp. 3–12; CS224R L3 pp. 9–10; Abbeel L3 pp. 5–24; Silver L7 pp. 16–22 | 6 |
| D06 | Reward-to-go | Each score term multiplies every reward of the episode, including rewards that came before the action. Causality: an action cannot change earlier rewards, and the score has mean zero given the state (D03: Σ_a π ∇ln π = ∇Σ_a π = 0), so those products average to zero. Drop them: ∇J = 𝔼[Σ_t G_t ∇ln π(A_t ∣ S_t, **θ**)]. Fewer terms, same mean, less noise. Discounted case, exact (E6): Σ_t γ^t G_t ∇ln π. Check: in D03, why was R itself the right weight? (One step: G_0 = R.) Notes: the common implementation drops γ^t (E6); CS224R's humanoid example (L3 p. 14) is the intuition for causality. | CS285 L5 pp. 14–23; CS224R L3 pp. 13–14; Abbeel L3 pp. 5–24; book box p. 328 (γ^t) | 6 |
| D07 | The policy gradient theorem | The same result written per state: ∇J(**θ**) ∝ 𝔼_π[q^π(S_t, A_t) ∇ln π(A_t ∣ S_t, **θ**)], and G_t is a sample of q^π(S_t, A_t) (old 35, 38; book eqs. 13.5–13.8). The change in the state distribution never has to be differentiated. Reading the update (book p. 327): proportional to the return; divided by the action's probability, so frequent actions do not win just by being frequent. Notes: in the episodic case ∝ hides the mean episode length (book p. 326), absorbed into α; the Σ_s μ(s) form and the proof (book p. 325) stay in the notes; old 35's "for any of the three objectives" is replaced by this statement. | old 35, 38 (fixed); book §13.2–13.3 printed 324–327 / PDF 346–349; Sutton 24-PG pp. 2–15 | 3 |
| D08 | REINFORCE | Algorithm (E7): run one episode with π(· ∣ ·, **θ**); compute G_t backward; ĝ = Σ_t G_t ∇ln π(A_t ∣ S_t, **θ**); **θ** ← **θ** + αĝ; discard the episode and repeat. Variants (old 39): average over several episodes per update. On-policy: the expectation is under the current π_**θ**, so old episodes cannot be reused without a correction (Week 8). Book box (p. 328) shown small, with its per-step update. Notes: in code the "loss" is −Σ_t G_t ln π(A_t ∣ S_t, **θ**) with G_t treated as a constant (sign check for A3); Williams (1992). | old 38–39 (fixed); DPG 9–10; book box p. 328 / PDF 350; CS285 L5 pp. 3–12 | 4 |
| D09 | Set up the sample for next time | The corridor at **θ** = (0, 0), p = 0.5, α = 0.1, and one episode: 1 →R 2 →R 1 →R 2 →L 3 →R G (five steps, probability 1/32 at p = 0.5). Students fill the G_t column now: −5, −4, −3, −2, −1. The rest is 7.2's B02. | constructed (§3) | 2 |
| D10 | Summary and exit question | REINFORCE in one line. Exit question: every return in this episode is negative. Does the update lower the probability of every action taken? | old 53 (first line) | 1 |

**Targets sum to 61.5 minutes** (E13): opener 4.5 (P00–P02), history 10 (H01–H05), parameterization 9
(S01–S03), derivation 38 (D01–D10). Protected: D03–D04 calculations (9 minutes).

## Teaching sequence for 7.2 `baseline` (slide level, unpolished)

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| B00 | Session divider | "Baselines, advantages and the critic" (same deck). | — | 0.5 |
| — | Administration | 5 minutes, instructor's content (project design checkpoint is due late Week 7, `decisions/project_decisions.md`). Outside the teaching targets. | — | (5) |
| B01 | Where we stopped | The estimator ĝ = Σ_t G_t ∇ln π and D09's table with the returns filled in. Segment 1 (**finish the sample, 8 minutes**). | D08–D09 | 1 |
| B02 | **Your turn: finish the update** | Score column: right (0.5, −0.5), left (−0.5, 0.5). Products: (−2.5, 2.5), (−2, 2), (−1.5, 1.5), (1, −1), (−0.5, 0.5). Sum (−5.5, 5.5); α × sum = (−0.55, 0.55); new p = 0.25; J goes from −12.0 to −18.7 (§3). The exact gradient at p = 0.5 is 2 × (1, −1), toward more right (§1). This episode moved p the wrong way. | constructed (§3) | 6 |
| B03 | Why every action went down | All returns are negative, so every sampled action was pushed down; earlier actions most, because their returns are the most negative. Only the differences between the pushes carry information. Thorndike's law of effect in one line: actions followed by satisfaction are strengthened; REINFORCE does this with a number attached (book §14.3). | book §14.3 printed 357–358 / PDF 379–380 | 1 |
| B04 | How noisy is one episode? | Segment 2 (**baseline identity and variance/evaluation, 22 minutes**). 100,000 episodes at p = 0.5: the θ_R part of ĝ has mean 2 and standard deviation about 27; about half (0.49) of the episodes point the wrong way (§5). Histogram. Old 39's "high variance"; DPG 13's "noisy". | §5; old 39; DPG 13; CS224R L3 p. 15 | 3 |
| B05 | The baseline identity | For any b(s) that does not depend on the action: 𝔼[b(S_t) ∇ln π(A_t ∣ S_t, **θ**)] = Σ_a π ∇ln π · b = b ∇Σ_a π = b ∇1 = 0 (old 44; book eq. 13.10). So ĝ = Σ_t (G_t − b(S_t)) ∇ln π has the same mean. The same zero-mean fact gave reward-to-go (D06). | old 44 (fixed); book §13.4 printed 329 / PDF 351; CS285 L5 pp. 14–23; CS234 L6 pp. 9–12 | 4 |
| B06 | **Your turn: D03 with a baseline** | The one-step example again. b = 1: estimates (0.5, −0.5) and (0, 0); mean (0.25, −0.25); variance of the θ_R part 0.5625 → 0.0625. b = 1.5: both samples give (0.25, −0.25), variance 0 (§2). D03's puzzle resolved: with b = 1.5, sampling L now pushes toward R. | constructed (§2) | 4 |
| B07 | The corridor with a baseline | Same episode as B02: with the constant b = −3, the sum is (−1, 1); with b = v^π(S_t) (v = −12, −10, −6), it is (9.5, −9.5), now toward more right (§3). Over 100,000 episodes: standard deviation 27 → 16.3 (b = −12 = J) or 16.8 (b = v^π(s)); wrong-way share 0.49 → 0.39 or 0.43 (§5). Psychology, one line: learning driven by the difference between what happened and what was expected is the Rescorla–Wagner idea, and dopamine responses look like such a difference (book §14.2.2, §15.3). Notes: v^π(s) is the natural baseline, not the variance-minimizing one; here a constant does about as well because one parameter collects every state's terms; the simulated means (about 1.91–1.94 for 100,000 episodes) differ from 2 by sampling error. | §§3, 5; book §14.2.2 printed 346 / PDF 368, §15.3 printed 381–383 / PDF 403–405 | 5 |
| B08 | Why not a baseline that depends on the action? | Check: what if b(s, a) = q^π(s, a)? Every weight becomes G_t − q^π(S_t, A_t), whose mean given S_t and A_t is 0: the update averages to zero. The identity needs Σ_a ∇π(a ∣ s) b to factor, which only works when b ignores a. | book p. 329; CS234 L6 pp. 9–12 | 2 |
| B09 | Would you believe "a baseline learns faster"? | Book Fig. 13.2 (REINFORCE with and without a baseline on this corridor, 100 runs). Questions from the accepted `evaluation` scope: same number of episodes for both? Each method's step size tuned separately (2^−13 against 2^−9), and is that fair? How much do runs vary? What is on the vertical axis? A3 runs this kind of comparison at a fixed interaction budget with several seeds. | book Fig. 13.2 printed 330 / PDF 352; Week 6 D10 (protocol); A3 task 2 | 4 |
| B10 | The advantage | Segment 3 (**advantage interpretation, 12 minutes**). With b = v^π: 𝔼[G_t − v^π(S_t) ∣ S_t = s, A_t = a] = q^π(s, a) − v^π(s) = A^π(s, a) (old 45). Meaning: how much better a is than what π does on average in s. Sign gives direction; Σ_a π(a ∣ s) A^π(s, a) = 0. ∇J ∝ 𝔼[A^π(S_t, A_t) ∇ln π]. | old 45 (fixed); CS285 L6 pp. 4–18; Abbeel L3 pp. 26–32; DPG 6 | 3 |
| B11 | **Your turn: advantages in the corridor** | At p = 0.5, given v = (−12, −10, −6): fill q^π(s, a) = −1 + v(next) and A^π (§6). State 1: A(R) = +1, A(L) = −1. State 2: A(R) = −3, A(L) = +3. State 3: A(R) = +5, A(L) = −5. Visits per episode (6, 4, 2) (§4). Question: the parameter is shared. Which states ask for more right, which for less, and who wins? (States 1 and 3 against state 2; net gradient 2 × (1, −1).) | constructed (§§4, 6); Week 5 F12a-A (shared weights) | 5 |
| B12 | REINFORCE with a learned baseline | Book box (p. 330; old 46): learn v̂(s, **w**) from the returns (Monte Carlo, Week 5's gradient MC), and update **θ** with (G_t − v̂(S_t, **w**)). Two step sizes α_**θ**, α_**w** (E12). Implementation point (A3's "accidental baseline gradient"): v̂ enters the policy update as a number; the baseline is trained only by its own squared error. In the corridor v̂ is a single weight, as in the book's Fig. 13.2. | old 46; book box p. 330 / PDF 352; CS285 L6 pp. 4–18; A3 starter | 3 |
| B13 | Check | True or false: (1) a bad baseline can bias REINFORCE (false: it costs variance only); (2) the advantages in a state average to zero under π (true). | B05, B10 | 1 |
| B14 | From baseline to critic | Segment 4 (**critic motivation and bias, 12 minutes**). Old 48: bootstrapping had lower variance and works online. Replace G_t by R_{t+1} + γ v̂(S_{t+1}, **w**): the weight is the TD error δ_t (book eqs. 13.12–13.14). With v̂ = v^π, 𝔼[δ_t ∣ S_t, A_t] = A^π(S_t, A_t) (old 47's derivation): the right direction on average. The learner that judges actions is the **critic**; the policy is the **actor**. Psychology, one line: the neural actor–critic hypothesis (dorsal striatum as actor, ventral striatum as critic, dopamine as the TD error; book §15.7). | old 47–48 (fixed); book §13.5 printed 331 / PDF 353, §15.7 printed 395 / PDF 417; CS224R L4 pp. 6–12 | 4 |
| B15 | **Your turn: a critic that cannot tell states apart** | The critic uses the same aliased features: v̂(s) = c in every state (fit to the returns, c ≈ −10.3 at p = 0.5). TD errors on B02's episode: −1, −1, −1, −1, then +9.33 on entering G (§7). Which action gets credit? (Only the last one, always "right".) | constructed (§7) | 3 |
| B16 | Reveal: the critic changes the direction | Expected actor update with this critic is positive at every p: at p = 0.7 it is +3.27 while the true gradient is −2.95, so it pushes past the best p (0.59) toward p → 1, where J → −∞ (§7). With the true v^π as critic, the expected update equals the true gradient (§7). A wrong baseline costs variance; a wrong critic costs direction. Week 3's trade-off, now for policies (old 59). Notes: the book (p. 331) says this bias does not come from bootstrapping as such: the actor would be biased even with a Monte Carlo-trained critic; a one-weight critic fitted by TD(0) gives c = −E[T] (−12 at p = 0.5), also negative, so the same push. A critic that can tell states apart reduces the bias as it learns; 8.1 builds that actor–critic. | §7; old 59 (with numbers); book p. 331 | 4 |
| B17 | Summary and next | Three weights for the score: G_t (unbiased, noisy); G_t − b(S_t) (unbiased, less noisy); δ_t with a learned v̂ (lower variance, biased if v̂ is wrong). Next (8.1): actor–critic, n-step and λ mixtures, GAE. | old 53 | 1 |

**Targets sum to 54.5 minutes** (+5 administrative): sample 8 (B01–B03), baseline and evaluation 22 (B04–B09),
advantage 12 (B10–B13), critic 12 (B14–B17), divider 0.5. Protected: B02 (6), B06 (4), B11 (5), B15 (3).

## Old-deck delta

### `7 - Policy Space Methods.pptx` (PPTX numbering; H = hidden)

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 1 | **Fix** | P00: new title format, title "Policy Gradients". |
| 2 (H) | **Cut** | Planning note (Schulman–Peters tutorial). |
| 3 | **Compress** | P01: one line. Its list (DP, MC, Sarsa, Q-learning, the deadly triad) was Weeks 2–5. |
| 4–5 | **Keep, merge** | P01 (picture), D01 (ascent). θ_t in "ℙ[A_t = a ∣ S_t = s, θ_t = θ]" → π(a ∣ s, **θ**). |
| 6 | **Keep, fix** | P02. "Better convergence properties" gets the book's reason and its condition (notes). "Can benefit from demonstrations" → notes (Week 12's behaviour cloning). |
| 7 | **Compress** | P02, one line (rock-paper-scissors). |
| 8–10 | **Cut** (E3) | Replaced by S01. Old 8's feature f(s, a) is the same aliasing idea as Week 5's F12-A. |
| 11 | **Merge** | H01, D01: "what is a good J, what is a good parameterization". "Non-gradient methods (will not cover)" is replaced by the accepted history segment. |
| 12–13 | **Keep picture** | S02–S03: "any differentiable function approximator". |
| 14 | **Keep, fix** | S02: f → **x**; "discreet" → discrete; preferences ≠ values (book). |
| 15 | **Keep, fix** | S03: μ, σ with **θ** subscripts as the book does (E12); exp keeps σ positive. |
| 16 | **Compress, fix** | D01: episodic start value only. "𝔼_{π_θ}[V_0]" → 𝔼[G_0]. J_av and J_ar → one notes line (3.1 covered average reward). |
| 17–20 | **Keep, merge** | H02, words only. Old 17's J formula (Σ R(s_t)) → notes. |
| 21 | **Keep, fix** | D01: "update θ in the negative direction of this gradient to find the maximum" → ascent; δ → ∂. |
| 22 | **Keep** | D01's question. Its "gradients are identical up to a constant" → D07's ∝. |
| 23, 30 | **Keep one picture** | H01: black-box versus white-box. |
| 24–25 | **Keep, words only** | H03 (E8). "Fix random seed (why?)" kept as the question. |
| 26 (H) | **Cut** | Duplicate of 25. |
| 27–28 | **Keep** | H04. |
| 29 | **Cut** | Recap; D01 replaces it. |
| 31 | **Merge** | H05, D02. |
| 32 (H) | **Cut** | Planning note. |
| 33 | **Keep, fix** | D02: π_θ(s, a) → π(a ∣ s, **θ**); the "hidden assumption: state distribution depends weakly on θ" line is wrong for the one-step case (μ(s) is the start distribution) and is removed; "log" → ln (E12). |
| 34 | **Keep, fix** | D02 (name), D05 ("model-free"). "Caveat: single step" answered by D05. |
| 35 | **Keep, fix** | D07, stated, expectation form. "For any of the three objectives" → episodic ∝ (notes). Wording of the "frequent actions" bullet from the book. |
| 36–37 | **Keep** | D04. "Probability density function VERSION" label → "density". |
| 38–39 | **Keep, fix** | D08: add γ^t or state γ = 1 (E6); per-episode form (E7). "These tricks will help you deal with high variance" → 7.2. |
| 40 | **Replace** | D05–D06: the board derivation as slides. |
| 41 | **Keep, move** | S03's check (continuous torque). "What about finite differences?" → H03 question. |
| 42 (H) | **Cut** | Recap. |
| 43 | **Cut** | Puck world learning curve without a reading task; B04's numbers show the noise directly. |
| 44 | **Keep, fix** | B05. "∝" with the baseline as in the book (13.10). "The baseline can be anything, even a random number" kept with "as long as it does not depend on the action". |
| 45 | **Keep, fix** | B10: A^{π_θ} → A^π (E12). |
| 46 | **Keep** | B12 (book box). |
| 47 | **Cut** | Empty slide. |
| 48 | **Keep** | B14. |
| 49–52 | **Move** (E11) | 8.1: actor–critic loop, Q actor–critic, the TD error as advantage (old 51's derivation is used in B14 in one line), A2C. |
| 53 | **Keep, split** | D10, B17. |
| 54–58 | **Cut** (E10) | Exam-excluded in the old course; time scales and backward traces are outside the accepted scope (`backward_trace_math: false`). |
| 59 | **Keep, rebuild** | B16 with numbers. "Recall the aliased gridworld" becomes the corridor. "Luckily … we can avoid introducing any bias" → cut (compatible approximation is out, E10). |
| 60–63 | **Cut** (E10) | Compatible function approximation: not in the accepted scope. Optional hidden appendix pointer to Sutton et al. (2000). |
| 64–66 (H) | **Cut / move** | Deterministic policies and natural gradients: Week 8–9 (8.2 small-update intuition; DDPG/TD3 are extension). |
| 67 | **Move** | Summary picture: 8.1 or 8.2. |
| 68 | **Cut** | Empty. |

### `9 - Deep PG.pptx` (Week 7-relevant slides only)

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 5–6, 8 | **Merge** | S02–S03 (network outputs as preferences or mean); DPG 6's advantage form → B10. DPG 8's "½Σ^{−1}" Gaussian score has a stray ½ for a symmetric Σ; not reused (multivariate case is not taught). |
| 9–10 | **Keep picture (optional)** | D08: Schulman–Abbeel's batch REINFORCE (Williams 1992). |
| 13 | **Split** | B04 (noisy, high variance); "poor sample efficiency" and "step sizes" → 8.2. |
| 11–12, 14–31 | **Move** | 8.2 (importance ratio, step sizes, NPG/TRPO intuition, PPO). |
| 32–34 | **Move** | 8.1 (deep actor–critic, advantage estimation). |
| 35–44 | **Move / extension** | Week 9 (SAC contrast) and extension (DPG, DDPG, TD3). |

**Teaching purpose of cut material** (workflow step 1):
- **Aliased gridworld (old 8–10):** "the best policy can be stochastic". S01 keeps the lesson with numbers; E3's
  alternative restores the picture.
- **Puck world (old 43):** "learning with REINFORCE is noisy". B04 shows it with the course's own example.
- **Compatible function approximation (old 60–63):** "when can a critic avoid bias?". B16 says that the bias exists
  and shrinks with a better critic; the exact conditions are optional reading (E10).
- **Time scales and traces (old 54–58):** already exam-excluded; the accepted plan keeps only an existence mention
  (8.1).
- **J_av, J_ar (old 16):** continuing objectives; average reward had its accepted 5 minutes in 3.1.

## Reference courses: what was used

Evidence, not authority. Page numbers are in the local copies under `sources/<id>/lectures/` or the PDFs indexed in
`output/lectures/session_sources.md`.
- **CS224R L3** (pp. 5–20): "do more of the good stuff" intuition, the trajectory derivation, causality with the
  humanoid example, baselines and reward scale (D02, D05–D06, B04–B05).
- **CS285 L5** (pp. 3–23): the trajectory derivation, Gaussian example, reward-to-go, baselines (D05–D06, S03, B05);
  **L6** (pp. 4–7): advantage and value fitting (B10, B12).
- **CS234 L5** (pp. 24–61) and **L6** (pp. 9–23): stochastic policy search, softmax/Gaussian scores, unbiased
  baselines (H01, S02–S03, B05, B08).
- **Silver L7** (pp. 3–34): motivation, finite differences, score function, the policy gradient theorem (P02, H03,
  D02, D07).
- **Abbeel L3** (pp. 5–32): likelihood-ratio gradients, trajectory decomposition, baseline choices (D05–D06, B10).
  Image-based slides; not re-inspected beyond the session index's description.
- **Sutton slides 24-PG** (pp. 2–15) and **23-biopsych**: policy-gradient theorem and baseline (D07, B05); conditioning
  and dopamine (B03, B07, B14).
- **Book:** Chapter 13 (§§13.1–13.5, 13.7) for every derivation and both corridor figures; §§14.2.2, 14.3, 15.3, 15.7
  for the psychology lines.

Not in the local sources: Kohl and Stone (2004), Szita and Lőrincz (2006), Salimans et al. (2017), Williams (1992),
Sutton et al. (2000). Claims resting on them are names and dates only, marked "verify" where a number would be quoted.
Williams's acronym (REINFORCE = REward Increment = Nonnegative Factor × Offset Reinforcement × Characteristic
Eligibility, where the "offset" is the reward minus a baseline) would make a good B05 aside; it is from memory and must
be checked against the paper before use.

## Notation

From `course/notation_guide.md`: **θ**, π(a ∣ s, **θ**), π_**θ**, J(**θ**), b(s), A_t (advantage context), Â_t,
**w**, v̂(s, **w**), **x**(s, a), **x**(s), ∇, G_t, δ_t, α, γ, q^π, v^π, ℳ. Conversions from the old decks (O9
style): π_θ(s, a) → π(a ∣ s, **θ**); f(s, a) → **x**(s, a); V^{π_θ} → v^{π_**θ**}; Q^{π_θ} → q^π; R(s, a) → ℛ(s, a);
V̂(s, w) → v̂(s, **w**); "log" → ln (if approved); old 21's δJ/δθ → ∂J/∂θ.

**Missing, needs approval (E12):**

| Item | Needed by | Proposal |
| --- | --- | --- |
| Action preference | S02, D04 | h(s, a, **θ**), as in the book (eq. 13.2). |
| Logarithm | D02 onward | ln, as in the book (ln π, ∇ln π). Alternative: log, as in CS285 and the old decks. |
| Gradient estimate | D01, D08, B05 | ĝ (hat = estimate, as in Â_t). Alternative: words ("estimate of ∇J"). |
| Episode probability | D05 | Pr{episode ∣ **θ**}, with the episode written out (S_0, A_0, R_1, …, S_T). **No τ**: τ is the Polyak rate (O5). Alternative: τ for a trajectory, relying on context. |
| Gaussian mean and standard deviation | S03, D04 | μ(s, **θ**), σ(s, **θ**), as in the book (§13.7). μ also denotes the state distribution μ^π(s); the policy gradient theorem is written in expectation form (D07) so that μ^π does not appear on Week 7 slides. Alternative: m(s, **θ**) for the mean. |
| Two step sizes | B12 | α_**θ**, α_**w** (subscript = which parameters). The book writes α^**θ**, α^**w**; the guide reserves superscripts for policy and optimality marks. |
| Advantage function | B10–B11 | A^π(s, a) = q^π(s, a) − v^π(s), superscript as in v^π (O1 asked to settle function notation when needed). |
| One-step expected reward | D02–D03 | ℛ(a) for a single-state problem (the guide allows other argument forms of ℛ). |
| Score | D02 | The word "score"; the book's "eligibility vector" named once (it clashes with eligibility traces, mentioned in 8.1). |
| Perturbation direction (finite differences) | H03 notes only | **u**_k, ε as on old 24, notes only. ε also means ε-greedy; acceptable in notes. |

## Prerequisite and timing checks

- **No forward references.** 7.1 uses returns (Week 3), features (Week 5) and Week 6's continuous-action question.
  7.2 uses 7.1, Week 3's bias–variance and Week 5's gradient MC (B12). No importance ratio (8.2), no n-step or λ
  advantage (8.1), no backward traces.
- **Worked activities protected:** D03–D04 (9 minutes) in 7.1; B02 (6), B06 (4), B11 (5), B15 (3) in 7.2.
- **Totals:** 7.1 targets sum to 61.5 (allocation 59; fine for delivery under the 63-minute allowance; planning
  estimate unchanged; segments 4.5 + 10 + 9 + 38 against the accepted 0 + 10 + 9 + 40, the opener taken from the
  derivation's 40). 7.2 sums to 54.5 (allocation 54) + 5 administrative.
- **Density:** 7.1 introduces the parameterized policy, the score, the trajectory gradient and REINFORCE; every one is
  used in the corridor sample. 7.2 introduces the baseline, the advantage and the critic; each gets a calculation.
- **Hidden workload:** none. No reading or video is assigned.
- **Scope claims:** no state-of-the-art claim. History items carry names and dates; convergence statements carry the
  book's conditions in the notes.
- **Week 8 interface:** B17 ends on actor–critic and GAE, which 8.1 `actor_gae` opens with; B16 gives 8.1 its
  "critic bias" motivation already in numbers.

## Open points to carry into the cross-review

1. E2: the corridor as the single running example, against a separate motivation example.
2. E6–E7 and A3: one estimator convention (γ^t or not; per-episode sum) for lecture, A3 and Midterm 2.
3. E12: notation approvals (especially ln versus log, τ versus "episode", μ for the Gaussian mean).
4. E9/B16: whether the aliased-critic demonstration is too strong a claim for 12 minutes, or should be framed only as
   "one example of critic bias" (the notes already say so).
5. History facts not in local sources (Kohl and Stone 2004, Szita and Lőrincz 2006, Salimans et al. 2017, Williams
   1992): check before rendering.
6. B07's note: the state-value baseline is not better than a constant here (one shared parameter). Keep it as a
   discussion point, or choose an example where v^π(s) clearly helps (would need a second example).
