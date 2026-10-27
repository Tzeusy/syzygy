#!/usr/bin/env python3
"""Builds docs/evidence/syzygy-bpyt-4-5/bounds-and-pins.json from the retained results beside it (syzygy-bpyt.4.5). Evidence tool, not authority.

usage: python3 -I build_record.py TREE BASE_COMMIT MAIN_COMMIT EVIDENCE_COMMIT PRIOR_TEST_COMMIT

BASE_COMMIT is where the branch began and where every base-side result ran; MAIN_COMMIT is the main the branch last merged.
The change is `git diff MAIN_COMMIT EVIDENCE_COMMIT`, and each file it touches must be identical at BASE_COMMIT and MAIN_COMMIT,
so the base-side results ran against the bytes the change replaced.

Every digest and total is computed here from the files and git objects, never typed in: the subject (the test files the
change touches, their sha256 at EVIDENCE_COMMIT, and the sha256 of `git diff MAIN EVIDENCE -- <them>`), each tool and
result file's sha256, the census totals at both commits, the mutant outcomes, the CPU separations and the full-suite runs.

What each result must have run against, checked here: the mutants and the head census at EVIDENCE_COMMIT itself; the
daemon-entry probe at a commit whose main.ts, state-directory.ts and daemon-entry test are byte-identical to EVIDENCE_COMMIT's;
both CPU separations (thread CPU on Node 24, and process CPU on Node 22, where the tests' cpuUsage falls back) at a commit
whose three timed test files differ from EVIDENCE_COMMIT's only in `const <NAME>_CPU_MS = ` lines or in lines that are `//`
comments, neither of which changes what the timed regions run.
Each result's tool must hash, at EVIDENCE_COMMIT, to the digest the result records, and each result that reads
tools/mutant-cases.json must record the digest that file has at EVIDENCE_COMMIT.

Checked claims: every mutant case ran as its `expect` says; every CPU bound in the tests sits 10x or more from the head's
slowest region and from the mutant's fastest, on thread CPU and under the process-CPU fallback alike. The bounds were set
at 3fc3709f at the geometric mean of the first separation and are not refitted: each later run's mean is recorded as
`geometricMeanNowMs`; on the daemon entry, every `defect` mutant fails the new test, every
`hook` mutant fails the load-hook row, every defect the old text pin failed the new test also fails, the R- mutants
(rev-532's daemon-path loads) pass the kept text row as it stood at PRIOR_TEST_COMMIT and fail it now, and the three
equivalents whose kills were dropped (E-comment-in-branch, E-renamed-binding, E-branch-swap) pass the new test. The narrative fields (`sites`, `residuals`) are the lane's own words.
"""
import glob, hashlib, json, math, os, re, subprocess, sys

tree, base, main, ev, prior = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
here = os.path.join(tree, 'docs/evidence/syzygy-bpyt-4-5')
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, check=True).stdout
sha = lambda b: hashlib.sha256(b).hexdigest()
load = lambda name: json.load(open(os.path.join(here, name), encoding='utf8'))
base, main, ev, prior = (git('rev-parse', c).decode().strip() for c in (base, main, ev, prior))
changed = sorted(p for p in git('diff', '--name-only', main, ev).decode().split('\n') if p)
for p in changed:
    if not p.startswith('docs/evidence/syzygy-bpyt-4-5/') and subprocess.run(['git', 'diff', '--quiet', base, main, '--', p], cwd=tree).returncode != 0:
        sys.exit(f'{p} differs between {base} and {main}')
tests = [p for p in changed if p.startswith(('apps/', 'packages/'))]
MAIN, STATE, DE_TEST = 'apps/syzygy/src/main.ts', 'packages/polaris-dossier/src/state-directory.ts', 'packages/cap1-system/src/daemon-entry-unchanged.system.test.ts'

mutants, census_base, census_head = load('bound-and-pin-mutants.json'), load('census-base.json'), load('census-head.json')
de_head, de_base, sep = load('daemon-entry-head.json'), load('daemon-entry-base-test.json'), load('cpu-separation.json')
de_prior, sep22 = load('daemon-entry-prior-test.json'), load('cpu-separation-node22.json')
if de_prior['testFileFrom'] != prior: sys.exit(f'daemon-entry-prior-test ran the test from {de_prior["testFileFrom"]}, not {prior}')
if sep['cpuSource'] != 'thread' or sep22['cpuSource'] != 'process' or not sep22['node'].startswith('v22.'):
    sys.exit('the CPU separations are not one thread-CPU run and one process-CPU run on Node 22')
