#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB container-shape profile amendment package.

N8 (`syzygy-u05.8`), drafted on the owner's 2026-09-26 direction to draft
(the sitting record, §6). The amendment lets the observed project's profile
declare each class's grammar rows from a closed vocabulary of nine container shapes and eight key forms,
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

What is pinned, exactly. The proposed spec.md is pinned whole: it must equal
the current spec.md with SPEC_EDITS applied, byte for byte, so no byte outside
those eight edits may change and none inside them may drift. The rule tables
below only name which rule a drift broke, and their digest is pinned. The
shape and key-form sentences must hash to the digest of `syzygy-dov.24`'s
tables at commit 1d5966c, and equal that builder's tables when it is in the
tree. GOVERNING-DEPENDENCIES.md and CONTRACT-COVERAGE.md are regenerated and
compared byte for byte. CAPABILITY-COVERAGE.md is pinned only by row 4 and its
totals, and otherwise only by the manifest digest. The patch files' own bytes
are not pinned beyond what they produce.
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
LOADED_OPENING = "- Until a profile is declared for Butlers, the observer reads Butlers by the"
DECLARED_ITEM_OPENING = "- A **declared item** "
DECLARED_ITEM_END = "- Stable item identity is"
#: The reader definitions from here to their end are not amended and must stay
#: byte-identical to the current text.
UNCHANGED_TAIL = "- The source-path denominator remains known"
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
#: The SHA-256 of repr((SHAPES, ITEM_KEY_SENTENCES)) in `syzygy-dov.24`'s
#: builder at commit 1d5966c, its round-3 repair (unchanged at the head its
#: confirmation round cleared). This package's tables must hash to it whether
#: or not that builder is in the tree.
SHARED_TEXT_COMMIT = "1d5966c"
SHARED_TEXT_SHA256 = "64b15eaeed24b510c7d744bdd09f1de4f5989d2c05c9165b3826b8ac226d753d"
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
        "other form, and the field inside any other table, is not read; an array-of-tables "
        "header such as [[other]] is a line in another form, so it neither opens a table nor "
        "ends the declared one; the value is trimmed "
        "and NFC-normalized, a backslash escape in a double-quoted value is not decoded, and "
        "the value becomes the item's context"),
}
#: The closed key-form vocabulary, name -> (the `syzygy-dov.24` form of the
#: same name, its sentence). The names are the same in both packages. The
#: prefixed ordinal has no shared sentence there: each success row writes its
#: own "<prefix>:<one-based ordinal>".
KEY_FORMS = {
    "fixed": ("fixed", "the fixed key"),
    "leading-bold": ("leading-bold", (
        "the item's leading bold span (** or __), NFC-normalized with whitespace runs "
        "collapsed; an item with no non-empty leading bold span fails the source as "
        "ambiguous-leading-label")),
    "leading-bold-or-code": ("leading-bold-or-code", (
        "the item's leading bold span, or else its leading code span, NFC-normalized with "
        "whitespace runs collapsed; the span must be non-empty and followed, after optional "
        "whitespace, by a hyphen-minus, en dash or em dash, or the source fails as "
        "ambiguous-leading-label; each item's context is the text of the declared heading it "
        "was read under")),
    "prefixed-ordinal": (None, (
        "<prefix>:<one-based ordinal>, with the prefix the grammar row declares")),
    "first-cell-link-text": ("first-cell-link-text", (
        "the link text of the first cell, trimmed and NFC-normalized; the cell must be one "
        "whole link [text](target), optionally with a space or tab and a title in double "
        "quotes after the target, with non-empty text, or the source fails as malformed-row")),
    "tree-key": ("tree-key", "the <key> segment of the tree population's pathPattern"),
    "ordinal-and-label": ("ordinal-and-label", (
        "the heading's ordinal, a colon and the first cell's label; the first cell must be "
        "exactly one bold span with a non-empty label, or the source fails as malformed-row; "
        "each item's context is the heading's ordinal")),
    "link-target-basename": ("link-target-basename", (
        "the basename of the link target in the declared column, without its fragment; a "
        "table with no such column, or a cell in it that is not one whole link whose target "
        "has a non-empty last segment, fails the source as malformed-row")),
}
ENTRY = re.compile(r"^  - `([^`\n]+)`: ", re.MULTILINE)
CLOSURES = {
    "vocabulary": "The vocabulary is closed at nine shapes, and no other shape is read.",
    "key-form": "The forms are closed at eight, and no other key form is read:",
}
#: Rules the vocabulary bullet states once for every shape.
VOCABULARY_RULES = {
    "what a sentence says": (
        "Each shape's sentence says what the shape reads and how that reading fails."
    ),
    "ATX headings at column 0": (
        "a heading is an ATX heading written at column 0 outside fenced code, so an "
        "indented line is never a heading;"
    ),
    "heading level and text": (
        "a declared heading with a level matches only at that level, and one without a "
        "level at any level, always by exact text;"
    ),
    "missing heading": "a declared heading that is missing fails the source as missing-heading,",
    "repeated heading": "and one that occurs more than once fails it as duplicate-key.",
    "several headings": (
        "When a list or table row declares more than one heading, the shape reads the "
        "section under each in the order declared, as it reads one section, and the items "
        "of all of them are that row's items."
    ),
    "heading-section at most two headings": (
        "A `heading-section` row declares at most two headings."
    ),
    "recognition left to the observer": (
        "How list markers, table rows, fenced code and TOML lines are recognized is shared "
        "by every project and left to the observer:"
    ),
}
#: How a grammar row names its key form.
KEY_FORM_RULES = {
    "stated by its sentence": (
        "A grammar row states its key form by carrying that form's sentence above, word "
        "for word, or, for `prefixed-ordinal`, by `<prefix>:<one-based ordinal>` with its "
        "prefix written in;"
    ),
    "names are labels": "the form names are this text's labels for those sentences.",
    "prefixed ordinal does not restart": (
        "When a row declares more than one heading, a `prefixed-ordinal` key counts "
        "the row's items across its sections in the order declared and does not "
        "restart at each heading."
    ),
}
#: The declared-item bullet: a class is read by its rule, made of rows, and
#: each class has one category.
DECLARED_ITEM_RULES = {
    "read by the class's rule": (
        "has one class from this closed set, read by that class's extraction rule (for a "
        "loaded profile, the class's grammar rows):"
    ),
    "no other item": "No other prose, heading, link or file mints an item.",
    "Heart and Soul classes": (
        "Each class belongs to one category: `project-account-section`, `principle`, "
        "`success-criterion` and `catalog-entry` to Heart and Soul;"
    ),
    "other categories": (
        "`design-contract` to Legends and Lore; `baseline-spec` to Spec and Spine; "
        "`topology-component` to Lay and Land; `craft-policy` to Craft and Care; and "
        "`roster-identity` to roster identity."
    ),
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
        "grammar written below, as a built-in default; no other project has a "
        "built-in default."
    ),
    "declared but unread is refused": (
        "A Butlers profile that is declared but that the observer does not read, "
        "for any reason, is treated as one the loader refuses,"
    ),
    "undeterminable declaration is refused": (
        "and so is a profile the observer cannot tell is or is not declared for "
        "Butlers."
    ),
    "refused profile does not fall back": (
        "A Butlers profile the loader refuses never returns Butlers to the built-in "
        "default."
    ),
    "project with no profile": (
        "A project other than Butlers with no loaded profile has no extraction rules: "
        "its classes' and categories' item denominators are Unknown, never zero, and "
        "no item is minted for it."
    ),
    "loaded profile is the only source": (
        "Once a project's profile is loaded, it is the only source of that "
        "project's extraction rules."
    ),
    "a class with no row": "A class that the loaded profile gives no row,",
    "a row outside the closed sets": (
        "or that has a row naming a shape or stating a key form outside these "
        "closed sets or lacking a parameter its shape or key form reads, or "
        "declaring more headings than its shape allows, is unreadable:"
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
        "denominator and every class's and category's item denominator is Unknown."
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
        "or, until a profile is declared for Butlers, the Butlers grammar "
        "written there"
    ),
    "body: one coverage state": (
        "Each admitted item SHALL be in exactly one coverage state: modeled, "
        "Unknown or contradicted."
    ),
    "body: unreadable source keeps identity": (
        "A source whose item population cannot be read SHALL retain its source "
        "identity while its item denominator renders Unknown."
    ),
    "label: case": "- **Case (sweep)**: enumerate the source population",
    "label: observable": "- **Observable**: per-category identities",
    "label: oracle": "- **Oracle**: two independent extractors",
    "label: oracle independence": "- **Oracle independence**: the expected denominator",
    "label: falsifier": "- **Falsifier**: the independent extractors disagree",
    "case: class with no row": "a loaded profile that gives one class no row,",
    "case: shape outside the vocabulary": (
        "a loaded profile with a row that names a shape outside the vocabulary,"
    ),
    "case: refused Butlers profile": "a Butlers profile the loader refuses,",
    "case: project with no profile": (
        "and a project other than Butlers with no loaded profile."
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
        "a loaded profile's missing or invalid rule is replaced by a built-in one,"
    ),
    "falsifier: refused profile falls back": (
        "a refused Butlers profile returns Butlers to the built-in grammar,"
    ),
    "falsifier: unreadable or refused class known": (
        "a class a loaded profile leaves unreadable, or any class of a Butlers "
        "profile that is refused or declared but unread, reports a known item "
        "denominator,"
    ),
    "falsifier: project with no profile": (
        "or a project other than Butlers with no loaded profile reports a known "
        "item denominator."
    ),
}
RETIRED_REQUIREMENT_TEXT = "declared item discovered by the closed extraction rule"
SCENARIOS = (
    "#### Scenario: Butlers' profile reproduces the written grammar",
    "#### Scenario: Loaded profile gives one class no row",
    "#### Scenario: Loaded profile names a shape outside the vocabulary",
    "#### Scenario: Refused or unread Butlers profile does not fall back",
    "#### Scenario: Project with no profile has Unknown item denominators",
)
#: Each added scenario, word for word; its rules below name what each clause
#: must keep.
SCENARIO_TEXT = {
    SCENARIOS[0]: (
        "- **WHEN** Butlers is observed through its loaded project profile\n"
        "- **THEN** each item is extracted through the container shape and item key\n"
        "  form its grammar row declares\n"
        "- **AND** the identities and D equal those produced by the grammar written in\n"
        "  these reader definitions\n"
    ),
    SCENARIOS[1]: (
        "- **WHEN** Butlers' loaded profile has no grammar row for one class\n"
        "- **THEN** that class's item denominator and its category's item denominator\n"
        "  render Unknown\n"
        "- **AND** every source stays in the source-path population and no built-in\n"
        "  rule reads the class\n"
    ),
    SCENARIOS[2]: (
        "- **WHEN** a grammar row in Butlers' loaded profile names a container shape or\n"
        "  item key form outside the closed sets\n"
        "- **THEN** that class's item denominator and its category's item denominator\n"
        "  render Unknown, and each source any of the class's rows names fails as a\n"
        "  source in which a class fails\n"
        "- **AND** no built-in or nearest shape reads the class in its place\n"
    ),
    SCENARIOS[3]: (
        "- **WHEN** a profile is declared for Butlers and the loader refuses it or the\n"
        "  observer does not read it\n"
        "- **THEN** every Butlers class's item denominator and its category's item\n"
        "  denominator render Unknown\n"
        "- **AND** every source stays in the source-path population and the grammar\n"
        "  written in these reader definitions reads no class\n"
    ),
    SCENARIOS[4]: (
        "- **WHEN** a project other than Butlers is observed with no loaded profile\n"
        "- **THEN** each of its classes' item denominators and each category's item\n"
        "  denominator render Unknown, never zero\n"
        "- **AND** no item is minted for it and the grammar written in these reader\n"
        "  definitions reads none of its classes\n"
    ),
}
SCENARIO_RULES = {
    SCENARIOS[0]: (
        "Butlers is observed through its loaded project profile",
        "each item is extracted through the container shape and item key form "
        "its grammar row declares",
        "the identities and D equal those produced by the grammar written in "
        "these reader definitions",
    ),
    SCENARIOS[1]: (
        "Butlers' loaded profile has no grammar row for one class",
        "that class's item denominator and its category's item denominator "
        "render Unknown",
        "every source stays in the source-path population and no built-in rule "
        "reads the class",
    ),
    SCENARIOS[2]: (
        "a grammar row in Butlers' loaded profile names a container shape or item "
        "key form outside the closed sets",
        "that class's item denominator and its category's item denominator "
        "render Unknown",
        "each source any of the class's rows names fails as a source in which a "
        "class fails",
        "no built-in or nearest shape reads the class in its place",
    ),
    SCENARIOS[3]: (
        "a profile is declared for Butlers and the loader refuses it or the "
        "observer does not read it",
        "every Butlers class's item denominator and its category's item "
        "denominator render Unknown",
        "every source stays in the source-path population and the grammar "
        "written in these reader definitions reads no class",
    ),
    SCENARIOS[4]: (
        "a project other than Butlers is observed with no loaded profile",
        "each of its classes' item denominators and each category's item "
        "denominator render Unknown, never zero",
        "no item is minted for it and the grammar written in these reader "
        "definitions reads none of its classes",
    ),
}
# The rule tables above name which rule a drifted paragraph or scenario
# breaks; they are not the guard on the bytes (SPEC_EDITS below is). Their
# digest is pinned so that a rule weakened, dropped or added in one place
# fails the selftest instead of passing with its own derived mutant.
RULE_TABLES_SHA256 = "b655c861078327f168ef337127e01f46962fd3404ff062419c4f22be91ae3031"
# The selftest's total, fixed so that a rule removed from any table above
# fails the selftest instead of lowering its count.
EXPECTED_KILLED = 196
# The whole proposed spec.md, pinned by construction: it must equal the
# current spec.md with each (anchor, replacement) pair applied once, and every
# other byte of the file unchanged. Each anchor must occur exactly once in the
# current spec.md. This is what holds every requirement, scenario and source
# population rule this package does not amend to its current bytes.
SPEC_EDITS = (
    (
        (
            '  `MANIFESTO.md` when present. Narrative links do not recurse.\n'
            '- A **declared item** has one class from this closed set and one extraction rule:\n'
            '  `project-account-section` uses the six keys purpose, promises, refusals,\n'
        ),
        (
            '  `MANIFESTO.md` when present. Narrative links do not recurse.\n'
            "- A **declared item** has one class from this closed set, read by that class's\n"
            "  extraction rule (for a loaded profile, the class's grammar rows):\n"
            '  `project-account-section` uses the six keys purpose, promises, refusals,\n'
        ),
    ),
    (
        (
            '  `roster-identity` uses each top-level roster directory containing\n'
            '  butler.toml. No other prose, heading, link or file mints an item.\n'
            '- Stable item identity is `(item class, declared key)`. Repository-relative path\n'
        ),
        (
            '  `roster-identity` uses each top-level roster directory containing\n'
            '  butler.toml. No other prose, heading, link or file mints an item. Each class\n'
            '  belongs to one category: `project-account-section`, `principle`,\n'
            '  `success-criterion` and `catalog-entry` to Heart and Soul; `design-contract`\n'
            '  to Legends and Lore; `baseline-spec` to Spec and Spine; `topology-component`\n'
            '  to Lay and Land; `craft-policy` to Craft and Care; and `roster-identity` to\n'
            '  roster identity.\n'
            '- Stable item identity is `(item class, declared key)`. Repository-relative path\n'
        ),
    ),
    (
        (
            '  one class is a contradiction rather than a path-based disambiguation.\n'
            '- The extraction grammar is literal:\n'
            '  - `project-account-section` mints exactly six aggregate keys: purpose from\n'
        ),
        (
            '  one class is a contradiction rather than a path-based disambiguation.\n'
            '- A **container shape** is how the items of one grammar row sit inside its\n'
            '  source. The vocabulary is closed at nine shapes, and no other shape is read.\n'
            "  Each shape's sentence says what the shape reads and how that reading fails.\n"
            '  Rules every shape shares are stated once here: a heading is an ATX heading\n'
            '  written at column 0 outside fenced code, so an indented line is never a\n'
            '  heading; a declared heading with a level matches only at that level, and one\n'
            '  without a level at any level, always by exact text; a declared heading that\n'
            '  is missing fails the source as missing-heading, and one that occurs more\n'
            '  than once fails it as duplicate-key. When a list or table row declares more\n'
            '  than one heading, the shape reads the section under each in the order\n'
            '  declared, as it reads one section, and the items of all of them are that\n'
            "  row's items. A `heading-section` row declares at most two headings. How list\n"
            '  markers, table rows, fenced code and TOML lines are recognized is shared by\n'
            '  every project and left to the observer:\n'
            '  - `heading-section`: the body under the declared heading: the lines after it\n'
            '    up to the next heading at the same or a higher level, with outer\n'
            '    whitespace trimmed, NFC-normalized; the body may be empty; when a row\n'
            "    declares two headings the item's text is the first heading's text, a blank\n"
            "    line, its body, a blank line, the second heading's text, a blank line and\n"
            '    its body, with outer whitespace trimmed.\n'
            '  - `every-level-2-section`: every level-2 heading in the file, in file order;\n'
            "    each part is the heading's text, a blank line and its body read as\n"
            '    heading-section reads it, with outer whitespace trimmed, and the parts are\n'
            '    joined by one blank line; a file with no level-2 heading fails the source\n'
            '    as missing-heading.\n'
            '  - `top-level-decimal-list`: each list item at column 0 in the section, which\n'
            '    must be numbered: a decimal number followed by . or ) and a space or tab;\n'
            '    a bulleted item at column 0 fails the source as malformed-list, and so\n'
            '    does a section with no list item at column 0.\n'
            '  - `top-level-list`: each list item at column 0 in the section, numbered or\n'
            '    bulleted; a section with no list item at column 0 fails the source as\n'
            '    malformed-list.\n'
            '  - `top-level-bulleted-list`: each list item at column 0 in the section,\n'
            '    which must be bulleted: a numbered item at column 0 fails the source as\n'
            '    malformed-list; a section with no list item yields no items and does not\n'
            '    fail.\n'
            '  - `first-table-rows`: each body row of the first table in the section; a\n'
            '    section with no table fails the source as malformed-row, and so does a\n'
            "    body row of that table whose cell count differs from its header's; later\n"
            '    tables in the section are not read.\n'
            '  - `ordinal-section-table-rows`: each body row of every table in the section\n'
            '    of every level-2 heading whose text opens with a decimal number,\n'
            '    optionally one lowercase letter, and then the end of the text or a\n'
            '    character that is not an ASCII letter, digit or underscore; a file with no\n'
            '    such heading fails the source as missing-heading, and a body row whose\n'
            "    cell count differs from its table's header fails it as malformed-row.\n"
            '  - `tree-path`: the Git tree path itself, matched against the tree\n'
            "    population's `pathPattern`; no body is read and nothing fails.\n"
            '  - `toml-table-field`: the declared field of the declared TOML table: exactly\n'
            '    one header line must name the table, and inside it the field must be\n'
            '    written once as `field = "value"` or `field = \'value\'` with a non-empty\n'
            '    value; no such table, a repeated table, a repeated field or a missing or\n'
            '    empty value fails the source as malformed-toml; a line in any other form,\n'
            '    and the field inside any other table, is not read; an array-of-tables\n'
            '    header such as `[[other]]` is a line in another form, so it neither opens\n'
            '    a table nor ends the declared one; the value is trimmed and\n'
            '    NFC-normalized, a backslash escape in a double-quoted value is not\n'
            "    decoded, and the value becomes the item's context.\n"
            "- An **item key form** says what becomes an item's key and how a key fails.\n"
            '  The forms are closed at eight, and no other key form is read:\n'
            '  - `fixed`: the fixed key.\n'
            "  - `leading-bold`: the item's leading bold span (`**` or `__`),\n"
            '    NFC-normalized with whitespace runs collapsed; an item with no non-empty\n'
            '    leading bold span fails the source as ambiguous-leading-label.\n'
            "  - `leading-bold-or-code`: the item's leading bold span, or else its leading\n"
            '    code span, NFC-normalized with whitespace runs collapsed; the span must be\n'
            '    non-empty and followed, after optional whitespace, by a hyphen-minus, en\n'
            '    dash or em dash, or the source fails as ambiguous-leading-label; each\n'
            "    item's context is the text of the declared heading it was read under.\n"
            '  - `prefixed-ordinal`: `<prefix>:<one-based ordinal>`, with the prefix the\n'
            '    grammar row declares.\n'
            '  - `first-cell-link-text`: the link text of the first cell, trimmed and\n'
            '    NFC-normalized; the cell must be one whole link `[text](target)`,\n'
            '    optionally with a space or tab and a title in double quotes after the\n'
            '    target, with non-empty text, or the source fails as malformed-row.\n'
            "  - `tree-key`: the `<key>` segment of the tree population's `pathPattern`.\n"
            "  - `ordinal-and-label`: the heading's ordinal, a colon and the first cell's\n"
            '    label; the first cell must be exactly one bold span with a non-empty\n'
            "    label, or the source fails as malformed-row; each item's context is the\n"
            "    heading's ordinal.\n"
            '  - `link-target-basename`: the basename of the link target in the declared\n'
            '    column, without its fragment; a table with no such column, or a cell in it\n'
            '    that is not one whole link whose target has a non-empty last segment,\n'
            '    fails the source as malformed-row.\n'
            '  A key that occurs twice within one class of one source fails the source as\n'
            "  duplicate-key. A grammar row states its key form by carrying that form's\n"
            '  sentence above, word for word, or, for `prefixed-ordinal`, by\n'
            '  `<prefix>:<one-based ordinal>` with its prefix written in; the form names\n'
            "  are this text's labels for those sentences. When a row declares more than\n"
            "  one heading, a `prefixed-ordinal` key counts the row's items across its\n"
            '  sections in the order declared and does not restart at each heading.\n'
            "- The **project profile** declares a project's extraction grammar as grammar\n"
            "  rows, and is carried in the project-shape observer's owner-adopted registry\n"
            '  entry. Each class above has one or more rows. Each row names its class and\n'
            '  its source; the heading or headings, each with its level when it has one and\n'
            '  its exact text, or the tree population that locate it, when its shape reads\n'
            '  one; every parameter its shape or key form reads, such as a table column, a\n'
            '  TOML table and field or a key prefix; exactly one container shape; and\n'
            '  exactly one item key form. A tree population is declared by a path pattern,\n'
            '  `pathPattern`, whose one `<key>` segment is a single directory name. A\n'
            '  profile cannot add a class, a shape or a key form.\n'
            '- Until a profile is declared for Butlers, the observer reads Butlers by the\n'
            '  grammar written below, as a built-in default; no other project has a\n'
            '  built-in default. A Butlers profile that is declared but that the observer\n'
            '  does not read, for any reason, is treated as one the loader refuses, and so\n'
            '  is a profile the observer cannot tell is or is not declared for Butlers. A\n'
            '  Butlers profile the loader refuses never returns Butlers to the built-in\n'
            '  default. A project other than Butlers with no loaded profile has no\n'
            "  extraction rules: its classes' and categories' item denominators are\n"
            "  Unknown, never zero, and no item is minted for it. Once a project's profile\n"
            "  is loaded, it is the only source of that project's extraction rules. A class\n"
            '  that the loaded profile gives no row, or that has a row naming a shape or\n'
            '  stating a key form outside these closed sets or lacking a parameter its\n'
            '  shape or key form reads, or declaring more headings than its shape allows,\n'
            "  is unreadable: its item denominator and its category's item denominator are\n"
            '  Unknown, each source any of its rows names fails as a source in which a\n'
            '  class fails, and every source stays in the source-path population. The\n'
            "  observer never substitutes a built-in rule for a loaded profile's missing or\n"
            '  invalid one. A loader that instead refuses the whole profile meets this rule\n'
            '  only if every source stays in the source-path population with an Unknown\n'
            "  item denominator and every class's and category's item denominator is\n"
            '  Unknown.\n'
            '- For every grammar, loaded or built-in, heading levels/text, top-level list\n'
            '  depth, table column counts, one-based ordinals and literal keys are exact.\n'
            '  Unicode is NFC-normalized; no case folding, stemming or punctuation\n'
            '  rewriting occurs. A missing heading, malformed row/list/TOML, unexpected\n'
            "  duplicate key or ambiguous leading label makes the enclosing source's item\n"
            '  denominator Unknown; it never produces a partial item set.\n'
            "- Butlers' profile declares exactly the following extraction grammar, which is\n"
            '  literal:\n'
            '  - `project-account-section` mints exactly six aggregate keys: purpose from\n'
        ),
    ),
    (
        (
            '    the directory is the key and the TOML `[butler].name` must be non-empty.\n'
            '  Heading levels/text, top-level list depth, table column counts, one-based\n'
            '  ordinals and literal keys are exact. Unicode is NFC-normalized; no case\n'
            '  folding, stemming or punctuation rewriting occurs. A missing heading,\n'
            '  malformed row/list/TOML, unexpected duplicate key or ambiguous leading label\n'
            "  makes the enclosing source's item denominator Unknown; it never produces a\n"
            '  partial item set.\n'
            '- The source-path denominator remains known through body-read failures. An\n'
        ),
        (
            '    the directory is the key and the TOML `[butler].name` must be non-empty.\n'
            '- The source-path denominator remains known through body-read failures. An\n'
        ),
    ),
    (
        (
            'For every lawfully admitted source body, Polaris SHALL account for each\n'
            'declared item discovered by the closed extraction rule across Heart and Soul,\n'
            'Legends and Lore, Spec and Spine, Lay and Land, Craft and Care and roster\n'
            'identity. Each admitted item SHALL be in exactly one coverage state: modeled,\n'
        ),
        (
            'For every lawfully admitted source body, Polaris SHALL account for each\n'
            'declared item discovered by the extraction grammar that governs its project\n'
            'under the reader definitions (the grammar rows of its loaded project profile,\n'
            'read only through the closed container shapes and item key forms, or, until\n'
            'a profile is declared for Butlers, the Butlers grammar written there)\n'
            'across Heart\n'
            'and Soul, Legends and Lore, Spec and Spine, Lay and Land, Craft and Care and roster\n'
            'identity. Each admitted item SHALL be in exactly one coverage state: modeled,\n'
        ),
    ),
    (
        (
            '  each readable category at one revision, then compare it to the model; include\n'
            '  an unreadable source case.\n'
            '- **Observable**: per-category identities and reconciling counts are visible in\n'
            '  the machine answer and reachable from Polaris.\n'
            '- **Oracle**: two independent extractors apply the literal grammar to the\n'
            '  revision-bound source population and must produce the same identities and D;\n'
            '  modeled + Unknown + contradicted equals D, with each identity appearing once;\n'
            '  malformed/unreadable sources carry an Unknown item denominator.\n'
            '- **Oracle independence**: the expected denominator is extracted from the\n'
        ),
        (
            '  each readable category at one revision, then compare it to the model; include\n'
            '  an unreadable source case, a loaded profile that gives one class no row, a\n'
            '  loaded profile with a row that names a shape outside the vocabulary, a\n'
            '  Butlers profile the loader refuses, and a project other than Butlers with no\n'
            '  loaded profile.\n'
            '- **Observable**: per-category identities and reconciling counts are visible in\n'
            '  the machine answer and reachable from Polaris.\n'
            '- **Oracle**: two independent extractors apply the literal grammar that\n'
            '  governs the project to the revision-bound source population and must produce\n'
            '  the same identities and D; for Butlers read through its loaded profile, both\n'
            '  also apply the grammar written in these reader definitions and must produce\n'
            '  the same identities and D; modeled + Unknown + contradicted equals D, with\n'
            '  each identity appearing once; malformed/unreadable sources, and every class\n'
            '  a loaded profile leaves unreadable, carry an Unknown item denominator.\n'
            '- **Oracle independence**: the expected denominator is extracted from the\n'
        ),
    ),
    (
        (
            '  a partial population, a known source disappears, an admitted item appears twice or\n'
            "  lacks a state, a known count does not reconcile, or an unavailable body's\n"
            '  item denominator is presented as known.\n'
            '\n'
        ),
        (
            '  a partial population, a known source disappears, an admitted item appears twice or\n'
            "  lacks a state, a known count does not reconcile, an unavailable body's\n"
            '  item denominator is presented as known, an item is read through a shape or\n'
            "  key form its governing grammar does not declare, a loaded profile's\n"
            '  missing or invalid rule is replaced by a built-in one, a refused Butlers\n'
            '  profile returns Butlers to the built-in grammar, a class a loaded profile\n'
            '  leaves unreadable, or any class of a Butlers profile that is refused or\n'
            '  declared but unread, reports a known item denominator, or a project other\n'
            '  than Butlers with no loaded profile reports a known item denominator.\n'
            '\n'
        ),
    ),
    (
        (
            '  sum to its denominator\n'
            '\n'
        ),
        (
            '  sum to its denominator\n'
            '\n'
            "#### Scenario: Butlers' profile reproduces the written grammar\n"
            '\n'
            '- **WHEN** Butlers is observed through its loaded project profile\n'
            '- **THEN** each item is extracted through the container shape and item key\n'
            '  form its grammar row declares\n'
            '- **AND** the identities and D equal those produced by the grammar written in\n'
            '  these reader definitions\n'
            '\n'
            '#### Scenario: Loaded profile gives one class no row\n'
            '\n'
            "- **WHEN** Butlers' loaded profile has no grammar row for one class\n"
            "- **THEN** that class's item denominator and its category's item denominator\n"
            '  render Unknown\n'
            '- **AND** every source stays in the source-path population and no built-in\n'
            '  rule reads the class\n'
            '\n'
            '#### Scenario: Loaded profile names a shape outside the vocabulary\n'
            '\n'
            "- **WHEN** a grammar row in Butlers' loaded profile names a container shape or\n"
            '  item key form outside the closed sets\n'
            "- **THEN** that class's item denominator and its category's item denominator\n"
            "  render Unknown, and each source any of the class's rows names fails as a\n"
            '  source in which a class fails\n'
            '- **AND** no built-in or nearest shape reads the class in its place\n'
            '\n'
            '#### Scenario: Refused or unread Butlers profile does not fall back\n'
            '\n'
            '- **WHEN** a profile is declared for Butlers and the loader refuses it or the\n'
            '  observer does not read it\n'
            "- **THEN** every Butlers class's item denominator and its category's item\n"
            '  denominator render Unknown\n'
            '- **AND** every source stays in the source-path population and the grammar\n'
            '  written in these reader definitions reads no class\n'
            '\n'
            '#### Scenario: Project with no profile has Unknown item denominators\n'
            '\n'
            '- **WHEN** a project other than Butlers is observed with no loaded profile\n'
            "- **THEN** each of its classes' item denominators and each category's item\n"
            '  denominator render Unknown, never zero\n'
            '- **AND** no item is minted for it and the grammar written in these reader\n'
            '  definitions reads none of its classes\n'
            '\n'
        ),
    ),
)
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


