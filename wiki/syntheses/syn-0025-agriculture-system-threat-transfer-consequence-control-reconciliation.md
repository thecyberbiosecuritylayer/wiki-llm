---
id: SYN-0025
type: synthesis
title: Agriculture lifecycle, system, threat, transfer, consequence and control reconciliation
aliases:
  - AGE WL SD TV XT CI CT reconciliation
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0010
  - SRC-0018
  - SRC-0032
  - SRC-0035
  - SRC-0037
  - SRC-0038
  - SRC-0039
  - SRC-0040
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: SYN-0025-C02
    evidence:
      - source: SRC-0032
        locator: "SRC-0032-C03–C07; printed pp. 4–24, 43–99 and 123–129"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: SYN-0025-C02
    evidence:
      - source: SRC-0035
        locator: "SRC-0035-C03–C08; main PDF pp. 13–35 and 43–49; Annex A; APHA PDF pp. 3–7"
  - predicate: evidenced-by
    target: SRC-0037
    claim_id: SYN-0025-C03
    evidence:
      - source: SRC-0037
        locator: "SRC-0037-C03–C09; animal/plant lifecycle and IMSOC architecture/control provisions"
  - predicate: evidenced-by
    target: SRC-0038
    claim_id: SYN-0025-C04
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03–C08; PDF pp. 1–4"
  - predicate: evidenced-by
    target: SRC-0039
    claim_id: SYN-0025-C06
    evidence:
      - source: SRC-0039
        locator: "SRC-0039-C02–C08; PDF pp. 2–4"
  - predicate: evidenced-by
    target: SRC-0040
    claim_id: SYN-0025-C06
    evidence:
      - source: SRC-0040
        locator: "SRC-0040-C02–C07; complete FBI statement"
  - predicate: depends-on
    target: WFL-0012
    claim_id: SYN-0025-C02
    evidence:
      - source: SRC-0037
        locator: "WFL-0012-C01/C02; SRC-0037-C04/C05"
      - source: SRC-0032
        locator: "SRC-0032-C04; production/value-chain lifecycle"
      - source: SRC-0035
        locator: "SRC-0035-C03/C05; environmental/sample surveillance lanes"
  - predicate: depends-on
    target: SYS-0012
    claim_id: SYN-0025-C03
    evidence:
      - source: SRC-0037
        locator: "SYS-0012-C01–C03; SRC-0037-C06/C09"
      - source: SRC-0032
        locator: "SRC-0032-C05; farm/remote/cloud/platform classes"
      - source: SRC-0035
        locator: "SRC-0035-C04/C05; laboratory/platform boundaries"
  - predicate: depends-on
    target: HAZ-0003
    claim_id: SYN-0025-C04
    evidence:
      - source: SRC-0010
        locator: "HAZ-0003-C01/C03; SRC-0010-C05"
      - source: SRC-0032
        locator: "HAZ-0003-C02/C03; SRC-0032-C06/C07"
  - predicate: depends-on
    target: HAZ-0004
    claim_id: SYN-0025-C04
    evidence:
      - source: SRC-0032
        locator: "HAZ-0004-C01/C02; SRC-0032-C03/C04/C07"
  - predicate: depends-on
    target: INC-0004
    claim_id: SYN-0025-C06
    evidence:
      - source: SRC-0039
        locator: "INC-0004-C01–C03/C07; USDA PDF pp. 2–4"
      - source: SRC-0040
        locator: "INC-0004-C04/C06/C07; complete FBI statement"
  - predicate: depends-on
    target: CTL-0017
    claim_id: SYN-0025-C07
    evidence:
      - source: SRC-0037
        locator: "CTL-0017-C01–C04; SRC-0037-C04–C09"
  - predicate: depends-on
    target: CTL-0018
    claim_id: SYN-0025-C07
    evidence:
      - source: SRC-0038
        locator: "CTL-0018-C01–C05; SRC-0038-C04/C05/C08"
tags:
  - agriculture
  - one-health
  - lifecycle
  - systems
  - threats
  - transfer
  - incidents
  - controls
  - reconciliation
---

# Agriculture lifecycle, system, threat, transfer, consequence and control reconciliation

## Decision scope

This synthesis audits exactly six frozen cells: `AGE-WL`, `AGE-SD`, `AGE-TV`,
`AGE-XT`, `AGE-CI` and `AGE-CT`. `AGE-AS` is excluded because `herd` remains a
literal unsupported/non-equivalent class. `AGE-AE` is excluded because no
complete deployed safeguard has an independent effectiveness assessment.
Existing `AGE-ST/GR` remain Pass and are not rescored.

