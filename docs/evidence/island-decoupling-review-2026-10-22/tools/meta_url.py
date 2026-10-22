import json, re, sys, os
root = sys.argv[1]
d = json.load(open(sys.argv[2]))
mods = d['reachedModules']
n = 0
for m in mods:
    text = open(os.path.join(root, m), encoding='utf8').read()
    for i, line in enumerate(text.split('\n'), 1):
        if 'import.meta' in line or re.search(r"\.(m?js)['\"`]", line) and ('URL(' in line or 'path.join' in line or 'resolve(' in line):
            n += 1
            print(f'{m}:{i}: {line.strip()[:200]}')
print('modules scanned:', len(mods), 'hits:', n)
