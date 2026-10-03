#!/usr/bin/env node
// Derive, from the code, what the generator hands to the `generate` port.
// Build first: `npx tsc -b packages/polaris-generation-core`.
// Prints a JSON report, or with --table the markdown table the public-repo
// admission builder embeds in the egress record. Every envelope field, every
// `inputs` field and every `generate` port field must have exactly one class
// below; a field with none fails the run (exit 2).
// Prints a JSON report; digests appear here at run time, never in the
// public-repo admission package (CG-15). Observed over the checked-out tree.
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { runGenerationPipeline, promptForStage, stageSchema, generationAnchorId, gitBlobObjectId } from '../packages/polaris-generation-core/dist/index.js';

const STAGES = ['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair'];
const sha = text => createHash('sha256').update(text).digest('hex');

// 1. The envelope the real pipeline serializes: stub every port, capture the
//    first `generate` call, then refuse its reply so the run stops.
const captured = [];
const body = 'fixture body';
const base = { repositoryId: 'derive:fixture', revision: 'a'.repeat(64), path: 'derive/src-1.md', objectId: gitBlobObjectId(body) };
const source = { ...base, sourceId: 'src-1', evaluationId: 'derive:evaluation', classificationBasis: 'body', exclusion: { excluded: false }, body,
  spans: [{ anchorId: generationAnchorId(base, 0, Buffer.byteLength(body)), start: 0, end: Buffer.byteLength(body), text: body }] };
const ports = {
  now: () => Date.now(), verifySources: async () => true, permissionIdentity: async () => 'derive',
  admit: async input => ({ kind: 'reserved', permit: { attemptId: `d:${input.ordinal}`, maxUsageUnits: 5, maxOutputBytes: 10_000 } }),
  permitted: async () => true, releaseUnsent: async () => undefined,
  responseSchema: stageSchema, validate: () => { throw new Error('derive-stop'); }, fidelity: () => ({ blocking: false, findings: [] }),
  generate: async input => { captured.push(input); return { body: '{}', model: 'derive', usageUnits: 1 }; },
  record: async () => undefined, lateReceipt: async () => undefined,
};
const request = {
  requestId: 'derive', projectId: 'derive', snapshotId: 'derive',
  routes: Object.fromEntries(STAGES.map(s => [s, 'derive'])), startedAt: Date.now(),
  sources: [source], readerQuestions: ['q'], requestedAssets: [{ id: 'x', kind: 'section', required: true }],
  budget: { maxCalls: 7, maxInputBytes: 500_000, maxOutputBytes: 100_000, maxUsageUnits: 100, maxElapsedMs: 30_000, maxRepairCycles: 1, accountingPolicy: 'derive' },
};
const outcome = await runGenerationPipeline(request, ports, new AbortController().signal).catch(e => e); if (!captured.length) { console.error("no generate call; pipeline outcome:", JSON.stringify(outcome)?.slice(0, 400), String(outcome).slice(0,200)); process.exit(1); }
const envelope = JSON.parse(captured[0].input);

// 2. Per stage, the generator-authored text: promptForStage (prompts.ts) and
//    stageSchema (provider-draft.ts).
const authored = STAGES.map(stage => {
  const prompt = promptForStage(stage);
  const schema = stageSchema(stage);
  return { stage, promptVersion: prompt.version, systemBytes: Buffer.byteLength(prompt.system), systemSha256: sha(prompt.system),
    schemaVersion: schema.version, schemaBytes: Buffer.byteLength(JSON.stringify(schema.schema)), schemaSha256: sha(JSON.stringify(schema.schema)) };
});

// 3. The `inputs` keys per stage, read from the pipeline's own call sites.
const text = readFileSync(new URL('../packages/polaris-generation-core/src/pipeline.ts', import.meta.url), 'utf8');
const inputKeys = {};
for (const m of text.matchAll(/await stage\('(\w+)', \{([^}]*)\}\)/g)) {
  inputKeys[m[1]] = [...new Set([...inputKeys[m[1]] ?? [], ...m[2].split(',').map(p => p.trim().split(':')[0].trim()).filter(Boolean)])];
}

