// `tailscale serve --set-path` forwards the full, unstripped request path to
// this loopback-bound daemon (verified: a request to
// https://tzeusy.parrot-hen.ts.net/butlers-syzygy arrives here as literal
// path `/butlers-syzygy`, not `/`). The daemon's router matches paths by
// exact string equality with no prefix support, so the mount prefix is
// registered as additional exact routes rather than taught to the shared
// router.
export const TAILNET_MOUNT_PREFIX = '/butlers-syzygy' as const;
