# OPTIONAL TEMPLATE — `RUN_OUTPUT.md`

**Use when an external evaluation produces one or more runs whose results should be preserved in a consistent record.**

This file is an evidence schema. Customize it to the actual protocol and external claim. Do not retain irrelevant fields or invent scoring categories after the run.

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** [REPOSITORY NAME]  
**External source:** [EXTERNAL SOURCE TITLE]  
**External author / creator:** [EXTERNAL AUTHOR / CREATOR]  
**External source version / identifier:** [VERSION / IDENTIFIER / UNKNOWN]  
**Claim / test ID:** [ID]  
**Run ID:** [RUN ID]  
**Date:** [YYYY-MM-DD]

---

## 1. External Source / Claim Identity

```text
EXTERNAL SOURCE TITLE:
EXTERNAL AUTHOR / CREATOR:
SOURCE LOCATION:
SOURCE VERSION / DATE / IDENTIFIER:
MATERIAL UNDER EVALUATION:
CLAIM_ID:
CLAIM TEXT / PREDECLARED PROPOSITION:
PROTOCOL VERSION:
```

The external source identity must remain separate from the AI Foundations evaluation identity.

---

## 2. Run Metadata

```text
RUN_ID:
DATE_TIME:
MODEL / SYSTEM / SOFTWARE VERSION:
INTERFACE / PRODUCT / ENVIRONMENT:
CONDITION / ARM:
MEMORY OR PRIOR HISTORY:
TOOLS / FILE ACCESS:
SYSTEM / DEVELOPER INSTRUCTIONS AVAILABLE:
SAMPLING SETTINGS IF AVAILABLE:
INPUT / STIMULUS NAME:
INPUT / STIMULUS ID OR HASH:
CODE COMMIT / VERSION:
OPERATOR:
TRANSCRIPT / RAW OUTPUT PRESERVED: yes/no
```

Use `UNKNOWN` for unavailable fields. Do not infer hidden settings.

---

## 3. Final Evaluation Outcome

```text
FINAL OUTCOME:
```

Allowed values:

```text
[INSERT THE EXACT OUTCOME / STATUS SPACE FROM THE FROZEN PROTOCOL]
```

Do not invent new outcome labels during a run.

---

## 4. Criteria / Measures — If Applicable

Delete this section if the evaluation does not use criterion-level scoring or quantitative measures.

```text
[CRITERION OR MEASURE 1]:
[CRITERION OR MEASURE 2]:
[CRITERION OR MEASURE 3]:
```

Use the exact definitions from the frozen protocol.

For each criterion or measure, preserve the relevant evidence pointer or raw value.

---

## 5. Comparator / Control Record — If Applicable

```text
BASELINE / CONTROL:
ALTERNATIVE / ABLATION:
MATCHED VARIABLES:
DIFFERING VARIABLE:
RESULT:
```

Delete this section only when no comparator is required by the protocol.

---

## 6. Revision / State-Change Record — If Applicable

```text
REVISION EVENT: YES / NO
EARLIER STATUS / OUTPUT:
LATER STATUS / OUTPUT:
STATED REASON:
TURN / LOCATION:
```

Do not erase earlier states when a later revision occurs.

---

## 7. Exceptions, Deviations, or Missing Data

```text
PROTOCOL DEVIATION: YES / NO
DESCRIPTION:
MISSING DATA:
INTERRUPTION / TOOL FAILURE:
SOURCE VERSION UNCERTAINTY:
OTHER NOTES:
```

A deviation should remain visible rather than being silently repaired.

---

## 8. Verbatim Transcript / Raw Output

For interactive studies, preserve the complete run exactly as it occurred.

For non-transcript studies, preserve the appropriate raw evidence: logs, tables, files, hashes, structured records, benchmark outputs, code results, or other primary evidence.

Do not summarize, paraphrase, silently correct, or replace repeated content with shorthand when the protocol requires verbatim preservation.

---

## 9. Evidence Files

```text
EXTERNAL SOURCE RECORD:
SOURCE COPY / RECOVERABLE SOURCE LOCATION:
PROTOCOL VERSION:
ORIGINAL INTERFACE / RUNTIME RECORD:
INPUT / STIMULUS FILES:
RAW OUTPUT FILES:
CODE / COMMIT:
SCREENSHOTS / EXPORTS:
HASHES:
OTHER:
```

Primary evidence has priority over reconstructed or summarized copies.

---

## 10. Claim Boundary

State the exact claim this run supports, weakens, falsifies, or leaves unresolved under the protocol:

> [INSERT EVALUATION-SPECIFIC CLAIM CEILING]

State explicitly what this run does **not** establish:

- [NON-CLAIM 1]
- [NON-CLAIM 2]

A result about an external source does not establish that the external source is part of AI Foundations.

---

## 11. External-Source Boundary

**AI Foundations conducted this evaluation. AI Foundations did not author the evaluated external source.**

The external source remains external to AI Foundations.

The result does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

Positive results are not adoption.
Negative results are not appropriation.
Unresolved results are not incorporation.

---

## 12. Completion Check

```text
[ ] External source / author / location recorded
[ ] Source version / identifier recorded or marked UNKNOWN
[ ] Exact claim / material under evaluation recorded
[ ] Required metadata recorded or marked UNKNOWN
[ ] Exact protocol outcome used
[ ] Required criteria / measures recorded, if applicable
[ ] Controls / comparators preserved, if applicable
[ ] Deviations preserved
[ ] Primary evidence saved
[ ] Transcript / raw output preserved as required
[ ] No missing content silently reconstructed
[ ] Claim ceiling preserved
[ ] External-source boundary preserved
```

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
