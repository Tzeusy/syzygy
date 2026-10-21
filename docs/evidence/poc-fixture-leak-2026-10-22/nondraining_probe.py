#!/usr/bin/env python3
"""Run a test file whose caller drains nothing, and count what it leaves behind.

Usage: nondraining_probe.py <worktree> <base-commit> <out.json> <private-tmpdir-root>

The probe test (written to the worktree as a temporary, untracked file and removed
afterwards) calls fixtureRepoWithGit three times with an array it never drains, and
asserts in its own afterAll that all three copies still exist, which shows the
end-of-file hook runs after the file's own hooks. It runs alone under a fresh
private TMPDIR in four trees and records the syzygy-poc-surface-fixture-*
directories left in that TMPDIR:
  base     test-model-fixture.ts as of <base-commit> (the helper before this change)
  head     the worktree as committed
  mutant   head with the copy's registration removed (the first rule-6 mutant)
  head-2   head again, after the mutant is restored (the byte-for-byte restore)
test-model-fixture.ts is restored byte for byte afterwards and its digest checked.
"""
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys

WT, BASE, OUT, ROOT = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve(), pathlib.Path(sys.argv[4]).resolve()
SRC = 'apps/three-surface-poc/src/test-model-fixture.ts'
PROBE = 'apps/three-surface-poc/src/zz-nondraining-probe.test.ts'
REGISTRATION = '  cleanups.push(root);\n  removeAtEndOfFile(root);\n'
PROBE_TEXT = """import { existsSync } from 'node:fs';
import { afterAll, describe, expect, it } from 'vitest';

import { fixtureRepoWithGit } from './test-model-fixture.js';

// A caller that never drains the array it hands over.
const ignored: string[] = [];

describe('a caller that drains nothing', () => {
  it('makes three copies', () => {
    for (let index = 0; index < 3; index += 1) fixtureRepoWithGit(ignored);
    expect(ignored).toHaveLength(3);
  });
  afterAll(() => {
    expect(ignored.every((directory) => existsSync(directory))).toBe(true);
  });
});
"""
git = lambda *a: subprocess.run(['git', *a], cwd=WT, capture_output=True, text=True, check=True).stdout
commit = git('rev-parse', 'HEAD').strip()
assert git('status', '--porcelain', '--', SRC).strip() == '', f'{SRC} must be committed'
original = (WT / SRC).read_text()
digest = hashlib.sha256(original.encode()).hexdigest()
trees = {
    'base': git('show', f'{BASE}:{SRC}'),
    'head': original,
    'mutant': original.replace(REGISTRATION, '  cleanups.push(root);\n', 1),
    'head-2': original,
}
assert trees['mutant'] != original, 'the registration fragment must occur'
results = {}
try:
    (WT / PROBE).write_text(PROBE_TEXT)
    for name, text in trees.items():
        tmp = ROOT / name
        shutil.rmtree(tmp, ignore_errors=True)
        tmp.mkdir(parents=True)
        (WT / SRC).write_text(text)
        proc = subprocess.run(['npx', 'vitest', 'run', PROBE, '--project', '@syzygy/three-surface-poc-app'], cwd=WT, capture_output=True, text=True, env={**os.environ, 'TMPDIR': str(tmp)})
        left = sorted(p.name for p in tmp.iterdir() if p.name.startswith('syzygy-poc-surface-fixture-'))
        summary = [line.strip() for line in (proc.stdout + proc.stderr).splitlines() if line.strip().startswith(('Test Files', 'Tests '))]
        results[name] = {
            'exit': proc.returncode,
            'summary': summary,
            'copiesLeft': sum(1 for n in left if not n.startswith('syzygy-poc-surface-fixture-template-')),
            'templatesLeft': sum(1 for n in left if n.startswith('syzygy-poc-surface-fixture-template-')),
        }
        print(name, results[name], flush=True)
        shutil.rmtree(tmp, ignore_errors=True)
finally:
    (WT / SRC).write_text(original)
    (WT / PROBE).unlink(missing_ok=True)
assert hashlib.sha256((WT / SRC).read_text().encode()).hexdigest() == digest
OUT.write_text(json.dumps({
    'tool': 'nondraining_probe.py',
    'treeCommit': commit,
    'baseCommit': BASE,
    'sha256OfHelperAtCommit': digest,
    'probeTest': PROBE_TEXT,
    'mutantFragment': {'old': REGISTRATION, 'new': '  cleanups.push(root);\n'},
    'results': results,
}, indent=1) + '\n')
