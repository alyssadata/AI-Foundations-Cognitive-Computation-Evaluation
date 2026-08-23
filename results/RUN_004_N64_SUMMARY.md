# AI Foundations | TEST_001 — RUN_004 / N64 Summary

## Condition Identity

TEST: `TEST_001`  
RUN: `RUN_004`  
CONDITION: `N = 64`  
ACTIVE PROPERTIES: 12  
BINARY MINIMUM: 6 questions  
MODELS COMPLETED: 4

Models:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

RUN_004 / N64 is the final formal candidate-space condition in TEST_001.

---

## Cross-Model Results

| Model | Hidden Target | Final Answer | Questions | Minimum | Overhead | Mean Divider Efficiency | Result |
|---|---|---|---:|---:|---:|---:|---|
| GPT-5.6 Sol | C04 | C04 | 6 | 6 | 0 | 1.0 | SUCCESS |
| Claude Opus 5 | C17 | C17 | 6 | 6 | 0 | 1.0 | SUCCESS |
| Gemini 3.1 Pro | C33 | C33 | 6 | 6 | 0 | 0.9479166667 | SUCCESS |
| Grok 4.5 | C11 | C11 | 6 | 6 | 0 | 1.0 | SUCCESS |

### Aggregate RUN_004 / N64 Result

```text
Correct final identifications: 4 / 4
Unique resolutions: 4 / 4
Successful model-runs: 4 / 4
Total scored questions: 24
Mean questions per model: 6.0
Binary minimum: 6
Mean question overhead: 0.0
Mean divider efficiency across model-runs: 0.9869791667
```

Every tested model reached its hidden target in the information-theoretic minimum number of binary questions.

Three model-runs selected a strongest available divider at every scored step. Gemini 3.1 Pro did not: its first distinction, `P01`, split the full N64 candidate space `22 / 42` even though `32 / 32` dividers were available. Its subsequent five choices were strongest available for the realized remaining states.

RUN_004 therefore reproduces the distinction first observed at N32: minimum-question identification can still occur on the realized target path even when every selected distinction is not globally strongest.

---

## Property Selection Paths

| Model | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 | Step 6 |
|---|---|---|---|---|---|---|
| GPT-5.6 Sol | P02 | P04 | P05 | P07 | P06 | P01 |
| Claude Opus 5 | P02 | P04 | P05 | P07 | P09 | P10 |
| Gemini 3.1 Pro | P01 | P02 | P04 | P05 | P07 | P03 |
| Grok 4.5 | P02 | P04 | P05 | P07 | P03 | P09 |

Candidate-count paths:

```text
GPT-5.6 Sol:   64 → 32 → 16 → 8 → 4 → 2 → 1
Claude Opus 5: 64 → 32 → 16 → 8 → 4 → 2 → 1
Gemini 3.1 Pro:64 → 42 → 21 → 10 → 5 → 3 → 1
Grok 4.5:      64 → 32 → 16 → 8 → 4 → 2 → 1
```

GPT-5.6 Sol, Claude Opus 5, and Grok 4.5 opened with `P02`, a maximally discriminating `32 / 32` split. Gemini opened with `P01`, a weaker `22 / 42` split, then recovered through strongest available subsequent distinctions and still identified `C33` in six total questions.

---

## Protocol-Threshold Check at N64

The frozen TEST_001 protocol defines final `SUPPORTED` as requiring:

- every formal model-condition run to identify its target correctly;
- mean divider efficiency of at least `0.90` at each tested `N`;
- mean question overhead no more than `+1` above `ceil(log2 N)` at each tested `N`.

For N64:

```text
Correct identifications: 4 / 4
Mean divider efficiency: 0.9869791667
Mean question overhead: 0.0
```

RUN_004 / N64 therefore meets the numerical support thresholds for the final condition.

---

## Run Integrity

### GPT-5.6 Sol

The scored path was complete and valid. After the sixth operator answer, the model emitted one internally inconsistent narration line announcing another question, then immediately gave the final answer without asking another property. This is preserved as an **output-format / interaction deviation** and does not alter the six-question deterministic path or task result.

### Claude Opus 5

The scored path was complete and valid. Reading and analyzing the supplied matrix with bash is part of the task and is not classified as a protocol deviation.

Claude again included unsolicited matrix-analysis and candidate-state narration despite the instruction to begin with the first P question only. This is preserved as an **output-format / interaction deviation**. It did not alter the scored path or task result.

### Gemini 3.1 Pro

The scored path was complete and valid. Use of the supplied file through the available Python/data-analysis tool is not classified as a protocol deviation. No target leakage, invalid question, inactive property use, interruption, or other scored-run deviation was reported.

### Grok 4.5

The scored path was complete and valid. No target leakage, invalid or compound question, inactive property use, interruption, tool failure, or other deviation was reported.

---

## Cross-Condition Completion

All four formal TEST_001 candidate-space conditions are now complete across the same four models.

```text
N = 8  → 4 / 4 correct → 12 total questions → mean efficiency 1.0
N = 16 → 4 / 4 correct → 16 total questions → mean efficiency 1.0
N = 32 → 4 / 4 correct → 20 total questions → mean efficiency 0.984375
N = 64 → 4 / 4 correct → 24 total questions → mean efficiency 0.9869791667
```

Across the complete formal run set:

```text
Completed model-condition runs: 16 / 16
Correct final identifications: 16 / 16
Unique resolutions: 16 / 16
Total scored questions: 72
Total question overhead above binary minimum: 0
Overall mean model-run divider efficiency: 0.9928385417
```

The scaling ladder was preserved exactly in realized question count for every model-condition run:

```text
N = 8  → 3 questions
N = 16 → 4 questions
N = 32 → 5 questions
N = 64 → 6 questions
```

The complete formal run set now permits assignment of the final TEST_001 outcome under the frozen protocol.

---

## Evidence

### N64 model-runs

- `runs/RUN_004_N64_GPT56SOL_TEST_001.md`
- `runs/RUN_004_N64_GPT56SOL_TEST_001_SCORE.md`
- `runs/RUN_004_N64_CLAUDEOPUS5_TEST_001.md`
- `runs/RUN_004_N64_CLAUDEOPUS5_TEST_001_SCORE.md`
- `runs/RUN_004_N64_GEMINI31PRO_TEST_001.md`
- `runs/RUN_004_N64_GEMINI31PRO_TEST_001_SCORE.md`
- `runs/RUN_004_N64_GROK45_TEST_001.md`
- `runs/RUN_004_N64_GROK45_TEST_001_SCORE.md`

### Prior condition summaries

- `results/RUN_001_N08_SUMMARY.md`
- `results/RUN_002_N16_SUMMARY.md`
- `results/RUN_003_N32_SUMMARY.md`

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
