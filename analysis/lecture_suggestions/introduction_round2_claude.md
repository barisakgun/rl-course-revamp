# Introduction and MDPs: Claude, round 2 (after instructor comments)

**[Claude 2026-10-06]** This responds to the instructor's comments of 2026-10-06, which were sent identically to both AIs. It covers:
1. why only the book and old slides were used;
2. the open questions left after both reviews;
3. a scan of the other sources' introductory lectures;
4. a recommended route to render-ready content.

These are recommendations only, and no render-ready content has been written. The instructor's comments are not yet in `decisions/decision_log.md`; see section 5.

## 1. Book and old slides only: instruction or assumption?

**Assumption.** No instruction restricted the suggestions to these two. The instructions say:
- AGENTS.md: "keep lecture planning lightweight, using the accepted lecture plan and existing sources";
- decision log, 2026-10-06: "reuse the existing sources and accepted lecture plan".

The configured reference courses are existing sources, and `output/lectures/session_sources.md` links their pages for 1.1.

I narrowed this to the book and the old decks myself. My reasons were reuse first (my Q8 criterion 4) and the note in my Q8 reply that the running example should come from the book. That note limits only where the running example comes from, not which sources to consult. ChatGPT's index-review caveat ("linked material is not a requirement to cover it all") concerns how much to cover, not whether to look. Section 3 makes up for this on the introductory lectures.

## 2. Open questions after both reviews

### Settled by the instructor's comments

| Item | Outcome |
| --- | --- |
| Running example for 1.1 | Recycling robot. Gridworlds come later. |
| Cuts | Accepted in general: AI/ML brainstorm, coins, history, applications tour, rational-agent review, Intro 44's "episodic vs sequential". |
| Interaction diagram | Intro slide 42 (PPTX). |
| Learning vs planning | Brief contrast, only where it fits naturally. A natural place: when Q1 asks whether one sampled day settles which behaviour is better. "If the robot knew the probabilities it could compute ahead (planning); it doesn't, so it must learn from days like this (learning)." About 1 minute, no extra slide. |
| Introducing the robot | Instructor builds it up gradually on an empty slide, with no story slide. |

### ChatGPT's findings on my suggestion: all accepted

| ChatGPT finding | My response |
| --- | --- |
| 1. Q1 premise | **Accept; my error.** A low-battery search does not "earn +2 now": failure gives −3 on that transition. Use ChatGPT's wording: "at low charge, search might give +2 or −3; recharge gives 0. Does this one day settle it?" Use high-charge *search (2) vs wait (1)* for the real immediate-vs-later tradeoff. |
| 2. Hidden-battery question | **Accept.** The book's action sets reveal the charge, because recharge is offered only when the battery is low. "At base" was also unspecified. Use the simpler verbal question: "You just collected two cans: is the battery high or low? What earlier events would help?" Choice between search and wait only. My search-count answer stays at most an instructor aside, with its assumptions stated. |
| 3. Four-step totals | **Accept.** Label the table "first four steps: cumulative reward so far". 1.2 must specify the return objective for the continuing robot and keep a brief episodic contrast. |
| 4. Pacing and Intro 51 | **Accept.** The vacuum question (Q2) becomes backup. Observations stay verbal. Edit Intro 51 so it does not say "no teacher/labels" as a universal rule: reward evaluates an outcome without saying which action was correct. |
| Its reply to my F5 | **Accept the correction.** Moving left until a wall appears does not identify the row. That claim was wrong, though it does not affect the robot. |

### Still open (small; instructor answers needed only for O1 and O2)