def shared_digest(shapes: dict[str, str], key_forms: dict) -> str:
    """The digest `SHARED_TEXT_SHA256` pins, over this package's two tables."""
    ours = {form: sentence for form, sentence in key_forms.values() if form}
    return sha256(repr((shapes, ours)).encode())


def shared_text_findings(module: object | None = None) -> list[str]:
    """This package's sentences against `syzygy-dov.24`'s: always by the pinned
    digest, and sentence by sentence once that builder is in the tree."""
    findings: list[str] = []
    if shared_digest(SHAPES, KEY_FORMS) != SHARED_TEXT_SHA256:
        findings.append(
            f"shape and key-form sentences do not hash to syzygy-dov.24's at "
            f"{SHARED_TEXT_COMMIT}"
        )
    if module is None:
        if not (ROOT / "scripts" / f"{SHARED_TEXT}.py").is_file():
            return findings
        sys.path.insert(0, str(ROOT / "scripts"))
        module = __import__(SHARED_TEXT)
    if getattr(module, "SHAPES", None) != SHAPES:
        findings.append("shape sentences differ from the loaded-profile amendment's")
    theirs = getattr(module, "ITEM_KEY_SENTENCES", None) or {}
    ours = {form: sentence for form, sentence in KEY_FORMS.values() if form}
    if theirs != ours:
        findings.append("key-form sentences differ from the loaded-profile amendment's")
    return findings


