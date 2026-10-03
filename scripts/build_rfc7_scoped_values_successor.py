#!/usr/bin/env python3
"""Build and verify the inert RFC-0007 scoped-values contract successor.

This script performs no owner act and writes no act record. The package
amends one accepted contract module, `rfcs/RFC-0007/rendering-and-surface.md`
(clause RFC7-33), with the permission paragraph the scoped-attributes
behavior amendment needs
(`candidates/pwb-scoped-attributes-amendment/`, step 1 of its two-act path).
Its act phrase is `SIGN OFF RFC-0007 SCOPED-VALUES AMENDMENT` over this
package's manifest-file digest. It is not yet a link of
`CONTRACT_SUCCESSOR_CHAIN` in `check_governance.py`: a chain link asserts
adoption order, which only the performing act decides.

Layout, under `.syzygy/governance/contracts/candidates/rfc7-scoped-values-successor/`:

- `proposed/RFC-0007/rendering-and-surface.md.patch` — one unified diff whose
  headers name the module relative to `.syzygy/governance/contracts/`
  (`a/rfcs/RFC-0007/rendering-and-surface.md`), the form the manifest row uses.
- `CONTRACT-AMENDMENT-MANIFEST.txt` — one row: the sha256 of the module bytes
  the patch produces.

The proposed bytes are NOT applied while the package is a candidate: CG-7h
binds both mirrors to the bootstrap manifest (and to the readability restyle
link, which excludes this module), so an edit in place would read as drift.
`--apply --at-adoption` writes the patched bytes into both mirrors; it
belongs in the same change as the owner's act record
(`scripts/record_rfc7_scoped_values_successor.py`) and refuses unless that
recorder's `check` finds both act records present and valid against its pins.

`--check` verifies, and prints `absent` and exits 0 when the package
directory does not exist:

1. the patch population is exactly the one expected module;
2. both mirrors of the module are byte-identical, and the patch applies
   cleanly to each, touches only that module and changes it;
3. the manifest equals an exact regeneration over the patched bytes;
4. structure is preserved: the multiset of clause leads matched by
   `verify_final_prespec.py`'s own `CLAUSE_DEF`, the YAML front-matter block
   byte for byte, and the Markdown heading lines outside code fences;
5. when the lane B package still carries its contract patch, applying that
   patch to the current bytes gives the same module bytes as this package's
   patch, so the two cannot drift apart;
6. on a scratch tree holding the patched `candidates/rfcs/`,
   `verify_final_prespec.py`, CG-13 and CG-17 report no failure.

After adoption the patch no longer applies, so `--check` instead reports the
package as applied when the row already equals both current mirrors.

Bare invocation refuses to overwrite the manifest; pass `--write` to
regenerate it. Once a packet quotes the manifest digest, a regeneration
retires the packet's argument (CG-7d/CG-7e catch the stale copy).
"""

from __future__ import annotations

import argparse
import io
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_contract_readability_restyle as shared  # noqa: E402

CONTRACTS = shared.CONTRACTS
CANDIDATES = shared.CANDIDATES
PACKAGE = CANDIDATES / "rfc7-scoped-values-successor"
PROPOSED = PACKAGE / "proposed"
MANIFEST = PACKAGE / "CONTRACT-AMENDMENT-MANIFEST.txt"
MODULE = "rfcs/RFC-0007/rendering-and-surface.md"
TITLE = "RFC-0007 SCOPED-VALUES CONTRACT AMENDMENT MANIFEST"
RECORDER = pathlib.Path("scripts") / "record_rfc7_scoped_values_successor.py"
LANE_B_PATCH = (CANDIDATES / "pwb-scoped-attributes-amendment" / "proposed"
                / "contract" / "RFC-0007-rendering-and-surface.md.patch")
sha256 = shared.sha256


def _recorder():
    return shared._load("record_rfc7_scoped_values_successor_builder", ROOT / RECORDER)


def population(root: pathlib.Path) -> list[str]:
    bootstrap = shared.bootstrap_paths(root)
    if MODULE not in bootstrap:
        raise ValueError(f"{MODULE} is not in the bootstrap population")
    return [MODULE]


