#!/usr/bin/env python3
"""Rule-6 probes of the restore paths of scripts/measure_vitest_test_durations.py --profile (syzygy-bpyt.4.13, PR 520 R1 F1).
Evidence tool, not authority.

usage: python3 -I docs/evidence/syzygy-bpyt-4-13/tools/probe_measure_restore.py TREE OLD_COMMIT OUT.json

Runs each probe against two versions of the script: OLD_COMMIT's, copied to a temporary directory, and TREE's own. TREE's tracked
files must be clean. Each probe passes only when, 3 s after the script exits, `git status --porcelain --untracked-files=no` is empty
and no descendant survives. A descendant is any process found by walking /proc parent links from the script's PID while it ran
(the last walk before the signal, and every walk after it until the script exited), or any process in one of their process groups;
a process counts as surviving only if its PID still has the start time recorded. The script runs in a session of its own, with
SIGINT's disposition reset to the default: a shell's background job inherits SIGINT ignored, and Python then keeps it ignored.

- P0: a profiled run of package-reader.test.ts to the end (TREE's script only: the control that the fix keeps the normal path).
  It must also exit 0 and write a record of 299 tests with a profile row for each.
- D1: --profile with a --file whose vitest import line is not the instrumentation anchor (consent-ports.test.ts). It must exit
  non-zero.
- T: SIGTERM to the script's PID once the testkit is instrumented and vitest has started.
- I: SIGINT to the script's PID only, at the same point.

After each probe, any survivor is sent SIGKILL by PID, and a dirty tree is restored with `git checkout` of the two instrumented
files, so the next probe starts clean. The record stores what was found before that cleanup."""
import hashlib, json, os, signal, subprocess, sys, tempfile, time

tree, old_commit, out_path = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3]
SCRIPT = 'scripts/measure_vitest_test_durations.py'
FILE = 'packages/polaris-generation-consent/src/package-reader.test.ts'
KIT = 'packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts'
D1_FILE = 'packages/polaris-generation-consent/src/consent-ports.test.ts'
PROJECT = '@syzygy/polaris-generation-consent'
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
status = lambda: git('status', '--porcelain', '--untracked-files=no')
if status(): sys.exit('tracked files not clean')

def stat(pid):
    """(ppid, pgid, start time) of a live process, or None."""
    try: text = open(f'/proc/{pid}/stat').read()
    except OSError: return None
    fields = text[text.rindex(')') + 2:].split()
    return int(fields[1]), int(fields[2]), int(fields[19])
def cmdline(pid):
    try: return open(f'/proc/{pid}/cmdline', 'rb').read().replace(b'\0', b' ').decode(errors='replace').strip()[:200]
    except OSError: return None
def all_procs():
    found = {}
    for p in os.listdir('/proc'):
        if p.isdigit() and (s := stat(int(p))) is not None: found[int(p)] = s
    return found
def walk(root, seen):
    procs = all_procs()
    children = {}
    for pid, (ppid, _, _) in procs.items(): children.setdefault(ppid, []).append(pid)
    todo = [root]
    while todo:
        for child in children.get(todo.pop(), []):
            if child not in seen: seen[child] = {'start': procs[child][2], 'pgid': procs[child][1], 'cmdline': cmdline(child)}
            todo.append(child)

