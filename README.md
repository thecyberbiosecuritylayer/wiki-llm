# Cyberbiosecurity Wiki

[![Repository check](https://github.com/thecyberbiosecuritylayer/wiki-llm/actions/workflows/check.yml/badge.svg)](https://github.com/thecyberbiosecuritylayer/wiki-llm/actions/workflows/check.yml)

**When software, data, or digital controls alter what happens to samples,
products, patients, or biological processes, the risk is no longer purely
cyber.**

Cyberbiosecurity analyzes and manages those cross-domain dependencies. This
public, evidence-traceable wiki maps the path from source to claim, from a
digital or biological state change to its consequence, and from that
consequence to the controls intended to prevent, detect, contain, or help
recover from it.

[Read the public explainer](wiki/syntheses/syn-0034-what-is-cyberbiosecurity-public-explainer.md)
· [Explore the wiki](wiki/index.md)
· [See a documented incident](wiki/incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
· [Contribute](CONTRIBUTING.md)

## Why this matters

NHS England classifies the 3 June 2024 attack on laboratory-services provider
Synnovis as ransomware and reports that it significantly reduced
test-processing capacity
([SRC-0009](wiki/sources/src-0009-nhs-england-synnovis-update-2025.md), update
paragraph 2). NHS Blood and Transplant separately reports that the event
disrupted access to systems supporting blood grouping, antibody screening, and
crossmatching. Affected hospitals relied more heavily on O-negative components;
NHSBT says the resulting pressure on limited stocks contributed to an amber
stock alert
([SRC-0008](wiki/sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–22
and 97).

```text
attack classified as ransomware
  → reduced laboratory-system availability
  → greater reliance on O-negative components
  → pressure on a limited biological stock
```

The available evidence does **not** establish that the stock was exhausted or
that the incident caused a specific patient injury. That combination of a
traceable cross-domain path and an explicit evidence boundary is what this
wiki is built to preserve. Read the
[full public explanation](wiki/syntheses/syn-0034-what-is-cyberbiosecurity-public-explainer.md)
for more examples in both directions.

## Choose your path

| If you want to… | Start here |
| --- | --- |
| Understand cyberbiosecurity without prior specialist knowledge | [What Is Cyberbiosecurity?](wiki/syntheses/syn-0034-what-is-cyberbiosecurity-public-explainer.md) |
| See what makes this field distinct from cybersecurity, biosecurity, and biosafety | [Cyberbiosecurity domain boundary](wiki/concepts/con-0001-cyberbiosecurity.md) |
| Follow cyber-to-biological and biological-to-digital transfer paths | [Cross-domain transfer directions](wiki/syntheses/syn-0003-cross-domain-transfer-directions.md) |
| Examine a documented real-world event and its evidentiary limits | [Synnovis transfusion-service disruption](wiki/incidents/inc-0001-synnovis-transfusion-disruption-2024.md) |
| Explore biological AI risks, controls, benchmarks, and governance | [Biological-AI lifecycle synthesis](wiki/syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md) |
| Compare nucleic-acid screening governance | [US–UK screening comparison](wiki/syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md) |

The thematic routes, complete page-type directory map, search examples, and
current knowledge cutoff are in [`wiki/index.md`](wiki/index.md).

## How the wiki reasons

A topic belongs here only if it answers three questions:

1. What biological asset, workflow, system, stakeholder, or consequence is at
   stake?
2. What digital dependency, data flow, threat, weakness, or control connects to
   it?
3. Why does that connection matter for security, privacy, safety, quality,
   resilience, or governance?

```text
intentional threat → technique ----------------------+
                                                       |
non-adversarial hazard → failure or trigger ----------+
                                                       ↓
interaction with a vulnerability, exposure, or failed trust boundary
  → origin domain and first affected asset
  → first digital, biological, or physical state change
  → transfer through data, control, custody, decision, or material
  → receiving-domain state change
  → immediate and downstream consequences
  → controls mapped to the exact edge they address
```

Every decision-relevant claim has a stable page-local ID and identifies its
evidence and limits. The normal evidence route is:

```text
primary source or retained artifact
  → SRC provenance note with a precise locator
  → claim with scope, evidence, and limits
  → reusable concept, risk, control, incident, governance, or synthesis page
```

Topic pages are not treated as evidence for other topic pages. Current laws,
standards, product capabilities, and institutional positions can change, so
readers should check each claim's jurisdiction, version, `As of`,
`Review after`, and limits before relying on it as current.

The goal is not to make uncertainty disappear. It is to make the evidence,
reasoning, and boundary of uncertainty inspectable.

## Key repository layers

- [`wiki/sources/`](wiki/sources/) records provenance, precise locators,
  coverage, and source limitations.
- [`wiki/risk-scenarios/`](wiki/risk-scenarios/) models plausible end-to-end
  paths; [`wiki/incidents/`](wiki/incidents/) is reserved for documented real
  events.
- [`wiki/controls/`](wiki/controls/) maps safeguards to exact scenario edges;
  [`wiki/governance/`](wiki/governance/) records jurisdiction- and
  version-bounded rules and guidance.
- [`wiki/syntheses/`](wiki/syntheses/) reconciles evidence across sources.

The [`index`](wiki/index.md) provides the complete directory map and knowledge
cutoff; the [`ID registry`](wiki/id-registry.md) and
[`glossary`](wiki/glossary.md) preserve stable identities and terminology.

Everything is ordinary Markdown. The same readable files form the durable
knowledge layer for people and LLM-assisted maintenance and querying; no
generated publication layer or maintenance runtime is required to read it.

## Scope, safety, and evidence boundaries

The corpus is global, comparative, defensive, and public-source. It covers
laboratories, genomics and other omics, biobanks, nucleic-acid synthesis,
engineering biology, connected instruments, biomanufacturing, agriculture,
biological AI, research infrastructure, and their supply chains—only where a
digital-biological dependency is actually demonstrated.

The wiki separates documented incidents from hypothetical risk scenarios and
labels claims as artifact observations, source reports, analytic judgments, or
hypotheses; unknowns remain explicit. It does not turn possibility into fact,
correlation into causation, or one jurisdiction's rule into a universal
conclusion.

The public corpus does not include harmful biological sequences, deployable
exploit code, credentials, facility-access details, or operational bypass
instructions.

## Sources and reproducibility

The canonical local `raw/` archive is immutable, while the public Git history
contains no binary raw artifacts. Exact files approved for redistribution are
published separately in the immutable
[public evidence release](https://github.com/thecyberbiosecuritylayer/wiki-llm/releases/tag/evidence-2026-07-16).
Its nine reviewed artifacts are accompanied by rights metadata and SHA-256
manifests. See [`RAW_SOURCES.md`](RAW_SOURCES.md),
[`RAW_ARTIFACTS.sha256`](RAW_ARTIFACTS.sha256), and
[`raw/README.md`](raw/README.md).

A missing raw file does not change which source a claim identifies, but a
public clone alone cannot provide byte-level verification of that file. The
corresponding `SRC` note retains its canonical URL, DOI or publication
identifier, local binding, coverage, and precise locators.

## Contribute, reuse, and cite

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before
opening an issue or pull request. Use [`SECURITY.md`](SECURITY.md), rather
than a public issue, for privacy, re-identification, sensitive-capability, or
security reports. Project authority is recorded in
[`MAINTAINERS.md`](MAINTAINERS.md), and [`RELEASES.md`](RELEASES.md)
distinguishes versioned knowledge snapshots from immutable evidence bundles.

Original wiki content and project documentation are available under
[CC BY 4.0](LICENSE), subject to the exclusions in [`RIGHTS.md`](RIGHTS.md).
Project-authored validation and workflow code are separately licensed under
the [MIT License](tools/LICENSE). Third-party source artifacts retain their
own terms. Citation metadata is available in [`CITATION.cff`](CITATION.cff).
For a reproducible citation, use a versioned knowledge release when one is
available; otherwise cite the exact Git commit and access date. Evidence
bundles are not versions of the wiki.

Before submitting a change, run:

```sh
python3 tools/check.py
```

The checker has no third-party dependencies. Its validation scope is
documented in [`tools/README.md`](tools/README.md).
