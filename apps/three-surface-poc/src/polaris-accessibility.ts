// Keyboard / non-visual navigation and WCAG AA contrast checks — task 4.4
// (syzygy-1z3.20; PWB-REQ-016, PWB-REQ-011, PWB-REQ-020; RFC7-31, RFC7-34).
//
// Everything here is measured in a real browser through `cdp-browser.ts`:
// the focusable population and document order come from the live DOM, the
// focus trace from real Tab / Shift+Tab presses, exact-source activation
// from a real Enter press, the non-visual representation from the
// browser's own accessibility tree, and every contrast ratio from computed
// styles. This module renders nothing and reads no page-building code — it
// only asks the browser what a keyboard-only or non-visual reader gets.
//
// Nothing is a pass without a denominator: every check reports the
// population it measured beside the violations it found.

import type { BrowserPage } from './cdp-browser.js';

// ---------------------------------------------------------------------------
// In-page scripts. Each is a self-contained expression returning JSON.

/** Every element that can take sequential focus, in document order, as the
 * browser sees it. `index` is the element's position among all elements. */
const POPULATION_SCRIPT = `(() => {
  const all = Array.from(document.querySelectorAll('*'));
  const selector = 'a[href], area[href], button, input, select, textarea, iframe, summary, [tabindex], [contenteditable="true"]';
  return all.filter((e) => e.matches(selector)).map((e) => ({
    index: all.indexOf(e),
    tag: e.tagName.toLowerCase(),
    id: e.id,
    href: e.getAttribute('href'),
    tabindex: e.getAttribute('tabindex'),
    text: (e.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 80),
    rendered: e.getClientRects().length > 0,
  }));
})()`;

/** The active element, described the same way as the population. */
const ACTIVE_SCRIPT = `(() => {
  const e = document.activeElement;
  if (!e || e === document.body || e === document.documentElement) return null;
  const all = Array.from(document.querySelectorAll('*'));
  const s = getComputedStyle(e);
  return {
    index: all.indexOf(e),
    tag: e.tagName.toLowerCase(),
    id: e.id,
    href: e.getAttribute('href'),
    text: (e.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 80),
    outline: { style: s.outlineStyle, width: parseFloat(s.outlineWidth) || 0, color: s.outlineColor },
    backdrop: ${'BACKDROP_OF'}(e),
  };
})()`;

/** The backdrop stack behind an element: every ancestor background colour
 * with alpha, bottom-up, plus the colours of any gradient image met on the
 * way (each is a candidate backdrop — contrast is judged against the worst). */
const BACKDROP_FUNCTION = `function BACKDROP_OF(start) {
  const layers = [];
  const gradients = [];
  const parse = (value) => {
    const m = /rgba?\\(([^)]+)\\)/.exec(value);
    if (!m) return null;
    const p = m[1].split(',').map((x) => parseFloat(x));
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  for (let node = start; node && node.nodeType === 1; node = node.parentElement) {
    const s = getComputedStyle(node);
    const bg = parse(s.backgroundColor);
    if (bg && bg.a > 0) layers.push(bg);
    if (s.backgroundImage && s.backgroundImage !== 'none') {
      const colours = [];
      const re = /rgba?\\([^)]+\\)/g;
      let m;
      while ((m = re.exec(s.backgroundImage)) !== null) { const c = parse(m[0]); if (c && c.a > 0) colours.push(c); }
      gradients.push(colours);
    }
  }
  return { layers: layers.reverse(), gradients };
}`;

/** Every element that directly carries rendered text, with its foreground,
 * size, weight and backdrop. */
const TEXT_SCRIPT = `(() => {
  ${BACKDROP_FUNCTION}
  const parse = (value) => {
    const m = /rgba?\\(([^)]+)\\)/.exec(value);
    if (!m) return null;
    const p = m[1].split(',').map((x) => parseFloat(x));
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const pathOf = (e) => {
    const parts = [];
    for (let n = e; n && n.nodeType === 1 && n !== document.body; n = n.parentElement) {
      const siblings = n.parentElement ? Array.from(n.parentElement.children).filter((c) => c.tagName === n.tagName) : [n];
      parts.unshift(n.tagName.toLowerCase() + (n.id ? '#' + n.id : siblings.length > 1 ? ':nth-of-type(' + (siblings.indexOf(n) + 1) + ')' : ''));
    }
    return parts.join('>');
  };
  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  for (let t = walker.nextNode(); t; t = walker.nextNode()) {
    if (!t.textContent || !t.textContent.trim()) continue;
    const e = t.parentElement;
    if (!e || seen.has(e) || e.closest('script,style,noscript')) continue;
    if (e.getClientRects().length === 0) continue;
    seen.add(e);
    const s = getComputedStyle(e);
    out.push({
      path: pathOf(e),
      text: t.textContent.replace(/\\s+/g, ' ').trim().slice(0, 60),
      color: parse(s.color),
      fontSize: parseFloat(s.fontSize),
      fontWeight: parseInt(s.fontWeight, 10) || 400,
      backdrop: BACKDROP_OF(e),
    });
  }
  return out;
})()`;

