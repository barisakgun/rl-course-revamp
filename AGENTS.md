# RL Course Revamp

## Objective

Develop a redesigned university Reinforcement Learning course that balances:

- fundamental reinforcement learning;
- deep reinforcement learning;
- modern RL topics;
- RL-based LLM post-training.

The course should emphasize coherent learning progression, transferable understanding, realistic student workload, and sufficient depth on foundational concepts.

Do not maximize topic coverage.

External courses are evidence and reference points, not authorities. Frequency across reference courses must not be treated as a vote that automatically determines the curriculum.

## Required project context

Before performing substantive work, read:

- `config/course.yaml`
- `config/sources.yaml`
- `config/taxonomy.yaml`
- `config/provisional_plan.yaml`
- `decisions/course_principles.md`
- `docs/repository_contract.md`

Follow the repository authority, derived-file, and source-of-truth rules defined in `docs/repository_contract.md`.

Do not treat files under `analysis/` or `output/` as authoritative curriculum decisions.

## Repository roles

Use the repository layers consistently:

- `config/`: project constraints, configured sources, taxonomy, and provisional plan.
- `sources/`: source evidence and local course material.
- `analysis/`: factual normalization, comparisons, audits, and recommendations.
- `decisions/`: accepted, rejected, or unresolved curriculum/design decisions.
- `course/`: editable teaching artifacts.
- `output/`: generated human-readable views, reports, and rendered/exported artifacts.
- `docs/`: repository and workflow documentation.
- `scripts/`: reproducible data collection, normalization, auditing, and generation utilities.

Editable teaching artifacts belong in `course/`.

Generated planning views, reports, audits, and rendered/exported artifacts belong in `output/`.

## Avoid duplicated state

Maintain each substantive curriculum fact in one authoritative location.

Examples:

- accepted topic role, mastery, status, delivery, and assessment decisions belong in `decisions/topic_decisions.yaml`;
- accepted video decisions belong in `decisions/video_decisions.md`;
- accepted reading decisions belong in `decisions/reading_decisions.md`;
- accepted assignment decisions belong in `decisions/assignment_decisions.md`;
- accepted project decisions belong in `decisions/project_decisions.md`.

Human-readable views derived from authoritative structured data should be generated rather than maintained independently.

Do not change curriculum state by editing a generated file.

Use Git history rather than creating parallel files such as `_v2`, `_new`, or `_final` unless explicitly requested.

## Evidence discipline

Keep factual source extraction separate from curriculum interpretation and recommendations.

For external course material, distinguish where possible between:

- explicitly covered;
- brief mention or exposure;
- assigned or recommended reading only;
- assessed through assignment/project/exam;
- not found in available public material;
- unknown because evidence is incomplete or inaccessible.

Do not interpret `not found` as `not taught`.

Label inferred properties such as depth, importance, or approximate time allocation as inference rather than fact.

Preserve source provenance for claims derived from external courses.

## Source collection

For every configured external course:

1. inventory relevant teaching material;
2. preserve source URL, offering/year where identifiable, retrieval date, and material type;
3. distinguish taught material from optional resources;
4. prefer linking/indexing to indiscriminate mirroring;

Local course material should be inventoried using the same conceptual categories where practical.

## Topic normalization

Normalize course-specific terminology into stable topic identifiers.

Use stable snake-case topic IDs, for example:

- `temporal_difference_learning`
- `q_learning`
- `generalized_advantage_estimation`

Do not infer equivalence solely from similar names.

Record ambiguous mappings explicitly.

Use the controlled taxonomy defined in `config/taxonomy.yaml`.

Keep source-course observations separate from decisions about the redesigned course.

## Curriculum iteration

External courses are evidence, not authority.

Every substantive proposed curriculum change must state:

- what changes;
- why;
- relevant evidence;
- what material is displaced, compressed, or moved;
- prerequisite consequences;
- delivery consequences where relevant;
- time-budget consequences.

Do not modify an accepted curriculum decision without recording the change in `decisions/decision_log.md`.

Curriculum recommendations belong in `analysis/`.

Accepted instructor decisions belong in `decisions/`.

Never silently promote a recommendation into an accepted decision.

## Time-budget discipline

Run a time-budget audit after every substantive curriculum revision.

Use the usable-content fraction defined in `config/course.yaml`.

The audit should identify:

- overloaded lectures or weeks;
- unrealistic topic combinations;
- prerequisite problems;
- inadequate time for examples, questions, or consolidation;
- Core topics receiving insufficient depth;
- videos or readings that create hidden workload.

Arithmetic fit is not sufficient evidence of pedagogical feasibility.

Any substantive addition should identify what time or depth it displaces.

## Current practice and research claims

Pedagogical role and research/practice status are separate dimensions.

Do not classify a topic as Core merely because it is recent or widely used.

Do not use `SOTA` or equivalent claims without specifying:

- task or domain scope;
- date or time period;
- supporting evidence.

Prefer durable conceptual understanding over short-lived algorithmic trends.

## Assessment alignment

Assessment should reflect intended mastery.

Topics expected at `derive`, `implement`, or `analyze` level should normally have an appropriate assessment path.

Exposure and Extension material should not create disproportionate assessment burden.

Before final course design is frozen, verify:

- learning outcomes map to taught material;
- important Core material is appropriately assessed;
- assessments do not require untaught prerequisites;
- project milestones occur after required concepts;
- assessment workload is realistic.

## Curriculum freeze

A curriculum may be proposed for freeze only when:

- included topics have pedagogical roles;
- included topics have expected mastery;
- included topics have research/practice status where relevant;
- prerequisite ordering is coherent;
- live/video/reading delivery decisions are sufficiently resolved;
- live teaching fits the configured usable-time budget;
- Core topics receive sufficient depth;
- learning outcomes are covered;
- high-impact curriculum recommendations are resolved.

Generate a curriculum consistency audit before recommending freeze.

## Syllabus/design freeze

After assignments, project structure, readings, and delivery decisions are finalized, audit:

- assessment-to-learning-outcome alignment;
- assignment workload and sequencing;
- project milestone timing;
- total student workload;
- required reading and video workload;
- consistency among accepted decisions, lecture plan, and syllabus.

Generate the final workload and consistency audits before recommending syllabus/design freeze.

## Phase boundaries

Work only on the phase explicitly requested.

Do not automatically advance to a later phase.

At the end of a phase:

1. complete the requested artifacts;
2. identify unresolved issues;
3. report material limitations or evidence gaps;
4. summarize recommended next actions;
5. stop.

Source extraction must not modify curriculum decisions.

Normalization must not silently become curriculum recommendation.

Analysis must not silently become accepted decision.

## Working style

Prefer structured Markdown and YAML that can be inspected and diffed.

Prefer reproducible scripts for repeated extraction, normalization, auditing, or output generation.

Make small, reviewable curriculum iterations rather than rewriting the whole course without justification.

At the end of a curriculum iteration, summarize:

1. proposed changes;
2. supporting evidence;
3. unresolved decisions;
4. time-budget result.