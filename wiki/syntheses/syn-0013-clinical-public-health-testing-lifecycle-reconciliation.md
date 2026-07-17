---
id: SYN-0013
type: synthesis
title: Clinical and public-health testing, hazard, transfer and control reconciliation
aliases:
  - CPH six-cell reconciliation
  - WHO LQMS NIST EHDS FDA NHS clinical testing synthesis
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
jurisdictions:
  - Global
  - United States
  - United Kingdom
  - European Union
relations:
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0026
        locator: "complete WHO LQMS Version 1.1, pp. 1–248, especially pp. 7–17, 36–48, 61–124, 152–168 and 182–222"
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0005
        locator: "NIST IR 8432 §§1.1–4.4.3, printed pp. 1–22/PDF pp. 10–31"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0007
        locator: "SP 1800-43C §§1.2–2.4, printed pp. 2–43/PDF pp. 11–52"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0008
        locator: "NHSBT pp. 9–10, 20–24, 92, 97 and 122–125"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0009
        locator: "NHS England update paragraphs 1–3, HTML lines 189–191"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0014
        locator: "controlled input/exposure/software study, printed pp. 765–778/PDF pp. 2–15 at safe abstraction"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0016
        locator: "EHDS Articles 1–46 and Annexes I–III, PDF pp. 29–55 and 92–95"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: SYN-0013-C01
    evidence:
      - source: SRC-0017
        locator: "FDA guidance §§I–VI and Appendix 1, printed pp. 1–30 and 38–46/PDF pp. 5–34 and 42–50"
tags:
  - clinical-laboratory
  - public-health
  - genomics
  - lifecycle
  - hazards
  - cross-domain-transfer
  - controls
  - evidence-quality
---

# Clinical and public-health testing, hazard, transfer and control reconciliation

## Question, cutoff and lineage rules

This synthesis tests only `CPH-ST/AS/WL/TV/XT/CT` at the 2026-07-12 cutoff.
WHO LQMS, NIST, EU, FDA, NHSBT/NHS England and USENIX are counted according to
their actual claim lineages. WHO/CDC/CLSI co-development of one handbook is one
lineage. NHSBT and NHS England are two issuers in one response ecosystem and do
not independently corroborate every incident edge. Normative, controlled-study
and observed-event predicates are never merged.

