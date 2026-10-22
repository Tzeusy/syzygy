import json, sys, collections
d = json.load(open(sys.argv[1]))
s = d['summary']
c = collections.Counter(n['kind'] for n in s['notes'])
print('note kinds:', dict(c))
for n in s['notes']:
    if n['kind'] != 'process-spawn' or (len(sys.argv) > 2 and sys.argv[2] == 'all'):
        print(n['kind'], f"{n['file']}:{n['line']}", n['text'][:200].replace('\n', ' '))
spawn_files = collections.Counter(n['file'] for n in s['notes'] if n['kind'] == 'process-spawn')
print('process-spawn by file:', dict(spawn_files))
print('intoIsland:')
for e in s['intoIsland']:
    print('  ', e)
print('rootImporters:')
for e in s['rootImporters']:
    print('  ', e)
print('edge kinds:', dict(collections.Counter(e['kind'] for e in d['edges'])))
print('problems:', s['problems'])
