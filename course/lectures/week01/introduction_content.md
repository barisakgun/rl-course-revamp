# Introduction to reinforcement learning — shared content proposal

**Shared:** instructor, ChatGPT and Claude. Created by ChatGPT, 2026-10-06.
**Status: FROZEN at instructor handoff (2026-10-07).** This is the record of the content agreed before the instructor took over the PPTX; do not edit it further. The maintained artifacts are now `introduction_claude.pptx` (teaching authority, SHA-256 `53c87088…`) and its source `introduction_claude.yaml`. The handed-off deck differs from this proposal by the instructor's edits recorded in `decisions/lectures/introduction.md` A13–A19 (opening slides and videos, robot slides with prompts and figure, no reward-table slide, merged observation/state, live summary, 42.5 minutes).
**Scope:** session 1.1, `formulate`, only. Eleven live slides across ten teaching segments (I09a/I09b share four minutes), plus one appendix slide; 38 teaching minutes after the separate course briefing. Session 1.2 is not drafted here.
**Decisions:** [introduction](../../../decisions/lectures/introduction.md). **Discussion and revisions:** [shared review](../../../analysis/lecture_suggestions/introduction_review.md).

Only **Display** text and explicitly requested visuals belong on slides. Notes, source instructions, timing and decision status belong in the content source/speaker notes, not on the student-facing canvas. No mathematical notation in 1.1; ordinary numerical rewards in the example are retained as a proposal under O3. Stable IDs below identify slides across reviews and rendering. Rendering: only I04 copies native old-slide content (the slide 42 diagram); slides marked "adapt old PPTX N" are new template slides with the displayed text below, and the old slide number is provenance (Claude, 2026-10-06).

## I01 — Introduction to reinforcement learning

**Time:** 1 minute. **Build:** adapt the definition from old Introduction PPTX slide 8; use the following short wording.

**Display**

> Introduction to reinforcement learning
>
> Learning to make decisions from experience

**Note:** The course briefing is already complete. Introduce the question of how an agent can improve its choices using experience and feedback on their consequences. Do not repeat the syllabus or prerequisite overview.

**Sources:** current Introduction PPTX 8; CS234 introduction, PDF p. 4.

## I02 — Why reinforcement learning?

**Time:** 4 minutes total. **Build:** one visual overview with four clearly separated examples; no algorithms, equations, performance charts or required video playback.

**Display — example choices follow A9/A11**

| Example | Caption |
| --- | --- |
| Go — AlphaGo, 2016 | Improving play through self-play |
| Fusion — DeepMind and EPFL, 2022 | Learning to control plasma shape |
| Robot movement — ANYmal, 2019 | Learning movement in simulation, then using it on a real robot |
| Language — ChatGPT, 2022 | Improving responses with feedback learned from human comparisons |

**Visual/source directions:**

- **Go:** a Go-board or match image from the primary AlphaGo source below. Do not copy CS234 p. 7's mathematical search diagram. Distinguish the 2016 AlphaGo example from later AlphaGo Zero.
- **Fusion:** a plasma-shape or TCV photograph, with attribution to DeepMind/EPFL as appropriate. CS234 p. 8 is the inspected visual reference; use its original credited source below.
- **Robotics:** a photograph or demonstration still of ANYmal from Hwangbo and colleagues' 2019 work. Do not label CS224R's Unitree photograph as ANYmal. The renderer must select and verify the actual media from the cited work.
- **LLM:** a small response-comparison illustration, clearly illustrative, or a historical ChatGPT image from the 2022 announcement. The point is feedback about response quality; the chatbot state/observation example stays in 1.2.
- Put a short author/organization and year credit by each example; retain full links in speaker notes. If optional motion is used later, it must fit these four minutes and have a still-image fallback.

**Notes:** Each example gets one point, not its own technical explanation. AlphaGo combined human-game training, reinforcement learning and search. Fusion refers to plasma control, not a claim that RL solved energy production. ANYmal's controller was trained in simulation and transferred to hardware. The historical ChatGPT pipeline included supervised training as well as RL using a learned reward model; this is not a claim that every user click immediately trains the deployed model. No current-best or universal adoption claims.

**Primary sources, checked 2026-10-06:**

