#!/usr/bin/env python3
"""Move the scratch outputs of the tools in this directory into dated records.

Usage: assemble_records.py <scratch-out> <evidence-dir> <repo-tree> <base> <main> <code> <first-record-commit> <full-run-tmpdir>

Copies the scratch outputs of the tools in this directory (and of compare_test_lists.py) to their
dated names, and writes two records:
  diagnosis-2026-10-22.json     the record of the first revision of this branch (read from
                                <first-record-commit>), with the records of the per-file hook it
                                dropped taken out and the final code commit's scan added
  verification-2026-10-22.json  the figures of the acceptance criteria, read from the copied records
                                and the gate logs in <scratch-out>, never typed
<full-run-tmpdir> is the private TMPDIR of the full-suite run; its listing is read here, so the
directory must still exist. <base> is main before this change, <main> the origin/main merged into
the branch, <code> the commit of test-model-fixture.ts and its test.
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
base, main, code, first, full_tmp = sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], pathlib.Path(sys.argv[8])
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
rev = lambda ref: git('rev-parse', ref)
load = lambda name: json.loads((evidence / name).read_text())
lines_of = lambda name, *starts: [line.strip() for line in (scratch / name).read_text().splitlines() if line.strip().startswith(starts)]
earlier = lambda path: json.loads(git('show', f'{first}:docs/evidence/poc-fixture-leak-2026-10-22/{path}'))

for source, target in (('b-drain-scan-head.json', 'drain-scan'), ('b-leak-by-file-head.json', 'leak-by-file-head'), ('b-clean-run-head.json', 'clean-run-head'),
                       ('b-kill-then-fresh-run-head.json', 'kill-then-fresh-run-head'), ('b-term-then-fresh-run-head.json', 'term-then-fresh-run-head'),
                       ('b-kill-then-fresh-run-sweep-disabled.json', 'kill-then-fresh-run-sweep-disabled'), ('b-interrupt-term-head.json', 'interrupt-term-head'),
                       ('interrupt-term-base.json', 'interrupt-term-base'), ('mutants-sweep-3f08143c.json', 'mutants-sweep'),
                       ('cli-probe-head.json', 'cli-sweep-probe-head'), ('cli-probe-mutant.json', 'cli-sweep-probe-mutant')):
    shutil.copyfile(scratch / source, evidence / f'{target}-{DATE}.json')
lists = json.loads((scratch / 'test-lists-3f08143c.json').read_text())
(evidence / f'test-lists-{DATE}.json').write_text(json.dumps({
    'tool': 'compare_test_lists.py (docs/evidence/poc-hygiene-2026-10-22)', 'baseTree': f'{rev(code)} with test-model-fixture.test.ts as at {rev(main)} and fixture-directories.test.ts absent', 'headTree': rev(code),
    'command': 'npx vitest list', 'note': 'the base list is the code commit with those two test files put back to origin/main (one reverted, one set aside) and restored afterwards: they are the only test files under apps/ and packages/ that differ',
    **lists}, indent=1) + '\n')

scan, by_file_head, by_file_base = load(f'drain-scan-{DATE}.json'), load(f'leak-by-file-head-{DATE}.json'), load(f'leak-by-file-base-{DATE}.json')
first_scan = earlier(f'drain-scan-{DATE}.json')
new_callers = sorted({r['file'] for r in scan['rows']} - {r['file'] for r in first_scan['rows']})
summary_keys = ('treeCommit', 'testFilesInDirectory', 'fixtureUsingTestFiles', 'filesWithCopiesLeft', 'filesWithTemplatesLeft', 'copiesLeftTotal', 'templatesLeftTotal', 'nonzeroExits')

diagnosis = earlier(f'diagnosis-{DATE}.json')
diagnosis['subject'] = {
    'baseCommit': rev(base),
    'note': 'the diagnosis is of main after PR 503, before the change. Revised 2026-10-22 after the coordinator dropped the per-file removal hook this branch first carried: its records (unit mutants, non-draining probe, head interrupt probe) are removed from this directory and are in git history at ' + rev(first),
}
diagnosis['interruptedRuns'].pop('head', None)
diagnosis['interruptedRuns']['method'] = 'interrupt_probe.py: the project run as the leader of a new process group, SIGKILL (`base`) or SIGTERM (`baseSigterm`) sent to that group once three fixture copies exist, then the TMPDIR sampled for 80 seconds'
term_base = load(f'interrupt-term-base-{DATE}.json')
diagnosis['interruptedRuns']['baseSigterm'] = {k: term_base[k] for k in ('treeCommit', 'signal', 'atSignal')} | {'lastSample': term_base['series'][-1], 'record': f'interrupt-term-base-{DATE}.json'}
diagnosis['interruptedRuns']['note'] = ('the copies and templates are still there 80 seconds after the signal: no hook runs in a killed worker, so nothing a test file registers can remove them. '
                                        'The orphaned processes in the samples are Chrome crashpad handlers and `cat` pipes of killed browser launches; each probe run\'s own were stopped afterwards by PID, each re-checked against the probe\'s unique TMPDIR in its environment.')
diagnosis['callersThatDrainNothing']['atTheFinalCodeCommit'] = {
    'treeCommit': scan['treeCommit'],
    'filesNamingTheHelper': scan['filesNamingTheHelper'],
    'callers': scan['callers'],
    'scanFlaggedNoDrain': scan['noDrainFound'],
    'scanDelegatedArrays': scan['filesWithADelegatedArray'],
    'callersNotInTheScanAtTheFirstRevision': {name: {row['file']: row for row in scan['rows']}[name]['arrayDrains'] for name in new_callers},
    'perFileRun': {k: by_file_head[k] for k in summary_keys},
    'note': 'main moved from 0d4d5098 to ' + rev(main) + ' with PR 507, whose main.test.ts now calls buildFixtureModel and drains in afterAll. The six files the scan flagged are the six read by hand above; the scan flags the same six. fixture-directories.test.ts is in the population of files naming the helper only because a comment in it names test-model-fixture.test.ts; it creates no repository (createsRepositories is false), which is why the files naming the helper rise from 44 at the base to 46 and the callers from 42 to 43 (main.test.ts alone); the per-file run counts it among its 44 files and it leaves 0.',
}
diagnosis['finding'] = (
    'The leak in /tmp is not a caller that fails to drain: a clean project run leaves 0 fixture directories, all fixture-using test files leave 0 when run alone, and no caller was found that drains nothing. '
    'The directories come from runs that were killed or aborted (mtime bursts of 25 to 49 copies, and SIGKILL and SIGTERM probes that leave them in place at base): no teardown hook runs there. [Inferred for the bursts, Observed for the probes]')
(evidence / f'diagnosis-{DATE}.json').write_text(json.dumps(diagnosis, indent=1) + '\n')


def listing(directory: pathlib.Path) -> dict:
    """What a run left in its private TMPDIR, by kind. Random suffixes are masked."""
    names = sorted(p.name for p in directory.iterdir())
    mask = lambda n: re.sub(r'(?<=-)[A-Za-z0-9_]{6}(?=-|$)', 'XXXXXX', n)
    kinds: dict[str, int] = {}
    for name in names:
        kinds[mask(name)] = kinds.get(mask(name), 0) + 1
    return {'entries': len(names), 'fixtureDirectories': sum(1 for n in names if n.startswith('syzygy-poc-surface-fixture-')), 'byKind': dict(sorted(kinds.items()))}


assert subprocess.run(['git', 'merge-base', '--is-ancestor', code, 'HEAD'], cwd=tree).returncode == 0, 'the tree must contain the code commit'
gate_tail = lambda name: [line for line in (scratch / name).read_text().splitlines() if line.strip()][-1]
clean, killed, termed, disabled, mutants = (load(f'{name}-{DATE}.json') for name in ('clean-run-head', 'kill-then-fresh-run-head', 'term-then-fresh-run-head', 'kill-then-fresh-run-sweep-disabled', 'mutants-sweep'))
cli_head, cli_mutant, interrupt_term_head = load(f'cli-sweep-probe-head-{DATE}.json'), load(f'cli-sweep-probe-mutant-{DATE}.json'), load(f'interrupt-term-head-{DATE}.json')
for record in (clean, killed, termed, disabled, mutants, cli_head, cli_mutant, interrupt_term_head, scan, by_file_head):
    assert rev(record['treeCommit']) == rev(code), (record['tool'], record['treeCommit'])
run_keys = ('exit', 'seconds', 'numTotalTests', 'numPassedTests', 'numFailedTests', 'numPendingTests', 'testFiles', 'testFilesFailed', 'failing')
test_names = [line.split(' > ', 1)[0].rsplit(' ', 1)[-1] + ' > ' + line.split(' > ', 1)[1] for line in (scratch / 'list-head-3f08143c.txt').read_text().splitlines()
              if '(syzygy-bpyt.4.10)' in line and 'apps/three-surface-poc/src/' in line]
first_verification = earlier(f'verification-{DATE}.json')


def log_facts(name: str) -> dict:
    text = (scratch / name).read_text()
    return {'log': name, 'summary': lines_of(name, 'Test Files', 'Tests ', 'Duration'),
            'failed': [line.strip()[len('FAIL  '):] for line in text.splitlines() if line.strip().startswith('FAIL')],
            'errorLines': sorted({line for line in text.splitlines() if line.startswith(('Error:', 'AssertionError:'))})}


def failing(record: dict) -> list:
    return [(f['file'], f['test'][-80:], f['firstErrorLine']) for f in record['freshRun']['failing']]


app_lines = [line for line in (scratch / 'vitest-full-3f08143c.log').read_text().splitlines() if '|@syzygy/three-surface-poc-app|' in line]
full_run = {'command': 'npx vitest run (TMPDIR=<emptied private directory>)', **log_facts('vitest-full-3f08143c.log'), 'left': listing(full_tmp),
            'appProject': {'filesPassed': sum(1 for l in app_lines if l.startswith(' ✓')), 'filesSkipped': sum(1 for l in app_lines if l.startswith(' ↓')), 'filesFailed': sum(1 for l in app_lines if l.startswith((' ❯', ' ×')))}}
def rerun_facts(name: str, command: str) -> dict:
    report = json.loads((scratch / name).read_text())
    return {'command': command, 'passed': report['numPassedTests'], 'failed': report['numFailedTests'], 'files': {f['name'].split('/src/')[-1]: f['status'] for f in report['testResults']},
            'failureErrorLines': sorted({(a['failureMessages'][0].splitlines() or [''])[0] for f in report['testResults'] for a in f['assertionResults'] if a['status'] == 'failed' and a['failureMessages']})}


files_failed = ' '.join(sorted({re.search(r'packages/\S+?\.test\.ts', line).group(0) for line in (scratch / 'vitest-full-3f08143c.log').read_text().splitlines() if line.strip().startswith('FAIL') and re.search(r'packages/\S+?\.test\.ts', line)}))
def act_families_outcomes() -> dict:
    runs = {}
    for log in sorted((scratch / 'act-families').glob('*.log')):
        text = log.read_text()
        runs[log.stem] = 'passed (65 tests)' if 'Tests  65 passed' in text else ('hook timed out (10 s), 65 skipped' if 'Hook timed out in 10000ms' in text else 'UNCLASSIFIED')
    tree = lambda marker: {name: outcome for name, outcome in runs.items() if marker in name}
    return {'runs': runs, 'alternating': {'mainA0406967': [runs[f'alternating-{n}-main-a0406967'] for n in (1, 2, 3)], 'branch3f08143c': [runs[f'alternating-{n}-branch-3f08143c'] for n in (1, 2, 3)]}}


full_run['rerunAlone'] = {
    'files': files_failed,
    'defaultTimeouts': rerun_facts('rerun-failed-default-timeouts.json', 'npx vitest run <the failed files together> (default timeouts)'),
    'timeoutsLifted': rerun_facts('rerun-failed.json', 'npx vitest run <the failed files together> --testTimeout=120000 --hookTimeout=120000'),
    'actFamilies': act_families_outcomes() | {
        'file': 'packages/polaris-generation-consent/src/act-families.test.ts',
        'why': 'its beforeAll renders each act record by spawning python3 (recorder-fixtures.testkit.ts, spawnSync) several times in a hook with a 10 s limit; one python3 import of the recorder took 1.9 s and 2.7 s wall in this session [Observed: time], so the hook passes or times out with the host load. It passes or fails alike on main a0406967 (alternating runs) and on this branch [Observed: runs]; the change adds a global setup to the app project only, which this file\'s project does not load [Inferred: from the config pin test and the diff].',
    },
}
verification = {
    'subject': {'baseCommit': rev(base), 'mergedMainCommit': rev(main), 'codeCommit': rev(code), 'treeAtRecording': rev('HEAD')},
    'appsAndPackagesDiffSinceCodeCommit': git('diff', '--stat', code, 'HEAD', '--', 'apps', 'packages'),
    'toolDigests': {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(evidence.glob('*.py')) if path.name != 'assemble_records.py'},
    'changedFilesMainToCode': git('diff', '--name-only', main, code).split(),
    'ac1Sigterm': {
        'claim': 'a run killed with SIGTERM leaks its fixture directories too, as one killed with SIGKILL does',
        'atBase': {'record': f'interrupt-term-base-{DATE}.json', 'treeCommit': term_base['treeCommit'], 'atSignal': term_base['atSignal'], 'eightySecondsAfter': term_base['series'][-1]},
        'atHead': {'record': f'interrupt-term-head-{DATE}.json', 'treeCommit': interrupt_term_head['treeCommit'], 'atSignal': interrupt_term_head['atSignal'], 'eightySecondsAfter': interrupt_term_head['series'][-1]},
        'note': 'the run is stopped at once and no hook runs, so the directories stay until the next run sweeps them (ac3, termedRun)',
    },
    'ac2': {
        'claim': 'a clean three-surface-poc project run with a fresh TMPDIR leaves 0 syzygy-poc-surface-fixture-* directories',
        'command': 'npx vitest run --project @syzygy/three-surface-poc-app',
        'cleanRunTool': {'record': f'clean-run-head-{DATE}.json', **{k: clean['freshRun'][k] for k in run_keys}, 'fixtureDirectoriesLeft': clean['freshRun']['left']['fixtureDirectories'], 'left': clean['freshRun']['left']},
        'inTheFullSuiteRun': {'where': 'the app project inside gates.fullVitest', **full_run['appProject'], 'fixtureDirectoriesLeft': full_run['left']['fixtureDirectories']},
        'perFile': {k: by_file_head[k] for k in summary_keys},
        'note': 'base leaves 0 too in a clean run (diagnosis), so this criterion shows the change leaves nothing new; AC3 is what the change is for. Failures in the runs of this record are listed under run, not hidden; the host\'s load average was 45 to 95 from other lanes throughout [Observed: uptime between runs].',
    },
    'ac3': {
        'claim': 'a run killed with SIGKILL or SIGTERM, followed by one fresh run, leaves 0 directories of dead processes; with the sweep disabled they stay',
        'killedRun': {'record': f'kill-then-fresh-run-head-{DATE}.json', 'killedRun': killed['killedRun'], 'freshRun': {k: killed['freshRun'][k] for k in run_keys} | {'left': killed['freshRun']['left']},
                      'failingInTheFreshRun': failing(killed), 'note': 'the criterion is the count of directories of dead processes in freshRun.left. The fresh run also exits non-zero on the tests in failingInTheFreshRun, vitest\'s timeout placeholder under load; none is a test of the fixture directories or of the sweep.'},
        'termedRun': {'record': f'term-then-fresh-run-head-{DATE}.json', 'killedRun': termed['killedRun'], 'freshRun': {k: termed['freshRun'][k] for k in run_keys} | {'left': termed['freshRun']['left']}, 'failingInTheFreshRun': failing(termed)},
        'sweepDisabled': {'record': f'kill-then-fresh-run-sweep-disabled-{DATE}.json', 'mutant': disabled['mutant'], 'killedRun': disabled['killedRun'], 'freshRun': {k: disabled['freshRun'][k] for k in run_keys} | {'left': disabled['freshRun']['left']},
                          'failingInTheFreshRun': failing(disabled), 'note': 'the directories of the killed run stay; the fresh run exits non-zero because the unit test that pins the global setup\'s registration fails on the mutated tree, as intended'},
        'unitMutants': {k: mutants[k] for k in ('treeCommit', 'command', 'mutants', 'killed')} | {'control': mutants['control'], 'ids': [(r['id'], r['outcome']) for r in mutants['results']]},
        'accessibilityCli': {
            'claim': 'the accessibility CLI, which Vitest\'s global setup never reaches, sweeps the dead-process directories of its temp directory once, as the first statement of main (review round 1, F2)',
            'head': {'record': f'cli-sweep-probe-head-{DATE}.json', 'exit': cli_head['run']['exit'], 'deadProcessDirectoriesLeft': cli_head['deadProcessDirectoriesLeft'], 'liveAndLegacyKept': cli_head['liveAndLegacyKept'], 'holds': cli_head['holds']},
            'mutant': {'record': f'cli-sweep-probe-mutant-{DATE}.json', 'id': cli_mutant['mutant']['id'], 'exit': cli_mutant['run']['exit'], 'deadProcessDirectoriesLeft': cli_mutant['deadProcessDirectoriesLeft'], 'holds': cli_mutant['holds']},
        },
    },
    'oncePerRun': {
        'claim': 'the sweep runs once per run, from a global setup of the app project, and not once per test file',
        'unitTests': [name for name in test_names if 'global setup' in name or 'does not sweep when a file makes its template' in name],
        'mutantsThatMustDie': {r['id']: r['outcome'] for r in mutants['results'] if r['id'] in ('global-setup-does-not-sweep', 'global-setup-not-registered', 'global-setup-on-every-project', 'sweep-per-file')},
    },
    'ac4ac5': {
        'claim': 'a directory whose pid is alive survives the sweep (the current process\'s pid, in a unit test); a legacy name with no pid survives; so does a dead pid of another PID namespace; a file and a symlink survive',
        'unitTestsAdded': test_names,
        'withNoPidSegmentKept': 'thirteen name shapes in one test: legacy copy and template, pid without the namespace segment (both forms), pid with no hyphen after it, namespace with no hyphen after it, empty namespace, an m segment, pid not straight after the prefix, another prefix, the prefix inside a longer name, the prefix without its last hyphen',
        'foreignNamespace': 'one test: a copy and a template with a dead pid and another namespace are kept, the own-namespace one beside them is removed',
        'noSymlinkFollowed': 'one test: a symlink to a directory outside the swept one, and a file, both with dead-pid names, are kept; the outside directory is untouched',
        'otherUser': 'one test, with a spy on process.getuid returning another uid; no second uid was available to this lane, so a real foreign-owned directory was not made',
    },
    'ac6': {k: load(f'test-lists-{DATE}.json')[k] for k in ('baseTree', 'headTree', 'baseLines', 'headLines', 'added', 'removed', 'addedByFile', 'testsLine')},
    'gates': {
        'fullVitest': full_run,
        'typecheck': {'command': 'npm run typecheck', 'last line of the log': gate_tail('gate-typecheck.log')},
        'checkGovernance': {'command': 'python3 scripts/check_governance.py', 'summary': [l for l in (scratch / 'gate-governance.log').read_text().splitlines() if l.endswith('derived, not asserted')], 'exit': gate_tail('gate-governance.log')},
        'checkQuotations': {'command': 'python3 scripts/check_quotations.py', 'exit': gate_tail('gate-quotations.log')},
    },
    'otherLeakSeen': {
        'where': 'packages/polaris-dossier/src/waiting-sessions.test.ts:276',
        'what': 'writes <tmpdir>/dossier-signoff-XXXXXX-outside-RAW.md beside its temporary directory and never removes it; found in the full-run TMPDIR listing. Filed by the coordinator as syzygy-bpyt.4.12',
        'left': full_run['left']['byKind'],
    },
    'oneOffCleanup': first_verification['oneOffCleanup'] | {'carriedFrom': f'verification-{DATE}.json at {rev(first)}; the directories no longer exist, so the counts cannot be re-derived'},
}
tidy_two = json.loads((scratch / 'tidy-2.json').read_text())
removed_two = (scratch / 'tmp-cleanup-2-removed-list.txt').read_text().split()
verification['oneOffCleanup']['secondPass'] = {
    'rule': verification['oneOffCleanup']['rule'], 'before': tidy_two['before'], 'removed': len(removed_two), 'after': tidy_two['after'], 'remainingOlderThan360Minutes': tidy_two['olderThan360MinutesAfter'],
    'removedNames': sorted(pathlib.PurePath(p).name for p in removed_two),
    'note': 'before and after typed from `find ... | wc -l` at the time; removed is the scripted find output saved before removal. The total was 193 at the end of the first pass and 193 again about seven hours later: no directory was added in between.',
}
(evidence / f'verification-{DATE}.json').write_text(json.dumps(verification, indent=1) + '\n')
print(json.dumps({'tests': verification['ac6']['testsLine'], 'cleanLeft': clean['freshRun']['left']['fixtureDirectories'], 'fullRunLeft': full_run['left']['fixtureDirectories'], 'appProject': full_run['appProject'],
                  'killedDead': killed['killedRun']['fiveSecondsAfterSignal']['ofDeadProcesses']['count'], 'killedFreshLeft': killed['freshRun']['left']['fixtureDirectories'],
                  'termedDead': termed['killedRun']['fiveSecondsAfterSignal']['ofDeadProcesses']['count'], 'termedFreshLeft': termed['freshRun']['left']['fixtureDirectories'],
                  'disabledLeft': disabled['freshRun']['left']['ofDeadProcesses']['count'], 'mutants': verification['ac3']['unitMutants']['killed'],
                  'cliHead': cli_head['holds'], 'cliMutant': cli_mutant['holds'], 'newCallers': new_callers, 'unitTestNames': len(test_names)}, indent=1))
