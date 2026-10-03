import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import {
  discoveryMapEnvelope, discoveryReduceEnvelope, parseDiscoveryMapReply, parseDiscoveryReduceReply,
  type DiscoveryMapRequest, type DiscoveryReduceRequest,
} from './discovery-provider.js';
import { DISCOVERY_STAGE_ILLUSTRATIONS, promptForStage } from './prompts.js';
import { stageSchema, validateDiscoveryReply } from './provider-draft.js';

const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

// The fictional files the illustrations name; no target content.
const mapRequest = (): DiscoveryMapRequest => ({
  subsystem: 'src', readerQuestions: ['What are the core ideas?', 'What trade-offs does the design accept?'],
  items: [
    { blobId: 'blob-readme', path: 'README.md', excerpt: 'Brindle builds documentation sites from Markdown.' },
    { blobId: 'blob-build', path: 'src/build.ts', excerpt: 'buildSite reads the content directory.' },
    { blobId: 'blob-cache', path: 'src/cache.ts', excerpt: 'renderPage skips unchanged pages.' },
  ],
});
const reduceRequest = (): DiscoveryReduceRequest => ({
  readerQuestions: ['What are the core ideas?'], maxSelected: 3,
  subsystems: [
    { subsystem: '.', blobs: 4, claims: [{ blobId: 'blob-readme', path: 'README.md', claim: 'States the purpose.', relevance: 9 }] },
    { subsystem: 'src', blobs: 7, claims: [
      { blobId: 'blob-build', path: 'src/build.ts', claim: 'Shows the build entry point.', relevance: 8 },
      { blobId: 'blob-cache', path: 'src/cache.ts', claim: 'Shows the render cache.', relevance: 7 },
    ] },
  ],
});
const json = (value: unknown): string => JSON.stringify(value);
const claim = (blobId: string, relevance = 5, text = 'Shows something.') => ({ blobId, claim: text, relevance });

const MAP_SYSTEM = promptForStage('discovery-map').system;
const REDUCE_SYSTEM = promptForStage('discovery-reduce').system;

