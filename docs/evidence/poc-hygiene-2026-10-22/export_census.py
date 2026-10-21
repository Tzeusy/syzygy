#!/usr/bin/env python3
"""Export census for apps/three-surface-poc/src.

Method (stated, re-runnable): enumerate every tracked non-test .ts file under
the app's src/, parse its top-level export declarations with Python re, and
for each exported name count identifier-token matches (comments stripped from
every file first; string and template text kept, so a name quoted in a string
counts as a use and the sweep errs toward keeping an export) in:
  prod   - every OTHER tracked non-test code file (.ts .mts .mjs .js .cjs
           and .py) anywhere in the repository (packages, apps, scripts,
           .github); a .py file is a consumer because the governance scripts
           parse TypeScript declarations by their literal text, and its
           comments are kept (a `#` line counts as a use); .py files under
           docs/evidence/ are measurement tooling and are not consumers
  test   - every tracked *.test.ts / *.test.mjs file anywhere
  self   - uses inside the declaring file beyond its own declaration
Classes: dead (prod=0, test=0, self=0), self-only (prod=0, test=0, self>0),
test-only (prod=0, test>0), prod (prod>0).
Usage: export_census.py <repo-root> [--json out.json]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1])
out = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
files = subprocess.run(['git', 'ls-files', '-z'], cwd=root, capture_output=True, check=True).stdout.decode().split('\0')
code_ext = ('.ts', '.mts', '.mjs', '.js', '.cjs', '.py')
# Measurement tooling under docs/evidence/ names the exports it measures and is
# not a consumer of them, so its .py files are left out of the consumer set.
code = [f for f in files if f.endswith(code_ext) and not f.startswith(('node_modules/',)) and not (f.endswith('.py') and f.startswith('docs/evidence/'))]
is_test = lambda f: bool(re.search(r'\.test\.(ts|mjs|js)$', f))
text = {f: (root / f).read_text(encoding='utf-8', errors='replace') for f in code}

APP = 'apps/three-surface-poc/src/'
declared = [f for f in code if f.startswith(APP) and f.endswith('.ts') and not is_test(f)]

DECL = re.compile(
    r'^export\s+(?:declare\s+)?(?:abstract\s+)?(?:async\s+)?(?:function\*?|const|let|var|class|interface|type|enum)\s+([A-Za-z_$][\w$]*)',
    re.M,
)
LIST = re.compile(r'^export\s+(?:type\s+)?\{([^}]*)\}(?:\s+from\s+[^;]+)?;', re.M | re.S)
STAR = re.compile(r'^export\s+\*(?:\s+as\s+\w+)?\s+from\s+', re.M)


def strip_comments(src: str) -> str:
    src = re.sub(r'/\*.*?\*/', '', src, flags=re.S)
    return re.sub(r'(?m)^\s*//.*$|(?<=[;,{}()\s])//[^\n]*$', '', src)


TOKEN = re.compile(r'[A-Za-z_$][\w$]*')
RAW = '--raw' in sys.argv
tokens = {f: (text[f] if RAW or f.endswith('.py') else strip_comments(text[f])) for f in code}
token_counts = {}
for f, body in tokens.items():
    counts_f = {}
    for tok in TOKEN.findall(body):
        counts_f[tok] = counts_f.get(tok, 0) + 1
    token_counts[f] = counts_f

rows = []
star_files = []
for f in declared:
    src = text[f]
    names = [(m.group(1), m.start()) for m in DECL.finditer(src)]
    for m in LIST.finditer(src):
        for part in m.group(1).split(','):
            part = part.strip()
            if not part:
                continue
            part = re.sub(r'^type\s+', '', part)
            name = part.split(' as ')[-1].strip()
            names.append((name, m.start()))
    if STAR.search(src):
        star_files.append(f)
    for name, pos in names:
        self_hits = token_counts[f].get(name, 0) - 1
        prod = [g for g in code if g != f and not is_test(g) and name in token_counts[g]]
        tests = [g for g in code if g != f and is_test(g) and name in token_counts[g]]
        line = src.count('\n', 0, pos) + 1
        if prod:
            cls = 'prod'
        elif tests:
            cls = 'test-only'
        elif self_hits > 0:
            cls = 'self-only'
        else:
            cls = 'dead'
        rows.append({'file': f, 'name': name, 'line': line, 'class': cls, 'self': self_hits, 'prod': prod, 'tests': tests})

counts = {}
for r in rows:
    counts[r['class']] = counts.get(r['class'], 0) + 1
print(f'declaring files: {len(declared)}; star re-export files: {len(star_files)} {star_files}')
print(f'exports scanned: {len(rows)}; ' + '; '.join(f'{k}={v}' for k, v in sorted(counts.items())))
if out:
    Path(out).write_text(json.dumps(rows, indent=1) + '\n')
