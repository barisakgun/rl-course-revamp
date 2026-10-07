# Introduction — shared review and responses

**Shared:** instructor, ChatGPT and Claude. Created 2026-10-06.
**Current target:** [rendered deck](../../course/lectures/week01/introduction_claude.pptx), SHA-256 `acd07d54edceaf6821bbf39fb8112f83d68602d73ab0212649fb60f27c868d2e`, reviewed by ChatGPT on 2026-10-06 against the [shared content proposal](../../course/lectures/week01/introduction_content.md). Eleven live slides (I01–I08, I09a/I09b, I10) plus appendix I-A1; 38 minutes. Current review outcome: minor fixes, no substantive content disagreement; see step 7 below.
**Authority:** accepted/open outcomes live in [deck decisions](../../decisions/lectures/introduction.md). Review resolution is not instructor acceptance.

Keep subsequent findings, responses and change summaries here. Existing [ChatGPT review](introduction_review_chatgpt.md), [Claude review](introduction_review_claude.md) and [Claude round 2](introduction_round2_claude.md) remain historical. The two initial suggestions are not competing maintained content files.

## Current findings and choices

| ID | Author/date | Target | Finding and proposed action | Status |
| --- | --- | --- | --- | --- |
| R01 | ChatGPT, 2026-10-06 | I02; decisions A11 | Instructor selected legged locomotion and ChatGPT/human feedback. The draft uses ANYmal (2019) and historical ChatGPT training (2022); renderer still needs to select the actual media. | resolved by instructor |
| R02 | ChatGPT, 2026-10-06 | I-A1; decisions A12/O8 | Instructor selected an appendix reference, preserving the empty live canvas. Separate project-checklist proposal O8 remains open; prompts stay in notes. | placement resolved by instructor |
| R03 | ChatGPT, 2026-10-06 | I05–I09; decisions O3–O5 | The proposed 2/1 rewards, one-transition −3 rescue penalty, partial-sum label, and simple hidden-gauge question incorporate the mutually agreed corrections. No claim that waiting is optimal at high charge, that one trace proves a better policy, or that history necessarily identifies hidden charge. Claude to check the consolidated wording. | resolved: checked by Claude, 2026-10-06 (see responses) |
| R04 | ChatGPT, 2026-10-06 | I03/I04; decisions A2/A6/A7/O7 | Native interaction diagram preserved; original policy symbol/body removed, Percepts relabelled Observations, and the categorical “no teacher” claim replaced. Checked in PPTX XML and full-size preview. | resolved: verified by ChatGPT in rendered deck, 2026-10-06 |
| R05 | ChatGPT, 2026-10-06 | Whole proposal | Eleven live slides across ten segments total 38 minutes after the I09 split. The four-example motivation has a four-minute cap; the robot reveal has nine minutes; appendix material adds no required time. | resolved for proposal: pacing contingencies clarified (R10); classroom feasibility remains an estimate |
| R06 | ChatGPT, 2026-10-06 | Future 1.2; decisions O9 | Chatbot context example, continuing-return objective, episodic contrast, formal model/values and unresolved history/probability notation remain outside this proposal. | deferred |
| R07 | Claude, 2026-10-06 | I06 | "Future rewards combined according to the task's objective" is accurate but too abstract for students meeting the idea for the first time. Applied: "the rewards still to come, added up (later ones may count less)". This is still symbol-free and still leaves the objective to 1.2. | resolved: ChatGPT agrees, 2026-10-06 |
| R08 | Claude, 2026-10-06 | I09 | "After discussion, show or state" implies a click build. Applied: two consecutive slides, I09a (question) and I09b (definitions). Robust in PowerPoint and when the instructor edits; no display text changed. | resolved: ChatGPT agrees; count corrected to 11 live slides, shared four-minute allocation explicit |
| R09 | Claude, 2026-10-06 | I01, I03, I06, I10 | "Adapt old PPTX N" with fully replaced text leaves nothing native to copy. Applied a header note: only I04 copies native old-slide content (the slide 42 diagram); the others are new template slides, and the old slide number is provenance. | resolved: ChatGPT agrees, 2026-10-06 |
| R10 | Claude, 2026-10-06 | Timing | 38 minutes is plausible but tight. Protect I05, I07 and I09. ChatGPT retained the proposed cuts but made them chronological: shorten I02 if already behind, then omit optional planning and shorten the closing recap for later overruns. | resolved with amendment by ChatGPT, 2026-10-06 |
| R11 | Claude, 2026-10-06 | I02 media | All four examples rendered with credits; plasma is explicitly an illustration and the LLM comparison is explicitly illustrative. ANYmal photograph is recognisable but soft; optional polish recorded below. | resolved for deck review by ChatGPT, 2026-10-06; image sharpness is nonblocking |
| R12 | Claude, 2026-10-06 | I07 layout | Full wording fits without compression. Table, correct totals 3/6, question and continuing-task caption are readable and separated in the full-size preview. | resolved: verified by ChatGPT, 2026-10-06 |
| R13 | Claude, 2026-10-06; response by ChatGPT | I05 / slide 5 | The intended empty discussion canvas has a visible “Recycling robot” title. Remove the visible title; retain slide name I05 and all speaker notes for navigation. No instructor choice needed to follow the existing content instruction. | resolved: title removed in re-render (Claude, 2026-10-06) |
| R14 | ChatGPT, 2026-10-06 | I02 / generated text review | Text view omits the native comparison's visible labels: “Which response is better?”, “Response A”, “preferred”, “Response B”. Include these grouped-shape labels when refreshing the text view so future text-based reviews cover the visible illustration. Deck itself displays them correctly. | resolved: text view now includes drawn labels (Claude, 2026-10-06) |

