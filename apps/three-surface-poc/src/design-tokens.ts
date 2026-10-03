import type { ProjectShapeClaim } from '@syzygy/three-surface-poc-core';

import type { PolarisCopyId } from './polaris-copy.js';

export type PocEpistemicLabel = 'Observed' | 'Unknown';

interface EpistemicEncoding {
  readonly label: PocEpistemicLabel;
  readonly className: string;
  readonly symbol: string;
  readonly description: string;
  readonly token: '--observed' | '--unknown';
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
    token: '--observed',
  },
  {
    label: 'Unknown',
    className: 'epistemic-unknown',
    symbol: '?',
    description: 'No verifying evidence exists yet; the reason is stated beside it.',
    token: '--unknown',
  },
];

/** One treatment for each live badge, project-shape tuple and Unknown disclosure. */
export const EPISTEMIC_TREATMENTS_CSS = EPISTEMIC_ENCODING.map((entry) => {
  const selectors = [
    `.epistemic.${entry.className}`,
    `.claim-tuple[data-epistemic-label="${entry.label}"]`,
    ...(entry.label === 'Unknown' ? ['[data-unknown-disclosure]'] : []),
  ];
  const symbolSelectors = selectors.map((selector) => `${selector}::before`);
  return `${selectors.join(', ')} { color: var(${entry.token}); }\n  ${symbolSelectors.join(', ')} { content: "${entry.symbol} "; }\n  [data-epistemic-scope-label="${entry.label}"] { --claim-color: var(${entry.token}); --claim-symbol: "${entry.symbol} "; }${entry.label === 'Unknown' ? '\n  [data-unknown-disclosure] { border-left: 3px solid var(--unknown); }\n  [data-unknown-disclosure] a { color: inherit; }' : ''}`;
}).join('\n  ');

type Tier = NonNullable<ProjectShapeClaim['epistemic']['tier']>;
type Freshness = NonNullable<ProjectShapeClaim['epistemic']['freshness']>;
type Challenge = ProjectShapeClaim['challenge'];

export type TupleField = 'tier' | 'freshness' | 'challenge';

/** One declared treatment of a tuple field value (syzygy-dov.3.2; P-70 M3
 * slice 5): the value, the class its span and its glossary row carry, the
 * symbol and semantic token that class renders, the copy row that describes
 * it, and — where a value can be absent from an evaluation — the reason and
 * route the glossary states when no claim carries it. */
export interface TupleFieldEncoding<V extends string = string> {
  readonly field: TupleField;
  readonly value: V;
  readonly className: string;
  readonly symbol: string;
  readonly token: '--ink' | '--muted';
  readonly description: PolarisCopyId;
  readonly unreachable?: string;
}

/** The six RFC2-25 rendering tiers, closed at six. */
export const TIER_ENCODING: readonly TupleFieldEncoding<Tier>[] = [
  { field: 'tier', value: 'gate-backed', className: 'tt-gate-backed', symbol: '◆', token: '--ink', description: 'states.tier.gate-backed' },
  { field: 'tier', value: 'report-fact', className: 'tt-report-fact', symbol: '◇', token: '--ink', description: 'states.tier.report-fact' },
  { field: 'tier', value: 'reduced-fidelity', className: 'tt-reduced-fidelity', symbol: '◒', token: '--muted', description: 'states.tier.reduced-fidelity' },
  { field: 'tier', value: 'asserted-by-worker', className: 'tt-asserted-by-worker', symbol: '✎', token: '--muted', description: 'states.tier.asserted-by-worker' },
  { field: 'tier', value: 'declared-only', className: 'tt-declared-only', symbol: '○', token: '--muted', description: 'states.tier.declared-only' },
  { field: 'tier', value: 'suspended', className: 'tt-suspended', symbol: '‖', token: '--muted', description: 'states.tier.suspended' },
];

