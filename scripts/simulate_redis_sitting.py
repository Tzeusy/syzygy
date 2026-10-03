#!/usr/bin/env python3
"""Dry-run the "owner sits, then the Redis dossier run" flow in a scratch clone.

Candidate tooling; it performs no owner act, writes no real act record and
binds nothing. Everything it changes lives in a scratch clone of this
repository (`git clone --shared`, so the real object store is only read); the
real working tree and its refs are compared before and after and the run
fails if either moved.

Steps, in the order of the sitting packet (PR 260):

  0 merge    the heads of the candidate PRs into a scratch branch; conflicts
             are resolved mechanically where that is safe (register rows by
             union, Python by an ast-validated candidate search) and
             reported where it is not
  1 overlay  the install tooling under test (`install_redis_sitting.py` and the
             two recorders that live outside the merged branches) is copied
             from this checkout into the scratch
  2 baseline check_governance, the review-campaign partition
  3 acts     (row 6, egress version 1, is not run: version 2 replaces it) every recorder runs on a synthetic argument computed from the
             current manifest row: the screening-scope policy (PR 266), the
             provider route (`--route b`: PR 273 recorder, a synthetic freeze;
             `--route a`: PR 255 recorder) and the Git source adapter, the three
             admission consents (PR 215), the RFC5-14 amendment (PR 257), the
             egress version 2 consent (row 8) and the narrative-profile adoption (PR 256)
  4 install  `scripts/install_redis_sitting.py`, then again (idempotent) and
             with `--check`; then row 8's end: egress version 1 stays
             unperformed, and (when the dossier wiring is in the tree) a
             temporary test in the scratch has the consent reader read the one
             in-force egress record and the stage map authorise the narrative
             plus the two discovery stages
  5 end      check_governance, the partition and (with `--vitest`) the full
             test suite must all be green; the report says so in `green`

Each recorder is fed a synthetic owner argument, so a "performed" record here
proves only that the recorder accepts the bytes, never that anyone consented.
The route-B recorder refuses until its package has a confirming review, so the
scratch gets a synthetic confirming raw and a synthetic freeze (said so in the
report); nothing of that reaches the real tree.

Usage:
  python3 scripts/simulate_redis_sitting.py [--scratch DIR] [--report FILE]
                                            [--base REF] [--route a|b] [--vitest] [--keep]
  python3 scripts/simulate_redis_sitting.py --selftest

Exit status 0 when the simulation ran to the end and the end state is green;
1 when it ran but the end state is not green; 2 when the scratch could not be
built or the real tree moved.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATE = "2026-10-04"
CAND = ".syzygy/governance/contracts/candidates"
DECISIONS = ".syzygy/governance/decisions"

#: (pull request, branch) in the order the scratch merges them. Merged pull
#: requests (215, 255, 256, 257, 266, 273, 278, 284, 288, 290, 299, 326, 340)
#: are already in the base. 337 is the screen that reads the v2 policy, 334 the
#: dossier wiring (consent readers, the per-digest stage map), 260 the packet.
BRANCHES = (
    (337, "agent/screening-v2"),
    (334, "agent/dossier-wiring"),
    (260, "governance/admission-sitting-packet"),
)
ORDERING_CASE = (120, "agent/tier4-dov25")
#: A case that times out at 5000 ms on main itself (bead syzygy-8wux); reported, not counted.
KNOWN_FLAKE = "tuple-encoding.test.ts > tuple field encoding tables"
#: Tools copied from this checkout into the scratch (they may be in no merged branch yet).
OVERLAY = (
    "scripts/install_redis_sitting.py",
    "scripts/record_messages_api_route_registry_act.py",
    "scripts/record_narrative_profile_adoption.py",
)

PKG_ADMISSION = f"{CAND}/public-repo-admission"
PKG_REGISTRY = f"{CAND}/public-admission-registry-entries"
PKG_MESSAGES = f"{CAND}/provider-route-messages-api-entry"
PKG_SCOPE = f"{CAND}/public-source-screening-scope"
PKG_SCOPE_V2 = f"{CAND}/public-source-screening-scope-v2"
V2_RECORDER = "scripts/record_public_source_screening_scope_v2_act.py"
V2_VARIANTS = ("none", "manifesto", "architecture", "both")
PKG_RFC5 = f"{CAND}/rfc5-project-documentation-class"
PKG_EGRESS_V2 = f"{CAND}/public-egress-v2"
EGRESS_V2_RECORDER = "record_public_egress_v2_act.py"
EGRESS_V2_ROW = "instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md"
EGRESS_V1_RECORD = f"{DECISIONS}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md"
EGRESS_V2_RECORD = f"{DECISIONS}/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md"
PKG_PROFILE_SPEC = "openspec/changes/polaris-non-governed-narrative-profile"
POLICY = ".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"

#: Remedy text per finding code. Codes are what the steps emit; the text is the
#: exact install-change edit, so the runbook and the report cannot drift.
REMEDIES = {
    "merge-register": "PENDING-OWNER-DECISIONS.md conflicts pairwise (every branch appends a row): merge with `git merge-file --union` on real temp files, then assert the row set is the distinct union of the inputs.",
    "merge-check-governance": "scripts/check_governance.py conflicts when two packages each register a phrase or a copy: keep both registrations. `git merge-file --union` is unsafe for Python (it interleaved a parenthesis); use the ast-validated candidate search in this script, then run `check_governance.py --selftest`.",
    "merge-stale-base": "The branch is based on a stale main and conflicts in docs/README.md, the partition checker and check_governance.py: ask its owner to rebase onto main before the sitting; do not resolve by hand.",
    "merge-semantic-278": "PR 278 closes GenerationSource exclusion reasons to GENERATION_EXCLUSION_REASONS, but main's repo-corpus.ts (PR 252) builds an excluded row from `reason: string`; the merge is textually clean and `npm run build:poc` then fails (TS2322 at repo-corpus.ts:167), which fails build-output.test.ts and pipeline-demo.test.ts. Fix on PR 278 (type the helper parameter GenerationExclusionReason); the simulation applies the same one-line change in the scratch so the rest of the run is meaningful.",
    "gate-not-refusing": "The Butlers read gate should refuse the new policy bytes (digest and version) between the row-1 act and the install, and admit them after it; the named expectation did not hold.",
    "installer-refused": "scripts/install_redis_sitting.py refused: read its message; it names the record or anchor it needs and restores the tree.",
    "egress-v2": "Row 8 (egress version 2) did not rehearse: version 1 must stay unperformed, version 2's record must exist and be the act argument, and the gate must read it with the stage map giving the narrative plus the two discovery stages. The detail is in the finding.",
    "not-green": "The simulated end state is not green: the named check still fails after the install. The failing lines are in the report.",
}


# ---------------------------------------------------------------- helpers ---

def parse_conflicts(text):
    """Split merge text into plain strings and (ours, base, theirs) tuples."""
    out, lines, i, buf = [], text.split("\n"), 0, []
    while i < len(lines):
        if lines[i].startswith("<<<<<<< "):
            if buf:
                out.append("\n".join(buf) + "\n")
                buf = []
            ours, base, theirs, mode = [], [], [], "o"
            i += 1
            while not lines[i].startswith(">>>>>>> "):
                if lines[i].startswith("||||||| "):
                    mode = "b"
                elif lines[i] == "=======" and mode in ("o", "b"):
                    mode = "t"
                else:
                    {"o": ours, "b": base, "t": theirs}[mode].append(lines[i])
                i += 1
            out.append(("\n".join(ours) + ("\n" if ours else ""),
                        "\n".join(base),
                        "\n".join(theirs) + ("\n" if theirs else "")))
            i += 1
        else:
            buf.append(lines[i])
            i += 1
    if buf:
        out.append("\n".join(buf))
    return out


def resolve_python(text):
    """First per-conflict combination that parses, else (None, None).

    A choice is both sides in either order, or both sides with the next N
    shared lines duplicated between them (so a shared closing paren or loop
    body survives). Validation is `ast.parse`; semantics are the caller's job.
    """
    segs = parse_conflicts(text)
    idx = [k for k, s in enumerate(segs) if isinstance(s, tuple)]
    choices = ("ot", "to") + tuple(f"{k}_{n}" for k in ("o_tail_t", "t_tail_o")
                                   for n in (1, 2, 3, 4))

    def render(pick):
        res = []
        for k, s in enumerate(segs):
            if not isinstance(s, tuple):
                res.append(s)
                continue
            ours, _base, theirs = s
            c = pick[idx.index(k)]
            nxt = segs[k + 1] if k + 1 < len(segs) and isinstance(segs[k + 1], str) else ""
            if c == "ot":
                res.append(ours + theirs)
            elif c == "to":
                res.append(theirs + ours)
            else:
                kind, n = c.rsplit("_", 1)
                tail = "".join(line + "\n" for line in nxt.split("\n")[:int(n)])
                res.append(ours + tail + theirs if kind == "o_tail_t" else theirs + tail + ours)
        return "".join(res)

    for pick in itertools.product(choices, repeat=len(idx)):
        cand = render(pick)
        try:
            ast.parse(cand)
        except SyntaxError:
            continue
        return cand, pick
    return None, None


def manifest_rows(text):
    """`(digest, path)` rows of a manifest file; comment lines skipped."""
    rows = []
    for line in text.splitlines():
        m = re.fullmatch(r"([0-9a-f]{64})  (\S.*)", line)
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows


def row_digest(manifest_text, path_suffix):
    hits = [d for d, p in manifest_rows(manifest_text) if p.endswith(path_suffix)]
    if len(hits) != 1:
        raise ValueError(f"{len(hits)} manifest rows end with {path_suffix!r}, expected 1")
    return hits[0]


def summary_line(output):
    """The 'N OK, N WARN, N FAIL' line check_governance prints, else None."""
    for line in reversed(output.splitlines()):
        if re.match(r"\d+ OK, \d+ WARN, \d+ FAIL", line):
            return line.split(" (")[0]
    return None


def fail_blocks(output):
    """{check id: [finding lines]} for each FAIL block in check_governance output."""
    blocks, cur = {}, None
    for line in output.splitlines():
        m = re.match(r"FAIL\s+(CG-\S+)\s", line)
        if m:
            cur = blocks.setdefault(m.group(1), [])
        elif re.match(r"(OK|WARN)\s+CG-", line) or re.match(r"\d+ OK,", line):
            cur = None
        elif cur is not None and line.startswith("        ") \
                and not line.strip().startswith(("rule:", "[registered]", "[current]", "[historical]")):
            cur.append(line.strip()[:240])
    return blocks


def failing_tests(output):
    """Distinct `file > test name` strings from vitest's `FAIL  |project| ...` lines."""
    seen = []
    for line in output.splitlines():
        m = re.match(r"\s*FAIL\s+\|[^|]*\|\s+(\S+)\s+>\s+(.*)$", line)
        if m:
            item = f"{m.group(1)} > {m.group(2)}"[:200]
            if item not in seen:
                seen.append(item)
    return seen


