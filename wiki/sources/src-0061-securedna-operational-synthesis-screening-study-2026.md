---
id: SRC-0061
type: source
title: SecureDNA operational synthesis-screening study, peer-reviewed 2026
aliases:
  - SecureDNA global DNA-synthesis screening operational study
  - Baum et al. private synthesis-screening study
  - A system capable of verifiably and privately screening global DNA synthesis
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-13
source_type: peer-reviewed-operational-synthesis-screening-study-and-provenance-package
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/securedna-peer-reviewed-article-current-2026-07-13.html
raw_bytes: 203503
sha256: 185a2273d3162a4f8aebaa02fb97a507b875e590e67207df85c4481d7011538e
raw_components:
  - path: ../../raw/securedna-operational-screening-preprint-2024.pdf
    role: complete-36-page-author-preprint-v2-and-page-stable-study-record
    bytes: 5000310
    sha256: 5f9b9cbcb41bd074f9d5aacd8b404ace1aac0942c138c8509c8fe1952558035a
  - path: ../../raw/securedna-peer-reviewed-doi-current-2026-07-13.json
    role: crossref-bibliographic-publication-and-license-metadata
    bytes: 19175
    sha256: fcb146f9ec8a391368ca9b19a5b77e837508c1c2a261da3b4199883b901ed0bf
canonical_url: https://doi.org/10.1093/nsr/nwag103
doi: 10.1093/nsr/nwag103
accessed: 2026-07-13
publication_date: 2026-02-16
publisher: Oxford University Press
venue: National Science Review
issuers:
  - National Science Review
  - Oxford University Press
jurisdictions:
  - United States
  - Europe
  - China
tags:
  - engineering-biology
  - dna-synthesis
  - sequence-screening
  - operational-study
  - privacy
  - provider-data
  - evidence-limits
---

# SecureDNA operational synthesis-screening study, peer-reviewed 2026

## Artifact identity and reproducibility

The retained package contains the peer-reviewed version-of-record HTML, a
complete 36-page author preprint and Crossref metadata. The canonical wiki
representation retains only aggregate defensive evidence; it does not
reproduce sequences, screening parameters or system implementation details.

> **Claim record — SRC-0061-C01 | artifact-observation**
> **Claim:** Three public objects totaling 5,222,988 bytes are retained with
> exact SHA-256 values; the article HTML and Crossref JSON are parseable, and
> PDF inspection confirms a complete 36-page preprint.
> **Claim status:** active
> **Scope:** Local artifact identity and completeness; not issuer-signature
> authentication, validation of every article conclusion or assurance that a
> live page will remain unchanged.
> **As of:** Retrieved and inspected 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths, byte counts and hashes; `file`, `pdfinfo`,
> complete text extraction and JSON parsing.
> **Basis / limits:** The observations establish the retained acquisition
> state. Multiple representations of one study do not create multiple
> independent empirical lineages.

## Peer-reviewed identity and version lineage

> **Claim record — SRC-0061-C02 | artifact-observation**
> **Claim:** Crossref and the retained journal HTML identify the article as
> *A system capable of verifiably and privately screening global DNA
> synthesis*, published in *National Science Review* by Oxford University
> Press on 2026-02-16 as volume 13, issue 14, article nwag103, DOI
> `10.1093/nsr/nwag103`, under CC BY 4.0;
> the retained preprint is an earlier representation of the same study.
> **Claim status:** active
> **Scope:** Bibliographic identity, publication status and same-study version
> lineage; not independent replication or proof that every preprint statement
> remained unchanged in peer review.
> **As of:** Publication 2026-02-16; metadata checked 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Journal citation header and article metadata; Crossref fields
> `title`, `DOI`, `published`, `container-title`, `volume`, `issue`, `type` and
> `license`; preprint title page.
> **Basis / limits:** The publisher and metadata record agree on identity.
> Crossref is bibliographic corroboration, not an independent evaluation of
> screening performance.

## Operational dataset and deployment scope

> **Claim record — SRC-0061-C03 | source-report**
> **Claim:** The authors report applying the system to anonymized historical
> orders comprising more than 150,000 genes and oligonucleotides and more than
> 67 million nucleotides from participating synthesis providers in the United
> States, Europe and China.
> **Claim status:** active
> **Scope:** Reported study corpus, provider regions and operational-data
> context; not a global provider census, market share, adoption rate or proof
> that every order was screened prospectively before fulfillment.
> **As of:** Corpus reported in the 2026 version of record.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Version-of-record `Abstract` and `Quantifying specificity using
> real-world synthesis data`; Figure 4; preprint printed pp. 7–9.
> **Basis / limits:** Scale, order classes and regions are direct author
> reports. Providers are anonymized and provider-level denominators are not
> available in the retained public package.

