import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { MessagesApiProviderError, acceptMessagesApiRequest, createMessagesApiGenerate, type MessagesApiProviderConfig } from './messages-api-provider.js';
import type { CapturedRequest } from './request-acceptance.js';
import { startCaptureEndpoint, type CaptureEndpoint } from './capture-endpoint.testkit.js';

const permit = { attemptId: 'attempt-1', maxUsageUnits: 100_000, maxOutputBytes: 20_000 };
const e = { system: 'SYSTEM PROMPT é\n"quoted"', input: '{"inputs":{"sources":[{"text":"Reduce recurring mental labor."}]}}' };
let endpoint: CaptureEndpoint;
beforeEach(async () => { endpoint = await startCaptureEndpoint(); });
afterEach(async () => { await endpoint.close(); });
const config = (extra: Partial<MessagesApiProviderConfig> = {}): MessagesApiProviderConfig => ({
  model: 'claude-opus-5-5', apiKey: 'sk-ant-dummy-capture-only', baseUrl: endpoint.url, effort: 'high', maxOutputTokens: 4000,
  retry: { maxAttempts: 3, baseDelayMs: 1, maxDelayMs: 2, budgetMs: 10_000 }, ...extra,
});
const expectation = { model: 'claude-opus-5-5', ...e, effort: 'high', maxTokens: 4000 };
const call = (h: ReturnType<typeof createMessagesApiGenerate>, signal = new AbortController().signal) =>
  h.generate({ permit, stage: 'inventory', system: e.system, input: e.input, responseSchema: {}, signal });

