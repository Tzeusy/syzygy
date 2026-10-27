"""syzygy-bpyt.8.39: derive summary.json from the raw outputs beside it, checking each against the git objects of the tree given.

The subject is the code commit HEAD over BASE (main after PR 487): the PR 536 review's notes N1, N2 and N4, and N3's optional comment
clause. Inputs (all in this directory):
  rev536-at-base.json, rev536-at-head.json  all 11 of the PR 536 reviewer's mutants, run unchanged from
                       docs/evidence/guard-pins-followup-review-2026-10-27/rev536-specs.json at BASE and at HEAD, with that
                       reviewer's copy of mut.py (the PR 524 reviewer's runner);
  island-diff.json, island-diff-selftest.json  docs/evidence/syzygy-bpyt-8-36/island_diff.py, old testkit (BASE) against new (HEAD);
  repeat-runs.json, titles.json  docs/evidence/syzygy-bpyt-8-36/repeat.py (the four guard files five times at HEAD) and titles.py
                       (their Vitest titles at both commits);
  comment-only.json    comment_only.cjs here: the testkit's comment-free emit and comment-free print at BASE and HEAD, with its selftest;
  npa-probe.json       npa_probe.cjs here: npm-package-arg's type for every version form the testkit comment and the rows name;
  suite.json           suite_summary.py here, over Vitest JSON reports of both packages' suites in a clean clone at HEAD;
  start-gates-default-reporter.log  the one file that failed by timeout in suite.json, run alone with the default reporter.
The test diff must be exactly the PR 536 reviewer's FIX-rows-only edits (rev536-fix-specs.json) applied to BASE.
repeat-runs.json, titles.json and npa-probe.json carry no commit of their own; each is tied to HEAD by its content: the repeat total is
HEAD's title count, every added title's row is in HEAD's blob and not BASE's, and the probe's pattern line is HEAD's.
Usage: python3 -I record.py <tree> [--check | --selftest]
  --check: exit 1 unless summary.json equals what the inputs give and no check fails.
  --selftest: mutate one input at a time in memory (rule 6) and exit 1 unless every mutation makes a check fail.
"""
import copy, hashlib, json, re, subprocess, sys
from pathlib import Path

TREE = Path(sys.argv[1]).resolve()
HERE_REL = 'docs/evidence/syzygy-bpyt-8-39'
HERE = TREE / HERE_REL
BASE = 'd38d7a3ce632a34c2a41bdb77ad323ba0b05b777'
HEAD = '308a62f4a48e47b625aeff9cc718b1b2c37161f8'
REACH = 'packages/polaris-generation-core/src/workspace-reach.test.ts'
KIT = 'packages/polaris-generation-core/src/workspace-reach.testkit.ts'
CODE = [REACH, KIT]
GUARDS = ['packages/polaris-dossier/src/subpath-imports.test.ts', 'packages/polaris-generation-core/src/island-boundary.test.ts', REACH]
START_GATES = 'packages/polaris-dossier/src/start-gates.test.ts'
REVIEW_DIR = 'docs/evidence/guard-pins-followup-review-2026-10-27'
RUNNER = f'{REVIEW_DIR}/tools/mut.py'
RUNNER_524 = 'docs/evidence/argv-guards-review-2026-10-25/tools/mut.py'
REVIEW_SPECS = f'{REVIEW_DIR}/rev536-specs.json'
FIX_SPECS = f'{REVIEW_DIR}/rev536-fix-specs.json'
TOOLS = {name: f'docs/evidence/syzygy-bpyt-8-36/{name}' for name in ('island_diff.py', 'titles.py', 'repeat.py')}
OWN_TOOLS = ['comment_only.cjs', 'npa_probe.cjs', 'suite_summary.py', 'record.py']
WS = f'{REACH} > the shared workspace resolver > '
NAMING = lambda label: f'{WS}reads a bare name declared as {label} as naming no module'
ROOT_DECLARES = f"{WS}reads a bare name the workspace root's manifest declares as a local dependency as naming no module"
# Each of the review's N1 and N2 targets, and the one new row that must be its only failure at HEAD.
TARGETS = {
    'RV536-M2-http-url-reads-outside': [NAMING('a remote http tarball URL dependency')],
    'RV536-M7-npm-alias-workspace-scope-only': [NAMING('an npm: alias of a registry package')],
    'RV536-M8-root-declarations-unread': [ROOT_DECLARES],
    'RV536-M9-dotdot-alone-outside': [NAMING('a dependency on its parent directory')],
}
# Survivors at both commits, as the review ruled them: M5 and M10 equivalent on the tree, M11 the named 8.38 residual.
RESIDUAL = ['RV536-M5-tree-depth-two', 'RV536-M10-test-exclusion-end-anchor-dropped', 'RV536-M11-residual-widened']
# The 4 titles this bead adds, each with the row literal that must be in HEAD's blob and not in BASE's.
ADDED = {
    ROOT_DECLARES: (REACH, '''  it("reads a bare name the workspace root's manifest declares as a local dependency as naming no module", () => {\n'''),
    **{NAMING(label): (REACH, f"    ['{label}', 'dossier', {{ dependencies: {{ dossier: '{version}' }} }}, {{}}],\n") for label, version in (
        ('a remote http tarball URL dependency', 'http://example.com/lib-1.0.0.tar.gz'), ('an npm: alias of a registry package', 'npm:typescript@^5.5.0'),
        ('a dependency on its parent directory', '..'))},
}
# npm-package-arg's type for each form the testkit comment names, as the comment states it.
CLAIMS = {**{f: 'directory' for f in ('file:../x', '.', '..', './x', '../x', '/x', '~/x')}, **{f: 'file' for f in ('x.tgz', 'x.tar', 'x.tar.gz')},
          'link:../x': 'throws EUNSUPPORTEDPROTOCOL', 'workspace:*': 'throws EUNSUPPORTEDPROTOCOL', 'npm:@syzygy/lib@*': 'alias',
          'npm:typescript@^5.5.0': 'alias', 'https://example.com/x.tgz': 'remote', 'http://example.com/x.tgz': 'remote',
          'github:someone/dossier#v1.tar': 'git', 'git+https://example.com/lib.tgz': 'git'}
