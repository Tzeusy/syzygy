#!/usr/bin/env python3
"""Rule-6 run for dist_compare.py: perturb a copy of the head's built output and
require the comparison to fail where it should.

Usage: mutate_dist_compare.py <base-tree> <head-tree> <tree-commit> <out.json>

The copies hold only the five projects' dist directories. The control (the
unperturbed copies, with the two expectations of this change) must exit 0. Each
perturbation edits the head copy, or its expectation, and must exit 1. Records,
per perturbation, what was changed and the comparison's first output line.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
BASE, HEAD = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
TREE_COMMIT, OUT = sys.argv[3], pathlib.Path(sys.argv[4]).resolve()
PROJECTS = ['packages/cap1-core', 'packages/cap1-daemon', 'packages/three-surface-poc-core', 'packages/polaris-generation-core', 'apps/three-surface-poc']
EXPECT = ['apps/three-surface-poc/dist/poc-main.js:3', 'apps/three-surface-poc/dist/poc-main.d.ts:2']
POC_MAIN = 'apps/three-surface-poc/dist/poc-main.js'


def copy(tree: pathlib.Path, into: pathlib.Path) -> None:
    for project in PROJECTS:
        shutil.copytree(tree / project / 'dist', into / project / 'dist', ignore=shutil.ignore_patterns('*.map', '*.tsbuildinfo'))


def compare(base: pathlib.Path, head: pathlib.Path, expect: list[str]):
    proc = subprocess.run([sys.executable, str(HERE / 'dist_compare.py'), str(base), '0' * 40, str(head), '1' * 40, str(head / 'out.json'), '--expect', *expect], capture_output=True, text=True)
    return proc.returncode, (proc.stdout.strip() or proc.stderr.strip().splitlines()[-1])


def append_to(relative: str, text: str):
    def apply(head: pathlib.Path):
        with (head / relative).open('a') as handle:
            handle.write(text)
    return apply


def delete(relative: str):
    return lambda head: (head / relative).unlink()


def replace_in(relative: str, old: str, new: str):
    def apply(head: pathlib.Path):
        path = head / relative
        text = path.read_text()
        assert text.count(old) == 1, f'{old!r} not found exactly once in {relative}'
        path.write_text(text.replace(old, new, 1))
    return apply


CASES = [
    ('an unrelated shipped file gains a line', append_to('apps/three-surface-poc/dist/routes.js', '// zz\n'), EXPECT),
    ('a shipped file is missing from the head', delete('apps/three-surface-poc/dist/launcher.js'), EXPECT),
    ('the expected file changes one line more than expected', append_to(POC_MAIN, '// zz\n'), EXPECT),
    ('the expected file is identical (the change is absent)', lambda head: shutil.copy(BASE / POC_MAIN, head / POC_MAIN), EXPECT),
    ('a core project file changes', append_to('packages/three-surface-poc-core/dist/index.js', '// zz\n'), EXPECT),
    ('a declaration file changes', append_to('apps/three-surface-poc/dist/cli.d.ts', '// zz\n'), EXPECT),
]

results = []
with tempfile.TemporaryDirectory(prefix='zz-mutate-dist-') as name:
    root = pathlib.Path(name)
    base, head = root / 'base', root / 'head'
    copy(BASE, base)
    copy(HEAD, head)
    control_code, control_line = compare(base, head, EXPECT)
    assert control_code == 0, f'the control must hold: {control_line}'
    for description, apply, expect in CASES:
        shutil.rmtree(head)
        copy(HEAD, head)
        apply(head)
        code, line = compare(base, head, expect)
        results.append({'perturbation': description, 'exit': code, 'outcome': 'killed' if code == 1 else 'SURVIVED', 'firstOutputLine': line[:300]})
        print(description, results[-1]['outcome'], flush=True)
OUT.write_text(json.dumps({
    'tool': 'mutate_dist_compare.py',
    'treeCommit': TREE_COMMIT,
    'control': {'exit': control_code, 'firstOutputLine': control_line[:300], 'holds': control_code == 0},
    'perturbations': len(CASES),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['perturbation'] for r in results if r['outcome'] != 'killed'])
