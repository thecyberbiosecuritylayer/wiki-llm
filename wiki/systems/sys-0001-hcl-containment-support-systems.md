---
id: SYS-0001
type: system
title: Containment-support cyberphysical systems in HCLs
aliases:
  - HCL containment-support systems
  - digitally supported laboratory containment
status: active
created: 2026-07-11
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0002
  - SRC-0004
  - SRC-0018
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0002
    claim_id: SYS-0001-C01
    evidence:
      - source: SRC-0002
        locator: "§ Pathogen research, first two paragraphs; Table 1, Worker Safety and Public Health rows"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYS-0001-C04
    evidence:
      - source: SRC-0004
        locator: "Glossary, Cybersecurity, printed p. xiv (PDF p. 16); §6.5, printed pp. 34–37 (PDF pp. 54–57)"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYS-0001-C06
    evidence:
      - source: SRC-0018
        locator: "§§2.3.5–2.3.7, printed pp. 22–26 (PDF pp. 39–43); §4.2.2, printed p. 55 (PDF p. 72); §§5.3.1–5.3.2, printed pp. 79–80 (PDF pp. 96–97)"
tags:
  - laboratories
  - high-containment
  - cyber-physical
  - containment
---

# Containment-support cyberphysical systems in HCLs

> This is a defensive system class for digitally controlled or monitored
> functions that support the laboratory environment, containment, monitoring,
> access, or related safety and security operations. The page does not describe
> a specific facility architecture or operational settings.

## Scope

`SYS-0001` covers the source-reported class of building-automation and related
cyberphysical dependencies in high-containment laboratories. It does not claim
that every HCL uses the same BAS, that all containment devices are connected to
a network, or that remote access is enabled.

Connected instruments, LIMS, storage systems, and QMS remain separate candidate
system classes within
[WFL-0002](../workflows/wfl-0002-high-containment-laboratory.md); they are not folded
into `SYS-0001` merely because they share a laboratory context.

## Functions and workflow role

The source analysis identifies the following as possible functions of advanced
building automation:

- monitoring or control of environmental and containment-support conditions;
- power and status monitoring and operational logging;
- support for physical-access monitoring; and
- interfaces with some laboratory safety equipment.

These are capability categories. The source does not establish the specific
set of functions, responsibility boundaries, manual overrides, fail-safe
behavior, network paths, or maintenance access
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Pathogen research, first two paragraphs).

> **Claim record — SYS-0001-C01 | source-report**
> **Claim:** Crawford et al. describe advanced HCL building automation as a
> cyberphysical system that may monitor, control, or log a range of facility and
> containment-support functions important to safety and security.
> **Claim status:** active
> **Scope:** Possible capabilities in a qualitative HCL model, not a universal
> architecture.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research, first two paragraphs; Table 1, Worker Safety and Public
> Health rows.
> **Basis / limits:** The source description relies in part on vendor and
> adjacent-domain literature; prevalence, configuration, and external exposure
> were not measured. Operational parameters are intentionally omitted.

## Security properties

The following properties matter for defensive modeling:

- **integrity** of the digital control state and monitoring data;
- **availability** of safety-support functions and visibility;
- **authenticity/authorization** of commands and maintenance actions;
- **provenance** of logs, alarms, and change records; and
- **resilience** during a digital outage or degraded operation.

> **Claim record — SYS-0001-C02 | analytic-judgment**
> **Claim:** The integrity and availability of a containment-support CPS are
> relevant to cyberbiosecurity only when the digital state actually affects a
> physical safety or security function; network connectivity alone does not
> establish such a consequence path.
> **Claim status:** active
> **Scope:** An editorial boundary rule for modeling HCL systems.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Methods — Asset-impact analysis; § Pathogen research; Table 1.
> **Basis / limits:** The authors' method directly moves from asset compromise
> to impact. The wiki additionally requires a supported control or physical
> dependency and does not accept connectivity as evidence of harm. Specific
> dependencies have not yet been validated.

## Boundaries and dependencies

Potentially significant boundaries include engineering and maintenance access,
interfaces between facility systems and laboratory operations, identity and
authorization, and dependence on power and monitoring. `SRC-0002` does not
describe them precisely enough to support claims about segmentation, protocols,
privileges, or the attack surface of a specific HCL.

