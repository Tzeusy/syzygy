#!/usr/bin/env node
// Derive, from the code, what the generator hands to the `generate` port.
// Build first: `npx tsc -b packages/polaris-generation-core`.
// Prints a JSON report, or with --table the markdown table the public-repo
// admission builder embeds in the egress record. Every envelope field, every
// `inputs` field and every `generate` port field must have exactly one class
// below; a field with none fails the run (exit 2).
// Prints a JSON report; digests appear here at run time, never in the
// public-repo admission package (CG-15). Observed over the checked-out tree.
// With --discovery it also derives the two discovery calls (discovery-map,
// discovery-reduce), which run before the pipeline: their envelopes are built
// by discovery-provider.ts from promptForStage and stageSchema, and every
// `inputs` leaf gets a class from DISCOVERY_INPUT_CLASS. Without the flag the
// output is unchanged, so the embedded egress table moves only when asked.
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import ts from 'typescript';
import { runGenerationPipeline, promptForStage, stageSchema, generationAnchorId, gitBlobObjectId, READER_QUESTION_TOPICS, discoveryMapEnvelope, discoveryReduceEnvelope, discoverAndSelect, generationSourcesForBody, DEFAULT_DISCOVERY_BUDGET } from '../packages/polaris-generation-core/dist/index.js';

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
  sources: [source], readerQuestions: [{ id: 'q1', topics: [READER_QUESTION_TOPICS[0]], text: 'q' }], requestedAssets: [{ id: 'x', kind: 'section', required: true }],
  budget: { maxCalls: 7, maxInputBytes: 500_000, maxOutputBytes: 100_000, maxUsageUnits: 100, maxElapsedMs: 30_000, maxRepairCycles: 1, accountingPolicy: 'derive' },
};
const outcome = await runGenerationPipeline(request, ports, new AbortController().signal).catch(e => e); if (!captured.length) { console.error("no generate call; pipeline outcome:", JSON.stringify(outcome)?.slice(0, 400), String(outcome).slice(0,200)); process.exit(1); }
const envelope = JSON.parse(captured[0].input);
// The pipeline's reader questions are structured ({ id, topics, text }). The
// table classes the field as a whole (run-profile), so every leaf the captured
// envelope carries must be one of these three; a new leaf has no class and
// fails the run (exit 2) instead of leaving unclassified text in a request.
const READER_QUESTION_LEAVES = ['id', 'topics', 'text'];
for (const q of envelope.inputs.readerQuestions ?? []) {
  const keys = q !== null && typeof q === 'object' && !Array.isArray(q) ? Object.keys(q) : ['<non-object>'];
  for (const key of keys) if (!READER_QUESTION_LEAVES.includes(key)) { console.error(`readerQuestions[] leaf ${key} has no class`); process.exit(2); }
}

// 2. Per stage, the generator-authored text: promptForStage (prompts.ts) and
//    stageSchema (provider-draft.ts).
const authored = STAGES.map(stage => {
  const prompt = promptForStage(stage);
  const schema = stageSchema(stage);
  return { stage, promptVersion: prompt.version, systemBytes: Buffer.byteLength(prompt.system), systemSha256: sha(prompt.system),
    schemaVersion: schema.version, schemaBytes: Buffer.byteLength(JSON.stringify(schema.schema)), schemaSha256: sha(JSON.stringify(schema.schema)) };
});

