#!/usr/bin/env python3
"""syzygy-bpyt.8.1: does any tracked file pin a line of a file this change edits? For every file that exists at <old> and differs at
<new>, find each citation at <old> of its path, or of its basename, followed by a line locator (`:N`, `:N-M`, `#LN`, `#LN-LM`, and a bare `:N` continuing it), and
say whether the cited lines read the same at <new> and whether the citing file is digest-bound. A locator was accurate at <old> when the
cited lines at <old> equal the same lines at the last commit (at or before <old>) that touched the citing file; only such a locator
can be shifted by this change, and the others were stale before it.
Bound means: under .syzygy/ or openspec/, a retained docs/reviews/*-RAW.md, or a file whose sha256 at <old> some other tracked file
at <old> carries. A basename or path suffix another tracked file also ends with is counted as ambiguous and skipped. Usage: python3 locator_check.py <tree> <old commit> <new commit>   (prints JSON)"""
import hashlib, json, re, subprocess, sys

tree, old, new = sys.argv[1:4]
git = lambda *args: subprocess.run(['git', '-C', tree, *args], capture_output=True, check=False)
rev = lambda c: git('rev-parse', c).stdout.decode().strip()
changed = [f for f in git('diff', '--name-only', old, new).stdout.decode().split('\n') if f]
existing = [f for f in changed if git('cat-file', '-e', f'{old}:{f}').returncode == 0]
tracked = [f for f in git('ls-tree', '-r', '-z', '--name-only', old).stdout.decode().split('\0') if f]
# A cited name pins this target only when no other tracked file ends with it (`index.ts:12` names nothing in particular).
unique = lambda cited: sum(1 for f in tracked if f == cited or f.endswith('/' + cited)) == 1
LOCATOR = r'(?::(\d+)(?:\s*[-–]\s*(\d+))?|#L(\d+)(?:-L?(\d+))?)'
NEXT_PATH = re.compile(r'[\w./@-]+\.\w+(?::\d|#L\d)')
CONTINUATION = re.compile(r'(?<![\w./@-]):(\d+)(?:\s*[-\u2013]\s*(\d+))?(?!\d)')
bound_cache = {}

def bound(path):
    if path not in bound_cache:
        if path.startswith(('.syzygy/', 'openspec/')):
            bound_cache[path] = 'governed plane'
        elif path.startswith('docs/reviews/') and path.endswith('-RAW.md'):
            bound_cache[path] = 'review raw'
        else:
            digest = hashlib.sha256(git('show', f'{old}:{path}').stdout).hexdigest()
            hits = [h.split(':', 1)[1] for h in git('grep', '-l', '-F', digest, old, '--').stdout.decode().split('\n') if h]
            hits = [h for h in hits if h != path]
            bound_cache[path] = f'digest cited by {len(hits)} file(s): ' + ', '.join(sorted(hits)) if hits else None
    return bound_cache[path]

lines_at = lambda commit, path: git('show', f'{commit}:{path}').stdout.decode().split('\n')
authored = {}
def accurate_at_old(citer, target, first, last, old_lines):
    if citer not in authored:
        authored[citer] = git('log', '-1', '--format=%H', old, '--', citer).stdout.decode().strip()
    then = git('show', f'{authored[citer]}:{target}')
    return then.returncode == 0 and then.stdout.decode().split('\n')[first - 1:last] == old_lines[first - 1:last]
