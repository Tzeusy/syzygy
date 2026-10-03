import { mkdtempSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { getEventListeners } from 'node:events';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { digestCanonicalJson, encodeCanonicalJson, promptForStage, runGenerationPipeline, type AttemptOutcome, type DispatchPermit, type PipelinePorts, type PipelineRequest } from '@syzygy/polaris-generation-core';
import { generationAnchorId, gitBlobObjectId, type GenerationSource } from '@syzygy/polaris-generation-core';
import { AGENT_SDK_BUILTIN_TOOLS, AgentSdkProviderError, agentSdkEnvironment, createAgentSdkGenerate, type AgentSdkAttemptRecord, type AgentSdkProviderConfig } from './agent-sdk-provider.js';
import { acceptCapturedRequest, acceptCapturedTraffic, isConnectivityProbe, SDK_FIXED_IDENTITY, type CapturedRequest, type ExpectedRequest } from './request-acceptance.js';
import { LOOPBACK_FOR_TESTS } from './egress-gate.js';
import { startCaptureEndpoint, startRecordingProxy, type CaptureEndpoint } from './capture-endpoint.testkit.js';

const DUMMY_KEY = 'sk-ant-dummy-capture-only';
const schema = { type: 'object', properties: { stage: { type: 'string' } }, required: ['stage'], additionalProperties: false };
const permit: DispatchPermit = { attemptId: 'attempt-1', maxUsageUnits: 100_000, maxOutputBytes: 20_000 };
const envelope = (): { system: string; input: string } => {
  const system = promptForStage('inventory').system;
  return { system, input: encodeCanonicalJson({ promptVersion: 'v', system, responseSchemaVersion: 's1', responseSchema: schema, inputs: { sources: [{ sourceId: 'a', text: 'Reduce recurring mental labor.' }] } }, { maxBytes: 100_000, maxNodes: 1000, maxDepth: 16 }) };
};

const handles: { close: () => Promise<void> }[] = [];
const make = (c: AgentSdkProviderConfig) => { const h = createAgentSdkGenerate(c); handles.push(h); return h; };
let endpoint: CaptureEndpoint;
let runDir: string;
beforeEach(async () => { endpoint = await startCaptureEndpoint(); runDir = mkdtempSync(join(tmpdir(), 'polaris-provider-')); });
afterEach(async () => { for (const h of handles.splice(0)) await h.close(); await endpoint.close(); rmSync(runDir, { recursive: true, force: true }); });

const config = (extra: Partial<AgentSdkProviderConfig> = {}): AgentSdkProviderConfig => ({
  runDir, model: 'claude-opus-5-5', auth: { apiKey: DUMMY_KEY }, upstream: { url: endpoint.url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: async () => true,
  retry: { maxAttempts: 3, baseDelayMs: 1, maxDelayMs: 2, budgetMs: 60_000 }, ...extra,
});
const expectation = (e: { system: string; input: string }, over: Partial<ExpectedRequest> = {}): ExpectedRequest => ({
  model: 'claude-opus-5-5', system: e.system, input: e.input, effort: 'medium', maxTokens: Math.min(permit.maxOutputBytes, permit.maxUsageUnits), ...over,
});
const call = (handle: ReturnType<typeof createAgentSdkGenerate>, e: { system: string; input: string }, signal = new AbortController().signal) =>
  handle.generate({ permit, stage: 'inventory', system: e.system, input: e.input, responseSchema: schema, signal });

describe('environment', () => {
  it('is a closed list that inherits nothing from process.env and points every state path into the run directory', () => {
    process.env.SYZYGY_CANARY_SECRET = 'leak';
    try {
      const env = agentSdkEnvironment(config(), 'http://127.0.0.1:1', 500);
      expect(Object.keys(env).sort()).toEqual([
        'ANTHROPIC_API_KEY', 'ANTHROPIC_BASE_URL', 'CLAUDE_CODE_ATTRIBUTION_HEADER', 'CLAUDE_CODE_DISABLE_AUTO_MEMORY', 'CLAUDE_CODE_DISABLE_CLAUDE_MDS',
        'CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC', 'CLAUDE_CODE_MAX_OUTPUT_TOKENS', 'CLAUDE_CODE_MAX_RETRIES', 'CLAUDE_CODE_SIMPLE',
        'CLAUDE_CONFIG_DIR', 'DISABLE_AUTOUPDATER', 'DISABLE_ERROR_REPORTING', 'DISABLE_TELEMETRY', 'HOME', 'TMPDIR',
        'XDG_CACHE_HOME', 'XDG_CONFIG_HOME', 'XDG_DATA_HOME', 'XDG_STATE_HOME']);
      expect(env.DISABLE_TELEMETRY).toBe('1');
      expect(env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC).toBe('1');
      for (const key of ['HOME', 'CLAUDE_CONFIG_DIR', 'TMPDIR', 'XDG_CONFIG_HOME', 'XDG_CACHE_HOME', 'XDG_DATA_HOME', 'XDG_STATE_HOME']) expect(env[key]!.startsWith(runDir + '/')).toBe(true);
    } finally { delete process.env.SYZYGY_CANARY_SECRET; }
  });
  it('rejects a relative run directory and an empty credential', () => {
    expect(() => createAgentSdkGenerate({ ...config(), runDir: 'relative' })).toThrow(AgentSdkProviderError);
    expect(() => createAgentSdkGenerate({ ...config(), auth: { apiKey: '' } })).toThrow(AgentSdkProviderError);
  });
});

describe('captured request (text mode)', () => {
  it('is exactly the generator bytes plus the closed set of SDK-fixed fields, with no tools, no context and nothing outside the run directory', async () => {
    const proxy = await startRecordingProxy();
    try {
      const e = envelope();
      endpoint.script({ kind: 'text', text: '{"stage":"inventory"}', inputTokens: 40, outputTokens: 9 });
      const handle = make(config({ diagnosticEnv: { HTTP_PROXY: proxy.url, HTTPS_PROXY: proxy.url, NO_PROXY: '127.0.0.1' } }));
      const reply = await call(handle, e);
      expect(endpoint.messages()).toHaveLength(1);
      const captured = endpoint.messages()[0]!;
      expect(acceptCapturedRequest(captured, expectation(e))).toEqual({ accepted: true, violations: [] });
      expect(acceptCapturedTraffic(endpoint.requests, expectation(e))).toEqual({ accepted: true, violations: [] });
      const body = JSON.parse(captured.body) as Record<string, any>;
      expect(body.system.map((s: { text: string }) => s.text)).toEqual([SDK_FIXED_IDENTITY, e.system]);
      expect(body.messages[0].content[0].text).toBe(e.input);
      expect(body.tools).toEqual([]);
      expect(captured.body).not.toContain(runDir);       // no cwd, home or config path in the request
      expect(captured.body).not.toContain('# Environment');
      expect(captured.body).not.toContain('CLAUDE.md');
      expect(reply).toEqual({ body: '{"stage":"inventory"}', model: 'capture-model', usageUnits: 1 });   // 49 tokens round up to one unit
      expect(readdirSync(handle.cwd)).toEqual([]);          // working directory stays empty
      expect(readdirSync(runDir).sort()).toEqual(['config', 'cwd', 'home', 'tmp', 'xdg-cache', 'xdg-config', 'xdg-data', 'xdg-state']);
      expect(proxy.hits).toEqual([]);                      // no proxy-honouring client tried another host
    } finally { await proxy.close(); }
  });

  it('rule 6: the acceptance predicate rejects each injected or altered field', async () => {
    const e = envelope();
    endpoint.script({ kind: 'text', text: '{}' });
    await call(make(config()), e);
    const good = endpoint.messages()[0]!;
    const body = JSON.parse(good.body) as Record<string, any>;
    const mutate = (edit: (b: Record<string, any>) => void): CapturedRequest => { const b = structuredClone(body); edit(b); return { ...good, body: JSON.stringify(b) }; };
    const mutants: [string, CapturedRequest, string][] = [
      ['extra system block', mutate(b => b.system.push({ type: 'text', text: 'x' })), 'system'],
      ['environment message', mutate(b => b.messages.push({ role: 'user', content: '# Environment' })), 'messages'],
      ['tool present', mutate(b => { b.tools = [{ name: 'Bash' }]; }), 'tools'],
      ['edited generator system', mutate(b => { b.system[1].text += ' '; }), 'system'],
      ['edited generator input', mutate(b => { b.messages[0].content[0].text += ' '; }), 'messages'],
      ['extra body field', mutate(b => { b.safeguards = []; }), 'unlisted body field safeguards'],
      ['thinking field', mutate(b => { b.thinking = { type: 'adaptive' }; }), 'unlisted body field thinking'],
      ['extra metadata key', mutate(b => { b.metadata.email = 'a@b'; }), 'metadata'],
      ['account uuid filled', mutate(b => { b.metadata.user_id = b.metadata.user_id.replace('"account_uuid":""', '"account_uuid":"u-1"'); }), 'metadata'],
      ['model drift', mutate(b => { b.model = 'other'; }), 'model'],
      ['unlisted header', { ...good, headers: { ...good.headers, 'x-extra': '1' } }, 'unlisted header x-extra'],
      ['wrong endpoint', { ...good, url: '/v1/complete' }, 'endpoint'],
      ['timeout value drift', { ...good, headers: { ...good.headers, 'x-stainless-timeout': '601' } }, 'header x-stainless-timeout'],
      ['connection value drift', { ...good, headers: { ...good.headers, connection: 'close' } }, 'header connection'],
    ];
    for (const [name, mutant, expected] of mutants) {
      const verdict = acceptCapturedRequest(mutant, expectation(e));
      expect(verdict.accepted, name).toBe(false);
      expect(verdict.violations.join(' | '), name).toContain(expected);
    }
    expect(acceptCapturedRequest(good, expectation(e, { effort: 'high' })).accepted).toBe(false);
    expect(acceptCapturedRequest(good, expectation(e, { maxTokens: 1 })).accepted).toBe(false);
    expect(acceptCapturedRequest({ ...good, body: 'not json' }, expectation(e)).accepted).toBe(false);
  });

  it('refuses to send when something else has written into the working directory', async () => {
    const handle = make(config());
    writeFileSync(join(handle.cwd, 'CLAUDE.md'), 'injected');
    await expect(call(handle, envelope())).rejects.toMatchObject({ code: 'cwd-not-empty' });
    expect(endpoint.messages()).toHaveLength(0);
  });

  it('caps max_tokens at the smaller of the permit output and usage allowances', async () => {
    const e = envelope();
    const small = { ...permit, maxOutputBytes: 321 };
    await make(config()).generate({ permit: small, stage: 'inventory', system: e.system, input: e.input, responseSchema: schema, signal: new AbortController().signal });
    expect((JSON.parse(endpoint.messages()[0]!.body) as { max_tokens: number }).max_tokens).toBe(321);
  });
});

describe('usage ceiling (dossier-units-v1)', () => {
  it('refuses before arming or sending when the permit leaves no room for one output token', async () => {
    const e = envelope();
    const room = Buffer.byteLength(e.system) + Buffer.byteLength(e.input);
    const h = make(config());
    await expect(h.generate({ permit: { ...permit, maxUsageUnits: Math.floor(room / 1000) }, stage: 'inventory', system: e.system, input: e.input, responseSchema: schema, signal: new AbortController().signal }))
      .rejects.toMatchObject({ code: 'budget-too-small', attempts: 0 });
    expect(endpoint.requests).toHaveLength(0);
    expect(h.attempts()).toHaveLength(0);
  });
  it('sends max_tokens so that input bytes plus output tokens fit the unit ceiling', async () => {
    const e = envelope();
    const bytes = Buffer.byteLength(e.system) + Buffer.byteLength(e.input);
    const units = Math.ceil((bytes + 700) / 1000);
    await make(config()).generate({ permit: { ...permit, maxUsageUnits: units, maxOutputBytes: 1_000_000 }, stage: 'inventory', system: e.system, input: e.input, responseSchema: schema, signal: new AbortController().signal });
    const sent = (JSON.parse(endpoint.messages()[0]!.body) as { max_tokens: number }).max_tokens;
    expect(sent).toBe(units * 1000 - bytes);
    expect(bytes + sent).toBeLessThanOrEqual(units * 1000);
  });
});

describe('version pin', () => {
  it('refuses an unpinned SDK at construction and fails a call whose CLI reports another version', async () => {
    expect(() => createAgentSdkGenerate(config({ pin: { sdk: '0.0.1', cli: '2.1.288' } }))).toThrow(AgentSdkProviderError);
    await expect(call(make(config({ pin: { sdk: '0.3.288', cli: '9.9.9' } })), envelope())).rejects.toMatchObject({ code: 'unpinned-version' });
    // Detection, not prevention: the CLI announces its version as it starts the request, so the construction-time SDK pin (which fixes the CLI binary) is the gate.
  });
  it('lets the profile lower the output cap', async () => {
    await call(make(config({ maxOutputTokens: 777 })), envelope());
    expect((JSON.parse(endpoint.messages()[0]!.body) as { max_tokens: number }).max_tokens).toBe(777);
  });
});

describe('captured request (schema-tool mode)', () => {
  it('adds exactly the SDK StructuredOutput tool carrying the stage schema, and nothing else', async () => {
    const e = envelope();
    endpoint.script({ kind: 'tool', name: 'StructuredOutput', input: { stage: 'inventory' } });
    const reply = await call(make(config({ outputMode: 'schema-tool' })), e);
    expect(acceptCapturedRequest(endpoint.messages()[0]!, expectation(e, { responseSchema: schema }))).toEqual({ accepted: true, violations: [] });
    expect(acceptCapturedRequest(endpoint.messages()[0]!, expectation(e)).accepted).toBe(false);
    expect(JSON.parse(reply.body)).toEqual({ stage: 'inventory' });
  });
});

describe('retry and receipts', () => {
  it('retries 429 then 529 and reports every try, billing only what the CLI reported', async () => {
    const seen: AgentSdkAttemptRecord[] = [];
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 529 }, { kind: 'text', text: '{"stage":"inventory"}', inputTokens: 5, outputTokens: 3 });
    const handle = make(config({ onAttempt: r => seen.push(r) }));
    const reply = await call(handle, envelope());
    expect(endpoint.messages()).toHaveLength(3);
    expect(seen).toEqual(handle.attempts());
    expect(seen.map(r => [r.try, r.outcome, r.httpStatus, r.usageUnits])).toEqual([[1, 'rate-limited', 429, 0], [2, 'overloaded', 529, 0], [3, 'completed', null, 1]]);
    expect(seen.map(r => r.backoffMs)).toEqual([1, 2, 0]);
    expect(reply.usageUnits).toBe(1);
    for (const r of endpoint.messages()) expect(acceptCapturedRequest(r, expectation(envelope())).accepted).toBe(true);
  });

  it('throws rate-limited with the try count when attempts are exhausted, and does not retry other statuses', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 429 }, { kind: 'status', status: 429 });
    await expect(call(make(config()), envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 3, status: 429 });
    expect(endpoint.messages()).toHaveLength(3);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 500 });
    await expect(call(make(config()), envelope())).rejects.toMatchObject({ code: 'provider-error' });
    expect(endpoint.messages()).toHaveLength(1);
  });

  it('stops retrying when the next backoff would exceed the run budget', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    const handle = make(config({ retry: { maxAttempts: 5, baseDelayMs: 5_000, maxDelayMs: 5_000, budgetMs: 4_000 } }));
    await expect(call(handle, envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 1 });
    expect(endpoint.messages()).toHaveLength(1);
    expect(handle.attempts().map(r => r.backoffMs)).toEqual([0]);
  });

  it('aborts during a backoff sleep without sending another request', async () => {
    const controller = new AbortController();
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    const handle = make(config({ retry: { maxAttempts: 3, baseDelayMs: 30_000, maxDelayMs: 30_000, budgetMs: 120_000 }, sleep: async (_ms, signal) => { controller.abort(); if (signal.aborted) throw new AgentSdkProviderError('aborted', 0); } }));
    await expect(call(handle, envelope(), controller.signal)).rejects.toMatchObject({ code: 'aborted' });
    expect(endpoint.messages()).toHaveLength(1);
  });
});

