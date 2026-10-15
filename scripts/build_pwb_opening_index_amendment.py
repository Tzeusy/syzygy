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


def position_findings(block: str, signed_block: str | None = None) -> list[str]:
    """Each replaced signed line is extended where it stood, not elsewhere.

    The engine asks only that some line of the block open with a replaced
    line's signed stem. Here the line that follows the replaced line's signed
    predecessor must be the one that does (round-2 review, finding 8). Every
    way this can fail is a named finding, never an exception (round-3
    review, finding 9): a replaced line missing from the signed block, a
    predecessor absent from or repeated in the proposed block, and a
    predecessor with no line after it.
    """
    rid = AMENDMENT.requirement
    if signed_block is None:
        current = engine.read_subjects()[engine.SPEC].decode("utf-8")
        signed_block = dict(engine.requirement_blocks(current)[1])[rid]
    old = signed_block.split("\n")
    new = block.split("\n")
    findings = []
    for line in AMENDMENT.replaced:
        if old.count(line) != 1 or old.index(line) == 0:
            findings.append(f"signed {rid} replaced line is not once in the signed block, after a predecessor: {line!r}")
            continue
        before = old[old.index(line) - 1]
        copies = new.count(before)
        if copies == 0:
            findings.append(f"signed {rid} predecessor of a replaced line is absent: {before!r}")
        elif copies > 1:
            findings.append(f"signed {rid} predecessor of a replaced line is not unique: {before!r}")
        elif new.index(before) + 1 >= len(new) or not new[new.index(before) + 1].startswith(line.rstrip(".")):
            findings.append(f"signed {rid} replaced line not extended in its own position: {line!r}")
    return findings


def position_selftest() -> int:
    """Rule-6 fixtures for the paths a proposed-spec mutant cannot reach.

    The engine's mutants edit only the proposed bytes, so a replaced line
    that has left the signed block, as after a sibling sign-off rewrites the
    requirement, is exercised here over a synthetic signed block.
    """
    first = AMENDMENT.replaced[0]
    signed = f"head\npred\n{first}\ntail"
    cases = (
        ("replaced line gone from the signed block", "head\npred\ntail", "x",
         "replaced line is not once in the signed block"),
        ("predecessor absent", signed, f"head\n{first}\ntail",
         "predecessor of a replaced line is absent"),
        ("predecessor repeated", signed, f"pred\npred\n{first}\ntail",
         "predecessor of a replaced line is not unique"),
        ("predecessor is the last line", signed, "head\npred",
         "replaced line not extended in its own position"),
    )
    failed = 0
    for name, signed_block, block, expected in cases:
        findings = position_findings(block, signed_block)
        if not any(expected in finding for finding in findings):
            print(f"SELFTEST FAILED: position fixture {name!r} gave {findings}, expected {expected!r}")
            failed += 1
    if not failed:
        print(f"position selftest: {len(cases)} fixtures fail closed with named findings")
    return failed


