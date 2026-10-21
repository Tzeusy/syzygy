#!/usr/bin/env python3
"""Rule-6 run for compare_differentials.py and compare_route_captures.py.

Usage: mutate_comparators.py <scratch-out-dir> <tree-commit> <out.json>

<scratch-out-dir> holds the inputs the two comparators read (diff-fixed-base.json,
diff-fixed-head.json with their .canonical and .run.json companions, and
route-base.json, route-head.json, route-base-run2.json). Each perturbation is
applied to a copy in a temporary directory; the comparator must exit non-zero
where it should, and the unperturbed control must exit 0. Records, per
perturbation, what was changed and the comparator's first output line.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SCRATCH, TREE_COMMIT, OUT = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2], pathlib.Path(sys.argv[3]).resolve()
BASE_COMMIT = '0' * 40  # placeholders: the comparators only copy the commits into their record
HEAD_COMMIT = '1' * 40
DIFF = ['diff-fixed-base.json', 'diff-fixed-base.json.canonical', 'diff-fixed-base.run.json', 'diff-fixed-head.json', 'diff-fixed-head.json.canonical', 'diff-fixed-head.run.json']
ROUTE = ['route-base.json', 'route-head.json', 'route-base-run2.json']


def load(path):
    return json.loads(path.read_text())


def save(path, value):
    path.write_text(json.dumps(value, indent=1) + '\n')


def run_diff(directory: pathlib.Path):
    proc = subprocess.run([sys.executable, str(HERE / 'compare_differentials.py'), str(directory / 'out.json'), str(directory / 'diff-fixed-base.json'), str(directory / 'diff-fixed-head.json'), BASE_COMMIT, HEAD_COMMIT], capture_output=True, text=True)
    return proc.returncode, (proc.stdout.strip() or proc.stderr.strip().splitlines()[-1] if (proc.stdout.strip() or proc.stderr.strip()) else '')


def run_route(directory: pathlib.Path):
    fixture = directory / 'repo'
    (directory / 'repo.json').write_text(json.dumps({'repoRoot': str(fixture), 'revision': '1f892687d53c829f9c2a4ee99bccccb23d6158df'}))
    proc = subprocess.run([sys.executable, str(HERE / 'compare_route_captures.py'), str(directory / 'out.json'), str(fixture), str(directory / 'route-base.json'), BASE_COMMIT, str(directory / 'route-head.json'), HEAD_COMMIT, str(directory / 'route-base-run2.json')], capture_output=True, text=True)
    return proc.returncode, (proc.stdout.strip() or proc.stderr.strip().splitlines()[-1] if (proc.stdout.strip() or proc.stderr.strip()) else '')


def first_route(capture):
    variant = next(iter(capture))
    key = next(iter(capture[variant]['routes']))
    return capture[variant]['routes'][key]


def perturb_transcript(directory):
    path = directory / 'diff-fixed-head.json.canonical'
    data = load(path)
    data[0]['new']['stdout'] += 'x'
    data[0]['old']['stdout'] += 'x'  # old and new stay equal inside head; only base-versus-head differs
    save(path, data)


def perturb_old_new_split(directory):
    path = directory / 'diff-fixed-head.json.canonical'
    data = load(path)
    data[0]['new']['exitCode'] += 1
    save(path, data)
    base = directory / 'diff-fixed-base.json.canonical'
    base_data = load(base)
    base_data[0]['new']['exitCode'] += 1
    save(base, base_data)  # base and head agree, so only the old-versus-new check can notice


def perturb_failed_test(directory):
    path = directory / 'diff-fixed-head.run.json'
    data = load(path)
    data['run']['failed'] = [{'test': 'scenario happy', 'firstErrorLine': 'AssertionError'}]
    save(path, data)


def perturb_scenario_order(directory):
    path = directory / 'diff-fixed-head.json.canonical'
    data = load(path)
    data[0], data[1] = data[1], data[0]
    save(path, data)


def perturb_old_script(directory):
    path = directory / 'diff-fixed-head.run.json'
    data = load(path)
    data['oldMainSha256'] = '2' * 64
    save(path, data)


def perturb_body(directory):
    path = directory / 'route-head.json'
    data = load(path)
    first_route(data)['bodySha256'] = '3' * 64
    save(path, data)


def perturb_status(directory):
    path = directory / 'route-head.json'
    data = load(path)
    first_route(data)['status'] += 1
    save(path, data)


def perturb_dropped_key(directory):
    path = directory / 'route-head.json'
    data = load(path)
    variant = next(iter(data))
    del data[variant]['routes'][next(iter(data[variant]['routes']))]
    save(path, data)


def perturb_second_run(directory):
    path = directory / 'route-base-run2.json'
    data = load(path)
    first_route(data)['bodyLength'] += 1
    save(path, data)


CASES = [
    ('compare_differentials', run_diff, DIFF, 'head transcript of one scenario differs from base', perturb_transcript),
    ('compare_differentials', run_diff, DIFF, 'new main differs from the old script in one scenario (base and head agree)', perturb_old_new_split),
    ('compare_differentials', run_diff, DIFF, 'one vitest test failed in the head run', perturb_failed_test),
    ('compare_differentials', run_diff, DIFF, 'scenario order differs', perturb_scenario_order),
    ('compare_differentials', run_diff, DIFF, 'the two runs used different old scripts', perturb_old_script),
    ('compare_route_captures', run_route, ROUTE, 'one head body digest differs', perturb_body),
    ('compare_route_captures', run_route, ROUTE, 'one head status differs', perturb_status),
    ('compare_route_captures', run_route, ROUTE, 'one head request key is missing', perturb_dropped_key),
    ('compare_route_captures', run_route, ROUTE, 'the second base run differs from the first', perturb_second_run),
]

results, controls = [], {}
for tool, runner, files, description, perturb in [(c[0], c[1], c[2], None, None) for c in {c[0]: c for c in CASES}.values()] + CASES:
    with tempfile.TemporaryDirectory(prefix='zz-mutate-comparators-') as name:
        directory = pathlib.Path(name)
        for file in files:
            shutil.copy(SCRATCH / file, directory / file)
        if perturb is not None:
            perturb(directory)
        code, line = runner(directory)
    if perturb is None:
        controls[tool] = {'exit': code, 'firstOutputLine': line, 'holds': code == 0}
    else:
        results.append({'tool': tool, 'perturbation': description, 'exit': code, 'outcome': 'killed' if code != 0 else 'SURVIVED', 'firstOutputLine': line})
        print(tool, description, results[-1]['outcome'], flush=True)
assert all(c['holds'] for c in controls.values()), f'a control failed: {controls}'
OUT.write_text(json.dumps({
    'tool': 'mutate_comparators.py',
    'treeCommit': TREE_COMMIT,
    'controls': controls,
    'perturbations': len(results),
    'killed': sum(1 for r in results if r['outcome'] == 'killed'),
    'results': results,
}, indent=1) + '\n')
print('survivors:', [r['perturbation'] for r in results if r['outcome'] != 'killed'])
