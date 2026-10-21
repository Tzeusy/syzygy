#!/usr/bin/env python3
"""Compare route captures (route-capture.mjs output), byte for byte and by response.

Usage: compare_captures.py <out.json> <capture.json>...

The first capture is the reference (the base). Every other capture is compared
with it response by response (status, content type, body length, body sha256),
and by the bytes of its `variants` object. The files themselves differ by
design (each names its own tree commit), so file bytes are not compared; the
comparison requires the same fixture repository path and revision in every
capture, and fails otherwise. The record names each capture's tree commit and
fixture repository, and reports how many of the reference's fixtures give
distinct output, how many request keys give a body that differs across
fixtures, and the status distribution, so a comparison that cannot tell
fixtures apart is visible. Only equality between the compared trees is claimed:
the digests depend on the fixture repository path and are not a reference for
any other run.
"""
import hashlib
import json
import sys
from pathlib import Path


def flat(capture: dict) -> dict:
    return {f'{variant} | {key}': response for variant, record in capture['variants'].items() for key, response in record['routes'].items()}


def variants_bytes(capture: dict) -> bytes:
    return (json.dumps(capture['variants'], indent=1) + '\n').encode('utf-8')


def main() -> int:
    out = Path(sys.argv[1])
    paths = [Path(p) for p in sys.argv[2:]]
    raw = [p.read_bytes() for p in paths]
    captures = [json.loads(b) for b in raw]
    reference = flat(captures[0])
    fixture = captures[0]['fixtureRepository']
    for capture in captures[1:]:
        if (capture['fixtureRepository']['path'], capture['fixtureRepository']['revision']) != (fixture['path'], fixture['revision']):
            raise SystemExit('captures name different fixture repositories; they are not comparable')
    comparisons = []
    for path, data, capture in zip(paths[1:], raw[1:], captures[1:]):
        other = flat(capture)
        comparisons.append({
            'file': path.name,
            'fileSha256': hashlib.sha256(data).hexdigest(),
            'treeCommit': capture['tree']['commit'],
            'changedTrackedFilesUnderPackagesAndApps': capture['tree']['changedTrackedFilesUnderPackagesAndApps'],
            'variantsSha256': hashlib.sha256(variants_bytes(capture)).hexdigest(),
            'variantsBytesEqualReference': variants_bytes(capture) == variants_bytes(captures[0]),
            'sameRequestKeys': other.keys() == reference.keys(),
            'responsesDifferingFromReference': sum(1 for k in reference if other.get(k) != reference[k]),
        })
    fixtures = captures[0]['variants']
    signature = {v: hashlib.sha256(json.dumps(rec['routes'], sort_keys=True).encode()).hexdigest() for v, rec in fixtures.items()}
    per_variant_keys = [list(rec['routes']) for rec in fixtures.values()]
    keys = per_variant_keys[0]
    bodies = {v: {k: r['bodySha256'] for k, r in rec['routes'].items()} for v, rec in fixtures.items()}
    statuses: dict[int, int] = {}
    for response in reference.values():
        statuses[response['status']] = statuses.get(response['status'], 0) + 1
    record = {
        'tool': 'compare_captures.py',
        'claim': 'equality between the compared trees only; the digests depend on the fixture repository path and are not a reference for any other run',
        'reference': {'file': paths[0].name, 'fileSha256': hashlib.sha256(raw[0]).hexdigest(), 'treeCommit': captures[0]['tree']['commit'],
                      'changedTrackedFilesUnderPackagesAndApps': captures[0]['tree']['changedTrackedFilesUnderPackagesAndApps'],
                      'variantsSha256': hashlib.sha256(variants_bytes(captures[0])).hexdigest()},
        'fixtureRepository': fixture,
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
        print(f"  {c['file']} ({c['treeCommit'][:8]}): variants bytes equal {c['variantsBytesEqualReference']}, differing responses {c['responsesDifferingFromReference']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
