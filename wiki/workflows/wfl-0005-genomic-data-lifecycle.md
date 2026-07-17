---
id: WFL-0005
type: workflow
title: Genomic data lifecycle
aliases:
  - genomic information lifecycle
  - genomic-data flow
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0008
  - SRC-0014
  - SRC-0015
  - SRC-0016
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: WFL-0005-C01
    evidence:
      - source: SRC-0005
        locator: "§2.1, printed pp. 3–4 (PDF pp. 12–13); Figure 1"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: WFL-0005-C04
    evidence:
      - source: SRC-0006
        locator: "§1.2 and Figure 1, printed pp. 4–5 (PDF pp. 15–16)"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: WFL-0005-C06
    evidence:
      - source: SRC-0007
        locator: "Volume C §1.2 and Figure 1, printed pp. 2–3 (PDF pp. 11–12); §§2.1 and 2.1.4, printed pp. 7–19 (PDF pp. 16–28); static Appendix E"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: WFL-0005-C07
    evidence:
      - source: SRC-0008
        locator: "pp. 30–31"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: WFL-0005-C08
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3, 3 and 5, printed pp. 767–773 (PDF pp. 4–10)"
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: WFL-0005-C09
    evidence:
      - source: SRC-0015
        locator: "28 CFR §§202.201, .210, Subparts C–E and J–K, final-rule PDF pp. 72–95 / 90 FR 1707–1730"
  - predicate: governed-by
    target: GOV-0005
    claim_id: WFL-0005-C09
    evidence:
      - source: SRC-0015
        locator: "28 CFR §§202.201, .210, Subparts C–E and J–K, final-rule PDF pp. 72–95 / 90 FR 1707–1730"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: WFL-0005-C10
    evidence:
      - source: SRC-0016
        locator: "Articles 3–16, 50–80 and 105, PDF pp. 34–39, 57–80, 90–91"
  - predicate: governed-by
    target: GOV-0006
    claim_id: WFL-0005-C10
    evidence:
      - source: SRC-0016
        locator: "Articles 1–2 and 105, PDF pp. 29–33, 90–91"
  - predicate: depends-on
    target: AST-0001
    claim_id: WFL-0005-C02
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §3.7, printed p. 12 (PDF p. 21)"
  - predicate: depends-on
    target: SYS-0003
    claim_id: WFL-0005-C03
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §4.4.2, printed pp. 20–22 (PDF pp. 29–31)"
tags:
  - genomics
  - workflow
  - data-lifecycle
  - consent
  - privacy
---

# Genomic data lifecycle

> NIST IR 8432 presents four source-defined stages, while IR 8467 2pd adds a
> fifth stage—data disposition—after sample collection, sample preparation,
> data generation, and data analysis. Storage, sharing, EHR integration, reanalysis,
> and retention cross these stages, as do consent and provenance contexts.
> This is a high-level model, not a validated chain of custody, consent
> propagation, or end-to-end data lineage. SP 1800-43C adds a bounded
> sample-to-service exercise and applied dataflow modeling, but does not make it
> a representative or validated end-to-end workflow.

## Scope and source boundary

Figure 1 includes four stages, but the report treats sample collection and
sample preparation as largely outside its cybersecurity scope. Its main focus
is data generation and analysis, although privacy and consent considerations
keep human sample collection in clinical care or studies relevant
([SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
§2.1, printed pp. 3–4).

> **Claim record — WFL-0005-C01 | source-report**
> **Claim:** Figure 1 of NIST IR 8432 models the genomic lifecycle as sample
> collection, sample preparation, data generation, and data analysis, with the
> first two stages largely outside the report's scope.
> **Claim status:** active
> **Scope:** Source workflow for genomic information, not a complete clinical,
> laboratory or biobank lifecycle.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); Figure 1.
> **Basis / limits:** The stages and scope boundary are direct. The body caption
> incorrectly identifies Naveed et al. as reference `[6]`; the List of Figures
> gives the correct reference `[7]`. The figure does not model identity,
> authorization, trust boundaries, or retention as formal stages.

### Five-phase draft extension

IR 8467 2pd retains the first four labels and makes `data disposition` an
explicit fifth phase. Its primary profile scope covers generated sequence and
other data, as well as derived analytical data; privacy-related processes
initiated before collection can feed requirements into in-scope phases.

