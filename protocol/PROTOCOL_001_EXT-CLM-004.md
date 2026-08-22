# AI Foundations | Protocol 001 — Hierarchical Recognition Scaling

**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source location:** https://philarchive.org/rec/NAUNOC-2  
**External source version / date:** PhilArchive Version 1 / 2025-09-10  
**Claims register:** `claims/CLAIMS_REGISTER.md` / 0.1.0  
**Protocol version:** 1.0.0  
**Date frozen:** 2026-08-22

---

## 1. External-Source Boundary

This protocol evaluates an independently authored external source.

**AI Foundations is the evaluator, not the source or author of the evaluated work.**

The external source remains external to AI Foundations. Evaluation does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

---

## 2. Claims-Register Prerequisite

**External Claim ID:** EXT-CLM-004  
**Claim label:** Hierarchical recognition has logarithmic search advantage  
**Claim source status:** EXPLICIT  
**Claim source location:** *Nature of Cognitive Computation*, “Hints from 20 Questions,” p.19

The registered claim states that recognition through a hierarchy defined by differences between sibling categories can scale as `O(log N)`, contrasted with an `O(N)` flat comparison account. The paper illustrates the distinction with one million categories and up to about twenty hierarchical comparisons.

This protocol does not strengthen that claim into a claim that cognition always finds the mathematically optimal divider.

---

## 3. Evaluation Target

This protocol evaluates the **recognition-time scaling claim** in EXT-CLM-004.

The primary question is:

> **When the same candidate space is searched either by flat sequential comparison or by successive hierarchical distinctions, does the hierarchical condition exhibit the claimed logarithmic reduction in recognition steps?**

The protocol also records a structural dependency that is relevant to interpretation: logarithmic traversal requires the hierarchy to reduce the remaining candidate space by a substantial fraction at successive steps.

### Variables

```text
N = number of candidate categories
FLAT COMPARISON = one candidate checked against the target
HIERARCHICAL DISTINCTION = one branch decision that reduces the remaining candidate set
BALANCED CONDITION = approximately 50/50 split at each level
MODERATELY IMBALANCED CONDITION = approximately 75/25 split at each level
PATHOLOGICAL CONDITION = one candidate removed at each level, with the remainder retained
RECOGNITION COST = number of comparisons/distinctions needed to reach one candidate
```

### Scope boundary

This first protocol evaluates **traversal / recognition cost once a hierarchy and its distinctions are available**.

It does **not** treat the cost of discovering, learning, constructing, maintaining, or selecting the hierarchy as zero in the theory as a whole. Those costs are simply not operationalized here because the external source does not specify a sufficiently precise divider-selection or hierarchy-construction algorithm for this protocol to test without inventing one.

That unresolved mechanism cost must therefore remain visible in the claim ceiling.

---

## 4. Testable Prediction

```text
EXTERNAL CLAIM ID: EXT-CLM-004
EXTERNAL CLAIM: Hierarchical difference-based recognition can achieve O(log N) search rather than O(N) flat comparison.

OPERATIONALIZATION:
Compare recognition-step counts across increasing candidate spaces N = 2^k.
Use a flat sequential scan as the O(N) comparator.
Use a pre-existing balanced binary hierarchy as the primary hierarchical condition.
Record moderately imbalanced and pathological hierarchies as structural stress conditions.

PREDICTED OBSERVATION:
For the balanced hierarchy, worst-case hierarchical depth increases by one step when N doubles and equals log2(N) for the tested powers of two, while flat worst-case comparisons increase in direct proportion to N.

OBSERVATION THAT WOULD WEAKEN THE CLAIM:
Under the stated balanced-hierarchy condition, hierarchical recognition requires comparison counts that scale approximately linearly with N or otherwise fails to show the claimed search reduction.

UNRESOLVED CONDITION:
The recognition-time advantage is observed, but the source does not provide enough mechanism to determine whether discovering/selecting/maintaining the required distinctions preserves the same total computational advantage in a cognitive system.
```

---

## 5. Status / Outcome Space

```text
OUTCOME ∈ {SUPPORTED_CONDITIONALLY, WEAKENED, UNRESOLVED}
```

**SUPPORTED_CONDITIONALLY** — the registered recognition-time scaling holds under the hierarchy condition actually described, while untested construction/selection costs remain outside the claim ceiling.

**WEAKENED** — the balanced hierarchical condition fails to produce the claimed recognition-step scaling under matched candidate-space conditions.

**UNRESOLVED** — the protocol cannot isolate the registered claim from an unmodeled dependency or implementation artifact.

---

## 6. Required Run Record

```text
RUN_ID:
DATE_TIME:
EXTERNAL_SOURCE_ID / VERSION:
CLAIM_ID: EXT-CLM-004
CLAIMS_REGISTER_VERSION: 0.1.0
PROTOCOL_VERSION: 1.0.0
SOFTWARE VERSION:
ENVIRONMENT:
INPUT SIZES:
CODE FILE / VERSION:
RAW OUTPUT PRESERVED: yes/no
FINAL OUTCOME:
NOTES:
```

