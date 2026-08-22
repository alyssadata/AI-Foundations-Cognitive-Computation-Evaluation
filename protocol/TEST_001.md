# AI Foundations | TEST_001 — Bounded Identification by Successive Distinctions

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**External source:** PhilArchive Version 1 / NAUNOC-2 / 2025-09-10  
**External Claim ID:** EXT-CLM-004  
**Protocol version:** 2.0.0  
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

It contains 64 candidates (`C01`–`C64`) and 10 binary properties (`P01`–`P10`).

The property names are intentionally opaque. Some properties divide the remaining candidates strongly; others divide them weakly.

The tested system sees the active candidate matrix. The target remains hidden.

Formal candidate-space sizes:

```text
N = 8   -> C01–C08
N = 16  -> C01–C16
N = 32  -> C01–C32
N = 64  -> C01–C64
```

The bounded answer space is necessary because elimination cannot be measured objectively when the possible answer could be anything.

---

## Run Rules

For each run:

1. Give the tested system the active candidate matrix.
2. The operator privately selects exactly one target candidate from that matrix.
3. The system may ask successive **yes/no questions** about any listed property.
4. The operator answers only `YES` or `NO` according to the hidden target row.
5. The system may not ask directly for the target candidate name or label.
6. The system may not ask the operator to describe or reveal the target.
7. Each scored question must test one listed property.
8. The run ends when the system states one candidate as its answer.

The system may choose the properties in any order and may answer as soon as it believes one candidate remains.

---

## What Is Measured

At every valid question, record:

```text
candidates remaining before the question
YES branch size
NO branch size
guaranteed elimination from the chosen property
best available guaranteed elimination at that state
divider efficiency
candidates remaining after the actual YES/NO answer
```

Divider efficiency compares the system's chosen distinction with the strongest available distinction at that exact state.

`1.0` means the system chose a best available divider.

Also record:

- correct / incorrect final identification;
- total valid questions;
- invalid or unscorable questions;
- candidate-space size `N`;
- `ceil(log2 N)` as the binary lower bound;
- question overhead above that lower bound.

The deterministic scorer is:

`protocol/score_test_001.py`

The run trace format is:

`protocol/TEST_001_RUN_TRACE_TEMPLATE.csv`

---

## Minimum Formal Run Set

Run four independently selected hidden targets at each size:

```text
N = 8   : 4 runs
N = 16  : 4 runs
N = 32  : 4 runs
N = 64  : 4 runs
TOTAL   : 16 runs minimum
```

Use a fresh model context for each formal run.

Record the hidden target after the run, never before the tested system gives its final answer.

---

## Outcome Rule

```text
OUTCOME ∈ {SUPPORTED, MIXED, WEAKENED, UNRESOLVED}
```

**SUPPORTED** — every target is identified correctly, mean divider efficiency is at least `0.90`, and mean question overhead is no more than `+1` above `ceil(log2 N)` at each tested `N`.

**MIXED** — the system shows a clear elimination advantage but does not meet all support criteria, or performance is inconsistent across answer-space sizes.

**WEAKENED** — strong dividers are available but the system repeatedly chooses weak or non-discriminating distinctions, fails to identify targets, or loses the expected strong-elimination advantage as `N` grows.

**UNRESOLVED** — target leakage, invalid operator answers, missing evidence, protocol failure, or another confound prevents interpretation.

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

## Files Used by TEST_001

```text
claims/CLAIMS_REGISTER.md
protocol/TEST_001.md
protocol/TEST_001_CANDIDATES.csv
protocol/TEST_001_RUN_TRACE_TEMPLATE.csv
protocol/score_test_001.py
```

Formal evidence goes into `runs/` when the test is actually run. Results go into `results/` only after formal evidence exists.

---

## External-Source Boundary

**AI Foundations conducted and authored this evaluation protocol. AI Foundations did not author the evaluated external source.**

External evaluation does not incorporate the source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
