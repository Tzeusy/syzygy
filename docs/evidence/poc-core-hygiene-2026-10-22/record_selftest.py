#!/usr/bin/env python3
"""Run export_census.py --selftest and keep its output with the subject's identity.

Usage: record_selftest.py <tool> <tree> <out.txt>

The first three lines name the tool's sha256, the tree's commit and the command;
the rest is the selftest output unchanged, ending with its summary line. The
exit code of the selftest is this script's exit code.
"""
import hashlib
import subprocess
import sys
from pathlib import Path

tool, tree, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
run = subprocess.run([sys.executable, str(tool), '--selftest'], capture_output=True, text=True)
header = f'# tool sha256: {hashlib.sha256(tool.read_bytes()).hexdigest()}\n# tree commit: {commit}\n# command: python3 {tool.name} --selftest (exit {run.returncode})\n'
out.write_text(header + run.stdout, encoding='utf-8')
print(run.stdout.rstrip().splitlines()[-1])
sys.exit(run.returncode)
