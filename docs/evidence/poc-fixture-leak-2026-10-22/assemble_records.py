#!/usr/bin/env python3
"""Move the scratch outputs of the tools in this directory into dated records.

Usage: assemble_records.py <scratch-out> <evidence-dir> <repo-tree> <base-commit> <code-commit> <tmp-root>

Copies each tool's JSON output to its dated name and writes two records:
  diagnosis-2026-10-22.json    what a clean run leaves, who drains, what an interrupted run leaves
  verification-2026-10-22.json the figures of the acceptance criteria, read from the copied
                               records and from the gate logs in <scratch-out>, never typed
<tmp-root> holds the private TMPDIR of each run (base, head, full); their listings are read
here, so the directories must still exist. Counts are derived.
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
base, code, tmp_root = sys.argv[4], sys.argv[5], pathlib.Path(sys.argv[6])
COPIES = {
    'leak-by-file-base.json': f'leak-by-file-base-{DATE}.json',
    'leak-by-file-head.json': f'leak-by-file-head-{DATE}.json',
    'drain-scan-head.json': f'drain-scan-{DATE}.json',
    'mutants-teardown.json': f'mutants-teardown-{DATE}.json',
    'nondraining-probe.json': f'nondraining-probe-{DATE}.json',
    'tmpdir-length-probe.json': f'tmpdir-length-probe-{DATE}.json',
    'census-after-cleanup.json': f'census-tmp-after-cleanup-{DATE}.json',
    'test-lists.json': f'test-lists-{DATE}.json',
    'interrupt-kill-3copies-base.json': f'interrupt-kill-base-{DATE}.json',
    'interrupt-kill-3copies-head.json': f'interrupt-kill-head-{DATE}.json',
}
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
load = lambda name: json.loads((evidence / name).read_text())
summary_lines = lambda name: [line.strip() for line in (scratch / name).read_text().splitlines() if line.strip().startswith(('Test Files', 'Tests ', 'Duration'))]


def listing(directory: pathlib.Path) -> dict:
    """What a run left in its private TMPDIR, by kind. Random suffixes are masked."""
    names = sorted(p.name for p in directory.iterdir())
    mask = lambda n: re.sub(r'(?<=-)[A-Za-z0-9_]{6}$', 'XXXXXX', n)
    kinds: dict[str, int] = {}
    for name in names:
        kinds[mask(name)] = kinds.get(mask(name), 0) + 1
    return {
        'entries': len(names),
        'fixtureCopies': sum(1 for n in names if n.startswith('syzygy-poc-surface-fixture-') and not n.startswith('syzygy-poc-surface-fixture-template-')),
        'fixtureTemplates': sum(1 for n in names if n.startswith('syzygy-poc-surface-fixture-template-')),
        'byKind': dict(sorted(kinds.items())),
    }


for source, target in COPIES.items():
    shutil.copyfile(scratch / source, evidence / target)
lists = json.loads((evidence / f'test-lists-{DATE}.json').read_text())
(evidence / f'test-lists-{DATE}.json').write_text(json.dumps({'tool': 'compare_test_lists.py (docs/evidence/poc-hygiene-2026-10-22)', 'baseTree': base, 'headTree': code, 'command': 'npx vitest list', 'note': 'the base list is the head tree with test-model-fixture.test.ts at the base commit: that is the only file under apps/ that differs', **lists}, indent=1) + '\n')

by_file_base, by_file_head, scan, probe = load(f'leak-by-file-base-{DATE}.json'), load(f'leak-by-file-head-{DATE}.json'), load(f'drain-scan-{DATE}.json'), load(f'nondraining-probe-{DATE}.json')
interrupt_base, interrupt_head = load(f'interrupt-kill-base-{DATE}.json'), load(f'interrupt-kill-head-{DATE}.json')
mutants, tmpdir_probe, census_after = load(f'mutants-teardown-{DATE}.json'), load(f'tmpdir-length-probe-{DATE}.json'), load(f'census-tmp-after-cleanup-{DATE}.json')

diagnosis = {
    'subject': {'baseCommit': git('rev-parse', base), 'note': 'the diagnosis is of main after PR 503, before the change'},
    'cleanRunsAtBase': {
        'command': 'npx vitest run --project @syzygy/three-surface-poc-app',
        'runs': [
            {'tmpdir': 'a path of 110 characters under the scratchpad', 'log': 'diagnosis-run-1/2', 'summary': summary_lines('diagnosis-run-1-browser-contention.log'),
             'note': 'ten browser-driven files failed with "browser exited with signal before announcing a DevTools endpoint"; see tmpdirLengthProbe. Not a clean run.'},
            {'tmpdir': '/tmp/lc410/base', 'summary': summary_lines('diagnosis-run.log'), 'left': listing(tmp_root / 'base')},
        ],
        'tmpdirLengthProbe': tmpdir_probe['results'],
    },
    'perFileAtBase': {k: by_file_base[k] for k in ('treeCommit', 'testFilesInDirectory', 'fixtureUsingTestFiles', 'filesWithCopiesLeft', 'filesWithTemplatesLeft', 'copiesLeftTotal', 'templatesLeftTotal', 'nonzeroExits')},
    'callersThatDrainNothing': {
        'population': f"{scan['filesNamingTheHelper']} tracked .ts files under apps/three-surface-poc/src name test-model-fixture or polaris-accessibility-variants; {scan['callers']} create repositories",
        'scanFlaggedNoDrain': scan['noDrainFound'],
        'scanDelegatedArrays': scan['filesWithADelegatedArray'],
        'readByHand': {
            'apps/three-surface-poc/src/polaris-accessibility-main.ts': 'drains cleanups in a finally block, line 50 (a CLI, no test hook exists outside Vitest)',
            'apps/three-surface-poc/src/polaris-opening-index.browser.test.ts': 'one array drained in a try/finally inside the test, line 290; the other drained by afterAll, line 321',
            'apps/three-surface-poc/src/polaris-accessibility-variants.ts': 'cleanups is a parameter; its three test callers and the CLI drain it (afterEach, afterAll, afterAll, finally)',
            'apps/three-surface-poc/src/polaris-copy.test.ts': 'owned is a parameter of buildVariant, called with variantCleanups, drained by afterAll lines 228-230; cleanups drained by afterEach lines 25-27',
            'apps/three-surface-poc/src/polaris-first-reading.test.ts': 'cleanupList is the sharedFixtureModels callback parameter, drained by afterAll(shared.remove) line 53; cleanups drained by afterEach lines 27-28',
            'apps/three-surface-poc/src/polaris-narrative.test.ts': 'cleanupList is the sharedFixtureModels callback parameter, drained by afterAll(shared.remove) line 60; cleanups drained by afterEach lines 18-19',
        },
        'conclusion': 'no caller was found that drains nothing: 0 of 42, by the static scan plus the by-hand reading above, and 0 of 42 test files by the per-file run (perFileAtBase)',
    },
    'interruptedRuns': {
        'method': 'interrupt_probe.py: the project run as the leader of a new process group, SIGKILL sent to that group once three fixture copies exist, then the TMPDIR sampled for 80 seconds',
        'base': {k: interrupt_base[k] for k in ('treeCommit', 'signal', 'atSignal')} | {'lastSample': interrupt_base['series'][-1]},
        'head': {k: interrupt_head[k] for k in ('treeCommit', 'signal', 'atSignal')} | {'lastSample': interrupt_head['series'][-1]},
        'note': 'the copies and templates are still there 80 seconds after the signal, with and without the change: no hook runs in a killed worker. The orphaned processes in the samples are Chrome crashpad handlers and `cat` pipes of killed browser launches; each probe run\'s own were stopped afterwards by PID, each re-checked against the probe\'s unique TMPDIR in its environment. An earlier attempt with `timeout -s` (unrecorded) listed fixture directories at once that were gone minutes later; the probe samples over time instead.',
    },
    'tmpCensus': {
        'afterCleanup': census_after,
        'beforeCleanup': {
            'asPrintedByTheCensusToolAt': '2026-10-22 06:2x +08, before the 58 oldest directories were removed (the tool was then a scratch script; census_tmp.py is its recorded successor)',
            'total': 251, 'copies': 243, 'templates': 8, 'bursts': 31,
            'burstSizeHistogram': {'1': 9, '2': 5, '3': 4, '4': 2, '5': 1, '6': 4, '25': 2, '28': 3, '49': 1},
            'note': 'typed from the tool output, not re-derivable: those directories no longer exist',
        },
        'readingOfTheCensus': '[Inferred] the six bursts of 25 to 49 copies over 3 to 7 minutes are interrupted runs, not a non-draining caller, which would leave a count tied to its file on every complete run',
    },
}
(evidence / f'diagnosis-{DATE}.json').write_text(json.dumps(diagnosis, indent=1) + '\n')

head_run = {'summary': summary_lines('head-project-run.log'), 'left': listing(tmp_root / 'head')}
full_run = {'summary': summary_lines('vitest-full.log'), 'left': listing(tmp_root / 'full')}
cleanup_list = (scratch / 'tmp-cleanup-removed-list.txt').read_text().split()
verification = {
    'subject': {'baseCommit': git('rev-parse', base), 'codeCommit': git('rev-parse', code), 'recordedAtHead': git('rev-parse', 'HEAD')},
    'appsAndPackagesDiffSinceCodeCommit': git('diff', '--stat', code, 'HEAD', '--', 'apps', 'packages'),
    'toolDigests': {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(evidence.glob('*.py')) if path.name != 'assemble_records.py'},
    'changedFilesBaseToCode': git('diff', '--name-only', base, code).split(),
    'ac2': {
        'claim': 'a full three-surface-poc project run with a fresh TMPDIR leaves 0 syzygy-poc-surface-fixture-* directories',
        'command': 'npx vitest run --project @syzygy/three-surface-poc-app',
        'head': head_run,
        'perFileHead': {k: by_file_head[k] for k in ('treeCommit', 'testFilesInDirectory', 'fixtureUsingTestFiles', 'filesWithCopiesLeft', 'filesWithTemplatesLeft', 'copiesLeftTotal', 'templatesLeftTotal', 'nonzeroExits')},
        'note': 'base leaves 0 too in a complete run (diagnosis); this criterion alone cannot tell the change from no change, which is what AC3 and the probe are for',
    },
    'ac3': {
        'claim': 'removing the new per-file registration leaks again',
        'unitMutants': {k: mutants[k] for k in ('treeCommit', 'command', 'mutants', 'killed')} | {'control': mutants['control'], 'ids': [(r['id'], r['outcome']) for r in mutants['results']]},
        'nonDrainingCallerProbe': {name: {k: v for k, v in result.items() if k != 'summary'} for name, result in probe['results'].items()},
        'probeCommit': probe['treeCommit'],
    },
    'ac4': {
        'fullVitest': full_run,
        'testNames': {k: load(f'test-lists-{DATE}.json')[k] for k in ('baseTree', 'headTree', 'baseLines', 'headLines', 'added', 'removed', 'addedByFile', 'testsLine')},
    },
    'otherLeakSeen': {
        'where': 'packages/polaris-dossier/src/waiting-sessions.test.ts:276',
        'what': 'writes <tmpdir>/dossier-signoff-XXXXXX-outside-RAW.md beside its temporary directory and never removes it; found in the full-run TMPDIR listing',
        'left': full_run['left']['byKind'],
    },
    'oneOffCleanup': {
        'rule': 'only directories directly under /tmp named syzygy-poc-surface-fixture-*, owned by this user, of type directory, with `find -mmin +360` (modified more than 360 minutes before the run)',
        'before': 251, 'removed': len(cleanup_list), 'after': 193,
        'remainingOlderThan360Minutes': 0,
        'removedNames': sorted(pathlib.PurePath(p).name for p in cleanup_list),
        'note': 'the before and after counts were read from `find ... | wc -l` at the time; the removed list is the scripted `find` output saved before removal',
    },
}
(evidence / f'verification-{DATE}.json').write_text(json.dumps(verification, indent=1) + '\n')
print(json.dumps({'diagnosis': {'baseRunLeft': diagnosis['cleanRunsAtBase']['runs'][1]['left']['fixtureCopies'], 'baseInterruptedLeft': diagnosis['interruptedRuns']['base']['lastSample']['fixtureCopies'], 'headInterruptedLeft': diagnosis['interruptedRuns']['head']['lastSample']['fixtureCopies']}, 'ac3': verification['ac3']['nonDrainingCallerProbe'], 'mutants': verification['ac3']['unitMutants']['killed'], 'headRunLeft': head_run['left']['fixtureCopies'], 'cleanup': len(cleanup_list)}, indent=1))
