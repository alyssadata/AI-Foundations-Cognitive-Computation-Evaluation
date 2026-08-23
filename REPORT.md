# AI Foundations | Cognitive Computation Evaluation Report

**External source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Evaluation repository:** AI-Foundations-Cognitive-Computation-Evaluation  
**Report status:** First completed evaluation  

---

## 1. Evaluation Approach

AI Foundations began this external evaluation by separating the source paper from the evaluation process.

The paper was first reviewed and its substantive claims were extracted into a claims register. Claim extraction was completed before test design so that the evaluation would begin from what the external source actually asserts rather than from a protocol designed in advance.

The claims register records each claim with:

- a stable external claim ID;
- source status;
- source location;
- evaluation readiness;
- dependencies;
- interpretation cautions;
- and a preliminary testability decision.

The initial register contains thirteen external claims. Some were classified as immediately testable, while others were marked as needing further sharpening, conceptual clarification, or later evaluation.

AI Foundations then prioritized claims that could be tested under bounded conditions without silently extending or repairing the source claim.

The first claim selected for empirical evaluation was:

## EXT-CLM-004 — Hierarchical recognition has logarithmic search advantage

The source characterizes flat similarity-based recognition as `O(N)` and a difference-defined hierarchical search as `O(log N)` when a usable hierarchy and discriminating distinctions are available.

The claim was classified as:

```text
Source status: EXPLICIT
Evaluation readiness: TESTABLE NOW
Selection: YES
```

It was selected because it was the strongest immediately measurable efficiency claim in the paper.

---

## 2. TEST_001

To evaluate EXT-CLM-004, AI Foundations designed **TEST_001 — Bounded Identification by Successive Distinctions**.

TEST_001 asked:

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

The system was given the complete active candidate/property matrix for each condition, but it was not given a decision tree or a required question order.

Exactly one candidate was privately selected as the hidden target. The tested system had to choose its own successive binary property questions until it could identify one candidate.

The purpose was not to test the already-established mathematical fact that a balanced binary tree has logarithmic depth. The purpose was to test the live dependency required by the paper's proposed mechanism:

> **Can the system itself choose useful successive distinctions inside a defined identification problem?**

---

## 3. Four Scaling Conditions

TEST_001 used four formal candidate-space conditions:

| Run | Candidate Space | Active Properties | Binary Minimum |
|---|---:|---:|---:|
| RUN_001 | N = 8 | 6 | 3 questions |
| RUN_002 | N = 16 | 8 | 4 questions |
| RUN_003 | N = 32 | 10 | 5 questions |
| RUN_004 | N = 64 | 12 | 6 questions |

The values `8`, `16`, `32`, and `64` are AI Foundations evaluation-design choices. They were selected as powers of two so that the candidate space doubled at each condition while the ideal binary path increased by exactly one question.

The intended scaling ladder was therefore:

```text
N = 8  → 3 questions
N = 16 → 4 questions
N = 32 → 5 questions
N = 64 → 6 questions
```

Each condition contained enough active properties to make every candidate uniquely identifiable while also preserving additional property choices, requiring the model to select among available distinctions rather than follow one predetermined path.

---

## 4. Models Tested

Each of the four conditions was conducted independently on four model families:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

This produced:

```text
4 candidate-space conditions
× 4 model families
= 16 formal model-condition runs
```

A fresh context was used for each formal run.

Each system selected its own property sequence. The operator answered only YES or NO according to the privately selected target row. The run ended when the system identified one candidate.

---

## 5. Scoring

Each valid question was scored against the candidate state that existed immediately before that question.

The evaluation recorded:

- whether the final identification was correct;
- whether the target was uniquely resolved;
- total valid questions;
- the binary lower bound for the condition;
- question overhead above that lower bound;
- the split produced by the selected property;
- the strongest available split at that state;
- and divider efficiency.

A divider-efficiency score of `1.0` means the system selected a strongest available distinction at that step.

The frozen TEST_001 support rule required:

1. every formal model-condition run to identify its target correctly;
2. mean divider efficiency of at least `0.90` at each tested candidate-space size;
3. mean question overhead of no more than `+1` above `ceil(log2 N)` at each tested candidate-space size.

---

## 6. Results

### Condition-Level Results

| Candidate Space | Correct | Total Questions | Binary-Minimum Questions | Mean Overhead | Mean Divider Efficiency |
|---:|---:|---:|---:|---:|---:|
| N = 8 | 4 / 4 | 12 | 12 | 0.0 | 1.0 |
| N = 16 | 4 / 4 | 16 | 16 | 0.0 | 1.0 |
| N = 32 | 4 / 4 | 20 | 20 | 0.0 | 0.984375 |
| N = 64 | 4 / 4 | 24 | 24 | 0.0 | 0.9869791667 |

