// Executable rule-6 proof for the M7 seams. Run only from a committed, clean
// worktree: this script temporarily rewrites its named source files.
import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const app = 'apps/three-surface-poc/src/polaris-generation/';
const core = 'packages/polaris-generation-core/src/';
const mutations = [
  {
    id: 'citation-back-to-list-index', file: `${app}draft-preview.ts`, test: `${app}draft-preview.test.ts`,
    mustFail: 'binds citation hrefs to source anchors, independent of list position',
    old: 'const href = routeForAnchor?.(source, anchorId) ?? `#${localAnchor(anchorId)}`;',
    new: 'const href = routeForAnchor?.(source, anchorId) ?? `#source-${sources.indexOf(source)}`;',
  },
  {
    id: 'uncertain-and-in-flight-replay', file: `${app}durable-lifecycle.ts`, test: `${app}durable-lifecycle.test.ts`,
    mustFail: 'keeps uncertain maximum reserved despite missing receipts and an expired lease field',
    old: "return { kind: 'refused', reason: prior.state === 'reserved' ? 'in-flight' : 'uncertain' };",
    new: "return { kind: 'reserved', permit: prior.permit };",
  },
  {
    id: 'source-object-binding-disabled', file: `${core}generation-source.ts`, test: `${core}generation-source.test.ts`,
    mustFail: 'rejects forged object binding, offset drift, duplicate anchors and unknown-byte spans',
    old: "if (gitBlobObjectId(body, objectId.length === 40 ? 'sha1' : 'sha256') !== objectId) fail('object-mismatch');",
    new: "if (false) fail('object-mismatch');",
  },
  {
    id: 'fidelity-receives-author-plan', file: `${core}pipeline.ts`, test: `${core}pipeline.test.ts`,
    mustFail: 'keeps the author plan out of the canonically encoded fidelity and repair envelopes',
    old: "let review = await stage('fidelity', { sources: citedSpans(context.draft), readerQuestions: context.readerQuestions, inventory: context.inventory, draft: context.draft, requestedAssets: context.requestedAssets });",
    new: "let review = await stage('fidelity', { sources: citedSpans(context.draft), readerQuestions: context.readerQuestions, inventory: context.inventory, plan: context.plan, draft: context.draft, requestedAssets: context.requestedAssets });",
  },
  {
    id: 'stage-route-completeness-disabled', file: `${core}pipeline.ts`, test: `${core}pipeline.test.ts`,
    mustFail: 'rejects a missing stage route before dispatch',
    old: "if (Object.keys(request.routes ?? {}).sort().join(',') !== 'author,edit,fidelity,inventory,plan,repair'",
    new: 'if (false',
  },
  {
    id: 'corpus-charged-twice', file: `${core}pipeline.ts`, test: `${app}self-corpus.test.ts`,
    mustFail: 'refuses a 1 MB corpus budget without truncation or a scripted send, then completes on sufficient budget and isolates one source perturbation',
    old: 'encodeCanonicalJson(compact, dataLimits(b.maxInputBytes))',
    new: 'encodeCanonicalJson(detached, dataLimits(b.maxInputBytes))',
  },
];

const digest = bytes => createHash('sha256').update(bytes).digest('hex');
const runGit = args => execFileSync('git', args, { cwd: root, encoding: 'utf8' }).trim();
const targets = [...new Set(mutations.flatMap(m => [m.file, m.test]))];
if (runGit(['status', '--porcelain', '--', ...targets])) throw new Error('mutation subjects or tests are dirty');
const commit = runGit(['rev-parse', 'HEAD']);
const scratch = mkdtempSync(join(tmpdir(), 'syzygy-m7-mutation-'));
const original = new Map([...new Set(mutations.map(m => m.file))].map(file => [file, readFileSync(join(root, file))]));

function run(test, label) {
  const output = join(scratch, `${label}.json`);
  const command = ['vitest', 'run', test, '--reporter=json', `--outputFile=${output}`];
  const result = spawnSync('npx', command, { cwd: root, env: { ...process.env, CI: '1' }, encoding: 'utf8' });
  if (result.error) throw result.error;
  let report;
  try { report = JSON.parse(readFileSync(output, 'utf8')); }
  catch { throw new Error(`missing test report for ${label}: exit=${result.status}; ${result.stderr}`); }
  const failing = report.testResults.flatMap(file => file.assertionResults)
    .filter(test => test.status === 'failed').map(test => test.fullName);
  return { command: `npx ${command.join(' ')}`, exit: result.status, total: report.numTotalTests,
    passed: report.numPassedTests, failed: report.numFailedTests, failing };
}

const records = [];
try {
  for (const [index, mutation] of mutations.entries()) {
    const before = original.get(mutation.file);
    const source = before.toString('utf8');
    if (source.split(mutation.old).length !== 2) throw new Error(`${mutation.id}: old fragment must occur exactly once`);
    const baseline = run(mutation.test, `baseline-${index}`);
    if (baseline.exit !== 0 || baseline.total === 0 || baseline.failed !== 0) throw new Error(`${mutation.id}: baseline not green`);
    let mutant;
    try {
      writeFileSync(join(root, mutation.file), source.replace(mutation.old, mutation.new));
      mutant = run(mutation.test, `mutant-${index}`);
    } finally { writeFileSync(join(root, mutation.file), before); }
    const after = readFileSync(join(root, mutation.file));
    const restored = before.equals(after);
    const killed = mutant.total > 0 && mutant.failed > 0 && mutant.failing.some(name => name.includes(mutation.mustFail));
    records.push({ ...mutation, baseline, mutant, sourceSha256Before: digest(before), sourceSha256After: digest(after), restored, killed });
    process.stdout.write(`${killed && restored ? 'KILLED' : 'SURVIVED'} ${mutation.id}: ${mutant.failed}/${mutant.total} failed, restored=${restored}\n`);
  }
} finally {
  for (const [file, bytes] of original) writeFileSync(join(root, file), bytes);
  rmSync(scratch, { recursive: true, force: true });
}
const evidence = { kind: 'm7-literal-source-mutations', capturedAt: new Date().toISOString(), testedCommit: commit,
  baselineAndMutantRunSeparately: true, records, summary: { planned: mutations.length,
    killedAndRestored: records.filter(record => record.killed && record.restored).length } };
const evidencePath = join(root, 'docs/evidence/polaris-m7-literal-mutations-2026-09-23.json');
writeFileSync(evidencePath, `${JSON.stringify(evidence, null, 2)}\n`);
process.stdout.write(`evidence: ${evidencePath}\n`);
if (evidence.summary.killedAndRestored !== mutations.length) process.exitCode = 1;
