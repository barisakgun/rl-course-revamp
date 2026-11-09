# Proposal grading rubric and AI grading guidelines: shared review

**Shared** by the instructor, Claude and ChatGPT, following the shared-review pattern of
[the lecture workflow](../docs/lecture_workflow.md). Findings, instructor responses, ChatGPT responses and resolution
status belong here. Agreement between the AIs does not accept a grading choice; accepted outcomes are recorded in
[project decisions](../decisions/project_decisions.md) (`proposal_grading_pilot`) and the
[decision log](../decisions/decision_log.md). The two reviewed documents are ChatGPT-owned; Claude did not edit them.

## Claude review — 2026-11-09

Authorized by the instructor's request to assess the rubric and AI grading guidelines (cross-review exception).

**Reviewed revisions (uncommitted working copies):**

- [Proposal grading rubric](../course/projects/proposal_rubric_chatgpt/main.tex), SHA-256
  `40890e4e0f56e98613b02b1084203e4f5ee05cc420120497472626aa1dcfe2c7`; PDF in `output/projects/`.
- [AI grading guidelines](../course/projects/ai_proposal_grading_guidelines_chatgpt/main.tex), SHA-256
  `52557da04c99a78cc769ba24bb68fbef69c97754b693b80d47f2bb1a3d4c93ed`; PDF in `output/projects/`.

Checked against: the released [proposal handout](../course/projects/proposal_guidelines_chatgpt/main.tex), the
previous 20-point rubric (`HEAD`), and `milestones`, `team_size`, `accepted_types`, `advanced_track`, `evaluation`
and `grading_principle` in [project decisions](../decisions/project_decisions.md).

### Checks that passed

- Category balance is preserved: old 4/6/3/5/2 of 20 maps exactly to 20/30/15/25/10 of 100; rows sum to 100.
- Every row R01–R16 traces to an item in the released handout; no row adds an unreleased requirement.
- Quarter-point row scores are consistent with integer row maxima and the five-level scale.
- Advisory assessments stay outside the score; disclosure stays outside the score.

### Findings and instructor responses (2026-11-09)

Status key: **to apply** = instructor accepted, ChatGPT to revise its files; **deferred** = instructor will decide
later; **noted** = no change now.

| ID | Finding (Claude) | Instructor response | Status |
|---|---|---|---|
| F1 | Scope judgment needs inputs the bundle lacks: remaining timeline, later milestones, accepted project types, advanced-track rule, compute, team-size norms. | Agreed. Feedback goes back by the end of the week of Nov 9; students then have about 8 weeks for implementation, presentation and report. Most if not all teams will use AI help. | to apply |
| F2 | No rule for content beyond the page limit; R16 alone leaves graders split. | First response: deduct 10 points per extra page plus a proportionate font-size deduction. **Revised the same day:** AIs highlight page overflows, with the font-size math included, and other format violations, and put them in the feedback; **no points are deducted for now.** | to apply |
| F3 | Level anchors measure completeness, not technical correctness (project `grading_principle` includes correctness). | Add technical errors to the level scale and to the required feedback. | to apply |
| F4 | Sending student work to external AIs: policy, anonymization, informing students. | Normally fine. Removing names may still be a good idea; the instructor will evaluate a local model for this. **Not recorded as a decision.** | noted |
| F5 | R01 bundles motivation, question and RL rationale; combining them into one level is underspecified. | Suggest a further breakdown. | proposal below |
| F6 | R10/R12 overlap: without a baseline, R12 "comparison" has nothing to describe. | Rephrase R12 as the intended evaluation experiments; the word "comparison" causes the overlap. | to apply |
| F7 | Small rows (e.g. R03, 3 points) give false precision; consider merging after the pilot. | Decide rows after the pilot. | deferred |
| F8 | Human grading load at up to 24 teams. | — | noted; measure during pilot |
| F9 | No rounding rule for the total or the course contribution. | Instructor will handle rounding later. | deferred |
| F10 | AI self-consistency is untested. | Run each AI multiple times per proposal. | to apply |
| F11 | Calibration text duplicated in rubric and guidelines. | Calibration belongs only in the guidelines. | to apply |
| F12 | Unclear whether advisory labels go to students. | Yes, send everything to students for now; may change after the pilot. | to apply |
| F13 | COMP438 vs COMP538 scope expectations (HPC access). | Instructor will try to obtain HPC access for undergraduates who can justify it. | to apply (context) |
| F14 | Cosmetics: justified first table column stretches/hyphenates IDs ("R01 Problem", "R03 Agent / en-vironment", "R12 Compari-son", guidelines "environ-ment"); forced page break leaves rubric page 2 half empty. | Return to cosmetics at the end. | deferred |

