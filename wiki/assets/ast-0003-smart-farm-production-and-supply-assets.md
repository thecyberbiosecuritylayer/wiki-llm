---
id: AST-0003
type: asset
title: Smart-farm production and supply assets
aliases:
  - connected agriculture assets
  - smart-farm biological digital and physical assets
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0010
  - SRC-0032
  - SRC-0035
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: AST-0003-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475; #s2-2, line 1538; #s3-3, lines 1565–1571"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: AST-0003-C04
    evidence:
      - source: SRC-0032
        locator: "Figure 2 and text, printed pp. 9–15 (physical pp. 15–21); roles/Figure 8, printed pp. 35–38 (physical pp. 41–44); Annex A1.1–A2.4, printed pp. 43–72 (physical pp. 49–78)"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: AST-0003-C05
    evidence:
      - source: SRC-0035
        locator: "Main PDF pp. 7, 13–19, 22–35; Annex A §§A.1–A.4.5; APHA PDF pp. 1–7"
tags:
  - agriculture
  - smart-farming
  - crops
  - livestock
  - monitoring-data
  - equipment
  - supply-continuity
---

# Smart-farm production and supply assets

> Agriculture-specific asset envelope for crop/livestock/fisheries production,
> environmental/input states, connected monitoring and equipment, operational/
> model/traceability data, organizational capability and value-chain
> continuity. It reconciles a U.S.-centered workshop lineage with an AU regional
> strategy but remains short of a complete One Health asset map.

## Scope

This page preserves the bounded `SRC-0010` classes used by the original
hypothetical data/access→production→supply path, adds direct classes from the
distinct AU regional strategy in `SRC-0032`, and adds PATH-SAFE's implemented
surveillance assets in `SRC-0035`. It now covers crop, livestock and fisheries
production; environmental and input states; pathogens/AMR, biological samples
and isolates; connected and laboratory equipment; genomic, operational,
model, registry and traceability data; downstream value-chain interests; and
the people/organizations using or governing them.

It still does not establish complete seed-asset or herd-record classes, a
complete veterinary/plant-laboratory asset inventory, treatment, regulated
animal movement or disposition. It contains no inventory location, device
configuration, production parameter, sample-level result or identity-level
information.

> **Claim record — AST-0003-C01 | source-report**
> **Claim:** Drape et al. frame smart agriculture around crops and livestock,
> remote monitoring, farm/production-facility equipment and computers,
> operational/company data, supplier/vendor exchange, production or harvest,
> and downstream food-supply stakeholders.
> **Claim status:** active
> **Scope:** Classes named in the 2021 article and 2020 workshop context, not a
> complete sector inventory or proof that every farm has these dependencies.
> **As of:** 2021-08-19.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Introduction `#s1`, lines 1472–1473; `#s1-1`, line 1475;
> Participants `#s2-2`, line 1538; Theme 3 `#s3-3`, lines 1565–1571.
> **Basis / limits:** The classes and exchanges are direct source statements.
> Exact records, ownership, architecture, value, current adoption and
> dependency strength are not reported.

## Asset classes and states

| Class | Relevant trustworthy/available state | Evidence boundary |
| --- | --- | --- |
| Crops and livestock | Production state can be observed and managed without an unrecognized digital error becoming a biological/physical action | No species, herd, field, health or welfare endpoint is studied |
| Harvest or production output | Output remains usable and available for the intended downstream flow | No quantity, quality, safety or loss measure is supplied |
| Monitoring/sensor data | Data are timely, attributable and sufficiently trustworthy for their intended decision | The source names false sensor data as a potential risk but validates no sensor or dataset |
| Operational and agricultural-company data | Legitimate users retain appropriate access and integrity for production/business use | No data schema, sensitivity classification or privacy population is defined |
| Equipment, machinery and computers | Legitimate operation remains available and aligned with safe production needs | No device, controller, protocol, topology or exposure is named |
| Supplier/vendor information exchange | Information needed across an organizational boundary retains appropriate provenance and availability | Direction, interface, contract and trust model are unknown |
| Human and organizational capability | Producers/workers can recognize, escalate and respond to a relevant issue | Workshop perceptions do not establish capability at a named organization |
| Supply continuity | Production output can move to downstream businesses and consumers | This is an affected interest, not a single fungible inventory or measured service level |

The table separates biological/physical production state, digital information,
equipment, people/capability and continuity interests. It does not imply that
all are connected to one network or controlled by the same party.

