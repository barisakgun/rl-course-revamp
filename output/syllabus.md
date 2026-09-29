<!-- Generated from the editable syllabus DOCX by scripts/syllabus_report.py. Edit the DOCX for teaching prose; accepted curriculum and assessment facts remain in decisions. -->

# COMP438/538 Reinforcement Learning

Fall 2026

## Class

Times: Tuesdays and Thursdays between 14.30 and 15:40

Location: CASEZ27

Website: https://learn.hub.ku.edu.tr

E-mail policy: Students are responsible for checking their account frequently and consistently.

## Instructor

Barış Akgün

Office Hours: By appointment (both online or face-to-face) or open door especially after lectures

E-mail: baakgun@ku.edu.tr

## Teaching Assistants

| Name | Email | Office hours |
| --- | --- | --- |
| TBA | TBA | TBA |

## Prerequisites

Comp341: Intro to Artificial Intelligence

The student should know agent-based modeling, rationality, utility and decision-making concepts and have a sense of what state, action and reward/cost mean.

This pre-req also indirectly enforces probability and statistics, and to a lesser extent Python Programming

Cop421/521: Machine Learning

The student should be familiar with general machine learning concepts, stochastic gradient descent, linear regression, and neural networks.

Deep Learning

No prerequisite but knowing deep learning would help the students.

Basics of Probability & Statistics and Linear Algebra (e.g., ENGR200 and MATH107)

No prerequisite, but students are expected to know or learn the relevant topics.

Python Programming

No prerequisite, but if you don’t know Python, I recommend not taking this course.

## Catalog Description

Introduction to the Reinforcement Learning, Markov Decision Processes, Value and Policy Iteration, Q-Learning and SARSA, Policy Search and Policy Gradients, Actor-Critic Approaches, Deep Reinforcement Learning, Model-Based Methods, Exploration, Applications

## Course Objectives

Build a coherent foundation in reinforcement learning, formulate sequential decision problems, and design and evaluate learning agents. Connect tabular and approximate methods to deep, model-based and offline RL, then use these foundations to understand RL-based LLM post-training.

## Learning Outcomes

L01. Distinguish RL from other learning and planning settings

L02. Explain and distinguish state, observation, action, reward, value, policy, model and partial observability

L03. Formulate sequential decision problems as MDPs

L04. Derive and implement representative RL methods

L05. Select methods based on data, interaction and model availability

L06. Diagnose important RL failure modes

L07. Design and evaluate RL experiments

L08. Connect modern RL methods to common RL foundations

## Topic Outline

The course retains 26 lectures in the sequence below. Teaching units describe progression, not booked calendar weeks. Timing may be adjusted within the topic scope.

| Teaching units | Topics |
| --- | --- |
| 1–2 | RL formulation and MDPs; returns and values; Bellman equations; policy evaluation, value iteration and policy iteration. |
| 3–4 | MC and TD prediction; bias, variance and n-step returns; exploration; SARSA and Q-learning; control failure modes. |
| 5–6 | Linear approximation and semi-gradients; instability and the deadly triad; DQN, replay, target networks and Double DQN. |
| 7–9.1 | REINFORCE and baselines; actor-critic and GAE; importance ratios, PPO, entropy and SAC. |
| 9.2–10 | Bandits and UCB; contextual decisions; MCTS, guided search and Dyna. |
| 11 | Learned models, MPC, horizon choice, uncertainty and model error; representative world-model ideas. |
| 12 | Offline data support and distribution shift; IQL value/policy fitting; brief conceptual CQL contrast. |
| 13 | RL for LLM post-training: policy updates, grouped estimators, rewards, failure modes and evaluation. |

## Teaching and Preparation

Teaching is mainly through lectures and worked examples. Lecture attendance is not tracked; participation, questions and discussion are encouraged. Two required background videos prepare you for search/MCTS and LLM RL. Videos are tentatively released seven days before use, with preparation reviewed in Weeks 4, 8 and 11.

No student readings are assigned this semester and there are no reading-only exam requirements. Required work is designed for personal-laptop access; there is no mandatory LLM-training assignment.

## Assessment and Grading

Theory, implementation and experimental reasoning are assessed through individual assignments, three midterms and a semester project.

| Component | Assessment | Course grade |
| --- | --- | --- |
| Assignments | Four individual assignments; best three count | 20% |
| Midterms | Three midterms; 15% each | 45% |
| Project | Staged reports and presentation | 35% |
| Total |  | 100% |

## Calendar Targets

Calendar Week 1 begins October 5, 2026. The expected end of classes is January 8, 2027. One makeup lecture is planned in each of October, November and December. Exact makeup, exam and submission dates and times are TBA. The week-level schedule will be reviewed after the first two weeks of classes when registration and attendance stabilize.

## Assignments

The assignment category is 20% times the mean of your highest three normalized scores. Missing submissions count as zero; completing all four is not required. Each counted assignment can contribute up to 20/3 course percentage points.

| Task | Focus | Release | Due |
| --- | --- | --- | --- |
| A1 | Planning and learning from sampled transitions | Week 4 | Week 7 (early) |
| A2 | Representation, instability and a small DQN | Week 6 | Week 9 |
| A3 | Policy-gradient estimators and update diagnosis | Week 8 | Week 11 (later) |
| A4 | Scaffolded IQL and offline data support | Week 12 | Week 15 |

