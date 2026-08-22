# AI Foundations | TEST_001 — Run Output Sheet

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source version / identifier:** PhilArchive Version 1 / NAUNOC-2 / 2025-09-10  
**Claim / test ID:** EXT-CLM-004 / TEST_001  
**Protocol:** `protocol/TEST_001.md` v2.0.0  
**Output-sheet version:** 1.0.0

---

## Use

Make one copy of this file for each formal run and rename it, for example:

`RUN_001_TEST_001.md`

This sheet records one run. It does **not** assign the final `SUPPORTED / MIXED / WEAKENED / UNRESOLVED` evaluation disposition by itself. That disposition is assigned only after the full protocol-defined run set is complete.

---

## 1. Run Identity

```text
RUN_ID:
DATE_TIME:
CANDIDATE_SPACE_N: 8 / 16 / 32 / 64
HIDDEN_TARGET:
MODEL / SYSTEM / SOFTWARE VERSION:
INTERFACE / PRODUCT / ENVIRONMENT:
MEMORY OR PRIOR HISTORY: fresh context / other
TOOLS / FILE ACCESS:
SAMPLING SETTINGS IF AVAILABLE:
OPERATOR: Alyssa Solen
```

Use `UNKNOWN` for unavailable metadata.

---

## 2. Exact Start Prompt

Paste the exact `PASTE 1` text used from `protocol/TEST_001_EASY_RUN_SHEET.md`, including the actual candidate-space size substituted for `[N]`.

```text
[PASTE EXACT START PROMPT HERE]
```

---

## 3. Raw Scored Interaction

Preserve the complete interaction from the first model property question through the model's final answer.

Do not summarize or repair it.

```text
[PASTE VERBATIM SCORED INTERACTION HERE]
```

If the complete transcript cannot be recovered exactly, write:

```text
TRANSCRIPT ACCESS INCOMPLETE
```

and preserve the original interface record separately.

---

## 4. Final Identification

```text
TRUE HIDDEN TARGET:
MODEL FINAL ANSWER:
CORRECT IDENTIFICATION: YES / NO
TOTAL VALID PROPERTY QUESTIONS:
INVALID / UNSCORABLE QUESTIONS:
```

Record the model's answer exactly as given before any correction or discussion.

---

## 5. Raw Trace File

**Trace file:** `RUN_XXX_TEST_001_TRACE.csv`

Required columns:

```text
candidate_space_n,target,step,property,answer
```

Record the path or link:

```text
RAW TRACE:
```

---

## 6. Deterministic Scoring Output

Run:

```text
python protocol/score_test_001.py protocol/TEST_001_CANDIDATES.csv runs/RUN_XXX_TEST_001_TRACE.csv
```

Record the generated evidence files:

```text
SCORED STEPS FILE:
SUMMARY FILE:
```

Copy the exact summary values below:

```text
CANDIDATE_SPACE_N:
TARGET:
SUCCESS: YES / NO
QUESTIONS:
INFORMATION_THEORETIC_MINIMUM:
QUESTION_OVERHEAD:
MEAN_DIVIDER_EFFICIENCY_RATIO:
FINAL_REMAINING:
```

Do not calculate these values by hand when the scorer output is available.

---

## 7. Step-Level Divider Evidence

The scored-steps CSV is authoritative for step-level measures.

For each valid question it records:

```text
candidates_before
yes_branch
no_branch
worst_case_guaranteed_elimination
best_available_guaranteed_elimination
divider_efficiency_ratio
candidates_after_actual_answer
```

Do not replace the CSV with a prose summary.

---

## 8. Deviations / Missing Data

```text
PROTOCOL DEVIATION: YES / NO
DESCRIPTION:
TARGET LEAKAGE: YES / NO
INVALID OPERATOR ANSWER: YES / NO
INTERRUPTION / TOOL FAILURE:
MISSING DATA:
TRANSCRIPT COMPLETE: YES / NO
OTHER NOTES:
```

A deviation stays visible. Do not silently repair the run.

---

## 9. Evidence Checklist

```text
[ ] Fresh model context used or deviation recorded
[ ] Correct N condition recorded
[ ] Hidden target recorded after scored interaction
[ ] Exact start prompt preserved
[ ] Verbatim scored interaction preserved
[ ] Model final answer preserved before correction
[ ] Raw trace CSV preserved
[ ] Deterministic scorer executed
[ ] Scored-steps CSV preserved
[ ] Summary CSV preserved
[ ] Deviations / missing data recorded
```

---

## 10. Run-Level Statement

Complete only the factual run statement below:

```text
In this run, the tested system [correctly / incorrectly] identified the hidden target using [X] valid successive property distinctions. The information-theoretic binary lower bound for N = [N] was [Y] questions, producing question overhead of [Z]. Mean divider efficiency was [RATIO].
```

Do **not** convert one run into the overall evaluation outcome.

---

## 11. Claim Boundary

This run contributes evidence toward TEST_001:

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

A single run does not establish that every recognition problem has a clean answer space, that all cognition is `O(log N)`, that biological cognition uses this mechanism, or that *Nature of Cognitive Computation* is supported as a whole.

---

## 12. External-Source Boundary

**AI Foundations conducted this evaluation. AI Foundations did not author the evaluated external source.**

The external source remains external to AI Foundations. Evaluation does not incorporate the source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