> **Claim record — AST-0003-C02 | analytic-judgment**
> **Claim:** The source supports a coupled but non-exhaustive asset envelope in
> which digital monitoring/access, physical equipment and crop/livestock
> production can share one decision or continuity path while remaining distinct
> asset classes.
> **Claim status:** active
> **Scope:** Wiki organization of the source-supported smart-farm segment, not
> a reference architecture or complete One Health map.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1`, lines 1472–1473; `#s1-1`, line 1475; `#s1-4`, line 1478;
> Discussion `#s4`, lines 1693–1698.
> **Basis / limits:** The source links technology/data, production and supply
> concerns but does not publish this asset taxonomy, validate coupling or show
> a complete consequence chain. Separate classes prevent connectivity from
> being mistaken for shared ownership or deterministic impact.

## AU regional extension

| Added class | Relevant trustworthy/available state | Evidence boundary |
| --- | --- | --- |
| Fisheries production and food outputs | Observation, production and value-chain state remain attributable and usable | Fisheries are in scope; no complete aquaculture/wildlife-health inventory is supplied |
| Soil, land, water, weather/climate, crop health and biodiversity | Environmental/input observations retain time, location, method, validation and decision context | Strategy classes, not a validated environmental-sampling programme |
| Fertilizer, pesticide, feed and water inputs | Intended identity/quality/application state is preserved across a production decision | No formulation, dose, setpoint or product-specific control is recorded here |
| Farmer/animal IDs, registries and profiles | Identity and eligibility/traceability records retain provenance, access and correction context | No personal record, national implementation or universal identifier is inferred |
| Traceability, certification, payment, insurance and market data | Records remain attributable across farm, platform and value-chain boundaries | Proposed/use-case classes, not a custody audit or verified market outcome |
| Remote-sensing, sensor, model and early-warning data | Observations, transformations and outputs remain valid for their intended decision | No model validation, alert performance or deployment denominator is supplied |
| AU/REC/Member-State and cross-sector authorities | Continental, regional and national role/action levels remain distinguishable | Strategy roles are not RACI, legal delegation or enforcement proof |

> **Claim record — AST-0003-C04 | source-report**
> **Claim:** AU DAS broadens the canonical agriculture asset/stakeholder map to
> crop, livestock and fisheries production; soil/land/water/weather/crop-health
> states; inputs and equipment; identity/registry, model, traceability,
> certification and financial data; value-chain actors; and AU/REC/national
> authorities.
> **Claim status:** active
> **Scope:** Classes directly named by the AU strategy and retained separately
> from the original Drape envelope; not a complete One Health asset map or
> proof of deployment.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> Figure 2 and related text, printed pp. 9–15 (physical pp. 15–21); roles and
> Figure 8, printed pp. 35–38 (physical pp. 41–44); Annex A1.1–A2.4, printed
> pp. 43–72 (physical pp. 49–78).
> **Basis / limits:** Named classes are direct. Seeds/genomes, biological
> samples, named pathogens, veterinarians/laboratories, wildlife and complete
> disposition remain absent or too weak in this source and are not invented.

## PATH-SAFE surveillance extension

PATH-SAFE adds named foodborne pathogens and AMR; animal, food, wastewater,
shellfish and environmental samples; isolates, genome sequences, phenotypes,
metadata and analytical outputs; qPCR/sequencing/culture methods; genomic and
source-attribution models; a genomic data platform; APHA/Defra/FSA/VMD/UKHSA
and other public authorities; processors, laboratories, researchers and
private-sector partners; and human, livestock, food-chain, aquatic and
environmental affected interests.

