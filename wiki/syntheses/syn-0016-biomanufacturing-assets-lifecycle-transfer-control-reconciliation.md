---
id: SYN-0016
type: synthesis
title: Biomanufacturing assets, lifecycle, transfer and control reconciliation
aliases:
  - BMO AS WL XT CT reconciliation
  - biomanufacturing four-cell SF2 audit
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-11
source_ids:
  - SRC-0003
  - SRC-0018
  - SRC-0031
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: SYN-0016-C01
    evidence:
      - source: SRC-0003
        locator: "Abstract; §§New Risks Within the Growing Bioeconomy, Digital Information Flow in Biomanufacturing, Continuous Manufacturing, Distributed Manufacturing and Considerations for Emerging Biologic Products; Figures 1–2"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYN-0016-C01
    evidence:
      - source: SRC-0018
        locator: "§§2.3.3, 3–6, printed pp. 19–138/PDF pp. 36–155; Appendices E–F, printed pp. 207–298/PDF pp. 224–315"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: SYN-0016-C01
    evidence:
      - source: SRC-0031
        locator: "Part I §§1–4.10, printed pp. 1–14/physical pp. 6–19; Annex III §§1–3.3, printed pp. 27–30/physical pp. 32–35; Annex IV §§3–5, printed pp. 33–36/physical pp. 38–41; Annex V §§1–3.3, printed pp. 37–41/physical pp. 42–46"
tags:
  - biomanufacturing
  - operational-technology
  - assets
  - lifecycle
  - transfer
  - controls
  - evidence-reconciliation
---

# Biomanufacturing assets, lifecycle, transfer and control reconciliation

## Question, cutoff and method

This synthesis asks whether the current corpus satisfies exactly four frozen
rubric cells: `BMO-AS`, `BMO-WL`, `BMO-XT` and `BMO-CT`. The evidence cutoff is
2026-07-12. It applies each literal criterion, the SF2 independence floor and
the anti-proxy rule in
[SYN-0001](syn-0001-coverage-rubric.md).

The method is conjunctive: every required element must have direct located
support; materially independent sources must cover the union; source-specific
gaps and non-equivalences remain visible; and no design/example is promoted to
implementation, incident, test or effectiveness evidence. Page volume and
repeated regional copies do not count.

## Evidence base and independence

The three source roles are distinct:

- Guttieres et al. provide the sector-specific conceptual biopharmaceutical/
  ATMP asset, stakeholder, material, information, control and cross-site
  value-chain envelope;
- NIST SP 800-82r3 provides current generic OT architecture, access, integrity
  monitoring, response, recovery and assurance functions with safety and
  availability constraints;
- ICH Q13 provides continuous-manufacturing material/process/quality,
  bidirectional signal/control, traceability, diversion, disposition, release
  and validation predicates.

Guttieres and Q13 are materially independent lineages for the asset, lifecycle
and transfer cells. NIST and ICH Q13 are the independent normative lineages for
the control cell; Guttieres supplies only the sector-path anchor there because
its control recommendations derive from an older NIST CSF. FDA and EMA are
regional presentations of the same ICH technical lineage and never create a
second technical source.

> **Claim record — SYN-0016-C01 | analytic-judgment**
> **Claim:** Guttieres, NIST SP 800-82r3 and ICH Q13 form claim-appropriate
> independent evidence roles for this four-cell audit: Guttieres plus Q13
> support `BMO-AS/WL/XT`, while NIST plus Q13 support `BMO-CT` and Guttieres
> anchors its sector applicability without being double-counted as a third
> control lineage.
> **Claim status:** active
> **Scope:** Frozen SF2 lineage accounting for four BMO cells; not source
> equivalence, current industry prevalence or independent evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Abstract; §§Digital Information Flow in Biomanufacturing/Continuous
> Manufacturing/Distributed Manufacturing/Considerations for Emerging
> Biologic Products; Figures 1–2;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md), §§1.1,
> 2.3.3 and 3–6, printed pp. 6, 19–138/PDF pp. 23, 36–155;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§1–4.10, printed pp. 1–14/physical pp. 6–19; Annex III, printed
> pp. 27–30/physical pp. 32–35; `SRC-0003-C01`–`C04/C07`,
> `SRC-0018-C02/C03/C05/C07` and `SRC-0031-C02`–`C10`.
> **Basis / limits:** Issuer, genre, technical content and derivation are
> explicit. Regional adoption wrappers, citations and derived control advice
> are not multiplied into independent lineages.

