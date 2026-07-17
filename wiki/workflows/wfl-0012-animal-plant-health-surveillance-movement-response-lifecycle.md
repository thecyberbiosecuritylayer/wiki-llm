---
id: WFL-0012
type: workflow
title: Animal and plant health surveillance, movement and response lifecycle
aliases:
  - EU animal plant lifecycle
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
    claim_id: WFL-0012-C01
    evidence:
      - source: SRC-0037
        locator: "SRC-0037-C04/C05/C07; Animal Articles 10–30, 43–123 and movement Parts; Plant Articles 8–27, 40–104"
tags:
  - agriculture
  - surveillance
  - movement
  - traceability
  - response
---

# Animal and plant health surveillance, movement and response lifecycle

## Two legal lanes

| Stage | Animal-health lane | Plant-health lane |
| --- | --- | --- |
| Breeding/production/keeping | operator responsibility, establishment/animal-group registration and routine biosecurity | breeding/production/storage/marketing roles, seeds/plants for planting and registered operators |
| Diagnostics/surveillance | health observation, notification, sampling, laboratory examination, surveillance programmes and reports | imminent-danger/operator notification, official-lab confirmation, surveys, sampling/testing and electronic reports |
| Treatment/control | vaccination/treatment where applicable, restriction, cleaning and other control measures | treatment, eradication/containment, quarantine/confinement and authorized risk measures |
| Movement/trade/traceability | identification/records, certificates, authority permission/restriction and TRACES exchanges | lot/operator traceability, passports/certificates, movement/trade conditions and TRACES/EUROPHYT exchanges |
| Suspected/confirmed outbreak response | suspicion/confirmation, epidemiological enquiry, zones, response, continued surveillance and review | confirmation, demarcation, contingency/simulation/action plans, response and notification updates |
| Closeout/disposition | slaughter/disposal or other conditional material action, cleaning, repopulation/restoration conditions | invalidation, treatment/destruction/disposition and lifting restrictions after evidence conditions |

Environmental sampling remains supported by independent PATH-SAFE/AU pages;
this EU legal lane does not silently substitute ecosystem monitoring for plant-
health surveys.

> **Claim record — WFL-0012-C01 | source-report**
> **Claim:** The animal lane directly covers production/keeping, diagnostics/
> surveillance, treatment/vaccination, regulated movement/trade/traceability,
> response, conditional disposal and restoration.
> **Claim status:** active
> **Scope:** Regulation 2016/429 legal functions; not one species-specific
> sequence, observed outbreak or implemented workflow.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md),
> `SRC-0037-C04`; relation locator above.
> **Basis / limits:** Stages are direct and conditional.

> **Claim record — WFL-0012-C02 | source-report**
> **Claim:** The plant lane directly covers breeding/production, survey/
> sampling/testing, treatment/containment, movement/trade/traceability,
> contingency/response and destruction/disposition states.
> **Claim status:** active
> **Scope:** Regulation 2016/2031 legal functions; not farm practice,
> environmental-sampling implementation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0037-C05`; Plant Articles 2, 8–27, 60–70, 78–104.
> **Basis / limits:** Stages are direct; exceptions remain applicable.

> **Claim record — WFL-0012-C03 | analytic-judgment**
> **Claim:** The two lanes fill treatment, regulated-movement and disposition
> candidates for `AGE-WL`, but one EU ecosystem cannot independently complete
> the frozen lifecycle cell without AU/PATH-SAFE/environmental reconciliation.
> **Claim status:** superseded
> **Scope:** AGE-WL candidate contribution; no score transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `WFL-0012-C01/C02`; [WFL-0007](wfl-0007-smart-farm-monitoring-production-supply.md);
> [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md); frozen rubric.
> **Basis / limits:** Reconciliation and SF2 remain pending.
> **Superseded by:** `SYN-0025-C02`, which completes the independent joined
> lifecycle reconciliation while preserving source-specific limits.

## Safety boundary

The page exposes no operational animal/plant handling procedure, location,
parameter or record.

> **Claim record — WFL-0012-C04 | analytic-judgment**
> **Claim:** The page exposes no operational animal/plant handling procedure,
> location, parameter or record.
> **Claim status:** stale
> **Scope:** Local page content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content.
> **Limits:** Only legal functional stages were retained at the stated review
> date. Repository-content assertions can change; this one is retained only as
> a historical safety note, with the current boundary stated in prose above.

## Related pages

- [GOV-0020](../governance/gov-0020-eu-animal-plant-health-imsoc-legislation.md)
- [AST-0009](../assets/ast-0009-animal-plant-health-assets-stakeholders.md)
- [SYS-0012](../systems/sys-0012-eu-animal-plant-health-imsoc-architecture.md)
- [CTL-0017](../controls/ctl-0017-animal-plant-health-traceability-notification-response-controls.md)
- [WFL-0007](wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [CTL-0019](../controls/ctl-0019-animal-disease-traceability-performance-assurance.md)

## Sources

- [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md)
