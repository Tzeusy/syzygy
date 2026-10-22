import json, sys
record, tree, mid = sys.argv[1], sys.argv[2], sys.argv[3]
m = next(x for x in json.load(open(record))['mutants'] if x['id'] == mid)
path = f"{tree}/{m['file']}"
src = open(path, encoding='utf8').read()
assert src.count(m['old']) == 1, (mid, src.count(m['old']))
open(path, 'w', encoding='utf8').write(src.replace(m['old'], m['new']))
print(mid, 'applied to', path)
