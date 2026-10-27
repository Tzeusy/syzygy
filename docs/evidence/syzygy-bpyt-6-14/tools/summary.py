#!/usr/bin/env python3
"""syzygy-bpyt.6.14: derive summary.json from the raw records beside it, checking each against the git objects of the tree given.

The subject is HEAD (the code commit) over BASE (main at d621bfa2): the PR 530 round-2 review's N9 (the support-leaf purity test)
and N10 (the S10 alias map). Inputs (all in docs/evidence/syzygy-bpyt-6-14/):
  mutants-{head,base}-{absent,present}.json  tools/mutants.py in a clean clone at each commit, with every dist/ absent and with
                         all twelve built; the reviewer's fragments are read from the committed round-2 records;
  shared-reader-identity.json  tools/shared_reader_identity.py: the testkit's reader and list against the two copies it replaces;
  bundle-differential.json     tools/bundle_differential.py: the S10 bundle at BASE and at HEAD, byte for byte;
  titles.json, suite-head.json tools/titles.py over the three changed test files, and tools/suite_run.py over the whole suite;
  residuals-head.json          tools/residuals.py: the two forms the allowlist is known to pass (R1, R2), disclosed.
Usage: python3 -I summary.py <tree> [--check | --selftest]
  --check: exit 1 unless summary.json equals what the inputs give and no check fails.
  --selftest: mutate one input at a time in memory (rule 6) and exit 1 unless every mutation makes a check fail.
"""
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

TREE = Path(sys.argv[1]).resolve()
HERE = TREE / 'docs/evidence/syzygy-bpyt-6-14'
BASE = 'd621bfa267f24ff68f6f83ac7bfba44b81a32a34'
HEAD = 'dff82655bf288c92f119c63a98ed0147f6ee4d31'
SUBJECT = sorted(['packages/polaris-dossier/src/no-egress.test.ts', 'packages/support/src/purity.testkit.ts',
                  'packages/support/src/support-purity.test.ts', 'packages/three-surface-poc-core/src/owner-act-drafter.test.ts'])
RUNS = [('head', 'absent'), ('head', 'present'), ('base', 'absent'), ('base', 'present')]
# What the bead requires to fail at HEAD, in both dist/ states: N9's named reviewer mutants and N10's two.
REQUIRED = [f'RP{n}' for n in range(2, 17)] + ['E6', 'E7', 'E8', 'E9', 'M1', 'M2']
ROUND2 = 'docs/evidence/support-leaf-review-2026-10-27/round-2'


def git(*args):
    return subprocess.run(['git', '-C', str(TREE), *args], capture_output=True, text=True, check=True).stdout


def load():
    inputs = {f'{side}-{dist}': json.load(open(HERE / f'mutants-{side}-{dist}.json')) for side, dist in RUNS}
    for name in ['shared-reader-identity', 'bundle-differential', 'titles', 'suite-head', 'residuals-head']:
        inputs[name] = json.load(open(HERE / f'{name}.json'))
    return inputs


def reviewer_rows():
    rows = {}
    for name in ['purity-mutants.json', 'purity-mutants-2.json', 'egress-mutants-2.json', 'egress-mutants-3.json']:
        data = json.loads(git('show', f'HEAD:{ROUND2}/{name}'))
        for row in data['rows'] if isinstance(data, dict) else data:
            rows[row['id']] = [{'path': e['path'], 'old': e['old'], 'new': e['new']} for e in row['edits']]
    return rows


