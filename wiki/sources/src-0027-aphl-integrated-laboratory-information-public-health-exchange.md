---
id: SRC-0027
type: source
title: APHL integrated laboratory information and centralized public-health data exchange package
aliases:
  - APHL LIS Integration Guide and AIMS toolkit
  - APHL clinical-public-health informatics package
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-technical-guidance-and-issuer-implementation-package
ingest_status: complete-package
sensitivity: public
dual_use: low
raw_path: ../../raw/aphl-laboratory-data-integrated-lis-implementation-guidance-2024.pdf
sha256: f6df76580f8ae3de199c49fd62b1a8b72317db79ab2f260b72e0e1bd830fee46
raw_components:
  - path: ../../raw/aphl-aims-centralized-public-health-data-exchanges-2025.pdf
    role: current-centralized-public-health-exchange-toolkit
    sha256: 07c44899020fdc953b3593c1d9d432cdaaf995a7a4dfa1912abe2bf20cf0566e
  - path: ../../raw/aphl-creating-modern-laboratory-systems-uganda-2026.html
    role: issuer-reported-implementation-companion
    sha256: 031506a652cbb05892aae17149290a6b5e4d41ed5ab82c313228da05bdf3f3f1
  - path: ../../raw/aphl-global-health-resources-current-2026-07-12.html
    role: current-official-catalogue-page
    sha256: 5ed0acd0e6a36635ffd4fc456935f3a62eed06e6434c772cae961d5395db7c70
canonical_url: https://aphl.org/resources/resource-detail/laboratory-data-and-integrated-laboratory-information-systems-implementation-guide
repository_url: https://aphl.org/docs/default-source/technical/gh-lis-integration-guide.pdf
aims_url: https://aphl.org/resources/resource-detail/centralized-public-health-data-exchanges--a-toolkit-for-platform-designers--technologists-and-public-health-decision-makers
implementation_url: https://aphl.org/our-publications/stories/lab-culture-news/blog-post/creating-more-modern-laboratory-systems-in-uganda
catalogue_url: https://aphl.org/focus-areas/global-health/resources/GH-resources
accessed: 2026-07-12
publication_dates:
  lis_guide: 2024-03
  aims_toolkit: 2025-05
  uganda_story: 2026-05-20
issuer: Association of Public Health Laboratories
partners:
  - Ruvos LLC
  - US Centers for Disease Control and Prevention
tags:
  - clinical-laboratory
  - public-health-laboratory
  - informatics
  - LIS
  - LIMS
  - middleware
  - EHR
  - HIE
  - public-health-data-exchange
  - cloud
  - identity-access-management
  - interface-validation
  - evidence-quality
---

# APHL integrated laboratory information and public-health exchange package

## Artifact identity and complete-package review

The preserved package contains one APHL informatics lineage at three evidence
states: technical guidance, an issuer-described operating platform/toolkit and
an issuer-reported implementation companion.

- Main March 2024 *Laboratory Data and Integrated Laboratory Information
  Systems Implementation Guidance*: 39 physical pages, 8,235,175 bytes,
  SHA-256
  `f6df76580f8ae3de199c49fd62b1a8b72317db79ab2f260b72e0e1bd830fee46`.
- May 2025 *Centralized Public Health Data Exchanges: A Toolkit for Platform
  Designers, Technologists and Public Health Decision Makers*: 54 physical
  pages, 2,990,975 bytes, SHA-256
  `07c44899020fdc953b3593c1d9d432cdaaf995a7a4dfa1912abe2bf20cf0566e`.
- APHL's 20 May 2026 Uganda implementation story: 330,931 bytes, SHA-256
  `031506a652cbb05892aae17149290a6b5e4d41ed5ab82c313228da05bdf3f3f1`.
- Current APHL Global Health Resources catalogue: 491,321 bytes, SHA-256
  `5ed0acd0e6a36635ffd4fc456935f3a62eed06e6434c772cae961d5395db7c70`.

Two official retrievals of every artifact on 2026-07-12 were byte-identical.
Both tagged, unencrypted PDF 1.7 files have no form, JavaScript, embedded file
or signature. All 93 physical PDF pages were inventoried and read; the
architecture, exchange, instrument, public-health and message-processing
figures were rendered and inspected. Both HTML pages were reviewed statically
without executing scripts, forms or third-party content.

