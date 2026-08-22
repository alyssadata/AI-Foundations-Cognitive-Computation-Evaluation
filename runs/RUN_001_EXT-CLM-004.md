# AI Foundations | Run 001 — EXT-CLM-004

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source version / identifier:** PhilArchive Version 1 / NAUNOC-2 / 2025-09-10  
**Claim / test ID:** EXT-CLM-004 / TEST_001  
**Run ID:** RUN_001  
**Date:** 2026-08-22

---

## 1. External Source / Claim Identity

```text
EXTERNAL SOURCE TITLE: Nature of Cognitive Computation
EXTERNAL AUTHOR / CREATOR: Oleksandr Naumenko
SOURCE LOCATION: https://philarchive.org/rec/NAUNOC-2
SOURCE VERSION / DATE / IDENTIFIER: PhilArchive Version 1 / 2025-09-10 / NAUNOC-2
MATERIAL UNDER EVALUATION: Hints from 20 Questions, especially p.19 recognition-scaling claim
CLAIM_ID: EXT-CLM-004
CLAIM TEXT / PREDECLARED PROPOSITION: Hierarchical difference-based recognition can achieve O(log N) search rather than O(N) flat comparison under the registered comparison.
CLAIMS_REGISTER_VERSION: 0.1.0
PROTOCOL: protocol/PROTOCOL_001_EXT-CLM-004.md
PROTOCOL_VERSION: 1.0.0
```

The external source identity remains separate from the AI Foundations evaluation identity.

---

## 2. Run Metadata

```text
RUN_ID: RUN_001
DATE_TIME: 2026-08-22, execution during evaluation session
MODEL / SYSTEM / SOFTWARE VERSION: Python 3.13.5
INTERFACE / PRODUCT / ENVIRONMENT: isolated Python execution environment
CONDITION / ARM: flat sequential; balanced 50/50; approximately 75/25; pathological 1-vs-rest
MEMORY OR PRIOR HISTORY: not applicable
TOOLS / FILE ACCESS: local Python standard library
SYSTEM / DEVELOPER INSTRUCTIONS AVAILABLE: not applicable to benchmark logic
SAMPLING SETTINGS IF AVAILABLE: deterministic; no sampling
INPUT / STIMULUS NAME: fixed candidate-space sizes
INPUT / STIMULUS ID OR HASH: N = 16, 256, 4096, 65536, 1048576
CODE FILE: protocol/test_001_hierarchical_search.py
CODE COMMIT: 24313de0b67f70d57072fb9efb0f39212aacfc39
TRANSCRIPT / RAW OUTPUT PRESERVED: yes — runs/RUN_001_EXT-CLM-004.csv
```

---

## 3. Final Evaluation Outcome

```text
FINAL OUTCOME: SUPPORTED_CONDITIONALLY
```

Allowed values from the frozen protocol:

```text
SUPPORTED_CONDITIONALLY / WEAKENED / UNRESOLVED
```

---

## 4. Measures

| N | Flat worst-case comparisons | Balanced 50/50 depth | 75/25 worst depth | 1-vs-rest worst depth | Flat / balanced ratio |
|---:|---:|---:|---:|---:|---:|
| 16 | 16 | 4 | 9 | 15 | 4.0 |
| 256 | 256 | 8 | 19 | 255 | 32.0 |
| 4,096 | 4,096 | 12 | 29 | 4,095 | 341.33 |
| 65,536 | 65,536 | 16 | 39 | 65,535 | 4,096.0 |
| 1,048,576 | 1,048,576 | 20 | 48 | 1,048,575 | 52,428.8 |

The balanced hierarchy matched `log2(N)` exactly at every tested scale.

The flat worst-case comparator matched `N` exactly at every tested scale.

The ratio between flat worst-case comparisons and balanced hierarchical depth increased sharply with candidate-space size, satisfying the frozen decision rule.

---

## 5. Comparator / Stress-Condition Record

```text
BASELINE / CONTROL: flat sequential candidate comparison
PRIMARY HIERARCHICAL CONDITION: balanced 50/50 binary hierarchy
STRESS CONDITION 1: approximately 75/25 hierarchy, larger branch followed
STRESS CONDITION 2: pathological 1-vs-rest hierarchy, remainder branch followed
MATCHED VARIABLE: candidate-space size N
DIFFERING VARIABLE: amount of candidate-space elimination produced by each successive distinction
```

