import * as http from 'node:http';

import { evaluationId, type AdmissionResult } from '@syzygy/cap1-core';

import {
  credentialFromAuthorizationHeader,
  ensureCredential,
  verifyCredential,
} from './credentials.js';
import type { ProjectEvaluation } from './pipeline.js';

// RT3 — the daemon's HTTP server core (CAP1-REQ-012's admission at the
// transport, under RFC5-3: classification by credential presented,
// never network location — enforced here by binding 127.0.0.1 only and
// by the admission gate consulting nothing but the Authorization
// header).
//
// The server is a ROUTE REGISTRY: RT4 (machine JSON endpoint) and RT5
// (server-rendered human page) plug in as `Route` values passed to
// `createDaemon` — this wave mounts only the minimal root route. The
// load-bearing mount property: credential admission runs BEFORE any
// machine-credentialed handler. A missing or invalid credential gets
// core's named refusal and the handler is NEVER invoked — no partial
// answer can exist, because the handler that would compute one never
// ran. Refusal bodies are core's named vocabulary
// (`{ admitted: false, served: 'nothing' }`), never a bare 401 string.
//
// Startup writes: exactly the credential/state files inside the
// explicit state directory (via `ensureCredential`, whose writes are
// routed through the state-write boundary). Nothing else is written.

// Local-only binding, fixed. Not configurable: the daemon is a LOCAL
// daemon; exposure beyond loopback is out of Capability 1's scope.
export const DAEMON_HOST = '127.0.0.1' as const;

export type CredentialClass = 'human-open' | 'machine-credentialed';

export interface RouteRequest {
  readonly method: string;
  /** URL pathname only (no query string). */
  readonly path: string;
  readonly query: URLSearchParams;
  readonly headers: Readonly<Record<string, string | string[] | undefined>>;
}

/** A complete response. Handlers return the WHOLE body — the mount
 * writes it in one step, so a throwing handler can never have sent a
 * partial answer. */
export interface RouteResponse {
  readonly status: number;
  readonly contentType: string;
  readonly body: string;
}

export interface RouteContext {
  readonly request: RouteRequest;
  /** Present exactly for machine-credentialed routes, and always the
   * ADMITTED arm — a refused admission never reaches a handler. */
  readonly admission?: Extract<AdmissionResult, { admitted: true }> | undefined;
}

// The route-registry contract RT4/RT5 build on: one value per
// (method, path), classed by credential requirement. Registration is
// data — pass the Route in `DaemonOptions.routes`; the mount applies
// admission for 'machine-credentialed' routes before `handle` runs.
export interface Route {
  readonly method: 'GET' | 'HEAD' | 'POST' | 'PUT' | 'DELETE';
  readonly path: string;
  readonly credentialClass: CredentialClass;
  handle(ctx: RouteContext): RouteResponse | Promise<RouteResponse>;
}

// Named bodies — every non-handler response is a named value, never a
// bare status string.
//
// The refusal body is core's admission vocabulary VERBATIM: refused
// admission serves 'nothing' (CAP1-REQ-015 oracle limb (c)).
export const REFUSAL_BODY = { admitted: false, served: 'nothing' } as const;
export const REFUSAL_STATUS = 401;

// Unknown route: an explicit named 404 body, never silence.
export const UNKNOWN_ROUTE_REASON = 'unknown-route' as const;
export const UNKNOWN_ROUTE_STATUS = 404;

// A handler that threw: the named failure, never a partial answer (the
// handler's body never started writing — see RouteResponse).
export const HANDLER_FAILURE_REASON = 'handler-failure' as const;
export const HANDLER_FAILURE_STATUS = 500;

export interface DaemonOptions {
  /** The daemon state directory — the ONLY location startup may write. */
  readonly stateDir: string;
  readonly routes: readonly Route[];
  /** TCP port; 0 (the default) binds an ephemeral port for tests. */
  readonly port?: number | undefined;
}

export interface RunningDaemon {
  readonly host: typeof DAEMON_HOST;
  readonly port: number;
  /** Where the machine credential lives — the PATH, never the value. */
  readonly credentialPath: string;
  readonly credentialProvision: 'minted' | 'reused';
  close(): Promise<void>;
}

export type DaemonStart =
  | { readonly started: true; readonly daemon: RunningDaemon }
  | {
      readonly started: false;
      readonly failure:
        | { readonly kind: 'credential-unprovisionable'; readonly detail: string }
        | { readonly kind: 'duplicate-route'; readonly detail: string }
        | { readonly kind: 'bind-failed'; readonly detail: string };
    };

function routeKey(method: string, path: string): string {
  return `${method} ${path}`;
}

function respond(res: http.ServerResponse, response: RouteResponse): void {
  res.writeHead(response.status, { 'content-type': response.contentType });
  res.end(response.body);
}

function respondJson(res: http.ServerResponse, status: number, body: unknown): void {
  respond(res, {
    status,
    contentType: 'application/json',
    body: JSON.stringify(body),
  });
}

/**
 * Create and start the daemon: provision the credential (the one
 * startup write, inside `stateDir`), mount the routes, bind 127.0.0.1.
 * Every failure is a named arm; a started daemon is closed via
 * `close()`.
 */
