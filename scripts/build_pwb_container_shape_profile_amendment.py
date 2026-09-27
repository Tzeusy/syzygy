#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB container-shape profile amendment package.

N8 (`syzygy-u05.8`), drafted under the 2026-09-26 sitting's §6 ruling. The
amendment lets the observed project's profile declare each class's extraction
rule from a closed vocabulary of nine container shapes and eight key forms,
and keeps today's Butlers grammar in the reader definitions as Butlers'
declaration. It performs no owner act and writes no act record.

The signed PWB bytes are never edited while this package is a candidate.
Proposed bytes live as patches, and the manifest hashes the eleven-artifact
subject after those patches. Applying them is an adoption-time operation.

`--check` verifies the proposed text rule by rule, regenerates the dependency
declaration and the contract-coverage report from the proposed bytes, and
composes every shared patch with each sibling PWB package in both orders
against a declared table, so a drifted sibling fails the check instead of
passing it.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
CANDIDATE = CANDIDATES / "pwb-container-shape-profile-amendment"
PROPOSED = CANDIDATE / "proposed"
MANIFEST_OUT = CANDIDATE / "PWB-CONTAINER-SHAPE-PROFILE-MANIFEST.txt"
TITLE = "PWB CONTAINER-SHAPE PROFILE AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
DEPENDENCIES = CHANGE / "GOVERNING-DEPENDENCIES.md"
CAPABILITY_COVERAGE = CHANGE / "CAPABILITY-COVERAGE.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"