### Observed structural dependency

A hierarchy by itself did not guarantee the strongest efficiency result.

The approximately 75/25 condition still reduced the search space by a constant fraction and therefore remained dramatically shallower than flat search, though with a larger constant factor than the balanced condition.

The pathological 1-vs-rest condition approached the flat linear case because each distinction removed only one candidate. At `N = 1,048,576`, its worst-case depth was `1,048,575` rather than `20`.

This is consistent with the source’s statement that useful questions should divide the remaining categories substantially, preferably roughly in half. It does not contradict EXT-CLM-004; it exposes a dependency required for the claimed advantage.

---

## 6. Divider-Selection / Construction Boundary

The run did **not** identify or test a source-specified algorithm for discovering the hierarchy or selecting the next distinction.

The evaluated source describes desirable properties of successive questions — including clear boundaries, dependence on prior answers, and roughly balanced partitioning — but this first protocol does not have a sufficiently precise source algorithm whose selection cost can be counted without adding evaluator-authored mechanism.

Therefore:

```text
RECOGNITION-TRAVERSAL CLAIM: supported conditionally
DIVIDER-SELECTION MECHANISM: unresolved by this run
HIERARCHY-CONSTRUCTION COST: unresolved by this run
TOTAL COGNITIVE COMPUTATIONAL COST: unresolved by this run
```

This boundary is part of the result, not a protocol failure.

---

## 7. Exceptions, Deviations, or Missing Data

```text
PROTOCOL DEVIATION: NO
DESCRIPTION: none
MISSING DATA: no source-specified divider-selection or hierarchy-construction cost model exists in operational form for this run
INTERRUPTION / TOOL FAILURE: no
SOURCE VERSION UNCERTAINTY: no for the public PhilArchive identity used here; the evaluation text remains the preserved extracted copy recorded in source/EXTERNAL_SOURCE.md
OTHER NOTES: the benchmark tests operation-count scaling, not measured biological or model runtime
```

---

## 8. Raw Output

Primary raw output is preserved in:

`runs/RUN_001_EXT-CLM-004.csv`

The output records Python version, candidate-space size, flat worst-case comparisons, flat expected comparisons, balanced depth, moderate-imbalance depth, pathological depth, and the flat-to-balanced ratio.

---

## 9. Evidence Files

```text
EXTERNAL SOURCE RECORD: source/EXTERNAL_SOURCE.md
SOURCE LOCATION: https://philarchive.org/rec/NAUNOC-2
CLAIMS REGISTER: claims/CLAIMS_REGISTER.md
PROTOCOL: protocol/PROTOCOL_001_EXT-CLM-004.md
CODE: protocol/test_001_hierarchical_search.py
CODE COMMIT: 24313de0b67f70d57072fb9efb0f39212aacfc39
RAW OUTPUT: runs/RUN_001_EXT-CLM-004.csv
RAW OUTPUT COMMIT: dc7cd7f7dbe7175c678bd5f1596654dfa1330df9
```

---

## 10. Claim Boundary

This run supports the following claim ceiling:

> **Given an available hierarchy whose successive distinctions substantially reduce the remaining candidate space, hierarchical recognition can produce the logarithmic traversal advantage described in EXT-CLM-004 relative to the specified flat sequential comparator.**

This run does **not** establish:

- how the system discovers the hierarchy;
- how the system identifies a useful next distinction;
- the computational cost of selecting that distinction;
- that the total cognitive process remains O(log N) once those costs are included;
- that biological cognition actually implements the tested data structure;
- that every similarity-based recognition system must inspect all N categories;
- or that the external theory as a whole is supported.

---

## 11. External-Source Boundary

**AI Foundations conducted this evaluation. AI Foundations did not author the evaluated external source.**

The external source remains external to AI Foundations.

A conditional supporting result does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

---

## 12. Completion Check

```text
[x] External source / author / location recorded
[x] Source version / identifier recorded
[x] Exact claim / material under evaluation recorded
[x] Required metadata recorded
[x] Exact frozen-protocol outcome used
[x] Measures recorded
[x] Comparator and stress conditions preserved
[x] Deviations preserved
[x] Primary raw evidence saved
[x] Code preserved
[x] Claim ceiling preserved
[x] External-source boundary preserved
```

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