Each assignment is released after its relevant concepts have been taught and remains open for at least 21 days. One-week overlaps are allowed. The early Week 7 A1 target must retain the full window after prerequisites; exact dates will be announced. Rubrics and an example LLM-use report will be provided with concrete assignment instructions.

## Midterms

| Exam | Target | Coverage |
| --- | --- | --- |
| MT1 | Week 6 | Teaching units 1–5: formulation through linear approximation and instability, before deep RL. |
| MT2 | Week 10 | Teaching units 6–8 plus 9.1: DQN through SAC; excludes bandits. |
| MT3 | Week 13 | Teaching units 9.2–12: bandits, search/model-based RL and offline RL, including a brief conceptual CQL question; excludes LLM RL. |

Each midterm uses a separate exam slot. Exact dates, durations and arrangements are TBA. There is no final exam. Exams assess taught concepts at the expected level; they do not assume that an assignment has been submitted or its feedback released.

## Semester Project

Develop an end-to-end RL study: formulate a problem, build a solution, compare a meaningful baseline, evaluate results systematically and communicate limitations. Teams of 2–3 are encouraged; individual work and four-person teams are considered case by case. A well-supported negative result can succeed; novelty and benchmark superiority are not required.

| Milestone | Target | Length | Course grade |
| --- | --- | --- | --- |
| Proposal | Week 4 | 2 pages | 5% |
| Formulation/design | Week 7 (later in the week) | 2–3 pages | 5% |
| Progress and evaluation plan | Week 11 (early in the week) | 3–4 pages | 7.5% |
| Presentation | Week 14 | 10 minutes + 3 minutes discussion per team | 7.5% |
| Final report and reproducibility package | Week 16 | 6–8 pages + references | 10% |

The final report and reproducibility package target Week 16, January 18–24, 2027. The exact deadline is TBA and must be one week before letter grades are due.

The proposal establishes the problem, baseline and feasibility. The design checkpoint establishes a runnable environment/data pipeline and simple baseline. The progress checkpoint shows preliminary results and an evaluation plan. The final report consolidates evidence, limitations, code/configuration and contributions.

Presentations are online, TA-led and recorded in Week 14. The tentative plan is three two-hour slots with up to eight teams per slot. Each team attends only its own slot. The TA and attending groups grade presentations; slots, staffing, rubric and grade split will be announced. Each team has 10 minutes plus 3 minutes for discussion.

Projects using offline or LLM RL need early self-study, a simple runnable baseline and a feasible fallback by Week 7. Late topics do not postpone the Week 11 progress checkpoint. Keep compute budgets manageable and evaluate against a meaningful baseline with a controlled comparison.

## Homework and Report Submissions and Late Policy

All homeworks and reports are required to be submitted online through the KU Hub system. The submission time will be taken as the server received time. If the system is down, we will give a proper extension. E-mail submissions are not accepted.

The students are expected to download their submissions and check them. It is the students’ responsibility to make sure that the submission is not corrupted, is not wrong, is not an older version etc. Only the latest submissions in the system will be graded.

You will have a total of 10 days late allowance with a maximum lateness of 3 days per submission other than the final report. You can use your remaining late days to submit your final report but depending on how late you are, you may receive an “Incomplete” grade. If you exceed your 3-day allowance per submission or your total 10-day allowance, your grades will be penalized.

## Code of Conduct

The students are expected to abide by the student and classroom codes of conduct of KU. There will be no tolerance for cheating, plagiarism, unruliness, and all other unethical and disruptive behavior. Any violation will be dealt with according to university policies.

## Large Language Model Use

LLMs may be used for coding and reports with disclosure. Cite their use; failure to disclose is treated as plagiarism. You remain responsible for errors and must understand, check and explain submitted work. A usage report is required; details will be supplied before the first assignment/report.

For assignments, one-shot or few-shot delegation of the assignment solution receives no credit. The operational rubric and penalty details will accompany the concrete assignments. The assignment-specific no-credit rule is not automatically extended to projects.

For the assignment LLM-use report:

- Identify which task components used an LLM; include representative prompts and output excerpts.

- Explain what was accepted, rejected or changed, and why; supply at least one relevant check/debugging example if an LLM contributed a solution.

- Explain the submitted update/experiment in the student’s own terms. Disclose non-use without manufacturing logs.

The students are not allowed to use LLMs for their midterms in case they end up being online or take-home, since we are measuring your knowledge on the topics and not on solving a problem using a tool.

## Makeup Exam Policy

There will be only a single comprehensive makeup exam, scheduled solely at the discretion of the instructor.

The makeup exam can be written or oral, at the discretion of the instructor.

Students need to have a legitimate excuse to be able to take the makeup exam. Students need to notify the instructor or the university within 5 days of the exam. The instructor reserves the right to deny the makeup after 5 days even if the excuse is legitimate.

If the student misses one exam with an acceptable excuse, the makeup grade will be counted towards the missed exam.

If the student misses two exams with acceptable excuses, the makeup grade will be counted towards both.

If the student misses three exams, the makeup will be counted towards at most two exams, regardless of having legitimate excuses for all three.

There will be no makeups for the makeup exam.

## Early Exam Policy

If you are going to an exchange program before the semester ends, you need to contact the instructor before week 10 to schedule an early exam. There will be no makeups for the early exam.