- **O1. Symbols in 1.1.** With Intro 42 and verbal observations, 1.1 can stay symbol-free. S_t, A_t, R_{t+1} would then arrive in 1.2 on MDP deck slide 3, edited. My original segment 2 explained R_{t+1} in 1.1. *Recommendation:* symbol-free 1.1. 1.2 (58 min) absorbs about 1 minute.
- **O2. A reference slide after the empty-slide build-up.** The board work is gone after class. *Recommendation:* one slide after the discussion with the book's formulation (states, action sets, rewards) and the formulation checklist. It is a reference for students and the Week 4 proposal, not a teaching slide. Instructor's choice.
- **O3. Numbers in 1.1.** Rewards of search 2 and wait 1 (my simplification; the book only requires search > wait) and the book's −3 rescue, with no probabilities. *Recommendation:* keep these numbers. The probabilities come in 1.2.
- **O4. Modern hook and exploration.** New, from the source scan (section 3).

## 3. Other sources: introductory lectures only

Scope: the first lecture of each reference course, read as extracted text on 2026-10-06, plus Sutton's local intro and MDP-examples decks. Downloads were kept in session scratch space, not mirrored into `sources/`.

| Source | URL / file |
| --- | --- |
| Silver, Lecture 1 | https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/intro_rl.pdf |
| CS234 (Winter 2026), Lecture 1 | https://web.stanford.edu/class/cs234/slides/lecture1post.pdf |
| CS224R (2026), Lecture 1 | https://cs224r.stanford.edu/slides/01_cs224r_intro_2026.pdf |
| CS285, Lecture 1 | https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-1.pdf (not in the session index, which links lec-4) |
| Sutton (local) | `sources/sutton/1-admin-and-intro.pdf`, `4-mdp-examples.pdf` |
| Abbeel (local) | `l1-mdps-exact-methods.pdf`: skipped; its intro part only defines the MDP tuple |

### What they do that our 1.1 plan does not

Inference about usefulness is mine; slide content is as observed.

1. **Exploration as a defining feature.**
   - CS234 p. 13 frames RL as optimization + delayed consequences + exploration + generalization. Its p. 17 says the agent only gets a reward for the decision it made and doesn't know what would have happened otherwise.
   - Silver pp. 40–42 has exploration and exploitation in Lecture 1.
   - *Gap:* neither suggestion mentions exploration.
   - *Proposal:* one sentence in the opening, on the robot: "on a day it searched, it never learns what waiting would have given". This is also the honest version of the evaluative-feedback point in the Intro 51 edit. Exploration itself stays in Weeks 4 and 9. About 30 seconds.
2. **A current-relevance hook including LLMs.**
   - CS234 pp. 2, 10–12: DeepSeek-R1, ChatGPT, o1, IMO.
   - CS224R p. 22: "nearly all modern language models use some form of RL for post-training".
   - CS285 p. 23: RLHF.
   - *Gap:* both suggestions cut the applications tour. That is fine, but 1.1 then never says why RL matters now, although the course ends with RL for LLMs.
   - *Proposal:* replace the optional montage with one slide, under 1 minute: robots/games and LLM post-training. Point to deck 0's roadmap. No "state of the art" claims; dated examples only.
3. **A modern observation-vs-state example.**
   - CS224R p. 37: for a web or chat agent, the observation is the user's most recent message and the trajectory is the conversation.
   - *Proposal (optional, about 1 minute):* after the robot question, ask "for a chatbot, is the latest user message enough to decide the reply?" Answer: no, the conversation so far matters. It is quick, needs no model assumptions (unlike the hidden battery), and links to Week 13. Use it as a backup if the robot question stalls.
4. **Students formulate a problem themselves.**
   - CS234 pp. 28–29 has an AI-tutor decision-process exercise.
   - CS224R p. 38 has a think-pair-share: driving, web agent, poker.
   - This supports the pair activity; nothing to add. Old Intro 52 (formulation brainstorming) can remain optional practice using the checklist.
5. **Stochastic policies early.** Silver p. 26, CS234 p. 42 and CS224R p. 42 all introduce them. Already adopted in the Intro 19 wording.
6. **Reward vs value phrasing.**
   - Sutton `4-mdp-examples` p. 17: "Pleasure = immediate reward ≠ good = long-term reward".
   - Mountain Car (p. 20): "−1 until goal, no discounting".
   - Optional one-liners; no change needed.

### Confirmed as later material, not 1.1

