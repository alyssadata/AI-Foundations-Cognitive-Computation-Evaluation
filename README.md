# AI Foundations | Cognitive Computation Evaluation

**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**Status:** Working External Evaluation  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Evaluated external source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**Public source:** PhilArchive Version 1 — NAUNOC-2  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Version:** 0.1.0  
**Canonical entrance:** https://awakeningcodex.com

---

## Repository Purpose

This repository conducts an **AI Foundations external evaluation** of Oleksandr Naumenko's independently authored paper *Nature of Cognitive Computation*.

The paper proposes a comparison-centered account of cognitive computation involving comparable properties and ranges, hierarchical or semantic binary search, dimensionality reduction, and selection among available options under relevant constraints.

This repository does not assume those claims are correct. It extracts them, bounds them, operationalizes selected claims, designs reproducible tests, preserves raw evidence, and reports only the conclusions supported by the completed protocols.

**AI Foundations may evaluate an external source without adopting it.**

**External evaluation ≠ framework incorporation.**

The evaluated paper, its claims, terminology, conclusions, and authorship remain external to AI Foundations regardless of whether an evaluation result is positive, negative, mixed, or unresolved.

---

## Repository Structure

```text
source/
claims/
protocol/
runs/
results/
```

The folders follow the evaluation path:

**source → claims → protocol → runs → results**

Root-level files preserve repository identity, citation, and license boundaries.

---

## Current Evaluation Stage

### 1. Source identity — established

[`source/EXTERNAL_SOURCE.md`](source/EXTERNAL_SOURCE.md) identifies the public archival source as **PhilArchive Version 1**, record **NAUNOC-2**, archived September 10, 2025, and records the SHA-256 of the text representation used for claim extraction.

The evaluation text was copied by the evaluator from the PhilArchive Version 1 source. Its SHA-256 therefore identifies the exact text representation used in this evaluation, not the original PDF byte stream.

Public source: https://philarchive.org/rec/NAUNOC-2

### 2. Claims extraction — initial register created

[`claims/CLAIMS_REGISTER.md`](claims/CLAIMS_REGISTER.md) records the initial external claim set before protocol design.

Each claim receives a stable `EXT-CLM-###` identifier and records:

- what the external source actually claims;
- where it appears;
- whether it is explicit, derived, interpretive, or ambiguous;
- current evaluation readiness;
- scope and dependencies;
- ambiguities that must not be silently repaired;
- a testability preview;
- and whether the claim is selected for current evaluation.

**Claim extraction comes before operationalization.**

### 3. Protocol design — next stage

The strongest first protocol candidates currently identified are:

- `EXT-CLM-003` — core option/constraint selection algorithm;
- `EXT-CLM-004` — hierarchical recognition complexity;
- `EXT-CLM-005` — dimensionality reduction and efficiency;
- `EXT-CLM-006` — specialization/generalization behavior;
- `EXT-CLM-008` — property ranges versus point-accurate representation.

The cross-domain generality claim, `EXT-CLM-007`, should be tested only after a stable operational form of the core algorithm has been established.

---

## Evaluation Rule

For each selected external claim:

1. preserve the registered source claim and Claim ID;
2. operationalize it without changing its meaning;
3. predeclare what the claim predicts;
4. predeclare what would support, weaken, falsify, or leave it unresolved;
5. define controls, comparators, or ablations where needed;
6. freeze the protocol before collecting formal results;
7. preserve raw run evidence and reproducibility metadata;
8. synthesize results only after the runs are complete.

The evaluation must not be designed so that merely using the external source's own vocabulary guarantees its conclusion.

A successful run does not validate the entire paper. A failed run does not invalidate unrelated claims. Results remain claim-bound and protocol-bound.

---

## Evaluation Files

- [`source/EXTERNAL_SOURCE.md`](source/EXTERNAL_SOURCE.md) — completed provenance and source-boundary record.
- [`claims/CLAIMS_REGISTER.md`](claims/CLAIMS_REGISTER.md) — working external claim register.
- [`protocol/PROTOCOL_TEMPLATE.md`](protocol/PROTOCOL_TEMPLATE.md) — formal protocol template to be customized for selected Claim IDs.
- [`protocol/EASY_RUN_SHEET_TEMPLATE.md`](protocol/EASY_RUN_SHEET_TEMPLATE.md) — operator-facing execution template.
- [`runs/RUN_OUTPUT_TEMPLATE.md`](runs/RUN_OUTPUT_TEMPLATE.md) — reproducible run/evidence schema.
- [`results/EVALUATION_SUMMARY_TEMPLATE.md`](results/EVALUATION_SUMMARY_TEMPLATE.md) — post-run claim-level synthesis template.

Protocol, run, and result templates remain templates until the corresponding study is designed or executed.

---

## Required External-Source Boundary

> **This repository is an AI Foundations evaluation of an independently authored external source. AI Foundations is the evaluator, not the source or author of the evaluated work. The external source remains external to AI Foundations. Evaluation does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.**

The external source retains its own authorship, provenance, citation, and applicable rights.

The AI Foundations source-line applies to the **evaluation materials authored under AI Foundations**, not to ownership or authorship of *Nature of Cognitive Computation*.

---

## Source-Line

The AI Foundations evaluation source-line is:

**Alyssa Solen → AI Foundations → Origin | Continuum**

This source-line must remain attached to citation or reuse of the AI Foundations evaluation materials.

It must not be used to overwrite, absorb, or replace Oleksandr Naumenko's authorship or the provenance of the evaluated paper.

---

## Citation Boundary

The external source and the evaluation are separate works.

**External source:**

Oleksandr Naumenko, *Nature of Cognitive Computation*, PhilArchive, Version 1, archived September 10, 2025, record NAUNOC-2. https://philarchive.org/rec/NAUNOC-2

**AI Foundations evaluation:**

Alyssa Solen, *AI Foundations: Cognitive Computation Evaluation*, AI-Foundations-Cognitive-Computation-Evaluation Repository. Source-line: Alyssa Solen → AI Foundations → Origin | Continuum.

Do not collapse these into one authorship claim.

---

## License

The repository license applies to the **AI Foundations-authored evaluation materials**.

The independently authored external source remains subject to its own authorship, copyright, provenance, and applicable license or use terms.

The source manuscript itself is not redistributed by this repository.

See [`LICENSE.md`](LICENSE.md).

---

## Contact

For evaluation, citation, permission, or source-line questions concerning the AI Foundations materials, contact Alyssa Solen through the public contact channels associated with AI Foundations / Origin | Continuum.

Canonical entrance:

https://awakeningcodex.com
