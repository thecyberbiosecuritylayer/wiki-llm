---
id: SYS-0002
type: system
title: Biomanufacturing process-control stack
aliases:
  - biomanufacturing process-control stack
  - biomanufacturing PLC DCS SCADA layers
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-15
source_ids:
  - SRC-0003
  - SRC-0018
  - SRC-0031
  - SRC-0044
  - SRC-0045
  - SRC-0048
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: SYS-0002-C01
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1 and caption"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYS-0002-C06
    evidence:
      - source: SRC-0018
        locator: "§2.3.3 and Figure 7, printed pp. 19–21 (PDF pp. 36–38); §§5.4.1–5.4.2 and Figures 18–19, printed pp. 83–87 (PDF pp. 100–104)"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: SYS-0002-C05
    evidence:
      - source: SRC-0031
        locator: "Part I §§3.1.4–3.1.7 and 4.1–4.4, printed pp. 4–10 (physical pp. 9–15); Annex III §§2.2–2.3, printed pp. 28–29 (physical pp. 33–34)"
  - predicate: evidenced-by
    target: SRC-0044
    claim_id: SYS-0002-C07
    evidence:
      - source: SRC-0044
        locator: "MHRA §§6.16 and 6.20, printed pp. 16 and 19; MRP, identity, supplier/cloud/service boundaries"
  - predicate: evidenced-by
    target: SRC-0045
    claim_id: SYS-0002-C07
    evidence:
      - source: SRC-0045
        locator: "NCSC definitive-architecture pp. 3–5/16–31 and secure-connectivity pp. 5–32; vendor/cloud/remote/external boundaries"
  - predicate: evidenced-by
    target: SRC-0048
    claim_id: SYS-0002-C07
    evidence:
      - source: SRC-0048
        locator: "FDA Q1/Q3/Q12, report pp. 4–6 and 10; cloud infrastructure, MES and LIMS"
tags:
  - biomanufacturing
  - process-control
  - ot
  - cyber-physical
---

# Biomanufacturing process-control stack

> Defensive abstraction of measurement/action, equipment-control,
> distributed-control and supervisory layers that connect digital state with a
> physical biomanufacturing process. This is not a network diagram or a list of
> externally reachable devices.

## Scope

The reconciled model covers sensors/actuators, programmable equipment
controllers, distributed/supervisory control, physical and digital equipment
interfaces, PAT/soft sensors, hardware/software active controls, process
models, automation and quality/release decision boundaries. Guttieres/NIST
supply generic PLC/DCS/SCADA classes; Q13 supplies sector-specific continuous-
manufacturing quality/control functions.

This page contains no controller vendors, product models, search services,
default credentials, protocols, addresses, or operational setpoints.

## Functional layers

1. **Measurement and action:** physical measurements and actions at process
   equipment.
2. **Equipment control:** dedicated controllers that integrate measurements and
   execute configured process logic.
3. **Distributed coordination:** systems coordinating multiple process units or
   production stages.
4. **Supervisory layer:** data collection/storage, monitoring/control and
   optimization at facility or cross-site level.

> **Claim record — SYS-0002-C01 | source-report**
> **Claim:** Figure 1 in Guttieres et al. models biomanufacturing process control
> as interacting measurement/action, PLC, DCS, and SCADA layers connected to
> upstream, downstream, and fill/finish stages.
> **Claim status:** active
> **Scope:** Conceptual information-flow model for typical monoclonal-antibody
> manufacturing.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> § Digital Information Flow in Biomanufacturing; Figure 1 and caption.
> **Basis / limits:** Layer labels and arrows are directly visible. The source
> does not establish universal deployment, network topology, interface
> security, or a validated architecture.

## Cyber-biological dependency

The key dependency is functional, not merely network-based: digital
measurements, logic, control signals or supervisory decisions can influence
physical process execution and the data used to assess it. Conversely,
physical/process measurements feed digital monitoring and decision layers.

