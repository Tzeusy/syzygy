import { runStatus } from './status.js';

/** The `syzygy dossier` command family (design "Command surface").
 *
 * Every command is non-interactive, prints a human summary and, with `--json`, the same content as
 * one JSON document. The human form is generated from that document, so the two cannot drift.
 * Exit status: 0 clean, 1 findings or refusal (reason printed), 2 usage error. The family serves no
 * route and opens no socket: it is a local program the operator's sessions run as the operator. */

export const EXIT = Object.freeze({ clean: 0, refused: 1, usage: 2 });

export const DOSSIER_USAGE = `syzygy dossier — operator-agent dossier runs

Usage: syzygy dossier <command> [--json] [arguments]

Commands:
  status <run>        report a run's state, limits spent, open findings and
                      reviews still required, from its run directory
  help                print this usage and exit

Every value status reports comes from files the agent sessions can write,
and is labelled Inferred. --json prints the same content as one JSON document.
Exit status: 0 clean, 1 refusal, 2 usage error.
`;

export interface CliIo {
  readonly stdout: (text: string) => void;
  readonly stderr: (text: string) => void;
}

export function runDossierCli(argv: readonly string[], io: CliIo): number {
  const json = argv.includes('--json');
  const args = argv.filter((arg) => arg !== '--json');
  const usageError = (detail: string): number => {
    io.stderr(`syzygy dossier: ${detail}\n\n${DOSSIER_USAGE}`);
    return EXIT.usage;
  };
  const [command, ...rest] = args;
  if (command === undefined) return usageError('a command is required');
  if (command === 'help' || command === '--help' || command === '-h') {
    if (rest.length > 0) return usageError(`help takes no arguments; got ${rest.join(' ')}`);
    io.stdout(DOSSIER_USAGE);
    return EXIT.clean;
  }
  if (command === 'status') {
    const flag = rest.find((arg) => arg.startsWith('-'));
    if (flag !== undefined) return usageError(`unknown option for status: ${flag}`);
    if (rest.length !== 1) return usageError('status takes exactly one argument, the run directory');
    const result = runStatus(rest[0]!);
    if (!result.ok) {
      const document = { command: 'status', outcome: 'refused', reason: result.reason, ...(result.refusals ? { refusals: result.refusals } : {}) };
      if (json) io.stdout(`${JSON.stringify(document, null, 2)}\n`);
      io.stderr(renderHuman(document));
      return EXIT.refused;
    }
    io.stdout(json ? `${JSON.stringify(result.report, null, 2)}\n` : renderHuman(result.report));
    return EXIT.clean;
  }
  return usageError(`unknown dossier command: ${command}`);
}

/** One `key: value` line per leaf of the document, in document order, keys joined by dots. */
export function renderHuman(document: object): string {
  const lines: string[] = [];
  const walk = (value: unknown, key: string): void => {
    if (value !== null && typeof value === 'object') {
      const entries = Array.isArray(value) ? value.map((item, index) => [String(index), item] as const) : Object.entries(value);
      if (entries.length === 0) lines.push(`${key}: (none)`);
      for (const [child, item] of entries) walk(item, key === '' ? child : `${key}.${child}`);
      return;
    }
    lines.push(`${key}: ${String(value)}`);
  };
  walk(document, '');
  return `${lines.join('\n')}\n`;
}