rows, ambiguous = [], []
for target in existing:
    base = target.rsplit('/', 1)[-1]
    old_lines, new_lines = lines_at(old, target), lines_at(new, target)
    grep = git('grep', '-n', '-P', re.escape(base) + LOCATOR, old, '--').stdout.decode().split('\n')
    for hit in filter(None, grep):
        _, citer, line_no, text = hit.split(':', 3)
        for m in re.finditer(r'([\w./@-]*' + re.escape(base) + r')' + LOCATOR, text):
            cited = m.group(1)
            if not (target == cited or target.endswith('/' + cited)):
                continue
            if cited != target and not unique(cited):
                ambiguous.append({'target': target, 'citer': citer, 'citerLine': int(line_no), 'locator': m.group(0)})
                continue
            spans = [(m.group(0), 'full path' if cited == target else 'basename' if cited == base else 'path suffix',
                      int(m.group(2) or m.group(4)), int(m.group(3) or m.group(5) or m.group(2) or m.group(4)))]
            # Continuation form (`a.ts:258` and `:270`): a bare `:N` before the next cited path names the same file.
            following = NEXT_PATH.search(text, m.end())
            for c in CONTINUATION.finditer(text, m.end(), following.start() if following else len(text)):
                spans.append((c.group(0), 'continuation', int(c.group(1)), int(c.group(2) or c.group(1))))
            for locator, form, first, last in spans:
                same = old_lines[first - 1:last] == new_lines[first - 1:last] and last <= len(old_lines)
                rows.append({'target': target, 'citer': citer, 'citerLine': int(line_no), 'locator': locator, 'form': form,
                             'citedLinesUnchanged': same, 'accurateAtOld': accurate_at_old(citer, target, first, last, old_lines),
                             'citerBound': bound(citer)})
shifted = [r for r in rows if not r['citedLinesUnchanged'] and r['accurateAtOld']]

def digest_citers(path):
    digest = hashlib.sha256(git('show', f'{old}:{path}').stdout).hexdigest()
    return sorted(h.split(':', 1)[1] for h in git('grep', '-l', '-F', digest, old, '--').stdout.decode().split('\n') if h and h.split(':', 1)[1] != path)

def reviewed_commit(path):
    found = re.search(r'^Reviewed commit:\s*`?([0-9a-f]{7,40})', git('show', f'{old}:{path}').stdout.decode(), re.M)
    return found.group(1) if found else None

RAW_REASON = ('a retained review raw (CC-REV-6 stores it unchanged): its locator names the lines at its own reviewed commit and still '
              'reads them correctly there; it never named the lines of main')
OTHER_REASON = ('a dated snapshot no tracked file cites by digest: its locator names the lines of the tree it was taken from, and the '
                'snapshot is not rewritten to a later tree')
def reads_same_at(commit, r):
    """Whether the cited lines at `commit` equal those at <old>; None when the commit is not in this clone."""
    if commit is None or git('cat-file', '-e', f'{commit}^{{commit}}').returncode != 0:
        return None
    m = re.search(r'(\d+)(?:\s*[-\u2013]\s*L?(\d+))?$', r['locator'])
    first, last = int(m.group(1)), int(m.group(2) or m.group(1))
    then = git('show', f'{commit}:{r["target"]}')
    return then.returncode == 0 and then.stdout.decode().split('\n')[first - 1:last] == lines_at(old, r['target'])[first - 1:last]

table = []
for r in shifted:
    raw = r['citerBound'] == 'review raw'
    reviewed = reviewed_commit(r['citer']) if raw else None
    table.append({'citer': r['citer'], 'citerLine': r['citerLine'], 'locator': r['locator'], 'target': r['target'],
                  'citerClass': 'review raw' if raw else 'governed plane' if r['citerBound'] == 'governed plane' else 'unbound file',
                  'citerDigestCitedBy': digest_citers(r['citer']), 'reviewedCommit': reviewed,
                  'citedLinesAtReviewedCommitEqualOld': reads_same_at(reviewed, r),
                  'citerLastCommit': authored[r['citer']], 'whyNoRepair': RAW_REASON if raw else OTHER_REASON})
print(json.dumps({'old': rev(old), 'new': rev(new), 'changedFiles': len(changed), 'existingAtOld': len(existing),
                  'locators': len(rows), 'ambiguousSkipped': len(ambiguous), 'staleAtOld': sum(1 for r in rows if not r['accurateAtOld']),
                  'shifted': len(shifted), 'shiftedTable': table, 'shiftedRows': shifted,
                  'shiftedInBoundCiters': [r for r in shifted if r['citerBound']],
                  'boundCitersAnyLocator': sorted({r['citer'] for r in rows if r['citerBound']}), 'rows': rows, 'ambiguous': ambiguous}, indent=2))
