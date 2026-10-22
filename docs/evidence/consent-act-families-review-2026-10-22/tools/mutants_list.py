"""Print each mutant's id, old and new fragments (shortened to their differing middle)."""
import json
import sys

doc = json.load(open(sys.argv[1], encoding='utf-8'))
for m in doc['mutants']:
    old, new = m['old'], m['new']
    i = 0
    while i < min(len(old), len(new)) and old[i] == new[i]:
        i += 1
    j = 0
    while j < min(len(old), len(new)) - i and old[-1 - j] == new[-1 - j]:
        j += 1
    ctx = 30
    o = old[max(0, i - ctx):len(old) - j + ctx]
    n = new[max(0, i - ctx):len(new) - j + ctx]
    print(f"{m['id']}: [{o}] -> [{n}]")
