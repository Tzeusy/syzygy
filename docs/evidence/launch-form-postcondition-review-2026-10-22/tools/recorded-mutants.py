"""Rule-6 mutants for syzygy-bpyt.8.18, a test-only change to launched.test.ts: each launch-form ask in the unreadable-marker row now
asserts that its run still reads `unreadable` afterwards (PR #506 review N1). Each mutant is run three times, against
launched.test.ts as it stood before PR #506's refill (`pre-refill`), at this change's base (`base`, the refill without the post-condition)
and at the fix (`fix`), so the record shows what the refill and the post-condition each catch that the row before them did not.

D1 makes launchFormRefusal remove the marker when it reads unreadable; D2 makes launchedMarkerState itself remove it (both from the
review's Appendix A). F2 is syzygy-bpyt.8.14's mutant: the declared forms read the bytes before judging the file type, so they drain a
FIFO, and the syzygy-launched path keeps no type check at all. M-all-forms-drain-bang-unchecked is the review's mutant of the same shape
with `bang` as the unchecked form (N2: the record of the bang form's discriminating mutant).

Each mutant replaces exact fragments (each must occur exactly once), runs the test file alone in its own process group with vitest's
JSON reporter, restores the bytes and verifies their digests. Killed: at least one test failed, or the run did not finish within the
timeout. Each failed test is stored with the first line of its first failure message.
Usage: python3 mutants.py <worktree> <base commit> <pre-refill commit> <scratch dir> <out.json>
"""
import hashlib, json, os, signal, subprocess, sys
from pathlib import Path

ROOT, BASE, PRE, SCRATCH, OUT = Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3], Path(sys.argv[4]).resolve(), Path(sys.argv[5])
TIMEOUT = 300
READER = 'packages/polaris-dossier/src/launched.ts'
TEST = 'packages/polaris-dossier/src/launched.test.ts'
REPORT = SCRATCH / 'mutant-vitest.json'
COMMAND = ['npx', 'vitest', 'run', '--project', '@syzygy/polaris-dossier', '--reporter=json', f'--outputFile={REPORT}', TEST]

SIGNATURE = ('export function launchedMarkerState(runDir: string): LaunchedMarkerState {',
             'export function launchedMarkerState(runDir: string, anyFileType = false): LaunchedMarkerState {')
TYPE_AFTER_READ = [
    (READER, "    if (!stat.isFile() || stat.size > MARKER_BYTES_MAX) return 'unreadable';", "    if (stat.size > MARKER_BYTES_MAX) return 'unreadable';"),
    (READER, "    if (length > MARKER_BYTES_MAX) return 'unreadable';",
     "    if (length > MARKER_BYTES_MAX || (!anyFileType && !stat.isFile())) return 'unreadable';"),
]
CALL = lambda unchecked: (READER, "  const state = launchedMarkerState(runDir);\n  if (state === 'unreadable')",
                          f"  const state = launchedMarkerState(runDir, {unchecked});\n  if (state === 'unreadable')")
REFUSAL = ("'the run\\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or "
           "syzygy-launched'")
REMOVE = "try { fs.rmSync(path.join(runDir, RUN_LAYOUT.launched), { recursive: true, force: true }); } catch { /* reviewer mutant */ }"

