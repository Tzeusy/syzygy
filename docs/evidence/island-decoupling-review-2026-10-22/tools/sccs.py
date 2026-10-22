"""Import cycles among in-repo modules in a static_reach.mjs graph: strongly connected components of size > 1 (or a self-loop),
over every edge kind. Usage: sccs.py <before.json> <after.json>"""
import json, sys
def graph(p):
    d = json.load(open(p))
    g = {}
    for e in d['edges']:
        to = e.get('module')
        if to and not e.get('builtin') and not e.get('external'):
            g.setdefault(e['from'], set()).add(to)
    return d, g
def sccs(g):
    index, low, stack, on, out, i = {}, {}, [], set(), [], [0]
    nodes = set(g) | {v for vs in g.values() for v in vs}
    def visit(v):
        index[v] = low[v] = i[0]; i[0] += 1; stack.append(v); on.add(v)
        for w in g.get(v, ()):
            if w not in index: visit(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop(); on.discard(w); comp.append(w)
                if w == v: break
            if len(comp) > 1 or v in g.get(v, ()): out.append(sorted(comp))
    sys.setrecursionlimit(10000)
    for v in sorted(nodes):
        if v not in index: visit(v)
    return out
for p in sys.argv[1:3]:
    d, g = graph(p)
    keys = sorted({k for e in d['edges'] for k in e})
    comps = sccs(g)
    print(p.rsplit('/', 1)[-1], 'edge keys', keys, 'nodes', len(set(g) | {v for vs in g.values() for v in vs}), 'cycles', len(comps))
    for c in comps: print('   ', len(c), c[:8])
