// syzygy-za9v: Chrome teardown in a real browser. Under load the leader
// misses its close grace and is killed alone; a helper that then outlives
// the profile drain failed suites with "private browser profile still held
// by 3 process(es)" (the helper plus the two `cat` pipes the google-chrome
// wrapper forks). Freezing the network-service helper makes that helper
// deterministic: it cannot exit on its own, so close() succeeds only if
// teardown stops the whole private group. Without a browser the suite is
// skipped, never passed.
import { readdirSync, readFileSync } from 'node:fs';

import { describe, expect, it } from 'vitest';

import { findBrowserExecutable, launchBrowser } from './cdp-browser.js';

const executable = findBrowserExecutable();

function stat(pid: number): readonly string[] {
  const text = readFileSync(`/proc/${pid}/stat`, 'utf8');
  return text.slice(text.lastIndexOf(')') + 2).trim().split(/\s+/);
}

/** This launch's network-service helper only: its session is led by the
 * Chrome this process spawned (other suites may run their own Chrome). */
function ownNetworkHelpers(): number[] {
  const pids = readdirSync('/proc').filter((name) => /^\d+$/.test(name)).map(Number);
  const leaders = new Set(pids.filter((pid) => { try { return Number(stat(pid)[1]) === process.pid; } catch { return false; } }));
  return pids.filter((pid) => {
    try {
      return leaders.has(Number(stat(pid)[3])) && readFileSync(`/proc/${pid}/cmdline`, 'utf8').includes('--utility-sub-type=network.mojom.NetworkService');
    } catch { return false; }
  });
}

function alive(pid: number): boolean {
  try { return !/\) [ZX] /.test(readFileSync(`/proc/${pid}/stat`, 'utf8')); } catch { return false; }
}

describe.skipIf(executable === undefined || process.platform !== 'linux')('disposable Chrome teardown in a real browser', () => {
  it('closes and drains even when a helper cannot exit on its own', async () => {
    const browser = await launchBrowser(executable as string);
    let frozen: number[] = [];
    let closeAttempted = false;
    try {
      const page = await browser.newPage();
      await page.navigate('data:text/html,<p>teardown</p>');
      frozen = ownNetworkHelpers();
      // One helper of this launch, so the case is not vacuous.
      expect(frozen).toHaveLength(1);
      for (const pid of frozen) process.kill(pid, 'SIGSTOP');
      closeAttempted = true;
      await expect(browser.close()).resolves.toBeUndefined();
      expect(frozen.filter(alive)).toEqual([]);
    } finally {
      for (const pid of frozen.filter(alive)) process.kill(pid, 'SIGKILL');
      // A failure before close() would otherwise leak this browser.
      if (!closeAttempted) await browser.close().catch(() => undefined);
    }
  }, 60_000);
});
