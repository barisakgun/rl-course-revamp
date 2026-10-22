# Proposal release preparation

ChatGPT, 2026-10-22. Recommendations and draft-artifact review, not accepted grading policy.

## Instructor review update

The instructor has now accepted both guideline documents (2026-10-22). Their accepted PDFs have moved to `course/projects/handouts/`, with editable TeX sources retained in place. The rubric remains a first-pass grading reference, not part of this acceptance. Publication is not recorded. Historical review choices below do not reopen the accepted handout instructions.

The instructor edited the two guideline TeX files and removed their visible draft labels. Those saved files now supply the current wording. The proposal emphasizes revisability/candidate approach, broadens success-metric examples and clarifies title placement, LearnHub-only submission and upload checking. The LLM instructions permit grouping members with similar use, request at most three examples, mention CLI logs, and condition the project-selection prompt on relevant AI use. Preserve these edits rather than restoring the initial draft.

The rubric's first pass found no significant issues. Detailed rubric review is deferred to grading; the initial numeric weights and penalty recommendations are not newly frozen. The proposed packaging and disclosure details below are historical preparation choices; consult the instructor-edited handouts for current wording. Publication is not recorded.

Wording clarification resolved by the instructor: retain the syllabus late-day allowance, with no further submissions or replacement files accepted once grading begins. The accepted cutoff is recorded in `decisions/project_decisions.md` under the proposal milestone and reflected in the handout. No grading-start date has been specified.

## Drafts and sources

- [Proposal guidelines](../course/projects/proposal_guidelines_chatgpt/main.tex): editable teaching handout. Retains the introduction, tentative formulation, related-work and evaluation spine of `sources/current_course/ProposalSpring21.pdf`, page 1. The October 22 instructor clarifications narrow related work, make the baseline tentative, broaden evaluation/feasibility and set two pages plus references. Includes the formulation checklist assigned to proposal preparation in `decisions/lectures/introduction.md`, O8.
- [Rubric](../course/projects/proposal_rubric_chatgpt/main.tex): proposed weights, descriptors and grading guidance; this TeX is the single editable copy of the proposed rubric.
- [LLM-use instructions](../course/projects/llm_use_written_reports_chatgpt/main.tex): accepted reusable core plus a short proposal-specific section. This TeX is the single editable copy of the operational instructions. Later reports can replace that section with their own prompts; those supplements are not drafted or imposed here.

All use the A4, 2.54 cm margin, serif text and centered course-heading style of `sources/NonRL/COMP341_example_hw.tex`, with compact spacing. Old programming-specific examples, archive rules and penalties are not transferred. Student report typography comes from the old proposal handout, not the example's programming instructions. Draft renders belong in `output/projects/`; accepted handout PDFs are in `course/projects/handouts/`.

## Accepted versus proposed

Accepted facts and the student-ownership boundary are in `decisions/project_decisions.md`. The deadline is stored there once; the TeX displays it as a teaching artifact. The requested release date is omitted. The frozen syllabus continues to govern disclosure, responsibility, academic integrity and writing quality.

Initial review choices (historical; superseded by the review update above where applicable):

1. Adopt or adjust the proposed rubric weights and descriptors. They assess proposal-stage reasoning, not completed algorithms or results. Do not reward novelty, exhaustive literature coverage or more compute.
2. Approve one separate usage-report PDF per team, covering all members, excluded from the main report page limit; a short non-use declaration suffices. This packaging/page allowance is a recommendation, not inferred acceptance of the earlier suggestion.
3. Approve the concise disclosure structure: all purposes listed, AI products and tool actions identified, one example for a single use or two/three selected examples for broader use, maximum three. Screenshots with annotations or relevant document/tool-action excerpts are acceptable evidence.
4. Set any operational handling of incomplete disclosure or prohibited delegation. The draft does not invent a zero-credit rule or numeric penalty. The assignment-specific rule is not extended to project coding.

The ownership boundary allows students to explore AI-suggested options while requiring their own reasoned selection, formulation and substantive report content. It prohibits handing over project choice or whole-report authorship, even across several prompts. Checking and editing assistance must be disclosed. AI tool actions (search, reading files/papers, document edits, calculations) are covered; manual non-AI tool use need not be logged.

## Scope, time and assessment check

The proposal still assesses formulation and an initial experimental plan. Its existing introductory/MDP prerequisites support the checklist. The baseline is tentative; no deep-RL implementation, working environment, results, full protocol or advanced-method mastery is added. Baseline implementation and preliminary results stay at later checkpoints.

This replaces a potentially expansive survey and transcript dump with a focused literature connection and selected disclosure evidence. No live teaching, required reading/video unit or milestone is added. Keep the existing 0.85 usable-content fraction and lecture allocations. The proposal's 3–5 active-hour estimate remains unpiloted; disclosure preparation should be included in it rather than silently treated as free. A planning estimate of 10–20 minutes for a short usage summary with already available excerpts is an inference, not a demonstrated bound. Large screenshot collections or reconstructed histories would exceed that intention; neither is requested. Confirm workload after release.

Before publishing the existing overview deck, update its proposal due-date TBD from the accepted timestamp. Do not rebuild the instructor-editable PPTX from its frozen content input. Its other dates remain TBD. The present task drafts documents and leaves that deck unchanged.
