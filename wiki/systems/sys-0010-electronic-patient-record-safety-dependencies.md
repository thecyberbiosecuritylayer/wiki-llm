---
id: SYS-0010
type: system
title: Electronic patient record safety dependencies
aliases:
  - EPR sociotechnical safety-dependency map
  - electronic patient record module and lifecycle boundaries
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0030
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0030
    claim_id: SYS-0010-C01
    evidence:
      - source: SRC-0030
        locator: "HSSIB physical pp. 2–5, 7–23 and 36–39"
  - predicate: depends-on
    target: AST-0006
    claim_id: SYS-0010-C02
    evidence:
      - source: SRC-0030
        locator: "HSSIB physical pp. 2–4, 9–15, 17–23 and 37"
tags:
  - clinical-care
  - electronic-patient-record
  - module-boundary
  - sociotechnical-system
  - patient-safety
  - configuration
  - interoperability
  - governance
---

# Electronic patient record safety dependencies

## Bounded class map

| Class or boundary | Safety-relevant function | Dependency that must remain explicit |
| --- | --- | --- |
| whole EPR / modular EPR | collect, store and manage individual-patient clinical information | one product may provide many modules, or different developers may provide separate modules |
| administration/appointments | associate patient, encounter and scheduling state | identity, accessibility, handoff and local process |
| clinical records/plans | make relevant care information available and findable | correct state, presentation, authorization, correction and staff workflow |
| diagnostics/orders/results | request tests and return information for interpretation/action | module/interface status, recipient, acknowledgement and downstream decision |
| medicines/ePMA | order and manage medication information | configuration, decision support, user action and care context |
| decision-support tools | present calculations, alerts or risk/decision information | input quality, current guidance, usability and human review |
| adjunct/interfacing software | exchange or extend EPR functions without necessarily being part of the EPR | product/module ownership, interoperability and responsibility boundary |
| infrastructure | provide usable devices, networks and physical access | hardware availability, Wi-Fi, environment, continuity and paper/electronic fallback |

The map uses HSSIB's review-specific sample boundary. Resource-management and
business-analytics modules were excluded from that sample, so their absence
from this page is not a claim that they are never part of a wider health-IT
ecosystem.

> **Claim record — SYS-0010-C01 | analytic-judgment**
> **Claim:** HSSIB supports a bounded EPR class map that distinguishes a whole
> system, specific modules, adjunct/interfacing software and infrastructure,
> while preserving uncertainty where underlying reports did not identify
> whether a module was standalone or part of a larger EPR.
> **Claim status:** active
> **Scope:** Cross-report functional classes, not a deployed topology, product
> inventory, universal EPR definition or assertion that every component is
> present in every setting.
> **As of:** 2025-11-27.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md),
> `SRC-0030-C03/C07/C08`; HSSIB physical pp. 2–5, 7–12, 27 and 37–39.
> **Basis / limits:** Module classes and ambiguity are direct. The single-
> versus multi-developer figure is conceptual, not a facility architecture.

## Sociotechnical dependency map

1. `needs → documented requirements → product/module capabilities`
2. `standards/risk expectations → selection and procurement scrutiny`
3. `procured design → local configuration → representative-user testing`
4. `EPR/module → existing technology + people + care processes`
5. `hardware/network/environment → usable access at the point of care`
6. `launch/change → training + contingency + operational support`
7. `care use → feedback/issue learning → correction and optimisation`
8. `local/regional/national/developer accountability → lifecycle governance`