def sha256(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


class Sim:
    def __init__(self, scratch, report_path, base, vitest):
        self.scratch = pathlib.Path(scratch)
        self.report_path = report_path
        self.base = base
        self.vitest = vitest
        self.v2_variant = "none"
        self.steps = []
        self.findings = []
        self.baseline_failing = set()
        self.green = False

    # -- plumbing
    def run(self, argv, timeout=900, check=False, cwd=None):
        p = subprocess.run(argv, cwd=cwd or self.scratch, capture_output=True,
                           text=True, timeout=timeout)
        if check and p.returncode:
            raise RuntimeError(f"{argv}: {p.stderr[-400:]}")
        return p

    def git(self, *a, check=True):
        return self.run(["git", *a], check=check)

    def commit(self, msg):
        self.git("add", "-A")
        self.git("-c", "user.name=sim", "-c", "user.email=sim@invalid",
                 "commit", "-qm", msg, "--allow-empty")

    def finding(self, step, code, evidence):
        self.findings.append({"step": step, "code": code, "evidence": evidence,
                              "remedy": REMEDIES[code]})

    def step(self, name, **info):
        self.steps.append({"step": name, **info})
        print(f"[{name}] " + "; ".join(f"{k}={v}" for k, v in info.items()), flush=True)

    def checks(self, name, with_governance=True):
        rec = {}
        if with_governance:
            p = self.run([sys.executable, "scripts/check_governance.py"], timeout=900)
            out = p.stdout + p.stderr
            rec["governance"] = summary_line(out)
            rec["failing"] = {k: len(v) for k, v in fail_blocks(out).items()}
            rec["failures"] = fail_blocks(out)
        p = self.run([sys.executable, "scripts/check_docs_review_campaign_partition.py"])
        rec["partition"] = (p.stdout.strip().splitlines() or [p.stderr.strip()])[-1][:160]
        rec["partition_exit"] = p.returncode
        self.step(name + ":checks", governance=rec.get("governance"),
                  failing=rec.get("failing"), partition=rec["partition"])
        self.steps[-1]["detail"] = rec
        return rec

    def npm_ci(self):
        """The PR 215 recorder compiles TypeScript; a fresh clone needs its own
        node_modules or `NodeNext` resolves the main checkout's (AGENTS.md)."""
        if not (self.scratch / "node_modules").exists():
            p = self.run(["npm", "ci", "--ignore-scripts"], timeout=1800)
            self.step("npm-ci", exit=p.returncode)

    def vitest_run(self, name):
        if not self.vitest:
            return
        self.npm_ci()
        p = self.run(["npx", "vitest", "run"], timeout=3000)
        out = p.stdout + p.stderr
        tail = [ln.strip() for ln in out.splitlines() if ln.strip().startswith("Tests ")]
        failing = failing_tests(out)
        if failing:
            # a case that fails under the full suite's load but passes alone is a timing flake
            # (several timed out at 5000 ms on a loaded machine); the rerun decides
            files = sorted({f.split(" > ")[0] for f in failing})
            still = []
            for f in files:   # one file per process, so the rerun is not itself loaded by the others
                q = self.run(["npx", "vitest", "run", f], timeout=1800)
                still += failing_tests(q.stdout + q.stderr)
            self.step(name + ":vitest-rerun", files=len(files), passed_on_rerun=len(failing) - len(still),
                      still_failing=still)
            failing = still
        self.step(name + ":vitest", exit=p.returncode, summary=tail[-1:], failing=failing)
        return failing

    # -- step 0
    def merge_all(self):
        merged, skipped = [], []
        for pr, branch in BRANCHES:
            ref = f"refs/sim/{branch}"
            if self.git("rev-parse", "--verify", "-q", ref, check=False).returncode:
                skipped.append((pr, "branch not found"))
                continue
            p = self.git("merge", "--no-ff", "--no-edit", "-q", ref, check=False)
            if p.returncode == 0:
                merged.append(pr)
                continue
            files = self.git("diff", "--name-only", "--diff-filter=U").stdout.split()
            ok = True
            for f in files:
                path = self.scratch / f
                if f.endswith("PENDING-OWNER-DECISIONS.md"):
                    self.union_merge(f)
                    self.finding("merge", "merge-register", f"PR {pr}: {f}")
                elif f.endswith(".py"):
                    new, pick = resolve_python(path.read_text())
                    if new is None:
                        ok = False
                        self.finding("merge", "merge-check-governance", f"PR {pr}: {f} unresolved")
                    else:
                        path.write_text(new)
                        self.finding("merge", "merge-check-governance",
                                     f"PR {pr}: {f} resolved with {list(pick)}")
                else:
                    ok = False
            if ok and files:
                self.git("add", "-A")
                self.git("-c", "user.name=sim", "-c", "user.email=sim@invalid",
                         "commit", "-qm", f"merge {branch}")
                merged.append(pr)
            else:
                self.git("merge", "--abort", check=False)
                skipped.append((pr, f"unresolved: {files}"))
        self.step("merge", merged=merged, skipped=skipped)
        # Python resolution is only trusted when the selftest still passes.
        if any(f["code"] == "merge-check-governance" for f in self.findings):
            p = self.run([sys.executable, "scripts/check_governance.py", "--selftest"], timeout=900)
            self.step("merge:selftest", exit=p.returncode, tail=(p.stdout.strip().splitlines() or [""])[-1][:160])

    def union_merge(self, rel):
        stages = {}
        for n, tag in ((1, "base"), (2, "ours"), (3, "theirs")):
            p = self.git("show", f":{n}:{rel}", check=False)
            fd = self.scratch.parent / f"{self.scratch.name}.{tag}"
            fd.write_text(p.stdout if p.returncode == 0 else "")
            stages[tag] = fd
        self.run(["git", "merge-file", "--union", str(stages["ours"]), str(stages["base"]), str(stages["theirs"])])
        (self.scratch / rel).write_text(stages["ours"].read_text())
        for fd in stages.values():
            fd.unlink()

    def merge_fixup(self):
        rel = "apps/three-surface-poc/src/polaris-generation/repo-corpus.ts"
        path = self.scratch / rel
        if not path.is_file():
            return
        text = path.read_text()
        old = "(reason: string): GenerationSource"
        if old not in text or "GenerationExclusionReason" not in (self.scratch / "packages/polaris-generation-core/src/generation-source.ts").read_text():
            return
        text = text.replace(old, "(reason: GenerationExclusionReason): GenerationSource")
        text = text.replace("import { isolatedGit }", "import type { GenerationExclusionReason } from '@syzygy/polaris-generation-core';\nimport { isolatedGit }", 1)
        path.write_text(text)
        self.commit("sim: type the excluded-row helper (PR 278 with main)")
        self.finding("merge", "merge-semantic-278", f"{rel}: reason typed as GenerationExclusionReason in the scratch")

    # -- step 1
    def overlay(self):
        copied = []
        for rel in OVERLAY:
            src = ROOT / rel
            dst = self.scratch / rel
            # the installer is the tool under test; a recorder already in the scratch (main or a
            # merged branch, possibly frozen to its confirmed package) is never overwritten
            if src.is_file() and (rel.endswith("install_redis_sitting.py") or not dst.exists()):
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src, dst)
                copied.append(rel)
        self.commit("sim: overlay the install tooling under test")
        self.step("overlay", copied=copied)

    # -- step 3
    SELECTION = ["--question-opening", "SIM opening", "--selection-label", "SIM at the manifest rows",
                 "--selection-description", "SIM synthetic selection; scratch clone only"]

    def instant(self):
        """Strictly increasing UTC instants on the act date, so chain order is defined."""
        self.clock = getattr(self, "clock", 0) + 1
        return f"{DATE}T{9 + self.clock // 60:02d}:{self.clock % 60:02d}:00Z"

    def record(self, script, key, argument, label, extra=()):
        argv = [sys.executable, f"scripts/{script}", "--record"] + ([key] if key else []) + ([argument] if argument else [])
        inst = self.instant()
        tail = ["--date", DATE, "--instant", inst, *extra]
        p = self.run(argv + tail)
        if p.returncode:
            self.step(label, record_exit=p.returncode, stderr=(p.stderr + p.stdout).strip()[-240:])
            return p
        c = self.run([sys.executable, f"scripts/{script}", "--check"] + ([key] if key else []) + ([argument] if argument else [])
                     + ["--date", DATE, *extra])
        self.step(label, record_exit=p.returncode, check_exit=c.returncode, instant=inst)
        return p

    def freeze_messages_recorder(self):
        """The route-B package has no confirming review yet; give the scratch a synthetic one."""
        rec = self.scratch / "scripts/record_messages_api_route_registry_act.py"
        pkg = self.scratch / PKG_MESSAGES
        manifest = pkg / "MESSAGES-API-ROUTE-REGISTRY-MANIFEST.txt"
        review = pkg / "reviews/R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-3-RAW.md"
        if review.is_file():   # the package has its real confirming round: nothing to simulate
            self.step("freeze-route-B", note="real confirming raw present; recorder already frozen")
            return
        review.write_text(f"# R3 (synthetic, scratch only)\nReviewed commit: {'a' * 40}\n"
                          f"Manifest SHA-256: {sha256(manifest)}\nVerdict: CONFIRM\n\n## Findings\n\nnone\n")
        files = [manifest, pkg / "OWNER-DECISION-PACKET.md", pkg / "REVIEW-BRIEF.md", pkg / "SEMANTIC-DELTA.md",
                 pkg / "IMPACT-LEDGER.md", *sorted((pkg / "proposed").glob("*.json"))]
        table = "".join(f'    pathlib.Path("{f.relative_to(self.scratch).as_posix()}"): "{sha256(f)}",\n' for f in files)
        text = rec.read_text()
        text = text.replace("FROZEN_SUBJECT: str | None = None", f'FROZEN_SUBJECT: str | None = "{"f" * 40}"')
        text = text.replace("FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {}",
                            "FROZEN_FILE_DIGESTS: dict[pathlib.Path, str] = {\n" + table + "}")
        rec.write_text(text)
        self.step("freeze-route-B", note="synthetic confirming raw and synthetic freeze, scratch only")

    def freeze_v2_recorder(self):
        """Once the recorder is frozen it is used as it stands, on the package's real round-4 raw. A
        recorder still unfrozen (an older branch) gets a synthetic confirming raw and a table from its
        own --freeze-table, in the scratch only."""
        rec = self.scratch / V2_RECORDER
        pkg = self.scratch / PKG_SCOPE_V2
        review = pkg / "reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-6-RAW.md"
        text = rec.read_text()
        if "FROZEN_SUBJECT: str | None = None" not in text:
            self.step("freeze-v2", note="recorder already frozen (the round-4 REVISE and its disclosed repairs); the real raw is used")
            return True
        review.parent.mkdir(parents=True, exist_ok=True)
        review.write_text(f"# R4 (synthetic, scratch only)\nReviewed commit: {'a' * 40}\n"
                          f"Manifest SHA-256: {sha256(pkg / 'PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt')}\n"
                          "Verdict: CONFIRM\n\n## Findings\n\nnone\n")
        p = self.run([sys.executable, V2_RECORDER, "--freeze-table"])
        if p.returncode or "FROZEN_FILE_DIGESTS" not in p.stdout:
            self.step("freeze-v2", exit=p.returncode, tail=(p.stderr + p.stdout)[-200:])
            return False
        # anchored to whole lines: the recorder's own selftest quotes both strings inside a snippet
        text, n1 = re.subn(r"^FROZEN_SUBJECT: str \| None = None$", lambda _m: f'FROZEN_SUBJECT: str | None = "{"f" * 40}"', text, count=1, flags=re.M)
        text, n2 = re.subn(r"^FROZEN_FILE_DIGESTS: dict\[pathlib\.Path, str\] = \{\}$", lambda _m: p.stdout.strip(), text, count=1, flags=re.M)
        if (n1, n2) != (1, 1):
            self.step("freeze-v2", note=f"the recorder's freeze lines were not found once each: {(n1, n2)}")
            return False
        rec.write_text(text)
        self.step("freeze-v2", note="synthetic confirming raw and synthetic freeze, scratch only")
        return True

    def v2_row(self, variant):
        text = (self.scratch / PKG_SCOPE_V2 / "PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt").read_text()
        m = re.search(rf"^([0-9a-f]{{64}})  \S+  \[variant: {variant}\]$", text, re.M)
        return m.group(1) if m else None

    def acts(self, route):
        scope = (self.scratch / PKG_SCOPE / "PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt").read_text()
        reg = (self.scratch / PKG_REGISTRY / "PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt").read_text()
        adm = (self.scratch / PKG_ADMISSION / "PUBLIC-REPO-ADMISSION-MANIFEST.txt").read_text()
        rfc = (self.scratch / PKG_RFC5 / "CONTRACT-AMENDMENT-MANIFEST.txt").read_text()
        sel = self.SELECTION
        self.record("record_public_source_screening_scope_act.py", None, row_digest(scope, "POLICY-CANDIDATE.json"), "row1-policy", sel)
        if route == "b":
            self.freeze_messages_recorder()
            msg = (self.scratch / PKG_MESSAGES / "MESSAGES-API-ROUTE-REGISTRY-MANIFEST.txt").read_text()
            self.record("record_messages_api_route_registry_act.py", None, row_digest(msg, "MESSAGES-API-CANDIDATE.json"), "row2-route-B", sel)
        else:
            self.record("record_public_admission_registry_entries_acts.py", "provider-route",
                        row_digest(reg, "AGENT-SDK-CANDIDATE.json"), "row2-route-A", sel)
        self.record("record_public_admission_registry_entries_acts.py", "git-source-acquisition",
                    row_digest(reg, "GIT-SOURCE-ACQUISITION-CANDIDATE.json"), "row3", sel)
        # Row 6 (egress version 1) is not offered at this sitting: version 2 replaces it (packet rows 6 and 8).
        for key, suffix, label in (("requests-observation", "requests/OBSERVATION-CONSENT.md", "row4"),
                                   ("redis-observation", "redis/OBSERVATION-CONSENT.md", "row5")):
            self.record("record_public_repo_admission_acts.py", key, row_digest(adm, suffix), label, sel)
        self.record("record_rfc5_project_documentation_act.py", None, row_digest(rfc, "consent-egress-secrets.md"), "row7", sel)
        egress = (self.scratch / PKG_EGRESS_V2 / "PUBLIC-EGRESS-V2-MANIFEST.txt")
        if egress.is_file():
            self.v2_argument = row_digest(egress.read_text(), EGRESS_V2_ROW)
            self.record(EGRESS_V2_RECORDER, "egress-anthropic-v2", self.v2_argument, "row8-egress-v2", sel)
        else:
            self.v2_argument = None
            self.step("row8-egress-v2", note="not run: the egress version 2 package is absent")
        if (self.scratch / V2_RECORDER).is_file() and self.v2_variant and self.freeze_v2_recorder():
            arg = self.v2_row(self.v2_variant)
            if arg is None:
                self.step("row12-policy-v2", note=f"no manifest row for variant {self.v2_variant}")
            else:
                self.record("record_public_source_screening_scope_v2_act.py", None, arg, "row12-policy-v2", sel)
        else:
            self.step("row12-policy-v2", note="not run: the package is absent or --no-v2 was given")
        self.record("record_narrative_profile_adoption.py", None, None, "row8-profile", sel)
        self.commit("sim: every recorder run")
        self.checks("after-acts")

    GATE_TEST = "apps/three-surface-poc/src/governance-inputs.test.ts"
    GATE_REAL = "evaluates the three real current PWB acts"

    def gate(self, name, expect_refusal):
        """Run the read gate's loader test on the scratch tree: before the install the pinned
        digest and version must refuse the new policy (packet Q2); after it they must admit."""
        self.npm_ci()
        p = self.run(["npx", "vitest", "run", self.GATE_TEST], timeout=900)
        failing = failing_tests(p.stdout + p.stderr)
        real = [f for f in failing if self.GATE_REAL in f]
        self.step(name, exit=p.returncode, failing=len(failing), real_tree_refused=bool(real))
        ok = bool(real) if expect_refusal else (p.returncode == 0 and not failing)
        if not ok:
            self.finding(name, "gate-not-refusing", f"expect_refusal={expect_refusal}; failing={failing[:3]}")
        return ok

    EGRESS_TEST = "apps/three-surface-poc/src/polaris-generation/sim-egress-v2.test.ts"
    EGRESS_TEST_BODY = """import { describe, expect, it } from 'vitest';

import { createPackageAdmissionReader, inForceRecords } from '@syzygy/polaris-generation-consent';

import { DISCOVERY_STAGES, EGRESS_V1_DIGEST, EGRESS_V2_DIGEST, NARRATIVE_STAGES, stagesAuthorisedBy } from './dossier-stage-authority.js';

// Written by scripts/simulate_redis_sitting.py into the scratch clone only, and removed after the run.
describe('simulated sitting: the gate reads egress version 2', () => {
  it('reads one in-force egress record, equal to the act argument, authorising discovery plus narrative', async () => {
    const root = process.env.SIM_ROOT!, argument = process.env.SIM_V2_ARGUMENT!, now = Date.parse(process.env.SIM_NOW!);
    const live = inForceRecords(await createPackageAdmissionReader({ root }).read(), now);
    const egress = live.filter(r => r.class === 'egress' && r.project === 'project:syzygy' && r.providerId === 'anthropic');
    expect(egress.length).toBe(1);
    expect(egress[0]!.digest).toBe(argument);
    expect(egress[0]!.digest).toBe(EGRESS_V2_DIGEST);
    const observed = new Set(live.filter(r => r.class === 'observation').map(r => r.repositoryId));
    expect(egress[0]!.admittedRepositories.length).toBeGreaterThan(0);
    expect(egress[0]!.admittedRepositories.some(id => observed.has(id))).toBe(true);
    expect([...stagesAuthorisedBy(egress[0]!.digest)]).toEqual([...NARRATIVE_STAGES, ...DISCOVERY_STAGES]);
    expect(live.some(r => r.digest === EGRESS_V1_DIGEST)).toBe(false);
    expect([...stagesAuthorisedBy(EGRESS_V1_DIGEST)]).toEqual([...NARRATIVE_STAGES]);
  });
});
"""

    def egress_v2(self, name):
        """Row 8 end to end: version 1 stays unperformed, the performed version 2 record is the act
        argument, and (when the wiring is in the tree) the gate reads it and the stage map gives
        the narrative plus the two discovery stages."""
        v1 = (self.scratch / EGRESS_V1_RECORD).is_file()
        v2 = (self.scratch / EGRESS_V2_RECORD).is_file()
        self.step(name + ":records", v1_performed=v1, v2_performed=v2)
        if v1 or not v2 or getattr(self, "v2_argument", None) is None:
            self.finding(name, "egress-v2", f"v1 performed={v1}, v2 performed={v2}")
            return False
        if not (self.scratch / "packages/polaris-generation-consent").is_dir() \
                or not (self.scratch / "apps/three-surface-poc/src/polaris-generation/dossier-stage-authority.ts").is_file():
            self.step(name + ":gate", note="not run: the dossier wiring (PR 334) is not in this scratch tree [Unknown]")
            return True
        self.npm_ci()
        test = self.scratch / self.EGRESS_TEST
        test.write_text(self.EGRESS_TEST_BODY)
        try:
            env = dict(os.environ, SIM_ROOT=str(self.scratch), SIM_V2_ARGUMENT=self.v2_argument, SIM_NOW=f"{DATE}T23:59:59Z")
            p = subprocess.run(["npx", "vitest", "run", self.EGRESS_TEST], cwd=self.scratch, env=env,
                               capture_output=True, text=True, timeout=900)
        finally:
            test.unlink(missing_ok=True)
        failing = failing_tests(p.stdout + p.stderr)
        self.step(name + ":gate", exit=p.returncode, failing=failing)
        if p.returncode:
            self.finding(name, "egress-v2", f"gate or stage map: {failing[:2]} {(p.stdout + p.stderr)[-300:]}")
        return p.returncode == 0

    # -- step 4
    def install(self):
        results = []
        for label, flags in (("install", []), ("install-again", []), ("install-check", ["--check"])):
            p = self.run([sys.executable, "scripts/install_redis_sitting.py", *flags])
            out = (p.stdout + p.stderr).strip()
            results.append((label, p.returncode, out.splitlines()[-1][:200] if out else ""))
            self.step(label, exit=p.returncode, tail=results[-1][2])
            if label == "install":
                if p.returncode:
                    self.finding(label, "installer-refused", out[-300:])
                    return False
                self.commit("sim: install_redis_sitting.py")
        again, check = results[1], results[2]
        if again[1] != 0 or "nothing to do" not in again[2]:
            self.finding("install-again", "not-green", f"the second run is not a no-op: {again}")
            return False
        if check[1] != 0:
            self.finding("install-check", "not-green", f"--check still reports work: {check}")
            return False
        return True

    # -- step 5
    def end(self, installed):
        rec = self.checks("end")
        green = installed
        if rec["failing"]:
            green = False
            self.finding("end", "not-green", f"failing checks: {rec['failing']}: " + "; ".join(
                f"{k}: {v[:2]}" for k, v in rec["failures"].items())[:600])
        m = re.search(r"(\d+) FAIL", rec.get("governance") or "")
        if m is None or int(m.group(1)) != 0:
            green = False
            self.finding("end", "not-green", f"check_governance summary: {rec.get('governance')}")
        if rec["partition_exit"] != 0:
            green = False
            self.finding("end", "not-green", f"partition: {rec['partition']}")
        if self.vitest:
            failing = self.vitest_run("end")
            flaky = {f for f in failing or [] if KNOWN_FLAKE in f}
            if flaky:
                self.step("end:known-flake", tests=sorted(flaky), bead="syzygy-8wux")
            beyond = sorted(set(failing or []) - self.baseline_failing - flaky)
            if beyond:
                green = False
                self.finding("end", "not-green", f"vitest: {len(beyond)} failing beyond the start-of-run baseline: {beyond[:3]}")
        self.green = green
        self.step("green", value=green)

    def ordering_case(self):
        pr, branch = ORDERING_CASE
        ref = f"refs/sim/{branch}"
        if self.git("rev-parse", "--verify", "-q", ref, check=False).returncode:
            self.step("ordering-120", note="branch not found")
            return
        self.git("stash", "-q", "--include-untracked", check=False)
        p = self.git("merge", "--no-commit", "--no-ff", "-q", ref, check=False)
        files = self.git("diff", "--name-only", "--diff-filter=U").stdout.split()
        self.git("merge", "--abort", check=False)
        self.step("ordering-120", merge_exit=p.returncode, conflicts=files)
        if files:
            self.finding("ordering-120", "merge-stale-base", f"PR {pr}: {files}")

    def write_report(self):
        pathlib.Path(self.report_path).write_text(json.dumps(
            {"candidate": True, "bindsNothing": True, "date": DATE, "green": self.green,
             "steps": self.steps, "findings": self.findings}, indent=2) + "\n")
        print(f"report: {self.report_path}  ({len(self.findings)} findings)")


