import { createHash } from 'node:crypto';
import { realpathSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import { createDaemon } from '@syzygy/cap1-daemon';
import {
  buildButlersPocModel,
  evaluateBodyReadAuthority,
  PocObservationError,
  readMaterializationRecordFile,
  readTestArtifactRecordFile,
  type ProjectShapeModelInput,
  type WalkthroughJudgmentInputs,
} from '@syzygy/three-surface-poc-core';

import { parsePocCli } from './cli.js';
import { loadBodyReadAuthorityInputs } from './governance-inputs.js';
import { loadWalkthroughJudgmentInputs } from './walkthrough-inputs.js';
import {
  observeGitRepository,
  pocObserverInputsAreClean,
} from './git-observation.js';
import { materializeRoutes } from './materialize-action.js';
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
      const stateDir = resolve(parsed.config.stateDir ?? defaultStateDir);

      function buildModel(): ReturnType<typeof buildButlersPocModel> {
        let materializationRecord;
        try {
          materializationRecord = readMaterializationRecordFile(stateDir);
        } catch {
          // A corrupt record must not crash startup or silently look
          // unmaterialized — model.ts's own confirmation step already
          // renders Unknown for a record that fails to resolve, so an
          // unreadable record here is simply treated the same way: no
          // positive claim is made without it.
          materializationRecord = null;
        }
        let testArtifactRecord;
        try {
          testArtifactRecord = readTestArtifactRecordFile(stateDir);
        } catch {
          // Same fail-closed posture as the materialization record above:
          // an unreadable ingested artifact must never be treated as
          // "not yet ingested" (which would be silently more permissive).
          testArtifactRecord = null;
        }
        const asOf = new Date().toISOString();
        // PWB-REQ-005: the body-read authority gate is evaluated from the
        // Syzygy governance tree (the daemon's working directory) before the
        // model may read any project-shape body. If the governance inputs
        // cannot even be loaded, no evaluation exists and the project shape
        // stays `not-evaluated` (Unknown) with the failure named — never a
        // synthetic admitting or rejecting evaluation.
        let projectShape: ProjectShapeModelInput | undefined;
        let projectShapeDetail: string | undefined;
        try {
          const authority = evaluateBodyReadAuthority(
            loadBodyReadAuthorityInputs({
              repoRoot: process.cwd(),
              evaluationId: `evaluation:pwb-body-read:${asOf}`,
              evaluationInstant: asOf,
            }),
          );
          projectShape = { authority };
        } catch (error: unknown) {
          projectShapeDetail = `Body-read authority inputs could not be loaded from ${process.cwd()}: ${
            error instanceof Error ? error.message : String(error)
          }`;
        }
        // PWB-REQ-022: the cold-open walkthrough pair is evaluated from the
        // same governance tree. An absent pair evaluates as `absent`
        // (Unknown, never met); only a loader failure leaves the judgment
        // `not-evaluated` with the failure named.
        let walkthroughJudgment: WalkthroughJudgmentInputs | undefined;
        let walkthroughJudgmentDetail: string | undefined;
        try {
          walkthroughJudgment = loadWalkthroughJudgmentInputs({
            repoRoot: process.cwd(),
            evaluationId: `evaluation:pwb-walkthrough-judgment:${asOf}`,
            evaluationInstant: asOf,
          });
        } catch (error: unknown) {
          walkthroughJudgmentDetail = `Walkthrough-judgment inputs could not be loaded from ${process.cwd()}: ${
            error instanceof Error ? error.message : String(error)
          }`;
        }
        return buildButlersPocModel({
          repoRoot,
          repositoryRevision,
          observerRevision,
          evaluation: { snapshot, asOf },
          materializationRecord,
          testArtifactRecord,
          projectShape,
          ...(projectShapeDetail === undefined ? {} : { projectShapeDetail }),
          walkthroughJudgment,
          ...(walkthroughJudgmentDetail === undefined ? {} : { walkthroughJudgmentDetail }),
        });
      }

      try {
        let model = buildModel();
        const start = await createDaemon({
          stateDir,
          port: parsed.config.port,
          routes: [
            ...pocRoutes(() => model),
            ...materializeRoutes({
              getModel: () => model,
              targetRepoRoot: repoRoot,
              stateDir: () => stateDir,
              onMaterialized: () => {
                model = buildModel();
              },
            }),
          ],
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