// 3. The `inputs` keys per stage, read from the pipeline's own call sites with
//    the TypeScript parser, not a text pattern. Every call of `stage(...)` must
//    name a literal stage in STAGES and pass an object literal of plain
//    properties; anything else (a variable, a spread, a computed key, a
//    template string) fails the run, and so does a stage in STAGES that no
//    call site names. A call the derivation cannot read is never dropped.
const pipelineArg = process.argv.indexOf('--pipeline');   // a mutated copy, for the builder's selftest only
const pipelinePath = pipelineArg > 0 ? process.argv[pipelineArg + 1] : new URL('../packages/polaris-generation-core/src/pipeline.ts', import.meta.url);
const sourceFile = ts.createSourceFile('pipeline.ts', readFileSync(pipelinePath, 'utf8'), ts.ScriptTarget.Latest, true);
const inputKeys = {};
const sourceExpr = {};
const callFailures = [];
const visit = node => {
  if (ts.isCallExpression(node) && ts.isIdentifier(node.expression) && node.expression.text === 'stage') {
    const [name, inputs] = node.arguments;
    const where = `pipeline.ts:${sourceFile.getLineAndCharacterOfPosition(node.getStart()).line + 1}`;
    if (!name || !ts.isStringLiteral(name) || !STAGES.includes(name.text)) { callFailures.push(`${where}: stage name is not a literal in STAGES`); }
    else if (!inputs || !ts.isObjectLiteralExpression(inputs)) { callFailures.push(`${where}: inputs of ${name.text} is not an object literal`); }
    else {
      const keys = [];
      for (const prop of inputs.properties) {
        if (ts.isShorthandPropertyAssignment(prop)) keys.push(prop.name.text);
        else if (ts.isPropertyAssignment(prop) && ts.isIdentifier(prop.name)) {
          keys.push(prop.name.text);
          if (prop.name.text === 'sources') sourceExpr[name.text] = prop.initializer.getText(sourceFile);
        } else callFailures.push(`${where}: inputs of ${name.text} has a property the derivation cannot read`);
      }
      inputKeys[name.text] = [...new Set([...inputKeys[name.text] ?? [], ...keys])];
    }
  }
  ts.forEachChild(node, visit);
};
visit(sourceFile);
for (const stage of STAGES) if (!inputKeys[stage]) callFailures.push(`stage ${stage} has no readable call site`);
if (callFailures.length) { console.error('UNREADABLE CALL SITES:\n' + callFailures.join('\n')); process.exit(2); }

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
// `sources` is classed by the expression the call site assigns it (above).
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
// 5. Discovery (--discovery only). Fixture requests with every field present;
//    leaves are classed by path, array indices collapsed to [].
const DISCOVERY = process.argv.includes('--discovery');
const DISCOVERY_STAGES = ['discovery-map', 'discovery-reduce'];
const DISCOVERY_INPUT_CLASS = {
  'subsystem': 'target-metadata', 'readerQuestions[]': 'run-profile',
  'items[].blobId': 'target-metadata', 'items[].path': 'target-metadata', 'items[].excerpt': 'target-content',
  'maxSelected': 'envelope-control', 'subsystems[].subsystem': 'target-metadata', 'subsystems[].blobs': 'target-metadata',
  'subsystems[].claims[].blobId': 'target-metadata', 'subsystems[].claims[].path': 'target-metadata',
  'subsystems[].claims[].claim': 'composite', 'subsystems[].claims[].relevance': 'composite',
};
const discoveryRows = [];
const discoveryAuthored = [];
if (DISCOVERY) {
  const leaves = (value, path = '') => Array.isArray(value) ? value.flatMap(item => leaves(item, `${path}[]`))
    : value !== null && typeof value === 'object' ? Object.entries(value).flatMap(([key, child]) => leaves(child, path ? `${path}.${key}` : key)) : [path];
  // The requests are the ones discoverAndSelect itself builds, captured at the
  // map and reduce ports, so a field the producer adds appears here and must be
  // classed: a hand-written item hides it (the #340 excerpt fields did, until
  // the table was run with them). Two files in one subsystem give the reduce
  // call claims to carry.
  const capturedDiscovery = {};
  const fixtureBodies = ['# a\n\nfixture prose.\n', 'int f(void) { return 1; }\n'];
  const discoverySources = fixtureBodies.flatMap((text, i) => generationSourcesForBody({
    sourceId: `derive-d${i}`, repositoryId: 'derive:fixture', revision: 'a'.repeat(40), path: `derive/d${i}.${i ? 'c' : 'md'}`,
    objectId: gitBlobObjectId(text), evaluationId: 'derive:evaluation', body: text }));
  await discoverAndSelect(discoverySources, ['q'], { ...DEFAULT_DISCOVERY_BUDGET, maxSelected: 1 }, {
    permitted: async () => true,
    receipt: async () => {},
    map: async input => { capturedDiscovery['discovery-map'] ??= input;
      return { claims: input.items.map(item => ({ blobId: item.blobId, claim: 'fixture claim', relevance: 5 })), usageUnits: 1 }; },
    reduce: async input => { capturedDiscovery['discovery-reduce'] ??= input; return { ranked: [], usageUnits: 1 }; },
  });
  if (!capturedDiscovery['discovery-map'] || !capturedDiscovery['discovery-reduce']) failures.push('discovery fixture did not reach both ports');
  const built = failures.length ? {} : {
    'discovery-map': discoveryMapEnvelope(capturedDiscovery['discovery-map']).envelope,
    'discovery-reduce': discoveryReduceEnvelope(capturedDiscovery['discovery-reduce']).envelope,
  };
  for (const stage of failures.length ? [] : DISCOVERY_STAGES) {
    const envelope = built[stage];
    const prompt = promptForStage(stage);
    const schema = stageSchema(stage);
    // The instruction text must be exactly the two symbols' output.
    if (envelope.system !== prompt.system || envelope.promptVersion !== prompt.version
      || JSON.stringify(envelope.responseSchema) !== JSON.stringify(schema.schema) || envelope.responseSchemaVersion !== schema.version) {
      failures.push(`${stage}: envelope instruction text is not promptForStage/stageSchema output`);
    }
    discoveryAuthored.push({ stage, promptVersion: prompt.version, systemBytes: Buffer.byteLength(prompt.system), systemSha256: sha(prompt.system),
      schemaVersion: schema.version, schemaBytes: Buffer.byteLength(JSON.stringify(schema.schema)), schemaSha256: sha(JSON.stringify(schema.schema)) });
    for (const key of Object.keys(envelope)) {
      if (key === 'inputs') continue;
      const cls = ENVELOPE_CLASS[key];
      if (!cls) failures.push(`${stage}: envelope field ${key} has no class`);
      discoveryRows.push({ where: 'envelope', field: key, stages: [stage], cls: cls ?? 'UNCLASSIFIED' });
    }
    for (const path of [...new Set(leaves(envelope.inputs))].sort()) {
      const cls = DISCOVERY_INPUT_CLASS[path];
      if (!cls) failures.push(`${stage}: inputs field ${path} has no class`);
      discoveryRows.push({ where: 'inputs', field: path, stages: [stage], cls: cls ?? 'UNCLASSIFIED' });
    }
  }
}

