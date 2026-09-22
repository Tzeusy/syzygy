import { escapeHtml, type Route, type RouteResponse } from '@syzygy/cap1-daemon';

import { browserRequestAllowed } from './browser-origin.js';
import { mountPrefixForRequest, TAILNET_MOUNT_PREFIX, withMountPrefix } from './tailnet.js';

export const REOBSERVE_HUMAN_PATH = '/polaris/reobserve' as const;
export const REOBSERVE_TAILNET_PATH = `${TAILNET_MOUNT_PREFIX}${REOBSERVE_HUMAN_PATH}` as const;

export type ReobserveResult =
  | { readonly kind: 'reobserved'; readonly evaluation: string }
  | { readonly kind: 'failed'; readonly reason: string };

export interface ReobserveRoutesOptions {
  readonly reobserve: () => Promise<ReobserveResult>;
}

function resultPage(result: ReobserveResult, mountPrefix: string): RouteResponse {
  const back = withMountPrefix(mountPrefix, '/polaris');
  if (result.kind === 'reobserved') {
    return {
      status: 200,
      contentType: 'text/html; charset=utf-8',
      body: `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Re-observed</title></head><body><h1>Re-observed</h1><p data-reobserve-evaluation="${escapeHtml(result.evaluation)}">A new identified evaluation was captured: <code>${escapeHtml(result.evaluation)}</code>.</p><p><a href="${escapeHtml(back)}">Back to Polaris</a></p></body></html>`,
    };
  }
  return {
    status: 502,
    contentType: 'text/html; charset=utf-8',
    body: `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Re-observation unavailable</title></head><body><h1>Re-observation unavailable</h1><p data-reobserve-reason="${escapeHtml(result.reason)}">Unknown — ${escapeHtml(result.reason)}. The prior complete evaluation remains served.</p><p><a href="${escapeHtml(back)}">Back to Polaris</a></p></body></html>`,
  };
}

export function reobserveRoutes(options: ReobserveRoutesOptions): readonly Route[] {
  let inFlight: Promise<ReobserveResult> | undefined;
  const handle: Route['handle'] = async ({ request }) => {
    if (!browserRequestAllowed(request.headers)) {
      return { status: 403, contentType: 'application/json', body: JSON.stringify({ served: 'nothing', reason: 'browser-origin-refused' }) };
    }
    const resultPromise = inFlight ?? (inFlight = options.reobserve().finally(() => { inFlight = undefined; }));
    const result = await resultPromise;
    return resultPage(result, mountPrefixForRequest(request.headers));
  };
  return [
    { method: 'POST', path: REOBSERVE_HUMAN_PATH, credentialClass: 'human-open', handle },
    { method: 'POST', path: REOBSERVE_TAILNET_PATH, credentialClass: 'human-open', handle },
  ];
}
