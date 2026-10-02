#!/usr/bin/env python3
"""Regenerate and check the two Polaris generated dependency unions.

Bead `syzygy-c51h`. Each Polaris change carries a generated
`GOVERNING-DEPENDENCIES.md`: the union, per warrant class, of every
` ```yaml warrants: ``` ` block in its own `spec.md`.

- base (`polaris-manifesto-generation`): a fixed header and one JSON object
  over the six warrant classes, each list sorted, with `primary` folded out;
- understanding amendment (`polaris-manifesto-understanding-amendment`): a
  fixed header and one `## <class>` section per class, `primary` first,
  values sorted and comma-joined, or `None declared in the requirement
  warrants.` when empty, and one trailing blank line.

Both files are signed subjects, so this script never writes them. `--check`
requires each file on disk to equal its regeneration. One exception is
allowed, for the case where a signed successor package proposes the
regeneration and has not yet been performed. Then the file must still be the
package's predecessor bytes, and the package's proposed bytes must equal the
regeneration. A performed package makes the strict comparison apply again.

`--render base|understanding` prints a regeneration. `--selftest` mutates
each predicate in a scratch tree and requires the check to fail. It also
confirms that the renderer reproduces the base union byte for byte, and
reproduces the signed understanding union once the one warrant this
regeneration adds is removed. The successor act was performed on
2026-10-02, so the scratch copy first replays the pre-act state: the
installed union is reversed to the predecessor and must hash to the digest
the package records.

The parser here is a line state machine. It is independent of the
regular-expression parser in `check_spec_reconciliation.py` R7, which
cross-checks the same unions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGES = pathlib.Path("openspec/changes")
DECISIONS = pathlib.Path(".syzygy/governance/decisions")
CLASSES = ("primary", "doctrine", "contracts", "policies", "decisions",
           "topology", "parent_requirements")
SUCCESSOR_PACKAGE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "polaris-understanding-dependency-union-successor")

BASE_HEAD = (
    "# Generator dependency declaration\n\n"
    "Generated from the current requirements' six-class warrants blocks.\n"
    "This is a union, not confirmation that the declarations or applicability sweep\n"
    "are complete. It binds nothing and has no independent authority.\n\n")
UNDERSTANDING_HEAD = (
    "# Governing dependency union\n\n"
    "Generated from this amendment's explicit requirement warrants; review routing,\n"
    "not authority, new permission or proof of semantic coverage.\n")
NONE_DECLARED = "None declared in the requirement warrants."


def union_spec(change: str) -> pathlib.Path:
    return CHANGES / change / "specs" / "polaris-generation" / "spec.md"


def union_file(change: str) -> pathlib.Path:
    return CHANGES / change / "GOVERNING-DEPENDENCIES.md"


UNIONS = {
    "base": "polaris-manifesto-generation",
    "understanding": "polaris-manifesto-understanding-amendment",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def warrants(spec: str) -> dict[str, set[str]]:
    """Union of every class over every warrants block, by line state machine."""
    union: dict[str, set[str]] = {cls: set() for cls in CLASSES}
    state, current = "prose", None
    blocks = 0
    for line in spec.split("\n"):
        if state == "prose":
            state = "fence" if line == "```yaml" else "prose"
            continue
        if state == "fence":
            state = "block" if line == "warrants:" else "prose"
            blocks += 1 if state == "block" else 0
            continue
        if line == "```":
            state, current = "prose", None
            continue
        stripped = line.strip()
        if line.startswith("  ") and not line.startswith("   ") and ":" in stripped:
            key, _sep, value = stripped.partition(":")
            if key not in union:
                raise ValueError(f"unknown warrant class {key!r}")
            current, value = key, value.strip()
            if value.startswith("[") and value.endswith("]"):
                union[key] |= {v.strip() for v in value[1:-1].split(",") if v.strip()}
            elif value:
                union[key].add(value)
        elif stripped.startswith("- ") and current:
            union[current].add(stripped[2:].strip())
        elif stripped:
            raise ValueError(f"unparsed warrant line {line!r}")
    if state != "prose":
        raise ValueError("unterminated warrants block")
    if blocks == 0:
        raise ValueError("spec carries no warrants block")
    return union


def render_base(union: dict[str, set[str]]) -> str:
    body = {cls: sorted(union[cls]) for cls in CLASSES if cls != "primary"}
    return BASE_HEAD + "```json\n" + json.dumps(body, indent=2) + "\n```\n"


def render_understanding(union: dict[str, set[str]]) -> str:
    out = [UNDERSTANDING_HEAD]
    for cls in CLASSES:
        values = sorted(union[cls])
        out.append(f"\n## {cls}\n\n{', '.join(values) if values else NONE_DECLARED}\n")
    return "".join(out) + "\n"


RENDER = {"base": render_base, "understanding": render_understanding}


def regenerate(root: pathlib.Path, key: str) -> str:
    spec = (root / union_spec(UNIONS[key])).read_text(encoding="utf-8")
    return RENDER[key](warrants(spec))


def successor_state(root: pathlib.Path):
    """(performed, predecessor digest, proposed bytes) of the successor package, or None."""
    config_path = root / SUCCESSOR_PACKAGE / "SUCCESSOR.json"
    if not config_path.is_file():
        return None
    config = json.loads(config_path.read_text(encoding="utf-8"))
    rel = union_file(UNIONS["understanding"]).as_posix()
    proposed = root / SUCCESSOR_PACKAGE / "proposed" / (rel + ".proposed")
    return ((root / config["act"]).is_file(), config["predecessor"].get(rel),
            proposed.read_bytes() if proposed.is_file() else None)


def check(root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    for key, change in UNIONS.items():
        target = root / union_file(change)
        try:
            expected = regenerate(root, key).encode("utf-8")
        except (OSError, ValueError) as error:
            findings.append(f"{key}: cannot regenerate: {error}")
            continue
        if not target.is_file():
            findings.append(f"{key}: missing {union_file(change).as_posix()}")
            continue
        actual = target.read_bytes()
        if actual == expected:
            continue
        state = successor_state(root) if key == "understanding" else None
        if state is None or state[0]:
            findings.append(f"{key}: {union_file(change).as_posix()} differs from "
                            "its regeneration")
            continue
        _performed, predecessor, proposed = state
        if sha256(actual) != predecessor:
            findings.append(f"{key}: the file is neither its regeneration nor the "
                            "successor package's predecessor")
        if proposed != expected:
            findings.append(f"{key}: the unperformed successor package does not "
                            "propose the regeneration")
    return findings


# --- selftest ----------------------------------------------------------------

def _inputs(root: pathlib.Path) -> list[pathlib.Path]:
    paths = []
    for change in UNIONS.values():
        paths += [union_spec(change), union_file(change)]
    package = root / SUCCESSOR_PACKAGE
    if package.is_dir():
        paths += [p.relative_to(root) for p in package.rglob("*") if p.is_file()]
    return paths


def _copy(src: pathlib.Path, dest: pathlib.Path) -> None:
    for rel in _inputs(src):
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src / rel, dest / rel)


def _edit(rel: pathlib.Path, old: str, new: str):
    def mutate(root: pathlib.Path) -> None:
        text = (root / rel).read_text(encoding="utf-8")
        if old not in text:
            raise AssertionError(f"mutation target absent in {rel}: {old[:60]!r}")
        (root / rel).write_text(text.replace(old, new, 1), encoding="utf-8")
    return mutate


def selftest() -> int:
    results: list[tuple[str, bool]] = []
    base_spec, und_spec = (union_spec(UNIONS[k]) for k in ("base", "understanding"))
    base_file, und_file = (union_file(UNIONS[k]) for k in ("base", "understanding"))
    proposed = SUCCESSOR_PACKAGE / "proposed" / (und_file.as_posix() + ".proposed")
    with tempfile.TemporaryDirectory() as tmp:
        clean = pathlib.Path(tmp) / "clean"
        _copy(ROOT, clean)
        # The scratch copy replays the pre-act state: the act record is never
        # copied, and once the act is performed (2026-10-02) the installed
        # union is reversed to its signed predecessor, whose digest the
        # package records.
        _performed, predecessor, _proposed = successor_state(clean)
        if sha256((clean / und_file).read_bytes()) != predecessor:
            reversed_ = (clean / und_file).read_text(encoding="utf-8").replace(
                "\n\nCC-REV-8, CC-SPEC-2, CC-SPEC-4\n", "\n\nCC-SPEC-2, CC-SPEC-4\n", 1)
            results.append(("the installed union reverses to its signed predecessor",
                            sha256(reversed_.encode("utf-8")) == predecessor))
            (clean / und_file).write_text(reversed_, encoding="utf-8")
        results.append(("the unmutated scratch copy verifies", check(clean) == []))

        # Renderer fidelity against signed bytes.
        results.append(("base renderer reproduces the signed base union byte for byte",
                        regenerate(clean, "base").encode() == (clean / base_file).read_bytes()))
        und = (clean / und_spec).read_text(encoding="utf-8")
        assert und.count("CC-SPEC-4, CC-REV-8]") == 1
        without = render_understanding(warrants(und.replace("CC-SPEC-4, CC-REV-8]",
                                                            "CC-SPEC-4]")))
        results.append(("understanding renderer reproduces the signed union once "
                        "CC-REV-8 is removed", without.encode() == (clean / und_file).read_bytes()))

        def broken(_root):
            raise AssertionError

        mutants = (
            ("a base warrant added", _edit(base_spec, "  decisions: []",
                                           "  decisions: [SDR-99]"), "base: "),
            ("the base union edited", _edit(base_file, '"VIS-1",', '"VIS-9",'), "base: "),
            ("an understanding warrant added", _edit(und_spec, "  decisions: [SDR-3]",
                                                     "  decisions: [SDR-3, SDR-99]"),
             "does not propose the regeneration"),
            ("the understanding union edited", _edit(und_file, "SDR-3", "SDR-4"),
             "neither its regeneration nor"),
            ("the proposed union edited", _edit(proposed, "CC-REV-8", "CC-REV-9"),
             "does not propose the regeneration"),
            ("the proposed union removed", lambda r: (r / proposed).unlink(),
             "does not propose the regeneration"),
            ("an unknown warrant class", _edit(und_spec, "  topology: []",
                                               "  topologies: []"), "unknown warrant class"),
            ("an unterminated warrants block", _edit(
                base_spec, "  parent_requirements: []\n```",
                "  parent_requirements: []\n"), "cannot regenerate"),
            ("the successor performed with the old union still installed",
             lambda r: (r / DECISIONS).mkdir(parents=True, exist_ok=True) or (
                 r / json.loads((r / SUCCESSOR_PACKAGE / "SUCCESSOR.json").read_text())[
                     "act"]).write_text("record\n"),
             "differs from its regeneration"),
        )
        for name, mutate, expect in mutants:
            tree = pathlib.Path(tmp) / name.replace(" ", "-")
            shutil.copytree(clean, tree)
            mutate(tree)
            got = check(tree)
            ok = any(expect in f for f in got)
            results.append((f"fails: {name}", ok))
            if not ok:
                print(f"  ({name}: got {got or 'nothing'})")

        # Performed: the proposed bytes installed and the record present pass.
        tree = pathlib.Path(tmp) / "performed"
        shutil.copytree(clean, tree)
        shutil.copyfile(tree / proposed, tree / und_file)
        act = json.loads((tree / SUCCESSOR_PACKAGE / "SUCCESSOR.json").read_text())["act"]
        (tree / act).parent.mkdir(parents=True, exist_ok=True)
        (tree / act).write_text("record\n")
        results.append(("performed: installed regeneration verifies", check(tree) == []))
        _edit(und_spec, "  decisions: [SDR-3]", "  decisions: [SDR-3, SDR-99]")(tree)
        results.append(("performed: a later warrant change fails strictly",
                        any("differs from its regeneration" in f for f in check(tree))))
        # With no successor package at all, the stale union fails strictly.
        tree = pathlib.Path(tmp) / "no-package"
        shutil.copytree(clean, tree)
        shutil.rmtree(tree / SUCCESSOR_PACKAGE)
        results.append(("without a successor package the stale union fails",
                        any("differs from its regeneration" in f for f in check(tree))))
    failing = sum(0 if ok else 1 for _n, ok in results)
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"{len(results)} fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--render", choices=sorted(UNIONS))
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.render:
        sys.stdout.write(regenerate(ROOT, args.render))
        return 0
    findings = check()
    if findings:
        print("Polaris dependency unions do not verify:")
        for finding in findings:
            print(f"  {finding}")
        return 1
    state = successor_state(ROOT)
    note = ("" if state is None or state[0] else
            "; understanding: signed predecessor installed, the unperformed successor "
            "package proposes the regeneration")
    print(f"2 Polaris dependency unions match their warrants{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
