#!/usr/bin/env python3
"""Compare the built output of two trees, file by file.

Usage: dist_compare.py <base-tree> <base-commit> <head-tree> <head-commit> <out.json> [--expect <path>:<n> ...]

Population: every `.js` and `.d.ts` file under `dist/` of the five projects the
POC build covers (packages/cap1-core, packages/cap1-daemon,
packages/three-surface-poc-core, packages/polaris-generation-core,
apps/three-surface-poc), source maps and tsbuildinfo excluded. Test files
(`*.test.js`, `*.test.d.ts`) are counted apart: they are not shipped output.
Both trees must have been built from clean (`npm run build:poc` runs
`tsc -b --force`). The record lists, for the shipped files, how many were
compared, which exist in one tree only, and which differ, with the differing
lines of each (a line-by-line diff, `-` base and `+` head).
`--expect path:n` asserts that the shipped file at `path` has exactly n changed
lines (added plus removed); the exit status is 1 when any expectation fails, when
a shipped file exists in one tree only, or when a shipped file differs that no
expectation names.
"""
import difflib
import hashlib
import json
import pathlib
import sys

PROJECTS = ['packages/cap1-core', 'packages/cap1-daemon', 'packages/three-surface-poc-core', 'packages/polaris-generation-core', 'apps/three-surface-poc']
args = sys.argv[1:]
expect = {}
if '--expect' in args:
    at = args.index('--expect')
    for token in args[at + 1:]:
        path, count = token.rsplit(':', 1)
        expect[path] = int(count)
    args = args[:at]
base_tree, base_commit, head_tree, head_commit, out = pathlib.Path(args[0]), args[1], pathlib.Path(args[2]), args[3], pathlib.Path(args[4])


def files(tree: pathlib.Path) -> dict[str, pathlib.Path]:
    found = {}
    for project in PROJECTS:
        root = tree / project / 'dist'
        for path in sorted(root.rglob('*')):
            if path.is_file() and (path.name.endswith('.js') or path.name.endswith('.d.ts')):
                found[str(path.relative_to(tree))] = path
    return found


b, h = files(base_tree), files(head_tree)
is_test = lambda name: '.test.' in name.rsplit('/', 1)[-1]
shipped = sorted(name for name in set(b) | set(h) if not is_test(name))
tests = sorted(name for name in set(b) | set(h) if is_test(name))
only_one = [name for name in shipped if (name in b) != (name in h)]
differing = []
for name in shipped:
    if name in b and name in h and b[name].read_bytes() != h[name].read_bytes():
        changed = [line for line in difflib.unified_diff(b[name].read_text().splitlines(), h[name].read_text().splitlines(), lineterm='', n=0) if line[:1] in '+-' and line[:3] not in ('+++', '---')]
        differing.append({'file': name, 'changedLines': len(changed), 'lines': changed})
unexpected = [d['file'] for d in differing if d['file'] not in expect]
wrong_count = [d['file'] for d in differing if d['file'] in expect and d['changedLines'] != expect[d['file']]]
missing = [name for name in expect if name not in {d['file'] for d in differing}]
record = {
    'tool': 'dist_compare.py',
    'base': {'treeCommit': base_commit},
    'head': {'treeCommit': head_commit},
    'projects': PROJECTS,
    'shippedFilesBase': sum(1 for n in b if not is_test(n)),
    'shippedFilesHead': sum(1 for n in h if not is_test(n)),
    'shippedFilesCompared': len(shipped) - len(only_one),
    'shippedFilesInOnlyOneTree': only_one,
    'shippedFilesDiffering': len(differing),
    'differing': differing,
    'expected': expect,
    'unexpectedDifferences': unexpected,
    'differencesWithAnotherChangedLineCount': wrong_count,
    'expectedButIdentical': missing,
    'testFilesCompared': len(tests),
    'testFilesDiffering': [n for n in tests if n in b and n in h and b[n].read_bytes() != h[n].read_bytes()],
    'testFilesInOnlyOneTree': [n for n in tests if (n in b) != (n in h)],
}
out.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({k: record[k] for k in ('shippedFilesCompared', 'shippedFilesInOnlyOneTree', 'shippedFilesDiffering', 'unexpectedDifferences', 'differencesWithAnotherChangedLineCount', 'expectedButIdentical', 'testFilesCompared')}))
sys.exit(0 if not only_one and not unexpected and not wrong_count and not missing else 1)
