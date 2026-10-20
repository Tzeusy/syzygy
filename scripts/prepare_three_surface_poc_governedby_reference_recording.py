#!/usr/bin/env python3
"""Read-only P115 candidate/recording preparation; never signs or installs.

Candidate checks inspect the real adopted subjects. Signed checks require the
exact actual transaction and current rows before replaying the frozen builder
in an owned full clone of its pre-signature tree. --preview is P115-only.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
KEY = "three-surface-poc-governedby-reference-amendment"
VERSION = "1.0"
CORE_COMMIT = "abd3f6ca2e8e99ad59327fdfc7b38d8bf41b07b5"
BASE = "4504514c019ca0ee0cb4a89ed97445a0bad21915"
CANDIDATE = Path(".syzygy/governance/contracts/candidates") / KEY
BUILDER = Path("scripts/build_three_surface_poc_governedby_reference_amendment.py")
COMPATIBILITY = Path("scripts/check_p115_compatibility_examples.py")
MANIFEST = CANDIDATE / "THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-MANIFEST.txt"
MANIFEST_SHA256 = "77e53d37ac42c5db4edb4f99d76d937629df5a80d370ac47751c0e62f27270bd"
RECORD = Path(".syzygy/governance/decisions/THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-SIGNOFF-v1.0.md")
AGGREGATE = Path(".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md")
MARKER = f"<!-- versioned-signoff:{KEY}:v{VERSION} -->"
CHANGE = Path("openspec/changes/three-surface-poc-experience")
SUBJECTS = tuple(CHANGE / p for p in (
    ".openspec.yaml", "CONTRACT-COVERAGE.md", "GOVERNING-DEPENDENCIES.md",
    "design.md", "proposal.md", "specs/three-surface-poc-experience/spec.md"))
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.M)


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True,
                          capture_output=True).stdout


def digest(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def core_paths(root: Path) -> list[str]:
    paths = git(root if (root / ".git").exists() else ROOT, "diff", "--name-only", "-z", BASE, CORE_COMMIT).decode().split("\0")
    paths = [p for p in paths if p]
    if not paths or any(not (p.startswith(CANDIDATE.as_posix() + "/")
                            or p in {BUILDER.as_posix(), COMPATIBILITY.as_posix()}) for p in paths):
        raise ValueError("frozen core path population is outside the P115 package and two frozen scripts")
    return paths


def core_findings(root: Path) -> list[str]:
    findings = []
    for path in core_paths(root):
        target = root / path
        expected = git(root if (root / ".git").exists() else ROOT, "show", f"{CORE_COMMIT}:{path}")
        if not target.is_file() or target.read_bytes() != expected:
            findings.append(f"frozen P115 core differs: {path}")
    return findings


def manifest_rows(root: Path) -> list[tuple[str, str]]:
    body = (root / MANIFEST).read_bytes()
    if digest(body) != MANIFEST_SHA256:
        raise ValueError("P115 manifest FILE digest differs from the frozen subject")
    rows = ROW.findall(body.decode())
    if [path for _sha, path in rows] != [p.as_posix() for p in SUBJECTS]:
        raise ValueError("P115 manifest must name exactly the six subjects in order")
    return rows


def applied_rows_match(root: Path) -> bool:
    """Recorder post-apply postcondition; this alone is NOT owner authority."""
    try:
        return all((root / path).is_file() and digest((root / path).read_bytes()) == sha
                   for sha, path in manifest_rows(root))
    except (OSError, ValueError):
        return False


def transaction_present(root: Path) -> bool:
    """A partial transaction is present too, so it cannot disappear as absent."""
    body = (root / AGGREGATE).read_text() if (root / AGGREGATE).is_file() else ""
    return (root / RECORD).exists() or MARKER in body


def builder_run(root: Path, mode: str) -> tuple[list[str], str]:
    done = subprocess.run([sys.executable, str(root / BUILDER), mode], cwd=root,
                          capture_output=True, text=True)
    output = done.stdout + done.stderr
    return ([] if done.returncode == 0 else [f"frozen P115 builder {mode} failed: {output.strip()}"]), output


def candidate_findings(root: Path) -> list[str]:
    findings = core_findings(root)
    manifest_rows(root)
    if not findings:
        problems, _output = builder_run(root, "--check")
        findings.extend(problems)
    return findings


def consumption_unknowns(root: Path) -> int:
    entries = json.loads((root / CANDIDATE / "REQUIREMENT-CONSUMPTION.json").read_text())["entries"]
    return sum(entry["classification"] == "undecidable" for entry in entries)


def recording_findings(root: Path) -> list[str]:
    """The future recorder must not bypass the packet's unresolved-impact gate."""
    findings = candidate_findings(root)
    count = consumption_unknowns(root)
    if count:
        findings.append(f"recording/offer remains gated by {count} undecidable requirement-consumption entries")
    return findings


