#!/usr/bin/env python3
"""Build and verify the inert PWB accessible-name amendment candidate.

The amendment adds two whole-page checks to PWB-REQ-016 (bead
``syzygy-u05.12``, slice C, register row P-99): interactive elements with
different targets carry different accessible names, and heading levels never
skip, both run over the complete population of a page rendered from a
whole-project evaluation and reporting that population as their denominator.
The engine and its modes live in ``scripts/pwb_requirement_amendment.py``;
this file declares only what this amendment must say.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pwb_requirement_amendment as engine  # noqa: E402


AMENDMENT = engine.Amendment(
    candidate="pwb-accessible-name-amendment",
    manifest="PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt",
    title="PWB ACCESSIBLE-NAME AMENDMENT MANIFEST",
    label="accessible-name",
    requirement="PWB-REQ-016",
    required_once=(
        "On a Polaris page, two interactive elements (links, buttons, `summary` disclosures and form controls) whose targets or controlled regions differ SHALL have different accessible names, as the browser computes them.",
        "A visible label repeated once per item or source SHALL be told apart in the accessible name by the item or source it belongs to.",
        "Two elements with the same target may share a name.",
        "A Polaris page SHALL have exactly one level-1 heading, and in document order no heading SHALL be more than one level deeper than the heading before it.",
        "The checks in this requirement SHALL run over every Polaris page served at one whole-project evaluation, including the entry page and each exact-source route response PWB-REQ-011 serves.",
        "Each check SHALL report the number of pages and, per page, the complete interactive and heading population as its denominators.",
        "a button's or form control's is the element its `aria-controls` names, or the control itself when it names none.",
        "The accessible name SHALL begin with the visible label",
        "The heading population is every heading element in the document after load, including those inside a closed `details`",
        "Headings inside a verbatim Butlers body rendered under PWB-REQ-011 are counted and reported but are outside the level-1 and order rules",
        "A fixture smaller than that population SHALL NOT stand in for it.",
        "[Unknown] How large these populations are on Butlers' Polaris today, and how many names they share: no current figure is quoted here.",
        "run the distinct-name and heading-order checks over every Polaris page served at a whole-project evaluation.",
        "no two interactive elements with different targets share an accessible name, no heading skips a level, there is one level-1 heading, and each sweep reports its denominator.",
        "group the interactive elements by computed accessible name and compare each group's targets, and read heading levels in document order;",
        "each check's page count must equal the pages Polaris serves at that evaluation, and each per-page denominator the population the browser enumerates on that page.",
        "two interactive elements with different targets sharing an accessible name;",
        "a skipped heading level or a second level-1 heading outside a verbatim body;",
        "or a check run over fewer pages, or a smaller population, than the evaluation serves.",
        "each of those links' accessible names names the source it routes to",
        "a skipped heading level, a second level-1 heading or a shared name across different targets fails the check",
    ),
    replaced=(
        "  perform the complete cold-open prompt set.",
        "  no pointer-only action exists, and the walkthrough record names its mode.",
        "  only action, keyboard trap, missing mode flag or failed cold-open path.",
    ),
    kept_scenarios=(
        "#### Scenario: Keyboard-only owner reaches exact intent",
    ),
    new_scenarios=(
        "#### Scenario: Repeated source links are told apart by name",
        "#### Scenario: Name and heading checks cover every Polaris page",
    ),
    mutants=(
        ("summary disclosures dropped",
         "(links, buttons, `summary` disclosures and form controls)", "(links and buttons)",
         "PWB-REQ-016 carries 0 copies of required phrase: 'On a Polaris page"),
        ("visible name instead of computed",
         "as the\n  browser computes them.", "as the\n  page labels them.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'On a Polaris page"),
        ("repeated label left ambiguous",
         "SHALL be told apart in\n    the accessible name", "may be told apart in\n    the accessible name",
         "PWB-REQ-016 carries 0 copies of required phrase: 'A visible label repeated"),
        ("second level-1 heading allowed",
         "exactly one level-1 heading,", "at least one level-1 heading,",
         "PWB-REQ-016 carries 0 copies of required phrase: 'A Polaris page SHALL have"),
        ("skip allowed",
         "no heading SHALL be more than one level deeper", "no heading SHALL be more than two levels deeper",
         "PWB-REQ-016 carries 0 copies of required phrase: 'A Polaris page SHALL have"),
        ("fixture stands in",
         "A fixture smaller\n  than that population SHALL NOT stand in for it.", "A fixture may stand in for it.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'A fixture smaller"),
        ("page count dropped",
         "Each check SHALL report the number of pages and, per page, the",
         "Each check SHALL report, per page, the",
         "PWB-REQ-016 carries 0 copies of required phrase: 'Each check SHALL report"),
        ("exact-source pages dropped",
         ", including\n  the entry page and each exact-source route response PWB-REQ-011 serves.", ".",
         "PWB-REQ-016 carries 0 copies of required phrase: 'The checks in this requirement"),
        ("label-in-name dropped",
         "The accessible\n    name SHALL begin with the visible label", "The accessible\n    name may omit the visible label",
         "PWB-REQ-016 carries 0 copies of required phrase: 'The accessible name SHALL"),
        ("verbatim headings ruled",
         "but are outside the level-1 and order rules", "and are inside the level-1 and order rules",
         "PWB-REQ-016 carries 0 copies of required phrase: 'Headings inside a verbatim"),
        ("current figure quoted",
         "[Unknown] How large", "[Observed] How large",
         "PWB-REQ-016 carries 0 copies of required phrase: \"[Unknown] How large"),
        ("oracle denominator dropped",
         "each check's page count must equal the pages Polaris serves at that\n  evaluation", "each check reports a page count",
         "PWB-REQ-016 carries 0 copies of required phrase: \"each check's page count"),
        ("population falsifier dropped",
         ";\n  or a check run over fewer pages, or a smaller population, than the\n  evaluation serves.", ".",
         "PWB-REQ-016 carries 0 copies of required phrase: 'or a check run over"),
        ("new scenario dropped",
         "#### Scenario: Name and heading checks cover every Polaris page\n",
         "#### Scenario: Name and heading checks\n",
         "PWB-REQ-016 lacks exactly one"),
        ("signed scenario dropped",
         "#### Scenario: Keyboard-only owner reaches exact intent\n",
         "#### Scenario: Keyboard-only owner\n",
         "PWB-REQ-016 lacks exactly one"),
    ),
    patch_drift=(
        "\n narrative change, and its record SHALL identify that mode.",
        "\n narrative change, and its record SHALL name that mode.",
    ),
)


if __name__ == "__main__":
    raise SystemExit(engine.main(AMENDMENT, sys.argv[1:]))
