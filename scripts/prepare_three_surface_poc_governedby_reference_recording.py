#!/usr/bin/env python3
"""Read-only P115 candidate/recording preparation; never signs or installs.

Candidate checks inspect the real adopted subjects. Signed checks require the
exact actual transaction and current rows before replaying the frozen builder
in an owned full clone of its pre-signature tree. --preview is P115-only.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
KEY = "three-surface-poc-governedby-reference-amendment"
VERSION = "1.0"
CORE_COMMIT = "9ef5d35836e722abbd4041900fa27bd02f82e277"
BASE = "4504514c019ca0ee0cb4a89ed97445a0bad21915"
CANDIDATE = Path(".syzygy/governance/contracts/candidates") / KEY
BUILDER = Path("scripts/build_three_surface_poc_governedby_reference_amendment.py")
COMPATIBILITY = Path("scripts/check_p115_compatibility_examples.py")
MANIFEST = CANDIDATE / "THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-MANIFEST.txt"
MANIFEST_SHA256 = "77e53d37ac42c5db4edb4f99d76d937629df5a80d370ac47751c0e62f27270bd"
RECORD = Path(".syzygy/governance/decisions/THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-SIGNOFF-v1.0.md")
AGGREGATE = Path(".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md")
MARKER = f"<!-- versioned-signoff:{KEY}:v{VERSION} -->"
END_MARKER = f"<!-- /versioned-signoff:{KEY}:v{VERSION} -->"
BASE_RECORD = Path(".syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md")
PREDECESSORS = (
    "three-surface-poc-block-provenance-amendment",
    "three-surface-poc-governing-intent-amendment",
    "three-surface-poc-vocabulary-epistemic-amendment",
)
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


def family_snapshot(root: Path) -> dict:
    """Closed leaf observation; never follow nonregular reserved entries.

    File grammar is every immediate name starting with the exact reserved
    stem, before extension/version normalization. Delimiter grammar is the
    case-sensitive exact package token with a colon/space/>/end boundary.
    Missing or unreadable evidence raises; it never establishes absence.
    """
    files = {}
    for path in sorted((root / RECORD.parent).iterdir()):
        if path.name.startswith("THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-SIGNOFF"):
            kind = path.lstat().st_mode
            files[path.name] = {"kind": "regular" if stat.S_ISREG(kind) else "nonregular",
                                "body": path.read_bytes() if stat.S_ISREG(kind) else None}
    path = root / AGGREGATE
    if not stat.S_ISREG(path.lstat().st_mode):
        raise ValueError("P115 aggregate is not a regular nonsymlink file")
    return {"files": files, "aggregate": path.read_bytes()}


def family_state(root: Path) -> tuple[str, list[str]]:
    """ABSENT, PRESENT_INVALID/Unknown, or canonical population; no authority."""
    try:
        population = family_snapshot(root)
        files, body = population["files"], population["aggregate"].decode("utf-8")
        occurrences = list(re.finditer(
            r"versioned-signoff\s*:\s*" + re.escape(KEY) + r"(?=[:\s>]|$)", body))
        if not files and not occurrences:
            return "ABSENT", []
        findings = []
        if set(files) != {RECORD.name} or any(row["kind"] != "regular" for row in files.values()):
            findings.append("P115 family supports only one regular canonical v1.0 dedicated filename")
        comments = list(re.finditer(r"<!--.*?-->", body, re.S))
        delimiters = []
        for occurrence in occurrences:
            enclosing = [comment for comment in comments
                         if comment.start() <= occurrence.start() < occurrence.end() <= comment.end()]
            if len(enclosing) != 1 or enclosing[0].group() not in (MARKER, END_MARKER):
                findings.append("P115 family contains an unsupported, alias, naked or malformed delimiter")
            else:
                delimiters.append(enclosing[0].group())
        if delimiters != [MARKER, END_MARKER] or len(occurrences) != 2:
            findings.append("P115 family requires exactly one ordered balanced canonical v1.0 block")
        return ("PRESENT_INVALID", findings) if findings else ("CANONICAL_POPULATION", [])
    except (OSError, ValueError, UnicodeError) as exc:
        return "PRESENT_INVALID", ["P115 family population is Unknown: " + str(exc)]


def transaction_present(root: Path) -> bool:
    """Malformed/indeterminate family presence cannot disappear as absent."""
    return family_state(root)[0] != "ABSENT"


def chain_findings(root: Path, prospective_date: str | None = None, *,
                   predecessors_only: bool = False) -> list[str]:
    """Leaf validation of this exact frozen POC chain, never later-row readers.

    Complete predecessor records are immutable C4 inputs. Their regenerated
    blocks must be unique, balanced and wholly before the next complete block.
    The prospective arm checks the append position before any recording write.
    """
    state, findings = family_state(root)
    if findings:
        return findings
    if (prospective_date is not None or predecessors_only) and state != "ABSENT":
        return ["P115 prospective chain requires an absent transaction family"]
    import record_versioned_signoff as recorder
    aggregate = (root / AGGREGATE).read_text()
    objects = root if (root / ".git").exists() else ROOT
    packages = recorder.real_packages()

    def fail(message):
        raise ValueError("P115 signed chain: " + message)

    def calendar(text):
        dates = re.findall(r"^Date: (.+)$", text, re.M)
        if len(dates) != 1 or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", dates[0]):
            fail("record must carry exactly one calendar Date line")
        return datetime.date.fromisoformat(dates[0])

    def block_position(start, end, block):
        if aggregate.count(start) != 1 or aggregate.count(end) != 1:
            fail("each begin/end delimiter must occur exactly once")
        begin, finish = aggregate.index(start), aggregate.index(end) + len(end)
        if finish <= begin or aggregate[begin:finish] != block.rstrip("\n"):
            fail("delimiters must enclose the complete regenerated block")
        return begin, finish

    def frozen_record(path):
        body = (root / path).read_bytes()
        if body != git(objects, "show", f"{CORE_COMMIT}:{path.as_posix()}"):
            fail(f"frozen predecessor record differs: {path}")
        return body.decode()

    try:
        baseline = frozen_record(BASE_RECORD)
        instants = re.findall(r"^Act instant: (.+)$", baseline, re.M)
        if len(instants) != 1:
            fail("baseline must carry exactly one act instant")
        previous_date = datetime.datetime.strptime(instants[0], "%Y-%m-%dT%H:%M:%SZ").date()
        start = "<!-- THREE-SURFACE-POC-READABILITY-SUCCESSOR:BEGIN -->"
        end = "<!-- THREE-SURFACE-POC-READABILITY-SUCCESSOR:END -->"
        _begin, previous_end = block_position(start, end, start + "\n" + baseline + end)
        for key in (*PREDECESSORS, *((KEY,) if prospective_date is None and not predecessors_only else ())):
            pkg = packages[key]
            path = recorder.record_rel(pkg, VERSION)
            body = (root / path).read_text() if key == KEY else frozen_record(path)
            date = calendar(body)
            fields = recorder.parse_record(body)
            disposition = None if fields["Disposition"] == "none" else fields["Disposition"]
            block = recorder.render_aggregate(pkg, VERSION, fields["Date"], fields["Review"],
                                              fields["Review verdict"], disposition)
            begin, finish = block_position(*recorder.block_markers(pkg, VERSION), block)
            if begin <= previous_end:
                fail(f"complete block does not follow its predecessor: {key}")
            if date < previous_date:
                fail(f"date precedes its predecessor: {key}")
            previous_end, previous_date = finish, date
        if prospective_date is not None:
            date = calendar("Date: " + prospective_date)
            if date < previous_date:
                fail("prospective date precedes its predecessor")
        return []
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        return [str(exc)]


def builder_run(root: Path, mode: str) -> tuple[list[str], str]:
    done = subprocess.run([sys.executable, str(root / BUILDER), mode], cwd=root,
                          capture_output=True, text=True)
    output = done.stdout + done.stderr
    return ([] if done.returncode == 0 else [f"frozen P115 builder {mode} failed: {output.strip()}"]), output


def candidate_findings(root: Path) -> list[str]:
    state, findings = family_state(root)
    if state != "ABSENT":
        return findings or ["P115 candidate requires an absent transaction family"]
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
    state, findings = family_state(root)
    if state != "CANONICAL_POPULATION":
        return findings or ["P115 dedicated sign-off record is absent"]
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
    findings.extend(chain_findings(root))
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
    population = family_snapshot(root)
    if any(row["kind"] != "regular" for row in population["files"].values()):
        raise ValueError("P115 validation snapshot refuses a nonregular reserved-family entry")
    paths = {(RECORD.parent / name).as_posix() for name in population["files"]}
    paths |= set(core_paths(root)) | {RECORD.as_posix(), AGGREGATE.as_posix(),
        BASE_RECORD.as_posix(),
        ".syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md",
        ".syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md"}
    paths.update((Path(".syzygy/governance/decisions") /
                  (key.upper() + "-SIGNOFF-v1.0.md")).as_posix() for key in PREDECESSORS)
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
        state = "performed; current six rows verified; explicit historical builder replay"
    else:
        findings = candidate_findings(root)
        state = "candidate; actual current subjects checked; not performed"
    return findings, "Unknown; P115 state unverified" if findings else state


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


def mutation_receipt(root: Path, name: str, before: dict, after: dict, predicate: str) -> None:
    """Retain literal changed fragments, identities and the intended predicate."""
    changes = []
    for path in sorted(before.keys() | after.keys()):
        old, new = before.get(path), after.get(path)
        if old == new:
            continue
        left, right = 0, 0
        if old is not None and new is not None:
            while left < min(len(old), len(new)) and old[left] == new[left]:
                left += 1
            while right < min(len(old), len(new)) - left and old[-right-1] == new[-right-1]:
                right += 1
        changes.append({"path": str(path), "offset": left,
            "old": None if old is None else old[left:len(old)-right if right else None].decode(),
            "new": None if new is None else new[left:len(new)-right if right else None].decode(),
            "oldSha256": None if old is None else digest(old),
            "newSha256": None if new is None else digest(new)})
    print("P115-MUTATION-EVIDENCE " + json.dumps({"name": name, "ranAt": git(root, "rev-parse", "HEAD").decode().strip(),
        "predicate": predicate, "changes": changes}, sort_keys=True))


def recording_failure_selftest(root: Path, expect) -> None:
    """Real main(argv), review gate, Git batch, writes and recovery in own clones.

    Fault barriers delegate real I/O. No package/readiness/postcondition result
    is mocked. Synthetic review commits and failed journals die with fixtures;
    their exact state/old/new/cause receipts are emitted to the retained log.
    """
    import record_versioned_signoff as recorder
    from unittest import mock
    paths = (*SUBJECTS, RECORD, AGGREGATE)
    raw = "docs/reviews/R-P115-ENTRYPOINT-SELFTEST-RAW.md"
    fingerprint = "P115 synthetic injected errno-5"
    cases = (
        "control", "dirty-staged", "dirty-unstaged", "dirty-untracked",
        "construction-drift", "preflight-bad-patch", "apply-after-write-failure", "postcondition-drift",
        "dedicated-before-write", "dedicated-stage-prefix-failure", "dedicated-after-write",
        "aggregate-before-write", "aggregate-stage-prefix-failure", "aggregate-after-write",
        "foreign-subject-edit", "foreign-subject-delete", "foreign-record-edit", "foreign-record-delete",
        "foreign-aggregate-edit", "foreign-aggregate-delete", "restore-failure", "restore-stage-drift",
        "linked-worktree-control", "linked-worktree-aggregate-failure",
        *(f"T{n:02}" for n in (*range(1, 16), 19, 20, 21, 22)),
        "OWN-1", "OWN-2", "OWN-3", "OWN-4", "BATCH-2", "BATCH-3", "BATCH-4", "DIRECT-1", "POP-6",
    )
    with tempfile.TemporaryDirectory(prefix="p115-entrypoint-fixtures-") as temp:
        template = Path(temp) / "template"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(root), str(template)],
                       check=True, capture_output=True)
        for name in (Path(__file__).name, "record_versioned_signoff.py"):
            shutil.copyfile(root / "scripts" / name, template / "scripts" / name)
        (template / raw).write_text(f"# Synthetic entrypoint fixture — {KEY}\nReviewed commit: {CORE_COMMIT}\n"
            f"Manifest SHA-256: {MANIFEST_SHA256}\nVerdict: CONFIRM\n\n## Findings\n\n"
            "No findings. Synthetic fixture only; no owner action.\n")
        git(template, "add", "--all")
        git(template, "-c", "user.name=P115 synthetic fixture", "-c", "user.email=fixture@invalid",
            "-c", "core.hooksPath=/dev/null", "commit", "--quiet", "-m",
            "Synthetic recording failure fixtures; no owner action")
        _current, proposed = load_frozen(template).collect()
        proposed = {Path(p): body for p, body in proposed.items()}
        for name in cases:
            tree = Path(temp) / name
            if name.startswith("linked-worktree-"):
                git(template, "-c", "core.hooksPath=/dev/null", "worktree", "add", "--quiet",
                    "--detach", str(tree), "HEAD")
            else:
                subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(template), str(tree)],
                               check=True, capture_output=True)
            cleanup_case = name in {"T09", "T10", "T11", "T22"}
            positive = name in {"control", "linked-worktree-control"} or cleanup_case
            before = {p: recorder.p115_read(tree / p) for p in paths}
            expected = dict(before)
            events, foreign, foreign_identities = [], {}, {}
            initial_head = git(tree, "rev-parse", "HEAD")
            initial_tags = git(tree, "tag", "--list")
            receipt_link_attempts = []
            dirty = tree / "README.md"
            if name in {"dirty-staged", "dirty-unstaged"}:
                dirty.write_bytes(dirty.read_bytes() + b"\nSynthetic unrelated dirt.\n")
                if name == "dirty-staged":
                    git(tree, "add", "README.md")
            if name == "dirty-untracked":
                dirty = tree / "p115-unrelated-untracked.txt"
                dirty.write_text("Synthetic unrelated untracked file.\n")
            dirty_body = dirty.read_bytes() if name.startswith("dirty-") else None
            initial_index = git(tree, "ls-files", "--stage", "-z")
            original_run, original_write = recorder.subprocess.run, recorder.p115_write
            original_stage, original_replace = recorder.p115_stage, recorder.os.replace
            original_link, original_unlink = recorder.os.link, Path.unlink
            original_rmtree, original_read = recorder.shutil.rmtree, recorder.p115_read
            original_read_bytes, original_lstat = Path.read_bytes, Path.lstat
            original_render = recorder.render_record
            failed_once = set()
            native_batches = []
            family_drift = RECORD.with_name(RECORD.name.replace("v1.0", "v02.0"))
            if name == "POP-6":
                exclude = Path(git(tree, "rev-parse", "--git-path", "info/exclude").decode().strip())
                exclude = exclude if exclude.is_absolute() else tree / exclude
                exclude.write_bytes(exclude.read_bytes() + b"\n" + family_drift.as_posix().encode() + b"\n")

            def replace_same_bytes(target):
                path = tree / target
                replacement = path.with_name(".foreign-p115-replacement")
                replacement.write_bytes(proposed[target])
                original_replace(replacement, path)
                foreign[target], foreign_identities[target] = path.read_bytes(), recorder.p115_identity(path)


            def inject(label):
                events.append(label)
                raise OSError(5, fingerprint + ": " + label)

            def run(argv, *args, **kwargs):
                apply = len(argv) > 1 and argv[:2] == ["git", "apply"]
                private = apply and Path(kwargs.get("cwd", tree)) != tree
                if apply and "--check" in argv and name == "preflight-bad-patch":
                    patch = tree / CANDIDATE / "proposed/spec.md.patch"
                    patch.write_text("--- a/p115-no-such-subject\n+++ b/p115-no-such-subject\n"
                                     "@@ -1 +1 @@\n-missing\n+bad\n")
                    foreign[patch.relative_to(tree)] = patch.read_bytes()
                    # Same actual bad-batch preflight, now in the private copy.
                    Path(argv[-1]).write_bytes(patch.read_bytes())
                    events.append("real bad-patch preflight")
                if private and "--check" not in argv and name == "BATCH-2":
                    import resource
                    def native_limit():
                        resource.setrlimit(resource.RLIMIT_FSIZE, (18000, 18000))
                    kwargs["preexec_fn"] = native_limit
                result = original_run(argv, *args, **kwargs)
                if private:
                    native_batches.append({"argv": list(argv), "cwd": str(kwargs["cwd"]),
                        "returncode": result.returncode,
                        "gitDir": kwargs["env"]["GIT_DIR"], "gitWorkTree": kwargs["env"]["GIT_WORK_TREE"],
                        "gitIndexFile": kwargs["env"]["GIT_INDEX_FILE"]})
                if apply and "--check" in argv and name == "BATCH-4":
                    patch = CANDIDATE / "proposed/spec.md.patch"
                    foreign[patch] = (tree / patch).read_bytes() + b"\nForeign root patch after private preflight.\n"
                    (tree / patch).write_bytes(foreign[patch])
                    events.append("native private preflight then foreign root patch drift")
                if apply and "--check" not in argv:
                    events.append("real five-patch apply")
                    if name == "apply-after-write-failure":
                        inject("after real Git apply")
                    if name == "postcondition-drift":
                        target = SUBJECTS[-1]
                        foreign[target] = proposed[target] + b"\nSynthetic foreign post-apply edit.\n"
                        (tree / target).write_bytes(foreign[target])
                    if name == "BATCH-2":
                        projection = Path(kwargs["cwd"])
                        partial = (projection / SUBJECTS[1]).read_bytes()
                        if result.returncode == -25 and len(partial) == 18000 and partial != proposed[SUBJECTS[1]]:
                            events.append("native private batch SIGXFSZ with real 18000-byte partial output")
                    if name == "BATCH-3":
                        path = Path(kwargs["cwd"]) / SUBJECTS[-1]
                        path.write_bytes(path.read_bytes() + b"\nForeign private output drift.\n")
                        events.append("real private batch then physical output mutation")
                return result

            def render(*args, **kwargs):
                result = original_render(*args, **kwargs)
                if name == "construction-drift" and "construction" not in failed_once:
                    failed_once.add("construction")
                    foreign[SUBJECTS[1]] = before[SUBJECTS[1]] + b"\nSynthetic construction-window edit.\n"
                    (tree / SUBJECTS[1]).write_bytes(foreign[SUBJECTS[1]])
                    events.append("real preimage drift during output construction")
                return result

            def write(path, body, **publication):
                rel = path.relative_to(tree)
                label = "dedicated" if rel == RECORD else "aggregate" if rel == AGGREGATE else "subject"
                if rel == RECORD and name in {"T12", "T13", "T14", "T15"}:
                    events.append("real write barrier with " + name + " exception chain")
                    try:
                        filename = tree / "synthetic-volume" if name == "T12" else str(tree / "synthetic-volume")
                        raise OSError(28, "P115 root storage exhausted", filename)
                    except OSError as cause:
                        if name in {"T12", "T15"}:
                            filename = recorder.os.fsencode(path) if name == "T12" else str(path)
                            raise OSError(5, "P115 record wrapper", filename) from cause
                        if name == "T13":
                            raise OSError(5, "P115 record wrapper", str(path))
                        raise OSError(5, "P115 record wrapper", str(path)) from None
                if name == label + "-before-write":
                    inject(label + " before staging")
                if name == "DIRECT-1" and rel == SUBJECTS[2]:
                    inject("direct apply mid-subject before staging")
                original_write(path, body, **publication)
                events.append(label + " real staged replace")
                if name == "OWN-1" and rel == RECORD:
                    replace_same_bytes(SUBJECTS[-1])
                    events.append("real dedicated publication then foreign same-byte subject inode")
                if name == label + "-after-write":
                    inject(label + " after completed replacement")
                foreign_barrier = AGGREGATE if name.startswith("foreign-aggregate-") else RECORD
                if rel == foreign_barrier and name.startswith("foreign-"):
                    family, operation = name.removeprefix("foreign-").rsplit("-", 1)
                    target = {"subject": SUBJECTS[-1], "record": RECORD, "aggregate": AGGREGATE}[family]
                    if operation == "delete":
                        (tree / target).unlink()
                        foreign[target] = None
                    else:
                        foreign[target] = (tree / target).read_bytes() + b"\nSynthetic foreign edit.\n"
                        (tree / target).write_bytes(foreign[target])
                    inject("after real " + label + " write and foreign " + family + " " + operation)
                if rel == AGGREGATE and name in {"restore-failure", "restore-stage-drift",
                                                "linked-worktree-aggregate-failure", "OWN-2"}:
                    inject("after real aggregate write before recovery fault")

            def stage(path, body, **ownership):
                rel = path.relative_to(tree) if path.is_relative_to(tree) else None
                label = "dedicated" if rel == RECORD else "aggregate" if rel == AGGREGATE else "subject"
                completion = path.name.endswith(".ATTEMPT.json") and b'"state": "completed"' in body
                if ((name == label + "-stage-prefix-failure" or name == "T07" and completion)
                        and name not in failed_once):
                    failed_once.add(name)
                    fdopen = recorder.os.fdopen
                    class PrefixStream:
                        def __init__(self, fd, mode):
                            self.stream = fdopen(fd, mode)
                        def __enter__(self):
                            self.stream.__enter__()
                            return self
                        def write(self, value):
                            self.stream.write(value[:max(1, len(value)//2)])
                            self.stream.flush()
                            inject(("completion receipt" if name == "T07" else label) + " real stage prefix write")
                        def __exit__(self, *exc):
                            return self.stream.__exit__(*exc)
                    with mock.patch.object(recorder.os, "fdopen", PrefixStream):
                        return original_stage(path, body, **ownership)
                result = original_stage(path, body, **ownership)
                if name in {"T01", "T02", "T03", "T04"} and name not in failed_once:
                    target = AGGREGATE if name in {"T01", "T02"} else RECORD
                    if rel == target:
                        failed_once.add(name)
                        foreign[target] = (None if name == "T02" else body if name == "T04"
                                           else b"Foreign write during forward staging.\n")
                        if foreign[target] is None:
                            path.unlink()
                        else:
                            path.write_bytes(foreign[target])
                        foreign_identities[target] = recorder.p115_identity(path)
                        events.append("real forward stage then " + name + " foreign mutation")
                if (name == "restore-stage-drift" and rel == SUBJECTS[-1]
                        and body == before[rel] and name not in failed_once):
                    failed_once.add(name)
                    foreign[rel] = proposed[rel] + b"\nSynthetic restoration-window edit.\n"
                    path.write_bytes(foreign[rel])
                    events.append("real restoration-stage ownership drift")
                if (name == "OWN-2" and rel == SUBJECTS[-1] and body == before[rel]
                        and name not in failed_once):
                    failed_once.add(name)
                    replace_same_bytes(rel)
                    events.append("real restoration stage then foreign same-byte subject inode")
                if name == "POP-6" and rel == SUBJECTS[2] and name not in failed_once:
                    failed_once.add(name)
                    foreign[family_drift] = b"Ignored unsupported P115 family drift.\n"
                    (tree / family_drift).write_bytes(foreign[family_drift])
                    events.append("real mid-subject stage then ignored unsupported family drift")
                return result

            def replace(source, destination):
                if (name in {"restore-failure", "T15"} and destination == tree / SUBJECTS[-1]
                        and Path(source).read_bytes() == before[SUBJECTS[-1]]):
                    foreign[SUBJECTS[-1]] = proposed[SUBJECTS[-1]]
                    inject("real restoration replacement failure")
                if Path(destination).name.endswith(".ATTEMPT.json"):
                    body = Path(source).read_bytes()
                    if name == "T08" and b'"state": "completed"' in body:
                        inject("completion receipt native publication failure")
                    if name == "T15" and b'"state": "failed"' in body:
                        events.append("real failed receipt publication barrier")
                        raise OSError(30, "P115 failure receipt storage refused", str(destination))
                result = original_replace(source, destination)
                if name == "OWN-4" and destination == tree / SUBJECTS[1]:
                    failed_once.add("identity-denied")
                    events.append("real native subject publication before identity denial")
                if (name == "T22" and Path(destination).name.endswith(".ATTEMPT.json")
                        and "cleanup-failed" in failed_once):
                    failed_once.add("cleanup-receipt-published")
                    events.append("real cleanup receipt native publication")
                return result

            def link(source, destination):
                if name in {"T20", "T21"} and Path(destination).name.endswith(".ATTEMPT.json"):
                    phase = json.loads(Path(source).read_bytes())["state"]
                    fault = name == "T20" or not receipt_link_attempts
                    receipt_link_attempts.append({"phase": phase, "fault": fault})
                    if fault:
                        events.append("native " + phase + " receipt publication refused")
                        raise OSError(28, "P115 native receipt publication refused: " + phase, str(destination))
                    result = original_link(source, destination)
                    events.append("real failed receipt exclusive publication")
                    return result
                if name == "T05" and destination == tree / RECORD:
                    foreign[RECORD] = Path(source).read_bytes()
                    Path(destination).write_bytes(foreign[RECORD])
                    foreign_identities[RECORD] = recorder.p115_identity(Path(destination))
                    events.append("native exclusive create meets same-byte foreign inode")
                return original_link(source, destination)

            def unlink(path, *args, **kwargs):
                if (name == "OWN-3" and name not in failed_once and path.name.startswith(".p115-")
                        and path.parent == (tree / SUBJECTS[1]).parent
                        and (tree / SUBJECTS[1]).read_bytes() == proposed[SUBJECTS[1]]):
                    failed_once.add(name)
                    inject("native subject staged unlink after confirmed publication")
                if (name == "T06" and name not in failed_once and path.name.startswith(".p115-")
                        and path.parent == (tree / RECORD).parent and (tree / RECORD).exists()):
                    failed_once.add(name)
                    inject("native staged unlink after confirmed publication")
                if name == "T11" and path.name.endswith(".ATTEMPT.json") and name not in failed_once:
                    journal = path.with_name(path.name.removesuffix(".ATTEMPT.json"))
                    if not journal.exists():
                        failed_once.add(name)
                        inject("native completed receipt unlink after payload deletion")
                return original_unlink(path, *args, **kwargs)

            def rmtree(path, *args, **kwargs):
                if (name in {"T09", "T10", "T22"} and Path(path).name.startswith("attempt-")
                        and Path(path).parent.name == "p115-recording-recovery"):
                    if name == "T10":
                        original_unlink(Path(path) / "0.before")
                        events.append("real cleanup removed one captured preimage")
                    failed_once.add("cleanup-failed")
                    inject("postcommit journal cleanup failure")
                return original_rmtree(path, *args, **kwargs)

            def lstat(path, *args, **kwargs):
                if name == "OWN-4" and "identity-denied" in failed_once and path == tree / SUBJECTS[1]:
                    events.append("native published subject identity inspection denied")
                    raise PermissionError(13, "P115 native subject identity inspection refused", str(path))
                return original_lstat(path, *args, **kwargs)

            def read_bytes(path):
                diagnostic = (name == "T22" and path.name.endswith(".ATTEMPT.json")
                              and "cleanup-receipt-published" in failed_once)
                if diagnostic and "cleanup-receipt-readback" in failed_once:
                    events.append("diagnostic receipt native read denied")
                    raise PermissionError(13, "P115 diagnostic receipt read refused", str(path))
                body = original_read_bytes(path)
                if diagnostic:
                    failed_once.add("cleanup-receipt-readback")
                    events.append("real cleanup receipt readback")
                return body

            def read(path):
                result = original_read(path)
                if (name == "T19" and name not in failed_once and path.name.endswith(".ATTEMPT.json")
                        and result is not None and b'"state": "completed"' in result):
                    failed_once.add(name)
                    foreign[SUBJECTS[-1]] = proposed[SUBJECTS[-1]] + b"\nForeign edit during completed receipt readback.\n"
                    (tree / SUBJECTS[-1]).write_bytes(foreign[SUBJECTS[-1]])
                    events.append("real completion receipt readback then foreign subject edit")
                return result

            output = io.StringIO()
            saved_root = recorder.ROOT
            try:
                recorder.ROOT = tree
                with mock.patch.object(recorder.subprocess, "run", run), \
                     mock.patch.object(recorder, "p115_write", write), \
                     mock.patch.object(recorder, "p115_stage", stage), \
                     mock.patch.object(recorder, "render_record", render), \
                     mock.patch.object(recorder.os, "replace", replace), \
                     mock.patch.object(recorder.os, "link", link), \
                     mock.patch.object(Path, "unlink", unlink), \
                     mock.patch.object(Path, "read_bytes", read_bytes), \
                     mock.patch.object(Path, "lstat", lstat), \
                     mock.patch.object(recorder.shutil, "rmtree", rmtree), \
                     mock.patch.object(recorder, "p115_read", read), \
                     contextlib.redirect_stdout(output):
                    if name == "DIRECT-1":
                        code = recorder.real_packages()[KEY].apply(tree)
                    else:
                        code = recorder.main(["--record", KEY, "--version", VERSION, "--date", "2026-10-21",
                            "--review", raw, "--owner-selection-quote", "Synthetic fixture only; no owner action"])
            finally:
                recorder.ROOT = saved_root
            actual = {p: recorder.p115_read(tree / p) for p in paths}
            if positive:
                expected.update(proposed)
                # Literal protocol outputs, independent of any transaction snapshots.
                pkg = recorder.real_packages()[KEY]
                expected[RECORD] = original_render(pkg, VERSION, "2026-10-21",
                    "Synthetic fixture only; no owner action", raw, CORE_COMMIT, "CONFIRM", None,
                    root=tree, rows=tuple(manifest_rows(tree))).encode()
                expected[AGGREGATE] = (before[AGGREGATE].decode().rstrip("\n") + "\n\n"
                    + recorder.render_aggregate(pkg, VERSION, "2026-10-21", raw, "CONFIRM", None)).encode()
            expected.update({p: body for p, body in foreign.items() if p in before})
            if name == "OWN-4":
                expected[SUBJECTS[1]] = proposed[SUBJECTS[1]]
            git_dir = Path(git(tree, "rev-parse", "--absolute-git-dir").decode().strip())
            retained = list((git_dir / "p115-recording-recovery").glob("attempt-*.ATTEMPT.json"))
            journals = [json.loads(p.read_text()) for p in retained]
            lines = output.getvalue()
            state_ok = actual == expected
            gate_ok = code == (0 if positive else 1) and is_signed(tree) == positive
            index_ok = (git(tree, "ls-files", "--stage", "-z") == initial_index
                        and git(tree, "rev-parse", "HEAD") == initial_head
                        and git(tree, "tag", "--list") == initial_tags)
            dirt_ok = (dirty_body is None or dirty.read_bytes() == dirty_body) and all(
                recorder.p115_read(tree / rel) == body for rel, body in foreign.items())
            reached = ("real five-patch apply" in events) == (name not in {
                "dirty-staged", "dirty-unstaged", "dirty-untracked", "construction-drift", "preflight-bad-patch",
                "T20", "T21"})
            originals = [json.loads(line.removeprefix("P115 original exception: "))
                         for line in lines.splitlines() if line.startswith("P115 original exception: ")]
            failure_evidence = (positive and not retained or
                name.startswith("dirty-") and not retained or name == "construction-drift" and not retained or
                bool(journals) and all(j["state"] == "failed" and j.get("originalError")
                                      and j.get("originalException") == originals[0] for j in journals))
            if cleanup_case:
                failure_evidence = (len(journals) == 1 and journals[0]["state"] == "completed"
                    and journals[0]["postconditions"] == {"sixSubjects": True, "exactRecords": True,
                        "signedChain": True, "capturedInputsAndIndex": True}
                    and journals[0]["cleanupException"]["nodes"][0]["errno"] == 5
                    and "P115 WARNING: recording completed; private cleanup failed:" in lines
                    and not originals)
            if name == "T15":
                # The explicitly faulted failure-receipt update leaves prepared
                # evidence. Its original diagnostic still precedes secondaries.
                failure_evidence = (len(journals) == 1 and journals[0]["state"] == "prepared"
                    and len(originals) == 1 and "P115 diagnostic fallback:" in lines
                    and "durable failure update unavailable" in lines)
            if name == "T20":
                failure_evidence = (not retained and len(originals) == 1
                    and "P115 diagnostic fallback:" in lines and "durable failure update unavailable" in lines)
            captured_payload = [{"path": f"{n}.before", "bytes": len(body), "sha256": digest(body)}
                                for n, body in enumerate(before.values()) if body is not None]
            preimages_ok = all(
                row["before"] == (None if before[Path(row["path"])] is None else
                                  digest((p.parent / row["preimage"]).read_bytes()))
                for p, j in zip(retained, journals) for row in j["paths"]
                if not cleanup_case)
            if cleanup_case and journals:
                payload = retained[0].with_name(retained[0].name.removesuffix(".ATTEMPT.json"))
                survivors = recorder.p115_payload_inventory(payload)
                wanted = ([] if name == "T11" else
                          captured_payload[1:] if name == "T10" else captured_payload)
                preimages_ok = (journals[0]["payloadCapturedAtCompletion"] == captured_payload
                                and journals[0]["payloadSurvivors"] == wanted == survivors)
            if name == "T20":
                payloads = [p for p in (git_dir / "p115-recording-recovery").glob("attempt-*") if p.is_dir()]
                preimages_ok = (len(payloads) == 1
                    and recorder.p115_payload_inventory(payloads[0]) == captured_payload)
            receipt_identity_ok = all(j["attemptId"] + ".ATTEMPT.json" == p.name
                and j["ranAt"] == initial_head.decode().strip()
                and j["indexSha256"] == digest(initial_index)
                and j["capturedAt"].endswith("Z") and j["updatedAt"].endswith("Z")
                and datetime.datetime.fromisoformat(j["capturedAt"][:-1] + "+00:00")
                    <= datetime.datetime.fromisoformat(j["updatedAt"][:-1] + "+00:00")
                for p, j in zip(retained, journals))
            claims = [line for line in lines.splitlines() if line.startswith((
                "P115 failed-attempt evidence retained: ", "P115 completed outcome receipt retained: "))]
            phases = [line for line in lines.splitlines() if line.startswith("P115 verified retained receipt phase: ")]
            if name == "T22":
                retention_ok = (not claims and not phases
                    and "P115 receipt verification: unverified/read-error; no retained receipt claimed:" in lines)
            elif journals:
                label = {"failed": "updated failed", "prepared": "older prepared", "completed": "completed"}
                prefix = "P115 completed outcome receipt retained: " if positive else "P115 failed-attempt evidence retained: "
                retention_ok = (len(journals) == 1 and claims == [prefix + str(retained[0])]
                    and phases == ["P115 verified retained receipt phase: " + label[journals[0]["state"]]])
            else:
                retention_ok = not claims and not phases
                if name == "T20":
                    retention_ok = retention_ok and "P115 receipt verification: absent; no retained receipt claimed:" in lines
            failure_evidence = failure_evidence and receipt_identity_ok and retention_ok
            recovery_ok = positive or (
                ("P115 recovery incomplete:" in lines) if actual != before else
                ("P115 recovery complete;" in lines))
            if name == "T20":
                recovery_ok = "P115 recovery incomplete: failure receipt persistence failed;" in lines
            if name == "foreign-record-delete":
                # Absence equals this preimage but does not prove ownership of
                # an independently deleted, previously published record.
                conflict = (str(RECORD) + ": independently changed or deleted; publication ownership unproven")
                recovery_ok = ("P115 recovery incomplete: " + conflict + "\n" in lines
                    and "P115 recovery complete;" not in lines
                    and len(journals) == 1 and journals[0]["recoveryConflicts"] == [conflict])
            if name.startswith("linked-worktree-"):
                preimages_ok = preimages_ok and (tree / ".git").is_file() and git_dir != template / ".git"
            required = {
                "construction-drift": ["real preimage drift during output construction"],
                "preflight-bad-patch": ["real bad-patch preflight"],
                "apply-after-write-failure": ["after real Git apply"],
                "postcondition-drift": ["real five-patch apply"],
                "restore-failure": ["after real aggregate write before recovery fault",
                                    "real restoration replacement failure"],
                "restore-stage-drift": ["after real aggregate write before recovery fault",
                                        "real restoration-stage ownership drift"],
                "linked-worktree-aggregate-failure": ["after real aggregate write before recovery fault"],
            }.get(name, [])
            for label in ("dedicated", "aggregate"):
                required += {
                    label + "-before-write": [label + " before staging"],
                    label + "-stage-prefix-failure": [label + " real stage prefix write"],
                    label + "-after-write": [label + " after completed replacement"],
                }.get(name, [])
            if name.startswith("foreign-"):
                family, operation = name.removeprefix("foreign-").rsplit("-", 1)
                barrier = "aggregate" if family == "aggregate" else "dedicated"
                required = [f"after real {barrier} write and foreign {family} {operation}"]
            required += {
                "T01": ["real forward stage then T01 foreign mutation"],
                "T02": ["real forward stage then T02 foreign mutation"],
                "T03": ["real forward stage then T03 foreign mutation"],
                "T04": ["real forward stage then T04 foreign mutation"],
                "T05": ["native exclusive create meets same-byte foreign inode"],
                "T06": ["native staged unlink after confirmed publication"],
                "T07": ["completion receipt real stage prefix write"],
                "T08": ["completion receipt native publication failure"],
                "T09": ["postcommit journal cleanup failure"],
                "T10": ["real cleanup removed one captured preimage", "postcommit journal cleanup failure"],
                "T11": ["native completed receipt unlink after payload deletion"],
                "T12": ["real write barrier with T12 exception chain"],
                "T13": ["real write barrier with T13 exception chain"],
                "T14": ["real write barrier with T14 exception chain"],
                "T15": ["real write barrier with T15 exception chain", "real restoration replacement failure",
                        "real failed receipt publication barrier"],
                "T19": ["real completion receipt readback then foreign subject edit"],
                "T20": ["native prepared receipt publication refused", "native failed receipt publication refused"],
                "T21": ["native prepared receipt publication refused", "real failed receipt exclusive publication"],
                "T22": ["postcommit journal cleanup failure", "real cleanup receipt native publication",
                        "real cleanup receipt readback", "diagnostic receipt native read denied"],
            }.get(name, [])
            required += {
                "OWN-1": ["real dedicated publication then foreign same-byte subject inode"],
                "OWN-2": ["after real aggregate write before recovery fault",
                          "real restoration stage then foreign same-byte subject inode"],
                "OWN-3": ["native subject staged unlink after confirmed publication"],
                "OWN-4": ["real native subject publication before identity denial",
                          "native published subject identity inspection denied"],
                "BATCH-2": ["native private batch SIGXFSZ with real 18000-byte partial output"],
                "BATCH-3": ["real private batch then physical output mutation"],
                "BATCH-4": ["native private preflight then foreign root patch drift"],
                "DIRECT-1": ["subject real staged replace", "direct apply mid-subject before staging"],
                "POP-6": ["subject real staged replace", "real mid-subject stage then ignored unsupported family drift"],
            }.get(name, [])
            reached = reached and all(event in events for event in required)
            injected = not positive and not name.startswith("T") and name not in {
                "dirty-staged", "dirty-unstaged", "dirty-untracked",
                "construction-drift", "preflight-bad-patch", "postcondition-drift",
                "OWN-1", "OWN-2", "OWN-3", "OWN-4", "BATCH-2", "BATCH-3", "BATCH-4", "DIRECT-1", "POP-6"}
            cause_ok = not injected or fingerprint in lines
            if injected:
                original_error = f"OSError: [Errno 5] {fingerprint}: {required[0]}"
                cause_ok = cause_ok and bool(journals) and all(
                    journal["originalError"] == original_error for journal in journals)
            if name == "postcondition-drift":
                # Original literal "P115 applied postcondition failed" was the
                # governed-batch phase; root drift now fails before publication.
                cause_ok = "P115 transaction input changed:" in lines
            if name == "preflight-bad-patch":
                cause_ok = "P115 preflight refused:" in lines
            if name in {"T06", "T07", "T08"}:
                cause_ok = (len(originals) == 1 and originals[0]["nodes"][0]["errno"] == 5
                            and fingerprint in originals[0]["traceback"])
            if name in {"T12", "T13", "T14", "T15"}:
                nodes = originals[0]["nodes"] if originals else []
                cause_ok = (len(nodes) == 2 and nodes[0]["errno"] == 5
                    and nodes[0]["filename"] == str(tree / RECORD)
                    and nodes[0]["context"] == 1
                    and nodes[0]["cause"] == (1 if name in {"T12", "T15"} else None)
                    and nodes[0]["suppressContext"] == (name != "T13")
                    and nodes[1]["errno"] == 28 and nodes[1]["filename"] == str(tree / "synthetic-volume")
                    and "P115 record wrapper" in originals[0]["traceback"]
                    and ("P115 root storage exhausted" in originals[0]["traceback"]) == (name != "T14"))
                if name == "T12":
                    cause_ok = (cause_ok
                        and nodes[0]["filenameEvidence"] == {"type": "builtins.bytes",
                            "filesystemBytesHex": recorder.os.fsencode(tree / RECORD).hex()}
                        and nodes[1]["filenameEvidence"] == {"type": "pathlib.PosixPath",
                            "filesystemBytesHex": recorder.os.fsencode(tree / "synthetic-volume").hex()}
                        and nodes[0]["filename2"] is None and nodes[1]["filename2"] is None)
                if name == "T15":
                    secondary = [json.loads(line.split(": ", 1)[1]) for line in lines.splitlines()
                                 if line.startswith(("P115 secondary evidence error: ",
                                                     "P115 secondary recovery error: "))]
                    cause_ok = (cause_ok and len(secondary) == 2
                        and sorted(e["nodes"][0]["errno"] for e in secondary) == [5, 30]
                        and lines.index("P115 original exception: ") < lines.index("P115 secondary "))
            if name in {"T01", "T02", "T03", "T04", "T19"}:
                cause_ok = len(originals) == 1 and "P115 transaction input changed:" in originals[0]["nodes"][0]["message"]
            if name == "T05":
                cause_ok = len(originals) == 1 and originals[0]["nodes"][0]["errno"] == 17
            if name in {"T20", "T21"}:
                secondary = [json.loads(line.split(": ", 1)[1]) for line in lines.splitlines()
                             if line.startswith("P115 secondary evidence error: ")]
                cause_ok = (len(originals) == 1 and originals[0]["nodes"][0]["errno"] == 28
                    and receipt_link_attempts == [{"phase": "prepared", "fault": True},
                        {"phase": "failed", "fault": name == "T20"}]
                    and len(secondary) == (1 if name == "T20" else 0))
                if name == "T20":
                    cause_ok = (cause_ok and secondary[0]["nodes"][0]["errno"] == 28
                        and lines.index("P115 original exception: ") < lines.index("P115 secondary evidence error: "))
            if name == "T22":
                secondary = [json.loads(line.split(": ", 1)[1]) for line in lines.splitlines()
                             if line.startswith("P115 secondary receipt verification error: ")]
                cause_ok = (len(secondary) == 1 and secondary[0]["nodes"][0]["errno"] == 13
                            and not originals and len(journals) == 1 and journals[0]["state"] == "completed")
            if name in {"OWN-1", "OWN-2"}:
                cause_ok = bool(originals) and "P115 recovery incomplete:" in lines
            if name in {"OWN-3", "DIRECT-1"}:
                cause_ok = bool(originals) and originals[0]["nodes"][0]["errno"] == 5
            if name == "OWN-4":
                cause_ok = bool(originals) and originals[0]["nodes"][0]["errno"] == 13
            if name == "BATCH-2":
                cause_ok = "P115 batch apply failed (-25):" in lines
            if name == "BATCH-3":
                cause_ok = "P115 private batch outputs differ" in lines
            if name == "BATCH-4":
                cause_ok = "P115 transaction input changed:" in lines
            if name == "POP-6":
                cause_ok = "P115 transaction reserved family changed" in lines
            ownership_ok = all(recorder.p115_identity(tree / rel) == identity
                               for rel, identity in foreign_identities.items())
            if name in {"T03", "T04", "T05", "T12", "T13", "T14"}:
                ownership_ok = ownership_ok and all(str(RECORD) not in j["publications"] for j in journals)
            if name in {"T06", "T07", "T08", "T19"}:
                ownership_ok = ownership_ok and all(str(RECORD) in j["publications"] for j in journals)
            if name in {"apply-after-write-failure", "postcondition-drift", "BATCH-2", "BATCH-3", "BATCH-4"}:
                ownership_ok = ownership_ok and all(not j["publications"] for j in journals)
            if name == "OWN-4":
                ownership_ok = ownership_ok and all(str(SUBJECTS[1]) in j["publications"] for j in journals)
            if name == "DIRECT-1":
                ownership_ok = ownership_ok and all(j["operation"] == "apply" and set(j["publications"]) == {str(SUBJECTS[1])}
                    and j["paths"][-2]["after"] is None for j in journals)
            private_ok = all(
                len(j["batch"]["orderedPatches"]) == 5 and
                j["batch"]["commands"][0]["argv"] == ["git", "init", "--quiet", "--template="]
                and len(j["privatePayloadOnFailure"] or []) > 0
                for j in journals if j["state"] == "failed" and j.get("batch", {}).get("commands"))
            if cleanup_case and journals:
                private_ok = (journals[0]["privatePayloadCapturedAtCompletion"]
                    and journals[0]["privatePayloadSurvivors"] == recorder.p115_private_inventory(payload)
                    and (not journals[0]["privatePayloadSurvivors"] if name == "T11" else
                         journals[0]["privatePayloadSurvivors"] == journals[0]["privatePayloadCapturedAtCompletion"]))
            if name == "BATCH-2":
                private_ok = (private_ok and len(journals) == 1
                    and journals[0]["batch"]["commands"][-1]["returncode"] == -25
                    and any(row["path"] == "projection/" + str(SUBJECTS[1]) and row.get("bytes") == 18000
                            for row in journals[0]["privatePayloadOnFailure"]))
            if native_batches:
                private_ok = private_ok and all(Path(row["cwd"]) != tree
                    and Path(row["gitWorkTree"]) == Path(row["cwd"])
                    and Path(row["gitDir"]).parent == Path(row["cwd"]).parent
                    and Path(row["gitIndexFile"]) == Path(row["gitDir"]) / "index" for row in native_batches)
            stages_clean = not any(any(parent.glob(".p115-*")) for parent in
                                   {(tree / rel).parent for rel in paths})
            expect("entrypoint " + name, state_ok and gate_ok and index_ok and dirt_ok and reached
                   and failure_evidence and cause_ok and preimages_ok and recovery_ok and stages_clean and ownership_ok and private_ok)
            mutation_receipt(tree, "entrypoint " + name, before, actual,
                             "exact scoped preimages/foreign states; no failed transaction signed")
            print("P115-TRANSACTION-EVIDENCE " + json.dumps({"case": name, "syntheticOnly": True,
                "ranAt": git(tree, "rev-parse", "HEAD").decode().strip(), "sourceHead": git(root, "rev-parse", "HEAD").decode().strip(),
                "tools": {p: digest((root / "scripts" / p).read_bytes()) for p in
                          (Path(__file__).name, "record_versioned_signoff.py")},
                "old": "real main(argv), clean captured inputs, real five-patch batch and staged writes",
                "new": name, "predicate": "P115 clean admission, exact postconditions and ownership-preserving recovery",
                "exit": code, "events": events, "expectedStates": {str(p): None if b is None else digest(b) for p,b in expected.items()},
                "actualStates": {str(p): None if b is None else digest(b) for p,b in actual.items()},
                "assertions": {"states": state_ok, "authority": gate_ok, "index": index_ok, "dirt": dirt_ok,
                               "barrierReached": reached, "failureEvidence": failure_evidence, "cause": cause_ok, "privateBatch": bool(private_ok),
                               "ownership": ownership_ok, "retentionVerified": retention_ok},
                "recoveryPreimagesExact": preimages_ok, "recoveryDiagnosticExact": recovery_ok,
                "receiptIdentityAndCaptureTime": receipt_identity_ok,
                "requiredEvents": required, "stageFilesRemoved": stages_clean,
                "originalException": originals, "foreignIdentities": {str(p): t for p,t in foreign_identities.items()},
                "journals": journals, "receiptLinkAttempts": receipt_link_attempts,
                "verifiedReceiptPhases": phases, "retentionClaims": claims, "nativeBatches": native_batches,
                "entryOperation": "direct Package.apply" if name == "DIRECT-1" else "main --record", "output": lines}, sort_keys=True))
            shutil.rmtree(tree)


def family_failure_selftest(root: Path, tree: Path, expect, before: dict, earlier: dict) -> None:
    """Finite family vectors exercise real readers and both existing operations.

    Every fixture commit/record is synthetic. Native metadata/read faults are
    confined to the exact own fixture path; no gate/recognition result is stubbed.
    """
    import record_versioned_signoff as recorder
    import record_pwb_behavior_amendment_acts as behavior
    import build_three_surface_poc_readability_successor as readability
    import check_spec_reconciliation as reconciliation
    import check_governance as governance
    from unittest import mock
    pkg = recorder.real_packages()[KEY]
    signed = {p: (tree / p).read_bytes() for p in (*SUBJECTS, RECORD, AGGREGATE)}
    fields = recorder.parse_record(signed[RECORD].decode())
    block = recorder.render_aggregate(pkg, VERSION, fields["Date"], fields["Review"],
                                      fields["Review verdict"], None)
    aggregate = signed[AGGREGATE].decode().replace(block, "").rstrip("\n") + "\n"
    census_path = Path(reconciliation.CENSUS)
    census_signed = (tree / census_path).read_bytes()
    census_base = git(tree, "show", f"{CORE_COMMIT}:{census_path}")
    unsupported = RECORD.with_name(RECORD.name.replace("v1.0", "v2.0"))
    alias = RECORD.with_name(RECORD.name.replace("v1.0", "v01.0"))
    extra = RECORD.with_name("THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-SIGNOFF.backup")
    vectors = (
        ("POP-1 malformed v2 file", "file", unsupported),
        ("POP-2 orphan v2 end", "orphan", None),
        ("POP-3 v01 alias file", "file", alias),
        ("POP-4 canonical begin-only", "begin", None),
        ("POP-4 canonical end-only", "end", None),
        ("POP-4 mismatched versions", "mismatch", None),
        ("POP-4 duplicate canonical block", "duplicate", None),
        ("POP-5 nonregular family directory", "directory", unsupported),
        ("POP-5 symlink family entry", "symlink", unsupported),
        ("POP companion naked delimiter", "naked", None),
        ("POP companion unclosed delimiter", "unclosed", None),
        ("POP companion whitespace alias", "whitespace", None),
        ("POP companion reserved stem extension", "file", extra),
        ("POP companion missing aggregate", "missing", None),
        ("POP companion unreadable aggregate", "unreadable", None),
    )
    def setup(installed):
        for path in (unsupported, alias, extra):
            target = tree / path
            if target.is_dir() and not target.is_symlink():
                target.rmdir()
            else:
                target.unlink(missing_ok=True)
        for path in SUBJECTS:
            (tree / path).write_bytes(signed[path] if installed else before[path])
        if installed:
            (tree / RECORD).write_bytes(signed[RECORD])
        else:
            (tree / RECORD).unlink(missing_ok=True)
        (tree / AGGREGATE).write_bytes(signed[AGGREGATE] if installed else aggregate.encode())
        (tree / census_path).write_bytes(census_signed if installed else census_base)

    governance_reports = []
    def bootstrap():
        saved = governance.ROOT
        try:
            governance.ROOT = str(tree)
            report = governance.Results()
            governance.cg7h_general_bootstrap_act(report)
            governance_reports.append({"failed": report.failed(), "summaries": report.summaries})
            return not report.failed()
        finally:
            governance.ROOT = saved

    for installed in (True, False):
        setup(installed)
        control_findings, control_state = check_state(tree)
        control_preview = preview(tree)
        control_label = ("performed; current six rows verified; explicit historical builder replay" if installed
                         else "candidate; actual current subjects checked; not performed")
        control = (is_signed(tree) == installed and not control_findings and bootstrap()
                   and control_state == control_label and control_preview["state"] == control_label
                   and not control_preview["candidateFindings"])
        for label, mutation, path in vectors:
            setup(installed)
            start = {p: (tree / p).read_bytes() if (tree / p).exists() else None
                     for p in (AGGREGATE, RECORD, *((path,) if path else ()))}
            if mutation == "file":
                (tree / path).write_bytes(b"Malformed synthetic P115 reserved-family record.\n")
            elif mutation == "directory":
                (tree / path).mkdir()
            elif mutation == "symlink":
                (tree / path).symlink_to("README.md")  # Census observes metadata; target is Syzygy documentation.
            elif mutation == "missing":
                (tree / AGGREGATE).unlink()
            elif mutation != "unreadable":
                prefixes = {
                    "orphan": (tree / AGGREGATE).read_text() + END_MARKER.replace("v1.0", "v2.0"),
                    "begin": aggregate + MARKER,
                    "end": aggregate + END_MARKER,
                    "mismatch": aggregate + MARKER + "\n" + END_MARKER.replace("v1.0", "v2.0"),
                    "duplicate": aggregate + block + block,
                    "naked": (tree / AGGREGATE).read_text() + f"versioned-signoff:{KEY}:v1.0",
                    "unclosed": (tree / AGGREGATE).read_text() + f"<!-- versioned-signoff:{KEY}:v1.0",
                    "whitespace": (tree / AGGREGATE).read_text() + f"<!-- versioned-signoff : {KEY}:v1.0 -->",
                }
                (tree / AGGREGATE).write_text(prefixes[mutation])
            # Whole-clean admission is real, so malformed family must be its
            # actual blocker rather than unrelated dirty-fixture refusal.
            git(tree, "add", "--all")
            git(tree, "-c", "user.name=P115 synthetic family", "-c", "user.email=fixture@invalid",
                "-c", "core.hooksPath=/dev/null", "commit", "--quiet", "--allow-empty", "-m",
                "Synthetic malformed P115 family; no owner action")
            physical = {p: (tree / p).read_bytes() if (tree / p).exists() else None
                        for p in (*SUBJECTS, RECORD, AGGREGATE)}
            raw_read = Path.read_bytes
            def read_bytes(target):
                if mutation == "unreadable" and target == tree / AGGREGATE:
                    raise PermissionError(13, "P115 synthetic family aggregate read refused", str(target))
                return raw_read(target)
            outputs, codes, frontiers = {}, {}, {}
            governance_reports.clear()
            saved_root = recorder.ROOT
            try:
                recorder.ROOT = tree
                with mock.patch.object(Path, "read_bytes", read_bytes):
                    state, findings = family_state(tree)
                    check_findings, check_label = check_state(tree)
                    preview_result = preview(tree)
                    frontiers.update(control=control, family=state == "PRESENT_INVALID" and bool(findings),
                        presence=transaction_present(tree), candidate=bool(candidate_findings(tree)),
                        recording=bool(recording_findings(tree)), checkState=bool(check_findings),
                        checkStateLabel=check_label == "Unknown; P115 state unverified",
                        preview=bool(preview_result["candidateFindings"]) and not preview_result["recordingReady"],
                        previewLabel=preview_result["state"] == "Unknown; P115 state unverified",
                        signed=bool(signed_findings(tree)) and not is_signed(tree),
                        chain=bool(chain_findings(tree)), historical=bool(historical_run(tree, "--check")[0]))
                    try:
                        inputs = validation_inputs(tree)
                        frontiers["snapshotClosure"] = path is None or path.as_posix() in inputs
                    except (OSError, ValueError):
                        frontiers["snapshotClosure"] = True  # Explicit refusal, never lossy snapshot success.
                    for operation in ("check", "record", "apply", "unsupported-check"):
                        out = io.StringIO()
                        with contextlib.redirect_stdout(out):
                            if operation == "apply":
                                code = pkg.apply(tree)
                            elif operation == "record":
                                code = recorder.main(["--record", KEY, "--version", VERSION, "--date", "2026-10-21",
                                    "--review", fields["Review"], "--owner-selection-quote", "Synthetic family fixture only"])
                            else:
                                code = recorder.main(["--check", KEY, "--version",
                                                      "2.0" if operation == "unsupported-check" else VERSION])
                        codes[operation], outputs[operation] = code, out.getvalue()
                    frontiers["CLIAndOperations"] = (all(code == 1 for code in codes.values())
                        and all("not performed" not in text and "superseded" not in text for text in outputs.values())
                        and "must be clean" not in outputs["record"] and "must be clean" not in outputs["apply"])
                    sha = dict((p, sha) for sha, p in manifest_rows(tree))[str(SUBJECTS[-1])]
                    frontiers["behaviorRows"] = sha not in behavior._later_rows(tree, None, str(SUBJECTS[-1]))
                    reconstructed = readability.installed_bytes_at(tree)
                    frontiers["readability"] = reconstructed != earlier if installed else reconstructed == earlier
                    child = next(c for c in reconciliation.CHILDREN if c["key"] == "poc")
                    successors = reconciliation.successors_for(tree, child)
                    later = next(row for row in successors if row.get("package") == KEY)
                    frontiers["reversal"] = reconciliation.bytes_at(tree, str(SUBJECTS[-1]), (later,)) is None
                    report = reconciliation.Report()
                    consumer_errors = {}
                    try:
                        reconciliation.check_outcomes(tree, report)
                        frontiers["reconciliation"] = "R1" in report.failed
                    except OSError as reader_error:
                        # Its immutable generic addition scan may refuse a
                        # nonregular reserved entry before returning a report.
                        # Only this exact fixture input is an admitted refusal.
                        consumer_errors["reconciliation"] = recorder.p115_exception(reader_error)
                        frontiers["reconciliation"] = (reader_error.filename is not None
                            and Path(reader_error.filename) in {tree / AGGREGATE, tree / path if path else tree / AGGREGATE})
                    census = reconciliation.Report()
                    try:
                        reconciliation.check_census(tree, census)
                        frontiers["census"] = (not installed or "R3" in census.failed)
                    except OSError as reader_error:
                        consumer_errors["census"] = recorder.p115_exception(reader_error)
                        frontiers["census"] = (reader_error.filename is not None
                            and Path(reader_error.filename) in {tree / AGGREGATE, tree / path if path else tree / AGGREGATE})
                    try:
                        frontiers["governance"] = not bootstrap() if installed or mutation == "missing" else bootstrap()
                    except OSError as reader_error:
                        consumer_errors["governance"] = recorder.p115_exception(reader_error)
                        frontiers["governance"] = (reader_error.filename is not None
                            and Path(reader_error.filename) in {tree / AGGREGATE, tree / path if path else tree / AGGREGATE})
            finally:
                recorder.ROOT = saved_root
            after = {p: (tree / p).read_bytes() if (tree / p).exists() else None for p in physical}
            frontiers["noWrites"] = after == physical
            name = label + (" on signed" if installed else " on unsigned")
            expect(name, all(frontiers.values()))
            changed = {p: (tree / p).read_bytes() if (tree / p).is_file() and not (tree / p).is_symlink() else None for p in start}
            mutation_receipt(tree, name, start, changed, "complete reserved-family invalidity at every P115 frontier")
            print("P115-FAMILY-EVIDENCE " + json.dumps({"case": name, "ranAt": git(tree, "rev-parse", "HEAD").decode().strip(),
                "sourceHead": git(root, "rev-parse", "HEAD").decode().strip(), "syntheticOnly": True,
                "tools": {n: digest((root / "scripts" / n).read_bytes()) for n in
                          (Path(__file__).name, "record_versioned_signoff.py")},
                "old": "valid signed v1.0" if installed else "pristine unsigned BASE subjects",
                "new": mutation, "entry": None if path is None else str(path), "familyState": state,
                "findings": findings, "checkState": {"state": check_label, "findings": check_findings},
                "preview": preview_result, "frontiers": frontiers, "codes": codes, "consumerErrors": consumer_errors, "governanceReports": governance_reports, "output": outputs}, sort_keys=True))
    setup(False)
    unrelated = f"<!-- versioned-signoff:{KEY}-different:v2.0 -->"
    saved = (tree / AGGREGATE).read_bytes()
    (tree / AGGREGATE).write_bytes(saved + unrelated.encode())
    expect("POP companion extended different package token stays outside family",
           family_state(tree) == ("ABSENT", []) and not transaction_present(tree))
    mutation_receipt(tree, "POP companion extended different package token stays outside family",
                     {AGGREGATE: saved}, {AGGREGATE: saved + unrelated.encode()}, "exact package token boundary")
    setup(True)


def recording_render_selftest(root: Path, expect) -> None:
    """Three pure full-output controls; no check, apply or recording is called."""
    import types
    import record_versioned_signoff as recorder
    historical = "5c07616c4c5719c9de4ce92c137162394bb32bb3"
    old = types.ModuleType("p115_historical_render_selftest")
    old.__file__ = str(root / "scripts/record_versioned_signoff.py")
    sys.modules[old.__name__] = old
    try:
        source = git(root, "show", historical + ":scripts/record_versioned_signoff.py")
        exec(compile(source, "Git:" + historical + ":record_versioned_signoff.py", "exec"), old.__dict__)
        packages, historical_packages = recorder.real_packages(), old.real_packages()
        pkg = packages[KEY]
        review = "docs/reviews/R-P115-RENDER-SELFTEST-RAW.md"
        quote = "Synthetic structured selection; no owner action"
        expected_aggregate = """<!-- versioned-signoff:three-surface-poc-governedby-reference-amendment:v1.0 -->
