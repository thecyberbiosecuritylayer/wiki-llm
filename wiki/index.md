# Cyberbiosecurity Wiki

> Primary language: English
> Scope: global, comparative, defensive, and public-source
> Knowledge cutoff: 2026-07-13

This evidence-based Markdown wiki examines risks at the boundary between
digital and biological systems. It helps readers trace a path from source to
claim, from a digital or biological state change to its consequence, and from
that consequence to relevant controls and remaining uncertainty.

The wiki is not automatically complete or current after the knowledge cutoff.
Topic and synthesis pages are not evidence in themselves: material findings
should be checked against the relevant `SRC` pages and, where necessary, the
immutable artifacts in the local `raw/` archive or, when specifically
allowlisted, the separate public evidence release.

## How to search

1. Define the subject, environment, jurisdiction, and date of interest.
2. Search for a title, alias, page ID, or keyword with GitHub code search or
   `rg` in a local clone.
3. Open the most relevant topic, incident, governance, control, or risk-scenario
   page.
4. Check its decision-relevant claims, limits, and cited `SRC` pages.
5. Do not use an overdue or superseded claim as a current finding without
   reverification.

Examples for a local clone:

```sh
rg -n -i "synnovis|transfusion" wiki
rg -n "RSK-0009|biological-to-digital" wiki
rg -l '^type: governance$' wiki/governance
rg -l '^type: incident$' wiki/incidents
rg -l '^type: source$' wiki/sources
```

## Start here

- [CON-0001 — Cyberbiosecurity](concepts/con-0001-cyberbiosecurity.md) defines
  the domain and its boundary with cybersecurity, biosecurity, and biosafety.
- [SYN-0034 — What Is Cyberbiosecurity?](syntheses/syn-0034-what-is-cyberbiosecurity-public-explainer.md)
  is the accessible public introduction.
- [SYN-0003 — Cyber-biological transfer directions and mechanisms](syntheses/syn-0003-cross-domain-transfer-directions.md)
  maps cyber-to-biological, biological-to-digital, and adjacent pathways.

## Explore by domain

Use the primary entry as a route into the domain, follow the useful synthesis,
workflow, risk, control, or incident branches, and combine the search patterns
to discover the current corpus without treating this guide as a complete
catalog.

| Route | Primary entry | Useful branches | Suggested `rg` pattern fragments |
| --- | --- | --- | --- |
| Laboratories and biobanks | [SYN-0031 — Laboratory threat breadth and reverse-transfer incident reconciliation](syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md) | [SYN-0010 — Laboratory and biobank scope, asset and lifecycle reconciliation](syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md); [WFL-0010 — Clinical laboratory testing, reporting and correction lifecycle](workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md) | `high[- ]containment`, `clinical laborator`, `public[- ]health laborator`, `biobank`, `biospecimen`, `LIMS`, `transfusion` |
| Genomics and human omics | [SYN-0021 — Genomic assets, lifecycle and system-boundary reconciliation](syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md) | [WFL-0005 — Genomic data lifecycle](workflows/wfl-0005-genomic-data-lifecycle.md); [RSK-0004 — Disclosure of human genomic data and kin privacy harm](risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md) | `genomic[- ]data`, `human[- ]omics`, `sequenc`, `kin[- ]privacy`, `23andMe` |
| Biomanufacturing and OT | [SYN-0028 — Biomanufacturing scope, threat, incident and governance reconciliation](syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md) | [WFL-0003 — Biopharmaceutical manufacturing information and control flows](workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md); [INC-0006 — Merck NotPetya manufacturing and supply disruption, 2017](incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md) | `biomanufactur`, `biopharmaceutical`, `process[- ]control`, `digital[- ]thread`, `GxP`, `CGMP`, `operational[- ]technology`, `Merck` |
| Agriculture and One Health | [SYN-0025 — Agriculture lifecycle, system, threat, transfer, consequence and control reconciliation](syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md) | [SYN-0009 — Global and US One Health agriculture/environment scope reconciliation](syntheses/syn-0009-global-us-one-health-scope-reconciliation.md); [WFL-0012 — Animal and plant health surveillance, movement and response lifecycle](workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md) | `agricultur`, `One[- ]Health`, `smart[- ]farm`, `animal[- ]health`, `plant[- ]health`, `IMSOC`, `food[- ]supply`, `veterinar` |
| Engineering biology and synthesis screening | [SYN-0032 — Engineering-biology lifecycle, threat, screening and governance reconciliation](syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md) | [WFL-0014 — Engineering-biology design-to-disposition lifecycle](workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md); [CTL-0024 — NIST-benchmarked nucleic-acid screening assurance](controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md) | `engineering[- ]biology`, `synthetic[- ]nucleic[- ]acid`, `synthesis[- ]screening`, `procurement[- ]screening`, `sequence[- ]screening`, `DBTL`, `benchtop` |
| Biological AI | [SYN-0029 — Biological-AI lifecycle, threat, benchmark and governance reconciliation](syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md) | [WFL-0013 — Secure biological-AI model lifecycle from intake to retirement](workflows/wfl-0013-biological-ai-secure-model-lifecycle.md); [RSK-0016 — Biological-AI output to unsafe experimental or decision action](risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md) | `biological[- ]AI`, `AI[- ]enabled`, `MLOps`, `model[- ]lifecycle`, `decision[- ]gate`, `protein[- ]model` |
| Governance and jurisdiction | [SYN-0008 — Global, US, EU, UK and Canada governance modality and actor reconciliation](syntheses/syn-0008-global-us-eu-uk-canada-governance-reconciliation.md) | [SYN-0004 — US–EU human-omics and electronic-health-data governance reconciliation](syntheses/syn-0004-us-eu-human-omics-health-data-governance.md); [SYN-0002 — US–UK synthetic nucleic-acid procurement screening comparison](syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md) | `jurisdiction`, `issuer`, `document_type`, `instrument_status`, `binding_status`, `effective_date` |
| Documented incidents | [INC-0001 — Synnovis cyberattack and transfusion-service disruption](incidents/inc-0001-synnovis-transfusion-disruption-2024.md) | [INC-0008 — Immensa PCR incorrect-negative reporting incident, 2021](incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md); [INC-0007 — 23andMe credential-stuffing and linked genetic-profile breach, 2023](incidents/inc-0007-23andme-genetic-data-breach-2023.md) | `ransomware`, `credential[- ]stuffing`, `incorrect[- ]negative`, `disruption`, `confirmed[- ]impact`, `reported[- ]vector`, `attribution` |