# The comment's N4 premise: npm takes only a registry spec after `npm:`, and refuses any other.
REGISTRY_TYPES = {'range', 'version', 'tag'}
NOT_REGISTRY_ALIASES = ['npm:./lib', 'npm:file:../lib']
NAMED_IN_COMMENT = ['`npm:`', '`github:someone/dossier#v1.tar`', '`https://…/x.tgz`', 'npm-package-arg 12.0.2 accepts only a registry spec after `npm:`']
RESIDUAL_FORMS = ['packages/polaris-dossier/', '.hidden-lib', 'a/b/c']
OUTSIDE_VERSIONS = ['2.9.0', '^1.0.0', 'github:someone/dossier', '~1.2.3', 'git+https://example.com/lib.tgz.git']
LOCAL_VERSION = re.compile(r'^(?:file:|link:|workspace:|npm:|\.\.?(?:/|$)|/|~/)|\.(?:tgz|tar|tar\.gz)$', re.I)
STRACE_SKIP = 'no provider call and no transmission (S10), without strace is not proved on this host'
MUTATE = {}


def git(*args):
    return subprocess.run(['git', '-C', str(TREE), *args], check=True, capture_output=True, text=True).stdout


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def blob(commit, path, cache={}):
    key = (commit, path)
    if key not in cache:
        try:
            cache[key] = git('show', f'{commit}:{path}')
        except subprocess.CalledProcessError:
            cache[key] = None
    return cache[key]


def load(name):
    obj = json.loads((HERE / name).read_text())
    return MUTATE[name](copy.deepcopy(obj)) if name in MUTATE else obj


def hooked(key, value):
    """A git-derived value, which --selftest may replace through MUTATE['@<key>']."""
    return MUTATE[f'@{key}'](value) if f'@{key}' in MUTATE else value


def row(line):
    """A mut.py FAIL line, less its project: `<file> > <describe> > <title>`."""
    match = re.fullmatch(r'FAIL\s+\S+\s+(\S.*)', line.strip())
    return match.group(1) if match else line


