"""Reviewer mutants for PR #511 (syzygy-bpyt.8.18), beyond the four the lane recorded.

Each mutant edits packages/polaris-dossier/src/launched.ts only. It runs against launched.test.ts at base 9c3350fb (the #506 refill,
no post-condition) and at the reviewed head (the post-condition). Killed: a nonzero exit with at least one failed test, or a timeout.

- D1-<form>-only: launchFormRefusal removes an unreadable marker, but only when asked for one form. Shows each of the three
  post-conditions is load-bearing on its own (rule 6, per predicate).
- D1-any-remover: D1 with an unlink fallback, because fs.rmSync with force silently leaves a dangling link in place.
- D3-repair-to-launched: launchFormRefusal replaces an unreadable marker with the one Syzygy writes (the fail-open direction).
- D4-truncate: launchFormRefusal truncates the file at the marker's name, following links. The state stays unreadable.
- M-every-form-drains-then-refuses: every read takes the bytes before judging the type, and every form still refuses.
For each failed test the record keeps the first error line and every launched.test.ts line named in its failure messages.
Usage: python3 rev511.py <clone> <scratch dir> <out.json>
"""
import hashlib, json, os, re, signal, subprocess, sys
from pathlib import Path

ROOT, SCRATCH, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
BASE = '9c3350fb04a62d89adc373230e2b9c83f51db54c'
TIMEOUT = 300
READER = 'packages/polaris-dossier/src/launched.ts'
TEST = 'packages/polaris-dossier/src/launched.test.ts'
REPORT = SCRATCH / 'rev511-vitest.json'
LIST = SCRATCH / 'rev511-list.json'
COMMAND = ['npx', 'vitest', 'run', '--project', '@syzygy/polaris-dossier', '--reporter=json', f'--outputFile={REPORT}', TEST]
LIST_COMMAND = ['npx', 'vitest', 'list', '--project', '@syzygy/polaris-dossier', f'--json={LIST}', TEST]

REFUSAL = ("'the run\\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or "
           "syzygy-launched'")
REFUSAL_LINE = f"  if (state === 'unreadable') return {REFUSAL};"
NAME = 'path.join(runDir, RUN_LAYOUT.launched)'
REMOVE_ANY = (f"try {{ fs.rmSync({NAME}, {{ recursive: true, force: true }}); }} catch {{ /* reviewer mutant */ }} "
              f"try {{ fs.unlinkSync({NAME}); }} catch {{ /* reviewer mutant */ }}")


def refusal_with(body):
    return [(READER, REFUSAL_LINE, f"  if (state === 'unreadable') {{ {body}\n    return {REFUSAL}; }}")]


