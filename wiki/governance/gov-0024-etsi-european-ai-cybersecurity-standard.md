---
id: GOV-0024
type: governance
title: ETSI European AI cybersecurity standard and guidance governance
aliases:
  - ETSI EN 304 223 governance
  - European baseline cybersecurity requirements for AI
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0049
  - SRC-0050
  - SRC-0051
jurisdictions:
  - European standardization instrument; national legal adoption not established
issuer: European Telecommunications Standards Institute
document_type: european-standard-with-informative-implementation-companion
version: EN 304 223 V2.1.1 with published TR 104 128 V1.1.1 and pending TR update
publication_date: 2025-12-12
adoption_date: 2025-12-08
effective_date: not-a-statute-or-general-regulatory-effective-date
instrument_status: current-published-en-with-ts-bound-informative-tr-and-unpublished-update
binding_status: normative-within-voluntary-standard-not-generally-binding-law
implementation_status: standard-publication-observed-organization-adoption-and-conformance-unknown
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: GOV-0024-C01
    evidence:
      - source: SRC-0049
        locator: "EN Foreword/Scope, pp. 4–6; EN clauses 5.1–5.5, pp. 10–15; ETSI work-item records"
tags:
  - governance
  - europe
  - standards
  - artificial-intelligence
  - cybersecurity
  - lifecycle
  - version-status
---

# ETSI European AI cybersecurity standard governance

## Status and force

ETSI EN 304 223 V2.1.1 is the current published European Standard in the
retained package. Its `shall` provisions are normative within the standard,
but the work-item record says it is not a harmonised standard and the artifact
does not itself create generally binding legislation. National adoption,
contractual incorporation, certification and organization-level conformance
are separate states not demonstrated here.

> **Claim record — GOV-0024-C01 | analytic-judgment**
> **Claim:** EN 304 223 V2.1.1 is a current published normative standard, not
> a generally binding law or proof that an organization or jurisdiction has
> adopted, certified or conformed to it.
> **Claim status:** active
> **Scope:** ETSI document status and force; not legal advice or a national
> standards-adoption census.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> `SRC-0049-C01/C02`; EN Foreword, p. 4; EN work item `REN/SAI-0022`.
> **Basis / limits:** Publication, adoption within ETSI and non-harmonised
> status are direct. No national implementing or conformity record is retained.

## Scope, actors and lifecycle

The EN covers AI models and systems intended for deployment, including
generative AI, and assigns roles to Developers, System Operators, Data
Custodians, End-users and Affected Entities. It expressly excludes academic
systems created and tested only for research when they will not be deployed.
The standard's five phases span design, development, deployment, maintenance
and end of life.

> **Claim record — GOV-0024-C02 | source-report**
> **Claim:** ETSI allocates security responsibilities across named AI actors
> over a design-to-retirement lifecycle while preserving a research-only,
> non-deployment exclusion.
> **Claim status:** active
> **Scope:** Cross-sector deployed-AI standard; not all academic research,
> biological-AI scope, a named operator or proof that roles are staffed.
> **As of:** EN V2.1.1.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> `SRC-0049-C03`; EN Introduction, p. 5; Scope, p. 6; actor definitions,
> pp. 9–10.
> **Basis / limits:** Scope, phases, roles and exclusion are direct. They are
> governance design rather than implementation evidence.

## Requirement and control classes

> **Claim record — GOV-0024-C03 | source-report**
> **Claim:** The EN supplies normative lifecycle requirements for risk and
> asset ownership, provenance/audit, dependency and access management,
> pre-deployment testing, deployment, controlled update, monitoring and
> retirement; the TR supplies nonbinding implementation examples.
> **Claim status:** active
> **Scope:** Standard requirement/control classes; not one mandatory toolset,
> implemented control, completed audit or effectiveness result.
> **As of:** EN V2.1.1 and TR V1.1.1 package reviewed 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> `SRC-0049-C04`–`C06`; EN clauses 5.1–5.5, pp. 10–15; TR §§6.1–6.13.
> **Basis / limits:** EN functions and TR examples are direct. The companion
> does not increase the standard's legal force or demonstrate compliance.

## Version and companion boundary

The published TR V1.1.1 implements the predecessor TS provision family. A new
TR V2.0.2 work item intended to align with the EN was only an unavailable early
draft at the cutoff. Neither the old companion nor the unpublished replacement
is treated as a second independent lineage.

> **Claim record — GOV-0024-C04 | analytic-judgment**
> **Claim:** Current governance must use the EN as controlling text, treat the
> published TR as informative predecessor-family guidance and keep the
> unavailable TR update as proposal/status evidence only.
> **Claim status:** active
> **Scope:** Version and conflict resolution through 2026-07-12; not a forecast
> of the draft's final content.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> `SRC-0049-C01/C02`; TR clause 4.1, p. 14; three current work-item records.
> **Basis / limits:** Version relationships and draft state are direct. ETSI
> artifacts remain one standardization lineage.

## Biological applicability and adoption boundary

The standard is generic AI. It becomes cyberbiosecurity-relevant only when a
biological or clinical model/system crosses its intended-deployment boundary;
NASEM, the oncology implementation and mlf-core provide those separate
biological contexts. The standard alone does not prove biological deployment,
adoption, conformance or harm reduction.

> **Claim record — GOV-0024-C05 | analytic-judgment**
> **Claim:** `GOV-0024` supplies one current independent standards-governance
> lineage for deployable AI, but biological scope, implementation and outcomes
> require separate direct sources and explicit applicability mapping.
> **Claim status:** active
> **Scope:** Evidence-lineage and cyberbio applicability boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `GOV-0024-C01`–`C04`; `SRC-0049-C07`;
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md);
> [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md);
> [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md).
> **Basis / limits:** Generic standard and biological sources are materially
> distinct. Cross-scope applicability is analytic, not a conformity finding.

> **Claim record — GOV-0024-C06 | analytic-judgment**
> **Claim:** Publication and one oncology implementation context do not
> establish organization-level adoption of the EN or independent
> effectiveness of its complete lifecycle control set.
> **Claim status:** active
> **Scope:** Adoption and assurance evidence state.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0049-C02/C07`; [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> implementation and limitations.
> **Basis / limits:** No retained conformity certificate, adoption census or
> independent outcome evaluation links the oncology programme to the EN.

## Related pages

- [SRC-0049 — ETSI source package](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [WFL-0013 — Secure model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)
- [CTL-0021 — Secure monitored controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [GOV-0025 — EU AI Act](gov-0025-eu-ai-act-life-sciences-applicability.md)
- [GOV-0026 — NIH genomic AI policy](gov-0026-nih-genomic-data-ai-use-policy.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md), exact locators above.
