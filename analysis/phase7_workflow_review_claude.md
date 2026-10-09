# Pilot v2 lecture workflow: evaluation and proposal (Claude, revision 4, 2026-10-09)

Claude's recommendation for the instructor; not a decision. It evaluates the workflow in `docs/lecture_workflow.md`
after the 1.1 (`formulate`) and 1.2 (`mdp_values`) pilots and proposes **pilot v2**. Revisions 2–3 incorporate the
instructor's comments of 2026-10-09 (revision 4: the first-render input is kept as a flagged, unmaintained first draft):
- iterate on the PPTX; no polishing of text versions; the PPTX is the maintained source;
- the full PowerPoint render review only at the end;
- AI checks after each round of instructor edits, especially of the speaker notes;
- YAML optional, made only on instructor request;
- Dropbox and backups suffice for PPTX versions this semester;
- suggestions pull from all sources, with a delta only against substantial old slides.

Facts come from the pilot files and deck histories; judgments about cost and value are inference.

## What happened in the pilots

| | 1.1 Introduction | 1.2 MDPs, returns and values |
| --- | --- | --- |
| Written before handoff | 2 suggestions, 3 AI reviews, round-2 notes, shared review (186 lines), content file (259 lines) | 2 suggestions, 2 old-deck comparisons, shared review (360 lines, 17 sections), content file (490 lines) |
| Renders before handoff | several (template, figure and timing iterations) | 2 full renders, each followed by a ChatGPT review |
| Instructor edits at handoff | 4 slides added, robot figure redrawn natively, title restyled, timing set in notes | 4 slides added, 3 replaced, 13 of the 16 remaining slide bodies edited, slides reordered, every timing re-set |
| Found after the instructor's edits | stale notes line (twice) | factual slips (R_t for R_{t+1}, γr_{t+2}, "deterministic rewards"), notation clashes, grammar, stale notes and equation sources, R15–R17 |

About 2,400 lines of suggestions, reviews and proposals were written for about 105 minutes of teaching.

What earned its cost:
- independent suggestions plus cross-review (problems caught before any slide existed);
- the old-deck comparison (the most instructor decisions per line written);
- checks after the instructor's edits (the errors students would see);
- native equations, previews and text views.

What did not:
- polishing text and decks before handoff;
- keeping the YAML in step after handoff;
- status restated in five files;
- AI timing estimates.

