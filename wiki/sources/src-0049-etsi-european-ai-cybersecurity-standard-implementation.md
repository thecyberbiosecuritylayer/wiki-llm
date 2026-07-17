---
id: SRC-0049
type: source
title: ETSI European AI cybersecurity standard and implementation-guide package 2025–2026
aliases:
  - ETSI EN 304 223
  - ETSI TR 104 128
  - ETSI baseline cybersecurity requirements for AI
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-european-standard-and-informative-implementation-guide-package
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/etsi-en-304223-v2.1.1-2025.pdf
raw_bytes: 109653
sha256: 1ef542acf1fac7f108aa0b3c8548d91d82395fe026f0036bffe7f1f32456d21a
raw_components:
  - path: ../../raw/etsi-tr-104128-v1.1.1-2025.pdf
    role: published-informative-implementation-guide
    bytes: 701782
    sha256: 824c2ef6720ea30e38c0b64ec7ac46e2d5a5ea6e597f0b69029e4e2605900e05
  - path: ../../raw/etsi-en-304223-work-item-current-2026-07-12.html
    role: current-en-work-item-and-publication-record
    bytes: 15135
    sha256: c100ba5bba0caa2f1e3b29348d32b698888c805e6bb781c619be89a1dfc42907
  - path: ../../raw/etsi-tr-104128-work-item-current-2026-07-12.html
    role: current-published-tr-work-item-record
    bytes: 15250
    sha256: fb7e15faf1def03684d9339acbeea74343e2a656ba7ff086c9b1d8aae3788665
  - path: ../../raw/etsi-tr-104128-update-work-item-current-2026-07-12.html
    role: current-unpublished-tr-update-work-item-record
    bytes: 13810
    sha256: 8ada877883a40934ae85d26c50c947c74f47c10a3449e7ba19651993a06210d3
canonical_url: https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf
tr_url: https://www.etsi.org/deliver/etsi_tr/104100_104199/104128/01.01.01_60/tr_104128v010101p.pdf
en_work_item_url: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74952
tr_work_item_url: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=73753
tr_update_work_item_url: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=78256
accessed: 2026-07-12
issuer: European Telecommunications Standards Institute
en_version: 2.1.1
en_publication_date: 2025-12-12
tr_published_version: 1.1.1
tr_publication_date: 2025-05-19
tr_update_state: early-draft-2.0.2-not-ready-for-download
jurisdictions:
  - European standardization instrument; cross-sector and internationally oriented
tags:
  - artificial-intelligence
  - ai-security
  - model-lifecycle
  - mlops
  - containers
  - model-registry
  - data-drift
  - confidentiality
  - supply-chain
  - standards
---

# ETSI AI cybersecurity standard and implementation-guide package 2025–2026

## Identity, acquisition and static review

The controlling artifact is ETSI EN 304 223 V2.1.1, *Securing Artificial
Intelligence (SAI); Baseline Cyber Security Requirements for AI Models and
Systems*. The package also retains the published ETSI TR 104 128 V1.1.1
implementation guide and three official work-item snapshots needed to keep
the EN/TR version relationship explicit.

- The EN is 109,653 bytes and 16 physical/printed pages; the TR is 701,782
  bytes and 74 physical/printed pages. The five-object package totals 855,630
  bytes.
- Every object was retrieved twice on 2026-07-12. Each pair was byte-identical;
  the temporary comparison copies were discarded after SHA-256 verification.
- Text extraction covered all 90 PDF pages. Every page cited below was
  manually reviewed, and the TR lifecycle figure on p. 14 was rendered and
  visually checked.
- Both PDFs are optimized, unencrypted, untagged PDF 1.7 files. `pdfinfo`
  reports no form or JavaScript; `pdfdetach` reports no embedded files.
  `pdfsig` reported no signature after an NSS initialization warning, so this
  is not successful cryptographic authentication.
- The three ISO-8859 work-item snapshots each contain two HTML forms and no
  script, iframe, object or embed element. They were inspected only as static
  text; no form was submitted.