// 4. One closed class per field. Classes: target-content (spans, under an
//    observation consent), target-metadata (source ids, bases, exclusion
//    flags and reasons, no body), composite (validated stage artifacts
//    computed from target content), instruction-text (generator-authored
//    prompts and schemas), envelope-control (version and stage labels
//    produced by the same symbols) and run-profile (reader questions and
//    requested assets).
const ENVELOPE_CLASS = { promptVersion: 'envelope-control', system: 'instruction-text', responseSchemaVersion: 'envelope-control', responseSchema: 'instruction-text' };
const INPUT_CLASS = { sourcePopulation: 'target-metadata', readerQuestions: 'run-profile', requestedAssets: 'run-profile',
  inventory: 'composite', plan: 'composite', draft: 'composite', findings: 'composite' };
const PORT_FIELD = {
  input: ['the envelope', 'sent as the user message'],
  system: ['instruction-text', 'sent as the system prompt'],
  responseSchema: ['instruction-text', 'a copy of the envelope field; not sent separately'],
  stage: ['envelope-control', 'never sent'],
  permit: ['dispatch permit', 'never sent'],
  signal: ['abort signal', 'never sent'],
};
const failures = [];
// `sources` is classed by the expression the call site assigns it.
const sourceExpr = {};
for (const m of text.matchAll(/await stage\('(\w+)', \{([^}]*)\}\)/g)) {
  const mm = /sources:\s*([A-Za-z.]+(?:\([^)]*\))?)/.exec(m[2]);
  if (mm) sourceExpr[m[1]] = mm[1];
}
const sourcesClass = stage => {
  const expr = sourceExpr[stage] ?? '';
  if (expr === 'sourcePopulation') return 'target-metadata';
  if (expr.startsWith('citedSpans(') || expr === 'context.sources') return 'target-content';
  failures.push(`sources at stage ${stage}: unclassified expression ${JSON.stringify(expr)}`);
  return 'UNCLASSIFIED';
};
const rows = [];
for (const key of Object.keys(envelope)) {
  if (key === 'inputs') continue;
  const cls = ENVELOPE_CLASS[key];
  if (!cls) failures.push(`envelope field ${key} has no class`);
  rows.push({ where: 'envelope', field: key, stages: STAGES, cls: cls ?? 'UNCLASSIFIED' });
}
const byField = new Map();
for (const stage of STAGES) for (const key of inputKeys[stage] ?? []) {
  const cls = key === 'sources' ? sourcesClass(stage) : INPUT_CLASS[key];
  if (!cls) { failures.push(`inputs field ${key} (stage ${stage}) has no class`); continue; }
  const id = `${key}\u0000${cls}`;
  byField.set(id, { where: 'inputs', field: key, cls, stages: [...(byField.get(id)?.stages ?? []), stage] });
}
rows.push(...byField.values());
const portRows = Object.keys(captured[0]).sort().map(key => {
  if (!PORT_FIELD[key]) { failures.push(`port field ${key} has no class`); return null; }
  return { where: 'generate port', field: key, cls: PORT_FIELD[key][0], note: PORT_FIELD[key][1] };
}).filter(Boolean);
for (const key of Object.keys(envelope.inputs)) if (!(key in INPUT_CLASS) && key !== 'sources') failures.push(`captured inputs field ${key} unmapped`);
if (failures.length) { console.error('UNCLASSIFIED:\n' + failures.join('\n')); process.exit(2); }

if (process.argv.includes('--table')) {
  const esc = s => s.replaceAll('|', '\\|');
  const lines = ['| Where | Field | Stages | Class |', '|---|---|---|---|'];
  for (const r of rows) lines.push(`| ${r.where} | \`${r.field}\` | ${r.stages.length === STAGES.length ? 'all' : r.stages.join(', ')} | ${esc(r.cls)} |`);
  for (const r of portRows) lines.push(`| ${r.where} | \`${r.field}\` | all | ${esc(r.cls)}; ${esc(r.note)} |`);
  console.log(lines.join('\n'));
  process.exit(0);
}
console.log(JSON.stringify({
  generateInputFields: Object.keys(captured[0]).sort(),
  envelopeKeys: Object.keys(envelope),
  inputKeysAcrossFirstStage: Object.keys(envelope.inputs),
  authored, inputKeys, classified: rows, portRows,
  authoredBySource: { 'packages/polaris-generation-core/src/prompts.ts': 'promptForStage', 'packages/polaris-generation-core/src/provider-draft.ts': 'stageSchema' },
}, null, 2));
