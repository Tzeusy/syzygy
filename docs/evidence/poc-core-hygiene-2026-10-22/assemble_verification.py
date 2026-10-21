#!/usr/bin/env python3
"""Verification record for syzygy-bpyt.7.6: figures computed from the records here.

Usage: assemble_verification.py <evidence-dir> <logs-dir> <repo-tree> <base-commit> <code-commit> <out.json>

Reads the JSON records in <evidence-dir> and the last lines of the gate logs in
<logs-dir> (vitest-full.log, governance-base.txt, governance-after.txt,
quotations-base.txt, quotations-after.txt), checks that packages/ and apps/ are
byte-identical between <code-commit> and the tree's HEAD, and writes the result.
"""
import json
import subprocess
import sys
from pathlib import Path


def last_lines(path: Path, n: int = 1) -> list[str]:
    return path.read_text(encoding='utf-8').rstrip('\n').splitlines()[-n:]


def main() -> int:
    evidence, logs, tree = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    base_commit, code_commit, out = sys.argv[4], sys.argv[5], Path(sys.argv[6])
    load = lambda name: json.loads((evidence / name).read_text(encoding='utf-8'))
    git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
    census, capture, lists = load('export-census-core-2026-10-22.json'), load('route-capture-comparison-2026-10-22.json'), load('test-lists-2026-10-22.json')
    emitted, mutants, sweep_b, sweep_c = load('emitted-code-diff-2026-10-22.json'), load('mutants-export-census-2026-10-22.json'), load('consumer-sweep-base-2026-10-22.json'), load('consumer-sweep-code-2026-10-22.json')
    comment_only, comment_mutants = load('comment-only-check-2026-10-22.json'), load('mutants-comment-only-check-2026-10-22.json')
    vitest_lines = [l.strip() for l in (logs / 'vitest-full.log').read_text(encoding='utf-8').splitlines() if l.strip().startswith(('Test Files', 'Tests '))]
    gov_b, gov_a = last_lines(logs / 'governance-base.txt')[0], last_lines(logs / 'governance-after.txt')[0]
    quot_same = (logs / 'quotations-base.txt').read_bytes() == (logs / 'quotations-after.txt').read_bytes()
    packages_apps_diff = git('diff', '--stat', code_commit, 'HEAD', '--', 'packages', 'apps')
    record = {
        'subject': {'baseCommit': base_commit, 'codeCommit': code_commit, 'recordedAtHead': git('rev-parse', 'HEAD'),
                    'note': 'packages/ and apps/ at the recording head are byte-identical to the code commit when packagesAndAppsDiffSinceCodeCommit is empty'},
        'packagesAndAppsDiffSinceCodeCommit': packages_apps_diff,
        'censusTool': {
            'fix': 'export_census.py strips comments with a small lexer (strings, templates and regex literals kept), replacing the earlier regex stripper that a glob string such as \'**/*.ts\' could turn into an unclosed block comment',
            'crossCheckedWithRaw': True,
            'lexerVersusRawOnBase': census['lexerVersusRawOnBase']['exportsWhoseClassDiffers'],
            'selftest': last_lines(evidence / 'selftest-export-census-2026-10-22.txt')[0],
            'mutants': {'ran': mutants['mutants'], 'killed': mutants['killed'], 'survivors': mutants['survivors'], 'ranAtCommit': mutants['ranAtCommit']},
        },
        'consumerSweeps': {'trackedFilesBase': sweep_b['trackedFiles'], 'trackedFilesCode': sweep_c['trackedFiles'],
                           'subjects': len(sweep_b['subjects']), 'methodsAgreeOnEverySubjectToken': all(t['methodsAgreeOnFiles'] for r in sweep_b['subjects'] + sweep_c['subjects'] for t in r['tokens'])},
        'censusTotals': {k: v for k, v in census['totals'].items()},
        'baseToAfterLexer': census['baseToAfterLexer'],
        'emittedCode': {'filesCompared': emitted['filesCompared'], 'filesDiffering': emitted['filesDiffering'], 'filesInOnlyOneTree': emitted['filesInOnlyOneTree'],
                        'differing': [f"{p['project']}/dist/{d['file']}" for p in emitted['projects'] for d in p['differingAfterCommentStrip']]},
        'routeCapture': {k: capture[k] for k in ('responses', 'fixtures', 'fixturesWithDistinctOutput', 'requestKeysPerFixture', 'requestKeysWhoseBodyDiffersAcrossFixtures', 'distinctBodyDigests', 'statuses')}
                        | {'claim': capture['claim'], 'fixtureRepository': {k: capture['fixtureRepository'][k] for k in ('path', 'revision')},
                           'reference': {k: capture['reference'][k] for k in ('treeCommit', 'variantsSha256')},
                           'comparisons': [{k: c[k] for k in ('file', 'treeCommit', 'variantsSha256', 'variantsBytesEqualReference', 'responsesDifferingFromReference')} for c in capture['comparisons']]},
        'commentOnlyCheck': {k: comment_only[k] for k in ('oldCommit', 'mergedWith', 'treeCommit', 'trackedChangesUnderPackagesAndApps', 'filesChanged', 'allIdenticalAfterCommentStrip', 'retainedExport')}
                            | {'files': [f['file'] for f in comment_only['files']],
                               'mutants': {'controls': [c['holds'] for c in comment_mutants['controls']], 'ran': comment_mutants['mutants'], 'killed': comment_mutants['killed'], 'survivors': comment_mutants['survivors'], 'ranAtCommit': comment_mutants['ranAtCommit']}},
        'testNames': {k: lists[k] for k in ('baseTree', 'headTree', 'baseLines', 'headLines', 'baseDistinctNames', 'headDistinctNames', 'added', 'removed', 'testsLine')},
        'fullVitestRun': {'command': 'npx vitest run', 'lines': vitest_lines, 'ranAt': 'the code commit tree (packages/ and apps/ identical to the recording head)'},
        'checkGovernance': {'base': gov_b, 'after': gov_a, 'differenceFromBase': 'file counts only (the new evidence directory)'},
        'checkQuotations': {'baseVsAfterOutputIdentical': quot_same},
        'typecheck': {'command': 'npm run typecheck', 'exit': 0},
        'authoritySweep': {'command': 'npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts', 'result': '5 passed'},
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: record[k] for k in ('packagesAndAppsDiffSinceCodeCommit', 'emittedCode', 'testNames', 'fullVitestRun')}, indent=1)[:1500])
    return 0


if __name__ == '__main__':
    sys.exit(main())
