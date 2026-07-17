---
id: SYN-0026
type: synthesis
title: U.S. animal-disease traceability herd and assurance reconciliation
aliases:
  - AGE AS AE traceability reconciliation
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0032
  - SRC-0035
  - SRC-0037
  - SRC-0041
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0041
    claim_id: SYN-0026-C02
    evidence:
      - source: SRC-0041
        locator: "SRC-0041-C03–C09; 9 CFR Part 86; APHIS performance PDF; OIG audit"
  - predicate: depends-on
    target: AST-0009
    claim_id: SYN-0026-C03
    evidence:
      - source: SRC-0041
        locator: "AST-0009-C01/C04/C05 and SRC-0041-C03/C04 literal herd union"
      - source: SRC-0037
        locator: "AST-0009-C01; EU animal/plant asset and stakeholder classes"
  - predicate: depends-on
    target: CTL-0019
    claim_id: SYN-0026-C04
    evidence:
      - source: SRC-0041
        locator: "CTL-0019-C01–C06; APHIS implementation/test plus OIG independent audit"
  - predicate: depends-on
    target: SYN-0025
    claim_id: SYN-0026-C01
    evidence:
      - source: SRC-0041
        locator: "Prior frozen score and AGE gap state in SYN-0025-C08/C09"
tags:
  - agriculture
  - animal-health
  - herd
  - assets
  - traceability
  - assurance
  - reconciliation
---

# U.S. animal-disease traceability herd and assurance reconciliation

## Decision scope

This synthesis audits exactly `AGE-AS` and `AGE-AE`. It does not rescore
`AGE-XT`: animal-disease traceability and disease incidents are not cyber→
animal/plant/ecosystem effects. It also does not promote `CTR-AE` or `THI-CI`.

> **Claim record — SYN-0026-C01 | artifact-observation**
> **Claim:** Before this transaction the corpus is 72 Pass, 35 Partial and
> 3 Absent = 72/110, with AGE at 7/10; `AGE-AS/XT/AE` are its only open cells.
> **Claim status:** active
> **Scope:** Wiki after `SYN-0025` and before `SRC-0041/SYN-0026` activation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0025](syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md),
> `SYN-0025-C08/C09`; current frozen rubric checkpoint C41.
> **Basis / limits:** Reproducible artifact state, not external completeness.

## Evidence roles and independence

| Required role | Lineage | Contribution | Non-equivalence |
| --- | --- | --- | --- |
| Broad AGE assets/stakeholders | AU strategy, UK PATH-SAFE, EU animal/plant law | seeds, genomes, pathogens, samples, sensors/equipment, data, farmers, veterinarians, regulators, ecosystems | Strategy, programme and law remain distinct |
| Literal herd | U.S. GPO/APHIS Part 86 | cattle/bison herd, owners, authorities, herd-unique records | Herd is not replaced by EU group/lot/flock |
| Deployment and test metric | APHIS ADT | implemented programme, four TPM exercises, baseline/elapsed-time series | Issuer test, not independent evaluation |
| Independent evaluation | USDA OIG | audit of 11 disease-incident traces, one failed traceback, risk gaps | Non-statistical sample; same department, independent audit function |

APHIS/GPO is materially independent from the EU/AU/UK asset lineages. Within
the U.S. package, OIG is organizationally independent for performance-audit
claims but is not a second jurisdiction, programme or metric replication.

> **Claim record — SYN-0026-C02 | analytic-judgment**
> **Claim:** Source independence is claim-specific: the U.S. regulation is a
> new independent literal-herd lineage for `AGE-AS`, while APHIS supplies
> programme/test evidence and USDA OIG supplies the required independent
> assurance assessment and failure limits for `AGE-AE`.
> **Claim status:** active
> **Scope:** SF2/SF3 evidence roles; not source-ID multiplication, departmental
> independence for every predicate or a second deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0041](../sources/src-0041-us-animal-disease-traceability-herd-performance-audit.md),
> `SRC-0041-C03`–`C09`; issuer and OIG methods.
> **Basis / limits:** Distinct functions and limitations are explicit.

## `AGE-AS` — complete literal asset/stakeholder union

| Required class | Direct evidence | Boundary |
| --- | --- | --- |
| Seeds | EU plant law/`AST-0009` | Planting-material class, not genome synonym |
| Genomes | AU/PATH-SAFE/`AST-0003` | Digital/biological class, not every herd record |
| Herds | U.S. Part 86/`SRC-0041-C03` | Literal cattle/bison commuter herd |
| Pathogens | PATH-SAFE and animal/plant health sources | Surveillance object, no sensitive content |
| Samples | PATH-SAFE/EU official laboratory functions | Material and result classes separated |
| Sensors/equipment | AU/`AST-0003` | Functional class, no inventory/topology |
| Traceability/model data | AU/EU/U.S. Part 86 | Jurisdiction/object boundaries preserved |
| Farmers/veterinarians/regulators | AU/EU/U.S. roles | Owner/operator/professional/authority not collapsed |
| Ecosystems | AU/PATH-SAFE/One Health sources | Affected interest, not system owner |

