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
  1 baseline check_governance, the review-campaign partition, the
             effective-scenario recount
  2 row 1    install the screening-scope policy bytes (PR 266 `propose`)
  3 rows 2-3 provider route A and the Git source adapter (PR 255 recorder)
  4 rows 4-6 the three admission consents (PR 215 recorder)
  5 row 7    the RFC5-14 amendment act (PR 257 recorder)
  6 install  register the performed records, apply the RFC-0005 patch to both
             mirrors, refresh the active-manifest row, regenerate the
             directive register
  7 narrative-profile spec install (PR 256) and the recount

Each recorder is fed a synthetic owner argument computed from the current
manifest row, so a "performed" record here proves only that the recorder
accepts the bytes, never that anyone consented. After every step the script
runs `check_governance.py` and records each FAIL line; `--vitest` also runs
the full test suite at the start and the end.

Usage:
  python3 scripts/simulate_redis_sitting.py [--scratch DIR] [--report FILE]
                                            [--base REF] [--vitest] [--keep]
  python3 scripts/simulate_redis_sitting.py --selftest

Exit status 0 when the simulation ran to the end (findings are the output,
not a failure); 2 when the scratch could not be built or the real tree moved.
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

#: (pull request, branch) in the order the scratch merges them.
BRANCHES = (
    (266, "governance/public-source-screening-scope"),
    (255, "governance/public-admission-registry-entries"),
    (273, "governance/provider-route-messages-api-entry"),
    (215, "polaris/public-repo-admission"),
    (257, "governance/rfc5-project-documentation"),
    (256, "governance/non-governed-narrative-profile"),
    (260, "governance/admission-sitting-packet"),
)
ORDERING_CASE = (120, "agent/tier4-dov25")

PKG_ADMISSION = f"{CAND}/public-repo-admission"
PKG_REGISTRY = f"{CAND}/public-admission-registry-entries"
PKG_SCOPE = f"{CAND}/public-source-screening-scope"
PKG_RFC5 = f"{CAND}/rfc5-project-documentation-class"
PKG_PROFILE_SPEC = "openspec/changes/polaris-non-governed-narrative-profile"
POLICY = ".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"

#: Performed record per act label, as the recorders write them.
PERFORMED = (
    ("CONSENT TO PUBLIC OBSERVATION OF PSF-REQUESTS", "PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md", "PUBLIC_ADMISSION_MANIFEST", "ADMISSION"),
    ("CONSENT TO PUBLIC OBSERVATION OF REDIS-REDIS", "PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md", "PUBLIC_ADMISSION_MANIFEST", "ADMISSION"),
    ("CONSENT TO PUBLIC TARGET EGRESS TO ANTHROPIC", "PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md", "PUBLIC_ADMISSION_MANIFEST", "ADMISSION"),
    ("ADOPT POLARIS PROVIDER EXECUTION ROUTE REGISTRY ENTRY", "PUBLIC-ADMISSION-REGISTRY-PROVIDER-ROUTE-ACT.md", "PUBLIC_REGISTRY_MANIFEST", "REGISTRY"),
    ("ADOPT POLARIS PUBLIC GIT SOURCE-ACQUISITION REGISTRY ENTRY", "PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-ACT.md", "PUBLIC_REGISTRY_MANIFEST", "REGISTRY"),
)

