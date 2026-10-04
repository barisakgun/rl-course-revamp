# Nuts and bolts revision plan

Prepared 2026-10-04. Phase 7 content planning for the instructor-supplied `sources/current_course/0 - NutsAndBolts.pptx` (14 slides, 16:9). This is an artifact recommendation, not a change to accepted curriculum or policy.

## Basis and deliverable

The frozen `course/syllabus/syllabusFall26.docx` governs student-facing policy. Its generated text view was checked against the frozen artifact. Relevant accepted assignment, project, grading and reading decisions were also inspected. Original PowerPoint text and external hyperlink relationships were inspected directly. All source and revised slides were subsequently rendered and visually inspected on October 5, 2026.

The editable [slide-content source](../course/lectures/week01/nuts_and_bolts.md) supplies copy and speaker notes for the [revised PPTX](../course/lectures/week01/nuts_and_bolts.pptx). It retains 14 slides while replacing the duplicate opening, resource catalog and outdated programming/LLM guidance. The source deck remains unchanged as evidence. The [rendered overview](../output/lectures/week01/nuts_and_bolts_preview.png) is generated from the revised deck.

## Slide changes

| Source slide | Finding | Proposed treatment |
| --- | --- | --- |
| 1 | Spring 2025 title | Update to COMP438/538, Fall 2026. Use the instructor name without an unverified academic rank. |
| 2 | Repeats the course title | Replace with a brief course map matching the frozen syllabus. |
| 3 | Contact information includes an office number and reply-time promise absent from the final syllabus | Retain email, office-hour policy and TBA assistants. Omit unconfirmed office/reply commitments. |
| 4 | Long background introductions could consume the briefing | Keep a brief background/interest check with a 90-second target. |
| 5 | Blackboard wording, QR/image and old Google Drive syllabus hyperlink | Use KU Hub and current class time/room. Remove the old QR/link in the PowerPoint revision. No current direct syllabus URL or upload has been verified. |
| 6 | Communication slide promises specific Hub resources | Retain course materials, announcements, submissions and email responsibility without promising a complete past-exam/code collection. |
| 7 | Required/recommended books and a time-sensitive claim about deep-RL books | Retain Sutton–Barto as the syllabus reference. State that no readings are assigned. Remove the unsupported publishing-landscape claim. |
| 8 | External resource catalog | Replace with expected preparation. No new resource-selection work or reading workload. |
| 9 | Attendance and fixed break promises | Keep participation and no attendance tracking; omit fixed break commitments. |
| 10 | Three assignments, two midterms/40%, project/40% | Use four planned individual assignments/20% with conditional lowest-drop rule, three midterms/45%, project/35%, no final. Move late policy to slide 14. |
| 11 | Old project milestones and weights | Use five current milestones, totaling 35%, revised team policy and evaluation purpose. Remove the promise of details in Week 2. |
| 12 | Older LLM guidance | Replace with disclosure, ownership, report requirement and assignment-specific no-credit rule. |
| 13 | Programming/math warning | Move preparation to slide 8. Use this slide for project writing standards and exam/academic-conduct rules. |
| 14 | “Code everything yourself” conflicts with supplied scaffolds and permitted LLM assistance | Replace with submissions and late policy, plus a pointer to full exam policies. |

## Time and prerequisite consequences

No curriculum addition, mastery change, assessment change or new prerequisite is proposed. This revises the existing syllabus briefing. It does not introduce the rest of Week 1's teaching material.

- Draft delivery targets total 16 minutes plus four minutes for questions, within the configured 20-minute briefing.
- Week 1.1 retains 38 teaching minutes. Its 20-minute briefing plus teaching uses 58 of 70 contact minutes, leaving 12 minutes.
- Week 1.2 retains 58 teaching minutes, leaving 12 minutes.
- Across Week 1, 96 teaching minutes fit the configured 99-minute content capacity after the briefing overhead. The remaining 24 contact minutes comprise the 21-minute generic reserve plus three usable minutes.
- The existing semester allocation remains 1,440 teaching minutes plus 19 additional administration minutes, with 68 usable minutes unallocated. Briefing time is already deducted separately and must not be charged twice.
- The full-class introduction round and external-resource tour are displaced by concise orientation and updated policy explanation. Keep the course map at the level of labels; explaining those algorithms here would consume time needed for RL formulation.

Arithmetic fit is only a pacing estimate. Rehearse the final slides and keep detailed project instructions and policy examples for their later handouts. Do not cover extra administrative detail by taking the planned 38 minutes for RL formulation.

## Remaining instructor review

- Review the proposed copy, especially whether to retain any instructor-specific contact or lecture practices omitted from the final syllabus.
- A KU Hub landing-page link replaces the outdated syllabus link and QR. A current direct syllabus URL can be substituted when provided.
- No uploaded-syllabus check, native PowerPoint application review or class delivery has occurred.

## October 5 implementation

The dependency tool became available in the Codex desktop app. `scripts/revise_nuts_and_bolts.mjs` imports the original PPTX with the bundled presentation runtime and applies the content source. Original dimensions, masters, red headings and Calibri/Calibri Light fonts are retained, together with the instructor photo, WALL-E image and Sutton–Barto cover. Obsolete resource images and the old QR were removed. Grading and project milestones are native editable tables. All 14 slides contain speaker notes.

The final PPTX passed package, geometry, font-policy, native-table and import checks. Every rendered slide was reviewed at full size. A cover-formatting issue was repaired and rerendered; the other 13 rendered slides were unchanged. A separate content check verified all proposed slide text, current hyperlink targets, note count and the 100% grading / 35% project-milestone totals. The source PPTX and frozen syllabus fingerprints remain unchanged. PowerPoint was not opened or controlled.

The content and pacing remain a teaching-artifact proposal for instructor review; this export accepts no new curriculum or policy decision.
