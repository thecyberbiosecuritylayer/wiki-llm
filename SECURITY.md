# Security and sensitive-content reporting

This project is a public-source knowledge base, not a production software
service. Security reports still matter when publication could expose people,
biological capabilities, credentials, source boundaries, or repository users.

## Report privately

Do **not** open a public issue or pull request for a sensitive report. GitHub
Private Vulnerability Reporting is enabled for this repository. Use
[Report a vulnerability](https://github.com/thecyberbiosecuritylayer/wiki-llm/security/advisories/new).

Include only the detail needed to locate and assess the problem. If that button
is not available, do not place sensitive details in an issue or pull request.
Withhold the details until a private route is available.

Use the private route for:

- personal, clinical, genomic, participant, or employee information;
- a combination of public details that could re-identify a person or sensitive
  facility;
- an undisclosed high-impact vulnerability or sensitive biological capability;
- harmful sequence information, deployable exploit detail, screening evasion,
  or a novel operational attack chain;
- committed credentials, tokens, private keys, internal paths, or confidential
  metadata; and
- flaws in repository tooling that could execute untrusted content, escape an
  expected boundary, corrupt evidence, or expose local raw artifacts.

For an apparent vulnerability in a third-party product or organization, first
use that party's responsible-disclosure channel. Tell this project privately
only what is necessary to identify material that should be withheld, corrected,
or removed from the wiki.

Ordinary factual disagreements, incomplete citations, and broken links are not
security reports. Use the evidence-correction issue form for them unless the
correction itself contains sensitive information.

## What to include

- the affected file, page ID, claim ID, or tool;
- the type and plausible impact of the exposure;
- minimal reproduction or re-identification conditions;
- whether the information is already public and where; and
- a safe way to verify the issue without redistributing sensitive content.

Do not attach restricted source material, personal data, harmful sequences,
credentials, or weaponizable proof-of-concept content.

## Handling

Maintainers will assess the report privately, preserve evidence only within an
appropriate boundary, and remove or abstract public detail when warranted.
They may coordinate with an affected source owner, vendor, institution, or
authority when responsible disclosure requires it. No bug bounty or guaranteed
response time is offered.

Security support applies to the current default branch. Corrections are applied
there and recorded in the next knowledge release. Published snapshots are not
silently rewritten. If a release itself creates a privacy or safety exposure,
maintainers may seek GitHub-assisted containment or removal and publish a
documented superseding record. Privacy and safety take precedence over
historical availability.
