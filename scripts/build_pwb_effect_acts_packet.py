#!/usr/bin/env python3
"""Build and verify the three-artifact PWB effect-act manifest and owner packet.

The three artifacts are the effect-specific authorities PWB-REQ-005 requires
before any Butlers project-shape body read: the observation-consent record, the
observing project's secret-classification policy and the observer's
adapter-registry entry. Each takes effect only through its own separate human
owner act bound to that artifact's exact SHA-256 (RFC3-16(b) item 3). This
script performs no act; it renders the closed population, verifies drift and
generates the plain-language packet the owner reads.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CANDIDATE = pathlib.Path(".syzygy/governance/contracts/candidates/pwb-effect-acts")
OUT = CANDIDATE / "PWB-EFFECT-ACTS-MANIFEST.txt"
ACT_SEMANTICS = CANDIDATE / "ACT-SEMANTICS.md"
REPORT = CANDIDATE / "CANDIDATE-REPORT.md"
OWNER_PACKET = CANDIDATE / "OWNER-SIGNOFF-PACKET.md"
SECURITY_REVIEW = pathlib.Path("docs/reviews/R-PWB-EFFECT-ACTS-SECURITY-RAW.md")

CONSENT = pathlib.Path(
    ".syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md"
)
POLICY = pathlib.Path(
    ".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"
)
REGISTRY = pathlib.Path(
    ".syzygy/governance/declarations/adapter-registry/"
    "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
)
SUBJECTS = tuple(sorted((CONSENT, POLICY, REGISTRY), key=lambda p: p.as_posix()))

# One act per artifact. The label is the exact owner phrase prefix; the
# argument is the artifact's own SHA-256, so the phrase binds the bytes directly.
ACTS = (
    ("consent-observation", CONSENT, "CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION"),
    ("approve-policy", POLICY, "APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY"),
    ("adopt-registry-entry", REGISTRY, "ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY"),
)
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.M)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def subject_bytes(
    root: pathlib.Path, overrides: dict[pathlib.Path, bytes] | None = None
) -> dict[pathlib.Path, bytes]:
    if len(SUBJECTS) != 3 or len(set(SUBJECTS)) != 3:
        raise ValueError("PWB effect-act population must be 3 unique paths")
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in SUBJECTS:
        if rel in overrides:
            values[rel] = overrides[rel]
            continue
        target = root / rel
        if not target.is_file():
            raise ValueError(f"required effect-act subject missing: {rel}")
        values[rel] = target.read_bytes()
    return values


def render(
    root: pathlib.Path = ROOT,
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> str:
    values = subject_bytes(root, overrides)
    lines = [
        "# PWB EFFECT-ACTS MANIFEST",
        "# Candidate; each row takes effect only through its own separate owner act",
        "# bound to that row's exact digest. No row binds anything by itself.",
        "# 3 artifacts; rows sorted by codepoint path.",
    ]
    lines.extend(f"{digest(values[rel])}  {rel.as_posix()}" for rel in SUBJECTS)
    return "\n".join(lines) + "\n"


def verify(text: str, root: pathlib.Path = ROOT) -> list[str]:
    findings: list[str] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ROW_RE.fullmatch(stripped) is None:
            findings.append(
                f"manifest line {line_number} is neither a comment nor a digest row"
            )
    rows = ROW_RE.findall(text)
    expected_paths = [path.as_posix() for path in SUBJECTS]
    actual_paths = [path for _, path in rows]
    if actual_paths != expected_paths:
        findings.append(
            "manifest paths differ from the exact ordered three-artifact population"
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


def phrases(values: dict[pathlib.Path, bytes]) -> list[tuple[str, pathlib.Path, str]]:
    """Return (act type, artifact, exact owner phrase) for each of the three acts."""
    return [
        (act_type, rel, f"{label}: {digest(values[rel])}")
        for act_type, rel, label in ACTS
    ]


def review_binds_exact(body: str, commit: str, manifest_sha: str) -> bool:
    commit_pattern = re.compile(
        r"^- \[Observed\] (?:Exact reviewed|Reviewed) commit:\s*\n"
        + r"\s*`" + re.escape(commit) + r"`\.$",
        re.M,
    )
    manifest_pattern = re.compile(
        r"^- \[Observed\] Manifest SHA-256:\s*\n"
        + r"\s*`" + re.escape(manifest_sha) + r"`\.$",
        re.M,
    )
    verdicts = re.findall(
        r"^\*\*(?:EXACT )?VERDICT: ([A-Z][A-Z ]*)\*\*$", body, re.M
    )
    return (
        commit_pattern.search(body) is not None
        and manifest_pattern.search(body) is not None
        and bool(verdicts)
        and all(verdict == "CONFIRM" for verdict in verdicts)
    )


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


def finalized_outputs(root: pathlib.Path, commit_value: str) -> dict[pathlib.Path, str]:
    commit = resolve_commit(root, commit_value)
    manifest_path = root / OUT
    if not manifest_path.is_file():
        raise ValueError(f"effect-act manifest missing: {OUT}")
    manifest_bytes = manifest_path.read_bytes()
    manifest_text = manifest_bytes.decode()
    findings = verify(manifest_text, root)
    if findings:
        raise ValueError("current manifest does not verify: " + " | ".join(findings))
    if manifest_text != render(root):
        raise ValueError("current manifest differs from exact regeneration")
    if committed_blob(root, commit, OUT) != manifest_bytes:
        raise ValueError("candidate commit does not carry the current manifest bytes")
    if committed_blob(root, commit, ACT_SEMANTICS) != (root / ACT_SEMANTICS).read_bytes():
        raise ValueError("candidate commit does not carry the current ACT-SEMANTICS bytes")

    values: dict[pathlib.Path, bytes] = {}
    for expected_digest, path in ROW_RE.findall(manifest_text):
        blob = committed_blob(root, commit, pathlib.Path(path))
        if digest(blob) != expected_digest:
            raise ValueError(f"candidate commit artifact mismatch: {path}")
        values[pathlib.Path(path)] = blob
    manifest_sha = digest(manifest_bytes)

    review_path = root / SECURITY_REVIEW
    if not review_path.is_file():
        raise ValueError(f"required security review missing: {SECURITY_REVIEW}")
    review_bytes = review_path.read_bytes()
    if not review_binds_exact(review_bytes.decode(), commit, manifest_sha):
        raise ValueError(
            "security review lacks exact subject binding or unanimous CONFIRM"
        )
    review_sha = digest(review_bytes)

    act_rows = phrases(values)
    consent_sha = digest(values[CONSENT])
    policy_sha = digest(values[POLICY])
    registry_sha = digest(values[REGISTRY])
    phrase_block = "\n".join(
        f"```text\n{phrase}\n```" for _, _, phrase in act_rows
    )

    report = f"""# Candidate report — PWB effect acts (consent, secret policy, observer registry)

