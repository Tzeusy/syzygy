#!/usr/bin/env python3
"""Simulate the screening-scope act on a scratch clone and list what breaks.

Package `contracts/candidates/public-source-screening-scope/` (`syzygy-mea`).
Performs no owner act, writes no act record and edits no tracked file of this
checkout. It answers one question, reproducibly: if the policy were replaced by
the proposed bytes, which checks, tools and pins would stop agreeing with the
tree? The packet's Q2 continuation and the impact ledger's pin table are written
from this output, not from reading.

Steps, all in a `git clone --shared` scratch copy of HEAD (a clean tree is
required, so the simulation measures committed bytes):

  1. replace the policy with the proposed bytes (the builder's `propose`) and
     commit them;
  2. sweep tracked files for the literals the old policy carries (its SHA-256
     and its version) and group the hits;
  3. run the re-pin builder and recorder `--check`s, `check_governance.py`, and
     with `--tests` the Three-Surface POC tests that assert the policy, after
     `npm ci` in the clone (a fresh clone must not resolve `@syzygy/*` to
     another checkout's `node_modules`);
  4. print each failing command with its first failure lines, and the hit table.

  --json    machine output
  --tests   also run the Vitest files that assert the policy (slow; needs npm)
  --keep    leave the scratch clone and print its path
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
sys.path.insert(0, str(ROOT / "scripts"))
import build_public_source_screening_scope as build  # noqa: E402

REPIN_POLICY_ARG = "policy"
TEST_FILES = (
    "apps/three-surface-poc/src/governance-inputs.test.ts",
    "packages/three-surface-poc-core/src/content-classification.test.ts",
    "packages/three-surface-poc-core/src/git-object-reader.test.ts",
    "packages/three-surface-poc-core/src/project-shape-model.test.ts",
)
#: Prefixes whose hits are tools, runtime or tests that must move with the act;
#: every other hit is a governance record that cites the old bytes and binds.
PIN_PREFIXES = ("apps/", "packages/", "scripts/", ".github/", "PROJECT-STATUS.md")


def run(argv, cwd, timeout=900):
    done = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return done.returncode, (done.stdout + done.stderr)


def tracked(cwd):
    out = subprocess.run(["git", "ls-files", "-z"], cwd=cwd, capture_output=True, check=True).stdout
    return [p for p in out.decode().split("\0") if p]


def sweep(cwd, literals):
    hits = {}
    for rel in tracked(cwd):
        try:
            text = (pathlib.Path(cwd) / rel).read_text(errors="strict")
        except (UnicodeDecodeError, OSError):
            continue
        for name, lit in literals.items():
            n = text.count(lit)
            if n:
                hits.setdefault(rel, {})[name] = n
    return hits


def first_failures(output, limit=6):
    keep = [l.strip() for l in output.splitlines()
            if re.search(r"FAIL|Error|error|differs|not the|mismatch|stale|hashes to|AssertionError", l)]
    return keep[:limit]


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--tests", action="store_true")
    ap.add_argument("--keep", action="store_true")
    args = ap.parse_args(argv[1:])
    if subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout.strip():
        print("refusing: the tree is not clean; commit first", file=sys.stderr)
        return 2
    base_text = (ROOT / build.POLICY).read_text()
    old_version = json.loads(base_text)["policyVersion"]
    old_digest = hashlib.sha256(base_text.encode()).hexdigest()
    proposed = build.propose(base_text)
    tmp = tempfile.mkdtemp(prefix="screening-scope-sim-")
    clone = pathlib.Path(tmp) / "clone"
    subprocess.run(["git", "clone", "-q", "--shared", str(ROOT), str(clone)], check=True)
    (clone / build.POLICY).write_text(proposed)
    subprocess.run(["git", "-c", "user.name=sim", "-c", "user.email=sim@example.invalid",
                    "commit", "-qam", "simulated act: proposed policy bytes"], cwd=clone, check=True)

    literals = {"old-policy-digest": old_digest, "old-policy-version": old_version}
    # The performed act's identity, recording tag and record pointers, read from
    # the gate's own pin file: a new act supersedes them whatever the version says.
    gate = (ROOT / "apps/three-surface-poc/src/governance-inputs.ts").read_text()
    block = re.search(r"\n      policy: \{(.*?)\n      \},", gate, re.S)
    if block:
        for key in ("actIdentity", "recordingTag"):
            m = re.search(key + r": '([^']+)'", block.group(1))
            if m:
                literals[f"performed-act {key}"] = m.group(1)
    for m in re.finditer(r"policy: '(\.syzygy/governance/decisions/[^']+)'", gate):
        literals[f"act record pointer {pathlib.Path(m.group(1)).name}"] = m.group(1)
    hits = sweep(clone, literals)
    commands = [
        ("repin builder --check", ["python3", "scripts/build_pwb_behavior_contract_repin.py", "--check"]),
        ("repin recorder --check policy", ["python3", "scripts/record_pwb_behavior_contract_repin_acts.py",
                                           "--check", REPIN_POLICY_ARG, old_digest, "--date", "2026-10-02"]),
        ("check_governance", ["python3", "scripts/check_governance.py"]),
    ]
    results = []
    for name, argv_ in commands:
        code, out = run(argv_, clone)
        failing = code != 0 or re.search(r"^FAIL ", out, re.M) is not None
        results.append({"command": name, "exit": code, "failed": bool(failing),
                        "lines": first_failures(out) if failing else []})
    if args.tests:
        code, out = run(["npm", "ci", "--no-audit", "--no-fund"], clone, 1800)
        results.append({"command": "npm ci (scratch clone)", "exit": code, "failed": code != 0,
                        "lines": first_failures(out) if code else []})
        if code == 0:
            for rel in TEST_FILES:
                code, out = run(["npx", "vitest", "run", rel], clone, 1800)
                results.append({"command": f"vitest {rel}", "exit": code, "failed": code != 0,
                                "lines": first_failures(out) if code else []})
    pins = {rel: v for rel, v in hits.items() if rel.startswith(PIN_PREFIXES)}
    records = {rel: v for rel, v in hits.items() if not rel.startswith(PIN_PREFIXES)}
    report = {"oldVersion": old_version, "newVersion": json.loads(proposed)["policyVersion"],
              "tracked": len(tracked(clone)), "results": results, "pinHits": pins,
              "recordHits": sorted(records), "recordHitCount": len(records),
              "scratch": str(clone) if args.keep else None}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"policy {old_version} -> {report['newVersion']}; {report['tracked']} tracked files")
        for r in results:
            print(("FAIL " if r["failed"] else "ok   ") + r["command"])
            for l in r["lines"]:
                print("       " + l[:160])
        print("pins (tools, runtime, tests, workflow, status battery):")
        for rel, v in sorted(pins.items()):
            print(f"  {rel}  {v}")
        print(f"records citing the old bytes (bind; not edited): {report['recordHitCount']} files")
    if not args.keep:
        subprocess.run(["rm", "-rf", tmp])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