## Safe aggregate screening results

> **Claim record — SRC-0061-C04 | source-report**
> **Claim:** Within the reported corpus, more than 99% of sequences passed;
> Figure 4 reports aggregate classifications of 0.57% flagged and 0.27%
> denied or recommended for denial.
> **Claim status:** active
> **Scope:** Study-corpus decision outputs at aggregate level; not a harmful-
> order prevalence, provider-specific result, current production rate,
> universal false-positive/false-negative estimate or observed prevention of
> physical or biological harm.
> **As of:** Corpus reported in the 2026 version of record.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Version-of-record Figure 4 and `Quantifying specificity using
> real-world synthesis data`; preprint printed pp. 7–9.
> **Basis / limits:** The aggregate outputs are directly reported. Pass,
> flag and denial are workflow states; none by itself proves malicious intent,
> a screening failure, unsafe fulfillment or avoided harm.

## Independence, availability and causal limits

> **Claim record — SRC-0061-C05 | analytic-judgment**
> **Claim:** This is a developer-led operational study: article contributors
> designed and implemented the system and conducted its performance and
> specificity analyses; providers remain anonymous, customer raw-order data
> are unavailable publicly because of legal restrictions, and the study
> supplies no causal prevented-harm outcome.
> **Claim status:** active
> **Scope:** Evidence-lineage and access limitations; not an allegation of
> misconduct, a rejection of peer review or a claim that the aggregate results
> are fabricated.
> **As of:** Version of record and public data statement reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Version-of-record `Author contributions`, `Data availability`,
> funding and conflict-of-interest statements; `SRC-0061-C03/C04`.
> **Basis / limits:** Contributor roles, provider anonymity and data-access
> limits are direct. Classifying the lineage as developer-led and separating
> decision outputs from causal harm prevention are analytic evidence controls.

## Safety and contribution boundary

> **Claim record — SRC-0061-C06 | analytic-judgment**
> **Claim:** The package contributes one peer-reviewed, developer-led
> operational screening lineage with a large multi-region anonymized corpus
> and safe aggregate decision outputs, but no independent system evaluation,
> privacy/security audit, provider adoption estimate, incident, raw-order
> replication or causal effectiveness result.
> **Claim status:** active
> **Scope:** Downstream evidence classification for the wiki; not a judgment
> that the system is effective or ineffective outside the reported corpus.
> **As of:** Full retained-package review 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0061-C01`–`C05`; article methods, results, data-
> availability, author-contribution, funding and conflict statements.
> **Basis / limits:** Publication, corpus and aggregate result are direct.
> Independence, generalizability and outcome claims remain bounded by the
> study design and unavailable raw orders.

## Scope and methods

The paper describes a privacy-preserving automated synthesis-order screening
system and evaluates reported performance and specificity against an
anonymized corpus supplied by participating providers. The retained article is
peer reviewed, but the evaluation was performed by contributors who also
developed the system. It is neither a randomized outcome study nor an
independent provider audit, and it contains no exposed-versus-unexposed harm
comparison.

## Limitations and conflicts

- Providers are anonymous, and public raw customer-order data are unavailable;
  provider-level replication and stratified estimates are therefore not
  possible from the retained package.
- The article, preprint and Crossref record are one substantive study lineage,
  not three independent evaluations.
- Corpus-scale percentages do not establish market coverage, current adoption,
  malicious-order prevalence, downstream fulfillment or causal harm avoided.
- The reported privacy and security properties are not an external operational
  privacy or security audit.
- System developers participated in design, implementation and analysis. The
  article reports funding sources and a related MIT patent for two authors;
  these disclosures are retained as evidence context, not treated as proof of
  bias.

## Version status

The journal HTML and Crossref metadata identify a peer-reviewed version of
record published on 2026-02-16, with the journal citation displaying volume 13,
issue 14, July 2026. The 36-page preprint is retained for page-stable locators
and provenance. It is not counted as an independent operational study.

## Safety handling

The full artifacts contain dual-use operational material. Canonical claims
omit all biological sequences and examples, exact screening windows and
decision logic, evasion or split-order mechanics, credentials, infrastructure,
costs and configuration detail. Only high-level system purpose, corpus scope,
aggregate decision outputs and evidence limitations are retained.

## Integration map

- [WFL-0014 — Engineering-biology lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [HAZ-0007 — Non-adversarial failure states](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
- [VUL-0007 — Screening and lifecycle exposure classes](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [CTL-0024 — Benchmark-bounded screening assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [CTL-0006 — Nucleic-acid screening control family](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [RSK-0008 — Bounded screening-classification edge](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)
