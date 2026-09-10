// Task 4.4 (syzygy-1z3.20) — keyboard / non-visual navigation and WCAG AA
// contrast, measured in a real browser (PWB-REQ-016, PWB-REQ-011; RFC7-31,
// RFC7-34).
//
// The oracle lives outside the renderer: a headless Chrome/Chromium driven
// through `cdp-browser.ts` enumerates the focusable population from the
// live DOM, presses real Tab / Shift+Tab / Enter keys, reads its own
// accessibility tree and reports computed colours. This file only asserts
// on what the browser reports. Without a browser the suite is *skipped*,
// never passed: `npm run poc:accessibility-check` records the evidence
// with the browser identity it ran on.
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest';

import { findBrowserExecutable, launchBrowser, type Browser, type BrowserPage } from './cdp-browser.js';
import { aaThreshold, candidateBackdrops, checkPolarisAccessibility, composite, contrastRatio, relativeLuminance } from './polaris-accessibility.js';
import { renderProjectReading } from './polaris.js';
import { ACCESSIBILITY_VARIANTS, renderVariant, type AccessibilityVariant } from './polaris-accessibility-variants.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

// ---------------------------------------------------------------------------
// The contrast arithmetic, against hand-typed WCAG reference values.

describe('WCAG contrast arithmetic (pure)', () => {
  it('computes the reference luminances and ratios', () => {
    expect(relativeLuminance({ r: 255, g: 255, b: 255 })).toBeCloseTo(1, 6);
    expect(relativeLuminance({ r: 0, g: 0, b: 0 })).toBeCloseTo(0, 6);
    expect(contrastRatio({ r: 255, g: 255, b: 255 }, { r: 0, g: 0, b: 0 })).toBeCloseTo(21, 6);
    // #777777 on white is the canonical "just fails AA" pair: 4.48:1.
    expect(contrastRatio({ r: 119, g: 119, b: 119 }, { r: 255, g: 255, b: 255 })).toBeCloseTo(4.48, 2);
    // #767676 on white passes: 4.54:1.
    expect(contrastRatio({ r: 118, g: 118, b: 118 }, { r: 255, g: 255, b: 255 })).toBeCloseTo(4.54, 2);
    // Order does not matter.
    expect(contrastRatio({ r: 0, g: 0, b: 0 }, { r: 255, g: 255, b: 255 })).toBeCloseTo(21, 6);
  });

  it('applies the AA thresholds by size and weight', () => {
    expect(aaThreshold(16, 400)).toBe(4.5);
    expect(aaThreshold(23.9, 400)).toBe(4.5);
    expect(aaThreshold(24, 400)).toBe(3);
    expect(aaThreshold(18.66, 700)).toBe(3);
    expect(aaThreshold(18.66, 600)).toBe(4.5);
    expect(aaThreshold(18.5, 700)).toBe(4.5);
  });

  it('composites alpha over the backdrop and forks candidates at gradients', () => {
    expect(composite({ r: 0, g: 0, b: 0, a: 0.5 }, { r: 255, g: 255, b: 255 })).toEqual({ r: 128, g: 128, b: 128 });
    expect(composite({ r: 10, g: 20, b: 30, a: 1 }, { r: 255, g: 255, b: 255 })).toEqual({ r: 10, g: 20, b: 30 });
    const opaque = candidateBackdrops({ layers: [{ r: 7, g: 16, b: 18, a: 1 }], gradients: [] });
    expect(opaque).toEqual([{ r: 7, g: 16, b: 18 }]);
    const withGradient = candidateBackdrops({ layers: [{ r: 7, g: 16, b: 18, a: 1 }], gradients: [[{ r: 23, g: 50, b: 56, a: 1 }]] });
    expect(withGradient).toEqual([
      { r: 7, g: 16, b: 18 },
      { r: 23, g: 50, b: 56 },
    ]);
    // A translucent panel over a gradient body keeps both candidates.
    const stacked = candidateBackdrops({ layers: [{ r: 7, g: 16, b: 18, a: 1 }, { r: 12, g: 24, b: 27, a: 0.5 }], gradients: [[{ r: 23, g: 50, b: 56, a: 1 }]] });
    expect(stacked).toHaveLength(2);
  });
});

