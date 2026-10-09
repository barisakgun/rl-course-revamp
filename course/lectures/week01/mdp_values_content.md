# MDPs, returns and values — shared content proposal (frozen)

**Shared:** instructor, ChatGPT and Claude. Revised by ChatGPT, 2026-10-07, following explicit instructor approval of C1–C8 and C10–C12, omitting C9 (deck decisions B12–B15).
**Status: FROZEN** at the instructor handoff of 2026-10-08 (handed-off deck `2223e515…`): the record of the content agreed before the instructor took over the PPTX; do not edit it. Current deck status: [deck decisions](../../../decisions/lectures/mdp_values.md).
**Historical scope at handoff:** session 1.2 `mdp_values`; **19 live slides, approximately 62 minutes; allowed ceiling 65, not a target**. M00 is the new title; M01–M18 retain their IDs. Battery ageing, position/velocity and the tail bound are notes-only backups, not additional slides or assigned work.
**Authority:** [deck decisions](../../../decisions/lectures/mdp_values.md), [notation guide](../../notation_guide.md). **Review and responses:** [shared review](../../../analysis/lecture_suggestions/mdp_values_review.md).

## Rendering conventions

- Only **Display** text, displayed equations/tables and requested visuals belong on the slide. Notes, timing, reuse instructions and review metadata are not slide text.
- Keep the existing lecture template. Preserve editable equations and diagrams. Reuse native equation objects from the old MDP deck where identified, editing their notation; do not copy surrounding obsolete material. If native reuse is inadequate, retain the formula's LaTeX source with the rendered equation.
- All old-deck numbers below are **PPTX positions including hidden slides**. “Adapt” specifies an object or explanation to reuse, not an unchanged whole slide. The instructor retains final slide-selection/editing authority under B2.
- The robot figure comes from the instructor-edited **Introduction slide 14**, not the frozen Introduction Markdown. Check the saved figure has wait reward **0**. Copy the figure alone; omit the old example traces and surrounding text. Do not modify that source deck.
- Reward indexing is always \(S_t,A_t,R_{t+1},S_{t+1}\). Use \(\mathbb E\), lower-case \(v_\pi,q_\pi\), numeric robot probabilities and the approved explicit-reward history. No \(\alpha,\beta\) probability labels, extra trajectory symbol or three-argument reward function is needed.
- M12 is the student calculation: show prompts, keep answers in speaker notes, and leave room for annotation. No animation implementation is required.
- Explicitly labelled **Live explanation** text is taught within that slide's allocation even when kept in speaker notes. It is distinct from optional notes-only backups. M10's motivation precedes its formula; M11's deadline contrast, M14's sampling explanation and M16's verbal value relationship are required live.
- M11 layout fix (R14/C12): lower the terminal box clear of the title divider and move its arrow endpoint with it. Check the fresh preview; do not mark this fixed from the Markdown alone.

## M00 — MDPs, returns and values

**Time:** 0.5 minute. **Build:** dedicated title slide in the established template; adapt old MDP slide 1's title-slide role.

**Display**

> MDPs, returns and values
>
> From the recycling robot to a mathematical model

**Note:** Session 1.2. Brief opening only; the interaction loop follows on M01.

**Sources:** old MDP 1; decision B12.

## M01 — The interaction loop

**Time:** 3 minutes. **Build:** restore old MDP slide 3's native perception–action–reward loop with the label edits below; do not substitute the state timeline.

**Display**

> Observe \(O_t\), choose \(A_t\), then receive \(R_{t+1}\) and \(O_{t+1}\).

**Visual:** retain Agent, Environment, Sensors and Actuators and their directed loop. Label the incoming observation before the action \(O_t\); the outgoing action \(A_t\); the consequence reward \(R_{t+1}\), with next observation \(O_{t+1}\). Use two clearly distinguished time labels on the observation path: “before action: \(O_t\)” and “after action: \(O_{t+1}\)”. Reward comes from the environment to the agent. Preserve the original diagram's roles while correcting the old \(R_t\) label throughout.