> **Claim record — SYN-0025-C01 | artifact-observation**
> **Claim:** The input corpus before this synthesis is 67 Pass, 40 Partial and
> 3 Absent = 67/110, with AGE at 2/10; the transaction contains one new
> canonical incident, two separated hazard classes and one criterion-level
> synthesis but no new external source.
> **Claim status:** active
> **Scope:** Wiki state after active `SRC-0040` and before `SYN-0025`
> activation; not absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), current rows
> and post-`SRC-0040` checkpoint; registry/log; reserved transaction pages.
> **Basis / limits:** This is a reproducible filesystem/rubric observation.
> Derived pages reorganize existing evidence and cannot create independence.

## Evidence-role and independence matrix

| Role | Materially distinct lineages | Boundary |
| --- | --- | --- |
| Production/data lifecycle and farm systems | Drape U.S. academic; AU continental strategy | Conceptual/strategy, not one deployment |
| Environmental/sample surveillance | PATH-SAFE evaluation plus primary APHA record in one programme ecosystem | Bounded field implementation, not universal lifecycle |
| Animal/plant lifecycle and IMSOC | One EU legislative ecosystem | Binding/design, not implementation/effectiveness |
| Ransomware threat/exposures/controls | One FBI/CISA/USDA-coordinated 2022 advisory | Anonymous aggregated cases, one publication lineage |
| JBS throughput consequence | USDA ERS/AMS economic-data lineage | Direct consequence measure, not cyber forensics |
| JBS incident/attribution context | FBI National Press Office | Independent context, not independent throughput measurement |
| Generic OT cyber controls | NIST SP 800-82r3 | Independent generic layer, not agriculture deployment |

Independence is claim-specific. The two FBI publications differ in event and
purpose but remain U.S. federal cyber lineages; the JBS FBI statement and USDA
ERS report describe one event. PATH-SAFE evaluation/APHA roles are not blanket
independent replication. EU animal/plant/IMSOC texts are one legal ecosystem.

## `AGE-WL` — complete lifecycle

The joined lifecycle covers every literal criterion stage:

| Required stage | Located evidence | Non-equivalence retained |
| --- | --- | --- |
| Breeding/production | AU farm/breeding/value-chain; EU animal keeping and plant breeding/production | Strategy/legal functions, not one farm SOP |
| Diagnostics/surveillance | EU notification, sampling, official-lab examination/survey/testing; PATH-SAFE sample/test/report | Legal design versus bounded implementation kept separate |
| Treatment/movement | EU animal treatment/vaccination/restriction/movement and plant treatment/movement | Disease/species/derogation conditionality retained |
| Trade/traceability | AU farm-to-fork/identity; EU records, certificates, passports, TRACES | Conceptual versus binding scope retained |
| Environmental sampling | PATH-SAFE environmental/food workstreams and AU monitoring | Not silently equated with plant-health surveys |
| Disposition | EU slaughter/disposal/restoration and plant invalidation/destruction/disposition | No universal sequence or observed outcome |

> **Claim record — SYN-0025-C02 | analytic-judgment**
> **Claim:** Independent AU/PATH-SAFE and EU lineages jointly satisfy
> `AGE-WL` at SF2: breeding/production, diagnostics/surveillance, treatment/
> movement, trade/traceability, environmental sampling and disposition are all
> explicitly located and reconciled.
> **Claim status:** active
> **Scope:** Frozen AGE-WL lifecycle classes; not a universal SOP, complete
> custody record, implementation census or effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C04`; [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C03/C05`; [WFL-0012](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md),
> `WFL-0012-C01`–`C03`; `SRC-0037-C04/C05`.
> **Basis / limits:** Every literal is direct in at least one claim-appropriate
> source and the portfolio is materially independent. Source-specific ordering,
> force, object and implementation states are not collapsed.

## `AGE-SD` — systems, dependencies and boundaries

| Required class | Located evidence | Boundary |
| --- | --- | --- |
| Farm OT/IoT | AU connected equipment/automation and explicit IoT/SCADA; Drape farm equipment | Conceptual classes, no site topology |
| Veterinary/plant labs | EU official/reference laboratory networks and diagnostic dependencies; PATH-SAFE/APHA operational laboratory role | Functional network, not full LIMS/IAM topology |
| Remote sensing | AU satellite/drone/GPS/GIS/ground-sensor stack | No calibration/performance validation |
| Traceability/surveillance platforms | AU registries/traceability/early warning; EU iRASFF/ADIS/EUROPHYT/TRACES; PATH-SAFE platform | Different jurisdictions/purposes retained |
| Boundaries | edge↔network/cloud, offline↔sync, owner↔platform/user, national↔regional, lab↔reporting, component↔national/external system, role/access and outage reconciliation | Legal/functional/observed boundaries, not one validated trust-zone design |

