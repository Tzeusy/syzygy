"""Compare a mutant re-run with the lane's recorded mutants.json: per-id outcome, killing test count, and fragments. Usage:
mutcmp.py <lane mutants.json> <rerun.json>"""
import json, sys
a, b = (json.load(open(p)) for p in sys.argv[1:3])
def index(d):
    rows = d['mutants'] if isinstance(d, dict) and 'mutants' in d else d['results'] if isinstance(d, dict) and 'results' in d else d
    return {r['id']: r for r in rows}
print('lane top keys:', list(a) if isinstance(a, dict) else type(a).__name__, '| rerun top keys:', list(b) if isinstance(b, dict) else type(b).__name__)
ia, ib = index(a), index(b)
print('lane ids', len(ia), 'rerun ids', len(ib), 'same ids', set(ia) == set(ib))
for k in sorted(set(ia) | set(ib)):
    x, y = ia.get(k, {}), ib.get(k, {})
    same_frag = x.get('old') == y.get('old') and x.get('new') == y.get('new')
    print(f"{k}: lane {x.get('outcome')} rerun {y.get('outcome')} {'SAME' if x.get('outcome') == y.get('outcome') else 'DIFFERENT'} fragments-equal {same_frag}")
    if y.get('outcome') != 'killed':
        print('     rerun detail:', {kk: (str(v)[:200]) for kk, v in y.items() if kk not in ('old', 'new')})
