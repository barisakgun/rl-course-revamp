# Session 1.2: comparison with the old MDP deck, and suggestions (temporary)

**Temporary file (Claude, 2026-10-07)**, at the instructor's request; it is not part of the shared review. Nothing here is accepted. Updated after reading ChatGPT's `mdp_values_old_deck_comparison_chatgpt.md`, which had read the first version of this file. IDs C1–C12 replace the earlier R14–R21 to avoid colliding with the shared review's IDs.

**Inputs:**
- the rendered deck `course/lectures/week01/mdp_values_claude.pptx` (SHA-256 `cff0ce74…`);
- the old `sources/current_course/2 - Markov Decision Processes.pptx` (PPTX positions);
- ChatGPT's comparison;
- decisions B10 (delivery up to 65 minutes, not a target) and B11 (Week 2 placements; the search-tree framing deferred to MCTS).

**Excluded** (accepted by the instructor): caveman → robot; no Markov-reward-process sequence.

## Corrections accepted from ChatGPT

- **Loop labels:** label the loop with observations, not "observation O_t (state S_t)". Observation and state coincide only because the robot is fully observed (C2).
- **Old slides 42–48:** forward prediction of the next-state distribution under fixed actions belongs before Bellman backups in Week 2.1, as now placed by B11. They are not trajectory probabilities for Week 7; Claude's earlier placement is withdrawn.
- **What's new vs old:** Claude's earlier list overstated it. The old deck already had a joint next-state/reward model (11), policy-conditioned Q-values (58) and a sample-to-expectation idea (25). The new deck strengthens and reorders these.
- **Infinite-return motivation** deserves live time before the return formula (C4), not just notes.

## Converged suggestions

