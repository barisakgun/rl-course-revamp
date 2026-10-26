# Project overview: first-render content

Author: ChatGPT, 2026-10-22. Instructor-requested content suggestion and first render.
Historical first-render input, frozen 2026-10-22. Edit `course/projects/project_overview_chatgpt.pptx` as the teaching source.
Accepted policy remains in `decisions/project_decisions.md` and the frozen syllabus.
The standalone proposal-guidelines handout is deferred to release-day preparation.

## Content rationale

Retain the previous `sources/current_course/Project.pptx` title/content template and its project-purpose, baseline and communication spine (slides 3–4). Replace novelty/benchmark emphasis (slide 5) with accepted bounded project types. Replace old dates/weights and the combined progress checkpoint (slides 8–10) with the accepted five milestones, displaying all release/due dates as TBD. Update team/submission/report expectations (slides 11–12) from current decisions and the frozen syllabus. Expand the old proposal slide 9 and `ProposalSpring21.pdf` page 1 into exactly three proposal-detail slides. The high-level related-work and tentative-baseline wording follows the instructor's October 22 clarifications.

Delivery estimate: approximately 12–15 minutes including brief questions, not a newly accepted lecture allocation. No curricular time, milestone, or implementation requirement is added. Slot placement remains to be chosen by the instructor. Existing usable-time planning fraction remains 0.85. The proposal's existing 3–5-hour estimate in `analysis/phase5_plan.yaml` remains an unpiloted estimate, not a workload guarantee.

## Slide 1 — Project requirements

**On slide**

COMP438/538 Reinforcement Learning
Project requirements

Fall 2026
Barış Akgün
Koç University

**Speaker notes**

Introduce the semester project and its milestones, then explain the proposal in detail. Detailed proposal guidelines will be available on release day. Release and due dates remain TBD. Cover artwork and visual template retained from sources/current_course/Project.pptx, slide 1. Policy sources: decisions/project_decisions.md and course/syllabus/syllabusFall26.docx.

## Slide 2 — Project purpose and teams

**On slide**

- Develop an end-to-end RL study around a focused problem.
- Formulate the task, build a solution and compare with a meaningful baseline.
- Evaluate the evidence and explain the limitations of your conclusions.
- The project contributes 35% of the overall course grade.
- Teams of 2–3 are encouraged. Individual and four-person projects need approval.

**Speaker notes**

Scope depends on team size. The project gives students an opportunity to use course concepts in a sustained study. Grading emphasizes formulation, correctness, experimental reasoning and communication. A well-supported negative result can succeed. Sources: decisions/project_decisions.md (purpose, team_size, grading_principle); course/syllabus/syllabusFall26.docx, Final Project. Adapted from old Project.pptx slides 3–4 and 11.

## Slide 3 — Suitable project directions

**On slide**

- Reproduce a result and investigate one ablation.
- Apply RL to a small problem with a justified formulation and baseline.
- Make a focused modification to a familiar method.
- Study data coverage, model error or evaluation with a working RL baseline.
- Novelty and benchmark superiority are not required.
- Offline or LLM RL projects need early self-study and a feasible fallback.

**Speaker notes**

Examples of bounded questions include comparing two reward definitions on the same task, removing one component of a reproduction, or varying data coverage. Examples illustrate the accepted types, not prescribed projects. Advanced-track teams must have a runnable simple baseline and compute-feasible fallback by the design checkpoint, and cannot defer working evidence beyond the progress checkpoint. Prefer small models, fixed datasets or supplied traces when suitable. Sources: decisions/project_decisions.md (accepted_types, advanced_track, grading_principle). Replaces the novelty/benchmark emphasis in old Project.pptx slides 5–7.

## Slide 4 — Project deliverables

**On slide**

| Deliverable | Grade | Length | Release | Due |
| --- | --- | --- | --- | --- |
| Proposal | 5% | 2 pages + references | TBD | TBD |
| Formulation and design | 5% | 2–3 pages | TBD | TBD |
| Progress and evaluation | 7.5% | 3–4 pages | TBD | TBD |
| Presentation | 7.5% | 10 min + 3 min discussion | TBD | TBD |
| Final report and code | 10% | 6–8 pages + references | TBD | TBD |

Percentages are of the overall course grade. Total: 35%.

**Speaker notes**

The milestones build on each other. Reuse unchanged material and refine it as the project develops. Presentation timing refers to the team slot. The final report includes the reproducibility package, not just prose. Exact dates will be announced. The final-report date must satisfy the existing one-week-before-letter-grades rule. Sources: decisions/project_decisions.md (milestones); decisions/grading_decisions.md; instructor direction on October 22 to show release and due dates as TBD. Supersedes old Project.pptx slide 8's dates and milestone structure.

## Slide 5 — Design and progress checkpoints

**On slide**

- Formulation and design: refine the RL formulation and establish a runnable environment or data pipeline.
- Show a simple baseline and plan one comparison, an evaluation protocol, compute budget and fallback.
- Advanced methods may still be planned at the design checkpoint.
- Progress and evaluation: show a working baseline and preliminary learning or evaluation results.
- Specify evaluation conditions, seeds and budget. Diagnose a failure and identify the remaining work.

**Speaker notes**

