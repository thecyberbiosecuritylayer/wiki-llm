---
id: AST-0007
type: asset
title: Biomanufacturing materials, quality records and stakeholder map
aliases:
  - biomanufacturing asset stakeholder map
  - biopharmaceutical manufacturing assets
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0003
  - SRC-0031
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: AST-0007-C01
    evidence:
      - source: SRC-0003
        locator: "Abstract; §§New Risks Within the Growing Bioeconomy, Digital Information Flow in Biomanufacturing, Considerations for Emerging Biologic Products; Figures 1–2"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: AST-0007-C01
    evidence:
      - source: SRC-0031
        locator: "Part I §§3.1.3–3.1.7 and 4.1–4.10, printed pp. 3–14 (physical pp. 8–19); Annex III §§1–3, printed pp. 27–30 (physical pp. 32–35); Annex IV §§3–5, printed pp. 33–36 (physical pp. 38–41)"
tags:
  - biomanufacturing
  - assets
  - stakeholders
  - therapeutic-proteins
  - process-quality
  - release-records
---

# Biomanufacturing materials, quality records and stakeholder map

## Scope and reconciliation method

This page reconciles two materially independent source forms at class level:

- Guttieres et al. supply the wider biopharmaceutical value-chain envelope:
  biologics/ATMP processes, proprietary process/IP, PLC/DCS/SCADA classes,
  plant workers, suppliers, providers, patients and cross-site supply actors;
- ICH Q13 supplies a current normative continuous-manufacturing envelope:
  input/cell-bank/material states, equipment and digital-control interfaces,
  PAT/models/process-quality data, specifications, batch/release evidence,
  CTD/PQS records and manufacturer/regulator roles.

Neither source is a named-facility inventory or implementation audit. The map
contains no recipe, process setpoint, credential, topology, patient record or
material identity.

## Canonical asset matrix

| Frozen `BMO-AS` class | Reconciled class | Direct evidence and boundary |
| --- | --- | --- |
| Raw materials and cell banks | starting/raw/input materials, media/feed and supplier variability; traceable cell-bank vials and harvest material | Q13 §§3.1.3/4.2 and Annex III §§1/3. `Cell bank` does not imply full chain of identity/custody or an inventory |
| Recipes and IP | proprietary process/product IP, process design/control strategy, parameter/quality-attribute relationships and model assumptions | Guttieres abstract/§New Risks; Q13 §§3.1.7/4.1–4.4. No formula, sequence, setpoint or transferable recipe is reproduced |
| Process and quality data | sensor/PAT measurements, process parameters, material attributes, quality attributes, trends, models, reference/offline tests and release evidence | Q13 §§3.1.5–3.1.7/4.2 and Annex III §2.3. Data state is not equated with physical material state |
| Controllers and equipment | sensors/actuators, PLC/DCS/SCADA functional classes plus equipment connections, digital control interfaces, PAT, automation and active-control/model functions | Guttieres Figure 1/§Digital Information Flow; Q13 §§3.1.4–3.1.5. This is not a validated architecture or network map |
| QMS and release records | PQS-managed diversion/disposition/investigation/CAPA procedures, specifications, batch information, CTD dossier and release/RTRT evidence | Q13 §§4.1–4.10 and Annex IV §§3–5. `PQS` is a quality-system function, not proof of a particular QMS software platform |
| Product | in-process/intermediate/output material, therapeutic-protein drug substance, drug product and diverted/non-conforming material | Q13 §§1.2/3.1.6 and Annex III; Guttieres Figures 1–2. Potential quality status does not establish an incident |
| Physical/facility state | unit operations, connected equipment, material-transfer points, single-use/filter integrity and integrated process state | Q13 §§3.1.4/4.1 and Annex III §§1–3. No facility location, layout or exploitable interface is retained |

> **Claim record — AST-0007-C01 | analytic-judgment**
> **Claim:** The reconciled map covers the frozen biomanufacturing asset classes
> for raw/cell-bank material, process/IP knowledge, process/quality data,
> controllers/equipment, QMS/release evidence and product while keeping their
> material, digital, control, documentation and physical states distinct.
> **Claim status:** active
> **Scope:** Class-level biologics/ATMP and Q13 continuous-manufacturing
> contexts; not industrial variants, an inventory, ownership conclusion,
> architecture validation or implementation.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Abstract; §§New Risks Within the Growing Bioeconomy, Digital Information
> Flow in Biomanufacturing and Considerations for Emerging Biologic Products;
> Figures 1–2; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.3–3.1.7 and 4.1–4.10, printed pp. 3–14
> (physical pp. 8–19); Annex III §§1–3, printed pp. 27–30
> (physical pp. 32–35); Annex IV §§3–5, printed pp. 33–36
> (physical pp. 38–41).
> **Basis / limits:** The complete class union is direct across independent
> lineages. Similar functions do not prove a single deployed system.

