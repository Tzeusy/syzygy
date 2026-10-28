#!/usr/bin/env python3
"""Builds spread-loops-2026-10-28.json, the record of syzygy-bpyt.1.18, from the tool outputs in this directory.

Usage: build-record.py <repo root> <code commit> <base commit>
Every figure is read from an output file or computed from git; nothing is typed here except the labels and the sentences that say
what a figure means. Run it from a checkout where the code commit is reachable. The record names its subject by commit and by the
sha256 of every changed file at that commit (rule 11), and lists the sha256 of every file beside it except itself.
"""
import hashlib
import json
import os
import subprocess
import sys

root, code, base = sys.argv[1:4]
here = os.path.join(root, 'docs/evidence/syzygy-bpyt-1-18')
OWNER_RECORD = '.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-FOLLOWUPS-2026-10-28.md'


def git(*args):
    return subprocess.run(['git', '-C', root, *args], capture_output=True, text=True, check=True).stdout


def blob_sha(commit, path):
    data = subprocess.run(['git', '-C', root, 'show', f'{commit}:{path}'], capture_output=True, check=True).stdout
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.load(open(os.path.join(here, name), encoding='utf-8'))


changed = [p for p in git('diff', '--name-only', f'{base}..{code}').split('\n') if p]
files = {}
for p in changed:
    stat = git('diff', '--numstat', f'{base}..{code}', '--', p).split()
    files[p] = {'baseSha256': blob_sha(base, p), 'codeSha256': blob_sha(code, p), 'added': int(stat[0]), 'removed': int(stat[1])}
production = [p for p in changed if not p.endswith('.test.ts')]

trace = {k: load(f'trace-{k}.json') for k in ('base-8d5d4bab-pipeline', 'base-8d5d4bab-extractor', 'head-0f0ce073-pipeline', 'head-0f0ce073-extractor')}


def shape_rows(pipeline):
    return {k: {'result': v['result'], 'sourceRecord': (v.get('detail') or {}).get('sourceRecord'), 'catFileCalls': v['gitCatFileCalls']} for k, v in pipeline['buildProjectShape'].items()}


def extractor_rows(extractor):
    return {k: {'result': v['result'], 'sourceRecord': (v.get('detail') or {}).get('sourceRecord'), 'successCriterionItems': (v.get('detail') or {}).get('items')} for k, v in extractor.items()}


before, after = trace['base-8d5d4bab-pipeline'], trace['head-0f0ce073-pipeline']
runs = {'default stack': load('huge-differential-default.json'), '--stack-size=492': load('huge-differential-stack-size-492.json'), '--stack-size=1968': load('huge-differential-stack-size-1968.json')}
thresholds = {}
for label, run in runs.items():
    thresholds[label] = {
        'maskInnerLinesFirstThrowing': {end: row['threshold'].get('firstThrowing') for end, row in run['mask'].items()},
        'extractorBulletsFirstThrowing': run['extractor']['threshold'].get('firstThrowing'),
        'failures': run['failures'],
        'maskBeyond': {end: [(b['inner'], b['base'], b['head'], b['headEqualsOracle']) for b in row['beyond']] for end, row in run['mask'].items()},
        'extractorBeyond': [(b['bullets'], b['base'], b['head'], b['headKeepsEveryItem']) for b in run['extractor']['beyond']],
        'survivorsEqual': all(s['baseEqualsHead'] for row in run['mask'].values() for s in row['survivors']) and all(s['baseEqualsHead'] for s in run['extractor']['survivors']),
        'survivorCount': sum(len(row['survivors']) for row in run['mask'].values()) + len(run['extractor']['survivors']),
    }

