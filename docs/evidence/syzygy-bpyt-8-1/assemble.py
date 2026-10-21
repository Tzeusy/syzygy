#!/usr/bin/env python3
"""syzygy-bpyt.8.1: one index over this directory's records (rule 11): the subject commit, the sha256 of every file the change touches
at that commit, and each record's own sha256 and headline counts, read from the record. Usage: python3 assemble.py <tree> > evidence.json"""
import hashlib, json, pathlib, subprocess, sys

tree = pathlib.Path(sys.argv[1]).resolve()
here = pathlib.Path(__file__).resolve().parent
load = lambda name: json.loads((here / name).read_text())
sha = lambda data: hashlib.sha256(data).hexdigest()
git = lambda *args: subprocess.run(['git', '-C', str(tree), *args], capture_output=True, check=True).stdout

reach_before, reach_after = load('reach-before.json'), load('reach-after.json')
diff, mutants, regen, citers, tests = load('differential.json'), load('mutants.json'), load('regen-check.json'), load('digest-citers.json'), load('tests-delta.json')
subject = mutants['commit']
for name, commit in [('reach-after.json', reach_after['commit']), ('differential.json', diff['new']['commit']), ('regen-check.json', regen['commit']),
                     ('digest-citers.json', citers['new']), ('tests-delta.json', tests['new'])]:
    assert commit == subject, f'{name} ran at {commit}, not the subject {subject}'
assert reach_before['commit'] == diff['old']['commit'] == citers['old'] == tests['old'], 'the records disagree on the commit before'

def reach(record):
    return {k: {'reachableModules': record[k]['reachableCount'], 'reachableIslandModules': len(record[k]['reachableIsland']),
                'coreRootImporters': record[k]['coreRootImporters'], 'edgesIntoIsland': len(record[k]['edgesIntoIsland']), 'unresolved': len(record[k]['unresolved'])}
            for k in ('everyEdge', 'consentPortsUnfollowed')}

outcomes = {}
for m in mutants['mutants']: outcomes.setdefault(m['outcome'], []).append(m['id'])
changed = [r['file'] for r in citers['rows']] + citers['addedFiles']
print(json.dumps({
    'format': 'syzygy-bpyt-8-1-index/1', 'bead': 'syzygy-bpyt.8.1',
    'subjectCommit': subject, 'commitBefore': reach_before['commit'], 'beadBaseCommit': '3000698f3706a7e583a21be37dfdc30e3ffef551',
    'subjectFileSha256': {f: (sha(git('show', f'{subject}:{f}')) if f in {p.decode() for p in git('ls-tree', '-r', '--name-only', '-z', subject).split(b'\0') if p} else None) for f in sorted(changed)},
    'records': {name: sha((here / name).read_bytes()) for name in sorted(p.name for p in here.glob('*.json') if p.name != 'evidence.json')},
    'scripts': {str(p.relative_to(here)): sha(p.read_bytes()) for p in sorted([*here.glob('*.py'), *here.glob('*.mjs'), *here.glob('gen/*')])},
    'reachability': {'before': reach(reach_before), 'after': reach(reach_after), 'islandModules': reach_after['islandCount']},
    'differential': {k: {'fixtures': diff[k]['fixtures'], 'identical': diff[k]['identical'], 'distinctOutputs': diff[k].get('distinctOutputs', diff[k].get('distinctOutcomes'))}
                     for k in ('localRender', 'providerRender', 'brief', 'validators')}
                    | {'guidanceIdentical': diff['brief']['guidance']['identical'],
                       'compiledModules': {k: diff['compiledModules'][k] for k in ('modules', 'identicalAfterLiveSpecifier', 'identicalOutsideImportStatements', 'identicalCodeOutsideImportStatements')}},
    'mutants': {'total': len(mutants['mutants']), **{k: len(v) for k, v in outcomes.items()}, 'survivors': outcomes.get('survived', [])},
    'regeneratedSplitIdentical': regen['allIdentical'],
    'digestCiters': {'changedFiles': citers['changedFiles'], 'citedFiles': citers['citedFiles'], 'citerClasses': citers['citerClasses'], 'governedPlaneCiters': citers['governedPlaneCiters']},
    'tests': tests['summary'],
}, indent=2))
