#!/usr/bin/env python3
"""Build and verify the inert PWB accessible-name amendment candidate.

The amendment adds two checks to PWB-REQ-016 (bead ``syzygy-u05.12``,
slice C, register row P-99): interactive elements with different targets
carry different accessible names, an element sharing its visible label with a
differently targeted one has a name that begins with that label, and heading
levels never skip. Both run over every Polaris page served at one
whole-project evaluation, the pages listed from the machine answer, and
report the page count and each page's complete population as their
denominators. The engine and its modes live in
``scripts/pwb_requirement_amendment.py``; this file declares only what this
amendment must say, and checks that each replaced signed line is extended in
its own position.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pwb_requirement_amendment as engine  # noqa: E402


def position_findings(spec: str, block: str) -> list[str]:
    """Each replaced signed line is extended where it stood, not elsewhere.

    The engine asks only that some line of the block open with a replaced
    line's signed stem. Here the line that follows the replaced line's signed
    predecessor must be the one that does (round-2 review, finding 6).
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


AMENDMENT = engine.Amendment(
    candidate="pwb-accessible-name-amendment",
    manifest="PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt",
    title="PWB ACCESSIBLE-NAME AMENDMENT MANIFEST",
    label="accessible-name",
    requirement="PWB-REQ-016",
    required_once=(
        "On a Polaris page, two interactive elements (links, buttons, `summary` disclosures and form controls) whose targets or controlled regions differ SHALL have different accessible names, as the browser computes them.",
        "The interactive population is every link with an `href`, button, `summary` and form control in the document after load, including those inside a closed `details`, and excluding those hidden by the `hidden` attribute, `aria-hidden=\"true\"` or a computed `display: none`.",
        "An element's visible label is its text content with each whitespace run collapsed to one space and the ends trimmed.",
        "Where elements of that population whose targets differ share one visible label on a page, each of their accessible names SHALL begin with that visible label.",
        "Where such an element's target is an exact-source route response, the words after the label SHALL include the repository-relative path the machine answer carries for the source that route serves (PWB-REQ-011's machine recovery).",
        "These two rules bind no other element.",
        "Two elements with the same target may share a name.",
        "A Polaris page SHALL have exactly one level-1 heading, and in document order no heading SHALL be more than one level deeper than the heading before it.",
        "The checks in this requirement SHALL run over every Polaris page served at one whole-project evaluation, including the entry page and each exact-source route response PWB-REQ-011 serves.",
        "Each check SHALL report the number of pages and, per page, the complete interactive and heading population as its denominators.",
        "a button's or form control's is the element its `aria-controls` names, or the control itself when it names none.",
        "The heading population is every `h1` to `h6` element, at its own level, and every element with `role=\"heading\"`, at its `aria-level`, in the document after load, including those inside a closed `details`, and excluding those hidden by the `hidden` attribute, `aria-hidden=\"true\"` or a computed `display: none`.",
        "No heading in that population is exempt, including one Polaris renders from Butlers-declared text.",
        "The pages are the entry page and one exact-source route response for each source the machine answer at that evaluation lists, whether that response serves the source's body or refuses it.",
        "The list comes from the machine answer, never from the links the renderer emits.",
        "A fixture smaller than that population SHALL NOT stand in for it.",
        "[Unknown] How large these populations are on Butlers' Polaris today, and how many names they share: no current figure is quoted here.",
        "run the distinct-name and heading-order checks over every Polaris page served at a whole-project evaluation.",
        "no two interactive elements with different targets share an accessible name, each element sharing a visible label with a differently targeted one has a name that begins with that label and, for an exact-source target, includes that source's path, no heading skips a level, there is one level-1 heading, and each sweep reports its denominator.",
        "group the interactive elements by computed accessible name and compare each group's targets; group them again by visible label and, in each group whose targets differ, compare the start of each computed name with the label and, for each exact-source target, look for the source's path in the words after it; and read heading levels in document order;",
        "each check's page count must equal the number of pages listed from the machine answer at that evaluation, and each per-page denominator the population this requirement defines on that page.",
        "The page list and each expected source path come from the machine answer, never from the rendered page.",
        "two interactive elements with different targets sharing an accessible name;",
        "an element sharing a visible label with a differently targeted one whose name does not begin with that label or, for an exact-source target, omits that source's path;",
        "a skipped heading level or a second level-1 heading;",
        "or a check run over fewer pages, or a smaller population, than the evaluation serves.",
        "each of those links' accessible names begins with that visible label and then includes the repository-relative path the machine answer carries for the source it routes to",
        "the pages listed from the machine answer, and report the page count and those populations",
        "a skipped heading level, a second level-1 heading, a shared name across different targets or a shared-label name that does not begin with its visible label fails the check",
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
        ("shared-label prefix relaxed",
         "each\n    of their accessible names SHALL begin with that visible label.",
         "each\n    of their accessible names may omit that visible label.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'Where elements of that population"),
        ("added words made free text",
         "the words\n    after the label SHALL include the repository-relative path the machine\n    answer carries",
         "the words\n    after the label are free text the renderer\n    chooses",
         "PWB-REQ-016 carries 0 copies of required phrase: \"Where such an element's target"),
        ("shared-label rule scoped to every element",
         "These two rules bind no other element.", "These two rules bind every element.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'These two rules bind no other"),
        ("hidden headings included",
         "and\n    excluding those hidden by the `hidden` attribute, `aria-hidden=\"true\"`\n    or a computed `display: none`.",
         "and\n    including those hidden by the `hidden` attribute, `aria-hidden=\"true\"`\n    or a computed `display: none`.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'The heading population is every"),
        ("closed-details links left out",
         "`summary` and form control in the document after load, including those\n    inside a closed `details`,",
         "`summary` and form control in the accessibility tree, excluding those\n    inside a closed `details`,",
         "PWB-REQ-016 carries 0 copies of required phrase: 'The interactive population is every"),
        ("page list taken from the renderer",
         "The list comes from the\n    machine answer, never from the links the renderer emits.",
         "The list comes from the\n    links the renderer emits.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'The list comes from the machine"),
        ("label-prefix falsifier dropped",
         " an\n  element sharing a visible label with a differently targeted one whose name\n  does not begin with that label or, for an exact-source target, omits that\n  source's path;", "",
         "PWB-REQ-016 carries 0 copies of required phrase: 'an element sharing a visible label"),
        ("scenario identity made free text",
         "begins with that visible\n  label and then includes the repository-relative path the machine answer\n  carries for the source it routes to",
         "names the source it routes\n  to",
         "PWB-REQ-016 carries 0 copies of required phrase: \"each of those links' accessible"),
        ("replaced line extended out of position",
         "nonvisual representation, then\n  perform the complete cold-open prompt set;",
         "nonvisual representation, then\n  and only then\n  perform the complete cold-open prompt set;",
         "signed PWB-REQ-016 replaced line not extended in its own position"),
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
        ("heading exemption added",
         "No heading in that population is exempt, including one Polaris renders\n    from Butlers-declared text.",
         "Headings in Butlers-declared text are exempt.",
         "PWB-REQ-016 carries 0 copies of required phrase: 'No heading in that population"),
        ("current figure quoted",
         "[Unknown] How large", "[Observed] How large",
         "PWB-REQ-016 carries 0 copies of required phrase: \"[Unknown] How large"),
        ("oracle denominator dropped",
         "each check's page count must equal the number of pages listed from the\n  machine answer at that evaluation", "each check reports a page count",
         "PWB-REQ-016 carries 0 copies of required phrase: \"each check's page count"),
        ("population falsifier dropped",
         "; or a\n  check run over fewer pages, or a smaller population, than the evaluation\n  serves.", ".",
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
    extra_findings=position_findings,
)


if __name__ == "__main__":
    raise SystemExit(engine.main(AMENDMENT, sys.argv[1:]))
