#!/usr/bin/env python3
"""Compare the emitted code of two built trees, comments stripped.

Usage: dist_code_diff.py <base-tree> <head-tree> <out.json>

For every built project (the ten `tsc -b` projects of `npm run build`) this
reads each `*.js` and `*.d.ts` under `<project>/dist` in both trees, drops
comments with the lexer in export_census.py (same directory), drops blank lines
and trailing blanks, and compares line by line. The record lists every file
that differs after stripping with its added and removed lines, and every file
present in only one tree. Source maps and tsbuildinfo are not compared.
"""
import difflib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_census import strip_comments  # noqa: E402

PROJECTS = [
    'packages/cap1-core', 'packages/cap1-daemon', 'packages/cap1-conformance', 'packages/three-surface-poc-core',
    'apps/syzygy', 'apps/three-surface-poc', 'packages/cap1-system', 'packages/polaris-generation-core',
    'packages/polaris-generation-consent', 'packages/polaris-dossier',
]


def emitted(tree: Path, project: str) -> dict[str, list[str]]:
    dist = tree / project / 'dist'
    out: dict[str, list[str]] = {}
    for path in sorted(dist.rglob('*')):
        if path.is_file() and (path.name.endswith('.js') or path.name.endswith('.d.ts')):
            lines = [line.rstrip() for line in strip_comments(path.read_text(encoding='utf-8')).splitlines()]
            out[str(path.relative_to(dist))] = [line for line in lines if line.strip()]
    return out


def tree_state(tree: Path) -> dict:
    git = lambda *args: subprocess.run(['git', *args], cwd=tree, capture_output=True, text=True, check=True).stdout.strip()
    return {'commit': git('rev-parse', 'HEAD'), 'trackedFilesModified': git('status', '--porcelain', '--untracked-files=no') != ''}


def main() -> int:
    base, head, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    projects = []
    for project in PROJECTS:
        a, b = emitted(base, project), emitted(head, project)
        differing = []
        for name in sorted(set(a) & set(b)):
            if a[name] != b[name]:
                delta = [line for line in difflib.unified_diff(a[name], b[name], lineterm='', n=0) if not line.startswith(('---', '+++', '@@'))]
                differing.append({'file': name, 'removedOrAddedLines': delta})
        projects.append({
            'project': project,
            'filesCompared': len(set(a) & set(b)),
            'onlyInBase': sorted(set(a) - set(b)),
            'onlyInHead': sorted(set(b) - set(a)),
            'differingAfterCommentStrip': differing,
        })
    record = {
        'tool': 'dist_code_diff.py',
        'baseTree': tree_state(base),
        'headTree': tree_state(head),
        'projects': projects,
        'filesCompared': sum(p['filesCompared'] for p in projects),
        'filesDiffering': sum(len(p['differingAfterCommentStrip']) for p in projects),
        'filesInOnlyOneTree': sum(len(p['onlyInBase']) + len(p['onlyInHead']) for p in projects),
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    print(f"compared={record['filesCompared']} differing={record['filesDiffering']} inOnlyOneTree={record['filesInOnlyOneTree']}")
    for p in projects:
        for d in p['differingAfterCommentStrip']:
            print(f"  {p['project']}/dist/{d['file']}: {d['removedOrAddedLines']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
