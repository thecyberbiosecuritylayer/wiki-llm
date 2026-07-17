---
id: SRC-0005
type: source
title: Cybersecurity of Genomic Data
aliases:
  - NIST IR 8432
  - NIST Internal Report 8432
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: expert-analysis
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/nist-ir-8432-cybersecurity-genomic-data-2023.pdf
sha256: 17ac87622e79bb004fd65229d8211a58e1c66c7ea54e08b8e0f2f376454f02d2
canonical_url: https://csrc.nist.gov/pubs/ir/8432/final
accessed: 2026-07-12
transient: true
doi: 10.6028/NIST.IR.8432
issuer: National Institute of Standards and Technology
version: final
publication_date: 2023-12-20
jurisdictions:
  - United States
tags:
  - genomics
  - genomic-data
  - cybersecurity
  - privacy
  - sequencing
  - bioeconomy
---

# Cybersecurity of Genomic Data

## Bibliographic identity

Pulivarti, Ron; Martin, Natalia; Byers, Fred; Wagner, Justin; Zook, Justin;
Maragh, Samantha; McDaniel, Jennifer; Wilson, Kevin; Wojtyniak, Martin;
Kreider, Brett; France, Ann-Marie; Edwards, Sallie; Morris, Tommy; Sheldon,
Jared; Ross, Scott; and Whitlow, Phillip. *Cybersecurity of Genomic Data*.
NIST Internal Report 8432. Gaithersburg, MD: National Institute of Standards
and Technology, December 2023. DOI `10.6028/NIST.IR.8432`.

In the wiki, this is `expert-analysis`: an official NIST technical report that
synthesizes stakeholder workshops, selected literature, a current-practice
inventory, and proposed solutions. It is not a standard, a binding rule, a
systematic review, or an implementation or effectiveness study.

## Provenance

- Immutable local artifact:
  `../../raw/nist-ir-8432-cybersecurity-genomic-data-2023.pdf`, 1,074,804
  bytes, PDF 1.7, 55 physical pages, SHA-256
  `17ac87622e79bb004fd65229d8211a58e1c66c7ea54e08b8e0f2f376454f02d2`.
- The PDF is tagged and unencrypted, with no JavaScript, forms, or embedded
  files. `pdfinfo`, complete text and layout extraction, and rendered
  inspection confirmed that the package is readable.
- Pagination mapping: PDF pp. 1–3 — unnumbered cover/title/notices; printed
  roman pp. i–vi = PDF pp. 4–9; printed Arabic pp. 1–46 = PDF pp. 10–55.
  For the main text, `PDF physical page = printed Arabic page + 9`.
- The front matter, sections 1–7, 88 references, Appendix A, and Appendix B
  were read in full. Tables 1–4 were checked through layout extraction;
  Figures 1–3 were checked on rendered pages and against their captions.
- Official CSRC page, accessed 2026-07-12, presents `IR 8432 (Final)`, date
  published December 2023, DOI, and document history `03/03/23: Draft` and
  `12/20/23: Final`. `transient: true` applies to this current web
  presentation; substantive evidence is reproducible from the local PDF.
- The cover and title pages and the official page support the 16-author list
  above. The PDF metadata omits Jennifer McDaniel; the suggested citation omits
  both Justin Zook and Jennifer McDaniel, gives `Frances A` instead of Ann-Marie
  France, and has a malformed DOI with a double `/`. The bibliographic identity
  above rests on the title pages, official page, and normalized DOI.

`ingest_status: complete` means that the local PDF package was reviewed in
full. It does not mean that all 88 cited sources, the current validity of every
legal statement in 2026, or implementation of the described solutions were
independently verified.

## Executive summary

NIST IR 8432 describes genomic data as a digital asset combining phenotype,
health, immutability, uniqueness, mystique, value, and kinship properties. The
report distinguishes the cybersecurity objectives of confidentiality,
integrity, and availability from the privacy-engineering objectives of
predictability, manageability, and disassociability: privacy problems may arise
either through a cyberattack or independently through data processing, consent,
and associability.

The document provides a partial lifecycle model from sample collection and
preparation to data generation and analysis, but focuses its substantive cyber
scope on generation, storage, processing, analysis, sharing, and the connected
sequencing ecosystem. It synthesizes two 2022 NCCoE public workshops and
selected research, grouping stakeholder-identified guidance, technical, and
policy and regulatory gaps. Chapter 5 records a cybersecurity profile already
published as an Initial Public Draft in June 2023, a planned privacy profile,
and candidate MUD, security-baseline, risk-management, and privacy-enhancing-
technology demonstrations.

