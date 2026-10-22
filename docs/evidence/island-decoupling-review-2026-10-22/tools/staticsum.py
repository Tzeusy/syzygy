"""Compact summaries of static_reach.mjs outputs: counts only, plus root importers. Usage: staticsum.py <json>..."""
import json, sys
for p in sys.argv[1:]:
    s = json.load(open(p))['summary']
    row = {k: (len(v) if isinstance(v, list) else v) for k, v in s.items() if k != 'root'}
    print(p.rsplit('/', 1)[-1], json.dumps(row))
    for k in ('rootImporters', 'problems'):
        if isinstance(s.get(k), list) and 0 < len(s[k]) <= 3: print('   ', k, s[k])
