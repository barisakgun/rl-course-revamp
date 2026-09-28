# Course Principles

## Course purpose

The course should provide a coherent foundation in reinforcement learning while giving students enough exposure to modern deep RL, model-based RL, offline RL, and RL-based LLM post-training to understand contemporary methods.

The goal is not to maximize the number of algorithms covered. Topic selection and depth should prioritize transferable concepts, coherent progression, and the ability to reason about unfamiliar RL methods.

## Foundations before algorithm catalogs

Students should first understand the common concepts underlying RL methods: sequential decision making, state and observation, reward and return, value functions, policies, models, Bellman equations, sampling, bootstrapping, exploration, distribution shift, and approximation.

Named algorithms should be used to instantiate these concepts rather than becoming an end in themselves.

When several methods teach essentially the same conceptual lesson, prefer one or two representative methods at meaningful depth over a broad catalog of variants.

## Classical and modern RL

The course should preserve classical material when it remains conceptually important for understanding modern RL.

Historical importance alone is not sufficient reason for detailed coverage. Classical methods whose main pedagogical value can be retained through a shorter conceptual treatment should be compressed or moved to exposure or extension status.

Modern or currently popular methods do not automatically become Core. Pedagogical role and current research/practice status are separate dimensions.

## Topic roles and mastery

Each included topic should eventually receive a pedagogical role:

- Core: expected of all students and important to later understanding or assessment.
- Exposure: students should understand the motivation, central idea, and relationship to other material, but detailed derivation or implementation is not required.
- Extension: optional advanced material, further reading, or project-oriented material.

Expected mastery should be recorded independently using appropriate levels such as recognize, explain, derive, implement, and analyze.

A topic's current research or practical status should also be recorded independently from its pedagogical role.

## Course pacing

The planned curriculum should fit within 13 weeks rather than relying on the full nominal 14-week semester.

Live lecture plans should not consume all nominal contact time. The configured usable-content fraction should reserve meaningful capacity for questions, examples, clarification, overruns, and consolidation.

A time-budget audit should be performed after every substantive curriculum revision.

Arithmetic fit is not sufficient. Topic combinations should also be judged for conceptual density and realistic student learning pace.

## Videos

Videos should primarily carry self-contained prerequisite or background material that benefits from pause/replay and does not require substantial live interaction.

Videos should be planned pedagogically rather than used as a routine mechanism for recovering from an overloaded syllabus.

Live time should preferentially be used for derivations, conceptual difficulties, examples, comparisons, and discussion.

## Readings

Required readings should be limited and purposeful.

Readings may serve different roles:

- textbook material for foundational development;
- seminal papers for historically or conceptually important methods;
- modern representative papers or surveys for current practice and active research.

A reading should not be required merely because it is influential. Required reading workload must be included in the final workload audit.

## Assessment

Assessment should follow expected mastery.

Topics students are expected to derive, implement, or analyze should normally have an appropriate assessment path.

Exposure and extension topics should not create disproportionate examination or assignment burden.

Assignments should help students achieve the relevant course learning outcomes through practice and feedback, and provide evidence of the expected mastery. Their scope and workload should serve those outcomes.

Detailed provisional assignment hypotheses belong in `config/provisional_plan.yaml`. Accepted assignment designs belong in `decisions/assignment_decisions.md` after the assignment-design phase.

A mandatory LLM assignment is not required. LLM-based RL should remain available as a project direction for interested students.

## Project

The course should retain a semester-long end-to-end project.

Students should identify a problem, formulate it as an RL problem, implement a solution, compare it with meaningful baselines, evaluate it systematically, and communicate the results.

Project milestones should force early formulation and evaluation decisions rather than allowing the project to become an end-of-semester implementation exercise.

The current milestone structure is proposal, formulation/design checkpoint, progress checkpoint, presentation, and final report. Scheduling must respect the class-hour constraints in `config/course.yaml`; exact milestone dates and grading remain subject to project-design review.

## Use of external courses

External courses are evidence, not authority.

Differences in audience, prerequisites, course length, instructor goals, and historical period must be considered when comparing curricula.

Frequency across reference courses must not be treated as a vote for inclusion.

Absence from available public material must not automatically be treated as evidence that a topic was not taught.

## Current practice and research claims

Claims that a method represents current practice, a de facto standard, or state of the art must specify the relevant task/domain and the date of the evidence.

Prefer durable conceptual understanding over chasing short-lived algorithmic trends.

## Curriculum revision

Curriculum changes should be small and reviewable.

Any substantive addition should identify what time or depth it displaces.

Accepted curriculum decisions should be recorded separately from recommendations and source analysis.

The course should be frozen only after topic roles, mastery expectations, ordering, delivery, learning-outcome coverage, and realistic time allocation are internally consistent.
