#!/usr/bin/env python3
"""Per-file and slow-test durations from hosted node-ci runs (syzygy-bpyt.4.31). Evidence tool, not authority.

usage: python3 -I docs/evidence/syzygy-bpyt-4-31/tools/ci_durations.py OUT.json RUN-ID [RUN-ID ...]

For each run, `gh run view RUN-ID --log` and `gh run view RUN-ID --json headSha,conclusion,createdAt` are read. In the test
steps (`npm test`, `npm run test:system`; older logs name every step UNKNOWN STEP, so lines are read from any step) vitest's
default reporter prints one line per test file (its project, path, test count and duration) and, beneath it, one line per test
slower than its 300 ms slowTestThreshold (full name and duration). Every such line is kept verbatim, with its parse; colour codes,
which gh prints as a literal caret and bracket, are removed. A test with no
line of its own took under 300 ms in that run; a file's duration is an upper bound for each of its tests, since a file's tests
run one after another in one worker."""
import json, re, subprocess, sys

ANSI = re.compile(r'(\x1b|\^\[)\[[0-9;]*m')  # gh prints the escape as a literal caret and bracket
STEP = re.compile(r'^[^\t]+\t([^\t]+)\t\ufeff?(\S+) (.*)$')
FILE = re.compile(r'^ ([✓×↓❯]) +(?:(@\S+) +)?(\S+\.test\.ts) \((\d+) tests?(?: \| [^)]*)?\) (\d+)ms')
TEST = re.compile(r'^ {3,}([✓×↓]) (.*?) +(\d+)ms$')
out_path, run_ids = sys.argv[1], sys.argv[2:]
runs = []
for rid in run_ids:
    meta = json.loads(subprocess.run(['gh', 'run', 'view', rid, '--json', 'headSha,conclusion,createdAt,workflowName'], capture_output=True, text=True, check=True).stdout)
    log = subprocess.run(['gh', 'run', 'view', rid, '--log'], capture_output=True, text=True, check=True).stdout
    files, current = [], None
    for raw in log.split('\n'):
        m = STEP.match(ANSI.sub('', raw))
        if not m: continue
        step, text = m.group(1), m.group(3)
        f = FILE.match(text)
        if f:
            current = {'step': step, 'mark': f.group(1), 'project': f.group(2), 'file': f.group(3), 'tests': int(f.group(4)), 'ms': int(f.group(5)), 'line': text.strip(), 'slowTests': []}
            files.append(current)
            continue
        t = TEST.match(text)
        if t and current is not None and current['step'] == step:
            current['slowTests'].append({'mark': t.group(1), 'name': t.group(2), 'ms': int(t.group(3)), 'line': text.strip()})
    runs.append({'runId': int(rid), **meta, 'files': files})
    print(f"run {rid} {meta['headSha'][:8]} {meta['conclusion']}: {len(files)} files, {sum(len(f['slowTests']) for f in files)} slow tests")
open(out_path, 'w', encoding='utf8').write(json.dumps({'tool': 'ci_durations.py', 'runs': runs}, indent=1, ensure_ascii=False) + '\n')