def rule_tables_digest() -> str:
    tables = (
        SHAPES, KEY_FORMS, CLOSURES, VOCABULARY_RULES, KEY_FORM_RULES,
        DECLARED_ITEM_RULES, DUPLICATE_KEY, PROFILE_RULES, LOADED_RULES,
        REQUIREMENT_RULES, RETIRED_REQUIREMENT_TEXT, SCENARIOS, SCENARIO_TEXT,
        SCENARIO_RULES,
    )
    return sha256(repr(tables).encode("utf-8"))


def expected_spec(base: str) -> tuple[str | None, list[str]]:
    """The current spec with each SPEC_EDITS pair applied once."""
    findings: list[str] = []
    text = base
    for anchor, replacement in SPEC_EDITS:
        if base.count(anchor) != 1:
            findings.append(
                "current spec does not carry the pinned anchor exactly once: "
                f"{anchor.splitlines()[0]!r}"
            )
            continue
        text = text.replace(anchor, replacement, 1)
    if findings:
        return None, findings
    return text, []


def pin_findings(text: str, base: str) -> list[str]:
    want, findings = expected_spec(base)
    if want is None:
        return findings
    if text == want:
        return []
    got_lines, want_lines = text.splitlines(), want.splitlines()
    for number, (got, wanted) in enumerate(zip(got_lines, want_lines), 1):
        if got != wanted:
            break
    else:
        number = min(len(got_lines), len(want_lines)) + 1
        got = got_lines[number - 1] if number <= len(got_lines) else "<end>"
        wanted = want_lines[number - 1] if number <= len(want_lines) else "<end>"
    return [
        f"proposed spec differs from the pinned text at line {number}: "
        f"got {got!r}, want {wanted!r}"
    ]


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
    for label, rules in (
        ("vocabulary", VOCABULARY_RULES),
        ("key-form", KEY_FORM_RULES),
        ("profile", PROFILE_RULES),
        ("loaded-profile", LOADED_RULES),
    ):
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
    declared_at = block.find(DECLARED_ITEM_OPENING)
    declared_end = block.find(DECLARED_ITEM_END, declared_at)
    if declared_at < 0 or declared_end < 0 or text.count(DECLARED_ITEM_OPENING) != 1:
        findings.append("missing or duplicate declared-item bullet")
    else:
        folded = fold(block[declared_at:declared_end])
        for rule_label, rule in DECLARED_ITEM_RULES.items():
            if fold(rule) not in folded:
                findings.append(f"declared-item bullet lacks {rule_label}")
    tail = block[block.find(UNCHANGED_TAIL):] if UNCHANGED_TAIL in block else None
    base_block = current[current.find(READER_START):current.find(READER_END)]
    if tail is None or tail != base_block[base_block.find(UNCHANGED_TAIL):]:
        findings.append("the source-path denominator bullet differs from the current one")
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
    findings = pin_findings(text, base) + reader_findings(text, base)
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
        scenario = _block(section, heading)
        body = fold(scenario)
        for rule in SCENARIO_RULES[heading]:
            if fold(rule) not in body:
                findings.append(f"scenario lacks '{rule}': {heading}")
        if scenario != f"{heading}\n\n{SCENARIO_TEXT[heading]}\n":
            findings.append(f"scenario text differs: {heading}")
    base_start = base.find(REQUIREMENT)
    base_section = base[base_start:base.find(NEXT_REQUIREMENT, base_start)]
    base_warrants = base_section[base_section.find(WARRANTS):]
    if preceding < 0 or _block(section, PRECEDING_SCENARIO) != _block(base_section, PRECEDING_SCENARIO):
        findings.append("the first PWB-REQ-002 scenario differs from the current one")
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
    # A row digest corrupted with the path order kept: only the exact
    # comparison sees it.
    corrupted_row = baseline.replace(rows[0][0], "0" * 64, 1)
    if "manifest differs from exact regeneration over proposed bytes" not in (
        verify_manifest(corrupted_row, baseline)
    ):
        return _fail("corrupted manifest row digest passed")
    killed += 3

    # Patch population: dropping the capability patch.
    without = [p for p in patch_files() if p.name != "CAPABILITY-COVERAGE.md.patch"]
    population = population_findings(without)
    if (
        "proposed patch population differs from declared subjects" not in population
        or f"declared patched subject is unchanged: {CAPABILITY_COVERAGE}" not in population
    ):
        return _fail("dropped-patch mutation passed the population predicate")
    killed += 1
    # An extra patch that changes a subject no patch is declared to change.
    with tempfile.TemporaryDirectory() as scratch:
        design = CHANGE / "design.md"
        lines = current[design].decode("utf-8").splitlines()
        extra = pathlib.Path(scratch) / "design.md.patch"
        extra.write_text(
            f"diff --git a/{design.as_posix()} b/{design.as_posix()}\n"
            f"--- a/{design.as_posix()}\n+++ b/{design.as_posix()}\n"
            f"@@ -{len(lines)} +{len(lines)},2 @@\n {lines[-1]}\n+undeclared drift\n"
        )
        if f"undeclared subject change: {design}" not in population_findings(
            patch_files() + [extra]
        ):
            return _fail("undeclared subject change passed the population predicate")
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

    # Vocabulary, key-form, profile and loaded-profile bullets: each rule
    # removed on its own.
    openings = dict(BULLETS)
    for label, rules, following in (
        ("vocabulary", VOCABULARY_RULES, "key-form"),
        ("key-form", KEY_FORM_RULES, "profile"),
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

    # Declared-item bullet: each rule removed, and the rule made "any".
    at = spec.index(DECLARED_ITEM_OPENING)
    end = spec.index(DECLARED_ITEM_END, at)
    for rule_label, rule in DECLARED_ITEM_RULES.items():
        paragraph = fold(spec[at:end])
        mutated_paragraph = paragraph.replace(fold(rule), "[removed]", 1)
        if mutated_paragraph == paragraph:
            return _fail(f"declared-item fixture matched nothing: {rule_label}")
        mutated = spec[:at] + mutated_paragraph + "\n" + spec[end:]
        if not spec_mutant(rule_label, mutated, f"declared-item bullet lacks {rule_label}"):
            return _fail(f"declared-item rule mutation passed: {rule_label}")
        killed += 1
    widened = _replace_once(spec, "read by that class's\n  extraction rule", "read by any\n  extraction rule", "any rule")
    if not spec_mutant("any rule", widened, "declared-item bullet lacks read by the class's rule"):
        return _fail("declared-item 'any extraction rule' mutation passed")
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
        "source-path bullet altered": (
            _replace_once(spec, "denominator is Unknown, never copied",
                          "denominator is 0, never copied", "source-path"),
            "the source-path denominator bullet differs from the current one",
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

    # Clauses a reviewer mutated in round 2: the requirement's SHALL and its
    # falsifier label.
    for name, old, new, expected in (
        ("SHALL made MAY", "Each admitted item SHALL be", "Each admitted item MAY be",
         "PWB-REQ-002 lacks body: one coverage state"),
        ("falsifier relabelled", "- **Falsifier**: the independent",
         "- **Non-falsifier**: the independent", "PWB-REQ-002 lacks label: falsifier"),
    ):
        if not spec_mutant(name, _replace_once(spec, old, new, name), expected):
            return _fail(f"{name} mutation passed")
        killed += 1

    # Scenario clauses a reviewer mutated in round 2, each with its checked
    # phrase kept, and the unchanged first scenario.
    for name, old, new, heading in (
        ("any project observed", "- **WHEN** Butlers is observed through",
         "- **WHEN** any project is observed through", SCENARIOS[0]),
        ("WHEN negated", "- **WHEN** Butlers' loaded profile has no grammar row for one class",
         "- **WHEN** not (Butlers' loaded profile has no grammar row for one class)", SCENARIOS[1]),
        ("THEN excepted", "  source in which a class fails\n- **AND** no built-in",
         "  source in which a class fails, except that the source leaves the source-path\n"
         "  population\n- **AND** no built-in", SCENARIOS[2]),
    ):
        mutated = _replace_once(spec, old, new, name)
        if not spec_mutant(name, mutated, f"scenario text differs: {heading}"):
            return _fail(f"{name} scenario mutation passed")
        killed += 1
    first_scenario = _replace_once(
        spec, "- **THEN** Polaris accounts for all D items exactly once",
        "- **THEN** Polaris accounts for most D items exactly once", "first scenario",
    )
    if not spec_mutant("first scenario", first_scenario,
                       "the first PWB-REQ-002 scenario differs from the current one"):
        return _fail("first scenario mutation passed")
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
            "   each readable category at one revision, then compare it to the model; include",
            "   each known category at one revision, then compare it to the model; include",
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

    # The whole-spec pin: text this package does not amend, each changed on
    # its own. The round-3 reviewer's mutants passed every rule above; the
    # PWB-REQ-001 title is one more.
    unamended = {
        "oracle 'malformed/unreadable'": ("malformed/unreadable sources,", "malformed sources,"),
        "oracle 'modeled + Unknown + contradicted'": (
            "modeled + Unknown + contradicted equals D", "modeled + Unknown equals D"),
        "oracle 'revision-bound'": (
            "governs the project to the revision-bound source population",
            "governs the project to the source population"),
        "oracle independence 'not from'": (
            "  source files, not from the POC's coverage object.",
            "  source files, or from the POC's coverage object."),
        "observable 'Polaris'": (
            "- **Observable**: per-category identities and reconciling counts are visible in",
            "- **Observable**: per-category identities and reconciling counts are kept in"),
        "Form invariant": (
            "Group: Coverage. Form: **invariant**.\n\nFor every lawfully admitted",
            "Group: Coverage. Form: **guideline**.\n\nFor every lawfully admitted"),
        "body category list": (
            "and Soul, Legends and Lore, Spec and Spine, Lay and Land, Craft and Care and roster",
            "and Soul, Legends and Lore, Spec and Spine, Lay and Land and roster"),
        "PWB-REQ-002 title": (
            "### Requirement: PWB-REQ-002 — Every declared project-shape item is accounted for",
            "### Requirement: PWB-REQ-002 — Most declared project-shape items are accounted for"),
        "case 'one revision'": (
            "  each readable category at one revision, then compare it to the model; include",
            "  each readable category at any revision, then compare it to the model; include"),
        "case 'unreadable source case'": (
            "  an unreadable source case, a loaded profile", "  a loaded profile"),
        "falsifier 'partial population'": (
            "  a partial population, a known source disappears,", "  a known source disappears,"),
        "falsifier 'unavailable body'": (
            "an unavailable body's", "an available body's"),
        "PWB-REQ-003 SHALL NOT made MAY": (
            "The POC SHALL NOT shrink the source-path denominator",
            "The POC MAY shrink the source-path denominator"),
        "source population 'do not recurse'": (
            "Narrative links do not recurse.", "Narrative links recurse."),
        "PWB-REQ-001 title": (
            "is revision-bound and explicitly scoped", "is explicitly scoped"),
    }
    for name, (old, new) in unamended.items():
        mutated = _replace_once(spec, old, new, name)
        if not any(
            f.startswith("proposed spec differs from the pinned text")
            for f in requirement_findings(mutated.encode())
        ):
            return _fail(f"unamended-text mutation passed the spec pin: {name}")
        killed += 1
    third = _block(spec, SCENARIOS[1])
    fourth = _block(spec, SCENARIOS[2])
    swapped = spec.replace(third + fourth, fourth + third, 1)
    if swapped == spec or not any(
        f.startswith("proposed spec differs from the pinned text")
        for f in requirement_findings(swapped.encode())
    ):
        return _fail("scenario order swap passed the spec pin")
    killed += 1
    # Round 3's R-C: the falsifier unscoped again fires on Butlers' interim
    # default, and both the pin and the rule refuse it.
    unscoped = _replace_once(
        spec,
        "or a project other\n  than Butlers with no loaded profile reports",
        "or a project with no\n  profile reports",
        "unscoped falsifier",
    )
    found = requirement_findings(unscoped.encode())
    if "PWB-REQ-002 lacks falsifier: project with no profile" not in found or not any(
        f.startswith("proposed spec differs from the pinned text") for f in found
    ):
        return _fail("unscoped falsifier passed")
    killed += 1
    # Each pinned anchor drifted in the current spec.
    base_text = current[SPEC].decode("utf-8")
    for anchor, _ in SPEC_EDITS:
        at = base_text.index(anchor)
        drifted = (base_text[:at + 1] + "~" + base_text[at + 1:]).encode()
        expected = (
            "current spec does not carry the pinned anchor exactly once: "
            f"{anchor.splitlines()[0]!r}"
        )
        if expected not in requirement_findings(proposed[SPEC], drifted):
            return _fail(f"drifted anchor passed: {anchor.splitlines()[0]}")
        killed += 1
    # Each pinned anchor present twice: "exactly once" refuses a duplicate,
    # not only an absence.
    for anchor, _ in SPEC_EDITS:
        doubled = (base_text + anchor).encode()
        expected = (
            "current spec does not carry the pinned anchor exactly once: "
            f"{anchor.splitlines()[0]!r}"
        )
        if expected not in requirement_findings(proposed[SPEC], doubled):
            return _fail(f"duplicated anchor passed: {anchor.splitlines()[0]}")
        killed += 1

    # check() itself: its manifest comparison and its shared-text digest are
    # wired in, not only correct as functions.
    global MANIFEST_OUT, SHARED_TEXT_SHA256
    kept_manifest, kept_digest = MANIFEST_OUT, SHARED_TEXT_SHA256
    with tempfile.TemporaryDirectory() as scratch:
        stale = pathlib.Path(scratch) / "manifest.txt"
        stale.write_text(baseline.replace(rows[0][0], "0" * 64, 1))
        MANIFEST_OUT = stale
        try:
            found = check()
        finally:
            MANIFEST_OUT = kept_manifest
    if "manifest differs from exact regeneration over proposed bytes" not in found:
        return _fail("check() passed a corrupted manifest")
    killed += 1
    SHARED_TEXT_SHA256 = "0" * 64
    try:
        found = check()
    finally:
        SHARED_TEXT_SHA256 = kept_digest
    if (
        "shape and key-form sentences do not hash to syzygy-dov.24's at "
        f"{SHARED_TEXT_COMMIT}"
    ) not in found:
        return _fail("check() passed without the shared-text digest")
    killed += 1

    # The shared sentences drifted on both sides at once: the sentence
    # comparison agrees, and only the pinned dov.24 digest refuses it.
    key = next(iter(SHAPES))
    original_sentence = SHAPES[key]
    SHAPES[key] = original_sentence + " [changed]"
    try:
        module = Module()
        module.SHAPES = dict(SHAPES)
        module.ITEM_KEY_SENTENCES = {form: s for form, s in KEY_FORMS.values() if form}
        found = shared_text_findings(module)
    finally:
        SHAPES[key] = original_sentence
    if found != [
        "shape and key-form sentences do not hash to syzygy-dov.24's at "
        f"{SHARED_TEXT_COMMIT}"
    ]:
        return _fail("shared-text drift on both sides passed the pinned digest")
    killed += 1

    if composition_findings():
        return _fail("sibling composition does not verify")
    if rule_tables_digest() != RULE_TABLES_SHA256:
        return _fail("rule tables changed without their pinned digest")
    if killed != EXPECTED_KILLED:
        return _fail(f"{killed} mutants killed, expected {EXPECTED_KILLED}")
    print(
        f"selftest: {killed} mutants killed — stale manifest, path order, a "
        "corrupted row digest, patch population, an undeclared subject change, "
        f"{len(SHAPES)} shape and {len(KEY_FORMS)} key-form "
        "sentences, entry dropped/added/moved and closure for each vocabulary, "
        f"the duplicate-key rule, {len(VOCABULARY_RULES)} vocabulary, "
        f"{len(KEY_FORM_RULES)} key-form, {len(PROFILE_RULES)} profile and "
        f"{len(LOADED_RULES)} loaded-profile rules, {len(DECLARED_ITEM_RULES)} "
        "declared-item rules and the rule made 'any', the source-path bullet, "
        "shared-text drift on either vocabulary and on both packages at once, "
        f"the whole-spec pin over {len(unamended)} unamended clauses, a "
        f"scenario swap, the unscoped falsifier, {len(SPEC_EDITS)} drifted and "
        f"{len(SPEC_EDITS)} duplicated anchors, check() without its manifest "
        "comparison or its shared-text digest, bullet order/duplicate/missing, retired opening, the "
        "hoisted exactness paragraph reworded or left behind, Butlers grammar "
        f"drift, {len(REQUIREMENT_RULES)} PWB-REQ-002 rules, retired "
        f"requirement text, SHALL made MAY, the falsifier relabelled, three "
        "scenario clauses and the first scenario altered, "
        f"{len(SCENARIOS)} scenarios x missing/duplicate/"
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
            f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); the whole spec "
            f"equals the current spec with {len(SPEC_EDITS)} pinned edits; {len(SHAPES)} "
            f"shapes, {len(KEY_FORMS)} key forms, {len(VOCABULARY_RULES)} "
            f"vocabulary, {len(KEY_FORM_RULES)} key-form, {len(PROFILE_RULES)} "
            f"profile, {len(LOADED_RULES)} loaded-profile and "
            f"{len(DECLARED_ITEM_RULES)} declared-item rules, the hoisted "
            f"exactness bullet, the unchanged source-path bullet, "
            f"{len(REQUIREMENT_RULES)} PWB-REQ-002 rules, {len(SCENARIOS)} "
            "scenarios word for word, the unchanged first scenario, the retained "
            "Butlers grammar, dependency "
            "and contract-coverage regeneration and "
            f"{len(DECLARED_COMPOSITION)} declared sibling-composition outcomes verify"
        )
        if (ROOT / "scripts" / f"{SHARED_TEXT}.py").is_file():
            print(
                "shape and key-form sentences hash to syzygy-dov.24's at "
                f"{SHARED_TEXT_COMMIT} and match the loaded-profile amendment's builder"
            )
        else:
            print(
                "shape and key-form sentences hash to syzygy-dov.24's at "
                f"{SHARED_TEXT_COMMIT}; scripts/{SHARED_TEXT}.py is not in this "
                "tree, so they are compared sentence by sentence only once it lands"
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
