---
id: TEC-0001
type: technique
title: Biological input propagated into downstream digital parsing
aliases:
  - material to parser cross-domain transfer
  - sequenced biological input as software input
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0014
sensitivity: public
dual_use: moderate
technique_kind: cross-domain-input-propagation
relations:
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: TEC-0001-C01
    evidence:
      - source: SRC-0014
        locator: "Introduction and §3, printed pp. 765–771 (PDF pp. 2–8)"
  - predicate: exploits
    target: VUL-0001
    claim_id: TEC-0001-C02
    evidence:
      - source: SRC-0014
        locator: "§§3 and 6, printed pp. 768–776 (PDF pp. 5–13)"
  - predicate: enables
    target: RSK-0009
    claim_id: TEC-0001-C02
    evidence:
      - source: SRC-0014
        locator: "Introduction and §3, printed pp. 765–771 (PDF pp. 2–8)"
tags:
  - genomics
  - sequencing
  - bioinformatics
  - cross-domain-transfer
  - biological-to-digital
  - defensive-abstraction
---

# Biological input propagated into downstream digital parsing

## Method boundary

This page captures a high-level transfer method, not an exploit recipe:

`physical biological/synthetic input → sequencing/measurement → digital reads
→ downstream parser or analysis utility`.

If the resulting digital representation reaches compatible unsafe input
handling, software state can be affected. The method is relevant to defensive
trust-boundary design regardless of whether the originating material is
ordinary, erroneous or intentionally adversarial.

> **Claim record — TEC-0001-C01 | source-report**
> **Claim:** Ney et al. experimentally propagated a physical synthetic-DNA
> input through sequencing into downstream digital processing and observed code
> execution in their deliberately weakened target setup.
> **Claim status:** active
> **Scope:** Controlled proof of concept; not a field technique observation,
> current exploitability conclusion or production reliability estimate.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction and §3, printed pp. 765–771 (PDF pp. 2–8).
> **Basis / limits:** Cross-domain stages and outcome are direct. Target
> modification, weakened defenses and run fragility sharply bound the finding.

## Relationship to threat, weakness and scenario

- [THR-0001](../threats/thr-0001-adversarial-sequencing-input.md) supplies the
  intentional threat context; the technique itself is the transfer method.
- [VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md)
  supplies the compatible weakness class.
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
  records the full controlled consequence path.

> **Claim record — TEC-0001-C02 | analytic-judgment**
> **Claim:** `TEC-0001` can exploit unsafe downstream input handling and enable
> `RSK-0009` only when material provenance, digital transformation, parser reach
> and a compatible weakness align; the source does not establish this alignment
> in operational systems.
> **Claim status:** active
> **Scope:** Defensive cross-domain mechanism at non-operational abstraction.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§3 and 6, printed pp. 768–776 (PDF pp. 5–13).
> **Basis / limits:** The PoC joins the transfer to an intentionally introduced
> weakness, while the audit shows only version-bounded weakness indicators and
> controlled crashes elsewhere. No field exploit or current exposure follows.

## Defensive observations

Trust decisions should consider the physical input, its provenance, the
measurement transformation, the derived files, downstream software and
isolation/recovery boundary as one chain. Merely protecting a file-upload edge
does not address every possible material-origin path; merely controlling a
sample does not establish safe parsing.

## Safety boundary

No sequence, encoding, payload, source code, target-specific weakness,
construction step, adaptation or infrastructure detail is reproduced. The
page supports architecture and control mapping, not operational use.

## Related pages

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [THR-0001](../threats/thr-0001-adversarial-sequencing-input.md)
- [VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md)
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
- [CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md)

## Sources

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
  Introduction, §§3 and 6.
