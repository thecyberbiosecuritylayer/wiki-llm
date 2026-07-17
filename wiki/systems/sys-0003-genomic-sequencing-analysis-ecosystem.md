---
id: SYS-0003
type: system
title: Genomic sequencing and analysis ecosystem
aliases:
  - genomic-data processing ecosystem
  - sequencing and bioinformatics systems
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0014
  - SRC-0015
  - SRC-0016
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: SYS-0003-C01
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §4.4.2, printed pp. 20–22 (PDF pp. 29–31)"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: SYS-0003-C04
    evidence:
      - source: SRC-0006
        locator: "§1.3, printed p. 5 (PDF p. 16); §2.1, printed p. 9 (PDF p. 20); Tables 9–11 and 26–29, printed pp. 57–85 and 141–146 (PDF pp. 68–96 and 152–157)"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: SYS-0003-C05
    evidence:
      - source: SRC-0007
        locator: "Volume C §§2.1.2–2.1.4 and Figure 4, printed pp. 8–19 (PDF pp. 17–28); static Appendix E"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYS-0003-C06
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3, 3, 5–6, printed pp. 767–776 (PDF pp. 4–13)"
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: SYS-0003-C07
    evidence:
      - source: SRC-0015
        locator: "28 CFR §§202.201, .248 and .401; CISA requirements, Definitions and §§I–II, pp. 2–6"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYS-0003-C08
    evidence:
      - source: SRC-0016
        locator: "Articles 2, 23–27, 55–57, 73–75 and 92–96, PDF pp. 31–33, 42–45, 60–62, 75–78, 83–87"
  - predicate: governed-by
    target: GOV-0006
    claim_id: SYS-0003-C08
    evidence:
      - source: SRC-0016
        locator: "Articles 1–2 and 105, PDF pp. 29–33, 90–91"
  - predicate: depends-on
    target: AST-0001
    claim_id: SYS-0003-C02
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §3.5, printed p. 11 (PDF p. 20)"
tags:
  - genomics
  - sequencing
  - bioinformatics
  - cloud
  - clinical-systems
---

# Genomic sequencing and analysis ecosystem

> Defensive functional system class for devices, storage, analysis software,
> repositories and clinical/research interfaces that generate or process
> [genomic data](../assets/ast-0001-genomic-data.md). It is not a network diagram,
> reference architecture or claim about a deployed environment.

## Scope

NIST IR 8432 spans research, clinical, government and commercial contexts. The
IR 8467 profile adds sequencing providers, genome centers, clinical
laboratories, healthcare, DTC, technology developers, cloud providers,
repositories and other partners as possible organizational roles. The sources
name common functional classes but do not establish that every
organization uses all of them, that a component is network-exposed, or that one
security baseline fits every human and non-human use case.

## Functional components

| Component class | Defensive role in the source model | Evidence boundary |
| --- | --- | --- |
| Sequencing or measurement device | Generate raw genomic data from prepared samples | No product inventory, configuration or exposure census |
| Local/on-premise storage | Hold raw, intermediate or processed data | No reference storage architecture or retention proof |
| Cloud storage/compute | Store, process or share large genomic datasets | No provider-specific control or deployment validation |
| Analysis pipeline | Transform and interpret data using open-source, commercial or custom software | No canonical pipeline, dependency manifest or verified configuration |
| Public/controlled database | Support research access, aggregation and sharing | No universal authorization or consent model |
| EHR interface | Make clinically relevant genomic information available for care and later reinterpretation | Interoperability, provenance and consent integration remain gaps |

> **Claim record — SYS-0003-C01 | source-report**
> **Claim:** NIST IR 8432 describes a genomic-data processing ecosystem that
> includes sequencing devices, on-premise or cloud storage, open-source or
> commercial analysis software, public or controlled-access databases and EHR
> integration.
> **Claim status:** active
> **Scope:** Functional component classes across genomic research and clinical
> use, not a universal deployment.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §4.4.2, printed
> pp. 20–22 (PDF pp. 29–31).
> **Basis / limits:** Component classes are explicit. Report provides no
> representative sample of installations, prevalence estimate, topology or
> current configuration evidence.

## Data and decision dependencies

The ecosystem depends on [AST-0001](../assets/ast-0001-genomic-data.md) as input,
intermediate state and output. Data integrity, availability, confidentiality,
authorization and provenance can matter at multiple transitions; downstream
research or clinical use also depends on correct interpretation and applicable
consent.

> **Claim record — SYS-0003-C02 | source-report**
> **Claim:** The source links sequencing and analysis systems to storage,
> sharing and downstream research/clinical uses, and treats portability,
> privacy, chain of custody, interoperability, consent management and
> reinterpretation as relevant dependencies.
> **Claim status:** active
> **Scope:** Source-reported dependency classes, not an implemented control
> model.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); §3.5, printed p. 11
> (PDF p. 20).
> **Basis / limits:** Source names the dependencies but does not supply a
> validated EHR interface, identity/custody schema or decision-authority map.

