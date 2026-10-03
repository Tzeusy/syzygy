#!/usr/bin/env python3
"""Build and verify the inert Three-Surface POC block-provenance amendment.

The amendment changes how POC-REQ-001 and POC-REQ-010 serve provenance (bead
``syzygy-u05.9``, pursuit move N9): the code-structure and work-item
observations each state their provenance once, as one record in the shape
the machine answer's entities and relationships already carry, and no entry
beneath them restates the observation's revision or capture instant. Every
entry still carries that revision as provenance, by belonging to its
observation. The six POC subjects are bound by the 2026-09-29 readability
successor act, so ``--check`` and ``--write`` apply this package's
``proposed/*.patch`` files only in a scratch tree; ``--apply --at-adoption``
writes them and belongs to the sign-off change alone.

It drives the family-neutral engine in
``build_pwb_anchor_resolution_amendment.py`` with its own ``Package``; the
modes and the structure predicates are the engine's. No warrant moves, so
neither ``CONTRACT-COVERAGE.md`` nor any other subject but the specification
and its generated dependency declaration changes.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_pwb_anchor_resolution_amendment as engine  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/three-surface-poc-experience")
SPEC = CHANGE / "specs/three-surface-poc-experience/spec.md"
GOVERNING = CHANGE / "GOVERNING-DEPENDENCIES.md"
CANDIDATE = engine.CANDIDATES / "three-surface-poc-block-provenance-amendment"

SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "CONTRACT-COVERAGE.md",
            GOVERNING,
            CHANGE / "design.md",
            CHANGE / "proposal.md",
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)

#: Phrases both amended requirements carry, one copy each.
SHARED_REQUIRED = (
    "The observation SHALL state its provenance once, as one record in the provenance shape the machine answer's entities and relationships carry,",
    "carries that revision as provenance by belonging to the observation.",
    "an exhausted sweep with no equal value decides.",
    "the provenance shape compared against is the one the machine answer's entities carry.",
)

REQ_001 = engine.Target(
    req_id="POC-REQ-001",
    required_once=SHARED_REQUIRED + (
        "whose every entry carries that revision as provenance.",
        "and that record names the revision. The observation SHALL name the revision nowhere else.",
        "No inventory entry SHALL carry a field whose whole value is the observation's revision or its capture instant.",
        "then sweeps every served inventory entry; the denominator is the complete served inventory.",
        "compare each field's whole value against the observation's revision and capture instant;",
        "Bounded: one revision, sampled entries for size and digest, every entry for the sweep.",
        "an observation served without a provenance record, with it in another shape, or naming its revision twice;",
        "or an inventory entry that carries the observation's revision or capture instant.",
        "identified by R, whose one provenance record names R,",
        "no inventory entry carries R, or the observation's capture instant, in a field of its own",
    ),
    replaced=(
        "  a known commit.",
        "- **Observable**: the observation's revision and inventory appear in",
        "  the machine answer; Orrery renders from it (POC-REQ-050).",
        "- **Oracle**: compare the served revision against `git rev-parse HEAD`",
        "  of the observed checkout, and a sampled file's served size and digest",
        "  against `stat` and an independent digest of the same path at that",
        "  commit; equality decides. Bounded: one revision, sampled entries.",
        "  filesystem directly, never from the POC's own output.",
        "- **Falsifier**: a served inventory entry whose revision, size, or",
        "  digest differs from the repository's own state at the named commit,",
        "  or an observation served without a revision.",
        "  identified by R, and every inventory entry cites R as its provenance",
        "  revision",
    ),
    scenarios=("#### Scenario: Structure observed at a commit",),
)

REQ_010 = engine.Target(
    req_id="POC-REQ-010",
    required_once=SHARED_REQUIRED + (
        "with every served work-item fact carrying that revision as provenance.",
        "and that record names the Dolt revision. The observation SHALL name the Dolt revision nowhere else.",
        "No work-item fact SHALL carry a field whose whole value is the observation's Dolt revision or its capture instant.",
        "then sweeps every served work-item fact; the denominator is the complete served item set.",
        "compare each field's whole value against the observation's Dolt revision and capture instant;",
        "without a provenance record, with it in another shape, or naming its Dolt revision twice;",
        "or a work-item fact that carries the observation's Dolt revision or capture instant.",
        "the served observation is identified by D, its one provenance record names D,",
        "no work-item fact carries D, or the observation's capture instant, in a field of its own",
    ),
    replaced=(
        "  Beads Dolt database at a known Dolt head.",
        "- **Observable**: the machine answer names the Dolt revision; a sampled",
        "  item's served status and timestamps match the database.",
        "- **Oracle**: compare the served Dolt revision against the database's",
        "  own head revision queried directly, and a sampled item's fields",
        "  against a direct SQL read at that revision; equality decides.",
        "  directly, never from the POC's output.",
        "  or a sampled field differing from the database's value at the named",
        "  revision.",
        "- **THEN** the served observation is identified by D and sampled item",
        "  facts equal direct reads at D",
    ),
    scenarios=("#### Scenario: Items read at a Dolt head",),
)

PACKAGE = engine.Package(
    label="Three-Surface POC block-provenance",
    candidate=CANDIDATE,
    manifest=CANDIDATE / "THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-MANIFEST.txt",
    title="THREE-SURFACE POC BLOCK-PROVENANCE AMENDMENT MANIFEST",
    change=CHANGE,
    spec=SPEC,
    governing=GOVERNING,
    subjects=SUBJECTS,
    patched=frozenset({GOVERNING, SPEC}),
    generator="build_three_surface_poc_spec_dependencies",
    req_prefix="POC-REQ-",
    targets=(REQ_001, REQ_010),
    performed_siblings={
        "three-surface-poc-readability-successor": "THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md",
    },
    declined_siblings=frozenset(),
    #: Unsigned; it touches the reader notes and POC-REQ-052…060, not 001 or
    #: 010, so the spec patches compose in either order. The dependency
    #: declaration's Source line is rewritten by both, so whichever is signed
    #: later is regenerated with --write over the earlier one's applied bytes.
    pending_siblings=frozenset({"three-surface-poc-identity-amendment"}),
)


def selftest() -> int:
    pkg = PACKAGE
    proposed = engine.proposed_bytes(pkg)
    spec = proposed[SPEC]
    replace = engine.replace_once
    mutants = {
        "other requirement drift": (
            SPEC, replace(spec, "### Requirement: POC-REQ-011 — Work-item observation is scoped to the registered bead-prefix", "### Requirement: POC-REQ-011 — Work-item observation is scoped"),
            "POC-REQ-011 changed",
        ),
        "reader notes drift": (
            SPEC, replace(spec, "Gaps in the numbering are deliberate.", "Gaps in the numbering are accidental."),
            "the specification text before the first requirement changed",
        ),
        "signed line edited": (
            SPEC, replace(spec, "structure, it SHALL produce one identified observation naming the exact git", "structure, it SHALL produce an identified observation naming the exact git"),
            "signed POC-REQ-001 line edited or removed",
        ),
        "second statement allowed": (
            SPEC, replace(spec, "The observation SHALL name the revision nowhere else.", "The observation MAY name the revision elsewhere."),
            "POC-REQ-001 carries 0 copies of required phrase",
        ),
        "per-entry repeat allowed": (
            SPEC, replace(spec, "No inventory entry SHALL carry a field whose whole value is the observation's revision or its capture instant.", "An inventory entry MAY carry the observation's revision."),
            "POC-REQ-001 carries 0 copies of required phrase",
        ),
        "capture instant dropped": (
            SPEC, replace(spec, "No work-item fact SHALL carry a field whose whole value is the observation's Dolt revision or its capture instant.", "No work-item fact SHALL carry a field whose whole value is the observation's Dolt revision."),
            "POC-REQ-010 carries 0 copies of required phrase",
        ),
        "shape requirement dropped": (
            SPEC, replace(spec, "once, as one record in the provenance shape the machine answer's entities and relationships carry, and that record names the Dolt revision.", "once, and names the Dolt revision."),
            "POC-REQ-010 carries 0 copies of required phrase",
        ),
        "sweep denominator dropped": (
            SPEC, replace(spec, "then sweeps every served inventory entry; the denominator is the complete served inventory.", "then samples entries."),
            "POC-REQ-001 carries 0 copies of required phrase",
        ),
        "repeat falsifier dropped": (
            SPEC, replace(spec, "or a work-item fact that carries the observation's Dolt revision or capture instant.", "."),
            "POC-REQ-010 carries 0 copies of required phrase",
        ),
        "scenario AND dropped": (
            SPEC, replace(spec, "- **AND** no inventory entry carries R, or the observation's capture instant, in a field of its own", ""),
            "POC-REQ-001 carries 0 copies of required phrase",
        ),
        "signed obligation sentence dropped": (
            SPEC, replace(spec, "with every served work-item fact carrying that revision as provenance.", "."),
            "signed POC-REQ-010 line edited or removed",
        ),
        "scenario renamed": (
            SPEC, replace(spec, "#### Scenario: Items read at a Dolt head", "#### Scenario: Items read"),
            "POC-REQ-010 scenario population differs",
        ),
        "warrant moved": (
            SPEC, replace(spec, "contracts: [RFC1-5, RFC2-1, RFC4-3, RFC4-11, RFC4-12, RFC6-15, RFC9-38]", "contracts: [RFC1-5, RFC2-1, RFC4-3, RFC4-11, RFC4-12, RFC6-15]"),
            "POC-REQ-001 warrants changed",
        ),
        "dependency drift": (
            GOVERNING, replace(proposed[GOVERNING], "24 requirement(s)", "25 requirement(s)"),
            "proposed GOVERNING-DEPENDENCIES differs from regeneration",
        ),
    }
    return engine.run_selftest(
        pkg, mutants,
        ("\n entry carries that revision as provenance.\n",
         "\n entry carries a revision as provenance.\n"),
    )


if __name__ == "__main__":
    raise SystemExit(engine.main(PACKAGE, selftest, sys.argv[1:]))
