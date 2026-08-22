# AI Foundations | Result 001 — EXT-CLM-004

**Evaluation repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**AI Foundations source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source version / identifier:** PhilArchive Version 1 / NAUNOC-2 / 2025-09-10  
**Result version:** 1.0.0  
**Date:** 2026-08-22

---

## Evaluated Claim

**EXT-CLM-004 — Hierarchical recognition has logarithmic search advantage**

Registered claim: hierarchical recognition organized through successive sibling differences can achieve `O(log N)` search rather than the `O(N)` flat-comparison behavior used as the paper’s comparator.

**Protocol:** `protocol/PROTOCOL_001_EXT-CLM-004.md` v1.0.0  
**Run:** `runs/RUN_001_EXT-CLM-004.md`  
**Raw evidence:** `runs/RUN_001_EXT-CLM-004.csv`

---

## Evaluation Disposition

**SUPPORTED_CONDITIONALLY**

The balanced hierarchical condition matched `log2(N)` exactly across all tested candidate spaces, while the flat sequential comparator matched `N` in the worst case.

At `N = 1,048,576`:

```text
flat worst-case comparisons: 1,048,576
balanced hierarchical distinctions: 20
flat / balanced ratio: 52,428.8
```

The stress conditions showed that the result depends on the elimination strength of successive distinctions:

```text
approximately 75/25 worst-case depth: 48
pathological 1-vs-rest worst-case depth: 1,048,575
```

A hierarchy that repeatedly removes only one candidate loses the logarithmic advantage. A hierarchy that removes a substantial fraction at each step retains a shallow search path, with the balanced case giving the strongest binary result.

---

## What the Evaluation Actually Established

The run supports the narrow recognition-time claim:

> **Given an available hierarchy whose successive distinctions substantially reduce the remaining candidate space, hierarchical recognition can produce the logarithmic traversal advantage described in EXT-CLM-004 relative to the specified flat sequential comparator.**

The result is conditional because the test begins with the relevant hierarchy available.

---

## Unresolved Dependency Exposed by the Evaluation

The evaluation does **not** establish how a cognitive system obtains the useful hierarchy or chooses the next distinction.

The source describes desirable features of good successive questions, including dependence on earlier answers and approximately balanced partitioning, but this protocol did not find a sufficiently precise source-specified mechanism whose computational cost could be counted without adding an evaluator-authored repair.

Therefore the following remains unresolved:

> **Does the cost of discovering, selecting, constructing, or maintaining the distinctions required for efficient traversal preserve the claimed computational advantage at the level of the complete cognitive mechanism?**

That is not a falsification of EXT-CLM-004 as registered. It is the next exposed evaluation boundary.

---

## Claim Ceiling

This result does **not** establish:

- that cognition universally uses balanced binary trees;
- that biological cognition implements the tested structure;
- that every similarity-based recognition method is necessarily `O(N)`;
- that the total cognitive process is `O(log N)` once hierarchy formation and divider-selection costs are counted;
- or that *Nature of Cognitive Computation* is supported as a whole.

---

## Reproducibility

```text
SOURCE RECOVERABLE: yes
CLAIMS REGISTER PRESERVED: yes
FROZEN PROTOCOL PRESERVED: yes
RUN METADATA PRESERVED: yes
RAW OUTPUT PRESERVED: yes
CODE PRESERVED: yes
COMPARATOR / STRESS CONDITIONS PRESERVED: yes
KNOWN REPRODUCIBILITY LIMITATION: the source does not provide an operational divider-selection / hierarchy-construction cost model for this test
```

---

## External-Source Boundary

**AI Foundations conducted the evaluation. AI Foundations did not author the evaluated external source.**

The external source remains external to AI Foundations. A supporting result does not incorporate the source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

---

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
