---
id: CTL-0017
type: control
title: Animal and plant health traceability, notification and response controls
aliases:
  - EU animal plant IMSOC controls
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
    claim_id: CTL-0017-C01
    evidence:
      - source: SRC-0037
        locator: "SRC-0037-C08/C09; Animal Articles 10–30, 43–123; Plant Articles 9–27, 60–70, 78–104; IMSOC Articles 4–11, 28–46"
  - predicate: depends-on
    target: WFL-0012
    claim_id: CTL-0017-C01
    evidence:
      - source: SRC-0037
        locator: "Exact legal control-to-lifecycle edges in SRC-0037-C04/C05/C08"
  - predicate: depends-on
    target: SYS-0012
    claim_id: CTL-0017-C03
    evidence:
      - source: SRC-0037
        locator: "IMSOC ownership/access/interface/security/contingency dependencies, Articles 4–11 and 28–46"
tags:
  - agriculture
  - biosecurity
  - traceability
  - detection
  - response
  - resilience
---

# Animal and plant health traceability, notification and response controls

## Exact-edge map

| Function | Animal-health edge | Plant-health edge | Digital/IMSOC prerequisite |
| --- | --- | --- | --- |
| Prevent | operator biosecurity, registration, identification, movement conditions | registered operators, quarantine/confinement, movement/passport conditions and critical-point plans | scoped ownership/access, current reference/contact data and maintained interfaces |
| Detect | observation/surveillance, sampling, official-lab examination | notification, official-lab confirmation, survey/sampling/testing | ADIS/EUROPHYT/iRASFF notification roles, required fields/deadlines and updates |
| Respond/contain | enquiry, restrictions/zones, treatment/vaccination, cleaning and other conditional control | eliminate/withdraw/recall, eradicate/contain, demarcate, restrict and invalidate | authority decision, certificate/consignment/follow-up states and role-scoped exchange |
| Trace | animal/group/establishment, germinal, movement and certificate records | supplier/recipient/trade-unit records, traceability codes, passports/certificates | TRACES/national-system exchange, signatures/seals and retention |
| Recover/resilience | continued surveillance, cleaning, repopulation/restoration conditions | evidence-based lifting of restrictions and corrective closure | outage template/alternate exchange followed by electronic reconstruction/reconciliation |

These are legal/control-design functions. A required action or platform
feature is not evidence that an organization implemented, tested or benefited
from it.

> **Claim record — CTL-0017-C01 | source-report**
> **Claim:** The Animal Health Law maps biosecurity, notification,
> surveillance, laboratory confirmation, movement restriction,
> identification/traceability, response and conditional recovery controls to
> named animal/material/establishment edges.
> **Claim status:** active
> **Scope:** Binding EU animal-health design with disease/species/derogation
> limits; not a cyber baseline, deployment, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md),
> `SRC-0037-C04/C08`; Animal Articles 10–30, 43–123 and movement Parts.
> **Basis / limits:** Control/object edges are direct and conditional.

> **Claim record — CTL-0017-C02 | source-report**
> **Claim:** The Plant Health Regulation maps notification, confirmation,
> survey/testing, eradication/containment, movement, traceability,
> passport/certificate, invalidation/correction and destruction/disposition
> controls to named plant/operator/lot/trade-unit edges.
> **Claim status:** active
> **Scope:** Binding EU plant-health design; not a general cyber baseline,
> observed event, implementation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0037-C05/C08`; Plant Articles 9–27, 60–70, 78–104.
> **Basis / limits:** Exact controls and exceptions are direct.

> **Claim record — CTL-0017-C03 | source-report**
> **Claim:** IMSOC adds responsibility, scoped access/security, standards-
> based exchange, signature/seal integrity, retention and outage-reconciliation
> dependencies to the notification/certificate/traceability controls.
> **Claim status:** active
> **Scope:** Legal digital-control design; not live IAM, architecture
> validation, recovery metric or proof of trusted restored state.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0037-C06/C08/C09`; IMSOC Articles 4–11, 28, 29b,
> 32 and 36–46; [SYS-0012](../systems/sys-0012-eu-animal-plant-health-imsoc-architecture.md).
> **Basis / limits:** Dependencies are direct; test/outcome evidence is absent.

> **Claim record — CTL-0017-C04 | analytic-judgment**
> **Claim:** The combined map supplies exact agriculture biosecurity,
> traceability, detection, response and resilience edges, but the EU package
> alone does not close `AGE-CT`: agriculture-specific cyber response/trusted
> recovery still requires independent NIST/Drape/AU/PATH-SAFE reconciliation.
> **Claim status:** superseded
> **Scope:** AGE-CT candidate contribution; no score transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `CTL-0017-C01`–`C03`; [CTL-0005](ctl-0005-agricultural-cyberbiosecurity-capability-controls.md);
> frozen rubric.
> **Basis / limits:** Exact legal edges are complete, while cyber and
> implementation/effectiveness predicates stay separate.
> **Superseded by:** `SYN-0025-C07`, which reconciles the independent
> agriculture biosecurity and cyber layers while retaining the same
> implementation/effectiveness boundary.

## Safety boundary

The page is defensive and omits operational identifiers, locations,
credentials, biological content and response procedures.

> **Claim record — CTL-0017-C05 | analytic-judgment**
> **Claim:** The page is defensive and omits operational identifiers,
> locations, credentials, biological content and response procedures.
> **Claim status:** stale
> **Scope:** Local page content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content; no external source is applicable to this
> editorial self-audit.
> **Limits:** Retained as a historical local-content audit, not as an
> externally evidenced decision claim. The current safety boundary is the
> prose above.

## Related pages

- [GOV-0020](../governance/gov-0020-eu-animal-plant-health-imsoc-legislation.md)
- [AST-0009](../assets/ast-0009-animal-plant-health-assets-stakeholders.md)
- [WFL-0012](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md)
- [SYS-0012](../systems/sys-0012-eu-animal-plant-health-imsoc-architecture.md)
- [CTL-0005](ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)

## Sources

- [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md)
