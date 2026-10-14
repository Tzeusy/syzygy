#!/usr/bin/env python3
"""Build and verify the inert PWB opening-index amendment candidate.

The amendment adds an opening index with mechanical reach offsets to
PWB-REQ-010 (bead ``syzygy-u05.12``, slice A, register row P-98): nine rows,
one per PWB-REQ-021 answer identity, each routed to a target the requirement
declares, each showing the word offset at which that target begins, and one
structural stopping line. The offsets are presentation measurements, never a
verdict, a claim or a walkthrough fact (RFC7-31). The engine and its modes
live in ``scripts/pwb_requirement_amendment.py``; this file declares only
what this amendment must say.

Beyond the engine's structure checks, ``--check`` requires the index table's
identity column to equal, in order, the nine identities PWB-REQ-021 lists in
the same proposed specification bytes, and each replaced signed line to be
extended in its own position.
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pwb_requirement_amendment as engine  # noqa: E402

INDEX_ROW_RE = re.compile(r"^  \| `([a-z0-9-]+)` \| ([^|\n]+) \| ([^|\n]+) \|$", re.MULTILINE)
NINE_RE = re.compile(r"nine identities: (.*?)\.\n", re.DOTALL)


def index_findings(spec: str, block: str) -> list[str]:
    _, blocks = engine.requirement_blocks(spec)
    nine = NINE_RE.search(dict(blocks)["PWB-REQ-021"])
    if nine is None:
        return ["PWB-REQ-021's nine identities cannot be read"]
    identities = re.findall(r"`([a-z0-9-]+)`", nine.group(1))
    rows = INDEX_ROW_RE.findall(block)
    if [identity for identity, _, _ in rows] != identities or len(identities) != 9:
        return ["the opening index rows differ from PWB-REQ-021's nine identities in order"]
    if any(not name.strip() or not target.strip() for _, name, target in rows):
        return ["an opening index row has an empty name or target"]
    return []


def position_findings(block: str) -> list[str]:
    """Each replaced signed line is extended where it stood, not elsewhere.

    The engine asks only that some line of the block open with a replaced
    line's signed stem. Here the line that follows the replaced line's signed
    predecessor must be the one that does (round-2 review, finding 8).
    """
    rid = AMENDMENT.requirement
    current = engine.read_subjects()[engine.SPEC].decode("utf-8")
    old = dict(engine.requirement_blocks(current)[1])[rid].split("\n")
    new = block.split("\n")
    findings = []
    for line in AMENDMENT.replaced:
        before = old[old.index(line) - 1]
        if new.count(before) != 1:
            findings.append(f"signed {rid} predecessor of a replaced line is not unique: {before!r}")
        elif not new[new.index(before) + 1].startswith(line.rstrip(".")):
            findings.append(f"signed {rid} replaced line not extended in its own position: {line!r}")
    return findings


def extra_findings(spec: str, block: str) -> list[str]:
    return index_findings(spec, block) + position_findings(block)


AMENDMENT = engine.Amendment(
    candidate="pwb-opening-index-amendment",
    manifest="PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt",
    title="PWB OPENING-INDEX AMENDMENT MANIFEST",
    label="opening-index",
    requirement="PWB-REQ-010",
    required_once=(
        "The first reading level SHALL begin with an index of exactly nine rows, one for each PWB-REQ-021 answer identity, in the order and to the targets this table declares.",
        "No run, reader or model decides a row's target.",
        '| `why` | purpose | the purpose statements |',
        '| `promises` | promises | the promise statements |',
        '| `refusals-and-rule` | non-goals | the non-goal statements |',
        '| `capabilities-and-fit` | capabilities | the capability catalog |',
        "| `exact-requirement` | exact requirements | the first link, in document order, to an exact requirement's text |",
        '| `unknown-or-contradiction` | gaps | the opening Unknown aggregate |',
        '| `claim-strength` | claim strength | the legend naming each epistemic label, tier and freshness state |',
        '| `architecture-and-groups` | architecture | the architecture statements |',
        '| `v1-success` | V1 success | the V1 scope and success-criteria statements |',
        "Each row shows its declared row name and routes to the first element of its target: the target's heading when it has one, otherwise its first element in document order.",
        "Row names are `action-label` strings; each offset and the stopping line is a `scope-instruction` string; the text of a row whose target is not rendered is an `epistemic-disclosure`.",
        "whose limit of one entry `scope-instruction` counts only the statement of the POC bound.",
        "The index precedes the PWB-REQ-014 narrative tree and is not one of its narrative units.",
        "A row whose target is not rendered at that evaluation SHALL say so and route nowhere; it SHALL NOT route to a substitute.",
        "Each row whose target is rendered SHALL show the word offset at which its target begins: the number of counted words that precede the target's first element in document order.",
        "A row whose target is not rendered shows no offset.",
        "Exactly one stopping line SHALL stand immediately after the first element of the target whose offset is largest, and give that largest offset and the page's word total, and nothing else about the index.",
        "Where two targets share the largest offset, the stopping line follows the one whose first element comes later in document order.",
        "Where that element lies inside a `details` element closed on first load, the line stands immediately after the outermost such `details` element instead.",
        "Where no indexed target is rendered, the line stands immediately after the index and gives only the word total.",
        "over the document as the browser holds it after load, with every `details` element in its first-load state, at the one viewport width and height the oracle declares and publishes with its result.",
        "A word is a maximal run of non-whitespace characters in a text node, counted in document order from the start of the body.",
        "Excluded from the count: text inside `script`, `style`, `template` and `noscript` elements; inside any element with the `hidden` attribute, `aria-hidden=\"true\"` or a computed `display: none`; any text node whose parent element's computed `visibility` is not `visible`; inside a `details` element closed on first load, except its `summary`, which counts; and the index rows and stopping line themselves.",
        "The total counts the same population over the whole body.",
        "They carry no epistemic tuple, enter no PWB-REQ-020 parity family and no PWB-REQ-021 record or readiness arm, and SHALL NOT state or imply that any prompt is, or can be, answered: the walkthrough verdict stays the owner's (RFC7-31).",
        "[Unknown] Which offsets and total Butlers' Polaris would show today: no current figure is quoted here.",
        "an independent word counter applies the declared method to the document after load and recomputes every row offset and the total",
        "each row's name and target are compared with this requirement's table, never with the renderer's own mapping;",
        "exactly one stopping line must stand where this requirement places it and carry the largest recomputed offset.",
        "located by a recognizer whose selectors are published with the oracle and key only on visible heading text, on claim identities the machine answer serves and on the PWB-REQ-011 exact-source route form, never on an attribute, class or identifier the renderer emits to mark an index target;",
        "the stopping line is missing, repeated or misplaced, or its offset is not the largest;",
        "expected offsets come from a word counter that shares no code with the renderer.",
        "an index row is missing, duplicated, out of order, shows a name other than its declared row name or is routed to a target other than the declared one",
        "an unrendered target's row routes anywhere or shows an offset",
        "an offset or total differs from the independent count",
        "the stopping line states or implies that a prompt is answered",
        "an offset is presented as a claim, a parity fact or a walkthrough fact.",
        "each showing its declared row name, routing to its declared target and showing that target's word offset by the declared method",
        "exactly one stopping line stands immediately after the first element of the target whose offset is largest, giving that offset and the page's word total, and claims nothing about whether any prompt is answered",
        "the `gaps` row says its target is not rendered, shows no offset and routes nowhere",
        "each of the other eight rows still routes to its declared target and shows that target's word offset by the declared method",
    ),
    replaced=(
        "  more capability deep dives.",
        "  routes to the catalogs; capability detail is subordinate.",
        "  independently enumerated project-level fact set.",
        "  machine model, not the rendered page.",
        "  category, or requires reading a capability deep dive to learn what Butlers is.",
    ),
    kept_scenarios=(
        "#### Scenario: WhatsApp is a drill-down, not the project account",
        "#### Scenario: One opening Unknown aggregate, reconciled with members",
    ),
    new_scenarios=(
        "#### Scenario: The opening index shows where each project question's material begins",
        "#### Scenario: An unrendered index target is stated, not substituted",
    ),
    mutants=(
        ("substitute routing allowed",
         "it SHALL NOT route to a substitute.", "it MAY route to a substitute.",
         "PWB-REQ-010 carries 0 copies of required phrase: 'A row whose target"),
        ("run decides the target",
         "No run, reader or model decides a\n  row's target.", "A run may decide a\n  row's target.",
         "PWB-REQ-010 carries 0 copies of required phrase: \"No run, reader"),
        ("closed details counted",
         "; inside a\n    `details` element closed on first load, except its `summary`, which\n    counts", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Excluded from the count"),
        ("offset base dropped",
         "begins: the number of counted words that\n  precede the target's first element in document order.", "begins.",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Each row whose target is rendered"),
        ("second stopping line allowed",
         "Exactly one stopping line SHALL stand", "A stopping line SHALL stand",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Exactly one stopping line"),
        ("stopping-line placement falsifier dropped",
         "the stopping line is missing,\n  repeated or misplaced, or its offset is not the largest; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'the stopping line is missing"),
        ("index row target swapped",
         "| `why` | purpose | the purpose statements |", "| `why` | purpose | the capability catalog |",
         "PWB-REQ-010 carries 0 copies of required phrase: '| `why` | purpose"),
        ("verdict exclusion dropped",
         "and SHALL NOT state or\n    imply that any prompt is, or can be, answered", "and may state that a\n    prompt is answered",
         "PWB-REQ-010 carries 0 copies of required phrase: 'They carry no epistemic tuple"),
        ("parity family entered",
         "enter no PWB-REQ-020 parity\n    family", "enter the PWB-REQ-020 parity\n    family",
         "PWB-REQ-010 carries 0 copies of required phrase: 'They carry no epistemic tuple"),
        ("current figure quoted",
         "[Unknown] Which offsets and total", "[Observed] Which offsets and total",
         "PWB-REQ-010 carries 0 copies of required phrase: \"[Unknown] Which offsets"),
        ("oracle shares the renderer's mapping",
         "never with the renderer's own\n  mapping;", "or with the renderer's own\n  mapping;",
         "PWB-REQ-010 carries 0 copies of required phrase: \"each row's name and target"),
        ("stopping-line falsifier dropped",
         "the stopping line\n  states or implies that a prompt is answered; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'the stopping line states"),
        ("stopping line role dropped",
         "each offset and the stopping line\n    is a `scope-instruction` string; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Row names are"),
        ("row name left unchecked",
         "each row's name and target\n  are compared", "each row's target\n  is compared",
         "PWB-REQ-010 carries 0 copies of required phrase: \"each row's name and target"),
        ("recognizer keys on renderer markup",
         "never on an attribute, class or identifier the\n  renderer emits", "or on an attribute, class or identifier the\n  renderer emits",
         "PWB-REQ-010 carries 0 copies of required phrase: 'located by a recognizer"),
        ("unrendered row shows an offset",
         "A row whose target\n  is not rendered shows no offset.", "A row whose target\n  is not rendered shows offset zero.",
         "PWB-REQ-010 carries 0 copies of required phrase: 'A row whose target is not rendered shows no"),
        ("viewport left open",
         ", at the one viewport width and height the oracle\n    declares and publishes with its result", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'over the document as the browser"),
        ("visible descendant of a hidden element excluded",
         "any text node whose\n    parent element's computed `visibility` is not `visible`",
         "inside any element with a computed\n    `visibility: hidden`",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Excluded from the count"),
        ("largest-offset tie left open",
         "Where two targets share the largest offset, the stopping line follows\n    the one whose first element comes later in document order. ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Where two targets share"),
        ("row-name falsifier dropped",
         ", shows a name other than\n  its declared row name", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'an index row is missing"),
        ("scenario stopping line moved to the last indexed target",
         "- **AND** exactly one stopping line stands immediately after the first\n  element of the target whose offset is largest",
         "- **AND** exactly one stopping line follows the last indexed target",
         "PWB-REQ-010 carries 0 copies of required phrase: 'exactly one stopping line stands"),
        ("other rows may change targets",
         "- **AND** each of the other eight rows still routes to its declared target",
         "- **AND** each of the other eight rows may change its target",
         "PWB-REQ-010 carries 0 copies of required phrase: 'each of the other eight rows"),
        ("replaced line extended out of position",
         "and one or\n  more capability deep dives; separately,",
         "and one or\n  of them\n  more capability deep dives; separately,",
         "signed PWB-REQ-010 replaced line not extended in its own position"),
        ("index row reordered",
         "  | `why` | purpose | the purpose statements |\n  | `promises` | promises | the promise statements |\n",
         "  | `promises` | promises | the promise statements |\n  | `why` | purpose | the purpose statements |\n",
         "the opening index rows differ from PWB-REQ-021's nine identities in order"),
        ("index row dropped",
         "  | `v1-success` | V1 success | the V1 scope and success-criteria statements |\n", "",
         "the opening index rows differ from PWB-REQ-021's nine identities in order"),
        ("index row target emptied",
         "| claim strength | the legend naming each epistemic label, tier and freshness state |",
         "| claim strength |   |",
         "an opening index row has an empty name or target"),
        ("new scenario dropped",
         "#### Scenario: An unrendered index target is stated, not substituted\n",
         "#### Scenario: An unrendered index target\n",
         "PWB-REQ-010 lacks exactly one"),
        ("signed scenario dropped",
         "#### Scenario: WhatsApp is a drill-down, not the project account\n",
         "#### Scenario: WhatsApp is a drill-down\n",
         "PWB-REQ-010 lacks exactly one"),
    ),
    patch_drift=(
        "\n single capability's detail.", "\n one capability's detail."
    ),
    extra_findings=extra_findings,
)


if __name__ == "__main__":
    raise SystemExit(engine.main(AMENDMENT, sys.argv[1:]))
