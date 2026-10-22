"""Summarize the lane's locators.json: counts, shifted rows, bound citers. Usage: locsum.py <locators.json>"""
import json, sys
d = json.load(open(sys.argv[1]))
for k in ('old', 'new', 'changedFiles', 'existingAtOld', 'locators', 'ambiguousSkipped', 'staleAtOld', 'shifted'):
    v = d[k]
    print(k, v if not isinstance(v, list) else f'list of {len(v)}')
print('shiftedInBoundCiters:', json.dumps(d['shiftedInBoundCiters'], indent=1)[:3000])
print('boundCitersAnyLocator:', json.dumps(d['boundCitersAnyLocator'], indent=1)[:3000])
print('shiftedTable:')
t = d['shiftedTable']
print(t if isinstance(t, str) else json.dumps(t, indent=1)[:6000])
print('shiftedRows sample keys:', list(d['shiftedRows'][0]) if d['shiftedRows'] else None)
print('rows count', len(d['rows']), 'row keys', list(d['rows'][0]) if d['rows'] else None)
