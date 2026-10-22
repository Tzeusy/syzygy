"""Summarize the rule-6 mutants evidence record: counts, outcomes, fields present, per-id list, survivors, and whether each
mutant's `old` fragment occurs exactly once in the subject file at the subject commit (given as argv[2], the file's bytes)."""
import collections
import json
import sys

doc = json.load(open(sys.argv[1], encoding='utf-8'))
subject = open(sys.argv[2], encoding='utf-8').read()
ms = doc['mutants']
print('subject', json.dumps(doc['subject'])[:400])
print('runner', doc.get('runnerPath'), doc.get('runnerSha256'))
print('mutants', len(ms))
print('outcomes', collections.Counter(m['outcome'] for m in ms))
keys = collections.Counter(k for m in ms for k in m)
print('keys', dict(keys))
bad_once = []
for m in ms:
    if m['file'].endswith('package-reader.ts'):
        n = subject.count(m['old'])
        if n != 1:
            bad_once.append((m['id'], n))
print('old fragments not occurring exactly once in subject file:', bad_once)
for m in ms:
    print(f"{m['id']:<40} {m['outcome']:<9} {m.get('failedTests')}/{m.get('totalTests')}  file={m['file'].split('/')[-1]}")
for m in ms:
    if m['outcome'] != 'killed':
        print('SURVIVOR', json.dumps(m, indent=1)[:3000])
err = collections.Counter()
for m in ms:
    for f in m.get('failures', []):
        first = f.get('firstErrorLine', '')
        err[first.split(':')[0]] += 1
print('first error classes', err.most_common(20))
extra = {k: v for k, v in doc.items() if k not in ('mutants',)}
print('top-level keys', list(doc.keys()))
for k in ('note', 'notes', 'equivalent', 'equivalence'):
    if k in doc:
        print(k, json.dumps(doc[k], indent=1)[:3000])
