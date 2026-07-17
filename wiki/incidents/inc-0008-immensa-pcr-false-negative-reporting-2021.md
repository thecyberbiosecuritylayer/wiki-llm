---
id: INC-0008
type: incident
title: Immensa PCR incorrect-negative reporting incident, 2021
aliases:
  - Immensa false-negative PCR incident
  - Wolverhampton laboratory result-misreporting incident
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
event_date: 2021-09-02
event_end_date: 2021-10-12
discovery_date: 2021-09-08
verification_date: 2021-10-12
disclosure_date: 2021-10-15
recovery_date: unknown
source_ids:
  - SRC-0057
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0057
    claim_id: INC-0008-C01
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary and §§1.2, 3.1, 3.3, 4; UKHSA epidemiological preprint Methods/Results; Warwick abstract and §§3–4"
  - predicate: affects
    target: AST-0006
    claim_id: INC-0008-C03
    evidence:
      - source: SRC-0057
        locator: "SUI §3.1.1, pp. 51–52; UKHSA preprint Introduction/Methods, pp. 1–2"
  - predicate: depends-on
    target: WFL-0010
    claim_id: INC-0008-C03
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary ¶¶3–4 and §3.1.1; observed test-input→classification→digital-report→action dependency"
  - predicate: depends-on
    target: VUL-0006
    claim_id: INC-0008-C06
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary ¶¶8–16, §§2.6 and 3.4; monitoring, quality-assurance and governance weaknesses"
  - predicate: enables
    target: RSK-0021
    claim_id: INC-0008-C09
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary ¶¶3–5; UKHSA preprint pp. 1–5 and Tables 3, 5–6"
tags:
  - documented-incident
  - laboratory
  - public-health
  - biological-input
  - digital-result
  - false-negative
  - configuration-error
  - non-malicious
  - reverse-transfer
---

# Immensa PCR incorrect-negative reporting incident, 2021

> [!WARNING]
> **Evidence classification**
> `INC-0008` is one non-malicious laboratory/public-health incident. The SUI,
> official web outputs, UKHSA impact analysis and Warwick working paper are
> evidence roles around that event, not separate incidents. Estimated tests,
> cases and infections are not converted into individually observed outcomes.

## Event identity and source roles

> **Claim record — INC-0008-C01 | analytic-judgment**
> **Claim:** `INC-0008` canonicalizes one 2021 result-misreporting incident
> using a primary official UKHSA investigation, a separate UKHSA ecological
> analysis and one institutionally independent Warwick working paper, without
> multiplying publication objects, affected samples or model outputs into
> events or investigations.
> **Claim status:** active
> **Scope:** One event and claim-specific source roles; not two independent
> forensic investigations or independent verification of every estimate.
> **As of:** Event 2021; records through 2022; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> `SRC-0057-C01/C02`; SUI scope/method, pp. 14–15 and 67–72.
> **Basis / limits:** Source roles and institutional affiliations are direct.
> The UKHSA analytical team is methodologically separate but not an external
> institution.

## Event, discovery, response and recovery chronology

| State | Date | Represented evidence boundary |
| --- | --- | --- |
| commissioned testing begins | 2021-09-02 | start of represented exposure window, not proven first error |
| first recorded concern | 2021-09-08 | local discordant-result issue, not yet laboratory attribution |
| formal incident registration | 2021-09-22 | structured issue record; investigation still focused elsewhere |
| affected laboratory linked | 2021-10-11 | barcode review tied the discordant tests to Immensa Wolverhampton; not yet the containment state |
| problem confirmed / containment | 2021-10-12 | high probability established; testing suspended immediately |
| public disclosure | 2021-10-15 | suspension publicly announced; affected public subsequently advised |
| cause-validation visit | 2021-10-18 | supported immediate-cause account |
| recovery | unknown | suspension and process changes do not establish result recovery or a trusted-restoration endpoint |

> **Claim record — INC-0008-C02 | source-report**
> **Claim:** The official chronology separates event window, first warning,
> formal incident registration, verification/containment, public disclosure,
> cause review and unknown recovery rather than using the report-publication
> date as event discovery or restoration.
> **Claim status:** active
> **Scope:** High-level lifecycle accounting; not a complete minute-level log.
> **As of:** Events September–October 2021.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI §3.1.1, p. 51; §§3.3.1–3.3.7, pp. 53–54; Appendix 6,
> pp. 85–88; `SRC-0057-C03`.
> **Basis / limits:** Represented dates are direct. The exact first erroneous
> classification and complete affected-person remediation state are unknown.

## Observed reverse-transfer path

The safe observed path is:

`biological test input → laboratory measurement and configured classification
→ digital negative result → person/public-health isolation and tracing decision
state → modelled population-level transmission consequence`

