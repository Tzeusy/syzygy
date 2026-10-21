#!/usr/bin/env python3
"""Module-level importer sweep for apps/three-surface-poc/src.

For every tracked non-test .ts module under the app src/, list the tracked
non-test code files (.ts .mts .mjs .js .cjs, repository-wide) whose comment-
stripped text contains an import/export-from/dynamic-import specifier resolving
to it (specifier './x.js' or '../x.js' or the file's package path), plus the
tracked test files that import it. A module with no non-test importer is an
orphan candidate; for *-main.ts entry modules the sweep also lists references
by basename in package.json scripts, scripts/, .github/ and docs/.
Usage: orphans.py <repo-root>
"""
import re
import subprocess
import sys
from pathlib import PurePosixPath, Path

root = Path(sys.argv[1])
files = subprocess.run(['git', 'ls-files', '-z'], cwd=root, capture_output=True, check=True).stdout.decode().split('\0')
code = [f for f in files if f.endswith(('.ts', '.mts', '.mjs', '.js', '.cjs'))]
is_test = lambda f: bool(re.search(r'\.test\.(ts|mjs|js)$', f))
text = {f: (root / f).read_text(encoding='utf-8', errors='replace') for f in code}
APP = 'apps/three-surface-poc/src/'
modules = [f for f in code if f.startswith(APP) and f.endswith('.ts') and not is_test(f)]

SPEC = re.compile(r"""(?:from\s+|import\s*\(\s*|import\s+)['"]([^'"]+)['"]""")
importers = {m: {'prod': set(), 'test': set()} for m in modules}


def resolve(src_file, spec):
    if not spec.startswith('.'):
        return None
    base = PurePosixPath(src_file).parent
    target = (base / spec)
    parts = []
    for part in target.parts:
        if part == '..':
            if parts:
                parts.pop()
        elif part != '.':
            parts.append(part)
    p = '/'.join(parts)
    p = re.sub(r'\.(m?js)$', '', p)
    for ext in ('.ts', '.mts'):
        if p + ext in importers:
            return p + ext
    return None


for f in code:
    for spec in SPEC.findall(text[f]):
        m = resolve(f, spec)
        if m and m != f:
            importers[m]['test' if is_test(f) else 'prod'].add(f)

# package.json export paths into the app's dist
pkg = (root / 'apps/three-surface-poc/package.json').read_text()
for m in modules:
    rel = m[len(APP):-3]
    if f'./dist/{rel}.js' in pkg:
        importers[m]['prod'].add('apps/three-surface-poc/package.json')

others = [f for f in files if f.startswith(('scripts/', '.github/', 'docs/', 'package.json', 'PROJECT-STATUS.md', 'README.md', 'AGENTS.md')) or f == 'package.json']
other_text = {f: (root / f).read_text(encoding='utf-8', errors='replace') for f in others if not f.startswith('docs/reviews/') and not f.startswith('docs/evidence/')}
root_pkg = (root / 'package.json').read_text()

print('module | prod importers | test importers | (entry refs)')
orph = []
for m in modules:
    p = importers[m]['prod']
    t = importers[m]['test']
    refs = []
    if m.endswith('-main.ts'):
        base = PurePosixPath(m).name[:-3]
        if base + '.js' in root_pkg or base in root_pkg:
            refs.append('package.json')
        refs += [f for f, s in other_text.items() if (base + '.js' in s or '/' + base in s) and f != 'package.json'][:3]
    if not p:
        orph.append(m)
        print(f"{m[len(APP):]:55} prod=0 test={len(t)} refs={refs}")
print(f'# modules: {len(modules)}; with no non-test importer: {len(orph)}')