Fragments ending mid-word, such as `sequenc`, intentionally match inflections;
`[- ]` matches either a hyphen or a space. Combine a row's fragments with `|` in
an `rg -n -i 'PATTERN' wiki` search. For a complete list of governance or
incident pages, use the type-specific `rg -l` commands above. Search patterns
aid discovery but do not establish corpus completeness.

These routes are navigation, not evidence. Resolve material claims through the
cited `SRC` pages and their source locators.

Current laws, standards, guidance, product capabilities, and institutional
statuses are time-sensitive. Always check the `As of`, `Review after`,
jurisdiction, and version recorded for the specific claim.

## Page directories

The corpus is organized by page type. Use file search for a complete list
rather than maintaining a second manual catalog in this index:

```text
sources/         provenance and source claims
concepts/        definitions and foundational models
assets/          biological, digital, physical, and human assets
systems/         instruments, platforms, and services
workflows/       processes, data flows, and trust boundaries
threats/         intentional actors and malicious events
hazards/         accidental and non-adversarial conditions
techniques/      mechanisms and adversarial methods
vulnerabilities/ weaknesses, exposures, and unsafe assumptions
risk-scenarios/  end-to-end cross-domain consequence paths
controls/        preventive, detective, response, and recovery measures
incidents/       documented real-world events
organizations/   institutions and programs
governance/      laws, regulations, standards, and guidance
syntheses/       cross-source comparisons and durable analyses
questions/       open evidence gaps
```

The `organizations/` directory is created when the first reusable `ORG` page is
activated; an absent directory does not remove that reserved page type.

## Supporting pages

- [Glossary](glossary.md) — terminology and disambiguation.
- [ID registry](id-registry.md) — issued, active, and retired page IDs.
- [SYN-0001 — Coverage rubric](syntheses/syn-0001-coverage-rubric.md) — a
  historical coverage-assessment tool, not evidence of completeness or
  certification.
- [Public changelog](../CHANGELOG.md) — publication history; not factual evidence.
- [Maintainer authority](../MAINTAINERS.md) and
  [release policy](../RELEASES.md) — project procedure; not factual evidence.
- [`_templates/`](_templates/) — simple templates for new pages.

Many synthesis pages ending in `reconciliation` are structured evidence-
integration checkpoints. They expose scope, conflicts, and unresolved gaps;
they are not certifications or interchangeable public introductions.

## Minimal workflow

```text
source URL or explicitly approved local artifact
→ one SRC page
→ updates to existing topic/risk pages
→ review evidence, relative links, and the Markdown diff
→ Git commit
```

No generated publication layer or maintenance runtime is required to read the
repository.