All 39 LIS-guide pages and all 54 AIMS pages contain extractable text; neither
PDF has a blank or wholly image-only page. AIMS physical p. 18 is
image-dominant, so all three ETOR/AR diagrams were read from the render;
physical pp. 2–53 match visible page numbers, while p. 1 cover and p. 54
credits/funding page are unnumbered.

The 2024 PDF cover says `Implementation Guidance`, while XMP title says `LIS
Integration Guide`; both identities are retained. Its section contents are
correct, but the p. 3 list of figures places every Figure 1–24 one physical page
late (for example, Figure 1 is on physical p. 5, not p. 6, and Figure 24 is on
p. 38, not p. 39). All locators in this wiki use the visually verified physical
pages rather than that defective figure list.

> **Claim record — SRC-0027-C01 | artifact-observation**
> **Claim:** The preserved package is a complete, reproducible APHL set of the
> March 2024 LIS guide (39/39 nonblank, text-bearing pages), May 2025 AIMS
> toolkit (54/54 nonblank, text-bearing pages), dated May 2026 implementation
> story and current catalogue page; each PDF has zero blank and zero wholly
> image-only pages, and every artifact/retrieval matches its byte count/hash.
> **Claim status:** active
> **Scope:** Artifact identity, completeness and reproducibility checked
> 2026-07-12; not endorsement of every architecture example or technology name.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Full 39- and 54-page PDFs; HTML title/date/article and catalogue
> entries; local hashes, byte counts, `pdfinfo`, page inventory and static
> visual review.
> **Basis / limits:** Completeness and file properties are locally observable.
> Dynamic site navigation is not substantive evidence.

## Lineage and evidence modalities

> **Claim record — SRC-0027-C02 | artifact-observation**
> **Claim:** The four artifacts are one APHL informatics lineage, not four
> independent sources: the 2024 document is technical guidance, the 2025
> toolkit combines an issuer description of AIMS with reusable guidance and the
> 2026 story is APHL/partner-reported implementation.
> **Claim status:** active
> **Scope:** Lineage and modality classification; no CDC-policy, regulator,
> independent-conformance or independent-effectiveness claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** LIS guide cover/purpose pp. 1 and 4; AIMS purpose,
> acknowledgments and disclaimer pp. 6 and 54; Uganda article byline,
> paragraphs 2–4 and named supporting organizations; APHL catalogue entries.
> **Basis / limits:** Ruvos prepared the AIMS document as APHL's long-term
> technical partner; CDC funded/reviewed it, while p. 54 says the contents are
> the authors' responsibility and not necessarily CDC/HHS/U.S. Government
> views or endorsement. Partner count therefore does not create independence.

## Laboratory-system classes and boundaries

> **Claim record — SRC-0027-C03 | source-report**
> **Claim:** APHL's LIS guide joins the required clinical/public-health system
> classes: laboratory instruments and point-of-care devices, middleware or
> integration engines, LIS/LIMS, EMR/EHR/HIS/HMIS, higher-tier referral
> laboratories, central repositories/exchanges and surveillance/reporting
> systems.
> **Claim status:** active
> **Scope:** Functional class map and exchange roles, not a universal topology
> or assertion that every laboratory deploys every component.
> **As of:** 2024-03-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** LIS guide §§2.1–2.4, pp. 5–10; §§7–10, pp. 16–32;
> Appendix §13.2–13.3, pp. 36–38; Figures 1–8, 12–24.
> **Basis / limits:** Classes and example interactions are direct. The guide is
> globally oriented implementation guidance, not a deployment census.

> **Claim record — SRC-0027-C04 | source-report**
> **Claim:** APHL defines interface boundaries by sender/receiver roles,
> initiator, exact exchanged fields and expected responses, data format,
> communication/security agreement, identity keys, transformation and repeated
> testing plus ongoing monitoring and maintenance.
> **Claim status:** active
> **Scope:** Validation-aware interface definition and lifecycle requirements;
> no protocol recipe, acceptance threshold or completed-conformance result.
> **As of:** 2024-03-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** LIS guide §§3.2, p. 10; §§5–8.3.6, pp. 12–21; §§11–13,
> pp. 32–38, especially pp. 17, 19–21, 32–33 and 36–38.
> **Basis / limits:** Required definition/test/monitor states are direct;
> precise protocols, credentials, endpoints and operational thresholds are
> intentionally omitted from the wiki.

