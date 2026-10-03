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
the same proposed specification bytes.
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


AMENDMENT = engine.Amendment(
    candidate="pwb-opening-index-amendment",
    manifest="PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt",
    title="PWB OPENING-INDEX AMENDMENT MANIFEST",
    label="opening-index",
    requirement="PWB-REQ-010",
    required_once=(
        "The first reading level SHALL begin with an index of exactly nine rows, one for each PWB-REQ-021 answer identity, in the order and to the targets this table declares.",
        "No run, reader or model decides a row's target.",
        "| `exact-requirement` | exact requirements | the first link, in document order, to an exact requirement's text |",
        "| `unknown-or-contradiction` | gaps | the opening Unknown aggregate |",
        "Each row is named by its project concept and routes to the first element of its target.",
        "Row names are `action-label` strings; each offset and the stopping line is a `scope-instruction` string; all of them obey PWB-REQ-012.",
        "A row whose target is not rendered at that evaluation SHALL say so and route nowhere; it SHALL NOT route to a substitute.",
        "Each row SHALL show the word offset at which its target begins.",
        "One stopping line SHALL follow the last indexed target in document order and give the largest row offset and the page's word total, and nothing else about the index.",
        "a word is a maximal run of non-whitespace characters in a rendered text node, counted in document order from the start of the body, excluding the content of `script` and `style` elements and of every `details` element closed on first load.",
        "The total counts the same population over the whole body.",
        "They carry no epistemic tuple, enter no PWB-REQ-020 parity family and no PWB-REQ-021 record or readiness arm, and SHALL NOT state or imply that any prompt is, or can be, answered: the walkthrough verdict stays the owner's (RFC7-31).",
        "[Unknown] Which offsets and total Butlers' Polaris would show today: no current figure is quoted here.",
        "an independent word counter applies the declared method to the served HTML and recomputes every row offset and the total",
        "each row's target is compared with this requirement's table, never with the renderer's own mapping.",
        "expected offsets from a word counter that shares no code with the renderer.",
        "an index row is missing, duplicated, out of order or routed to a target other than the declared one",
        "an unrendered target's row routes anywhere",
        "an offset or total differs from the independent count",
        "the stopping line states or implies that a prompt is answered",
        "an offset is presented as a claim, a parity fact or a walkthrough fact.",
        "the `gaps` row says its target is not rendered and routes nowhere",
        "claims nothing about whether any prompt is answered",
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
         " and of every `details` element closed on first load.", ".",
         "PWB-REQ-010 carries 0 copies of required phrase: 'a word is a maximal run"),
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
         "never with the renderer's own mapping.", "or with the renderer's own mapping.",
         "PWB-REQ-010 carries 0 copies of required phrase: \"each row's target"),
        ("stopping-line falsifier dropped",
         "the stopping line\n  states or implies that a prompt is answered; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'the stopping line states"),
        ("stopping line role dropped",
         "each\n    offset and the stopping line is a `scope-instruction` string; ", "",
         "PWB-REQ-010 carries 0 copies of required phrase: 'Row names are"),
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
    extra_findings=index_findings,
)


if __name__ == "__main__":
    raise SystemExit(engine.main(AMENDMENT, sys.argv[1:]))
