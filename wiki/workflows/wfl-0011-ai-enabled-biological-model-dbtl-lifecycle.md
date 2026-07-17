---
id: WFL-0011
type: workflow
title: AI-enabled biological-model and DBTL lifecycle
aliases:
  - biological AI model lifecycle
  - AI-enabled design-build-test-learn lifecycle
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0034
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: WFL-0011-C01
    evidence:
      - source: SRC-0033
        locator: "Summary, printed pp. 2–4 (physical pp. 23–25); Chapter 2, printed pp. 19–25 (physical pp. 40–46); Figure 2-1"
  - predicate: depends-on
    target: AST-0008
    claim_id: WFL-0011-C02
    evidence:
      - source: SRC-0033
        locator: "Chapter 5, printed pp. 64–74 (physical pp. 85–95); Figures 5-1–5-2"
  - predicate: depends-on
    target: SYS-0011
    claim_id: WFL-0011-C02
    evidence:
      - source: SRC-0033
        locator: "Chapters 2 and 5, printed pp. 19–25 and 68–77 (physical pp. 40–46 and 89–98)"
  - predicate: evidenced-by
    target: SRC-0034
    claim_id: WFL-0011-C05
    evidence:
      - source: SRC-0034
        locator: "§§3.2–5, pp. 5–9; Resources, pp. 9–10; Appendix §§A.2–A.4, pp. 28–34"
tags:
  - artificial-intelligence
  - biological-models
  - dbtl
  - model-lifecycle
  - experimental-validation
  - provenance
---

# AI-enabled biological-model and DBTL lifecycle

## Scope

This page normalizes the lifecycle represented in NASEM and the bounded
ProteinGym research-evaluation segment without inventing a complete MLOps
process. It connects research-data management, model analysis/design and
physical Design–Build–Test–Learn (DBTL) work. The workflow is functional and
defensive; it contains no biological design, experimental parameter, model
prompt, target or automation instruction.

> **Claim record — WFL-0011-C01 | source-report**
> **Claim:** NASEM describes a biological-AI workflow in which data and domain
> knowledge support analysis or design, candidate outputs pass to physical
> build/test and experimental results can feed later learning and refinement.
> **Claim status:** active
> **Scope:** Functional DBTL stages and feedback, not one mandatory sequence,
> autonomous laboratory, deployed model lifecycle or safe-outcome guarantee.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary, printed pp. 2–4 (physical pp. 23–25); Chapter 2, printed pp. 19–25
> (physical pp. 40–46), especially Figure 2-1; Chapter 3, printed pp. 32–37
> (physical pp. 53–58); Appendix A Figure A-1 and design discussion, printed
> pp. 89 and 106–109 (physical pp. 110 and 127–130).
> **Basis / limits:** Main-report stages and physical gate are direct.
> Appendix A is attributed background in the same lineage. No throughput,
> correctness, deployment or outcome metric is supplied.

## Reconciled lifecycle

| Lifecycle phase | Direct state/function | Preserved limit |
| --- | --- | --- |
| Plan and scope | define research/public-health question, applicable data, biological context, roles and intended use | A stated purpose does not prove authority or feasibility |
| Acquire and create data | collect experimental, repository, surveillance or other biological data and context | Coverage, labels, consent and quality can be incomplete |
| Curate, label and preserve | standardize/annotate, record provenance, store and manage | No universal curation metric or complete label lineage |
| Train, adapt or analyze | train/fine-tune a biological model or use a model for analysis/inference | Model family and task determine applicability; inventory/version state may be incomplete |
| Generate or rank output | predict, classify, score or propose candidate outputs | Digital output is not biological truth or authorization to act |
| Review and validate digitally | evaluate robustness, uncertainty, task fit and safety under human review | Internal consistency and a benchmark grade are not experimental validation |
| Select and gate | accountable person/process decides whether a candidate may cross into build/test or consequential use | Human presence does not guarantee a correct or safe decision |
| Build and test physically | synthesize/order/build only through applicable controls and conduct bounded experiment/validation | Physical production, safety, quality and resources remain separate constraints |
| Learn and reconcile | record results, compare expectation to observation and feed validated evidence into later data/model state | Feedback can amplify low-quality or corrupted state if provenance is weak |
| Deploy or use | apply a validated output in research, surveillance, public-health or other explicitly governed context | NASEM does not provide a universal deployment/authorization pattern |
| Monitor and update | reassess data quality, model change, capability and vulnerabilities; audit updates | Monitoring cadence, thresholds and implementation are not established |
| Retire and dispose | **open gap** for model retirement/decommission and complete derivative-state disposition | Data retention/destruction in Figure 5-1 is not model retirement |

