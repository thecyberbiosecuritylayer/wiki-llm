---
id: SRC-0006
type: source
title: Genomic Data Cybersecurity and Privacy Frameworks Community Profile
aliases:
  - NIST IR 8467 2pd
  - Genomic Data Profile
  - Genomic Data Profile Tailoring Spreadsheet
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: normative-guidance
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/nist-ir-8467-genomic-profile-2pd-2024.pdf
sha256: 573191dee67b2b38599169b09a5fef0bd6c07cd03a196355dfca291733a91f59
raw_components:
  - path: ../../raw/nist-ir-8467-genomic-profile-2pd-2024.xlsx
    role: official-tailoring-spreadsheet
    sha256: 062d73e24aac7684107134b64538355cb597ae762fd1cece9d44eccbbc85224d
canonical_url: https://csrc.nist.gov/pubs/ir/8467/2pd
project_url: https://www.nccoe.nist.gov/projects/cybersecurity-and-privacy-genomic-data
spreadsheet_url: https://www.nccoe.nist.gov/sites/default/files/2024-12/genomic-data-profile.xlsx
accessed: 2026-07-12
transient: true
doi: 10.6028/NIST.IR.8467.2pd
issuer: National Institute of Standards and Technology
version: second-public-draft
publication_date: 2024-12-16
jurisdictions:
  - United States
tags:
  - genomics
  - genomic-data
  - cybersecurity-framework
  - privacy-framework
  - community-profile
  - draft-guidance
---

# Genomic Data Cybersecurity and Privacy Frameworks Community Profile

## Bibliographic identity

Ronald Pulivarti, Justin Wagner, Justin Zook, Eugene Craft, Brett Kreider,
Jeremy Miller, Patrick O'Neil, Christina Sames, Julie Snyder, Bob Stea, Martin
Wojtyniak. *Genomic Data Cybersecurity and Privacy Frameworks Community
Profile*. NIST Internal Report 8467, Second Public Draft. Gaithersburg, MD:
National Institute of Standards and Technology, December 2024. DOI
`10.6028/NIST.IR.8467.2pd`.

In the wiki, this is `normative-guidance` with **draft** status: the document
proposes stakeholder-informed outcomes for an organizational Target Profile
based on NIST Cybersecurity Framework 2.0 and Privacy Framework 1.0. It does not
establish any binding force or document adoption; it is not a final standard,
implementation census, control test, or effectiveness study.

## Provenance

- Immutable primary artifact:
  `../../raw/nist-ir-8467-genomic-profile-2pd-2024.pdf`, 3,198,481 bytes,
  PDF 1.7, 185 physical pages, SHA-256
  `573191dee67b2b38599169b09a5fef0bd6c07cd03a196355dfca291733a91f59`.
- Official companion:
  `../../raw/nist-ir-8467-genomic-profile-2pd-2024.xlsx`, 269,348 bytes,
  Office Open XML workbook, SHA-256
  `062d73e24aac7684107134b64538355cb597ae762fd1cece9d44eccbbc85224d`.
- PDF unencrypted and contains no JavaScript, forms or embedded files. The
  workbook is a valid ZIP package without VBA, external relationships or
  external-link parts; its summary sheet contains ordinary local formulas.
- PDF pagination: physical pp. 1–11 are cover/front matter; printed Arabic p. 1
  begins on PDF p. 12, so `PDF physical page = printed page + 11`. Printed
  p. 174 is PDF p. 185.
- Fully reviewed: front matter, §§1–6, all four rendered figures, Tables 1–36,
  31 references, selected bibliography, acronyms and glossary. Tables 4–25
  cover all 106 CSF 2.0 Subcategories; Tables 26–36 add PF entries unique to
  the chosen crosswalk.
- All four workbook sheets were parsed: `User Guide`, `Mission Objectives`,
  `Integrated CSF 2.0 & PF Profile` and `High Priority Summaries`. The
  integrated sheet has 406 directional rows representing 206 unique outcomes
  (106 CSF and 100 PF), with nonblank priorities limited to `1`, `2` and `3`.
- Workbook core metadata reports creation on 2024-09-03 and last modification
  on 2025-01-10, during the public-comment period. It should therefore be
  treated as the official companion retrieved on 2026-07-12, not assumed
  byte-identical to a hypothetical launch-day workbook.
- Official CSRC and NCCoE pages, accessed 2026-07-12, still present this as a
  Second Public Draft with closed comment period; the NCCoE project status is
  `Reviewing Comments`. The web status is volatile (`transient: true`), while
  substantive claims are reproducible from the local PDF/XLSX package.
