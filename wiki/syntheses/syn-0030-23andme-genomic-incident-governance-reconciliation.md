---
id: SYN-0030
type: synthesis
title: 23andMe genomic incident, timeline and Canada–UK governance reconciliation
aliases:
  - 23andMe GEN THI GOV reconciliation
  - genomic privacy incident and breach-governance audit
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0055
  - SRC-0056
sensitivity: public
dual_use: low
relations:
  - predicate: depends-on
    target: SYN-0001
    claim_id: SYN-0030-C13
    evidence:
      - source: SRC-0055
        locator: "Frozen rubric v1.0 current rows and prior checkpoint SYN-0001-C45"
  - predicate: depends-on
    target: SYN-0028
    claim_id: SYN-0030-C04
    evidence:
      - source: SRC-0055
        locator: "SYN-0028-C09 conservative five-event lower bound before INC-0007"
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: SYN-0030-C02
    evidence:
      - source: SRC-0055
        locator: "Joint OPC/ICO report paragraphs 3–35, 47–200; UK penalty notice; SEC 8-K, 8-K/A and 2024 10-K exact locators"
  - predicate: evidenced-by
    target: SRC-0056
    claim_id: SYN-0030-C06
    evidence:
      - source: SRC-0056
        locator: "PIPEDA sections 4, 10.1–10.3 and 26; Canadian Regulations sections 2–6; current ICO guide anchored reporting/notification/record sections"
  - predicate: depends-on
    target: INC-0007
    claim_id: SYN-0030-C03
    evidence:
      - source: SRC-0055
        locator: "INC-0007-C01–C12; one event, full chronology, populations, consequences and limitations"
  - predicate: depends-on
    target: RSK-0020
    claim_id: SYN-0030-C03
    evidence:
      - source: SRC-0055
        locator: "RSK-0020-C01–C05; observed cyber-to-genomic-privacy path"
  - predicate: depends-on
    target: CTL-0022
    claim_id: SYN-0030-C09
    evidence:
      - source: SRC-0055
        locator: "CTL-0022-C01–C07; exact account, linked-profile, containment and notice edges"
  - predicate: governed-by
    target: GOV-0027
    claim_id: SYN-0030-C07
    evidence:
      - source: SRC-0055
        locator: "GOV-0027-C01–C09; one joint case, two jurisdictional applications and explicit evaluation limits"
tags:
  - genomics
  - incident
  - privacy
  - timeline
  - notification
  - enforcement
  - canada
  - united-kingdom
  - reconciliation
---

# 23andMe genomic incident, timeline and Canada–UK governance reconciliation

## Decision scope and frozen pre-state

This synthesis adjudicates only the cells directly affected by the new
documented genomic incident and current breach-governance package:
`GEN-CI`, `THI-WL/SD/CI/CT/AE/GR`, `CTR-CI`, and `GOV-CI/AE`. It does not reopen
unaffected passed
cells or relax their source floors. Page count, two Commissioners, three SEC
filings and several affected populations are not multiplied into independent
events, investigations or deployments.

`SYN-0030-C01` is superseded because its pre-state included rubric units later
retired from the public corpus.

> **Claim record — SYN-0030-C13 | artifact-observation**
> **Claim:** Before this transaction the recalculated public wiki has 86 Pass,
> 21 Partial, and 3 Absent cells, or 86/110 (78.2%), with dimension vector
> `10/8/5/8/8/8/10/10/3/8/8`, critical cells 73/17/1, three dimensions at
> least 9/10, and global gates at 7 Pass/5 Fail.
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), recalculated checkpoint
> `SYN-0001-C45`; [SYN-0029](syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md);
> [SYN-0028](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md),
> `SYN-0028-C14`–`C17`.
> **Limits:** This is public-corpus checkpoint arithmetic, not absolute domain
> completeness.

## Evidence roles, lineages and non-duplication

| Evidence role | Canonical lineage | Counting boundary |
| --- | --- | --- |
| company disclosure | original 8-K, 8-K/A and 2024 10-K | one evolving 23andMe issuer lineage |
| independent case reconstruction | joint OPC/ICO findings | one joint investigation; two national legal applications |
| UK sanction output | penalty notice and current enforcement record | derivative of the joint investigation, not another investigation |
| current Canadian rules | PIPEDA and Canadian Regulations | one Canadian official-law package |
| current UK rules | current ICO UK-GDPR guide | independent UK regulator guidance; not itself legislation |
| canonical event | `INC-0007` | one event despite direct and linked populations |

