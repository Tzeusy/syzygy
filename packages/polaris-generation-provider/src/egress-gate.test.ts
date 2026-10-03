import { execFileSync } from 'node:child_process';
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync, statSync } from 'node:fs';
import http from 'node:http';
import https from 'node:https';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, describe, expect, it } from 'vitest';
import { LOOPBACK_FOR_TESTS, assertAllowedUpstream, parseRetryAfterMs, startEgressGate, type EgressGate } from './egress-gate.js';
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
/** A module specifier that names the gate file itself (any directory, src or dist, any extension), statically or dynamically. */
const importsGateByPath = (text: string): boolean =>
  /(?:\bfrom\s*|\bimport\s*\(\s*|\brequire\s*\(\s*)['"][^'"]*\begress-gate(?:\.[cm]?[jt]s)?['"]/u.test(text);

describe('egress gate', () => {
  it('forwards only an armed, accepted, permitted request to the configured upstream', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
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
      gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true, stripFingerprint: strip });
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
      gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted });
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
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
    expect((await send(gate.url, 'HEAD', '/api/hello')).status).toBe(403);
    gate.arm(c => ({ accepted: c.method === 'POST', violations: ['not a message request'] }));
    expect((await send(gate.url, 'HEAD', '/other')).status).toBe(403);
    expect(upstream.requests).toEqual([]);
  });
  it('listens on 127.0.0.1 only', async () => {
    gate = await startEgressGate({ permitted: async () => true });
    expect(gate.boundAddress).toBe('127.0.0.1');
    expect(new URL(gate.url).hostname).toBe('127.0.0.1');
  });
  it('forwards exactly one request per armed try, and a later try forwards again', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
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
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
    gate.arm(accepting);
    const results = await Promise.all([send(gate.url, 'POST', '/v1/messages', '{}'), send(gate.url, 'POST', '/v1/messages', '{}')]);
    expect(results.map(r => r.status).sort()).toEqual([200, 403]);
    expect(upstream.requests).toHaveLength(1);
  });
  it('does not forward the gate\'s own Host header', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
    gate.arm(accepting);
    await send(gate.url, 'POST', '/v1/messages', '{}');
    expect(upstream.requests[0]!.headers.host).toBe(new URL(upstream.url).host);
    expect(upstream.requests[0]!.headers.host).not.toBe(new URL(gate.url).host);
  });
  it('answers an armed, accepted HEAD /api/hello locally with no upstream hit and does not spend the try', async () => {
    upstream = await startCaptureEndpoint();
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
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
      gate = await startEgressGate({ upstream: { url: `http://127.0.0.1:${(redirector.address() as { port: number }).port}`, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
      gate.arm(accepting);
      const answer = await send(gate.url, 'POST', '/v1/messages', '{}');
      expect(answer.status).toBe(502);
      expect(answer.text).not.toContain('elsewhere');
      expect(hits).toEqual([]);
    } finally { redirector.close(); target.close(); }
  });
  it('accepts only the provider origin as upstream; loopback only with the test-only token', async () => {
    for (const ok of ['https://api.anthropic.com', 'https://api.anthropic.com/']) expect(() => assertAllowedUpstream(ok), ok).not.toThrow();
    for (const local of ['http://127.0.0.1:9', 'http://localhost:9']) {
      expect(() => assertAllowedUpstream(local), local).toThrow();
      expect(() => assertAllowedUpstream(local, LOOPBACK_FOR_TESTS), local).not.toThrow();
    }
    for (const bad of ['http://api.anthropic.com', 'https://api.anthropic.com.evil.test', 'https://evil.test', 'https://user:pw@api.anthropic.com', 'https://api.anthropic.com:8443', 'http://10.0.0.5:80', 'not a url', 'file:///etc/passwd']) {
      expect(() => assertAllowedUpstream(bad), bad).toThrow();
      expect(() => assertAllowedUpstream(bad, LOOPBACK_FOR_TESTS), bad).toThrow();   // the token never widens beyond loopback
    }
    await expect(startEgressGate({ upstream: { url: 'https://evil.test' }, permitted: async () => true })).rejects.toThrow('upstream must be');
    await expect(startEgressGate({ upstream: { url: 'http://127.0.0.1:9' }, permitted: async () => true })).rejects.toThrow('upstream must be');   // production wiring
  });
  it('does not export the loopback token from the package index', async () => {
    const index = await import('./index.js');
    expect(Object.keys(index)).not.toContain('LOOPBACK_FOR_TESTS');
  });
  it('does not forward when the caller disconnects, or the try is disarmed or re-armed, while consent is being asked', async () => {
    upstream = await startCaptureEndpoint();
    let release: (v: boolean) => void = () => undefined;
    const slow = (): Promise<boolean> => new Promise(resolve => { release = resolve; });
    gate = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: slow });
    const post = (): { done: Promise<number>; abort: () => void } => {
      const u = new URL(gate!.url);
      let done: Promise<number>;
      const req = http.request({ hostname: u.hostname, port: u.port, method: 'POST', path: '/v1/messages', headers: { 'content-type': 'application/json' } });
      done = new Promise(resolve => { req.on('response', r => { r.resume(); resolve(r.statusCode ?? 0); }); req.on('error', () => resolve(0)); });
      req.end('{}');
      return { done, abort: () => req.destroy() };
    };
    const tick = (): Promise<void> => new Promise(resolve => setTimeout(resolve, 50));
    // caller goes away
    gate.arm(accepting);
    let call = post(); await tick(); call.abort(); await tick(); release(true); await call.done;
    expect(upstream.requests).toEqual([]);
    expect(gate.decisions.at(-1)).toMatchObject({ decision: 'refused', reasons: ['try ended while consent was being asked'] });
    // disarmed
    gate.disarm(); gate.arm(accepting);
    call = post(); await tick(); gate.disarm(); release(true);
    expect(await call.done).toBe(403);
    expect(upstream.requests).toEqual([]);
    // disarmed and armed again for a new try
    gate.arm(accepting);
    call = post(); await tick(); gate.disarm(); gate.arm(accepting); release(true);
    expect(await call.done).toBe(403);
    expect(upstream.requests).toEqual([]);
  });
  it('refuses to start, and to forward, while a CA-store or TLS flag is in process.execArgv', async () => {
    upstream = await startCaptureEndpoint();
    const saved = [...process.execArgv];
    for (const flag of ['--use-system-ca', '--use-openssl-ca', '--tls-min-v1.0', '--tls-max-v1.2', '--tls-cipher-list=ALL', '--tls-keylog=/tmp/keys']) {
      try {
        process.execArgv.push(flag);
        await expect(startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true }), flag).rejects.toThrow('ambient');
      } finally { process.execArgv.splice(0, process.execArgv.length, ...saved); }
      const g = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
      try {
        g.arm(accepting);
        process.execArgv.push(flag);
        expect((await send(g.url, 'POST', '/v1/messages', '{}')).status, flag).toBe(403);
        expect(g.decisions.at(-1), flag).toMatchObject({ decision: 'refused', reasons: ['ambient Node network environment is set'] });
      } finally { process.execArgv.splice(0, process.execArgv.length, ...saved); await g.close(); }
    }
    // Flags that only look alike are not refused.
    for (const flag of ['--use-bundled-ca', '--title=tls-runner', '--max-old-space-size=4096']) {
      try {
        process.execArgv.push(flag);
        const g = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
        await g.close();
      } finally { process.execArgv.splice(0, process.execArgv.length, ...saved); }
    }
    expect(upstream.requests).toEqual([]);
  });
  it('refuses to start, and to forward, while any ambient Node network variable is set', async () => {
    const names = ['NODE_TLS_REJECT_UNAUTHORIZED', 'NODE_EXTRA_CA_CERTS', 'NODE_USE_ENV_PROXY', 'NODE_USE_SYSTEM_CA', 'NODE_OPTIONS', 'SSL_CERT_FILE', 'SSL_CERT_DIR', 'HTTPS_PROXY', 'HTTP_PROXY', 'ALL_PROXY', 'https_proxy', 'http_proxy', 'all_proxy'];
    upstream = await startCaptureEndpoint();
    for (const name of names) {
      try {
        process.env[name] = '1';
        await expect(startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true }), name).rejects.toThrow('ambient');
      } finally { delete process.env[name]; }
      const g = await startEgressGate({ upstream: { url: upstream.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
      try {
        g.arm(accepting);
        process.env[name] = '1';
        expect((await send(g.url, 'POST', '/v1/messages', '{}')).status, name).toBe(403);
        expect(g.decisions.at(-1), name).toMatchObject({ reasons: ['ambient Node network environment is set'] });
      } finally { delete process.env[name]; await g.close(); }
    }
    expect(upstream.requests).toEqual([]);
  });
  it('ends the caller\'s response with an error when the upstream drops mid-body', async () => {
    const dropper = http.createServer((_req, res) => { res.writeHead(200, { 'content-type': 'application/json', 'content-length': '1000' }); res.write('{"partial":'); setTimeout(() => res.socket?.destroy(), 30); });
    await new Promise<void>(r => dropper.listen(0, '127.0.0.1', r));
    try {
      gate = await startEgressGate({ upstream: { url: `http://127.0.0.1:${(dropper.address() as { port: number }).port}`, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
      gate.arm(accepting);
      const outcome = await new Promise<string>(resolve => {
        const u = new URL(gate!.url);
        const timer = setTimeout(() => resolve('hung'), 4000);
        const req = http.request({ hostname: u.hostname, port: u.port, method: 'POST', path: '/v1/messages', headers: { 'content-type': 'application/json' } }, res => {
          res.on('error', () => { clearTimeout(timer); resolve('error'); });
          res.on('aborted', () => { clearTimeout(timer); resolve('error'); });
          res.on('close', () => { clearTimeout(timer); resolve(res.complete ? 'complete' : 'error'); });
          res.resume();
        });
        req.on('error', () => { clearTimeout(timer); resolve('error'); });
        req.end('{}');
      });
      expect(outcome).toBe('error');
    } finally { dropper.close(); }
  });
  it('verifies the upstream certificate: a self-signed https upstream is not reached', async () => {
    const dir = mkdtempSync(path.join(tmpdir(), 'gate-cert-'));
    let server: https.Server | undefined;
    try {
      execFileSync('openssl', ['req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-keyout', path.join(dir, 'k.pem'), '-out', path.join(dir, 'c.pem'), '-days', '1', '-subj', '/CN=127.0.0.1', '-addext', 'subjectAltName=IP:127.0.0.1'], { stdio: 'ignore' });
      let hits = 0;
      server = https.createServer({ key: readFileSync(path.join(dir, 'k.pem')), cert: readFileSync(path.join(dir, 'c.pem')) }, (_req, res) => { hits++; res.writeHead(200); res.end('x'); });
      await new Promise<void>(r => server!.listen(0, '127.0.0.1', r));
      gate = await startEgressGate({ upstream: { url: `https://127.0.0.1:${(server.address() as { port: number }).port}`, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
      // Even if the process-wide default agent is made insecure, the gate's own pinned agent must still verify.
      const globalOptions = https.globalAgent.options as { rejectUnauthorized?: boolean };
      const before = globalOptions.rejectUnauthorized;
      globalOptions.rejectUnauthorized = false;
      try {
        gate.arm(accepting);
        expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(502);
      } finally { globalOptions.rejectUnauthorized = before; }
      expect(hits).toBe(0);
      expect(gate.decisions.at(-1)).toMatchObject({ reasons: ['upstream unreachable'] });
    } finally { server?.close(); rmSync(dir, { recursive: true, force: true }); }
  });
  it('does not carry an earlier rejected try\'s unbilled evidence into a later 429 whose body is cut off', async () => {
    let n = 0;
    const flaky = http.createServer((_req, res) => {
      n++;
      if (n === 1) { res.writeHead(429, { 'content-type': 'application/json' }); res.end('{"type":"error","error":{"type":"rate_limit_error","message":"x"}}'); return; }
      res.writeHead(429, { 'content-type': 'application/json', 'content-length': '500' }); res.write('{"type":"err'); setTimeout(() => res.socket?.destroy(), 30);
    });
    await new Promise<void>(r => flaky.listen(0, '127.0.0.1', r));
    try {
      gate = await startEgressGate({ upstream: { url: `http://127.0.0.1:${(flaky.address() as { port: number }).port}`, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
      gate.arm(accepting);
      expect((await send(gate.url, 'POST', '/v1/messages', '{}')).status).toBe(429);
      await new Promise(r => setTimeout(r, 50));
      // first try's evidence is deliberately NOT taken; the second try must reset it
      gate.disarm(); gate.arm(accepting);
      await new Promise<void>(resolve => {
        const u = new URL(gate!.url);
        const req = http.request({ hostname: u.hostname, port: u.port, method: 'POST', path: '/v1/messages', headers: { 'content-type': 'application/json' } }, res => { res.on('error', () => undefined); res.on('close', () => resolve()); res.resume(); });
        req.on('error', () => resolve());
        req.end('{}');
      });
      await new Promise(r => setTimeout(r, 100));
      expect(gate.takeRejectedUnbilled()).toBe(false);
    } finally { flaky.close(); }
  });
  it('recognises every by-path form of a gate import: source or dist, absolute-package or relative, static or dynamic', () => {
    for (const text of [
      "import { startEgressGate } from '../../packages/polaris-generation-provider/src/egress-gate.js';",
      "import { startEgressGate } from '../packages/polaris-generation-provider/dist/egress-gate.js';",
      "import { LOOPBACK_FOR_TESTS as t } from './dist/egress-gate.js';",
      "export * from \"../dist/egress-gate\";",
      "const gate = await import('../dist/egress-gate.js');",
      "const gate = require('./egress-gate.cjs');",
    ]) expect(importsGateByPath(text), text).toBe(true);
    for (const text of ["import { startEgressGate } from '@syzygy/polaris-generation-provider';", "// see egress-gate.ts for the gate", "const name = 'egress-gate-report';"]) {
      expect(importsGateByPath(text), text).toBe(false);
    }
  });
  it('is imported by name outside tests and testkits nowhere: LOOPBACK_FOR_TESTS appears only in the gate module, tests and testkits', () => {
    const here = path.dirname(fileURLToPath(import.meta.url));
    const root = path.resolve(here, '../../..');
    const hits: string[] = [];
    const walk = (dir: string): void => {
      for (const entry of readdirSync(dir)) {
        if (entry === 'node_modules' || entry === 'dist' || entry === '.git' || entry === '.worktrees') continue;
        const full = path.join(dir, entry);
        if (statSync(full).isDirectory()) { walk(full); continue; }
        if (!/\.(ts|tsx|mts|js|mjs|cjs)$/.test(entry)) continue;
        if (/\.test\.(ts|tsx|mts)$/.test(entry) || /\.testkit\.ts$/.test(entry)) continue;
        const text = readFileSync(full, 'utf8');
        if (text.includes('LOOPBACK_FOR_TESTS') && path.relative(root, full) !== 'packages/polaris-generation-provider/src/egress-gate.ts') hits.push(path.relative(root, full));
        if (importsGateByPath(text) && !path.relative(root, full).startsWith('packages/polaris-generation-provider/')) hits.push(`${path.relative(root, full)} (imports the gate by path)`);
      }
    };
    walk(path.join(root, 'packages')); walk(path.join(root, 'apps')); if (existsSync(path.join(root, 'scripts'))) walk(path.join(root, 'scripts'));
    expect(hits).toEqual([]);
  });
  it('parses retry-after seconds and dates, and nothing else', () => {
    expect(parseRetryAfterMs('3', 0)).toBe(3000);
    expect(parseRetryAfterMs(new Date(5000).toUTCString(), 1000)).toBe(4000);
    expect(parseRetryAfterMs('soon', 0)).toBeNull();
    expect(parseRetryAfterMs(undefined, 0)).toBeNull();
    expect(parseRetryAfterMs('-1', 0)).toBeNull();
  });
});
