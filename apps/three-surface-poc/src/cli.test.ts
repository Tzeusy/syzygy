import { describe, expect, it } from 'vitest';

import { parsePocCli } from './cli.js';

describe('three-surface POC CLI', () => {
  it('accepts one explicit repository and rejects ambiguous or invalid input', () => {
    expect(
      parsePocCli([
        '--repo',
        '/work/butlers',
        '--state-dir',
        '/tmp/syzygy-poc',
        '--port',
        '0',
      ]),
    ).toEqual({
      kind: 'run',
      config: {
        repoRoot: '/work/butlers',
        stateDir: '/tmp/syzygy-poc',
        port: 0,
        watch: false,
      },
    });
    expect(parsePocCli([])).toEqual({
      kind: 'invalid',
      detail: '--repo is required; this POC observes exactly one explicit repository',
    });
    expect(parsePocCli(['--repo', '/work/butlers', '--repo', '/work/other'])).toEqual({
      kind: 'invalid',
      detail: '--repo may be supplied exactly once',
    });
    expect(parsePocCli(['--repo', '/work/butlers', '--port', '70000'])).toEqual({
      kind: 'invalid',
      detail: 'port must be an integer in [0, 65535]; got `70000`',
    });
    expect(parsePocCli(['--help'])).toEqual({ kind: 'help' });
  });

  it('takes --watch as a value-less flag, exactly once (syzygy-u05.2)', () => {
    expect(parsePocCli(['--watch', '--repo', '/work/butlers'])).toEqual({
      kind: 'run',
      config: { repoRoot: '/work/butlers', stateDir: undefined, port: 7478, watch: true },
    });
    expect(parsePocCli(['--repo', '/work/butlers', '--watch', '--watch'])).toEqual({
      kind: 'invalid',
      detail: '--watch may be supplied exactly once',
    });
    expect(parsePocCli(['--repo', '--watch'])).toEqual({ kind: 'invalid', detail: '--repo requires a value' });
  });
});
