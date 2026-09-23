import { DESIGN_TOKENS_CSS, legendHtml, skipLinkHtml } from './design-tokens.js';
import { withMountPrefix } from './tailnet.js';

export type SurfaceRouteId = 'home' | 'polaris' | 'trajectory' | 'orrery';

export interface HumanOperabilityStatus {
  readonly evaluationDigest: string | null;
  readonly projectRevision: string | null;
  readonly observerRevision: string | null;
  readonly credentialProvision: 'minted' | 'reused' | null;
  readonly inputBreaches: number | null;
  readonly servedBreaches: number | null;
  readonly latestBreach: { readonly limit: 'maxHumanResponseBytes' | 'maxMachineResponseBytes'; readonly sequence: number; readonly declared: number; readonly observed: number } | null;
}

/** One compact, non-verdict summary. Prefixes are labeled as prefixes; full
 * identities remain on the existing detailed surface. */
export function humanStatusLine(status: HumanOperabilityStatus | undefined, escapeHtml: (value: string) => string): string {
  const evaluation = status?.evaluationDigest === undefined || status.evaluationDigest === null ? 'Unknown (no evaluation)' : `sha256:${status.evaluationDigest.slice(0, 12)} prefix`;
  const project = status?.projectRevision === undefined || status.projectRevision === null ? 'Unknown (no project revision)' : `${status.projectRevision.slice(0, 12)} prefix`;
  const observer = status?.observerRevision === undefined || status.observerRevision === null ? 'Unknown (no observer revision)' : `${status.observerRevision.slice(0, 12)} prefix`;
  const credential = status?.credentialProvision ?? 'Unknown (no provision record)';
  const input = status?.inputBreaches === undefined || status.inputBreaches === null ? 'Unknown (shape unavailable)' : String(status.inputBreaches);
  const served = status?.servedBreaches === undefined || status.servedBreaches === null ? 'Unknown (recorder unavailable)' : String(status.servedBreaches);
  const latest = status?.latestBreach === null || status?.latestBreach === undefined
    ? ''
    : `; last ${status.latestBreach.limit === 'maxHumanResponseBytes' ? 'human' : 'machine'} #${status.latestBreach.sequence} ${status.latestBreach.observed}/${status.latestBreach.declared} B`;
  return `<p class="operability-status" data-human-status data-eval="${escapeHtml(status?.evaluationDigest ?? 'unknown')}" data-breaches="${escapeHtml(served)}" data-copy-role="epistemic-disclosure">Evaluation ${escapeHtml(evaluation)}; project ${escapeHtml(project)}; observer ${escapeHtml(observer)}; credential ${escapeHtml(credential)}; breaches input ${escapeHtml(input)}, served ${escapeHtml(served)}${latest}</p>`;
}

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
    return `<li><a href="${escapeHtml(href)}"${current_} data-copy-role="action-label" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>${escapeHtml(item.label)}</a></li>`;
  }).join('');
  return `<nav class="site-nav" aria-label="Three-surface POC sections"><ul>${items}</ul></nav>`;
}

export interface PageShellInput {
  readonly title: string;
  readonly current: SurfaceRouteId;
  readonly eyebrow: string;
  readonly heading: string;
  readonly lede: string;
  readonly extraStyle?: string;
  readonly readingLayout?: boolean;
  readonly body: string;
  readonly sidebar?: string;
  readonly footer: string;
  readonly status?: HumanOperabilityStatus;
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
  <style>${DESIGN_TOKENS_CSS}.operability-status{margin:.5rem auto 1rem;max-width:var(--content-width,90rem);padding:.4rem 1rem;border:1px solid var(--line);color:var(--muted);font:.75rem/1.45 var(--font-mono);overflow-wrap:anywhere}${input.extraStyle ?? ''}</style>
</head>
<body>
  ${skipLinkHtml('main-content')}
  ${input.readingLayout ? siteNav(input.current, mountPrefix, escapeHtml) : ''}
  ${input.sidebar === undefined ? '' : '<div class="reading-layout">'}
  <header>
    <div class="eyebrow" data-copy-role="project-fact" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>${escapeHtml(input.eyebrow)}</div>
    <h1 data-copy-role="project-fact" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>${escapeHtml(input.heading)}</h1>
    <p class="lede" data-copy-role="scope-instruction" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>${escapeHtml(input.lede)}</p>
  </header>
  ${humanStatusLine(input.status, escapeHtml)}
  ${input.sidebar === undefined ? '' : `<aside class="reading-sidebar">${input.sidebar}</aside>`}
  ${input.readingLayout ? '' : siteNav(input.current, mountPrefix, escapeHtml)}
  <main id="main-content">
    ${input.readingLayout ? '' : legendHtml(escapeHtml)}
    ${input.body}
  </main>
  <footer data-copy-role="project-fact" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>${input.readingLayout ? legendHtml(escapeHtml) : ''}${input.footer}</footer>
  ${input.sidebar === undefined ? '' : '</div>'}
</body>
</html>`;
}
