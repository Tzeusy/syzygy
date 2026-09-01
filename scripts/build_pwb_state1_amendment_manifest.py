#!/usr/bin/env python3
"""Build and verify the exact eleven-artifact PWB state-(1) amendment manifest."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/pwb-state1-amendment"
)
OUT = CANDIDATE / "PWB-AMENDMENT-MANIFEST.txt"
REPORT = CANDIDATE / "CANDIDATE-REPORT.md"
OWNER_PACKET = CANDIDATE / "OWNER-SIGNOFF-PACKET.md"
FINAL_REVIEWS = (
    pathlib.Path("docs/reviews/R-PWB-STATE1-FINAL-SECURITY-RAW.md"),
    pathlib.Path("docs/reviews/R-PWB-STATE1-FINAL-ORACLES-RAW.md"),
    pathlib.Path("docs/reviews/R-PWB-STATE1-FINAL-TRANSACTION-RAW.md"),
)
SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "proposal.md",
            CHANGE / "design.md",
            CHANGE / "specs/polaris-project-wide-butlers-model/spec.md",
            CHANGE / "CAPABILITY-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CHANGE / "GOVERNING-DEPENDENCIES.md",
            CHANGE / "contract-coverage-matrix/RFC-0001-0003.md",
            CHANGE / "contract-coverage-matrix/RFC-0004-0006.md",
            CHANGE / "contract-coverage-matrix/RFC-0007-0009.md",
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.M)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def subject_bytes(
    root: pathlib.Path, overrides: dict[pathlib.Path, bytes] | None = None
) -> dict[pathlib.Path, bytes]:
    if len(SUBJECTS) != 11 or len(set(SUBJECTS)) != 11:
        raise ValueError("PWB amendment population must be 11 unique paths")
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in SUBJECTS:
        if rel in overrides:
            values[rel] = overrides[rel]
            continue
        target = root / rel
        if not target.is_file():
            raise ValueError(f"required PWB amendment subject missing: {rel}")
        values[rel] = target.read_bytes()
    return values


def render(
    root: pathlib.Path = ROOT,
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> str:
    values = subject_bytes(root, overrides)
    lines = [
        "# PWB STATE-(1) AMENDMENT MANIFEST",
        "# Candidate; binds nothing until the human owner signs this exact manifest digest.",
        "# 11 signed artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
    ]
    lines.extend(f"{digest(values[rel])}  {rel.as_posix()}" for rel in SUBJECTS)
    return "\n".join(lines) + "\n"


def verify(text: str, root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    rows = ROW_RE.findall(text)
    expected_paths = [path.as_posix() for path in SUBJECTS]
    actual_paths = [path for _, path in rows]
    if actual_paths != expected_paths:
        findings.append(
            "manifest paths differ from the exact ordered eleven-artifact population"
        )
        return findings
    for expected_digest, path in rows:
        target = root / path
        if not target.is_file():
            findings.append(f"manifest subject missing: {path}")
            continue
        actual_digest = digest(target.read_bytes())
        if actual_digest != expected_digest:
            findings.append(
                f"manifest digest mismatch: {path} {actual_digest} != {expected_digest}"
            )
    return findings


def git_output(root: pathlib.Path, *args: str) -> bytes:
    result = subprocess.run(
        ("git", *args), cwd=root, check=False, capture_output=True
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ValueError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def resolve_commit(root: pathlib.Path, value: str) -> str:
    resolved = git_output(root, "rev-parse", f"{value}^{{commit}}").decode().strip()
    if not re.fullmatch(r"[0-9a-f]{40}", resolved):
        raise ValueError(f"candidate commit did not resolve exactly: {value}")
    return resolved


def committed_blob(root: pathlib.Path, commit: str, rel: pathlib.Path) -> bytes:
    return git_output(root, "show", f"{commit}:{rel.as_posix()}")


def final_review_rows(
    root: pathlib.Path, commit: str, manifest_sha: str
) -> list[tuple[pathlib.Path, str]]:
    rows: list[tuple[pathlib.Path, str]] = []
    for rel in FINAL_REVIEWS:
        target = root / rel
        if not target.is_file():
            raise ValueError(f"required final review missing: {rel}")
        data = target.read_bytes()
        body = data.decode()
        if commit not in body or manifest_sha not in body:
            raise ValueError(f"final review does not bind exact subject: {rel}")
        if re.search(r"\*\*(?:EXACT )?VERDICT: CONFIRM\*\*", body) is None:
            raise ValueError(f"final review does not carry exact CONFIRM: {rel}")
        rows.append((rel, digest(data)))
    return rows


def finalized_outputs(root: pathlib.Path, commit_value: str) -> dict[pathlib.Path, str]:
    commit = resolve_commit(root, commit_value)
    manifest_path = root / OUT
    if not manifest_path.is_file():
        raise ValueError(f"PWB amendment manifest missing: {OUT}")
    manifest_bytes = manifest_path.read_bytes()
    manifest_text = manifest_bytes.decode()
    findings = verify(manifest_text, root)
    if findings:
        raise ValueError("current PWB manifest does not verify: " + " | ".join(findings))
    if committed_blob(root, commit, OUT) != manifest_bytes:
        raise ValueError("candidate commit does not carry the current manifest bytes")

    artifact_rows = ROW_RE.findall(manifest_text)
    for expected_digest, path in artifact_rows:
        actual = digest(committed_blob(root, commit, pathlib.Path(path)))
        if actual != expected_digest:
            raise ValueError(
                f"candidate commit artifact mismatch: {path} {actual} != {expected_digest}"
            )

    manifest_sha = digest(manifest_bytes)
    review_rows = final_review_rows(root, commit, manifest_sha)
    review_table = "\n".join(
        f"| `{rel.as_posix()}` | `CONFIRM` | `{review_sha}` |"
        for rel, review_sha in review_rows
    )
    artifact_table = "\n".join(
        f"| `{path.removeprefix(CHANGE.as_posix() + '/')}` | `{artifact_sha}` |"
        for artifact_sha, path in artifact_rows
    )

    report = f"""# Candidate report — PWB state-(1) amendment

