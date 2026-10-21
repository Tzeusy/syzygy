#!/usr/bin/env python3
"""Show that route-capture.mjs leaves no temporary directory behind (round 1, N4d).

Usage: route_capture_leak_check.py <built-tree> <out.json>

The capture runs with TMPDIR pointing at an empty private directory and a fresh
fixture-repository path outside it, so everything the script creates in the
system temporary directory lands where it can be listed afterwards. The script
as it is must leave that directory empty. As the rule-6 mutant, a copy of the
script without the `rmSync(made.repoRoot ...)` line must leave exactly one
fixture directory (`syzygy-poc-surface-fixture-*`). The tree needs a built
apps/three-surface-poc and packages/cap1-daemon.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

tree, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
script = Path(__file__).resolve().parent / 'route-capture.mjs'
LINE = "  rmSync(made.repoRoot, { recursive: true, force: true });\n"
text = script.read_text(encoding='utf-8')
assert text.count(LINE) == 1, 'the cleanup line must occur once'


def run(label: str, source: str) -> dict:
    work = Path(tempfile.mkdtemp(prefix='zz-leak-check-'))
    try:
        tmp, fixture_home = work / 'tmp', work / 'fixture'
        tmp.mkdir()
        fixture_home.mkdir()
        copy = work / 'route-capture.mjs'
        copy.write_text(source, encoding='utf-8')
        proc = subprocess.run(['node', str(copy), str(tree), str(work / 'capture.json'), str(fixture_home / 'repo')], capture_output=True, text=True, env={**os.environ, 'TMPDIR': str(tmp)})
        left = sorted(p.name.rsplit('-', 1)[0] + '-<random>' for p in tmp.iterdir())
        return {'case': label, 'exit': proc.returncode, 'lastStdoutLine': proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else None,
                'entriesLeftInTheTemporaryDirectory': left}
    finally:
        shutil.rmtree(work, ignore_errors=True)


real = run('script as committed', text)
mutant = run('mutant: cleanup line removed', text.replace(LINE, ''))
holds = real['exit'] == 0 and real['entriesLeftInTheTemporaryDirectory'] == [] and mutant['exit'] == 0 and mutant['entriesLeftInTheTemporaryDirectory'] == ['syzygy-poc-surface-fixture-<random>']
commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
record = {'tool': 'route_capture_leak_check.py', 'toolSha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'subject': 'route-capture.mjs', 'subjectSha256': hashlib.sha256(script.read_bytes()).hexdigest(), 'treeCommit': commit,
          'mutantOld': LINE, 'mutantNew': '', 'cases': [real, mutant], 'holds': holds}
out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
print(f"holds={holds} real left={real['entriesLeftInTheTemporaryDirectory']} mutant left={mutant['entriesLeftInTheTemporaryDirectory']}")
sys.exit(0 if holds else 1)