> **Claim record — SRC-0027-C05 | source-report**
> **Claim:** The guide explicitly maps one- and two-way
> instrument↔middleware↔LIS exchanges, including point-of-care middleware,
> analyzer result transfer, result/test mapping and transfer-history monitoring.
> **Claim status:** active
> **Scope:** Defensive functional boundary; no device-specific interface,
> command sequence or facility configuration.
> **As of:** 2024-03-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** LIS guide §6.1.3, pp. 14–15; §8.3.4, p. 20; §9.1.4,
> pp. 22–23; §§9.2–9.5, pp. 24–26; §13.2, pp. 36–37; Figures 17–18
> and 22–23.
> **Basis / limits:** The exchange directions and monitoring functions are
> direct; implementation examples do not establish every device's support.

> **Claim record — SRC-0027-C06 | source-report**
> **Claim:** Referral boundaries are explicit: a local LIS can send order,
> patient/specimen context and a specimen referral to another or higher-tier
> laboratory, whose LIS returns reviewed results to the originating LIS/EMR.
> **Claim status:** active
> **Scope:** Referral/reference-laboratory information flow at safe abstraction;
> not sample-routing detail or chain-of-custody proof for a named case.
> **As of:** 2026-05-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** LIS guide §8.2.8, p. 19; §§9.1.1–9.1.3, pp. 22–23;
> Uganda article, `From point A to point B` paragraphs 1–5.
> **Basis / limits:** The guide supplies higher-tier/referral flow; the article
> supplies the literal national-reference-laboratory deployment context. Both
> remain one APHL lineage.

## Public-health exchange, cloud and identity

> **Claim record — SRC-0027-C07 | source-report**
> **Claim:** The AIMS toolkit describes a current operating public-health
> exchange connecting laboratories, healthcare providers/EHRs, HIEs and
> public-health agencies for ELR, eCR and electronic test-order/result uses.
> **Claim status:** active
> **Scope:** APHL issuer-described AIMS functions and participants; no
> independent traffic audit, universal U.S. coverage or legal-compliance
> conclusion.
> **As of:** 2025-05-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** AIMS toolkit Executive Summary pp. 2–3; Platform Story
> pp. 7–18; technical-assistance/LIMS connection pp. 27–28; terminology p. 53.
> **Basis / limits:** HIE, EHR, laboratory, provider, agency and use-case
> predicates are literal. Scale figures are issuer-reported and not required
> for the architecture criterion; differently defined daily/monthly/message
> counts in the toolkit are not merged into one metric.

> **Claim record — SRC-0027-C08 | source-report**
> **Claim:** APHL's model and operating-platform description covers cloud and
> hybrid hosting, on-premises gateways/middleware, ESB/API gateways and
> interface engines together with IAM, RBAC, SSO, federated authentication,
> identity providers, audit logging, health checks and continuity functions.
> **Claim status:** active
> **Scope:** Functional trust-boundary and control classes; no reusable
> production topology, credential, endpoint, configuration value or claim that
> architecture language alone proves effectiveness.
> **As of:** 2025-05-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** AIMS toolkit pp. 7–14 and 19–28, especially pp. 20–23 and 27;
> implementation considerations pp. 29–38; cloud comparison pp. 50–53.
> **Basis / limits:** The current platform functions and reusable model are
> separated in the source. Specific technology examples are not universal
> requirements and are retained only at class level.

> **Claim record — SRC-0027-C09 | source-report**
> **Claim:** APHL describes actual AIMS sender self-test/inline validation,
> test/staging/production observability, an earlier cloud proof of concept,
> CI/CD testing and health monitoring; separately, its reusable guidance lists
> partner-format checks, production-readiness documentation and validation/
> testing→go-live→evaluation onboarding stages.
> **Claim status:** active
> **Scope:** Issuer-described message/interface and deployment-state checks;
> not an independent conformance certificate or outcome evaluation.
> **As of:** 2025-05-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** AIMS toolkit Data Enhancement and Partner Services pp. 9–10;
> cloud proof-of-concept p. 13; security/infrastructure/gateway pp. 20–23;
> governance pp. 24–25; illustrative documentation and onboarding pp. 44–49.
> **Basis / limits:** Actual issuer-described platform checks and reusable
> documentation/stage recommendations are explicitly separated. The latter are
> not completed AIMS validations, and no audit/test-result package establishes
> independent conformance or effectiveness.