describe('discovery instruction text comes from promptForStage and stageSchema', () => {
  // Recipe replay: an intentional edit needs a version decision and a new digest.
  it.each([
    ['discovery-map', 'polaris-discovery-map-v2', '1485dd779fff5fd45ed34bde2725e17481cae823c9b6366349a3f311a62b59e6'],
    ['discovery-reduce', 'polaris-discovery-reduce-v2', '487a8d380c3e023ecda98f15fa99fd4620f0dd95588f8336af2868412b6b5e23'],
  ] as const)('pins the %s prompt bytes', (stage, version, digest) => {
    const prompt = promptForStage(stage);
    expect(prompt.version).toBe(version);
    expect(sha256(prompt.system)).toBe(digest);
    expect(Buffer.byteLength(prompt.system, 'utf8')).toBeLessThan(4096);
    expect(promptForStage(stage, 'dossier')).toEqual(prompt);
  });

  it.each([
    ['discovery-map', 'polaris-provider-discovery-map-v1', 'cf4dd39aa3eb3c1bc3805f4de902c8e679cb8956f74d853ee80ab599496ed894'],
    ['discovery-reduce', 'polaris-provider-discovery-reduce-v1', 'fd1deb4230c7892e05a05dfe07f5cc6221f817fe46142541d57f1783c321a14d'],
  ] as const)('pins the %s reply schema bytes', (stage, version, digest) => {
    const schema = stageSchema(stage);
    expect(schema.version).toBe(version);
    expect(sha256(JSON.stringify(schema.schema))).toBe(digest);
  });

  it('closes the map reply schema: exactly claims of blobId, claim (1..400) and relevance (0..10)', () => {
    expect(stageSchema('discovery-map').schema).toEqual({ type: 'object', additionalProperties: false, required: ['claims'], properties: {
      claims: { type: 'array', minItems: 0, maxItems: 200, items: { type: 'object', additionalProperties: false, required: ['blobId', 'claim', 'relevance'], properties: {
        blobId: { type: 'string', minLength: 1, maxLength: 100, pattern: '^[A-Za-z0-9][A-Za-z0-9_.:-]*$' },
        claim: { type: 'string', minLength: 1, maxLength: 400 },
        relevance: { type: 'number', minimum: 0, maximum: 10 },
      } } } } });
  });

  it('closes the reduce reply schema: exactly a unique ranked list of handles', () => {
    expect(stageSchema('discovery-reduce').schema).toEqual({ type: 'object', additionalProperties: false, required: ['ranked'], properties: {
      ranked: { type: 'array', minItems: 0, maxItems: 200, uniqueItems: true, items: { type: 'string', minLength: 1, maxLength: 100, pattern: '^[A-Za-z0-9][A-Za-z0-9_.:-]*$' } } } });
  });

  it('sends exactly those two symbols\' output as the instruction text, whatever the request', () => {
    const other: DiscoveryMapRequest = { subsystem: 'elsewhere', readerQuestions: ['other'], items: [{ blobId: 'zzz', path: 'z', excerpt: 'z' }] };
    for (const request of [mapRequest(), other]) {
      const { envelope } = discoveryMapEnvelope(request);
      expect(envelope.system).toBe(promptForStage('discovery-map').system);
      expect(envelope.promptVersion).toBe(promptForStage('discovery-map').version);
      expect(envelope.responseSchema).toEqual(stageSchema('discovery-map').schema);
      expect(envelope.responseSchemaVersion).toBe(stageSchema('discovery-map').version);
    }
    const { envelope } = discoveryReduceEnvelope(reduceRequest());
    expect(envelope.system).toBe(promptForStage('discovery-reduce').system);
    expect(envelope.responseSchema).toEqual(stageSchema('discovery-reduce').schema);
  });

  it('ends each prompt with an illustration its own parser accepts', () => {
    const mapTail = MAP_SYSTEM.split('\n').at(-1)!;
    const reduceTail = REDUCE_SYSTEM.split('\n').at(-1)!;
    expect(JSON.parse(mapTail)).toEqual(DISCOVERY_STAGE_ILLUSTRATIONS['discovery-map']);
    expect(JSON.parse(reduceTail)).toEqual(DISCOVERY_STAGE_ILLUSTRATIONS['discovery-reduce']);
    expect(parseDiscoveryMapReply(mapRequest(), mapTail)).toEqual(DISCOVERY_STAGE_ILLUSTRATIONS['discovery-map']);
    expect(parseDiscoveryReduceReply(reduceRequest(), reduceTail)).toEqual(DISCOVERY_STAGE_ILLUSTRATIONS['discovery-reduce']);
  });

  // JSON cannot carry these, but validateDiscoveryReply is exported and takes a value.
  it.each([Number.NaN, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY])('refuses a relevance of %s in validateDiscoveryReply', (relevance) => {
    expect(() => validateDiscoveryReply('discovery-map', { claims: [{ blobId: 'blob-readme', claim: 'x', relevance }] }, { candidateIds: ['blob-readme'] })).toThrow('invalid-number');
  });

  it('refuses a generation-stage name in validateDiscoveryReply', () => {
    expect(() => validateDiscoveryReply('author' as 'discovery-map', { claims: [] }, { candidateIds: [] })).toThrow('invalid-stage');
  });
});