## `BMO-AS` — assets and stakeholders

| Literal element | Direct reconciled support | Non-equivalence boundary |
| --- | --- | --- |
| raw materials/cell banks | Q13 input/raw material, supplier variability, traceable cell-bank vial and harvest predicates | no complete inventory or custody proof |
| recipes/IP | Guttieres proprietary process/product knowledge plus Q13 process design, control strategy and model assumptions | no formula, sequence, setpoint or transferable recipe |
| process/quality data | Q13 PAT/sensor data, parameters/attributes, models, trends, tests and release evidence | recorded state is not physical product quality |
| controllers | Guttieres sensors/actuators and PLC/DCS/SCADA plus Q13 equipment, PAT, automation and digital-control interfaces | no deployed architecture or reachable interface |
| QMS/release records | Q13 PQS diversion/disposition/investigation/CAPA, specifications, batch/CTD and release evidence | PQS is not proof of QMS software |
| product | Guttieres finished product plus Q13 in-process, intermediate, output, therapeutic-protein and diverted/non-conforming material | no affected commercial batch or incident |
| workforce | Guttieres plant/operator functions plus Q13 manufacturer/applicant, quality/PQS and investigation functions | no staffing or authority-performance evidence |
| patients | Guttieres patient and patient-specific ATMP interests | no patient record or outcome |
| supply stakeholders | suppliers, sites/control centres, providers/hospitals, warehouses/retailers and regulators across the two sources | no complete responsibility or logistics map |

> **Claim record — SYN-0016-C02 | analytic-judgment**
> **Claim:** `AST-0007` and its independent Guttieres/Q13 basis satisfy
> `BMO-AS`: every literal material, knowledge, data, controller, quality/
> release, product, workforce, patient and supply-stakeholder class is directly
> represented and reconciled without merging its state or role.
> **Claim status:** active
> **Scope:** Frozen class-level `BMO-AS` criterion; not industrial scope,
> ownership, inventory completeness, architecture validation or deployment.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Abstract; §§New Risks Within the Growing Bioeconomy/Digital Information Flow
> in Biomanufacturing/Considerations for Emerging Biologic Products;
> Figures 1–2; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.3–3.1.7 and 4.1–4.10, printed pp. 3–14/physical
> pp. 8–19; Annex III §§1–3, printed pp. 27–30/physical pp. 32–35;
> Annex IV §§3–5, printed pp. 33–36/physical pp. 38–41;
> [AST-0007](../assets/ast-0007-biomanufacturing-assets-stakeholders.md),
> `AST-0007-C01`–`C03`.
> **Basis / limits:** Every literal class is located in the independent-source
> union. The normalized map is editorial and does not imply one deployed
> facility or software stack.

## `BMO-WL` — end-to-end lifecycle

| Required stage | Direct support | Preserved boundary |
| --- | --- | --- |
| development | Guttieres cell-line/process/IP context; Q13 process/control/model development | no named programme or technology-transfer result |
| raw supply | Guttieres raw-material start; Q13 input/material variability and cell-bank traceability | no supplier-qualification outcome |
| upstream | Guttieres cell culture; Q13 Annex III perfusion culture/harvest | therapeutic-protein branch is not all biologics/ATMP |
| downstream | Guttieres purification; Q13 capture, inactivation, polishing, filtration and concentration classes | functional sequence, not an operating procedure |
| fill/finish | Guttieres Figure 1 downstream→fill/finish→finished product | not independently supplied by Q13 Annex III |
| release | Q13 monitoring/testing/specification, validation, diversion/disposition, PQS/CAPA and release evidence | design/evidence expectations, not an approved batch |
| distribution | Guttieres Figure 2 provider/warehouse/downstream supply network | no storage/logistics execution record |

Across those stages, `WFL-0003` separately tracks material, data, control and
quality/decision state. Detailed technology transfer, supplier qualification,
storage, recall, retirement and validated recovery remain useful enterprise
gaps, but they are not substituted for or added to the frozen literal stage
criterion.

