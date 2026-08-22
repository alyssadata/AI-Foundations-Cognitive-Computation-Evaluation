# AI Foundations | External Evaluation Repository Template

**Repository:** AI-Foundations-EXTERNAL-EVAL-Repo-Template  
**Status:** Reusable External Evaluation Template  
**Evaluator:** AI Foundations  
**Evaluation author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Canon status:** This template does not make any evaluated external source part of AI Foundations or AI Foundations canon.  
**Version:** 1.0.0  
**Release date:** [YYYY-MM-DD]  
**Canonical entrance:** https://awakeningcodex.com

---

## Repository Purpose

This repository is the reusable template for **AI Foundations external evaluations**.

Use it when AI Foundations evaluates a theory, paper, model, framework, dataset, protocol, system, repository, claim set, or other source that was created outside AI Foundations.

The evaluation is conducted by **AI Foundations**. The evaluated source remains an **independently authored external source**.

**AI Foundations may evaluate an external source without adopting it.**

**External evaluation ≠ framework incorporation.**

Evaluation, citation, testing, reproduction of test conditions, positive results, negative results, or discussion of an external source does **not** make that source, its claims, terminology, authorship, conclusions, or framework part of AI Foundations.

---

## Repository Structure

```text
source/
claims/
protocol/
runs/
results/
```

The folders follow the evaluation path:

**source → claims → protocol → runs → results**

Keep root-level repository identity files such as `README.md`, `CITATION.cff`, and `LICENSE.md` at the top level.

---

## Required External-Source Record

Every child repository created from this template must identify the evaluated source before the evaluation is run.

Start with [`source/EXTERNAL_SOURCE_TEMPLATE.md`](source/EXTERNAL_SOURCE_TEMPLATE.md) and record at minimum:

- external source title;
- external author / creator;
- source type;
- where the source came from;
- canonical or supplied source location;
- version, publication date, release date, or other identifier when available;
- date accessed or received;
- exact material under evaluation;
- external source citation;
- evaluator: **AI Foundations**;
- evaluation author: **Alyssa Solen**;
- and the external-source boundary statement.

Do not begin a formal evaluation until the evaluated object is identifiable enough for another researcher to recover the same source or understand exactly what material was tested.

---

## Required Claims Register

After the external source is identified and **before protocol design**, complete [`claims/CLAIMS_REGISTER_TEMPLATE.md`](claims/CLAIMS_REGISTER_TEMPLATE.md).

The claims register is the source-to-test bridge. It records what the external work actually claims before AI Foundations decides how to test those claims.

Each candidate claim receives a stable `EXT-CLM-###` identifier and records:

- the exact or faithfully stated external claim;
- where the claim appears in the external source;
- whether the claim is explicit, derived, interpretive, or ambiguous;
- its scope and stated limits;
- terms whose meaning materially affects the claim;
- dependencies on other external claims;
- whether clarification is needed;
- whether the claim is presently testable;
- and whether it has been selected for the current evaluation.

**Claim extraction comes before operationalization.**

Do not strengthen, repair, generalize, or silently reinterpret an external claim in order to make it easier to test.

**External claim ≠ AI Foundations claim.**

Recording or evaluating an external claim does not incorporate it into AI Foundations or AI Foundations canon.

---

## Required External-Source Boundary

Every child repository must preserve this distinction in substance:

> **This repository is an AI Foundations evaluation of an independently authored external source. AI Foundations is the evaluator, not the source or author of the evaluated work. The external source remains external to AI Foundations. Evaluation does not incorporate the external source, its claims, terminology, conclusions, authorship, or framework into AI Foundations or AI Foundations canon.**

The external source must retain its own authorship, provenance, citation, and applicable license.

The AI Foundations source-line applies to the **evaluation materials authored under AI Foundations**, not to ownership or authorship of the external source itself.

---

## Evaluation Setup

For each external evaluation:

