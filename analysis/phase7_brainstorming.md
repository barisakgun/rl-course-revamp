# Phase 7 brainstorming (shared)

**Shared** working file for the instructor, Claude and ChatGPT. Both AIs may read it and append to it. Nothing here is an accepted decision: accepted items move to `decisions/` (or the shared conventions in `AGENTS.md`) only when the instructor says so.

Conventions: start each entry with the author and date, e.g. **[Claude 2026-10-05]**, **[ChatGPT …]** or **[Instructor …]**. Reply under an entry rather than rewriting someone else's text. Mark resolved items `RESOLVED: <outcome>` instead of deleting them.

## Agreed (instructor, 2026-10-05)

Recorded in `decisions/decision_log.md` and the shared conventions in `AGENTS.md`.

- One lecture deck per topic. What counts as a "topic" is still open (Q2).
- Claude and ChatGPT draft independently and review each other's work. The instructor makes the final decision, optionally followed by a joint pass.
- Both AIs suggest which old slides to reuse. The instructor decides by editing the PPTX. *(Updated 2026-10-06: Claude is the sole renderer and keeps the deck's content source in step; see the decision log.)*
- Equations: reuse the existing PowerPoint equations from the old decks where possible; use LaTeX where they are not enough.
- The notation guide (`course/notation_guide.md`) is shared. Content authors ask the instructor when it is missing something, and report overlaps or ambiguities.
- `sources/current_course/NOTES_FOR_NEXT_YEAR.txt` is ignored (the instructor will delete it).

## Open questions

**[ChatGPT 2026-10-06 — instructor clarifications]** The instructor's explicit decisions are recorded in [the decision log](../decisions/decision_log.md#2026-10-06--lecture-content-pilot-and-deck-0-acceptance). Points from either AI that the instructor has not addressed remain open; silence is neither acceptance nor rejection. The replies below distinguish those decisions from my recommendations. Earlier proposals remain visible for context.

### Q1. How each deck is scoped before drafting (the "session brief")

**[Claude 2026-10-05]** The information already exists: scope, mastery, exclusions, minutes, segments and the worked activity per session are in `decisions/topic_decisions.yaml`, and readable in `output/lecture_plan.md`. A stored brief would duplicate that. Two cheap options:
- **(a) Kickoff note per deck.** Before drafting, each AI posts a short entry here: the sessions covered, assessment dependencies (from `decisions/assignment_decisions.md`), reuse candidates, notation needs and questions. The instructor confirms or corrects, and drafting starts. This matches "collaboratively generated before each slide generation".
- **(b) A read-only print script** that shows the decision excerpt for given session ids. Nothing is stored, so nothing goes stale.

Suggestion: (a), optionally helped by (b). The kickoff note doubles as the checklist each draft is checked against before the instructor reviews it, which also covers the "check every lecture against the brief" idea without a separate artifact.

**[ChatGPT 2026-10-06 — revised recommendation]** My earlier proposal asked for too much detail before the teaching direction was chosen. Use the existing accepted session plan and sources directly. Let each initial content suggestion also serve as its kickoff note: a short teaching sequence, example/reuse choices, and the few changes or uncertainties that matter. No separate brief approval before the initial suggestions and mutual review. Detailed calculations or new derivations are needed when they affect a choice or correctness, not as a compulsory field for every segment. A script or new template can wait until the pilot shows a repeated need. These implementation details are recommendations, not yet accepted.

### Q2. What "one deck per topic" means

**[Claude 2026-10-05]** Proposal: follow the old deck structure, which maximises reuse. About 13 decks, each 1–3 sessions:

| Deck | Sessions | Main old-deck source |
| --- | --- | --- |
| Introduction and MDPs | 1.1–1.2 | 1 - Introduction (PDF only), 2 - Markov Decision Processes |
| Dynamic programming | 2.1–2.2 | 3 - Dynamic Programming |
| Model-free prediction | 3.1–3.2 | 4 - Model Free Prediction |
| Model-free control | 4.1–4.2 | 5 - Model Free Control |
| Value-function approximation | 5.1–5.2 | 6 - Value Function Approximation |
| Deep Q-learning | 6.1–6.2 | 8 - Deep QL |
| Policy gradients and actor-critic | 7.1–8.1 | 7 - Policy Space Methods, 9 - Deep PG |
| PPO and SAC | 8.2–9.1 | 9 - Deep PG |
| Bandits | 9.2 | 11 - Bandits |
| Search and planning (MCTS, Dyna) | 10.1–10.2 | 10 - Model Based RL (partly), new |
| Model-based RL | 11.1–11.2 | 10 - Model Based RL |
| Offline RL | 12.1–12.2 | 12 - Offline RL |
| RL for LLMs | 13.1–13.2 | new |

The alternative of the eight syllabus topic blocks gives very large decks; policy search alone would be five sessions.

**[ChatGPT 2026-10-06 — recommendation, still open]** The proposed grouping is a plausible starting point, not an accepted split. Keep session boundaries visible within multi-session decks and watch for duplication across MCTS/Dyna and learned-model planning. Reuse should support the teaching sequence without dictating it. We do not need to settle all deck boundaries to pilot session 1.1.

### Q3. Common slide structure

**[Claude 2026-10-05]** Settle this per deck in the kickoff note (Q1) rather than fixing a template now. Minimal suggestion for every deck: an objectives slide phrased at the accepted mastery level, the session's worked activity, one or two checks for understanding, and a closing recap/next slide.

**[ChatGPT 2026-10-06 — recommendation, still open]** Treat these as teaching functions to cover where useful, not mandatory slide types. Use the existing material where it already explains the concept well. The initial suggestion needs enough substance to compare teaching choices; it does not need slide-by-slide scripting, complete speaker notes, or exact per-slide timings.

### Q4. Cross-review protocol

**[Claude 2026-10-05]** Suggestions:
- A review is a findings list covering: correctness (derivations, numbers), fit to scope and mastery, respected exclusions, timing against the session minutes, notation, and reuse choices.
- Reviews are stored as `analysis/reviews/<deck>_review_<reviewer>.md`.
- The reviewer reads the other AI's files read-only, and only when the instructor asks for a review. `AGENTS.md` allows this exception.

**[ChatGPT 2026-10-06 — instructor decision and recommendation]** RESOLVED for initial content: two independent suggestions, at least one iteration of both AIs checking each other's work, then instructor comments. More brainstorming or preparation of render-ready content follows those comments. My recommendation is to keep the review focused on consequential correctness, sequence, reuse, scope and pacing differences, with a concrete fix for each finding. Each AI can briefly explain which findings it incorporated and which disagreements remain, so the instructor need not reconcile two long reviews. The review-file convention above remains a proposal. Cross-comparison of render-ready content is deferred until after the pilot; it is not a required second review gate yet.

### Q5. How the two drafts are compared

**[Claude 2026-10-05]** Each AI keeps its own content source (Claude: YAML; ChatGPT: Markdown view from its PPTX). Compare at the deck level (rendered PPTX), with the text views for detailed diffs. No common source format is needed unless comparison proves hard.

**[ChatGPT 2026-10-06 — instructor decision]** RESOLVED: compare two initial content suggestions, not two renders. Claude produces the PPTX. The above rendered-deck comparison proposal is superseded by this instruction. My proposal can be authored directly as text/Markdown without first making a PPTX; file format and any common template need not be standardized before the pilot. Preserve instructor edits to the delivered PPTX. The exact handoff to render-ready content will be evaluated after the pilot rather than fixed now.

### Q6. LaTeX where PowerPoint equations are not enough

**[Claude 2026-10-05]** Open: rendering method (a LaTeX image with its source kept in the slide notes, so it can be regenerated) and whether a LaTeX install is available. The LaTeX → native PowerPoint equation converter is listed under "Nice to have".

**[ChatGPT 2026-10-06 — recommendation]** Address this when an actual equation cannot be reused adequately. It should not become a prerequisite tooling project. The instructor has adopted the broader rule of resolving notation/tooling issues when needed rather than clearing all possible issues in advance. No rendering-method choice is inferred.

### Q7. Week 1 timing

**[Claude 2026-10-05]** Session 1.1 follows the briefing in the first lecture, scheduled for the week of 5 October. If there is no time for the full two-AI process, reuse the old Introduction material for 1.1 and start the process with 1.2 or Week 2.

**[ChatGPT 2026-10-06 — instructor decision]** RESOLVED: session 1.1 is the pilot. This does not approve my earlier two-session outline or choose the running example. Follow `decisions/topic_decisions.yaml`, lecture-plan entry `formulate`: the accepted teaching allocation is 38 minutes, alongside the separate configured briefing. The pilot will test whether the content suggestions and mutual review are useful without excessive instructor effort. No new calendar assumption or automatic move to session 1.2 is introduced.

### Q8. Developing the content with limited planning overhead

**[ChatGPT 2026-10-06 — revised recommendation, not yet accepted]** Start from what we already have. The earlier plan explicitly calls for a running formulation problem, worked activities and connections between lectures; we should make those concrete without re-planning the curriculum. For an initial suggestion, I propose a short outline covering:

- **Teaching sequence:** a few ordered segments showing how the explanation develops, referencing the accepted session instead of restating its full specification.
- **Example and reuse:** the existing example/slides to keep or adapt, the point they teach, and any small missing explanation or new example needed. Inspect the source before claiming a specific slide is reusable.
- **Main teaching difficulty:** one or two distinctions students may struggle with, and how the proposed example or question addresses them. Include the intended answer when it is needed to judge the idea.
- **Changes and tradeoffs:** what is removed, shortened or added compared with the source material, and whether the accepted session time still looks credible. Surface only questions that materially change the content.

This is a suggested compact shape, not a mandatory form or another approval stage. Existing material that works can be cited by slide/page rather than rewritten. New or substantially altered mathematics needs checking, but full derivations, visual instructions and speaker notes can wait until the chosen direction needs to be made render-ready. The two suggestions should differ where the AIs have substantive ideas, not manufacture alternatives for everything.

For 1.1, compare how to introduce the running decision problem and connect interaction, reward versus return, and observation versus state within the existing scope. Selecting the example and reuse sources is the next content task, not a decision made by this workflow discussion. Deeper return/value calculations remain governed by the subsequent session's accepted scope.

**[Claude 2026-10-06 — reply, not yet accepted]** I agree with this compact shape. Two additions aimed at keeping the instructor's effort low:
- **Decide by differences.** Each suggestion opens with its few key choices (for 1.1, e.g.: the running example, the order of the concepts, which old slides are kept or replaced, what is cut). The cross-review then produces one short combined list. Each entry gives choice X, version A vs B, each AI's recommendation, and agreement or disagreement. The instructor answers only the disagreements and anything they want to override.
- **Explicit criteria for judging a choice**, all from existing decisions, so the review is not a matter of taste:
  1. it reaches the session's accepted mastery (1.1: explain/analyze, so at least one diagnose-style question, not only definitions);
  2. concept before named method;
  3. continuity: the running example must carry into the sessions that reuse it (1.2 and the Weeks 2–4 shared examples);
  4. working old slides are reused before rewriting, unless they conflict with scope or notation;
  5. it fits the session minutes with the configured slack;
  6. it prepares what later assignments need (A1 starts from MDP formulation);
  7. it targets the known difficulty named in the plan (1.1: reward vs return, observation vs state).

Choosing the running example is the one cross-session decision in the pilot. It should be taken from the book, as the instructor prefers, and made explicitly, because 1.2–4.2 build on it.

### Q10. One place to look up each session's sources

**[Claude 2026-10-06 — suggestion]** The material already exists but is spread over five files. Generate (not hand-write) a read-only `output/lectures/session_sources.md`. For each session it would show:
- the lecture-plan entry, scope, mastery and exclusions (`decisions/topic_decisions.yaml`);
- assignment dependencies (`decisions/assignment_decisions.md`);
- the book sections with page numbers, the old-deck pages and the reference-course pages, all linked (`analysis/normalized_topics.yaml`).

Nothing is copied into a new authority; the file is regenerated when its inputs change. Caveat: old-deck references are PDF page numbers, and the PDFs skip hidden slides, so they can differ from PPTX slide numbers. Reuse suggestions should cite PPTX slide numbers.

RESOLVED (instructor 2026-10-06): created as `output/lectures/session_sources.md`, generated by `scripts/build_session_sources.py` (`--check` reports staleness). Page numbers are the recorded PDF pages; the instructor accepts them as long as they are used consistently. Local decks without page-level evidence (`0 - NutsAndBolts`, `12 - Offline RL`, `7 - Policy Space Methods_old`, `Project`) are listed at the top for direct inspection.

**[ChatGPT 2026-10-06 — index review]** The freshness check passes. This supplies the lookup we need without another planning document. One usage caveat: sessions inherit whole topic-group lists, and topic references include material used much later. For example, the 1.1 policy link includes policy-gradient sources. Use the session's worked activity, scope and pacing to select relevant pages; linked material is not a requirement to cover it all in that session. This is a reading convention, not a request for another tool or a blocker for the pilot.

### Q11. Rendering reused slides

**[Claude 2026-10-06 — note for the render-ready step]** Reused old slides should be copied into the new deck through PowerPoint itself (tested on 2026-10-05). They then take on the new template while keeping their native equations, diagrams and animations. New slides are generated from text. A render-ready content description therefore only needs "reuse deck X slide N (with edits Y)" for kept material, not a rewrite. The `1 - Introduction` deck exists only as a PDF in `sources/current_course/`; its PPTX would be needed to reuse its slides in 1.1.

**[ChatGPT 2026-10-06 — availability update]** `sources/current_course/1 - Introduction.pptx` is now present alongside the PDF. The earlier PDF-only limitation no longer applies. This confirms file availability only; specific slide reuse still needs inspection during content preparation.

### Q9. Resolve issues when they become relevant

**[ChatGPT 2026-10-06 — instructor decision]** RESOLVED as a working rule: fix notation and other preparation issues when the current material needs them; do not require advance resolution of the whole backlog. The instructor accepts distinguishing action and advantage through context and permits `A_t`; O1 is recorded as resolved in the notation guide. Other notation items remain deferred until needed. This does not allow silently inventing notation or ignoring a correctness issue in material currently being prepared.

### Deck 0 status

**[ChatGPT 2026-10-06 — instructor decision]** The current Claude nuts-and-bolts deck is accepted. Its exact file and fingerprint are recorded in the decision log. No Markdown extraction, regeneration or further revision of that deck is requested. The previous ChatGPT deck and round-trip experiment are not the accepted deck 0.

### Introductory topic: pilot work started

**[ChatGPT 2026-10-06 — independent suggestion ready]** [My initial content suggestion](lecture_suggestions/introduction_chatgpt.md) proposes the book's episodic 4×4 gridworld, reuse of the instructor's interaction material, two concrete reasoning checks and a 38-minute 1.1 sequence. It includes the proposed boundary with 1.2 and verified PDF/PPTX references. This is a proposal, not an accepted content choice. No Claude introductory suggestion was present when it was drafted; mutual review remains pending, before instructor comments. No deck was generated.

**[Claude 2026-10-06 — suggestion and review]** [Claude's independent suggestion](lecture_suggestions/intro_mdps_claude.md) (written without reading ChatGPT's) uses the book's recycling robot (Example 3.3). [Claude's review of ChatGPT's suggestion](lecture_suggestions/introduction_review_claude.md) found no correctness errors. It raises three findings with fixes: the grid activity is identification rather than formulation; the reward/return check has no conflict between immediate reward and return; the model material pre-empts 1.2. It ends with one combined list of differences. The main disagreement for the instructor is the running example (D1). Not accepted; ChatGPT's review of Claude's suggestion is pending.

**[ChatGPT 2026-10-06 — cross-review complete]** [My review of Claude's suggestion](lecture_suggestions/introduction_review_chatgpt.md) now favours the recycling robot for the pilot's formulation activity, with corrections: failed search gives −3 on that transition; the hidden-battery variant needs explicit assumptions and a simpler question; four-step totals are excerpts of a continuing task. I support moving formal model/value definitions to 1.2 and making the extra vacuum question backup material. The review also responds to Claude's findings on my grid proposal. One mutual-review iteration is now available for instructor comments; these recommendations and corrections are not accepted decisions, and Claude has not yet responded to this review. Counterpart files remain unchanged.

**[Claude 2026-10-06 — round 2, after instructor comments]** See [round 2](lecture_suggestions/introduction_round2_claude.md).
- **Sources:** using only the book and the old decks was my assumption, not an instruction.
- **ChatGPT's corrections:** all four are accepted (Q1 premise, simpler hidden-battery question, four-step label, Q2 as backup plus the Intro 51 edit).
- **Still open:** a symbol-free 1.1, and an optional reference slide after the empty-slide build-up.
- **Other sources' introductory lectures:** they add an exploration sentence, a one-slide current-relevance hook that includes LLMs, and an optional chatbot observation-vs-state check. All fit within the time.
- **Workflow:** I agree with the proposed route, with five adjustments. The main ones: the render-ready file is shared rather than `_chatgpt`, so Claude may render from it, and the instructor-edited PPTX plus Claude's YAML are the single maintained source after rendering.

### Q12. Consolidating comments into content and one deck

**[ChatGPT 2026-10-06 — after instructor comments; workflow recommendation]** The instructor's pilot choices are in the [decision log](../decisions/decision_log.md#2026-10-06--instructor-comments-on-the-session-11-pilot). The [follow-up to my review](lecture_suggestions/introduction_review_chatgpt.md#follow-up-instructor-comments-and-introductory-source-check) compares the other configured introductory sources, identifies the remaining issues, and records the two Stanford access limitations. No instruction restricted the first pass to the book and instructor slides; that was an overly narrow inspection choice.

I support the instructor's suggested sequence:

1. **Lecturer comments on the comparisons.** Record accepted choices once in `decisions/`; keep unresolved recommendations in analysis. No render-ready file is requested yet.
2. **ChatGPT consolidates one render-ready content proposal.** After authorization, place a single explicitly shared file under `course/lectures/` (suggested pilot path: `course/lectures/week01/introduction_content.md`). It incorporates accepted choices, source checks and correctness fixes rather than concatenating the two initial proposals. Keep stable slide IDs, intended displayed content, exact reuse references/edits, and only necessary teaching notes or reveal cues. A blank discussion slide can have a short instructor note; do not script the instructor's robot reveal or require a separate exercise slide. Pause only for a consequential unresolved choice.
3. **Claude reviews that proposal.** Make concrete corrections in the shared file with a short change summary; refer substantive alternatives to the lecturer. Do not create a competing render-ready source. If the renderer needs YAML or another format, generate it from the shared source rather than maintain two independent descriptions.
4. **Claude creates the PPTX.** Keep the source-to-slide mapping and preserve the explicitly chosen native slide reuse. The normal technical checks are part of rendering, not another lecturer approval stage.
5. **ChatGPT reviews the actual PPTX.** Check content fidelity, mathematics, notation, diagrams, notes and visible layout; Claude repairs actionable findings. This review does not create another render or grant acceptance.
6. **Lecturer edits the PPTX.** The edited deck takes precedence for the teaching artifact. Claude reconciles substantive edits back into the same shared content file, including changed examples, deleted slides and intentional blank discussion space. This is a semantic check, not a blind text-extraction round trip. Do not regenerate over lecturer edits or invent spoken/board content absent from the saved artifact.
7. **Lecturer gives the thumbs up.** Record completion against the saved deck version and the reconciled content. Later substantive changes reopen that artifact's status; they do not silently inherit acceptance.

This is a proposed consolidation workflow for the instructor to confirm after comparing both responses, not authorization to start rendering now. Once adopted, the explicit shared-file designation and scoped proposal/deck reviews should be reflected in the ownership conventions; initial AI-specific suggestions remain historical analysis. Routine wording and rendering fixes should not repeatedly interrupt the lecturer. Ask only about changes to teaching intent, scope, important example assumptions or unresolved notation.

**[ChatGPT 2026-10-06 — refinement after Claude round 2]** Claude's [round-2 response](lecture_suggestions/introduction_round2_claude.md) arrived during this pass and accepts the content corrections. My [review addendum](lecture_suggestions/introduction_review_chatgpt.md#addendum-after-claudes-round-2-response-arrived) records the remaining small choices and our agreement on the learning/exploration prompt. I revise Q12 steps 2/6 to fit the existing renderer: create one explicitly shared Markdown proposal before rendering, then freeze it at handoff as historical/superseded content; Claude maintains the deck's YAML against the lecturer-edited PPTX, with a generated Markdown view for review. Do not maintain the frozen proposal and YAML independently. Previews/text must correspond to the saved PPTX being reviewed, and direct read-only deck inspection remains available under the scoped review. This is a recommendation, not a claim that the synchronization tooling has been validated. Keep the instructor's requested review sequence unless they explicitly shorten it. The instructor's current comments are already logged once.

**[Claude 2026-10-06 — Q12 outcome]** RESOLVED (instructor, 2026-10-06): the workflow is adopted, with the instructor's addition of a per-deck decision file. It is written up in `docs/lecture_workflow.md`; the 1.1 decisions are in `decisions/lectures/introduction.md`. ChatGPT's exploration wording ("does not directly observe the unchosen action's outcome on that trial") replaces my "never learns", which was too strong.

## Nice to have

Moved to the shared `analysis/ideas_backlog.md` (instructor, 2026-10-06), so ideas that may be adopted in later course iterations are tracked beyond Phase 7. Add new materials or tooling ideas there.
