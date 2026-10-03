import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import {
  DISCOVERY_MAP_ILLUSTRATION, DISCOVERY_MAP_SYSTEM, DISCOVERY_REDUCE_ILLUSTRATION, DISCOVERY_REDUCE_SYSTEM,
  discoveryMapEnvelope, discoveryMapReplySchema, discoveryReduceEnvelope, discoveryReduceReplySchema,
  parseDiscoveryMapReply, parseDiscoveryReduceReply, type DiscoveryMapRequest, type DiscoveryReduceRequest,
} from './discovery-provider.js';

const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

// The fictional files the illustrations name; no target content.
const mapRequest = (): DiscoveryMapRequest => ({
  subsystem: 'src', readerQuestions: ['What are the core ideas?', 'What trade-offs does the design accept?'],
  items: [
    { blobId: 'blob-readme', path: 'README.md', excerpt: 'Tidemark is an in-memory cache for session data.' },
    { blobId: 'blob-server', path: 'src/server.c', excerpt: 'handleSet parses the SET command.' },
    { blobId: 'blob-evict', path: 'src/evict.c', excerpt: 'maybeEvict samples 5 keys.' },
  ],
});
const reduceRequest = (): DiscoveryReduceRequest => ({
  readerQuestions: ['What are the core ideas?'], maxSelected: 3,
  subsystems: [
    { subsystem: '.', blobs: 4, claims: [{ blobId: 'blob-readme', path: 'README.md', claim: 'States the purpose.', relevance: 9 }] },
    { subsystem: 'src', blobs: 7, claims: [
      { blobId: 'blob-server', path: 'src/server.c', claim: 'Shows the SET entry point.', relevance: 8 },
      { blobId: 'blob-evict', path: 'src/evict.c', claim: 'Shows sampled eviction.', relevance: 7 },
    ] },
  ],
});
interface MapReplySchema {
  additionalProperties: boolean;
  properties: { claims: { maxItems: number; items: { additionalProperties: boolean; required: string[]; properties: { blobId: { enum: string[] }; claim: unknown; relevance: unknown } } } };
}
interface ReduceReplySchema { additionalProperties: boolean; required: string[]; properties: { ranked: { maxItems: number } } }
const json = (value: unknown): string => JSON.stringify(value);
const claim = (blobId: string, relevance = 5, text = 'Shows something.') => ({ blobId, claim: text, relevance });

describe('discovery instruction text', () => {
  // Recipe replay: an intentional edit needs a version decision and a new digest.
  it.each([
    ['map', DISCOVERY_MAP_SYSTEM, 'b522e91ae2c99e659d1f9e39114698f5b0c2ae98e2fdffd473cb78638620dcef'],
    ['reduce', DISCOVERY_REDUCE_SYSTEM, '300cf688c755779ab28cdcbaf4a9cd7ed0fba0831483145ce3a54fb9c1169da3'],
  ])('pins the %s prompt bytes', (_step, system, digest) => {
    expect(sha256(system)).toBe(digest);
    expect(Buffer.byteLength(system, 'utf8')).toBeLessThan(4096);
  });

  it('ends each prompt with an illustration its own parser accepts', () => {
    const mapTail = DISCOVERY_MAP_SYSTEM.split('\n').at(-1)!;
    const reduceTail = DISCOVERY_REDUCE_SYSTEM.split('\n').at(-1)!;
    expect(JSON.parse(mapTail)).toEqual(DISCOVERY_MAP_ILLUSTRATION);
    expect(JSON.parse(reduceTail)).toEqual(DISCOVERY_REDUCE_ILLUSTRATION);
    expect(parseDiscoveryMapReply(mapRequest(), mapTail)).toEqual(DISCOVERY_MAP_ILLUSTRATION);
    expect(parseDiscoveryReduceReply(reduceRequest(), reduceTail)).toEqual(DISCOVERY_REDUCE_ILLUSTRATION);
  });
});

