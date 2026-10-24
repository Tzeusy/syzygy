#!/usr/bin/env python3
"""Join the census runs, the tracer's logs and the static site census into one record of every scratch prefix.

Usage: assemble_census.py <worktree> <commit> <static-sites.json> <runs-directory> <probe-directory> <out.json>
       assemble_census.py --selftest <out.json>

<runs-directory> holds, for each label, <label>.json (census_run.py's record), <label>.trace.jsonl.gz and <label>.samples.json, as
collect_runs.py writes them, and optionally operator-notes.json ({label: [text, ...]}). Every run must name <commit>, and so must the
static census. <probe-directory> must not exist or be empty and be a short absolute path: the assembler runs `npx vitest --version`
there once, to record which entries the launcher alone leaves in a temp directory.

What a name is: a name the trace logged as created by mkdtemp is classed by its prefix (the pid and namespace digits of an owner-pid
name replaced by <pid> and <ns>); a name the trace logged as a mkdir or file creation is a fixed name, or a derived name when it
starts with a mkdtemp name of the same run; a name no trace line covers is classed by shape: a Chrome singleton directory, a
21-character vitest project directory, npm's compile cache, or else unattributed. Dispositions come from RULES below, first
match wins; a class that matches none stops the assembler.

--selftest runs the classifier and the rule table over a fixture whose expected answer is written as literals here, then over
mutants of this file (one predicate changed in each), and requires every mutant to fail.
"""
import collections
import functools
import gzip
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

SUFFIXES = ('.ts', '.mts', '.cts', '.js', '.mjs', '.cjs', '.py', '.sh')
NO_FRAME = '(no frame under the repository)'
TEST_FILE = re.compile(r'\.(?:browser\.)?test\.(?:ts|mts|cts|js|mjs)$|\.testkit\.ts$')
CHROME = re.compile(r'^\.?(?:com\.google\.Chrome|org\.chromium\.Chromium)\.[A-Za-z0-9]+$')
NANOID = re.compile(r'^[A-Za-z0-9_-]{21}$')
OWNER_PID = re.compile(r'-p\d+-n\d+-')
NUMERIC = re.compile(r'(?<![A-Za-z0-9])\d+(?![A-Za-z0-9])')
STEM = re.compile(r'[A-Za-z][A-Za-z.]*(?:-[A-Za-z][A-Za-z.]*)*-')


def normalise(prefix: str) -> str:
    return OWNER_PID.sub('-p<pid>-n<ns>-', prefix)


class Index:
    """What one run's trace says about the names in its temp directory."""

    def __init__(self, rows: list):
        self.made = {}  # basename -> normalised prefix, for mkdtemp
        self.seen = collections.defaultdict(list)  # basename -> rows
        for row in rows:
            name = os.path.basename(row['path'])
            self.seen[name].append(row)
            if row['kind'] == 'mkdtemp':
                self.made[name] = normalise(row['prefix'])


def classify(name: str, index: Index) -> tuple:
    if name in index.made:
        return ('mkdtemp', index.made[name])
    if name in index.seen:
        for made, prefix in index.made.items():
            if name.startswith(made) and name != made:
                return ('derived', prefix + '<random>' + name[len(made):])
        return ('fixed', name)
    if CHROME.match(name):
        return ('chrome-singleton', 'chrome-singleton-directory')
    if NANOID.match(name):
        return ('vitest-project-directory', 'nanoid-21')
    if name == 'node-compile-cache':
        return ('npm-compile-cache', 'node-compile-cache')
    return ('unattributed', NUMERIC.sub('<n>', name))


def creating_frames(row: dict) -> list:
    return row['calledFrom'] if 'calledFrom' in row else row['frames']


def innermost_file(rows: list) -> str:
    counts = collections.Counter()
    for row in rows:
        frames = creating_frames(row)
        counts[frames[0].rsplit(':', 1)[0] if frames else NO_FRAME] += 1
    return counts.most_common(1)[0][0]