The report is predominantly US-centric and captures the state of discussion in
2022–2023. Its use cases simulate real-life challenges; apart from the already
published Initial Public Draft, maturity remains planned, candidate, or
proposed, and expected benefits are not evidence of implementation, testing,
or effectiveness.

## Claims and locators

> **Claim record — SRC-0005-C01 | source-report**
> **Claim:** NIST developed the report from two 2022 NCCoE public workshops—the
> first on current and anticipated challenges and the second on possible
> solutions—and additional research; the first workshop was a 5.5-hour virtual
> event with nearly 500 stakeholders, and the agendas and presenters for both
> workshops appear in Appendix B.
> **Claim status:** active
> **Scope:** Report-development method and stakeholder input, not a
> representative survey of the genomics sector.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, Acknowledgments, printed p. vi (PDF p. 9);
> §1.1–§1.2, printed p. 2 (PDF p. 11); §4.4 opening, printed p. 20
> (PDF p. 29); Appendix B, Tables 2–4, printed pp. 45–46
> (PDF pp. 54–55).
> **Basis / limits:** Dates, sequence, duration and reported attendance are
> direct. The report gives no sampling frame, participant demographics,
> response rate, coding protocol or representativeness analysis; workshop
> findings cannot establish prevalence.

> **Claim record — SRC-0005-C02 | source-report**
> **Claim:** NIST identifies seven genomic-data characteristics — phenotype,
> health, immutable, unique, mystique, value and kinship — and argues that the
> combination, rather than any one property, distinguishes the value and
> sensitivity of genomic data from other data types.
> **Claim status:** active
> **Scope:** NIST's genomic-data framing based on workshop discussion and cited
> research, not a universal biological taxonomy.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract, printed p. i (PDF p. 4); §2.6, printed p. 6
> (PDF p. 15); Figure 2, printed p. 7 (PDF p. 16).
> **Basis / limits:** The list and combination claim are explicit. The source
> says these concepts were discussed at a workshop and posited by some in the
> research community; simplified formulations such as practical immutability
> or uniqueness except identical siblings should not be generalized beyond
> the report's stated context.

> **Claim record — SRC-0005-C03 | source-report**
> **Claim:** The report distinguishes cybersecurity objectives of
> confidentiality, integrity and availability from privacy-engineering
> objectives of predictability, manageability and disassociability, and states
> that genomic-data processing can create privacy risk independently of a
> cyberattack.
> **Claim status:** active
> **Scope:** Cybersecurity/privacy conceptual distinction for processing
> genomic data.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §1.1 and footnote 1, printed pp. 1–2
> (PDF pp. 10–11).
> **Basis / limits:** Objectives and the independent processing-risk pathway
> are direct. Privacy must not be reduced to confidentiality; examples describe
> potential harms and needed capabilities, not observed frequency or measured
> likelihood.

> **Claim record — SRC-0005-C04 | source-report**
> **Claim:** Figure 1 presents `Sample Collection -> Sample Preparation -> Data
> Generation -> Data Analysis`; collection and preparation are mostly outside
> the report's cyber scope, generation and analysis are in scope, and retention
> and disposal are additional considerations outside the four-stage figure.
> **Claim status:** active
> **Scope:** Partial genomic-information lifecycle used by NIST IR 8432.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §2.1 and Figure 1, printed pp. 3–4
> (PDF pp. 12–13).
> **Basis / limits:** Stage labels and scope boundary were visually verified.
> Human-DNA collection remains relevant to privacy and informed consent. This
> is not a complete sample-to-disposal lifecycle, chain-of-identity/custody
> architecture or validated end-to-end data-lineage model.

> **Claim record — SRC-0005-C05 | analytic-judgment**
> **Claim:** The report describes a sequencing/analysis ecosystem in which raw
> data may be stored on-premises or in cloud services, processed by open-source
> or commercial software, shared through public or controlled-access databases,
> and integrated or reinterpreted through EHR workflows; connected sequencers,
> pipelines, storage, software and organizational handoffs therefore create
> multiple security and privacy boundaries.
> **Claim status:** active
> **Scope:** High-level ecosystem description across research and healthcare,
> not a product- or facility-specific architecture.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** §2.1–§2.5, printed pp. 3–5 (PDF pp. 12–14);
> §4.4.2, printed pp. 20–22 (PDF pp. 29–31).
> **Basis / limits:** Components and transfers are directly described; the
> trust-boundary conclusion is a bounded synthesis of those descriptions. The
> source supplies no network inventory, identity model, deployment sample or
> implementation prevalence data.

