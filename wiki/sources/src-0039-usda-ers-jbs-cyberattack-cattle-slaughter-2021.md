---
id: SRC-0039
type: source
title: USDA ERS JBS cyberattack and cattle-slaughter disruption record, June 2021
aliases:
  - Livestock Dairy and Poultry Outlook June 2021
  - LDP-M-324 JBS cyberattack section
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-12
source_type: official-us-federal-economic-outlook-report
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/usda-ers-livestock-dairy-poultry-outlook-june-2021.pdf
sha256: c2060914931c4d474828bcbc0affc997c2cd8597b2d1380b8080f4079d5e8585
raw_components:
  - path: ../../raw/usda-ers-livestock-dairy-poultry-outlook-june-2021-current-2026-07-12.html
    role: current-official-publication-landing-page
    sha256: 49e3dd1d027c0eccdda824dfcdc665bc0bd5972db96b6955790b24c75116b7f5
canonical_url: https://www.ers.usda.gov/publications/101459
current_pdf_url: https://www.ers.usda.gov/media/10354/ldp-m-324.pdf
acquired_from_url: https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/101460/LDP-M-324.pdf?v=47722
accessed: 2026-07-12
published: 2021-06-16
report_number: LDP-M-324
issuer: United States Department of Agriculture, Economic Research Service
beef_section_authors:
  - Russell Knight
  - Christopher G. Davis
jurisdictions:
  - United States
tags:
  - agriculture
  - food-processing
  - cattle-slaughter
  - cyberattack
  - jbs
  - economic-data
  - incident-consequence
---

# USDA ERS JBS cyberattack and cattle-slaughter disruption record, June 2021

## Identity, acquisition and complete review

The retained primary artifact is the 28-page USDA Economic Research Service
*Livestock, Dairy, and Poultry Outlook: June 2021*, report `LDP-M-324`,
published 16 June 2021. The JBS record appears in the Beef/Cattle summary on
PDF p. 2 and in the section by Russell Knight and Christopher Davis on PDF
p. 3. The official publication landing page still identifies the report,
date, author group, report number and complete PDF on 2026-07-12.

- The official PDF is 1,314,705 bytes; repeat retrieval from the acquisition
  URL and a fresh retrieval from the current landing-linked `/media/10354/`
  URL were byte-identical.
- The retained official landing HTML is 43,258 bytes. Together the two objects
  total 1,357,963 bytes.
- All 28 pages and all text, tables, charts, notes, source labels, forecast
  tables and legal/publication notices were reviewed. `pdfimages` found no
  embedded raster images; the relevant vector/text table was also rendered and
  visually checked against extracted text.
- The PDF is tagged, unencrypted PDF 1.5 with an AcroForm, no JavaScript and no
  embedded files. `pdfsig` reports no signatures and emitted an NSS-
  initialisation warning, so no cryptographic-authentication claim is made.
- Static inspection of the landing page found 14 script and one form elements
  and no iframe/object/embed. Nothing was executed or submitted; this is not
  runtime assurance. A fresh landing retrieval was four bytes longer and
  differed only in dynamic/cosmetic canonical-host, CSP-nonce and cache-buster
  fields; publication identity and substantive presentation remained
  unchanged.

> **Claim record — SRC-0039-C01 | artifact-observation**
> **Claim:** The retained 1,357,963-byte package contains the complete official
> 28-page USDA ERS report and current official landing snapshot, with hashes,
> repeat-retrieval identity, complete-review state and format/safety limits
> recorded.
> **Claim status:** active
> **Scope:** Retained artifacts and review process; not cryptographic
> authentication, runtime assurance or independent replication of report data.
> **As of:** Report 2021-06-16; artifacts reviewed 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Two raw objects and hashes above; PDF pp. 1–28; official
> landing metadata and download entry.
> **Basis / limits:** Object identity, full text and table rendering are
> reproducible. The landing page is a current companion from the same USDA ERS
> publication lineage, not an independent source.

## Publication role and method

`LDP-M-324` is a federal sector outlook, not a cyber-investigation report or a
JBS first-party disclosure. Its overall purpose is livestock, dairy and poultry
economic analysis. For the JBS subsection, ERS states that it compares actual
and estimated daily cattle-slaughter data from USDA's Agricultural Marketing
Service across Memorial Day weeks from 2018 through 2021. The subsection also
warns that very little slaughter normally occurs on Memorial Day and that
Saturday slaughter is commonly elevated to compensate within a holiday week.

