---
id: CON-0001
type: concept
title: Cyberbiosecurity
aliases:
  - cyberbiosecurity
  - cyber-biosecurity
status: active
created: 2026-07-11
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0001
  - SRC-0002
  - SRC-0004
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0001
    claim_id: CON-0001-C01
    evidence:
      - source: SRC-0001
        locator: "§ Introduction, first paragraph"
  - predicate: evidenced-by
    target: SRC-0002
    claim_id: CON-0001-C04
    evidence:
      - source: SRC-0002
        locator: "Abstract; § Introduction, second paragraph; § Methods — Asset-impact analysis"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: CON-0001-C05
    evidence:
      - source: SRC-0004
        locator: "Glossary, printed pp. xiii–xiv (PDF pp. 15–16); §1 and Figure 1.1, printed pp. 1–3 (PDF pp. 21–23)"
tags:
  - cyberbiosecurity
  - foundations
---

# Cyberbiosecurity

> In this wiki, **cyberbiosecurity** is the operational field concerned with
> analyzing coupled risks in which digital and biological systems are linked by
> a dependency or consequence-transfer mechanism, such that a change in the
> state of one can affect the other.

This is the wiki's editorial boundary, not a claim that the definition is
universally accepted.

## Scope

The following criteria are an editorial rule for the information architecture,
not a finding from `SRC-0001`, `SRC-0002`, or `SRC-0004`. A topic falls within
the scope of this wiki when it explicitly connects:

1. a biological or biotechnology asset, workflow, system, stakeholder, or
   consequence;
2. a digital dependency, data flow, trust boundary, cyber threat,
   vulnerability, or control; and
3. an implication for security, privacy, safety, quality, resilience, or
   governance.

> [!NOTE]
> **Editorial convention**
> The model allows transitions in both directions: a digital state may affect a
> biological process or decision, while a biological input or failure may
> affect analysis, software, or a digital decision. This is not a finding from
> Murch et al.; the evidentiary boundaries must be established separately for
> each risk scenario.

General cybersecurity without a biological connection, and general biosafety
or biosecurity without a digital dependency, are adjacent but do not
automatically fall within scope. WHO 2024 now provides a direct international
laboratory baseline; it shows a continuum and overlap, not a universal boundary
for every sector and jurisdiction.

## Source definitions

> **Claim record — CON-0001-C01 | source-report**
> **Claim:** Murch et al. proposed cyberbiosecurity as a hybrid discipline at
> the intersection of cybersecurity, cyber-physical security, and biosecurity;
> their initial definition encompasses vulnerabilities and protective measures
> in connected life-science, medical, cyber, cyber-physical, supply-chain, and
> infrastructure systems.
> **Claim status:** active
> **Scope:** The definition proposed by a specific group of authors in 2018.
> **As of:** 2018-04-05.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Introduction, first paragraph.
> **Basis / limits:** The source is primary evidence for the authors' own
> definition, but it does not establish international or interdisciplinary
> consensus.

