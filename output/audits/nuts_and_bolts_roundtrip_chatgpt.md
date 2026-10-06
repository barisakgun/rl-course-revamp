# Nuts and bolts conversion check

Review date: October 5, 2026. Scope: the instructor's saved ChatGPT deck, 15 slides. This is a conversion audit, not a curriculum or policy acceptance record.

The PPTX-to-Markdown export preserves the current deck's wording, tables, text hyperlinks and notes. It now also copies the four embedded images unchanged, including the syllabus QR code. Reconstructing from this Markdown preserves those contents but does **not** restore the original design. Continue editing the working PPTX and refreshing its derived Markdown.

- [Working deck](../../course/lectures/week01/nuts_and_bolts_chatgpt.pptx)
- [Refreshed Markdown](../lectures/week01/nuts_and_bolts_chatgpt.md)
- [Separate reconstruction candidate](../lectures/week01/nuts_and_bolts.roundtrip.candidate_chatgpt.pptx)
- [Machine-readable comparison](nuts_and_bolts_roundtrip_chatgpt.json)

## Method and result

The experiment rebuilt the deck from Markdown and its linked image files using `scripts/roundtrip_nuts_and_bolts_chatgpt.mjs`. It did not import the original PPTX, use original object coordinates, or replace the working deck. The 16:9 canvas, Calibri fonts and red headings were deliberately supplied as reconstruction defaults after inspecting the source. They were not recovered from Markdown.

`scripts/compare_pptx_content_chatgpt.py` independently read both PPTX packages, without importing the Markdown exporter. All of its content checks passed:

| Check | Result |
| --- | --- |
| Slide count, title sequence and hidden state | All 15 match |
| Visible text, including table text | All 109 nonempty paragraphs match after whitespace normalization |
| Speaker notes | All 45 nonempty paragraphs match, in order within each slide |
| Native editable tables | Both match, including all cell values |
| Text hyperlink targets | All 9 match |
| Embedded pictures | All 4 match byte for byte |
| Syllabus QR | Slide 4 image matches `course/syllabus/IntroToRL_F26.png` byte for byte |

The text check compares paragraph contents and duplicate counts within each slide; it does not assert visual reading order or original text-box grouping. Source and rebuilt slides were rendered and all 15 inspected individually with the bundled presentation renderer. The final file passed package, geometry, native-table, font and import checks. No native PowerPoint application was opened. This does not verify rendering in PowerPoint itself or scan-test the QR from a projected slide.

## Information lost or changed

| Example | Observed difference |
| --- | --- |
| Cover, slide 1 | Centered composition and mixed sizes/colors become the reconstruction's ordinary title and body layout |
| Instructor, slide 2 | Portrait moves from left to right; text positions and spacing change |
| Syllabus, slide 4 | QR remains exact but is smaller and repositioned; hyperlink changes from black to blue |
| Textbook, slide 8 | Cover moves right; book-title italics are absent because run formatting was not exported |
| Assessment, slide 10 | Table moves below the bullets because Markdown follows XML object order, not original visual order |
| Resources, slide 15 | Inherited nested bullet formatting disappears; font sizes, indents and URL wrapping change |
| Throughout | Original coordinates, text-box grouping, sizes, paragraph spacing, theme/master inheritance and image crops are not encoded in the Markdown |

Animations, transitions, comments, accessibility metadata, charts and equations are outside this comparison's fidelity checks. Do not infer general lossless conversion from this text-and-image deck. Exported image files are exact; displaying their full uncropped contents does not reproduce any original crop or mask.

## Repeating the checks

```sh
python3 scripts/pptx_to_markdown.py
python3 scripts/pptx_to_markdown.py --check
python3 -B -m unittest discover -s scripts -p 'test_pptx_to_markdown.py'
python3 scripts/compare_pptx_content_chatgpt.py \
  course/lectures/week01/nuts_and_bolts_chatgpt.pptx \
  output/lectures/week01/nuts_and_bolts.roundtrip.candidate_chatgpt.pptx
```

Seven regression tests pass, including image-byte preservation, missing-image detection, saved instructor changes, slide ordering, notes and overwrite protection. See `scripts/README.md` for the bundled-runtime reconstruction procedure. If the working deck changes later, the saved candidate and this dated report become historical; `--check` only checks Markdown/image freshness, not candidate freshness.

Source PPTX SHA-256: `6bdf13c9c25f527a9fa493266c07e841d052fd49caf206cf89f33a1cdf626dbf`.

Candidate PPTX SHA-256: `bea870d74c4d0ce5d070dccf03d346411352392a0600a7946a96e25a23c818aa`.

The working PPTX's hash was unchanged at handoff. No teaching content, accepted curriculum decisions, syllabus or course time allocation was revised. Claude-specific artifacts were not used.
