# AI Foundations | TEST_001 — Easy Run Sheet

**Claim:** EXT-CLM-004  
**Test:** TEST_001  
**Formal protocol:** `protocol/TEST_001.md`

---

# WHAT YOU DO

## Plain-language version

**You pick a C. The AI asks about P's. You answer YES/NO until it identifies your C.**

- `C01`, `C02`, `C03`, etc. are the possible candidates.
- `P01` through `P10` are the properties the AI is allowed to ask about.
- You secretly choose one `C` from the active range.
- The AI does not know which `C` you chose.
- The AI asks about the `P` values one at a time.
- You answer `YES` or `NO` using the row for your chosen `C`.
- The AI keeps asking until it gives one final `C` as its answer.

For one run:

**fresh AI chat → upload candidate file → secretly choose one C → paste the start prompt → AI asks about P's → answer YES/NO → AI identifies a C → paste the final collection prompt → save the AI-generated run output**

That is the whole operator workflow.

You do **not** manually fill out an output sheet.
You do **not** manually reconstruct the transcript.
You do **not** calculate scores while the test is running.

The tested AI generates the run metadata, transcript, final-answer record, and scorer-ready trace **after the scored interaction is complete**.

---

# BEFORE THE RUN

## 1. Choose the run size

Use one of these:

```text
N = 8   → C01–C08
N = 16  → C01–C16
N = 32  → C01–C32
N = 64  → C01–C64
```

## 2. Open a fresh AI chat

Use a fresh context for every formal run.

## 3. Upload this file

```text
protocol/TEST_001_CANDIDATES.csv
```

## 4. Secretly choose the target C

Pick exactly one `C` from the active range.

Example:

```text
If N = 16, choose one C from C01–C16.
```

Keep that `C` private until the tested AI has given its final answer.

---

# PASTE 1 — START THE SCORED RUN

Replace both `[N]` entries before sending.

```text
You are participating in TEST_001.

The attached file contains the candidate matrix. For this run, the active answer space is C01 through C[N], for a total of [N] candidates. Exactly one active candidate has been privately selected as the hidden target.

Your task is to identify the hidden target.

Rules:
- Ask one YES/NO question at a time.
- Each question must ask about exactly one listed property, P01 through P10.
- You choose which property to ask next.
- No decision tree or property order will be supplied.
- Do not ask directly for the candidate name or label.
- Do not ask me to describe or reveal the target.
- Do not use compound questions.
- Continue until you are ready to identify one candidate.
- When ready, state exactly: FINAL ANSWER: Cxx

Begin with your first property question only.
```

---

# DURING THE SCORED RUN

**You already picked a C. Now the AI asks about P's.**

The AI will ask a property question such as:

```text
Is P04 YES for the hidden target?
```

Look at your chosen `C` row in `TEST_001_CANDIDATES.csv` and find `P04`.

Reply with **only**:

```text
YES
```

or

```text
NO
```

Then the AI asks another `P` question. Answer from the same chosen `C` row.

Continue until the AI states:

```text
FINAL ANSWER: Cxx
```

**The scored interaction ends at that final answer.**

Do not correct the AI before the final answer is recorded.

---

# PASTE 2 — GENERATE THE COMPLETE RUN OUTPUT

Only after the scored interaction has ended, replace `[RUN_ID]` and `[TRUE_TARGET]`, then paste this into the **same chat**:

```text
The scored interaction is complete.

RUN_ID: [RUN_ID]
TRUE_HIDDEN_TARGET: [TRUE_TARGET]
FRESH_CONTEXT_USED: YES

Generate the complete archival output for this TEST_001 run.

Do not invent unavailable metadata. For any metadata you cannot directly know or verify, write UNKNOWN.
Do not summarize, clean, repair, reinterpret, or reorder the scored interaction.
If you cannot recover the complete scored interaction exactly, write TRANSCRIPT ACCESS INCOMPLETE rather than reconstructing missing turns.
Do not calculate the deterministic TEST_001 scoring metrics. Set SCORING_STATUS: PENDING.

Return only the following run record:

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
Reproduce the exact PASTE 1 prompt used for this run, including the actual N.

## 3. Verbatim Scored Interaction
Reproduce the scored interaction exactly from your first property question through your FINAL ANSWER line.

## 4. Final Identification
MODEL_FINAL_ANSWER:
CORRECT_IDENTIFICATION: YES / NO

## 5. Scorer-Ready Trace
Return a CSV code block using exactly this header:
candidate_space_n,target,step,property,answer

Include one row for each scored property question, in chronological order. Use the true hidden target supplied above in the target column.

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
State whether the metadata, exact start prompt, scored transcript, final answer, and scorer-ready trace above were recovered completely from the current conversation. Do not claim completeness if any part is unavailable.
```

The tested AI's response to PASTE 2 is the **run output record**.

Save that response as:

```text
runs/RUN_XXX_TEST_001.md
```

You do **not** manually populate `runs/TEST_001_OUTPUT_TEMPLATE.md`. That file defines the required generated-output structure.

---

# AFTER THE MODEL GENERATES THE RUN OUTPUT

From Section 5 of the generated output, save the CSV block as:

```text
runs/RUN_XXX_TEST_001_TRACE.csv
```

Then scoring can be run with:

```text
python protocol/score_test_001.py protocol/TEST_001_CANDIDATES.csv runs/RUN_XXX_TEST_001_TRACE.csv
```

The scorer creates the quantitative evidence files. The operator does not calculate those values by hand.

---

# FORMAL RUN SET

```text
N = 8   → 4 runs
N = 16  → 4 runs
N = 32  → 4 runs
N = 64  → 4 runs

TOTAL = 16 runs
```

Use a fresh AI context and an independently selected hidden target for each run.

---

# ONE-LINE VERSION

> **Pick a C. The AI asks about P's. Answer YES/NO until it identifies your C. Then ask the same AI for the complete metadata + exact transcript + scorer-ready trace and save its generated output.**

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
