# AI Foundations | TEST_001 — Bounded Identification by Successive Distinctions

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source location:** https://philarchive.org/rec/NAUNOC-2  
**External source version / date:** PhilArchive Version 1 / 2025-09-10  
**Claims register:** `claims/CLAIMS_REGISTER.md` / 0.1.0  
**External Claim ID:** EXT-CLM-004  
**Protocol version:** 2.0.0  
**Date frozen:** 2026-08-22

---

## Test Question

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

This is the formal TEST_001 question.

The system is not given a decision tree or told which distinction to choose next. It must select its own successive questions from the available properties.

---

## Why the Answer Space Is Defined

The test is not a mind-reading task.

An unbounded instruction such as “discover what I am thinking of” does not provide a stable candidate universe, so elimination cannot be measured objectively and the relevance of a proposed distinction cannot be determined against a known search space.

TEST_001 therefore supplies an explicit candidate set before the target is selected.

---

## Relation to EXT-CLM-004

EXT-CLM-004 records the external claim that hierarchical recognition through successive differences can achieve a logarithmic search advantage relative to flat comparison when a usable hierarchy and discriminating property splits are available.

TEST_001 does **not** test the already-established mathematics of a prebuilt balanced tree.

It tests a dependency of the external recognition claim:

> **Can the system itself select useful successive distinctions, rather than being handed the efficient hierarchy in advance?**

A positive result supports this bounded dependency. It does not establish that all cognition uses the mechanism or that the complete cognitive architecture is logarithmic in every setting.

---

## Controlled Answer Space

The primary controlled candidate matrix is:

`protocol/TEST_001_CANDIDATES.csv`

It contains 64 candidates (`C01`–`C64`) and 10 binary properties (`P01`–`P10`).

The property names are intentionally opaque. Some properties produce strong partitions and some produce weaker partitions. The system must determine which available distinction is useful from the matrix itself.

Four candidate-space sizes are evaluated:

```text
N = 8   -> C01–C08
N = 16  -> C01–C16
N = 32  -> C01–C32
N = 64  -> C01–C64
```

The system sees the active candidate set and its property matrix. The target remains private until the run ends.

---

## Run Rule

For each run:

1. Present the active candidate matrix to the system.
2. The operator privately selects one target candidate from the active answer space.
3. Tell the system that exactly one candidate is the intended answer.
4. The system may ask successive **yes/no questions** about any listed property.
5. The operator answers only `YES` or `NO`, according to the hidden target row.
6. The system may not ask directly for the target candidate name or label.
7. The system may not ask the operator to describe or reveal the target.
8. The run ends when the system states one candidate as its answer.

Each question must test one listed property. Compound questions are not scored as valid distinctions.

The system is free to choose the order of properties and may state the answer as soon as it believes the target is uniquely identified.

---

## Primary Measures

At every valid question, preserve:

```text
R = candidates remaining before the question
YES_BRANCH = number of remaining candidates answering YES
NO_BRANCH = number of remaining candidates answering NO
WORST_CASE_REMAINDER = max(YES_BRANCH, NO_BRANCH)
GUARANTEED_ELIMINATION = 1 - WORST_CASE_REMAINDER / R
BEST_AVAILABLE_ELIMINATION = strongest guaranteed elimination available from any valid unused property at that state
DIVIDER_EFFICIENCY = GUARANTEED_ELIMINATION / BEST_AVAILABLE_ELIMINATION
ACTUAL_REMAINDER = candidates remaining after the operator's answer
```

`DIVIDER_EFFICIENCY = 1.0` means the system selected a best available divider at that state.

Also preserve:

- final identification accuracy;
- total valid questions;
- invalid or unscorable questions;
- candidate-space size `N`;
- theoretical binary lower bound `ceil(log2 N)`;
- question overhead above that lower bound.

---

## Scaling Question

Because the candidate spaces increase from 8 to 64, TEST_001 can measure whether question count remains close to the depth expected from strong successive elimination as the answer space grows.

The important observation is not merely that a logarithmic tree exists.

The observation is whether the **system's own selected distinctions** keep the candidate space contracting efficiently.

---

## Minimum Formal Run Set

Run at least four independently selected hidden targets at each candidate-space size:

```text
N = 8   : 4 runs
N = 16  : 4 runs
N = 32  : 4 runs
N = 64  : 4 runs
TOTAL   : 16 runs minimum
```

Use a fresh model context for each formal run unless a separate repeated-history condition is explicitly registered later.

The hidden target may be selected randomly or privately by the operator. Record the target after the run so the evidence is reproducible, but do not reveal it to the tested system before its final answer.

---

## Predeclared Outcome Space

```text
OUTCOME ∈ {SUPPORTED, MIXED, WEAKENED, UNRESOLVED}
```

**SUPPORTED** — across the formal run set, the system identifies every target correctly, mean divider efficiency is at least `0.90`, and mean question overhead is no more than `+1` above `ceil(log2 N)` at each tested `N`.

**MIXED** — the system shows a clear elimination advantage but does not meet all SUPPORT criteria, or performance is inconsistent across answer-space sizes.

**WEAKENED** — despite strong dividers being available, the system repeatedly selects weak or non-discriminating properties, fails to identify targets, or question growth loses the expected strong-elimination advantage.

**UNRESOLVED** — protocol failure, target leakage, invalid operator answers, missing evidence, or another confound prevents interpretation.

These thresholds are evaluator-defined operational criteria for TEST_001. They are not claims attributed to the external author.

---

## Controls and Confounds

The candidate matrix itself supplies the objective comparator: at each state the scorer can calculate the best divider actually available and compare the system's chosen divider against it.

The following do not qualify as support:

- giving the system the optimal property order;
- revealing the hidden target;
- allowing direct candidate-name queries;
- counting a prebuilt balanced traversal as autonomous divider selection;
- changing the candidate matrix after results are observed;
- scoring an ambiguous natural-language property that is not represented in the matrix;
- or treating successful identification alone as proof of efficient elimination.

---

## Evidence Files

Primary protocol assets:

- `protocol/PROTOCOL_001_EXT-CLM-004.md` — this frozen protocol;
- `protocol/TEST_001_CANDIDATES.csv` — controlled answer space;
- `protocol/TEST_001_RUN_TRACE_TEMPLATE.csv` — raw question/answer trace format;
- `protocol/score_test_001.py` — deterministic scorer;
- `claims/CLAIMS_REGISTER.md` — external claim record.

Formal run evidence belongs in `runs/`.

Results are synthesized only after formal runs are complete.

---

## Claim Ceiling

A positive TEST_001 result supports only the following bounded conclusion:

> **Within a defined identification problem containing measurable candidate distinctions, the tested intelligent system can autonomously select successive distinctions that preserve a strong elimination advantage and correctly identify the target.**

It does **not** establish:

- that every recognition problem has a clean defined answer space;
- that useful distinctions are always available;
- that the system can construct the candidate representation from an unbounded world;
- that all cognitive recognition is `O(log N)`;
- that biological cognition uses the same procedure;
- or that *Nature of Cognitive Computation* is supported as a whole.

---

## Protocol History

Protocol v1.0.0 was a preliminary scaling demonstration using prebuilt hierarchical partitions. It established the expected mathematical traversal behavior but did not test autonomous divider selection.

**Protocol v2.0.0 supersedes that design as formal TEST_001.** Existing v1.0.0 run/result artifacts remain historical preliminary evidence and must not be reported as results of this v2.0.0 test.

---

## External-Source Boundary

**AI Foundations conducted and authored this evaluation protocol. AI Foundations did not author the evaluated external source.**

External evaluation does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
