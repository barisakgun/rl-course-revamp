# RL Course Revamp Workflow

This document defines the project phases, expected outputs, permitted repository changes, and transition criteria.

Phase-specific prompts may add detail, but should remain consistent with this workflow, `AGENTS.md`, and `docs/repository_contract.md`.

The Phase 2 generated views (`analysis/topic_matrix.md` and `analysis/sequencing.md`) and the Phase 3 working audit (`analysis/time_budget.md`) are explicit exceptions to the usual `output/` location for generated views and reports. Their locations and permissions are specified below.

---

# Phase 1 — Source Collection and Inventory

## Goal

Build a reliable inventory of the configured external courses and the instructor's existing course material without yet comparing or redesigning curricula.

## Main activities

For each configured course:

- identify the relevant course offering/year where possible;
- inventory lecture pages, slides, notes, recordings, and other teaching material;
- inventory assignments and linked starter code where relevant;
- inventory readings;
- inventory project descriptions, milestones, rubrics, and examples where available;
- record source provenance and accessibility;
- distinguish downloaded/snapshotted material from externally linked material.

Do not yet normalize topics across courses.

Do not recommend curriculum changes.

## Primary outputs

For each external/local course source:

- `sources/<source_id>/manifest.yaml`
- `sources/<source_id>/README.md` if useful
- relevant downloaded or snapshotted source material where appropriate
- `analysis/source_summaries/<source_id>.md`

Books registered under `books` in `config/sources.yaml` are direct reference files and require no manifest or separate course-source inventory. Course-to-book topic mapping belongs to Phase 2. Apply the single-baseline convention in `docs/repository_contract.md` to the local course.

## May modify

- `sources/**`
- `analysis/source_summaries/**`
- `scripts/**` when needed for reproducible collection

## Normally read-only

- `config/**`
- `decisions/**`
- `course/**`
- other `analysis/**`
- `output/**`

## Exit criteria

Phase 1 is complete when:

- configured sources have been inventoried;
- source offering/year is identified where practical;
- important inaccessible or ambiguous resources are documented;
- major evidence gaps are identified;
- manifests contain enough provenance to support Phase 2.

---

# Phase 2 — Topic Normalization and Evidence Model

## Goal

Build a common topic vocabulary and structured comparison model across:

- the instructor's existing course;
- the provisional curriculum;
- all configured external reference courses.

This phase organizes evidence. It does not decide the redesigned curriculum.

## Main activities

Create stable normalized topic IDs.

Map source-specific terminology to normalized topics.

Record ambiguity where mappings are uncertain.

Map course topics to relevant chapters, sections, and pages in the configured book. Store these references under the book's configured ID alongside the normalized topic evidence in `analysis/normalized_topics.yaml`, keeping book coverage separate from course coverage or assigned-reading evidence.

For every source/topic combination, capture evidence such as:

- coverage category;
- approximate sequence/order;
- apparent depth;
- assessment presence;
- associated readings;
- project relationship;
- relevant source evidence;
- confidence in inferred properties.

Distinguish direct evidence from inference.

## `analysis/normalized_topics.yaml`

Create this file during Phase 2.

It is the structured source of truth for normalized source-course evidence.

Recommended conceptual structure:

```yaml
topics:
  - id: temporal_difference_learning
    name: Temporal-Difference Learning
    aliases:
      - TD learning
      - TD(0)

    sources:
      silver_rl:
        coverage: explicitly-covered
        sequence: 4
        apparent_depth: substantial
        assessment:
          status: unknown
        evidence:
          - source: ...
        confidence: high
```

Recommended coverage vocabulary:

- `explicitly-covered`
- `brief-exposure`
- `reading-only`
- `assessment-only`
- `not-found`
- `unknown`

Do not use `not-covered` unless the evidence actually supports that conclusion.

Properties such as `apparent_depth`, `estimated_emphasis`, and similar fields should indicate confidence or inference status.

Do not store redesigned-course decisions such as accepted role, mastery, delivery, or decision state here.

## Human-readable comparison

Generate:

- `analysis/topic_matrix.md`
- `analysis/sequencing.md`

`topic_matrix.md` should be a useful human-readable view of `normalized_topics.yaml`, not an independent second source of truth.

It should emphasize:

- source coverage;
- source depth;
- sequence;
- assessment/use;
- notable treatment differences.

It should not independently maintain accepted curriculum decisions.

## May modify

- `analysis/normalized_topics.yaml`
- `analysis/topic_matrix.md`
- `analysis/sequencing.md`
- related Phase-2 analysis files
- `scripts/**`

## Normally read-only

- `config/**`
- `sources/**`, except correcting manifest errors discovered during normalization
- `decisions/**`
- `course/**`
- `output/**`

## Exit criteria