---

## 7. Entry Condition

Before execution:

1. this protocol must be committed and frozen;
2. the code must implement the conditions below without changing the decision rule;
3. candidate-space sizes must be fixed at `N = 16, 256, 4096, 65536, 1048576`;
4. the flat and hierarchical conditions must use the same `N` at each scale;
5. result interpretation must remain bounded to recognition-step complexity.

---

## 8. Execution Phases

### Phase A — Flat sequential comparator

**Purpose:** Measure the linear-search baseline used in the registered claim.

**Procedure:** For each `N`, place the target at the final candidate position and sequentially inspect candidates until the target is found. Record the actual comparison count. Also record the exact expected comparison count for a uniformly distributed target as `(N + 1) / 2`.

### Phase B — Balanced hierarchy

**Purpose:** Test the source’s hierarchical-recognition scaling under approximately ideal binary partitioning.

**Procedure:** For each `N = 2^k`, begin with `N` remaining candidates. At each hierarchical distinction, retain one half of the remaining candidates. Continue until one candidate remains. Record the number of distinctions.

### Phase C — Partition-quality stress conditions

**Purpose:** Expose whether the efficiency result depends on the elimination strength of successive distinctions.

**Procedure:** Repeat worst-case traversal counts for:

- an approximately 75/25 hierarchy, always following the larger branch; and
- a pathological 1-vs-rest hierarchy, always following the remainder branch.

These conditions are diagnostic. They do not redefine the external claim.

### Phase D — Boundary record

**Purpose:** Prevent traversal efficiency from being silently treated as proof of a complete cognitive mechanism.

**Procedure:** Record whether the evaluated source supplies an operational rule whose computational cost can be counted for discovering/selecting the successive distinctions used by the hierarchy.

If no sufficiently precise rule is available, record that dependency as unresolved rather than inventing a rule for the source.

---

## 9. Decision Rule

Assign **SUPPORTED_CONDITIONALLY** if all of the following hold:

1. balanced hierarchical worst-case depth equals `log2(N)` at every tested `N`;
2. flat worst-case comparisons equal `N` at every tested `N`;
3. the ratio between flat worst-case comparisons and balanced hierarchical depth increases as `N` increases;
4. no protocol deviation invalidates the comparison.

Assign **WEAKENED** if the balanced hierarchy does not exhibit the predicted scaling under the frozen setup.

Assign **UNRESOLVED** if implementation or protocol conditions prevent the scaling comparison from being interpreted.

The unresolved cost of discovering/selecting/constructing the hierarchy does **not** convert a successful traversal result into failure, because that would test a stronger claim than EXT-CLM-004 currently states. It must instead remain in the claim boundary and motivate a separate evaluation if the external theory is meant to explain total cognitive efficiency.

---

## 10. Controls / Comparators / Ablations

**Primary comparator:** flat sequential search over the same `N` candidates.

**Structural stress conditions:**

- balanced 50/50 hierarchy;
- approximately 75/25 hierarchy;
- pathological 1-vs-rest hierarchy.

The stress conditions distinguish **having a hierarchy** from **having a hierarchy whose successive distinctions actually eliminate substantial portions of the remaining candidate space**.

---

## 11. Non-Qualifying Evidence / Confounds

The following do not by themselves establish EXT-CLM-004:

- citing the mathematical existence of balanced binary trees without performing the frozen comparison;
- assuming every hierarchy is balanced;
- treating the label “20 Questions” as evidence that twenty questions are universally sufficient;
- counting only traversal while claiming that hierarchy discovery or construction has also been explained;
- replacing the external source’s comparator with a stronger or weaker one after results are known;
- interpreting the result as proof that human or biological cognition uses this mechanism.

---

## 12. Claim Ceiling

A positive result may support only the following conclusion:

> **Given an available hierarchy whose successive distinctions substantially reduce the remaining candidate space, hierarchical recognition can produce the logarithmic traversal advantage described in EXT-CLM-004 relative to the specified flat sequential comparator.**

A positive result does **not** establish:

- how a cognitive system discovers the relevant hierarchy;
- how it selects the next useful distinction;
- what those operations cost;
- that biological cognition implements this data structure;
- that all similarity-based recognition must be O(N);
- or that *Nature of Cognitive Computation* is validated as a whole.

---

## 13. Reproducibility Boundary

Pair this protocol with:

- `claims/CLAIMS_REGISTER.md`;
- `protocol/test_001_hierarchical_search.py`;
- `runs/RUN_001_EXT-CLM-004.md`;
- `runs/RUN_001_EXT-CLM-004.csv`;
- and the corresponding claim-level result summary.

Preserve source identity, claim identity, claims-register version, protocol version, code, and raw output across reruns.

---

## 14. Final External-Source Boundary

**External evaluation ≠ framework incorporation.**

A positive, negative, or unresolved result does not make the evaluated external source part of AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
