"""Reviewer harness for PR 513 (syzygy-bpyt.4.12). Not part of the PR.

Runs packages/polaris-dossier/src/waiting-sessions.test.ts alone, each run in a fresh, empty TMPDIR under TMP_ROOT, and records the
TMPDIR's full listing before and after (top level, plus every path not under node-compile-cache). Each scenario writes exact fragment
replacements (each `old` must occur exactly once) into the reader and/or the test file, runs vitest with its JSON reporter (report
written outside the TMPDIR), restores the bytes and verifies their sha256 against the originals.

Usage: python3 rev513.py <clone> <base commit> <tmp root> <out.json>
"""
import hashlib, json, os, signal, subprocess, sys
from pathlib import Path

ROOT, BASE, TMP, OUT = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]).resolve()
TIMEOUT = 900
READER = 'packages/polaris-dossier/src/waiting-sessions.ts'
TEST = 'packages/polaris-dossier/src/waiting-sessions.test.ts'
PROJECT = '@syzygy/polaris-dossier'
REPORT_DIR = OUT.parent / 'reports'
ROW = 'the record names a review outside the records root'

R1 = (READER, "  if (review === undefined || review.split('/').includes('..')) return false;",
      "  if (review === undefined) return false;")
R2 = (READER, "  if (review === undefined || review.split('/').includes('..')) return false;",
      "  if (review === undefined || review.split('/')[0] === '..') return false;")
WRITE = "      fs.writeFileSync(outside, reviewHead(digest));\n"
T_EAGER = (TEST, WRITE, "      fs.writeFileSync(outside, reviewHead(digest));\n      fs.rmSync(outside);\n")
T_DROP = (TEST, "      cleanups.push(() => fs.rmSync(outside, { force: true }));\n", "")
T_THROW = (TEST, WRITE, "      fs.writeFileSync(outside, reviewHead(digest));\n      throw new Error('probe: thrown after the write');\n")