BEHAVIOR_SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "CAPABILITY-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CHANGE / "CONTRACT-COVERAGE.md",
            CHANGE / "GOVERNING-DEPENDENCIES.md",
            CHANGE / "contract-coverage-matrix/RFC-0001-0003.md",
            CHANGE / "contract-coverage-matrix/RFC-0004-0006.md",
            CHANGE / "contract-coverage-matrix/RFC-0007-0009.md",
            CHANGE / "design.md",
            CHANGE / "proposal.md",
            CHANGE / "specs/polaris-project-wide-butlers-model/spec.md",
        ),
        key=lambda path: path.as_posix(),
    )
)
PATCHED = tuple(
    sorted(
        (CAPABILITY_COVERAGE, DEPENDENCIES, SPEC),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)

READER_START = "Reader definitions:\n"
READER_END = "## ADDED Requirements"
VOCABULARY_OPENING = "- A **container shape** is how the items of one grammar row sit inside its"
KEYS_OPENING = "- An **item key form** says what becomes an item's key and how a key fails."
PROFILE_OPENING = "- The **project profile** declares a project's extraction grammar as grammar"
LOADED_OPENING = "- Until Butlers' profile is loaded, the observer reads Butlers by the grammar"
EXACT_OPENING = "- For every grammar, loaded or built-in, heading levels/text, top-level list"
BUTLERS_OPENING = (
    "- Butlers' profile declares exactly the following extraction grammar, "
    "which is\n  literal:\n"
)
#: The reader-definition bullets this package adds, in the order they must
#: appear. Each runs to the next one; the last runs to BUTLERS_OPENING.
BULLETS = (
    ("vocabulary", VOCABULARY_OPENING),
    ("key-form", KEYS_OPENING),
    ("profile", PROFILE_OPENING),
    ("loaded-profile", LOADED_OPENING),
    ("exactness", EXACT_OPENING),
    ("Butlers grammar", BUTLERS_OPENING),
)
#: The pre-amendment opening of the Butlers grammar bullet. It must be gone:
#: the grammar is now Butlers' declaration, not the only grammar.
RETIRED_OPENING = "- The extraction grammar is literal:\n"
#: The exactness paragraph as it closes the Butlers grammar today. The package
#: hoists it into its own bullet so it governs every grammar.
GRAMMAR_END = "  Heading levels/text, top-level list depth"
EXACT_PREFIX = "- For every grammar, loaded or built-in, h"
#: The loaded-profile amendment's builder (`syzygy-dov.24`, PR #123). When it
#: is in the tree its sentences are compared with these; until then the two
#: packages agree by copy, and `--check` says so.
SHARED_TEXT = "build_pwb_registry_loaded_profile_amendment"
#: The closed shape vocabulary, name -> the sentence `syzygy-dov.24` gives it,
#: copied verbatim. The spec adds a full stop and code-span backticks around
#: markup; both are removed before the whitespace-folded comparison.
SHAPES = {
    "heading-section": (
        "the body under the declared heading: the lines after it up to the next heading at "
        "the same or a higher level, with outer whitespace trimmed, NFC-normalized; the body "
        "may be empty; when a row declares two headings the item's text is the first heading's "
        "text, a blank line, its body, a blank line, the second heading's text, a blank line "
        "and its body, with outer whitespace trimmed"),
    "every-level-2-section": (
        "every level-2 heading in the file, in file order; each part is the heading's text, a "
        "blank line and its body read as heading-section reads it, with outer whitespace "
        "trimmed, and the parts are joined by one blank line; a file with no level-2 heading "
        "fails the source as missing-heading"),
    "top-level-decimal-list": (
        "each list item at column 0 in the section, which must be numbered: a decimal number "
        "followed by . or ) and a space or tab; a bulleted item at column 0 fails the source "
        "as malformed-list, and so does a section with no list item at column 0"),
    "top-level-list": (
        "each list item at column 0 in the section, numbered or bulleted; a section with no "
        "list item at column 0 fails the source as malformed-list"),
    "top-level-bulleted-list": (
        "each list item at column 0 in the section, which must be bulleted: a numbered item at "
        "column 0 fails the source as malformed-list; a section with no list item yields no "
        "items and does not fail"),
    "first-table-rows": (
        "each body row of the first table in the section; a section with no table fails the "
        "source as malformed-row, and so does a body row of that table whose cell count "
        "differs from its header's; later tables in the section are not read"),
    "ordinal-section-table-rows": (
        "each body row of every table in the section of every level-2 heading whose text opens "
        "with a decimal number, optionally one lowercase letter, and then the end of the text "
        "or a character that is not an ASCII letter, digit or underscore; a file with no such "
        "heading fails the source as missing-heading, and a body row whose cell count differs "
        "from its table's header fails it as malformed-row"),
    "tree-path": (
        "the Git tree path itself, matched against the tree population's pathPattern; no body "
        "is read and nothing fails"),
    "toml-table-field": (
        "the declared field of the declared TOML table: exactly one header line must name the "
        "table, and inside it the field must be written once as field = \"value\" or "
        "field = 'value' with a non-empty value; no such table, a repeated table, a repeated "
        "field or a missing or empty value fails the source as malformed-toml; a line in any "
        "other form, and the field inside any other table, is not read"),
}
#: The closed key-form vocabulary, spec name -> (the `syzygy-dov.24` form it
#: restates, its sentence). The prefixed ordinal has no shared sentence there:
#: each success row names its own "<prefix>:<one-based ordinal>".
KEY_FORMS = {
    "fixed": ("fixed", "the fixed key"),
    "leading-bold": ("principle", (
        "the item's leading bold span (** or __), NFC-normalized with whitespace runs "
        "collapsed; an item with no non-empty leading bold span fails the source as "
        "ambiguous-leading-label")),
    "leading-bold-or-code": ("catalog", (
        "the item's leading bold span, or else its leading code span, NFC-normalized with "
        "whitespace runs collapsed; the span must be non-empty and followed, after optional "
        "whitespace, by a hyphen-minus, en dash or em dash, or the source fails as "
        "ambiguous-leading-label")),
    "prefixed-ordinal": (None, (
        "<prefix>:<one-based ordinal>, with the prefix the grammar row declares")),
    "first-cell-link-text": ("design", (
        "the link text of the first cell, which must be one whole link [text](target), "
        "optionally with a quoted title, with non-empty text, or the source fails as "
        "malformed-row")),
    "tree-key": ("tree", "the <key> segment of the tree population's pathPattern"),
    "ordinal-and-label": ("topology", (
        "the heading's ordinal, a colon and the first cell's label; the first cell must be "
        "exactly one bold span with a non-empty label, or the source fails as malformed-row")),
    "link-target-basename": ("craft", (
        "the basename of the link target in the declared column, without its fragment; a "
        "table with no such column, or a cell in it that is not one whole link whose target "
        "has a non-empty last segment, fails the source as malformed-row")),
}
ENTRY = re.compile(r"^  - `([^`\n]+)`: ", re.MULTILINE)
CLOSURES = {
    "vocabulary": "The vocabulary is closed at nine shapes, and no other shape is read.",
    "key-form": "The forms are closed at eight, and no other key form is read:",
}
DUPLICATE_KEY = (
    "A key that occurs twice within one class of one source fails the source as "
    "duplicate-key."
)
PROFILE_RULES = {
    "carried in the registry entry": (
        "is carried in the project-shape observer's owner-adopted registry entry"
    ),
    "one or more rows per class": "Each class above has one or more rows.",
    "row: class and source": "Each row names its class and its source;",
    "row: headings or tree population": (
        "the heading or headings, each with its level when it has one and its "
        "exact text, or the tree population that locate it, when its shape reads one;"
    ),
    "row: parameters": (
        "every parameter its shape or key form reads, such as a table column, a "
        "TOML table and field or a key prefix;"
    ),
    "row: one shape and one key form": (
        "exactly one container shape; and exactly one item key form."
    ),
    "tree population pattern": (
        "A tree population is declared by a path pattern, `pathPattern`, whose "
        "one `<key>` segment is a single directory name."
    ),
    "nothing added by a profile": (
        "A profile cannot add a class, a shape or a key form."
    ),
}
LOADED_RULES = {
    "Butlers' interim default": (
        "written below, as a built-in default; no other project has a built-in "
        "default."
    ),
    "loaded profile is the only source": (
        "Once a project's profile is loaded, it is the only source of that "
        "project's extraction rules."
    ),
    "a class with no row": "A class that the loaded profile gives no row,",
    "a row outside the closed sets": (
        "or that has a row naming a shape or key form outside these closed sets "
        "or lacking a parameter its shape or key form reads, is unreadable:"
    ),
    "class and category Unknown": (
        "its item denominator and its category's item denominator are Unknown,"
    ),
    "sources fail as the exactness bullet says": (
        "each source any of its rows names fails as a source in which a class fails,"
    ),
    "every source stays counted": (
        "and every source stays in the source-path population."
    ),
    "no built-in substitute once loaded": (
        "The observer never substitutes a built-in rule for a loaded profile's "
        "missing or invalid one."
    ),
    "whole-load refusal": (
        "A loader that instead refuses the whole profile meets this rule only if "
        "every source stays in the source-path population with an Unknown item "
        "denominator."
    ),
}

REQUIREMENT = "### Requirement: PWB-REQ-002"
NEXT_REQUIREMENT = "### Requirement: PWB-REQ-003"
PRECEDING_SCENARIO = "#### Scenario: Declared shape reconciles"
WARRANTS = "```yaml\nwarrants:"
REQUIREMENT_RULES = {
    "body: governing grammar": (
        "declared item discovered by the extraction grammar that governs its "
        "project under the reader definitions"
    ),
    "body: loaded profile through closed sets": (
        "the grammar rows of its loaded project profile, read only through the "
        "closed container shapes and item key forms"
    ),
    "body: Butlers default": (
        "or, before Butlers' profile is loaded, the Butlers grammar written there"
    ),
    "case: class with no row": "a loaded profile that gives one class no row,",
    "case: shape outside the vocabulary": (
        "a loaded profile with a row that names a shape outside the vocabulary."
    ),
    "oracle: governing grammar": (
        "two independent extractors apply the literal grammar that governs the "
        "project"
    ),
    "oracle: written Butlers grammar": (
        "for Butlers read through its loaded profile, both also apply the grammar "
        "written in these reader definitions and must produce the same "
        "identities and D;"
    ),
    "oracle: unreadable class": (
        "and every class a loaded profile leaves unreadable, carry an Unknown "
        "item denominator."
    ),
    "falsifier: undeclared shape": (
        "an item is read through a shape or key form its governing grammar does "
        "not declare"
    ),
    "falsifier: built-in fallback": (
        "a loaded profile's missing or invalid rule is replaced by a built-in one."
    ),
}
RETIRED_REQUIREMENT_TEXT = "declared item discovered by the closed extraction rule"
SCENARIOS = (
    "#### Scenario: Butlers' profile reproduces the written grammar",
    "#### Scenario: Loaded profile gives one class no row",
    "#### Scenario: Loaded profile names a shape outside the vocabulary",
)
SCENARIO_RULES = {
    SCENARIOS[0]: (
        "each item is extracted through the container shape and item key form "
        "its grammar row declares",
        "the identities and D equal those produced by the grammar written in "
        "these reader definitions",
    ),
    SCENARIOS[1]: (
        "has no grammar row for one class",
        "that class's item denominator and its category's item denominator "
        "render Unknown",
        "every source stays in the source-path population and no built-in rule "
        "reads the class",
    ),
    SCENARIOS[2]: (
        "names a container shape or item key form outside the closed sets",
        "that class's item denominator and its category's item denominator "
        "render Unknown",
        "each source any of the class's rows names fails as a source in which a "
        "class fails",
        "no built-in or nearest shape reads the class in its place",
    ),
}
CAPABILITY_ROW = (
    "| 4 | Account for every admitted declared item exactly once, reading each "
    "class only through the grammar rows its loaded project profile declares "
    "from the closed nine-shape and eight-key-form vocabularies, with no "
    "built-in fallback once a profile is loaded | covered — PWB-REQ-002 |"
)
CAPABILITY_TOTALS = (
    "Totals: 25 covered, 6 lawfully out of scope, 0 Unknown/unresolved; 31 total."
)

SIBLINGS = {
    "opening-band-dov.21": CANDIDATES / "pwb-opening-band-scenario",
    "exact-source-dov.30": CANDIDATES / "pwb-exact-source-render-mode-scenario",
    "machine-view-dov.22": CANDIDATES / "pwb-machine-view-amendment",
    "lane-b": CANDIDATES / "pwb-scoped-attributes-amendment",
    "missing-currency-dov.20": CANDIDATES / "pwb-missing-currency-disclosure-scenario",
}
# Every (sibling, shared patch) pair and its observed outcome against this
# package's patch for the same file. "compose" means both orders apply and
# yield identical bytes; "collide" means neither order applies, so whichever
# package lands second regenerates its patch and manifest with --write.
DECLARED_COMPOSITION = {
    ("opening-band-dov.21", "GOVERNING-DEPENDENCIES.md.patch"): "collide",
    ("opening-band-dov.21", "spec.md.patch"): "compose",
    ("exact-source-dov.30", "CAPABILITY-COVERAGE.md.patch"): "compose",
    ("exact-source-dov.30", "GOVERNING-DEPENDENCIES.md.patch"): "collide",
    ("exact-source-dov.30", "spec.md.patch"): "compose",
    ("machine-view-dov.22", "GOVERNING-DEPENDENCIES.md.patch"): "collide",
    ("machine-view-dov.22", "spec.md.patch"): "compose",
    ("lane-b", "GOVERNING-DEPENDENCIES.md.patch"): "collide",
    ("lane-b", "spec.md.patch"): "compose",
    ("missing-currency-dov.20", "CAPABILITY-COVERAGE.md.patch"): "compose",
    ("missing-currency-dov.20", "GOVERNING-DEPENDENCIES.md.patch"): "collide",
    ("missing-currency-dov.20", "spec.md.patch"): "compose",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fold(text: str) -> str:
    return " ".join(text.split())


def current_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in BEHAVIOR_SUBJECTS:
        target = ROOT / rel
        if rel in overrides:
            values[rel] = overrides[rel]
        elif target.is_file():
            values[rel] = target.read_bytes()
        else:
            raise ValueError(f"missing amendment subject: {rel}")
    return values


def patch_files() -> list[pathlib.Path]:
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda path: path.name)


def apply_patches(base: pathlib.Path, patches: list[pathlib.Path]) -> None:
    for patch in patches:
        done = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", str(patch)],
            cwd=base,
            capture_output=True,
            text=True,
        )
        if done.returncode != 0:
            raise ValueError(f"{patch.name} does not apply: {done.stderr.strip()}")


