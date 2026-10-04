import { execFileSync, spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildSync } from 'esbuild';
import { describe, expect, it } from 'vitest';

/** "No other hosts" evidence. The adapter runs in a network namespace that has
 * only a loopback interface, with its own capture endpoint inside it, under
 * strace. Nothing can leave the machine, and every socket address the CLI (and
 * its children) names is logged whether or not the connect succeeds. A positive
 * control proves the same rig would show a stray attempt. Paths not taken in
 * this run (error paths, long runs, login flows) are not covered. */
const have = (command: string, args: string[]): boolean => spawnSync(command, args, { stdio: 'ignore' }).status === 0;
const available = have('strace', ['-V']) && have('unshare', ['-rn', 'true']);

interface Endpoint { readonly kind: 'inet' | 'unix'; readonly address: string; readonly port: number | null; readonly syscall: string }
/** Every socket address a traced syscall names, from strace's text. */
export function socketAddresses(trace: string): Endpoint[] {
  const found: Endpoint[] = [];
  for (const line of trace.split('\n')) {
    const syscall = /^(?:\d+\s+)?(\w+)\(/.exec(line)?.[1] ?? '';
    for (const m of line.matchAll(/sa_family=AF_INET6?,[^}]*?sin6?_port=htons\((\d+)\)[^}]*?(?:inet_addr\("([^"]+)"\)|inet_pton\(AF_INET6, "([^"]+)")/g)) found.push({ kind: 'inet', address: (m[2] ?? m[3])!, port: Number(m[1]), syscall });
    for (const m of line.matchAll(/sa_family=AF_UNIX, sun_path="([^"]+)"/g)) found.push({ kind: 'unix', address: m[1]!, port: null, syscall });
  }
  return found;
}

const rig = (inner: string[]): { trace: string; stdout: string; status: number | null } => {
  const dir = mkdtempSync(join(tmpdir(), 'polaris-isolation-'));
  const log = join(dir, 'strace.log');
  const result = spawnSync('unshare', ['-rn', 'sh', '-c', `ip link set lo up && exec strace -f -qq -e trace=connect,sendto,sendmsg,sendmmsg -o "${log}" "$@"`, 'sh', ...inner], { encoding: 'utf8', timeout: 90_000 });
  let trace = '';
  try { trace = readFileSync(log, 'utf8'); } catch { /* no trace written */ }
  rmSync(dir, { recursive: true, force: true });
  return { trace, stdout: result.stdout, status: result.status };
};

describe('strace parser', () => {
  it('reports a stray inet address and ignores nothing it can read', () => {
    const trace = [
      '123   connect(24, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("160.79.104.10")}, 16) = -1 ENETUNREACH',
      '124   sendto(9, "x", 1, 0, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("10.0.0.2")}, 16) = -1 ENETUNREACH',
      '125   connect(5, {sa_family=AF_INET6, sin6_port=htons(443), sin6_flowinfo=htonl(0), inet_pton(AF_INET6, "2606:4700::1", &sin6_addr), sin6_scope_id=0}, 28) = -1 ENETUNREACH',
      '126   connect(6, {sa_family=AF_UNIX, sun_path="/run/x.sock"}, 20) = 0',
    ].join('\n');
    expect(socketAddresses(trace)).toEqual([
      { kind: 'inet', address: '160.79.104.10', port: 443, syscall: 'connect' },
      { kind: 'inet', address: '10.0.0.2', port: 53, syscall: 'sendto' },
      { kind: 'inet', address: '2606:4700::1', port: 443, syscall: 'connect' },
      { kind: 'unix', address: '/run/x.sock', port: null, syscall: 'connect' },
    ]);
  });
});

describe.skipIf(!available)('egress isolation (network namespace + strace)', () => {
  it('positive control: a connect to another host is visible in the trace and cannot succeed', () => {
    const control = rig(['node', '-e', "const s=require('net').connect(80,'192.0.2.1');s.on('error',()=>process.exit(0));setTimeout(()=>process.exit(0),3000)"]);
    expect(socketAddresses(control.trace).some(e => e.kind === 'inet' && e.address === '192.0.2.1' && e.port === 80)).toBe(true);
  });

  it.each(['agent-sdk', 'messages'])('the %s adapter names no socket address other than its capture endpoint, and its request is accepted', route => {
    const here = dirname(fileURLToPath(import.meta.url));
    const cache = join(here, '..', '..', '..', 'node_modules', '.cache', 'polaris-provider-isolation');
    mkdirSync(cache, { recursive: true });
    const helper = join(cache, 'helper.mjs');
    buildSync({ entryPoints: [join(here, 'isolation-helper.testkit.ts')], bundle: true, platform: 'node', format: 'esm', outfile: helper, external: ['@anthropic-ai/claude-agent-sdk'], logLevel: 'silent' });
    const runDir = mkdtempSync(join(tmpdir(), 'polaris-isolation-run-'));
    try {
      const run = rig([process.execPath, helper, runDir, route]);
      expect(run.status, run.stdout).toBe(0);
      const seen = JSON.parse(run.stdout.trim().split('\n').at(-1)!) as { port: number; gatePort: number; requests: string[]; verdict: { accepted: boolean; violations: string[] }; replyBody: string };
      expect(seen.verdict).toEqual({ accepted: true, violations: [] });
      const addresses = socketAddresses(run.trace);
      const inet = addresses.filter(a => a.kind === 'inet');
      // Denominator: the capture endpoint must appear, or the trace saw nothing.
      const own = (a: Endpoint): boolean => a.address === '127.0.0.1' && (a.port === seen.port || a.port === seen.gatePort);
      expect(inet.some(a => a.address === '127.0.0.1' && a.port === seen.port)).toBe(true);
      expect(inet.some(a => a.port === seen.gatePort)).toBe(true);   // the CLI reached the gate, not the endpoint directly
      expect(inet.filter(a => !own(a))).toEqual([]);
      // Unix sockets must live inside the run directory, apart from libc's local name-service cache socket (a lookup on this machine, not a network address).
      expect(addresses.filter(a => a.kind === 'unix' && !a.address.startsWith(runDir + '/') && a.address !== '/var/run/nscd/socket')).toEqual([]);
    } finally { rmSync(runDir, { recursive: true, force: true }); rmSync(cache, { recursive: true, force: true }); }
  });
});
