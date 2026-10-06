# Decision Log

## 2026-10-06 — Clarification: scope of content suggestions and roles

- Authority: instructor instruction in the Claude conversation, restating the process given to ChatGPT; this fills gaps in the entry below.
- Each AI provides initial content suggestions per topic (deck); a suggestion may propose splitting the deck.
- Both AIs decide on content; Claude is the sole PPTX renderer. Old-slide reuse is still decided by the instructor editing the PPTX; Claude keeps the deck's content source in step with the edited deck. ChatGPT maintains no parallel deck or deck source.
- Suggest new preliminary or detailed planning material only when the information does not already exist in the accepted plan, decisions, instructor sources or analysis. A way to compile existing sources into one place for easier access may be proposed.
- Process and role clarification only; no curriculum, assessment, timing or workload change.

## 2026-10-06 — Lecture-content pilot and deck 0 acceptance

- Authority: instructor feedback on the Phase 7 workflow proposal in the ChatGPT conversation.
- Accept the current Claude deck 0 (nuts and bolts): `course/lectures/week01/nuts_and_bolts_claude.pptx`, SHA-256 `bb87519e5a6fa2d364d47b77651435f7e5df484a2602ccdc4e922a6df069a951`. This identifies the accepted saved version, not future edits or the earlier ChatGPT deck/candidate. No Markdown extraction or deck regeneration is requested. Recording instructor acceptance does not claim a new technical/visual review or amend the frozen syllabus and curriculum decisions.
- Use session 1.1 (`formulate`) as the content-workflow pilot. Its accepted scope and teaching allocation remain unchanged. The pilot choice does not approve ChatGPT's previous two-session content outline or a particular running example.
- Prepare two independent initial content suggestions, followed by at least one iteration of both AIs checking each other's work, then instructor comments. After those comments, decide whether to continue brainstorming or develop content detailed enough to render. Claude handles PPTX production; two renders are not required.
- Keep lecture planning lightweight and reuse the existing sources and accepted lecture plan. Do not impose an extremely detailed plan on each lecture. Cross-comparison of render-ready content remains deferred for evaluation after the pilot, not an adopted mandatory step.
- Resolve notation and other preparation issues when the material needs them, not all in advance. The instructor accepts action/advantage distinction through context and permits `A_t`; resolve notation-guide O1 accordingly. Other notation questions remain deferred until needed, with instructor approval still required for changes to the guide.
- Unanswered proposals are neither accepted nor rejected. Preserve them as open recommendations. Deck boundaries, a compulsory slide structure, review-file format and other unaddressed implementation suggestions remain unresolved.
- These are artifact acceptance and Phase 7 working conventions. No topic, mastery, assessment, teaching-time or student-workload revision is made; no curriculum time-budget rerun is needed for this documentation change.

## 2026-10-05 — Shared lecture-content conventions for Claude and ChatGPT

- Authority: instructor direction while comparing Claude and ChatGPT lecture workflows.
- One lecture deck per topic; the exact deck split is open in `analysis/phase7_brainstorming.md`.
- Claude and ChatGPT draft independently and review each other's work on request (read-only cross-review); the instructor makes the final decision.
- Both AIs may suggest reuse of old slides; the instructor decides by editing the PPTX, and each AI updates its own content source from it.
- Equations: reuse existing PowerPoint equations where possible; LaTeX where they are not enough.
- Adopt the shared `course/notation_guide.md`. Its open overlap items await instructor resolution; authors ask when it is missing a symbol or is ambiguous.
- `sources/current_course/NOTES_FOR_NEXT_YEAR.txt` is not used as guidance.
- This is a Phase 7 working convention. It does not change curriculum, assessment, timing or workload decisions.

## 2026-10-05 — ChatGPT file suffix and separate Claude work

- Instructor renamed the edited working deck to `course/lectures/week01/nuts_and_bolts_chatgpt.pptx` and requests the `_chatgpt` suffix on all subsequently created ChatGPT PPTX files, including candidates.
- Point the Markdown exporter and current navigation at the renamed deck. Generated views follow the matching basename. Preserve the deck and Office lock files without modification.
- Ignore Claude-created files unless obviously shared, such as the syllabus, or explicitly marked as shared. Ask when a needed file's ownership/shared status is uncertain. This does not undo prior work in either workflow.
- These are naming and collaboration rules only. No curriculum, assessment or artifact acceptance change is inferred.

