---
id: SRC-0042
type: source
title: AAFC chicken-farm cyberattack and reported animal-effect account, 2023
aliases:
  - AAFC Episode 036 chicken farm incident
  - From Fences to Firewalls cyber security in agriculture
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-15
source_type: official-canadian-government-interview-transcript-and-hypothetical-guidance
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/aafc-episode-036-cyber-security-agriculture-current-2026-07-12.html
sha256: 21e48f8337a2aff3128883afa319835e52f5d8e368b730f4d528c5aa8a593720
raw_components:
  - path: ../../raw/aafc-cyber-security-dairy-sector-case-study-2024.pdf
    role: same-lineage-hypothetical-mechanism-and-control-companion
    sha256: a52776f5a686fde9261c59e2445a16d895616e42dc02f923eedd5b09f82fe3b9
canonical_url: https://agriculture.canada.ca/en/agri-info/episode-036-fences-firewalls-cyber-security-agriculture
infographic_url: https://agriculture.canada.ca/sites/default/files/documents/2024-10/cyber-security-infographic_v2-eng.pdf
accessed: 2026-07-12
published: 2025-10-15
page_modified: 2025-10-15
issuer: Agriculture and Agri-Food Canada
speaker: Ali Dehghantanha
speaker_role: Canada Research Chair in Cybersecurity, University of Guelph
jurisdictions:
  - Canada
tags:
  - agriculture
  - poultry
  - chicken-farm
  - cyberattack
  - temperature-control
  - animal-effect
  - interview-transcript
  - anonymous-incident
---

# AAFC chicken-farm cyberattack and reported animal-effect account, 2023

## Identity, acquisition and complete review

The primary artifact is the complete current official AAFC Episode 036 HTML
page, including its full transcript and 2025-10-15 issued/modified metadata.
The companion is AAFC's one-page 2024 illustrative conditional dairy-sector
infographic. Both
were retrieved twice from official URLs with byte-identical results.

The two declared objects total 206,970 bytes and match the frontmatter hashes.
The HTML contains 11 scripts, one form, one external iframe/player, one audio
element and an external media source; nothing was executed, submitted or
played. The transcript, not the audio, is the represented evidence. The PDF is
unsigned, unencrypted, has no JavaScript/embedded files and was reviewed both
as extracted text and rendered layout. Extraction emitted invalid-font-weight
warnings, but the full text and rendered visual content remained readable.

> **Claim record — SRC-0042-C01 | artifact-observation**
> **Claim:** The retained 206,970-byte package contains a complete official
> AAFC transcript page and one-page same-lineage infographic with exact hashes,
> repeat-retrieval identity and full static/text/visual review.
> **Claim status:** active
> **Scope:** Declared artifacts; not transcript-to-audio verification, runtime
> assurance, cryptographic authentication or proof the page never changed.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths/hashes; full transcript/PDF review; repeat
> official retrieval comparison; HTML tag and PDF metadata inspection.
> **Basis / limits:** File identity and content state are reproducible; the PDF
> is unsigned and external media was not required or executed.

> **Claim record — SRC-0042-C02 | artifact-observation**
> **Claim:** The official page identifies AAFC as publisher, Ali Dehghantanha
> as the interviewed Canada Research Chair/University of Guelph expert and
> 2025-10-15 as both issued and modified date.
> **Claim status:** active
> **Scope:** Page metadata and attributed speaker role; not government adoption
> of every interview statement or independent validation of the account.
> **As of:** 2025-10-15; verified 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** HTML title/introduction, transcript attribution and
> `dcterms.issued/modified` metadata.
> **Basis / limits:** Publication and attribution are direct; speaker testimony
> remains distinct from AAFC institutional findings.

## Anonymous late-December 2023 chicken-farm account

Asked for the scariest farm cyberattack he had seen, Ali describes a late-
December 2023 call about a chicken farm. He reports the caller saying that barn
temperature control was being lost and chicks were dying. The source does not
identify the farm, jurisdiction, caller, system, technique, animal count,
duration, veterinary record, forensic report or independent investigation.

> **Claim record — SRC-0042-C03 | source-report**
> **Claim:** In direct responder testimony, Ali recounts receiving a call in
> late December 2023 during a chicken-farm cyberattack and the farmer's
> contemporaneous report of losing barn-temperature control while chicks were
> dying.
> **Claim status:** active
> **Scope:** One anonymous source-reported event/path; not exact date/location,
> firsthand observation of the animals, forensic causality, actor/vector,
> system identity, duration or death count.
> **As of:** Late December 2023 account, published 2025-10-15.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** Official transcript, question beginning `What has been the
> scariest example...` and Ali response beginning `Well, the scariest for me...`.
> **Basis / limits:** Call receipt and relayed farm state are direct speaker
> testimony; animal state and cyber linkage are not independently investigated.

> **Claim record — SRC-0042-C04 | analytic-judgment**
> **Claim:** At safe abstraction, the account supplies a complete reported
> `cyberattack context → loss of digital/automated barn-temperature control →
> chicks dying` path and therefore a cyber→animal-effect example.
> **Claim status:** active
> **Scope:** Source-reported functional path; not proof of malware/command
> mechanism, threshold, exact causal contribution, prevalence or generality.
> **As of:** Event account late December 2023.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `SRC-0042-C03`; official transcript same question/response.
> **Basis / limits:** The source frames the event as a cyberattack and places
> control loss and deaths in the same contemporaneous report. No forensic or
> veterinary confirmation is represented.

