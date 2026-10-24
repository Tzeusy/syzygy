#!/usr/bin/env python3
"""Builds docs/evidence/syzygy-bpyt-4-5/bounds-and-pins.json from the retained results beside it (syzygy-bpyt.4.5). Evidence tool, not authority.

usage: python3 -I build_record.py TREE BASE_COMMIT EVIDENCE_COMMIT

Every digest and total is computed here from the files and git objects, never typed in: the subject (the test files the
change touches, their sha256 at EVIDENCE_COMMIT, and the sha256 of `git diff BASE EVIDENCE -- <them>`), each tool and
result file's sha256, the census totals at both commits, the mutant outcomes and the full-suite runs. The narrative fields
(`sites`, `residuals`) are the lane's own claims, checked against the results where a result exists: each site's mutant ids
must be cases in the mutant record and each must have run as expected.
"""
import glob, hashlib, json, os, subprocess, sys

tree, base, ev = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3]
here = os.path.join(tree, 'docs/evidence/syzygy-bpyt-4-5')
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, check=True).stdout
sha = lambda b: hashlib.sha256(b).hexdigest()
load = lambda name: json.load(open(os.path.join(here, name), encoding='utf8'))
base, ev = git('rev-parse', base).decode().strip(), git('rev-parse', ev).decode().strip()
tests = sorted(p for p in git('diff', '--name-only', base, ev, '--', 'apps', 'packages').decode().split('\n') if p)

mutants, census_base, census_head = load('bound-and-pin-mutants.json'), load('census-base.json'), load('census-head.json')
de_head, de_base, cpu = load('daemon-entry-head.json'), load('daemon-entry-base-test.json'), load('cpu-margins.json')
for name, record, key in (('mutants', mutants, 'tree'), ('daemon-entry-head', de_head, 'commit'), ('daemon-entry-base-test', de_base, 'commit'),
                          ('cpu-margins', cpu, 'tree'), ('census-head', census_head, 'commit')):
    if record[key] != ev: sys.exit(f'{name} ran at {record[key]}, not {ev}')
if census_base['commit'] != base or mutants['base'] != base or de_base['testFileFrom'] != base: sys.exit('a base-side result names another base')
for name, record in (('mutants', mutants), ('daemon-entry-head', de_head), ('cpu-margins', cpu), ('census', census_head)):
    path = os.path.join(here, 'tools', record['tool']['name'])
    if sha(git('show', f'{ev}:{os.path.relpath(path, tree)}')) != record['tool']['sha256']: sys.exit(f'{name}: tool digest differs from {ev}')

cases = {c['id']: c for c in mutants['results']}
def killed_as_expected(ids):
    for i in ids:
        if i not in cases: sys.exit(f'no mutant case {i}')
        if not all(s['asExpected'] for s in cases[i]['sides']): sys.exit(f'case {i} did not run as expected')
    return {i: {s['side']: s['outcome'] for s in cases[i]['sides']} for i in ids}

