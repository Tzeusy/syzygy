import * as fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import { issueBrief } from './brief.js';
import { checkDraft } from './check.js';
import { closeRun } from './close.js';
import { createCredentialProbe, credentialListFromEnv } from './credential-probe.js';
import { DECLARATIONS, RUN_DIRECTORY_CHOICES, allowExecution } from './execution-choice.js';
import { PERMITTING_ARM_ENABLED } from './execution-rule.js';
import { createPackageGateSources, type GateSources } from './gate-sources.js';
import { initRun } from './init.js';
import { checkInventory, inventoryBrief } from './inventory.js';
import { preflight } from './preflight.js';
import type { ReverifyOptions } from './reverify.js';
import { RUN_CONFIG_JSON_LIMITS } from './run-config.js';
import { renderRun, type DossierRenderer } from './render.js';
import { reviewCheck, reviewPacket } from './review.js';
import type { ScreenLoad } from './screen.js';
import { launchForm, sessionPrompt } from './session-handover.js';
import { runStatus } from './status.js';

/** The `syzygy dossier` command family (design "Command surface").
 *
 * Every command is non-interactive, prints a human summary and, with `--json`, the same content as
 * one JSON document. The human form is generated from that document, so the two cannot drift.
 * Exit status: 0 clean, 1 findings or refusal (reason printed), 2 usage error. The family serves no
 * route and opens no socket: it is a local program the operator's sessions run as the operator. */

export const EXIT = Object.freeze({ clean: 0, refused: 1, usage: 2 });

export const STATE_ROOT_ENV = 'SYZYGY_DOSSIER_STATE_ROOT';

export const DOSSIER_USAGE = `syzygy dossier — operator-agent dossier runs

Usage: syzygy dossier <command> [--json] [arguments]

Commands:
  preflight <url>     report whether the observation consent, the source-acquisition
                      registry entry and the classification and screening policy are
                      in force for the repository, the revisions the consent names,
                      any per-project statement, and whether D9 and the RFC7-20
                      reading are in force; the URL is parsed, never fetched
  init <clone> --url <url> --config <run.json> [--state-root <dir>]
                      check the start gates, pin the clone's HEAD to a consented
                      revision, decide whether the subject is governed, and make the
                      run directory under the state root (or $${STATE_ROOT_ENV});
                      there is no default state root
  brief <run>         re-verify the pinned revision and issue the authoring brief
                      (brief.md) and the draft schema (draft.schema.json) in the run
                      directory, starting the deadline clock; a run is briefed once.
                      The brief carries SEC-3's execution rule, quoted from the
                      adopted security.md
  allow-execution <run> --revision <pinned> --declare owner-started-session,owners-own-host,owner-attends
                      record the owner's execution choice for this one run and its
                      pinned revision, with the operator's three declarations; run it
                      personally, never through an agent. Refused while D9 is not in
                      force, after the brief, or for another run or revision. It is
                      not an execution consent and approves no execution profile
  check <run> [--draft <file>]
                      re-verify the pinned revision, refuse past the deadline or the
                      repair-cycle limit, check the draft (drafts/next.json by
                      default) against the objects at the pinned revision, read from
                      the object store of the clone init recorded and re-hashed,
                      freeze it as revision N
                      and write checks/rev-N.json; exit 1 on any finding
  session-prompt <run> inventory|review [--kind <kind>] [--tool <tool>] [--tool-version <v>] [--model <m>]
                      at a hand-over: make the inventory session's directory under
                      <state root>/<run id>.sessions/, beside the run directory and
                      holding only the inventory brief, print the fixed prompt and
                      the command that starts an interactive session there
                      (claude '<prompt>', also behind !, or codex '<prompt>'), and
                      record the prompt's digest; Syzygy starts nothing. The tool, version and
                      model default to the run's declared values. review --kind
                      fidelity|design builds that review's packet and copies it,
                      with its digest, into the review session's directory there
  launch-form <run> inventory|review terminal|bang [--kind fidelity|design]
                      record, once, how the operator declares the latest inventory
                      or review session (of the kind, fidelity by default) was
                      started; any other form is refused. An inventory or verdict
                      counts only once its launch form is recorded
  inventory-brief <run>
                      print Syzygy's own rendering of the latest inventory session's
                      brief, and whether the stored copy matches it
  inventory-check <run> [--inventory <file>]
                      check the inventory (the latest session's inventory.json by
                      default) as check checks a draft, refuse one declared under the
                      authoring session's identifier, freeze it as inventory/rev-N.json
                      and write inventory/checks/rev-N.json; exit 1 on any finding
  review-packet <run> --kind fidelity|design
                      build the fidelity packet from the latest passed draft revision
                      and the inventory of record (the draft without its discovery
                      account, the frozen inventory, every cited span as Syzygy reads
                      it now, the criteria and the verdict schema), or the design
                      packet from the latest site/<n>/ (every page without its
                      review-status region), write it under reviews/ with its digest
                      and print the digest
  review-check <run> [--kind fidelity|design] [--verdict <file>]
                      rebuild the packet and validate the verdict (the latest
                      session's verdict.json of the kind, fidelity by default):
                      schema, packet digest, pinned revision, session identifiers,
                      completeness, quotations and consistency; freeze it as
                      reviews/<kind>-verdict-N.json and record the result in
                      reviews/checks/; exit 1 when refused
  render <run>        verify the pinned revision again, re-derive every check of the
                      latest passed draft revision from objects read now, rebuild the
                      fidelity review of record, and render the dossier into a new
                      site/<n>/ with the run disclosure on every page and in
                      machine.json; a design review counts only while these pages,
                      outside the review-status region, are the pages it reviewed;
                      the draft layer is Unknown unless the owner's reading of
                      RFC7-20 is in force; exit 1 when refused
  close <run> [--usage-tokens <n>] [--usage-turns <n>]
                      verify the pinned revision again and write the run's
                      Execution Record (record.json), once, with the usage the
                      operator declares (a positive integer each, Inferred and
                      attributed to the operator, never a receipt) or, with none
                      declared, usage not recorded; it copies no prompt or
                      transcript body. Exit 1 when refused or on a
                      credential finding
  status <run>      report a run's state, limits spent, open findings and
                      reviews still required, from its run directory
  help                print this usage and exit

Every value status reports comes from files the agent sessions can write,
and is labelled Inferred. --json prints the same content as one JSON document;
the machine form, refusals included, is printed only with --json.
Exit status: 0 clean, 1 refusal, 2 usage error.
`;

