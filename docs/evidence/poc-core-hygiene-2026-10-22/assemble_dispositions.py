#!/usr/bin/env python3
"""Disposition table for syzygy-bpyt.7.6, with the sweep counts read from the records.

Usage: assemble_dispositions.py <consumer-sweep-base.json> <consumer-sweep-code.json> <export-census.json> <out.json>

The decisions and their reasons are written here; every count (files hit, by
category, denominator) is read from the sweep and census records, never typed.
"""
import json
import sys
from pathlib import Path

CORE = 'packages/three-surface-poc-core/src/'

# id -> (kind, disposition, reason, authority/consumer citations)
TABLE = {
    'evidence-population.ts': (
        'orphan', 'kept; head comment added; barrel export unchanged',
        'Not unconsumed: the M1 page-size design note requires new page-size evidence records to carry a population block derived with '
        'derivePopulationBlock in this path, and a retained measurement script embeds a require of this module\'s compiled file. '
        'Moving or deleting it breaks the path that script and note name; the package barrel is not the consumer.',
        ['docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md:380-384 (candidate design material, binds nothing)',
         'docs/evidence/pwb-m1-polaris-lane-a-population-2026-09-23.json (measurementScript requires dist/evidence-population.js)']),
    'owner-act-drafter.ts': (
        'orphan', 'kept unchanged; note added in the barrel, not in the file',
        'Consumed by owner ruling, not dead: P-71 Q3 arm (b) is "a pure drafter that writes no file", and the operator command that would render '
        'its output was never built. The note sits in the barrel because docs/evidence/syzygy-dov41-unknown-routes-rule6-2026-10-03.json cites '
        'the file\'s digest; the file\'s bytes stay as that record has them.',
        ['.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:58 (P-71, ruled A, 2026-09-21)',
         '.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/OWNER-DECISION-PACKET.md:341',
         'docs/evidence/syzygy-dov41-unknown-routes-rule6-2026-10-03.json']),
    'test-cleanup.ts': (
        'orphan', 'kept in place; test-support head comment added',
        'Already outside the barrel and package exports; the only importers are model.test.ts and its own test. A test-support entry would add '
        'a package entry point for one same-package caller, so none was added. A near-duplicate, removeTemporaryDirectory, lives in '
        'apps/three-surface-poc/src/temporary-directory.ts for the app (follow-up, not folded here: it would change the app).',
        []),
    'JUDGMENT_INVALID_CASE_IDS': (
        'deleted', 'deleted with its comment, and with the import of COMMON_INVALID_CASES only it used',
        'Declared with the PWB-REQ-022 evaluator and never read: the test asserts the 84-case population from its own hand-typed table. '
        'The component arrays and the JudgmentInvalidCase type stay.',
        []),
    'ClassificationOutcome': ('deleted', 'deleted', 'A type alias nothing names.', []),
    'FactFamilyKind': (
        'deleted', 'deleted',
        'A type alias nothing names. Its only reader was FACT_FAMILIES, which now has no code reader and stays (see cascades).',
        []),
    'appendEvaluation': (
        'test-only', 'kept; Test seam comment',
        'Pins the PWB-REQ-005 append-only history rule; no production code calls it yet. The retained-evaluations design reuses the pattern.',
        ['docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md (candidate design material, binds nothing)']),
    'appendJudgmentEvaluation': (
        'test-only', 'kept; Test seam comment',
        'Pins the PWB-REQ-022 append-only judgment history; the mutation sweep\'s history-append-only site is in its body '
        '(apps/three-surface-poc/src/pwb-mutation-sweep.ts and its test count exactly one such site), so deleting it would retire a sweep site.',
        ['docs/PWB-IMPLEMENTATION-PLAN.md', 'docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md']),
    'rollbackMaterializedWorkItem': (
        'test-only', 'kept; Test seam comment',
        'The inverse of the materialize action: it closes the recorded work item and clears the local record. No route or command calls it, and '
        'it acts on the observed repository\'s tracker, so removing or wiring it is an authority question, not hygiene.',
        []),
    'ownerActProvenance': (
        'test-only', 'kept; Test seam comment',
        'Builds the plan\'s owner-act provenance entries per authority; pinned by project-shape-model.test.ts.',
        ['docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md (candidate design material, binds nothing)']),
    'clearTestArtifactRecordFile': (
        'test-only', 'kept; Test seam comment',
        'The test cleanup counterpart of writeTestArtifactRecordFile; the package test is its only caller.',
        []),
    'liveTestOperatorInstructions': (
        'test-only', 'kept; Test seam comment',
        'The message the live verification test prints when the operator\'s result is missing; test-artifact-verification.live.test.ts calls it and '
        'test-artifact-verification-live-source.test.ts asserts the call in that file\'s source.',
        []),
}

