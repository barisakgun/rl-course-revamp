# Session 1.2 — MDPs, returns and values: ChatGPT initial content suggestion

**Author:** ChatGPT, 2026-10-07. **Status:** independent initial suggestion for the second workflow pilot; not consolidated render-ready content. No Claude 1.2 suggestion was read.

**Basis:** accepted `mdp_values` session (58 minutes), [deck decisions](../../decisions/lectures/mdp_values.md), and the instructor's subsequent answers in this conversation. Those answers resolve the earlier questions: failed search gives −3 total; terminal failure also gives −3; history includes explicit rewards; **waiting now gives 0**. The instructor and Claude will synchronize the deck and related decision/notation files; this proposal uses the explicit answers even while those files still show earlier wording. Source evidence and the pre-planning discussion are in the [shared review](mdp_values_review.md).

## Main choices

- Formalize the robot directly. Use the numeric model already encountered in 1.1 instead of starting a second caveman or gridworld example.
- Introduce notation as each concept needs it, beginning with the interaction timeline. Keep the hidden-gauge and chatbot comparisons short and conceptual.
- Compute a complete return for one terminating robot trajectory, then show exactly what is missing when the same reward prefix belongs to a continuing task.
- Make values concrete with the **always-wait policy**. Its zero future rewards make both state values and action values calculable directly from their definitions. Save recursive value evaluation and optimal-policy calculations for Week 2.

## Teaching sequence and time check

These are teaching segments, not fixed slide counts. Questions and calculations are included in their times. Final old-slide selection remains with the instructor under B2.

| Segment | Minutes | Content and intended student contribution |
| --- | ---: | --- |
| 1. From the robot to an interaction timeline | 6 | Label state, action, next reward and next state; distinguish a random variable from a realized value. Recover the two charge states and available actions from the familiar figure. |
| 2. History, observation and a Markov state | 8 | Introduce the agreed history convention. Explain sufficient information for predicting consequences, using the hidden gauge and a brief chatbot context contrast. |
| 3. The model: outcomes and probabilities | 9 | Read the robot's joint next-state/reward distribution. Fill its two low-charge search outcomes; distinguish realized reward from expected immediate reward. |
| 4. Policies | 5 | Write the familiar search-high/recharge-low policy and one stochastic alternative. Separate the agent's action probabilities from the environment's outcome probabilities. |
| 5. Returns, discounting and termination | 16 | Define discounted return, explain the discount, compute a terminal trajectory backward, and contrast it with a continuing prefix. Count terminal reward once; zero rewards afterward. |
| 6. State values and action values | 11 | Define both as policy-conditioned expected returns. Work out the always-wait example and explain why an action value depends on what the agent does afterward. |
| 7. Closing check and bridge | 3 | Distinguish reward, return and value; identify which uncertainty the model and policy describe. Next session: use the model's structure to compute nontrivial values. |
| **Total** | **58** | **70 × 0.85 = 59.5 usable minutes; 1.5 remains within that allowance.** |

No 1.1 carryover enters these calculations. The extra administrative overhead applies to 1.1, not this session.

## Concrete content and worked checks

### 1–2. Information before action; consequences afterward

Use the sequence

\[
S_0, A_0, R_1, S_1, A_1, R_2, S_2,\ldots
\]

to establish that the reward produced by action \(A_t\) is \(R_{t+1}\). In the fully observed robot, the gauge supplies the high/low state. Upper-case letters identify random variables; lower-case letters identify particular outcomes. Avoid presenting a whole notation dictionary first.

For the information actually available to the agent, use the instructor-approved convention:

\[
H_t=(O_0,A_0,R_1,O_1,\ldots,A_{t-1},R_t,O_t),
\qquad H_0=(O_0).
\]

Explicitly distinguish the agent's chosen state representation from the environment's full physical description. A Markov representation retains the history's information needed to predict the next state and reward given an action; it need not predict a single certain outcome. The robot's stochastic transitions are compatible with a Markov state.

**Check:** hide the gauge. Does the newest observation necessarily suffice? No; prior actions and observations can matter. History can inform charge without uniquely revealing it. This is not a claim that a fixed number of past observations always restores the Markov property.

Use the accepted **CS224R chatbot contrast** briefly: the latest message “Yes, please” is ambiguous without what preceded it. Conversation context helps choose a response, but does not expose all hidden user intentions. This illustrates observation versus useful state information; no chatbot reward design, belief update or neural-network block is added.

