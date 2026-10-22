#!/usr/bin/env python3
"""Rule-6 run for the owner-pid naming and the dead-process sweep of the POC surface fixtures.

Usage: mutate_sweep.py <worktree> <out.json> <private-tmpdir>

Each mutant is a list of (file, old, new) edits to the sources below; the two test files run
ALONE under a private TMPDIR (so a mutant that leaks, leaks there and not into a shared /tmp,
and the app project's global setup sweeps that directory and nothing else), and every edited
file is restored byte for byte afterwards. A control (the unmutated tree) runs first and must
pass and leave no fixture directory. A mutant is `killed` when the run exits non-zero. A
fragment that does not occur exactly once in its file is recorded as FRAGMENT-COUNT-n and never
guessed.

Records, per mutant: the edits (old and new fragments), the command, the commit the run was
made at and every failing test with its first error line (from vitest's JSON reporter). The
edited files and the two test files must be committed before the run.
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
FD = 'apps/three-surface-poc/src/fixture-directories.ts'
GS = 'apps/three-surface-poc/src/test-fixture-sweep.global-setup.ts'
TM = 'apps/three-surface-poc/src/test-model-fixture.ts'
VC = 'vitest.config.ts'
TESTS = ['apps/three-surface-poc/src/fixture-directories.test.ts', 'apps/three-surface-poc/src/test-model-fixture.test.ts']
GLOBAL_SETUP_LINE = "          // Once per run: removes the fixture directories of killed runs (syzygy-bpyt.4.10).\n          globalSetup: [fileURLToPath(new URL('./apps/three-surface-poc/src/test-fixture-sweep.global-setup.ts', import.meta.url))],\n"
TRY = ("    try {\n      const stat = lstatSync(entry);\n      if (stat.isDirectory() && (user === undefined || stat.uid === user)) rmSync(entry, { recursive: true, force: true });\n"
       "    } catch {\n      // Left for the next run.\n    }\n")
GUARD = 'if (stat.isDirectory() && (user === undefined || stat.uid === user)) rmSync('
DECIDE = 'if (owner === null || owner[2] !== namespace || ownerMayBeAlive(Number(owner[1]))) continue;'
LIST = "  let names: string[];\n  try {\n    names = readdirSync(directory);\n  } catch {\n    return;\n  }\n"

MUTANTS = [
    ('live-pid-removed', 'a directory whose pid is alive is removed too',
     [(FD, DECIDE, 'if (owner === null || owner[2] !== namespace) continue;')]),
    ('foreign-namespace-swept', 'a dead pid from another PID namespace is judged by this namespace and removed (review round 1, F1)',
     [(FD, DECIDE, 'if (owner === null || ownerMayBeAlive(Number(owner[1]))) continue;')]),
    ('every-error-means-dead', 'EPERM and an out-of-range pid count as dead',
     [(FD, "return (error as NodeJS.ErrnoException).code !== 'ESRCH';", 'return false;')]),
    ('name-without-pid-is-dead', 'a name with no pid segment is swept as pid 4194305',
     [(FD, 'const owner = FIXTURE_NAME_WITH_OWNER.exec(name);', "const owner = FIXTURE_NAME_WITH_OWNER.exec(name) ?? [name, '4194305', namespace];")]),
    ('hyphen-after-namespace-dropped', 'a namespace with no hyphen after it matches',
     [(FD, 'p(\\d+)-n(\\d+)-/;', 'p(\\d+)-n(\\d+)/;')]),
    ('anchor-dropped', 'the prefix may sit inside a longer name',
     [(FD, 'const FIXTURE_NAME_WITH_OWNER = /^syzygy-', 'const FIXTURE_NAME_WITH_OWNER = /syzygy-')]),
    ('template-form-unmatched', 'a template directory of a dead process is never swept',
     [(FD, '(?:template-)?p(\\d+)-n(\\d+)-/;', 'p(\\d+)-n(\\d+)-/;')]),
    ('is-directory-guard-dropped', 'a regular file or a symlink with a dead-pid name is removed, not only a directory (review round 1, F3)',
     [(FD, GUARD, 'if (user === undefined || stat.uid === user) rmSync(')]),
    ('uid-guard-dropped', 'a directory of another user with a dead-pid name is entered and removed (review round 1, F3)',
     [(FD, GUARD, 'if (stat.isDirectory()) rmSync(')]),
    ('stat-follows-symlink', 'a symlink to a directory is judged by its target, not by itself',
     [(FD, "import { lstatSync, readdirSync, readlinkSync, rmSync } from 'node:fs';", "import { lstatSync, readdirSync, readlinkSync, rmSync, statSync } from 'node:fs';"),
      (FD, 'const stat = lstatSync(entry);', 'const stat = statSync(entry);')]),
    ('removal-failure-propagates', 'a directory that cannot be removed fails the run that sweeps',
     [(FD, TRY, "    const stat = lstatSync(entry);\n    if (stat.isDirectory() && (user === undefined || stat.uid === user)) rmSync(entry, { recursive: true, force: true });\n")]),
    ('readdir-outside-try', 'a temp directory that cannot be listed fails the run that sweeps (review round 1, N1)',
     [(FD, LIST, '  const names = readdirSync(directory);\n')]),
    ('lists-the-parent', 'the sweep lists the parent of the directory it is given',
     [(FD, 'names = readdirSync(directory);', "names = readdirSync(join(directory, '..'));")]),
    ('tmpdir-read-from-the-variable', 'the default directory is the TMPDIR variable itself, not what the operating system answers for the temp directory',
     [(FD, 'directory: string = tmpdir()', "directory: string = process.env['TMPDIR'] as string")]),
    ('copy-name-without-pid', 'a copy is named as before, with no pid',
     [(FD, '`${FIXTURE_PREFIX}p${process.pid}-n${pidNamespace()}-`', '`${FIXTURE_PREFIX}`')]),
    ('copy-name-without-namespace', 'a copy is named with its pid but not its PID namespace',
     [(FD, '`${FIXTURE_PREFIX}p${process.pid}-n${pidNamespace()}-`', '`${FIXTURE_PREFIX}p${process.pid}-`')]),
    ('template-name-without-pid', 'the template is named as before, with no pid',
     [(FD, '`${FIXTURE_PREFIX}template-p${process.pid}-n${pidNamespace()}-`', '`${FIXTURE_PREFIX}template-`')]),
    ('template-name-without-namespace', 'the template is named with its pid but not its PID namespace',
     [(FD, '`${FIXTURE_PREFIX}template-p${process.pid}-n${pidNamespace()}-`', '`${FIXTURE_PREFIX}template-p${process.pid}-`')]),
    ('global-setup-does-not-sweep', 'the global setup runs and sweeps nothing',
     [(GS, '  removeFixturesOfDeadProcesses();\n', '')]),
    ('global-setup-not-registered', 'the app project registers no global setup: no sweep at all',
     [(VC, GLOBAL_SETUP_LINE, '')]),
    ('global-setup-on-every-project', 'the global setup is registered at the root, so every project runs it',
     [(VC, "    maxWorkers: '50%',\n", "    maxWorkers: '50%',\n    globalSetup: [fileURLToPath(new URL('./apps/three-surface-poc/src/test-fixture-sweep.global-setup.ts', import.meta.url))],\n")]),
    ('sweep-per-file', 'every file sweeps when it makes its template, as well as the global setup',
     [(TM, "import { ownedCopyPrefix, ownedTemplatePrefix } from './fixture-directories.js';", "import { ownedCopyPrefix, ownedTemplatePrefix, removeFixturesOfDeadProcesses } from './fixture-directories.js';"),
      (TM, '  const root = mkdtempSync(join(tmpdir(), ownedTemplatePrefix()));', '  removeFixturesOfDeadProcesses();\n  const root = mkdtempSync(join(tmpdir(), ownedTemplatePrefix()));')]),
]

run = lambda *a: subprocess.run(a, cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
commit = run('git', 'rev-parse', 'HEAD')
FILES = sorted({f for _, _, edits in MUTANTS for f, _, _ in edits} | set(TESTS))
dirty = run('git', 'status', '--porcelain', '--', *FILES)
assert dirty == '', f'{FILES} must be committed before a rule-6 run: {dirty}'
originals = {name: (WT / name).read_text() for name in FILES}
digests = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in originals.items()}
report = pathlib.Path(tempfile.mkdtemp(prefix='zz-mutate-sweep-')) / 'report.json'  # removed in the final `finally`
command = ['npx', 'vitest', 'run', *TESTS, '--project', '@syzygy/three-surface-poc-app', '--reporter=json', f'--outputFile={report}']


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
    assert control['holds'], 'the unmutated tree must pass both test files and leave no fixture directory'
    for name, meaning, edits in MUTANTS:
        record = {'id': name, 'meaning': meaning, 'edits': [{'file': f, 'old': old, 'new': new} for f, old, new in edits]}
        counts = [originals[f].count(old) for f, old, _ in edits]
        if any(c != 1 for c in counts):
            results.append(record | {'outcome': 'FRAGMENT-COUNT-' + '/'.join(map(str, counts))})
            print(name, results[-1]['outcome'], flush=True)
            continue
        try:
            for f, old, new in edits:
                (WT / f).write_text((WT / f).read_text().replace(old, new, 1))
            exit_code, total, failing, leaked = vitest()
        finally:
            for f in {f for f, _, _ in edits}:
                (WT / f).write_text(originals[f])
        results.append(record | {'exit': exit_code, 'outcome': 'killed' if exit_code != 0 else 'SURVIVED', 'testsRun': total, 'failing': failing, 'fixtureDirectoriesLeftInPrivateTmpdir': leaked})
        print(name, results[-1]['outcome'], len(failing), flush=True)
finally:
    for name, text in originals.items():
        (WT / name).write_text(text)
    shutil.rmtree(PRIVATE_TMP, ignore_errors=True)
    shutil.rmtree(report.parent, ignore_errors=True)
for name, text in originals.items():
    assert hashlib.sha256((WT / name).read_text().encode()).hexdigest() == digests[name]
OUT.write_text(json.dumps({
    'tool': 'mutate_sweep.py',
    'testFiles': TESTS,
    'command': ' '.join(command[:7]),
    'treeCommit': commit,
    'sha256AtCommit': digests,
    'control': control,
    'mutants': len(MUTANTS),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['id'] for r in results if r['outcome'] != 'killed'])
