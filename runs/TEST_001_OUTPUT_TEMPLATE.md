# AI Foundations | TEST_001 — Generated Run Output Template

**Claim:** EXT-CLM-004  
**Test:** TEST_001  
**Formal protocol:** `protocol/TEST_001.md`

---

## Purpose

This file defines the required structure of the **AI-generated archival output produced after a TEST_001 run**.

**The operator does not manually fill this sheet.**

After the tested AI gives its scored `FINAL ANSWER`, the operator uses **PASTE 2** from `protocol/TEST_001_EASY_RUN_SHEET.md`. That final collection prompt tells the same AI to return the complete run metadata, exact scored transcript, final-answer record, deviations, and scorer-ready trace in the structure below.

The AI-generated response is then saved as the run record, for example:

```text
runs/RUN_001_TEST_001.md
```

Use `UNKNOWN` for unavailable metadata. Never invent missing metadata or reconstruct an incomplete transcript.

---

# REQUIRED GENERATED OUTPUT

```text
# AI Foundations | TEST_001 — Run Output

## 1. Run Identity
RUN_ID:
DATE_TIME:
CANDIDATE_SPACE_N:
TRUE_HIDDEN_TARGET:
MODEL / SYSTEM / SOFTWARE VERSION:
INTERFACE / PRODUCT / ENVIRONMENT:
FRESH_CONTEXT_USED:
TOOLS / FILE ACCESS:
SAMPLING SETTINGS IF AVAILABLE:

## 2. Exact Start Prompt
[EXACT PASTE 1 PROMPT AS SENT, INCLUDING THE ACTUAL N]

## 3. Verbatim Scored Interaction
[EXACT INTERACTION FROM THE FIRST PROPERTY QUESTION THROUGH FINAL ANSWER]

If exact transcript access is incomplete, write:
TRANSCRIPT ACCESS INCOMPLETE

## 4. Final Identification
MODEL_FINAL_ANSWER:
CORRECT_IDENTIFICATION: YES / NO

## 5. Scorer-Ready Trace
candidate_space_n,target,step,property,answer
[ONE ROW PER SCORED PROPERTY QUESTION]

## 6. Deviations / Missing Data
TARGET_LEAKED_BEFORE_FINAL_ANSWER: YES / NO / UNKNOWN
NON_YES_NO_OPERATOR_RESPONSE_DURING_SCORED_RUN: YES / NO / UNKNOWN
INVALID_OR_COMPOUND_MODEL_QUESTION: YES / NO / UNKNOWN
INTERRUPTION_OR_TOOL_FAILURE: YES / NO / UNKNOWN
TRANSCRIPT_ACCESS: COMPLETE / INCOMPLETE
OTHER_DEVIATION:

## 7. Scoring Status
SCORING_STATUS: PENDING

## 8. Archival Integrity Note
[STATE WHETHER THE METADATA, START PROMPT, SCORED TRANSCRIPT, FINAL ANSWER, AND TRACE WERE RECOVERED COMPLETELY FROM THE CURRENT CONVERSATION]
```

---

## Scoring Happens After This Output Is Generated

Section 5 is saved separately as the scorer input, for example:

```text
runs/RUN_001_TEST_001_TRACE.csv
```

Then run:

```text
python protocol/score_test_001.py protocol/TEST_001_CANDIDATES.csv runs/RUN_001_TEST_001_TRACE.csv
```

The deterministic scorer, not the tested AI and not the operator, produces:

- question count;
- binary lower bound;
- question overhead;
- step-level elimination;
- best available divider;
- divider efficiency;
- final remaining candidate state.

Do not ask the tested AI to invent or estimate those scorer outputs in the archival record.

---

## Primary Evidence Rule

The original visible interaction remains primary evidence.

The generated run output is an archival extraction from that interaction. If the generated transcript conflicts with the visible interaction, preserve the visible interaction and mark the generated extraction as incomplete or discrepant rather than silently repairing it.

---

## External-Source Boundary

This run contributes evidence toward TEST_001 for EXT-CLM-004.

A single run does not establish that all cognition is logarithmic, that every recognition problem has a clean answer space, or that *Nature of Cognitive Computation* is supported as a whole.

**AI Foundations conducted the evaluation. AI Foundations did not author the evaluated external source.**

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
