#!/usr/bin/env python3
"""syzygy-bpyt.8.1: is any file this change edits bound by digest? For every file that exists at <old> and differs at <new>, hash its
<old> bytes and list each tracked file at <old> that carries that sha256, classed by where it sits.
Usage: python3 digest_citers.py <tree> <old commit> <new commit>   (prints JSON)"""
import hashlib, json, subprocess, sys

tree, old, new = sys.argv[1:4]
git = lambda *args: subprocess.run(['git', '-C', tree, *args], capture_output=True, check=False)
changed = [f for f in git('diff', '--name-only', old, new).stdout.decode().split('\n') if f]
klass = lambda path: ('governed plane' if path.startswith(('.syzygy/', 'openspec/')) else 'evidence record' if path.startswith('docs/evidence/')
                      else 'review raw' if path.startswith('docs/reviews/') else 'other')
rows, added = [], []
for path in changed:
    blob = git('show', f'{old}:{path}')
    if blob.returncode != 0:
        added.append(path)
        continue
    digest = hashlib.sha256(blob.stdout).hexdigest()
    hits = git('grep', '-l', '-F', digest, old, '--').stdout.decode().split('\n')
    citers = sorted(h.split(':', 1)[1] for h in hits if h)
    rows.append({'file': path, 'oldSha256': digest, 'citers': [{'path': c, 'class': klass(c)} for c in citers]})
classes = sorted({c['class'] for r in rows for c in r['citers']})
print(json.dumps({'old': git('rev-parse', old).stdout.decode().strip(), 'new': git('rev-parse', new).stdout.decode().strip(),
                  'changedFiles': len(changed), 'existingAtOld': len(rows), 'addedFiles': added,
                  'citedFiles': sum(1 for r in rows if r['citers']), 'citerClasses': classes,
                  'governedPlaneCiters': [c['path'] for r in rows for c in r['citers'] if c['class'] == 'governed plane'], 'rows': rows}, indent=2))
