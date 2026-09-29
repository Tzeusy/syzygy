// Executable rule-6 proof for M13 slices 1-4. Exact source fragments are
// temporarily replaced only from a committed clean tree, then restored.
import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const app = 'apps/three-surface-poc/src/';
const polaris = `${app}polaris.ts`;
const copy = `${app}polaris-copy.test.ts`;
const reach = `${app}polaris-reachability.test.ts`;
const edits = (old, replacement) => [{ old, replacement }];
const mutations = [
  {
    id: 'exact-label-bare', file: polaris, tests: [copy],
    edits: edits("${copy('label.exact-text')} — ${escapeHtml(path)}", "${copy('label.exact-text')}"),
    mustFail: 'classifies each interpolated source control',
  },
  {
    id: 'source-label-constant', file: polaris, tests: [copy],
    edits: edits("${copy('label.source-record')} — ${escapeHtml(source.path)}", "${copy('label.source-record')} — constant"),
    mustFail: 'classifies each interpolated source control',
  },
  {
    id: 'exact-href-identity-changed', file: polaris, tests: [copy, `${app}polaris-source-route.test.ts`],
    edits: edits('sourceRouteHref(activeMountPrefix, identity)', 'sourceRouteHref(activeMountPrefix, path)'),
    mustFail: 'classifies each interpolated source control',
  },
  {
    id: 'heading-fixed-offset', file: `${app}polaris-markdown.ts`, tests: [`${app}polaris-markdown.test.ts`, reach],
    edits: edits('Math.min(6, anchorHeadingLevel + 1 + heading[1]!.length - shallowestHeading)', 'Math.min(6, heading[1]!.length + 3)'),
    mustFail: 'starts a shallowest ### one below its anchor',
  },
  {
    id: 'selected-heading-reverts-to-three-hashes', file: `${app}polaris-reading.ts`, tests: [`${app}polaris-reading.test.ts`],
    edits: edits("heading === true ? '# ' : ''", "heading === true ? '### ' : ''"),
    mustFail: 'preserves exact selected passages and the full declaration',
  },
  {
    id: 'missing-digest-disclosure-empty', file: polaris, tests: [`${app}polaris-project-shape.test.ts`],
    edits: edits("<small${copyAttr('sentence.no-body-read')}>${copy('sentence.no-body-read')}</small>", "<small${copyAttr('sentence.no-body-read')}></small>"),
    mustFail: 'keeps every source record visible in six scoped columns',
  },
  {
    id: 'source-table-not-bare', file: polaris, tests: [reach],
    edits: edits("tableRegion('polaris-shape-sources', `<table><thead><tr>", "tableRegion('polaris-shape-sources', `<table role=\"region\"><thead><tr>"),
    mustFail: 'carries no pointer-only or layout-only affordance',
  },
  {
    id: 'source-target-inside-details', file: polaris, tests: [`${app}polaris-first-reading.test.ts`],
    edits: [
      { old: "${tableRegion('polaris-shape-sources', `<table><thead><tr>", replacement: "<details><summary>Source records</summary>${tableRegion('polaris-shape-sources', `<table><thead><tr>" },
      { old: ", ' data-source-index')}\n  </section>\n  <section class=\"claim-section\" data-polaris-section=\"shape:exclusions\">",
        replacement: ", ' data-source-index')}</details>\n  </section>\n  <section class=\"claim-section\" data-polaris-section=\"shape:exclusions\">" },
    ],
    mustFail: 'keeps each item population and the exclusions complete behind a native disclosure',
  },
  {
    id: 'outline-heading-deleted', file: polaris, tests: [reach],
    edits: edits('missing[level]!.push(`<a href="#${escapeHtml(id)}"${SCOPE}>${label} — ${escapeHtml(group)}</a>`);',
      "if (!id.includes('currency-probe')) missing[level]!.push(`<a href=\"#${escapeHtml(id)}\"${SCOPE}>${label} — ${escapeHtml(group)}</a>`);"),
    mustFail: 'lists the four depths as native links in document order',
  },
  {
    id: 'early-shortcuts-inside-details', file: `${app}page-shell.ts`, tests: [reach],
    edits: edits("${input.earlyLinks ?? ''}", "<details><summary>Group shortcuts</summary>${input.earlyLinks ?? ''}</details>"),
    mustFail: 'keeps seven group shortcuts among the first ten tabs',
  },
  {
    id: 'hidden-count-constant', file: polaris, tests: [`${app}polaris-accessibility.browser.test.ts`],
    edits: edits("drawer.querySelectorAll('a').length", '1'),
    mustFail: 'gives seven early native shortcuts and a complete no-script outline with a truthful live hidden count',
  },
];

