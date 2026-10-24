#!/usr/bin/env python3
"""Copy the files of finished census_run.py runs into one directory, checking each against the digest its record names.

Usage: collect_runs.py <destination> <label>=<run-record.json> [<label>=<run-record.json> ...]

For each label writes <destination>/<label>.json (the run record), <destination>/<label>.trace.jsonl (the tracer's log) and
<destination>/<label>.samples.json (the sampler's record), after checking that the trace's sha256 and line count equal the ones in
the run record. It refuses a label it has already written. It reads and copies; nothing is removed.
"""
import hashlib
import json
import pathlib
import shutil
import sys

destination = pathlib.Path(sys.argv[1])
destination.mkdir(parents=True, exist_ok=True)
for pair in sys.argv[2:]:
    label, record_path = pair.split('=', 1)
    record_file = pathlib.Path(record_path)
    record = json.loads(record_file.read_text())
    private = pathlib.Path(record['privateDirectory'])
    trace, samples = private / 'trace.jsonl', pathlib.Path(record['samplerRecord'])
    digest = hashlib.sha256(trace.read_bytes()).hexdigest()
    lines = len(trace.read_text().splitlines())
    assert digest == record['trace']['sha256'] and lines == record['trace']['lines'], (label, 'the trace is not the one the record names')
    targets = [destination / f'{label}.json', destination / f'{label}.trace.jsonl', destination / f'{label}.samples.json']
    assert not any(t.exists() for t in targets), (label, 'already collected')
    for source, target in zip((record_file, trace, samples), targets):
        shutil.copyfile(source, target)
    print(label, digest, lines)
