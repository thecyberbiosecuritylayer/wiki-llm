---
id: SRC-0030
type: source
title: HSSIB electronic patient record systems thematic review
aliases:
  - HSSIB EPR systems thematic review 2025
  - Patient safety issues associated with EPR systems
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-independent-thematic-systems-review
ingest_status: complete-package
sensitivity: public
dual_use: low
raw_path: ../../raw/hssib-epr-systems-thematic-review-2025.pdf
sha256: 39121f8475e75c8435f9ca09260aa481e19c1e18d854dc85bf5bd02ba1590e0e
raw_components:
  - path: ../../raw/hssib-epr-systems-thematic-review-current-2026-07-12.html
    role: complete-current-official-html-rendering
    sha256: 03a21089af35b21e2343873f5137500c78b36e6b5e786d3a2c508073169f7ea8
canonical_url: https://www.hssib.org.uk/patient-safety-investigations/electronic-patient-record-epr-systems-thematic-review/investigation-report/
repository_url: https://www.hssib.org.uk/patient-safety-investigations/electronic-patient-record-epr-systems-thematic-review/investigation-report/pdf/
accessed: 2026-07-12
publication_date: 2025-11-27
evidence_corpus_cutoff: 2025-05-31
issuer: Health Services Safety Investigations Body
jurisdictions:
  - England
  - United Kingdom
tags:
  - electronic-patient-record
  - patient-safety
  - thematic-review
  - clinical-informatics
  - sociotechnical-system
  - interoperability
  - implementation
  - evidence-quality
---

# HSSIB electronic patient record systems thematic review

## Artifact identity and complete-package review

The preserved package contains HSSIB's complete 50-page report and its current
official HTML rendering.

- PDF: 262,851 bytes, SHA-256
  `39121f8475e75c8435f9ca09260aa481e19c1e18d854dc85bf5bd02ba1590e0e`;
  untagged, unencrypted PDF 1.7 with 50 A4 pages.
- HTML: 614,400 bytes, SHA-256
  `03a21089af35b21e2343873f5137500c78b36e6b5e786d3a2c508073169f7ea8`.
- Package total: 877,251 bytes.

Two complete official retrievals of each artifact on 2026-07-12 were
byte-identical. The PDF endpoint did not close its connection after delivering
the complete payload, but both 262,851-byte files had the same hash, parsed as
50 pages and ended as valid complete PDFs. All pages contain extractable text;
there are no blank or wholly image-only pages. The single raster figure on
physical p. 8 was rendered and inspected. The PDF has no form, JavaScript,
embedded file, encryption or cryptographic signature. Its ordinary URI
annotations were inventoried but not executed. The HTML's 12 scripts, one form
and one iframe were reviewed statically and not executed.

> **Claim record — SRC-0030-C01 | artifact-observation**
> **Claim:** The preserved 877,251-byte package is complete and reproducible:
> both files match byte-identical repeat retrievals and their recorded sizes and
> hashes; all 50 PDF pages are text-bearing and reviewed, the only raster figure
> was visually inspected, and static active-content checks are recorded.
> **Claim status:** active
> **Scope:** Artifact identity, completeness, reproducibility and static safety
> review on 2026-07-12; not substantive validation of the review's findings.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Full official PDF and HTML; PDF physical pp. 1–50; HTML title,
> canonical and publication metadata; local hashes/byte counts, `pdfinfo`,
> `pdfsig`, `pdfdetach`, page-text inventory and full-page/figure renders.
> **Basis / limits:** File properties are locally observable. The PDF transport
> caveat concerns connection closure after a complete payload, not missing
> bytes; scripts, form, iframe and linked content were not executed.

## Lineage, modality and independence

> **Claim record — SRC-0030-C02 | artifact-observation**
> **Claim:** The report, HTML and underlying HSSIB/HSIB report corpus form one
> HSSIB thematic-review lineage. It is primary for HSSIB's review method,
> coding and cross-report findings but derivative for every underlying case,
> quotation, recommendation and vignette.
> **Claim status:** active
> **Scope:** Evidence-lineage and modality classification; 112 summaries, 63
> included reports and 50 full reports are not independent issuers.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF `About this report`, physical p. 2; §§2–4, pp. 10–29;
> Appendix A, pp. 36–38; Appendices B–D, pp. 39–50.
> **Basis / limits:** HSSIB is the review issuer and its predecessor's reports
> are inputs to the same corpus. Consultation with national bodies on p. 38
> does not make those stakeholders co-issuers or independent evaluators.

> **Claim record — SRC-0030-C03 | source-report**
> **Claim:** HSSIB published this as a thematic summary and analysis of prior
> HSSIB/HSIB investigations, explicitly not as a new investigation of EPR
> systems; EPR areas not previously investigated are therefore unrepresented.
> **Claim status:** active
> **Scope:** Report purpose and coverage boundary, not a national census,
> systematic review of all EPR evidence or universal assessment of products.
> **As of:** 2025-11-27.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF cover and `About this report`, physical pp. 1–2;
> Executive Summary, pp. 3–7; HTML matching report header and sections.
> **Basis / limits:** The modality and omissions are direct. Current HTML
> availability does not extend the end-May-2025 evidence-corpus cutoff.