> **GENERATED CANDIDATE REPORT — never authority.** The three artifacts bind
> nothing until the human owner performs the exact phrases in
> `OWNER-SIGNOFF-PACKET.md`; each phrase acts on one artifact only.

Frozen candidate commit: `{commit}`

Three-artifact manifest SHA-256: `{manifest_sha}`

## Result

The three effect-specific authorities PWB-REQ-005 requires before any Butlers
project-shape body read are drafted at their final bytes, cite only the
currently signed PWB package (`2e453a6e…`, manifest `14a84aba…`) and the
currently accepted RFC-0004 general contract (`b21fc950…`), and carry the
PWB-REQ-005 authority-specific fields. Each is offered for a separate state-(1)
human owner act bound to its own SHA-256.

| Act type | Artifact | sha256 |
|---|---|---|
| `consent-observation` | `{CONSENT.as_posix()}` | `{consent_sha}` |
| `approve-policy` | `{POLICY.as_posix()}` | `{policy_sha}` |
| `adopt-registry-entry` | `{REGISTRY.as_posix()}` | `{registry_sha}` |

## Independent confirmation

| Raw review | Exact verdict | sha256 |
|---|---|---|
| `{SECURITY_REVIEW.as_posix()}` | `CONFIRM` | `{review_sha}` |

## Authority boundary

This report performs no owner act. Even after all three acts, no body read
occurs until separate PWB implementation authorization (task 1.8) exists and
an implementation evaluates the acts under PWB-REQ-005.
"""

    packet = f"""# Owner sign-off packet — the three Butlers observation authorities