## Inventory and responsibility model

IR 8467 recommends inventorying data and metadata, hardware, software,
services, owners, locations, data actions, purposes, flows, dependencies and
data-processing ecosystem parties. This sharpens what a local architecture
assessment should bound without supplying the architecture itself.

> **Claim record — SYS-0003-C04 | source-report**
> **Claim:** NIST IR 8467 2pd recommends organization-specific inventories and
> mappings of genomic-data assets, processing purposes and actions, system and
> service dependencies, internal/external flows, owners and third-party roles.
> **Claim status:** active
> **Scope:** Desired asset/responsibility model for genomic-data processing,
> not evidence of a complete inventory or universal reference architecture.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §1.3, printed p. 5 (PDF p. 16); §2.1, printed p. 9 (PDF p. 20);
> Tables 9–11 and 26–29, printed pp. 57–85 and 141–146
> (PDF pp. 68–96 and 152–157).
> **Basis / limits:** Inventory, mapping and responsibility outcomes are direct.
> The profile reports no asset census, completeness rate, validated flow map,
> identity model, deployment topology or supplier-assurance result.

## Example-applied system mapping

SP 1800-43C applies contextual worksheets and augmented dataflow diagrams to
generalized clinical and research environments. It associates functional
components and material/digital handoffs with managing entities and data
actions, producing a more concrete example of how an organization might bound
the ecosystem for privacy analysis. The exercise does not turn those
components into a normative architecture or establish their configuration,
exposure or control state.

> **Claim record — SYS-0003-C05 | source-report**
> **Claim:** NIST SP 1800-43C demonstrates organization- and use-case-specific
> mapping of genomic-processing components, responsible entities and physical
> or digital dataflows before privacy-threat identification.
> **Claim status:** active
> **Scope:** Generalized sample environments used in the draft exercise, not a
> representative deployment or reusable network design.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §§2.1.2–2.1.4 and Figure 4, printed pp. 8–19 (PDF pp. 17–28);
> static Appendix E.
> **Basis / limits:** The modeling activity and entity/flow association are
> direct. The paper reports no asset census completeness, live topology,
> network exposure, identity/custody validation, control configuration or
> security test. Operational detail is intentionally not reproduced.

## Controlled reverse-direction system evidence

USENIX independently exercises one functional chain: physical sequencing input
becomes digital reads and reaches downstream software. Its separate software
audit and cross-sample measurement show why the instrument→file→parser and
shared-run→sample-association boundaries need explicit defensive treatment.

> **Claim record — SYS-0003-C06 | source-report**
> **Claim:** Ney et al. directly exercise a sequencer-to-derived-file-to-
> downstream-software chain and measure cross-sample output association, while
> their version-bounded software audit identifies unsafe input-handling
> conditions in selected NGS tools.
> **Claim status:** active
> **Scope:** One controlled research setup and selected 2017 software versions;
> not a production topology, current exposure census or validated architecture.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§2.2–2.3, 3, 5–6, printed pp. 767–776 (PDF pp. 4–13).
> **Basis / limits:** Functional chain, measured association errors and audit
> results are direct. The code-execution target was deliberately modified;
> audited real tools produced controlled crashes, not demonstrated execution.

## Candidate interfaces and trust boundaries

Relevant candidate boundaries include device-to-storage, storage-to-analysis,
pipeline-to-reference/resource, organization-to-repository, organization-to-
cloud and genomic result-to-EHR interfaces. Third-party software, external data
holders and cross-organization sharing add responsibility boundaries.

These are candidate interfaces only. No protocol, address, privilege, remote-
access path, product weakness or facility layout is asserted.