| ID | Change | Where | Time | Agreement | Instructor input |
| --- | --- | --- | ---: | --- | --- |
| C1 | **Title slide**, "MDPs, returns and values"; the subtitle "From the recycling robot to a mathematical model" moves off M01 | new, before M01 | +0.5 | both | — |
| C2 | **Old slide 3's perception–action–reward loop** in M01, relabelled: observation O_t, action A_t, reward R_{t+1}, next observation O_{t+1} (old R_t indexing corrected). Keep the capital/lower-case line. | M01 | 0 | both | **Q1:** where the state timeline goes (below) |
| C3 | **Environment state vs agent state**, one line ("the environment's full state need not be visible; the agent builds its state from the available history; calling something a state doesn't make it Markov"). **Make the chatbot slide a question:** "What earlier information would you keep to interpret 'Yes, please'?" | M03, M05 | +1 | both | **Q2:** extra position/velocity example? |
| C4 | **Why discount, before the formula:** "If the task never ends, what is the sum of all future rewards?" A hypothetical +1 per step is unbounded; with γ = 0.5, 1 + 0.5 + 0.25 + … = 2 (not the robot's wait reward, which is 0). Then: less weight on later consequences; bounded rewards with γ < 1 give a finite return. Don't restore the stationary-preferences theorem or the old four reasons wholesale. | before or on M10 | +1 | both | — |
| C5 | **Continuing vs natural termination vs deadline:** with a deadline, time remaining can change the right action in the same physical state. Verbal or one line; no finite-horizon equations. | M11 | +1 | ChatGPT recommends live; Claude: optional | **Q3:** live or notes? |
| C6 | **State the goal:** "We want a policy that maximises expected discounted return; values let us evaluate policies and compare first actions; next we learn how to improve decisions." For this finite discounted MDP, an optimal policy is best from every state. Integrated into the always-wait example, in words: a state's value averages its action values under the policy (for a deterministic policy, the chosen action's value). Contrast with search-high/recharge-low, where restored charge has value because the continuation uses it. | M09/M17, M16 | +0.5 | both | — |
| C7 | **Estimating a value from samples:** average the returns of repeated runs from the same state under the same policy (completed episodes, e.g. the terminal model; for q, also fix the first action). Averaging four-step excerpts does *not* recover the continuing value: more samples reduce sampling noise, not the missing tail. No Monte Carlo update or notation (Week 3). | M14/M17 | +0.5 | both | — |
| C8 | **Other reward conventions** R(s), R(s, a), R(s, a, s′): notes only, when a question or source makes them useful. No new displayed notation (guide approval would apply). | M08 notes | 0 | both | — |
| C9 | **Learning vs planning bridge:** one short transition, "the model lets us compute ahead; experience can teach values, a policy or a model". | M06/M08 | +0.5–1 | both: optional | **Q4:** did 1.1 cover it? |
| C10 | **Discount reasons:** keep spoken from the notes; don't copy old slide 23. | M10 notes | 0 | both | — |
| C11 | **Later placements:** already accepted (B11): transition prediction and value/Bellman relationships in 2.1; reward sensitivity in 2.2; search-tree framing decided at MCTS. Nothing to do in 1.2. | — | 0 | both | — |
| C12 | **M11 layout polish:** lower the "out of battery" box slightly off the title rule, moving its arrow with it (ChatGPT's deck review, shared review R14). Rendering only. | M11 | 0 | both | — |

Not restored (both): the rat example, belief-state or RNN equations, the stationary-preferences theorem, the claim that discounting guarantees convergence of all RL algorithms, and the biological/economic analogies.

## Instructor answers (2026-10-07, in the Claude conversation; not yet recorded in the decision file)

- **Q1: (b).** Move the state timeline and the "state S_t, action A_t → R_{t+1}, S_{t+1}" line to M04/M06, after state and history are defined. M01 shows the loop with observations only.
- **Q2: no** position/velocity example; it stays a backup at most.
- **Q3: the deadline contrast (C5) is live,** about 1 minute.
- **Q4: no** learning vs planning bridge (C9 dropped).
- **Q5** (not answered explicitly): implied by Q3 and Q4, C1–C7 are adopted for about **62 minutes**, within the 65-minute ceiling.

Selected set: **C1–C8, C10–C12; C9 dropped.**

## Ambiguities needing the instructor (original questions, answered above)

- **Q1. Where the state timeline goes once M01 shows observations.** Today M01 shows S_0, A_0, R_1, … and "state S_t, then action A_t; reward R_{t+1}, next state S_{t+1}". With the loop labelled by observations, writing states on the same slide mixes the two before state is defined (M03).
  - (a) Keep it on M01 with "for our fully observed robot, the state is the observation".
  - (b) Move the state timeline and transition line to M04/M06, after state and history are defined.
  - (c) Drop it; H_t (M03) and p(s′, r ∣ s, a) (M06) already carry the sequence.

  *Claude recommends (b).*
- **Q2. A second state-construction example** (position with opposite velocities) in addition to the strengthened chatbot question. *Both recommend no:* keep it as a backup.
- **Q3. Deadline contrast (C5) live or in the notes.** *ChatGPT recommends live (+1 min); Claude is neutral.* It's the old deck's finite-horizon point, and the 65-minute allowance covers it.
- **Q4. The learning vs planning bridge (C9).** In 1.1 it was an optional spoken remark, and the lecture stopped before it. Include it in 1.2 if it wasn't delivered.
- **Q5. Target length.** With all of C1–C7: about **62 minutes** (both AIs). Dropping C5 and C9 gives about 61; 65 is a ceiling, not a target.

## Timing (if C1–C7 are adopted; C9 not included)

| Segment | Now | Proposed |
| --- | ---: | ---: |
| Title, loop and robot | 6 | 6.5 |
| Information, Markov state, chatbot | 6 | 7 |
| Model and expected reward | 9 | 9 |
| Policies | 5 | 5 |
| Returns, horizons, endings | 16 | 18 |
| Values, goal, samples | 13 | 14 |
| Closing | 3 | 2.5 |
| **Total** | **58** | **62** |

Usable time is 59.5 minutes. 62 uses 2.5 of the lecture's buffer; the ceiling is 65 (B10).