def proposed_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
    patches: list[pathlib.Path] | None = None,
) -> dict[pathlib.Path, bytes]:
    current = current_bytes(overrides)
    patches = patch_files() if patches is None else patches
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        for rel, body in current.items():
            (base / rel).parent.mkdir(parents=True, exist_ok=True)
            (base / rel).write_bytes(body)
        apply_patches(base, patches)
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def _plain(text: str) -> str:
    """Whitespace-folded text with code-span backticks removed."""
    return fold(text.replace("`", ""))


def _grammar_items(text: str, opening: str, end: str | None) -> str | None:
    """The nine class bullets of the Butlers grammar, byte for byte.

    In the current spec they end where the exactness paragraph begins; in the
    proposed spec, which hoists that paragraph, at the next top-level bullet.
    """
    at = text.find(opening)
    if at < 0:
        return None
    start = at + len(opening)
    stop = text.find(end, start) if end else text.find("\n- ", start) + 1
    return text[start:stop] if stop > 0 else None


def _exactness(current: str) -> str | None:
    """The current exactness paragraph, as the proposed bullet must restate it."""
    at = current.find(GRAMMAR_END)
    if at < 0:
        return None
    stop = current.find("\n- ", at)
    return current[at:stop + 1] if stop >= 0 else None


def entry_span(block: str, name: str) -> tuple[int, int] | None:
    """Where one `  - `name`: ...` entry and its continuation lines sit."""
    entry = re.search(
        rf"^  - `{re.escape(name)}`: (?:[^\n]*\n)(?:    [^\n]*\n)*",
        block,
        re.MULTILINE,
    )
    return entry.span() if entry else None


