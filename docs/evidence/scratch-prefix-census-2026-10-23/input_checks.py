#!/usr/bin/env python3
"""Does assemble_census.py refuse inputs that are not the ones its records name?

Usage: input_checks.py <worktree> <commit> <static-sites.json> <runs-directory> <scratch-directory> <out.json>

Copies <runs-directory> into <scratch-directory> (a short absolute path that does not exist or is empty), runs the assembler on the
copy as a control (it must succeed), then on copies each corrupted in one way, and requires the assembler to stop with a non-zero
exit and the message named below. The corruptions: one byte of a trace changed; one line of a trace removed; a run record naming
another commit; the static census naming another commit; a run's sampler record missing. It removes <scratch-directory> at the end.
"""
import gzip
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
WT, COMMIT, STATIC, RUNS, SCRATCH, OUT = (pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve(), pathlib.Path(sys.argv[4]).resolve(),
                                          pathlib.Path(sys.argv[5]), pathlib.Path(sys.argv[6]).resolve())
assert SCRATCH.is_absolute() and len(str(SCRATCH)) <= 12 and (not SCRATCH.exists() or (SCRATCH.is_dir() and not any(SCRATCH.iterdir()))), 'give a short absolute scratch directory (at most 12 bytes: the assembler\'s probe path must stay within 30) that is empty'
LABEL = 'k2-kill-75s'
OTHER_COMMIT = '0' * 40


def case(name: str, change) -> dict:
    root = SCRATCH / name
    runs, static = root / 'runs', root / 'static.json'
    shutil.copytree(RUNS, runs)
    shutil.copyfile(STATIC, static)
    change(runs, static)
    ran = subprocess.run([sys.executable, '-I', str(HERE / 'assemble_census.py'), str(WT), COMMIT, str(static), str(runs), str(root / 'probe'), str(root / 'out.json')],
                         capture_output=True, text=True, timeout=600)
    return {'exit': ran.returncode, 'lastLine': (ran.stderr.strip().splitlines() or [''])[-1][:200], 'wroteTheRecord': (root / 'out.json').exists()}


def trace_edit(edit):
    def apply(runs, static):
        path = runs / f'{LABEL}.trace.jsonl.gz'
        raw = gzip.decompress(path.read_bytes())
        path.write_bytes(gzip.compress(edit(raw), mtime=0))
    return apply


def record_edit(runs, static):
    path = runs / f'{LABEL}.json'
    record = json.loads(path.read_text())
    record['treeCommit'] = OTHER_COMMIT
    path.write_text(json.dumps(record))


def static_edit(runs, static):
    record = json.loads(static.read_text())
    record['treeCommit'] = OTHER_COMMIT
    static.write_text(json.dumps(record))


CASES = {
    'trace-byte-changed': (trace_edit(lambda raw: raw[:100] + bytes([raw[100] ^ 1]) + raw[101:]), 'the trace is not the one the record names'),
    'trace-line-removed': (trace_edit(lambda raw: raw.split(b'\n', 1)[1]), 'the trace is not the one the record names'),
    'run-record-names-another-commit': (record_edit, 'the run names another commit'),
    'static-census-names-another-commit': (static_edit, 'the static census names another commit'),
    'sampler-record-missing': (lambda runs, static: (runs / f'{LABEL}.samples.json').unlink(), 'FileNotFoundError'),
}
shutil.rmtree(SCRATCH, ignore_errors=True)
SCRATCH.mkdir(parents=True)
try:
    record = {'tool': 'input_checks.py', 'treeCommit': COMMIT, 'assemblerSha256': hashlib.sha256((HERE / 'assemble_census.py').read_bytes()).hexdigest(), 'runsChecked': LABEL}
    record['control'] = case('control', lambda runs, static: None)
    record['control']['meets'] = record['control']['exit'] == 0 and record['control']['wroteTheRecord']
    record['cases'] = {}
    for name, (change, message) in CASES.items():
        got = case(name, change)
        got['expectedMessage'] = message
        got['refused'] = got['exit'] != 0 and message in got['lastLine'] and not got['wroteTheRecord']
        record['cases'][name] = got
finally:
    shutil.rmtree(SCRATCH, ignore_errors=True)
record['holds'] = record['control']['meets'] and all(c['refused'] for c in record['cases'].values())
OUT.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({'control': record['control']['meets'], 'refused': {n: c['refused'] for n, c in record['cases'].items()}, 'holds': record['holds']}))
sys.exit(0 if record['holds'] else 1)
