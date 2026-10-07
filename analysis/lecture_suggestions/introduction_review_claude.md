# Introduction and MDPs: Claude's review of ChatGPT's suggestion

**[Claude 2026-10-06]** Mutual-review iteration 1. Read-only review of `introduction_chatgpt.md`, at the instructor's request. Compared against Claude's own suggestion `intro_mdps_claude.md`. Recommendations only. Following Q4 and Q8, it lists consequential findings with a fix for each, then one combined list of differences for the instructor.

## Verified

- Example 4.1 is on book PDF p. 98.
- Grid geometry. From cell 5, `up, left` gives return −2; `right, right, down, down` (5→6→7→11→terminal) gives −4.
- Cells 5 and 6 have the same "adjacent walls" observation (none). Moving left from them reaches cell 4 (left boundary wall) or cell 5 (no wall), so the observation alone does not predict the next observation.
- Time arithmetic: 70 × 0.85 − 20 = 39.5.
- Intro PDF pages cited (5, 7, 26–28, 31, 35, 37–39) match the cited slide titles. The Intro PDF is an older 40-page export, not the 45 visible PPTX slides, as ChatGPT notes. MDP deck PPTX 37–40 ↔ PDF 33–36 matches.
- Intro PPTX slide 42's diagram (agent "?", sensors/actuators, percepts/actions/rewards) is a grouped shape with no symbols on it, so reusing it raises no reward-index notation issue.

## Findings

**F1. The running example is already formulated, so the worked activity becomes identification (consequential).** Example 4.1 arrives with states, actions, dynamics and reward fixed by the book. The accepted activity is "*formulate* one running problem", and the Week 4 project proposal needs exactly that skill: choosing a state, actions, reward and horizon. Block 2 ("identify the agent, actions, information received and reward") exercises recognition rather than design.

*Fix if the grid is kept:* add one design choice students must make. The natural one is reward design. Replace "−1 per step" with "+1 on reaching the goal, no discount", then ask which routes are now best. *Intended answer:* every route that eventually terminates earns +1, so the agent has no reason to hurry. The −1 per step is what encodes "fast". This is a genuine formulation decision with an analyze-level answer, and it takes about 3 minutes.

**F2. The reward/return check has no conflict between immediate reward and return (moderate).** Every transition gives −1, so immediate reward never favours the worse route. The check shows that totals differ, but not that maximizing immediate reward can mislead, which is the misconception the plan targets. Students are likely to answer "obviously the shorter route" without engaging the reward/return distinction.

*Fix:* use the goal-reward question from F1 as the second half of the check, or add a labelled variant with a tempting intermediate reward. The robot in Claude's suggestion has this conflict built in: searching on a low battery pays +2 now but risks −3.

**F3. "Policy, model and learning" (6 min) pre-empts 1.2 (moderate).** 1.2's accepted worked activity is "define a policy/model/value on the running MDP". Introducing the model and value in 1.1 either duplicates 1.2 or leaves it partly done, and it squeezes the closing check to 4 min.

*Fix:*
- Keep one sentence on planning (rules known) vs learning (rules unknown) in 1.1 for L01.
- Move the model and value material to 1.2.
- Give the minutes to F1's formulation choice.

**F4. Continuity across weeks is the strongest argument for the grid; the gap is discounting (for the instructor).**
- **Strength:** Example 4.1 is the book's own policy-evaluation example (random-policy values in Figure 4.1). Cliff walking and windy gridworld (old deck 5) are labelled grid variants. This continuity into Weeks 2–4 is better than the robot's, which reaches only 2.1.
- **Gap:** the task is episodic and undiscounted. 1.2's scope ("finite episodic/discounted MDPs") has to introduce discounting with no reason for it in the running example. 1.2 would need a labelled continuing or discounted variant.
- **Tradeoff:** the 14-state grid makes hand-worked sweeps in 2.1 longer than a 2-state MDP, although the book's figure offsets this.

**F5. Wording of the observation/state check (minor).** "Regardless of earlier location information" is hard to parse aloud.

*Fix:* "You see only 'no walls nearby' and choose *left*. Can you predict what you will see next?" Optional extension, still inside scope: the history can recover the cell, for example after moving left until a wall appears. This makes "state built from history" concrete without history notation.

**F6. Reuse points I adopt in my own suggestion.** Two of ChatGPT's choices are better than mine:
- **Policy wording:** policies may choose action *probabilities*. My suggestion reused Intro 19, whose "Policy: map states to actions" has the same flaw.
- **Interaction diagram:** Intro 42's diagram has no symbols, which suits a verbal 1.1 better than editing MDP deck slide 3. Under that plan, my notation item N1 (`O_t`) can wait until 1.2, as ChatGPT says.

## Combined differences for the instructor

| # | Choice | ChatGPT | Claude | Status |
| --- | --- | --- | --- | --- |
| D1 | Running example | Book Example 4.1 (4×4 episodic grid) | Book Example 3.3 (recycling robot) | **Disagree; instructor decides.** Deciding question: will Week 2 DP move from the old 3×4 stochastic grid to Example 4.1? If yes, the grid's continuity wins; apply the F1/F2 fixes and a discounting variant in 1.2. If the old DP grid stays, Example 4.1 adds a third grid, and the robot carries Week 1–2.1 better (formulation, reward conflict, continuing task). |
| D2 | Model, planning vs learning | Taught in 1.1 (6 min) | Taught in 1.2 | Claude recommends: one-sentence contrast in 1.1, the rest in 1.2 (F3). |
| D3 | Interaction diagram | Intro 42 (symbol-free) | MDP deck 3 (edited to S_t, R_{t+1}) | **Agree on Intro 42** for 1.1; MDP deck 3, edited, when symbols arrive in 1.2. |
| D4 | Formulation activity | Identify components of a given task | Pairs formulate the robot, then reveal the book's version | Claude recommends at least one real design choice either way (F1). |
| D5 | Other reuse | Intro 6, 8, 37–39, 47, 49–51; MDP deck 37–40 later | Intro 51, 47, 19; MDP deck 3, 5; rat (MDP deck 9) as backup | Largely compatible. Both cut the AI/ML brainstorm, history and applications tour, and both drop "episodic vs sequential". |
| D6 | Policy wording | Includes stochastic policies | (Intro 19 deterministic) | **Agree with ChatGPT.** |
| D7 | Notation | No symbols needed in a verbal 1.1 | N1 `O_t` needed in 1.1 | **Agree with ChatGPT for 1.1** under D3; N1–N4 are still needed by 1.2. |

There are no correctness errors in ChatGPT's mathematics or source references.
