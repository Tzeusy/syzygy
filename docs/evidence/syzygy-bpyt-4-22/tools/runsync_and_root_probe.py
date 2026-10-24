#!/usr/bin/env python3
"""Rule-6 evidence for syzygy-bpyt.4.22 and syzygy-bpyt.4.25, two system tests in packages/cap1-system. Evidence tool, not authority.

usage: python3 -I docs/evidence/syzygy-bpyt-4-22/tools/runsync_and_root_probe.py TREE BASE_COMMIT OUT.json

TREE must be a checkout with `npm ci` run and its tracked files clean. BASE_COMMIT is the commit the branch was cut from. The suite
runs the built daemon, so the tool runs `npm run build` first and again after each mutant. Every run is `npx vitest run --config
packages/cap1-system/vitest.config.ts` with the JSON reporter, in a session of its own. The cases:

- base, head: both touched files as at BASE_COMMIT, then as at HEAD, unmutated. Each must exit 0 with no failed test. The record
  keeps every test's title and status, and compares the two populations.
- R5, R9: the argv-reader mutants of docs/evidence/syzygy-bpyt-8-2/mutants/. Each edit's `old` and `new` are read from that
  record, whose sha256 is stored. The mutant is applied to the source and built, then daemon-entry-unchanged.system.test.ts runs at
  HEAD. A mutant that does not type-check still counts if `tsc -b` emitted it: the build's exit code and type errors are recorded,
  and each edit's `new` fragment, whitespace collapsed, must be in the emitted dist file. It passes when vitest exits non-zero within 300 s, at least one row fails with ETIMEDOUT (runSync's timeout) in its failure
  message, and every failed row took under the timeout plus 5 s. While it runs, `ss -ltnpH` is sampled every 0.25 s: no socket
  may listen on port 7477, and the record lists the ports that the run's own processes listened on. 3 s after vitest exits, no
  process of the run may survive. Survivors are found by walking /proc parent links from vitest's PID and by vitest's session.
- root-shim, root-shim-base: state-dir.system.test.ts, filtered with -t to the mode-000 row, with NODE_OPTIONS importing a shim
  that makes process.getuid() return 0. At HEAD the row must be skipped. At BASE_COMMIT, which has no skipIf, it must run and
  pass. This checks the skip's condition only. The process is not root, so chmod 000 still blocks it, and the run says nothing
  about the row under a real root.
- root-control: the same filter at HEAD without the shim. The row must run and pass.

Each case writes back the files it changed, and rebuilds after a mutant, however it ends short of a SIGKILL of the tool. Each
case's record stores its command, its edits as old and new fragments, every test's status and duration, and its findings."""
import hashlib, json, os, re, signal, subprocess, sys, tempfile, time

tree, base_commit, out_path = os.path.realpath(sys.argv[1]), sys.argv[2], sys.argv[3]
ENTRY_TEST = 'packages/cap1-system/src/daemon-entry-unchanged.system.test.ts'
STATE_TEST = 'packages/cap1-system/src/state-dir.system.test.ts'
MUTANTS = 'docs/evidence/syzygy-bpyt-8-2/mutants'
ROW = 'rejects an unreadable state-dir path as named invalid before writes or a listener'
TIMEOUT_MS, DEADLINE_S, PORT = 20_000, 300, '7477'
git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
status = lambda: git('status', '--porcelain', '--untracked-files=no')
sha = lambda data: hashlib.sha256(data).hexdigest()
if status(): sys.exit('tracked files not clean')
head = git('rev-parse', 'HEAD').strip()
base = git('rev-parse', base_commit).strip()
at = lambda commit, path: subprocess.run(['git', 'show', f'{commit}:{path}'], cwd=tree, capture_output=True, check=True).stdout

def build(allow_errors=False):
    """`npm run build`; with allow_errors, a type error is returned rather than fatal (tsc -b still emits)."""
    done = subprocess.run(['npm', 'run', 'build'], cwd=tree, capture_output=True, text=True)
    errors = [line for line in (done.stdout + done.stderr).split('\n') if ': error TS' in line]
    if done.returncode and not allow_errors: sys.exit(f'npm run build exited {done.returncode}:\n{done.stdout[-2000:]}{done.stderr[-2000:]}')
    return {'exitCode': done.returncode, 'typeErrors': errors}

def stat(pid):
    try: text = open(f'/proc/{pid}/stat').read()
    except OSError: return None
    f = text[text.rindex(')') + 2:].split()
    return {'ppid': int(f[1]), 'sid': int(f[3]), 'start': int(f[19])}
def procs():
    found = {}
    for p in os.listdir('/proc'):
        if p.isdigit() and (s := stat(int(p))) is not None: found[int(p)] = s
    return found
