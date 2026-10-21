#!/usr/bin/env python3
"""Apply the export-census classes to apps/three-surface-poc/src.

  self-only -> remove the `export` keyword (all overload signatures)
  test-only -> add a `// Test seam:` comment above the declaration (or its
               attached doc comment); `test-*.ts` support modules get one
               module-head comment instead
  dead, and rows the script cannot place by declaration regex -> reported,
  never edited (handled by hand)

Reads the census JSON written by export_census.py, edits files in place.
Usage: deexport.py <repo-root> <census.json> [--dry]
"""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
rows = json.load(open(sys.argv[2]))
dry = '--dry' in sys.argv
APP = 'apps/three-surface-poc/src/'

EXCLUDED = {
    APP + 'polaris.ts',  # dov.16.4 lands alone; A2/A3 own it
    APP + 'polaris-generation/public-source-screening.ts',  # syzygy-qkea.17
    APP + 'polaris-generation/source-adapter.ts',  # deleted as an orphan
}
HEAD_COMMENT = '// Test support: exports with no non-test importer are consumed by tests only, by design.\n\n'

KIND = r'(function\*?|const|let|var|class|interface|type|enum)'


def decl_re(name: str) -> re.Pattern:
    return re.compile(rf'^export\s+((?:declare\s+)?(?:abstract\s+)?(?:async\s+)?){KIND}\s+{re.escape(name)}\b', re.M)


def comment_for(kind: str, selfuses: int, entry: bool) -> str:
    if entry:
        return '// Test seam: the entry script is the only production caller; exported so a test can drive it.'
    if kind in ('interface', 'type'):
        return '// Test seam: exported type the tests name; production code uses it only inside this file.'
    if selfuses > 0:
        return '// Test seam: exported for the tests; production code reaches it only inside this file.'
    return '// Test seam: exported for the tests; no production code uses it.'


def attached_start(lines: list[str], index: int) -> int:
    """Index of the first line of the comment block directly above lines[index]."""
    i = index
    while i > 0:
        prev = lines[i - 1].strip()
        if prev.startswith(('/**', '*', '*/', '//', '/*')):
            i -= 1
            continue
        break
    return i


by_file: dict[str, list[dict]] = {}
for r in rows:
    if r['class'] in ('self-only', 'test-only', 'dead'):
        by_file.setdefault(r['file'], []).append(r)

report = {'unexported': [], 'commented': [], 'head': [], 'skipped-excluded': [], 'unplaced': [], 'dead': []}
for file, items in sorted(by_file.items()):
    path = root / file
    text = path.read_text(encoding='utf-8')
    base = file.split('/')[-1]
    support = base.startswith('test-')
    entry = base.endswith('-main.ts')
    for r in items:
        name = r['name']
        if file in EXCLUDED:
            report['skipped-excluded'].append((file, name, r['class']))
            continue
        if r['class'] == 'dead':
            report['dead'].append((file, name))
            continue
        rx = decl_re(name)
        matches = list(rx.finditer(text))
        if not matches:
            report['unplaced'].append((file, name, r['class']))
            continue
        if r['class'] == 'self-only':
            text = rx.sub(lambda m: re.sub(r'^export\s+', '', m.group(0)), text)
            report['unexported'].append((file, name))
        else:  # test-only
            if support:
                continue
            m = matches[0]
            lines = text.split('\n')
            line_index = text.count('\n', 0, m.start())
            start = attached_start(lines, line_index)
            comment = comment_for(m.group(2), r['self'], entry)
            indent = re.match(r'\s*', lines[line_index]).group(0)
            lines.insert(start, indent + comment)
            text = '\n'.join(lines)
            report['commented'].append((file, name))
    if support and any(r['class'] == 'test-only' for r in items) and file not in EXCLUDED:
        if not text.startswith('// Test support:'):
            text = HEAD_COMMENT + text
            report['head'].append(file)
    if not dry:
        path.write_text(text, encoding='utf-8')

for key, value in report.items():
    print(f'{key}: {len(value)}')
    if key in ('unplaced', 'dead', 'head'):
        for v in value:
            print('   ', v)
