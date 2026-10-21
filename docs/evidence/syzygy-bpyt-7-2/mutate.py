#!/usr/bin/env python3
"""Rule-6 mutate-and-fail runs for syzygy-bpyt.7.2.

Each mutant rewrites one fragment (every occurrence is asserted to be exactly
one), runs the stated command, records exit code and failing-test counts, and
restores the file byte-for-byte. Output: JSON list on stdout and --out.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

WT = Path('/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-bpyt.7.2')
OUT = Path(sys.argv[1])
ONLY = set(sys.argv[2:])

VITEST = ['npx', 'vitest', 'run', '--project', '@syzygy/cap1-conformance', '--project', '@syzygy/cap1-daemon']
TSC = ['npx', 'tsc', '-b', '--force', 'packages/cap1-conformance']
SYSTEM = ['bash', '-c', 'npm run build >/dev/null 2>&1; npx vitest run --config packages/cap1-system/vitest.config.ts packages/cap1-system/src/write-boundary.system.test.ts']
MAIN = 'apps/syzygy/src/main.ts'
FX = 'packages/cap1-conformance/src/fixtures/index.ts'
TESTING = 'packages/cap1-core/src/testing.ts'
INDEX = 'packages/cap1-core/src/index.ts'
VCONF = 'vitest.config.ts'
PKG = 'packages/cap1-core/package.json'

MUTANTS = [
    ('M01-schema-version', FX, 'schema_version: "1"', 'schema_version: "2"', VITEST),
    ('M02-spec-root', FX, 'spec_root: openspec/', 'spec_root: specs/', VITEST),
    ('M03-owner-default', FX, "fields.owner ?? FIXTURE_OWNER", "fields.owner ?? 'nobody@example.com'", VITEST),
    ('M04-repository-role', FX, 'role: ${repository.role}', 'role: observed-source', VITEST),
    ('M05-consents-dropped', FX, "sequence('consents', consents)", "sequence('consents', [])", VITEST),
    ('M06-relations-dropped', FX, "sequence('relations', relations)", "sequence('relations', [])", VITEST),
    ('M07-profiles-dropped', FX, "sequence('profiles', profiles)", "sequence('profiles', [])", VITEST),
    ('M08-as-of', FX, "FIXTURE_AS_OF = '2026-08-21T00:00:00Z'", "FIXTURE_AS_OF = '2026-08-22T00:00:00Z'", VITEST),
    ('M09-evaluation-swap', FX, 'return { snapshot, asOf };', 'return { snapshot: asOf, asOf };', VITEST),
    ('M10-consent-grant-state', FX, "fields.grantState ?? 'in-force'", "fields.grantState ?? 'withdrawn'", VITEST),
    ('M11-consent-attribution', FX, "attribution: 'owner',", "attribution: 'agent',", VITEST),
    ('M12-consent-project', FX, 'projectId: fields.projectId,', 'projectId: fields.repositoryId as unknown as ProjectId,', VITEST),
    ('M13-consent-scope', FX, "scope: 'observe',", "scope: 'full',", VITEST),
    ('M14-schema-version-line-dropped', FX, "'\\nschema_version: \"1\"\\n',", "'\\n',", VITEST),
    ('M15-declarations-emptied', FX, "'declarations:\\n  spec_root: openspec/\\n',", "'declarations: {}\\n',", VITEST),
    ('M16-project-id-dropped', FX, 'project:\\n  id: ${fields.id}\\n  name:', 'project:\\n  name:', VITEST),
    ('M17-repositories-dropped', FX, "sequence('repositories', repositories)", "sequence('repositories', [])", VITEST),
    ('S00-system-control-unmutated', MAIN, 'const { root, stateDir, port } = parsed.config;', 'const { root, stateDir, port } = parsed.config;', SYSTEM),
    ('S01-daemon-writes-syzygy-plane', MAIN, 'const { root, stateDir, port } = parsed.config;', "const { root, stateDir, port } = parsed.config;\n  fs.writeFileSync(path.join(root, '.syzygy', 'zz-intruder.txt'), 'x');", SYSTEM),
    ('S02-daemon-writes-openspec-plane', MAIN, 'const { root, stateDir, port } = parsed.config;', "const { root, stateDir, port } = parsed.config;\n  fs.writeFileSync(path.join(root, 'openspec', 'zz-intruder.txt'), 'x');", SYSTEM),
    ('E01-testing-drops-boundary', TESTING, "export * from './write-boundary.js';", '', VITEST),
    ('E02-testing-drops-oracle', TESTING, "export * from './parity-oracle.js';", '', VITEST),
    ('E03-alias-dropped', VCONF, "'@syzygy/cap1-core/testing'", "'@syzygy/cap1-core/testing-gone'", VITEST),
    ('E04-package-export-dropped', PKG, '"./testing"', '"./testing-gone"', TSC),
    ('E05-barrel-readds-boundary', INDEX, "export * from './parity.js';", "export * from './parity.js';\nexport * from './write-boundary.js';", VITEST),
]


def run(cmd):
    proc = subprocess.run(cmd, cwd=WT, capture_output=True, text=True)
    text = proc.stdout + proc.stderr
    failed_tests = re.search(r'Tests\s+(?:(\d+) failed)?', text)
    failed_files = re.search(r'Test Files\s+(?:(\d+) failed)?', text)
    return proc.returncode, text, failed_files, failed_tests


results = []
head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=WT, capture_output=True, text=True).stdout.strip()
for ident, rel, old, new, cmd in MUTANTS:
    if ONLY and ident not in ONLY:
        continue
    path = WT / rel
    original = path.read_bytes()
    text = original.decode('utf-8')
    count = text.count(old)
    if count != 1:
        results.append({'id': ident, 'error': f'fragment occurs {count} times in {rel}'})
        continue
    path.write_text(text.replace(old, new), encoding='utf-8')
    try:
        code, out, files, tests = run(cmd)
    finally:
        path.write_bytes(original)
    summary = [line for line in out.splitlines() if line.strip().startswith(('Test Files', 'Tests', 'error TS'))][:3]
    results.append({
        'id': ident,
        'file': rel,
        'old': old,
        'new': new,
        'command': ' '.join(cmd),
        'exit': code,
        'killed': code != 0,
        'summary': summary,
    })
    print(ident, 'exit', code, summary[:2], flush=True)

OUT.write_text(json.dumps({'baseHeadAtRun': head, 'mutants': results}, indent=1) + '\n')
