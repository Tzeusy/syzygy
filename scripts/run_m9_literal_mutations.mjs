// Rule-6 source-mutation proof for M9 slices 1-2. Run from a committed tree;
// each exact fragment is restored byte-for-byte before the next case.
import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const app = 'apps/three-surface-poc/src/';
const core = 'packages/three-surface-poc-core/src/';
const routes = `${app}surface-routes.test.ts`;
const links = `${app}surface-links.ts`;
const crossCutting = `${app}cross-cutting.test.ts`;
const modelTest = `${core}model.test.ts`;
const mutations = [
  {
    id: 'cross-fragment-dangles', file: links, tests: [routes, `${app}polaris-reachability.test.ts`],
    old: 'return `polaris-deep-dive-${sourceSlug(capabilityId)}`;',
    new: "return 'polaris-deep-dive-missing-target';",
    mustFail: ['exhausts 13 runtime cross-surface links over five classes and fetches every direct target'],
    mustPass: ['resolves every internal link to exactly one id in every shape state'],
  },
  {
    id: 'mounted-prefix-omitted', file: links, tests: [routes],
    old: 'withMountPrefix(mountPrefix, ROUTES[target])', new: 'ROUTES[target]',
    mustFail: ['exhausts 13 runtime cross-surface links over five classes and fetches every tailnet target'],
    mustPass: ['exhausts 13 runtime cross-surface links over five classes and fetches every direct target'],
  },
  {
    id: 'work-count-member-deleted', file: `${app}polaris.ts`, tests: [routes],
    old: "crossSurfaceLink({ model, className: 'work-count', sourceId: 'region:work-items', target: 'trajectory', targetId: null, mountPrefix: activeMountPrefix, label: `${wi.items.length} work items` })",
    new: 'escapeHtml(`${wi.items.length} work items`)',
    mustFail: ['exhausts 13 runtime cross-surface links over five classes and fetches every direct target'],
  },
  {
    id: 'orrery-runtime-member-deleted', file: `${app}orrery.ts`, tests: [routes],
    old: 'block.appendChild(capabilityLink);', new: 'if (false) block.appendChild(capabilityLink);',
    mustFail: ['exhausts 13 runtime cross-surface links over five classes and fetches every direct target'],
  },
  {
    id: 'seed-state-validation-disabled', file: `${core}model.ts`, tests: [modelTest],
    old: 'if (surface.state !== SURFACE_STATES[surface.id]) {', new: 'if (false) {',
    mustFail: ['rejects invalid public seed graphs before observation with typed failures'],
  },
  {
    id: 'trajectory-state-projection-swapped', file: `${core}model.ts`, tests: [crossCutting],
    old: ': {\n                  id: surface.id,\n                  state: surface.state,\n                  title: surface.title,',
    new: ": {\n                  id: surface.id,\n                  state: surface.id === 'trajectory' ? 'observed' : surface.state,\n                  title: surface.title,",
    mustFail: ['names each page plane once outside the legend and each home panel once'],
  },
  {
    id: 'legend-plane-spelling-changed', file: `${app}page-shell.ts`, tests: [crossCutting],
    old: 'holds the ${escapeHtml(surface.state)} state', new: 'holds a ${escapeHtml(surface.state)} state',
    mustFail: ['names each page plane once outside the legend and each home panel once'],
  },
];

const digest = bytes => createHash('sha256').update(bytes).digest('hex');
const git = args => execFileSync('git', args, { cwd: root, encoding: 'utf8' }).trim();
const targets = [...new Set(mutations.flatMap(m => [m.file, ...m.tests]))];
if (git(['status', '--porcelain', '--', ...targets])) throw new Error('mutation subjects or tests are dirty');
const commit = git(['rev-parse', 'HEAD']);
const originals = new Map([...new Set(mutations.map(m => m.file))].map(file => [file, readFileSync(join(root, file))]));
const scratch = mkdtempSync(join(tmpdir(), 'syzygy-m9-mutation-'));

function run(tests, label) {
  const reportPath = join(scratch, `${label}.json`);
  const args = ['vitest', 'run', ...tests, '--reporter=json', `--outputFile=${reportPath}`];
  const process = spawnSync('npx', args, { cwd: root, env: { ...globalThis.process.env, CI: '1' }, encoding: 'utf8' });
  if (process.error) throw process.error;
  let report;
  try { report = JSON.parse(readFileSync(reportPath, 'utf8')); }
  catch { throw new Error(`missing test report for ${label}: exit=${process.status}; ${process.stderr}`); }
  const assertions = report.testResults.flatMap(file => file.assertionResults)
    .map(test => ({ name: test.fullName, status: test.status }));
  return { command: `npx ${args.join(' ')}`, exit: process.status, total: report.numTotalTests,
    passed: report.numPassedTests, failed: report.numFailedTests,
    failing: assertions.filter(test => test.status === 'failed').map(test => test.name),
    passing: assertions.filter(test => test.status === 'passed').map(test => test.name) };
}

const records = [];
try {
  for (const [index, mutation] of mutations.entries()) {
    const before = originals.get(mutation.file);
    const source = before.toString('utf8');
    if (source.split(mutation.old).length !== 2) throw new Error(`${mutation.id}: old fragment must occur exactly once`);
    const baseline = run(mutation.tests, `baseline-${index}`);
    if (baseline.exit !== 0 || baseline.total === 0 || baseline.failed !== 0) throw new Error(`${mutation.id}: baseline not green`);
    let mutant;
    try {
      writeFileSync(join(root, mutation.file), source.replace(mutation.old, mutation.new));
      mutant = run(mutation.tests, `mutant-${index}`);
    } finally { writeFileSync(join(root, mutation.file), before); }
    const after = readFileSync(join(root, mutation.file));
    const restored = before.equals(after);
    const expectedFailures = mutation.mustFail.every(name => mutant.failing.some(actual => actual.includes(name)));
    const preservedControls = (mutation.mustPass ?? []).every(name => mutant.passing.some(actual => actual.includes(name)));
    const killed = mutant.total > 0 && mutant.failed > 0 && expectedFailures && preservedControls;
    records.push({ ...mutation, baseline, mutant, sourceSha256Before: digest(before), sourceSha256After: digest(after), restored, killed });
    globalThis.process.stdout.write(`${killed && restored ? 'KILLED' : 'SURVIVED'} ${mutation.id}: ${mutant.failed}/${mutant.total} failed, restored=${restored}\n`);
  }
} finally {
  for (const [file, bytes] of originals) writeFileSync(join(root, file), bytes);
  rmSync(scratch, { recursive: true, force: true });
}
const evidence = { kind: 'm9-literal-source-mutations', capturedAt: new Date().toISOString(), testedCommit: commit,
  baselineAndMutantRunSeparately: true, records, summary: { planned: mutations.length,
    killedAndRestored: records.filter(record => record.killed && record.restored).length } };
const evidencePath = join(root, 'docs/evidence/polaris-m9-literal-mutations-2026-09-23.json');
writeFileSync(evidencePath, `${JSON.stringify(evidence, null, 2)}\n`);
globalThis.process.stdout.write(`evidence: ${evidencePath}\n`);
if (evidence.summary.killedAndRestored !== mutations.length) globalThis.process.exitCode = 1;
