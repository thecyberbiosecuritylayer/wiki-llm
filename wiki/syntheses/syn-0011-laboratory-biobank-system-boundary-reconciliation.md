---
id: SYN-0011
type: synthesis
title: Laboratory and biobank system-boundary reconciliation
aliases:
  - LAB-SD reconciliation
  - LIMS ELN storage containment boundary matrix
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
jurisdictions:
  - Global
  - United States
  - Canada
relations:
  - predicate: evidenced-by
    target: SRC-0023
    claim_id: SYN-0011-C01
    evidence:
      - source: SRC-0023
        locator: "HTML §§II, IV.C and VI.A–B; companion Scientific Record Keeping/Data Management, printed pp. 8–13/physical pp. 11–16"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: SYN-0011-C01
    evidence:
      - source: SRC-0022
        locator: "§§C.1.4–C.1.5, C.2.8–C.2.9 and C.6–C.6.6, printed pp. 38–40, 51–54, 64–70/physical pp. 41–43, 54–57, 67–73"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYN-0011-C01
    evidence:
      - source: SRC-0004
        locator: "Glossary `Cybersecurity`, printed p. xiv/PDF p. 16; §§5.3.4/6.5–7, printed pp. 21–22, 34–44/PDF pp. 41–42, 54–64"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: SYN-0011-C01
    evidence:
      - source: SRC-0019
        locator: "Chapter 1 and §§1.1–1.2.3, printed pp. 2–4/PDF pp. 34–36; §4.1, printed pp. 52–57/PDF pp. 84–89; Chapter 5, printed pp. 102–121/PDF pp. 134–153"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYN-0011-C01
    evidence:
      - source: SRC-0018
        locator: "§§2.3.5–2.3.7, printed pp. 22–26/PDF pp. 39–43; §§5.3–5.4, printed pp. 69–89/PDF pp. 86–106; §§6.2.1/6.3–6.5, printed pp. 97–108, 126–138/PDF pp. 114–125, 143–155"
tags:
  - laboratory
  - biobank
  - system-boundaries
  - lims
  - eln
  - instruments
  - storage
  - containment
  - cloud
  - identity
  - validation
  - evidence-quality
---

# Laboratory and biobank system-boundary reconciliation

## Question, cutoff and independence

This synthesis tests only the frozen `LAB-SD` criterion after complete
`SRC-0023` integration. Cutoff is 2026-07-12.

NIH OIR ELN policy and NCI biobank guidance share the NIH/HHS parent and count
as one broader U.S. institutional lineage for independence. WHO laboratory
guidance, the Canadian Biosafety Standard and NIST OT guidance are materially
separate issuer/development lineages. NIST is generic OT evidence and is used
only where a laboratory/biobank source first establishes sector relevance.

