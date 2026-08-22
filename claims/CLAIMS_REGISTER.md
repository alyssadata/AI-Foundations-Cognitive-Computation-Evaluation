# AI Foundations | External Claims Register

**Evaluation repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**AI Foundations source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**External source:** *Nature of Cognitive Computation*  
**External author / creator:** Oleksandr Naumenko  
**External source version / date:** UNKNOWN  
**Claims-register version:** 0.1.0 — initial extraction, not protocol-frozen  

---

## Purpose

This file records the claims made by the independently authored external source **before** AI Foundations designs tests for them.

The purpose is to preserve the source-to-test boundary: first identify what the paper actually claims, then decide what can be operationalized, then design the protocol.

The claims recorded here remain claims of **Oleksandr Naumenko / Nature of Cognitive Computation**. Extracting, organizing, operationalizing, testing, supporting, weakening, or falsifying them does **not** incorporate them into AI Foundations or AI Foundations canon.

**External claim ≠ AI Foundations claim.**

This register is intentionally broader than the first runnable protocol. A claim may be registered and left for later without being silently dropped or treated as tested.

---

## 1. Claim-Extraction Rule

For each claim:

- preserve the external author's meaning;
- record where the claim appears;
- distinguish explicit claims from evaluator inferences;
- do not strengthen the claim beyond the source;
- do not repair ambiguity silently;
- do not turn examples, metaphors, motivations, or background statements into mechanism claims unless the source actually uses them that way;
- and do not design the test while extracting the claim.

**Claim extraction comes before operationalization.**

---

## 2. Claim Status Vocabulary

```text
EXPLICIT — directly stated by the external source.
DERIVED — follows from multiple explicit statements but is not stated in one place; derivation must be shown.
INTERPRETIVE — plausible evaluator reading that requires confirmation or caution.
AMBIGUOUS — source wording does not support one stable interpretation.

TESTABLE NOW — sufficiently bounded to begin operationalization.
NEEDS SHARPENING — potentially testable, but a term, scope, mechanism, or prediction is unclear.
CONCEPTUAL ONLY — meaningful claim but not presently suitable for empirical evaluation as stated.
OUT OF SCOPE — intentionally excluded from the current evaluation.
```

These labels describe evaluation readiness. They do not modify the external source.

---

## 3. Claims Index

| Claim ID | Short label | Source status | Evaluation readiness | Source location | Selected? |
|---|---|---|---|---|---|
| EXT-CLM-001 | Comparison as cognitive computation | EXPLICIT | NEEDS SHARPENING | Abstract p.2; Cognitive Computation pp.22–23 | YES — umbrella |
| EXT-CLM-002 | Intelligence handles differences | EXPLICIT | CONCEPTUAL ONLY | Definition and Implementation p.44 | LATER |
| EXT-CLM-003 | Core option/constraint selection algorithm | EXPLICIT | TESTABLE NOW | Core Algorithm pp.38–39 | YES |
| EXT-CLM-004 | Hierarchical recognition has logarithmic search advantage | EXPLICIT | TESTABLE NOW | Hints from 20 Questions p.19 | YES |
| EXT-CLM-005 | Dimensionality reduction + semantic binary search improves efficiency | EXPLICIT | TESTABLE NOW | pp.21, 41 | YES |
| EXT-CLM-006 | Specialization adds differences; generalization ignores them | EXPLICIT | TESTABLE NOW | pp.21–22 | YES |
| EXT-CLM-007 | General filtering algorithm extends to any cognitive function/task | EXPLICIT | NEEDS SHARPENING | pp.21–22 | YES — cross-domain |
| EXT-CLM-008 | Intelligence relies on property ranges rather than point-accurate values | EXPLICIT | TESTABLE NOW | pp.28, 41 | YES |
| EXT-CLM-009 | Continual learning accumulates options and constraints | EXPLICIT | TESTABLE NOW | pp.39–40 | LATER |
| EXT-CLM-010 | Intelligence is not creative; it uses familiar options | EXPLICIT | NEEDS SHARPENING | p.39 | LATER |
| EXT-CLM-011 | Proposed algorithm is substrate-independent | EXPLICIT | NEEDS SHARPENING | p.10 | LATER |
| EXT-CLM-012 | Language uses the core cognitive algorithm | EXPLICIT | NEEDS SHARPENING | pp.45–46 | LATER |
| EXT-CLM-013 | Language functions as a context filter rather than direct information transfer | EXPLICIT | NEEDS SHARPENING | pp.46–47 | LATER |