> **Claim record — AST-0003-C05 | source-report**
> **Claim:** PATH-SAFE directly adds pathogens/AMR, biological samples,
> isolates, genomic/metadata/model assets, laboratory and surveillance tools,
> veterinary/public authorities, processors/researchers and human, animal,
> food-chain and environmental interests to the canonical agriculture asset
> envelope.
> **Claim status:** active
> **Scope:** Represented 2021–2025 PATH-SAFE projects and the bounded 2024 APHA
> bulk-milk survey; not a universal UK inventory, sample-level dataset or
> complete seed-asset/herd-record and veterinary/plant-laboratory map.
> **As of:** 2025-03-11.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C03/C05/C06`; main PDF pp. 7, 13–19, 22–35; Annex A
> §§A.1–A.4.5; APHA PDF pp. 1–7.
> **Basis / limits:** Asset and stakeholder classes are direct across one UK
> programme/application package. It materially fills prior gaps but does not
> supply complete seeds or herd records, and one programme line cannot by
> itself complete every SF2 class.

## Stakeholders

Across the three represented agriculture lines, named or invited actors
include:

- farmers/producers and farm workers;
- agribusinesses, food manufacturers and commodity boards;
- suppliers, vendors and auxiliary companies;
- technology and cybersecurity providers;
- universities and researchers;
- state/federal agencies and law enforcement;
- downstream businesses, communities and consumers.
- livestock keepers, fisherfolk, cooperatives, extension/advisory services,
  processors, transport/storage and market actors;
- AUC/AUDA-NEPAD, RECs, Member-State agriculture/ICT and related ministries,
  civil society, researchers and multilateral/development partners.
- APHA, Defra, FSA/FSS, VMD, UKHSA and partner laboratories; milk processors,
  veterinary/public-health authorities and programme data users.

Plant-health professionals, practising veterinarians, laboratory custodians
and ecosystem rights/interests are still not developed as a complete SF2
actor map. Authority and partner names do not create a statutory RACI or prove
universal participation.

> **Claim record — AST-0003-C03 | source-report**
> **Claim:** Workshop discourse treated expertise, infrastructure, training,
> response knowledge and the ability of smaller producers to invest as relevant
> organizational capability constraints.
> **Claim status:** active
> **Scope:** Participant perceptions in one workshop, not a verified maturity
> assessment or prevalence estimate.
> **As of:** 2020-10-07.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Theme 1 `#s3-1`, lines 1547–1556; Discussion `#s4`, line 1694.
> **Basis / limits:** The perceptions are direct findings of the qualitative
> study. Anonymous quotations and missing denominators do not identify which
> organizations lack which capability.

## Security, safety and quality properties

- **availability:** legitimate users can access required data/equipment in time
  for the bounded production activity;
- **integrity/authenticity:** monitoring and operational data are sufficiently
  trustworthy for their intended use;
- **provenance:** supplier/vendor and monitoring information retains source and
  decision context;
- **physical/biological safety:** digital actions must not silently override
  locally necessary production, animal/plant-health or worker safeguards;
- **continuity:** a local disruption should not propagate unnecessarily into
  downstream product movement;
- **confidentiality/IP:** the source raises company-data concerns, but supplies
  no classified dataset, observed disclosure or privacy outcome.

## Evidence and uncertainty

The page now uses a Virginia Tech programme/workshop, an African Union regional
strategy and a UK programme/application package. Independence is claim-
specific: AU material cites/derives background sources, and FSA/RAND, APHA/
Defra and the 2026 issuer blog have different roles without becoming blanket-
independent confirmation. PATH-SAFE adds direct genomic/sample and bounded
implementation evidence, while complete seeds/herd records, veterinary/plant-
laboratory breadth, operational inventories and independent effectiveness
remain required.

## Related pages

- [SRC-0021 — Quadripartite scope/implementation guide](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md)
- [SYN-0009 — reconciled One Health scope and explicit asset gaps](../syntheses/syn-0009-global-us-one-health-scope-reconciliation.md)
- [SRC-0020 — U.S. National One Health Framework](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)

- [WFL-0007 — Smart-farm monitoring, production and supply segment](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYS-0005 — Connected smart-farm ecosystem](../systems/sys-0005-connected-smart-farm-ecosystem.md)
- [RSK-0007 — Farm data/access production and supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [RSK-0017 — Agriculture cyber disruption to production/supply](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0005 — Agricultural cyberbiosecurity capability controls](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SRC-0010 — Drape et al. 2021](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0032 — AU Digital Agriculture Strategy](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [GOV-0017 — AU digital-agriculture governance](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md)
- [HAZ-0003 — Non-adversarial sensor/data-quality hazard](../hazards/haz-0003-agriculture-sensor-and-data-quality-failure.md)
- [HAZ-0004 — Ecological and supply hazards](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md)
- [INC-0004 — JBS cattle-processing disruption](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md)
- [INC-0005 — Anonymous chicken-farm animal-effect incident](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
- [RSK-0018 — Poultry-barn cyber-to-animal path](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md), HTML
  `#s1`, `#s1-1`, `#s1-4`, `#s2-2`, `#s3-1`, `#s3-3` and `#s4`.
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
  printed pp. 9–15, 35–38 and 43–72.
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md), main PDF
  pp. 7, 13–19, 22–35; Annex A §§A.1–A.4.5; APHA PDF pp. 1–7.
