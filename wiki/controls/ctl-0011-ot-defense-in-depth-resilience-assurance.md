---
id: CTL-0011
type: control
title: Risk-based OT defense-in-depth, safe response and trusted recovery
aliases:
  - NIST OT defense in depth controls
  - cross-sector OT resilience and assurance
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-11
source_ids:
  - SRC-0002
  - SRC-0003
  - SRC-0004
  - SRC-0010
  - SRC-0018
sensitivity: public
dual_use: low
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: CTL-0011-C01
    evidence:
      - source: SRC-0018
        locator: "§§3–6, printed pp. 33–138 (PDF pp. 50–155); Appendices E–F, printed pp. 207–298 (PDF pp. 224–315)"
  - predicate: governed-by
    target: GOV-0008
    claim_id: CTL-0011-C01
    evidence:
      - source: SRC-0018
        locator: "§1.1, printed p. 6 (PDF p. 23); Appendix F §§F.2 and F.4, printed pp. 214, 223–224 (PDF pp. 231, 240–241)"
  - predicate: mitigates
    target: RSK-0002
    claim_id: CTL-0011-C02
    evidence:
      - source: SRC-0003
        locator: "Digital Information Flow in Biomanufacturing and Figure 1"
      - source: SRC-0018
        locator: "§§5.2.3, 5.4 and 6.1–6.2, printed pp. 71–75, 83–125 (PDF pp. 88–92, 100–142)"
  - predicate: detects
    target: RSK-0002
    claim_id: CTL-0011-C02
    evidence:
      - source: SRC-0003
        locator: "Digital Information Flow in Biomanufacturing and Figure 1"
      - source: SRC-0018
        locator: "§§6.3.1–6.3.3, printed pp. 126–133 (PDF pp. 143–150)"
  - predicate: contains
    target: RSK-0002
    claim_id: CTL-0011-C02
    evidence:
      - source: SRC-0003
        locator: "Digital Information Flow in Biomanufacturing and Figure 1"
      - source: SRC-0018
        locator: "§§4.2.2, 6.2.4.5 and 6.4, printed pp. 55, 114–117, 134–137 (PDF pp. 72, 131–134, 151–154)"
  - predicate: recovers
    target: RSK-0002
    claim_id: CTL-0011-C02
    evidence:
      - source: SRC-0003
        locator: "Digital Information Flow in Biomanufacturing and Figure 1"
      - source: SRC-0018
        locator: "§§5.3.2, 6.2.4.3–6.2.4.5 and 6.5, printed pp. 79–80, 112–117, 137–138 (PDF pp. 96–97, 129–134, 154–155)"
  - predicate: mitigates
    target: RSK-0001
    claim_id: CTL-0011-C03
    evidence:
      - source: SRC-0002
        locator: "HCL dependency analysis and Table 1"
      - source: SRC-0004
        locator: "§§6.3–6.4.2, printed pp. 31–34 (PDF pp. 51–54); §7, printed pp. 40–44 (PDF pp. 60–64)"
      - source: SRC-0018
        locator: "§§2.3.5–2.3.7, 4.2.2 and 5.3.1, printed pp. 22–26, 55, 79 (PDF pp. 39–43, 72, 96)"
  - predicate: detects
    target: RSK-0001
    claim_id: CTL-0011-C03
    evidence:
      - source: SRC-0002
        locator: "HCL dependency analysis and Table 1"
      - source: SRC-0004
        locator: "§§6.3–6.4.2, printed pp. 31–34 (PDF pp. 51–54); §§6.5–6.6, printed pp. 34–39 (PDF pp. 54–59)"
      - source: SRC-0018
        locator: "§§6.3.1–6.3.3, printed pp. 126–133 (PDF pp. 143–150)"
  - predicate: contains
    target: RSK-0001
    claim_id: CTL-0011-C03
    evidence:
      - source: SRC-0002
        locator: "HCL dependency analysis and Table 1"
      - source: SRC-0004
        locator: "§§6.3–6.6, printed pp. 31–39 (PDF pp. 51–59); §7, printed pp. 40–44 (PDF pp. 60–64)"
      - source: SRC-0018
        locator: "§§4.2.2, 5.3.1 and 6.4, printed pp. 55, 79, 134–137 (PDF pp. 72, 96, 151–154)"
  - predicate: recovers
    target: RSK-0001
    claim_id: CTL-0011-C03
    evidence:
      - source: SRC-0002
        locator: "HCL dependency analysis and Table 1"
      - source: SRC-0004
        locator: "§§6.3–6.6, printed pp. 31–39 (PDF pp. 51–59); §7, printed pp. 40–44 (PDF pp. 60–64)"
      - source: SRC-0018
        locator: "§§5.3.2 and 6.5, printed pp. 79–80, 137–138 (PDF pp. 96–97, 154–155)"
  - predicate: mitigates
    target: RSK-0007
    claim_id: CTL-0011-C04
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-1, #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§2.3.8, 5.3.3, 5.3.6–5.3.7 and 6.2.9–6.2.10, printed pp. 26–28, 81–82, 120–124 (PDF pp. 43–45, 98–99, 137–141)"
  - predicate: detects
    target: RSK-0007
    claim_id: CTL-0011-C04
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§6.3.1–6.3.3, printed pp. 126–133 (PDF pp. 143–150)"
  - predicate: contains
    target: RSK-0007
    claim_id: CTL-0011-C04
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§5.3.3, 6.2.10 and 6.4, printed pp. 81, 122–124, 134–137 (PDF pp. 98, 139–141, 151–154)"
  - predicate: recovers
    target: RSK-0007
    claim_id: CTL-0011-C04
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§5.3.2 and 6.5, printed pp. 79–80, 137–138 (PDF pp. 96–97, 154–155)"
tags:
  - operational-technology
  - defense-in-depth
  - incident-response
  - recovery
  - assurance