---

# CLAIM RECORDS

## EXT-CLM-001 — Comparison as cognitive computation

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** NEEDS SHARPENING  
**Source location:** Abstract p.2; Cognitive Computation pp.22–23  

**Faithful claim statement:**

The paper proposes comparison as a foundational form of cognitive computation, operating through comparable properties and their ranges.

### B. Scope

**Claim applies to:** the paper's proposed account of cognitive computation generally.  
**Claim does not clearly apply to:** a precisely bounded list of necessary and sufficient cognitive operations.  
**Universality level:** general / potentially universal within the paper's theory.

### C. Terms That Must Hold

```text
TERM: comparison
SOURCE USE: computation that establishes differences/interchangeability through comparable properties and ranges.
AMBIGUITY: the boundary between mere comparison and cognitively sufficient comparison is not fully operationalized.
```

### D. Dependencies

**Depends on:** EXT-CLM-008 and the paper's comparable-properties account.  
**Supports:** EXT-CLM-003 through EXT-CLM-013.

### E. Evaluator Interpretation Check

**What the source clearly says:** comparison is proposed as cognitive computation and as a core hypothesis of the theory.

**Evaluator inference to avoid:** treating every system that computes a difference as therefore intelligent.

**Author clarification needed before a direct one-shot test:** YES.

Question: what observable result would distinguish the claimed cognitive form of comparison from ordinary non-cognitive comparison or differencing?

### F. Testability Preview

**Observable consequence suggested:** successful operational subclaims should require comparison-sensitive representations or operations and degrade when those are removed.

**Evidence type:** ablation / comparative / computational.

**Main obstacle:** the umbrella claim is broader than any one experiment.

### G. Selection Decision

**Selected:** YES — as the umbrella claim.  
**Reason:** test it through narrower registered subclaims rather than treating one run as a direct proof of the whole hypothesis.

---

## EXT-CLM-002 — Intelligence handles differences

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** CONCEPTUAL ONLY  
**Source location:** Definition and Implementation, p.44  

**Faithful claim statement:**

The paper defines intelligence as the ability to handle differences.

### B. Scope

**Claim applies to:** the paper's definition of intelligence.  
**Claim does not clearly apply to:** a discriminating empirical boundary between intelligent and non-intelligent difference-handling systems.  
**Universality level:** definitional / universal within the proposed theory.

### C. Terms That Must Hold

```text
TERM: handle
SOURCE USE: connected to comparison, comparable properties, and comparison-based selection.
AMBIGUITY: no exact threshold separates trivial response-to-difference from intelligence.
```

### D. Dependencies

**Depends on:** EXT-CLM-001.  
**Supports:** the architecture as a whole.

### E. Evaluator Interpretation Check

A comparator, thermostat, or simple control system also handles differences in an ordinary sense. Counting those systems as intelligent would be an evaluator extension unless the source supplies the boundary.

**Author clarification needed before empirical testing:** YES.

### F. Testability Preview

**Observable consequence:** UNKNOWN until the inclusion/exclusion boundary is specified.

**Evidence type:** conceptual boundary test, then behavioral/computational evaluation if operationalized.

### G. Selection Decision

**Selected:** LATER.  
**Reason:** preserve as a central definition but do not pretend it is already a bounded empirical claim.

---

## EXT-CLM-003 — Core option/constraint selection algorithm

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** TESTABLE NOW  
**Source location:** Core Algorithm, pp.38–39  

**Faithful claim statement:**

The proposed core algorithm selects the most fitting option from those available while respecting relevant constraints.

### B. Scope

**Claim applies to:** categorization, planning, and other examples the paper maps into options and constraints.  
**Claim does not clearly apply to:** tasks where no stable option set or constraint representation can be recovered.  
**Universality level:** general core-mechanism claim.

### C. Terms That Must Hold

```text
TERM: available option
SOURCE USE: an option accessible in the current context.
AMBIGUITY: how candidate options are generated or represented may vary by task.

TERM: relevant constraint
SOURCE USE: a condition that filters or changes the viability of options; opportunities are also included under the paper's broad constraint treatment.
AMBIGUITY: relevance must be specified without hindsight.

TERM: most fitting
SOURCE USE: surviving/best option after relevant constraints are applied.
AMBIGUITY: tie-breaking can require additional factors.
```

