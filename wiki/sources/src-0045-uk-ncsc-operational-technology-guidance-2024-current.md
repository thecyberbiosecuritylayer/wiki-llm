---
id: SRC-0045
type: source
title: UK NCSC operational-technology architecture and secure-connectivity guidance, current collection
aliases:
  - NCSC Operational Technology collection
  - NCSC definitive OT architecture view
  - NCSC secure connectivity principles for OT
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-uk-multinational-partner-ot-cybersecurity-guidance-package
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/uk-ncsc-operational-technology-collection-current-2026-07-12.html
raw_bytes: 151736
sha256: 0a76dae5345e95a01a605132de7613ea6ed04b2f439adcf3be855c16dd2b75c4
raw_components:
  - path: ../../raw/uk-ncsc-definitive-view-ot-architecture-2025.pdf
    role: complete-definitive-ot-architecture-guidance
    bytes: 1007995
    sha256: e1468ff9b3270ae2fcd5bd72f1d597c2c88dd14a2cf6e964ffecd4952aeca684
  - path: ../../raw/uk-ncsc-secure-connectivity-operational-technology-2026.pdf
    role: complete-secure-ot-connectivity-guidance
    bytes: 926576
    sha256: a4754462e9dc19f57d7f617b0d0dc60465b2ea05614fe76eb706efa1e7f413ae
canonical_url: https://www.ncsc.gov.uk/collection/operational-technology
definitive_view_url: https://www.ncsc.gov.uk/collection/operational-technology/definitive-architecture-view
definitive_view_pdf_url: https://www.ncsc.gov.uk/files/ncsc-creating-and-maintaining-a-definitive-view-of-your-operational-technology-architecture.pdf
secure_connectivity_url: https://www.ncsc.gov.uk/collection/operational-technology/secure-connectivity
secure_connectivity_pdf_url: https://www.ncsc.gov.uk/sites/default/files/documents/ncsc-secure-connectivity-for-operational-technology.pdf
accessed: 2026-07-12
collection_published: 2024-03-18
collection_reviewed: 2024-03-18
collection_version: "1.0"
issuer: United Kingdom National Cyber Security Centre
partner_agencies:
  - Australian Signals Directorate Australian Cyber Security Centre
  - Canadian Centre for Cyber Security
  - United States Cybersecurity and Infrastructure Security Agency
  - United States Federal Bureau of Investigation
  - Germany Federal Office for Information Security
  - Netherlands National Cyber Security Centre
  - New Zealand National Cyber Security Centre
jurisdictions:
  - United Kingdom
tags:
  - biomanufacturing
  - operational-technology
  - ics
  - scada
  - architecture
  - connectivity
  - vulnerability
  - insider-risk
  - supply-chain
  - regulatory-guidance
---

# UK NCSC operational-technology architecture and secure-connectivity guidance, current collection

## Identity, acquisition and complete review

The retained package contains the complete 151,736-byte NCSC OT collection
page, the complete 32-page 2025 definitive-architecture PDF and the complete
33-page 2026 secure-connectivity PDF. The three declared objects total
2,086,307 bytes and match the frontmatter hashes. All 65 PDF pages and the
collection's identity, navigation, OT definition, role and metadata were
reviewed.

Both PDFs are tagged, unencrypted and unsigned, with no form, JavaScript or
embedded-file component detected. Text extraction was coherent. `qpdf` was
unavailable, and the signature tool's local NSS trust database did not
initialize before it reported that neither PDF contains signatures.

Repeat retrievals of the collection and both linked official PDFs on
2026-07-12 were byte-identical. The collection is still a discovery/current-
presentation wrapper: it and the two PDFs form one NCSC OT publication
programme, not three independent lineages.

> **Claim record — SRC-0045-C01 | artifact-observation**
> **Claim:** The retained 2,086,307-byte package contains three hash-verified
> official NCSC objects with complete 65-page PDF review, reproducible repeat
> bytes and explicit same-programme counting limits.
> **Claim status:** active
> **Scope:** Declared artifacts only; not cryptographic authentication, runtime
> assurance, structural validation by unavailable `qpdf` or independent-source
> multiplication.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths, bytes and hashes; full HTML/PDF review;
> official repeat retrieval hashes; PDF metadata/component inspection.
> **Basis / limits:** Artifact identity is reproducible. Editorial programme
> relationships remain distinct from independent factual corroboration.

## Current presentation, authorship and force

The live collection presents OT as physical-world-interface technology and
includes ICS, SCADA and DCS. Both PDFs identify the UK NCSC as producer with
contributions from Australian, Canadian, U.S., German, Dutch and New Zealand
partner agencies. The definitive-view PDF is copyrighted 2025 and the secure-
connectivity PDF 2026. Each says its principles are goals rather than minimum
requirements.

