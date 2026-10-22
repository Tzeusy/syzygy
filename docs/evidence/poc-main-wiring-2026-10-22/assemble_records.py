#!/usr/bin/env python3
"""Move the scratch outputs of the tools in this directory into dated records.

Usage: assemble_records.py records <scratch-out> <evidence-dir> <base-commit> <code-commit>
       assemble_records.py verification <scratch-out> <evidence-dir> <repo-tree> <base-commit> <code-commit>

`records` copies each tool's JSON output to its dated name, adds the tree commits
to the test-list record (compare_test_lists.py does not name them), and keeps the
canonical differential transcripts and the head route capture, which name no
scratch path. `verification` runs after the gates, from their logs in
<scratch-out>: it writes verification-2026-10-22.json, which names the figures it
derives from the records, never copies them from a report.
"""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

DATE = '2026-10-22'
COPIES = {
    'mutants-head.json': f'mutants-main-test-head-{DATE}.json',
    'mutants-base.json': f'mutants-main-test-base-{DATE}.json',
    'differential-comparison.json': f'differential-{DATE}.json',
    'diff-fixed-head.json.canonical': f'differential-transcripts-{DATE}.json',
    'route-comparison.json': f'route-capture-comparison-{DATE}.json',
    'route-head.json': f'route-capture-head-{DATE}.json',
    'dist-compare.json': f'dist-compare-{DATE}.json',
    'mutants-comparators.json': f'mutants-comparators-{DATE}.json',
    'mutants-dist-compare.json': f'mutants-dist-compare-{DATE}.json',
    'mutants-sweep-waits.json': f'mutants-sweep-waits-{DATE}.json',
    'sweep-waits-head.json': f'sweep-waits-head-{DATE}.json',
    'sweep-waits-base.json': f'sweep-waits-base-{DATE}.json',
}


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def records(scratch: pathlib.Path, evidence: pathlib.Path, base: str, code: str) -> None:
    for source, target in COPIES.items():
        shutil.copyfile(scratch / source, evidence / target)
    lists = json.loads((scratch / 'test-lists.json').read_text())
    lists = {'tool': lists.pop('tool'), 'baseTree': base, 'headTree': code, 'command': 'npx vitest list', **lists}
    (evidence / f'test-lists-{DATE}.json').write_text(json.dumps(lists, indent=1) + '\n')
    print('records written:', len(COPIES) + 1)


def last(path: pathlib.Path, n: int = 1) -> list[str]:
    return path.read_text().rstrip('\n').splitlines()[-n:]


