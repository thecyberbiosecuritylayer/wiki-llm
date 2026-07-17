---
id: RSK-0013
type: risk-scenario
title: Laboratory result disruption or corruption affecting clinical/public-health decisions
aliases:
  - laboratory information to care decision path
  - specimen input to public-health decision path
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0014
  - SRC-0016
  - SRC-0017
  - SRC-0026
sensitivity: public
dual_use: low
origin_domain: mixed
destination_domains:
  - digital
  - clinical
  - public-health
  - biological
relations:
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: RSK-0013-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 10–15, 61–72, 152–168 and 193–207"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: RSK-0013-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22, 92 and 97"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: RSK-0013-C02
    evidence:
      - source: SRC-0009
        locator: "article update paragraphs 2–3; HTML lines 190–191"
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: RSK-0013-C01
    evidence:
      - source: SRC-0005
        locator: "§§1.1 and 3.1–3.5, printed pp. 1–2 and 9–11/PDF pp. 10–11 and 18–20"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: RSK-0013-C03
    evidence:
      - source: SRC-0014
        locator: "controlled reverse-path study, Abstract/Introduction and §3, printed pp. 765–766 and 768–771/PDF pp. 2–3 and 5–8, at safe abstraction"
  - predicate: depends-on
    target: WFL-0010
    claim_id: RSK-0013-C04
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS total-testing workflow pp. 11–15 and reporting/correction pp. 193–207"
  - predicate: depends-on
    target: SYS-0008
    claim_id: RSK-0013-C04
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS information system pp. 197–207"
      - source: SRC-0016
        locator: "EHDS Articles 3–30, PDF pp. 34–46"
  - predicate: affects
    target: AST-0006
    claim_id: RSK-0013-C05
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 10, 62, 152–166"
      - source: SRC-0009
        locator: "NHS England update paragraphs 2–3"
tags:
  - clinical-laboratory
  - public-health
  - result-integrity
  - availability
  - decision
  - bidirectional
  - mixed-evidence
---

# Laboratory result disruption or corruption affecting clinical/public-health decisions

> [!WARNING]
> **Evidence classification**
> This page reconciles two path classes. Availability→service/care delay has an
> observed NHS event; generic integrity manipulation and specimen/input→digital
> decision effects remain hypothetical/controlled or source-reported hazards.
> They are not merged into one incident or likelihood estimate.

## Path A — digital state to laboratory/care/public-health action

`digital availability or integrity state → instrument/interface/LIS/reporting
function → result absent, delayed or untrusted → clinical/public-health user
cannot act or acts on the altered state → conditional service, safety or
population consequence`.

> **Claim record — RSK-0013-C01 | analytic-judgment**
> **Claim:** WHO's normal result/report/interpretation dependency and current
> NIST/FDA digital integrity/availability models jointly support a complete
> conditional digital→test/report→care/public-health-action path.
> **Claim status:** active
> **Scope:** Cross-source defensive scenario, not a named integrity incident,
> product vulnerability, probability or deterministic patient outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C07/C08`, pp. 10–15, 152–166 and 193–207;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C05/C07`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04/C05`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08`.
> **Basis / limits:** Digital failure possibilities and normal decision
> dependency are direct across independent lineages; the end-to-end path is an
> analytic conditional, not a case reconstruction.

> **Claim record — RSK-0013-C02 | analytic-judgment**
> **Claim:** The Synnovis records independently anchor the availability branch:
> ransomware reduced pathology/test capacity, disrupted specific compatibility
> functions and delayed care, but no result corruption or confirmed patient
> injury is reported.
> **Claim status:** active
> **Scope:** June–December 2024 NHS service-disruption context; not evidence for
> generic integrity or public-health-surveillance manipulation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C03/C04`; [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> `SRC-0009-C03/C04`; [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> `SRC-0007-C04` only for the separate privacy-state boundary.
> **Basis / limits:** Two official issuers support event/capacity/delay states,
> but not every laboratory edge or biological harm.

## Path B — specimen/material input to digital interpretation/decision

`specimen or material identity/quality/input state → examination/sequencing or
software processing → digital result/report → interpretation/decision →
conditional clinical/public-health consequence`.

> **Claim record — RSK-0013-C03 | analytic-judgment**
> **Claim:** WHO directly supports specimen identity/quality→result→decision
> dependence, while controlled USENIX evidence independently shows that a
> biological/material input can alter a digital processing state; together they
> support the reverse-direction class without claiming a clinical incident.
> **Claim status:** active
> **Scope:** Material/input→digital-decision mechanism class; no sequence,
> exploit mechanics, patient sample, observed diagnosis or public-health event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C06/C08`, pp. 10–15, 61–72 and 162–166;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> `SRC-0014-C02/C08` at safe abstraction; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C04/C07`.
> **Basis / limits:** Normal clinical dependency and controlled digital-input
> execution are materially independent. The combined decision path remains
> analytic and does not transplant controlled-study conditions into care.

## Transfer, consequences and controls

> **Claim record — RSK-0013-C04 | analytic-judgment**
> **Claim:** The transfer mechanisms are association, data/report transmission,
> functional availability and human/automated decision reliance across
> [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
> and [SYS-0008](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md).
> **Claim status:** active
> **Scope:** Canonical exact-edge model; no deployment topology or operational
> attack path.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `RSK-0013-C01`–`C03`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C05/C06`.
> **Basis / limits:** Mechanisms are direct across sources; their normalization
> is analytic and context-dependent.

> **Claim record — RSK-0013-C05 | analytic-judgment**
> **Claim:** Confirmed consequences are bounded to the NHS availability/service
> effects; inappropriate care/public-health action, biological injury or
> population harm remain conditional unless a separate primary outcome case is
> ingested.
> **Claim status:** active
> **Scope:** Evidence-state separation for affected [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md).
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `RSK-0013-C01`–`C03`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C03/C04`; [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> `SRC-0009-C03/C04`; WHO possible consequences `SRC-0026-C08`.
> **Basis / limits:** Service effects and possible harms have different
> evidence predicates; the latter are not upgraded by proximity.

> **Claim record — RSK-0013-C06 | artifact-observation**
> **Claim:** Independent strict review accepts the two full SF2 directions for
> `CPH-XT`, while `CPH-CI`, `CPH-AE` and the global directionality/incident/
> control gates remain unchanged.
> **Claim status:** active
> **Scope:** Accepted frozen-rubric cell boundary after independent review.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `RSK-0013-C01`–`C05`; frozen CPH/global criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Sector-level transfer directions are complete; the
> stricter global reverse-to-digital-decision gate still lacks a corroborated
> observed outcome and the primary patient/population case floor is unmet.

## Controls

[CTL-0012](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md)
maps identity, validation, authorization, integrity, notification, downtime and
recovery functions to the exact edges. It does not establish effectiveness.

## Related pages

- [SYN-0023 — Laboratory transfer/incident reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [HAZ-0002 — non-adversarial failure](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md)
- [RSK-0003 — genomic integrity decision harm](rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0006 — observed availability/material-pressure path](rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [RSK-0009 — controlled material/input→digital execution](rsk-0009-sequenced-input-to-digital-execution.md)
- [SYN-0013 — CPH reconciliation](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
