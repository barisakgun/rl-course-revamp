# Deep Q-learning · first-render content

**Frozen at the first render (2026-11-16).** Historical: the PPTX `deep_q_learning_claude.pptx` is the deck's source from that render on; status in the deck decision file. Shared · ChatGPT · 2026-11-16. First-render input for the Week 6 deck. [Deck decisions](../../../decisions/lectures/deep_q_learning.md) · [Shared review](../../../analysis/lecture_suggestions/deep_q_learning_review.md) · [Notation](../../notation_guide.md). Freeze at first render. Give every slide its ID, time, source and answer cues in the notes. The bold headings are slide titles. Reveal answers after students attempt the prompts.

## Renderer handoff and route timing

Build both replay alternatives and both worked examples for instructor inspection. Label the alternatives on screen and in notes by choice. Select one replay slide independently of the worked example. Pair the 6.1 worked example with its own 6.2 slides. Keep the 6.2 divider visible and H01–H03 hidden. Reuse native shapes and equations where identified. Replace inherited notation and notes. “Old P” means PPTX slide number in [8 – Deep QL](<../../../sources/current_course/8 - Deep QL.pptx>), “Control P” in [5 – Model Free Control](<../../../sources/current_course/5 - Model Free Control.pptx>), and “VFA P” in [6 – Value Function Approximation](<../../../sources/current_course/6 - Value Function Approximation.pptx>).

| Session | Order and target minutes | Total |
| --- | --- | ---: |
| 6.1 | V00, V00a, V01–02 (1+2+4+4), V03-A or B (3), V04–08 (4+3+5+4+4), V09–11 on one route (4+6+6), V12–14 (1+3+3) | 57 |
| 6.2 | D00–02 (1+4+3), D03–05 (5+3+4), D06–07 on one route (4+4), D08–10 (4+6+5), D11–13 (6+3+3) | 55 |

Every route preserves the 20-minute double-estimator block (D03–07), four minutes writing the patch (D07), and the 15-minute ablation (D08–10). Both sessions retain 15 minutes outside targeted delivery. Protect the prediction, calculation and explanation prompts. Reveal intermediate values if arithmetic runs long.

## 6.1 · DQN as approximate Q-learning

**V00 · Deep Q-learning · 1 min.** Course title, instructor, Fall 2026. Notes: retrieve Week 5’s closing question about richer features, reusable experience and more stable targets.

**V00a · What Week 5 left open · 2 min.** Added by Claude at render (instructor, 2026-11-16, D13). Left: Week 5's G12b control table with the bottom-right cell (Q-learning, nonlinear: ✗ can diverge) highlighted. Right: G14's three wishes, each with the mechanism that answers it: richer value functions → a network with one output per action; reusable experience → replay; more stable targets → a target network copied every C updates. Ask: "Which wish does each mechanism serve?" before revealing the right-hand labels. Notes: none of the three restores a convergence guarantee; DQN is nonlinear Q-learning, so the ✗ still describes it. Source: Week 5 deck G12b, G14.