MUTANTS = [
    ('D1-terminal-only', refusal_with(f"if (form['value'] === 'terminal') {{ {REMOVE_ANY} }}")),
    ('D1-bang-only', refusal_with(f"if (form['value'] === 'bang') {{ {REMOVE_ANY} }}")),
    ('D1-syzygy-launched-only', refusal_with(f"if (form['value'] === SYZYGY_LAUNCHED) {{ {REMOVE_ANY} }}")),
    ('D1-any-remover', refusal_with(REMOVE_ANY)),
    ('D3-repair-to-launched', refusal_with(f"{REMOVE_ANY} try {{ writeLaunchedMarker(runDir, 'run-x', 0); }} catch {{ /* reviewer mutant */ }}")),
    ('D4-truncate', refusal_with(f"try {{ fs.truncateSync({NAME}, 0); }} catch {{ /* reviewer mutant */ }}")),
    ('M-every-form-drains-then-refuses', [
        (READER, "    if (!stat.isFile() || stat.size > MARKER_BYTES_MAX) return 'unreadable';", "    if (stat.size > MARKER_BYTES_MAX) return 'unreadable';"),
        (READER, "    if (length > MARKER_BYTES_MAX) return 'unreadable';", "    if (length > MARKER_BYTES_MAX || !stat.isFile()) return 'unreadable';"),
    ]),
]
LINE = re.compile(r'launched\.test\.ts:(\d+):\d+')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def run(command, report):
    report.unlink(missing_ok=True)
    proc = subprocess.Popen(command, cwd=ROOT, env={**os.environ, 'CI': '1'}, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)
    try:
        proc.communicate(timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.communicate()
        return None
    return proc.returncode


def run_suite():
    code = run(COMMAND, REPORT)
    if code is None or not REPORT.exists():
        return code, None, []
    report = json.loads(REPORT.read_text())
    failed = []
    for file in report['testResults']:
        for test in file['assertionResults']:
            if test['status'] != 'failed':
                continue
            text = '\n'.join(test['failureMessages'])
            failed.append({'test': test['fullName'],
                           'firstErrorLine': next((line for line in text.splitlines() if line.strip()), None),
                           'testFileLines': [int(n) for n in LINE.findall(text)]})
    return code, {k: report[k] for k in ('numTotalTests', 'numPassedTests', 'numFailedTests')}, failed


def names():
    code = run(LIST_COMMAND, LIST)
    if code != 0 or not LIST.exists():
        return code, None
    return code, sorted(entry['name'] for entry in json.loads(LIST.read_text()))


def main():
    assert git('status', '--porcelain', '--untracked-files=no') == ''
    head = git('rev-parse', 'HEAD').strip()
    originals = {READER: (ROOT / READER).read_bytes(), TEST: (ROOT / TEST).read_bytes()}
    sides = {'base': git('show', f'{BASE}:{TEST}').encode('utf8'), 'head': originals[TEST]}
    assert git('show', f'{BASE}:{READER}').encode('utf8') == originals[READER]
    results, unmutated, name_sets = [], {}, {}
    try:
        for side, test_bytes in sides.items():
            (ROOT / TEST).write_bytes(test_bytes)
            name_sets[side] = names()
            code, counts, failed = run_suite()
            unmutated[side] = {'testSha256': sha(test_bytes), 'exitCode': code, 'counts': counts, 'failedTests': failed}
            print('unmutated', side, code, counts, flush=True)
            for mutant_id, edits in MUTANTS:
                text = originals[READER].decode('utf8')
                for file, old, new in edits:
                    assert text.count(old) == 1, (mutant_id, old)
                    text = text.replace(old, new)
                (ROOT / READER).write_bytes(text.encode('utf8'))
                try:
                    code, counts, failed = run_suite()
                finally:
                    (ROOT / READER).write_bytes(originals[READER])
                blocked = code is None
                results.append({'id': mutant_id, 'tests': side, 'edits': [{'file': f, 'old': o, 'new': n} for f, o, n in edits],
                                'exitCode': code, 'counts': counts, 'failedTests': failed, 'blocked': blocked,
                                'outcome': 'killed' if blocked or (code != 0 and failed) else 'survived',
                                'readerRestored': sha((ROOT / READER).read_bytes()) == sha(originals[READER]),
                                'testIntact': sha((ROOT / TEST).read_bytes()) == sha(test_bytes)})
                print(mutant_id, side, results[-1]['outcome'], counts, flush=True)
    finally:
        for file, data in originals.items():
            (ROOT / file).write_bytes(data)
    base_names, head_names = name_sets['base'][1], name_sets['head'][1]
    record = {
        'head': head, 'base': BASE, 'readerSha256': sha(originals[READER]), 'testSha256': {s: sha(b) for s, b in sides.items()},
        'command': ' '.join(COMMAND).replace(str(REPORT), '<scratch>/rev511-vitest.json'), 'timeoutSeconds': TIMEOUT,
        'nameSets': {'base': len(base_names), 'baseDistinct': len(set(base_names)), 'head': len(head_names),
                     'headDistinct': len(set(head_names)), 'added': sorted(set(head_names) - set(base_names)),
                     'removed': sorted(set(base_names) - set(head_names))},
        'unmutated': unmutated, 'mutants': results,
        'readerRestoredAfter': sha((ROOT / READER).read_bytes()) == sha(originals[READER]),
        'testRestoredAfter': sha((ROOT / TEST).read_bytes()) == sha(originals[TEST]),
        'trackedTreeCleanAfter': git('status', '--porcelain', '--untracked-files=no') == '',
        'summary': {f'{r["id"]} / {r["tests"]}': f'{r["outcome"]} {r["counts"]["numFailedTests"] if r["counts"] else "-"} failed' for r in results},
        'harnessSha256': sha(Path(__file__).read_bytes()),
    }
    OUT.write_text(json.dumps(record, indent=2) + '\n')
    print('summary', json.dumps(record['summary'], indent=1))
    print('nameSets', json.dumps(record['nameSets']))


main()
