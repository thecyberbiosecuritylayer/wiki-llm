---
id: RSK-0007
type: risk-scenario
title: Disruption of farm data or equipment access with production and supply effects
aliases:
  - smart-farm data-to-production disruption
  - farm access and supply-chain disruption scenario
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0010
  - SRC-0018
  - SRC-0032
  - SRC-0035
sensitivity: public
dual_use: low
origin_domain: digital
destination_domains:
  - physical
  - biological
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: RSK-0007-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-1, line 1475; #s1-4, line 1478; #s3-1, lines 1547–1556"
  - predicate: depends-on
    target: SYS-0005
    claim_id: RSK-0007-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475"
  - predicate: affects
    target: AST-0003
    claim_id: RSK-0007-C03
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-1, line 1475; #s1-4, line 1478; #s3-1, lines 1547–1556"
  - predicate: affects
    target: WFL-0007
    claim_id: RSK-0007-C03
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475; #s3-1, lines 1547–1556"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: RSK-0007-C05
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-1, #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§2.3.8, 5.3.3, 5.3.6–5.3.7 and 6.2.9–6.2.10, printed pp. 26–28, 81–82, 120–124 (PDF pp. 43–45, 98–99, 137–141)"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: RSK-0007-C06
    evidence:
      - source: SRC-0032
        locator: "Figure 2 and data layer, printed pp. 10 and 14–15 (physical pp. 16 and 20–21); remote-sensing/control paths, printed pp. 23–24 (physical pp. 29–30); Annex data architecture, printed pp. 48–57 (physical pp. 54–63); smart farming/forecasting/irrigation/data sharing, printed pp. 90–99 (physical pp. 96–105)"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: RSK-0007-C08
    evidence:
      - source: SRC-0035
        locator: "Main PDF Box 1, pp. 24–26, and pp. 27–35; APHA PDF pp. 3–7"
tags:
  - agriculture
  - smart-farming
  - data-integrity
  - availability
  - production-continuity
  - supply-chain
  - hypothetical
---

# Disruption of farm data or equipment access with production and supply effects

> [!WARNING]
> **Evidence classification**
> The central unsafe digital→production→supply scenario remains **strictly
> hypothetical and source-derived**. A separate PATH-SAFE/APHA record now
> directly shows a bounded biological-sample→laboratory-test/report direction,
> but not a hostile cyber trigger, GB disease consequence, incident, attack
> reconstruction, validated vulnerability, or likelihood estimate.

## Scenario

If a connected farm materially depends on monitoring data or digital access to
equipment, loss of availability or integrity in that digital state may alter or
interrupt a production decision or physical operation. If independent
observation, safe fallback, detection, response, and recovery do not interrupt
the path, the receiving production state may become degraded, interrupted, or
uncertain. A sufficiently prolonged or material production effect may create a
downstream supply interruption for agribusinesses and consumers.

This page does not describe an access route, exploit sequence, named farm,
specific device, configuration, operational setting, or method for bypassing
safeguards.

> **Claim record — RSK-0007-C01 | hypothesis**
> **Claim:** In a connected-farm context with a material digital dependency,
> unreliable monitoring data or loss of access to data or equipment may
> conditionally cross a decision/control boundary into production disruption
> and then into a downstream food-supply effect.
> **Claim status:** active
> **Scope:** Hypothetical smart-farm production segment; not all farms, devices,
> crops, livestock systems, or supply chains.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1`, lines 1472–1473; `#s1-1`, line 1475; `#s1-4`, line 1478;
> `#s3-1`, lines 1547–1556.
> **Basis / limits:** Source names connected monitoring, false sensor data,
> data/machinery access, production/harvest disruption and supply ripple
> concerns. The end-to-end chain is a wiki hypothesis assembled at defensive
> level; the source supplies no observed complete path, system validation,
> duration threshold, probability, control failure or independent confirmation.

## Assets and workflow

- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md) — crops,
  livestock, production output, monitoring/operational data, equipment and
  organizational capability within the source's bounded scope;
- [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md) — candidate
  digital origin and data/access dependency class;
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md) —
  conceptual monitoring→management/production→downstream-supply segment;
- producers/workers, agribusinesses, suppliers/vendors, downstream users and
  consumers as conditional stakeholders.

