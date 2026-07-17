---
id: SYS-0011
type: system
title: Biological AI data–compute–model–laboratory ecosystem
aliases:
  - biological AI system and supply-chain map
  - life-science AI ecosystem
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0034
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: SYS-0011-C01
    evidence:
      - source: SRC-0033
        locator: "Chapter 5, printed pp. 65–77 (physical pp. 86–98), especially Figures 5-1–5-2 and Boxes 5-1–5-3"
  - predicate: depends-on
    target: AST-0008
    claim_id: SYS-0011-C02
    evidence:
      - source: SRC-0033
        locator: "Chapters 2, 4 and 5, printed pp. 19–25, 46–59 and 64–77 (physical pp. 40–46, 67–80 and 85–98)"
  - predicate: evidenced-by
    target: SRC-0034
    claim_id: SYS-0011-C05
    evidence:
      - source: SRC-0034
        locator: "Figure 1, p. 3; §§4 and 6, pp. 6–10; Appendix §§A.3.3–A.4, pp. 32–34"
tags:
  - artificial-intelligence
  - biological-models
  - system-boundaries
  - software-supply-chain
  - cloud
  - hpc
  - laboratories
---

# Biological AI data–compute–model–laboratory ecosystem

## Scope

This conceptual system page preserves NASEM's data, AI and application layers,
the digital-to-physical laboratory boundary and ProteinGym's bounded benchmark
resource instance. It is not a site topology, implementation reference
architecture, model registry, software inventory or automation blueprint. No
endpoint, credential, sequence, model weight, laboratory parameter or target-
specific weakness is included.

> **Claim record — SYS-0011-C01 | source-report**
> **Claim:** NASEM represents a biological-AI ecosystem that connects data
> repositories and labels, cloud/HPC and storage, model/software layers,
> researchers and access bodies, APIs/workbenches, design/analysis
> applications, instruments and physical laboratories.
> **Claim status:** active
> **Scope:** Conceptual system classes and dependencies; not one deployed
> system, validated interface, complete supply chain or current inventory.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 2 and 4, printed pp. 19–25 and 46–59 (physical pp. 40–46 and
> 67–80); Chapter 5, printed pp. 65–77 (physical pp. 86–98), especially
> Figures 5-1–5-2 and Boxes 5-1–5-3; Appendix A, printed pp. 85–124 (physical
> pp. 106–145).
> **Basis / limits:** Main-report layers and resources are direct; Appendix A
> adds attributed technical background. Conceptual classes do not show that
> every component is present, connected, authorized or securely configured.

## System and dependency map

| Layer | System classes | Primary dependencies | Boundary retained |
| --- | --- | --- | --- |
| Biological/experimental input | specimens/material-derived measurements, sequence/structure/function/omics, epidemiological and experimental-result data | instruments, laboratories, repositories, metadata and provenance | biological/material state is distinct from its digital representation |
| Data stewardship | public/federal/private databases, repositories, curation, storage, access committees and data stewards | identity/credentials, policy, metadata, quality and retention | FAIR does not mean open; repository does not mean model registry |
| Compute/environment | local/cloud/HPC resources, sandboxed workbenches, storage and training/inference capacity | funding, operators, software, data location and access | class-level cloud/HPC does not establish tenancy, isolation or capacity |
| AI/software | foundation, predictive, generative/design and assistant models; code, libraries, packages and dependencies | training data, versions/configuration, compute, developers and evaluation | source names packages/APIs but not containers or a complete SBOM |
| Interface/application | proprietary/open model access, APIs, analysis/design tools, surveillance/decision applications | identity, purpose, model/output state and human reviewer | API can obscure safeguards; application authority is context-specific |
| Laboratory/physical action | instruments, automation agents, foundries/cloud labs, order/fulfillment and experimental build/test | selected output, human gate, materials, safety/quality and physical capability | model output is not permission, material or validated result |
| Decision/response | researchers, clinical/public-health users, agencies and other accountable decision makers | evidence quality, intended use, uncertainty and governance | advisory or analytical output is not a guaranteed outcome |

## Trust and responsibility boundaries

- data contributor/subject or laboratory ↔ repository/data steward;
- repository ↔ training/analysis environment;
- public/open-source dependency ↔ model/application maintainer;
- proprietary model/API provider ↔ research end user;
- credentialed user/institution ↔ sandbox/workbench;
- model output ↔ accountable human/experimental gate;
- digital design/order ↔ screening/provider/physical fulfillment;
- model/automation agent ↔ instrument or laboratory process;
- experiment/result ↔ curated feedback and future training state;
- federal funder/advisory body ↔ implementing organization.