> **Claim record — SRC-0049-C01 | artifact-observation**
> **Claim:** The retained 855,630-byte package contains the complete published
> EN V2.1.1, complete published TR V1.1.1 and three hash-verified current
> work-item records; all ten acquisition requests resolved into five
> byte-identical repeat pairs.
> **Claim status:** active
> **Scope:** Artifact identity, pagination, retrieval repeatability and static
> component review; not digital-signature authentication, conformance testing,
> legal adoption or runtime safety.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Local objects, byte counts and SHA-256 values in frontmatter;
> complete EN pp. 1–16; complete TR pp. 1–74; all three work-item snapshots.
> **Basis / limits:** Bytes and static properties are direct. Official ETSI
> hosting supports provenance, but related ETSI artifacts remain one
> institutional/normative lineage rather than independent corroborators.

## Current version, document force and conflict boundary

The EN work item `REN/SAI-0022` records publication on 2025-12-12, latest
version 2.1.1, and describes the EN as a transposition of ETSI TS 104 223
V1.1.1 with feedback implemented. The EN foreword records adoption on
2025-12-08. The work-item record says `Harmonised Standard: No`; the document
does not itself create a generally binding legal obligation.

The published TR work item `DTR/SAI-0012` records publication on 2025-05-19,
version 1.1.1. Its scope is guidance for meeting the earlier ETSI TS 104 223,
and TR clause 4.1, p. 14, likewise identifies the TS as its target. The newer
work item `RTR/SAI-0023` existed on 2026-07-12 specifically to update the guide
for EN 304 223 and associated conformance tests. Its current state was `Early
draft (2026-07-01)`, latest version `2.0.2 Draft`, and `Standard Not Ready For
Download`.

Accordingly, this wiki treats:

- EN 304 223 V2.1.1 as the current published requirements text;
- TR 104 128 V1.1.1 as informative implementation evidence for the older TS
  provision family; and
- the unpublished TR V2.0.2 work item only as current version-status evidence,
  never as imported requirements or guidance.

> **Claim record — SRC-0049-C02 | source-report**
> **Claim:** EN 304 223 V2.1.1 is the current published European Standard in
> this package, while TR 104 128 V1.1.1 is a published informative guide tied
> to the predecessor TS and its EN-aligned V2.0.2 replacement remained an
> unavailable early draft on 2026-07-12.
> **Claim status:** active
> **Scope:** ETSI publication/version/force relationship; not legal advice,
> national transposition, certification, organization-level compliance or a
> claim that draft content will remain unchanged.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** EN Foreword, p. 4; EN work item `REN/SAI-0022`; TR clause 4.1,
> p. 14; published TR work item `DTR/SAI-0012`; update work item
> `RTR/SAI-0023`.
> **Basis / limits:** Status and document relationships are direct ETSI
> statements. `Shall` in an EN is normative within the standard; it is not
> silently converted into statute, regulatory mandate or proof of adoption.

## Scope and lifecycle model

EN clause 1 covers baseline security requirements for AI models and systems,
including deep neural networks and generative AI. It expressly excludes
academics creating and testing systems only for research when those systems
will not be deployed. The Introduction separates five phases: secure design,
secure development, secure deployment, secure maintenance and secure end of
life. Its note maps them to ISO/IEC 22989 design/development, deployment,
operations/monitoring and retirement stages.

Clause 4 distinguishes Developers, System Operators, Data Custodians,
End-users and Affected Entities. A single organization can hold multiple
roles. This role allocation and the research-only exclusion matter when the
generic standard is stitched to biological research: it applies directly to
the deployed-system subset, not automatically to every exploratory notebook,
benchmark or academic model.