> **Claim record — SRC-0005-C06 | source-report**
> **Claim:** NIST reports that genomic data may retain re-identification risk
> after removal of conventional identifiers and that exposure or processing can
> affect biological relatives and conflict with individual informed-consent
> limits, creating individual and group/class privacy harms.
> **Claim status:** active
> **Scope:** Human genomic data, especially aggregation, sharing and combination
> with other datasets.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** Background, printed p. 3 (PDF p. 12); §3.2, printed
> pp. 9–10 (PDF pp. 18–19); §4.3.1, printed p. 19 (PDF p. 28);
> §4.4.3, printed p. 22 (PDF p. 31).
> **Basis / limits:** Relational privacy, consent complexity and residual risk
> are consistent across the report. Strong formulations about high-probability
> re-identification, whole-genome anonymization or utility-destroying
> de-identification are secondary claims here; cited primary studies [6]–[9],
> [30] and [72] were not independently appraised in this ingest.

> **Claim record — SRC-0005-C07 | source-report**
> **Claim:** The report identifies hypothetical integrity pathways in which
> altered sequences, annotations, variant-calling tools or analytical systems
> could change research, identification or clinical decisions and propagate
> into economic, reputational, health, manufacturing or biological
> consequences.
> **Claim status:** active
> **Scope:** Potential genomic-data integrity scenarios, not documented
> incidents or quantified risk.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** §1.1, printed pp. 1–2 (PDF pp. 10–11);
> §3.1, printed p. 9 (PDF p. 18); §3.3, printed p. 10
> (PDF p. 19); §3.5, printed p. 11 (PDF p. 20); §4.4.2,
> printed pp. 21–22 (PDF pp. 30–31).
> **Basis / limits:** The source explicitly presents potential paths and says
> likelihood of the national-security threats was not evaluated. Some paths
> are stakeholder suggestions or literature-derived speculation. They support
> a hypothetical `RSK`, not attribution, incident creation or a likelihood
> score.

> **Claim record — SRC-0005-C08 | source-report**
> **Claim:** Workshop stakeholders identified guidance and policy/regulatory
> gaps concerning genomic-specific risk guidance, safe sharing and monitoring,
> sequencer/pipeline configuration guidance, fragmented U.S. privacy coverage,
> direct-to-consumer data outside some HIPAA relationships, and residual
> re-identification risk.
> **Claim status:** active
> **Scope:** Stakeholder-reported U.S.-centric gap landscape as documented in
> 2022–2023, with selected international context.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract, printed p. i (PDF p. 4); §4.4,
> §4.4.1 and §4.4.3, printed pp. 20, 22 (PDF pp. 29, 31);
> Conclusion, printed p. 33 (PDF p. 42).
> **Basis / limits:** High confidence that the report records these gaps, not
> that they remain current in 2026. Laws, NIST profiles, guidance and market
> practice are time-sensitive and require current primary-source verification;
> the report is not legal advice or a comprehensive state-law survey.

> **Claim record — SRC-0005-C09 | source-report**
> **Claim:** Stakeholders also identified technical gaps involving sequencer
> SBOM visibility, data confinement/DLP, network communication requirements,
> secure reset and decommissioning, container vulnerability scanning, genomic
> EHR/FHIR scale, and security of third-party variant-calling components and
> downstream use.
> **Claim status:** active
> **Scope:** Reported technical problem set for genomic-data generation and
> analysis systems as of 2023.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §4.4.2, printed pp. 20–22
> (PDF pp. 29–31); §6, printed p. 32 (PDF p. 41).
> **Basis / limits:** The gap categories are explicit, but categorical
> statements such as manufacturers not providing SBOMs or scanners not being
> optimized for containers are unsupported by a product census in the report.
> Treat them as dated workshop/source reports, not universal current facts.

> **Claim record — SRC-0005-C10 | source-report**
> **Claim:** NIST maps general risk-management resources — especially the NIST
> RMF, Cybersecurity Framework and Privacy Framework — to genomic-data concerns
> and argues they require mission-specific tailoring, informed-consent context,
> control assessment and continuous monitoring.
> **Claim status:** active
> **Scope:** Framework applicability and report-authored mapping, not compliance
> or implementation evidence.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §4.1 and Table 1, printed pp. 13–15
> (PDF pp. 22–24); §§4.2–4.3, printed pp. 16–19
> (PDF pp. 25–28); Conclusion, printed p. 33 (PDF p. 42).
> **Basis / limits:** The mappings and need for tailoring are direct. The
> inventory mixes U.S. Government, international and industry resources current
> to publication and neither demonstrates adoption nor evaluates comparative
> control effectiveness.