### D. Dependencies

**Depends on:** EXT-CLM-001; often EXT-CLM-008.  
**Supports:** EXT-CLM-007, EXT-CLM-009, EXT-CLM-012.

### E. Evaluator Interpretation Check

Do not merely label an arbitrary decision process "options" and "constraints" after the result. The protocol must predeclare the option set, constraints, and predicted selection behavior.

**Author clarification needed:** NO for an initial bounded test.

### F. Testability Preview

**Observable consequence:** with options held constant, changing a relevant constraint should change the surviving/selected option in a predeclared way; removing irrelevant constraints should not have the same effect.

**Evidence type:** behavioral / computational / ablation.

### G. Selection Decision

**Selected:** YES.  
**Reason:** central, operationalizable, and capable of failing under controlled manipulations.

---

## EXT-CLM-004 — Hierarchical recognition has logarithmic search advantage

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** TESTABLE NOW  
**Source location:** Hints from 20 Questions, p.19  

**Faithful claim statement:**

For the paper's one-million-category example, flat similarity-based recognition is characterized as O(N), while a difference-defined hierarchical tree is characterized as O(log N), requiring up to about 20 one-property comparisons.

### B. Scope

**Claim applies to:** recognition over a category set when a usable hierarchy and discriminating property splits are available.  
**Claim does not clearly apply to:** overlapping, poorly balanced, multiply inherited, or dynamically changing category structures without additional assumptions.  
**Universality level:** conditional computational claim.

### C. Terms That Must Hold

```text
TERM: hierarchy
SOURCE USE: tree of categories/subcategories divided by discriminating properties.
AMBIGUITY: construction and maintenance cost are not included in the stated recognition comparison.

TERM: roughly balanced split
SOURCE USE: the paper prefers questions that divide remaining categories roughly in half.
AMBIGUITY: performance degrades when splits are imbalanced.
```

### D. Dependencies

**Depends on:** EXT-CLM-001, EXT-CLM-006, availability of a usable hierarchy.  
**Supports:** EXT-CLM-005.

### E. Evaluator Interpretation Check

The protocol must separate **lookup/search cost after the tree exists** from **tree-construction and maintenance cost**. The paper's stated complexity comparison is about recognition, not a proof that the entire lifecycle is O(log N).

**Author clarification needed:** NO for the narrow recognition claim.

### F. Testability Preview

**Observable consequence:** under matched category sets and known discriminators, hierarchical search should require substantially fewer category/property comparisons than exhaustive flat comparison; the measured curve should scale logarithmically under the stated tree assumptions.

**Evidence type:** computational / efficiency / comparative.

### G. Selection Decision

**Selected:** YES.  
**Reason:** strongest immediately measurable efficiency claim in the paper.

---

## EXT-CLM-005 — Dimensionality reduction + semantic binary search improves efficiency

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** TESTABLE NOW  
**Source location:** p.21; Multiple Dimensions and Dimensionality Reduction, p.41  

**Faithful claim statement:**

The paper claims that using only relevant subsets of properties, together with semantic binary search and property ranges, reduces computational load and makes cognitive functions more efficient.

### B. Scope

**Claim applies to:** recognition and other tasks in which many properties are available but only a subset is relevant.  
**Claim does not clearly apply to:** tasks where discarded dimensions carry necessary information.  
**Universality level:** general but condition-dependent.

### C. Terms That Must Hold

```text
TERM: dimensionality reduction
SOURCE USE: operations use only a relevant subset/projection of available properties.
AMBIGUITY: the method for selecting the relevant subset may itself have cost.
```

### D. Dependencies

**Depends on:** EXT-CLM-004, EXT-CLM-008.  
**Supports:** the real-time/computability motivation of the theory.

### E. Evaluator Interpretation Check

Efficiency must be measured against an explicit comparator and accuracy must be preserved enough that "faster" is not achieved merely by discarding necessary information.

**Author clarification needed:** NO for a bounded benchmark.

### F. Testability Preview

**Observable consequence:** relevant-feature restriction should reduce operations/time/memory relative to an otherwise matched full-dimensional condition without unacceptable loss on the task metric.

**Evidence type:** computational / ablation / efficiency.

