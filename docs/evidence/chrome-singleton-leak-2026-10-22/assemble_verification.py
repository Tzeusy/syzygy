#!/usr/bin/env python3
"""Move the scratch outputs of the tools in this directory to dated records and write the verification record.

Usage: assemble_verification.py <scratch-out> <evidence-dir> <repo-tree> <base> <code> <first-approach>

<scratch-out> holds the outputs of launch_probe.py, tmpdir_length_probe.py, launch_failure_probe.py, mutate_cdp.py,
browser_files_run.py and compare_test_lists.py, and the gate logs (typecheck, governance, quotations, authority).
<base> is main before this change, <code> the last commit that changes a file under apps/ or vitest.config.ts,
<first-approach> the commit of the approach dropped for the TMPDIR constraint it added. Every figure in
verification-2026-10-22.json is read from the copied records or computed from git here, never typed.
"""
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys

DATE = '2026-10-22'
scratch, evidence, tree = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
base, code, first = sys.argv[4], sys.argv[5], sys.argv[6]
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
rev = lambda ref: git('rev-parse', ref).strip()
load = lambda name: json.loads((evidence / f'{name}-{DATE}.json').read_text())

COPIES = (('launch-probe-head', 'launch-probe-head'), ('launch-probe-base', 'launch-probe-base'), ('tmpdir-length-head', 'tmpdir-length-head'), ('tmpdir-length-base', 'tmpdir-length-base'),
          ('tmpdir-length-rejected', 'tmpdir-length-rejected'), ('launch-failure-head', 'launch-failure-head'), ('launch-failure-base', 'launch-failure-base'),
          ('mutants-cdp', 'mutants-cdp'), ('browser-files-head', 'browser-files-head'), ('browser-files-base', 'browser-files-base'),
          ('test-lists', 'test-lists'), ('test-lists-attempt-1', 'test-lists-attempt-1'))
for source, target in COPIES:
    shutil.copyfile(scratch / f'{source}.json', evidence / f'{target}-{DATE}.json')

tools = sorted(p.name for p in evidence.iterdir() if p.suffix in ('.py', '.mjs'))
digests = {name: hashlib.sha256((evidence / name).read_bytes()).hexdigest() for name in tools}

probe_h, probe_b = load('launch-probe-head')['summary'], load('launch-probe-base')['summary']
fail_h, fail_b = load('launch-failure-head'), load('launch-failure-base')
mut = load('mutants-cdp')
files_h, files_b = load('browser-files-head'), load('browser-files-base')
lists = load('test-lists')
length = {m: load(f'tmpdir-length-{m}') for m in ('head', 'base', 'rejected')}

# Assertions unchanged: every line the change removes from an existing test file, and how many name an assertion
# (an import line that names `expect` is an import, not an assertion, and is counted apart).
ASSERTION = re.compile(r'\bexpect\b|\bassert\b|\.to[A-Z]\w*\(|\.resolves\b|\.rejects\b')
changed_tests = [f for f in git('diff', '--name-only', base, code).splitlines() if f.endswith('.test.ts')]
removed = {}
for f in changed_tests:
    lines = [l[1:] for l in git('diff', '-U0', base, code, '--', f).splitlines() if l.startswith('-') and not l.startswith('---')]
    removed[f] = {'removedLines': len(lines), 'removedImportLines': sum(1 for l in lines if l.lstrip().startswith('import')),
                  'removedLinesNamingAnAssertion': sum(1 for l in lines if not l.lstrip().startswith('import') and ASSERTION.search(l)), 'removed': lines}

