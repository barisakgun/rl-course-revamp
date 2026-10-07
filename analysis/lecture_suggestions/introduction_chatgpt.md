# Introduction and MDPs: initial content suggestion

**ChatGPT · 2026-10-06 · independent proposal, awaiting mutual review.** Topic-level suggestion with session 1.1 as the pilot. This proposes teaching choices, not a new lecture plan or a parallel deck source. Claude's initial content suggestion was not consulted.

Use the accepted `formulate` and `mdp_values` entries in [topic decisions](../../decisions/topic_decisions.yaml) and their [session index](../../output/lectures/session_sources.md). No scope, mastery or assessment change is proposed.

## Main choices

1. **Use the book's small episodic gridworld as the running example.** Sutton & Barto, Example 4.1, printed p. 76 / PDF p. 98: a 4×4 grid, four deterministic moves, boundary attempts leave the position unchanged, −1 per transition until termination. The two shaded corners represent the same terminal state. Introduce only the task in 1.1; do not import the surrounding dynamic-programming mathematics yet.
2. **Keep the instructor's interaction diagram and question-led style.** Move quickly from a concrete decision to agent, environment, action, observation and reward. Introduce policy as the agent's behaviour, then ask what information that behaviour needs.
3. **Give reward/return and observation/state actual examples.** Replace part of the broad introduction with two short reasoning checks on the same grid. These are the main new teaching content proposed below.
4. **Keep one Introduction and MDPs deck with an explicit 1.1/1.2 break for now.** This is a proposed split, not acceptance of the full 13-deck scheme. Session 1.2 formalizes what students have already seen.

The book grid supplies short terminating trajectories and a direct bridge to policy evaluation. Its cost is replacing the old 3×4 grid and reward conventions. Keeping the old grid is the main alternative if reuse takes priority.

## Session 1.1: suggested progression

These estimates include the questions and responses within each block, not just presentation time.

| Block | Min | Teaching choice |
| --- | ---: | --- |
| A sequential decision | 4 | Open with the grid task and ask what the agent should do. Use the existing decision-making prompt. Explain that the course concerns learning behaviour from experience; distinguish a reward from a label telling the agent the correct move. |
| Formulating the interaction | 6 | Use the existing agent–environment diagram. Have students identify the agent, actions, information received and reward in the grid. Describe a policy as a rule for choosing actions, potentially randomized. |
| Reward and return | 8 | Compare two completed routes with identical immediate rewards but different totals. Separate immediate feedback, the return on one trajectory, and the expected return under a policy. Introduce value verbally; defer value calculations to 1.2. |
| Observation and sufficient state | 10 | First give the agent its cell identity. Then remove that information and show only adjacent walls. Use the diagnostic below to explain why a convenient observation need not be a Markov state. No history equations, belief-state machinery or abstraction theorem. |
| Policy, model and learning | 6 | Revisit the diagram: policy chooses, model predicts, value evaluates longer-term outcomes. Contrast having the transition/reward rules available for planning with learning from experience when they are unknown. Mention that actions influence subsequent experience, without opening the full RL taxonomy. |
| Formulation check and bridge | 4 | Ask students to explain what changed when cell identity was hidden, and whether supplying a map supplies a policy. Close with 1.2's task: make the model, returns and values precise. |
| **Total** | **38** | |

**Reward/return check.** From cell 5, `up, left` terminates in two steps; `right, right, down, down` terminates in four. Every transition, including the final one, gives −1: returns are −2 and −4. Ask: “Does the identical first reward make these routes equally good?” No: their later consequences differ. These are realized route totals, not value estimates. No rewards accrue after termination.

**Observation/state check (adaptation of the book example).** Cells 5 and 6 have identical adjacent-wall observations. Moving left reaches cell 4 or cell 5: one has a left boundary wall and the other does not. Is the wall observation alone sufficient to predict the next observation given the action, regardless of earlier location information? No. Cell identity is sufficient under this task model; the compressed observation is not. No POMDP solution is needed.

## Existing material to reuse or adapt

Numbers below identify the inspected files explicitly. PPTX positions include hidden slides; the PDF and PPTX are not interchangeable versions.

| Material | Proposal |
| --- | --- |
| Introduction PPTX slides **6, 8**; PDF pp. **5, 7** | Keep the decision-making question and interaction-based definition, shortened around the running example. |
| Introduction PPTX slide **42**, “Agents and RL”; PDF p. **31** | Reuse the interaction diagram. Say policies choose actions or action probabilities; avoid making deterministic state-to-action mapping the only possible policy. |
| Introduction PPTX slides **37–39**; PDF pp. **26–28** | Reuse the motivation for choosing relevant information. Add the concrete sufficiency check above rather than implying any abstraction is a Markov state. |
| Introduction PPTX slides **47, 49–51**; PDF pp. **35, 37–39** | Retain the immediate/long-term distinction and action-dependent experience. Add return explicitly. Shorten the reward-hypothesis discussion and avoid the categorical “no teacher” slogan as a definition of every RL setting. |
| MDP PPTX slides **37–40**; PDF pp. **33–36** | Reuse the formulation questions later, but replace the old grid/reward diagram if choosing Example 4.1. Its stochastic 3×4 world is a different model. |

Compress or leave out the broad AI/ML brainstorm, extended history, company list and multi-example application tour in this pilot. They make room for the worked formulation; they are not being moved to required homework or video. Keep the familiar Pac-Man picture/question as an alternative brief motivation if desired, not a second full formulation exercise. Do not reuse the “episodic vs sequential” row as a distinction: the proposed episodic task itself involves sequential decisions.

## Continuity, timing and remaining review choices

**1.2:** retain the same grid while defining the MDP, calculating discounted/undiscounted returns, and distinguishing policy, model and state/action value. A random policy supplies uncertainty in trajectories even with deterministic movement. A stochastic-transition illustration can use the old grid-actions material, clearly labelled as a variant. Bellman derivation stays in Week 2. This is a boundary recommendation, not a second detailed session plan.

Reuse the grid for Week 2 backups and later sampled trajectories, with explicitly labelled variants where needed (e.g. cliff-style control). This prepares A1's small-MDP work without fixing its unreleased environment.

**Time check:** 70 × 0.85 − 20 = 39.5 available content minutes; the 38-minute proposal leaves 1.5 minutes within that allowance, in addition to the reserved 10.5-minute general buffer. Arithmetic fits the accepted allocation. The main pacing risk is the observation/state discussion; protect its concrete check and shorten repeated definitions if necessary. No new required reading, video or student deliverable is proposed.

**For mutual review:** prioritize the running example, motivation/formulation balance and clarity of the checks. Observation/history symbols are unnecessary for this verbal pilot; resolve them only if needed. Slide wording and layout follow instructor comments.

## Inspected sources

- [Current Introduction PDF](../../sources/current_course/1%20-%20Introduction.pdf) and [PPTX](../../sources/current_course/1%20-%20Introduction.pptx): complete PDF text and PPTX text/order/hidden flags; interaction and Pac-Man diagrams viewed.
- [Current MDP PDF](../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pdf) and [PPTX](../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx): early formulation text and gridworld material; grid/action diagrams viewed.
- [Sutton & Barto](../../sources/RLbook2020.pdf): §§1.1–1.3, §§3.1–3.3, and Example 4.1 (printed p. 76 / PDF p. 98, visually checked). Example 3.3 informed the alternative considered above. These are instructor references, not assigned readings.

No counterpart introductory suggestion is currently present in the project. Mutual review is pending; this file does not claim that review or instructor acceptance.
