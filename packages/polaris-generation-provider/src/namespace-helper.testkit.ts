/** Test-only entry, bundled and run inside a user, mount and network namespace
 * (egress-namespace.test.ts) where api.anthropic.com resolves to 127.0.0.1, the
 * system CA store holds only a probe CA, or /etc/claude-code holds a managed
 * policy. It prints one JSON line saying what an interceptor saw. */
import http from 'node:http';
import https from 'node:https';
import { mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import tls from 'node:tls';
import { query } from '@anthropic-ai/claude-agent-sdk';
import { LOOPBACK_FOR_TESTS, PROVIDER_ORIGIN, startEgressGate } from './egress-gate.js';
import { AgentSdkProviderError, createAgentSdkGenerate } from './agent-sdk-provider.js';
import { startCaptureEndpoint } from './capture-endpoint.testkit.js';

const [mode, dir, variant] = [process.argv[2]!, process.argv[3]!, process.argv[4] ?? ''];
const done = (value: unknown): never => { console.log(JSON.stringify(value)); process.exit(0); };
let intercepted = 0;

if (mode === 'tls-raw' || mode === 'tls-gate') {
  // The interceptor presents a leaf for api.anthropic.com signed by the probe CA.
  const server = https.createServer({ key: readFileSync(join(dir, 'leaf.key')), cert: readFileSync(join(dir, 'leaf.pem')) }, (req, res) => { intercepted++; req.resume(); res.end('{}'); });
  await new Promise<void>(resolve => server.listen(443, '127.0.0.1', resolve));
  if (mode === 'tls-raw') {
    // Control: the default agent in this process trusts the probe CA, so the rig can intercept.
    await new Promise<void>(resolve => { const r = https.get(`${PROVIDER_ORIGIN}/`, res => { res.resume(); res.on('end', resolve); }); r.on('error', () => resolve()); });
    done({ intercepted });
  }
  if (variant === 'inprocess-ca') tls.setDefaultCACertificates([...tls.getCACertificates('default'), readFileSync(join(dir, 'ca.pem'), 'utf8')]);
  // An undetected trust source: the flags stay in effect but the gate's flag check cannot see them.
  if (variant === 'hide-flags') process.execArgv.splice(0, process.execArgv.length);
  let gate;
  try { gate = await startEgressGate({ upstream: { url: PROVIDER_ORIGIN }, permitted: async () => true }); }
  catch (error) { done({ started: false, error: (error as Error).message, intercepted }); }
  gate!.arm(() => ({ accepted: true, violations: [] }));
  const status = await new Promise<number>(resolve => {
    const u = new URL(gate!.url);
    const req = http.request({ hostname: u.hostname, port: u.port, method: 'POST', path: '/v1/messages', headers: { 'content-type': 'application/json' } }, res => { res.resume(); res.on('end', () => resolve(res.statusCode ?? 0)); });
    req.on('error', () => resolve(0));
    req.end('{}');
  });
  done({ started: true, status, decisions: gate!.decisions, intercepted });
}

if (mode === 'managed-raw' || mode === 'managed-adapter') {
  // The managed policy points ANTHROPIC_BASE_URL here.
  const interceptor = http.createServer((req, res) => { intercepted++; req.resume(); res.writeHead(500); res.end(); });
  await new Promise<void>(resolve => interceptor.listen(18080, '127.0.0.1', resolve));
  const endpoint = await startCaptureEndpoint({ kind: 'text', text: '{}' });
  if (mode === 'managed-raw') {
    // Control: the CLI with the adapter's closed environment, but no refusal in front of it.
    for (const d of ['home', 'config', 'tmp', 'cwd']) mkdirSync(join(dir, d), { recursive: true });
    const env = { HOME: join(dir, 'home'), CLAUDE_CONFIG_DIR: join(dir, 'config'), TMPDIR: join(dir, 'tmp'), ANTHROPIC_API_KEY: 'sk-ant-dummy-capture-only',
      ANTHROPIC_BASE_URL: endpoint.url, CLAUDE_CODE_SIMPLE: '1', CLAUDE_CODE_MAX_RETRIES: '0', DISABLE_TELEMETRY: '1', CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: '1', NO_PROXY: '*',
      ...(variant === 'override' ? { CLAUDE_CODE_MANAGED_SETTINGS_PATH: join(dir, 'tmp') } : {}) };
    const q = query({ prompt: 'x', options: { systemPrompt: 's', settingSources: [], mcpServers: {}, tools: [], cwd: join(dir, 'cwd'), env, maxTurns: 1, persistSession: false } });
    try { for await (const _ of q) { /* drain */ } } catch { /* the outcome is what the servers saw */ }
    done({ intercepted, captured: endpoint.requests.length });
  }
  const handle = createAgentSdkGenerate({ runDir: dir, model: 'claude-opus-5-5', auth: { apiKey: 'sk-ant-dummy-capture-only' }, upstream: { url: endpoint.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
  let code = 'none';
  try { await handle.generate({ permit: { attemptId: 'a', maxUsageUnits: 1000, maxOutputBytes: 1000 }, stage: 'inventory', system: 'S', input: '{"inputs":{}}', responseSchema: {}, signal: new AbortController().signal }); }
  catch (error) { code = error instanceof AgentSdkProviderError ? error.code : 'other'; }
  done({ code, intercepted, captured: endpoint.requests.length });
}
done({ error: `unknown mode ${mode}` });
