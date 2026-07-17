---
id: SYS-0005
type: system
title: Connected smart-farm monitoring and equipment ecosystem
aliases:
  - connected smart-farm ecosystem
  - smart agriculture monitoring system class
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
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: SYS-0005-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475; #s4, lines 1693–1698"
  - predicate: depends-on
    target: AST-0003
    claim_id: SYS-0005-C02
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYS-0005-C03
    evidence:
      - source: SRC-0018
        locator: "§2.3.8 and Figure 12, printed pp. 26–28 (PDF pp. 43–45); §§5.3.3 and 5.3.6–5.3.7, printed pp. 81–82 (PDF pp. 98–99)"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: SYS-0005-C04
    evidence:
      - source: SRC-0032
        locator: "Layer model, printed pp. 5, 10 and 13–15 (physical pp. 11, 16 and 19–21); selected Annex A1.1–A2.4 material/Figures 10–13, printed pp. 44–68 (physical pp. 50–74); smart-farming/data-sharing packages, printed pp. 90–99 (physical pp. 96–105)"
  - predicate: governed-by
    target: GOV-0017
    claim_id: SYS-0005-C04
    evidence:
      - source: SRC-0032
        locator: "Governance/data roles and platforms, printed pp. 24–39, 60–68 and 120–129 (physical pp. 30–45, 66–74 and 126–135)"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: SYS-0005-C05
    evidence:
      - source: SRC-0035
        locator: "Main PDF pp. 18–21, 24–35 and 43–49; Annex A §A.1 and related workstreams; APHA PDF pp. 3–7"
tags:
  - agriculture
  - smart-farming
  - monitoring
  - equipment
  - data-exchange
  - conceptual-system
---

# Connected smart-farm monitoring and equipment ecosystem

> Defensive functional class for connected sensing/equipment/automation,
> explicit IoT/SCADA examples, remote sensing, network/cloud analytics,
> registry/traceability and surveillance
> platforms supported by academic and AU strategy lineages. It is not a
> deployed reference architecture or a map of a particular farm.

## Scope

The page covers source-supported system classes needed to inspect how
environmental/crop/livestock observations and digital decisions/access may
interact with production. `SRC-0010` anchors the original connected-monitoring
and equipment class; `SRC-0032` adds connected sensing/equipment/automation,
explicit IoT/SCADA examples, remote-sensing, network/cloud, data-platform,
registry, traceability and early-warning components. `SRC-0035` adds a real
genomic-surveillance platform, repository/data-sharing relationships and the
APHA–milk-processor–government reporting configuration. The page
does not specify a device, controller, protocol, service account, network path,
physical location or operational parameter.

> **Claim record — SYS-0005-C01 | source-report**
> **Claim:** Drape et al. describe smart agriculture through connected remote
> crop/livestock monitoring, equipment, machinery and computers within farms or
> production facilities, plus data exchange with suppliers and vendors.
> **Claim status:** active
> **Scope:** Source-specific system classes, not prevalence, topology or
> validated control authority.
> **As of:** 2021-08-19.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Introduction `#s1`, lines 1472–1473; `#s1-1`, line 1475; Discussion
> `#s4`, lines 1693–1698.
> **Basis / limits:** The component classes and exchange are direct statements.
> The article supplies no inventory, interface, authority, security
> configuration, adoption denominator or technical validation.

## Functional components and dependencies

| Function | Candidate component/dependency | Evidence boundary |
| --- | --- | --- |
| Observe | connected monitoring or sensor information about crops/livestock | Sensor type, calibration and decision relevance unknown |
| Present/manage | computers or other digital tools used by producers/workers | User roles, identity system and automation authority unknown |
| Act/operate | farm equipment or machinery with some digital access dependency | Source does not show whether technology commands, configures or merely observes equipment |
| Exchange | supplier/vendor information relationship | Direction, schema, provenance, authentication and contract unknown |
| Continue/respond | people, expertise, infrastructure and response knowledge | Workshop perceptions, not a verified organizational capability assessment |

