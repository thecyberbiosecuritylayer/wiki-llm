---
id: WFL-0009
type: workflow
title: Biospecimen material, data and custody lifecycle
aliases:
  - laboratory biobank lifecycle
  - biospecimen resource lifecycle
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
    claim_id: WFL-0009-C01
    evidence:
      - source: SRC-0004
        locator: "§§1.1–1.2, printed pp. 2–3/PDF pp. 22–23; §§5–6.6, printed pp. 19–39/PDF pp. 39–59; §7, printed pp. 40–44/PDF pp. 60–64"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: WFL-0009-C01
    evidence:
      - source: SRC-0019
        locator: "§§1.1–1.2.3, printed pp. 2–4/PDF pp. 34–36; §4.1, printed pp. 52–57/PDF pp. 84–89; Chapter 5, printed pp. 102–121/PDF pp. 134–153"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: WFL-0009-C01
    evidence:
      - source: SRC-0022
        locator: "§§B.1–B.12.3 (including B.12.1.1–B.12.1.4), printed pp. 4–34/physical pp. 7–37; §§C.2–C.3.3, printed pp. 41–61/physical pp. 44–64; §§C.5–C.6.6, printed pp. 62–70/physical pp. 65–73"
  - predicate: depends-on
    target: AST-0005
    claim_id: WFL-0009-C03
    evidence:
      - source: SRC-0022
        locator: "§§A.1/B.1–B.12/C.2/C.5–C.6, printed pp. 3–34, 41–70/physical pp. 6–37, 44–73"
tags:
  - laboratory
  - biobank
  - biospecimen
  - lifecycle
  - custody
  - consent
  - incident-learning
  - disposition
---

# Biospecimen material, data and custody lifecycle

## Scope and normalization

This lifecycle reconciles NCI human research biobanking with WHO/CBS laboratory
material and incident/programme governance. It is a functional map, not a
laboratory procedure.

The frozen word `accession` is normalized narrowly because NCI does not use it
as the canonical stage name: here it means `receipt/acquisition + unique-ID/
label assignment + inventory entry`. It does not import a clinical accessioning
process or claim that every resource performs those events in one step.

## Parallel lifecycle lanes

| Stage | Physical material lane | Data/consent lane | Identity/custody/quality lane | Evidence boundary |
| --- | --- | --- | --- | --- |
| Plan/authorize | define intended collection/use and resource scope | governance, protocol, consent, permitted use and data plan | roles, custodian/steward, risk/QMS baseline | NCI §§B.1–B.5; WHO risk cycle; design, not adoption |
| Collect/receive | collect or receive material under the bounded scope | capture source/context and required annotations | document handoff, condition and responsible actor | NCI §§C.2/C.2.10; WHO §§1.1–1.2 |
| Accession (normalized) | create/recognize the physical item and derivatives | associate consent/provenance and unique non-identifying record | assign label/ID and enter item/location into inventory | NCI §§C.2.8.4/C.6.1–C.6.2; no quoted accession term |
| Process/quality | process/preserve/derive under fit-for-purpose controls | record preanalytical/process/quality state | approved SOP, deviation and traceable operator/time state | NCI §§C.2–C.3; no universal procedure/settings |
| Inventory/store | maintain material and derivative physical state | retain inventory, annotations and permission state | location↔record reconciliation, access/monitoring/continuity controls | NCI §§C.2.8–C.2.9/C.6; no actual facility result |
| Retrieve/use/share | retrieve/use/distribute the permitted item | check purpose, consent/data-use and associated-data boundary | authorization, audit log, remaining quantity/state | NCI §§B.8–B.9/C.6.2 |
| Transfer/transport | package, hand off, receive and verify material | provide authorized manifest/context and data terms | agreement, chain of custody, discrepancy/condition record | NCI §C.2.10; WHO accountability/transport |
| Deviate/incident/respond | protect/contain material and continuity when state differs | preserve/report relevant records and notifications | detect, investigate, correct, reconcile and document | NCI §§C.1.6/C.3; WHO §§6.6–7; required loop, not event evidence |
| Close/transfer/dispose | transfer collection/custody or ethically dispose/return as applicable | transfer, de-identify, retain or dispose data under permission/legal limits | approve legacy decision and document final state | NCI §§B.12–B.12.3, including B.12.1.1–B.12.1.4; no claim all data can be recalled |
| Review/learn | update practices after deviations, incidents and lifecycle change | update governance/consent/data controls where applicable | audit, corrective action, control/risk review and lessons | WHO §§5–7; CBS §4.1/Chapter 5; NCI QMS |