// ---------------------------------------------------------------------------
// The browser-measured checks.

const executable = findBrowserExecutable();

describe.skipIf(executable === undefined)('Polaris keyboard, non-visual and contrast checks in a real browser', () => {
  let browser: Browser;
  let pages: string;

  beforeAll(async () => {
    browser = await launchBrowser(executable as string);
    pages = mkdtempSync(join(tmpdir(), 'syzygy-poc-a11y-'));
  }, 60_000);

  afterAll(async () => {
    await browser?.close();
    if (pages !== undefined) rmSync(pages, { recursive: true, force: true });
  });

  function pageUrl(variant: AccessibilityVariant): { readonly url: string; readonly expectedTargets: readonly string[] } {
    const rendered = renderVariant(variant, cleanups);
    const file = join(pages, `${variant.id}.html`);
    writeFileSync(file, rendered.html);
    return { url: pathToFileURL(file).href, expectedTargets: rendered.expectedTargets };
  }

  it('keeps a separate desktop section rail and an in-flow mobile drawer', async () => {
    const { url } = pageUrl(ACCESSIBILITY_VARIANTS[0] as AccessibilityVariant);
    const page = await browser.newPage();
    try {
      await page.setViewport(1440, 1000);
      await page.navigate(url);
      const wide = await page.evaluate<{ open: boolean; separate: boolean; fits: boolean }>(`(() => {
        const rail = document.querySelector('.reading-sidebar').getBoundingClientRect();
        const main = document.querySelector('main').getBoundingClientRect();
        return { open: document.querySelector('.contents-list').open,
          separate: rail.right < main.left, fits: document.documentElement.scrollWidth <= innerWidth };
      })()`);
      expect(wide).toEqual({ open: true, separate: true, fits: true });
      await page.evaluate(`document.documentElement.style.scrollBehavior = 'auto'; scrollTo(0, 1600)`);
      const pinned = await page.evaluate<boolean>(`(() => {
        const rail = document.querySelector('.reading-sidebar').getBoundingClientRect();
        const nav = document.querySelector('.site-nav').getBoundingClientRect();
        return rail.top >= nav.bottom && rail.bottom <= innerHeight;
      })()`);
      expect(pinned).toBe(true);
      await page.setViewport(390, 844);
      await page.navigate('about:blank');
      await page.navigate(url);
      expect(await page.evaluate<boolean>(`!document.querySelector('.contents-list').open && getComputedStyle(document.querySelector('.reading-sidebar')).position === 'static' && document.documentElement.scrollWidth <= innerWidth`)).toBe(true);
      await page.evaluate(`document.querySelector('.contents-list summary').focus()`);
      await page.press('Enter');
      expect(await page.evaluate<boolean>(`document.querySelector('.contents-list').open`)).toBe(true);
      await page.evaluate(`document.documentElement.style.scrollBehavior = 'auto'; const rail = document.querySelector('.reading-sidebar'); scrollTo(0, rail.offsetTop + rail.offsetHeight + 100)`);
      expect(await page.evaluate<boolean>(`document.querySelector('.reading-sidebar').getBoundingClientRect().bottom <= 0`)).toBe(true);
      await page.evaluate(`document.querySelector('.quick-links a').click()`);
      const destination = await page.evaluate<{ top: number; navBottom: number }>(`({ top: document.querySelector('#polaris-group-v1').getBoundingClientRect().top, navBottom: document.querySelector('.site-nav').getBoundingClientRect().bottom })`);
      expect(destination.top).toBeGreaterThanOrEqual(destination.navBottom);
    } finally { await page.close(); }
  });

  it('keeps diagram labels legible and flow order unambiguous across widths', async () => {
    const rendered = renderVariant(ACCESSIBILITY_VARIANTS[0] as AccessibilityVariant, cleanups);
    const short = '```flow\nReceive --> Classify --> Route --> Spawn --> Act --> Log\n```';
    const long = '```flow\n' + Array.from({ length: 12 }, (_, index) => 'Stage ' + (index + 1)).join(' --> ') + '\n```';
    const relation = '```relations\n' + JSON.stringify([{ from: 'External clients', to: 'Module tools', description: 'Clients call the declared tool interface.' }]) + '\n```';
    const diagrams = renderProjectReading({ summary: short + '\n\n' + long + '\n\n' + relation, full: '', condensed: false,
      figures: [{ id: 'runtime', title: 'Inside the runtime', nodes: ['Daemon', 'Sessions', 'Tools'], explanation: 'Daemon spawns sessions. Sessions call tools.' }] });
    const file = join(pages, 'diagram-layout.html');
    writeFileSync(file, rendered.html.replace('</main>', `<div data-copy-role="project-fact">${diagrams}</div></main>`));
    const page = await browser.newPage();
    try {
      for (const width of [1440, 390]) {
        await page.setViewport(width, 1000);
        await page.navigate('about:blank');
        await page.navigate(pathToFileURL(file).href);
        const report = await page.evaluate<{ fits: boolean; legible: boolean; shortOrdered: boolean; longOrdered: boolean; figureVisible: boolean }>(`(() => {
          const flows = [...document.querySelectorAll('.source-flow')].filter(flow => !flow.closest('.source-figure')).map(flow => [...flow.querySelectorAll('.flow-node')].map(node => node.getBoundingClientRect()));
          const vertical = nodes => nodes.every((node, index) => index === 0 || node.top > nodes[index - 1].bottom);
          const labels = [...document.querySelectorAll('.flow-node, .relationship-nodes strong')];
          return { fits: document.documentElement.scrollWidth <= innerWidth,
            legible: labels.every(node => parseFloat(getComputedStyle(node).fontSize) >= 12 && node.getBoundingClientRect().width >= 40),
            shortOrdered: innerWidth > 800 ? flows[0].every(node => Math.abs(node.top - flows[0][0].top) < 1) : vertical(flows[0]),
            longOrdered: vertical(flows[1]),
            figureVisible: document.querySelector('[data-diagram-id="runtime"]').closest('details') === null && document.querySelectorAll('[data-diagram-id="runtime"] .flow-node').length === 3 };
        })()`);
        expect(report).toEqual({ fits: true, legible: true, shortOrdered: true, longOrdered: true, figureVisible: true });
      }
    } finally { await page.close(); }
  });

  it('opens a linked component guide and can reveal the complete declaration', async () => {
    const rendered = renderVariant(ACCESSIBILITY_VARIANTS[0] as AccessibilityVariant, cleanups);
    const guides = renderProjectReading({ summary: 'The two components have separate responsibilities.',
      full: 'Runtime\n\nKeeps time.\n\nTools\n\nExpose actions.', condensed: true,
      chapters: [{ id: 'test-runtime', title: 'Runtime', body: 'Keeps time.' }, { id: 'test-tools', title: 'Tools', body: 'Expose actions.' }] });
    const file = join(pages, 'component-guides.html');
    writeFileSync(file, rendered.html.replace('</main>', `<a id="guide-test-link" href="#polaris-guide-test-tools">Read tools</a><div data-copy-role="project-fact">${guides}</div></main>`));
    const page = await browser.newPage();
    try {
      await page.setViewport(390, 844);
      await page.navigate(pathToFileURL(file).href);
      expect(await page.evaluate<number>(`document.querySelectorAll('[data-component-guide] details[open]').length`)).toBe(0);
      // Native hashchange is queued after click. A fast collapse must survive it.
      expect(await page.evaluate<number>(`(async () => {
        const navigation = new Promise(resolve => addEventListener('hashchange', resolve, { once: true }));
        document.querySelector('#guide-test-link').click();
        const button = document.querySelector('.expand-declaration');
        button.click();
        button.click();
        await navigation;
        return document.querySelectorAll('[data-component-guide] details[open]').length;
      })()`)).toBe(0);
      await page.evaluate(`document.querySelector('#guide-test-link').focus()`);
      await page.press('Enter');
      expect(await page.evaluate<boolean>(`document.querySelector('#polaris-guide-test-tools details').open && document.querySelector('#polaris-guide-test-tools').closest('details') === null`)).toBe(true);
      await page.evaluate(`document.querySelector('.expand-declaration').focus()`);
      await page.press('Enter');
      expect(await page.evaluate<number>(`document.querySelectorAll('[data-component-guide] details[open]').length`)).toBe(2);
      expect(await page.evaluate<string>(`document.querySelector('.expand-declaration').getAttribute('aria-expanded')`)).toBe('true');
      await page.press('Enter');
      expect(await page.evaluate<number>(`document.querySelectorAll('[data-component-guide] details[open]').length`)).toBe(0);
      // Leaving the guide and returning through browser history is a new navigation.
      await page.evaluate(`new Promise(resolve => {
        addEventListener('hashchange', resolve, { once: true });
        location.hash = '#polaris-group-architecture';
      })`);
      expect(await page.evaluate<boolean>(`new Promise(resolve => {
        addEventListener('hashchange', () => resolve(document.querySelector('#polaris-guide-test-tools details').open), { once: true });
        history.back();
      })`)).toBe(true);
    } finally { await page.close(); }
  });

  it('keeps source records compact while citation targets remain keyboard-reachable', async () => {
    const { url } = pageUrl(ACCESSIBILITY_VARIANTS[0] as AccessibilityVariant);
    const page = await browser.newPage();
    try {
      await page.navigate(url);
      expect(await page.evaluate<boolean>(`(() => { const index = document.querySelector('[data-source-index]'); return index.scrollHeight > index.clientHeight && index.clientHeight <= innerHeight; })()`)).toBe(true);
      const id = await page.evaluate<string>(`document.querySelector('tr[data-polaris-source]').id`);
      await page.navigate('about:blank');
      await page.navigate(url + '#' + id);
      const closed = await page.evaluate<{ open: boolean; hidden: boolean; targetOutsideDisclosure: boolean }>(`(() => {
        const row = document.getElementById(${JSON.stringify(id)});
        const record = row.querySelector('.source-record');
        return { open: record.open, hidden: !record.querySelector('cite').checkVisibility(),
          targetOutsideDisclosure: row.closest('details') === null };
      })()`);
      expect(closed).toEqual({ open: false, hidden: true, targetOutsideDisclosure: true });
      await page.press('Tab');
      expect(await page.evaluate<boolean>(`document.activeElement === document.getElementById(${JSON.stringify(id)}).querySelector('.source-record summary')`)).toBe(true);
      await page.press('Enter');
      expect(await page.evaluate<boolean>(`document.getElementById(${JSON.stringify(id)}).querySelector('.source-record cite').checkVisibility()`)).toBe(true);
      await page.press('Enter');
      await page.press('Tab');
      const next = await page.evaluate<string | null>(`document.activeElement.closest('tr[data-polaris-source]')?.id ?? null`);
      expect(next).not.toBeNull();
      expect(next).not.toBe(id);
    } finally { await page.close(); }
  });

  for (const variant of ACCESSIBILITY_VARIANTS) {
    it(`${variant.id}: every distinction is keyboard-operable, named for assistive technology, and AA-contrasting`, async () => {
      const { url, expectedTargets } = pageUrl(variant);
      const page: BrowserPage = await browser.newPage();
      const report = await checkPolarisAccessibility(page, url, variant.id, { expectedTargets });
      await page.close();

      // The denominators must be real before a zero can mean anything.
      expect(report.focusTrace.population).toBeGreaterThan(10);
      expect(report.focusTrace.reached).toBe(report.focusTrace.population);
      expect(report.focusTrace.reverse).toHaveLength(report.focusTrace.forward.length);
      expect(report.activations.length).toBeGreaterThan(5);
      expect(report.accessibilityTree.nodes).toBeGreaterThan(50);
      expect(report.accessibilityTree.byRole['heading'] ?? 0).toBeGreaterThan(5);
      expect(report.accessibilityTree.byRole['link']).toBeGreaterThan(5);
      expect(report.contrast.measured).toBeGreaterThan(50);
      expect(report.contrast.minimumRatio).toBeGreaterThanOrEqual(4.5);
      expect(expectedTargets.length).toBeGreaterThan(0);

      expect(report.violations).toEqual([]);
    }, 240_000);
  }
});
