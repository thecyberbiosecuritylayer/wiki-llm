# Maintainers

This file records project authority and operating responsibility. It is not
factual evidence for the wiki.

## Maintainer of record

[`@thecyberbiosecuritylayer`](https://github.com/thecyberbiosecuritylayer) is
currently the sole maintainer and community moderator.

The maintainer is responsible for:

- evidence-integration and stable-ID decisions;
- privacy, sensitivity, dual-use, and redistribution-rights decisions;
- pull-request review, merges, repository settings, and moderation;
- authorization of raw acquisition or archival; and
- knowledge-base and evidence-bundle releases.

## Decision model

Editorial decisions are based on evidence quality rather than simple vote
counts. They favor primary sources, traceable locators, scoped claims, visible
uncertainty, and small reviewable changes. Unresolved questions remain open
rather than being filled with a plausible guess.

While there is one maintainer, self-merge is permitted after the complete
quality gate passes and the diff has been reviewed against its cited sources.
A passing CI check is necessary but is not independent review. Sensitive
reports and moderation decisions use the private route in
[`SECURITY.md`](SECURITY.md).

The sole maintainer is also the current moderator and controls that private
GitHub route. The project therefore does not yet offer an independent
escalation channel for a complaint about the maintainer. Do not publish
confidential details to work around this limitation; it should be resolved when
a second trusted moderator or a real independent private contact becomes
available.

LLMs and automation may research, edit, and validate within an authorized task
under [`AGENTS.md`](AGENTS.md). They cannot authorize a release, raw archival,
a sensitivity downgrade, or external communication on the project's behalf.

## Adding maintainers

Maintainer access requires sustained contributions and demonstrated judgment
about evidence, privacy, rights, and dual-use boundaries. A change in authority
is recorded through a pull request that updates this file.

When a second trusted maintainer is active, the project should add a
`CODEOWNERS` file and require one approving review for protected-branch changes.
Requiring an approval before a second trusted reviewer exists would prevent the
sole maintainer from merging pull requests.

Maintenance and moderation are best-effort; the project does not promise a
response-time service level.