1. Create a child repository from this template.
2. Rename and complete `source/EXTERNAL_SOURCE_TEMPLATE.md` as the repository's source record.
3. Complete `claims/CLAIMS_REGISTER_TEMPLATE.md` and assign stable IDs to the external claims relevant to the evaluation.
4. Select the claim or claims to be evaluated without changing their meaning.
5. For each selected claim, define what observable evidence would support, weaken, falsify, or leave it unresolved.
6. Customize `protocol/PROTOCOL_TEMPLATE.md` for the selected claim IDs.
7. Customize the run and output templates only as needed for that evaluation.
8. Preserve raw evidence and enough metadata for reproducibility.
9. Complete `results/EVALUATION_SUMMARY_TEMPLATE.md` only after the relevant runs are preserved, using the registered claim IDs and frozen protocol versions.
10. Keep the external-source boundary visible in the README, claims register, protocol, run records, and evaluation summary.

The evaluation must not be designed so that adopting the external source's own vocabulary automatically guarantees its conclusion.

---

## External Evaluation Templates

This repository includes six reusable evaluation files:

- [`source/EXTERNAL_SOURCE_TEMPLATE.md`](source/EXTERNAL_SOURCE_TEMPLATE.md) — identifies and bounds the independently authored external source.
- [`claims/CLAIMS_REGISTER_TEMPLATE.md`](claims/CLAIMS_REGISTER_TEMPLATE.md) — extracts, identifies, and bounds the external claims before test design.
- [`protocol/PROTOCOL_TEMPLATE.md`](protocol/PROTOCOL_TEMPLATE.md) — formal evaluation specification for selected claim IDs.
- [`protocol/EASY_RUN_SHEET_TEMPLATE.md`](protocol/EASY_RUN_SHEET_TEMPLATE.md) — operator-facing exact execution path.
- [`runs/RUN_OUTPUT_TEMPLATE.md`](runs/RUN_OUTPUT_TEMPLATE.md) — reproducible run / evidence record.
- [`results/EVALUATION_SUMMARY_TEMPLATE.md`](results/EVALUATION_SUMMARY_TEMPLATE.md) — claim-level synthesis across completed runs without replacing the underlying evidence.

Customize them to the external source and claim under evaluation. Remove sections that do not apply.

Do not force one experimental structure onto unrelated external sources merely because these files exist in the template.

---

## Evidence Rule

Preserve the evidence required to reproduce or inspect the evaluation.

Depending on the study, this may include:

- exact source material or a recoverable source reference;
- claim IDs;
- exact prompts / stimuli;
- model, system, software, or environment versions;
- configuration and sampling settings when available;
- code version / commit;
- raw outputs;
- scoring or decision rules;
- deviations and missing data;
- timestamps;
- run manifests;
- and verbatim transcripts when the evaluation is interaction-based.

Use `UNKNOWN` rather than guessing unavailable metadata.

The evaluation summary is a synthesis layer only. It must not replace or overwrite the claims register, frozen protocol, or primary run evidence.

---

## Source-Line

The AI Foundations evaluation source-line is:

**Alyssa Solen → AI Foundations → Origin | Continuum**

This source-line must remain attached to citation or reuse of the **AI Foundations evaluation materials**.

It must not be used to overwrite, absorb, or replace the authorship or provenance of the external source being evaluated.

---

## Citation Boundary

Two things may require separate citation:

1. the **external source**, cited to its actual author / creator and source; and
2. the **AI Foundations evaluation**, cited to Alyssa Solen / AI Foundations.

Do not collapse those citations into one authorship claim.

Preferred evaluation citation template:

Alyssa Solen, *AI Foundations: External Evaluation — [Evaluation Title]*, [Repository Name] Repository. Source-line: Alyssa Solen → AI Foundations → Origin | Continuum.

---

## License

This repository uses `CC-BY-ND-4.0` citation metadata and the AI Foundations Source-Line License for the **evaluation materials**.

The external source remains subject to its own authorship, copyright, provenance, and licensing terms.

Citation of the evaluation is permitted with the AI Foundations source-line preserved.

Derivative use of AI Foundations evaluation materials is not authorized except as expressly stated in `LICENSE.md`.

---

## Contact

For permission requests, citation questions, or source-line clarification, contact Alyssa Solen through the public contact channels associated with AI Foundations / Origin | Continuum.

Canonical entrance:

https://awakeningcodex.com
