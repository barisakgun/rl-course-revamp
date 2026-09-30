<!-- Generated from the instructor-frozen course/syllabus/syllabusFall26.docx by scripts/syllabus_report.py. Do not edit this view. Freeze identity/scope: decisions/syllabus_decisions.yaml. Internal planning detail is not added to the student-facing text. -->

# COMP438/538 Reinforcement Learning – Fall 2026

## Class

Times: Tuesdays and Thursdays, 14.30 - 15:40

Location: CASEZ27

Website: [https://learn.hub.ku.edu.tr](<https://learn.hub.ku.edu.tr>)

E-mail policy: Students are responsible for checking their university email regularly.

## Instructor

Barış Akgün

Office Hours: By appointment (online or in person), or whenever my door is open, especially after lectures.

E-mail: [baakgun@ku.edu.tr](<mailto:baakgun@ku.edu.tr>)

## Teaching Assistants

| NAME | E-MAIL | OFFICE HOURS |
| --- | --- | --- |
| TBA | TBA | TBA |

## Prerequisites

### COMP341: Intro to Artificial Intelligence

- Students should know agent-based modeling, rationality, utility and decision-making concepts and have a sense of what state, action and reward/cost mean.

- This prerequisite also assumes background in probability and statistics and, to a lesser extent, Python programming.

### COMP421/521: Machine Learning

- Students should be familiar with general machine learning concepts, stochastic gradient descent, linear regression, and neural networks.

### Deep Learning

- Prior coursework in deep learning is not required, but familiarity with it would be helpful.

### Basics of Probability & Statistics and Linear Algebra (e.g., ENGR200 and MATH107)

- No formal prerequisite, but students are expected to know/learn the relevant material.

### Python Programming

- Python is not a formal prerequisite, but I recommend taking this course only if you already know Python.

## Catalog Description

Introduction to Reinforcement Learning, Markov Decision Processes, Value and Policy Iteration, Q-Learning and SARSA, Policy Search and Policy Gradients, Actor-Critic Approaches, Deep Reinforcement Learning, Model-Based Methods, Exploration, Applications

## Course Objectives

Build a coherent foundation in reinforcement learning, formulate sequential decision problems, and design and evaluate learning agents. Connect tabular and approximate methods to deep, model-based and offline RL, then use these foundations to understand RL-based LLM post-training.

## Learning Outcomes

1. Distinguish RL from other learning and planning settings

2. Explain and distinguish state, observation, action, reward, value, policy, model and partial observability

3. Formulate sequential decision problems as MDPs

4. Derive and implement representative RL methods

5. Select methods based on data, interaction and model availability

6. Diagnose important RL failure modes

7. Design and evaluate RL experiments

8. Connect modern RL methods to common RL foundations

## Textbook

Sutton and Barto, [Reinforcement Learning: An Introduction](<http://incompleteideas.net/book/the-book.html>), 2nd Ed.

## Tentative Topics

| Topic | Details |
| --- | --- |
| MDP Fundamentals | RL formulation and MDPs; returns and values; Bellman equations; policy evaluation, value iteration and policy iteration. |
| Tabular RL | MC and TD prediction; bias, variance and n-step returns; exploration; SARSA and Q-learning; control failure modes. |
| Value Function Approximation | Linear approximation and semi-gradients; instability and the deadly triad; DQN, replay, target networks and Double DQN. |
| Policy Search | REINFORCE and baselines; actor-critic and GAE; importance ratios, PPO, entropy and SAC. |
| Exploration and Planning | Bandits and UCB; contextual decisions; MCTS, guided search and Dyna. |
| Model-Based RL | Learned models, MPC, horizon choice, uncertainty and model error; representative world-model ideas. |
| Offline RL | Offline data support and distribution shift; IQL value/policy fitting; conceptual overview of CQL. |
| LLMs + RL | RL for LLM post-training: policy updates, grouped estimators, rewards, failure modes and evaluation. |

## Teaching

The course will be taught mainly through lectures, supplemented by videos as needed. Lecture attendance will not be tracked, but participation, questions and discussion are encouraged.

## Assessment and Grading

Theory, implementation and experimental reasoning are assessed through individual assignments, three midterms and a semester project.

| Type | Description | Grade % |
| --- | --- | --- |
| Assignments | Planned 4 individual assignments, lowest one dropped | 20 |
| Midterms | 3 Midterms, 15% each | 45 |
| Final Project | Reports and Presentation (see below) | 35 |
| Total |  | 100 |

## Assignments

There are 4 planned programming assignments. The number may change depending on how the semester proceeds. If there are more than 3, the lowest one will be discarded.

## Exams

Each midterm will cover a different set of topics. There will be no final exam.

## Final Project

The idea is for you to apply and extend your RL knowledge by working on a problem and develop an end-to-end RL study: formulate a problem, build a solution, compare your solution against a meaningful baseline, evaluate results systematically, communicate limitations and present your work. Teams of 2–3 are encouraged, but individual work and four-person teams may be considered. The expected project scope will depend on team size.  A well-supported negative result can succeed; novelty and benchmark superiority are not required. Further details of the final project will be presented during the semester. The project milestones and their weights in the overall course grade are:

- Project Proposal Report (5%)

- Formulation and Design Report (5%)

- Progress and Evaluation Report (7.5%)

- Presentation (7.5%)

- Final Report (10%)

## Assignment/Report Submissions and Late Policy

All assignments and reports are required to be submitted online through the KU Hub system. The submission time is the time recorded by the server. If the system is down, an appropriate extension will be granted. E-mail submissions are not accepted.

Students are expected to download and check their submissions. They are responsible for ensuring that the correct, current files were uploaded and are not corrupted. Only the latest submission for each assignment or report will be graded.

You will have a total allowance of 10 late days, with a maximum of 3 late days per submission, except for the final report. You can use your remaining late days to submit your final report, but depending on how late you are, you may receive an “Incomplete” grade. If you exceed your 3-day allowance per submission or your total 10-day allowance, your grades will be penalized.

## Code of Conduct

Students are expected to abide by the student and classroom codes of conduct of KU. There will be no tolerance for cheating, plagiarism, unruliness, and all other unethical and disruptive behavior. Any violation will be dealt with according to university policies.

## Large Language Model (LLM) Use Policy

LLMs may be used for coding and reports with disclosure. You must disclose their use and failure to do so is treated as plagiarism. You remain responsible for errors and must understand, check and explain submitted work. An LLM-use report is required for each assignment and report. The requirement details will be given before the first assignment/report. For assignments, one-shot or few-shot delegation of the assignment solution receives no credit. You must disclose their use; failure to do so is treated as plagiarism. Project reports will lose marks for verbose, repetitive, unnecessarily detailed, unfocused or vague writing, including such writing frequently produced by AI tools.

If midterms are held online or as take-home exams, students may not use LLMs: these exams assess their knowledge of the material, rather than their ability to solve problems using a tool.

## Make-up Policy

- There will be only a single comprehensive make-up exam, scheduled solely at the discretion of the instructor.

- The make-up exam can be written or oral, at the discretion of the instructor.

- Students need to have a legitimate excuse to be able to take the make-up exam. Students need to notify the instructor or the university within 5 days of the exam. The instructor reserves the right to deny a make-up request if notification is received more than 5 days after the exam, even if the excuse is legitimate.

- If a student misses one exam with an acceptable excuse, the make-up grade will be counted towards the missed exam.

- If a student misses two exams with acceptable excuses, the make-up grade will be counted towards both.

- If a student misses three exams, the make-up will be counted towards at most two exams, regardless of having legitimate excuses for all three.

- There will be no make-ups for the make-up exam.

## Early Exam Policy

If you will leave for an exchange program before the semester ends, you need to contact the instructor before week 10 to schedule an early exam. There will be no make-ups for an early exam.
