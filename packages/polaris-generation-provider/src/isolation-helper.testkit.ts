/** Test-only entry, bundled and run inside an empty network namespace under
 * strace: starts its own loopback capture endpoint, makes one adapter call and
 * prints what the endpoint saw. */
import { LOOPBACK_FOR_TESTS } from './egress-gate.js';
import { createMessagesApiGenerate, acceptMessagesApiRequest } from './messages-api-provider.js';
import { createAgentSdkGenerate } from './agent-sdk-provider.js';
import { acceptCapturedTraffic } from './request-acceptance.js';
import { startCaptureEndpoint } from './capture-endpoint.testkit.js';

const runDir = process.argv[2]!;
const endpoint = await startCaptureEndpoint({ kind: 'text', text: '{"stage":"inventory"}' });
const system = 'SYSTEM';
const input = '{"inputs":{}}';
const route = process.argv[3] ?? 'agent-sdk';
const handle = route === 'messages'
  ? createMessagesApiGenerate({ model: 'claude-opus-5-5', apiKey: 'sk-ant-dummy-capture-only', upstream: { url: endpoint.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true, effort: 'medium', maxOutputTokens: 1000 })
  : createAgentSdkGenerate({ runDir, model: 'claude-opus-5-5', auth: { apiKey: 'sk-ant-dummy-capture-only' }, upstream: { url: endpoint.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true });
const reply = await handle.generate({ permit: { attemptId: 'a', maxUsageUnits: 1000, maxOutputBytes: 1000 }, stage: 'inventory', system, input, responseSchema: {}, signal: new AbortController().signal });
const expected = { model: 'claude-opus-5-5', system, input, effort: 'medium', maxTokens: 1000 };
const verdict = route === 'messages' ? acceptMessagesApiRequest(endpoint.requests[0]!, expected) : acceptCapturedTraffic(endpoint.requests, expected);
console.log(JSON.stringify({ port: endpoint.port, gatePort: Number(new URL((handle as { gateUrl?: () => string | undefined }).gateUrl?.() ?? 'http://127.0.0.1:0').port), requests: endpoint.requests.map(r => `${r.method} ${r.url}`), verdict, replyBody: reply.body }));
await endpoint.close();
process.exit(0);
