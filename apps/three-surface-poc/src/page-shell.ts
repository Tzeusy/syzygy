import { DESIGN_TOKENS_CSS, legendHtml, skipLinkHtml } from './design-tokens.js';
import { withMountPrefix } from './tailnet.js';

export type SurfaceRouteId = 'home' | 'polaris' | 'trajectory' | 'orrery';

const NAV_ITEMS: readonly { readonly id: SurfaceRouteId; readonly href: string; readonly label: string }[] = [
  { id: 'home', href: '/', label: 'Overview' },
  { id: 'polaris', href: '/polaris', label: 'Polaris' },
  { id: 'trajectory', href: '/trajectory', label: 'Trajectory' },
  { id: 'orrery', href: '/orrery', label: 'Orrery' },
];

function siteNav(
  current: SurfaceRouteId,
  mountPrefix: string,
  escapeHtml: (value: string) => string,
): string {
  const items = NAV_ITEMS.map((item) => {
    const current_ = item.id === current ? ' aria-current="page"' : '';
    const href = withMountPrefix(mountPrefix, item.href);
    return `<li><a href="${escapeHtml(href)}"${current_}>${escapeHtml(item.label)}</a></li>`;
  }).join('');
  return `<nav aria-label="Three-surface POC sections"><ul>${items}</ul></nav>`;
}

export interface PageShellInput {
  readonly title: string;
  readonly current: SurfaceRouteId;
  readonly eyebrow: string;
  readonly heading: string;
  readonly lede: string;
  readonly extraStyle?: string;
  readonly body: string;
  readonly footer: string;
  readonly escapeHtml: (value: string) => string;
  /** The mount this page is being rendered under (`''` direct, or
   * `TAILNET_MOUNT_PREFIX` when reached via `tailscale serve`) — every
   * nav link is built relative to it. Defaults to `''`. */
  readonly mountPrefix?: string;
}

export function pageShell(input: PageShellInput): string {
  const escapeHtml = input.escapeHtml;
  const mountPrefix = input.mountPrefix ?? '';
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(input.title)}</title>
  <style>${DESIGN_TOKENS_CSS}${input.extraStyle ?? ''}</style>
</head>
<body>
  ${skipLinkHtml('main-content')}
  <header>
    <div class="eyebrow">${escapeHtml(input.eyebrow)}</div>
    <h1>${escapeHtml(input.heading)}</h1>
    <p class="lede">${escapeHtml(input.lede)}</p>
  </header>
  ${siteNav(input.current, mountPrefix, escapeHtml)}
  <main id="main-content">
    ${legendHtml(escapeHtml)}
    ${input.body}
  </main>
  <footer>${input.footer}</footer>
</body>
</html>`;
}
