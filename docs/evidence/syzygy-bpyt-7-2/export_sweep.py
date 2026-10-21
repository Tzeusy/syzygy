#!/usr/bin/env python3
"""Classify every export of the production modules in cap1-core and cap1-daemon.

For each exported name in a non-test source file under the given package dirs,
report where it is referenced (word match, via Python re over file bytes):
  prod_other  - non-test source files other than the defining file
  prod_self   - uses inside the defining file beyond its own declaration
  test        - *.test.ts files
A name with prod_other == 0 is "not used by another production module";
test-only means prod_other == 0 and prod_self == 0 and test > 0.
Usage: export_sweep.py <repo-root> <pkgdir> [<pkgdir> ...]
"""
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1])
pkgs = sys.argv[2:]

files = subprocess.run(
    ["git", "ls-files", "-z", "--", "packages", "apps"],
    cwd=root, capture_output=True, check=True,
).stdout.decode().split("\0")
ts = [f for f in files if f.endswith(".ts") and "/src/" in f]
is_test = lambda f: f.endswith(".test.ts")
text = {f: (root / f).read_text(encoding="utf-8") for f in ts}

EXPORT = re.compile(
    r"^export\s+(?:declare\s+)?(?:async\s+)?(?:function\*?|const|let|class|interface|type|enum)\s+([A-Za-z_$][\w$]*)",
    re.M,
)

rows = []
for f in ts:
    if is_test(f) or not any(f.startswith(p + "/") for p in pkgs):
        continue
    if f.endswith("/index.ts"):
        continue
    for m in EXPORT.finditer(text[f]):
        name = m.group(1)
        pat = re.compile(r"(?<![\w$])" + re.escape(name) + r"(?![\w$])")
        self_hits = len(pat.findall(text[f])) - 1
        prod_other, tests = [], []
        for g in ts:
            if g == f:
                continue
            if pat.search(text[g]):
                (tests if is_test(g) else prod_other).append(g)
        rows.append((f, name, self_hits, prod_other, tests))

print("file\tname\tself_uses\tprod_other_files\ttest_files")
for f, name, self_hits, po, t in rows:
    if not po:
        print(f"{f}\t{name}\t{self_hits}\t{len(po)}\t{len(t)}")
print(f"# exports scanned: {len(rows)}")
print(f"# no other production module: {sum(1 for r in rows if not r[3])}")
print(f"# test-only (no other prod, no self use, >0 test): {sum(1 for r in rows if not r[3] and r[2] == 0 and r[4])}")
print(f"# unreferenced anywhere (no self use): {sum(1 for r in rows if not r[3] and r[2] == 0 and not r[4])}")
