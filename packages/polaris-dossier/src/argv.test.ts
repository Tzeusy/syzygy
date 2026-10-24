import { describe, expect, it } from 'vitest';
import { isArgvFault, readArgv, type ArgvSpec } from './argv.js';

// syzygy-bpyt.8.32 (the review of syzygy-bpyt.8.2, N1 and N5): what readArgv answers under each caller's policy, as literals. The
// policies are copies of the ones the callers pass: the daemon's parseCli (apps/syzygy/src/main.ts), cli.ts's one-argument and
// options readings, and `syzygy polaris`'s parseArgs (polaris.ts). Each table holds a row per predicate the policy reaches: `--`, a
// short group, a group starting with `-h`, a lone `-`, a negative number, an inline `--x=v`, a dash-led value, a repeat, a missing
// value, a boolean option and a stop option.

const DAEMON: ArgvSpec = { valued: ['--root', '--state-dir', '--port'], stopAt: ['--help', '-h'], dashValue: 'take', repeat: 'last', positionals: false };
const DOSSIER_ONE: ArgvSpec = { valued: [], dashValue: 'refuse', repeat: 'refuse', positionals: true };
/** `allow-execution`'s options; every options command is read the same way. */
const DOSSIER_OPTIONS: ArgvSpec = { valued: ['--revision', '--declare'], dashValue: 'refuse', repeat: 'refuse', positionals: true };
const POLARIS: ArgvSpec = {
  valued: ['--clone', '--revision', '--state-root', '--deadline', '--audience', '--model', '--repair-cycles', '--questions', '--token-budget',
    '--turn-budget', '--operator', '--attach', '--stop', '--resume', '--tmux-session'],
  booleans: ['--author-skip-permissions', '--no-attach', '--supervise', '--help', '-h'], dashValue: 'take', repeat: 'last', positionals: true,
};

/** The answer as plain data: a fault as it is, a read with its map and set spelled out. */
function answer(args: readonly string[], spec: ArgvSpec): unknown {
  const read = readArgv(args, spec);
  if (isArgvFault(read)) return read;
  return { values: Object.fromEntries(read.values), flags: [...read.flags], positional: read.positional, ...(read.stoppedAt === undefined ? {} : { stoppedAt: read.stoppedAt }) };
}

describe('readArgv under the daemon policy: values taken whatever they start with, the last of a repeat, no positionals, stop at help', () => {
  it.each<[readonly string[], unknown]>([
    [[], { values: {}, flags: [], positional: [] }],
    [['--root', '/r', '--state-dir', '/s', '--port', '0'], { values: { '--root': '/r', '--state-dir': '/s', '--port': '0' }, flags: [], positional: [] }],
    [['--port', '1', '--port', '2'], { values: { '--port': '2' }, flags: [], positional: [] }],
    [['--root', '-x'], { values: { '--root': '-x' }, flags: [], positional: [] }],
    [['--port', '--help'], { values: { '--port': '--help' }, flags: [], positional: [] }],
    [['--port'], { fault: 'missing-value', arg: '--port' }],
    [['--help', '--bogus', 'x'], { values: {}, flags: [], positional: [], stoppedAt: '--help' }],
    [['--port', '1', '-h', '--root'], { values: { '--port': '1' }, flags: [], positional: [], stoppedAt: '-h' }],
    [['dossier'], { fault: 'unknown', arg: 'dossier' }],
    [['--', '--help'], { fault: 'unknown', arg: '--' }],
    [['-hx'], { fault: 'unknown', arg: '-hx' }],
    [['--help=1'], { fault: 'unknown', arg: '--help=1' }],
    [['--port=5'], { fault: 'unknown', arg: '--port=5' }],
    [['-abc'], { fault: 'unknown', arg: '-abc' }],
    [['-'], { fault: 'unknown', arg: '-' }],
    [['-5'], { fault: 'unknown', arg: '-5' }],
    [['--bogus'], { fault: 'unknown', arg: '--bogus' }],
  ])('%j reads as %j', (args, expected) => {
    expect(answer(args, DAEMON)).toEqual(expected);
  });
});

describe('readArgv under the dossier one-argument policy: positionals only', () => {
  it.each<[readonly string[], unknown]>([
    [['run'], { values: {}, flags: [], positional: ['run'] }],
    [['a', 'b'], { values: {}, flags: [], positional: ['a', 'b'] }],
    [['--', 'run'], { fault: 'unknown', arg: '--' }],
    [['run', '-'], { fault: 'unknown', arg: '-' }],
    [['-5'], { fault: 'unknown', arg: '-5' }],
    [['-abc'], { fault: 'unknown', arg: '-abc' }],
    [['-hx'], { fault: 'unknown', arg: '-hx' }],
    [['--x=v'], { fault: 'unknown', arg: '--x=v' }],
    [['run', '--draft', 'd'], { fault: 'unknown', arg: '--draft' }],
    [['--help'], { fault: 'unknown', arg: '--help' }],
  ])('%j reads as %j', (args, expected) => {
    expect(answer(args, DOSSIER_ONE)).toEqual(expected);
  });
});