> **Claim record — WFL-0005-C04 | source-report**
> **Claim:** Figure 1 of NIST IR 8467 2pd models a five-phase genomic-data
> lifecycle from sample collection to data disposition and explains that
> privacy outcomes may become relevant before collection and influence later
> processing.
> **Claim status:** active
> **Scope:** Draft profile lifecycle and scope boundary, not an implemented
> sample-to-disposal workflow.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §1.2 and Figure 1, printed pp. 4–5 (PDF pp. 15–16).
> **Basis / limits:** Stage labels and scope statement are direct and the
> figure was visually checked. The extension does not validate physical
> custody, identity, consent synchronization, retention authority, deletion or
> backup disposition.

### Applied sample-to-service exercise

SP 1800-43C narrows one part of the broader lifecycle to client/partner →
sequencing service → returned digital result → secondary analysis. It reports
that the NCCoE team sent DNA reference material to a genomic center and
received the resulting data, then used generalized clinical and research
environments to document physical and digital data actions. This is direct
evidence that the **modeling exercise** was applied to a real handoff; it is not
evidence that the published model is a production workflow or that security,
privacy, identity and custody were validated.

> **Claim record — WFL-0005-C06 | source-report**
> **Claim:** NIST SP 1800-43C reports a bounded reference-material exercise
> spanning physical transfer to a genomic sequencing service, return of digital
> results and secondary analysis, and applies dataflow modeling to generalized
> clinical and research use cases.
> **Claim status:** active
> **Scope:** Sample environments and handoffs studied by the draft, not a
> representative sector workflow or complete lifecycle.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §1.2 and Figure 1, printed pp. 2–3 (PDF pp. 11–12); §§2.1 and
> 2.1.4, printed pp. 7–19 (PDF pp. 16–28); static Appendix E.
> **Basis / limits:** The reported exercise and modeled handoffs are direct.
> The source supplies no representative sampling, identity/custody test,
> consent-propagation result, protocol assurance, error rate, threat occurrence
> or end-to-end control validation. Operational topology is not reproduced.

### Operational clinical genotyping segment

An independent NHSBT institutional source documents one live segment of the
human-genomic lifecycle: a patient provides a blood sample for DNA-based
extended blood-group testing, a genotype is established and the result supports
future transfusion matching. It does not document the full data lifecycle,
identity/provenance controls or downstream outcome validation.

> **Claim record — WFL-0005-C07 | source-report**
> **Claim:** NHSBT reports an operational sample→DNA-based genotype→transfusion-
> matching decision segment with more than 5,300 extended blood-group genotype
> tests during 2024–25.
> **Claim status:** active
> **Scope:** One English clinical programme for haemoglobinopathy/rare-anaemia
> care, not a complete genomic-data lifecycle or universal workflow.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 30–31.
> **Basis / limits:** Sample, test purpose and count are direct. The report
> provides no data schema, custody/identity evidence, pipeline validation,
> consent propagation, matching outcome or independent effectiveness result.

### Controlled material-to-digital processing segment

Ney et al. add an independent empirical segment spanning physical input,
sequencing, derived digital reads and downstream software. The same run also
measured cross-sample association errors. This validates that material/input
state can propagate into digital processing; it does not validate the full
collection-to-disposition lifecycle or a production architecture.

> **Claim record — WFL-0005-C08 | source-report**
> **Claim:** A controlled USENIX study traversed physical sequencing input→
> digital reads→downstream processing and separately measured cross-sample read
> assignment in the generation-to-analysis handoff.
> **Claim status:** active
> **Scope:** One artificial execution setup and one multiplex run; not a
> representative workflow, incident or end-to-end custody/consent validation.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§2.2–2.3, 3 and 5, printed pp. 767–773 (PDF pp. 4–10).
> **Basis / limits:** Material, measurement, derived-file and processing stages
> are directly exercised. The target was deliberately modified and the run
> does not establish identity, consent, disposition or operational prevalence.

## Lifecycle model

