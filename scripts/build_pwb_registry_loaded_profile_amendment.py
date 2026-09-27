#!/usr/bin/env python3
"""Build and verify the inert PWB registry loaded-profile amendment.

This script performs no owner act and writes no act record. Its subject is
the Polaris Butlers project-shape observer registry entry, whose current
bytes are the argument of a performed `adopt-registry-entry` act. The
proposed bytes therefore live only as one unified diff under `proposed/`.

The diff is drafted on top of the `syzygy-dov.18` currency-and-briefing
candidate, which edits the same subject and lands first. `--check` builds
the base the same way whichever state the tree is in:

- `.18` not yet adopted: current bytes, then `.18`'s patch, then this one;
- `.18` adopted (the subject hashes to `.18`'s manifest row): current bytes,
  then this patch alone.

Either way the manifest row is the digest a superseding
`adopt-registry-entry` act would take as its argument. It matches the tree
only after `--apply --at-adoption`.

The fields this package adds restate the source grammar the observer
applies today. `--check` proves that three ways: the six existing grammar
keys and every other entry field are unchanged; every heading literal is
present in the specification's reader definitions; and the root index
path, pillar labels, heading literals and per-source bindings match the
constants in `packages/three-surface-poc-core/src/`. The constants cross-check
is retired by the change that deletes the constants (M8 slice 5 limb 5),
which then owns the loaded-profile test itself.

Bare invocation refuses to overwrite the manifest; pass `--write`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
SUBJECT = pathlib.Path(
    ".syzygy/governance/declarations/adapter-registry/"
    "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
)
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
CANDIDATE = CANDIDATES / "pwb-registry-loaded-profile-amendment"
PROPOSED = CANDIDATE / "proposed"
OUT = CANDIDATE / "PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt"
TITLE = "PWB REGISTRY LOADED-PROFILE EFFECT AMENDMENT MANIFEST"

#: The `.18` package this one is drafted on top of.
PRIOR = CANDIDATES / "pwb-registry-currency-briefing-amendment"
PRIOR_PATCH = PRIOR / "proposed" / f"{SUBJECT.name}.patch"
PRIOR_MANIFEST = PRIOR / "PWB-EFFECT-AMENDMENT-MANIFEST.txt"

SPEC = pathlib.Path(
    "openspec/changes/polaris-project-wide-butlers-model/specs/"
    "polaris-project-wide-butlers-model/spec.md"
)
CORE = pathlib.Path("packages/three-surface-poc-core/src")

PROPOSED_VERSION = "1.3.0-candidate.1"
BASE_VERSION = "1.2.0-candidate.1"

#: The six grammar keys the performed act already binds, unchanged here.
EXISTING_GRAMMAR_KEYS = (
    "factFamilies",
    "fixedClassKeys",
    "fixedCatalogKeys",
    "fixedProjectAccountKeys",
    "rootSummary",
    "precedence",
)
#: The keys this package adds, in order.
ADDED_GRAMMAR_KEYS = (
    "rootIndex",
    "pillars",
    "sourcePopulation",
    "containerShapes",
    "classGrammar",
    "sourceGrammarSemantics",
)
SEMANTICS_KEYS = (
    "scope",
    "headingMatch",
    "containerShape",
    "rootIndependent",
    "missingField",
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def current_bytes(override: bytes | None = None) -> bytes:
    if override is not None:
        return override
    target = ROOT / SUBJECT
    if not target.is_file():
        raise ValueError(f"missing amendment subject: {SUBJECT.as_posix()}")
    return target.read_bytes()


def patch_files() -> list[pathlib.Path]:
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda p: p.name)


def _apply(body: bytes, patches: list[pathlib.Path], what: str) -> bytes:
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / SUBJECT).parent.mkdir(parents=True, exist_ok=True)
        (base / SUBJECT).write_bytes(body)
        for patch in patches:
            done = subprocess.run(
                ["git", "apply", "--whitespace=nowarn", str(patch)],
                cwd=base, capture_output=True, text=True,
            )
            if done.returncode != 0:
                raise ValueError(
                    f"{patch.name} ({what}) does not apply to "
                    f"{SUBJECT.as_posix()}: {done.stderr.strip()}")
        return (base / SUBJECT).read_bytes()


def prior_row(text: str | None = None) -> str | None:
    """`.18`'s manifest digest, or None when that package is absent."""
    if text is None:
        target = ROOT / PRIOR_MANIFEST
        if not target.is_file():
            return None
        text = target.read_text()
    rows = ROW.findall(text)
    if len(rows) != 1 or rows[0][1] != SUBJECT.as_posix():
        raise ValueError(f"{PRIOR_MANIFEST.as_posix()} does not carry one subject row")
    return rows[0][0]


