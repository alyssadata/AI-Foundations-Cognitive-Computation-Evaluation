# AI Foundations | TEST_001 — RUN_003 N32 GPT-5.6 Sol Score Summary

## Run

ARCHIVE_RUN_ID: `RUN_003_N32_GPT56SOL`  
TEST RUN: `RUN_003`  
CONDITION: `N = 32`  
MODEL: GPT-5.6 Sol  
TRUE_HIDDEN_TARGET: C20  
MODEL_FINAL_ANSWER: C20  
INPUT_FILE: `TEST_001_INPUT_N32.csv`

## Result

**RUN_003 / N32 / GPT-5.6 Sol: SUCCESS**

The tested system correctly identified `C20` and uniquely resolved the candidate space.

This is a **model-run result only**. It does not determine the RUN_003 / N32 cross-model condition result or the final TEST_001 outcome.

## Deterministic Score

| Measure | Result |
|---|---:|
| Correct final identification | YES |
| Unique resolution | YES |
| Successful identification | YES |
| Questions asked | 5 |
| Binary minimum for N=32 | 5 |
| Question overhead | 0 |
| Mean divider efficiency | 1.0 |
| Final candidates remaining | 1 |

## Step Score

| Step | Property | Answer | Candidates Before | Split | Candidates After | Best Available | Divider Efficiency |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | P02 | NO | 32 | 16 / 16 | 16 | 0.5 | 1.0 |
| 2 | P04 | YES | 16 | 8 / 8 | 8 | 0.5 | 1.0 |
| 3 | P07 | NO | 8 | 4 / 4 | 4 | 0.5 | 1.0 |
| 4 | P06 | NO | 4 | 2 / 2 | 2 | 0.5 | 1.0 |
| 5 | P10 | YES | 2 | 1 / 1 | 1 | 0.5 | 1.0 |

## Interpretation

GPT-5.6 Sol selected a maximally discriminating active property at every scored step:

```text
32 → 16 → 8 → 4 → 2 → 1
```

`P02` divided the full N32 candidate space 16/16. After the actual `NO` answer, `P04` divided the 16 remaining candidates 8/8. After `YES`, `P07` divided the eight remaining candidates 4/4. After `NO`, `P06` divided the four remaining candidates 2/2. Finally, after `NO`, `P10` divided the last two candidates 1/1.

The target was therefore identified in exactly `log2(32) = 5` binary questions, with zero question overhead and divider efficiency `1.0` at every step.

The relevant behavior is not merely that `C20` was correct. The system autonomously selected successive distinctions that preserved the maximum guaranteed elimination available throughout the run.

## Transcript Notes

The operator responses were lowercase `yes` / `no`; these are valid binary responses and introduce no scoring ambiguity.

The model asked exactly one active P question per scored turn. No target leakage, compound query, inactive property use, interruption, tool failure, or other deviation was reported. Transcript access was complete.

## Cross-Condition Note

For GPT-5.6 Sol, the completed TEST_001 conditions now show:

```text
N = 8  → 3 questions → overhead 0 → mean divider efficiency 1.0
N = 16 → 4 questions → overhead 0 → mean divider efficiency 1.0
N = 32 → 5 questions → overhead 0 → mean divider efficiency 1.0
```

This is positive within-model scaling evidence across the first three conditions, but `N = 64` remains untested and no final TEST_001 outcome is assigned from this run alone.

## Evidence Files

- Full generated run record and verbatim scored transcript: `runs/RUN_003_N32_GPT56SOL_TEST_001.md`
- Normalized scorer-ready trace: `runs/RUN_003_N32_GPT56SOL_TEST_001_TRACE.csv`
- Deterministic step scores: `runs/RUN_003_N32_GPT56SOL_TEST_001_TRACE_SCORED_STEPS.csv`
- Deterministic run summary: `runs/RUN_003_N32_GPT56SOL_TEST_001_TRACE_SUMMARY.csv`

## Evaluation Boundary

This run provides one GPT-5.6 Sol observation under TEST_001 at `N=32`. It does not by itself establish the RUN_003 cross-model result, scaling through N64, or support *Nature of Cognitive Computation* as a whole.
