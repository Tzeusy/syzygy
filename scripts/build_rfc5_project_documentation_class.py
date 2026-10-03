#!/usr/bin/env python3
"""Build and verify the inert RFC5-14 `project-documentation` class package.

This script performs no owner act and writes no act record. The package
amends one accepted contract module, `rfcs/RFC-0005/consent-egress-secrets.md`
(clause RFC5-14), adding a seventh content class (packet question Q7 of
`public-repo-admission`, option a). It has no recorder and no `--apply`: the
act form is the owner's choice (see the packet), and no chain link is
asserted, because a link asserts adoption order, which only the performing
act decides.

Layout, under `.syzygy/governance/contracts/candidates/rfc5-project-documentation-class/`:

- `proposed/RFC-0005/consent-egress-secrets.md.patch` — one unified diff
  naming the module relative to `.syzygy/governance/contracts/`.
- `CONTRACT-AMENDMENT-MANIFEST.txt` — one row: the sha256 of the module bytes
  the patch produces.

The proposed bytes are NOT applied while the package is a candidate: CG-7h
binds both mirrors to the bootstrap manifest, so an edit in place would read
as drift.

`--check` verifies, and prints `absent` and exits 0 when the package
directory does not exist:

1. the patch population is exactly the one expected module;
2. both mirrors are byte-identical and the patch applies cleanly to each,
   touches only that module and changes it;
3. the manifest equals an exact regeneration over the patched bytes;
4. structure is preserved: clause leads, YAML front matter and Markdown
   headings, as in the sibling RFC-0007 successor builder;
5. the RFC5-14 table gains exactly one row, `project-documentation`, between
   `code-content` and `work-history`, the six existing rows are byte-identical
   and in order, and the composite-inheritance bullet is byte-identical;
6. on a scratch tree holding the patched `candidates/rfcs/`,
   `verify_final_prespec.py`, CG-13 and CG-17 report no failure.

Bare invocation refuses to overwrite the manifest; pass `--write`.
"""

from __future__ import annotations

import argparse
import io
import pathlib
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_contract_readability_restyle as shared  # noqa: E402

CONTRACTS = shared.CONTRACTS
CANDIDATES = shared.CANDIDATES
PACKAGE = CANDIDATES / "rfc5-project-documentation-class"
PROPOSED = PACKAGE / "proposed"
MANIFEST = PACKAGE / "CONTRACT-AMENDMENT-MANIFEST.txt"
MODULE = "rfcs/RFC-0005/consent-egress-secrets.md"
TITLE = "RFC-0005 PROJECT-DOCUMENTATION CONTENT-CLASS AMENDMENT MANIFEST"
NEW_CLASS = "project-documentation"
OLD_CLASSES = ("governance-text", "code-structure", "code-content",
               "work-history", "evidence-content", "derived-composites")
COMPOSITE_BULLET = (
    "- A composite inherits the **highest** class of any content it embeds;\n"
    "  `derived-composites` consent alone never launders an unconsented class into\n"
    "  an egress.\n")
sha256 = shared.sha256


def patch_path() -> pathlib.Path:
    rel = pathlib.PurePosixPath(MODULE).relative_to("rfcs").as_posix()
    return PROPOSED / f"{rel}.patch"


def patch_files(root: pathlib.Path) -> list[pathlib.Path]:
    base = root / PROPOSED
    if not base.is_dir():
        return []
    return sorted((p.relative_to(root) for p in base.rglob("*.patch")),
                  key=lambda p: p.as_posix())


def proposed_bytes(root: pathlib.Path) -> tuple[dict[str, bytes], list[str]]:
    findings: list[str] = []
    installed_file = root / CONTRACTS / MODULE
    mirror_file = root / CANDIDATES / MODULE
    if not installed_file.is_file() or not mirror_file.is_file():
        return {}, [f"mirror pair for `{MODULE}` is incomplete"]
    installed, mirror = installed_file.read_bytes(), mirror_file.read_bytes()
    if installed != mirror:
        findings.append(f"installed and candidate mirrors of `{MODULE}` differ")
    patch = root / patch_path()
    if not patch.is_file():
        return {}, findings
    results = []
    for label, body in (("installed", installed), ("candidate", mirror)):
        try:
            results.append(shared.apply_patch(MODULE, body, patch))
        except ValueError as error:
            findings.append(f"{label} mirror: {error}")
    if len(results) != 2:
        return {}, findings
    if results[0] != results[1]:
        findings.append(f"`{MODULE}` patches to different bytes on the two mirrors")
    elif results[0] == installed:
        findings.append(f"patch for `{MODULE}` changes nothing")
    else:
        return {MODULE: results[0]}, findings
    return {}, findings


