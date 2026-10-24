#!/usr/bin/env python3
"""CPU milliseconds each CPU-time bound's region takes at the tree's head, beside its bound (syzygy-bpyt.4.5). Evidence tool, not authority.

usage: python3 -I cpu_margins.py TREE OUT.json [RUNS]

For each file holding `expect(cpuMsSince(cpu)).toBeLessThan(N);` it rewrites every such line to log
`PROBE {"cpuMs","bound"}` instead, runs the file RUNS times (default 5) with vitest, reads the PROBE lines, and restores
the file. It records each run's 1-minute load at start and end, and the largest region cost per logged region (in test order: a
site inside a loop or it.each logs once per case) against its bound.
The tree must be clean before and is checked clean after.
"""
import hashlib, json, os, re, subprocess, sys, time

tree, out_path = os.path.abspath(sys.argv[1]), sys.argv[2]
runs = int(sys.argv[3]) if len(sys.argv) > 3 else 5
SITE = re.compile(r'expect\(cpuMsSince\(cpu\)\)\.toBeLessThan\(([0-9_]+)\);')
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
if subprocess.run(['git', 'diff', '--quiet'], cwd=tree).returncode != 0: sys.exit('tree is not clean')
files = sorted(p for p in git('grep', '-l', '-F', 'expect(cpuMsSince(cpu)).toBeLessThan(').split('\n') if p)
load = lambda: float(open('/proc/loadavg').read().split()[0])
results = []
for rel in files:
    text = open(os.path.join(tree, rel), encoding='utf8').read()
    sites = len(SITE.findall(text))
    probe = SITE.sub(lambda m: "console.log('PROBE ' + JSON.stringify({ cpuMs: cpuMsSince(cpu), bound: " + m.group(1) + " }));", text)
    try:
        open(os.path.join(tree, rel), 'w', encoding='utf8').write(probe)
        for k in range(runs):
            start, began = load(), time.time()
            done = subprocess.run(['npx', 'vitest', 'run', rel], cwd=tree, capture_output=True, text=True, timeout=900,
                                  env={k2: v for k2, v in os.environ.items() if not k2.startswith('VITEST')})
            probes = [json.loads(l.split('PROBE ', 1)[1]) for l in done.stdout.splitlines() if 'PROBE {' in l]
            results.append({'file': rel, 'run': k + 1, 'sites': sites, 'exit': done.returncode, 'load1Start': start, 'load1End': load(),
                            'seconds': round(time.time() - began, 1), 'probes': probes})
            print(json.dumps(results[-1])[:400], flush=True)
    finally:
        open(os.path.join(tree, rel), 'w', encoding='utf8').write(text)
if subprocess.run(['git', 'diff', '--quiet'], cwd=tree).returncode != 0: sys.exit('tree not restored')
worst = {}
for r in results:
    for i, p in enumerate(r['probes']):
        key = (r['file'], i, p['bound'])
        worst[key] = max(worst.get(key, 0), p['cpuMs'])
json.dump({'tool': {'name': 'cpu_margins.py', 'sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()},
           'tree': git('rev-parse', 'HEAD').strip(), 'runs': runs, 'results': results,
           'worst': [{'file': f, 'probeIndex': i, 'boundMs': b, 'worstCpuMs': w, 'margin': round(b / w, 1) if w else None} for (f, i, b), w in sorted(worst.items())]},
          open(out_path, 'w'), indent=1)
