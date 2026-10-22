"""Digest citers of the PR's modified files, scanned in a chosen tree. For each file modified between <base> and <head> that exists
at <base>: its <base> sha256 and blob id, and every tracked file at <scan> (other than the file itself, and outside <exclude> if
given) carrying either. Usage: citers_at.py <repo> <base> <head> <scan> [exclude-prefix]"""
import collections, hashlib, subprocess, sys
repo, base, head, scan = sys.argv[1:5]
exclude = sys.argv[5] if len(sys.argv) > 5 else None
git = lambda *a: subprocess.run(['git', '-C', repo, *a], capture_output=True, check=True).stdout
modified = [l.split('\t')[1] for l in git('diff', '--name-status', base, head).decode().splitlines() if l[0] == 'M']
tracked = [t for t in git('ls-tree', '-r', '-z', '--name-only', scan).decode().split('\0') if t and not (exclude and t.startswith(exclude))]
texts = {t: git('show', f'{scan}:{t}').decode('utf8', 'replace') for t in tracked}
cited, records = [], collections.defaultdict(set)
for f in modified:
    blob = git('show', f'{base}:{f}')
    keys = (hashlib.sha256(blob).hexdigest(), git('rev-parse', f'{base}:{f}').decode().strip())
    hits = sorted(t for t, x in texts.items() if t != f and any(k in x for k in keys))
    if hits: cited.append(f)
    for h in hits: records[h].add(f)
print(f'scan {scan}, exclude {exclude}: tracked scanned {len(texts)}; modified files {len(modified)}; with a digest or blob citer {len(cited)}')
print('citing records:', len(records), '| outside docs/evidence/:', sorted(r for r in records if not r.startswith('docs/evidence/')))
print('governed-plane citers:', sorted(r for r in records if r.startswith(('.syzygy/', 'openspec/'))))
for r in sorted(records): print('  ', r, sorted(p.rsplit('/', 1)[-1] for p in records[r]))