def patch_for(path: str) -> pathlib.Path:
    rel = pathlib.PurePosixPath(path).relative_to("rfcs").as_posix()
    return PROPOSED / f"{rel}.patch"


def patch_files(root: pathlib.Path) -> list[pathlib.Path]:
    base = root / PROPOSED
    if not base.is_dir():
        return []
    return sorted((p.relative_to(root) for p in base.rglob("*.patch")),
                  key=lambda p: p.as_posix())


def proposed_bytes(root: pathlib.Path) -> tuple[dict[str, bytes], list[str]]:
    findings: list[str] = []
    out: dict[str, bytes] = {}
    installed_file = root / CONTRACTS / MODULE
    mirror_file = root / CANDIDATES / MODULE
    if not installed_file.is_file() or not mirror_file.is_file():
        return out, [f"mirror pair for `{MODULE}` is incomplete"]
    installed, mirror = installed_file.read_bytes(), mirror_file.read_bytes()
    if installed != mirror:
        findings.append(f"installed and candidate mirrors of `{MODULE}` differ")
    patch = root / patch_for(MODULE)
    if not patch.is_file():
        return out, findings
    results = []
    for label, body in (("installed", installed), ("candidate", mirror)):
        try:
            results.append(shared.apply_patch(MODULE, body, patch))
        except ValueError as error:
            findings.append(f"{label} mirror: {error}")
    if len(results) != 2:
        return out, findings
    if results[0] != results[1]:
        findings.append(f"`{MODULE}` patches to different bytes on the two mirrors")
    elif results[0] == installed:
        findings.append(f"patch for `{MODULE}` changes nothing")
    else:
        out[MODULE] = results[0]
    return out, findings


def render(proposed: dict[str, bytes], paths: list[str]) -> str:
    lines = [
        f"# {TITLE}",
        "# One accepted RFC 0001-0009 module (RFC7-33); the row is sorted by path.",
        "# Paths are relative to .syzygy/governance/contracts/.",
        "# These rows bind only by the owner act that names this file's digest in",
        "# ACCEPTANCE-ACT-RECORD.md; until that act is performed they bind nothing.",
        "# Rows hash the PROPOSED bytes: both identical mirrors with",
        "# proposed/<path under rfcs/>.patch applied. They match the tree only",
        "# after --apply --at-adoption. Installed and candidate-mirror bytes are",
        "# required to match exactly.",
    ]
    lines.extend(f"{sha256(proposed[path])}  {path}" for path in paths)
    return "\n".join(lines) + "\n"


def applied(root: pathlib.Path) -> bool:
    target = root / MANIFEST
    if not target.is_file():
        return False
    rows = shared.manifest_rows(target.read_text(encoding="utf-8"))
    if [path for _sha, path in rows] != population(root):
        return False
    for sha, path in rows:
        for base in (CONTRACTS, CANDIDATES):
            file = root / base / path
            if not file.is_file() or sha256(file.read_bytes()) != sha:
                return False
    return True


def lane_b_findings(root: pathlib.Path, proposed: dict[str, bytes]) -> list[str]:
    """The lane B package's own contract patch must give the same bytes."""
    patch = root / LANE_B_PATCH
    if not patch.is_file() or MODULE not in proposed:
        return []
    old = (root / CONTRACTS / MODULE).read_bytes()
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        target = base / CONTRACTS / MODULE
        target.parent.mkdir(parents=True)
        target.write_bytes(old)
        done = subprocess.run(["git", "apply", "--whitespace=nowarn", str(patch)],
                              cwd=base, capture_output=True, text=True)
        if done.returncode != 0:
            return [f"lane B contract patch does not apply to the current module: "
                    f"{done.stderr.strip()[:200]}"]
        if target.read_bytes() != proposed[MODULE]:
            return ["lane B contract patch and this package's patch give "
                    "different module bytes"]
    return []


STAMP_HEAD = "**Page-level evaluation stamp on the interactive surface.**"
SUBCLAUSE_HEAD = "**Non-citability travels, on every rendering.**"
EXCLUSION = "`non-citable` / `presentation-artifact`"