describe('discovery envelopes', () => {
  it('builds the map envelope with the stage envelope fields and the request rebuilt field by field', () => {
    const request = { ...mapRequest(), extra: 'never sent', items: mapRequest().items.map(item => ({ ...item, mode: '100644' })) };
    const { envelope, input } = discoveryMapEnvelope(request);
    expect(Object.keys(envelope).sort()).toEqual(['inputs', 'promptVersion', 'responseSchema', 'responseSchemaVersion', 'system']);
    expect(envelope.promptVersion).toBe('polaris-discovery-map-v2');
    expect(envelope.responseSchemaVersion).toBe('polaris-provider-discovery-map-v1');
    expect(envelope.system).toBe(MAP_SYSTEM);
    expect(envelope.inputs).toEqual(mapRequest());
    expect(JSON.parse(input)).toEqual(envelope);
    expect(input).not.toContain('never sent');
    expect(input).not.toContain('100644');
  });

  it('builds the reduce envelope the same way', () => {
    const request = { ...reduceRequest(), extra: 'never sent', subsystems: reduceRequest().subsystems.map(entry => ({
      ...entry, owner: 'entry extra', claims: entry.claims.map(claim => ({ ...claim, mode: '100644' })) })) };
    const { envelope, input } = discoveryReduceEnvelope(request);
    expect(envelope.promptVersion).toBe('polaris-discovery-reduce-v2');
    expect(envelope.responseSchemaVersion).toBe('polaris-provider-discovery-reduce-v1');
    expect(envelope.system).toBe(REDUCE_SYSTEM);
    expect(envelope.inputs).toEqual(reduceRequest());
    expect(JSON.parse(input)).toEqual(envelope);
    expect(input).not.toContain('never sent');
    expect(input).not.toContain('entry extra');
    expect(input).not.toContain('100644');
  });

  // The whole user message, schema included, for the fixtures above.
  it.each([
    ['map', () => discoveryMapEnvelope(mapRequest()).input, '191c12071085dd577f3b96af7d7b8cf91b43e3116122778df1aade1b940a28ea'],
    ['reduce', () => discoveryReduceEnvelope(reduceRequest()).input, 'f938ed16e4e893636b85fcde7242fe37d454263b86a56b0a551d7ce1b8426493'],
  ])('pins the %s envelope encoding', (_step, encode, digest) => {
    expect(sha256(encode())).toBe(digest);
  });

  it.each([
    ['duplicate item ids', { ...mapRequest(), items: [mapRequest().items[0]!, mapRequest().items[0]!] }],
    ['no items', { ...mapRequest(), items: [] }],
    ['no reader questions', { ...mapRequest(), readerQuestions: [] }],
    ['an empty subsystem name', { ...mapRequest(), subsystem: '' }],
    ['an item without a path', { ...mapRequest(), items: [{ blobId: 'blob-readme', excerpt: 'x' }] }],
  ])('refuses a map request with %s', (_name, request) => {
    expect(() => discoveryMapEnvelope(request as DiscoveryMapRequest)).toThrow('invalid-map-request');
  });

  it.each([
    ['maxSelected 0', { ...reduceRequest(), maxSelected: 0 }],
    ['a fractional maxSelected', { ...reduceRequest(), maxSelected: 1.5 }],
    ['no claims', { ...reduceRequest(), subsystems: [{ subsystem: 'src', blobs: 3, claims: [] }] }],
    ['a blob claimed twice', { ...reduceRequest(), subsystems: [...reduceRequest().subsystems, reduceRequest().subsystems[0]!] }],
    ['a non-finite relevance', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: 'c', relevance: Number.NaN }] }] }],
    ['an infinite relevance', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: 'c', relevance: Number.POSITIVE_INFINITY }] }] }],
    ['a string relevance', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: 'c', relevance: '5' }] }] }],
    ['a relevance below 0', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: 'c', relevance: -0.5 }] }] }],
    ['a relevance above 10', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: 'c', relevance: 10.5 }] }] }],
    ['an empty claim', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: '', relevance: 5 }] }] }],
    ['a claim of 401 code points', { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 1, claims: [{ blobId: 'b', path: 'p', claim: 'a'.repeat(401), relevance: 5 }] }] }],
  ])('refuses a reduce request with %s', (_name, request) => {
    expect(() => discoveryReduceEnvelope(request as DiscoveryReduceRequest)).toThrow('invalid-reduce-request');
    expect(() => parseDiscoveryReduceReply(request as DiscoveryReduceRequest, json({ ranked: [] }))).toThrow('invalid-reduce-request');
  });

  it('accepts reduce claims at the map reply bounds, counted in code points', () => {
    const request = { ...reduceRequest(), subsystems: [{ subsystem: 'x', blobs: 2, claims: [
      { blobId: 'b0', path: 'p0', claim: '\u{1F600}'.repeat(400), relevance: 0 },
      { blobId: 'b10', path: 'p10', claim: 'c', relevance: 10 },
    ] }] };
    expect(discoveryReduceEnvelope(request).envelope.inputs).toEqual({ readerQuestions: request.readerQuestions, maxSelected: 3, subsystems: request.subsystems });
  });

  // A request field is read once: a getter cannot pass validation with one
  // value and be encoded or bound to the reply with another.
  const counting = <T extends object>(base: T, key: keyof T, values: unknown[]): { request: T; reads: () => number } => {
    let reads = 0;
    const request = { ...base };
    Object.defineProperty(request, key, { enumerable: true, get: () => values[Math.min(reads++, values.length - 1)] });
    return { request, reads: () => reads };
  };

  it('reads each map request field once and encodes what it validated', () => {
    const good = mapRequest().items;
    const { request, reads } = counting(mapRequest(), 'items', [good, [{ blobId: 'blob-other', path: 'x', excerpt: 'swapped' }]]);
    expect(discoveryMapEnvelope(request).envelope.inputs.items).toEqual(good);
    expect(reads()).toBe(1);
    const item = counting(good[0]!, 'excerpt', ['first', 'second']);
    expect(discoveryMapEnvelope({ ...mapRequest(), items: [item.request] }).envelope.inputs.items).toEqual([{ ...good[0], excerpt: 'first' }]);
    expect(item.reads()).toBe(1);
  });

  it('reads each reduce request field once and binds the reply to what it validated', () => {
    const { request, reads } = counting(reduceRequest(), 'maxSelected', [1, 3]);
    expect(() => parseDiscoveryReduceReply(request, json({ ranked: ['blob-readme', 'blob-build'] }))).toThrow('invalid-reduce-reply');
    expect(reads()).toBe(1);
    const relevance = counting(reduceRequest().subsystems[0]!.claims[0]!, 'relevance', [9, 99]);
    const subsystems = [{ ...reduceRequest().subsystems[0]!, claims: [relevance.request] }];
    expect(discoveryReduceEnvelope({ ...reduceRequest(), subsystems }).envelope.inputs.subsystems).toEqual([{ ...subsystems[0], claims: [{ ...reduceRequest().subsystems[0]!.claims[0]!, relevance: 9 }] }]);
    expect(relevance.reads()).toBe(1);
  });
});

