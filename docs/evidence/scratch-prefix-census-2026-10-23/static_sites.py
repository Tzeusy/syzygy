#!/usr/bin/env python3
"""Every place a tracked file creates a scratch entry in the temp directory, by pattern, with its literal prefix where there is one.

Usage: static_sites.py <worktree> <commit> <out.json>

Population: every tracked file (git ls-files -z at <commit>, which must be HEAD of <worktree>) whose name ends .ts .mts .cts .js .mjs
.cjs .py or .sh, grouped by its first path component. A site is a line that matches one of these patterns (PATTERNS below holds
the exact regexes; they are published here so the count can be re-derived):
  js-mkdtemp         mkdtemp(  or  mkdtempSync(
  js-tmpdir-entry    a mkdir / writeFile / symlink / copyFile call with tmpdir() in its first argument (a fixed or computed name directly in the temp directory)
  py-mkdtemp         tempfile.mkdtemp(  /  tempfile.TemporaryDirectory(  /  tempfile.NamedTemporaryFile(  /  tempfile.mkstemp(
A site's `literal` is the first string literal on the line that ends in `-` or `_` (the shape of a prefix), else None; a None site
passes its prefix as a variable and is attributed by the run's trace, not here. This tool reads files only.
"""
import json
import pathlib
import re
import subprocess
import sys

WT, COMMIT, OUT = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve()
git = lambda *a: subprocess.run(['git', *a], cwd=WT, capture_output=True, text=True, check=True).stdout
assert re.fullmatch(r'[0-9a-f]{40}', COMMIT) and git('rev-parse', 'HEAD').strip() == COMMIT, 'the worktree must be at the full <commit>'
PATTERNS = {
    'js-mkdtemp': r'\bmkdtemp(?:Sync)?\(',
    'js-tmpdir-entry': r'\b(?:mkdirSync|mkdir|writeFileSync|writeFile|symlinkSync|symlink|copyFileSync|copyFile|cpSync|cp)\([^;]*\btmpdir\(\)',
    'py-mkdtemp': r'\btempfile\.(?:mkdtemp|TemporaryDirectory|NamedTemporaryFile|mkstemp)\(',
}
COMPILED = {k: re.compile(v) for k, v in PATTERNS.items()}
LITERAL = re.compile(r'''['"]([A-Za-z0-9._]+[-_])['"]''')
SUFFIXES = ('.ts', '.mts', '.cts', '.js', '.mjs', '.cjs', '.py', '.sh')
files = [f for f in git('ls-files', '-z').split('\0') if f.endswith(SUFFIXES)]
rows: dict = {}
for name in files:
    try:
        text = (WT / name).read_text()
    except (OSError, UnicodeDecodeError):
        continue
    sites = []
    for number, line in enumerate(text.splitlines(), 1):
        for kind, pattern in COMPILED.items():
            if pattern.search(line):
                literal = LITERAL.search(line)
                sites.append({'line': number, 'kind': kind, 'literal': literal.group(1) if literal else None})
    if sites:
        rows[name] = sites
by_tree: dict = {}
for name, sites in rows.items():
    tree = name.split('/')[0]
    entry = by_tree.setdefault(tree, {'files': 0, 'sites': 0})
    entry['files'] += 1
    entry['sites'] += len(sites)
record = {'tool': 'static_sites.py', 'treeCommit': COMMIT, 'patterns': PATTERNS, 'filePopulation': {'suffixes': list(SUFFIXES), 'trackedFiles': len(files)},
          'filesWithASite': len(rows), 'sites': sum(len(v) for v in rows.values()), 'byTree': dict(sorted(by_tree.items())), 'files': rows}
OUT.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({k: record[k] for k in ('filePopulation', 'filesWithASite', 'sites', 'byTree')}))