> **Claim record — SRC-0005-C11 | source-report**
> **Claim:** The report records a June 2023 Initial Public Draft Cybersecurity
> Framework Profile for Genomic Data, describes a Privacy Framework Profile as
> planned, and presents sequencer MUD micro-segmentation, pipeline security
> baselines, genomic risk-management demonstrations and privacy-enhancing
> technology demonstrations as candidate responses; it also acknowledges that
> PETs have applicability, performance, accuracy and composition limits and are
> not complete standalone solutions.
> **Claim status:** active
> **Scope:** Mixed Initial-Public-Draft, planned and proposed solution status
> with expected benefits; not deployed or validated safeguards.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §5.1–§5.6, printed pp. 23–31
> (PDF pp. 32–40); Figure 3, printed p. 26 (PDF p. 35);
> §6, printed p. 32 (PDF p. 41); Conclusion, printed p. 33
> (PDF p. 42).
> **Basis / limits:** Maturity labels differ: the cybersecurity Profile had an
> Initial Public Draft, the privacy Profile was planned, Figure 3 is notional,
> and demonstrations are proposed. The report supplies no implementation
> cohort, benchmark result, adversarial evaluation, operational test or
> independent effectiveness evidence for these genomic uses. No `INC` follows
> from the use cases.

> **Claim record — SRC-0005-C12 | artifact-observation**
> **Claim:** As of 2026-07-12, the official CSRC page presents NIST IR 8432 as
> the December 2023 final publication and records a 2023-03-03 draft followed
> by the 2023-12-20 final; the local 55-page artifact carries the final title
> and contains no draft marking.
> **Claim status:** active
> **Scope:** Publication identity and visible CSRC document history, not a
> systematic search for all later genomics publications.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** official CSRC publication page, accessed 2026-07-12; local
> artifact cover/title pages (PDF pp. 1–2) and notices (PDF p. 3).
> **Basis / limits:** Current web presentation can change. No correction or
> retraction is visible on that page, but absence there is not proof that no
> related or superseding publication exists.

## Scope and methods

The report asks what properties make genomic data distinctive, which
cybersecurity/privacy concerns and current practices apply across its lifecycle,
where stakeholders perceive gaps, and which candidate solutions could address
them. It covers human and non-human genomic information, NGS, variant calling,
genome editing and DTC testing, but human privacy, U.S. national security and the
U.S. bioeconomy dominate the analysis.

The evidence-development process combines:

- a January 26, 2022 virtual workshop on challenges, reported as 5.5 hours with
  nearly 500 stakeholders;
- May 18–19, 2022 virtual sessions focused on sequencer security,
  security-sensitive human data, risk management and EHR use;
- feedback solicited at HIMSS on March 16, 2022;
- presentations and discussion from government, research, privacy, industry,
  cloud, healthcare and bioeconomy participants; and
- subsequent selected research and an 88-item reference list.

Appendix B reports agendas and presenters, but the document has no dedicated
empirical methods section. It does not provide participant recruitment and
demographics, a sampling strategy, systematic-search protocol, inclusion/
exclusion criteria, qualitative coding procedure, evidence-grading scheme or
conflict-of-interest analysis. Results therefore represent NIST's expert and
stakeholder synthesis, not measured sector prevalence or consensus.

## Limitations and conflicts

- The analysis is U.S.-centric. International frameworks and laws appear as
  context, but U.S. national-security, bioeconomy, federal-law and healthcare
  concerns structure the report. It cannot establish global legal duties or
  practice.
- Workshops and selected literature are not a representative empirical survey
  or systematic review. The report does not estimate likelihood for the
  national-security concerns and does not quantify exposure, incidence or
  consequence distributions.
- `Cyberbiosecurity` appears as a keyword, but the report does not define the
  discipline; it is not an independent definitional source for `CON-0001`.
- Manufacturing/agriculture integrity concerns remain stakeholder- and
  literature-derived risk statements. They do not independently corroborate
  `RSK-0002`, and the four-stage genomic lifecycle does not validate WHO's
  broader material-custody lifecycle in `WFL-0004`.
- Figure 1 is a partial lifecycle: sample collection/preparation are mostly out
  of scope and retention/disposal sit outside the figure. Full custody,
  identity, consent propagation, lineage and disposal implementation remain
  unresolved.
- Legal, policy, product and technical-gap statements describe the 2022–2023
  landscape. They must not be described as current in 2026 without checking
  primary legislation, final NIST profiles, vendor capabilities and current
  practice.
