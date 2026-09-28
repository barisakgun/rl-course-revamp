# RL Course Revamp

This repository supports the redesign of a university Reinforcement Learning course.

The goal is to build a course that preserves strong RL foundations while providing coherent coverage of deep RL, modern RL methods, model-based and offline RL, and RL-based LLM post-training.

The redesign is evidence-informed rather than based on copying any single existing course. Public teaching materials from several established RL courses are collected and compared with the current course and a provisional redesign. These comparisons are then used to make explicit decisions about topic selection, depth, sequencing, delivery, assessment, readings, and project structure.

## Main goals

The project aims to:

- collect and organize relevant material from selected RL courses;
- compare those courses with the existing course and provisional redesign;
- build a normalized topic taxonomy across courses;
- map course topics to the reference book and support book-grounded questions and gap analysis;
- decide which topics should be Core, Exposure, or Extension material;
- define expected mastery and current research/practice status for each topic;
- maintain a realistic lecture-time budget throughout curriculum revision;
- decide which material is best delivered live, by video, or through reading;
- finalize assignments and the semester project structure;
- select appropriate textbook chapters, seminal papers, and modern readings;
- generate a coherent lecture plan and syllabus;
- later update the actual teaching materials to match the finalized design.

## Course design constraints

The current design assumes:

- 13 planned teaching weeks;
- two lectures per week;
- deliberate slack rather than planning every available minute;
- a balance between fundamental and modern RL;
- a semester-long project;
- assignments that help students achieve the relevant learning outcomes;
- no mandatory LLM-specific assignment;
- optional LLM-based project directions;
- approximately two supporting videos where asynchronous delivery is pedagogically useful.

Detailed constraints and learning outcomes are defined in `config/course.yaml`.

## Reference courses and book

The initial comparison set includes:

- David Silver's Reinforcement Learning course;
- Stanford CS234;
- Berkeley CS285;
- Stanford CS224R;
- Pieter Abbeel's six-lecture Foundations of Deep RL series;
- the Sutton slide collection;
- the instructor's existing RL course.

Sutton and Barto's *Reinforcement Learning: An Introduction* is also available as a local reference book. Course topics will be mapped to its chapters, sections, and pages. It can support book-grounded questions, including questions about potentially missing material, without making book coverage an automatic curriculum requirement.

Configured courses, books, paths, and roles are defined in `config/sources.yaml`. The book is referenced directly and does not need a manifest or its own source directory. See `docs/repository_contract.md` for the evidence and mapping rules.

Additional courses may be added later without changing the overall workflow.

## Repository structure

```text
rl-course-revamp/
├── AGENTS.md
├── README.md
│
├── config/
│   ├── course.yaml
│   ├── sources.yaml
│   ├── taxonomy.yaml
│   └── provisional_plan.yaml
│
├── docs/
│   ├── repository_contract.md
│   └── workflow.md
│
├── sources/
│   ├── <source_id>/
│   └── RLbook2020.pdf
│
├── analysis/
│
├── decisions/
│
├── course/
│
├── output/
│
└── scripts/
```

The main repository layers are:

- **`config/`** — course constraints, configured sources, taxonomy, and provisional curriculum;
- **`docs/`** — repository structure and workflow documentation;
- **`sources/`** — external-course evidence, existing local course material, and the reference book;
- **`analysis/`** — normalized evidence, comparisons, audits, and recommendations;
- **`decisions/`** — accepted, rejected, and unresolved curriculum/design decisions;
- **`course/`** — editable teaching materials;
- **`output/`** — generated plans, reports, audits, and rendered/exported artifacts;
- **`scripts/`** — reproducible collection, normalization, auditing, and generation utilities.

See `docs/repository_contract.md` for authoritative-file and source-of-truth rules.

The generated comparison views and working time-budget audit explicitly listed in `docs/workflow.md` remain under `analysis/`; other generated outputs follow the usual `output/` convention.

## Workflow

The redesign proceeds in controlled phases:

0. **Repository sanity check**  
   Validate repository structure, configuration, consistency, and readiness.

1. **Source collection and inventory**  
   Inventory teaching materials from the configured external and local course sources. The registered book requires no manifest.

2. **Topic normalization and evidence model**  
   Build a common topic vocabulary and structured comparison across courses, including references to the relevant book material.

3. **Curriculum comparison and iteration**  
   Compare the provisional curriculum with the evidence, propose changes, and repeatedly audit the time budget.

4. **Curriculum freeze and consistency audit**  
   Finalize topic selection, sequencing, role, mastery, status, delivery, and approximate allocation.

5. **Assignments, project, and readings**  
   Design assessments and supporting material around the frozen curriculum.

6. **Syllabus and course-design freeze**  
   Integrate the complete design and audit alignment and student workload.

7. **Teaching artifact revision**  
   Update lecture slides, assignments, project documents, videos, readings, and related materials.

Detailed phase definitions, modification permissions, outputs, and exit criteria are defined in `docs/workflow.md`.

## Design philosophy

The project follows several broad principles:

- foundations take priority over algorithm catalogs;
- modern popularity does not automatically make a topic Core;
- historical importance does not automatically justify detailed coverage;
- pedagogical role and current research/practice status are separate;
- external courses provide evidence rather than votes;
- topic additions must account for the material or time they displace;
- arithmetic schedule fit is not sufficient if the resulting lectures are too dense;
- live teaching time should emphasize material that benefits from explanation, derivation, examples, and interaction;
- required readings and videos count toward student workload;
- assessment should reflect the expected level of mastery.

The complete pedagogical principles are maintained in `decisions/course_principles.md`.

## Sources and provenance

External course materials are used for curriculum analysis and comparison.

The local materials are treated as one baseline course, even when files have different years or course labels. Identify artifacts by their content and retain file provenance, following `docs/repository_contract.md`.

The repository should preserve source provenance, including URLs, course offerings where identifiable, retrieval dates, and resource types.

Where possible, external material should be linked or indexed rather than indiscriminately mirrored. Copyright, licensing, access restrictions, and site policies should be respected.

Absence of a topic from publicly available material should not automatically be interpreted as evidence that the topic was not taught.

## Decision process

Analysis and accepted decisions are deliberately separated.

External evidence and recommendations belong under `analysis/`.

Accepted curriculum and course-design decisions belong under `decisions/`.

Generated summaries and plans under `output/` or `analysis/` are not independent sources of curriculum truth.

This separation is intended to make curriculum changes reviewable, traceable, and reproducible.

## Current status

The repository sanity check has been completed and its setup clarifications are being incorporated. Phase 1 source collection has not begun and requires an explicit request.

## Codex usage

Codex should read `AGENTS.md` before performing substantive work.

`AGENTS.md` identifies the additional project-context files that must be read and defines the permanent behavioral rules for work in this repository.

Individual prompts should normally request one workflow phase at a time. Codex should not automatically advance to subsequent phases.