def signed_findings(root: Path) -> list[str]:
    """Canonical record checks plus frozen review binding and exact current rows.

    This is a leaf with respect to later-row readers: P115's Package.applied
    uses only applied_rows_match, never _later_rows or this function.
    """
    findings = core_findings(root)
    count = consumption_unknowns(root)
    if count:
        findings.append(f"signed recognition remains gated by {count} undecidable requirement-consumption entries")
    if not (root / RECORD).is_file():
        return findings + ["P115 dedicated sign-off record is absent"]
    if not applied_rows_match(root):
        findings.append("P115 signed six current subjects do not match the frozen manifest")
    if findings:
        return findings
    import record_versioned_signoff as recorder
    pkg = recorder.real_packages()[KEY]
    fields = recorder.parse_record((root / RECORD).read_text())
    disposition = None if fields["Disposition"] == "none" else fields["Disposition"]
    for value in (fields["Review"], disposition):
        if value is not None and (Path(value).is_absolute() or ".." in Path(value).parts):
            return ["P115 evidence path must stay inside the repository"]
    reviewed, _verdict = recorder.validate_review(root, fields["Review"], disposition)
    recorder.review_binds(root, pkg, fields["Review"])
    # Reconciliation snapshots carry no .git. Their object source is this
    # tool's repository, but every compared file remains the snapshot's own.
    objects = root if (root / ".git").exists() else ROOT
    for path in core_paths(root):
        if git(objects, "show", f"{reviewed}:{path}") != (root / path).read_bytes():
            findings.append(f"reviewed commit does not carry the frozen P115 core: {path}")
    if findings:
        return findings
    recorder.extension_present(root, pkg)
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        code = recorder.check(root, pkg, VERSION)
    return [] if code == 0 else [output.getvalue().strip()]


def is_signed(root: Path) -> bool:
    """Only this exact valid transaction can explain earlier subject rows."""
    if not transaction_present(root):
        return False
    try:
        return not signed_findings(root)
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError):
        return False


def validation_inputs(root: Path) -> set[str]:
    """Exact additional inputs needed by reconciliation's read-only snapshots."""
    paths = set(core_paths(root)) | {RECORD.as_posix(), AGGREGATE.as_posix(),
        ".syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md",
        ".syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md"}
    if (root / RECORD).is_file():
        for name in ("Review", "Disposition"):
            values = re.findall(rf"^{name}: (.+)$", (root / RECORD).read_text(), re.M)
            if len(values) == 1 and values[0] != "none":
                path = Path(values[0])
                if path.is_absolute() or ".." in path.parts:
                    raise ValueError("P115 evidence path must stay inside the repository")
                paths.add(path.as_posix())
    return paths


def historical_run(root: Path, mode: str) -> tuple[list[str], str]:
    """Current frozen builder, exact pre-signature subjects, full Git objects.

    Unlike the older archive-only PWB selftests, this builder needs its BASE
    objects and index for its two-method sweep. The clone is disposable;
    neither the current subjects nor any registered worktree is rewritten.
    """
    findings = signed_findings(root)
    if findings:
        return findings, ""
    with tempfile.TemporaryDirectory(prefix="p115-before-signature-") as temp:
        tree = Path(temp) / "tree"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", "--no-checkout",
                        str(root), str(tree)], check=True, capture_output=True)
        git(tree, "checkout", "--quiet", "--detach", CORE_COMMIT)
        if (tree / RECORD).exists():
            return ["P115 historical core unexpectedly carries its sign-off record"], ""
        for path in core_paths(root):
            shutil.copyfile(root / path, tree / path)
            if (tree / path).read_bytes() != (root / path).read_bytes():
                return [f"historical frozen-core copy differs: {path}"], ""
        return builder_run(tree, mode)


def check_state(root: Path) -> tuple[list[str], str]:
    if transaction_present(root):
        findings, _output = historical_run(root, "--check")
        return findings, "performed; current six rows verified; explicit historical builder replay"
    return candidate_findings(root), "candidate; actual current subjects checked; not performed"