- [DeepMind, AlphaGo](https://deepmind.google/research/alphago/): self-play, combined methods, March 2016 Lee Sedol match.
- [DeepMind, plasma control, 16 February 2022](https://deepmind.google/blog/accelerating-fusion-science-through-learned-plasma-control/): TCV work with EPFL.
- [Hwangbo et al., 2019, Learning agile and dynamic motor skills for legged robots](https://arxiv.org/abs/1901.08652): ANYmal simulation-to-real locomotion.
- [OpenAI, Introducing ChatGPT, 30 November 2022](https://openai.com/index/chatgpt/): supervised fine-tuning, human comparisons, reward modelling and RL.

The earlier alternative suggestions and their sources remain in the shared review for context.

## I03 — How does RL differ from other learning methods?

**Time:** 3 minutes. **Build:** adapt old Introduction PPTX 51 and CS224R PDF p. 8; replace their text with the following symbol-free comparison.

**Display**

| Learning setting | Typical learning signal |
| --- | --- |
| Supervised learning | Examples of the desired output |
| Unsupervised learning | Structure in the data, without target labels |
| Reinforcement learning | Rewards from the consequences of actions |

> In RL, actions affect later experience. A reward need not tell us which action was best.

**Notes:** This is a short contrast, not a taxonomy lecture. Rewards can arrive immediately; consequences can also appear much later. Learning methods can be combined, as the motivation examples illustrate. Do not restore “no teacher/labels” or assert that all supervised data must be independent. Describe RL's feedback and decision problem, rather than defining it solely by absence of labels.

**Sources:** current Introduction PPTX 51; CS224R introduction p. 8; CS234 introduction pp. 16–17; book §1.1.

## I04 — Agent and environment

**Time:** 3 minutes. **Build:** reuse the **native interaction diagram from `1 - Introduction.pptx`, slide 42**. Preserve its agent, environment, sensors/actuators and arrow structure.

**Display**

> Agent and environment
>
> The agent chooses an action.
> The environment responds with an observation and a reward.
>
> A policy describes how the agent chooses actions.

**Reuse edits:** Copy the diagram, not the entire original slide unchanged. Remove the original body text, including its Greek policy symbol and deterministic-only “mapping between states and actions” wording. Relabel “Percepts” as “Observations” if needed for consistency. The question mark inside the agent is part of the original diagram and may stay. Add no time indices or formula labels.

**Note:** A policy may choose an action or assign probabilities to actions; no policy notation or probability calculation here. The agent–environment boundary depends on what decisions we choose to study. Use the diagram as a bridge to the robot, not a second full formulation exercise.

**Source:** current Introduction PPTX 42, including text inspected directly from the PPTX.

## I05 — Recycling robot: live discussion canvas

**Time:** 9 minutes, including student contributions. **Build:** an empty slide for the instructor's gradual reveal.

**Display:** Leave the working canvas blank. No prewritten story, question list, robot state table or animated answer sequence.

**Instructor notes — consistency reference, not a reveal script:**

- The task is collecting empty cans over time. The agent makes high-level decisions about searching, waiting and recharging; motor control is outside this simple decision model.
- In the book's formulation the observed battery charge is high or low. At high charge, search and wait are available; at low charge, recharge is also available. Omitting high-charge recharge is a modelling choice, not a physical impossibility.
- Searching can lower charge. A search starting at high charge completes without rescue and can leave high or low charge. A successful search starting at low charge leaves it low; depletion causes rescue and returns it to high. Waiting leaves charge unchanged; recharging returns it to high.
- For the proposed arithmetic example: successful search gives 2 reward units; waiting gives 1; recharge gives 0; a depleted search gives −3 on that transition and collects no cans. The 2 and 1 are teaching simplifications, not constants specified by the book. No transition probabilities are introduced.
- The task continues after the four-step excerpt shown later. The formulation aims at collecting cans while accounting for depletion/rescue, not simply avoiding all risk.
- Give students room to suggest the information, actions and feedback. A different defensible formulation can be discussed before naming the book's simplified model. Do not impose a fixed pair exercise.

**Source:** Sutton & Barto, Example 3.3, printed pp. 52–53 / PDF pp. 74–75. Content details remain proposals under O3–O5; A3 fixes the blank-canvas format.

## I06 — Reward and return

**Time:** 3 minutes. **Build:** adapt the immediate/future distinction in old Introduction PPTX 49–50; use new wording, without value formulas or the cost-to-go aside.

**Display**

> **Reward:** feedback from one step.
>
> **Return:** the rewards still to come, added up (later ones may count less).
>
> Recharging earns nothing immediately, but changes what can happen next.

**Notes:** For this course's upcoming episodic/discounted setting, return combines future rewards by adding them, possibly discounting later ones. Leave the precise objective and calculations to 1.2. Contrast high-charge search and waiting if useful: search earns more immediately under our numbers, but can leave less charge for later. This exposes a future consequence; it does not establish that waiting is better. Do not claim low-charge search pays 2 before a separate later rescue penalty.

**Sources:** current Introduction PPTX 49–50; book §§3.2–3.3.

## I07 — First four steps: cumulative reward so far

**Time:** 5 minutes including the question. **Build:** one readable comparison table; these are two possible traces, not expected values.

**Layout fallback:** If cells are too dense at a readable classroom size, shorten repeated prose while retaining labels: “High: search; reward 2; stays high” and “Low: search; reward −3; rescued to high”. Keep the charge before acting, action, reward and stated outcome distinguishable. Do not replace “reward 2” with an unexplained bare number. Apply any shortened display wording here before rendering and retain both totals, the question and the continuing-task caption.

**Display**

| Step | Always search | Search when high; recharge when low |
| --- | --- | --- |
| 1 | High charge: search, reward 2; stays high | High charge: search, reward 2; stays high |
| 2 | High charge: search, reward 2; becomes low | High charge: search, reward 2; becomes low |
| 3 | Low charge: search, reward −3; rescued to high | Low charge: recharge, reward 0; becomes high |
| 4 | High charge: search, reward 2 | High charge: search, reward 2 |
| **Reward accumulated so far** | **3** | **6** |

> Does this one outcome establish which behaviour is better?

Small caption: “Illustrative rewards and outcomes. The robot keeps working after step 4.”

**Notes / intended answer:** No. Low-charge search could instead succeed and give 2. The action's expected immediate reward already depends on its chance of failure; longer-term comparison also depends on what follows and the return objective. The table shows realized partial sums, not complete continuing returns or policy values. The initial outcomes match to make the behavioural difference easy to see, not because separate real runs necessarily have the same luck. No arithmetic beyond these sums is needed.

**Source:** an illustrative trace consistent with book Example 3.3; reward and trace corrections consolidated from the mutual reviews and O3–O4.

## I08 — Learning from experience

**Time:** 4 minutes. **Build:** new short slide on the same robot; no exploration algorithm or second application example.

**Display**

> If the robot is not given the consequences of its actions, how could it learn them?
>
> On a trial, it observes what happened for the action it chose—not directly what the alternatives would have produced.
>
> **Exploration:** trying actions to learn more.
> **Exploitation:** using what it has learned to obtain reward.

**Notes:** The battery gauge is still visible here. The uncertainty under discussion is about action consequences, not hidden battery charge. Students can suggest trying actions and comparing repeated experience; acknowledge that experiments can cost reward. Do not claim one failed trial settles a policy comparison or that the unchosen action can never be learned about later.

**Natural planning contrast, spoken only if it fits:** With a usable model of the consequences, the robot can compute ahead: planning. It can also learn from experience, including learning a model and then planning with it. Model knowledge does not make stochastic outcomes certain. Use this answer to the opening question; no standalone learning/planning slide is required.

**Sources:** CS234 introduction p. 17; Silver introduction pp. 37–42; current Introduction PPTX 51. A5 and A8 govern this short treatment.

## I09 — Observation and state

**Time:** 4 minutes combined, including discussion and both slides. **Build:** two consecutive slides, I09a (question) and I09b (definitions), rather than a click animation; do not copy the mathematical history/state slides from the old MDP deck.

**I09a — Display**

> The battery gauge is hidden. You have just collected two cans.
>
> Is the battery high or low?
> What earlier events could help you decide what to do next?

**I09b, shown after the discussion:**

> **Observation:** what the agent receives now.
> **State:** a description used to predict consequences and choose actions.
>
> A useful state must retain the information that matters for what happens next.

**Notes / intended answer:** Two cans alone do not identify charge; a successful search can end at high or low charge. Recent recharging, searching and rescue events can inform what the agent knows, without necessarily identifying the true charge. For this question consider only choosing between search and wait. Do not show an action-availability indicator, a base-location indicator or another cue that reveals charge. Do not ask students to prove that a search count is sufficient. Under the original simplified model, known high/low charge is sufficient for predicting the distribution of consequences; hiding the gauge changes the available information. Uncertainty in an outcome is not itself evidence of a bad state representation.

**Sources:** book Example 3.3, adapted sensor-information question; CS234 pp. 35–38; Silver pp. 18–24. The CS224R chatbot example is reserved for 1.2 under A10.

## I10 — Formulating a decision problem

**Time:** 2 minutes. **Build:** adapt old Introduction PPTX 19 as a short closing check, using words only.

**Display**

> For the recycling robot:
>
> - What decisions does it make, and what feedback does it receive?
> - Why might the latest observation be insufficient?
> - Why doesn't one good outcome settle which behaviour to use?
>
> Next: make the model, return objective and policy precise.

**Notes:** Use brief student answers rather than another vocabulary lecture. Actions are search/wait/recharge under the chosen model; rewards evaluate consequences, not the identity of a correct action. Hidden charge can make the latest observation insufficient. One outcome does not supply the distribution of future consequences. The next session will also introduce values and contrast continuing with episodic tasks. Assign no reading, video or extra exercise.

**Sources:** current Introduction PPTX 19; accepted `formulate` / `mdp_values` boundary.

## I-A1 — Recycling robot reference (appendix only)

**Status:** appendix placement accepted under A12; detailed wording remains part of this proposal. Do not insert into the live reveal or allocate additional teaching time. The separate project-checklist proposal O8 remains open; its prompts are in notes only.

**Display**

> Recycling robot — the simplified formulation

| Component | Choice in this example |
| --- | --- |
| Decisions | Search, wait; also recharge when charge is low |
| State with the gauge visible | High or low battery charge |
| Feedback | Successful search: 2; wait: 1; recharge: 0; depletion/rescue: −3 |
| Objective | Collect cans over time while accounting for rescue costs |
| Horizon | Continuing; the four displayed steps are an excerpt |

Small caption: “Adapted from Sutton & Barto, Example 3.3. Successful-search and waiting rewards are illustrative.”

**Notes:** Formulation prompts for later project work: what decisions, what information, what reward, and over what horizon? Do not turn this into a new student deliverable or require it during the blank-slide discussion. The vacuum reward-design question remains an optional verbal backup in instructor notes, not another live slide: if a cleaning robot can dump and recollect dirt, rewarding collected dirt can reward that loop. Use only if it helps a question raised in class; it is outside the planned core discussion.

## Timing and rendering boundary

| Segment | Minutes |
| --- | ---: |
| I01 — introduction | 1 |
| I02 — four motivation examples | 4 |
| I03 — short learning-method comparison | 3 |
| I04 — interaction diagram | 3 |
| I05 — instructor-led robot formulation | 9 |
| I06 — reward and return | 3 |
| I07 — trace comparison | 5 |
| I08 — learning and exploration, including conditional planning contrast | 4 |
| I09a/I09b — observation/state discussion and definitions, combined | 4 |
| I10 — closing check and bridge | 2 |
| **Total** | **38** |

The configured allowance is 70 × 0.85 − 20 = 39.5 content minutes, leaving 1.5 within that allowance and the separate 15% general buffer. Questions are included in the segment estimates. Compared with the earlier suggestions, the four-example motivation and exploration prompt use time recovered from the longer standalone policy/model block, fixed pair-exercise format and extra vacuum question. This is a local feasibility estimate, not a claim of classroom-tested pacing. The I09 split adds no explanation or teaching time.

**Pacing contingencies:** If the briefing has already overrun when I02 begins, shorten motivation narration to about 2.5 minutes while retaining all four examples. If the robot discussion overruns later, skip the optional spoken planning contrast in I08, then reduce I10 to the bridge sentence if needed. Shortening I02 cannot recover a later overrun. Protect the robot formulation (I05) and the two reasoning checks (I07, I09a/I09b); these are the main pacing risks, so avoid adding examples or a second vocabulary explanation. No scope, assessment or required-workload addition is proposed.

Claude's proposal review and ChatGPT's response are in the [same review file](../../../analysis/lecture_suggestions/introduction_review.md). Example choices and appendix placement are settled; other open content details in the deck decisions remain proposals for instructor review. Actual media selection, native-diagram fidelity and table readability still need checking during rendering and deck review. This proposal remains editable through review and fixes; no PPTX is generated as part of this review response.

## Local source locators

PPTX numbers include hidden slides; PDF numbers are physical pages. These are instructor references, not student readings.

- [Current Introduction PPTX](../../../sources/current_course/1%20-%20Introduction.pptx): 8, 19, 42, 49–51. Reuse edits are specified at the relevant slide IDs above.
- [Sutton & Barto](../../../sources/RLbook2020.pdf): Example 3.3, printed pp. 52–53 / PDF pp. 74–75; §§1.1, 3.2–3.3.
- [CS234 Winter 2026 introduction](../../../sources/stanford_cs234/lectures/lecture1post.pdf): pp. 4, 7–8, 13–19, 35–38. Go and fusion visuals were inspected; retain primary attributions.
- [CS224R Spring 2026 introduction](../../../sources/stanford_cs224r/lectures/01_cs224r_intro_2026.pdf): pp. 8, 17–22; p. 37 reserved for 1.2. Adapt explanations, not its notation or full application tour.
- [Silver introduction](../../../sources/silver_rl/lectures/intro_rl.pdf): pp. 18–24 and 37–42. Other introductory sources already compared in the historical review do not require additional slides.