describe('abort', () => {
  it('rejects promptly mid-response and closes the connection', async () => {
    endpoint.script({ kind: 'hang' });
    const controller = new AbortController();
    const handle = make(config());
    const pending = call(handle, envelope(), controller.signal);
    const assertion = expect(pending).rejects.toMatchObject({ code: 'aborted' });
    for (let i = 0; i < 200 && endpoint.messages().length === 0; i++) await new Promise(r => setTimeout(r, 50));
    expect(endpoint.messages()).toHaveLength(1);
    const t0 = Date.now();
    controller.abort();
    await assertion;
    expect(Date.now() - t0).toBeLessThan(10_000);
    for (let i = 0; i < 100 && endpoint.closedWhileHanging() === 0; i++) await new Promise(r => setTimeout(r, 50));
    expect(endpoint.closedWhileHanging()).toBe(1);
    expect(handle.attempts().at(-1)?.outcome).toBe('aborted');
  });
  it('does not start when the signal is already aborted', async () => {
    const controller = new AbortController();
    controller.abort();
    await expect(call(make(config()), envelope(), controller.signal)).rejects.toMatchObject({ code: 'aborted' });
    expect(endpoint.messages()).toHaveLength(0);
  });
});

describe('through the pipeline', () => {
  const source = (): GenerationSource => {
    const body = 'Reduce recurring mental labor.';
    const base = { repositoryId: 'synthetic:project-a', revision: 'a'.repeat(40), path: 'synthetic/purpose.md', objectId: gitBlobObjectId(body) };
    const end = Buffer.byteLength(body);
    return { ...base, sourceId: 'purpose', evaluationId: 'evaluation:fixture', classificationBasis: 'body', exclusion: { excluded: false }, body,
      spans: [{ anchorId: generationAnchorId(base, 0, end), start: 0, end, text: body }] };
  };
  it('sends every stage as built by the generator and maps usage into the receipts', async () => {
    const request: PipelineRequest = {
      requestId: 'r1', projectId: 'project-a', snapshotId: 's1', startedAt: Date.now(),
      routes: { inventory: 'agent-sdk', plan: 'agent-sdk', author: 'agent-sdk', edit: 'agent-sdk', fidelity: 'agent-sdk', repair: 'agent-sdk' },
      budget: { maxCalls: 10, maxInputBytes: 200_000, maxOutputBytes: 20_000, maxUsageUnits: 100_000, maxElapsedMs: 120_000, maxRepairCycles: 0, accountingPolicy: 'dossier-units-v1' },
      sources: [source()], readerQuestions: [{ id: 'why', topics: [], text: 'Why does this project exist?' }], requestedAssets: [],
    };
    const handle = make(config());
    const outcomes: AttemptOutcome[] = [];
    let ordinal = 0;
    const ports: PipelinePorts = {
      now: () => Date.now(), verifySources: async () => true, permissionIdentity: async () => 'fixture',
      admit: async () => ({ kind: 'reserved', permit: { attemptId: `a${ordinal++}`, maxUsageUnits: 50_000, maxOutputBytes: 5_000 } }),
      permitted: async () => true, releaseUnsent: async () => undefined,
      responseSchema: () => ({ version: 'capture-v1', schema }),
      generate: handle.generate,
      validate: (stage, value) => { if ((value as { stage?: string }).stage !== stage) throw Error('schema'); return value; },
      record: async (_, outcome) => { outcomes.push(outcome); }, lateReceipt: async () => undefined, fidelity: () => ({ blocking: false, findings: [] }),
    };
    for (const stage of ['inventory', 'plan', 'author', 'edit', 'fidelity']) endpoint.script({ kind: 'text', text: JSON.stringify({ stage }), inputTokens: 100, outputTokens: 10 });
    const result = await runGenerationPipeline(request, ports, new AbortController().signal);
    expect(result.status).toBe('awaiting-rendered-review');
    expect(endpoint.messages()).toHaveLength(5);
    endpoint.messages().forEach((captured, index) => {
      const stage = (['inventory', 'plan', 'author', 'edit', 'fidelity'] as const)[index]!;
      const sent = JSON.parse(captured.body) as { system: { text: string }[]; messages: { content: { text: string }[] }[] };
      const built = JSON.parse(sent.messages[0]!.content[0]!.text) as { system: string; responseSchema: unknown };
      expect(built.system).toBe(promptForStage(stage).system);
      expect(acceptCapturedRequest(captured, expectation({ system: sent.system[1]!.text, input: sent.messages[0]!.content[0]!.text }, { maxTokens: 5_000 }))).toEqual({ accepted: true, violations: [] });
      expect(sent.system[1]!.text).toBe(promptForStage(stage).system);
    });
    expect(outcomes.map(o => o.kind === 'validated' ? o.usageUnits : -1)).toEqual([1, 1, 1, 1, 1]);   // 110 tokens per stage round up to one unit
    expect(digestCanonicalJson({ ok: true }, { maxBytes: 100, maxNodes: 10, maxDepth: 4 }).digest).toMatch(/^[0-9a-f]{64}$/);
  });
});