const ACTIVE_WITH_BACKDROP_SCRIPT = `(() => { ${BACKDROP_FUNCTION} return ${ACTIVE_SCRIPT.replace("${'BACKDROP_OF'}", 'BACKDROP_OF')}; })()`;

const AFTER_ACTIVATION_SCRIPT = `(() => {
  const all = Array.from(document.querySelectorAll('*'));
  const target = document.querySelector(':target');
  return {
    hash: location.hash,
    targetId: target ? target.id : null,
    targetIndex: target ? all.indexOf(target) : -1,
    targetTag: target ? target.tagName.toLowerCase() : null,
    targetText: target ? (target.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 80) : null,
  };
})()`;

/** The rendered text elements inside the current `:target`, measured the
 * same way as the page-wide sweep (the targeted row changes backdrop). */
const TARGET_TEXT_SCRIPT = TEXT_SCRIPT.replace('document.createTreeWalker(document.body,', "document.createTreeWalker(document.querySelector(':target') || document.createElement('div'),");

// ---------------------------------------------------------------------------
// Shapes returned by the scripts.

export interface FocusableElement {
  readonly index: number;
  readonly tag: string;
  readonly id: string;
  readonly href: string | null;
  readonly tabindex: string | null;
  readonly text: string;
  readonly rendered: boolean;
}

interface Rgba {
  readonly r: number;
  readonly g: number;
  readonly b: number;
  readonly a: number;
}

interface Backdrop {
  readonly layers: readonly Rgba[];
  readonly gradients: readonly (readonly Rgba[])[];
}

interface ActiveElement {
  readonly index: number;
  readonly tag: string;
  readonly id: string;
  readonly href: string | null;
  readonly text: string;
  readonly outline: { readonly style: string; readonly width: number; readonly color: string };
  readonly backdrop: Backdrop;
}

interface TextElement {
  readonly path: string;
  readonly text: string;
  readonly color: Rgba | null;
  readonly fontSize: number;
  readonly fontWeight: number;
  readonly backdrop: Backdrop;
}

interface Activation {
  readonly hash: string;
  readonly targetId: string | null;
  readonly targetIndex: number;
  readonly targetTag: string | null;
  readonly targetText: string | null;
}

// ---------------------------------------------------------------------------
// WCAG 2.x contrast arithmetic (pure; unit-tested against hand-typed pairs).

export interface Rgb {
  readonly r: number;
  readonly g: number;
  readonly b: number;
}

function channel(value: number): number {
  const c = value / 255;
  return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
}

/** Relative luminance per WCAG 2.x. */
export function relativeLuminance(colour: Rgb): number {
  return 0.2126 * channel(colour.r) + 0.7152 * channel(colour.g) + 0.0722 * channel(colour.b);
}

/** Contrast ratio (1..21) between two opaque colours. */
export function contrastRatio(foreground: Rgb, background: Rgb): number {
  const a = relativeLuminance(foreground);
  const b = relativeLuminance(background);
  const [light, dark] = a >= b ? [a, b] : [b, a];
  return (light + 0.05) / (dark + 0.05);
}

/** Source-over compositing of `top` (with alpha) on an opaque `bottom`. */
export function composite(top: Rgba, bottom: Rgb): Rgb {
  const a = Math.max(0, Math.min(1, top.a));
  return {
    r: Math.round(top.r * a + bottom.r * (1 - a)),
    g: Math.round(top.g * a + bottom.g * (1 - a)),
    b: Math.round(top.b * a + bottom.b * (1 - a)),
  };
}

/** WCAG AA threshold: 3:1 for large text (≥ 24px, or ≥ 18.66px bold), else 4.5:1. */
export function aaThreshold(fontSizePx: number, fontWeight: number): number {
  return fontSizePx >= 24 || (fontSizePx >= 18.66 && fontWeight >= 700) ? 3 : 4.5;
}

