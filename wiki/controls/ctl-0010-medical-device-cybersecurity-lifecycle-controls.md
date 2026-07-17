---
id: CTL-0010
type: control
title: Medical-device cybersecurity lifecycle controls
aliases:
  - FDA device cybersecurity control family
  - medical-device secure product lifecycle controls
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0017
sensitivity: public
dual_use: low
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: CTL-0010-C01
    evidence:
      - source: SRC-0017
        locator: "§V.B.1, printed pp. 21–22 (PDF pp. 25–26); Appendix 1, printed pp. 38–46 (PDF pp. 42–50)"
  - predicate: governed-by
    target: GOV-0007
    claim_id: CTL-0010-C01
    evidence:
      - source: SRC-0017
        locator: "Introductory notice and §§I–II, printed pp. 1–3 (PDF pp. 5–7); §VII, printed pp. 30–37 (PDF pp. 34–41)"
  - predicate: mitigates
    target: RSK-0012
    claim_id: CTL-0010-C02
    evidence:
      - source: SRC-0017
        locator: "§§V.A–B, printed pp. 10–25 (PDF pp. 14–29); Appendix 1, printed pp. 38–46 (PDF pp. 42–50)"
  - predicate: detects
    target: RSK-0012
    claim_id: CTL-0010-C03
    evidence:
      - source: SRC-0017
        locator: "§V.C, printed pp. 25–27 (PDF pp. 29–31); Appendix 1, Event Detection and Logging, printed pp. 43–45 (PDF pp. 47–49)"
  - predicate: contains
    target: RSK-0012
    claim_id: CTL-0010-C04
    evidence:
      - source: SRC-0017
        locator: "§VI.B and §VII.C, printed pp. 30–35 (PDF pp. 34–39); Appendix 1, printed pp. 43–46 (PDF pp. 47–50)"
  - predicate: recovers
    target: RSK-0012
    claim_id: CTL-0010-C04
    evidence:
      - source: SRC-0017
        locator: "§VI.A, printed pp. 27–30 (PDF pp. 31–34); Appendix 1, Resiliency and Recovery/Firmware and Software Updates, printed pp. 45–46 (PDF pp. 49–50)"
tags:
  - medical-device
  - secure-product-development
  - prevention
  - detection
  - response
  - recovery
  - assurance
---

# Medical-device cybersecurity lifecycle controls

## Scope and evidence state

This page translates FDA's device-specific design and lifecycle guidance into
the wiki's defensive control functions. It does not replace product risk
assessment, submission review, current law or user/facility controls. The FDA
document contains recommendations and descriptions of scoped duties, not a
deployed control set.

> **Claim record — CTL-0010-C01 | source-report**
> **Claim:** FDA supplies eight named technical categories—authentication,
> authorization, cryptography, code/data/execution integrity, confidentiality,
> event detection/logging, resiliency/recovery and firmware/software updates—
> inside a broader lifecycle risk and assurance process.
> **Claim status:** active
> **Scope:** Medical devices within FDA guidance scope; no universal baseline
> for every device, clinical system or provider.
> **As of:** 2026-02-03.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §V.B.1, printed pp. 21–22 (PDF pp. 25–26); Appendix 1, printed
> pp. 38–46 (PDF pp. 42–50); §§V.A, V.C and VI, printed pp. 10–19,
> 25–30 (PDF pp. 14–23, 29–34).
> **Basis / limits:** Categories and lifecycle processes are direct. Their
> selection, implementation and sufficiency are product/system-specific.

## Prevent and reduce exposure

For [RSK-0012](../risk-scenarios/rsk-0012-medical-device-cyber-disruption-care-harm.md),
prevention addresses the first two edges: insecure/untrusted access or input to
an altered device/system function. Controls include scoped authentication and
authorization, confidentiality and integrity protection, secure architecture,
component/SBOM management, least privilege, safe defaults and trustworthy
updates. No single control prevents every availability or safety hazard.

> **Claim record — CTL-0010-C02 | analytic-judgment**
> **Claim:** FDA preventive categories conditionally mitigate unauthorized or
> untrusted state reaching a safety-relevant device/system function in
> `RSK-0012`, subject to architecture, user, supplier, lifecycle and clinical-
> environment prerequisites.
> **Claim status:** active
> **Scope:** FDA-covered device branch of `RSK-0012`; not a guarantee against
> compromise, misconfiguration, misuse or non-cyber failure.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V.A–B, printed pp. 10–25 (PDF pp. 14–29); Appendix 1, printed
> pp. 38–43 and 45–46 (PDF pp. 42–47, 49–50).
> **Basis / limits:** Intended functions are direct; exact scenario-edge mapping
> is editorial. Product implementation and residual-risk acceptance are absent.

## Detect and characterize

Event detection/logging, anomaly notification, vulnerability monitoring,
threat modeling, component inventory and verification/testing can expose
conditions before or after functional impact. Detection must preserve usable
timestamps/context and be actionable; a log or submitted test report does not
prove timely detection in deployment.