const fakeQuery = (runs: unknown[][], seen: { calls: number } = { calls: 0 }): NonNullable<AgentSdkProviderConfig['query']> => (() => {
  const messages = runs[Math.min(seen.calls++, runs.length - 1)]!;
  const iterator = (async function* () { for (const m of messages) yield m; })();
  return Object.assign(iterator, { close: () => undefined });
}) as unknown as NonNullable<AgentSdkProviderConfig['query']>;
const resultMessage = (over: Record<string, unknown> = {}): Record<string, unknown> => ({ type: 'result', subtype: 'success', is_error: false, result: '{}', usage: { input_tokens: 1, output_tokens: 1 }, ...over });

describe('runtime gate in the adapter', () => {
  it('forwards nothing when consent is not exactly true, and reports egress-refused', async () => {
    for (const verdict of [false, 1, 'true', undefined] as unknown[]) {
      endpoint.requests.length = 0;
      const h = make(config({ permitted: async () => verdict as boolean }));
      await expect(call(h, envelope())).rejects.toMatchObject({ code: 'egress-refused' });
      expect(endpoint.requests).toEqual([]);
      expect(h.gateDecisions().some(d => d.decision === 'refused' && d.reasons.includes('consent not permitted'))).toBe(true);
    }
  });
  it('re-asks consent on every try: a withdrawal after the first request stops the retry', async () => {
    let asked = 0;
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    const h = make(config({ permitted: async () => ++asked === 1 }));
    await expect(call(h, envelope())).rejects.toMatchObject({ code: 'egress-refused', attempts: 2 });
    expect(endpoint.messages()).toHaveLength(1);
  });
  it('refuses everything when no upstream is configured', async () => {
    const h = make(config({ upstream: undefined as never }));
    await expect(call(h, envelope())).rejects.toMatchObject({ code: 'egress-refused' });
    expect(endpoint.requests).toEqual([]);
  });
  it('refuses, at construction, a loopback upstream without the test-only token and any other non-provider upstream (production wiring)', async () => {
    for (const url of [endpoint.url, 'https://evil.test', 'http://api.anthropic.com']) {
      expect(() => make(config({ upstream: { url } })), url).toThrow(AgentSdkProviderError);
    }
    expect(endpoint.requests).toEqual([]);
  });
  it('answers the connectivity probe locally and never forwards it', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 429 }, { kind: 'status', status: 429 });
    const h = make(config());
    await call(h, envelope()).catch(() => undefined);
    expect(endpoint.requests.every(r => r.method === 'POST')).toBe(true);
    expect(h.gateDecisions().filter(d => d.decision === 'answered-locally').every(d => d.method === 'HEAD' && d.url === '/api/hello')).toBe(true);
  });
  it('rejects a second concurrent call', async () => {
    endpoint.script({ kind: 'hang' });
    const controller = new AbortController();
    const h = make(config());
    const first = call(h, envelope(), controller.signal).catch(() => undefined);
    for (let i = 0; i < 200 && endpoint.messages().length === 0; i++) await new Promise(r => setTimeout(r, 50));
    await expect(call(h, envelope())).rejects.toMatchObject({ code: 'concurrent-call' });
    controller.abort(); await first;
  });
});

