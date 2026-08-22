# AI Foundations | TEST_001 — Easy Run Sheet

**Claim:** EXT-CLM-004  
**Test:** TEST_001  
**Formal protocol:** `protocol/TEST_001.md`

---

# WHAT YOU DO

For one run:

**fresh AI chat → upload candidate file → secretly choose one candidate → paste the start prompt → answer YES/NO → save the finished interaction**

That is the whole run.

You do **not** calculate scores while the test is running.
You do **not** fill out branch sizes while the test is running.
You do **not** run Python while the test is running.

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

Write down the N you chose.

## 2. Open a fresh AI chat

Use a fresh context for every formal run.

Write down the model name/version if visible.

## 3. Upload this file

```text
protocol/TEST_001_CANDIDATES.csv
```

## 4. Secretly choose the target

Pick exactly one candidate from the active range.

Example:

```text
If N = 16, choose one candidate from C01–C16.
```

Write the target down somewhere private.

**Do not tell the tested AI which candidate you chose.**

---

# PASTE 1 — START THE RUN

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

# DURING THE RUN

The AI will ask something like:

```text
Is P04 YES for the hidden target?
```

Find your hidden target's row in `TEST_001_CANDIDATES.csv`.

If that row says `YES` for P04, reply:

```text
YES
```

If that row says `NO` for P04, reply:

```text
NO
```

**Reply with YES or NO only.**

Then answer the next property question the same way.

Keep going until the AI says:

```text
FINAL ANSWER: Cxx
```

The scored interaction ends immediately when the AI gives its final answer.

Do not correct it before saving the result.

---

# AFTER THE FINAL ANSWER

## 1. Record the result

Make a copy of:

```text
runs/TEST_001_OUTPUT_TEMPLATE.md
```

Rename it for the run, for example:

```text
RUN_001_TEST_001.md
```

Fill in:

```text
RUN ID
DATE
N
HIDDEN TARGET
MODEL
MODEL FINAL ANSWER
CORRECT: YES / NO
```

Then paste the complete scored interaction into that output file.

---

# PASTE 2 — GET A SIMPLE TRACE

Only after the AI has already given its final answer, paste this:

```text
The scored interaction is complete.

Return only a CSV trace of the property questions you asked during the scored interaction and the YES/NO answers I gave.

Use exactly this header:
step,property,answer

Example format:
1,P04,NO
2,P07,YES

Do not add, remove, repair, reinterpret, or reorder anything.
If you cannot recover the complete scored interaction exactly, write:
TRANSCRIPT ACCESS INCOMPLETE
```

Copy that trace into the run output file too.

The original visible chat remains the primary evidence.

---

# THAT IS ALL YOU DO FOR THE RUN

At this point, stop.

You have preserved:

```text
N
hidden target
model
exact start prompt
full scored interaction
model final answer
correct / incorrect
simple question trace
```

**Scoring happens afterward.**

The scoring step converts the simple trace into the quantitative measures required by `TEST_001.md`, including elimination, best available divider, divider efficiency, question count, and overhead.

You do not calculate those by hand.

---

# FORMAL RUN SET

The full formal evaluation requires:

```text
N = 8   → 4 runs
N = 16  → 4 runs
N = 32  → 4 runs
N = 64  → 4 runs

TOTAL = 16 runs
```

Use a fresh AI context for each run and choose a hidden target independently for each run.

---

# ONE-LINE VERSION

> **Upload the candidate matrix, secretly choose one candidate, paste PASTE 1, answer only YES/NO until the AI guesses, then save the interaction in the output sheet.**

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
