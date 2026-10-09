# Phase 7 pilot retrospective and suggested workflow — ChatGPT

**Author/date:** ChatGPT, 2026-10-09.
**Status:** recommendations incorporating the instructor's comments after the 1.1/1.2 pilot. This document does not update or supersede the governing workflow or accepted decisions. Only this file was created for this request.
**Inputs:** [Claude's retrospective](phase7_workflow_review_claude.md), [current workflow](../docs/lecture_workflow.md), both initial 1.2 suggestions, the old-deck comparisons, the shared 1.1/1.2 reviews, deck decisions and the instructor's subsequent discussion with ChatGPT. Claude's files were read for this scoped review only.

## Alignment with the instructor

The instructor's first combined comment addresses my original recommendations 1–2; the remaining comments address original recommendations 3–8 in order.

1. **Preserve introductory context and motivation.** Yes: this is the main correction I intended, and the instructor's formulation is clearer. Both AIs removed or compressed non-mathematical explanations that establish what a quantity is for, why it is needed and how it fits the larger problem. The resulting first pass too often assumed an audience that already understood the purpose and needed only definitions, mathematics and examples. Initial suggestions and their mutual review must instead assume students are encountering these ideas for the first time. Source inspection supports this requirement; merely citing sources does not satisfy it.
2. **Define “unpolished.”** Correct content and a usable teaching sequence are required; refined wording and visual design can wait. One qualification: essential context and motivation are part of introductory content, not optional polish. They can initially be expressed as short prompts or explanatory cues. Additional anecdotes, stylistic transitions and richer illustrations can emerge in PPTX iteration, but the first draft must not leave the central “why” for the instructor to reconstruct.
3. **Review priorities fit the existing loop.** No additional review stage or approval process is proposed. Distinguish errors, likely teaching difficulties, optional preferences and maintenance within the existing findings. This should make the AI feedback more useful and reduce unnecessary work for the instructor. My withdrawn M04 finding illustrates the need to check surrounding content before treating a precision suggestion as a required correction.
4. **Use targeted visual checks during iteration.** Do not rely exclusively on text diffs and postpone every visual issue until the end. Inspect affected slides when an edit changes diagrams, equations, layout, media or reveals. A suitable existing or freshly generated preview can support this; use PowerPoint when another renderer cannot faithfully show the affected feature. The final comprehensive check remains the full-deck check after substantive iteration settles. Finding something there leads to a repair and verification, not a new workflow category.
5. **Keep instructor acceptance explicit.** AI review completion means ready for acceptance. The instructor marks the deck done. The PPTX is the teaching artifact; accepted curriculum scope and cross-session commitments remain governed by the decision records.
6. **Make timing interpretations softer.** The instructor already treats timings as estimates. AI checks and report wording should do the same. Arithmetic and consistency checks remain exact; judgments of teaching feasibility remain approximate. Do not treat an exact sum of slide targets as evidence that students can learn the material in that time.
7. **Improve iteration efficiency rather than minimize instructor editing.** Editing is a productive part of preparing a lecture. The aim is to reduce preventable correction, repeated decisions, weak review findings and synchronization work, while making the instructor's substantive choices easier to realize.

## What the pilot supports

The initial suggestions did contain old-slide references and source-based checks. The more precise failure was inadequate preservation of those sources' explanatory content. The later old-deck comparison restored the interaction loop, motivation for an infinite return, the policy objective and estimation from repeated returns. These were useful teaching components, not merely additional mathematical coverage.

Mutual review also earned its place: the distinction between a continuing return and a truncated sum, and between truncation error and sampling variation, improved through cross-review. However, agreement between the AIs did not reveal their shared assumption that much of the motivation could be compressed. Review must explicitly test introductory accessibility as well as correctness.

PPTX iteration proved useful because the instructor could change the actual teaching artifact directly. Maintaining a parallel current YAML and repeating status across several files added work without replacing that editing process. First-render inputs should remain historical after rendering; the saved PPTX and its generated review views support subsequent work.

These are judgments from the pilot history, not measured estimates of preparation-time savings.

## Suggested workflow per deck

### 1. Independent initial suggestions from both AIs

Use the accepted session scope, mastery, activity and timing frame. Inspect the relevant existing course slides, book sections and configured reference-course material, using the session source index to locate them. Earlier redesigned decks supply continuity: notation, running examples and what students have already encountered. They do not replace the sources for the new session.

Where substantial old material exists, include a compact keep/cut/fix/move comparison, with deck and slide references. Group related slides when that is clearer. Account for the teaching purpose of material proposed for removal or compression: preserve it elsewhere, explain why it is unnecessary, or identify the accepted later placement. Do not require a slide-by-slide comparison against every external course, a separate source-audit document or instructor permission for routine source selection.

Each suggestion should give a concise teaching sequence, meaningful alternatives and their consequences. For each major new concept or quantity, make clear:

- the problem or question it addresses;
- its meaning and purpose before or alongside its formal definition;
- its connection to what students already know;
- an example, interpretation or student question that checks understanding.

These are criteria for the sequence, not a mandatory four-part template for every slide. A concept may develop across several slides. Do not turn every qualification or source observation into additional live content.

### 2. One bounded mutual cross-review

Compare the initial suggestions in the existing shared review file. Check mathematics, source use, introductory context, motivation, sequencing, accepted commitments and approximate feasibility. Specifically ask whether the proposals assume knowledge of why a quantity is useful before the lecture has supplied that knowledge.

Identify substantive differences and omissions, including assumptions shared by both suggestions. Resolve straightforward corrections and present only consequential choices to the instructor. Avoid repeated prose refinement, duplicate summaries of agreement or an additional review of the consolidated text proposal.

### 3. Instructor choices recorded once

Record explicit outcomes in the deck decision file, with the existing decision-log convention. Agreement between AIs is not instructor acceptance. Routine content preparation proceeds within the accepted scope; pause only for substantive unresolved choices under the existing important-decision rules.

### 4. Minimal first-render content input

ChatGPT consolidates the choices into the shared content file. Include stable slide IDs where practical, the proposed order, exact reuse references and edits, necessary new displayed content, correct equations and essential speaker cues or answers.

“Unpolished” means that visual layout, fine wording, illustrative enrichment and stylistic transitions need not be finalized. It does not mean incorrect equations, missing essential explanations, unresolved factual placeholders or a sequence that requires the instructor to supply its entire motivation. Copying an old slide usually needs a reuse reference and an edit list rather than a lengthy textual reconstruction.

There is no separate proposal-review loop. Claude raises substantive issues encountered during rendering in the shared review. At most one correctness pass before instructor handoff is sufficient; do not use this interval to polish an artifact that the instructor has not yet seen.

### 5. First PPTX and handoff

Claude produces a usable, editable PPTX, preserving appropriate native old-slide objects. A quick preview checks for gross rendering problems. The initial content and any renderer YAML are then frozen as first-render inputs, clearly marked historical and pointing to the deck decision file for current status. They are not maintained descriptions of the evolving deck.

From this point, the saved PPTX is the teaching source. Preserve Dropbox history and the existing deck backups; no new version-control mechanism is proposed for this semester. Never rebuild over an edited deck. Maintained YAML is only produced if the instructor explicitly requests it.

### 6. Instructor–AI iteration on the PPTX

After a saved round, refresh the generated text view and identify the version under review. Both AIs check changed content and affected dependencies rather than repeatedly auditing every unchanged slide. A model or notation change may affect distant equations and notes even when their text did not change.

Within this same loop, check:

- facts, mathematics, notation and consistency;
- context, motivation, teaching sequence and likely student misconceptions;
- speaker-note agreement, answers, cues and obsolete references;
- approximate timing and protection of worked activities;
- visual or behavioral changes that a text diff cannot show.

For the last item, inspect affected diagrams, equation formatting, image changes, layout, slide visibility and relevant builds/media using suitable previews or the actual presentation. Text diffs are an aid, not a complete change detector. Identify stale previews explicitly. The pilot documented differences between PowerPoint and other renderers; do not interpret an unreliable preview as proof of a defect in the deck, or as proof that the deck is correct.

Keep findings concise in the shared review: affected slide, issue, consequence, proposed correction and resolution. Label the distinction between an error, a teaching risk, an optional preference and maintenance without adding a new workflow stage. Read the slide in context before reporting a missing explanation. Claude applies instructor-approved fixes directly to the PPTX and refreshes affected views. The reviewer verifies the affected material; unrelated clean material need not be checked again on every round.

### 7. Final comprehensive check and instructor acceptance

When substantive iteration settles, perform a complete content/notes review by both AIs and inspect a fresh PowerPoint render of the deck. Include hidden slides and confirm their intended status. Check meaningful animations, builds, media or links in slideshow mode where static exports cannot establish correct behavior.

If equations were edited through tooling, Claude performs any necessary fallback-image refresh before producing the final review exports. Check the resulting saved artifact. All review views must correspond to the identified PPTX; an earlier clean review does not establish the correctness of later edits.

Fix remaining issues and recheck the affected content and visuals. A wider recheck is warranted only when a fix has wider effects. Report material limitations explicitly rather than equating extraction or a successful export with a full visual review.

The instructor then accepts the deck. Record done status and the accepted fingerprint in the deck decision file, with one decision-log entry. Current status is maintained only there; other artifacts point to it. Historical reviews retain the versions they examined. Later substantive edits reopen the applicable review/acceptance work.

## Timing and recordkeeping refinements

Treat block and slide targets as planning estimates. Prefer approximate block allocations and a small number of concrete pacing concerns over fine-grained claims of feasibility. Protect student calculation, explanation and discussion time. Required spoken content counts even when it resides only in notes.

Keep arithmetic checks, stale-data checks and comparisons with accepted allocations. Report their meaning accurately: “targets sum to X; feasibility remains an estimate,” rather than “the lecture fits.” Small differences between an approximate planning baseline and saved slide estimates should be explained, not automatically treated as a curriculum change. Explicit changes to accepted allocations or ceilings still require the existing decision process. Classroom carryover remains excluded from later-session planning under the accepted convention.

Current deck status belongs only in its decision file. Shared reviews hold findings and their historical evidence; generated text and previews describe the saved deck; frozen first-render inputs retain their original purpose. Do not maintain equation transcriptions or duplicate state merely to make all representations look synchronized. Essential source attribution and teaching notes remain useful, but the actual displayed content must be inspected for correctness.

When an instructor edit materially changes scope, a prerequisite, a running example or another cross-session commitment, reconcile that change with the authoritative decisions. Wording and layout edits do not need individual curriculum-log entries. No new required reading, assessment or student workload follows from this workflow proposal.

## Evaluating the next iteration

Use a short retrospective in the existing review rather than another reporting system. Assess whether the first PPTX preserves the relevant source explanations, whether the instructor had to restore missing motivation, which consequential errors the reviews caught, and where repeated decisions or synchronization work caused avoidable effort. Instructor editing volume alone is not a failure measure.

The shortened workflow and deck split remain separate deferred decisions. This recommendation introduces no additional mandatory review round and no change to the course's timing allocations. If adopted, its operational rules can be incorporated into the workflow and shared conventions in a later authorized update; those files have not been edited here.
