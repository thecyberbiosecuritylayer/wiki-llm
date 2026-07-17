---
id: SYN-0017
type: synthesis
title: AU agriculture transfer, control and governance reconciliation
aliases:
  - AGE XT CT GR reconciliation
  - AU DAS One Health cyber-data reconciliation
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0010
  - SRC-0018
  - SRC-0020
  - SRC-0021
  - SRC-0032
  - SRC-0035
sensitivity: public
dual_use: low
jurisdictions:
  - Global guidance
  - United States
  - African Union regional strategy
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: SYN-0017-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-1/#s1-4, lines 1475/1478; #s3-1–2, lines 1547–1565; #s4/#s6, lines 1693–1704"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYN-0017-C01
    evidence:
      - source: SRC-0018
        locator: "§§2.3.8, 5.3.3, 5.3.6–5.3.7, 6.2.9–6.2.10 and 6.3–6.5, printed pp. 26–28, 81–82 and 120–138"
  - predicate: evidenced-by
    target: SRC-0020
    claim_id: SYN-0017-C01
    evidence:
      - source: SRC-0020
        locator: "Executive Summary/Purpose and Scope, PDF pp. 3–7; Goals 3–6, pp. 10–12; Conclusion, p. 13"
  - predicate: evidenced-by
    target: SRC-0021
    claim_id: SYN-0017-C01
    evidence:
      - source: SRC-0021
        locator: "Executive Summary and §§1.1–1.5, printed pp. ix–x and 2–11 (physical pp. 9–10 and 12–21); Pathways 1–3, printed pp. 18–22 (physical pp. 28–32)"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: SYN-0017-C01
    evidence:
      - source: SRC-0032
        locator: "Scope/data/system paths, printed pp. 4–24 and 43–68 (physical pp. 10–30 and 49–74); action packages, printed pp. 81–99 (physical pp. 87–105); Objectives B–F, printed pp. 121–129 (physical pp. 127–135)"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: SYN-0017-C07
    evidence:
      - source: SRC-0035
        locator: "Main PDF pp. 18–49; APHA PDF pp. 3–7; SRC-0035-C05–C10"
tags:
  - agriculture
  - one-health
  - cross-domain-transfer
  - controls
  - governance
  - evidence-reconciliation
---

# AU agriculture transfer, control and governance reconciliation

## Question and strict method

This synthesis originally tested only the frozen `AGE-XT`, `AGE-CT` and
`AGE-GR` contracts after `SRC-0032`; `SYN-0017-C07` now reconciles its current
status after `SRC-0035` without rewriting the historical decision. It does not
reward source volume, terminology overlap or better description. A cell passes
only if every literal limb is located, its floor is met and the reconciliation
preserves intended function versus hostile path, agriculture early warning
versus cyber detection, strategy/guidance versus national law, and design
versus implementation or effectiveness.

Six source IDs represent different evidence roles, not automatically six
independent lineages:

| Evidence line | Claim-appropriate role | Independence boundary |
| --- | --- | --- |
| Drape (`SRC-0010`) | academic/workshop agriculture cyber-risk hypothesis and capability proposals | distinct from the official instruments; potential statements partly synthesize prior literature |
| NIST (`SRC-0018`) | generic current OT component/control functions | independent technical line, but agriculture applicability is editorial and not a sector outcome |
| U.S. NOHF (`SRC-0020`) | current U.S. One Health coordination/surveillance/laboratory programme design | one coordinated U.S. government lineage, not implementation or national law |
| Quadripartite (`SRC-0021`) | global One Health country-implementation guidance and data/surveillance design | one joint WHO/FAO/UNEP/WOAH lineage, not four or a second national jurisdiction |
| AU DAS (`SRC-0032`) | African regional agriculture/data/cyber strategy, system/use-case and action-plan design | one AUC/PRIDA package; FAO/ITU participation and derivative/cited material require claim-specific independence |
| UK PATH-SAFE (`SRC-0035`) | primary APHA field-survey/application plus commissioned FSA/RAND programme evaluation and current issuer status | delivery, evaluation and issuer roles are distinguishable but do not automatically create independent safeguard replication/effectiveness |

