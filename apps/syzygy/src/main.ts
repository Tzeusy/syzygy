// syzygy — the Capability 1 local daemon entry point (RT3).
//
// Starts from a fresh clone with no prior state: observes the given
// repository root, assembles the observation → consent → evaluation
// pipeline (packages/cap1-daemon), and serves HTTP on 127.0.0.1 with
// credential-classed admission. Prints the bound address and the
// credential file's LOCATION — never the credential value.
//
// Configuration (flags win over environment; defaults last):
//   --root <dir>        observed repository root
//                       (env SYZYGY_OBSERVED_ROOT; default: cwd)
//   --state-dir <dir>   daemon state directory — the only startup
//                       write location; must NOT lie inside the
//                       observed root's `openspec/` or `.syzygy/`
//                       (env SYZYGY_STATE_DIR;
//                        default: <root>/.syzygy-daemon-state — a
//                        SIBLING of `.syzygy/`, deliberately outside
//                        the governed plane)
//   --port <n>          TCP port; 0 = ephemeral
//                       (env SYZYGY_PORT; default: 7477)
//   --help              print usage and exit
//
// This file is the composition root: the ONE place a clock is read (the
// evaluation's as-of instant, injected into the pipeline — RFC2-3) and
// the one place process signals are handled (clean shutdown on
// SIGINT/SIGTERM).

import * as fs from 'node:fs';
import { registerHooks } from 'node:module';
import * as path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

// The workspace packages export TypeScript SOURCE (`./src/index.ts`)
// for vitest and tsc; plain `node` cannot execute those (its type
// stripping does not remap `./x.js` specifiers to `./x.ts` sources).
// This bootstrap therefore redirects the two workspace bare specifiers
// to their COMPILED `dist/` entries — built by `npm run build` — before
// anything imports them. Confined to this composition root; no package
// manifest is altered.
const HERE = path.dirname(fileURLToPath(import.meta.url)); // apps/syzygy/{src,dist}
const REPO_ROOT = path.resolve(HERE, '..', '..', '..');
const WORKSPACE_DIST_ENTRIES: Readonly<Record<string, string>> = {
  '@syzygy/cap1-core': path.join(REPO_ROOT, 'packages', 'cap1-core', 'dist', 'index.js'),
  '@syzygy/cap1-daemon': path.join(REPO_ROOT, 'packages', 'cap1-daemon', 'dist', 'index.js'),
};
registerHooks({
  resolve(specifier, context, nextResolve) {
    const mapped = WORKSPACE_DIST_ENTRIES[specifier];
    if (mapped !== undefined) {
      return { url: pathToFileURL(mapped).href, shortCircuit: true };
    }
    return nextResolve(specifier, context);
  },
});

// Imported AFTER the hook is registered, so the bare specifier resolves
// to the compiled entry at runtime (types still come from the source).
const daemonModule = await import('@syzygy/cap1-daemon');
const { createDaemon, evaluateProject, humanRoutes, machineRoutes } = daemonModule;
type EntrySourceRead = import('@syzygy/cap1-daemon').EntrySourceRead;

const DEFAULT_PORT = 7477;
const DEFAULT_STATE_DIR_NAME = '.syzygy-daemon-state';

const USAGE = `syzygy — Capability 1 local daemon

Usage: node apps/syzygy/dist/main.js [options]

Options:
  --root <dir>        observed repository root (env SYZYGY_OBSERVED_ROOT; default: cwd)
  --state-dir <dir>   daemon state directory (env SYZYGY_STATE_DIR;
                      default: <root>/${DEFAULT_STATE_DIR_NAME});
                      refused if inside <root>/openspec or <root>/.syzygy
  --port <n>          TCP port, 0 for ephemeral (env SYZYGY_PORT; default: ${DEFAULT_PORT})
  --help              print this usage and exit
`;

interface CliConfig {
  readonly root: string;
  readonly stateDir: string;
  readonly port: number;
}

