"""Compare two check_governance.py outputs: status lines by check id, and the last 4 lines of each. Usage: cgcmp.py <old.txt> <new.txt>"""
import re, sys
def parse(p):
    text = open(p).read().split('\n')
    rows = {}
    for line in text:
        m = re.match(r'^(OK|WARN|FAIL|ERROR)\s+(CG-\S+)\s+(.*)$', line)
        if m: rows[m.group(2)] = (m.group(1), m.group(3))
    return text, rows
(ta, a), (tb, b) = parse(sys.argv[1]), parse(sys.argv[2])
print('old head:', ta[:2]); print('new head:', tb[:2])
print('checks old', len(a), 'new', len(b))
from collections import Counter
print('old statuses', Counter(v[0] for v in a.values())); print('new statuses', Counter(v[0] for v in b.values()))
for k in sorted(set(a) | set(b)):
    if a.get(k) != b.get(k): print('DIFF', k, '\n   old:', a.get(k), '\n   new:', b.get(k))
for k, v in b.items():
    if v[0] in ('FAIL', 'ERROR'): print('NEW-FAIL', k, v)
print('old tail:', [l for l in ta if l.strip()][-3:]); print('new tail:', [l for l in tb if l.strip()][-3:])
