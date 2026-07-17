---
id: SYN-0010
type: synthesis
title: Laboratory and biobank scope, asset and lifecycle reconciliation
aliases:
  - LAB-ST AS WL reconciliation
  - research diagnostic HCL biobank matrix
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-11
source_ids:
  - SRC-0002
  - SRC-0004
  - SRC-0018
  - SRC-0019
  - SRC-0022
sensitivity: public
dual_use: low
jurisdictions:
  - Global
  - United States
  - Canada
relations:
  - predicate: evidenced-by
    target: SRC-0002
    claim_id: SYN-0010-C01
    evidence:
      - source: SRC-0002
        locator: "Introduction; Methods—Asset-impact analysis; Cyber elements of high-containment laboratories/research laboratories/diagnostic laboratories/high-containment biomanufacturing facilities; Figure 2"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYN-0010-C01
    evidence:
      - source: SRC-0004
        locator: "Glossary, printed pp. xiii–xv/PDF pp. 15–17; §§1.1–1.2, printed pp. 2–3/PDF pp. 22–23; §§5–7, printed pp. 19–44/PDF pp. 39–64"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: SYN-0010-C01
    evidence:
      - source: SRC-0019
        locator: "Chapter 1 and §§1.1–1.2.4, printed pp. 2–5/PDF pp. 34–37; §4.1, printed pp. 52–57/PDF pp. 84–89; Chapter 5, printed pp. 102–121/PDF pp. 134–153"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: SYN-0010-C01
    evidence:
      - source: SRC-0022
        locator: "Introduction and §§A.1–A.3, printed pp. 1–3/physical pp. 4–6; §§B.1–B.12.3, printed pp. 4–34/physical pp. 7–37; §§C.1–C.6.6, printed pp. 35–70/physical pp. 38–73"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYN-0010-C05
    evidence:
      - source: SRC-0018
        locator: "§§2.3.5–2.3.7, printed pp. 22–26/PDF pp. 39–43; §§5.3–5.4, printed pp. 69–89/PDF pp. 86–106; §§6.2.1/6.3–6.5, printed pp. 97–108, 126–138/PDF pp. 114–125, 143–155"
tags:
  - laboratory
  - biobank
  - reconciliation
  - research-laboratory
  - diagnostic-laboratory
  - high-containment
  - assets
  - lifecycle
  - evidence-quality
---

# Laboratory and biobank scope, asset and lifecycle reconciliation

## Question, cutoff and independence

This synthesis tests only the frozen `LAB-ST`, `LAB-AS` and `LAB-WL` criteria
after complete `SRC-0022` integration. Cutoff is 2026-07-12.

The acceptance-bearing lineages are materially independent:

- NCI 2026 is U.S. voluntary human-research biospecimen-resource guidance;
- WHO 2024 is global normative laboratory-biosecurity guidance;
- Canadian CBS is a national standard with scoped licence/permit force;
- Crawford et al. is an academic qualitative HCL model.

WHO cites Crawford for part of its cyber context, so those two do not count as
independent empirical cyberarchitecture evidence. The three cells here instead
rest on direct NCI biobank and WHO/CBS scope/lifecycle/actor evidence; Crawford
adds class terminology/context rather than manufacturing an SF2 floor.

