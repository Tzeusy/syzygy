#!/usr/bin/env python3
"""Run the 42-scenario old-script versus new-main differential with fixed roots.

Usage: run_differential_fixed_roots.py <worktree> <old-main-commit> <fixed-root> <transcripts-out.json>

The harness is ../poc-hygiene-2026-10-22/main-old-vs-new-differential.test.ts.txt,
unchanged on disk. The page bodies and the default state directory of five
scenarios embed the repository roots, which that harness draws at random, so a
base-versus-head comparison of its transcripts can only say "equal except the
five that embed a temporary path". This script writes a copy of the harness in
which three statements are replaced (each replacement must match exactly once)
so that both roots are the same paths on every run:
  - the observed repository `REPO` is <fixed-root>/repo (a directory);
  - the fixture model is built over <fixed-root>/fixture, a copy of the fixture
    repository whose revision is deterministic (pinned commit instants).
The copy and the old script (`git show <old-main-commit>:...main.ts`) are
written under the worktree's apps/three-surface-poc/src as throwaway files and
removed afterwards. Two files are written: the raw transcripts at
<transcripts-out.json>, which name the scratch path, and <transcripts-out.json>.canonical
with the repository and fixed-root paths replaced by <REPO> and <FIXED-ROOT>, which
is what a record keeps; the caller records both digests.
"""
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
WT = pathlib.Path(sys.argv[1]).resolve()
OLD_MAIN_COMMIT = sys.argv[2]
FIXED_ROOT = pathlib.Path(sys.argv[3])
TRANSCRIPTS = pathlib.Path(sys.argv[4]).resolve()
HARNESS = HERE.parent / 'poc-hygiene-2026-10-22' / 'main-old-vs-new-differential.test.ts.txt'
SRC = WT / 'apps/three-surface-poc/src'
ZZ_TEST, ZZ_OLD = SRC / 'zz-main-differential.test.ts', SRC / 'zz-main-old.ts'
REL_TEST = 'apps/three-surface-poc/src/zz-main-differential.test.ts'

REPLACEMENTS = [
    ("import { createHash } from 'node:crypto';\nimport { mkdtempSync, realpathSync, rmSync, writeFileSync } from 'node:fs';",
     "import { createHash } from 'node:crypto';\nimport { cpSync, existsSync, mkdirSync, mkdtempSync, realpathSync, rmSync, writeFileSync } from 'node:fs';"),
    ("const REPO = realpathSync(mkdtempSync(join(tmpdir(), 'zz-main-repo-')));",
     "const FIXED_ROOT = process.env.ZZ_FIXED_ROOT!;\nmkdirSync(join(FIXED_ROOT, 'repo'), { recursive: true });\nconst REPO = realpathSync(join(FIXED_ROOT, 'repo'));"),
    ("    model = buildFixtureModel(cleanups);",
     "    const fixtureRoot = join(FIXED_ROOT, 'fixture');\n"
     "    const made = fixtureRepoWithGit(cleanups);\n"
     "    if (!existsSync(fixtureRoot)) cpSync(made.repoRoot, fixtureRoot, { recursive: true });\n"
     "    model = buildFixtureModel(cleanups, { fixtureRepo: { repoRoot: fixtureRoot, revision: made.revision } });"),
    ("import { buildFixtureModel } from './test-model-fixture.js';",
     "import { buildFixtureModel, fixtureRepoWithGit } from './test-model-fixture.js';"),
    ("afterAll(() => { rmSync(REPO, { recursive: true, force: true }); });",
     "afterAll(() => { for (const directory of cleanups) rmSync(directory, { recursive: true, force: true }); /* the fixed roots are removed by the caller */ });"),
    ("    if (out !== undefined) writeFileSync(out, JSON.stringify((globalThis as { __zzTranscripts?: unknown[] }).__zzTranscripts, null, 1).replaceAll(REPO, '<REPO>'));",
     "    if (out !== undefined) {\n"
     "      const raw = JSON.stringify((globalThis as { __zzTranscripts?: unknown[] }).__zzTranscripts, null, 1);\n"
     "      writeFileSync(out, raw);\n"
     "      writeFileSync(`${out}.canonical`, raw.replaceAll(REPO, '<REPO>').replaceAll(FIXED_ROOT, '<FIXED-ROOT>'));\n"
     "    }"),
]

text = HARNESS.read_text()
for old, new in REPLACEMENTS:
    assert text.count(old) == 1, f'harness statement not found exactly once: {old[:60]!r}'
    text = text.replace(old, new, 1)
old_main = subprocess.run(['git', 'show', f'{OLD_MAIN_COMMIT}:apps/three-surface-poc/src/main.ts'], cwd=WT, capture_output=True, text=True, check=True).stdout
report = pathlib.Path(tempfile.mkdtemp(prefix='zz-differential-')) / 'report.json'
summary = {}
try:
    ZZ_TEST.write_text(text)
    ZZ_OLD.write_text(old_main)
    proc = subprocess.run(['npx', 'vitest', 'run', REL_TEST, '--reporter=json', f'--outputFile={report}'], cwd=WT, capture_output=True, text=True,
                          env={**os.environ, 'ZZ_TRANSCRIPT_OUT': str(TRANSCRIPTS), 'ZZ_FIXED_ROOT': str(FIXED_ROOT)})
    data = json.loads(report.read_text())
    cases = [a for suite in data['testResults'] for a in suite['assertionResults']]
    summary = {
        'exit': proc.returncode,
        'tests': len(cases),
        'passed': sum(1 for a in cases if a['status'] == 'passed'),
        'failed': [{'test': a['fullName'], 'firstErrorLine': (a['failureMessages'][0].splitlines() or [''])[0]} for a in cases if a['status'] == 'failed'],
    }
finally:
    ZZ_TEST.unlink(missing_ok=True)
    ZZ_OLD.unlink(missing_ok=True)

record = {
    'treeCommit': subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=WT, capture_output=True, text=True, check=True).stdout.strip(),
    'oldMainCommit': OLD_MAIN_COMMIT,
    'oldMainSha256': hashlib.sha256(old_main.encode()).hexdigest(),
    'harnessSha256': hashlib.sha256(HARNESS.read_bytes()).hexdigest(),
    'replacements': len(REPLACEMENTS),
    'run': summary,
}
TRANSCRIPTS.with_suffix('.run.json').write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps(record))
sys.exit(summary.get('exit', 1))
