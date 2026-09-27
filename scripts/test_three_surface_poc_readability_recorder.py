"""Disposable Git worktree tests for the readability successor transaction.

No test uses the caller's common Git directory for its journal or receipt.
"""

from __future__ import annotations

import fcntl
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

import record_three_surface_poc_readability_successor as r


PHRASE = r.LABEL + ": " + r.MANIFEST_SHA  # synthetic fixture, never an owner act
INSTANT = "ACT INSTANT: 2026-09-28T12:00:00Z"
TESTS = 0


def assert_case(name: str, condition: bool) -> None:
    global TESTS
    if not condition:
        raise AssertionError(name)
    TESTS += 1


def run(*command: str, cwd: Path | None = None, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True)


def cli(root: Path, mode: str, *, failure: str | None = None, kill: str | None = None, manifest: str | None = None) -> subprocess.CompletedProcess:
    command = [sys.executable, str(root / "scripts/record_three_surface_poc_readability_successor.py"), "--" + mode]
    if mode in ("record", "render-performed"):
        command += ["--phrase", PHRASE, "--act-instant", INSTANT]
    if mode == "record":
        command += ["--expected-output-manifest-sha256", manifest or rendered_manifest(root)]
    env = os.environ.copy()
    env.update(SYZYGY_RECORDER_TESTING="1")
    if failure:
        env["SYZYGY_RECORDER_FAIL_AT"] = failure
    if kill:
        env["SYZYGY_RECORDER_KILL_AT"] = kill
    return run(*command, cwd=root, env=env)


def rendered_manifest(root: Path) -> str:
    _root, _git_dir, common, tx = r.context(root)
    return r.render(root, common, tx, PHRASE, INSTANT)["output_manifest_sha256"]


def check(root: Path) -> str:
    _root, _git_dir, common, tx = r.context(root)
    return r.check_state(root, common, tx)


def refuses(callback, contains: str | None = None) -> bool:
    try:
        callback()
    except (r.Refusal, OSError) as error:
        return contains is None or contains in str(error)
    return False


def overlay_script(source: Path, root: Path) -> None:
    target = root / "scripts" / source.name
    target.write_bytes(source.read_bytes())


def reset(a: Path, b: Path, common: Path) -> None:
    for root in (a, b):
        done = run("git", "reset", "--hard", "HEAD", cwd=root)
        if done.returncode:
            raise AssertionError(done.stderr)
        (root / r.DEDICATED).unlink(missing_ok=True)
    shutil.rmtree(common / r.TX_NAME, ignore_errors=True)


def snapshot(root: Path) -> dict[str, bytes | None]:
    return {path: (root / path).read_bytes() if (root / path).exists() else None
            for path in (*r.TARGETS, r.ROWS[0][0], r.ROWS[1][0])}


def install_direct(a: Path, values: dict[str, bytes]) -> None:
    for path, body in values.items():
        target = a / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)