def render(proposed: dict[str, bytes]) -> str:
    return "\n".join([
        f"# {TITLE}",
        "# One accepted RFC 0001-0009 module (RFC5-14); the row is sorted by path.",
        "# Paths are relative to .syzygy/governance/contracts/.",
        "# These rows bind only by the owner act that names this file's digest in",
        "# ACCEPTANCE-ACT-RECORD.md; until that act is performed they bind nothing.",
        "# Rows hash the PROPOSED bytes: both identical mirrors with",
        "# proposed/<path under rfcs/>.patch applied. They match the tree only",
        "# after adoption. Installed and candidate-mirror bytes are required to",
        "# match exactly.",
        f"{sha256(proposed[MODULE])}  {MODULE}",
    ]) + "\n"


def applied(root: pathlib.Path) -> bool:
    target = root / MANIFEST
    if not target.is_file():
        return False
    rows = shared.manifest_rows(target.read_text(encoding="utf-8"))
    if [p for _s, p in rows] != [MODULE]:
        return False
    return all((root / base / MODULE).is_file()
               and sha256((root / base / MODULE).read_bytes()) == rows[0][0]
               for base in (CONTRACTS, CANDIDATES))


def _table_rows(text: str) -> list[str]:
    start = text.index("**RFC5-14.**")
    body = text[start:]
    end = body.index("\n\n- A composite")
    return [l for l in body[:end].splitlines() if l.startswith("| `")]


def class_findings(old: bytes, new: bytes) -> list[str]:
    o, n = old.decode("utf-8"), new.decode("utf-8")
    findings: list[str] = []
    old_rows, new_rows = _table_rows(o), _table_rows(n)
    want = [r for r in new_rows if not r.startswith(f"| `{NEW_CLASS}`")]
    if want != old_rows:
        findings.append(f"`{MODULE}`: the six existing RFC5-14 rows are not "
                        "byte-identical and in order")
    names = [r.split("`")[1] for r in new_rows]
    expected = list(OLD_CLASSES)
    expected.insert(expected.index("work-history"), NEW_CLASS)
    if names != expected:
        findings.append(f"`{MODULE}`: the RFC5-14 table is not the six classes "
                        f"plus `{NEW_CLASS}` between `code-content` and `work-history`")
    if COMPOSITE_BULLET not in n or n.count(COMPOSITE_BULLET) != 1:
        findings.append(f"`{MODULE}`: the composite-inheritance bullet changed")
    if "no ordering among classes" not in n:
        findings.append(f"`{MODULE}`: the amendment does not state that it adds no "
                        "ordering among classes")
    return findings


def check(root: pathlib.Path = ROOT, scratch: bool = True) -> list[str]:
    findings: list[str] = []
    paths = shared.bootstrap_paths(root)
    if MODULE not in paths:
        return [f"{MODULE} is not in the bootstrap population"]
    expected, actual = [patch_path()], patch_files(root)
    if sorted(set(expected) - set(actual)):
        findings.append("missing patch(es): " + ", ".join(
            p.as_posix() for p in sorted(set(expected) - set(actual))))
    if sorted(set(actual) - set(expected)):
        findings.append("patch(es) outside the one-module population: " + ", ".join(
            p.as_posix() for p in sorted(set(actual) - set(expected))))
    proposed, applying = proposed_bytes(root)
    findings.extend(applying)
    if MODULE in proposed:
        old = (root / CONTRACTS / MODULE).read_bytes()
        findings.extend(shared.structure_findings(
            MODULE, old, proposed[MODULE], shared._verifier().CLAUSE_DEF))
        findings.extend(class_findings(old, proposed[MODULE]))
    if findings:
        return findings
    target = root / MANIFEST
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST.as_posix()}")
    else:
        findings.extend(shared.verify_manifest(
            target.read_text(encoding="utf-8"), render(proposed), [MODULE]))
    if scratch:
        findings.extend(shared.scratch_findings(root, proposed))
    return findings


def write(root: pathlib.Path) -> int:
    proposed, findings = proposed_bytes(root)
    if findings or MODULE not in proposed:
        print("refusing to write: the patch does not produce the module")
        for finding in findings:
            print(f"  {finding}")
        return 1
    (root / MANIFEST).write_text(render(proposed), encoding="utf-8")
    print(f"wrote {MANIFEST.as_posix()}")
    return 0


def _quiet_write(root: pathlib.Path) -> None:
    sink, saved = io.StringIO(), sys.stdout
    sys.stdout = sink
    try:
        write(root)
    finally:
        sys.stdout = saved


def _fixture_root(scratch: pathlib.Path) -> pathlib.Path:
    root = scratch / "repo"
    for rel in (CONTRACTS / "rfcs", CANDIDATES / "rfcs", CANDIDATES / "fixtures"):
        shutil.copytree(ROOT / rel, root / rel)
    for rel in (shared.BOOTSTRAP_MANIFEST,
                *(CANDIDATES / e for e in shared.SCRATCH_EXTRAS)):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(ROOT / rel, root / rel)
    shutil.copy(ROOT / patch_path(), _mk(root / patch_path()))
    return root