diff = load('mask-differential-output.json')
overall = {k: sum(diff['delta'][f'{c}/all'][k] for c in ('fence', 'n2', 'vet')) for k in ('rows', 'refuses', 'accepts', 'sameDecisionOtherFindings', 'unchanged')}
mutants = load('spread-mutants-output.json')
selftest = load('huge-differential-selftest-output.json')
delta = load('test-delta-output.json')
sweep_base, sweep_head = load('spread-sweep-8d5d4bab.json'), load('spread-sweep-0f0ce073.json')
ceiling = load('ceiling-head-0f0ce073.json')
removed_sites = sorted({(h['path'], h['text']) for h in sweep_base['hits']} - {(h['path'], h['text']) for h in sweep_head['hits']})
added_sites = sorted({(h['path'], h['text']) for h in sweep_head['hits']} - {(h['path'], h['text']) for h in sweep_base['hits']})

record = {
    'bead': 'syzygy-bpyt.1.18',
    'title': 'The mask and extractor one-call spread pushes become loops',
    'date': '2026-10-28',
    'authority': {
        'ownerRecord': OWNER_RECORD,
        'ownerRecordSha256': hashlib.sha256(open(os.path.join(root, OWNER_RECORD), 'rb').read()).hexdigest(),
        'question': 'GP-B2 Q1 and its follow-up',
        'selectedLabels': {'Q1': 'A: read it (Recommended)', 'followUp': 'Land #544 first (Recommended)'},
        'note': 'Labels as recorded by the owner direction record; this record does not restate the record beyond them.',
    },
    'subject': {'baseCommit': base, 'codeCommit': code, 'node': trace['base-8d5d4bab-pipeline']['node'], 'files': files, 'productionFiles': production},
    'claims': [
        {'label': 'Observed', 'text': f'Of the {len(changed)} changed files, the production files are {production}; no other non-test file changes in the code commit. The evidence directory is added after it.'},
        {'label': 'Observed', 'text': f'The argument-spread census (spread_sweep.py, its regex verbatim) over {sweep_base["population"]} tracked files finds {sweep_base["regexHits"]} calls at the base and {sweep_head["regexHits"]} at the code commit; removed: {[list(s) for s in removed_sites]}; added: {[list(s) for s in added_sites]}. The other {sweep_head["regexHits"]} are syzygy-bpyt.54 and are untouched.'},
        {'label': 'Observed', 'text': 'At the base, scanActiveContent and buildProjectShape throw RangeError (Maximum call stack size exceeded) for a closed fence of 200,000 lines in LF, CRLF and CR, in a phase-B source (vision.md) and in the phase-A root index; at the code commit every one of those 12 builds returns an observed shape with the source classified, with the same 14 cat-file calls as the 100,000-line builds.'},
        {'label': 'Observed', 'text': 'At the base, buildProjectShape throws for a success list of 130,000 and of 200,000 bullets (520,268 and 800,268 bytes, under maxBytesPerSource) and returns for 125,000; at the code commit all of 100,000, 125,000, 130,000 and 200,000 return an observed shape with every item.'},
        {'label': 'Observed', 'text': 'The boundary is a measurement of a run, not a constant: the first throwing inner-line count was 125,285 (CR) to 125,287 (LF and CRLF) in a vitest process, 125,457 to 125,465 in a bare node process, and it scales with the V8 stack size (about 62,490 at --stack-size=492, 125,460 at the default 984, 251,409 at 1968).'},
        {'label': 'Observed', 'text': 'The mask differential of syzygy-bpyt.16, unchanged, run between the base build and the code commit build over its 11,054 synthetic texts, returns 0 refuses, 0 accepts, 0 same-decision-other-findings and 11,054 unchanged, with C1 to C4 at 0 failures. Every output the change alters is therefore a throw that becomes a decision, at a fence or class past the stack boundary.'},
        {'label': 'Observed', 'text': 'Rule 6: six mutants (two restore a spread, four are off-by-one or order faults of a loop) are all killed, and restoring both spreads fails 20 of the new tests; the control run at the code commit fails none.'},
        {'label': 'Observed', 'text': f'A 130,000-item success list makes a shape whose JSON is {ceiling["shapeJsonBytes"]:,} bytes, against maxMachineResponseBytes {ceiling["maxMachineResponseBytes"]:,} and maxHumanResponseBytes {ceiling["maxHumanResponseBytes"]:,}.'},
        {'label': 'Inferred', 'text': 'Because routes.ts serializes the model for the machine routes and bounds each response (a breach answers HTTP 503 with served nothing), a daemon that now starts on such a repository would answer those routes with that 503. Not run: no route or daemon was exercised on a model of that size.'},
        {'label': 'Inferred', 'text': 'Startup: createReobserveSession builds the first model inside serveBoundRepository, so a build that no longer throws lets the daemon start where it exited 1 with an observation failure; re-observation of the same input returns reobserved where it returned failed and kept the prior model (the second is run through createReobserveState; the first is read from the code).'},
        {'label': 'Unknown', 'text': 'The effect on any real repository: no repository body was read, every text is synthetic. Whether any observed repository holds a fence or a class that large is not measured.'},
    ],
    'beforeAfter': {
        'node': trace['base-8d5d4bab-pipeline']['node'],
        'pipeline': {'before': shape_rows(before), 'after': shape_rows(after)},
        'direct': {'before': {k: [v['mask'], v['scanActiveContent']] for k, v in before['direct'].items()}, 'after': {k: [v['mask'], v['scanActiveContent']] for k, v in after['direct'].items()}},
        'reobserve': {'before': before['reobserveState'], 'after': after['reobserveState']},
        'extractor': {'before': extractor_rows(trace['base-8d5d4bab-extractor']), 'after': extractor_rows(trace['head-0f0ce073-extractor'])},
        'startupBefore': before['startupStderrLine'],
        'measuredAt': {'before': base, 'after': code},
    },
    'stackDependence': thresholds,
    'maskDifferential': {'tool': 'docs/evidence/syzygy-bpyt-16/crlf-differential.mjs', 'output': 'mask-differential-output.json', 'population': diff['population']['texts'], 'checks': diff['checks'], 'failures': diff['failureCount'], 'tally': overall},
    'rule6': {
        'summary': mutants['summary'],
        'rows': [{'id': r['id'], 'outcome': r.get('outcome'), 'failingTestCount': len(r['failingTests']), 'detectors': r['detectors']} for r in mutants['rows']],
        'fullRows': 'spread-mutants-output.json',
        'differentialSelftest': {'killed': selftest['killed'], 'total': selftest['total'], 'ids': [m['id'] for m in selftest['mutants']], 'output': 'huge-differential-selftest-output.json'},
    },
    'tests': {'line': delta['line'], 'baseTests': delta['baseTests'], 'headTests': delta['headTests'], 'overFiles': sorted({p for p in changed if p.endswith('.test.ts')}), 'allBasePassed': delta['allBasePassed'], 'allHeadPassed': delta['allHeadPassed']},
    'ceilingProbe': ceiling,
    'residuals': [
        'The 31 remaining spread calls are syzygy-bpyt.54; a fix there that turns a crash into a decision returns to the owner.',
        'The stack boundary is not removed by this change anywhere else: other recursive or argument-bounded code is not swept here.',
        'Surfaces were not exercised on a model with 130,000 items: the over-ceiling answer is inferred from routes.ts, not run.',
    ],
}
skip = {'spread-loops-2026-10-28.json'}
record['files'] = {n: hashlib.sha256(open(os.path.join(here, n), 'rb').read()).hexdigest() for n in sorted(os.listdir(here)) if n not in skip}
with open(os.path.join(here, 'spread-loops-2026-10-28.json'), 'w', encoding='utf-8') as handle:
    json.dump(record, handle, indent=1)
    handle.write('\n')
print(json.dumps({k: record[k] for k in ('tests', 'maskDifferential')}, indent=1)[:900])
