#!/usr/bin/env node
// Time the recorder line slot's failing reads (syzygy-bpyt.8.17). Evidence tool, not a check and not authority.
//
//   (in each tree) npm ci && npx tsc -b packages/polaris-generation-consent packages/polaris-dossier
//   node scripts/measure_line_slot_reads.mjs <tree> --out <file.json> [--old <tree>]
//
// Two measurements, on the main thread with nothing else running in the process:
// - the record of the timing-bounded test in packages/polaris-generation-consent/src/recorder-template.test.ts (four line slots of
//   160 non-space characters, then a literal that fails): `templateFields` with `<tree>`'s `SLOT.line`, twenty times, and with the
//   ambiguous `[^\r\n]*\S[^\r\n]*` once (minutes), against the test's one-second bound;
// - the failing read of the provider statement version 2 record: the real record, as recorded and altered by each of
//   syzygy-bpyt.8.10's `PROSE_ALTERATIONS`, its `HEAD_FIELD_ALTERATION` and ` [altered]` on the last line, read with the production
//   template (`templateFields` over `PROVIDER_V2_FORM.template`, the read syzygy-bpyt.8.10 timed) five times in `<tree>` and once in
//   `--old` when given; and the same records, in memory (the file on disk is not touched), read whole through the production path by
//   `createPackageGateSources(...).providerStatements.statementsFor('redis-redis')`, which evaluates that template twice, and by
//   `readDigestBoundActState` over `PROVIDER_V2_FORM`, three times each in `<tree>` and once each in `--old`. A whole read also sweeps
//   every decisions file for other records naming the act, which takes as long on a record that holds as on one that fails.
// Timings depend on the machine and its load; the answers do not. It reads the trees only and writes only `--out`. It exits 1 when a
// failing template read in `<tree>` takes 100 ms or more, the test record takes `<tree>` a tenth of the bound or more, or (with
// `--old`) an answer differs between the trees.

import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as fsp from 'node:fs/promises';
import * as os from 'node:os';
import * as path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const SCRIPT = fileURLToPath(import.meta.url);
const SCRIPT_REL = 'scripts/measure_line_slot_reads.mjs';
const RECORD = '.syzygy/governance/decisions/DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md';
const AMBIGUOUS = '[^\\r\\n]*\\S[^\\r\\n]*';
const BOUND_MS = 1000, READ_LIMIT_MS = 100, NOW = Date.parse('2026-10-22T12:00:00Z');
const sha256 = text => createHash('sha256').update(text, 'utf8').digest('hex');
const git = (tree, ...args) => execFileSync('git', ['-C', tree, ...args], { encoding: 'utf8' }).trim();
const label = value => JSON.stringify(value).replace(/\b[0-9a-f]{40,64}\b/g, '<hex>').slice(0, 200);
const timed = async read => { const started = performance.now(); let said; try { said = label(await read()); } catch (error) { said = `throws ${error?.name}: ${error?.message}`; } return { ms: Math.round((performance.now() - started) * 100) / 100, said }; };
const median = values => [...values].sort((a, b) => a - b)[Math.floor(values.length / 2)];
/** When a measurement started, and the host's 1, 5 and 15 minute load averages then (what `uptime` prints). */
const host = () => ({ at: new Date().toISOString(), loadAverage: os.loadavg().map(n => Math.round(n * 100) / 100) });

const argv = process.argv.slice(2);
const arg = flag => (argv.includes(flag) ? argv[argv.indexOf(flag) + 1] : undefined);
const tree = argv[0] === undefined || argv[0].startsWith('--') ? undefined : path.resolve(argv[0]);
const out = arg('--out'), oldTree = arg('--old') === undefined ? undefined : path.resolve(arg('--old'));
if (tree === undefined || out === undefined) { process.stderr.write('usage: node scripts/measure_line_slot_reads.mjs <tree> --out <file.json> [--old <tree>]\n'); process.exit(2); }