> **Claim record — SYN-0017-C01 | analytic-judgment**
> **Claim:** The six packages supply distinct claim-appropriate academic,
> generic-OT, U.S. One Health, global One Health, AU regional-strategy and UK
> field-application/evaluation roles, but independence is adjudicated per
> predicate and coordinated/derivative material is never multiplied.
> **Claim status:** active
> **Scope:** Provenance and normalization for `AGE-XT/CT/GR`; not blanket
> independence for outcomes, controls, laws or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> bibliographic/method/limitations and `SRC-0010-C09`;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> identity/scope and `SRC-0018-C01/C08/C09`;
> [SRC-0020](../sources/src-0020-us-national-one-health-framework-2025-2029.md),
> `SRC-0020-C01/C02/C10`; [SRC-0021](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md),
> `SRC-0021-C01/C02/C10`; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C01/C02/C08/C09`;
> [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C01/C02/C05/C08`.
> **Basis / limits:** Issuers, methods, geography and evidence roles are direct.
> Shared participants, citations, derivative figures and programme coordination
> are explicit limits on claim-specific independence.

## `AGE-XT` — intended directions do not complete a cyber/untrusted-state path

| Required path | Located nodes/edges | Evidence class and missing predicate |
| --- | --- | --- |
| Biological/environmental/sensor input→digital control/surveillance decision | AU: plant/soil/water/weather/animal or sensor/human input→network/database/cloud→analytics→forecast, pest/disease detection, advisory, alert or machine instruction (`SRC-0032-C06`); U.S./Quadripartite add environmental/surveillance data→models/early-warning decisions (`SRC-0020-C06`, `SRC-0021-C07/C08`) | direct intended functional design at SF2 through AU plus independent U.S. NOHF; no observed decision outcome or validated system, which are limits rather than `AGE-XT` requirements |
| Cyber/untrusted digital state→animal/plant effect | Drape: false sensor data, data/machinery access and ransomware are potential classes→production/harvest/supply disruption (`SRC-0010-C04/C05`, `RSK-0007-C01/C02`); AU shows a separate intended digital-output→farm-action dependency (`SRC-0032-C06`) | joining potential cyber state to AU decision/control authority is editorial; no directly linked cyber/untrusted-state→farm decision/control authority→explicit animal/plant receiving-state path reaches claim-appropriate SF2 |
| Cyber/untrusted digital state→ecosystem effect | AU names environmental/resource state and irrigation/application decisions; Drape does not model ecosystem outcome | missing complete cyber/untrusted-state origin→transfer→ecosystem receiving-state path |

