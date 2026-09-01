#!/usr/bin/env python3
"""Build the exact-digest generalized trusted-bootstrap transaction."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import shutil
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
TX_REL = pathlib.Path(
    ".syzygy/governance/contracts/candidates/"
    "general-trusted-bootstrap-authorization"
)
CONTRACT_MANIFEST_REL = TX_REL / "CONTRACT-AMENDMENT-MANIFEST.txt"
PWB_MANIFEST_REL = TX_REL / "PWB-COVERAGE-AMENDMENT-MANIFEST.txt"
ACT_SEMANTICS_REL = TX_REL / "ACT-SEMANTICS.md"
TRANSACTION_MANIFEST_REL = TX_REL / "TRANSACTION-MANIFEST.txt"
IMPACT_LEDGER_REL = TX_REL / "IMPACT-LEDGER.md"

CAP1_COVERAGE_REL = pathlib.Path(
    "openspec/changes/project-registration-and-honest-shape-visibility/"
    "CONTRACT-COVERAGE.md"
)
POC_COVERAGE_REL = pathlib.Path(
    "openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md"
)
SPEC_POLICY_REL = pathlib.Path(
    ".syzygy/governance/contracts/candidates/policy-candidates/"
    "SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md"
)
PWB_COVERAGE_RELS = (
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "CONTRACT-COVERAGE.md"
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "CONTRACT-COVERAGE-REPAIR-DELTA.md"
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "contract-coverage-matrix/RFC-0001-0003.md"
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "contract-coverage-matrix/RFC-0004-0006.md"
    ),
    pathlib.Path(
        "openspec/changes/polaris-project-wide-butlers-model/"
        "contract-coverage-matrix/RFC-0007-0009.md"
    ),
)
EXPECTED_ACCEPTED_MODULES = 30
ACT_REL = pathlib.Path(
    ".syzygy/governance/decisions/"
    "GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md"
)
AGGREGATE_ACT_REL = pathlib.Path(
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
)
ACT_LABEL = "SIGN OFF GENERAL TRUSTED-BOOTSTRAP AUTHORIZATION TRANSACTION"
PRODUCTION_PERFORMED_DIGEST = (
    "1885a323c659364f98e81cdf04479cebfecf5b22d350928d046ebb5b7c5268f6"
)
ACT_PATTERN = re.compile(
    r"^" + re.escape(ACT_LABEL) + r": ([0-9a-f]{64})$", re.M
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_bytes(root: pathlib.Path, rel: pathlib.Path) -> bytes:
    target = root / rel
    if not target.is_file():
        raise ValueError(f"required transaction subject missing: {rel}")
    return target.read_bytes()


def record_digest(root: pathlib.Path, rel: pathlib.Path) -> str | None:
    record = root / rel
    if not record.is_file():
        return None
    matches = ACT_PATTERN.findall(record.read_text())
    if not matches:
        return None
    if len(set(matches)) != 1:
        raise ValueError(f"{rel}: conflicting performed transaction digests")
    return matches[-1]


def performed_digest(
    root: pathlib.Path, *, allow_pre_act: bool = False
) -> str | None:
    dedicated = record_digest(root, ACT_REL)
    aggregate = record_digest(root, AGGREGATE_ACT_REL)
    if dedicated is None and aggregate is None:
        if allow_pre_act:
            return None
        raise ValueError(
            "production performed-state pin requires both act records; "
            "neither performed signal is present"
        )
    if dedicated is None or aggregate is None:
        missing = ACT_REL if dedicated is None else AGGREGATE_ACT_REL
        raise ValueError(
            f"conflicting post-act state: performed signal missing from {missing}"
        )
    if dedicated != aggregate:
        raise ValueError(
            f"conflicting performed digests: {ACT_REL}={dedicated}, "
            f"{AGGREGATE_ACT_REL}={aggregate}"
        )
    if dedicated != PRODUCTION_PERFORMED_DIGEST:
        raise ValueError(
            f"performed records agree on {dedicated}, but production is "
            f"irreversibly pinned to {PRODUCTION_PERFORMED_DIGEST}"
        )
    return PRODUCTION_PERFORMED_DIGEST


def manifest_text(title: str, notes: tuple[str, ...], rows: list[tuple[str, str]]) -> str:
    lines = [f"# {title}"]
    lines.extend(f"# {note}" for note in notes)
    lines.extend(f"{digest}  {path}" for path, digest in rows)
    return "\n".join(lines) + "\n"


def contract_manifest(root: pathlib.Path) -> str:
    accepted_root = root / ".syzygy/governance/contracts"
    candidate_root = accepted_root / "candidates"
    accepted_files = sorted((accepted_root / "rfcs").rglob("*.md"))
    if len(accepted_files) != EXPECTED_ACCEPTED_MODULES:
        raise ValueError(
            "accepted RFC 0001-0009 population changed: "
            f"{len(accepted_files)} != {EXPECTED_ACCEPTED_MODULES}"
        )
    rows = []
    for accepted in accepted_files:
        rel = accepted.relative_to(accepted_root)
        mirror = candidate_root / rel
        if not mirror.is_file():
            raise ValueError(f"candidate mirror missing: {mirror.relative_to(root)}")
        accepted_bytes = accepted.read_bytes()
        if accepted_bytes != mirror.read_bytes():
            raise ValueError(f"accepted/candidate bytes differ: {rel}")
        rows.append((rel.as_posix(), sha256_bytes(accepted_bytes)))
    return manifest_text(
        "GENERAL-TRUSTED-BOOTSTRAP CONTRACT AMENDMENT MANIFEST",
        (
            f"{len(rows)} accepted RFC 0001-0009 modules; rows sorted by codepoint path.",
            "Paths are relative to .syzygy/governance/contracts/.",
            "Installed and candidate-mirror bytes are required to match exactly.",
            "This amendment manifest never rewrites historical Wave A/B act arguments.",
        ),
        rows,
    )


def pwb_manifest(root: pathlib.Path) -> str:
    rows = [
        (rel.as_posix(), sha256_bytes(read_bytes(root, rel)))
        for rel in sorted(PWB_COVERAGE_RELS)
    ]
    return manifest_text(
        "PWB CONTRACT-COVERAGE AMENDMENT MANIFEST",
        (
            f"{len(rows)} signed coverage artifacts; rows sorted by codepoint path.",
            "The behavioral specification, proposal and design are not changed by this manifest.",
        ),
        rows,
    )


def act_semantics(
    contract_manifest_sha: str,
    cap1_coverage_sha: str,
    poc_coverage_sha: str,
    pwb_manifest_sha: str,
    spec_policy_sha: str,
) -> str:
    return f"""# General trusted-bootstrap authorization act semantics