The original `SRC-0010` path does not model seeds, veterinary/plant
diagnostics, traceability, environmental monitoring, trade or disposition.
`SRC-0032` now supplies conceptual traceability, environmental observation and
value-chain system classes, but it does not turn them into an observed unsafe
path or add complete diagnostics/treatment/disposition evidence.

## Preconditions and trust boundaries

The scenario requires all of the following conditions:

1. monitoring data or digital equipment access materially informs or enables a
   production action rather than merely providing optional visibility;
2. the digital state becomes unavailable or unreliable for long enough to
   matter to that action;
3. operators cannot obtain sufficiently trustworthy independent information or
   use a safe, locally validated fallback;
4. detection, human review, isolation, response or recovery does not stop the
   state before it affects production;
5. the production effect is large or persistent enough to affect downstream
   product movement or availability.

These are analytic preconditions, not source-reported facts about an identified
farm. Candidate boundaries are monitoring input↔management decision, digital
access↔physical equipment, farm production↔supplier/vendor exchange, and
production output↔downstream supply. Their architecture and strength are
unvalidated.

## Origin-domain state

The digital origin state is one or both of:

- monitoring/operational data are unreliable, incomplete or unavailable; or
- legitimate users cannot access data or digitally dependent equipment needed
  for the bounded production segment.

Trigger, intent and mechanism remain unknown. `SRC-0010` mentions potential
cyberattack and ransomware classes but supplies no actor, event, technique,
vulnerability or non-adversarial hazard suitable for a standalone page.

> **Claim record — RSK-0007-C02 | source-report**
> **Claim:** Drape et al. present false sensor data, data and machinery access,
> and data encryption/ransomware as potential precision-agriculture risks and
> associate exploitation with possible production or harvest disruption.
> **Claim status:** active
> **Scope:** Author/literature framing of possible risk, not observed
> exploitation or a current farm vulnerability.
> **As of:** 2021-08-19.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, line 1475; `#s1-4`, line 1478.
> **Basis / limits:** Potential classes and consequences are explicit source
> statements. They rely substantially on cited prior literature and are not
> supported here by primary incident, device test, prevalence or causal data.

## Cross-domain transfer

Two high-level transfer mechanisms are possible:

- **data/decision:** unreliable monitoring state informs a farm-management or
  production decision;
- **availability/control:** unavailable legitimate access prevents or delays a
  digitally dependent physical production action.

The source does not establish which mechanism is present in any particular
configuration. Connectivity alone is insufficient: the scenario requires a
material influence on physical or biological production state.

## Intended reverse and forward functional paths

AU DAS supplies distinct intended non-adversarial functional paths that the
earlier workshop did not supply or validate. It is candidate claim-specific
independent evidence, not blanket-independent corroboration:

- environmental, plant, soil, water, weather or animal observation enters a
  digital system through satellite, drone, ground sensor or human input;
- data are transmitted, stored/processed and analyzed for forecast,
  pest/disease detection, advisory, alert or machine instruction;
- digital outputs can influence irrigation, fertilization, pesticide use,
  equipment operation, certification, market access, subsidy/voucher, credit
  or insurance decisions.

It also warns that erroneous/outdated data and weak metadata/validation can
lead to poor decisions. These are intended system and data-quality paths, not
a hostile trigger or observed cyber-biological consequence.

> **Claim record — RSK-0007-C06 | source-report**
> **Claim:** AU DAS directly documents a functional observation→digital
> analytics/surveillance decision direction and a digital advisory/control/
> record→physical or value-chain action direction in agriculture.
> **Claim status:** active
> **Scope:** Intended smart-farming, forecasting, irrigation, traceability and
> data-sharing functionality; not adversarial cyber→harm, a named farm,
> incident, universal automation or causal outcome.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> Figure 2 and data layer, printed pp. 10 and 14–15 (physical pp. 16 and
> 20–21); remote-sensing/control paths, printed pp. 23–24 (physical pp. 29–30);
> Annex data architecture, printed pp. 48–57 (physical pp. 54–63); smart
> farming, forecasting, irrigation and data sharing, printed pp. 90–99
> (physical pp. 96–105).
> **Basis / limits:** Input, processing, decision and action functions are
> direct. Combining use cases is editorial and proves neither hostile state,
> unsafe transfer, likelihood nor consequence.