**A shared failure in 1.2 (instructor's observation):** both AIs built the 1.2 suggestion on top of 1.1 instead of
starting from the existing course material for MDPs. The old-deck comparison had to be done afterwards and drove most
of the revision. This calls for better suggestion instructions (W1), not for dropping the step.

## Pilot v2 workflow (per deck)

1. **Initial suggestions (both AIs, independent, unpolished).** Each AI writes one combined suggestion:
   - **pull what is relevant from all sources:** the existing course, the book, the configured reference courses and
     the session sources index, with provenance;
   - **delta against the previous course's slides where they are substantial:** list the old decks and slides that cover
     the session (a session can draw on several old decks, and one old deck can span several sessions), each marked
     keep / cut / fix / move, with correctness and notation issues. If unsure whether the existing material is substantial
     enough, ask the instructor;
   - **continuity:** what students already saw in earlier new decks (running example, notation), used as context, not
     as the base.

   Format: a slide-level outline with reasons and timing impact; no polished wording.
2. **Mutual cross-review (both AIs)**, one round in the shared review file (unchanged; low cost).
3. **Instructor comments**, recorded once in the deck decision file (unchanged).
4. **Content file (ChatGPT), render-ready but unpolished.** Slide list, old-slide references, equations, minimal notes.
   It is the input to the first render only and is frozen at that render. There is no separate review of the text
   proposal: Claude raises issues it finds while rendering in the shared review.
5. **First render (Claude).** PPTX with old slides copied natively, plus a quick LibreOffice preview for gross problems.
   From here the PPTX is the source. The builder's input (`<deck>_claude.yaml`) is kept in the repository as a
   **first draft, not maintained**, with a header saying so and naming the PPTX as the source (see W5).
6. **Iteration: instructor edits ↔ AI content and error check**, repeated as needed. After each saved round, both AIs
   check what changed (the text-view diff shows it):
   - facts and arithmetic;
   - notation against the guide;
   - grammar;
   - **speaker notes:** stale references, notes that no longer match the slide, missing answers or cues;
   - consistency across slides;
   - timing against the ceiling.

   Findings go to the shared review. Claude applies the fixes the instructor approves directly in the PPTX and
   regenerates the text view. Quick previews: Claude uses LibreOffice, Codex its own tool (limits below).
7. **Final complete check.** A PowerPoint render of every slide (layout, figures, equations, fonts) and a full pass over
   content and notes by both AIs. Claude refreshes the equation fallback pictures
   (`scripts/refresh_math_fallbacks_claude.py`) if equations were edited outside PowerPoint. After the fixes the deck is
   **done**: fingerprint, previews and text view from the final PPTX, status in the deck decision file, one
   decision-log line.

Unchanged:
- file ownership;
- the important-decision pause list;
- the timing convention;
- never rebuilding over an edited deck;
- instructor approval for notation-guide changes.

Deferred: the shortened chain (W7).

**Previews during iteration (tested on the 1.2 deck, 2026-10-09).** LibreOffice is fine for text, wrapping and gross
layout. It is not reliable for:
- native equations: it shows each equation's stored fallback picture, which PowerPoint updates only when it re-saves that
  equation, so equations edited outside PowerPoint look stale until the step 7 refresh;
- connector figures: the robot figure's curved arrows render wrongly;
- fonts and spacing.

Alternatives considered: python-pptx cannot render, and the `pptx-renderer` package is a templating tool (it fills
placeholders in a template) and does not produce images. So: LibreOffice for quick text/layout previews; PowerPoint
for the final visual check.

## Decisions for the instructor

| # | Question | Status / Claude's recommendation |
| --- | --- | --- |
| W1 | Initial suggestions as in step 1: pull from all sources; delta against the previous course's slides where substantial; ask if unsure. Add instruction text to the shared conventions. | Instructor's reformulation, adopted in step 1; final decision after ChatGPT's input. Instruction text below. |
| W2 | No separate review of the text proposal, neither by an AI nor by the instructor; the PPTX is reviewed instead. Keep the AI cross-review of initial suggestions. | Instructor agrees. |
| W3 | One correctness-only AI pass before handoff at most; no polishing. | Instructor agrees. |
| W4 | Iteration (step 6) plus a final complete check including the PowerPoint render (step 7). | Instructor's proposal; in the steps. |
| W5 | YAML optional: a maintained YAML only when the instructor asks; the AIs neither recommend nor require it. No pull-back transcription; no script work to keep YAML generation current. The first-render input stays in the repository, flagged as an unmaintained first draft. | Instructor's decision in principle (2026-10-09), including the first-draft file: a PPTX cannot always be converted back (equation-slide bodies and PowerPoint-only content such as figures and copied slides are not recoverable), so the draft is worth keeping. |
| W5a | PPTX version control | Resolved for this semester: Dropbox history and `output/deck_backups/` (instructor). The slim git-tracked copy idea is in `analysis/ideas_backlog.md`. |
| W6 | Deck status only in the deck decision file; clean up 1.1 and 1.2. | Instructor agrees in principle. Proposed cleanup below; not yet done. |
| W7 | Shortened chain | Deferred until the main workflow is settled. |
| W8 | Deck split beyond the pilot | Separate decision; one log line when decided. |

**W1, cost of a delta against all sources.** A slide-by-slide delta against every source would be long and mostly
wasted: each reference course has dozens of slides per topic, and most only confirm what the book says. Pulling what is
relevant from all sources, with a delta only against substantial old course slides, keeps the useful part of the 1.2
old-deck comparison without that cost.

**W5, first-draft header** (for the YAML files from now on):
> First draft: renderer input for the first render of this deck only (date). Not maintained: the PPTX is the source
> from that render on. Do not rebuild over the deck or treat this file as its current content.

**W5, what an optional YAML loses.** Rebuilding from text is not usable after instructor edits anyway. A rebuild cannot
reproduce PowerPoint-only content, and it is forbidden over an edited deck. The versioned description of the deck becomes
the tracked text view (all text, notes and equation text) plus the previews. Reuse happens by copying slides in
PowerPoint. The builder and pull script stay available when the instructor asks for a YAML.

**W6, proposed cleanup for 1.1 and 1.2.**
- The deck decision file keeps the status and fingerprint.
- The shared review, content-file headers and YAML headers replace their status restatements with a one-line pointer
  to the decision file.
- The decision log stays append-only, since it is the audit record. From now on it gets one line per batch of decisions
  and one at "done"; past entries are not rewritten.

**Proposed instruction text for W1** (shared conventions in CLAUDE.md and AGENTS.md):
> When preparing a session's initial suggestion, pull what is relevant from all sources (the existing course, the book,
> the configured reference courses), with provenance. Where the previous course has substantial slides for the
> session's scope, which may be spread over several old decks, start from them: give a keep/cut/fix/move delta with slide
> references. If unsure whether the existing material is substantial, ask the instructor. Earlier new decks are context
> for continuity (running example, notation, what students already saw), not the base.

If accepted:
- `docs/lecture_workflow.md` is rewritten to the pilot v2 steps;
- the instruction text is added to both convention files;
- a decision-log entry is made.

Existing pilot files stay as they are, apart from the W6 cleanup.