> **Claim record — SYN-0030-C02 | analytic-judgment**
> **Claim:** Two material event-evidence lineages are available—one first-
> party SEC lineage and one independent joint regulatory investigation—while
> Canada and the UK independently supply current national rule frames; no
> filing, regulator output, jurisdiction or affected-population row is counted
> as an additional event or investigation.
> **Claim status:** active
> **Scope:** Claim-specific SF2/SF3 lineage accounting; not equal source
> weight, independent reconstruction of every count or two tested deployments.
> **As of:** Full package reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C01/C02/C06`; [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C01/C06`–`C10`; [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md),
> `INC-0007-C01/C07/C11`.
> **Basis / limits:** Issuers, genres and evidence-production roles are direct.
> Regulators lacked some privileged records and did not independently verify
> the final revised raw-DNA figure.

## Genomic downstream consequence — `GEN-CI`

The accepted observed path is:

`credential-based account compromise → direct account and linked-relative
profile access → unauthorized copying/online offering of heterogeneous
identity, ancestry, health/genetic and relationship information → documented
privacy, identity, kinship, legal and financial consequence`

This is not a biological alteration or clinical outcome. It is nevertheless a
downstream privacy outcome involving human genomic/relative information, one
of the four outcome classes literally accepted by `GEN-CI`.

> **Claim record — SYN-0030-C03 | analytic-judgment**
> **Claim:** `GEN-CI` passes at SF3: `INC-0007/RSK-0020` document an observed
> downstream genomic privacy/identity/kinship consequence in a primary company
> case record, with materially independent joint-regulator reconstruction,
> enforcement and methodological limitations.
> **Claim status:** active
> **Scope:** One consumer-genetics incident and privacy outcome; not a clinical,
> research-validity or biological effect, universal genomics risk or safeguard
> effectiveness result.
> **As of:** Event 2023; regulatory record through 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md),
> `INC-0007-C01/C03`–`C07/C11`; [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md),
> `RSK-0020-C01`–`C04`; `SRC-0055-C03`–`C06/C10/C11`.
> **Basis / limits:** Unauthorized access/copying, online offering, affected
> asset classes and legal/accounting consequences are direct. Individual harm
> rates and biological/clinical effects are not measured.

## Incident lifecycle and corpus — `THI-WL/CI`

### Six-event conservative lower bound

The prior five public INC/review pages support five distinguishable events.
`INC-0007` is unrelated in organization, date, sector, evidence, and affected
population. The conservative six-event set is:

1. Synnovis transfusion disruption (`INC-0001`, LAB);
2. the national clinical review and fatal-outcome account (`INC-0003`, CPH);
3. JBS processing disruption (`INC-0004`, AGE);
4. anonymous chicken-farm control/animal-effect account (`INC-0005`, AGE);
5. Merck manufacturing/supply disruption (`INC-0006`, BMO); and
6. 23andMe genomic privacy breach (`INC-0007`, GEN).

> **Claim record — SYN-0030-C04 | analytic-judgment**
> **Claim:** `THI-WL` passes at SF3: six canonical public INC/review pages now
> support a conservative lower bound of six distinguishable primary-supported
> events, and every counted page separates event, discovery, disclosure,
> response and recovery/remediation states or explicitly records them unknown.
> **Claim status:** active
> **Scope:** Six-event lower bound, not seven distinct events, complete
> forensics, equal timeline precision or known recovery for every event.
> **As of:** Corpus 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0028](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md),
> `SYN-0028-C09`; `INC-0001/0003/0004/0005/0006/0007`
> timeline/evidence sections;
> `INC-0007-C01/C02/C08`.
> **Basis / limits:** 23andMe is provably separate from every prior branch.
> Aggregate report units are not multiplied into events.