> **Claim record — SRC-0049-C03 | source-report**
> **Claim:** The EN supplies an explicit deployed-AI lifecycle from design and
> development through deployment, operations/monitoring and retirement, with
> named developer, operator, custodian and user roles.
> **Claim status:** active
> **Scope:** Cross-sector AI systems intended for deployment; not pure
> research-only systems, a biological-AI taxonomy, one implemented lifecycle
> or proof that the allocated roles operate effectively.
> **As of:** EN V2.1.1, 2025-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** EN Introduction, p. 5; Scope, p. 6; inference/training
> definitions, pp. 7–8; stakeholder definitions, pp. 9–10; TR clause 4.1 and
> Figure 4.1-1, p. 14.
> **Basis / limits:** Phases, mapping and roles are direct. The TR figure is a
> same-lineage illustration, not a separately observed deployment.

## Lifecycle requirements and implementation examples

The EN joins previously missing post-validation states without claiming that
they have been implemented:

| Lifecycle function | Controlling EN locator | Informative TR detail |
| --- | --- | --- |
| Provenance and lifecycle record | `5.1.2-3`, p. 10; `5.2.4`, p. 13 | `6.2.4`, p. 24: MLOps audit trail and versioned models/datasets/prompts |
| Validation before release | `5.2.5`, pp. 13–14 | testing examples throughout `6.9`, pp. 54–59 |
| Deployment | `5.3`, p. 14 | `6.10`, pp. 60–62 |
| Update, retrain and version | `5.4.1`, p. 14 | `6.11`, pp. 63–65: patching, CI/CD, rollback, retraining and versioned APIs |
| Production monitoring | `5.4.2`, p. 15 | `6.12`, pp. 65–69: logging, data/model/concept drift, error rate and bias |
| Retirement/disposition | `5.5.1`, p. 15 | `6.13`, pp. 69–70: secure transfer, disposal and decommission |

The requirements distinguish pre-deployment testing, ongoing maintenance and
end of life. They do not prescribe a biological validation protocol, prove a
successful update or require that every deployment use the TR's example tools.

> **Claim record — SRC-0049-C04 | source-report**
> **Claim:** The current EN directly requires or recommends auditable
> lifecycle records, pre-deployment testing, secure deployment, update and
> major-version evaluation, production logging/monitoring, drift detection,
> and secure model/data decommission or disposal.
> **Claim status:** active
> **Scope:** Requirement/control functions and published implementation
> examples; not a deployed system, completed audit, successful rollback,
> biological validation or effectiveness result.
> **As of:** EN V2.1.1, 2025-12; TR V1.1.1, 2025-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Exact EN and TR locators in the table above.
> **Basis / limits:** EN provisions are direct normative text. TR details are
> illustrative and tied to the predecessor TS; they cannot increase the EN's
> force or demonstrate implementation.

## Assets, infrastructure and trust boundaries

The EN requires an inventory of assets and their interdependencies,
authentication/version control, protection of confidential training data or
weights, secure APIs, dedicated development/model-tuning environments,
least-privilege separation, software supply-chain processes and appropriate
cloud agreements. Its generic requirements do not name every implementation
class needed by the wiki's biological-AI system map.

The informative TR makes several missing classes literal:

- external components include operating systems, libraries, **container
  images**, programming packages, models and datasets (`6.2.5`, p. 25);
- versioned assets can use package repositories and a **model registry**, with
  RBAC/MFA and API/CI-mediated access (`6.5.2`, pp. 38–39);
- separated development/test/production examples use a model registry and
  containerization (`6.6.3`, p. 44);
- API gateways, cloud contracts and versioned interfaces are discussed in
  `6.6.2–6.6.6`, pp. 42–46.

> **Claim record — SRC-0049-C05 | source-report**
> **Claim:** The ETSI package directly represents asset/dependency inventory,
> APIs, cloud, separated environments and identity/least-privilege boundaries,
> while the informative guide explicitly adds packages, container images and
> model registries.
> **Claim status:** active
> **Scope:** Generic system classes and control boundaries; not one deployed
> topology, SBOM/ML-BOM, IAM test, container image validation or biological
> laboratory architecture.
> **As of:** 2026-07-12 package review.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** EN `5.1.2-4/6`, pp. 10–11; `5.2.1–5.2.3`, pp. 12–13; TR
> `6.2.5`, p. 25; `6.5.2`, pp. 38–39; `6.6.2–6.6.6`, pp. 42–46.
> **Basis / limits:** EN classes and boundaries are normative; `container
> images` and `model registry` are literal but informative TR examples. A
> registry is not silently assumed to store both governance metadata and model
> binaries.

