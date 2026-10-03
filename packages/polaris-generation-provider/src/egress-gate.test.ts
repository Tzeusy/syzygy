import http from 'node:http';
import { afterEach, describe, expect, it } from 'vitest';
import { parseRetryAfterMs, startEgressGate, type EgressGate } from './egress-gate.js';
import { startCaptureEndpoint, type CaptureEndpoint } from './capture-endpoint.testkit.js';

let upstream: CaptureEndpoint | undefined;
let gate: EgressGate | undefined;
afterEach(async () => { await gate?.close(); await upstream?.close(); gate = undefined; upstream = undefined; });

const send = (url: string, method: string, path: string, body = ''): Promise<{ status: number; text: string }> => new Promise((resolve, reject) => {
  const u = new URL(url);
  const req = http.request({ hostname: u.hostname, port: u.port, method, path, headers: { 'content-type': 'application/json' } }, res => {
    const chunks: Buffer[] = [];
    res.on('data', c => chunks.push(c as Buffer));
    res.on('end', () => resolve({ status: res.statusCode ?? 0, text: Buffer.concat(chunks).toString('utf8') }));
  });
  req.on('error', reject);
  req.end(body);
});
const accepting = () => ({ accepted: true, violations: [] as string[] });

describe('egress gate', () => {
  it('forwards only an armed, accepted, permitted request to the configured upstream', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true });
    // unarmed
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(403);
    expect(upstream.requests).toEqual([]);
    // armed with a predicate that rejects
    gate.arm(() => ({ accepted: false, violations: ['unlisted body field tools'] }));
    expect((await send(gate.url, 'POST', '/v1/messages', '{"tools":[]}')).status).toBe(403);
    expect(upstream.requests).toEqual([]);
    expect(gate.decisions.at(-1)).toMatchObject({ decision: 'refused', reasons: ['unlisted body field tools'] });
    // a throwing predicate refuses
    gate.disarm(); gate.arm(() => { throw new Error('boom'); });
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(403);
    // accepted
    gate.disarm(); gate.arm(accepting);
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(200);
    expect(upstream.requests).toHaveLength(1);
    expect(gate.arm(accepting)).toBe(false);   // one try at a time
  });
  it('refuses when consent is anything but true, throws, or no upstream is configured', async () => {
    upstream = await startCaptureEndpoint();
    for (const permitted of [async () => false, async () => 1 as unknown as boolean, async () => { throw new Error('x'); }]) {
      gate = await startEgressGate({ upstream: { url: upstream.url }, permitted });
      gate.arm(accepting);
      expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(403);
      await gate.close();
    }
    gate = await startEgressGate({ permitted: async () => true });
    gate.arm(accepting);
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(403);
    expect(upstream.requests).toEqual([]);
  });
  it('answers HEAD /api/hello itself, only while armed, and only with the probe shape', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true });
    expect((await send(gate.url, 'HEAD', '/api/hello')).status).toBe(403);
    gate.arm(c => ({ accepted: c.method === 'POST', violations: ['not a message request'] }));
    expect((await send(gate.url, 'HEAD', '/other')).status).toBe(403);
    expect(upstream.requests).toEqual([]);
  });
  it('parses retry-after seconds and dates, and nothing else', () => {
    expect(parseRetryAfterMs('3', 0)).toBe(3000);
    expect(parseRetryAfterMs(new Date(5000).toUTCString(), 1000)).toBe(4000);
    expect(parseRetryAfterMs('soon', 0)).toBeNull();
    expect(parseRetryAfterMs(undefined, 0)).toBeNull();
    expect(parseRetryAfterMs('-1', 0)).toBeNull();
  });
});