describe('diagnostic environment', () => {
  it('admits only proxy variables and refuses any name the adapter sets or could abuse', () => {
    for (const key of ['ANTHROPIC_BASE_URL', 'ANTHROPIC_API_KEY', 'HOME', 'LD_PRELOAD', 'NODE_OPTIONS', 'PATH', 'DISABLE_TELEMETRY']) {
      expect(() => createAgentSdkGenerate(config({ diagnosticEnv: { [key]: 'x' } })), key).toThrow(AgentSdkProviderError);
    }
    expect(() => createAgentSdkGenerate(config({ diagnosticEnv: { HTTP_PROXY: 'http://127.0.0.1:1', HTTPS_PROXY: 'http://127.0.0.1:1', NO_PROXY: '127.0.0.1' } }))).not.toThrow();
  });
});

describe('accounting and budget', () => {
  it('counts a reply that reports no usage at the full ceiling its permit allowed, never at zero', async () => {
    const noUsage = resultMessage({ usage: undefined });
    const h = make(config({ query: fakeQuery([[noUsage]]) }));
    expect((await call(h, envelope())).usageUnits).toBe(permit.maxUsageUnits);
    expect(h.attempts()[0]!.usageUnits).toBeNull();   // the attempt record keeps the Unknown
  });
  it('makes no further try after a rejected try whose billing is unknown', async () => {
    const rateLimited = (usage: unknown) => resultMessage({ is_error: true, api_error_status: 429, usage });
    const h = make(config({ query: fakeQuery([[rateLimited(undefined)], [resultMessage()]]) }));
    await expect(call(h, envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 1, spentUnits: null });
    expect(h.attempts()).toHaveLength(1);
  });
  it('counts a rejected try as unbilled only on the provider\'s documented error body', async () => {
    endpoint.script({ kind: 'status', status: 429, body: '{"oops":1}' }, { kind: 'text', text: '{}' });
    const h = make(config());
    await expect(call(h, envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 1, spentUnits: null });
    expect(h.attempts()[0]!.usageUnits).toBeNull();
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    expect((await call(make(config()), envelope())).usageUnits).toBe(1);
  });
  it('strips the OS, architecture and runtime-version headers only when the profile says so', async () => {
    await call(make(config({ stripFingerprint: true })), envelope());
    await call(make(config()), envelope());
    const [stripped, kept] = endpoint.messages();
    for (const name of ['x-stainless-os', 'x-stainless-arch', 'x-stainless-runtime-version']) {
      expect(stripped!.headers[name]).toBeUndefined();
      expect(kept!.headers[name]).toBeDefined();
    }
    expect(stripped!.headers['user-agent']).toBe(kept!.headers['user-agent']);
  });
  it('carries the tokens spent on the final error', async () => {
    const limited = resultMessage({ is_error: true, api_error_status: 429, usage: { input_tokens: 3, output_tokens: 2 } });
    await expect(call(make(config({ query: fakeQuery([[limited]]) })), envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 1, spentUnits: null });   // the CLI's own usage is not evidence a rejected request was unbilled, and an unknown try ends the call
  });
  it('honours retry-after over the computed backoff, and stops when it cannot fit the budget', async () => {
    const slept: number[] = [];
    endpoint.script({ kind: 'status', status: 429, retryAfter: '2' }, { kind: 'text', text: '{}' });
    const h = make(config({ sleep: async ms => { slept.push(ms); } }));
    await call(h, envelope());
    expect(slept).toEqual([2000]);
    expect(h.attempts()[0]!.backoffMs).toBe(2000);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 529, retryAfter: '120' }, { kind: 'text', text: '{}' });
    const g = make(config({ sleep: async ms => { slept.push(ms); } }));
    await expect(call(g, envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 1 });
    expect(slept).toEqual([2000]);
  });
  it('bounds each try by the remaining budget', async () => {
    endpoint.script({ kind: 'hang' });
    const t0 = Date.now();
    await expect(call(make(config({ retry: { maxAttempts: 3, baseDelayMs: 1, maxDelayMs: 2, budgetMs: 1500 } })), envelope())).rejects.toMatchObject({ code: 'deadline', spentUnits: null });   // a timed-out try's usage is unknown, never zero
    expect(Date.now() - t0).toBeLessThan(12_000);
  });
  it('does not leak the abort listener when query() throws synchronously', async () => {
    const controller = new AbortController();
    const throwing = (() => { throw new Error('spawn failed'); }) as unknown as NonNullable<AgentSdkProviderConfig['query']>;
    await expect(call(make(config({ query: throwing })), envelope(), controller.signal)).rejects.toMatchObject({ code: 'transport-failed' });
    expect(getEventListeners(controller.signal, 'abort')).toHaveLength(0);
  });
});

