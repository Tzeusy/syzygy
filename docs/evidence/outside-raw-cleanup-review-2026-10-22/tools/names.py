"""Compare the test-name sets of two vitest JSON reports (base and fix), and print the row outcomes for every scenario.
Usage: python3 names.py <reports dir>
"""
import json, sys
from pathlib import Path

reports = Path(sys.argv[1])
names = lambda f: sorted(t['fullName'] for r in json.loads((reports / f).read_text())['testResults'] for t in r['assertionResults'])
base, fix = names('U-base.json'), names('U-fix.json')
print('base', len(base), 'fix', len(fix), 'distinct', len(set(base)), len(set(fix)))
print('added', sorted(set(fix) - set(base)))
print('removed', sorted(set(base) - set(fix)))
for f in sorted(reports.glob('*.json')):
    data = json.loads(f.read_text())
    statuses = {}
    for r in data['testResults']:
        for t in r['assertionResults']:
            statuses[t['status']] = statuses.get(t['status'], 0) + 1
    print(f.stem, statuses)
