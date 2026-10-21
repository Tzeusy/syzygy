#!/usr/bin/env python3
"""Rule-6 mutation record for comment_only_check.py.

Usage: mutate_comment_only.py <tree> <old-commit> <out.json>

Each mutant rewrites one file of <tree> in place (a source file or a built dist
file), runs comment_only_check.py against <old-commit>, records what the check
reported, and restores the file's exact bytes in a finally block. A mutant is
killed when the check's verdict is the failing one. <tree> must be built.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

CORE = 'packages/three-surface-poc-core/'
MUTANTS = [
    # id, file, old fragment, new fragment, predicate over the check record that holds when the mutant is killed
    ('source-code-token-added', CORE + 'src/evidence-population.ts', '// Keep the name, the path and the barrel export.\n', '// Keep the name, the path and the barrel export.\nexport const ZZ_MUTANT = 1;\n', 'comment-only-false'),
    ('source-comment-edit-is-not-a-failure', CORE + 'src/evidence-population.ts', '// Keep the name, the path and the barrel export.\n', '// Keep the name, the path and the barrel export. (edited)\n', 'comment-only-true'),
    ('dist-module-export-removed', CORE + 'dist/evidence-population.js', 'export function derivePopulationBlock', 'function derivePopulationBlock', 'module-export-false'),
    ('dist-barrel-reexport-removed', CORE + 'dist/index.js', "export * from './evidence-population.js';", '', 'barrel-false'),
]


def killed(kind: str, rec: dict) -> bool:
    return {
        'comment-only-false': rec['allIdenticalAfterCommentStrip'] is False,
        'comment-only-true': rec['allIdenticalAfterCommentStrip'] is True,
        'module-export-false': rec['retainedExport']['moduleExportsFunction'] is False,
        'barrel-false': rec['retainedExport']['barrelReexportsSameFunction'] is False,
    }[kind]


def main() -> int:
    tree, old, out = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3])
    check = Path(__file__).resolve().parent / 'comment_only_check.py'
    commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
    records = []
    for mutant_id, rel, frag_old, frag_new, kind in MUTANTS:
        path = tree / rel
        original = path.read_bytes()
        text = original.decode('utf-8')
        if text.count(frag_old) != 1:
            raise SystemExit(f'{mutant_id}: old fragment occurs {text.count(frag_old)} times in {rel}, expected 1')
        try:
            path.write_text(text.replace(frag_old, frag_new), encoding='utf-8')
            with tempfile.TemporaryDirectory() as tmp:
                res = subprocess.run([sys.executable, str(check), str(tree), old, str(Path(tmp) / 'r.json')], capture_output=True, text=True)
                rec = json.loads((Path(tmp) / 'r.json').read_text())
        finally:
            path.write_bytes(original)
        records.append({'id': mutant_id, 'file': rel, 'old': frag_old, 'new': frag_new, 'expectedFailure': kind, 'killed': killed(kind, rec),
                        'firstOutputLine': res.stdout.splitlines()[0] if res.stdout else res.stderr.splitlines()[-1]})
    summary = {'subject': 'comment_only_check.py', 'ranAtCommit': commit, 'oldCommit': old, 'mutants': len(records), 'killed': sum(r['killed'] for r in records),
               'survivors': [r['id'] for r in records if not r['killed']], 'records': records}
    out.write_text(json.dumps(summary, indent=1) + '\n', encoding='utf-8')
    print(f"mutants={summary['mutants']} killed={summary['killed']} survivors={summary['survivors']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