describe('discovery envelopes', () => {
  it('builds the map envelope with the stage envelope fields and the request rebuilt field by field', () => {
    const request = { ...mapRequest(), extra: 'never sent', items: mapRequest().items.map(item => ({ ...item, mode: '100644' })) };
    const { envelope, input } = discoveryMapEnvelope(request);
    expect(Object.keys(envelope).sort()).toEqual(['inputs', 'promptVersion', 'responseSchema', 'responseSchemaVersion', 'system']);
    expect(envelope.promptVersion).toBe('polaris-discovery-map-v1');
    expect(envelope.responseSchemaVersion).toBe('polaris-discovery-map-reply-v1');
    expect(envelope.system).toBe(DISCOVERY_MAP_SYSTEM);
    expect(envelope.inputs).toEqual(mapRequest());
    expect(JSON.parse(input)).toEqual(envelope);
    expect(input).not.toContain('never sent');
    expect(input).not.toContain('100644');
  });

  it('builds the reduce envelope the same way', () => {
    const request = { ...reduceRequest(), extra: 'never sent' };
    const { envelope, input } = discoveryReduceEnvelope(request);
    expect(envelope.promptVersion).toBe('polaris-discovery-reduce-v1');
    expect(envelope.responseSchemaVersion).toBe('polaris-discovery-reduce-reply-v1');
    expect(envelope.system).toBe(DISCOVERY_REDUCE_SYSTEM);
    expect(envelope.inputs).toEqual(reduceRequest());
    expect(JSON.parse(input)).toEqual(envelope);
    expect(input).not.toContain('never sent');
  });

  // The whole user message, schema included, for the fixtures above.
  it.each([
    ['map', () => discoveryMapEnvelope(mapRequest()).input, '6ba8c20b41937aac5bf5f725ea6ad1dcaf0e3ef6b3840def48f9a1a941aa3a44'],
    ['reduce', () => discoveryReduceEnvelope(reduceRequest()).input, 'a30543e18dae2ccb683a8d2c54b269c8875036f9b9595d680b96e773f2dec95a'],
  ])('pins the %s envelope encoding', (_step, encode, digest) => {
    expect(sha256(encode())).toBe(digest);
  });

  it('closes the map reply schema over the request\'s own blob ids', () => {
    const schema = discoveryMapReplySchema(mapRequest()) as unknown as MapReplySchema;
    expect(schema.additionalProperties).toBe(false);
    expect(schema.properties.claims.maxItems).toBe(3);
    const item = schema.properties.claims.items;
    expect(item.additionalProperties).toBe(false);
    expect(item.required).toEqual(['blobId', 'claim', 'relevance']);
    expect(item.properties.blobId.enum).toEqual(['blob-readme', 'blob-server', 'blob-evict']);
    expect(item.properties.claim).toEqual({ type: 'string', minLength: 1, maxLength: 400 });
    expect(item.properties.relevance).toEqual({ type: 'number', minimum: 0, maximum: 10 });
  });

  it('closes the reduce reply schema over the claims\' blob ids and maxSelected', () => {
    const schema = discoveryReduceReplySchema({ ...reduceRequest(), maxSelected: 2 }) as unknown as ReduceReplySchema;
    expect(schema.additionalProperties).toBe(false);
    expect(schema.required).toEqual(['ranked']);
    expect(schema.properties.ranked).toEqual({ type: 'array', uniqueItems: true, maxItems: 2, items: { type: 'string', enum: ['blob-readme', 'blob-server', 'blob-evict'] } });
    expect((discoveryReduceReplySchema({ ...reduceRequest(), maxSelected: 50 }) as unknown as ReduceReplySchema).properties.ranked.maxItems).toBe(3);
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
  ])('refuses a reduce request with %s', (_name, request) => {
    expect(() => discoveryReduceEnvelope(request as DiscoveryReduceRequest)).toThrow('invalid-reduce-request');
  });
});

describe('discovery reply parsers', () => {
  it('accepts a map reply naming only the request\'s blob ids, including no claims at all', () => {
    expect(parseDiscoveryMapReply(mapRequest(), json({ claims: [claim('blob-evict', 0), claim('blob-readme', 10)] })).claims.map(c => c.blobId)).toEqual(['blob-evict', 'blob-readme']);
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
    ['more claims than items', json({ claims: [claim('blob-readme'), claim('blob-server'), claim('blob-evict'), claim('blob-readme')] })],
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
    expect(parseDiscoveryReduceReply(reduceRequest(), json({ ranked: ['blob-evict', 'blob-readme'] }))).toEqual({ ranked: ['blob-evict', 'blob-readme'] });
    expect(parseDiscoveryReduceReply(reduceRequest(), json({ ranked: [] }))).toEqual({ ranked: [] });
  });

  it.each([
    ['an id no claim names', json({ ranked: ['blob-unclaimed'] })],
    ['a repeated id', json({ ranked: ['blob-readme', 'blob-readme'] })],
    ['more than maxSelected', json({ ranked: ['blob-readme', 'blob-server', 'blob-evict'] }), 2],
    ['a non-string id', json({ ranked: [7] })],
    ['an extra field', json({ ranked: [], reason: 'x' })],
    ['ranked that is not an array', json({ ranked: 'blob-readme' })],
  ])('refuses a reduce reply with %s', (_name, body, maxSelected = 3) => {
    expect(() => parseDiscoveryReduceReply({ ...reduceRequest(), maxSelected }, body)).toThrow('invalid-reduce-reply');
  });
});