These requirements belong to later milestones. The proposal does not require a working implementation. At progress, identify one ablation or controlled comparison and distinguish held-out evaluation from tuning. Reuse unchanged formulation text. The accepted design checkpoint does not require PPO/GAE completion before teaching. Source: decisions/project_decisions.md (formulation_design, progress_evaluation). Replaces the old combined formulation/progress stage in Project.pptx slide 10.

## Slide 6 — Experimental expectations

**On slide**

- Use a meaningful baseline and one controlled comparison.
- Make data, interaction and compute budgets explicit.
- Separate tuning from final evaluation.
- Plan for three independent seeds when feasible. Explain limitations if you use fewer.
- Include a failure case and discuss what the evidence supports.
- A well-supported negative result can succeed.

**Speaker notes**

These are project-wide expectations that become concrete across the checkpoints. At proposal, an initial plan is sufficient. A controlled comparison should isolate the factor under study where practical. Pilot on a laptop and scale only when needed. Extra compute and polished prose do not substitute for understanding. Source: decisions/project_decisions.md (evaluation, grading_principle).

## Slide 7 — Presentation and final submission

**On slide**

- Presentation: 10 minutes plus 3 minutes of discussion per team, outside lecture hours.
- Online, TA-led and recorded. Each member has a short explanation opportunity.
- Final report: formulation, related work, method/baseline, results, limitations and conclusions.
- Reproducibility package: runnable code, configuration, seeds, environment versions and representative logs.
- Include a statement of each member’s contributions.

**Speaker notes**

Each team attends its assigned slot. TA and attending groups grade presentations; exact slots and the grading split remain open. The final report consolidates prior reports into a coherent account of the work and its evidence. Details will accompany the relevant releases. Source: decisions/project_decisions.md (presentation, final_report, presentation_plan). This updates old Project.pptx slides 11–12 without adopting the old separate code deadline.

## Slide 8 — Reports and responsible use of LLMs

**On slide**

- Submit reports through KU Hub and check the uploaded files.
- LLMs may be used for coding and writing with disclosure.
- An LLM-use report is required for every report. Detailed instructions will accompany the release.
- Understand, check and be able to explain all submitted work.
- Reports lose marks for verbose, repetitive, unfocused or vague writing.
- The syllabus submission and late-day policies apply.

**Speaker notes**

Failure to disclose LLM use is treated as plagiarism. Students remain responsible for errors. The one-shot/few-shot no-credit rule in the syllabus is specific to assignments and is not extended to project coding. The syllabus permits ten late days in total with at most three per submission, except for the final report, whose separate rule remains in the syllabus. Do not promise a numeric penalty or an LLM-report format before those details are settled. Source: course/syllabus/syllabusFall26.docx (Assignment/Report Submissions and Late Policy; Large Language Model Use Policy), decisions/project_decisions.md (llm_use).

## Slide 9 — Proposal: problem and formulation

**On slide**

5% of course grade. 2 pages + references.
Release: TBD. Due: TBD.

- Include the project title and team members.
- Motivate the problem and state one question you want to investigate.
- Give a tentative RL formulation: states/observations, actions, rewards and horizon or termination.
- Explain the decision problem clearly, beyond naming a software environment.

**Speaker notes**

This is the first of three dedicated proposal-detail slides. For episodic tasks, explain what starts and ends an episode. For continuing tasks, explain the intended horizon or objective. Keep the formulation tentative where choices are still open, but make its meaning understandable. No deep-RL implementation is expected at this point. Sources: decisions/project_decisions.md (proposal, updated October 22); ProposalSpring21.pdf page 1; old Project.pptx slide 9. Names/title are retained from the old handout. The two pages cover main content and exclude references; the LLM-report page-count treatment remains to be specified in the release-day guidelines.

## Slide 10 — Proposal: baseline and related work

**On slide**

- Identify a tentative baseline and explain why it is a useful comparison.
- Describe the candidate approach or variation you want to investigate.
- Related work can be high-level and incomplete at this stage.
- Use it to support the motivation and sharpen the problem definition.
- Cite relevant sources and distinguish established work from your planned study.

**Speaker notes**

A baseline can be simple, provided it gives an informative comparison for the question. It need not be implemented or final at proposal time. A candidate approach can be described at a high level without claiming mastery of a method that has not yet been taught. The literature discussion should help explain why the problem or question matters; an exhaustive survey is not expected. Sources: instructor clarifications of October 22; decisions/project_decisions.md (proposal); ProposalSpring21.pdf page 1, related work.

## Slide 11 — Proposal: evaluation and feasibility

**On slide**

- Explain how you plan to answer the question: comparison, metrics and evaluation conditions.
- State how the metric reflects success. It may differ from the training reward.
- Identify the environment or data and how you will access it.
- Describe available compute, likely constraints and practical risks.
- Indicate how you could reduce scope if needed. No completed experiments are expected yet.

**Speaker notes**

Keep this an initial plan. For example, a navigation task could assess success rate, collision frequency or steps to completion while using a shaped training reward. The selected metric should answer the project question. Indicate uncertainty honestly: data access or runtime estimates may still need checking. This operationalizes the accepted broader evaluation/feasibility scope without requiring a completed evaluation protocol, measured runtime or a working fallback at proposal. For offline/LLM directions, plan early self-study and a runnable simple baseline plus fallback by design. Sources: decisions/project_decisions.md (proposal, advanced_track); ProposalSpring21.pdf page 1, evaluation plan. The standalone proposal guidelines will be supplied on release day.
