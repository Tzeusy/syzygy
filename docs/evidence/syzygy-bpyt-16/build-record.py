#!/usr/bin/env python3
"""Builds crlf-mask-2026-10-27.json, the record of syzygy-bpyt.16, from the outputs beside it. Every digest and total is computed.

Usage: build-record.py <git repo> <base commit> <code commit> <evidence dir>
Refuses (exit 1) unless the outputs say what the record is about to say: no differential failure, every non-equivalent mutant
killed, the self-test killing 4 of 4, the two digest-citer methods agreeing, the vet runner agreeing at HEAD on every row.
"""
import hashlib
import json
import os
import subprocess
import sys

repo, base_arg, code_arg, evidence = sys.argv[1:]
MASK = 'packages/three-surface-poc-core/src/markdown-code-context.ts'


def git(*args):
    return subprocess.run(['git', '-C', repo, *args], capture_output=True, check=True).stdout


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.load(open(os.path.join(evidence, name), encoding='utf8'))


base = git('rev-parse', base_arg).decode().strip()
code = git('rev-parse', code_arg).decode().strip()

diff = load('crlf-differential-output.json')
mut = load('crlf-mask-mutants-output.json')
self_test = load('crlf-differential-selftest-output.json')
citers = load('digest-citers-6928b50a.json')
vet_head = load('vet-run-at-head-summary.json')
tests = load('test-delta-output.json')
problems = []
if any(c['failures'] for c in diff['checks'].values()) or diff['failureCount'] != 0:
    problems.append('the differential has failures')
if mut['summary']['survived'] or mut['summary']['killed'] + mut['summary']['survivedEquivalent'] != mut['summary']['mutants']:
    problems.append('a non-equivalent mutant survived')
if self_test['killed'] != self_test['total'] or self_test['total'] != 4:
    problems.append('the differential self-test is not 4 of 4')
if not citers['methodsAgree'] or citers['codeHeadCommit'] != code or citers['baseCommit'] != base_arg:
    problems.append('digest-citers: methods disagree or another commit')
vs = vet_head['summary']
for group in ('CRLF', 'CR', 'MRT'):
    for key in ('payload_today_vs_lf', 'payload_today_vs_oTerm', 'control_today_vs_lf'):
        t = vs[group][key]
        if t['same'] != t['denominator']:
            problems.append(f'vet runner at HEAD: {group} {key} {t["same"]} of {t["denominator"]}')
if vet_head['oracleDisagreeLf'] != 0:
    problems.append('vet oracle disagrees with the LF text')
if not (tests['allBasePassed'] and tests['allHeadPassed']):
    problems.append('a test did not pass')
if diff['baseDistModule'] == diff['headDistModule']:
    problems.append('the base and head builds are the same module')
if problems:
    print('REFUSED:', *problems, sep='\n  ')
    sys.exit(1)

# Files this change adds or edits, at the code commit.
changed = []
names = git('diff', '--name-status', '-z', base, code).decode().split('\0')
for i in range(0, len(names) - 1, 2):
    status, path = names[i], names[i + 1]
    blob = git('show', f'{code}:{path}')
    changed.append({'path': path, 'status': status, 'bytesAtCode': len(blob), 'sha256AtCode': sha(blob)})
base_mask, head_mask = git('show', f'{base}:{MASK}'), git('show', f'{code}:{MASK}')

# Files of this directory, except the record itself.
own = []
for root, _dirs, files in os.walk(evidence):
    for f in sorted(files):
        path = os.path.join(root, f)
        rel = os.path.relpath(path, evidence)
        if rel == 'crlf-mask-2026-10-27.json':
            continue
        data = open(path, 'rb').read()
        own.append({'path': 'docs/evidence/syzygy-bpyt-16/' + rel, 'bytes': len(data), 'sha256': sha(data)})
own.sort(key=lambda r: r['path'])

