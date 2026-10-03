#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert Three-Surface POC identity amendment package.

Ruling P-75 (2026-09-21) directed one CC-REV-2 amendment against the
three-surface-poc-experience specification alone: POC-REQ-054 (one subject
identity across the surfaces, with the per-claim three-state scenario),
POC-REQ-055 (every relation kind is a closed-vocabulary name or flagged
outside it), and an amendment to POC-REQ-060 (one epistemic record shape and
the Inferred label). The signed bytes are never edited while this package is
a candidate: proposed bytes live as patches, and the manifest hashes the
six-artifact subject after those patches. Applying them is a sign-off-time
operation.

    --check      verify patches, structure, regeneration and the manifest
    --selftest   one rule-6 mutation per predicate
    --write      regenerate the manifest over the proposed bytes
    --diff       print the proposed patches
    --apply --at-adoption   write the proposed bytes (sign-off change only)

The one signed coverage row the ruling names (P-75 Q3) must survive byte for
byte; every other signed row may only move from Part B2 to Part A, and every
added row says it is an amendment row.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/three-surface-poc-experience")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/three-surface-poc-identity-amendment"
)
PROPOSED = CANDIDATE / "proposed"
MANIFEST_OUT = CANDIDATE / "THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt"
TITLE = "THREE-SURFACE POC IDENTITY AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/three-surface-poc-experience/spec.md"
DEPENDENCIES = CHANGE / "GOVERNING-DEPENDENCIES.md"
PROPOSAL = CHANGE / "proposal.md"
COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"

SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            COVERAGE,
            DEPENDENCIES,
            CHANGE / "design.md",
            PROPOSAL,
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
PATCHED = tuple(
    sorted((COVERAGE, DEPENDENCIES, PROPOSAL, SPEC), key=lambda path: path.as_posix())
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
REQ_HEADING = re.compile(r"^### Requirement: (POC-REQ-\d{3}) — ", re.MULTILINE)
COVERAGE_ROW = re.compile(r"^\| (RFC\d+-[^ |]+) \|", re.MULTILINE)

NEW_IDS = ("POC-REQ-054", "POC-REQ-055")
AMENDED_IDS = ("POC-REQ-060",)
#: The signed row ruling P-75 Q3 names; it is edited on no arm.
BOUND_ROW = (
    "| RFC1-26 | Relations outside the closed table don't exist; "
    "no prose-widening | covered | POC-REQ-052 |"
)
#: P-75 Q3 chose disclosure, not removal, so closure itself stays Unknown.
CLOSURE_ROW_PREFIX = "| RFC1-26 | No relation outside the closed table is emitted at all |"
#: Part B2 beliefs that move to Part A because a requirement now covers one
#: of their consequences.
MOVED_FROM_B2 = ("RFC2-25", "RFC6-1", "RFC6-3", "RFC6-12")
AMENDMENT_MARK = "Amendment row"
POC_DIR_KEY = "`POC-DIR-2026-09-21`"
POC_DIR_FILE = "`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`"

#: Whitespace-normalized phrases each new or amended block must carry.
REQUIRED_PHRASES: dict[str, tuple[tuple[str, str], ...]] = {
    "POC-REQ-054": (
        ("cross-cutting group", "Group: Cross-cutting experience. Form: **invariant**."),
        ("one identity, by no other", "name that subject by that identity and by no other"),
        ("no surface-local handle", "No surface-local handle"),
        ("exactly one element per link", "to exactly one element for the same subject"),
        ("slot filled only by a joined subject", "filled only from a subject joined to that claim by its identity"),
        ("unfilled slot is a reasoned Unknown", "SHALL render Unknown with its reason and its resolution route"),
        ("slot never absent, scored or positive", "never absent, blank, a score, a verdict or styled as a positive state"),
        ("slot parity with the machine answer", "the machine answer SHALL carry the same three slots for the same identity"),
        ("identity scenario", "#### Scenario: One subject, one identity on every surface"),
        ("ribbon scenario", "#### Scenario: A three-state view with nothing joined"),
    ),
    "POC-REQ-055": (
        ("cross-cutting group", "Group: Cross-cutting experience. Form: **invariant**."),
        ("closed-table name in its roles", "a relation name from RFC1-25's closed table, emitted with its source and target in the roles that table assigns the relation"),
        ("outside flag with a reason", "carry an explicit outside-closed-vocabulary flag with a stated reason"),
        ("flag carried and rendered", "carried in the machine answer and rendered wherever the kind is rendered"),
        ("flag never widens the vocabulary", "it never adds the kind to that vocabulary"),
        ("reversed roles falsify", "emitted with source and target reversed"),
        ("disclosure scenario", "#### Scenario: A kind outside the closed table is disclosed"),
    ),
    "POC-REQ-060": (
        ("three labels encoded", "(Observed, Inferred, Unknown, and their reasons) identically wherever they appear"),
        ("one record shape", "in one record shape, in the shared model and in the machine answer"),
        ("closed tiers inside the parent label", "a rendering tier from RFC2-25's closed six where one applies, always inside its parent label"),
        ("closed reasons with a route", "exactly one primary reason from RFC2-24's closed twelve with its resolution route"),
        ("Inferred only from an agent", "An Inferred state SHALL arise only from an agent's assertion"),
        ("Inferred never Observed or clearing", "SHALL never count toward an Observed total or clear an Unknown"),
        ("Inferred encoded distinctly", "render with an encoding the legend distinguishes from Observed"),
        ("Inferred fixture limb", "the Inferred limbs are exercised by a fixture record injected at the model seam"),
        ("signed scenario kept", "#### Scenario: Unknown looks the same everywhere"),
        ("Inferred scenario", "#### Scenario: An agent assertion stays Inferred"),
    ),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized(text: str) -> str:
    return " ".join(text.split())


def current_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in SUBJECTS:
        if rel in overrides:
            values[rel] = overrides[rel]
        elif (ROOT / rel).is_file():
            values[rel] = (ROOT / rel).read_bytes()
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
        return {rel: (base / rel).read_bytes() for rel in SUBJECTS}


# --- the specification -------------------------------------------------------

def requirement_blocks(spec: str) -> tuple[str, list[tuple[str, str]]]:
    """(preamble, [(id, block)]) in file order; a block runs to the next heading."""
    marks = list(REQ_HEADING.finditer(spec))
    if not marks:
        return spec, []
    blocks = []
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(spec)
        blocks.append((mark.group(1), spec[mark.start():end]))
    return spec[: marks[0].start()], blocks


def spec_findings(proposed: bytes, current: bytes) -> list[str]:
    findings: list[str] = []
    new_pre, new_blocks = requirement_blocks(proposed.decode("utf-8"))
    old_pre, old_blocks = requirement_blocks(current.decode("utf-8"))
    old_ids = [rid for rid, _ in old_blocks]
    expected: list[str] = []
    for rid in old_ids:
        if rid == "POC-REQ-060":
            expected.extend(NEW_IDS)
        expected.append(rid)
    new_ids = [rid for rid, _ in new_blocks]
    if new_ids != expected:
        findings.append(
            "requirement population or order differs: expected "
            f"{len(expected)} with POC-REQ-054 and POC-REQ-055 between "
            f"POC-REQ-053 and POC-REQ-060, found {new_ids}"
        )
        return findings
    old_by_id = dict(old_blocks)
    for rid, block in new_blocks:
        if rid in NEW_IDS or rid in AMENDED_IDS:
            text = normalized(block)
            for label, phrase in REQUIRED_PHRASES[rid]:
                if normalized(phrase) not in text:
                    findings.append(f"{rid} lacks {label}")
            if "POC-DIR-2026-09-21" not in block:
                findings.append(f"{rid} warrants do not cite ruling P-75's decision key")
        elif block != old_by_id[rid]:
            findings.append(f"{rid} changed; the amendment touches only POC-REQ-054, 055 and 060")
    if "## ADDED Requirements" not in new_pre or (
        new_pre.split("## ADDED Requirements")[0] != old_pre.split("## ADDED Requirements")[0]
    ):
        findings.append("the specification's title, banner or Purpose changed")
    if POC_DIR_KEY not in new_pre or POC_DIR_FILE not in new_pre:
        findings.append("reader notes do not define the POC-DIR-2026-09-21 decision key")
    old_scenario = old_by_id["POC-REQ-060"].split("#### Scenario:", 1)[1].split("```yaml", 1)[0]
    new_060 = dict(new_blocks)["POC-REQ-060"]
    if "#### Scenario:" + old_scenario.rstrip("\n") not in new_060:
        findings.append("POC-REQ-060's signed scenario is not preserved verbatim")
    return findings


def dependency_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_three_surface_poc_spec_dependencies as generator

    rendered, errors = generator.generate(proposed[SPEC].decode("utf-8"))
    if errors:
        return [f"proposed warrants do not validate: {'; '.join(errors)}"]
    if rendered.encode("utf-8") != proposed[DEPENDENCIES]:
        return [
            "proposed GOVERNING-DEPENDENCIES.md differs from regeneration "
            "over the proposed spec bytes"
        ]
    return []


# --- the coverage matrix -----------------------------------------------------

def _section(text: str, start: str, end: str) -> str:
    begin = text.index(start)
    return text[begin: text.index(end, begin)]


def coverage_parts(text: str) -> dict[str, list[str]]:
    parts = {
        "A": _section(text, "## Part A", "## Part B1"),
        "B1": _section(text, "## Part B1", "## Part B2"),
        "B2": _section(text, "## Part B2", "## Verifying"),
    }
    return {
        key: [line for line in body.split("\n") if COVERAGE_ROW.match(line)]
        for key, body in parts.items()
    }


def _clause(row: str) -> str:
    return row.split("|")[1].strip()


def _disposition(row: str) -> str:
    return row.split("|")[3].strip()


def coverage_totals(text: str) -> dict[str, object]:
    parts = coverage_parts(text)
    families: dict[str, collections.Counter] = {}
    for key, rows in parts.items():
        families[key] = collections.Counter(
            re.match(r"(RFC\d+)-", clause).group(1) for clause in {_clause(r) for r in rows}
        )
    part_a = parts["A"]
    return {
        "a_rows": len(part_a),
        "a_clauses": len({_clause(r) for r in part_a}),
        "a_covered": sum(_disposition(r).startswith("covered") for r in part_a),
        "a_unknown": sum(_disposition(r).startswith("**Unknown**") for r in part_a),
        "b1_rows": len(parts["B1"]),
        "b1_clauses": len({_clause(r) for r in parts["B1"]}),
        "b2_clauses": len({_clause(r) for r in parts["B2"]}),
        "families": families,
    }


def totals_findings(text: str) -> list[str]:
    findings: list[str] = []
    totals = coverage_totals(text)
    families = totals["families"]
    for family in sorted(
        set().union(*(set(counter) for counter in families.values())),
        key=lambda name: int(name[3:]),
    ):
        match = re.search(rf"^\| {family} \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$", text, re.MULTILINE)
        if not match:
            findings.append(f"family table has no {family} row")
            continue
        accepted, a, b1, b2 = (int(value) for value in match.groups())
        computed = (families["A"][family], families["B1"][family], families["B2"][family])
        if (a, b1, b2) != computed:
            findings.append(f"family table {family} reads {(a, b1, b2)}, computed {computed}")
        if a + b1 + b2 != accepted:
            findings.append(f"family table {family} parts do not sum to {accepted}")
    a, b1, b2 = (totals["a_clauses"], totals["b1_clauses"], totals["b2_clauses"])
    printed = {
        "family total": f"| **Total** | **{a + b1 + b2}** | **{a}** | **{b1}** | **{b2}** |",
        "Part A totals": normalized(
            f"**{totals['a_rows']} consequence rows over {a} clauses — "
            f"{totals['a_covered']} covered, {totals['a_unknown']} Unknown.**"
        ),
        "Part B1 totals": normalized(
            f"**{totals['b1_rows']} consequence rows over {b1} clauses — all Unknown.**"
        ),
        "Part B2 total": f"**{b2} clauses.**",
        "denominator sum": f"{a} + {b1} + {b2} = {a + b1 + b2}.",
        "mapped-set count": f"`contracts[]` union ({a} identifiers).",
    }
    flat = normalized(text)
    for label, sentence in printed.items():
        if normalized(sentence) not in flat:
            findings.append(f"{label} is not the computed figure ({sentence})")
    return findings


def coverage_findings(
    proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]
) -> list[str]:
    findings: list[str] = []
    new = proposed[COVERAGE].decode("utf-8")
    old = current[COVERAGE].decode("utf-8")
    if new.split("\n").count(BOUND_ROW) != 1:
        findings.append("the signed RFC1-26 closure row ruling P-75 Q3 names is not preserved exactly once")
    new_parts, old_parts = coverage_parts(new), coverage_parts(old)
    new_rows = {key: set(rows) for key, rows in new_parts.items()}
    for key, rows in old_parts.items():
        for row in rows:
            if row in new_rows[key]:
                continue
            if key == "B2" and _clause(row) in MOVED_FROM_B2:
                continue
            findings.append(f"signed Part {key} row edited or removed: {_clause(row)}")
    old_all = {row for rows in old_parts.values() for row in rows}
    for key, rows in new_parts.items():
        for row in rows:
            if row not in old_all and AMENDMENT_MARK not in row:
                findings.append(f"added Part {key} row does not say it is an amendment row: {_clause(row)}")
    clauses = {key: {_clause(r) for r in rows} for key, rows in new_parts.items()}
    for first, second in (("A", "B1"), ("A", "B2"), ("B1", "B2")):
        both = clauses[first] & clauses[second]
        if both:
            findings.append(f"clauses in both Part {first} and Part {second}: {sorted(both)}")
    for clause in MOVED_FROM_B2:
        if clause not in clauses["A"]:
            findings.append(f"{clause} left Part B2 but is not in Part A")

    sys.path.insert(0, str(ROOT / "scripts"))
    import build_three_surface_poc_spec_dependencies as generator

    reqs, errors = generator.parse(proposed[SPEC].decode("utf-8"))
    if not errors:
        union = {cid for _rid, warrants in reqs for cid in warrants["contracts"]}
        if union != clauses["A"]:
            findings.append(
                "Part A's clause set differs from the proposed contracts[] union: "
                f"only in Part A {sorted(clauses['A'] - union)}, "
                f"only in the union {sorted(union - clauses['A'])}"
            )
    if "**Amendment disclosure — the RFC1-26 closure row (ruling P-75 Q3).**" not in new:
        findings.append("the amendment disclosure for the preserved RFC1-26 row is missing")
    closure = [row for row in new_parts["A"] if row.startswith(CLOSURE_ROW_PREFIX)]
    if len(closure) != 1 or not _disposition(closure[0]).startswith("**Unknown**"):
        findings.append("closure itself is not disclosed as one Unknown RFC1-26 row")
    findings.extend(totals_findings(new))
    return findings


def companion_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    proposal = proposed[PROPOSAL].decode("utf-8")
    findings = []
    if "## Amendment — one identity, one vocabulary, one epistemic shape" not in proposal:
        findings.append("proposal does not carry the amendment section")
    if "- Inferred mappings, edges or missing intent." not in proposal:
        findings.append("proposal's non-goal against inferred mappings, edges or intent changed")
    return findings


# --- the manifest ------------------------------------------------------------

def render(values: dict[pathlib.Path, bytes]) -> str:
    lines = [
        f"# {TITLE}",
        "# Candidate: binds nothing until the owner signs it off.",
        f"# {len(SUBJECTS)} artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
        "# Rows hash the PROPOSED bytes: current bytes with proposed/*.patch",
        "# applied. They match the tree only after --apply, the sign-off step.",
    ]
    lines.extend(f"{sha256(values[rel])}  {rel.as_posix()}" for rel in SUBJECTS)
    return "\n".join(lines) + "\n"


def verify_manifest(text: str, expected: str) -> list[str]:
    rows = ROW.findall(text)
    if [path for _digest, path in rows] != [path.as_posix() for path in SUBJECTS]:
        return ["manifest path population or order differs"]
    if text != expected:
        return ["manifest differs from exact regeneration over proposed bytes"]
    return []


def structure_findings(
    proposed: dict[pathlib.Path, bytes], current: dict[pathlib.Path, bytes]
) -> list[str]:
    return (
        spec_findings(proposed[SPEC], current[SPEC])
        + dependency_findings(proposed)
        + coverage_findings(proposed, current)
        + companion_findings(proposed)
    )


def check() -> list[str]:
    findings: list[str] = []
    patches = patch_files()
    if [patch.name for patch in patches] != sorted(f"{path.name}.patch" for path in PATCHED):
        findings.append("proposed patch population differs from declared subjects")
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    current = current_bytes()
    for rel in SUBJECTS:
        changed = proposed[rel] != current[rel]
        if changed and rel not in PATCHED:
            findings.append(f"undeclared subject change: {rel}")
        if not changed and rel in PATCHED:
            findings.append(f"declared patched subject is unchanged: {rel}")
    findings.extend(structure_findings(proposed, current))
    target = ROOT / MANIFEST_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST_OUT}")
    else:
        findings.extend(verify_manifest(target.read_text(encoding="utf-8"), render(proposed)))
    return findings


