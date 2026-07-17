---
id: CTL-0008
type: control
title: Covered data-transaction prohibition, access and assurance controls
aliases:
  - Part 202 restricted transaction controls
  - CISA restricted transaction security requirements
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0015
sensitivity: public
dual_use: low
control_status: binding-transaction-classification-and-restricted-access-controls
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: CTL-0008-C01
    evidence:
      - source: SRC-0015
        locator: "Corrected 28 CFR §§202.248 and .401; final-rule PDF pp. 80, 84–85 / 90 FR 1715, 1719–1720; CISA requirements, pp. 1–6"
  - predicate: mitigates
    target: RSK-0011
    claim_id: CTL-0008-C02
    evidence:
      - source: SRC-0015
        locator: "28 CFR §§202.301–.401 and CISA requirements, Background and §§I–II, pp. 1–6"
  - predicate: detects
    target: RSK-0011
    claim_id: CTL-0008-C02
    evidence:
      - source: SRC-0015
        locator: "CISA requirements §I.A.7, §I.B.3 and §I.C, pp. 3–4"
  - predicate: contains
    target: RSK-0011
    claim_id: CTL-0008-C02
    evidence:
      - source: SRC-0015
        locator: "CISA requirements §I.A.7 and §I.B–C, pp. 3–4"
  - predicate: recovers
    target: RSK-0011
    claim_id: CTL-0008-C02
    evidence:
      - source: SRC-0015
        locator: "CISA requirements §I.A.7 and §I.B.3, pp. 3–4"
  - predicate: governed-by
    target: GOV-0005
    claim_id: CTL-0008-C01
    evidence:
      - source: SRC-0015
        locator: "Corrected 28 CFR §§202.248 and .401; Subparts J–K"
tags:
  - access-control
  - restricted-transactions
  - data-governance
  - audit
  - logging
  - covered-person-data-access
---

# Covered data-transaction prohibition, access and assurance controls

> Binding Part 202 transaction-decision and restricted-access control design
> when the full predicates apply. Prohibition is the preventive mechanism for
> the human-omic/derivable-biospecimen limb; the incorporated CISA safeguards
> apply only to eligible restricted transactions. This is not a comprehensive
> cybersecurity baseline.

## Applicability and legal boundary

Corrected §202.401(a) conditionally authorizes restricted vendor, employment
and investment transactions only when the U.S. person complies with the
security requirements defined by §202.248 and all other applicable Part 202
duties. The human-omic/derivable-biospecimen prohibition is upstream of these
controls.

> **Claim record — CTL-0008-C01 | source-report**
> **Claim:** Part 202 makes the incorporated CISA controls and other applicable
> duties conditions for restricted-transaction authorization, while prohibited
> human-omic/derivable-biospecimen transactions are not converted into
> restricted transactions by implementing those controls.
> **Claim status:** active
> **Scope:** Corrected federal control requirement; not legal advice or a
> compliance finding for a named transaction.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.248, .303 and corrected .401, PDF pp. 80, 83–85 / 90 FR 1715,
> 1718–1720; correction, 90 FR 16466–16467; CISA requirements, pp. 1–6.
> **Basis / limits:** Modalities and cross-reference are explicit. Coverage,
> exception and license analysis remains fact-specific.

## Control functions and exact scenario edges

| Function | Exact `RSK-0011` edge | Intended mechanism | Evidence boundary |
| --- | --- | --- | --- |
| Prevent/classify | proposed transaction → prohibited/restricted decision | classify data, actors, access and transaction; stop prohibited paths | Classification can be wrong and is not itself an access safeguard |
| Prevent/protect | restricted transaction → covered-person access | organization/system governance, identity/access and data-level measures | Required design, not observed deployment |
| Detect | access attempt/state → review | access/security logging and annual data-risk reassessment | No detection coverage or rate |
| Contain/respond | suspect access/control failure → bounded response | incident-response planning, credential/access action and retained evidence | Plan requirement, not an exercised response |
| Recover | affected system/control state → renewed authorized operation | response/recovery use of logs and corrected access/control state | No recovery-time or trustworthy-state test |
| Assure | selected controls → accountable authorization basis | due diligence, certified policy, independent audit, records/reporting | Audit requirement, not a positive audit result |