export interface CliIo {
  readonly stdout: (text: string) => void;
  readonly stderr: (text: string) => void;
}

/** What the commands read besides their arguments. The defaults are the process environment, the system clock and the records in
 * this Syzygy checkout. */
export interface CliPorts {
  readonly env?: Readonly<Record<string, string | undefined>>;
  readonly now?: () => number;
  readonly sources?: GateSources;
  /** The object reader the step guard lists the pinned tree with; by default the re-hashing in-process reader. */
  readonly openReader?: ReverifyOptions['openReader'];
  /** The screen `check` applies; by default the policy the act chain puts in force in this checkout. */
  readonly loadScreen?: () => Promise<ScreenLoad>;
  /** The multi-page dossier renderer `render` draws through; the `syzygy` composition root injects it. Without it `render` refuses. */
  readonly renderer?: DossierRenderer;
}

/** The Syzygy checkout this package belongs to: packages/polaris-dossier/{src,dist} → the repository root. */
const RECORDS_ROOT = fileURLToPath(new URL('../../..', import.meta.url));

export async function runDossierCli(argv: readonly string[], io: CliIo, ports: CliPorts = {}): Promise<number> {
  const json = argv.includes('--json');
  const args = argv.filter((arg) => arg !== '--json');
  const now = ports.now ?? Date.now;
  const sources = (): GateSources => ports.sources ?? createPackageGateSources({ root: RECORDS_ROOT, now });
  const openReader = ports.openReader ? { openReader: ports.openReader } : {};
  const usageError = (detail: string): number => {
    io.stderr(`syzygy dossier: ${detail}\n\n${DOSSIER_USAGE}`);
    return EXIT.usage;
  };
  const refused = (document: object): number => {
    if (json) io.stdout(`${JSON.stringify(document, null, 2)}\n`);
    io.stderr(renderHuman(document));
    return EXIT.refused;
  };
  const report = (document: object, exit: number): number => {
    io.stdout(json ? `${JSON.stringify(document, null, 2)}\n` : renderHuman(document));
    return exit;
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
    if (!result.ok) return refused({ command: 'status', outcome: 'refused', reason: result.reason, ...(result.refusals ? { refusals: result.refusals } : {}) });
    return report(result.report, EXIT.clean);
  }
  if (command === 'preflight') {
    const flag = rest.find((arg) => arg.startsWith('-'));
    if (flag !== undefined) return usageError(`unknown option for preflight: ${flag}`);
    if (rest.length !== 1) return usageError('preflight takes exactly one argument, the repository URL');
    const result = await preflight(rest[0]!, sources(), now());
    if (!result.ok) return refused({ command: 'preflight', outcome: 'refused', reason: result.reason });
    return report(result.report, result.report.outcome === 'ready' ? EXIT.clean : EXIT.refused);
  }
  if (command === 'brief') {
    const flag = rest.find((arg) => arg.startsWith('-'));
    if (flag !== undefined) return usageError(`unknown option for brief: ${flag}`);
    if (rest.length !== 1) return usageError('brief takes exactly one argument, the run directory');
    const env = ports.env ?? process.env;
    const result = await issueBrief(rest[0]!, { sources: sources(), now, ...openReader, permitting: {
      enabled: PERMITTING_ARM_ENABLED, choices: RUN_DIRECTORY_CHOICES, probe: createCredentialProbe(credentialListFromEnv(env)),
    } });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  if (command === 'check') {
    const options = parseOptions(rest, ['--draft']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('check takes exactly one positional argument, the run directory');
    const draftFile = options.values.get('--draft');
    const env = ports.env ?? process.env;
    const result = await checkDraft(options.positional[0]!, draftFile === undefined ? {} : { draftFile }, {
      sources: sources(), now, probe: createCredentialProbe(credentialListFromEnv(env)), ...openReader, ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}),
    });
    if (!result.ok) return refused(result.refusal);
    return report(result.report, result.report.outcome === 'passed' ? EXIT.clean : EXIT.refused);
  }
  if (command === 'session-prompt') {
    const options = parseOptions(rest, ['--kind', '--tool', '--tool-version', '--model']);
    if (typeof options === 'string') return usageError(options);
    const [run, role, ...extra] = options.positional;
    if (run === undefined || (role !== 'inventory' && role !== 'review') || extra.length > 0) return usageError('session-prompt takes the run directory and a role, inventory or review');
    const v = options.values;
    const result = await sessionPrompt(run, {
      role, ...(v.has('--kind') ? { kind: v.get('--kind')! } : {}), ...(v.has('--tool') ? { tool: v.get('--tool')! } : {}),
      ...(v.has('--tool-version') ? { toolVersion: v.get('--tool-version')! } : {}), ...(v.has('--model') ? { model: v.get('--model')! } : {}),
    }, { sources: sources(), now, ...openReader, ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}) });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  if (command === 'review-packet') {
    const options = parseOptions(rest, ['--kind']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('review-packet takes exactly one positional argument, the run directory');
    const kind = options.values.get('--kind');
    if (kind === undefined) return usageError('review-packet requires --kind fidelity|design');
    const result = await reviewPacket(options.positional[0]!, { kind }, { sources: sources(), now, ...openReader, ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}) });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  if (command === 'review-check') {
    const options = parseOptions(rest, ['--verdict', '--kind']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('review-check takes exactly one positional argument, the run directory');
    const verdictFile = options.values.get('--verdict');
    const kind = options.values.get('--kind');
    const result = await reviewCheck(options.positional[0]!, { ...(verdictFile === undefined ? {} : { verdictFile }), ...(kind === undefined ? {} : { kind }) }, { sources: sources(), now, ...openReader, ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}) });
    if (!result.ok) return refused(result.refusal);
    return report(result.report, result.report.outcome === 'validated' ? EXIT.clean : EXIT.refused);
  }
  if (command === 'render') {
    const flag = rest.find((arg) => arg.startsWith('-'));
    if (flag !== undefined) return usageError(`unknown option for render: ${flag}`);
    if (rest.length !== 1) return usageError('render takes exactly one argument, the run directory');
    const env = ports.env ?? process.env;
    const result = await renderRun(rest[0]!, {
      sources: sources(), now, probe: createCredentialProbe(credentialListFromEnv(env)), ...openReader,
      ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}), ...(ports.renderer ? { renderer: ports.renderer } : {}),
    });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  if (command === 'close') {
    const options = parseOptions(rest, ['--usage-tokens', '--usage-turns']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('close takes exactly one positional argument, the run directory');
    const v = options.values;
    const env = ports.env ?? process.env;
    const result = await closeRun(options.positional[0]!, {
      ...(v.has('--usage-tokens') ? { usageTokens: v.get('--usage-tokens')! } : {}), ...(v.has('--usage-turns') ? { usageTurns: v.get('--usage-turns')! } : {}),
    }, { sources: sources(), now, probe: createCredentialProbe(credentialListFromEnv(env)), ...openReader, ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}) });
    if (!result.ok) return refused(result.refusal);
    return report(result.report, result.report.outcome === 'closed' ? EXIT.clean : EXIT.refused);
  }
  if (command === 'launch-form') {
    const options = parseOptions(rest, ['--kind']);
    if (typeof options === 'string') return usageError(options);
    const [run, role, form, ...extra] = options.positional;
    if (run === undefined || role === undefined || form === undefined || extra.length > 0) return usageError('launch-form takes the run directory, a role and the launch form the operator declares');
    const kind = options.values.get('--kind');
    const result = await launchForm(run, { role, form, ...(kind === undefined ? {} : { kind }) }, { sources: sources(), now, ...openReader });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  if (command === 'inventory-brief') {
    const flag = rest.find((arg) => arg.startsWith('-'));
    if (flag !== undefined) return usageError(`unknown option for inventory-brief: ${flag}`);
    if (rest.length !== 1) return usageError('inventory-brief takes exactly one argument, the run directory');
    const result = await inventoryBrief(rest[0]!, { sources: sources(), now, ...openReader });
    if (!result.ok) return refused(result.refusal);
    if (json) return report(result.report, EXIT.clean);
    const { brief, ...summary } = result.report;
    io.stdout(`${brief}\n${renderHuman(summary)}`);
    return EXIT.clean;
  }
  if (command === 'inventory-check') {
    const options = parseOptions(rest, ['--inventory']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('inventory-check takes exactly one positional argument, the run directory');
    const inventoryFile = options.values.get('--inventory');
    const env = ports.env ?? process.env;
    const result = await checkInventory(options.positional[0]!, inventoryFile === undefined ? {} : { inventoryFile }, {
      sources: sources(), now, probe: createCredentialProbe(credentialListFromEnv(env)), ...openReader, ...(ports.loadScreen ? { loadScreen: ports.loadScreen } : {}),
    });
    if (!result.ok) return refused(result.refusal);
    return report(result.report, result.report.outcome === 'passed' ? EXIT.clean : EXIT.refused);
  }
  if (command === 'allow-execution') {
    const options = parseOptions(rest, ['--revision', '--declare']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('allow-execution takes exactly one positional argument, the run directory');
    const revision = options.values.get('--revision'), declare = options.values.get('--declare');
    if (revision === undefined) return usageError('allow-execution requires --revision <pinned revision>');
    if (declare === undefined) return usageError(`allow-execution requires --declare ${Object.keys(DECLARATIONS).join(',')}`);
    const result = await allowExecution(options.positional[0]!, { revision, declarations: declare.split(',') }, { sources: sources(), now, ...openReader });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  if (command === 'init') {
    const options = parseOptions(rest, ['--url', '--config', '--state-root']);
    if (typeof options === 'string') return usageError(options);
    if (options.positional.length !== 1) return usageError('init takes exactly one positional argument, the clone directory');
    const url = options.values.get('--url'), configPath = options.values.get('--config');
    if (url === undefined || configPath === undefined) return usageError('init requires --url <url> and --config <run.json>');
    const env = ports.env ?? process.env;
    const stateRoot = options.values.get('--state-root') ?? env[STATE_ROOT_ENV];
    if (stateRoot === undefined || stateRoot === '') {
      return refused({ command: 'init', outcome: 'refused', stage: 'state-root', reason: `no state root: pass --state-root <dir> or set ${STATE_ROOT_ENV}; there is no default, and none is derived from the clone`, objectsRead: false });
    }
    const configText = readBounded(configPath, RUN_CONFIG_JSON_LIMITS.maxBytes);
    if (typeof configText !== 'string') return refused({ command: 'init', outcome: 'refused', stage: 'config', reason: configText.reason, objectsRead: false });
    const result = await initRun({ clone: options.positional[0]!, url, configText, stateRoot }, { sources: sources(), now });
    return result.ok ? report(result.report, EXIT.clean) : refused(result.refusal);
  }
  return usageError(`unknown dossier command: ${command}`);
}

/** `--name value` pairs (each at most once) and positional arguments; a description of the fault otherwise. */
function parseOptions(args: readonly string[], names: readonly string[]): { readonly values: ReadonlyMap<string, string>; readonly positional: readonly string[] } | string {
  const values = new Map<string, string>();
  const positional: string[] = [];
  for (let index = 0; index < args.length; index++) {
    const arg = args[index]!;
    if (!arg.startsWith('-')) { positional.push(arg); continue; }
    if (!names.includes(arg)) return `unknown option: ${arg}`;
    if (values.has(arg)) return `${arg} given more than once`;
    const value = args[index + 1];
    if (value === undefined || value.startsWith('-')) return `${arg} requires a value`;
    values.set(arg, value);
    index++;
  }
  return { values, positional };
}

function readBounded(file: string, limit: number): string | { readonly reason: string } {
  try {
    const stats = fs.statSync(file);
    if (!stats.isFile()) return { reason: `${file} is not a regular file` };
    if (stats.size > limit) return { reason: `${file} is larger than the ${limit}-byte configuration bound` };
    return fs.readFileSync(file, 'utf8');
  } catch (cause) {
    return { reason: `${file} cannot be read (${(cause as NodeJS.ErrnoException).code ?? 'unknown-error'})` };
  }
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
