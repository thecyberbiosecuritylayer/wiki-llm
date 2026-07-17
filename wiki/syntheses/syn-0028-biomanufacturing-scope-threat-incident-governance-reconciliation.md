---
id: SYN-0028
type: synthesis
title: Biomanufacturing scope, threat, incident and governance reconciliation
aliases:
  - BMO residual ST TV CI GR reconciliation
  - Merck cross-cutting incident threshold reconciliation
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0003
  - SRC-0018
  - SRC-0031
  - SRC-0043
  - SRC-0044
  - SRC-0045
  - SRC-0046
  - SRC-0047
  - SRC-0048
sensitivity: public
dual_use: low
relations:
  - predicate: depends-on
    target: SYN-0016
    claim_id: SYN-0028-C01
    evidence:
      - source: SRC-0043
        locator: "SYN-0016-C06/C07 prior BMO residual state"
  - predicate: evidenced-by
    target: SRC-0043
    claim_id: SYN-0028-C03
    evidence:
      - source: SRC-0043
        locator: "SRC-0043-C02–C08; report pp. 23–33/physical pp. 29–39"
  - predicate: evidenced-by
    target: SRC-0044
    claim_id: SYN-0028-C04
    evidence:
      - source: SRC-0044
        locator: "SRC-0044-C03–C10; MHRA §§2–6.20, printed pp. 3–19"
  - predicate: evidenced-by
    target: SRC-0045
    claim_id: SYN-0028-C04
    evidence:
      - source: SRC-0045
        locator: "SRC-0045-C03–C10; definitive-view and secure-connectivity PDFs"
  - predicate: evidenced-by
    target: SRC-0046
    claim_id: SYN-0028-C05
    evidence:
      - source: SRC-0046
        locator: "SRC-0046-C02–C08; 10-K anchors sC5918D6835605DFB9861637AED9AB7C7 (Item 1A, displayed printed p. 25), s02DF6574F3035C8485C795D393F48705 (MD&A, p. 38) and sBB3EEB5901095A398997106BC9F8CDA1 (Vaccines, p. 41)"
  - predicate: evidenced-by
    target: SRC-0047
    claim_id: SYN-0028-C05
    evidence:
      - source: SRC-0047
        locator: "SRC-0047-C02–C08; opinion pp. 4–12 and 34–35"
  - predicate: evidenced-by
    target: SRC-0048
    claim_id: SYN-0028-C06
    evidence:
      - source: SRC-0048
        locator: "SRC-0048-C02–C10; FDA report pp. 1–13/physical pp. 5–17"
  - predicate: depends-on
    target: VUL-0003
    claim_id: SYN-0028-C04
    evidence:
      - source: SRC-0045
        locator: "VUL-0003-C01–C06; reconciled insider/supply/concrete exposure corpus"
  - predicate: depends-on
    target: INC-0006
    claim_id: SYN-0028-C14
    evidence:
      - source: SRC-0046
        locator: "INC-0006-C01–C10; canonical Merck event, timeline and evidence roles"
  - predicate: depends-on
    target: RSK-0019
    claim_id: SYN-0028-C05
    evidence:
      - source: SRC-0046
        locator: "RSK-0019-C01–C07; observed manufacturing/order/supply path"
  - predicate: depends-on
    target: CTL-0020
    claim_id: SYN-0028-C15
    evidence:
      - source: SRC-0046
        locator: "CTL-0020-C01–C07; exact event/control edges and evidence states"
  - predicate: governed-by
    target: GOV-0021
    claim_id: SYN-0028-C06
    evidence:
      - source: SRC-0048
        locator: "U.S. FDA drug-CGMP/data-integrity force, scope and exceptions"
  - predicate: governed-by
    target: GOV-0022
    claim_id: SYN-0028-C06
    evidence:
      - source: SRC-0044
        locator: "UK MHRA GxP data-integrity force, scope and exceptions"
  - predicate: governed-by
    target: GOV-0023
    claim_id: SYN-0028-C06
    evidence:
      - source: SRC-0045
        locator: "NCSC OT guidance force, contributor and adoption boundaries"
tags:
  - biomanufacturing
  - operational-technology
  - scope
  - threat-model
  - incident
  - governance
  - reconciliation
---

# Biomanufacturing scope, threat, incident and governance reconciliation

## Decision scope and prior state

This synthesis adjudicates exactly four residual BMO cells and the incident/
control thresholds directly affected by one new canonical Merck event. It does
not reopen already accepted `BMO-AS/WL/XT/CT` or borrow page volume as evidence.