def check_runs(name, commit, specs, problems):
    d = load(name)
    if d['head'] != commit:
        problems.append(f'{name}: ran at {d["head"]}, not {commit}')
    rows = {}
    for r in d['results']:
        spec = specs.get(r['id'])
        if spec is None:
            problems.append(f'{name} {r["id"]}: no such spec')
            continue
        if r.get('edits') != spec['edits']:
            problems.append(f'{name} {r["id"]}: edits differ from the spec')
        for e in spec['edits']:
            if 'old' in e and (blob(commit, e['file']) or '').count(e['old']) != 1:
                problems.append(f'{name} {r["id"]}: old fragment does not occur once in {e["file"]} at {commit[:8]}')
        expected = 'survives' if r.get('exit') == 0 else ('killed' if r.get('failed') else 'error')
        if r.get('outcome') != expected:
            problems.append(f'{name} {r["id"]}: outcome {r.get("outcome")} disagrees with exit {r.get("exit")} and {len(r.get("failed", []))} failed rows')
        if r.get('timeouts'):
            problems.append(f'{name} {r["id"]}: {r["timeouts"]} timeouts, so a failure may be load, not the mutant')
        if not r.get('cleanAfter'):
            problems.append(f'{name} {r["id"]}: tree not clean after')
        rows[r['id']] = {'outcome': r.get('outcome'), 'failedRows': sorted(row(f) for f in r.get('failed', [])), 'tests': r.get('tests')}
    missing = sorted(set(specs) - set(rows))
    if missing:
        problems.append(f'{name}: {len(missing)} specs never ran: {missing[:3]}')
    return rows


def diff_lines(path):
    """Every changed line of `path`, BASE to HEAD, as (sign, line number on its side, text)."""
    out, old, new = [], None, None
    for line in git('diff', '-U0', BASE, HEAD, '--', path).splitlines():
        hunk = re.match(r'@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@', line)
        if hunk:
            old, new = int(hunk.group(1)), int(hunk.group(2))
        elif old is None:
            continue  # the header, before the first hunk
        elif line.startswith('-'):
            out.append(['-', old, line[1:]])
            old += 1
        elif line.startswith('+'):
            out.append(['+', new, line[1:]])
            new += 1
    return hooked(f'lines {path}', out)


def doc_comment_span(text):
    """The 1-based first and last lines of the doc comment directly above `const LOCAL_VERSION`."""
    lines = text.splitlines()
    at = [i for i, line in enumerate(lines) if line.startswith('const LOCAL_VERSION = ')]
    if len(at) != 1 or not lines[at[0] - 1].endswith('*/'):
        return None
    start = max(i for i in range(at[0]) if lines[i].startswith('/**'))
    if any('*/' in line for line in lines[start:at[0] - 1]):
        return None
    return start + 1, at[0]


def apply_fix(text, edits, problems):
    for e in edits:
        if e['file'] != REACH or text.count(e['old']) != 1:
            problems.append(f'fix: an edit is not to {REACH} or its old text does not occur once at BASE')
            continue
        text = text.replace(e['old'], e['new'])
    return text


