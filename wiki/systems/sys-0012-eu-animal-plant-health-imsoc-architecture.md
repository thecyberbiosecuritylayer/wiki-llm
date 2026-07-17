---
id: SYS-0012
type: system
title: EU animal and plant health IMSOC architecture
aliases:
  - ADIS EUROPHYT TRACES architecture
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0037
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0037
    claim_id: SYS-0012-C01
    evidence:
      - source: SRC-0037
        locator: "SRC-0037-C06/C07/C09; IMSOC Articles 1–11, 29–46"
tags:
  - imsoc
  - adis
  - europhyt
  - traces
  - architecture
  - agriculture
---

# EU animal and plant health IMSOC architecture

## Components and exact boundaries

| Component/boundary | Function | Responsibility/limit |
| --- | --- | --- |
| Official veterinary/plant laboratory network and diagnostic dependency | animal reference/official-laboratory cooperation, results/reporting and disease-system exchange; plant official confirmation, reference-lab/survey/test and quarantine/confinement dependencies | functional legal network/dependency, not laboratory IT topology, LIMS inventory or validation |
| iRASFF | food/feed alert and cooperation information | distinct risk/non-compliance notification classes; not an incident count |
| ADIS | animal-disease Union notification/reporting | Commission/Member-State authority network and contact points |
| EUROPHYT | plant-pest outbreak notifications and updates | official-confirmation/new-information workflow; not general environmental monitoring |
| TRACES | certificates, consignments, authority decisions and follow-up | scoped operator/authority access, signatures/seals and responsibility by contribution/role |
| Component↔component | iRASFF/TRACES, EUROPHYT/TRACES and ADIS/TRACES exchanges | legal functional links, not proof of one technical deployment topology |
| National/external systems↔IMSOC | standards/data-dictionary/business-rule exchange and service-level maintenance | includes Member-State and bounded third-country/international access conditions |
| Availability boundary | temporary templates/alternate exchange followed by electronic reconciliation | contingency design, not recovery performance or accepted safe state |

> **Claim record — SYS-0012-C01 | source-report**
> **Claim:** IMSOC directly maps iRASFF, ADIS, EUROPHYT and TRACES plus their
> networks/contact points, cross-component and national/external interfaces,
> operator/authority access and ownership/responsibility boundaries.
> **Claim status:** active
> **Scope:** Legal component and trust-boundary architecture; not a deployed
> topology, endpoint inventory, live IAM validation or performance result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md),
> `SRC-0037-C06`; IMSOC Articles 1–11, 29–45.
> **Basis / limits:** Components, interfaces and roles are explicit.

> **Claim record — SYS-0012-C02 | source-report**
> **Claim:** The architecture assigns data/controller/security/access,
> signature/seal, retention and contribution-specific responsibility rather
> than treating every network member as universally authorized.
> **Claim status:** active
> **Scope:** Legal trust-boundary design; not GDPR compliance, credential
> configuration, penetration test or implementation evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0037-C06/C09`; IMSOC Articles 4–11, 36–45.
> **Basis / limits:** Role/access predicates are direct and scoped.

> **Claim record — SYS-0012-C03 | source-report**
> **Claim:** ADIS/TRACES contingency rules require bounded out-of-system
> capture and later reconciliation after availability returns, but provide no
> measured recovery time, completeness or trusted-state validation.
> **Claim status:** active
> **Scope:** IMSOC contingency design, not actual outage/recovery evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0037-C09`; IMSOC Articles 28, 29b and 46.
> **Basis / limits:** Required reconciliation is direct; outcome predicates are
> absent.

> **Claim record — SYS-0012-C04 | analytic-judgment**
> **Claim:** `SYS-0012` supplies official notification/traceability-platform
> architecture linked to veterinary/plant laboratory-network and diagnostic
> functions for `AGE-SD`; complete laboratory IT architecture, validated
> organization-specific boundaries and SF2 reconciliation remain pending.
> **Claim status:** superseded
> **Scope:** AGE-SD candidate contribution; no score transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0037-C03/C05/C06`; Animal Articles 13, 16–17 and
> 22–23; Plant Articles 10, 19a, 25/27 and 60–64; `SYS-0012-C01`–`C03`;
> [SYS-0005](sys-0005-connected-smart-farm-ecosystem.md);
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md);
> frozen rubric.
> **Basis / limits:** One legal architecture is not deployed validation or
> independent synthesis.
> **Superseded by:** `SYN-0025-C03`, which completes the independent functional
> system-class reconciliation without claiming deployed topology validation.

## Safety boundary

No live endpoint, credential, topology or operational identifier is exposed.

> **Claim record — SYS-0012-C05 | analytic-judgment**
> **Claim:** No live endpoint, credential, topology or operational identifier
> is exposed.
> **Claim status:** stale
> **Scope:** Local page content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content.
> **Limits:** Only public component classes were retained at the stated review
> date. Repository-content assertions can change; this one is retained only as
> a historical safety note, with the current boundary stated in prose above.

## Related pages

- [GOV-0020](../governance/gov-0020-eu-animal-plant-health-imsoc-legislation.md)
- [AST-0009](../assets/ast-0009-animal-plant-health-assets-stakeholders.md)
- [WFL-0012](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md)
- [CTL-0017](../controls/ctl-0017-animal-plant-health-traceability-notification-response-controls.md)
- [SYS-0005](sys-0005-connected-smart-farm-ecosystem.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)

## Sources

- [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md)