> **Claim record — SYN-0013-C01 | analytic-judgment**
> **Claim:** The portfolio is SF2-appropriate for six frozen CPH criteria because
> the WHO total-testing/QMS lineage is reconciled with materially independent
> NIST genomics/privacy, EU health-data/EHR, FDA device, NHS operational and
> controlled USENIX evidence, each used only for its direct predicate.
> **Claim status:** active
> **Scope:** Source independence and evidence-class accounting; not global
> implementation, legal equivalence or a combined effectiveness study.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C01`–`C12`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C03`–`C07`; [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> `SRC-0007-C02`–`C06`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C02`–`C05`; [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> `SRC-0009-C02`–`C04`; [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> `SRC-0014-C02/C04`–`C06/C08`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C03/C05/C08/C09`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04`–`C09`.
> **Basis / limits:** Genres, issuers, derivative links and predicate limits are
> explicit. Document count is not treated as independence.

## Criterion reconciliation matrix

| Cell | Literal criterion coverage | Independent evidence and boundary | Candidate |
| --- | --- | --- | :---: |
| `CPH-ST` | clinical diagnostics/genomics, laboratory medicine, care delivery, public-health reporting/surveillance | WHO LQMS clinical/public-health scope + NIST genomics + FDA diagnostic-device and EHDS care/data contexts | Pass |
| `CPH-AS` | specimen/patient identity, orders/results, instruments, LIS/EHR/reporting, clinicians, patients, relatives, populations | complete `AST-0006`; no actual record or deployment | Pass |
| `CPH-WL` | order→collection→accession→test→interpret→report→notify/action→retain/reanalyse/correct | complete `WFL-0010`; normalized across WHO and current data/operational lineages | Pass |
| `CPH-TV` | cyber manipulation/outage, identity/specimen mismatch, privacy, quality hazards, specific exposure | NIST/FDA possibilities, observed NHS outage, WHO `HAZ-0002`, NIST privacy and USENIX bounded exposure; no likelihood | Pass |
| `CPH-XT` | digital→test/report/care/public-health and specimen/input→digital interpretation/decision | two full `RSK-0013` paths; evidence states separated | Pass |
| `CPH-CT` | identity, validation, authorization, result integrity, notification, downtime, recovery on exact edges | complete `CTL-0012`; requirements/implementation/effectiveness separated | Pass |

> **Claim record — SYN-0013-C02 | analytic-judgment**
> **Claim:** `CPH-ST` is complete at SF2: WHO distinguishes clinical/
> diagnostic/medical/public-health laboratory purposes and surveillance, while
> independent NIST, FDA and EHDS sources add literal genomics, diagnostic-
> device and care/health-data contexts.
> **Claim status:** active
> **Scope:** Frozen scope/terms criterion only; not a universal taxonomy or
> current governance conclusion from the 2011 handbook.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0013-C01`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C02/C04`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C04/C05`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04/C05`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C03/C05`.
> **Basis / limits:** Every literal scope limb is direct across independent
> lineages; terms are reconciled rather than declared equivalent.

> **Claim record — SYN-0013-C03 | analytic-judgment**
> **Claim:** `CPH-AS` is complete at SF2 through `AST-0006-C01`–`C03`, with
> all literal asset/stakeholder classes present and identity, privacy and system
> trust states kept distinct.
> **Claim status:** active
> **Scope:** Frozen asset/stakeholder criterion only.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md),
> `AST-0006-C01`–`C03`; underlying source relations in `SYN-0013-C01`.
> **Basis / limits:** Class coverage is complete; no inventory, topology or
> implementation is inferred.

> **Claim record — SYN-0013-C04 | analytic-judgment**
> **Claim:** `CPH-WL` is complete at SF2 through `WFL-0010-C01`–`C04`, which
> preserves material, information, decision, retention/reanalysis and
> correction/notification branches across independent lineages.
> **Claim status:** active
> **Scope:** Frozen workflow/lifecycle criterion only.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md),
> `WFL-0010-C01`–`C04`; underlying source relations in `SYN-0013-C01`.
> **Basis / limits:** The normalization is explicit; no one source is said to
> contain a modern deployed end-to-end digital workflow.

> **Claim record — SYN-0013-C05 | analytic-judgment**
> **Claim:** `CPH-TV` is complete at SF2 because the corpus separately covers
> malicious/integrity possibilities, observed outage, identity/specimen error,
> privacy threats, non-adversarial quality hazards and a version-bounded
> technical exposure without converting any into a prevalence estimate.
> **Claim status:** active
> **Scope:** Frozen threat/hazard/vulnerability/exposure criterion only; not a
> current threat-intelligence feed or incident attribution.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [HAZ-0002](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md),
> `HAZ-0002-C01`–`C04`; `SRC-0005-C07`; `SRC-0007-C04/C05`;
> `SRC-0008-C03`; `SRC-0009-C03`; `SRC-0014-C04`–`C06`;
> `SRC-0017-C05`; `SRC-0026-C08/C11`.
> **Basis / limits:** Required classes arise from independent evidence genres.
> The USENIX exposure is controlled/version-bounded and NHS availability is
> observed; neither generalizes to all laboratories.

> **Claim record — SYN-0013-C06 | analytic-judgment**
> **Claim:** `CPH-XT` is complete at SF2 through `RSK-0013-C01`–`C05`, which
> distinguishes the digital→test/report/action and specimen/material-input→
> digital-interpretation/decision directions and their evidence maturity.
> **Claim status:** active
> **Scope:** Frozen cross-domain-transfer criterion only; not the stricter
> global directionality gate or a combined incident.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md),
> `RSK-0013-C01`–`C05`; underlying source relations in `SYN-0013-C01`.
> **Basis / limits:** Both sector paths are source-backed; observed service
> delay, controlled input execution and hypothetical decision harm retain
> separate labels.