> **Claim record — CTL-0010-C03 | analytic-judgment**
> **Claim:** FDA event/logging, monitoring and verification functions
> conditionally detect device/system conditions and control weaknesses along
> `RSK-0012`, but the guidance reports no detection coverage, latency or field
> result.
> **Claim status:** active
> **Scope:** Recommended device/system detection and assurance functions, not a
> named deployment or incident detector.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V.A.4–A.6 and V.C, printed pp. 15–19, 25–27 (PDF pp. 19–23,
> 29–31); Appendix 1, Event Detection and Logging, printed pp. 43–45
> (PDF pp. 47–49).
> **Basis / limits:** Intended monitoring/testing functions are direct. No
> empirical false-positive, missed-detection or time-to-detect evidence exists.

## Contain, communicate and recover

The family combines critical-function protection, degraded/independent
operation, trusted configuration recovery, authorized update/patch processes,
vulnerability disclosure, user communication, field correction and lifecycle
plans. The clinically safe response is device/use-context specific: isolation,
shutdown or update can itself interrupt care.

> **Claim record — CTL-0010-C04 | analytic-judgment**
> **Claim:** FDA resilience, vulnerability-management, communication, field-
> action and trusted-update/restore functions conditionally contain and recover
> `RSK-0012`, while requiring benefit-risk judgment to avoid response-induced
> loss of clinical function.
> **Claim status:** active
> **Scope:** Device/system response and recovery design; no operational
> instruction, recovery-time claim or demonstrated safe state.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§VI–VII, printed pp. 27–37 (PDF pp. 31–41); Appendix 1,
> Event Detection and Logging, Resiliency and Recovery, and Firmware and
> Software Updates, printed pp. 43–46 (PDF pp. 47–50).
> **Basis / limits:** Functions and benefit-risk boundary are direct; exact edge
> mapping is inferred. Restore trust, timeliness and patient outcome are unknown.

## Assure

FDA asks for threat/risk models, architecture views, traceability, verification/
validation, vulnerability assessment, security testing, tester-independence
disclosure, labeling and postmarket plans. Those artifacts can support
assurance, but requested evidence is not a completed or favorable result.

> **Claim record — CTL-0010-C05 | source-report**
> **Claim:** FDA's assurance design requires or recommends traceable risk,
> architecture and test evidence with tester provenance, without supplying a
> product test, independent evaluation or effectiveness conclusion itself.
> **Claim status:** active
> **Scope:** Guidance-level assurance design and cited scoped requirements.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V.A–C, printed pp. 10–27 (PDF pp. 14–31); Appendix 4,
> printed pp. 51–53 (PDF pp. 55–57).
> **Basis / limits:** Evidence requests are direct. Submission, test outcome,
> FDA decision, implementation and independent causal evaluation are absent.

## Prerequisites, failure modes and tradeoffs

- scope/classification and intended/use environment must be correct;
- manufacturer, supplier, facility, clinician and patient responsibilities
  must be feasible and communicated;
- controls must preserve clinical safety, availability and usability;
- device and related-system boundaries, components and update dependencies can
  change over the lifecycle;
- external/compensating controls may be unavailable or shift risk to users;
- logs, SBOMs, labels and declarations can be incomplete or stale;
- update/containment action can create downtime or unsafe transition;
- end-of-support and third-party discontinuity can reduce maintainability.

> **Claim record — CTL-0010-C06 | analytic-judgment**
> **Claim:** The mapped family can fail through scope/boundary error, stale
> evidence, supplier/user dependency, unsafe intervention or lifecycle loss of
> support, so its residual clinical risk cannot be inferred from design labels.
> **Claim status:** active
> **Scope:** Failure/tradeoff synthesis from FDA guidance, not a measured failure
> rate or product finding.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§IV.B–D and V.A–C, printed pp. 7–27 (PDF pp. 11–31); §VI,
> printed pp. 27–30 (PDF pp. 31–34); Appendix 1, printed pp. 38–46.
> **Basis / limits:** Dependency and benefit-risk caveats are direct; the compact
> failure list is editorial and no failure prevalence is claimed.

## Evidence maturity

| State | Current evidence for `CTL-0010` |
| --- | --- |
| Recommended | Yes; FDA guidance recommendations |
| Binding design | Only where separately cited QMSR/§524B predicates apply |
| Implemented | Unknown |
| Tested | Unknown; testing requested is not a result |
| Effective | Unknown |
| Independently evaluated | Unknown |

> **Claim record — CTL-0010-C07 | analytic-judgment**
> **Claim:** `CTL-0010` remains recommended/scoped-binding design; no represented
> implementation, passed test, effectiveness or independent evaluation is
> established.
> **Claim status:** active
> **Scope:** Evidence ladder for this control page and transaction.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C03/C08/C10`; §§V.C and VII.E, printed pp. 25–27 and 36–37
> (PDF pp. 29–31 and 40–41).
> **Basis / limits:** Source modality and absence of result data are direct.
> Separate product/test evidence may change these states later.

## Related pages

- [SRC-0017 — FDA guidance 2026](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [GOV-0007 — FDA medical-device governance](../governance/gov-0007-us-fda-medical-device-cybersecurity-2026.md)
- [RSK-0012 — Medical-device cyber disruption and care harm](../risk-scenarios/rsk-0012-medical-device-cyber-disruption-care-harm.md)
- [SYN-0006 — Official control function/state taxonomy](../syntheses/syn-0006-official-control-function-state-taxonomy.md)
- [CTL-0009 — EHDS safeguards](ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [SYN-0007 — Cross-sector exact control-edge portfolio](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md), at the
  claim locators above.
