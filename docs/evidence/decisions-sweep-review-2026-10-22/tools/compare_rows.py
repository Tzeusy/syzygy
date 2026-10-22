# Compare a reviewer differential run's world rows with the retained record's rows, keyed by (kind, base, subject, operator).
import json, sys, collections
mine, theirs = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
key = lambda r: (r['kind'], r['base'], r['subject'], r['operator'])
t = collections.defaultdict(list)
for r in theirs['worlds']: t[key(r)].append(r)
dup = sum(1 for v in t.values() if len(v) > 1)
kinds = collections.Counter(r['kind'] for r in mine['worlds'])
same_vec = same_lab = missing = 0; diff = []
for r in mine['worlds']:
    cand = t.get(key(r), [])
    if not cand: missing += 1; continue
    if any(c['answers'] == r['answers'] for c in cand): same_vec += 1
    else: diff.append(key(r))
    if any(c.get('labels') == r.get('labels') for c in cand): same_lab += 1
print(json.dumps({'myWorlds': len(mine['worlds']), 'byKind': kinds, 'recordKeysWithDuplicates': dup, 'missingInRecord': missing,
                  'answerVectorEqualToRecord': same_vec, 'labelVectorEqualToRecord': same_lab, 'vectorDiffers': len(diff), 'firstDiffers': diff[:5],
                  'myTotals': {k: mine['totals'][k] for k in ('worlds', 'answersCompared', 'mismatches', 'distinctAnswerVectors', 'distinctLabelVectors')},
                  'myCorpus': mine['corpus']['sha256'], 'myTrees': [(x['role'], x['commit'][:8], x['clean'], x['sha256']['packageReaderJs'][:12]) for x in mine['trees']],
                  'myScript': mine['script']['sha256'][:12]}, default=dict))