def _mk(path: pathlib.Path) -> pathlib.Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def selftest() -> int:
    passed: list[str] = []
    failures: list[str] = []

    def expect(label, findings, want):
        ok = any(want in f for f in findings) if want else not findings
        (passed if ok else failures).append(label if ok else f"{label}: got {findings[:3]}")

    with tempfile.TemporaryDirectory() as directory:
        root = _fixture_root(pathlib.Path(directory))
        expect("unwritten manifest reported", check(root, scratch=False), "manifest missing")
        _quiet_write(root)
        expect("valid package verifies, scratch structure included", check(root), None)
        good = (root / MANIFEST).read_text(encoding="utf-8")
        old = (root / CONTRACTS / MODULE).read_bytes()
        full = proposed_bytes(root)[0][MODULE].decode("utf-8")

        def with_patch(transform, label, want, scratch_run=False):
            target = root / patch_path()
            saved = target.read_text(encoding="utf-8")
            new = transform(full)
            target.write_text(shared.make_patch(MODULE, old, new.encode("utf-8")))
            try:
                expect(label, check(root, scratch=scratch_run), want)
            finally:
                target.write_text(saved)

        def mutate_file(rel, fn, label, want):
            t = root / rel
            saved = t.read_bytes() if t.exists() else None
            fn(t)
            try:
                expect(label, check(root, scratch=False), want)
            finally:
                if saved is None:
                    t.unlink()
                else:
                    t.write_bytes(saved)

        row = next(r for r in _table_rows(full) if r.startswith(f"| `{NEW_CLASS}`"))
        mutate_file(MANIFEST, lambda t: t.write_text(
            good.replace(shared.manifest_rows(good)[0][0], sha256(b"x"), 1)),
            "manifest digest mismatch rejected", "exact regeneration")
        mutate_file(CANDIDATES / MODULE, lambda t: t.write_bytes(t.read_bytes() + b"drift\n"),
                    "mirror drift rejected", "mirrors of")
        mutate_file(patch_path(), lambda t: t.unlink(), "missing patch rejected", "missing patch")
        with_patch(lambda s: s.replace(row + "\n", "", 1),
                   "new class row removed rejected", "not the six classes")
        with_patch(lambda s: s.replace(row + "\n", "", 1).replace(
            "| `derived-composites`", "| `derived-composites`", 1).replace(
            "\n\n- A composite", "\n" + row + "\n\n- A composite", 1),
            "new class row misplaced rejected", "not the six classes")
        with_patch(lambda s: s.replace(
            "| `code-content` | Source and test bodies |",
            "| `code-content` | Source bodies |", 1),
            "existing row edited rejected", "byte-identical and in order")
        with_patch(lambda s: s.replace("`derived-composites` consent alone never",
                                       "`derived-composites` consent never", 1),
                   "composite bullet edited rejected", "composite-inheritance")
        with_patch(lambda s: s.replace("no ordering among classes",
                                       "an ordering among classes", 1),
                   "ordering disclaimer removed rejected", "no ordering")
        with_patch(lambda s: s.replace(shared.headings(s)[0],
                                       shared.headings(s)[0] + " changed", 1),
                   "heading change rejected", "heading lines changed")
        with_patch(lambda s: s + "word " * 9000 + "\n",
                   "verify_final_prespec failure on the patched tree rejected",
                   "verify_final_prespec.py fails", scratch_run=True)
        expect("restored package verifies again", check(root), None)
        absent = pathlib.Path(directory) / "absent"
        absent.mkdir()
        code, message = check_command(absent)
        (passed if code == 0 and "absent" in message else failures).append(
            "absent package: --check prints absent and exits 0")
    for label in passed:
        print(f"  pass  {label}")
    for label in failures:
        print(f"  FAIL  {label}")
    print(f"{len(passed) + len(failures)} fixtures, {len(failures)} failing")
    return 1 if failures else 0


def check_command(root: pathlib.Path) -> tuple[int, str]:
    if not (root / PACKAGE).is_dir():
        return 0, (f"RFC-0005 project-documentation package absent: "
                   f"{PACKAGE.as_posix()} does not exist; nothing to verify")
    if applied(root):
        return 0, "RFC-0005 project-documentation package applied: the row equals both mirrors"
    findings = check(root)
    if findings:
        return 1, "RFC-0005 project-documentation package does not verify:\n" + "\n".join(
            f"  {f}" for f in findings)
    return 0, ("RFC-0005 project-documentation manifest matches the patched module on "
               "both identical mirrors; clause leads, front matter and headings "
               "unchanged; the six existing RFC5-14 rows and the composite bullet "
               "are byte-identical; verify_final_prespec, CG-13 and CG-17 pass")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--write", action="store_true",
                      help="regenerate the manifest (retires any copy of its digest)")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.check:
        code, message = check_command(ROOT)
        print(message)
        return code
    if not args.write:
        print("refusing: regenerating the manifest changes the act argument; pass --write")
        return 2
    return write(ROOT)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