> **Claim record — SYN-0016-C03 | analytic-judgment**
> **Claim:** The Guttieres/Q13 union satisfies `BMO-WL`: a located material,
> data, control and quality lineage covers development→raw supply→upstream→
> downstream→fill/finish→release→distribution with the provider of each stage
> and every cross-source stitch explicit.
> **Claim status:** active
> **Scope:** Frozen `BMO-WL` criterion across represented traditional-
> biologics/ATMP and Q13 continuous therapeutic-protein contexts; not one
> universal process, jurisdiction, implementation or complete enterprise
> retirement/recall model.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> §§New Risks Within the Growing Bioeconomy/Digital Information Flow in
> Biomanufacturing/Considerations for Emerging Biologic Products;
> Figures 1–2; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§1–4, printed pp. 1–14/physical pp. 6–19; Annex III §§1–3,
> printed pp. 27–30/physical pp. 32–35;
> [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md),
> `WFL-0003-C05/C06`.
> **Basis / limits:** All seven frozen stages and four flow/state classes are
> direct in the independent-source union. The normalized sequence does not
> claim that every represented branch occurs in one product or site.

## `BMO-XT` — both functional transfer directions

| Required full path | Located path | What it does not establish |
| --- | --- | --- |
| digital control/data→process/product | digital measurement/model/control or automation state → adjustment/pause/diversion/process action → physical material or product-quality state | malicious access, exploitability, occurrence or outcome |
| material/process-signal→digital release/control decision | input/material/equipment/process condition → sensor/PAT/test/model data → digital control, diversion, investigation or release decision | biological-input cyber incident or decision correctness |

Guttieres Figure 1 provides the explicit control/process coupling and Q13
provides direct monitoring/action and material/signal/quality-decision limbs.
`RSK-0002` preserves cyber origin as hypothetical and treats both directions as
functional dependencies, not as two observed incidents.

> **Claim record — SYN-0016-C04 | analytic-judgment**
> **Claim:** `BMO-XT` passes because Guttieres and Q13 independently support
> two complete functional paths—digital control/data→process/product and
> material/process-signal→digital release/control decision—and
> `WFL-0003/RSK-0002` preserve their distinct states and limits.
> **Claim status:** active
> **Scope:** Frozen bidirectional transfer-structure criterion; not a malicious
> technique, observed event, primary incident or evidenced consequence.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1 and §Digital Information Flow in Biomanufacturing;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1.4–3.1.7 and 4.1–4.2, printed pp. 4–10/physical pp. 9–15;
> Annex III §2.3, printed p. 29/physical p. 34; Annex V §§3.1–3.3,
> printed pp. 38–41/physical pp. 43–46;
> [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md),
> `WFL-0003-C06`; [RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md),
> `RSK-0002-C05`.
> **Basis / limits:** Both intended directions and intermediate state changes
> are direct. Functional corroboration does not satisfy the separate SF3
> incident/outcome or global observed-directionality requirements.

## `BMO-CT` — exact-edge control stitch

| Required limb | Generic OT layer | Sector quality layer | Exact bounded edge |
| --- | --- | --- | --- |
| architecture | NIST inventory, flow/boundary mapping, segmentation and pharmaceutical-DCS anchor | Q13 integrated equipment/PAT/model/control strategy | variable input/equipment/model state → unreliable process/control premise |
| access | NIST identity, authorization, remote-access and configuration controls | Q13 process/model justification and validation requirements | unauthorized change → altered control/data state |
| integrity monitoring | NIST passive monitoring, logging and baselines | Q13 PAT/sampling, trend/drift/data-gap, model and reference-test gates | hidden material/process state → detection/assessment |
| safety/quality gates | NIST safety/availability-aware tailoring and independent/manual constraints | Q13 acceptance criteria, pause, traceable diversion, offline testing and disposition | detected anomaly → bounded affected material |
| response | NIST OT-aware incident response and safe isolation | Q13 quarantine, investigation, root cause and CAPA | recognized condition → contained process/material state |
| trusted recovery | NIST verified restore, configuration/data validation and reconciliation | Q13 restart/collection criteria plus material disposition/release | restored digital state → trustworthy process/product re-entry |

The layers are complementary rather than interchangeable. NIST is not GMP or
quality-release guidance; Q13 is not cyber access, segmentation or trusted-
restore guidance. Their conjunction remains conditional on the actual
material↔signal↔model↔control boundary and on safe facility-specific response.