describe('Messages API route', () => {
  it('sends exactly the generator bytes plus profile-set limits, and maps usage and model', async () => {
    endpoint.script({ kind: 'text', text: '{"stage":"inventory"}', inputTokens: 40, outputTokens: 9 });
    const reply = await call(createMessagesApiGenerate(config()));
    expect(endpoint.requests).toHaveLength(1);                       // no probe, no second host call
    const captured = endpoint.requests[0]!;
    expect(acceptMessagesApiRequest(captured, expectation)).toEqual({ accepted: true, violations: [] });
    expect(JSON.parse(captured.body)).toEqual({ model: 'claude-opus-5-5', max_tokens: 4000, system: e.system, messages: [{ role: 'user', content: e.input }], output_config: { effort: 'high' }, stream: true });
    expect(reply).toEqual({ body: '{"stage":"inventory"}', model: 'capture-model', usageUnits: 49 });
  });

  it('lets permit allowances lower max_tokens but never raise it', async () => {
    await createMessagesApiGenerate(config()).generate({ permit: { ...permit, maxOutputBytes: 321 }, stage: 'inventory', system: e.system, input: e.input, responseSchema: {}, signal: new AbortController().signal });
    expect(JSON.parse(endpoint.requests[0]!.body).max_tokens).toBe(321);
  });

  it('rule 6: the acceptance predicate rejects each added or altered field', () => {
    const good: CapturedRequest = { method: 'POST', url: '/v1/messages', headers: { 'content-type': 'application/json', 'x-api-key': 'k' }, body: JSON.stringify({ model: 'claude-opus-5-5', max_tokens: 4000, system: e.system, messages: [{ role: 'user', content: e.input }], output_config: { effort: 'high' }, stream: true }) };
    expect(acceptMessagesApiRequest(good, expectation).accepted).toBe(true);
    const body = JSON.parse(good.body) as Record<string, any>;
    const mutate = (edit: (b: Record<string, any>) => void): CapturedRequest => { const b = structuredClone(body); edit(b); return { ...good, body: JSON.stringify(b) }; };
    const mutants: [string, CapturedRequest, string][] = [
      ['tools added', mutate(b => { b.tools = []; }), 'unlisted body field tools'],
      ['metadata added', mutate(b => { b.metadata = { user_id: 'x' }; }), 'unlisted body field metadata'],
      ['thinking added', mutate(b => { b.thinking = { type: 'adaptive' }; }), 'unlisted body field thinking'],
      ['system edited', mutate(b => { b.system += ' '; }), 'body field system'],
      ['system as block list', mutate(b => { b.system = [{ type: 'text', text: e.system }]; }), 'body field system'],
      ['extra message', mutate(b => { b.messages.push({ role: 'user', content: 'x' }); }), 'body field messages'],
      ['input edited', mutate(b => { b.messages[0].content += ' '; }), 'body field messages'],
      ['effort drift', mutate(b => { b.output_config.effort = 'low'; }), 'body field output_config'],
      ['max_tokens drift', mutate(b => { b.max_tokens = 5; }), 'body field max_tokens'],
      ['not streaming', mutate(b => { b.stream = false; }), 'body field stream'],
      ['unlisted header', { ...good, headers: { ...good.headers, cookie: 'a' } }, 'unlisted header cookie'],
      ['wrong endpoint', { ...good, url: '/v1/messages?beta=true' }, 'unexpected endpoint'],
    ];
    for (const [name, mutant, expected] of mutants) {
      const verdict = acceptMessagesApiRequest(mutant, expectation);
      expect(verdict.accepted, name).toBe(false);
      expect(verdict.violations.join('|'), name).toContain(expected);
    }
  });

  it('retries 429 then 529, reports every try, and stops on exhaustion or other statuses', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 529 }, { kind: 'text', text: '{}', inputTokens: 5, outputTokens: 3 });
    const h = createMessagesApiGenerate(config());
    expect((await call(h)).usageUnits).toBe(8);
    expect(h.attempts().map(r => [r.try, r.outcome, r.httpStatus, r.usageUnits, r.backoffMs])).toEqual([[1, 'rate-limited', 429, 0, 1], [2, 'overloaded', 529, 0, 2], [3, 'completed', null, 8, 0]]);
    expect(endpoint.requests).toHaveLength(3);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 429 }, { kind: 'status', status: 429 });
    await expect(call(createMessagesApiGenerate(config()))).rejects.toMatchObject({ code: 'rate-limited', attempts: 3, status: 429 });
    expect(endpoint.requests).toHaveLength(3);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 500 });
    await expect(call(createMessagesApiGenerate(config()))).rejects.toMatchObject({ code: 'provider-error', status: 500 });
    expect(endpoint.requests).toHaveLength(1);
  });

  it('stops retrying when the next backoff would exceed the run budget', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    await expect(call(createMessagesApiGenerate(config({ retry: { maxAttempts: 5, baseDelayMs: 5_000, maxDelayMs: 5_000, budgetMs: 100 } })))).rejects.toMatchObject({ code: 'rate-limited', attempts: 1 });
    expect(endpoint.requests).toHaveLength(1);
  });

  it('aborts mid-response and closes the connection, and does not start when already aborted', async () => {
    endpoint.script({ kind: 'hang' });
    const controller = new AbortController();
    const h = createMessagesApiGenerate(config());
    const pending = call(h, controller.signal);
    const assertion = expect(pending).rejects.toMatchObject({ code: 'aborted' });
    for (let i = 0; i < 100 && endpoint.requests.length === 0; i++) await new Promise(r => setTimeout(r, 20));
    controller.abort();
    await assertion;
    for (let i = 0; i < 100 && endpoint.closedWhileHanging() === 0; i++) await new Promise(r => setTimeout(r, 20));
    expect(endpoint.closedWhileHanging()).toBe(1);
    expect(h.attempts().at(-1)?.outcome).toBe('aborted');
    const done = new AbortController(); done.abort();
    await expect(call(createMessagesApiGenerate(config()), done.signal)).rejects.toBeInstanceOf(MessagesApiProviderError);
  });

  it('refuses a tool-use or empty reply as no-output', async () => {
    endpoint.script({ kind: 'tool', name: 'x', input: {} });
    await expect(call(createMessagesApiGenerate(config()))).rejects.toMatchObject({ code: 'no-output' });
  });

  it('rejects invalid configuration', () => {
    expect(() => createMessagesApiGenerate(config({ apiKey: '' }))).toThrow(MessagesApiProviderError);
    expect(() => createMessagesApiGenerate(config({ maxOutputTokens: 0 }))).toThrow(MessagesApiProviderError);
  });
});