| Phase | Source-supported flow | Important unresolved state |
| --- | --- | --- |
| Collect | A laboratory or clinic obtains a biological sample and associated context | Identity, consent and physical custody are mostly outside report scope |
| Prepare | The sample is prepared for measurement | Procedure-level controls and sample transformations are not modeled |
| Generate | A sequencer or other measurement produces raw genomic data | Device configuration, provenance and transfer assurance are not validated |
| Analyze | Software/pipelines interpret raw data, including variant-oriented analysis | Pipeline dependencies, reproducibility and decision gates remain incomplete |
| Store and retain | Data may reside on-premise or in cloud storage and may need long-term retention | Retention authority, immutable history and disposal proof are not specified |
| Share or integrate | Data may enter public/controlled databases, research exchange or EHR workflows | Consent propagation, recipient authorization and downstream reuse remain gaps |
| Reanalyze | Data may require later reinterpretation as knowledge or purpose changes | Trigger, lineage, authorization and decision revalidation are not specified |
| Dispose | IR 8467 makes disposition a lifecycle phase; retention, deletion or transfer may change data state | Authority, deletion scope, backups, downstream copies and proof are not validated |

The table combines Figure 1 with adjacent prose; NIST does not present it as one
implemented sequence.

> **Claim record — WFL-0005-C02 | source-report**
> **Claim:** NIST IR 8432 reports that genomic data may move from generation to
> on-premise or cloud storage, open-source or commercial analysis, public or
> controlled-access databases and EHR-related use; it also identifies sharing,
> reanalysis, retention, disposal, consent and chain-of-custody as important
> lifecycle considerations.
> **Claim status:** active
> **Scope:** Candidate genomic-data flows across research and clinical contexts.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); §§2.2–2.3, printed pp. 4–5
> (PDF pp. 13–14); §3.7, printed p. 12 (PDF p. 21).
> **Basis / limits:** Flows and considerations are explicit, but report does
> not define a canonical event model, consent schema, EHR implementation,
> retention schedule or deletion proof.

## Data states and decision dependencies

At a defensive level the workflow distinguishes:

- biological sample and associated identity and consent context;
- raw measurements from data generation;
- processed data, variants, and analytic outputs;
- stored, aggregated, or shared datasets;
- clinical or research interpretations that may be revisited as knowledge changes.

The source describes these classes without publishing personal records or
establishing that every implementation uses the same formats or transitions.

IR 8467 adds a target-state provenance envelope: origin, custody changes,
annotations, derived data, data/software versions, configuration and analysis
parameters. It also recommends that processing permissions and consent context
remain associated with data across sharing and changing partners.

> **Claim record — WFL-0005-C05 | source-report**
> **Claim:** IR 8467 2pd recommends lifecycle provenance covering origin,
> custody, derived states and processing dependencies, together with consent
> and processing-permission context that travels with shared data.
> **Claim status:** active
> **Scope:** Desired lifecycle state for genomic processing, not proof of an
> interoperable schema or operational propagation.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§5.1, 5.4 and 5.6, printed pp. 22–25 (PDF pp. 33–36);
> Tables 10 and 33, printed pp. 64–77 and 155–158
> (PDF pp. 75–88 and 166–169); Appendix C `Provenance`, printed p. 174.
> **Basis / limits:** Provenance dimensions and permission/consent outcomes
> are explicit recommendations. The profile supplies no canonical metadata
> schema, implementation sample, synchronization test or deletion proof.

## Systems and candidate trust boundaries

[SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) supplies
the functional ecosystem used by the source model. Candidate handoffs include:

- clinic/laboratory collection context ↔ preparation and generation;
- generation device ↔ local or cloud storage;
- raw/processed data ↔ analysis pipeline and third-party software;
- institutional environment ↔ public or controlled-access repository;
- research/analysis output ↔ EHR or downstream decision workflow;
- data holder ↔ other organizations with different consent and policy duties.

> **Claim record — WFL-0005-C03 | analytic-judgment**
> **Claim:** NIST IR 8432 supports a functional system-and-handoff map for
> genomic data, but not validated trust boundaries, network architecture,
> end-to-end provenance, chain of identity/custody or consent propagation.
> **Claim status:** active
> **Scope:** Coverage assessment of the source workflow after `SRC-0005`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §4.4.2, printed
> pp. 20–22 (PDF pp. 29–31); Figure 1.
> **Basis / limits:** Source names stages, systems and gaps but gives no
> implementation sample or validated cross-organization data lineage. Figure 3
> is explicitly notional and is not used as a deployed architecture.

### Covered-access and transaction overlay

Part 202 adds a governance overlay to the lifecycle rather than a sixth
scientific phase. It classifies access through data brokerage and vendor,
employment or investment agreements, then connects relevant transactions to
controls, diligence, audit, retention and reporting. It does not validate
sample identity, consent propagation, sequencing, interpretation or
disposition.

