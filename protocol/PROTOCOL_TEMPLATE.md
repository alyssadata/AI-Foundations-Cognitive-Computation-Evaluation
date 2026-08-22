# OPTIONAL TEMPLATE — `PROTOCOL.md`

**Use when the external evaluation includes a runnable test, evaluation, procedure, experiment, or repeatable execution path.**

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** [REPOSITORY NAME]  
**External source:** [EXTERNAL SOURCE TITLE]  
**External author / creator:** [EXTERNAL AUTHOR / CREATOR]  
**External source location:** [URL / DOI / REPOSITORY / FILE REFERENCE]  
**External source version / date:** [VERSION / DATE / UNKNOWN]  
**Claims register:** [CLAIMS REGISTER FILE / VERSION]  
**Protocol version:** [VERSION]  
**Date frozen:** [YYYY-MM-DD]

---

## 1. External-Source Boundary

This protocol evaluates an independently authored external source.

**AI Foundations is the evaluator, not the source or author of the evaluated work.**

The external source remains external to AI Foundations. Evaluation does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

The AI Foundations source-line applies to this evaluation protocol and related AI Foundations-authored evaluation materials, not to ownership or authorship of the external source.

---

## 2. Claims-Register Prerequisite

This protocol must test a claim already recorded in the repository's completed claims register.

**External Claim ID:** [EXT-CLM-###]  
**Claim label:** [SHORT LABEL]  
**Claim source status:** [EXPLICIT / DERIVED / INTERPRETIVE / AMBIGUOUS]  
**Claim source location:** [PAGE / SECTION / LINE / URL / OTHER]

Do not create a new external claim inside the protocol merely because a test would be easier to design around it.

If operationalization reveals that the registered claim is ambiguous, underspecified, or materially different from what the protocol would need to test, return to the claims register and record that problem before proceeding.

**Claim extraction comes before operationalization.**

---

## 3. Evaluation Target

**External claim / mechanism / artifact ID:** [EXT-CLM-### OR OTHER REGISTERED ID]

[State exactly what registered external claim, mechanism, artifact, behavior, or proposition this protocol evaluates.]

Quote or cite the external source precisely enough that the tested claim can be recovered without reinterpretation.

Define all required variables, statuses, labels, or predicates before execution.

Do not import criteria that are irrelevant to the claim being tested.

---

## 4. Testable Prediction

State what observable result the external claim predicts.

```text
EXTERNAL CLAIM ID:
EXTERNAL CLAIM:
OPERATIONALIZATION:
PREDICTED OBSERVATION:
OBSERVATION THAT WOULD WEAKEN / FALSIFY THE CLAIM:
UNRESOLVED CONDITION:
```

Do not design the test so that merely using the external source's own terminology guarantees the conclusion.

---

## 5. Status / Outcome Space

[Define the allowed outcomes for this evaluation.]

Example only:

```text
OUTCOME ∈ {SUPPORTED, WEAKENED, UNRESOLVED}
```

Use `PASS / FAIL / UNRESOLVED` only when that language accurately matches the claim and protocol.

---

## 6. Required Run Record

Preserve metadata relevant to reproducibility.

Suggested fields:

```text
RUN_ID:
DATE_TIME:
EXTERNAL_SOURCE_ID / VERSION:
CLAIM_ID:
CLAIMS_REGISTER_VERSION:
MODEL / SYSTEM / SOFTWARE VERSION:
INTERFACE / ENVIRONMENT:
MEMORY / PRIOR HISTORY:
TOOLS / FILE ACCESS:
SYSTEM / DEVELOPER INSTRUCTIONS AVAILABLE:
SAMPLING SETTINGS IF AVAILABLE:
INPUT / STIMULUS ID OR HASH:
CODE COMMIT / VERSION:
FULL TRANSCRIPT OR RAW OUTPUT PRESERVED: yes/no
FINAL OUTCOME:
NOTES:
```

If a field is unavailable, record `UNKNOWN` rather than guessing.

---

## 7. Entry Condition

[Define what must happen before the protocol begins.]

The entry condition must match the evaluated external claim and must not presuppose the result.

---

## 8. Execution Phases

Create only the phases needed for this evaluation.

For each phase include:

```text
PHASE NAME:
PURPOSE:
EXACT OPERATOR ACTION:
EXACT PROMPT / INPUT / PROCEDURE, IF APPLICABLE:
WHAT TO PRESERVE:
OUTCOME RULE, IF APPLICABLE:
```

Do not add extra human scorers, reviewers, co-evaluators, or auditors to the initial study unless the evaluation explicitly requires them.

---

## 9. Decision Rule

[State the deterministic or predeclared rule for assigning the final outcome.]

Do not change the decision rule after seeing results without recording the revision as a protocol change.

---

## 10. Controls / Comparators / Ablations

[State any baseline, control, alternative architecture, ablation, or comparison needed to distinguish the external theory's prediction from an ordinary or competing explanation.]

Delete this section only when no meaningful comparator is required.

---

## 11. Non-Qualifying Evidence / Confounds

[List shortcuts, confounds, or evidence that must not be treated as sufficient.]

Prevent the evaluation from being passed by superficial compliance, copied language, evaluator vocabulary, prompt leakage, or retrospective reinterpretation.

---

## 12. Claim Ceiling

State the strongest claim the result supports about the **registered external claim under evaluation**.

Then explicitly state what the result does **not** establish.

A result may support an external claim without incorporating that claim into AI Foundations.

---

## 13. Reproducibility Boundary

The frozen protocol defines the study. Pair it with:

- `claims/CLAIMS_REGISTER_TEMPLATE.md` or its completed child file as the authoritative claim record;
- `protocol/EASY_RUN_SHEET_TEMPLATE.md` when an operator-facing execution sheet is useful;
- `runs/RUN_OUTPUT_TEMPLATE.md` when runs need a consistent evidence record.

Preserve source identity, claim identity, claims-register version, protocol version, and raw evidence across reruns.

---

## 14. Final External-Source Boundary

**External evaluation ≠ framework incorporation.**

A positive, negative, or unresolved result does not make the evaluated external source part of AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
