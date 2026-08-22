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

The repository now has one active evaluation path:

```text
source/EXTERNAL_SOURCE.md
        ↓
claims/CLAIMS_REGISTER.md
        ↓
protocol/TEST_001.md
        ↓
formal runs
        ↓
results
```

### 1. Source

[`source/EXTERNAL_SOURCE.md`](source/EXTERNAL_SOURCE.md)

Records exactly which external paper/version is being evaluated and preserves the source boundary.

### 2. Claims

[`claims/CLAIMS_REGISTER.md`](claims/CLAIMS_REGISTER.md)

Records the claims extracted from the paper before test design.

### 3. Active Test

[`protocol/TEST_001.md`](protocol/TEST_001.md)

**TEST_001 question:**

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

### 4. TEST_001 Assets

- [`protocol/TEST_001_CANDIDATES.csv`](protocol/TEST_001_CANDIDATES.csv) — the controlled answer space.
- [`protocol/TEST_001_RUN_TRACE_TEMPLATE.csv`](protocol/TEST_001_RUN_TRACE_TEMPLATE.csv) — the exact trace format used to record a run.
- [`protocol/score_test_001.py`](protocol/score_test_001.py) — deterministic scoring for elimination and divider efficiency.

That is the entire active test.

---

## Current Status

**TEST_001 is designed and frozen. No formal TEST_001 runs or results have been added yet.**

The `runs/` and `results/` stages are created only when actual formal evidence exists.

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