type CliParse =
  | { readonly kind: 'run'; readonly config: CliConfig }
  | { readonly kind: 'help' }
  | { readonly kind: 'invalid'; readonly detail: string };

function parseCli(argv: readonly string[], env: NodeJS.ProcessEnv): CliParse {
  const flags = new Map<string, string>();
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--help' || arg === '-h') {
      return { kind: 'help' };
    }
    if (arg === '--root' || arg === '--state-dir' || arg === '--port') {
      const value = argv[i + 1];
      if (value === undefined) {
        return { kind: 'invalid', detail: `${arg} requires a value` };
      }
      flags.set(arg, value);
      i++;
      continue;
    }
    return { kind: 'invalid', detail: `unknown argument: ${arg ?? ''}` };
  }

  const root = path.resolve(
    flags.get('--root') ?? env['SYZYGY_OBSERVED_ROOT'] ?? process.cwd(),
  );
  const stateDir = path.resolve(
    flags.get('--state-dir') ??
      env['SYZYGY_STATE_DIR'] ??
      path.join(root, DEFAULT_STATE_DIR_NAME),
  );

  const portText = flags.get('--port') ?? env['SYZYGY_PORT'] ?? String(DEFAULT_PORT);
  const port = Number(portText);
  if (!Number.isInteger(port) || port < 0 || port > 65535) {
    return { kind: 'invalid', detail: `port must be an integer in [0, 65535]; got \`${portText}\`` };
  }

  // The state directory may never lie inside the governed plane: the
  // daemon's state writes are outside `openspec/**` and `.syzygy/**`
  // by construction, so pointing state INTO them is refused, named.
  // This lexical pass keeps parseCli pure (no filesystem); symlink
  // reality is judged by `governedPlaneViolation` in main() (RTF-1).
  for (const governed of ['openspec', '.syzygy']) {
    const governedRoot = path.join(root, governed);
    if (stateDir === governedRoot || stateDir.startsWith(governedRoot + path.sep)) {
      return {
        kind: 'invalid',
        detail: `state directory ${stateDir} lies inside the governed plane (${governedRoot}); choose a location outside openspec/ and .syzygy/`,
      };
    }
  }

  return { kind: 'run', config: { root, stateDir, port } };
}

// --- Governed-plane containment by symlink reality (RTF-1) ---------------

/** Nearest existing ancestor of an absolute path (always terminates at '/'). */
function nearestExistingAncestor(absolutePath: string): string {
  let current = absolutePath;
  for (;;) {
    if (fs.existsSync(current)) {
      return current;
    }
    const parent = path.dirname(current);
    if (parent === current) {
      return current;
    }
    current = parent;
  }
}

/**
 * Real filesystem location of a (possibly not-yet-created) absolute
 * path: realpath the nearest EXISTING ancestor, re-append the unbuilt
 * tail — the same discipline as the two write-guards
 * (packages/cap1-daemon credentials.ts / write-guard.ts).
 */
function realLocation(absolutePath: string): string {
  const ancestor = nearestExistingAncestor(absolutePath);
  const realAncestor = fs.realpathSync(ancestor);
  const tail = path.relative(ancestor, absolutePath);
  return tail === '' ? realAncestor : path.join(realAncestor, tail);
}

/**
 * Judge the state directory's REAL location against the REAL governed
 * roots. The lexical pass in parseCli is not enough: an
 * operator-supplied symlink (`ln -s <root>/.syzygy/x /tmp/sd;
 * --state-dir /tmp/sd`) resolves lexically outside the governed plane
 * while its real target lies inside it — the credential write would
 * land in the governed plane via the link (RTF-1). Returns the named
 * refusal detail, or null when the real state dir is outside both real
 * governed roots. Read-only: no write, no directory creation.
 */
