#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB container-shape profile amendment package.

N8 (`syzygy-u05.8`), drafted under the 2026-09-26 sitting's §6 ruling. The
amendment lets the observed project's profile declare each class's extraction
rule from a closed vocabulary of nine container shapes and eight key forms,
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
VOCABULARY_OPENING = "- A **container shape** is how one class's items sit inside a source."
PROFILE_OPENING = "- The **project profile** declares the extraction rules."
BUTLERS_OPENING = (
    "- Butlers' profile declares exactly the following extraction grammar, "
    "which is\n  literal:\n"
)
#: The pre-amendment opening of the Butlers grammar bullet. It must be gone:
#: the grammar is now Butlers' declaration, not the only grammar.
RETIRED_OPENING = "- The extraction grammar is literal:\n"
GRAMMAR_END = "  Heading levels/text, top-level list depth"
#: The closed shape vocabulary, name -> the sentence the spec gives it
#: (compared after whitespace folding). Order is the spec's order.
SHAPES = {
    "heading-section": (
        "the body under one exact heading, up to the next heading at the same "
        "or a higher level."
    ),
    "every-level-2-section": (
        "every H2 in the file with its section body, in file order."
    ),
    "top-level-decimal-list": (
        "each top-level numbered list item in the section; any other top-level "
        "list item makes the source malformed."
    ),
    "top-level-list": (
        "each top-level list item in the section, numbered or bulleted."
    ),
    "top-level-bulleted-list": (
        "each top-level bulleted list item in the section; a numbered item "
        "makes the source malformed."
    ),
    "first-table-rows": (
        "each body row of the first table in the section; a row with the wrong "
        "cell count makes the source malformed."
    ),
    "ordinal-section-table-rows": (
        "each body row of every table under an H2 whose text begins with a "
        "decimal plus optional lowercase suffix."
    ),
    "tree-path": "the Git tree path itself; no body is parsed.",
    "toml-table-field": (
        "one field of one TOML table, present exactly once; anything else makes "
        "the source malformed."
    ),
}
SHAPE_ENTRY = re.compile(r"^  - `([^`\n]+)`: ", re.MULTILINE)
PROFILE_RULES = {
    "carried in the registry entry": (
        "carried in the project-shape observer's owner-adopted registry entry"
    ),
    "one source, heading, shape and key form": (
        "declares the source, the heading or tree rule, exactly one container "
        "shape and exactly one key form"
    ),
    "key forms closed at eight": "The key forms are closed at the eight",
    "key form: fixed key": "a fixed key;",
    "key form: leading bold phrase": "the leading bold phrase;",
    "key form: bold or code span": (
        "the leading bold or code span before the first dash;"
    ),
    "key form: prefixed ordinal": "a prefixed one-based ordinal;",
    "key form: first-column link text": "the first-column link text;",
    "key form: link target basename": "the link target basename;",
    "key form: tree directory": "the one tree directory;",
    "key form: H2 ordinal and label": (
        "an H2 ordinal with a first-column bold label."
    ),
    "missing or unknown rule is Unknown": (
        "A class whose rule is missing from the profile, or whose rule names a "
        "shape or key form outside these closed sets, makes its sources' item "
        "denominators Unknown"
    ),
    "no built-in substitute": "the observer never substitutes a built-in rule",
    "nothing added by a profile": (
        "A profile cannot add a class, a shape or a key form."
    ),
}

