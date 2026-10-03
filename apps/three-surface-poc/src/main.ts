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
  observeObservatoryDrift,
  observeRevisionChange,
  pocObserverInputsAreClean,
  resolvePwbRepositoryBinding,
} from './git-observation.js';
import { launchAfterPwbRepositoryBinding } from './launcher.js';
import { materializeRoutes } from './materialize-action.js';
import { buildPocEvaluationEvidence, buildProductionPocModel, type PocRuntimeCapture } from './production-reobserve.js';
import { reobserveRoutes } from './reobserve-action.js';
import { createReobserveSession } from './reobserve-session.js';
import { pocRoutes } from './routes.js';
import { ServedResponseRecorder } from './served-response-recorder.js';
import { daemonStartDetail, gitObservationDetail, unexpectedObservationDetail } from './startup-detail.js';
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
  --watch             re-observe each time Enter is pressed on this console, and only then
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
          process.stderr.write(`syzygy POC: ${gitObservationDetail(cause)}\n`);
          process.exitCode = 1;
          repositoryRevision = '';
          observerRevision = '';
          workingTreeDigest = '';
          repositoryCommitterInstant = '';
        }

        if (repositoryRevision !== '' && observerRevision !== '') {
          const horizon = observeGitHorizon(repoRoot, repositoryRevision);
          const capture: PocRuntimeCapture = {
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

          const buildModel = (currentCapture: PocRuntimeCapture): PocModel => buildProductionPocModel({
            capture: currentCapture,
            repoRoot,
            stateDir,
            observerRoot: process.cwd(),
          });

          try {
            const servedResponses = new ServedResponseRecorder();
            let credentialProvision: 'minted' | 'reused' | undefined;
            // syzygy-u05.2: every evaluation is a named re-evaluation result
            // carrying the identity it supersedes, the three clocks and the
            // two staleness limbs. The observatory limb counts Syzygy commits
            // since the revision this daemon was started from.
            const buildRevision = observerRevision;
            const session = createReobserveSession({
              capture,
              build: buildModel,
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
              observeHorizon: (pinned) => observeGitHorizon(repoRoot, pinned),
              observeRevisionChange: (from, to) => observeRevisionChange(repoRoot, from, to),
              observeObservatory: () => observeObservatoryDrift(process.cwd(), buildRevision),
              now: () => new Date().toISOString(),
            });
            const start = await createDaemon({
              stateDir,
              port: parsed.config.port,
              routes: [
                // PWB-REQ-011 (amended): Polaris's transient exact-requirement
                // route — the observed shape's own admitted baseline-spec object,
                // read at render and never stored.
                ...pocRoutes(session.model, undefined, (current) => ({ verbatim: verbatimRouteReader(current, gitBlobReaderFor(repoRoot)) }), servedResponses, () => credentialProvision, session.latest),
                ...materializeRoutes({
                  getModel: session.model,
                  targetRepoRoot: repoRoot,
                  stateDir: () => stateDir,
                  onMaterialized: session.afterMaterialized,
                }),
                ...reobserveRoutes({ reobserve: session.reobserve }),
              ],
            });
            if (!start.started) {
              process.stderr.write(`syzygy POC: daemon did not start (${start.failure.kind}: ${daemonStartDetail(start.failure)})\n`);
              process.exitCode = 1;
            } else {
              const daemon = start.daemon;
              credentialProvision = daemon.credentialProvision;
              process.stdout.write(
                [
                  `Syzygy Three-Surface POC: http://${daemon.host}:${daemon.port}/`,
                  `Observed repository: ${repoRoot}`,
                  `Observed revision: ${repositoryRevision}`,
                  ...walkthroughBindingLines(session.model()),
                  `Machine endpoint: http://${daemon.host}:${daemon.port}/api/poc`,
                  `Machine credential (${daemon.credentialProvision}) at: ${daemon.credentialPath}`,
                  'Credential value is never printed. POC is local, experimental, and non-release.',
                  '',
                ].join('\n'),
              );
              void session.startConsole(parsed.config.watch, { input: process.stdin, output: process.stdout });

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
              process.stderr.write(`syzygy POC: observation failed (${unexpectedObservationDetail(cause)})\n`);
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