# Dispositions, first match wins. A rule sees the class family, its label and the set of innermost creating files.
OWNER_PID_SWEEP, TEST_KIT_ROOT, RESIDUAL = 'owner-pid name and sweep', 'test-kit temp root', 'stated residual'
RULES = [
    ('R1-fixture-sweep-landed', OWNER_PID_SWEEP,
     lambda family, label, files: family == 'mkdtemp' and label.startswith('syzygy-poc-surface-fixture-') and '<pid>' in label,
     'PR 509 (merged as 7de5dc40): the name carries the creating pid and namespace, and a sweep at the start of the next run removes the dead owners\' directories.'),
    ('R2-chrome-singleton', RESIDUAL,
     lambda family, label, files: family == 'chrome-singleton',
     'Chrome makes this directory itself; its name carries no owner. PR 515 removes it when the launching process survives to run its cleanup; a SIGKILLed runner runs none. It can be removed only through the profile\'s SingletonSocket link (follow-up F1).'),
    ('R3-browser-profile', OWNER_PID_SWEEP,
     lambda family, label, files: family == 'mkdtemp' and label == 'syzygy-poc-browser-',
     'Proposed, not covered by PR 509 or 515: name the profile with the owner pid and extend the sweep to it, reading SingletonSocket and refusing while a process still carries the --user-data-dir marker (follow-up F1). Until then a residual.'),
    ('R4-vitest-project-directory', RESIDUAL,
     lambda family, label, files: family == 'vitest-project-directory',
     'Created by vitest itself in its main process (TestProject.tmpDir = join(tmpdir(), nanoid())), before any test runs, so a test-kit root cannot contain it. A run wrapper that sets TMPDIR to an owner-pid root would (follow-up F3).'),
    ('R5-npm-compile-cache', RESIDUAL,
     lambda family, label, files: family == 'npm-compile-cache',
     'Created by npx/npm (module.enableCompileCache), one directory reused by every run, not one per run. Not growing; outside this repository.'),
    ('R6-non-test-module', TEST_KIT_ROOT,
     lambda family, label, files: family in ('mkdtemp', 'derived', 'fixed') and files and not any(TEST_FILE.search(f) for f in files)
     and all(f.startswith('apps/') or f.startswith('packages/') or f.startswith('scripts/') for f in files),
     'Created by a non-test module under apps/ or packages/: operator code that a test runs (dossier-trigger.ts, self-corpus.ts) or test support (test-model-fixture.ts, cdp-browser.ts when no sweep applies). It calls os.tmpdir() at the point of use, which reads TMPDIR then, so a test-kit root installed as TMPDIR in the worker reaches it; the same code run by an operator keeps its directories in the operator\'s TMPDIR by design.'),
    ('R7-stale-lock-by-design', RESIDUAL,
     lambda family, label, files: family == 'unattributed' and label.startswith('syzygy-poc-restart-'),
     'A lock file named for the uid and the port, made with O_EXCL by restart.ts (no trace line: the tracer does not wrap open). The code states its intent: "A stale lock requires operator inspection; the script never guesses that it is safe to remove one." A pid-based sweep would contradict that sentence, so no sweep is proposed; the stale lock matters only to a later run on the same port.'),
    ('R8-creator-unknown', RESIDUAL,
     lambda family, label, files: family == 'unattributed' or files == {NO_FRAME},
     'Unknown: no trace line carries the name and no shape rule names it, or the creating call has no frame under the repository root (third-party or Node internals). Not attributed to any file here.'),
    ('R9-test-file', TEST_KIT_ROOT,
     lambda family, label, files: family in ('mkdtemp', 'derived', 'fixed') and files and all(TEST_FILE.search(f) for f in files),
     'Created by a test file. The kit\'s tempDir() (syzygy-bpyt.4.4) makes one owner-pid root per process and every test directory lives under it, so one sweep covers all of them.'),
]


def disposition(family: str, label: str, files: set) -> dict:
    for rule_id, kind, predicate, why in RULES:
        if predicate(family, label, files):
            return {'rule': rule_id, 'disposition': kind}
    raise SystemExit(f'no disposition rule for {family} {label!r} (files {sorted(files)})')


# ---------------------------------------------------------------------------------------------------------------------------------
FIXTURE_ROWS = [
    {'kind': 'mkdtemp', 'path': '/t/dossier-records-AAAAAA', 'prefix': 'dossier-records-', 'frames': ['packages/polaris-dossier/src/start-gates.test.ts:10']},
    {'kind': 'mkdir', 'path': '/t/dossier-records-AAAAAA', 'frames': ['packages/polaris-dossier/src/start-gates.test.ts:11']},
    {'kind': 'mkdtemp', 'path': '/t/syzygy-poc-surface-fixture-p123-n4567-BBBBBB', 'prefix': 'syzygy-poc-surface-fixture-p123-n4567-', 'frames': ['apps/three-surface-poc/src/test-model-fixture.ts:45']},
    {'kind': 'mkdtemp', 'path': '/t/syzygy-poc-surface-fixture-EEEEEE', 'prefix': 'syzygy-poc-surface-fixture-', 'frames': ['apps/three-surface-poc/src/test-model-fixture.ts:45']},
    {'kind': 'mkdtemp', 'path': '/t/syzygy-dossier-src-CCCCCC', 'prefix': 'syzygy-dossier-src-', 'frames': [], 'calledFrom': ['apps/three-surface-poc/src/polaris-generation/dossier-trigger.ts:145']},
    {'kind': 'mkdtemp', 'path': '/t/syzygy-poc-browser-DDDDDD', 'prefix': 'syzygy-poc-browser-', 'frames': ['apps/three-surface-poc/src/cdp-browser.ts:445']},
    {'kind': 'writeFile', 'path': '/t/dossier-records-AAAAAA-outside-RAW.md', 'frames': ['packages/polaris-dossier/src/waiting-sessions.test.ts:279']},
    {'kind': 'mkdir', 'path': '/t/fixed-dir', 'frames': ['packages/cap1-daemon/src/server.test.ts:5']},
    {'kind': 'mkdtemp', 'path': '/t/thirdparty-FFFFFF', 'prefix': 'thirdparty-', 'frames': []},
]
FIXTURE_NAMES = ['dossier-records-AAAAAA', 'syzygy-poc-surface-fixture-p123-n4567-BBBBBB', 'syzygy-poc-surface-fixture-EEEEEE', 'syzygy-dossier-src-CCCCCC', 'syzygy-poc-browser-DDDDDD',
                 'dossier-records-AAAAAA-outside-RAW.md', 'fixed-dir', 'thirdparty-FFFFFF', '.com.google.Chrome.b7S2hn', 'com.google.Chrome.CCtKIQ', 'org.chromium.Chromium.x1y2z3',
                 '.com.google.Chrome.b7S2hn.bak', 'syzygy-poc-restart-1000-39331.lock', '5dlMwwEPs6llimFC5iPYz', '5dlMwwEPs6llimFC5iPY', 'node-compile-cache', 'mystery']