## Versioned sign-off — three-surface-poc-governedby-reference-amendment — v1.0 — recorded 2026-10-21

The owner signed off version 1.0 by selecting an option in a structured
question naming this package and version (quoted in the dedicated record).

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Kind | specification amendment |
| Review outcome | `docs/reviews/R-P115-RENDER-SELFTEST-RAW.md`: `CONFIRM` |
| Recording | `.syzygy/governance/decisions/THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-SIGNOFF-v1.0.md`; annotated tag `three-surface-poc-governedby-reference-amendment-v1.0` on the commit carrying these records and the applied result |
| Direction | `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, extended by `.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md` |

This sign-off authorizes no implementation, widens no consent, read, write or
egress, and a later version of the package is signed separately.
<!-- /versioned-signoff:three-surface-poc-governedby-reference-amendment:v1.0 -->
"""
        expected_record = """# Three-Surface POC governedBy reference amendment — version-tagged sign-off v1.0

Date: 2026-10-21

Owner: Tzeusy

Package: three-surface-poc-governedby-reference-amendment

Version: 1.0

Tag: three-surface-poc-governedby-reference-amendment-v1.0

Kind: specification amendment

Owner selection: Synthetic structured selection; no owner action

Review: docs/reviews/R-P115-RENDER-SELFTEST-RAW.md

Reviewed commit: 9ef5d35836e722abbd4041900fa27bd02f82e277

Review verdict: CONFIRM

Disposition: none

Scope A extension: `.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md` extends the direction below to this package's kind

Signed under `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`: the owner's selection of an option naming this package and version is the sign-off; no phrase or digest argument exists.

## What this records

The owner signed off version 1.0 of `.syzygy/governance/contracts/candidates/three-surface-poc-governedby-reference-amendment` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the frozen P115 builder check passed before the exact five patches were applied
as one preflighted Git batch through the P115 recording adapter.

The binding is the annotated tag `three-surface-poc-governedby-reference-amendment-v1.0` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
"""
        actual_aggregate = recorder.render_aggregate(pkg, VERSION, "2026-10-21", review, "CONFIRM", None)
        actual_record = recorder.render_record(pkg, VERSION, "2026-10-21", quote, review, CORE_COMMIT,
                                               "CONFIRM", None)
        for name, expected, actual, before in (
            ("T16 exact neutral P115 aggregate", expected_aggregate, actual_aggregate,
             old.render_aggregate(historical_packages[KEY], VERSION, "2026-10-21", review, "CONFIRM", None)),
            ("T18 exact P115 application provenance record", expected_record, actual_record,
             old.render_record(historical_packages[KEY], VERSION, "2026-10-21", quote, review,
                               CORE_COMMIT, "CONFIRM", None)),
        ):
            expect(name, actual == expected)
            print("P115-RENDER-EVIDENCE " + json.dumps({"case": name, "syntheticOnly": True,
                "ranAt": git(root, "rev-parse", "HEAD").decode().strip(), "historicalHead": historical,
                "predicate": "full independent literal output; P115-only provenance", "old": before,
                "new": actual, "expected": expected, "passed": actual == expected}, sort_keys=True))
        keys = (
            "pwb-missing-currency-disclosure-scenario", "pwb-dismissal-expiry-amendment",
            "pwb-container-shape-profile-amendment", "pwb-item-depth-amendment", "pwb-readability-successor",
            "pwb-tree-framing-amendment", "pwb-anchor-resolution-amendment",
            "three-surface-poc-block-provenance-amendment", "pwb-class-granular-extraction-amendment",
            "pwb-accessible-name-amendment", "pwb-opening-index-amendment",
            "three-surface-poc-governing-intent-amendment", "three-surface-poc-vocabulary-epistemic-amendment",
            "cap1-trusted-bootstrap-consent", "polaris-dossier-local-agent-mode",
            "public-git-source-acquisition-local-agent", "polaris-dossier-local-agent-mode@1.1",
            "polaris-dossier-local-agent-mode@1.2",
        )
        controls = []
        for key in keys:
            new_pkg, old_pkg = packages[key], historical_packages[key]
            version = key.split("@", 1)[1] if "@" in key else "1.0"
            choices = (frozenset(), frozenset({"n6"})) if key.endswith("@1.1") else (frozenset(),)
            rows = tuple(("0" * 64, p.as_posix()) for p in old_pkg.applied_subjects)
            for options in choices:
                for verdict, disposition in (("CONFIRM", None), ("CONFIRM WITH EXCEPTIONS", "synthetic-disposition.md")):
                    args = version, "2026-10-21", quote, review, CORE_COMMIT, verdict, disposition, options
                    kwargs = {"root": root, "instant": "2026-10-21T00:00:00Z", "rows": rows}
                    before_record = old.render_record(old_pkg, *args, **kwargs)
                    after_record = recorder.render_record(new_pkg, *args, **kwargs)
                    before_aggregate = old.render_aggregate(old_pkg, version, "2026-10-21", review, verdict, disposition)
                    after_aggregate = recorder.render_aggregate(new_pkg, version, "2026-10-21", review, verdict, disposition)
                    controls.append({"key": key, "version": version, "options": sorted(options), "verdict": verdict,
                        "disposition": disposition, "oldRecord": before_record, "newRecord": after_record,
                        "oldAggregate": before_aggregate, "newAggregate": after_aggregate,
                        "passed": before_record == after_record and before_aggregate == after_aggregate})
        passed = (set(keys) == set(packages) - {KEY} == set(historical_packages) - {KEY}
                  and len(controls) == 38 and all(row["passed"] for row in controls))
        expect("T17 all non-P115 full historical record and aggregate outputs", passed)
        print("P115-RENDER-EVIDENCE " + json.dumps({"case": "T17", "syntheticOnly": True,
            "ranAt": git(root, "rev-parse", "HEAD").decode().strip(), "historicalHead": historical,
            "predicate": "entire non-P115 payloads match frozen historical formatter", "keys": list(keys),
            "packageCount": len(keys), "argumentCases": len(controls), "fullOutputs": 2 * len(controls),
            "controls": controls, "passed": passed}, sort_keys=True))
    finally:
        sys.modules.pop(old.__name__, None)


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
        # The actual P115 apply/record path admits only a clean checkout.
        git(tree, "add", "--all")
        git(tree, "-c", "user.name=P115 synthetic fixture", "-c", "user.email=fixture@invalid",
            "-c", "core.hooksPath=/dev/null", "commit", "--quiet", "-m",
            "Synthetic P115 preparation fixture; no owner action")
        _current, proposed = load_frozen(tree).collect()
        reference = recorder._module(Path(__file__).stem)
        bad_patch = tree / CANDIDATE / "proposed/spec.md.patch"
        saved_patch = bad_patch.read_bytes()
        from unittest import mock
        native_run = recorder.subprocess.run
        def corrupt_at_preflight(argv, *args, **kwargs):
            if argv[:2] == ["git", "apply"] and "--check" in argv:
                # The real strict gate already passed; only own captured
                # private bytes mutate at this native preflight boundary.
                Path(argv[-1]).write_text("--- a/p115-no-such-subject\n+++ b/p115-no-such-subject\n"
                                         "@@ -1 +1 @@\n-missing\n+bad\n")
            return native_run(argv, *args, **kwargs)
        capture = io.StringIO()
        with mock.patch.object(recorder.subprocess, "run", corrupt_at_preflight), contextlib.redirect_stdout(capture):
            bad_code = pkg.apply(tree)
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
            mutation_receipt(tree, name, {path: saved}, {path: changed}, "signed recognition refuses exact mutation")
            if name == "unresolved consumption entry":
                expect("unresolved consumption trips its own signed predicate",
                       "signed recognition remains gated by 1 undecidable requirement-consumption entries"
                       in signed_findings(tree))
            if name == "record-only is partial":
                expect("partial transaction cannot explain predecessor rows",
                       not p108.applied(tree) and not bootstrap_ok(tree)
                       and "R1" in outcomes(tree).failed)
            target.write_bytes(saved)
        end = recorder.block_markers(pkg, VERSION)[1]
        signed_aggregate = (tree / AGGREGATE).read_bytes()
        chain_mutations = [
            ("P115 block before all predecessors", {AGGREGATE: (block + aggregate).encode()}),
            ("P115 backdated before predecessors", {
                RECORD: record.replace("Date: 2026-10-21", "Date: 2026-01-01").encode(),
                AGGREGATE: signed_aggregate.replace(b"recorded 2026-10-21", b"recorded 2026-01-01")}),
            ("P115 duplicate closing delimiter", {AGGREGATE: signed_aggregate + end.encode() + b"\n"}),
            ("P115 orphan closing is present", {RECORD: None, AGGREGATE: aggregate.encode() + end.encode() + b"\n"}),
            ("P115 invalid calendar date", {
                RECORD: record.replace("Date: 2026-10-21", "Date: 2026-02-30").encode(),
                AGGREGATE: signed_aggregate.replace(b"recorded 2026-10-21", b"recorded 2026-02-30")}),
        ]
        predecessor = recorder.real_packages()[PREDECESSORS[-1]]
        pred_start, pred_end = recorder.block_markers(predecessor, VERSION)
        # Preserve the predecessor start position but break its complete block.
        chain_mutations.append(("P115 nested inside predecessor block", {AGGREGATE:
            (aggregate.replace(pred_end, block + pred_end)).encode()}))
        chain_mutations.append(("predecessor orphan closing delimiter", {AGGREGATE:
            signed_aggregate + pred_end.encode() + b"\n"}))
        pred_record = recorder.record_rel(predecessor, VERSION)
        chain_mutations.append(("predecessor duplicate date", {pred_record:
            (tree / pred_record).read_bytes() + b"\nDate: 2026-10-15\n"}))
        for name, changes in chain_mutations:
            saved = {path: (tree / path).read_bytes() for path in changes}
            for path, body in changes.items():
                (tree / path).unlink() if body is None else (tree / path).write_bytes(body)
            findings = signed_findings(tree)
            expect(name, transaction_present(tree) and not is_signed(tree) and bool(findings))
            mutation_receipt(tree, name, saved, changes, "leaf complete-chain dates/order/unique balanced delimiters")
            for path, body in saved.items():
                (tree / path).write_bytes(body)
        expect("mutations restore the signed fixture", is_signed(tree))
        family_failure_selftest(root, tree, expect, before, earlier)
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
    recording_failure_selftest(root, expect)
    recording_render_selftest(root, expect)
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
