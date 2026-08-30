export const BROWSER_ORIGIN_REFUSAL = {
  served: 'nothing',
  reason: 'browser-origin-refused',
} as const;

// Exposed only via `tailscale serve` (TLS-terminated at the tailnet edge,
// proxying to the loopback-bound daemon), never a direct public bind — see
// AGENTS.md "Hard prohibitions" (no broad remote access). Exported: it is
// also the one reliable signal (via the Host header) that a request arrived
// through the tailnet mount rather than direct loopback access — see
// `tailnet.ts`'s `mountPrefixForRequest`. `tailscale serve --set-path`
// strips the mount prefix from the forwarded request path, so the path
// itself cannot be used for that distinction.
export const TAILNET_HOST = 'tzeusy.parrot-hen.ts.net' as const;

function singleHeader(
  value: string | readonly string[] | undefined,
): string | undefined {
  return typeof value === 'string' ? value : undefined;
}

function expectedOrigin(host: string): string {
  return host === TAILNET_HOST ? `https://${host}` : `http://${host}`;
}

export function browserRequestAllowed(
  headers: Readonly<Record<string, string | readonly string[] | undefined>>,
): boolean {
  const host = singleHeader(headers['host']);
  const hostAllowed =
    host !== undefined &&
    (/^(?:127\.0\.0\.1|localhost):[0-9]+$/.test(host) || host === TAILNET_HOST);
  if (!hostAllowed) {
    return false;
  }
  const origin = singleHeader(headers['origin']);
  return origin === undefined || origin === expectedOrigin(host);
}
