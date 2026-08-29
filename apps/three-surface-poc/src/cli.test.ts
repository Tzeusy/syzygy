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
});