---

# Risk-based OT defense-in-depth, safe response and trusted recovery

## Control family and evidence state

This page maps generic NIST OT controls only where an independent sector source
already establishes a relevant process/equipment dependency. Similar components
or a sector label are insufficient to validate a topology, failure path or
biological consequence. All NIST-derived control states remain recommended.

> **Claim record — CTL-0011-C01 | source-report**
> **Claim:** SP 800-82 Rev. 3 provides a risk-based OT portfolio spanning
> inventory/governance, prevention, detection, containment/response, recovery
> and assurance, with tailoring and safety/availability constraints.
> **Claim status:** active
> **Scope:** Generic OT control functions, not a complete sector baseline or
> implementation result.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§3–6, printed pp. 33–138 (PDF pp. 50–155); Appendices E–F,
> printed pp. 207–298 (PDF pp. 224–315).
> **Basis / limits:** Portfolio and constraints are direct. Exact applicability
> and residual risk require sector/deployment evidence.

## Biomanufacturing branch

[SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md) establishes
generic biomanufacturing measurement/control and PLC/DCS/SCADA dependencies;
NIST independently describes pharmaceutical DCS and OT control functions. The
pair supports a conditional control mapping to
[RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md),
but not GMP release, MES/LIMS/QMS/ERP coverage or an observed product path.

[CTL-0015](ctl-0015-continuous-manufacturing-quality-control.md) now
supplies the separate ICH Q13 process-quality/release/disposition complement.
Those predicates are not inherited into this generic NIST family, and the two
pages together still do not prove one deployed architecture or effectiveness.

> **Claim record — CTL-0011-C02 | analytic-judgment**
> **Claim:** Inventory/boundary mapping, configuration/access/segmentation,
> passive monitoring, safety-aware response and trusted restoration
> conditionally mitigate, detect, contain and recover the generic control/data
> edges of `RSK-0002`.
> **Claim status:** active
> **Scope:** Generic biomanufacturing OT dependency supported by `SRC-0003` and
> NIST; no validated GMP/quality architecture or incident.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow and Figure 1;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5.2.3, 5.4 and 6.1–6.5, printed pp. 71–75, 83–138
> (PDF pp. 88–92, 100–155).
> **Basis / limits:** Sector dependency and generic control functions are
> independent/direct; exact mapping is editorial. Implementation and product-
> quality interruption evidence are absent.

## Laboratory branch

[SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
supports digitally dependent HCL functions. NIST supplies generic BAS, access-
control and safety-system classes plus OT safeguards. This makes selected
controls relevant to [RSK-0001](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
without proving biological containment, custody, LIMS/ELN or a facility design.

> **Claim record — CTL-0011-C03 | analytic-judgment**
> **Claim:** BAS/PACS/safety-system separation, access, monitoring, safe manual/
> independent operation, incident response and restoration conditionally map
> to the digitally supported edges of `RSK-0001`.
> **Claim status:** active
> **Scope:** Generic facility-OT branch with an independent HCL dependency
> source; not HCL containment validation or a facility-specific safeguard.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> HCL dependency analysis and Table 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.3–6.4.2, printed pp. 31–34 (PDF pp. 51–54); §7,
> printed pp. 40–44 (PDF pp. 60–64);
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.5–2.3.7, 4.2.2, 5.3.1–5.3.2, 6.2.4.4–6.2.4.5 and
> 6.3–6.5, printed pp. 22–26, 55, 79–80, 113–138.
> **Basis / limits:** HCL dependency and generic system/control classes are
> independent/direct; mapping is editorial. Biological safe state and
> containment performance are not established.

## Agriculture branch

[SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md) supports
a bounded smart-farm data/equipment/production path. NIST adds generic IIoT,
distributed and remote OT control functions. The pair does not establish One
Health breadth, traceability/surveillance platforms or farm topology.

> **Claim record — CTL-0011-C04 | analytic-judgment**
> **Claim:** Asset/flow inventory, access/remote-path restriction, monitoring,
> local response and restoration conditionally mitigate, detect, contain and
> recover the generic connected-equipment edges of `RSK-0007`.
> **Claim status:** active
> **Scope:** Bounded smart-farm equipment/data branch; not all agriculture,
> validated control authority, One Health or a field incident.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML #s1-1, #s1-4 and #s3-1–2; Tables 1–2;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.8, 5.3.3, 5.3.6–5.3.7, 6.2.9–6.2.10 and 6.3–6.5,
> printed pp. 26–28, 81–82, 120–138.
> **Basis / limits:** Farm dependency and generic IIoT/OT controls are
> independent/direct; exact mapping is inferred. Deployment and outcomes are
> unknown.

## Prerequisites, failure modes and tradeoffs

- active discovery/scanning can disrupt legacy or fragile OT;
- authentication/lockout latency can impede emergency operator action;
- monitoring can have encrypted blind spots, resource cost and false signals;
- isolation, disconnect or shutdown can worsen production or safety;
- one `safe state` does not fit every biological/process system;
- vendor, legacy and single-source dependencies can make a control infeasible;
- backup existence does not establish restorability or process-state integrity;
- compensating control requires evidence, equivalence and residual-risk review.

> **Claim record — CTL-0011-C05 | source-report**
> **Claim:** NIST explicitly states OT control selection should account for operational,
> safety, legacy, vendor, visibility and recovery tradeoffs that can make a
> conventionally secure action unsafe or infeasible.
> **Claim status:** active
> **Scope:** Generic OT prerequisites/failure modes, not a failure finding for
> the three mapped sectors.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §2.4/Table 1, printed pp. 28–32; §§4.2.1–4.2.2, 5.3 and
> 6.1–6.5, printed pp. 54–55, 79–138; Appendix F §F.4.
> **Basis / limits:** Tradeoffs and tailoring needs are direct. Their presence
> or severity in a deployment is unknown.

## Assurance method versus result

Assessment, independent-assessor selection, exercises, restoration testing,
continuous monitoring and compensating-control documentation are recommended
assurance mechanisms. The source does not contain a completed sector test or
metric.

> **Claim record — CTL-0011-C06 | source-report**
> **Claim:** NIST defines assessment and monitoring processes but supplies no
> completed cyberbio safeguard test, restoration metric or independently
> evaluated effectiveness result for `CTL-0011`.
> **Claim status:** active
> **Scope:** Evidence maturity of this NIST-derived family.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§4.3.5–4.3.7, printed pp. 63–65; §§6.3.2–6.5, printed
> pp. 128–138; Appendix F assessment/contingency families.
> **Basis / limits:** Processes and missing results are direct. Separate
> deployment/test evidence could change the states.

## Version and state boundary

The source maps CSF 1.1 and its stated SP 800-53 Rev. 5 baseline, not CSF 2.0.
Rev. 4 remains preliminary. Every relation here is recommended/conditional;
implementation, testing, effectiveness and independent evaluation are unknown.

> **Claim record — CTL-0011-C07 | analytic-judgment**
> **Claim:** `CTL-0011` is a versioned recommended family; crosswalk membership,
> a selected control or compensating-control label does not establish adoption,
> compliance, testing or effectiveness.
> **Claim status:** active
> **Scope:** Framework/evidence-state boundary through 2026-07-12.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§6.1–6.5 and Appendix F; `SRC-0018-C06`–`C09`.
> **Basis / limits:** Version/modality limits are direct; the evidence-state
> conclusion follows the absence of deployment results.

## Related pages

- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SYS-0007 — bounded biobank informatics/storage overlay](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [GOV-0008 — NIST OT governance](../governance/gov-0008-nist-sp-800-82r3-ot-security-2023.md)
- [SYN-0007 — OT applicability across cyberbio sectors](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [RSK-0001 — HCL containment disruption](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [RSK-0002 — Biomanufacturing control disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [RSK-0007 — Farm production/supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [CTL-0001 — Laboratory controls](ctl-0001-risk-based-laboratory-information-cybersecurity.md)
- [CTL-0005 — Agricultural controls](ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [CTL-0015 — continuous-manufacturing quality controls](ctl-0015-continuous-manufacturing-quality-control.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [SYN-0017 — Agriculture transfer/control/governance reconciliation](../syntheses/syn-0017-au-agriculture-transfer-control-governance-reconciliation.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