# --- selftest ----------------------------------------------------------------

def _replace(data: bytes, old: str, new: str) -> bytes:
    if old.encode("utf-8") not in data:
        raise AssertionError(f"selftest fixture matched nothing: {old[:60]!r}")
    return data.replace(old.encode("utf-8"), new.encode("utf-8"), 1)


def selftest() -> int:
    proposed = proposed_bytes()
    current = current_bytes()
    baseline = structure_findings(proposed, current)
    if baseline:
        print(f"SELFTEST FAILED: the package does not verify before mutation: {baseline}")
        return 1
    spec, cov = proposed[SPEC].decode("utf-8"), proposed[COVERAGE].decode("utf-8")
    first_052 = spec.index("### Requirement: POC-REQ-052")
    req_054 = spec.index("### Requirement: POC-REQ-054")
    req_060 = spec.index("### Requirement: POC-REQ-060")
    moved_b2_row = (
        "| RFC6-1 | RFC1-qualified selection-reference identity scheme (entity kind + "
        "durable identity + evaluation/scenario qualifiers); POC builds no cross-surface "
        "selection/identity system |"
    )
    mutants: dict[str, tuple[pathlib.Path, bytes, str]] = {
        "bound row edited": (
            COVERAGE,
            _replace(proposed[COVERAGE], BOUND_ROW, BOUND_ROW.replace("covered | POC-REQ-052", "covered | POC-REQ-055")),
            "the signed RFC1-26 closure row ruling P-75 Q3 names is not preserved exactly once",
        ),
        "unrelated requirement drift": (
            SPEC,
            _replace(proposed[SPEC], "Orrery SHALL NOT render an edge", "Orrery SHALL NOT draw an edge"),
            "POC-REQ-052 changed; the amendment touches only POC-REQ-054, 055 and 060",
        ),
        "new requirement missing": (
            SPEC,
            (spec[:req_054] + spec[spec.index("### Requirement: POC-REQ-055"):]).encode("utf-8"),
            "requirement population or order differs",
        ),
        "new requirement misplaced": (
            SPEC,
            (spec[:first_052] + spec[req_054:req_060] + spec[first_052:req_054] + spec[req_060:]).encode("utf-8"),
            "requirement population or order differs",
        ),
        "slot may be absent": (
            SPEC,
            _replace(proposed[SPEC], "render Unknown with its reason and its resolution route — never absent,", "render Unknown with its reason, or be omitted — never"),
            "POC-REQ-054 lacks slot never absent, scored or positive",
        ),
        "flag widens the vocabulary": (
            SPEC,
            _replace(proposed[SPEC], "it\nnever adds the kind to that vocabulary.", "it\nadds the kind to that vocabulary."),
            "POC-REQ-055 lacks flag never widens the vocabulary",
        ),
        "Inferred counted as Observed": (
            SPEC,
            _replace(proposed[SPEC], "SHALL never count toward an Observed total or clear an\nUnknown", "MAY count toward an Observed total"),
            "POC-REQ-060 lacks Inferred never Observed or clearing",
        ),
        "signed 060 scenario dropped": (
            SPEC,
            _replace(proposed[SPEC], "#### Scenario: Unknown looks the same everywhere", "#### Scenario: Unknown looks alike"),
            "POC-REQ-060 lacks signed scenario kept",
        ),
        "decision key undefined": (
            SPEC,
            _replace(proposed[SPEC], "`POC-DIR-2026-09-21`\n  names", "`POC-DIR-2026-09-22`\n  names"),
            "reader notes do not define the POC-DIR-2026-09-21 decision key",
        ),
        "Part A union drift": (
            COVERAGE,
            "\n".join(line for line in cov.split("\n") if not line.startswith("| RFC6-12 |")).encode("utf-8"),
            "Part A's clause set differs from the proposed contracts[] union",
        ),
        "computed total drift": (
            COVERAGE,
            _replace(proposed[COVERAGE], "102 covered,", "103 covered,"),
            "Part A totals is not the computed figure",
        ),
        "family table drift": (
            COVERAGE,
            _replace(proposed[COVERAGE], "| RFC6 | 28 | 13 | 1 | 14 |", "| RFC6 | 28 | 12 | 1 | 15 |"),
            "family table RFC6 reads",
        ),
        "unmarked added row": (
            COVERAGE,
            _replace(proposed[COVERAGE], "| covered — Amendment row; extends the trust-floor", "| covered — extends the trust-floor"),
            "added Part A row does not say it is an amendment row: RFC1-26",
        ),
        "moved clause kept in B2": (
            COVERAGE,
            _replace(proposed[COVERAGE], "| RFC6-2 |", moved_b2_row + "\n| RFC6-2 |"),
            "clauses in both Part A and Part B2: ['RFC6-1']",
        ),
        "signed row edited elsewhere": (
            COVERAGE,
            _replace(proposed[COVERAGE], "| RFC9-48 | A tabular/non-3D equivalent", "| RFC9-48 | A tabular equivalent"),
            "signed Part A row edited or removed: RFC9-48",
        ),
        "disclosure dropped": (
            COVERAGE,
            _replace(proposed[COVERAGE], "**Amendment disclosure — the RFC1-26 closure row (ruling P-75 Q3).**", "**Note.**"),
            "the amendment disclosure for the preserved RFC1-26 row is missing",
        ),
        "closure claimed covered": (
            COVERAGE,
            _replace(
                proposed[COVERAGE],
                CLOSURE_ROW_PREFIX + " **Unknown** — Amendment row;",
                CLOSURE_ROW_PREFIX + " covered — Amendment row;",
            ),
            "closure itself is not disclosed as one Unknown RFC1-26 row",
        ),
        "dependency drift": (
            DEPENDENCIES,
            _replace(proposed[DEPENDENCIES], "26 requirement(s)", "27 requirement(s)"),
            "proposed GOVERNING-DEPENDENCIES.md differs from regeneration",
        ),
        "non-goal widened": (
            PROPOSAL,
            _replace(proposed[PROPOSAL], "- Inferred mappings, edges or missing intent.\n", ""),
            "proposal's non-goal against inferred mappings, edges or intent changed",
        ),
    }
    for name, (rel, mutated, expected) in mutants.items():
        values = dict(proposed)
        values[rel] = mutated
        found = structure_findings(values, current)
        if mutated == proposed[rel] or not any(f.startswith(expected) for f in found):
            print(f"SELFTEST FAILED: {name} did not fail on its predicate ({expected!r}); found {found}")
            return 1
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text(encoding="utf-8")
        context = next(line for line in original.splitlines() if line.startswith(" ") and line.strip())
        broken.write_text(original.replace(context, context + " drifted", 1), encoding="utf-8")
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a drifted patch applied")
            return 1
    manifest = render(proposed)
    rows = ROW.findall(manifest)
    reordered = manifest.replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, manifest):
        print("SELFTEST FAILED: manifest path-order mutation passed")
        return 1
    unpatched = next(rel for rel in SUBJECTS if rel not in PATCHED)
    drifted = render(proposed_bytes({unpatched: current[unpatched] + b"\nsubject drift\n"}))
    if not verify_manifest(drifted, manifest):
        print("SELFTEST FAILED: subject drift did not stale the manifest")
        return 1
    print(
        f"selftest: {len(mutants)} structure mutants, patch drift, manifest order "
        "and subject drift all fail closed on their own predicates"
    )
    return 0


# --- entry -------------------------------------------------------------------

def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is a sign-off-time operation; pass --at-adoption "
            "only in the owner's sign-off change"
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
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
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
            sys.stdout.write(patch.read_text(encoding="utf-8"))
        return 0
    if args.apply:
        return apply(args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("Three-Surface POC identity amendment package does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        totals = coverage_totals(proposed_bytes()[COVERAGE].decode("utf-8"))
        print(
            f"Three-Surface POC identity amendment manifest matches {len(SUBJECTS)} "
            f"proposed subjects ({len(PATCHED)} patched, {len(SUBJECTS) - len(PATCHED)} "
            f"unchanged); 26 requirements, Part A {totals['a_clauses']} clauses over "
            f"{totals['a_rows']} rows; structure, regeneration and the preserved "
            "RFC1-26 row verify"
        )
        return 0
    if not args.write:
        print("refusing: pass --write to regenerate the manifest, or --check to verify it")
        return 2
    proposed = proposed_bytes()
    structure = structure_findings(proposed, current_bytes())
    if structure:
        for finding in structure:
            print(f"  {finding}")
        return 1
    target = ROOT / MANIFEST_OUT
    target.write_text(render(proposed), encoding="utf-8")
    print(f"wrote {MANIFEST_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
