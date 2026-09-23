import { rmSync, writeFileSync } from 'node:fs';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { afterEach, describe, expect, it } from 'vitest';

import { createDaemon, type RunningDaemon } from '@syzygy/cap1-daemon';

import { TAILNET_HOST } from './browser-origin.js';
import { findBrowserExecutable, launchBrowser, type BrowserPage } from './cdp-browser.js';
import { ORRERY_HUMAN_PATH } from './orrery.js';
import { POLARIS_HUMAN_PATH, renderPolarisPage } from './polaris.js';
import { POC_HUMAN_PATH, pocRoutes } from './routes.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';
import { fetchWithHost } from './test-http-client.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { ADMITTING_AUTHORITY, projectShapeFixtureGit } from './test-project-shape-fixture.js';
import { TRAJECTORY_HUMAN_PATH } from './trajectory.js';

const cleanups: string[] = [];
const running: RunningDaemon[] = [];
const browserExecutable = findBrowserExecutable();

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

type Family = 'badge' | 'tuple' | 'disclosure';
interface EncodingMember { readonly family: Family; readonly label: string; readonly tag: string }
const EXPECTED = {
  Observed: { token: '--observed', symbol: '●' },
  Unknown: { token: '--unknown', symbol: '?' },
} as const;

/** Parse served tags independently of the renderer and carry the nearest scope. */
function encodingMembers(html: string): EncodingMember[] {
  const body = html.replace(/<(style|script)\b[^>]*>[\s\S]*?<\/\1>/gi, '');
  const members: EncodingMember[] = [];
  const scopes: { tag: string; label?: string }[] = [];
  for (const match of body.matchAll(/<(\/)?([a-z][a-z0-9-]*)([^<>]*)>/gi)) {
    const [, closing, name, attrs = ''] = match;
    if (name === undefined) continue;
    if (closing !== undefined) {
      let index = -1;
      for (let i = scopes.length - 1; i >= 0; i--) if (scopes[i]?.tag === name) { index = i; break; }
      if (index >= 0) scopes.splice(index);
      continue;
    }
    const attribute = (key: string): string | undefined => new RegExp(`(?:^|\\s)${key}="([^"]*)"`).exec(attrs)?.[1];
    const classes = (attribute('class') ?? '').split(/\s+/);
    let inherited: string | undefined;
    for (let i = scopes.length - 1; i >= 0; i--) if (scopes[i]?.label !== undefined) { inherited = scopes[i]?.label; break; }
    const own = attribute('data-epistemic-label');
    const family: Family | undefined = classes.includes('epistemic') ? 'badge'
      : classes.includes('claim-tuple') ? 'tuple'
        : attribute('data-unknown-disclosure') !== undefined ? 'disclosure' : undefined;
    if (family !== undefined) {
      const label = family === 'badge' ? classes.find((cls) => cls.startsWith('epistemic-') && cls !== 'epistemic')?.slice('epistemic-'.length)
        : family === 'disclosure' ? 'Unknown' : own ?? inherited;
      if (label === undefined) throw new Error(`${family} has no local or inherited label: ${match[0]}`);
      members.push({ family, label: label[0]!.toUpperCase() + label.slice(1), tag: match[0] });
    }
    if (!/^(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)$/i.test(name) && !attrs.trimEnd().endsWith('/')) {
      scopes.push({ tag: name, label: attribute('data-epistemic-scope-label') });
    }
  }
  return members;
}

