# AI Foundations | External Claims Register Template

**Evaluation repository:** [REPOSITORY NAME]  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**AI Foundations source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**External source:** [EXTERNAL SOURCE TITLE]  
**External author / creator:** [EXTERNAL AUTHOR / CREATOR]  
**External source version / date:** [VERSION / DATE / UNKNOWN]  

---

## Purpose

This file records the claims made by the independently authored external source **before** AI Foundations designs tests for them.

The purpose is to prevent the evaluation from drifting away from what the external source actually claims.

The claims recorded here remain claims of the **external source**. Extracting, organizing, operationalizing, testing, supporting, weakening, or falsifying them does **not** incorporate them into AI Foundations or AI Foundations canon.

**External claim ≠ AI Foundations claim.**

---

## 1. Claim-Extraction Rule

Read the external source first and identify the claims that may matter to the evaluation.

For each claim:

- preserve the external author's meaning;
- record where the claim appears;
- distinguish explicit claims from evaluator inferences;
- do not strengthen the claim beyond the source;
- do not repair ambiguity silently;
- do not turn examples, metaphors, motivations, or background statements into claims unless the source actually uses them as claims;
- and do not design the test while extracting the claim.

Claim extraction comes **before** operationalization.

---

## 2. Claim Status Vocabulary

Use the following source-status labels:

```text
EXPLICIT — directly stated by the external source.
DERIVED — follows from multiple explicit statements but is not stated in one place; derivation must be shown.
INTERPRETIVE — plausible evaluator reading that requires confirmation or caution.
AMBIGUOUS — source wording does not support one stable interpretation.
```

Use the following evaluation-readiness labels:

```text
TESTABLE NOW — sufficiently bounded to operationalize.
NEEDS SHARPENING — potentially testable, but a term, scope, mechanism, or prediction is unclear.
CONCEPTUAL ONLY — meaningful claim but not presently suitable for empirical evaluation.
OUT OF SCOPE — intentionally excluded from the current evaluation.
```

These labels describe the evaluation state. They do not modify the external source.

---

## 3. Claims Index

Create one row for every claim entered below.

| Claim ID | Short label | Source status | Evaluation readiness | Source location | Selected for testing? |
|---|---|---|---|---|---|
| EXT-CLM-001 | [SHORT LABEL] | [EXPLICIT / DERIVED / INTERPRETIVE / AMBIGUOUS] | [STATUS] | [PAGE / SECTION / LINE / URL] | [YES / NO / LATER] |
| EXT-CLM-002 | [SHORT LABEL] | [STATUS] | [STATUS] | [LOCATION] | [YES / NO / LATER] |

Add rows as needed.

---

# CLAIM RECORD

Duplicate this section once for each claim.

## EXT-CLM-[###] — [SHORT CLAIM LABEL]

### A. External Claim

**Source status:** [EXPLICIT / DERIVED / INTERPRETIVE / AMBIGUOUS]  
**Evaluation readiness:** [TESTABLE NOW / NEEDS SHARPENING / CONCEPTUAL ONLY / OUT OF SCOPE]  
**Source location:** [PAGE / SECTION / PARAGRAPH / LINE / URL / TIMESTAMP / OTHER]  

**Exact quotation, if brief and permitted:**

> [INSERT SHORT SOURCE QUOTATION OR `NOT QUOTED`]

**Faithful claim statement:**

[State the external claim as narrowly and faithfully as possible. Do not strengthen it.]

### B. Scope

**Claim applies to:**

[Specify the entities, systems, conditions, domains, or situations the source says the claim applies to.]

**Claim does not clearly apply to:**

[Record explicit exclusions, limits, or `NOT SPECIFIED`.]

**Universality level:** [universal / general / conditional / local / example-specific / unclear]

### C. Terms That Must Hold

List any terms whose meaning materially affects the claim.

```text
TERM:
SOURCE DEFINITION / USE:
AMBIGUITY, IF ANY:
```

Do not substitute an AI Foundations definition for an external-source term.

### D. Dependencies

**Depends on earlier external claims:** [CLAIM IDs / NONE / UNKNOWN]  
**Supports later external claims:** [CLAIM IDs / NONE / UNKNOWN]

Record only dependencies actually supported by the source or required by the claim's logic.

### E. Evaluator Interpretation Check

**What the source clearly says:**

[INSERT]

**What would be an evaluator inference rather than a source claim:**

[INSERT OR NONE]

**Author clarification needed before testing:** [YES / NO]

If yes:

[STATE THE EXACT QUESTION THAT NEEDS CLARIFICATION]

### F. Testability Preview

Do **not** build the full protocol here. Record only whether the claim exposes an observable consequence.

**Observable consequence suggested by the claim:**

[INSERT / UNKNOWN]

**What kind of evidence could bear on it:**

[behavioral / computational / comparative / ablation / efficiency / prediction / implementation / archival / other]

**Main obstacle to testing, if any:**

[INSERT / NONE]

### G. Selection Decision

**Selected for current evaluation:** [YES / NO / LATER]  
**Reason:** [INSERT]

If selected, this claim ID must remain attached to its protocol, run records, outputs, and conclusions.

---

## 4. Claim-Set Review

Before protocol design begins, check:

```text
[ ] External source identity is already recorded in source/EXTERNAL_SOURCE_TEMPLATE.md or its completed child file
[ ] Every candidate claim has a stable Claim ID
[ ] Every claim has a recoverable source location
[ ] Explicit claims are separated from evaluator-derived or interpretive claims
[ ] Ambiguous claims are marked rather than silently repaired
[ ] External terminology has not been replaced with AI Foundations terminology
[ ] Scope and universality have not been strengthened beyond the source
[ ] Claims selected for testing are identified
[ ] No test has been designed to guarantee the external claim by definition
[ ] External claims remain attributed to the external author / source
```

---

## 5. Transition to Protocol

Only after the claims register is complete enough to identify the target claim should protocol design begin.

For each selected claim:

1. carry its `EXT-CLM-###` identifier into `PROTOCOL.md`;
2. operationalize the claim without changing its meaning;
3. predeclare the predicted observation;
4. predeclare what would weaken, falsify, or leave the claim unresolved;
5. define controls, comparators, or ablations where needed;
6. preserve the claim ID through every run and result record.

If operationalization reveals that the claim itself is ambiguous, return to the claims register and mark the ambiguity rather than silently changing the claim inside the protocol.

---

## External-Source Boundary

**AI Foundations is the evaluator, not the source or author of the claims recorded here.**

The external source remains external to AI Foundations.

Claim extraction, organization, testing, support, criticism, or falsification does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
