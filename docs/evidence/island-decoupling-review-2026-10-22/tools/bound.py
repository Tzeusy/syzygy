"""Bound-record sweep (rev-510). For each file the PR modifies that exists at the base: its base sha256 and git blob id, every
tracked file at the head citing either (full 64/40 hex), and every tracked file under .syzygy/ or openspec/ or any *MANIFEST* file
naming its path. Also: renamed or deleted files. Usage: bound.py <repo> <base> <head>"""
import hashlib, re, subprocess, sys, collections
repo, base, head = sys.argv[1:4]
git = lambda *a: subprocess.run(['git', '-C', repo, *a], capture_output=True, check=True).stdout
status = git('diff', '--name-status', '-M', base, head).decode().splitlines()
kinds = collections.Counter(line.split('\t')[0][0] for line in status)
print('name-status kinds:', dict(kinds))
for line in status:
    if line[0] in 'RDC': print('  ', line)
modified = [line.split('\t')[1] for line in status if line[0] == 'M']
print('modified files existing at base:', len(modified))
tracked = git('ls-tree', '-r', '-z', '--name-only', head).decode().split('\0')
tracked = [t for t in tracked if t]
texts = {}
for t in tracked:
    try: texts[t] = git('show', f'{head}:{t}').decode('utf8', 'replace')
    except subprocess.CalledProcessError: pass
print('tracked files scanned at head:', len(texts))
governed = lambda t: t.startswith('.syzygy/') or t.startswith('openspec/') or 'MANIFEST' in t
cited = 0
rows = []
for f in modified:
    blob = git('show', f'{base}:{f}')
    s256 = hashlib.sha256(blob).hexdigest()
    oid = git('rev-parse', f'{base}:{f}').decode().strip()
    d_citers = sorted(t for t, x in texts.items() if s256 in x)
    o_citers = sorted(t for t, x in texts.items() if oid in x)
    p_citers = sorted(t for t, x in texts.items() if governed(t) and f in x)
    if d_citers or o_citers: cited += 1
    rows.append((f, d_citers, o_citers, p_citers))
for f, d, o, p in rows:
    gov_d = [t for t in d + o if governed(t)]
    print(f'{f}: sha256-citers {len(d)} blob-citers {len(o)} governed-digest-citers {gov_d} governed-path-citers {p}')
    for t in d + o:
        if not t.startswith('docs/evidence/'): print('     non-evidence citer:', t)
print('files with any digest or blob citer:', cited, 'of', len(modified))