> Capital letters: random variables. Lower-case letters: particular outcomes.

**Note:** Formalize the interaction already encountered; do not reteach unfinished 1.1 material. Keep observation and state distinct here. The state timeline and state/action transition explanation move to M06, after M03–M04 define history and state. The fully observed robot permits identifying its observed charge with its model state; this is not a general equivalence.

**Sources:** old MDP 3; book §3.1.

## M02 — The recycling robot

**Time:** 3 minutes. **Build:** copy the updated native robot figure from Introduction PPTX 14; retain all action/outcome arrows and their numeric labels.

**Display**

\[
\mathcal S=\{\text{high},\text{low}\}
\]
\[
\mathcal A(\text{high})=\{\text{search},\text{wait}\},\qquad
\mathcal A(\text{low})=\{\text{search},\text{wait},\text{recharge}\}.
\]

Caption: “Our numeric adaptation of Sutton & Barto, Example 3.3. Wait means idle without collecting cans.”

**Figure requirements:** high-search → high: 0.8, reward 2; high-search → low: 0.2, reward 2; low-search → low: 0.7, reward 2; low-search → high: 0.3, reward −3 (rescue); both wait loops: probability 1, reward 0; low-recharge → high: probability 1, reward 0. Reward −3 is the whole failed-search reward, not an additional penalty after +2.

**Note:** Ask why \(\mathcal A\) depends on state. High-charge recharge is omitted as a modelling choice. These are high-level decisions; the state need not describe every physical component of the robot. Do not restore the book's positive waiting-reward story or the former illustrative +1.

**Sources:** accepted Introduction figure/A14a; book Example 3.3, printed 52–53.

## M03 — Observation, history and state

**Time:** 2.5 minutes. **Build:** adapt old MDP 4–5, replacing the old history sequence.

**Display**

> \(O_t\): the observation received now.
>
> \(H_t\): the information accumulated before choosing \(A_t\).

\[
H_t=(O_0,A_0,R_1,O_1,\ldots,A_{t-1},R_t,O_t),\qquad H_0=(O_0).
\]

> The environment's full state need not be visible to the agent.
>
> The agent builds its state from the available history. Calling it a state does not make it Markov.
>
> With the battery gauge hidden, the latest observation need not identify the charge.

**Note:** Answer the earlier gauge question rather than restarting it as an exercise. Past observations, actions and rewards can inform charge without uniquely revealing it. This convention keeps rewards separate from observations; the book's §17.3 folds rewards into observations. Do not mix the two sequences. A state representation can omit irrelevant physical detail, but not information needed for the predictions being modelled.

**Sources:** old MDP 4–5; book §17.3; notation O10, now resolved.

## M04 — A Markov state

**Time:** 2 minutes. **Build:** adapt old MDP 7's controlled-process explanation. Use the following joint next-state/reward form; split the equation over two lines if needed.

**Display**

> Given the state and action, earlier history adds no information about the next state and reward.