> **Claim record — SYS-0011-C02 | analytic-judgment**
> **Claim:** The ecosystem depends on the asset classes in `AST-0008` and
> contains explicit data→model, model→application, application→physical-action
> and experiment→data feedback boundaries.
> **Claim status:** active
> **Scope:** Reconciled source-supported dependency graph; not a deployed
> topology, trust decision, authorization map or causal incident path.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Figure 2-1, printed p. 20 (physical p. 41); Chapter 5 Figures 5-1–5-2,
> printed pp. 70 and 73 (physical pp. 91 and 94); Appendix A Figure A-1,
> printed p. 89 (physical p. 110).
> **Basis / limits:** Layers and arrows are direct or visually verified. Their
> canonical boundary labels are wiki analysis; no interface assurance or
> organizational responsibility test is reported.

## Supply-chain and architecture completeness

NASEM directly discusses open-source software dependencies, packages,
proprietary APIs, public/federal/private databases, cloud/HPC, instruments and
automated-laboratory concepts. Figure 5-1 visually names electronic laboratory
notebooks and version control. However, the source does not provide a literal
container map, model registry, complete API inventory, identity hierarchy,
package/version graph or one joined data/model/software/experiment lineage.

> **Claim record — SYS-0011-C03 | analytic-judgment**
> **Claim:** `SYS-0011` is a direct but incomplete biological-AI system and
> supply-chain map: packages, notebooks, cloud/HPC, APIs, databases,
> instruments and identity/access cases are present, while containers and
> model registries remain absent and no deployment is validated.
> **Claim status:** active
> **Scope:** Literal class-coverage audit of the represented source; not a
> claim that every organization lacks those components.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 4, printed pp. 52–53 (physical pp. 73–74); Chapter 5, printed pp.
> 66–77 (physical pp. 87–98), including Figures 5-1–5-2 and Box 5-2; Appendix
> A tables and discussion, printed pp. 89–124 (physical pp. 110–145).
> **Basis / limits:** Present classes are direct; absent literal classes were
> searched across the full artifact. A workbench is not called a notebook
> unless the figure says so, and a database is not normalized to a model
> registry.

## Failure and uncertainty boundaries

- Data quality or provenance failure can propagate into models and later
  experimental/decision outputs.
- A compromised dependency can affect model/application behavior without
  changing the biological input itself.
- A proprietary API boundary can hide implementation and security features.
- Automation can amplify an erroneous or unauthorized decision, but a
  conceptual automation agent is not an observed autonomous deployment.
- Physical build/test remains a separate bottleneck and possible detection
  opportunity, not a guaranteed safeguard.
- Repositories, compute access and partnership recommendations are not proof
  of capacity, availability, adoption or resilience.

> **Claim record — SYS-0011-C04 | analytic-judgment**
> **Claim:** System-class and boundary evidence supports threat and control
> mapping but does not establish implementation, configuration, availability,
> compromise, recovery or effectiveness for a named biological-AI system.
> **Claim status:** active
> **Scope:** Evidence-state boundary for `SYS-0011`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> exact locators above.
> **Basis / limits:** The report is a capability/risk/control synthesis and
> advisory study, not an architecture assessment or incident/deployment audit.

> **Claim record — SYS-0011-C05 | source-report**
> **Claim:** ProteinGym reports a research benchmark ecosystem connecting DMS/
> clinical datasets, preprocessing, model-specific scoring through a common
> code interface, alignments/structures/scores, repository/server resources
> and a comparison website.
> **Claim status:** active
> **Scope:** Reported research-resource classes and interfaces; not a validated
> runtime topology, deployed API/identity boundary, container inventory or
> model registry.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> Figure 1, p. 3; §§4 and 6, pp. 6–10; Appendix §§A.3.3–A.4,
> pp. 32–34; `SRC-0034-C04/C07`.
> **Basis / limits:** Classes and reported interfaces are direct. Only the
> paper and proceedings record were retained; no external resource or
> configuration was run or validated.

## Related pages

- [SYN-0029 — AIB residual reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SYN-0023 — Engineering-biology transfer reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)

- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [RSK-0016 — AI output to unsafe action](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0016 — Biological AI controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [SYS-0003 — Sequencing/bioinformatics ecosystem](sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [SYS-0006 — Screening systems](sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SYN-0018 — Biological-AI SF2 reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SRC-0034 — ProteinGym benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact
  locators above.
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md), exact
  locators above.