> **Claim record — SYS-0005-C02 | analytic-judgment**
> **Claim:** The source supports a candidate monitoring→management→equipment/
> production dependency class that relies on digital, physical, biological and
> human assets in `AST-0003`, but it does not validate any trust boundary or
> prove that a digital state can control a physical action.
> **Claim status:** active
> **Scope:** Minimal defensive system model for `WFL-0007` and `RSK-0007`.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1`, lines 1472–1473; `#s1-1`, line 1475; `#s1-4`, line 1478.
> **Basis / limits:** The functional arrangement is wiki analysis. Connectivity
> does not establish command authority, exploitability, consequence or a shared
> security boundary.

> **Claim record — SYS-0005-C03 | analytic-judgment**
> **Claim:** NIST independently supports generic IIoT, edge/platform,
> distributed and remote-operation system classes relevant to the bounded farm
> model, but not a smart-farm topology, One Health system or control authority.
> **Claim status:** active
> **Scope:** Generic OT/IIoT component applicability to `SYS-0005`.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1`, `#s1-1` and `#s4`;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §2.3.8 and Figure 12, printed pp. 26–28 (PDF pp. 43–45);
> §§5.3.3 and 5.3.6–5.3.7, printed pp. 81–82 (PDF pp. 98–99).
> **Basis / limits:** Generic class overlap is independent/direct; sector
> application is editorial. NIST's Food and Agriculture label alone is not
> workflow, deployment or validation evidence.

## AU functional stack and interfaces

| Layer/function | Source-supported class | Boundary retained |
| --- | --- | --- |
| Observe/identify | ground sensors, remote sensing/satellite, drones, GPS/GIS, farmer/animal IDs, RFID/QR/barcodes | measurement quality, calibration and identity governance remain context-specific |
| Edge/operate | farm equipment, automation, microcontrollers, irrigation/fertilization control and offline devices | command authority, fail-safe state and exact interface are unvalidated |
| Connect | electricity, mobile/fibre/satellite, local/wide/low-power networks and periodic synchronization | intermittent connectivity and provider responsibility are explicit dependencies |
| Store/process | databases, central servers, national data pools, cloud/PaaS and analytics/DSS/AI/ML | hosting, tenancy, model validation and security configuration are unknown |
| Deliver/use | web/mobile apps, SMS/USSD/IVR, advisory, market/finance/insurance, registry and traceability platforms | role, authorization, correction and contractual responsibility vary |
| Coordinate/surveil | climate and pest/disease early-warning, regional data platforms and national↔REC↔AU exchange | platform design is planned/conceptual, not a verified operating network |

One direct functional path is `sensor/observation → transmission → database or
cloud → analytics → farmer/advisory/alert or machine feedback`. Relevant
interfaces are farm/edge↔network/cloud, offline device↔periodic sync, data
provider/owner↔platform/user, agriculture↔ICT authority and national↔regional/
continental platform.

> **Claim record — SYS-0005-C04 | source-report**
> **Claim:** AU DAS adds agriculture-specific connected sensing, equipment,
> automation and explicit IoT/SCADA examples; remote-sensing, network/cloud,
> application, registry, traceability and early-warning platform classes; and
> functional, synchronization, data-ownership and organizational interfaces.
> **Claim status:** active
> **Scope:** Conceptual technology landscape and planned system classes; not a
> deployed topology, validated trust zone, access-control design or prevalence
> claim.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> layer model, printed pp. 5, 10 and 13–15 (physical pp. 11, 16 and 19–21);
> strategy framework, printed pp. 23–24 (physical pp. 29–30); selected Annex
> A1.1–A2.4 material and Figures 10–13, printed pp. 44–68 (physical pp.
> 50–74); smart-farming/
> data-sharing packages, printed pp. 90–99 (physical pp. 96–105).
> **Basis / limits:** Components and interfaces are direct. Broad benefit
> labels for AI/blockchain/cloud are not converted into trust, security or
> performance assurance, and veterinary/plant laboratory architecture remains
> absent.