NAMES = {  # sweep subject id -> token whose counts are cited
    'evidence-population.ts': ('orphan-path', 'evidence-population'),
    'owner-act-drafter.ts': ('orphan-path', 'owner-act-drafter'),
    'test-cleanup.ts': ('orphan-path', 'test-cleanup'),
}


def sweep_view(sweep: dict, kind: str, subject: str, token: str | None) -> dict:
    for record in sweep['subjects']:
        if record['kind'] == kind and record['id'] == subject:
            tokens = record['tokens']
            t = next((x for x in tokens if x['token'] == token), tokens[-1]) if token else tokens[-1]
            return {
                'token': t['token'],
                'files': t['pyRegexFiles'],
                'methodsAgreeOnFiles': t['methodsAgreeOnFiles'],
                'filesByCategory': {k: len(v) for k, v in t['filesByCategory'].items()},
            }
    raise SystemExit(f'no sweep record for {kind} {subject}')


def main() -> int:
    base, code, census = (json.loads(Path(p).read_text()) for p in sys.argv[1:4])
    out = Path(sys.argv[4])
    entries = []
    for subject, (kind, disposition, reason, cites) in TABLE.items():
        sweep_kind = {'orphan': 'orphan-path' if subject.endswith('.ts') else 'orphan-name', 'deleted': 'deleted-name', 'test-only': 'test-only-name'}[kind]
        token = NAMES.get(subject, (None, None))[1]
        entries.append({
            'subject': subject,
            'class': kind,
            'disposition': disposition,
            'reason': reason,
            'citations': cites,
            'sweepAtBase': sweep_view(base, sweep_kind, subject, token),
            'sweepAtCodeCommit': sweep_view(code, sweep_kind, subject, token),
        })
    totals = census['totals']
    record = {
        'bead': 'syzygy-bpyt.7.6',
        'denominator': {'trackedFilesAtBase': base['trackedFiles'], 'baseCommit': base['treeCommit'], 'trackedFilesAtCodeCommit': code['trackedFiles'], 'codeCommit': code['treeCommit']},
        'methods': 'consumer_sweep.py: git grep -I -n -w -F (names) or -F (paths and stems), and an independent Python regex over every tracked file; both must agree on the file list. Stems are also searched with whitespace removed to catch a citation wrapped across a line.',
        'dispositions': entries,
        'cascades': [
            {'subject': 'FACT_FAMILIES', 'change': census['baseToAfterLexer']['classChanged'], 'disposition': 'kept; note added; the registry-currency amendment packet and its builder script cite it by name'},
            {'subject': 'COMMON_INVALID_CASES', 'disposition': 'kept; now used only inside body-read-authority.ts, left to the un-export sweep'},
        ],
        'notInScope': {
            'selfOnlyExportsAfter': totals['after-lexer']['classes']['self-only'],
            'text': 'Exports used only inside their own file are a public-surface un-export sweep, not dead code: filed as a follow-up in the Worker Report.',
        },
        'censusClassTotals': {k: v['classes'] for k, v in totals.items()},
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    print(f"dispositions={len(entries)} denominatorBase={base['trackedFiles']} codeCommit={code['treeCommit'][:8]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
