# AI Foundations | TEST_001 — RUN_003 / N32 Summary

## Condition Identity

TEST: `TEST_001`  
RUN: `RUN_003`  
CONDITION: `N = 32`  
ACTIVE PROPERTIES: 10  
BINARY MINIMUM: 5 questions  
MODELS COMPLETED: 4

Models:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

This is a **condition-level summary only**. It does not determine the final TEST_001 outcome, which still requires RUN_004 / N64.

---

## Cross-Model Results

| Model | Hidden Target | Final Answer | Questions | Minimum | Overhead | Mean Divider Efficiency | Result |
|---|---|---|---:|---:|---:|---:|---|
| GPT-5.6 Sol | C20 | C20 | 5 | 5 | 0 | 1.0 | SUCCESS |
| Claude Opus 5 | C09 | C09 | 5 | 5 | 0 | 1.0 | SUCCESS |
| Gemini 3.1 Pro | C25 | C25 | 5 | 5 | 0 | 1.0 | SUCCESS |
| Grok 4.5 | C31 | C31 | 5 | 5 | 0 | 0.9375 | SUCCESS |

### Aggregate RUN_003 / N32 Result

```text
Correct final identifications: 4 / 4
Unique resolutions: 4 / 4
Successful model-runs: 4 / 4
Total scored questions: 20
Mean questions per model: 5.0
Binary minimum: 5
Mean question overhead: 0.0
Mean divider efficiency across model-runs: 0.984375
```

Every tested model reached its hidden target in the information-theoretic minimum number of binary questions.

Three model-runs selected a strongest available divider at every scored step. Grok 4.5 did not: its first distinction, `P01`, split the full N32 candidate space `11 / 21` even though `16 / 16` dividers were available. Its subsequent four choices were strongest available for the realized remaining states.

Accordingly, RUN_003 is the first TEST_001 condition in which successful minimum-question identification and perfect divider selection come apart.

---

## Property Selection Paths

| Model | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|---|---|---|---|---|---|
| GPT-5.6 Sol | P02 | P04 | P07 | P06 | P10 |
| Claude Opus 5 | P09 | P02 | P07 | P10 | P04 |
| Gemini 3.1 Pro | P02 | P04 | P07 | P03 | P01 |
| Grok 4.5 | P01 | P02 | P04 | P03 | P08 |

GPT-5.6 Sol and Gemini 3.1 Pro opened with `P02`, while Claude Opus 5 opened with `P09`. Both `P02` and `P09` divide the full N32 candidate set `16 / 16` and are maximally discriminating first questions.

Grok 4.5 opened with `P01`, which divides the full candidate set `11 / 21`. The realized `YES` branch left 11 candidates, after which Grok adapted successfully through strongest available dividers and still resolved the target in five total questions.

The candidate-count paths were:

```text
GPT-5.6 Sol:   32 → 16 → 8 → 4 → 2 → 1
Claude Opus 5: 32 → 16 → 8 → 4 → 2 → 1
Gemini 3.1 Pro:32 → 16 → 8 → 4 → 2 → 1
Grok 4.5:      32 → 11 → 6 → 3 → 2 → 1
```

This distinction matters: a realized path can still achieve the binary minimum even when an earlier property choice was not globally strongest, provided the actual branch and later adaptive choices permit recovery.

---

## Protocol-Threshold Check at N32

The frozen TEST_001 protocol defines final `SUPPORTED` as requiring every formal model-condition run to identify its target correctly, mean divider efficiency of at least `0.90`, and mean question overhead no more than `+1` at each tested `N`.

For the completed N32 condition:

```text
Correct identifications: 4 / 4
Mean divider efficiency: 0.984375
Mean question overhead: 0.0
```

So **RUN_003 / N32 meets the protocol's numerical support thresholds for this condition**.

This is not a final `SUPPORTED` outcome. RUN_004 / N64 remains required before TEST_001 can receive its final outcome classification.

---

## Run Integrity

### GPT-5.6 Sol

The scored transcript was complete and no target leakage, invalid or compound question, inactive property use, interruption, or tool failure was reported.

### Claude Opus 5

The scored path was complete and valid. Reading the supplied candidate/property matrix before Question 1 is part of the task and is not a deviation.

Claude again included extra lead-in and candidate-count narration despite the instruction to begin with the first P question only. This is preserved as an **output-format / interaction deviation**. It did not alter the scored property sequence or task result.

### Gemini 3.1 Pro

The deterministic task path was complete and successful. The generated record marked `INTERRUPTION_OR_TOOL_FAILURE: YES`.

Post-run clarification established that this referred to a recoverable Python `NameError`: the model used the pandas alias `pd` without first including `import pandas as pd` in one code block, then corrected the import in the next tool call and continued successfully.

The original deviation flag remains preserved; the clarification explains it without rewriting the scored transcript or result.

### Grok 4.5

The scored transcript was complete and no target leakage, invalid or compound question, inactive property use, interruption, or tool failure was reported.

---

## Non-Scored Interaction Observations

These observations are descriptive only and are **not part of TEST_001 competence scoring**.

Claude Opus 5 has now shown unsolicited task-state narration across N08, N16, and N32. The repetition makes this a stronger recurring interaction-style observation for the tested configuration, while remaining separate from competence.

Gemini 3.1 Pro and Grok 4.5 again used minimal scored interactions without unsolicited candidate-count narration. GPT-5.6 Sol also used a minimal scored interaction in N32.

---

## Cross-Condition Observation So Far

RUN_001 / N08, RUN_002 / N16, and RUN_003 / N32 are now complete across the same four models.

Across the first three candidate-space conditions:

```text
Completed model-condition runs: 12 / 12
Correct final identifications: 12 / 12
Unique resolutions: 12 / 12
Total scored questions: 48
Total question overhead above binary minimum: 0

Mean divider efficiency by condition:
N08: 1.0
N16: 1.0
N32: 0.984375
```

The scaling ladder observed so far is:

```text
N = 8  → minimum 3 questions
N = 16 → minimum 4 questions
N = 32 → minimum 5 questions
```

All twelve completed model-condition runs have reached the correct target in the binary minimum number of questions. The first departure from perfect divider selection appears at N32 in Grok 4.5, while the N32 condition mean remains above the protocol's `0.90` threshold.

The final formal condition is:

```text
RUN_004 → N = 64 → binary minimum 6 questions
```

No final `SUPPORTED`, `MIXED`, `WEAKENED`, or `UNRESOLVED` TEST_001 outcome is assigned until RUN_004 / N64 is complete.

---

## Evidence

### GPT-5.6 Sol

- `runs/RUN_003_N32_GPT56SOL_TEST_001.md`
- `runs/RUN_003_N32_GPT56SOL_TEST_001_SCORE.md`

### Claude Opus 5

- `runs/RUN_003_N32_CLAUDEOPUS5_TEST_001.md`
- `runs/RUN_003_N32_CLAUDEOPUS5_TEST_001_SCORE.md`

### Gemini 3.1 Pro

- `runs/RUN_003_N32_GEMINI31PRO_TEST_001.md`
- `runs/RUN_003_N32_GEMINI31PRO_TEST_001_SCORE.md`

### Grok 4.5

- `runs/RUN_003_N32_GROK45_TEST_001.md`
- `runs/RUN_003_N32_GROK45_TEST_001_SCORE.md`

### Prior condition summaries

- `results/RUN_001_N08_SUMMARY.md`
- `results/RUN_002_N16_SUMMARY.md`

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