export async function createDaemon(options: DaemonOptions): Promise<DaemonStart> {
  const provision = ensureCredential(options.stateDir);
  if (provision.kind === 'unprovisionable') {
    return {
      started: false,
      failure: { kind: 'credential-unprovisionable', detail: provision.detail },
    };
  }
  const expectedToken = provision.token;

  const registry = new Map<string, Route>();
  for (const route of options.routes) {
    const key = routeKey(route.method, route.path);
    if (registry.has(key)) {
      return {
        started: false,
        failure: {
          kind: 'duplicate-route',
          detail: `two routes registered for \`${key}\``,
        },
      };
    }
    registry.set(key, route);
  }

  const server = http.createServer((req, res) => {
    void handleRequest(req, res);
  });

  async function handleRequest(
    req: http.IncomingMessage,
    res: http.ServerResponse,
  ): Promise<void> {
    const url = new URL(req.url ?? '/', `http://${DAEMON_HOST}`);
    const method = req.method ?? 'GET';
    const route = registry.get(routeKey(method, url.pathname));

    if (route === undefined) {
      respondJson(res, UNKNOWN_ROUTE_STATUS, {
        served: 'nothing',
        reason: UNKNOWN_ROUTE_REASON,
        method,
        path: url.pathname,
      });
      return;
    }

    let admission: Extract<AdmissionResult, { admitted: true }> | undefined;
    if (route.credentialClass === 'machine-credentialed') {
      // Admission BEFORE the handler: a refused credential means the
      // handler is never invoked and nothing but the named refusal is
      // served. The decision consults the presented credential alone —
      // no address, no route detail (RFC5-3).
      const credential = credentialFromAuthorizationHeader(req.headers.authorization);
      const result = verifyCredential(expectedToken, credential);
      if (!result.admitted) {
        respondJson(res, REFUSAL_STATUS, REFUSAL_BODY);
        return;
      }
      admission = result;
    }

    const context: RouteContext = {
      request: {
        method,
        path: url.pathname,
        query: url.searchParams,
        headers: req.headers,
      },
      admission,
    };

    try {
      const response = await route.handle(context);
      respond(res, response);
    } catch (cause) {
      // The handler returns a complete body or nothing (RouteResponse),
      // so no partial answer preceded this named failure.
      respondJson(res, HANDLER_FAILURE_STATUS, {
        served: 'nothing',
        reason: HANDLER_FAILURE_REASON,
        detail: cause instanceof Error ? cause.message : String(cause),
      });
    }
  }

  const port = options.port ?? 0;
  const bound = await new Promise<
    { readonly ok: true; readonly port: number } | { readonly ok: false; readonly detail: string }
  >((resolve) => {
    server.once('error', (cause) => {
      resolve({ ok: false, detail: cause.message });
    });
    server.listen(port, DAEMON_HOST, () => {
      const address = server.address();
      if (address === null || typeof address === 'string') {
        server.close();
        resolve({ ok: false, detail: 'server bound without a TCP address' });
        return;
      }
      resolve({ ok: true, port: address.port });
    });
  });

  if (!bound.ok) {
    return { started: false, failure: { kind: 'bind-failed', detail: bound.detail } };
  }

  return {
    started: true,
    daemon: {
      host: DAEMON_HOST,
      port: bound.port,
      credentialPath: provision.path,
      credentialProvision: provision.kind,
      close: () =>
        new Promise<void>((resolve, reject) => {
          server.close((cause) => (cause ? reject(cause) : resolve()));
        }),
    },
  };
}

// --- This wave's minimal root route --------------------------------------

// A plain served-facts statement at `/` — human-open, text/plain. RT4
// and RT5 replace nothing here: they REGISTER their own routes; this
// route only states, honestly, what the pipeline evaluated. Every line
// is derived from named pipeline values; nothing is invented.
export function minimalRootRoute(evaluation: ProjectEvaluation): Route {
  return {
    method: 'GET',
    path: '/',
    credentialClass: 'human-open',
    handle(): RouteResponse {
      return {
        status: 200,
        contentType: 'text/plain; charset=utf-8',
        body: rootStatement(evaluation),
      };
    },
  };
}

function rootStatement(evaluation: ProjectEvaluation): string {
  const lines: string[] = ['syzygy capability-1 daemon — served facts', ''];
  switch (evaluation.kind) {
    case 'project-evaluated': {
      lines.push(`selection: ${evaluation.model.selection}`);
      lines.push(`evaluation: ${evaluationId(evaluation.model.evaluation)}`);
      lines.push('');
      for (const fact of evaluation.model.facts) {
        const reason =
          fact.epistemic.label === 'Unknown' && 'reasons' in fact.epistemic
            ? ` (reason: ${fact.epistemic.reasons.primary})`
            : '';
        lines.push(`- ${fact.name}: ${fact.value} [${fact.epistemic.label}]${reason}`);
      }
      break;
    }
    case 'declaration-invalid': {
      lines.push('declaration: read but invalid — registration failed');
      for (const failure of evaluation.failures) {
        lines.push(`- validation failure (${failure.kind}): ${failure.detail}`);
      }
      break;
    }
    case 'no-declaration-observed': {
      const obs = evaluation.declarationObservation;
      lines.push(`declaration: ${obs.label} (reason: ${obs.reason})`);
      break;
    }
  }
  lines.push('');
  lines.push('machine endpoint and human page arrive as registered routes (RT4/RT5).');
  return lines.join('\n');
}