> **Claim record — SYN-0016-C05 | analytic-judgment**
> **Claim:** Independent NIST and ICH Q13 lineages satisfy `BMO-CT`: NIST
> supplies generic OT architecture/access/integrity-monitoring, safety-aware
> response and trusted restoration, while Q13 supplies continuous-
> manufacturing quality/diversion/disposition/release gates; the complementary
> functions map to exact `RSK-0002` process edges with prerequisites, failure
> modes and tradeoffs explicit.
> **Claim status:** active
> **Scope:** Frozen control-design criterion; not a complete `BMO-SD`
> architecture, regional compliance, implementation, successful test,
> effectiveness or independent evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.3, 2.4/Table 1, 4.2.2, 5.2.3, 5.4 and 6.1–6.5, printed
> pp. 19–21, 28–32, 55, 71–75, 83–138/PDF pp. 36–38, 45–49, 72,
> 88–92, 100–155;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1.1–3.1.7 and 4.1–4.9, printed pp. 2–12/physical pp. 7–17;
> Annex III §§2–3, printed pp. 28–30/physical pp. 33–35; Annex V
> §§3.1–3.3, printed pp. 38–41/physical pp. 43–46;
> [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md),
> `CTL-0011-C02/C05/C06`; [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md),
> `CTL-0015-C01`–`C06`; [RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md),
> `RSK-0002-C06`.
> **Basis / limits:** Each required limb and edge is located across two
> independent official/normative sources. Guttieres establishes sector
> applicability only; design and recommended states are not result evidence.

## Adjacent-cell and global-gate discipline

| Cell/gate | State after the four-cell decision | Why it does not change |
| --- | --- | --- |
| `BMO-ST` | Partial | industrial variants remain absent |
| `BMO-SD` | Partial | MES/LIMS/QMS-software/ERP and vendor/cloud/remote boundaries remain absent |
| `BMO-TV` | Partial | insider/supply coverage and concrete vulnerabilities/exposures remain incomplete |
| `BMO-CI` | Partial | no primary case or controlled consequence test is added |
| `BMO-AE` | Absent | no deployment, metric, comparator or independent evaluator is added |
| `BMO-GR` | Partial | ICH/FDA/EMA remain one technical lineage, not an independent two-jurisdiction GMP/data-integrity/OT-cyber reconciliation |
| global risk-chain | FAIL unchanged | one strengthened BMO path cannot complete every applied sector |
| global directionality | FAIL unchanged | functional design paths do not create the missing observed/corroborated global case evidence |
| global incident | FAIL unchanged | no `INC` or primary event is added |
| global controls | FAIL unchanged | no implementation/effectiveness/null-result portfolio is added |

