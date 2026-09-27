#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB truth/policy amendment manifests.

This script performs no owner act and writes no act record. The eleven PWB
behavior artifacts form one indivisible subject. The policy and registry are
separate subjects because each requires its own effect-specific owner act.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-truth-policy-amendment"
)
BEHAVIOR_OUT = CANDIDATE / "PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt"
EFFECT_OUT = CANDIDATE / "PWB-EFFECT-AMENDMENT-MANIFEST.txt"

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
EFFECT_SUBJECTS = tuple(
    sorted(
        (
            pathlib.Path(
                ".syzygy/governance/policies/"
                "POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"
            ),
            pathlib.Path(
                ".syzygy/governance/declarations/adapter-registry/"
                "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
            ),
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)
#: Effect rows a later performed act has superseded: once that act's record
#: exists the row is history, fixed at the digest this package offered, and
#: the tree no longer hashes to it.
SUPERSEDED_ROWS = {
    pathlib.Path(
        ".syzygy/governance/declarations/adapter-registry/"
        "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/"
            "PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md"
        ),
        "0765f4d534afad9003463790113fd433d250550091df783c1ff372d227643e4f",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "GOVERNING-DEPENDENCIES.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-OPENING-BAND-SCENARIO-ACT.md"
        ),
        "2b5a453baf53ec03278b5950abe3689267b085275fb21f1a2ef54010b02532f0",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/specs/"
        "polaris-project-wide-butlers-model/spec.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-OPENING-BAND-SCENARIO-ACT.md"
        ),
        "42d073cdeaf7fa7940c5e822b05213267ec1d0064faaaad092f21d264b76a2b1",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "CAPABILITY-COVERAGE.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md"
        ),
        "517d698b55425701919132163d316c3c891097d7a7058281b404e89bd05adcac",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/design.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-EXACT-SOURCE-RENDER-MODE-AMENDMENT-ACT.md"
        ),
        "b89fae42697810692507b5a049aa66949a04afd95d1df1783e95d910e7bfb53e",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md"
        ),
        "77f6b685f7a92eff39d874b92ed36b99e832ded16d1970f1242b6750641b5349",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md"
        ),
        "ada47e4b993951873855a3055e0958bd5e0947ab51060404b0ef11eaff84c578",
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/proposal.md"
    ): (
        pathlib.Path(
            ".syzygy/governance/decisions/PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md"
        ),
        "2054c425e02f4eaffb1a2eeec07238fe4975a8f6eb41d1bc429a4a891fb93a38",
    ),
}


def _later_signed_rows(rel: pathlib.Path) -> set[str]:
    """Digests a performed version-tagged package's manifest declares for
    `rel`: a package counts as performed once `<STEM>-SIGNOFF-v*.md` exists in
    decisions, its candidate directory being the lowercased stem."""
    found: set[str] = set()
    decisions = ROOT / ".syzygy/governance/decisions"
    candidates = ROOT / ".syzygy/governance/contracts/candidates"
    for record in decisions.glob("*-SIGNOFF-v*.md"):
        stem = record.name.rsplit("-SIGNOFF-v", 1)[0].lower()
        for manifest in (candidates / stem).glob("*MANIFEST.txt"):
            for sha, path in ROW.findall(manifest.read_text()):
                if path == rel.as_posix():
                    found.add(sha)
    return found