> **Claim record — SYN-0028-C01 | artifact-observation**
> **Claim:** Before this transaction the frozen rubric is 75 Pass, 32 Partial
> and 3 Absent = 75/110, with BMO at 4/10, THI at 2/10, CTR at 8/10, critical
> cells at 63/27/1, dimensions at least 9/10 at 3/11 and global gates at
> 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Wiki after active `SYN-0027` and before this transaction; not
> external domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), checkpoint
> `C43`; [SYN-0016](syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md),
> `SYN-0016-C06/C07`.
> **Basis / limits:** Reproducible artifact state only.

## Evidence roles and independence

| Decision | Direct role | Independent role | Boundary |
| --- | --- | --- | --- |
| `BMO-ST` | NIST AMS industrial-biomanufacturing classes | existing Guttieres/ICH biologics, ATMP and production contexts | economic scope is not OT deployment |
| `BMO-TV` | NCSC concrete OT exposures/insider/supply classes | MHRA/FDA GxP data-integrity plus NIST/ICH cyber/process-quality roles | generic risk is not a named-facility finding |
| `BMO-CI` | Merck 10-K manufacturing/order/supply measurement | NJ published opinion/Kroll incident-property-damage context | court does not replicate order or dollar values |
| `BMO-GR` | U.S. FDA and UK MHRA data-integrity/GMP roles | NIST/NCSC OT-cyber and existing ICH/Q13 context | guidance, cited obligations and adoption signals remain distinct |

