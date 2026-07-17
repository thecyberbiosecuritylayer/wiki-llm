---
id: GOV-0026
type: governance
title: NIH genomic-data sharing and generative-AI controlled-access governance
aliases:
  - NIH GDS generative AI governance
  - NIH controlled genomic data AI policy
  - NIH GDS and DUC AI governance
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
source_ids:
  - SRC-0054
jurisdictions:
  - United States
issuer: National Institutes of Health
document_type: nih-award-contract-intramural-policy-with-duc-ai-clarification-and-later-rfi
version: NOT-OD-14-124 with NOT-OD-25-081 interim clarification; NOT-OD-26-023 remains proposed
publication_date: 2014-08-27
adoption_date: 2014-08-27
effective_date: 2015-01-25
instrument_status: current-policy-lineage-with-interim-ai-clarification-and-later-closed-comment-rfi-checked-2026-07-12
binding_status: binding-through-covered-award-contract-intramural-and-data-use-terms-not-general-us-law-rfi-not-binding
implementation_status: formal-issuance-and-conditional-applicability-observed-recipient-compliance-and-outcomes-unknown
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0054
    claim_id: GOV-0026-C01
    evidence:
      - source: SRC-0054
        locator: "NOT-OD-14-124 Sections II-III and compliance paragraph; NOT-OD-25-081 Purpose; NOT-OD-26-023 title/Purpose/Request for Input"
tags:
  - governance
  - united-states
  - nih
  - genomic-data
  - controlled-access
  - generative-ai
  - research-policy
  - data-use-certification
  - proposal-status
---

# NIH genomic-data sharing and generative-AI controlled-access governance

## Status, force and adoption boundary

NIH GDS is a policy for covered NIH grants, contracts, cooperative agreements
and intramural research. The notice makes compliance a term/condition of the
award or contract and identifies possible enforcement including withholding
funding. Controlled-access users and their institutions also accept Data Use
Certification terms. These mechanisms create conditional normative force but
do not make GDS a statute or generally applicable federal regulation.

The March 2025 AI notice interprets existing GDS/DUC non-transferability for
controlled-access human genomic data pending future guidance. The December
2025 notice is an RFI containing draft/proposed rules. It does not supply final
issuance or an effective date and is not represented as current law or policy.

> **Claim record — GOV-0026-C01 | analytic-judgment**
> **Claim:** Current NIH force is bounded to covered award, contract,
> intramural and DUC relationships; the AI clarification operates through that
> substrate, while the later RFI remains nonbinding proposal material.
> **Claim status:** active
> **Scope:** NIH-level force/status currentness through 2026-07-12; not all U.S.
> research, a private project without NIH/DUC nexus or legal advice.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `SRC-0054-C02/C04/C05`; `NOT-OD-14-124` Sections II-III and compliance
> paragraph; `NOT-OD-25-081` Purpose; `NOT-OD-26-023` title and Purpose.
> **Basis / limits:** The documents state their mechanisms and proposal
> language. Applicability depends on funding, project, access and agreement facts.

## Research, data and actor scope

GDS covers NIH-supported generation of large-scale human and non-human genomic
data and subsequent research use, including named sequence, variant,
transcriptomic, metagenomic, epigenomic and expression classes. Responsibilities
are distributed among investigators, institutions, signing officials, IRBs or
equivalent bodies, funding Institutes/Centers, repositories, Data Access
Committees and approved secondary users. The AI notice is narrower: it concerns
approved users/developers and controlled-access human genomic/associated data,
not every class in the base policy.

> **Claim record — GOV-0026-C02 | source-report**
> **Claim:** NIH governance links genomic-data generation, institutional
> certification, repository submission, controlled access and secondary use,
> while the generative-AI clarification applies only inside the narrower
> controlled-human-data/approved-user boundary.
> **Claim status:** active
> **Scope:** Named NIH policy actors and data stages; not a repository topology,
> data-access decision, study census or finding about a named institution.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `SRC-0054-C02`-`C04`; `NOT-OD-14-124` Sections II, IV and V;
> `NOT-OD-25-081` Purpose.
> **Basis / limits:** Data classes, actors and stages are direct. The narrower
> AI scope cannot be generalized to all NIH or public genomic data.

## Requirements and control mappings

Covered projects require genomic-data-sharing planning, institutional
certification for human data, consent/data-use compatibility review, timely
submission and responsible secondary use under access terms. The AI notice
maps non-transferability to public generative-AI interfaces and treats trained
models/parameters as Data Derivatives. Until future guidance, NIH-approved
development may continue, but model sharing is limited to approved-user
collaborators and retention at project closeout is restricted.

These duties map defensively to access authorization, provenance, approved-use
limitation, approved-user collaboration, lifecycle retention/destruction and
model-release decision gates. The notices do not report a deployed technical control,
data-leakage incident, audit result or effectiveness measure.

