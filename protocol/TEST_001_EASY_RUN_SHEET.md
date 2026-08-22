# AI Foundations | TEST_001 — Easy Run Sheet

**Claim:** EXT-CLM-004  
**Test:** TEST_001  
**Formal protocol:** `protocol/TEST_001.md` v2.1.0

---

# WHAT YOU DO

**I pick a C.**  
**The AI asks from P.**  
**I answer YES/NO until it identifies my C.**

That is the test.

You do **not** calculate scores during the run.  
You do **not** fill out an output sheet.  
After the AI gives its final answer, the same AI generates the metadata, transcript, and scorer-ready trace for the run.

---

# 1. CHOOSE THE RUN SIZE

Use the matching input file:

```text
N = 8  → protocol/TEST_001_INPUT_N08.csv
N = 16 → protocol/TEST_001_INPUT_N16.csv
N = 32 → protocol/TEST_001_INPUT_N32.csv
N = 64 → protocol/TEST_001_INPUT_N64.csv
```

Each file already contains **only the C's and P's active for that condition**.

You do not need to decide how many P's belong in the run. The input file already does that.

---

# 2. OPEN A FRESH AI CHAT

Use a fresh context for every formal run.

Upload **one** matching TEST_001 input CSV from the list above.

---

# 3. PICK A C

Secretly choose exactly one `C` from the uploaded file.

Example:

```text
C11
```

Do not tell the AI which C you picked.

Keep the uploaded CSV open so you can read the YES/NO values from your chosen C row.

---

# 4. PASTE 1 — START THE SCORED RUN

Paste this exactly:

```text
You are participating in TEST_001.

The attached CSV is the complete active candidate/property matrix for this run. Exactly one candidate in that file has been privately selected as the hidden target.

Your task is to identify the hidden target.

Rules:
- Ask one YES/NO question at a time.
- Each question must ask about exactly one P property column present in the attached file.
- You choose which P to ask next.
- Do not ask directly for the candidate name or label.
- Do not ask me to describe or reveal the target.
- Do not use compound questions.
- Continue until you are ready to identify one candidate.
- When ready, state exactly: FINAL ANSWER: Cxx

Begin with your first P question only.
```

---

# 5. ANSWER THE P QUESTIONS

The AI will ask something like:

```text
Is P04 YES for the hidden target?
```

Go to **your chosen C row** and find `P04`.

If it says YES, reply only:

```text
YES
```

If it says NO, reply only:

```text
NO
```

Then it asks another P.

Keep answering from the **same C row** until the AI says:

```text
FINAL ANSWER: Cxx
```

**The scored interaction ends at the FINAL ANSWER.**

Do not correct the AI before that answer is recorded.

---

# 6. PASTE 2 — GENERATE THE RUN OUTPUT

After the AI has already given its FINAL ANSWER, replace `[RUN_ID]` and `[TRUE_TARGET]` below and paste it into the **same chat**:

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
INPUT_FILE:

## 2. Exact Start Prompt
Reproduce the exact PASTE 1 prompt used for this run.

## 3. Verbatim Scored Interaction
Reproduce the scored interaction exactly from your first P question through your FINAL ANSWER line.

## 4. Final Identification
MODEL_FINAL_ANSWER:
CORRECT_IDENTIFICATION: YES / NO

## 5. Scorer-Ready Trace
Return a CSV code block using exactly this header:
run_id,candidate_space_n,target,step,property,answer

Include one row for each scored P question, in chronological order. Use the RUN_ID and true hidden target supplied above.

## 6. Deviations / Missing Data
TARGET_LEAKED_BEFORE_FINAL_ANSWER: YES / NO / UNKNOWN
NON_YES_NO_OPERATOR_RESPONSE_DURING_SCORED_RUN: YES / NO / UNKNOWN
INVALID_OR_COMPOUND_MODEL_QUESTION: YES / NO / UNKNOWN
INACTIVE_PROPERTY_USED: YES / NO / UNKNOWN
INTERRUPTION_OR_TOOL_FAILURE: YES / NO / UNKNOWN
TRANSCRIPT_ACCESS: COMPLETE / INCOMPLETE
OTHER_DEVIATION:

## 7. Scoring Status
SCORING_STATUS: PENDING

## 8. Archival Integrity Note
State whether the metadata, exact start prompt, scored transcript, final answer, and scorer-ready trace above were recovered completely from the current conversation. Do not claim completeness if any part is unavailable.
```

The AI's response to PASTE 2 is the run record.

Save it as, for example:

```text
runs/RUN_001_TEST_001.md
```

---

# 7. SCORE AFTERWARD

Save Section 5 of the generated run output as, for example:

```text
runs/RUN_001_TEST_001_TRACE.csv
```

Then run:

```text
python protocol/score_test_001.py protocol/TEST_001_CANDIDATES.csv runs/RUN_001_TEST_001_TRACE.csv
```

The scorer does the math. The operator does not.

---

# FORMAL RUN SET

```text
N = 8  → 4 runs
N = 16 → 4 runs
N = 32 → 4 runs
N = 64 → 4 runs

TOTAL = 16 runs
```

Use a fresh AI context and independently selected hidden C for every run.

---

# ONE-LINE VERSION

> **Pick the N file. Pick a C. The AI asks from the P columns in that file. Answer YES/NO until it identifies your C. Then ask it to generate the run record.**

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