> **Claim record — INC-0008-C03 | analytic-judgment**
> **Claim:** The incident directly demonstrates a material/biological-input→
> laboratory-interpretation→digital-result→decision path: staff configuration
> error caused some test measurements to be digitally reported negative when
> they otherwise would have been classified positive, changing the digital
> notification state that ordinarily initiates positive-result contact tracing.
> **Claim status:** active
> **Scope:** Safe causal direction and affected [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)/
> [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
> states; no assay setting, procedure, person record or claim that every
> estimated result followed an identical path.
> **As of:** Event 2021; finding 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> `SRC-0057-C03/C04/C10`; SUI Executive summary ¶¶3–5, pp. 8–9;
> SUI §2.6.7, printed p. 45 (data-upload KPI), and §3.1.1, p. 51
> (barcode review and tailored text messages); UKHSA preprint Introduction,
> p. 2 (positive-result notification initiates contact tracing).
> **Basis / limits:** Input, interpretation, report and intended action
> dependency are direct. Individual tracing/isolation behavior is not
> reconstructed, and population consequences require separate modelling.

## Scale and consequence states

> **Claim record — INC-0008-C04 | source-report**
> **Claim:** UKHSA's revised scale was around 39,000 likely incorrect negative
> reports among 417,000 processed tests—roughly 10% of the laboratory's samples
> and 0.3% of NHS Test and Trace samples during the period—but this was a
> statistical estimate, not 39,000 individually re-adjudicated results.
> **Claim status:** active
> **Scope:** Event-period test-result estimate with denominators preserved;
> not unique-person count, prevalence or exact harm census.
> **As of:** 2021-09-02–2021-10-12; published 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0057-C05`; SUI §1.2.4, p. 13; UKHSA preprint Table 3,
> p. 20; official press summary.
> **Basis / limits:** Initial circa-43,000 and revised circa-39,000 estimates
> are successive states, not additive counts.

> **Claim record — INC-0008-C05 | analytic-judgment**
> **Claim:** UKHSA's area-level model estimates about 24,098 additional
> reported cases and approximately 55,000 infections in the most affected
> areas, while intervals for hospitalisations and deaths include zero and no
> individual test, transmission chain or outcome can be identified.
> **Claim status:** active
> **Scope:** Modelled public-health consequence with uncertainty; not observed
> person-level infection, hospitalization or death attribution.
> **As of:** Modelled 2021 event/follow-up period; preprint 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `SRC-0057-C06`; UKHSA preprint Methods/Results/Discussion,
> pp. 2–5; Tables 5–6, pp. 22–23.
> **Basis / limits:** Ecological estimates support a bounded population-impact
> direction. The retained preprint's ambiguous per-result multiplier is not
> used.

## Causality, vector, impact and attribution

> **Claim record — INC-0008-C06 | analytic-judgment**
> **Claim:** Immediate cause is graded high for staff configuration error;
> malicious/cyber vector is unsupported; impact comprises estimated result
> scale plus modelled population outcomes; and organizational attribution is
> split between the immediate laboratory action and UKHSA/predecessor
> assurance/response weaknesses that delayed detection.
> **Claim status:** active
> **Scope:** Separate causal predicates for one event; not legal liability,
> motive attribution or a single deterministic root cause.
> **As of:** Investigation findings 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0057-C04`–`C08`; SUI Executive summary ¶¶4, 8–16;
> Appendix 2 root-cause method, pp. 70–72.
> **Basis / limits:** The panel found multiple missed opportunities and no
> single root cause or deliberate NHSTT decision not to act.

> **Claim record — INC-0008-C07 | analytic-judgment**
> **Claim:** Warwick independently supports a positive transmission-impact
> direction at area level, but its 0.6–1.6 estimate and early 43,000 scaling do
> not independently verify UKHSA's revised result count or any personal
> outcome.
> **Claim status:** active
> **Scope:** Independent context and countercheck; not a second incident or
> complete replication.
> **As of:** Working paper 2021; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** `SRC-0057-C07`; Warwick abstract and §§3.4–5, pp. 3, 15–21.
> **Basis / limits:** Institutional independence is direct; method/data limits
> and superseded scale input remain explicit.

## Response, lessons and recovery boundary

> **Claim record — INC-0008-C08 | source-report**
> **Claim:** Testing was suspended when the affected laboratory was identified,
> and UKHSA later reported strengthened performance reporting, oversight/
> incident links, accountability and decision logging; the SUI separately
> recommended integrated quality, accreditation, monitoring-trigger and
> incident-governance improvements.
> **Claim status:** active
> **Scope:** Containment, issuer-reported implementation and recommendation
> states; not full recovery or independently measured effectiveness.
> **As of:** Response 2021; changes/recommendations reported 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `SRC-0057-C03/C09`; improvements page numbered items 1–4;
> SUI Recommendations 1–14, pp. 63–66.
> **Basis / limits:** Implemented and recommended states are separated. Lower
> demand and fewer providers also altered recurrence risk.

> **Claim record — INC-0008-C09 | analytic-judgment**
> **Claim:** `INC-0008` is a qualifying primary incident anchor for
> [RSK-0021](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
> and the reverse-direction incident corpus, but not evidence of a cyberattack,
> malicious insider, exact individual harm or safeguard effectiveness.
> **Claim status:** active
> **Scope:** Incident contribution and nonpromotion boundary.
> **As of:** Full package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `INC-0008-C01`–`C08`; `SRC-0057-C10`.
> **Basis / limits:** The observed direction is direct; adjacent threat and
> assurance predicates remain absent.

## Safety boundary

No patient/sample record, assay setting, laboratory procedure, facility
topology or exploitable configuration is retained. Only high-level causal,
timeline, evidence-state and defensive control abstractions are represented.

## Related pages

- [SRC-0057 — evidence package](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [VUL-0006 — exposure classes](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [RSK-0021 — observed reverse path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0023 — response/control lessons](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md)
- [SYN-0003 — canonical transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md)
- [SYN-0031 — reconciliation](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md), exact locators above.