- The official CSRC author metadata abbreviates Eugene Craft as `R. Craft`;
  the PDF title page gives `Eugene Craft` and is used for bibliographic
  identity.

`ingest_status: complete` means the complete local PDF/XLSX package was
reviewed. It does not mean every cited external source, law, framework update
or stakeholder assertion was independently validated.

## Executive summary

IR 8467 2pd integrates CSF 2.0 and PF 1.0 into a draft genomics Community
Profile. Its scope covers assets processing human, microbiome, microbial,
model-organism and plant genomic data; privacy outcomes are emphasized when
human genomic data are processed. Figure 1 extends the earlier four-stage NIST
model to `sample collection -> sample preparation -> data generation -> data
analysis -> data disposition`, while privacy and consent considerations may
begin before collection and propagate through later processing.

The profile organizes 206 framework outcomes around 12 ranked Mission
Objectives. For each objective, outcomes receive `1` High, `2` Moderate or `3`
Other priority; `Other` expressly does not mean low. Organizations are expected
to tailor the profile to their own obligations, environment and objectives and
to compare Current and Target Profiles. The document excludes Implementation
Tiers and provides no deployment, test, outcome or independent-evaluation
results.

Development used 2022–2023 stakeholder sessions and NCCoE expert analysis.
Stakeholders first prioritized CSF 1.1 Categories; NCCoE translated those
inputs to Subcategories and later migrated them to CSF 2.0 through a crosswalk.
Privacy sessions prioritized PF Categories. Participant counts, recruitment,
raw votes, aggregation rules, consensus thresholds, disagreements and empirical
validation are not reported, so the matrix is stakeholder-informed draft
guidance rather than a measured sector baseline.

## Claims and locators

> **Claim record — SRC-0006-C01 | artifact-observation**
> **Claim:** NIST identifies the artifact as NIST IR 8467 Second Public Draft,
> published in December 2024, and the official publication/project pages still
> display draft/reviewing-comments status as of 2026-07-12.
> **Claim status:** active
> **Scope:** Version and current official presentation of this publication,
> not a conclusion about future finalization or adoption.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local PDF, cover and title pages, PDF pp. 1–3; official CSRC
> publication record and NCCoE project page, accessed 2026-07-12.
> **Basis / limits:** Draft label, DOI and publication date are direct. Web
> state can change and must be reviewed; absence of a final on these official
> pages is not proof that no other later artifact can ever exist.

> **Claim record — SRC-0006-C02 | source-report**
> **Claim:** The profile applies to assets processing human, microbiome,
> microbial, model-organism or plant genomic data, emphasizes privacy outcomes
> for human processing, and models five phases: sample collection, sample
> preparation, data generation, data analysis and data disposition.
> **Claim status:** active
> **Scope:** Profile scope and high-level lifecycle, not a universal laboratory,
> clinical or biobank chain of identity/custody.
> **As of:** 2024-12-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §1.2–§1.3 and Figure 1, printed pp. 4–5
> (PDF pp. 15–16).
> **Basis / limits:** Data types, audience and stage labels are explicit and
> Figure 1 was visually verified. The profile scope centers on generated and
> derived data; it does not validate sample custody, identity linkage,
> consent propagation, disposal proof or an implemented end-to-end lineage.

> **Claim record — SRC-0006-C03 | source-report**
> **Claim:** IR 8467 distinguishes cybersecurity incidents involving
> confidentiality, integrity or availability from privacy events caused by
> data processing, and states that permitted processing can create privacy
> problems even when cybersecurity risk management operates as intended.
> **Claim status:** active
> **Scope:** Conceptual cyber/privacy distinction for genomic-data processing.
> **As of:** 2024-12-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§2.1–2.2.1 and Figures 2–3, printed pp. 9–11
> (PDF pp. 20–22).
> **Basis / limits:** The distinct and overlapping pathways are direct. Figure
> 3 presents potential individual harms and organizational impacts, not an
> observed incident sequence, frequency estimate or causal validation.

> **Claim record — SRC-0006-C04 | source-report**
> **Claim:** From October 2022 through February 2023, stakeholders developed
> and prioritized Mission Objectives and CSF 1.1 Categories; later privacy
> sessions prioritized PF Categories, and NCCoE experts translated the inputs
> into Subcategory priorities and migrated the cyber portion to CSF 2.0 using a
> crosswalk.
> **Claim status:** active
> **Scope:** Profile-development process as reported by NIST; not a
> representative survey or direct vote on every CSF 2.0/PF 1.0 outcome.
> **As of:** 2024-12-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §4, printed p. 20 (PDF p. 31).
> **Basis / limits:** Dates, participant-sector categories and transformation
> steps are direct. The document gives no participant count, sampling frame,
> sector distribution, response rate, raw vote data, weighting or aggregation
> rule, consensus threshold, dissent record, inter-rater analysis or empirical
> validation. `Garnered consensus` is therefore not treated as a formal
> consensus method.

