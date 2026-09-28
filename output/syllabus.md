# Reinforcement Learning — syllabus draft

Syllabus content and workload accepted in principle. Weekly teaching sequence is unchanged. Revised assignment windows are incorporated; exact calendar dates remain provisional.

## Course purpose and preparation

Develop a coherent foundation in tabular and approximate RL, connect it to deep/model-based/offline methods, and use those foundations to understand RL-based LLM post-training. Expected background: probability, linear_algebra, basic_machine_learning, python_programming, basics of tree/graph search. Required work is designed around personal-laptop access; no mandatory LLM-training assignment.

## Learning outcomes

- L01: distinguish RL from other learning and planning settings
- L02: explain and distinguish state, observation, action, reward, value, policy, model and partial observability
- L03: formulate sequential decision problems as MDPs
- L04: derive and implement representative RL methods
- L05: select methods based on data, interaction and model availability
- L06: diagnose important RL failure modes
- L07: design and evaluate RL experiments
- L08: connect modern RL methods to common RL foundations

## Weekly teaching plan

| Week | First lecture | Second lecture |
| --- | --- | --- |
| 1 | RL formulation and information | MDPs, returns and values |
| 2 | Bellman equations and evaluation | Improvement, VI and PI |
| 3 | Sampling, MC/TD and continuing objectives | Bias, variance and n-step targets |
| 4 | Exploratory control and target policies | Control failure modes and project formulation |
| 5 | Linear approximation and semi-gradients | Approximation instability |
| 6 | DQN as approximate Q-learning | Double estimators and experimental diagnosis |
| 7 | Policy-search history and REINFORCE | Sampled gradients, baselines and critic motivation |
| 8 | Actor-critic, forward lambda and GAE | Importance ratios, PPO and entropy |
| 9 | SAC mechanism and policy-method comparison | Bandits, UCB and contextual decisions |
| 10 | From UCB to tree search | Guided search and Dyna |
| 11 | Model learning, MPC and horizon | Uncertainty, exploration and model error |
| 12 | Offline data, optimism/pessimism and IQL motivation | IQL value/policy fitting and CQL contrast |
| 13 | LLM policy updates after video preparation | Grouped estimators, rewards and evaluation |

See the [detailed lecture plan](lecture_plan.md) for accepted bounded scopes and time estimates.

## Assessment and grading

| Component | Course grade |
| --- | --- |
| Midterms | 45% |
| Project | 35% |
| Assignments | 20% |

Midterms: 15%, 15%, 15%.

Assignments are individual. assignment category score = 20 × mean(highest three normalized scores); omitted submissions count as zero. No separate requirement to complete all four is adopted. No final exam. Midterms use separate slots.

| Exam | Accepted window | Coverage |
| --- | --- | --- |
| midterm_1 | Week 6 or 7 | Weeks 1–5, before deep RL. Accepted taught/mastery scope governs questions; optional extensions are not silently examinable. |
| midterm_2 | Week 10 or 11 | Weeks 6–8 plus 9.1, including SAC; bandits in 9.2 are excluded. Interpret up to bandits as before bandits, following explicit session list. |
| midterm_3 | Week 13 | Instructor explicitly confirmed keeping midterm 3 in Week 13; its scope ends at Week 12 and excludes the LLM bridge. |

| Assignment | Last prerequisite | Release | Deadline |
| --- | --- | --- | --- |
| A1 | 4.2 | 4.2 | 7.2 |
| A2 | 6.2 | 6.2 | 9.2 |
| A3 | 8.2 | 8.2 | 11.2 |
| A4 | 12.2 | 12.2 | 15.2 |

The relative schedule assumes uninterrupted weeks; holidays, absences and makeups can change the mapping. Week 15.2 is a deadline coordinate after teaching, not an added lecture. A4’s revised January deadline and its proximity to the final project report remain provisional.

Accepted planning envelope: 26 lectures, with one tentative November makeup and one December makeup. Instructor reports October 29 holiday, November 3 absence and January unavailability. Start: Week of October 5; expected end January 8. Exact session dates, makeup placements and year are not inferred. Logical lecture weeks need not equal calendar weeks after these adjustments.

See [accepted assignment design](assignments.md) for task scope.

## Project

| Milestone | Deadline | Course grade | Length |
| --- | --- | --- | --- |
| Proposal | Week 4 | 5% | 2 pages |
| Formulation/design | Week 7 | 5% | 2–3 pages |
| Progress and evaluation plan | Week 10 | 7.5% | 3–4 pages |
| Presentation | Week 13 | 7.5% | 10 minutes + 3 minutes discussion per team |
| Final report and reproducibility package | One week before letter grades are due (expected Third week of January; exact date/year from official calendar, not inferred) | 10% | 6–8 pages + references |

Teams of 2–3 encouraged; individual/four-person exceptions case by case. Three tentative two-hour presentation slots, eight teams per slot; attend only your own slot. Presentation scheduling/peer grading will be settled during the semester. See [project schedule](project_schedule.md).

## Videos and readings

| Video | Tentative release | Needed before | Playback minutes | Student effort including playback |
| --- | --- | --- | --- | --- |
| search_background | 9.1 | 10.1 | 30–40 | 40–60 |
| llm_background | 12.1 | 13.1 | 50–65 | 70–100 |

Videos are required background, tentatively released seven days before use; scopes reviewed in Weeks 4, 8 and 11. No assigned readings this semester.

## Assignment authorship and LLM use

Include examples of how LLMs were used. Instructor specifies no credit for one-shot or few-shot delegation of the assignment solution.

- Identify which task components used an LLM; include representative prompts and output excerpts.
- Explain what was accepted, rejected or changed, and why; supply at least one relevant check/debugging example if an LLM contributed a solution.
- Explain the submitted update/experiment in the student’s own terms. Disclose non-use without manufacturing logs.

Concrete rubric, penalty scope and the example report will be finalized during the semester, as directed. No prompt-count threshold or new penalty is inferred in this draft.

## Dates and operational details to finalize

Official dated calendar, exact exam dates/durations, and January deadline mapping remain to be finalized. Presentation slots and the Week 13 clash will be resolved during the semester after proposals/team freeze. Readings are removed. Concrete assignment rubrics/examples are intentionally deferred.
