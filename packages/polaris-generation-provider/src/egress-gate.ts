import http from 'node:http';
import https from 'node:https';
import type { AddressInfo } from 'node:net';
import { isConnectivityProbe, type CapturedRequest, type RequestAcceptance } from './request-acceptance.js';

/** The single egress check, as code. Adapters point their client at this
 * in-process loopback server and never at a provider. A request is forwarded
 * only when (1) the current try armed an acceptance predicate that the exact
 * request satisfies, (2) the injected consent `permitted()` returns exactly
 * `true` now, and (3) an explicit upstream was configured. Anything else gets a
 * refusal and no byte leaves. The CLI's body-less connectivity probe is
 * answered here and never forwarded. */
export interface EgressGateOptions {
  /** Explicit allowRemote: the only host bytes may be forwarded to. Absent = every request is refused. */
  readonly upstream?: { readonly url: string; /** Test-only: allows a loopback upstream. Not exported from the package index, so production wiring cannot name it. */ readonly loopbackForTests?: typeof LOOPBACK_FOR_TESTS };
  /** Consent switch, asked for every request including retries. Only `true` permits. */
  readonly permitted: () => Promise<boolean>;
  /** Drop the machine-identifying `x-stainless-os`, `-arch` and `-runtime-version` headers before forwarding. Default false: bytes are forwarded as accepted. */
  readonly stripFingerprint?: boolean;
}

/** Capability token for tests that point the gate at a local capture endpoint. Deliberately absent from `index.ts`. */
export const LOOPBACK_FOR_TESTS: unique symbol = Symbol('loopback-upstream-for-tests');

const FINGERPRINT_HEADERS = ['x-stainless-os', 'x-stainless-arch', 'x-stainless-runtime-version'] as const;
const RATE_ERRORS: ReadonlySet<string> = new Set(['rate_limit_error', 'overloaded_error']);

export interface GateDecision {
  readonly method: string;
  readonly url: string;
  readonly decision: 'forwarded' | 'answered-locally' | 'refused';
  /** Content-free: predicate violation texts name fields, never values. */
  readonly reasons: readonly string[];
  readonly upstreamStatus: number | null;
  /** For a 429/529: the provider's documented error type (`rate_limit_error`, `overloaded_error`) read from the response body, else null. Evidence that the request was rejected unbilled. */
  readonly rejectedUnbilled?: boolean;
}

export interface EgressGate {
  readonly url: string;
  /** The address the listener is bound to (always 127.0.0.1). */
  readonly boundAddress: string;
  readonly decisions: readonly GateDecision[];
  /** Arms one try; the try may forward exactly one request.  Returns false (and arms nothing) when a try is already armed. */
  readonly arm: (accept: (captured: CapturedRequest) => RequestAcceptance) => boolean;
  readonly disarm: () => void;
  /** Retry-After from the last 429/529 the upstream returned, in ms, consumed once. */
  readonly takeRetryAfterMs: () => number | null;
  /** True if the last 429/529 response body was the provider's documented rate-limit or overloaded error; consumed once. */
  readonly takeRejectedUnbilled: () => boolean;
  readonly close: () => Promise<void>;
}

export function parseRetryAfterMs(value: string | string[] | undefined | null, now: number): number | null {
  if (typeof value !== 'string') return null;
  const seconds = Number(value);
  if (value.trim() !== '' && Number.isFinite(seconds) && seconds >= 0) return Math.round(seconds * 1000);
  if (!/[A-Za-z]/.test(value)) return null;
  const date = Date.parse(value);
  return Number.isNaN(date) ? null : Math.max(0, date - now);
}

/** Node TLS, certificate-store, proxy and preload variables of the process that forwards. Any of them
 * can redirect the connection or change who is trusted, so the gate refuses to start or forward while one is set
 * (or while a matching flag is in process.execArgv, below). */
export const AMBIENT_NODE_NETWORK_ENV: readonly string[] = [
  'NODE_TLS_REJECT_UNAUTHORIZED', 'NODE_EXTRA_CA_CERTS', 'NODE_USE_ENV_PROXY', 'NODE_USE_SYSTEM_CA', 'NODE_OPTIONS',
  'SSL_CERT_FILE', 'SSL_CERT_DIR', 'HTTPS_PROXY', 'HTTP_PROXY', 'ALL_PROXY', 'https_proxy', 'http_proxy', 'all_proxy',
];
export function ambientNetworkEnvironment(env: NodeJS.ProcessEnv = process.env): readonly string[] {
  return Object.keys(env).filter(name => AMBIENT_NODE_NETWORK_ENV.includes(name));
}

