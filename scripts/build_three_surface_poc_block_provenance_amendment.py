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
    "provenance once, as one record in the shape each element of the machine answer's entity and relationship provenance lists takes,",
    "The capture instant stays on the observation beside that record, as the second half of the observation's identity. It is not a second statement of provenance.",
    "carries that revision as provenance by belonging to the observation.",
    "Over every field of the served observation, compare each whole value against the",
    "exactly one field holds the",
    "the provenance record's, and exactly one holds the capture instant, the observation's own",
    "an exhausted sweep decides.",
    "the provenance shape compared against is the one the machine answer's entities carry.",
)

REQ_001 = engine.Target(
    req_id="POC-REQ-001",
    required_once=SHARED_REQUIRED + (
        "whose every entry carries that revision as provenance.",
        "The observation so produced SHALL state its",
        "and that record names the revision. No other field of the observation, its own or an entry's, SHALL hold the revision as its whole value.",
        "No inventory entry SHALL carry a field whose whole value is the observation's revision or its capture instant.",
        "then sweeps every field of the served observation, its own and every entry's; the denominator is the observation's own fields and the complete served inventory.",
        "Bounded: one revision, sampled entries for size and digest, every field for the sweep.",
        "an observation served without a provenance record, with it in another shape, or with any other field holding the revision;",
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
    token_counts=((r"\bMAY\b", 0),),
)

REQ_010 = engine.Target(
    req_id="POC-REQ-010",
    required_once=SHARED_REQUIRED + (
        "with every served work-item fact carrying that revision as provenance.",
        "The observation so served SHALL state its",
        "and that record names the Dolt revision. No other field of the observation, its own or a work-item fact's, SHALL hold the Dolt revision as its whole value.",
        "No work-item fact SHALL carry a field whose whole value is the observation's Dolt revision, or carry the capture instant in any field other than a time the database itself records for that item.",
        "then sweeps every field of the served observation, its own and every item's; the denominator is the observation's own fields and the complete served item set.",
        "leaving out each item's created, updated and closed times, which the database records;",
        "without a provenance record, with it in another shape, or with any other field holding the Dolt revision;",
        "or a work-item fact that carries the observation's Dolt revision, or its capture instant outside a time the database records for that item.",
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
    token_counts=((r"\bMAY\b", 0),),
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
    #: Both unsigned. The identity amendment touches the reader notes and
    #: POC-REQ-052…060; the governing-intent amendment (P-100) touches the
    #: reader notes and POC-REQ-014. Neither touches 001 or 010, so each spec
    #: patch composes with this one in every order (proved on every --check);
    #: with each other they do not (exclusive_pending below). The dependency declaration's Source line is rewritten by all
    #: three, so whichever is signed later is regenerated with --write over
    #: the earlier one's applied bytes. The governing-intent package carries
    #: no builder or manifest, so this classification has no reverse entry.
    pending_siblings=frozenset({
        "three-surface-poc-identity-amendment",
        "three-surface-poc-governing-intent-amendment",
    }),
    #: The identity and governing-intent amendments both rewrite the reader
    #: notes' requirement-family lines, so as drafted no order applies both
    #: (review of PR 322). Coordinator decision 2026-10-04, a process ruling
    #: and not an owner act: declare exactly this pair. Whichever of the two
    #: is signed second is regenerated with --write over the first's applied
    #: bytes. --check warns about the pair on every run; each of the two still
    #: has to compose with this package in every order.
    exclusive_pending=frozenset({frozenset({
        "three-surface-poc-identity-amendment",
        "three-surface-poc-governing-intent-amendment",
    })}),
)


def selftest() -> int:
    pkg = PACKAGE
    proposed = engine.proposed_bytes(pkg)
    spec = proposed[SPEC]
    replace = engine.replace_once
    one = "POC-REQ-001 carries 0 copies of required phrase: "
    ten = "POC-REQ-010 carries 0 copies of required phrase: "
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
            SPEC, replace(spec, "No other field of the observation, its own or an entry's, SHALL hold the revision as its whole value.", "The header MAY repeat the revision."),
            one + "and that record names the revision.",
        ),
        "per-entry repeat allowed": (
            SPEC, replace(spec, "No inventory entry SHALL carry a field whose whole value is the observation's revision or its capture instant.", "An inventory entry MAY carry the observation's revision."),
            one + "No inventory entry SHALL",
        ),
        "capture instant homeless": (
            SPEC, replace(spec, "SHALL hold the revision as its whole value. - The capture instant stays on the observation beside that record, as the second half of the observation's identity. It is not a second statement of provenance.", "SHALL hold the revision as its whole value.\n  - The capture instant is dropped."),
            one + "The capture instant stays",
        ),
        "source timestamps not exempt": (
            SPEC, replace(spec, "or carry the capture instant in any field other than a time the database itself records for that item.", "or its capture instant."),
            ten + "No work-item fact SHALL",
        ),
        "shape requirement dropped": (
            SPEC, replace(spec, "provenance once, as one record in the shape each element of the machine answer's entity and relationship provenance lists takes, and that record names the Dolt revision.", "provenance once, and names the Dolt revision."),
            ten + "provenance once, as one record",
        ),
        "sweep narrowed to a sample (001)": (
            SPEC, replace(spec, "Over every field of the served observation, compare each whole value against the revision and", "Over one sampled entry, compare each whole value against the revision and"),
            one + "Over every field of the served observation",
        ),
        "sweep narrowed to a sample (010)": (
            SPEC, replace(spec, "Over every field of the served observation, compare each whole value against the Dolt revision", "Over one sampled item, compare each whole value against the Dolt revision"),
            ten + "Over every field of the served observation",
        ),
        "header limb dropped": (
            SPEC, replace(spec, "exactly one field holds the Dolt revision, the provenance record's, and", "no item field holds the Dolt revision, and"),
            ten + "exactly one field holds the",
        ),
        "sweep denominator dropped": (
            SPEC, replace(spec, "then sweeps every field of the served observation, its own and every entry's; the denominator is the observation's own fields and the complete served inventory.", "then samples entries."),
            one + "then sweeps every field",
        ),
        "repeat falsifier dropped": (
            SPEC, replace(spec, "or a work-item fact that carries the observation's Dolt revision, or its capture instant outside a time the database records for that item.", "."),
            ten + "or a work-item fact that carries",
        ),
        "scenario AND dropped": (
            SPEC, replace(spec, "- **AND** no inventory entry carries R, or the observation's capture instant, in a field of its own", ""),
            one + "no inventory entry carries R",
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
        "permissive modal inserted": (
            SPEC, replace(spec, "  - Every inventory entry carries that revision as provenance by", "  - An entry MAY restate it.\n  - Every inventory entry carries that revision as provenance by"),
            "POC-REQ-001 carries 1 matches of token",
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