def fixture_tests(a: Path, b: Path, common: Path) -> None:
    global TESTS
    tx = common / r.TX_NAME
    assert_case("distinct worktree roots", a != b and r.context(a)[0] != r.context(b)[0])
    assert_case("shared canonical common Git directory", r.context(a)[2] == r.context(b)[2] == common)
    assert_case("one lock/journal/receipt path", r.context(a)[3] == r.context(b)[3] == tx and common / r.LOCK_NAME == r.context(a)[2] / r.LOCK_NAME)
    assert_case("root checkout canonical lock path", r.context(r.ROOT)[2] / r.LOCK_NAME == r.git_path(r.ROOT, "--git-common-dir") / r.LOCK_NAME)
    assert_case("absolute target escape refused", refuses(lambda: r.safe_target(a, "/tmp/escape"), "noncanonical"))
    assert_case("parent target escape refused", refuses(lambda: r.safe_target(a, "../escape"), "noncanonical"))
    assert_case("inert A and B", check(a) == check(b) == "candidate-unperformed")
    subject = a / r.TARGETS[0]
    saved_subject = subject.read_bytes()
    subject.unlink()
    subject.symlink_to(a / r.TARGETS[1])
    assert_case("symlinked subject refused", refuses(lambda: check(a), "symlinked"))
    subject.unlink()
    subject.write_bytes(saved_subject)
    tx.parent.mkdir(parents=True, exist_ok=True)
    tx.symlink_to(a, target_is_directory=True)
    assert_case("symlinked journal root refused", refuses(lambda: r.context(a), "symlinked"))
    tx.unlink()

    # A shared reader and exclusive writer both wait for the common lock.
    fd = os.open(common / r.LOCK_NAME, os.O_RDWR | os.O_CREAT, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        reader = subprocess.Popen([sys.executable, str(b / "scripts/record_three_surface_poc_readability_successor.py"), "--check"], cwd=b, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.8)
        assert_case("shared check waits behind exclusive lock", reader.poll() is None)
        fcntl.flock(fd, fcntl.LOCK_UN)
        reader.communicate(timeout=30)
        assert_case("shared check resumes", reader.returncode == 0)
        fcntl.flock(fd, fcntl.LOCK_SH)
        writer = subprocess.Popen([sys.executable, str(a / "scripts/record_three_surface_poc_readability_successor.py"), "--record", "--phrase", PHRASE, "--act-instant", INSTANT, "--expected-output-manifest-sha256", rendered_manifest(a)], cwd=a, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.8)
        assert_case("exclusive record waits behind shared lock", writer.poll() is None)
        fcntl.flock(fd, fcntl.LOCK_UN)
        writer.communicate(timeout=60)
        assert_case("exclusive record resumes", writer.returncode == 0 and check(a) == "performed-exact")
    finally:
        os.close(fd)
    reset(a, b, common)
    assert_case("candidate manifest recomputes", r.sha((a / r.MANIFEST).read_bytes()) == r.MANIFEST_SHA)
    proposed = r.candidate(a)
    assert_case("four changed and two identical proposals", sum(old != new for _p, old, new in r.ROWS) == 4 and all(r.sha(proposed[p]) == n for p, _o, n in r.ROWS))
    assert_case("render deterministic", r.render(a, common, tx, PHRASE, INSTANT) == r.render(a, common, tx, PHRASE, INSTANT))
    bad_phrases = [None, PHRASE + "\n", PHRASE.lower(), PHRASE.replace(": ", ":  "), PHRASE[:-1] + "A", "`" + PHRASE + "`", PHRASE + " extra"]
    for value in bad_phrases:
        assert_case("malformed owner phrase refused", refuses(lambda value=value: r.owner_inputs(value, INSTANT), "owner phrase"))
    for value in (None, "ACT INSTANT: 2026-02-30T12:00:00Z", "ACT INSTANT: 2026-09-28T12:00:00+00:00", "ACT INSTANT: 2026-09-28T12:00:00Z\n", "2026-09-28T12:00:00Z"):
        assert_case("invalid owner instant refused", refuses(lambda value=value: r.owner_inputs(PHRASE, value), "ACT INSTANT"))
    assert_case("exact owner inputs accepted", r.owner_inputs(PHRASE, INSTANT) == "2026-09-28T12:00:00Z")
    assert_case("record needs output manifest", refuses(lambda: r.record(a, r.context(a)[1], common, tx, PHRASE, INSTANT, None), "output manifest"))

    # Closed state matrix with the exact eight performed bytes.
    values = r.outputs(a, proposed, PHRASE, INSTANT)
    install_direct(a, {p: values[p] for p in r.TARGETS[:4]})
    assert_case("installed subjects without acts refused", refuses(lambda: check(a), "without both"))
    install_direct(a, {r.DEDICATED: values[r.DEDICATED]})
    assert_case("dedicated only refused", refuses(lambda: check(a), "without both"))
    reset(a, b, common)
    (a / r.AGGREGATE).write_bytes(values[r.AGGREGATE])
    assert_case("aggregate only with predecessors refused", refuses(lambda: check(a), "predecessor subjects"))
    reset(a, b, common)
    install_direct(a, {p: values[p] for p in r.TARGETS})
    assert_case("exact performed without receipt", check(a) == "performed-exact")
    (a / r.AGGREGATE).write_bytes((a / r.AGGREGATE).read_bytes() + r.aggregate_block(values[r.DEDICATED]))
    assert_case("duplicated aggregate block refused", refuses(lambda: check(a), "aggregate"))
    (a / r.AGGREGATE).write_bytes(values[r.AGGREGATE])
    (a / r.ROUTER).write_bytes((a / r.ROUTER).read_bytes() + r.router_row("2026-09-28T12:00:00Z"))
    assert_case("duplicated router row refused", refuses(lambda: check(a), "router"))
    (a / r.ROUTER).write_bytes(values[r.ROUTER])
    (a / r.STATUS).write_bytes((a / r.STATUS).read_bytes() + r.status_statement("2026-09-28T12:00:00Z"))
    assert_case("duplicated current statement refused", refuses(lambda: check(a), "PROJECT-STATUS"))
    (a / r.STATUS).write_bytes(values[r.STATUS])
    (a / r.TARGETS[0]).write_bytes(values[r.TARGETS[0]] + b"drift")
    assert_case("post-act signed subject drift refused", refuses(lambda: check(a), "neither predecessor nor successor"))
    (a / r.TARGETS[0]).write_bytes(values[r.TARGETS[0]])
    for path in (r.AGGREGATE, r.ROUTER, r.STATUS):
        (a / path).write_bytes((a / path).read_bytes() + b"\nUnrelated later note.\n")
    assert_case("scoped append-only performed check", check(a) == "performed-exact")
    reset(a, b, common)

    # All ordinary exceptions before the commit point return exact inert bytes.
    baseline = snapshot(a)
    for failure in ("before-install", *[f"target-{n}" for n in range(1, 9)], "installed-verified", "pending-receipt"):
        reset(a, b, common)
        result = cli(a, "record", failure=failure)
        assert_case(f"exception {failure} fails", result.returncode != 0)
        assert_case(f"exception {failure} restores inert", snapshot(a) == baseline and check(a) == "candidate-unperformed" and not r.journal_present(tx))

    # SIGKILL leaves a visible journal. B alone recovers A and never changes B.
    for boundary in ("prepared", *[f"target-{n}" for n in range(1, 9)], "installed-verified", "pending-receipt", "committed-phase", "final-receipt", "cleanup-start"):
        reset(a, b, common)
        b_before = snapshot(b)
        result = cli(a, "record", kill=boundary)
        assert_case(f"SIGKILL {boundary} reached", result.returncode == -9 and r.journal_present(tx))
        assert_case(f"SIGKILL {boundary} blocks both checks", all(cli(root, "check").returncode != 0 and "recovery required" in cli(root, "check").stderr for root in (a, b)))
        recovered = cli(b, "recover")
        expect = "performed-exact" if boundary in ("committed-phase", "final-receipt", "cleanup-start") else "candidate-unperformed"
        assert_case(f"B recovers A after {boundary}", recovered.returncode == 0 and expect in recovered.stdout and check(a) == expect and not r.journal_present(tx))
        assert_case(f"B unchanged after {boundary}", snapshot(b) == b_before)
        if expect == "candidate-unperformed":
            assert_case(f"A inert after {boundary}", snapshot(a) == baseline and not r.receipt_path(tx).exists())
        else:
            assert_case(f"receipt after {boundary}", r.receipt_path(tx).is_file())

    # Independent corruption of backup, stage and journal fields refuses recovery.
    for kind in ("backup", "staged", "version", "uuid", "phase", "next_index", "worktree_root", "git_dir", "common_dir", "common_dev", "common_ino", "manifest_sha256", "phrase_sha256", "instant_line_sha256", "targets"):
        reset(a, b, common)
        result = cli(a, "record", kill="target-1")
        assert_case(f"corruption setup {kind}", result.returncode == -9)
        if kind in ("backup", "staged"):
            file = tx / ("backups" if kind == "backup" else "staged") / "00.bin"
            file.write_bytes(file.read_bytes() + b"corrupt")
        else:
            file = r.journal_path(tx)
            value = json.loads(file.read_bytes())
            value[kind] = "corrupt" if kind != "targets" else []
            value["checksum_sha256"] = r.sha(r.canonical_json({key: item for key, item in value.items() if key != "checksum_sha256"}))
            file.write_bytes(r.canonical_json(value))
        before = snapshot(a)
        rejected = cli(b, "recover")
        assert_case(f"corrupt {kind} rejected with evidence", rejected.returncode != 0 and r.journal_present(tx) and snapshot(a) == before)

    # A relocated or symlinked worktree must never turn B into a recovery target.
    reset(a, b, common)
    assert_case("missing-root setup", cli(a, "record", kill="target-1").returncode == -9)
    moved = a.with_name(a.name + "-moved")
    a.rename(moved)
    try:
        assert_case("missing bound root refuses", cli(b, "recover").returncode != 0 and r.journal_present(tx))
        a.symlink_to(moved, target_is_directory=True)
        assert_case("symlinked bound root refuses", cli(b, "recover").returncode != 0 and r.journal_present(tx))
        a.unlink()
    finally:
        moved.rename(a)
    assert_case("restored bound root recovers", cli(b, "recover").returncode == 0)

    # Two linked workers serialize; only one may record this act identity.
    reset(a, b, common)
    before_a, before_b = snapshot(a), snapshot(b)
    manifest = rendered_manifest(a)
    def command(root):
        return [sys.executable, str(root / "scripts/record_three_surface_poc_readability_successor.py"), "--record", "--phrase", PHRASE, "--act-instant", INSTANT, "--expected-output-manifest-sha256", manifest]
    first = subprocess.Popen(command(a), cwd=a, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    second = subprocess.Popen(command(b), cwd=b, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    first.communicate(timeout=120)
    second.communicate(timeout=120)
    assert_case("concurrent one winner", sorted((first.returncode, second.returncode)) == [0, 1])
    winner, loser = (a, b) if first.returncode == 0 else (b, a)
    assert_case("winner exact, loser byte-identical", check(winner) == "performed-exact" and snapshot(loser) == (before_b if loser == b else before_a))
    assert_case("one repository-wide receipt", r.receipt_path(tx).is_file() and not r.journal_present(tx))
    assert_case("same-common-dir replay refused", cli(loser, "record", manifest=manifest).returncode != 0)
    receipt = r.receipt_path(tx)
    original = receipt.read_bytes()
    receipt.write_bytes(original + b"bad")
    assert_case("malformed optional receipt fails", refuses(lambda: check(winner), "receipt"))
    receipt.write_bytes(original)
    assert_case("restored optional receipt passes", check(winner) == "performed-exact")
    reset(a, b, common)

    # A performed commit remains checkable after cloning without git-local receipt.
    values = r.outputs(a, r.candidate(a), PHRASE, INSTANT)
    install_direct(a, values)
    add = run("git", "add", *r.TARGETS, cwd=a)
    commit = run("git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture performed successor", cwd=a)
    assert_case("fixture performed commit", add.returncode == commit.returncode == 0)
    clean = a.with_name("performed-clone")
    cloned = run("git", "clone", "-q", str(a), str(clean))
    assert_case("performed clean clone created", cloned.returncode == 0)
    overlay_script(r.SCRIPT, clean)
    assert_case("portable performed check without receipt", cli(clean, "check").returncode == 0 and "performed-exact" in cli(clean, "check").stdout and not r.receipt_path(r.context(clean)[3]).exists())


def selftest() -> int:
    with tempfile.TemporaryDirectory(prefix="syzygy-poc-recorder-test-") as directory:
        base = Path(directory)
        main, a, b = base / "repo", base / "A", base / "B"
        clone = run("git", "clone", "-q", "--no-hardlinks", str(r.ROOT), str(main))
        if clone.returncode:
            raise AssertionError(clone.stderr)
        for root in (a, b):
            worktree = run("git", "worktree", "add", "--detach", str(root), "HEAD", cwd=main)
            if worktree.returncode:
                raise AssertionError(worktree.stderr)
        for root in (a, b):
            overlay_script(r.SCRIPT, root)
        common = r.context(a)[2]
        fixture_tests(a, b, common)
    print(f"PASS {TESTS} recorder assertions: state, phrase/time, exception, SIGKILL, recovery, corruption, concurrency, replay, portable clone")
    return 0


def governance_fixtures() -> list[tuple[str, bool]]:
    """Exercise CG-7i's existence gate and the real recorder state predicate."""
    spec = importlib.util.spec_from_file_location("poc_governance_fixture", r.ROOT / "scripts/check_governance.py")
    governance = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(governance)

    class Capture:
        def __init__(self):
            self.rows = []

        def add(self, status, name, examined, findings, unit, note=None, details=None):
            self.rows.append((status, examined, findings, details or []))

    with tempfile.TemporaryDirectory(prefix="syzygy-poc-cg7i-") as directory:
        root = Path(directory) / "repo"
        clone = run("git", "clone", "-q", "--no-hardlinks", str(r.ROOT), str(root))
        if clone.returncode:
            raise AssertionError(clone.stderr)
        overlay_script(r.SCRIPT, root)

        def result():
            capture = Capture()
            governance.cg7i_poc_readability_successor(capture, str(root))
            return capture.rows[0]

        def restore():
            done = run("git", "reset", "--hard", "HEAD", cwd=root)
            if done.returncode:
                raise AssertionError(done.stderr)
            (root / r.DEDICATED).unlink(missing_ok=True)

        cases = []
        manifest = root / r.MANIFEST
        script = root / "scripts/record_three_surface_poc_readability_successor.py"
        manifest.unlink()
        script.unlink()
        cases.append(("CG-7i absent candidate reports no claim", result()[0:3] == ("WARN", 0, 0)))
        restore()
        overlay_script(r.SCRIPT, root)
        cases.append(("CG-7i inert candidate accepted", result()[0:3] == ("OK", 6, 0)))
        proposed = r.candidate(root)
        outputs = r.outputs(root, proposed, PHRASE, INSTANT)
        install_direct(root, {p: outputs[p] for p in r.TARGETS[:4]})
        cases.append(("CG-7i installed/no acts rejected", result()[0] == "FAIL"))
        install_direct(root, {r.DEDICATED: outputs[r.DEDICATED]})
        cases.append(("CG-7i dedicated only rejected", result()[0] == "FAIL"))
        (root / r.DEDICATED).unlink()
        install_direct(root, {r.AGGREGATE: outputs[r.AGGREGATE]})
        cases.append(("CG-7i aggregate only rejected", result()[0] == "FAIL"))
        install_direct(root, {r.DEDICATED: outputs[r.DEDICATED], r.ROUTER: outputs[r.ROUTER], r.STATUS: outputs[r.STATUS]})
        cases.append(("CG-7i exact performed accepted", result()[0:3] == ("OK", 6, 0)))
        (root / r.AGGREGATE).write_bytes(outputs[r.AGGREGATE] + r.aggregate_block(outputs[r.DEDICATED]))
        cases.append(("CG-7i conflicting duplicate rejected", result()[0] == "FAIL"))
        (root / r.AGGREGATE).write_bytes(outputs[r.AGGREGATE])
        (root / r.STATUS).write_bytes(outputs[r.STATUS] + b"false-current\n")
        # A conflicting exact statement is required for this predicate.
        (root / r.STATUS).write_bytes(outputs[r.STATUS] + r.status_statement("2026-09-28T12:00:00Z"))
        cases.append(("CG-7i post-act current-state drift rejected", result()[0] == "FAIL"))
        restore()
        overlay_script(r.SCRIPT, root)
        manifest.write_bytes(manifest.read_bytes().replace(b".openspec.yaml\n", b"tasks.md\n"))
        cases.append(("CG-7i wrong manifest chain rejected", result()[0] == "FAIL"))
        return cases