function governedPlaneViolation(root: string, stateDir: string): string | null {
  const realRoot = realLocation(root);
  const realStateDir = realLocation(stateDir);
  for (const governed of ['openspec', '.syzygy']) {
    const governedRoot = path.join(realRoot, governed);
    if (realStateDir === governedRoot || realStateDir.startsWith(governedRoot + path.sep)) {
      return `state directory ${stateDir} really resolves to ${realStateDir}, inside the governed plane (${governedRoot}); choose a location outside openspec/ and .syzygy/`;
    }
  }
  return null;
}

async function main(): Promise<number> {
  let parsed = parseCli(process.argv.slice(2), process.env);
  if (parsed.kind === 'run') {
    // Symlink reality (RTF-1): the pure lexical check in parseCli
    // cannot see links; judge the real locations here, where fs is
    // available — same named 'invalid' arm, before anything starts.
    const violation = governedPlaneViolation(parsed.config.root, parsed.config.stateDir);
    if (violation !== null) {
      parsed = { kind: 'invalid', detail: violation };
    }
  }
  if (parsed.kind === 'help') {
    process.stdout.write(USAGE);
    return 0;
  }
  if (parsed.kind === 'invalid') {
    process.stderr.write(`syzygy daemon: ${parsed.detail}\n\n${USAGE}`);
    return 1;
  }
  const { root, stateDir, port } = parsed.config;

  // The one clock read: the evaluation's as-of instant. The snapshot
  // coordinate names the observed root at that instant; both are
  // injected — the pipeline itself holds no clock (RFC2-3).
  const asOf = new Date().toISOString();
  const evaluation = { snapshot: `daemon-start-${asOf}`, asOf };

  const projectEvaluation = await evaluateProject(root, { evaluation });

  // Both channels serve from this ONE evaluation — parity by construction
  // (CAP1-REQ-041/043): the human page and the machine endpoint share the
  // same FactModel source, never two computations.
  const getEvaluation = () => projectEvaluation;

  // Entry content is read from the observed root at request time; ENOENT
  // renders the named absent finding, everything else the named unreadable
  // arm (CAP1-REQ-022) — never a fabricated page.
  const readEntrySource = async (entryPath: string): Promise<EntrySourceRead> => {
    const { readFile } = await import('node:fs/promises');
    try {
      const text = await readFile(path.join(root, entryPath), 'utf8');
      return { state: 'present', text };
    } catch (cause: unknown) {
      if ((cause as NodeJS.ErrnoException).code === 'ENOENT') {
        return { state: 'absent' };
      }
      const reason =
        (cause as NodeJS.ErrnoException).code ??
        (cause instanceof Error ? cause.message : String(cause));
      return { state: 'unreadable', reason };
    }
  };

  const start = await createDaemon({
    stateDir,
    port,
    routes: [
      ...humanRoutes({ getEvaluation, readEntrySource }),
      ...machineRoutes({ getEvaluation }),
    ],
  });
  if (!start.started) {
    process.stderr.write(
      `syzygy daemon: failed to start (${start.failure.kind}): ${start.failure.detail}\n`,
    );
    return 1;
  }
  const daemon = start.daemon;

  process.stdout.write(
    [
      `syzygy daemon listening at http://${daemon.host}:${daemon.port}/`,
      `observed root: ${root}`,
      `machine credential (${daemon.credentialProvision}) at: ${daemon.credentialPath}`,
      'the credential value is never printed; read the file to authenticate machine requests.',
      '',
    ].join('\n'),
  );

  await new Promise<void>((resolve) => {
    let closing = false;
    const shutdown = (signal: string): void => {
      if (closing) return;
      closing = true;
      process.stdout.write(`syzygy daemon: ${signal} received, shutting down\n`);
      void daemon.close().then(resolve, (cause: unknown) => {
        process.stderr.write(
          `syzygy daemon: close failed: ${cause instanceof Error ? cause.message : String(cause)}\n`,
        );
        resolve();
      });
    };
    process.on('SIGINT', () => shutdown('SIGINT'));
    process.on('SIGTERM', () => shutdown('SIGTERM'));
  });
  return 0;
}

process.exitCode = await main();
