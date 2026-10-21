#!/usr/bin/env python3
"""Rule-6 run for sweep_waits.py: each mutant edits a scratch copy of
main.test.ts so that one wait is no longer bounded, and the sweep must exit 1.

Usage: mutate_sweep_waits.py <test-file> <tree-commit> <out.json>

The control (the file as committed) must exit 0. A scratch copy is edited, never
the committed file. Records, per mutant, the exact old/new fragment, the sweep's
exit status and the block it reports as not bounded.
"""
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
test_file, tree_commit, out = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve()
original = test_file.read_text()

MUTANTS = [
    ('waitfor-timeout-above-test-timeout', '{ timeout: WAIT_MS }', '{ timeout: 40_000 }'),
    ('waitfor-timeout-option-dropped', ', { timeout: WAIT_MS });', ');'),
    ('test-timeout-dropped',
     "    fake.signal('SIGTERM');\n    expect(await run).toBe(0);\n    expect(fake.out().endsWith('syzygy POC: SIGTERM received, shutting down\\n')).toBe(true);\n  }, TEST_TIMEOUT_MS);",
     "    fake.signal('SIGTERM');\n    expect(await run).toBe(0);\n    expect(fake.out().endsWith('syzygy POC: SIGTERM received, shutting down\\n')).toBe(true);\n  });"),
    ('test-timeout-constant-lowered', 'const TEST_TIMEOUT_MS = 30_000;', 'const TEST_TIMEOUT_MS = 5_000;'),
    ('started-bound-parameter-dropped', 'boundMs: number = WAIT_MS', 'boundMs?: number'),
    ('started-bound-constant-raised', 'const WAIT_MS = 10_000;', 'const WAIT_MS = 30_000;'),
]


def sweep(text: str, scratch: pathlib.Path) -> tuple[int, str]:
    copy = scratch / 'main.test.ts'
    copy.write_text(text)
    proc = subprocess.run([sys.executable, str(HERE / 'sweep_waits.py'), str(copy), tree_commit, str(scratch / 'sweep.json')], capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip() or proc.stderr.strip().splitlines()[-1]


results = []
with tempfile.TemporaryDirectory(prefix='zz-sweep-waits-') as directory:
    scratch = pathlib.Path(directory)
    control_exit, control_line = sweep(original, scratch)
    assert control_exit == 0, f'the control must hold: {control_line}'
    for name, old, new in MUTANTS:
        if original.count(old) != 1:
            results.append({'id': name, 'old': old, 'new': new, 'outcome': f'FRAGMENT-COUNT-{original.count(old)}'})
            continue
        code, line = sweep(original.replace(old, new, 1), scratch)
        results.append({'id': name, 'old': old, 'new': new, 'exit': code, 'outcome': 'killed' if code == 1 else 'SURVIVED', 'firstOutputLine': line})
        print(name, results[-1]['outcome'], flush=True)
out.write_text(json.dumps({
    'tool': 'mutate_sweep_waits.py',
    'treeCommit': tree_commit,
    'testFile': test_file.name,
    'control': {'exit': control_exit, 'firstOutputLine': control_line, 'holds': control_exit == 0},
    'mutants': len(MUTANTS),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['id'] for r in results if r['outcome'] != 'killed'])
