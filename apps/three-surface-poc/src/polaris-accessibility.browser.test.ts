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
