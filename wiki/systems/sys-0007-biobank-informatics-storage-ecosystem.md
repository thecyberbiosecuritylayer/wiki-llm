---
id: SYS-0007
type: system
title: Biobank informatics, storage and laboratory-support ecosystem
aliases:
  - biospecimen resource system map
  - biobank LIMS and storage ecosystem
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-11
source_ids:
  - SRC-0004
  - SRC-0018
  - SRC-0019
  - SRC-0022
  - SRC-0023
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYS-0007-C05
    evidence:
      - source: SRC-0004
        locator: "Glossary `Cybersecurity`, printed p. xiv/PDF p. 16; §5.3.4, printed pp. 21–22/PDF pp. 41–42; §6.5, printed pp. 34–37/PDF pp. 54–57"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYS-0007-C05
    evidence:
      - source: SRC-0018
        locator: "§§2.3.5–2.3.7, printed pp. 22–26/PDF pp. 39–43; §5.3, printed pp. 69–82/PDF pp. 86–99; §5.4, printed pp. 83–89/PDF pp. 100–106; §6.2.1, printed pp. 97–108/PDF pp. 114–125; §6.3, printed pp. 126–133/PDF pp. 143–150; §§6.4–6.5, printed pp. 134–138/PDF pp. 151–155"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: SYS-0007-C05
    evidence:
      - source: SRC-0019
        locator: "§§1.1–1.2.3, printed pp. 2–4/PDF pp. 34–36; §4.1, printed pp. 52–57/PDF pp. 84–89; Chapter 5, printed pp. 102–121/PDF pp. 134–153"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: SYS-0007-C05
    evidence:
      - source: SRC-0022
        locator: "§§C.1.4–C.1.5, printed pp. 38–40/physical pp. 41–43; §§C.2.8–C.2.9, printed pp. 51–54/physical pp. 54–57; §§C.6–C.6.6, printed pp. 64–70/physical pp. 67–73"
  - predicate: depends-on
    target: AST-0005
    claim_id: SYS-0007-C02
    evidence:
      - source: SRC-0022
        locator: "§§A.1/B.1–B.12/C.2/C.5–C.6, printed pp. 3–34, 41–70/physical pp. 6–37, 44–73"
  - predicate: depends-on
    target: WFL-0009
    claim_id: SYS-0007-C02
    evidence:
      - source: SRC-0022
        locator: "§§B.1–B.12/C.2/C.5–C.6, printed pp. 4–34, 41–70/physical pp. 7–37, 44–73"
  - predicate: evidenced-by
    target: SRC-0023
    claim_id: SYS-0007-C05
    evidence:
      - source: SRC-0023
        locator: "HTML §§II, IV.C and VI.A–B; companion Scientific Record Keeping/Data Management, printed pp. 8–13/physical pp. 11–16"
  - predicate: evidenced-by
    target: SRC-0023
    claim_id: SYS-0007-C06
    evidence:
      - source: SRC-0023
        locator: "HTML §I final bullet, §IV.A opening, §IV.C and §VI.A–B; companion Electronic Notebooks, printed p. 9/physical p. 12"
tags:
  - laboratory
  - biobank
  - lims
  - instruments
  - storage
  - freezers
  - cloud
  - backup
  - identity
  - trust-boundaries
---

# Biobank informatics, storage and laboratory-support ecosystem

## Scope and evidence state

This is a class-level defensive system map combining NCI biobank informatics/
storage, NIH IRP ELN, WHO/CBS laboratory/building/containment scope and NIST
general OT architecture. It is not a reference architecture for a named
facility. `SRC-0023` closes the earlier literal-ELN evidence gap without
turning prescribed functions into deployment or test results.

## System and boundary matrix

| Component class | Coupled functions/assets | Trust boundary and validation state |
| --- | --- | --- |
| LIMS/biobank informatics | biospecimen/derivative IDs, processing/history, inventory/location, associated data, consent/access and audit state | NCI recommends validated systems; no deployment/result is observed |
| ELN | complete research record receiving human/program/imaging/instrument outputs and associating rationale, samples, results, storage and analysis | NIH IRP directly defines the class and prescribes identity/integrity/storage boundaries; no observed interface, named-facility topology or completed validation is inferred |
| Instruments/automation | collection/processing/analysis equipment, label/scanning and physical sample state | instrument↔record association and validation are recommended; interface/authority in a real facility is unknown |
| Storage/freezers/monitoring | physical material, containers/positions, alarms, backup capability and retrieval | inventory↔location and equipment-state boundaries require reconciliation/test; no location or setting is retained |
| Building/containment/support systems | containment/building automation, utilities, access/security and safety-relevant support | WHO/CBS/NIST establish relevance/control design, not a facility topology or universal coupling |
| Cloud/on-premise/external hosting | informatics platform, protected data, backups/restores and service availability | NCI identifies deployment options and prescribed backup/restore testing; host, tenancy, test completion and implementation are unknown |
| APIs/local/external systems | clinical/research databases, authorized platforms and data-standard translations | documented interface, authorization, conformance/interoperability and change boundaries; no actual API is exposed |
| Identity/role/project authorization | users, projects, permitted material/data operations and attributable audit events | RBAC/project permissions and identity-bearing logs are recommended; no credential secret or observed access decision |
| Backup/test environment | protected copies, recovery/restore and change/regression validation | prescribed tests are design evidence; completion and effectiveness remain unknown |

