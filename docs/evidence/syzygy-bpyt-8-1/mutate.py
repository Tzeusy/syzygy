#!/usr/bin/env python3
"""syzygy-bpyt.8.1 rule-6 runner (AGENTS.md verification rule 6): apply each mutant's single-occurrence replacement, run the named
vitest files, record every failed test's name and first error line, restore the file from git.
Usage: python3 mutate.py <tree> SPEC.json OUT.json   (the tree's tracked files must be committed and clean)
SPEC.json: {"mutants": [{id, file, old, new, also?, tests, project | config, note?}]}; `old` must occur exactly once in `file`, and so
must each `also` entry's `old` after the edits before it (a move is two edits: delete in one place, insert in another).
OUT.json records the commit, the sha256 of each mutated file and test file as committed, and this runner's sha256."""
import datetime, hashlib, json, pathlib, subprocess, sys, tempfile

tree, spec = pathlib.Path(sys.argv[1]).resolve(), json.loads(pathlib.Path(sys.argv[2]).read_text())
sha = lambda data: hashlib.sha256(data).hexdigest()
run = lambda cmd: subprocess.run(cmd, cwd=tree, capture_output=True, text=True)
if run(['git', 'status', '--porcelain', '--untracked-files=no']).stdout.strip(): sys.exit('tracked files not clean')
head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
committed = lambda f: sha(subprocess.run(['git', 'show', f'HEAD:{f}'], cwd=tree, capture_output=True, check=True).stdout)
out = {'format': 'syzygy-bpyt-8-1-mutants/1', 'commit': head, 'runnerSha256': sha(pathlib.Path(__file__).read_bytes()),
       'runner': 'single-occurrence replacement of `old` by `new` in `file`, then `npx vitest run` over `tests` (by project, or by config); '
                 'killed = at least one failed test, errored = no test result (the file failed to collect); restored from git after each run',
       'fileSha256': {f: committed(f) for f in sorted({m['file'] for m in spec['mutants']})},
       'testFileSha256': {t: committed(t) for t in sorted({t for m in spec['mutants'] for t in m['tests']})},
       'ranAt': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'mutants': []}
for m in spec['mutants']:
    target = tree / m['file']
    original = target.read_text(encoding='utf8')
    mutated = original
    for edit in [m, *m.get('also', [])]:
        if mutated.count(edit['old']) != 1: sys.exit(f"{m['id']}: `old` occurs {mutated.count(edit['old'])} times in {m['file']}")
        mutated = mutated.replace(edit['old'], edit['new'])
    target.write_text(mutated, encoding='utf8')
    with tempfile.TemporaryDirectory() as scratch:
        report = pathlib.Path(scratch) / 'report.json'
        where = ['--config', m['config']] if 'config' in m else ['--project', m['project']]
        try:
            run(['npx', 'vitest', 'run', *where, *m['tests'], '--reporter=json', f'--outputFile={report}'])
        finally:
            run(['git', 'checkout', '--', m['file']])
        result = json.loads(report.read_text()) if report.exists() else None
    failed, total, errored_files = [], 0, []
    for suite in (result or {}).get('testResults', []):
        if suite.get('status') == 'failed' and not suite.get('assertionResults'):
            errored_files.append({'file': str(pathlib.Path(suite['name']).relative_to(tree)), 'firstErrorLine': (suite.get('message') or '').strip().split('\n')[0]})
        for test in suite.get('assertionResults', []):
            total += 1
            if test['status'] == 'failed':
                first = next((line for line in '\n'.join(test.get('failureMessages', [])).split('\n') if line.strip()), '')
                failed.append({'test': test['fullName'], 'firstErrorLine': first.strip()})
    outcome = 'errored' if result is None or (total == 0 and errored_files) else ('killed' if failed or errored_files else 'survived')
    out['mutants'].append({**{k: m[k] for k in ('id', 'file', 'old', 'new', 'tests')}, **({'also': m['also']} if 'also' in m else {}),
                           **({'project': m['project']} if 'project' in m else {'config': m['config']}),
                           'outcome': outcome, 'totalTests': total, 'failedTests': failed, 'erroredFiles': errored_files, **({'note': m['note']} if 'note' in m else {})})
    print(m['id'], outcome, len(failed), flush=True)
if run(['git', 'status', '--porcelain', '--untracked-files=no']).stdout.strip(): sys.exit('tree not restored')
pathlib.Path(sys.argv[3]).write_text(json.dumps(out, indent=2) + '\n')
