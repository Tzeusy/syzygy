#!/usr/bin/env python3
"""syzygy-bpyt.8.1 (GP-Q0 extras): old-versus-new differential of the consent readers, over syzygy-bpyt.8.10's mutated-record corpus.
scripts/measure_consent_gate_recognition.mjs (on main from PR #500) reads every consent act record through the compiled consent
barrel, which loads consent-ports.ts and through it this package's root; it alters each non-blank line on its own (appended to,
then deleted) and applies the named alterations, prose ones included. Run it in the old and the new tree, then compare the two
outputs here, leaving out only what names the run: the commit, the worker pool and each record's read timing.
Usage: python3 consent_differential.py <old census.json> <new census.json>   (prints JSON)"""
import copy, hashlib, json, pathlib, sys

paths = [pathlib.Path(p) for p in sys.argv[1:3]]
raw = [p.read_bytes() for p in paths]
old, new = (json.loads(b) for b in raw)

def comparable(document):
    document = copy.deepcopy(document)
    for key in ('measuredOn', 'pool'):
        document.pop(key)
    document['supersededRegeneration'].pop('measuredOn')
    for record in document['records']:
        record.pop('readTiming')
    return document

a, b = comparable(old), comparable(new)
by_path = lambda document: {r['path']: r for r in document['records']}
ra, rb = by_path(a), by_path(b)
rows = [{'path': path, 'model': ra[path]['model'], 'sha256': ra[path]['sha256'], 'identical': ra[path] == rb.get(path),
         'fixtures': 1 + 2 * ra[path]['nonBlankLines'] + len(ra[path]['alterations'])} for path in ra]
answers = {r['baseline'] for r in a['records']} | {alt['answer'] for r in a['records'] for alt in r['alterations'] if alt['applies']}
print(json.dumps({
    'format': 'syzygy-bpyt-8-1-consent-differential/1',
    'old': {'commit': old['measuredOn']['commit'], 'treeClean': old['measuredOn']['treeClean'], 'censusSha256': hashlib.sha256(raw[0]).hexdigest()},
    'new': {'commit': new['measuredOn']['commit'], 'treeClean': new['measuredOn']['treeClean'], 'censusSha256': hashlib.sha256(raw[1]).hexdigest()},
    'script': old['script'], 'sameScript': old['script'] == new['script'],
    'fixtures': 'per record: the record as committed, each non-blank line appended to and deleted on its own, and each named alteration',
    'records': len(rows), 'recordsIdentical': sum(r['identical'] for r in rows), 'sameRecordSet': sorted(ra) == sorted(rb),
    'fixtureCount': sum(r['fixtures'] for r in rows), 'distinctAnswers': len(answers),
    'distinctAnswersOf': 'the baselines and named alterations; the census stores each append or delete only as same as, or unlike, its baseline',
    'checkLinesIdentical': [r['checkLines'] for r in a['records']] == [r['checkLines'] for r in b['records']],
    'supersededRegenerationIdentical': a['supersededRegeneration'] == b['supersededRegeneration'],
    'wholeDocumentIdentical': a == b, 'rows': rows,
}, indent=2))
