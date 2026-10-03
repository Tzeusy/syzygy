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
  readonly upstream?: { readonly url: string };
  /** Consent switch, asked for every request including retries. Only `true` permits. */
  readonly permitted: () => Promise<boolean>;
}

export interface GateDecision {
  readonly method: string;
  readonly url: string;
  readonly decision: 'forwarded' | 'answered-locally' | 'refused';
  /** Content-free: predicate violation texts name fields, never values. */
  readonly reasons: readonly string[];
  readonly upstreamStatus: number | null;
}

export interface EgressGate {
  readonly url: string;
  readonly decisions: readonly GateDecision[];
  /** Arms one try. Returns false (and arms nothing) when a try is already armed. */
  readonly arm: (accept: (captured: CapturedRequest) => RequestAcceptance) => boolean;
  readonly disarm: () => void;
  /** Retry-After from the last 429/529 the upstream returned, in ms, consumed once. */
  readonly takeRetryAfterMs: () => number | null;
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

export async function startEgressGate(options: EgressGateOptions): Promise<EgressGate> {
  const decisions: GateDecision[] = [];
  let armed: ((captured: CapturedRequest) => RequestAcceptance) | null = null;
  let retryAfter: number | null = null;
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
        let allowed = false;
        try { allowed = (await options.permitted()) === true; } catch { allowed = false; }
        if (!allowed) { refuse(res, { ...base, reasons: ['consent not permitted'] }); return; }
        if (options.upstream === undefined) { refuse(res, { ...base, reasons: ['no upstream configured'] }); return; }
        const target = new URL(options.upstream.url);
        const headers = { ...req.headers };
        delete headers.host; delete headers.connection;
        const transport = target.protocol === 'https:' ? https : http;
        const out = transport.request({ protocol: target.protocol, hostname: target.hostname, port: target.port, method: captured.method, path: captured.url, headers }, upstreamRes => {
          const status = upstreamRes.statusCode ?? 502;
          if (status === 429 || status === 529) retryAfter = parseRetryAfterMs(upstreamRes.headers['retry-after'], Date.now());
          decisions.push({ ...base, decision: 'forwarded', reasons: [], upstreamStatus: status });
          res.writeHead(status, upstreamRes.headers);
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
    url: `http://127.0.0.1:${port}`, decisions,
    arm: accept => { if (armed !== null) return false; armed = accept; return true; },
    disarm: () => { armed = null; },
    takeRetryAfterMs: () => { const v = retryAfter; retryAfter = null; return v; },
    close: () => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }),
  };
}