> **Claim record — SRC-0006-C05 | source-report**
> **Claim:** The profile ranks 12 Mission Objectives: provenance/data quality;
> relatives' privacy; cyber/privacy risk; consent; donor privacy; authorized
> access; trust/reputation; research/education; legal compliance; intellectual
> property; fit-for-purpose diversity; and privacy-enhancing/secure sharing
> technologies.
> **Claim status:** active
> **Scope:** Informative profile priorities that organizations may add,
> remove, reorder or deconstruct, not a universal risk ranking.
> **As of:** 2024-12-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Table 3 and §§5.1–5.12, printed pp. 21–28
> (PDF pp. 32–39); workbook `Mission Objectives` sheet.
> **Basis / limits:** Names and order are explicit. The priorities do not
> quantify likelihood, consequence, maturity, control strength or benefit.

> **Claim record — SRC-0006-C06 | source-report**
> **Claim:** The PDF and official spreadsheet assign priorities for 106 CSF
> 2.0 and 100 PF 1.0 outcomes across the 12 Mission Objectives, where `1` is
> High, `2` Moderate and `3` Other; `Other` is not low, and organizations are
> expected to tailor Current and Target Profiles to their own context.
> **Claim status:** active
> **Scope:** Structure and intended use of the draft matrix, not implementation,
> compliance, risk score or control-effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §3.2–§3.3, printed pp. 16–19 (PDF pp. 27–30);
> §6 and Figure 4, printed pp. 29–31 (PDF pp. 40–42); Tables 4–36,
> printed pp. 32–166 (PDF pp. 43–177); workbook `User Guide` and
> `Integrated CSF 2.0 & PF Profile` sheets.
> **Basis / limits:** Counts, values and tailoring instructions were checked
> across both artifacts. The CSF↔PF alignment is described as draft and planned
> for update with PF 1.1. A priority cell is not evidence that an organization
> implemented, tested or benefited from the outcome.

> **Claim record — SRC-0006-C07 | source-report**
> **Claim:** Mission Objective 1 defines provenance broadly across data origin,
> custody changes, annotations, derived data, data/software versions,
> configurations and analysis parameters, and treats trustworthy,
> fit-for-purpose data as a prerequisite for reliable research, products and
> decisions.
> **Claim status:** active
> **Scope:** Draft target-state provenance and data-quality objective, not a
> validated provenance implementation or observed failure path.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §5.1, printed pp. 22–23 (PDF pp. 33–34);
> Appendix C `Provenance`, printed p. 174 (PDF p. 185); Tables 10–12,
> printed pp. 64–90 (PDF pp. 75–101).
> **Basis / limits:** Scope and rationale are explicit. The document recommends
> inventories, mapping, assessment and improvement outcomes but supplies no
> completeness metric, implementation record, error rate or decision-outcome
> validation.

> **Claim record — SRC-0006-C08 | source-report**
> **Claim:** The profile treats donor and relative privacy as distinct Mission
> Objectives, recommends that consent context remain synchronized with data
> across changing processing and partners, and separates authorized technical
> access from permitted processing under consent and purpose constraints.
> **Claim status:** active
> **Scope:** Human genomic-data privacy target state; relatives often cannot
> provide the donor's consent, and legal rights/duties remain context-specific.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§5.2, 5.4–5.6, printed pp. 23–25
> (PDF pp. 34–36); Tables 10, 13, 26 and 32–36, printed
> pp. 64–77, 91–97 and 141–166 (PDF pp. 75–88, 102–108,
> 152–177).
> **Basis / limits:** Objectives and rationales are direct recommendations.
> The source does not validate a consent schema, demonstrate propagation or
> establish a universal deletion, notification or re-consent duty.

> **Claim record — SRC-0006-C09 | source-report**
> **Claim:** The profile recommends organization-specific inventories and
> mappings of genomic data, metadata, hardware, software, services, owners,
> locations, processing actions, purposes, flows, dependencies and third-party
> roles throughout the lifecycle.
> **Claim status:** active
> **Scope:** Desired governance/system outcomes for a genomic-data processing
> ecosystem, not a reference architecture or deployment census.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Tables 4, 9–11 and 26–29, printed pp. 32–38,
> 57–85 and 141–146 (PDF pp. 43–49, 68–96 and 152–157).
> **Basis / limits:** Outcome text and rationales are direct. Remote access,
> supplier and cloud examples do not establish exposure, prevalence, topology,
> privilege, vulnerability or a control implementation in a named system.

