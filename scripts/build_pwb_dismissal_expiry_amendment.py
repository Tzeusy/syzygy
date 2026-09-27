#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB dismissal-expiry amendment package.

The signed PWB bytes are never edited while this package is a candidate.
Proposed bytes live as patches, and the manifest hashes the eleven-artifact
subject after those patches. Applying them is an adoption-time operation.

The package is drafted against the current tree and is proposed to land after
every sibling PWB package. The sibling-composition table below records, per
shared file, which patch pairs compose in both orders and which collide, so a
drifted sibling or a new shared file fails the check instead of passing it.
The composing siblings are also applied together, in table order, before this
package's patch, so a pairwise pass cannot hide a sequential failure.
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
CANDIDATE = CANDIDATES / "pwb-dismissal-expiry-amendment"
PROPOSED = CANDIDATE / "proposed"
MANIFEST_OUT = CANDIDATE / "PWB-DISMISSAL-EXPIRY-MANIFEST.txt"
TITLE = "PWB DISMISSAL-EXPIRY AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
DEPENDENCIES = CHANGE / "GOVERNING-DEPENDENCIES.md"
PROPOSAL = CHANGE / "proposal.md"
CAPABILITY_COVERAGE = CHANGE / "CAPABILITY-COVERAGE.md"
CONTRACT_REPAIR = CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md"
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
        (
            CAPABILITY_COVERAGE,
            CONTRACT_COVERAGE,
            CONTRACT_REPAIR,
            DEPENDENCIES,
            PROPOSAL,
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)

