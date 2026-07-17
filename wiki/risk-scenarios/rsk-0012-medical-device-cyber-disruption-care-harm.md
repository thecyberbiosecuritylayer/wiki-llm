---
id: RSK-0012
type: risk-scenario
title: Medical-device cyber disruption affecting diagnosis or care
aliases:
  - medical-device compromise to patient-care harm
  - diagnostic-device cyber disruption path
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0017
sensitivity: public
dual_use: low
origin_domain: digital
destination_domains:
  - digital
  - clinical
  - biological
  - physical
relations:
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: RSK-0012-C01
    evidence:
      - source: SRC-0017
        locator: "§§I–III, printed pp. 1–5 (PDF pp. 5–9); §V.B.2, printed pp. 22–25 (PDF pp. 26–29)"
tags:
  - medical-device
  - diagnostics
  - care-delivery
  - patient-safety
  - hypothetical
---

# Medical-device cyber disruption affecting diagnosis or care

> [!WARNING]
> **Evidence classification**
> This is a **hypothetical FDA-guidance path**, not an incident or product
> finding. FDA describes possible device/system safety consequences and cites
> historical events secondarily; it does not document a complete named-device
> path, likelihood, patient injury or control failure.

## Scenario

A cybersecurity condition affects a medical device or a dependency in its
larger system. Device functionality, diagnostic-result reporting, alarming,
programming, treatment delivery or availability is altered or lost. If the
condition is not prevented, detected, contained or recovered before a clinical
decision/action, it can delay diagnosis or treatment, interrupt care or create
a patient-safety hazard. Connected common dependencies can make the potential
scope multi-device or multi-patient.

The page does not identify a product, facility, patient, interface, credential,
vulnerability or attack sequence. Device classification and harm are not
assumed for any existing wiki system.

## Preconditions and boundaries

The conditional path requires:

1. a medical device function or safety-relevant related-system dependency;
2. a cybersecurity condition able to alter availability, integrity,
   authorization, execution or trusted communication;
3. reliance on the affected function for diagnosis, reporting, monitoring,
   programming, treatment or another care action;
4. insufficient prevention/detection or a delay/failure in safe containment,
   fallback, communication or recovery; and
5. a clinical exposure capable of creating delay or patient harm.

Connectivity alone does not prove exploitability, and a device anomaly alone
does not prove clinical harm.

> **Claim record — RSK-0012-C01 | source-report**
> **Claim:** FDA describes a conditional device/system cybersecurity path in
> which compromised function or availability can disrupt diagnostic reporting
> or care and may create delay, multi-patient exposure or patient harm.
> **Claim status:** active
> **Scope:** Potential U.S. medical-device safety path in guidance, not a named
> event, product defect, probability or observed patient outcome.
> **As of:** 2026-02-03.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§I–III, printed pp. 1–5 (PDF pp. 5–9); §V.B.2, especially global-system,
> multi-patient-harm and security-use-case views, printed pp. 22–25
> (PDF pp. 26–29).
> **Basis / limits:** FDA directly states the possible safety/care dependency.
> It provides no end-to-end primary case or measured likelihood.

## Origin and transfer

The origin is a digital security state affecting a device or system dependency.
The transfer mechanism is functional and decisional: the altered or unavailable
digital state changes what a device reports, monitors, commands, delivers or
makes available to a clinician/patient. The first receiving state can remain
digital or become a clinical action/failure before any biological consequence.

> **Claim record — RSK-0012-C02 | analytic-judgment**
> **Claim:** The safe canonical path is `digital security condition → device or
> related-system function → diagnostic/care decision or action → conditional
> patient consequence`, with every transition requiring deployment facts.
> **Claim status:** active
> **Scope:** Defensive scenario abstraction from FDA's system/safety model; no
> operational mechanism or target.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §III, printed pp. 3–5 (PDF pp. 7–9); §§V.A–B, printed pp. 10–25
> (PDF pp. 14–29); Appendix 5 definitions of system and patient harm,
> printed pp. 57–59 (PDF pp. 61–63).
> **Basis / limits:** System elements and safety-relevant use cases are direct;
> the compact sequence is editorial. No actor, vector or clinical threshold is
> established.

## Consequences

Potential consequences include unavailable or altered device function,
untrusted diagnostic results, delayed diagnosis/treatment, diverted or
interrupted care and direct or indirect patient harm. Each is conditional.
Operational disruption is not relabeled as injury, and the guidance's
secondary historical references are not independent evidence for this path.

> **Claim record — RSK-0012-C03 | source-report**
> **Claim:** FDA distinguishes device/system compromise and care delay from the
> further possibility of patient harm; the latter is not automatic.
> **Claim status:** active
> **Scope:** Consequence categories in the guidance, not severity, incidence or
> attribution.
> **As of:** 2026-02-03.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §I, printed pp. 1–2 (PDF pp. 5–6); §V.A, printed pp. 10–13
> (PDF pp. 14–17); Appendix 5, `Patient harm`, printed p. 57 (PDF p. 61).
> **Basis / limits:** Potential effects and risk distinctions are direct. The
> source contains no patient cohort, injury determination or frequency.

## Evidence and uncertainty

This scenario has one normative FDA lineage. It is not corroborated by the EU
EHDS regulation, which governs health data/EHR systems rather than proving a
medical-device safety path. Current NHS/Synnovis pages document a different
laboratory service disruption and do not identify an FDA-covered device.

> **Claim record — RSK-0012-C04 | analytic-judgment**
> **Claim:** `RSK-0012` remains hypothetical and single-lineage; no `INC`, THR,
> VUL, affected product, causal patient outcome or deployment-specific
> likelihood follows from FDA's guidance.
> **Claim status:** active
> **Scope:** Evidence classification for this scenario.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> full-document review; `SRC-0017-C05/C10`.
> **Basis / limits:** Source genre and missing case-level evidence are direct.
> This does not establish that no medical-device incidents exist elsewhere.

## Controls by function

[CTL-0010](../controls/ctl-0010-medical-device-cybersecurity-lifecycle-controls.md)
conditionally maps prevention, detection, containment/response, recovery and
assurance to this path. Its recommendations and cited scoped duties do not
prove a product implements or survives those controls.

## Related scenarios

- [RSK-0006 — Observed transfusion-service disruption](rsk-0006-transfusion-testing-disruption-supply-pressure.md) is an operational
  laboratory/supply path; no affected FDA-regulated device is inferred.
- [RSK-0003 — Genomic integrity/decision harm](rsk-0003-genomic-data-integrity-decision-harm.md) is data/provenance-specific and
  is not generalized from FDA's device guidance.

## Related pages

- [SRC-0017 — FDA guidance 2026](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [GOV-0007 — FDA medical-device governance](../governance/gov-0007-us-fda-medical-device-cybersecurity-2026.md)
- [CTL-0010 — Medical-device lifecycle controls](../controls/ctl-0010-medical-device-cybersecurity-lifecycle-controls.md)
- [SYN-0005 — Global/US/EU clinical-health governance](../syntheses/syn-0005-global-us-eu-clinical-health-governance.md)
- [SYN-0006 — Official control function/state taxonomy](../syntheses/syn-0006-official-control-function-state-taxonomy.md)

## Sources

- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md), at the
  exact locators in the claims above.