> **Claim record — SRC-0006-C10 | source-report**
> **Claim:** Tables 4–36 recommend governance, inventory, risk assessment,
> access, data/platform protection, monitoring, incident response, recovery and
> privacy-management outcomes, including assessment, exercises and restored-
> state verification, but report no implementation or evaluation results.
> **Claim status:** active
> **Scope:** Recommended draft outcome set and its evidence classification.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §6 and Tables 4–36, printed pp. 29–166
> (PDF pp. 40–177); workbook integrated and high-priority sheets.
> **Basis / limits:** The document recommends tests, assessments, supplier
> evidence, exercises, monitoring, backup integrity and recovery verification.
> Statements such as `effective`, `testing assures` or `independent assessment`
> are desired rationales, not findings. No deployed organization, test method,
> result, detection rate, residual risk, measured outcome or independent
> evaluation is reported.

> **Claim record — SRC-0006-C11 | analytic-judgment**
> **Claim:** IR 8467 2pd is a follow-on output of the same NIST/NCCoE genomics
> programme as IR 8432: it turns the earlier cybersecurity-profile work and
> planned privacy profile into an integrated CSF 2.0/PF 1.0 draft, without
> superseding IR 8432 or forming an independent evidence lineage for risk or
> effectiveness claims.
> **Claim status:** active
> **Scope:** Corpus reconciliation between `SRC-0005` and `SRC-0006`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0005](src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §5.1–§5.2, printed pp. 23–25 (PDF pp. 32–34); local IR 8467 PDF,
> §§1 and 4, printed pp. 1–6, 20–21 (PDF pp. 12–17, 31–32);
> overlapping programme, workshops and authorship.
> **Basis / limits:** Publication progression and shared programme lineage are
> direct; the non-independence conclusion is a conservative wiki judgment.
> IR 8467 adds later privacy sessions and CSF 2.0 analysis, so it is not merely
> duplicate text.

> **Claim record — SRC-0006-C12 | artifact-observation**
> **Claim:** The preserved package has production inconsistencies: a different
> title in the suggested citation, a broken Table 4 bookmark, `Medium` versus
> `Moderate` terminology, acronym defects, an authoring-path remnant in workbook
> metadata, and one High Priority Summary row that labels MO 12's `GV.OC-03`
> legal-requirements content as `GV.OV-03`.
> **Claim status:** active
> **Scope:** Internal integrity of the local PDF/XLSX package; not a rejection
> of the remaining profile matrix.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF suggested citation, unnumbered PDF p. 3; List of Tables,
> printed p. v (PDF p. 9); §6 and Figure 4, printed pp. 29–31
> (PDF pp. 40–42); Appendix B, printed pp. 171–173
> (PDF pp. 182–184); workbook metadata and `High Priority Summaries`
> row 321 compared with integrated-profile rows for `GV.OC-03` and `GV.OV-03`.
> **Basis / limits:** Direct artifact comparison supports each inconsistency.
> The erroneous summary row's text and priority match `GV.OC-03`, whereas
> actual `GV.OV-03` has a different description and MO 12 priority `2`.
> Canonical identifiers and primary table rows take precedence over the summary
> typo; no other spreadsheet row is inferred invalid from this check.

## Scope and methods

### Source scope

- Organizations processing genomic data, including sequencing providers,
  genome centers, clinical laboratories, healthcare, direct-to-consumer
  testing, technology developers, cloud providers, researchers, repositories
  and other ecosystem participants.
- Human and non-human genomic data; privacy objectives are not automatically
  transferred to non-human data.
- Generated sequence/other data and derived analytic data are central; privacy
  processes can begin before sample collection and inform later phases.
- Integrated CSF 2.0/PF 1.0 outcomes used to construct context-specific Current
  and Target Profiles. Implementation Tiers are outside scope.

### Development method

NCCoE reports virtual working sessions across government, academia, nonprofit
and industry participants. Earlier sessions ranked Mission Objectives and CSF
1.1 Categories; later privacy sessions reviewed objectives and prioritized PF
Categories. NCCoE experts derived Subcategory priorities and used a CSF
1.1-to-2.0 crosswalk after CSF 2.0 publication. The document calls the result
consensus-informed but does not disclose the data needed to evaluate formal
consensus, representativeness or reliability.

### Matrix semantics

`1/2/3` expresses suggested sequence of attention under resource constraints.
It is not a likelihood, severity, maturity, compliance, assurance or control-
effectiveness scale. All outcomes remain candidates; `Other` is explicitly not
`low`. Workbook formulas filter and summarize the static matrix but do not add
empirical evidence.

## Limitations and conflicts

- Second Public Draft; public comments are closed but disposition and final
  content are not shown on the preserved official pages.
- PF version is 1.0 and the CSF↔PF alignment is itself labeled draft; the source
  anticipates update with PF 1.1.
- No participant count, recruitment/sampling method, raw responses, scoring
  rule, disagreement analysis or formal validation.
- Stakeholders did not directly score all 106 CSF 2.0 Subcategories; NCCoE
  transformed earlier category-level input.
- No representative organization sample, reference deployment, implementation
  census, assessment result, control test, outcome study or independent
  evaluation.
- Legal and regulatory examples are dated/context-specific references, not a
  current cross-jurisdictional legal analysis. Applicability must be checked
  from current primary law.
- Framework and control rationales sometimes use categorical future tense or
  words such as `effective`; these are target-state language, not observed
  facts.
- IR 8432 and IR 8467 share programme, workshop and author lineage. The later
  profile improves specificity but does not independently corroborate an
  incident, threat prevalence, control deployment or effect.
- Spreadsheet summary typo and PDF production defects require canonical-row
  reconciliation. The integrated sheet's priority values were internally
  consistent across duplicate directional rows; rationales can differ by
  crosswalk direction.
- Workbook XML and cached formula values were inspected without executing or
  recalculating formulas. High-priority membership matched the integrated
  matrix for 11 objectives and exposed the single MO 12 identifier defect
  documented above; this is an artifact consistency check, not software QA.

## Version status

Official CSRC history lists a June 2023 draft and this December 2024 Second
Public Draft. As of the 2026-07-12 review, CSRC still labels the publication
`2nd Public Draft` and NCCoE reports `Reviewing Comments`; no final is displayed
on those official pages. Review by 2026-10-10 or sooner if NIST publishes a
replacement. Do not label this artifact final, current binding baseline or
adopted requirement.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
  — reuses genomic provenance, IP, donor/relative and authorized-use classes
  alongside an independent NASEM biological-AI asset line.
- [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
  — reuses version/context, access, monitoring, response and recovery target
  states in a biological-AI control reconciliation; draft status and absent
  implementation/effectiveness remain explicit.

- [AST-0001](../assets/ast-0001-genomic-data.md) — expanded data examples and clear
  human/non-human privacy scope.
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — explicit fifth
  disposition phase and target-state provenance/consent propagation.
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) — roles,
  asset/data inventories, flows and dependencies without reference-architecture
  inference.
- [RSK-0003](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md) —
  provenance/data-quality interruption points; scenario remains hypothetical.
- [RSK-0004](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md) —
  disclosure/access-boundary pathway affecting donor and relative privacy.
- [RSK-0005](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md) —
  distinct privacy-problem path from technically authorized processing without
  a required cybersecurity incident or disclosure.
- [CTL-0002](../controls/ctl-0002-genomic-data-risk-management.md) — versioned CSF
  2.0/PF 1.0 Community Profile mapping; recommended/draft, with implementation,
  testing, effectiveness and independent evaluation unknown.
- [CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md) — uses the
  profile's provenance, integrity, monitoring and recovery outcomes as one
  independent normative lineage for reverse-path safeguards; no implementation
  or effectiveness is inferred.
- This source alone still does not justify an `INC`, `THR`, `TEC` or `VUL`
  page. Later `SRC-0014` independently supports safe reverse-path entities;
  [SYN-0003](../syntheses/syn-0003-cross-domain-transfer-directions.md) reconciles
  them with the NIST genomic threat/integrity lineage without making NIST a
  second observation of the USENIX experiment.
- [SYN-0006](../syntheses/syn-0006-official-control-function-state-taxonomy.md)
  reconciles NIST functions and profile evidence state with independent FDA
  and WHO lineages without treating draft priorities as implementation.
- [SYN-0008](../syntheses/syn-0008-global-us-eu-uk-canada-governance-reconciliation.md)
  preserves Community Profile as an instrument form and Second Public Draft as
  a distinct lifecycle state in the canonical governance matrix.
- [SYN-0018](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
  uses this profile together with IR 8432 as one NIST programme lineage for
  biological-AI assets and exact-edge controls; draft recommendations are not
  implementation or effectiveness evidence.
- [SYN-0020](../syntheses/syn-0020-foundational-cross-sector-assets-lifecycle-governance-reconciliation.md)
  uses this profile as the genomic and public-draft exemplar in cross-sector
  asset/lifecycle/governance reconciliation without inferring implementation.
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)