> **Claim record — SRC-0045-C02 | source-report**
> **Claim:** The current NCSC collection directly includes 2025 definitive-
> architecture and 2026 secure-connectivity guidance produced by UK NCSC with
> the same named multinational partner-agency group.
> **Claim status:** active
> **Scope:** Publication/current-presentation and contribution roles; not eight
> national adoptions, regulations, independent sources or legal instruments.
> **As of:** Official collection retained 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Collection page title/navigation/metadata; definitive PDF
> pp. 1-2 and copyright p. 32; secure-connectivity PDF pp. 1-2 and copyright
> p. 33.
> **Basis / limits:** Dates and contributors are direct; co-authorship is not
> jurisdiction-by-jurisdiction legal adoption.

> **Claim record — SRC-0045-C03 | analytic-judgment**
> **Claim:** The two NCSC instruments are nonbinding principles-based cyber
> guidance whose stated goals require organization-specific risk decisions;
> imperative wording is not converted into GMP law or minimum compliance.
> **Claim status:** active
> **Scope:** Instrument force and interpretation; not legal advice or a claim
> that no sector regulator can separately require similar controls.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Definitive-view PDF p. 4, `Principles-based guidance`;
> secure-connectivity PDF p. 4, same section; collection classification as
> `Guidance`.
> **Basis / limits:** Both guides explicitly call the principles goals rather
> than minimum requirements.

## OT architecture, information and boundaries

The definitive-view guide represents field devices, sensors, actuators,
networking, gateways, computer platforms, digital services and software. It
separates internal from external connections and explicitly includes
enterprise systems, vendors, third parties and cloud services. It recommends
asset/configuration records, passive discovery and validated change control.

> **Claim record — SRC-0045-C04 | source-report**
> **Claim:** NCSC supplies a generic OT architecture model spanning digital
> sensors/actuators, PLC/RTU configuration, SCADA, software/services,
> enterprise/vendor/cloud connections, protocols, data flows and system trust
> boundaries.
> **Claim status:** active
> **Scope:** Generic greenfield/brownfield OT model; not a biomanufacturing-
> specific deployment, complete MES/LIMS/QMS/ERP stack or verified inventory.
> **As of:** Definitive-view guidance 2025.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Definitive-view PDF pp. 3-7, 10-11 and 18-22.
> **Basis / limits:** Classes and boundaries are direct; actual facility
> presence and sector mapping require separate evidence.

## Threats, process effects and concrete exposures

The guides distinguish disruptive, destructive, espionage and physical-
effect aims. They connect compromised information or connectivity to altered
setpoints/commands, incorrect PLC action, process interruption, lower yield,
safety harm, environmental impact and service disruption. These are generic
threat/risk paths, not observed biomanufacturing incidents.

> **Claim record — SRC-0045-C05 | source-report**
> **Claim:** NCSC explicitly models cyber manipulation and outage paths from
> architecture/credential/protocol or connectivity compromise to unauthorized
> control behavior, disrupted process, reduced yield and possible physical,
> safety or environmental effect.
> **Claim status:** active
> **Scope:** Generic OT risk mechanisms; not occurrence, causal probability,
> product-quality finding or a specific biomanufacturing consequence.
> **As of:** 2025-2026 guidance package.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Definitive-view PDF pp. 12-18 and 21-27; secure-connectivity
> PDF pp. 3 and 5-8.
> **Basis / limits:** Paths and possible impacts are direct recommendations/
> threat-model content; no incident or control result is represented.

> **Claim record — SRC-0045-C06 | source-report**
> **Claim:** Concrete exposure and vulnerability classes include obsolete or
> unsupported products, missing updates/authentication, internet/remote and
> wireless exposure, insecure legacy protocols, default credentials,
> excessive privilege, removable media and flat-network lateral movement.
> **Claim status:** active
> **Scope:** Vulnerability classes and examples; not a product CVE inventory,
> exploit instructions, prevalence estimate or finding at a named facility.
> **As of:** 2025-2026 guidance package.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Definitive-view PDF pp. 7, 12, 16-18, 22 and 27-31;
> secure-connectivity PDF pp. 5-6, 10-14 and 17-23.
> **Basis / limits:** Classes are direct. This local page omits actionable
> configuration and exploitation detail.

