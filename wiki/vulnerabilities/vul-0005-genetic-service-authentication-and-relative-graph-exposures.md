---
id: VUL-0005
type: vulnerability
title: Consumer-genetics authentication, monitoring and relative-graph exposure classes
aliases:
  - genetic service account exposure classes
  - relative graph and authentication weaknesses
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
source_ids:
  - SRC-0055
sensitivity: public
dual_use: low
vulnerability_status: event-specific-regulatory-findings-not-universal-service-state
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: VUL-0005-C01
    evidence:
      - source: SRC-0055
        locator: "Joint OPC/ICO report paragraphs 57–87 and 111–117"
  - predicate: enables
    target: RSK-0020
    claim_id: VUL-0005-C03
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 20–35 and 136–147"
tags:
  - genomics
  - vulnerability
  - authentication
  - monitoring
  - linked-profiles
  - privacy
---

# Consumer-genetics authentication, monitoring and relative-graph exposure classes

## Event-specific findings

> **Claim record — VUL-0005-C01 | source-report**
> **Claim:** Regulators found the pre-event 23andMe state deficient in its
> credential-stuffing risk treatment, mandatory authentication, compromised-
> password screening, anomaly monitoring, investigation of warning events and
> incident-specific response preparation relative to the sensitive data held.
> **Claim status:** active
> **Scope:** One platform and relevant period; not a census of genetics
> services, a current vulnerability scan or a claim every weakness was causal.
> **As of:** Pre/during-breach state assessed in 2025 findings.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C07`; joint report paragraphs 57–117.
> **Basis / limits:** The deficiencies are direct legal/technical findings from
> one joint investigation. Full privileged records were unavailable.

## Relative-graph boundary

> **Claim record — VUL-0005-C02 | analytic-judgment**
> **Claim:** An opted-in relative/family sharing feature becomes an exposure
> amplifier when one authorized account view reveals information about many
> linked people and account compromise is not contained; relational visibility
> itself is not automatically a vulnerability or unauthorized processing.
> **Claim status:** active
> **Scope:** Canonical linked-profile boundary demonstrated by the case; not a
> universal design defect, kinship inference method or re-identification claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C03/C04`; joint report paragraphs 28–35;
> [AST-0001](../assets/ast-0001-genomic-data.md).
> **Basis / limits:** Visibility expansion is direct. Vulnerability status
> requires the compromised-account and failed-control conjunction.

## Conditional consequence and remediation state

> **Claim record — VUL-0005-C03 | analytic-judgment**
> **Claim:** These weakness/boundary classes enable `RSK-0020` only where an
> actor obtains reach, sensitive or linked information is exposed, and
> prevention/detection/containment fails; none alone proves misuse or harm.
> **Claim status:** active
> **Scope:** Defensive exact-edge causal semantics.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `VUL-0005-C01/C02`;
> [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md).
> **Basis / limits:** Conditions reflect documented event edges while keeping
> access, exposure and downstream effects distinct.

> **Claim record — VUL-0005-C04 | analytic-judgment**
> **Claim:** Regulators accepted represented improvements through 2024-12-31
> as resolving their safeguard concerns, so this page does not assert that the
> historical platform state persists; independent effectiveness and outcome
> evidence remain unavailable.
> **Claim status:** active
> **Scope:** Temporal vulnerability status, not certification or a current
> secure-configuration finding.
> **As of:** Remediation represented through 2024-12-31; reviewed 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** `SRC-0055-C09`; joint report paragraphs 114–117.
> **Basis / limits:** Legal resolution is direct; measures were principally
> self-reported and not independently tested for harm reduction.

## Related pages

- [THR-0004](../threats/thr-0004-credential-based-genetic-data-access.md)
- [TEC-0004](../techniques/tec-0004-credential-stuffing-and-linked-profile-scraping.md)
- [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md)
- [SYN-0030](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