REQUIREMENT = "### Requirement: PWB-REQ-007"
NEXT_REQUIREMENT = "### Requirement: PWB-REQ-004"
CASE = "- **Case (sweep)**"
PARAGRAPH_OPENING = (
    "A claim MAY carry the `dismissed-by-decision` sibling surface state, and only"
)
PRECEDING_SCENARIO = "#### Scenario: Missing current evidence remains explicit Unknown"
SCENARIOS = (
    "#### Scenario: A dismissal lapses only through a new evaluation",
    "#### Scenario: A dismissal replaces the rendering, never the facts",
    "#### Scenario: A record that no longer applies is lapsed or retired, never refused",
)
WARRANTS = "```yaml\nwarrants:"
# Each rule the new paragraph must state, compared after whitespace folding.
PARAGRAPH_RULES = {
    "attributed human decision": "an attributed human decision",
    "reason and expiry": "states a reason and an expiry instant",
    "governed-plane record": "is committed to the governed plane",
    "identified evaluation input": (
        "Every dismissal record present in the governed plane at an "
        "evaluation's snapshot is an identified input of that evaluation"
    ),
    "Unknown-only scope": "Only a claim whose label is Unknown MAY be dismissed",
    "contradiction exclusion": (
        "never one whose primary reason is `contradicted-pending-adjudication`"
    ),
    "challenge exclusion": (
        "or `challenge-suspended`, which leaves only through its challenge's "
        "resolution"
    ),
    "no other dismissal source": (
        "Nothing else dismisses a claim: not a view preference, a query "
        "parameter, browser or daemon state, an owner note or a model assertion"
    ),
    "expiry boundary": (
        "only while that evaluation's as-of instant is earlier than the "
        "record's expiry instant"
    ),
    "reason currency": (
        "the claim's primary reason is still the one the record dismissed"
    ),
    "as-of instant only": (
        "SHALL decide this from its own as-of instant and never from the "
        "instant a page or answer is read"
    ),
    "lapse by new evaluation": (
        "a dismissal lapses only through a new identified evaluation"
    ),
    "facts stay visible": (
        "replaces the claim's status rendering and never its facts"
    ),
    "every fact named": (
        "the claim's label, tier, primary and secondary reasons, resolution "
        "route, freshness, challenge state, claim identity and evaluation "
        "identity stay visible and unchanged"
    ),
    "same surface": (
        "on the same surface as the claim and without further disclosure"
    ),
    "human and machine parity": (
        "disclosure, identically in the human and machine views"
    ),
    "no tuple change": "SHALL not change any tuple value",
    "never positive": "render as a positive, resolved, aligned or current state",
    "no favourable aggregate": (
        "count as resolved or favourable in any aggregate"
    ),
    "aggregate counts kept": (
        "Dismissed members SHALL remain in every per-label, tier, freshness "
        "and reason count of an aggregate"
    ),
    "aggregate expansion": (
        "SHALL additionally be counted and expandable as a sibling state"
    ),
    "three disclosed classes": (
        "is disclosed in exactly one of three classes, each distinct from the "
        "others and from a dismissal in effect"
    ),
    "class order": (
        "The classes are tested in order, refused first, then bound to a "
        "retired identity, then lapsed, and a record is disclosed in the first "
        "class whose test it meets"
    ),
    "refused records disclosed": (
        "It is a refused record when it lacks an author, reason, expiry "
        "instant, claim identity or dismissed primary reason"
    ),
    "refused by its own reason": (
        "or itself names, as the reason it dismisses, a primary reason that "
        "may not be dismissed"
    ),
    "lapse conditions": (
        "Otherwise it is a lapsed record when the evaluation's as-of instant "
        "is not earlier than its expiry instant, or the claim's primary reason "
        "is no longer the one it dismissed, including because the claim is no "
        "longer Unknown or its new primary reason is one that may not be "
        "dismissed"
    ),
    "lapsed records disclosed": (
        "a lapsed record is disclosed beside the claim with its reason, expiry "
        "instant, author, record identity and the condition that lapsed it"
    ),
    "retired identity": (
        "Otherwise it is bound to a retired identity when a split or merge has "
        "retired the claim identity it names; it is never transferred to a "
        "successor"
    ),
}
# Each rule a scenario's body must state, compared after whitespace folding.
SCENARIO_RULES = {
    SCENARIOS[0]: {
        "boundary evaluations": (
            "one evaluation's as-of instant falls before that instant and a "
            "second evaluation's as-of instant equals it exactly"
        ),
        "re-read unchanged": (
            "reading the first evaluation again after the expiry instant has "
            "passed renders the same claim state"
        ),
        "lapsed at the boundary": "discloses the record as lapsed",
        "no tuple change": "none of them changed by the dismissal",
    },
    SCENARIOS[1]: {
        "parity on the claim's surface": (
            "carry the same sibling state and the same complete tuple on the "
            "claim's own surface"
        ),
        "aggregate counts kept": (
            "keeps the claim in its per-label, tier, freshness and reason "
            "counts"
        ),
        "refused by its own reason": (
            "a record whose own dismissed primary reason is "
            "`contradicted-pending-adjudication`"
        ),
        "refused records": (
            "or `challenge-suspended`, each dismiss nothing and are disclosed "
            "as refused records"
        ),
    },
    SCENARIOS[2]: {
        "reason drift lapses": "is disclosed beside the claim as lapsed",
        "lapsed onto an undismissable reason": (
            "even when the claim's new primary reason is one that may not be "
            "dismissed"
        ),
        "no transfer": "is never transferred to a successor",
        "never refused": "neither record is disclosed as refused",
    },
}
# Each phrase a scenario's body must carry exactly once, so a second
# rendering claim for the same evaluation cannot be appended beside the first.
SCENARIO_ONCE = {
    SCENARIOS[0]: ("the first evaluation renders", "without the sibling state"),
}
# Wording that would let a dismissal act by reading time, leave the page,
# leave a count, come from another source or be refused by another route.
FORBIDDEN = {
    "clock": r"clock",
    "hide": r"\bhid(?:e|es|den|ing)\b",
    "collapse": r"collaps",
    "expire-on-read": r"expir\w*[- ]on[- ]read",
    "removal": r"\bremov\w*",
    "exclusion": r"\bexclu\w*",
    "second refusal route": r"refused record also|also (?:a )?refused",
    "permissive dismissal source": r"\b(?:MAY|can|could)\s+dismiss\b",
    "claim-reason refusal": r"naming a claim whose primary reason",
}
REQUIRED_WARRANTS = (
    "VIS-6", "RFC1-12", "RFC1-20", "RFC1-25", "RFC2-1", "RFC2-15"
)
PROPOSAL_TOKEN = (
    "A claim that renders Unknown may carry a recorded, attributed human "
    "dismissal with a reason and an expiry, committed to the governed plane."
)
CAPABILITY_ROW = (
    "| 32 | Admit an attributed, reasoned, expiring governed-plane dismissal of "
    "an Unknown claim, decided at each evaluation's as-of instant, replacing "
    "the rendering and never the facts | covered — PWB-REQ-007 |"
)
CAPABILITY_TOTALS = (
    "Totals: 26 covered, 6 lawfully out of scope, 0 Unknown/unresolved; 32 total."
)
# The gap rows stay Unknown until the owner decides which gap a claim-level
# dismissal binds (packet question 4); unadopted-draft is a used state.
REPAIR_DISPOSITIONS = {
    "RFC1-12.r1": ("RFC1-12.c1", "covered:PWB-REQ-007"),
    "RFC1-12.r2": ("RFC1-12.c1", "believed-not-applicable"),
    "RFC1-20.r1": ("RFC1-20.c1", "unknown-uncovered"),
    "RFC1-25.r1": ("RFC1-25.c14", "unknown-uncovered"),
    "RFC1-25.r2": ("RFC1-25.c14", "believed-not-applicable"),
    "RFC2-1.r2": ("RFC2-1.c12", "unknown-uncovered"),
    "RFC2-1.r3": ("RFC2-1.c12", "covered:PWB-REQ-007"),
    "RFC2-15.r1": ("RFC2-15.c2", "unknown-uncovered"),
    "RFC6-14.r4": ("RFC6-14.c5", "covered:PWB-REQ-007"),
    "RFC6-14.r5": ("RFC6-14.c5", "unknown-uncovered"),
    "RFC6-14.r6": ("RFC6-14.c5", "unknown-uncovered"),
    "RFC6-17.r7": ("RFC6-17.c2", "covered:PWB-REQ-007"),
}

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
    ("lane-b", "spec.md.patch"): "collide",
    ("missing-currency-dov.20", "CAPABILITY-COVERAGE.md.patch"): "compose",
    ("missing-currency-dov.20", "CONTRACT-COVERAGE-REPAIR-DELTA.md.patch"): "collide",
    ("missing-currency-dov.20", "CONTRACT-COVERAGE.md.patch"): "collide",
    ("missing-currency-dov.20", "GOVERNING-DEPENDENCIES.md.patch"): "collide",
    ("missing-currency-dov.20", "proposal.md.patch"): "compose",
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