function verifyEncodingPopulation(html: string, checkTokenExclusivity = true, omitFamily?: Family): Record<Family, number> {
  const css = /<style>([\s\S]*?)<\/style>/.exec(html)?.[1];
  if (css === undefined) throw new Error('served page has no stylesheet');
  const cleanCss = css.replace(/\/\*[\s\S]*?\*\//g, '');
  const members = encodingMembers(html).filter((member) => member.family !== omitFamily);
  const counts: Record<Family, number> = { badge: 0, tuple: 0, disclosure: 0 };
  for (const member of members) {
    counts[member.family]++;
    const expected = EXPECTED[member.label as keyof typeof EXPECTED];
    if (expected === undefined) throw new Error(`undeclared label ${member.label}`);
    if (/\sstyle=/.test(member.tag)) throw new Error(`ad hoc inline treatment: ${member.tag}`);
    const scoped = member.family === 'tuple' && !member.tag.includes('data-epistemic-label=');
    const selector = member.family === 'badge' ? `.epistemic.epistemic-${member.label.toLowerCase()}`
      : member.family === 'tuple' ? scoped
        ? `[data-epistemic-scope-label="${member.label}"]`
        : `.claim-tuple[data-epistemic-label="${member.label}"]`
        : '[data-unknown-disclosure]';
    const rules = [...cleanCss.matchAll(/([^{}]+)\{([^{}]*)\}/g)];
    if (scoped) {
      const declaration = rules.find((rule) => rule[1]?.trim() === selector);
      const inheritedColor = rules.find((rule) => rule[1]?.trim() === '.claim-tuple:not([data-epistemic-label])');
      const inheritedSymbol = rules.find((rule) => rule[1]?.trim() === '.claim-tuple:not([data-epistemic-label])::before');
      if (!declaration?.[2]?.includes(`--claim-color: var(${expected.token});`) || !declaration[2].includes(`--claim-symbol: "${expected.symbol} ";`)) throw new Error(`wrong scope declaration for ${selector}`);
      if (!inheritedColor?.[2]?.includes('color: var(--claim-color);') || !inheritedSymbol?.[2]?.includes('content: var(--claim-symbol);')) throw new Error('scope inheritance consumer missing');
    } else {
      const color = rules.find((rule) => rule[1]?.includes(selector) && !rule[1]?.includes('::before') && /\bcolor:\s*var\(/.test(rule[2] ?? ''));
      const symbol = rules.find((rule) => rule[1]?.includes(`${selector}::before`) && rule[2]?.includes(`content: "${expected.symbol} "`));
      if (color?.[2]?.includes(`color: var(${expected.token});`) !== true) throw new Error(`wrong color for ${selector}`);
      if (symbol === undefined) throw new Error(`missing symbol for ${selector}`);
    }
  }
  const body = html.replace(/<(style|script)\b[^>]*>[\s\S]*?<\/\1>/gi, '');
  const independent = {
    badge: [...body.matchAll(/class="[^"]*\bepistemic epistemic-(?:observed|unknown)\b/g)].length,
    tuple: [...body.matchAll(/class="[^"]*\bclaim-tuple\b/g)].length,
    disclosure: [...body.matchAll(/\sdata-unknown-disclosure="/g)].length,
  };
  expect(counts).toEqual(independent);
  for (const rule of checkTokenExclusivity ? cleanCss.matchAll(/([^{}]+)\{([^{}]*)\}/g) : []) {
    if (!/var\(--(?:observed|unknown)\)/.test(rule[2] ?? '')) continue;
    const selector = rule[1] ?? '';
    if (!/(?:\.epistemic\.epistemic-|\.claim-tuple|\[data-unknown-disclosure\]|\[data-epistemic-scope-label=)/.test(selector)) {
      throw new Error(`epistemic token outside declared families: ${selector}`);
    }
  }
  return counts;
}

interface BrowserEncodingCensus {
  readonly query: Record<Family, number>;
  readonly walked: Record<Family, number>;
  readonly unmapped: number;
  readonly markedUnmapped: number;
  readonly treatmentFailures: readonly string[];
  readonly unnamedUnknowns: number;
}

/** Enumerates the actual post-script DOM and computed treatments in Chrome. */
async function browserEncodingCensus(page: BrowserPage): Promise<BrowserEncodingCensus> {
  return page.evaluate<BrowserEncodingCensus>(`(() => {
    const query = {
      badge: document.querySelectorAll('.epistemic.epistemic-observed, .epistemic.epistemic-unknown').length,
      tuple: document.querySelectorAll('.claim-tuple').length,
      disclosure: document.querySelectorAll('[data-unknown-disclosure]').length,
    };
    const walked = { badge: 0, tuple: 0, disclosure: 0 };
    const treatmentFailures = [];
    let unnamedUnknowns = 0;
    const nodes = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT);
    while (nodes.nextNode()) {
      const element = nodes.currentNode;
      const badge = element.classList.contains('epistemic') &&
        (element.classList.contains('epistemic-observed') || element.classList.contains('epistemic-unknown'));
      const tuple = element.classList.contains('claim-tuple');
      const disclosure = element.hasAttribute('data-unknown-disclosure');
      const family = badge ? 'badge' : tuple ? 'tuple' : disclosure ? 'disclosure' : undefined;
      if (!family) continue;
      walked[family]++;
      const label = badge ? (element.classList.contains('epistemic-observed') ? 'Observed' : 'Unknown')
        : tuple ? (element.getAttribute('data-epistemic-label') || element.closest('[data-epistemic-scope-label]')?.getAttribute('data-epistemic-scope-label'))
        : 'Unknown';
      const color = getComputedStyle(element).color;
      const symbol = getComputedStyle(element, '::before').content;
      const expectedColor = label === 'Observed' ? 'rgb(120, 225, 209)' : 'rgb(243, 197, 111)';
      const expectedSymbol = label === 'Observed' ? '●' : '?';
      if ((label !== 'Observed' && label !== 'Unknown') || color !== expectedColor || !symbol.includes(expectedSymbol)) {
        treatmentFailures.push(family + ':' + (label || 'missing'));
      }
      if (element.classList.contains('orrery-block') && element.classList.contains('unmapped') && !element.textContent.includes('Unknown')) unnamedUnknowns++;
    }
    const unmapped = [...document.querySelectorAll('.orrery-block.unmapped')];
    return {
      query,
      walked,
      unmapped: unmapped.length,
      markedUnmapped: unmapped.filter((element) => element.getAttribute('data-unknown-disclosure') === element.querySelector('a')?.getAttribute('href')?.slice(1)).length,
      treatmentFailures,
      unnamedUnknowns,
    };
  })()`);
}

function verifyRuntimeCensus(server: Record<Family, number>, runtime: BrowserEncodingCensus, orrery: boolean): void {
  expect(runtime.query).toEqual(runtime.walked);
  expect(runtime.treatmentFailures).toEqual([]);
  expect(runtime.unnamedUnknowns).toBe(0);
  expect(runtime.query.badge).toBe(server.badge);
  expect(runtime.query.tuple).toBe(server.tuple);
  expect(runtime.query.disclosure).toBe(server.disclosure + (orrery ? runtime.unmapped : 0));
  expect(runtime.markedUnmapped).toBe(runtime.unmapped);
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
      expect(html).toContain('<nav class="site-nav" aria-label="Three-surface POC sections">');
      expect(html).toContain('class="legend"');

      const rebound = await fetch(`${baseUrl}${path}`, {
        headers: { host: 'poc.attacker.invalid', origin: 'http://poc.attacker.invalid' },
      });
      expect(rebound.status).toBe(403);
    }
  });

  it('exhausts every served badge, tuple and Unknown disclosure on the three surfaces; Home is a separate diagnostic (POC-REQ-060)', async () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
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

    const counts = pages.map(({ path, html }) => ({ path, counts: verifyEncodingPopulation(html, path !== '/') }));
    const surfaces = counts.filter(({ path }) => path !== '/');
    expect(surfaces).toHaveLength(3);
    const total = surfaces.reduce((sum, page) => sum + Object.values(page.counts).reduce((a, b) => a + b, 0), 0);
    expect(total).toBeGreaterThan(80);
    expect(surfaces.find(({ path }) => path === POLARIS_HUMAN_PATH)?.counts.tuple).toBeGreaterThan(40);
    expect(counts.find(({ path }) => path === '/')?.counts.badge).toBeGreaterThan(0);
  });

  it.skipIf(browserExecutable === undefined)('counts the post-JavaScript DOM on all three served surfaces and kills an unmarked Orrery region', async () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    if (model.orrery.kind !== 'observed' || model.orrery.unmappedFileCount < 1) throw new Error('fixture needs an unmapped Orrery region');
    const start = await createDaemon({
      stateDir: join(tempDir('syzygy-poc-runtime-state-'), 'state'),
      routes: pocRoutes(() => model),
      port: 0,
    });
    if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
    running.push(start.daemon);
    const baseUrl = `http://${start.daemon.host}:${start.daemon.port}`;
    const browser = await launchBrowser(browserExecutable as string);
    const page = await browser.newPage();
    const directory = tempDir('syzygy-poc-runtime-pages-');
    try {
      let total = 0;
      let serverTotal = 0;
      for (const form of ['direct', 'tailnet'] as const) {
        for (const path of [POLARIS_HUMAN_PATH, TRAJECTORY_HUMAN_PATH, ORRERY_HUMAN_PATH]) {
          const response = form === 'direct' ? await fetch(`${baseUrl}${path}`)
            : await fetchWithHost(`${baseUrl}${path}`, TAILNET_HOST, { origin: `https://${TAILNET_HOST}` });
          expect(response.status).toBe(200);
          const html = await response.text();
          const server = verifyEncodingPopulation(html);
          const file = join(directory, `${form}-${path.slice(1)}.html`);
          writeFileSync(file, html);
          await page.navigate(pathToFileURL(file).href);
          const runtime = await browserEncodingCensus(page);
          verifyRuntimeCensus(server, runtime, path === ORRERY_HUMAN_PATH);
          total += Object.values(runtime.query).reduce((a, b) => a + b, 0);
          serverTotal += Object.values(server).reduce((a, b) => a + b, 0);
          if (path !== ORRERY_HUMAN_PATH) continue;
          expect(runtime.unmapped).toBe(1);
          expect(runtime.query.disclosure).toBe(server.disclosure + 1);
          const oldFragment = 'unmapped.dataset.unknownDisclosure = data.unmappedRegionEntityId;';
          expect(html).toContain(oldFragment);
          const mutant = html.replace(oldFragment, '');
          const mutantFile = join(directory, `${form}-orrery-unmarked.html`);
          writeFileSync(mutantFile, mutant);
          await page.navigate(pathToFileURL(mutantFile).href);
          const unmarked = await browserEncodingCensus(page);
          expect(() => verifyRuntimeCensus(server, unmarked, true)).toThrow();
          expect(unmarked.unmapped).toBe(1);
          expect(unmarked.markedUnmapped).toBe(0);
        }
      }
      expect(total).toBe(serverTotal + 2);
    } finally {
      await page.close();
      await browser.close();
    }
  }, 45_000);

  it.each([
    ['wrong Unknown token', (html: string) => html.replace('color: var(--unknown);', 'color: var(--observed);')],
    ['missing Unknown symbol', (html: string) => html.replace('content: "? ";', 'content: "";')],
    ['missing badge selector', (html: string) => html.replace('.epistemic.epistemic-observed, ', '')],
    ['missing local tuple selector', (html: string) => html.replace('.claim-tuple[data-epistemic-label="Observed"] { color:', '.missing-tuple { color:')],
    ['missing Unknown disclosure selector', (html: string) => html.replace(', [data-unknown-disclosure] { color:', ' { color:')],
    ['ad hoc inline tuple color', (html: string) => html.replace('class="claim-tuple"', 'class="claim-tuple" style="color:red"')],
    ['epistemic token outside the three families', (html: string) => html.replace('</style>', '.rogue { color: var(--unknown); }</style>')],
  ] as const)('rejects %s', (_name, mutate) => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    const html = renderPolarisPage(model);
    expect(verifyEncodingPopulation(html).tuple).toBeGreaterThan(40);
    const mutant = mutate(html);
    expect(mutant).not.toBe(html);
    expect(() => verifyEncodingPopulation(mutant)).toThrow();
  });

  it('rejects a checker that drops any one family or substitutes page count for element count', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    const html = renderPolarisPage(model);
    const counts = verifyEncodingPopulation(html);
    expect(Object.values(counts).reduce((a, b) => a + b, 0)).toBeGreaterThan(1);
    for (const family of ['badge', 'tuple', 'disclosure'] as const) {
      expect(counts[family]).toBeGreaterThan(0);
      expect(() => verifyEncodingPopulation(html, true, family)).toThrow();
    }
    expect(Object.values(counts).reduce((a, b) => a + b, 0)).not.toBe(1);
  });

  it('resolves a tuple without a local label from its nearest declaring scope', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    const html = renderPolarisPage(model);
    const hoisted = html.replace(
      /<p class="tuple-line"([^>]*)><span class="claim-tuple"([^>]*) data-epistemic-label="Observed"/,
      '<p class="tuple-line" data-epistemic-scope-label="Observed"$1><span class="claim-tuple"$2',
    );
    expect(hoisted).not.toBe(html);
    expect(verifyEncodingPopulation(hoisted)).toEqual(verifyEncodingPopulation(html));
    const nested = hoisted.replace(/(<p class="tuple-line" data-epistemic-scope-label="Observed"[^>]*>[^<]*<span class="claim-tuple"[^>]*>[\s\S]*?<\/span><\/p>)/, '<div data-epistemic-scope-label="Unknown">$1</div>');
    expect(nested).not.toBe(hoisted);
    expect(verifyEncodingPopulation(nested)).toEqual(verifyEncodingPopulation(html));
  });

  it('serves the exact state-(1) authority sentence on Polaris both directly and through the tailnet Host mount (PWB-REQ-005; PWB-RECON-01)', async () => {
    const sentence = "Owner-trusted only; same-tree forgeable from Syzygy&#39;s perspective. Digest detects drift, not authorship or attendance.";
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    if (model.projectShape.kind !== 'observed') throw new Error(`fixture shape is ${model.projectShape.kind}`);
    const start = await createDaemon({
      stateDir: join(tempDir('syzygy-poc-surface-state-'), 'state'),
      routes: pocRoutes(() => model),
      port: 0,
    });
    if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
    running.push(start.daemon);
    const baseUrl = `http://${start.daemon.host}:${start.daemon.port}`;
    const direct = await (await fetch(`${baseUrl}${POLARIS_HUMAN_PATH}`)).text();
    const mounted = await (await fetchWithHost(`${baseUrl}${POLARIS_HUMAN_PATH}`, TAILNET_HOST, { origin: `https://${TAILNET_HOST}` })).text();
    for (const html of [direct, mounted]) {
      const sentences = Array.from(html.matchAll(/data-parity-field="authority-disclosure"[^>]*>([^<]*)</g), (match) => match[1]);
      expect(sentences).toEqual([sentence, sentence, sentence]);
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
      const nav = html.match(/<nav class="site-nav" aria-label="Three-surface POC sections">.*?<\/nav>/s)?.[0] ?? '';
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
