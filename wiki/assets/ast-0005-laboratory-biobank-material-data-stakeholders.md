---
id: AST-0005
type: asset
title: Laboratory and biobank material, data and stakeholder map
aliases:
  - laboratory biobank asset map
  - biospecimen resource assets and stakeholders
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0004
  - SRC-0019
  - SRC-0022
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: AST-0005-C01
    evidence:
      - source: SRC-0004
        locator: "Glossary, printed pp. xiii–xv/physical PDF pp. 15–17; §§1.1–1.2, printed pp. 2–3/PDF pp. 22–23; §5.1, printed p. 20/PDF p. 40; §6.3, printed p. 31/PDF p. 51; §§5.3.4 and 6.5, printed pp. 21–22 and 34–37/PDF pp. 41–42 and 54–57"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: AST-0005-C01
    evidence:
      - source: SRC-0019
        locator: "Chapter 1 and §§1.1–1.2.3, printed pp. 2–4/physical PDF pp. 34–36; §4.1, printed pp. 52–57/PDF pp. 84–89"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: AST-0005-C01
    evidence:
      - source: SRC-0022
        locator: "§§A.1–A.2, printed p. 3/physical p. 6; §§B.1–B.4, printed pp. 4–8/physical pp. 7–11; §B.5.1.3, printed p. 11/physical p. 14; §§C.1.2–C.1.5, printed pp. 35–40/physical pp. 38–43; §§C.2.6/C.2.8/C.3.2/C.5–C.6, printed pp. 50–54, 57–59, 62–70/physical pp. 53–57, 60–62, 65–73"
tags:
  - laboratory
  - biobank
  - biospecimen
  - assets
  - stakeholders
  - metadata
  - identity
  - public-interest
---

# Laboratory and biobank material, data and stakeholder map

## Scope and reconciliation method

This page joins three independent official lineages at the class level:

- WHO 2024 covers laboratory material/information, personnel, institutions,
  national authorities and community/public interests;
- Canadian CBS covers regulated human/terrestrial-animal material/facilities,
  licence/permit holders, management, BSO, personnel and regulators;
- NCI 2026 covers human research specimens/derivatives, associated data,
  consent/provenance, biobank infrastructure/informatics and donors/patients,
  researchers, providers, communities and public interests.

The map is not an inventory. It contains no material identity, sample record,
person, credential secret, facility location or operational setting.

## Canonical asset and stakeholder matrix

| Frozen class | Reconciled class | Direct evidence and boundary |
| --- | --- | --- |
| Specimens/material | human research biospecimens and derivatives; laboratory biological material; separately bounded regulated pathogen/toxin material | NCI §§A.1/C.2/C.6; WHO §§1.1–1.2; CBS Chapter 1. Scope classes do not make every biospecimen CBS-regulated |
| Strains/cell lines/reagents | laboratory biological-agent/derivative classes plus human-cell/sample, literal cell-line and fit-for-purpose reagent/supply classes | WHO glossary/§§1–2; NCI §B.5.1.3 and §§C.2.6/C.3.2. No strain, cell-line or reagent inventory is inferred |
| Metadata and consent/provenance | identifiers, participant consent/permissions, collection/processing/storage annotations, clinical/research metadata, custody/audit state | NCI §§B.1–B.8/C.5–C.6; WHO inventory/accountability. Associated data are not equated with the material |
| Instruments and facility | laboratory/biobank instruments, storage, physical resource structure, connected equipment and building/support systems | NCI §§A.1/C.1.4–C.1.5/C.2.8; WHO §6.5; CBS regulated-facility scope. No topology or specific device is asserted |
| Credentials and identities | user identity, role/project authorization, access/audit identity, licence/permit-holder and assigned institutional roles | NCI §§C.6.1.4–C.6.1.5; CBS §§1.2/4.1. Credentials mean access/role state, not passwords or clearance rules |
| Workers | laboratory/biobank personnel, technicians, managers, data/quality/biosafety staff and institutional support | NCI §C.1.2; WHO §§4–8; CBS §4.1. Recommended/required roles are not evidence of staffing |
| Donors/patients | research participants/specimen contributors, patients and providers with consent/privacy/return-of-results interests | NCI §§B.1–B.8. This human-research limb is not supplied by WHO/CBS alone |
| Public and communities | participant communities, patient advocates, affected community/general public and public-health/environmental interests | NCI §§B.1–B.4; WHO/CBS protected/affected interests. Interests are not manufactured into universal legal rights |

