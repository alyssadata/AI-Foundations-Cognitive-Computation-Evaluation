# AI Foundations | TEST_001 — RUN_001 / N08 Summary

## Condition Identity

TEST: `TEST_001`  
RUN: `RUN_001`  
CONDITION: `N = 8`  
ACTIVE PROPERTIES: 6  
BINARY MINIMUM: 3 questions  
MODELS COMPLETED: 4

Models:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

This is a **condition-level summary only**. It does not determine the final TEST_001 outcome, which requires RUN_002 / N16, RUN_003 / N32, and RUN_004 / N64.

---

## Cross-Model Results

| Model | Hidden Target | Final Answer | Questions | Minimum | Overhead | Mean Divider Efficiency | Result |
|---|---|---|---:|---:|---:|---:|---|
| GPT-5.6 Sol | C06 | C06 | 3 | 3 | 0 | 1.0 | SUCCESS |
| Claude Opus 5 | C02 | C02 | 3 | 3 | 0 | 1.0 | SUCCESS |
| Gemini 3.1 Pro | C08 | C08 | 3 | 3 | 0 | 1.0 | SUCCESS |
| Grok 4.5 | C01 | C01 | 3 | 3 | 0 | 1.0 | SUCCESS |

### Aggregate RUN_001 / N08 Result

```text
Correct final identifications: 4 / 4
Unique resolutions: 4 / 4
Successful model-runs: 4 / 4
Total scored questions: 12
Mean questions per model: 3.0
Binary minimum: 3
Mean question overhead: 0.0
Mean divider efficiency across model-runs: 1.0
```

Every tested model reached its hidden target in the information-theoretic minimum number of binary questions.

Every scored property choice matched a strongest available divider at the state where it was selected.

All four model-runs therefore followed the same candidate-count reduction pattern:

```text
8 → 4 → 2 → 1
```

---

## Property Selection Paths

| Model | Step 1 | Step 2 | Step 3 |
|---|---|---|---|
| GPT-5.6 Sol | P04 | P10 | P07 |
| Claude Opus 5 | P04 | P07 | P10 |
| Gemini 3.1 Pro | P04 | P07 | P10 |
| Grok 4.5 | P04 | P01 | P03 |

All four models independently selected `P04` as the first distinction. At the full N08 state, `P04` produces a 4 / 4 partition and is therefore a maximally discriminating first question.

The later paths were not identical across all models. GPT-5.6 Sol, Claude Opus 5, Gemini 3.1 Pro, and Grok 4.5 reached the same ideal reduction pattern through more than one valid property sequence.

This matters because RUN_001 is observing adaptive property selection rather than requiring one fixed question order.

---

## Run Integrity

Three runs had no reported scored-run interruption or tool failure:

- GPT-5.6 Sol
- Claude Opus 5
- Grok 4.5

Gemini 3.1 Pro reported `INTERRUPTION_OR_TOOL_FAILURE: YES`. Post-run clarification established that the flag referred to a recoverable Python `NameError` after the third operator answer: the model omitted `import pandas as pd`, corrected the import in the next tool call, and then completed the identification.

The Gemini scored transcript remained complete. The clarification did not alter the recorded P-question sequence, operator answers, or final answer. The deterministic task result therefore remains `SUCCESS`, with the recoverable tool error preserved as a run-integrity deviation.

---

## Non-Scored Interaction Observations

These observations are descriptive only and are **not part of TEST_001 competence scoring**.

Claude Opus 5 spontaneously narrated intermediate task state between scored questions, including candidate-count progress and a final uniqueness statement. The narration did not affect correctness, but it added output beyond the task-required question sequence. That additional output carries a token-efficiency cost relative to a minimal interaction path; no token, latency, or monetary magnitude was measured in RUN_001.

GPT-5.6 Sol, Gemini 3.1 Pro, and Grok 4.5 used a comparatively minimal scored interaction: required P questions followed by the final answer, without unsolicited candidate-count narration.

These are single-condition observations and should not be generalized as stable model characteristics unless the same patterns persist across later runs.

---

## RUN_001 Interpretation

At `N = 8`, all four tested models successfully selected successive distinctions that preserved maximum available elimination and correctly identified their hidden targets.

RUN_001 therefore provides a clean positive observation at the smallest TEST_001 candidate-space condition.

It does **not** yet establish the scaling claim being evaluated. The critical next question is whether the same strong-elimination behavior persists as the candidate space doubles through:

```text
RUN_002 → N = 16
RUN_003 → N = 32
RUN_004 → N = 64
```

No final `SUPPORTED`, `MIXED`, `WEAKENED`, or `UNRESOLVED` TEST_001 outcome is assigned at this stage.

---

## Evidence

### GPT-5.6 Sol

- `runs/RUN_001_N08_GPT56SOL_TEST_001.md`
- `runs/RUN_001_N08_GPT56SOL_TEST_001_SCORE.md`

### Claude Opus 5

- `runs/RUN_001_N08_CLAUDEOPUS5_TEST_001.md`
- `runs/RUN_001_N08_CLAUDEOPUS5_TEST_001_SCORE.md`

### Gemini 3.1 Pro

- `runs/RUN_001_N08_GEMINI31PRO_TEST_001.md`
- `runs/RUN_001_N08_GEMINI31PRO_TEST_001_SCORE.md`

### Grok 4.5

- `runs/RUN_001_N08_GROK45_TEST_001.md`
- `runs/RUN_001_N08_GROK45_TEST_001_SCORE.md`

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