/** The same switches given as Node flags rather than variables: the system or OpenSSL CA store and any `--tls-*` option. */
export function ambientNetworkFlags(execArgv: readonly string[] = process.execArgv): readonly string[] {
  return execArgv.filter(flag => flag === '--use-system-ca' || flag === '--use-openssl-ca' || flag.startsWith('--use-system-ca=')
    || flag.startsWith('--use-openssl-ca=') || flag.startsWith('--tls-'));
}
const ambientNetwork = (): boolean => ambientNetworkEnvironment().length > 0 || ambientNetworkFlags().length > 0;

/** The only remote destination bytes may ever be forwarded to. */
export const PROVIDER_ORIGIN = 'https://api.anthropic.com';

/** Throws unless the upstream is exactly the provider origin. A loopback
 * address is accepted only with the test-only token: in production a local
 * listener could forward anywhere. */
export function assertAllowedUpstream(url: string, loopbackToken?: typeof LOOPBACK_FOR_TESTS): void {
  let parsed: URL;
  try { parsed = new URL(url); } catch { throw new Error('egress gate: upstream is not a URL'); }
  const loopback = (parsed.protocol === 'http:' || parsed.protocol === 'https:') && (parsed.hostname === '127.0.0.1' || parsed.hostname === 'localhost' || parsed.hostname === '[::1]');
  const provider = parsed.origin === PROVIDER_ORIGIN && parsed.username === '' && parsed.password === '';
  if (!(loopback && loopbackToken === LOOPBACK_FOR_TESTS) && !provider) throw new Error(`egress gate: upstream must be ${PROVIDER_ORIGIN} (tests may add a loopback address)`);
}

