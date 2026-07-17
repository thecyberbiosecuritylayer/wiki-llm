---
id: TEC-0004
type: technique
title: Credential stuffing followed by linked-profile information collection
aliases:
  - credential stuffing and relative graph access
  - linked DNA profile collection technique
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_ids:
  - SRC-0055
sensitivity: public
dual_use: low
technique_kind: defensive-high-level-credential-reuse-and-authorized-view-expansion-class
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: TEC-0004-C01
    evidence:
      - source: SRC-0055
        locator: "Joint OPC/ICO report paragraphs 20–30"
  - predicate: exploits
    target: VUL-0005
    claim_id: TEC-0004-C02
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 57–87 and 111–113"
  - predicate: enables
    target: RSK-0020
    claim_id: TEC-0004-C02
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 28–35 and 136–147"
tags:
  - genomics
  - credential-stuffing
  - linked-profiles
  - technique
  - defensive-taxonomy
---

# Credential stuffing followed by linked-profile information collection

## Method class

> **Claim record — TEC-0004-C01 | source-report**
> **Claim:** In the 23andMe event, credential stuffing used login details
> exposed elsewhere to enter matching accounts; information visible through
> opted-in DNA Relatives and family-tree relationships then expanded the
> affected information beyond directly accessed accounts.
> **Claim status:** active
> **Scope:** High-level method documented in one event; not credential values,
> software, rates, request sequence or proof all linked files were downloaded.
> **As of:** Attack 2023-04-29–2023-09-20.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C03/C04`; joint report paragraphs 20–30.
> **Basis / limits:** Method and expansion boundary are direct. “Almost seven
> million” is an affected/accessible profile population, not raw-DNA downloads.

## Preconditions and consequence boundary

> **Claim record — TEC-0004-C02 | analytic-judgment**
> **Claim:** The method exploits `VUL-0005` and enables `RSK-0020` only when
> credential reuse, matching account access, linked-profile visibility and
> insufficient prevention/detection coincide; credential stuffing alone does
> not guarantee genetic-data access or downstream privacy harm.
> **Claim status:** active
> **Scope:** Conditional exact-edge model without operational procedure.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `TEC-0004-C01`; `SRC-0055-C07`;
> [VUL-0005](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md);
> [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md).
> **Basis / limits:** The event supplies the conjunction. It is not generalized
> to services without the same account, sharing or safeguard state.

> **Claim record — TEC-0004-C03 | analytic-judgment**
> **Claim:** `THR-0004` is the intentional actor/objective class, `TEC-0004`
> the high-level method, `VUL-0005` the enabling weakness/boundary state and
> `INC-0007` the observed event; none is interchangeable with a privacy outcome.
> **Claim status:** active
> **Scope:** Canonical typed-graph semantics.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Linked canonical pages; `SRC-0055-C03/C07/C11`.
> **Basis / limits:** Source roles are explicit; a generic method page is not
> counted as a second event or independent investigation.

## Safety boundary

Only public defensive abstraction is retained; no executable, credential,
endpoint, payload, request pattern, threshold or evasion guidance appears.

## Related pages

- [THR-0004](../threats/thr-0004-credential-based-genetic-data-access.md)
- [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [SYN-0030](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
