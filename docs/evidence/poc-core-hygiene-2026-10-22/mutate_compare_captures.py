#!/usr/bin/env python3
"""Rule-6 mutation record for compare_captures.py.

Usage: mutate_compare_captures.py <reference-capture.json> <other-capture.json> <out.json>

Both captures come from route-capture.mjs. Each mutant is a copy of
<other-capture.json> with one perturbation, compared with the reference by
compare_captures.py; the unperturbed pair is the control. A mutant is killed when
the comparison reports the perturbation: a differing response, unequal variant
bytes, a different request-key set, or a refusal to compare captures made over
different fixture repositories.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def first_route(capture: dict) -> tuple[dict, str]:
    variant = next(iter(capture['variants'].values()))
    return variant['routes'], next(iter(variant['routes']))


def digest_flipped(c: dict) -> None:
    routes, key = first_route(c)
    routes[key]['bodySha256'] = ('0' if routes[key]['bodySha256'][0] != '0' else '1') + routes[key]['bodySha256'][1:]


def status_altered(c: dict) -> None:
    routes, key = first_route(c)
    routes[key]['status'] += 1


def route_dropped(c: dict) -> None:
    routes, key = first_route(c)
    del routes[key]


def fixture_revision_altered(c: dict) -> None:
    c['fixtureRepository']['revision'] = '0' * 40


def fixture_path_altered(c: dict) -> None:
    c['fixtureRepository']['path'] += '-other'


MUTANTS = [
    ('response-digest-altered', digest_flipped, 'one-differing-response'),
    ('response-status-altered', status_altered, 'one-differing-response'),
    ('request-key-dropped', route_dropped, 'key-set-differs'),
    ('fixture-revision-altered', fixture_revision_altered, 'refused'),
    ('fixture-path-altered', fixture_path_altered, 'refused'),
]


def compare(tool: Path, ref: Path, other_text: str) -> tuple[subprocess.CompletedProcess, dict | None]:
    with tempfile.TemporaryDirectory() as tmp:
        other, out = Path(tmp) / 'other.json', Path(tmp) / 'cmp.json'
        other.write_text(other_text, encoding='utf-8')
        res = subprocess.run([sys.executable, str(tool), str(out), str(ref), str(other)], capture_output=True, text=True)
        return res, (json.loads(out.read_text()) if out.exists() else None)


def main() -> int:
    ref, other, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
    tool = Path(__file__).resolve().parent / 'compare_captures.py'
    original = other.read_text(encoding='utf-8')
    res, cmp = compare(tool, ref, original)
    c = cmp['comparisons'][0]
    control = {'exit': res.returncode, 'responsesDifferingFromReference': c['responsesDifferingFromReference'], 'variantsBytesEqualReference': c['variantsBytesEqualReference'],
               'sameRequestKeys': c['sameRequestKeys'], 'holds': res.returncode == 0 and c['responsesDifferingFromReference'] == 0 and c['variantsBytesEqualReference'] and c['sameRequestKeys']}
    records = []
    for mutant_id, perturb, expect in MUTANTS:
        capture = json.loads(original)
        perturb(capture)
        res, cmp = compare(tool, ref, json.dumps(capture, indent=1) + '\n')
        if cmp is None:
            killed, seen = expect == 'refused' and res.returncode != 0, {'exit': res.returncode}
        else:
            k = cmp['comparisons'][0]
            seen = {'exit': res.returncode, 'responsesDifferingFromReference': k['responsesDifferingFromReference'], 'variantsBytesEqualReference': k['variantsBytesEqualReference'], 'sameRequestKeys': k['sameRequestKeys']}
            killed = {'one-differing-response': k['responsesDifferingFromReference'] == 1 and not k['variantsBytesEqualReference'],
                      'key-set-differs': not k['sameRequestKeys'] and k['responsesDifferingFromReference'] >= 1,
                      'refused': False}[expect]
        records.append({'id': mutant_id, 'expected': expect, 'killed': killed, 'seen': seen, 'firstOutputLine': (res.stdout.splitlines() or res.stderr.splitlines() or [''])[0] if res.returncode == 0 else (res.stderr.splitlines() or [''])[-1]})
    commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tool.parent, capture_output=True, text=True, check=True).stdout.strip()
    summary = {'subject': 'compare_captures.py', 'subjectSha256': hashlib.sha256(tool.read_bytes()).hexdigest(), 'ranAtCommit': commit,
               'reference': {'file': ref.name, 'sha256': hashlib.sha256(ref.read_bytes()).hexdigest()},
               'other': {'file': other.name, 'sha256': hashlib.sha256(other.read_bytes()).hexdigest()},
               'control': control, 'mutants': len(records), 'killed': sum(r['killed'] for r in records), 'survivors': [r['id'] for r in records if not r['killed']], 'records': records}
    out.write_text(json.dumps(summary, indent=1) + '\n', encoding='utf-8')
    print(f"control holds={control['holds']} mutants={summary['mutants']} killed={summary['killed']} survivors={summary['survivors']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