> **Claim record — CON-0001-C02 | analytic-judgment**
> **Claim:** The Murch et al. definition is useful as a historical and initial
> framing of the field, but it is insufficient as the sole canonical definition
> for a global wiki.
> **Claim status:** active
> **Scope:** Editorial application of the source in this wiki.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Introduction, first paragraph;
> [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Introduction, second paragraph; § Methods — Asset-impact analysis.
> **Basis / limits:** Murch et al. describe their own definition as initial and
> expect it to evolve. Crawford et al. operationalize a later HCL framing but
> directly cite Murch; this is the same definitional lineage, not independent
> evidence of global consensus.

> **Claim record — CON-0001-C04 | source-report**
> **Claim:** Crawford et al. describe cyberbiosecurity as identifying and
> assessing risks at the interfaces among cybersecurity, cyberphysical
> security, biosecurity, and biosafety, and as developing controls to prevent,
> detect, respond, and recover; in HCLs, they operationalize this through
> asset-impact analysis.
> **Claim status:** active
> **Scope:** A source-specific 2023 HCL framing derived from Murch et al.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Abstract; § Introduction, second paragraph; § Methods — Asset-impact
> analysis.
> **Basis / limits:** The source is primary evidence for its own
> operationalization, but it directly cites the Murch definition and is neither
> an independent definitional lineage nor a normative consensus.

## Current understanding

The initial framing is useful in two respects. First, it does not reduce the
field to the confidentiality of biological data: cyber-physical, supply-chain,
and facility dependencies also come into view. Second, it directs analysis not
only toward threats but also toward prevention, protection, mitigation,
investigation, and attribution
([SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Introduction,
first paragraph).

Crawford et al. add a laboratory-specific operationalization: first identify
the workflow and cyber or cyberphysical assets, then consider potential impacts
from loss of confidentiality, integrity, or availability. This broadens the
concept's practical application but does not alter its normative status
(`CON-0001-C04`;
[SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Methods — Asset-impact analysis; Figure 1).

WHO 2024 adds direct normative terminology for adjacent domains: biosafety
focuses on unintentional exposure and inadvertent release; laboratory
biosecurity concerns the protection, control, and accountability of material,
technology, and information; and cybersecurity includes equipment and building
systems. WHO also describes biosafety and biosecurity as a continuum, so this
baseline clarifies the scope but does not turn the editorial definition in
`CON-0001` into a global consensus
([SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
Glossary, printed pp. xiii–xiv; §1, printed pp. 1–3; Figure 1.1).

> **Claim record — CON-0001-C05 | source-report**
> **Claim:** WHO 2024 defines biosafety, laboratory biosecurity, and
> cybersecurity as overlapping but distinct scopes and explicitly includes
> connected laboratory equipment and building systems in the cyber context.
> **Claim status:** active
> **Scope:** Direct WHO laboratory terminology, not a definition of the term
> `cyberbiosecurity` itself and not a universal legal consensus.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> Glossary, printed pp. xiii–xiv (PDF pp. 15–16); §1 and Figure 1.1,
> printed pp. 1–3 (PDF pp. 21–23).
> **Basis / limits:** The definitions and cyber-laboratory scope are direct.
> WHO does not use them to endorse Murch's definition or claim global adoption
> of `cyberbiosecurity`.

Under the wiki's editorial contract, every risk page must separately identify
the asset or workflow, digital dependency, initial state change, mechanism of
cross-domain transfer, downstream consequence, evidence, and evidenced control
edge—or an explicit gap if no supported control exists. This is a modeling rule,
not a source-reported finding of the article.

## Evidence and uncertainty

As of 2026-07-12, this page relies on two linked scholarly framings and one
direct WHO normative terminology source. `SRC-0002` directly develops the Murch
et al. framing in an HCL context and is therefore not an independent
definitional lineage. `SRC-0004` independently defines adjacent domains but not
the term `cyberbiosecurity` itself, and it does not demonstrate global adoption
(`CON-0001-C02`, `CON-0001-C04`, `CON-0001-C05`). Until a jurisdictional and
sectoral comparison is available:

- this definition should not be described as universally accepted;
- the boundaries with biosafety, biosecurity, and cybersecurity rely on a WHO
  laboratory baseline but remain editorial outside its scope; and
- the sector list should be read as a proposed scope, not as evidence that risk
  is uniform across sectors.

## Terminology overlap and evidence gap

Murch et al. include accidental release of infectious-disease pathogens or
their by-products, such as toxins, in their brief description of biosecurity.
The editorial contract for this wiki instead classifies accidental exposure,
release, or harm as biosafety, while associating biosecurity with unauthorized
access, loss, theft, misuse, diversion, or intentional release. The formulations
serve different purposes and scopes, so this is terminological overlap rather
than evidence of conflicting practical requirements
([SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Background,
first paragraph). Crawford et al., by contrast, restate a clearer WHO-derived
distinction. Direct WHO 2024 evidence now supports the biosafety definition;
its Glossary includes intentional **or accidental unauthorized access** within
biosecurity, while §§5.1 and 5.3 separately classify the accidental release or
loss of biosecurity-relevant material as biosecurity risks or incidents.
Accordingly, direct normative evidence does not eliminate the overlap but makes
it explicit
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Introduction, second paragraph;
[SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
Glossary, printed p. xiii; §1, printed pp. 1–3; §§5.1, 5.3, printed
pp. 19–22).

> **Claim record — CON-0001-C03 | analytic-judgment**
> **Claim:** The source-specific description of biosecurity in Murch et al.
> overlaps the wiki's editorial biosafety boundary, and the corpus available at
> the time was insufficient to resolve that overlap normatively.
> **Claim status:** superseded
> **Scope:** Comparison of terminology in the corpus before direct WHO ingest.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-07.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Background, first paragraph;
> [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Introduction, second paragraph.
> **Basis / limits:** The overlap follows directly from including accidental
> release in the source-specific description of biosecurity and from the wiki's
> editorial distinction. It does not establish which terminology prevails in
> international or jurisdiction-specific normative sources; that issue is
> tracked in [QUE-0001](../questions/que-0001-domain-boundaries.md).
> **Superseded by:** `CON-0001-C06` following direct ingestion of WHO 2024.

> **Claim record — CON-0001-C06 | analytic-judgment**
> **Claim:** Direct WHO 2024 evidence partially resolves the normative evidence
> gap, but source-specific overlap remains: WHO includes accidental unauthorized
> access and separately treats accidental release or loss of
> biosecurity-relevant material as biosecurity risks or incidents; a universal
> jurisdictional or sectoral boundary remains unestablished.
> **Claim status:** active
> **Scope:** Reconciliation of the wiki's editorial boundary, scholarly
> framings, and WHO laboratory guidance.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Background, first paragraph;
> [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Introduction, second paragraph;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> Glossary, printed pp. xiii–xiv; §1, printed pp. 1–3; §§5.1, 5.3,
> printed pp. 19–22.
> **Basis / limits:** WHO supplies direct authoritative definitions for its own
> laboratory context. A single issuer and context cannot establish universal
> usage; the comparison remains tracked in `QUE-0001`.

**Question status:** open, partially resolved. Resolution requires a comparison
of current normative definitions, as described in
[QUE-0001](../questions/que-0001-domain-boundaries.md).

## Related pages

- [SRC-0001 — Murch et al. 2018](../sources/src-0001-murch-cyberbiosecurity-2018.md)
- [SRC-0002 — Crawford et al. 2023](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0004 — WHO Laboratory Biosecurity Guidance 2024](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [GOV-0001 — WHO Laboratory Biosecurity Guidance 2024](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [WFL-0001 — Systems model of a biomanufacturing facility](../workflows/wfl-0001-biomanufacturing-system.md)
- [WFL-0002 — HCL cyber-physical workflow](../workflows/wfl-0002-high-containment-laboratory.md)
- [QUE-0001 — Normative boundaries between adjacent domains](../questions/que-0001-domain-boundaries.md)

## Sources

- [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), §§ Introduction,
  Background, Moving cyberbiosecurity forward.
- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
  Abstract; §§ Introduction, Methods — Asset-impact analysis.
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
  Glossary, printed pp. xiii–xiv; §1 and Figure 1.1.