const load = async root => ({
  consent: await import(pathToFileURL(path.join(root, 'packages/polaris-generation-consent/dist/index.js')).href),
  gate: await import(pathToFileURL(path.join(root, 'packages/polaris-dossier/dist/gate-sources.js')).href),
});
const subject = await load(tree), before = oldTree === undefined ? null : await load(oldTree);
const testing = await import(pathToFileURL(path.join(tree, 'packages/polaris-generation-consent/dist/testing.js')).href);
if (!Array.isArray(testing.PROSE_ALTERATIONS) || typeof testing.HEAD_FIELD_ALTERATION !== 'function') throw new Error('this tree\'s test-support build exports no PROSE_ALTERATIONS and HEAD_FIELD_ALTERATION (syzygy-bpyt.8.10, PR #500)');

// The timing-bounded test's record.
const { recorderTemplate, templateFields, SLOT } = subject.consent;
const SLOTS = ['a', 'b', 'c', 'd'];
const testTemplate = pattern => recorderTemplate('a: {a}\nb: {b}\nc: {c}\nd: {d}\nEND\n', Object.fromEntries(SLOTS.map(s => [s, pattern])));
const testRecord = `${SLOTS.map(s => `${s}: ${'x'.repeat(160)}\n`).join('')}END!\n`;
const fresh = testTemplate(SLOT.line), freshMs = [], freshHost = host();
for (let i = 0; i < 20; i += 1) { const t = await timed(() => templateFields(fresh, testRecord)); if (t.said !== 'null') throw new Error(`the test record read ${t.said}`); freshMs.push(t.ms); }
process.stderr.write(`test record, ${SLOT.line}: max ${Math.max(...freshMs)} ms; now the ambiguous pattern, once\n`);
const ambiguousHost = host(), ambiguous = await timed(() => templateFields(testTemplate(AMBIGUOUS), testRecord));
process.stderr.write(`test record, ${AMBIGUOUS}: ${ambiguous.ms} ms\n`);

// The failing provider statement version 2 reads.
const text = fs.readFileSync(path.join(tree, RECORD), 'utf8');
const cases = [['as recorded', text], ...testing.PROSE_ALTERATIONS.map(([name, alter]) => [name, alter(text)]), ['date-field-altered', testing.HEAD_FIELD_ALTERATION(text)], ['last-line-altered', text.replace(/([^\n])(\n*)$/, '$1 [altered]$2')]];
const overlay = (root, altered) => ({
  readdir: dir => fsp.readdir(dir),
  readFile: async file => (path.relative(root, file) === RECORD ? altered : fsp.readFile(file, 'utf8')),
});
const reads = (mod, root, altered) => {
  const fsPort = overlay(root, altered);
  return [
    ['statementsFor', () => mod.gate.createPackageGateSources({ root, fs: fsPort, now: () => NOW }).providerStatements.statementsFor('redis-redis')],
    ['readDigestBoundActState', () => mod.consent.readDigestBoundActState({ root, fs: fsPort, now: NOW, form: mod.gate.PROVIDER_V2_FORM })],
  ];
};
const templateRuns = [];
for (const [name, altered] of cases) {
  const times = [], newHost = host();
  let said;
  for (let i = 0; i < 5; i += 1) { const t = await timed(() => templateFields(subject.gate.PROVIDER_V2_FORM.template, altered)); times.push(t.ms); said = t.said; }
  const row = { case: name, changed: altered !== text, newHost, newMs: { median: median(times), max: Math.max(...times) }, newRead: said !== 'null' };
  if (before !== null) {
    const oldHost = host(), t = await timed(() => before.consent.templateFields(before.gate.PROVIDER_V2_FORM.template, altered));
    Object.assign(row, { oldHost, oldMs: t.ms, sameAnswer: t.said === said });
  }
  templateRuns.push(row);
  process.stderr.write(`${name} template: ${row.newMs.max} ms${row.oldMs === undefined ? '' : `, old ${row.oldMs} ms`}\n`);
}
const runs = [];
for (const [name, altered] of cases) {
  for (const [reader, read] of reads(subject, tree, altered)) {
    const times = [], newHost = host();
    let said;
    for (let i = 0; i < 3; i += 1) { const t = await timed(read); times.push(t.ms); said = t.said; }
    const row = { case: name, changed: altered !== text, reader, newHost, newMs: { median: median(times), max: Math.max(...times) }, newAnswer: said };
    if (before !== null) {
      const [, oldRead] = reads(before, oldTree, altered).find(([r]) => r === reader);
      const oldHost = host(), t = await timed(oldRead);
      Object.assign(row, { oldHost, oldMs: t.ms, sameAnswer: t.said === said });
    }
    runs.push(row);
    process.stderr.write(`${name} ${reader}: ${row.newMs.max} ms${row.oldMs === undefined ? '' : `, old ${row.oldMs} ms`}\n`);
  }
}