> **Claim record — SRC-0030-C04 | artifact-observation**
> **Claim:** This lineage is materially separate from event-specific case and
> national-review packages by issuer, source corpus, method, and claim object.
> It independently evaluates the broader EPR system class but does not confirm
> any individual event or mechanism.
> **Claim status:** active
> **Scope:** Independence for a systems-evaluation predicate, not same-event
> corroboration or a new incident lineage.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF pp. 2, 10, 15 and 36–38; complete PDF and HTML bounded
> event-term searches; reported sample cutoff at end May 2025.
> **Basis / limits:** No searched event-specific term occurs, and the review
> corpus predates the November 2025 NatPSA. Absence in this bounded corpus does
> not establish absence from all HSSIB work or wider evidence.

## Review method and unit discipline

> **Claim record — SRC-0030-C05 | source-report**
> **Claim:** Two HSSIB reviewers used template analysis in three rounds plus
> refinement: 40 reports informed an initial coding template; all 112 executive
> summaries were then screened and 63 reports included; 50 relevant full
> reports were split between reviewers with 10% reviewed by both.
> **Claim status:** active
> **Scope:** Review flow and quality procedures, not additive samples, incident
> counts, patients, deployments or a calculated inter-rater agreement result.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §2 opening, physical p. 10; §3 opening, p. 15; Appendix A
> `Analysis approach` and `Ensuring trustworthy findings`, pp. 36–38.
> **Basis / limits:** `40`, `112`, `63` and `50` are sequential/overlapping
> review-stage units and must not be summed. Exclusions were second-checked;
> no inter-rater statistic is reported.

> **Claim record — SRC-0030-C06 | artifact-observation**
> **Claim:** Appendix B's counts are overlapping report-code frequencies: 63
> reports were included; design, implementation and absent-EPR problems were
> coded in 38, 31 and 26 reports, while patient-safety, organisational,
> national/wider-system and unclear impact were coded in 52, 29, 14 and 5.
> **Claim status:** active
> **Scope:** Report-level thematic coding; not mutually exclusive incident,
> harmed-patient, provider, prevalence, severity or causality counts.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Appendix B top-code table, physical p. 39; detailed overlapping
> coding tables, pp. 41–49.
> **Basis / limits:** The source labels the unit `Number of reports`, permits
> multiple codes per report and gives no national EPR denominator.

These are report and coding units, not incidents, patients, harmed patients,
deaths, deployments or independent evidence lineages.

## EPR system scope, problems and consequences

> **Claim record — SRC-0030-C07 | source-report**
> **Claim:** For this review an EPR is software managing individual-patient
> clinical information and may be one multi-capability product or modules from
> different developers. Included functions cover administration/appointments,
> records/plans, diagnostic ordering/results, medicines and decision support;
> resource management and business analytics were excluded from the sample.
> **Claim status:** active
> **Scope:** Review-specific system boundary; not a universal EPR definition or
> an assertion that every report examined a whole EPR or every listed module.
> **As of:** 2025-11-27.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §1.1 and Figure 1, physical pp. 7–9; §2.1, p. 10; Appendix A
> `Review sample`, p. 37; §4.2.2–4.2.3, p. 27.
> **Basis / limits:** HSSIB says prior reports sometimes left unclear whether a
> whole EPR, a module, standalone software or an interfacing element was at
> issue; the canonical map preserves that ambiguity.

> **Claim record — SRC-0030-C08 | source-report**
> **Claim:** Across the included investigations HSSIB grouped problems into
> design/accessibility/usability/functionality/interoperability,
> implementation/configuration/integration, and absent system/module/function
> classes, including coexistence of paper and electronic processes.
> **Claim status:** active
> **Scope:** Cross-report problem taxonomy, not one product, one root cause,
> cyberattack, frequency estimate or proof that each class occurred together.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Executive Summary, physical pp. 3–7; §§2.1–2.2, pp. 10–12;
> Appendix B, pp. 39 and 41–49.
> **Basis / limits:** Codes overlap and originate from HSSIB's purposive report
> corpus. Design, local configuration and organizational integration are not
> collapsed into a single software-cause claim.

> **Claim record — SRC-0030-C09 | source-report**
> **Claim:** HSSIB found EPR-related conditions associated with care being
> missed, delayed or incorrect, including misidentification; recurrent
> unavailable or unfindable information, difficult-to-correct wrong record
> state and absent known-risk controls were identified, and several underlying
> reports described direct contributions to patient harm.
> **Claim status:** active
> **Scope:** HSSIB's cross-report evaluation and outcome categories, not a
> count of harmed patients, incidence rate, independent confirmation of each
> underlying event or proof of the mechanisms in any separately documented
> case.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Executive Summary, pp. 3–7; §2.3.1–2.3.6, pp. 12–15;
> Appendix B outcome tables, pp. 39 and 43–46.
> **Basis / limits:** Potential physical/psychological harm and directly
> contributed harm are kept separate. The source provides no national
> denominator and its underlying cases remain derivative here.