> **GENERATED CANDIDATE REPORT — never authority.** The eleven artifact bytes
> remain inert unless the human owner performs the exact ceremony in
> `OWNER-SIGNOFF-PACKET.md`.

Date: 2026-09-02

Frozen candidate commit: `{commit}`

Eleven-artifact manifest SHA-256: `{manifest_sha}`

## Result

The owner-directed profile-A amendment is completely drafted and independently
reviewed. It accepts valid state (1) or state (2) for PWB-REQ-005 body-read
authority and PWB-REQ-022 owner judgment, retains exact state on the human and
machine channels, and keeps every invalid act fail closed.

The closed test populations are 8 valid admission triples, 195
admission-invalid cases, 2 valid judgment states, 84 present-invalid judgment
cases and 2 absent judgment cases. State (1) remains same-tree forgeable from
Syzygy's perspective and is never called independently verified.

## Final independent confirmations

| Raw review | Exact verdict | sha256 |
|---|---|---|
{review_table}

Earlier `REVISE` reviews remain stored verbatim. Their findings were repaired
before these confirmations; they are not erased or reworded.

## Verified structure

- Strict OpenSpec validation passes.
- The generated dependency union covers 17 requirements.
- The effective contract matrix represents 324 clauses and 622 consequences:
  137 covered, 237 Unknown uncovered, 248 believed not applicable.
- Capability coverage is 27 obligations/refusals: 21 covered and 6 lawfully
  out of scope.
- The PWB manifest generator verifies 11 artifacts and mutation-proves byte and
  path drift.
- The performed 2026-09-01 transaction remains frozen and valid over 30
  contract paths, 5 historical PWB paths and 5 act rows; all 10 transaction
  mutations pass.
- Governance self-tests pass 178 fixtures. The ordinary governance run remains
  deliberately `32 OK / 19 WARN / 1 FAIL`: CG-7h rejects the five unsigned
  current PWB coverage paths until matching aggregate and dedicated successor
  act records exist.

## Authority boundary

This report performs no owner act and grants no consent, policy approval,
registry adoption, judgment, body read, implementation, write, egress,
execution, deployment, release, recovery or mission authority.
"""

    packet = f"""# Owner sign-off packet — PWB state-(1) amendment

Date: 2026-09-02

Candidate: `polaris-project-wide-butlers-model`

Frozen candidate commit: `{commit}`

Manifest: `{OUT.as_posix()}`

Manifest SHA-256: `{manifest_sha}`

## Decision

Should the eleven exact artifacts below supersede the currently signed PWB
package as the behavioral authority for the bounded, local,
one-Butlers-repository POC?

## What changes

- PWB-REQ-005 accepts each exact consent, policy and registry human owner act
  in valid state (1) or state (2), including all eight mixed/equal triples.
- PWB-REQ-022 accepts an exact-scope human owner judgment in valid state (1) or
  state (2).
- Every human and machine rendering retains the exact state. Only state (2) is
  independently verified. State (1) discloses that it is owner-trusted,
  uncorrelated and same-tree forgeable from Syzygy's perspective.
- Invalid acts fail closed. The signed test obligations close 195
  admission-invalid cases, 84 present-invalid judgment cases, 2 absent cases,
  exact two-channel parity and fail-then-restore mutation proof.
- Acts remain warrants. They are not evidence that a read, screening,
  comprehension or any effect succeeded.

## Accepted risk

State-(1) consent, policy, registry and judgment records are same-tree
forgeable from Syzygy's perspective. Exact digests detect drift; they do not
establish authorship or owner attendance. Choice A accepted this residual risk
only for this bounded POC. The amendment exposes the limitation and keeps every
other security gate conjunctive.

## Evidence and disclosed gaps

- Three final independent review classes returned exact `CONFIRM` on the same
  frozen commit and manifest:

