# AI Foundations | TEST_001 — Easy Run Sheet

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source version / identifier:** PhilArchive Version 1 / NAUNOC-2 / 2025-09-10  
**Claim / test ID:** EXT-CLM-004 / TEST_001  
**Protocol:** `protocol/TEST_001.md` v2.0.0  
**Run-sheet version:** 1.0.0

---

## What This Sheet Is

This is the operator-facing execution sheet for **TEST_001 — Bounded Identification by Successive Distinctions**.

Formal test question:

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

Use this sheet to run the test without having to reinterpret the formal protocol during execution.

---

# BEFORE YOU START

## 1. Choose one candidate-space size

Run one of the four formal conditions:

```text
N = 8   -> active candidates C01–C08
N = 16  -> active candidates C01–C16
N = 32  -> active candidates C01–C32
N = 64  -> active candidates C01–C64
```

Minimum formal run set: **4 independently selected hidden targets at each N = 16 total runs.**

## 2. Open a fresh model context

Use a fresh chat / model context for every formal run.

Record the model name/version and interface if visible. Do not guess unavailable metadata.

## 3. Attach the candidate file

Attach:

`protocol/TEST_001_CANDIDATES.csv`

The tested system may inspect the entire matrix, but only the first `N` rows are active for the selected condition.

## 4. Privately choose the hidden target

Choose exactly one candidate from the active set.

Example for `N = 16`: choose one of `C01` through `C16`.

**Do not tell the model which candidate you selected.**

Keep the candidate file open separately so you can answer each property question from the hidden target's row.

## 5. Start a run record

Copy `runs/TEST_001_OUTPUT_TEMPLATE.md` and rename the copy for the run, for example:

`RUN_001_TEST_001.md`

Also copy `protocol/TEST_001_RUN_TRACE_TEMPLATE.csv` for the raw question/answer trace.

---

# RUN

## PASTE 1 — Start the test

Replace `[N]` with the active candidate-space size before sending.

```text
You are participating in TEST_001.

The attached file contains the candidate matrix. For this run, the active answer space is the first [N] candidates only: C01 through C[N]. Exactly one active candidate has been privately selected as the hidden target.

Your task is to identify the hidden target by selecting successive distinctions.

Rules:
1. Ask only one YES/NO question at a time.
2. Each question must ask about exactly one listed property P01–P10.
3. You choose which property to ask about next. No decision tree or property order will be supplied.
4. Do not ask directly for the candidate name or label.
5. Do not ask the operator to describe or reveal the target.
6. Do not use compound questions.
7. After each YES/NO answer, continue until you are ready to identify one candidate.
8. When you are ready, state exactly: FINAL ANSWER: Cxx

Begin with your first property question only.
```

Do not add explanation before or after this paste.

---

## FOR EACH MODEL QUESTION

The model should ask one property question such as:

```text
Is P04 YES for the hidden target?
```

Look at the hidden target row in `TEST_001_CANDIDATES.csv` and reply with **only**:

```text
YES
```

or

```text
NO
```

At the same time, add one row to the raw trace file:

```text
candidate_space_n,target,step,property,answer
```

Example:

```text
16,C11,1,P04,NO
```

Do **not** tell the tested model the target while the run is active.

Continue answering only `YES` or `NO` until the model gives a final answer.

---

## WHEN THE MODEL GIVES ITS FINAL ANSWER

Immediately record the exact final answer in the run output sheet.

Do not correct the model before recording it.

Then reveal the true hidden target only in the run record, not as part of the scored interaction.

The scored interaction ends at:

```text
FINAL ANSWER: Cxx
```

---

# AFTER THE SCORED INTERACTION

## PASTE 2 — Optional transcript extraction

Use this only **after** the model has already given its final answer. It is not part of the scored interaction.

```text
The scored interaction is complete.

Return a chronological trace of only the property questions you asked during the scored interaction and the YES/NO answers I gave.

Use exactly this CSV header:
step,property,answer

Do not add, remove, repair, reinterpret, or reorder any question or answer. If you cannot recover the complete scored interaction exactly, write:
TRANSCRIPT ACCESS INCOMPLETE
```

Treat the original visible chat as primary evidence. Do not replace it with a reconstructed trace if the extraction is incomplete or conflicts with the visible transcript.

---

# SCORE THE RUN

Save the raw trace as a CSV using the five required columns:

```text
candidate_space_n,target,step,property,answer
```

Then run:

```text
python protocol/score_test_001.py protocol/TEST_001_CANDIDATES.csv runs/RUN_XXX_TEST_001_TRACE.csv
```

The scorer creates:

```text
RUN_XXX_TEST_001_TRACE_SCORED_STEPS.csv
RUN_XXX_TEST_001_TRACE_SUMMARY.csv
```

Copy the summary values into `runs/TEST_001_OUTPUT_TEMPLATE.md` for the completed run.

---

# WHAT TO SAVE FOR EACH RUN

Save:

```text
RUN_XXX_TEST_001.md
RUN_XXX_TEST_001_TRACE.csv
RUN_XXX_TEST_001_TRACE_SCORED_STEPS.csv
RUN_XXX_TEST_001_TRACE_SUMMARY.csv
```

Also preserve the original chat/interface transcript or export when available.

---

# EASY FINAL RULE

**The model must choose its own successive property distinctions, correctly identify the hidden target, and have those choices scored against the best divider actually available at each state.**

The result evaluates the external claim dependency. It does not make the external claim part of AI Foundations.

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
