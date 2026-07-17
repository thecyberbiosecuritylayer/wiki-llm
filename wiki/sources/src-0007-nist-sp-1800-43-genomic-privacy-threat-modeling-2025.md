---
id: SRC-0007
type: source
title: Genomic Data Threat Modeling — Volumes A and C
aliases:
  - NIST SP 1800-43 Initial Public Draft
  - NIST SP 1800-43A Executive Summary
  - NIST SP 1800-43C Privacy
  - NCCoE Genomic Data Threat Modeling static supplement
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: exercise
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/nist-sp-1800-43c-genomic-privacy-draft-2025.pdf
sha256: 025265bd5f02bd793f30ce2ace968ef5ce93fc94ee57d4b0474f65f769058139
raw_components:
  - path: ../../raw/nist-sp-1800-43a-genomic-threat-model-draft-2025.pdf
    role: volume-a-executive-summary
    sha256: 02dd8445f753dc15efdb7a32cc7800a8cd896dc9026c74d35d46a1a8cfcfb219
  - path: ../../raw/nist-sp-1800-43-supplement-bdc395e-2026-07-12.tar.gz
    role: official-static-supplement-commit-snapshot
    sha256: 4e781fb4dea69e4db14ef6ddb22dcbcb5f1942054708d4896a5334db4c3741fa
    commit: bdc395e52479f069c02cc1343f88ba0bb6f6bf5e
canonical_url: https://csrc.nist.gov/pubs/sp/1800/43/ipd
project_url: https://www.nccoe.nist.gov/projects/cybersecurity-and-privacy-genomic-data
supplement_url: https://pages.nist.gov/nccoe-genomic-data-threat-modeling/
repository_url: https://github.com/usnistgov/nccoe-genomic-data-threat-modeling
accessed: 2026-07-12
transient: true
issuer: National Institute of Standards and Technology
version: initial-public-draft
publication_date: 2025-08-05
jurisdictions:
  - United States
tags:
  - genomics
  - genomic-data
  - privacy
  - threat-modeling
  - exercise
  - draft-guidance
---

# Genomic Data Threat Modeling — Volumes A and C

## Bibliographic identity

Ronald Pulivarti, Justin Wagner, Brett Kreider, Stuart S. Shapiro, Julie
Nethery Snyder, Kevin E. Wilson, Martin Wojtyniak, Scott Ross, Philip Whitlow,
Isabelle Brown-Cantrell, Patrick Pape and Jared Sheldon. *Genomic Data Threat
Modeling: An Implementation for Genomic Data Sequencing and Analysis*. NIST
Special Publication 1800-43, Initial Public Draft, Volumes A and C.
Gaithersburg, MD: National Institute of Standards and Technology, August 2025.

In the wiki, this is one compound `exercise` source package comprising **only
the published Volumes A and C** and their official static supplement. Volume A
is a two-page Executive Summary; substantive evidence here comes mainly from
Volume C and online-only Appendices C–G. The separate NIST CSWP 35 Initial
Public Draft is not included: as of 2026-07-12 it had not been published as SP
1800-43B and has its own bibliographic identity.

## Provenance

- Substantive local artifact: Volume C,
  `../../raw/nist-sp-1800-43c-genomic-privacy-draft-2025.pdf`, 1,535,894 bytes,
  PDF 1.6, 56 physical pages, SHA-256
  `025265bd5f02bd793f30ce2ace968ef5ce93fc94ee57d4b0474f65f769058139`.
- Executive-summary artifact: Volume A,
  `../../raw/nist-sp-1800-43a-genomic-threat-model-draft-2025.pdf`, 386,194
  bytes, PDF 1.6, 5 physical pages, SHA-256
  `02dd8445f753dc15efdb7a32cc7800a8cd896dc9026c74d35d46a1a8cfcfb219`.
- Both PDFs are unencrypted and contain no JavaScript, forms or embedded files.
  Each is byte-identical to the corresponding official NCCoE download checked
  on 2026-07-12.