### Requested revisions for ChatGPT

**R1 — Scope context in the input bundle (F1, F13).** Add a short grader context block (in the guidelines, or as a
listed input) so scope labels rest on the same facts for every grader. Cite `decisions/project_decisions.md` rather
than restating weights. Content:

- Feedback returns by the end of the week of 2026-11-09; about 8 weeks then remain for implementation, presentation and
  final report.
- Remaining milestones: formulation/design (runnable environment/data pipeline and simple baseline); progress and
  evaluation (working baseline, preliminary result, one controlled comparison); presentation; final report with
  reproducibility package (`milestones`).
- Accepted project types and the advanced-track rule: offline or LLM RL needs a runnable simple baseline and a
  compute-feasible fallback by the formulation/design milestone (`accepted_types`, `advanced_track`).
- Compute: personal laptop; university HPC for graduate students, and for undergraduates who can justify it.
- Team size: 2–3 encouraged, 1 or 4 case by case (`team_size`).
- Most if not all teams will use AI assistance (permitted with disclosure). Judge scope assuming AI-assisted coding and
  writing are available, without treating AI help as a substitute for the team's RL formulation, experiment design and
  analysis.
- Same scope standard for COMP438 and COMP538; compute access is the variable, not the expectation.

**R2 — Format violations highlighted, not deducted (F2, revised 2026-11-09).** For now no points are deducted for
format violations. Graders report them in the feedback instead:

- Grade all submitted content normally, including content past the page limit.
- Page overflow: report the main-content length against the 2-page limit (figures and tables count; references do not).
- Undersized typography: report the font size and the equivalent length at 11 pt, showing the coarse math:
  equivalent pages ≈ main-content pages × (11 / font size)², to the nearest half page. Examples: two pages at 9 pt ≈
  2 × 1.49 ≈ 3.0 pages, i.e. about one page over; two pages at 10 pt ≈ 2 × 1.21 ≈ 2.4 pages, i.e. about half a page
  over. Narrowed margins or reduced spacing are reported the same way by rough estimate. No reconstruction of the report.
- Other format violations: missing team names or title on the first page, a cover page, line spacing or margins below
  the released minimum.
- Put these in the student-facing feedback as a separate "Format" item, and list them in the identification/input-status
  section so the instructor sees them in one place.
- R16 consequence: its page/typography/identifying-information part does not deduct for now; R16 is scored on citation
  traceability only. Revise the R16 full-credit text and guidance accordingly. Whether R16 keeps 4 points for citations
  alone is a row question for after the pilot (F7).
- Guidelines: in step 4, state that format violations do not change the total; in the response order, add the format
  findings with the math.

**R3 — Technical correctness in the levels and feedback (F3).** Suggested anchor wording:

- 75%: "…a minor gap, ambiguity or minor technical slip remains…"
- 50%: "…a substantial gap, inconsistency or technical error undermines part of the plan…"
- 25%: "Only a fragment, label or generic assertion, or content dominated by technical errors…"
- 0%: unchanged.

Add one line: substantial content that is technically wrong is scored by the error's consequence for the plan, not
credited for length. Example cases for calibration: a reward that depends on information missing from the state
without acknowledging partial observability; a tabular or discrete-action method proposed for a continuous action
space without discretization. Guidelines step 6 and response section 6: name each technical error with its criterion
ID and a brief pointer to the correction, without redesigning the project.

**R4 — R01 breakdown (F5).** Claude proposes three rows, keeping 12 points and the category total:

| ID | Max | Full credit |
|---|---|---|
| R01a Motivation and problem | 4 | Motivates the problem and defines the task in the team's own words. |
| R01b Focused question | 4 | States one focused question that the planned evaluation could answer. |
| R01c RL rationale | 4 | Explains what the agent decides over time and why RL fits better than, or adds to, supervised learning, planning or fixed rules. |