EXPECTED = {
    'dossier-records-AAAAAA': ['mkdtemp', 'dossier-records-', 'R9-test-file', TEST_KIT_ROOT],
    'syzygy-poc-surface-fixture-p123-n4567-BBBBBB': ['mkdtemp', 'syzygy-poc-surface-fixture-p<pid>-n<ns>-', 'R1-fixture-sweep-landed', OWNER_PID_SWEEP],
    'syzygy-poc-surface-fixture-EEEEEE': ['mkdtemp', 'syzygy-poc-surface-fixture-', 'R6-non-test-module', TEST_KIT_ROOT],
    'syzygy-dossier-src-CCCCCC': ['mkdtemp', 'syzygy-dossier-src-', 'R6-non-test-module', TEST_KIT_ROOT],
    'syzygy-poc-browser-DDDDDD': ['mkdtemp', 'syzygy-poc-browser-', 'R3-browser-profile', OWNER_PID_SWEEP],
    'dossier-records-AAAAAA-outside-RAW.md': ['derived', 'dossier-records-<random>-outside-RAW.md', 'R9-test-file', TEST_KIT_ROOT],
    'fixed-dir': ['fixed', 'fixed-dir', 'R9-test-file', TEST_KIT_ROOT],
    'thirdparty-FFFFFF': ['mkdtemp', 'thirdparty-', 'R8-creator-unknown', RESIDUAL],
    '.com.google.Chrome.b7S2hn': ['chrome-singleton', 'chrome-singleton-directory', 'R2-chrome-singleton', RESIDUAL],
    'com.google.Chrome.CCtKIQ': ['chrome-singleton', 'chrome-singleton-directory', 'R2-chrome-singleton', RESIDUAL],
    'org.chromium.Chromium.x1y2z3': ['chrome-singleton', 'chrome-singleton-directory', 'R2-chrome-singleton', RESIDUAL],
    '.com.google.Chrome.b7S2hn.bak': ['unattributed', '.com.google.Chrome.b7S2hn.bak', 'R8-creator-unknown', RESIDUAL],
    'syzygy-poc-restart-1000-39331.lock': ['unattributed', 'syzygy-poc-restart-<n>-<n>.lock', 'R7-stale-lock-by-design', RESIDUAL],
    '5dlMwwEPs6llimFC5iPYz': ['vitest-project-directory', 'nanoid-21', 'R4-vitest-project-directory', RESIDUAL],
    '5dlMwwEPs6llimFC5iPY': ['unattributed', '5dlMwwEPs6llimFC5iPY', 'R8-creator-unknown', RESIDUAL],
    'node-compile-cache': ['npm-compile-cache', 'node-compile-cache', 'R5-npm-compile-cache', RESIDUAL],
    'mystery': ['unattributed', 'mystery', 'R8-creator-unknown', RESIDUAL],
}


def creating_files(name: str, index: Index) -> set:
    """The innermost creating file of the first trace row of a name; empty when the trace never saw it."""
    rows = index.seen.get(name)
    return {innermost_file(rows[:1])} if rows else set()


def classify_fixture() -> dict:
    index = Index(FIXTURE_ROWS)
    result = {}
    for name in FIXTURE_NAMES:
        family, label = classify(name, index)
        verdict = disposition(family, label, creating_files(name, index))
        result[name] = [family, label, verdict['rule'], verdict['disposition']]
    return result