## 2026-10-05 — Instructor edits lecture PPTX directly

- Authority: instructor prefers viewing and editing the PPTX, requests refreshing Markdown from it if practical, and asks that generators preserve edited files.
- Adopt PPTX-first lecture artifact editing. The nuts-and-bolts working file remains `course/lectures/week01/nuts_and_bolts.pptx`; its derived Markdown view moves to `output/lectures/week01/nuts_and_bolts.md` and refreshes through `scripts/pptx_to_markdown.py`.
- Remove the former independently editable Markdown draft from `course/`; its earlier version remains in Git history. Protect the working PPTX from generator replacement. Reconstruction proposals use separate `.candidate.pptx` files, not automatic promotion into `course/`.
- This accepts an editing workflow, not the contents of the current deck or a curriculum/policy revision. Current saved slide text and notes are extracted as-is; no slide changes, new pacing judgment or artifact acceptance is inferred. Visual previews must be refreshed separately after PowerPoint edits.

## 2026-10-04 — Phase 7 started with Week 1 nuts and bolts

- Authority: instructor requests beginning Week 1 with the nuts-and-bolts material, permits a planning start, and supplies the source PPTX.
- Start artifact revision with a syllabus-aligned slide-content draft and revision plan. This does not accept a new curriculum, policy, assessment, timing or workload decision.
- Preserve the supplied PPTX under sources and the frozen syllabus DOCX/PDF. The first deliverable is editable Markdown under `course/lectures/week01/`; PowerPoint editing and visual verification remain pending.
- Mark Phase 7 in progress. Phase 6 remains closed and actual-date calendar/operational finalization remains deferred as previously directed.

## 2026-09-30 — Align generators and views with the frozen syllabus

- Authority: instructor explicitly requests aligning generators and Markdown views with the final syllabus. The DOCX/PDF remain unchanged; Phase 6 stays closed and Phase 7 has not started.
- Consolidate the accepted artifact identity and freeze scope in `decisions/syllabus_decisions.yaml`; its fingerprints are those recorded at the September 29 freeze. The exporter reads the final DOCX, preserves its wording, and refuses changed frozen artifacts rather than updating fingerprints automatically.
- Reconcile accepted records with the actual final wording: four assignments/best-three remain the current internal design, while the syllabus reserves discretion to change the count and drop the lowest if more than three are offered. A changed count requires a renewed aggregation/alignment/workload review; no new count or formula is adopted here.
- Record the final project disclosure/report obligation and writing-quality policy in project decisions. The final syllabus retains the assignment-specific one-shot/few-shot no-credit rule; it does not extend it to project coding. Concrete report instructions and rubrics remain deferred.
- Detailed dates, project lengths, assignment windows and video rules omitted from the concise syllabus remain internal planning decisions, not additional published commitments. No topic, mastery, prerequisite, teaching-time allocation or grade weight changes; the unchanged time/workload audits remain applicable and are rerun during alignment.
- Replace stale draft checks with final-file identity, published-fact and Markdown consistency checks. Preserve the old visual-review record explicitly as historical draft evidence; do not claim a new visual review, final-PDF layout verification or upload.

## 2026-09-29 — Instructor freezes syllabus; Phase 6 closed

- Authority: instructor confirms incorporating the editorial suggestions, completing the PDF conversion for upload, and explicitly directs marking the syllabus frozen. Phase 6 is closed by instructor acceptance; Phase 7 will be addressed later and has not started.
- Frozen student-facing artifacts: `course/syllabus/syllabusFall26.docx` and its instructor-produced `course/syllabus/syllabusFall26.pdf`. These supersede the earlier draft as the syllabus for this offering. Upload is not claimed completed.
- Preserve the instructor's concise syllabus and deliberate flexibility on timing and requirements. Do not repopulate it from the older detailed draft or internal planning views.
- Scope of freeze: the instructor-approved syllabus. Actual-date calendar mapping and operational scheduling remain deferred until after Phase 7, retaining the post-Week-2 checkpoint. Existing workload uncertainty, task pilots, rubric/example preparation, staffing and grading-turnaround follow-ups remain tracked; they are not newly resolved by this freeze.
- Prior Phase 6 workload/design audits and the subsequent editorial review were completed. The instructor performed the final edits and PDF conversion. No new agent render, final-PDF verification, syllabus modification or report regeneration was requested or performed in this closeout.
- Repository follow-up before reusing generators in Phase 7: reconcile final syllabus wording with structured policy records, update the old draft-path/export assumptions, and distinguish historical draft verification from final-artifact verification. Do not infer that every suggested alternative was adopted or reverse instructor edits to satisfy stale checks.
- Frozen artifact fingerprints (SHA-256):
  - `course/syllabus/syllabusFall26.docx`: `71a332e99ca52eb41da303f0dbec0e07d310224f2339114d06c109ebeb337fb1`
  - `course/syllabus/syllabusFall26.pdf`: `687b7f5e0196d059a3d43f67894067bf04d7ca4c10187cc5bd6b1556111e6598`