for name, at in (('mutants', mutants['tree']), ('census-head', census_head['commit'])):
    if at != ev: sys.exit(f'{name} ran at {at}, not {ev}')
if census_base['commit'] != base or mutants['base'] != base or de_base['testFileFrom'] != base: sys.exit('a base-side result names another base')
for name, record in (('daemon-entry-head', de_head), ('daemon-entry-base-test', de_base), ('daemon-entry-prior-test', de_prior)):
    if subprocess.run(['git', 'diff', '--quiet', record['commit'], ev, '--', MAIN, STATE, DE_TEST], cwd=tree).returncode != 0:
        sys.exit(f'{name}: {MAIN}, {STATE} or the test differ between {record["commit"]} and {ev}')
cpu_files = sorted({s['file'] for s in sep['sites']})
for name, record in (('cpu-separation', sep), ('cpu-separation-node22', sep22)):
    for line in git('diff', '-U0', record['tree'], ev, '--', *cpu_files).decode().split('\n'):
        if line.startswith(('+++', '---')) or not line.startswith(('+', '-')): continue
        if not re.match(r'^[+-](const [A-Z_]+_CPU_MS = [0-9_]+;|\s*//)', line): sys.exit(f'{name}: a line other than a bound or a comment differs from {ev}: {line}')
cases_sha = sha(git('show', f'{ev}:docs/evidence/syzygy-bpyt-4-5/tools/mutant-cases.json'))
for name, record in (('mutants', mutants), ('cpu-separation', sep), ('cpu-separation-node22', sep22)):
    if record['cases']['sha256'] != cases_sha: sys.exit(f'{name} used a mutant-cases.json other than the one at {ev}')
for name, record in (('mutants', mutants), ('daemon-entry-head', de_head), ('daemon-entry-base-test', de_base), ('daemon-entry-prior-test', de_prior),
                     ('cpu-separation', sep), ('cpu-separation-node22', sep22), ('census', census_head)):
    path = f'docs/evidence/syzygy-bpyt-4-5/tools/{record["tool"]["name"]}'
    if sha(git('show', f'{ev}:{path}')) != record['tool']['sha256']: sys.exit(f'{name}: tool digest differs from {ev}')

cases = {c['id']: c for c in mutants['results']}
def ran_as_expected(ids):
    for i in ids:
        if i not in cases: sys.exit(f'no mutant case {i}')
        if not all(s['asExpected'] for s in cases[i]['sides']): sys.exit(f'case {i} did not run as expected')
    def said(s):
        failed = [r for r in s.get('rows', []) if r['status'] == 'failed']
        return 'fail (by the test timeout)' if s['outcome'] == 'fail' and failed and all(r.get('byTimeout') for r in failed) else s['outcome']
    return {i: {s['side']: said(s) for s in cases[i]['sides']} for i in ids}
if not all(s['asExpected'] for c in cases.values() for s in c['sides']): sys.exit('a mutant case did not run as expected')

bounds_at_ev = {}
for f in cpu_files:
    for m in re.finditer(r'^const ([A-Z_]+_CPU_MS) = ([0-9_]+);', git('show', f'{ev}:{f}').decode(), re.M): bounds_at_ev[m.group(1)] = int(m.group(2).replace('_', ''))
fallback = {}
for s in sep22['sites']:
    b = bounds_at_ev.get(s['bound'])
    if b is None or s['fileBound']['ms'] != b or not s['fileBound']['separated']: sys.exit(f'{s["bound"]}: not 10x from both sides under the process-CPU fallback')
    fallback[s['bound']] = {'node': sep22['node'], 'cpuSource': 'process', 'headRuns': len(s['headRuns']), 'headMaxMs': s['headMaxMs'], 'mutantMinMs': s['mutantMinMs'],
                            'mutantMinIsLowerBound': s['mutantMinIsLowerBound'], 'boundOverHeadMax': s['fileBound']['overHeadMax'], 'mutantMinOverBound': s['fileBound']['mutantMinOver']}