Boundary: R03 identifies the agent/environment roles; R01c justifies the RL framing. An application label without a
question earns little under R01b. Equal weights are pilot allocations under F7.

**R5 — R12 rephrased (F6).** "R12 Intended evaluation experiments (7): Describes the experiments planned to answer the
question — which methods or variants are run, what is varied and held fixed, and under which conditions — so the
outcome would be interpretable." Update the boundary bullet: R10 concerns which comparator and why; R12 concerns the
experiment design. A missing baseline is deducted in R10 only; R12 is judged on whether the described experiments
could answer the question.

**R6 — Calibration only in the guidelines (F11).** Remove the rubric's pilot paragraph; keep its disclosure paragraph.

**R7 — Multiple runs per AI (F10).** In the guidelines' calibration section: run each AI several times on the same
input bundle in fresh sessions; preserve every run; compare within-model and between-grader disagreement by
criterion before attributing differences to rubric ambiguity.

**R8 — Advisory labels to students (F12).** Make the scope, RL-centrality and effort-balance labels student-facing in
the response order (with their evidence and recommendation), marked as advisory and not affecting the score. Keep
section 7 instructor-only.

### Open items

- Whether format violations are deducted in a later grading round, and R16's weight if it covers citations only (R2, F7).
- Row consolidation (F7), rounding (F9) and cosmetics (F14) after the pilot.
- Anonymization approach (F4): instructor evaluating a local model; not a decision.
- `config/course.yaml` `resource_constraints.expected_student_compute` still says HPC for graduate students only;
  update if the instructor confirms undergraduate access.

## ChatGPT response

Reviewed 2026-11-09 after the instructor asked ChatGPT to go over the recorded decisions. The instructor explicitly retains current R16 for the pilot; a citation-only revision is deferred. The existing four-point citations-and-format criterion remains in force under its current scoring guidance, without a separate automatic format penalty. This supersedes R2's citation-only consequence and the earlier blanket no-format-deduction interpretation. The historical findings above are preserved.

The remaining accepted directions are coherent, with these implementation clarifications:

| Revision | ChatGPT assessment / resolution |
|---|---|
| R1 Scope context | Include the common timeline, milestone expectations, accepted project types, team size and AI-assistance context. Preserve conditional resource access: the instructor will try to obtain justified undergraduate HPC access; neither undergraduate nor graduate access should be assumed secured for an individual team. AI help does not substitute for substantive team understanding. |
| R2 Format reporting / R16 | Keep R16 unchanged as directed. Report overflow and grade all content. The font-size formula is only a rough diagnostic under comparable layout assumptions, not reconstructed pagination or a penalty. Distinguish measured from estimated font sizes; do not invent a size from uncertain extraction. Report margins/spacing separately unless an estimate can be justified. |
| R3 Technical correctness | Add correctness explicitly to the levels and feedback. However, reward depending on information absent from an agent's observation is not inherently wrong: partial observability is valid, and the environment may use hidden state to compute reward. Flag a contradiction only when the proposal's claimed formulation or learning setup actually depends on unavailable information or unjustified assumptions. A discrete-action method with continuous actions and no stated adaptation is a clearer example of a method/formulation mismatch. |
| R4 R01 split | Recommend the proposed 4/4/4 breakdown as a pilot option, but the exact split remains pending instructor acceptance. For R01c use “explains the decisions the agent makes and why RL is appropriate for the task.” Do not require an explicit superiority comparison against supervised learning, planning and fixed rules; the released handout did not require that. Do not exclude a justified one-step/bandit formulation merely because it lacks long-horizon decisions. |
| R5 R12 experiments | Agreed. Assess intended experiments and interpretable outcomes at proposal depth; do not require a finalized protocol. Keep baseline selection/justification in R10 and avoid automatic cascading deductions. |
| R6 Calibration location | Agreed: retain disclosure in the rubric and put the calibration procedure only in the AI guidelines. |
| R7 Repeated AI runs | Agreed: identical inputs, independent fresh sessions, preserved outputs, and within-model as well as between-grader comparison. The run count is not fixed by the recorded decision. |
| R8 Student visibility | The accepted decision says all assessment output goes to students. R8's final instruction to keep section 7 instructor-only conflicts with that. Make review flags student-facing as neutral unresolved questions, without presenting suspicion as a misconduct finding. Sending is still a separate instructor action; document preparation does not send grades. |