> **Claim record — SYN-0017-C02 | analytic-judgment**
> **Claim:** The corpus now directly specifies the reverse biological/
> environmental/sensor-input→digital decision function and the intended
> digital-output→farm-action dependency, but `AGE-XT` remains Partial because
> no directly linked cyber/untrusted-state→farm decision/control authority→
> explicit animal/plant/ecosystem receiving-state path reaches claim-
> appropriate SF2.
> **Claim status:** active
> **Scope:** Frozen `AGE-XT` only; not denial that such events could occur or a
> likelihood/consequence estimate.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md),
> `RSK-0007-C01/C02/C06/C07`; [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> `SRC-0010-C04/C05`; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> `SRC-0018-C04`; [SRC-0020](../sources/src-0020-us-national-one-health-framework-2025-2029.md),
> `SRC-0020-C06`; [SRC-0021](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md),
> `SRC-0021-C07/C08`; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C05/C06/C07` and exact locators above.
> **Basis / limits:** AU intended functions and Drape potential-risk statements
> are direct source reports; the `RSK-0007` path and their joining are
> editorial. NIST generic OT consequence categories do not validate an
> agriculture-specific endpoint. Connectivity and decision relevance do not
> prove untrusted-state control or an explicit biological/ecosystem receiving
> state. An
> observed event/test is not required by SF2 `AGE-XT`; its absence remains an
> incident/effectiveness limitation rather than the scoring blocker here.

## `AGE-CT` — complementary design without a complete exact-edge stitch

| Frozen control limb | Located evidence | Exact-edge limit |
| --- | --- | --- |
| Biosecurity | U.S. NOHF laboratory biosafety/biosecurity and sample goals; Quadripartite health/ecological action/data tracks | decisive gap: no direct biological-biosecurity safeguard maps to a named animal/plant/ecosystem, production or value-chain edge in `RSK-0007` |
| Cyber | Drape training/monitoring/response proposals plus NIST generic OT architecture/access/integrity/response/recovery | conditionally maps to monitoring-input↔management-decision and digital-access↔physical-equipment edges; NIST remains generic/editorially applied and no agriculture-specific cyber baseline is established |
| Traceability | AU farmer/animal identity, registries, certification and farm/value-chain traceability | no explicit traceability-control mapping to the named farm↔supplier/vendor and production-output↔downstream-supply boundaries |
| Detection | Drape monitoring/reporting plus NIST logging/passive monitoring | conditionally maps to `RSK-0007` precondition 4/loss-of-trust detection edge; AU/Quadripartite climate/pest/disease early warning is a separate agriculture function, not cyber detection |
| Response | Drape locally appropriate protocols plus NIST safety-aware incident response | conditionally maps to `RSK-0007` precondition 4/transfer-response edge, but no biological-biosecurity response control maps to a named agriculture edge |
| Resilience | NIST-derived restoration/recovery mapping plus Drape continuity/learning and AU infrastructure/resilience objectives | fallback/restoration/continuity maps to `RSK-0007` preconditions 3–4 and `CTL-0005-C02` recovery/learning edge; agriculture-specific detail remains thin |

> **Claim record — SYN-0017-C03 | analytic-judgment**
> **Claim:** Drape, NIST, U.S./global One Health and AU sources cover all six
> control labels at high level, but `AGE-CT` remains Partial because
> a biological-biosecurity safeguard is not mapped to a named agriculture edge
> and traceability lacks an explicit control-to-boundary mapping. Cyber
> detection remains separate from
> agricultural early warning; the sector recovery stitch remains thin.
> **Claim status:** active
> **Scope:** Frozen `AGE-CT`; not implementation, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md),
> `CTL-0005-C01/C02/C04/C05/C06`;
> [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md),
> `CTL-0011-C01/C04/C05/C06/C07`;
> [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md),
> Preconditions and trust boundaries, conditions 3–5 and four named
> boundaries; `RSK-0007-C04/C05`;
> [SRC-0020](../sources/src-0020-us-national-one-health-framework-2025-2029.md),
> `SRC-0020-C07/C08`; [SRC-0021](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md),
> `SRC-0021-C07`–`C09`; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C07/C08`.
> **Basis / limits:** Labels and generic/recommended functions are direct.
> Planned/recommended state is preserved but is not itself an `AGE-CT` failure;
> the blockers are literal biosecurity/traceability completeness and exact-
> edge mapping. SF2 applies to the cell-level reconciliation rather than every
> limb independently; implementation/effectiveness belongs to `AGE-AE`.

## `AGE-GR` — regional strategy does not complete a two-jurisdiction portfolio

| Required governance limb | Located evidence | Missing reconciliation predicate |
| --- | --- | --- |
| Current One Health animal/plant/environment scope | current-presented U.S. NOHF plus global Quadripartite guide reconcile scope in `SYN-0009` | U.S. NOHF is coordination/programme design; global guidance is not a second jurisdiction |
| Current cyber/data instrument | AU DAS has current presentation and proposed data-quality/privacy/cyber/traceability actions | AU DAS is an African regional strategy, not organized under One Health and no legal force/national adoption is established |
| At least two jurisdictions | United States is one definite jurisdiction; AU supplies a regional strategy context and the Quadripartite supplies global guidance | global guidance is not a jurisdiction; AU legal/adoption status and non-One-Health framing do not establish a second qualifying jurisdictional instrument line |
| Reconciled applicability/status | source pages distinguish strategy, guidance, programme, dates, roles and adoption gaps | no full two-jurisdiction One Health applicability/force/adoption/exception comparison exists |

> **Claim record — SYN-0017-C04 | analytic-judgment**
> **Claim:** AU DAS adds a distinct African regional agriculture/data/cyber
> policy line to the U.S./global One Health corpus, but `AGE-GR` remains Partial
> because the corpus lacks a second qualifying jurisdictional instrument line
> and does not
> collectively reconcile a complete animal/plant-health, environmental and
> cyber/data instrument portfolio under One Health across two jurisdictions.
> **Claim status:** active
> **Scope:** Frozen `AGE-GR`; not a claim that AU digital agriculture is
> unrelated to One Health or that national instruments do not exist externally.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [GOV-0010](../governance/gov-0010-us-national-one-health-framework-2025-2029.md),
> `GOV-0010-C01`–`C06`; [GOV-0011](../governance/gov-0011-quadripartite-one-health-jpa-national-guide.md),
> `GOV-0011-C01`–`C06`; [GOV-0017](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md),
> `GOV-0017-C01`–`C05`; [SYN-0009](syn-0009-global-us-one-health-scope-reconciliation.md),
> `SYN-0009-C01`–`C03`.
> **Basis / limits:** Current presentation and modality/status distinctions are
> direct. The frozen grammar requires collective class coverage across at least
> two qualifying jurisdictions, not every class duplicated in each. Treating
> global guidance or an AU strategy with unestablished jurisdictional adoption
> and no One Health framing as the second qualifying jurisdictional instrument
> line would relax it.

## Non-equivalence and strict score decision

The original synthesis did not revisit `AGE-AS/WL/SD`; PATH-SAFE now fills
several of those historical gaps. Current remaining blockers are seed assets/
complete herd records and full actor/inventory reconciliation; treatment,
regulated movement, formal recall/disposition/end-of-life and one joined
custody lifecycle; and complete veterinary/plant-laboratory architecture, IAM/
topology and validated boundaries. `AGE-TV` still lacks a concrete adversarial/
vulnerability corpus. `AGE-CI` now has a primary null survey but no qualifying
consequence with independent empirical confirmation, and `AGE-AE` has bounded
implementation/evaluation but no qualifying independent effectiveness result.

> **Claim record — SYN-0017-C05 | analytic-judgment**
> **Claim:** `AGE-AS/WL/SD/TV/XT/CT/GR` remain Partial and `AGE-CI/AE` remain
> Absent after strict AU reconciliation; source breadth and intended functions
> do not substitute for literal missing predicates or evidence floors.
> **Claim status:** superseded
> **Scope:** Current AGE sufficiency under frozen rubric v1.0; absence means
> absent from this corpus, not from the external field.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0017-C01`–`C04`; current AGE rows and criteria in
> [SYN-0001](syn-0001-coverage-rubric.md); independent read-only
> `AGE-AS/WL/SD` and `AGE-XT/CT/GR` audits completed 2026-07-12.
> **Basis / limits:** Each missing limb is explicit and no `Partial` earns a
> binary point.
> **Superseded by:** `SYN-0017-C07` after complete `SRC-0035` integration.

> **Claim record — SYN-0017-C06 | artifact-observation**
> **Claim:** Strict reconciliation accepts zero Partial→Pass transitions, so
> the score remains 42 Pass, 62 Partial and 6 Absent = 42/110 (38.2%), AGE
> remains 1/10 and every global-gate state is unchanged.
> **Claim status:** superseded
> **Scope:** Wiki filesystem after active `SYN-0017`; not absolute domain
> completeness or an external evidence claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0017-C01`–`C05`; prior `SYN-0001-C28`; frozen 110-cell
> rubric and independent strict reviews.
> **Basis / limits:** No cell transition means no arithmetic change; all
> strengthened Partial predicates remain recorded for source selection.
> **Superseded by:** `SYN-0017-C07`; this remains the correct historical
> post-`SYN-0017`, pre-`SRC-0033` checkpoint.

## Current status after PATH-SAFE

> **Claim record — SYN-0017-C07 | analytic-judgment**
> **Claim:** The original zero-promotion decision for `AGE-XT/CT/GR` remains
> valid after PATH-SAFE: each retains at least one decisive literal/SF2 gap.
> `SRC-0035` separately moves `AGE-CI/AE` from Absent to Partial, so the current
> corpus is 46 Pass, 61 Partial and 3 Absent = 46/110 (41.8%), with AGE at
> 1/10 and no new Pass or global-gate change.
> **Claim status:** superseded
> **Scope:** Current status reconciliation for this formerly pre-PATH-SAFE
> synthesis; not a new source-transaction promotion, incident, qualifying
> consequence or effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C05`–`C10`; [SYN-0001](syn-0001-coverage-rubric.md),
> `SYN-0001-C33`; `SYN-0017-C02`–`C04`.
> **Basis / limits:** PATH-SAFE adds a primary reverse field path and bounded
> biological-surveillance controls/evaluation but no hostile cyber→animal/
> plant/ecosystem path, complete cyber-response/recovery and traceability-
> boundary stitch, or second qualifying jurisdictional One Health portfolio.
> Historical `SYN-0017-C05/C06` are retained but superseded for current state.
> **Superseded by:** `SYN-0017-C08` after active `SYN-0019` UK–U.S. governance
> reconciliation.

## Current status after UK–U.S. One Health governance reconciliation

This section records the pre-`SYN-0025` checkpoint. Its current-state claim is
superseded below; the original evidence and limits remain auditable.

> **Claim record — SYN-0017-C08 | analytic-judgment**
> **Claim:** The original zero-promotion decisions for `AGE-XT/CT` remain
> valid, while `AGE-GR` now independently passes through `SYN-0019`'s explicit
> UK–U.S. national One Health reconciliation. `AGE-CI/AE` remain Partial, so
> the current corpus is 47 Pass, 60 Partial and 3 Absent = 47/110 (42.7%),
> with AGE at 2/10 and no global-gate change.
> **Claim status:** superseded
> **Scope:** Current-status refresh of this formerly pre-UK-BSS synthesis; not
> a new transfer/control promotion, technical integration, incident,
> qualifying consequence or effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0019](syn-0019-uk-us-national-one-health-governance-reconciliation.md),
> `SYN-0019-C01`–`C05`; [SYN-0001](syn-0001-coverage-rubric.md),
> current `AGE-*` rows and `SYN-0001-C35`; `SYN-0017-C02/C03/C07`.
> **Basis / limits:** Current national governance now meets its own SF2 cell.
> It does not fill the hostile forward path, exact cyber-response/recovery and
> traceability-boundary control gaps, qualifying consequence or independent
> safeguard-effectiveness requirements.
> **Superseded by:** `SYN-0025-C09`; `AGE-CT/CI` and three additional AGE cells
> now pass, while `AGE-XT/AE` remain Partial.

## Safety boundary

This synthesis stays at public policy, functional architecture and defensive
control-family level. It contains no farm/facility topology, identity record,
operating setpoint, access route, exploit sequence or target-specific weakness.

## Related pages

- [SYN-0001 — Frozen coverage rubric](syn-0001-coverage-rubric.md)
- [SYN-0009 — U.S./global One Health scope](syn-0009-global-us-one-health-scope-reconciliation.md)
- [RSK-0007 — Agriculture transfer hypothesis](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [CTL-0005 — Agriculture control family](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [CTL-0011 — Generic OT control layer](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)
- [GOV-0011 — Global One Health guidance](../governance/gov-0011-quadripartite-one-health-jpa-national-guide.md)
- [GOV-0017 — AU DAS governance](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [SYN-0019 — UK–U.S. national One Health governance reconciliation](syn-0019-uk-us-national-one-health-governance-reconciliation.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0020](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [SRC-0021](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md)
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