/** No tier applies (an Unknown with no evidence). A treatment of the tier
 * slot's absence, never a seventh tier: it sits outside TIER_ENCODING. */
export const TIER_ABSENCE_ENCODING: TupleFieldEncoding<'unstated'> = {
  field: 'tier', value: 'unstated', className: 'tt-unstated', symbol: '∅', token: '--muted', description: 'states.tier.unstated',
};

/** The four RFC2-10 freshness values. A claim with no freshness carries no
 * value from this slot; its absence is disclosed beside the tuple. */
export const FRESHNESS_ENCODING: readonly TupleFieldEncoding<Freshness>[] = [
  { field: 'freshness', value: 'fresh', className: 'tt-fresh', symbol: '▲', token: '--ink', description: 'states.freshness.fresh',
    unreachable: 'Not reachable at this evaluation: no claim was captured at this evaluation. Route: capture an evaluation that carries the evidence.' },
  { field: 'freshness', value: 'stale', className: 'tt-stale', symbol: '△', token: '--muted', description: 'states.freshness.stale',
    unreachable: 'Not reachable at this evaluation: no claim freshness is judged against a currency bound; declare the bound and route freshness through the currency assessor.' },
  { field: 'freshness', value: 'broken', className: 'tt-broken', symbol: '✕', token: '--muted', description: 'states.freshness.broken',
    unreachable: 'Not reachable at this evaluation: one pinned revision carries no earlier claim; a changed source belongs to a later evidence probe, not this freshness value. Route: re-observe the repository.' },
  { field: 'freshness', value: 'superseded', className: 'tt-superseded', symbol: '»', token: '--muted', description: 'states.freshness.superseded',
    unreachable: 'Not reachable at this evaluation: no claim from an earlier evaluation is carried. Route: capture a new evaluation that carries the replacement.' },
];

/** The one challenge value the model carries. */
export const CHALLENGE_ENCODING: readonly TupleFieldEncoding<Challenge>[] = [
  { field: 'challenge', value: 'unchallenged', className: 'tt-unchallenged', symbol: '◌', token: '--ink', description: 'states.challenge.unchallenged' },
];

const TUPLE_FIELD_TREATMENTS: readonly TupleFieldEncoding[] = [...TIER_ENCODING, TIER_ABSENCE_ENCODING, ...FRESHNESS_ENCODING, ...CHALLENGE_ENCODING];

/** The declared treatment of one served field value; an undeclared value
 * refuses to render rather than falling back to an ad hoc style. */
export function tupleFieldEncoding(field: TupleField, value: string): TupleFieldEncoding {
  const encoding = TUPLE_FIELD_TREATMENTS.find((entry) => entry.field === field && entry.value === value);
  if (encoding === undefined) throw new Error(`no declared ${field} encoding for value: ${value}`);
  return encoding;
}

/** One rule pair per declared value, shared by the tuple's field mark and
 * the glossary row that defines it. The symbol carries an empty alternative
 * text: the value's word is already in the tuple and the row. */