def cmdline(pid):
    try: return open(f'/proc/{pid}/cmdline', 'rb').read().replace(b'\0', b' ').decode(errors='replace').strip()[:120]
    except OSError: return None
def walk(root, seen):
    ps = procs()
    children = {}
    for pid, s in ps.items(): children.setdefault(s['ppid'], []).append(pid)
    todo = [root]
    while todo:
        for child in children.get(todo.pop(), []):
            if child not in seen: seen[child] = {**ps[child], 'cmdline': cmdline(child)}
            todo.append(child)
def listeners():
    """(port, pids) for every listening TCP socket ss shows."""
    out = subprocess.run(['ss', '-ltnpH'], capture_output=True, text=True).stdout
    found = []
    for line in out.split('\n'):
        fields = line.split()
        if len(fields) >= 4: found.append((fields[3].rsplit(':', 1)[1], [int(p) for p in re.findall(r'pid=(\d+)', line)]))
    return found

def vitest(name, filters, extra_args=(), env_extra=None):
    with tempfile.TemporaryDirectory(prefix='laneb-422-') as tmp:
        report = os.path.join(tmp, 'report.json')
        command = ['npx', 'vitest', 'run', '--config', 'packages/cap1-system/vitest.config.ts', *filters, *extra_args,
                   '--reporter=json', f'--outputFile={report}']
        before = [port for port, _ in listeners() if port == PORT]
        proc = subprocess.Popen(command, cwd=tree, start_new_session=True, env={**os.environ, 'TMPDIR': tmp, **(env_extra or {})},
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        seen, t0, on_port, own_ports, samples, killed = {}, time.monotonic(), [], set(), 0, False
        while proc.poll() is None:
            if time.monotonic() - t0 > DEADLINE_S:
                os.killpg(proc.pid, signal.SIGKILL); killed = True; proc.wait(); break
            walk(proc.pid, seen)
            for port, pids in listeners():
                if port == PORT: on_port.append({'t': round(time.monotonic() - t0, 2), 'pids': pids})
                if set(pids) & (set(seen) | {proc.pid}): own_ports.add(port)
            samples += 1
            time.sleep(0.25)
        wall = round(time.monotonic() - t0, 1)
        time.sleep(3)
        survivors = {}
        for pid, s in procs().items():
            if (pid in seen and seen[pid]['start'] == s['start']) or s['sid'] == proc.pid:
                survivors[str(pid)] = cmdline(pid)
        for pid in survivors:
            try: os.kill(int(pid), signal.SIGKILL)
            except ProcessLookupError: pass
        data = json.load(open(report)) if os.path.exists(report) else {}
    tests = [{'name': a['fullName'], 'status': a['status'], 'durationMs': None if a.get('duration') is None else round(a['duration']),
              'failure': (a.get('failureMessages') or [''])[0][:300] or None}
             for s in data.get('testResults', []) for a in s.get('assertionResults', [])]
    run = {'case': name, 'command': ' '.join(command).replace(tmp, '<tmp>'), 'env': env_extra or {}, 'exitCode': proc.returncode,
           'wallSeconds': wall, 'killedAtDeadline': killed, 'port7477ListenersBefore': len(before), 'samples': samples,
           'port7477ListenersSeen': on_port, 'portsTheRunListenedOn': sorted(own_ports, key=int), 'processesSeen': len(seen),
           'survivors': survivors, 'tests': tests}
    print(f"{name}: exit {proc.returncode}, {wall} s, {len(tests)} tests ({sum(t['status'] == 'failed' for t in tests)} failed), "
          f"7477 seen {len(on_port)} of {samples} samples, own ports {run['portsTheRunListenedOn']}, {len(survivors)} survivors", flush=True)
    return run

def with_files(contents, body):
    """Writes {path: bytes} into TREE, runs body, writes the original bytes back."""
    originals = {path: open(os.path.join(tree, path), 'rb').read() for path in contents}
    try:
        for path, data in contents.items(): open(os.path.join(tree, path), 'wb').write(data)
        return body()
    finally:
        for path, data in originals.items(): open(os.path.join(tree, path), 'wb').write(data)

def target(run):
    rows = [t for t in run['tests'] if t['name'].endswith(ROW)]
    return rows[0]['status'] if len(rows) == 1 else f'{len(rows)} rows'

build()
runs = []
runs.append(with_files({ENTRY_TEST: at(base, ENTRY_TEST), STATE_TEST: at(base, STATE_TEST)},
                       lambda: vitest('base', ['daemon-entry-unchanged', 'state-dir.system'])))
runs.append(vitest('head', ['daemon-entry-unchanged', 'state-dir.system']))
for runner in runs: runner['passes'] = runner['exitCode'] == 0 and not any(t['status'] == 'failed' for t in runner['tests'])
mutants = []
for mid in ('R5-positional-taken-when-refused', 'R9-missing-value-unchecked'):
    record_path = f'{MUTANTS}/{mid}.json'
    raw = open(os.path.join(tree, record_path), 'rb').read()
    edits = json.loads(raw)['edits']
    contents = {}
    for edit in edits:
        text = contents.get(edit['file']) or open(os.path.join(tree, edit['file']), 'rb').read()
        if text.count(edit['old'].encode()) != 1: sys.exit(f"{mid}: the old fragment occurs {text.count(edit['old'].encode())} times")
        contents[edit['file']] = text.replace(edit['old'].encode(), edit['new'].encode())
    def mutated():
        built = build(allow_errors=True)
        squash = lambda text: re.sub(r'\s+', ' ', text)
        carried = [squash(edit['new']) in squash(open(os.path.join(tree, edit['file'].replace('/src/', '/dist/')[:-3] + '.js'), encoding='utf8').read())
                   for edit in edits]
        if not all(carried): sys.exit(f'{mid}: the build did not carry the mutant into dist')
        return {**vitest(mid.split('-')[0], ['daemon-entry-unchanged']), 'build': built, 'distCarriesMutant': True}
    try: run = with_files(contents, mutated)
    finally: build()
    failed = [t for t in run['tests'] if t['status'] == 'failed']
    run.update({'mutantRecord': {'path': record_path, 'sha256': sha(raw)}, 'edits': edits,
                'failedRows': len(failed), 'timedOutRows': sum('ETIMEDOUT' in (t['failure'] or '') for t in failed),
                'slowestFailedRowMs': max((t['durationMs'] or 0 for t in failed), default=None)})
    run['passes'] = (run['exitCode'] not in (0, None) and not run['killedAtDeadline'] and run['timedOutRows'] >= 1
                     and all((t['durationMs'] or 0) < TIMEOUT_MS + 5000 for t in failed) and not run['port7477ListenersSeen']
                     and run['port7477ListenersBefore'] == 0 and not run['survivors'])
    mutants.append(run)
with tempfile.TemporaryDirectory(prefix='laneb-422-shim-') as shim_dir:
    shim = os.path.join(shim_dir, 'getuid-zero.mjs')
    open(shim, 'w', encoding='utf8').write('process.getuid = () => 0;\n')
    shim_env = {'NODE_OPTIONS': f'--import=file://{shim}'}
    roots = [vitest('root-shim', ['state-dir.system'], ['-t', ROW], shim_env),
             with_files({STATE_TEST: at(base, STATE_TEST)}, lambda: vitest('root-shim-base', ['state-dir.system'], ['-t', ROW], shim_env)),
             vitest('root-control', ['state-dir.system'], ['-t', ROW])]
for run, wanted in zip(roots, (('skipped', 'pending'), ('passed',), ('passed',))):
    run['env'] = {'NODE_OPTIONS': '--import=file://<tmp>/getuid-zero.mjs'} if run['env'] else {}
    run['row'] = target(run)
    run['passes'] = run['exitCode'] == 0 and run['row'] in wanted
if status(): sys.exit('tree not restored')
titles = lambda run: [(t['name'], t['status']) for t in run['tests']]
out = {'schema': 'runsync-and-root-probe/1', 'beads': ['syzygy-bpyt.4.22', 'syzygy-bpyt.4.25'],
       'text': 'Evidence record, not authority: the unmutated runs of the two touched system tests at the base commit and at HEAD, the R5 and R9 argv-reader mutants against daemon-entry-unchanged.system.test.ts, and a getuid shim against the mode-000 row of state-dir.system.test.ts. Generated by the tool named here; do not edit.',
       'tool': {'path': 'docs/evidence/syzygy-bpyt-4-22/tools/runsync_and_root_probe.py', 'sha256': sha(open(os.path.realpath(__file__), 'rb').read())},
       'commit': head, 'baseCommit': base,
       'files': {path: {'head': sha(at(head, path)), 'base': sha(at(base, path))} for path in (ENTRY_TEST, STATE_TEST)},
       'host': {'cores': os.cpu_count(), 'node': subprocess.run(['node', '--version'], capture_output=True, text=True).stdout.strip()},
       'runSyncTimeoutMs': TIMEOUT_MS,
       'populations': {'baseTests': len(runs[0]['tests']), 'headTests': len(runs[1]['tests']),
                       'sameTitlesAndStatuses': titles(runs[0]) == titles(runs[1])},
       'unmutated': runs, 'mutants': mutants, 'rootShim': roots}
out['allPass'] = all(r['passes'] for r in runs + mutants + roots) and out['populations']['sameTitlesAndStatuses']
open(out_path, 'w', encoding='utf8').write(json.dumps(out, indent=1) + '\n')
print(json.dumps({r['case']: r['passes'] for r in runs + mutants + roots}), 'populations', out['populations'], 'allPass', out['allPass'])
