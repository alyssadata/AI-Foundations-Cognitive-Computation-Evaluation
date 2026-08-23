# AI Foundations | TEST_001 — Bounded Identification by Successive Distinctions

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**External source:** PhilArchive Version 1 / NAUNOC-2 / 2025-09-10  
**External Claim ID:** EXT-CLM-004  
**Protocol version:** 2.2.0  
**Date frozen:** 2026-08-22

---

## Test Question

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

That is TEST_001.

The system is **not** given a decision tree or told which distinction to choose next. It must choose its own successive questions.

---

## What This Tests

EXT-CLM-004 claims that difference-based hierarchical recognition can gain a logarithmic search advantage when useful successive distinctions are available.

TEST_001 does **not** test whether a prebuilt balanced tree has logarithmic depth. That mathematics is already established.

TEST_001 tests the live dependency:

> **Can the system itself choose useful successive distinctions inside a defined identification problem?**

---

## Defined Answer Space

The controlled answer space is:

`protocol/TEST_001_CANDIDATES.csv`

It contains 64 candidates (`C01`–`C64`) and 12 binary properties (`P01`–`P12`).

The property names are intentionally opaque. The tested system sees the active candidate rows and the active property set for the selected condition. The target remains hidden.

Formal conditions:

```text
N = 8
Candidates: C01–C08
Active P's: P01, P03, P04, P07, P08, P10
Active-property count: 6
Binary minimum: 3
Additional choices: 3

N = 16
Candidates: C01–C16
Active P's: P01, P02, P03, P04, P06, P07, P08, P10
Active-property count: 8
Binary minimum: 4
Additional choices: 4

N = 32
Candidates: C01–C32
Active P's: P01, P02, P03, P04, P06, P07, P08, P09, P10, P11
Active-property count: 10
Binary minimum: 5
Additional choices: 5

N = 64
Candidates: C01–C64
Active P's: P01–P12
Active-property count: 12
Binary minimum: 6
Additional choices: 6
```

### Why TEST_001 Uses N = 8, 16, 32, and 64

The specific values `8`, `16`, `32`, and `64` are **AI Foundations evaluation-design choices**. They are not values specified by Naumenko.

The external paper supplies the scaling claim: hierarchical difference-based recognition is described as a binary-search-like process in which useful successive distinctions can reduce recognition from `O(N)` toward `O(log N)`. The paper also uses a much larger illustrative case of roughly one million categories and approximately twenty binary comparisons.

TEST_001 uses smaller powers of two so that the scaling behavior can be measured cleanly and repeatedly under controlled conditions.

```text
N = 8   → binary lower bound = 3 questions
N = 16  → binary lower bound = 4 questions
N = 32  → binary lower bound = 5 questions
N = 64  → binary lower bound = 6 questions
```

Each condition exactly doubles the candidate space. Under ideal binary division, each doubling should require only **one additional question**. This creates a simple scaling ladder rather than a single easy/hard comparison.

The four conditions serve different experimental roles:

- `N = 8` establishes the small-space floor: can the system perform the task when the answer space is minimal but still requires successive distinctions?
- `N = 16` and `N = 32` provide intermediate scaling points, allowing degradation or improvement to be located rather than observed only at the endpoints.
- `N = 64` is the largest formal condition in TEST_001: large enough to require six ideal binary distinctions and meaningful property selection, while still remaining practical for repeated controlled runs and exact scoring.

The purpose of using four powers of two is therefore **not** to reproduce a number stated in the paper. It is to operationalize the paper's scaling claim in a controlled test where candidate-space growth and binary lower bounds are explicit.

### Property-Count Control

For each condition:

```text
active property count = 2 × log2(N)
```

Because all tested `N` values are powers of two, each condition contains the minimum number of discriminating dimensions needed for unique identification **plus the same number of additional property choices**.

This preserves a **1:1 ratio between necessary discriminating capacity and additional available choices** as the candidate space grows.

The active matrix is constructed so every candidate in each condition remains uniquely identifiable from that condition's active properties.

---

## Run Numbering Across Models

Within `TEST_001`, the run number identifies the candidate-space condition:

```text
RUN_001 → N = 8
RUN_002 → N = 16
RUN_003 → N = 32
RUN_004 → N = 64
```

Every tested model uses the same run number for the same `N` condition. The model tag makes each complete run identity unique.

