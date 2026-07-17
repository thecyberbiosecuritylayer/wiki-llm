---
id: CTL-0023
type: control
title: Laboratory result validation, anomaly detection and containment controls
aliases:
  - Immensa and HSE laboratory incident control lessons
  - laboratory context configuration monitoring response controls
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_ids:
  - SRC-0004
  - SRC-0026
  - SRC-0057
  - SRC-0058
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0057
    claim_id: CTL-0023-C02
    evidence:
      - source: SRC-0057
        locator: "UKHSA improvements page, testing operations items 1–4; SUI Recommendations 1–14, pp. 63–66"
  - predicate: evidenced-by
    target: SRC-0058
    claim_id: CTL-0023-C04
    evidence:
      - source: SRC-0058
        locator: "ED03-2024 Action required and record-keeping/IT sections; HID 5-2011 Action required"
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: CTL-0023-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 36–48, 61–72, 74–124, 142–168 and 190–207"
  - predicate: mitigates
    target: RSK-0021
    claim_id: CTL-0023-C01
    evidence:
      - source: SRC-0057
        locator: "SUI observed failed/interrupted edges and Recommendations 4–10, pp. 63–65"
      - source: SRC-0058
        locator: "HSE context, linkage, alert and containment-decision action edges"
  - predicate: detects
    target: HAZ-0006
    claim_id: CTL-0023-C03
    evidence:
      - source: SRC-0057
        locator: "SUI §§2.6 and 3.4; performance/anomaly monitoring and investigation findings"
      - source: SRC-0026
        locator: "WHO LQMS QC, occurrence, audit and result-review controls"
tags:
  - laboratory
  - result-validation
  - context-capture
  - anomaly-detection
  - incident-response
  - correction
  - containment
  - evidence-state
---

# Laboratory result validation, anomaly detection and containment controls

## Exact-edge control map

| `RSK-0021` edge | Prevent/detect | Contain/respond/recover | Evidence state |
| --- | --- | --- | --- |
| input/context→accession | structured required context, visibility, cross-sample linkage, validation | clarify/reject/update and alert affected staff | HSE directed; no adoption metric |
| measurement→classification | authorized configuration/change, verification, QC, competent review | hold, investigate, correct and trace affected results | WHO recommended; SUI lesson |
| classification→report | contextual multi-indicator performance monitoring and anomaly triggers | escalate, investigate and suspend affected processing | UKHSA reports implementation |
| report→decision | authorization, destination/receipt and correction controls | notify affected recipients and update advice/records | WHO design; incident response observed |
| concern→incident response | unified logging, ownership, risk assessment and evidence review | single governance line, external challenge and communication | SUI recommended; some logging/accountability implemented |
| restoration→assurance | verified correction, traceability, review and test evidence | independently assess outcome/recurrence limits | required evidence state absent here |

