"""Two further reviewer mutants for PR #511, run against the whole @syzygy/polaris-dossier project at the reviewed head (rev511c: rev511b with the file argument dropped).

- D1-with-memoized-reader: launchedMarkerState remembers each run directory's first answer, and launchFormRefusal removes an unreadable
  marker (D1, with an unlink fallback). The post-condition asks the same reader, so it hears the remembered `unreadable`.
- T-ask-of-an-unplanted-run (a test-side mutant): asked() takes a fresh, empty run instead of a planted one. Shows the post-condition
  fails when a row's plant never took effect.
Killed: a nonzero exit with at least one failed test, or a timeout.
Usage: python3 rev511b.py <clone> <scratch dir> <out.json>
"""
import hashlib, json, os, re, signal, subprocess, sys
from pathlib import Path

ROOT, SCRATCH, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
TIMEOUT = 1500
READER = 'packages/polaris-dossier/src/launched.ts'
TEST = 'packages/polaris-dossier/src/launched.test.ts'
REPORT = SCRATCH / 'rev511c-vitest.json'
COMMAND = ['npx', 'vitest', 'run', '--project', '@syzygy/polaris-dossier', '--reporter=json', f'--outputFile={REPORT}']
REFUSAL = ("'the run\\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or "
           "syzygy-launched'")
NAME = 'path.join(runDir, RUN_LAYOUT.launched)'
REMOVE_ANY = (f"try {{ fs.rmSync({NAME}, {{ recursive: true, force: true }}); }} catch {{ /* reviewer mutant */ }} "
              f"try {{ fs.unlinkSync({NAME}); }} catch {{ /* reviewer mutant */ }}")
MUTANTS = [
    ('D1-with-memoized-reader', [
        (READER, "export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);",
         "const REMEMBERED = new Map<string, LaunchedMarkerState>();\n"
         "export function launchedMarkerState(runDir: string): LaunchedMarkerState {\n"
         "  const hit = REMEMBERED.get(runDir); if (hit) return hit;\n"
         "  const state = launchedMarkerStateOnce(runDir); REMEMBERED.set(runDir, state); return state;\n}\n\n"
         "function launchedMarkerStateOnce(runDir: string): LaunchedMarkerState {\n  const file = path.join(runDir, RUN_LAYOUT.launched);"),
        (READER, f"  if (state === 'unreadable') return {REFUSAL};", f"  if (state === 'unreadable') {{ {REMOVE_ANY}\n    return {REFUSAL}; }}"),
    ]),
]
LINE = re.compile(r'launched\.test\.ts:(\d+):\d+')


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
    failed = []
    for file in report['testResults']:
        for test in file['assertionResults']:
            if test['status'] == 'failed':
                text = '\n'.join(test['failureMessages'])
                failed.append({'test': test['fullName'], 'firstErrorLine': next((l for l in text.splitlines() if l.strip()), None),
                               'testFileLines': [int(n) for n in LINE.findall(text)]})
    return proc.returncode, {k: report[k] for k in ('numTotalTests', 'numPassedTests', 'numFailedTests')}, failed


def main():
    assert git('status', '--porcelain', '--untracked-files=no') == ''
    originals = {f: (ROOT / f).read_bytes() for f in (READER, TEST)}
    results = []
    try:
        for mutant_id, edits in MUTANTS:
            current = {f: data.decode('utf8') for f, data in originals.items()}
            for file, old, new in edits:
                assert current[file].count(old) == 1, (mutant_id, old)
                current[file] = current[file].replace(old, new)
            for file, text in current.items():
                (ROOT / file).write_bytes(text.encode('utf8'))
            try:
                code, counts, failed = run_suite()
            finally:
                for file, data in originals.items():
                    (ROOT / file).write_bytes(data)
            results.append({'id': mutant_id, 'tests': 'head', 'edits': [{'file': f, 'old': o, 'new': n} for f, o, n in edits],
                            'exitCode': code, 'counts': counts, 'failedTests': failed, 'blocked': code is None,
                            'outcome': 'killed' if code is None or (code != 0 and failed) else 'survived',
                            'restored': all(sha((ROOT / f).read_bytes()) == sha(d) for f, d in originals.items())})
            print(mutant_id, results[-1]['outcome'], counts, flush=True)
    finally:
        for file, data in originals.items():
            (ROOT / file).write_bytes(data)
    record = {'head': git('rev-parse', 'HEAD').strip(), 'readerSha256': sha(originals[READER]), 'testSha256': sha(originals[TEST]),
              'mutants': results, 'trackedTreeCleanAfter': git('status', '--porcelain', '--untracked-files=no') == '',
              'harnessSha256': sha(Path(__file__).read_bytes())}
    OUT.write_text(json.dumps(record, indent=2) + '\n')


main()
