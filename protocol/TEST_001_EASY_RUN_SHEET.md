# AI Foundations | TEST_001 — Easy Run Sheet

**Claim:** EXT-CLM-004  
**Test:** TEST_001  
**Formal protocol:** `protocol/TEST_001.md` v2.2.0

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

# 1. CHOOSE THE RUN / N CONDITION

Within TEST_001, the run number identifies the N condition:

```text
RUN_001 → N = 8  → protocol/TEST_001_INPUT_N08.csv
RUN_002 → N = 16 → protocol/TEST_001_INPUT_N16.csv
RUN_003 → N = 32 → protocol/TEST_001_INPUT_N32.csv
RUN_004 → N = 64 → protocol/TEST_001_INPUT_N64.csv
```

Each file already contains **only the C's and P's active for that condition**.

You do not need to decide how many P's belong in the run. The input file already does that.

---

# 2. NAME THE MODEL RUN

Every tested model uses the same RUN number for the same N condition. Add the model tag so the complete RUN_ID is unique.

Format:

```text
RUN_<condition-number>_N<condition>_<MODEL_TAG>
```

Examples:

```text
RUN_001_N08_GPT56SOL
RUN_001_N08_<OTHER_MODEL_TAG>
RUN_002_N16_GPT56SOL
RUN_003_N32_GPT56SOL
RUN_004_N64_GPT56SOL
```

`RUN_001` always means the `N = 8` condition under TEST_001.  
`RUN_002` always means `N = 16`.  
`RUN_003` always means `N = 32`.  
`RUN_004` always means `N = 64`.

The RUN number is **not** a replicate number.

Use a short stable model tag with no spaces. Do not reuse the same complete RUN_ID for two scored interactions.

---

# 3. OPEN A FRESH AI CHAT

Use a fresh context for every formal run.

Upload **one** matching TEST_001 input CSV from the list above.

---

# 4. PICK A C

Secretly choose exactly one `C` from the uploaded file.

Example:

```text
C11
```

Do not tell the AI which C you picked.

Keep the uploaded CSV open so you can read the YES/NO values from your chosen C row.

---

# 5. PASTE 1 — START THE SCORED RUN

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

# 6. ANSWER THE P QUESTIONS

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

# 7. PASTE 2 — GENERATE THE RUN OUTPUT

After the AI has already given its FINAL ANSWER, replace `[RUN_ID]` and `[TRUE_TARGET]` below and paste it into the **same chat**.

Use the complete model-aware RUN_ID from Step 2, for example `RUN_001_N08_GPT56SOL`.

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
run_id,candidate_space_n,target,final_answer,step,property,answer

Include one row for each scored P question, in chronological order. Use the RUN_ID, true hidden target, and model final answer recorded above.

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

Save it using the complete RUN_ID, for example:

```text
runs/RUN_001_N08_GPT56SOL_TEST_001.md
```

---

# 8. SCORE AFTERWARD

Save Section 5 of the generated run output using the same RUN_ID, for example:

```text
runs/RUN_001_N08_GPT56SOL_TEST_001_TRACE.csv
```

Then run:

```text
python protocol/score_test_001.py protocol/TEST_001_CANDIDATES.csv runs/RUN_001_N08_GPT56SOL_TEST_001_TRACE.csv
```

The scorer does the math. The operator does not.

---

# FORMAL RUN SET

For each tested model:

```text
RUN_001 → N = 8   → 1 formal run
RUN_002 → N = 16  → 1 formal run
RUN_003 → N = 32  → 1 formal run
RUN_004 → N = 64  → 1 formal run

TOTAL = 4 formal runs per model
```

Across models, all `RUN_001` runs are N08, all `RUN_002` runs are N16, all `RUN_003` runs are N32, and all `RUN_004` runs are N64. The model tag keeps each complete run identity distinct.

Use a fresh AI context and independently selected hidden C for every model-condition run.

---

# ONE-LINE VERSION

> **Pick the run/N file. Pick a C. The AI asks from the P columns in that file. Answer YES/NO until it identifies your C. Then ask it to generate the model-tagged run record.**

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
