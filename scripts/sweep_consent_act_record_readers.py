#!/usr/bin/env python3
"""Which production sources name the consent-gate census's act records, and which records carry a recording tag (syzygy-bpyt.8.10).
Evidence tool, not a check and not authority.

usage: python3 -I scripts/sweep_consent_act_record_readers.py TREE --out OUT.json [--remote NAME]

TREE is a git checkout. Everything is read at its HEAD commit through git, never from the working tree. The records are the ones
`docs/evidence/consent-gate-recognition-models-2026-10-21.json` lists; the population is every tracked `.ts` file under `packages/`
or `apps/` whose name does not end `.test.ts`, `.testkit.ts` or `.d.ts`. Three line sweeps run over it:

- literal: the line holds a record's file name;
- constructed: the line holds a template piece `<PREFIX>${...}<SUFFIX>` (PREFIX a run of capitals, digits and hyphens ending in a
  hyphen, SUFFIX a hyphen, such a run and `.md`) that a record's file name fills with a stem, and the same file holds that stem as a
  quoted string literal;
- decisions: the line holds the word `decisions`, the records' directory. A source that reads a record by enumerating the directory
  names no record and is found only here; the sweep lists these and does not decide what they read.

For each record it also reads every `- recording tag:` line (the form the PWB owner-act parser reads in a Ceremony section) and
compares the record's blob at the tag's commit with its blob at HEAD; with --remote, it also asks that remote for the tag. Writes only
OUT.json; source lines are recorded by number, never copied."""
import hashlib, json, re, subprocess, sys

CENSUS = 'docs/evidence/consent-gate-recognition-models-2026-10-21.json'
SCRIPT = 'scripts/sweep_consent_act_record_readers.py'
TEMPLATE = re.compile(r'([A-Z0-9][A-Z0-9-]*-)\$\{[^}]*\}(-[A-Z0-9-]*\.md)')
DECISIONS = re.compile(r'\bdecisions\b')
TAG_LINE = re.compile(r'^\s*- recording tag: `([^`]+)`', re.M)

args = sys.argv[1:]
if len(args) < 3 or '--out' not in args: sys.exit(__doc__.split('\n\n')[1])
tree, out_path = args[0], args[args.index('--out') + 1]
remote = args[args.index('--remote') + 1] if '--remote' in args else None
sha = lambda b: hashlib.sha256(b).hexdigest()

def git(*a, check=True):
    r = subprocess.run(['git', '-C', tree, *a], capture_output=True)
    if check and r.returncode != 0: sys.exit(f"git {' '.join(a)} failed: {r.stderr.decode().strip()}")
    return r

def show(rev_path): return git('show', rev_path).stdout

def rev(spec):
    r = git('rev-parse', '--verify', '--quiet', spec, check=False)
    return r.stdout.decode().strip() if r.returncode == 0 else None

head = rev('HEAD^{commit}')
census = json.loads(show(f'HEAD:{CENSUS}'))
records = [{'path': r['path'], 'model': r['model'], 'family': r['family']} for r in census['records']]
names = {r['path'].rsplit('/', 1)[1]: r['path'] for r in records}

listing = [p for p in git('ls-tree', '-r', '-z', '--name-only', 'HEAD', '--', 'packages', 'apps').stdout.decode().split('\0') if p]
population = sorted(p for p in listing if p.endswith('.ts') and not p.endswith(('.test.ts', '.testkit.ts', '.d.ts')))
literal, constructed, decisions = [], [], {}
for src in population:
    lines = show(f'HEAD:{src}').decode('utf8').split('\n')
    for n, line in enumerate(lines, 1):
        for name, path in names.items():
            if name in line: literal.append({'file': src, 'line': n, 'record': path})
        if DECISIONS.search(line): decisions.setdefault(src, []).append(n)
        for prefix, suffix in TEMPLATE.findall(line):
            for name, path in names.items():
                if not (name.startswith(prefix) and name.endswith(suffix) and len(name) > len(prefix) + len(suffix)): continue
                stem = name[len(prefix):len(name) - len(suffix)]
                quoted = [f"'{stem}'", f'"{stem}"', f'`{stem}`']
                for m, other in enumerate(lines, 1):
                    if any(q in other for q in quoted):
                        constructed.append({'file': src, 'templateLine': n, 'stemLine': m, 'stem': stem, 'record': path})