> **Claim record — SRC-0045-C07 | source-report**
> **Claim:** The package directly covers insider and supply-chain/third-party
> risks through privileged access, vendors/integrators/MSPs, remote support,
> supplier components/updates, contractor footholds and out-of-band access.
> **Claim status:** active
> **Scope:** Threat-actor/dependency classes; not allegation against a vendor,
> observed insider event, compromise attribution or sector frequency.
> **As of:** 2025-2026 guidance package.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Definitive-view PDF pp. 23-24 and 27-31;
> secure-connectivity PDF pp. 3, 9, 15-16 and 22-23.
> **Basis / limits:** Insider and supply predicates are literal and remain
> bounded from occurrence or culpability.

## Controls, exceptions and adoption boundary

The guides recommend inventory/change control, segmentation, authenticated
protocols, centralized access, monitoring, isolation and recovery planning.
They also preserve operational constraints: insecure protocols may need
documented compensating controls in time-critical safety uses; obsolete
equipment may require temporary containment; critical data flows may need
bounded isolation exceptions. Recommendation and test language is not a
reported deployment or outcome.

> **Claim record — SRC-0045-C08 | source-report**
> **Claim:** NCSC pairs architecture, access, integrity-monitoring,
> segmentation and isolation controls with documented operational exceptions,
> compensating controls and safety/availability tradeoffs.
> **Claim status:** active
> **Scope:** Recommended design and exception logic; not deployed safeguards,
> successful tests, risk elimination, regulatory compliance or effectiveness.
> **As of:** 2025-2026 guidance package.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Definitive-view PDF pp. 20-30; secure-connectivity PDF
> pp. 5-8, 17-22, 24-32.
> **Basis / limits:** Controls and constraints are direct; implementation,
> comparator and evaluator are absent.

> **Claim record — SRC-0045-C09 | analytic-judgment**
> **Claim:** Current official presentation establishes availability and
> intended audience, but the package provides no organization-level adoption
> census, regulatory mandate, implementation audit or evaluated outcome; its
> two PDFs count as one NCSC/multinational-partner technical lineage.
> **Claim status:** active
> **Scope:** Adoption/evidence and source-count boundaries; not a claim that
> no organization uses the guidance.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0045-C01`-`C08`; full collection/PDF review; shared
> producer, contributors and programme framing.
> **Basis / limits:** Publication is observable; uptake and effectiveness are
> not measured. Companion documents are not independent corroborators.

## Criterion and non-promotion boundary

> **Claim record — SRC-0045-C10 | analytic-judgment**
> **Claim:** Reconciled with existing biomanufacturing process/quality
> sources, `SRC-0045` can fill insider, supply-chain and concrete-exposure
> predicates for `BMO-TV` and the OT-cyber instrument role for `BMO-GR`, but
> cannot pass `BMO-SD` or `BMO-AE` by itself.
> **Claim status:** superseded
> **Scope:** Candidate SF2 contributions and frozen-cell non-promotion; not
> source-level score arithmetic, a BMO incident or external absence claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0045-C03`-`C09`; frozen BMO rows in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Generic OT guidance needs an explicit sector stitch;
> QMS-as-software/ERP coverage and SF3 result/comparator/evaluator evidence
> remain absent.
> **Superseded by:** `SYN-0028-C04/C06/C07`, after strict sector/governance
> reconciliation and adjacent-cell audit.

## Safety abstraction

Only high-level defensive architecture, threat and dependency classes are
retained. The page exposes no named operator, live asset, endpoint, address,
credential, exploitable version, command syntax, setpoint or facility-specific
route, and it does not reproduce implementation-ready attack steps.

> **Claim record — SRC-0045-C11 | analytic-judgment**
> **Claim:** The local NCSC representation is defensive and non-operational:
> it omits live targets, credentials, exploitable versions, commands,
> setpoints, facility routes and implementation-ready attack instructions.
> **Claim status:** active
> **Scope:** Local wiki page; not a safety assessment of the complete public
> guidance or all cited external resources.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and bounded threat descriptions in
> `SRC-0045-C04`-`C10`.
> **Basis / limits:** Only high-level threat predicates needed for defensive
> reasoning are represented.

## Integration map

- [GOV-0023](../governance/gov-0023-uk-ncsc-operational-technology-governance.md)
- [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md)
- [VUL-0003](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [SYN-0028](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)

## Official links

- <https://www.ncsc.gov.uk/collection/operational-technology>
- <https://www.ncsc.gov.uk/collection/operational-technology/definitive-architecture-view>
- <https://www.ncsc.gov.uk/files/ncsc-creating-and-maintaining-a-definitive-view-of-your-operational-technology-architecture.pdf>
- <https://www.ncsc.gov.uk/collection/operational-technology/secure-connectivity>
- <https://www.ncsc.gov.uk/sites/default/files/documents/ncsc-secure-connectivity-for-operational-technology.pdf>
