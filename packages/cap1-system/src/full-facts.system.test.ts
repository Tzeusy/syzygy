// RT6 system test 1 — the epic's definition-of-done, automated: a real
// spawned daemon over a complete on-disk fixture repository serves the
// same facts through a browser-equivalent GET and an authenticated
// machine request. Every expected value below is a HARD-CODED literal
// (oracle independence); the cross-channel comparison is a sweep with a
// denominator over the facts the wire actually carried.

import { rmSync } from 'node:fs';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  readCredential,
  startDaemon,
  sweepWireParity,
  tempBase,
  writeCompleteFixture,
  type DaemonProcess,
  type WireFact,
} from './harness.js';

const cleanups: (() => Promise<void> | void)[] = [];

afterEach(async () => {
  for (const cleanup of cleanups.splice(0).reverse()) {
    await cleanup();
  }
});

async function startCompleteFixtureDaemon(): Promise<DaemonProcess> {
  const base = tempBase('syz-sys-full-');
  cleanups.push(() => rmSync(base, { recursive: true, force: true }));
  const fixtureRoot = join(base, 'fixture');
  writeCompleteFixture(fixtureRoot);
  const daemon = await startDaemon({
    fixtureRoot,
    stateDir: join(base, 'state'),
  });
  cleanups.push(async () => {
    await daemon.stop();
  });
  return daemon;
}

// The seven facet names, hard-coded — never imported from a vocabulary
// module.
const SEVEN_FACETS = [
  'Registered',
  'Shape present',
  'Human-understandable',
  'Observable',
  'Traceable',
  'Mission-ready',
  'Reconciled',
];

describe('RT6 — full-facts demonstration over the spawned daemon', () => {
  it('serves the human page with verbatim facts, labels, and the Why-this-answer drawer', async () => {
    const daemon = await startCompleteFixtureDaemon();

    const response = await fetch(`${daemon.baseUrl}/`);
    expect(response.status).toBe(200);
    expect(response.headers.get('content-type')).toBe('text/html; charset=utf-8');
    const html = await response.text();

    // Key verbatim facts, as literals.
    expect(html).toContain('Project prj-sys-fixture');
    expect(html).toContain('data-answer-name="Registered"');
    expect(html).toContain('data-answer-value="satisfied"');
    expect(html).toContain('data-epistemic-label="Observed"');
    expect(html).toContain('[Observed]');
    expect(html).toContain('[Unknown]');
    expect(html).toContain('The seven shape answers');
    // The explanation drawer, one per answer.
    expect(html).toContain('Why this answer?');
    const drawerCount = (html.match(/data-explains="/g) ?? []).length;
    expect(drawerCount).toBe(7);
    // Every one of the seven facets renders as its own answer article.
    for (const facet of SEVEN_FACETS) {
      expect(html).toContain(`data-answer-name="${facet}"`);
    }
  });

  it('serves the fixture overview at /entry', async () => {
    const daemon = await startCompleteFixtureDaemon();

    const response = await fetch(`${daemon.baseUrl}/entry`);
    expect(response.status).toBe(200);
    const html = await response.text();

    expect(html).toContain('data-entry-state="present"');
    // The fixture entry text, served verbatim (HTML-escaped as text).
    expect(html).toContain('# Syzygy system fixture overview');
    expect(html).toContain('This is the fixture entry document.');
    // The one fixed publication location, rendered.
    expect(html).toContain('.syzygy/intent/OVERVIEW.md');
  });

  it('serves the JSON facts to an authenticated machine request, and every served JSON fact appears in the HTML (sweep with denominator)', async () => {
    const daemon = await startCompleteFixtureDaemon();
    const token = readCredential(daemon.credentialPath);

    const machineResponse = await fetch(`${daemon.baseUrl}/api/project`, {
      headers: { authorization: `Bearer ${token}` },
    });
    expect(machineResponse.status).toBe(200);
    expect(machineResponse.headers.get('content-type')).toBe('application/json');
    const body = (await machineResponse.json()) as {
      kind: string;
      state: { current: { selection: string; facts: WireFact[] } };
    };

    expect(body.kind).toBe('project-evaluated');
    expect(body.state.current.selection).toBe('project:prj-sys-fixture');
    const jsonFacts = body.state.current.facts;
    expect(jsonFacts.map((fact) => fact.name)).toEqual(SEVEN_FACETS);
    const registered = jsonFacts.find((fact) => fact.name === 'Registered');
    expect(registered?.value).toBe('satisfied');
    expect(registered?.epistemic.label).toBe('Observed');

    // CROSS-CHANNEL PARITY FROM THE WIRE: every fact the JSON carries
    // must appear in the HTML with the same name, value, and label.
    // Denominator: the JSON fact set; numerator: facts asserted.
    const htmlResponse = await fetch(`${daemon.baseUrl}/`);
    const html = await htmlResponse.text();
    const asserted = sweepWireParity(jsonFacts, html);
    expect(asserted).toBe(jsonFacts.length);
    expect(jsonFacts.length).toBe(7);
  });
});
