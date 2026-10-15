// POC-REQ-014: the reader narrows the Trajectory board to the items marked
// with the governing-intent Unknown. Driven in Chrome over the served page:
// the checker enumerates the visible cards before and after checking the
// toggle. Every card carries the Unknown, so the narrowed board equals the
// un-narrowed one; a card this test injects without the mark proves the
// toggle narrows at all (a no-op toggle would pass the first half alone).
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest';

import { findBrowserExecutable, launchBrowser, type Browser } from './cdp-browser.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { renderTrajectoryPage } from './trajectory.js';

const executable = findBrowserExecutable();
const cleanups: string[] = [];

afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

const VISIBLE_CARDS = `Array.from(document.querySelectorAll('li.wi-card')).filter(card => getComputedStyle(card).display !== 'none').map(card => card.dataset.workItemId)`;

describe.skipIf(executable === undefined)('Trajectory narrowing to the governing-intent Unknown (POC-REQ-014)', () => {
  let browser: Browser;

  beforeAll(async () => {
    browser = await launchBrowser(executable as string);
  }, 60_000);

  afterAll(async () => {
    await browser?.close();
  });

  it('the narrowed board lists exactly the cards the board renders, and hides an unmarked one', async () => {
    const model = buildFixtureModel(cleanups);
    const directory = mkdtempSync(join(tmpdir(), 'syzygy-trajectory-narrowing-'));
    cleanups.push(directory);
    const file = join(directory, 'trajectory.html');
    writeFileSync(file, renderTrajectoryPage(model));
    const page = await browser.newPage();
    try {
      await page.navigate(pathToFileURL(file).href);
      const before = await page.evaluate<readonly string[]>(VISIBLE_CARDS);
      expect(before).toEqual(['bu-open1', 'bu-progress1', 'bu-blocked1', 'bu-closed-old', 'bu-closed-recent']);
      await page.evaluate(`(() => {
        const unmarked = document.querySelector('li.wi-card').cloneNode(true);
        unmarked.removeAttribute('data-governed-by');
        unmarked.dataset.workItemId = 'injected-unmarked';
        document.querySelector('ol.wi-list').appendChild(unmarked);
      })()`);
      expect(await page.evaluate<readonly string[]>(VISIBLE_CARDS)).toContain('injected-unmarked');
      await page.evaluate(`document.querySelector('label[for="narrow-governing-intent-unknown"]').click()`);
      expect(await page.evaluate<boolean>(`document.getElementById('narrow-governing-intent-unknown').checked`)).toBe(true);
      expect(await page.evaluate<readonly string[]>(VISIBLE_CARDS)).toEqual(before);
    } finally {
      await page.close();
    }
  });
});
