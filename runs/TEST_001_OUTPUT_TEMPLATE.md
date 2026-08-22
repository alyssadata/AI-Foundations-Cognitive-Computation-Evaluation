# AI Foundations | TEST_001 — Run Output Sheet

Make one copy of this file for each formal run.

Example filename:

```text
RUN_001_TEST_001.md
```

Do not score the run while it is happening. This sheet is filled **after the tested AI gives its final answer**.

---

## 1. Run Information

```text
RUN_ID:
DATE:
N: 8 / 16 / 32 / 64
HIDDEN_TARGET:
MODEL / VERSION:
INTERFACE:
FRESH CONTEXT USED: YES / NO
OPERATOR: Alyssa Solen
```

Use `UNKNOWN` if a field is unavailable.

---

## 2. Exact Start Prompt

Paste the exact PASTE 1 prompt you sent, with the actual N filled in.

```text
[PASTE EXACT START PROMPT HERE]
```

---

## 3. Full Scored Interaction

Paste everything from the AI's first property question through its final answer.

Do not summarize or clean it up.

```text
[PASTE FULL SCORED INTERACTION HERE]
```

The scored interaction ends at:

```text
FINAL ANSWER: Cxx
```

---

## 4. Result

```text
TRUE HIDDEN TARGET:
MODEL FINAL ANSWER:
CORRECT: YES / NO
```

Do not correct the AI before recording its answer.

---

## 5. Simple Question Trace

After the run is over, use PASTE 2 from `protocol/TEST_001_EASY_RUN_SHEET.md` and paste the returned trace here.

```text
step,property,answer
[PASTE TRACE HERE]
```

If the tested AI cannot recover the trace exactly, write:

```text
TRANSCRIPT ACCESS INCOMPLETE
```

The full scored interaction above remains the primary evidence.

---

## 6. Deviations

```text
TARGET LEAKED BEFORE FINAL ANSWER: YES / NO
NON-YES/NO OPERATOR RESPONSE: YES / NO
INVALID / COMPOUND MODEL QUESTION: YES / NO
INTERRUPTION OR TOOL FAILURE: YES / NO
OTHER DEVIATION:
```

If none:

```text
OTHER DEVIATION: NONE
```

---

## 7. Scoring — Fill Afterward

Do not calculate this during the run.

After the simple trace has been converted into the scorer input and `protocol/score_test_001.py` has been run, copy the generated summary here.

```text
SUCCESS:
QUESTIONS:
BINARY LOWER BOUND:
QUESTION OVERHEAD:
MEAN DIVIDER EFFICIENCY:
FINAL REMAINING CANDIDATE(S):
```

If scoring has not been run yet:

```text
SCORING STATUS: PENDING
```

---

## 8. Run Statement — Fill After Scoring

```text
In this run, the tested system [correctly / incorrectly] identified [HIDDEN TARGET] from an answer space of N = [N] using [QUESTIONS] successive property questions. Mean divider efficiency was [VALUE], with question overhead of [VALUE] above the binary lower bound.
```

This is a factual statement about this run only. It is not the overall TEST_001 result.

---

## 9. External-Source Boundary

This run contributes evidence toward TEST_001 for EXT-CLM-004.

It does not establish that all cognition is logarithmic, that every recognition problem has a clean answer space, or that *Nature of Cognitive Computation* is supported as a whole.

**AI Foundations conducted the evaluation. AI Foundations did not author the evaluated external source.**

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