> **Claim record — CTL-0023-C01 | analytic-judgment**
> **Claim:** The matrix maps context, configuration, validation, anomaly
> detection, incident response, correction, containment, recovery and assurance
> functions to exact `RSK-0021` edges rather than asserting a generic or
> universal mitigation.
> **Claim status:** active
> **Scope:** Defensive control-function map; not a laboratory procedure,
> universal baseline, implementation claim or safety guarantee.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [RSK-0021](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md),
> `RSK-0021-C01`–`C04`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C06/C07/C09/C10`; `SRC-0057-C08/C09`; `SRC-0058-C04/C05`.
> **Basis / limits:** Each function has a direct source role. Exact-edge
> normalization and prerequisite stitching are analytic.

## Implemented post-incident states

> **Claim record — CTL-0023-C02 | source-report**
> **Claim:** UKHSA reports implementing national/regional performance reports,
> daily monitoring, closer laboratory-oversight/incident-response links,
> clearer public-health accountability and stronger logging/tracking of
> decisions after the Immensa incident.
> **Claim status:** active
> **Scope:** Issuer-reported implementation in the represented testing system;
> not independent verification, coverage completeness or outcome
> effectiveness.
> **As of:** Reported 2022-11-29.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> `SRC-0057-C09`; improvements page `testing operations group` items 1–4.
> **Basis / limits:** Implemented wording is direct. Reduced demand/provider
> count also changed risk, and no before/after outcome comparison is supplied.

> **Claim record — CTL-0023-C03 | analytic-judgment**
> **Claim:** Performance monitoring must be interpreted in context and linked
> to an investigation trigger; the SUI shows that collected indicators or
> concerns without clear ownership, analysis and escalation can fail to detect
> or contain a result-integrity event promptly.
> **Claim status:** active
> **Scope:** Event-derived detective-control failure condition; not a numeric
> rule, alert threshold or universal monitoring recipe.
> **As of:** Event 2021; findings 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI §§2.6 and 3.4, pp. 45–59; Recommendations 6–10,
> pp. 64–65; `SRC-0057-C08/C09`.
> **Basis / limits:** Missed interpretation/escalation opportunities are
> direct. The report cautions that no single process would necessarily have
> prevented the originating error.

## Input/context and containment-decision controls

> **Claim record — CTL-0023-C04 | source-report**
> **Claim:** HSE directs duty holders to capture and expose relevant specimen
> context, link related samples, alert laboratory staff to later information,
> train involved roles, maintain clear guidance and monitor/audit correct
> completion so containment decisions receive the needed input.
> **Claim status:** active
> **Scope:** Defensive context-to-decision controls for clinical/veterinary
> laboratories; not confirmed adoption or an operational containment method.
> **As of:** ED03-2024; checked 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md),
> `SRC-0058-C04/C05`; both notices' `Action required` sections.
> **Basis / limits:** Control functions are direct. No implementation, test or
> exposure-reduction metric is reported.

## Recommendations, prerequisites and failure limits

> **Claim record — CTL-0023-C05 | source-report**
> **Claim:** The SUI's broader quality framework, accreditation, procurement,
> monitoring-trigger, single-governance, risk-assessment, evidence-review,
> communication and external-challenge actions remain recommendations unless
> separately identified as implemented.
> **Claim status:** active
> **Scope:** Recommendation/implementation state separation; not legal duty or
> automatic completion.
> **As of:** Recommendations published 2022-11-29.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI Recommendations 1–14, pp. 63–66; improvements page;
> `SRC-0057-C09`.
> **Basis / limits:** Recommendation text and separately implemented items are
> direct. Future-tense commercial commitments are not promoted.

> **Claim record — CTL-0023-C06 | analytic-judgment**
> **Claim:** These controls depend on trustworthy input, suitable indicators,
> competent review, authority to stop/correct, traceable affected-state scope,
> timely communication and validated restoration; they can fail through
> missing context, bad configuration, alert overload, siloed ownership,
> delayed escalation or unverified recovery.
> **Claim status:** active
> **Scope:** Defensive prerequisites/failure modes; no probability, settings or
> operational instructions.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `CTL-0023-C01`–`C05`; `SRC-0057-C08/C09`;
> `SRC-0058-C03`–`C05`; `SRC-0026-C09/C10`.
> **Basis / limits:** Dependencies and failures are source-supported; the
> concise cross-source list is analytic.

> **Claim record — CTL-0023-C07 | analytic-judgment**
> **Claim:** The portfolio contains recommended, directed and issuer-reported
> implemented controls but no independent before/after test, comparator,
> recurrence metric, harm-reduction result or verified restoration endpoint;
> it therefore cannot satisfy `LAB-AE` or `CTR-AE`.
> **Claim status:** active
> **Scope:** Complete evidence-state boundary for this control family.
> **As of:** Full package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0057-C09/C10`; `SRC-0058-C05/C07`;
> `CTL-0023-C01`–`C06`.
> **Basis / limits:** Missing effectiveness predicates are explicit; absence
> of represented results is not evidence the controls had no benefit.

## Safety boundary

No assay setting, alert rule, system endpoint, facility topology, laboratory
procedure or personal/sample data is retained.

## Related pages

- [HAZ-0006 — detected hazards](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
- [VUL-0006 — enabling exposures](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [INC-0008 — event lessons](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [RSK-0021 — mitigated path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0012 — broader clinical-laboratory controls](ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md)
- [SYN-0031 — rubric reconciliation](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md)
