/** Test-only. A local Messages-API-shaped endpoint on 127.0.0.1 that records
 * every request and answers from a script. It never forwards anything. */
import http from 'node:http';
import type { AddressInfo } from 'node:net';
import type { CapturedRequest } from './request-acceptance.js';

export type Script =
  | { readonly kind: 'text'; readonly text: string; readonly inputTokens?: number; readonly outputTokens?: number }
  | { readonly kind: 'tool'; readonly name: string; readonly input: unknown; readonly inputTokens?: number; readonly outputTokens?: number }
  | { readonly kind: 'status'; readonly status: number }
  | { readonly kind: 'hang' };

export interface CaptureEndpoint {
  readonly url: string;
  readonly port: number;
  readonly requests: CapturedRequest[];
  /** Only the POST /v1/messages requests (the ones that carry the generator's bytes). */
  readonly messages: () => CapturedRequest[];
  readonly closedWhileHanging: () => number;
  readonly script: (...next: Script[]) => void;
  readonly close: () => Promise<void>;
}

export async function startCaptureEndpoint(defaultScript: Script = { kind: 'text', text: '{}' }): Promise<CaptureEndpoint> {
  const requests: CapturedRequest[] = [];
  const queue: Script[] = [];
  let closed = 0;
  const server = http.createServer((req, res) => {
    const chunks: Buffer[] = [];
    req.on('data', c => chunks.push(c as Buffer));
    req.on('end', () => {
      requests.push({ method: req.method ?? '', url: req.url ?? '', headers: req.headers, body: Buffer.concat(chunks).toString('utf8') });
      if (req.method === 'HEAD') { res.writeHead(200); res.end(); return; }   // connectivity probe: answered, never scripted
      const step = queue.shift() ?? defaultScript;
      if (step.kind === 'hang') { res.writeHead(200, { 'content-type': 'text/event-stream' }); res.write(': hold\n\n'); res.on('close', () => { closed++; }); return; }
      if (step.kind === 'status') {
        res.writeHead(step.status, { 'content-type': 'application/json', 'request-id': 'req_capture' });
        res.end(JSON.stringify({ type: 'error', error: { type: step.status === 429 ? 'rate_limit_error' : 'overloaded_error', message: 'capture' } }));
        return;
      }
      const ev = (name: string, data: object): void => { res.write(`event: ${name}\ndata: ${JSON.stringify({ type: name, ...data })}\n\n`); };
      res.writeHead(200, { 'content-type': 'text/event-stream' });
      ev('message_start', { message: { id: 'msg_capture', type: 'message', role: 'assistant', model: 'capture-model', content: [], stop_reason: null, usage: { input_tokens: step.inputTokens ?? 11, output_tokens: 1 } } });
      if (step.kind === 'text') {
        ev('content_block_start', { index: 0, content_block: { type: 'text', text: '' } });
        ev('content_block_delta', { index: 0, delta: { type: 'text_delta', text: step.text } });
      } else {
        ev('content_block_start', { index: 0, content_block: { type: 'tool_use', id: 'toolu_capture', name: step.name, input: {} } });
        ev('content_block_delta', { index: 0, delta: { type: 'input_json_delta', partial_json: JSON.stringify(step.input) } });
      }
      ev('content_block_stop', { index: 0 });
      ev('message_delta', { delta: { stop_reason: step.kind === 'text' ? 'end_turn' : 'tool_use' }, usage: { output_tokens: step.outputTokens ?? 7 } });
      ev('message_stop', {});
      res.end();
    });
  });
  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = (server.address() as AddressInfo).port;
  return {
    url: `http://127.0.0.1:${port}`, port, requests, messages: () => requests.filter(r => r.method === 'POST'), closedWhileHanging: () => closed,
    script: (...next) => { queue.push(...next); },
    close: () => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }),
  };
}

/** A recording proxy: any client that honours HTTP(S)_PROXY and tries a host other than the capture endpoint lands here. */
export async function startRecordingProxy(): Promise<{ readonly url: string; readonly hits: string[]; readonly close: () => Promise<void> }> {
  const hits: string[] = [];
  const server = http.createServer((req, res) => { hits.push(`${req.method} ${req.url}`); res.writeHead(502); res.end(); });
  server.on('connect', (req, socket) => { hits.push(`CONNECT ${req.url}`); socket.end('HTTP/1.1 502 Bad Gateway\r\n\r\n'); });
  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = (server.address() as AddressInfo).port;
  return { url: `http://127.0.0.1:${port}`, hits, close: () => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }) };
}
