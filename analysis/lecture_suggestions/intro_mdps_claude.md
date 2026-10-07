# Introduction and MDPs: Claude's initial content suggestion (session 1.1 pilot)

**[Claude 2026-10-06]** Initial content suggestion, written independently of ChatGPT. This is a recommendation, not an accepted decision. It follows the compact shape in `analysis/phase7_brainstorming.md` Q8. Accepted scope, mastery and minutes come from `decisions/topic_decisions.yaml` (`formulate`, group `formulation`), as listed in `output/lectures/session_sources.md`.

- **Session:** 1.1 `formulate`, 38 min (range 35–45), after the 20-minute briefing (deck 0).
- **Mastery:** explain, analyze.
- **Worked activity:** formulate one running problem; distinguish reward, return, observation and state.
- **Exclusions:** no POMDP solver, no abstraction theorem ("defer abstraction theory").
- **Deck:** keep 1.1 and 1.2 in one "Introduction and MDPs" deck with a visible session divider (as proposed in Q2). 1.1 is the pilot; the short 1.2 sketch at the end is there only so the running example is judged across both sessions.

Old-slide numbers are **PPTX slide numbers** (hidden slides counted), checked by extracting slide text. Visual layout was not inspected.

## Key choices (to compare with ChatGPT's suggestion)

| # | Choice | Claude's suggestion |
| --- | --- | --- |
| C1 | Running problem | **Recycling robot**, Sutton & Barto Example 3.3 (§3.1, PDF p. 74). The noisy gridworld stays the visual example for VI/PI in 2.2, as in old deck 3. |
| C2 | Concept order | Why RL is different → interaction loop → formulate the robot → reward vs return → observation vs state → recap. Concepts are taught on the robot, not as a vocabulary list first. |
| C3 | Old Intro deck | Keep about 4 slides; cut the AI/ML review, coin examples, history and applications block (details below). |
| C4 | Observation vs state question | A new robot question ("which summary of the past should the robot keep?") instead of Silver's rat example. The rat slide stays as a backup. |
| C5 | Moved to 1.2 | Discounting, the episodic/continuing distinction, model p(s′, r ∣ s, a), learning vs planning, policy and value definitions. 1.1 ends on the cliffhanger "the robot never stops: what does *total* reward mean?" |

### Why the recycling robot (C1)

- **From the book**, with a finite MDP table already in it. Students can find it in the free textbook.
- **Formulation is a real design decision here.** The book itself stresses the choice of decision level (high-level search/wait/recharge, not motor voltages) and restricted action sets 𝒜(high) ≠ 𝒜(low). A gridworld arrives already formulated, so "formulate" becomes trivial.
- **Reward vs return appears without any mathematics.** Searching when the battery is low gives the best immediate reward but risks the −3 rescue.
- **Observation vs state has a natural version.** Remove the battery gauge, and the robot must summarize its history.
- **Continuing task.** It motivates discounting in 1.2 rather than announcing it.
- **Two states.** A fixed-policy evaluation in 2.1 ("derive one expectation backup and perform policy-evaluation sweeps") can be done by hand. The Bellman optimality equations for this robot are book Example 3.9 (§3.6).

**Cost.** The caveman MRP sequence in old deck 2 (slides 14–35, many native equations) is replaced. Its structure (watch a trajectory, compute G, then ask about the expectation) can be kept with the robot's numbers.

**Alternatives.**
- **Gridworld:** maximum reuse of decks 2–3; weak for observation vs state and for formulation.
- **Caveman:** the instructor's own example with full reuse; not from the book; an MRP first, with actions added late.

## Session 1.1 teaching sequence (38 min)