> **Claim record — WFL-0005-C09 | analytic-judgment**
> **Claim:** Part 202 overlays the genomic lifecycle with classified access/
> transaction, control, diligence, audit, record and reporting stages, but does
> not define or validate the underlying collection-to-disposition workflow.
> **Claim status:** active
> **Scope:** U.S. covered-transaction governance overlay, not a universal
> genomic workflow or proof that access or transfer occurred.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.201, .210, Subparts C–E and J–K, PDF pp. 72–95 /
> 90 FR 1707–1730.
> **Basis / limits:** Transaction and compliance stages are direct. Their
> placement as an overlay on `WFL-0005` is an inference limited to the
> sharing/reuse/access branch; it neither replaces the biological/data
> lifecycle nor establishes implementation.

### EHDS primary/secondary-use overlay

EHDS adds two staged governance paths around the genomic lifecycle. Primary
use covers registration, patient/professional access, correction, exchange and
clinical priority categories. Secondary use covers dataset description,
application/permit, preparation, secure processing, controlled output, result
publication, retention/deletion and correction/audit. These paths govern data
actions; they do not replace sample collection, preparation, sequencing or
analysis phases.

> **Claim record — WFL-0005-C10 | analytic-judgment**
> **Claim:** EHDS overlays `WFL-0005` with distinct primary-use and secondary-
> use governance paths from registration/access/exchange through permit/secure
> processing/output/retention, while leaving the underlying genomic biological
> and analytical phases intact.
> **Claim status:** active
> **Scope:** EU EHDS-governed portions of a genomic/electronic-health-data
> lifecycle; not a deployed workflow or a claim that every genomic dataset is
> an EHR record.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> Articles 3–16, 50–80 and 105, PDF pp. 34–39, 57–80, 90–91.
> **Basis / limits:** Data-action stages are direct; their mapping onto the
> broader genomic lifecycle is editorial. Staged application and missing
> implementation evidence are preserved.

## Evidence and uncertainty

The workflow now combines two stakeholder-informed high-level NIST models, one
bounded NIST/NCCoE exercise, an independent NHSBT operational clinical segment
and an independent USENIX controlled material-to-digital segment. The first
three remain one programme lineage; NHSBT adds implementation evidence for a
narrow sample-to-genotype-to-decision use, while USENIX adds empirical reverse-
direction and cross-sample evidence. Together they still
do not establish a complete identity/custody/consent lineage, representative
practice, error rates, measured cyber exposure or safeguard effectiveness.
Missing elements are corpus gaps, not evidence that real organizations lack
them.

## Related pages

- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)

- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [RSK-0003 — Genomic-data integrity and decision harm](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0004 — Genomic-data disclosure and kin privacy harm](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0020 — Observed consumer-genetics disclosure path](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [INC-0007 — 23andMe genetic-data breach](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [RSK-0005 — Technically authorized processing and genomic privacy harm](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
- [RSK-0009 — Sequenced input to digital execution](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
- [RSK-0010 — Multiplex cross-sample exposure](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [RSK-0011 — Part 202 regulated access branches](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md)
- [CTL-0002 — Genomic-data risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [CTL-0003 — Genomic-data privacy threat modeling](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md)
- [CTL-0007 — Secure sequencing input processing](../controls/ctl-0007-secure-sequencing-input-processing.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [CTL-0009 — EHDS safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [GOV-0006 — EU EHDS governance](../governance/gov-0006-eu-ehds-regulation-2025.md)
- [SYN-0004 — US–EU governance reconciliation](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [WFL-0004 — High-consequence material lifecycle](wfl-0004-high-consequence-material-lifecycle.md)
- [SRC-0005 — NIST IR 8432](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0007 — NIST SP 1800-43 A/C](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0008 — NHSBT Annual Report 2024–25](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0014 — Ney et al. 2017](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0015 — DOJ final rule and correction chain](../sources/src-0015-us-doj-data-security-program-2025.md)
- [SRC-0016 — EU EHDS Regulation](../sources/src-0016-eu-ehds-regulation-2025.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§2.1–2.3, 3.7, 4.4.2; Figure 1.
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §§1.2, 5.1, 5.4, 5.6 and 6; Figures 1 and 4; Tables 10 and 33.
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
  Volume C §§1.2, 2.1 and 2.1.4; Figures 1 and 4; static Appendix E.
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 30–31.
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §§2–3 and 5.
- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
  §§202.201, .210, Subparts C–E and J–K.
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md), Articles 3–16,
  50–80 and 105.