def selftest(out: pathlib.Path) -> None:
    here = pathlib.Path(__file__).resolve()
    source = here.read_text()
    mutants = {
        'owner-pid-digits-not-normalised': ("OWNER_PID = re.compile(r'-p\\d+-n\\d+-')", "OWNER_PID = re.compile(r'-q\\d+-n\\d+-')"),
        'derived-names-not-recognised': ("if name.startswith(made) and name != made:", "if False:"),
        'chrome-dotted-form-only': ("CHROME = re.compile(r'^\\.?(?:", "CHROME = re.compile(r'^\\.(?:"),
        'chromium-form-dropped': ("(?:com\\.google\\.Chrome|org\\.chromium\\.Chromium)\\.[A-Za-z0-9]+$')\nNANOID", "(?:com\\.google\\.Chrome)\\.[A-Za-z0-9]+$')\nNANOID"),
        'chrome-suffix-unanchored': ("\\.[A-Za-z0-9]+$')\nNANOID", "\\.[A-Za-z0-9]*')\nNANOID"),
        'nanoid-length-one-more': ("NANOID = re.compile(r'^[A-Za-z0-9_-]{21}$')", "NANOID = re.compile(r'^[A-Za-z0-9_-]{22}$')"),
        'nanoid-length-any-near': ("NANOID = re.compile(r'^[A-Za-z0-9_-]{21}$')", "NANOID = re.compile(r'^[A-Za-z0-9_-]{20,22}$')"),
        'fixture-rule-matches-every-surface-prefix': ("and '<pid>' in label,", ","),
        'operator-rule-matches-test-files': ("not any(TEST_FILE.search(f) for f in files)\n     and all(", "all("),
        'operator-code-given-the-wrong-disposition': ("('R6-non-test-module', TEST_KIT_ROOT,", "('R6-non-test-module', RESIDUAL,"),
        'stale-lock-rule-dropped': ("lambda family, label, files: family == 'unattributed' and label.startswith('syzygy-poc-restart-'),", "lambda family, label, files: False,"),
        'unknown-creator-rule-dropped': ("lambda family, label, files: family == 'unattributed' or files == {NO_FRAME},", "lambda family, label, files: False,"),
        'no-frame-not-treated-as-unknown': ("or files == {NO_FRAME},", ","),
        'creating-frame-ignores-calledFrom': ("return row['calledFrom'] if 'calledFrom' in row else row['frames']", "return row['frames']"),
        'unattributed-name-given-a-class': ("return ('unattributed', NUMERIC.sub('<n>', name))", "return ('npm-compile-cache', 'node-compile-cache')"),
        'numeric-segments-not-normalised': ("NUMERIC = re.compile(r'(?<![A-Za-z0-9])\\d+(?![A-Za-z0-9])')", "NUMERIC = re.compile(r'(?<![A-Za-z0-9])\\d+(?![A-Za-z0-9])x')"),
        'digits-inside-words-normalised': ("NUMERIC = re.compile(r'(?<![A-Za-z0-9])\\d+(?![A-Za-z0-9])')", "NUMERIC = re.compile(r'\\d+')"),
    }
    record = {'tool': 'assemble_census.py --selftest', 'sha256': hashlib.sha256(source.encode()).hexdigest(), 'expected': EXPECTED}
    got = classify_fixture()
    record['unmutated'] = {'got': got, 'meets': got == EXPECTED}
    record['mutants'] = {}
    with tempfile.TemporaryDirectory(prefix='as-') as scratch:
        for name, (old, new) in mutants.items():
            code = source[:source.index('def selftest(')]  # the mutants' own text below it names the same fragments
            assert code.count(old) == 1, (name, code.count(old))
            path = pathlib.Path(scratch) / f'mutant_{name.replace("-", "_")}.py'
            path.write_text(source.replace(old, new, 1))
            ran = subprocess.run([sys.executable, '-I', str(path), '--classify-fixture'], capture_output=True, text=True, timeout=60)
            try:
                answer = json.loads(ran.stdout)
            except json.JSONDecodeError:
                answer = None
            record['mutants'][name] = {'old': old, 'new': new, 'killed': answer != EXPECTED, 'exit': ran.returncode,
                                       'diverges': 'the mutant stopped with an error' if answer is None else sorted(k for k in EXPECTED if answer.get(k) != EXPECTED[k])}
    record['holds'] = record['unmutated']['meets'] and all(m['killed'] for m in record['mutants'].values())
    out.write_text(json.dumps(record, indent=1) + '\n')
    print(json.dumps({'unmutated': record['unmutated']['meets'], 'killed': {n: m['killed'] for n, m in record['mutants'].items()}, 'holds': record['holds']}))
    sys.exit(0 if record['holds'] else 1)


if len(sys.argv) >= 2 and sys.argv[1] == '--classify-fixture':
    print(json.dumps(classify_fixture()))
    sys.exit(0)
if len(sys.argv) >= 2 and sys.argv[1] == '--selftest':
    selftest(pathlib.Path(sys.argv[2]).resolve())

WT, COMMIT, STATIC, RUNS, PROBE, OUT = (pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]), pathlib.Path(sys.argv[4]),
                                        pathlib.Path(sys.argv[5]), pathlib.Path(sys.argv[6]).resolve())
assert re.fullmatch(r'[0-9a-f]{40}', COMMIT), 'give the full 40-hex commit'
git = lambda *a: subprocess.run(['git', *a], cwd=WT, capture_output=True, text=True, check=True).stdout


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


static = json.loads(STATIC.read_text())
assert static['treeCommit'] == COMMIT, 'the static census names another commit'
labels = sorted(p.name[:-5] for p in RUNS.glob('*.json') if not p.name.endswith('.samples.json') and p.name != 'operator-notes.json')
records, traces, samples = {}, {}, {}
for label in labels:
    records[label] = json.loads((RUNS / f'{label}.json').read_text())
    assert records[label]['treeCommit'] == COMMIT, (label, 'the run names another commit')
    raw_trace = gzip.decompress((RUNS / f'{label}.trace.jsonl.gz').read_bytes())
    lines = raw_trace.decode().splitlines()
    assert hashlib.sha256(raw_trace).hexdigest() == records[label]['trace']['sha256'] and len(lines) == records[label]['trace']['lines'], (label, 'the trace is not the one the record names')
    traces[label] = [json.loads(line) for line in lines]
    samples[label] = json.loads((RUNS / f'{label}.samples.json').read_text())