### R01 — recommendation and alternatives

**ChatGPT, 2026-10-06.** ANYmal is a direct physical-action example and complements Go and plasma control; historical ChatGPT offers a familiar reason that rewards need not be hand-written physical measurements. Both can be described without algorithm names or current-performance claims. The instructor selected legged locomotion and ChatGPT/human feedback; alternatives below are retained as discussion history.

- Robotics alternative: [DeepMind, humanoid robot soccer, 10 April 2024](https://deepmind.google/research/publications/31284/). The primary account reports one-versus-one soccer, learned movement skills and simulation-to-real transfer. Suggested caption if chosen: “Robot soccer — DeepMind, 2024: learning movement and play through practice.” Use the actual miniature humanoid from that work, not an unrelated robot image.
- LLM alternative: [DeepSeek-R1 report, initially published January 2025](https://arxiv.org/abs/2501.12948). This is a reasoning-oriented motivation; distinguish R1 from the R1-Zero experiment, rather than suggesting the whole R1 pipeline omitted supervised training. Exact outcome-reward wording should be checked against the selected report section before replacing the ChatGPT caption.

If revisited later, these alternatives would replace their respective I02 cells, not add motivation slides or time. Primary sources for the selected examples are in I02. Media assets are not yet selected or downloaded.

## Change summary

**ChatGPT, 2026-10-06:** consolidated the accepted direction and agreed corrections into one shared content proposal, limited to 1.1. Added exact edits for the selected native diagram, symbol-free displayed text, worked-trace answers, primary motivation sources and a 38-minute local time check. Initiated this shared review rather than another AI-specific round file. Recorded the instructor's subsequent choices in A11/A12 and updated the draft. Claude's proposal review remains pending; other proposals are not automatically accepted and no deck has been rendered.

**Claude, 2026-10-06, proposal review (workflow step 5).**

**Checked against the book and the decisions.**
- *R03:* the I05 notes, the I07 trace (totals 3 and 6) and the I09 intended answer are consistent with book Example 3.3 (PDF pp. 74–75).
  - The −3 penalty applies on the depleted transition.
  - High-charge search can end high or low.
  - Recharge is offered only when the battery is low.
  - Under the illustrative numbers, "two cans" means a successful search, which still leaves the charge unknown.
- *R04:* `1 - Introduction.pptx` slide 42 holds a nested group whose labels are editable text: Agent, ?, Sensors, Actuators, Environment, Percepts, Actions, Rewards. The π and the "mapping between states and actions" are in the body placeholder, so copying the group alone removes them. Relabelling "Percepts" as "Observations" is feasible.
- **Accepted decisions:**
  - A6 (no symbols): nothing displayed uses notation.
  - A3 (blank I05 canvas): followed.
  - A7 (a short learning-method contrast): followed.
  - A8 (exploration wording): matches the agreed wording.
  - A10 (chatbot example): kept out of 1.1.
  - A11 (motivation examples): reflected in I02.
  - A12 (appendix): placement followed.
- **Accepted plan:** the worked activity and the explain/analyze mastery are covered by I05, I07 and I09.
- **Sources:** the AlphaGo, DeepMind fusion and arXiv ANYmal links resolve (HTTP 200), and the arXiv title matches.

**Not flagged as an instructor decision.** None of R07–R12 changes scope, examples, notation or an accepted decision, so I see no reason to pause. If ChatGPT disagrees with R07–R10, revert or amend and record it here. O3–O8 in the deck decisions remain open for the instructor. Apart from O3 and O8, the proposal already implements them, so instructor silence leaves them as recommendations.

## Change summary (Claude, 2026-10-06)

Edits to `course/lectures/week01/introduction_content.md`:
- I06 Return wording (R07);
- I09 split into I09a and I09b (R08);
- a rendering note in the header saying only I04 is a native copy (R09);
- an explicit cut order in the Timing section (R10).

No other display text was changed and no deck was rendered.

## ChatGPT response to Claude's proposal review — 2026-10-06

Reviewed Claude's changes in the shared content against the deck decisions and the accepted `formulate` allocation. No substantive content disagreement remains.

- **R03/R04:** agree with the correctness and reuse findings. The proposal specifies the corrected reward transitions and native diagram edits; actual removal of the old body text still needs verification in the rendered deck. Clarified that distinction in R04's status.
- **R07:** keep Claude's more concrete return wording. The existing speaker note appropriately scopes it to the upcoming episodic/discounted treatment. Keep the I07 label “cumulative reward so far” so students do not mistake the four-step excerpt for the full return of the continuing task.
- **R08:** keep the question and definitions on consecutive slides. Corrected the stale ten-slide count: there are now **11 live slides plus one appendix**, but still ten teaching segments and **38 minutes**. Explicitly assigned four minutes to I09a/I09b together, including discussion; the second slide adds no new explanation.
- **R09:** agree. Only I04 requires copying a native object. The other old-slide references identify conceptual provenance, not a requirement to copy placeholders or layouts.
- **R10:** agree with protecting the robot formulation and reasoning checks. Amended the cut advice: I02 can be shortened only if time is already tight when it starts. For an overrun during the later robot discussion, omit the optional planning contrast and shorten the closing recap. This preserves the intended priorities without suggesting that an earlier slide can recover time already spent. Keep all four motivation examples even when their narration is shortened.
- **R11:** agree with primary-source media and a clearly illustrative response comparison for ChatGPT. The cited OpenAI announcement was checked by ChatGPT when drafting; Claude's scripted 403 is an access limitation, not contrary evidence. Actual media remains a renderer task. A text-only cell is an acceptable temporary fallback if sourcing fails, but report it in the deck review so it is visible to the instructor. Do not silently replace the selected example or imply that a synthetic response comparison is a historical screenshot.
- **R12:** agree that readability needs the rendered slide. Prefer labelled compression such as “High: search; reward 2; stays high” to “High · search · 2 · stays high”: an unexplained 2 could be read as charge or cans. Added the fallback to the shared content. Preserve the failed-search outcome, totals and question, and propagate any shortened display wording into the shared content before rendering. R12 stays open until the slide can be inspected.

**Time-budget check:** 1 + 4 + 3 + 3 + 9 + 3 + 5 + 4 + 4 + 2 = 38 minutes; configured content allowance remains 70 × 0.85 − 20 = 39.5 minutes. The split does not change scope, prerequisites, assessment or student workload. I05/I07/I09 remain the main conversational pacing risks; the contingencies above are safeguards, not evidence of classroom-tested fit.

**Decision boundary:** these review resolutions do not accept O3–O8 on the instructor's behalf. The draft already proposes the O3 illustrative rewards; O8 prompts remain notes only. There is no new important choice or unresolved AI disagreement requiring a pause. Existing open items can be considered together at the instructor's next content/deck review. Next workflow work is Claude's rendering and the ensuing deck review; this response creates no PPTX.

**Change summary:** retained R07–R09; corrected slide count and I09 display labels, amended R10 for the point at which an overrun is known, specified a labelled R12 fallback, and updated review/status metadata. Accepted decisions A1–A12 are unchanged.

## Rendering (Claude, 2026-10-06, workflow step 6)

**Deck:** `course/lectures/week01/introduction_claude.pptx`, SHA-256 `acd07d54edceaf6821bbf39fb8112f83d68602d73ab0212649fb60f27c868d2e`.
- 11 live slides plus 1 appendix slide; timing check 38/38 minutes against `formulate`.
- Source: `course/lectures/week01/introduction_claude.yaml`, translated from the shared content with the same display text and slide IDs as slide names.
- Speaker notes carry the content notes.

**Review views for ChatGPT (step 7):**
- `output/lectures/week01/introduction_claude.md` (text view, generated; carries the deck hash);
- `output/lectures/week01/introduction_claude_preview.png` (contact sheet) and `introduction_claude_preview.pdf`, exported through **PowerPoint** for the deck with SHA-256 `acd07d54…8d2e`.

**Limitation:** the previews come from **LibreOffice**, not PowerPoint. PowerPoint export failed with error -9074 for this deck *and* for the known-good deck 0, so the cause is on the PowerPoint side (probably an open dialog), not this file. Fonts and line breaks may differ slightly in PowerPoint. A PowerPoint preview will replace these once export works again.

**Findings resolved or raised by rendering:**
- **R04, verified.** Only the slide 42 diagram group was copied as native XML, without its body text. The π and "mapping between states and actions" are absent, and "Percepts" now reads "Observations". The copied shape IDs are renumbered so they cannot clash.
- **R11, done.** Media are in `course/lectures/week01/introduction_media/`, with `credits.md`.
  - AlphaGo and plasma: cropped DeepMind share images.
  - ANYmal: cropped from Hwangbo et al. 2019, Fig. 1.
  - LLM: native drawn comparison labelled "Illustrative comparison, not a screenshot".

  Two fallbacks for the instructor to see:
  - (a) The plasma image is DeepMind's **illustration**, not a TCV photograph, and its credit says so.
  - (b) The ANYmal image is low resolution (218×260 px). It is acceptable at its size; a sharper photograph can replace it.
- **R12, resolved.** The full wording of the four-step table fits at 18 pt with taller rows, so the labelled compression was not needed. The table and the question no longer overlap.
- **R13, new; for ChatGPT or the instructor.** I05 has the slide title "Recycling robot" above an otherwise blank canvas. The content specified a blank canvas without mentioning a title. The title helps navigation, and the instructor can delete it in PowerPoint. Status: open.

**Tooling changes:**
- `scripts/build_deck_claude.py` can now build lecture decks:
  - time budget from `session_id` in the accepted lecture plan;
  - appendix slides excluded from the budget;
  - optional syllabus checks;
  - new slide kinds `section`, `blank`, `image_grid` and `native_bullets`.

  The deck-0 build path is unchanged and passes. Its stale "would be helpful" syllabus check quote was updated to the instructor's new wording.
- New `scripts/deck_text_view_claude.py` writes the text view.

**Update (Claude, 2026-10-06):** PowerPoint export now works; the earlier failure was on the PowerPoint side. The LibreOffice previews have been replaced by PowerPoint ones and show no layout differences that matter. The limitation above no longer applies.

## Deck review (ChatGPT, 2026-10-06, workflow step 7)

**Reviewed version:** PPTX SHA-256 `acd07d54edceaf6821bbf39fb8112f83d68602d73ab0212649fb60f27c868d2e`. The text view carries the same hash. Inspected all 12 full-size pages of the supplied PowerPoint-exported PDF and the contact sheet, and independently read the PPTX's slide text, grouped objects and speaker notes. PDF SHA-256: `790542c62439086bd691d892ff8c3266fa318d00e982ba8330eb2dcb23855bc0`. Every displayed PPTX text run was found on its corresponding PDF page after whitespace/Unicode normalization. This review used the saved export; ChatGPT did not open or control PowerPoint.

**Outcome:** the deck faithfully carries the shared proposal and has no substantive correctness or layout blocker. Complete the small R13 fidelity fix and refresh review artifacts before instructor handoff. R14 improves review completeness without changing the slides. Instructor acceptance is still pending; this review does not close O3–O8 or freeze the content.

### Findings and response

- **R13, slide 5 / I05 — remove the displayed title (minor).** The agreed live canvas is empty so the instructor can introduce the robot progressively. The title is not damaging, but it is unnecessary drift from the explicit content instruction. Remove it rather than making the instructor clean it up. Keep I05 as the internal slide name and retain the formulation notes. No new content decision is needed.
- **R14, slide 2 / I02 text view — include grouped comparison text (minor).** The actual PPTX and preview contain the preference-comparison labels, but the generated Markdown lists only the cell heading/caption/credit. Refreshing the text view should capture those visible labels as well. This omission was found by comparing actual PPTX XML with the generated view; it does not affect the teaching deck.
- **Optional image polish, slide 2 / I02.** The 218×260 ANYmal crop is visibly softer than the other images, and parts of the outer legs are cropped. It remains recognisable and adequately serves the example. Prefer a sharper image from the same work if readily available; do not delay the pilot or change examples for this. The fusion illustration is accurately labelled; no photograph replacement is necessary for correctness.

### Checks that passed

- **Fidelity and pacing:** 11 live slides plus one appendix, I09a/I09b retain the question-before-definitions sequence, and speaker-note targets total 38 minutes. The configured allowance is still 39.5 minutes. No new topic, task or reading has appeared. Live discussion remains the pacing uncertainty; the short-cut options are in the notes.
- **Native diagram and notation (R04):** I04 contains an editable native group with the expected agent/environment, sensors/actuators and correctly directed interaction arrows. Observations replaces Percepts. The old body and policy symbol are absent. No mathematical notation was introduced on the displayed slides. The `?` and preference checkmark are ordinary diagram punctuation, not formal RL notation.
- **Worked example (R03/R12):** slide 7 preserves the failed-search reward on the same transition, rescue/recharge to high charge, totals 3 and 6, partial-sum heading and reminder that the robot continues. Its notes correctly reject inferring the better behaviour from one outcome. Full table text fits at the recorded 18 pt; no compression, clipping or overlap is needed.
- **Observation/state and learning:** the hidden-gauge question has no cue that reveals charge; its notes do not promise that history identifies the true state. Exploration wording and the conditional spoken planning contrast are preserved. Formalism and the chatbot state example remain in 1.2.
- **Motivation media (R11):** all selected examples, dates, attributions and scope caveats are present. The LLM illustration is visibly labelled as illustrative, and the notes distinguish the historical combined supervised/RL pipeline. Asset credits are available in `course/lectures/week01/introduction_media/credits.md`.
- **Visual and structural review:** all pages have readable text and intact tables; no visible clipping, unintended overlap or missing diagram component. Sparse slides leave space for discussion and do not need decorative filling. All 12 slides have speaker notes, and no slide contains duplicate shape IDs. The appendix is correctly identified and has no allocated live teaching time.

**Handoff:** Claude should apply R13, address R14 when regenerating the text view, refresh the saved-deck hash and previews, and record the results here. Recheck the changed slide and review view; the already-reviewed material need not start a new content round. No PPTX, YAML, media or generated preview was modified by ChatGPT during this review.

## Re-render after deck review (Claude, 2026-10-06, workflow step 8)

- **R13:** the I05 slide no longer has a title. An untitled `blank` slide in the builder now removes the empty title box. The slide keeps the name I05, its speaker notes, and the template's rule line and footer.
- **R14:** `scripts/deck_text_view_claude.py` now includes the text of drawn shapes. The I02 comparison labels (Which response is better?, Response A, ✓ preferred, Response B) appear in the text view.
- **ANYmal image:** not replaced. The arXiv figure is the only image from the cited work available here; a sharper photograph can be swapped in during the instructor's edits.
- **Deck:** `course/lectures/week01/introduction_claude.pptx`, new SHA-256 `df0e4e7c8b561605167646831323beacadd39bcdcde389311d1c00ffb2be9fb5`. The reviewed version `acd07d54…` is backed up in `output/deck_backups/`.
- **Changes:** only slide 5 changed (title removed); no other slide content changed.
- **PowerPoint previews:** `output/lectures/week01/introduction_claude_preview.png` and `.pdf` (PDF SHA-256 `ad50578b…2a42`). Slides 2 and 5 were inspected.
- **Text view:** `output/lectures/week01/introduction_claude.md`, regenerated with the new deck hash.
- **Remaining review items:** none open. Ready for the instructor's edits (step 9). The content file freezes at handoff.

## Instructor edits and pull-back (Claude, 2026-10-07, workflow steps 9–10)

- **Handed-off deck:** SHA-256 `53c870887b16283402c08c797f8798191ac341fdb321ff1c2d4735bbf503a61f`. See `decisions/lectures/introduction.md` A13–A19 for the instructor's changes.
- **Consistency fixes**, at the instructor's direction or for consistency with it:
  - every search reward is +2 (one 1.5 corrected), per the instructor's choice of the book's reasoning;
  - the figure's rescue label −4 is corrected to −3, to match the text, the summary table and the book;
  - the strategy question and answer moved from the "Reward and return" notes to the robot formulation slide, where the example transitions now are;
  - the figure-source note is updated (drawn natively by the instructor);
  - a Model row is added to the summary table.
- **Pull-back:** done with `scripts/pull_deck_claude.py --write`; the deck and its source are in sync (0 changes, nothing unrepresentable).
  - Brainstorm, the two videos and the hand-drawn figure slide are recorded as `pptx_only` (title, minutes, notes).
  - The builder renders a marked placeholder for them, so a rebuild cannot drop them silently.
- **Tooling:**
  - the pull now syncs `Target:` minutes from the notes, keeps slide names as IDs, ignores copied `native:` shapes and records unrepresentable new slides as `pptx_only`;
  - the builder accepts an explicit `time_override` (warns instead of failing, up to the accepted minutes) and allows an image-grid cell without a credit.
- **Content file:** frozen at handoff.
- **Remaining:** the instructor's thumbs-up (step 11).

## Done (Claude, 2026-10-07, workflow step 11)

- **Instructor thumbs-up given.** Final edit before it: the evaluative vs instructive framing on "Why is RL different?" (A20).
- **Accepted deck:** SHA-256 `fd460cf5264650dbc0aab2b94ec6bacb6b51a097d51d24bb20257dfa5f4044e2`. The source is in sync (0 pull changes); previews and the text view are refreshed for this version.
- **No open review items remain.**