- Volume C pagination: printed p. 1 is PDF physical p. 10; through printed
  p. 47 the stable relation is `PDF physical page = printed page + 9`.
  Printed pp. 46–47 end with references and links to online-only Appendices
  C–G. Volume A printed pp. 1–2 are PDF physical pp. 4–5.
- Official static supplement:
  `../../raw/nist-sp-1800-43-supplement-bdc395e-2026-07-12.tar.gz`, 20,658,363
  bytes, 165 archive entries, SHA-256
  `4e781fb4dea69e4db14ef6ddb22dcbcb5f1942054708d4896a5334db4c3741fa`.
  It is the GitHub archive for exact commit
  `bdc395e52479f069c02cc1343f88ba0bb6f6bf5e` of the official NIST
  repository. The commit snapshot contains the published RST and media for
  Volumes A and C, including Appendices C–G, but no Volume B.
- Fully reviewed: Volume A printed pp. 1–2; Volume C front matter, Summary,
  §§1–3, Figures 1–4, Tables 1–21, Appendices A–B and all references; all
  current split RST for online Appendices C–G and their referenced diagrams,
  mappings and ranking artifacts. Repository scripts, JavaScript, build files
  and development DOCX were treated as untrusted source content and not
  executed.
- The static tree also contains an unreferenced monolithic
  `source/Vol_C/Appendix.rst` that differs from the split files selected by the
  current toctree. It is retained in the immutable snapshot as repository
  residue, not merged as additional published findings.

## Executive summary

Volume C demonstrates an iterative privacy threat-modeling process against
generalized clinical and research genomic-sequencing environments. The team
framed business/privacy context with adapted NIST PRAM worksheets, mapped
components and physical/digital dataflows, used LINDDUN and PANOPTIC to identify
and cross-check possible privacy threats, assigned subjective feasibility and
difficulty categories for ordering, and illustrated how selected threats can
lead to candidate Privacy Framework and SP 800-53 controls.

This is stronger than a purely proposed method because the authors applied it
to two bounded use cases and report sending reference material to a sequencing
center and receiving data for secondary analysis. It is not a representative
deployment study, observed attack corpus, vulnerability assessment, control
implementation, effectiveness test or independent evaluation. Its scenario
and taxonomy “validation” checks analytical consistency, not whether an attack
occurred or a control prevented harm.

## Claims and locators

> **Claim record — SRC-0007-C01 | artifact-observation**
> **Claim:** The currently published SP 1800-43 package contains Initial Public
> Draft Volumes A and C plus an official static supplement; it does not contain
> a published SP 1800-43B.
> **Claim status:** active
> **Scope:** Official artifacts and publication records checked on 2026-07-12.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local A/C artifacts and static-supplement archive described in
> Provenance; CSRC publication record; NCCoE project page; static-site root.
> **Basis / limits:** The archive file list and current web records are direct.
> CSRC's 2025 announcement says CSWP 35 would become Volume B when finalized,
> but that forecast does not establish later publication. Web status is
> volatile and must be rechecked.

> **Claim record — SRC-0007-C02 | source-report**
> **Claim:** Volume C applies privacy threat modeling to generalized clinical
> and research sample environments that send physical material to a sequencing
> service, receive digital results and perform subsequent analysis; the NCCoE
> team reports exercising the sample-to-service handoff with DNA reference
> material.
> **Claim status:** active
> **Scope:** The paper's bounded example and exercise, not a universal genomic
> workflow or a production deployment.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Volume C §1.2 and Figure 1, printed pp. 2–3 (PDF pp. 11–12);
> §2.1 and §2.1.4, printed pp. 7–19 (PDF pp. 16–28); Appendix E in the static
> supplement.
> **Basis / limits:** The handoffs and reported reference-material exercise are
> direct. The source does not report chain-of-identity/custody test results,
> consent synchronization, protocol assurance, security testing, error rates
> or representativeness; detailed topology is intentionally not reproduced.

