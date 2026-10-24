#!/usr/bin/env python3
"""Rule-6 probes of the stop and restore paths of scripts/measure_vitest_test_durations.py --profile (syzygy-bpyt.4.13, PR 520
rounds 1 and 2). Evidence tool, not authority.

usage: python3 -I docs/evidence/syzygy-bpyt-4-13/tools/probe_measure_restore.py TREE ROUND0_COMMIT ROUND1_COMMIT OUT.json

Runs each probe against up to three versions of the script: ROUND0_COMMIT's (`round0`) and ROUND1_COMMIT's (`round1`), each copied
to a temporary directory, and TREE's own (`fix`). TREE's tracked files must be clean. Where a probe compares two versions, their
attempts alternate, so load drift falls on both.

Each attempt starts the script in a session of its own, with SIGINT and SIGHUP reset to the default (a shell's background job
inherits SIGINT ignored, and Python then keeps it ignored), except that H starts it with SIGHUP ignored, as `nohup` does. TMPDIR is
a private directory. While the script runs, descendants are found every 50 ms in two ways: by walking /proc parent links from the
script's PID, and as any process whose cwd is inside TREE and which started after the attempt began. The second way catches a child
orphaned before a walk saw it. 3 s after the script exits, a process survives if its PID still has the start time recorded, or if
it started after the attempt began and sits in the process group or session of the script or of a process seen. An attempt passes
only if `git status --porcelain --untracked-files=no` is then empty and nothing survives, and also:

- P0 (fix only): a profiled run of package-reader.test.ts to the end. Exit 0, and a record of 299 tests with a profile row each.
- D1: --file consent-ports.test.ts, whose vitest import line is not the instrumentation anchor. A non-zero exit.
- T, I: SIGTERM, or SIGINT, to the script's PID 3 s after vitest's worker is seen.
- E: SIGTERM to the script's PID D us (busy wait) after the instrumented test-file write is seen, while vitest is being started
  (R2 F2). The write must have been seen.
- G: two SIGTERMs to the script's PID G us apart (busy wait), 0.5 s after vitest's worker is seen (R2 F3 (a)).
- K: a run to the end with os.killpg patched: the first killpg(pid, 0) whose real answer is ESRCH answers "alive" instead, so the
  script's next call, its SIGTERM to the group, meets a group already gone (R2 F3 (b)). Exit 0 and the 299-test record, and the
  patched answer must have been followed by that SIGTERM call, or the attempt did not exercise the race.
- H: SIGHUP to the script's PID 3 s after vitest's worker is seen, with SIGHUP inherited ignored (R2 N7). Exit 0 and the 299-test
  record: an ignored hangup must not end the run.

After each attempt, any survivor is sent SIGKILL by PID, and a dirty tree is restored with `git checkout` of the two instrumented
files, so the next attempt starts clean. The record stores what was found before that cleanup.

`--as-killpg-race SCRIPT ARGS...` is K's wrapper: it runs SCRIPT unchanged under the patch above, logging each killpg call and its
real answer to stderr as a KILLPG line."""
import hashlib, json, os, runpy, signal, subprocess, sys, tempfile, threading, time

if sys.argv[1:2] == ['--as-killpg-race']:
    real_killpg, faked = os.killpg, []
    def killpg(pid, number):
        try: real_killpg(pid, number)
        except ProcessLookupError:
            if int(number) == 0 and not faked:
                faked.append(pid)
                print(f'KILLPG {pid} 0 -> ESRCH, answered alive', file=sys.stderr, flush=True)
                return
            print(f'KILLPG {pid} {int(number)} -> ESRCH', file=sys.stderr, flush=True)
            raise
        print(f'KILLPG {pid} {int(number)} -> ok', file=sys.stderr, flush=True)
    os.killpg = killpg
    sys.argv = sys.argv[2:]
    runpy.run_path(sys.argv[0], run_name='__main__')
    sys.exit(0)