def main_summary():
    problems = []
    review = {m['id']: m for m in json.loads(blob(HEAD, REVIEW_SPECS) or '{"mutants": []}')['mutants']}
    if blob(BASE, REVIEW_SPECS) != blob(HEAD, REVIEW_SPECS) or len(review) != 11:
        problems.append('the reviewer specs differ between BASE and HEAD, or are not 11')
    base = check_runs('rev536-at-base.json', BASE, review, problems)
    head = check_runs('rev536-at-head.json', HEAD, review, problems)
    for i, own_rows in TARGETS.items():
        b, h = base.get(i, {}), head.get(i, {})
        if (b.get('outcome'), h.get('outcome')) != ('survives', 'killed'):
            problems.append(f'{i}: {b.get("outcome")} at base, {h.get("outcome")} at head')
        if h.get('failedRows') != own_rows:
            problems.append(f'{i}: killed at head by {h.get("failedRows")}, not by its own row alone')
    for i in RESIDUAL:
        if (base.get(i, {}).get('outcome'), head.get(i, {}).get('outcome')) != ('survives', 'survives'):
            problems.append(f'{i}: the residual is not a survivor at both commits')
    compare = {'stronger': [], 'unchanged': [], 'weaker': []}
    for i in sorted(set(review) - set(TARGETS) - set(RESIDUAL)):
        b, h = base.get(i), head.get(i)
        if b is None or h is None:
            continue
        if b['outcome'] != 'killed' or h['outcome'] != 'killed' or not set(b['failedRows']) <= set(h['failedRows']):
            compare['weaker'].append(i)
        else:
            compare['stronger' if set(h['failedRows']) > set(b['failedRows']) else 'unchanged'].append(i)
    if compare['weaker']:
        problems.append(f'weaker at head, or not killed at base: {compare["weaker"]}')

    fix = {m['id']: m for m in json.loads(blob(HEAD, FIX_SPECS) or '{"mutants": []}')['mutants']}.get('FIX-rows-only', {'edits': []})
    fixed = hooked('fixed', apply_fix(blob(BASE, REACH) or '', fix['edits'], problems))
    if not fix['edits'] or fixed != blob(HEAD, REACH):
        problems.append("fix: HEAD's test file is not the reviewer's FIX-rows-only edits applied to BASE")
    reach_lines = diff_lines(REACH)
    if any(sign == '-' for sign, _, _ in reach_lines):
        problems.append(f'{REACH}: the subject removes a line')

    kit_lines = diff_lines(KIT)
    spans = {'-': doc_comment_span(blob(BASE, KIT) or ''), '+': doc_comment_span(blob(HEAD, KIT) or '')}
    outside = [line for line in kit_lines if spans[line[0]] is None or not spans[line[0]][0] < line[1] < spans[line[0]][1]
               or not re.match(r' \* ', line[2])]
    if not kit_lines or outside:
        problems.append(f'testkit: a changed line is not a ` * ` line inside the LOCAL_VERSION doc comment: {outside[:1]}')
    only = load('comment-only.json')
    st = only.get('selftest', {})
    if (only['file'], only['base'], only['head'], only['baseSha256'], only['headSha256'], only['bytesDiffer'], only['emitEqual'], only['printEqual']) \
            != (KIT, BASE, HEAD, sha(blob(BASE, KIT) or ''), sha(blob(HEAD, KIT) or ''), True, True, True):
        problems.append("comment-only: not BASE's and HEAD's testkit, or the comment-free emit or print differs")
    if st.get('identifierRenamed') != {'emitEqual': False, 'printEqual': False} or st.get('literalChanged') != {'emitEqual': False, 'printEqual': False} \
            or st.get('commentAdded') != {'emitEqual': True, 'printEqual': True}:
        problems.append('comment-only: the selftest does not separate a code change from a comment change')

    diff, selftest = load('island-diff.json'), load('island-diff-selftest.json')
    tool = sha(blob(HEAD, TOOLS['island_diff.py']) or '')
    for d, label in ((diff, 'island-diff'), (selftest, 'island-diff-selftest')):
        if (d['base'], d['head'], d['cleanAfter'], d['vitestExit'], d['toolSha256']) != (BASE, HEAD, True, 0, tool):
            problems.append(f'{label}: base, head, clean tree, exit or tool digest is not as required')
    if diff['selftest'] or diff['walks']['equal'] != diff['walks']['entries'] or diff['resolves']['equal'] != diff['resolves']['specifiers'] \
            or diff['walks']['unequal'] or diff['resolves']['unequal']:
        problems.append('island-diff: an answer differs')
    if not selftest['selftest'] or selftest['walks']['equal'] == selftest['walks']['entries'] or selftest['resolves']['equal'] == selftest['resolves']['specifiers']:
        problems.append('island-diff-selftest: the mutated testkit changed no answer')

    titles = load('titles.json')
    added = [f'{f} > {n}' for f, n in titles['addedNames']]
    per_file = titles['perFile']
    if titles['removed'] or titles['removedNames'] or titles['added'] != len(added) or titles['head'] - titles['base'] != len(added) \
            or sum(v['base'] for v in per_file.values()) != titles['base'] or sum(v['head'] for v in per_file.values()) != titles['head'] \
            or titles['duplicatesBase'] or titles['duplicatesHead']:
        problems.append('titles: a title was removed, the arithmetic does not close, or a title is duplicated')
    if sorted(added) != sorted(ADDED):
        problems.append(f'titles: added {sorted(set(added) ^ set(ADDED))[:2]} beyond or short of the 4 rows this bead adds')
    for title, (path, fragment) in ADDED.items():
        if (blob(HEAD, path) or '').count(fragment) != 1 or fragment in (blob(BASE, path) or ''):
            problems.append(f'titles: the row of {title.rsplit(" > ", 1)[-1]!r} is not new at HEAD')
    repeat = load('repeat-runs.json')
    if len(repeat['runs']) < 5 or any(r['exit'] or r['failed'] or r['passed'] != r['total'] or r['total'] != titles['head'] for r in repeat['runs']):
        problems.append("repeat-runs: fewer than 5 ran, a run failed, or a total is not HEAD's title count")

    probe = load('npa-probe.json')
    pattern = [line for line in (blob(HEAD, KIT) or '').splitlines() if line.startswith('const LOCAL_VERSION = ')]
    base_pattern = [line for line in (blob(BASE, KIT) or '').splitlines() if line.startswith('const LOCAL_VERSION = ')]
    if probe['pattern'] != (pattern[0] if len(pattern) == 1 else None) or pattern != base_pattern or probe['npaVersion'] != '12.0.2':
        problems.append("npa-probe: not HEAD's pattern line, the pattern moved since BASE, or not npm-package-arg 12.0.2")
    comment = {r['spec']: r for r in probe['comment']}
    for form, kind in CLAIMS.items():
        if (comment.get(form, {}).get('npa'), comment.get(form, {}).get('local')) != (kind, True):
            problems.append(f'npa-probe: {form} is not {kind} and refused')
    aliases = [r for r in [*probe['comment'], *probe['rows']] if r['npa'] == 'alias']
    if not aliases or any(r.get('aliasOf') not in REGISTRY_TYPES for r in aliases) \
            or any(comment.get(form, {}).get('npa') != 'throws aliases only work for registry deps' for form in NOT_REGISTRY_ALIASES):
        problems.append('npa-probe: npm takes an alias of a spec that is not a registry spec')
    for words in NAMED_IN_COMMENT:
        if words not in (blob(HEAD, KIT) or ''):
            problems.append(f'testkit comment: does not name {words}')
    for form in RESIDUAL_FORMS:
        if (comment.get(form, {}).get('npa'), comment.get(form, {}).get('local')) != ('directory', False) or f'`{form}`' not in (blob(HEAD, KIT) or ''):
            problems.append(f'npa-probe: the residual {form} is not a directory npm reads that the pattern leaves outside, named in the comment')
    for r in probe['rows']:
        if f": '{r['spec']}' }}" not in (blob(HEAD, REACH) or '') or r['local'] != (r['spec'] not in OUTSIDE_VERSIONS):
            problems.append(f'npa-probe: the row version {r["spec"]} is not in HEAD\'s rows, or sits on the wrong side')
    if sorted(r['spec'] for r in probe['rows'] if not r['local']) != sorted(OUTSIDE_VERSIONS):
        problems.append('npa-probe: the outside rows are not the five controls')

    suite = load('suite.json')
    runs = {r['label']: r for r in suite['runs']}
    full, lifted, alone, alone_lifted = (runs.get(k, {}) for k in ('full', 'full-timeout-60s', 'start-gates-alone', 'start-gates-timeout-60s'))
    if suite['commit'] != HEAD or not suite['cleanAfter'] or sorted(runs) != ['full', 'full-timeout-60s', 'start-gates-alone', 'start-gates-timeout-60s']:
        problems.append('suite: not a clean tree at HEAD, or not the four runs')
    skips = lambda r: [t for t in r.get('notPassed', []) if t['status'] != 'failed']
    for r in (full, lifted):
        if r.get('files') != 55 or r.get('total') != r.get('passed', 0) + r.get('failed', 0) + r.get('skipped', 0) \
                or len(skips(r)) != 1 or not skips(r)[0]['name'].startswith(STRACE_SKIP) or skips(r)[0]['status'] != 'skipped':
            problems.append(f'suite {r.get("label")}: totals do not close, or a test other than the strace capture did not run')
    if not lifted.get('success') or lifted.get('failed') or lifted.get('total') != full.get('total'):
        problems.append('suite: the run with a 60 s test timeout failed, or ran another population')
    timed_out = sorted(t['name'] for t in full.get('notPassed', []) if t['status'] == 'failed')
    if any(t['file'] != START_GATES or t['ms'] < 5000 for t in full.get('notPassed', []) if t['status'] == 'failed'):
        problems.append(f'suite: the full run failed outside {START_GATES}, or before the 5 s timeout')
    if not timed_out or not set(timed_out) <= {t['name'] for t in alone.get('notPassed', []) if t['status'] == 'failed'} \
            or any(t['ms'] < 5000 for t in alone.get('notPassed', [])) or not alone_lifted.get('success') or alone_lifted.get('notPassed') \
            or alone_lifted.get('total') != alone.get('total'):
        problems.append('suite: the full run\'s failures do not recur alone by timeout, or the file fails with a 60 s timeout')
    log = (HERE / 'start-gates-default-reporter.log').read_text()
    if HEAD not in log.splitlines()[0] or log.count('Error: Test timed out in 5000ms.') != len([t for t in alone.get('notPassed', []) if t['status'] == 'failed']) \
            or 'Tests  2 failed | 102 passed (104)' not in log:
        problems.append('start-gates log: not at HEAD, or its failures are not the timeouts of the run alone')
    gates = hooked('start-gates', blob(HEAD, START_GATES) or '')
    if 'workspace-reach' in gates:
        problems.append(f'{START_GATES}: imports a file the subject changes')

    runner = sha(blob(HEAD, RUNNER) or '')
    if runner != sha(blob(HEAD, RUNNER_524) or 'x'):
        problems.append("the mutant runner is not the PR 524 reviewer's mut.py")
    changed = hooked('names', git('diff', '--name-only', BASE, HEAD).split())
    if sorted(changed) != sorted(CODE):
        problems.append(f'the subject touches {changed}, not the two files')
    importers = hooked('importers', sorted(line.split(':', 1)[1] for line in git('grep', '-l', '-F', 'workspace-reach.testkit', HEAD, '--',
                                                                                 'apps', 'packages', 'scripts').split()))
    if importers != sorted(GUARDS):
        problems.append(f'the testkit is imported by {importers}, not the three guard tests')
    tracked = [p for p in git('ls-tree', '-r', '--name-only', '-z', HEAD).split('\0') if p]
    manifests = [p for p in tracked if p == 'package.json' or re.fullmatch(r'(?:apps|packages)/[^/]+/package\.json', p)]
    versions = [[p, field, name, version] for p in manifests for field in ('dependencies', 'devDependencies', 'optionalDependencies', 'peerDependencies')
                for name, version in json.loads(blob(HEAD, p)).get(field, {}).items()]
    return {
        'bead': 'syzygy-bpyt.8.39', 'base': BASE, 'head': HEAD,
        'subject': {'what': f'git diff {BASE[:8]} {HEAD[:8]}', 'sha256': sha(git('diff', BASE, HEAD)),
                    'files': {f: {'base': sha(blob(BASE, f)), 'head': sha(blob(HEAD, f))} for f in CODE}},
        'productFilesChanged': [f for f in changed if f not in CODE],
        'testkitImporters': importers,
        'mutRunnerSha256': runner,
        'targets': {i: {'base': base.get(i, {}).get('outcome'), 'head': head.get(i, {}).get('outcome'),
                        'headFailedRows': head.get(i, {}).get('failedRows')} for i in [*TARGETS, *RESIDUAL]},
        'otherReviewMutants': compare,
        'fix': {'specs': FIX_SPECS, 'specsSha256': sha(blob(HEAD, FIX_SPECS) or ''), 'edits': len(fix['edits']), 'headEqualsBaseWithFix': fixed == blob(HEAD, REACH),
                'linesAdded': len(reach_lines), 'linesRemoved': 0},
        'testkit': {'changedLines': {'-': sum(1 for l in kit_lines if l[0] == '-'), '+': sum(1 for l in kit_lines if l[0] == '+')},
                    'docCommentLines': {'base': spans['-'], 'head': spans['+']},
                    'emitEqual': only['emitEqual'], 'printEqual': only['printEqual'], 'typescript': only['typescript'], 'selftest': st},
        'islandDiff': {'walks': {k: diff['walks'][k] for k in ('entries', 'equal', 'answersSha256')},
                       'resolves': {k: diff['resolves'][k] for k in ('files', 'specifiers', 'equal', 'byAnswer', 'answersSha256')},
                       'selftest': {'walksEqual': selftest['walks']['equal'], 'resolvesEqual': selftest['resolves']['equal']}, 'toolSha256': tool},
        'repeats': {'runs': len(repeat['runs']), 'passed': [r['passed'] for r in repeat['runs']], 'load1': [r['load1'] for r in repeat['runs']]},
        'titles': {'base': titles['base'], 'head': titles['head'], 'added': len(added), 'removed': titles['removed'], 'perFile': per_file,
                   'line': f'Tests: +{len(added)} ~0 -{titles["removed"]}'},
        'npaProbe': {'npaVersion': probe['npaVersion'], 'node': probe['node'], 'forms': len(probe['comment']) + len(probe['rows'])},
        'suite': {r['label']: {k: r[k] for k in ('total', 'passed', 'failed', 'skipped', 'load1Before', 'load1After')} for r in suite['runs']},
        'suiteTimeouts': timed_out,
        'tools': {**{name: sha(blob(HEAD, path) or '') for name, path in TOOLS.items()},
                  **{name: sha((HERE / name).read_text()) for name in OWN_TOOLS}},
        'faithfulTree': {'manifests': len(manifests), 'dependencyVersions': len(versions),
                         'local': [v for v in versions if LOCAL_VERSION.search(v[3])],
                         'bareDirectoryShaped': [v for v in versions if ':' not in v[3] and ('/' in v[3] or v[3].startswith('.')) and not LOCAL_VERSION.search(v[3])]},
        'problems': problems,
    }