describe('thinking profile', () => {
  it('off sends no thinking field; adaptive adds exactly thinking, context_management and one beta entry', async () => {
    const e = envelope();
    await call(make(config({ thinking: 'adaptive', effort: 'high' })), e);
    const captured = endpoint.messages()[0]!;
    const body = JSON.parse(captured.body) as Record<string, unknown>;
    expect(body.thinking).toEqual({ type: 'adaptive', display: 'updates' });
    expect(body.context_management).toEqual({ edits: [{ type: 'clear_thinking_20251015', keep: 'all' }] });
    expect(captured.headers['anthropic-beta']).toMatch(/,thinking-display-updates-2026-08-18$/);
    expect(acceptCapturedRequest(captured, expectation(e, { thinking: 'adaptive', effort: 'high' }))).toEqual({ accepted: true, violations: [] });
    expect(acceptCapturedRequest(captured, expectation(e, { thinking: 'off', effort: 'high' })).accepted).toBe(false);
  });
});

describe('header values', () => {
  it('rule 6: the acceptance predicate rejects an altered header value', async () => {
    const e = envelope();
    await call(make(config()), e);
    const good = endpoint.messages()[0]!;
    const edits: [string, string, string][] = [
      ['anthropic-beta', 'x', 'anthropic-beta'], ['user-agent', 'curl/8', 'user-agent'], ['x-api-key', 'sk-other', 'x-api-key'],
      ['x-claude-code-session-id', '00000000-0000-0000-0000-000000000000', 'x-claude-code-session-id'], ['content-length', '1', 'content-length'],
      ['anthropic-version', '2024-01-01', 'anthropic-version'], ['x-stainless-os', 'Linux; rm -rf', 'x-stainless-os'],
    ];
    for (const [name, value, expected] of edits) {
      const verdict = acceptCapturedRequest({ ...good, headers: { ...good.headers, [name]: value } }, expectation(e, { apiKey: DUMMY_KEY }));
      expect(verdict.accepted, name).toBe(false);
      expect(verdict.violations.join('|'), name).toContain(expected);
    }
    expect(acceptCapturedRequest(good, expectation(e, { apiKey: DUMMY_KEY })).accepted).toBe(true);
  });
});
