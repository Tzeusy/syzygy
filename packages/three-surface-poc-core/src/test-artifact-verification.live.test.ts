import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

import { buildPocModel } from './model.js';
import { BUTLERS_POC_SEEDS } from './poc-seeds.js';
import { buildTestArtifactRecordFromJUnit, parseJUnitRootTotals } from './test-artifact-verification.js';

// Gated exactly like the existing SYZYGY_POC_BUTLERS_REPO-gated live
// checks (work-items.live.test.ts): the default suite stays hermetic, but
// this proves the real end-to-end path on demand — a real JUnit artifact
// from the real, configured Butlers checkout, and a real "verified" render
// through the full shared model (syzygy-0r9 AC1: a real focused Butlers
// test artifact captured outside Syzygy, ingested, and only then shown
// verified).
//
// Syzygy never runs the observed test suite, here or anywhere (SEC-3,
// RFC5-18; syzygy-hjuz, under the owner's syzygy-4mbu direction "print the
// command"). The operator runs the focused pytest command in their own
// shell and hands the result back through the environment:
//   SYZYGY_POC_BUTLERS_JUNIT         the JUnit file the run wrote
//   SYZYGY_POC_BUTLERS_JUNIT_COMMIT  the commit it ran at (git rev-parse HEAD)
//   SYZYGY_POC_BUTLERS_JUNIT_EXIT    its exit status
//   SYZYGY_POC_BUTLERS_PYTHON        the interpreter it used (default python3)
// With the repository set and the result missing, the test fails and names
// the command to run, rather than skipping or running it.
const BUTLERS_REPO = process.env.SYZYGY_POC_BUTLERS_REPO;
const PYTHON = process.env.SYZYGY_POC_BUTLERS_PYTHON ?? 'python3';
const JUNIT = process.env.SYZYGY_POC_BUTLERS_JUNIT;
const JUNIT_COMMIT = process.env.SYZYGY_POC_BUTLERS_JUNIT_COMMIT;
const JUNIT_EXIT = process.env.SYZYGY_POC_BUTLERS_JUNIT_EXIT;
const describeLive = BUTLERS_REPO === undefined ? describe.skip : describe;

const SCOPE = 'tests/connectors/test_whatsapp_user_client.py';

describeLive('live real focused-pytest verification (SYZYGY_POC_BUTLERS_REPO gated)', () => {
  const repoRoot = BUTLERS_REPO as string;

  it('ingests one real, passing operator-run focused-pytest artifact and renders Verified through the full model (AC1/AC3)', () => {
    if (JUNIT === undefined || JUNIT_COMMIT === undefined || JUNIT_EXIT === undefined) {
      throw new Error(
        'Syzygy does not run the Butlers test suite. In your own shell, run\n' +
          `  git -C ${repoRoot} rev-parse HEAD\n` +
          `  cd ${repoRoot} && ${PYTHON} -m pytest ${SCOPE} -q --junitxml=<file>; echo "exit $?"\n` +
          'then set SYZYGY_POC_BUTLERS_JUNIT=<file>, SYZYGY_POC_BUTLERS_JUNIT_COMMIT=<commit> and ' +
          'SYZYGY_POC_BUTLERS_JUNIT_EXIT=<status>, and run this test again.',
      );
    }
    expect(JUNIT_EXIT).toBe('0');

    const repositoryCommit = execFileSync('git', ['-C', repoRoot, 'rev-parse', 'HEAD'], {
      encoding: 'utf8',
    }).trim();
    // A run at one commit is never ingested against another.
    expect(repositoryCommit).toBe(JUNIT_COMMIT);

    const rawJUnitXml = readFileSync(JUNIT, 'utf8');
    const totals = parseJUnitRootTotals(rawJUnitXml);
    expect(totals).not.toBeNull();
    expect({ failures: totals?.failures, errors: totals?.errors }).toEqual({ failures: 0, errors: 0 });
    {
      const built = buildTestArtifactRecordFromJUnit({
        rawJUnitXml,
        command: [PYTHON, '-m', 'pytest', SCOPE, '-q'],
        exitCode: Number(JUNIT_EXIT),
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
      const model = buildPocModel({
        seeds: BUTLERS_POC_SEEDS,
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
    }
  }, 120_000);
});