const binding = root => ({ commit: git(root, 'rev-parse', 'HEAD'), clean: git(root, 'status', '--porcelain', '--untracked-files=no') === '',
  recorderTemplateJsSha256: sha256(fs.readFileSync(path.join(root, 'packages/polaris-generation-consent/dist/recorder-template.js'), 'utf8')) });
const failing = templateRuns.filter(r => !r.newRead);
const document = {
  schema: 'line-slot-read-timing/1',
  bead: 'syzygy-bpyt.8.17',
  text: 'Evidence record, not authority: the recorder line slot\'s failing reads timed, the timing-bounded test\'s record and the provider statement version 2 record through the production path. Generated by the script named here; do not edit.',
  script: { path: SCRIPT_REL, sha256: sha256(fs.readFileSync(SCRIPT, 'utf8')) },
  measuredOn: { tree: { ...binding(tree), linePattern: SLOT.line }, ...(before === null ? {} : { old: { ...binding(oldTree), linePattern: before.consent.SLOT.line } }), node: process.version, cores: os.availableParallelism() },
  timing: 'wall time on the main thread, nothing else running in the process; the host carried other lanes\' work (each measurement names its start and the load averages then), so times are upper bounds of an unloaded run, not measurements of one',
  testRecord: {
    test: 'the line slot (syzygy-bpyt.8.17) refuses a record that fails after four long line slots within a second',
    slots: SLOTS.length, slotLength: 160, sha256: sha256(testRecord), boundMs: BOUND_MS,
    linePatternHost: freshHost, linePatternMs: { first: freshMs[0], median: median(freshMs), max: Math.max(...freshMs), runs: freshMs.length },
    ambiguousHost, ambiguousMs: ambiguous.ms, ambiguousAnswer: ambiguous.said,
    passMargin: Math.round(BOUND_MS / Math.max(...freshMs)), killMargin: Math.round(ambiguous.ms / BOUND_MS),
  },
  providerV2: {
    record: { path: RECORD, sha256: sha256(text) }, template: 'PROVIDER_V2_FORM.template', limitMs: READ_LIMIT_MS,
    templateRuns,
    failingTemplateReads: failing.length, failingTemplateReadMaxMs: Math.max(...failing.map(r => r.newMs.max)),
    ...(before === null ? {} : { failingTemplateReadOldMinMs: Math.min(...failing.map(r => r.oldMs)), failingTemplateReadOldMaxMs: Math.max(...failing.map(r => r.oldMs)) }),
    now: new Date(NOW).toISOString(), wholeReadRuns: runs,
    ...(before === null ? {} : { answersAgree: templateRuns.every(r => r.sameAnswer) && runs.every(r => r.sameAnswer) }),
  },
};
fs.writeFileSync(out, `${JSON.stringify(document, null, 1)}\n`);
process.exitCode = failing.length > 0 && document.providerV2.failingTemplateReadMaxMs < READ_LIMIT_MS && Math.max(...freshMs) < BOUND_MS / 10 && (before === null || document.providerV2.answersAgree) ? 0 : 1;
