#!/usr/bin/env python3
"""Build and verify the inert PWB registry currency-and-briefing amendment.

This script performs no owner act and writes no act record. Its subject is a
single governed artifact: the Polaris Butlers project-shape observer registry
entry. That artifact's current bytes are the argument of a performed
`adopt-registry-entry` act, so they are never edited while this package is a
candidate; a drafted edit in place would read as drift against the act record
and against the CG-7 family in `check_governance.py`.

The proposed bytes therefore live only as one unified diff under `proposed/`.
The manifest row hashes the bytes that diff produces when applied to the
current subject bytes, so the row is the digest a superseding
`adopt-registry-entry` act would take as its argument. It matches the tree
only after `--apply`, which is the adoption step and belongs in the same
change as the owner's new act record and its dedicated recorder.

`--check` verifies that the patch still applies to the bound bytes, that the
result is valid JSON satisfying the structural claims this package makes
about it, and that the manifest is an exact regeneration over that result.

Bare invocation refuses to overwrite the manifest; pass `--write` to
regenerate it.
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
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "pwb-registry-currency-briefing-amendment"
)
PROPOSED = CANDIDATE / "proposed"
OUT = CANDIDATE / "PWB-EFFECT-AMENDMENT-MANIFEST.txt"
TITLE = "PWB REGISTRY CURRENCY-AND-BRIEFING EFFECT AMENDMENT MANIFEST"

#: The version both the registry and the entry carry after the amendment.
PROPOSED_VERSION = "1.2.0-candidate.1"
#: The version they carry today, under the performed amendment act.
CURRENT_VERSION = "1.1.0-candidate.1"
#: The new response ceiling this amendment mints.
BRIEFING_LIMIT_KEY = "maxBriefingResponseBytes"
BRIEFING_LIMIT_SEMANTICS = (
    "the final encoded HTTP body for each authenticated derived read-only "
    "machine view response whose required subject is one exact project-shape "
    "claim identified by its full claim id and whose remaining fields are "
    "same-evaluation joins independently derivable from the machine answer "
    "already served under maxMachineResponseBytes; it is a separate and tighter "
    "ceiling, never a share of that one, and a view without its own declared "
    "ceiling is not served"
)
#: The `claimClassAssignment` sentence must name this claim-id shape: the
#: item-identity twin `factClaim` mints for every admitted item (F1,
#: confirmation round 2). It is the fourth `FACT_FAMILIES` entry in
#: `project-shape-coverage.ts` (`item`), one row earlier in the same closed
#: list as the three families the sentence already named, and it is real,
#: current and populated (`byIdentity` pushes the same reconciled item into
#: both `items` and `facts`) — not future code the assignment may omit.
CLAIM_FACT_ITEM_PHRASE = "claim:fact:item:<class>:<key>"
#: The seven semantics keys the currency-bound block must declare.
CURRENCY_SEMANTICS_KEYS = (
    "measuredFrom",
    "measuredTo",
    "claimClassAssignment",
    "undeclaredClass",
    "outOfBoundResult",
    "outsideTheseBounds",
    "boundChange",
)
#: Every claim class that takes a declared bound in this proposal.
CURRENCY_CLASSES = (
    "project-account-section",
    "principle",
    "success-criterion",
    "catalog-entry",
    "design-contract",
    "baseline-spec",
    "topology-component",
    "craft-policy",
    "roster-identity",
    "project-fact-declaration",
    "project-account-statement",
    "source-coverage",
    "project-shape",
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


def proposed_bytes(
    override: bytes | None = None,
    patches: list[pathlib.Path] | None = None,
) -> bytes:
    """Current subject bytes with every `proposed/*.patch` applied, in a scratch tree."""
    body = current_bytes(override)
    patches = patch_files() if patches is None else patches
    if not patches:
        raise ValueError(f"no proposed patch under {PROPOSED.as_posix()}")
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        (base / SUBJECT).parent.mkdir(parents=True, exist_ok=True)
        (base / SUBJECT).write_bytes(body)
        for patch in patches:
            done = subprocess.run(
                ["git", "apply", "--whitespace=nowarn", str(patch)],
                cwd=base,
                capture_output=True,
                text=True,
            )
            if done.returncode != 0:
                raise ValueError(
                    f"{patch.name} does not apply to the current bytes of "
                    f"{SUBJECT.as_posix()}: {done.stderr.strip()}"
                )
        return (base / SUBJECT).read_bytes()


def structure_findings(body: bytes) -> list[str]:
    """Every structural claim this package makes about the proposed bytes."""
    findings: list[str] = []
    try:
        doc = json.loads(body)
    except ValueError as error:
        return [f"proposed bytes are not valid JSON: {error}"]
    if doc.get("registryVersion") != PROPOSED_VERSION:
        findings.append(
            f"registryVersion is not {PROPOSED_VERSION}: "
            f"{doc.get('registryVersion')!r}"
        )
    entries = doc.get("entries")
    if not isinstance(entries, list) or len(entries) != 1:
        return findings + ["proposed bytes do not carry exactly one registry entry"]
    entry = entries[0]
    if entry.get("observerVersion") != PROPOSED_VERSION:
        findings.append(
            f"observerVersion is not {PROPOSED_VERSION}: "
            f"{entry.get('observerVersion')!r}"
        )
    limits = entry.get("resourceLimits")
    semantics = entry.get("resourceLimitSemantics")
    if not isinstance(limits, dict) or not isinstance(semantics, dict):
        findings.append("resourceLimits or resourceLimitSemantics is not an object")
    else:
        value = limits.get(BRIEFING_LIMIT_KEY)
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            findings.append(
                f"{BRIEFING_LIMIT_KEY} is not a positive integer: {value!r}")
        if semantics.get(BRIEFING_LIMIT_KEY) != BRIEFING_LIMIT_SEMANTICS:
            findings.append(
                f"{BRIEFING_LIMIT_KEY} semantics do not match the exact "
                "single-claim machine-view scope")
        for key in limits:
            if key not in semantics:
                findings.append(f"resource limit without a semantics sentence: {key}")
    bounds = entry.get("currencyBounds")
    if not isinstance(bounds, list) or not bounds:
        findings.append("currencyBounds is missing or empty")
    else:
        classes = [row.get("claimClass") if isinstance(row, dict) else None
                   for row in bounds]
        if len(set(classes)) != len(classes):
            findings.append("currencyBounds declares a claim class twice")
        if tuple(classes) != CURRENCY_CLASSES:
            findings.append(
                "currencyBounds class population or order differs from the "
                "declared set")
        for row in bounds:
            if not isinstance(row, dict) or set(row) != {"claimClass", "maxAgeMs"}:
                findings.append(f"currencyBounds row has unexpected keys: {row!r}")
                continue
            age = row.get("maxAgeMs")
            if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
                findings.append(
                    f"maxAgeMs is not a positive integer for "
                    f"{row.get('claimClass')!r}: {age!r}")
    bound_semantics = entry.get("currencyBoundSemantics")
    if not isinstance(bound_semantics, dict):
        findings.append("currencyBoundSemantics is missing or not an object")
    else:
        if tuple(bound_semantics) != CURRENCY_SEMANTICS_KEYS:
            findings.append(
                "currencyBoundSemantics key population or order differs from the "
                "declared set")
        for key, sentence in bound_semantics.items():
            if not isinstance(sentence, str) or not sentence.strip():
                findings.append(f"currencyBoundSemantics sentence is empty: {key}")
        assignment = bound_semantics.get("claimClassAssignment")
        if isinstance(assignment, str) and CLAIM_FACT_ITEM_PHRASE not in assignment:
            findings.append(
                "claimClassAssignment does not name the "
                f"{CLAIM_FACT_ITEM_PHRASE} item-identity twin family")
    return findings


def render(body: bytes) -> str:
    lines = [
        f"# {TITLE}",
        "# This row binds only by the owner act that takes its digest as the",
        "# argument of a superseding adopt-registry-entry act; until that act is",
        "# performed it binds nothing.",
        "# 1 artifact; the row hashes the PROPOSED bytes: the current bytes of the",
        "# subject with proposed/*.patch applied. It matches the tree only after",
        "# --apply, the adoption step.",
        "# The subject's current bytes stay the argument of the act in force.",
        f"{sha256(body)}  {SUBJECT.as_posix()}",
    ]
    return "\n".join(lines) + "\n"


def verify_manifest(text: str, expected: str) -> list[str]:
    rows = ROW.findall(text)
    if [path for _digest, path in rows] != [SUBJECT.as_posix()]:
        return ["manifest row population or path differs"]
    if text != expected:
        return ["manifest differs from exact regeneration over the proposed bytes"]
    return []


def patch_population_findings(patches: list[pathlib.Path]) -> list[str]:
    """The one declared subject patch, and nothing else, lives under proposed/."""
    if [p.name for p in patches] != [f"{SUBJECT.name}.patch"]:
        return [
            "proposed/*.patch population is not the single declared subject patch: "
            + ", ".join(p.name for p in patches)
        ]
    return []


def noop_findings(proposed: bytes, current: bytes) -> list[str]:
    """A patch that changes nothing would make the act argument the current bytes."""
    if proposed == current:
        return [f"the proposed patch changes nothing: {SUBJECT.as_posix()}"]
    return []


def manifest_findings(text: str | None, expected: str) -> list[str]:
    """`text` is None when the manifest file is absent — never a silent pass."""
    if text is None:
        return [f"manifest missing: {OUT.as_posix()}"]
    return verify_manifest(text, expected)


def check() -> list[str]:
    findings: list[str] = []
    findings.extend(patch_population_findings(patch_files()))
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(noop_findings(proposed, current_bytes()))
    findings.extend(structure_findings(proposed))
    target = ROOT / OUT
    findings.extend(manifest_findings(
        target.read_text() if target.is_file() else None, render(proposed)))
    return findings


def selftest() -> int:
    findings = check()
    if findings:
        print("SELFTEST FAILED: the package does not verify on current bytes")
        for finding in findings:
            print(f"  {finding}")
        return 1
    current = current_bytes()
    if CURRENT_VERSION.encode() not in current:
        print("SELFTEST FAILED: the subject no longer carries the current version")
        return 1
    baseline = render(proposed_bytes())

    # Predicate 1: subject drift retires the patch.
    drifted = current.replace(
        b'"maxMachineResponseBytes": 8388608',
        b'"maxMachineResponseBytes": 8388609', 1)
    assert drifted != current
    try:
        proposed_bytes(drifted)
    except ValueError:
        pass
    else:
        print("SELFTEST FAILED: the patch applied over drifted subject bytes")
        return 1

    # Predicate 2: a corrupted patch does not apply.
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "broken.patch"
        original = (ROOT / PROPOSED / f"{SUBJECT.name}.patch").read_text()
        corrupted = original.replace(
            f'"registryVersion": "{CURRENT_VERSION}"',
            '"registryVersion": "1.1.0-candidate.9"', 1)
        assert corrupted != original
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            print("SELFTEST FAILED: a corrupted patch applied")
            return 1

    # Predicate 3: a manifest digest mutation is caught.
    rows = ROW.findall(baseline)
    flipped = "0" * 64 if rows[0][0] != "0" * 64 else "1" * 64
    if not verify_manifest(baseline.replace(rows[0][0], flipped, 1), baseline):
        print("SELFTEST FAILED: a manifest digest mutation passed")
        return 1

    # Predicate 4: a manifest path mutation is caught.
    if not verify_manifest(
            baseline.replace(SUBJECT.as_posix(), "OTHER.json", 1), baseline):
        print("SELFTEST FAILED: a manifest path mutation passed")
        return 1

    proposed = proposed_bytes()
    if structure_findings(proposed):
        print("SELFTEST FAILED: the proposed bytes do not satisfy their own claims")
        return 1

    # Predicate 5: an unbumped version fails the structural claim.
    unbumped = proposed.replace(
        f'"observerVersion": "{PROPOSED_VERSION}"'.encode(),
        f'"observerVersion": "{CURRENT_VERSION}"'.encode(), 1)
    assert unbumped != proposed
    if not structure_findings(unbumped):
        print("SELFTEST FAILED: an unbumped observerVersion passed")
        return 1

    # Predicate 6: a limit without its semantics sentence fails.
    unexplained = proposed.replace(
        f'"{BRIEFING_LIMIT_KEY}": "the final encoded'.encode(),
        f'"{BRIEFING_LIMIT_KEY}Note": "the final encoded'.encode(), 1)
    assert unexplained != proposed
    if not structure_findings(unexplained):
        print("SELFTEST FAILED: a resource limit without a semantics sentence passed")
        return 1

    # Predicate 7: a renamed claim class fails.
    renamed = proposed.replace(
        b'"claimClass": "project-shape"', b'"claimClass": "project-shapes"', 1)
    assert renamed != proposed
    if not structure_findings(renamed):
        print("SELFTEST FAILED: a renamed claim class passed")
        return 1

    # Predicate 8: a non-positive bound fails.
    zeroed = proposed.replace(b'"maxAgeMs": 2592000000', b'"maxAgeMs": 0', 1)
    assert zeroed != proposed
    if not structure_findings(zeroed):
        print("SELFTEST FAILED: a zero maxAgeMs passed")
        return 1

    # Predicate 9: a renamed semantics key fails.
    stripped = proposed.replace(b'"boundChange"', b'"boundChanged"', 1)
    assert stripped != proposed
    if not structure_findings(stripped):
        print("SELFTEST FAILED: a renamed semantics key passed")
        return 1

    # Predicate 10: invalid JSON fails.
    if not structure_findings(proposed + b"}"):
        print("SELFTEST FAILED: invalid JSON passed")
        return 1

    # Predicate 11: the top-level registryVersion is checked by its own `if`,
    # separately from observerVersion. Bump one and not the other — the exact
    # shape a hand-edit produces, because convention edits them together.
    half_bumped = proposed.replace(
        f'"registryVersion": "{PROPOSED_VERSION}"'.encode(),
        f'"registryVersion": "{CURRENT_VERSION}"'.encode(), 1)
    assert half_bumped != proposed
    if not structure_findings(half_bumped):
        print("SELFTEST FAILED: an unbumped top-level registryVersion passed")
        return 1

    # Predicate 12: a duplicated claim class — a copy-pasted currencyBounds
    # row — fails, and not only through the population comparison.
    duplicated = proposed.replace(
        b'"claimClass": "principle"',
        b'"claimClass": "project-account-section"', 1)
    assert duplicated != proposed
    if "currencyBounds declares a claim class twice" not in structure_findings(
            duplicated):
        print("SELFTEST FAILED: a duplicated claim class passed")
        return 1

    # Predicate 13: a non-positive briefing ceiling fails. A ceiling of zero
    # serves nothing and is indistinguishable from an absent declaration.
    no_ceiling = proposed.replace(
        f'"{BRIEFING_LIMIT_KEY}": 20480'.encode(),
        f'"{BRIEFING_LIMIT_KEY}": 0'.encode(), 1)
    assert no_ceiling != proposed
    if not structure_findings(no_ceiling):
        print("SELFTEST FAILED: a zero briefing ceiling passed")
        return 1

    # Predicate 14: the ceiling semantics are an exact cross-package boundary,
    # not merely a non-empty sentence. Widening one claim to an unspecified
    # subject would reopen the syzygy-dov.22 dependency this package records.
    widened_scope = proposed.replace(
        b"one exact project-shape claim identified by its full claim id",
        b"one named subject", 1)
    assert widened_scope != proposed
    if not structure_findings(widened_scope):
        print("SELFTEST FAILED: widened briefing subject semantics passed")
        return 1

    # Predicates 15-21 mutate the parsed document and re-serialize, so each
    # one reaches the structural assertion under test rather than failing
    # earlier on JSON validity. Each names the assertion it covers.
    def mutate(fn) -> bytes:
        doc = json.loads(proposed)
        fn(doc)
        return json.dumps(doc, indent=2).encode()

    structural_mutants = (
        ("a second registry entry",
         lambda doc: doc["entries"].append(dict(doc["entries"][0]))),
        ("resourceLimits that is not an object",
         lambda doc: doc["entries"][0].__setitem__("resourceLimits", [])),
        ("absent currencyBounds",
         lambda doc: doc["entries"][0].pop("currencyBounds")),
        ("a currencyBounds row carrying an extra key",
         lambda doc: doc["entries"][0]["currencyBounds"][0].__setitem__(
             "note", "why")),
        ("currencyBoundSemantics that is not an object",
         lambda doc: doc["entries"][0].__setitem__(
             "currencyBoundSemantics", "see the contract")),
        ("an empty currencyBoundSemantics sentence",
         lambda doc: doc["entries"][0]["currencyBoundSemantics"].__setitem__(
             CURRENCY_SEMANTICS_KEYS[0], "   ")),
        # Predicate 21: claimClassAssignment must keep naming the
        # claim:fact:item: item-identity twin family (F1, confirmation
        # round 2) — dropping just that phrase, and nothing else in the
        # sentence, must still be caught.
        ("claimClassAssignment missing its claim:fact:item: family clause",
         lambda doc: doc["entries"][0]["currencyBoundSemantics"].__setitem__(
             "claimClassAssignment",
             doc["entries"][0]["currencyBoundSemantics"][
                 "claimClassAssignment"].replace(
                     CLAIM_FACT_ITEM_PHRASE, "the item-identity twin family"))),
    )
    for label, fn in structural_mutants:
        mutant = mutate(fn)
        assert mutant != proposed
        if not structure_findings(mutant):
            print(f"SELFTEST FAILED: {label} passed")
            return 1

    # Predicates 22-24 cover the three assertions `check()` makes that
    # `structure_findings` does not. Each is exercised through the helper
    # `check()` itself calls, so a fixture cannot drift from the caller.
    good_patches = patch_files()
    assert not patch_population_findings(good_patches)
    if not patch_population_findings(
            good_patches + [pathlib.Path("SECOND.patch")]):
        print("SELFTEST FAILED: a second patch under proposed/ passed")
        return 1

    assert not noop_findings(proposed, current)
    if not noop_findings(proposed, proposed):
        print("SELFTEST FAILED: a patch that changes nothing passed")
        return 1

    assert not manifest_findings(baseline, baseline)
    if not manifest_findings(None, baseline):
        print("SELFTEST FAILED: an absent manifest passed")
        return 1

    print("selftest: 24 predicates — subject drift, patch corruption, patch "
          "population, a no-op patch, manifest digest, path mutation and "
          "absence, both version bumps, limit semantics, the briefing "
          "ceiling's value and exact single-claim scope, claim-class population, "
          "duplication, row shape and bound value, the semantics block's type, "
          "keys and empty sentences, entry count, the claim:fact:item: family "
          "name and JSON validity all fail closed")
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print("refusing: --apply writes the proposed bytes over an artifact a "
              "performed act still binds; it is the adoption step and belongs in "
              "the change that records the superseding act. Pass --at-adoption.")
        return 2
    findings = check()
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
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
                        help="regenerate the manifest (retires any packet quoting it)")
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
            print("PWB registry currency-and-briefing amendment does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(f"PWB registry currency-and-briefing amendment manifest matches the "
              f"1 proposed subject ({len(CURRENCY_CLASSES)} currency bounds, "
              f"1 new response ceiling); the patch applies to the bound bytes")
        return 0
    if not args.write:
        print("refusing: regenerating the manifest changes the act argument; pass "
              "--write, then update every registered copy of the digest")
        return 2
    target = ROOT / OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(proposed_bytes()))
    print(f"wrote {OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