> **Candidate — binds nothing.** The transaction manifest binds this file's
> exact digest. The owner ceremony supplies the act instant and performs the
> five rows together.

Project identity for every act: `project:syzygy`

Owner attribution for every act: Tzeusy

Provenance state at the ceremony: `owner-adopted (bootstrap, uncorrelated)`;
RFC3-16(b) item 9 records the A1 audit identity as explicitly absent. This is
an effective owner act only if the human owner performs the exact ceremony.

| # | Act type | Stable subject identity | Exact digest(s) | Scope | Supersession / revocation |
|---|---|---|---|---|---|
| 1 | `accept-contract-amendment` | accepted RFC 0001-0009 contract set | contract-amendment manifest `{contract_manifest_sha}` | Accept the generalized effective-owner-act model: valid state (1) and state (2) acts may satisfy existing owner gates, exact state always renders, invalid acts fail closed, and acts remain warrants rather than evidence | Supersedes the current bytes accepted through the historical Wave A/B acts; those acts, manifests and prior bytes remain immutable historical evidence |
| 2 | `sign-off-coverage-amendment` | Capability 1 change `project-registration-and-honest-shape-visibility`, `CONTRACT-COVERAGE.md` only | `{cap1_coverage_sha}` | Reconcile contract traceability to the amended RFC3-16 model; change no requirement, proposal, design or implementation authorization | Supersedes only that artifact's digest in the 2026-08-20 adoption; all other adopted digests remain |
| 3 | `sign-off-coverage-amendment` | signed change `three-surface-poc-experience`, `CONTRACT-COVERAGE.md` only | `{poc_coverage_sha}` | Reconcile contract traceability to the amended RFC3-16 model; change no POC requirement, scope or implementation authority | Supersedes only that artifact's digest in the 2026-08-30 sign-off; all other signed digests remain |
| 4 | `sign-off-coverage-amendment` | signed change `polaris-project-wide-butlers-model`, contract-coverage bundle | PWB coverage manifest `{pwb_manifest_sha}` | Reconcile five signed coverage artifacts while leaving PWB-REQ-005 and PWB-REQ-022 deliberately stricter at state (2); change no requirement, proposal, design or implementation authority | Supersedes only the five artifact digests listed by the PWB coverage manifest; every other 2026-08-31 sign-off digest remains |
| 5 | `confirm-craft-amendment` | in-force policy `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1..11) | `{spec_policy_sha}` | Amend CC-SPEC-8's reviewed-N/A owner-act gate to accept valid state (1) or state (2), render the exact state, and fail closed on absent or invalid acts; no other craft obligation changes | Supersedes the policy digest confirmed by craft act 6; that performed act, digest and prior bytes remain immutable historical evidence |

The five rows are one same-logical-change transaction under CC-REV-2. A
partial ceremony performs none of them. Editing any subject, manifest or this
mapping retires the offering and requires fresh exact-byte review.

Apart from row 5's CC-SPEC craft amendment, this transaction performs no
effect-specific consent or policy approval, registry adoption, write, egress,
execution, deployment, release, recovery or mission act. It
does not accept RFC 0010 or RFC 0011, sign Mission Control behavior, amend
doctrine, implement PWB, or authorize observation of a repository body.
"""


def transaction_manifest(
    outputs: dict[pathlib.Path, str], root: pathlib.Path
) -> str:
    subjects = (
        ACT_SEMANTICS_REL,
        IMPACT_LEDGER_REL,
        CONTRACT_MANIFEST_REL,
        PWB_MANIFEST_REL,
        CAP1_COVERAGE_REL,
        POC_COVERAGE_REL,
        SPEC_POLICY_REL,
    )
    rows = []
    for rel in subjects:
        if rel in outputs:
            data = outputs[rel].encode()
        else:
            data = read_bytes(root, rel)
        rows.append((rel.as_posix(), sha256_bytes(data)))
    return manifest_text(
        "GENERAL-TRUSTED-BOOTSTRAP AUTHORIZATION TRANSACTION MANIFEST",
        (
            f"{len(rows)} bound subjects; order is protocol-defined, not inferred.",
            "This file's own sha256 is the sole argument of the owner ceremony.",
            "A changed subject, row, order or digest retires the offering.",
        ),
        rows,
    )


def build_outputs(root: pathlib.Path) -> dict[pathlib.Path, str]:
    contract_text = contract_manifest(root)
    pwb_text = pwb_manifest(root)
    cap1_sha = sha256_bytes(read_bytes(root, CAP1_COVERAGE_REL))
    poc_sha = sha256_bytes(read_bytes(root, POC_COVERAGE_REL))
    spec_policy_sha = sha256_bytes(read_bytes(root, SPEC_POLICY_REL))
    act_text = act_semantics(
        sha256_bytes(contract_text.encode()),
        cap1_sha,
        poc_sha,
        sha256_bytes(pwb_text.encode()),
        spec_policy_sha,
    )
    outputs = {
        CONTRACT_MANIFEST_REL: contract_text,
        PWB_MANIFEST_REL: pwb_text,
        ACT_SEMANTICS_REL: act_text,
    }
    outputs[TRANSACTION_MANIFEST_REL] = transaction_manifest(outputs, root)
    return outputs


def run(
    check: bool, root: pathlib.Path = ROOT, *, allow_pre_act: bool = False
) -> int:
    try:
        frozen = performed_digest(root, allow_pre_act=allow_pre_act)
        outputs = build_outputs(root)
    except ValueError as exc:
        print(f"DRIFT: {exc}")
        return 1
    drift = []
    for rel, content in outputs.items():
        target = root / rel
        if not target.is_file() or target.read_bytes() != content.encode():
            drift.append(rel)
    act_drift = None
    if frozen is not None:
        target = root / TRANSACTION_MANIFEST_REL
        if not target.is_file():
            act_drift = f"performed transaction subject missing: {TRANSACTION_MANIFEST_REL}"
        else:
            actual = sha256_bytes(target.read_bytes())
            if actual != frozen:
                act_drift = (
                    f"performed transaction digest {frozen} != current manifest "
                    f"{actual}"
                )
        if drift or act_drift:
            if act_drift:
                print(f"DRIFT: {act_drift}")
            for rel in drift:
                print(f"DRIFT: immutable performed subject {rel}")
            return 1
        if check:
            print(
                "performed general trusted-bootstrap transaction frozen and "
                f"current — {EXPECTED_ACCEPTED_MODULES} contract modules, "
                f"{len(PWB_COVERAGE_RELS) + 2} signed coverage artifacts, "
                "5 owner-act rows"
            )
        else:
            print(
                "immutable performed transaction unchanged — rewrite refused; "
                "all generated subjects remain exact"
            )
        return 0

    if check:
        if drift:
            for rel in drift:
                print(f"DRIFT: {rel}")
            return 1
        print(
            "general trusted-bootstrap transaction current — "
            f"{EXPECTED_ACCEPTED_MODULES} contract modules, "
            f"{len(PWB_COVERAGE_RELS) + 2} signed coverage artifacts, "
            "5 owner-act rows"
        )
        return 0
    for rel in drift:
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(outputs[rel])
    for rel in outputs:
        state = "rewrote" if rel in drift else "unchanged"
        print(f"{state}  {rel}  sha256 {sha256_bytes(outputs[rel].encode())}")
    return 0


def selftest() -> int:
    baseline = build_outputs(ROOT)
    with tempfile.TemporaryDirectory(prefix="general-bootstrap-tx-") as temp:
        clone = pathlib.Path(temp)
        for rel in (
            pathlib.Path(".syzygy/governance/contracts/rfcs"),
            pathlib.Path(".syzygy/governance/contracts/candidates/rfcs"),
        ):
            shutil.copytree(ROOT / rel, clone / rel)
        for rel in (
            IMPACT_LEDGER_REL,
            CAP1_COVERAGE_REL,
            POC_COVERAGE_REL,
            SPEC_POLICY_REL,
            *PWB_COVERAGE_RELS,
        ):
            target = clone / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)

        mirror = clone / (
            ".syzygy/governance/contracts/candidates/rfcs/"
            "RFC-0002/challenge-lifecycle.md"
        )
        mirror.write_text(mirror.read_text() + "\nmirror mutation\n")
        try:
            build_outputs(clone)
            parity_fails = False
        except ValueError as exc:
            parity_fails = "accepted/candidate bytes differ" in str(exc)
        print(f"{'PASS' if parity_fails else 'FAIL'} mirror divergence rejected")

        shutil.copy2(
            ROOT
            / ".syzygy/governance/contracts/candidates/rfcs/RFC-0002/challenge-lifecycle.md",
            mirror,
        )
        cap1 = clone / CAP1_COVERAGE_REL
        cap1.write_text(cap1.read_text() + "\ncoverage mutation\n")
        changed = build_outputs(clone)
        digest_changes = (
            changed[TRANSACTION_MANIFEST_REL]
            != baseline[TRANSACTION_MANIFEST_REL]
            and changed[ACT_SEMANTICS_REL] != baseline[ACT_SEMANTICS_REL]
        )
        print(f"{'PASS' if digest_changes else 'FAIL'} subject mutation changes act and transaction")

        shutil.copy2(ROOT / CAP1_COVERAGE_REL, cap1)
        for rel, content in baseline.items():
            target = clone / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
        for rel in (ACT_REL, AGGREGATE_ACT_REL):
            record = clone / rel
            record.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, record)

        frozen_before = {
            rel: (clone / rel).read_bytes() for rel in baseline
        }
        clean_noop = run(False, clone) == 0
        clean_unchanged = all(
            (clone / rel).read_bytes() == content
            for rel, content in frozen_before.items()
        )
        print(
            f"{'PASS' if clean_noop and clean_unchanged else 'FAIL'} "
            "performed clean write mode is a no-op success"
        )

        (clone / ACT_REL).unlink()
        missing_dedicated = run(False, clone) == 1
        missing_dedicated_unchanged = all(
            (clone / rel).read_bytes() == content
            for rel, content in frozen_before.items()
        )
        print(
            f"{'PASS' if missing_dedicated and missing_dedicated_unchanged else 'FAIL'} "
            "missing dedicated act record refuses rewrite"
        )
        shutil.copy2(ROOT / ACT_REL, clone / ACT_REL)

        (clone / AGGREGATE_ACT_REL).unlink()
        missing_aggregate = run(False, clone) == 1
        missing_aggregate_unchanged = all(
            (clone / rel).read_bytes() == content
            for rel, content in frozen_before.items()
        )
        print(
            f"{'PASS' if missing_aggregate and missing_aggregate_unchanged else 'FAIL'} "
            "missing aggregate act record refuses rewrite"
        )
        shutil.copy2(ROOT / AGGREGATE_ACT_REL, clone / AGGREGATE_ACT_REL)

        (clone / ACT_REL).unlink()
        (clone / AGGREGATE_ACT_REL).unlink()
        both_absent = run(False, clone) == 1
        both_absent_unchanged = all(
            (clone / rel).read_bytes() == content
            for rel, content in frozen_before.items()
        )
        print(
            f"{'PASS' if both_absent and both_absent_unchanged else 'FAIL'} "
            "both absent act records refuse production rewrite"
        )
        shutil.copy2(ROOT / ACT_REL, clone / ACT_REL)
        shutil.copy2(ROOT / AGGREGATE_ACT_REL, clone / AGGREGATE_ACT_REL)

        semantics = clone / ACT_SEMANTICS_REL
        crlf = semantics.read_bytes().replace(b"\n", b"\r\n")
        semantics.write_bytes(crlf)
        crlf_refused = run(False, clone) == 1
        crlf_unchanged = semantics.read_bytes() == crlf
        print(
            f"{'PASS' if crlf_refused and crlf_unchanged else 'FAIL'} "
            "CRLF generated-subject drift rejected byte-exactly"
        )
        for rel, content in baseline.items():
            (clone / rel).write_text(content)

        cap1.write_text(cap1.read_text() + "\npost-act coverage mutation\n")
        frozen_before_drift = {
            rel: (clone / rel).read_bytes() for rel in baseline
        }
        rewrite_refused = run(False, clone) == 1
        drift_unchanged = all(
            (clone / rel).read_bytes() == content
            for rel, content in frozen_before_drift.items()
        )
        print(
            f"{'PASS' if rewrite_refused and drift_unchanged else 'FAIL'} "
            "performed drift rejected without rewriting bound outputs"
        )
    passed = (
        parity_fails and digest_changes and clean_noop and clean_unchanged
        and missing_dedicated and missing_dedicated_unchanged
        and missing_aggregate and missing_aggregate_unchanged
        and both_absent and both_absent_unchanged
        and crlf_refused and crlf_unchanged
        and rewrite_refused and drift_unchanged
    )
    print(f"8 transaction mutations, {0 if passed else 1} failing")
    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return run(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
