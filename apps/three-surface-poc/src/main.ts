import { createHash } from 'node:crypto';
import { realpathSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import { createDaemon } from '@syzygy/cap1-daemon';
import {
  PocObservationError,
  type PocModel,
} from '@syzygy/three-surface-poc-core';

import { parsePocCli } from './cli.js';
import {
  observeGitHorizon,
  observeGitRepository,
  pocObserverInputsAreClean,
  resolvePwbRepositoryBinding,
} from './git-observation.js';
import { launchAfterPwbRepositoryBinding } from './launcher.js';
import { materializeRoutes } from './materialize-action.js';
import { buildPocEvaluationEvidence, buildProductionPocModel, type PocRuntimeCapture } from './production-reobserve.js';
import { reobserveRoutes } from './reobserve-action.js';
import { createReobserveState } from './reobserve-state.js';
import { pocRoutes } from './routes.js';
import { gitBlobReaderFor, verbatimRouteReader } from './verbatim-route.js';

/** The exact binding a PWB-WALKTHROUGH-001 record must name for this
 * evaluation, printed so the recording session copies it rather than
 * invents it; absent lines mean readiness could not be evaluated. */
function walkthroughBindingLines(model: PocModel): readonly string[] {
  const readiness = model.walkthroughReadiness;
  if (readiness.kind !== 'evaluated') return [];
  const { expected } = readiness.readiness;
  return [
    `Walkthrough surface version: ${expected.surfaceVersion}`,
    `Walkthrough evaluation identity: ${expected.evaluationIdentity}`,
  ];
}

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
    const launch = await launchAfterPwbRepositoryBinding(
      repoRoot,
      resolvePwbRepositoryBinding,
      async (boundRepoRoot) => {
        repoRoot = boundRepoRoot;
        let repositoryRevision: string;
        let observerRevision: string;
        let workingTreeDigest: string;
        let repositoryCommitterInstant: string;
        try {
          const repository = observeGitRepository(repoRoot);
          const observer = observeGitRepository(process.cwd());
          if (!pocObserverInputsAreClean(observer)) {
            throw new Error('observer-checkout-dirty');
          }
          repositoryRevision = repository.revision;
          repositoryCommitterInstant = repository.committerInstant;
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
          repositoryCommitterInstant = '';
        }

        if (repositoryRevision !== '' && observerRevision !== '') {
          const horizon = observeGitHorizon(repoRoot, repositoryRevision);
          let capture: PocRuntimeCapture = {
            repositoryRevision,
            observerRevision,
            workingTreeDigest,
            evidence: buildPocEvaluationEvidence(new Date().toISOString(), repositoryRevision, repositoryCommitterInstant, horizon),
          };
          const defaultStateDir = join(
            tmpdir(),
            'syzygy-three-surface-poc',
            createHash('sha256').update(repoRoot).digest('hex').slice(0, 16),
          );
          const stateDir = resolve(parsed.config.stateDir ?? defaultStateDir);

          const buildModel = (currentCapture = capture): PocModel => buildProductionPocModel({
            capture: currentCapture,
            repoRoot,
            stateDir,
            observerRoot: process.cwd(),
          });

          try {
            let model = buildModel(capture);
            const reobserver = createReobserveState({
              capture,
              model,
              observe: async () => {
                const nextRepository = observeGitRepository(repoRoot);
                const nextObserver = observeGitRepository(process.cwd());
                if (!pocObserverInputsAreClean(nextObserver)) throw new Error('POC runtime inputs are dirty; re-observation was refused');
                const nextHorizon = observeGitHorizon(repoRoot, nextRepository.revision);
                const asOf = new Date().toISOString();
                return {
                  repositoryRevision: nextRepository.revision,
                  observerRevision: nextObserver.revision,
                  workingTreeDigest: nextRepository.worktreeMetadataDigest,
                  evidence: buildPocEvaluationEvidence(asOf, nextRepository.revision, nextRepository.committerInstant, nextHorizon),
                };
              },
              build: buildModel,
            });
            const start = await createDaemon({
              stateDir,
              port: parsed.config.port,
              routes: [
                // PWB-REQ-011 (amended): Polaris's transient exact-requirement
                // route — the observed shape's own admitted baseline-spec object,
                // read at render and never stored.
                ...pocRoutes(() => model, undefined, (current) => ({ verbatim: verbatimRouteReader(current, gitBlobReaderFor(repoRoot)) })),
                ...materializeRoutes({
                  getModel: () => model,
                  targetRepoRoot: repoRoot,
                  stateDir: () => stateDir,
                  onMaterialized: () => {
                    model = buildModel(capture);
                    reobserver.replace(capture, model);
                  },
                }),
                ...reobserveRoutes({
                  reobserve: async () => {
                    const result = await reobserver.reobserve();
                    if (result.kind === 'failed') return result;
                    model = result.model;
                    capture = reobserver.getCapture();
                    return { kind: 'reobserved', evaluation: result.model.evaluation.snapshot };
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
                  ...walkthroughBindingLines(model),
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
              const suffix = [cause.artifactPath, cause.detail]
                .filter((part): part is string => part !== undefined)
                .map((part) => `: ${part}`)
                .join('');
              process.stderr.write(`syzygy POC: observation failed (${cause.kind})${suffix}\n`);
            } else {
              process.stderr.write('syzygy POC: observation failed (unexpected-failure)\n');
            }
            process.exitCode = 1;
          }
        }
      },
    );
    if (launch.kind === 'rejected') {
      process.stderr.write(`syzygy POC: configured repository authority rejected (${launch.reason})\n`);
      process.exitCode = 1;
    }
  }
}
