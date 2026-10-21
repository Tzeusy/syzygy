#!/usr/bin/env python3
"""Run the built POC entry in every invocation form against a base tree and a
head tree and compare stdout, stderr and exit code.

Usage: invocation_forms.py <base-tree> <head-tree> <out.json>

Each tree must be a built checkout with its own node_modules (a symlinked
node_modules resolves @syzygy/* into the linked tree). No observed repository
is read: the arguments name a path that does not exist, an empty scratch
directory (the P1 gate rejects it before any observation) or nothing.

Forms (cwd is the tree root; the entry is never given a daemon to serve):
  js        node apps/three-surface-poc/dist/main.js
  bare      node apps/three-surface-poc/dist/main          (no extension)
  package   node apps/three-surface-poc                    (package.json "main")
  symlink   node <scratch>/entry-link.mjs -> dist/main.js
  import    node --input-type=module -e "await import(<dist/main.js>)"
  root      node --input-type=module -e "await import('@syzygy/three-surface-poc-app')"
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

base, head, out = (Path(a).resolve() for a in sys.argv[1:4])
ENTRY = 'apps/three-surface-poc/dist/main.js'
scratch = Path(tempfile.mkdtemp(prefix='zz-invocation-forms-'))
empty_repo = scratch / 'empty-repo'
empty_repo.mkdir()
missing = scratch / 'no' / 'such' / 'repo'

ARGS = {
    'help': ['--help'],
    'no-arguments': [],
    'unknown-argument': ['--bogus'],
    'unreadable-repo': ['--repo', str(missing)],
    'rejected-binding': ['--repo', str(empty_repo)],
}


def command(tree: Path, form: str, args: list[str]) -> list[str]:
    if form == 'js':
        return ['node', ENTRY, *args]
    if form == 'bare':
        return ['node', ENTRY.removesuffix('.js'), *args]
    if form == 'package':
        return ['node', 'apps/three-surface-poc', *args]
    if form == 'symlink':
        link = scratch / f'entry-link-{hashlib.sha256(str(tree).encode()).hexdigest()[:8]}.mjs'
        if not link.exists() and not link.is_symlink():
            link.symlink_to(tree / ENTRY)
        return ['node', str(link), *args]
    if form == 'import':
        return ['node', '--input-type=module', '-e', f"await import({json.dumps((tree / ENTRY).as_uri())})", '--', 'placeholder', *args]
    if form == 'root':
        return ['node', '--input-type=module', '-e', "await import('@syzygy/three-surface-poc-app')", '--', 'placeholder', *args]
    raise SystemExit(form)


def run(tree: Path, form: str, args: list[str]) -> dict:
    proc = subprocess.run(command(tree, form, args), cwd=tree, capture_output=True, text=True, timeout=60, stdin=subprocess.DEVNULL)

    def mask(text: str) -> str:
        return text.replace(str(scratch), '<SCRATCH>').replace(str(tree), '<TREE>')

    return {'exit': proc.returncode, 'stdout': mask(proc.stdout), 'stderr': mask(proc.stderr)}


rows = []
for form in ('js', 'bare', 'package', 'symlink', 'import', 'root'):
    for name, args in ARGS.items():
        # Importing runs the entry with the importing process's own argv. With
        # `-e`, argv[1] is the first word after `--`, so the import forms put a
        # placeholder there and the entry sees the arguments from argv[2].
        b, h = run(base, form, args), run(head, form, args)
        rows.append({'form': form, 'arguments': name, 'base': b, 'head': h, 'identical': b == h})

signatures = {json.dumps(r['head'], sort_keys=True) for r in rows}
record = {
    'tool': 'invocation_forms.py',
    'toolSha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'trees': {
        'base': {'commit': subprocess.run(['git', '-C', str(base), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()},
        'head': {'commit': subprocess.run(['git', '-C', str(head), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()},
    },
    'node': subprocess.run(['node', '--version'], capture_output=True, text=True).stdout.strip(),
    'entry': ENTRY,
    'pairs': len(rows),
    'identicalPairs': sum(1 for r in rows if r['identical']),
    'distinctHeadOutputs': len(signatures),
    'rows': rows,
}
out.write_text(json.dumps(record, indent=1) + '\n')
print(f"pairs={record['pairs']} identical={record['identicalPairs']} distinctHeadOutputs={record['distinctHeadOutputs']}")
for r in rows:
    if not r['identical']:
        print('DIFFERS', r['form'], r['arguments'], 'base', r['base']['exit'], 'head', r['head']['exit'])