def _entries(block: str, expected: dict[str, str], label: str) -> list[str]:
    findings: list[str] = []
    names = ENTRY.findall(block)
    if names != list(expected):
        findings.append(f"{label} vocabulary differs: {names} is not {list(expected)}")
    for name, sentence in expected.items():
        span = entry_span(block, name)
        body = block[span[0]:span[1]].split(": ", 1)[1] if span else ""
        if not span or _plain(body) != fold(sentence.replace("`", "") + "."):
            findings.append(f"{label} sentence differs: {name}")
    return findings


def shared_text_findings(module: object | None = None) -> list[str]:
    """This package's sentences against `syzygy-dov.24`'s, once it is in the tree."""
    if module is None:
        if not (ROOT / "scripts" / f"{SHARED_TEXT}.py").is_file():
            return []
        sys.path.insert(0, str(ROOT / "scripts"))
        module = __import__(SHARED_TEXT)
    findings: list[str] = []
    if getattr(module, "SHAPES", None) != SHAPES:
        findings.append("shape sentences differ from the loaded-profile amendment's")
    theirs = getattr(module, "ITEM_KEY_SENTENCES", None) or {}
    ours = {form: sentence for form, sentence in KEY_FORMS.values() if form}
    if theirs != ours:
        findings.append("key-form sentences differ from the loaded-profile amendment's")
    return findings


def reader_findings(text: str, current: str) -> list[str]:
    """The added bullets in order, each rule in them, and the Butlers grammar."""
    findings: list[str] = []
    start = text.find(READER_START)
    end = text.find(READER_END, start)
    if start < 0 or end < 0:
        return ["reader definitions are missing"]
    block = text[start:end]
    positions: dict[str, int] = {}
    for label, opening in BULLETS:
        if text.count(opening) != 1 or block.count(opening) != 1:
            findings.append(f"missing or duplicate {label} bullet")
        else:
            positions[label] = block.find(opening)
    if len(positions) == len(BULLETS) and list(positions.values()) != sorted(positions.values()):
        findings.append("the added reader-definition bullets are out of order")
    if RETIRED_OPENING in text:
        findings.append("the retired single-grammar opening is still present")
    bodies: dict[str, str] = {}
    labels = [label for label, _opening in BULLETS]
    for label, following in zip(labels, labels[1:]):
        if label in positions and following in positions and positions[following] > positions[label]:
            bodies[label] = block[positions[label]:positions[following]]
    if "vocabulary" in bodies:
        findings.extend(_entries(bodies["vocabulary"], SHAPES, "shape"))
    if "key-form" in bodies:
        findings.extend(_entries(
            bodies["key-form"],
            {name: sentence for name, (_form, sentence) in KEY_FORMS.items()},
            "key-form",
        ))
        if fold(DUPLICATE_KEY) not in fold(bodies["key-form"]):
            findings.append("key-form bullet lacks the duplicate-key rule")
    for label, closure in CLOSURES.items():
        if label in bodies and fold(closure) not in fold(bodies[label]):
            findings.append(f"{label} bullet is not stated closed")
    for label, rules in (("profile", PROFILE_RULES), ("loaded-profile", LOADED_RULES)):
        if label in bodies:
            folded = fold(bodies[label])
            for rule_label, rule in rules.items():
                if fold(rule) not in folded:
                    findings.append(f"{label} bullet lacks {rule_label}")
    expected_exact = _exactness(current)
    if expected_exact is None:
        findings.append("current spec no longer carries the exactness paragraph this package hoists")
    elif "exactness" in bodies and fold(bodies["exactness"]) != fold(
        EXACT_PREFIX + expected_exact.strip()[1:]
    ):
        findings.append("exactness bullet does not restate the current paragraph")
    if GRAMMAR_END in text:
        findings.append("the exactness paragraph is still inside the Butlers grammar")
    retained = _grammar_items(text, BUTLERS_OPENING, None)
    expected = _grammar_items(current, RETIRED_OPENING, GRAMMAR_END)
    if expected is None:
        findings.append("current spec no longer carries the grammar this package restates")
    elif retained != expected:
        findings.append("Butlers grammar is not byte-identical to the current grammar")
    return findings


def _block(text: str, heading: str) -> str:
    start = text.index(heading)
    stop = text.index("\n\n", text.index("- **AND**", start)) + 2
    return text[start:stop]


def requirement_findings(spec: bytes, current: bytes | None = None) -> list[str]:
    text = spec.decode("utf-8")
    base = (current if current is not None else current_bytes()[SPEC]).decode("utf-8")
    findings = reader_findings(text, base)
    start = text.find(REQUIREMENT)
    end = text.find(NEXT_REQUIREMENT, start)
    if start < 0 or end < 0:
        return findings + ["PWB-REQ-002 or its following requirement is missing"]
    section = text[start:end]
    folded = fold(section)
    for label, rule in REQUIREMENT_RULES.items():
        if fold(rule) not in folded:
            findings.append(f"PWB-REQ-002 lacks {label}")
    if RETIRED_REQUIREMENT_TEXT in folded:
        findings.append("PWB-REQ-002 still reads the closed extraction rule")
    preceding = section.find(PRECEDING_SCENARIO)
    warrants = section.find(WARRANTS)
    for heading in SCENARIOS:
        if text.count(heading) != 1:
            findings.append(f"missing or duplicate scenario: {heading}")
            continue
        at = section.find(heading)
        if not 0 <= preceding < at < warrants:
            findings.append(
                f"scenario is not in the required PWB-REQ-002 position: {heading}"
            )
            continue
        body = fold(_block(section, heading))
        for rule in SCENARIO_RULES[heading]:
            if fold(rule) not in body:
                findings.append(f"scenario lacks '{rule}': {heading}")
    base_start = base.find(REQUIREMENT)
    base_section = base[base_start:base.find(NEXT_REQUIREMENT, base_start)]
    base_warrants = base_section[base_section.find(WARRANTS):]
    if warrants < 0 or section[warrants:] != base_warrants:
        findings.append("PWB-REQ-002 warrants differ from the current warrants")
    return findings