> **Claim record — SYS-0010-C02 | analytic-judgment**
> **Claim:** EPR safety depends jointly on software design, local
> configuration/integration, patient and staff needs, real work, hardware and
> connectivity, training/contingency, feedback/optimisation and lifecycle
> governance; HSSIB's review does not support a universal single-factor cause.
> **Claim status:** active
> **Scope:** Defensive sociotechnical dependency abstraction across HSSIB's
> report corpus, not blame allocation or causality for a named event.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C08/C10`; HSSIB §§3.2–3.5, physical pp. 15–23;
> Appendix B contributory coding, pp. 41–49; affected asset/stakeholder classes
> in [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md).
> **Basis / limits:** The dependency classes recur in the review, but code
> overlap and a purposive corpus prevent prevalence or universal-cause claims.

## Failure states and consequence boundary

| State class | Safe abstraction | What is not inferred |
| --- | --- | --- |
| unavailable | needed information/function/system cannot be accessed | cyberattack, outage cause or rate |
| unfindable | information exists but is not surfaced or located in work | a universal UI defect |
| incorrect or difficult-to-correct | record state can lead to continuing decision risk | one data-entry mechanism or named product cause |
| non-interoperable | information/function does not cross an organizational or module boundary as needed | protocol-level fault |
| misconfigured or poorly integrated | local adaptation/process interaction introduces or fails to control risk | software-only or organization-only blame |
| absent control/function | a known-risk interruption is unavailable | effectiveness of an untested replacement |
| consequence | care may be missed, delayed or incorrect; some source reports describe direct harm contribution | incident rate, harmed-patient count or independent case confirmation |

> **Claim record — SYS-0010-C03 | source-report**
> **Claim:** The reviewed system states can create conditions for missed,
> delayed or incorrect care, including misidentification, and some underlying
> reports described direct contributions to patient harm; HSSIB provides no
> national rate, denominator or independently reviewable case count here.
> **Claim status:** active
> **Scope:** Systems-level outcome evaluation, not a new incident page,
> independent confirmation of each prior case or measured safeguard effect.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C06/C09`; HSSIB Executive Summary, physical pp. 3–7;
> §2.3, pp. 12–15; Appendix B, pp. 39 and 43–46.
> **Basis / limits:** Report-code frequencies, potential harm and direct
> contribution language are preserved as different units/evidence states.

> **Claim record — SYS-0010-C04 | analytic-judgment**
> **Claim:** Electronic prescribing and medicines administration is one
> medication-management module/example within the broader EPR review; neither
> every EPR nor HSSIB's general findings can be treated as an allergy-screening
> system or proof of a particular allergy-record interface cause.
> **Claim status:** active
> **Scope:** Module and causal boundary relevant to later clinical-outcome
> reconciliation; not denial that medication modules can affect patient safety.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C04/C07/C12`; HSSIB physical pp. 10, 12–14, 27 and
> 37; bounded absence-of-term search described in `SRC-0030-C04`.
> **Basis / limits:** HSSIB distinguishes whole systems, modules and adjuncts.
> Its derivative medication vignette is not treated as the NatPSA event.

## Review-unit and evidence-state boundary

> **Claim record — SYS-0010-C05 | analytic-judgment**
> **Claim:** The `112 → 63 → 50` flow and Appendix B frequencies describe
> screening, included reports, full-report coding and overlapping themes—not
> deployments, independent lineages, incidents, patients, harmed patients or
> measured near misses.
> **Claim status:** active
> **Scope:** Unit discipline for this system map and downstream rubric use.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C02/C05/C06`; HSSIB physical pp. 10, 15 and 36–49.
> **Basis / limits:** The report stages overlap, codes are non-exclusive and
> the corpus is one issuer's prior investigations.

> **Claim record — SYS-0010-C06 | analytic-judgment**
> **Claim:** This independent systems evaluation supplies broader context for
> availability/findability/handoff and incorrect-state/integration mechanisms
> represented in separate clinical risk pages, but does not investigate or
> corroborate their event facts, patient identities, exact root causes or
> shared-system hypothesis.
> **Claim status:** active
> **Scope:** Claim-appropriate system-class context, not same-event
> confirmation or causal synthesis.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C04/C08`–`C10`; HSSIB physical pp. 10–23 and 36–49;
> separate clinical risk pages retain their own event-specific evidence.
> **Basis / limits:** The HSSIB source lacks event-specific searched terms and
> predates the NatPSA. Common system classes do not establish common events.

> **Claim record — SYS-0010-C07 | artifact-observation**
> **Claim:** The map distinguishes systems-risk evaluation, recommendation,
> implementation, test and independently evaluated effectiveness; HSSIB
> supplies the first and recommendation/observation outputs, not the latter
> three, so this source transaction changes no frozen cell or global gate.
> **Claim status:** active
> **Scope:** Evidence maturity and zero-delta rubric boundary before separate
> outcome reconciliation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C10`–`C13`; frozen `CPH-CI/AE`, CTR and global-gate
> criteria in [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Evaluation of a problem class is not evaluation of a
> safeguard. The independent evaluation predicate can be reconciled only in a
> separate synthesis transaction.

## Safety boundary

This page contains system/module classes, abstract dependency states and
defensive lifecycle questions only. It excludes patient/facility identifiers,
medication/dose details, live topology, vendors, endpoints, credentials,
protocol recipes, interface fields, local configurations and exploitable
failure instructions.

## Related pages

- [SRC-0030 — HSSIB thematic review](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md)
- [AST-0006 — clinical/public-health assets and stakeholders](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [SYS-0009 — complementary laboratory/exchange architecture](sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [RSK-0015 — separate wrong-entry event mechanism](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md)

## Sources

- [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md)