> **Claim record — SYN-0030-C05 | analytic-judgment**
> **Claim:** `THI-CI` and the global incident gate pass at SF3: the conservative
> six-event corpus spans LAB, CPH, AGE, BMO and GEN across more than four
> independent lineages/sectors and retains multiple evidenced patient, animal,
> processing/product-supply and privacy outcomes, with evidence grades and
> event-identity limits explicit.
> **Claim status:** active
> **Scope:** Frozen incident floor; not six biological injuries, equal event
> assurance, representative incidence or proof every event has independent
> outcome measurement.
> **As of:** 2026-07-12 corpus.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0028-C09`; `INC-0001/0003/0004/0005/0006/0007`;
> [SYN-0015](syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md),
> `SYN-0015-C03/C12`;
> [SYN-0025](syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md);
> `INC-0006-C04`–`C06`; `INC-0007-C06`.
> **Basis / limits:** Count, sectors and at least two biological/clinical/
> product/ecological outcomes were already one event short; the independent
> genomic event closes count without being mislabeled biological harm.

## Current incident governance — `THI-GR`

| Governance function | Canada | United Kingdom | Safe reconciliation |
| --- | --- | --- | --- |
| regulator report | real risk of significant harm; as soon as feasible | likely risk; without undue delay and within 72 hours where feasible | timing and thresholds remain distinct |
| affected-person notice | same Canadian harm threshold; direct unless prescribed route/other-law qualifier | likely high risk; without undue delay | content/route differences preserved |
| preservation | every breach record; 24 months after determination | every breach record; no duration in retained guide | breach accountability, not forensic chain of custody |
| attribution | cause only if known in Canadian report | no actor field in retained minimum-content checklist | known actor is not a reporting prerequisite |

> **Claim record — SYN-0030-C06 | analytic-judgment**
> **Claim:** `THI-GR` passes at SF2: independent current Canadian law and UK
> regulator guidance reconcile reporting, affected-person notification,
> breach-record preservation and attribution-governance rules while preserving
> different thresholds, timing, force, scope, exceptions and missing detail.
> **Claim status:** active
> **Scope:** Federal Canadian private-sector and represented UK-GDPR duties;
> not all Canadian provinces, UK sectoral branches, forensic evidence custody,
> legal advice or a merged deadline.
> **As of:** Canada current to 2026-05-26; UK guide checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C02`–`C10`; [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md),
> `GOV-0027-C02/C07`; 23andMe joint findings footnote 13 and paragraphs
> 118–187 for application despite attribution uncertainty.
> **Basis / limits:** All four governance functions have direct national
> support. UK guidance omits a record duration and full Article 34(3)
> exceptions; those absences remain explicit.

## Governance case and implementation evaluation — `GOV-CI/AE`

### Obligations operating in practice

> **Claim record — SYN-0030-C07 | analytic-judgment**
> **Claim:** `GOV-CI` passes at SF3: 23andMe adds an actual multi-jurisdiction
> regulator/enforcement case applying safeguard, threshold, timing, content,
> remediation and penalty duties, while the separate national patient-safety
> review retains its prospective-action role rather than being inflated into
> privacy enforcement.
> **Claim status:** active
> **Scope:** Public case corpus showing governance operation; not a general
> compliance precedent, two 23andMe investigations, or a claim that prior
> official records independently replicate privacy enforcement.
> **As of:** Cases through 2025; currentness checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md),
> `GOV-0027-C01`–`C07`;
> [INC-0003](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md);
> `SRC-0055-C07/C08/C10`.
> **Basis / limits:** 23andMe directly supplies enforcement and two legal
> applications. The prior national review supplies a different governance-
> operation context, not an extra 23andMe event or implementation test.

### Two-jurisdiction implementation evaluation

The same factual implementation was legitimately evaluated twice in the
jurisdictional—not investigative—sense: OPC applied PIPEDA to Canadian people
and reached Canadian findings; ICO applied UK GDPR to UK people and reached UK
findings/penalty. Shared fact-gathering prevents counting two investigations,
but it does not erase two legal implementation evaluations demanded by the
literal `GOV-AE` criterion.

> **Claim record — SYN-0030-C08 | analytic-judgment**
> **Claim:** `GOV-AE` passes narrowly at SF3: one joint investigation evaluated
> actual authentication, monitoring, response and notification implementation
> on one global platform separately under Canadian PIPEDA and UK GDPR, reached
> jurisdiction-specific findings and assessed remediation, with material
> method and effectiveness limitations reported.
> **Claim status:** active
> **Scope:** Two jurisdictional implementation evaluations in one case; not
> two independent investigations/deployments, control certification, causal
> effectiveness or generalization to consumer genetics.
> **As of:** Implementation 2023–2024; evaluation 2025.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** `GOV-0027-C03`–`C08`; joint report paragraphs 15–19,
> 112–117, 149–200 and 201; penalty notice paragraph 11; `SRC-0055-C09`.
> **Basis / limits:** Actual controls and separate legal conclusions are
> direct. Implementation information was largely company-supplied, privileged
> records were unavailable, revised raw-DNA counts were unverified, and no
> independent outcome/effectiveness comparator exists.

## Control/taxonomy contribution and nonpromotions