> **Claim record — SRC-0042-C05 | source-report**
> **Claim:** The speaker reports the farmer saying that temperature change for
> more than 15 minutes causes chicks to start dying, but the source does not
> establish that the event lasted 15 minutes or validate that threshold.
> **Claim status:** active
> **Scope:** Reported response-time context only; not an operating limit,
> husbandry instruction, measured event duration or causal experiment.
> **As of:** 2025-10-15 transcript.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** Official transcript, paragraph immediately following the
> chicken-farm account.
> **Basis / limits:** The threshold is nested farmer testimony and is not used
> as a facility parameter or quantified incident fact.

## Location, actor and mechanism boundaries

The earlier Southern Ontario exchange describes the laboratory's 2024 call
volume, not the 2023 chicken-farm location. Later generic comments mention
attackers, ransomware and access patterns; they are not incident-specific
forensic facts. The incident is not assigned to Ontario, ransomware, a product,
an entry vector or a named actor.

> **Claim record — SRC-0042-C06 | analytic-judgment**
> **Claim:** The transcript does not locate or attribute the chicken-farm event
> and does not establish its malware class, initial access, affected product,
> exact control architecture, recovery or investigation result.
> **Claim status:** active
> **Scope:** Explicit unknowns for this event; not evidence that these facts do
> not exist outside the retained source.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-15.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Full transcript review and `SRC-0042-C03`–`C05`.
> **Basis / limits:** Adjacent generic/region statements are not silently
> attached to the event.

## Same-lineage hypothetical dairy mechanism

The AAFC infographic introduces an illustrative hypothetical farmer `Alex` and
says a
phishing link could download ransomware, spread across a farm network, stop
autonomous milking, disrupt schedule and affect cow health/milk production. It
lists training, antimalware, segmentation, isolated backups, insurance and
incident planning as possible mitigations. It is explanatory design, not an
observed incident, deployed control or effectiveness test.

> **Claim record — SRC-0042-C07 | source-report**
> **Claim:** AAFC's illustrative hypothetical dairy case provides an explicit safe
> `phishing→ransomware→network/data unavailability→autonomous-milking stop→
> cow-health/milk-production effect` mechanism and recommended controls.
> **Claim status:** active
> **Scope:** One hypothetical AAFC scenario; not a real farmer/event, current
> threat prevalence, product weakness, deployment or effectiveness evidence.
> **As of:** PDF created 2024-10-03.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** One-page PDF, title/introduction, `Autonomous milking machines`
> and `Alex's situation could have been mitigated` panels.
> **Basis / limits:** The conditional illustrative framing is direct and retained.

## Source independence and count boundaries

The official AAFC transcript is one Canadian government-hosted source with one
direct responder account. The interviewee is not the farmer, veterinarian,
forensic investigator or independent confirmer. AAFC transcript and infographic
are one lineage. Existing Virginia Tech/Drape, U.S. FBI-advisory and AU/
PATH-SAFE evidence are materially independent for their distinct roles.

> **Claim record — SRC-0042-C08 | analytic-judgment**
> **Claim:** The AAFC account is a new SF1 forward-effect lineage independent
> from existing Drape/FBI and AU/PATH-SAFE roles, but it supplies neither SF3
> independent confirmation nor a second event through its infographic.
> **Claim status:** active
> **Scope:** Claim-specific source independence; not institutional validation,
> forensic corroboration or source/page multiplication.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0042-C01`–`C07`; issuer/speaker roles; existing sources.
> **Basis / limits:** Direct account and source roles are explicit.

> **Claim record — SRC-0042-C09 | analytic-judgment**
> **Claim:** The transcript's 46 laboratory responses in Southern Ontario in
> 2024, the separate UPA event and other anonymous examples are not multiplied
> into `INC` pages or attributed to the chicken-farm account in this transaction.
> **Claim status:** active
> **Scope:** Wiki event-count boundary; not a conclusion that those reports are
> false or unimportant.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Full transcript and local bounded transaction design.
> **Basis / limits:** No report-to-event mapping or independent records exist
> in the retained package for those adjacent statements.

> **Claim record — SRC-0042-C10 | analytic-judgment**
> **Claim:** `SRC-0042` supplies candidate evidence for `AGE-XT` and one
> anonymous agriculture incident, but no frozen cell or global gate changes
> before canonical event/path creation and explicit SF2 synthesis.
> **Claim status:** superseded
> **Scope:** Wiki source-transaction state before `SYN-0027`.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0042-C03`–`C09`; frozen criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Candidate evidence is not arithmetic promotion.
> **Superseded by:** `SYN-0027-C05/C07` after canonical SF2 reconciliation.

## Safety boundary

> **Claim record — SRC-0042-C11 | analytic-judgment**
> **Claim:** The page preserves anonymity and exposes no farm/location,
> product, endpoint, identifier, credential, exploit, access route, temperature/
> setpoint, validated operating threshold/instruction or targetable system
> configuration; the unvalidated 15-minute testimony is urgency context only.
> **Claim status:** active
> **Scope:** Local page, not the complete public external artifacts.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and explicit uncertainty boundaries.
> **Basis / limits:** Only high-level defensive path evidence is retained.

## Integration map

- [INC-0005](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
- [RSK-0018](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md)
- [SYN-0027](../syntheses/syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)

## Official links

- <https://agriculture.canada.ca/en/agri-info/episode-036-fences-firewalls-cyber-security-agriculture>
- <https://agriculture.canada.ca/sites/default/files/documents/2024-10/cyber-security-infographic_v2-eng.pdf>