> **Claim record — SYN-0028-C02 | analytic-judgment**
> **Claim:** NIST scope, FDA/MHRA regulator, NIST/NCSC OT, Merck issuer and New
> Jersey adjudicative roles are materially independent for their assigned
> claims; wrappers, regional ICH copies, NCSC companion PDFs, Kroll and the
> court are not multiplied beyond their actual roles.
> **Claim status:** active
> **Scope:** Claim-specific SF2/SF3 source accounting, not universal
> institutional independence or equal evidentiary weight.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0043-C01/C07`; `SRC-0044-C01/C09`;
> `SRC-0045-C01/C02/C09`; `SRC-0046-C01/C08`; `SRC-0047-C01/C06`;
> `SRC-0048-C01/C09`; existing `SYN-0016-C01`.
> **Basis / limits:** Issuer, jurisdiction, genre and evidence-production
> differences are explicit; same-programme artifacts stay one lineage.

## BMO decisions

### Industrial scope — `BMO-ST`

> **Claim record — SYN-0028-C03 | analytic-judgment**
> **Claim:** `BMO-ST` passes at SF2: the existing independent corpus covers
> biologics, cell/gene/ATMP plus batch, continuous, centralized and distributed
> contexts, while NIST AMS directly supplies the missing industrial variants
> across food/beverage, chemical/biofuel/bioplastic, forest/material and other
> bounded manufacturing branches.
> **Claim status:** active
> **Scope:** Frozen scope literal; not a claim every listed establishment uses
> advanced biotechnology, the same OT stack or one universal definition.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0043](../sources/src-0043-nist-us-biomanufacturing-economy-2023.md),
> `SRC-0043-C02`–`C07`; [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md);
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md);
> `SYN-0016-C01`–`C04`.
> **Basis / limits:** Every literal scope branch is direct in the independent
> union and NIST's broad/advanced/mechanical boundaries remain explicit.

### Threat, hazard, insider, supply and exposure — `BMO-TV`

> **Claim record — SYN-0028-C04 | analytic-judgment**
> **Claim:** `BMO-TV` passes at SF2: existing NIST/ICH roles supply cyber
> manipulation/outage and process/quality hazards, while `VUL-0003` reconciles
> independent NCSC/MHRA/FDA insider, supply-chain and concrete identity,
> integrity, legacy, vendor/cloud/remote and connectivity exposures.
> **Claim status:** active
> **Scope:** Defensive BMO threat/vulnerability corpus, not prevalence,
> exploitability, named-facility weakness or an observed product-quality event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [VUL-0003](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md),
> `VUL-0003-C01`–`C04`; `SRC-0044-C04`–`C08`;
> `SRC-0045-C04`–`C08`; `SRC-0048-C04`–`C08`; `SRC-0018/SRC-0031`.
> **Basis / limits:** All literal classes have direct independent support and
> malicious/non-adversarial states remain separated.

### Observed manufacturing/supply consequence — `BMO-CI`

> **Claim record — SYN-0028-C05 | analytic-judgment**
> **Claim:** `BMO-CI` passes at SF3: Merck's primary 10-K directly documents
> cyberattack→manufacturing disruption→order backlog/unfulfilled certain-
> product orders→supply consequence, and the independent published court
> lineage confirms the NotPetya incident/property-damage context with Kroll/
> expert technical evidence while leaving Merck the sole consequence measurer.
> **Claim status:** active
> **Scope:** One 2017–2018 incident and bounded supply outcome; not batch
> quality, confirmed shortage, patient injury, attack-only Gardasil causation,
> independently replicated figures or control effectiveness.
> **As of:** Records through 2023-05-01.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md),
> `INC-0006-C01`–`C08`; [RSK-0019](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md),
> `RSK-0019-C01`–`C05`; `SRC-0046-C02`–`C07`; `SRC-0047-C02`–`C08`.
> **Basis / limits:** Direct observed outcome plus materially independent
> incident/context role meets the frozen floor without source multiplication.

### U.S.–UK GMP/data-integrity/OT governance — `BMO-GR`

> **Claim record — SYN-0028-C06 | analytic-judgment**
> **Claim:** `BMO-GR` passes at SF2: independent U.S. FDA and UK MHRA drug/GxP
> data-integrity instruments plus NIST/NCSC OT-cyber roles are reconciled for
> jurisdiction, scope, nonbinding guidance versus cited obligations, current
> status, exceptions, inspection/enforcement context and unknown firm-level
> adoption/effectiveness.
> **Claim status:** active
> **Scope:** U.S.–UK BMO governance comparison; not legal advice, global
> equivalence, compliance finding, adoption census or effectiveness.
> **As of:** Current official presentations reviewed 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [GOV-0021](../governance/gov-0021-us-fda-drug-cgmp-data-integrity-governance.md);
> [GOV-0022](../governance/gov-0022-uk-mhra-gxp-data-integrity-governance.md);
> [GOV-0023](../governance/gov-0023-uk-ncsc-operational-technology-governance.md);
> `SRC-0044-C02`–`C10`; `SRC-0045-C02`–`C10`;
> `SRC-0048-C02`–`C10`; existing `GOV-0016/SRC-0018` context.
> **Basis / limits:** Two jurisdictional regulator lineages and complementary
> OT roles meet the criterion; issuance/inspection context is not uptake.

### BMO nonpromotions

> **Claim record — SYN-0028-C07 | analytic-judgment**
> **Claim:** `BMO-SD` remains Partial because QMS-as-software and ERP remain
> absent despite new MES/LIMS/MRP/vendor/cloud/remote coverage; `BMO-AE`
> remains Absent because no deployed safeguard has a metric, comparator and
> independent evaluator.
> **Claim status:** active
> **Scope:** Exact adjacent-cell residuals; MRP≠ERP and organizational quality
> systems/PQS≠QMS software.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md),
> `SYS-0002-C07`; `SRC-0044-C10`; `SRC-0045-C10`; `SRC-0048-C10`;
> `VUL-0003-C06`; exact frozen criteria.
> **Basis / limits:** Related terms and test requirements cannot replace
> missing literals or SF3 outcome evidence.

## Cross-cutting incident and control thresholds

### Event count, lifecycle and technical support

The canonical public INC/review-page set at this checkpoint is five: Synnovis
(`INC-0001`, LAB), the national clinical review (`INC-0003`, CPH), JBS
(`INC-0004`, AGE), the anonymous chicken-farm account (`INC-0005`, AGE), and
Merck (`INC-0006`, BMO). The conservative distinct-event lower bound is five.
Merck creates the fourth sector, not another event from its two source roles.

`SYN-0028-C08` is superseded for the public corpus because one of its four
technical-support units was retired for privacy.

> **Claim record — SYN-0028-C14 | analytic-judgment**
> **Claim:** `THI-SD` remains Partial because Synnovis, the chicken-farm
> account, and Merck provide only three incident-specific technical dependency
> cases at this checkpoint; `THI-WL` also remains Partial because five public
> INC/review pages cannot meet the six-event lifecycle floor.
> **Evidence:** `INC-0001/0003/0004/0005/0006` event, timeline, and evidence
> sections; `INC-0006-C01`–`C03`; court pp. 7–10; the frozen `THI-WL/SD`
> criteria in [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** The national clinical review supports an outcome branch but does
> not establish an event-specific interface dependency. Unknown mechanisms and
> dates remain explicit.

### Consequence count and global incident gate

> **Claim record — SYN-0028-C09 | analytic-judgment**
> **Claim:** `THI-CI` and the global incident gate remain Fail: the corpus now
> spans LAB, CPH, AGE and BMO and includes multiple evidenced patient, animal,
> processing and supply outcomes, but supports a conservative lower bound of
> only five distinguishable events. Aggregate review units cannot be
> multiplied into additional events.
> **Claim status:** active
> **Scope:** Frozen incident-count/sector/outcome contract and conservative
> event identity; not equal event assurance, universal biological harm or all
> known cyberbio incidents.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `INC-0001/0003/0004/0005/0006`; `SYN-0015-C03`;
> `SYN-0025-C06`, `SYN-0027-C06`; `INC-0006-C04`–`C06`; exact
> `THI-CI`/global incident criteria.
> **Basis / limits:** Sector and outcome limbs are now met, but event identity
> is conjunctive and remains one below the six-event floor.

### Incident lessons, investigations and control portfolio

`SYN-0028-C10` is superseded for the public corpus because its incident,
control-lesson, and investigation numerators included a lineage retired for
privacy.

> **Claim record — SYN-0028-C15 | analytic-judgment**
> **Claim:** `THI-CT`, `THI-AE`, and `CTR-CI` remain Partial at this checkpoint:
> Synnovis, the national clinical review, and Merck supply three public
> control-lesson lineages; Kroll is the only qualifying independent technical
> investigation; and the four-primary-incident control-lesson floor is not met.
> **Evidence:** [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md),
> `CTL-0020-C01`–`C06`; `CTL-0004/0014`; `INC-0006-C03`–`C08`; court
> pp. 7–10; the frozen `THI-CT/AE` and `CTR-CI` criteria in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** Kroll is counted once through bounded court-recorded findings;
> its report and method are unavailable, the court is not another technical
> investigation, and implementation is not control effectiveness.

## Remaining cells and global gates

`SYN-0028-C11` is superseded because the public nonpromotion set expanded
after the privacy retirement.

> **Claim record — SYN-0028-C17 | analytic-judgment**
> **Claim:** `THI-WL/SD/TV/XT/CI/CT/AE/GR`, `BMO-AE`, `CTR-CI/AE`, and the
> global risk-chain, directionality, incident, and control gates remain
> unchanged at this checkpoint.
> **Evidence:** `SYN-0028-C01`–`C07`, `C09`, `C14`, and `C15`; the exact
> current rubric and gate contracts in [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** One incident cannot fill unrelated count, taxonomy,
> directionality, governance, investigation, or effectiveness floors.

## Score decision

`SYN-0028-C12` is superseded because its score included four public-corpus
transitions that no longer meet their numerators.

> **Claim record — SYN-0028-C16 | artifact-observation**
> **Claim:** Strict public-corpus review accepts exactly four Partial→Pass
> transitions, `BMO-ST/TV/CI/GR`. Totals become 78 Pass, 29 Partial, and
> 3 Absent, or 78/110 (70.9%); BMO becomes 8/10, THI remains 2/10,
> CTR remains 8/10, critical cells become 66/24/1, dimensions at least
> 9/10 remain 2/11, and global gates remain 7 Pass/5 Fail.
> **Evidence:** `SYN-0028-C01`–`C07`, `C09`, and `C14`–`C17`; frozen
> criteria/source floors; prior recalculated checkpoint in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** This is checkpoint arithmetic, not absolute completeness; all
> remaining Partial and Absent cells earn zero.

## Safety boundary

> **Claim record — SYN-0028-C13 | analytic-judgment**
> **Claim:** The synthesis contains no indicator, code, credential, endpoint,
> vulnerable version, exploit sequence, facility/network topology, process
> setting, biological recipe or operational response procedure.
> **Claim status:** stale
> **Scope:** Local content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and source/derivative safety boundaries.
> **Limits:** Functional edges and evidence-state reasoning are sufficient for
> every claimed pass. This is a local page-content assertion, not an
> externally evidenced decision claim, so it is retained as a safety note but
> is no longer maintained as active evidence.

## Related pages

- [SYN-0030 — Subsequent genomic incident-count and governance reconciliation](syn-0030-23andme-genomic-incident-governance-reconciliation.md)
- [SYN-0001](syn-0001-coverage-rubric.md)
- [SYN-0016](syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [VUL-0003](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [RSK-0019](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [GOV-0021](../governance/gov-0021-us-fda-drug-cgmp-data-integrity-governance.md)
- [GOV-0022](../governance/gov-0022-uk-mhra-gxp-data-integrity-governance.md)
- [GOV-0023](../governance/gov-0023-uk-ncsc-operational-technology-governance.md)

## Sources

- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [SRC-0043](../sources/src-0043-nist-us-biomanufacturing-economy-2023.md)
- [SRC-0044](../sources/src-0044-uk-mhra-gxp-data-integrity-guidance-2018-current.md)
- [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md)
- [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md)
- [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md)
- [SRC-0048](../sources/src-0048-us-fda-drug-cgmp-data-integrity-guidance-2018-current.md)