separation = {}
for s in sep['sites']:
    b = bounds_at_ev.get(s['bound'])
    if b is None or s['fileBound']['ms'] != b: sys.exit(f'{s["bound"]}: the separation measured a bound other than the {b} the test holds')
    if not (s['fileBound']['separated'] and b / s['headMaxMs'] >= 10 and s['mutantMinMs'] / b >= 10): sys.exit(f'{s["bound"]}: not 10x from both sides')
    loads = [r['load1Start'] for r in s['headRuns']] + [r['load1End'] for r in s['headRuns']]
    separation[s['bound']] = {
        'file': s['file'], 'boundMs': b, 'headRuns': len(s['headRuns']), 'headMaxMs': s['headMaxMs'], 'headLoad1': [min(loads), max(loads)],
        'mutants': [{'id': m['id'], 'title': m['title'], 'runs': len(m['runs']), 'cappedRuns': m['cappedRuns'], 'minMs': m['min'], 'reached': m['reached']} for m in s['mutants']],
        'mutantMinMs': s['mutantMinMs'], 'mutantMinIsLowerBound': s['mutantMinIsLowerBound'],
        'boundOverHeadMax': round(b / s['headMaxMs'], 1), 'mutantMinOverBound': round(s['mutantMinMs'] / b, 1), 'geometricMeanNowMs': s['proposedBoundMs'],
        'underProcessCpuFallback': fallback[s['bound']]}

SITES = [
    {'site': 'apps/three-surface-poc/src/capture-test-artifact-main.test.ts:381 (base)', 'was': 'expect(Date.now() - started).toBeLessThan(5_000)',
     'property': 'a FIFO is refused before any open', 'now': 'the lstat-refusal message alone; no elapsed bound',
     'mutants': ['fifo-no-lstat', 'fifo-blocking-open']},
    {'site': 'apps/three-surface-poc/src/main.test.ts:547 (base)', 'was': 'expect(Date.now() - began).toBeLessThan(WAIT_MS / 2)',
     'property': 'started() reports a finished run at once', 'now': "a bound twice the test's own timeout, so a report made at the bound times the test out",
     'mutants': ['started-waits-for-bound']},
    {'site': 'packages/polaris-dossier/src/git-object-reader.test.ts:581 (base) and the refusedWithin call sites (refusedWithinCallSites)', 'was': 'expect(Date.now() - started).toBeLessThan(30_000); refusedWithin(2000 | 5000 | 30_000, ...)',
     'property': 'refusal by the byte budget, the depth cap or the stored bound; a special file never blocks', 'now': "refusal() and each test's own timeout",
     'mutants': ['reader-no-call-budget', 'reader-no-depth-cap', 'reader-blocking-open', 'reader-no-stored-bound']},
    {'site': 'packages/polaris-generation-core/src/dossier-profile.test.ts:167 (base)', 'was': 'expect(performance.now() - started).toBeLessThan(2000)',
     'property': 'the edge trim is linear', 'now': 'EDGE_TRIM_CPU_MS, a CPU-time bound; each filler also goes in as a blank run between visible characters, the shape the old regex is quadratic on',
     'finding': 'The base guard is vacuous: the backtracking edge trim it names passes the base test (edge-backtracking-regex, base side), because no base timed input has a blank run between visible characters.',
     'mutants': ['edge-backtracking-regex'], 'bound': 'EDGE_TRIM_CPU_MS'},
    {'site': 'packages/polaris-generation-core/src/excerpt.test.ts:262 (base), 2 cases', 'was': 'expect(Date.now() - started).toBeLessThan(500)',
     'property': 'a line past the pattern prefix is never pattern-matched', 'now': 'HOSTILE_LINE_CPU_MS, a CPU-time bound',
     'finding': "The bound has a predicate of its own: with the prefix cap removed and FUNCTION_LINE backtracking, the `an identifier` case's output assertion still passes once the bound is deleted and vitest's timeout lifted (excerpt-time-only).",
     'mutants': ['excerpt-quadratic-pattern-only', 'excerpt-no-prefix-cap', 'excerpt-no-cap-quadratic-pattern', 'excerpt-time-only'], 'bound': 'HOSTILE_LINE_CPU_MS'},
    {'site': 'packages/three-surface-poc-core/src/test-artifact-verification.test.ts:96 (base), 3 cases', 'was': 'expect(performance.now() - started).toBeLessThan(2_000)',
     'property': 'the JUnit tag scan is linear', 'now': 'TAG_SCAN_CPU_MS, a CPU-time bound', 'mutants': ['junit-tag-regex'], 'bound': 'TAG_SCAN_CPU_MS'},
    {'site': 'packages/three-surface-poc-core/src/test-artifact-verification.test.ts:103 (base)', 'was': 'expect(performance.now() - started).toBeLessThan(2_000)',
     'property': 'the JUnit attribute scan is linear', 'now': 'ATTRIBUTE_SCAN_CPU_MS, a CPU-time bound', 'mutants': ['junit-attr-regex'], 'bound': 'ATTRIBUTE_SCAN_CPU_MS'},
    {'site': 'packages/polaris-generation-core/src/dossier-evaluation.test.ts:107-113,127-131 (base)', 'was': 'byte literals 1038, 670, 235, 1273, 669',
     'property': 'page bytes, bytes through the last level-0 close, per-depth and total bytes', 'now': 'counts taken from the fixture text',
     'mutants': ['dossier-page-bytes-plus-one', 'dossier-first-level-short', 'dossier-total-first-page', 'dossier-budget-first-level-short', 'dossier-budget-total-first-page']},
    {'site': 'apps/three-surface-poc/src/polaris-generation/redis-shaped-discovery.test.ts:137 (base)', 'was': 'expect(bytes.selected).toBeGreaterThan(390_000)',
     'property': 'the byte cap is filled greedily', 'now': 'every unsplit deferred file holds more quotable bytes than the room left; the 400,000 cap stays (the contract, named in the describe title)',
     'mutants': ['redis-stop-at-first-misfit']},
    {'site': 'apps/three-surface-poc/src/polaris-generation/self-corpus.test.ts:11 (base), PINNED_MAIN', 'was': 'an exact 40-hex commit pin',
     'property': "the self-corpus denominator is the one the M7 record measured", 'disposition': 'kept',
     'now': 'kept as an exact pin: the commit is the contract docs/evidence/polaris-m7-synthetic-successor-2026-09-23.json binds, and node-ci.yml checks out with fetch-depth: 0 to keep it in a hosted checkout; the comment above the constant says so',
     'mutants': []},
    {'site': 'apps/three-surface-poc/src/polaris-generation/redis-shaped-discovery.test.ts:152,159 (base), the two [Observed] rows', 'was': 'exact byte totals {selected, deferred, cap}',
     'property': 'what selection measured on the fixed fixture corpus', 'disposition': 'kept',
     'now': "kept: each row reports an observation over the fixed fixture corpus, so its totals are the observation and not a bound; the greedy fill is the :137 (base) row's property; the comment above the two rows says so",
     'mutants': []},
]
for s in SITES:
    s['outcomes'] = ran_as_expected(s['mutants'])
    if 'bound' in s: s['separation'] = separation[s['bound']]
