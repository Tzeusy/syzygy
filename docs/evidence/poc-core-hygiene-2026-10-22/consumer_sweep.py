#!/usr/bin/env python3
"""Consumer sweep for the syzygy-bpyt.7.6 subjects, over one tree.

Usage: consumer_sweep.py <tree> <out.json>

Two independent methods per subject, each over every tracked file of <tree>:
  git-grep   `git grep -I -n -w -F <token>` (names) or `-F <path>` (paths)
  py-regex   a Python regex over every tracked file read as UTF-8 (errors
             replaced), identifier boundaries (?<![\\w$])token(?![\\w$])
For paths and stems a third column, py-joined, searches the text with all
whitespace removed, so a citation hard-wrapped inside a code span still
matches; a file found only that way is a wrapped citation.
The record names the tree's commit; it is valid only for that commit (rule 7).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

CORE = 'packages/three-surface-poc-core/src/'

# (kind, id, tokens). kind 'path' tokens are path or stem strings; 'name' tokens
# are identifiers.
SUBJECTS = [
    ('orphan-path', 'evidence-population.ts', [CORE + 'evidence-population.ts', 'evidence-population']),
    ('orphan-name', 'derivePopulationBlock', ['derivePopulationBlock']),
    ('orphan-path', 'owner-act-drafter.ts', [CORE + 'owner-act-drafter.ts', 'owner-act-drafter']),
    ('orphan-name', 'draftOwnerAct', ['draftOwnerAct']),
    ('orphan-path', 'test-cleanup.ts', [CORE + 'test-cleanup.ts', 'test-cleanup']),
    ('orphan-name', 'removeFixtureDirectory', ['removeFixtureDirectory']),
    ('deleted-name', 'JUDGMENT_INVALID_CASE_IDS', ['JUDGMENT_INVALID_CASE_IDS']),
    ('deleted-name', 'ClassificationOutcome', ['ClassificationOutcome']),
    ('deleted-name', 'FactFamilyKind', ['FactFamilyKind']),
    ('test-only-name', 'appendEvaluation', ['appendEvaluation']),
    ('test-only-name', 'appendJudgmentEvaluation', ['appendJudgmentEvaluation']),
    ('test-only-name', 'rollbackMaterializedWorkItem', ['rollbackMaterializedWorkItem']),
    ('test-only-name', 'ownerActProvenance', ['ownerActProvenance']),
    ('test-only-name', 'clearTestArtifactRecordFile', ['clearTestArtifactRecordFile']),
    ('test-only-name', 'liveTestOperatorInstructions', ['liveTestOperatorInstructions']),
]


def category(path: str) -> str:
    if path.startswith(CORE):
        return 'core-test' if '.test.' in path else 'core-src'
    if path.startswith('apps/') or path.startswith('packages/'):
        return 'other-code-test' if '.test.' in path else 'other-code'
    if path.startswith('docs/evidence/'):
        return 'docs-evidence'
    if path.startswith('docs/reviews/'):
        return 'docs-reviews'
    if path.startswith('docs/'):
        return 'docs-other'
    if path.startswith('.syzygy/') or path.startswith('openspec/'):
        return 'governed-plane'
    if path.startswith('scripts/'):
        return 'scripts'
    return 'other'


def git(tree: Path, *args: str) -> bytes:
    return subprocess.run(['git', *args], cwd=tree, capture_output=True, check=False).stdout


def main() -> int:
    tree = Path(sys.argv[1])
    out = Path(sys.argv[2])
    commit = git(tree, 'rev-parse', 'HEAD').decode().strip()
    tracked = [p for p in git(tree, 'ls-files', '-z').decode().split('\0') if p]
    text = {p: (tree / p).read_text(encoding='utf-8', errors='replace') for p in tracked if (tree / p).is_file()}
    squashed = {p: re.sub(r'\s+', '', t) for p, t in text.items()}
    records = []
    for kind, subject, tokens in SUBJECTS:
        per_token = []
        for token in tokens:
            is_path = '/' in token or '-' in token
            args = ['grep', '-I', '-n', '-F'] + ([] if is_path else ['-w']) + ['-e', token]
            grep_out = git(tree, *args).decode(errors='replace')
            grep_hits: dict[str, int] = {}
            for line in grep_out.splitlines():
                path = line.split(':', 1)[0]
                grep_hits[path] = grep_hits.get(path, 0) + 1
            pattern = re.compile(r'(?<![\w$])' + re.escape(token) + r'(?![\w$])') if not is_path else re.compile(re.escape(token))
            py_hits = {p: len(pattern.findall(t)) for p, t in text.items() if pattern.search(t)}
            joined = re.sub(r'\s+', '', token)
            joined_files = sorted(p for p, t in squashed.items() if joined in t) if is_path else None
            wrapped_only = sorted(set(joined_files) - set(py_hits)) if joined_files is not None else None
            by_cat: dict[str, list[str]] = {}
            for p in sorted(py_hits):
                by_cat.setdefault(category(p), []).append(p)
            per_token.append({
                'token': token,
                'gitGrepFiles': len(grep_hits),
                'gitGrepLines': sum(grep_hits.values()),
                'pyRegexFiles': len(py_hits),
                'pyRegexHits': sum(py_hits.values()),
                'methodsAgreeOnFiles': sorted(grep_hits) == sorted(py_hits),
                'wrappedCitationOnlyFiles': wrapped_only,
                'filesByCategory': by_cat,
            })
        records.append({'kind': kind, 'id': subject, 'tokens': per_token})
    result = {
        'tool': 'consumer_sweep.py',
        'treeCommit': commit,
        'trackedFiles': len(tracked),
        'textFilesRead': len(text),
        'subjects': records,
    }
    out.write_text(json.dumps(result, indent=1) + '\n', encoding='utf-8')
    for r in records:
        for t in r['tokens']:
            cats = ', '.join(f'{k}={len(v)}' for k, v in sorted(t['filesByCategory'].items()))
            print(f"{r['kind']:15} {t['token'][:70]:70} files={t['pyRegexFiles']:3} agree={t['methodsAgreeOnFiles']} wrapped={t['wrappedCitationOnlyFiles']} | {cats}")
    print(f'tracked={len(tracked)} read={len(text)} commit={commit}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