- Strong re-identification and anonymization statements are secondary and at
  times categorical. Primary studies and their populations, data types, threat
  models and probability estimates require separate appraisal before stronger
  generalization.
- The report's challenges, future concerns and use cases are potential or
  simulated; they are not incidents. No `INC` page is supported by this source
  alone, and attack occurrence statements require their underlying primary
  evidence.
- Solution ideas, expected benefits and the notional MUD architecture do not
  establish implementation, testing, safety compatibility or effectiveness.
  PET sections themselves acknowledge computational, accuracy, composition and
  applicability limits.
- Broad claims about sequencer connectivity, manufacturer SBOM availability,
  container scanners and third-party software are not backed by a disclosed
  product census or deployment sample.
- Internal citations contain editorial inconsistencies: §1.1 points to [2]–[3]
  for two workshops although the reference list places them at [3]–[4], and
  rendered Figures 1–2 cite Naveed et al. as [6] although the reference list
  places Naveed et al. at [7]. Chapter 5 has further mismatches: SP 1800-15,
  CIS Benchmarks, NISTIR 8259 and SBOM entries are cited with neighboring wrong
  numbers, while the federated homomorphic-encryption discussion points to
  bibliography [87], an unrelated blockchain report, instead of the matching
  [88]. Trace important secondary or “demonstrated/proven” claims by title and
  independently read the intended primary source rather than trusting the
  bracket number.
- §2.6 calls the May 18–19 sessions the `first` NCCoE public workshop, while
  the acknowledgments, development narrative and Appendix B place the January
  26 workshop first and May second. On printed p. 10, citation [28] attached to
  a whole-genome anonymization statement points to an unrelated
  cyberbiosecurity article. These editorial defects further limit secondary
  claim tracing without title-level verification.
- The commercial-entity notice states that identification does not imply NIST
  recommendation or endorsement (PDF p. 3). No dedicated funding or
  conflict-of-interest disclosure was identified; that absence is not evidence
  that no interests existed.
- Potential biological-misuse discussion remains high-level in the wiki. No
  sequences, exploit steps, facility access paths or operational evasion detail
  are reproduced.

## Version status

The official CSRC page checked 2026-07-12 identifies a draft dated 2023-03-03
and this final dated 2023-12-20. The local artifact is the final December 2023
NIST IR 8432 and exposes DOI `10.6028/NIST.IR.8432`. The page shows no correction
or retraction notice. Current status is web-dependent and scheduled for review
by 2026-10-10; this source note does not claim that IR 8432 is the latest NIST
genomics publication or that its 2023 gaps remain unresolved.

IR 8467 2pd documents a later stage of the profile work anticipated in Chapter
5: cybersecurity and privacy outcomes are integrated against CSF 2.0 and PF
1.0. It does not replace IR 8432's distinct final report on properties, risks
and gaps.

> **Claim record — SRC-0005-C13 | analytic-judgment**
> **Claim:** The cybersecurity Profile and planned Privacy Profile described in
> IR 8432 later appear as the integrated IR 8467 Second Public Draft; this
> follow-on improves profile specificity but neither supersedes IR 8432 nor
> forms an independent evidence lineage for incidents, risk prevalence or
> control effectiveness.
> **Claim status:** active
> **Scope:** Version/programme reconciliation between two NIST/NCCoE genomics
> publications.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** this source, §§5.1–5.2, printed pp. 23–25
> (PDF pp. 32–34); [SRC-0006](src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1 and 4, printed pp. 1–6, 20–21 (PDF pp. 12–17, 31–32).
> **Basis / limits:** The publication trajectory, programme and overlapping
> inputs/authorship are direct. Non-independence is a conservative wiki
> judgment; IR 8467 includes later privacy sessions and new CSF 2.0 analysis.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
  — reuses the independent genomic RMF monitoring/response/recovery line in a
  biological-AI exact-edge control reconciliation; no AI implementation or
  effectiveness is inferred.
- [SYN-0018](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
  — counts IR 8432/8467 once as the independent NIST programme line for the
  biological-AI asset and exact-edge control cells.

- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [RSK-0003 — Genomic-data integrity compromise and decision harm](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0004 — Genomic-data disclosure and kin privacy](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0005 — Technically authorized processing and genomic privacy harm](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
- [CTL-0002 — Genomic data risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [SRC-0006 — NIST IR 8467 2pd](src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [AST-0006 — clinical/public-health laboratory assets](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [HAZ-0002 — specimen/result quality hazard](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md)
- [RSK-0013 — laboratory result/decision paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [SYN-0013 — CPH testing/lifecycle reconciliation](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)
- [SYN-0023 — Laboratory transfer/incident reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