> **Claim record — SRC-0039-C02 | source-report**
> **Claim:** USDA ERS places the JBS event inside an official livestock-market
> outlook and uses AMS actual-and-estimated daily cattle-slaughter observations
> plus prior Memorial Day weeks as quantitative context.
> **Claim status:** active
> **Scope:** Report role, stated data source and comparator method; not a cyber
> forensic method, final microdata audit or causal counterfactual estimate.
> **As of:** 2021-06-16.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 3, `Beef Production Was Disrupted Temporarily Due to a
> Cyberattack`, narrative and table source note; landing-page overview.
> **Basis / limits:** Issuer, method and source label are direct. The report
> does not distinguish which daily values were actual versus estimated or
> publish underlying case-level data here.

## Event, closure and restoration timing

ERS reports that JBS Foods was the victim of a cyberattack on Sunday 30 May
2021, that nine U.S. plants were closed on Tuesday 1 June, and that the
facilities were fully operational by Thursday 3 June. Its summary characterizes
the cattle-slaughter disruption as lasting two days.

> **Claim record — SRC-0039-C03 | source-report**
> **Claim:** USDA ERS reports a cyberattack→nine-U.S.-plant closure→two-day
> cattle-slaughter disruption→facilities-fully-operational-by-3-June sequence.
> **Claim status:** active
> **Scope:** Source-reported JBS event, operational state and dates; not
> ransomware classification, actor attribution, initial-access vector,
> affected-system topology, restoration test or independent cyber forensics.
> **As of:** Event 2021-05-30 through 2021-06-03.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 2, Beef/Cattle summary; p. 3, first paragraph of the JBS
> subsection.
> **Basis / limits:** The sequence and two-day characterization are direct ERS
> reporting. `Fully operational` is an operational statement, not proof of
> clean, validated or independently tested cyber recovery.

## Measured cattle-slaughter context

The report's Memorial Day-week table gives daily values in thousand head. For
2021 it reports 2.0 Monday, 94.0 Tuesday, 105.0 Wednesday, 120.0 Thursday,
119.0 Friday and 98.0 Saturday, totaling 538.0. Corresponding totals were
584.7 in 2018, 588.1 in 2019 and 527.1 in 2020. ERS summarizes the event week
as above 2020 but well below 2019.

> **Claim record — SRC-0039-C04 | source-report**
> **Claim:** USDA's table supplies a measured/estimated food-processing
> throughput
> context for the cyber event: 2021 Tuesday/Wednesday cattle-slaughter values
> below the 2019/2020 comparator values, a Thursday value of 120.0 thousand
> head, and a 538.0-thousand-head week above 2020 but below 2018/2019 Memorial
> Day-week totals.
> **Claim status:** active
> **Scope:** Reported federally inspected cattle-slaughter series for selected
> holiday weeks; not animals injured, meat shortage, revenue loss, price
> effect, discarded product or a cyber-only causal effect size.
> **As of:** Memorial Day week 2021, report published 2021-06-16.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 3, `Cattle slaughter the week of Memorial Day, 2018–21`
> table and accompanying paragraph; PDF p. 2 summary.
> **Basis / limits:** Table values and the report's qualitative comparison are
> direct. `Actual and estimated` status, holiday timing and compensating
> Saturday production prevent a clean causal or loss estimate.

## Counterfactual and consequence limits

The four Memorial Day weeks are contextual comparators, not a controlled
experiment. 2020 had pandemic-related closures/slowdowns, the 2021 holiday fell
a week later than in the prior year, and slaughter may shift to Saturday. The
report does not provide plant-level data, expected-without-attack values, meat
output, supply-shortage measurements or financial loss.