> **Claim record — SYN-0013-C07 | analytic-judgment**
> **Claim:** `CPH-CT` is complete at SF2 through `CTL-0012-C01`–`C04`, with
> every required control function mapped to an exact edge and recommended,
> binding-design, implemented and evaluated states kept separate.
> **Claim status:** active
> **Scope:** Frozen controls criterion only; not `CPH-AE`, `CTR-AE` or the
> global control gate.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0012](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md),
> `CTL-0012-C01`–`C04`; underlying source relations in `SYN-0013-C01`.
> **Basis / limits:** Function/edge/source-floor coverage is direct; independent
> effectiveness remains absent.

## Residual and arithmetic audit

> **Claim record — SYN-0013-C08 | analytic-judgment**
> **Claim:** `CPH-SD/CI/AE` remain Partial and `CPH-GR` remains its existing
> Pass: modern system-boundary validation is incomplete, WHO consequences are
> not a primary case, NHS service delays are not biological harm, and no scoped
> safeguard metric has independent outcome evaluation.
> **Claim status:** active
> **Scope:** Frozen adjacent-cell audit after SRC-0026; Partial is a corpus gap,
> not a claim about real-world absence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0008-C04`; `RSK-0013-C05/C06`; `CTL-0012-C03`–`C05`;
> `SRC-0026-C10`–`C12`; frozen CPH criteria and existing `SYN-0005-C05`.
> **Basis / limits:** Missing predicates are named exactly; adjacent cells are
> not promoted by proxy.

> **Claim record — SYN-0013-C09 | artifact-observation**
> **Claim:** Independent strict review accepts exactly six cells as
> Partial→Pass—`CPH-ST/AS/WL/TV/XT/CT`—raising CPH from 1/10 to 7/10 and the
> overall score from 30/110 to 36/110 (32.7%), with 36 Pass, 68 Partial and
> 6 Absent.
> **Claim status:** active
> **Scope:** Accepted checkpoint arithmetic under frozen rubric v1.0; not
> absolute domain completeness or final certification.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0013-C01`–`C08`; prior `SYN-0001-C19` checkpoint at
> 30 Pass/74 Partial/6 Absent; frozen score method in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Six literal transitions produce the arithmetic; independent
> artifact, locator, lineage, graph and cell review completed 2026-07-12.

> **Claim record — SYN-0013-C10 | artifact-observation**
> **Claim:** No global gate changes: the reverse observed-decision,
> six-incident/four-sector, independently evaluated control and per-sector full-
> chain requirements remain unmet despite the six candidate CPH cells.
> **Claim status:** active
> **Scope:** Global-gate residual audit at the accepted SRC-0026 checkpoint.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0013-C05`–`C09`; twelve frozen global gates in `SYN-0001`.
> **Basis / limits:** Sector-cell completion and global certification have
> different predicates; no global state is inferred from score magnitude.

## Safety boundary

The synthesis retains class-level workflows, hazards, transfer mechanisms and
defensive control functions only. It contains no patient/sample data,
laboratory topology, credentials, diagnostic procedure, transport setting,
attack sequence or current operational threshold.

## Related pages

- [SRC-0026 — WHO LQMS handbook](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [AST-0006 — assets/stakeholders](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [WFL-0010 — lifecycle](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
- [SYS-0008 — system/gap map](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md)
- [HAZ-0002 — quality hazard](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md)
- [RSK-0013 — transfer paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [CTL-0012 — exact-edge controls](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md)
- [SYN-0005 — existing CPH governance Pass](syn-0005-global-us-eu-clinical-health-governance.md)
- [SYN-0001 — frozen rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