#: Remedy text per finding code. Codes are what the steps emit; the text is the
#: exact install-change edit, so the runbook and the report cannot drift.
REMEDIES = {
    "merge-register": "PENDING-OWNER-DECISIONS.md conflicts pairwise (every branch appends a row): merge with `git merge-file --union` on real temp files, then assert the row set is the distinct union of the inputs.",
    "merge-check-governance": "scripts/check_governance.py conflicts when two packages each register a phrase or a copy: keep both registrations. `git merge-file --union` is unsafe for Python (it interleaved a parenthesis); use the ast-validated candidate search in this script, then run `check_governance.py --selftest`.",
    "merge-stale-base": "The branch is based on a stale main and conflicts in docs/README.md, the partition checker and check_governance.py: ask its owner to rebase onto main before the sitting; do not resolve by hand.",
    "recorder-215-paths": "scripts/record_public_repo_admission_acts.py `live_inputs` passes `root / PKG` to `build.instances` and `build.stale`, which expect the cwd-relative PKG; every `--record` and `--check` refuses until the two calls take `PKG`. Latent bug in PR 215's recorder, not a frozen package byte: fix it in that PR's next round.",
    "policy-cg7e": "Installing the PR 266 policy bytes changes the argument of 'APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY': CG-7e reports six stale copies (re-pin manifest, aggregate record, re-pin act record x2, PROJECT-STATUS.md, screening-scope manifest unregistered) and the re-pin builder and recorder `--check` fail. PR 266's impact ledger lists them; the install change adds the superseded-argument entries, the chain link and the status-battery edits that ledger names.",
    "performed-unregistered": "Each performed record (five in this simulation) is an unregistered act-copy file. Install change: add the five records to ACT_DIGEST_COPY_FILES (and each label to the aggregate record's labels) with an existence-gated activation function.",
    "performed-manifest-heading": "Each performed record quotes `manifest SHA-256:` (the container manifest file digest); CG-7e's bare-heading check reads it as a stale act argument. Install change: add the five (record, 'manifest') pairs to BARE_DIGEST_HEADING_MANIFEST_EXEMPTIONS, as the re-pin act records already are.",
    "rfc5-cg7a-cg7h": "Applying the RFC-0005 patch to both mirrors fails CG-7a (ACTIVE-CONTRACT-MANIFEST row for RFC-0005) and CG-7h (the general-trusted-bootstrap contract manifest row). Install change: refresh the active-manifest row from the installed bytes and add a PWB_SUCCESSOR_CHAIN contract link superseding the RFC-0005 row, as the contract restyle act did; register the #257 phrase in the same change (registering earlier fails CG-7e).",
    "no-recorder": "No recorder exists for this row; its install is a byte copy and an acceptance-record entry written by hand at the sitting.",
    "policy-vitest": "Tests that pin the policy by byte equality (the content-classification and git-object-reader constants, the governance-inputs loader tests) fail once the PR 266 policy bytes are installed. The install change moves the code constants and the act-record fixtures with the policy, in the same commit; PR 266's impact ledger is the list to check against.",
    "profile-dead-refs": "Moving the narrative-profile spec from proposed/ to specs/ leaves package prose that names the proposed/ path dead (CG-1b). Those are package files, not manifest rows [Unknown: confirm against the package manifest before editing]; update the references in the install commit.",
    "recount-third-spec": "After the narrative-profile spec moves to specs/, scripts/count_polaris_effective_scenarios.py stops with 'expected exactly one base spec.md ... found 2'. The package's tasks.md names the generalization; it must land in the same change as the install.",
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
        self.steps = []
        self.findings = []

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
        self.step(name + ":vitest", exit=p.returncode, summary=tail[-1:], failing=failing)
        if any("byte-equal" in f or "governance-inputs" in f for f in failing) and name != "start":
            self.finding(name, "policy-vitest", f"{len(failing)} failing: {failing[:3]}")

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

    # -- steps 2..5
    def install_policy(self):
        sys.path.insert(0, str(self.scratch / "scripts"))
        try:
            import importlib
            build = importlib.import_module("build_public_source_screening_scope")
            base_text = (self.scratch / build.POLICY).read_text()
            (self.scratch / build.POLICY).write_text(build.propose(base_text))
        finally:
            sys.path.pop(0)
        self.commit("sim row 1: screening-scope policy bytes installed")
        rc = {}
        for script, args in (
                ("build_pwb_behavior_contract_repin.py", ["--check"]),
                ("build_public_source_screening_scope.py", ["--check"])):
            p = self.run([sys.executable, f"scripts/{script}", *args])
            rc[script] = p.returncode
        self.step("row1", repin_check_exit=rc["build_pwb_behavior_contract_repin.py"],
                  scope_check_exit=rc["build_public_source_screening_scope.py"])
        rec = self.checks("row1")
        if rec["failing"].get("CG-7e"):
            self.finding("row1", "policy-cg7e", f"CG-7e findings: {rec['failing']['CG-7e']}")

    def record(self, script, key, argument, label):
        argv = [sys.executable, f"scripts/{script}", "--record"] + ([key] if key else []) + [argument]
        tail = ["--date", DATE, "--question-opening", "SIM opening",
                "--selection-label", "SIM at the manifest rows",
                "--selection-description", "SIM synthetic selection; scratch clone only"]
        p = self.run(argv + tail)
        if p.returncode:
            return p
        c = self.run([sys.executable, f"scripts/{script}", "--check"] + ([key] if key else []) + [argument] + tail)
        self.step(label, record_exit=p.returncode, check_exit=c.returncode)
        return p

    def acts(self):
        reg = (self.scratch / PKG_REGISTRY / "PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt").read_text()
        adm = (self.scratch / PKG_ADMISSION / "PUBLIC-REPO-ADMISSION-MANIFEST.txt").read_text()
        self.step("row2-route-B", note="no recorder; byte install only")
        self.finding("row2-route-B", "no-recorder", "PR 273: route B has no recorder")
        for key, suffix, text, script, label in (
                ("provider-route", "AGENT-SDK-CANDIDATE.json", reg, "record_public_admission_registry_entries_acts.py", "row2-route-A"),
                ("git-source-acquisition", "GIT-SOURCE-ACQUISITION-CANDIDATE.json", reg, "record_public_admission_registry_entries_acts.py", "row3")):
            self.record(script, key, row_digest(text, suffix), label)
        self.commit("sim rows 2-3")
        patched = False
        for key, suffix, label in (
                ("requests-observation", "requests/OBSERVATION-CONSENT.md", "row4"),
                ("redis-observation", "redis/OBSERVATION-CONSENT.md", "row5"),
                ("egress-anthropic", "EGRESS-CONSENT-ANTHROPIC.md", "row6")):
            arg = row_digest(adm, suffix)
            p = self.record("record_public_repo_admission_acts.py", key, arg, label)
            if p.returncode and not patched:
                rec = self.scratch / "scripts/record_public_repo_admission_acts.py"
                text = rec.read_text()
                fixed = text.replace("build.instances(root / PKG)", "build.instances(PKG)") \
                            .replace("build.stale(root / PKG)", "build.stale(PKG)")
                if fixed != text:
                    rec.write_text(fixed)
                    patched = True
                    self.finding(label, "recorder-215-paths", p.stderr.strip().splitlines()[-1][:200] if p.stderr.strip() else "refused")
                    p = self.record("record_public_repo_admission_acts.py", key, arg, label)
            if p.returncode:
                self.step(label, record_exit=p.returncode, stderr=p.stderr.strip()[-200:])
        self.commit("sim rows 4-6")
        self.checks("rows2-6")
        rfc = (self.scratch / PKG_RFC5 / "CONTRACT-AMENDMENT-MANIFEST.txt").read_text()
        self.record("record_rfc5_project_documentation_act.py", None, row_digest(rfc, "consent-egress-secrets.md"), "row7")
        self.commit("sim row 7")
        self.checks("row7")
        self.vitest_run("after-acts")

    # -- step 6
    def install_change(self):
        cg = self.scratch / "scripts/check_governance.py"
        s = cg.read_text()
        add = ["\n\ndef _activate_sim_performed_registries():",
               '    """Simulated install-change registration of the performed records."""',
               '    aggregate = f"{DECISIONS}/ACCEPTANCE-ACT-RECORD.md"',
               "    for label, rel in ("]
        for label, rec, _m, _p in PERFORMED:
            add.append(f'            ({label!r}, f"{{DECISIONS}}/{rec}"),')
        add += ["    ):",
                "        if not os.path.isfile(os.path.join(ROOT, rel)):",
                "            continue",
                "        labels = ACT_DIGEST_COPY_FILES.get(aggregate, ())",
                "        if label not in labels:",
                "            ACT_DIGEST_COPY_FILES[aggregate] = labels + (label,)",
                "        ACT_DIGEST_COPY_FILES[rel] = (label,)",
                "", "", "_activate_sim_performed_registries()", ""]
        anchor = "_activate_public_admission_manifest_copy_registry()\n"
        i = s.rindex(anchor) + len(anchor)
        cg.write_text(s[:i] + "\n".join(add) + s[i:])
        self.commit("sim install: register performed records")
        rec = self.checks("install-registered")
        unreg = [f for f in rec["failures"].get("CG-7e", []) if "not in either act-copy registry" in f]
        self.finding("install", "performed-unregistered", f"{len(unreg)} unregistered before this edit (see rows2-6 checks)")
        s = cg.read_text()
        pairs = "".join(
            f'    (f"{{DECISIONS}}/{rec_}", "manifest"): {man},\n'
            for _l, rec_, man, _p in PERFORMED)
        key = '     "effect manifest"): PWB_BEHAVIOR_REPIN_MANIFEST,\n}\n'
        if s.count(key) == 1:
            cg.write_text(s.replace(key, key[:-2] + pairs + "}\n"))
        self.commit("sim install: manifest-heading exemptions")
        rec = self.checks("install-exemptions")
        self.finding("install", "performed-manifest-heading",
                     f"CG-7e findings after registration: {rec['failing'].get('CG-7e')}")
        # RFC-0005 amendment bytes on both mirrors.
        patch = self.scratch / PKG_RFC5 / "proposed/RFC-0005/consent-egress-secrets.md.patch"
        for mirror in ("rfcs", "candidates/rfcs"):
            target = f".syzygy/governance/contracts/{mirror}/RFC-0005/consent-egress-secrets.md"
            self.run(["patch", "-p0", target, "-i", str(patch)], check=True)
        self.run([sys.executable, "scripts/build_directive_register.py"])
        self.commit("sim install: RFC-0005 amendment applied to both mirrors")
        rec = self.checks("install-rfc5")
        if rec["failing"].get("CG-7a") or rec["failing"].get("CG-7h"):
            self.finding("install", "rfc5-cg7a-cg7h", f"failing: {rec['failing']}")

    def narrative_profile(self):
        src = self.scratch / PKG_PROFILE_SPEC / "proposed/polaris-generation/spec.md"
        if not src.is_file():
            self.step("profile", note="spec not present in this merge")
            return
        dst = self.scratch / PKG_PROFILE_SPEC / "specs/polaris-generation/spec.md"
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        self.commit("sim install: narrative-profile spec moved to specs/")
        p = self.run([sys.executable, "scripts/count_polaris_effective_scenarios.py", "--check"])
        out = (p.stdout + p.stderr).strip().splitlines()
        self.step("profile:recount", exit=p.returncode, tail=out[-1][:200] if out else "")
        if p.returncode:
            self.finding("profile", "recount-third-spec", out[-1][:200] if out else "")
        rec = self.checks("profile")
        if rec["failing"].get("CG-1b"):
            self.finding("profile", "profile-dead-refs", "; ".join(rec["failures"]["CG-1b"])[:300])
        self.vitest_run("end")

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
            {"candidate": True, "bindsNothing": True, "date": DATE,
             "steps": self.steps, "findings": self.findings}, indent=2) + "\n")
        print(f"report: {self.report_path}  ({len(self.findings)} findings)")