**V01 · From frames to action values · 4 min.** Old P15’s Atari image and P3’s state-in, action-values-out panel. Display four recent frames → learned features → one estimated return per joystick action. Ask “Which way is the ball moving?” Reveal the temporal order. Caption: “Same architecture and training procedure, trained separately on 49 games. Above 75% of human-normalized performance on 29.” Notes: random play anchors 0% and the human tester 100% on each game’s scale. Frame history supplies motion information. Changes in game score supply the reward, clipped for training in this study. [Mnih et al. 2015, Fig. 3 and Extended Data Table 2](https://doi.org/10.1038/nature14236)

**V02 · Train the output for the action taken · 4 min.** Reuse old P4–5’s semi-gradient update. Mark the recorded action at the current state and the greedy action at the successor. Display, for a nonterminal transition,
\[
U_t=R_{t+1}+\gamma\max_a\hat q(S_{t+1},a,\mathbf w),\qquad
\mathbf w\leftarrow\mathbf w+\alpha[U_t-\hat q(S_t,A_t,\mathbf w)]\nabla\hat q(S_t,A_t,\mathbf w).
\]
For a terminal transition display \(U_t=R_{t+1}\). Ask which output receives the error. Notes: backpropagate from the recorded action’s current prediction. The label stays fixed during differentiation. An update to shared weights can change a successor prediction used in the next label.

**V03-A · Replay motivation A · Consecutive frames · 3 min.** Draw three schematic Breakout frames with the same paddle and bricks and the ball moving one position right/up each time. Draw a later frame with the ball across the screen. Ask which region dominates three successive updates and which regions could appear together in a batch drawn from memory. Reveal a batch spanning both. Notes: distinguish sample mixing from reuse. Retain V02’s question about the target for V06.

**V03-B · Replay motivation B · Four updates on the same eight examples · 3 min.** One shared prediction, initially 0. Targets A = +1 and B = −1. Each step moves halfway to the mean target of its pair. Reveal the batch order, ask for the direction of movement, then reveal the values.

| Pair order | After 1 | After 2 | After 3 | After 4 |
| --- | ---: | ---: | ---: | ---: |
| AA, AA, BB, BB | 0.5 | 0.75 | −0.125 | −0.5625 |
| AB, AB, AB, AB | 0 | 0 | 0 | 0 |

Notes: both conditions use the same examples, batch size, optimizer steps and step size. AB is deliberately balanced. Uniform replay can draw AA or BB. This is a supervised illustration of the effect of grouping. Show sample reuse separately on V04.

**V04 · Draw training examples from replay · 4 min.** Reuse old P9–10’s buffer picture and VFA P57’s collection/fitting distinction. Append a transition and terminal flag to bounded 𝒟, evict the oldest when full, then draw a uniform minibatch after warm-up. Draw one old row into two different updates. Ask how many environment steps produced that row. Answer: one. Notes: distinguish reuse from increasing optimizer steps per interaction. Random sampling reduces temporal clustering while retaining the buffer’s coverage.

**V05 · Why an old action supplies a Q-learning update · 3 min.** Show one stored transition. Ask students to identify its recorded action and the source of the greedy successor value. What else would sampled SARSA need? Notes: with unchanged dynamics, the reward and successor supply a sample conditional on the recorded state and action. Q-learning constructs its greedy bootstrap from successor values. A stored SARSA successor action came from the behaviour policy that acted then. The buffer can mix many earlier behaviour policies.

**V06 · Freeze the label for five updates · 5 min.** Repeat Week 5’s I02 transition five times: current state valued at \(w\), successor at \(2w\), reward 0, γ = 0.9, α = 0.1, initial weight 10. The current-weight label is \(1.8w\); the snapshot label starts at 18. Ask for update 2. Reveal update 5 and the copy.

| Weight after update | Start | 1 | 2 | 5 |
| --- | ---: | ---: | ---: | ---: |
| Recompute the label each step | 10 | 10.8 | 11.664 | 14.693 |
| Hold the label at 18 for five updates | 10 | 10.8 | 11.52 | 13.276 |

Display “After update 5, copy the weight. The next label is 23.90.” Notes: within the frozen block \(w\leftarrow w+0.1(18-w)\). Holding a label fixed in one derivative and freezing its generating weights across optimizer steps are distinct operations. Growth continues across copies in this experiment. These numbers apply to repeated updates on one row of the earlier construction.

**V07 · Construct the target and fit the minibatch · 4 min.** Reuse old P11 and P13. Each sampled \((s_j,a_j,r_j,s'_j)\) carries its terminal flag. Display
\[
U_j=\begin{cases}r_j & \text{terminal},\\ r_j+\gamma\max_a\hat q(s'_j,a,\mathbf w^-)&\text{otherwise},\end{cases}
\qquad L(\mathbf w)=\underset{j\text{ in minibatch}}{\operatorname{mean}}\;\tfrac12[U_j-\hat q(s_j,a_j,\mathbf w)]^2 .
\]
Ask which weights the optimizer changes. Notes: targets are detached. A delayed snapshot can lag behind new information. A second copy of the parameters supplies predictions with no second backward pass. The mask denotes true termination. At an external time limit on a continuing task, bootstrap from the final observation before reset.

**V08 · The DQN loop · 4 min.** Rebuild old P12 around three clocks (environment steps, optimizer steps, target copies).

1. Initialize the online weights. Copy **w**⁻ ← **w**. Create an empty replay buffer.
2. Choose an ε-greedy action with the online network. Step the environment, store the transition and terminal flag, and advance or reset the episode.
3. After warm-up, draw a uniform minibatch. Compute targets with **w**⁻ and gather current predictions at the recorded actions.
4. Take one optimizer step on the mean loss with respect to **w**.
5. After every C learner updates, copy **w**⁻ ← **w**. Continue collection.

Notes: ask what changes during warm-up, during an ordinary update and on the update that triggers a copy.

### Worked example A · Train two output biases

**V09-A · Act, append, sample · 4 min.** Two actions, L/R. All rewards in this episodic toy lie in [−1,+1]; γ = 0.5. Freeze the features and head weights; only the additive bias of each output is trainable. Behaviour takes right, receives −1 and reaches termination. Show three buffer cards (older nonterminal, intervening, newest terminal); reveal the uniform draw of the first and third. Successor outputs are ordered (left, right).

| Drawn row | Recorded action | Reward | Online at recorded action | Online at successor | Target at successor |
| --- | --- | ---: | ---: | --- | --- |
| Older, nonterminal | left | +1 | 2 | (4, 2) | (2, 6) |
| Newest, terminal | right | −1 | 0 | — | — |

Notes: these are supplied predictions. Reward magnitude ≤ 1 gives discounted return magnitude ≤ 2. The prediction of 6 supplies a question for 6.2. One large prediction alone cannot establish statistical bias.

**V10-A · Compute two labels and one loss · 6 min.** Retain the table. Ask for each target, target minus recorded prediction, and mean half-squared error. Reveal targets (4, −1), errors (+2, −1), loss (4+1)/4 = **1.25**. Notes: row one uses 1 + 0.5 × 6. Row two uses the reward alone.

**V11-A · Follow the change to the successor · 6 min.** Plain SGD with step size 0.1. Ask which predictions at other states move. Reveal:

1. Bias changes +0.10 for left and −0.05 for right. Each contributes once to the two-row mean.
2. At the first successor, online outputs move (4, 2) → (4.1, 1.95). A label from current online weights would move 3 → 3.05.
3. The target-network label stays **4** through the optimizer step. Copy **w**⁻ ← **w** now and recompute: 1 + 0.5 × 4.1 = **3.05**.

Notes: each bias is shared across states for its own action. Save the **pre-update, pre-copy** V09-A snapshot for D06-A.

### Worked example B · A three-position corridor

**V09-B · Act, append, sample · 4 min.** Draw 1–2–3–goal with a wall left of 1. Goal entry gives +1 and terminates; every other reward is zero. Actions L/R; γ = 0.5. Each action head takes the dot product of its two weights with (1, position). At position 3 take the greedy action. Ask what enters the buffer. Supply:

| Position | Online (L,R) | Target (L,R) |
| --- | --- | --- |
| 1 | (0.20, 0.20) | (0.10, 0.20) |
| 2 | (0.30, 0.40) | (0.20, 0.30) |
| 3 | (0.40, 0.60) | (0.30, 0.40) |
| Goal encoded as 4 | — | (0.40, 0.50) |

Notes: store (3,R,+1,goal,done). Reveal the realized uniform draw of the two old rows and newest row below. The goal outputs allow the missing-mask check.

**V10-B · Construct three labels · 6 min.** Give row data first and reveal the last three columns after student work.

| State, action, reward, successor | Terminal? | DQN label | Recorded prediction | TD error |
| --- | --- | ---: | ---: | ---: |
| 2, L, 0, 1 | no | 0.10 | 0.30 | −0.20 |
| 2, R, 0, 3 | no | 0.20 | 0.40 | −0.20 |
| 3, R, +1, goal | yes | 1.00 | 0.60 | +0.40 |

Notes: mean half-squared loss = 0.04. Without the mask, the goal output would yield 1.25. Ask where the extra 0.25 came from.

**V11-B · Why did the prediction rise? · 6 min.** Supply the left-head step (0.10, 0.10) → (0.08, 0.06). Give the initial right-head weights (0, 0.2). Students compute the right-head step with α = 0.3 and the same three-row mean. Reveal
\[
(0,0.2)+\frac{0.3}{3}\,[{-0.2}(1,2)+0.4(1,3)]=(0.02,0.28).
\]
At position 2 the right prediction goes **0.40 → 0.58**, despite its negative error. Ask why before revealing the copy. Notes: the goal transition pulls on the same weights. At position 3 the online maximum goes 0.60 → 0.86. For row two a current-weight label would move 0.30 → 0.43. Its target-network label stays 0.20 through the step and becomes 0.43 after copying.

### Common close

**V12 · Settings for a DQN learner · 1 min.** Combine old P22’s tuning list and P14’s target update. Display “Data: exploration schedule, warm-up, buffer and minibatch size. Updates: step size, clipping, target-copy period C. Soft-update alternative: move the target weights a fraction τ toward the online weights each update.” Notes: this lecture uses hard copies and mean half-squared loss. A2 settings belong to its handout.

**V13 · Reconstruct the loop · 3 min.** Repeat V08 with four blanks: recorded action, source of bootstrap, optimizer destination, direction of copy. Answers: recorded action indexes online prediction; snapshot supplies nonterminal maximum; optimizer changes online weights; copy runs online → target.

**V14 · What changed in the update? · 3 min.** Ask “Which operation mixes correlated samples? Where does averaging reduce sampling variability? Which operation slows target motion? What can bias a bootstrap?” Notes: replay mixes experience; minibatch averaging can reduce gradient variance; delayed copies freeze a row’s plain-DQN label between copies; value estimates used to bootstrap can be inaccurate. Close by asking what happens when the learner takes the largest of several noisy estimates.

## 6.2 · Double estimators and experimental diagnosis

**D00 · Double estimators and experimental diagnosis · 1 min.** Visible session divider. Start with the figure on D01, then retrieve the loop.

**D01 · What return does the trained agent achieve? · 4 min.** Use the Alien panel from the top row of the original Double DQN Figure 3. Retain the axes, both agents, their horizontal lines and shaded bands. Label the curves “Predicted value during training” and the horizontal lines “Discounted return measured after training”. Ask students to compare the **right end** of each curve with its same-colour line. Notes: orange is DQN, blue is Double DQN. The lines average discounted returns from visited states when the corresponding trained agents were run. The curves summarize six seeds. DQN’s final predictions for this game exceed its measured return. Ask which operation in its target could favour optimistic errors. The coin calculation on D03 isolates one cause. [van Hasselt, Guez & Silver 2016, Fig. 3, PDF p. 5](https://people.engr.tamu.edu/guni/csce642/files/ddqn.pdf#page=5)

**D02 · Who chose the action inside the maximum? · 3 min.** Retrieve V08’s ordinary nonterminal target. Underline the maximum over the target network’s outputs. Ask students to point first to the operation that selects the largest entry, then to the number used to evaluate that choice. Answer: the same row of values performs both jobs. Notes: the environment action was chosen by the behaviour policy. On route A, recall the prediction of 6 and the return bound of 2; ask what evidence would establish bias across repeated estimates.

### Twenty-minute activity · From maximization bias to the Double DQN patch

**D03 · Two actions worth zero · 5 min.** Rebuild Control P46 as a calculation. Both true action values are zero. Each estimate independently equals +1 or −1 with equal probability. Ask for the maximum in the four equiprobable cases. Reveal the last column after the vote.

| First estimate | Second estimate | Maximum |
| ---: | ---: | ---: |
| −1 | −1 | −1 |
| −1 | +1 | +1 |
| +1 | −1 | +1 |
| +1 | +1 | +1 |

The mean of each action’s estimates is zero. The mean maximum is +0.5. Ask where the excess enters the preceding state’s target. Answer: the discounted bootstrap. Notes: the expected maximum is at least the maximum of the expectations, and equality is possible. Here the independent fair signs make the inequality strict.

**D04 · An optimistic estimate changes an earlier decision · 3 min.** Use Control P47’s copy of Sutton & Barto Figure 6.5, including its MDP and curve. At A, right terminates for 0. Left gives 0 and leads to B, where every action terminates with a noisy reward of mean −0.1. Vote on which action at A has higher expected return. Reveal the fraction of left choices early in learning. Notes: right is optimal. A noisy maximum at B can make left look attractive at A. With ε = 0.1 and two actions at A, the greedy-right policy’s ε-greedy counterpart still chooses left 5% of the time. [Sutton & Barto §6.7, Example 6.7](../../../sources/RLbook2020.pdf#page=156)

**D05 · Two estimates, two jobs · 4 min.** Reuse Control P48’s logic as one branch: “Q₁ and Q₂; subscript = which table. Flip a fair coin to choose which table to update. When updating Q₁, select the successor action with Q₁ and read its value from Q₂. Swap roles when updating Q₂.” Display the nonterminal bootstrap \(Q_2(s',\arg\max_a Q_1(s',a))\). Ask for the expected evaluation on D03 if the chosen action receives a fresh independent fair sign. Answer: zero conditional on either choice. Notes: the tabular algorithm can act ε-greedily on the sum of the tables. It shares a behaviour trajectory and bootstraps across tables. Independence belongs to the toy calculation. With true values (1,0) and independent fair-sign noise, selecting the inferior action one quarter of the time gives a mean independent evaluation of 0.75, while the ordinary maximum averages 1.25.

**Common equation panel on D06-A and D06-B.** Adapt old P16–18. Use the method names as row labels. Highlight the action index in the second line. For a nonterminal row display

\[
\begin{aligned}
\text{DQN}\quad &U_j=r_j+\gamma\max_a\hat q(s'_j,a,\mathbf w^-),\\
\text{Double DQN}\quad &U_j=r_j+\gamma\hat q\!\left(s'_j,\arg\max_a\hat q(s'_j,a,\mathbf w),\mathbf w^-\right).
\end{aligned}
\]

Display \(U_j=r_j\) at true termination for both methods. Notes: Double DQN uses the delayed copy already present in DQN. The online and target estimates can remain correlated.

**D06-A · Reopen the original two-row batch · 4 min.** Show V09-A’s **pre-update, pre-copy** snapshot. The older row has reward +1 and γ = 0.5. Online outputs (4,2) select left; target outputs (2,6) evaluate left at 2. Ask for both labels. Reveal **DQN 4, Double DQN 2**. The terminal row still gives −1. Have students identify selector and evaluator before they touch the arithmetic.

**D07-A · Write the patch and test the batch · 4 min.** Show the V09-A rows beside the V08 loop. Ask students to replace the label construction; reveal the implementation below after they write theirs. Check that the pre-copy labels are (2, −1). Retest the first row immediately after the V11-A copy; DQN and Double DQN both give 3.05. These are the disagreement, terminal and agreement checks.

**D06-B · Which network selects the successor action? · 4 min.** Use one new three-action batch for D06-B/D07-B. First read the two vectors of row one as separate estimates at the same successor; then label them online/target. Use γ = 0.9. With action numbers 1–3, the online network favours action 2 and the target favours action 3. Ask for both labels on row one. Reveal that row’s answers; reserve the remaining answers for D07-B.

| Reward, termination | Online successor outputs | Target successor outputs | DQN | Double DQN |
| --- | --- | --- | ---: | ---: |
| 0, continuing | (1.0, 2.0, 1.5) | (1.2, 1.4, 1.8) | 1.62 | 1.26 |
| +1, continuing | (0.5, 0.2, 0.1) | (0.9, 0.3, 0.4) | 1.81 | 1.81 |
| −1, terminal | (3, 1, 2) | (2, 5, 1) | −1 | −1 |

**D07-B · Write the patch and test the batch · 4 min.** Use D06-B’s three rows beside the V08 loop. Students replace the label construction and predict the result on the disagreement, agreement and terminal cases. Reveal the implementation and check (1.26, 1.81, −1).

**Implementation reveal and notes for either D07.** Start the label vector as a copy of the rewards. On nonterminal rows select the online maximizing action separately for each successor. Gather that column from the corresponding target-network row and add its discounted value to the label. Detach the labels. Compute the original loss at current states and recorded actions. Ask why the targets agree after a copy. With positive discount on a nonterminal row, they agree whenever the online choice is among the target network’s maximizing actions, including ties. Changing the selector leaves the data collection and optimizer steps intact.

### Fifteen-minute activity · Replay and fixed targets

**D08 · Design four learners · 4 min.** Draw a 2 × 2 grid for replay on/off and delayed targets on/off. In the proposed classroom comparison, replay on draws uniformly from the buffer; off takes the latest contiguous minibatch after warm-up. Target on uses the periodically copied snapshot; off uses a detached bootstrap from the current online weights. Ask which two cells isolate a change of target when replay is on. Answer: full DQN and replay only. Notes: match interactions, batch size, optimizer steps, architecture, exploration, evaluation schedule and tuning effort. Replay jointly changes sample ages, grouping and reuse. D09 reports the historical study under its own protocol.

**D09 · Does the same component help more in both games? · 6 min.** Recreate the primary paper’s table, keeping its column order. Heading: “Highest average evaluation episode score”. Work through Breakout and Seaquest. Keep the other three games visible. Students compare one switch while holding the other fixed. [Mnih et al. 2015, Extended Data Table 3, PDF p. 12](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf#page=12)

| Game | Replay + target | Replay only | Target only | Neither |
| --- | ---: | ---: | ---: | ---: |
| Breakout | 316.8 | 240.7 | 10.2 | 3.2 |
| Enduro | 1006.3 | 831.4 | 141.9 | 29.1 |
| River Raid | 7446.6 | 4102.8 | 2867.7 | 1453.0 |
| Seaquest | 2894.4 | 822.6 | 1003.0 | 275.8 |
| Space Invaders | 1088.9 | 826.3 | 373.2 | 302.0 |

Notes: with targets on, adding replay gains 306.6 in Breakout and 1891.4 in Seaquest. With replay on, adding targets gains 76.1 and 2071.8, respectively. The ranking reverses. Compare within each game; game scores use different scales.

**D10 · What claim can this table support? · 5 min.** Ask for a verdict on “Replay matters more than fixed targets.” Reveal the reporting rule: 10 million training frames per agent, three learning rates, validation every 250,000 training frames for 135,000 frames, highest average episode score reported. Ask what information is missing and what a replication should show. Notes: the table lacks per-seed spread. Reporting the best checkpoint after trying learning rates selects among noisy estimates. Show separate evaluation episodes at matched checkpoints, individual seeds and uncertainty, interaction and optimizer budgets, and comparable tuning effort. Ask for one observation that distinguishes a pair of explanations: track the label on a fixed probe transition across copies to test for a moving target, or measure row ages and sample counts to test for reuse. A return collapse has several possible causes.

### Common close

**D11 · Is the learner improving? · 6 min.** Display four questions and have students choose a measurement for each. “How does the greedy policy perform on fresh episodes?” → evaluation return. “What is the learner earning as it explores?” → training return. “How do its predictions change on the same states?” → mean maximum predicted value on a fixed probe set. “How well does it fit today’s labels?” → minibatch TD loss. Ask how to test overestimation directly. Notes: compare predictions to empirical discounted returns matched for states, policy, reward transformation and discount. Raw game score and clipped discounted return have different units. A fixed probe curve tracks prediction drift. Low training loss can accompany poor control. [Mnih et al. 2013, Fig. 2](https://arxiv.org/pdf/1312.5602)

**D12 · Choose a check for the suspected bug · 3 min.** Reveal the checks after students predict them. Terminal label varies with supplied successor values → run a fixed terminal-row test. Gradient flows through the bootstrap → inspect the label’s gradient path. Copy happens too early or never → inspect target weights across an ordinary learner step and a scheduled copy. Only recent data appear → inspect sampled indices over repeated draws. Notes: a correct numerical label can still carry a gradient path.

**D13 · From choosing an action to learning a policy · 3 min.** Adapt old P22–23. Exit questions: “What batch distinguishes DQN from Double DQN? How would you select an action when the network can no longer enumerate the choices?” Answers: use a nonterminal row where the online choice has a strictly smaller target value than the target maximum, plus a true terminal control. Week 7 introduces directly parameterized policies. Keep A2 release instructions asynchronous. Closing notes pointer: “The appendix links fitted and asynchronous Q-learning, prioritized replay, dueling networks, multi-step and distributional targets, noisy networks, and their combination in Rainbow.”

## Hidden appendix · 0 live minutes

Render H01–H03 hidden, each with clickable paper links. No assigned reading or assessment.

**H01 · Fitting Q from a batch and learning from parallel actors.** Old P6–8.

- Neural fitted Q-iteration recomputes bootstrap labels on a stored transition set and fits a neural regressor to them. [Riedmiller 2005](https://www.machine-learning-lab.com/_media/publications/rieecml05.pdf)
- Tree-based fitted Q-iteration fits successive regression targets on stored transition tuples using tree-based approximators. [Ernst, Geurts & Wehenkel 2005](https://www.jmlr.org/papers/v6/ernst05a.html)
- Asynchronous one-step and n-step Q-learning use parallel actor-learners to update shared parameters from their trajectories. [Mnih et al. 2016](https://arxiv.org/abs/1602.01783)

**H02 · Changing replay, outputs and targets.** Old P19–21 and P23.

- Prioritized replay samples transitions with different probabilities, often based on TD-error magnitude. [Schaul et al. 2016](https://arxiv.org/abs/1511.05952)
- Dueling networks combine a state-value stream and an action-advantage stream into action-value estimates. [Wang et al. 2016](https://arxiv.org/abs/1511.06581)
- Multi-step deep Q-learning accumulates rewards over several steps before bootstrapping. Rainbow incorporates this target. [Hessel et al. 2018](https://arxiv.org/abs/1710.02298)

**H03 · Distributions, exploration and combinations.**

- C51 approximates the distribution of discounted returns on a fixed categorical support. [Bellemare, Dabney & Munos 2017](https://arxiv.org/abs/1707.06887)
- Noisy networks learn the scale of parameter noise used for exploration. [Fortunato et al. 2018](https://arxiv.org/abs/1706.10295)
- Rainbow combines Double DQN, prioritized replay, dueling networks, multi-step targets, distributional learning and noisy networks, and evaluates component ablations. [Hessel et al. 2018](https://arxiv.org/abs/1710.02298)