# ------------------------------------------------------------------- main ---

def real_state(repo):
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    status = subprocess.run(["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True).stdout
    refs = subprocess.run(["git", "for-each-ref", "--format=%(refname) %(objectname)"], cwd=repo,
                          capture_output=True, text=True).stdout
    return head, status, dict(line.split(" ", 1) for line in refs.splitlines())


def moved(before, after):
    """(hard, refs): a moved HEAD or working tree is a failure; refs that
    moved are reported by name, because other sessions share the object store
    and fetch or push while a long run is going."""
    hard = [n for n, b, a in (("HEAD", before[0], after[0]), ("status", before[1], after[1])) if b != a]
    refs = sorted(r for r in set(before[2]) | set(after[2]) if before[2].get(r) != after[2].get(r))
    return hard, refs


def build_scratch(repo, scratch, base):
    scratch = pathlib.Path(scratch).resolve()
    if repo in scratch.parents or scratch == repo:
        raise SystemExit("refusing: the scratch directory is inside the real tree")
    if scratch.exists():
        raise SystemExit(f"refusing: {scratch} already exists")
    subprocess.run(["git", "clone", "-q", "--shared", str(repo), str(scratch)], check=True)
    run = lambda *a: subprocess.run(["git", *a], cwd=scratch, check=True, capture_output=True, text=True)
    run("fetch", "-q", str(repo), "+refs/remotes/origin/*:refs/sim/*")
    run("fetch", "-q", str(repo), f"+{base}:refs/sim/main")   # separate: a base other than origin/main would collide with the first mapping
    run("checkout", "-q", "-B", "sim", "refs/sim/main")
    return scratch


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--scratch")
    ap.add_argument("--report", default="redis-sitting-simulation.json")
    ap.add_argument("--base", default="refs/remotes/origin/main")
    ap.add_argument("--route", choices=("a", "b"), default="b")
    ap.add_argument("--vitest", action="store_true")
    ap.add_argument("--v2-variant", choices=V2_VARIANTS + ("skip",), default="none",
                    help="the screening-scope v2 variant row recorded as row 12 (skip: version 1 only)")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    before = real_state(ROOT)
    tmp = None
    if a.scratch is None:
        tmp = tempfile.mkdtemp(prefix="sitting-sim-")
        a.scratch = os.path.join(tmp, "clone")
    scratch = build_scratch(ROOT, a.scratch, a.base)
    sim = Sim(scratch, a.report, a.base, a.vitest)
    sim.v2_variant = None if a.v2_variant == "skip" else a.v2_variant
    try:
        sim.merge_all()
        sim.merge_fixup()
        sim.overlay()
        sim.npm_ci()
        sim.checks("baseline")
        sim.baseline_failing = set(sim.vitest_run("start") or [])
        sim.acts(a.route)
        refused = sim.gate("gate-before-install", True)
        installed = sim.install() and sim.gate("gate-after-install", False) and refused
        installed = sim.egress_v2("egress-v2") and installed
        sim.end(installed)
        sim.ordering_case()
    finally:
        sim.write_report()
    after = real_state(ROOT)
    hard, refs = moved(before, after)
    if refs:
        print(f"note: {len(refs)} ref(s) in the real repository moved during the run "
              f"(other sessions share it): {refs[:5]}", file=sys.stderr)
    if hard:
        print(f"FAIL: the real tree moved during the simulation: {hard}", file=sys.stderr)
        return 2
    if tmp and not a.keep:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0 if sim.green else 1


# --------------------------------------------------------------- selftest ---

def selftest():
    failures = []

    def expect(name, cond):
        if not cond:
            failures.append(name)

    conflict = ("a = 1\n<<<<<<< HEAD\nX = (\n    'one',\n=======\nY = (\n    'two',\n>>>>>>> br\n"
                ")\nz = 3\n")
    new, pick = resolve_python(conflict)
    expect("resolver finds a parsing combination", new is not None and ast.parse(new) is not None)
    expect("resolver keeps both sides", new is not None and "'one'" in new and "'two'" in new)
    bad = "<<<<<<< HEAD\ndef f(:\n=======\ndef g(:\n>>>>>>> br\n"
    expect("resolver refuses unparsable input", resolve_python(bad) == (None, None))
    expect("union of plain text is not trusted as python",
           resolve_python("<<<<<<< HEAD\nx = (\n=======\ny = (\n>>>>>>> b\n")[0] is None)

    d = "a" * 64
    e = "b" * 64
    man = f"# c\n{d}  dir/one.md\n{e}  dir/two.md\nnot a row\n"
    expect("manifest rows parse", manifest_rows(man) == [(d, "dir/one.md"), (e, "dir/two.md")])
    expect("row digest by suffix", row_digest(man, "two.md") == e)
    for suffix in ("md", "absent.md"):
        try:
            row_digest(man, suffix)
            expect(f"row digest refuses suffix {suffix}", False)
        except ValueError:
            pass

    out = ("OK    CG-1  fine\nFAIL  CG-7e  x — 2 findings\n        rule: r\n"
           "        a.md — stale\n        [registered] ok.md — fine\n        b.md — stale\n"
           "WARN  CG-8  y\n30 OK, 21 WARN, 1 FAIL (52 checks) — counts derived\n")
    expect("summary line", summary_line(out) == "30 OK, 21 WARN, 1 FAIL")
    expect("fail blocks keep findings only",
           fail_blocks(out) == {"CG-7e": ["a.md — stale", "b.md — stale"]})
    expect("no summary yields None", summary_line("nothing") is None)
    vt = ("noise\n FAIL  |@x/app| a/b.test.ts > suite > one\n FAIL  |@x/app| a/b.test.ts > suite > one\n"
          " FAIL  |@x/core| c.test.ts > two\n")
    expect("vitest failures are distinct", failing_tests(vt) == ["a/b.test.ts > suite > one", "c.test.ts > two"])
    expect("no vitest failures", failing_tests("all passed") == [])
    expect("every finding code has a remedy", all(REMEDIES[k] for k in REMEDIES))
    expect("merged pull requests are not merged again",
           not {278, 273, 326} & {pr for pr, _b in BRANCHES})
    expect("the gate test reads one in-force egress record equal to the act argument and checks the stage map",
           all(part in Sim.EGRESS_TEST_BODY for part in (
               "expect(egress.length).toBe(1)", "toBe(argument)", "toBe(EGRESS_V2_DIGEST)",
               "[...NARRATIVE_STAGES, ...DISCOVERY_STAGES]", "EGRESS_V1_DIGEST")))
    expect("row 8 is a recorded act and row 6 is not", EGRESS_V2_RECORDER.startswith("record_public_egress_v2")
           and EGRESS_V1_RECORD != EGRESS_V2_RECORD)

    # The scratch builder refuses a directory inside the real tree and the real
    # tree comparison notices a change, on a throwaway repository.
    with tempfile.TemporaryDirectory() as t:
        repo = pathlib.Path(t) / "repo"
        repo.mkdir()
        g = lambda *x: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *x],
                                      cwd=repo, check=True, capture_output=True, text=True)
        g("init", "-q")
        (repo / "f").write_text("1")
        g("add", "f")
        g("commit", "-qm", "c")
        s0 = real_state(repo)
        try:
            build_scratch(repo, repo / "inside", "HEAD")
            expect("scratch inside the real tree refused", False)
        except SystemExit:
            pass
        (repo / "f").write_text("2")
        expect("real-tree comparison notices a modified file", moved(s0, real_state(repo))[0] == ["status"])
        (repo / "f").write_text("1")
        expect("real-tree comparison is stable when restored", moved(s0, real_state(repo)) == ([], []))
        g("branch", "other")
        expect("a new ref is reported by name, not as a hard failure",
               moved(s0, real_state(repo)) == ([], ["refs/heads/other"]))

    for f in failures:
        print(f"FAIL: {f}")
    print(f"selftest: {'FAILED' if failures else 'ok'} ({len(failures)} failing)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
