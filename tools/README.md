# Repository quality gate

Run the complete local publication check from the repository root:

```sh
python3 tools/check.py
```

The checker has no third-party dependencies. It validates text hygiene,
frontmatter and stable identities, public-sensitivity boundaries, claim IDs,
relation ownership and targets, the ID registry, relative Markdown links,
English-only Markdown, the binary-free public raw boundary, and the release
artifact manifest against the `SRC` hash bindings. It intentionally does not
make network requests or download release assets; external URLs and released
bytes are reviewed separately so transient publisher failures do not block
every pull request.

The validator and workflow are licensed under the [MIT License](LICENSE).