| Topic | Sources | Where it belongs |
| --- | --- | --- |
| Agent components: policy/value/model, maze example | Silver pp. 25–33 | 1.2 |
| Agent taxonomy | Silver pp. 34–36 | later |
| Prediction vs control | Silver p. 43; CS234 p. 44 | Week 2 |
| Markov definition and history formalism | Silver pp. 18–21; CS234 pp. 35–36; CS224R pp. 34–36 | 1.2 |
| Mars-rover MRP | CS234 pp. 39–59 | 1.2 / Week 2 equivalent |
| Imitation learning | CS224R pp. 46–50 | Week 12 |

Silver's Atari learning-vs-planning pair (pp. 38–39) is the source of old MDP deck slides 12–13. It is available if the 1.1 contrast needs a picture, but the robot sentence above should suffice.

**Time:**
- Items 1 and 2 replace the optional montage and part of the opening (net about 0).
- Item 3 is backup only.
- Moving Q2 to backup frees about 3 minutes, which the formulation discussion keeps.

No scope, mastery, assessment or workload change.

## 4. Route to render-ready content

The instructor's proposed sequence:
1. lecturer comments;
2. ChatGPT drafts render-ready content, pausing on important decisions;
3. Claude reviews it, pausing likewise;
4. Claude renders;
5. ChatGPT reviews the PPTX;
6. lecturer edits;
7. Claude pulls the edits back;
8. done on the lecturer's thumbs up.

I agree with the sequence. Five adjustments would avoid duplicated state and rule conflicts:

1. **Make the render-ready file shared, not ChatGPT-owned.**
   - *Problem:* under AGENTS.md, Claude may not *adopt* a `_chatgpt` file as input. Rendering from ChatGPT's proposal is adoption.
   - *Fix:* ChatGPT writes it as a shared file, e.g. `course/lectures/week01/intro_mdps_content.md`, marked shared in its header. This is a one-line ownership exception the instructor would record.
   - Claude's review findings go in a separate file, or are applied as edits after they are agreed. Agreed edits by either AI are allowed because the file is shared.
2. **One maintained source after rendering.**
   - Once the PPTX exists, the instructor's PPTX is the authority, and Claude's deck YAML is kept in step with it (`pull_deck_claude.py`).
   - The shared content file is then frozen as the record of what was agreed. It should not be maintained in parallel; otherwise three copies drift.
   - "Push the changes back to the content files" then means the YAML, plus a regenerated read-only Markdown view for ChatGPT.
3. **Give ChatGPT a reviewable render.** At step 5, Claude exports slide previews (PDF/PNG) and a text view to `output/lectures/week01/`. ChatGPT reviews those, so it never needs to open or extract the Claude deck.
4. **Add a fix pass before the lecturer edits.** Between steps 5 and 6, Claude applies the review findings both AIs agree on, so the instructor does not see known defects. Disagreements go to the instructor as a short list.
5. **Define "important decision" for the pauses.** Pause only for:
   - changes to accepted scope, mastery or minutes;
   - running-example or cross-session choices;
   - notation not in the guide;
   - an AI disagreement about old-slide reuse;
   - a correctness doubt.

   Everything else proceeds and is listed for the instructor.

**At "done":** record the deck's fingerprint in the decision log, as was done for deck 0. Evaluate the pilot after 1.1: instructor time spent, and whether the step-3 review earned its cost.

**Timing caveat:** 1.1 is scheduled for this week. If delivery comes before the full chain finishes, a shortened chain is enough for 1.1 and the full chain can be judged from 1.2 onward. The shortened chain: ChatGPT writes render-ready content → Claude renders, noting any review findings → lecturer edits.

## 5. Recording the instructor's comments

The comments in section 2 are explicit instructor content decisions for 1.1, so they belong in `decisions/decision_log.md`. Both AIs received the same message, so to avoid two entries I have **not** logged them. I suggest the next author in the agreed flow (ChatGPT, at step 2) records them once, or the instructor names who should.