### G. Selection Decision

**Selected:** YES.

---

## EXT-CLM-006 — Specialization adds differences; generalization ignores them

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** TESTABLE NOW  
**Source location:** pp.21–22  

**Faithful claim statement:**

Within the proposed hierarchy, specialization proceeds downward by introducing differences, while generalization proceeds upward by ignoring differences between subcategories.

### B. Scope

**Claim applies to:** hierarchical concepts/categories under the proposed tree organization.  
**Claim does not clearly apply to:** non-hierarchical or overlapping concept structures without further representation rules.  
**Universality level:** general within the tree model.

### C. Terms That Must Hold

```text
TERM: specialization
SOURCE USE: move down the hierarchy by adding differentiating features.

TERM: generalization
SOURCE USE: move upward by ignoring differences among lower-level categories.
```

### D. Dependencies

**Depends on:** hierarchy representation and comparable differences.  
**Supports:** EXT-CLM-007.

### E. Evaluator Interpretation Check

Do not assume that every successful generalization was produced by this mechanism. The test must compare outputs when differentiating features are added, removed, or masked.

**Author clarification needed:** NO for an initial synthetic hierarchy.

### F. Testability Preview

**Observable consequence:** adding a discriminating feature should produce a predictable finer partition; removing/ignoring that feature should collapse the partition toward the parent category.

**Evidence type:** computational / behavioral / ablation.

### G. Selection Decision

**Selected:** YES.

---

## EXT-CLM-007 — General filtering algorithm extends to any cognitive function/task

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** NEEDS SHARPENING  
**Source location:** pp.21–22  

**Faithful claim statement:**

The paper states that the general filtering algorithm illustrated by 20 Questions may be generalized to any cognitive function or task.

### B. Scope

**Claim applies to:** stated broadly across cognitive functions/tasks.  
**Claim does not clearly apply to:** no explicit exclusions are supplied.  
**Universality level:** universal-sounding / very broad.

### C. Terms That Must Hold

```text
TERM: same algorithm
SOURCE USE: filtering/selecting among options using properties/constraints, while task semantics may change.
AMBIGUITY: how much task-specific machinery may change before it is no longer the same algorithm?
```

### D. Dependencies

**Depends on:** EXT-CLM-003 and the domain-specific representation of options/constraints.  
**Supports:** EXT-CLM-012 and other cross-domain applications.

### E. Evaluator Interpretation Check

The evaluation must not retroactively redescribe every successful task as "filtering". A common operational form must be fixed before cross-domain testing.

**Author clarification needed:** YES for the strongest universal reading.

Question: what components must remain invariant across domains for two implementations to count as the same core algorithm?

### F. Testability Preview

**Observable consequence:** one predeclared algorithmic implementation should transfer across multiple task classes with domain semantics changing but core procedure held fixed.

**Evidence type:** cross-domain computational transfer / implementation / ablation.

### G. Selection Decision

**Selected:** YES — as a later cross-domain phase after the core algorithm is operationalized.

---

## EXT-CLM-008 — Intelligence relies on property ranges rather than point-accurate values

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** TESTABLE NOW  
**Source location:** Causality and Relevance p.28; Multiple Dimensions p.41  

**Faithful claim statement:**

The paper hypothesizes that intelligence primarily relies on ranges of comparable properties rather than point-accurate measurements, with ranges enabling interchangeability and computational feasibility.

### B. Scope

**Claim applies to:** representations used by the proposed cognitive architecture.  
**Claim does not clearly apply to:** cases where precision is critical; the paper allows arbitrarily small ranges there.  
**Universality level:** general hypothesis with a precision caveat.

### C. Terms That Must Hold

```text
TERM: range
SOURCE USE: bounded/rule-defined grouping of comparable property values.
AMBIGUITY: range construction and adaptation costs are not fully specified.
```

### D. Dependencies

**Depends on:** comparable properties.  
**Supports:** EXT-CLM-004, EXT-CLM-005.

### E. Evaluator Interpretation Check

A fair test must include tasks where binning/ranges help and tasks where precision matters, because otherwise the evaluation could guarantee the expected efficiency advantage by construction.

**Author clarification needed:** NO for an initial comparative test.

### F. Testability Preview

**Observable consequence:** range-based representation should reduce the candidate/operation burden under matched tasks; overly coarse ranges should expose predictable accuracy or ambiguity costs.

