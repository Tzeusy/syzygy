#!/usr/bin/env python3
"""Rule-6 runner (AGENTS.md verification rule 6): apply each mutant fragment, run the named vitest files, record the outcome, restore.
usage: python3 scripts/rule6_mutation_runner.py SPEC.json OUT.json   (cwd = worktree root, tree committed and clean)
SPEC.json carries `project` and `mutants` (id, file, old, new, tests, optional project and note); a previous OUT.json is a valid SPEC.
OUT.json records the commit, the sha256 of each mutated file and of each test file as committed, and this runner's path and sha256."""
import hashlib, json, re, subprocess, sys, datetime
spec = json.load(open(sys.argv[1]))
sha = lambda b: hashlib.sha256(b).hexdigest()
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
head = run(['git','rev-parse','HEAD']).stdout.strip()
dirty = run(['git','status','--porcelain','--untracked-files=no']).stdout.strip()
if dirty: sys.exit('tree not clean:\n'+dirty)
tests = sorted({t for m in spec['mutants'] for t in m['tests']})
subject = {f: sha(run(['git','show',f'HEAD:{f}']).stdout.encode()) for f in sorted({m['file'] for m in spec['mutants']} | set(spec.get('subjectFiles', [])))}
out = {'subject': {'commit': head, 'branch': run(['git','rev-parse','--abbrev-ref','HEAD']).stdout.strip(), 'fileSha256': subject, 'testFileSha256': {t: sha(run(['git','show',f'HEAD:{t}']).stdout.encode()) for t in tests}},
       'runnerPath': 'scripts/rule6_mutation_runner.py', 'runnerSha256': sha(run(['git','show','HEAD:scripts/rule6_mutation_runner.py']).stdout.encode()),
       'runner': 'single-occurrence textual replacement of `old` by `new` in `file`, then `npx vitest run --project <project> <testFiles>`; killed = at least one failed test; file restored from git after each run',
       'project': spec['project'], 'ranAt': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'mutants': []}
for m in spec['mutants']:
    orig = open(m['file'], encoding='utf8').read()
    if orig.count(m['old']) < 1: sys.exit(f"fragment not found for {m['id']}")
    open(m['file'], 'w', encoding='utf8').write(orig.replace(m['old'], m['new'], 1))
    try:
        r = run(['npx','vitest','run','--project',m.get('project',spec['project']),*m['tests']])
    finally:
        run(['git','checkout','--',m['file']])
    text = r.stdout + r.stderr
    f = re.search(r'Tests\s+(\d+) failed', text)
    tot = re.search(r'Tests\s+.*?\((\d+)\)', text)
    failed = int(f.group(1)) if f else (0 if tot else None)
    total = int(tot.group(1)) if tot else None
    killed = (failed or 0) > 0 or tot is None   # no Tests line = the run errored (collection or compile failure)
    out['mutants'].append({'id': m['id'], 'file': m['file'], 'old': m['old'], 'new': m['new'], 'tests': m['tests'], 'outcome': ('errored' if tot is None else 'killed') if killed else 'survived', 'failedTests': failed, 'totalTests': total, **({'note': m['note']} if 'note' in m else {})})
    print(m['id'], out['mutants'][-1]['outcome'], failed, flush=True)
assert not run(['git','status','--porcelain','--untracked-files=no']).stdout.strip(), 'tree not restored'
json.dump(out, open(sys.argv[2], 'w'), indent=2); open(sys.argv[2], 'a').write('\n')
