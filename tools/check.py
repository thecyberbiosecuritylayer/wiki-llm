#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run the publication checks for the Markdown-first wiki.

The checker deliberately uses only the Python standard library. It validates
the public Git boundary, not every ignored artifact in the local raw archive.
"""

from __future__ import annotations

import posixpath
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

TYPE_LAYOUT = {
    "source": ("SRC", "sources"),
    "concept": ("CON", "concepts"),
    "asset": ("AST", "assets"),
    "system": ("SYS", "systems"),
    "workflow": ("WFL", "workflows"),
    "threat": ("THR", "threats"),
    "hazard": ("HAZ", "hazards"),
    "technique": ("TEC", "techniques"),
    "vulnerability": ("VUL", "vulnerabilities"),
    "risk-scenario": ("RSK", "risk-scenarios"),
    "control": ("CTL", "controls"),
    "incident": ("INC", "incidents"),
    "organization": ("ORG", "organizations"),
    "governance": ("GOV", "governance"),
    "synthesis": ("SYN", "syntheses"),
    "question": ("QUE", "questions"),
}
PREFIXES = tuple(prefix for prefix, _ in TYPE_LAYOUT.values())
ID_RE = re.compile(rf"(?:{'|'.join(PREFIXES)})-[0-9]{{4}}")
CLAIM_ID_RE = re.compile(rf"(?:{'|'.join(PREFIXES)})-[0-9]{{4}}-C[0-9]{{2,}}")
CLAIM_RE = re.compile(
    rf"^> \*\*Claim record — (?P<id>{CLAIM_ID_RE.pattern})"
    r" \| (?P<kind>[a-z-]+)\*\*\s*$",
    re.MULTILINE,
)
CLAIM_TYPES = {
    "artifact-observation",
    "source-report",
    "analytic-judgment",
    "hypothesis",
}
LINK_RE = re.compile(
    r"!?\[[^\]\n]*\]\("
    r"(?P<target><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'))?\)"
)
CYRILLIC_RE = re.compile(r"[\u0400-\u052f\u2de0-\u2dff\ua640-\ua69f]")
TEXT_SUFFIXES = {
    ".cff",
    ".html",
    ".json",
    ".md",
    ".py",
    ".sha256",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEXT_NAMES = {".gitattributes", ".gitignore", "LICENSE"}
REQUIRED_PROJECT_PATHS = {
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/evidence-correction.yml",
    ".github/ISSUE_TEMPLATE/new-source.yml",
    ".github/ISSUE_TEMPLATE/structural-proposal.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/check.yml",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "MAINTAINERS.md",
    "RELEASES.md",
    "wiki/_templates/control.md",
    "wiki/_templates/governance.md",
    "wiki/_templates/incident.md",
    "wiki/_templates/question.md",
    "wiki/_templates/risk-scenario.md",
    "wiki/_templates/source.md",
    "wiki/_templates/synthesis.md",
    "wiki/_templates/topic.md",
}
UNPUBLISHED_CHANGELOG_CHECKPOINTS = {("0.1.0", "2026-07-13")}


@dataclass(frozen=True)
class Diagnostic:
    path: str
    line: int
    message: str


@dataclass
class Page:
    path: Path
    wiki_path: str
    text: str
    frontmatter: dict[str, str]
    frontmatter_lines: list[str]
    claims: set[str] = field(default_factory=set)

    @property
    def identifier(self) -> str:
        return self.frontmatter.get("id", "")

    @property
    def page_type(self) -> str:
        return self.frontmatter.get("type", "")


@dataclass(frozen=True)
class RegistryRow:
    identifier: str
    page_type: str
    current_path: str
    issued: str
    state: str
    line: int


class Checker:
    def __init__(self) -> None:
        self.errors: list[Diagnostic] = []
        self.public_paths: set[str] = set()
        self.markdown: dict[str, str] = {}
        self.pages: list[Page] = []
        self.pages_by_id: dict[str, Page] = {}
        self.pages_by_path: dict[str, Page] = {}
        self.claims: dict[str, tuple[Page, int]] = {}
        self.link_count = 0
        self.relation_count = 0
        self.registry_count = 0
        self.raw_count = 0
        self.release_artifact_count = 0
        self.text_count = 0

    def error(self, path: Path | str, message: str, line: int = 1) -> None:
        if isinstance(path, Path):
            try:
                shown = path.relative_to(ROOT).as_posix()
            except ValueError:
                shown = path.as_posix()
        else:
            shown = path
        self.errors.append(Diagnostic(shown, line, message))

    def run(self) -> int:
        self._inventory_public_files()
        self._check_text_files()
        self._check_project_contracts()
        self._read_pages()
        self._index_claims_and_relations()
        self._check_registry()
        self._check_markdown_links()
        self._check_public_raw_boundary()

        if self.errors:
            for item in sorted(self.errors, key=lambda value: (value.path, value.line, value.message)):
                print(f"ERROR {item.path}:{item.line}: {item.message}", file=sys.stderr)
            print(f"FAIL quality gate: {len(self.errors)} error(s)", file=sys.stderr)
            return 1

        print(
            "PASS quality gate: "
            f"text={self.text_count} markdown={len(self.markdown)} "
            f"entities={len(self.pages)} claims={len(self.claims)} "
            f"relations={self.relation_count} registry={self.registry_count} "
            f"links={self.link_count} raw_git={self.raw_count} "
            f"release_artifacts={self.release_artifact_count}"
        )
        return 0

    def _inventory_public_files(self) -> None:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", "replace").strip()
            self.error(".", f"cannot inventory the public Git boundary: {detail}")
            return

        try:
            names = result.stdout.decode("utf-8").split("\0")
        except UnicodeDecodeError as exc:
            self.error(".", f"Git path inventory is not UTF-8: {exc}")
            return

        casefolded: dict[str, str] = {}
        for name in names:
            if not name:
                continue
            rel = PurePosixPath(name).as_posix()
            path = ROOT / rel
            if not path.exists() and not path.is_symlink():
                continue
            if path.is_symlink():
                self.error(path, "public files must not be symbolic links")
                continue
            if not path.is_file():
                continue
            self.public_paths.add(rel)
            folded = rel.casefold()
            previous = casefolded.get(folded)
            if previous is not None and previous != rel:
                self.error(path, f"path collides case-insensitively with {previous!r}")
            else:
                casefolded[folded] = rel

    def _check_text_files(self) -> None:
        for rel in sorted(self.public_paths):
            path = ROOT / rel
            if rel.startswith("raw/") and rel != "raw/README.md":
                continue
            if path.name not in TEXT_NAMES and path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                data = path.read_bytes()
            except OSError as exc:
                self.error(path, f"cannot read text file: {exc}")
                continue
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError as exc:
                self.error(path, f"text file is not valid UTF-8: {exc}")
                continue
            self.text_count += 1
            if text.startswith("\ufeff"):
                self.error(path, "UTF-8 text must not use a byte-order mark")
            if "\r" in text:
                line = text.count("\n", 0, text.index("\r")) + 1
                self.error(path, "text must use LF line endings", line)
            if data and not data.endswith(b"\n"):
                self.error(path, "text file must end with a newline", text.count("\n") + 1)
            for line_number, line_text in enumerate(text.splitlines(), 1):
                if line_text.endswith((" ", "\t")):
                    self.error(path, "trailing whitespace", line_number)
            if path.suffix.lower() == ".md":
                self.markdown[rel] = text
                match = CYRILLIC_RE.search(text)
                if match is not None:
                    line = text.count("\n", 0, match.start()) + 1
                    self.error(path, "Cyrillic text is not allowed in the English Markdown corpus", line)
                obsidian = text.find("[[")
                if obsidian >= 0:
                    line = text.count("\n", 0, obsidian) + 1
                    self.error(path, "Obsidian-style [[ links are not allowed", line)

    def _check_project_contracts(self) -> None:
        for rel in sorted(REQUIRED_PROJECT_PATHS):
            if rel not in self.public_paths:
                self.error(
                    ROOT / rel,
                    "missing required project contract, contribution route, or page template",
                )

        citation_path = ROOT / "CITATION.cff"
        changelog_path = ROOT / "CHANGELOG.md"
        try:
            citation = citation_path.read_text(encoding="utf-8")
        except OSError as exc:
            self.error(citation_path, f"cannot read citation metadata: {exc}")
            return
        changelog = self.markdown.get("CHANGELOG.md")
        if changelog is None:
            self.error(changelog_path, "missing public changelog")
            return

        version_match = re.search(
            r'^version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$',
            citation,
            re.MULTILINE,
        )
        date_match = re.search(
            r'^date-released:\s*["\']?([0-9]{4}-[0-9]{2}-[0-9]{2})["\']?\s*$',
            citation,
            re.MULTILINE,
        )
        if bool(version_match) != bool(date_match):
            self.error(
                citation_path,
                "version and date-released must either both be present or both be absent",
            )
            return

        released = re.findall(
            r"^## \[([0-9]+\.[0-9]+\.[0-9]+)\] - ([0-9]{4}-[0-9]{2}-[0-9]{2})$",
            changelog,
            re.MULTILINE,
        )
        if not released:
            if version_match is not None:
                self.error(
                    changelog_path,
                    "citation metadata declares a release absent from the changelog",
                )
            return
        newest_release = max(
            released,
            key=lambda item: tuple(int(part) for part in item[0].split(".")),
        )
        if version_match is None or date_match is None:
            if newest_release not in UNPUBLISHED_CHANGELOG_CHECKPOINTS:
                self.error(
                    citation_path,
                    "the newest changelog release requires matching version and "
                    "date-released fields",
                )
            return

        citation_release = (version_match.group(1), date_match.group(1))
        if citation_release in UNPUBLISHED_CHANGELOG_CHECKPOINTS:
            self.error(
                citation_path,
                "citation metadata must not present the untagged 0.1.0 checkpoint "
                "as a public knowledge release",
            )
        elif citation_release != newest_release:
            self.error(
                citation_path,
                "citation version/date do not match the newest released changelog heading "
                f"{newest_release[0]} ({newest_release[1]})",
            )

    def _read_pages(self) -> None:
        filenames: dict[str, Page] = {}
        for page_type, (_, directory) in TYPE_LAYOUT.items():
            entity_dir = WIKI / directory
            if not entity_dir.exists():
                continue
            for path in sorted(entity_dir.glob("*.md")):
                rel_root = path.relative_to(ROOT).as_posix()
                text = self.markdown.get(rel_root)
                if text is None:
                    self.error(path, "entity page is outside the public Git boundary or unreadable")
                    continue
                fields, frontmatter_lines = self._parse_frontmatter(path, text)
                page = Page(
                    path=path,
                    wiki_path=path.relative_to(WIKI).as_posix(),
                    text=text,
                    frontmatter=fields,
                    frontmatter_lines=frontmatter_lines,
                )
                self.pages.append(page)
                for required in ("id", "type", "title", "status", "sensitivity", "dual_use"):
                    if not fields.get(required, "").strip():
                        self.error(path, f"missing required frontmatter field {required!r}")
                if fields.get("sensitivity") not in {"", "public"}:
                    self.error(path, "a public Git entity must have sensitivity 'public'")
                if fields.get("dual_use") not in {"", "low", "moderate", "high"}:
                    self.error(path, f"invalid dual_use value {fields.get('dual_use')!r}")

                identifier = page.identifier
                if not ID_RE.fullmatch(identifier):
                    self.error(path, f"invalid page ID {identifier!r}")
                else:
                    expected_prefix = identifier.lower() + "-"
                    if not path.name.startswith(expected_prefix):
                        self.error(path, f"filename must start with {expected_prefix!r}")
                    if not re.fullmatch(
                        r"[a-z]{3}-[0-9]{4}-[a-z0-9][a-z0-9-]*\.md", path.name
                    ):
                        self.error(path, "filename must be lowercase ASCII with an ID prefix and slug")

                if page.page_type != page_type:
                    self.error(
                        path,
                        f"frontmatter type {page.page_type!r} does not match directory type {page_type!r}",
                    )
                expected_prefix = TYPE_LAYOUT[page_type][0]
                if identifier and not identifier.startswith(expected_prefix + "-"):
                    self.error(path, f"ID prefix must be {expected_prefix} for type {page_type!r}")

                folded = path.name.casefold()
                previous = filenames.get(folded)
                if previous is not None:
                    self.error(path, f"entity filename duplicates {previous.wiki_path!r}")
                else:
                    filenames[folded] = page

                previous_id = self.pages_by_id.get(identifier)
                if identifier and previous_id is not None:
                    self.error(path, f"duplicate page ID {identifier}; first used by {previous_id.wiki_path}")
                elif identifier:
                    self.pages_by_id[identifier] = page
                self.pages_by_path[page.wiki_path] = page

    def _parse_frontmatter(self, path: Path, text: str) -> tuple[dict[str, str], list[str]]:
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            self.error(path, "entity page must start with YAML frontmatter")
            return {}, []
        try:
            end = lines.index("---", 1)
        except ValueError:
            self.error(path, "frontmatter has no closing '---'")
            return {}, []

        fields: dict[str, str] = {}
        for offset, line in enumerate(lines[1:end], 2):
            match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
            if match is None:
                continue
            key = match.group(1)
            value = self._unquote((match.group(2) or "").strip())
            if key in fields:
                self.error(path, f"duplicate top-level frontmatter key {key!r}", offset)
            else:
                fields[key] = value
        return fields, lines[1:end]

    @staticmethod
    def _unquote(value: str) -> str:
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            return value[1:-1]
        return value

    def _index_claims_and_relations(self) -> None:
        for page in self.pages:
            searchable = self._without_fenced_code(page.text)
            claim_line_starts: set[int] = set()
            for match in CLAIM_RE.finditer(searchable):
                identifier = match.group("id")
                line = searchable.count("\n", 0, match.start()) + 1
                claim_line_starts.add(line)
                if match.group("kind") not in CLAIM_TYPES:
                    self.error(page.path, f"invalid claim type {match.group('kind')!r}", line)
                if page.identifier and not identifier.startswith(page.identifier + "-C"):
                    self.error(page.path, f"claim {identifier} is not owned by {page.identifier}", line)
                previous = self.claims.get(identifier)
                if previous is not None:
                    self.error(
                        page.path,
                        f"duplicate claim ID {identifier}; first used by {previous[0].wiki_path}:{previous[1]}",
                        line,
                    )
                else:
                    self.claims[identifier] = (page, line)
                page.claims.add(identifier)

            for line_number, line_text in enumerate(searchable.splitlines(), 1):
                if line_text.startswith("> **Claim record") and line_number not in claim_line_starts:
                    self.error(page.path, "malformed claim record heading", line_number)
                if line_text.startswith("> [!claim]"):
                    self.error(page.path, "legacy Obsidian claim callouts are not allowed", line_number)

            relation_claims, relation_tuples = self._parse_relations(page)
            self.relation_count += len(relation_tuples)
            seen_relations: set[tuple[str, str, str]] = set()
            for predicate, target, claim_id, line in relation_tuples:
                key = (predicate, target, claim_id)
                if key in seen_relations:
                    self.error(
                        page.path,
                        f"duplicate relation predicate={predicate!r} target={target!r} claim_id={claim_id!r}",
                        line,
                    )
                else:
                    seen_relations.add(key)
                if not ID_RE.fullmatch(target):
                    self.error(page.path, f"invalid relation target {target!r}", line)
                elif target not in self.pages_by_id:
                    self.error(page.path, f"relation target {target} has no public entity page", line)
            for claim_id, line in relation_claims:
                if not CLAIM_ID_RE.fullmatch(claim_id):
                    self.error(page.path, f"invalid relation claim_id {claim_id!r}", line)
                elif page.identifier and not claim_id.startswith(page.identifier + "-C"):
                    self.error(page.path, f"relation claim_id {claim_id} is not owned by {page.identifier}", line)
                elif claim_id not in page.claims:
                    self.error(page.path, f"relation claim_id {claim_id} has no claim record on this page", line)

    def _parse_relations(
        self, page: Page
    ) -> tuple[list[tuple[str, int]], list[tuple[str, str, str, int]]]:
        claims: list[tuple[str, int]] = []
        relations: list[tuple[str, str, str, int]] = []
        in_relations = False
        current: dict[str, str | int] | None = None

        def finish() -> None:
            nonlocal current
            if current is None:
                return
            predicate = str(current.get("predicate", ""))
            target = str(current.get("target", ""))
            claim_id = str(current.get("claim_id", ""))
            if predicate and target and claim_id:
                relations.append((predicate, target, claim_id, int(current.get("line", 1))))
            else:
                missing = [
                    name
                    for name, value in (
                        ("predicate", predicate),
                        ("target", target),
                        ("claim_id", claim_id),
                    )
                    if not value
                ]
                self.error(
                    page.path,
                    f"relation is missing {', '.join(missing)}",
                    int(current.get("line", 1)),
                )
            current = None

        for index, line in enumerate(page.frontmatter_lines, 2):
            if line == "relations:":
                in_relations = True
                continue
            if in_relations and line and not line.startswith(" "):
                finish()
                in_relations = False
            if not in_relations:
                continue
            predicate = re.match(r"^  - predicate:\s*(.+?)\s*$", line)
            if predicate:
                finish()
                current = {"predicate": self._unquote(predicate.group(1)), "line": index}
                continue
            if current is None:
                continue
            target = re.match(r"^    target:\s*(.+?)\s*$", line)
            if target:
                current["target"] = self._unquote(target.group(1))
                continue
            claim = re.match(r"^    claim_id:\s*(.+?)\s*$", line)
            if claim:
                value = self._unquote(claim.group(1))
                if "claim_id" in current:
                    self.error(page.path, "relation repeats claim_id", index)
                current["claim_id"] = value
                claims.append((value, index))
        finish()
        return claims, relations

    def _check_registry(self) -> None:
        path = WIKI / "id-registry.md"
        text = self.markdown.get("wiki/id-registry.md")
        if text is None:
            self.error(path, "missing public ID registry")
            return
        rows: list[RegistryRow] = []
        for line_number, line in enumerate(text.splitlines(), 1):
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 5 or not ID_RE.fullmatch(cells[0]):
                continue
            rows.append(
                RegistryRow(
                    identifier=cells[0],
                    page_type=cells[1],
                    current_path=cells[2].strip("`"),
                    issued=cells[3],
                    state=cells[4].split(" — ", 1)[0].strip(),
                    line=line_number,
                )
            )
        self.registry_count = len(rows)
        if not rows:
            self.error(path, "registry contains no entity rows")
            return

        by_id: dict[str, RegistryRow] = {}
        by_path: dict[str, RegistryRow] = {}
        valid_states = {"active", "reserved", "retired", "superseded", "archived"}
        required_status = {"active": "active", "superseded": "superseded", "archived": "archived"}
        for row in rows:
            if row.identifier in by_id:
                self.error(path, f"duplicate registry ID {row.identifier}", row.line)
            else:
                by_id[row.identifier] = row
            has_path = row.current_path not in {"", "—", "-"}
            if has_path:
                folded_path = row.current_path.casefold()
                if folded_path in by_path:
                    self.error(path, f"duplicate registry path {row.current_path!r}", row.line)
                else:
                    by_path[folded_path] = row
            if row.page_type not in TYPE_LAYOUT:
                self.error(path, f"unknown registry type {row.page_type!r}", row.line)
                continue
            prefix, directory = TYPE_LAYOUT[row.page_type]
            if not row.identifier.startswith(prefix + "-"):
                self.error(path, f"registry ID {row.identifier} does not match type {row.page_type!r}", row.line)
            if has_path:
                pure = PurePosixPath(row.current_path)
                if pure.is_absolute() or ".." in pure.parts or pure.parent.as_posix() != directory:
                    self.error(path, f"unsafe or misplaced registry path {row.current_path!r}", row.line)
                if not pure.name.startswith(row.identifier.lower() + "-"):
                    self.error(path, f"registry path does not use the ID prefix for {row.identifier}", row.line)
            elif row.state != "retired":
                self.error(path, f"registry state {row.state!r} requires a current path", row.line)
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", row.issued):
                self.error(path, f"registry Issued is not an ISO date: {row.issued!r}", row.line)
            if row.state not in valid_states:
                self.error(path, f"invalid registry state {row.state!r}", row.line)

            page = self.pages_by_path.get(row.current_path) if has_path else None
            public_page_for_id = self.pages_by_id.get(row.identifier)
            if row.state == "retired" and public_page_for_id is not None:
                self.error(path, f"retired registry ID {row.identifier} must not have a public page", row.line)
            if row.state in {"active", "superseded", "archived"} and page is None:
                self.error(path, f"{row.state} registry row {row.identifier} has no page", row.line)
                continue
            if page is None:
                continue
            if page.identifier != row.identifier:
                self.error(path, f"registry ID {row.identifier} disagrees with page ID {page.identifier!r}", row.line)
            if page.page_type != row.page_type:
                self.error(
                    path,
                    f"registry type {row.page_type!r} disagrees with page type {page.page_type!r}",
                    row.line,
                )
            expected = required_status.get(row.state)
            if expected and page.frontmatter.get("status") != expected:
                self.error(path, f"registry state {row.state!r} requires page status {expected!r}", row.line)
            if row.state == "reserved" and page.frontmatter.get("status") != "draft":
                self.error(path, "a present reserved page must have status 'draft'", row.line)

        for page in self.pages:
            row = by_id.get(page.identifier)
            if row is None:
                self.error(page.path, f"entity {page.identifier} is missing from id-registry.md")
            elif row.current_path != page.wiki_path:
                self.error(
                    page.path,
                    f"registry path for {page.identifier} is {row.current_path!r}, expected {page.wiki_path!r}",
                )

    def _check_markdown_links(self) -> None:
        public_files = self.public_paths
        public_directories: set[str] = {"."}
        for rel in public_files:
            parent = PurePosixPath(rel).parent
            while parent.as_posix() not in {".", ""}:
                public_directories.add(parent.as_posix())
                parent = parent.parent

        for rel, text in sorted(self.markdown.items()):
            searchable = self._without_fenced_code(text)
            searchable = re.sub(r"`+[^`\n]*`+", "", searchable)
            source_parent = PurePosixPath(rel).parent.as_posix()
            for match in LINK_RE.finditer(searchable):
                target = match.group("target")
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                target = unquote(target)
                if not target or target.startswith("#"):
                    continue
                if target.startswith("//") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                    continue
                line = searchable.count("\n", 0, match.start()) + 1
                self.link_count += 1
                if target.startswith("/"):
                    self.error(ROOT / rel, f"repository link must be relative: {target!r}", line)
                    continue
                clean = target.split("#", 1)[0].split("?", 1)[0]
                if not clean:
                    continue
                if "\\" in clean:
                    self.error(ROOT / rel, f"repository link must use forward slashes: {target!r}", line)
                    continue
                combined = posixpath.normpath(posixpath.join(source_parent, clean))
                if combined == ".." or combined.startswith("../") or combined.startswith("/"):
                    self.error(ROOT / rel, f"repository link escapes the repository: {target!r}", line)
                    continue
                if combined not in public_files and combined not in public_directories:
                    folded = combined.casefold()
                    case_match = next(
                        (
                            item
                            for item in public_files | public_directories
                            if item.casefold() == folded
                        ),
                        None,
                    )
                    if case_match is not None:
                        self.error(
                            ROOT / rel,
                            f"repository link has wrong path case: {target!r}; expected {case_match!r}",
                            line,
                        )
                    else:
                        self.error(ROOT / rel, f"unresolved public repository link {target!r}", line)

    def _check_public_raw_boundary(self) -> None:
        gitignore_path = ROOT / ".gitignore"
        raw_sources_path = ROOT / "RAW_SOURCES.md"
        manifest_path = ROOT / "RAW_ARTIFACTS.sha256"
        try:
            gitignore = gitignore_path.read_text(encoding="utf-8")
        except OSError as exc:
            self.error(gitignore_path, f"cannot read raw allowlist: {exc}")
            return
        raw_sources = self.markdown.get("RAW_SOURCES.md")
        if raw_sources is None:
            self.error(raw_sources_path, "missing public raw-source review")
            return
        try:
            manifest_text = manifest_path.read_text(encoding="utf-8")
        except OSError as exc:
            self.error(manifest_path, f"cannot read release-artifact manifest: {exc}")
            return

        ignored_allowlist = {
            line[1:].strip()
            for line in gitignore.splitlines()
            if line.startswith("!raw/") and line.strip() != "!raw/README.md"
        }
        actual_public = {
            rel for rel in self.public_paths if rel.startswith("raw/") and rel != "raw/README.md"
        }
        self.raw_count = len(actual_public)
        if ignored_allowlist:
            self.error(
                gitignore_path,
                "raw binaries must not be unignored for Git: " + ", ".join(sorted(ignored_allowlist)),
            )
        if actual_public:
            self.error(
                gitignore_path,
                "public Git history must not contain raw binaries: " + ", ".join(sorted(actual_public)),
            )

        manifest: dict[str, str] = {}
        manifest_order: list[str] = []
        for line_number, line in enumerate(manifest_text.splitlines(), 1):
            match = re.fullmatch(
                r"([0-9a-f]{64})  (raw/[a-z0-9][a-z0-9.-]*\.(?:jpg|pdf))",
                line,
            )
            if match is None:
                self.error(manifest_path, "invalid raw release manifest entry", line_number)
                continue
            digest, rel = match.groups()
            if rel in manifest:
                self.error(manifest_path, f"duplicate raw release path {rel!r}", line_number)
                continue
            manifest[rel] = digest
            manifest_order.append(rel)
        if manifest_order != sorted(manifest_order):
            self.error(manifest_path, "raw release manifest paths must be sorted")
        self.release_artifact_count = len(manifest)

        reviewed_paths = set(re.findall(r"`(raw/[a-z0-9][a-z0-9.-]*\.(?:jpg|pdf))`", raw_sources))
        self._compare_sets(
            manifest_path,
            "RAW_ARTIFACTS.sha256 paths",
            set(manifest),
            "RAW_SOURCES.md reviewed paths",
            reviewed_paths,
        )

        provenance: dict[str, str] = {}
        for line_number, line in enumerate(raw_sources.splitlines(), 1):
            targets = [match.group("target").strip("<>") for match in LINK_RE.finditer(line)]
            raw_targets = re.findall(r"`(raw/[a-z0-9][a-z0-9.-]*\.(?:jpg|pdf))`", line)
            if not raw_targets:
                continue
            source_targets = [target for target in targets if target.startswith("wiki/sources/")]
            if len(source_targets) != 1:
                self.error(
                    raw_sources_path,
                    "each raw allowlist row must identify exactly one wiki/sources provenance page",
                    line_number,
                )
                continue
            for raw_target in raw_targets:
                previous = provenance.get(raw_target)
                if previous is not None and previous != source_targets[0]:
                    self.error(
                        raw_sources_path,
                        f"raw artifact {raw_target!r} has conflicting provenance links",
                        line_number,
                    )
                provenance[raw_target] = source_targets[0]

        bindings = self._source_raw_bindings()
        for rel, manifest_hash in sorted(manifest.items()):
            source_rel = provenance.get(rel)
            if source_rel is None:
                self.error(raw_sources_path, f"released raw artifact {rel!r} has no provenance row")
                continue
            candidates = [item for item in bindings.get(rel, []) if item[0] == source_rel]
            if not candidates:
                self.error(
                    raw_sources_path,
                    f"{rel!r} is not bound to a sha256 in its declared provenance page {source_rel!r}",
                )
                continue
            valid_hashes = {
                declared_hash.lower()
                for _, declared_hash in candidates
                if re.fullmatch(r"[0-9a-fA-F]{64}", declared_hash)
            }
            for _, declared_hash in candidates:
                if not re.fullmatch(r"[0-9a-fA-F]{64}", declared_hash):
                    self.error(ROOT / source_rel, f"invalid sha256 for {rel!r}: {declared_hash!r}")
            if manifest_hash not in valid_hashes:
                self.error(
                    manifest_path,
                    f"sha256 mismatch: {source_rel} does not bind {rel!r} to {manifest_hash}",
                )

    def _source_raw_bindings(self) -> dict[str, list[tuple[str, str]]]:
        bindings: dict[str, list[tuple[str, str]]] = {}
        for page in self.pages:
            if page.page_type != "source":
                continue
            main_path = page.frontmatter.get("raw_path")
            main_hash = page.frontmatter.get("sha256")
            if main_path and main_hash:
                normalized = self._normalize_declared_path(page.path, main_path)
                if normalized is not None:
                    bindings.setdefault(normalized, []).append(
                        (page.path.relative_to(ROOT).as_posix(), main_hash)
                    )

            current_path: str | None = None
            current_hash: str | None = None

            def finish_component() -> None:
                nonlocal current_path, current_hash
                if current_path and current_hash:
                    normalized = self._normalize_declared_path(page.path, current_path)
                    if normalized is not None:
                        bindings.setdefault(normalized, []).append(
                            (page.path.relative_to(ROOT).as_posix(), current_hash)
                        )
                current_path = None
                current_hash = None

            in_components = False
            for line in page.frontmatter_lines:
                if line == "raw_components:":
                    in_components = True
                    continue
                if in_components and line and not line.startswith(" "):
                    finish_component()
                    in_components = False
                if not in_components:
                    continue
                component = re.match(r"^  - path:\s*(.+?)\s*$", line)
                if component:
                    finish_component()
                    current_path = self._unquote(component.group(1))
                    continue
                digest = re.match(r"^    sha256:\s*(.+?)\s*$", line)
                if digest and current_path:
                    current_hash = self._unquote(digest.group(1))
            finish_component()
        return bindings

    def _normalize_declared_path(self, page: Path, value: str) -> str | None:
        page_parent = page.relative_to(ROOT).parent.as_posix()
        normalized = posixpath.normpath(posixpath.join(page_parent, value))
        if normalized == ".." or normalized.startswith("../") or normalized.startswith("/"):
            self.error(page, f"raw path escapes the repository: {value!r}")
            return None
        return normalized

    def _compare_sets(
        self,
        path: Path,
        left_name: str,
        left: set[str],
        right_name: str,
        right: set[str],
    ) -> None:
        missing = sorted(left - right)
        extra = sorted(right - left)
        if missing:
            self.error(path, f"{right_name} missing entries from {left_name}: {', '.join(missing)}")
        if extra:
            self.error(path, f"{right_name} has entries absent from {left_name}: {', '.join(extra)}")

    @staticmethod
    def _without_fenced_code(text: str) -> str:
        result: list[str] = []
        fence_char = ""
        fence_length = 0
        for line in text.splitlines(keepends=True):
            match = re.match(r"^\s*(`{3,}|~{3,})", line)
            if not fence_char and match:
                fence_char = match.group(1)[0]
                fence_length = len(match.group(1))
                result.append("\n" if line.endswith("\n") else "")
                continue
            if fence_char:
                closing = re.match(rf"^\s*{re.escape(fence_char)}{{{fence_length},}}\s*$", line.rstrip("\n"))
                if closing:
                    fence_char = ""
                    fence_length = 0
                result.append("\n" if line.endswith("\n") else "")
                continue
            result.append(line)
        return "".join(result)


if __name__ == "__main__":
    raise SystemExit(Checker().run())