describe('discovery reply parsers', () => {
  it('accepts a map reply naming only the request\'s blob ids, including no claims at all', () => {
    expect(parseDiscoveryMapReply(mapRequest(), json({ claims: [claim('blob-cache', 0), claim('blob-readme', 10)] })).claims.map(c => c.blobId)).toEqual(['blob-cache', 'blob-readme']);
    expect(parseDiscoveryMapReply(mapRequest(), json({ claims: [] }))).toEqual({ claims: [] });
  });

  it('counts a claim\'s length in code points, as discovery truncates it', () => {
    const astral = '\u{1F600}'.repeat(400);
    expect(parseDiscoveryMapReply(mapRequest(), json({ claims: [claim('blob-readme', 5, astral)] })).claims[0]!.claim).toBe(astral);
    expect(() => parseDiscoveryMapReply(mapRequest(), json({ claims: [claim('blob-readme', 5, `${astral}x`)] }))).toThrow('invalid-map-reply');
  });

  it.each([
    ['a blob id outside the request', json({ claims: [claim('blob-other')] })],
    ['a repeated blob id', json({ claims: [claim('blob-readme'), claim('blob-readme', 6)] })],
    ['more claims than items', json({ claims: [claim('blob-readme'), claim('blob-build'), claim('blob-cache'), claim('blob-readme')] })],
    ['relevance above 10', json({ claims: [claim('blob-readme', 10.5)] })],
    ['relevance below 0', json({ claims: [claim('blob-readme', -1)] })],
    ['a string relevance', json({ claims: [{ blobId: 'blob-readme', claim: 'x', relevance: '5' }] })],
    ['an empty claim', json({ claims: [claim('blob-readme', 5, '')] })],
    ['an extra claim field', json({ claims: [{ ...claim('blob-readme'), path: 'README.md' }] })],
    ['a missing claim field', json({ claims: [{ blobId: 'blob-readme', claim: 'x' }] })],
    ['an extra top-level field', json({ claims: [], usageUnits: 3 })],
    ['claims that are not an array', json({ claims: {} })],
    ['a top-level array', json([claim('blob-readme')])],
    ['a fenced body', `\`\`\`json\n${json({ claims: [] })}\n\`\`\``],
    ['prose around the JSON', `Here you go: ${json({ claims: [] })}`],
  ])('refuses a map reply with %s', (_name, body) => {
    expect(() => parseDiscoveryMapReply(mapRequest(), body)).toThrow('invalid-map-reply');
  });

  it('accepts a reduce reply ranking claimed blob ids, up to maxSelected', () => {
    expect(parseDiscoveryReduceReply(reduceRequest(), json({ ranked: ['blob-cache', 'blob-readme'] }))).toEqual({ ranked: ['blob-cache', 'blob-readme'] });
    expect(parseDiscoveryReduceReply(reduceRequest(), json({ ranked: [] }))).toEqual({ ranked: [] });
  });

  it.each([
    ['an id no claim names', json({ ranked: ['blob-unclaimed'] })],
    ['a repeated id', json({ ranked: ['blob-readme', 'blob-readme'] })],
    ['more than maxSelected', json({ ranked: ['blob-readme', 'blob-build', 'blob-cache'] }), 2],
    ['a non-string id', json({ ranked: [7] })],
    ['an extra field', json({ ranked: [], reason: 'x' })],
    ['ranked that is not an array', json({ ranked: 'blob-readme' })],
  ])('refuses a reduce reply with %s', (_name, body, maxSelected = 3) => {
    expect(() => parseDiscoveryReduceReply({ ...reduceRequest(), maxSelected }, body)).toThrow('invalid-reduce-reply');
  });
});