def base_bytes(override: bytes | None = None,
               prior_digest: str | None | bool = False,
               prior_patch: pathlib.Path | None = None) -> tuple[bytes, str]:
    """The bytes this package's patch applies to, and which state produced them."""
    body = current_bytes(override)
    digest = prior_row() if prior_digest is False else prior_digest
    if digest is not None and sha256(body) == digest:
        return body, ".18 adopted: current bytes"
    patch = ROOT / PRIOR_PATCH if prior_patch is None else prior_patch
    if not patch.is_file():
        raise ValueError(
            "the .18 package is neither adopted nor present; this package is "
            "drafted on top of it and must be rebased")
    return _apply(body, [patch], ".18"), ".18 pending: current bytes + .18 patch"


def proposed_bytes(override: bytes | None = None,
                   patches: list[pathlib.Path] | None = None) -> bytes:
    base, _state = base_bytes(override)
    patches = patch_files() if patches is None else patches
    if not patches:
        raise ValueError(f"no proposed patch under {PROPOSED.as_posix()}")
    return _apply(base, patches, "this package")


# ---------------------------------------------------------------------
# What the proposed bytes must say.

def _entry(doc: object) -> dict | None:
    if not isinstance(doc, dict):
        return None
    entries = doc.get("entries")
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        return None
    return entries[0]


def unchanged_findings(proposed: bytes, base: bytes) -> list[str]:
    """Only the two versions and the added grammar keys may move."""
    try:
        new, old = json.loads(proposed), json.loads(base)
    except ValueError as error:
        return [f"not valid JSON: {error}"]
    findings: list[str] = []
    new_entry, old_entry = _entry(new), _entry(old)
    if new_entry is None or old_entry is None:
        return ["proposed or base bytes do not carry exactly one registry entry"]
    for key in set(new) | set(old):
        if key in ("entries", "registryVersion"):
            continue
        if new.get(key) != old.get(key):
            findings.append(f"top-level field changed: {key}")
    for key in set(new_entry) | set(old_entry):
        if key in ("observationGrammar", "observerVersion"):
            continue
        if new_entry.get(key) != old_entry.get(key):
            findings.append(f"entry field changed: {key}")
    grammar, before = new_entry.get("observationGrammar"), old_entry.get("observationGrammar")
    if not isinstance(grammar, dict) or not isinstance(before, dict):
        return findings + ["observationGrammar is not an object"]
    if tuple(before) != EXISTING_GRAMMAR_KEYS:
        findings.append("the base grammar no longer carries the six bound keys in order")
    for key in EXISTING_GRAMMAR_KEYS:
        if grammar.get(key) != before.get(key):
            findings.append(f"bound grammar key changed: {key}")
    if tuple(grammar) != EXISTING_GRAMMAR_KEYS + ADDED_GRAMMAR_KEYS:
        findings.append("grammar key population or order differs from the declared set")
    return findings


def _positive_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _headings(row: dict) -> list[dict]:
    if "heading" in row:
        return [row["heading"]]
    return list(row.get("headings", []))


