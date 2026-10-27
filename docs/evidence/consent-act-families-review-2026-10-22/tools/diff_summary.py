"""Summarize a differential evidence record: everything but the per-world rows and per-reader answer lists."""
import collections
import json
import sys

doc = json.load(open(sys.argv[1], encoding='utf-8'))
for k, v in doc.items():
    if k in ('worlds', 'answersPerReader'):
        continue
    s = json.dumps(v)
    print(k, ':', s if len(s) < 1500 else s[:1500] + ' ...')
rows = doc['worlds']
print('rows', len(rows), 'same', sum(1 for r in rows if r['same']), 'not same', sum(1 for r in rows if not r['same']))
print('rows by kind', dict(collections.Counter(r['kind'] for r in rows)))
print('subjects by kind', dict(collections.Counter((r['kind'], (r['subject'] or '').split(':')[0]) for r in rows if r['kind'] in ('line', 'named', 'record'))))
apr = doc['answersPerReader']
for name, answers in apr.items():
    print(f'{name}: {len(answers)} distinct; top labels:')
    for a in answers[:6]:
        print(f"    {a['worlds']:>5}  {a['label'][:160]}")
if len(sys.argv) > 2:
    other = json.load(open(sys.argv[2], encoding='utf-8'))
    print('--- compare with', sys.argv[2])
    print('totals equal:', doc['totals'] == other['totals'])
    for k in doc['totals']:
        if doc['totals'][k] != other['totals'][k]:
            print('  totals differ at', k, json.dumps(doc['totals'][k])[:300], json.dumps(other['totals'][k])[:300])
    a = [(r['kind'], r['subject'], r['operator'], r['answers']) for r in doc['worlds']]
    b = [(r['kind'], r['subject'], r['operator'], r['answers']) for r in other['worlds']]
    print('world rows identical (kind, subject, operator, answer-vector sha):', a == b, len(a), len(b))
    if a != b:
        sa, sb = set(a), set(b)
        print('  only in first', len(sa - sb), 'only in second', len(sb - sa))
        for x in list(sa - sb)[:10]:
            print('   first-only', x)
        for x in list(sb - sa)[:10]:
            print('   second-only', x)