notes = json.loads((RUNS / 'operator-notes.json').read_text()) if (RUNS / 'operator-notes.json').exists() else {}
indexes = {label: Index(rows) for label, rows in traces.items()}
by_private = {r['privateDirectory']: label for label, r in records.items()}


def seeded_from(label: str):
    seeded = records[label].get('seededFrom')
    return by_private[seeded['privateDirectory']] if seeded else None


def children_of(name: str):
    for r in records.values():
        for base in (pathlib.Path(r['tmpdir']) / name,):
            if base.is_dir():
                return sorted(os.listdir(base))
    return None


# Classes ------------------------------------------------------------------------------------------------------------------------
classes: dict = {}


def entry_for(family: str, label: str) -> dict:
    return classes.setdefault((family, label), {'family': family, 'label': label, 'created': {}, 'filesCreating': collections.Counter(), 'testFiles': collections.Counter(),
                                                'leftAtEnd': {}, 'leftFromSeed': {}, 'observedSpellings': set(), 'observedChildren': None})


for label, index in indexes.items():
    per_name = {}
    for name, rows in index.seen.items():
        family, cls = classify(name, index)
        per_name.setdefault((family, cls), {})[name] = rows
    for (family, cls), names in per_name.items():
        item = entry_for(family, cls)
        item['created'][label] = len(names)
        for rows in names.values():
            item['filesCreating'][innermost_file(rows[:1])] += 1
            for row in rows[:1]:
                for frame in creating_frames(row):
                    path = frame.rsplit(':', 1)[0]
                    if TEST_FILE.search(path):
                        item['testFiles'][path] += 1
                        break

for label, r in records.items():
    mine, earlier = indexes[label], (indexes[seeded_from(label)] if seeded_from(label) else None)
    seed_names = set(r['seededFrom']['entriesMovedIn']) if r.get('seededFrom') else set()
    for entry in r['listingAtEnd']:
        name = entry['name']
        family, cls = classify(name, mine)
        if family in ('unattributed', 'chrome-singleton', 'vitest-project-directory', 'npm-compile-cache') and earlier is not None and name in seed_names:
            family, cls = classify(name, earlier)
        elif name in seed_names and earlier is not None and name not in mine.seen:
            family, cls = classify(name, earlier)
        item = entry_for(family, cls)
        slot = item['leftFromSeed' if name in seed_names else 'leftAtEnd'].setdefault(label, {'entries': 0, 'bytes': 0, 'oldestMtime': None, 'newestMtime': None})
        slot['entries'] += 1
        slot['bytes'] += entry['bytes']
        slot['oldestMtime'] = entry['mtime'] if slot['oldestMtime'] is None else min(slot['oldestMtime'], entry['mtime'])
        slot['newestMtime'] = entry['mtime'] if slot['newestMtime'] is None else max(slot['newestMtime'], entry['mtime'])
        if family in ('chrome-singleton', 'vitest-project-directory'):
            item['observedSpellings'].add(re.sub(r'[A-Za-z0-9]{6}$', '<random>', name) if family == 'chrome-singleton' else '<21 characters>')
            if family == 'vitest-project-directory' and item['observedChildren'] is None:
                item['observedChildren'] = children_of(name)

# Names the sampler saw that no trace line and no final listing carries ---------------------------------------------------------
untraced_seen = {}
for label, s in samples.items():
    final = {e['name'] for e in records[label]['listingAtEnd']}
    for name, seen in s['entries'].items():
        if name in indexes[label].seen:
            continue
        seed = records[label].get('seededFrom', {}).get('entriesMovedIn', [])
        if name in seed:
            continue
        family, cls = classify(name, indexes[label])
        untraced_seen.setdefault(label, {}).setdefault(f'{family}: {cls}', {'names': 0, 'stillThereAtEnd': 0})
        untraced_seen[label][f'{family}: {cls}']['names'] += 1
        untraced_seen[label][f'{family}: {cls}']['stillThereAtEnd'] += name in final

sampler_vs_listing = {label: {'inListingNotInSampler': sorted({e['name'] for e in records[label]['listingAtEnd']} - set(samples[label]['entries'])),
                              'inSamplerFinalNotInListing': sorted(set(samples[label]['present']) - {e['name'] for e in records[label]['listingAtEnd']})}
                      for label in labels}

# Static join ---------------------------------------------------------------------------------------------------------------------
static_files = set(static['files'])


@functools.lru_cache(maxsize=None)
def files_naming(stem: str) -> tuple:
    if not stem:
        return ()
    ran = subprocess.run(['git', 'grep', '-F', '-l', '-z', '-e', f"'{stem}", '-e', f'"{stem}', '-e', f'`{stem}', COMMIT, '--', 'apps', 'packages', 'scripts', '.syzygy'], cwd=WT, capture_output=True, text=True)
    return tuple(sorted({f.split(':', 1)[1] for f in ran.stdout.split('\0') if f and f.split(':', 1)[1].endswith(SUFFIXES)}))


def grep_any(*literals: str) -> list:
    arguments = [part for literal in literals for part in ('-e', literal)]
    ran = subprocess.run(['git', 'grep', '-F', '-l', '-z', *arguments, COMMIT, '--', 'apps', 'packages', 'scripts', '.syzygy'], cwd=WT, capture_output=True, text=True)
    return sorted({f.split(':', 1)[1] for f in ran.stdout.split('\0') if f and f.split(':', 1)[1].endswith(SUFFIXES)})