def dependency_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_spec_dependencies as generator

    rendered, errors = generator.generate(proposed[SPEC].decode("utf-8"))
    if errors:
        return [f"proposed warrants do not validate: {'; '.join(errors)}"]
    if rendered.encode("utf-8") != proposed[DEPENDENCIES]:
        return [
            "proposed GOVERNING-DEPENDENCIES.md differs from regeneration "
            "over the proposed spec bytes"
        ]
    return []


def companion_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    findings: list[str] = []
    capability = proposed[CAPABILITY_COVERAGE].decode("utf-8")
    if capability.count(CAPABILITY_ROW) != 1:
        findings.append("capability coverage does not carry the amended row 4 exactly once")
    if CAPABILITY_TOTALS not in capability or "Population: 31 positive" not in capability:
        findings.append("capability coverage population or totals are not 31")

    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_contract_coverage as coverage

    # The coverage generator reads the spec's warrants from disk; serve it the
    # proposed spec bytes so an unchanged report is proved, not assumed.
    spec_path = pathlib.Path(coverage.dependencies.SPEC).resolve()
    proposed_spec = proposed[SPEC].decode("utf-8")
    original_read = coverage.base.read

    def read(path: str) -> str:
        if pathlib.Path(path).resolve() == spec_path:
            return proposed_spec
        return original_read(path)

    coverage.base.read = read
    try:
        rendered = coverage.render()
    except ValueError as error:
        findings.append(f"contract coverage does not validate: {error}")
    else:
        if rendered.encode("utf-8") != proposed[CONTRACT_COVERAGE]:
            findings.append(
                "CONTRACT-COVERAGE.md differs from regeneration over the "
                "proposed spec bytes"
            )
    finally:
        coverage.base.read = original_read
    return findings


def _target(patch: pathlib.Path) -> pathlib.Path:
    for line in patch.read_text().splitlines():
        if line.startswith("+++ b/"):
            return pathlib.Path(line[len("+++ b/"):])
    raise ValueError(f"{patch} names no target")


def _compose(target: pathlib.Path, order: list[pathlib.Path]) -> bytes | None:
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / target).parent.mkdir(parents=True, exist_ok=True)
        (base / target).write_bytes((ROOT / target).read_bytes())
        try:
            apply_patches(base, order)
        except ValueError:
            return None
        return (base / target).read_bytes()


def composition_findings(
    mine: dict[str, pathlib.Path] | None = None,
    declared: dict[tuple[str, str], str] | None = None,
) -> list[str]:
    """Exercise both orders of every shared patch against the declared table."""
    if mine is None:
        mine = {patch.name: patch for patch in patch_files()}
    declared = DECLARED_COMPOSITION if declared is None else declared
    findings: list[str] = []
    observed: set[tuple[str, str]] = set()
    for name, directory in SIBLINGS.items():
        proposed = ROOT / directory / "proposed"
        if not proposed.is_dir():
            findings.append(f"missing sibling package: {directory}")
            continue
        for sibling in sorted(proposed.glob("*.patch")):
            if sibling.name not in mine:
                continue
            key = (name, sibling.name)
            observed.add(key)
            target = _target(sibling)
            first = _compose(target, [sibling, mine[sibling.name]])
            second = _compose(target, [mine[sibling.name], sibling])
            if first is not None and second is not None and first == second:
                outcome = "compose"
                if target == SPEC:
                    # The sibling's own text sits beside ours; ours must still
                    # verify, judged against the sibling-patched base.
                    sibling_only = _compose(target, [sibling])
                    if sibling_only is None or requirement_findings(first, sibling_only):
                        findings.append(
                            f"{name} composition misplaces this package's text"
                        )
            elif first is None and second is None:
                outcome = "collide"
            else:
                outcome = "order-dependent"
            if declared.get(key) != outcome:
                findings.append(
                    f"{name} {sibling.name}: observed {outcome}, declared "
                    f"{declared.get(key, 'nothing')}"
                )
    for key in sorted(set(declared) - observed):
        findings.append(f"declared pair not observed: {key[0]} {key[1]}")
    return findings


def render(values: dict[pathlib.Path, bytes]) -> str:
    lines = [
        f"# {TITLE}",
        "# These rows bind only by the owner act that names this file's digest in",
        "# ACCEPTANCE-ACT-RECORD.md; until that act is performed they bind nothing.",
        f"# {len(BEHAVIOR_SUBJECTS)} artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
        "# Rows hash the PROPOSED bytes: current bytes with proposed/*.patch",
        "# applied. They match the tree only after --apply, the adoption step.",
    ]
    lines.extend(f"{sha256(values[rel])}  {rel.as_posix()}" for rel in BEHAVIOR_SUBJECTS)
    return "\n".join(lines) + "\n"


def verify_manifest(text: str, expected: str) -> list[str]:
    rows = ROW.findall(text)
    expected_paths = [path.as_posix() for path in BEHAVIOR_SUBJECTS]
    if [path for _digest, path in rows] != expected_paths:
        return ["manifest path population or order differs"]
    if text != expected:
        return ["manifest differs from exact regeneration over proposed bytes"]
    return []