def exclusion_findings(proposed: dict[str, bytes]) -> list[str]:
    """The added paragraph must keep non-citability off every scope, and the
    sub-clause that follows it must stand: the structure checks compare only
    clause leads, front matter and headings, so removing the exclusion
    sentence would otherwise pass."""
    body = proposed.get(MODULE)
    if body is None:
        return []
    text = body.decode("utf-8")
    start = text.find(STAMP_HEAD)
    end = text.find(SUBCLAUSE_HEAD)
    if start < 0 or end < start:
        return [f"`{MODULE}`: the page-level evaluation stamp paragraph is absent "
                "or does not sit directly above the non-citability sub-clause"]
    paragraph = text[start:end]
    findings = []
    if EXCLUSION not in paragraph or "never carries" not in paragraph:
        findings.append(f"`{MODULE}`: the stamp paragraph does not exclude "
                        "non-citability from every scope")
    if "stands in full" not in paragraph:
        findings.append(f"`{MODULE}`: the stamp paragraph does not state that the "
                        "non-citability sub-clause stands in full")
    return findings


def check(root: pathlib.Path = ROOT, scratch: bool = True) -> list[str]:
    findings: list[str] = []
    paths = population(root)
    expected = [patch_for(path) for path in paths]
    actual = patch_files(root)
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing:
        findings.append("missing patch(es): " + ", ".join(p.as_posix() for p in missing))
    if extra:
        findings.append("patch(es) outside the one-module population: "
                        + ", ".join(p.as_posix() for p in extra))
    proposed, applying = proposed_bytes(root)
    findings.extend(applying)
    clause_def = shared._verifier().CLAUSE_DEF
    for path, body in proposed.items():
        old = (root / CONTRACTS / path).read_bytes()
        findings.extend(shared.structure_findings(path, old, body, clause_def))
    findings.extend(exclusion_findings(proposed))
    findings.extend(lane_b_findings(root, proposed))
    if findings:
        return findings
    target = root / MANIFEST
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST.as_posix()}")
    else:
        findings.extend(shared.verify_manifest(
            target.read_text(encoding="utf-8"), render(proposed, paths), paths))
    if scratch:
        findings.extend(shared.scratch_findings(root, proposed))
    return findings


def apply(root: pathlib.Path, at_adoption: bool, pins=None) -> int:
    if not at_adoption:
        print("refusing: --apply writes the proposed bytes into both mirrors and is "
              "the adoption step; pass --at-adoption in the change that records the act")
        return 2
    try:
        recorded = _recorder().check(root, pins=pins)
    except (ValueError, OSError) as error:
        print(f"refusing to apply: the act records do not validate: {error}")
        return 1
    if not recorded:
        print("refusing to apply: no owner act is recorded; run "
              f"{RECORDER.as_posix()} --record first")
        return 1
    return install(root)