| Min | Segment | Content | Source |
| --- | --- | --- | --- |
| 4 | Why RL is different | No labels, only evaluative feedback; sequential, non-i.i.d. data the agent's own actions create; delayed consequences. One sentence contrasting supervised/unsupervised learning (students have ML). | Reuse Intro **51** as is. Optional 30-second picture: Intro **16**. |
| 6 | The interaction loop | S_t, A_t, then R_{t+1}, S_{t+1}. Say explicitly why the reward index is t+1: it is the consequence of (S_t, A_t). Agent–environment boundary: whatever the agent cannot change arbitrarily is environment (book §3.1). | Reuse Intro **42** (symbol-free agent/environment diagram; revised after reviewing ChatGPT's suggestion). Indices may be spoken or added in one line; MDP deck **3**, edited to S_t / R_{t+1}, moves to 1.2. |
| 10 | Formulate the running problem (worked activity) | Tell the robot story *without* the book's answer. Pairs, 3 min: when are decisions made, which actions, what does the robot know, what is the reward? Then reveal the book's formulation: 𝒮 = {high, low}, 𝒜(high) = {search, wait}, 𝒜(low) = {search, wait, recharge}, reward = cans collected, −3 for a rescue. Ask why recharge is not in 𝒜(high), and what is lost by choosing high-level actions instead of motor commands. | New slides (story, reveal). Book §3.1, Example 3.3. No probabilities or table yet (that is 1.2). |
| 9 | Reward vs return | Reward hypothesis (book §3.2 wording). One sampled "day" for two behaviours (table below). Diagnose question Q1. Rewards say *what* to achieve, not *how* (book §3.2): question Q2. | Reuse Intro **47** (trim to the hypothesis and "agree or disagree?"). New slide for the sampled day. |
| 7 | Observation vs state | Remove the battery gauge: the robot observes only O_t (cans found, whether it is at base, whether a rescue happened). Its state must be built from the history. Diagnose question Q3. Environment state vs agent state. One-line forward pointer: a single Atari frame does not show velocity (revisited for DQN, Week 6). | New question slide. Reuse MDP deck **5** (environment vs agent state). Backup: MDP deck **9** (Silver's rat). |
| 2 | Recap and bridge | The vocabulary on the robot: observation, state, action, reward, return, policy (= the two behaviours we compared). Formulation checklist for the project proposal (below). Cliffhanger for 1.2. | Reuse Intro **19** ("What do we need for RL?") with "return" added. Reword its policy line: a policy chooses actions *or action probabilities* (adopted from ChatGPT's review point). |

**Sampled day** (one possible outcome, same luck for the first two steps). Simplification for 1.1: a search period yields 2 cans and waiting yields 1. The book only requires r_search > r_wait; 1.2 replaces these with expected rewards.

| Step | "Always search" | "Search when high, recharge when low" |
| --- | --- | --- |
| 1 | high, search → +2, stays high | high, search → +2, stays high |
| 2 | high, search → +2, drops to low | high, search → +2, drops to low |
| 3 | low, search → battery depleted, rescued: −3, back to high | low, recharge → 0, back to high |
| 4 | high, search → +2 | high, search → +2 |
| Total | 3 | 6 |

### Diagnose questions with intended answers

These give the session its analyze-level component.

- **Q1.** At step 3 searching earns +2 now and recharging earns 0. Which is better? Does the table prove the second behaviour is better?
  *Intended:* the reward alone cannot decide; what matters is what follows (the return). The table does not prove it. It shows one sampled day, and a low-battery search might have succeeded and earned +2. A fair comparison needs the *expected* return, which depends on the depletion probability. That is the value function in 1.2.
- **Q2.** A designer of a cleaning robot rewards "amount of dirt collected". What might the robot learn? (This is the AIMA vacuum performance-measure example, familiar from COMP341.)
  *Intended:* dump dirt and collect it again. Reward the outcome you want, not a proxy for how to achieve it. Book §3.2 makes the same point with chess subgoals.
- **Q3.** Without a battery gauge, which summary of the past should the robot keep to decide whether to search? (a) its latest observation; (b) steps since the last recharge or rescue; (c) *search periods* since the last recharge or rescue; (d) the entire history.
  *Intended:*
  - (a) is not enough.
  - (d) always works but grows without bound.
  - (b) loses information, because waiting never drains the battery.
  - (c) works under this model: only searches can lower the charge, and recharge or rescue resets it to high. The probability that the battery is still high therefore depends only on that count.

  Lesson: a state is a summary of the history that keeps what matters for the future. Keep this informal; the formal Markov property is 1.2 and abstraction theory is excluded.

**Formulation checklist** (one slide; it prepares the Week 4 project proposal: "tentative MDP/state-action-reward/horizon"):
1. When are decisions made?
2. What are the actions?
3. What is observed, and what state will the agent keep?
4. What is the reward, and does it describe the goal or a guess at how to reach it?
5. When does it end? (Answered in 1.2.)

## Main teaching difficulties

1. **Reward vs return.** Students treat each reward as the goal of each step, or put the solution into the reward. Q1 and Q2 address both.
2. **Observation vs state.** Students equate the state with what the sensors show, or with the full world state. Q3 and MDP deck slide 5 address both.
3. **The R_{t+1} index.** The old decks use R_t (see the notation issues below). Explain it once, on the loop slide.

## Changes and tradeoffs vs the old material

**Old `1 - Introduction.pptx`** (62 slides, 45 visible): most of it is replaced.
- **Cut:**
  - AI/ML brainstorm and coin examples (2–15): covered by the prerequisites; one contrast sentence remains.
  - Agents, environment and rationality (35–44): COMP341 review (deck 0 slide 7 lists COMP341 as expected background).
  - History (26–31): optional pointer to book §1.7.
- **Applications and videos (16–25, 32–34):** keep at most one montage slide (16 or 25, about 1 min), at the instructor's choice.
- **Intro 44 "Problem types":** do not reuse in 1.1. Its "Episodic vs Sequential" is the Russell & Norvig sense, which clashes with the book's "episodic vs continuing tasks" taught in 1.2. Rename the line if the slide is kept anywhere.
- **Intro 52 (formulation brainstorming list):** could serve as optional out-of-class practice with the checklist. It is not graded and adds no required workload.

**Old `2 - Markov Decision Processes.pptx`:**
- **Into 1.1:** slides 5 and 9 (backup). Slide 3, edited, moves to 1.2.
- **Moved to 1.2:** the rest; see the sketch below.

**Time.** The sequence sums to 38 min. The risk is the pair activity (segment 3). If it overruns:
1. Cut the montage and the Atari line.
2. Move Q2 to the opening of 1.2.

The slot then still fits the configured buffer (20-minute briefing + 38 min ≤ 59.5 usable minutes). This is a pacing estimate, not tested in class.

**No change** to scope, mastery, minutes, assessments or student workload. There is no required reading (readings are excluded this semester); book sections are cited only as optional pointers.

## Notation issues

**Update 2026-10-06:** at the instructor's request these are now in `course/notation_guide.md`: N1 adds O_t to the MDP table; N2 is open item O10; N3 is open item O11; N4 is listed under O9.


- **N1 (needed by 1.2; optional in 1.1 if observations stay verbal).** The guide has no symbol for observations. Proposal: add O_t (observation at time t), following book §17.3. 1.1 needs only O_t; the history and state-update symbols are not needed under this plan.
- **N2 (needed for 1.2 if old slides are reused).** History H_t is not in the guide.
  - Book §17.3: H_t = A_0, O_1, …, A_{t−1}, O_t (rewards are treated as part of observations).
  - Old MDP deck slide 4: H_t = O_1, A_1, R_1, …, O_t.
  - This needs a choice before 1.2.
- **N3 (1.2/2.1).** The book's robot uses α and β as transition probabilities, which clashes with α (step size) and β (O6). Proposal: write numeric probabilities on slides and mention the book's symbols only when pointing to Example 3.3. Its table also uses r(s, a, s′), which is not in the guide (the guide has r(s, a) and p(s′, r ∣ s, a)).
- **N4 (reuse edit, under O9).** The old decks index the reward as R_t (MDP deck 3; Intro 54) and write G_t = r_t + γ r_{t+1} + … (MDP deck 22, 24). Reused slides must be converted to R_{t+1} and G_t = R_{t+1} + γR_{t+2} + …. MDP deck 11 uses T(s, a, s′) and R(s, a), which become p(s′ ∣ s, a) and r(s, a).

## Short 1.2 sketch (continuity only, not the pilot)

The same robot and the same sampled day continue into 1.2:
- Markov property (MDP deck 4, 7).
- Model p(s′, r ∣ s, a) with numbers (new table from Example 3.3; MDP deck 11 edited).
- Continuing task → discounting (MDP deck 21, 23; deck 22 with index fix). Recompute the sampled day with γ, then ask what the *expected* return is.
- The two behaviours become policies π.
- Define v_π and q_π (MDP deck 59, 62, notation checked).
- MDP definition (MDP deck 36, edited).
- Learning vs planning (MDP deck 12).

Gridworld slides 37–48 move to 2.2 or serve as a short "common environment" preview.

## Self-check against the Q8 criteria (Claude, 2026-10-06)

| Criterion | Assessment |
| --- | --- |
| Mastery (explain/analyze) | Q1–Q3 are diagnose questions with intended answers. |
| Concept before named method | No algorithms. |
| Continuity | Robot carries 1.1 → 1.2 → 2.1. Gridworld is kept for 2.2. Weeks 3–4 keep their book examples (old decks 4–5). |
| Reuse before rewrite | 5 old slides reused or edited (Intro 51, 42, 47, 19; MDP deck 5), 1 backup. New slides only for the running example. Caveman sequence replaced: a real cost, stated above. |
| Fits minutes | 38/38, with a fallback. |
| Prepares assessment | Checklist feeds the Week 4 project proposal. A1 (Week 4) uses a supplied MDP and builds on 1.2–4.2, not 1.1 directly. MT1 can ask Q1/Q3-style scenario questions. |
| Targets the known difficulty | Reward vs return; observation vs state. |