export async function startEgressGate(options: EgressGateOptions): Promise<EgressGate> {
  if (options.upstream !== undefined) assertAllowedUpstream(options.upstream.url, options.upstream.loopbackForTests);
  if (ambientNetwork()) throw new Error('egress gate: ambient Node network environment is set');
  let spent = false;
  let armGeneration = 0;
  // Pinned for every upstream request: verified certificates, modern TLS, no connection reuse, and no proxy (Node reads none unless NODE_USE_ENV_PROXY, refused above).
  const upstreamAgent = new https.Agent({ rejectUnauthorized: true, minVersion: 'TLSv1.2', keepAlive: false });
  const decisions: GateDecision[] = [];
  let armed: ((captured: CapturedRequest) => RequestAcceptance) | null = null;
  let retryAfter: number | null = null;
  let unbilled = false;
  const refuse = (res: http.ServerResponse, record: Omit<GateDecision, 'decision' | 'upstreamStatus'>): void => {
    decisions.push({ ...record, decision: 'refused', upstreamStatus: null });
    res.writeHead(403, { 'content-type': 'application/json' });
    res.end(JSON.stringify({ type: 'error', error: { type: 'permission_error', message: 'egress-refused' } }));
  };
  const server = http.createServer((req, res) => {
    const chunks: Buffer[] = [];
    req.on('data', c => chunks.push(c as Buffer));
    req.on('end', () => {
      void (async () => {
        let clientGone = req.socket.destroyed;
        req.socket.once('close', () => { clientGone = true; });   // attached before any await
        const body = Buffer.concat(chunks);
        const captured: CapturedRequest = { method: req.method ?? '', url: req.url ?? '', headers: req.headers, body: body.toString('utf8') };
        const base = { method: captured.method, url: captured.url };
        if (armed === null) { refuse(res, { ...base, reasons: ['no try armed'] }); return; }
        if (isConnectivityProbe(captured)) {
          decisions.push({ ...base, decision: 'answered-locally', reasons: [], upstreamStatus: 200 });
          res.writeHead(200); res.end(); return;
        }
        let verdict: RequestAcceptance;
        try { verdict = armed(captured); } catch { verdict = { accepted: false, violations: ['acceptance predicate failed'] }; }
        if (!verdict.accepted) { refuse(res, { ...base, reasons: verdict.violations }); return; }
        if (spent) { refuse(res, { ...base, reasons: ['try already forwarded one request'] }); return; }
        spent = true;   // one forward per try, claimed before any await
        const mine = armGeneration;
        let allowed = false;
        try { allowed = (await options.permitted()) === true; } catch { allowed = false; }
        if (!allowed) { refuse(res, { ...base, reasons: ['consent not permitted'] }); return; }
        // Consent was answered a moment ago; the try must still be the same arming (disarm() and arm() both advance the generation) and the caller still connected.
        if (armGeneration !== mine || clientGone) { refuse(res, { ...base, reasons: ['try ended while consent was being asked'] }); return; }
        if (ambientNetwork()) { refuse(res, { ...base, reasons: ['ambient Node network environment is set'] }); return; }
        if (options.upstream === undefined) { refuse(res, { ...base, reasons: ['no upstream configured'] }); return; }
        const target = new URL(options.upstream.url);
        const headers = { ...req.headers };
        delete headers.host; delete headers.connection;
        if (options.stripFingerprint === true) for (const name of FINGERPRINT_HEADERS) delete headers[name];
        const transport = target.protocol === 'https:' ? https : http;
        const out = transport.request({ protocol: target.protocol, hostname: target.hostname, port: target.port, method: captured.method, path: captured.url, headers, ...(target.protocol === 'https:' ? { agent: upstreamAgent } : {}) }, upstreamRes => {
          const status = upstreamRes.statusCode ?? 502;
          if (status >= 300 && status < 400) {
            upstreamRes.resume();
            decisions.push({ ...base, decision: 'forwarded', reasons: ['upstream redirect not followed'], upstreamStatus: status });
            res.writeHead(502, { 'content-type': 'application/json' });
            res.end(JSON.stringify({ type: 'error', error: { type: 'api_error', message: 'upstream-redirect-refused' } }));
            return;
          }
          const rejected = status === 429 || status === 529;
          if (rejected) { retryAfter = parseRetryAfterMs(upstreamRes.headers['retry-after'], Date.now()); unbilled = false; }
          const entry: { -readonly [K in keyof GateDecision]: GateDecision[K] } = { ...base, decision: 'forwarded', reasons: [], upstreamStatus: status };
          decisions.push(entry);
          res.writeHead(status, upstreamRes.headers);
          if (rejected) {
            const seen: Buffer[] = [];
            let size = 0;
            upstreamRes.on('data', (c: Buffer) => { if (size < 4096) { seen.push(c); size += c.length; } });
            upstreamRes.on('end', () => {
              try { const j = JSON.parse(Buffer.concat(seen).toString('utf8')) as { type?: unknown; error?: { type?: unknown } }; unbilled = j.type === 'error' && typeof j.error?.type === 'string' && RATE_ERRORS.has(j.error.type); } catch { unbilled = false; }
              entry.rejectedUnbilled = unbilled;
            });
          }
          upstreamRes.on('error', () => res.destroy());
          upstreamRes.on('close', () => { if (!upstreamRes.complete) res.destroy(); });   // upstream dropped mid-body: the caller sees an error, never a hang
          upstreamRes.pipe(res);
        });
        out.on('error', () => { if (!res.headersSent) { decisions.push({ ...base, decision: 'forwarded', reasons: ['upstream unreachable'], upstreamStatus: null }); res.writeHead(502); } res.end(); });
        res.on('close', () => { if (!res.writableFinished) out.destroy(); });
        out.end(body);
      })();
    });
  });
  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = (server.address() as AddressInfo).port;
  return {
    url: `http://127.0.0.1:${port}`, boundAddress: (server.address() as AddressInfo).address, decisions,
    arm: accept => { if (armed !== null) return false; armed = accept; spent = false; armGeneration++; return true; },
    disarm: () => { armed = null; armGeneration++; },
    takeRetryAfterMs: () => { const v = retryAfter; retryAfter = null; return v; },
    takeRejectedUnbilled: () => { const v = unbilled; unbilled = false; return v; },
    close: () => new Promise<void>(resolve => { upstreamAgent.destroy(); server.closeAllConnections(); server.close(() => resolve()); }),
  };
}