controls = ran_as_expected(sorted(i for i in cases if i.startswith('control-')))

PIN = 'each import is dynamic and inside the `dossier` or `polaris` branch'
HOOK_ROW, TEXT_ROW = 'the daemon path never loads the POC app, and the `dossier render` branch does', 'every line of main.ts naming the POC app sits inside the `dossier` or the `polaris` branch'
PRIOR_TEXT_ROW = 'every line of main.ts naming the POC app sits in the `dossier` and `polaris` branches'
REV_LOADS, DROPPED_EQUIVALENTS = ['R1-flag-between-branches', 'R2-flag-createRequire-before-daemon', 'R3-runtime-hook'], ['E-comment-in-branch', 'E-renamed-binding', 'E-branch-swap']
def outcome(record):
    out = {}
    for r in record['results']:
        mid = (r['mutant'] or {}).get('id', 'control')
        out[mid] = {'kind': (r['mutant'] or {}).get('kind'), 'skipped': r.get('skipped'), 'passed': r['passed'], 'failed': r['failed']}
    return out
new, old, prior_test = outcome(de_head), outcome(de_base), outcome(de_prior)
if new['control']['failed'] or old['control']['failed'] or prior_test['control']['failed']: sys.exit('a daemon-entry control failed')
for mid in REV_LOADS:
    if prior_test[mid]['failed'] or not prior_test[mid]['passed']: sys.exit(f'{mid}: fails the kept text row as it stood at {prior}, so it is not the survivor rev-532 found')
    if not any(TEXT_ROW in t for t in new[mid]['failed']): sys.exit(f'{mid}: the narrowed text row passes it')
for mid in DROPPED_EQUIVALENTS:
    if new[mid]['failed']: sys.exit(f'{mid}: an equivalent the new test fails')
for mid, r in new.items():
    rows = r['failed']
    if r['kind'] == 'defect' and not rows: sys.exit(f'{mid}: a defect the new test passes')
    if r['kind'] == 'hook' and not any(HOOK_ROW in t for t in rows): sys.exit(f'{mid}: a hook mutant the load-hook row passes')
    pin_killed = any(PIN in t for t in old.get(mid, {}).get('failed', []))
    if r['kind'] == 'defect' and pin_killed and not rows: sys.exit(f'{mid}: the old pin killed it and the new test does not')