def install(root: pathlib.Path) -> int:
    """Verify the package, then write the proposed bytes into both mirrors.

    Shared by `apply` (the phrase-bound act) and the versioned sign-off
    recorder, which validates its own records before calling it.
    """
    findings = check(root)
    if findings:
        print("refusing to apply: the package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    proposed, _ = proposed_bytes(root)
    for path in population(root):
        for base in (CONTRACTS, CANDIDATES):
            (root / base / path).write_bytes(proposed[path])
        print(f"applied {path} (installed and candidate mirrors)")
    return 0


def write(root: pathlib.Path) -> int:
    proposed, findings = proposed_bytes(root)
    paths = population(root)
    if findings or set(proposed) != set(paths):
        print("refusing to write: the patch does not produce the module")
        for finding in findings:
            print(f"  {finding}")
        return 1
    (root / MANIFEST).parent.mkdir(parents=True, exist_ok=True)
    (root / MANIFEST).write_text(render(proposed, paths), encoding="utf-8")
    print(f"wrote {MANIFEST.as_posix()}")
    return 0


def write_quiet(root: pathlib.Path) -> None:
    with io.StringIO() as sink:
        stdout, sys.stdout = sys.stdout, sink
        try:
            write(root)
        finally:
            sys.stdout = stdout


# --------------------------------------------------------------- selftest

def _fixture_root(scratch: pathlib.Path) -> pathlib.Path:
    """A copy of the inputs this builder reads, with a synthetic package."""
    root = scratch / "repo"
    # The frozen rev9 corpus too: the verifier asserts REV9_ENDS against it
    # and fails when it is absent (syzygy-3rhe).
    for rel in (CONTRACTS / "rfcs", CANDIDATES / "rfcs", CANDIDATES / "fixtures",
                CANDIDATES / "history" / "rev9-rfcs"):
        shutil.copytree(ROOT / rel, root / rel)
    for rel in (shared.BOOTSTRAP_MANIFEST,
                *(CANDIDATES / e for e in shared.SCRATCH_EXTRAS)):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(ROOT / rel, root / rel)
    old = (root / CONTRACTS / MODULE).read_bytes()
    if STAMP_HEAD.encode() in old:
        new = old + b"\n<!-- scoped-values successor fixture -->\n"
    else:
        fixture_paragraph = (
            f"{STAMP_HEAD} Fixture text. A scope never carries {EXCLUSION}; the "
            "non-citability sub-clause below stands in full.\n\n").encode()
        new = old.replace(SUBCLAUSE_HEAD.encode(),
                          fixture_paragraph + SUBCLAUSE_HEAD.encode(), 1)
        assert new != old
    target = root / patch_for(MODULE)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(shared.make_patch(MODULE, old, new), encoding="utf-8")
    return root


def selftest() -> int:
    failures: list[str] = []
    passed: list[str] = []

    def expect(label, findings, want):
        ok = any(want in f for f in findings) if want else not findings
        (passed if ok else failures).append(
            label if ok else f"{label}: got {findings[:3]}")

    with tempfile.TemporaryDirectory() as directory:
        scratch = pathlib.Path(directory)
        root = _fixture_root(scratch)
        expect("unwritten manifest reported", check(root, scratch=False),
               "manifest missing")
        write_quiet(root)
        expect("valid one-patch package verifies, scratch structure included",
               check(root), None)
        manifest = root / MANIFEST
        good = manifest.read_text(encoding="utf-8")
        rows = shared.manifest_rows(good)
        (passed if [p for _s, p in rows] == [MODULE] else failures).append(
            "manifest is exactly the one RFC-0007 rendering module")

        def mutate_file(rel, transform, label, want, scratch_run=False):
            target = root / rel
            saved = target.read_bytes() if target.exists() else None
            transform(target)
            try:
                expect(label, check(root, scratch=scratch_run), want)
            finally:
                if saved is None:
                    target.unlink()
                else:
                    target.write_bytes(saved)

        mutate_file(MANIFEST, lambda t: t.write_text(
            good.replace(rows[0][0], sha256(b"tampered"), 1)),
            "manifest row digest mismatch rejected", "exact regeneration")
        mutate_file(MANIFEST, lambda t: t.write_text(
            good.replace(MODULE, "rfcs/RFC-0007/narrative-contract.md")),
            "manifest naming another module rejected", "population or order")
        mutate_file(CANDIDATES / MODULE, lambda t: t.write_bytes(
            t.read_bytes() + b"drift\n"),
            "mirror drift rejected", "mirrors of")
        mutate_file(patch_for(MODULE), lambda t: t.unlink(),
                    "missing patch rejected", "missing patch")
        mutate_file(PROPOSED / "RFC-0007" / "narrative-contract.md.patch",
                    lambda t: t.write_text(shared.make_patch(
                        "rfcs/RFC-0007/narrative-contract.md", b"x\n", b"y\n")),
                    "patch for another module rejected", "outside the one-module")

        def identity_patch(t):
            lines = (root / CONTRACTS / MODULE).read_text(encoding="utf-8").splitlines()
            before, line, after = lines[1:4]
            t.write_text(f"diff --git a/{MODULE} b/{MODULE}\n--- a/{MODULE}\n"
                         f"+++ b/{MODULE}\n@@ -2,3 +2,3 @@\n {before}\n"
                         f"-{line}\n+{line}\n {after}\n")

        mutate_file(patch_for(MODULE), identity_patch,
                    "identity (no-op) patch rejected as changing nothing",
                    "changes nothing")
        both = []
        for base in (CONTRACTS, CANDIDATES):
            both.append((base / MODULE, (root / base / MODULE).read_bytes()))
            drifted = (root / base / MODULE).read_bytes().replace(
                SUBCLAUSE_HEAD.encode(), SUBCLAUSE_HEAD.encode() + b" drifted", 1)
            assert drifted != both[-1][1]
            (root / base / MODULE).write_bytes(drifted)
        expect("patch over drifted mirrors rejected",
               check(root, scratch=False), "does not apply")
        for rel, body in both:
            (root / rel).write_bytes(body)

        def rewrite(fn):
            old = (root / CONTRACTS / MODULE).read_bytes()
            new = fn(old.decode("utf-8")).encode("utf-8")
            assert new != old
            return lambda t: t.write_text(shared.make_patch(MODULE, old, new))

        text = (root / CONTRACTS / MODULE).read_text(encoding="utf-8")
        mutate_file(patch_for(MODULE), rewrite(lambda s: s.replace(
            shared.headings(s)[0], shared.headings(s)[0] + " changed", 1)),
            "heading change rejected", "heading lines changed")
        if shared.front_matter(text) is not None:
            mutate_file(patch_for(MODULE), rewrite(
                lambda s: s.replace("\nid: ", "\nid:  ", 1)),
                "front-matter change rejected", "front matter changed")
        else:
            passed.append("front-matter change rejected (module has none; skipped)")
        clause_def = shared._verifier().CLAUSE_DEF

        def drop_clause(s):
            m = clause_def.search(s)
            return s[:m.start()] + "**Clause" + s[m.start() + 2:]

        mutate_file(patch_for(MODULE), rewrite(drop_clause),
                    "clause-lead change rejected", "clause leads changed")

        def stamp_mutation(transform):
            def writer(t):
                old = (root / CONTRACTS / MODULE).read_bytes()
                full = proposed_bytes(root)[0][MODULE].decode("utf-8")
                cut = full.index(STAMP_HEAD)
                new = full[:cut] + transform(full[cut:])
                t.write_text(shared.make_patch(MODULE, old, new.encode("utf-8")))
            return writer

        mutate_file(patch_for(MODULE), stamp_mutation(
            lambda s: s.replace(EXCLUSION, "the two flags", 1)),
            "non-citability exclusion removed from the stamp paragraph rejected",
            "does not exclude")
        mutate_file(patch_for(MODULE), stamp_mutation(
            lambda s: s.replace("never carries", "may carry", 1)),
            "exclusion verb weakened rejected", "does not exclude")
        mutate_file(patch_for(MODULE), stamp_mutation(
            lambda s: s.replace("stands in full", "stands", 1)),
            "sub-clause standing sentence removed rejected", "stands in full")
        mutate_file(patch_for(MODULE), stamp_mutation(
            lambda s: s.replace(STAMP_HEAD, "**Another heading.**", 1)),
            "stamp paragraph heading removed rejected", "absent")
        saved_manifest = manifest.read_bytes()

        def oversize(t):
            old = (root / CONTRACTS / MODULE).read_bytes()
            good_new = proposed_bytes(root)[0][MODULE]
            t.write_text(shared.make_patch(MODULE, old, good_new + b"\nword" * 7200 + b"\n"))
            write_quiet(root)

        mutate_file(patch_for(MODULE), oversize,
                    "verify_final_prespec failure on the patched tree rejected",
                    "verify_final_prespec.py fails", scratch_run=True)
        manifest.write_bytes(saved_manifest)
        # The lane B patch must agree with this package's patch.
        lane = root / LANE_B_PATCH
        lane.parent.mkdir(parents=True, exist_ok=True)
        old = (root / CONTRACTS / MODULE).read_bytes()
        lane.write_text(shared.make_patch(
            MODULE, old, old + b"\n<!-- a different amendment -->\n"))
        # The lane B patch names the repo-relative path; use that form.
        lane.write_text(lane.read_text().replace(
            f"a/{MODULE}", f"a/{CONTRACTS.as_posix()}/{MODULE}").replace(
            f"b/{MODULE}", f"b/{CONTRACTS.as_posix()}/{MODULE}"))
        expect("lane B patch giving other bytes rejected",
               check(root, scratch=False), "different module bytes")
        lane.unlink()
        expect("restored package verifies again", check(root), None)

        recorder = _recorder()
        aggregate = root / recorder.AGGREGATE
        aggregate.parent.mkdir(parents=True, exist_ok=True)
        aggregate.write_text("# Synthetic aggregate\n")
        manifest_sha = sha256(manifest.read_bytes())
        pins = recorder.write_review(
            root, "docs/reviews/R-SCOPED-VALUES-CONFIRM-RAW.md", manifest_sha)
        with io.StringIO() as sink:
            stdout, sys.stdout = sys.stdout, sink
            try:
                refused = apply(root, at_adoption=False, pins=pins)
                unrecorded = apply(root, at_adoption=True, pins=pins)
                unrecorded_said = sink.getvalue()
                recorder.record(root, f"{recorder.LABEL}: {manifest_sha}",
                                "2026-10-02T00:00:00Z", verify=False, pins=pins)
                act = root / recorder.ACT
                saved_act = act.read_bytes()
                act.write_bytes(saved_act.replace(b"Owner: Tzeusy", b"Owner: x"))
                invalid = apply(root, at_adoption=True, pins=pins)
                act.write_bytes(saved_act)
                unpinned = apply(root, at_adoption=True,
                                 pins=recorder.Pins(None, None, None))
                untouched = not applied(root)
                done = apply(root, at_adoption=True, pins=pins)
            finally:
                sys.stdout = stdout
        (passed if refused == 2 else failures).append(
            "apply without --at-adoption refused")
        (passed if unrecorded == 1 and "no owner act is recorded" in unrecorded_said
         else failures).append("apply --at-adoption without act records refused")
        (passed if invalid == 1 and unpinned == 1 and untouched else failures).append(
            "apply --at-adoption over an edited record or an unpinned recorder "
            "refused, nothing written")
        (passed if done == 0 and applied(root) else failures).append(
            "apply --at-adoption after a valid record installs both mirrors")
        absent = scratch / "absent"
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


# ------------------------------------------------------------------- main

def check_command(root: pathlib.Path) -> tuple[int, str]:
    if not (root / PACKAGE).is_dir():
        return 0, (f"RFC-0007 scoped-values package absent: {PACKAGE.as_posix()} "
                   "does not exist; nothing to verify")
    if applied(root):
        return 0, ("RFC-0007 scoped-values package applied: the manifest row "
                   "equals both current mirrors")
    findings = check(root)
    if findings:
        return 1, "RFC-0007 scoped-values package does not verify:\n" + "\n".join(
            f"  {finding}" for finding in findings)
    return 0, ("RFC-0007 scoped-values manifest matches the patched module on both "
               "identical mirrors; clause leads, front matter and headings "
               "unchanged; the lane B contract patch gives the same bytes; "
               "verify_final_prespec, CG-13 and CG-17 pass on the patched tree")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Build and verify the RFC-0007 scoped-values successor package.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--write", action="store_true",
                      help="regenerate the manifest (retires any packet quoting it)")
    parser.add_argument("--at-adoption", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.check:
        code, message = check_command(ROOT)
        print(message)
        return code
    if not (ROOT / PACKAGE).is_dir():
        print(f"refusing: package directory {PACKAGE.as_posix()} does not exist")
        return 1
    if args.apply:
        return apply(ROOT, args.at_adoption)
    if not args.write:
        print("refusing: regenerating the manifest changes the act argument; pass "
              "--write, then update every registered copy of the digest")
        return 2
    return write(ROOT)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