CHROME_LITERALS = ('--user-data-dir', '--remote-debugging')
chrome_launchers = grep_any(*CHROME_LITERALS)
frames_seen, innermost_seen = set(), set()
for rows in traces.values():
    for row in rows:
        frames = creating_frames(row)
        for frame in frames:
            frames_seen.add(frame.rsplit(':', 1)[0])
        if frames:
            innermost_seen.add(frames[0].rsplit(':', 1)[0])

kill_labels = [l for l in labels if records[l]['mode'] == 'kill']
fresh_labels = [l for l in labels if seeded_from(l)]
clean_labels = [l for l in labels if records[l]['mode'] == 'clean' and not seeded_from(l)]

exposure_label = clean_labels[0]
exposure_duration, exposure_interval = records[exposure_label]['seconds'], samples[exposure_label]['intervalSeconds']
exposure_raw: dict = {}
for name in set(samples[exposure_label]['entries']) | set(indexes[exposure_label].seen):
    key = classify(name, indexes[exposure_label])
    slot = exposure_raw.setdefault(key, {'sampled': 0, 'neverSampled': 0, 'lower': 0.0, 'upper': 0.0})
    seen = samples[exposure_label]['entries'].get(name)
    if seen:
        slot['sampled'] += 1
        slot['lower'] += seen['last'] - seen['first']
        slot['upper'] += seen['last'] - seen['first'] + exposure_interval
    else:
        slot['neverSampled'] += 1
        slot['upper'] += exposure_interval


def exposure_of(family: str, cls: str):
    slot = exposure_raw.get((family, cls))
    if not slot:
        return None
    return {'run': exposure_label, 'namesSampled': slot['sampled'], 'namesNeverSampled': slot['neverSampled'],
            'expectedNamesPresentAtARandomMoment': {'lowerBound': round(slot['lower'] / exposure_duration, 3), 'upperBound': round(slot['upper'] / exposure_duration, 3)}}


table = []
for (family, cls), item in sorted(classes.items(), key=lambda kv: (kv[0][0], kv[0][1])):
    files = set(item['filesCreating'])
    verdict = disposition(family, cls, files if family in ('mkdtemp', 'derived', 'fixed') else set())
    stem = cls.split('<')[0] if family in ('mkdtemp', 'derived') else None
    if stem and '<pid>' in cls and stem.endswith('-p'):
        stem = stem[:-1]  # the owner-pid part is added by a helper; the literal is what precedes it
    if family == 'unattributed':
        found = STEM.match(cls)
        stem = found.group(0) if found and len(found.group(0)) >= 8 else None
    killed_left = {l: item['leftAtEnd'][l] for l in kill_labels if l in item['leftAtEnd']}
    row = {'class': cls, 'family': family, 'created': item['created'], 'creatingFiles': dict(item['filesCreating'].most_common()), 'testFiles': dict(item['testFiles'].most_common()),
           'leftAfterSIGKILL': killed_left, 'afterTheNextFreshRun': {fl: {'killRun': seeded_from(fl), 'leftBySIGKILL': item['leftAtEnd'].get(seeded_from(fl), {}).get('entries', 0),
                                         'stillThere': item['leftFromSeed'].get(fl, {}).get('entries', 0), 'bytesStillThere': item['leftFromSeed'].get(fl, {}).get('bytes', 0)}
                                     for fl in fresh_labels if item['leftAtEnd'].get(seeded_from(fl))},
           'leftByTheFreshRunItself': {l: item['leftAtEnd'][l] for l in fresh_labels if l in item['leftAtEnd']},
           'leftAfterCleanRun': {l: item['leftAtEnd'][l] for l in clean_labels if l in item['leftAtEnd']},
           'staticFilesNamingTheLiteral': list(files_naming(stem)) if stem else None, 'staticStem': stem, 'creatingFilesAmongTheStaticMatches': (bool(set(item['filesCreating']) & set(files_naming(stem))) if stem and item['filesCreating'] else None),
           'staticStemIsInferred': family == 'unattributed' if stem else None, 'exposureInTheCleanRun': exposure_of(family, cls), 'rule': verdict['rule'], 'disposition': verdict['disposition']}
    if family == 'chrome-singleton':
        row['launchedByFilesNaming'] = {'literals': list(CHROME_LITERALS), 'files': chrome_launchers}
    if item['observedSpellings']:
        row['observedSpellings'] = sorted(item['observedSpellings'])
    if item['observedChildren'] is not None:
        row['topLevelChildrenOfOneObserved'] = item['observedChildren']
    table.append(row)

per_file: dict = {}
slot_of = lambda f: per_file.setdefault(f, {'classes': set(), 'pathsCreatedInTheCleanRun': 0, 'leftAfterSIGKILL': {}})
for name, rows in indexes[exposure_label].seen.items():
    slot = slot_of(innermost_file(rows[:1]))
    slot['classes'].add(classify(name, indexes[exposure_label])[1])
    slot['pathsCreatedInTheCleanRun'] += 1
