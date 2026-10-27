"""Compare the lane's locators.json with a re-run at another head: counts and the shifted row set. Then spot-check two raw locators
by reading the cited lines at the raw's reviewed commit and at the base. Usage: loccmp.py <lane.json> <rerun.json> <repo>"""
import json, subprocess, sys
a, b = (json.load(open(p)) for p in sys.argv[1:3])
repo = sys.argv[3]
for k in ('changedFiles', 'existingAtOld', 'locators', 'ambiguousSkipped', 'staleAtOld', 'shifted'):
    print(k, 'lane', a[k] if not isinstance(a[k], list) else len(a[k]), 'rerun', b[k] if not isinstance(b[k], list) else len(b[k]))
key = lambda r: (r['target'], r['citer'], r['citerLine'], r['locator'])
sa, sb = {key(r) for r in a['shiftedRows']}, {key(r) for r in b['shiftedRows']}
print('shifted sets equal:', sa == sb, 'only lane', sorted(sa - sb), 'only rerun', sorted(sb - sa))
ra, rb = {key(r): r for r in a['rows']}, {key(r): r for r in b['rows']}
print('row keys equal:', set(ra) == set(rb), 'rows differing in a field:', sum(1 for k in ra if k in rb and ra[k] != rb[k]))
show = lambda c, p, lo, hi: subprocess.run(['git', '-C', repo, 'show', f'{c}:{p}'], capture_output=True).stdout.decode().split('\n')[lo - 1:hi]
for commit, path, lo, hi in (('4f3c3ebf', 'apps/syzygy/src/main.ts', 258, 258), ('4f3c3ebf', 'apps/syzygy/src/main.ts', 270, 270),
                             ('cf3ba3fe', 'packages/polaris-dossier/src/brief.ts', 248, 250)):
    at_review, at_base, at_head = show(commit, path, lo, hi), show('c55acb73', path, lo, hi), show('6ac21f2c', path, lo, hi)
    print(f'{path}:{lo}-{hi} reviewed {commit} == base: {at_review == at_base}; base == head: {at_base == at_head}')
    print('   at review:', at_review)
    print('   at head  :', at_head)
