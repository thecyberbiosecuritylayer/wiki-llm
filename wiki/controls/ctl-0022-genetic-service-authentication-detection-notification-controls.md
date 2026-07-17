---
id: CTL-0022
type: control
title: Consumer-genetics authentication, detection, containment and notification controls
aliases:
  - genetic-service incident control family
  - 23andMe regulatory control lessons
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
source_ids:
  - SRC-0055
  - SRC-0056
sensitivity: public
dual_use: low
control_status: case-derived-regulatory-and-current-rule-family
implementation_status: measures-reported-implemented-and-regulator-accepted-through-2024-12-31
testing_status: company-reported-exercises-and-technical-changes-not-independently-replicated
effectiveness_status: unknown
independent_evaluation_status: bounded-regulatory-implementation-review-not-outcome-effectiveness-test
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: CTL-0022-C01
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 57–117 and 198–200"
  - predicate: evidenced-by
    target: SRC-0056
    claim_id: CTL-0022-C04
    evidence:
      - source: SRC-0056
        locator: "PIPEDA sections 10.1–10.3; Canadian Regulations sections 2–6; ICO guide breach-reporting anchors"
  - predicate: mitigates
    target: RSK-0020
    claim_id: CTL-0022-C05
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 114–117 and 198–200"
  - predicate: detects
    target: THR-0004
    claim_id: CTL-0022-C02
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 76–98 and 115–117"
  - predicate: contains
    target: INC-0007
    claim_id: CTL-0022-C03
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 99–110"
  - predicate: governed-by
    target: GOV-0027
    claim_id: CTL-0022-C06
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 112–117, 149–200"
tags:
  - genomics
  - authentication
  - detection
  - incident-response
  - notification
  - control
---

# Consumer-genetics authentication, detection, containment and notification controls

## Objective and evidence ladder

Protect sensitive genetic-service accounts and linked profiles before access,
detect anomalous account/linked actions, contain verified compromise, and
report/notify completely under applicable law.

| Evidence rung | Current evidence |
| --- | --- |
| required/recommended | OPC/ICO findings/recommendations and current Canada/UK breach duties |
| implemented | measures represented as implemented through 2024-12-31 |
| tested | company-reported simulations/exercises and regulator review fragments |
| effective | unknown |
| independently evaluated | regulators assessed implementation/legal resolution, not comparative harm reduction |

> **Claim record — CTL-0022-C01 | source-report**
> **Claim:** The case supports preventive controls at credential/password/MFA
> and sensitive-download boundaries, detective controls for anomalous login and
> linked-account activity, response controls for session/account containment,
> and governance controls for exercises, review and notification.
> **Claim status:** active
> **Scope:** Public case-derived control functions; not a universal baseline,
> product configuration or causal-effectiveness result.
> **As of:** Joint findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C07`–`C09`; joint report paragraphs 57–117 and 198–200.
> **Basis / limits:** Functions and failed/remedial edges are direct. Several
> implementation details are company representations accepted by regulators.

## Prevent, detect and contain

> **Claim record — CTL-0022-C02 | analytic-judgment**
> **Claim:** Unique-password policy, compromised-password checks and MFA act at
> account entry; risk-based login/behavior monitoring, calibrated alerts and
> user-visible event history act at detection; these controls require complete
> identity/event telemetry and timely investigation to be useful.
> **Claim status:** active
> **Scope:** Exact defensive functions and prerequisites; no thresholds,
> fingerprints, rule logic or bypass detail.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> joint report paragraphs 57–98 and 114–117.
> **Limits:** Failed and changed functions are direct; general exact-
> edge placement is defensive normalization.

> **Claim record — CTL-0022-C03 | analytic-judgment**
> **Claim:** Rapid session invalidation, password reset, temporary restriction
> of sensitive export/transfer and mandatory stronger authentication act at
> verified-compromise containment, while delayed execution leaves residual
> account and data-export exposure.
> **Claim status:** active
> **Scope:** Incident-response edge and failure mode; not an operational runbook
> or proof copied information can be recovered.
> **As of:** Event response 2023.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 99–110; `SRC-0055-C05/C07`.
> **Basis / limits:** Actions and regulator-identified delays are direct. Full
> recovery and effect of each action are unmeasured.

## Reporting, notification and record duties

> **Claim record — CTL-0022-C04 | analytic-judgment**
> **Claim:** Incident classification, regulator report, affected-person notice,
> phased update and breach-record functions must preserve jurisdiction-specific
> thresholds, timing and content; known actor attribution is not a prerequisite
> and breach-record preservation is not forensic chain of custody.
> **Claim status:** active
> **Scope:** Current Canadian/UK governance mapping; not legal advice or a
> universal incident-report format.
> **As of:** Current sources checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C02`–`C10`; `SRC-0055-C08`.
> **Basis / limits:** Duties and differences are direct; applicability remains
> fact- and jurisdiction-specific.

## Exact-edge map and governance

> **Claim record — CTL-0022-C05 | analytic-judgment**
> **Claim:** The family maps to `RSK-0020` at credential→account prevention,
> account→linked-profile detection, profile→download/export step-up, verified-
> event→containment, and confirmed-breach→report/notice/record edges, with no
> universal mitigation assertion.
> **Claim status:** active
> **Scope:** Defensive exact-edge crosswalk for the represented event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `CTL-0022-C01`–`C04`;
> [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md).
> **Basis / limits:** Each edge has direct case/rule support. Control presence
> without coverage, telemetry, authority and response speed is insufficient.

> **Claim record — CTL-0022-C06 | analytic-judgment**
> **Claim:** PIPEDA and UK-GDPR findings govern the same implementation through
> different jurisdictional duties; their joint review and remediation
> acceptance establish bounded implementation evaluation but not legal
> equivalence, certification or independent effectiveness.
> **Claim status:** active
> **Scope:** Governance/evidence-state semantics for one shared platform.
> **As of:** Findings 2025; currentness checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md);
> `SRC-0055-C02/C07`–`C10`.
> **Basis / limits:** Separate legal conclusions are direct; the investigation
> is one evidence lineage, not two independent deployments.

> **Claim record — CTL-0022-C07 | analytic-judgment**
> **Claim:** The corpus does not show a comparator, before/after attack rate,
> independently replicated control test, reduced privacy harm or restored
> stolen data; regulator resolution therefore remains below causal
> effectiveness.
> **Claim status:** active
> **Scope:** Complete-control-family evidence gap, not a claim the changes had
> no benefit.
> **As of:** Full package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C02/C09/C11`; investigation limitations in joint
> report paragraphs 16–19 and 188–196.
> **Basis / limits:** Missing predicates are explicit; absence of represented
> effectiveness evidence is not evidence of ineffectiveness.

## Safety boundary

This page contains no detection threshold, rule expression, architecture,
endpoint, credential, automation method, profile data or bypass technique.

## Related pages

- [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [SYN-0030](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
