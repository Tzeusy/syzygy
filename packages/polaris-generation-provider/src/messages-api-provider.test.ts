import { getEventListeners } from 'node:events';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { MessagesApiProviderError, acceptMessagesApiRequest, createMessagesApiGenerate, type MessagesApiProviderConfig } from './messages-api-provider.js';
import { LOOPBACK_FOR_TESTS } from './egress-gate.js';
import type { CapturedRequest } from './request-acceptance.js';
import { startCaptureEndpoint, type CaptureEndpoint } from './capture-endpoint.testkit.js';

const permit = { attemptId: 'attempt-1', maxUsageUnits: 100_000, maxOutputBytes: 20_000 };
const e = { system: 'SYSTEM PROMPT é\n"quoted"', input: '{"inputs":{"sources":[{"text":"Reduce recurring mental labor."}]}}' };
const handles: { close: () => Promise<void> }[] = [];
const make = (c: MessagesApiProviderConfig) => { const h = createMessagesApiGenerate(c); handles.push(h); return h; };
let endpoint: CaptureEndpoint;
beforeEach(async () => { endpoint = await startCaptureEndpoint(); });
afterEach(async () => { for (const h of handles.splice(0)) await h.close(); await endpoint.close(); });
const config = (extra: Partial<MessagesApiProviderConfig> = {}): MessagesApiProviderConfig => ({
  model: 'claude-opus-5-5', apiKey: 'sk-ant-dummy-capture-only', upstream: { url: endpoint.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true, effort: 'high', maxOutputTokens: 4000,
  retry: { maxAttempts: 3, baseDelayMs: 1, maxDelayMs: 2, budgetMs: 60_000 }, ...extra,
});
const expectation = { model: 'claude-opus-5-5', ...e, effort: 'high', maxTokens: 4000, apiKey: 'sk-ant-dummy-capture-only' };
const call = (h: ReturnType<typeof make>, signal: AbortSignal | undefined = new AbortController().signal) =>
  h.generate({ permit, stage: 'inventory', system: e.system, input: e.input, responseSchema: {}, signal: signal ?? new AbortController().signal });

describe('Messages API route', () => {
  it('sends exactly the generator bytes plus profile-set limits, and maps usage and model', async () => {
    endpoint.script({ kind: 'text', text: '{"stage":"inventory"}', inputTokens: 40, outputTokens: 9 });
    const reply = await call(make(config()));
    expect(endpoint.requests).toHaveLength(1);                       // no probe, no second host call
    const captured = endpoint.requests[0]!;
    expect(acceptMessagesApiRequest(captured, expectation)).toEqual({ accepted: true, violations: [] });
    expect(JSON.parse(captured.body)).toEqual({ model: 'claude-opus-5-5', max_tokens: 4000, system: e.system, messages: [{ role: 'user', content: e.input }], output_config: { effort: 'high' }, stream: true });
    expect(reply).toEqual({ body: '{"stage":"inventory"}', model: 'capture-model', usageUnits: 49 });
  });

  it('lets permit allowances lower max_tokens but never raise it', async () => {
    await make(config()).generate({ permit: { ...permit, maxOutputBytes: 321 }, stage: 'inventory', system: e.system, input: e.input, responseSchema: {}, signal: new AbortController().signal });
    expect(JSON.parse(endpoint.requests[0]!.body).max_tokens).toBe(321);
  });

  it('rule 6: the acceptance predicate rejects each added or altered field', async () => {
    await call(make(config()), undefined);
    const realCapture = endpoint.requests[0]!;
    const good = realCapture;
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
      ['user-agent', { ...good, headers: { ...good.headers, 'user-agent': 'curl/8' } }, 'header user-agent'],
      ['api key', { ...good, headers: { ...good.headers, 'x-api-key': 'sk-other' } }, 'x-api-key'],
      ['version', { ...good, headers: { ...good.headers, 'anthropic-version': '2024-01-01' } }, 'anthropic-version'],
      ['content-length', { ...good, headers: { ...good.headers, 'content-length': '1' } }, 'content-length'],
      ['missing header', { ...good, headers: Object.fromEntries(Object.entries(good.headers).filter(([k]) => k !== 'anthropic-version')) }, 'anthropic-version missing'],
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
    const h = make(config());
    expect((await call(h)).usageUnits).toBe(8);
    expect(h.attempts().map(r => [r.try, r.outcome, r.httpStatus, r.usageUnits, r.backoffMs])).toEqual([[1, 'rate-limited', 429, 0, 1], [2, 'overloaded', 529, 0, 2], [3, 'completed', null, 8, 0]]);
    expect(endpoint.requests).toHaveLength(3);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 429 }, { kind: 'status', status: 429 });
    await expect(call(make(config()))).rejects.toMatchObject({ code: 'rate-limited', attempts: 3, status: 429 });
    expect(endpoint.requests).toHaveLength(3);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 500 });
    await expect(call(make(config()))).rejects.toMatchObject({ code: 'provider-error', status: 500 });
    expect(endpoint.requests).toHaveLength(1);
  });

  it('stops retrying when the next backoff would exceed the run budget', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    await expect(call(make(config({ retry: { maxAttempts: 5, baseDelayMs: 5_000, maxDelayMs: 5_000, budgetMs: 100 } })))).rejects.toMatchObject({ code: 'rate-limited', attempts: 1 });
    expect(endpoint.requests).toHaveLength(1);
  });

  it('aborts mid-response and closes the connection, and does not start when already aborted', async () => {
    endpoint.script({ kind: 'hang' });
    const controller = new AbortController();
    const h = make(config());
    const pending = call(h, controller.signal);
    const assertion = expect(pending).rejects.toMatchObject({ code: 'aborted' });
    for (let i = 0; i < 100 && endpoint.requests.length === 0; i++) await new Promise(r => setTimeout(r, 20));
    controller.abort();
    await assertion;
    for (let i = 0; i < 100 && endpoint.closedWhileHanging() === 0; i++) await new Promise(r => setTimeout(r, 20));
    expect(endpoint.closedWhileHanging()).toBe(1);
    expect(h.attempts().at(-1)?.outcome).toBe('aborted');
    const done = new AbortController(); done.abort();
    await expect(call(make(config()), done.signal)).rejects.toBeInstanceOf(MessagesApiProviderError);
  });

  it('refuses a tool-use or empty reply as no-output', async () => {
    endpoint.script({ kind: 'tool', name: 'x', input: {} });
    await expect(call(make(config()))).rejects.toMatchObject({ code: 'no-output' });
  });

  it('rejects invalid configuration', () => {
    expect(() => createMessagesApiGenerate(config({ apiKey: '' }))).toThrow(MessagesApiProviderError);
    expect(() => createMessagesApiGenerate(config({ maxOutputTokens: 0 }))).toThrow(MessagesApiProviderError);
  });
});

