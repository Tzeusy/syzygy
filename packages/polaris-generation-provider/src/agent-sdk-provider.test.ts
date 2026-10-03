import { mkdtempSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { digestCanonicalJson, encodeCanonicalJson, promptForStage, runGenerationPipeline, type AttemptOutcome, type DispatchPermit, type PipelinePorts, type PipelineRequest } from '@syzygy/polaris-generation-core';
import { generationAnchorId, gitBlobObjectId, type GenerationSource } from '@syzygy/polaris-generation-core';
import { AGENT_SDK_BUILTIN_TOOLS, AgentSdkProviderError, agentSdkEnvironment, createAgentSdkGenerate, type AgentSdkAttemptRecord, type AgentSdkProviderConfig } from './agent-sdk-provider.js';
import { acceptCapturedRequest, acceptCapturedTraffic, isConnectivityProbe, SDK_FIXED_IDENTITY, type CapturedRequest, type ExpectedRequest } from './request-acceptance.js';
import { startCaptureEndpoint, startRecordingProxy, type CaptureEndpoint } from './capture-endpoint.testkit.js';

const DUMMY_KEY = 'sk-ant-dummy-capture-only';
const schema = { type: 'object', properties: { stage: { type: 'string' } }, required: ['stage'], additionalProperties: false };
const permit: DispatchPermit = { attemptId: 'attempt-1', maxUsageUnits: 100_000, maxOutputBytes: 20_000 };
const envelope = (): { system: string; input: string } => {
  const system = promptForStage('inventory').system;
  return { system, input: encodeCanonicalJson({ promptVersion: 'v', system, responseSchemaVersion: 's1', responseSchema: schema, inputs: { sources: [{ sourceId: 'a', text: 'Reduce recurring mental labor.' }] } }, { maxBytes: 100_000, maxNodes: 1000, maxDepth: 16 }) };
};

let endpoint: CaptureEndpoint;
let runDir: string;
beforeEach(async () => { endpoint = await startCaptureEndpoint(); runDir = mkdtempSync(join(tmpdir(), 'polaris-provider-')); });
afterEach(async () => { await endpoint.close(); rmSync(runDir, { recursive: true, force: true }); });

const config = (extra: Partial<AgentSdkProviderConfig> = {}): AgentSdkProviderConfig => ({
  runDir, model: 'claude-opus-5-5', auth: { apiKey: DUMMY_KEY }, baseUrl: endpoint.url,
  retry: { maxAttempts: 3, baseDelayMs: 1, maxDelayMs: 2, budgetMs: 10_000 }, ...extra,
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
      const env = agentSdkEnvironment(config(), 500);
      expect(Object.keys(env).sort()).toEqual([
        'ANTHROPIC_API_KEY', 'ANTHROPIC_BASE_URL', 'CLAUDE_CODE_ATTRIBUTION_HEADER', 'CLAUDE_CODE_DISABLE_AUTO_MEMORY', 'CLAUDE_CODE_DISABLE_CLAUDE_MDS',
        'CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC', 'CLAUDE_CODE_DISABLE_THINKING', 'CLAUDE_CODE_MAX_OUTPUT_TOKENS', 'CLAUDE_CODE_MAX_RETRIES', 'CLAUDE_CODE_SIMPLE',
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
      const handle = createAgentSdkGenerate(config({ diagnosticEnv: { HTTP_PROXY: proxy.url, HTTPS_PROXY: proxy.url, NO_PROXY: '127.0.0.1' } }));
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
      expect(reply).toEqual({ body: '{"stage":"inventory"}', model: 'capture-model', usageUnits: 49 });
      expect(readdirSync(handle.cwd)).toEqual([]);          // working directory stays empty
      expect(readdirSync(runDir).sort()).toEqual(['config', 'cwd', 'home', 'tmp', 'xdg-cache', 'xdg-config', 'xdg-data', 'xdg-state']);
      expect(proxy.hits).toEqual([]);                      // no proxy-honouring client tried another host
    } finally { await proxy.close(); }
  });

  it('rule 6: the acceptance predicate rejects each injected or altered field', async () => {
    const e = envelope();
    endpoint.script({ kind: 'text', text: '{}' });
    await call(createAgentSdkGenerate(config()), e);
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
    const handle = createAgentSdkGenerate(config());
    writeFileSync(join(handle.cwd, 'CLAUDE.md'), 'injected');
    await expect(call(handle, envelope())).rejects.toMatchObject({ code: 'cwd-not-empty' });
    expect(endpoint.messages()).toHaveLength(0);
  });

  it('caps max_tokens at the smaller of the permit output and usage allowances', async () => {
    const e = envelope();
    const small = { ...permit, maxOutputBytes: 321 };
    await createAgentSdkGenerate(config()).generate({ permit: small, stage: 'inventory', system: e.system, input: e.input, responseSchema: schema, signal: new AbortController().signal });
    expect((JSON.parse(endpoint.messages()[0]!.body) as { max_tokens: number }).max_tokens).toBe(321);
  });
});

