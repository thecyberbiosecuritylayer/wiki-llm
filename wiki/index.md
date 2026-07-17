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
rg -l '^type: source$' wiki/sources
```

## Core domain maps

- [CON-0001 — Cyberbiosecurity](concepts/con-0001-cyberbiosecurity.md) — the
  domain boundary and distinctions from biosafety, biosecurity, and
  cybersecurity.
- [SYN-0034 — What Is Cyberbiosecurity?](syntheses/syn-0034-what-is-cyberbiosecurity-public-explainer.md) —
  an accessible explanation through dependencies, causal transitions,
  documented examples, and evidentiary limits.
- [SYN-0003](syntheses/syn-0003-cross-domain-transfer-directions.md) —
  cyber-to-biological, biological-to-digital, and adjacent pathway classes.
- [SYN-0032](syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)
  — a broad engineering-biology lifecycle synthesis of threats, screening,
  and governance.
- [SYN-0029](syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
  — biological-AI risks, benchmarks, controls, and governance limits.
- [SYN-0031](syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)
  — laboratory reverse-transfer paths, incident evidence, and the limits of
  causal conclusions.
- [SYN-0001 — Coverage rubric](syntheses/syn-0001-coverage-rubric.md) — a
  historical coverage-assessment tool, not evidence of completeness or
  certification.

## Representative risk scenarios

- [RSK-0001](risk-scenarios/rsk-0001-hcl-containment-control-disruption.md) —
  disruption of digitally supported containment functions in a high-
  containment laboratory.
- [RSK-0006](risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
  — disruption of transfusion testing and resulting supply pressure.
- [RSK-0009](risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md) —
  biological input to digital execution.
- [RSK-0021](risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
  — biological test input to digital result and public-health action.

## Representative incidents and controls

- [INC-0001](incidents/inc-0001-synnovis-transfusion-disruption-2024.md) — the
  Synnovis transfusion disruption.
- [INC-0005](incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
  — an anonymous chicken-farm report and an example of weak nested evidence
  lineage.
- [INC-0008](incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md) —
  Immensa false-negative reporting as an observed, non-malicious reverse path.
- [CTL-0016](controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
  — biological-AI provenance and decision gates.
- [CTL-0021](controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
  — secure, monitored biological-AI lifecycle controls.

## Governance starting points

- [SYN-0002](syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md) — a
  comparison of US and UK nucleic-acid screening frameworks.
- [GOV-0025](governance/gov-0025-eu-ai-act-life-sciences-applicability.md) — EU
  AI Act applicability to life sciences, medical devices, and IVD AI.

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

## Supporting pages

- [Glossary](glossary.md) — terminology and disambiguation.
- [ID registry](id-registry.md) — issued, active, and retired page IDs.
- [Public changelog](../CHANGELOG.md) — publication history; not factual evidence.
- `_templates/` — simple templates for new pages.

## Minimal workflow

```text
raw source
→ one SRC page
→ updates to existing topic/risk pages
→ review evidence, relative links, and the Markdown diff
→ Git commit
```

No generated publication layer or maintenance runtime is required to read the
repository.