Frozen candidate commit: `{commit}`

Manifest: `{OUT.as_posix()}` (SHA-256 `{manifest_sha}`)

Act semantics: `{ACT_SEMANTICS.as_posix()}`

## What you are being asked

Before Syzygy may read any Butlers project-shape file, three separate things
need your act: consent to observe Butlers, approval of the secret-screening
policy that runs on everything read, and adoption of the registry entry that
says exactly what the observer may read. This packet offers all three. Each
phrase below is one act on one file, bound to that file's exact SHA-256. You
may perform one, two or all three; a body read needs all three.

Performing an act here is a **state-(1)** act: owner-trusted, uncorrelated, and
same-tree forgeable from Syzygy's perspective. Its digest detects later drift;
it does not prove authorship or attendance. No independent audit trail (A1)
exists, and the act records that absence explicitly. This is the trust model
you selected on 2026-08-31 and signed into PWB-REQ-005 on 2026-09-02.

## The three files

**1. Observation consent** — `{CONSENT.as_posix()}`
SHA-256 `{consent_sha}`

Records your 2026-08-31 statement ("you have consent for butlers observation;
obviously don't read secrets from butler") as a consent record for the pair
(project:syzygy, repository:butlers-configured-poc), content class
`declared-project-shape-text`. Scope: read-only Git objects selected by the
signed PWB source population, at the Butlers revision the POC observes. It
excludes PostgreSQL, credential stores, secret APIs, `.env` and credential
files, arbitrary implementation-file bodies, working-tree traversal, code
execution, network egress, writes to Butlers and any second repository. No
silent expiry; you may narrow or revoke by a later act. It does not
retroactively authorize the reads recorded in the precondition-read incident.

**2. Secret-classification policy** — `{POLICY.as_posix()}`
SHA-256 `{policy_sha}`

Syzygy's own concrete policy for screening Butlers bytes before anything is
modeled. Denied filenames and suffixes (`.env*`, `credentials.json`,
`secrets.json`, `id_rsa`, `id_ed25519`, `.pem`, `.key`, `.p12`, `.pfx`), four
detectors (private-key blocks, known token formats, credential assignments,
credential-bearing URLs), strict UTF-8 without NUL, and a closed extraction
class per source. Any match or anything unclassifiable excludes the whole file;
only its hash, path, policy id/version and detector id are retained. Raw bodies
are never stored, logged, rendered, returned or sent anywhere.

**3. Observer registry entry** — `{REGISTRY.as_posix()}`
SHA-256 `{registry_sha}`

The governance-plane entry for the observer `polaris-butlers-project-shape`.
Read-only authority: phase A reads only `about/README.md`, the pillar README
indexes it names and Git tree metadata; phase B reads only the exact Git
objects in the resulting revision-bound manifest. Empty write surface, no
database access, no network access, no observed-code execution, no
working-tree reads, fixed resource limits. The implementation path it names
does not exist yet; adopting the entry authorizes no implementation.

## What this does and does not do

- All three acts together satisfy PWB-REQ-005's authority precondition in
  state (1). They are warrants, not evidence that any read, screening or
  derived claim succeeded.
- They do **not** authorize PWB implementation (task 1.8 is a separate act),
  any write, egress, execution, deployment, release, recovery, mission, a
  second repository, autonomous behavior or multi-user support.
- Nothing reads Butlers as a result of these acts. A read can only happen once
  an authorized implementation evaluates all three acts and finds them valid.
- Each act is recorded in `.syzygy/governance/decisions/` and appended to
  `ACCEPTANCE-ACT-RECORD.md`, with a tag on the recording commit. Editing any
  of the three files afterwards breaks its act; changes go through a new act.

## Evidence

- Fresh-context security and authority-boundary review at this exact commit
  and manifest: `{SECURITY_REVIEW.as_posix()}`, verdict `CONFIRM`,
  sha256 `{review_sha}`.
- The manifest generator reproduces this closed three-row population and
  mutation-proves byte and path drift (`--selftest`).

## Exact owner responses

Each line is one act. Write exactly the line(s) you intend, and nothing else
on that line. State (1) is selected by performing the phrase; the recorder
writes the A1 audit-record identity as absent.

{phrase_block}
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

    original = (ROOT / POLICY).read_bytes()
    mutated = render(overrides={POLICY: original + b"\n"})
    if mutated == first:
        print("SELFTEST FAILED: subject-byte mutation did not change manifest")
        return 1
    before_rows = dict((path, sha) for sha, path in ROW_RE.findall(first))
    after_rows = dict((path, sha) for sha, path in ROW_RE.findall(mutated))
    changed = [path for path in before_rows if before_rows[path] != after_rows[path]]
    if changed != [POLICY.as_posix()]:
        print(f"SELFTEST FAILED: mutation changed wrong rows: {changed}")
        return 1
    if phrases({**subject_bytes(ROOT), POLICY: original + b"\n"})[1][2] == phrases(subject_bytes(ROOT))[1][2]:
        print("SELFTEST FAILED: policy mutation did not change the policy phrase")
        return 1

    malformed = first.replace(f"  {SUBJECTS[0].as_posix()}\n", "  missing.md\n", 1)
    if not verify(malformed):
        print("SELFTEST FAILED: path mutation was not rejected")
        return 1
    digest_drift = first.replace(before_rows[POLICY.as_posix()], "0" * 64, 1)
    if not verify(digest_drift):
        print("SELFTEST FAILED: digest mutation was not rejected")
        return 1
    dropped = "\n".join(
        line for line in first.splitlines() if not line.endswith(REGISTRY.as_posix())
    ) + "\n"
    if not verify(dropped):
        print("SELFTEST FAILED: dropped row was not rejected")
        return 1
    stray = first + "not a row\n"
    if not verify(stray):
        print("SELFTEST FAILED: stray line was not rejected")
        return 1

    good_review = (
        "- [Observed] Reviewed commit:\n  `" + "a" * 40 + "`.\n"
        "- [Observed] Manifest SHA-256:\n  `" + "b" * 64 + "`.\n"
        "**VERDICT: CONFIRM**\n"
    )
    if not review_binds_exact(good_review, "a" * 40, "b" * 64):
        print("SELFTEST FAILED: well-bound CONFIRM review was rejected")
        return 1
    if review_binds_exact(good_review.replace("CONFIRM", "REVISE"), "a" * 40, "b" * 64):
        print("SELFTEST FAILED: REVISE review was accepted")
        return 1
    if review_binds_exact(good_review, "c" * 40, "b" * 64):
        print("SELFTEST FAILED: review bound to a different commit was accepted")
        return 1
    print("SELFTEST OK: 3 rows; byte, digest, path, dropped-row, stray-line and review-binding mutations rejected")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify the committed manifest")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--phrases", action="store_true", help="print the three exact phrases for the current bytes")
    parser.add_argument("--finalize", metavar="COMMIT", help="write CANDIDATE-REPORT.md and OWNER-SIGNOFF-PACKET.md for the frozen commit")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    if args.phrases:
        for act_type, rel, phrase in phrases(subject_bytes(ROOT)):
            print(f"{act_type:22} {rel.as_posix()}\n  {phrase}")
        return 0
    if args.finalize:
        try:
            outputs = finalized_outputs(ROOT, args.finalize)
        except ValueError as exc:
            print(f"FINALIZE FAILED: {exc}")
            return 1
        for rel, text in outputs.items():
            (ROOT / rel).write_text(text)
            print(f"wrote {rel.as_posix()}")
        return 0
    rendered = render()
    if args.check:
        target = ROOT / OUT
        if not target.is_file():
            print(f"CHECK FAILED: missing {OUT}")
            return 1
        current = target.read_text()
        findings = verify(current)
        if current != rendered:
            findings.append("committed manifest differs from exact regeneration")
        if findings:
            for finding in findings:
                print(f"CHECK FAILED: {finding}")
            return 1
        print(f"CHECK OK: {len(SUBJECTS)} rows verified; {OUT.as_posix()} matches regeneration")
        return 0
    (ROOT / OUT).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / OUT).write_text(rendered)
    print(f"wrote {OUT.as_posix()} ({len(SUBJECTS)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