for label in kill_labels:
    for entry in records[label]['listingAtEnd']:
        rows = indexes[label].seen.get(entry['name'])
        slot = slot_of(innermost_file(rows[:1]) if rows else '(no trace line)')
        slot['classes'].add(classify(entry['name'], indexes[label])[1])
        slot['leftAfterSIGKILL'][label] = slot['leftAfterSIGKILL'].get(label, 0) + 1
per_file = {f: {**v, 'classes': sorted(v['classes'])} for f, v in sorted(per_file.items(), key=lambda kv: (-kv[1]['pathsCreatedInTheCleanRun'], kv[0]))}

sweep_effect = {}
for fl in fresh_labels:
    seeded = records[fl]['seededFrom']['entriesMovedIn']
    kill_index = indexes[seeded_from(fl)]
    still = {e['name'] for e in records[fl]['listingAtEnd']} & set(seeded)
    by_class = lambda names: dict(sorted(collections.Counter(classify(n, kill_index)[1] for n in names).items()))
    sweep_effect[fl] = {'killRun': seeded_from(fl), 'seededEntries': len(seeded), 'removedByTheFreshRun': len(seeded) - len(still), 'removedClasses': by_class(set(seeded) - still),
                        'stillThere': len(still), 'stillThereByClass': by_class(still)}

BEAD_OBSERVATION = ('syzygy-poc-surface-fixture-p<pid>-n<ns>-', 'syzygy-public-screen-', 'syzygy-trigger-repo-', 'syzygy-build-output-', 'syzygy-dossier-src-',
                    'syzygy-poc-surface-state-', 'syzygy-trigger-', 'syzygy-poc-browser-', 'chrome-singleton-directory')
named = {}
for wanted in BEAD_OBSERVATION:
    found = [r for r in table if r['class'] == wanted]
    named[wanted] = ({'createdInTheCleanRun': found[0]['created'].get(exposure_label, 0), 'creatingFiles': list(found[0]['creatingFiles']), 'leftInAnyOfTheKills': sorted(found[0]['leftAfterSIGKILL']) or 'none of the three',
                      'rule': found[0]['rule'], 'exposureInTheCleanRun': found[0]['exposureInTheCleanRun']} if found else {'present': False})

left_after_kill = [r for r in table if r['leftAfterSIGKILL']]
never_left = [r for r in table if not r['leftAfterSIGKILL']]
dispositions_by_rule = collections.Counter(r['rule'] for r in table)

# Probe: what the launcher alone leaves ----------------------------------------------------------------------------------------
assert PROBE.is_absolute() and len(str(PROBE)) <= 30 and str(PROBE.resolve()) not in ('/', str(pathlib.Path.home().resolve()), str(pathlib.Path(tempfile.gettempdir()).resolve())), 'give a short private probe path'
assert not PROBE.exists() or (PROBE.is_dir() and not any(PROBE.iterdir())), 'the probe directory is not empty'
(PROBE / 'tmp').mkdir(parents=True)
ran = subprocess.run(['npx', 'vitest', '--version'], cwd=WT, env={**os.environ, 'TMPDIR': str(PROBE / 'tmp')}, capture_output=True, text=True, timeout=300)
probe = {'command': 'npx vitest --version', 'exit': ran.returncode, 'stdout': ran.stdout.strip(), 'leftInTheTempDirectory': sorted(os.listdir(PROBE / 'tmp'))}
chrome = {}
for candidate in ('/opt/google/chrome/chrome', '/usr/bin/google-chrome'):
    if os.path.exists(candidate):
        chrome[candidate] = subprocess.run([candidate, '--version'], capture_output=True, text=True, timeout=60).stdout.strip()
probe['chromeVersions'] = chrome
vitest_dist = sorted((WT / 'node_modules' / 'vitest' / 'dist' / 'chunks').glob('cli-api.*.js'))
literal = 'tmpDir = join(tmpdir(), nanoid());'
probe['vitestSourceLiteral'] = {'literal': literal, 'files': [{'path': str(p.relative_to(WT)), 'occurrences': p.read_text().count(literal), 'sha256': sha256(p)} for p in vitest_dist],
                               'version': json.loads((WT / 'node_modules' / 'vitest' / 'package.json').read_text())['version']}

# Static coverage -------------------------------------------------------------------------------------------------------------
uncovered = sorted(static_files - innermost_seen)
coverage = {'filesWithAStaticSite': len(static_files), 'sitesInThem': static['sites'], 'byTree': static['byTree'],
            'filesWithASiteThatWasTheInnermostCreatingFrameInSomeRun': len(static_files & innermost_seen),
            'filesWithASiteThatAppearedInSomeFrame': len(static_files & frames_seen),
            'filesWithASiteNeverSeen': len(uncovered),
            'neverSeenByTree': dict(sorted(collections.Counter(f.split('/')[0] for f in uncovered).items())),
            'neverSeen': {f: sorted({s['literal'] for s in static['files'][f] if s['literal']}) + (['(a prefix passed as a variable)'] if any(s['literal'] is None for s in static['files'][f]) else []) for f in uncovered}}

