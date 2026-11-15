# A1 LLM-use report

Name and student number:

Fill in ONE of the two sections. This report is required. A submission whose
solution was delegated to an LLM in one or a few prompts earns no credit
(syllabus).

## A. I did not use an LLM for this assignment

Write "I did not use an LLM for this assignment." and nothing else. Do not invent
interactions.

## B. I used an LLM

For each part where you used one, give:

1. **Where:** which function or question.
2. **What you asked and what you got:** a representative prompt and an excerpt of
   the output. Do not paste whole conversations.
3. **What you did with it:** what you accepted, rejected or changed, and why.
4. **How you checked it:** at least one concrete check, if the LLM contributed code
   or an explanation you relied on (a test you ran, a number you compared by hand).

Then, in two or three sentences and in your own words, explain the update in your
`train` loop for SARSA.

---

## Example of a filled entry (delete before submitting)

**Where:** `td0_update` in `prediction.py`.

**What I asked and what I got:** I asked: "My TD(0) values for the terminal
transition are too large. Here is my function: [function]. What is wrong?" The
answer said, in part: "You add gamma * V[s_next] even when the transition
terminates. The value after termination is zero, so the target should be the
reward alone."

**What I did with it:** I accepted the diagnosis and added the `terminated`
check myself. The answer also suggested setting `V[s_next] = 0` inside the
function; I rejected that, because the function should not change other entries.

**How I checked it:** `pytest tests/test_part2_prediction.py -k td0` passed
afterwards, and I recomputed the `terminated-nonzero-successor` case by hand:
target = 1.0, so the new value is V[s] + alpha * (1.0 - V[s]).
