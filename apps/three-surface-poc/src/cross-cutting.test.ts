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

describe('cross-cutting: the three doctrine planes stay distinct from epistemic labels', () => {
  const expected = [
    { id: 'polaris', title: 'Polaris', state: 'desired', phrase: 'Polaris · desired state · what this project is meant to be' },
    { id: 'trajectory', title: 'Trajectory', state: 'execution', phrase: 'Trajectory · execution state · what work is underway' },
    { id: 'orrery', title: 'Orrery', state: 'observed', phrase: 'Orrery · observed state · what code and evidence show' },
  ] as const;

  function checkLegend(html: string): void {
    const mappings = [...html.matchAll(/data-surface-state-map="([^"]+)">([^<]+)<\/span>/g)]
      .map((match) => [match[1], match[2]]);
    expect(mappings).toEqual(expected.map(({ id, title, state }) => [id, `${title} holds the ${state} state`]));
  }

  it('names each page plane once outside the legend and each home panel once', () => {
    const model = buildFixtureModel(cleanups);
    const rendered = pages(model);
    expect(model.surfaces.map(({ id, state }) => [id, state])).toEqual(expected.map(({ id, state }) => [id, state]));
    for (const page of rendered) checkLegend(page.html);
    for (const plane of expected) {
      const html = rendered.find((page) => page.name === plane.id)!.html;
      expect([...html.matchAll(new RegExp(`data-surface-plane="${plane.id}"`, 'g'))]).toHaveLength(1);
      expect(html).toContain(`>${plane.phrase}</div>`);
      expect([...rendered[0]!.html.matchAll(new RegExp(`data-surface-plane="${plane.id}"`, 'g'))]).toHaveLength(1);
      expect(rendered[0]!.html).toContain(`>${plane.state} state</div>`);
    }
    expect(rendered.map(page => (page.html.match(/data-surface-state-map=/g) ?? []).length)).toEqual([3, 3, 3, 3]);
  });

  it('detects a misspelled legend mapping and a swapped surface plane', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderPolarisPage(model);
    expect(() => checkLegend(html.replace('Polaris holds the desired state', 'Polaris holds the proposed state'))).toThrow();
    const swapped = { ...model, surfaces: model.surfaces.map(surface =>
      surface.id === 'trajectory' ? { ...surface, state: 'observed' as const }
        : surface.id === 'orrery' ? { ...surface, state: 'execution' as const } : surface) };
    const page = renderTrajectoryPage(swapped);
    expect(page).not.toContain(`>${expected[1].phrase}</div>`);
    expect(() => checkLegend(page)).toThrow();
  });
});