const CANVAS_WHITE: Rgb = { r: 255, g: 255, b: 255 };

/** Every opaque backdrop the element may sit on: the layers composited
 * bottom-up from the canvas, forking at each gradient into one candidate
 * per gradient colour plus the see-through case. */
export function candidateBackdrops(backdrop: Backdrop): readonly Rgb[] {
  let candidates: Rgb[] = [CANVAS_WHITE];
  const gradientQueue = [...backdrop.gradients].reverse();
  for (const layer of backdrop.layers) {
    candidates = candidates.map((below) => composite(layer, below));
    const gradient = gradientQueue.shift();
    if (gradient !== undefined && gradient.length > 0) {
      candidates = [...candidates, ...candidates.flatMap((below) => gradient.map((stop) => composite(stop, below)))];
    }
  }
  for (const gradient of gradientQueue) {
    if (gradient.length > 0) candidates = [...candidates, ...candidates.flatMap((below) => gradient.map((stop) => composite(stop, below)))];
  }
  return dedupe(candidates);
}

function dedupe(colours: readonly Rgb[]): readonly Rgb[] {
  const seen = new Map<string, Rgb>();
  for (const colour of colours) seen.set(`${colour.r},${colour.g},${colour.b}`, colour);
  return [...seen.values()];
}

/** The worst contrast of `foreground` against any candidate backdrop. */
export function worstContrast(foreground: Rgba, backdrop: Backdrop): { readonly ratio: number; readonly against: Rgb } {
  let worst: { ratio: number; against: Rgb } | undefined;
  for (const candidate of candidateBackdrops(backdrop)) {
    const ratio = contrastRatio(composite(foreground, candidate), candidate);
    if (worst === undefined || ratio < worst.ratio) worst = { ratio, against: candidate };
  }
  return worst ?? { ratio: 1, against: CANVAS_WHITE };
}

function parseColour(value: string): Rgba | null {
  const match = /rgba?\(([^)]+)\)/.exec(value);
  if (match === null) return null;
  const parts = (match[1] as string).split(',').map((part) => Number.parseFloat(part));
  return { r: parts[0] ?? 0, g: parts[1] ?? 0, b: parts[2] ?? 0, a: parts.length > 3 ? (parts[3] as number) : 1 };
}

function hex(colour: Rgb): string {
  return `#${[colour.r, colour.g, colour.b].map((c) => c.toString(16).padStart(2, '0')).join('')}`;
}

// ---------------------------------------------------------------------------
// The checks.

export type ViolationKind =
  | 'non-native-control'
  | 'unreachable-by-tab'
  | 'focus-order-differs-from-document-order'
  | 'reverse-order-differs'
  | 'keyboard-trap'
  | 'focus-not-visible'
  | 'focus-indicator-contrast'
  | 'fragment-target-missing'
  | 'activation-did-not-reach-target'
  | 'focus-did-not-continue-from-target'
  | 'unnamed-accessible-node'
  | 'accessible-link-count-differs'
  | 'text-contrast'
  | 'expected-target-absent'
  | 'disclosure-did-not-open';

export interface Violation {
  readonly kind: ViolationKind;
  readonly where: string;
  readonly detail: string;
}

export interface FocusTraceReport {
  readonly forward: readonly string[];
  readonly reverse: readonly string[];
  readonly population: number;
  readonly reached: number;
}

export interface ActivationReport {
  readonly href: string;
  readonly targetId: string | null;
  readonly targetTag: string | null;
  readonly continuedTo: string | null;
}

export interface ContrastMeasurement {
  readonly path: string;
  readonly text: string;
  readonly foreground: string;
  readonly against: string;
  readonly ratio: number;
  readonly threshold: number;
}

export interface AxReport {
  readonly nodes: number;
  readonly byRole: Readonly<Record<string, number>>;
  readonly unnamed: readonly string[];
}

export interface DisclosureReport {
  /** Native disclosures (`<details>`) on the page, each opened by Enter on its summary. */
  readonly population: number;
  readonly opened: number;
}

export interface AccessibilityReport {
  readonly label: string;
  readonly url: string;
  readonly focusables: readonly FocusableElement[];
  readonly disclosures: DisclosureReport;
  readonly focusTrace: FocusTraceReport;
  readonly activations: readonly ActivationReport[];
  readonly accessibilityTree: AxReport;
  readonly contrast: { readonly measured: number; readonly minimumRatio: number; readonly worst: readonly ContrastMeasurement[] };
  readonly violations: readonly Violation[];
}

