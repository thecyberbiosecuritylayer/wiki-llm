---
id: SRC-0018
type: source
title: NIST SP 800-82 Rev. 3 Guide to Operational Technology Security
aliases:
  - NIST SP 800-82r3
  - Guide to Operational Technology OT Security
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-11
source_type: normative-guidance
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/nist-sp-800-82r3-ot-security-2023.pdf
sha256: 608f554514d381853e24e0b33123b7080fbd757826f460032690aade63394616
canonical_url: https://csrc.nist.gov/pubs/sp/800/82/r3/final
direct_pdf_url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
doi: 10.6028/NIST.SP.800-82r3
accessed: 2026-07-12
issuer: National Institute of Standards and Technology
publication_date: 2023-09-28
approval_date: 2023-09-20
jurisdictions:
  - United States
external_companions:
  - title: NIST SP 800-82 Rev. 3 potential updates spreadsheet
    canonical_url: https://csrc.nist.gov/files/pubs/sp/800/82/r3/final/docs/sp800-82r3-potential-updates.xlsx
    accessed: 2026-07-12
    transient: true
  - title: NIST SP 800-82 Rev. 4 initial preliminary draft call
    canonical_url: https://csrc.nist.gov/pubs/sp/800/82/r4/iprd
    accessed: 2026-07-12
    transient: true
tags:
  - operational-technology
  - industrial-control
  - nist
  - defense-in-depth
  - resilience
---

# NIST SP 800-82 Rev. 3 Guide to Operational Technology Security

## Artifact identity and complete review

- Immutable artifact: `../../raw/nist-sp-800-82r3-ot-security-2023.pdf`,
  8,584,345 bytes, 316 physical pages, SHA-256
  `608f554514d381853e24e0b33123b7080fbd757826f460032690aade63394616`.
- The official NIST PDF was byte-identical on 2026-07-12. It is a tagged,
  unencrypted PDF 1.6 with a text layer on all pages. It has an AcroForm but no
  XFA, JavaScript, signature, embedded file or launch action. Its `OpenAction`
  is a page navigation.
- All 316 pages were extracted/read; 47 image-bearing pages and the relevant
  figures were rendered/checked. Printed page equals physical PDF page minus
  17. The document contains 299 numbered main/appendix pages after front matter.

> **Claim record — SRC-0018-C01 | artifact-observation**
> **Claim:** The preserved 8,584,345-byte, 316-page PDF is complete and
> byte-identical to the official NIST SP 800-82 Rev. 3 download checked on
> 2026-07-12.
> **Claim status:** active
> **Scope:** Artifact identity, completeness and dated comparison; not
> currentness, adoption or implementation.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Local file/hash, PDF structure/text/render inspection, physical
> PDF pp. 1–316; official NIST byte/hash comparison on 2026-07-12.
> **Basis / limits:** File identity and page mapping are reproducible. External
> status and proposed updates require separate currentness evidence.

## OT scope and operating constraints

NIST defines OT broadly as programmable systems/devices that interact with the
physical environment or manage such interaction. It emphasizes performance,
reliability, availability and safety differences from conventional IT. The
guidance is risk-based and contextual rather than a universal checklist; some
common IT controls can disrupt operations or safety if transferred directly.

> **Claim record — SRC-0018-C02 | source-report**
> **Claim:** SP 800-82 Rev. 3 defines a broad physical-interaction OT scope and
> requires security decisions to account for OT performance, reliability,
> availability and safety constraints rather than copying an IT checklist.
> **Claim status:** active
> **Scope:** General OT guidance, not every cyberphysical or biological system.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract and §1.1, printed p. 6 (physical PDF p. 23); §2.4 and
> Table 1, printed pp. 28–32 (PDF pp. 45–49).
> **Basis / limits:** Scope and differences are direct. Applicability to a
> sector/deployment requires independent evidence and tailoring.

## System classes and sector anchors

The document describes SCADA, PLC, DCS, BAS, physical access control, safety
systems and IIoT classes. Its DCS discussion explicitly includes
pharmaceutical processing, while Food and Agriculture appears only as a
critical-infrastructure sector label. BAS/HVAC/PACS and pharmaceutical DCS are
useful component anchors, not laboratory-containment, GMP or farm topologies.

