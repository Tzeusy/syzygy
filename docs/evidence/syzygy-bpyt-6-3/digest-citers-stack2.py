#!/usr/bin/env python3
"""Does any tracked file cite the digest of a file this change edits? For syzygy-bpyt.6.3 stack 2 (decodeUtf8 and canonicalJson).

The stack-3 tool of the same name, extended: a file the change adds has no digest at the base and is listed apart, with its head digest
only. Everything else is as there.

Usage: digest-citers-stack2.py <git repo> <base commit> <code head> <population commit> <out.json>
       digest-citers-stack2.py --selftest

The edited files are the production .ts files that differ between the base and the code head. For each, the sha256 of its bytes
at the base and at the code head is computed (never transcribed) and looked for, as the full 64 hex digits and as the first 12,
in every tracked file at the population commit except the directory docs/evidence/syzygy-bpyt-6-3/ (which holds this tool's own output). Method one
reads every blob with Python `bytes.find`; method two is `git grep -F -l` per needle; the two must name the same files.
Prints a JSON summary; exit status 1 when the two methods disagree. A cited digest is reported, not failed: the citers are listed by tree.
"""
import hashlib
import json
import subprocess
import sys

OWN = 'docs/evidence/syzygy-bpyt-6-3/'


def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], capture_output=True, check=True).stdout


def edited_production(repo, base, head):
    names = git(repo, 'diff', '--name-only', '-z', base, head).decode().split('\0')
    return [n for n in names if n.startswith(('packages/', 'apps/')) and '/src/' in n and n.endswith('.ts') and not n.endswith('.test.ts')]


def citers(repo, head, needles):
    files = [f for f in git(repo, 'ls-tree', '-r', '-z', '--name-only', head).decode().split('\0') if f and not f.startswith(OWN)]
    method_one = {n: [] for n in needles}
    for f in files:
        blob = git(repo, 'show', f'{head}:{f}')
        for n in needles:
            if blob.find(n.encode()) >= 0:
                method_one[n].append(f)
    method_two = {}
    for n in needles:
        out = subprocess.run(['git', '-C', repo, 'grep', '-F', '-l', '-e', n, head], capture_output=True, text=True)
        method_two[n] = sorted(l.split(':', 1)[1] for l in out.stdout.splitlines() if not l.split(':', 1)[1].startswith(OWN))
    return files, method_one, method_two


def selftest():
    """A digest that a tracked file does cite must be found by both methods; an absent one by neither."""
    import re
    here = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True, check=True).stdout.strip()
    host = 'docs/evidence/syzygy-bpyt-8-36/summary.json'
    token = re.search(rb'[0-9a-f]{64}', git(here, 'show', f'HEAD:{host}')).group(0).decode()
    absent = hashlib.sha256(b'syzygy-bpyt.6.3 digest-citers: a digest no file cites').hexdigest()
    _, one, two = citers(here, 'HEAD', [token, token[:12], absent])
    ok = host in one[token] and host in one[token[:12]] and sorted(one[token]) == two[token] and sorted(one[token[:12]]) == two[token[:12]] and one[absent] == [] and two[absent] == []
    print(json.dumps({'selftest': 'present digest found by both methods, absent digest by neither', 'host': host, 'pass': ok}))
    sys.exit(0 if ok else 1)


def main():
    if '--selftest' in sys.argv:
        selftest()
    repo, base, head, population, out = sys.argv[1:6]
    edited = edited_production(repo, base, head)
    digests = []
    added = []
    for path in edited:
        for label, commit in (('base', base), ('head', head)):
            if label == 'base' and subprocess.run(['git', '-C', repo, 'cat-file', '-e', f'{base}:{path}'], capture_output=True).returncode != 0:
                added.append(path)
                continue
            digests.append({'path': path, 'at': label, 'sha256': hashlib.sha256(git(repo, 'show', f'{commit}:{path}')).hexdigest()})
    needles = sorted({d['sha256'] for d in digests} | {d['sha256'][:12] for d in digests})
    files, one, two = citers(repo, population, needles)
    hits = {n: v for n, v in one.items() if v}
    agree = all(sorted(one[n]) == two[n] for n in needles)
    citers_by_tree = {}
    for n, cited_by in hits.items():
        for f in cited_by:
            tree = '/'.join(f.split('/')[:2])
            citers_by_tree[tree] = sorted(set(citers_by_tree.get(tree, [])) | {f})
    cited_files = sorted({d['path'] for d in digests if d['sha256'] in hits or d['sha256'][:12] in hits})
    result = {
        'baseCommit': base, 'codeHeadCommit': head, 'populationCommit': population,
        'population': f'{len(files)} tracked files at the population commit, excluding {OWN}',
        'editedProductionFiles': edited, 'addedByTheChange': added, 'digests': digests, 'needles': len(needles),
        'methods': 'one: Python bytes.find over every blob; two: git grep -F -l per needle',
        'methodsAgree': agree, 'needlesCited': hits, 'editedFilesWhoseDigestIsCited': cited_files, 'citersByTree': citers_by_tree,
    }
    json.dump(result, open(out, 'w'), indent=1)
    open(out, 'a').write('\n')
    print(f'edited {len(edited)} files, {len(needles)} needles, {len(files)} files scanned, needles cited {len(hits)} (edited files affected: {len(cited_files)}), methods agree {agree}')
    sys.exit(0 if agree else 1)


if __name__ == '__main__':
    main()