def structure_findings(body: bytes) -> list[str]:
    findings: list[str] = []
    try:
        doc = json.loads(body)
    except ValueError as error:
        return [f"proposed bytes are not valid JSON: {error}"]
    if doc.get("registryVersion") != PROPOSED_VERSION:
        findings.append(f"registryVersion is not {PROPOSED_VERSION}")
    entry = _entry(doc)
    if entry is None:
        return findings + ["proposed bytes do not carry exactly one registry entry"]
    if entry.get("observerVersion") != PROPOSED_VERSION:
        findings.append(f"observerVersion is not {PROPOSED_VERSION}")
    g = entry.get("observationGrammar")
    if not isinstance(g, dict):
        return findings + ["observationGrammar is not an object"]
    classes = g.get("fixedClassKeys") or []

    pillars = g.get("pillars")
    pillar_keys: list[str] = []
    if not isinstance(pillars, list) or not pillars:
        findings.append("pillars is missing or empty")
    else:
        for p in pillars:
            if not isinstance(p, dict) or set(p) != {"key", "label"} or not all(
                    isinstance(p[k], str) and p[k] for k in ("key", "label")):
                findings.append(f"pillar row malformed: {p!r}")
            else:
                pillar_keys.append(p["key"])
        if len(set(pillar_keys)) != len(pillar_keys):
            findings.append("a pillar key is declared twice")

    root = g.get("rootIndex")
    if not isinstance(root, dict) or not isinstance(root.get("path"), str) or not root["path"]:
        findings.append("rootIndex.path is missing")

    pop = g.get("sourcePopulation")
    rules: list[str] = []
    if not isinstance(pop, dict):
        findings.append("sourcePopulation is not an object")
        pop = {}
    else:
        if not _positive_int(pop.get("indexChainDepth")):
            findings.append("indexChainDepth is not a positive integer")
        rules = pop.get("sourceRules") or []
        trees = pop.get("treePopulations")
        if not isinstance(trees, list) or not trees:
            findings.append("treePopulations is missing or empty")
        else:
            for t in trees:
                if not isinstance(t, dict) or t.get("rule") not in rules:
                    findings.append(f"tree population names an undeclared rule: {t!r}")
                elif not isinstance(t.get("rootIndependent"), bool):
                    findings.append(f"rootIndependent is not a boolean: {t.get('rule')}")
                elif "<key>" not in str(t.get("pathPattern", "")):
                    findings.append(f"tree pathPattern has no <key>: {t.get('rule')}")
        bound: set[str] = set()
        for b in pop.get("extractionBindings") or []:
            if not isinstance(b, dict) or b.get("rule") not in rules:
                findings.append(f"extraction binding names an undeclared rule: {b!r}")
                continue
            if "pillar" in b and b["pillar"] not in pillar_keys:
                findings.append(f"extraction binding names an undeclared pillar: {b['pillar']}")
            for c in b.get("classes") or []:
                if c not in classes:
                    findings.append(f"extraction binding names an undeclared class: {c}")
                bound.add(c)
        if bound != set(classes):
            findings.append("extraction bindings do not cover exactly the declared classes")

    shapes = g.get("containerShapes")
    if not isinstance(shapes, dict) or not shapes:
        findings.append("containerShapes is missing or empty")
        shapes = {}
    for name, sentence in shapes.items():
        if not isinstance(sentence, str) or not sentence.strip():
            findings.append(f"container shape without a sentence: {name}")

    grammar = g.get("classGrammar")
    used: set[str] = set()
    covered: set[str] = set()
    account_keys: list[str] = []
    if not isinstance(grammar, list) or not grammar:
        findings.append("classGrammar is missing or empty")
        grammar = []
    for row in grammar:
        if not isinstance(row, dict):
            findings.append(f"class grammar row is not an object: {row!r}")
            continue
        cls = row.get("class")
        if cls not in classes:
            findings.append(f"class grammar names an undeclared class: {cls}")
        covered.add(cls)
        shape = row.get("container")
        if shape not in shapes:
            findings.append(f"class grammar row names an undeclared container shape: {cls} {shape}")
        used.add(shape)
        if not isinstance(row.get("itemKey"), str) or not row["itemKey"]:
            findings.append(f"class grammar row has no itemKey: {cls}")
        for h in _headings(row):
            if not isinstance(h, dict) or not isinstance(h.get("text"), str) or not h["text"]:
                findings.append(f"heading without text: {cls}")
            elif "level" in h and h["level"] not in (1, 2, 3, 4, 5, 6):
                findings.append(f"heading level out of range: {cls} {h['level']}")
        if cls == "project-account-section":
            account_keys.append(row.get("key"))
        if row.get("headingsFrom") not in (None, "fixedCatalogKeys"):
            findings.append(f"headingsFrom names an unknown list: {row.get('headingsFrom')}")
    if covered != set(classes):
        findings.append("class grammar does not cover exactly the declared classes")
    unused = set(shapes) - used
    if unused:
        findings.append(f"container shape declared and never used: {sorted(unused)}")
    if account_keys != list(g.get("fixedProjectAccountKeys") or []):
        findings.append("project-account rows do not match fixedProjectAccountKeys in order")

    sem = g.get("sourceGrammarSemantics")
    if not isinstance(sem, dict) or tuple(sem) != SEMANTICS_KEYS:
        findings.append("sourceGrammarSemantics key population or order differs")
    else:
        for key, sentence in sem.items():
            if not isinstance(sentence, str) or not sentence.strip():
                findings.append(f"sourceGrammarSemantics sentence is empty: {key}")
    return findings