> **Claim record — SYN-0010-C01 | analytic-judgment**
> **Claim:** The represented NCI, WHO and Canadian lineages are materially
> independent and claim-appropriate for laboratory/biobank scope, asset and
> lifecycle reconciliation, with NCI voluntary research guidance, WHO global
> guidance and CBS scoped national-standard force kept non-equivalent.
> **Claim status:** active
> **Scope:** SF2 provenance/modality for `LAB-ST/AS/WL`; not independence for
> an incident, system implementation, audit or effectiveness outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> cover/Introduction/§§A.1–A.3, physical pp. 1, 4–6;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> official identity/§§1.1–1.2, PDF pp. 4, 21–23;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> Preface/Figure 1 and §§1.1–1.2.4, PDF pp. 6–7, 34–37;
> [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> bibliographic identity/§ Methods — Asset-impact analysis/§ Cyber elements
> of high-containment laboratories; `SRC-0002-C01/C02/C07`.
> **Basis / limits:** Issuers, genres, force and source-development contexts are
> distinct. Shared citations are not double-counted for empirical claims.

## Laboratory/biobank scope and rule matrix

| Frozen class | Direct represented scope | Where rules/evidence differ |
| --- | --- | --- |
| Research laboratory | WHO includes research settings across material stages; CBS covers research facilities when regulated material/activity facts apply; Crawford models research HCL; NCI covers research specimens/resources | WHO/NCI are nonbinding guidance; CBS force is licence/permit-scoped; research laboratory is not automatically a biobank or HCL |
| Diagnostic laboratory | WHO includes diagnostic settings; CBS contains diagnostic exclusions/exemptions and applicable regulated-facility rules; Crawford models diagnostic HCL | diagnostic handling/reporting differs from NCI's research-resource purpose; an exclusion from CBS licensing is not absence of other obligations |
| High-containment laboratory | Crawford's primary analytical scope plus WHO high-consequence laboratory governance and CBS containment/programme/test requirements | Crawford is qualitative, WHO advisory and CBS jurisdiction/applicability-specific; none proves facility implementation |
| Biobank/repository | NCI directly defines human research biospecimen resource as material+data+storage structure+processes/policies and equates the broad class with biobank/biorepository | NCI is voluntary human-research guidance, not diagnostic/HCL/accreditation law; WHO/CBS do not independently create a distinct general biobank class |
| Cross-class exclusions | NCI separates detailed procedures/post-mortem work; WHO is risk/context tailored; CBS records material/activity exclusions and separate aquatic/plant regimes | current accreditation, non-human repositories and detailed diagnostic/clinical rules require separate sources |

> **Claim record — SYN-0010-C02 | analytic-judgment**
> **Claim:** The matrix satisfies `LAB-ST` at SF2 by distinguishing research,
> diagnostic, high-containment and biobank/repository classes and directly
> reconciling their purpose, force, applicability and exclusion differences.
> **Claim status:** active
> **Scope:** Frozen `LAB-ST` criterion in represented global/U.S./Canadian
> contexts; not a universal laboratory taxonomy or accreditation reconciliation.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> Introduction/§§A.1–A.3, printed pp. 1–3/physical pp. 4–6;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2, printed pp. 2–3/PDF pp. 22–23;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> Chapter 1/§§1.1–1.2.4, PDF pp. 34–37; `SRC-0019-C04/C09`;
> [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Introduction/Methods/HCL, research, diagnostic and biomanufacturing sections;
> `SRC-0002-C01/C02`.
> **Basis / limits:** Every required class and difference is direct across
> independent lineages. Class coverage is not implementation or equivalence.

## Asset/stakeholder acceptance

`AST-0005` supplies one canonical matrix with every frozen row: specimens/
material; strains/cells/reagents; metadata/consent/provenance; instruments/
facility; identities/credentials; workers; donors/patients; communities/public.
It separates material, digital, physical and authorization states and records
where NCI human-research scope differs from WHO/CBS laboratory scope.

> **Claim record — SYN-0010-C03 | analytic-judgment**
> **Claim:** `AST-0005-C01/C02` satisfies `LAB-AS` at SF2 by directly covering
> all required asset and stakeholder classes across independent NCI and
> WHO/CBS lineages, with no inventory, role execution or legal equivalence
> inferred.
> **Claim status:** active
> **Scope:** Frozen `LAB-AS` class-level criterion; not system architecture,
> facility implementation, incident or asset-value completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md),
> `AST-0005-C01`–`C04`; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§A.1/B.1–B.5.1.3/C.1.2–C.1.5/C.2.6/C.3.2/C.5–C.6, printed
> pp. 3–11, 35–40, 50, 57–59, 62–70/physical pp. 6–14, 38–43, 53,
> 60–62, 65–73; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> glossary/§§1.1–1.2/5.1/6.3, PDF pp. 15–17, 22–23, 40, 51;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> Chapter 1/§4.1, PDF pp. 34–37, 84–89.
> **Basis / limits:** Matrix rows and source-specific boundaries are explicit.
> Canonical grouping is editorial and does not imply shared ownership/force.

## Lifecycle acceptance

`WFL-0009` maps parallel physical-material, data/consent and identity/custody/
quality lanes through planning, collection/receipt, bounded accession,
processing, inventory/storage, retrieve/use/share, transfer/transport,
deviation/incident, closeout/disposition and review/learning. `Accession` is
explicitly normalized as receipt/acquisition + unique ID + inventory entry,
not falsely quoted as an NCI stage.

> **Claim record — SYN-0010-C04 | analytic-judgment**
> **Claim:** `WFL-0009-C01/C04` satisfies `LAB-WL` at SF2 by directly covering
> collection/receipt, bounded accession, processing, inventory/storage,
> use/share/transport, closeout/disposal and incident learning across
> independent NCI and WHO/CBS lineages.
> **Claim status:** active
> **Scope:** Frozen `LAB-WL` functional criterion; not a universal operating
> sequence, completed incident loop or performance finding.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [WFL-0009](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md),
> `WFL-0009-C01`–`C04`; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.12.3 (including B.12.1.1–B.12.1.4), C.2–C.3.3 and C.5–C.6.6,
> printed pp. 4–34, 41–70/physical pp. 7–37, 44–73;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2/5–6.6 and Annex 2, PDF pp. 22–23, 39–59, 98–102;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §4.1/Chapter 5, PDF pp. 84–89, 134–153.
> **Basis / limits:** Every stage is located and accession normalization is
> explicit. Normative learning loops are not incident/result evidence.

## Strict residual-cell audit

| LAB cell | State after SRC-0022 | Why no new Pass |
| --- | --- | --- |
| `LAB-SD` | Partial | `SYS-0007` now covers LIMS, instruments, storage/freezers, building/containment, cloud/backup, identity and validation design, but no direct ELN class is ingested |
| `LAB-TV` | Partial | NCI/WHO/CBS add accidental, environmental, inventory, continuity and insider/control concerns, but no complete malicious/insider/accidental/environmental/supply plus vulnerability/exposure corpus at SF2 is reconciled |
| `LAB-XT` | Partial | lifecycle/boundary structure is not a full cyber→containment/sample/result and material/custody→LIMS/decision scenario pair at SF2 |
| `LAB-CI` | Partial | no primary incident with laboratory/biobank biological, safety, privacy or continuity outcome plus independent corroboration is added |
| `LAB-CT` | **Pass, unchanged** | existing `SYN-0007-C03` already satisfies the exact-edge criterion; new design detail is not a second point |
| `LAB-AE` | Partial | audits, tests, drills and validation are prescribed, but no deployed safeguard with scoped completed metric and independent evaluation is added |
| `LAB-GR` | Partial | NCI is voluntary best-practices guidance, not current accreditation; the companion CAP checklist is excluded and WHO/CBS/NCI do not complete current accreditation/adoption reconciliation |

> **Claim record — SYN-0010-C05 | analytic-judgment**
> **Claim:** Only `LAB-ST/AS/WL` change to Pass; `LAB-SD/TV/XT/CI/AE/GR`
> remain Partial and existing `LAB-CT` remains Pass because source scope,
> design and structure cannot substitute for ELN, scenarios, incidents,
> completed assurance or current accreditation evidence.
> **Claim status:** active
> **Scope:** Frozen LAB evidence sufficiency immediately after SRC-0022;
> Partial means incomplete in this corpus, not absent from real laboratories.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0010-C01`–`C04`;
> [SYS-0007](../systems/sys-0007-biobank-informatics-storage-ecosystem.md),
> `SYS-0007-C01`–`C04`; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> `SRC-0022-C07`–`C12`, §§C.1.6/C.3/C.6, printed pp. 40–41, 57–61,
> 64–70/physical pp. 43–44, 60–64, 67–73;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.5–2.3.7/5.3–5.4/6.2.1/6.3–6.5, PDF pp. 39–43, 86–106,
> 114–125, 143–155; frozen LAB criteria in `SYN-0001`.
> **Basis / limits:** Each missing predicate is named. Adjacent normative or
> architectural evidence is not promoted by analogy.

## Score delta

> **Claim record — SYN-0010-C06 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `LAB-ST`, `LAB-AS` and
> `LAB-WL` as Partial→Pass, raising Laboratories/Biobanks from 1/10 to
> 4/10 and the overall score from 25/110 to 28/110 (25.5%), with 28 Pass, 76
> Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after complete SRC-0022 integration and frozen
> rubric v1.0; not absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0010-C01`–`C05`; prior `SYN-0001-C15` checkpoint at 25 Pass/
> 79 Partial/6 Absent; frozen `LAB-ST/AS/WL` criteria and score method in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Three literal transitions produce the arithmetic;
> independent content, locator, relation and binary-score review passed on
> 2026-07-12.

## Safety boundary

The synthesis retains class-level scope, assets, lifecycle and defensive
boundaries only. It omits material identities, patient records, facility
topology, storage/containment settings, access secrets and operational
procedures.

## Related pages

- [SRC-0022 — NCI Best Practices](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [GOV-0012 — NCI governance](../governance/gov-0012-nci-best-practices-biospecimen-resources-2026.md)
- [AST-0005 — assets/stakeholders](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [WFL-0009 — lifecycle](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md)
- [SYS-0007 — system map](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SYN-0011 — system-boundary reconciliation](syn-0011-laboratory-biobank-system-boundary-reconciliation.md)
- [SRC-0024 — current ISO biobanking-standard status](../sources/src-0024-iso-20387-biobanking-standard-current-status.md)
- [GOV-0014 — ISO 20387 governance](../governance/gov-0014-iso-20387-biobanking-standard.md)
- [SYN-0012 — governance reconciliation](syn-0012-global-canada-us-laboratory-biobank-governance-reconciliation.md)
- [WFL-0004 — high-consequence material lifecycle](../workflows/wfl-0004-high-consequence-material-lifecycle.md)
- [SYS-0001 — HCL support systems](../systems/sys-0001-hcl-containment-support-systems.md)
- [GOV-0001 — WHO laboratory governance](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [GOV-0009 — Canadian CBS governance](../governance/gov-0009-canadian-biosafety-standard-third-edition.md)
- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)
- [SYN-0007 — existing LAB-CT acceptance](syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
