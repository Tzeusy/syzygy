#!/usr/bin/env python3
"""Rule-6 run for the end-of-file teardown in apps/three-surface-poc/src/test-model-fixture.ts.

Usage: mutate_teardown.py <worktree> <out.json> <private-tmpdir>

Each mutant edits test-model-fixture.ts in <worktree>; test-model-fixture.test.ts
runs ALONE under a private TMPDIR (so a mutant that leaks, leaks there and not
into a shared /tmp), and the file is restored byte for byte afterwards. A control
(the unmutated tree) runs first and must pass. A mutant is `killed` when the test
file exits non-zero. A fragment that does not occur exactly once in the file is
recorded as FRAGMENT-COUNT-n and never guessed.

Records, per mutant: the old and new fragment, the command, the commit the run was
made at and every failing test with its first error line (from vitest's JSON
reporter). The tree must be committed at the two files before the run.
"""
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

WT, OUT, PRIVATE_TMP = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve(), pathlib.Path(sys.argv[3]).resolve()
SRC = 'apps/three-surface-poc/src/test-model-fixture.ts'
TEST = 'apps/three-surface-poc/src/test-model-fixture.test.ts'

MUTANTS = [
    ('copy-not-registered', 'the copy is never registered, only the template',
     '  cleanups.push(root);\n  removeAtEndOfFile(root);\n', '  cleanups.push(root);\n'),
    ('set-not-cleared', 'the set keeps its roots after the teardown, so the next file registers nothing',
     '    removeWhenFileEnds.clear();\n', ''),
    ('template-not-reset', 'the next copy comes from a template the teardown removed',
     '    template = undefined;\n  };\n', '  };\n'),
    ('teardown-per-copy', 'every copy registers its own teardown and exit listener',
     '  if (!first) return;\n', ''),
    ('only-first-removed', 'the teardown removes the first registered root only',
     'for (const owned of removeWhenFileEnds) rmSync(', 'for (const owned of [...removeWhenFileEnds].slice(0, 1)) rmSync('),
    ('template-kept', 'the teardown removes copies but not the template',
     'for (const owned of removeWhenFileEnds) rmSync(owned, { recursive: true, force: true });',
     "for (const owned of removeWhenFileEnds) if (!owned.includes('-template-')) rmSync(owned, { recursive: true, force: true });"),
    ('hook-bypassed', 'the teardown always waits for process exit, never the per-file hook',
     'if (afterTestFile === undefined) process.once(\'exit\', remove);\n  else afterTestFile(remove);',
     "process.once('exit', remove);"),
    ('exit-branch-dropped', 'outside Vitest nothing is registered at all',
     "if (afterTestFile === undefined) process.once('exit', remove);\n  else afterTestFile(remove);",
     'if (afterTestFile !== undefined) afterTestFile(remove);'),
]

run = lambda *a: subprocess.run(a, cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
commit = run('git', 'rev-parse', 'HEAD')
dirty = run('git', 'status', '--porcelain', '--', SRC, TEST)
assert dirty == '', f'{SRC} and {TEST} must be committed before a rule-6 run: {dirty}'
originals = {name: (WT / name).read_text() for name in (SRC, TEST)}
digests = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in originals.items()}
report = pathlib.Path(tempfile.mkdtemp(prefix='zz-mutate-teardown-')) / 'report.json'
command = ['npx', 'vitest', 'run', TEST, '--project', '@syzygy/three-surface-poc-app', '--reporter=json', f'--outputFile={report}']


def vitest() -> tuple[int, int, list[dict], int]:
    shutil.rmtree(PRIVATE_TMP, ignore_errors=True)
    PRIVATE_TMP.mkdir(parents=True)
    report.unlink(missing_ok=True)
    proc = subprocess.run(command, cwd=WT, capture_output=True, text=True, env={**os.environ, 'TMPDIR': str(PRIVATE_TMP)})
    data = json.loads(report.read_text()) if report.exists() else {'testResults': []}
    cases = [a for suite in data['testResults'] for a in suite['assertionResults']]
    failing = [{'test': a['fullName'], 'firstErrorLine': (a['failureMessages'][0].splitlines() or [''])[0] if a['failureMessages'] else ''}
               for a in cases if a['status'] == 'failed']
    leaked = sum(1 for p in PRIVATE_TMP.iterdir() if p.name.startswith('syzygy-poc-surface-fixture-'))
    return proc.returncode, len(cases), failing, leaked


results = []
control = {}
try:
    exit_code, total, failing, leaked = vitest()
    control = {'exit': exit_code, 'testsRun': total, 'failing': failing, 'fixtureDirectoriesLeftInPrivateTmpdir': leaked, 'holds': exit_code == 0 and total > 0 and leaked == 0}
    print('control', control['holds'], total, leaked, flush=True)
    assert control['holds'], 'the unmutated tree must pass test-model-fixture.test.ts and leave no fixture directory'
    for name, meaning, old, new in MUTANTS:
        text = originals[SRC]
        if text.count(old) != 1:
            results.append({'id': name, 'meaning': meaning, 'old': old, 'new': new, 'outcome': f'FRAGMENT-COUNT-{text.count(old)}'})
            print(name, results[-1]['outcome'], flush=True)
            continue
        (WT / SRC).write_text(text.replace(old, new, 1))
        try:
            exit_code, total, failing, leaked = vitest()
        finally:
            (WT / SRC).write_text(text)
        results.append({'id': name, 'meaning': meaning, 'old': old, 'new': new, 'exit': exit_code, 'outcome': 'killed' if exit_code != 0 else 'SURVIVED',
                        'testsRun': total, 'failing': failing, 'fixtureDirectoriesLeftInPrivateTmpdir': leaked})
        print(name, results[-1]['outcome'], len(failing), flush=True)
finally:
    for name, text in originals.items():
        (WT / name).write_text(text)
    shutil.rmtree(PRIVATE_TMP, ignore_errors=True)
for name, text in originals.items():
    assert hashlib.sha256((WT / name).read_text().encode()).hexdigest() == digests[name]
OUT.write_text(json.dumps({
    'tool': 'mutate_teardown.py',
    'testFile': TEST,
    'command': ' '.join(command[:6]),
    'treeCommit': commit,
    'sha256AtCommit': digests,
    'control': control,
    'mutants': len(MUTANTS),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['id'] for r in results if r['outcome'] != 'killed'])