> **Claim record — SRC-0018-C03 | source-report**
> **Claim:** NIST directly covers major control, building/access, safety and
> IIoT system classes and names pharmaceutical processing under DCS, but it
> does not validate a biomanufacturing plant, high-containment laboratory or
> smart-farm architecture.
> **Claim status:** active
> **Scope:** Generic system classes and explicit sector mentions; no deployed
> topology or complete sector workflow.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§2.2–2.3.8, printed pp. 9–28 (PDF pp. 26–45), especially
> §2.3.3 p. 19 and Figures 7, 9–12.
> **Basis / limits:** Classes and the pharmaceutical anchor are direct. Sector-
> specific architecture, custody, quality and biological consequences are not.

## Risk and consequence framing

NIST describes possible production, product-contamination, equipment, safety,
environmental, regulatory and continuity impacts, then links cyber/physical
dependencies to hazard analysis, PHA/FMEA and customizable impact categories.
These are risk-analysis categories and examples, not documented incidents,
frequency estimates or sector-specific causal findings.

> **Claim record — SRC-0018-C04 | source-report**
> **Claim:** SP 800-82 Rev. 3 supports cyberphysical risk analysis that includes
> potential process, product, safety, environmental and continuity consequences
> and integrates PHA/FMEA-style reasoning.
> **Claim status:** active
> **Scope:** Potential OT consequence/risk-analysis categories, not occurrence,
> severity calibration or an observed cyberbiosecurity event.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§3.2–3.2.1, printed pp. 34–35 (PDF pp. 51–52);
> §§4.1.1–4.1.2, printed pp. 46–52 (PDF pp. 63–69); Tables 3–5.
> **Basis / limits:** Categories and methods are direct. Tables are
> customizable examples and cannot be applied as ready sector risk ratings.

## Control and assurance families

The guidance covers programme lifecycle, inventory/data-flow mapping,
configuration/change control, segmentation/DMZs, identity/access, remote
access, logging/passive monitoring, safety-aware/manual fallback, incident
response, backups/restoration, supply chain and assessment/continuous
monitoring. Recommended controls must be selected against OT constraints.

> **Claim record — SRC-0018-C05 | source-report**
> **Claim:** NIST provides a full generic OT control portfolio across govern/
> inventory, prevent, detect, contain/respond, recover and assure, with explicit
> safety/availability prerequisites and tradeoffs.
> **Claim status:** active
> **Scope:** Recommended general OT control functions, not implementation,
> compliance or suitability for every sector edge.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §3, printed pp. 33–43 (PDF pp. 50–60); §§4–6, printed
> pp. 44–138 (PDF pp. 61–155); Appendices E–F, printed pp. 207–298
> (PDF pp. 224–315).
> **Basis / limits:** Portfolio breadth and qualifications are direct. Exact
> sector transfer requires an independently supported dependency/path.

## Tailoring, overlay and compensating controls

Appendix F is a cross-sector OT overlay and explicitly partial; organizations
must tailor it. Compensating controls require documented rationale,
equivalent/comparable protection and residual-risk decision and are not a
waiver. The appendix's federal/nongovernmental applicability boundary is not a
universal legal obligation.

> **Claim record — SRC-0018-C06 | source-report**
> **Claim:** The OT overlay is a tailoring starting point, and a compensating
> control requires documented equivalence and residual-risk treatment rather
> than being assumed compliant or effective.
> **Claim status:** active
> **Scope:** Appendix F use boundary; not a system authorization or legal-
> applicability decision.
> **As of:** 2023-09-28.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Appendix F note and §F.2, printed pp. 213–214
> (PDF pp. 230–231); §F.4, printed pp. 223–224 (PDF pp. 240–241).
> **Basis / limits:** Partial-overlay/tailoring and compensating-control
> qualifications are direct. An organization's actual rationale is absent.

## Evidence maturity and excluded uses

Notional architecture figures do not show deployed systems. Appendix C's
incident summaries are secondary/historical and heterogeneous; Appendix D is a
programme/resource directory; Appendix E describes capability categories.
None supplies a sector implementation, control test or effectiveness result.
The source uses CSF 1.1 and a versioned SP 800-53 Rev. 5 baseline; it is not a
native CSF 2.0 mapping.