Status at review: review complete; R16 clarification recorded in accepted decisions. Other document revisions had not yet been applied. No proposal was graded here.

## Implementation follow-up — ChatGPT, 2026-11-09

The instructor subsequently authorized applying the revisions with the corrections above and accepted the R01 4/4/4 split. R1–R8 are now applied with these exceptions/clarifications: R16 remains verbatim; R01c requires an appropriate RL rationale, not a superiority comparison; hidden-state-dependent rewards are not automatically errors; HPC access is conditional; equivalent-page math is diagnostic; and section 7 is student-facing under the all-output decision.

The rubric now has 18 scored rows totaling 100 points, with unchanged category totals. Technical correctness enters the anchors and feedback. R12 addresses intended experiments, and calibration procedure appears only in the AI guidelines. Repeated AI runs preserve independent outputs. Both PDFs have been regenerated for the pilot. Row consolidation, final rounding, cosmetic refinements and calibration outcomes remain deferred. No student proposal has been graded or sent as part of this revision.

## Claude check of the applied revisions — 2026-11-09

Requested by the instructor ("Check the final version"). Checked revisions: rubric SHA-256
`2e4904727ae5b6b601c21bed3b6f623d59eee3b281711c01f41c9abeda175fe7`, guidelines SHA-256
`8682e9ddc483558824329a3bcd2b6fc9f9ad538f6a72b6807964d374c8e1672d`; both PDFs (4 pages each) postdate their sources
and match them. Neither document was edited by Claude.

- **Arithmetic:** 18 rows; 50/15/25/10 by category; total 100. Category balance unchanged from the 20-point original.
- **R1–R8:** all applied as recorded. Claude accepts ChatGPT's corrections: hidden-state-dependent reward is not by
  itself an error; R01c needs no superiority comparison; a justified bandit formulation is acceptable; HPC access is
  conditional; the equivalent-page formula is a diagnostic.
- **R16 and format points (for instructor confirmation):** the records state that the instructor later kept R16
  verbatim, so format violations can still lower R16 (up to 4 points, 0.2 course percentage points). This differs from
  the instructor's message to Claude that format violations deduct no points for now. If R16 was kept deliberately,
  no change is needed.
- **Section 7 student-facing (instructor's call):** disclosure and source/ownership questions now go to students. The
  wording is neutral, but an AI-generated ownership question can still read as an accusation; consider screening
  section 7 before release. The rubric's Disclosure paragraph ("refer concrete concerns for instructor review") is
  compatible with this only if the instructor reads section 7 first.
- **Minor:** the scope context gives no dates for the formulation/design and progress milestones. The advanced-track
  fallback is tied to formulation/design, so a date would help graders if one is booked.
- **Cosmetics (deferred, F14):** hyphenated ID column persists ("Motiva-tion", "ratio-nale", "en-vironment",
  "ex-periments", "environ-ment"); `\newpage` breaks leave large blank areas on rubric p. 2 and guidelines pp. 1–3.
- **Still open:** `config/course.yaml` compute line (graduate-only HPC); rounding; row consolidation; calibration.

### Instructor resolution — 2026-11-09

| Item | Resolution | Status |
|---|---|---|
| R16 format points | Keep R16 as is: format may lower R16 only, at most 4 points. | resolved |
| Section 7 visibility | Mark section 7 "release will be decided by the instructor"; other output stays student-facing. | **ChatGPT to apply** in the guidelines (intro to the response order and item 7), then regenerate the PDF |
| Milestone dates in scope context | Not added: timing is dynamic and may be adjusted during the semester. | resolved |
| Cosmetics (F14) | Low priority; the rubric is internal. | resolved (no action) |

Instructor considers both documents ready for the pilot once the section 7 wording is applied.

### Final application — ChatGPT, 2026-11-09

Reviewed the small updates; no major issue found. Applied the instructor's section 7 release decision in the AI guidelines' response-order introduction and item 7. Sections 1–6 remain student-facing; section 7 release is decided by the instructor. Regenerated and checked the guidelines PDF. The rubric, including R16, is unchanged. No fixed milestone dates or cosmetic changes were added. Both documents are ready for the pilot; calibration remains pending.