## Stakeholder matrix

| Frozen stakeholder class | Reconciled actors/interests | Boundary |
| --- | --- | --- |
| Workforce | manufacturer/applicant, plant workers/operators, quality/PQS and investigation functions | Named functions do not prove staffing, training or exercised authority |
| Patients | patients and patient-specific ATMP material/information interests | Guttieres supplies this limb; Q13 itself does not map patients or clinical use |
| Supply stakeholders | input suppliers, manufacturing sites/control centers, providers/hospitals, warehouses/retailers and regulators | Guttieres Figure 2 is high-level; Q13 adds supplier variability and regulatory submission/review, not complete logistics responsibility |
| Wider affected interests | industry, government/regulators, healthcare providers and public supply/patient interests | Interests are not converted into universal rights or duties |

> **Claim record — AST-0007-C02 | analytic-judgment**
> **Claim:** The represented sources jointly cover workforce, patient and
> supply stakeholders together with manufacturer/applicant, supplier,
> provider, quality and regulator functions.
> **Claim status:** active
> **Scope:** Actor and affected-interest classes in represented
> biopharmaceutical/continuous contexts; not a complete responsibility matrix,
> legal duty allocation or observed role performance.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Abstract; §§New Risks Within the Growing Bioeconomy, Digital Information
> Flow in Biomanufacturing and Considerations for Emerging Biologic Products;
> Figure 2; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§4.1–4.10, printed pp. 8–14 (physical pp. 13–19), especially
> supplier/applicant/manufacturer/regulatory-authority predicates.
> **Basis / limits:** Required classes are direct in the union. Q13's regional
> adoption and Guttieres' conceptual map are not operational accountability
> evidence.

## Asset-state and trust-boundary model

| Boundary | Trustworthy state | Failure not established by this map |
| --- | --- | --- |
| input/cell bank ↔ recorded identity | source/lot/cell-bank state remains traceable to affected material/batch | no demonstrated custody break or error rate |
| material/process ↔ sensor/PAT data | measurement remains representative, timely and complete for its intended decision | no malicious signal manipulation or validated vulnerability |
| data/model ↔ active control | model assumptions, input quality and control action remain valid for system configuration and intended use | no deployed model, algorithm or attack path |
| process state ↔ quality/release record | specifications, tests, diversion and disposition evidence refer to the correct material/time segment | no released non-conforming product or patient outcome |
| quality hold/diversion ↔ physical material | digital decision and physical collection/diversion remain synchronized | no universal fail-safe or effectiveness result |

> **Claim record — AST-0007-C03 | analytic-judgment**
> **Claim:** Material identity, measured process state, model/control state,
> physical diversion and release-record state are separate trust objects; a
> trustworthy record alone does not prove material quality, and a conforming
> measurement alone does not prove complete product disposition.
> **Claim status:** active
> **Scope:** Defensive boundary model derived from the source classes; not an
> observed failure, likelihood estimate or universal architecture.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.2–3.1.7 and 4.1–4.8, printed pp. 3–12
> (physical pp. 8–17); Annex III §§1–3, printed pp. 27–30
> (physical pp. 32–35); [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1 and §Digital Information Flow in Biomanufacturing.
> **Basis / limits:** Sources distinguish material, data, control and quality
> states. The normalized trust-object interpretation is editorial.

## Evidence and acceptance boundary

> **Claim record — AST-0007-C04 | artifact-observation**
> **Claim:** `AST-0007` now exposes every literal `BMO-AS` class for later
> adjudication, but page completeness is not a score change, deployment,
> incident, system-validation or effectiveness result.
> **Claim status:** superseded
> **Scope:** Historical wiki structure after `SRC-0031`; final frozen-cell status remained
> subject to a separately reserved reconciliation and independent review.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `AST-0007-C01`–`C03`; frozen `BMO-AS/SD/CI/AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Rows and residual boundaries are directly inspectable.
> Editorial completeness cannot substitute for external evidence floors.
> Historical `SRC-0031` candidate checkpoint; `SYN-0016-C02/C07` subsequently
> completed independent reconciliation and superseded the pending decision.
> **Superseded by:** `SYN-0016-C02/C07`.

## Related pages

- [SRC-0031 — ICH Q13](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [SRC-0003 — Guttieres et al.](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [WFL-0003 — biopharmaceutical manufacturing digital thread](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [SYS-0002 — process-control stack](../systems/sys-0002-biomanufacturing-process-control.md)
- [RSK-0002 — control/data integrity disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [CTL-0015 — continuous-manufacturing quality controls](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [INC-0006 — Merck manufacturing/supply incident](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [RSK-0019 — observed supply path](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [SYN-0028 — BMO residual reconciliation](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