const NATIVE_CONTROL_TAGS = new Set(['a', 'div', 'summary']);
// Unique landmarks (banner, main, contentinfo) need no name; regions and
// navigations, which may repeat, do.
const NAMED_ROLES = new Set(['link', 'heading', 'region', 'navigation']);

function describe(element: { readonly tag: string; readonly id: string; readonly href: string | null; readonly text: string }): string {
  return `${element.tag}${element.id === '' ? '' : `#${element.id}`}${element.href === null ? '' : `[href=${element.href}]`} "${element.text.slice(0, 40)}"`;
}

const SUMMARY_INDEXES_SCRIPT = `(() => {
  const all = Array.from(document.querySelectorAll('*'));
  return all.flatMap((element, index) => (element.tagName === 'SUMMARY' && element.parentElement && element.parentElement.tagName === 'DETAILS') ? [index] : []);
})()`;

const OPEN_DISCLOSURES_SCRIPT = `(() => { document.querySelectorAll('details').forEach((details) => { details.open = true; }); return null; })()`;

export interface CheckOptions {
  /** Element ids the page must reach by keyboard (e.g. every depth target). */
  readonly expectedTargets?: readonly string[];
  /** Cap on fragment links to activate (all when undefined). */
  readonly maxActivations?: number;
}

/** Runs every check against the page at `url`. */
export async function checkPolarisAccessibility(page: BrowserPage, url: string, label: string, options: CheckOptions = {}): Promise<AccessibilityReport> {
  const violations: Violation[] = [];
  await page.navigate(url);

  // 0. Progressive disclosure (PWB-REQ-011): every native disclosure opens
  // by a real Enter press on its summary, so the populations behind them
  // are keyboard-reachable; then every disclosure is opened so the rest of
  // the checks see the complete page. `reopen` restores that state after
  // each navigation below.
  const summaries = await page.evaluate<readonly number[]>(SUMMARY_INDEXES_SCRIPT);
  let opened = 0;
  for (const index of summaries) {
    const before = await page.evaluate<boolean>(`(() => { const all = document.querySelectorAll('*'); const s = all[${index}]; s.focus(); return s.parentElement.open; })()`);
    await page.press('Enter');
    const after = await page.evaluate<boolean>(`document.querySelectorAll('*')[${index}].parentElement.open`);
    if (after === before) {
      violations.push({ kind: 'disclosure-did-not-open', where: `summary[${index}]`, detail: `Enter on the summary left its disclosure ${before ? 'open' : 'closed'}` });
    } else if (after) {
      opened += 1;
    }
  }
  const reopen = async (): Promise<void> => {
    await page.navigate(url);
    await page.evaluate<null>(OPEN_DISCLOSURES_SCRIPT);
  };
  await reopen();

  // 1. The focusable population: native links and named keyboard-scrollable
  // regions only — nothing a pointer alone can operate.
  const focusables = await page.evaluate<readonly FocusableElement[]>(POPULATION_SCRIPT);
  for (const element of focusables) {
    const native = element.tag === 'a' && element.href !== null;
    const region = element.tag === 'div' && element.tabindex === '0';
    const disclosure = element.tag === 'summary';
    if (!native && !region && !disclosure) violations.push({ kind: 'non-native-control', where: describe(element), detail: `focusable ${element.tag} is neither a link, a disclosure summary nor a tabindex="0" region` });
    if (!NATIVE_CONTROL_TAGS.has(element.tag)) violations.push({ kind: 'non-native-control', where: describe(element), detail: `unexpected focusable tag ${element.tag}` });
  }
  const expectedIds = new Set(focusables.map((element) => element.index));

  // 2. Forward focus trace by real Tab presses, until the sequence wraps.
  const forward: ActiveElement[] = [];
  const seenIndexes = new Set<number>();
  for (let step = 0; step < focusables.length + 2; step += 1) {
    await page.press('Tab');
    const active = await page.evaluate<ActiveElement | null>(ACTIVE_WITH_BACKDROP_SCRIPT);
    if (active === null) break; // focus returned to the document: the sequence wrapped
    if (seenIndexes.has(active.index)) {
      if (forward.length > 0 && (forward[forward.length - 1] as ActiveElement).index === active.index) {
        violations.push({ kind: 'keyboard-trap', where: describe(active), detail: 'Tab left focus on the same element' });
      }
      break;
    }
    seenIndexes.add(active.index);
    forward.push(active);
  }
  for (const element of focusables) {
    if (!seenIndexes.has(element.index)) violations.push({ kind: 'unreachable-by-tab', where: describe(element), detail: 'never received focus in the Tab sequence' });
  }
  for (const active of forward) {
    if (!expectedIds.has(active.index)) violations.push({ kind: 'unreachable-by-tab', where: describe(active), detail: 'focused an element outside the enumerated population' });
  }
  const forwardIndexes = forward.map((active) => active.index);
  const documentOrder = [...forwardIndexes].sort((a, b) => a - b);
  if (forwardIndexes.some((index, position) => index !== documentOrder[position])) {
    violations.push({ kind: 'focus-order-differs-from-document-order', where: label, detail: `Tab order ${forwardIndexes.join(',')} vs document order ${documentOrder.join(',')}` });
  }
  // Visible focus with a 3:1 indicator on every stop.
  for (const active of forward) {
    if (active.outline.style === 'none' || active.outline.width <= 0) {
      violations.push({ kind: 'focus-not-visible', where: describe(active), detail: `outline ${active.outline.style} ${active.outline.width}px` });
      continue;
    }
    const colour = parseColour(active.outline.color);
    if (colour === null) continue;
    const worst = worstContrast(colour, active.backdrop);
    if (worst.ratio < 3) violations.push({ kind: 'focus-indicator-contrast', where: describe(active), detail: `${active.outline.color} on ${hex(worst.against)} = ${worst.ratio.toFixed(2)}:1 < 3:1` });
  }

  // 3. Reverse trace by Shift+Tab from the end must mirror the forward trace.
  const reverse: ActiveElement[] = [];
  const reverseSeen = new Set<number>();
  for (let step = 0; step < forward.length + 2; step += 1) {
    await page.press('Tab', { shift: true });
    const active = await page.evaluate<ActiveElement | null>(ACTIVE_WITH_BACKDROP_SCRIPT);
    if (active === null || reverseSeen.has(active.index)) break;
    reverseSeen.add(active.index);
    reverse.push(active);
  }
  const reverseIndexes = reverse.map((active) => active.index);
  const expectedReverse = [...forwardIndexes].reverse();
  if (reverseIndexes.length !== expectedReverse.length || reverseIndexes.some((index, position) => index !== expectedReverse[position])) {
    violations.push({ kind: 'reverse-order-differs', where: label, detail: `Shift+Tab visited ${reverseIndexes.length} of ${forward.length} in order ${reverseIndexes.slice(0, 12).join(',')}…` });
  }

  // 4. Every expected target exists and is reachable through some fragment link.
  const fragmentLinks = focusables.filter((element) => element.tag === 'a' && element.href !== null && element.href.startsWith('#') && element.href.length > 1);
  const fragmentTargets = new Set(fragmentLinks.map((element) => (element.href as string).slice(1)));
  for (const target of options.expectedTargets ?? []) {
    if (!fragmentTargets.has(target)) violations.push({ kind: 'expected-target-absent', where: `#${target}`, detail: 'no fragment link leads to this target' });
  }

  // 5. Activate every fragment link with a real Enter press: the target must
  // exist, become `:target`, and the next Tab must continue after it.
  const activations: ActivationReport[] = [];
  const targetContrast: TextElement[] = [];
  const measuredTargets = new Set<string>();
  const toActivate = options.maxActivations === undefined ? fragmentLinks : fragmentLinks.slice(0, options.maxActivations);
  const firstFocusable = focusables[0];
  for (const link of toActivate) {
    const targetId = (link.href as string).slice(1);
    // Re-activating the fragment already in the URL is a no-op in every
    // browser (no navigation, no new focus start point), so start each
    // activation from a page whose hash is not already the target.
    const currentHash = await page.evaluate<string>('location.hash');
    if (currentHash === `#${targetId}`) await reopen();
    await page.evaluate<null>(`(() => { const all = document.querySelectorAll('*'); all[${link.index}].focus(); return null; })()`);
    await page.press('Enter');
    const outcome = await page.evaluate<Activation>(AFTER_ACTIVATION_SCRIPT);
    const exists = await page.evaluate<boolean>(`document.getElementById(${JSON.stringify(targetId)}) !== null`);
    if (!exists) {
      violations.push({ kind: 'fragment-target-missing', where: describe(link), detail: `no element has id ${targetId}` });
      activations.push({ href: link.href as string, targetId: null, targetTag: null, continuedTo: null });
      continue;
    }
    if (outcome.targetId !== targetId) {
      violations.push({ kind: 'activation-did-not-reach-target', where: describe(link), detail: `after Enter, hash=${outcome.hash} :target=${outcome.targetId ?? 'none'}` });
    }
    await page.press('Tab');
    const next = await page.evaluate<ActiveElement | null>(ACTIVE_WITH_BACKDROP_SCRIPT);
    // The next Tab must land on the first focusable after the target; when
    // nothing focusable follows it, the sequence lawfully wraps (to the
    // browser chrome, then the first focusable).
    const following = focusables.find((element) => element.index > outcome.targetIndex);
    const continued = following === undefined
      ? next === null || (firstFocusable !== undefined && next.index === firstFocusable.index)
      : next !== null && next.index === following.index;
    if (!continued) {
      violations.push({ kind: 'focus-did-not-continue-from-target', where: describe(link), detail: next === null ? 'Tab after activation focused nothing' : `Tab went to ${describe(next)} (index ${next.index}; target ${outcome.targetIndex}, expected ${following === undefined ? 'wrap' : following.index})` });
    }
    if (!measuredTargets.has(targetId)) {
      measuredTargets.add(targetId);
      targetContrast.push(...(await page.evaluate<readonly TextElement[]>(TARGET_TEXT_SCRIPT)));
    }
    activations.push({ href: link.href as string, targetId: outcome.targetId, targetTag: outcome.targetTag, continuedTo: next === null ? null : describe(next) });
  }

  // 6. The non-visual representation: every link, heading and landmark has
  // an accessible name, and the tree carries one link per rendered link.
  const tree = await page.axTree();
  const live = tree.filter((node) => !node.ignored);
  const byRole: Record<string, number> = {};
  const unnamed: string[] = [];
  for (const node of live) {
    byRole[node.role] = (byRole[node.role] ?? 0) + 1;
    if (NAMED_ROLES.has(node.role) && node.name.trim() === '') unnamed.push(`${node.role}#${node.nodeId}`);
    if (node.role === 'button') violations.push({ kind: 'non-native-control', where: `ax ${node.role} "${node.name}"`, detail: 'a button role reached the accessibility tree' });
  }
  for (const entry of unnamed) violations.push({ kind: 'unnamed-accessible-node', where: entry, detail: 'no accessible name' });
  const renderedLinks = focusables.filter((element) => element.tag === 'a' && element.href !== null && element.rendered).length;
  const skipLinks = focusables.filter((element) => element.tag === 'a' && element.href !== null && !element.rendered).length;
  const axLinks = byRole['link'] ?? 0;
  if (axLinks !== renderedLinks + skipLinks) {
    violations.push({ kind: 'accessible-link-count-differs', where: label, detail: `accessibility tree has ${axLinks} links; the DOM has ${renderedLinks} rendered + ${skipLinks} off-screen` });
  }

  // 7. WCAG AA contrast over every rendered text element (plus the targeted rows).
  await reopen();
  const texts = [...(await page.evaluate<readonly TextElement[]>(TEXT_SCRIPT)), ...targetContrast];
  const measurements: ContrastMeasurement[] = [];
  for (const element of texts) {
    if (element.color === null) continue;
    const worst = worstContrast(element.color, element.backdrop);
    const threshold = aaThreshold(element.fontSize, element.fontWeight);
    const measurement = { path: element.path, text: element.text, foreground: hex(composite(element.color, worst.against)), against: hex(worst.against), ratio: Number(worst.ratio.toFixed(2)), threshold };
    measurements.push(measurement);
    if (worst.ratio < threshold) violations.push({ kind: 'text-contrast', where: `${element.path} "${element.text}"`, detail: `${measurement.foreground} on ${measurement.against} = ${measurement.ratio}:1 < ${threshold}:1` });
  }
  const ranked = [...measurements].sort((a, b) => a.ratio - b.ratio);

  return {
    label,
    url,
    focusables,
    disclosures: { population: summaries.length, opened },
    focusTrace: { forward: forward.map(describe), reverse: reverse.map(describe), population: focusables.length, reached: forward.length },
    activations,
    accessibilityTree: { nodes: live.length, byRole, unnamed },
    contrast: { measured: measurements.length, minimumRatio: ranked[0]?.ratio ?? 0, worst: ranked.slice(0, 10) },
    violations,
  };
}