def superseded_digest(rel: pathlib.Path) -> str | None:
    entry = SUPERSEDED_ROWS.get(rel)
    if entry is not None and (ROOT / entry[0]).is_file():
        return entry[1]
    # General rule: a row a later performed sign-off re-patched stays at the
    # digest this package already offered, when the tree hashes to that
    # sign-off's own manifest row.
    target = ROOT / rel
    if entry is None and target.is_file():
        actual = sha256(target.read_bytes())
        if actual in _later_signed_rows(rel):
            for out in (BEHAVIOR_OUT, EFFECT_OUT):
                if (ROOT / out).is_file():
                    for sha, path in ROW.findall((ROOT / out).read_text()):
                        # Only a row the tree has genuinely moved past.
                        if path == rel.as_posix() and sha != actual:
                            return sha
    return None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def subject_bytes(
    subjects: tuple[pathlib.Path, ...],
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in subjects:
        target = ROOT / rel
        if rel in overrides:
            values[rel] = overrides[rel]
        elif target.is_file():
            values[rel] = target.read_bytes()
        else:
            raise ValueError(f"missing amendment subject: {rel}")
    return values


def render(
    title: str,
    subjects: tuple[pathlib.Path, ...],
    indivisible: bool,
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> str:
    values = subject_bytes(subjects, overrides)
    effect = (
        "All rows take effect together or none do."
        if indivisible
        else "Each row requires its own separate owner act; neither row binds the other."
    )
    lines = [
        f"# {title}",
        "# Candidate; this file and its rows bind nothing by themselves.",
        f"# {len(subjects)} artifacts; rows sorted by codepoint path.",
        f"# {effect}",
    ]
    lines.extend(
        f"{superseded_digest(rel) or sha256(values[rel])}  {rel.as_posix()}"
        for rel in subjects
    )
    return "\n".join(lines) + "\n"


def outputs(overrides: dict[pathlib.Path, bytes] | None = None) -> dict[pathlib.Path, str]:
    return {
        BEHAVIOR_OUT: render(
            "PWB TRUTH-AND-READINESS BEHAVIOR AMENDMENT MANIFEST",
            BEHAVIOR_SUBJECTS,
            True,
            overrides,
        ),
        EFFECT_OUT: render(
            "PWB POLICY-AND-REGISTRY EFFECT AMENDMENT MANIFEST",
            EFFECT_SUBJECTS,
            False,
            overrides,
        ),
    }


def verify_manifest(
    text: str, subjects: tuple[pathlib.Path, ...], expected: str
) -> list[str]:
    findings: list[str] = []
    rows = ROW.findall(text)
    expected_paths = [path.as_posix() for path in subjects]
    if [path for _digest, path in rows] != expected_paths:
        findings.append("manifest path population or order differs")
        return findings
    for digest, path in rows:
        target = ROOT / path
        if not target.is_file():
            findings.append(f"subject missing: {path}")
        elif superseded_digest(pathlib.Path(path)) is not None:
            continue
        elif sha256(target.read_bytes()) != digest:
            findings.append(f"subject digest mismatch: {path}")
    if text != expected:
        findings.append("manifest differs from exact regeneration")
    return findings


def check() -> list[str]:
    findings: list[str] = []
    for out, expected in outputs().items():
        target = ROOT / out
        if not target.is_file():
            findings.append(f"manifest missing: {out}")
            continue
        subjects = BEHAVIOR_SUBJECTS if out == BEHAVIOR_OUT else EFFECT_SUBJECTS
        findings.extend(f"{out}: {item}" for item in verify_manifest(target.read_text(), subjects, expected))
    return findings


def _rule_cases() -> list[tuple[str, bool]]:
    """Fixtures for the general re-patched-row rule of `superseded_digest`.

    A row is history only when the tree digest equals a later performed
    sign-off's manifest row for that path; every other state is strict.
    """
    import tempfile

    rel = next(path for path in BEHAVIOR_SUBJECTS if path not in SUPERSEDED_ROWS)
    old, new = sha256(b"offered\n"), sha256(b"re-patched\n")
    decisions = pathlib.Path(".syzygy/governance/decisions")
    candidates = pathlib.Path(".syzygy/governance/contracts/candidates")

    def result(
        *,
        body: bytes | None = b"re-patched\n",
        record: str | None = "FOO-SIGNOFF-v1.0.md",
        later_dir: str = "foo",
        later_row: tuple[str, str] | None = None,
        offered_in: pathlib.Path = BEHAVIOR_OUT,
        offered: str = old,
        subject: pathlib.Path = rel,
    ) -> str | None:
        later_row = later_row or (new, rel.as_posix())
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            if body is not None:
                (root / subject).parent.mkdir(parents=True, exist_ok=True)
                (root / subject).write_bytes(body)
            if record is not None:
                (root / decisions).mkdir(parents=True, exist_ok=True)
                (root / decisions / record).write_text("record\n")
            (root / candidates / later_dir).mkdir(parents=True, exist_ok=True)
            (root / candidates / later_dir / "FOO-MANIFEST.txt").write_text(
                f"{later_row[0]}  {later_row[1]}\n")
            (root / offered_in).parent.mkdir(parents=True, exist_ok=True)
            (root / offered_in).write_text(f"{offered}  {subject.as_posix()}\n")
            saved = globals()["ROOT"]
            globals()["ROOT"] = root
            try:
                return superseded_digest(subject)
            finally:
                globals()["ROOT"] = saved

    listed = next(iter(SUPERSEDED_ROWS))
    return [
        ("a row the tree hashes to a later sign-off's row stays at its offered digest",
         result() == old),
        ("a row offered in the effect manifest is pinned the same way",
         result(offered_in=EFFECT_OUT) == old),
        ("no performed sign-off record leaves the row strict",
         result(record=None) is None),
        ("a later manifest in another package directory leaves the row strict",
         result(later_dir="bar") is None),
        ("a sign-off record whose stem names another package leaves the row strict",
         result(record="BAR-SIGNOFF-v1.0.md") is None),
        ("a decision record that is not a version-tagged sign-off leaves the row strict",
         result(record="FOO-ACT.md", later_dir="foo-act.md") is None),
        ("a tree digest outside every later manifest row stays strict",
         result(body=b"drifted\n") is None),
        ("a later manifest row for another path leaves the row strict",
         result(later_row=(new, "elsewhere.md")) is None),
        ("an offered row the tree still hashes to is not history",
         result(offered=new) is None),
        ("a missing subject file stays strict", result(body=None) is None),
        ("a listed superseded path never takes the general rule",
         result(subject=listed, later_row=(new, listed.as_posix()),
                body=b"re-patched\n") is None),
    ]


def selftest() -> int:
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        print("SELFTEST FAILED: behavior population is not 11 unique paths")
        return 1
    if len(EFFECT_SUBJECTS) != 2 or len(set(EFFECT_SUBJECTS)) != 2:
        print("SELFTEST FAILED: effect population is not 2 unique paths")
        return 1
    first = BEHAVIOR_SUBJECTS[0]
    baseline = outputs()
    mutated = outputs({first: subject_bytes(BEHAVIOR_SUBJECTS)[first] + b"\nmutation\n"})
    if baseline[BEHAVIOR_OUT] == mutated[BEHAVIOR_OUT]:
        print("SELFTEST FAILED: subject-byte mutation did not change behavior manifest")
        return 1
    rows = ROW.findall(baseline[BEHAVIOR_OUT])
    reordered = baseline[BEHAVIOR_OUT].replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, BEHAVIOR_SUBJECTS, baseline[BEHAVIOR_OUT]):
        print("SELFTEST FAILED: path-order mutation passed")
        return 1
    failed = [name for name, ok in _rule_cases() if not ok]
    if failed:
        print("SELFTEST FAILED: re-patched-row rule: " + "; ".join(failed))
        return 1
    print("selftest: closed populations, byte drift and path order fail closed")
    print("selftest: the re-patched-row rule holds in 11 states")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.check:
        findings = check()
        if findings:
            print("PWB amendment manifests do not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print("PWB amendment manifests match 11 behavior and 2 separate effect subjects")
        return 0
    for rel, body in outputs().items():
        target = ROOT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body)
        print(f"wrote {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
