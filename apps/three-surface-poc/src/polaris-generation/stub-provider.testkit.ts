/** Test-only. A Messages-API-shaped endpoint on 127.0.0.1 whose replies are computed from each request, so a whole pipeline can
 * run against it. It records every request body and never forwards anything. */
import http from 'node:http';
import type { AddressInfo } from 'node:net';

export interface StubRequest { readonly system: string; readonly input: string; readonly maxTokens: number; readonly raw: string }
export interface StubReply { readonly text: string; readonly inputTokens?: number; readonly outputTokens?: number }
export interface StubProvider { readonly url: string; readonly requests: StubRequest[]; readonly close: () => Promise<void> }

export async function startStubProvider(respond: (request: StubRequest, ordinal: number) => StubReply): Promise<StubProvider> {
  const requests: StubRequest[] = [];
  const server = http.createServer((req, res) => {
    const chunks: Buffer[] = [];
    req.on('data', c => chunks.push(c as Buffer));
    req.on('end', () => {
      if (req.method === 'HEAD') { res.writeHead(200); res.end(); return; }
      const raw = Buffer.concat(chunks).toString('utf8');
      let parsed: { system?: unknown; messages?: { content?: unknown }[]; max_tokens?: unknown } = {};
      try { parsed = JSON.parse(raw); } catch { /* recorded as an empty request */ }
      const request: StubRequest = { system: typeof parsed.system === 'string' ? parsed.system : '', input: typeof parsed.messages?.[0]?.content === 'string' ? parsed.messages[0].content : '', maxTokens: typeof parsed.max_tokens === 'number' ? parsed.max_tokens : 0, raw };
      const ordinal = requests.length;
      requests.push(request);
      const reply = respond(request, ordinal);
      const ev = (name: string, data: object): void => { res.write(`event: ${name}\ndata: ${JSON.stringify({ type: name, ...data })}\n\n`); };
      res.writeHead(200, { 'content-type': 'text/event-stream', 'request-id': `req_stub_${ordinal}` });
      ev('message_start', { message: { id: `msg_stub_${ordinal}`, type: 'message', role: 'assistant', model: 'stub-model', content: [], stop_reason: null, usage: { input_tokens: reply.inputTokens ?? 1000, output_tokens: 1 } } });
      ev('content_block_start', { index: 0, content_block: { type: 'text', text: '' } });
      ev('content_block_delta', { index: 0, delta: { type: 'text_delta', text: reply.text } });
      ev('content_block_stop', { index: 0 });
      ev('message_delta', { delta: { stop_reason: 'end_turn' }, usage: { output_tokens: reply.outputTokens ?? 1000 } });
      ev('message_stop', {});
      res.end();
    });
  });
  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = (server.address() as AddressInfo).port;
  return { url: `http://127.0.0.1:${port}`, requests, close: () => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }) };
}
