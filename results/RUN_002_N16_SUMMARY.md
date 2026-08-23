# AI Foundations | TEST_001 — RUN_002 / N16 Summary

## Condition Identity

TEST: `TEST_001`  
RUN: `RUN_002`  
CONDITION: `N = 16`  
ACTIVE PROPERTIES: 8  
BINARY MINIMUM: 4 questions  
MODELS COMPLETED: 4

Models:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

This is a **condition-level summary only**. It does not determine the final TEST_001 outcome, which still requires RUN_003 / N32 and RUN_004 / N64.

---

## Cross-Model Results

| Model | Hidden Target | Final Answer | Questions | Minimum | Overhead | Mean Divider Efficiency | Result |
|---|---|---|---:|---:|---:|---:|---|
| GPT-5.6 Sol | C03 | C03 | 4 | 4 | 0 | 1.0 | SUCCESS |
| Claude Opus 5 | C11 | C11 | 4 | 4 | 0 | 1.0 | SUCCESS |
| Gemini 3.1 Pro | C07 | C07 | 4 | 4 | 0 | 1.0 | SUCCESS |
| Grok 4.5 | C15 | C15 | 4 | 4 | 0 | 1.0 | SUCCESS |

### Aggregate RUN_002 / N16 Result

```text
Correct final identifications: 4 / 4
Unique resolutions: 4 / 4
Successful model-runs: 4 / 4
Total scored questions: 16
Mean questions per model: 4.0
Binary minimum: 4
Mean question overhead: 0.0
Mean divider efficiency across model-runs: 1.0
```

Every tested model reached its hidden target in the information-theoretic minimum number of binary questions.

Every scored property choice matched a strongest available divider at the state where it was selected.

All four model-runs therefore followed the same candidate-count reduction pattern:

```text
16 → 8 → 4 → 2 → 1
```

---

## Property Selection Paths

| Model | Step 1 | Step 2 | Step 3 | Step 4 |
|---|---|---|---|---|
| GPT-5.6 Sol | P02 | P04 | P01 | P07 |
| Claude Opus 5 | P02 | P07 | P10 | P04 |
| Gemini 3.1 Pro | P02 | P04 | P01 | P03 |
| Grok 4.5 | P02 | P04 | P07 | P01 |

All four models selected `P02` as the first distinction. At the full N16 state, `P02` produces an 8 / 8 partition and is therefore a maximally discriminating first question.

The later paths diverged while preserving ideal reduction. The models therefore reached the same optimal candidate-count trajectory through multiple valid property sequences rather than one fixed question order.

---

## Run Integrity

All four N16 runs had complete scored transcripts and reported no target leakage, invalid or compound P question, inactive property use, invalid operator response, interruption, or tool failure.

Claude Opus 5 did record an **output-format / interaction deviation**: despite the instruction `Begin with your first P question only`, its first turn included a lead-in before the valid P02 question, and later turns included brief candidate-count progress narration. Each scored turn still contained exactly one valid active-property question. The additional narration did not change the property choice, reveal the target, or prevent deterministic interpretation, so the task result remains `SUCCESS`.

---

## Non-Scored Interaction Observations

These observations are descriptive only and are **not part of TEST_001 competence scoring**.

Claude Opus 5 again externalized candidate-count progress between valid questions. The same behavior occurred in its RUN_001 / N08 run, so the narration pattern has now appeared across two consecutive Claude conditions. The additional text also increases output-token use relative to a minimal interaction path, although no token, latency, or monetary magnitude was measured.

Gemini 3.1 Pro and Grok 4.5 again used minimal scored interactions without unsolicited candidate-count narration, matching their N08 behavior. GPT-5.6 Sol likewise used a minimal scored interaction in this N16 run.

These repeated observations strengthen the evidence for recurring interaction-style tendencies, but they remain non-scored and should not be treated as universal model characteristics from only two conditions.

---

## Cross-Condition Observation So Far

RUN_001 / N08 and RUN_002 / N16 are now complete across the same four models.

Across the first two candidate-space conditions:

```text
Completed model-condition runs: 8 / 8
Correct final identifications: 8 / 8
Unique resolutions: 8 / 8
Total scored questions: 28
Total question overhead above binary minimum: 0
Mean divider efficiency across completed model-runs: 1.0
```

The candidate space doubled from `N = 8` to `N = 16`, and the ideal path length increased by exactly one question:

```text
N = 8  → 3 questions → 8 → 4 → 2 → 1
N = 16 → 4 questions → 16 → 8 → 4 → 2 → 1
```

So far, all four tested models preserved maximum available elimination as the candidate space doubled once.

This is positive early scaling evidence, but it is not sufficient to assign the final TEST_001 outcome. The next conditions are:

```text
RUN_003 → N = 32
RUN_004 → N = 64
```

No final `SUPPORTED`, `MIXED`, `WEAKENED`, or `UNRESOLVED` TEST_001 outcome is assigned at this stage.

---

## Evidence

### GPT-5.6 Sol

- `runs/RUN_002_N16_GPT56SOL_TEST_001.md`
- `runs/RUN_002_N16_GPT56SOL_TEST_001_SCORE.md`

### Claude Opus 5

- `runs/RUN_002_N16_CLAUDEOPUS5_TEST_001.md`
- `runs/RUN_002_N16_CLAUDEOPUS5_TEST_001_SCORE.md`

### Gemini 3.1 Pro

- `runs/RUN_002_N16_GEMINI31PRO_TEST_001.md`
- `runs/RUN_002_N16_GEMINI31PRO_TEST_001_SCORE.md`

### Grok 4.5

- `runs/RUN_002_N16_GROK45_TEST_001.md`
- `runs/RUN_002_N16_GROK45_TEST_001_SCORE.md`

### Prior condition summary

- `results/RUN_001_N08_SUMMARY.md`

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