daemon_entry = {
    'mutants': [{'id': mid, 'kind': r['kind'], 'newHookRow': 'fail' if any(HOOK_ROW in t for t in r['failed']) else 'pass',
                 'newTextRow': 'fail' if any(TEXT_ROW in t for t in r['failed']) else 'pass',
                 'newOtherRows': sorted(t for t in r['failed'] if HOOK_ROW not in t and TEXT_ROW not in t),
                 'oldTextPin': 'skipped' if old[mid]['skipped'] else ('fail' if any(PIN in t for t in old[mid]['failed']) else 'pass'),
                 'oldOtherRows': sorted(t for t in old[mid]['failed'] if PIN not in t),
                 'priorTest': 'skipped' if prior_test[mid]['skipped'] else ('pass' if not prior_test[mid]['failed'] else sorted(prior_test[mid]['failed']))} for mid, r in new.items()],
    'priorTestFrom': prior,
    'note': 'defect: the daemon path loads the POC app on some argv or event; equivalent: nothing on any daemon path loads it; hook: the load hook itself is broken.'}
daemon_entry['pinKillsDropped'] = [m['id'] for m in daemon_entry['mutants'] if m['oldTextPin'] == 'fail' and m['newHookRow'] == 'pass' and m['newTextRow'] == 'pass']
daemon_entry['pinMisses'] = [m['id'] for m in daemon_entry['mutants'] if m['kind'] == 'defect' and m['oldTextPin'] == 'pass']

THIRD = r'hrtime|performance\.now\(\)|Date\.now\(\) *-|elapsed|getTime\(\) *-|[cC]puUsage'
third = [l for l in git('grep', '-n', '-E', THIRD, ev, '--', 'apps/*.test.*', 'packages/*.test.*').decode().split('\n') if l]
grep_n = lambda commit, pattern, path: [l for l in subprocess.run(['git', 'grep', '-n', '-F', pattern, commit, '--', path], cwd=tree, capture_output=True, text=True).stdout.split('\n') if l]
READER = 'packages/polaris-dossier/src/git-object-reader.test.ts'
refused_within = {'base': [l for l in grep_n(base, 'refusedWithin(', READER) if 'function refusedWithin' not in l and 'const refusedWithin' not in l],
                  'head': grep_n(ev, 'refusedWithin', READER)}
timeouts = [r for r in census_head['rows'] if r['kind'].startswith('timeout')]
RESIDUALS = [
    'process.threadCpuUsage() exists from Node 23.9.0 while package.json engines admits Node 22.15 and later. On a Node 22 the tests fall back to process.cpuUsage(), which also counts the worker process\'s other threads (garbage collection, compilation): each bound\'s separation under that fallback, on Node 22, is `underProcessCpuFallback`. CI and this host run Node 24.',
    'The near-miss tag-names case runs under TAG_SCAN_CPU_MS with no mutant that fails it: the replaced scan is linear on that input too, so the bound rests on the other two cases; the test says so in a comment.',
    'A capped mutant run gives a lower bound on its region, not the region: the mutant minimum for those bounds is at least the cap, so each bound sits at least as far from the mutant as recorded.',
    'The kept daemon-entry text row also fails a mutant that loads nothing: a type-only import naming the POC app at module top (E-type-only-import), and a comment naming it outside the two branches would fail it the same way. The equivalents it passes are in daemonEntry.',
    "dossier-evaluation's INDEX and DEEP fixtures are ASCII, so a module that counted string length instead of UTF-8 bytes would pass every byte assertion there, at the base (literals) and at the head (counts) alike.",
    'A FIFO capture with the lstat refusal removed blocks in a synchronous open at both sides: the row fails by the test timeout or the run is killed, never by a fast refusal (fifo-blocking-open).',
    'Explicit timeouts are harness bounds, not assertions, and are out of this bead (syzygy-bpyt.4.31); most carry no one-line reason (unreasonedTimeouts).',
    'Two concurrent full-suite runs were not green on this host at the base or the head alike (attempts 1 to 3): every failure was a 5 s default timeout or a 10 s hook timeout in a file this change does not touch. One run at a time, twice in sequence, was green (attempts 4 and 5).',
]
row_delta = subprocess.run([sys.executable, '-I', os.path.join(here, 'tools', 'row_delta.py'), tree, main, ev], capture_output=True, text=True, check=True).stdout.splitlines()
suites = [load(os.path.relpath(p, here)) for p in sorted(glob.glob(os.path.join(here, 'full-suite', 'attempt-*.json')))]
durations = [load(os.path.relpath(p, here)) for p in sorted(glob.glob(os.path.join(here, 'durations', '*.json')))]