> **Claim record — WFL-0009-C01 | analytic-judgment**
> **Claim:** The reconciled lifecycle covers collection/receipt, a bounded
> accession-equivalent, processing, inventory/storage, use/share/transport,
> closeout/disposal and incident-learning stages required by `LAB-WL`.
> **Claim status:** active
> **Scope:** Canonical laboratory/biobank functional stages across NCI/WHO/CBS;
> not one universal order, clinical accession rule or operating procedure.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.12.3 (including B.12.1.1–B.12.1.4), C.2–C.3.3 and C.5–C.6.6,
> printed pp. 4–34, 41–70/
> physical pp. 7–37, 44–73; `SRC-0022-C05/C06/C08/C10`;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2/5–7, printed pp. 2–3, 19–44/PDF pp. 22–23, 39–64;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §§1.1–1.2.3/4.1 and Chapter 5, PDF pp. 34–36, 84–89, 134–153.
> **Basis / limits:** Required stages are direct across independent sources;
> the ordering and accession normalization are explicit wiki analysis.

> **Claim record — WFL-0009-C02 | analytic-judgment**
> **Claim:** Material, data/consent and identity/custody/quality are parallel
> lanes: a specimen may be physically available while use is impermissible,
> data incomplete or custody/quality state unresolved.
> **Claim status:** active
> **Scope:** State-separation model for defensive review; not an observed
> mismatch, legal conclusion or claim that every lane uses one platform.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.12 and C.2/C.5/C.6, printed pp. 4–34, 41–57, 62–70/physical
> pp. 7–37, 44–60, 65–73; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.3–6.6, printed pp. 20–39/PDF pp. 40–59.
> **Basis / limits:** Sources directly distinguish material, information,
> permission, identity and custody predicates. Parallel lanes are editorial.

## Handoffs and exact trust boundaries

- donor/source ↔ collection: identity/consent and material source must remain
  associated without exposing unnecessary identity;
- receipt ↔ inventory: item/condition/identifier and responsible handoff must
  agree before the record becomes authoritative;
- material ↔ derivative: each division/derivation gets a traceable identity and
  origin without losing the parent relationship;
- physical location ↔ LIMS/inventory: moves/retrieval/distribution update both
  sides and retain an attributable history;
- permission/purpose ↔ use/share: material availability is insufficient if the
  consent, governance, legal or project authorization does not permit use;
- sender ↔ carrier ↔ receiver: chain of custody, manifest and condition/
  discrepancy state remain reconciled;
- operation ↔ incident/learning: deviation/incident evidence feeds corrective
  action and risk/control review rather than disappearing at recovery.

> **Claim record — WFL-0009-C03 | analytic-judgment**
> **Claim:** Every lifecycle handoff depends on distinct material, associated-
> data, permission, identity and custody assets in `AST-0005`, so no single
> inventory flag proves lawful use, specimen quality or continuity.
> **Claim status:** active
> **Scope:** Exact trust-boundary model, not a validated system architecture or
> observed chain failure.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.12/C.2/C.5–C.6, printed pp. 4–34, 41–70/physical pp. 7–37,
> 44–73; [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md),
> `AST-0005-C01`–`C03`.
> **Basis / limits:** Dependencies follow direct source separations; exact
> edges are wiki analysis and carry no implementation/result claim.

## Incident-learning and assurance boundary

WHO provides the explicit detect/report→contain/respond→investigate→correct→
review/learn loop; CBS adds required programme/test design; NCI adds deviations,
audits, corrective action, continuity and legacy review. None supplies a
completed biobank incident or independently evaluated outcome in this
transaction.

> **Claim record — WFL-0009-C04 | analytic-judgment**
> **Claim:** Incident learning is part of the reconciled lifecycle by direct
> normative design, but no incident, drill metric or effectiveness result is
> inferred from the existence of that loop.
> **Claim status:** active
> **Scope:** `LAB-WL` incident-learning limb and evidence-state boundary; not
> `LAB-CI` or `LAB-AE` acceptance.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.6–6.6.2, printed pp. 37–39/PDF pp. 57–59; Annex 2, printed
> pp. 78–82/PDF pp. 98–102; `SRC-0004-C07/C10`;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §4.1/Chapter 5, PDF pp. 84–89, 134–153; `SRC-0019-C06`;
> [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§C.1.6/C.3, printed pp. 40–41, 57–61/physical pp. 43–44, 60–64.
> **Basis / limits:** Loop/design predicates are direct. Result predicates are
> absent and deliberately not manufactured.

## Acceptance boundary

Subject to independent review of `SYN-0010`, this page meets `LAB-WL` at SF2.
It does not close `LAB-SD/CI/AE` and contains no operational sample detail,
storage settings, facility layout or personal record.

## Related pages

- [SYN-0023 — Laboratory transfer reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [SRC-0022 — NCI Best Practices](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [GOV-0012 — NCI governance](../governance/gov-0012-nci-best-practices-biospecimen-resources-2026.md)
- [AST-0005 — assets/stakeholders](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [SYS-0007 — informatics/storage system](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SYN-0010 — laboratory/biobank reconciliation](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [WFL-0004 — high-consequence material lifecycle](wfl-0004-high-consequence-material-lifecycle.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