### 3. Model: one action, two possible rewards

Define

\[
p(s',r\mid s,a)
=\Pr\{S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a\}.
\]

The central fill-in is the **low-charge search** row pair:

| Current state | Action | Next state | Reward | Probability |
| --- | --- | --- | ---: | ---: |
| low | search | low | 2 | 0.7 |
| low | search | high | −3 | 0.3 |

The other model rows follow the familiar diagram: high-charge search ends high/low with probabilities 0.8/0.2 and reward 2 either way; wait keeps charge and gives 0; recharge is available at low charge, returns to high and gives 0. Interpret waiting as idling without collecting cans, unlike the book's possibility of receiving cans while stationary.

**Check:** probabilities for each state/action sum to one. What is the expected immediate reward of searching at low charge?

\[
r(\text{low},\text{search})=0.7(2)+0.3(-3)=0.5.
\]

The robot receives **2 or −3**, not 0.5 on each attempt. Introduce \(p(s'\mid s,a)\) as the next-state marginal and \(r(s,a)\) as an expectation; no additional three-argument reward notation is needed. The fixed numeric outcome rewards are a teaching model, not a claim that the book specifies deterministic can counts.

### 4. Policy is not the transition model

Use \(\pi(s)\) for the familiar deterministic choice: search at high, recharge at low. Then show a stochastic policy that chooses search or recharge with probability 0.5 each at low charge and chooses search at high. Its wait probability is zero. In general, \(\pi(a\mid s)\) assigns probabilities over \(\mathcal A(s)\).

**Check:** the policy's 0.5 describes the agent's choice; the model's 0.7 describes what happens **after search is chosen**. A fixed policy turns the MDP into a Markov reward process: one brief connection, not another model-building exercise. Restrict the current examples to stationary policies; do not claim all possible policies must be stationary or deterministic.

### 5. A complete return versus a continuing prefix

Use the common discounted definition and its recursion:

\[
G_t=\sum_{k=0}^{\infty}\gamma^k R_{t+k+1},
\qquad G_t=R_{t+1}+\gamma G_{t+1}.
\]

Use \(\gamma=0.5\) for arithmetic. Explain that immediate reward has weight 1 and the next reward has weight 0.5. Smaller discounts give less weight to later consequences; the parameter is part of the objective and depends on the task/time step, not a universal recommended setting. Bounded rewards and \(\gamma<1\) keep the continuing discounted sum finite.

**Worked terminal trajectory:** high → high → low → out of battery, searching on each transition, with rewards **2, 2, −3**. The final transition ends the episode at \(T=3\). Its penalty is −3 total; the instructor may remark verbally that a real failure might deserve a larger penalty.

Start with \(G_3=0\), then have students work backward:

\[
G_2=-3,\qquad G_1=2+0.5(-3)=0.5,
\qquad G_0=2+0.5(0.5)=2.25.
\]

The same result is \(2+0.5(2)+0.5^2(-3)\). Explain the absorbing-state convention: rewards **after** termination are zero, not repeated failure penalties. Episodic return may also be written as a finite sum ending at \(R_T\); discounting is compatible with episodic tasks.

**Contrast:** in the continuing rescue model, the same three rewards leave the robot at high charge. Its return is \(G_0=2.25+0.5^3G_3\); the observed prefix alone does not tell us \(G_3\). Changing the destination isolates termination's effect while retaining the reward numbers. Neither sampled path alone ranks policies by expected return.

**Necessary caveat:** a terminal state can exist without every policy reaching it. Waiting or recharging can avoid depletion forever. Keep discounting for this robot variant rather than silently adding a deadline or promising finite undiscounted returns. A fixed time limit would be a further model choice, potentially requiring time remaining in the state; mention only if asked.

### 6. Expected return under a stated policy

Adapt the existing definitions:

\[
v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],
\qquad
q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
\]

Explain the second as: take the specified first action, **then** follow the policy. The definition applies even when that first action would not be chosen by the policy. The expectation accounts for environment outcomes and, when applicable, randomized policy choices.

**Concrete check:** let \(\pi\) always wait. Since waiting now yields zero forever,

\[
v_\pi(\text{high})=v_\pi(\text{low})=0.
\]

If we take one search and then follow this policy, all subsequent rewards are zero:

\[
q_\pi(\text{high},\text{search})=2,
\qquad q_\pi(\text{low},\text{search})=0.5,
\qquad q_\pi(\text{low},\text{recharge})=0.
\]

This needs only the earlier probability-weighted calculation, not a Bellman equation. Here action value equals expected immediate reward **because of this particular continuation policy**, not in general.

**Main reasoning question:** why is recharging worth zero under this policy even though it can be useful? Because the robot waits afterward and never uses the restored charge to collect cans. Change the continuation policy and the action's value can change. Do not present the always-wait policy as good or solve for the optimum here.

If explaining the state/action-value relationship, use the already-defined stochastic policy idea: state value averages action values according to the policy. Retain the formal weighted-sum expression for consolidation only if it fits; do not continue into a next-state Bellman expansion.

## Reuse candidates and source contributions

Old numbers below are **PPTX positions**, not PDF pages. Text and native equation objects were inspected; these are candidates for instructor selection, not instructions to keep every source slide.

| Source | Keep/adapt | Required change or limit |
| --- | --- | --- |
| Accepted 1.1 robot diagram | Same states, arrows and numeric probabilities | Instructor will change wait to 0; Claude should use that updated native figure. Do not copy the former +1 reward silently. |
| Old MDP deck 3–4, 7 | Interaction, history and Markov explanation | Reward follows action: \(R_{t+1}\). Replace the history sequence with the approved convention; use controlled-action Markov wording. Do not add the old higher-order/rat examples. |
| Old MDP deck 11, 36 | Model and MDP components, including native equations | Convert \(T\)/upper-case reward-function notation to the guide; update reward indices. Avoid the default deterministic-reward claim: the low-search example has two possible rewards. |
| Old MDP deck 21–22, 24 | Discounting, return and backward-calculation structure | Slide 21's absorbing-state line needs correction: absorption does not guarantee arrival under every policy. Fix indices; replace caveman paths with the robot path. Drop average reward here. |
| Old MDP deck 51, 58; optionally the first relationship on 59 | Deterministic/stochastic policy and value definitions | Lower-case \(v_\pi,q_\pi\), proper reward indices; omit the sequence symbol and unqualified deterministic-optimum claim. Leave next-state Bellman expansion for Week 2. |
| Sutton & Barto §§3.1–3.5; Sutton MDP lectures PDF 11, 13, 28 | Joint dynamics; zero-reward absorbing continuation; return arithmetic; expected-return definitions | Main mathematical anchor, with explicit numeric/reward adaptation. |
| Silver lecture 2 PDF 12–14, 26–28; CS234 lecture 1 PDF 35–42, 53–55 | Discount interpretation, Markov information, policies and values | Take conceptual explanations and checks, not their full MRP-first sequence. |
| CS224R introduction PDF 35–40 | Most-recent chatbot message versus context | Brief transfer check; no formal POMDP model or neural policy. |
| CS285 lecture 4 PDF 5–12; Abbeel lecture 1 PDF 16–20 | Fixed-policy process connection; distinction between finite horizon and stationary formulations | Use as explanatory support; no trajectory-distribution algebra or finite-horizon solver. |

Exact local file links and inspected page ranges are in the [source-check table](mdp_values_review.md#source-check-and-implications-for-the-initial-suggestions). Candidate old deck: [2 — Markov Decision Processes](../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx).

## Tradeoffs and review focus

Compared with the old deck, the extended caveman construction, rat-history exercise, multi-slide gridworld transition tree, stationary-preference theorem and repeated recaps are compressed or omitted. Bellman derivations and solvers remain in Week 2; average reward stays in Week 3. This recovers time for students to compute a return and explain policy-dependent values on one familiar problem, without changing accepted mastery or adding workload.

The main pacing risks are the information/Markov explanation and the first expected-return definitions. Keep the chatbot to one short context check and the model exercise to the low-search row pair. If needed, shorten the MRP connection and closing recap; protect the return calculation and value example. The 58-minute estimate is a feasibility judgment, not classroom-validated timing.

**For cross-review:** test whether this direct robot sequence gives enough intuition before formulas; check the terminal/continuing comparison and always-wait value example; compare reuse choices and time. No new instructor decision blocks the suggestion. Do not add a full optimal-policy calculation merely because it is easy for the two-state model. No slide deck or consolidated content file has been created at this stage.