> **Claim record — CTL-0008-C02 | analytic-judgment**
> **Claim:** `CTL-0008` conditionally mitigates `RSK-0011` through transaction
> classification/prohibition and, only for its restricted-data limb, access
> denial; it conditionally detects, contains and supports recovery for that
> restricted limb through logging/risk assessment and incident planning;
> current evidence establishes design only.
> **Claim status:** active
> **Scope:** Restricted transactions within Part 202, not every genomic system,
> foreign access path or cybersecurity risk.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.301–.401 and .1001–.1104, PDF pp. 82–95 / 90 FR 1717–1730;
> CISA requirements, Background and §§I–II, pp. 1–6.
> **Basis / limits:** Functions and intended access objective are direct; the
> exact-edge synthesis is editorial. No implementation, attack, detection,
> response or recovery test is supplied.

## High-level safeguard families

- accountable asset, risk and supplier governance;
- covered-system identity, logical/physical access and logging;
- scoped vulnerability and incident-response practices;
- transaction-specific data-risk assessment;
- data minimization/masking, encryption/key separation, privacy-enhancing
  processing or access denial selected to meet the regulated objective;
- diligence, policy certification, independent audit, records and reporting.

This page deliberately omits network topology, configuration values,
government-location data and operational evasion examples.

## Assurance ladder

| Level | Status | Basis |
| --- | --- | --- |
| Required/recommended | Binding where Part 202 classifies the transaction as restricted | Corrected §§202.248/.401 and incorporated CISA requirements |
| Implemented | Unknown | No entity record in source |
| Tested | Unknown | Audit is required, but no completed test/audit result is present |
| Effective | Unknown | No measured access-prevention or outcome comparison |
| Independently evaluated | Unknown | The rule requires an independent auditor; it does not supply an evaluation |

> **Claim record — CTL-0008-C03 | analytic-judgment**
> **Claim:** Mandatory annual independent audit and effectiveness assessment
> are assurance requirements, not evidence that a safeguard was implemented,
> tested, found effective or independently validated in practice.
> **Claim status:** active
> **Scope:** Evidence maturity for this transaction, not a claim that no audit
> has occurred anywhere.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.1001–.1002 and .1101, PDF pp. 93–94 / 90 FR 1728–1729;
> audit discussion, PDF pp. 62–63 / 90 FR 1697–1698.
> **Basis / limits:** Required audit scope is direct. Implementation and audit
> outcomes require separate organization- or regulator-specific records.

## Failure modes and tradeoffs

- a prohibited transaction cannot be cured by technical controls;
- classification depends on data/volume, actor, access, knowledge, transaction
  and exception facts;
- CISA states that its requirements are not a comprehensive cyber programme;
- a selected combination can fail its regulated access-prevention objective;
- minimization, privacy-enhancing processing and operational utility require
  transaction-specific assessment; and
- logs, policies and records support accountability but do not prove lawful or
  effective operation.

> **Claim record — CTL-0008-C04 | source-report**
> **Claim:** CISA expressly limits the requirements to the restricted-
> transaction risk objective, allows transaction-appropriate combinations of
> data-level measures and states that a combination shown insufficient to
> prevent covered access is invalid for protecting future access.
> **Claim status:** active
> **Scope:** Source-defined limitation/failure rule, not a reported deployment
> failure or universal product requirement.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> CISA requirements, Background and In General, pp. 1–2.
> **Basis / limits:** Purpose, flexibility and failure condition are direct.
> No tested combination, failure rate or remediation outcome is reported.

## Related pages

- [SRC-0015 — DOJ final rule and correction chain](../sources/src-0015-us-doj-data-security-program-2025.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [RSK-0011 — Part 202 regulated access branches](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md)
- [CTL-0002 — Genomic-data risk management](ctl-0002-genomic-data-risk-management.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [CTL-0009 — EHDS health-data and EHR safeguards](ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [SYN-0004 — US–EU human-omics and health-data governance](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)

## Sources

- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md), corrected
  §§202.248/.401, Subparts J–K and incorporated CISA requirements.