> **Claim record — SYS-0007-C01 | analytic-judgment**
> **Claim:** The reconciled map directly covers LIMS/informatics, instruments/
> automation, storage/freezers, building/containment systems, cloud/backup,
> interfaces and identity, but retains ELN as an explicit missing system class.
> **Claim status:** superseded
> **Scope:** Laboratory/biobank component classes across NCI/WHO/CBS/NIST;
> not a named-facility topology, implementation or `LAB-SD` Pass.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§C.1.4–C.1.5/C.2.8–C.2.9/C.6–C.6.6, printed pp. 38–40, 51–54,
> 64–70/physical pp. 41–43, 54–57, 67–73; `SRC-0022-C07`–`C09`;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> glossary/§§5.3.4/6.5, PDF pp. 16, 41–42, 54–57;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> Chapter 1/§4.1/Chapter 5, PDF pp. 34–37, 84–89, 134–153;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.5–2.3.7, printed pp. 22–26/PDF pp. 39–43; §§5.3–5.4,
> printed pp. 69–89/PDF pp. 86–106; §6.2.1, printed pp. 97–108/PDF
> pp. 114–125; §§6.3–6.5, printed pp. 126–138/PDF pp. 143–155;
> full-corpus search for literal `ELN` completed 2026-07-12.
> **Basis / limits:** Covered classes are direct and independent. Search
> non-retrieval is a corpus gap, not proof no ELN exists externally.
> **Superseded by:** `SYS-0007-C05`, after `SRC-0023` supplied the literal ELN
> class.

## Exact dependency boundaries

| Edge | Required trustworthy state | Failure/non-equivalence boundary |
| --- | --- | --- |
| instrument/label ↔ LIMS | physical identity/output is correctly associated with the intended item/record | connectivity does not prove command authority, calibration or data validity |
| specimen/derivative ↔ inventory | parent/child identity, quantity/state and physical location remain traceable | correct database state does not prove specimen quality or permitted use |
| storage/monitoring ↔ continuity | alarm/equipment state reaches an accountable responder and tested fallback | mandated alarm/test is not a completed drill or successful recovery |
| LIMS ↔ consent/clinical/research data | identifiers and authorized associations preserve privacy/purpose limits | data availability does not authorize a use or guarantee re-identification is impossible |
| API/external system ↔ local system | authorized, compatible, validated exchange preserves business/security rules | documented API design is not a live interface or universal interoperability |
| identity/project ↔ function/data | role/project authorization and attributable logging bound each operation | role label is not authentication strength, clearance or least-privilege proof |
| instrument/output ↔ ELN | intended record/output association preserves attributable scientific context | class-level inclusion does not prove a live interface, automation, calibration or valid result |
| user/PI/institution ↔ ELN | authorized users, responsible-investigator control and institutional ownership/access remain attributable | assigned responsibility does not prove an observed access decision or least privilege |
| ELN ↔ approved storage/cloud/local host | authorized deployment, integrity history and backup preserve availability/custody | prescribed ATO/backup boundaries do not prove topology, current vendor certification or successful recovery |
| production ↔ test environment | changes/upgrades are exercised separately before protected use | test-environment recommendation is not result evidence |
| informatics ↔ building/containment | dependencies are identified and segmented/tailored where applicable | co-location/relevance does not establish one network or control channel |

> **Claim record — SYS-0007-C02 | analytic-judgment**
> **Claim:** The system map organizes conceptual trust boundaries between the
> assets in `AST-0005` and lifecycle handoffs in `WFL-0009`, while every edge's
> actual implementation, direction, test state and dependency strength remain
> separately unknown.
> **Claim status:** active
> **Scope:** Exact defensive boundary map, not a facility architecture, data-
> flow observation or assurance result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.12/C.2/C.5–C.6, printed pp. 4–34, 41–70/physical pp. 7–37,
> 44–73; [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md),
> `AST-0005-C01`–`C03`; [WFL-0009](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md),
> `WFL-0009-C01`–`C03`; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5.3–5.4, printed pp. 69–89/PDF pp. 86–106; §§6.2.1/6.3–6.5,
> printed pp. 97–108, 126–138/PDF pp. 114–125, 143–155.
> **Basis / limits:** Direct functions support the edges; their canonical
> organization and validation labels are editorial.

## Resilience and evidence maturity

NCI recommends monitored storage, alarms, alternate capability, tested failure
response, backup/restore checks, physical-inventory reconciliation, software
validation and regression testing. WHO/CBS/NIST add laboratory/OT risk,
response, recovery and programme/test design. No source in this transaction
reports a named biobank's completed test or measured outcome.