SITES = [
    {'site': 'apps/three-surface-poc/src/capture-test-artifact-main.test.ts:381 (base)', 'was': 'expect(Date.now() - started).toBeLessThan(5_000)',
     'property': 'a FIFO is refused before any open', 'now': 'the lstat-refusal message alone; no elapsed bound',
     'mutants': ['fifo-no-lstat', 'fifo-blocking-open']},
    {'site': 'apps/three-surface-poc/src/main.test.ts:547 (base)', 'was': 'expect(Date.now() - began).toBeLessThan(WAIT_MS / 2)',
     'property': 'started() reports a finished run at once', 'now': "a bound twice the test's own timeout, so a report made at the bound times the test out",
     'mutants': ['started-waits-for-bound']},
    {'site': 'packages/polaris-dossier/src/git-object-reader.test.ts:581 (base) and refusedWithin, 9 call sites', 'was': 'expect(Date.now() - started).toBeLessThan(30_000); refusedWithin(2000 | 5000 | 30_000, ...)',
     'property': 'refusal by the byte budget, the depth cap or the stored bound; a special file never blocks', 'now': "refusal() and each test's own timeout",
     'mutants': ['reader-no-call-budget', 'reader-no-depth-cap', 'reader-blocking-open', 'reader-no-stored-bound']},
    {'site': 'packages/polaris-generation-core/src/dossier-profile.test.ts:167 (base)', 'was': 'expect(performance.now() - started).toBeLessThan(2000)',
     'property': 'the edge trim is linear', 'now': 'a CPU-time bound, and each filler also as a blank run between visible characters',
     'mutants': ['edge-backtracking-regex']},
    {'site': 'packages/polaris-generation-core/src/excerpt.test.ts:262 (base), 2 cases', 'was': 'expect(Date.now() - started).toBeLessThan(500)',
     'property': 'a line past the pattern prefix is never pattern-matched', 'now': 'a CPU-time bound',
     'mutants': ['excerpt-quadratic-pattern-only', 'excerpt-no-prefix-cap', 'excerpt-no-cap-quadratic-pattern']},
    {'site': 'packages/three-surface-poc-core/src/test-artifact-verification.test.ts:96,103 (base), 4 cases', 'was': 'expect(performance.now() - started).toBeLessThan(2_000)',
     'property': 'the JUnit tag and attribute scans are linear', 'now': 'a CPU-time bound', 'mutants': ['junit-tag-regex', 'junit-attr-regex']},
    {'site': 'packages/polaris-generation-core/src/dossier-evaluation.test.ts:107-113,127-131 (base)', 'was': 'byte literals 1038, 670, 235, 1273, 669',
     'property': 'page bytes, bytes through the last level-0 close, per-depth and total bytes', 'now': 'counts taken from the fixture text',
     'mutants': ['dossier-page-bytes-plus-one', 'dossier-first-level-short', 'dossier-total-first-page', 'dossier-budget-first-level-short', 'dossier-budget-total-first-page']},
    {'site': 'apps/three-surface-poc/src/polaris-generation/redis-shaped-discovery.test.ts:137 (base)', 'was': 'expect(bytes.selected).toBeGreaterThan(390_000)',
     'property': 'the byte cap is filled greedily', 'now': 'every unsplit deferred file holds more quotable bytes than the room left; the 400,000 cap stays (the contract, named in the describe title)',
     'mutants': ['redis-stop-at-first-misfit']},
]
for s in SITES: s['outcomes'] = killed_as_expected(s['mutants'])
controls = killed_as_expected(sorted(i for i in cases if i.startswith('control-')))

def row_failed(record, mutant_id):
    r = next(x for x in record['results'] if (x['mutant'] or {}).get('id', 'control') == mutant_id or (x['mutant'] is None and mutant_id == 'control'))
    return 'skipped' if r.get('skipped') else {'passed': r['passed'], 'failed': r['failed']}
de_ids = ['control'] + [m['mutant']['id'] for m in de_head['results'] if m['mutant']]

THIRD = r'hrtime|performance\.now\(\)|Date\.now\(\) *-|elapsed|getTime\(\) *-|cpuUsage'
third = [l for l in git('grep', '-n', '-E', THIRD, ev, '--', 'apps/*.test.*', 'packages/*.test.*').decode().split('\n') if l]
timeouts = [r for r in census_head['rows'] if r['kind'].startswith('timeout')]
RESIDUALS = [
    'The CPU-time bounds read process.cpuUsage(), which counts every thread of the worker process, so garbage collection or other work in the same worker during the region counts toward the bound; the worst of 5 runs leaves the margins in cpuMargins.',
    "dossier-evaluation's INDEX and DEEP fixtures are ASCII, so a module that counted string length instead of UTF-8 bytes would pass every byte assertion there, at the base (literals) and at the head (counts) alike.",
    'A FIFO capture with the lstat refusal removed blocks in a synchronous open at both sides: the row fails by the test timeout or the run is killed, never by a fast refusal (fifo-blocking-open).',
    'Explicit timeouts are harness bounds, not assertions, and stay; most carry no one-line reason (unreasonedTimeouts).',
    'Two concurrent full-suite runs were not green on this host at the base or the head alike (attempts 1 to 3): every failure was a 5 s default timeout or a 10 s hook timeout in a file this change does not touch. One run at a time, twice in sequence, was green (attempt 4).',
]
row_delta = subprocess.run([sys.executable, '-I', os.path.join(here, 'tools', 'row_delta.py'), tree, base, ev], capture_output=True, text=True, check=True).stdout.splitlines()
suites = []
for attempt in sorted(glob.glob(os.path.join(here, 'full-suite', 'attempt-*.json'))):
    suites.append(load(os.path.relpath(attempt, here)))

