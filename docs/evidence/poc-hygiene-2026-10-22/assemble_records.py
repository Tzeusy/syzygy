#!/usr/bin/env python3
"""Assemble the differential, route-capture and verification records from the
raw runs of this repair, and copy the raw run outputs next to them.

Usage: assemble_records.py <tree> <base-commit> <runs-dir> <evidence-dir>

<runs-dir> holds the raw outputs named below (see RUNS). Every count is
computed here from them; the only prose is method text and the equivalence
arguments for mutants that survive the differential by construction.
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

TREE, BASE, RUNS, OUT = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]).resolve(), Path(sys.argv[4]).resolve()
HERE = Path(__file__).resolve().parent
SRC = 'apps/three-surface-poc/src/'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.run(['git', '-C', str(TREE), *args], capture_output=True, text=True, check=True).stdout.strip()


def load(name: str):
    return json.loads((RUNS / name).read_text())


def canonical_sha(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def line_matching(path: Path, pattern: str) -> str:
    found = [ln.strip() for ln in path.read_text(encoding='utf-8').splitlines() if re.search(pattern, ln)]
    assert len(found) == 1, (path.name, pattern, len(found))
    return found[0]


HEAD = git('rev-parse', 'HEAD')
BASE_FULL = git('rev-parse', BASE)
OUT.mkdir(parents=True, exist_ok=True)

# Raw outputs kept as records.
for source, target in {
    'transcripts.json': 'main-differential-transcripts-2026-10-22.json',
    'main-test-mutants.json': 'main-test-mutants-2026-10-22.json',
    'limb-isolation.json': 'limb-isolation-2026-10-22.json',
    'forms.json': 'invocation-forms-2026-10-22.json',
    'forms-control.json': 'invocation-forms-control-reviewed-commit-2026-10-22.json',
    'dist-compare.json': 'dist-compare-2026-10-22.json',
    'capture-head.json': 'route-capture-fixtures-2026-10-22.json',
    'test-lists.json': 'test-lists-2026-10-22.json',
}.items():
    shutil.copyfile(RUNS / source, OUT / target)

# --- main differential --------------------------------------------------
transcripts = load('transcripts.json')
mutants = load('differential-mutants.json')
diff_run = load('transcripts.run.json')
scenarios = []
for t in transcripts:
    old, new = t['old'], t['new']
    assert old == new and t['entryEqualsOld'] is True
    scenarios.append({
        'name': t['name'], 'exitCode': old['exitCode'], 'thrown': old['thrown'], 'collaboratorCalls': len(old['calls']),
        'stdoutBytes': len(old['stdout']), 'stderrBytes': len(old['stderr']), 'postStartResponses': len(old['after']),
        'oldTranscriptSha256': canonical_sha(old), 'newMainTranscriptSha256': canonical_sha(new), 'newEntryEqualsOld': t['entryEqualsOld'],
    })
distinct = len({s['oldTranscriptSha256'] for s in scenarios})
survivors = [r['id'] for r in mutants['results'] if r['outcome'] != 'killed']
EQUIVALENT = {
    'observer-read-at-process-cwd': 'equivalent under the harness: it fixes process.cwd and io.cwd to the same value because the composition root defines io.cwd as process.cwd(); killed by main.test.ts, which gives the two different values',
    'model-observer-root-process-cwd': 'same reason; killed by main.test.ts',
    'observation-instant-from-clock': 'equivalent under the harness: Date is faked to the instant io.now returns, and the composition root defines io.now as new Date().toISOString(); killed by main.test.ts, which injects a distinct clock',
}
assert set(survivors) <= set(EQUIVALENT), survivors
main_test = load('main-test-mutants.json')
killed_by_main_test = {r['id'] for r in main_test['results'] if r['outcome'] == 'killed'}
assert set(survivors) <= killed_by_main_test
differential = {
    'subject': {
        'oldMain': {'commit': BASE_FULL, 'path': SRC + 'main.ts', 'sha256': diff_run['oldMainSha256']},
        'newMain': {'ranAtCommit': HEAD, 'path': SRC + 'poc-main.ts', 'sha256': sha(TREE / SRC / 'poc-main.ts')},
        'newEntry': {'ranAtCommit': HEAD, 'path': SRC + 'main.ts', 'sha256': sha(TREE / SRC / 'main.ts')},
    },
    'harness': {
        'file': 'docs/evidence/poc-hygiene-2026-10-22/main-old-vs-new-differential.test.ts.txt',
        'sha256': diff_run['harnessSha256'],
        'runner': 'docs/evidence/poc-hygiene-2026-10-22/run_differential.py',
        'runnerSha256': sha(HERE / 'run_differential.py'),
        'reproduce': 'python3 run_differential.py <worktree> <base-commit> <transcripts-out.json> [--mutants <out.json>]: it copies the harness to apps/three-surface-poc/src/zz-main-differential.test.ts, writes the base commit main.ts to zz-main-old.ts, runs npx vitest run on the harness, and deletes both afterwards; they are never committed.',
        'method': 'Per scenario the old script runs as a module (top level, process.argv, process.stdout, process.cwd, process.stdin, signals), the new exported main in poc-main.ts runs with a fake PocIo, and the new entry main.ts runs as a module the same way as the old script, all against the same mocked collaborators (git observation, production model builder, daemon). The three transcripts (stdout, stderr, exit code, ordered collaborator calls, daemon options and route list, post-start route responses, close count, thrown error) must be deeply equal.',
        'scenarios': len(scenarios),
        'identical': sum(1 for s in scenarios if s['newEntryEqualsOld']),
        'distinctTranscripts': distinct,
        'tests': diff_run['run']['tests'],
        'testsPassed': diff_run['run']['passed'],
    },
    'scenarios': scenarios,
    'rule6': {
        'ranAtCommit': mutants['ranAtCommit'],
        'command': mutants['command'],
        'mutatedFile': mutants['mutatedFile'],
        'mutatedFileSha256AtCommit': mutants['mutatedFileSha256AtCommit'],
        'mutants': mutants['mutants'],
        'killed': mutants['killed'],
        'results': [{'id': r['id'], 'old': r['old'], 'new': r['new'], 'outcome': r['outcome'], 'testsRun': r['testsRun'], 'failing': r['failing']} for r in mutants['results']],
        'survivorsExplained': {i: EQUIVALENT[i] for i in survivors},
    },
    'transcriptsFile': 'main-differential-transcripts-2026-10-22.json',
}
(OUT / 'main-differential-2026-10-22.json').write_text(json.dumps(differential, indent=1) + '\n')

# --- route capture --------------------------------------------------------
base_1, base_2, head_cap = load('capture-base-1.json'), load('capture-base-2.json'), load('capture-head.json')
fixture = load('fixture-repo.json')
flat = lambda cap: {f'{v} {k}': r for v, rec in cap.items() for k, r in rec['routes'].items()}
fb, fh = flat(base_1), flat(head_cap)
assert set(fb) == set(fh)
statuses = {}
for r in fh.values():
    statuses[str(r['status'])] = statuses.get(str(r['status']), 0) + 1
bodies_per_key = {}
for key in {k.split(' ', 1)[1] for k in fh}:
    bodies_per_key[key] = len({fh[f'{v} {key}']['bodySha256'] for v in head_cap})
capture_record = {
    'subject': {'baseCommit': BASE_FULL, 'ranAtCommit': HEAD},
    'tool': {'path': 'docs/evidence/poc-hygiene-2026-10-22/route-capture.mjs', 'sha256': sha(HERE / 'route-capture.mjs')},
    'method': 'For each of five fixture models (shape not evaluated, admitted, rejected, with a secret, with a baseline spec) the app route set main.ts registers (pocRoutes, materializeRoutes, reobserveRoutes) is served on a private daemon (--port 0, scratch state directory, never port 7478) and every route is requested in its direct and tailnet Host forms, with and without the machine bearer for machine-credentialed routes, recording status, content type, body length and body sha256 (scratch paths and the port masked). Credentialed POSTs are not sent. No observed repository is read: every model comes from the app fixtures, on one fixed fixture repository path so the evaluation inputs digest is stable.',
    'fixtureRepository': {
        'path': fixture['repoRoot'],
        'revision': fixture['revision'],
        'creation': 'first run only: fixtureRepoWithGit([]) from apps/three-surface-poc/dist/test-model-fixture.js builds a git repository from eight fixed files with pinned commit instants (GIT_AUTHOR_DATE and GIT_COMMITTER_DATE 2026-08-24T00:00:00Z) and no global or system git config, so its revision is a function of the files alone; the script copies it to the path above and writes the revision to <path>.json; later runs reuse the path',
        'comparability': 'the evaluation inputs digest inside the page bodies includes the repository root, so a capture reproduces the digests below only when run with this exact path (rm -rf the path and its .json to recreate it; the revision above is then reproduced)',
        'revisionRecreated': load('fixture-recreated.json')['revision'] == fixture['revision'],
    },
    'denominator': {'variants': len(head_cap), 'routesPerVariant': sorted({r['routeCount'] for r in head_cap.values()}), 'responsesCompared': len(fh)},
    'result': {
        'baseRunsByteIdentical': sha(RUNS / 'capture-base-1.json') == sha(RUNS / 'capture-base-2.json'),
        'headEqualsBaseByteForByte': sha(RUNS / 'capture-base-1.json') == sha(RUNS / 'capture-head.json'),
        'responsesDiffering': sum(1 for k in fb if fb[k] != fh[k]),
        'baseCaptureSha256': sha(RUNS / 'capture-base-1.json'),
        'headCaptureSha256': sha(RUNS / 'capture-head.json'),
        'statusHistogram': dict(sorted(statuses.items())),
        'distinctBodies': len({r['bodySha256'] for r in fh.values()}),
        'fixtureVariantsPairwiseDistinct': len({canonical_sha(rec) for rec in head_cap.values()}) == len(head_cap),
        'requestKeysByDistinctBodyCount': {str(n): sum(1 for c in bodies_per_key.values() if c == n) for n in sorted(set(bodies_per_key.values()))},
    },
    'captureFile': 'route-capture-fixtures-2026-10-22.json',
    'limits': 'The capture covers the route handlers; the process banner, exit codes and the order of collaborator calls that main owns are covered by the old-vs-new differential, and the invocation forms by invocation-forms-2026-10-22.json. The live Butlers page text is not captured (the daemon accepts only the registered Butlers locator and no repository body may be read).',
}
(OUT / 'route-capture-2026-10-22.json').write_text(json.dumps(capture_record, indent=1) + '\n')

# --- verification ---------------------------------------------------------
forms, control, dist, lists, limb = load('forms.json'), load('forms-control.json'), load('dist-compare.json'), load('test-lists.json'), load('limb-isolation.json')
changed = git('diff', '--name-only', BASE_FULL, 'HEAD').split()
gates = RUNS
test_failures = [r['id'] for r in main_test['results'] if r['outcome'] != 'killed']
assert not test_failures, test_failures
verification = {
    'subject': {
        'baseCommit': BASE_FULL,
        'ranAtCommit': HEAD,
        'note': 'every run named here ran on the ranAtCommit tree; the pushed head differs from it only by files under docs/evidence/poc-hygiene-2026-10-22/ (this record set)',
    },
    'roundOneRepairs': [
        {'finding': 'F1', 'repair': 'the entry-script guard is removed: main, serveBoundRepository, PocIo, PocMainDeps and REAL_DEPS live in poc-main.ts (no import-time effect) and main.ts is the unconditional entry', 'shownBy': ['invocation-forms-2026-10-22.json', 'invocation-forms-control-reviewed-commit-2026-10-22.json', 'main-differential-2026-10-22.json']},
        {'finding': 'F2(a)', 'repair': 'the PR body states classes 1 (P1 repository-binding composition) and 3 (PocRuntimeCapture composition), citing R-GP-IMPL-POC-APP-HYGIENE-1', 'shownBy': ['PR body']},
        {'finding': 'F2(b)', 'repair': 'main.test.ts throws a bare PocObservationError and one with a detail and no artifact path, with literal expected stderr', 'shownBy': ['main-test-mutants-2026-10-22.json: suffix-filter-dropped']},
        {'finding': 'F2(c)', 'repair': 'the suffix-filter predicate has a recorded mutant, killed with its first error lines', 'shownBy': ['main-test-mutants-2026-10-22.json: suffix-filter-dropped']},
        {'finding': 'F2(d)', 'repair': 'alteredProseLimb below maps the limb to the emitted-JS identity of the record-reading modules', 'shownBy': ['dist-compare-2026-10-22.json']},
        {'finding': 'F2(e)', 'repair': 'the owner notice is posted by the coordinator at landing', 'shownBy': []},
        {'finding': 'N1', 'repair': 'the two governance-inputs comments are parse anchors naming the scripts; the census counts .py consumers and found none for the 162 un-exported or deleted names', 'shownBy': ['export-census-2026-10-22.json: dispositions.unexportedSelfOnly.pyConsumerSweep']},
        {'finding': 'N2', 'repair': 'the fake daemon creates its state directory and refuses to start, so a bypassed gate fails fast and the existsSync limb can fail', 'shownBy': ['limb-isolation-2026-10-22.json']},
        {'finding': 'N3', 'repair': 'the census diff cites reachable commits, the route-capture record names the fixture repository path, revision and creation, the denominators are defined, every record names ranAtCommit', 'shownBy': ['export-census-2026-10-22.json', 'route-capture-2026-10-22.json']},
        {'finding': 'N4', 'repair': 'the census method states the policy: types named in an exported signature stay private by design and are re-exported when the first caller needs one', 'shownBy': ['export-census-2026-10-22.json: method']},
        {'finding': 'N5', 'repair': 'the --watch test waits with vi.waitFor, the no-watch test waits two event-loop turns and asserts the call log, and each exported type carries one seam note', 'shownBy': ['main.test.ts', 'main-test-mutants-2026-10-22.json: console-attached-without-watch']},
    ],
    'testNames': {
        'method': 'npx vitest list (all projects) at the base commit (a separate worktree with its own npm ci) and at the ranAtCommit; the two lists are compared as multisets of the full "[project] file > describe > test" line',
        **{k: lists[k] for k in ('baseLines', 'headLines', 'baseDistinctNames', 'headDistinctNames', 'added', 'removed', 'addedByFile', 'removedByFile', 'testsLine')},
    },
    'filesChangedBaseToHead': len(changed),
    'fullVitestRun': {
        'command': 'npx vitest run',
        'testFiles': line_matching(gates / 'vitest-full.log', r'^\s*Test Files\s'),
        'tests': line_matching(gates / 'vitest-full.log', r'^\s*Tests\s'),
        'exitLine': line_matching(gates / 'vitest-full.log', r'^exit='),
    },
    'checkGovernance': {
        'baseLastLine': (gates / 'governance-base.txt').read_text().strip().splitlines()[-1],
        'headLastLine': (gates / 'governance-head.txt').read_text().strip().splitlines()[-1],
    },
    'checkQuotations': {'baseVsHeadOutputIdentical': (gates / 'quotations-base.txt').read_bytes() == (gates / 'quotations-head.txt').read_bytes()},
    'typecheck': {'command': 'npm run typecheck', 'exitLine': line_matching(gates / 'typecheck.log', r'^exit=')},
    'authoritySweep': {'command': 'npx vitest run apps/three-surface-poc/src/polaris-authority-sweep.test.ts', 'testsLine': line_matching(gates / 'authority-sweep.log', r'^\s*Tests\s')},
    'invocationForms': {
        'pairs': forms['pairs'], 'identicalPairs': forms['identicalPairs'], 'distinctOutputs': forms['distinctHeadOutputs'],
        'controlAtReviewedCommit': {'pairs': control['pairs'], 'identicalPairs': control['identicalPairs'], 'reviewedCommit': control['trees']['head']['commit']},
    },
    'gpq0ExtraChecks': {
        'oldVersusNewDifferential': f"{differential['harness']['identical']} of {differential['harness']['scenarios']} scenarios identical three ways ({distinct} distinct transcripts); {mutants['killed']} of {mutants['mutants']} differential mutants killed, the other {len(survivors)} equivalent by construction and killed by main.test.ts",
        'ruleSixMutantPerPredicate': f"main.test.ts: {main_test['killed']} of {main_test['mutants']} mutants of poc-main.ts killed; the four predicates that survived at the reviewed commit are the entry guard's (removed with the guard) and the suffix filter (suffix-filter-dropped, killed)",
        'alteredProseLimb': {
            'limb': 'an old-versus-new differential over a mutated-record corpus that includes records with altered prose (GP-Q0 review rule)',
            'mapping': 'no module that reads a record or observed text changed in substance: for the record-reading modules listed in dist-compare-2026-10-22.json (predicate and count stated there) the emitted JavaScript is identical base against head once comments and export are removed, so any record, altered or not, is read and judged by the same code; the only non-identical emitted modules are listed under differing',
            'method': dist['tool'] + ': each non-test .js file under apps/three-surface-poc/dist in a clean base build and a clean head build is parsed with the TypeScript compiler API (version ' + dist['typescriptVersion'] + '), export modifiers and local export lists are dropped, and the result is printed without comments',
            'commonModules': dist['commonFiles'],
            'recordReadingModules': dist['recordReadingModules']['count'],
            'recordReadingTally': dist['recordReadingModules']['tally'],
            'recordReadingDiffering': dist['recordReadingModules']['differing'],
            'allModulesTally': dist['tally'],
            'differing': dist['differing'],
            'addedInHead': dist['addedInHead'],
            'removedInHead': dist['removedInHead'],
        },
        'ownerNotice': 'left to the coordinator, posted in the cycle report at landing',
    },
    'limbIsolation': {'cells': [{'cell': c['cell'], 'exit': c['exit']} for c in limb['cells']]},
}
(OUT / 'verification-2026-10-22.json').write_text(json.dumps(verification, indent=1) + '\n')
print(json.dumps({
    'scenarios': len(scenarios), 'distinct': distinct, 'differentialMutants': f"{mutants['killed']}/{mutants['mutants']}",
    'mainTestMutants': f"{main_test['killed']}/{main_test['mutants']}", 'capture': capture_record['result'], 'forms': verification['invocationForms'],
}, indent=1))