def scenario_body(text: str, heading: str) -> str:
    """A scenario's text from its heading to the next heading or warrants."""
    start = text.index(heading) + len(heading)
    stops = [at for at in (text.find("\n#### ", start), text.find("\n```yaml", start)) if at >= 0]
    return text[start:min(stops)] if stops else text[start:]


def forbidden_findings(where: str, text: str) -> list[str]:
    return [
        f"{where} uses forbidden {label} wording"
        for label, pattern in FORBIDDEN.items()
        if re.search(pattern, text, re.IGNORECASE)
    ]


def requirement_findings(spec: bytes) -> list[str]:
    """The paragraph, the scenarios and the warrants sit inside PWB-REQ-007."""
    text = spec.decode("utf-8")
    findings: list[str] = []
    start = text.find(REQUIREMENT)
    end = text.find(NEXT_REQUIREMENT, start)
    if start < 0 or end < 0:
        return ["PWB-REQ-007 or its following requirement is missing"]
    section = text[start:end]
    if text.count(PARAGRAPH_OPENING) != 1:
        findings.append("missing or duplicate dismissal paragraph")
    else:
        opening = section.find(PARAGRAPH_OPENING)
        case = section.find(CASE)
        if not 0 <= opening < case:
            findings.append(
                "dismissal paragraph is not in the required PWB-REQ-007 position"
            )
        else:
            paragraph = fold(section[opening:case])
            for label, rule in PARAGRAPH_RULES.items():
                if fold(rule) not in paragraph:
                    findings.append(f"dismissal paragraph lacks {label}")
            findings.extend(forbidden_findings("dismissal paragraph", paragraph))
    preceding = section.find(PRECEDING_SCENARIO)
    warrants = section.find(WARRANTS)
    for heading in SCENARIOS:
        if text.count(heading) != 1:
            findings.append(f"missing or duplicate scenario: {heading}")
            continue
        at = section.find(heading)
        if not 0 <= preceding < at < warrants:
            findings.append(
                f"scenario is not in the required PWB-REQ-007 position: {heading}"
            )
            continue
        body = fold(scenario_body(section, heading))
        for label, rule in SCENARIO_RULES[heading].items():
            if fold(rule) not in body:
                findings.append(f"scenario lacks {label}: {heading}")
        for phrase in SCENARIO_ONCE.get(heading, ()):
            if body.count(fold(phrase)) != 1:
                findings.append(f"scenario does not say {phrase!r} exactly once: {heading}")
        findings.extend(forbidden_findings(f"scenario {heading}", body))
    block = section[warrants:] if warrants >= 0 else ""
    for authority in REQUIRED_WARRANTS:
        if not re.search(rf"[\[ ,]{re.escape(authority)}[\],]", block):
            findings.append(f"PWB-REQ-007 warrants lack {authority}")
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
    proposal = proposed[PROPOSAL].decode("utf-8")
    capability = proposed[CAPABILITY_COVERAGE].decode("utf-8")
    repair = proposed[CONTRACT_REPAIR].decode("utf-8")
    if fold(PROPOSAL_TOKEN) not in fold(proposal):
        findings.append("proposal does not carry the dismissal obligation")
    if capability.count(CAPABILITY_ROW) != 1:
        findings.append("capability coverage does not carry row 32 exactly once")
    if CAPABILITY_TOTALS not in capability or "Population: 32 positive" not in capability:
        findings.append("capability coverage population or totals are not 32")
    for repair_id, (supersedes, disposition) in REPAIR_DISPOSITIONS.items():
        rows = [line for line in repair.splitlines() if line.startswith(f"| {repair_id} |")]
        if len(rows) != 1:
            findings.append(f"{repair_id} is missing or duplicated")
            continue
        cells = [cell.strip() for cell in rows[0].strip("|").split("|")]
        if cells[1] != supersedes or cells[-1] != disposition:
            findings.append(
                f"{repair_id} does not supersede {supersedes} as {disposition}"
            )

    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_contract_coverage as coverage

    # The coverage generator checks each covered row against the spec's
    # warrants, which it reads from disk; this package changes those warrants,
    # so serve it the proposed spec bytes for that one path.
    spec_path = pathlib.Path(coverage.dependencies.SPEC).resolve()
    proposed_spec = proposed[SPEC].decode("utf-8")
    original_read = coverage.base.read

    def read(path: str) -> str:
        if pathlib.Path(path).resolve() == spec_path:
            return proposed_spec
        return original_read(path)

    coverage.base.read = read
    try:
        rendered = coverage.render(repair_text=repair)
    except ValueError as error:
        findings.append(f"contract-coverage repair does not validate: {error}")
    else:
        if rendered.encode("utf-8") != proposed[CONTRACT_COVERAGE]:
            findings.append(
                "proposed CONTRACT-COVERAGE.md differs from regeneration over "
                "the proposed repair delta"
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
                if target == SPEC and requirement_findings(first):
                    findings.append(f"{name} composition misplaces this package's text")
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


def sequential_findings(
    mine: dict[str, pathlib.Path] | None = None,
    declared: dict[tuple[str, str], str] | None = None,
) -> list[str]:
    """Apply every composing sibling patch in table order, then this one."""
    if mine is None:
        mine = {patch.name: patch for patch in patch_files()}
    declared = DECLARED_COMPOSITION if declared is None else declared
    findings: list[str] = []
    for name, patch in sorted(mine.items()):
        order = [
            ROOT / directory / "proposed" / name
            for sibling, directory in SIBLINGS.items()
            if declared.get((sibling, name)) == "compose"
        ]
        result = _compose(_target(patch), order + [patch])
        if result is None:
            findings.append(f"{name} does not apply after its composing siblings in order")
        elif _target(patch) == SPEC and requirement_findings(result):
            findings.append("sequential composition misplaces this package's text")
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
    if [patch.name for patch in patches] != [f"{path.name}.patch" for path in PATCHED]:
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


def check() -> list[str]:
    findings = population_findings(patch_files())
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(requirement_findings(proposed[SPEC]))
    findings.extend(dependency_findings(proposed))
    findings.extend(companion_findings(proposed))
    findings.extend(composition_findings())
    findings.extend(sequential_findings())
    target = ROOT / MANIFEST_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST_OUT}")
    else:
        findings.extend(verify_manifest(target.read_text(), render(proposed)))
    return findings


