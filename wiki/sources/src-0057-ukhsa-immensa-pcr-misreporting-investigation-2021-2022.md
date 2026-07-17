---
id: SRC-0057
type: source
title: UKHSA Immensa PCR-result misreporting investigation and impact analyses, 2021–2022
aliases:
  - UKHSA Immensa serious untoward incident package
  - Immensa false-negative investigation evidence package
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_type: official-incident-investigation-implementation-record-and-epidemiological-analysis-package
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/ukhsa-immensa-sui-final-report-2022.pdf
raw_bytes: 1027971
sha256: 32934b8d420d921967411b074db670299049aff5356929a1a71ee3355c39f34a
raw_components:
  - path: ../../raw/ukhsa-immensa-investigation-landing-current-2026-07-12.html
    role: official-publication-landing-and-investigation-independence-context
    bytes: 76490
    sha256: 151ffec9f8eab0d83d2957ad08089c0bab2a3b226886350629bf5421361c2439
  - path: ../../raw/ukhsa-immensa-process-improvements-current-2026-07-12.html
    role: issuer-reported-post-incident-system-and-process-improvements
    bytes: 76507
    sha256: 594b6d2921f49f4983054ffe8e9c55976ca63f6b5905baa47c3a1a6157f9d8cf
  - path: ../../raw/ukhsa-immensa-investigation-press-release-2022.html
    role: official-high-level-cause-scale-and-response-summary
    bytes: 75123
    sha256: 931ac113b287fec311641af43e677f40d06fda24cad05de87122e5053d0adc1d
  - path: ../../raw/ukhsa-immensa-epidemiological-analysis-preprint-2022.pdf
    role: ukhsa-ecological-impact-analysis-preprint
    bytes: 3260159
    sha256: e7b7a71ab232baa0d61007479e58f9f9b7108254e96af446b73e45c7f5c9c254
  - path: ../../raw/warwick-immensa-natural-experiment-working-paper-2021.pdf
    role: institutionally-independent-academic-natural-experiment-working-paper
    bytes: 2928234
    sha256: a051913d062d8310fc7c5c62ed2a30515521a85f9415308c28e8c9553b03e6c1
canonical_url: https://www.gov.uk/government/publications/serious-untoward-incident-investigation-immensa-health-clinic-limited
report_url: https://assets.publishing.service.gov.uk/media/63bc39d3d3bf7f2639626de0/SUI_INVESTIGATION_FINAL_REPORT.pdf
improvements_url: https://www.gov.uk/government/publications/serious-untoward-incident-investigation-immensa-health-clinic-limited/improvements-to-ukhsas-systems-and-processes-implemented-since-the-immensa-incident
press_release_url: https://www.gov.uk/government/news/ukhsa-publishes-investigation-findings-following-errors-at-the-private-immensa-lab
epidemiology_url: https://www.medrxiv.org/content/10.1101/2022.11.30.22282922v1
warwick_url: https://wrap.warwick.ac.uk/id/eprint/160564/
accessed: 2026-07-12
publication_date: 2022-11-29
issuers:
  - UK Health Security Agency
  - University of Warwick
jurisdictions:
  - United Kingdom
tags:
  - laboratory
  - public-health
  - incident
  - result-integrity
  - false-negative
  - configuration-error
  - epidemiology
  - quality-assurance
---

# UKHSA Immensa PCR-result misreporting investigation and impact analyses, 2021–2022

## Package identity and reproducibility

The retained package contains the complete 89-page SUI report, official
landing, implementation and press pages, a 23-page UKHSA epidemiological
preprint and a 37-page Warwick working paper. The canonical wiki
representation does not reproduce person-level records, operational assay
values or laboratory procedures from those full artifacts.

> **Claim record — SRC-0057-C01 | artifact-observation**
> **Claim:** Six public objects totaling 7,444,484 bytes are retained with
> exact hashes; repeat retrieval on 2026-07-12 was byte-identical for every
> object, and PDF inspection confirmed 89, 23 and 37 complete pages.
> **Claim status:** active
> **Scope:** Local artifact completeness and reproducibility; not
> cryptographic issuer authentication or a guarantee that live HTML will not
> later change.
> **As of:** Retrieved and repeated 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths, byte counts and SHA-256 values; repeat
> retrieval, `cmp`, `file`, `pdfinfo` and complete text extraction/review.
> **Basis / limits:** Byte identity establishes the retained acquisition
> state. It does not validate every source conclusion.

