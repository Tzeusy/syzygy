import http from 'node:http';
import { afterEach, describe, expect, it } from 'vitest';
import { assertAllowedUpstream, parseRetryAfterMs, startEgressGate, type EgressGate } from './egress-gate.js';
import { startCaptureEndpoint, type CaptureEndpoint } from './capture-endpoint.testkit.js';

let upstream: CaptureEndpoint | undefined;
let gate: EgressGate | undefined;
afterEach(async () => { await gate?.close(); await upstream?.close(); gate = undefined; upstream = undefined; });

const send = (url: string, method: string, path: string, body = '', extra: Record<string, string> = {}): Promise<{ status: number; text: string }> => new Promise((resolve, reject) => {
  const u = new URL(url);
  const req = http.request({ hostname: u.hostname, port: u.port, method, path, headers: { ...(method === 'HEAD' ? {} : { 'content-type': 'application/json' }), ...extra } }, res => {
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
  it('forwards the SDK platform fingerprint headers unless stripFingerprint is set, and no others are touched', async () => {
    upstream = await startCaptureEndpoint();
    const fingerprint = { 'x-stainless-os': 'Linux', 'x-stainless-arch': 'x64', 'x-stainless-runtime-version': 'v24.0.0', 'x-stainless-lang': 'js' };
    const post = (url: string): Promise<number> => new Promise((resolve, reject) => {
      const u = new URL(url);
      const req = http.request({ hostname: u.hostname, port: u.port, method: 'POST', path: '/v1/messages', headers: { 'content-type': 'application/json', ...fingerprint } }, res => { res.resume(); res.on('end', () => resolve(res.statusCode ?? 0)); });
      req.on('error', reject); req.end('{}');
    });
    for (const strip of [false, true]) {
      gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true, stripFingerprint: strip });
      gate.arm(accepting);
      expect(await post(gate.url)).toBe(200);
      await gate.close(); gate = undefined;
    }
    const [kept, stripped] = upstream.requests;
    for (const name of ['x-stainless-os', 'x-stainless-arch', 'x-stainless-runtime-version']) {
      expect(kept!.headers[name]).toBe(fingerprint[name as keyof typeof fingerprint]);
      expect(stripped!.headers[name]).toBeUndefined();
    }
    expect(stripped!.headers['x-stainless-lang']).toBe('js');
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
  it('listens on 127.0.0.1 only', async () => {
    gate = await startEgressGate({ permitted: async () => true });
    expect(new URL(gate.url).hostname).toBe('127.0.0.1');
    const server = (gate as unknown as { server?: unknown }).server;
    expect(server).toBeUndefined();   // the listener is not exposed; its address is the URL above
    const sockets = await new Promise<string>(resolve => { const s = http.get(gate!.url, r => { resolve(r.socket.remoteAddress ?? ''); r.resume(); }); s.on('error', () => resolve('')); });
    expect(sockets).toBe('127.0.0.1');
  });
  it('forwards exactly one request per armed try, and a later try forwards again', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true });
    gate.arm(accepting);
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(200);
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(403);
    expect(upstream.requests).toHaveLength(1);
    expect(gate.decisions.at(-1)).toMatchObject({ decision: 'refused', reasons: ['try already forwarded one request'] });
    gate.disarm(); gate.arm(accepting);
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(200);
    expect(upstream.requests).toHaveLength(2);
  });
  it('two simultaneous requests in one try forward at most one', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true });
    gate.arm(accepting);
    const results = await Promise.all([send(gate.url, 'POST', '/v1/messages', '{}'), send(gate.url, 'POST', '/v1/messages', '{}')]);
    expect(results.map(r => r.status).sort()).toEqual([200, 403]);
    expect(upstream.requests).toHaveLength(1);
  });
  it('does not forward the gate\'s own Host header', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true });
    gate.arm(accepting);
    await send(gate.url, 'POST', '/v1/messages', '{}');
    expect(upstream.requests[0]!.headers.host).toBe(new URL(upstream.url).host);
    expect(upstream.requests[0]!.headers.host).not.toBe(new URL(gate.url).host);
  });
  it('answers an armed, accepted HEAD /api/hello locally with no upstream hit and does not spend the try', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url }, permitted: async () => true });
    gate.arm(accepting);
    expect((await send(gate.url, 'HEAD', '/api/hello', '', { 'user-agent': 'Bun/1.4.3', accept: '*/*' })).status).toBe(200);
    expect(upstream.requests).toEqual([]);
    expect(gate.decisions.at(-1)).toMatchObject({ decision: 'answered-locally' });
    expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(200);
    expect(upstream.requests).toHaveLength(1);
  });
  it('turns any upstream redirect into a 502 and never follows it', async () => {
    const hits: string[] = [];
    const target = http.createServer((req, res) => { hits.push(req.url ?? ''); res.writeHead(200); res.end('x'); });
    await new Promise<void>(r => target.listen(0, '127.0.0.1', r));
    const targetUrl = `http://127.0.0.1:${(target.address() as { port: number }).port}`;
    const redirector = http.createServer((_req, res) => { res.writeHead(307, { location: `${targetUrl}/elsewhere` }); res.end(); });
    await new Promise<void>(r => redirector.listen(0, '127.0.0.1', r));
    try {
      gate = await startEgressGate({ upstream: { url: `http://127.0.0.1:${(redirector.address() as { port: number }).port}` }, permitted: async () => true });
      gate.arm(accepting);
      const answer = await send(gate.url, 'POST', '/v1/messages', '{}');
      expect(answer.status).toBe(502);
      expect(answer.text).not.toContain('elsewhere');
      expect(hits).toEqual([]);
    } finally { redirector.close(); target.close(); }
  });
  it('accepts only the provider origin or a loopback address as upstream', async () => {
    for (const ok of ['https://api.anthropic.com', 'https://api.anthropic.com/', 'http://127.0.0.1:9', 'http://localhost:9']) expect(() => assertAllowedUpstream(ok), ok).not.toThrow();
    for (const bad of ['http://api.anthropic.com', 'https://api.anthropic.com.evil.test', 'https://evil.test', 'https://user:pw@api.anthropic.com', 'https://api.anthropic.com:8443', 'http://10.0.0.5:80', 'not a url', 'file:///etc/passwd'])
      expect(() => assertAllowedUpstream(bad), bad).toThrow();
    await expect(startEgressGate({ upstream: { url: 'https://evil.test' }, permitted: async () => true })).rejects.toThrow('upstream must be');
  });
  it('parses retry-after seconds and dates, and nothing else', () => {
    expect(parseRetryAfterMs('3', 0)).toBe(3000);
    expect(parseRetryAfterMs(new Date(5000).toUTCString(), 1000)).toBe(4000);
    expect(parseRetryAfterMs('soon', 0)).toBeNull();
    expect(parseRetryAfterMs(undefined, 0)).toBeNull();
    expect(parseRetryAfterMs('-1', 0)).toBeNull();
  });
});
