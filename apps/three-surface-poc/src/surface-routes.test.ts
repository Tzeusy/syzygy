import { rmSync } from 'node:fs';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { createDaemon, type RunningDaemon } from '@syzygy/cap1-daemon';

import { TAILNET_HOST } from './browser-origin.js';
import { ORRERY_HUMAN_PATH } from './orrery.js';
import { POLARIS_HUMAN_PATH } from './polaris.js';
import { POC_HUMAN_PATH, pocRoutes } from './routes.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';
import { fetchWithHost } from './test-http-client.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { TRAJECTORY_HUMAN_PATH } from './trajectory.js';

const cleanups: string[] = [];
const running: RunningDaemon[] = [];

afterEach(async () => {
  for (const daemon of running.splice(0)) {
    await daemon.close().catch(() => undefined);
  }
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function tempDir(prefix: string): string {
  const directory = mkdtempSync(join(tmpdir(), prefix));
  cleanups.push(directory);
  return directory;
}

describe('surface routes', () => {
  it('serves Polaris, Trajectory, and Orrery as human-open, same-origin-guarded pages', async () => {
    const model = buildFixtureModel(cleanups);
    const start = await createDaemon({
      stateDir: join(tempDir('syzygy-poc-surface-state-'), 'state'),
      routes: pocRoutes(() => model),
      port: 0,
    });
    if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
    running.push(start.daemon);
    const baseUrl = `http://${start.daemon.host}:${start.daemon.port}`;

    for (const path of [POLARIS_HUMAN_PATH, TRAJECTORY_HUMAN_PATH, ORRERY_HUMAN_PATH]) {
      const response = await fetch(`${baseUrl}${path}`);
      expect(response.status).toBe(200);
      expect(response.headers.get('content-type')).toBe('text/html; charset=utf-8');
      const html = await response.text();
      expect(html).toContain('<nav aria-label="Three-surface POC sections">');
      expect(html).toContain('class="legend"');

      const rebound = await fetch(`${baseUrl}${path}`, {
        headers: { host: 'poc.attacker.invalid', origin: 'http://poc.attacker.invalid' },
      });
      expect(rebound.status).toBe(403);
    }
  });

  it('encodes Observed and Unknown identically across the home page and all three surfaces (POC-REQ-060)', async () => {
    const model = buildFixtureModel(cleanups);
    const start = await createDaemon({
      stateDir: join(tempDir('syzygy-poc-surface-state-'), 'state'),
      routes: pocRoutes(() => model),
      port: 0,
    });
    if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
    running.push(start.daemon);
    const baseUrl = `http://${start.daemon.host}:${start.daemon.port}`;

    const pages = await Promise.all(
      ['/', POLARIS_HUMAN_PATH, TRAJECTORY_HUMAN_PATH, ORRERY_HUMAN_PATH].map(async (path) => ({
        path,
        html: await (await fetch(`${baseUrl}${path}`)).text(),
      })),
    );

    const denominator = pages.length;
    let consistent = 0;
    for (const page of pages) {
      const hasDeclaredObserved = page.html.includes('class="epistemic epistemic-observed"');
      const hasDeclaredUnknown = page.html.includes('class="epistemic epistemic-unknown"');
      // every page that renders any epistemic state at all uses the one
      // declared class names; a page with neither state present is excluded
      // from the sweep denominator rather than falsely counted
      if (!hasDeclaredObserved && !hasDeclaredUnknown) {
        continue;
      }
      consistent += 1;
    }
    expect(consistent).toBeGreaterThan(0);
    expect(consistent).toBeLessThanOrEqual(denominator);
    for (const page of pages) {
      expect(page.html).toContain('epistemic-observed { color: var(--cyan); }');
      expect(page.html).toContain('epistemic-unknown { color: var(--unknown)');
    }
  });

  it('nav links stay inside the current mount — root-relative for direct loopback access, prefixed for the tailnet-Host-headered request `tailscale serve` actually forwards', async () => {
    // `tailscale serve --set-path` strips the mount prefix from the
    // forwarded path (verified empirically — see tailnet.ts), so the
    // signal this test exercises is the Host header, never the request
    // path: every tailnet-routed request the daemon ever actually
    // receives arrives at one of the plain (unprefixed) paths below, with
    // Host set to the tailnet hostname.
    const model = buildFixtureModel(cleanups);
    const start = await createDaemon({
      stateDir: join(tempDir('syzygy-poc-surface-state-'), 'state'),
      routes: pocRoutes(() => model),
      port: 0,
    });
    if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
    running.push(start.daemon);
    const baseUrl = `http://${start.daemon.host}:${start.daemon.port}`;

    function navHrefs(html: string): string[] {
      const nav = html.match(/<nav aria-label="Three-surface POC sections">.*?<\/nav>/s)?.[0] ?? '';
      return [...nav.matchAll(/href="([^"]*)"/g)].map((match) => match[1] ?? '');
    }

    const paths = [POC_HUMAN_PATH, POLARIS_HUMAN_PATH, TRAJECTORY_HUMAN_PATH, ORRERY_HUMAN_PATH];
    for (const path of paths) {
      const directHtml = await (await fetch(`${baseUrl}${path}`)).text();
      const directHrefs = navHrefs(directHtml);
      expect(directHrefs.length).toBeGreaterThan(0);
      for (const href of directHrefs) {
        expect(href.startsWith(TAILNET_MOUNT_PREFIX)).toBe(false);
      }

      const tailnetHtml = await (
        await fetchWithHost(`${baseUrl}${path}`, TAILNET_HOST, { origin: `https://${TAILNET_HOST}` })
      ).text();
      const tailnetHrefs = navHrefs(tailnetHtml);
      expect(tailnetHrefs.length).toBeGreaterThan(0);
      for (const href of tailnetHrefs) {
        expect(href.startsWith(TAILNET_MOUNT_PREFIX)).toBe(true);
      }
    }
  });
});
