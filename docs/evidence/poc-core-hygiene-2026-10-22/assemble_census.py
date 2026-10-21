#!/usr/bin/env python3
"""Census of packages/three-surface-poc-core before and after, one record.

Usage: assemble_census.py <base-tree> <after-tree> <out.json>

Runs export_census.census (same directory) over both trees in lexer mode and in
--raw mode (comments count as uses: the cross-check on the lexer), then records
class totals, the exports removed, added and re-classed between the two trees in
lexer mode, and the full rows of the subject names. Each tree is a git checkout;
the record names the commit of each.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_census import census  # noqa: E402

PREFIX = 'packages/three-surface-poc-core/src/'
BARRELS = {PREFIX + 'index.ts'}
SUBJECT_NAMES = {
    'derivePopulationBlock', 'draftOwnerAct', 'removeFixtureDirectory',
    'JUDGMENT_INVALID_CASE_IDS', 'ClassificationOutcome', 'FactFamilyKind', 'FACT_FAMILIES', 'COMMON_INVALID_CASES',
    'appendEvaluation', 'appendJudgmentEvaluation', 'rollbackMaterializedWorkItem', 'ownerActProvenance',
    'clearTestArtifactRecordFile', 'liveTestOperatorInstructions',
}


def totals(rows: list[dict]) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in rows:
        out[r['class']] = out.get(r['class'], 0) + 1
    return dict(sorted(out.items()))


def commit(tree: Path) -> str:
    return subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()


def main() -> int:
    base, after, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    runs = {}
    for label, tree in (('base', base), ('after', after)):
        for mode, raw in (('lexer', False), ('raw', True)):
            rows, stars, declaring = census(tree, PREFIX, BARRELS, raw)
            runs[(label, mode)] = rows
            print(f'{label} {mode}: declaring files {declaring}, exports {len(rows)}, {totals(rows)}, star re-export files {stars}')
    key = lambda r: (r['file'], r['name'])
    b = {key(r): r for r in runs[('base', 'lexer')]}
    a = {key(r): r for r in runs[('after', 'lexer')]}
    braw = {key(r): r['class'] for r in runs[('base', 'raw')]}
    record = {
        'tool': 'assemble_census.py (export_census.census)',
        'prefix': PREFIX,
        'barrels': sorted(BARRELS),
        'baseCommit': commit(base),
        'afterCommit': commit(after),
        'totals': {f'{label}-{mode}': {'exports': len(rows), 'classes': totals(rows)} for (label, mode), rows in runs.items()},
        'lexerVersusRawOnBase': {
            'exportsWhoseClassDiffers': sorted(f'{k[0].split("/")[-1]}:{k[1]} lexer={b[k]["class"]} raw={braw[k]}' for k in b if b[k]['class'] != braw[k]),
        },
        'baseToAfterLexer': {
            'removed': sorted(f'{k[0].split("/")[-1]}:{k[1]}' for k in set(b) - set(a)),
            'added': sorted(f'{k[0].split("/")[-1]}:{k[1]}' for k in set(a) - set(b)),
            'classChanged': sorted(f'{k[0].split("/")[-1]}:{k[1]} {b[k]["class"]} -> {a[k]["class"]}' for k in set(b) & set(a) if b[k]['class'] != a[k]['class']),
        },
        'subjectRows': {
            label: [r for r in runs[(label, 'lexer')] if r['name'] in SUBJECT_NAMES]
            for label in ('base', 'after')
        },
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    d = record['baseToAfterLexer']
    print('removed', d['removed'], 'added', d['added'], 'classChanged', d['classChanged'])
    print('lexer vs raw differ on base:', len(record['lexerVersusRawOnBase']['exportsWhoseClassDiffers']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