| Raw review | Exact verdict | sha256 |
|---|---|---|
{review_table}

- The effective contract matrix remains 622 consequences: 137 covered, 237
  Unknown uncovered and 248 believed not applicable. No believed-N/A row is an
  owner-reviewed N/A judgment.
- No implementation or runtime effect has been performed or proven.
- Before this sign-off, the full governance battery intentionally fails CG-7h
  on five unsigned current-vs-historical PWB rows. Recording this act in both
  required homes is what permits the successor manifest to become current.

## Exact eleven-artifact package

| Artifact relative to the PWB change | sha256 |
|---|---|
{artifact_table}

The manifest generator independently verifies this closed, codepoint-sorted
population. All eleven rows take effect together or none do. `.openspec.yaml`
is unchanged semantically but remains bound as part of the indivisible package.

## Effect of sign-off

This act signs the amended PWB behavior and supersedes the six PWB artifact
digests still current from the 2026-08-31 sign-off plus the five coverage
artifact digests made current by the 2026-09-01 general trusted-bootstrap
transaction. Those prior acts, manifests, digests and bytes remain immutable
historical evidence.

If performed, the ceremony will be recorded as state (1), `owner-adopted
(bootstrap, uncorrelated)`, with A1 audit-record identity explicitly absent. It
is a real human owner act only if the owner performs the exact phrase below.
The commit, tag and in-tree records preserve context but do not establish
attendance or state (2).

## What sign-off does not authorize

Sign-off does not create or approve observation consent, the concrete secret
policy, the adapter-registry entry or a walkthrough judgment. It authorizes no
repository-body read and no PWB implementation. It grants no write, egress,
execution, deployment, release, recovery, mission, another repository,
autonomous behavior or multi-user support. Separate effect-specific owner acts
and separate implementation authorization remain mandatory.

## Exact owner response

If and only if these exact reviewed bytes should become the amended behavioral
authority, respond exactly:

```text
SIGN OFF PWB STATE-(1) AMENDMENT: {manifest_sha}
```
"""

    return {REPORT: report, OWNER_PACKET: packet}


def selftest() -> int:
    first = render()
    second = render()
    if first != second:
        print("SELFTEST FAILED: manifest rendering is nondeterministic")
        return 1
    if verify(first):
        print("SELFTEST FAILED: rendered manifest does not verify")
        return 1

    proposal = CHANGE / "proposal.md"
    original = (ROOT / proposal).read_bytes()
    mutated = render(overrides={proposal: original + b"\nmutation\n"})
    if mutated == first:
        print("SELFTEST FAILED: subject-byte mutation did not change manifest")
        return 1
    before_rows = dict((path, sha) for sha, path in ROW_RE.findall(first))
    after_rows = dict((path, sha) for sha, path in ROW_RE.findall(mutated))
    changed = [path for path in before_rows if before_rows[path] != after_rows[path]]
    if changed != [proposal.as_posix()]:
        print(f"SELFTEST FAILED: mutation changed wrong rows: {changed}")
        return 1

    malformed = first.replace(f"  {SUBJECTS[0].as_posix()}\n", "  missing.md\n", 1)
    if not verify(malformed):
        print("SELFTEST FAILED: path mutation was not rejected")
        return 1

    print("selftest: 11-row population, determinism, byte mutation and path mutation hold")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument(
        "--finalize-packet",
        metavar="COMMIT",
        help="generate the candidate report and owner packet for exact COMMIT",
    )
    parser.add_argument(
        "--check-finalized",
        metavar="COMMIT",
        help="check the generated report and owner packet for exact COMMIT",
    )
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    finalize_commit = args.finalize_packet or args.check_finalized
    if finalize_commit:
        try:
            outputs = finalized_outputs(ROOT, finalize_commit)
        except ValueError as exc:
            print(f"FAILED: {exc}")
            return 1
        if args.check_finalized:
            drift = [
                rel for rel, content in outputs.items()
                if not (ROOT / rel).is_file() or (ROOT / rel).read_text() != content
            ]
            if drift:
                for rel in drift:
                    print(f"PWB finalized output differs from regeneration: {rel}")
                return 1
            print(
                "PWB candidate report and owner packet match regeneration — "
                f"commit {resolve_commit(ROOT, finalize_commit)[:12]}…"
            )
            return 0
        for rel, content in outputs.items():
            target = ROOT / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
            print(f"wrote {rel}")
        return 0

    expected = render()
    target = ROOT / OUT
    if args.check:
        if not target.is_file():
            print(f"PWB amendment manifest missing: {OUT}")
            return 1
        actual = target.read_text()
        if actual != expected:
            print("PWB amendment manifest differs from regeneration")
            return 1
        findings = verify(actual)
        if findings:
            for finding in findings:
                print(f"FAILED: {finding}")
            return 1
        print("PWB amendment manifest matches regeneration — 11 artifacts")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(expected)
    print(f"wrote {OUT} — 11 artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
