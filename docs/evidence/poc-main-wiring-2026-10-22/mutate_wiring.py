#!/usr/bin/env python3
"""Rule-6 run for the wiring pins in apps/three-surface-poc/src/main.test.ts.

Usage: mutate_wiring.py <worktree> <out.json> [--extras] [--helpers]

Each mutant edits one file of <worktree>, the command below runs main.test.ts
ALONE (not the old-script differential), and the file is restored byte for byte
afterwards. The nine N1 mutants of the round-2 review of syzygy-bpyt.5.5
(R-GP-IMPL-POC-APP-HYGIENE-2, note N1) edit poc-main.ts: five survived both
main.test.ts and the differential, four were killed only by the differential.
--extras adds mutants of the new seam and of the state-directory digest input
(poc-main.ts at this commit only); --helpers adds mutants of the wait helpers
in main.test.ts. A run against a tree that lacks a fragment records
FRAGMENT-COUNT-0 for it instead of guessing.

Records, per mutant: the exact old/new fragment, the command, the commit the run
was made at, and every failing test with its first error line (read from vitest's
JSON reporter, not scraped from text). A control (the unmutated tree) runs first
and must pass; a mutant is `killed` when main.test.ts exits non-zero.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

WT = pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2]).resolve()
EXTRAS = '--extras' in sys.argv
HELPERS = '--helpers' in sys.argv
TEST = 'apps/three-surface-poc/src/main.test.ts'
MAIN = 'apps/three-surface-poc/src/poc-main.ts'

# (id, file, old, new). `required` marks the nine N1 mutants.
REQUIRED = [
    ('bound-locator-ignored', MAIN,
     '(boundRepoRoot) => serveBoundRepository(boundRepoRoot, parsed.config, io, deps),',
     '(boundRepoRoot) => serveBoundRepository(repoRoot, parsed.config, io, deps),'),
    ('reobserve-horizon-root', MAIN,
     'observeHorizon: (pinned) => deps.observeGitHorizon(repoRoot, pinned),',
     'observeHorizon: (pinned) => deps.observeGitHorizon(io.cwd(), pinned),'),
    ('session-clock', MAIN,
     '      now: io.now,\n',
     '      now: () => new Date().toISOString(),\n'),
    ('verbatim-reader-root', MAIN, 'gitBlobReaderFor(repoRoot)', 'gitBlobReaderFor(io.cwd())'),
    ('materialize-target-root', MAIN, 'targetRepoRoot: repoRoot,', 'targetRepoRoot: io.cwd(),'),
    ('revision-change-root', MAIN,
     'deps.observeRevisionChange(repoRoot, from, to)',
     'deps.observeRevisionChange(io.cwd(), from, to)'),
    ('state-dir-unresolved', MAIN,
     'const stateDir = resolve(config.stateDir ?? join(',
     'const stateDir = (config.stateDir ?? join('),
    ('credential-provision-dropped', MAIN,
     'servedResponses, () => credentialProvision, session.latest)',
     'servedResponses, () => undefined, session.latest)'),
    ('reevaluation-dropped', MAIN,
     'servedResponses, () => credentialProvision, session.latest)',
     'servedResponses, () => credentialProvision)'),
]
EXTRA = [
    ('materialize-seam-bypassed', MAIN, '...deps.materializeRoutes({', '...materializeRoutes({'),
    ('state-dir-digest-input', MAIN,
     "createHash('sha256').update(repoRoot).digest('hex')",
     "createHash('sha256').update(io.cwd()).digest('hex')"),
]
HELPER = [
    ('started-ignores-finish', TEST, ' && exitCode === undefined && Date.now() < deadline', ' && Date.now() < deadline'),
    ('started-ignores-bound', TEST, ' && exitCode === undefined && Date.now() < deadline', ' && exitCode === undefined'),
]
MUTANTS = REQUIRED + (EXTRA if EXTRAS else []) + (HELPER if HELPERS else [])

run = lambda *a: subprocess.run(a, cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
commit = run('git', 'rev-parse', 'HEAD')
dirty = run('git', 'status', '--porcelain', '--', MAIN, TEST)
assert dirty == '', f'{MAIN} and {TEST} must be committed before a rule-6 run: {dirty}'
originals = {name: (WT / name).read_text() for name in (MAIN, TEST)}
digests = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in originals.items()}

report = pathlib.Path(tempfile.mkdtemp(prefix='zz-mutate-wiring-')) / 'report.json'
command = ['npx', 'vitest', 'run', TEST, '--reporter=json', f'--outputFile={report}']


def vitest() -> tuple[int, int, list[dict]]:
    report.unlink(missing_ok=True)
    proc = subprocess.run(command, cwd=WT, capture_output=True, text=True)
    data = json.loads(report.read_text()) if report.exists() else {'testResults': []}
    cases = [a for suite in data['testResults'] for a in suite['assertionResults']]
    failing = [{'test': a['fullName'], 'firstErrorLine': (a['failureMessages'][0].splitlines() or [''])[0] if a['failureMessages'] else ''}
               for a in cases if a['status'] == 'failed']
    return proc.returncode, len(cases), failing


results = []
control = {}
try:
    exit_code, total, failing = vitest()
    control = {'exit': exit_code, 'testsRun': total, 'failing': failing, 'holds': exit_code == 0 and total > 0}
    print('control', control['holds'], total, flush=True)
    assert control['holds'], 'the unmutated tree must pass main.test.ts'
    for name, file, old, new in MUTANTS:
        text = originals[file]
        if text.count(old) != 1:
            results.append({'id': name, 'file': file, 'old': old, 'new': new, 'outcome': f'FRAGMENT-COUNT-{text.count(old)}'})
            print(name, results[-1]['outcome'], flush=True)
            continue
        (WT / file).write_text(text.replace(old, new, 1))
        try:
            exit_code, total, failing = vitest()
        finally:
            (WT / file).write_text(text)
        results.append({'id': name, 'file': file, 'old': old, 'new': new, 'exit': exit_code,
                        'outcome': 'killed' if exit_code != 0 else 'SURVIVED', 'testsRun': total, 'failing': failing})
        print(name, results[-1]['outcome'], len(failing), flush=True)
finally:
    for name, text in originals.items():
        (WT / name).write_text(text)
for name, text in originals.items():
    assert hashlib.sha256((WT / name).read_text().encode()).hexdigest() == digests[name]
required_ids = [m[0] for m in REQUIRED]
OUT.write_text(json.dumps({
    'tool': 'mutate_wiring.py',
    'testFile': TEST,
    'command': ' '.join(command[:4]),
    'treeCommit': commit,
    'sha256AtCommit': digests,
    'control': control,
    'requiredMutants': len(required_ids),
    'requiredKilled': sum(1 for r in results if r['id'] in required_ids and r['outcome'] == 'killed'),
    'mutants': len(MUTANTS),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['id'] for r in results if r['outcome'] != 'killed'])