def first(d, i):
    return next(r for r in d['results'] if r['id'] == i)


def kill(r, rows=('FAIL   @syzygy/x  packages/x/src/x.test.ts > x > y',)):
    r.update(outcome='killed', exit=1, failed=list(rows))


def run(d, label):
    return next(r for r in d['runs'] if r['label'] == label)


SELFTEST = {
    'a target that survives at head': {'rev536-at-head.json': lambda d: (first(d, 'RV536-M8-root-declarations-unread').update(outcome='survives', exit=0, failed=[]), d)[1]},
    'a target killed at base': {'rev536-at-base.json': lambda d: (kill(first(d, 'RV536-M2-http-url-reads-outside')), d)[1]},
    'a target killed by another row too': {'rev536-at-head.json': lambda d: (first(d, 'RV536-M7-npm-alias-workspace-scope-only')['failed'].append('FAIL   @syzygy/x  ' + ROOT_DECLARES), d)[1]},
    'a target never run at base': {'rev536-at-base.json': lambda d: (d.update(results=[r for r in d['results'] if r['id'] != 'RV536-M9-dotdot-alone-outside']), d)[1]},
    'a residual killed at head': {'rev536-at-head.json': lambda d: (kill(first(d, 'RV536-M5-tree-depth-two')), d)[1]},
    'a base kill lost at head': {'rev536-at-head.json': lambda d: (first(d, 'RV536-M6-root-keeps-only-dependencies').update(outcome='survives', exit=0, failed=[]), d)[1]},
    'a base kill with a row lost at head': {'rev536-at-head.json': lambda d: (first(d, 'RV536-M3-tarball-needs-dot-slash')['failed'].pop(0), d)[1]},
    'a run at another commit': {'rev536-at-head.json': lambda d: (d.update(head=BASE), d)[1]},
    'a run with a timeout': {'rev536-at-head.json': lambda d: (first(d, 'RV536-M1-https-url-reads-outside').update(timeouts=1), d)[1]},
    'an outcome that disagrees with its exit': {'rev536-at-base.json': lambda d: (first(d, 'RV536-M4-census-takes-ts-md').update(exit=0), d)[1]},
    'a run whose edits are not its spec': {'rev536-at-base.json': lambda d: (first(d, 'RV536-M2-http-url-reads-outside')['edits'][0].update(new='x'), d)[1]},
    'a tree left dirty': {'rev536-at-head.json': lambda d: (first(d, 'RV536-M10-test-exclusion-end-anchor-dropped').update(cleanAfter=False), d)[1]},
    "a test file that is not the reviewer's fix": {'@fixed': lambda text: text.replace("'..'", "'../'", 1)},
    'a line removed from the test file': {f'@lines {REACH}': lambda lines: [*lines, ['-', 90, "    ['a ./ path dependency', ..."]]},
    'a code line changed in the testkit': {f'@lines {KIT}': lambda lines: [*lines, ['+', 70, 'const LOCAL_VERSION = /^file:/iu;']]},
    'a comment line changed outside the doc comment': {f'@lines {KIT}': lambda lines: [*lines, ['+', 3, ' * x']]},
    'a comment-free emit that differs': {'comment-only.json': lambda d: (d.update(emitEqual=False), d)[1]},
    'a comment-only check of another blob': {'comment-only.json': lambda d: (d.update(headSha256='0' * 64), d)[1]},
    'a comment-only selftest that misses a rename': {'comment-only.json': lambda d: (d['selftest']['identifierRenamed'].update(printEqual=True), d)[1]},
    'a walk that differs': {'island-diff.json': lambda d: (d['walks'].update(equal=d['walks']['equal'] - 1), d)[1]},
    'an island diff by another tool': {'island-diff.json': lambda d: (d.update(toolSha256='0' * 64), d)[1]},
    'a differential selftest that changes nothing': {'island-diff-selftest.json': lambda d: (d['resolves'].update(equal=d['resolves']['specifiers']), d['walks'].update(equal=d['walks']['entries']), d)[2]},
    'a repeat run that fails': {'repeat-runs.json': lambda d: (d['runs'][2].update(failed=['x'], passed=d['runs'][2]['passed'] - 1), d)[1]},
    "a repeat run of BASE's population": {'repeat-runs.json': lambda d: ([r.update(total=165, passed=165) for r in d['runs']], d)[1]},
    'a title removed': {'titles.json': lambda d: (d.update(removed=1), d['removedNames'].append([REACH, 'x']), d)[2]},
    'an added title this bead does not add': {'titles.json': lambda d: (d['addedNames'][0].__setitem__(1, 'x > y'), d)[1]},
    'a probe of another pattern': {'npa-probe.json': lambda d: (d.update(pattern=d['pattern'].replace('tgz|', '')), d)[1]},
    'a comment claim npm does not make': {'npa-probe.json': lambda d: (next(r for r in d['comment'] if r['spec'] == 'github:someone/dossier#v1.tar').update(npa='remote'), d)[1]},
    'an alias of a path that npm takes': {'npa-probe.json': lambda d: (next(r for r in d['comment'] if r['spec'] == 'npm:./lib').update(npa='alias', aliasOf='directory'), d)[1]},
    'an alias of a non-registry spec': {'npa-probe.json': lambda d: (next(r for r in d['rows'] if r['spec'] == 'npm:typescript@^5.5.0').update(aliasOf='git'), d)[1]},
    'a residual the pattern refuses': {'npa-probe.json': lambda d: (next(r for r in d['comment'] if r['spec'] == 'a/b/c').update(local=True), d)[1]},
    'a row version on the wrong side': {'npa-probe.json': lambda d: (next(r for r in d['rows'] if r['spec'] == '..').update(local=False), d)[1]},
    'a suite at another commit': {'suite.json': lambda d: (d.update(commit=BASE), d)[1]},
    'a lifted-timeout suite with a failure': {'suite.json': lambda d: (run(d, 'full-timeout-60s').update(success=False, failed=1, passed=run(d, 'full-timeout-60s')['passed'] - 1), d)[1]},
    'a full-suite failure in another file': {'suite.json': lambda d: (run(d, 'full')['notPassed'].append({'file': REACH, 'name': 'x', 'status': 'failed', 'ms': 9000, 'error': ''}), d)[1]},
    'a full-suite failure before the timeout': {'suite.json': lambda d: (next(t for t in run(d, 'full')['notPassed'] if t['status'] == 'failed').update(ms=40), d)[1]},
    'a start-gates file that fails with a 60 s timeout': {'suite.json': lambda d: (run(d, 'start-gates-timeout-60s').update(success=False), d)[1]},
    'a full suite that skips another test': {'suite.json': lambda d: (run(d, 'full')['notPassed'].append({'file': REACH, 'name': 'y', 'status': 'skipped', 'ms': None, 'error': ''}), d)[1]},
    'a start-gates file that imports the testkit': {'@start-gates': lambda text: text + "\nimport './workspace-reach.testkit.js';\n"},
    'a product file in the subject': {'@names': lambda names: [*names, 'packages/polaris-dossier/src/argv.ts']},
    'a product module importing the testkit': {'@importers': lambda names: sorted([*names, 'apps/syzygy/src/main.ts'])},
}


def main():
    if '--selftest' in sys.argv[2:]:
        if main_summary()['problems']:
            print('selftest: the unmutated inputs already fail')
            sys.exit(1)
        survived = []
        for label, mutation in SELFTEST.items():
            MUTATE.clear()
            MUTATE.update(mutation)
            problems = main_summary()['problems']
            print('killed' if problems else 'SURVIVED', '|', label, '|', problems[:1])
            if not problems:
                survived.append(label)
        MUTATE.clear()
        print(f'selftest: {len(SELFTEST) - len(survived)}/{len(SELFTEST)} mutations make a check fail')
        sys.exit(1 if survived else 0)
    text = json.dumps(main_summary(), indent=1, ensure_ascii=False) + '\n'
    summary = json.loads(text)
    if '--check' in sys.argv[2:]:
        same = (HERE / 'summary.json').read_text() == text
        print('summary.json', 'matches' if same else 'DIFFERS', '; problems:', len(summary['problems']))
        sys.exit(0 if same and not summary['problems'] else 1)
    (HERE / 'summary.json').write_text(text)
    print('wrote summary.json; problems:', len(summary['problems']))
    for p in summary['problems']:
        print(' -', p)


main()
