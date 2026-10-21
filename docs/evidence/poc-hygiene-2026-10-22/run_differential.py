#!/usr/bin/env python3
"""Run the old-script versus new-main differential, and optionally its rule-6 mutants.

Usage: run_differential.py <worktree> <base-commit> <transcripts-out.json> [--mutants <rule6-out.json>]

Copies main-old-vs-new-differential.test.ts.txt to
apps/three-surface-poc/src/zz-main-differential.test.ts and writes the base
commit's main.ts to zz-main-old.ts (both throwaway, removed afterwards, never
committed). The harness runs 42 scenarios; in each the old script, the new
`main` in poc-main.ts and the new entry main.ts must give equal transcripts.
With --mutants, mutate_main.py then runs its mutants against the harness.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
WT = pathlib.Path(sys.argv[1]).resolve()
BASE = sys.argv[2]
TRANSCRIPTS = pathlib.Path(sys.argv[3]).resolve()
MUTANTS_OUT = pathlib.Path(sys.argv[sys.argv.index('--mutants') + 1]).resolve() if '--mutants' in sys.argv else None
SRC = WT / 'apps/three-surface-poc/src'
HARNESS = HERE / 'main-old-vs-new-differential.test.ts.txt'
ZZ_TEST, ZZ_OLD = SRC / 'zz-main-differential.test.ts', SRC / 'zz-main-old.ts'
REL_TEST = 'apps/three-surface-poc/src/zz-main-differential.test.ts'

old_main = subprocess.run(['git', 'show', f'{BASE}:apps/three-surface-poc/src/main.ts'], cwd=WT, capture_output=True, text=True, check=True).stdout
report = pathlib.Path(tempfile.mkdtemp(prefix='zz-differential-')) / 'report.json'
summary = {}
try:
    ZZ_TEST.write_text(HARNESS.read_text())
    ZZ_OLD.write_text(old_main)
    proc = subprocess.run(['npx', 'vitest', 'run', REL_TEST, '--reporter=json', f'--outputFile={report}'], cwd=WT, capture_output=True, text=True,
                          env={**__import__('os').environ, 'ZZ_TRANSCRIPT_OUT': str(TRANSCRIPTS)})
    data = json.loads(report.read_text())
    cases = [a for suite in data['testResults'] for a in suite['assertionResults']]
    summary = {
        'exit': proc.returncode,
        'tests': len(cases),
        'passed': sum(1 for a in cases if a['status'] == 'passed'),
        'failed': [{'test': a['fullName'], 'firstErrorLine': (a['failureMessages'][0].splitlines() or [''])[0]} for a in cases if a['status'] == 'failed'],
    }
    print(json.dumps({k: summary[k] for k in ('exit', 'tests', 'passed')}), 'failed', len(summary['failed']), flush=True)
    if MUTANTS_OUT is not None and proc.returncode == 0:
        subprocess.run([sys.executable, str(HERE / 'mutate_main.py'), str(WT), REL_TEST, str(MUTANTS_OUT)], check=True)
finally:
    ZZ_TEST.unlink(missing_ok=True)
    ZZ_OLD.unlink(missing_ok=True)

record = {
    'oldMainSha256': hashlib.sha256(old_main.encode()).hexdigest(),
    'harnessSha256': hashlib.sha256(HARNESS.read_bytes()).hexdigest(),
    'run': summary,
}
TRANSCRIPTS.with_suffix('.run.json').write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps(record))
sys.exit(summary.get('exit', 1))