## 2026-09-29 — Phase 6 provisional integration prepared for review

- Completed the authorized generator repairs, provisional-design/workload audit and supplied-syllabus revision. No teaching scope, mastery, assessment weight or week target was changed.
- Preserved the supplied catalog/prerequisite text verbatim and retained administrative policies. Reconciled syllabus assessment/delivery text with existing decisions; changed the obsolete phrase “early final” to “early exam” because no final exam is required.
- Read class hours and room from the supplied DOCX rather than requesting them again. Actual-date mapping remains deferred after Phase 7; this discovery does not book makeup or assessment dates.
- Reviewed all five rendered syllabus pages and recorded file-hash-bound verification in analysis. Workload ranges remain unpiloted; the retained final-report late-day policy creates a grading-turnaround follow-up, not a new policy decision.
- The provisional integration package is ready for instructor review. Final syllabus/design freeze is not declared and Phase 7 has not started. The possible later workflow phases remain a note for future discussion.

## 2026-09-28 — Phase 6 integration resumed

- Instructor explicitly authorizes the Phase 6 plan, lifting the syllabus/audit hold: repair generators, audit the provisional design, inspect the supplied DOCX, review findings, revise the syllabus and verify consistency after editing.
- Calendar finalization and operational follow-up remain deferred until after Phase 7, retaining the post-Week-2 checkpoint. Unknown dates must be reported as limitations rather than passed checks.
- No curriculum, grading or assessment-scope change is authorized by this integration step. Final syllabus/design freeze remains a separate instructor decision; Phase 7 is not started.

## 2026-09-28 — Calendar finalization deferred until after Phase 7

- Instructor directs that completion of actual-date calendar mapping and its operational follow-up be left until after Phase 7. Retain the existing post-Week-2 registration/attendance checkpoint; this work is no longer an immediate Phase 6 step. Accepted week-level targets, prerequisites and full 21-day assignment windows remain binding.
- Note for later workflow review: consider additional phases for work after lectures start, including calendar/staffing finalization and affected audit reruns. No new phases are defined or adopted now.
- Instructor suggests the Phase 6 order of generator fixes, audit, DOCX inspection, review of artifacts/issues, then syllabus revision, leaving final sequencing to the assistant. This is a planning note, not an instruction to execute those steps now; the syllabus/audit hold remains in effect.
- Phase 6 can assess the provisional design with explicit calendar limitations. Final syllabus consistency must still be verified after editing; a pre-edit review does not establish final syllabus/design freeze.

## 2026-09-28 — Schedule provisionally frozen; syllabus and audit held

- Instructor freezes the reviewed week-level schedule until it is reopened after the first two weeks of classes, once attendance and registration stabilize. Exact dates remain unbooked; this is not final syllabus/design freeze.
- Accept A1 release Week 4 / due early Week 7; A2 Week 6 / Week 9; A3 Week 8 / late Week 11; A4 Week 12 / Week 15. Retain 21-day windows and taught prerequisites, with the A1 early-week issue explicitly deferred to calendar mapping.
- Accept MT1 Week 6, MT2 Week 10 and MT3 Week 13; exam coverage and 15% weights unchanged.
- Project: proposal Week 4, design late Week 7, progress early Week 11, presentations Week 14, final report Week 16 subject to one week before letter grades. Weights, lengths and scope unchanged.
- Accept online, recorded, TA-led presentations with TA/group grading. Exact slots, staffing and grading split remain unresolved; keep three two-hour slots and own-slot attendance. Regular-semester template unchanged.
- Update capacity inputs to two assumed unavailable holiday slots and three makeups (October/November/December), retaining 26 lectures. December 31 loss is a planning assumption, not verified holiday status. No lecture scope or minute change.
- Instructor explicitly defers syllabus editing and the full audit. Record completeness/handoff information and render only the schedule snapshot; do not run audit-bearing generators or edit the DOCX.