> **Claim record — SRC-0027-C10 | source-report**
> **Claim:** APHL reports that Uganda's sample-tracking, laboratory repository
> and dashboard package underwent phased testing and validation at selected
> facilities before multi-site rollout; it includes a national-reference-
> laboratory referral workflow, while the repository separately connects
> multiple laboratories/health systems to authorized public-health users.
> **Claim status:** active
> **Scope:** Dated APHL issuer/partner implementation report; not independent
> deployment census, validation protocol, acceptance result or outcome study.
> **As of:** 2026-05-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** Uganda article title/date/byline; opening paragraphs 1–3;
> `From point A to point B` paragraphs 1–5; `Data in near real time`
> paragraphs 1–3; `Looking ahead` paragraphs 1–4.
> **Basis / limits:** Deployment, phased testing, class-level connectivity and
> remaining work are direct APHL statements. User satisfaction and scale are
> issuer-reported signals, not independently evaluated effectiveness.

## Currentness and criterion boundary

The 2024 guide reuses a 2019 APHL LIS definition and points to 2003 public-
health LIMS requirements; an ICD-10 footnote uses a 2019 browser, and its
HL7/FHIR/ASTM/SiLA comparisons are unversioned or simplified. Country examples
and benefits lack separate methods/metrics, while the p. 33 fully digital/
IoT/AI language is aspirational. None is used here as a current standards
version, conformance result, deployment census or measured outcome.

> **Claim record — SRC-0027-C11 | artifact-observation**
> **Claim:** APHL's current catalogue still lists the 2024 LIS and 2025 AIMS
> guides on 2026-07-12 and the May 2026 story is a later implementation
> snapshot; embedded older definitions/references, unversioned standards,
> uncited benefit/country examples and aspirational forecasts are not silently
> treated as current standards, conformance, deployment or outcome evidence.
> **Claim status:** active
> **Scope:** Official APHL catalogue/site search and current presentation as of
> the access date; absence of a located successor is not evidence that none can
> exist elsewhere.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Preserved APHL catalogue entries; PDF dates/copyright; Uganda
> page date; LIS guide pp. 5–6, 14–15 and 33; bounded official-site search
> completed 2026-07-12.
> **Basis / limits:** Current presentation and embedded source dates/genres are
> direct. The bounded search located no successor but cannot prove none exists.

> **Claim record — SRC-0027-C12 | artifact-observation**
> **Claim:** Complete SF2 integration and independent strict review promote only `CPH-SD`:
> the package fills instruments, middleware/LIS, EHR/HIE, reference-laboratory,
> public-health-platform, cloud/IAM and tested-boundary predicates, but does not
> supply a new patient outcome or independent effectiveness evaluation.
> **Claim status:** active
> **Scope:** Accepted frozen-rubric cell boundary after independent artifact,
> lineage, graph and cell review; not certification by APHL alone.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0027-C02`–`C11`; frozen `CPH-SD/CI/AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md); prior `SYN-0001-C20`
> checkpoint at 36/110.
> **Basis / limits:** APHL supplies the missing coherent architecture and
> validation-aware boundary package. Independent existing sources remain
> necessary for SF2, and implementation/test language is not effectiveness.
> Independent review completed 2026-07-12.

## Safety handling

The wiki retains only system classes, role/trust boundaries, evidence states
and defensive validation functions. It omits geographic exchange maps,
facility identities, endpoints, message-routing detail, credentials, protocol
recipes, operational thresholds and any patient/specimen record.

## Integration map

- [SYS-0009 — integrated clinical/public-health system map](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [SYN-0014 — CPH system-boundary reconciliation](../syntheses/syn-0014-clinical-public-health-system-boundary-reconciliation.md)
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)