# (id, test side, edits, extra vitest args, expectation)
SCENARIOS = [
    ('U-fix', 'fix', [], [], 'pass, no stray'),
    ('U-base', 'base', [], [], 'pass, one stray (the leak reproduced)'),
    ('R1-fix', 'fix', [R1], [], 'killed by the row, no stray'),
    ('R1-base', 'base', [R1], [], 'killed by the row, one stray'),
    ('R2-fix', 'fix', [R2], [], 'reviewer mutant: leading-segment-only check; predicted to survive (row uses a leading ..)'),
    ('T-eager+R1-fix', 'fix', [T_EAGER, R1], [], 'cleanup moved before the assertion; predicted R1 survives (shows timing is load-bearing)'),
    ('T-drop-fix', 'fix', [T_DROP], [], 'cleanup registration dropped; predicted stray returns (listing detects the leak)'),
    ('P-throw-fix', 'fix', [T_THROW], [], 'throw after the write; row fails, predicted no stray'),
    ('P-retry+R1-fix', 'fix', [R1], ['--retry=2'], 'row fails on all 3 tries; predicted no stray'),
    ('P-timeout-fix', 'fix', [], ['--testTimeout=1'], 'every test given 1 ms; record stray outcome'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def listing(tmp):
    top = sorted(os.listdir(tmp))
    deep = []
    for dirpath, dirnames, filenames in os.walk(tmp):
        rel = os.path.relpath(dirpath, tmp)
        if rel == 'node-compile-cache' or rel.startswith('node-compile-cache' + os.sep):
            continue
        for name in dirnames + filenames:
            path = os.path.normpath(os.path.join(rel, name))
            if path != 'node-compile-cache':
                deep.append(path)
    return top, sorted(deep)


def run(command, tmp):
    proc = subprocess.Popen(command, cwd=ROOT, env={**os.environ, 'CI': '1', 'TMPDIR': str(tmp)}, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, start_new_session=True)
    try:
        out, _ = proc.communicate(timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        out, _ = proc.communicate()
        return None, out
    return proc.returncode, out


def main():
    assert git('status', '--porcelain', '--untracked-files=no') == '', 'tracked tree not clean'
    TMP.mkdir()
    REPORT_DIR.mkdir(exist_ok=True)
    head = git('rev-parse', 'HEAD').strip()
    tests = {'base': git('show', f'{BASE}:{TEST}').encode('utf8'), 'fix': (ROOT / TEST).read_bytes()}
    originals = {READER: (ROOT / READER).read_bytes(), TEST: tests['fix']}
    digests = {f: sha(b) for f, b in originals.items()}
    results = []
    try:
        for n, (sid, side, edits, extra, expect) in enumerate(SCENARIOS, 1):
            current = {READER: originals[READER].decode('utf8'), TEST: tests[side].decode('utf8')}
            for file, old, new in edits:
                assert current[file].count(old) == 1, (sid, file, old)
                current[file] = current[file].replace(old, new)
            for file, text in current.items():
                (ROOT / file).write_bytes(text.encode('utf8'))
            tmp = TMP / f't{n}'
            tmp.mkdir()
            report = REPORT_DIR / f'{sid}.json'
            report.unlink(missing_ok=True)
            before = listing(tmp)
            try:
                code, out = run(['npx', 'vitest', 'run', '--project', PROJECT, '--reporter=json', f'--outputFile={report}', *extra, TEST], tmp)
            finally:
                for file, data in originals.items():
                    (ROOT / file).write_bytes(data)
            after = listing(tmp)
            restored = all(sha((ROOT / f).read_bytes()) == d for f, d in digests.items())
            counts, failed, row = None, [], []
            if report.exists():
                data = json.loads(report.read_text())
                counts = {k: data[k] for k in ('numTotalTests', 'numPassedTests', 'numFailedTests')}
                for file in data['testResults']:
                    for test in file['assertionResults']:
                        first = next((l for m in test.get('failureMessages', []) for l in m.splitlines() if l.strip()), None)
                        if test['status'] == 'failed':
                            failed.append({'test': test['fullName'], 'firstErrorLine': first})
                        if ROW in test['fullName']:
                            row.append({'test': test['fullName'], 'status': test['status'], 'firstErrorLine': first,
                                        'retryCount': test.get('retryCount')})
            stray = [p for p in after[1] if p.startswith('dossier-')]
            result = {
                'id': sid, 'tests': side, 'testSha256': sha(tests[side]),
                'edits': [{'file': f, 'old': o, 'new': nw} for f, o, nw in edits], 'extraArgs': extra, 'expectation': expect,
                'exitCode': code, 'counts': counts, 'failedTests': failed, 'row': row,
                'tmpdir': str(tmp), 'listingBefore': {'top': before[0], 'deep': before[1]},
                'listingAfter': {'top': after[0], 'deep': after[1]}, 'strayDossierAfter': stray, 'restored': restored,
                'outputTail': out.decode('utf8', 'replace').splitlines()[-15:],
            }
            results.append(result)
            print(sid, code, counts, 'row=', [(r['status'], r['firstErrorLine']) for r in row], 'stray=', stray, 'restored=', restored,
                  flush=True)
            OUT.write_text(json.dumps({'partial': True, 'results': results}, indent=2) + '\n')
    finally:
        for file, data in originals.items():
            (ROOT / file).write_bytes(data)
    record = {
        'reviewer': 'rev-513', 'commit': head, 'base': git('rev-parse', BASE).strip(),
        'readerSha256': digests[READER], 'testSha256': {s: sha(b) for s, b in tests.items()},
        'command': f'TMPDIR=<fresh empty dir> CI=1 npx vitest run --project {PROJECT} --reporter=json --outputFile=<scratch>/reports/<id>.json [extra] {TEST}',
        'results': results,
        'trackedTreeCleanAfter': git('status', '--porcelain', '--untracked-files=no') == '',
        'harnessSha256': sha(Path(__file__).read_bytes()),
    }
    OUT.write_text(json.dumps(record, indent=2) + '\n')
    print('done', flush=True)


main()
