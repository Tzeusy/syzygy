import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { renderHuman, runDossierCli } from './cli.js';
import { parseRunConfig } from './run-config.js';
import { encodeRunRecord } from './run-record.js';

// Design "Command surface": non-interactive; a human summary and, with --json, the same content as
// one JSON document; exit status 0 clean, 1 refusal, 2 usage error.
const run = (argv: readonly string[]): { code: number; stdout: string; stderr: string } => {
  let stdout = '';
  let stderr = '';
  const code = runDossierCli(argv, { stdout: (text) => { stdout += text; }, stderr: (text) => { stderr += text; } });
  return { code, stdout, stderr };
};

let runDir: string;
beforeEach(() => {
  runDir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-cli-')));
  const parsed = parseRunConfig(JSON.stringify({
    operator: 'Tzeusy', agentTool: 'claude-code', agentToolVersion: '2.1.0', agentProvider: 'anthropic',
    model: 'claude-opus-5-5', deadline: 'PT1H', agentTokenBudget: 100_000, maxRepairCycles: 1, maxQuestions: 2,
    audience: 'an operator', operatorIsOwner: true,
  }));
  if (!parsed.ok) throw new Error('fixture configuration refused');
  fs.writeFileSync(path.join(runDir, 'run.json'), encodeRunRecord(parsed.config));
});
afterEach(() => fs.rmSync(runDir, { recursive: true, force: true }));

/** Every leaf of a JSON document as `dotted.key: value`, computed here rather than by the module. */
const leaves = (value: unknown, key = ''): string[] => {
  if (value !== null && typeof value === 'object') {
    const entries = Object.entries(value);
    if (entries.length === 0) return [`${key}: (none)`];
    return entries.flatMap(([child, item]) => leaves(item, key === '' ? child : `${key}.${child}`));
  }
  return [`${key}: ${String(value)}`];
};

describe('syzygy dossier', () => {
  it('exits 2 with usage when no command is given', () => {
    const result = run([]);
    expect(result.code).toBe(2);
    expect(result.stdout).toBe('');
    expect(result.stderr.startsWith('syzygy dossier: a command is required\n\nsyzygy dossier — operator-agent dossier runs\n')).toBe(true);
  });

  it.each([[['init']], [['preflight', 'https://example.invalid/r']], [['frobnicate']]])('exits 2 for a command this build does not have (%j)', (argv) => {
    const result = run(argv);
    expect(result.code).toBe(2);
    expect(result.stderr.startsWith(`syzygy dossier: unknown dossier command: ${argv[0]}\n`)).toBe(true);
  });

  it.each([[['status']], [['status', 'a', 'b']], [['status', '--verbose', 'a']], [['help', 'extra']]])('exits 2 for malformed arguments (%j)', (argv) => {
    expect(run(argv).code).toBe(2);
  });

  it.each([[['help']], [['--help']], [['-h']]])('prints usage and exits 0 for %j', (argv) => {
    const result = run(argv);
    expect(result.code).toBe(0);
    expect(result.stderr).toBe('');
    expect(result.stdout.startsWith('syzygy dossier — operator-agent dossier runs\n')).toBe(true);
  });

  it('reports status, exit 0, with the human form carrying every JSON leaf in order', () => {
    const human = run(['status', runDir]);
    const json = run(['status', runDir, '--json']);
    expect(human.code).toBe(0);
    expect(json.code).toBe(0);
    expect(human.stderr + json.stderr).toBe('');
    const document = JSON.parse(json.stdout) as Record<string, unknown>;
    expect(document['label']).toBe('Inferred');
    expect(human.stdout).toBe(`${leaves(document).join('\n')}\n`);
    expect(human.stdout).toContain('principal.credentialIdentity: Unknown\n');
  });

  it('accepts --json before the command', () => {
    const result = run(['--json', 'status', runDir]);
    expect(result.code).toBe(0);
    expect(JSON.parse(result.stdout).command).toBe('status');
  });

  it('refuses an unreadable run with exit 1, the reason on stderr and, with --json, the same reason as JSON', () => {
    const missing = path.join(runDir, 'absent');
    const human = run(['status', missing]);
    expect(human).toEqual({
      code: 1,
      stdout: '',
      stderr: `command: status\noutcome: refused\nreason: run directory ${missing} cannot be read (ENOENT)\n`,
    });
    const json = run(['status', missing, '--json']);
    expect(json.code).toBe(1);
    expect(JSON.parse(json.stdout)).toEqual({ command: 'status', outcome: 'refused', reason: `run directory ${missing} cannot be read (ENOENT)` });
  });

  it('renders an empty list or object as (none)', () => {
    expect(renderHuman({ a: [], b: {} })).toBe('a: (none)\nb: (none)\n');
  });
});

describe('no route and no credential', () => {
  // REQ-polaris-generation-033: the commands serve no route, accept no network request and hold no
  // credential. A static sweep of the package's sources: no module that opens a socket is imported.
  const SRC = path.dirname(fileURLToPath(import.meta.url));
  const NETWORK = /from\s+['"](?:node:)?(?:net|http|https|http2|tls|dgram)['"]|import\(\s*['"](?:node:)?(?:net|http|https|http2|tls|dgram)['"]\s*\)/;
  const sources = fs.readdirSync(SRC).filter((name) => name.endsWith('.ts') && !name.endsWith('.test.ts')).sort();

  it('sweeps a non-empty population of source files', () => {
    expect(sources).toEqual(['cli.ts', 'git-object-reader.ts', 'index.ts', 'run-config.ts', 'run-record.ts', 'state-directory.ts', 'status.ts']);
  });

  it.each(sources.map((name) => [name]))('%s imports no network module', (name) => {
    expect(NETWORK.test(fs.readFileSync(path.join(SRC, name), 'utf8'))).toBe(false);
  });

  it('the sweep pattern catches a network import (its own mutant)', () => {
    expect(NETWORK.test("import * as net from 'node:net';")).toBe(true);
    expect(NETWORK.test("const http = await import('http');")).toBe(true);
  });
});
