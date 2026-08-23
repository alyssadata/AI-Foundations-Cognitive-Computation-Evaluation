# AI Foundations | Cognitive Computation Evaluation

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Evaluated external source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**Public source:** PhilArchive Version 1 — NAUNOC-2  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Current status:** **TEST_001 COMPLETE — OUTCOME: SUPPORTED**

---

## What This Repository Does

This repository evaluates selected claims from Oleksandr Naumenko's independently authored paper *Nature of Cognitive Computation* using AI Foundations evaluation methods.

**External evaluation ≠ framework incorporation.**

The paper remains external to AI Foundations regardless of the evaluation outcome.

---

## Completed Evaluation — TEST_001

TEST_001 asks:

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

The evaluation isolates one bounded dependency inside the external paper's hierarchical-recognition argument. The system receives the complete candidate/property matrix but is not given a decision tree or required question order. It must select its own successive binary distinctions.

### Completed formal run set

Four candidate-space conditions were tested:

| Run | Candidate Space | Active Properties | Binary Minimum |
|---|---:|---:|---:|
| RUN_001 | 8 | 6 | 3 |
| RUN_002 | 16 | 8 | 4 |
| RUN_003 | 32 | 10 | 5 |
| RUN_004 | 64 | 12 | 6 |

The same four model families were tested at every condition:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

This produced **16 formal model-condition runs**.

### Completed result

```text
Completed formal runs: 16 / 16
Correct final identifications: 16 / 16
Unique resolutions: 16 / 16
Total scored questions: 72
Total question overhead above binary minimum: 0
Overall mean model-run divider efficiency: 0.9928385417
```

Every formal run reached the correct target at the binary minimum number of questions for its condition.

Frozen protocol criteria were satisfied.

# TEST_001 OUTCOME: SUPPORTED

The complete bounded result, interpretation, limitations, and evidence map are here:

**[results/TEST_001_EVALUATION_AND_RESULTS.md](results/TEST_001_EVALUATION_AND_RESULTS.md)**

---

## Evidence Structure

### Protocol

- [protocol/TEST_001.md](protocol/TEST_001.md)
- [protocol/TEST_001_EASY_RUN_SHEET.md](protocol/TEST_001_EASY_RUN_SHEET.md)
- [protocol/score_test_001.py](protocol/score_test_001.py)

### Condition summaries

- [results/RUN_001_N08_SUMMARY.md](results/RUN_001_N08_SUMMARY.md)
- [results/RUN_002_N16_SUMMARY.md](results/RUN_002_N16_SUMMARY.md)
- [results/RUN_003_N32_SUMMARY.md](results/RUN_003_N32_SUMMARY.md)
- [results/RUN_004_N64_SUMMARY.md](results/RUN_004_N64_SUMMARY.md)

### Full run evidence

Each formal model-condition run is preserved under `runs/` with archival run records, normalized traces, deterministic scored-step files, trace summaries, and score summaries.

The evidence remains distributed rather than collapsed into the final result page so that the conclusion can be traced back to the underlying runs.

---

## What TEST_001 Supports

Within the frozen claim ceiling, the completed result supports this bounded conclusion:

> **Within a defined identification problem containing measurable candidate distinctions, the tested intelligent systems autonomously selected successive distinctions that preserved a strong elimination advantage and correctly identified their targets.**

This is positive evidence for the operationalized dependency tested here.

---

## What TEST_001 Does Not Establish

TEST_001 does not establish that:

- arbitrary real-world recognition problems arrive with a defined candidate set;
- useful distinctions are always available;
- a system can construct the relevant ontology from an unbounded environment;
- every selected distinction will be globally optimal;
- all cognitive recognition is `O(log N)`;
- biological cognition uses this procedure;
- or *Nature of Cognitive Computation* is supported as a whole.

The controlled matrix supplies the representation in which distinctions can be measured. The harder question of how such a representation is constructed remains outside TEST_001.

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
