---
id: GOV-0005
type: governance
title: US Data Security Program for country-of-concern and covered-person data access
aliases:
  - DOJ Data Security Program governance
  - 28 CFR Part 202 governance
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0015
jurisdictions:
  - United States
issuer: US Department of Justice, National Security Division
document_type: federal-regulation-with-incorporated-security-requirements
version: Current corrected Part 202 checked 2026-07-12
publication_date: 2025-01-08
effective_date: 2025-04-08
binding_status: binding-federal-regulation-subject-to-scope-exceptions-and-current-text
implementation_status: unknown
enforcement_event_status: none-in-source
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: GOV-0005-C01
    evidence:
      - source: SRC-0015
        locator: "Final rule DATES and codified Part 202, PDF pp. 1, 72–96 / 90 FR 1636, 1707–1731; correction, 90 FR 16466–16467; current eCFR checked 2026-07-12"
tags:
  - governance
  - united-states
  - binding-regulation
  - covered-person-data-access
  - omics
  - audit
---

# US Data Security Program for country-of-concern and covered-person data access

## Status and force

28 CFR Part 202 is a binding U.S. federal transaction regime, not voluntary
guidance, a technical standard or a general cybersecurity baseline. It applies
through defined data, actor, access, knowledge, transaction and exception
conditions. The current page incorporates the April 2025 correction and does
not reproduce the local January PDF's erroneous §202.408 reference.

> **Claim record — GOV-0005-C01 | source-report**
> **Claim:** Corrected 28 CFR Part 202 is an effective federal regulation that
> prohibits or restricts defined access transactions involving government-
> related data or bulk U.S. sensitive personal data, including bounded human-
> omic and biospecimen classes.
> **Claim status:** active
> **Scope:** Current instrument character through 2026-07-12; not a coverage
> determination or legal advice for a particular party.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> final rule `DATES`, §§202.101, .201, .205–.206, .210, .222–.224 and
> .301–.401, PDF pp. 1, 72–85 / 90 FR 1636, 1707–1720; correction,
> 90 FR 16466–16467; current eCFR check.
> **Basis / limits:** Force, scope architecture and corrected current wording
> are direct. Entity- and transaction-specific analysis requires facts and
> authorities not represented here.

## Duty holders, rights holders and authorities

Primary transaction duties fall on defined U.S. persons. The regime also
defines countries of concern, covered persons, foreign persons, counterparties
and ownership/residence relationships. DOJ/NSD administers the programme;
CISA supplies incorporated security requirements; other named federal
authorities retain their own roles. Data subjects can be affected stakeholders,
but Part 202 is framed as a national-security access regime rather than an
individual-rights code.

> **Claim record — GOV-0005-C02 | source-report**
> **Claim:** Part 202 allocates primary classification, diligence, control,
> audit, record and reporting responsibility to defined U.S. persons while
> differentiating covered counterparties and preserving other federal
> authorities.
> **Claim status:** active
> **Scope:** Institutional allocation in Part 202, not a complete map of every
> privacy, health, research or investment-law duty.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.103–.104, .211, .230, .256, .401, .601, .701 and Subparts J–K,
> PDF pp. 72–95 / 90 FR 1707–1730.
> **Basis / limits:** Roles and responsibility classes are explicit. The page
> does not reproduce operational contact data, country-specific examples or
> claim universal extraterritorial scope.

## Governance lifecycle and modalities

The high-level governance lifecycle is:

`classify data/actors/transaction → prohibit or conditionally authorize →
apply controls and diligence → audit/retain/report → license/investigate/
enforce where applicable`.

Prohibited human-omic/derivable-biospecimen transactions cannot be made
permissible merely by adding the restricted-transaction controls. Exceptions
are activity- and condition-specific, not a blanket research or clinical safe
harbor.

> **Claim record — GOV-0005-C03 | analytic-judgment**
> **Claim:** The regime uses distinct governance modalities—prohibition,
> conditional authorization, exception, license, reporting and enforcement—so
> a control crosswalk or audit plan cannot by itself establish that a
> transaction is authorized or compliant.
> **Claim status:** active
> **Scope:** Structural interpretation of Part 202's modalities; not a legal
> conclusion about an actual transaction.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> Subparts C–E and H–M, PDF pp. 82–96 / 90 FR 1717–1731.
> **Basis / limits:** Each modality is explicit; the lifecycle synthesis is a
> safe editorial model. It omits detailed examples and cannot replace current
> legal analysis.

## Assurance and enforcement boundary

The programme requires policies, due diligence, annual independent audit,
records and differentiated reports. Those are binding assurance mechanisms.
They are not evidence that any organization implemented them, that an auditor
found them effective or that DOJ enforced them in a completed case.

> **Claim record — GOV-0005-C04 | analytic-judgment**
> **Claim:** Part 202 supplies strong assurance and enforcement design but no
> implementation, inspection, audit-result, violation or causal-effectiveness
> record; all such evidence states remain unknown for this wiki transaction.
> **Claim status:** active
> **Scope:** Evidence maturity of this legal source lineage.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.1001–.1306, PDF pp. 93–96 / 90 FR 1728–1731; `SRC-0015-C09`.
> **Basis / limits:** Requirements and powers are direct. No completed
> organization-level record appears in the final rule or its correction.

## Exact governance relationships

- [RSK-0011](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md) is
  `governed-by` this regime only when its data, actor, access, transaction and
  knowledge conditions are met.
- [CTL-0008](../controls/ctl-0008-restricted-data-transaction-controls.md) records
  the restricted-transaction safeguards and assurance duties; it does not
  authorize the prohibited human-omic/biospecimen class.
## Safety and legal-use boundary

No location polygon, personal record, evasion scenario, system topology or
configuration recipe is reproduced. This page is a source-backed governance
map, not legal advice.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [SRC-0015 — DOJ final rule and correction chain](../sources/src-0015-us-doj-data-security-program-2025.md)
- [RSK-0011 — Part 202 regulated access branches](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [GOV-0006 — EU EHDS governance](gov-0006-eu-ehds-regulation-2025.md)
- [SYN-0004 — US–EU human-omics and health-data governance](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)
- [SYN-0008 — Five-context governance reconciliation](../syntheses/syn-0008-global-us-eu-uk-canada-governance-reconciliation.md)

## Sources

- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md), final rule,
  official correction, current eCFR verification and incorporated CISA
  requirements at the locators in the claims above.