describe('captured request (schema-tool mode)', () => {
  it('adds exactly the SDK StructuredOutput tool carrying the stage schema, and nothing else', async () => {
    const e = envelope();
    endpoint.script({ kind: 'tool', name: 'StructuredOutput', input: { stage: 'inventory' } });
    const reply = await call(createAgentSdkGenerate(config({ outputMode: 'schema-tool' })), e);
    expect(acceptCapturedRequest(endpoint.messages()[0]!, expectation(e, { responseSchema: schema }))).toEqual({ accepted: true, violations: [] });
    expect(acceptCapturedRequest(endpoint.messages()[0]!, expectation(e)).accepted).toBe(false);
    expect(JSON.parse(reply.body)).toEqual({ stage: 'inventory' });
  });
});

describe('retry and receipts', () => {
  it('retries 429 then 529 and reports every try, billing only what the CLI reported', async () => {
    const seen: AgentSdkAttemptRecord[] = [];
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 529 }, { kind: 'text', text: '{"stage":"inventory"}', inputTokens: 5, outputTokens: 3 });
    const handle = createAgentSdkGenerate(config({ onAttempt: r => seen.push(r) }));
    const reply = await call(handle, envelope());
    expect(endpoint.messages()).toHaveLength(3);
    expect(seen).toEqual(handle.attempts());
    expect(seen.map(r => [r.try, r.outcome, r.httpStatus, r.usageUnits])).toEqual([[1, 'rate-limited', 429, 0], [2, 'overloaded', 529, 0], [3, 'completed', null, 8]]);
    expect(seen.map(r => r.backoffMs)).toEqual([1, 2, 0]);
    expect(reply.usageUnits).toBe(8);
    for (const r of endpoint.messages()) expect(acceptCapturedRequest(r, expectation(envelope())).accepted).toBe(true);
  });

  it('throws rate-limited with the try count when attempts are exhausted, and does not retry other statuses', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'status', status: 429 }, { kind: 'status', status: 429 });
    await expect(call(createAgentSdkGenerate(config()), envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 3, status: 429 });
    expect(endpoint.messages()).toHaveLength(3);
    endpoint.requests.length = 0;
    endpoint.script({ kind: 'status', status: 500 });
    await expect(call(createAgentSdkGenerate(config()), envelope())).rejects.toMatchObject({ code: 'provider-error' });
    expect(endpoint.messages()).toHaveLength(1);
  });

  it('stops retrying when the next backoff would exceed the run budget', async () => {
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    const handle = createAgentSdkGenerate(config({ retry: { maxAttempts: 5, baseDelayMs: 5_000, maxDelayMs: 5_000, budgetMs: 100 } }));
    await expect(call(handle, envelope())).rejects.toMatchObject({ code: 'rate-limited', attempts: 1 });
    expect(endpoint.messages()).toHaveLength(1);
    expect(handle.attempts().map(r => r.backoffMs)).toEqual([0]);
  });

  it('aborts during a backoff sleep without sending another request', async () => {
    const controller = new AbortController();
    endpoint.script({ kind: 'status', status: 429 }, { kind: 'text', text: '{}' });
    const handle = createAgentSdkGenerate(config({ retry: { maxAttempts: 3, baseDelayMs: 30_000, maxDelayMs: 30_000, budgetMs: 120_000 }, sleep: async (_ms, signal) => { controller.abort(); if (signal.aborted) throw new AgentSdkProviderError('aborted', 0); } }));
    await expect(call(handle, envelope(), controller.signal)).rejects.toMatchObject({ code: 'aborted' });
    expect(endpoint.messages()).toHaveLength(1);
  });
});

describe('abort', () => {
  it('rejects promptly mid-response and closes the connection', async () => {
    endpoint.script({ kind: 'hang' });
    const controller = new AbortController();
    const handle = createAgentSdkGenerate(config());
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
    await expect(call(createAgentSdkGenerate(config()), envelope(), controller.signal)).rejects.toMatchObject({ code: 'aborted' });
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
      budget: { maxCalls: 10, maxInputBytes: 200_000, maxOutputBytes: 20_000, maxUsageUnits: 100_000, maxElapsedMs: 120_000, maxRepairCycles: 0, accountingPolicy: 'agent-sdk-tokens-v1' },
      sources: [source()], readerQuestions: ['Why does this project exist?'], requestedAssets: [],
    };
    const handle = createAgentSdkGenerate(config());
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
    expect(outcomes.map(o => o.kind === 'validated' ? o.usageUnits : -1)).toEqual([110, 110, 110, 110, 110]);
    expect(digestCanonicalJson({ ok: true }, { maxBytes: 100, maxNodes: 10, maxDepth: 4 }).digest).toMatch(/^[0-9a-f]{64}$/);
  });
});
