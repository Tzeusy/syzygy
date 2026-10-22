"""Print the mismatches of a differential record."""
import json
import sys

doc = json.load(open(sys.argv[1], encoding='utf-8'))
print('trees', [(t['role'], t['commit'][:8], t['packageReaderSha256'][:12]) for t in doc['trees']])
print('totals', json.dumps({k: doc['totals'][k] for k in ('worlds', 'answersCompared', 'mismatches', 'distinctAnswerVectors')}))
for m in doc['mismatches']:
    print(m['kind'], m['subject'], m['operator'], m['reader'], '| old:', m['old']['label'][:100], '| new:', m['new']['label'][:100])
