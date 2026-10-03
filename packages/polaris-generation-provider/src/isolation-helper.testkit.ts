/** Test-only entry, bundled and run inside an empty network namespace under
 * strace: starts its own loopback capture endpoint, makes one adapter call and
 * prints what the endpoint saw. */
import { createAgentSdkGenerate } from './agent-sdk-provider.js';
import { acceptCapturedTraffic } from './request-acceptance.js';
import { startCaptureEndpoint } from './capture-endpoint.testkit.js';

const runDir = process.argv[2]!;
const endpoint = await startCaptureEndpoint({ kind: 'text', text: '{"stage":"inventory"}' });
const system = 'SYSTEM';
const input = '{"inputs":{}}';
const handle = createAgentSdkGenerate({ runDir, model: 'claude-opus-5-5', auth: { apiKey: 'sk-ant-dummy-capture-only' }, baseUrl: endpoint.url });
const reply = await handle.generate({ permit: { attemptId: 'a', maxUsageUnits: 1000, maxOutputBytes: 1000 }, stage: 'inventory', system, input, responseSchema: {}, signal: new AbortController().signal });
const verdict = acceptCapturedTraffic(endpoint.requests, { model: 'claude-opus-5-5', system, input, effort: 'medium', maxTokens: 1000 });
console.log(JSON.stringify({ port: endpoint.port, requests: endpoint.requests.map(r => `${r.method} ${r.url}`), verdict, replyBody: reply.body }));
await endpoint.close();
process.exit(0);
