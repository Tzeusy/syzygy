#!/usr/bin/env python3
"""Sweep a test file for waits that can outlast their test.

Usage: sweep_waits.py <test-file> <tree-commit> <out.json>

Population: every `  it(` block at two-space indent in <test-file> (the file's
one nesting level under `describe`); a block ends at the first following line
that starts `  }` and closes the call. Each block is read for its waits:
  - `vi.waitFor(`: bound is its `timeout:` option (a number or a `const` of the
    file); no option means vitest's default of 1000 ms, which is not explicit;
  - `started(`: bound is its third argument when given (a number or a `const`),
    else the default parameter of its declaration (a `const` of the file).
The block's test timeout is its closing `}, <number|const>);` argument, else
vitest's default of 5000 ms (no project sets another for this package).
A block is `bounded` when it has a wait, every wait's bound is explicit, and its
test timeout exceeds the sum of its waits' bounds. A `started(` whose
declaration has no bound parameter has no bound, so its block is not bounded.
The sweep reports the denominators: all blocks, blocks with a wait, blocks with
an explicit test timeout, bounded blocks, and every block that waits without
being bounded; it exits 1 when any block waits without being bounded.
"""
import json
import pathlib
import re
import sys

path, tree_commit, out = pathlib.Path(sys.argv[1]), sys.argv[2], pathlib.Path(sys.argv[3])
lines = path.read_text().splitlines()
consts = {m.group(1): int(m.group(2).replace('_', '')) for line in lines if (m := re.match(r'^const ([A-Z_]+) = ([0-9_]+);', line))}
DEFAULT_TEST_TIMEOUT = 5000
DEFAULT_WAITFOR_TIMEOUT = 1000


def number(token: str) -> int:
    token = token.strip()
    return int(token.replace('_', '')) if re.fullmatch(r'[0-9_]+', token) else consts[token]


declaration = next(line for line in lines if line.startswith('async function started('))
bound_default = re.search(r'boundMs: number = ([A-Za-z0-9_]+)', declaration)
started_default = number(bound_default.group(1)) if bound_default else None  # None: the poll has no bound

blocks = []
i = 0
while i < len(lines):
    opening = re.match(r"^  it\((['`])(.*)\1, async \(\) => \{$", lines[i])
    if opening is None:
        i += 1
        continue
    j = i + 1
    while not lines[j].startswith('  }'):
        j += 1
    closing = re.match(r'^  \}(?:, ([A-Za-z0-9_]+))?\);', lines[j])
    assert closing is not None, f'line {j + 1} does not close the block opened at line {i + 1}'
    body = '\n'.join(lines[i + 1:j])
    waits = []
    for call in re.finditer(r'vi\.waitFor\(', body):
        option = re.search(r'\{ timeout: ([A-Za-z0-9_]+) \}', body[call.end():].split('\n', 1)[0])
        waits.append({'kind': 'vi.waitFor', 'boundMs': number(option.group(1)) if option else DEFAULT_WAITFOR_TIMEOUT, 'explicit': option is not None})
    for call in re.finditer(r'\bstarted\(', body):
        depth, end = 1, call.end()
        while depth:
            depth += {'(': 1, ')': -1}.get(body[end], 0)
            end += 1
        arguments = [part.strip() for part in body[call.end():end - 1].split(',')]
        waits.append({'kind': 'started', 'boundMs': number(arguments[2]) if len(arguments) > 2 else started_default, 'explicit': len(arguments) > 2 or started_default is not None})
    timeout = number(closing.group(1)) if closing.group(1) else DEFAULT_TEST_TIMEOUT
    total = None if any(w['boundMs'] is None for w in waits) else sum(w['boundMs'] for w in waits)
    blocks.append({'line': i + 1, 'name': opening.group(2), 'waits': waits, 'sumOfWaitBoundsMs': total,
                   'testTimeoutMs': timeout, 'testTimeoutExplicit': closing.group(1) is not None,
                   'bounded': bool(waits) and total is not None and timeout > total and all(w['explicit'] for w in waits)})
    i = j + 1

waiting = [b for b in blocks if b['waits']]
record = {
    'tool': 'sweep_waits.py',
    'file': str(path.name),
    'treeCommit': tree_commit,
    'fileSha256': __import__('hashlib').sha256(path.read_bytes()).hexdigest(),
    'constants': consts,
    'startedDefaultBoundMs': started_default,
    'itBlocks': len(blocks),
    'viWaitForCalls': len(re.findall(r'vi\.waitFor\(', '\n'.join(lines))),
    'blocksWithAWait': len(waiting),
    'blocksWithAnExplicitTestTimeout': sum(1 for b in blocks if b['testTimeoutExplicit']),
    'blocksWithAWaitAndAnExplicitTestTimeout': sum(1 for b in waiting if b['testTimeoutExplicit']),
    'boundedBlocks': sum(1 for b in waiting if b['bounded']),
    'waitingBlocksNotBounded': [{k: b[k] for k in ('line', 'name', 'sumOfWaitBoundsMs', 'testTimeoutMs')} for b in waiting if not b['bounded']],
    'blocks': blocks,
}
assert record['viWaitForCalls'] == sum(1 for b in blocks for w in b['waits'] if w['kind'] == 'vi.waitFor'), 'a vi.waitFor call sits outside an it block'
out.write_text(json.dumps(record, indent=1) + '\n')
print(json.dumps({k: record[k] for k in ('itBlocks', 'viWaitForCalls', 'blocksWithAWait', 'boundedBlocks', 'waitingBlocksNotBounded')}))
sys.exit(1 if record['waitingBlocksNotBounded'] else 0)
