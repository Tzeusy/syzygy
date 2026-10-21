#!/usr/bin/env python3
"""Rule-6 run for apps/three-surface-poc/src/main.test.ts (and, when present,
the throwaway old-vs-new differential): each mutant edits main.ts, the named
test file must FAIL, and main.ts is restored byte-for-byte afterwards.

Usage: mutate_main.py <worktree> <test-file-relative-to-worktree> <out.json>
Records, per mutant, the exact old/new fragment, the command, the commit the
run was made at, and the names of the failing tests.
"""
import hashlib
import json
import pathlib
import subprocess
import sys

WT = pathlib.Path(sys.argv[1])
TEST = sys.argv[2]
OUT = pathlib.Path(sys.argv[3])
MAIN = WT / 'apps/three-surface-poc/src/main.ts'
original = MAIN.read_text()
digest = hashlib.sha256(original.encode()).hexdigest()
commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
dirty = subprocess.run(['git', 'status', '--porcelain', '--', 'apps/three-surface-poc/src/main.ts'], cwd=WT, capture_output=True, text=True, check=True).stdout.strip()
assert dirty == '', f'main.ts must be committed before a rule-6 run: {dirty}'

MUTANTS = [
    ('launcher-gate-bypassed',
     "  const launch = await launchAfterPwbRepositoryBinding(\n    repoRoot,\n    deps.resolveBinding,\n    (boundRepoRoot) => serveBoundRepository(boundRepoRoot, parsed.config, io, deps),\n  );",
     "  const launch = { kind: 'launched' as const, result: await serveBoundRepository(repoRoot, parsed.config, io, deps) };"),
    ('help-exit-code', "    io.stdout.write(USAGE);\n    return 0;", "    io.stdout.write(USAGE);\n    return 1;"),
    ('invalid-exit-code', "    io.stderr.write(`syzygy POC: ${parsed.detail}\\n\\n${USAGE}`);\n    return 1;", "    io.stderr.write(`syzygy POC: ${parsed.detail}\\n\\n${USAGE}`);\n    return 2;"),
    ('unreadable-repo-message', "configured repository is not readable", "configured repository is unreadable"),
    ('rejected-binding-exit-code', "authority rejected (${launch.reason})\\n`);\n    return 1;", "authority rejected (${launch.reason})\\n`);\n    return 2;"),
    ('rejected-binding-reason-dropped', "authority rejected (${launch.reason})", "authority rejected"),
    ('initial-dirty-refusal-name', "observeCheckouts('observer-checkout-dirty')", "observeCheckouts('observer-dirty')"),
    ('horizon-inside-startup-try',
     "  const capture = observeCapture(observed);\n",
     "  let capture: PocRuntimeCapture;\n  try { capture = observeCapture(observed); } catch (cause) { io.stderr.write(`syzygy POC: ${gitObservationDetail(cause)}\\n`); return 1; }\n"),
    ('observer-read-at-process-cwd', "const observer = deps.observeGitRepository(io.cwd());", "const observer = deps.observeGitRepository(process.cwd());"),
    ('model-observer-root-process-cwd', "    observerRoot: io.cwd(),", "    observerRoot: process.cwd(),"),
    ('observation-instant-from-clock', "buildPocEvaluationEvidence(io.now(),", "buildPocEvaluationEvidence(new Date().toISOString(),"),
    ('observatory-root', "deps.observeObservatoryDrift(io.cwd(), buildRevision)", "deps.observeObservatoryDrift(repoRoot, buildRevision)"),
    ('state-dir-digest-width', "slice(0, 16)", "slice(0, 15)"),
    ('daemon-start-failure-exit', "      return 1;\n    }\n    const daemon = start.daemon;", "      return 0;\n    }\n    const daemon = start.daemon;"),
    ('daemon-start-failure-kind-dropped', "daemon did not start (${start.failure.kind}: ${daemonStartDetail(start.failure)})", "daemon did not start (${daemonStartDetail(start.failure)})"),
    ('walkthrough-binding-lines-dropped', "        ...walkthroughBindingLines(session.model()),\n", ""),
    ('credential-line-dropped', "        `Machine credential (${daemon.credentialProvision}) at: ${daemon.credentialPath}`,\n", ""),
    ('console-output-stream', "{ input: io.stdin, output: io.stdout }", "{ input: io.stdin, output: io.stderr }"),
    ('re-observation-refusal-message', "'POC runtime inputs are dirty; re-observation was refused'", "'POC runtime inputs are dirty'"),
    ('shutdown-message', "`syzygy POC: ${signal} received, shutting down\\n`", "`syzygy POC: ${signal} received\\n`"),
    ('shutdown-guard-removed', "        if (closing) return;\n", ""),
    ('sigterm-not-handled', "      io.onSignal('SIGTERM', () => shutdown('SIGTERM'));\n", ""),
    ('model-failure-exit-code', "      io.stderr.write(`syzygy POC: observation failed (${unexpectedObservationDetail(cause)})\\n`);\n    }\n    return 1;", "      io.stderr.write(`syzygy POC: observation failed (${unexpectedObservationDetail(cause)})\\n`);\n    }\n    return 2;"),
    ('observation-error-path-dropped', ".filter((part): part is string => part !== undefined)", ".filter((part): part is string => part !== undefined && part !== cause.artifactPath)"),
]

command = ['npx', 'vitest', 'run', TEST]
results = []
try:
    for name, old, new in MUTANTS:
        if original.count(old) != 1:
            results.append({'id': name, 'old': old, 'new': new, 'outcome': f'FRAGMENT-COUNT-{original.count(old)}'})
            print(name, results[-1]['outcome'], flush=True)
            continue
        MAIN.write_text(original.replace(old, new, 1))
        proc = subprocess.run(command, cwd=WT, capture_output=True, text=True)
        out = proc.stdout + proc.stderr
        failed = sorted({line.split(' > ', 1)[-1].strip() for line in out.splitlines() if line.lstrip().startswith(('×', 'FAIL ')) and ' > ' in line})
        results.append({'id': name, 'old': old, 'new': new, 'exit': proc.returncode, 'outcome': 'killed' if proc.returncode != 0 else 'SURVIVED', 'failingTests': failed})
        print(name, results[-1]['outcome'], len(failed), flush=True)
finally:
    MAIN.write_text(original)
assert hashlib.sha256(MAIN.read_text().encode()).hexdigest() == digest
OUT.write_text(json.dumps({
    'mutatedFile': 'apps/three-surface-poc/src/main.ts',
    'testFile': TEST,
    'command': ' '.join(command),
    'ranAtCommit': commit,
    'mainTsSha256AtCommit': digest,
    'mutants': len(MUTANTS),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['id'] for r in results if r['outcome'] != 'killed'])
