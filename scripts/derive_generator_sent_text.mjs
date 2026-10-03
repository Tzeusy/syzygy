#!/usr/bin/env node
// Derive, from the code, what the generator hands to the `generate` port.
// Build first: `npx tsc -b packages/polaris-generation-core`.
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
console.log(JSON.stringify({
  generateInputFields: Object.keys(captured[0]).sort(),
  envelopeKeys: Object.keys(envelope),
  inputKeysAcrossFirstStage: Object.keys(envelope.inputs),
  authored, inputKeys,
  authoredBySource: { 'packages/polaris-generation-core/src/prompts.ts': 'promptForStage', 'packages/polaris-generation-core/src/provider-draft.ts': 'stageSchema' },
}, null, 2));