# ---------------------------------------------------------------------
# Does it restate today's grammar? Two independent witnesses.

def reader_definitions(spec_text: str) -> str:
    start = spec_text.find("Reader definitions:")
    end = spec_text.find("## ADDED Requirements")
    if start < 0 or end < start:
        raise ValueError(f"{SPEC.as_posix()} has no reader-definitions block")
    return spec_text[start:end]


def spec_findings(body: bytes, spec_text: str) -> list[str]:
    """Every heading literal and catalog key appears in the reader definitions."""
    block = " ".join(reader_definitions(spec_text).split())
    g = _entry(json.loads(body))["observationGrammar"]
    findings = []
    literals = [h["text"] for row in g["classGrammar"] for h in _headings(row)]
    literals += list(g["fixedCatalogKeys"])
    for text in literals:
        if text not in block:
            findings.append(f"heading literal not in the reader definitions: {text!r}")
    return findings


def _ts(name: str) -> str:
    target = ROOT / CORE / name
    if not target.is_file():
        raise ValueError(f"missing {(CORE / name).as_posix()}")
    return target.read_text()


def expected_code_lines(body: bytes) -> list[tuple[str, str]]:
    """Source lines the constants must contain if the profile restates them."""
    g = _entry(json.loads(body))["observationGrammar"]
    out: list[tuple[str, str]] = [
        ("project-shape-manifest.ts",
         f"export const PWB_ROOT_INDEX_PATH = '{g['rootIndex']['path']}';"),
        ("project-shape-manifest.ts",
         f"export const PWB_INDEX_DEPTH = {g['sourcePopulation']['indexChainDepth']};"),
        ("project-shape-manifest.ts",
         "export const PILLAR_KEYS = ["
         + ", ".join(f"'{p['key']}'" for p in g["pillars"]) + "] as const;"),
        ("project-shape-manifest.ts",
         "export const SOURCE_RULES = ["
         + ", ".join(f"'{r}'" for r in g["sourcePopulation"]["sourceRules"])
         + "] as const;"),
    ]
    for p in g["pillars"]:
        out.append(("project-shape-manifest.ts", f"  '{p['key']}': '{p['label']}',"))
    for b in g["sourcePopulation"]["extractionBindings"]:
        classes = "[" + ", ".join(f"'{c}'" for c in b["classes"]) + "]"
        if b["rule"] == "pillar-named-file" and b["pillar"] != "heart-and-soul":
            out.append(("project-shape-manifest.ts",
                        f"if (pillar === '{b['pillar']}' && relativePath === "
                        f"'{b['relativePath']}') return {classes};"))
        elif b["rule"] == "pillar-named-file":
            out.append(("project-shape-manifest.ts",
                        f"if (relativePath === '{b['relativePath']}') return {classes};"))
        elif b["rule"] == "pillar-index":
            out.append(("project-shape-manifest.ts",
                        f"if (pillar === '{b['pillar']}') return {classes};"))
        elif b["rule"] == "roster-tree":
            out.append(("project-shape-manifest.ts",
                        f"return relativePath === '{b['relativePath']}' ? {classes} : [];"))
        else:
            out.append(("project-shape-manifest.ts", f"return {classes};"))
    for t in g["sourcePopulation"]["treePopulations"]:
        pattern = "([^/]+)".join(
            re.escape(part).replace("/", "\\/") for part in t["pathPattern"].split("<key>"))
        out.append(("project-shape-manifest.ts", f"/^{pattern}$/"))
    for row in g["classGrammar"]:
        for h in _headings(row):
            out.append(("project-shape-extraction.ts", f"'{h['text']}'"))
    return out