def probe(version, script, pid_name, args, signal_number=None):
    with tempfile.TemporaryDirectory(prefix='laneb-413-probe-') as tmp:
        out = os.path.join(tmp, 'measure-out.json')
        command = ['python3', '-I', script, '.', '--project', PROJECT, '--mode', 'alone', '--runs', '1', '--out', out, '--profile', *args]
        proc = subprocess.Popen(command, cwd=tree, start_new_session=True, env={**os.environ, 'TMPDIR': tmp}, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_DFL))
        seen, t0, sent_at, instrumented = {}, time.monotonic(), None, None
        if signal_number is not None:
            while time.monotonic() - t0 < 90 and proc.poll() is None and KIT not in status(): time.sleep(0.2)
            instrumented = round(time.monotonic() - t0, 1) if KIT in status() else None
            while time.monotonic() - t0 < 90 and proc.poll() is None:   # vitest has started its worker: a node process three levels down
                walk(proc.pid, seen)
                if sum('vitest' in (d['cmdline'] or '') for d in seen.values()) >= 2: break
                time.sleep(0.2)
            time.sleep(3)
            walk(proc.pid, seen)
            sent_at = round(time.monotonic() - t0, 1)
            os.kill(proc.pid, signal_number)
        deadline = time.monotonic() + 600
        while proc.poll() is None and time.monotonic() < deadline:
            walk(proc.pid, seen)
            time.sleep(0.2)
        if proc.poll() is None: proc.kill()
        output = proc.communicate()[0]
        time.sleep(3)
        tree_after = status()
        groups = {d['pgid'] for d in seen.values()} | {proc.pid}
        survivors = {}
        for pid, (ppid, pgid, start) in all_procs().items():
            if (pid in seen and seen[pid]['start'] == start) or pgid in groups: survivors[pid] = cmdline(pid)
        for pid in survivors:
            try: os.kill(pid, signal.SIGKILL)
            except ProcessLookupError: pass
        if tree_after: subprocess.run(['git', 'checkout', '--', KIT, FILE], cwd=tree, check=True)
        record = json.load(open(out)) if os.path.exists(out) else None
    result = {'probe': pid_name, 'script': version, 'command': ' '.join(command).replace(tmp, '<tmp>'), 'signal': signal.Signals(signal_number).name if signal_number else None,
              'instrumentedAfterSeconds': instrumented, 'signalSentAtSeconds': sent_at, 'descendantsSeen': len(seen), 'exitCode': proc.returncode,
              'outputTail': output[-600:], 'treeAfterExit': tree_after, 'survivors': {str(k): v for k, v in survivors.items()}}
    ok = not tree_after and not survivors
    if pid_name == 'P0':
        rows = record['runs'][0] if record else {}
        result['recordTests'], result['recordProfileRows'] = rows.get('fileTests'), len(rows.get('profile') or [])
        ok = ok and proc.returncode == 0 and result['recordTests'] == 299 and result['recordProfileRows'] == 299
    if pid_name == 'D1': ok = ok and proc.returncode != 0
    result['passes'] = ok
    print(f"{version:>3} {pid_name}: exit {proc.returncode}, tree {'clean' if not tree_after else 'DIRTY ' + tree_after.strip()!r}, "
          f"{len(survivors)} survivors of {len(seen)} seen -> {'pass' if ok else 'FAIL'}", flush=True)
    if status(): sys.exit('tree not restored after a probe')
    return result

sha = lambda path: hashlib.sha256(open(path, 'rb').read()).hexdigest()
results = []
with tempfile.TemporaryDirectory(prefix='laneb-413-old-') as old_dir:
    old_script = os.path.join(old_dir, 'measure_vitest_test_durations.py')
    open(old_script, 'w', encoding='utf8').write(subprocess.run(['git', 'show', f'{old_commit}:{SCRIPT}'], cwd=tree, capture_output=True, text=True, check=True).stdout)
    versions = [('old', old_script, git('rev-parse', old_commit).strip()), ('new', os.path.join(tree, SCRIPT), git('rev-parse', 'HEAD').strip())]
    scripts = [{'version': v, 'commit': c, 'path': SCRIPT, 'sha256': sha(p)} for v, p, c in versions]
    results.append(probe('new', versions[1][1], 'P0', ['--file', FILE]))
    for version, path, _ in versions:
        results.append(probe(version, path, 'D1', ['--file', D1_FILE]))
        results.append(probe(version, path, 'T', ['--file', FILE], signal.SIGTERM))
        results.append(probe(version, path, 'I', ['--file', FILE], signal.SIGINT))
out = {'schema': 'measure-restore-probes/1', 'bead': 'syzygy-bpyt.4.13',
       'text': 'Evidence record, not authority: rule-6 probes of the restore paths of scripts/measure_vitest_test_durations.py --profile, run against the script before and after the PR 520 round-1 F1 fix. Generated by the tool named here; do not edit.',
       'tool': {'path': 'docs/evidence/syzygy-bpyt-4-13/tools/probe_measure_restore.py', 'sha256': sha(__file__)},
       'commit': git('rev-parse', 'HEAD').strip(), 'scripts': scripts,
       'predicate': 'passes iff, 3 s after the script exits, git status --porcelain --untracked-files=no is empty and no descendant survives; P0 also needs exit 0 and a 299-test record with 299 profile rows; D1 also needs a non-zero exit',
       'results': results,
       'summary': {v: {r['probe']: r['passes'] for r in results if r['script'] == v} for v in ('old', 'new')}}
open(out_path, 'w', encoding='utf8').write(json.dumps(out, indent=1) + '\n')
print(json.dumps(out['summary']))