## 2026-09-28 — Regular-semester timing and current timing review

- Record the instructor’s regular-semester template: midterm 3 early Week 14; presentations late Week 14 or early Week 15 when available throughout. Current-semester dates are not changed by this template.
- Instructor supplied a new tentative current-semester timeline and requested timing assessment before other changes. Review it in `analysis/timing_review.md`; do not replace the current generated schedule or edit the supplied DOCX before this timing review is considered.
- The requested additional October makeup offsets an assumed lost December 31 slot; the review retains 26 teaching sessions. The holiday/half-day status is not independently confirmed.

## 2026-09-28 — Three-week assignments and workload review

- Instructor accepts current syllabus content and judges workload acceptable against a 150–180-hour semester target, noting estimates may be high. Retain unpiloted ranges rather than lowering them without evidence.
- Preserve original assignment releases after 4.2, 6.2, 8.2 and 12.2; extend each deadline by one week to allow 21 calendar days. This supersedes the 14-day/no-overlap rule. A1/A2 and A2/A3 overlap by one week on the relative schedule.
- Keep accepted midterm windows and project deadlines. Homework may support exam preparation, but completion and graded feedback are not prerequisites for exams.
- Generate a compact combined timeline. Indicative calendar ranges assume uninterrupted weeks anchored on October 5; they are not booked dates. A4 now falls at relative 15.2, and its proximity to the project final report needs calendar confirmation.
- Weekly curriculum and live-time allocation are unchanged. Final calendar mapping and operational arrangements remain provisional.

## 2026-09-28 — Semester start clarified

- Instructor confirmed the starting week is October 5, correcting the earlier November 5 statement. The expected January 8 end and 14-week term are retained.
- Preserve 26 planned lectures and tentative November/December makeups. Exact session dates and late-course assessment mapping remain provisional; weekly teaching scope and minutes are unchanged.

## 2026-09-28 — Midterm weights and provisional calendar envelope

- Instructor confirmed three midterms at 15% each.
- Retain 26 lectures, with one tentative makeup in November and one in December. Instructor reports October 29 holiday, November 3 absence and January unavailability; exact makeup dates are not booked.
- Start was stated as the week of November 5, with a 14-week term ending January 8. These do not align; request start-month clarification and preserve the raw statement rather than silently correcting it. Exact lecture weekdays/year and letter-grade deadline are not inferred.
- Accepted grading totals and frozen teaching capacity remain unchanged; dated release/deadline mapping stays provisional.

## 2026-09-28 — Phase 5 accepted; Phase 6 authorized

- Instructor accepted the first three assignment review choices: integrated Double DQN, scaffolded IQL and workload calibration. High-level tasks are accepted; performing the pilots remains future artifact work, not a claim that pilots ran.
- Apply explicit curriculum revisions: Double DQN Core with bounded target-patch implementation; IQL Core with three scaffolded losses. Clarify maximization bias as Core in line with instructor intent (it was previously grouped under Exposure in the repository); tabular Double Q remains Exposure. No weekly topic moves or minute changes. Existing examples in 6.2/12.2 connect equations to code within their allocated time.
- Move accepted assignment tasks/strategy and finalized project scope into decisions. Preserve single authoritative copies; keep estimates, evidence and rationale in analysis.
- Close Phase 5 at the high-level design gate. The fourth review item—rubric/penalty details and example LLM report—is explicitly deferred to the semester. Project presentation scheduling and its midterm-3 conflict remain deferred as directed.
- Phase 6 assignment rule supersedes prior candidate windows: release after the final relevant topic, give 14 calendar days, and delay release to the previous assignment deadline if needed. The prior January A4 target must be checked against the official calendar rather than guessed.
- Tentatively release each required video seven days before its first relevant live topic, retaining Weeks 4/8/11 review checkpoints. No readings this semester.
- Phase 6 is authorized; syllabus/design freeze is not yet declared. No Phase 7 teaching artifact construction.

## 2026-09-28 — Assignment refinements and grading-capacity constraint

