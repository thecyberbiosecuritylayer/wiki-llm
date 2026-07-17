---
id: GOV-0023
type: governance
title: UK NCSC operational-technology architecture and connectivity governance
aliases:
  - NCSC OT governance
  - NCSC definitive architecture and secure connectivity principles
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0045
jurisdictions:
  - United Kingdom
  - multinational-contributor-context
issuer: United Kingdom National Cyber Security Centre
document_type: principles-based-ot-cybersecurity-guidance
version: current collection with 2025 definitive-view and 2026 secure-connectivity PDFs
publication_date: 2024-03-18
adoption_date: unknown-no-universal-adoption-date
effective_date: not-applicable-nonbinding-guidance
instrument_status: official-collection-live-checked-2026-07-12
binding_status: nonbinding-goals-not-minimum-requirements
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0045
    claim_id: GOV-0023-C01
    evidence:
      - source: SRC-0045
        locator: "Current NCSC OT collection; definitive-view PDF pp. 1-4 and copyright p. 32; secure-connectivity PDF pp. 1-4 and copyright p. 33"
tags:
  - governance
  - united-kingdom
  - ncsc
  - operational-technology
  - connectivity
  - supply-chain
  - nonbinding-guidance
---

# UK NCSC operational-technology architecture and connectivity governance

## Status, authorship and scope

The retained official collection includes a 2025 definitive-architecture guide
and a 2026 secure-connectivity guide. UK NCSC is producer; Australian,
Canadian, U.S., German, Dutch and New Zealand agencies are contributors to the
same publications. This is one UK-primary/multinational-partner technical
lineage, not separate instruments adopted by eight jurisdictions.

> **Claim record — GOV-0023-C01 | source-report**
> **Claim:** The current NCSC OT collection presents two linked principles-
> based guides produced by UK NCSC with the same named multinational
> contributor group and directed to organizations deploying or operating OT.
> **Claim status:** active
> **Scope:** Official publication, authorship and audience checked 2026-07-12;
> not national adoption by each contributor, law, standard or independent
> source multiplication.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> `SRC-0045-C01/C02/C09`; collection and both PDFs, pp. 1-4.
> **Basis / limits:** Producer, contributors and collection relationship are
> direct; they establish one coordinated lineage.

## Binding character

Both PDFs explicitly say their principles describe goals rather than minimum
requirements. Imperative wording such as `should` and `must ensure` is design
guidance within the principles, not a standalone regulatory obligation. A
sector regulator or contract may separately require a pattern, but that force
must come from the separate instrument.

> **Claim record — GOV-0023-C02 | analytic-judgment**
> **Claim:** NCSC definitive-view and secure-connectivity principles are
> nonbinding design goals, not minimum compliance requirements, and their
> imperative wording is not converted into GMP or NIS law.
> **Claim status:** active
> **Scope:** Instrument-force interpretation; not legal advice or a claim that
> no related control can be mandatory under another instrument.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> `SRC-0045-C03`; definitive-view PDF p. 4 and secure-connectivity PDF p. 4,
> `Principles-based guidance`.
> **Basis / limits:** Goals-not-minimum wording is direct. External legal or
> contractual force requires separate provenance.

## Requirements or recommendations

The guidance recommends a definitive OT record, risk ownership, asset and
connectivity inventories, third-party dependency analysis, change control,
segmentation, secure/authenticated protocols, centralized remote access,
monitoring and tested isolation planning. It spans safety, availability and
integrity but remains generic to OT rather than biomanufacturing quality/GMP.

> **Claim record — GOV-0023-C03 | source-report**
> **Claim:** NCSC's governance model assigns OT owners a documented risk,
> architecture, asset/connectivity, supplier, access, monitoring and isolation
> decision chain across greenfield and brownfield systems.
> **Claim status:** active
> **Scope:** Recommended generic OT governance; not a binding duty, complete
> biomanufacturing architecture, deployed control or assurance result.
> **As of:** 2025-2026 guidance package.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> `SRC-0045-C04/C08`; definitive-view PDF pp. 3-11 and 19-31;
> secure-connectivity PDF pp. 5-32.
> **Basis / limits:** Recommended roles and records are direct; implementation
> and performance are not represented.

## Exceptions and operational interpretation

The guidance allows risk-based prioritization and compensating controls where
obsolete assets or time-critical safety functions make ideal controls
infeasible. It preserves documented insecure-protocol exceptions, temporary
containment during replacement, and bounded isolation exemptions where loss
of a critical data flow could create unsafe or national-level impact.

