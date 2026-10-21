#!/usr/bin/env python3
"""Assemble the verification record for the NON_HUMAN_PRINCIPAL pin change.

Usage:
  assemble_verification.py <tree> <base-commit> <logs-dir> <out.json>

<tree> is the checkout the gate logs were produced on; <logs-dir> holds
vitest-full.log, typecheck.log, governance-base.txt, governance-head.txt,
authority-sweep.log, quotations-base.txt and quotations-head.txt. The record
stores each log's sha256 and the lines it quotes, the digest of act-fields.ts
in the tree and in both mutant records, and whether the tree differs from the
base in that file or in any non-test implementation file.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

EVIDENCE = 'docs/evidence/non-human-principal-pins-2026-10-22'
RULE_FILE = 'packages/three-surface-poc-core/src/act-fields.ts'
TEST_FILES = [
    'packages/three-surface-poc-core/src/body-read-authority.test.ts',
    'packages/three-surface-poc-core/src/walkthrough-judgment.test.ts',
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(tree: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(['git', '-C', str(tree), *args], capture_output=True, text=True)


def line_matching(path: Path, pattern: str) -> str:
    matches = [ln.strip() for ln in path.read_text(encoding='utf-8').splitlines() if re.search(pattern, ln)]
    if len(matches) != 1:
        raise SystemExit(f'{path.name}: expected exactly one line matching {pattern!r}, found {len(matches)}')
    return matches[0]


def main() -> int:
    tree, base, logs, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
    head = git(tree, 'rev-parse', 'HEAD').stdout.strip()
    before = json.loads((tree / EVIDENCE / 'mutants-before-2026-10-22.json').read_text(encoding='utf-8'))
    after = json.loads((tree / EVIDENCE / 'mutants-after-2026-10-22.json').read_text(encoding='utf-8'))
    lists = json.loads((tree / EVIDENCE / 'test-lists-2026-10-22.json').read_text(encoding='utf-8'))

    rule_digest = sha256(tree / RULE_FILE)
    rule_diff = git(tree, 'diff', '--stat', base, 'HEAD', '--', RULE_FILE).stdout
    changed = git(tree, 'diff', '--name-only', base, 'HEAD').stdout.split()
    implementation_changed = [
        p for p in changed
        if p not in TEST_FILES and not p.startswith(EVIDENCE + '/')
    ]

    full = logs / 'vitest-full.log'
    gov_base, gov_head = logs / 'governance-base.txt', logs / 'governance-head.txt'
    quot_base, quot_head = logs / 'quotations-base.txt', logs / 'quotations-head.txt'
    gov_tail = lambda p: p.read_text(encoding='utf-8').strip().splitlines()[-1]
    log_files = [full, logs / 'typecheck.log', gov_base, gov_head,
                 logs / 'authority-sweep.log', quot_base, quot_head]

    record = {
        'subject': 'verification of the NON_HUMAN_PRINCIPAL pin change (test-only)',
        'tree': {'head': head, 'base': base},
        'ruleFile': {
            'path': RULE_FILE,
            'digestInTree': rule_digest,
            'digestInBeforeRecord': before['subjectDigests'][RULE_FILE],
            'digestInAfterRecord': after['subjectDigests'][RULE_FILE],
            'equalAcrossAll': rule_digest == before['subjectDigests'][RULE_FILE] == after['subjectDigests'][RULE_FILE],
            'gitDiffStatBaseToHead': rule_diff,
        },
        'filesChangedBaseToHead': changed,
        'implementationFilesChanged': implementation_changed,
        'fullSuite': {
            'command': 'npx vitest run',
            'ranAt': head,
            'testFilesLine': line_matching(full, r'^\s*Test Files\s'),
            'testsLine': line_matching(full, r'^\s*Tests\s'),
            'exitLine': line_matching(full, r'^exit='),
        },
        'targetedTests': {
            'baseTotal': before['baseline']['total'],
            'headTotal': after['baseline']['total'],
            'headFailed': after['baseline']['failed'],
            'testsLine': lists['testsLine'],
        },
        'gates': {
            'typecheck': {'command': 'npm run typecheck', 'exitLine': line_matching(logs / 'typecheck.log', r'^exit=')},
            'governance': {
                'command': 'python3 scripts/check_governance.py',
                'baseLastLine': gov_tail(gov_base),
                'headLastLine': gov_tail(gov_head),
                'note': 'the two outputs differ only in the examined-file counts (3029 to 3035 and 1926 to 1928) when run at the same depth beside each other; a base run in a scratch directory also differs in the CG-1f reference listing, which depends on where the root sits',
            },
            'quotations': {
                'command': 'python3 scripts/check_quotations.py',
                'outputsByteIdentical': quot_base.read_bytes() == quot_head.read_bytes(),
            },
            'authoritySweep': {
                'command': 'npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts',
                'testsLine': line_matching(logs / 'authority-sweep.log', r'^\s*Tests\s'),
            },
        },
        'mutants': {
            'planned': after['summary']['planned'],
            'beforeKilled': before['summary']['killed'],
            'afterKilled': after['summary']['killed'],
            'afterSurvivors': after['summary']['survivors'],
            'afterSurvivorsEquivalentWithArgument': after['summary']['survivorsEquivalentWithArgument'],
            'afterSurvivorsWithCorpusWitness': after['summary']['survivorsWithCorpusWitness'],
            'section3HBefore': before['summary']['section3HKilled'],
            'section3HAfter': after['summary']['section3HKilled'],
            'allRestoredBothRuns': before['summary']['allRestored'] and after['summary']['allRestored'],
        },
        'logDigests': {p.name: sha256(p) for p in log_files},
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: record[k] for k in ('ruleFile', 'implementationFilesChanged', 'fullSuite', 'gates')}, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