**Evidence type:** computational / comparative / ablation.

### G. Selection Decision

**Selected:** YES.

---

## EXT-CLM-009 — Continual learning accumulates options and constraints

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** TESTABLE NOW  
**Source location:** pp.39–40  

**Faithful claim statement:**

The paper proposes that continual learning relies on accumulating knowledge about available options, relevant constraints, actions, affected properties, and action efficiency, thereby broadening future selection.

### B. Scope

**Claim applies to:** repeated encounters/tasks under the proposed option-and-constraint architecture.  
**Claim does not clearly apply to:** all known forms of learning or representation change.  
**Universality level:** general proposal.

### C. Terms That Must Hold

```text
TERM: accumulation
SOURCE USE: adding/refining known options and constraints over experience.
AMBIGUITY: exact update rule and forgetting/reorganization mechanism are not fully specified.
```

### D. Dependencies

**Depends on:** EXT-CLM-003.  
**Supports:** broader learning claims.

### E. Evaluator Interpretation Check

Improvement over repeated runs does not by itself establish this mechanism; the evaluation would need to inspect or control what option/constraint information was added.

**Author clarification needed:** NO for a bounded implementation; YES for claims about biological mechanism.

### F. Testability Preview

**Observable consequence:** controlled addition of option/constraint knowledge should predictably change later selection and task performance.

**Evidence type:** learning curve / intervention / ablation.

### G. Selection Decision

**Selected:** LATER.

---

## EXT-CLM-010 — Intelligence is not creative; it uses familiar options

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** NEEDS SHARPENING  
**Source location:** p.39  

**Faithful claim statement:**

The paper hypothesizes that intelligence itself is not creative because it can operate only with options already familiar to it; apparently novel use depends on previously acquired property knowledge.

### B. Scope

**Claim applies to:** creativity under the paper's option-selection model.  
**Claim does not clearly apply to:** a precise boundary between recombination, abstraction, transformation, and genuinely unfamiliar option generation.  
**Universality level:** broad.

### C. Terms That Must Hold

```text
TERM: familiar option
AMBIGUITY: whether a new composition of familiar components counts as a familiar option is not fixed.

TERM: creative
AMBIGUITY: the paper uses a narrower mechanistic sense than many ordinary definitions.
```

### D. Dependencies

**Depends on:** EXT-CLM-003.

### E. Evaluator Interpretation Check

Do not test this claim until "option" and "familiar" are defined tightly enough that a novel output cannot be reclassified after the fact.

**Author clarification needed:** YES.

### F. Testability Preview

**Observable consequence:** if option-generation is restricted to registered familiar primitives/combinations, outputs claimed to be novel should remain traceable to those available structures under a predeclared rule.

**Evidence type:** generative / novelty / provenance / ablation.

### G. Selection Decision

**Selected:** LATER.

---

## EXT-CLM-011 — Proposed algorithm is substrate-independent

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** NEEDS SHARPENING  
**Source location:** p.10  

**Faithful claim statement:**

The paper proposes an algorithm that can be performed on different substrates and may explain intelligent decision-making across very different biological and organizational systems.

### B. Scope

**Claim applies to:** the same proposed computational principle across substrate types.  
**Claim does not clearly apply to:** a specified implementation equivalence test across those substrates.  
**Universality level:** broad substrate-independence claim.

### C. Terms That Must Hold

```text
TERM: same algorithm
AMBIGUITY: invariant computational structure across radically different substrates is not yet formally specified.
```

### D. Dependencies

**Depends on:** EXT-CLM-003 and EXT-CLM-007.

### E. Evaluator Interpretation Check

Showing that many systems can be *described* using option/constraint language is weaker than showing that they instantiate the same computational architecture.

**Author clarification needed:** YES for a strong substrate-independence test.

### F. Testability Preview

**Observable consequence:** a formal algorithm should be implementable across materially different computational representations while preserving predeclared input-output and complexity properties.

**Evidence type:** implementation / computational equivalence / cross-substrate simulation.

### G. Selection Decision

**Selected:** LATER.

---

## EXT-CLM-012 — Language uses the core cognitive algorithm

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** NEEDS SHARPENING  
**Source location:** pp.45–46  

**Faithful claim statement:**

The paper claims that language uses the proposed core algorithm for multiple purposes and depends on other cognitive functions.

