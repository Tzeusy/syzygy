// `npm run poc:fresh-checkout-demo -- --repo <butlers>` — task 4.5
// (syzygy-1z3.21): the fresh-checkout demonstration against the configured
// Butlers revision, with the exact test and runtime artifacts retained.
//
// What it does, from committed bytes only:
//   1. `git clone` this checkout into a temporary directory (tags included —
//      the body-read authority gate needs the signing tags);
//   2. `npm ci`, `npm run build`, then the clone's own test run to a JUnit
//      artifact;
//   3. start the clone's own built daemon against the one configured Butlers
//      repository (the daemon evaluates PWB-REQ-005 from the clone's
//      governance tree before any body read — this program reads nothing
//      from Butlers itself);
//   4. fetch every human route and the machine answer (unauthenticated must
//      be refused; authenticated must succeed) and compare Polaris's claim
//      tuples with the machine answer's claim ids, both denominators kept;
//   5. retain every artifact byte-exact, named by SHA-256, in a local
//      retention directory outside the repository (the consent excludes
//      network egress, and this repository is pushed), and write a
//      committed evidence record carrying digests, counts and states only —
//      never act digests, never Butlers text.
//
// The daemon (`main.ts`) never imports this file.
import { execFileSync, spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { homedir, tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import type { PocModel, ProjectShape } from '@syzygy/three-surface-poc-core';

function argument(name: string): string | undefined {
  const index = process.argv.indexOf(name);
  return index === -1 ? undefined : process.argv[index + 1];
}

function sha256(bytes: Uint8Array | string): string {
  return createHash('sha256').update(bytes).digest('hex');
}

function git(cwd: string, args: readonly string[]): string {
  return execFileSync('git', args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
}

interface Timed {
  readonly seconds: number;
  readonly exitCode: number;
}

function run(cwd: string, command: string, args: readonly string[], log: string[]): Timed {
  const started = Date.now();
  let exitCode = 0;
  try {
    execFileSync(command, args, { cwd, stdio: ['ignore', 'pipe', 'pipe'], maxBuffer: 64 * 1024 * 1024 });
  } catch (error: unknown) {
    exitCode = typeof (error as { status?: number }).status === 'number' ? (error as { status: number }).status : 1;
    const stderr = (error as { stderr?: Buffer }).stderr;
    log.push(`${command} ${args.join(' ')} exited ${exitCode}\n${stderr === undefined ? '' : stderr.toString('utf8').slice(-4000)}`);
  }
  return { seconds: Number(((Date.now() - started) / 1000).toFixed(1)), exitCode };
}

/** Root-tag attributes of a JUnit report, read without descending into cases. */
function junitTotals(xml: string): Record<string, string> {
  const root = /<testsuites\b([^>]*)>/.exec(xml) ?? /<testsuite\b([^>]*)>/.exec(xml);
  const out: Record<string, string> = {};
  if (root === null) return out;
  for (const match of (root[1] as string).matchAll(/([a-zA-Z]+)="([^"]*)"/g)) out[match[1] as string] = match[2] as string;
  return out;
}

interface Daemon {
  readonly baseUrl: string;
  readonly credentialPath: string;
  readonly observedRevision: string;
  stop(): Promise<number | null>;
  readonly stderr: () => string;
}

function startDaemon(cloneDir: string, butlersRepo: string, stateDir: string): Promise<Daemon> {
  const child = spawn(process.execPath, [join(cloneDir, 'apps', 'three-surface-poc', 'dist', 'main.js'), '--repo', butlersRepo, '--state-dir', stateDir, '--port', '0'], {
    cwd: cloneDir,
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  let out = '';
  let err = '';
  child.stdout?.setEncoding('utf8');
  child.stderr?.setEncoding('utf8');
  child.stdout?.on('data', (chunk: string) => {
    out += chunk;
  });
  child.stderr?.on('data', (chunk: string) => {
    err += chunk;
  });
  const exited = new Promise<number | null>((resolveExit) => child.once('exit', (code) => resolveExit(code)));
  return new Promise<Daemon>((resolveDaemon, reject) => {
    const deadline = setTimeout(() => {
      child.kill('SIGKILL');
      reject(new Error(`daemon did not announce its address within 120s\nstdout:\n${out}\nstderr:\n${err}`));
    }, 120_000);
    const tryResolve = (): void => {
      const url = /Syzygy Three-Surface POC: (http:\/\/127\.0\.0\.1:\d+)\//.exec(out);
      const credential = /Machine credential \((?:minted|reused)\) at: (.+)/.exec(out);
      const revision = /Observed revision: (\S+)/.exec(out);
      if (url?.[1] === undefined || credential?.[1] === undefined || revision?.[1] === undefined) return;
      clearTimeout(deadline);
      resolveDaemon({
        baseUrl: url[1],
        credentialPath: credential[1].trim(),
        observedRevision: revision[1],
        stderr: () => err,
        stop: async () => {
          if (child.exitCode === null && child.signalCode === null) child.kill('SIGINT');
          return exited;
        },
      });
    };
    child.stdout?.on('data', tryResolve);
    void exited.then((code) => {
      clearTimeout(deadline);
      reject(new Error(`daemon exited (${String(code)}) before announcing its address\nstdout:\n${out}\nstderr:\n${err}`));
    });
  });
}

async function fetchRoute(baseUrl: string, path: string, token?: string): Promise<{ readonly status: number; readonly body: Uint8Array; readonly contentType: string }> {
  const response = await fetch(`${baseUrl}${path}`, { headers: token === undefined ? {} : { authorization: `Bearer ${token}` } });
  return { status: response.status, body: new Uint8Array(await response.arrayBuffer()), contentType: response.headers.get('content-type') ?? '' };
}

/** The claim ids the machine answer carries for the project shape. */
function machineClaimIds(shape: ProjectShape): string[] {
  const ids = [shape.claim.claimId];
  if (shape.kind !== 'observed') return ids;
  for (const source of shape.sources) ids.push(source.claim.claimId);
  for (const item of shape.items) ids.push(item.claim.claimId);
  for (const aggregate of Object.values(shape.classes)) ids.push(aggregate.claim.claimId);
  for (const fact of shape.facts) ids.push(fact.claim.claimId);
  for (const fact of shape.contradictions) ids.push(fact.claim.claimId);
  for (const statement of shape.projectAccount) ids.push(statement.claim.claimId);
  return ids;
}

/** A state-only summary of the project shape: no act digests, no Butlers text. */
function summarizeShape(shape: ProjectShape): Record<string, unknown> {
  const authority = shape.authority === undefined
    ? undefined
    : {
        admits: shape.authority.admits,
        authorizationMode: shape.authority.authorizationMode,
        authorities: shape.authority.authorities.map((entry) => ({ authority: entry.authority, state: entry.state, independentlyVerified: entry.independentlyVerified, invalidCase: entry.invalidCase ?? null })),
        contradiction: shape.authority.contradiction ?? null,
      };
  const claim = { label: shape.claim.epistemic.label, tier: shape.claim.epistemic.tier ?? null, freshness: shape.claim.epistemic.freshness ?? null };
  switch (shape.kind) {
    case 'not-evaluated':
      return { kind: shape.kind, detail: shape.detail, claim };
    case 'not-admitted':
      return { kind: shape.kind, authority, reason: shape.reason, secondaryReasons: shape.secondaryReasons, claim };
    case 'observation-failed':
      return { kind: shape.kind, authority, failure: shape.failure, claim };
    case 'observed':
      return {
        kind: shape.kind,
        authority,
        identity: {
          repositoryId: shape.identity.repositoryId,
          revision: shape.identity.revision,
          sourceClaimedInstant: shape.identity.sourceClaimedInstant,
          observer: shape.identity.observer,
          policy: shape.identity.policy,
          manifestIdentity: shape.identity.manifestIdentity,
          manifestDigest: shape.identity.manifestDigest,
          observationDigest: shape.identity.observationDigest,
        },
        counts: shape.counts,
        classes: Object.fromEntries(Object.entries(shape.classes).map(([name, aggregate]) => [name, { denominator: aggregate.denominator, modeled: aggregate.modeled, unknown: aggregate.unknown, contradicted: aggregate.contradicted, sourcesWithUnknownDenominator: aggregate.sourcesWithUnknownDenominator, label: aggregate.claim.epistemic.label }])),
        sources: shape.sources.map((source) => ({ path: source.path, label: source.claim.epistemic.label, reason: 'reasons' in source.claim.epistemic ? source.claim.epistemic.reasons.primary : null })),
        unknownItemsByReason: countBy(shape.items.filter((item) => item.claim.epistemic.label === 'Unknown').map((item) => ('reasons' in item.claim.epistemic ? item.claim.epistemic.reasons.primary : 'unstated'))),
        exclusions: shape.exclusions.length,
        limitBreaches: shape.limitBreaches.length,
        degradation: shape.degradation ?? null,
        contradictions: shape.contradictions.length,
        claim,
      };
  }
}

function countBy(values: readonly string[]): Record<string, number> {
  const out: Record<string, number> = {};
  for (const value of values) out[value] = (out[value] ?? 0) + 1;
  return out;
}

async function main(): Promise<number> {
  const butlersRepo = argument('--repo');
  if (butlersRepo === undefined) {
    process.stderr.write('usage: npm run poc:fresh-checkout-demo -- --repo <absolute-path-to-butlers> [--retain-dir <dir>] [--date YYYY-MM-DD]\n');
    return 2;
  }
  const date = argument('--date') ?? new Date().toISOString().slice(0, 10);
  const sourceRoot = process.cwd();
  const sourceHead = git(sourceRoot, ['rev-parse', 'HEAD']);
  const retainDir = resolve(argument('--retain-dir') ?? join(process.env['XDG_STATE_HOME'] ?? join(homedir(), '.local', 'state'), 'syzygy', `pwb-p4-5-fresh-checkout-demo-${date}`));
  mkdirSync(retainDir, { recursive: true });
  const base = mkdtempSync(join(tmpdir(), 'syzygy-poc-fresh-'));
  const cloneDir = join(base, 'clone');
  const stateDir = join(base, 'state');
  const log: string[] = [];
  const retained: { readonly name: string; readonly bytes: number; readonly sha256: string }[] = [];
  const retain = (name: string, bytes: Uint8Array | string): string => {
    const data = typeof bytes === 'string' ? new TextEncoder().encode(bytes) : bytes;
    const digest = sha256(data);
    writeFileSync(join(retainDir, name), data);
    retained.push({ name, bytes: data.byteLength, sha256: digest });
    return digest;
  };
  const say = (line: string): void => {
    process.stdout.write(`${line}\n`);
  };

  try {
    // 1. Fresh clone of committed bytes, tags included.
    const cloneTimed = run(sourceRoot, 'git', ['clone', '--quiet', sourceRoot, cloneDir], log);
    if (cloneTimed.exitCode !== 0) throw new Error('git clone failed');
    const cloneHead = git(cloneDir, ['rev-parse', 'HEAD']);
    const signingTags = git(cloneDir, ['tag', '-l', 'pwb-*-signed-*']).split('\n').filter((tag) => tag !== '');
    say(`clone ${cloneHead.slice(0, 12)} (${cloneTimed.seconds}s), ${signingTags.length} signing tags`);

    // 2. Install, build, test in the clone.
    const install = run(cloneDir, 'npm', ['ci', '--no-audit', '--no-fund'], log);
    say(`npm ci exit ${install.exitCode} (${install.seconds}s)`);
    const build = run(cloneDir, 'npm', ['run', 'build'], log);
    say(`npm run build exit ${build.exitCode} (${build.seconds}s)`);
    const junitPath = join(base, 'vitest-junit.xml');
    const test = run(cloneDir, 'npx', ['vitest', 'run', '--reporter=junit', `--outputFile=${junitPath}`], log);
    const junitXml = readFileSync(junitPath, 'utf8');
    const junitDigest = retain('vitest-junit.xml', junitXml);
    const totals = junitTotals(junitXml);
    say(`vitest exit ${test.exitCode} (${test.seconds}s): ${JSON.stringify(totals)}`);

    // 3. The clone's own daemon against the configured Butlers repository.
    const daemon = await startDaemon(cloneDir, butlersRepo, stateDir);
    say(`daemon at ${daemon.baseUrl}, observed Butlers revision ${daemon.observedRevision}`);
    const token = readFileSync(daemon.credentialPath, 'utf8').trim();

    // 4. Routes and the machine answer.
    const routes: Record<string, unknown>[] = [];
    for (const path of ['/', '/polaris', '/trajectory', '/orrery']) {
      const response = await fetchRoute(daemon.baseUrl, path);
      const name = `${path === '/' ? 'home' : path.slice(1)}.html`;
      routes.push({ path, status: response.status, contentType: response.contentType, bytes: response.body.byteLength, sha256: retain(name, response.body), retainedAs: name });
    }
    const refused = await fetchRoute(daemon.baseUrl, '/api/poc');
    routes.push({ path: '/api/poc', authenticated: false, status: refused.status, bytes: refused.body.byteLength });
    const machine = await fetchRoute(daemon.baseUrl, '/api/poc', token);
    routes.push({ path: '/api/poc', authenticated: true, status: machine.status, contentType: machine.contentType, bytes: machine.body.byteLength, sha256: retain('api-poc.json', machine.body), retainedAs: 'api-poc.json' });
    const model = JSON.parse(new TextDecoder().decode(machine.body)) as PocModel;

    // Parity: Polaris claim tuples versus the machine answer's claim ids.
    const polarisHtml = new TextDecoder().decode((await fetchRoute(daemon.baseUrl, '/polaris')).body);
    const humanIds = Array.from(polarisHtml.matchAll(/data-claim-id="([^"]*)"/g), (match) => (match[1] as string).replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&'));
    const machineIds = machineClaimIds(model.projectShape);
    const humanSet = new Set(humanIds);
    const machineSet = new Set(machineIds);
    const parity = {
      humanClaimTuples: humanIds.length,
      humanDistinctClaimIds: humanSet.size,
      machineClaimIds: machineIds.length,
      machineDistinctClaimIds: machineSet.size,
      machineIdsAbsentFromHuman: [...machineSet].filter((id) => !humanSet.has(id)).length,
      humanIdsAbsentFromMachine: [...humanSet].filter((id) => !machineSet.has(id)).length,
    };
    say(`parity: ${parity.humanDistinctClaimIds} human vs ${parity.machineDistinctClaimIds} machine claim ids; absent ${parity.machineIdsAbsentFromHuman}/${parity.humanIdsAbsentFromMachine}`);

    const daemonExit = await daemon.stop();
    say(`daemon stopped (${String(daemonExit)}); project shape ${model.projectShape.kind}`);

    const evidence = {
      task: 'syzygy-1z3.21 (PWB task 4.5)',
      kind: 'fresh-checkout demonstration against the configured Butlers revision',
      capturedAt: new Date().toISOString(),
      node: process.version,
      source: { root: sourceRoot, head: sourceHead },
      clone: { head: cloneHead, headMatchesSource: cloneHead === sourceHead, signingTags, seconds: cloneTimed.seconds },
      install: { ...install },
      build: { ...build },
      test: { ...test, junit: totals, junitSha256: junitDigest },
      butlers: { configuredRepository: butlersRepo, observedRevision: daemon.observedRevision, modelRevision: model.project.revision, observerRevision: model.observerRevision },
      evaluation: { snapshot: model.evaluation.snapshot, asOf: model.evaluation.asOf, inputsDigest: model.evaluation.inputsDigest },
      daemon: { exitCode: daemonExit, stderr: daemon.stderr().slice(-2000) },
      routes,
      parity,
      projectShape: summarizeShape(model.projectShape),
      otherRegions: {
        codeStructure: model.codeStructure.kind,
        workItems: model.workItems.kind,
        workerChange: model.workerChange.kind,
        testArtifactVerification: model.testArtifactVerification.kind,
        proposedWork: (model as unknown as { proposedWork?: { kind?: string } }).proposedWork?.kind ?? null,
        walkthroughJudgment: (model as unknown as { walkthroughJudgment?: { kind?: string } }).walkthroughJudgment?.kind ?? null,
      },
      retention: { directory: retainDir, note: 'exact artifact bytes retained locally, outside the repository; the consent excludes network egress', files: retained },
      log,
    };
    mkdirSync(join(sourceRoot, 'docs', 'evidence'), { recursive: true });
    const evidencePath = join(sourceRoot, 'docs', 'evidence', `pwb-p4-5-fresh-checkout-demo-${date}.json`);
    writeFileSync(evidencePath, `${JSON.stringify(evidence, null, 2)}\n`);
    say(`wrote ${evidencePath}; artifacts retained in ${retainDir}`);
    const healthy = install.exitCode === 0 && build.exitCode === 0 && test.exitCode === 0 && refused.status === 401 && machine.status === 200 && routes.slice(0, 4).every((route) => route['status'] === 200);
    return healthy ? 0 : 1;
  } finally {
    rmSync(base, { recursive: true, force: true });
  }
}

main().then(
  (code) => process.exit(code),
  (error: unknown) => {
    process.stderr.write(`${error instanceof Error ? error.stack ?? error.message : String(error)}\n`);
    process.exit(1);
  },
);
