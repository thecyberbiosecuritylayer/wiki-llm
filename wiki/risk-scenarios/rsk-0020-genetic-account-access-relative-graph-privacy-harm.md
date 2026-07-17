---
id: RSK-0020
type: risk-scenario
title: Genetic-account compromise propagating through relative graphs to privacy harm
aliases:
  - 23andMe account to kin privacy path
  - consumer genetics linked-profile breach path
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
origin_domain: cyber
destination_domains:
  - genomic-privacy
  - human-identity-and-kin-privacy
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: RSK-0020-C01
    evidence:
      - source: SRC-0055
        locator: "Joint OPC/ICO report paragraphs 20–35 and 136–147"
  - predicate: depends-on
    target: INC-0007
    claim_id: RSK-0020-C01
    evidence:
      - source: SRC-0055
        locator: "Joint OPC/ICO report paragraphs 20–35, 89–117 and 149–200"
  - predicate: affects
    target: AST-0001
    claim_id: RSK-0020-C03
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 28–35"
  - predicate: depends-on
    target: WFL-0005
    claim_id: RSK-0020-C03
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 28–35; account, report and linked-sharing states"
  - predicate: depends-on
    target: SYS-0003
    claim_id: RSK-0020-C03
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 28–35, 57–87 and 99–110"
  - predicate: governed-by
    target: GOV-0027
    claim_id: RSK-0020-C05
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 112–117, 147–187 and 198–201"
tags:
  - genomics
  - consumer-genetics
  - cyber-to-privacy
  - relatives
  - observed
---

# Genetic-account compromise propagating through relative graphs to privacy harm

## Evidence classification and observed path

This is a mixed observed/analytic path anchored in one documented incident:

`reused-credential account access → account and linked-relative visibility →
collection/public offering of identity, ancestry, health/genetic and kinship
information → persistent privacy, identity, dignity and relationship risk`

> **Claim record — RSK-0020-C01 | analytic-judgment**
> **Claim:** `INC-0007` supplies an observed cyber-to-genomic-privacy path from
> credential-based account compromise through linked-profile access to
> unauthorized disclosure/online offering of sensitive identity, ancestry,
> health/genetic and relationship information.
> **Claim status:** active
> **Scope:** One consumer-genetics incident; not a biological change, clinical
> outcome, realized harm for every person or re-identification procedure.
> **As of:** Event 2023; regulatory findings 2025.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md);
> [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C03`–`C05`.
> **Basis / limits:** Access, data classes and online offering are direct. The
> downstream harm categories are regulatory risk findings, not a cohort outcome.

## Populations and consequence grade

> **Claim record — RSK-0020-C02 | source-report**
> **Claim:** The event directly affected 18,222 accessed accounts but expanded
> through linked profile visibility to almost seven million affected/accessible
> customer profiles; those populations overlap by category and cannot be added
> or interpreted as seven million raw-genetic-data downloads.
> **Claim status:** active
> **Scope:** Event population semantics; not an exact deduplicated worldwide
> census or evidence each field was accessed for each person.
> **As of:** Findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C03/C04`; joint report paragraphs 20, 28–35 and tables.
> **Basis / limits:** Counts and categories are direct; raw-DNA download counts
> were methodologically disputed and remain separate.

> **Claim record — RSK-0020-C03 | analytic-judgment**
> **Claim:** Affected assets include account identity/settings, ancestry and
> health reports, raw genetic files where relevant, relative/family profiles
> and relationship metadata; stakeholders include account holders and linked
> relatives whose information was visible through another account.
> **Claim status:** active
> **Scope:** Public asset/stakeholder classes for one event; no personal record.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C04`;
> [AST-0001](../assets/ast-0001-genomic-data.md);
> [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md);
> [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md).
> **Basis / limits:** Classes are source-reported; exact per-person exposure is
> heterogeneous and no dataset is reproduced.

> **Claim record — RSK-0020-C04 | source-report**
> **Claim:** Regulators found high sensitivity and high misuse probability,
> including persistent identity, discrimination, dignity, reputational,
> relationship and other privacy harms; the retained case does not measure a
> biological, clinical or physical outcome caused by the breach.
> **Claim status:** active
> **Scope:** Regulatory risk/outcome classification, not incidence or severity
> measurement for individuals.
> **As of:** Joint findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 118–147; `SRC-0055-C11`.
> **Basis / limits:** Risk thresholds and harm categories are direct; individual
> realized outcomes and causal rates are unmeasured.

## Governance and control edges

> **Claim record — RSK-0020-C05 | analytic-judgment**
> **Claim:** Exact control edges are unique-password/compromised-password and
> MFA prevention at account entry, anomaly/linked-action monitoring and event
> history at access, sensitive-download step-up/delay at export, rapid session/
> account containment, and complete regulator/person notification after breach.
> **Claim status:** active
> **Scope:** Defensive edge mapping from the case and current rules; not a
> configuration recipe or claim each measure is independently effective.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md);
> `SRC-0055-C07`–`C09`; [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md).
> **Basis / limits:** Failed and remedial edges are direct; effectiveness beyond
> bounded regulatory resolution is unknown.

> **Claim record — RSK-0020-C06 | analytic-judgment**
> **Claim:** The case supplies the missing primary genomic downstream privacy
> outcome with independent regulator context and a seventh `INC`/review page
> that supplies the sixth conservatively distinguishable primary-supported
> event; exact rubric transitions require the strict reconciliation in
> `SYN-0030`.
> **Claim status:** superseded
> **Scope:** Candidate contribution, not a score change by this page alone.
> **As of:** 2026-07-12 pre-activation audit.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `RSK-0020-C01`–`C05`; frozen `GEN-CI`, `THI-WL/CI` criteria.
> **Basis / limits:** Event and privacy outcome roles are present; synthesis
> must still enforce lineage, sector and independent-context floors.
> **Superseded by:** `SYN-0030-C03/C04/C05`, after strict genomic-outcome and
> incident-count reconciliation.

## Safety boundary

No credentials, records, profiles, endpoints, code, request patterns,
re-identification method or operational response procedure is exposed.

## Related pages

- [THR-0004](../threats/thr-0004-credential-based-genetic-data-access.md)
- [TEC-0004](../techniques/tec-0004-credential-stuffing-and-linked-profile-scraping.md)
- [VUL-0005](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md)
- [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [RSK-0004 — Prior hypothetical genomic disclosure path](rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md)
- [SYN-0030](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
