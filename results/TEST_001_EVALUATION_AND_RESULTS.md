# AI Foundations | TEST_001 — Evaluation and Results

**External source:** *Nature of Cognitive Computation*  
**External author:** Oleksandr Naumenko  
**External Claim ID:** `EXT-CLM-004`  
**Protocol:** `TEST_001`, version 2.2.0  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen

This file closes the first completed evaluation in the repository as a compact, section-sized result. Detailed transcripts, traces, step scores, and condition summaries remain in `runs/` and `results/` and are not repeated here.

---

## 1. Evaluated Question

TEST_001 asked:

> **Given an explicit identification problem with a defined answer space, can an intelligent system autonomously select successive distinctions that efficiently reduce that space and identify the correct answer?**

The evaluated external claim concerns a logarithmic search advantage from hierarchical difference-based recognition when useful distinctions are available.

TEST_001 isolates one live dependency inside that claim: the system is given the complete candidate/property matrix, but it is not given a decision tree or a required question order. It must choose its own successive binary distinctions.

---

## 2. Evaluation Design

Four candidate-space conditions were tested:

| Run | Candidate Space | Active Properties | Binary Minimum |
|---|---:|---:|---:|
| RUN_001 | 8 | 6 | 3 |
| RUN_002 | 16 | 8 | 4 |
| RUN_003 | 32 | 10 | 5 |
| RUN_004 | 64 | 12 | 6 |

The specific values `8`, `16`, `32`, and `64` are AI Foundations evaluation-design choices. They operationalize the scaling claim using powers of two; they are not values specified by the external paper.

The same four model families were tested at every condition:

- GPT-5.6 Sol
- Claude Opus 5
- Gemini 3.1 Pro
- Grok 4.5

This produced **16 formal model-condition runs**.

For each run, the operator privately selected one candidate. The system asked one active-property YES/NO question at a time until it identified one candidate. Each choice was scored against the strongest still-unused divider available at the actual candidate state.

Primary measures were:

- correctness of final identification;
- unique resolution;
- valid question count;
- question overhead above `ceil(log2 N)`;
- divider efficiency.

---

## 3. Results

### 3.1 Condition-Level Results

| N | Correct | Total Questions | Binary-Minimum Questions | Mean Overhead | Mean Divider Efficiency |
|---:|---:|---:|---:|---:|---:|
| 8 | 4 / 4 | 12 | 12 | 0.0 | 1.0 |
| 16 | 4 / 4 | 16 | 16 | 0.0 | 1.0 |
| 32 | 4 / 4 | 20 | 20 | 0.0 | 0.984375 |
| 64 | 4 / 4 | 24 | 24 | 0.0 | 0.9869791667 |

Across the complete formal run set:

```text
Completed formal runs: 16 / 16
Correct final identifications: 16 / 16
Unique resolutions: 16 / 16
Total scored questions: 72
Total question overhead: 0
Overall mean model-run divider efficiency: 0.9928385417
```

Every formal run identified the correct target in the binary minimum number of questions for its candidate-space size.

The realized scaling ladder was therefore:

```text
N = 8  → 3 questions
N = 16 → 4 questions
N = 32 → 5 questions
N = 64 → 6 questions
```

Each doubling of the candidate space added exactly one scored question in every formal run.

### 3.2 Divider Selection

Perfect divider selection was not required for every successful run.

At N08 and N16, every scored property choice across all models matched a strongest available divider.

At N32, Grok 4.5 opened with `P01`, producing an `11 / 21` split even though `16 / 16` dividers were available. Its remaining choices were strongest available, and it still identified the target in five questions. The run mean divider efficiency was `0.9375`.

At N64, Gemini 3.1 Pro opened with `P01`, producing a `22 / 42` split even though `32 / 32` dividers were available. Its remaining choices were strongest available, and it still identified the target in six questions. The run mean divider efficiency was `0.9479166667`.

These two runs show that **minimum realized question count and perfect divider selection are not identical measures**. A weaker distinction can still occur on a path that reaches the target at the binary minimum if the realized branch and later adaptive choices permit recovery.

---

## 4. Formal Outcome

The frozen TEST_001 protocol defines `SUPPORTED` as requiring:

1. every formal model-condition run to identify its target correctly;
2. mean divider efficiency of at least `0.90` at each tested `N`;
3. mean question overhead no more than `+1` above `ceil(log2 N)` at each tested `N`.

Observed results:

```text
Correct identification at every formal run: YES

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

All frozen support criteria are satisfied.

# TEST_001 OUTCOME: SUPPORTED

---

## 5. What the Result Supports

Within the claim ceiling established before the runs, TEST_001 supports the following bounded conclusion:

> **Within a defined identification problem containing measurable candidate distinctions, the tested intelligent systems autonomously selected successive distinctions that preserved a strong elimination advantage and correctly identified their targets.**

The strongest empirical observation is not merely final correctness. Across four increasing answer-space sizes and four tested model families, every formal run reached the correct target at the binary lower bound, while condition-level mean divider efficiency remained above `0.98`.

This provides positive evidence for the operationalized dependency that an intelligent system can select useful successive distinctions inside an already-defined candidate/property space.

---

## 6. What the Result Does Not Establish

TEST_001 does not establish that:

- arbitrary real-world recognition problems arrive with a defined candidate set;
- useful distinctions are always available;
- a system can construct the relevant ontology or candidate representation from an unbounded environment;
- every selected distinction will be globally optimal;
- all cognitive recognition is `O(log N)`;
- biological cognition uses this procedure;
- or *Nature of Cognitive Computation* is supported as a whole.

The controlled matrix intentionally supplies the representation in which distinctions can be measured. The harder question of how such a representation is constructed remains outside TEST_001.

---

## 7. Run-Integrity Notes

The formal results remained deterministically interpretable across all 16 runs.

Recorded non-score-changing deviations included:

- recurring extra task-state narration from Claude Opus 5 despite instructions to begin with the P question only;
- one recoverable Gemini Python `NameError` in an earlier condition, preserved and clarified post-run;
- one GPT-5.6 Sol N64 narration line after the sixth answer that announced another question but was followed immediately by the correct final answer.

Tool use to read or analyze the supplied candidate/property matrix is not treated as a deviation because matrix access is required to choose among the supplied distinctions and does not reveal the privately selected target.

None of the preserved deviations altered the scored answer path, introduced target leakage, or prevented deterministic scoring.

---

## 8. Evidence Structure

Condition summaries:

- `results/RUN_001_N08_SUMMARY.md`
- `results/RUN_002_N16_SUMMARY.md`
- `results/RUN_003_N32_SUMMARY.md`
- `results/RUN_004_N64_SUMMARY.md`

Each model-run additionally has a full archival record, normalized trace, deterministic scored-steps file, trace summary, and score summary under `runs/`.

This evaluation is therefore closed without collapsing the underlying evidence into this section. Later evaluations of the external paper can be written as separate evaluation/result sections and combined only at the final synthesis layer.

---

## External-Source Boundary

**AI Foundations conducted and authored this evaluation. AI Foundations did not author the evaluated external source.**

External evaluation does not incorporate the source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.

**AI Foundations evaluation source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