> **Claim record — SYN-0011-C01 | analytic-judgment**
> **Claim:** The complete-criterion portfolio is SF2-appropriate: one broader
> NIH/HHS lineage supplies direct LIMS/biobank and literal ELN functions, while
> materially independent WHO, Canadian and NIST lineages establish laboratory/
> containment and generic OT boundary/control context; NIH and NCI are not
> double-counted.
> **Claim status:** active
> **Scope:** Independence and claim appropriateness for `LAB-SD`; not
> independence for implementation, incident or effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md),
> `SRC-0023-C02`–`C10`; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> `SRC-0022-C03/C07`–`C10`; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C03/C05/C08`; [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> `SRC-0019-C04/C06/C08`; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> `SRC-0018-C03/C04/C06/C08`.
> **Basis / limits:** Issuers and source-development contexts are explicit.
> Per-limb duplication is not manufactured, and shared federal/NIH ancestry is
> not counted as two independent ELN/biobank lineages.

## Literal component and boundary matrix

| Frozen component | Direct evidence in the reconciled map | Validation/non-equivalence boundary |
| --- | --- | --- |
| LIMS/informatics | NCI specifies biospecimen identity/history/inventory/data/access/audit functions | recommended validation and auditability are design; no deployed LIMS result |
| ELN | NIH directly defines complete electronic research-record creation/storage/retrieval/sharing and instrument/program inputs | literal class and requirements are direct; no named-facility interface or completed validation |
| Instruments/automation | NCI covers laboratory equipment/record association; NIH covers instrument output entering the record; NIST supplies generic OT classes | association does not prove command authority, automation, calibration or valid output |
| Storage/freezers | NCI covers material-location/equipment monitoring/continuity; WHO/CBS add laboratory material/facility expectations | no location, setpoint, alarm route or completed drill is retained |
| Building/containment | WHO/CBS establish laboratory/building/containment functions; NIST supplies generic building/physical-access/OT boundaries | relevance does not prove one network, topology or universal coupling |
| Cloud/backup | NCI covers hosted/on-premise options and prescribed restore testing; NIH distinguishes approved SaaS/cloud from local deployment and requires backup; NIST adds generic availability/recovery structure | no tenancy, vendor-status, successful restore or effectiveness claim |
| Identity | NCI project/role/audit design plus NIH user/PI/institution ownership/authorization allocation | role assignment is not authentication strength, least privilege or observed access |
| Validated boundaries | NCI/NIST prescribe software/interface/change/test validation; NIH prescribes authorization, attributable history and ATO branches | `validated` is represented as explicit validation/authorization requirement and evidence-state boundary, not a fabricated completed test |

> **Claim record — SYN-0011-C02 | analytic-judgment**
> **Claim:** The matrix covers every literal `LAB-SD` component—LIMS, ELN,
> instruments/automation, storage/freezers, building/containment, cloud/backup,
> identity and validation-aware boundaries—with exact evidence and source-
> appropriate non-equivalences.
> **Claim status:** active
> **Scope:** Frozen class-level system/dependency/trust-boundary criterion;
> not a universal reference architecture or evidence of deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0007](../systems/sys-0007-biobank-informatics-storage-ecosystem.md),
> `SYS-0007-C02/C03/C05/C06`; `SYN-0011-C01`; underlying locators recorded in
> the five source relations above.
> **Basis / limits:** Every noun and boundary predicate in the frozen criterion
> is direct. No missing component is proxied by a neighboring class.

## Exact defensive edges

The acceptance-bearing edges are deliberately functional rather than
deployment-specific:

1. `physical item/instrument output ↔ intended LIMS/ELN record` preserves
   association and provenance without asserting automation or valid output;
2. `authorized user/project/PI/institution ↔ record/system function` preserves
   responsibility and attributable access without asserting authentication
   strength or a real decision;
3. `LIMS/ELN ↔ approved local/cloud storage and backup` preserves custody,
   availability and authorization branches without topology/vendor claims;
4. `storage/building/containment state ↔ accountable monitoring/continuity`
   preserves dependency awareness without publishing settings or alarm routes;
5. `production system/interface/change ↔ separate validation/test state`
   preserves required verification without calling a prescription a result.

> **Claim record — SYN-0011-C03 | analytic-judgment**
> **Claim:** These five bounded edges reconcile material, record, identity,
> hosting, facility and validation dependencies while explicitly separating
> class relevance, required controls, implementation and completed test state.
> **Claim status:** active
> **Scope:** Defensive trust-boundary semantics for `LAB-SD`; not a threat
> scenario, incident path or control-effectiveness conclusion.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0011-C01/C02`; [SYS-0007](../systems/sys-0007-biobank-informatics-storage-ecosystem.md),
> exact dependency matrix and `SYS-0007-C02/C03/C06`.
> **Basis / limits:** Each edge has a located underlying function and explicit
> failure/non-equivalence boundary. No operational configuration is exposed.

## Frozen-cell decision and residual audit