> **Claim record — SYN-0026-C03 | analytic-judgment**
> **Claim:** `AST-0003/0009` plus independent AU, PATH-SAFE, EU and U.S.
> lineages satisfy `AGE-AS` at SF2 across every literal asset and stakeholder
> class, with herd directly represented and non-equivalence explicit.
> **Claim status:** active
> **Scope:** Canonical class map; not a farm/herd inventory, universal data
> model, protection state, deployment census or effect claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md);
> [AST-0009](../assets/ast-0009-animal-plant-health-assets-stakeholders.md),
> `AST-0009-C01/C04/C05`; `SRC-0032-C03`, `SRC-0035-C03`,
> `SRC-0037-C03`, `SRC-0041-C03/C04`.
> **Basis / limits:** Every literal is direct in a claim-appropriate source;
> no group/flock/lot class substitutes for herd.

## `AGE-AE` — deployed, tested and independently evaluated safeguard

The safeguarded function is animal-disease traceability: link regulated animal/
herd/movement states to retrievable records so an investigation can trace back
or forward. Evidence states are preserved:

1. Part 86 provides binding design;
2. APHIS documents programme implementation since 2013;
3. four TPM exercises provide defined elapsed-time tests and baseline/results;
4. OIG independently audits actual trace records, identifies one failure and
   tests oversight/risk-management adequacy; and
5. neither source proves universal biological or causal effectiveness.

> **Claim record — SYN-0026-C04 | analytic-judgment**
> **Claim:** `CTL-0019` satisfies `AGE-AE` at SF3: a deployed animal-disease
> traceability safeguard has scoped exercise metrics and an organizationally
> independent OIG performance assessment with positive, failure and method/
> coverage limitations explicit.
> **Claim status:** active
> **Scope:** One U.S. traceability safeguard and bounded evidence chain; not a
> cybersecurity control, universal effectiveness, disease-prevention outcome,
> causal effect size or independent reproduction of APHIS metrics.
> **As of:** Evidence through OIG report 2022 and current status 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0019](../controls/ctl-0019-animal-disease-traceability-performance-assurance.md),
> `CTL-0019-C01`–`C05`; `SRC-0041-C05`–`C09`.
> **Basis / limits:** Deployment/test and independent evaluation are direct;
> advance notice, subset coverage, terminated/failed traces, non-statistical
> audit sampling and absent computer-system assurance prevent overclaiming.

## Non-promotions

- `AGE-XT` remains Partial: neither natural disease nor traceability failure is
  a cyber→animal/plant/ecosystem effect.
- `THI-CI` remains Partial: 11 sampled disease traces are not eleven named or
  independently documented cyber incidents.
- `CTR-AE` remains Partial: one AGE safeguard does not meet its six-instance,
  four-sector and three-evaluator portfolio floor.
- The global control gate remains Fail; no universal effective cyber safeguard
  or required multi-sector independent corpus is created.

> **Claim record — SYN-0026-C05 | analytic-judgment**
> **Claim:** `AGE-XT`, `THI-CI`, `CTR-AE` and all global gates remain unchanged;
> disease/trace records, sample count and closed recommendations are not
> promoted into cyber incidents or effectiveness multiplication.
> **Claim status:** superseded
> **Scope:** Explicit adjacent-cell and gate boundaries.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0026-C01`–`C04`; frozen criteria/gates in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Separate literal/count/source-floor requirements remain.
> **Superseded by:** `SYN-0027-C06`; `AGE-XT` now passes while `THI-CI`,
> `CTR-AE` and every global gate remain unchanged.

## Score decision

> **Claim record — SYN-0026-C06 | artifact-observation**
> **Claim:** Strict review accepts exactly `AGE-AS` and `AGE-AE` Partial→Pass.
> Totals become 74 Pass, 33 Partial and 3 Absent = 74/110 (67.3%); AGE becomes
> 9/10, critical cells become 62 Pass/28 Partial/1 Absent, dimensions at least
> 9/10 become 3/11 and global gates remain 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Wiki after active `SRC-0041`, updated `AST-0009`, `CTL-0019` and
> `SYN-0026`; not absolute domain completeness or any adjacent transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0026-C01`–`C05`; exact frozen criteria/source floors;
> independent audits required before activation.
> **Basis / limits:** One critical and one noncritical cell move. `AGE-XT`
> stays Partial and every global gate is unchanged.

## Safety boundary

> **Claim record — SYN-0026-C07 | analytic-judgment**
> **Claim:** The synthesis exposes no farm, herd, animal, movement or disease-
> case record; no live identifier, system topology, credential, exploit,
> control parameter or operational response procedure is included.
> **Claim status:** stale
> **Scope:** Local content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page and source safety limits.
> **Limits:** Only public classes, aggregate metrics and audit states are
> retained. This is a local page-content assertion, not an externally
> evidenced decision claim, so it is retained as a safety note but is no
> longer maintained as active evidence.

## Related pages

- [SYN-0001](syn-0001-coverage-rubric.md)
- [SYN-0025](syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [AST-0009](../assets/ast-0009-animal-plant-health-assets-stakeholders.md)
- [CTL-0019](../controls/ctl-0019-animal-disease-traceability-performance-assurance.md)

## Sources

- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [SRC-0037](../sources/src-0037-eu-animal-plant-health-imsoc-legislative-ecosystem.md)
- [SRC-0041](../sources/src-0041-us-animal-disease-traceability-herd-performance-audit.md)
