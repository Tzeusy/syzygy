import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { measureDossierCapSelection, type DossierCapMeasurement } from './redis-shaped-measure.js';

let scratch = '', measured: DossierCapMeasurement;
beforeAll(async () => {
  scratch = mkdtempSync(join(tmpdir(), 'syzygy-dossier-cap-'));
  measured = await measureDossierCapSelection(join(scratch, 'repo'));
}, 120_000);
afterAll(() => rmSync(scratch, { recursive: true, force: true }));

describe('what heuristic discovery reads under the dossier cap on the design-prose fixture (no model)', () => {
  // Before the role signals of the prior (measured at the baseline commit): 4 of 18 core files, 134,671 bytes of them; 99,997 bytes of release notes, 60,050 of configuration and 3,065 of build files read.
  it('reads more of the core, and none of the release notes, configuration or build files, once the prior has role signals', () => {
    expect(measured).toMatchObject({ selectedBytes: 399_859, selectedBlobs: 19, partialBlobs: 2, coreRead: 10, coreReadBytes: 302_641, designDocsRead: 5 });
    expect(measured.bytesByClass).toEqual({ 'design-docs': 60_509, 'other-prose': 920, source: 338_430 });
    for (const unwanted of ['release-notes', 'configuration', 'build', 'tests', 'vendored']) expect(measured.bytesByClass[unwanted] ?? 0, unwanted).toBe(0);
  });
});
