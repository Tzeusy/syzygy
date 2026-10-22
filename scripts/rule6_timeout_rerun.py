#!/usr/bin/env python3
"""Re-run named mutants of a rule-6 record (scripts/rule6_mutation_runner.py output) with one change: vitest's per-test timeout raised.
Evidence tool, not a check (syzygy-bpyt.8.20). Records, per mutant and for an unmutated
control, the outcome and the duration of each named test, so a kill that came only from a test's timeout can be told from one that came
from an answer. usage: python3 scripts/rule6_timeout_rerun.py TREE RECORD.json OUT.json TIMEOUT_MS TEST_NAME_SUBSTRING ID [ID ...]"""
import hashlib, json, os, subprocess, sys, tempfile, datetime
tree, record, out_path, timeout, watched, ids = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5], sys.argv[6:]
spec = json.load(open(record))
run = lambda cmd: subprocess.run(cmd, capture_output=True, text=True, cwd=tree)
assert not run(['git', 'status', '--porcelain', '--untracked-files=no']).stdout.strip(), 'tree not clean'
head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
me = os.path.abspath(__file__)
out = {'subject': {'commit': head}, 'script': {'path': 'scripts/rule6_timeout_rerun.py', 'sha256': hashlib.sha256(open(me, 'rb').read()).hexdigest()},
       'record': os.path.basename(record), 'recordSha256': hashlib.sha256(open(record, 'rb').read()).hexdigest(), 'testTimeoutMs': timeout, 'watchedTest': watched,
       'ranAt': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'runs': []}
for mid in ['M0-unmutated-control', *ids]:
    m = next(x for x in spec['mutants'] if x['id'] == mid)
    target = os.path.join(tree, m['file'])
    orig = open(target, encoding='utf8').read()
    assert orig.count(m['old']) >= 1, mid
    open(target, 'w', encoding='utf8').write(orig.replace(m['old'], m['new'], 1))
    command = ['npx', 'vitest', 'run', '--project', spec['project'], f'--testTimeout={timeout}', *m['tests']]
    load1 = round(os.getloadavg()[0], 2)
    with tempfile.TemporaryDirectory() as tmp:
        rp = os.path.join(tmp, 'r.json')
        try:
            r = run([*command, '--reporter=json', f'--outputFile.json={rp}'])
        finally:
            run(['git', 'checkout', '--', m['file']])
        report = json.load(open(rp))
    results = [a for t in report['testResults'] for a in t['assertionResults']]
    failed = [a['fullName'] for a in results if a['status'] == 'failed']
    durations = [round(a.get('duration') or 0) for a in results if watched in a['fullName']]
    out['runs'].append({'id': mid, 'old': m['old'], 'new': m['new'], 'command': ' '.join(command), 'load1Before': load1,
                        'totalTests': len(results), 'failedTests': failed, 'watchedTestMs': durations})
    print(mid, len(results), 'failed', len(failed), 'watched ms', durations, 'load1', load1, flush=True)
assert not run(['git', 'status', '--porcelain', '--untracked-files=no']).stdout.strip(), 'tree not restored'
json.dump(out, open(out_path, 'w'), indent=1); open(out_path, 'a').write('\n')
