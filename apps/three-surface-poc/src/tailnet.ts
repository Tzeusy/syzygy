import { TAILNET_HOST } from './browser-origin.js';

// `tailscale serve --set-path /butlers-syzygy <target>` STRIPS the mount
// prefix before forwarding — verified empirically this session by mounting
// a throwaway echo listener at a second `--set-path` and inspecting the raw
// request it received: a browser request to
// https://tzeusy.parrot-hen.ts.net/butlers-syzygy/polaris arrives at the
// backend as literal path `/polaris`, carrying no header that names the
// original mount path either. So the request path can never distinguish
// tailnet-mounted access from direct loopback access; the routes registered
// below at `TAILNET_MOUNT_PREFIX`-prefixed paths are unreachable through
// this deployment's real `tailscale serve` config and exist only for a
// hypothetical path-preserving proxy in front of the daemon instead.
//
// The one signal that does survive the hop is the Host header the browser
// actually sent — see `mountPrefixForRequest`.
export const TAILNET_MOUNT_PREFIX = '/butlers-syzygy' as const;

function singleHeader(value: string | readonly string[] | undefined): string | undefined {
  return typeof value === 'string' ? value : undefined;
}

/** Which mount a request arrived on, decided by the Host header the
 * browser actually sent (survives the tailscale hop even though the path
 * does not). Every internal link a rendered page emits must be built
 * through `withMountPrefix` using this value, or it silently reverts to a
 * root-absolute path that resolves to the wrong host in the browser once
 * reached via the tailnet mount. */
export function mountPrefixForRequest(
  headers: Readonly<Record<string, string | readonly string[] | undefined>>,
): '' | typeof TAILNET_MOUNT_PREFIX {
  return singleHeader(headers['host']) === TAILNET_HOST ? TAILNET_MOUNT_PREFIX : '';
}

export function withMountPrefix(mountPrefix: string, path: string): string {
  return `${mountPrefix}${path}`;
}