def population_findings(patches: list[pathlib.Path]) -> list[str]:
    findings: list[str] = []
    if [patch.name for patch in patches] != sorted(f"{path.name}.patch" for path in PATCHED):
        findings.append("proposed patch population differs from declared subjects")
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)]
    current = current_bytes()
    for rel in BEHAVIOR_SUBJECTS:
        changed = proposed[rel] != current[rel]
        if changed and rel not in PATCHED:
            findings.append(f"undeclared subject change: {rel}")
        if not changed and rel in PATCHED:
            findings.append(f"declared patched subject is unchanged: {rel}")
    return findings


def structure_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    return (
        requirement_findings(proposed[SPEC])
        + dependency_findings(proposed)
        + companion_findings(proposed)
    )


def check() -> list[str]:
    findings = population_findings(patch_files())
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(structure_findings(proposed))
    findings.extend(shared_text_findings())
    findings.extend(composition_findings())
    target = ROOT / MANIFEST_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST_OUT}")
    else:
        findings.extend(verify_manifest(target.read_text(), render(proposed)))
    return findings


def _fail(name: str) -> int:
    print(f"SELFTEST FAILED: {name}")
    return 1


def _replace_once(text: str, old: str, new: str, name: str) -> str:
    if text.count(old) < 1:
        raise AssertionError(f"fixture matched nothing: {name}")
    return text.replace(old, new, 1)


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        return _fail("behavior subject is not eleven unique paths")
    proposed = proposed_bytes()
    if structure_findings(proposed):
        return _fail("unmutated proposed bytes do not verify")
    spec = proposed[SPEC].decode("utf-8")
    killed = 0

    def spec_mutant(name: str, mutated: str, expected: str) -> bool:
        return expected in requirement_findings(mutated.encode())

    # Manifest: subject drift and row order.
    baseline = render(proposed)
    current = current_bytes()
    first = next(path for path in BEHAVIOR_SUBJECTS if path not in PATCHED)
    if baseline == render(proposed_bytes({first: current[first] + b"\nsubject drift\n"})):
        return _fail("subject drift did not stale the manifest")
    rows = ROW.findall(baseline)
    reordered = baseline.replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, baseline):
        return _fail("manifest path-order mutation passed")
    killed += 2

    # Patch population: dropping the capability patch.
    without = [p for p in patch_files() if p.name != "CAPABILITY-COVERAGE.md.patch"]
    population = population_findings(without)
    if (
        "proposed patch population differs from declared subjects" not in population
        or f"declared patched subject is unchanged: {CAPABILITY_COVERAGE}" not in population
    ):
        return _fail("dropped-patch mutation passed the population predicate")
    killed += 1

    # Shape and key-form vocabularies: each sentence altered, one entry
    # dropped, one added, one moved, and each closure sentence removed.
    for label, entries in (("shape", SHAPES), ("key-form", KEY_FORMS)):
        for name in entries:
            span = entry_span(spec, name)
            if span is None:
                return _fail(f"{label} entry fixture matched nothing: {name}")
            entry = spec[span[0]:span[1]]
            mutated_entry = entry.rstrip("\n").rstrip(".") + " [changed].\n"
            mutated = spec[:span[0]] + mutated_entry + spec[span[1]:]
            if not spec_mutant(name, mutated, f"{label} sentence differs: {name}"):
                return _fail(f"{label} sentence mutation passed: {name}")
            killed += 1
        last = list(entries)[-1]
        first_name = list(entries)[0]
        span = entry_span(spec, last)
        entry = spec[span[0]:span[1]]
        first_at = spec.index(f"  - `{first_name}`: ")
        entry_mutants = {
            "dropped": spec[:span[0]] + spec[span[1]:],
            "added": spec[:span[1]] + "  - `prose-paragraphs`: each paragraph.\n" + spec[span[1]:],
            "moved": (
                spec[:first_at] + entry + spec[first_at:span[0]] + spec[span[1]:]
            ),
        }
        for name, mutated in entry_mutants.items():
            if mutated == spec or not any(
                f.startswith(f"{label} vocabulary differs")
                for f in requirement_findings(mutated.encode())
            ):
                return _fail(f"{label} entry {name} mutation passed")
            killed += 1
    for label, closure in CLOSURES.items():
        opened = _replace_once(spec, closure.split(", and")[0], "The list is open", label)
        if not spec_mutant(label, opened, f"{label} bullet is not stated closed"):
            return _fail(f"{label} closure mutation passed")
        killed += 1
    duplicate = _replace_once(spec, "fails the source as\n  duplicate-key.", "is kept.", "duplicate key")
    if not spec_mutant("duplicate", duplicate, "key-form bullet lacks the duplicate-key rule"):
        return _fail("duplicate-key rule mutation passed")
    killed += 1

    # Profile and loaded-profile bullets: each rule removed on its own.
    openings = dict(BULLETS)
    for label, rules, following in (
        ("profile", PROFILE_RULES, "loaded-profile"),
        ("loaded-profile", LOADED_RULES, "exactness"),
    ):
        at = spec.index(openings[label])
        end = spec.index(openings[following])
        for rule_label, rule in rules.items():
            paragraph = fold(spec[at:end])
            mutated_paragraph = paragraph.replace(fold(rule), "[removed]", 1)
            if mutated_paragraph == paragraph:
                return _fail(f"{label} fixture matched nothing: {rule_label}")
            mutated = spec[:at] + mutated_paragraph + "\n" + spec[end:]
            if not spec_mutant(rule_label, mutated, f"{label} bullet lacks {rule_label}"):
                return _fail(f"{label} rule mutation passed: {rule_label}")
            killed += 1

    # Shared text: a drifted sentence on either side of the two packages.
    class Module:
        pass

    for label, attribute, expected in (
        ("shape", "SHAPES", "shape sentences differ from the loaded-profile amendment's"),
        ("key form", "ITEM_KEY_SENTENCES", "key-form sentences differ from the loaded-profile amendment's"),
    ):
        module = Module()
        module.SHAPES = dict(SHAPES)
        module.ITEM_KEY_SENTENCES = {form: s for form, s in KEY_FORMS.values() if form}
        if shared_text_findings(module):
            return _fail("shared-text fixture does not verify unmutated")
        drifted = dict(getattr(module, attribute))
        key = next(iter(drifted))
        drifted[key] = drifted[key] + " [changed]"
        setattr(module, attribute, drifted)
        if expected not in shared_text_findings(module):
            return _fail(f"shared {label} drift passed")
        killed += 1

    # Bullet order, duplicates, the retired opening, the hoisted exactness
    # paragraph and the retained grammar.
    vocabulary_at = spec.index(VOCABULARY_OPENING)
    keys_at = spec.index(KEYS_OPENING)
    profile_at = spec.index(PROFILE_OPENING)
    vocabulary = spec[vocabulary_at:keys_at]
    keys = spec[keys_at:profile_at]
    reader_mutants = {
        "bullets out of order": (
            spec[:vocabulary_at] + keys + vocabulary + spec[profile_at:],
            "the added reader-definition bullets are out of order",
        ),
        "duplicate key-form bullet": (
            spec[:profile_at] + keys + spec[profile_at:],
            "missing or duplicate key-form bullet",
        ),
        "missing loaded-profile bullet": (
            spec.replace(LOADED_OPENING, "- Until later, the observer reads Butlers by the grammar", 1),
            "missing or duplicate loaded-profile bullet",
        ),
        "missing Butlers bullet": (
            spec.replace(BUTLERS_OPENING, "- Butlers declares:\n", 1),
            "missing or duplicate Butlers grammar bullet",
        ),
        "retired opening restored": (
            spec.replace(BUTLERS_OPENING, BUTLERS_OPENING + RETIRED_OPENING, 1),
            "the retired single-grammar opening is still present",
        ),
        "exactness paragraph reworded": (
            _replace_once(spec, "Unknown; it never produces a partial item set.",
                          "Unknown; it may produce a partial item set.", "exactness"),
            "exactness bullet does not restate the current paragraph",
        ),
        "exactness paragraph left in the Butlers grammar": (
            spec.replace("\n- The source-path denominator remains known",
                         "\n" + GRAMMAR_END + " are exact.\n- The source-path denominator remains known", 1),
            "the exactness paragraph is still inside the Butlers grammar",
        ),
        "Butlers grammar altered": (
            _replace_once(
                spec,
                "“Non-Negotiable Rules”; its literal leading bold phrase is the key.",
                "“Non-Negotiable Rules”; its leading bold phrase is the key.",
                "grammar",
            ),
            "Butlers grammar is not byte-identical to the current grammar",
        ),
    }
    for name, (mutated, expected) in reader_mutants.items():
        if mutated == spec or not spec_mutant(name, mutated, expected):
            return _fail(f"{name} mutation passed")
        killed += 1

    # PWB-REQ-002: each rule removed, and the retired text restored.
    req_at = spec.index(REQUIREMENT)
    req_end = spec.index(NEXT_REQUIREMENT)
    section = spec[req_at:req_end]
    for label, rule in REQUIREMENT_RULES.items():
        folded = fold(section)
        mutated_section = folded.replace(fold(rule), "[removed]", 1)
        if mutated_section == folded:
            return _fail(f"requirement-rule fixture matched nothing: {label}")
        mutated = spec[:req_at] + mutated_section + "\n\n" + spec[req_end:]
        if not spec_mutant(label, mutated, f"PWB-REQ-002 lacks {label}"):
            return _fail(f"requirement-rule mutation passed: {label}")
        killed += 1
    restored = _replace_once(
        spec,
        "declared item discovered by the extraction grammar that governs its project\n",
        "declared item discovered by the closed extraction rule across\n",
        "retired body",
    )
    if not spec_mutant("retired", restored, "PWB-REQ-002 still reads the closed extraction rule"):
        return _fail("retired requirement text mutation passed")
    killed += 1

    # Each scenario missing, duplicated, moved and emptied of each rule.
    for heading in SCENARIOS:
        block = _block(spec, heading)
        removed = spec.replace(block, "", 1)
        next_heading_end = removed.index("\n", removed.index(NEXT_REQUIREMENT)) + 1
        moved = removed[:next_heading_end] + "\n" + block + removed[next_heading_end:]
        scenario_mutants = {
            "missing": (removed, f"missing or duplicate scenario: {heading}"),
            "duplicate": (
                spec.replace(block, block + block, 1),
                f"missing or duplicate scenario: {heading}",
            ),
            "misplaced": (
                moved,
                f"scenario is not in the required PWB-REQ-002 position: {heading}",
            ),
        }
        for rule in SCENARIO_RULES[heading]:
            folded_block = fold(block)
            emptied = folded_block.replace(fold(rule), "[removed]", 1)
            scenario_mutants[f"rule '{rule}'"] = (
                spec.replace(block, emptied + "\n\n", 1),
                f"scenario lacks '{rule}': {heading}",
            )
        for name, (mutated, expected) in scenario_mutants.items():
            if mutated == spec or not spec_mutant(name, mutated, expected):
                return _fail(f"{name} scenario mutation passed: {heading}")
            killed += 1

    # Warrants: PWB-REQ-002's block must stay exactly as it is.
    warrants_at = spec.index(WARRANTS, req_at)
    warranted = _replace_once(
        spec[warrants_at:], "primary: VIS-2", "primary: VIS-4", "warrants"
    )
    if not spec_mutant(
        "warrants", spec[:warrants_at] + warranted,
        "PWB-REQ-002 warrants differ from the current warrants",
    ):
        return _fail("warrant mutation passed")
    killed += 1

    # Generated companions and the capability row.
    tampered = dict(proposed)
    tampered[DEPENDENCIES] = proposed[DEPENDENCIES].replace(
        b"17 requirement(s)", b"18 requirement(s)", 1
    )
    if tampered[DEPENDENCIES] == proposed[DEPENDENCIES] or not dependency_findings(tampered):
        return _fail("generated dependency drift passed")
    coverage_drift = dict(proposed)
    coverage_drift[CONTRACT_COVERAGE] = proposed[CONTRACT_COVERAGE] + b"\n"
    if not any("CONTRACT-COVERAGE.md differs" in f for f in companion_findings(coverage_drift)):
        return _fail("contract-coverage drift passed")
    companion_mutants = {
        "capability row": (
            CAPABILITY_ROW.encode(),
            CAPABILITY_ROW.replace("with no built-in fallback", "with a built-in fallback", 1).encode(),
            "capability coverage does not carry the amended row 4 exactly once",
        ),
        "capability totals": (
            CAPABILITY_TOTALS.encode(),
            CAPABILITY_TOTALS.replace("31 total", "32 total").encode(),
            "capability coverage population or totals are not 31",
        ),
    }
    for name, (old, new, expected) in companion_mutants.items():
        mutated = dict(proposed)
        mutated[CAPABILITY_COVERAGE] = proposed[CAPABILITY_COVERAGE].replace(old, new, 1)
        if mutated[CAPABILITY_COVERAGE] == proposed[CAPABILITY_COVERAGE] or expected not in companion_findings(mutated):
            return _fail(f"{name} mutation passed")
    killed += 4

    # Patch drift: a corrupted spec patch neither applies nor composes.
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        corrupted = original.replace(
            " - **Case (sweep)**: enumerate the source population",
            " - **Case (sweep)**: enumerate each source population",
            1,
        )
        if corrupted == original:
            return _fail("patch-drift fixture matched nothing")
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            return _fail("patch drift passed")
        mine = {patch.name: patch for patch in patch_files()}
        mine["spec.md.patch"] = broken
        if not composition_findings(mine=mine):
            return _fail("corrupted patch passed sibling composition")
    killed += 2

    # Composition table: every declared outcome flipped, one dropped, one extra.
    for key, outcome in DECLARED_COMPOSITION.items():
        flipped = dict(DECLARED_COMPOSITION)
        flipped[key] = "collide" if outcome == "compose" else "compose"
        if not composition_findings(declared=flipped):
            return _fail(f"flipped composition outcome passed: {key}")
        killed += 1
    dropped = dict(DECLARED_COMPOSITION)
    dropped.pop(("lane-b", "spec.md.patch"))
    if not composition_findings(declared=dropped):
        return _fail("undeclared sibling pair passed")
    extra = dict(DECLARED_COMPOSITION)
    extra[("lane-b", "proposal.md.patch")] = "compose"
    if not composition_findings(declared=extra):
        return _fail("declared but unobserved sibling pair passed")
    killed += 2

    if composition_findings():
        return _fail("sibling composition does not verify")
    print(
        f"selftest: {killed} mutants killed — stale manifest, path order, patch "
        f"population, {len(SHAPES)} shape and {len(KEY_FORMS)} key-form "
        "sentences, entry dropped/added/moved and closure for each vocabulary, "
        f"the duplicate-key rule, {len(PROFILE_RULES)} profile and "
        f"{len(LOADED_RULES)} loaded-profile rules, shared-text drift on both "
        "vocabularies, bullet order/duplicate/missing, retired opening, the "
        "hoisted exactness paragraph reworded or left behind, Butlers grammar "
        f"drift, {len(REQUIREMENT_RULES)} PWB-REQ-002 rules, retired "
        f"requirement text, {len(SCENARIOS)} scenarios x missing/duplicate/"
        "placement plus each scenario rule, warrants, dependency and "
        "contract-coverage drift, capability row and totals, patch drift, "
        f"{len(DECLARED_COMPOSITION)} composition outcomes and two table-shape "
        "mutants all fail closed"
    )
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is an adoption-time operation; pass --at-adoption "
            "only in the owner's act change"
        )
        return 2
    findings = check()
    if findings:
        print("refusing to apply: package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    proposed = proposed_bytes()
    for rel in PATCHED:
        (ROOT / rel).write_bytes(proposed[rel])
        print(f"applied {rel.as_posix()}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--at-adoption", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.diff:
        for patch in patch_files():
            sys.stdout.write(patch.read_text())
        return 0
    if args.apply:
        return apply(args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("PWB container-shape profile package does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(
            f"PWB container-shape profile manifest matches {len(BEHAVIOR_SUBJECTS)} "
            f"proposed subjects ({len(PATCHED)} patched, "
            f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); {len(SHAPES)} "
            f"shapes, {len(KEY_FORMS)} key forms, {len(PROFILE_RULES)} profile "
            f"rules, {len(LOADED_RULES)} loaded-profile rules, the hoisted "
            f"exactness bullet, {len(REQUIREMENT_RULES)} PWB-REQ-002 rules, "
            f"{len(SCENARIOS)} scenarios, the retained Butlers grammar, dependency "
            "and contract-coverage regeneration and "
            f"{len(DECLARED_COMPOSITION)} declared sibling-composition outcomes verify"
        )
        if (ROOT / "scripts" / f"{SHARED_TEXT}.py").is_file():
            print("shape and key-form sentences match the loaded-profile amendment's builder")
        else:
            print(
                f"shape and key-form sentences are a copy: scripts/{SHARED_TEXT}.py "
                "is not in this tree, so they are compared only once it lands"
            )
        return 0
    if not args.write:
        print(
            "refusing: regenerating the manifest retires copied act arguments; "
            "pass --write and update every registered digest copy"
        )
        return 2
    proposed = proposed_bytes()
    structure = population_findings(patch_files()) + structure_findings(proposed)
    if structure:
        for finding in structure:
            print(f"  {finding}")
        return 1
    target = ROOT / MANIFEST_OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(proposed))
    print(f"wrote {MANIFEST_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