> **Claim record — SYS-0001-C03 | analytic-judgment**
> **Claim:** The corpus available at the time supported the existence of a
> generic digital-to-physical dependency class, but not a reference
> architecture, prevalence estimate, or validated vulnerability for HCL
> containment systems.
> **Claim status:** superseded
> **Scope:** Wiki corpus following ingestion of `SRC-0002`.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Methods — Asset-impact analysis; §§ Cyber considerations in HCLs,
> Pathogen research.
> **Basis / limits:** The source is a single-source qualitative synthesis.
> Architecture and control conclusions require normative laboratory guidance,
> primary engineering evidence, and independent validation.
> **Superseded by:** `SYS-0001-C05` following ingestion of WHO normative
> guidance.

> **Claim record — SYS-0001-C04 | source-report**
> **Claim:** WHO 2024 explicitly includes cyber access to laboratory equipment
> and building systems and recommends protecting building-management,
> automation, and security systems within the scope of laboratory information
> and cybersecurity.
> **Claim status:** active
> **Scope:** Normative control scope, not HCL architecture or exposure evidence.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> Glossary, `Cybersecurity`, printed p. xiv (PDF p. 16); §6.5,
> printed pp. 34–37 (PDF pp. 54–57).
> **Basis / limits:** WHO directly includes these system classes but does not
> report network topology, prevalence, compromise, implementation, or testing.

> **Claim record — SYS-0001-C05 | analytic-judgment**
> **Claim:** The corpus now supports both a qualitative HCL dependency class and
> WHO normative control scope, but still not a reference architecture,
> facility-specific dependency, validated vulnerability, or control
> effectiveness for containment-support systems.
> **Claim status:** active
> **Scope:** Evidence reconciliation following `SRC-0004`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research; Table 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> Glossary, printed p. xiv; §§5.3.4 and 6.5, printed pp. 21–22 and
> 34–37.
> **Basis / limits:** The WHO cyber section cites Crawford for cyberattack
> context, so it is not independent empirical corroboration. It adds
> authoritative recommendations, not engineering validation.

> **Claim record — SYS-0001-C06 | analytic-judgment**
> **Claim:** NIST independently supports generic BAS, physical-access, and
> safety-system classes together with separation and continuity concerns, while
> HCL-specific containment, LIMS or ELN, custody, and facility validation remain
> unproven.
> **Claim status:** active
> **Scope:** Relevance of generic facility-OT components to HCL dependencies;
> not a containment architecture or deployment.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research and Table 1;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.5–2.3.7, printed pp. 22–26 (PDF pp. 39–43); §4.2.2,
> printed p. 55 (PDF p. 72); §§5.3.1–5.3.2, printed pp. 79–80.
> **Basis / limits:** The component classes and independent HCL dependency are
> direct; their combined applicability is editorial. No biological safe state,
> network boundary, or control result is inferred.

## Evidence and uncertainty

The page does not reproduce product names, settings, access paths, or detailed
failure sequences. Everything beyond capability categories and security
properties remains open. `RSK-0001` uses this system class as a precondition and
explicitly labels the scenario hypothetical.

## Related pages

- [SYS-0007 — LIMS/storage/cloud/identity map with ELN gap](sys-0007-biobank-informatics-storage-ecosystem.md)
- [AST-0005 — Laboratory/biobank asset and stakeholder classes](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [SYN-0010 — Laboratory/biobank reconciliation](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [WFL-0002 — HCL cyber-physical workflow](../workflows/wfl-0002-high-containment-laboratory.md)
- [RSK-0001 — Disruption of digitally supported containment functions](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [CTL-0001 — Risk-based laboratory information and cybersecurity controls](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
- [GOV-0001 — WHO Laboratory Biosecurity Guidance 2024](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0002 — Crawford et al. 2023](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0004 — WHO Laboratory Biosecurity Guidance 2024](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
  § Pathogen research; Table 1.
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
  Glossary, printed p. xiv; §§5.3.4, 6.5.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.5–2.3.7, 4.2.2, and 5.3.