gates = {}
for key, name, ok in (('typecheck', 'gate-typecheck.log', lambda t: 'exit 0' in t.splitlines()[-1]), ('checkGovernance', 'gate-governance.log', lambda t: ' 0 FAIL' in t),
                      ('checkQuotations', 'gate-quotations.log', None), ('authoritySweep', 'gate-authority.log', lambda t: 'Tests  5 passed (5)' in t)):
    path = scratch / name
    if path.exists():
        text = path.read_text()
        gates[key] = {'log': name, 'lastLine': next((l for l in reversed(text.splitlines()) if l.strip()), ''), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

verification = {
    'subject': {'baseCommit': rev(base), 'codeCommit': rev(code), 'firstApproachCommit': rev(first), 'headAtRecording': rev('HEAD')},
    'appsAndConfigDiffSinceCodeCommit': git('diff', '--stat', code, 'HEAD', '--', 'apps', 'vitest.config.ts', 'package.json').strip(),
    'toolDigests': digests,
    'diagnosis': {
        'claim': 'Chrome leaves .com.google.Chrome.<random> in TMPDIR only when its leader is killed (closeDisposableBrowser, after the 1 s close grace); a clean exit removes it',
        'atBase': {'record': 'launch-probe-base-2026-10-22.json', 'launches': probe_b['launches'], 'launchesWhoseCloseThrew': probe_b['launchesWhoseCloseThrew'], 'killed': probe_b['killed'],
                   'exitedCleanly': probe_b['exitedCleanly'], 'killedAndLeftAChromeDirectory': probe_b['killedAndLeftAChromeDirectory'],
                   'exitedAndLeftAChromeDirectory': probe_b['exitedAndLeftAChromeDirectory'], 'holds': probe_b['holds']},
        'linkGoneByRemoval': 'Chrome unlinks <profile>/SingletonSocket as it begins to shut down, before it removes the directory, so a link read at removal time finds nothing on a killed launch '
                             '(the first revision of this fix read it there and still left the directory on killed launches; see the commit message of the replacing commit)',
        'existingTeardownTestAtBase': next(({'file': f['file'], 'attempts': len(f['attempts']), 'chromeSingletonDirectoriesLeftOnPassingAttempt': [a['left']['chromeSingletonDirectories'] for a in f['attempts'] if a['exit'] == 0]}
                                            for f in files_b['perFile'] if f['file'].endswith('cdp-browser.browser.test.ts')), None),
    },
    'ac1': {
        'claim': 'after a passing run of every Chrome-driven vitest file with a fresh private TMPDIR, that TMPDIR holds no .com.google.Chrome.* or polaris-draft-browser-* directory',
        'listA': files_h['listA'], 'listB': files_h['listB'], 'inAButNotB': files_h['summary']['inAButNotB'], 'inBButNotA': files_h['summary']['inBButNotA'],
        'atHead': {'record': 'browser-files-head-2026-10-22.json', 'treeCommit': files_h['treeCommit'], **{k: files_h['summary'][k] for k in files_h['summary'] if k.startswith(('files', 'chrome', 'draft', 'combined', 'every'))}},
        'atBase': {'record': 'browser-files-base-2026-10-22.json', 'treeCommit': files_b['treeCommit'], **{k: files_b['summary'][k] for k in files_b['summary'] if k.startswith(('files', 'chrome', 'draft', 'combined', 'every'))}},
        'launchProbeAtHead': {'record': 'launch-probe-head-2026-10-22.json', **{k: probe_h[k] for k in (
            'launches', 'launchesThatClosed', 'launchesWhoseCloseThrew', 'closeErrors', 'killed', 'exitedCleanly', 'closedLaunchesThatLeftAnything',
            'leftByLaunchesWhoseCloseThrew', 'entriesInPrivateTmpdirAtTheEnd', 'entriesAtTheEndNotLeftByAThrownClose', 'holds')}},
        'launchFailure': {'atHead': {'record': 'launch-failure-head-2026-10-22.json', 'draftPreviewDirectoriesLeft': fail_h['draftPreviewDirectoriesLeft'], 'retainedProfilesLeft': fail_h['retainedProfilesLeft'], 'holds': fail_h['holds']},
                          'atBase': {'record': 'launch-failure-base-2026-10-22.json', 'draftPreviewDirectoriesLeft': fail_b['draftPreviewDirectoriesLeft'], 'retainedProfilesLeft': fail_b['retainedProfilesLeft'], 'holds': fail_b['holds']}},
    },
    'closeThrewUnderLoad': {
        'claim': 'closeDisposableBrowser throws, and keeps the profile (and so Chrome\'s singleton directory, which is removed only with it), when two empty scans of the process group do not come within its 3 s drain; on this loaded host it happened in runs of the real-Chrome cases',
        'attemptsOfTheBrowserFilesRunAtHead': [{'file': f['file'], 'attempt': a['attempt'], 'firstErrorLine': x['firstErrorLine'], 'chromeSingletonDirectoriesLeft': a['left']['chromeSingletonDirectories'],
                                                 'browserProfilesLeft': a['left']['browserProfiles']}
                                                for f in files_h['perFile'] for a in f['attempts'] if a['exit'] != 0 for x in a['failing'] if 'profile drain did' in x['firstErrorLine']],
        'attemptsOfTheMutantControl': [{'attempt': a['attempt'], 'status': a['status'], 'chromeSingletonDirectoriesLeft': sum(1 for n in a['left'] if n.startswith('.com.google.Chrome.')),
                                        'drainErrors': sum(1 for x in a['failing'] if 'profile drain did' in x['firstErrorLine'])} for a in mut['control']['attempts']],
        'acceptedAs': 'a load failure, not a pass and not a kill: the criterion of AC1 is over passing attempts, and the mutant runs score only failures with another first error line',
    },
    'ac2': 'out of scope: a killed test runner (SIGKILL/SIGTERM of vitest or of an operator command) leaves whatever Chrome and the helper had made; syzygy-bpyt.4.10 sweeps only syzygy-poc-surface-fixture-* directories of dead processes and this change adds no sweep. '
           'What this change covers is a Chrome the helper itself kills in a run that otherwise ends normally.',
    'ac3': {'claim': 'no existing assertion changes', 'changedTestFiles': removed},
    'tmpdirLength': {'claim': 'the longest TMPDIR that launches Chrome did not move; the first approach (Chrome\'s temp directory set to the profile) cut it',
                     **{m: {'record': f'tmpdir-length-{m}-2026-10-22.json', 'longestLaunched': length[m]['longestLaunched'], 'shortestFailed': length[m]['shortestFailed']} for m in length}},
    'mutants': {'record': 'mutants-cdp-2026-10-22.json', 'treeCommit': mut['treeCommit'], 'total': mut['mutants'], 'killed': mut['killed'],
                'outcomes': {r['id']: r['outcome'] for r in mut['results']}, 'controlHolds': mut['control']['holds'], 'controlLaunchFailureHolds': mut['controlLaunchFailure']['holds']},
    'tests': {'record': 'test-lists-2026-10-22.json', 'testsLine': lists['testsLine'], 'baseLines': lists['baseLines'], 'headLines': lists['headLines'], 'addedByFile': lists['addedByFile'], 'removedByFile': lists['removedByFile'],
              'firstListing': {'record': 'test-lists-attempt-1-2026-10-22.json', 'testsLine': load('test-lists-attempt-1')['testsLine'],
                               'why': 'the first head listing omitted three session-view tests that are gated by a bwrap probe at import time (packages/polaris-dossier/src/session-view.test.ts: `hasBwrap`, which runs bwrap and so depends on host load); a relisting matched'}},
    'gates': gates,
}
(evidence / f'verification-{DATE}.json').write_text(json.dumps(verification, indent=1) + '\n')
print(json.dumps({'tests': lists['testsLine'], 'mutants': f"{mut['killed']}/{mut['mutants']}", 'ac1Head': verification['ac1']['atHead'].get('everyFilePassedAloneAndLeftNone'),
                  'ac1Base': verification['ac1']['atBase'].get('everyFilePassedAloneAndLeftNone'), 'lengths': {m: (length[m]['longestLaunched'], length[m]['shortestFailed']) for m in length},
                  'assertionLinesRemoved': {f: (v['removedLines'], v['removedLinesNamingAnAssertion']) for f, v in removed.items()}}, indent=1))
