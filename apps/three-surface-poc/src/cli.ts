export interface PocCliConfig {
  readonly repoRoot: string;
  readonly stateDir?: string | undefined;
  readonly port: number;
}

export type PocCliParse =
  | { readonly kind: 'run'; readonly config: PocCliConfig }
  | { readonly kind: 'help' }
  | { readonly kind: 'invalid'; readonly detail: string };

const DEFAULT_PORT = 7478;

export function parsePocCli(argv: readonly string[]): PocCliParse {
  if (argv.includes('--help') || argv.includes('-h')) {
    return { kind: 'help' };
  }

  const values = new Map<string, string>();
  for (let index = 0; index < argv.length; index++) {
    const flag = argv[index];
    if (flag !== '--repo' && flag !== '--state-dir' && flag !== '--port') {
      return { kind: 'invalid', detail: `unknown argument: ${flag ?? ''}` };
    }
    if (values.has(flag)) {
      return { kind: 'invalid', detail: `${flag} may be supplied exactly once` };
    }
    const value = argv[index + 1];
    if (value === undefined || value.startsWith('--')) {
      return { kind: 'invalid', detail: `${flag} requires a value` };
    }
    values.set(flag, value);
    index++;
  }

  const repoRoot = values.get('--repo');
  if (repoRoot === undefined || repoRoot.trim() === '') {
    return {
      kind: 'invalid',
      detail: '--repo is required; this POC observes exactly one explicit repository',
    };
  }
  const portText = values.get('--port') ?? String(DEFAULT_PORT);
  const port = Number(portText);
  if (!Number.isInteger(port) || port < 0 || port > 65535) {
    return {
      kind: 'invalid',
      detail: `port must be an integer in [0, 65535]; got \`${portText}\``,
    };
  }

  return {
    kind: 'run',
    config: {
      repoRoot,
      stateDir: values.get('--state-dir'),
      port,
    },
  };
}
