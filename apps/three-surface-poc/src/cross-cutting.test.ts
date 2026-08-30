import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { EPISTEMIC_ENCODING } from './design-tokens.js';
import { renderOrreryPage } from './orrery.js';
import { renderPolarisPage } from './polaris.js';
import { renderPocPage } from './routes.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { renderTrajectoryPage } from './trajectory.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function pages(model: ReturnType<typeof buildFixtureModel>): readonly { readonly name: string; readonly html: string }[] {
  return [
    { name: 'home', html: renderPocPage(model) },
    { name: 'polaris', html: renderPolarisPage(model) },
    { name: 'trajectory', html: renderTrajectoryPage(model) },
    { name: 'orrery', html: renderOrreryPage(model) },
  ];
}

describe('cross-cutting: no runtime fetch of external executable code (POC-REQ-021)', () => {
  it('sweeps every served page for a script reference to a foreign origin', () => {
    const model = buildFixtureModel(cleanups);
    const denominator = pages(model);
    expect(denominator.length).toBe(4);
    let external = 0;
    for (const page of denominator) {
      const scriptSrcs = [...page.html.matchAll(/<script[^>]*\ssrc="([^"]+)"/g)].map(
        (match) => match[1] as string,
      );
      for (const src of scriptSrcs) {
        if (/^https?:\/\//.test(src)) {
          external += 1;
        }
      }
    }
    expect(external).toBe(0);
  });
});

describe('cross-cutting: legend matches the declared encoding table on every surface (POC-REQ-060/061)', () => {
  it('every surface renders a legend entry for each declared epistemic encoding, and vice versa', () => {
    const model = buildFixtureModel(cleanups);
    const denominator = pages(model);
    for (const page of denominator) {
      for (const encoding of EPISTEMIC_ENCODING) {
        expect(page.html).toContain(`<span class="epistemic ${encoding.className}">`);
        expect(page.html).toContain(encoding.description);
      }
      // no legend entry that doesn't correspond to one of the two declared
      // encodings — the sweep's population is the full label set
      const legendMatches = [...page.html.matchAll(/<span class="epistemic (epistemic-\w+)">/g)];
      const legendClassNames = new Set(legendMatches.map((match) => match[1]));
      for (const className of legendClassNames) {
        expect(EPISTEMIC_ENCODING.some((encoding) => encoding.className === className)).toBe(true);
      }
    }
  });

  it('carries a skip link and keyboard-focusable native elements only for interactivity', () => {
    const model = buildFixtureModel(cleanups);
    for (const page of pages(model)) {
      expect(page.html).toContain('class="skip-link"');
      // interactive affordances are native <a>/<button> elements (keyboard
      // operable by default), never a bare div/span with a click handler
      expect(page.html).not.toMatch(/<div[^>]*onclick=/);
      expect(page.html).not.toMatch(/<span[^>]*onclick=/);
    }
  });

  it('respects reduced-motion preference identically across surfaces', () => {
    const model = buildFixtureModel(cleanups);
    for (const page of pages(model)) {
      expect(page.html).toContain('@media (prefers-reduced-motion: reduce)');
    }
  });
});