> **Claim record — SRC-0007-C03 | source-report**
> **Claim:** The demonstrated Four Question process documents scope and
> dataflows, identifies possible privacy threats, prioritizes responses and
> then calls for iterative review of the model and selected interventions.
> **Claim status:** active
> **Scope:** Reusable assessment method for a locally bounded genomic-data
> environment.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Volume C Summary, printed p. 1 (PDF p. 10); §§2.1–2.4, printed
> pp. 7–43 (PDF pp. 16–52); static Appendix D, `Methodology Overview`.
> **Basis / limits:** Steps and iteration are direct. The sequence is a method,
> not evidence that every organization completed it or that its outputs are
> exhaustive, accurate or effective.

> **Claim record — SRC-0007-C04 | source-report**
> **Claim:** The paper treats privacy threats as broader than hostile external
> cyber activity: they may arise from inaction, ordinary processing side
> effects or a system operating as designed, and are evaluated from the data
> subject's perspective.
> **Claim status:** active
> **Scope:** Privacy-threat-modeling frame used in this exercise; not a finding
> that a named organization caused privacy harm.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Volume C §§1.4–1.6, printed pp. 4–6 (PDF pp. 13–15); static
> Appendix C, `Privacy Threat Modeling` and `LINDDUN`.
> **Basis / limits:** The distinction is explicit. Illustrative examples and
> taxonomy entries are not incidents, prevalence estimates or legal findings.

> **Claim record — SRC-0007-C05 | source-report**
> **Claim:** The exercise cross-checks possible threats by requiring a
> PANOPTIC attack to map to a LINDDUN threat and to threaten at least one NIST
> privacy engineering objective, then ranks retained threats with analyst-set
> feasibility, difficulty and LINDDUN weights.
> **Claim status:** active
> **Scope:** Internal analytical screening and ordering in the example.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Volume C §§2.2.2–2.3.1 and Tables 13–20, printed pp. 24–35
> (PDF pp. 33–44); static Appendices D, F and G.
> **Basis / limits:** “Validated” means consistency with the chosen taxonomies
> and objectives. Numeric values order this example and do not measure attack
> probability, risk, consequence severity, model accuracy or external validity.

> **Claim record — SRC-0007-C06 | source-report**
> **Claim:** For Question 3 the source presents eliminate, disrupt, transfer or
> accept as response choices and illustrates a path from selected threat
> actions through Privacy Framework priorities to candidate SP 800-53 controls;
> Question 4 provides review and future-testing guidance.
> **Claim status:** active
> **Scope:** Candidate response selection and assurance planning, not evidence
> that a safeguard was deployed or worked.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Volume C §§2.3.2–2.4.4 and Table 21, printed pp. 35–43
> (PDF pp. 44–52); static Appendices C–D.
> **Basis / limits:** Response options, mappings and recommendations are
> direct. The paper selects an illustrative intervention but gives no deployed
> configuration, test protocol, outcome measure or effectiveness result.

> **Claim record — SRC-0007-C07 | analytic-judgment**
> **Claim:** SP 1800-43 A/C supports an example-applied privacy threat-modeling
> control and bounded workflow/system context, but it does not support an
> `INC`, deployed vulnerability, representative architecture, likelihood,
> implemented risk-reduction safeguard or effectiveness claim.
> **Claim status:** active
> **Scope:** Evidence sufficiency of this source package for wiki integration.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Volume C Summary and §§1–3, printed pp. 1–43 (PDF pp. 10–52);
> static Appendices C–G; Volume A printed pp. 1–2 (PDF pp. 4–5).
> **Basis / limits:** The source repeatedly calls its environments, attacks and
> interventions examples or possibilities and gives local tailoring/review
> guidance. Performing the assessment method is implementation evidence for
> that method only; it is not evidence that mapped safeguards were implemented
> or reduced harm.

## Scope and methods

### Question 1 — bound the system

The paper adapts PRAM Worksheets 1 and 2, records organizational and individual
context, associates components with responsible entities and labels physical
and digital data actions. The complete example spans a clinical use case and a
research use case; the simpler core example is explanatory. The current static
Appendix E supplies the complete diagrams, which are used here only to support
functional boundaries—not to publish an operational network map.

### Question 2 — enumerate and screen possibilities

