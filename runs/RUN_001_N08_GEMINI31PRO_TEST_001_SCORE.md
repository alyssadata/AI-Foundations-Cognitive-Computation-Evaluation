# AI Foundations | TEST_001 — RUN_001 N08 Gemini 3.1 Pro Score Summary

## Run

ARCHIVE_RUN_ID: `RUN_001_N08_GEMINI31PRO`  
TEST RUN: `RUN_001`  
CONDITION: `N = 8`  
MODEL: Gemini 3.1 Pro (operator-identified; generated record reported model version as `UNKNOWN`)  
TRUE_HIDDEN_TARGET: C08  
MODEL_FINAL_ANSWER: C08  
INPUT_FILE: `TEST_001_INPUT_N08.csv`

## Deterministic Task Result

**TASK SCORE: SUCCESS**

The tested system correctly identified `C08` and uniquely resolved the candidate space.

| Measure | Result |
|---|---:|
| Correct final identification | YES |
| Unique resolution | YES |
| Successful identification | YES |
| Questions asked | 3 |
| Binary minimum for N=8 | 3 |
| Question overhead | 0 |
| Mean divider efficiency | 1.0 |
| Final candidates remaining | 1 |

## Step Score

| Step | Property | Answer | Candidates Before | Split | Candidates After | Best Available | Divider Efficiency |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | P04 | YES | 8 | 4 / 4 | 4 | 0.5 | 1.0 |
| 2 | P07 | YES | 4 | 2 / 2 | 2 | 0.5 | 1.0 |
| 3 | P10 | YES | 2 | 1 / 1 | 1 | 0.5 | 1.0 |

The decision path was:

```text
8 → 4 → 2 → 1
```

Every chosen property was a strongest available divider at that state. The target was identified in exactly `log2(8) = 3` binary questions with zero question overhead.

## Run-Integrity Deviation

The generated archival record reports:

```text
INTERRUPTION_OR_TOOL_FAILURE: YES
TRANSCRIPT_ACCESS: COMPLETE
```

This deviation is preserved rather than silently corrected. The recovered scored interaction itself is complete and contains no invalid question, inactive property, target leakage, invalid operator response, or missing scored turn.

Under TEST_001, `UNRESOLVED` applies when protocol failure, missing evidence, or another confound **prevents interpretation**. On the evidence currently preserved, the reported tool/interruption flag does **not** prevent deterministic scoring of the decision path: the full P-question sequence, answers, and final identification are available and internally consistent.

Accordingly, this file separates two judgments:

- **Deterministic task score:** SUCCESS
- **Run-integrity status:** DEVIATION RECORDED — reported interruption/tool failure, with complete scored transcript

If later evidence shows that the interruption/tool failure altered the candidate matrix, answers, question selection, or transcript completeness, this run should be reclassified for interpretability.

## Model Interaction Observation

Gemini 3.1 Pro emitted only the required P questions and final answer during the scored interaction. Unlike a narrated progress style, the scored transcript contains no unsolicited candidate-count summaries or intermediate task-state commentary.

This is a **non-scored interaction-style observation**, not a competence judgment. It may become useful only if the same pattern persists across additional Gemini runs.

## Evidence Files

- Generated run record and verbatim scored transcript: `runs/RUN_001_N08_GEMINI31PRO_TEST_001.md`
- Normalized scorer-ready trace: `runs/RUN_001_N08_GEMINI31PRO_TEST_001_TRACE.csv`
- Deterministic step scores: `runs/RUN_001_N08_GEMINI31PRO_TEST_001_TRACE_SCORED_STEPS.csv`
- Deterministic run summary: `runs/RUN_001_N08_GEMINI31PRO_TEST_001_TRACE_SUMMARY.csv`

## Evaluation Boundary

This is one Gemini 3.1 Pro observation under TEST_001 at `N=8`. It does not by itself establish scaling at larger N conditions or support *Nature of Cognitive Computation* as a whole.