> **Claim record — SRC-0030-C10 | source-report**
> **Claim:** The recurring dependency lifecycle runs from requirements,
> capability/standards assessment and procurement through configuration,
> representative-user testing, integration, infrastructure, launch and
> training to feedback, change, optimisation, contingency and resourcing,
> under local/regional/national governance.
> **Claim status:** active
> **Scope:** Systems-review lifecycle and sociotechnical dependencies, not a
> universal deployment architecture or evidence that every organization
> omitted every function.
> **As of:** 2025-05-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§3.2–3.5, physical pp. 15–23; local-level prompts, pp. 27–29;
> Appendix B contributory-theme coding, pp. 46–49.
> **Basis / limits:** Procurement, software, human workflow, hardware/Wi-Fi,
> organization and governance predicates are jointly represented; no one is
> inferred to be a universal or sole cause.

## Recommendations, derivative cases and assurance boundary

> **Claim record — SRC-0030-C11 | source-report**
> **Claim:** Twenty-eight of the 50 full reports contained 29 relevant safety
> recommendations and 26 safety observations; HSSIB also issued observation
> `O/2025/079` and local learning prompts, while noting that progress of some
> planned actions was unclear.
> **Claim status:** active
> **Scope:** Recommendation/observation inventory and current review output;
> not implementation, compliance, completed response, test, effectiveness or
> patient-outcome evaluation.
> **As of:** 2025-11-27.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§4.1–4.2, physical pp. 23–29; Appendix D, pp. 49–50.
> **Basis / limits:** Counts are recommendations/observations within reports,
> not independent safeguards or evaluators. `O/2025/079` is a new output of
> this review and is separate from the 55 historical outputs. A published
> recommendation, observation, response or prompt is not evidence that risk
> was reduced.

> **Claim record — SRC-0030-C12 | artifact-observation**
> **Claim:** Vignettes A and B are derivative summaries of cited HSSIB reports,
> and `several near misses` in vignette B is unquantified; neither vignette is
> promoted to a new primary `INC`, outcome count or global-incident unit in
> this transaction.
> **Claim status:** active
> **Scope:** Case provenance and counting boundary; no judgment that the
> underlying events lack evidentiary value if their original reports are later
> ingested separately.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §2.3.3 vignettes A/B, physical pp. 13–14; cited HSSIB 2022b
> and 2025a entries, pp. 31 and 33; Appendix C list, pp. 39–41.
> **Basis / limits:** The review supplies summaries rather than independently
> ingested underlying case files. Patient, dose and interface details are not
> reproduced in this wiki.

> **Claim record — SRC-0030-C13 | artifact-observation**
> **Claim:** The independent EPR systems-evaluation predicate required by the
> strict `CPH-CI` plan is now available, but this source transaction changes no
> frozen cell: explicit three-lineage outcome/mechanism reconciliation remains
> pending, so the score stays 37/110 and CPH stays 8/10.
> **Claim status:** active
> **Scope:** Frozen-rubric boundary after source integration, not a finding
> that HSSIB adds no relevant evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0030-C02`–`C12`; frozen `CPH-CI/AE`, THI/CTR/FND/GOV
> and global-gate criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md); prior `SYN-0001-C23`.
> **Basis / limits:** HSSIB independently evaluates the broader system class,
> but does not itself perform cross-lineage case reconciliation.
> `CPH-AE` and every global gate remain unchanged.

## Limitations and safety handling

The corpus is HSSIB's purposive investigation set, not a national EPR census or
all-study systematic review. It includes final-draft inputs, spans a changing
2018–2025 digital context and double-reviewed only 10% at round 3. The report
does not publish its full keyword list, exclusion flow/reasons, raw coding
matrix, inter-rater statistic, formal adjudication, quality appraisal, evidence
weighting or saturation analysis; the round-1 selection rule is also
unreported. Current HTML availability and the `© 2026` footer do not update the
May-2025 evidence window or November-2025 publication. The wiki retains system
classes, aggregate report-code units, minimum
outcome categories and defensive governance questions; it omits patient,
facility, dose, UI, software-vendor, topology, credential, configuration and
deployable workflow detail.

## Integration map

- [SYS-0010 — Electronic patient record safety dependencies](../systems/sys-0010-electronic-patient-record-safety-dependencies.md)

## Related evidence

- [SRC-0029 — NHS England national review lineage](src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
- [SYN-0001 — frozen coverage rubric](../syntheses/syn-0001-coverage-rubric.md)
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
