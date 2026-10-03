/** Test-only. A local Messages-API-shaped endpoint on 127.0.0.1 that records
 * every request and answers from a script. It never forwards anything. */
import http from 'node:http';
import type { AddressInfo } from 'node:net';
import type { CapturedRequest } from './request-acceptance.js';

export type Script =
  | { readonly kind: 'text'; readonly text: string; readonly inputTokens?: number; readonly outputTokens?: number; readonly noUsage?: boolean; readonly stopReason?: string }
  | { readonly kind: 'tool'; readonly name: string; readonly input: unknown; readonly inputTokens?: number; readonly outputTokens?: number }
  | { readonly kind: 'status'; readonly status: number; readonly retryAfter?: string; readonly body?: string }
  | { readonly kind: 'mixed'; readonly text: string }
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
        res.writeHead(step.status, { 'content-type': 'application/json', 'request-id': 'req_capture', ...(step.retryAfter === undefined ? {} : { 'retry-after': step.retryAfter }) });
        res.end(step.body ?? JSON.stringify({ type: 'error', error: { type: step.status === 429 ? 'rate_limit_error' : 'overloaded_error', message: 'capture' } }));
        return;
      }
      const ev = (name: string, data: object): void => { res.write(`event: ${name}\ndata: ${JSON.stringify({ type: name, ...data })}\n\n`); };
      res.writeHead(200, { 'content-type': 'text/event-stream' });
      const noUsage = step.kind === 'text' && step.noUsage === true;
      ev('message_start', { message: { id: 'msg_capture', type: 'message', role: 'assistant', model: 'capture-model', content: [], stop_reason: null, usage: noUsage ? {} : { input_tokens: step.kind === 'mixed' ? 11 : step.inputTokens ?? 11, output_tokens: 1 } } });
      let index = 0;
      const text = (value: string): void => {
        ev('content_block_start', { index, content_block: { type: 'text', text: '' } });
        ev('content_block_delta', { index, delta: { type: 'text_delta', text: value } });
        ev('content_block_stop', { index }); index++;
      };
      const tool = (name: string, input: unknown): void => {
        ev('content_block_start', { index, content_block: { type: 'tool_use', id: 'toolu_capture', name, input: {} } });
        ev('content_block_delta', { index, delta: { type: 'input_json_delta', partial_json: JSON.stringify(input) } });
        ev('content_block_stop', { index }); index++;
      };
      if (step.kind === 'text') text(step.text);
      else if (step.kind === 'mixed') { text(step.text); tool('Bash', { command: 'ls' }); }
      else tool(step.name, step.input);
      const stop = step.kind === 'text' ? step.stopReason ?? 'end_turn' : step.kind === 'mixed' ? 'end_turn' : 'tool_use';
      ev('message_delta', { delta: { stop_reason: stop }, usage: noUsage ? {} : { output_tokens: step.kind === 'mixed' ? 7 : step.outputTokens ?? 7 } });
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
