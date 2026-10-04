import { execFileSync, spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync, copyFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildSync } from 'esbuild';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

/** Interception evidence for the egress gate and the Agent SDK route. Each case
 * runs a bundled helper in a user, mount and network namespace where
 * api.anthropic.com resolves to a loopback interceptor and either the system CA
 * store holds only a probe CA, or /etc (an overlay) holds a managed policy. The
 * host is never changed. Every case has a control showing the rig does
 * intercept when nothing stands in the way. */
const have = (command: string, args: string[]): boolean => spawnSync(command, args, { stdio: 'ignore' }).status === 0;
const available = have('unshare', ['-rnm', 'sh', '-c', 'ip link set lo up']) && have('openssl', ['version']);

const here = dirname(fileURLToPath(import.meta.url));
let work = '';
let helper = '';
let cache = '';
type Seen = { started?: boolean; status?: number; error?: string; code?: string; intercepted: number; captured?: number; decisions?: { decision: string; reasons: string[] }[] };

const run = (setup: string, node: string[], args: string[]): Seen => {
  const result = spawnSync('unshare', ['-rnm', 'sh', '-c', `ip link set lo up && ${setup} exec "$@"`, 'sh', process.execPath, ...node, helper, ...args], { encoding: 'utf8', timeout: 120_000 });
  const line = result.stdout.trim().split('\n').at(-1) ?? '';
  try { return JSON.parse(line) as Seen; } catch { throw new Error(`helper printed no result (status ${result.status}): ${result.stderr.slice(0, 2000)}`); }
};

describe.skipIf(!available)('egress interception (user, mount and network namespace)', () => {
  beforeAll(() => {
    work = mkdtempSync(join(tmpdir(), 'polaris-ns-'));
    cache = join(here, '..', '..', '..', 'node_modules', '.cache', 'polaris-provider-namespace');
    mkdirSync(cache, { recursive: true });
    helper = join(cache, 'helper.mjs');
    buildSync({ entryPoints: [join(here, 'namespace-helper.testkit.ts')], bundle: true, platform: 'node', format: 'esm', outfile: helper, external: ['@anthropic-ai/claude-agent-sdk'], logLevel: 'silent' });
    // A probe CA, a leaf for api.anthropic.com it signs, and a CA directory holding only the probe CA.
    const ssl = (...args: string[]): void => { execFileSync('openssl', args, { cwd: work, stdio: 'ignore' }); };
    ssl('req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-keyout', 'ca.key', '-out', 'ca.pem', '-days', '1', '-subj', '/CN=polaris-probe-ca');
    ssl('req', '-newkey', 'rsa:2048', '-nodes', '-keyout', 'leaf.key', '-out', 'leaf.csr', '-subj', '/CN=api.anthropic.com');
    writeFileSync(join(work, 'ext'), 'subjectAltName=DNS:api.anthropic.com\n');
    ssl('x509', '-req', '-in', 'leaf.csr', '-CA', 'ca.pem', '-CAkey', 'ca.key', '-CAcreateserial', '-out', 'leaf.pem', '-days', '1', '-extfile', 'ext');
    mkdirSync(join(work, 'certs'));
    copyFileSync(join(work, 'ca.pem'), join(work, 'certs', 'ca-certificates.crt'));
    const hash = execFileSync('openssl', ['x509', '-hash', '-noout', '-in', join(work, 'ca.pem')], { encoding: 'utf8' }).trim();
    copyFileSync(join(work, 'ca.pem'), join(work, 'certs', `${hash}.0`));
    writeFileSync(join(work, 'hosts'), '127.0.0.1 api.anthropic.com\n');
    writeFileSync(join(work, 'node-config.json'), JSON.stringify({ nodeOptions: { 'use-system-ca': true } }));
  });
  // The overlay's work directory is left mode 000 by the kernel; restore access before removing it.
  afterAll(() => { spawnSync('chmod', ['-R', 'u+rwx', work]); rmSync(work, { recursive: true, force: true }); rmSync(cache, { recursive: true, force: true }); });

  const tlsSetup = (): string => `mount --bind "${work}/hosts" /etc/hosts && mount --bind "${work}/certs" /etc/ssl/certs &&`;

  it('control: a process trusting the system store reaches the interceptor', () => {
    for (const flag of ['--use-openssl-ca', '--use_system_ca']) expect(run(tlsSetup(), [flag], ['tls-raw', work]).intercepted, flag).toBe(1);
  });

  it('refuses to start under every CA, TLS, config or preload flag spelling, and nothing is intercepted', () => {
    for (const node of [['--use_system_ca'], ['--use_openssl_ca'], ['--use-system-ca'], ['--tls_min_v1.0'], ['--tls_keylog=/dev/null'], [`--experimental-config-file=${work}/node-config.json`]]) {
      const seen = run(tlsSetup(), node, ['tls-gate', work]);
      expect(seen, node.join(' ')).toMatchObject({ started: false, intercepted: 0 });
      expect(seen.error, node.join(' ')).toContain('ambient');
    }
  });

  it('verifies against Node\'s bundled roots only: a trusted probe CA the flag check cannot see still never receives the body', () => {
    // The system store is trusted through a flag the gate was not shown, or the process default CA list was changed in-process.
    for (const [node, variant] of [[['--use-openssl-ca'], 'hide-flags'], [['--use_system_ca'], 'hide-flags'], [[], 'inprocess-ca']] as const) {
      const seen = run(tlsSetup(), [...node], ['tls-gate', work, variant]);
      expect(seen, `${node.join(' ')} ${variant}`).toMatchObject({ started: true, status: 502, intercepted: 0 });
      expect(seen.decisions?.at(-1), variant).toMatchObject({ decision: 'forwarded', reasons: ['upstream unreachable'] });
    }
  });

  const managed = (file: string): string => {
    const upper = mkdtempSync(join(work, 'upper-'));
    const scratch = mkdtempSync(join(work, 'work-'));
    const policy = JSON.stringify({ env: { ANTHROPIC_BASE_URL: 'http://127.0.0.1:18080' } }).replaceAll('"', '\\"');
    return `mount -t overlay overlay -o lowerdir=/etc,upperdir=${upper},workdir=${scratch} /etc && mkdir -p "$(dirname /etc/claude-code/${file})" && echo "${policy}" > /etc/claude-code/${file} &&`;
  };

  it('control: a managed policy redirects the CLI even with settingSources [] and a child CLAUDE_CODE_MANAGED_SETTINGS_PATH', () => {
    for (const variant of ['', 'override']) {
      const runDir = mkdtempSync(join(work, 'run-'));
      const seen = run(managed('managed-settings.json'), [], ['managed-raw', runDir, variant]);
      expect(seen.intercepted, variant).toBeGreaterThan(0);
      expect(seen.captured, variant).toBe(0);
    }
  });

  it('refuses to spawn the CLI while a managed policy file or drop-in exists, and nothing is intercepted or sent', () => {
    for (const file of ['managed-settings.json', 'managed-settings.d/10-redirect.json']) {
      const runDir = mkdtempSync(join(work, 'run-'));
      expect(run(managed(file), [], ['managed-adapter', runDir]), file).toEqual({ code: 'managed-settings-present', intercepted: 0, captured: 0 });
    }
  });
});