## Evidence roles and independence

> **Claim record — SRC-0057-C02 | analytic-judgment**
> **Claim:** The SUI panel was operationally separate from the incident and
> testing programme but remained inside UKHSA; the UKHSA epidemiological team
> adds a different method, not an independent institution; Warwick supplies
> one institutionally independent academic analysis, while the landing,
> press and improvements pages are derivative UKHSA publication outputs.
> **Claim status:** active
> **Scope:** Claim-specific evidence-lineage accounting; not equal evidentiary
> weight, two independent incident investigations or independent replication
> of every count.
> **As of:** Publications 2021–2022; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Official landing `Details`; SUI §§1.3 and Appendix 1–2,
> especially pp. 15, 68–71; UKHSA preprint title/affiliations and Methods;
> Warwick working paper title page, abstract and method.
> **Basis / limits:** Operational, institutional and methodological
> independence are different predicates. The retained epidemiological papers
> are preprint/working-paper artifacts, not additional incident reports.

## Event, cause and chronology

> **Claim record — SRC-0057-C03 | source-report**
> **Claim:** Testing at the contracted laboratory began on 2021-09-02; the
> first recorded discordant-result concern was logged on 2021-09-08, the issue
> became a formal incident on 2021-09-22, barcode analysis linked the
> discordant tests to the affected laboratory on 2021-10-11, and the high-
> probability problem was confirmed and testing suspended on 2021-10-12,
> followed by a public announcement on 2021-10-15 and a validation visit on
> 2021-10-18.
> **Claim status:** active
> **Scope:** High-level event/discovery/escalation/containment chronology; not
> a complete operational log or a claim that the first error occurred exactly
> when commissioned testing began.
> **As of:** Event 2021-09-02–2021-10-18; report 2022-11-29.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI §3.1.1, p. 51; §§3.3.1–3.3.7, pp. 53–54; Appendix 6,
> pp. 85–88.
> **Basis / limits:** Dates and represented states are direct. Recovery of the
> affected service/result population is not established.

> **Claim record — SRC-0057-C04 | source-report**
> **Claim:** UKHSA concluded that a laboratory staff configuration error in
> result classification was the immediate cause of some biological test
> measurements being digitally reported negative when they otherwise would
> have been classified positive; no malicious or cyber cause was reported.
> **Claim status:** active
> **Scope:** Safe high-level immediate-cause statement; no operational setting,
> assay procedure, individual result or exploit detail.
> **As of:** Incident September–October 2021; finding 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI Executive summary ¶4, p. 8; Appendix 2 §2(B)(vi), p. 71;
> official press release paragraphs beginning `The cause was` and investigator
> statement; SUI §2.6.7, printed p. 45 (data-upload KPI), and §3.1.1,
> p. 51 (barcode review and tailored text messages).
> **Basis / limits:** Immediate cause and non-malicious classification are
> direct. The SUI scope focused on UKHSA/predecessor management systems rather
> than reconstructing every action inside Immensa.

## Scale, consequences and uncertainty

> **Claim record — SRC-0057-C05 | source-report**
> **Claim:** UKHSA revised its initial circa-43,000 figure to around 39,000
> likely incorrect negative reports among 417,000 tests processed during the
> period; the press summary represents this as roughly 10% of that laboratory's
> samples and 0.3% of NHS Test and Trace samples, all as estimates rather than
> person-by-person confirmed results.
> **Claim status:** active
> **Scope:** Estimated test-result scale with separate numerator and
> denominator populations; not 39,000 independently verified people or an
> incidence rate outside the event period.
> **As of:** Event 2021-09-02–2021-10-12; estimates published 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI §1.2.4, p. 13; official press release paragraph beginning
> `Based on background infection rates`; UKHSA preprint Results and Table 3,
> pp. 3 and 20.
> **Basis / limits:** Scale is statistically estimated. The initial and revised
> figures are not added or treated as independent observations.