MUTANTS = [
    ('D1-launch-form-refusal-removes-an-unreadable-marker', [
        (READER, f"  if (state === 'unreadable') return {REFUSAL};",
         f"  if (state === 'unreadable') {{ {REMOVE}\n    return {REFUSAL}; }}")]),
    ('D2-marker-state-removes-an-unreadable-marker', [
        (READER, "export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);",
         "export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const state = launchedMarkerStateOnce(runDir);\n"
         f"  if (state === 'unreadable') {{ {REMOVE} }}\n  return state;\n}}\n\n"
         "function launchedMarkerStateOnce(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);")]),
    ('F2-declared-forms-drain-then-judge-type-syzygy-launched-unchecked', [
        (READER, *SIGNATURE), *TYPE_AFTER_READ, CALL("form['value'] === SYZYGY_LAUNCHED")]),
    ('M-all-forms-drain-bang-unchecked', [
        (READER, *SIGNATURE), *TYPE_AFTER_READ, CALL("form['value'] === 'bang'")]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def run_suite():
    REPORT.unlink(missing_ok=True)
    proc = subprocess.Popen(COMMAND, cwd=ROOT, env={**os.environ, 'CI': '1'}, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)
    try:
        proc.communicate(timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.communicate()
        return None, None, []
    if not REPORT.exists():
        return proc.returncode, None, []
    report = json.loads(REPORT.read_text())
    failed = [{'test': test['fullName'],
               'firstErrorLine': next((line for message in test['failureMessages'] for line in message.splitlines() if line.strip()), None)}
              for file in report['testResults'] for test in file['assertionResults'] if test['status'] == 'failed']
    return proc.returncode, {k: report[k] for k in ('numTotalTests', 'numPassedTests', 'numFailedTests')}, failed


def main():
    assert git('status', '--porcelain', '--untracked-files=no') == ''
    head_test = (ROOT / TEST).read_bytes()
    tests = {'pre-refill': git('show', f'{PRE}:{TEST}').encode('utf8'), 'base': git('show', f'{BASE}:{TEST}').encode('utf8'), 'fix': head_test}
    originals = {READER: (ROOT / READER).read_bytes(), TEST: head_test}
    for commit in (PRE, BASE):
        assert git('show', f'{commit}:{READER}').encode('utf8') == originals[READER], f'the reader differs between {commit} and the fix'
    results, unmutated = [], {}
    try:
        for side, test_bytes in tests.items():
            (ROOT / TEST).write_bytes(test_bytes)
            code, counts, failed = run_suite()
            unmutated[side] = {'testSha256': sha(test_bytes), 'exitCode': code, 'counts': counts, 'failedTests': failed}
            for mutant_id, edits in MUTANTS:
                current = {READER: originals[READER].decode('utf8'), TEST: test_bytes.decode('utf8')}
                for file, old, new in edits:
                    assert current[file].count(old) == 1, (mutant_id, side, old)
                    current[file] = current[file].replace(old, new)
                for file in current:
                    (ROOT / file).write_bytes(current[file].encode('utf8'))
                try:
                    code, counts, failed = run_suite()
                finally:
                    (ROOT / READER).write_bytes(originals[READER])
                    (ROOT / TEST).write_bytes(test_bytes)
                blocked = code is None
                results.append({'id': mutant_id, 'tests': side, 'edits': [{'file': f, 'old': o, 'new': n} for f, o, n in edits],
                                'exitCode': code, 'counts': counts, 'failedTests': failed, 'blocked': blocked,
                                'outcome': 'killed' if blocked or (code != 0 and failed) else 'survived',
                                'restored': sha((ROOT / READER).read_bytes()) == sha(originals[READER])})
                print(mutant_id, side, results[-1]['outcome'], counts, flush=True)
    finally:
        for file, data in originals.items():
            (ROOT / file).write_bytes(data)
    record = {
        'title': 'syzygy-bpyt.8.18 rule-6 mutants: each launch-form ask leaves its run unreadable',
        'bead': 'syzygy-bpyt.8.18', 'subject': [TEST], 'testSha256': {side: sha(data) for side, data in tests.items()},
        'readerSha256': sha(originals[READER]), 'preRefill': git('rev-parse', PRE).strip(), 'base': git('rev-parse', BASE).strip(), 'commit': git('rev-parse', 'HEAD').strip(),
        'command': ' '.join(COMMAND).replace(str(REPORT), '<scratch>/mutant-vitest.json'), 'timeoutSeconds': TIMEOUT,
        'unmutated': unmutated, 'mutants': results,
        'trackedTreeCleanAfter': git('status', '--porcelain', '--untracked-files=no') == '',
        'summary': {f'{m} / {side} tests': next(r['outcome'] for r in results if r['id'] == m and r['tests'] == side)
                    for m, _ in MUTANTS for side in tests},
        'harnessSource': Path(__file__).read_text(),
    }
    OUT.write_text(json.dumps(record, indent=2) + '\n')
    print('summary', json.dumps(record['summary'], indent=1))


main()
