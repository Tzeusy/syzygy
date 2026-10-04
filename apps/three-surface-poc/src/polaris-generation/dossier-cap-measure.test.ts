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

describe('what heuristic discovery reads under the dossier cap on the design-prose fixture', () => {
  it('prints the measurement', () => { console.log('MEASURED', JSON.stringify(measured)); expect(measured.selectedBytes).toBeGreaterThan(0); });
});