- Instructor reports at most one TA, possibly none. Remove A1's separate hand-worked target task. Keep correctness checks in automated assignment support.
- Accept using existing PPO code for behavior/clipping analysis in A3, with no PPO/SAC implementation requirement; exact experiment remains proposed.
- Remove CQL conservatism from A4 and route a conceptual question to midterm 3 at existing Exposure/explain scope, replacing comparable exam content rather than adding an exam category.
- Accept A1–A3 timing windows and A4 due in the final period around the second week of January; no final exam. Exact calendar dates remain unassigned. Project final-report rule is unchanged; check the adjacent January workload.
- Accept the proposed LLM-use report contents; prepare an example only with concrete assignments. Defer all numerical rubrics and final penalty details to that stage.
- Integrated Double DQN and scaffolded IQL are recommendations requested by the instructor, not accepted coding/mastery changes. Document their prerequisites, displacement, workload and zero-added-live-time substitutions in analysis/assignment_proposal.yaml; frozen topic decisions are unchanged.

## 2026-09-28 — Individual assignments; best three of four accepted

- Instructor selected individual assignments and best three of four, normalized to the entire 20% category. Missing submissions count as zero when selecting the three scores; no separate all-four completion requirement is inferred.
- Each counted normalized score contributes up to 20/3 course percentage points. Four-task scope and delivery dates remain proposals.
- Record the implementation-evidence limitation when a distinct assignment is omitted. Midterms can assess reasoning, but do not establish implementation mastery; the frozen intended masteries are unchanged.

## 2026-09-28 — Project details accepted; assignment design authorized

- Instructor excludes readings from current planning. Preserve the internal map without further reading selection; no new reading workload or reading-only exam content.
- Accept project milestone weights 5/5/7.5/7.5/10% of the course and existing proposal/design/progress lengths. Final report is 6–8 pages plus references, due one week before letter grades (expected third week of January); do not infer a date/year or Week 14 deadline.
- Retain other deadline weeks: proposal 4, design 7, progress 10 and presentation 13. Encourage teams of 2–3; individual work and four-person teams require case-by-case decisions.
- Retain the 10-minute presentation plus three-minute discussion length. Tentatively schedule three two-hour slots of eight teams, up to 24 teams, with attendance only at the team's own slot. This leaves 16 minutes per slot for transitions. Finalize after proposals/team freeze. Peer grading remains an undecided possibility without assigned weight.
- Keep the Week 13 midterm/presentation coincidence explicitly unresolved for in-semester scheduling; no rescheduling is inferred. Presentation sessions and exams stay outside lectures.
- Move accepted milestone fields into project decisions, leaving workload estimates and recommendations in analysis. Enter assignment design within Phase 5; do not change frozen curriculum or start Phase 6.

## 2026-09-28 — Phase 5 exam and reading clarifications

- Instructor explicitly confirmed keeping midterm 3 in Week 13, covering 9.2 and Weeks 10–12. LLM RL in Week 13 is excluded from this exam. Preserve Week 14 / through-Week-13 coverage only as the future-offering template.
- The 45% exam category is unchanged. Equal 15% weights are a recommendation; exact dates and durations are still unresolved. The instructor confirmed separate exam slots, preserving all frozen lecture minutes.
- Instructor chose an internal reading map and deferred student readings this semester. No reading-only exam requirement or required reading workload is introduced. Required prerequisite videos are unaffected.

## 2026-09-28 — Curriculum frozen; Phase 5 grading, project and reading work authorized

- Authority: explicit instructor request to freeze the reviewed curriculum and begin grading/project/reading work; assignment design will be addressed separately within Phase 5.
- Accept remaining role/status classifications and the audited baseline lecture sequence. Move those fields and sessions from the Phase 3 proposal into `decisions/topic_decisions.yaml`, preserving one authoritative copy. Masteries and content scope are unchanged.
- Record curriculum frozen following the Phase 4 consistency audit. Session times remain planning estimates; two video scopes retain their authorized checkpoints. This is not syllabus/design freeze.
- Preserve the 1,440 teaching + 19 additional administration allocation and 68-minute usable margin. Midterm placement must not silently consume the existing lecture budget; unresolved exam scheduling is Phase 5 assessment work.
- Adopt the instructor's 45% midterm, 35% project, 20% assignment categories. Project subweights are explicitly tentative; assignment aggregation and this-semester third-midterm scheduling need resolution.
- Record assignment LLM permission with disclosure/examples and the instructor's no-credit rule for one-/few-shot solution delegation. Operational criteria and assignment-comprehension exam items remain for assignment design; do not silently expand this into a project policy.
- Reading publication/exam policy remains under review. Prepare a book-first internal map using normalized evidence and existing references, without a broad current-paper search or adding required readings.

