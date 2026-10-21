#!/usr/bin/env python3
"""Regenerate each superseded screening-scope policy act record with its own recorder (syzygy-bpyt.8.10). Evidence tool, not a check.

The battery holds the screening-scope chain's records to their recorders only through the version-4 `--check` line: a superseded
version's recorder refuses before it regenerates anything, because the policy on disk is no longer the bytes its act bound ("fails
--check by design"). This probe asks the question that line no longer can: is each superseded record still exactly what its recorder
renders? In a scratch clone of this checkout's HEAD commit it puts back the policy bytes the version's act bound and runs that
recorder's own `do_check` (the function its `--check` line calls) over the record; it never writes to this checkout. Version 2 and 3
bytes are the policy blob committed with each act record. Version 1's were never committed (versions 1 and 2 were recorded and applied
in one commit), so they are rebuilt by the version-1 builder's `propose()` as it stood in the parent of that commit, over the policy
there. The owner selection passed to `do_check` is read from the record's own ceremony lines.

Output is JSON on stdout: per record, the recorder, the commit the bytes came from, whether they hash to the act's argument (the
argument itself is never printed: cite the record), the exit status and the recorder's own output, and the same check over the
record with one Effect line altered, which must fail. Exit 0 only when every record regenerates and every control fails.

  python3 scripts/probe_superseded_policy_act_regeneration.py [--keep-clones]

Reads git objects and files of this checkout only; writes only under a temporary directory it removes. Standard library only.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib
import io
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = ".syzygy/governance/decisions"
POLICY = ".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"
#: (recorder module, record file, where the bound policy bytes come from: the recording commit's blob, or the version-1 builder run
#: at the recording commit's parent)
ROWS = (
    ("record_public_source_screening_scope_act", "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md", "propose-at-parent"),
    ("record_public_source_screening_scope_v2_act", "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md", "blob-at-commit"),
    ("record_public_source_screening_scope_v3_act", "PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V3-ACT.md", "blob-at-commit"),
)


def git(*args: str, cwd: pathlib.Path = ROOT) -> str:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout


def clone(at: str, into: pathlib.Path) -> pathlib.Path:
    subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(into)], check=True)
    subprocess.run(["git", "-C", str(into), "checkout", "--quiet", "--detach", at], check=True)
    return into


def selection_args(text: str, fields: tuple[str, ...]) -> tuple[str, ...]:
    """The owner selection as the record's ceremony states it, in the order the recorder's `Selection` takes it."""
    opening = re.search(r'that opened "(.*)" by selecting the$', text, re.M)
    row = re.search(r'^\| "(.*)" \| "(.*)" \|$', text, re.M)
    if opening is None or row is None:
        raise ValueError("the record's ceremony carries no opening line or selection row")
    values = {"opening": opening.group(1), "label": row.group(1), "description": row.group(2)}
    if "words" in fields:
        words = re.search(r'maps that option to its words "(.*?)"', text, re.S)
        if words is None:
            raise ValueError("the record's ceremony carries no packet words")
        values["words"] = words.group(1)
    return tuple(values[name] for name in fields)


#: The control: the same check over the record with one prose line of its Effect section altered must fail (rule 6), or a pass
#: above proves nothing about the record's prose.
ALTERATION = "the first non-blank line after '## Effect' gets ' [altered]' appended"


def altered(text: str) -> str:
    lines = text.split("\n")
    at = lines.index("## Effect") + 1
    while not lines[at].strip():
        at += 1
    lines[at] += " [altered]"
    return "\n".join(lines)


def probe(head: pathlib.Path, scratch: pathlib.Path) -> list[dict]:
    sys.path.insert(0, str(head / "scripts"))
    head_policy = (head / POLICY).read_bytes()
    out = []
    for module_name, record, source in ROWS:
        m = importlib.import_module(module_name)
        rel = f"{DECISIONS}/{record}"
        text = (head / rel).read_text()
        argument = re.search(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`$", text, re.M).group(1)
        date = re.search(r"^Date: (\S+)$", text, re.M).group(1)
        added = git("log", "--format=%H", "--diff-filter=A", "--", rel).split()
        if len(added) != 1:
            raise ValueError(f"{rel} was added by {len(added)} commits, not 1")
        if source == "blob-at-commit":
            at = added[0]
            policy = subprocess.run(["git", "show", f"{at}:{POLICY}"], cwd=ROOT, capture_output=True, check=True).stdout
            how = f"the policy blob committed with the record at {at}"
        else:
            at = git("rev-parse", f"{added[0]}^").strip()
            old = clone(at, scratch / f"parent-{at[:12]}")
            run = subprocess.run([sys.executable, "-c", "import pathlib, sys; sys.path.insert(0, 'scripts'); "
                                  "import build_public_source_screening_scope as b; "
                                  "sys.stdout.write(b.propose(pathlib.Path(b.POLICY).read_text()))"],
                                 cwd=old, capture_output=True, text=True, check=True)
            policy = run.stdout.encode()
            how = f"scripts/build_public_source_screening_scope.py propose() at {at}, over the policy there"
        row = {"recorder": f"scripts/{module_name}.py", "record": rel, "recordedIn": added[0], "policyBytes": how,
               "policyBytesAreTheArgument": hashlib.sha256(policy).hexdigest() == argument}
        sel = m.Selection(*selection_args(text, tuple(m.Selection.__dataclass_fields__)))
        try:
            (head / POLICY).write_bytes(policy)
            for key, record_text in (("", text), ("controlAlteredProse", altered(text))):
                (head / rel).write_text(record_text)
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    code = m.do_check(head, m.ACT, argument, date, sel)
                if key:
                    row[key] = {"alteration": ALTERATION, "exit": code, "stdout": buf.getvalue()}
                else:
                    row["exit"], row["stdout"] = code, buf.getvalue()
        finally:
            (head / POLICY).write_bytes(head_policy)
            (head / rel).write_text(text)
        out.append(row)
    return out


def main(argv: list[str]) -> int:
    keep = "--keep-clones" in argv[1:]
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="probe-superseded-policy-acts-"))
    try:
        commit = git("rev-parse", "HEAD").strip()
        head = clone(commit, scratch / "head")
        rows = probe(head, scratch)
        print(json.dumps({"measuredOn": {"commit": commit, "note": "committed bytes of HEAD only; working-tree edits are not read"},
                          "records": rows}, indent=1))
        return 0 if all(r["exit"] == 0 and r["policyBytesAreTheArgument"] and r["controlAlteredProse"]["exit"] == 1 for r in rows) else 1
    finally:
        if not keep:
            shutil.rmtree(scratch, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