Across the complete formal run set:

```text
Formal runs completed: 16 / 16
Correct final identifications: 16 / 16
Unique resolutions: 16 / 16
Total scored questions: 72
Total question overhead above binary minimum: 0
Overall mean model-run divider efficiency: 0.9928385417
```

Every formal run identified the correct hidden target in the binary minimum number of questions for its candidate-space size.

The observed scaling ladder was exactly:

```text
N = 8  → 3 questions
N = 16 → 4 questions
N = 32 → 5 questions
N = 64 → 6 questions
```

Each doubling of the candidate space added exactly one scored question in every formal run.

---

## 7. Divider Selection

Most runs selected a strongest available divider at every step, but perfect divider selection was not universal.

At `N = 32`, Grok 4.5 opened with `P01`, which produced an `11 / 21` split even though `16 / 16` distinctions were available. Its later choices were strongest available, and the target was still identified in five questions. The run mean divider efficiency was `0.9375`.

At `N = 64`, Gemini 3.1 Pro opened with `P01`, which produced a `22 / 42` split even though `32 / 32` distinctions were available. Its later choices were strongest available, and the target was still identified in six questions. The run mean divider efficiency was `0.9479166667`.

These cases are informative because they separate two measurements that could otherwise be conflated:

**minimum realized question count** and **perfect divider selection** are not the same thing.

A model can make a weaker-than-best distinction and still reach the target at the binary minimum on the realized path if the observed branch and later adaptive choices permit recovery.

Despite these two departures from perfect divider selection, the condition-level mean divider efficiency remained above `0.98` at both N32 and N64.

---

## 8. TEST_001 Outcome

The observed results satisfied every frozen support criterion:

```text
Every formal run correct: YES

Mean divider efficiency:
N08 = 1.0
N16 = 1.0
N32 = 0.984375
N64 = 0.9869791667

Mean question overhead:
N08 = 0.0
N16 = 0.0
N32 = 0.0
N64 = 0.0
```

# TEST_001 OUTCOME: SUPPORTED

---

## 9. What This Result Supports

Within the claim ceiling established before testing, TEST_001 supports the following bounded conclusion:

> **Within a defined identification problem containing measurable candidate distinctions, the tested intelligent systems autonomously selected successive distinctions that preserved a strong elimination advantage and correctly identified their targets.**

The result provides positive evidence for the operationalized dependency that an intelligent system can select useful successive distinctions inside an already-defined candidate/property space.

Across four increasing answer-space sizes and four tested model families, every formal run reached the correct target at the binary lower bound, while mean divider efficiency remained above the frozen support threshold at every condition.

---

## 10. What This Result Does Not Establish

TEST_001 does not establish that:

- arbitrary real-world recognition problems arrive with a defined candidate set;
- useful distinctions are always available;
- a system can construct the relevant hierarchy, ontology, or candidate representation from an unbounded environment;
- every selected distinction will be globally optimal;
- all cognitive recognition is `O(log N)`;
- biological cognition uses this mechanism;
- or *Nature of Cognitive Computation* is supported as a whole.

TEST_001 deliberately supplied the representation in which candidate distinctions could be measured. The harder question of how that representation is formed remains outside this first evaluation.

---

## 11. Evaluation Sequence Going Forward

TEST_001 is the first completed empirical evaluation in this repository.

The repository will continue by evaluating additional registered claims in separate, bounded sections rather than collapsing the entire paper into one oversized test or report.

The intended structure is:

```text
Claim extraction
→ testability assessment
→ bounded test design
→ formal runs
→ deterministic scoring
→ evaluation + results section
→ next selected claim
```

Each completed test can therefore stand as its own evaluation section, while a later synthesis can evaluate how the evidence across multiple tests bears on the larger theory.

---

## 12. Evidence

Claims register:

- `claims/CLAIMS_REGISTER.md`

Protocol:

- `protocol/TEST_001.md`

Condition summaries:

- `results/RUN_001_N08_SUMMARY.md`
- `results/RUN_002_N16_SUMMARY.md`
- `results/RUN_003_N32_SUMMARY.md`
- `results/RUN_004_N64_SUMMARY.md`

Completed TEST_001 evaluation:

- `results/TEST_001_EVALUATION_AND_RESULTS.md`

Full model-run records, normalized traces, scored steps, trace summaries, and individual score summaries are preserved under `runs/`.

---

## External-Source Boundary

**AI Foundations conducted and authored this evaluation. AI Foundations did not author the evaluated external source.**

The evaluated claims remain claims of Oleksandr Naumenko and *Nature of Cognitive Computation*.

Extracting, organizing, testing, supporting, weakening, or falsifying an external claim does not incorporate that claim, its terminology, its conclusions, its authorship, or its framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
