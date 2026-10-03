#!/usr/bin/env python3
"""Run a signed PWB candidate builder's ``--selftest`` against its pre-adoption tree.

A versioned-sign-off PWB builder's selftest builds its fixtures from the
candidate's proposed patches applied to the signed subjects. After sign-off
the recorder has applied those patches, and later sign-offs have rewritten
the subjects, so the selftest stops at "patch does not apply" at main and its
rule-6 fixtures become unrunnable (syzygy-tmkb).

``rerun_before_signoff`` restores them. Once the package's sign-off record
exists, it extracts the last candidate-phase commit with ``git archive`` into
a scratch directory, copies in the builder's *current* bytes and this module,
and runs ``--selftest`` there. Inside that tree the record does not exist, so
the selftest runs in place. The scratch tree is read from git and never
registered as a worktree; the repository is not written. A clone without that
commit (a shallow one) refuses with exit 1 and says why, rather than passing.

``--selftest`` here checks the helper itself in a synthetic repository.
"""

from __future__ import annotations

import hashlib
import pathlib
import shutil
import subprocess
import sys
import os
import tarfile
import tempfile

HELPER = pathlib.Path(__file__).resolve()
#: Set for the nested run, so a pre-adoption tree that somehow carries the
#: record can never start a second archive inside the first.
NESTED = "PWB_SIGNED_SELFTEST_NESTED"


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rerun_before_signoff(script: str, record: str, commit: str) -> int | None:
    """None while ``record`` is absent (run the selftest in place); otherwise
    the exit code of ``script --selftest`` run in an archive of ``commit``."""
    builder = pathlib.Path(script).resolve()
    root = builder.parents[1]
    if not (root / record).is_file():
        return None
    name = builder.name
    if os.environ.get(NESTED):
        print(f"refusing: {record} exists inside the pre-adoption tree; "
              f"not starting a nested rerun")
        return 1
    print(f"{name}: signed off ({record}); running this file's current bytes "
          f"against the pre-adoption tree {commit[:12]} (git archive)", flush=True)
    with tempfile.TemporaryDirectory() as temp:
        tree = pathlib.Path(temp)
        proc = subprocess.Popen(["git", "-C", str(root), "archive", commit],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert proc.stdout is not None
        try:
            with tarfile.open(fileobj=proc.stdout, mode="r|") as archive:
                if hasattr(tarfile, "data_filter"):
                    archive.extractall(tree, filter="data")
                else:
                    archive.extractall(tree)
        except tarfile.TarError:
            proc.stdout.read()
        error = proc.stderr.read().decode() if proc.stderr else ""
        if proc.wait() != 0:
            print(f"refusing: cannot read pre-adoption commit {commit} "
                  f"(a shallow clone lacks it): {error.strip()}")
            return 1
        (tree / "scripts").mkdir(exist_ok=True)
        for source in (builder, HELPER):
            shutil.copy2(source, tree / "scripts" / source.name)
            if sha256(tree / "scripts" / source.name) != sha256(source):
                print(f"refusing: {source.name} copy differs from its current bytes")
                return 1
        if (tree / record).is_file():
            print(f"refusing: {record} already exists at {commit[:12]}, "
                  f"which is therefore not a pre-adoption tree")
            return 1
        return subprocess.run([sys.executable, str(tree / "scripts" / name),
                               "--selftest"], cwd=tree,
                              env={**os.environ, NESTED: "1"}).returncode


# ------------------------------------------------------------------ selftest

BUILDER = '''import os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pwb_signed_selftest as helper
VERSION = "{version}"
if "--selftest" in sys.argv:
    rerun = helper.rerun_before_signoff(__file__, "RECORD.md", os.environ["COMMIT"])
    if rerun is not None:
        raise SystemExit(rerun)
    root = pathlib.Path(__file__).resolve().parents[1]
    here = (root / "FIXTURE").is_file() and (pathlib.Path.cwd() / "FIXTURE").is_file()
    print("ran", VERSION, "fixture" if here else "no-fixture")
    raise SystemExit(0 if here else 3)
'''


def selftest() -> int:
    cases = []
    with tempfile.TemporaryDirectory() as temp:
        repo = pathlib.Path(temp) / "repo"
        (repo / "scripts").mkdir(parents=True)

        def git(*args: str) -> str:
            return subprocess.run(["git", "-C", str(repo), *args], check=True,
                                  capture_output=True, text=True).stdout.strip()

        def run(commit: str) -> subprocess.CompletedProcess:
            return subprocess.run([sys.executable, str(repo / "scripts/build.py"),
                                   "--selftest"], capture_output=True, text=True,
                                  cwd=repo, env={**os.environ, "COMMIT": commit})

        git("init", "-q")
        git("config", "user.email", "selftest@example.invalid")
        git("config", "user.name", "selftest")
        shutil.copy2(HELPER, repo / "scripts" / HELPER.name)
        (repo / "scripts/build.py").write_text(BUILDER.format(version="old"))
        (repo / "FIXTURE").write_text("candidate-phase fixture\n")
        git("add", "-A")
        git("commit", "-q", "-m", "candidate")
        candidate = git("rev-parse", "HEAD")

        candidate_run = run(candidate)
        cases.append(("no record: the selftest runs in place",
                      candidate_run.returncode == 0
                      and "ran old fixture" in candidate_run.stdout
                      and "signed off" not in candidate_run.stdout))

        # Sign-off: the record appears, the fixture goes, the builder changes.
        (repo / "RECORD.md").write_text("signed\n")
        (repo / "FIXTURE").unlink()
        (repo / "scripts/build.py").write_text(BUILDER.format(version="new"))
        git("add", "-A")
        git("commit", "-q", "-m", "sign-off")
        signed = git("rev-parse", "HEAD")

        rerun = run(candidate)
        cases.append(("after sign-off: current bytes run in the pre-adoption tree",
                      rerun.returncode == 0 and "ran new fixture" in rerun.stdout))
        cases.append(("the scratch tree leaves the repository unchanged",
                      git("status", "--porcelain") == ""
                      and len(git("worktree", "list").splitlines()) == 1))
        signed_run = run(signed)
        cases.append(("a commit carrying the record is refused",
                      signed_run.returncode == 1
                      and "is therefore not a pre-adoption tree" in signed_run.stdout))
        missing = run("0" * 40)
        cases.append(("an unreadable commit refuses rather than passing",
                      missing.returncode == 1
                      and "cannot read pre-adoption commit" in missing.stdout))
        nested = subprocess.run([sys.executable, str(repo / "scripts/build.py"), "--selftest"],
                                capture_output=True, text=True, cwd=repo,
                                env={**os.environ, "COMMIT": candidate, NESTED: "1"})
        cases.append(("a nested rerun is refused",
                      nested.returncode == 1 and "nested rerun" in nested.stdout))

    failed = [name for name, caught in cases if not caught]
    for name, caught in cases:
        print(f"selftest: {name}: {'ok' if caught else 'FAILED'}")
    if failed:
        print("SELFTEST FAILED: " + ", ".join(failed))
        return 1
    print(f"selftest: {len(cases)} cases pass")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        raise SystemExit(selftest())
    print("usage: pwb_signed_selftest.py --selftest (imported by the PWB builders)")
    raise SystemExit(2)