> **Claim record — SYN-0025-C03 | analytic-judgment**
> **Claim:** `SYS-0005/SYS-0012` plus independent AU, PATH-SAFE and EU source
> roles satisfy `AGE-SD` at SF2 across farm OT/IoT, veterinary/plant
> laboratories, remote sensing, traceability/surveillance platforms and
> explicit organizational/data/system boundaries.
> **Claim status:** active
> **Scope:** Complete functional system-class map; not a deployed reference
> architecture, endpoint inventory, validated IAM/topology or performance test.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md),
> `SYS-0005-C01`–`C05`; [SYS-0012](../systems/sys-0012-eu-animal-plant-health-imsoc-architecture.md),
> `SYS-0012-C01`–`C04`; `SRC-0032-C05`; `SRC-0035-C04/C05`;
> `SRC-0037-C06/C09`.
> **Basis / limits:** Every literal component and boundary class is direct at
> functional level across materially independent lineages. Validation is not a
> criterion literal and is explicitly not inferred.

## `AGE-TV` — separated threat/hazard/vulnerability corpus

| Required class | Canonical page/source | Boundary |
| --- | --- | --- |
| Adversarial | `THR-0002` / FBI agriculture ransomware advisory | Generic criminal ransomware, no event multiplication |
| Accidental | `HAZ-0003` / AU direct | False/erroneous/outdated sensor/data state; Drape's hacker-exploitation path does not corroborate this label |
| Ecological | `HAZ-0004` / AU | Climate/weather, pest/disease and environmental-resource hazards, not cyber |
| Supply | `HAZ-0004`, `SRC-0038` | Natural/organizational supply risks versus cyber-conditioned cascades separated |
| Sensor/data integrity | `HAZ-0003` / Drape + AU | Data-quality/decision path, not validated field failure |
| Vulnerabilities/exposures | `VUL-0002` / FBI advisory | Unpatched known weakness, shared-resource and managed-service classes; no product/exploit detail |

> **Claim record — SYN-0025-C04 | analytic-judgment**
> **Claim:** `THR-0002`, `HAZ-0003/0004` and `VUL-0002` satisfy `AGE-TV` at
> SF2 by separating adversarial, accidental, ecological, supply, sensor/data-
> integrity and concrete exposure classes and linking them to agriculture
> assets/workflows: AU supplies accidental/data-quality, ecological and supply
> risks; Drape supplies a sensor/data-integrity transfer risk in an adversarial
> hacker-exploitation context; the FBI advisory supplies ransomware and
> concrete exposure classes.
> **Claim status:** active
> **Scope:** Defensive sector taxonomy; not prevalence, likelihood, current
> affected-product inventory, exploitability or empirical occurrence of every
> class.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md),
> `THR-0002-C01`–`C03`; [HAZ-0003](../hazards/haz-0003-agriculture-sensor-and-data-quality-failure.md),
> `HAZ-0003-C01`–`C03`; [HAZ-0004](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md),
> `HAZ-0004-C01/C02`; [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md),
> `VUL-0002-C01`–`C03`; `SRC-0032-C07`; `SRC-0038-C03`–`C07`.
> **Basis / limits:** Required classes are literal, role-specific and non-
> equivalent across independent AU, Drape and FBI-advisory lineages. Drape does
> not independently corroborate the accidental label; typed pages plus asset/
> workflow relations make the portfolio queryable without assigning unsupported
> intent.

## `AGE-XT` — strong evidence but literal effect gap

The reverse direction is independently complete: AU maps biological,
environmental and sensor observations through transmission/analytics into
surveillance/advisory/control decisions; PATH-SAFE/APHA directly implements a
sample→laboratory test/result→weekly surveillance-report lane.

The hostile forward direction is now concrete at safe abstraction:

- Drape supplies false-data/access→production/harvest→supply potential;
- the agriculture advisory supplies ransomware→availability→manual/slower or
  halted production and conditional processor/farm/animal-processing pressure;
- `INC-0004` supplies an observed cyberattack→nine-plant closure→two-day
  cattle-slaughter/processing-throughput effect with materially independent FBI
  incident/attribution context.

