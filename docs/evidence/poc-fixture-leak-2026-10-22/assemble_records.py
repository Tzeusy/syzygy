#!/usr/bin/env python3
"""Move the scratch outputs of the tools in this directory into dated records.

Usage: assemble_records.py <scratch-out> <evidence-dir> <repo-tree> <base> <main> <code> <first-record-commit> <full-run-tmpdir>

Copies the scratch outputs of drain_scan.py, leak_by_file.py and compare_test_lists.py to their
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

shutil.copyfile(scratch / 'drain-scan-new.json', evidence / f'drain-scan-{DATE}.json')
shutil.copyfile(scratch / 'leak-by-file-head-new.json', evidence / f'leak-by-file-head-{DATE}.json')
lists = json.loads((scratch / 'test-lists.json').read_text())
(evidence / f'test-lists-{DATE}.json').write_text(json.dumps({
    'tool': 'compare_test_lists.py (docs/evidence/poc-hygiene-2026-10-22)', 'baseTree': f'{rev(code)} with test-model-fixture.test.ts as at {rev(main)}', 'headTree': rev(code),
    'command': 'npx vitest list', 'note': 'the base list is the code commit with test-model-fixture.test.ts at origin/main: that is the only test file under apps/ and packages/ that differs',
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
    'note': 'main moved from 0d4d5098 to ' + rev(main) + ' with PR 507, whose main.test.ts now calls buildFixtureModel and drains in afterAll. The six files the scan flagged are the six read by hand above; the scan flags the same six.',
}
diagnosis['finding'] = (
    'The leak in /tmp is not a caller that fails to drain: a clean project run leaves 0 fixture directories, all fixture-using test files leave 0 when run alone, and no caller was found that drains nothing. '
    'The directories come from runs that were killed or aborted (mtime bursts of 25 to 49 copies, and a SIGKILL probe that leaves them in place at base): no teardown hook runs there. [Inferred for the bursts, Observed for the probe]')
(evidence / f'diagnosis-{DATE}.json').write_text(json.dumps(diagnosis, indent=1) + '\n')


def listing(directory: pathlib.Path) -> dict:
    """What a run left in its private TMPDIR, by kind. Random suffixes are masked."""
    names = sorted(p.name for p in directory.iterdir())
    mask = lambda n: re.sub(r'(?<=-)[A-Za-z0-9_]{6}(?=-|$)', 'XXXXXX', n)
    kinds: dict[str, int] = {}
    for name in names:
        kinds[mask(name)] = kinds.get(mask(name), 0) + 1
    return {'entries': len(names), 'fixtureDirectories': sum(1 for n in names if n.startswith('syzygy-poc-surface-fixture-')), 'byKind': dict(sorted(kinds.items()))}


gate_tail = lambda name: [line for line in (scratch / name).read_text().splitlines() if line.strip()][-1]
clean, killed, disabled, mutants = load(f'clean-run-head-{DATE}.json'), load(f'kill-then-fresh-run-head-{DATE}.json'), load(f'kill-then-fresh-run-sweep-disabled-{DATE}.json'), load(f'mutants-sweep-{DATE}.json')
run_keys = ('exit', 'seconds', 'numTotalTests', 'numPassedTests', 'numFailedTests', 'numPendingTests', 'testFiles', 'testFilesFailed', 'failing')
test_names = [line.split(' > ', 1)[1] for line in (scratch / 'list-head.txt').read_text().splitlines() if 'a killed run left behind (syzygy-bpyt.4.10)' in line]
first_verification = earlier(f'verification-{DATE}.json')
full_run = {'summary': lines_of('vitest-full-head.log', 'Test Files', 'Tests ', 'Duration'), 'left': listing(full_tmp)}
verification = {
    'subject': {'baseCommit': rev(base), 'mergedMainCommit': rev(main), 'codeCommit': rev(code), 'treeAtRecording': rev('HEAD')},
    'appsAndPackagesDiffSinceCodeCommit': git('diff', '--stat', code, 'HEAD', '--', 'apps', 'packages'),
    'toolDigests': {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(evidence.glob('*.py')) if path.name != 'assemble_records.py'},
    'changedFilesMainToCode': git('diff', '--name-only', main, code).split(),
    'ac2': {
        'claim': 'a clean three-surface-poc project run with a fresh TMPDIR leaves 0 syzygy-poc-surface-fixture-* directories',
        'command': 'npx vitest run --project @syzygy/three-surface-poc-app',
        'run': {k: clean['freshRun'][k] for k in run_keys} | {'left': clean['freshRun']['left']},
        'perFile': {k: by_file_head[k] for k in summary_keys},
        'note': 'base leaves 0 too in a clean run (diagnosis), so this criterion shows the change leaves nothing new; AC3 is what the change is for. A first attempt of this run at the same commit, under machine load 30, failed sync-child-process-guard.test.ts: the new test used spawnSync, which that guard forbids; the test now awaits an async spawn. Its report was not retained.',
    },
    'ac3': {
        'claim': 'a run killed with SIGKILL, followed by one fresh run, leaves 0 directories of dead processes; with the sweep disabled they stay',
        'withTheSweep': {'killedRun': killed['killedRun'], 'freshRun': {k: killed['freshRun'][k] for k in run_keys} | {'left': killed['freshRun']['left']}},
        'sweepDisabled': {'mutant': disabled['mutant'], 'killedRun': disabled['killedRun'], 'freshRun': {k: disabled['freshRun'][k] for k in run_keys} | {'left': disabled['freshRun']['left']},
                          'note': 'the fresh run exits 1 because the unit test that exercises the sweep fails on the mutated tree; the 5 directories of the killed run stay'},
        'unitMutants': {k: mutants[k] for k in ('treeCommit', 'command', 'mutants', 'killed')} | {'control': mutants['control'], 'ids': [(r['id'], r['outcome']) for r in mutants['results']]},
    },
    'ac4ac5': {
        'claim': 'a directory whose pid is alive survives the sweep (the current process\'s pid, in a unit test); a legacy name with no pid survives',
        'unitTestsAddedToTestModelFixtureTestTs': test_names,
        'withNoPidSegmentKept': 'seven name shapes in one test: legacy copy, legacy template, pid with no hyphen, pid not straight after the prefix (copy and template forms), another prefix, the prefix inside a longer name, the prefix without its last hyphen',
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
        'what': 'writes <tmpdir>/dossier-signoff-XXXXXX-outside-RAW.md beside its temporary directory and never removes it; found in the full-run TMPDIR listing',
        'left': full_run['left']['byKind'],
    },
    'oneOffCleanup': first_verification['oneOffCleanup'] | {'carriedFrom': f'verification-{DATE}.json at {rev(first)}; the directories no longer exist, so the counts cannot be re-derived'},
}
(evidence / f'verification-{DATE}.json').write_text(json.dumps(verification, indent=1) + '\n')
print(json.dumps({'tests': verification['ac6']['testsLine'], 'ac2Left': clean['freshRun']['left']['fixtureDirectories'], 'ac3KilledDead': killed['killedRun']['fiveSecondsAfterKill']['ofDeadProcesses']['count'],
                  'ac3FreshLeft': killed['freshRun']['left']['fixtureDirectories'], 'ac3DisabledLeft': disabled['freshRun']['left']['ofDeadProcesses']['count'], 'mutants': verification['ac3']['unitMutants']['killed'],
                  'newCallers': new_callers, 'fullRunLeft': full_run['left']['fixtureDirectories'], 'unitTestNames': len(test_names)}, indent=1))