if (failures.length) { console.error('UNCLASSIFIED:\n' + failures.join('\n')); process.exit(2); }

if (process.argv.includes('--table')) {
  const esc = s => s.replaceAll('|', '\\|');
  const lines = ['| Where | Field | Stages | Class |', '|---|---|---|---|'];
  for (const r of rows) lines.push(`| ${r.where} | \`${r.field}\` | ${r.stages.length === STAGES.length ? 'all' : r.stages.join(', ')} | ${esc(r.cls)} |`);
  for (const r of portRows) lines.push(`| ${r.where} | \`${r.field}\` | all | ${esc(r.cls)}; ${esc(r.note)} |`);
  for (const r of discoveryRows) lines.push(`| discovery ${r.where} | \`${r.field}\` | ${r.stages.join(', ')} | ${esc(r.cls)} |`);
  console.log(lines.join('\n'));
  process.exit(0);
}
console.log(JSON.stringify({
  generateInputFields: Object.keys(captured[0]).sort(),
  envelopeKeys: Object.keys(envelope),
  inputKeysAcrossFirstStage: Object.keys(envelope.inputs),
  authored, inputKeys, classified: rows, portRows,
  authoredBySource: { 'packages/polaris-generation-core/src/prompts.ts': 'promptForStage', 'packages/polaris-generation-core/src/provider-draft.ts': 'stageSchema' },
  ...(DISCOVERY ? { discovery: { authored: discoveryAuthored, classified: discoveryRows } } : {}),
}, null, 2));