> **Claim record — SYN-0025-C05 | analytic-judgment**
> **Claim:** Independent AU/PATH-SAFE and Drape/FBI-advisory/JBS lineages
> complete the biological/environmental/sensor-input→digital surveillance/
> decision direction and a hostile cyber→cattle-processing-throughput limb,
> but no represented source completes the frozen cyber→animal/plant/ecosystem-
> effect literal; `AGE-XT` therefore remains Partial.
> **Claim status:** superseded
> **Scope:** Strong directional candidate evidence at safe abstraction; not an
> animal health/welfare, plant or ecosystem effect, universal automation,
> likelihood, exact malicious technique or farm-to-consumer outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0032-C06`; `SRC-0035-C03/C05/C06`;
> [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md),
> `RSK-0007-C01/C04/C05/C08`; [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md),
> `RSK-0017-C01`–`C04`; [INC-0004](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md),
> `INC-0004-C01`–`C04/C07`.
> **Basis / limits:** The reverse direction is complete and the hostile
> operational limb has input, transfer and processing-throughput consequence
> nodes across independent roles. Processing throughput is not silently
> upgraded to an animal/plant/ecosystem effect.
> **Superseded by:** `SYN-0027-C05`; the AAFC account supplies the missing
> source-reported animal-effect limb and `AGE-XT` now passes at SF2.

## `AGE-CI` — observed consequence with independent context

`INC-0004` is one event. USDA ERS directly reports the cyberattack/plant-
closure/two-day cattle-slaughter consequence and supplies AMS actual-and-
estimated national throughput context. The FBI independently confirms the JBS
incident and attribution context but does not confirm the USDA figures.

> **Claim record — SYN-0025-C06 | analytic-judgment**
> **Claim:** `INC-0004` satisfies `AGE-CI` at SF3: a direct official USDA
> event/economic-data record documents an observed food-processing/cattle-
> slaughter throughput consequence, and a materially independent FBI lineage
> supplies incident/attribution context with source roles and non-confirmed
> consequences explicit.
> **Claim status:** active
> **Scope:** One JBS event and bounded processing-throughput outcome; not two
> incidents, independent consequence replication, finished-food shortage,
> animal injury, isolated loss, price causality or control effectiveness.
> **As of:** Event 2021-05-30 through 2021-06-03; reconciled 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0004](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md),
> `INC-0004-C01`–`C07`; `SRC-0039-C02`–`C08`; `SRC-0040-C02`–`C07`.
> **Basis / limits:** USDA is direct and claim-appropriate for the measured
> consequence. `AGE-CI` requires independent context and SF3 requires
> independent confirmation/evaluation; FBI independently confirms the JBS
> incident/attribution context, while USDA remains the sole consequence
> measurement.

## `AGE-CT` — exact sector-edge control stitch

| Required function | Exact agriculture edge | Source/control role |
| --- | --- | --- |
| Biosecurity | operator prevention, registration, movement and critical-point measures | EU `CTL-0017` binding design |
| Cyber | maintenance/access/segmentation/monitoring and generic OT overlay | FBI advisory `CTL-0018`; NIST `CTL-0011`; Drape/AU `CTL-0005` |
| Traceability | animal/group/establishment, plant lot/operator, certificate/passport/TRACES records | EU `CTL-0017`; AU `CTL-0005` |
| Detection | surveillance/sampling/lab confirmation; cyber monitoring/reporting | EU/PATH-SAFE `CTL-0017/0005`; FBI `CTL-0018` |
| Response | restriction/treatment/containment/notification plus cyber containment/manual continuity | EU `CTL-0017`; FBI `CTL-0018` |
| Resilience/recovery | continued surveillance/restoration, IMSOC outage reconciliation, protected backup/recovery planning | EU `CTL-0017`; FBI `CTL-0018`; NIST `CTL-0011` |

> **Claim record — SYN-0025-C07 | analytic-judgment**
> **Claim:** `CTL-0005/0011/0017/0018` satisfy `AGE-CT` at SF2 by reconciling
> independent agriculture biosecurity, cyber, traceability, detection,
> response and resilience/recovery functions to exact `WFL-0007/0012` and
> `RSK-0007/0017` edges.
> **Claim status:** active
> **Scope:** Complete exact-edge control design; not deployment, compliance,
> trusted restoration, test, interrupted-event causality or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md),
> `CTL-0005-C01`–`C07`; [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md);
> [CTL-0017](../controls/ctl-0017-animal-plant-health-traceability-notification-response-controls.md),
> `CTL-0017-C01`–`C04`; [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md),
> `CTL-0018-C01`–`C05`.
> **Basis / limits:** Every criterion function is mapped to a named sector edge
> across materially independent academic, AU, EU, FBI-advisory and NIST roles.
> Assurance/effectiveness stays in `AGE-AE` and is not required for this cell.

## Remaining AGE and cross-cutting gaps

- `AGE-AS` remains Partial: seeds, genomes, pathogens, samples, equipment,
  traceability/model data and actor/ecosystem classes are strong, but `herd`
  remains neither directly represented nor safely equivalent to EU animal-
  group/establishment/epidemiological-unit records.
- `AGE-XT` remains Partial: reverse input→digital decision and hostile
  cyber→processing throughput are strong, but the literal animal/plant/
  ecosystem effect is absent.
- `AGE-AE` remains Partial: PATH-SAFE has bounded implementation and method/
  design metrics, but no complete safeguard has independent outcome-
  effectiveness evaluation.
- `THI-CI` remains Partial: `INC-0004` adds one distinguishable event and AGE
  sector role, bringing the corpus to at most four primary-supported events
  across three sector classes, below six/four.
- `CTR-CI` remains Partial: JBS supplies no scoped control-failure/recovery
  implementation lesson because no control is linked to the result.
- Global incident, control and critical-coverage gates therefore remain Fail.

> **Claim record — SYN-0025-C08 | analytic-judgment**
> **Claim:** `AGE-AS/XT/AE`, `THI-WL/SD/CI/CT/AE`, `CTR-CI/AE` and the related
> global gates remain open; JBS counts once, supplies no independent consequence
> replication and supplies no effectiveness example.
> **Claim status:** superseded
> **Scope:** Explicit non-promotions and remaining floors after this synthesis.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0025-C01`–`C07`; frozen AGE/THI/CTR criteria and global
> gates in [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Missing literals, counts, independent evaluation and
> source-role limits are explicit. No Partial earns a point.
> **Superseded by:** `SYN-0026-C05/C06`; `AGE-AS/AE` now pass, while
> `AGE-XT`, adjacent count floors and global gates remain open.

## Score decision

> **Claim record — SYN-0025-C09 | artifact-observation**
> **Claim:** Strict review accepts exactly five Partial→Pass transitions:
> `AGE-WL`, `AGE-SD`, `AGE-TV`, `AGE-CI` and `AGE-CT`. Totals become 72 Pass,
> 35 Partial and 3 Absent = 72/110 (65.5%); AGE becomes 7/10 and critical cells
> become 61 Pass, 29 Partial and 1 Absent. Dimensions at least
> 9/10 remain 2/11 and global gates remain 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Wiki after active `INC-0004`, `HAZ-0003/0004` and `SYN-0025`;
> not external-domain completeness or a transition for any adjacent cell.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0025-C01`–`C08`; exact frozen criteria/source floors;
> post-activation structural and rubric lint; independent audits required
> before activation.
> **Basis / limits:** Five complete critical contracts move. `AGE-AS/XT/AE` and
> every enumerated cross-cutting gap remain Partial; no global gate moves.

## Safety boundary

> **Claim record — SYN-0025-C10 | analytic-judgment**
> **Claim:** The synthesis remains defensive and contains no farm/facility
> topology, operating parameter, biological procedure, indicator, access path,
> exploit, product-specific weakness, target identity beyond the public JBS
> event or recovery procedure.
> **Claim status:** stale
> **Scope:** Local synthesis content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content and source safety boundaries.
> **Limits:** Only high-level public classes, evidence roles and criterion
> decisions are retained. This is a local page-content assertion, not an
> externally evidenced decision claim, so it is retained as a safety note but
> is no longer maintained as active evidence.

## Related pages

- [SYN-0026](syn-0026-us-animal-disease-traceability-herd-assurance-reconciliation.md)
- [SYN-0027](syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md)
- [SYN-0001](syn-0001-coverage-rubric.md)
- [INC-0004](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md)
- [HAZ-0003](../hazards/haz-0003-agriculture-sensor-and-data-quality-failure.md)
- [HAZ-0004](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md)
- [WFL-0012](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md)
- [SYS-0012](../systems/sys-0012-eu-animal-plant-health-imsoc-architecture.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0017](../controls/ctl-0017-animal-plant-health-traceability-notification-response-controls.md)
- [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md)
- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md)
- [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md)
- [SRC-0040](../sources/src-0040-fbi-statement-jbs-cyberattack-2021.md)
