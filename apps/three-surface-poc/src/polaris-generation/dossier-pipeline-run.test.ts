import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { DECISIONS_DIR, EGRESS_V2_INSTANCE, INSTANCES_DIR } from '@syzygy/polaris-generation-consent';
import { renderRecorderAct } from '@syzygy/polaris-generation-consent/testing';
import { createMessagesApiGenerate } from '@syzygy/polaris-generation-provider';
import { LOOPBACK_FOR_TESTS } from '@syzygy/polaris-generation-provider/testing';

import { main } from './dossier-main.js';
import { fixturePolicyActPort, fixtureRouteRoot } from './dossier-fixtures.testkit.js';
import type { ProviderFactory } from './dossier-generation.js';
import { EGRESS_V2_DIGEST } from './dossier-stage-authority.js';
import { startStubProvider } from './stub-provider.testkit.js';

let repo = '', commit = '';
beforeAll(() => {
  repo = mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-repo-'));
  const run = (...a: string[]): string => execFileSync('git', ['-C', repo, ...a], { encoding: 'utf8' }).trim();
  run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
  for (const [p, body] of Object.entries({ 'README.md': '# Fixture\nIt does a thing.\n', 'src/core.c': 'int core(void) { return 1; }\n' })) {
    mkdirSync(path.dirname(path.join(repo, p)), { recursive: true }); writeFileSync(path.join(repo, p), body);
  }
  run('add', '-A'); run('commit', '-qm', 'fixture'); commit = run('rev-parse', 'HEAD');
});
afterAll(() => rmSync(repo, { recursive: true, force: true }));


const REPO_ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../../../..');
const hex = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

/** A scratch Syzygy root in which the redis observation record (pinned to the fixture commit) and the real egress version 2 record are
 * in force by the recorders' own acts, plus the route's registry act. Nothing here is the repository's own decisions directory. */
function admissionRoot(route: 'messages-api'): string {
  const root = fixtureRouteRoot(route);
  const put = (rel: string, body: string): void => { mkdirSync(path.dirname(path.join(root, rel)), { recursive: true }); writeFileSync(path.join(root, rel), body); };
  const realObs = readFileSync(path.join(REPO_ROOT, INSTANCES_DIR, 'redis/OBSERVATION-CONSENT.md'), 'utf8');
  const obs = realObs.replace(/^\| `([^`\n]+)` \| `[0-9a-f]+` \|$/gm, (_m, label: string) => `| \`${label}\` | \`${commit}\` |`);
  const v2 = readFileSync(path.join(REPO_ROOT, EGRESS_V2_INSTANCE), 'utf8');
  put(`${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`, obs);
  put(EGRESS_V2_INSTANCE, v2);
  put(`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`, renderRecorderAct('redis-observation', hex(obs), '2026-09-01', '2026-09-01T09:30:00Z'));
  put(`${DECISIONS_DIR}/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md`, renderRecorderAct('egress-anthropic-v2', hex(v2), '2026-09-01', '2026-09-01T09:30:00Z'));
  return root;
}

const loopback = (url: string): ProviderFactory => build => createMessagesApiGenerate({ model: build.profile.model, apiKey: build.apiKey, upstream: { url, loopbackForTests: LOOPBACK_FOR_TESTS },
  permitted: build.permitted, effort: build.profile.effort, thinking: build.profile.thinking, maxOutputTokens: build.profile.maxOutputTokens });

describe('discovery of the request shapes', () => {
  it('prints the first stage requests', async () => {
    const seen: string[] = [];
    const stub = await startStubProvider((request, n) => { seen.push(`#${n} system=${request.system.slice(0, 60)} | input=${request.input.slice(0, 700)}`); return { text: '{}' }; });
    const root = admissionRoot('messages-api');
    const out = path.join(mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-out-')), 'run');
    const code = await main(['https://github.com/redis/redis', '--route', 'messages-api', '--out', out, '--json'], { lsRemote: () => `${commit}\tHEAD\n`, materialize: async () => repo, policyAct: fixturePolicyActPort() },
      { root, env: { SYZYGY_POLARIS_PROVIDER_API_KEY: 'sk-test-pipeline' }, providerFactory: loopback(stub.url), stdout: t => seen.push(t), stderr: t => seen.push(t) });
    await stub.close();
    console.log(code, seen.join('\n'));
  }, 60_000);
});