def main(argv: list[str]) -> int:
    if "--selftest" in argv and position_selftest():
        return 1
    return engine.main(AMENDMENT, argv)


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
        "Each row's visible text begins with its declared row name, exactly as the table spells it, character for character and in the same case, and the row's offset, or its statement that its target is not rendered, follows the name.",
        "Each row routes to the first element of its target: the target's heading when it has one, otherwise its first element in document order.",
        "Row names are `action-label` strings; each offset and the stopping line is a `scope-instruction` string; the text of a row whose target is not rendered is an `epistemic-disclosure`.",
        "whose limit of one entry `scope-instruction` counts only the statement of the POC bound.",
        "The index precedes the PWB-REQ-014 narrative tree and is not one of its narrative units.",
        "A row whose target is not rendered at that evaluation SHALL say so and route nowhere; it SHALL NOT route to a substitute.",
        "Each row whose target is rendered SHALL show the word offset at which its target begins: the number of counted words that precede the target's first element in document order.",
        "A row whose target is not rendered shows no offset.",
        "Exactly one stopping line SHALL stand at the place the next item fixes.",
        "Where any indexed target is rendered, the line gives the largest offset and the page's word total, and nothing else about the index.",
        "The target that sets the line is the rendered target whose offset is largest; where two share the largest offset, it is the one whose first element comes later in document order.",
        "The line stands immediately after the outermost element that contains the first element of the target that sets the line, that first element itself included, and is either a `details` element closed on first load or a `p`, heading (`h1` to `h6`), `ul`, `ol`, `dl` or `table` element; where no such element contains it, the line stands immediately after that first element.",
        "Where no indexed target is rendered, the line stands immediately after the index and gives only the word total.",
        "The stopping line's visible text is its numbers and their unit, and nothing else.",
        '"Stopping line" is this specification\'s name for it and is never shown on the page.',
        "Words are counted by one declared method, over the document as the browser holds it after load, with every `details` element in its first-load state, at the viewport width and height the page has when it loads.",
        "The offsets and total a page shows SHALL be those of that viewport; an oracle declares the viewport it ran at and publishes it with its result.",
        "A word is a maximal run of non-whitespace characters in a text node, counted in document order from the start of the body.",
        "Excluded from the count: text inside `script`, `style`, `template` and `noscript` elements; inside any element with the `hidden` attribute, `aria-hidden=\"true\"` or a computed `display: none`; any text node whose parent element's computed `visibility` is not `visible`; inside a `details` element closed on first load, except its `summary`, which counts; and the index rows and stopping line themselves.",
        "The total counts the same population over the whole body.",
        "The index, its offsets and the stopping line are presentation measurements.",
        "They carry no epistemic tuple, enter no PWB-REQ-020 parity family and no PWB-REQ-021 record or readiness arm, and SHALL NOT state or imply that any prompt is, or can be, answered: the walkthrough verdict stays the owner's (RFC7-31).",
        "[Unknown] Which offsets and total Butlers' Polaris would show today: no current figure is quoted here.",
        "They are measured on a fresh private-daemon capture at a named commit when this is implemented.",
        "at an evaluation where every indexed target renders, at one where the opening Unknown aggregate is absent, at one where two targets share the largest offset, at one where the target that sets the stopping line begins inside a `details` element closed on first load, and at one where no indexed target renders.",
        "the first reading level begins with the index, whose nine rows appear in the declared order with their names, targets and offsets, and one stopping line stands where this requirement places it.",
        "an independent word counter applies the declared method to the document after load and recomputes every row offset and the total",
        "each row's name and target are compared with this requirement's table, never with the renderer's own mapping;",
        "exactly one stopping line must stand where this requirement places it and carry the largest recomputed offset, or, where no indexed target renders, only the recomputed total.",
        "located by a recognizer whose selectors, and every heading string they match, are published with the oracle before it runs and key only on visible heading text, on claim identities the machine answer serves and on the PWB-REQ-011 exact-source route form, never on an attribute, class or identifier the renderer emits to mark an index target;",
        "the stopping line is missing, repeated or misplaced, or its offset is not the largest;",
        "expected offsets come from a word counter that shares no code with the renderer.",
        "the index is present but does not begin the first reading level;",
        "an index row is missing, duplicated or out of order, its text does not begin with its declared row name exactly, or it is routed to a target other than the declared one;",
        "an unrendered target's row does not say that its target is not rendered, routes anywhere or shows an offset;",
        "an offset or total differs from the independent count",
        "where no indexed target renders, the stopping line gives anything but the word total;",
        "the stopping line shows any text beyond its numbers and their unit;",
        "the stopping line states or implies that a prompt is answered",
        "an offset is presented as a claim, a parity fact or a walkthrough fact.",
        "**WHEN** Polaris renders its first reading level at an evaluation where every indexed target renders",
        "each beginning with its declared row name, routing to its declared target and showing that target's word offset by the declared method",
        "exactly one stopping line stands at the place this requirement fixes for the target that sets the line: immediately after that target's first element, or after the outermost closed `details`, `p`, heading, `ul`, `ol`, `dl` or `table` element containing it; the line gives the largest offset and the page's word total, and claims nothing about whether any prompt is answered",
        "the `gaps` row says its target is not rendered, shows no offset and routes nowhere",
        "each of the other eight rows still routes to its declared target and shows that target's word offset by the declared method",
        "the target that sets the stopping line is the one whose first element comes later in document order",
        "exactly one stopping line stands immediately after the outermost element containing that first element that is a closed `details`, `p`, heading, `ul`, `ol`, `dl` or `table` element, so that no closed `details` element contains the line",
        "every row says its target is not rendered, shows no offset and routes nowhere",
        "exactly one stopping line stands immediately after the index and gives only the page's word total",
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
        "#### Scenario: A tie on the largest offset is broken by document order",
        "#### Scenario: A last-beginning target inside a closed disclosure moves the line after it",
        "#### Scenario: With no indexed target rendered, the stopping line gives only the total",
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
         "the stopping line is missing, repeated\n  or misplaced, or its offset is not the largest; ", "",
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
         "never on an attribute, class or identifier the renderer emits", "or on an attribute, class or identifier the renderer emits",
         "PWB-REQ-010 carries 0 copies of required phrase: 'located by a recognizer"),
        ("unrendered row shows an offset",
         "A row whose target\n  is not rendered shows no offset.", "A row whose target\n  is not rendered shows offset zero.",
         "PWB-REQ-010 carries 0 copies of required phrase: 'A row whose target is not rendered shows no"),
        ("viewport left to the oracle",
         "at the viewport width and height the page has when it\n    loads", "at the viewport width and height the oracle\n    declares",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Words are counted by one declared"),
        ("displayed offsets of another viewport",
         "SHALL be those of that\n    viewport", "MAY be those of any\n    viewport",
         "PWB-REQ-010 carries 0 copies of required phrase: 'The offsets and total"),
        ("visible descendant of a hidden element excluded",
         "any text node whose\n    parent element's computed `visibility` is not `visible`",
         "inside any element with a computed\n    `visibility: hidden`",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Excluded from the count"),
        ("largest-offset tie left open",
         "; where two share the largest offset, it is the one whose first\n    element comes later in document order", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'The target that sets the line"),
        ("closed-details override keyed back to 'that element'",
         "after the outermost element that contains the first element of the\n    target that sets the line",
         "after the outermost element that contains that element",
         "PWB-REQ-010 carries 0 copies of required phrase: 'The line stands immediately after"),
        ("closed-details scenario lets the line stay inside",
         ", so that no closed `details`\n  element contains the line", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'exactly one stopping line stands immediately after the out"),
        ("row-name falsifier dropped",
         "its text does not begin with\n  its declared row name exactly, or it is routed", "or it is routed",
         "PWB-REQ-010 carries 0 copies of required phrase: 'an index row is missing"),
        ("row-name match loosened",
         "exactly as\n    the table spells it, character for character and in the same case", "loosely",
         "PWB-REQ-010 carries 0 copies of required phrase: \"Each row's visible"),
        ("scenario stopping line moved to the last indexed target",
         "- **AND** exactly one stopping line stands at the place this requirement\n  fixes for the target that sets the line",
         "- **AND** exactly one stopping line follows the last indexed target",
         "PWB-REQ-010 carries 0 copies of required phrase: 'exactly one stopping line stands at the place"),
        ("presentation measurements become project claims",
         "are presentation\n    measurements", "are project\n    claims",
         "PWB-REQ-010 carries 0 copies of required phrase: 'The index, its offsets"),
        ("any counting method",
         "Words are counted by one declared method", "Words are counted by any method",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Words are counted"),
        ("stopping line's name shown",
         "and\n    is never shown on the page", "and\n    may be shown on the page",
         "PWB-REQ-010 carries 0 copies of required phrase: '\"Stopping line\""),
        ("stopping-line text unbounded",
         "The stopping line's visible text is its numbers and their unit, and\n    nothing else.",
         "The stopping line's visible text includes its numbers.",
         "PWB-REQ-010 carries 0 copies of required phrase: \"The stopping line's"),
        ("case's absent-aggregate evaluation dropped",
         ", at one where the opening\n  Unknown aggregate is absent", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'at an evaluation where every indexed"),
        ("observable's index limb dropped",
         "the first reading\n  level begins with the index, whose nine rows", "the nine rows",
         "PWB-REQ-010 carries 0 copies of required phrase: 'the first reading level begins with the index"),
        ("first scenario's WHEN widened",
         "- **WHEN** Polaris renders its first reading level at an evaluation where\n  every indexed target renders",
         "- **WHEN** Polaris renders its first reading level",
         "PWB-REQ-010 carries 0 copies of required phrase: '**WHEN** Polaris renders"),
        ("capture replaced by an estimate",
         "They are measured on a fresh\n    private-daemon capture", "They are estimated",
         "PWB-REQ-010 carries 0 copies of required phrase: 'They are measured on a fresh"),
        ("index-first falsifier dropped",
         "the index is present but does not begin the first reading level; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'the index is present"),
        ("unrendered row may stay silent",
         "does not say that its target is\n  not rendered, routes", "routes",
         "PWB-REQ-010 carries 0 copies of required phrase: \"an unrendered target's"),
        ("no-target stopping line may show an offset",
         "where no indexed target\n  renders, the stopping line gives anything but the word total; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'where no indexed target renders, the stopping"),
        ("heading strings read off the page",
         "selectors, and every heading string they match, are published with the\n  oracle before it runs",
         "selectors are published with the\n  oracle",
         "PWB-REQ-010 carries 0 copies of required phrase: 'located by a recognizer"),
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
        ("tie scenario dropped",
         "#### Scenario: A tie on the largest offset is broken by document order\n",
         "#### Scenario: A tie\n",
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
    raise SystemExit(main(sys.argv[1:]))
