#!/usr/bin/env python3
"""Compare surface-route captures taken over two trees.

Usage: compare_route_captures.py <out.json> <fixture-repo-path> <base.json> <base-commit> <head.json> <head-commit> <base-run2.json>

The captures are written by ../poc-hygiene-2026-10-22/route-capture.mjs, which
serves the app's three route groups over five fixture models and records
status, content type, body length and body sha256 per request. The body digests
of the model pages embed the fixture repository's root, so two captures are
comparable only over the same path; <fixture-repo-path> is that path. It is
replaced by <FIXTURE-REPO> in the text that is hashed as canonical, and the raw
digest of every file is kept beside it (the capture file itself does not name
the path, so the two digests agree unless a later capture embeds it; the count
of replacements is recorded).

Records: equality of the base and head captures (key by key), a second base run
as a determinism control, and the non-vacuity figures: how many requests were
made, with which statuses, and how many request keys give a different body in
different fixtures (a comparison that cannot tell fixtures apart proves nothing).
"""
import hashlib
import json
import pathlib
import sys
from collections import Counter

out, fixture_path = pathlib.Path(sys.argv[1]), sys.argv[2]
base_file, base_commit, head_file, head_commit, run2_file = sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
fixture_meta = json.loads(pathlib.Path(fixture_path + '.json').read_text())
assert fixture_meta['repoRoot'] == fixture_path, 'the fixture record names another path'


def load(file):
    raw = pathlib.Path(file).read_bytes()
    canonical = raw.replace(fixture_path.encode(), b'<FIXTURE-REPO>')
    return json.loads(raw), {
        'file': pathlib.Path(file).name,
        'rawSha256': hashlib.sha256(raw).hexdigest(),
        'canonicalSha256': hashlib.sha256(canonical).hexdigest(),
        'pathOccurrencesReplaced': raw.count(fixture_path.encode()),
    }


base, base_digest = load(base_file)
head, head_digest = load(head_file)
run2, run2_digest = load(run2_file)


def flatten(capture):
    return {(variant, key): value for variant, record in capture.items() for key, value in record['routes'].items()}


b, h, r = flatten(base), flatten(head), flatten(run2)
keys = sorted(set(b) | set(h))
differing = [f'{v} :: {k}' for v, k in keys if b.get((v, k)) != h.get((v, k))]
control_differing = [f'{v} :: {k}' for v, k in sorted(set(b) | set(r)) if b.get((v, k)) != r.get((v, k))]
by_key = {}
for (variant, key), value in b.items():
    by_key.setdefault(key, set()).add(value['bodySha256'])
statuses = Counter(value['status'] for value in b.values())
record = {
    'tool': 'compare_route_captures.py',
    'capturedBy': 'docs/evidence/poc-hygiene-2026-10-22/route-capture.mjs',
    'fixtureRepository': {'path': '<FIXTURE-REPO>', 'revision': fixture_meta['revision'],
                          'note': 'a directory inside the author scratch area, deleted after the run; body digests are bound to its path, so the same path was used for every capture here'},
    'base': {'treeCommit': base_commit, **base_digest},
    'head': {'treeCommit': head_commit, **head_digest},
    'baseSecondRun': {'treeCommit': base_commit, **run2_digest},
    'variants': sorted(base),
    'requestKeys': len(b),
    'requestKeysEqualBaseVersusHead': len(keys) - len(differing),
    'differingBaseVersusHead': differing,
    'baseVersusBaseSecondRunDiffering': control_differing,
    'statuses': {str(k): v for k, v in sorted(statuses.items())},
    'nonVacuity': {
        'distinctBodyDigests': len({value['bodySha256'] for value in b.values()}),
        'requestPathsWhoseBodyDiffersAcrossVariants': sum(1 for digests in by_key.values() if len(digests) > 1),
        'requestPathsInAllVariants': len(by_key),
    },
    'claim': 'equality between the base and head trees over these fixtures; the digests are not comparable across other fixture paths',
}
out.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({k: record[k] for k in ('requestKeys', 'requestKeysEqualBaseVersusHead', 'statuses', 'nonVacuity')}))
sys.exit(0 if not differing and not control_differing else 1)
