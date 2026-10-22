"""Compare a re-run of the recorded harness with the committed record, field by field.
Temp paths in error lines (`<TMPDIR>/polaris-marker-XXXXXX/`) are normalised, since each run draws its own.
Usage: python3 compare.py <committed.json> <rerun.json>"""
import json, re, sys

TMP = re.compile(r"'/tmp/[^']*?/polaris-marker-[A-Za-z0-9]{6}/")
committed, rerun = (json.load(open(p)) for p in sys.argv[1:3])


def norm(value):
    if isinstance(value, str):
        return TMP.sub("'<tmp>/polaris-marker-XXXXXX/", value)
    if isinstance(value, list):
        return [norm(v) for v in value]
    if isinstance(value, dict):
        return {k: norm(v) for k, v in value.items()}
    return value


top = sorted(set(committed) | set(rerun))
print('top-level fields:', len(top))
for key in top:
    same = norm(committed.get(key)) == norm(rerun.get(key))
    print(f'  {key}: {"same" if same else "DIFFERS"}')
    if not same and key not in ('mutants',):
        print('    committed:', json.dumps(committed.get(key))[:200])
        print('    rerun:    ', json.dumps(rerun.get(key))[:200])
entries = list(zip(committed['mutants'], rerun['mutants']))
print('mutant entries:', len(committed['mutants']), 'committed,', len(rerun['mutants']), 'rerun')
fields = ('id', 'tests', 'edits', 'exitCode', 'counts', 'failedTests', 'blocked', 'outcome', 'restored')
identical = 0
for c, r in entries:
    bad = [f for f in fields if norm(c.get(f)) != norm(r.get(f))]
    identical += not bad
    print(f'  {c["id"]} / {c["tests"]}: {"identical" if not bad else "differs on " + ", ".join(bad)}')
print(f'identical entries: {identical} of {len(entries)} over {len(fields)} fields each')