Phase 2 is complete when:

- major topics across sources have stable normalized IDs;
- ambiguous mappings are documented;
- source evidence is represented consistently;
- the provisional curriculum is mapped into the common vocabulary;
- the topic matrix can be generated from structured evidence;
- important evidence gaps are known.

---

# Phase 3 — Curriculum Comparison and Iteration

## Goal

Use normalized evidence to challenge and refine the provisional curriculum.

This is where pedagogical decisions are proposed and iteratively accepted, rejected, or deferred.

## Main activities

Compare the provisional course against:

- the current local course;
- Silver;
- CS234;
- CS285;
- CS224R;
- any subsequently approved reference courses.

Use the course-to-book mappings to answer requested book-grounded gap questions, such as whether important book material is missing. Cite the relevant book sections and distinguish factual coverage from recommendations; presence in the book does not itself require inclusion in the redesigned course.

For each proposed curriculum change, specify:

- change;
- pedagogical rationale;
- relevant evidence;
- role;
- expected mastery;
- status;
- prerequisite implications;
- delivery implications;
- approximate time allocation;
- displaced or compressed content.

Analyze:

- gaps;
- redundancy;
- sequence;
- conceptual dependencies;
- depth;
- contemporary relevance;
- assessment implications.

## Time-budget audit

Run after every substantive revision.

Maintain the current audit in:

- `analysis/time_budget.md`

Use Git history for previous iterations rather than maintaining multiple versioned files.

The audit should evaluate both arithmetic capacity and conceptual density.

Time-accounting inputs are authoritative in `config/course.yaml`:

- Planned contact minutes = planned weeks × lectures per week × lecture minutes.
- Check that planned lectures fit the nominal lecture count after holidays,
  instructor absences and makeups; do not subtract those losses a second time.
- Content capacity = planned contact minutes × `design.planned_content_fraction`
  minus the sum of `minutes` in `design.in_class_overheads`. Apply overheads to their specified weeks,
  after the content fraction, so they do not consume the reserved slack.
- Follow `design.project_presentations_outside_class_hours` when accounting for
  presentations. Sessions outside class consume no live lecture budget but still
  contribute to student workload in the later workload audit.
- Allocate minutes to teaching blocks; overlapping topic IDs within a block
  must not be counted as separate allocations.

Compute totals from these inputs in the audit rather than maintaining another
authoritative copy of the time allowances.

## Video decisions

Video suitability should be considered during this phase because delivery affects the live-time budget and prerequisite sequence.

Record recommendations in analysis first.

Move accepted decisions to:

- `decisions/video_decisions.md`

## Topic decisions

Recommendations may propose topic classifications.

Accepted classifications belong in:

- `decisions/topic_decisions.yaml`

These may include:

- role;
- mastery;
- status;
- delivery;
- assessment expectations;
- prerequisites;
- estimated teaching time;
- rationale.

Changes to accepted decisions must be logged in:

- `decisions/decision_log.md`

## May modify

- `analysis/**`
- `scripts/**`
- `decisions/topic_decisions.yaml` after explicit instructor acceptance
- `decisions/video_decisions.md` after explicit instructor acceptance
- `decisions/decision_log.md` when accepted decisions change

## Normally read-only

- `config/**`
- `sources/**`
- `course/**`
- generated `output/**`

## Exit criteria

Phase 3 is ready to proceed when:

- major curriculum recommendations have been reviewed;
- high-impact additions/removals are resolved;
- included topics have proposed or accepted role/mastery/status;
- topic sequencing is coherent;
- video choices are sufficiently resolved;
- the curriculum passes a realistic time-budget audit;
- unresolved issues are small enough for a formal consistency review.

---

# Phase 4 — Curriculum Freeze and Consistency Audit

## Goal

Determine whether the curriculum is internally coherent enough to freeze before detailed assignment/project design.

## Main activities

Audit the proposed curriculum against:

- course learning outcomes;
- topic roles;
- mastery expectations;
- topic status;
- prerequisite structure;
- sequence;
- approximate time allocation;
- delivery mode;
- planned assessment expectations;
- configured semester capacity.

Check specifically that:

- all Core topics receive sufficient depth;
- mastery expectations are compatible with teaching time;
- prerequisite order is valid;
- videos/readings do not create hidden dependency problems;
- important learning outcomes are supported;
- there are no unresolved high-impact curriculum recommendations.

Generate a formal curriculum consistency audit.

## Primary outputs

- accepted `decisions/topic_decisions.yaml`
- accepted `decisions/video_decisions.md`
- relevant entries in `decisions/decision_log.md`
- `output/audits/curriculum_consistency.md`
- generated `output/topic_details.md`
- generated preliminary `output/lecture_plan.md`

## May modify