REQUIREMENT = "### Requirement: PWB-REQ-002"
NEXT_REQUIREMENT = "### Requirement: PWB-REQ-003"
PRECEDING_SCENARIO = "#### Scenario: Declared shape reconciles"
WARRANTS = "```yaml\nwarrants:"
REQUIREMENT_RULES = {
    "body: profile rule": (
        "declared item discovered by the extraction rule its project profile "
        "declares, using only the closed container-shape vocabulary, across"
    ),
    "case: missing-rule case": "and a profile missing one class's rule.",
    "oracle: profile grammar": (
        "two independent extractors apply the literal grammar declared by the "
        "project profile"
    ),
    "oracle: written Butlers grammar": (
        "for Butlers, both also apply the grammar written in these reader "
        "definitions and must produce the same identities;"
    ),
    "falsifier: undeclared shape": (
        "an item is read through a shape the profile does not declare"
    ),
    "falsifier: built-in fallback": (
        "a missing or unknown profile rule is replaced by a built-in one."
    ),
}
RETIRED_REQUIREMENT_TEXT = "declared item discovered by the closed extraction rule"
SCENARIOS = (
    "#### Scenario: Butlers' profile reproduces the written grammar",
    "#### Scenario: Profile rule is missing or names an unknown shape",
)
SCENARIO_RULES = {
    SCENARIOS[0]: (
        "extracted through the container shape the profile declares for it",
        "the identities and D equal those produced by the grammar written in "
        "these reader definitions",
    ),
    SCENARIOS[1]: (
        "names a shape or key form outside the closed sets",
        "stays counted with an Unknown item denominator",
        "no built-in rule or shape is used in its place",
    ),
}
CAPABILITY_ROW = (
    "| 4 | Account for every admitted declared item exactly once, reading each "
    "class only through the container shape its project profile declares from "
    "the closed nine-shape vocabulary, with no built-in fallback | covered — "
    "PWB-REQ-002 |"
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


def _grammar_items(text: str, opening: str) -> str | None:
    """The nine class bullets of the Butlers grammar, byte for byte."""
    at = text.find(opening)
    if at < 0:
        return None
    start = at + len(opening)
    end = text.find(GRAMMAR_END, start)
    return text[start:end] if end >= 0 else None


def reader_findings(text: str, current: str) -> list[str]:
    """The vocabulary, the profile rule and the retained Butlers grammar."""
    findings: list[str] = []
    start = text.find(READER_START)
    end = text.find(READER_END, start)
    if start < 0 or end < 0:
        return ["reader definitions are missing"]
    block = text[start:end]
    positions = []
    for label, opening in (
        ("vocabulary", VOCABULARY_OPENING),
        ("profile", PROFILE_OPENING),
        ("Butlers grammar", BUTLERS_OPENING),
    ):
        if text.count(opening) != 1 or block.count(opening) != 1:
            findings.append(f"missing or duplicate {label} bullet")
            positions.append(-1)
        else:
            positions.append(block.find(opening))
    if -1 not in positions and positions != sorted(positions):
        findings.append("vocabulary, profile and Butlers bullets are out of order")
    if RETIRED_OPENING in text:
        findings.append("the retired single-grammar opening is still present")
    if positions[0] >= 0 and positions[1] > positions[0]:
        vocabulary = block[positions[0]:positions[1]]
        names = SHAPE_ENTRY.findall(vocabulary)
        if names != list(SHAPES):
            findings.append(
                f"shape vocabulary differs: {names} is not {list(SHAPES)}"
            )
        for name, sentence in SHAPES.items():
            entry = re.search(
                rf"^  - `{re.escape(name)}`: ((?:[^\n]*\n)(?:    [^\n]*\n)*)",
                vocabulary,
                re.MULTILINE,
            )
            if not entry or fold(entry.group(1)) != fold(sentence):
                findings.append(f"shape sentence differs: {name}")
        if "closed at nine shapes, and no other shape is read" not in fold(vocabulary):
            findings.append("vocabulary is not stated closed at nine")
    if positions[1] >= 0 and positions[2] > positions[1]:
        profile = fold(block[positions[1]:positions[2]])
        for label, rule in PROFILE_RULES.items():
            if fold(rule) not in profile:
                findings.append(f"profile bullet lacks {label}")
    retained = _grammar_items(text, BUTLERS_OPENING)
    expected = _grammar_items(current, RETIRED_OPENING)
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
    findings = reader_findings(text, base)
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
        body = fold(_block(section, heading))
        for rule in SCENARIO_RULES[heading]:
            if fold(rule) not in body:
                findings.append(f"scenario lacks '{rule}': {heading}")
    base_start = base.find(REQUIREMENT)
    base_section = base[base_start:base.find(NEXT_REQUIREMENT, base_start)]
    base_warrants = base_section[base_section.find(WARRANTS):]
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
    killed += 2

    # Patch population: dropping the capability patch.
    without = [p for p in patch_files() if p.name != "CAPABILITY-COVERAGE.md.patch"]
    population = population_findings(without)
    if (
        "proposed patch population differs from declared subjects" not in population
        or f"declared patched subject is unchanged: {CAPABILITY_COVERAGE}" not in population
    ):
        return _fail("dropped-patch mutation passed the population predicate")
    killed += 1

    # Vocabulary: each shape's sentence altered, one shape dropped, one added,
    # two shapes swapped, and the closure sentence removed.
    for name, sentence in SHAPES.items():
        words = sentence.split()
        mutated_sentence = " ".join(words[:-1] + ["[changed]."])
        entry_at = spec.index(f"  - `{name}`: ")
        entry_end = spec.index("\n  - ", entry_at + 1) if name != "toml-table-field" else spec.index("\n- ", entry_at)
        mutated = spec[:entry_at] + f"  - `{name}`: {mutated_sentence}" + spec[entry_end:]
        if not spec_mutant(name, mutated, f"shape sentence differs: {name}"):
            return _fail(f"shape sentence mutation passed: {name}")
        killed += 1
    tree_line = "  - `tree-path`: the Git tree path itself; no body is parsed.\n"
    shape_mutants = {
        "shape dropped": spec.replace(tree_line, "", 1),
        "shape added": spec.replace(
            tree_line, tree_line + "  - `prose-paragraphs`: each paragraph.\n", 1
        ),
        "shape moved": spec.replace(
            tree_line, "", 1
        ).replace(
            "  - `heading-section`:", tree_line + "  - `heading-section`:", 1
        ),
    }
    for name, mutated in shape_mutants.items():
        if mutated == spec or not any(
            f.startswith("shape vocabulary differs") for f in requirement_findings(mutated.encode())
        ):
            return _fail(f"{name} mutation passed")
        killed += 1
    closure = _replace_once(
        spec,
        "closed at nine shapes, and no other shape is read",
        "open, and other shapes may be read",
        "closure",
    )
    if not spec_mutant("closure", closure, "vocabulary is not stated closed at nine"):
        return _fail("vocabulary closure mutation passed")
    killed += 1

    # Profile bullet: each rule removed on its own.
    profile_at = spec.index(PROFILE_OPENING)
    profile_end = spec.index(BUTLERS_OPENING)
    for label, rule in PROFILE_RULES.items():
        paragraph = fold(spec[profile_at:profile_end])
        mutated_paragraph = paragraph.replace(fold(rule), "[removed]", 1)
        if mutated_paragraph == paragraph:
            return _fail(f"profile-rule fixture matched nothing: {label}")
        mutated = spec[:profile_at] + mutated_paragraph + "\n" + spec[profile_end:]
        if not spec_mutant(label, mutated, f"profile bullet lacks {label}"):
            return _fail(f"profile-rule mutation passed: {label}")
        killed += 1

    # Bullet order, duplicates, the retired opening and the retained grammar.
    vocabulary_at = spec.index(VOCABULARY_OPENING)
    vocabulary = spec[vocabulary_at:profile_at]
    profile = spec[profile_at:profile_end]
    reader_mutants = {
        "bullets out of order": (
            spec[:vocabulary_at] + profile + vocabulary + spec[profile_end:],
            "vocabulary, profile and Butlers bullets are out of order",
        ),
        "duplicate profile bullet": (
            spec[:profile_end] + profile + spec[profile_end:],
            "missing or duplicate profile bullet",
        ),
        "missing Butlers bullet": (
            spec.replace(BUTLERS_OPENING, "- Butlers declares:\n", 1),
            "missing or duplicate Butlers grammar bullet",
        ),
        "retired opening restored": (
            spec.replace(BUTLERS_OPENING, BUTLERS_OPENING + RETIRED_OPENING, 1),
            "the retired single-grammar opening is still present",
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
        "declared item discovered by the extraction rule its project profile declares,\nusing only the closed container-shape vocabulary, across",
        "declared item discovered by the closed extraction rule across",
        "retired body",
    )
    if not spec_mutant("retired", restored, "PWB-REQ-002 still reads the closed extraction rule"):
        return _fail("retired requirement text mutation passed")
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
            CAPABILITY_ROW.replace("with no built-in fallback", "with a built-in fallback").encode(),
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
            " - **Case (sweep)**: enumerate the source population",
            " - **Case (sweep)**: enumerate each source population",
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

    if composition_findings():
        return _fail("sibling composition does not verify")
    print(
        f"selftest: {killed} mutants killed — stale manifest, path order, patch "
        f"population, {len(SHAPES)} shape sentences, shape dropped/added/"
        f"moved, vocabulary closure, {len(PROFILE_RULES)} profile rules, "
        "bullet order/duplicate/missing, retired opening, Butlers grammar "
        f"drift, {len(REQUIREMENT_RULES)} PWB-REQ-002 rules, retired "
        f"requirement text, {len(SCENARIOS)} scenarios x missing/duplicate/"
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
            f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); {len(SHAPES)} "
            f"shapes, {len(PROFILE_RULES)} profile rules, "
            f"{len(REQUIREMENT_RULES)} PWB-REQ-002 rules, {len(SCENARIOS)} "
            "scenarios, the retained Butlers grammar, dependency and "
            "contract-coverage regeneration and "
            f"{len(DECLARED_COMPOSITION)} declared sibling-composition outcomes verify"
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