> **Claim record — SRC-0057-C06 | analytic-judgment**
> **Claim:** The UKHSA ecological analysis estimates about 24,098 additional
> reported cases and approximately 55,000 additional infections in the most
> affected areas, while hospitalisation and death intervals include zero; it
> cannot identify true individual test states, transmission chains or personal
> outcomes.
> **Claim status:** active
> **Scope:** Modelled population-level consequence and uncertainty; not
> observed individual causation, exact national totals or confirmed deaths.
> **As of:** Modelled event period and follow-up in 2021; preprint 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** UKHSA preprint Methods, p. 2; Results/Discussion, pp. 3–5;
> Tables 5–6, pp. 22–23.
> **Basis / limits:** Case/infection signal is stronger than the admission/death
> estimates. The paper contains an internally ambiguous per-result multiplier,
> so this package does not reproduce or rely on that multiplier.

> **Claim record — SRC-0057-C07 | analytic-judgment**
> **Claim:** Warwick independently found a positive transmission direction and
> estimated 0.6–1.6 additional infections per missed case in its 13-area
> synthetic-control analysis, but its national scaling used the earlier
> 43,000 estimate and its working-paper, area-level method cannot assign
> individual outcomes.
> **Claim status:** active
> **Scope:** Independent directional context and method limits; not a final
> count, clinical attribution or peer-reviewed replication of UKHSA.
> **As of:** Working paper 2021; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** Warwick abstract, p. 3; §§3.4 and results, pp. 15–20; data-
> granularity limitation, pp. 20–21.
> **Basis / limits:** The institution and method are independent, but one
> working paper does not remove ecological, classification or comparator
> uncertainty.

## Oversight, response and control-state boundary

> **Claim record — SRC-0057-C08 | source-report**
> **Claim:** The SUI panel found fragmented quality/governance, monitoring and
> incident-review weaknesses that delayed identification, yet did not conclude
> that any single contracting or monitoring weakness would have prevented the
> laboratory error; it also found no deliberate decision by NHSTT not to act.
> **Claim status:** active
> **Scope:** Case-specific organizational findings; not a universal laboratory
> governance model or exoneration of every actor/process.
> **As of:** Management systems and reviews through 2021; findings 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** SUI Executive summary ¶¶8–16, pp. 9–11; §§2.6 and 3.4,
> pp. 45–59; conclusions §§4.1–4.8, pp. 60–63.
> **Basis / limits:** Multiple missed opportunities are direct; they are not
> collapsed into one deterministic root cause.

> **Claim record — SRC-0057-C09 | source-report**
> **Claim:** UKHSA reported implementing national/regional laboratory-
> performance reporting, closer laboratory-oversight/incident-response links,
> clearer accountabilities and stronger decision logging, while the SUI issued
> 14 broader recommendations for quality, accreditation, monitoring and
> incident governance.
> **Claim status:** active
> **Scope:** Issuer-reported implementation plus separately recommended
> actions; not independent effectiveness, universal completion or causal harm
> reduction.
> **As of:** Changes and recommendations reported 2022-11-29.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** Improvements page, `Improvements within the testing operations
> group` items 1–4 and `commercial function`; SUI Recommendations 1–14,
> pp. 63–66.
> **Basis / limits:** Some commercial-training commitments were future-tense,
> and reduced demand/fewer providers also changed recurrence risk. No
> independent outcome comparison is represented.

## Safety and contribution boundary

> **Claim record — SRC-0057-C10 | analytic-judgment**
> **Claim:** The package supports one observed material/input→laboratory-
> interpretation→digital-result→public-health/person-decision incident and
> bounded control lessons, but supplies no malicious event, operational
> laboratory recipe, independently effective safeguard or person-level harm
> reconstruction.
> **Claim status:** active
> **Scope:** Downstream-use and safety classification for the wiki.
> **As of:** Full package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0057-C02`–`C09`; SUI scope/method; both epidemiological
> papers' stated limitations; SUI §2.6.7, printed p. 45, and §3.1.1, p. 51;
> UKHSA preprint Introduction, p. 2 (positive-result notification and contact-
> tracing initiation).
> **Basis / limits:** The direction and incident are direct at safe abstraction;
> numerical downstream effects retain their modelled status.

## Related pages

- [INC-0008 — canonical incident](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [HAZ-0006 — observed configuration hazard](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
- [VUL-0006 — event-specific exposures](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [RSK-0021 — reverse-transfer path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0023 — incident controls](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md)
- [SYN-0003 — canonical transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md)
- [SYN-0031 — rubric reconciliation](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- Retained objects and exact canonical URLs in frontmatter.
