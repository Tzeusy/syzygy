"""Compare a rule-6 re-run with the PR's record, mutant by mutant: outcome, failed count, total count, failed test names.
argv[1] = the PR's record, argv[2] = the re-run, argv[3:] = optional further re-run records whose mutants replace same-id rows."""
import collections
import json
import sys

rec = json.load(open(sys.argv[1], encoding='utf-8'))
runs = [json.load(open(p, encoding='utf-8')) for p in sys.argv[2:]]
mine = {}
for r in runs:
    for m in r['mutants']:
        mine[m['id']] = m
print('record', rec['subject']['commit'], len(rec['mutants']), 'mutants; re-run', ', '.join(r['subject']['commit'] for r in runs), len(mine), 'mutants')
print('record outcomes', dict(collections.Counter(m['outcome'] for m in rec['mutants'])))
print('re-run outcomes', dict(collections.Counter(m['outcome'] for m in mine.values())))
same = diff = 0
for m in rec['mutants']:
    o = mine.get(m['id'])
    if o is None:
        print('  missing from re-run:', m['id'])
        diff += 1
        continue
    a = (m['outcome'], m['failedTests'], m['totalTests'], sorted(f['test'] for f in m.get('failures') or []))
    b = (o['outcome'], o['failedTests'], o['totalTests'], sorted(f['test'] for f in o.get('failures') or []))
    if a == b and m['old'] == o['old'] and m['new'] == o['new']:
        same += 1
    else:
        diff += 1
        print(f"  {m['id']}: record {a[:3]} re-run {b[:3]} names-equal {a[3] == b[3]} fragments-equal {m['old'] == o['old'] and m['new'] == o['new']}")
print('identical outcome, counts, failed-test names and fragments:', same, 'of', len(rec['mutants']), '; differing', diff)