> **Claim record — SYS-0002-C02 | analytic-judgment**
> **Claim:** `SYS-0002` creates a two-way cyber-physical dependency class:
> digital control state can affect process state, while process/sensor state
> affects digital monitoring and decisions; a complete RSK still requires a
> specific failure, validation gap and downstream consequence.
> **Claim status:** active
> **Scope:** Defensive interpretation of Figure 1, not a claim about a named
> facility.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1; § Digital Information Flow in Biomanufacturing, paragraphs on
> sensors/actuators, PLCs, DCSs and SCADA.
> **Basis / limits:** Figure supports bidirectional input/output and control
> layers. It does not show which physical changes are possible, what validation
> catches them or whether an attacker can reach the system.

## Continuous-manufacturing quality interfaces

Q13 adds the sector-specific functions absent from the earlier generic stack:

- physical connections and digital control interfaces between equipment;
- in-line/online/at-line PAT, soft sensors and physical/data sampling;
- hardware/software active controls, automation and process models;
- process/quality data used for adjustment, pause, diversion and release;
- conventional/reference tests and human/PQS investigation/disposition where
  digital/real-time evidence is unavailable or insufficient;
- validation, continuous verification and model-performance maintenance.

> **Claim record — SYS-0002-C05 | source-report**
> **Claim:** Q13 defines a continuous-manufacturing system through equipment,
> physical/digital connections, monitoring/control systems and configuration,
> and links PAT, automation and models to process and quality decisions.
> **Claim status:** active
> **Scope:** Q13 functional system class, not a network diagram, named vendor,
> commercial deployment or validated cyber boundary.
> **As of:** 2022-11-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.4–3.1.7 and 4.1–4.4, printed pp. 4–10
> (physical pp. 9–15); Glossary, printed pp. 15–16
> (physical pp. 20–21); Annex III §§2.2–2.3, printed pp. 28–29
> (physical pp. 33–34).
> **Basis / limits:** Components, interfaces and decision functions are direct.
> Q13 does not identify enterprise/network products, identities or privileges.

> **Claim record — SYS-0002-C06 | analytic-judgment**
> **Claim:** Guttieres, NIST and Q13 now reconcile generic PLC/DCS/SCADA,
> continuous process-control and quality/release boundaries, but the corpus
> still lacks a complete MES/LIMS/QMS-software/ERP, identity, vendor/cloud/
> remote and validated-boundary architecture.
> **Claim status:** superseded
> **Scope:** Current corpus-level BMO system map; `PQS` is not treated as proof
> of a QMS software platform and Q13 examples are not deployments.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1/§Digital Information Flow; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §2.3.3/Figure 7 and §§5.4.1–5.4.2/Figures 18–19, printed pp. 19–21,
> 83–87; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.4–3.1.7/4.1–4.4, printed pp. 4–10
> (physical pp. 9–15).
> **Basis / limits:** The covered union and absent literal classes are directly
> inspectable. Missing evidence is not a claim that facilities lack them.
> **Superseded by:** `SYS-0002-C07` after current FDA/MHRA/NCSC integration.

