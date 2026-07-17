---
id: AST-0008
type: asset
title: AI-enabled biological data, model and stakeholder assets
aliases:
  - biological AI asset and stakeholder map
  - life-science model assets
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0006
  - SRC-0034
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: AST-0008-C01
    evidence:
      - source: SRC-0033
        locator: "Summary, printed pp. 1–4 (physical pp. 22–25); Chapters 2 and 5, printed pp. 19–25 and 64–77 (physical pp. 40–46 and 85–98); Figures 5-1–5-2"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: AST-0008-C02
    evidence:
      - source: SRC-0006
        locator: "§§1.2 and 5.1–5.12, printed pp. 4–7 and 21–28 (PDF pp. 15–18 and 32–39); Tables 10–36"
  - predicate: evidenced-by
    target: SRC-0034
    claim_id: AST-0008-C05
    evidence:
      - source: SRC-0034
        locator: "Figure 1, p. 3; §§3–4, pp. 4–8; Resources, pp. 9–10; Appendix §§A.3–A.4, pp. 29–34"
tags:
  - artificial-intelligence
  - biological-data
  - models
  - software
  - compute
  - stakeholders
  - intellectual-property
---

# AI-enabled biological data, model and stakeholder assets

## Scope and evidence lineages

This defensive asset map covers biological AI as a coupled data/model/software/
compute/experimental system. It does not contain individual records, biological
designs, model weights, code, credentials, target lists or laboratory
parameters.

Two materially independent institutional lineages are reconciled at class
level:

- NASEM supplies the biology-specific model, software, compute, output,
  laboratory and stakeholder ecosystem;
- NIST IR 8467 2pd supplies a genomics-specific data/provenance/privacy and
  stakeholder line, including intellectual property, donors and relatives.
- ProteinGym supplies a third, primary empirical benchmark instance with
  concrete data/model/resource roles; it is not a complete inventory or an
  independent evaluator of every included method.

NIST is still a Second Public Draft, and none of the three lineages is an
organization-specific inventory or implementation audit.

> **Claim record — AST-0008-C01 | source-report**
> **Claim:** NASEM identifies biological datasets/labels, model families,
> software and dependencies, compute/repositories, APIs, outputs/designs,
> laboratory assets and researcher/developer/steward/user/funder roles as
> coupled assets in AI-enabled life-science work.
> **Claim status:** active
> **Scope:** Classes directly named or diagrammed in the report; not a complete
> inventory, system topology, SBOM, identity model or current model catalogue.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary, printed pp. 1–4 (physical pp. 22–25); Chapters 2 and 5, printed pp.
> 19–25 and 64–77 (physical pp. 40–46 and 85–98); Figures 5-1–5-2; Appendix A
> taxonomy and dataset review, printed pp. 85–124 (physical pp. 106–145).
> **Basis / limits:** Main-report classes are direct; Appendix A is
> author-attributed background in the same lineage. Figure 5-1 visually names
> electronic notebooks, version control, reproducibility and IP but is a
> reproduced data-lifecycle framework, not a complete model lifecycle.

> **Claim record — AST-0008-C02 | source-report**
> **Claim:** NIST's genomics profile independently identifies data origin,
> custody, annotations, derived data, software/version/configuration context,
> intellectual property, donors, relatives, researchers and authorized
> decision/use roles as protected genomic-data interests.
> **Claim status:** active
> **Scope:** Human and non-human genomic-data profile classes with human-
> privacy predicates applied only where human data are processed; not all
> biological AI or a final standard.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2 and 5.1–5.12, printed pp. 4–7 and 21–28 (PDF pp. 15–18 and 32–39),
> especially Mission Objectives 1–6 and 10; Tables 10–36.
> **Basis / limits:** Classes and target-state outcomes are direct. NIST's
> source is a draft genomics profile, not evidence that every biological model
> uses human data or that the recommended inventory exists.

## Canonical asset and stakeholder matrix

