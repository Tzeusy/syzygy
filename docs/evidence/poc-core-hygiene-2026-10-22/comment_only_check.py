#!/usr/bin/env python3
"""Prove a follow-up commit changed comments only, and that the retained export still resolves.

Usage: comment_only_check.py <tree> <old-commit> <out.json>

For every file under packages/ and apps/ that differs between <old-commit> and the
tree's working files, strips comments from both versions with export_census.py's
lexer and compares them. Then, from the tree's built dist (run `npm run build`
first), checks that dist/evidence-population.js exports derivePopulationBlock and
that the package barrel (dist/index.js) re-exports the same function under the
same name: the retained measurement script requires that dist file by path.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_census import strip_comments  # noqa: E402


def norm(text: str) -> list[str]:
    return [line.rstrip() for line in strip_comments(text).splitlines() if line.strip()]


def main() -> int:
    tree, old, out = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3])
    git = lambda *a: subprocess.run(['git', *a], cwd=tree, capture_output=True, text=True, check=True).stdout
    changed = [p for p in git('diff', '--name-only', old, '--', 'packages', 'apps').splitlines() if p]
    files = []
    for path in changed:
        before, after = git('show', f'{old}:{path}'), (tree / path).read_text(encoding='utf-8')
        files.append({'file': path, 'sha256Before': hashlib.sha256(before.encode()).hexdigest(), 'sha256After': hashlib.sha256(after.encode()).hexdigest(),
                      'identicalAfterCommentStrip': norm(before) == norm(after)})
    script = ("const m = await import(process.argv[1] + '/packages/three-surface-poc-core/dist/evidence-population.js');"
              "const b = await import(process.argv[1] + '/packages/three-surface-poc-core/dist/index.js');"
              "console.log(JSON.stringify({moduleExportsFunction: typeof m.derivePopulationBlock === 'function', barrelReexportsSameFunction: b.derivePopulationBlock === m.derivePopulationBlock}));")
    node = json.loads(subprocess.run(['node', '--input-type=module', '-e', script, str(tree)], capture_output=True, text=True, check=True).stdout)
    record = {
        'tool': 'comment_only_check.py',
        'oldCommit': old,
        'treeCommit': git('rev-parse', 'HEAD').strip(),
        'filesChanged': len(files),
        'allIdenticalAfterCommentStrip': all(f['identicalAfterCommentStrip'] for f in files),
        'files': files,
        'retainedExport': {'distPath': 'packages/three-surface-poc-core/dist/evidence-population.js', 'name': 'derivePopulationBlock', **node},
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    print(f"changed={len(files)} allCommentOnly={record['allIdenticalAfterCommentStrip']} retainedExport={node}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
