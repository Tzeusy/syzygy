import { escapeHtml } from '@syzygy/cap1-daemon';
import type { PocModel } from '@syzygy/three-surface-poc-core';

import { exactTablesSection } from './exact-tables.js';
import { pageShell } from './page-shell.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';

export const ORRERY_HUMAN_PATH = '/orrery' as const;
export const ORRERY_TAILNET_PATH = `${TAILNET_MOUNT_PREFIX}/orrery` as const;

interface OrreryDataIsland {
  readonly revision: string;
  readonly districts: readonly {
    readonly id: string;
    readonly path: string;
    readonly fileCount: number;
    readonly totalBytes: number;
    readonly languages: readonly string[];
  }[];
  readonly mappedRegions: readonly {
    readonly id: string;
    readonly path: string;
    readonly capabilityId: string;
    readonly sizeBytes: number;
  }[];
  readonly mappedFileCount: number;
  readonly unmappedFileCount: number;
  readonly totalFileCount: number;
  readonly unmappedRegionEntityId: string;
}

const ORRERY_STYLE = `
  .unavailable-notice { max-width: 78ch; margin: 1rem 0; }
  #orrery-canvas {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(7rem, 1fr));
    gap: .6rem;
    padding: 1.5rem 0 2rem;
    min-height: 8rem;
  }
  .orrery-block {
    position: relative;
    border: 1px solid var(--line);
    background: linear-gradient(160deg, #102126, var(--panel));
    padding: .6rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    min-height: var(--block-height, 4rem);
  }
  .orrery-block .block-label { font-family: var(--font-mono); font-size: .68rem; color: var(--muted); }
  .orrery-block.mapped { border-color: var(--cyan); }
  .orrery-block.mapped a { display: block; color: var(--cyan); text-decoration: none; font-size: .78rem; }
  .orrery-block.unmapped { border-style: dashed; border-color: var(--unknown); }
  .orrery-block.unmapped a { color: var(--unknown); font-size: .78rem; text-decoration: none; }
  .orrery-scope { max-width: 78ch; }
`;

/**
 * Deterministic (POC-REQ-050): a pure function of the JSON island's data,
 * itself the same `model.orrery` object served at `GET /api/poc` — no
 * randomness, no server-derived layout hints beyond directory grouping and
 * declared mappings.
 */
const CLIENT_SCRIPT = `
(function () {
  var dataEl = document.getElementById('orrery-data');
  var canvas = document.getElementById('orrery-canvas');
  if (!dataEl || !canvas) return;
  var data;
  try { data = JSON.parse(dataEl.textContent || '{}'); } catch (e) { return; }
  canvas.innerHTML = '';
  var maxBytes = 1;
  (data.districts || []).forEach(function (d) { if (d.totalBytes > maxBytes) maxBytes = d.totalBytes; });

  (data.districts || []).slice().sort(function (a, b) {
    return a.path < b.path ? -1 : a.path > b.path ? 1 : 0;
  }).forEach(function (district) {
    var block = document.createElement('div');
    block.className = 'orrery-block';
    block.dataset.parityField = 'orrery-district';
    block.dataset.districtId = district.id;
    var height = 3 + (district.totalBytes / maxBytes) * 6;
    block.style.setProperty('--block-height', height.toFixed(2) + 'rem');
    var label = document.createElement('span');
    label.className = 'block-label';
    label.textContent = district.path + ' (' + district.fileCount + ' files)';
    block.appendChild(label);
    canvas.appendChild(block);
  });

  (data.mappedRegions || []).forEach(function (region) {
    var block = document.createElement('div');
    block.className = 'orrery-block mapped';
    var link = document.createElement('a');
    link.href = '#' + region.id;
    link.dataset.parityField = 'orrery-mapped-region';
    link.textContent = region.path;
    block.appendChild(link);
    canvas.appendChild(block);
  });

  if (data.unmappedFileCount > 0) {
    var unmapped = document.createElement('div');
    unmapped.className = 'orrery-block unmapped';
    var unmappedLink = document.createElement('a');
    unmappedLink.href = '#' + data.unmappedRegionEntityId;
    unmappedLink.dataset.parityField = 'orrery-unmapped-region';
    unmappedLink.textContent = 'Unmapped (' + data.unmappedFileCount + ' files)';
    unmapped.appendChild(unmappedLink);
    canvas.appendChild(unmapped);
  }
})();
`;

export function renderOrreryPage(model: PocModel): string {
  const orrery = model.orrery;
  let body: string;

  if (orrery.kind === 'unknown') {
    body = `<p class="unavailable-notice" data-unknown-disclosure="region:code-structure">Unknown — ${escapeHtml(orrery.reason)}. The exact tables below remain the honest record of what is known.</p>
    ${exactTablesSection(model)}`;
  } else {
    const island: OrreryDataIsland = {
      revision: orrery.revision,
      districts: orrery.districts,
      mappedRegions: orrery.mappedRegions,
      mappedFileCount: orrery.mappedFileCount,
      unmappedFileCount: orrery.unmappedFileCount,
      totalFileCount: orrery.totalFileCount,
      unmappedRegionEntityId: 'region:unmapped-code',
    };
    const islandJson = JSON.stringify(island).replace(/</g, '\\u003c');

    body = `
      <p class="orrery-scope notice" data-parity-field="orrery-scope">
        ${orrery.mappedFileCount} of ${orrery.totalFileCount} observed files sit in a declared mapping;
        <span data-parity-field="orrery-unmapped-count">${orrery.unmappedFileCount}</span> are unmapped and shown as an explicit Unknown region.
        Revision <code>${escapeHtml(orrery.revision.slice(0, 12))}</code>.
      </p>
      <noscript>
        <p class="unavailable-notice">The spatial city rendering requires JavaScript and is unavailable without it. The same facts are in the exact tables below.</p>
      </noscript>
      <section id="orrery-canvas" aria-label="Spatial code city (JavaScript-rendered; see exact tables for the no-script form)"></section>
      <script type="application/json" id="orrery-data">${islandJson}</script>
      <script>${CLIENT_SCRIPT}</script>
      ${exactTablesSection(model)}`;
  }

  return pageShell({
    title: 'Orrery · Syzygy three-surface POC',
    current: 'orrery',
    eyebrow: `Orrery · Butlers ${model.project.revision.slice(0, 12)}`,
    heading: 'Where the code lives',
    lede: 'A deterministic spatial map over observed directory structure and declared capability-to-code mappings. Unmapped code stays visibly Unknown.',
    extraStyle: ORRERY_STYLE,
    body,
    footer:
      orrery.kind === 'observed'
        ? `Code-structure revision <code>${escapeHtml(orrery.revision)}</code>.`
        : 'Code-structure region: Unknown.',
    escapeHtml,
  });
}