## 2026-09-28 — CQL clarified; Phase 3 closed and Phase 4 authorized

- Authority: instructor clarified Conservative Q-Learning and authorized starting Phase 4 if no handoff blocker remained. Scope/mastery review and pacing judgment were already accepted.
- Make the existing CQL entry discoverable by name; record its explicitly accepted Exposure role and explain mastery. Retain its five-minute Week 12.2 contrast within the existing allocation. This adds no topic time and does not introduce BCQ or safety-constrained Q-learning.
- Close Phase 3: major scope changes, masteries and video direction are reviewed; optional LSTD/IRL remain outside the base allocation. Enter Phase 4 consistency review.
- Generate the audit, topic view and preliminary lecture plan. Remaining role/status proposals and assessment paths stay in analysis pending formal adoption; no curriculum freeze or Phase 5 authorization is inferred.

## 2026-09-28 — Mastery review accepted; Q-learning exposure term being clarified

- Authority: instructor reviewed the masteries and found them in good shape, with latitude to fine-tune teaching according to pacing and student interest.
- Move the reviewed mastery fields from the working proposal into `decisions/topic_decisions.yaml`. Generated views now join accepted mastery with the remaining proposed classifications; do not maintain a second editable copy in analysis.
- Accepted mastery applies to the bounded scope of the existing groups, not every conceivable method under each topic ID. No new assignment or assessment design is accepted.
- The instructor also requested “constrained Q-learning” as Exposure. Conservative Q-Learning is already a five-minute exposure in the offline unit; Batch-Constrained Q-learning and safety/cost-constrained Q-learning are different possible readings of that term. A focused clarification is pending; no equivalence or additional time has been assumed.
- Existing live-time allocation remains unchanged until the intended method is identified. No Phase 4 work or freeze action.

## 2026-09-28 — Phase 3 pacing, video checkpoints and future-topic register

- Authority: instructor follow-up on outstanding Phase 3 tasks. Topic scope/mastery review is still pending; the instructor judges the tight timings doable.
- Keep the configured 0.85 advance-planning fraction. The generic 15% buffer is available during delivery when needed, with the corresponding loss of question/example/consolidation time. This supersedes the earlier analytical wording that treated the buffer as unavailable. The fraction and calendar arithmetic are unchanged; generic buffer cannot be counted twice.
- Accept thirty minutes for SAC within the five policy lectures, releasing ten minutes of contingency relative to the previous candidate. The ten-minute gradient-free/finite-difference history stays.
- Calibrate BC to a high-level motivation for distribution shift. The candidate's eight-minute BC segment is an implementation estimate, not a separately accepted minute commitment. IQL remains primary and CQL a brief contrast.
- Clarify LLM RL as exposure supported by video, sufficient to begin reading papers, not comprehensive coverage. Proposed mastery labels are updated for instructor review.
- Semi-freeze the two video scopes with Week 4 (plan search), Week 8 (verify search, consider policy supplement, plan LLM preparation), and Week 11 (verify LLM requirements) checkpoints. A policy supplement is considered at the checkpoint, not automatically assigned now. See `decisions/video_decisions.md`.
- Record early-MDP redistribution, trimming repeated n-step examples and extended questions/next-session recaps as pacing options, not automatic simultaneous time savings. Preserve one n-step worked target for GAE. Moving MDPs earlier only relieves Week 2 if the freed time also advances Bellman preparation.
- Create `analysis/future_topics.md` for deferred topics and tentative connections, including the possible future classical/theory and deep/LLM course split. This authorizes a reference register, not designing two courses or adding all listed topics to the current course.
- LSTD remains an explicit optional five-minute note. The possible five-minute IRL mention and optional diffusion-policy/VLA pointers are likewise not compulsory additions; the base plan does not charge them as if accepted. Selecting multiple mentions must use real time or identify displacement.
- No new accepted assignments/readings, source normalization, teaching artifacts, Phase 4 audit or freeze action.