> **Claim record — AST-0005-C01 | analytic-judgment**
> **Claim:** The reconciled map covers every frozen `LAB-AS` asset class—
> specimens/material, strains/cells/reagents, metadata, instruments/facility and
> identities/credentials—without merging biological, physical, digital and
> authorization states.
> **Claim status:** active
> **Scope:** Class-level laboratory/biobank map across represented WHO, Canadian
> and NCI contexts; not a complete inventory, topology or applicability ruling.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> glossary and §§1.1–1.2/5.1/5.3.4/6.3/6.5, PDF pp. 15–17, 22–23,
> 40–42, 51, 54–57;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> Chapter 1/§§1.1–1.2.3 and §4.1, PDF pp. 34–36, 84–89;
> [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§A.1–A.2, B.1–B.4, B.5.1.3, C.1.2–C.1.5, C.2.6, C.3.2 and C.5–C.6,
> printed pp. 3–8, 11, 35–40, 50, 57–59, 62–70/physical pp. 6–11, 14,
> 38–43, 53, 60–62, 65–73; `SRC-0022-C03/C04/C07/C08`.
> **Basis / limits:** Each class is directly located, while the canonical
> separations are editorial. Similar words do not imply shared regulation.

> **Claim record — AST-0005-C02 | analytic-judgment**
> **Claim:** The map also covers the frozen stakeholder set—workers,
> donors/patients and public—together with custodians/stewards, researchers,
> providers, institutions, review bodies and national regulators.
> **Claim status:** active
> **Scope:** Actor/affected-interest classes, not universal rights, complete
> responsibility allocation, participation quality or observed role execution.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.4, printed pp. 4–8/physical pp. 7–11; §C.1.2, printed pp. 35–37/
> physical pp. 38–40; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§4–4.3.2 and 8.1–8.1.5, printed pp. 12–18, 45–51/PDF pp. 32–38,
> 65–71; [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §§1.2.1–1.2.3/4.1, PDF pp. 36–37, 84–89.
> **Basis / limits:** Required classes are direct across independent official
> contexts. Legal duties and recommendations remain differentiated.

## Asset-state and boundary model

| Boundary | Trustworthy state | What remains unestablished |
| --- | --- | --- |
| material ↔ identifier | unique, durable, non-identifying label remains linked to the correct specimen/derivative and history | no implementation error rate or universal identifier scheme |
| material ↔ associated data | consent/provenance, preanalytical history and clinical/research annotation remain correctly associated | no patient-level record or completeness metric |
| physical location ↔ inventory | recorded storage/transfer state matches the controlled physical item | no actual location, facility map or completed reconciliation result |
| identity/role ↔ access | authorized role/project and material/data purpose govern access and leave an attributable audit state | no credential value, clearance procedure or adoption proof |
| donor/community ↔ governance | permitted use, withdrawal limits, privacy and communication follow documented governance/consent | no universal right or guarantee that shared data can be recalled |
| worker/public ↔ continuity/safety | workers and affected interests remain protected when material/data/equipment fail or change | no incident/outcome or control-effectiveness measure |

> **Claim record — AST-0005-C03 | analytic-judgment**
> **Claim:** Material↔identifier↔data↔location↔authorized-user boundaries are
> distinct dependencies, so a trustworthy digital record does not by itself
> establish material quality, lawful use, physical custody or safety.
> **Claim status:** active
> **Scope:** Defensive asset-state model derived from the mapped sources; not a
> causal incident path or assertion that every resource uses one architecture.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.12 and C.2/C.5/C.6, printed pp. 4–34, 41–57, 62–70/physical
> pp. 7–37, 44–60, 65–73; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5–6, printed pp. 19–39/PDF pp. 39–59.
> **Basis / limits:** Sources distinguish these states and controls. The
> boundary model is an editorial synthesis and supplies no observed failure.

## Evidence and acceptance boundary

The matrix meets the literal `LAB-AS` class list at SF2, subject to independent
binary review in `SYN-0010`. It does not close system architecture (`LAB-SD`),
incident (`LAB-CI`) or effectiveness (`LAB-AE`) merely because the assets and
stakeholders are now mapped.

> **Claim record — AST-0005-C04 | artifact-observation**
> **Claim:** `AST-0005` is structurally complete for the `LAB-AS` class list but
> is not implementation, incident, system-validation or effectiveness evidence.
> **Claim status:** active
> **Scope:** Wiki map sufficiency after SRC-0022; final Pass remains subject to
> `SYN-0010` and independent frozen-rubric review.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `AST-0005-C01`–`C03`; frozen `LAB-AS/SD/CI/AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Required rows are explicit and residual evidence states
> are separated. Page structure cannot substitute for external results.

## Related pages

- [SRC-0022 — NCI Best Practices](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [GOV-0012 — NCI governance](../governance/gov-0012-nci-best-practices-biospecimen-resources-2026.md)
- [WFL-0009 — material/data lifecycle](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md)
- [SYS-0007 — informatics/storage system](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SYN-0010 — laboratory/biobank reconciliation](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [WFL-0004 — high-consequence material lifecycle](../workflows/wfl-0004-high-consequence-material-lifecycle.md)
- [SYS-0001 — HCL support systems](../systems/sys-0001-hcl-containment-support-systems.md)
- [THR-0005 — laboratory intentional threat classes](../threats/thr-0005-laboratory-malicious-insider-and-supply-actions.md)
- [HAZ-0006 — laboratory non-adversarial hazards](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
