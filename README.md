# AI Foundations | Cognitive Computation Evaluation

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Evaluated external source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**Public source:** PhilArchive Version 1 — NAUNOC-2  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Status:** TEST_001 protocol v2.2.0 frozen; formal runs in progress

---

## What This Repository Does

This repository evaluates selected claims from Oleksandr Naumenko's independently authored paper *Nature of Cognitive Computation* using AI Foundations evaluation methods.

**External evaluation ≠ framework incorporation.**

The paper remains external to AI Foundations regardless of the evaluation outcome.

---

## Start Here

```text
source/EXTERNAL_SOURCE.md
        ↓
claims/CLAIMS_REGISTER.md
        ↓
protocol/TEST_001.md
        ↓
protocol/TEST_001_EASY_RUN_SHEET.md
        ↓
AI generates the complete run output after the scored interaction
        ↓
score generated trace
        ↓
results
```

### Formal TEST_001 Protocol

[`protocol/TEST_001.md`](protocol/TEST_001.md)

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

### Easy Run Sheet — Use This to Actually Run the Test

[`protocol/TEST_001_EASY_RUN_SHEET.md`](protocol/TEST_001_EASY_RUN_SHEET.md)

Plain-language rule:

**I pick a C.**  
**The AI asks from P.**  
**I answer YES/NO until it identifies my C.**

The operator does **not** manually fill an output sheet or calculate scores during the run.

---

## TEST_001 Run Map

The run number identifies the N condition across all tested models:

```text
RUN_001 → N = 8
RUN_002 → N = 16
RUN_003 → N = 32
RUN_004 → N = 64
```

Every model follows the same four-run sequence. The complete run ID adds the model tag so parallel runs remain unique, for example:

```text
RUN_001_N08_GPT56SOL
RUN_001_N08_<OTHER_MODEL_TAG>
RUN_002_N16_GPT56SOL
RUN_003_N32_GPT56SOL
RUN_004_N64_GPT56SOL
```

The run number is **not** a replicate number.

---

## Condition-Specific Input Files

Use **one** input file per run:

```text
N = 8  → protocol/TEST_001_INPUT_N08.csv → 8 C's, 6 active P's
N = 16 → protocol/TEST_001_INPUT_N16.csv → 16 C's, 8 active P's
N = 32 → protocol/TEST_001_INPUT_N32.csv → 32 C's, 10 active P's
N = 64 → protocol/TEST_001_INPUT_N64.csv → 64 C's, 12 active P's
```

Each file contains only the candidate rows and P columns active for that condition.

The scaling rule is:

```text
active P count = 2 × log2(N)
```

So each condition preserves a **1:1 ratio between the minimum discriminating capacity required for unique identification and additional available property choices**.

The full backend matrix is [`protocol/TEST_001_CANDIDATES.csv`](protocol/TEST_001_CANDIDATES.csv). It contains all 64 candidates and all 12 properties and is used by the deterministic scorer.

---

## Generated Run Output

[`runs/TEST_001_OUTPUT_TEMPLATE.md`](runs/TEST_001_OUTPUT_TEMPLATE.md)

This defines the structure the tested AI generates after the scored interaction. It is **not** a manual worksheet.

The generated response is saved as the actual model-tagged run record, for example:

```text
runs/RUN_001_N08_GPT56SOL_TEST_001.md
```

The scorer-ready trace uses:

```text
run_id,candidate_space_n,target,final_answer,step,property,answer
```

The deterministic scorer is [`protocol/score_test_001.py`](protocol/score_test_001.py).

---

## Actual Operator Flow

```text
choose RUN / N condition
→ upload matching TEST_001_INPUT_Nxx.csv
→ privately pick one C
→ send PASTE 1
→ AI asks from the P columns in that file
→ answer only YES/NO from your chosen C row
→ AI gives FINAL ANSWER
→ send PASTE 2 with model-tagged RUN_ID + true C
→ AI generates metadata + exact transcript + scorer-ready trace
→ save generated run output
→ score trace afterward
```

No manual transcript reconstruction. No manual output-sheet completion. No scoring during the live test.

---

## Current Status

**TEST_001 v2.2.0 is designed and frozen. Formal runs are in progress.**

`RUN_001_N08_GPT56SOL` has been completed and archived as the first formal model-condition run. Additional models may complete their own `RUN_001_N08_<MODEL_TAG>` runs under the same N08 condition before the sequence advances through RUN_002 / N16, RUN_003 / N32, and RUN_004 / N64.

The `results/` stage is created only after the formal run set has produced evidence sufficient for synthesis.

---

## External-Source Boundary

**AI Foundations is the evaluator, not the author or source of the evaluated paper.**

Evaluation, citation, support, weakening, or falsification of an external claim does not incorporate that claim, its terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

---

## Citation Separation

**External source:**  
Oleksandr Naumenko, *Nature of Cognitive Computation*, PhilArchive, Version 1, archived September 10, 2025, record NAUNOC-2.

**AI Foundations evaluation:**  
Alyssa Solen, *AI Foundations: Cognitive Computation Evaluation*, AI-Foundations-Cognitive-Computation-Evaluation Repository. Source-line: Alyssa Solen → AI Foundations → Origin | Continuum.

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
