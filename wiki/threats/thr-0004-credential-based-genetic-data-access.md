---
id: THR-0004
type: threat
title: Intentional credential-based access to consumer genetic information
aliases:
  - consumer genetics account-access threat
  - genetic-service credential abuse threat
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_ids:
  - SRC-0055
sensitivity: public
dual_use: low
threat_kind: intentional-credential-based-account-and-linked-profile-access
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: THR-0004-C01
    evidence:
      - source: SRC-0055
        locator: "Joint OPC/ICO report paragraphs 20–35, 57–117 and 136–147"
  - predicate: exploits
    target: VUL-0005
    claim_id: THR-0004-C02
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 57–87 and 111–113"
  - predicate: enables
    target: TEC-0004
    claim_id: THR-0004-C02
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 20–30"
tags:
  - genomics
  - consumer-genetics
  - threat
  - credential-abuse
  - privacy
---

# Intentional credential-based access to consumer genetic information

## Threat class and observed anchor

This page represents an intentional actor objective: obtain unauthorized
access to consumer-genetics accounts and information visible through linked
relative/family-profile features. The canonical method is `TEC-0004`, enabling
weaknesses are `VUL-0005`, and the documented 23andMe event is `INC-0007`.

> **Claim record — THR-0004-C01 | source-report**
> **Claim:** The joint OPC/ICO investigation documents an intentional threat
> actor using reused credentials to access consumer-genetics accounts and then
> obtain account and linked-relative information, with copied information
> subsequently advertised online.
> **Claim status:** active
> **Scope:** One documented consumer-genetics event and high-level actor goal;
> not actor identity, prevalence, a credential source list or access recipe.
> **As of:** Event 2023; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C03`–`C05`; joint report paragraphs 20–35.
> **Basis / limits:** Intent, unauthorized access and online offering are
> regulator findings. The record does not conclusively establish that every
> action or post came from one person.

## Preconditions and graph semantics

> **Claim record — THR-0004-C02 | analytic-judgment**
> **Claim:** `THR-0004` can exploit deficient authentication, password-risk,
> monitoring or linked-profile boundary state in `VUL-0005` and enable
> `TEC-0004` only where reusable credentials reach an account and preventive or
> detective controls fail.
> **Claim status:** active
> **Scope:** Defensive precondition model; no credentials, target selection,
> automation parameters, endpoints or evasion instructions.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `THR-0004-C01`; joint report paragraphs 57–117;
> [VUL-0005](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md);
> [TEC-0004](../techniques/tec-0004-credential-stuffing-and-linked-profile-scraping.md).
> **Basis / limits:** Regulator findings support the failed boundaries; the
> conditional graph does not imply every genetics service shares them.

> **Claim record — THR-0004-C03 | analytic-judgment**
> **Claim:** Actor/threat, method, weakness, incident and consequence remain
> separate nodes; unknown actor attribution does not erase the documented
> intentional access, and a generic credential threat does not create another
> incident.
> **Claim status:** active
> **Scope:** Canonical threat/incident ontology and attribution grade.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C02/C03/C11`;
> [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md);
> [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md).
> **Basis / limits:** The official case supports intent and event; conclusive
> personal attribution is absent and unnecessary for defensive classification.

## Safety boundary

No credential values, credential-acquisition source, login route, automation
rate, code, indicator, endpoint, evasion method or re-identification procedure
is included.

## Related pages

- [AST-0001](../assets/ast-0001-genomic-data.md)
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [SYN-0030](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
