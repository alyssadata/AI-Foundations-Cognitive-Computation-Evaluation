# AI Foundations | Cognitive Computation Evaluation

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Evaluated external source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**Public source:** PhilArchive Version 1 — NAUNOC-2  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Status:** TEST_001 protocol frozen; formal runs pending

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
runs/TEST_001_OUTPUT_TEMPLATE.md
        ↓
formal run evidence
        ↓
results
```

### 1. Source

[`source/EXTERNAL_SOURCE.md`](source/EXTERNAL_SOURCE.md)

Records exactly which external paper/version is being evaluated.

### 2. Claims

[`claims/CLAIMS_REGISTER.md`](claims/CLAIMS_REGISTER.md)

Records the claims extracted from the paper before test design.

### 3. Formal TEST_001 Protocol

[`protocol/TEST_001.md`](protocol/TEST_001.md)

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

### 4. Easy Run Sheet — Use This to Actually Run the Test

[`protocol/TEST_001_EASY_RUN_SHEET.md`](protocol/TEST_001_EASY_RUN_SHEET.md)

Contains the exact operator workflow, including:

- what file to attach;
- how to choose the hidden target;
- the exact first prompt to paste into a fresh model context;
- exactly how to answer each model question;
- how to record the trace;
- the optional post-run transcript extraction paste;
- and the scoring command.

### 5. Run Output Sheet — One Copy Per Formal Run

[`runs/TEST_001_OUTPUT_TEMPLATE.md`](runs/TEST_001_OUTPUT_TEMPLATE.md)

Copy this once for every formal run. It records the exact prompt, verbatim scored interaction, hidden target, final answer, scorer outputs, deviations, and run-level evidence.

### 6. Supporting TEST_001 Assets

- [`protocol/TEST_001_CANDIDATES.csv`](protocol/TEST_001_CANDIDATES.csv) — controlled answer space.
- [`protocol/TEST_001_RUN_TRACE_TEMPLATE.csv`](protocol/TEST_001_RUN_TRACE_TEMPLATE.csv) — raw question/answer trace format.
- [`protocol/score_test_001.py`](protocol/score_test_001.py) — deterministic scoring for elimination and divider efficiency.

---

## Current Status

**TEST_001 is designed and frozen. No formal TEST_001 results have been declared yet.**

The `runs/` folder currently contains the output template. Actual run evidence is added only when a formal run is completed.

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