> **Claim record — SRC-0018-C07 | analytic-judgment**
> **Claim:** This source supports current generic OT guidance and historical
> context only; it provides no deployed cyberbio architecture, primary `INC`,
> completed safeguard test, adoption census or independent effectiveness
> evaluation.
> **Claim status:** active
> **Scope:** Evidence classification for this transaction, not a finding that
> no implementation or incident exists elsewhere.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Full-document review; especially §1.1, Appendix C notes,
> Appendix D and Appendix E/F boundaries, printed pp. 6, 169–298.
> **Basis / limits:** Document genre, notional/example labels and missing result
> records are observable. External deployments/evaluations need new sources.

## Current status and revision activity

NIST's publication record still marked Rev. 3 `Final` on 2026-07-12. A
22 January 2026 Rev. 4 initial-preliminary/pre-draft call opened a revision
process but did not publish or supersede Rev. 3. NIST's `potential updates`
spreadsheet is a planning artifact, not an applied erratum.

> **Claim record — SRC-0018-C08 | source-report**
> **Claim:** Rev. 3 remained the current final edition on 2026-07-12; Rev. 4
> activity was only a preliminary revision call and did not supersede it.
> **Claim status:** active
> **Scope:** NIST publication status checked 2026-07-12; revision activity can
> change quickly.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** NIST Rev. 3 final publication record and Rev. 4 initial
> preliminary draft page checked 2026-07-12; Rev. 3 front matter.
> **Basis / limits:** Official status labels are direct. A later draft/final or
> erratum requires immediate re-review.

## Artifact and proposed-update defects

Table 2 at printed p. 43 visibly contains malformed appendix references such as
`Appendices 169 and 186`; the TOC/§1.3 show that appendix letters were intended.
This is recorded as a local artifact observation, not an official correction.
Separately, NIST's potential-updates spreadsheet proposes changing `PL-4(1)` to
`PL-8(1)` on printed p. 268; NIST had not applied it as an official erratum.

> **Claim record — SRC-0018-C09 | artifact-observation**
> **Claim:** The PDF contains a locally observed Table 2 appendix-label defect,
> while NIST separately lists one proposed p. 268 control-reference update;
> neither is silently corrected in the immutable artifact.
> **Claim status:** active
> **Scope:** Document-quality observations and dated planning spreadsheet, not
> substantive reinterpretation of the OT guidance.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Table 2 and §1.3, printed pp. 7 and 43 (PDF pp. 24 and 60);
> TOC; official potential-updates spreadsheet checked 2026-07-12, row for
> printed p. 268.
> **Basis / limits:** Visible text and official proposed change are direct. The
> Table 2 interpretation is local and the spreadsheet is not an issued erratum.

## Safety boundary

No facility layout, network address, credential/configuration recipe or attack
procedure is reproduced. Architecture and control descriptions stay at generic
defensive class/function level. Appendix C does not generate incident pages.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [SYS-0007 — bounded biobank informatics/storage plus generic OT overlay](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SRC-0023 — NIH IRP ELN Policy](src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
- [SYN-0010 — LAB scope/asset/lifecycle reconciliation](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [SYN-0011 — LAB system-boundary reconciliation](../syntheses/syn-0011-laboratory-biobank-system-boundary-reconciliation.md)
- [GOV-0008 — NIST OT governance](../governance/gov-0008-nist-sp-800-82r3-ot-security-2023.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [CTL-0015 — Q13 quality-gate complement to generic OT controls](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [SYN-0007 — OT applicability across cyberbio sectors](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [SYS-0001 — HCL support systems](../systems/sys-0001-hcl-containment-support-systems.md)
- [SYS-0002 — Biomanufacturing process control](../systems/sys-0002-biomanufacturing-process-control.md)
- [SYS-0005 — Connected smart farm](../systems/sys-0005-connected-smart-farm-ecosystem.md)
- [RSK-0001 — HCL containment disruption](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [RSK-0002 — Biomanufacturing control disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [RSK-0007 — Farm production/supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [CTL-0001 — Laboratory controls](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
- [CTL-0005 — Agricultural controls](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SYN-0017 — Agriculture transfer/control/governance reconciliation](../syntheses/syn-0017-au-agriculture-transfer-control-governance-reconciliation.md)

## Official links

- Final record: <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Official PDF: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf>
- Rev. 4 preliminary call: <https://csrc.nist.gov/pubs/sp/800/82/r4/iprd>
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
