import json, sys
old = json.load(open(sys.argv[1]))['result']
new = json.load(open(sys.argv[2]))['result']
for k in new:
    o, n = set(old.get(k) or []), set(new.get(k) or [])
    # a name that changes between value and type counts as removed+added; compare by bare name too
    bare = lambda s: {x.replace(' (type)', '') for x in s}
    print(f'{k}: old={len(o)} new={len(n)} removed={sorted(o - n)} added={sorted(n - o)} bare_removed={sorted(bare(o) - bare(n))}')
live = set(new['core ./live']); root = set(new['core .'])
print('live subset of root:', live <= root, 'live minus root:', sorted(live - root))
print('root minus live:', sorted(root - live))
