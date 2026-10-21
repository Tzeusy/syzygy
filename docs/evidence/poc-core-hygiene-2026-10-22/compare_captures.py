#!/usr/bin/env python3
"""Compare route captures (route-capture.mjs output), byte for byte and by response.

Usage: compare_captures.py <out.json> <capture.json>...

The first capture is the reference (the base). Every other capture is compared
with it response by response (status, content type, body length, body sha256),
and as raw file bytes. The record also reports how many of the reference's
fixtures give distinct output, how many request keys give a body that differs
across fixtures, and the status distribution, so a comparison that cannot tell
fixtures apart is visible.
"""
import hashlib
import json
import sys
from pathlib import Path


def flat(capture: dict) -> dict:
    return {f'{variant} | {key}': response for variant, record in capture.items() for key, response in record['routes'].items()}


def main() -> int:
    out = Path(sys.argv[1])
    paths = [Path(p) for p in sys.argv[2:]]
    raw = [p.read_bytes() for p in paths]
    captures = [json.loads(b) for b in raw]
    reference = flat(captures[0])
    comparisons = []
    for path, data, capture in zip(paths[1:], raw[1:], captures[1:]):
        other = flat(capture)
        comparisons.append({
            'file': path.name,
            'fileSha256': hashlib.sha256(data).hexdigest(),
            'fileBytesEqualReference': data == raw[0],
            'sameRequestKeys': other.keys() == reference.keys(),
            'responsesDifferingFromReference': sum(1 for k in reference if other.get(k) != reference[k]),
        })
    fixtures = captures[0]
    signature = {v: hashlib.sha256(json.dumps(rec['routes'], sort_keys=True).encode()).hexdigest() for v, rec in fixtures.items()}
    per_variant_keys = [list(rec['routes']) for rec in fixtures.values()]
    keys = per_variant_keys[0]
    bodies = {v: {k: r['bodySha256'] for k, r in rec['routes'].items()} for v, rec in fixtures.items()}
    statuses: dict[int, int] = {}
    for response in reference.values():
        statuses[response['status']] = statuses.get(response['status'], 0) + 1
    record = {
        'tool': 'compare_captures.py',
        'reference': {'file': paths[0].name, 'fileSha256': hashlib.sha256(raw[0]).hexdigest()},
        'fixtures': len(fixtures),
        'fixturesWithDistinctOutput': len(set(signature.values())),
        'routesPerFixture': [rec['routeCount'] for rec in fixtures.values()],
        'responses': len(reference),
        'requestKeysPerFixture': len(keys),
        'requestKeysWhoseBodyDiffersAcrossFixtures': sum(1 for k in keys if len({bodies[v][k] for v in bodies}) > 1),
        'distinctBodyDigests': len({r['bodySha256'] for r in reference.values()}),
        'statuses': {str(k): v for k, v in sorted(statuses.items())},
        'comparisons': comparisons,
    }
    out.write_text(json.dumps(record, indent=1) + '\n', encoding='utf-8')
    print(f"responses={record['responses']} fixtures={record['fixtures']} distinct={record['fixturesWithDistinctOutput']} "
          f"keysVarying={record['requestKeysWhoseBodyDiffersAcrossFixtures']}/{record['requestKeysPerFixture']}")
    for c in comparisons:
        print(f"  {c['file']}: bytes equal {c['fileBytesEqualReference']}, differing responses {c['responsesDifferingFromReference']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