files = sorted(p for p in glob.glob(os.path.join(here, '**', '*'), recursive=True) if os.path.isfile(p) and not p.endswith('bounds-and-pins.json'))
record = {
    'schema': 'syzygy-bpyt-4-5-bounds-and-pins/1', 'bead': 'syzygy-bpyt.4.5',
    'subject': {'base': base, 'evidenceCommit': ev, 'testFiles': [{'path': p, 'sha256': sha(git('show', f'{ev}:{p}'))} for p in tests],
                'testDiffSha256': sha(git('diff', base, ev, '--', *tests)), 'note': 'The test files are the subject; no product file differs between base and the evidence commit.'},
    'productFilesChanged': sorted(p for p in git('diff', '--name-only', base, ev).decode().split('\n') if p and not p.startswith('docs/evidence/syzygy-bpyt-4-5/') and p not in tests),
    'files': [{'path': os.path.relpath(p, tree), 'sha256': sha(open(p, 'rb').read())} for p in files],
    'ac1Sweep': {'population': {'base': census_base['population'], 'head': census_head['population']},
                 'elapsedFirstMethod': {'base': census_base['summary'].get('elapsed', {}).get('lines', 0), 'head': census_head['summary'].get('elapsed', {}).get('lines', 0)},
                 'elapsedSecondMethod': {'base': len(census_base['secondMethod']), 'head': len(census_head['secondMethod']), 'headLines': census_head['secondMethod']},
                 'raceTimers': {'base': census_base['summary'].get('race', {}).get('lines', 0), 'head': [r for r in census_head['rows'] if r['kind'] == 'race']},
                 'cpuBounds': [r for r in census_head['rows'] if r['kind'] == 'cpu-bound'],
                 'thirdMethod': {'regex': THIRD, 'over': 'apps/*.test.* and packages/*.test.* at the evidence commit, git grep -E', 'lines': third},
                 'unreasonedTimeouts': {'sites': len(timeouts), 'withReason': sum(1 for r in timeouts if r['reason']),
                                        'withoutReason': sum(1 for r in timeouts if not r['reason']), 'files': census_head['unreasonedTimeoutFiles']},
                 'clockReadingsAtHead': {cls: sum(1 for r in census_head['rows'] if r['kind'] == 'clock' and r['class'] == cls) for cls in ('deadline', 'now-input')}},
    'sites': SITES, 'controls': controls, 'residuals': RESIDUALS,
    'mutantTotals': {'cases': len(cases), 'sides': sum(len(c['sides']) for c in cases.values()), 'asExpected': sum(s['asExpected'] for c in cases.values() for s in c['sides'])},
    'daemonEntry': {'newRow': {i: row_failed(de_head, i) for i in de_ids}, 'oldTextPin': {i: row_failed(de_base, i) for i in de_ids}},
    'rowDelta': {'tool': 'row_delta.py', 'base': base, 'head': ev, 'lines': row_delta},
    'cpuMargins': cpu['worst'], 'fullSuite': suites,
}
open(os.path.join(here, 'bounds-and-pins.json'), 'w', encoding='utf8').write(json.dumps(record, indent=1, ensure_ascii=False) + '\n')
print(json.dumps({'rowDelta': row_delta[-1], 'testFiles': len(tests), 'productFilesChanged': record['productFilesChanged'], 'mutantTotals': record['mutantTotals'], 'ac1': record['ac1Sweep']['elapsedFirstMethod']}))