## Defensive threat and failure envelope

The EN addresses adversarial inputs/system failure, data poisoning, model
inversion, membership inference, confidential training data/weights, software
supply chains and unexpected behavior over time. The TR's threat overview
adds model tampering, privacy attacks, information disclosure, training-data
extraction and excessive agency. Its examples connect dependencies,
confidentiality leakage, false positives/negatives, bias, error rate and
data/model/concept drift to defensive assessment, monitoring and human
oversight.

> **Claim record — SRC-0049-C06 | source-report**
> **Claim:** At defensive abstraction, the package covers poisoning and model
> tampering, confidentiality/privacy leakage, software dependencies, bias,
> drift, error and unsafe/excessive automation.
> **Claim status:** active
> **Scope:** Generic threat, failure and control categories; not biological
> consequence, exploit procedure, attack success, prevalence, attribution or
> control effectiveness.
> **As of:** 2026-07-12 package review.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** EN Introduction, p. 5; `5.1.2–5.1.4`, pp. 10–11;
> `5.2.1–5.2.5`, pp. 12–14; `5.4.2`, p. 15; TR threat overview, pp. 15–16;
> `6.2.5–6.2.8`, pp. 25–28; `6.4.1–6.4.3`, pp. 33–35; `6.12.2–6.12.4`,
> pp. 67–69.
> **Basis / limits:** Categories are literal. Operational attack detail is not
> reproduced, and possible harm is not converted into an incident.

## Independence, biological stitch and non-promotion boundary

EN 304 223, TR 104 128 and their work items constitute **one ETSI
standardization lineage**. Multiple artifacts and `shall` provisions do not create
multiple independent evidence lineages. The package is also generic AI: a
biological-AI conclusion requires a separate biological source and explicit
mapping of the biological system to the EN's deployed-system scope.

> **Claim record — SRC-0049-C07 | analytic-judgment**
> **Claim:** This package can independently supply a current generic
> deployment-to-retirement, infrastructure and defensive-threat baseline for
> a biological-AI synthesis, but it cannot establish biology-specific scope,
> a real deployment, implementation success or effectiveness by itself.
> **Claim status:** active
> **Scope:** Source-lineage and cross-domain applicability classification; not
> a score change or a claim that the standard is irrelevant to life sciences.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0049-C02`–`C06`; EN Scope, p. 6; shared ETSI work-item
> relationships and supporting organizations.
> **Basis / limits:** Generic lifecycle and security predicates are direct.
> Biological applicability and independent corroboration must come from a
> materially separate lineage such as `SRC-0050` or `SRC-0051`.

## Safety abstraction

This page retains lifecycle, architecture, identity, threat and control
classes only. It omits exploit sequences, live targets, credentials, endpoint
details, model weights, prompts and biological design instructions.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [GOV-0024 — ETSI governance](../governance/gov-0024-etsi-european-ai-cybersecurity-standard.md)
- [HAZ-0005 — Drift/bias/error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [THR-0003 — Adversarial AI threat](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md)
- [TEC-0002 — AI transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0050 — Oncology AI governance implementation](src-0050-stetson-responsible-ai-governance-oncology-2025.md)
- [SRC-0051 — Reproducible biomedical MLOps](src-0051-mlf-core-reproducible-biomedical-mlops-2023.md)
- [WFL-0013 — Secure biological-AI model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps infrastructure and trust boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)

## Sources

- ETSI EN 304 223 V2.1.1 and ETSI TR 104 128 V1.1.1, local immutable
  objects and exact locators above.
- ETSI work items `REN/SAI-0022`, `DTR/SAI-0012` and `RTR/SAI-0023`, local
  static snapshots retained 2026-07-12.
