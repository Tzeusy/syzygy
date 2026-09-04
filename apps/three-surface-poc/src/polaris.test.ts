import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

describe('Polaris', () => {
  it('references every entity in at least one titled section (POC-REQ-030)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderPolarisPage(model);

    const sectionIds = new Set(
      [...html.matchAll(/data-polaris-section="([^"]+)"/g)].map((match) => match[1]),
    );
    const denominator = model.entities.length;
    let covered = 0;
    for (const entity of model.entities) {
      if (sectionIds.has(entity.id)) {
        covered += 1;
      }
    }
    expect(covered).toBe(denominator);
  });

  it('resolves every claim marker against the shared model, reporting the sweep denominator (POC-REQ-031)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderPolarisPage(model);

    const entityIds = new Set(model.entities.map((entity) => entity.id));
    const relationshipIds = new Set(model.relationships.map((relationship) => relationship.id));
    const syntheticRegionIds = new Set(['region:code-structure', 'region:work-items']);

    const markers = [...html.matchAll(/data-claim-provenance="([^"]+)"/g)].map((match) => match[1]);
    expect(markers.length).toBeGreaterThan(0);
    let resolved = 0;
    for (const markerId of markers) {
      if (
        entityIds.has(markerId as string) ||
        relationshipIds.has(markerId as string) ||
        syntheticRegionIds.has(markerId as string)
      ) {
        resolved += 1;
      }
    }
    expect(resolved).toBe(markers.length);
  });

  it('discloses Unknown in place rather than asserting positively (POC-REQ-032)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderPolarisPage(model);

    const unknownEntities = model.entities.filter(
      (entity): entity is typeof entity & { epistemic: { label: 'Unknown'; reason: string } } =>
        entity.epistemic.label === 'Unknown',
    );
    expect(unknownEntities.length).toBeGreaterThan(0);
    for (const entity of unknownEntities) {
      const sectionMatch = new RegExp(
        `data-polaris-section="${entity.id}">([\\s\\S]*?)</section>`,
      ).exec(html);
      expect(sectionMatch).not.toBeNull();
      const section = sectionMatch?.[1] ?? '';
      expect(section).toContain(`data-unknown-disclosure="${entity.id}"`);
      expect(section).toContain(entity.epistemic.reason);
      expect(section).not.toContain(`data-claim-provenance="${entity.id}"`);
    }
  });

  it('opens with the project-level groups in the required order, before any capability claim (PWB-REQ-010)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderPolarisPage(model);

    // Hand-typed oracle from task 3.1: never imported from the renderer.
    const required = ['overview', 'boundaries', 'architecture', 'v1', 'catalog', 'capability-detail', 'evidence-and-gaps'];
    const rendered = [...html.matchAll(/data-polaris-group="([^"]+)"/g)].map((match) => match[1]);
    expect(rendered).toEqual(required);

    // Every capability entity claim is rendered after the catalog group and
    // before the evidence group; the tally of such claims equals the model's.
    const catalogIndex = html.indexOf('data-polaris-group="catalog"');
    const detailIndex = html.indexOf('data-polaris-group="capability-detail"');
    const evidenceIndex = html.indexOf('data-polaris-group="evidence-and-gaps"');
    let placed = 0;
    for (const entity of model.entities) {
      const index = html.indexOf(`data-polaris-section="${entity.id}"`);
      if (index > detailIndex && index < evidenceIndex && detailIndex > catalogIndex) placed += 1;
    }
    expect(placed).toBe(model.entities.length);

    // The slice is labeled as one capability within the catalog, and the
    // old capability-first framing is gone.
    expect(html).toContain('data-polaris-capability-scope');
    expect(html).toContain('one capability within the complete catalog');
    expect(html).not.toContain('data-polaris-movement');
    expect(html).not.toContain('data-polaris-framing');
  });

  it('mutation check: removing an entity from coverage would fail the sweep', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderPolarisPage(model);
    const withoutOneSection = html.replace(
      new RegExp(`<section class="claim-section" data-polaris-section="${model.entities[0]?.id}"[\\s\\S]*?</section>`),
      '',
    );
    const sectionIds = new Set(
      [...withoutOneSection.matchAll(/data-polaris-section="([^"]+)"/g)].map((match) => match[1]),
    );
    expect(sectionIds.has(model.entities[0]?.id as string)).toBe(false);
  });
});
