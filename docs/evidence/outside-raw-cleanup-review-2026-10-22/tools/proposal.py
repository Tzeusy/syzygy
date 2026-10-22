"""Reviewer probe for PR 513 (not part of the PR): does one more row, naming the outside raw as `docs/../../<root>-outside-RAW.md`,
kill R2 (the review-path check reduced to the first segment), which survives the reviewed file? Same method as rev513.py: a fresh empty
TMPDIR per run, listing before and after, exact fragment edits, bytes restored and verified.

Usage: python3 proposal.py <clone> <tmp root> <out.json>
"""
import hashlib, json, os, signal, subprocess, sys
from pathlib import Path

ROOT, TMP, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3]).resolve()
TIMEOUT = 900
READER = 'packages/polaris-dossier/src/waiting-sessions.ts'
TEST = 'packages/polaris-dossier/src/waiting-sessions.test.ts'
PROJECT = '@syzygy/polaris-dossier'
REPORT_DIR = OUT.parent / 'proposal-reports'
ANCHOR = "  ])('opens on no record when %s', (_name, mutate) => {\n"
NEW_ROW = """    ['the record names a review that leaves the records root after its first segment (reviewer proposal)', (root, decisions) => {
      const digest = createHash('sha256').update(fs.readFileSync(path.join(root, SPEC_REL))).digest('hex');
      const outside = path.join(path.dirname(root), `${path.basename(root)}-outside-RAW.md`);
      cleanups.push(() => fs.rmSync(outside, { force: true }));
      fs.writeFileSync(outside, reviewHead(digest));
      const file = path.join(decisions, 'POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.2.md');
      fs.writeFileSync(file, fs.readFileSync(file, 'utf8').replace('Review: docs/reviews/FIXTURE-v1.2-RAW.md', `Review: docs/../../${path.basename(root)}-outside-RAW.md`));
    }],
"""
ADD_ROW = (TEST, ANCHOR, NEW_ROW + ANCHOR)
R1 = (READER, "  if (review === undefined || review.split('/').includes('..')) return false;",
      "  if (review === undefined) return false;")
R2 = (READER, "  if (review === undefined || review.split('/').includes('..')) return false;",
      "  if (review === undefined || review.split('/')[0] === '..') return false;")
SCENARIOS = [
    ('Q-unmutated', [ADD_ROW], 'all 117 pass, no stray'),
    ('Q-R2', [ADD_ROW, R2], 'the new row fails, the existing row passes, no stray'),
    ('Q-R1', [ADD_ROW, R1], 'both outside rows fail, no stray'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def run(command, tmp):
    proc = subprocess.Popen(command, cwd=ROOT, env={**os.environ, 'CI': '1', 'TMPDIR': str(tmp)}, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, start_new_session=True)
    try:
        proc.communicate(timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.communicate()
        return None
    return proc.returncode


def main():
    assert git('status', '--porcelain', '--untracked-files=no') == '', 'tracked tree not clean'
    TMP.mkdir()
    REPORT_DIR.mkdir(exist_ok=True)
    originals = {f: (ROOT / f).read_bytes() for f in (READER, TEST)}
    digests = {f: sha(b) for f, b in originals.items()}
    results = []
    try:
        for n, (sid, edits, expect) in enumerate(SCENARIOS, 1):
            current = {f: b.decode('utf8') for f, b in originals.items()}
            for file, old, new in edits:
                assert current[file].count(old) == 1, (sid, file)
                current[file] = current[file].replace(old, new)
            for file, text in current.items():
                (ROOT / file).write_bytes(text.encode('utf8'))
            tmp = TMP / f'q{n}'
            tmp.mkdir()
            report = REPORT_DIR / f'{sid}.json'
            before = sorted(os.listdir(tmp))
            try:
                code = run(['npx', 'vitest', 'run', '--project', PROJECT, '--reporter=json', f'--outputFile={report}', TEST], tmp)
            finally:
                for file, data in originals.items():
                    (ROOT / file).write_bytes(data)
            after = sorted(os.listdir(tmp))
            data = json.loads(report.read_text())
            rows = [{'test': t['fullName'], 'status': t['status'],
                     'firstErrorLine': next((l for m in t['failureMessages'] for l in m.splitlines() if l.strip()), None)}
                    for r in data['testResults'] for t in r['assertionResults'] if 'records root' in t['fullName']]
            results.append({'id': sid, 'edits': [{'file': f, 'old': o, 'new': nw} for f, o, nw in edits], 'expectation': expect,
                            'exitCode': code, 'counts': {k: data[k] for k in ('numTotalTests', 'numPassedTests', 'numFailedTests')},
                            'rows': rows, 'tmpdir': str(tmp), 'listingBefore': before, 'listingAfter': after,
                            'restored': all(sha((ROOT / f).read_bytes()) == d for f, d in digests.items())})
            print(sid, code, results[-1]['counts'], [(r['status'], r['test'][-60:]) for r in rows], after, flush=True)
    finally:
        for file, data in originals.items():
            (ROOT / file).write_bytes(data)
    OUT.write_text(json.dumps({'commit': git('rev-parse', 'HEAD').strip(), 'results': results,
                               'trackedTreeCleanAfter': git('status', '--porcelain', '--untracked-files=no') == '',
                               'harnessSha256': sha(Path(__file__).read_bytes())}, indent=2) + '\n')
    print('done', flush=True)


main()