\[
\begin{aligned}
&\Pr\{S_{t+1}=s',R_{t+1}=r\mid H_t=h,A_t=a\}\\
&\qquad=\Pr\{S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a\},
\end{aligned}
\]

> where \(s\) is the state built from history \(h\).
>
> A Markov state predicts a distribution of outcomes, not a certain outcome.

**Note:** Here \(S_t\) is the representation built from the available history. Relate the statement to high/low charge in the simplified robot model. Stochasticity itself does not violate the Markov property. Do not copy old slide 8's noise claim. The ageing question is a backup in the final notes section, not another live check.

**Sources:** old MDP 7; book §3.1 and §17.3; CS234 introduction PDF 35–38.

## M05 — A chatbot's latest message

**Time:** 2.5 minutes. **Build:** short context question adapted from CS224R introduction PDF 37; no borrowed mathematical notation or reward example.

**Display**

> Latest user message: **“Yes, please.”**
>
> Earlier question: “Would you like a shorter explanation?”
>
> Or: “Would you like a worked example?”
>
> **What earlier information would you keep to interpret “Yes, please” and choose a response?**

**Live explanation / answer:** Give students a brief chance to answer. Retaining the preceding question resolves this particular ambiguity: the latest observation is the same, but the useful context differs. Conversation history is not a guarantee of observing all user intentions or obtaining a perfect Markov representation. Keep this a transfer check, not a second fully specified MDP or an LLM-training discussion.

**Sources:** Introduction A10; CS224R introduction PDF 35–39.

## M06 — The MDP model

**Time:** 3 minutes. **Build:** adapt native equations from old MDP 11 and the component summary from 36. Replace \(T\), upper-case reward-function notation and old reward indices.

**Display**

\[
S_0,\ A_0,\ R_1,\ S_1,\ A_1,\ R_2,\ S_2,\ldots
\]

> In a Markov-state model: state \(S_t\), then action \(A_t\); consequences are reward \(R_{t+1}\) and next state \(S_{t+1}\).

> A finite MDP specifies states \(\mathcal S\), available actions \(\mathcal A(s)\), possible rewards \(\mathcal R\), and the dynamics:

\[
p(s',r\mid s,a)\doteq
\Pr\{S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a\}.
\]

> Given a state and action, which next state and reward can occur, and with what probability?
>
> For this robot, \(\mathcal R=\{-3,0,2\}\).

**Note:** The relocated timeline now follows the history/state definitions. Connect it directly to the conditional model instead of repeating M01's loop narration. For our fully observed robot the observed charge identifies the model state. Use the guide's definition sign ≐. The dynamics are time-independent in this model. The return objective adds the discount factor at M10. State/action sets are already on M02; do not repeat a full component lecture. Terminal-inclusive \(\mathcal S^+\) arrives with M11. Do not add the learning-versus-planning bridge (C9).

**Sources:** old MDP 3/11/36; book §3.1.

## M07 — Reading the robot's dynamics

**Time:** 4 minutes, including student interpretation. **Build:** native editable table. These are all nonzero rows for the continuing model.

**Display**

| State \(s\) | Action \(a\) | Next state \(s'\) | Reward \(r\) | \(p(s',r\mid s,a)\) |
| --- | --- | --- | ---: | ---: |
| high | search | high | 2 | 0.8 |
| high | search | low | 2 | 0.2 |
| high | wait | high | 0 | 1 |
| low | search | low | 2 | 0.7 |
| low | search | high | −3 | 0.3 |
| low | wait | low | 0 | 1 |
| low | recharge | high | 0 | 1 |

> For each state/action pair, do the outcome probabilities add to one?

**Note:** Concentrate on the two low-search rows; distinguish the state/action being conditioned on from the outcome. Failure gives −3 and returns the robot to high charge. The rows use fixed illustrative reward outcomes; the book's can-count rewards need not be deterministic. No separate gridworld transition tree.

**Sources:** book Example 3.3 and Exercise 3.4; accepted robot parameters.

## M08 — A reward outcome and an expected reward

**Time:** 2 minutes. **Build:** adapt old MDP 11's transition and expected-reward equations with corrected notation.

**Display**

\[
p(s'\mid s,a)\doteq\Pr\{S_{t+1}=s'\mid S_t=s,A_t=a\}
\]
\[
r(s,a)\doteq\mathbb E[R_{t+1}\mid S_t=s,A_t=a]
\]

> Searching at low charge gives **2 or −3**.

\[
r(\text{low},\text{search})=0.7(2)+0.3(-3)=0.5.
\]

> The expected reward is 0.5; neither outcome gives 0.5.

**Note:** The transition-only probability is obtained by summing over reward outcomes in the joint model. Explain that in words rather than adding another summation. The reward function here is an expectation, not a claim that rewards are deterministic given state/action.

**Optional notes only, if a source or question calls for it:** some texts condition rewards on the state alone, the state and action, or also the next state. Check whether they mean a realized deterministic reward or a conditional expectation; these assumptions are not interchangeable. Keep this explanation verbal. Do not display or introduce alternative reward-function symbols; the joint model and approved expected-reward notation suffice here.

**Sources:** old MDP 11; book §3.1.

## M09 — Policies

**Time:** 5 minutes. **Build:** reuse/edit old MDP **51**'s native deterministic/stochastic policy definitions. Slide 50 provides motivation only; do not copy its value-based action-selection claim as the definition.

**Display**

> A deterministic policy chooses an action: \(a=\pi(s)\).

| State | Example action |
| --- | --- |
| high | search |
| low | recharge |

> A stochastic policy assigns action probabilities: \(\pi(a\mid s)\).
>
> Example at low charge: search with probability 0.5, recharge with probability 0.5.
>
> **Policy probability:** which action the agent chooses.
> **Model probability:** what happens after that action.

**Note:** The stochastic example selects search at high with probability 1 and wait with probability 0 everywhere. Ask students to distinguish its 0.5 choice probability from the robot's 0.7 low-search success probability. Current policies are stationary; do not claim all policies must be stationary or deterministic. Say once: fixing a stationary policy turns this MDP into a Markov reward process. Do not start a separate chain/MRP example or an optimality theorem.

**Sources:** old MDP 50–51; book §3.5; Silver lecture 2 PDF 26–28; CS285 lecture 4 PDF 6.

## M10 — Discounted return

**Time:** 5 minutes, including 1 minute of live motivation before the definition. **Build:** adapt old MDP 21's infinite-utilities question, then reuse/edit old MDP 22's native return and recursion equations with corrected indices. Old 23 supplies spoken reasons only; no separate reasons slide.

**Live explanation before the formula:** “If the task never ends, what happens when we add all future rewards?” A hypothetical reward of +1 at every step gives an unbounded undiscounted sum; discounting by 0.5 gives 1 + 0.5 + 0.25 + … = 2. This is a hypothetical stream, **not** the robot's wait reward, which remains 0. Discounting gives less weight to later consequences and changes the objective; bounded rewards with a discount below one give a finite return. Present this motivation before pointing to the definition (no new slide or animation required).

**Display**

\[
G_t\doteq R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots
=\sum_{k=0}^{\infty}\gamma^k R_{t+k+1}
\]
\[
G_t=R_{t+1}+\gamma G_{t+1}
\]

> Here \(\gamma=0.5\): successive reward weights are 1, 0.5, 0.25, …
>
> Smaller \(\gamma\) gives less weight to later consequences.
>
> Bounded rewards and \(0\leq\gamma<1\) keep the continuing sum finite.

**Note:** Choose 0.5 for hand calculation, not as a typical deployment recommendation; appropriate discounting depends on the task and the duration of a step. The immediate reward is not discounted. Derive the one-line return recursion by grouping the later terms; this is not a Bellman value derivation. Keep the discount reasons spoken within these five minutes. Do not restore old slide 23's claims that randomness makes the future unrepresentable or that discounting guarantees convergence of all RL algorithms; omit biological/economic analogies and the stationary-preferences theorem. Leave average reward at its Week 3 location.

**Sources:** old MDP 21–23; book §3.3, printed 54–55 (including its hypothetical +1 stream); Silver lecture 2 PDF 12–13.

## M11 — One failure, two possible endings

**Time:** 4 minutes, including 1 minute for the live horizon contrast. **Build:** duplicate the native robot figure into a terminal variant. Change only the low-search failure destination: a new “out of battery” terminal state replaces rescue to high. Keep probability 0.3 and reward −3. Other transitions/rewards are unchanged. Show that changed branch clearly; full repeated figures are unnecessary if they crowd the text. **Required layout fix R14/C12:** lower the terminal box clear of the title divider and move its arrow endpoint with it; preserve readable labels and check the fresh preview.

**Display**

| Model | Failed search at low charge |
| --- | --- |
| Continuing rescue | Reward −3; return to high charge and keep working |
| Terminal failure | Reward −3; the episode ends |

> \(\mathcal S^+\) includes the terminal state.
>
> After termination, imagine a self-loop producing reward **0** forever.
>
> A terminal state can exist even if some policies never reach it.

**Live explanation — continuing, natural termination, deadline:** the rescue model keeps going; in the terminal version an event (failed search) ends an episode. A separate imposed deadline ends the task when its time is up. Time remaining can change the right action at the same physical state: a robot may recharge when there is time to use that charge, but recharging solely for later collection has no benefit when no working step remains. Account for the deadline by including time remaining in the state, or by treating time explicitly in a finite-horizon model and policy. This is a conceptual contrast, not a deadline added to our robot calculations. Stopping data collection after four steps in an ongoing task does not make that task terminal.

**Note:** The failure reward is paid once on entry; the zero-reward absorbing continuation unifies the return notation. Wait/recharge policies can avoid failure indefinitely, so use \(\gamma=0.5\) for both robot variants. A bounded episode allows an undiscounted sum, but this robot has no added deadline. Correct old MDP 21's shorthand rather than repeating it. Instructor's verbal caveat: “This should probably be penalized more, but this is just an example.”

**Sources:** old MDP 21, adapted; book §§3.3–3.4; Abbeel lecture 1 PDF 17–20 (finite-horizon, time-dependent policies); decisions B7/B13.

## M12 — Calculate the terminal return

**Time:** 5 minutes including student calculation. **Build:** native path/table plus open calculation space; reuse old MDP 24's calculation structure, replacing the caveman example.

**Display**

> The first three search transitions from our earlier example, now with a terminal ending:

| Time \(t\) | State \(S_t\) | Action \(A_t\) | Reward \(R_{t+1}\) | Next state \(S_{t+1}\) |
| ---: | --- | --- | ---: | --- |
| 0 | high | search | 2 | high |
| 1 | high | search | 2 | low |
| 2 | low | search | −3 | terminal |

\[
T=3,\qquad G_3=0,\qquad G_t=R_{t+1}+0.5G_{t+1}
\]

> Work backward: \(G_2=?\quad G_1=?\quad G_0=?\)

**Answer in speaker notes:** \(G_2=-3\); \(G_1=2+0.5(-3)=0.5\); \(G_0=2+0.5(0.5)=2.25\). Direct check: \(2+0.5(2)+0.5^2(-3)=2.25\). \(G_3=0\) because the penalty was already received as \(R_3\); it is not counted again. The finite discounted episode sum ends at \(R_T\). Do not multiply realized rewards by transition probabilities when calculating the return of this observed path.

**Sources:** old MDP 24, adapted; book §§3.3–3.4.

## M13 — The continuing return has a tail

**Time:** 4 minutes. **Build:** same visual trajectory language as M12; the third transition now rescues the robot to high, and a fourth search gives 2 and leaves high, as in 1.1.

**Display**

> Observed rewards: **2, 2, −3, 2**, then the robot continues.

> Four-step discounted reward sum:

\[
2+0.5(2)+0.5^2(-3)+0.5^3(2)=2.5
\]

> Complete continuing return:

\[
G_0=2.5+0.5^4G_4
\]

> The excerpt alone does not tell us \(G_4\).

**Note:** This is the same prefix students saw in 1.1. Contrast the complete terminal return 2.25 with the continuing expression, not with a falsely completed 2.5. Do not label the truncated backward values as complete \(G_t\). The second old trace has prefix sum 3.25 and its own tail; keep that in notes, not a second live calculation. A single excerpt cannot settle which policy has the greater expected complete return. The 0.375 tail bound is a backup below.

**Sources:** accepted Introduction trace; book §3.3; shared-review R05/R10/R11.

## M14 — Values are expected returns

**Time:** 4.5 minutes, including the repeated-return explanation. **Build:** reuse/edit old MDP 58's native value definitions; omit its alternative trajectory notation and return recap. Use lower-case value functions.

**Display**

\[
v_\pi(s)\doteq\mathbb E_\pi[G_t\mid S_t=s]
\]

> Start in state \(s\), then follow policy \(\pi\).

\[
q_\pi(s,a)\doteq\mathbb E_\pi[G_t\mid S_t=s,A_t=a]
\]

> Start in \(s\), take action \(a\), **then** follow \(\pi\).
>
> A return belongs to a trajectory. A value averages possible returns under a policy.

**Live explanation — estimating values:** run repeated independent episodes from the same state under the same policy and average their complete discounted returns to estimate the state value. Use the terminal robot under always-search as the illustration: it terminates with probability one; other robot policies need not. To estimate an action value, also fix the first action, then follow that same continuation policy. Averaging four-step excerpts estimates the expected four-step sum, not automatically the full continuing value. More samples reduce sampling noise; they do not supply the missing tail. No estimator notation, Monte Carlo update or new exercise.

**Note:** Explain the second definition as specifying the first action even if the policy would not choose it; this avoids treating an impossible action under a deterministic policy as an undefined classroom example. The expectation includes stochastic transitions and any stochastic policy choices. Do not introduce value estimates \(V,Q\), Monte Carlo updates or a Bellman expansion here.

**Sources:** old MDP 25/58; book §3.5, printed 58–59; Silver lecture 2 PDF 28.

## M15 — A policy whose values we can calculate

**Time:** 3 minutes. **Build:** new short example based on the same robot.

**Display**

> Let \(\pi\) **always wait**, at either charge level.
>
> Waiting preserves charge and gives reward 0.

\[
G_t=0+0.5(0)+0.5^2(0)+\cdots=0
\]
\[
v_\pi(\text{high})=v_\pi(\text{low})=0.
\]

> What if we take one different action, then always wait?

**Note:** This policy is chosen because students can compute its values directly, not because it is desirable. The infinite zero sequence is harmless even though this policy never terminates. Distinguish this from the nonzero continuing rewards of search policies.

**Sources:** value definitions applied to the accepted zero-wait model.

## M16 — The first action and the continuation policy

**Time:** 4 minutes. **Build:** native table/equations; all entries use the same always-wait policy \(\pi\) from M15.

**Display**

> Take the specified action once, then always wait:

| Starting state and first action | Expected complete return |
| --- | --- |
| high, search | \(q_\pi(\text{high},\text{search})=2\) |
| low, search | \(q_\pi(\text{low},\text{search})=0.7(2)+0.3(-3)=0.5\) |
| low, recharge | \(q_\pi(\text{low},\text{recharge})=0\) |

> Why is recharging worth zero here, even though it can be useful?

**Live explanation:** A state's value averages its action values according to the policy's action probabilities. For a deterministic policy it is the value of the chosen action; always-wait chooses wait, whose action value is zero. Here recharge has zero value because the continuation waits forever. Under search-high/recharge-low, restored charge has value because the continuation uses it to collect cans. Keep this in words; formal value relationships and Bellman expansions remain in Week 2.

**Answer in speaker notes:** After the first action, every reward is zero because the policy waits forever. Recharging restores charge but that charge is never used to collect cans. Action values depend on the continuation policy. Here \(q_\pi(s,a)=r(s,a)\) only because that policy produces zero continuation rewards; the equality is not true in general. The same simple values hold in the terminal variant because termination and subsequent waiting both contribute zero after the first reward. State value averages action values according to the policy; for this deterministic policy, its chosen wait action has value zero. Do not add the next-state Bellman formula from old MDP 59.

**Sources:** book §3.5; old MDP 59's state/action-value relationship as explanation only.

## M17 — Values of the two familiar policies

**Time:** 2.5 minutes, including the explicit policy objective. **Build:** native table, with model and discount clearly stated. Show these results, do not derive them.

**Display**

> Continuing rescue model, \(\gamma=0.5\)

> **Goal: find a policy that maximizes expected discounted return.**

| Policy | \(v_\pi(\text{high})\) | \(v_\pi(\text{low})\) |
| --- | ---: | ---: |
| Always search | 3.60 | 1.60 |
| Search at high; recharge at low | 3.64 | 1.82 |

Caption: “Complete expected discounted returns, rounded to two decimals.”

> One observed excerpt cannot rank policies. These values average complete returns.

**Live explanation:** Values let us evaluate policies and compare first actions under a specified continuation. For this finite discounted MDP, an optimal policy achieves the best expected return from every state. The table compares two policies; by itself it does not prove global optimality. Next we learn to compute values and improve decisions; the proof and improvement argument stay in Week 2.

**Note:** Exact values are (18/5, 8/5) and (40/11, 20/11). Do not call 3.64/1.82 exact. Comparing the old 2.5/3.25 prefixes with these values involves both an omitted tail and sampling variation; do not attribute all of the difference to a lucky/unlucky sample. Ask how such values can be computed without enumerating every future: that is the Week 2 bridge, not a derivation here.

**Brief spoken rescue/terminal contrast:** with these numbers and always-search, rescue restores a positive expected continuation; terminal failure removes it. Thus rescue has the higher low-state value in this example. Optional answer numbers, notes only: 1.60 versus 10/13 ≈ 0.77. This is not a general rule that termination is worse in every task. Keep this to one sentence, not a third worked comparison.

**Sources:** independently checked policy evaluation of the accepted model; shared-review R06/R07/R11; old MDP 51/53 and book §3.6, printed 62 (policy objective, without importing its equations/proof). Computational verification is not additional taught content.

## M18 — From returns to value computation

**Time:** 2.5 minutes. **Build:** short closing check, not a new definition list.

**Display**

> For our robot:
>
> - What distinguishes a reward, a return and a value?
> - Which uncertainty belongs to the policy, and which to the model?
> - What is missing when we see only the first four rewards?
>
> Next: use the model to compute values — Bellman equations and policy evaluation.

**Answer in speaker notes:** Reward is one step's feedback; return accumulates a trajectory's future rewards according to the objective; value is its expectation under a specified policy. Policy probabilities describe chosen actions; model probabilities describe subsequent outcomes. An excerpt lacks the tail and alone does not establish an expectation. No new homework, reading or video is assigned here.

## Notes-only backups

**Position/velocity (C3):** the same observed position with opposite velocities can lead to different next positions. Recent observations may help infer velocity; position plus velocity is sufficient only under an appropriate simplified motion model. A fixed observation window does not universally solve partial observability. Backup only in response to a question or in place of other narration; no additional live example or slide.

**Ageing / Markov representation (R04):** two histories leave the robot reporting low charge, but one battery is worn and has a different depletion probability. If history contains information about wear that high/low omits, high/low alone is not sufficient for the model's predictions. Add relevant information to the state or acknowledge an approximation. Do not equate noise with non-Markov behaviour. Use only in response to a question or instead of other narration; no extra slide.

**Tail bound (R05):** with \(|R_{t+1}|\leq3\) and \(\gamma=0.5\), \(|G_4|\leq3/(1-0.5)=6\), hence \(|0.5^4G_4|\leq0.375\). This conservative bound concerns the omitted tail of a realization, not sampling uncertainty in a value estimate. It is not required live content or assessed material from this session.

## Timing and handoff check

| Segment | Slides | Minutes |
| --- | --- | ---: |
| Title, interaction and robot | M00–M02 | 6.5 |
| Information and Markov state | M03–M05 | 7 |
| Joint model and expected reward | M06–M08 | 9 |
| Policies | M09 | 5 |
| Returns, horizons and endings | M10–M13 | 18 |
| Values, objective and samples | M14–M17 | 14 |
| Closing check | M18 | 2.5 |
| **Total** | **19 live slides** | **62** |

62 minutes exceeds the configured 59.5 usable minutes (70 × 0.85) by **2.5 minutes**, using the instructor-approved buffer allowance and leaving **8 minutes** of the physical lecture. **65 is a ceiling, not a target**: it would use 5.5 buffer minutes and leave 5 physical minutes. **No 1.1 carryover is counted.** Relative to the former 58-minute content, the title uses 0.5 minute recovered from closing; information gains 1, returns/horizons 2, and values 1. No other session allocation changes.

The seven-minute information block still requires concise formalization and one brief transfer question; the robot is familiar. M06 integrates the relocated timeline with the model within its existing three minutes. Protect the four-minute model-table interpretation, policy/model probability check, five-minute return calculation and always-wait value reasoning. M10's motivation, M11's horizon contrast and M14/M16/M17's live explanations are included in the times above, even when spoken from notes. If pacing runs long, shorten repeated model narration, the optional fixed-policy/MRP sentence and closing recap; do not silently drop approved live explanations or add backups. M17's table remains a shown result, not a solver exercise. The smaller buffer and conceptual density remain delivery risks; arithmetic fit is not proof of pedagogical feasibility.

This replaces the extended caveman/MRP route, repeated recaps and gridworld transition tree in the old material. Bellman derivations, matrix solutions, VI/PI, average reward and POMDP solvers remain in their accepted later locations. Scope, mastery, prerequisites, assessment and required workload are unchanged. Pacing remains an estimate until taught.

**Claude handoff:** check this revised shared content and record findings/responses in the same review file before rendering. Preserve M01–M18 and add M00; translate the new allocations and required live explanations into notes. Verify the restored old-slide-3 loop's observation/action/reward labels; the relocated M06 timeline; native equations after notation edits; both robot figures' reward labels; M12's notes/answer; M13's nonzero tail; and M17's rounding caption. Apply the required M11 terminal-box/arrow layout fix (R14/C12) and verify clearance in the fresh preview. Check M03/M06 text density and avoid crowding M10/M11 by displaying speaker-only material. Export fresh preview and text views for the saved PPTX and record its hash. Existing exports describe the earlier 18-slide version. Content stays editable through this review/render/fix loop. Do not regenerate or alter the accepted Introduction deck.

## Source locators

- [Old MDP PPTX](../../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx): 1, 3–5, 7, 11, 21–25, 36, 50–51, 53, 58–59; exact reuse and cuts above.
- [Instructor-edited Introduction PPTX](introduction_claude.pptx): native robot figure on 14; expected current reward labels governed by Introduction A14a. The renderer checks the saved source rather than the frozen proposal.
- [Sutton & Barto](../../../sources/RLbook2020.pdf): Example 3.3 and §§3.1–3.5, PDF 69–81; §3.6 opening, PDF 84 (objective only); §17.3, PDF 486–487.
- [Silver lecture 2](../../../sources/silver_rl/lectures/lecture-2-mdp.pdf): PDF 12–14, 26–28.
- [CS234 introduction](../../../sources/stanford_cs234/lectures/lecture1post.pdf): PDF 35–42, 53–55.
- [CS224R introduction](../../../sources/stanford_cs224r/lectures/01_cs224r_intro_2026.pdf): PDF 35–40, especially chatbot on 37.
- [CS285 RL basics](../../../sources/berkeley_cs285/lectures/lec-4.pdf): PDF 5–12, especially fixed-policy connection on 6.
- [Sutton MDP lectures](../../../sources/sutton/5-6-MDPs.pdf): PDF 11, 13, 28.
- [Abbeel foundations lecture 1](../../../sources/foundations-deep-rl-abbeel/l1-mdps-exact-methods.pdf): PDF 16–20, finite-horizon contrast; no solver content imported.

PDF references are physical pages. These source locators support preparation and attribution, not a new student reading assignment.
