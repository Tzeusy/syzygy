#!/usr/bin/env python3
"""Assemble export-census-2026-10-22.json from fresh census runs.

Usage: assemble_census.py <head-tree> <base-tree> <previous-record.json> <out.json>

Runs export_census.py and orphans.py on both trees (default and --raw modes),
computes the un-export list from the two export sets, the .py consumer sweep by
two methods, the test-only buckets and every denominator, and carries over only
the hand-judged prose fields of <previous-record.json> (the record as reviewed
at 4f3c3ebf, retrievable with `git show`). Nothing countable is typed in.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEAD, BASE = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
PREVIOUS = json.loads(Path(sys.argv[3]).read_text())
OUT = Path(sys.argv[4])
APP = 'apps/three-surface-poc/src/'
EXCLUDED = {APP + 'polaris.ts', APP + 'polaris-generation/public-source-screening.ts'}
DELETED_FILE = APP + 'polaris-generation/source-adapter.ts'
DELETED_NAMES = {(APP + 'polaris-narrative.ts', 'MAX_ANCHORS_PER_BLOCK')}
scratch = Path(tempfile.mkdtemp(prefix='zz-assemble-census-'))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(tree: Path, *args: str) -> str:
    return subprocess.run(['git', '-C', str(tree), *args], capture_output=True, text=True, check=True).stdout


def census(tree: Path, raw: bool) -> tuple[list[dict], str]:
    out = scratch / f"{tree.name}-{'raw' if raw else 'default'}.json"
    cmd = [sys.executable, str(HERE / 'export_census.py'), str(tree), '--json', str(out)] + (['--raw'] if raw else [])
    line = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return json.loads(out.read_text()), line


def counts(rows: list[dict]) -> dict:
    return dict(sorted(Counter(r['class'] for r in rows).items()))


head_rows, head_line = census(HEAD, False)
base_rows, base_line = census(BASE, False)
head_raw, _ = census(HEAD, True)
base_raw, _ = census(BASE, True)
key = lambda r: (r['file'], r['name'])
head_set, base_set = {key(r) for r in head_rows}, {key(r) for r in base_rows}
short = lambda k: f"{k[0][len(APP):]}:{k[1]}"

# Denominators, with their definitions (N3).
files_scanned = lambda tree: int(re.search(r'declaring files: (\d+)', census_line[tree]).group(1))
census_line = {BASE: base_line, HEAD: head_line}
denominators = {
    'definition': {
        'filesScanned': 'tracked non-test .ts files under apps/three-surface-poc/src (export_census.py "declaring files": every file the census parses for export declarations)',
        'filesWithAtLeastOneExport': 'the files among those that declare one or more exports (distinct `file` values among the census rows)',
    },
    'base': {'filesScanned': files_scanned(BASE), 'filesWithAtLeastOneExport': len({r['file'] for r in base_rows}), 'exports': len(base_rows)},
    'head': {'filesScanned': files_scanned(HEAD), 'filesWithAtLeastOneExport': len({r['file'] for r in head_rows}), 'exports': len(head_rows)},
}

# Un-export list: exports at base absent at head, less the deleted file and the deleted constant.
gone = sorted(base_set - head_set)
deleted_file_names = [k for k in gone if k[0] == DELETED_FILE]
deleted_constants = [k for k in gone if k in DELETED_NAMES]
unexported = [k for k in gone if k[0] != DELETED_FILE and k not in DELETED_NAMES]
previous_names = PREVIOUS['dispositions']['unexportedSelfOnly']['names']
assert sorted(short(k) for k in unexported) == sorted(previous_names), 'the un-export list differs from the reviewed record'
added_exports = sorted(head_set - base_set)

# The diff that removed the keywords: reachable commits on both ends.
base_commit, head_commit = git(BASE, 'rev-parse', 'HEAD').strip(), git(HEAD, 'rev-parse', 'HEAD').strip()
diff = git(HEAD, 'diff', '--unified=0', '--no-color', base_commit, head_commit, '--', APP,
           f':(exclude){APP}main.ts', f':(exclude){APP}poc-main.ts', f':(exclude){APP}main.test.ts',
           f':(exclude){DELETED_FILE}', f':(exclude){APP}polaris-generation/source-adapter.test.ts')
removed_lines = [ln[1:] for ln in diff.splitlines() if ln.startswith('-') and not ln.startswith('---')]
added_lines = Counter(ln[1:] for ln in diff.splitlines() if ln.startswith('+') and not ln.startswith('+++'))
keyword_removals = sum(1 for ln in removed_lines if ln.startswith('export ') and not re.match(r'export (type )?\{', ln) and added_lines[ln[len('export '):]] > 0)
list_edits = sum(1 for ln in removed_lines if re.match(r'export (type )?\{', ln))

# .py consumers of the un-exported names: two methods.
py_files = [f for f in git(HEAD, 'ls-files', '-z').split('\0') if f.endswith('.py') and not f.startswith('docs/evidence/')]
names = sorted({k[1] for k in unexported} | {k[1] for k in DELETED_NAMES})
token = re.compile(r'[A-Za-z_$][\w$]*')
token_hits = []
for f in py_files:
    present = set(token.findall((HEAD / f).read_text(encoding='utf-8', errors='replace')))
    token_hits += [(f, n) for n in names if n in present]
names_file = scratch / 'names.txt'
names_file.write_text('\n'.join(names) + '\n')
grep = subprocess.run(['git', '-C', str(HEAD), 'grep', '-n', '-w', '-F', '-f', str(names_file), '--', '*.py', ':(exclude)docs/evidence'], capture_output=True, text=True)
assert grep.returncode in (0, 1)
grep_hits = grep.stdout.splitlines()
py_sweep = {
    'population': f'{len(py_files)} tracked .py files (git ls-files) at {head_commit[:8]}, less the .py files under docs/evidence/ (measurement tooling that names the exports it measures)',
    'names': len(names),
    'methodTokens': 'Python re [A-Za-z_$][\\w$]* tokens of each file, name in token set',
    'methodGitGrep': "git grep -n -w -F -f <names> -- '*.py'",
    'hitsByTokens': len(token_hits),
    'hitsByGitGrep': len(grep_hits),
    'newlyFoundConsumers': sorted({n for _, n in token_hits}),
    'exportKeywordsRestored': [],
}
assert not token_hits and not grep_hits, ('a script consumes an un-exported name; restore its export', token_hits[:5], grep_hits[:5])

# Un-exported types named in a still-exported declaration of the same file (N4).
unexported_types = []
named_in_signature = []
for f, n in unexported:
    base_text = (BASE / f).read_text()
    if not re.search(rf'^export\s+(?:interface|type)\s+{re.escape(n)}\b', base_text, re.M):
        continue
    unexported_types.append(short((f, n)))
    head_text = (HEAD / f).read_text()
    if re.search(rf'^export\s+(?:declare\s+)?(?:async\s+)?(?:function|const|type|interface|class)\b[^\n]*\b{re.escape(n)}\b', head_text, re.M):
        named_in_signature.append(short((f, n)))

# Test-only buckets at head.
def seam_comment_above(path: str, line: int) -> bool:
    lines = (HEAD / path).read_text().splitlines()
    i = line - 2
    while i >= 0 and lines[i].strip().startswith(('/**', '*', '*/', '//', '/*')):
        if 'Test seam' in lines[i]:
            return True
        i -= 1
    return False


buckets = Counter()
unbucketed = []
for r in head_rows:
    if r['class'] != 'test-only':
        continue
    f = r['file']
    if f in EXCLUDED:
        buckets['untouched by constraint (polaris.ts, public-source-screening.ts)'] += 1
    elif f.split('/')[-1].startswith('test-'):
        buckets['test-support module, one module-head comment'] += 1
    elif f.endswith('pwb-mutation.ts'):
        buckets['mutation runner, not edited beyond un-exports'] += 1
    elif seam_comment_above(f, r['line']):
        buckets['own Test seam comment'] += 1
    else:
        unbucketed.append(short(key(r)))
        buckets['UNBUCKETED'] += 1

orph = {}
for label, tree in (('before', BASE), ('after', HEAD)):
    text = subprocess.run([sys.executable, str(HERE / 'orphans.py'), str(tree)], capture_output=True, text=True, check=True).stdout.splitlines()
    summary = [ln for ln in text if ln.startswith('# modules:')][0]
    listed = [ln.split()[0] for ln in text if ' prod=0 ' in ln]
    orph[label] = {'line': summary, 'noNonTestImporter': listed}

tools = {name: {'sha256': sha(HERE / name)} for name in ('export_census.py', 'orphans.py', 'deexport.py', 'assemble_census.py')}
record = {
    'subject': {
        'baseCommit': base_commit,
        'ranAtCommit': head_commit,
        'note': 'counts below are computed by assemble_census.py from tracked files of the two trees; the base is the main branch the PR merged (b7697f6a at the repair), the head is the tree the scripts ran on',
    },
    'tools': tools,
    'method': (
        'export_census.py: enumerate tracked non-test .ts files under apps/three-surface-poc/src, parse top-level export declarations and export lists with Python re, '
        'then count identifier-token matches of each exported name in (prod) every other tracked non-test code file anywhere in the repository (.ts .mts .mjs .js .cjs and .py; '
        'a .py file counts as a consumer because three governance scripts parse TypeScript declarations by their literal text, and its comments are kept; .py files under docs/evidence/ are measurement tooling and are not consumers), '
        '(test) every tracked *.test.* file, (self) the declaring file beyond the declaration. Classes: dead (no use anywhere), self-only, test-only, prod. '
        'Default mode strips C-style comments first (not from .py files) and keeps string text; --raw skips comment stripping. '
        'Policy for types: a type named in an exported signature stays private by design when no other file names it, and is re-exported when the first caller needs to name one; '
        'this is a code-quality choice, not a defect (typesNamedInExportedSignature counts the affected types). '
        'The un-export list is the set difference of the two exports (base minus head) less the deleted adapter file and the deleted constant.'
    ),
    'denominators': denominators,
    'before': {'exports': len(base_rows), 'classes': counts(base_rows), 'rawModeClasses': counts(base_raw)},
    'after': {'exports': len(head_rows), 'classes': counts(head_rows), 'rawModeClasses': counts(head_raw)},
    'defaultVsRawDisagreements': {
        'base': sorted(short(key(r)) for r in base_rows if next(x for x in base_raw if key(x) == key(r))['class'] != r['class']),
        'head': sorted(short(key(r)) for r in head_rows if next(x for x in head_raw if key(x) == key(r))['class'] != r['class']),
    },
    'dispositions': {
        'unexportedSelfOnly': {
            'count': len(unexported),
            'selfOnlyInDeletedFile': [short(k) for k in deleted_file_names],
            'exportKeywordRemovalsInDiff': keyword_removals,
            'exportListEditsInDiff': list_edits,
            'diffMethod': f'git diff --unified=0 {base_commit[:8]} {head_commit[:8]} over the app src minus main.ts, poc-main.ts, main.test.ts and the deleted adapter pair (both commits are reachable from the PR branch): removed lines that start with export and reappear without it, plus removed export-list lines',
            'handBuiltException': 'governance-inputs.ts readText was unexported by editing the export list, not by the script',
            'selfOnlyAtBaseThatGainedAUserFromTheNewMainAndItsTest': sorted(
                short(key(r)) for r in base_rows if r['class'] == 'self-only' and key(r) in head_set and next(x for x in head_rows if key(x) == key(r))['class'] != 'self-only'
            ),
            'names': sorted(short(k) for k in unexported),
            'pyConsumerSweep': py_sweep,
        },
        'typesNamedInExportedSignature': {
            'method': 'for each type or interface un-exported by the PR, a whole-word match in the same file on a line that starts a still-exported function, const, type, interface or class declaration',
            'unexportedTypes': len(unexported_types),
            'namedInAStillExportedDeclaration': len(named_in_signature),
            'names': sorted(named_in_signature),
        },
        'newExportsAtHead': [short(k) for k in added_exports],
        'testOnlyAfter': dict(buckets),
        'testOnlyUnbucketed': unbucketed,
        'remainingSelfOnlyOrDead': sorted(f"{short(key(r))} ({r['class']})" for r in head_rows if r['class'] in ('self-only', 'dead')),
        'deletedDead': [f"{short(k)} (git grep -n -F over the whole repository found only its declaration)" for k in sorted(deleted_constants)],
        'misclassifiedDeadByDefaultMode': PREVIOUS['dispositions']['misclassifiedDeadByDefaultMode'],
    },
    'orphanSweep': {
        'method': PREVIOUS['orphanSweep']['method'],
        'before': orph['before'],
        'after': orph['after'],
        'deleted': PREVIOUS['orphanSweep']['deleted'],
        'keptWithReason': PREVIOUS['orphanSweep']['keptWithReason'],
    },
}
OUT.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({'denominators': denominators, 'before': record['before']['classes'], 'after': record['after']['classes'], 'unexported': len(unexported),
                  'keywordRemovals': keyword_removals, 'listEdits': list_edits, 'testOnlyAfter': dict(buckets), 'orphans': {k: v['line'] for k, v in orph.items()}}, indent=1))