selection = diff['vetSelection']
record = {
    'record': 'syzygy-bpyt.16: the code-context mask ends a line at CRLF, CR and LF',
    'date': '2026-10-27',
    'bead': 'syzygy-bpyt.16',
    'authority': {
        'decisionBead': 'syzygy-bpyt.1.14',
        'ownerAnswer': 'Arm (a) + bare CR (Recommended)',
        'authorized': 'Inside maskMarkdownCodeContexts a line ends at CRLF, CR or LF. The split keeps every terminator and offset. A CRLF or CR text gets exactly the decision its LF form gets.',
        'notAuthorized': [
            'any specification or policy byte (the PWB-REQ-006 clarifying sentence was not chosen)',
            'the extraction, index-link and consent readers (G2, G3 and G4 of the fence-rule record stay open owner questions)',
            'any change to how an LF text is read',
            'normalizing the text at the scanner entry, which would renumber findings in a bare-CR file',
        ],
    },
    'subject': {
        'baseCommit': base,
        'codeCommit': code,
        'note': 'The record is committed after the code commit. The code commit is the subject of every measurement here; the PR head adds only this directory.',
        'productionFile': {
            'path': MASK,
            'base': {'bytes': len(base_mask), 'sha256': sha(base_mask)},
            'code': {'bytes': len(head_mask), 'sha256': sha(head_mask)},
        },
        'builtModule': {'base': diff['baseDistModule'], 'code': diff['headDistModule'], 'what': 'sha256 of dist/markdown-code-context.js, each built with tsc -b in its own checkout'},
        'changedFiles': changed,
    },
    'ccRev1Classes': {
        'touched': [4, 3],
        'class4': 'security: the mask decides which text the active-content scan (SEC-3 untrusted-content gate) reads; scanActiveContent is the only caller',
        'class3': 'deterministic observation: the same bytes now give one admit/refuse decision whatever their line terminator',
        'notClaimed': {'class1': 'authority boundaries: body-read-authority, the write-universe and the typed-authority table are untouched'},
        'rule': 'Class membership is never finally determined by the agent performing the change; a reviewer or the owner may reclassify.',
    },
    'vetPackage': {
        'directory': 'docs/evidence/syzygy-bpyt-16/vet-v-crlf-mask-1/',
        'what': 'the files of the V-CRLF-MASK-1 vet (verdict REPRODUCED at 8ff50172) copied byte for byte: its corpus, runner, mutant runner, pin tests, prototype diff and result files',
        'rawReview': {
            'name': 'V-CRLF-MASK-1-RAW.md',
            'sha256': '4f1b16f3fd9c2130e3a0ccae5ec447e676592ec4b012d0e1cbf8cb1cc3f62ac3',
            'inThisTree': False,
            'why': 'the raw quotes an act argument, which check_governance CG-7e accepts only in a file under the raw-review lane (docs/reviews, a -RAW.md name) or in a registered copy, and a file in that lane needs a campaign pattern and a docs/README.md row, the shared count that one integration edit per batch of raws changes; the coordinator retains it',
        },
    },
    'corpora': {
        'vet': diff['population']['vet'],
        'fenceCases': diff['population']['fence']['cases'],
        'n2Cases': diff['population']['n2']['cases'],
        'renderings': diff['population']['renderings'],
        'texts': diff['population']['texts'],
        'distinctTexts': diff['population']['distinctTexts'],
        'distinctLfForms': diff['population']['distinctLfForms'],
        'inputs': diff['corpusFiles'],
        'readsNoRepository': 'every text is synthetic, written in the corpus files named here',
    },
    'differential': {
        'tool': 'docs/evidence/syzygy-bpyt-16/crlf-differential.mjs',
        'output': 'docs/evidence/syzygy-bpyt-16/crlf-differential-output.json',
        'checks': diff['checks'],
        'meaning': {
            'C1': 'every LF text decides identically at BASE and HEAD: findings and mask deep-equal',
            'C2': 'at HEAD every CRLF, CR and mixed rendering decides as its LF form: same finding multiset (form, context, malformed line), equal mask once terminators read as LF',
            'C3': 'at HEAD the masked text has the text length, every terminator at its offset, every other byte its own or a space',
            'C4': 'at HEAD a CRLF text has findings deep-equal to its LF form, line and column included',
        },
        'anyOtherDifference': 'none: every check above has 0 failures; a failure would have stopped the work',
        'positionOf': diff['positionOf'],
    },
    'acceptRefuseDelta': {
        'definition': 'BASE and HEAD each decide the same CRLF, CR or mixed text; refuses = BASE admits and HEAD excludes (a fail-open closed); accepts = BASE excludes and HEAD admits (a fail-closed reading the LF form admits); the others keep their decision',
        'vetCorpus': {
            'CRLF': {'payloadPositions': selection['CRLF']['payload'], 'controls': selection['CRLF']['control']},
            'CR': {'payloadPositions': selection['CR']['payload'], 'controls': selection['CR']['control']},
            'mixedAndTrailingCrVariants': {'payloadPositions': selection['variants']['payload'], 'controls': selection['variants']['control']},
            'sumOfRows': diff['delta']['vet/all'],
            'vetBaseSummary': 'vet-v-crlf-mask-1/summary.json, the vet run over the BASE build, holds the same 32/48, 32/44 and 4/44 (controls 7/5, 7/3, 1/9)',
        },
        'fenceCorpus': diff['delta']['fence/all'],
        'n2Corpus': diff['delta']['n2/all'],
        'byRenderingAndCorpus': diff['delta'],
        'byCase': diff['deltaByCase'],
        'changedOutputsByClass': diff['transitions'],
        'vetChangedDecisions': diff['vetChangedDecisions'],
    },
    'secondMethod': {
        'what': 'the vet runner (vet-v-crlf-mask-1/tools/run.mjs, unchanged) over the HEAD build, with the vet independent oracle written from the PWB-REQ-006 bullets (CR read as a line terminator)',
        'output': 'docs/evidence/syzygy-bpyt-16/vet-run-at-head-summary.json',
        'rows': vs['rows'],
        'headEqualsLfAndEqualsOracle': {g: {'payload': vs[g]['payload_today_vs_lf']['same'], 'oracle': vs[g]['payload_today_vs_oTerm']['same'], 'of': vs[g]['payload_today_vs_lf']['denominator']} for g in ('CRLF', 'CR', 'MRT')},
        'oracleDisagreesWithLfCode': vet_head['oracleDisagreeLf'],
        'crEqualsCrlf': vs['crEqualsCrlf'],
    },
    'rule6': {
        'differentialSelftest': {
            'tool': 'docs/evidence/syzygy-bpyt-16/crlf-differential-selftest.mjs',
            'output': 'docs/evidence/syzygy-bpyt-16/crlf-differential-selftest-output.json',
            'killed': self_test['killed'],
            'of': self_test['total'],
            'mutants': [{k: m[k] for k in ('id', 'predicate', 'file', 'old', 'new', 'failingChecks')} for m in self_test['mutants']],
        },
        'maskMutants': {
            'tool': 'docs/evidence/syzygy-bpyt-16/crlf-mask-mutants.py',
            'output': 'docs/evidence/syzygy-bpyt-16/crlf-mask-mutants-output.json',
            'ranAt': code,
            'detectors': 'the seven test files this change adds or edits, one vitest run per mutant',
            'summary': mut['summary'],
            'mutants': [{'id': r['id'], 'outcome': r['outcome'], 'failedTests': {k: v['failed'] for k, v in r['detectors'].items()}} for r in mut['rows'] if r['id'].startswith(('MU', 'BASE'))],
            'equivalent': 'MU16: a line holds no CR or LF now (both are split points), so blanking by [^\\n] and by length agree; no test can tell them apart',
        },
    },
    'digestCitersSweep': {
        'tool': 'docs/evidence/syzygy-bpyt-6-3/digest-citers.py',
        'output': 'docs/evidence/syzygy-bpyt-16/digest-citers-6928b50a.json',
        'population': citers['population'],
        'editedProductionFiles': citers['editedProductionFiles'],
        'methodsAgree': citers['methodsAgree'],
        'headDigestCitedBy': sorted(set(citers['needlesCited'].get(citers['digests'][1]['sha256'][:12], []))),
        'baseDigestCitedBy': sorted(set(citers['needlesCited'].get(citers['digests'][0]['sha256'][:12], []))),
        'reading': 'the base digest is cited only by retained review-measurement records of the fence-rule review (they name the file as it was then); no act, manifest, acceptance record or .syzygy or openspec file cites either digest',
    },
    'tests': {
        'line': tests['line'],
        'method': 'by (file, full name) identity from vitest reports of the seven files at each commit, and by call text for a changed it.each call (tool: test-delta.py, test-inventory.mjs); a helper the callbacks call is not followed',
        'baseTests': tests['baseTests'],
        'headTests': tests['headTests'],
        'output': 'docs/evidence/syzygy-bpyt-16/test-delta-output.json',
    },
    'residuals': [
        '[Observed] positionOf in git-object-reader counts LF only and is unchanged (the ruling). A non-malformed finding in a bare-CR or mixed text keeps the LF-only line and column; a malformed finding takes the mask line, which now counts CR and CRLF as line ends. The differential counts those rows under positionOf.',
        '[Observed] The extractor splits at LF and drops one trailing CR; the link reader splits at LF only. For a bare-CR text each differs from the profile (links in 30 of the 33 fence cases, extraction in all 33, pinned in fence-rules.test.ts rows named GAP G2/G3). They are open owner questions G2 and G3 and are not changed here.',
        '[Observed] The consent reader (outsideFences) is unchanged and stays CR-blind (G4).',
        '[Observed] docs/evidence/syzygy-bpyt-6-3/dc3-fence-rules-2026-10-25.json and its probe outputs record G1 as measured before this fix; they are not edited.',
        '[Unknown] No Butlers body or other observed repository was read; the measurement is over synthetic corpora only, so how many real CRLF sources the exclusions change is Unknown.',
    ],
    'files': own,
}
text = json.dumps(record, indent=1) + '\n'
open(os.path.join(evidence, 'crlf-mask-2026-10-27.json'), 'w', encoding='utf8').write(text)
print('wrote', len(text), 'bytes;', len(own), 'files;', tests['line'], 'mutants', mut['summary'])