> **Claim record — GOV-0026-C03 | source-report**
> **Claim:** NIH connects genomic research governance to the generative-AI-model lifecycle
> decisions through approval, non-transferability, derivative treatment,
> collaborator authorization and closeout destruction/retention boundaries.
> **Claim status:** active
> **Scope:** Policy and DUC expectations for covered actors; not a technical
> architecture, model-security guarantee, incident or evaluated safeguard.
> **As of:** AI notice released 2025-03-28; reviewed 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `SRC-0054-C03/C04`; `NOT-OD-25-081` Purpose bullets and interim paragraphs;
> `NOT-OD-14-124` Sections IV-V.
> **Basis / limits:** Requirements are direct. Their technical implementation
> and effectiveness are not observed.

## Exceptions and interpretation limits

Smaller studies are generally outside GDS but can fall under Institute/Center
or other programme expectations. Consent treatment differs for specimens and
cell lines created before and after the effective date. A funding Institute or
Center can assess compelling scientific reasons for specified unconsented
post-effective-date material and can grant a data-submission exception where
Institutional Certification criteria cannot be met. These are bounded review
paths, not unconditional waivers. The AI notice itself allows continued model
development only where NIH approved the use and preserves its stated sharing
and closeout restrictions.

> **Claim record — GOV-0026-C04 | source-report**
> **Claim:** NIH exceptions retain scale, date, consent, decision-maker and
> alternate-plan conditions; they do not create a general exemption from GDS,
> DUC non-transferability or other applicable requirements.
> **Claim status:** active
> **Scope:** Express policy qualifications; not approval of a project,
> exception, data release or model-sharing action.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `SRC-0054-C03/C04`; `NOT-OD-14-124` scope discussion, Sections IV.C.4-6;
> `NOT-OD-25-081` interim-development paragraph.
> **Basis / limits:** Each condition is direct and remains fact-specific.

## Proposal and currentness boundary

The later RFI proposes a harmonized Controlled-Access Data Policy and GDS
revisions, including scope, thresholds, consent and repository practices. Its
comment period ended 18 March 2026, but comment closure does not make the draft
operative. Within the retained package, current and proposed language remain
separate; a future final notice would require a new currentness review and
could change this page.

> **Claim record — GOV-0026-C05 | analytic-judgment**
> **Claim:** Proposed RFI provisions cannot fill current-policy requirements or
> exceptions until NIH issues a final instrument with an effective status;
> comment closure is an observed procedure event, not adoption.
> **Claim status:** active
> **Scope:** `NOT-OD-26-023` status through 2026-07-12; not prediction of its
> final content or a permanent assertion that no successor will issue.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `SRC-0054-C05`; `NOT-OD-26-023` title, Purpose, draft/proposed headings,
> Request for Input and response deadline.
> **Basis / limits:** Proposal status is explicit. Future final action remains
> an open currentness dependency.

## Implementation, independence and effectiveness boundary

Issuance, incorporation into award/contract terms and execution of a DUC are
normative/adoption mechanisms. The retained notices provide no recipient
implementation census, compliance audit, confirmed AI leakage event,
independent model test or causal effectiveness result. They are one NIH policy
lineage and require a materially independent jurisdictional lineage for a
two-jurisdiction governance reconciliation.

> **Claim record — GOV-0026-C06 | analytic-judgment**
> **Claim:** `GOV-0026` supplies one current U.S. NIH governance lineage with
> scope, force, exceptions and proposal status resolved, but not implementation
> or effectiveness evidence and not a second jurisdiction.
> **Claim status:** active
> **Scope:** Evidence maturity and source-count boundary; not a claim that NIH
> recipients do not comply.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `SRC-0054-C01/C06`; full retained policy lineage.
> **Basis / limits:** Conditional force is direct. Implementation and outcomes
> need separate award, repository, audit, incident or evaluation records.

## Cyberbiosecurity relevance and safety boundary

The policy connects genomic/associated research data, access decisions and
generative-AI model artifacts across a biomedical research lifecycle. This
page retains only public defensive governance. It contains no controlled data,
participant identity, model parameter, repository credential, access route or
re-identification procedure.

> **Claim record — GOV-0026-C07 | analytic-judgment**
> **Claim:** The governance representation supports defensive AI/genomics
> comparison without exposing controlled data or converting policy design into
> technical assurance, compliance or effectiveness claims.
> **Claim status:** active
> **Scope:** Local page; not a security assessment of NIH repositories,
> recipients or models.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `GOV-0026-C01`-`C06`; local content.
> **Basis / limits:** Only governance-level defensive content is represented.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0054 — NIH source package](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md)
- [GOV-0005 — U.S. data-security regulation](gov-0005-us-data-security-program-2025.md)
- [AST-0001 — genomic data](../assets/ast-0001-genomic-data.md)
- [AST-0008 — AI biological assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0005 — genomic lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [WFL-0011 — AI biological lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [CTL-0016 — provenance and validation controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)

## Sources

- [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md), at the exact notice-section locators above.