record = {
    'subject': {'what': 'every entry a full vitest run creates directly in its temp directory, and which of them a SIGKILLed run, and one fresh run after it, leave behind',
                'treeCommit': COMMIT, 'command': 'npx vitest run (the root configuration: every project, maxWorkers 50%)',
                'notRun': 'test:system (packages/cap1-system) and the Python and shell scripts under scripts/, which the root run does not start; they appear only in the static census below',
                'toolSha256': {name: sha256(pathlib.Path(__file__).resolve().parent / name) for name in ('assemble_census.py', 'census_run.py', 'collect_runs.py', 'scratch_trace.cjs', 'static_sites.py', 'tmp_sampler.py')},
                'staticSitesSha256': sha256(STATIC)},
    'runs': {label: {'mode': r['mode'], 'seededFrom': seeded_from(label), 'entriesMovedIn': len(r['seededFrom']['entriesMovedIn']) if r.get('seededFrom') else 0, 'killAfterSeconds': r.get('killAfterSeconds'),
                     'secondsIntoTheRun': r.get('secondsIntoTheRun'), 'seconds': r.get('seconds'), 'exit': r['exit'], 'loadAverageAtStart': r['loadAverageAtStart'],
                     'groupMembersAtSignal': r.get('groupMembersAtSignal'), 'entriesAtSignal': r.get('entriesAtSignal'), 'afterSignal': r.get('afterSignal'),
                     'traceLines': r['trace']['lines'], 'traceSha256': r['trace']['sha256'], 'pathsCreatedDirectlyInTemp': len({row['path'] for row in traces[label]}),
                     'processesCreating': len({row['pid'] for row in traces[label]}), 'entriesAtEnd': len(r['listingAtEnd']), 'bytesAtEnd': sum(e['bytes'] for e in r['listingAtEnd']),
                     'processesCarryingTheMarker': r['processesCarryingTheMarker'], 'stoppedByPid': r['stoppedByPid'], 'operatorNotes': notes.get(label, [])}
             for label, r in records.items()},
    'classCounts': {'classes': len(table), 'leftBySomeSIGKILL': len(left_after_kill), 'neverLeftInTheseKills': len(never_left), 'byRule': dict(sorted(dispositions_by_rule.items())),
                    'byFamily': dict(sorted(collections.Counter(r['family'] for r in table).items()))},
    'whatEachFreshRunRemovedOfTheKilledRunsLeftovers': sweep_effect,
    'namedInTheBeadObservation': named,
    'perCreatingFile': per_file,
    'leftBySIGKILL': left_after_kill,
    'neverLeftInTheseKills': [{k: r[k] for k in ('class', 'family', 'created', 'creatingFiles', 'rule', 'disposition')} for r in never_left],
    'dispositionRules': [{'rule': rid, 'disposition': kind, 'why': why} for rid, kind, _, why in RULES],
    'namesTheSamplerSawThatNoTraceLineCarries': untraced_seen,
    'samplerAgainstFinalListing': sampler_vs_listing,
    'staticGrepScope': 'git grep -F -l for the quoted stem (\' " or `) in blobs of the commit under apps, packages, scripts and .syzygy, files ending ' + ' '.join(SUFFIXES) + '; docs/ is left out because its evidence tools quote prefixes without creating them',
    'launcherProbe': probe,
    'staticCoverage': coverage,
    'exposureRanking': {'run': exposure_label, 'meaning': 'expected number of directories of the class present at a uniformly random moment of the clean run (sampler interval %s s); the upper bound counts every name once for a whole sampler interval more than it was seen' % exposure_interval,
                        'top': [{'class': r['class'], 'upperBound': r['exposureInTheCleanRun']['expectedNamesPresentAtARandomMoment']['upperBound'], 'lowerBound': r['exposureInTheCleanRun']['expectedNamesPresentAtARandomMoment']['lowerBound']}
                                for r in sorted((r for r in table if r['exposureInTheCleanRun']), key=lambda r: -r['exposureInTheCleanRun']['expectedNamesPresentAtARandomMoment']['upperBound'])[:15]]},
    'limits': [
        'The tracer wraps mkdtemp, mkdir, writeFile and symlink only (sync, callback and promise forms). A name made by open/openSync, copyFile, rename, link, cp, a stream, or by a process that is not Node has no trace line: it is classed by shape, or by the static stem and labelled inferred.',
        'The sampler lists the temp directory every %s s. A directory that lives less than that can be missed; the exposure bounds say so.' % exposure_interval,
        'Three SIGKILL points (about 25, 50 and 75 percent of a clean run of about 150 s) catch the directories alive at that moment. A class absent from every kill is not thereby safe; its disposition rests on its creating file, not on a leftover.',
        'The root vitest run only. test:system (packages/cap1-system) and the Python and shell scripts are in the static census, not in any run.',
        'Runs shared the host with other work (load average at each start is recorded); one fresh run exited 1 on two 5000 ms test timeouts.',
        'The fresh run after each kill starts in that kill\'s leftovers renamed into a new private temp directory; the process ids of the dead owners are not reused within the minutes between the runs [Inferred].',
    ],
}
OUT.write_text(json.dumps(record, indent=1, default=sorted) + '\n')
print(json.dumps({'classes': record['classCounts'], 'runs': {l: {k: v[k] for k in ('entriesAtEnd', 'pathsCreatedDirectlyInTemp')} for l, v in record['runs'].items()},
                  'coverage': {k: v for k, v in coverage.items() if k not in ('neverSeen', 'byTree')}}, indent=1))