def _fail(name: str) -> int:
    print(f"SELFTEST FAILED: {name}")
    return 1


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        return _fail("behavior subject is not eleven unique paths")
    proposed = proposed_bytes()
    spec = proposed[SPEC]
    if requirement_findings(spec) or companion_findings(proposed) or dependency_findings(proposed):
        return _fail("unmutated proposed bytes do not verify")
    killed = 0

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

    # Patch population: dropping one declared patch.
    without_proposal = [p for p in patch_files() if p.name != "proposal.md.patch"]
    population = population_findings(without_proposal)
    if (
        "proposed patch population differs from declared subjects" not in population
        or f"declared patched subject is unchanged: {PROPOSAL}" not in population
    ):
        return _fail("dropped-patch mutation passed the population predicate")
    killed += 1

    # One mutant per paragraph rule, each isolating its own finding.
    text = spec.decode("utf-8")
    opening = text.index(PARAGRAPH_OPENING)
    case = text.index(CASE, opening)
    paragraph = text[opening:case]
    for label, rule in PARAGRAPH_RULES.items():
        folded = fold(paragraph)
        mutated_paragraph = folded.replace(fold(rule), "[removed]", 1)
        if mutated_paragraph == folded:
            return _fail(f"paragraph-rule fixture matched nothing: {label}")
        mutated = (text[:opening] + mutated_paragraph + "\n\n" + text[case:]).encode()
        found = requirement_findings(mutated)
        if f"dismissal paragraph lacks {label}" not in found:
            return _fail(f"paragraph-rule mutation passed: {label}")
        killed += 1

    # Paragraph missing, duplicated and moved out of PWB-REQ-007.
    next_start = text.index(NEXT_REQUIREMENT)
    next_case = text.index(CASE, next_start)
    moved = (
        text[:opening]
        + text[case:next_case]
        + paragraph
        + text[next_case:]
    ).encode()
    paragraph_mutants = {
        "missing paragraph": (
            text.replace(PARAGRAPH_OPENING, "A claim may be annotated", 1).encode(),
            "missing or duplicate dismissal paragraph",
        ),
        "duplicate paragraph": (
            (text[:case] + paragraph + text[case:]).encode(),
            "missing or duplicate dismissal paragraph",
        ),
        "misplaced paragraph": (
            moved,
            "dismissal paragraph is not in the required PWB-REQ-007 position",
        ),
    }
    for name, (mutated, expected) in paragraph_mutants.items():
        if expected not in requirement_findings(mutated):
            return _fail(f"{name} mutation passed")
        killed += 1

    # Each scenario missing, duplicated and moved into the next requirement.
    for heading in SCENARIOS:
        start = text.index(heading)
        stop = text.index("\n\n", text.index("- **AND**", start)) + 2
        block = text[start:stop]
        removed = text[:start] + text[stop:]
        next_heading_end = removed.index("\n", removed.index(NEXT_REQUIREMENT)) + 1
        misplaced = (
            removed[:next_heading_end] + "\n" + block + removed[next_heading_end:]
        )
        scenario_mutants = {
            "missing": (
                text.replace(heading + "\n", "", 1),
                f"missing or duplicate scenario: {heading}",
            ),
            "duplicate": (
                text.replace(heading + "\n", heading + "\n" + heading + "\n", 1),
                f"missing or duplicate scenario: {heading}",
            ),
            "misplaced": (
                misplaced,
                f"scenario is not in the required PWB-REQ-007 position: {heading}",
            ),
        }
        for name, (mutated, expected) in scenario_mutants.items():
            if expected not in requirement_findings(mutated.encode()):
                return _fail(f"{name} scenario mutation passed: {heading}")
            killed += 1

    # One mutant per scenario-body rule, each isolating its own finding.
    for heading, rules in SCENARIO_RULES.items():
        body = scenario_body(text, heading)
        at = text.index(heading) + len(heading)
        for label, rule in rules.items():
            folded = fold(body)
            if folded.count(fold(rule)) != 1:
                return _fail(f"scenario-rule fixture is not unique: {label}")
            mutated = (
                text[:at] + "\n\n" + folded.replace(fold(rule), "[removed]", 1)
                + text[at + len(body):]
            ).encode()
            if f"scenario lacks {label}: {heading}" not in requirement_findings(mutated):
                return _fail(f"scenario-rule mutation passed: {label}")
            killed += 1

    # Each forbidden wording, once in the paragraph and once in a scenario.
    fixtures = {
        "clock": "The reader's clock decides it.",
        "hide": "A page MAY hide the dismissed claim.",
        "collapse": "A view MAY collapse the claim's facts.",
        "expire-on-read": "A dismissal MAY expire on read.",
        "removal": "A dismissed Unknown claim is removed from the aggregate's Unknown total.",
        "exclusion": "A dismissed member is excluded from the freshness count.",
        "second refusal route": "It is a refused record also when its expiry has passed.",
        "permissive dismissal source": "A model assertion MAY dismiss a claim.",
        "claim-reason refusal": (
            "A record naming a claim whose primary reason is `challenge-suspended` is refused."
        ),
    }
    if set(fixtures) != set(FORBIDDEN):
        return _fail("forbidden fixtures do not cover every forbidden wording")
    first_heading = SCENARIOS[0]
    first_body_end = text.index(first_heading) + len(first_heading) + len(
        scenario_body(text, first_heading)
    )
    for label, sentence in fixtures.items():
        if [name for name, pattern in FORBIDDEN.items()
                if re.search(pattern, sentence, re.IGNORECASE)] != [label]:
            return _fail(f"forbidden fixture does not isolate: {label}")
        in_paragraph = (text[:case] .rstrip("\n") + " " + sentence + "\n\n" + text[case:]).encode()
        if f"dismissal paragraph uses forbidden {label} wording" not in requirement_findings(in_paragraph):
            return _fail(f"forbidden paragraph wording passed: {label}")
        in_scenario = (
            text[:first_body_end] + "\n  " + sentence + text[first_body_end:]
        ).encode()
        if f"scenario {first_heading} uses forbidden {label} wording" not in requirement_findings(in_scenario):
            return _fail(f"forbidden scenario wording passed: {label}")
        killed += 2

    # Round-2 review mutants: a second rendering claim in Scenario 1, one fact
    # dropped from the disclosure list, and Scenario 2's refusal reverted to
    # naming the claim's current reason.
    for heading, phrases in SCENARIO_ONCE.items():
        end = text.index(heading) + len(heading) + len(scenario_body(text, heading))
        for phrase in phrases:
            repeated = (text[:end] + "\n  " + phrase + text[end:]).encode()
            expected = f"scenario does not say {phrase!r} exactly once: {heading}"
            if expected not in requirement_findings(repeated):
                return _fail(f"repeated scenario phrase passed: {phrase}")
            killed += 1
    fact_list = fold(PARAGRAPH_RULES["every fact named"])
    folded = fold(paragraph)
    dropped_fact = folded.replace(fact_list, fact_list.replace("freshness, ", "", 1), 1)
    if dropped_fact == folded:
        return _fail("fact-list fixture matched nothing")
    mutated = (text[:opening] + dropped_fact + "\n\n" + text[case:]).encode()
    if "dismissal paragraph lacks every fact named" not in requirement_findings(mutated):
        return _fail("dropped-fact mutation passed")
    killed += 1
    reverted = text.replace(
        "whose own dismissed primary reason is", "naming a claim whose primary reason is", 1
    )
    if reverted == text:
        return _fail("scenario-2 reversion fixture matched nothing")
    found = requirement_findings(reverted.encode())
    if (
        f"scenario lacks refused by its own reason: {SCENARIOS[1]}" not in found
        or f"scenario {SCENARIOS[1]} uses forbidden claim-reason refusal wording" not in found
    ):
        return _fail("scenario-2 reversion passed")
    killed += 1

    # Each required warrant removed from PWB-REQ-007's block only.
    warrants_at = text.index(WARRANTS, text.index(REQUIREMENT))
    block_end = text.index("```\n", warrants_at + len(WARRANTS)) + 4
    block = text[warrants_at:block_end]
    for authority in REQUIRED_WARRANTS:
        stripped = re.sub(
            rf"(?<=\[){re.escape(authority)}, |, {re.escape(authority)}(?=[,\]])",
            "",
            block,
            count=1,
        )
        if stripped == block:
            return _fail(f"warrant fixture matched nothing: {authority}")
        mutated = (text[:warrants_at] + stripped + text[block_end:]).encode()
        if f"PWB-REQ-007 warrants lack {authority}" not in requirement_findings(mutated):
            return _fail(f"warrant mutation passed: {authority}")
        killed += 1

    # Generated companions: dependency and contract-coverage drift.
    tampered = dict(proposed)
    tampered[DEPENDENCIES] = proposed[DEPENDENCIES].replace(
        b"17 requirement(s)", b"18 requirement(s)", 1
    )
    if tampered[DEPENDENCIES] == proposed[DEPENDENCIES] or not dependency_findings(tampered):
        return _fail("generated dependency drift passed")
    coverage_drift = dict(proposed)
    coverage_drift[CONTRACT_COVERAGE] = proposed[CONTRACT_COVERAGE].replace(
        b"141 covered", b"142 covered", 1
    )
    if coverage_drift[CONTRACT_COVERAGE] == proposed[CONTRACT_COVERAGE] or not companion_findings(coverage_drift):
        return _fail("generated contract-coverage drift passed")
    killed += 2

    # Companion rules: proposal bullet, capability row and totals, each repair row.
    companion_mutants = {
        "proposal bullet": (
            PROPOSAL,
            b"A claim that renders Unknown may carry",
            b"A claim that renders Unknown may hide",
            "proposal does not carry the dismissal obligation",
        ),
        "capability row": (
            CAPABILITY_COVERAGE,
            CAPABILITY_ROW.encode(),
            CAPABILITY_ROW.replace("covered —", "Unknown —").encode(),
            "capability coverage does not carry row 32 exactly once",
        ),
        "capability totals": (
            CAPABILITY_COVERAGE,
            CAPABILITY_TOTALS.encode(),
            CAPABILITY_TOTALS.replace("32 total", "31 total").encode(),
            "capability coverage population or totals are not 32",
        ),
    }
    for repair_id, (supersedes, disposition) in REPAIR_DISPOSITIONS.items():
        flipped = (
            "unknown-uncovered" if disposition != "unknown-uncovered" else "covered:PWB-REQ-007"
        )
        row = re.search(
            rf"^\| {re.escape(repair_id)} \|[^\n]*$",
            proposed[CONTRACT_REPAIR].decode(),
            re.MULTILINE,
        ).group(0).encode()
        companion_mutants[f"repair row {repair_id}"] = (
            CONTRACT_REPAIR,
            row,
            row.replace(f"| {disposition} |".encode(), f"| {flipped} |".encode()),
            f"{repair_id} does not supersede {supersedes} as {disposition}",
        )
    for name, (rel, old, new, expected) in companion_mutants.items():
        mutated = dict(proposed)
        mutated[rel] = proposed[rel].replace(old, new, 1)
        if mutated[rel] == proposed[rel] or expected not in companion_findings(mutated):
            return _fail(f"{name} mutation passed")
        killed += 1

    # Patch drift: a corrupted spec patch neither applies nor composes.
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        corrupted = original.replace(
            " - **Case (sweep)**: enumerate every project entity",
            " - **Case (sweep)**: enumerate each project entity",
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

    # Composition table: every declared outcome flipped, and one pair dropped.
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

    # Sequential order: a broken patch, and a colliding sibling put in order.
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        broken.write_text(corrupted)
        mine = {patch.name: patch for patch in patch_files()}
        mine["spec.md.patch"] = broken
        if not sequential_findings(mine=mine):
            return _fail("corrupted patch passed sequential composition")
    forced = dict(DECLARED_COMPOSITION)
    forced[("lane-b", "spec.md.patch")] = "compose"
    if not sequential_findings(declared=forced):
        return _fail("a colliding sibling passed sequential composition")
    killed += 2

    if composition_findings() or sequential_findings():
        return _fail("sibling composition does not verify")
    print(
        f"selftest: {killed} mutants killed — stale manifest, path order, patch "
        f"population, {len(PARAGRAPH_RULES)} paragraph rules, paragraph "
        f"missing/duplicate/placement, {len(SCENARIOS)} scenarios x "
        "missing/duplicate/placement, "
        f"{sum(len(rules) for rules in SCENARIO_RULES.values())} scenario-body "
        f"rules, {len(FORBIDDEN)} forbidden wordings x paragraph/scenario, "
        f"{sum(len(p) for p in SCENARIO_ONCE.values())} once-only scenario "
        "phrases, a dropped fact, the scenario-2 reversion, "
        f"{len(REQUIRED_WARRANTS)} warrants, "
        "dependency and contract-coverage drift, proposal, capability row and "
        f"totals, {len(REPAIR_DISPOSITIONS)} repair rows, patch drift, "
        f"{len(DECLARED_COMPOSITION)} composition outcomes, two table-shape "
        "and two sequential-order mutants all fail closed"
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
            print("PWB dismissal-expiry package does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(
            f"PWB dismissal-expiry manifest matches {len(BEHAVIOR_SUBJECTS)} "
            f"proposed subjects ({len(PATCHED)} patched, "
            f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); requirement, "
            "companion, dependency regeneration, "
            f"{len(DECLARED_COMPOSITION)} declared sibling-composition outcomes "
            "and the sequential sibling order verify"
        )
        return 0
    if not args.write:
        print(
            "refusing: regenerating the manifest retires copied act arguments; "
            "pass --write and update every registered digest copy"
        )
        return 2
    proposed = proposed_bytes()
    structure = (
        population_findings(patch_files())
        + requirement_findings(proposed[SPEC])
        + dependency_findings(proposed)
        + companion_findings(proposed)
    )
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