tree, round0, round1, out_path = os.path.realpath(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
TOOL = os.path.realpath(__file__)
SCRIPT = 'scripts/measure_vitest_test_durations.py'
FILE = 'packages/polaris-generation-consent/src/package-reader.test.ts'
KIT = 'packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts'
D1_FILE = 'packages/polaris-generation-consent/src/consent-ports.test.ts'
PROJECT = '@syzygy/polaris-generation-consent'
E_DELAYS_US, G_GAPS_US = (800, 1000, 1200, 1500, 1800, 2200), (0, 30, 60, 100, 150, 200, 300, 500, 1000)
E_REPEATS, G_REPEATS = 3, 4
TICKS = os.sysconf('SC_CLK_TCK')
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
status = lambda: git('status', '--porcelain', '--untracked-files=no')
if status(): sys.exit('tracked files not clean')

def stat(pid):
    """ppid, pgid, sid and start time of a live process, or None."""
    try: text = open(f'/proc/{pid}/stat').read()
    except OSError: return None
    f = text[text.rindex(')') + 2:].split()
    return {'ppid': int(f[1]), 'pgid': int(f[2]), 'sid': int(f[3]), 'start': int(f[19])}
def cmdline(pid):
    try: return open(f'/proc/{pid}/cmdline', 'rb').read().replace(b'\0', b' ').decode(errors='replace').strip()[:120]
    except OSError: return None
def cwd(pid):
    try: return os.readlink(f'/proc/{pid}/cwd')
    except OSError: return None
def procs():
    found = {}
    for p in os.listdir('/proc'):
        if p.isdigit() and (s := stat(int(p))) is not None: found[int(p)] = s
    return found
def now_ticks(): return int(float(open('/proc/uptime').read().split()[0]) * TICKS)
def walk(root, seen, began):
    ps = procs()
    children = {}
    for pid, s in ps.items(): children.setdefault(s['ppid'], []).append(pid)
    todo = [root]
    while todo:
        for child in children.get(todo.pop(), []):
            if child not in seen: seen[child] = {**ps[child], 'cmdline': cmdline(child)}
            todo.append(child)
    for pid, s in ps.items():
        if pid not in seen and pid != os.getpid() and s['start'] >= began and (d := cwd(pid)) and (d == tree or d.startswith(tree + '/')):
            seen[pid] = {**s, 'cmdline': cmdline(pid), 'byCwd': True}
def vitest_started(seen): return sum('vitest' in (d['cmdline'] or '') for d in seen.values()) >= 2
def busy(us):
    end = time.perf_counter() + us / 1e6
    while time.perf_counter() < end: pass
def send(pid, number):
    try: os.kill(pid, number)
    except ProcessLookupError: pass

def attempt(probe, version, script, param=None):
    with tempfile.TemporaryDirectory(prefix='laneb-413-probe-') as tmp:
        out = os.path.join(tmp, 'measure-out.json')
        command = ['python3', '-I', script, '.', '--project', PROJECT, '--mode', 'alone', '--runs', '1', '--out', out, '--profile',
                   '--file', D1_FILE if probe == 'D1' else FILE]
        if probe == 'K': command = ['python3', '-I', TOOL, '--as-killpg-race', script, *command[3:]]
        def pre():
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            signal.signal(signal.SIGHUP, signal.SIG_IGN if probe == 'H' else signal.SIG_DFL)
        began = now_ticks() - 1
        proc = subprocess.Popen(command, cwd=tree, start_new_session=True, env={**os.environ, 'TMPDIR': tmp}, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, preexec_fn=pre)
        chunks = []
        reader = threading.Thread(target=lambda: chunks.append(proc.stdout.read()), daemon=True)
        reader.start()
        seen, t0, sent = {}, time.monotonic(), None
        if probe in ('T', 'I', 'G', 'H'):
            while time.monotonic() - t0 < 120 and proc.poll() is None and not vitest_started(seen):
                walk(proc.pid, seen, began); time.sleep(0.05)
            settle = time.monotonic() + (0.5 if probe == 'G' else 3)
            while time.monotonic() < settle and proc.poll() is None: walk(proc.pid, seen, began); time.sleep(0.05)
            if vitest_started(seen) and proc.poll() is None:
                if probe == 'G':
                    send(proc.pid, signal.SIGTERM); busy(param); send(proc.pid, signal.SIGTERM)
                else: send(proc.pid, {'T': signal.SIGTERM, 'I': signal.SIGINT, 'H': signal.SIGHUP}[probe])
                sent = round(time.monotonic() - t0, 3)
        elif probe == 'E':
            full = os.path.join(tree, FILE)
            base, deadline = os.stat(full).st_mtime_ns, time.monotonic() + 60
            while time.monotonic() < deadline and proc.poll() is None and os.stat(full).st_mtime_ns == base: pass
            if os.stat(full).st_mtime_ns != base and proc.poll() is None:
                busy(param); send(proc.pid, signal.SIGTERM)
                sent = round(time.monotonic() - t0, 3)
        while proc.poll() is None and time.monotonic() - t0 < 900:
            walk(proc.pid, seen, began); time.sleep(0.05)
        if proc.poll() is None: proc.kill(); proc.wait()
        exited = round(time.monotonic() - t0, 3)
        time.sleep(3)
        reader.join(5)
        output = (chunks[0] if chunks else b'').decode(errors='replace')
        tree_after = status()
        groups = {d['pgid'] for d in seen.values()} | {d['sid'] for d in seen.values()} | {proc.pid}
        survivors = {}
        for pid, s in procs().items():
            if pid == os.getpid(): continue
            if (pid in seen and seen[pid]['start'] == s['start']) or ((s['pgid'] in groups or s['sid'] in groups) and s['start'] >= began):
                survivors[str(pid)] = cmdline(pid)
        for pid in survivors:
            try: os.kill(int(pid), signal.SIGKILL)
            except ProcessLookupError: pass
        if tree_after: subprocess.run(['git', 'checkout', '--', KIT, FILE], cwd=tree, check=True)
        record = json.load(open(out)) if os.path.exists(out) else None
    rows = record['runs'][0] if record and record.get('runs') else {}
    result = {'probe': probe, 'script': version, 'param': param, 'command': ' '.join(command).replace(tmp, '<tmp>').replace(old_dir, '<old>').replace(tree + '/', ''),
              'signalSentAtSeconds': sent, 'scriptExitedAtSeconds': exited, 'exitCode': proc.returncode,
              'descendantsSeen': len(seen), 'seenOnlyByCwd': sum(1 for d in seen.values() if d.get('byCwd')),
              'treeAfterExit': tree_after, 'survivors': survivors, 'recordTests': rows.get('fileTests'),
              'recordProfileRows': len(rows.get('profile') or []) if rows else None, 'outputTail': output[-400:]}
    ok = not tree_after and not survivors
    if probe in ('E', 'G', 'T', 'I', 'H'):
        result['exercised'] = sent is not None
    if probe == 'K':
        calls = [line for line in output.split('\n') if line.startswith('KILLPG ')]
        at = next((i for i, line in enumerate(calls) if line.endswith('answered alive')), None)
        result['killpgCalls'] = calls
        result['exercised'] = at is not None and at + 1 < len(calls) and calls[at + 1].split()[2] == str(int(signal.SIGTERM))
    if probe in ('P0', 'K', 'H'):
        ok = ok and proc.returncode == 0 and result['recordTests'] == 299 and result['recordProfileRows'] == 299
    if probe == 'D1': ok = ok and proc.returncode != 0
    result['passes'] = ok and result.get('exercised', True)
    print(f"{version:>6} {probe}{'' if param is None else ' ' + str(param)}: exit {proc.returncode}, tree "
          f"{'clean' if not tree_after else 'DIRTY ' + tree_after.strip()!r}, {len(survivors)} survivors of {len(seen)} seen, "
          f"exercised {result.get('exercised', '-')} -> {'pass' if result['passes'] else 'FAIL'}", flush=True)
    if status(): sys.exit('tree not restored after an attempt')
    return result

sha = lambda path: hashlib.sha256(open(path, 'rb').read()).hexdigest()
PLAN = [('P0', ('fix',), [None]), ('D1', ('round0', 'round1', 'fix'), [None]), ('T', ('round0', 'round1', 'fix'), [None]),
        ('I', ('round0', 'round1', 'fix'), [None]), ('E', ('round1', 'fix'), [d for _ in range(E_REPEATS) for d in E_DELAYS_US]),
        ('G', ('round1', 'fix'), [g for _ in range(G_REPEATS) for g in G_GAPS_US]), ('K', ('round1', 'fix'), [None]),
        ('H', ('round1', 'fix'), [None])]
EXPECTED = {'P0': {'fix': 'pass'}, 'D1': {'round0': 'fail', 'round1': 'pass', 'fix': 'pass'},
            'T': {'round0': 'fail', 'round1': 'pass', 'fix': 'pass'}, 'I': {'round0': 'fail', 'round1': 'pass', 'fix': 'pass'},
            'E': {'round1': 'fail', 'fix': 'pass'}, 'G': {'round1': 'fail', 'fix': 'pass'}, 'K': {'round1': 'fail', 'fix': 'pass'},
            'H': {'round1': 'fail', 'fix': 'pass'}}
results = []
with tempfile.TemporaryDirectory(prefix='laneb-413-old-') as old_dir:
    paths, scripts = {'fix': os.path.join(tree, SCRIPT)}, []
    for version, commit in (('round0', round0), ('round1', round1)):
        paths[version] = os.path.join(old_dir, version, 'measure_vitest_test_durations.py')
        os.mkdir(os.path.dirname(paths[version]))
        open(paths[version], 'wb').write(subprocess.run(['git', 'show', f'{commit}:{SCRIPT}'], cwd=tree, capture_output=True, check=True).stdout)
    for version, commit in (('round0', round0), ('round1', round1), ('fix', 'HEAD')):
        scripts.append({'version': version, 'commit': git('rev-parse', commit).strip(), 'path': SCRIPT, 'sha256': sha(paths[version])})
    for probe, versions, params in PLAN:
        for param in params:
            for version in versions: results.append(attempt(probe, version, paths[version], param))
summary = {}
for probe, versions, _ in PLAN:
    for version in versions:
        mine = [r for r in results if r['probe'] == probe and r['script'] == version]
        passed = sum(r['passes'] for r in mine)
        expected = EXPECTED[probe][version]
        summary.setdefault(probe, {})[version] = {
            'attempts': len(mine), 'passed': passed, 'failed': len(mine) - passed, 'expected': expected,
            'asExpected': passed == len(mine) if expected == 'pass' else passed < len(mine)}
out = {'schema': 'measure-restore-probes/2', 'bead': 'syzygy-bpyt.4.13',
       'text': 'Evidence record, not authority: rule-6 probes of the stop and restore paths of scripts/measure_vitest_test_durations.py --profile, run against the script before the PR 520 round-1 fix (round0), before the round-2 fix (round1) and after it (fix). Generated by the tool named here; do not edit.',
       'tool': {'path': 'docs/evidence/syzygy-bpyt-4-13/tools/probe_measure_restore.py', 'sha256': sha(TOOL)},
       'commit': git('rev-parse', 'HEAD').strip(), 'host': {'cores': os.cpu_count(), 'python': sys.version.split()[0]}, 'scripts': scripts,
       'parameters': {'E': {'delaysUs': list(E_DELAYS_US), 'repeats': E_REPEATS}, 'G': {'gapsUs': list(G_GAPS_US), 'repeats': G_REPEATS}},
       'predicate': 'an attempt passes iff, 3 s after the script exits, git status --porcelain --untracked-files=no is empty and no process survives; P0, K and H also need exit 0 and a 299-test record with 299 profile rows; D1 also needs a non-zero exit; E, G, T, I, H and K also need the probe to have exercised its case (a signal sent while the script ran; for K, the patched answer followed by the script\'s SIGTERM call). Expected "fail" means at least one attempt fails; expected "pass" means every attempt passes.',
       'summary': summary, 'allAsExpected': all(v['asExpected'] for p in summary.values() for v in p.values()), 'results': results}
open(out_path, 'w', encoding='utf8').write(json.dumps(out, indent=1) + '\n')
print(json.dumps({p: {v: f"{s['passed']}/{s['attempts']} passed, expected {s['expected']}, as expected {s['asExpected']}" for v, s in vs.items()} for p, vs in summary.items()}, indent=1))
print('allAsExpected', out['allAsExpected'])