> **Claim record — SYS-0003-C03 | analytic-judgment**
> **Claim:** `SRC-0005`–`SRC-0007` are sufficient for a reusable functional
> ecosystem, desired inventory model and bounded example mapping, but
> insufficient for a reference
> network architecture, deployment claim,
> validated trust boundary, vulnerability or control-effectiveness conclusion.
> **Claim status:** active
> **Scope:** Evidence sufficiency after the three NIST/NCCoE genomic source
> transactions.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§2.1–2.3, printed pp. 3–5; §4.4.2, printed pp. 20–22; §5.3 and
> Figure 3, printed pp. 25–26 (PDF pp. 34–35);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> Tables 9–11 and 26–29, printed pp. 57–85 and 141–146;
> [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §§2.1–2.1.4, printed pp. 7–19 (PDF pp. 16–28); static Appendix E.
> **Basis / limits:** Figure 3 is explicitly `notional` and solution-oriented;
> IR 8467 outcomes are draft recommendations; SP 1800-43C applies mapping to a
> bounded example. None is evidence of representative deployment, security
> testing or safeguard effectiveness. Operational protocol, topology and
> access detail are intentionally not reproduced here.

### Covered-system responsibility overlay

Part 202 and the incorporated CISA requirements add a transaction-specific
system boundary: information systems that interact with covered data as part
of a restricted transaction can be covered systems even when data are
encrypted, anonymized, pseudonymized or de-identified. This is a responsibility
boundary, not a reference architecture or claim that every workstation,
sequencer or repository is covered.

> **Claim record — SYS-0003-C07 | source-report**
> **Claim:** The Part 202/CISA lineage defines transaction-specific covered-
> system responsibility around systems interacting with covered data and
> requires organization-, system- and data-level safeguards without supplying
> a deployment topology or complete cybersecurity architecture.
> **Claim status:** active
> **Scope:** Systems involved in a classified restricted transaction; not every
> genomic system or foreign-service relationship.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.201, .248 and corrected .401; CISA requirements, Definitions and
> §§I–II, pp. 2–6.
> **Basis / limits:** System responsibility and control levels are direct.
> Operational topology, configuration and implementation status are withheld
> or absent.

### EHDS EHR and cross-border service classes

EHDS adds EHR systems with mandatory interoperability/logging components,
health-data access services, professional access services, national contact
points, `MyHealth@EU`, health data access bodies, secure processing
environments, `HealthData@EU`, catalogues and Commission central services.
These are legal functional classes, not a deployed EU topology.

> **Claim record — SYS-0003-C08 | source-report**
> **Claim:** EHDS defines interoperating EHR, identity/access, national-contact-
> point, secure-processing, catalogue and Union-platform component/role classes
> across primary and secondary electronic-health-data use.
> **Claim status:** active
> **Scope:** EU regulatory functional architecture; genomic data are one
> eligible data class, not the only object of these systems.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> Articles 2, 23–27, 55–57, 73–75 and 92–96, PDF pp. 31–33, 42–45,
> 60–62, 75–78, 83–87.
> **Basis / limits:** Classes and responsibilities are direct. Implementing
> specifications, current connections, topology and operational conformance
> are absent.

## Security and safety considerations

- A change to pipeline software or configuration may affect both cyber risk and
  analytic reliability; local validation is required.
- Data handling must distinguish technical access from authorized use under
  consent and policy.
- Long retention and later reinterpretation make lifecycle state and provenance
  important, but the current source does not validate an implementation.
- Device or service outage is not automatically a biological or clinical harm;
  a complete consequence path must show the affected workflow and decision.

## Evidence and uncertainty

NIST IR 8432, IR 8467 and SP 1800-43 combine overlapping programme input and
expert/partner analysis. SP 1800-43 adds example-applied system mapping, but
the three source IDs remain one programme lineage. USENIX adds an independent
controlled functional-chain and software-audit lineage without supplying a
representative deployment or validated architecture. None of the sources is a
current topology/exposure census or tested system architecture.

## Related pages

- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)

- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [RSK-0003 — Genomic-data integrity and decision harm](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0004 — Genomic-data disclosure and kin privacy harm](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0020 — Observed account and linked-profile path](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [RSK-0005 — Technically authorized processing and genomic privacy harm](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
- [RSK-0009 — Sequenced input to digital execution](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
- [RSK-0010 — Cross-sample digital exposure](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [RSK-0011 — Part 202 regulated access branches](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md)
- [CTL-0002 — Genomic-data risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [CTL-0003 — Genomic-data privacy threat modeling](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md)
- [CTL-0007 — Secure sequencing input processing](../controls/ctl-0007-secure-sequencing-input-processing.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [CTL-0009 — EHDS safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [GOV-0006 — EU EHDS governance](../governance/gov-0006-eu-ehds-regulation-2025.md)
- [SYN-0004 — US–EU governance reconciliation](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [SRC-0005 — NIST IR 8432](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0007 — NIST SP 1800-43 A/C](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0014 — Ney et al. 2017](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0015 — DOJ final rule and correction chain](../sources/src-0015-us-doj-data-security-program-2025.md)
- [SRC-0016 — EU EHDS Regulation](../sources/src-0016-eu-ehds-regulation-2025.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§2.1–2.3, 3.5, 4.4.2, 5.3; Figures 1 and 3.
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §1.3; Tables 9–11 and 26–29.
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
  Volume C §§2.1–2.1.4 and Figure 4; static Appendix E.
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §§2–3, 5–6.
- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
  §§202.201, .248 and .401; CISA requirements, Definitions and §§I–II.
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md), Articles 2, 23–27,
  55–57, 73–75 and 92–96.
