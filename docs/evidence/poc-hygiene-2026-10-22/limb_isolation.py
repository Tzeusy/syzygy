#!/usr/bin/env python3
"""Show that the `existsSync(stateDir)` limb of main.test.ts's rejected-binding
test carries weight (round 1, N2).

Usage: limb_isolation.py <worktree> <out.json>

A throwaway variant of main.test.ts (apps/three-surface-poc/src/
main-limb-isolation.test.ts, removed afterwards) keeps only the existsSync
limb of that test: the exit-code, stderr, stdout and call-log assertions are
held out. Each cell runs the variant, or the full test, against poc-main.ts
with or without a source mutant, and poc-main.ts is restored byte for byte.

  cells                                     expected
  limb-only, unmutated                      passes   (the variant is sound)
  limb-only, gate bypassed                  fails    (the limb alone detects it)
  limb-only, gate bypassed, fake daemon
    that creates nothing (the reviewed
    state of the test)                      passes   (the limb could not fail)
  limb-only, state directory written
    before the gate                         fails    (independent of the daemon fake)
  full test, gate bypassed                  fails    (first error line recorded)
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

WT = pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2])
SRC = 'apps/three-surface-poc/src/'
MUTATED = SRC + 'poc-main.ts'
TEST = SRC + 'main.test.ts'
VARIANT = SRC + 'main-limb-isolation.test.ts'
main_path, test_path, variant_path = WT / MUTATED, WT / TEST, WT / VARIANT

BYPASS = (
    "  const launch = await launchAfterPwbRepositoryBinding(\n    repoRoot,\n    deps.resolveBinding,\n    (boundRepoRoot) => serveBoundRepository(boundRepoRoot, parsed.config, io, deps),\n  );",
    "  const launch = { kind: 'launched' as const, result: await serveBoundRepository(repoRoot, parsed.config, io, deps) };",
)
PRE_GATE_WRITE = (
    "  const launch = await launchAfterPwbRepositoryBinding(",
    "  if (parsed.config.stateDir !== undefined) (await import('node:fs')).mkdirSync(parsed.config.stateDir, { recursive: true });\n  const launch = await launchAfterPwbRepositoryBinding(",
)

ASSERTIONS = (
    "    expect(await main(['--repo', repoRoot, '--state-dir', stateDir], fake.io, h.deps)).toBe(1);\n"
    "    expect(fake.err()).toBe('syzygy POC: configured repository authority rejected (locator-mismatched)\\n');\n"
    "    expect(fake.out()).toBe('');\n"
    "    expect(h.calls).toEqual([`bind ${repoRoot}`]);\n"
    "    expect(existsSync(stateDir)).toBe(false);\n"
)
LIMB_ONLY = (
    "    await main(['--repo', repoRoot, '--state-dir', stateDir], fake.io, h.deps);\n"
    "    expect(existsSync(stateDir)).toBe(false);\n"
)
DAEMON_MAKES = "      { daemonMakesStateDir: true, start:"
DAEMON_NOT = "      { start:"

original_main = main_path.read_text()
original_test = test_path.read_text()
digest = hashlib.sha256(original_main.encode()).hexdigest()
commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
dirty = subprocess.run(['git', 'status', '--porcelain', '--', MUTATED, TEST], cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
assert dirty == '', f'commit {MUTATED} and {TEST} before a rule-6 run: {dirty}'
assert original_test.count(ASSERTIONS) == 1 and original_test.count(DAEMON_MAKES) == 1


def variant_text(keep_daemon_fake: bool) -> str:
    text = original_test.replace(ASSERTIONS, LIMB_ONLY)
    return text if keep_daemon_fake else text.replace(DAEMON_MAKES, DAEMON_NOT)


report_dir = pathlib.Path(tempfile.mkdtemp(prefix='zz-limb-isolation-'))


def run(label: str, test_file: str, mutant) -> dict:
    main_path.write_text(original_main if mutant is None else original_main.replace(mutant[0], mutant[1], 1))
    if mutant is not None:
        assert original_main.count(mutant[0]) == 1
    report = report_dir / 'report.json'
    report.unlink(missing_ok=True)
    proc = subprocess.run(['npx', 'vitest', 'run', test_file, '-t', 'a rejected binding exits 1', '--reporter=json', f'--outputFile={report}'], cwd=WT, capture_output=True, text=True)
    data = json.loads(report.read_text())
    cases = [a for suite in data['testResults'] for a in suite['assertionResults']]
    failing = [{'test': a['fullName'], 'firstErrorLine': (a['failureMessages'][0].splitlines() or [''])[0]} for a in cases if a['status'] == 'failed']
    passed = sum(1 for a in cases if a['status'] == 'passed')
    print(label, 'exit', proc.returncode, 'passed', passed, 'failed', len(failing), flush=True)
    return {'cell': label, 'testFile': test_file, 'mutant': None if mutant is None else {'old': mutant[0], 'new': mutant[1]},
            'exit': proc.returncode, 'passed': passed, 'failing': failing}


cells = []
try:
    variant_path.write_text(variant_text(True))
    cells.append(run('limb-only / unmutated', VARIANT, None))
    cells.append(run('limb-only / gate bypassed', VARIANT, BYPASS))
    cells.append(run('limb-only / state directory written before the gate', VARIANT, PRE_GATE_WRITE))
    variant_path.write_text(variant_text(False))
    cells.append(run('limb-only, fake daemon creates nothing / gate bypassed', VARIANT, BYPASS))
    cells.append(run('full test / gate bypassed', TEST, BYPASS))
finally:
    main_path.write_text(original_main)
    variant_path.unlink(missing_ok=True)
assert hashlib.sha256(main_path.read_text().encode()).hexdigest() == digest
assert test_path.read_text() == original_test and not variant_path.exists()

expected = [0, 1, 1, 0, 1]
assert [0 if c['exit'] == 0 else 1 for c in cells] == expected, [(c['cell'], c['exit']) for c in cells]
OUT.write_text(json.dumps({
    'tool': 'limb_isolation.py',
    'toolSha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    'ranAtCommit': commit,
    'mutatedFile': MUTATED,
    'mutatedFileSha256AtCommit': digest,
    'testFile': TEST,
    'testFileSha256AtCommit': hashlib.sha256(original_test.encode()).hexdigest(),
    'question': 'does the existsSync(stateDir) limb of the rejected-binding test fail on its own when the gate is bypassed',
    'answer': 'yes when the fake daemon creates its state directory; no when it creates nothing (the reviewed state of the test)',
    'cells': cells,
}, indent=1) + '\n')
print('ok')
