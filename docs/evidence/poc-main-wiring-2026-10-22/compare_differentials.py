#!/usr/bin/env python3
"""Compare two runs of the fixed-roots differential (run_differential_fixed_roots.py).

Usage: compare_differentials.py <out.json> <base-prefix> <head-prefix> <base-commit> <head-commit>

<prefix> is the transcripts-out path given to the runner: <prefix> is the raw
transcripts, <prefix>.canonical the same with the scratch paths replaced, and
<prefix without .json>.run.json the runner's summary. The raw files name the
author's scratch path, so they are not kept; their digests are, beside the
canonical digests that a reader can re-derive from the kept canonical file.

Reports, per tree, how many scenarios ran and passed, whether the base and head
transcripts are equal scenario by scenario, and the non-vacuity figures: how many
scenarios reached each stage and how many distinct transcripts there are (a
comparison in which every scenario ended at the same refusal would prove nothing).
"""
import hashlib
import json
import pathlib
import sys
from collections import Counter

out = pathlib.Path(sys.argv[1])
base_prefix, head_prefix, base_commit, head_commit = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4], sys.argv[5]


def read(prefix: pathlib.Path):
    raw = prefix.read_bytes()
    canonical = pathlib.Path(str(prefix) + '.canonical').read_bytes()
    run = json.loads(prefix.with_suffix('.run.json').read_text())
    return json.loads(canonical), run, {'rawSha256': hashlib.sha256(raw).hexdigest(), 'canonicalSha256': hashlib.sha256(canonical).hexdigest()}


base, base_run, base_digests = read(base_prefix)
head, head_run, head_digests = read(head_prefix)
assert [t['name'] for t in base] == [t['name'] for t in head], 'the scenario lists differ'
unequal = [b['name'] for b, h in zip(base, head) if b != h]
oldMain = {run['oldMainSha256'] for run in (base_run, head_run)}
assert len(oldMain) == 1, 'the two runs used different old scripts'


def stage(transcript) -> str:
    old = transcript['old']
    if old['thrown'] is not None:
        return 'rejected-with-throw'
    if 'Machine endpoint' in old['stdout']:
        return 'served'
    if old['exitCode'] == 0:
        return 'help'
    return 'refused'


record = {
    'tool': 'compare_differentials.py',
    'runner': 'docs/evidence/poc-main-wiring-2026-10-22/run_differential_fixed_roots.py',
    'harness': 'docs/evidence/poc-hygiene-2026-10-22/main-old-vs-new-differential.test.ts.txt',
    'harnessSha256': head_run['harnessSha256'],
    'oldScript': {'commit': head_run['oldMainCommit'], 'sha256': head_run['oldMainSha256']},
    'base': {'treeCommit': base_commit, 'vitestTests': base_run['run']['tests'], 'passed': base_run['run']['passed'], 'failed': len(base_run['run']['failed']), **base_digests},
    'head': {'treeCommit': head_commit, 'vitestTests': head_run['run']['tests'], 'passed': head_run['run']['passed'], 'failed': len(head_run['run']['failed']), **head_digests},
    'scenarios': len(head),
    'scenariosWithEqualTranscriptsBaseVersusHead': len(head) - len(unequal),
    'scenariosWithUnequalTranscripts': unequal,
    'rawFilesByteEqual': base_digests['rawSha256'] == head_digests['rawSha256'],
    'nonVacuity': {
        'scenariosByStage': dict(sorted(Counter(stage(t) for t in head).items())),
        'distinctScenarioTranscripts': len({json.dumps(t, sort_keys=True) for t in head}),
        'scenariosWithPostStartActions': sum(1 for t in head if t['old']['after']),
        'oldEqualsNewInEveryScenarioAtHead': all(t['old'] == t['new'] for t in head),
    },
    'claim': 'the new main(), the entry main.ts and the pre-extraction script give equal transcripts in 42 scenarios, and the base and head trees give the same transcripts; repository roots are fixed so the five scenarios that embed one are comparable',
}
out.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({k: record[k] for k in ('scenarios', 'scenariosWithEqualTranscriptsBaseVersusHead', 'rawFilesByteEqual', 'nonVacuity')}))
sys.exit(0 if not unequal and record['nonVacuity']['oldEqualsNewInEveryScenarioAtHead'] and not base_run['run']['failed'] and not head_run['run']['failed'] else 1)