> **Claim record — SYS-0002-C07 | analytic-judgment**
> **Claim:** The current union now adds explicit MES, LIMS, MRP, identity,
> vendor, cloud, remote and external-connectivity classes to generic PLC/DCS/
> SCADA and Q13 process/quality boundaries, but still lacks literal QMS-as-
> software and ERP coverage; `BMO-SD` therefore remains Partial.
> **Claim status:** active
> **Scope:** Corpus-level component/boundary audit; MRP is not ERP and
> organizational PQS/quality-system language is not a QMS software platform.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0002-C01/C05`; [SRC-0048](../sources/src-0048-us-fda-drug-cgmp-data-integrity-guidance-2018-current.md),
> Q1/Q3/Q12, report pp. 4–6 and 10; [SRC-0044](../sources/src-0044-uk-mhra-gxp-data-integrity-guidance-2018-current.md),
> §§6.16/6.20, printed pp. 16/19; [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> definitive-architecture pp. 3–5/16–31 and secure-connectivity pp. 5–32.
> **Basis / limits:** Named classes are direct across independent sources;
> missing literal enterprise applications cannot be replaced by related terms.

## Security properties

The following list consists of defensive requirements analytically derived in
`SYS-0002-C02` from the functional dependency in Figure 1; these are not
source-reported controls or evidence of their implementation or effectiveness:

- integrity and authenticity of measurements, logic and commands;
- availability of control, monitoring and data history;
- provenance and temporal consistency of process/quality data;
- authorized change and maintenance;
- recoverability without creating product-quality or safety ambiguity.

These properties are defensive requirements inferred from the dependency; they
are not proof that any specific weakness exists.

## Boundaries and dependencies

Potential boundaries exist between field/equipment control, distributed
control, supervisory systems, PAT/model/release evidence, human quality
decisions, facility IT and—in distributed models—remote manufacturing sites/
control centers. Q13 adds quality and material-decision boundaries but still
does not provide segmentation, identities, privileges, protocols, vendor/cloud
responsibilities, manual cyber fallback or safety-system independence.

> **Claim record — SYS-0002-C03 | analytic-judgment**
> **Claim:** Current evidence supports the functional layer model but not a
> current OT reference architecture, validated vulnerability, prevalence claim
> or control-effectiveness conclusion for biomanufacturing.
> **Claim status:** superseded
> **Scope:** Wiki corpus after `SRC-0003`.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> § Digital Information Flow in Biomanufacturing; Figure 1; § Ensuring a
> Resilient Biomanufacturing Industry.
> **Basis / limits:** Source is a 2019 Perspective and gives general
> recommendations. NIST SP 800-82r3 and implementation/evaluation sources must
> be ingested before current architecture/control claims. Historical
> after-`SRC-0003` assessment; superseded by `SYS-0002-C06`.
> **Superseded by:** `SYS-0002-C06` (with the current residual carried by
> `SYS-0002-C07`).

> **Claim record — SYS-0002-C04 | analytic-judgment**
> **Claim:** Independent NIST OT guidance corroborates the generic PLC/DCS/
> SCADA class and explicitly names pharmaceutical DCS, but neither source
> establishes a validated biomanufacturing architecture or complete MES/LIMS/
> QMS/ERP and release boundary.
> **Claim status:** superseded
> **Scope:** Generic biomanufacturing/OT functional classes, not a facility
> topology, GMP validation or product implementation.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow and Figure 1;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §2.3.3 and Figure 7, printed pp. 19–21 (PDF pp. 36–38);
> §§5.4.1–5.4.2 and Figures 18–19, printed pp. 83–87
> (PDF pp. 100–104).
> **Basis / limits:** The generic layer/class overlap is independent and direct.
> NIST's notional figures and sector mention do not validate the missing quality,
> identity, supplier or deployment boundaries. Historical after-`SRC-0018`
> assessment; Q13 now supplies the quality/release limb, and current residual
> architecture gaps are stated in `SYS-0002-C06`.
> **Superseded by:** `SYS-0002-C06` (with the current residual carried by
> `SYS-0002-C07`).

## Evidence and uncertainty

Dated source statements about discoverability, default credentials and broad
controller vulnerability were deliberately not integrated. They are neither
needed for the defensive layer model nor adequate as current, product-specific
evidence.

## Related pages

- [WFL-0003 — Biopharmaceutical manufacturing information and control flows](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [RSK-0002 — Process-control integrity or availability disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [SRC-0003 — Guttieres et al. 2019](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0031 — ICH Q13](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [CTL-0015 — continuous-manufacturing quality controls](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [AST-0007 — biomanufacturing assets/stakeholders](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [VUL-0003 — BMO data-integrity/OT exposure classes](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [INC-0006 — Merck manufacturing/supply incident](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [RSK-0019 — observed Merck supply path](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [SYN-0028 — BMO residual reconciliation](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
  § Digital Information Flow in Biomanufacturing; Figure 1.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.3 and 5.4.
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
  §§3.1.4–3.1.7/4.1–4.4; Annex III §§2.2–2.3.
- [SRC-0044](../sources/src-0044-uk-mhra-gxp-data-integrity-guidance-2018-current.md)
- [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md)
- [SRC-0048](../sources/src-0048-us-fda-drug-cgmp-data-integrity-guidance-2018-current.md)