by_record = {r['path']: {'literal': sorted({h['file'] for h in literal if h['record'] == r['path']}),
                         'constructed': sorted({h['file'] for h in constructed if h['record'] == r['path']})} for r in records}
naming = sorted({h['file'] for h in literal} | {h['file'] for h in constructed})
named = [p for p, v in by_record.items() if v['literal'] or v['constructed']]

remote_tags = None
if remote is not None:
    r = subprocess.run(['git', '-C', tree, 'ls-remote', '--tags', remote], capture_output=True, text=True)
    if r.returncode != 0: sys.exit(f'git ls-remote {remote} failed: {r.stderr.strip()}')
    remote_tags = {}
    for row in r.stdout.splitlines():
        oid, ref = row.split('\t')
        if ref.endswith('^{}'): remote_tags[ref[len('refs/tags/'):-3]] = oid
        else: remote_tags.setdefault(ref[len('refs/tags/'):], oid)
tags = []
for r in records:
    text = show(f"HEAD:{r['path']}").decode('utf8')
    at_head = rev(f"HEAD:{r['path']}")
    found = TAG_LINE.findall(text)
    if not found: tags.append({'record': r['path'], 'model': r['model'], 'tag': None}); continue
    for tag in found:
        commit = rev(f'refs/tags/{tag}^{{commit}}')
        at_tag = rev(f"{commit}:{r['path']}") if commit else None
        row = {'record': r['path'], 'model': r['model'], 'tag': tag, 'tagCommit': commit, 'blobAtTag': at_tag, 'blobAtHead': at_head,
               'state': 'tag absent' if commit is None else 'record absent at tag' if at_tag is None else 'blob equal' if at_tag == at_head else 'blob differs'}
        if remote_tags is not None: row['remoteCommit'] = remote_tags.get(tag)
        tags.append(row)

out = {
    'schema': 'consent-gate-act-record-readers/1', 'bead': 'syzygy-bpyt.8.10',
    'text': 'Evidence record, not authority: which production sources name the census records, and the census records\' recording tags. Generated by the script named here; do not edit.',
    'script': {'path': SCRIPT, 'sha256': sha(show(f'HEAD:{SCRIPT}'))},
    'measuredOn': {'commit': head, 'readFrom': 'the HEAD commit, through git', 'census': {'path': CENSUS, 'sha256': sha(show(f'HEAD:{CENSUS}'))}},
    'population': {'predicate': 'tracked .ts files under packages/ or apps/, excluding *.test.ts, *.testkit.ts and *.d.ts', 'count': len(population)},
    'methods': {'literal': 'line contains the record file name', 'constructed': f'line matches {TEMPLATE.pattern}, the record file name is PREFIX + stem + SUFFIX, and the file holds the stem quoted', 'decisions': f'line matches {DECISIONS.pattern}'},
    'records': records,
    'literal': literal, 'constructed': constructed,
    'decisionsDirectory': [{'file': f, 'lines': v, 'namesARecord': f in naming} for f, v in sorted(decisions.items())],
    'byRecord': by_record,
    'summary': {'records': len(records), 'recordsNamed': len(named), 'recordsNamedByNoSource': sorted(set(by_record) - set(named)),
                'recordsNamedOnlyByConstruction': sorted(p for p, v in by_record.items() if v['constructed'] and not v['literal']),
                'sourcesNamingARecord': naming, 'sourcesNamingTheDecisionsDirectory': len(decisions),
                'sourcesNamingTheDecisionsDirectoryButNoRecord': sorted(set(decisions) - set(naming))},
    'recordingTags': {'line': TAG_LINE.pattern, 'remote': remote, 'rows': tags},
}
json.dump(out, open(out_path, 'w'), indent=2); open(out_path, 'a').write('\n')
print('population', len(population), 'records', len(records), 'named', len(named), 'sources naming a record', len(naming), 'decisions-directory sources', len(decisions))
for row in tags: print(row['record'].rsplit('/', 1)[1], row.get('tag'), row.get('state'), row.get('remoteCommit') == row.get('tagCommit') if remote_tags is not None and row.get('tag') else '')
