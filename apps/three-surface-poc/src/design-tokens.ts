export type PocEpistemicLabel = 'Observed' | 'Unknown';

interface EpistemicEncoding {
  readonly label: PocEpistemicLabel;
  readonly className: string;
  readonly symbol: string;
  readonly description: string;
}

/**
 * The one declared epistemic encoding table (POC-REQ-060). Every surface
 * imports this table rather than styling Observed/Unknown ad hoc, and the
 * legend on every surface is generated from it — so a legend entry always
 * matches a live encoding and vice versa (POC-REQ-061).
 */
export const EPISTEMIC_ENCODING: readonly EpistemicEncoding[] = [
  {
    label: 'Observed',
    className: 'epistemic-observed',
    symbol: '●',
    description: 'A resolvable observation or governed artifact backs this claim.',
  },
  {
    label: 'Unknown',
    className: 'epistemic-unknown',
    symbol: '?',
    description: 'No verifying evidence exists yet; the reason is stated beside it.',
  },
];

export function epistemicClassName(label: PocEpistemicLabel): string {
  const encoding = EPISTEMIC_ENCODING.find((entry) => entry.label === label);
  if (encoding === undefined) {
    throw new Error(`no declared encoding for epistemic label: ${label}`);
  }
  return encoding.className;
}

/**
 * One shared token set (POC-REQ-060). Surface-specific CSS may add rules,
 * never redefine these variables.
 */
export const DESIGN_TOKENS_CSS = `
  :root {
    color-scheme: dark;
    --ink: #dfe9e7;
    --muted: #8ca3a4;
    --void: #071012;
    --panel: #0c181b;
    --panel-raised: #102126;
    --line: #294248;
    --cyan: #78e1d1;
    --amber: #f1b85b;
    --unknown: #f3c56f;
    --focus: #f1b85b;
    --font-serif: Georgia, 'Times New Roman', serif;
    --font-mono: 'Courier New', ui-monospace, monospace;
    --space-1: .5rem;
    --space-2: 1rem;
    --space-3: 1.5rem;
    --space-4: 2.5rem;
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    color: var(--ink);
    background: radial-gradient(circle at 15% 0%, #173238 0, transparent 34rem), var(--void);
    font-family: var(--font-serif);
    line-height: 1.5;
  }
  a { color: var(--cyan); text-underline-offset: .22em; }
  a:focus-visible, button:focus-visible, [tabindex]:focus-visible {
    outline: 3px solid var(--focus);
    outline-offset: 4px;
  }
  code, .kind, .epistemic, .eyebrow, nav, .legend {
    font-family: var(--font-mono);
  }
  .skip-link {
    position: absolute;
    left: -999px;
    top: 0;
    background: var(--panel-raised);
    color: var(--ink);
    padding: .6rem 1rem;
    z-index: 10;
    border: 1px solid var(--line);
  }
  .skip-link:focus { left: 1rem; top: 1rem; }
  header, main, footer { width: min(1180px, calc(100% - 2rem)); margin-inline: auto; }
  header { padding: 3rem 0 2rem; }
  .eyebrow { color: var(--cyan); letter-spacing: .15em; text-transform: uppercase; font-size: .77rem; }
  h1 { max-width: 18ch; font-size: clamp(2.2rem, 5.5vw, 4.4rem); line-height: .95; letter-spacing: -.03em; margin: .5rem 0 1rem; }
  .lede { max-width: 70ch; font-size: 1.08rem; color: #bfd0d0; }
  .notice {
    border-left: 3px solid var(--amber);
    padding: .85rem 1rem;
    background: #1b211c;
    color: #f6dfb5;
    max-width: 78ch;
  }
  nav {
    position: sticky;
    top: 0;
    z-index: 2;
    background: color-mix(in srgb, var(--void) 92%, transparent);
    border-block: 1px solid var(--line);
    backdrop-filter: blur(10px);
  }
  nav ul {
    width: min(1180px, calc(100% - 2rem));
    margin: 0 auto;
    padding: .8rem 0;
    display: flex;
    gap: 1.25rem;
    list-style: none;
    overflow-x: auto;
  }
  nav a[aria-current="page"] { color: var(--ink); text-decoration: underline; }
  .epistemic {
    display: inline-block;
    padding: .08rem .5rem;
    border: 1px solid currentColor;
    border-radius: .2rem;
    font-size: .74rem;
    letter-spacing: .05em;
    text-transform: uppercase;
  }
  .epistemic-observed { color: var(--cyan); }
  .epistemic-unknown { color: var(--unknown); background: #3d2f1322; }
  .legend {
    list-style: none;
    padding: 0;
    margin: 1rem 0;
    display: flex;
    flex-wrap: wrap;
    gap: 1rem 1.5rem;
    font-size: .78rem;
    color: var(--muted);
  }
  .legend li { display: flex; align-items: center; gap: .4rem; }
  .table-wrap { overflow-x: auto; border: 1px solid var(--line); }
  table { width: 100%; border-collapse: collapse; background: #091416; font-size: .92rem; }
  th, td { text-align: left; vertical-align: top; padding: .85rem; border-bottom: 1px solid var(--line); }
  th { color: var(--muted); font-family: var(--font-mono); font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; }
  tr:target { background: #1e383b; outline: 2px solid var(--cyan); outline-offset: -2px; }
  .kind { color: #9fc0c2; font-size: .74rem; }
  small { color: var(--muted); }
  .unavailable-notice { color: var(--unknown); border: 1px dashed var(--unknown); padding: .75rem 1rem; }
  footer { padding: 2rem 0 4rem; border-top: 1px solid var(--line); color: var(--muted); }
  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    * { animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; }
  }
`;

export function legendHtml(escapeHtml: (value: string) => string): string {
  const items = EPISTEMIC_ENCODING.map(
    (entry) =>
      `<li><span class="epistemic ${entry.className}">${escapeHtml(entry.symbol)} ${escapeHtml(entry.label)}</span> ${escapeHtml(entry.description)}</li>`,
  ).join('');
  return `<ul class="legend" aria-label="Epistemic encoding legend" data-copy-role="epistemic-disclosure">${items}</ul>`;
}

export function skipLinkHtml(targetId: string): string {
  return `<a class="skip-link" href="#${targetId}" data-copy-role="action-label">Skip to main content</a>`;
}
