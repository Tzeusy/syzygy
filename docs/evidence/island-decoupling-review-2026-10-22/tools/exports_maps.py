"""Every workspace package's exports map: subpaths, condition keys in order, and whether Node's runtime choice (first key in
{node, import, default}) equals the boundary test's choice (`import ?? default`). Usage: exports_maps.py <repo>"""
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
n = 0
for parent in ('apps', 'packages'):
    for pj in sorted((root / parent).glob('*/package.json')):
        m = json.loads(pj.read_text())
        ex = m.get('exports')
        if ex is None:
            print(f"{m['name']}: no exports; main={m.get('main')}"); continue
        if isinstance(ex, str):
            print(f"{m['name']}: exports is a string {ex}"); continue
        for sub, target in ex.items():
            n += 1
            if isinstance(target, str):
                print(f"{m['name']} {sub}: {target}")
                continue
            keys = list(target)
            node_choice = next((target[k] for k in keys if k in ('node', 'import', 'default')), None)
            test_choice = target.get('import', target.get('default'))
            print(f"{m['name']} {sub}: keys={keys} node={node_choice} test={test_choice} {'SAME' if node_choice == test_choice else 'DIFFERENT'}")
print('subpaths:', n)