> **Claim record — WFL-0011-C02 | analytic-judgment**
> **Claim:** The canonical workflow depends on the assets in `AST-0008` and the
> data–compute–model–laboratory boundaries in `SYS-0011`; crossing from digital
> output to physical or consequential action is an explicit decision gate.
> **Claim status:** active
> **Scope:** Wiki normalization of source-supported dependencies and boundary;
> not an implemented architecture or claim that every path is linear.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 2, printed pp. 19–25 (physical pp. 40–46); Chapter 5 and Figures
> 5-1–5-2, printed pp. 64–77 (physical pp. 85–98).
> **Basis / limits:** Assets, layers, DBTL stages and transfer are direct; their
> canonical arrangement is analysis. The report supplies no site topology,
> interface validation, RACI or universal authorization rule.

## Provenance and reproducibility states

NASEM connects data origin, creation context, model/software dependencies and
training use. Its research-data lifecycle visually includes metadata,
electronic laboratory notebooks, version control, reproducibility, retention
and destruction. Appendix A discusses held-out evaluation and experimental
feedback. These are relevant lifecycle predicates but remain incomplete for a
full model lineage: acquisition/label records, training configuration, model
version, deployment state, monitoring history and retirement disposition are
not all joined in one demonstrated record.

> **Claim record — WFL-0011-C03 | source-report**
> **Claim:** The report supports data provenance, software-dependency context,
> electronic records/versioning, evaluation and experimental feedback as
> lifecycle assurance states, but does not demonstrate one complete
> reproducible model lineage.
> **Claim status:** active
> **Scope:** Reported lifecycle functions and omissions; not a reproducibility
> audit, model card, registry record or successful restoration.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 5, printed pp. 69–81 (physical pp. 90–102), especially Figures
> 5-1–5-2; Appendix A, printed pp. 115–124 (physical pp. 136–145).
> **Basis / limits:** Named states are direct or visually verified. The
> third-party Figure 5-1 is a data lifecycle; it cannot supply absent model
> deployment, monitoring/update or retirement states by analogy.

## Completeness and evidence state

| Evidence dimension | Status |
| --- | --- |
| Stage/function design | direct single-source evidence |
| Named deployment | unknown |
| Monitoring/update implementation | unknown |
| Model retirement/decommission | absent from represented source |
| Reproducible end-to-end lineage | not demonstrated |
| Experimental/model validation | required/discussed plus one primary benchmark result; no universal downstream result |
| Effectiveness or independent evaluation | one author-team benchmark line; no deployment or independent confirmation |

> **Claim record — WFL-0011-C04 | analytic-judgment**
> **Claim:** `WFL-0011` is a strong DBTL and partial model-lifecycle map, not a
> complete acquisition-to-retirement lifecycle or evidence of implementation,
> reproducibility, testing success or effectiveness.
> **Claim status:** active
> **Scope:** Coverage classification for this workflow.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> exact locators above.
> **Basis / limits:** DBTL and many data/model states are direct in NASEM.
> Retirement is absent and deployment/monitoring are not reconciled end to
> end. ProteinGym, added below, is a bounded research benchmark rather than an
> implementation or downstream outcome study.

> **Claim record — WFL-0011-C05 | source-report**
> **Claim:** ProteinGym directly instantiates a bounded research-evaluation
> segment: curate/label data → preprocess and split → train or score → compare
> metrics and biological strata → report limitations and reproducibility
> resources.
> **Claim status:** active
> **Scope:** ProteinGym v1.0 benchmark workflow; not production deployment,
> monitoring/update implementation, model retirement or end-to-end runtime
> reproduction.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> §§3.2–5, pp. 5–9; Resources, pp. 9–10; Appendix §§A.2–A.4,
> pp. 28–34; `SRC-0034-C03`–`C07`.
> **Basis / limits:** Stages, split logic, outputs and limitations are direct.
> Continuing website/repository updates are planned or reported, not a
> demonstrated monitor/update/retirement loop.

## Related pages

- [SYN-0023 — Engineering-biology transfer reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [RSK-0016 — AI output to unsafe action](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0016 — Biological AI controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [WFL-0005 — Genomic-data lifecycle](wfl-0005-genomic-data-lifecycle.md)
- [WFL-0008 — Procurement/screening segment](wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SYN-0018 — Biological-AI SF2 reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SRC-0034 — ProteinGym benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact
  locators above.
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md), exact
  locators above.
