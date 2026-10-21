#!/usr/bin/env python3
"""Interrupt a project run with a signal and watch what it leaves behind, and for how long.

Usage: interrupt_probe.py <worktree> <tree-commit> <out.json> <private-tmpdir> <signal> <min-copies>

Starts `npx vitest run --project @syzygy/three-surface-poc-app` as the leader of a new
process group with TMPDIR=<private-tmpdir> (emptied first), polls that directory every
0.1 s and, once at least <min-copies> syzygy-poc-surface-fixture-* copies exist, sends
<signal> to that process group (os.killpg of the group this script created, so only this
run's processes are touched; no name or pattern is matched). It then samples, at fixed
offsets, the fixture directories and the other entries in the TMPDIR and the live
processes whose environment names that TMPDIR (read from /proc, read-only). A listing
taken at once may show files that surviving workers still remove, so the record keeps the
whole series.
"""
import json
import os
import pathlib
import shutil
import signal
import subprocess
import sys
import time

WT, COMMIT, OUT, TMP = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve(), pathlib.Path(sys.argv[4]).resolve()
SIGNAL, MIN_COPIES = getattr(signal, 'SIG' + sys.argv[5]), int(sys.argv[6])
OFFSETS = [0, 2, 5, 10, 20, 40, 80]
shutil.rmtree(TMP, ignore_errors=True)
TMP.mkdir(parents=True)


def owners() -> list[int]:
    found = []
    for entry in pathlib.Path('/proc').iterdir():
        if not entry.name.isdigit():
            continue
        try:
            environ = (entry / 'environ').read_bytes().split(b'\0')
        except OSError:
            continue
        if f'TMPDIR={TMP}'.encode() in environ:
            found.append(int(entry.name))
    return found


def sample() -> dict:
    names = sorted(p.name for p in TMP.iterdir())
    fixture = [n for n in names if n.startswith('syzygy-poc-surface-fixture-')]
    return {
        'fixtureCopies': sum(1 for n in fixture if not n.startswith('syzygy-poc-surface-fixture-template-')),
        'fixtureTemplates': sum(1 for n in fixture if n.startswith('syzygy-poc-surface-fixture-template-')),
        'otherSyzygyEntries': sum(1 for n in names if n.startswith('syzygy-') and n not in fixture),
        'liveProcessesNamingThisTmpdir': len(owners()),
    }


started = time.time()
run = subprocess.Popen(['npx', 'vitest', 'run', '--project', '@syzygy/three-surface-poc-app'], cwd=WT, env={**os.environ, 'TMPDIR': str(TMP)}, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
at_signal = None
while run.poll() is None:
    present = sample()
    if present['fixtureCopies'] >= MIN_COPIES:
        at_signal = {'secondsIntoTheRun': round(time.time() - started, 1), **present}
        os.killpg(run.pid, SIGNAL)
        break
    time.sleep(0.1)
signalled = time.time()
series = []
for offset in OFFSETS:
    wait = offset - (time.time() - signalled)
    if wait > 0:
        time.sleep(wait)
    series.append({'secondsAfterSignal': offset, **sample()})
    print(series[-1], flush=True)
run.wait()
OUT.write_text(json.dumps({'tool': 'interrupt_probe.py', 'treeCommit': COMMIT, 'signal': sys.argv[5], 'minCopiesBeforeSignal': MIN_COPIES, 'atSignal': at_signal, 'runFinishedBeforeSignal': at_signal is None, 'series': series}, indent=1) + '\n')
