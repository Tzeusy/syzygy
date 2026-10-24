import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';
import { isArgvFault, readArgv, type ArgvSpec } from './argv.js';

// syzygy-bpyt.8.32 (the review of syzygy-bpyt.8.2, N1 and N5): what readArgv answers under each caller's policy, as literals. The
// policies are copies of the ones the callers pass: the daemon's parseCli (apps/syzygy/src/main.ts), cli.ts's one-argument and
// options readings, and `syzygy polaris`'s parseArgs (polaris.ts). Each table holds a row per predicate the policy reaches: `--`, a
// short group, a group starting with `-h`, a lone `-`, a negative number, an inline `--x=v`, a dash-led value, a repeat, a missing
// value, a boolean option and a stop option, and since 8.34 an empty value and a repeat whose second value is missing. The last block checks each copy against the spec its caller passes, read from the
// caller's syntax tree, so a caller's policy cannot drift from its copy unseen (syzygy-bpyt.8.34, the review of 8.32, N2); 8.5 is to
// export each spec and pin it once.

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
    [['--root', ''], { values: { '--root': '' }, flags: [], positional: [] }],
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
    [['run', '--revision', 'a', '--revision'], { fault: 'repeated', arg: '--revision' }],
    [['run', '--revision', 'a', '--revision', '-x'], { fault: 'repeated', arg: '--revision' }],
    [['run', '--revision', ''], { values: { '--revision': '' }, flags: [], positional: ['run'] }],
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
    [['--model', '', 'url'], { values: { '--model': '' }, flags: [], positional: ['url'] }],
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
    [{ ...DOSSIER_ONE, valued: ['--out='] }, 'argv: the valued option --out= is not --<name>'],
    [{ ...DOSSIER_ONE, valued: ['out'] }, 'argv: the valued option out is not --<name>'],
    [{ ...DOSSIER_ONE, booleans: ['json'] }, 'argv: the option json is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, booleans: ['-'] }, 'argv: the option - is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, booleans: ['-vv'] }, 'argv: the option -vv is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, stopAt: ['help'] }, 'argv: the option help is neither --<name> nor -<c>'],
    [{ ...DOSSIER_ONE, stopAt: ['--'] }, 'argv: the option -- is neither --<name> nor -<c>'],
  ])('throws for %j, before reading anything', (spec, message) => {
    expect(() => readArgv(['run'], spec)).toThrow(new Error(message));
  });

  it('throws for such a spec even when the arguments would fault first', () => {
    expect(() => readArgv(['--bogus'], { ...DOSSIER_ONE, valued: ['-o'] })).toThrow(new Error('argv: the valued option -o is not --<name>'));
  });

  it('reads a short boolean option and a short stop option, which are judged by the whole argument', () => {
    expect(answer(['-v', 'run'], { ...DOSSIER_ONE, booleans: ['-v'] })).toEqual({ values: {}, flags: ['-v'], positional: ['run'] });
    expect(answer(['run', '-q', '-x'], { ...DOSSIER_ONE, stopAt: ['-q'] })).toEqual({ values: {}, flags: [], positional: ['run'], stoppedAt: '-q' });
  });
});

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));

/** A spec as its caller writes it, as plain data: an expression that is no literal reads as `{ expression: <its text> }`. */
function literal(node: ts.Expression, source: ts.SourceFile): unknown {
  if (ts.isStringLiteralLike(node)) return node.text;
  if (node.kind === ts.SyntaxKind.TrueKeyword) return true;
  if (node.kind === ts.SyntaxKind.FalseKeyword) return false;
  if (ts.isArrayLiteralExpression(node)) return node.elements.map((element) => literal(element, source));
  if (ts.isObjectLiteralExpression(node)) {
    return Object.fromEntries(node.properties.map((property) => (ts.isPropertyAssignment(property)
      ? [ts.isStringLiteral(property.name) ? property.name.text : property.name.getText(source), literal(property.initializer, source)]
      : [property.getText(source), { unsupported: ts.SyntaxKind[property.kind] }])));
  }
  return { expression: node.getText(source) };
}

/** Every non-test source module of the workspace that names readArgv, and every call of it there with the spec it passes. */
function readArgvCallers(): { modules: string[]; calls: { module: string; spec: unknown }[] } {
  const sources = ['apps', 'packages'].flatMap((parent) => fs.readdirSync(path.join(ROOT, parent)).map((name) => `${parent}/${name}/src`))
    .filter((dir) => fs.existsSync(path.join(ROOT, dir)))
    .flatMap((dir) => fs.readdirSync(path.join(ROOT, dir), { recursive: true, encoding: 'utf8' }).map((file) => `${dir}/${file}`))
    .filter((module) => module.endsWith('.ts') && !module.endsWith('.test.ts')).sort();
  const modules: string[] = [];
  const calls: { module: string; spec: unknown }[] = [];
  for (const module of sources) {
    const text = fs.readFileSync(path.join(ROOT, module), 'utf8');
    if (!text.includes('readArgv')) continue;
    modules.push(module);
    const source = ts.createSourceFile(module, text, ts.ScriptTarget.Latest, true);
    const visit = (node: ts.Node): void => {
      if (ts.isCallExpression(node) && ts.isIdentifier(node.expression) && node.expression.text === 'readArgv') {
        calls.push({ module, spec: node.arguments[1] === undefined ? undefined : literal(node.arguments[1], source) });
      }
      ts.forEachChild(node, visit);
    };
    visit(source);
  }
  return { modules, calls };
}

describe('each policy copy above, against the spec its caller passes', () => {
  it('is the spec of every readArgv call, and no other module names readArgv', () => {
    const { modules, calls } = readArgvCallers();
    expect(modules).toEqual(['apps/syzygy/src/main.ts', 'packages/polaris-dossier/src/argv.ts', 'packages/polaris-dossier/src/cli.ts', 'packages/polaris-dossier/src/polaris.ts']);
    expect(calls).toEqual([
      { module: 'apps/syzygy/src/main.ts', spec: DAEMON },
      { module: 'packages/polaris-dossier/src/cli.ts', spec: DOSSIER_ONE },
      { module: 'packages/polaris-dossier/src/cli.ts', spec: { ...DOSSIER_OPTIONS, valued: { expression: 'shape.options' } } },
      { module: 'packages/polaris-dossier/src/polaris.ts', spec: POLARIS },
    ]);
  });

  it("names allow-execution's options as the dossier options policy's", () => {
    const module = 'packages/polaris-dossier/src/cli.ts';
    const source = ts.createSourceFile(module, fs.readFileSync(path.join(ROOT, module), 'utf8'), ts.ScriptTarget.Latest, true);
    const found: unknown[] = [];
    const visit = (node: ts.Node): void => {
      if (ts.isPropertyAssignment(node) && ts.isStringLiteral(node.name) && node.name.text === 'allow-execution' && ts.isObjectLiteralExpression(node.initializer)) {
        const args = node.initializer.properties.find((property) => ts.isPropertyAssignment(property) && property.name.getText(source) === 'args');
        if (args !== undefined && ts.isPropertyAssignment(args)) found.push(literal(args.initializer, source));
      }
      ts.forEachChild(node, visit);
    };
    visit(source);
    expect(found).toEqual([{ kind: 'options', options: DOSSIER_OPTIONS.valued, noun: { expression: 'RUN' } }]);
  });
});
