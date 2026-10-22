import json, sys
rec = json.load(open(sys.argv[1]))
src = open(sys.argv[2], encoding='utf8').read()
for m in rec['mutants']:
    print('=' * 100)
    print(m['id'], '| occurrences of old in subject file:', src.count(m['old']), '| tests:', len(m.get('tests', [])), '| failed:', m.get('failedTests'), '| total:', m.get('totalTests'))
    print('--- old:'); print(m['old'])
    print('--- new:'); print(m['new'])
    ft = m.get('failures', [])
    for t in ft[:4]:
        print('   failed:', (t if isinstance(t, str) else json.dumps(t))[:220])