describe('runtime gate in the Messages API adapter', () => {
  it('forwards nothing unless consent is exactly true, and re-asks on every try', async () => {
    for (const verdict of [false, 1, undefined] as unknown[]) {
      endpoint.requests.length = 0;
      await expect(call(make(config({ permitted: async () => verdict as boolean })))).rejects.toMatchObject({ code: 'egress-refused' });
      expect(endpoint.requests).toEqual([]);
    }
    let asked = 0;
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    await expect(call(make(config({ permitted: async () => ++asked === 1 })))).rejects.toMatchObject({ code: 'egress-refused', attempts: 2 });
    expect(endpoint.requests).toHaveLength(1);
  });
  it('refuses everything with no upstream configured, and a request the predicate rejects is never forwarded', async () => {
    await expect(call(make(config({ upstream: undefined as never })))).rejects.toMatchObject({ code: 'egress-refused' });
    expect(endpoint.requests).toEqual([]);
    const h = make(config());
    await call(h);                                   // starts the gate
    const gateUrl = h.gateUrl()!;
    endpoint.requests.length = 0;
    const res = await fetch(`${gateUrl}/v1/messages`, { method: 'POST', body: JSON.stringify({ model: 'x', tools: [] }) });
    expect(res.status).toBe(403);                    // not armed
    expect(endpoint.requests).toEqual([]);
  });
});

describe('accounting and budget', () => {
  it('honours retry-after, stops when it cannot fit the budget, and carries spent tokens as unknown after a timeout', async () => {
    const slept: number[] = [];
    endpoint.script({ kind: 'status', status: 429, retryAfter: '2' }, { kind: 'text', text: '{}' });
    const h = make(config({ sleep: async ms => { slept.push(ms); } }));
    await call(h);
    expect(slept).toEqual([2000]);
    endpoint.script({ kind: 'status', status: 529, retryAfter: '120' });
    await expect(call(make(config({ sleep: async ms => { slept.push(ms); } })))).rejects.toMatchObject({ code: 'rate-limited', attempts: 1, spentUnits: 0 });
    expect(slept).toEqual([2000]);
    endpoint.script({ kind: 'hang' });
    await expect(call(make(config({ retry: { maxAttempts: 3, baseDelayMs: 1, maxDelayMs: 2, budgetMs: 1000 } })))).rejects.toMatchObject({ code: 'deadline', spentUnits: null });
  });
  it('does not leak the abort listener on the caller signal', async () => {
    const controller = new AbortController();
    endpoint.script({ kind: 'status', status: 500 });
    await call(make(config()), controller.signal).catch(() => undefined);
    expect(getEventListeners(controller.signal, 'abort')).toHaveLength(0);
  });
});

describe('thinking profile', () => {
  it('off omits the field; adaptive and a budget add exactly one thinking field and the reply may carry thinking blocks', async () => {
    for (const [profile, field] of [['adaptive', { type: 'adaptive' }], [{ budgetTokens: 2048 }, { type: 'enabled', budget_tokens: 2048 }]] as const) {
      endpoint.requests.length = 0;
      await call(make(config({ thinking: profile })));
      const sent = JSON.parse(endpoint.requests[0]!.body) as Record<string, unknown>;
      expect(sent.thinking).toEqual(field);
      expect(Object.keys(sent).sort()).toEqual(['max_tokens', 'messages', 'model', 'output_config', 'stream', 'system', 'thinking']);
      expect(acceptMessagesApiRequest(endpoint.requests[0]!, { ...expectation, thinking: profile })).toEqual({ accepted: true, violations: [] });
      expect(acceptMessagesApiRequest(endpoint.requests[0]!, expectation).accepted).toBe(false);
    }
    expect(() => createMessagesApiGenerate(config({ thinking: { budgetTokens: 4000 } }))).toThrow(MessagesApiProviderError);   // must be below max_tokens
    expect(() => createMessagesApiGenerate(config({ thinking: { budgetTokens: 100 } }))).toThrow(MessagesApiProviderError);
  });
});