def derive(inputs):
    failures = []
    check = lambda ok, what: ok or failures.append(what)
    commits = {'head': HEAD, 'base': BASE}
    reviewer = reviewer_rows()
    record_digests = {f'{ROUND2}/{n}': hashlib.sha256(git('show', f'HEAD:{ROUND2}/{n}').encode()).hexdigest()
                      for n in ['purity-mutants.json', 'purity-mutants-2.json', 'egress-mutants-2.json', 'egress-mutants-3.json']}
    mutants = {}
    for side, dist in RUNS:
        run = inputs[f'{side}-{dist}']
        key = f'{side}-{dist}'
        check(run['commit'] == commits[side] and run['side'] == side and run['dist'] == dist, f'{key}: commit, side or dist')
        check(len(run['distDirs']) == (12 if dist == 'present' else 0), f'{key}: dist dirs')
        check(run['statusAfter'] == '' and run['leftovers'] == [], f'{key}: tree not restored')
        check(run['reviewerRecords'] == record_digests, f'{key}: reviewer records differ from the committed round-2 bytes')
        for row in run['rows']:
            rid = row['id']
            if rid in reviewer:
                check(row['edits'] == reviewer[rid], f'{key} {rid}: edits differ from the reviewer record')
            check(row['observed'] == row['expected'], f'{key} {rid}: observed {row["observed"]}, expected {row["expected"]}')
            entry = mutants.setdefault(rid, {})
            entry[key] = row['observed']
            if side == 'head' and row['observed'] == 'killed':
                entry.setdefault('killedAtHeadBy', sorted({t['name'] for t in row['failedTests']} | {f'file: {m.splitlines()[0][:160]}' for m in row['fileMessages']}))
    for prefix in REQUIRED:
        ids = [rid for rid in mutants if rid.split('-')[0] == prefix]
        check(len(ids) == 1, f'{prefix}: {len(ids)} rows')
        for rid in ids:
            check(all(mutants[rid].get(f'head-{d}') == 'killed' for d in ['absent', 'present']), f'{rid}: not killed at HEAD in both dist states')
    identity = inputs['shared-reader-identity']
    check(identity['base'] == BASE and identity['head'] == HEAD and identity['allAgree'] is True, 'shared reader: copies disagree')
    bundle = inputs['bundle-differential']
    check([r['commit'] for r in bundle['runs']] == [BASE, HEAD] and bundle['identical'] is True, 'bundle differential')
    check(all(r['failed'] == 0 and r['exit'] == 0 and r['statusAfter'] == '' for r in bundle['runs']), 'bundle differential: a run failed')
    titles = inputs['titles']
    check(titles['baseCommit'] == BASE and titles['headCommit'] == HEAD and titles['duplicatesHead'] == [], 'titles')
    suite = inputs['suite-head']
    check(suite['commit'] == HEAD and suite['exit'] == 0 and suite['failed'] == 0 and suite['cleanAfter'] is True, 'suite at HEAD')
    residuals = inputs['residuals-head']
    check(residuals['commit'] == HEAD and residuals['statusAfter'] == '', 'residuals: commit or tree')
    check([(r['id'], r['observed']) for r in residuals['rows']] == [(r['id'], 'survives') for r in residuals['rows']] and len(residuals['rows']) == 2, 'residuals: a disclosed form no longer survives')
    changed = sorted(git('diff', '--name-only', BASE, HEAD).split())
    check(changed == SUBJECT, f'subject: {changed}')
    since = sorted(git('diff', '--name-only', HEAD, 'HEAD').split())
    check(all(p.startswith('docs/evidence/syzygy-bpyt-6-14/') for p in since), f'tree HEAD changes more than this evidence since {HEAD}: {since}')
    summary = {
        'bead': 'syzygy-bpyt.6.14', 'base': BASE, 'head': HEAD, 'subject': SUBJECT,
        'subjectSha256': {p: hashlib.sha256(subprocess.run(['git', '-C', str(TREE), 'show', f'{HEAD}:{p}'], capture_output=True, check=True).stdout).hexdigest() for p in SUBJECT},
        'required': REQUIRED, 'mutants': mutants,
        'counts': {key: {'rows': len(inputs[key]['rows']), 'killed': sum(r['observed'] == 'killed' for r in inputs[key]['rows']),
                         'survives': sum(r['observed'] == 'survives' for r in inputs[key]['rows']),
                         'pass': sum(r['observed'] == 'pass' for r in inputs[key]['rows'])} for key in [f'{s}-{d}' for s, d in RUNS]},
        'sharedReaderSha256': {n: c['sha256'] for n, c in identity['copies'].items()},
        'bundle': [{k: r[k] for k in ['commit', 'distDirs', 'bytes', 'sha256']} for r in bundle['runs']],
        'titles': {k: titles[k] for k in ['base', 'head', 'added', 'removed']},
        'suite': {k: suite[k] for k in ['commit', 'distDirs', 'files', 'total', 'passed', 'failed', 'skipped']},
        'residualsSurviving': [r['id'] for r in residuals['rows'] if r['observed'] == 'survives'],
        'checksFailed': failures,
    }
    return summary


def main():
    mode = sys.argv[2] if len(sys.argv) > 2 else None
    inputs = load()
    summary = derive(inputs)
    if mode == '--selftest':
        def flip(i):
            i['head-absent']['rows'][1]['observed'] = 'survives'
        def commit(i):
            i['base-present']['commit'] = HEAD
        def status(i):
            i['head-present']['statusAfter'] = ' M packages/support/package.json\n'
        def fragment(i):
            row = next(r for r in i['head-present']['rows'] if r['id'].startswith('RP6-'))
            row['edits'][0]['new'] = row['edits'][0]['new'].replace("'node:f' + 's'", "'node:fs'")
        def dropped(i):
            i['head-absent']['rows'] = [r for r in i['head-absent']['rows'] if not r['id'].startswith('E9-')]
        def survived(i):
            row = next(r for r in i['head-present']['rows'] if r['id'].startswith('M2-'))
            row['observed'] = row['expected'] = 'survives'
        def dist(i):
            i['head-absent']['distDirs'] = ['packages/support/dist']
        def identity(i):
            i['shared-reader-identity']['allAgree'] = False
        def bundle(i):
            i['bundle-differential']['identical'] = False
        def suite(i):
            i['suite-head']['failed'] = 1
        def residual(i):
            i['residuals-head']['rows'][0]['observed'] = 'killed'
        survivors = []
        for mutate in [flip, commit, status, fragment, dropped, survived, dist, identity, bundle, suite, residual]:
            mutated = copy.deepcopy(inputs)
            mutate(mutated)
            if not derive(mutated)['checksFailed']:
                survivors.append(mutate.__name__)
        print('selftest:', 'all 11 mutations caught' if not survivors else f'survived: {survivors}')
        sys.exit(1 if survivors or summary['checksFailed'] else 0)
    if mode == '--check':
        stored = json.load(open(HERE / 'summary.json'))
        ok = stored == summary and not summary['checksFailed']
        print('check:', 'summary.json matches its inputs and no check fails' if ok else f"FAIL {summary['checksFailed']} equal={stored == summary}")
        sys.exit(0 if ok else 1)
    json.dump(summary, open(HERE / 'summary.json', 'w'), indent=1)
    print(json.dumps({k: summary[k] for k in ['counts', 'checksFailed']}, indent=1))


if __name__ == '__main__':
    main()
