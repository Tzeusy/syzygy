// `tailscale serve --set-path` forwards the full, unstripped request path to
// this loopback-bound daemon (verified: a request to
// https://tzeusy.parrot-hen.ts.net/butlers-syzygy arrives here as literal
// path `/butlers-syzygy`, not `/`). The daemon's router matches paths by
// exact string equality with no prefix support, so the mount prefix is
// registered as additional exact routes rather than taught to the shared
// router.
export const TAILNET_MOUNT_PREFIX = '/butlers-syzygy' as const;

/** Which mount a request arrived on, decided by matched request path
 * (exact-match router — never a prefix strip). Every internal link a
 * rendered page emits must be built through `withMountPrefix` using this
 * value, or it silently reverts to a root-absolute path that `tailscale
 * serve --set-path` does not proxy. */
export function mountPrefixForPath(path: string): '' | typeof TAILNET_MOUNT_PREFIX {
  return path.startsWith(TAILNET_MOUNT_PREFIX) ? TAILNET_MOUNT_PREFIX : '';
}

export function withMountPrefix(mountPrefix: string, path: string): string {
  return `${mountPrefix}${path}`;
}