export const TUPLE_FIELD_TREATMENTS_CSS = TUPLE_FIELD_TREATMENTS
  .map((entry) => `.${entry.className} { color: var(${entry.token}); }\n  .${entry.className}::before { content: "${entry.symbol} " / ""; }`)
  .join('\n  ');

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
    --observed: #78e1d1;
    --amber: #f1b85b;
    --unknown: #f3c56f;
    --proposed: #aa90ee;
    /* Its own token (N4; S11-F2, repaired after independent review): the
       first cut aliased --focus to the --cyan literal (#78e1d1), which
       collides with --cyan's OWN semantic meaning — EPISTEMIC_ENCODING's
       "Observed" class (.epistemic-observed, rendered in the legend by
       legendHtml()) resolves to exactly that colour, so a focus ring was
       indistinguishable from the "this claim is Observed" marker. That is
       the same defect class S11-F2 named for --amber, just recreated with a
       different colour (VIS-7: never let a UI-state colour collide with a
       claim-bearing semantic colour). #b98eff is spent by no
       EPISTEMIC_ENCODING class (--cyan, --unknown), no --amber/.notice
       accent, and no link colour (also --cyan) — see
       design-tokens.test.ts's CSS-derived distinctness sweep. Contrast
       against the page background (--void #071012 under the header
       radial-gradient toward #173238) is ~7.7:1 by WCAG relative luminance,
       clearing the >=3:1 floor WCAG 2.4.11/1.4.11 set for a non-text focus
       indicator. */
    --focus: #b98eff;
    /* The Polaris reading column's declared canonical measure (N4; S11-F3,
       reworded after independent review — this token DECLARES a value, it
       does not RESOLVE anything: nothing in this file, or elsewhere in this
       change's scope, reads var(--measure-reading) yet). polaris.ts
       (POLARIS_STYLE) redeclares .reading-prose twice — 66ch at line ~1342,
       then 74ch at line ~1403, so the later cascade rule (74ch) is what
       actually renders, and is also the value every other reading-layout
       rule in that stylesheet already uses (.band, .claim-section, .group,
       header, .capability-guide, etc.). docs/POLARIS-READING-LAYOUT.md
       line 3 states no literal ch number ("Polaris uses a wider editorial
       column..."), so the doc alone cannot settle the two numbers; 74ch is
       the wider of the pair and the one that already wins the cascade, so
       it is the value this token declares as canonical. polaris.ts is out
       of scope for this change (owned by another slice) — this token does
       not delete the duplicate 66ch declaration there, and nothing wires
       polaris.ts to read this token yet; it only names the canonical value
       for slice 2 to wire var(--measure-reading) into, and for the
       duplicate declaration there to converge on. */
    --measure-reading: 74ch;
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
  a:focus-visible, button:focus-visible, summary:focus-visible, [tabindex]:focus-visible {
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
  .site-nav {
    position: sticky;
    top: 0;
    z-index: 2;
    background: color-mix(in srgb, var(--void) 92%, transparent);
    border-block: 1px solid var(--line);
    backdrop-filter: blur(10px);
  }
  .site-nav ul {
    width: min(1180px, calc(100% - 2rem));
    margin: 0 auto;
    padding: .8rem 0;
    display: flex;
    gap: 1.25rem;
    list-style: none;
    overflow-x: auto;
  }
  .site-nav a[aria-current="page"] { color: var(--ink); text-decoration: underline; }
  .epistemic {
    display: inline-block;
    padding: .08rem .5rem;
    border: 1px solid currentColor;
    border-radius: .2rem;
    font-size: .74rem;
    letter-spacing: .05em;
    text-transform: uppercase;
  }
  ${EPISTEMIC_TREATMENTS_CSS}
  .claim-tuple:not([data-epistemic-label]) { color: var(--claim-color); }
  .claim-tuple:not([data-epistemic-label])::before { content: var(--claim-symbol); }
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
  .unavailable-notice { border: 1px dashed var(--line); padding: .75rem 1rem; }
  footer { padding: 2rem 0 4rem; border-top: 1px solid var(--line); color: var(--muted); }
  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    * { animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; }
  }
`;

export function legendHtml(escapeHtml: (value: string) => string): string {
  const items = EPISTEMIC_ENCODING.map(
    (entry) =>
      `<li><span class="epistemic ${entry.className}">${escapeHtml(entry.label)}</span> ${escapeHtml(entry.description)}</li>`,
  ).join('');
  return `<ul class="legend" aria-label="Epistemic encoding legend" data-copy-role="epistemic-disclosure" data-claim-role="epistemic-claim" data-presentation-artifact data-non-citable>${items}</ul>`;
}

export function skipLinkHtml(targetId: string): string {
  return `<a class="skip-link" href="#${targetId}" data-copy-role="action-label" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>Skip to main content</a>`;
}