| Frozen `AIB-AS` class | Canonical classes | Evidence and boundary |
| --- | --- | --- |
| Datasets and labels | sequence, structure, function, genomic, epigenomic, transcriptomic, epidemiological, clinical-context and experimental-result data; annotations, metadata and labels | NASEM Ch. 5/Appendix A; NIST provenance. Predicted data are not experimental truth |
| Models and code | foundation, predictive, generative/design and assistant models; source code, libraries and packages | NASEM Chs. 2/5. No weights, source or vulnerability detail is included |
| Environments and dependencies | training/analysis environments, open-source dependencies, proprietary API boundary, sandbox/workbench | NASEM pp. 52–53 and 68–77. Containers and complete environment manifests remain absent |
| Compute and storage | cloud/HPC, repository, database, storage and model-training/inference resources | NASEM pp. 68–73. A resource class is not a deployed capacity or trust guarantee |
| Outputs and IP | predictions, scores, candidate designs, analyses, models, publications, records and intellectual property | NASEM Figures 5-1/5-2; NIST Mission Objective 10. No design or IP content is reproduced |
| Subjects and relatives | consented human-data participants/donors and biological relatives where human genomic information is involved | NASEM All of Us case plus NIST Mission Objectives 2/4/5. Not applicable by default to non-human data |
| Developers and operators | model/software developers, data stewards, repository/access bodies, laboratory/instrument operators and infrastructure providers | NASEM Chs. 4–5. Role labels do not establish accountability in one deployment |
| Researchers and decision makers | scientists, bioinformaticians, experimental reviewers, clinical/public-health users, funders and oversight actors | NASEM Chs. 2/4/5. Human review does not guarantee a safe or correct decision |

> **Claim record — AST-0008-C03 | analytic-judgment**
> **Claim:** NASEM and NIST jointly support all frozen biological-AI asset and
> stakeholder class labels, while their distinct scope, version and lineage
> boundaries remain explicit.
> **Claim status:** active
> **Scope:** Reconciled class coverage for biological AI and genomics; not one
> universal inventory, architecture, legal classification or deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 2, 4 and 5, printed pp. 19–25, 46–81 (physical pp. 40–46,
> 67–102); [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2 and 5.1–5.12, printed pp. 4–7 and 21–28 (PDF pp. 15–18 and 32–39).
> **Basis / limits:** Each frozen label has direct support somewhere in the
> two-lineage union, and the matrix collectively draws on two materially
> independent institutions. NASEM is broad biological AI, while NIST supplies
> stronger genomics privacy/provenance and IP/relative classes. Neither proves
> completeness in a named organization, and no claim says each institution
> independently supplies every literal.

## State and sensitivity boundaries

- A biological dataset may be public, controlled, proprietary or otherwise
  sensitive; `FAIR` does not mean universally open.
- Human privacy, consent and kinship predicates are not transferred to plant,
  microbial or model-organism data without a human-data link.
- A model, output or package is not trusted merely because it is open source,
  proprietary, high performing or cited.
- Digital candidate outputs remain distinct from synthesized material,
  experimental state, clinical state and public-health action.
- Provenance records support assessment; their existence does not establish
  accuracy, authorization or fitness for purpose.

> **Claim record — AST-0008-C04 | analytic-judgment**
> **Claim:** Asset class coverage does not establish asset inventory quality,
> sensitivity classification, ownership, authorization, implementation or
> protection effectiveness in any deployment.
> **Claim status:** active
> **Scope:** Evidence-state boundary for this canonical map.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> printed pp. 65–81 (physical pp. 86–102); [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3–6 and Tables 4–36.
> **Basis / limits:** Both sources describe target classes, risks and
> recommended management. Neither supplies a named inventory completeness
> metric, conformance result or independent effectiveness evaluation.

> **Claim record — AST-0008-C05 | source-report**
> **Claim:** ProteinGym supplies a concrete biological-AI benchmark asset
> instance containing DMS and clinical labels, processed and reported raw-data
> classes, alignments, structures, code/common interfaces, model scores, some
> checkpoints and researcher/model-developer/user roles.
> **Claim status:** active
> **Scope:** Assets reported for ProteinGym v1.0; not retained record-level
> data, a current repository inventory, container/model registry, ownership
> determination or deployment.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> Figure 1, p. 3; §§3–4, pp. 4–8; Resources, pp. 9–10; Appendix
> §§A.3–A.4, pp. 29–34; `SRC-0034-C03/C04/C07`.
> **Basis / limits:** The classes and reported resource roles are direct. Only
> the paper/official record are retained; availability, exact state and
> reproducibility of external resources were not validated.

## Related pages

- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [RSK-0016 — AI output to unsafe action](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0016 — Biological AI controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [AST-0001 — Genomic data](ast-0001-genomic-data.md)
- [AST-0004 — Synthesis order/equipment assets](ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0006 — NIST genomic profile](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SYN-0018 — Biological-AI SF2 reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SRC-0034 — ProteinGym benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact
  locators above.
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md), exact
  locators above.
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md), exact
  locators above.