LINDDUN is applied per dataflow segment. PANOPTIC supplies contextual domains,
privacy activities and attack-scenario groupings. Retained entries must map
across the two taxonomies and threaten predictability, manageability or
disassociability. This increases internal traceability but does not empirically
validate attack feasibility or completeness.

### Question 3 — prioritize and select responses

The source assigns categorical feasibility and a five-step difficulty scale,
combines them with adjustable threat-type weights, and uses the resulting
values only to rank example entries. Organizations are told to tailor inputs
and choose elimination, disruption, transfer or acceptance. Candidate
disruptions can be traced from a critical privacy action through NIST Privacy
Framework Subcategories and IR 8467 priorities to SP 800-53 controls.

### Question 4 — review and iterate

The paper recommends reviewing scope, diagrams, assumptions, identified
threats and responses; considering exercises, red-team or other testing where
appropriate; and maintaining the model as system and threat conditions change.
These are future assurance activities. No reported test result closes the loop
inside this draft.

## Limitations and conflicts

- Volume C explicitly limits its exercise to a small set of use cases and
  organizations. It does not establish a reference architecture, sector
  prevalence, likelihood or consequence distribution.
- The paper reports potential attacks and internally “validated” model entries,
  not observed exploitation. No threat, technique, vulnerability or incident
  entity should be inferred solely from the tables or diagrams.
- The same NIST/NCCoE programme produced `SRC-0005`, `SRC-0006` and this source.
  Multiple publication IDs and workshop/partner input do not create materially
  independent corroboration.
- Volume A writes `confidentially`, `solution illustrate` and `LINDUNN`; the
  substantive Volume C uses `LINDDUN`. Volume A also says partner technologies
  are “shown below,” but its rendered content contains no such list.
- Volume A PDF metadata spells Martin Wojtyniak's surname `Wojtniak`; CSRC uses
  `Phillip Whitlow`, whereas the PDFs use `Philip Whitlow`. These are identity
  metadata defects, not competing technical findings.
- Volume C Appendix A's LINDDUN expansion omits Non-repudiation even though
  Appendix C includes it. Appendix B reference [5] labels IR 8467 as a 2023
  Initial Public Draft while linking the 2024 Second Public Draft DOI.
- Question 4 briefly refers to having “implemented interventions,” while
  Question 3 and the conclusion provide an illustrative selection. This wiki
  follows the detailed evidence and classifies safeguard implementation and
  effectiveness as unknown.
- The current static root has an empty abstract, while the Volume C page and PDF
  have one. The CSRC record says `No Download Available` even though the NCCoE
  project page provides the official A/C PDFs.
- Detailed diagrams and attack tables contain operational context. The wiki
  retains only defensive abstractions needed for scoping and assurance and does
  not consolidate access paths, system topology or attack instructions.

## Version status

The CSRC record, accessed 2026-07-12, still labels SP 1800-43 an **Initial
Public Draft**, published 2025-08-05, with comments closed 2025-09-04. The NCCoE
project status is **Reviewing Comments** and currently links only draft Volumes
A and C. The static site calls CSWP 35 the draft cybersecurity companion; its
statement that the white paper would later become Volume B is a publication
plan, not evidence that the conversion occurred.

The source is voluntary draft practice material and explicitly disclaims
regulatory or statutory authority. Current status and supplement content must
be rechecked by `review_after` or before relying on them as current.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [CTL-0003](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md) — new
  reusable, example-applied assessment control; testing and effectiveness
  remain unknown.
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — adds a bounded
  sample-to-service-to-digital-result exercise and physical/digital handoffs.
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) — adds
  example-applied responsibility and dataflow modeling, not a reference
  architecture.
- [RSK-0004](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md) —
  adds hypothetical model support, not an incident or likelihood estimate.
- [RSK-0005](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
  — strengthens the distinction between cyber compromise and privacy threat
  from ordinary or designed processing.
- [HAZ-0002](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md)
  — keeps non-adversarial quality/identity failure separate from privacy threat.
- [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
  — bounded clinical/public-health transfer paths with evidence states separated.
- [SYN-0013](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
  — uses the privacy-state distinction without treating the exercise as an incident.
- No `INC`, `THR`, `TEC` or `VUL` page is created.
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)
