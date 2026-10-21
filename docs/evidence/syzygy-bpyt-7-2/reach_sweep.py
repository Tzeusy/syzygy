#!/usr/bin/env python3
"""Name-based reachability closure from the production entry over cap1-* modules.

A module is REACHABLE when the production entry (apps/syzygy/src/main.ts), or a
module already reachable, mentions in CODE (comments and string/template
literals included only as code text; // and /* */ comments stripped) a name
exported by that module. Barrel index.ts files are skipped as defining files.
Reports the cap1-core / cap1-daemon source modules that are NOT reachable.
Usage: reach_sweep.py <repo-root>
"""
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1])
files = subprocess.run(
    ["git", "ls-files", "-z", "--", "packages", "apps"],
    cwd=root, capture_output=True, check=True,
).stdout.decode().split("\0")
ts = [f for f in files if f.endswith(".ts") and "/src/" in f and not f.endswith(".test.ts")]
scope = [f for f in ts if f.startswith(("packages/cap1-core/", "packages/cap1-daemon/", "apps/syzygy/"))]


def strip_comments(src: str) -> str:
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"(?m)^\s*//.*$|(?<=[;,{}()\s])//[^\n]*$", "", src)


code = {f: strip_comments((root / f).read_text(encoding="utf-8")) for f in scope}
EXPORT = re.compile(
    r"^export\s+(?:declare\s+)?(?:async\s+)?(?:function\*?|const|let|class|interface|type|enum)\s+([A-Za-z_$][\w$]*)",
    re.M,
)
exports = {f: {m.group(1) for m in EXPORT.finditer(code[f])} for f in scope if not f.endswith("/index.ts")}

entry = "apps/syzygy/src/main.ts"
reached = {entry}
queue = [entry]
while queue:
    cur = queue.pop()
    idents = set(re.findall(r"[A-Za-z_$][\w$]*", code[cur]))
    for f, names in exports.items():
        if f not in reached and f != cur and names & idents:
            reached.add(f)
            queue.append(f)

print(f"scope files (non-test cap1-core, cap1-daemon, apps/syzygy): {len(scope)}")
print(f"reached from {entry}: {len(reached)}")
for f in scope:
    if f not in reached and not f.endswith("/index.ts"):
        print("NOT REACHED:", f)
