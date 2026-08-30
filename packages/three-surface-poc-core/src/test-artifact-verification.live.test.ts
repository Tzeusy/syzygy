import { execFileSync, spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';

import { buildButlersPocModel } from './model.js';
import { buildTestArtifactRecordFromJUnit } from './test-artifact-verification.js';

// Gated exactly like the existing SYZYGY_POC_BUTLERS_REPO-gated live
// checks (work-items.live.test.ts): the default suite stays hermetic, but
// this proves the real end-to-end path — an actual `pytest` invocation
// against the real, configured Butlers checkout, a real JUnit artifact,
// and a real "verified" render through the full shared model — on demand
// (syzygy-0r9 AC1: a real focused Butlers test artifact captured outside
// Syzygy, ingested, and only then shown verified).
const BUTLERS_REPO = process.env.SYZYGY_POC_BUTLERS_REPO;
const PYTHON = process.env.SYZYGY_POC_BUTLERS_PYTHON ?? 'python3';
const describeLive = BUTLERS_REPO === undefined ? describe.skip : describe;

const SCOPE = 'tests/connectors/test_whatsapp_user_client.py';

describeLive('live real focused-pytest verification (SYZYGY_POC_BUTLERS_REPO gated)', () => {
  const repoRoot = BUTLERS_REPO as string;

  it('captures one real, passing focused-pytest artifact and renders Verified through the full model (AC1/AC3)', () => {
    const junitDir = mkdtempSync(join(tmpdir(), 'syzygy-poc-live-capture-'));
    try {
      const junitPath = join(junitDir, 'artifact.xml');
      const proc = spawnSync(PYTHON, ['-m', 'pytest', SCOPE, '-q', `--junitxml=${junitPath}`], {
        cwd: repoRoot,
        encoding: 'utf8',
      });
      expect(proc.error).toBeUndefined();
      expect(proc.status).toBe(0);

      const rawJUnitXml = readFileSync(junitPath, 'utf8');
      const repositoryCommit = execFileSync('git', ['-C', repoRoot, 'rev-parse', 'HEAD'], {
        encoding: 'utf8',
      }).trim();
      const built = buildTestArtifactRecordFromJUnit({
        rawJUnitXml,
        command: [PYTHON, '-m', 'pytest', SCOPE, '-q'],
        exitCode: proc.status ?? 1,
        capturedAt: new Date().toISOString(),
        repositoryCommit,
        scope: SCOPE,
      });
      expect(built.kind).toBe('built');
      if (built.kind !== 'built') throw new Error('unreachable');
      expect(built.record.summary).toMatch(/passed/);
      expect(built.record.summary).not.toContain('Traceback');

      // Compose through the full shared model, with the git-based
      // worker-change observer's `runGit` seam pointed at this same real
      // commit — the observer's own commit-discovery logic is covered by
      // worker-change-observation.test.ts; this proves the *composition*
      // with a genuinely captured artifact end-to-end.
      const model = buildButlersPocModel({
        repoRoot,
        repositoryRevision: repositoryCommit,
        observerRevision: repositoryCommit,
        evaluation: {
          snapshot: 'butlers@live-capture',
          asOf: new Date(Date.now() + 60 * 60 * 1000).toISOString(),
        },
        materializationRecord: {
          beadId: 'bu-live-capture-1',
          externalRef: 'syzygy-poc:live-capture-test',
          targetRepoRoot: repoRoot,
          createdAt: new Date().toISOString(),
          doltRevisionAtCreation: null,
          attribution: 'live-test',
        },
        runWorkItemQuery: () =>
          JSON.stringify([
            {
              revision: 'dolt-live',
              id: 'bu-live-capture-1',
              title: 'live capture',
              status: 'in_progress',
              issue_type: 'task',
              priority: 1,
              created_at: new Date().toISOString(),
              updated_at: new Date().toISOString(),
              closed_at: null,
            },
          ]),
        runGit: (root, args) => {
          if (args[0] === 'symbolic-ref') return 'refs/remotes/origin/main';
          if (args[0] === 'rev-parse') return repositoryCommit;
          if (args[0] === 'log') {
            const format = `${repositoryCommit}\x1f${built.record.capturedAt}\x1flive capture [bu-live-capture-1]`;
            return `${format}\n`;
          }
          if (args[0] === 'merge-base') return '';
          if (args[0] === 'for-each-ref') return 'main\n';
          return execFileSync('git', ['--no-optional-locks', '-C', root, ...args], { encoding: 'utf8' });
        },
        testArtifactRecord: built.record,
      });

      expect(model.workerChange.kind).toBe('observed');
      if (model.workerChange.kind !== 'observed') throw new Error('unreachable');
      expect(model.workerChange.state).toBe('changed-or-merged');
      expect(model.testArtifactVerification.kind).toBe('verified');
    } finally {
      rmSync(junitDir, { recursive: true, force: true });
    }
  }, 120_000);
});