def code_findings(body: bytes, reader=_ts) -> list[str]:
    findings = []
    sources: dict[str, str] = {}
    for name, line in expected_code_lines(body):
        text = sources.setdefault(name, reader(name))
        if line not in text:
            findings.append(f"{name} does not carry {line!r}")
    return findings


# ---------------------------------------------------------------------
# Manifest, population, composition.

def render(body: bytes) -> str:
    lines = [
        f"# {TITLE}",
        "# This row binds only by the owner act that takes its digest as the",
        "# argument of a superseding adopt-registry-entry act; until that act is",
        "# performed it binds nothing.",
        "# 1 artifact; the row hashes the PROPOSED bytes: the subject with the",
        "# syzygy-dov.18 patch (unless already adopted) and then proposed/*.patch",
        "# applied. It matches the tree only after --apply, the adoption step.",
        "# The subject's current bytes stay the argument of the act in force.",
        f"{sha256(body)}  {SUBJECT.as_posix()}",
    ]
    return "\n".join(lines) + "\n"


def manifest_findings(text: str | None, expected: str) -> list[str]:
    if text is None:
        return [f"manifest missing: {OUT.as_posix()}"]
    rows = ROW.findall(text)
    if [path for _d, path in rows] != [SUBJECT.as_posix()]:
        return ["manifest row population or path differs"]
    if text != expected:
        return ["manifest differs from exact regeneration over the proposed bytes"]
    return []


def patch_population_findings(patches: list[pathlib.Path]) -> list[str]:
    if [p.name for p in patches] != [f"{SUBJECT.name}.patch"]:
        return ["proposed/*.patch population is not the single declared subject "
                "patch: " + ", ".join(p.name for p in patches)]
    return []


def noop_findings(proposed: bytes, base: bytes) -> list[str]:
    if proposed == base:
        return [f"the proposed patch changes nothing: {SUBJECT.as_posix()}"]
    return []


def composition_findings(root: pathlib.Path | None = None) -> list[str]:
    """No candidate other than `.18` and this one patches the same subject."""
    root = ROOT if root is None else root
    allowed = {PRIOR.as_posix(), CANDIDATE.as_posix()}
    findings = []
    for patch in sorted((root / CANDIDATES).glob(f"*/proposed/{SUBJECT.name}.patch")):
        package = patch.parent.parent.relative_to(root).as_posix()
        if package not in allowed:
            findings.append(
                f"undeclared sibling patches the same subject: {package}; declare "
                "the landing order and rebase before either act")
    return findings


def check() -> list[str]:
    findings: list[str] = []
    findings.extend(patch_population_findings(patch_files()))
    findings.extend(composition_findings())
    try:
        base, _state = base_bytes()
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(noop_findings(proposed, base))
    findings.extend(unchanged_findings(proposed, base))
    structural = structure_findings(proposed)
    findings.extend(structural)
    if not structural:
        findings.extend(spec_findings(proposed, (ROOT / SPEC).read_text()))
        try:
            findings.extend(code_findings(proposed))
        except ValueError as error:
            findings.append(str(error))
    target = ROOT / OUT
    findings.extend(manifest_findings(
        target.read_text() if target.is_file() else None, render(proposed)))
    return findings


# ---------------------------------------------------------------------
# Rule 6: every predicate above is mutated and must fail closed.