> **Claim record — SYN-0030-C09 | analytic-judgment**
> **Claim:** `THR-0004/TEC-0004/VUL-0005/CTL-0022` preserve actor, method,
> actual weakness, event, consequence and recommended/implemented/evaluated
> control states with exact edges, but create no transition for `GEN-AE`,
> `THI-XT`, `CTR-AE` or any sector assurance cell.
> **Claim status:** active
> **Scope:** Nonpromotion and graph-semantics audit; no reopening of already
> passed taxonomy/control cells.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [THR-0004](../threats/thr-0004-credential-based-genetic-data-access.md);
> [TEC-0004](../techniques/tec-0004-credential-stuffing-and-linked-profile-scraping.md);
> [VUL-0005](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md);
> [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md),
> `CTL-0022-C01`–`C07`; frozen criteria.
> **Basis / limits:** Case-derived implementation and regulatory resolution
> are not independent harm-reduction effectiveness. No input/material→digital-
> decision incident is added.

## Accepted transitions and resulting state

> **Claim record — SYN-0030-C14 | analytic-judgment**
> **Claim:** The 23andMe incident restores the public-corpus floors for
> `THI-SD`, `THI-CT`, `THI-AE`, and `CTR-CI`: it provides the fourth
> incident-specific technical dependency case, the fourth exact control-lesson
> lineage, and a joint regulator investigation independent of the separately
> retained Kroll investigation.
> **Evidence:** `SYN-0028-C14/C15`; [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md),
> `INC-0007-C01/C03/C07/C11`; [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md),
> `CTL-0022-C01`–`C07`; `SYN-0030-C02`; `GOV-0027-C01`–`C08`.
> **Limits:** The joint OPC/ICO work counts as one investigation, the Kroll
> report remains unavailable, control implementation is not effectiveness,
> and no affected-population row is an additional event or evaluator.

`SYN-0030-C10` is superseded because its pre-state did not reflect the public
privacy retirement and therefore omitted four transitions restored here.

> **Claim record — SYN-0030-C15 | artifact-observation**
> **Claim:** Exactly ten Partial→Pass transitions are supported:
> `GEN-CI`, `THI-WL/SD/CI/CT/AE/GR`, `CTR-CI`, and `GOV-CI/AE`. Totals
> become 96 Pass, 11 Partial, and 3 Absent, or 96/110 (87.3%), with vector
> `10/9/5/8/8/8/10/10/9/9/10`, critical cells 82/8/1, and seven
> dimensions at least 9/10.
> **Evidence:** `SYN-0030-C02`–`C09` and `C13/C14`; exact frozen criteria and
> SF2/SF3 floors in [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** Partial and Absent earn zero. The clinical consequence cell
> remains Partial and this checkpoint is not ≥90% certification.

> **Claim record — SYN-0030-C11 | analytic-judgment**
> **Claim:** The global incident gate changes Fail→Pass because `THI-CI`
> passes; global gates become 8 Pass/4 Fail, while numeric, risk-chain,
> directionality and controls gates remain Fail and every other gate remains
> unchanged.
> **Claim status:** active
> **Scope:** Global gate state after this transaction; not final certification.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0030-C05/C09/C14/C15`; frozen twelve global gates in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** The transaction does not supply a complete per-sector
> risk chain, material/input→digital incident or independently effective
> control family and remains below the numeric threshold.

## Remaining gaps and safety

After activation, the remaining critical gaps are `SEB-WL/TV/CI/GR`,
`LAB-TV`, `BMO-SD`, `CPH-CI`, `THI-XT`, and `CTR-AE`. Passing those nine cells is the
minimum route to satisfy every critical cell and all dimension floors; with
the current six-event lifecycle transition included, that floor is 105/110,
not merely the nominal 99/110 threshold. Noncritical assurance gaps remain in
`GEN-AE`, `SEB-AE`, `LAB-AE`, `BMO-AE` and `CPH-AE`.

> **Claim record — SYN-0030-C12 | analytic-judgment**
> **Claim:** The transaction remains defensive and privacy-preserving: it
> exposes no credentials, personal/genetic records, endpoint, request pattern,
> automation/evasion, re-identification or harmful-production procedure, and
> it keeps privacy consequence separate from biological/clinical harm.
> **Claim status:** active
> **Scope:** Transaction content and safety boundary; not a legal or security
> assessment of the current service.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C11`; `INC-0007-C06/C12`; `RSK-0020-C04`;
> `THR-0004/TEC-0004/VUL-0005/CTL-0022` safety boundaries.
> **Basis / limits:** All operational and personal-data detail is excluded;
> public counts, legal findings and defensive control classes suffice.

## Related pages

- [SYN-0001 — Frozen rubric](syn-0001-coverage-rubric.md)
- [SYN-0028 — Prior incident-count reconciliation](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)
- [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md)
- [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md)
- [INC-0007](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [RSK-0020](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [CTL-0022](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md)