> **Claim record — SYN-0011-C04 | analytic-judgment**
> **Claim:** Independent strict review confirms that the complete matrix
> satisfies `LAB-SD` at SF2 because every required system/dependency/boundary
> class is literal and reconciled across materially independent lineages, even
> though not every individual limb is independently duplicated.
> **Claim status:** active
> **Scope:** Frozen `LAB-SD` binary acceptance only; not facility validation,
> implementation or absolute laboratory architecture completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0011-C01`–`C03`; frozen `LAB-SD` criterion in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** The criterion asks for a validated-boundary map at SF2,
> not an observed facility deployment. Completed validation remains separately
> unavailable and cannot support `LAB-AE`.

| LAB cell | State after SRC-0023 | Why no additional Pass |
| --- | --- | --- |
| `LAB-ST/AS/WL` | Pass, unchanged | NIH record/material context strengthens existing accepted cells but cannot create a second point |
| `LAB-TV` | Partial | no complete malicious/insider/accidental/environmental/supply plus weakness/exposure corpus is added |
| `LAB-XT` | Partial | system boundaries are not two full source-backed cyber→bio and material/input→digital-decision scenarios |
| `LAB-CI` | Partial | no primary laboratory/biobank incident outcome plus independent corroboration is added |
| `LAB-CT` | Pass, unchanged | existing exact-edge control acceptance already scores once |
| `LAB-AE` | Partial | prescribed authorization, backup and validation have no completed scoped metric or independent evaluation |
| `LAB-GR` | Partial | NIH institutional policy does not supply current biobank accreditation/adoption reconciliation |

> **Claim record — SYN-0011-C05 | analytic-judgment**
> **Claim:** Only `LAB-SD` is a candidate promotion; all adjacent LAB cells and
> global gates retain their prior states because system/requirement evidence
> cannot substitute for scenarios, incidents, completed assurance or current
> accreditation/adoption evidence.
> **Claim status:** active
> **Scope:** Frozen-rubric residual audit after SRC-0023; Partial denotes an
> incomplete corpus, not absence from real laboratories.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0011-C01`–`C04`; [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md),
> `SRC-0023-C09/C10`; [GOV-0013](../governance/gov-0013-nih-intramural-electronic-laboratory-notebook-policy.md),
> `GOV-0013-C05/C06`; frozen LAB/global criteria in `SYN-0001`.
> **Basis / limits:** Every unfulfilled predicate is named; no adjacency credit
> or document-volume credit is awarded.

## Score delta

> **Claim record — SYN-0011-C06 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `LAB-SD` as
> Partial→Pass, raising Laboratories/Biobanks from 4/10 to 5/10 and the
> overall score from 28/110 to 29/110 (26.4%), with 29 Pass, 75 Partial and
> 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after complete SRC-0023 integration and frozen
> rubric v1.0; not absolute completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0011-C01`–`C05`; prior `SYN-0001-C16` checkpoint at
> 28 Pass/76 Partial/6 Absent; frozen score method in `SYN-0001`.
> **Basis / limits:** One literal transition produces the arithmetic;
> independent content, locator, lineage and binary-score review passed on
> 2026-07-12.

## Safety boundary

This synthesis contains class-level system and trust-boundary semantics only.
It omits facility topology, account paths, platform configuration, storage/
containment settings, credentials, alarm routes, research records and
operational recovery procedures.

## Related pages

- [SRC-0023 — NIH IRP ELN Policy](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
- [GOV-0013 — NIH IRP ELN governance](../governance/gov-0013-nih-intramural-electronic-laboratory-notebook-policy.md)
- [SYS-0007 — laboratory/biobank system map](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SRC-0022 — NCI biobank guidance](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SYN-0010 — LAB scope/assets/lifecycle reconciliation](syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [SYN-0007 — existing LAB control acceptance](syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)
- [SYN-0012 — LAB governance reconciliation](syn-0012-global-canada-us-laboratory-biobank-governance-reconciliation.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