> **Claim record — SYS-0007-C03 | analytic-judgment**
> **Claim:** The represented sources specify detection, continuity, recovery
> and validation functions at storage/informatics/building boundaries but do
> not establish a deployed biobank architecture or completed assurance result.
> **Claim status:** active
> **Scope:** Normative architecture/control design, not `LAB-AE`, incident or
> effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§C.2.8.5/C.3/C.6.5–C.6.6, printed pp. 53, 57–61, 69–70/physical
> pp. 56, 60–64, 72–73; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.5–7, PDF pp. 54–64; [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §4.1/Chapter 5, PDF pp. 84–89, 134–153;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§6.3–6.5, printed pp. 126–138/PDF pp. 143–155.
> **Basis / limits:** Functions/assurance expectations are direct; deployment
> and result predicates are absent.

> **Claim record — SYS-0007-C04 | artifact-observation**
> **Claim:** `SYS-0007` materially strengthens `LAB-SD` but leaves it Partial
> because the frozen criterion explicitly includes ELN and no current direct
> ELN evidence is ingested; adjacent LIMS/document functions are not proxies.
> **Claim status:** superseded
> **Scope:** Frozen-rubric evidence sufficiency after SRC-0022; not a claim that
> ELNs are absent from real laboratories.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYS-0007-C01`–`C03`; frozen `LAB-SD` criterion in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** One literal system class remains missing; Partial is
> non-scoring and prevents proxy substitution.
> **Superseded by:** `SYS-0007-C07` and the `SYN-0011-C04/C06` decision after
> ELN integration and independent reconciliation.

## SRC-0023 ELN integration

> **Claim record — SYS-0007-C05 | analytic-judgment**
> **Claim:** With `SRC-0023`, the reconciled class map directly covers every
> frozen `LAB-SD` component: LIMS, literal ELN, instruments/automation,
> storage/freezers, building/containment, cloud/backup, identity and explicit
> validation/authorization boundaries.
> **Claim status:** active
> **Scope:** Class-level laboratory/biobank system coverage across NIH/NCI,
> WHO/CBS and NIST lineages; not a named-facility architecture, deployment or
> completed validation result.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md),
> `SRC-0023-C03`–`C07`; HTML §§II, IV.C and VI.A–B; companion printed
> pp. 8–13/physical pp. 11–16; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> `SRC-0022-C07`–`C09`; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> glossary/§§5.3.4/6.5; [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> Chapter 1/§4.1/Chapter 5; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.5–2.3.7/5.3–5.4/6.2.1/6.3–6.5.
> **Basis / limits:** Every literal class/boundary is located. NIH and NCI are
> one broader NIH/HHS institutional lineage for independence accounting;
> WHO/CBS/NIST supply materially independent laboratory/containment/OT lines.

> **Claim record — SYS-0007-C06 | analytic-judgment**
> **Claim:** The new ELN edges are bounded as instrument/output↔record,
> user/PI/institution↔record and ELN↔approved storage/cloud/local deployment;
> each preserves association, authorization, integrity or availability without
> asserting a live interface, topology, current vendor certification or test
> outcome.
> **Claim status:** active
> **Scope:** Defensive trust-boundary reconciliation; no account path,
> configuration, command authority or operational recovery procedure.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md),
> `SRC-0023-C04`–`C07/C09/C10`; HTML §I final bullet, §IV.A opening,
> §IV.C and §VI.A–B; companion printed pp. 9, 12–13/physical pp. 12,
> 15–16; `SYS-0007-C02/C03`.
> **Basis / limits:** Direct requirements support the edges and explicit
> non-equivalences prevent architectural or effectiveness overclaim.

> **Claim record — SYS-0007-C07 | artifact-observation**
> **Claim:** `SYS-0007` now supplies complete literal system/boundary structure
> for `LAB-SD`; independent SF2/rubric review accepts that cell and does not
> alter `LAB-TV/XT/CI/AE/GR` or existing `LAB-CT`.
> **Claim status:** active
> **Scope:** Activated frozen-rubric sufficiency after SRC-0023, not absolute
> laboratory architecture completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYS-0007-C02/C03/C05/C06`; frozen `LAB-SD` criterion in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** All frozen components are present; `SYN-0011` records the
> separate synthesis and independent binary decision.

## Safety boundary

No facility layout, system address, network path, storage setpoint, material
identity, access secret, alarm contact or operational recovery instruction is
retained. The map is suitable for defensive architecture review only.

## Related pages

- [SYN-0023 — Laboratory transfer reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [SRC-0022 — NCI Best Practices](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0023 — NIH IRP ELN Policy](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
- [GOV-0012 — NCI governance](../governance/gov-0012-nci-best-practices-biospecimen-resources-2026.md)
- [GOV-0013 — NIH IRP ELN governance](../governance/gov-0013-nih-intramural-electronic-laboratory-notebook-policy.md)
- [AST-0005 — assets/stakeholders](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [WFL-0009 — lifecycle](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md)
- [SYN-0010 — reconciliation](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [SYN-0011 — system-boundary reconciliation](../syntheses/syn-0011-laboratory-biobank-system-boundary-reconciliation.md)
- [SYS-0001 — HCL support systems](sys-0001-hcl-containment-support-systems.md)
- [CTL-0011 — generic OT controls](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability and existing LAB-CT acceptance](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
