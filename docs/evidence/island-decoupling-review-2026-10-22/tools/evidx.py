"""Re-derive every digest evidence.json indexes. records/scripts: each entry's sha256 against the file in the evidence directory at
the reviewed head. subjectFileSha256: each entry against `git show <subject>:<path>`. Usage: evidx.py <repo> <reviewed head>"""
import hashlib, json, pathlib, subprocess, sys
repo, head = sys.argv[1:3]
d_dir = pathlib.Path(repo) / 'docs/evidence/syzygy-bpyt-8-1'
idx = json.loads((d_dir / 'evidence.json').read_text())
sha = lambda b: hashlib.sha256(b).hexdigest()
digest_of = lambda v: v if isinstance(v, str) else v.get('sha256')
show = lambda c, p: subprocess.run(['git', '-C', repo, 'show', f'{c}:{p}'], capture_output=True)
for group in ('records', 'scripts'):
    ok = bad = 0
    for name, v in idx[group].items():
        same = sha((d_dir / name).read_bytes()) == digest_of(v)
        ok += same; bad += not same
        if not same: print('  MISMATCH', group, name)
    print(group, 'entries', len(idx[group]), 'match', ok, 'mismatch', bad)
on_disk = sorted(p.relative_to(d_dir).as_posix() for p in d_dir.rglob('*') if p.is_file())
indexed = set(idx['records']) | set(idx['scripts']) | {'evidence.json'}
print('files in the directory not indexed:', [p for p in on_disk if p not in indexed])
ok = bad = 0
mism = []
for path, v in idx['subjectFileSha256'].items():
    r = show(idx['subjectCommit'], path)
    same = r.returncode == 0 and sha(r.stdout) == digest_of(v)
    ok += same; bad += not same
    if not same: mism.append(path)
print('subjectFileSha256 entries', len(idx['subjectFileSha256']), 'match at subject', ok, 'mismatch', bad, mism[:20])
example = next(iter(idx['records'].values()))
print('record entry shape:', example if isinstance(example, str) else list(example))