## PATH-SAFE surveillance systems and boundaries

PATH-SAFE adds a genomic platform for Salmonella, *E. coli* and *Listeria*,
qPCR/sequencing/culture and onsite-diagnostic tool classes, public and partner
laboratories, project-level exchanges/deposits, and an operational bulk-milk
configuration connecting voluntarily participating processors through the
National Milk Records company to the APHA national reference laboratory and
weekly reporting to chief veterinary officers/policy makers.

The same source documents unresolved bilateral agreements, legal/data-
protection interpretation, metadata/linkage/anonymisation, access, ownership,
maintenance, funding and unavailable private veterinary/water-company data.
These are real organizational/data boundaries, not a validated topology or
trust-zone design.

> **Claim record — SYS-0005-C05 | source-report**
> **Claim:** PATH-SAFE directly adds a named genomic-surveillance platform,
> laboratory/diagnostic component classes, project-level exchanges/deposits and
> an operational APHA–National Milk Records–processor–government reporting
> configuration, together with documented unresolved organizational/data-
> sharing boundaries.
> **Claim status:** active
> **Scope:** Represented UK programme and 2024 APHA survey; not a complete
> veterinary/plant-laboratory architecture, validated API/topology, IAM model,
> trust zone or broad business-as-usual adoption.
> **As of:** 2025-03-11.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C04/C05/C06`; main PDF pp. 18–21, 24–35 and 43–49;
> Annex A §A.1 and related workstreams; APHA PDF pp. 3–7.
> **Basis / limits:** Components, roles, exchanges and barriers are direct.
> Main-report `National Milk Laboratories`/`National Milk Records` forms are
> not normalized; the primary APHA identity is used only for its survey.

## Candidate trust boundaries

- monitoring input ↔ operator or management decision;
- legitimate digital access ↔ equipment availability;
- farm/production facility ↔ supplier or vendor;
- equipment/data provider ↔ producer responsibility;
- production system ↔ downstream supply organizations.
- farm/edge/offline device ↔ network/cloud/periodic synchronization;
- data owner/provider ↔ platform operator ↔ advisory or machine user;
- national platform ↔ REC/AU regional or continental platform;
- agriculture authority ↔ ICT/infrastructure and related sector authorities.

All remain candidates. No boundary has source-supported validation, ownership,
interface assurance or observed failure evidence.

## Evidence and uncertainty

The Drape source includes workshop perceptions that some organizations may
lack expertise, infrastructure, current safeguards or clear response plans.
The AU source adds remote-sensing, traceability, surveillance, cloud/identity
and environmental-system classes but reports designs/use cases rather than a
validated deployment. PATH-SAFE adds named deployed surveillance components
and unresolved boundaries, but no cyber vulnerability, IAM/topology or
validated trust-zone finding. Complete veterinary and plant-laboratory
architecture remains unmodeled, and every security trust boundary remains
candidate/unvalidated.

## Related pages

- [SRC-0020 — U.S. National One Health Framework](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)

- [AST-0003 — Smart-farm production and supply assets](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007 — Smart-farm monitoring, production and supply segment](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [RSK-0007 — Farm data/access production and supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [CTL-0005 — Agricultural cyberbiosecurity capability controls](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SRC-0010 — Drape et al. 2021](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0032 — AU Digital Agriculture Strategy](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [GOV-0017 — AU digital-agriculture governance](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md), HTML
  `#s1`, `#s1-1`, `#s1-4`, `#s3-1` and `#s4`.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.8 and 5.3.3/5.3.6–5.3.7.
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
  printed pp. 5, 10, 13–15, 23–24, 44–68 and 90–99.
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md), main PDF
  pp. 18–21, 24–35 and 43–49; Annex A; APHA PDF pp. 3–7.