### B. Scope

**Claim applies to:** the paper's language case study, including reference and disambiguation.  
**Claim does not clearly apply to:** every linguistic process without qualification.  
**Universality level:** broad within the language section.

### C. Terms That Must Hold

```text
TERM: uses the core algorithm
AMBIGUITY: which language operations must show option/constraint filtering, and which may rely on other mechanisms?
```

### D. Dependencies

**Depends on:** EXT-CLM-003, EXT-CLM-007.  
**Supports:** EXT-CLM-013.

### E. Evaluator Interpretation Check

Do not count a language task as support merely because its output can be narrated afterward in option/constraint vocabulary.

**Author clarification needed:** YES for the broadest reading.

### F. Testability Preview

**Observable consequence:** predeclared ambiguity/reference tasks should be solvable by the same fixed filtering procedure used outside language, with task-specific options/constraints but unchanged core logic.

**Evidence type:** cross-domain behavioral/computational transfer.

### G. Selection Decision

**Selected:** LATER.

---

## EXT-CLM-013 — Language is a context filter rather than direct information transfer

### A. External Claim

**Source status:** EXPLICIT  
**Evaluation readiness:** NEEDS SHARPENING  
**Source location:** Role of Language, pp.46–47  

**Faithful claim statement:**

The paper proposes that language does not directly transfer all information; it provides a filter over the current context that guides attention toward relevant objects, after which listener cognition collects and processes information.

### B. Scope

**Claim applies to:** communication/reference as described in the language section.  
**Claim does not clearly apply to:** contexts where the listener lacks independent perceptual or memory access to the referred information.  
**Universality level:** broad hypothesis.

### C. Terms That Must Hold

```text
TERM: filter
SOURCE USE: linguistic properties differentiate relevant objects from other context objects.
AMBIGUITY: whether verbally encoded novel facts count as information transfer is a major boundary question.
```

### D. Dependencies

**Depends on:** EXT-CLM-003 and the paper's context/reference model.

### E. Evaluator Interpretation Check

A test must distinguish information supplied only by the utterance from information already available in listener context/perception; otherwise the claim risks becoming definitional.

**Author clarification needed:** YES.

### F. Testability Preview

**Observable consequence:** in a context-rich reference task, language should function primarily by narrowing the candidate referent set; performance should depend on the listener's independently available context.

**Evidence type:** behavioral / information-ablation / reference resolution.

### G. Selection Decision

**Selected:** LATER.

---

## 4. Initial Claim-Set Review

```text
[x] External source identity recorded in source/EXTERNAL_SOURCE.md
[x] Initial major architecture claims assigned stable Claim IDs
[x] Each registered claim has a recoverable paper page/section location
[x] Explicit claims separated from evaluator cautions/inferences
[x] Ambiguities marked rather than silently repaired
[x] External terminology preserved rather than replaced with AI Foundations terminology
[x] Scope/universality not intentionally strengthened beyond the source
[x] Initial claims selected for protocol development identified
[x] No protocol has yet been designed to guarantee a claim by definition
[x] External claims remain attributed to Oleksandr Naumenko / Nature of Cognitive Computation
```

### Initial protocol candidates

The strongest first protocol candidates are:

1. **EXT-CLM-003** — core option/constraint selection;
2. **EXT-CLM-004** — hierarchical recognition complexity;
3. **EXT-CLM-005** — dimensionality reduction and efficiency;
4. **EXT-CLM-006** — specialization/generalization behavior;
5. **EXT-CLM-008** — ranges versus point-accurate representation.

`EXT-CLM-007` should become a cross-domain test only after a stable implementation of the core algorithm exists.

---

## 5. Transition to Protocol

For each selected claim:

1. carry its `EXT-CLM-###` identifier into the protocol;
2. operationalize the claim without changing its meaning;
3. predeclare the predicted observation;
4. predeclare what would weaken, falsify, or leave the claim unresolved;
5. define controls, comparators, or ablations where needed;
6. preserve the claim ID through every run and result record.

If operationalization reveals that a claim is materially ambiguous, return to this register and record the ambiguity before proceeding.

---

## External-Source Boundary

**AI Foundations is the evaluator, not the source or author of the claims recorded here.**

The external source remains external to AI Foundations.

Claim extraction, organization, testing, support, criticism, or falsification does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
