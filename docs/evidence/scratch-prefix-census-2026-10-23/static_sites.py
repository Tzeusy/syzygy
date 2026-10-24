#!/usr/bin/env python3
"""Every line of a tracked file that creates, or builds a path in, the system temp directory, with its literal prefix where there is one.

Usage: static_sites.py <worktree> <commit> <out.json>

Population: every blob of <commit> (git ls-tree -r -z, read through git cat-file --batch, so the worktree's own files are not
read) whose name ends .ts .mts .cts .js .mjs .cjs .py or .sh. A site is a line that matches at least one of PATTERNS below (the
exact regexes, published so the count can be re-derived); a line matching several is one site with several kinds:
  js-mkdtemp       mkdtemp( or mkdtempSync(
  js-tmpdir        tmpdir()  (any use of Node's temp directory: join(tmpdir(), ...), a lock path, a log path)
  py-tempfile      tempfile.mkdtemp( / TemporaryDirectory( / NamedTemporaryFile( / mkstemp( / gettempdir(
  sh-mktemp        the word mktemp
  literal-tmp-path a string that starts with /tmp/
A site's `literal` is the first string literal on the line that ends in `-` or `_` and is followed by a closing quote or `${`
(the shape of a prefix), else None; a None site builds its prefix some other way and is attributed by a run's trace or by hand.
The census over-counts on purpose (a line that only reads the temp directory is a site); it is the denominator for "which
files that touch the temp directory did the runs reach".
"""
import json
import pathlib
import re
import subprocess
import sys

WT, COMMIT, OUT = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve()
assert re.fullmatch(r'[0-9a-f]{40}', COMMIT), 'give the full 40-hex commit'
PATTERNS = {
    'js-mkdtemp': r'\bmkdtemp(?:Sync)?\(',
    'js-tmpdir': r'\btmpdir\(\)',
    'py-tempfile': r'\btempfile\.(?:mkdtemp|TemporaryDirectory|NamedTemporaryFile|mkstemp|gettempdir)\(',
    'sh-mktemp': r'\bmktemp\b',
    'literal-tmp-path': r'''['"`]/tmp/''',
}
COMPILED = {k: re.compile(v) for k, v in PATTERNS.items()}
LITERAL = re.compile(r'''['"`]([A-Za-z0-9._]+[-_])(?=['"`]|\$\{)''')
SUFFIXES = ('.ts', '.mts', '.cts', '.js', '.mjs', '.cjs', '.py', '.sh')


def blobs(names: list) -> dict:
    """Read blobs of COMMIT through one git cat-file --batch process."""
    ran = subprocess.run(['git', 'cat-file', '--batch'], cwd=WT, input=''.join(f'{COMMIT}:{n}\n' for n in names).encode(), capture_output=True, check=True)
    data, position, found = ran.stdout, 0, {}
    for name in names:
        end = data.index(b'\n', position)
        header = data[position:end].split()
        assert header[1] == b'blob', (name, header)
        size = int(header[2])
        found[name] = data[end + 1:end + 1 + size]
        position = end + 1 + size + 1
    assert position == len(data)
    return found


listing = subprocess.run(['git', 'ls-tree', '-r', '-z', '--name-only', COMMIT], cwd=WT, capture_output=True, text=True, check=True).stdout.split('\0')
names = [n for n in listing if n.endswith(SUFFIXES)]
rows: dict = {}
for name, raw in blobs(names).items():
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError:
        continue
    sites = []
    for number, line in enumerate(text.splitlines(), 1):
        kinds = [kind for kind, pattern in COMPILED.items() if pattern.search(line)]
        if kinds:
            literal = LITERAL.search(line)
            sites.append({'line': number, 'kinds': kinds, 'literal': literal.group(1) if literal else None})
    if sites:
        rows[name] = sites
by_tree: dict = {}
for name, sites in rows.items():
    entry = by_tree.setdefault(name.split('/')[0], {'files': 0, 'sites': 0})
    entry['files'] += 1
    entry['sites'] += len(sites)
by_kind = {kind: sum(1 for sites in rows.values() for s in sites if kind in s['kinds']) for kind in PATTERNS}
record = {'tool': 'static_sites.py', 'treeCommit': COMMIT, 'patterns': PATTERNS, 'filePopulation': {'suffixes': list(SUFFIXES), 'blobsRead': len(names)},
          'filesWithASite': len(rows), 'sites': sum(len(v) for v in rows.values()), 'sitesByKind': by_kind, 'byTree': dict(sorted(by_tree.items())), 'files': rows}
OUT.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({k: record[k] for k in ('filePopulation', 'filesWithASite', 'sites', 'sitesByKind', 'byTree')}))
