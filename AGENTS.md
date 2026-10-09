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

Most of the generated planning views, reports, audits, and rendered/exported artifacts belong in `output/`. However, certain generated files will be put into `analysis/`

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

### ChatGPT and Claude file ownership

- Every PPTX created by ChatGPT/Codex must end in `_chatgpt.pptx`, including draft and candidate decks. For example: `nuts_and_bolts_chatgpt.pptx` and `nuts_and_bolts.candidate_chatgpt.pptx`.
- Preserve instructor-edited PPTX files. For existing ChatGPT artifacts, refreshing Markdown must only read the `_chatgpt.pptx`; it must not overwrite the deck. Under the current shared content workflow, Claude handles PPTX production and ChatGPT need not create a parallel deck.
- Ignore Claude-created files, including files named with `_claude`, unless they are obviously shared (such as the syllabus) or explicitly marked as shared. Do not read, edit, regenerate, rename, or adopt Claude-specific files as inputs to this workflow.
- Claude follows the mirror rule: files Claude creates use the `_claude` suffix, and Claude ignores ChatGPT-created files (`_chatgpt`) on the same terms.
- Exception for cross-review: when the instructor asks one AI to review the other's work, the reviewer may read the other AI's files for that review only. It must never edit, regenerate, rename or adopt them.
- Shared syllabus, project configuration, accepted decisions and repository governance remain shared authority. If ownership or shared status is unclear and the file is needed, ask the instructor before using it.
- Leave Office lock files (`~$...`) and unrelated files alone. The `_chatgpt` and `_claude` suffixes distinguish authorship, not curriculum acceptance.

### Shared lecture-content conventions (Claude and ChatGPT)

- Shared files: `course/notation_guide.md` (notation for all teaching material), `analysis/phase7_brainstorming.md` (open questions and proposals; both AIs may append, labelled by author and date) `analysis/ideas_backlog.md` (materials and tooling ideas for later course iterations; not accepted or scheduled) and `output/lectures/session_sources.md` (generated per-session index of plan, scope, dependencies, book sections and source pages; regenerate with `python3 scripts/build_session_sources.py`, never edit by hand).
- Use only notation from the notation guide. If content needs a symbol that is missing, or the guide overlaps or is ambiguous (with itself, the book, the old decks or a cited paper), ask or notify the instructor and record the item in the guide's open items. Do not edit the guide without instructor approval.
- Resolve notation and other preparation issues when the current material needs them. Do not require clearing all future open items before starting. Address correctness issues in the material being prepared; retain the instructor-approval rule for notation-guide changes.
- One lecture deck per topic. The deck split is still open in the brainstorming file.
- Claude and ChatGPT produce independent initial content suggestions per topic (deck); a suggestion may propose splitting the deck. Each pulls what is relevant from all sources and, where the previous course has substantial slides for the session, starts from a delta against them; earlier redesigned decks give continuity, not the base (`docs/lecture_workflow.md` step 1). Both AIs decide on content; at least one iteration of mutual cross-review precedes instructor comments. Read the counterpart's AI-specific files only for the scoped review; preserve ownership and do not edit those files. After instructor comments, proceed to more brainstorming or render-ready content as directed. Claude produces the PPTX; there are not two renders. The full per-deck sequence is in `docs/lecture_workflow.md`. Its shared files are an explicit exception to the ownership rule: both AIs may read and edit the deck decision file `decisions/lectures/<deck>.md`, the single review file `analysis/lecture_suggestions/<deck>_review.md`, and the single render-ready content file `course/lectures/weekNN/<deck>_content.md` in their workflow step. Keep findings, responses and resolution status in the shared review; existing AI-specific reviews remain historical. The content file and Claude's YAML are first-render inputs, frozen at the first render; from then on the PPTX is the source, and Claude keeps only the generated review views in step with it. A maintained YAML is made only if the instructor asks.
- Keep lecture planning lightweight, using the accepted lecture plan and existing sources. Do not require an extremely detailed per-lecture plan. Instructor silence on a proposal means neither acceptance nor rejection; only explicit decisions resolve it.
- Both AIs may suggest which old slides (`sources/current_course/`) to reuse. The instructor decides by editing the PPTX, which is the deck's source; Claude, as the sole renderer, regenerates its review views.
- Suggest new preliminary or detailed planning material only when the information does not already exist in the accepted plan, decisions, instructor sources or analysis.
- Equations: reuse existing PowerPoint equations from the old decks where possible; use LaTeX where they are not enough.
- Lecture content follows `decisions/topic_decisions.yaml` (session scope, mastery, exclusions, minutes, worked activity). A content need that conflicts with it is raised with the instructor, not silently resolved.

Prefer structured Markdown and YAML that can be inspected and diffed.

Prefer reproducible scripts for repeated extraction, normalization, auditing, or output generation.

Make small, reviewable curriculum iterations rather than rewriting the whole course without justification.

At the end of a curriculum iteration, summarize:

1. proposed changes;
2. supporting evidence;
3. unresolved decisions;
4. time-budget result.
