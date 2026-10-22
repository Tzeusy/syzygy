#!/usr/bin/env python3
"""Rule-6 run for the owner-pid naming and the dead-process sweep in
apps/three-surface-poc/src/test-model-fixture.ts.

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
    ('sweep-not-called', 'the first template of a file no longer sweeps',
     '  removeFixturesOfDeadProcesses();\n  const root = mkdtempSync(join(tmpdir(), `${FIXTURE_PREFIX}template-p',
     '  const root = mkdtempSync(join(tmpdir(), `${FIXTURE_PREFIX}template-p'),
    ('live-pid-removed', 'a directory whose pid is alive is removed too',
     'if (pid === undefined || ownerMayBeAlive(Number(pid))) continue;', 'if (pid === undefined) continue;'),
    ('every-error-means-dead', 'EPERM and an out-of-range pid count as dead',
     "return (error as NodeJS.ErrnoException).code !== 'ESRCH';", 'return false;'),
    ('name-without-pid-is-dead', 'a name with no pid segment is swept as pid 4194305',
     'const pid = FIXTURE_NAME_WITH_OWNER.exec(name)?.[1];', "const pid = FIXTURE_NAME_WITH_OWNER.exec(name)?.[1] ?? '4194305';"),
    ('hyphen-after-pid-dropped', 'a pid with no hyphen after it matches',
     'p(\\d+)-/;', 'p(\\d+)/;'),
    ('anchor-dropped', 'the prefix may sit inside a longer name',
     'const FIXTURE_NAME_WITH_OWNER = /^syzygy-', 'const FIXTURE_NAME_WITH_OWNER = /syzygy-'),
    ('template-form-unmatched', 'a template directory of a dead process is never swept',
     '(?:template-)?p(\\d+)-/;', 'p(\\d+)-/;'),
    ('copy-name-without-pid', 'a copy is named as before, with no pid',
     '`${FIXTURE_PREFIX}p${process.pid}-`', '`${FIXTURE_PREFIX}`'),
    ('template-name-without-pid', 'the template is named as before, with no pid',
     '`${FIXTURE_PREFIX}template-p${process.pid}-`', '`${FIXTURE_PREFIX}template-`'),
    ('removal-failure-propagates', 'a directory that cannot be removed fails the run that sweeps',
     '    try {\n      rmSync(join(directory, name), { recursive: true, force: true });\n    } catch {\n      // Left for the next run.\n    }\n',
     '    rmSync(join(directory, name), { recursive: true, force: true });\n'),
]

run = lambda *a: subprocess.run(a, cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
commit = run('git', 'rev-parse', 'HEAD')
dirty = run('git', 'status', '--porcelain', '--', SRC, TEST)
assert dirty == '', f'{SRC} and {TEST} must be committed before a rule-6 run: {dirty}'
originals = {name: (WT / name).read_text() for name in (SRC, TEST)}
digests = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in originals.items()}
report = pathlib.Path(tempfile.mkdtemp(prefix='zz-mutate-sweep-')) / 'report.json'
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
    'tool': 'mutate_sweep.py',
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