> **Claim record — SYN-0016-C06 | analytic-judgment**
> **Claim:** The evidence supports only `BMO-AS/WL/XT/CT`; it cannot change
> `BMO-ST/SD/TV/CI/AE/GR`, another dimension or any global-gate pass/fail state
> because the missing industrial, enterprise-architecture, threat,
> event/outcome, evaluation and independent-governance predicates remain
> explicit.
> **Claim status:** superseded
> **Scope:** Frozen-rubric adjacency audit for this synthesis transaction; not
> a claim that the missing evidence does not exist outside the corpus.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0016-C01`–`C05`; current residuals in
> [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md),
> `SYS-0002-C06`; [RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md),
> assumptions/uncertainty and `RSK-0002-C05/C06`;
> [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md),
> `CTL-0015-C06`; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> `SRC-0031-C07/C09/C10`; frozen BMO cells/global gates in `SYN-0001`.
> **Basis / limits:** Every non-transition has a named missing predicate.
> Partial and Absent remain non-scoring and are not converted into claims of
> real-world absence.
> **Superseded by:** `SYN-0028-C03`–`C07`, which resolves industrial scope,
> threat/exposure, primary supply consequence and U.S.–UK governance while
> preserving the exact `BMO-SD/BMO-AE` residuals.

## Decision and score delta

Three independent read-only structural/locator, source/criterion and frozen-
rubric/semantic audits accept exactly these transitions:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `BMO-AS` | Partial | **Pass** | `SYN-0016-C02`: all nine literal asset/stakeholder classes across independent Guttieres/Q13 lineages |
| `BMO-WL` | Partial | **Pass** | `SYN-0016-C03`: all seven stages plus material/data/control/quality lineage across independent Guttieres/Q13 lineages |
| `BMO-XT` | Partial | **Pass** | `SYN-0016-C04`: both complete functional directions across independent Guttieres/Q13 lineages |
| `BMO-CT` | Partial | **Pass** | `SYN-0016-C05`: all six exact-edge generic-OT and sector-quality limbs across independent NIST/Q13 lineages |

No other cell changes. Because all four cells are critical, the critical-cell
distribution changes in parallel with the overall score:

| Result | Before SYN-0016 | After SYN-0016 |
| --- | ---: | ---: |
| Pass | 38 | **42** |
| Partial | 66 | **62** |
| Absent | 6 | **6** |
| Score | 38/110 (34.5%) | **42/110 (38.2%)** |
| BMO dimension | 0/10 | **4/10** |
| Critical cells | 35 Pass / 54 Partial / 2 Absent | **39 Pass / 50 Partial / 2 Absent** |
| Dimensions at least 9/10 | 1/11 | **1/11** |
| Global-gate pass/fail states | 7 Pass / 5 Fail | **unchanged: 7 Pass / 5 Fail** |

> **Claim record — SYN-0016-C07 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `BMO-AS`, `BMO-WL`,
> `BMO-XT` and `BMO-CT` as Partial→Pass, producing 42 Pass, 62 Partial and
> 6 Absent = 42/110 (38.2%), BMO 4/10 and 39/91 critical cells passed; no
> other cell, dimension-at-9 count or global-gate pass/fail state changes.
> **Claim status:** active
> **Scope:** Frozen rubric v1.0 decision for the `SYN-0016` transaction after
> three independent read-only audits; not absolute domain completeness,
> implementation, incident, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0016-C01`–`C06`; frozen `BMO-AS/WL/XT/CT` criteria,
> source floors and scoring method in
> [SYN-0001](syn-0001-coverage-rubric.md); prior zero-delta
> `SYN-0001-C26` checkpoint; independent structural/locator,
> source/criterion and semantic/frozen-rubric audits completed 2026-07-12.
> **Basis / limits:** Four Partial→Pass transitions yield the exact arithmetic;
> every adjacent missing predicate remains named in `SYN-0016-C06`. The audit
> decision changes evidence sufficiency only and creates no external event or
> safeguard result.

## Counterevidence, assumptions and confidence

- Guttieres is a 2019 Perspective with conceptual, non-exhaustive figures; it
  does not validate a facility, current prevalence or an attack path.
- NIST is generic OT guidance. Its pharmaceutical DCS mention anchors
  applicability but does not establish GMP, product disposition or a deployed
  biomanufacturing architecture.
- Q13 is one harmonized normative lineage. Its annex examples are illustrative
  and its FDA/EMA wrappers establish regional status, not independent technical
  corroboration, compliance, implementation or effectiveness.
- The row-to-row lifecycle and control conjunctions are editorial. Confidence
  is high in criterion coverage and low-to-unknown in deployment prevalence,
  attack likelihood and safeguard performance, which are outside these cells.
- The apparent FDA Annex V §3.3 internal cross-reference defect is preserved in
  `SRC-0031`; it does not alter the main ICH/EMA technical predicate used here.

## Implications and open questions

Passing these cells means the wiki can answer four structural questions with
traceable SF2 evidence: what assets/actors matter, how the lifecycle is
connected, how state moves in both directions and where design-level controls
interrupt the path. It does not mean the BMO dimension or domain is complete.

At this historical checkpoint, the next evidence priorities were industrial
scope, enterprise architecture, insider/supply/concrete exposures, a primary
consequence, evaluated safeguards and two-jurisdiction governance.
[SYN-0028](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)
subsequently resolves the industrial, exposure, primary supply-consequence and
U.S.–UK governance limbs. Literal QMS-as-software/ERP coverage and an
independently evaluated deployed safeguard remain open.

## Safety boundary

This synthesis retains only defensive class, dependency, state and control-
function mappings. It contains no product recipe, sequence, operating setpoint,
facility/network topology, credential, exploit path or reusable configuration.

## Related pages

- [AST-0007 — assets and stakeholders](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [WFL-0003 — development-to-distribution lineage](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [SYS-0002 — process-control system map](../systems/sys-0002-biomanufacturing-process-control.md)
- [RSK-0002 — bidirectional hypothetical path](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [CTL-0011 — generic OT control layer](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [CTL-0015 — Q13 quality-control layer](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [SYN-0007 — OT applicability and control stitch](syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0028 — subsequent BMO scope, threat, incident and governance reconciliation](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)
- [SYN-0001 — frozen acceptance rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