> **Claim record — GOV-0023-C04 | source-report**
> **Claim:** NCSC couples desired end states with explicit operational
> constraints, requiring documented risk acceptance/compensating controls and
> bounded safety/availability exceptions rather than unconditional control
> deployment.
> **Claim status:** active
> **Scope:** Guidance exception logic; not approval of a specific exception,
> legal exemption, successful test or risk elimination.
> **As of:** 2025-2026 guidance package.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> `SRC-0045-C08`; secure-connectivity PDF pp. 5-8, 17-22 and 30-32;
> definitive-view PDF pp. 25-30.
> **Basis / limits:** Conditions and tradeoffs are direct and remain
> organization-specific.

## NIS reference boundary

The collection says NCSC has published guidance to help regulators and
operators of essential services adhere to the UK NIS Regulations. That
reference is contextual. The retained package is not the NIS legal text,
does not establish which organization is regulated, and provides no proof of
NIS compliance, enforcement or adoption of these principles.

> **Claim record — GOV-0023-C05 | analytic-judgment**
> **Claim:** The collection's reference to NIS-supporting guidance does not
> make `GOV-0023` the NIS Regulations, prove regulatory applicability or give
> the NCSC principles binding/adopted status.
> **Claim status:** active
> **Scope:** Citation/force/adoption boundary; not an interpretation of the
> NIS Regulations or an operator-of-essential-services determination.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> retained collection introduction and `SRC-0045-C03/C09`.
> **Basis / limits:** The page describes a helping role and links outward; the
> legal instrument and applicability evidence are not retained here.

## Adoption, currentness and source independence

Live collection inclusion and current PDF availability show publication and
official maintenance context. They do not measure operator uptake,
implementation, conformity or effectiveness. The two PDFs, wrapper and seven
partner contributors remain one coordinated technical lineage. NIST SP
800-82r3 is a separate U.S. technical lineage; ICH Q13 is a separate quality-
governance lineage.

> **Claim record — GOV-0023-C06 | analytic-judgment**
> **Claim:** Observable adoption is limited to official NCSC publication and
> contributor endorsement of the documents; operator implementation and
> outcome remain unknown, and wrapper/PDF/partner roles are not multiplied
> into independent governance anchors.
> **Claim status:** active
> **Scope:** Adoption/currentness/source-count field; not a claim that no
> operator follows the principles.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> `SRC-0045-C01`-`C03/C09`; shared authorship and collection structure.
> **Basis / limits:** Publication and endorsement are direct; uptake and
> effectiveness evidence are absent from the package.

## Cyberbiosecurity relevance and control mapping

NCSC provides the generic OT-cyber side needed to interpret integrity,
connectivity, insider and supplier risks in biomanufacturing. It does not
govern product quality/release and needs reconciliation with MHRA/FDA/ICH
quality instruments. Generic OT architecture also does not fill literal QMS-
software/ERP gaps or SF3 assurance.

> **Claim record — GOV-0023-C07 | analytic-judgment**
> **Claim:** `GOV-0023` can supply the OT-cyber instrument role for
> `BMO-GR` reconciliation and threat-model predicates for `BMO-TV`, but it
> cannot alone pass `BMO-SD`, `BMO-AE` or prove compliance/effectiveness.
> **Claim status:** superseded
> **Scope:** Candidate frozen-rubric governance/control contribution; not
> score arithmetic, legal equivalence or sector deployment evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> `SRC-0045-C04`-`C10`; frozen BMO rows in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Generic guidance must be stitched to independent
> manufacturing/quality evidence; missing literals and SF3 results remain.
> **Superseded by:** `SYN-0028-C04/C06/C07`, after sector/governance
> reconciliation and adjacent-cell audit.

## Evidence and safety boundary

> **Claim record — GOV-0023-C08 | analytic-judgment**
> **Claim:** The local governance page preserves nonbinding force, adoption
> uncertainty and defensive control abstraction without exposing live assets,
> credentials, exploitable versions, commands, setpoints or facility routes.
> **Claim status:** active
> **Scope:** Local page; not legal advice or a safety assessment of the public
> guidance and linked external resources.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content; `GOV-0023-C01`-`C07`.
> **Basis / limits:** Only governance-level evidence required for defensive
> comparison is retained.

## Related pages

- [SRC-0045 — NCSC OT source package](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md)
- [GOV-0008 — NIST SP 800-82r3 OT guidance](gov-0008-nist-sp-800-82r3-ot-security-2023.md)
- [GOV-0016 — ICH Q13 quality governance](gov-0016-ich-q13-continuous-manufacturing.md)
- [SYN-0028 — BMO reconciliation](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md), at the exact locators above.