# ------------------------------------------------------------------- main ---

def real_state(repo):
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    status = subprocess.run(["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True).stdout
    refs = subprocess.run(["git", "for-each-ref", "--format=%(refname) %(objectname)"], cwd=repo,
                          capture_output=True, text=True).stdout
    return head, status, hashlib.sha256(refs.encode()).hexdigest()


def build_scratch(repo, scratch, base):
    scratch = pathlib.Path(scratch).resolve()
    if repo in scratch.parents or scratch == repo:
        raise SystemExit("refusing: the scratch directory is inside the real tree")
    if scratch.exists():
        raise SystemExit(f"refusing: {scratch} already exists")
    subprocess.run(["git", "clone", "-q", "--shared", str(repo), str(scratch)], check=True)
    run = lambda *a: subprocess.run(["git", *a], cwd=scratch, check=True, capture_output=True, text=True)
    run("fetch", "-q", str(repo), "+refs/remotes/origin/*:refs/sim/*", f"+{base}:refs/sim/main")
    run("checkout", "-q", "-B", "sim", "refs/sim/main")
    return scratch


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--scratch")
    ap.add_argument("--report", default="redis-sitting-simulation.json")
    ap.add_argument("--base", default="refs/remotes/origin/main")
    ap.add_argument("--vitest", action="store_true")
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
    try:
        sim.merge_all()
        sim.npm_ci()
        sim.checks("baseline")
        sim.vitest_run("start")
        sim.install_policy()
        sim.acts()
        sim.install_change()
        sim.narrative_profile()
        sim.ordering_case()
    finally:
        sim.write_report()
    after = real_state(ROOT)
    if before != after:
        print("FAIL: the real tree moved during the simulation", file=sys.stderr)
        return 2
    if tmp and not a.keep:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


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
        expect("real-tree comparison notices a modified file", real_state(repo) != s0)
        (repo / "f").write_text("1")
        expect("real-tree comparison is stable when restored", real_state(repo) == s0)

    for f in failures:
        print(f"FAIL: {f}")
    print(f"selftest: {'FAILED' if failures else 'ok'} ({len(failures)} failing)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
