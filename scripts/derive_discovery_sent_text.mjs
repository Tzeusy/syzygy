#!/usr/bin/env node
// Derives what a discovery map or reduce call sends, field by field, from the
// real envelope builders (packages/polaris-generation-core/src/discovery-provider.ts),
// and gives every leaf one closed class. Companion to
// scripts/derive_generator_sent_text.mjs (#215), which runs the six-stage
// pipeline and so never sees discovery calls; the class names are that
// script's. An unclassified leaf exits 2. Build the core package first.
//
//   node scripts/derive_discovery_sent_text.mjs [--table]

import { createHash } from 'node:crypto';
import { discoveryMapEnvelope, discoveryReduceEnvelope } from '../packages/polaris-generation-core/dist/index.js';

const sha = text => createHash('sha256').update(text).digest('hex');

// Fixture requests with every field populated; no target content.
const map = discoveryMapEnvelope({ subsystem: 'derive', readerQuestions: ['q'],
  items: [{ blobId: 'b1', path: 'derive/a.md', excerpt: 'fixture excerpt' }, { blobId: 'b2', path: 'derive/b.md', excerpt: 'fixture excerpt' }] });
const reduce = discoveryReduceEnvelope({ readerQuestions: ['q'], maxSelected: 2,
  subsystems: [{ subsystem: 'derive', blobs: 2, claims: [{ blobId: 'b1', path: 'derive/a.md', claim: 'fixture claim', relevance: 5 }] }] });

// Leaf paths, array indices collapsed to [].
const leaves = (value, path = '') => Array.isArray(value)
  ? value.flatMap(item => leaves(item, `${path}[]`))
  : value !== null && typeof value === 'object'
    ? Object.entries(value).flatMap(([key, child]) => leaves(child, path ? `${path}.${key}` : key))
    : [path];

// Classes: target-content (body text under an observation consent),
// target-metadata (ids, paths, counts; no body), composite (model output
// computed from target content), instruction-text (generator-authored prompt
// and schema text), envelope-control (version labels and budget numbers),
// run-profile (reader questions).
const CLASS = [
  [/^promptVersion$/u, 'envelope-control'],
  [/^system$/u, 'instruction-text'],
  [/^responseSchemaVersion$/u, 'envelope-control'],
  // The per-call schema closes over the request's blob ids and counts.
  [/^responseSchema\..*\.enum\[\]$/u, 'target-metadata'],
  [/^responseSchema\..*\.maxItems$/u, 'target-metadata'],
  [/^responseSchema\./u, 'instruction-text'],
  [/^inputs\.readerQuestions\[\]$/u, 'run-profile'],
  [/^inputs\.maxSelected$/u, 'envelope-control'],
  [/^inputs\.subsystem$/u, 'target-metadata'],
  [/^inputs\.items\[\]\.(blobId|path)$/u, 'target-metadata'],
  [/^inputs\.items\[\]\.excerpt$/u, 'target-content'],
  [/^inputs\.subsystems\[\]\.(subsystem|blobs)$/u, 'target-metadata'],
  [/^inputs\.subsystems\[\]\.claims\[\]\.(blobId|path)$/u, 'target-metadata'],
  [/^inputs\.subsystems\[\]\.claims\[\]\.(claim|relevance)$/u, 'composite'],
];
const failures = [];
const rows = [];
for (const [call, built] of [['map', map], ['reduce', reduce]]) {
  for (const path of [...new Set(leaves(built.envelope))].sort()) {
    const cls = CLASS.find(([pattern]) => pattern.test(path))?.[1];
    if (cls === undefined) failures.push(`${call}: ${path} has no class`);
    rows.push({ call, field: path, cls: cls ?? 'UNCLASSIFIED' });
  }
}
if (failures.length) { console.error('UNCLASSIFIED:\n' + failures.join('\n')); process.exit(2); }

if (process.argv.includes('--table')) {
  console.log(['| Call | Field | Class |', '|---|---|---|', ...rows.map(r => `| ${r.call} | \`${r.field}\` | ${r.cls} |`)].join('\n'));
  process.exit(0);
}
console.log(JSON.stringify({
  envelopeKeys: Object.keys(map.envelope).sort(),
  authored: [map, reduce].map(({ envelope }) => ({ promptVersion: envelope.promptVersion, systemBytes: Buffer.byteLength(envelope.system), systemSha256: sha(envelope.system),
    responseSchemaVersion: envelope.responseSchemaVersion, note: 'responseSchema is computed per call; its enum and maxItems carry target metadata' })),
  classified: rows,
  authoredBySource: { 'packages/polaris-generation-core/src/discovery-provider.ts': 'discoveryMapEnvelope, discoveryReduceEnvelope' },
}, null, 2));