files = sorted(p for p in glob.glob(os.path.join(here, '**', '*'), recursive=True) if os.path.isfile(p) and not p.endswith('bounds-and-pins.json'))
record = {
    'schema': 'syzygy-bpyt-4-5-bounds-and-pins/2', 'bead': 'syzygy-bpyt.4.5',
    'subject': {'base': base, 'main': main, 'evidenceCommit': ev, 'testFiles': [{'path': p, 'sha256': sha(git('show', f'{ev}:{p}'))} for p in tests],
                'testDiffSha256': sha(git('diff', main, ev, '--', *tests)), 'note': 'The test files are the subject; no product file differs between base and the evidence commit.'},
    'productFilesChanged': [p for p in changed if not p.startswith('docs/evidence/syzygy-bpyt-4-5/') and p not in tests],
    'resultsRanAt': {'mutants': mutants['tree'], 'censusHead': census_head['commit'], 'daemonEntryHead': de_head['commit'], 'daemonEntryOldTest': de_base['commit'], 'daemonEntryPriorTest': de_prior['commit'],
                     'cpuSeparation': sep['tree'], 'cpuSeparationNode22': sep22['tree']},
    'files': [{'path': os.path.relpath(p, tree), 'sha256': sha(open(p, 'rb').read())} for p in files],
    'ac1Sweep': {'population': {'base': census_base['population'], 'head': census_head['population']},
                 'elapsedFirstMethod': {'base': census_base['summary'].get('elapsed', {}).get('lines', 0), 'head': census_head['summary'].get('elapsed', {}).get('lines', 0),
                                        'baseLines': [r for r in census_base['rows'] if r['kind'] == 'elapsed']},
                 'elapsedSecondMethod': {'base': len(census_base['secondMethod']), 'head': len(census_head['secondMethod']), 'headLines': census_head['secondMethod']},
                 'thirdMethod': {'regex': THIRD, 'over': 'apps/*.test.* and packages/*.test.* at the evidence commit, git grep -E', 'lines': third},
                 'refusedWithinCallSites': refused_within,
                 'raceTimers': {'base': [r for r in census_base['rows'] if r['kind'] == 'race'], 'head': [r for r in census_head['rows'] if r['kind'] == 'race']},
                 'cpuBounds': {'lines': [r for r in census_head['rows'] if r['kind'] == 'cpu-bound'], 'justification': 'CPU time of the thread running the test, not wall time; each bound and its separation in `sites`.'},
                 'clockReadingsAtHead': {cls: sum(1 for r in census_head['rows'] if r['kind'] == 'clock' and r['class'] == cls) for cls in ('deadline', 'now-input')},
                 'unreasonedTimeouts': {'sites': len(timeouts), 'withReason': sum(1 for r in timeouts if r['reason']),
                                        'withoutReason': sum(1 for r in timeouts if not r['reason']), 'files': census_head['unreasonedTimeoutFiles'], 'bead': 'syzygy-bpyt.4.31'}},
    'sites': SITES, 'controls': controls, 'residuals': RESIDUALS,
    'mutantTotals': {'cases': len(cases), 'sides': sum(len(c['sides']) for c in cases.values()), 'asExpected': sum(s['asExpected'] for c in cases.values() for s in c['sides'])},
    'daemonEntry': daemon_entry,
    'rowDelta': {'tool': 'row_delta.py', 'base': main, 'head': ev, 'lines': row_delta},
    'wallDurations': durations, 'fullSuite': suites,
}
open(os.path.join(here, 'bounds-and-pins.json'), 'w', encoding='utf8').write(json.dumps(record, indent=1, ensure_ascii=False) + '\n')
print(json.dumps({'rowDelta': row_delta[-1], 'testFiles': len(tests), 'productFilesChanged': record['productFilesChanged'], 'mutantTotals': record['mutantTotals'],
                  'ac1': record['ac1Sweep']['elapsedFirstMethod']['head'], 'bounds': {k: (v['boundMs'], v['boundOverHeadMax'], v['mutantMinOverBound']) for k, v in separation.items()},
                  'pinKillsDropped': daemon_entry['pinKillsDropped'], 'pinMisses': daemon_entry['pinMisses']}))