def preview(root: Path, review: str | None = None, disposition: str | None = None) -> dict:
    findings, state = check_state(root)
    review_ready = False
    review_error = None
    if review:
        import record_versioned_signoff as recorder
        try:
            recorder.verify_reviewed(root, recorder.real_packages()[KEY], review, disposition)
            review_ready = True
        except (OSError, ValueError) as exc:
            review_error = str(exc)
    unknowns = consumption_unknowns(root)
    return {"package": KEY, "version": VERSION, "coreCommit": CORE_COMMIT,
            "manifestFileSha256": MANIFEST_SHA256, "coreFiles": len(core_paths(root)),
            "subjects": len(SUBJECTS), "state": state, "candidateFindings": findings,
            "reviewReady": review_ready, "reviewError": review_error,
            "undecidableConsumptionEntries": unknowns,
            "recordingReady": not findings and review_ready and unknowns == 0
                              and not transaction_present(root),
            "ownerSelection": "not collected by this tool", "writes": "none"}


def load_frozen(root: Path):
    spec = importlib.util.spec_from_file_location("p115_frozen_fixture", root / BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def selftest(root: Path) -> int:
    """Only owned temporary fixture subjects/records are ever written."""
    global CORE_COMMIT
    import record_versioned_signoff as recorder
    import build_three_surface_poc_readability_successor as readability
    import check_spec_reconciliation as reconciliation
    import check_governance as governance
    count = consumption_unknowns(root)
    if count:
        print(f"P115 recording preparation selftest BLOCKED: {count} undecidable "
              "requirement-consumption entries; no signed-positive fixtures or readiness claim.")
        return 1
    cases = []
    def expect(name: str, passed: bool):
        cases.append((name, passed))
    def outcomes(tree: Path):
        report = reconciliation.Report()
        reconciliation.check_outcomes(tree, report)
        return report
    def census_report(tree: Path):
        report = reconciliation.Report()
        population = reconciliation.check_census(tree, report)
        return population, report
    def bootstrap_ok(tree: Path) -> bool:
        saved = governance.ROOT
        try:
            governance.ROOT = str(tree)
            report = governance.Results()
            governance.cg7h_general_bootstrap_act(report)
            return not report.failed()
        finally:
            governance.ROOT = saved
    with tempfile.TemporaryDirectory(prefix="p115-recording-selftest-") as temp:
        tree = Path(temp) / "tree"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", "--no-checkout",
                        str(root), str(tree)], check=True, capture_output=True)
        git(tree, "checkout", "--quiet", "--detach", CORE_COMMIT)
        # Exercise current preparation/reader bytes in the frozen core tree.
        for name in (Path(__file__).name, "record_versioned_signoff.py",
                     "record_pwb_behavior_amendment_acts.py", "check_spec_reconciliation.py",
                     "check_governance.py", "build_three_surface_poc_readability_successor.py",
                     "build_three_surface_poc_vocabulary_epistemic_amendment.py"):
            shutil.copyfile(root / "scripts" / name, tree / "scripts" / name)
        expect("candidate checks real BASE subjects", candidate_findings(tree) == [])
        expect("no record supplies no signed successor", not is_signed(tree))
        expect("preview never invents a review/owner answer", not preview(tree)["recordingReady"])
        expect("recording gate follows frozen impact disposition",
               bool(recording_findings(tree)) == bool(consumption_unknowns(tree)))
        expect("candidate does not add a reconciliation successor",
               not any(later.get("package") == KEY for later in
                       reconciliation.successors_for(tree, next(c for c in reconciliation.CHILDREN if c["key"] == "poc"))))
        expect("candidate reconciliation and baseline census pass",
               not outcomes(tree).failed and not census_report(tree)[1].failed)
        expect("candidate bootstrap history passes", bootstrap_ok(tree))
        pkg = recorder.real_packages()[KEY]
        expect("manifest-backed POC registration", pkg.subject == MANIFEST and not pkg.package_digest
               and pkg.extension == recorder.POC_EXTENSION_REL and pkg.installed is None)
        before = {rel: (tree / rel).read_bytes() for rel in SUBJECTS}
        earlier = readability.installed_bytes_at(tree)
        raw = "docs/reviews/R-P115-SELFTEST-RAW.md"
        (tree / raw).write_text(f"# Synthetic review — {KEY}\nReviewed commit: {CORE_COMMIT}\n"
                               f"Manifest SHA-256: {MANIFEST_SHA256}\nVerdict: CONFIRM\n\n"
                               "## Findings\n\nNo findings. Synthetic fixture only; no owner action.\n")
        ready = preview(tree, raw)
        expect("preview checks a synthetic raw without collecting authority",
               ready["reviewReady"] and ready["recordingReady"] == (consumption_unknowns(tree) == 0)
               and ready["ownerSelection"] == "not collected by this tool")
        confirm_raw = (tree / raw).read_bytes()
        notes = confirm_raw.replace(b"Verdict: CONFIRM\n", b"Verdict: CONFIRM WITH EXCEPTIONS\n")
        notes = notes.replace(b"No findings.", "**Finding 1 — fixture note** (note)\n".encode())
        (tree / raw).write_bytes(notes)
        expect("notes-only raw needs a matching disposition", preview(tree, raw)["reviewError"] is not None)
        disposition = (CANDIDATE / "ROUND-999-DISPOSITIONS.md").as_posix()
        (tree / disposition).write_text(f"Reviewed record: {raw}\n\n**Finding 1 — fixture note**\nRetained.\n")
        expect("notes-only raw with matching sibling disposition parses",
               preview(tree, raw, disposition)["reviewReady"])
        (tree / disposition).unlink()
        (tree / raw).write_bytes(confirm_raw)
        _current, proposed = load_frozen(tree).collect()
        reference = recorder._module(Path(__file__).stem)
        original_gate = reference.recording_findings
        bad_patch = tree / CANDIDATE / "proposed/spec.md.patch"
        saved_patch = bad_patch.read_bytes()
        def corrupt_after_gate(location):
            findings = original_gate(location)
            if not findings:
                bad_patch.write_text("--- a/p115-no-such-subject\n+++ b/p115-no-such-subject\n"
                                     "@@ -1 +1 @@\n-missing\n+bad\n")
            return findings
        capture = io.StringIO()
        try:
            # Only this scratch fixture changes between the real gate and
            # preflight. One bad patch must prevent the whole batch writing.
            reference.recording_findings = corrupt_after_gate
            with contextlib.redirect_stdout(capture):
                bad_code = pkg.apply(tree)
        finally:
            reference.recording_findings = original_gate
            bad_patch.write_bytes(saved_patch)
        expect("one bad-patch preflight leaves all six subjects unchanged",
               bad_code != 0 and "P115 preflight refused:" in capture.getvalue()
               and {rel: (tree / rel).read_bytes() for rel in SUBJECTS} == before)
        with contextlib.redirect_stdout(io.StringIO()):
            applied = pkg.apply(tree)
        expect("P115-only five-patch batch installs exact synthetic subjects",
               applied == 0 and applied_rows_match(tree)
               and all((tree / rel).read_bytes() == body for rel, body in proposed.items()))
        expect("unsigned installed proposal is refused", bool(check_state(tree)[0]) and not is_signed(tree))
        expect("unsigned proposed census and bootstrap remain failures",
               "R3" in census_report(tree)[1].failed and not bootstrap_ok(tree))
        quote = "Synthetic fixture selection; no owner action"
        record = recorder.render_record(pkg, VERSION, "2026-10-21", quote, raw,
                                         CORE_COMMIT, "CONFIRM", None)
        aggregate = (tree / AGGREGATE).read_text()
        block = recorder.render_aggregate(pkg, VERSION, "2026-10-21", raw, "CONFIRM", None)
        (tree / RECORD).write_text(record)
        (tree / AGGREGATE).write_text(aggregate.rstrip("\n") + "\n\n" + block)
        expect("exact signed synthetic transaction recognized", is_signed(tree))
        expect("earlier readability rows reconstruct exactly", readability.installed_bytes_at(tree) == earlier)
        p108 = recorder.real_packages()["three-surface-poc-vocabulary-epistemic-amendment"]
        expect("earlier recorder rows accept only signed successor", p108.applied(tree))
        expect("signed six-row reconciliation chain reverses exactly", not outcomes(tree).failed)
        population, report = census_report(tree)
        expect("signed census requires regeneration", "R3" in report.failed)
        (tree / reconciliation.CENSUS).write_text(reconciliation.census_json(population))
        expect("signed census admits exactly 26 requirements and 34 scenarios",
               not census_report(tree)[1].failed
               and len(population["POC"]) == 26
               and sum(len(row["scenarios"]) for row in population["POC"].values()) == 34
               and len(population["POC"]["POC-REQ-014"]["scenarios"]) == 8)
        expect("signed bootstrap current rows are recognized", bootstrap_ok(tree))
        route_report = reconciliation.Report()
        reconciliation.check_routes(tree, population, route_report)
        expect("signed route activation requires root-owned terminal entries",
               any(RECORD.name in finding for finding in route_report.findings.get("R5", ())))
        snapshot = Path(temp) / "snapshot"
        reconciliation.scratch(tree, snapshot)
        expect("read-only snapshot retains signed proof and exact chain",
               is_signed(snapshot) and not outcomes(snapshot).failed)
        # One predicate per mutation, restoring exact bytes after each case.
        unresolved = json.loads((tree / CANDIDATE / "REQUIREMENT-CONSUMPTION.json").read_text())
        unresolved["entries"][0]["classification"] = "undecidable"
        mutations = [
            ("record-only is partial", AGGREGATE, aggregate.encode()),
            ("aggregate-only is partial", RECORD, None),
            ("duplicate aggregate block", AGGREGATE, (aggregate + block + block).encode()),
            ("wrong recorded version", RECORD, record.replace("Version: 1.0", "Version: 2.0").encode()),
            ("wrong review binding", Path(raw), (tree / raw).read_bytes().replace(MANIFEST_SHA256.encode(), b"0" * 64)),
            ("wrong reviewed core", Path(raw), (tree / raw).read_bytes().replace(CORE_COMMIT.encode(), BASE.encode())),
            ("escaping review path", RECORD, record.replace(f"Review: {raw}", "Review: ../outside-RAW.md").encode()),
            ("missing review", Path(raw), None),
            ("wrong manifest hash", MANIFEST, (tree / MANIFEST).read_bytes() + b"\n"),
            ("current subject drift", SUBJECTS[-1], (tree / SUBJECTS[-1]).read_bytes() + b"\n"),
            ("rollback to predecessor is refused", SUBJECTS[-1], before[SUBJECTS[-1]]),
            ("wrong patch bytes", CANDIDATE / "proposed/spec.md.patch",
             (tree / CANDIDATE / "proposed/spec.md.patch").read_bytes() + b"\n"),
            ("unresolved consumption entry", CANDIDATE / "REQUIREMENT-CONSUMPTION.json",
             json.dumps(unresolved).encode()),
        ]
        for name, path, changed in mutations:
            target = tree / path
            saved = target.read_bytes()
            if changed is None:
                target.unlink()
            else:
                target.write_bytes(changed)
            expect(name, not is_signed(tree))
            if name == "unresolved consumption entry":
                expect("unresolved consumption trips its own signed predicate",
                       "signed recognition remains gated by 1 undecidable requirement-consumption entries"
                       in signed_findings(tree))
            if name == "record-only is partial":
                expect("partial transaction cannot explain predecessor rows",
                       not p108.applied(tree) and not bootstrap_ok(tree)
                       and "R1" in outcomes(tree).failed)
            target.write_bytes(saved)
        expect("mutations restore the signed fixture", is_signed(tree))
        findings, output = historical_run(tree, "--selftest")
        expect("signed replay runs frozen selftest, not current subjects", not findings and "Preparation selftest:" in output)
        # Probe the actual signed/replay path with unavailable frozen objects.
        saved_commit = CORE_COMMIT
        try:
            CORE_COMMIT = "0" * 40
            expect("missing frozen history refuses signed recognition", not is_signed(tree))
            try:
                historical_run(tree, "--check")
            except subprocess.CalledProcessError:
                expect("missing frozen history refuses replay", True)
            else:
                expect("missing frozen history refuses replay", False)
        finally:
            CORE_COMMIT = saved_commit
    for name, passed in cases:
        print(f"P115 selftest: {name}: {'ok' if passed else 'FAILED'}")
    failed = sum(not passed for _name, passed in cases)
    print(f"P115 recording preparation selftest: {len(cases)} cases; {failed} failed; scratch only.")
    return int(failed != 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--preview", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    parser.add_argument("--review")
    parser.add_argument("--disposition")
    args = parser.parse_args()
    try:
        if args.selftest:
            return selftest(ROOT)
        if args.preview:
            result = preview(ROOT, args.review, args.disposition)
            print(json.dumps(result, indent=2))
            return int(bool(result["candidateFindings"]) or result["reviewError"] is not None)
        findings, state = check_state(ROOT)
        if findings:
            print("P115 preparation FAILED: " + " | ".join(findings))
            return 1
        print(f"P115 preparation: {state}; {len(core_paths(ROOT))} frozen core files; six subjects; no writes.")
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(f"P115 preparation FAILED: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