describe('readArgv under the dossier options policy: a dash-led value and a repeat refused', () => {
  it.each<[readonly string[], unknown]>([
    [['run', '--revision', 'abc', '--declare', 'd'], { values: { '--revision': 'abc', '--declare': 'd' }, flags: [], positional: ['run'] }],
    [['run', '--revision', '-x'], { fault: 'missing-value', arg: '--revision' }],
    [['--revision', '--declare', 'd'], { fault: 'missing-value', arg: '--revision' }],
    [['--revision', '-'], { fault: 'missing-value', arg: '--revision' }],
    [['--revision', 'a', '--revision', 'b'], { fault: 'repeated', arg: '--revision' }],
    [['run', '--revision'], { fault: 'missing-value', arg: '--revision' }],
    [['--revision=abc'], { fault: 'unknown', arg: '--revision=abc' }],
    [['run', '--', '--revision', 'x'], { fault: 'unknown', arg: '--' }],
    [['--revision', 'a', '-'], { fault: 'unknown', arg: '-' }],
    [['-5'], { fault: 'unknown', arg: '-5' }],
    [['-rd'], { fault: 'unknown', arg: '-rd' }],
    [['-hx'], { fault: 'unknown', arg: '-hx' }],
    [['run', '--kind', 'k'], { fault: 'unknown', arg: '--kind' }],
  ])('%j reads as %j', (args, expected) => {
    expect(answer(args, DOSSIER_OPTIONS)).toEqual(expected);
  });
});

describe('readArgv under the polaris policy: boolean options, values taken whatever they start with, the last of a repeat', () => {
  it.each<[readonly string[], unknown]>([
    [['https://github.com/o/r'], { values: {}, flags: [], positional: ['https://github.com/o/r'] }],
    [['--supervise', '--no-attach'], { values: {}, flags: ['--supervise', '--no-attach'], positional: [] }],
    [['url', '-h'], { values: {}, flags: ['-h'], positional: ['url'] }],
    [['--model', 'a', '--model', 'b', 'url'], { values: { '--model': 'b' }, flags: [], positional: ['url'] }],
    [['--operator', '-x', 'url'], { values: { '--operator': '-x' }, flags: [], positional: ['url'] }],
    [['--model', '--help'], { values: { '--model': '--help' }, flags: [], positional: [] }],
    [['url', '--deadline'], { fault: 'missing-value', arg: '--deadline' }],
    [['--', 'url'], { fault: 'unknown', arg: '--' }],
    [['-'], { fault: 'unknown', arg: '-' }],
    [['-hx'], { fault: 'unknown', arg: '-hx' }],
    [['-abc'], { fault: 'unknown', arg: '-abc' }],
    [['--supervise=1'], { fault: 'unknown', arg: '--supervise=1' }],
    [['-5'], { fault: 'unknown', arg: '-5' }],
    [['--bogus'], { fault: 'unknown', arg: '--bogus' }],
  ])('%j reads as %j', (args, expected) => {
    expect(answer(args, POLARIS)).toEqual(expected);
  });
});

describe('a spec naming an option readArgv could never see', () => {
  it.each<[ArgvSpec, string]>([
    [{ ...DOSSIER_ONE, valued: ['-o'] }, 'argv: the valued option -o is not --<name>'],
    [{ ...DOSSIER_ONE, valued: ['--'] }, 'argv: the valued option -- is not --<name>'],
    [{ ...DOSSIER_ONE, valued: ['---out'] }, 'argv: the valued option ---out is not --<name>'],
    [{ ...DOSSIER_ONE, valued: ['--out=x'] }, 'argv: the valued option --out=x is not --<name>'],
    [{ ...DOSSIER_ONE, valued: ['out'] }, 'argv: the valued option out is not --<name>'],
    [{ ...DOSSIER_ONE, booleans: ['json'] }, 'argv: the option json is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, booleans: ['-'] }, 'argv: the option - is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, booleans: ['-vv'] }, 'argv: the option -vv is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, stopAt: ['help'] }, 'argv: the option help is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, stopAt: ['--'] }, 'argv: the option -- is neither --<name> nor -<c>'],
  ])('throws for %j, before reading anything', (spec, message) => {
    expect(() => readArgv(['run'], spec)).toThrow(new Error(message));
  });

  it('reads a short boolean option and a short stop option, which are judged by the whole argument', () => {
    expect(answer(['-v', 'run'], { ...DOSSIER_ONE, booleans: ['-v'] })).toEqual({ values: {}, flags: ['-v'], positional: ['run'] });
    expect(answer(['run', '-q', '-x'], { ...DOSSIER_ONE, stopAt: ['-q'] })).toEqual({ values: {}, flags: [], positional: ['run'], stoppedAt: '-q' });
  });
});