def verification(scratch: pathlib.Path, evidence: pathlib.Path, tree: pathlib.Path, base: str, code: str) -> None:
    load = lambda name: json.loads((evidence / name).read_text())
    git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
    head, base_mutants = load(f'mutants-main-test-head-{DATE}.json'), load(f'mutants-main-test-base-{DATE}.json')
    differential, route, dist = load(f'differential-{DATE}.json'), load(f'route-capture-comparison-{DATE}.json'), load(f'dist-compare-{DATE}.json')
    sweep_head, sweep_base, sweep_mutants = load(f'sweep-waits-head-{DATE}.json'), load(f'sweep-waits-base-{DATE}.json'), load(f'mutants-sweep-waits-{DATE}.json')
    comparators, dist_mutants, lists = load(f'mutants-comparators-{DATE}.json'), load(f'mutants-dist-compare-{DATE}.json'), load(f'test-lists-{DATE}.json')
    required = [r for r in head['results'] if r['id'] in {'bound-locator-ignored', 'reobserve-horizon-root', 'session-clock', 'verbatim-reader-root', 'materialize-target-root', 'revision-change-root', 'state-dir-unresolved', 'credential-provision-dropped', 'reevaluation-dropped'}]
    summary_lines = lambda name: [line.strip() for line in (scratch / name).read_text().splitlines() if line.strip().startswith(('Test Files', 'Tests ', 'exit='))]
    production_diff = git('diff', base, code, '--', 'apps', 'packages')
    record = {
        'subject': {
            'baseCommit': base,
            'codeCommit': code,
            'recordedAtHead': git('rev-parse', 'HEAD').strip(),
            'note': 'apps/ and packages/ at the recording head equal the code commit when appsAndPackagesDiffSinceCodeCommit is empty',
        },
        'appsAndPackagesDiffSinceCodeCommit': git('diff', '--stat', code, 'HEAD', '--', 'apps', 'packages').strip(),
        'productionChange': {
            'files': git('diff', '--name-only', base, code, '--', 'apps', 'packages').split(),
            'poc-main.ts': [line for line in production_diff.splitlines() if line[:1] in '+-' and line[:3] not in ('+++', '---')],
        },
        'toolDigests': {path.name: sha256(path) for path in sorted(evidence.glob('*.py'))},
        'ac1': {
            'claim': 'each of the nine N1 mutants is killed by main.test.ts alone',
            'mutantsKilledAtHead': f"{sum(1 for r in required if r['outcome'] == 'killed')} of {len(required)}",
            'mutantsSurvivingAtBase': f"{sum(1 for r in base_mutants['results'] if r['outcome'] == 'SURVIVED')} of {base_mutants['mutants']}",
            'headControl': head['control']['holds'], 'baseControl': base_mutants['control']['holds'],
            'headTestsRun': head['control']['testsRun'], 'baseTestsRun': base_mutants['control']['testsRun'],
            'extraMutantsKilledAtHead': f"{head['killed'] - len(required)} of {head['mutants'] - len(required)}",
            'headRanAtCommit': head['treeCommit'], 'baseRanAtCommit': base_mutants['treeCommit'],
        },
        'ac2': {
            'differential': {k: differential[k] for k in ('scenarios', 'scenariosWithEqualTranscriptsBaseVersusHead', 'rawFilesByteEqual', 'nonVacuity')},
            'routeCapture': {k: route[k] for k in ('requestKeys', 'requestKeysEqualBaseVersusHead', 'statuses', 'nonVacuity')} | {'fixtureRevision': route['fixtureRepository']['revision'], 'baseVersusBaseSecondRunDiffering': len(route['baseVersusBaseSecondRunDiffering'])},
            'emittedOutput': {k: dist[k] for k in ('shippedFilesCompared', 'shippedFilesInOnlyOneTree', 'shippedFilesDiffering', 'unexpectedDifferences', 'testFilesCompared')} | {'differing': [{'file': d['file'], 'changedLines': d['changedLines'], 'lines': d['lines']} for d in dist['differing']]},
            'comparatorChecks': {'comparators': f"{comparators['killed']} of {comparators['perturbations']} perturbations detected", 'dist': f"{dist_mutants['killed']} of {dist_mutants['perturbations']} perturbations detected"},
        },
        'ac3': {
            'head': {k: sweep_head[k] for k in ('itBlocks', 'viWaitForCalls', 'blocksWithAWait', 'blocksWithAWaitAndAnExplicitTestTimeout', 'boundedBlocks', 'waitingBlocksNotBounded')},
            'base': {k: sweep_base[k] for k in ('itBlocks', 'viWaitForCalls', 'blocksWithAWait', 'boundedBlocks')} | {'waitingBlocksNotBounded': len(sweep_base['waitingBlocksNotBounded'])},
            'sweepChecks': f"{sweep_mutants['killed']} of {sweep_mutants['mutants']} mutants detected",
        },
        'testNames': {k: lists[k] for k in ('baseTree', 'headTree', 'baseLines', 'headLines', 'baseDistinctNames', 'headDistinctNames', 'added', 'removed', 'addedByFile', 'testsLine')}
                     | {'note': 'by name; five existing tests in main.test.ts changed only their test-timeout argument, and the --watch test its waitFor option'},
        'gates': {
            'fullVitest': {'command': 'npx vitest run', 'lines': summary_lines('vitest-full.log')},
            'typecheck': {'command': 'npm run typecheck', 'lines': summary_lines('typecheck-final.log')},
            'checkGovernance': {'base': last(scratch / 'governance-base.txt')[0], 'head': last(scratch / 'governance-head.txt')[0]},
            'checkQuotations': {'baseVsHeadOutputIdentical': (scratch / 'quotations-base.txt').read_bytes() == (scratch / 'quotations-head.txt').read_bytes()},
            'authoritySweep': {'command': 'npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts', 'lines': summary_lines('authority-sweep.log')},
        },
    }
    (evidence / f'verification-{DATE}.json').write_text(json.dumps(record, indent=1) + '\n')
    print(json.dumps({k: record[k] for k in ('ac1', 'ac3', 'gates')}, indent=1)[:2500])


if __name__ == '__main__':
    stage = sys.argv[1]
    if stage == 'records':
        records(pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4], sys.argv[5])
    elif stage == 'verification':
        verification(pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), pathlib.Path(sys.argv[4]), sys.argv[5], sys.argv[6])
    else:
        sys.exit('stage must be records or verification')
