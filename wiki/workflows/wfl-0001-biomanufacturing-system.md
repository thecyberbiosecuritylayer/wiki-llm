---
id: WFL-0001
type: workflow
title: Systems model of one biomanufacturing facility
aliases:
  - Biomanufacturing test bed in Murch et al.
  - Murch et al. biomanufacturing test bed
status: active
created: 2026-07-11
updated: 2026-07-11
last_reviewed: 2026-07-11
review_after: 2027-01-11
source_ids:
  - SRC-0001
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0001
    claim_id: WFL-0001-C01
    evidence:
      - source: SRC-0001
        locator: "§ Adding another dimension, paragraph beginning ‘The bioprocess development/bioproduction facility…’"
tags:
  - biomanufacturing
  - workflow
  - cyber-physical
---

# Systems model of one biomanufacturing facility

> Murch et al. present one undisclosed biomanufacturing facility as a system
> that connects bioprocess development, GMP scale-up, a stage carrying the
> source label `Bulk Drug & Documents`, the supply chain, personnel, equipment,
> information systems, and physical infrastructure.

This page reconstructs the systems framing of one facility used as a test bed.
It is not a universal reference architecture for all manufacturing facilities.

## Scope and unit of analysis

The facility developed and manufactured clinical batches of protein
biotherapeutic products and accompanying documentation for commercial and
government clients. The authors do not identify the facility and publish only
a high-level overview
([SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Adding another
dimension, paragraph beginning “The bioprocess development/bioproduction
facility…”).

## Stages and system elements

The main text directly identifies four interconnected subsystems:

1. end-to-end bioprocess development and biomanufacturing;
2. the supply chain;
3. supporting information systems and cyber-physical interfaces with the
   process; and
4. facility infrastructure and its connection to host-facility infrastructure.

Figure 1 separately shows the main path `Bioprocess Development → GMP Scale-Up
→ Bulk Drug & Documents`. The source does not define `Bulk Drug` as a
regulatory category or explain its relationship to the figure's other
labels—`End Product` and `Final Product Storage`—so this page equates it with
neither drug substance nor finished drug product. The diagram also names the
following cross-cutting elements: personnel; critical instrumentation and
equipment; facility and infrastructure; access control and physical security;
raw materials and supplies management; data and knowledge management of
critical IP; final-product storage; instrument service and calibration;
bio-cyber-physical interfaces; internal IT; and external IT interfaces and
services (`WFL-0001-C07`;
[SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), Figure 1 and
§ Adding another dimension).

The authors call the labels surrounding the central diagram **defensive sets**.
They are potential directions for protection, not system dependencies. They
could be modeled as source-recommended or proposed controls with explicitly
unknown effectiveness, but they remain on the source and workflow pages because
they are too broad and insufficiently specified for separate `CTL` pages.

## Trust boundaries and process interfaces

The source does not provide a formal trust-boundary, data-flow, or network
model. For further analysis, Figure 1 supports only **candidate surfaces**, which
should be divided into two groups:

- **External interfaces and access surfaces labeled in the diagram:**
  client-provided source materials; visitors and on-site access; external IT
  interfaces and services; and the end product and final documentation provided
  to a client and government regulator. VPN is mentioned only in one external
  defensive-set label; the figure does not establish that it was a deployed
  dependency at this facility.
- **Internal process transitions:** arrows between `Bioprocess Development`,
  `GMP Scale-Up`, and `Bulk Drug & Documents`. They show the sequence of stages
  but do not, by themselves, establish a change in trust, authority, or custody,
  or a specific flow of data or material.

This limited decomposition is formalized in `WFL-0001-C06`; verified trust
boundaries require additional architectural or workflow evidence
([SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), Figure 1 and
§ Adding another dimension).

## Evidence and uncertainty

> **Claim record — WFL-0001-C01 | source-report**
> **Claim:** The authors report that they studied the facility as four
> interconnected subsystems: end-to-end bioprocess development and
> biomanufacturing, the supply chain, supporting information systems with
> cyber-physical interfaces, and facility and host-facility infrastructure.
> **Claim status:** active
> **Scope:** One test-bed facility producing clinical batches of protein
> biotherapeutics.
> **As of:** 2018-04-05.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Adding another dimension, paragraph beginning “The bioprocess
> development/bioproduction facility…”.
> **Basis / limits:** The high confidence applies to the authors' description;
> neither the facility nor the completeness of the four-part model has been
> independently verified.

> **Claim record — WFL-0001-C02 | source-report**
> **Claim:** The authors state that vulnerabilities may exist throughout the
> system and that personnel and physical-security considerations cannot be
> excluded from the analysis.
> **Claim status:** active
> **Scope:** High-level results from the analysis of the same facility.
> **As of:** 2018-04-05.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Adding another dimension, list following Figure 1.
> **Basis / limits:** The publication does not provide a list of results or
> assessment criteria, so the claim cannot be generalized to prevalence across
> the industry.

> **Claim record — WFL-0001-C03 | analytic-judgment**
> **Claim:** For defensive threat modeling of this process, the system boundary
> should be drawn more broadly than the IT perimeter and should include
> material, data, control, custody, people, and infrastructure dependencies.
> **Claim status:** superseded
> **Scope:** An initial model of one biomanufacturing facility, not a finished
> industry reference model.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> Figure 1; § Adding another dimension, description of the four subsystems and
> overarching findings.
> **Basis / limits:** The conclusion follows from the interdependencies in the
> diagram, but its external validity has not yet been tested against other
> sources.
> **Superseded by:** `WFL-0001-C05`.
> **Supersession reason:** Figure 1 does not establish distinct control or
> custody flows; the replacement claim retains only directly supported
> categories.

> **Claim record — WFL-0001-C04 | analytic-judgment**
> **Claim:** Figure 1 supports a working identification of five classes of
> trust boundary: external inputs from a supplier or client; employee and
> visitor access; external network and service interfaces; transitions among
> bioprocess development, GMP scale-up, and bulk drug and documents; and
> outbound flows to the client or regulator.
> **Claim status:** superseded
> **Scope:** An analytical decomposition of the published top-level diagram of
> one test-bed facility.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> Figure 1 and § Adding another dimension, description of the facility and four
> subsystems.
> **Basis / limits:** The boundaries are inferred from labeled interfaces and
> process direction; the source does not call them a formal trust-boundary
> taxonomy, claim completeness, or retain Figure 1's pixels locally.
> **Superseded by:** `WFL-0001-C06`.
> **Supersession reason:** The initial claim combined external defensive-set
> labels, central system labels, and internal process transitions, giving them
> stronger trust-boundary and data-flow semantics than the source supports.

> **Claim record — WFL-0001-C05 | analytic-judgment**
> **Claim:** For defensive scoping of this test bed, the source supports a
> system boundary broader than the IT perimeter: it encompasses the bioprocess,
> materials and supplies, data and IP, people, equipment, physical
> infrastructure, and internal and external IT interfaces.
> **Claim status:** active
> **Scope:** An initial model of one undisclosed biomanufacturing facility, not
> an industry reference architecture.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> Figure 1; § Adding another dimension, paragraph beginning “The bioprocess
> development/bioproduction facility…”.
> **Basis / limits:** The categories are directly named in the text or diagram,
> but the publication does not provide a complete architecture, data lineage,
> or evidence of the model's external validity.

> **Claim record — WFL-0001-C06 | analytic-judgment**
> **Claim:** Figure 1 supports a working distinction between external candidate
> interfaces and access surfaces and internal process transitions, but not a
> formal five-class trust-boundary or data-flow taxonomy.
> **Claim status:** active
> **Scope:** An analytical decomposition of a top-level diagram of one test-bed
> facility.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> Figure 1 and its caption.
> **Basis / limits:** The figure visually separates external defensive sets,
> central system labels, and arrows between stages. It does not define trust
> levels, privileges, protocols, data or material flow directions, or interface
> completeness. The candidate-interface classification remains an analytical
> inference, so overall confidence is medium.

> **Claim record — WFL-0001-C07 | source-report**
> **Claim:** Figure 1 shows the central sequence `Bioprocess Development → GMP
> Scale-Up → Bulk Drug & Documents`, cross-cutting elements involving people,
> equipment, materials and supplies, data and IP, facilities, security,
> internal and external IT, and bio-cyber-physical interfaces, while its caption
> calls the external directions defensive sets.
> **Claim status:** active
> **Scope:** A systems-view diagram of one undisclosed test-bed facility.
> **As of:** 2018-04-05.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> Figure 1 and its caption; JPEG provenance is given in the source note.
> **Basis / limits:** The claim conveys the visible labels and composition of
> the figure. The pixels remain a transient external component; the diagram
> does not define `Bulk Drug` as a regulatory category and is not a validated
> reference architecture.

> **Claim record — WFL-0001-C08 | source-report**
> **Claim:** The authors identify possible consequences including theft of
> intellectual property, supply-chain disruption, manipulation of bioprocess
> development or bioproduction, cyberattacks on key IT or cyber-physical
> interfaces, corruption of critical data, and manipulation of security systems
> and infrastructure.
> **Claim status:** active
> **Scope:** Possible consequence classes in the introduction to the facility
> analysis, not documented incidents or established end-to-end attack paths.
> **As of:** 2018-04-05.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Adding another dimension, first paragraph.
> **Basis / limits:** The high confidence applies to the source's list of
> possibilities, not their likelihood, prevalence, feasibility, or scale.

> **Claim record — WFL-0001-C09 | source-report**
> **Claim:** The authors recommend facility-tailored multidisciplinary
> analysis, potentially combining several defensive approaches, developing and
> validating assessment methods or protocols, and considering guidelines or
> standards to promote consistent, high-quality assessments.
> **Claim status:** active
> **Scope:** Source recommendations derived from one undisclosed facility
> analysis.
> **As of:** 2018-04-05.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Adding another dimension, final three paragraphs.
> **Basis / limits:** The source provides no implementation evidence, testing
> outcomes, or independent assessment of effectiveness; the claim records
> recommendations, not demonstrated effectiveness.

## Consequence surfaces

The article identifies possible consequences including theft of intellectual
property, supply-chain disruption, manipulation of bioprocess development or
biomanufacturing, corruption of critical data, and manipulation of security
systems. These are consequence classes, not documented incidents or established
attack paths (`WFL-0001-C08`;
[SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Adding another
dimension, first paragraph).

Separate risk-scenario pages should be created only when evidence becomes
available for the preconditions, transfer mechanism, receiving-domain state,
and downstream consequences.

## Defensive implications

The authors **recommend**, rather than demonstrate as effective:

- conducting a comprehensive, multidisciplinary assessment tailored to the
  facility;
- combining multiple defensive approaches where one measure is insufficient;
- developing and validating assessment methods or protocols; and
- considering guidelines or standards that would support consistency and
  quality in analysis, including assessor qualifications and the quality or
  effectiveness of adopted measures.

These recommendations should not be converted into evidence of control
effectiveness without further research (`WFL-0001-C09`;
[SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Adding another
dimension, final three paragraphs).

## Assumptions and limits

- Only one source and one undisclosed facility are available.
- The detailed method, list of results, and criteria for an acceptable security
  state were not published.
- Figure 1 is a high-level conceptual diagram, not a data-flow diagram or a
  validated reference architecture.
- The publication reports no likelihood estimates, consequence magnitude, or
  control effectiveness.
- The page intentionally does not consolidate operational attack sequences; its
  purpose is defensive definition of the system scope and candidate interfaces.

## Related pages

- [CON-0001 — Cyberbiosecurity](../concepts/con-0001-cyberbiosecurity.md)
- [WFL-0002 — HCL cyber-physical workflow](wfl-0002-high-containment-laboratory.md)
- [WFL-0003 — Information and control flows in biopharmaceutical manufacturing](wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [SRC-0001 — Murch et al. 2018](../sources/src-0001-murch-cyberbiosecurity-2018.md)

## Sources

- [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Adding another
  dimension; Figure 1.