Examples:

```text
RUN_001_N08_GPT56SOL
RUN_001_N08_<OTHER_MODEL_TAG>
RUN_002_N16_GPT56SOL
RUN_003_N32_GPT56SOL
RUN_004_N64_GPT56SOL
```

Therefore, `RUN_001` groups all formal `N = 8` model runs under TEST_001; `RUN_002` groups all `N = 16` model runs; `RUN_003` groups all `N = 32` model runs; and `RUN_004` groups all `N = 64` model runs.

The run number is **not** a replicate number.

---

## Run Rules

For each run:

1. Give the tested system the candidate matrix.
2. State the active candidate range and active P set for the selected `N`.
3. The operator privately selects exactly one target candidate from the active range.
4. The system may ask successive **yes/no questions** about the active P's only.
5. The operator answers only `YES` or `NO` according to the hidden target row.
6. The system may not ask directly for the target candidate name or label.
7. The system may not ask the operator to describe or reveal the target.
8. Each scored question must test exactly one active property.
9. The run ends when the system states one candidate as its final answer.

The system may choose the active properties in any order and may answer as soon as it believes one candidate remains.

The operator-facing execution instructions and exact copy/paste blocks are in:

`protocol/TEST_001_EASY_RUN_SHEET.md`

---

## What Is Measured

At every valid question, record:

```text
candidates remaining before the question
YES branch size
NO branch size
guaranteed elimination from the chosen property
best available guaranteed elimination among the still-unused ACTIVE properties
divider efficiency
candidates remaining after the actual YES/NO answer
```

Divider efficiency compares the system's chosen distinction with the strongest still-unused **active** distinction available at that exact state.

`1.0` means the system chose a best available divider.

Also record:

- correct / incorrect final identification;
- total valid questions;
- invalid or unscorable questions;
- candidate-space size `N`;
- `ceil(log2 N)` as the binary lower bound;
- question overhead above that lower bound.

The deterministic scorer is `protocol/score_test_001.py`.

The scorer-input trace schema is `protocol/TEST_001_RUN_TRACE_TEMPLATE.csv`.

The AI-generated archival output schema is `runs/TEST_001_OUTPUT_TEMPLATE.md`.

---

## Formal Run Set

For **each tested model**:

```text
RUN_001 → N = 8   : 1 formal run
RUN_002 → N = 16  : 1 formal run
RUN_003 → N = 32  : 1 formal run
RUN_004 → N = 64  : 1 formal run
TOTAL              : 4 formal runs per model
```

Across models, runs with the same run number use the same `N` condition and remain distinct through the model tag in the complete `RUN_ID`.

Use a fresh model context for each formal run.

The true hidden target is supplied to the tested system only after its scored final answer, when the post-run archival output is requested.

---

## Outcome Rule

```text
OUTCOME ∈ {SUPPORTED, MIXED, WEAKENED, UNRESOLVED}
```

**SUPPORTED** — every formal model-condition run identifies its target correctly, mean divider efficiency is at least `0.90`, and mean question overhead is no more than `+1` above `ceil(log2 N)` at each tested `N`.

**MIXED** — the tested systems show a clear elimination advantage but do not meet all support criteria, or performance is inconsistent across answer-space sizes or models.

**WEAKENED** — strong active dividers are available but tested systems repeatedly choose weak or non-discriminating distinctions, fail to identify targets, or lose the expected strong-elimination advantage as `N` grows.

**UNRESOLVED** — target leakage, invalid operator answers, use of inactive properties, missing evidence, protocol failure, or another confound prevents interpretation.

These thresholds are AI Foundations evaluation criteria. They are not claims attributed to Naumenko.

---

## Claim Ceiling

A positive result supports only:

> **Within a defined identification problem containing measurable candidate distinctions, the tested intelligent system can autonomously select successive distinctions that preserve a strong elimination advantage and correctly identify the target.**

It does **not** establish that:

- every recognition problem has a clean defined answer space;
- useful distinctions are always available;
- an intelligent system can construct the candidate representation from an unbounded world;
- all cognitive recognition is `O(log N)`;
- biological cognition uses this procedure;
- or *Nature of Cognitive Computation* is supported as a whole.

---

## External-Source Boundary

**AI Foundations conducted and authored this evaluation protocol. AI Foundations did not author the evaluated external source.**

External evaluation does not incorporate the source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
