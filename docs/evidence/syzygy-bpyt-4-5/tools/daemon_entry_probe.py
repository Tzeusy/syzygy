#!/usr/bin/env python3
"""Which daemon-entry rows fail when the daemon path loads the POC app (syzygy-bpyt.4.5). Evidence tool, not authority.

usage: python3 -I daemon_entry_probe.py TREE OUT.json [TEST-FILE-SOURCE-COMMIT]

For each mutant of apps/syzygy/src/main.ts, of a module it imports, or of the test file (and a control with none) it applies the fragment; a
mutant whose `old` does not occur exactly once is recorded as skipped (the H- mutants exist only in the new test). It rebuilds apps/syzygy with `tsc -b`, runs packages/cap1-system/src/daemon-entry-unchanged.system.test.ts
under the system-tier config with the JSON reporter, records every row's status, restores main.ts and rebuilds. With
TEST-FILE-SOURCE-COMMIT, the test file is first replaced by that commit's copy (and restored afterwards), so one tree
can be probed with the old and the new test. Each run is its own session; one that outlives LIMIT_S is SIGKILLed as
a group. It checks the tree is clean (`git diff --quiet`) at the end.
"""
import hashlib, json, os, signal, subprocess, sys, time

tree, out_path = os.path.abspath(sys.argv[1]), sys.argv[2]
test_source = sys.argv[3] if len(sys.argv) > 3 else None
MAIN = 'apps/syzygy/src/main.ts'
TEST = 'packages/cap1-system/src/daemon-entry-unchanged.system.test.ts'
LIMIT_S = 600
ANCHOR = "import { resolvePathIntent } from '@syzygy/polaris-dossier/state-directory';\n"
DAEMON = "  let parsed = parseCli(process.argv.slice(2), process.env);\n"
MUTANTS = [
    None,
    {'id': 'P-static', 'file': MAIN, 'note': 'a static side-effect import of the POC app at module top',
     'old': ANCHOR, 'new': ANCHOR + "import '@syzygy/three-surface-poc-app/dossier-site';\n"},
    {'id': 'P-daemon-dynamic', 'file': MAIN, 'note': 'a dynamic import of the POC app on the daemon path, before parseCli',
     'old': DAEMON, 'new': "  await import('@syzygy/three-surface-poc-app/dossier-site');\n" + DAEMON},
    {'id': 'P-transitive', 'file': 'packages/polaris-dossier/src/state-directory.ts',
     'note': 'a module main.ts imports statically (polaris-dossier state-directory) imports the POC app; main.ts itself is unchanged',
     'old': "import * as path from 'node:path';\n", 'new': "import * as path from 'node:path';\nimport '@syzygy/three-surface-poc-app/dossier-site';\n"},
    {'id': 'H-hook-blind', 'file': TEST, 'note': "the hook's POC-app prefix points at a directory nothing loads from (the new row only)",
     'old': "    const app = `${pathToFileURL(realpathSync(path.join(REPO_ROOT, 'apps', 'three-surface-poc'))).href}/`;\n",
     'new': "    const app = `${pathToFileURL(realpathSync(path.join(REPO_ROOT, 'apps', 'three-surface-poc'))).href}/no-such-dir/`;\n"},
    {'id': 'H-no-preload', 'file': TEST, 'note': 'NODE_OPTIONS carries no --import, so no hook runs (the new row only)',
     'old': "    const hooked = { NODE_OPTIONS: `--import=${pathToFileURL(hook).href}`, POC_APP_URL: app, POC_LOAD_LOG: log };\n",
     'new': "    const hooked = { NODE_OPTIONS: '', POC_APP_URL: app, POC_LOAD_LOG: log };\n"},
]
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
sha = lambda path: hashlib.sha256(open(path, 'rb').read()).hexdigest()

def build():
    done = subprocess.run(['npx', 'tsc', '-b', 'apps/syzygy'], cwd=tree, capture_output=True, text=True)
    if done.returncode != 0: sys.exit(f'build failed: {done.stdout[-2000:]}{done.stderr[-2000:]}')

def run(mutant):
    main_text = open(os.path.join(tree, MAIN), encoding='utf8').read()
    test_text = open(os.path.join(tree, TEST), encoding='utf8').read()
    other = mutant['file'] if mutant and mutant['file'] not in (MAIN, TEST) else None
    other_text = open(os.path.join(tree, other), encoding='utf8').read() if other else None
    report = os.path.join(os.environ.get('TMPDIR', '/tmp'), f'daemon-entry-{mutant["id"] if mutant else "control"}.json')
    try:
        if test_source: open(os.path.join(tree, TEST), 'w', encoding='utf8').write(git('show', f'{test_source}:{TEST}'))
        if mutant:
            target = open(os.path.join(tree, mutant['file']), encoding='utf8').read()
            if target.count(mutant['old']) != 1:
                return {'mutant': mutant, 'skipped': f'old occurs {target.count(mutant["old"])} times in {mutant["file"]}', 'failed': [], 'passed': 0, 'exit': None}
            open(os.path.join(tree, mutant['file']), 'w', encoding='utf8').write(target.replace(mutant['old'], mutant['new']))
        build()
        began, load = time.time(), float(open('/proc/loadavg').read().split()[0])
        child = subprocess.Popen(['npx', 'vitest', 'run', '--config', 'packages/cap1-system/vitest.config.ts', TEST, '--reporter=json',
                                  f'--outputFile={report}'], cwd=tree, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                 start_new_session=True, env={k: v for k, v in os.environ.items() if not k.startswith('VITEST')})
        killed = False
        try: child.communicate(timeout=LIMIT_S)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL); killed = True; child.communicate()
        rows = []
        if os.path.exists(report):
            for suite in json.load(open(report, encoding='utf8'))['testResults']:
                rows += [{'title': a['fullName'], 'status': a['status'], 'failure': (a.get('failureMessages') or [''])[0][:300]} for a in suite['assertionResults']]
        return {'mutant': mutant, 'exit': child.returncode, 'killedAfterLimit': killed, 'seconds': round(time.time() - began, 1), 'load1Start': load,
                'rows': rows, 'failed': sorted(r['title'] for r in rows if r['status'] == 'failed'), 'passed': sum(r['status'] == 'passed' for r in rows)}
    finally:
        open(os.path.join(tree, MAIN), 'w', encoding='utf8').write(main_text)
        open(os.path.join(tree, TEST), 'w', encoding='utf8').write(test_text)
        if other: open(os.path.join(tree, other), 'w', encoding='utf8').write(other_text)
        if os.path.exists(report): os.remove(report)

results = []
for m in MUTANTS:
    results.append(run(m)); r = results[-1]
    print(json.dumps({'mutant': m['id'] if m else 'control', 'exit': r['exit'], 'passed': r['passed'], 'failed': r['failed']}), flush=True)
build()
if subprocess.run(['git', 'diff', '--quiet'], cwd=tree).returncode != 0: sys.exit('tree not restored')
json.dump({'tool': {'name': os.path.basename(__file__), 'sha256': sha(os.path.abspath(__file__))}, 'commit': git('rev-parse', 'HEAD').strip(),
           'testFileFrom': test_source or 'the tree', 'testFileSha256': hashlib.sha256((git('show', f'{test_source}:{TEST}') if test_source else
           open(os.path.join(tree, TEST), encoding='utf8').read()).encode()).hexdigest(), 'results': results}, open(out_path, 'w'), indent=1)