> **Claim record — RSK-0007-C07 | analytic-judgment**
> **Claim:** Drape's potential loss-of-trust/access→production/supply hypothesis
> and AU DAS's distinct intended bidirectional functional paths make the
> intended transfer structure more completely specified, but they still do not
> corroborate a full
> cyber→animal/plant/ecosystem harm event or a reverse observed decision
> outcome.
> **Claim status:** active
> **Scope:** Evidence-strength judgment for `RSK-0007`; not a rubric pass,
> incident classification, likelihood estimate or claim that every AU use case
> is cyber-controllable.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2`; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C05/C06/C07`.
> **Basis / limits:** The lineages are institutionally distinct and support
> complementary risk/function predicates, but independence remains claim-
> specific because FAO/ITU participated and AU content cites/derives Figure 2,
> use-case and other background material. Neither provides a primary incident,
> system test, ecosystem outcome, hostile mechanism or control-failure trace.

## Receiving-domain state

The receiving state may be interrupted, delayed, reduced or uncertain crop/
livestock production or harvest. The scenario does not assert disease,
animal/plant injury, contamination, food-safety failure or ecosystem effect;
none is documented by this source.

## Immediate and downstream consequences

Potential immediate effects are operational delay, inability to complete a
production step, or uncertainty about a decision made from unreliable data.
Potential downstream effects are producer/business loss, interrupted movement
of products, supply imbalance or reduced availability to downstream users.

> **Claim record — RSK-0007-C03 | analytic-judgment**
> **Claim:** If the stated preconditions hold, loss of trusted data/access can
> affect the coupled digital, equipment and production assets in `AST-0003` and
> interrupt the bounded `WFL-0007` segment; extension into supply consequence
> remains conditional on severity, duration, fallback and downstream buffers.
> **Claim status:** active
> **Scope:** Conditional effect on the source-derived smart-farm model, not an
> empirical sector-wide consequence claim.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1`, lines 1472–1473; `#s1-1`, line 1475; `#s1-4`, line 1478;
> `#s3-1`, lines 1547–1556.
> **Basis / limits:** The source links connected monitoring, production and
> supply-chain concerns. Asset grouping, exact edges and propagation conditions
> are wiki analysis; no magnitude, reversibility, biological endpoint or
> observed causal sequence is supplied.

## Evidence

The evidence base now combines one 2021 peer-reviewed qualitative study whose
potential-risk statements partly summarize prior literature with one
distinct AU regional strategy describing intended functional
paths and data-quality risks. Workshop quotations, AU commercial examples and
strategy targets are not incident corroboration. Each package remains one
lineage regardless of its internal modalities or participating organizations.

No `INC`, `THR`, `HAZ`, `TEC` or `VUL` page is created. Direct empirical farm
studies, primary event records or controlled system tests are required before
raising this scenario above hypothesis.

## Controls by function

[CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
records source recommendations at high level:

- **identify/prepare:** map relevant data, equipment, responsibilities and
  operational dependencies and provide role-appropriate training;
- **detect/report:** establish proportionate monitoring, reporting and review
  for suspected loss of trustworthy state;
- **contain/respond:** use locally validated protocols and cross-functional
  escalation when a penetration or disruption is suspected;
- **recover:** preserve a trustworthy operational state and coordinate
  continuity without assuming one fallback fits every producer;
- **assure/improve:** use authorized, scoped assessment and incident learning.

All are **recommended only**. Implementation, testing, effectiveness and
independent evaluation are unknown.

AU DAS adds validation/metadata/interoperability, privacy/cybersecurity
standards, traceability, pest/disease early warning, cross-sector coordination
and resilience objectives. It still does not provide a complete cyber incident
response/recovery procedure, exact deployment, test or independent outcome.

> **Claim record — RSK-0007-C04 | analytic-judgment**
> **Claim:** The recommended capability/control families in `CTL-0005` can be
> mapped to the precondition, detection, transfer and response edges of this
> hypothesis, but `SRC-0010` does not show that any edge was actually interrupted.
> **Claim status:** active
> **Scope:** Defensive mapping to `RSK-0007`, not implementation or
> effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s3-2`, lines 1556–1565; Discussion `#s4`, lines 1693–1698;
> Recommendations `#s6`, lines 1702–1704.
> **Basis / limits:** Source proposals address readiness, detection/assessment,
> response and collaboration in general. No exact deployment, test, baseline,
> causal effect or independent assessment is available.

> **Claim record — RSK-0007-C05 | analytic-judgment**
> **Claim:** NIST's generic IIoT/remote-access and OT control guidance
> strengthens the bounded technical dependency/control model but does not
> corroborate the complete farm→production→supply chain or any observed event.
> **Claim status:** active
> **Scope:** Generic OT applicability to the existing hypothetical smart-farm
> segment; not One Health, topology, likelihood or harm evidence.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2` and Tables 1–2;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.8, 5.3.3, 5.3.6–5.3.7 and 6.2.9–6.2.10,
> printed pp. 26–28, 81–82, 120–124.
> **Basis / limits:** Technical classes/control functions are independent and
> direct; their relation to this scenario is editorial. Within the two sources
> cited by this claim, traceability, ecological/biological outcomes and field
> evidence remain absent; `SRC-0032` later adds conceptual traceability but no
> outcome or field validation.

## Observed reverse surveillance path

PATH-SAFE/APHA now supplies one bounded, non-adversarial reverse functional
path. Prior bulk-milk feasibility evidence and relationships supported a Defra
proposal and method-selection decision. The resulting separate survey used raw
bulk-milk samples supplied through voluntary processors, same-day RT-PCR and
weekly reports to chief veterinary officers/policy makers, producing a
time/design-bounded all-negative surveillance conclusion. It does not show
that the weekly reports caused another decision.

> **Claim record — RSK-0007-C08 | source-report**
> **Claim:** PATH-SAFE/APHA directly demonstrates a biological sample→
> laboratory result→policy-report→bounded surveillance-conclusion direction
> and prior evidence→method-selection decision, strengthening the reverse
> agriculture transfer path with field implementation.
> **Claim status:** active
> **Scope:** Great Britain bulk-milk H5N1 survey, 23 May–27 June 2024; not a
> hostile cyber→animal/plant/ecosystem path, disease detection, biological/
> economic harm, downstream decision caused by weekly reporting or incident.
> **As of:** 2024-06-27.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C05/C06`; main PDF Box 1, pp. 24–26; APHA PDF pp. 3–7.
> **Basis / limits:** The implemented field path and null result are direct
> across a commissioned evaluation and distinct primary APHA record in the same
> programme ecosystem. No cyber origin, affected receiving state or qualifying
> consequence is supplied, so the unsafe forward scenario remains hypothetical
> and `AGE-XT/CI` do not pass.

## Assumptions and uncertainty

- Likelihood: **not assessed**.
- Consequence: potential and farm/crop/livestock/supply-context dependent.
- Trigger, intent, actor, technique, vulnerability and attribution: unknown.
- Device/system architecture and actual digital-to-physical authority: unknown.
- Existing manual, human, biological, safety and supply buffers: not inventoried.
- Biological, food-safety, animal/plant-health and ecosystem outcomes: not
  established.
- Counterevidence: independent observations, fail-safe behavior, timely human
  review, local fallback or downstream inventory may stop or absorb propagation;
  the source does not evaluate them.

## Related scenarios

[RSK-0002](rsk-0002-biomanufacturing-control-integrity-disruption.md)
also models a digital-to-production path, but in biopharmaceutical manufacturing
with a different workflow, evidence base and quality/supply context. It is not
corroboration of this agricultural scenario.

## Related pages

- [SRC-0020 — U.S. National One Health Framework](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)

- [AST-0003 — Smart-farm production and supply assets](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007 — Smart-farm monitoring, production and supply segment](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYS-0005 — Connected smart-farm ecosystem](../systems/sys-0005-connected-smart-farm-ecosystem.md)
- [CTL-0005 — Agricultural cyberbiosecurity capability controls](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SRC-0010 — Drape et al. 2021](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0032 — AU Digital Agriculture Strategy](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [GOV-0017 — AU digital-agriculture governance](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0017 — Agriculture transfer/control/governance reconciliation](../syntheses/syn-0017-au-agriculture-transfer-control-governance-reconciliation.md)
- [HAZ-0003 — Non-adversarial sensor/data-quality hazard](../hazards/haz-0003-agriculture-sensor-and-data-quality-failure.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md), HTML
  `#s1`, `#s1-1`, `#s1-4`, `#s3-1`, `#s3-2`, `#s4` and `#s6`.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.8, 5.3, 6.2.9–6.2.10 and 6.3–6.5.
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
  printed pp. 10, 14–15, 23–24, 48–57 and 90–99.
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md), main PDF
  Box 1, pp. 24–26; APHA PDF pp. 3–7.
