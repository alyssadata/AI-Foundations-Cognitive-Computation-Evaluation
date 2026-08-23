# AI Foundations | TEST_001 — RUN_003 N32 Grok 4.5 Score Summary

## Run

ARCHIVE_RUN_ID: `RUN_003_N32_GROK45`  
TEST RUN: `RUN_003`  
CONDITION: `N = 32`  
MODEL: Grok 4.5  
TRUE_HIDDEN_TARGET: C31  
MODEL_FINAL_ANSWER: C31  
INPUT_FILE: `TEST_001_INPUT_N32.csv`

## Result

**RUN_003 / N32 / Grok 4.5: SUCCESS**

The tested system correctly identified `C31` and uniquely resolved the candidate space.

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
| Mean divider efficiency | 0.9375 |
| Final candidates remaining | 1 |

## Step Score

| Step | Property | Answer | Candidates Before | Split | Candidates After | Best Available | Divider Efficiency |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | P01 | YES | 32 | 11 / 21 | 11 | 0.5 | 0.6875 |
| 2 | P02 | YES | 11 | 6 / 5 | 6 | 0.4545 | 1.0 |
| 3 | P04 | NO | 6 | 3 / 3 | 3 | 0.5 | 1.0 |
| 4 | P03 | NO | 3 | 1 / 2 | 2 | 0.3333 | 1.0 |
| 5 | P08 | NO | 2 | 1 / 1 | 1 | 0.5 | 1.0 |

## Interpretation

Grok 4.5 correctly identified the hidden target in exactly `log2(32) = 5` binary questions, with zero question overhead.

The candidate-count path was:

```text
32 → 11 → 6 → 3 → 2 → 1
```

This differs from the ideal-halving path seen in the other completed N32 runs.

The first selected distinction, `P01`, split the full candidate set `11 / 21`. Stronger `16 / 16` dividers were available at that state, so the first choice did **not** preserve maximum guaranteed elimination. Its divider-efficiency ratio was `0.6875`.

After that first choice, every subsequent selected property matched a strongest available divider for the actual remaining candidate set. The run-level mean divider efficiency was therefore:

```text
(0.6875 + 1 + 1 + 1 + 1) / 5 = 0.9375
```

The favorable `YES` branch on P01 left 11 candidates, and the subsequent adaptive choices still resolved `C31` within five total questions. Thus this run is a successful identification with zero question overhead, but it is **not a perfect-divider run**.

This distinction is important: correct minimum-length identification on the realized target path does not imply that every distinction selected was globally strongest at the state where it was chosen.

## Transcript Notes

The operator responses were lowercase `yes` / `no`; these are valid binary responses and introduce no scoring ambiguity.

The model asked exactly one active P question per scored turn. No target leakage, compound query, inactive property use, interruption, tool failure, or other deviation was reported. Transcript access was complete.

## Non-Scored Model Observation

Grok 4.5 again used a minimal scored interaction: required P questions followed by the final answer, with no unsolicited candidate-count narration or intermediate task-state commentary.

The same interaction style was observed in its N08 and N16 runs. This remains descriptive only and is not part of TEST_001 competence scoring.

## Cross-Condition Note

For Grok 4.5, the completed TEST_001 conditions now show:

```text
N = 8  → 3 questions → overhead 0 → mean divider efficiency 1.0
N = 16 → 4 questions → overhead 0 → mean divider efficiency 1.0
N = 32 → 5 questions → overhead 0 → mean divider efficiency 0.9375
```

The N32 run therefore preserves successful minimum-question identification while introducing the first observed reduction in Grok's divider-efficiency score. N64 remains untested.

## Evidence Files

- Full generated run record and verbatim scored transcript: `runs/RUN_003_N32_GROK45_TEST_001.md`
- Normalized scorer-ready trace: `runs/RUN_003_N32_GROK45_TEST_001_TRACE.csv`
- Deterministic step scores: `runs/RUN_003_N32_GROK45_TEST_001_TRACE_SCORED_STEPS.csv`
- Deterministic run summary: `runs/RUN_003_N32_GROK45_TEST_001_TRACE_SUMMARY.csv`

## Evaluation Boundary

This run provides one Grok 4.5 observation under TEST_001 at `N=32`. It does not by itself establish the RUN_003 cross-model result, scaling through N64, or support *Nature of Cognitive Computation* as a whole.