const digest = bytes => createHash('sha256').update(bytes).digest('hex');
const git = args => execFileSync('git', args, { cwd: root, encoding: 'utf8' }).trim();
const subjects = [...new Set(mutations.flatMap(mutation => [mutation.file, ...mutation.tests]))];
if (git(['status', '--porcelain', '--', ...subjects])) throw new Error('mutation subjects or tests are dirty');
const commit = git(['rev-parse', 'HEAD']);
const originals = new Map([...new Set(mutations.map(mutation => mutation.file))].map(file => [file, readFileSync(join(root, file))]));
const scratch = mkdtempSync(join(tmpdir(), 'syzygy-m13-mutation-'));

function run(tests, label) {
  const reportPath = join(scratch, `${label}.json`);
  const args = ['vitest', 'run', ...tests, '--reporter=json', `--outputFile=${reportPath}`];
  const result = spawnSync('npx', args, { cwd: root, env: { ...process.env, CI: '1' }, encoding: 'utf8' });
  if (result.error) throw result.error;
  let report;
  try { report = JSON.parse(readFileSync(reportPath, 'utf8')); }
  catch { throw new Error(`missing test report for ${label}: exit=${result.status}; ${result.stderr}`); }
  const failing = report.testResults.flatMap(file => file.assertionResults)
    .filter(test => test.status === 'failed').map(test => test.fullName);
  return { command: `npx ${args.join(' ')}`, exit: result.status, total: report.numTotalTests,
    passed: report.numPassedTests, failed: report.numFailedTests, failing };
}

const records = [];
try {
  for (const [index, mutation] of mutations.entries()) {
    const before = originals.get(mutation.file);
    let source = before.toString('utf8');
    for (const edit of mutation.edits) {
      if (source.split(edit.old).length !== 2) throw new Error(`${mutation.id}: old fragment must occur exactly once`);
      source = source.replace(edit.old, edit.replacement);
    }
    const baseline = run(mutation.tests, `baseline-${index}`);
    if (baseline.exit !== 0 || baseline.total === 0 || baseline.failed !== 0) throw new Error(`${mutation.id}: baseline not green`);
    let mutant;
    try {
      writeFileSync(join(root, mutation.file), source);
      mutant = run(mutation.tests, `mutant-${index}`);
    } finally { writeFileSync(join(root, mutation.file), before); }
    const after = readFileSync(join(root, mutation.file));
    const restored = before.equals(after);
    const killed = mutant.total > 0 && mutant.failed > 0 && mutant.failing.some(name => name.includes(mutation.mustFail));
    records.push({ ...mutation, baseline, mutant, sourceSha256Before: digest(before), sourceSha256After: digest(after), restored, killed });
    process.stdout.write(`${killed && restored ? 'KILLED' : 'SURVIVED'} ${mutation.id}: ${mutant.failed}/${mutant.total} failed, restored=${restored}\n`);
  }
} finally {
  for (const [file, bytes] of originals) writeFileSync(join(root, file), bytes);
  rmSync(scratch, { recursive: true, force: true });
}
const evidence = { kind: 'm13-literal-source-mutations', capturedAt: new Date().toISOString(), testedCommit: commit,
  baselineAndMutantRunSeparately: true, records, summary: { planned: mutations.length,
    killedAndRestored: records.filter(record => record.killed && record.restored).length } };
const evidencePath = join(root, 'docs/evidence/polaris-m13-literal-mutations-2026-09-23.json');
writeFileSync(evidencePath, `${JSON.stringify(evidence, null, 2)}\n`);
process.stdout.write(`evidence: ${evidencePath}\n`);
if (evidence.summary.killedAndRestored !== mutations.length) process.exitCode = 1;