- curriculum-related `decisions/**`
- freeze-related `analysis/**`
- `output/audits/**`
- generated curriculum views under `output/**`
- `scripts/**`

## Normally read-only

- `config/**`
- `sources/**`
- `course/**`

## Exit criteria

Curriculum freeze requires:

- included topics have accepted role and mastery;
- status is resolved where relevant;
- sequence and prerequisites are coherent;
- live/video/reading delivery is sufficiently resolved;
- the time budget passes;
- Core depth is considered adequate;
- learning outcomes are covered;
- high-impact curriculum recommendations are resolved.

After curriculum freeze, changes to curriculum structure should be treated as explicit revisions rather than routine iteration.

---

# Phase 5 — Assignments, Project, and Readings

## Goal

Design the high-level assessment and supporting-reading structure around the frozen curriculum.

## Assignment design

Use:

- curriculum learning outcomes;
- accepted mastery expectations;
- external-course evidence;
- existing local assignments;
- realistic student workload.

Decide:

- assignment count;
- purpose of each assignment;
- algorithms/concepts assessed;
- expected implementation depth;
- starter-code strategy;
- approximate workload;
- sequencing.

Record analysis first.

Accepted decisions belong in:

- `decisions/assignment_decisions.md`

Generate:

- `output/assignments.md`

## Project design

Review the existing local project structure and reference-course project formats.

Finalize:

- proposal;
- formulation/design checkpoint;
- progress checkpoint;
- presentation;
- final report;
- grading structure;
- expectations for baselines and evaluation;
- acceptable project types.

Accepted decisions belong in:

- `decisions/project_decisions.md`

Generate:

- `output/project.md`

## Reading design

For each relevant topic/week, consider:

- textbook chapters;
- seminal papers;
- modern representative papers;
- optional surveys/tutorials.

Keep required reading deliberately limited.

Accepted reading choices belong in:

- `decisions/reading_decisions.md`

Generate:

- `output/readings.md`

## May modify

- assessment/project/reading `analysis/**`
- corresponding `decisions/**` after acceptance
- corresponding generated `output/**`
- `scripts/**`

## Normally read-only

- frozen curriculum decisions except through explicit curriculum-revision process
- `config/**`
- `sources/**`
- `course/**`

## Exit criteria

Phase 5 is complete when:

- high-level assignments are accepted;
- project milestones and expectations are accepted;
- required/optional reading strategy is accepted;
- expected assessment/mastery alignment is coherent;
- workload is ready for final audit.

---

# Phase 6 — Syllabus and Course-Design Freeze

## Goal

Integrate curriculum, assessments, project, readings, videos, schedule, and policies into a coherent course design and syllabus.

## Main activities

Generate/update:

- final weekly lecture plan;
- syllabus;
- assessment schedule;
- project schedule;
- required reading/video plan.

Run a total course-design audit covering:

- learning outcome alignment;
- teaching/assessment alignment;
- assignment workload;
- project milestone timing;
- reading/video workload;
- deadline clustering;
- consistency among syllabus, lecture plan, and accepted decisions.

## Primary outputs

- `course/syllabus/**`
- `output/syllabus.*`
- `output/lecture_plan.md`
- `output/audits/workload.md`
- updated `output/audits/curriculum_consistency.md` if necessary

## May modify

- `course/syllabus/**`
- syllabus/design-related `analysis/**`
- generated `output/**`
- corresponding `decisions/**` if explicit final design decisions are made
- `scripts/**`

## Normally read-only

- frozen curriculum decisions except through explicit revision
- `sources/**`
- unrelated teaching artifacts

## Exit criteria

Syllabus/design freeze requires:

- internal consistency across course artifacts;
- acceptable student workload;
- sensible deadline distribution;
- no assessment requiring unavailable prerequisites;
- learning outcomes, teaching, and assessment aligned;
- syllabus matching accepted decisions.

---

# Phase 7 — Teaching Artifact Revision

## Goal

Create or update the actual materials used to teach the finalized course.

## Possible activities

- revise lecture slides;
- create new lecture slides;
- update assignments and starter code;
- update project guidelines and rubrics;
- create video outlines/scripts/material;
- prepare reading lists;
- generate instructor notes;
- revise examples and exercises.

Artifact work should follow the frozen curriculum and design rather than reopening curriculum decisions implicitly.

If artifact development exposes a genuine curriculum problem, log it and return explicitly to the appropriate earlier decision process.

## May modify

- `course/**`
- artifact-related `output/**`
- `scripts/**`
- `decisions/**` only through explicit revision when artifact work reveals a substantive design issue

## Normally read-only

- source evidence
- project governance/configuration unless explicitly revising them

## Exit criteria

Determined artifact-by-artifact rather than through one global completion gate.