## 2026-09-28 — Phase 3 first review: smaller changes accepted with refinements

- Authority: explicit instructor response accepting R1–R6/C1–C5 with the refinements below. This is partial curriculum acceptance, not curriculum freeze or Phase 3 completion.
- Accepted content scope is recorded in `decisions/topic_decisions.yaml`; accepted video scope is in `decisions/video_decisions.md`. Detailed allocation, proposed taxonomy classifications and assessment paths remain analysis. The empty topic-decision schema now records accepted scopes by normalized topic groups.
- R1/C1: preserve the foundational reductions/moves; eliminate backward-lambda mathematics entirely, retaining only an existence mention alongside forward lambda/GAE.
- R2/C2: five live policy-method lectures accepted. Retain a ten-minute, nonmathematical historical overview of gradient-free/finite-difference methods and expand SAC beyond the prior brief contrast. Exact SAC depth/allocation is conditional on a focused time-budget audit, not approval of unrestricted extra material.
- R3: accept approximation/instability depth and explicit embedded experimental-design teaching.
- R4/C3: one bandit lecture accepted; move selected general exploration concepts into learned-model teaching. Preserve the narrower search/model sequence.
- R5/C4: replace the proposed CQL-primary treatment with IQL-primary and a CQL mention. Emphasize the reasons for online optimism versus offline pessimism/support constraints.
- R6/C5: accept LLM transfer/synthesis with greater use of video preparation and somewhat greater live post-training depth. Transformer, autoregressive-model, pretraining and SFT background may be carried by video. Search preparation likewise uses video, assuming CS-level BFS/DFS knowledge. These replace the earlier analytical delivery recommendations, not earlier accepted video decisions.
- Other scope: accept a five-minute average-reward introduction and dispersed psychology/neuroscience connections within existing teaching, with no separate block. LSTD is an optional five-minute suggestion, not a required addition; the instructor explicitly allowed BC to suffice.
- Displacement: reallocate within the five policy lectures; retain SAC at a bounded mechanism level rather than a full derivation/implementation unit. Move model exploration into existing model teaching and reduce latent-model survey time; replace CQL detail with IQL; carry LLM prerequisites in the video. Exact reallocations are proposed and audited in analysis, not separately accepted minute commitments.
- Prerequisites: no backward-trace dependency; replay/targets/critic knowledge supports SAC. IQL needs a bounded expectile/advantage-weighted fitting bridge. Video preparation precedes search and LLM live units. Offline support restrictions must not be confused with a claim that IQL is itself a generic pessimistic lower bound.
- Calendar, 0.85 fraction, syllabus overhead, outside-class presentations, project requirement and no-mandatory-LLM-assignment constraint remain unchanged. No source evidence, Phase 4 audit, assignment design or teaching artifact is modified by this decision.

## 2026-09-28 — Teaching-time allowances clarified before Phase 3

- Accepted explicitly by the instructor after the Phase 2 review.
- Changed the usable-content fraction from 0.90 to 0.85; reserved 20 minutes in
  Week 1 for the syllabus overview; scheduled project presentations outside
  class hours. Current values are authoritative in `config/course.yaml`.
- Accounting convention: apply the content fraction to scheduled contact time,
  then deduct the syllabus overhead separately, preserving the full slack reserve.
- Capacity check at acceptance: 28 − 1 − 3 + 2 = 26 lectures, matching 13 × 2;
  26 × 70 × 0.85 − 20 = 1,527 content minutes. Week 1 has 99 content minutes;
  each other planned week has 119. Presentations consume no lecture minutes;
  their student workload remains for later assessment/workload design.
- No topics, learning outcomes or provisional milestone weeks were changed.
  Pedagogical feasibility and topic allocations remain Phase 3 work.

## 2026-09-28 — Assignment principles clarified during repository setup

- Accepted by the instructor in the repository sanity-check follow-up.
- Removed the detailed provisional assignment sequence from `decisions/course_principles.md`; the existing hypotheses remain in `config/provisional_plan.yaml`.
- Replaced that sequence with a high-level principle: assignments support relevant learning outcomes through practice and feedback and provide evidence of expected mastery.
- Rationale: keep principles at a high level and avoid maintaining the same provisional assignment sequence in two places.
- This clarification does not revise the planned topics, assignment hypotheses, delivery, or teaching-time allocation.