def selftest() -> int:
    findings = check()
    if findings:
        print("SELFTEST FAILED: the package does not verify on current bytes")
        for finding in findings:
            print(f"  {finding}")
        return 1
    base, _ = base_bytes()
    proposed = proposed_bytes()
    baseline = render(proposed)
    spec_text = (ROOT / SPEC).read_text()
    failures: list[str] = []
    count = 0

    def expect(label: str, got: list[str]) -> None:
        nonlocal count
        count += 1
        if not got:
            failures.append(label)

    def mutate(fn) -> bytes:
        doc = json.loads(proposed)
        fn(doc)
        return json.dumps(doc, indent=2).encode()

    def g(doc):
        return doc["entries"][0]["observationGrammar"]

    # Base-state composition.
    current = current_bytes()
    drifted = current.replace(b'"registryVersion": "1.1.0', b'"registryVersion": "1.1.9', 1)
    assert drifted != current
    try:
        proposed_bytes(drifted)
    except ValueError:
        count += 1
    else:
        failures.append("the patches applied over drifted subject bytes")
    # Drift outside every hunk's context still applies; the manifest catches it.
    distant = current.replace(b'"maxSources": 512', b'"maxSources": 513', 1)
    assert distant != current
    expect("subject drift outside the patch context",
           manifest_findings(baseline, render(proposed_bytes(distant))))
    try:
        base_bytes(prior_digest=None, prior_patch=ROOT / PRIOR / "absent.patch")
    except ValueError:
        count += 1
    else:
        failures.append("an absent, unadopted .18 package passed")
    adopted, state = base_bytes(override=base, prior_digest=sha256(base))
    count += 1
    if adopted != base or not state.startswith(".18 adopted"):
        failures.append("an adopted .18 state was not recognised")
    try:
        prior_row("# header only\n")
    except ValueError:
        count += 1
    else:
        failures.append("a .18 manifest with no row passed")

    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "broken.patch"
        original = (ROOT / PROPOSED / f"{SUBJECT.name}.patch").read_text()
        corrupted = original.replace(f'-  "registryVersion": "{BASE_VERSION}"',
                                     '-  "registryVersion": "1.2.0-candidate.9"', 1)
        assert corrupted != original
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            count += 1
        else:
            failures.append("a corrupted patch applied")

    # Manifest.
    rows = ROW.findall(baseline)
    flipped = "0" * 64 if rows[0][0] != "0" * 64 else "1" * 64
    expect("a manifest digest mutation", manifest_findings(
        baseline.replace(rows[0][0], flipped, 1), baseline))
    expect("a manifest path mutation", manifest_findings(
        baseline.replace(SUBJECT.as_posix(), "OTHER.json", 1), baseline))
    expect("an absent manifest", manifest_findings(None, baseline))
    expect("a second patch under proposed/", patch_population_findings(
        patch_files() + [pathlib.Path("SECOND.patch")]))
    expect("a patch that changes nothing", noop_findings(base, base))

    # Composition: an undeclared third package patching the subject.
    with tempfile.TemporaryDirectory() as scratch:
        root = pathlib.Path(scratch)
        for pkg in (PRIOR, CANDIDATE, CANDIDATES / "some-other-package"):
            (root / pkg / "proposed").mkdir(parents=True)
            (root / pkg / "proposed" / f"{SUBJECT.name}.patch").write_text("")
        expect("an undeclared sibling patching the subject",
               composition_findings(root))
        (root / CANDIDATES / "some-other-package" / "proposed" /
         f"{SUBJECT.name}.patch").unlink()
        count += 1
        if composition_findings(root):
            failures.append("the declared pair alone was flagged")

    # Nothing else moves.
    unchanged_mutants = (
        ("a changed top-level field", lambda d: d.__setitem__("status", "adopted")),
        ("a changed entry field", lambda d: d["entries"][0].__setitem__(
            "discoveryVersion", "pwb-discovery-v3")),
        ("a changed bound grammar key", lambda d: g(d)["fixedCatalogKeys"].append("Extra")),
        ("a changed resource limit", lambda d: d["entries"][0]["resourceLimits"].__setitem__(
            "maxSources", 1)),
        ("a grammar key added outside the declared set",
         lambda d: g(d).__setitem__("extra", {})),
    )
    for label, fn in unchanged_mutants:
        expect(label, unchanged_findings(mutate(fn), base))
    reordered = json.loads(proposed)
    grammar = g(reordered)
    moved = {k: grammar[k] for k in reversed(list(grammar))}
    reordered["entries"][0]["observationGrammar"] = moved
    expect("reordered grammar keys",
           unchanged_findings(json.dumps(reordered).encode(), base))

    # Structure.
    expect("invalid JSON", structure_findings(proposed + b"}"))
    structural_mutants = (
        ("an unbumped registryVersion", lambda d: d.__setitem__("registryVersion", BASE_VERSION)),
        ("an unbumped observerVersion",
         lambda d: d["entries"][0].__setitem__("observerVersion", BASE_VERSION)),
        ("a second entry", lambda d: d["entries"].append(dict(d["entries"][0]))),
        ("a grammar that is not an object",
         lambda d: d["entries"][0].__setitem__("observationGrammar", [])),
        ("empty pillars", lambda d: g(d).__setitem__("pillars", [])),
        ("a pillar row with an extra key", lambda d: g(d)["pillars"][0].__setitem__("x", 1)),
        ("a duplicated pillar key", lambda d: g(d)["pillars"][1].__setitem__(
            "key", "heart-and-soul")),
        ("an absent root index path", lambda d: g(d)["rootIndex"].pop("path")),
        ("a population that is not an object", lambda d: g(d).__setitem__("sourcePopulation", [])),
        ("a zero index chain depth",
         lambda d: g(d)["sourcePopulation"].__setitem__("indexChainDepth", 0)),
        ("empty tree populations",
         lambda d: g(d)["sourcePopulation"].__setitem__("treePopulations", [])),
        ("a tree population naming an undeclared rule",
         lambda d: g(d)["sourcePopulation"]["treePopulations"][0].__setitem__("rule", "x")),
        ("a non-boolean root-independence flag",
         lambda d: g(d)["sourcePopulation"]["treePopulations"][0].__setitem__(
             "rootIndependent", "yes")),
        ("a tree pattern without <key>",
         lambda d: g(d)["sourcePopulation"]["treePopulations"][0].__setitem__(
             "pathPattern", "openspec/specs/spec.md")),
        ("a binding naming an undeclared rule",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][0].__setitem__("rule", "x")),
        ("a binding naming an undeclared pillar",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][0].__setitem__("pillar", "x")),
        ("a binding naming an undeclared class",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][0]["classes"].append("x")),
        ("a class no binding reads",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"].pop()),
        ("empty container shapes", lambda d: g(d).__setitem__("containerShapes", {})),
        ("a container shape without a sentence",
         lambda d: g(d)["containerShapes"].__setitem__("tree-path", " ")),
        ("a container shape never used",
         lambda d: g(d)["containerShapes"].__setitem__("unused-shape", "never read")),
        ("empty class grammar", lambda d: g(d).__setitem__("classGrammar", [])),
        ("a grammar row that is not an object", lambda d: g(d)["classGrammar"].append("x")),
        ("a grammar row naming an undeclared class",
         lambda d: g(d)["classGrammar"][6].__setitem__("class", "x")),
        ("a grammar row naming an undeclared shape",
         lambda d: g(d)["classGrammar"][6].__setitem__("container", "prose")),
        ("a grammar row without an item key",
         lambda d: g(d)["classGrammar"][6].pop("itemKey")),
        ("a heading without text",
         lambda d: g(d)["classGrammar"][0]["heading"].__setitem__("text", "")),
        ("a heading level out of range",
         lambda d: g(d)["classGrammar"][0]["heading"].__setitem__("level", 7)),
        ("headingsFrom naming an unknown list",
         lambda d: g(d)["classGrammar"][9].__setitem__("headingsFrom", "x")),
        ("a class no grammar row reads",
         lambda d: g(d).__setitem__("classGrammar", [
             r for r in g(d)["classGrammar"] if r["class"] != "roster-identity"])),
        ("project-account rows out of key order",
         lambda d: g(d)["classGrammar"].insert(0, g(d)["classGrammar"].pop(1))),
        ("renamed semantics key",
         lambda d: g(d).__setitem__("sourceGrammarSemantics", {
             ("scopes" if k == "scope" else k): v
             for k, v in g(d)["sourceGrammarSemantics"].items()})),
        ("an empty semantics sentence",
         lambda d: g(d)["sourceGrammarSemantics"].__setitem__("missingField", "")),
    )
    assert not structure_findings(proposed)
    for label, fn in structural_mutants:
        expect(label, structure_findings(mutate(fn)))

    # Witness 1: the specification's reader definitions.
    expect("a heading literal the specification does not carry",
           spec_findings(mutate(lambda d: g(d)["classGrammar"][0]["heading"].__setitem__(
               "text", "What Syzygy Is")), spec_text))
    expect("a catalog key the specification does not carry",
           spec_findings(mutate(lambda d: g(d)["fixedCatalogKeys"].__setitem__(
               0, "Core Plumbing")), spec_text))
    try:
        reader_definitions("no block here")
    except ValueError:
        count += 1
    else:
        failures.append("a specification with no reader-definitions block passed")

    # Witness 2: the code constants.
    code_mutants = (
        ("a root index path the code does not use",
         lambda d: g(d)["rootIndex"].__setitem__("path", "docs/README.md")),
        ("an index chain depth the code does not use",
         lambda d: g(d)["sourcePopulation"].__setitem__("indexChainDepth", 4)),
        ("a pillar label the code does not use",
         lambda d: g(d)["pillars"][0].__setitem__("label", "Heart & Soul")),
        ("reordered pillars", lambda d: g(d)["pillars"].reverse()),
        ("a binding the code does not make",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][3].__setitem__(
             "relativePath", "design.md")),
        ("a binding with a class the code does not assign",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][3]["classes"].append(
             "principle")),
        ("a pillar-index binding the code does not make",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][0].__setitem__(
             "pillar", "lay-and-land")),
        ("a roster binding the code does not make",
         lambda d: g(d)["sourcePopulation"]["extractionBindings"][7].__setitem__(
             "relativePath", "roster.toml")),
        ("a tree pattern the code does not use",
         lambda d: g(d)["sourcePopulation"]["treePopulations"][0].__setitem__(
             "pathPattern", "specs/<key>/spec.md")),
        ("a heading the code does not carry",
         lambda d: g(d)["classGrammar"][7]["heading"].__setitem__("text", "What Winning Looks Like")),
        ("reordered source rules",
         lambda d: g(d)["sourcePopulation"]["sourceRules"].reverse()),
    )
    for label, fn in code_mutants:
        expect(label, code_findings(mutate(fn)))
    try:
        code_findings(proposed, reader=lambda name: (_ for _ in ()).throw(
            ValueError(f"missing {name}")))
    except ValueError:
        count += 1
    else:
        failures.append("a missing constants file passed")

    if failures:
        print("SELFTEST FAILED: these mutants passed:")
        for label in failures:
            print(f"  {label}")
        return 1
    print(f"selftest: {count} predicates — base-state composition (.18 pending, "
          ".18 adopted, .18 absent, subject drift, patch corruption), manifest "
          "digest, path and absence, patch population, a no-op patch, an "
          "undeclared sibling, nothing-else-moves, every structural claim, and "
          "both restatement witnesses (the specification's reader definitions "
          "and the code constants) all fail closed")
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print("refusing: --apply writes the proposed bytes over an artifact a "
              "performed act still binds; it is the adoption step. Pass --at-adoption.")
        return 2
    findings = check()
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    _base, state = base_bytes()
    if not state.startswith(".18 adopted"):
        print("refusing to apply: the .18 act has not been applied; this package "
              "lands after it")
        return 1
    (ROOT / SUBJECT).write_bytes(proposed_bytes())
    print(f"applied {SUBJECT.as_posix()}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--at-adoption", action="store_true")
    parser.add_argument("--diff", action="store_true",
                        help="print the proposed diff and exit")
    parser.add_argument("--write", action="store_true",
                        help="regenerate the manifest (changes the act argument)")
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
            print("PWB registry loaded-profile amendment does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        _base, state = base_bytes()
        doc = json.loads(proposed_bytes())
        grammar = _entry(doc)["observationGrammar"]
        print(f"PWB registry loaded-profile amendment manifest matches the 1 "
              f"proposed subject ({state}); {len(ADDED_GRAMMAR_KEYS)} grammar keys "
              f"added, {len(grammar['classGrammar'])} class-grammar rows, "
              f"{len(grammar['containerShapes'])} container shapes, "
              f"{len(grammar['sourcePopulation']['extractionBindings'])} extraction "
              f"bindings; the 6 bound grammar keys and every other field unchanged; "
              f"every literal found in the specification and the code constants")
        return 0
    if not args.write:
        print("refusing: regenerating the manifest changes the act argument; pass --write")
        return 2
    target = ROOT / OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(proposed_bytes()))
    print(f"wrote {OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
