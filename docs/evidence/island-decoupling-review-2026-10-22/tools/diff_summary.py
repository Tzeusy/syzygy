import json, sys
d = json.load(open(sys.argv[1]))
print('old', d['old']['commit'], 'new', d['new']['commit'])
for k in ['localRender', 'localRenderViaXorEntry', 'providerRender']:
    if k not in d: continue
    v = d[k]
    refused = sorted({r['refused'] for r in v['rows'] if r['refused']})
    print(f"{k}: {v['identical']}/{v['fixtures']} identical, {v['distinctOutputs']} distinct outputs; refusals: {refused}")
    for r in v['rows']:
        if not r['identical']: print('   DIFFERS', r['name'])
b = d['brief']
print(f"brief: {b['identical']}/{b['fixtures']} identical, {b['distinctOutputs']} distinct; guidance {b['guidance']}; carries guidance: {[r['carriesGuidance'] for r in b['rows']]}")
v = d['validators']
print(f"validators: {v['identical']}/{v['fixtures']} identical, {v['distinctOutcomes']} distinct outcomes, {v['refusals']} refusals; sameObjects: {v['sameObjects']}")
for r in v['rows']:
    if not r['identical']: print('   DIFFERS', r['fn'], r['name'])
import collections
print('  by fn:', dict(collections.Counter(r['fn'] for r in v['rows'])))
c = d['compiledModules']
print(f"compiled: {c['modules']} modules; identicalAfterLiveSpecifier {c['identicalAfterLiveSpecifier']}; outside imports {c['identicalOutsideImportStatements']}; code outside imports {c['identicalCodeOutsideImportStatements']}")
for r in c['rows']:
    if not r['identicalAfterLiveSpecifier']: print('   not identical after specifier:', r['file'], 'outside-imports', r['identicalOutsideImportStatements'], 'code', r['identicalCodeOutsideImportStatements'])
for r in c['rows']:
    if any(x in r['file'] for x in ['reverify', '/check.js', 'screen', 'class-gate', '/render.js']): print('   gate module', r['file'], 'afterSpecifier', r['identicalAfterLiveSpecifier'])