> **Claim record — SRC-0039-C05 | analytic-judgment**
> **Claim:** `SRC-0039` directly supports an observed temporary cattle-
> processing/slaughter consequence with numeric context, but it does not
> identify the cyberattack's isolated causal effect or a downstream food,
> animal-welfare, price, revenue or consumer outcome.
> **Claim status:** active
> **Scope:** Evidence-maturity interpretation of the ERS event subsection.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0039-C02`–`C04`; PDF pp. 2–3.
> **Basis / limits:** The report directly connects attack, closure and temporary
> slaughter disruption. It does not publish the counterfactual or broader
> consequence measurements needed for stronger causal/economic claims.

## Price and production-forecast non-attribution

The next p. 3 subsection says high cow-slaughter numbers and persistent drought
conditions drove changes that raised the annual beef-production forecast by 5
million pounds. On p. 4, ERS ties fed-steer forecast increases to current price
data and strong wholesale beef prices. Those passages do not attribute either
forecast change or the displayed prices to the JBS cyberattack.

> **Claim record — SRC-0039-C06 | source-report**
> **Claim:** The report does not support attributing its annual beef-production
> forecast increase, fed-steer price forecast changes or displayed wholesale
> prices to the JBS cyberattack; it gives other stated bases for those changes.
> **Claim status:** active
> **Scope:** Causal-reading boundary for adjacent Beef/Cattle subsections; not a
> finding that the attack had no price or economic effect.
> **As of:** 2021-06-16.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 3, `2021 Beef Production Raised Slightly...`; p. 4,
> `Fed Steer Price Estimates Rise...`; complete-report cyber-term search.
> **Basis / limits:** The stated forecast rationales are direct and the
> complete report mentions the cyberattack only in the summary and JBS
> subsection. Absence of attribution is not evidence of zero effect.

## Cyber-evidence and independence boundary

ERS calls the event a `cyberattack` but supplies no ransomware classification,
actor, vector, vulnerability, system type, ransom/payment, investigation or
technical-response detail. It is materially distinct in institutional role and
data basis from a law-enforcement attribution statement, but the two sources
will still describe one event and must not be counted as two incidents.

> **Claim record — SRC-0039-C07 | artifact-observation**
> **Claim:** Complete review finds no source support for ransomware, actor,
> vector, vulnerability or affected IT/OT-system or system-topology assertions;
> `SRC-0039` contributes official economic/processing context rather than
> technical attribution.
> **Claim status:** active
> **Scope:** Complete 28-page retained report; not a claim that technical facts
> were unknown outside this source.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF pp. 1–28; cyber/JBS term locations at pp. 2–3 only.
> **Basis / limits:** Full-text and visual review support the absence boundary.
> A separate primary FBI record is required for source-appropriate attribution.

## Rubric contribution and score boundary

The report is a direct official record of a temporary cyber-associated food-
processing consequence with a slaughter-throughput metric and recovery timing.
It therefore
strengthened the candidate for `AGE-CI` and one agriculture incident role at
the source-transaction checkpoint. It did not by itself meet SF3; the later
independent incident-context and criterion reconciliation are in `SYN-0025`.

> **Claim record — SRC-0039-C08 | analytic-judgment**
> **Claim:** `SRC-0039` supplies direct candidate evidence for `AGE-CI`—an
> observed cattle-slaughter/food-processing-throughput consequence with
> numeric context—but alone changes no frozen cell or global gate.
> **Claim status:** superseded
> **Scope:** Wiki after one USDA source transaction; no incident page, score
> transition or conclusion about `AGE-AE`/control effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0039-C02`–`C07`; `AGE-CI` criterion and SF3 floor in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Observed slaughter/processing throughput and dates are
> direct. One ERS
> lineage lacks independent confirmation and does not establish actor/vector,
> food shortage, biological injury, causal loss magnitude or effectiveness.
> **Superseded by:** `SYN-0025-C06`, after bounded canonical-event and
> independent incident-context reconciliation.

> **Claim record — SRC-0039-C09 | analytic-judgment**
> **Claim:** The page remains defensive and contains no indicators, malicious-
> software detail, affected-system topology, credentials, exploit information
> or operational response procedure.
> **Claim status:** active
> **Scope:** Local page content, not the complete public raw artifact.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content compared with the complete report.
> **Basis / limits:** Only event/consequence and evidence-quality information
> needed for defensive reasoning is retained.

## Limitations and conflicts

- ERS is an official sector-economic source, not the victim, a court record or
  cyber-forensic investigator.
- The report does not state the source of its plant-closure/restoration facts.
- AMS values are described collectively as actual and estimated; final/micro
  data and uncertainty are not supplied in the subsection.
- Memorial Day timing, compensating Saturday work and the abnormal 2020
  comparator limit causal inference.
- No animal injury, food shortage, spoilage, price/revenue loss or consumer
  outcome is documented.
- `Fully operational` is not trusted-recovery or effectiveness evidence.

## Integration map

- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)
- [INC-0004](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
