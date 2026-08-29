import { createHash } from 'node:crypto';
import { realpathSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import { createDaemon } from '@syzygy/cap1-daemon';
import {
  buildButlersPocModel,
  PocObservationError,
} from '@syzygy/three-surface-poc-core';

import { parsePocCli } from './cli.js';
import {
  observeGitRepository,
  pocObserverInputsAreClean,
} from './git-observation.js';
import { pocRoutes } from './routes.js';

const USAGE = `syzygy three-surface POC (local, non-release)

Usage: npm run poc -- --repo <absolute-path-to-butlers> [options]

Options:
  --repo <path>       one explicit Butlers repository (required)
  --state-dir <path>  credential/state directory (default: OS temp directory)
  --port <n>          loopback TCP port; 0 selects an ephemeral port (default: 7478)
  --help              print this usage and exit
`;

const parsed = parsePocCli(process.argv.slice(2));
if (parsed.kind === 'help') {
  process.stdout.write(USAGE);
} else if (parsed.kind === 'invalid') {
  process.stderr.write(`syzygy POC: ${parsed.detail}\n\n${USAGE}`);
  process.exitCode = 1;
} else {
  let repoRoot: string;
  try {
    repoRoot = realpathSync(resolve(parsed.config.repoRoot));
  } catch {
    process.stderr.write('syzygy POC: configured repository is not readable\n');
    process.exitCode = 1;
    repoRoot = '';
  }

  if (repoRoot !== '') {
    let repositoryRevision: string;
    let observerRevision: string;
    let workingTreeDigest: string;
    try {
      const repository = observeGitRepository(repoRoot);
      const observer = observeGitRepository(process.cwd());
      if (!pocObserverInputsAreClean(observer)) {
        throw new Error('observer-checkout-dirty');
      }
      repositoryRevision = repository.revision;
      observerRevision = observer.revision;
      workingTreeDigest = repository.worktreeMetadataDigest;
    } catch (cause) {
      process.stderr.write(
        cause instanceof Error && cause.message === 'observer-checkout-dirty'
          ? 'syzygy POC: POC runtime inputs have uncommitted changes\n'
          : 'syzygy POC: a required git revision could not be observed\n',
      );
      process.exitCode = 1;
      repositoryRevision = '';
      observerRevision = '';
      workingTreeDigest = '';
    }

    if (repositoryRevision !== '' && observerRevision !== '') {
      const asOf = new Date().toISOString();
      const snapshot = [
        `butlers:${repositoryRevision}`,
        `working-tree:${workingTreeDigest}`,
        `observer:${observerRevision}`,
      ].join('|');
      const defaultStateDir = join(
        tmpdir(),
        'syzygy-three-surface-poc',
        createHash('sha256').update(repoRoot).digest('hex').slice(0, 16),
      );

      try {
        const model = buildButlersPocModel({
          repoRoot,
          repositoryRevision,
          observerRevision,
          evaluation: { snapshot, asOf },
        });
        const start = await createDaemon({
          stateDir: resolve(parsed.config.stateDir ?? defaultStateDir),
          port: parsed.config.port,
          routes: pocRoutes(() => model),
        });
        if (!start.started) {
          process.stderr.write(`syzygy POC: daemon did not start (${start.failure.kind})\n`);
          process.exitCode = 1;
        } else {
          const daemon = start.daemon;
          process.stdout.write(
            [
              `Syzygy Three-Surface POC: http://${daemon.host}:${daemon.port}/`,
              `Observed repository: ${repoRoot}`,
              `Observed revision: ${repositoryRevision}`,
              `Machine endpoint: http://${daemon.host}:${daemon.port}/api/poc`,
              `Machine credential (${daemon.credentialProvision}) at: ${daemon.credentialPath}`,
              'Credential value is never printed. POC is local, experimental, and non-release.',
              '',
            ].join('\n'),
          );

          await new Promise<void>((resolveShutdown) => {
            let closing = false;
            const shutdown = (signal: string): void => {
              if (closing) return;
              closing = true;
              process.stdout.write(`syzygy POC: ${signal} received, shutting down\n`);
              void daemon.close().then(resolveShutdown, () => resolveShutdown());
            };
            process.on('SIGINT', () => shutdown('SIGINT'));
            process.on('SIGTERM', () => shutdown('SIGTERM'));
          });
        }
      } catch (cause) {
        if (cause instanceof PocObservationError) {
          const suffix = cause.artifactPath === undefined ? '' : `: ${cause.artifactPath}`;
          process.stderr.write(`syzygy POC: observation failed (${cause.kind})${suffix}\n`);
        } else {
          process.stderr.write('syzygy POC: observation failed (unexpected-failure)\n');
        }
        process.exitCode = 1;
      }
    }
  }
}
