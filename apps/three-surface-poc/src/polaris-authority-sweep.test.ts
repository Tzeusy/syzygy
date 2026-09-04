import { readFileSync, readdirSync, rmSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel } from '@syzygy/three-surface-poc-core';

import { parseNarrativeScript } from './polaris-narrative.js';
import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { ADMITTING_AUTHORITY, PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC, projectShapeFixtureGit } from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));

/** How the Polaris surface would be named if something cited it. */
const POLARIS_SURFACE = /(^|[^A-Za-z0-9-])\/polaris\b|polaris\.ts\b|apps\/three-surface-poc\/src\/polaris|\/api\/poc\b|^polaris$/i;

/** Hand-typed warrant id families (a new family must be added here). */
const WARRANT_FAMILIES = [
  /^(VIS|SEC|SDR|RFC\d+|CC-[A-Z]+|POC-REQ|PWB-REQ|CAP1-REQ)-\d+[a-z]?(\([a-z]\))?$/,
  /^(POC|POLARIS|PWB-STATE1-AMENDMENT)-DIR-\d{4}-\d{2}-\d{2}$/,
  /^P-\d+-ruling-\d{4}-\d{2}-\d{2}( \(decisions\/[A-Z0-9-]+\.md\))?$/,
  /^decisions\/[A-Z0-9-]+\.md$/,
  /^[a-z0-9-]+\/(POC|PWB|CAP1)-REQ-\d+$/,
];

function walk(directory: string, accept: (path: string) => boolean, out: string[] = []): string[] {
  for (const entry of readdirSync(directory)) {
    if (entry === 'node_modules' || entry === 'dist' || entry === '.git') continue;
    const path = join(directory, entry);
    if (statSync(path).isDirectory()) walk(path, accept, out);
    else if (accept(path)) out.push(path);
  }
  return out;
}

function machineReferences(model: PocModel, html: string): string[] {
  const refs: string[] = [];
  for (const entity of model.entities) for (const item of entity.provenance) refs.push(item.source, item.revision);
  for (const relationship of model.relationships) for (const item of relationship.provenance) refs.push(item.source, item.revision);
  const shape = model.projectShape;
  if (shape.kind === 'observed') {
    for (const source of shape.sources) refs.push(source.path, source.identity);
    for (const group of [shape.projectAccount, shape.items, shape.facts, Object.values(shape.classes)]) {
      for (const entry of group) for (const support of entry.claim.support) refs.push(support.path, support.sourceIdentity ?? '');
    }
  }
  refs.push(model.proposedWork.proposal.path, model.proposedWork.delta.path);
  if (model.proposedWork.currentAuthority.kind === 'baseline-spec') refs.push(model.proposedWork.currentAuthority.path);
  for (const block of parseNarrativeScript(html).blocks) for (const anchor of block.anchors) refs.push(anchor.targetId, anchor.locator);
  return refs.filter((ref) => ref !== '');
}

describe('Zero downstream citations of Polaris as authority (PWB-REQ-014)', () => {
  it('no machine reference on the model or its narrative anchors targets the Polaris surface', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC) } });
    const html = renderPolarisPage(model);
    const refs = machineReferences(model, html);
    expect(refs.length).toBeGreaterThan(100);
    expect(refs.filter((ref) => POLARIS_SURFACE.test(ref))).toEqual([]);
    // The anchors' own targets are project artifacts, evidence, decisions or
    // work — never a presentation surface.
    for (const block of parseNarrativeScript(html).blocks) for (const anchor of block.anchors) expect(anchor.targetClass).not.toMatch(/presentation|polaris|surface/i);
  });

  it('every OpenSpec warrant entry belongs to a known id family and none targets Polaris (POLARIS-DIR-* ids are owner decisions)', () => {
    const specs = walk(join(REPO_ROOT, 'openspec'), (path) => path.endsWith('.md'));
    const entries: { file: string; key: string; value: string }[] = [];
    for (const file of specs) {
      const text = readFileSync(file, 'utf8');
      for (const block of text.matchAll(/```yaml\s*\nwarrants:\n([\s\S]*?)```/g)) {
        for (const line of (block[1] as string).split('\n')) {
          const match = /^\s+([a-z_]+):\s*(.*)$/.exec(line);
          if (match === null) continue;
          const list = (match[2] as string).replace(/^\[|\]$/g, '').split(/,(?![^(]*\))/).map((entry) => entry.trim().replace(/^["']|["']$/g, '')).filter((entry) => entry !== '');
          for (const value of list) entries.push({ file: relative(REPO_ROOT, file), key: match[1] as string, value });
        }
      }
    }
    expect(specs.length).toBeGreaterThan(3);
    expect(entries.length).toBeGreaterThan(300);
    const unknownFamily = entries.filter((entry) => !WARRANT_FAMILIES.some((family) => family.test(entry.value)));
    expect(unknownFamily, 'warrant entries outside every hand-typed id family').toEqual([]);
    expect(entries.filter((entry) => POLARIS_SURFACE.test(entry.value))).toEqual([]);
    const polarisNamed = entries.filter((entry) => /polaris/i.test(entry.value));
    expect(polarisNamed.length).toBeGreaterThan(0);
    for (const entry of polarisNamed) {
      expect(entry.key).toBe('decisions');
      expect(entry.value).toMatch(/^POLARIS-DIR-\d{4}-\d{2}-\d{2}$/);
    }
  });

  it('no source/authority/provenance field in the governance, spec, code or docs trees names the Polaris surface', () => {
    const roots = ['.syzygy/governance', 'openspec', 'packages', 'apps', 'docs'];
    const files = roots.flatMap((root) => walk(join(REPO_ROOT, root), (path) => /\.(md|json|ya?ml|ts)$/.test(path)));
    expect(files.length).toBeGreaterThan(500);
    const hits: string[] = [];
    for (const file of files) {
      if (file.endsWith('polaris-authority-sweep.test.ts')) continue;
      const lines = readFileSync(file, 'utf8').split('\n');
      lines.forEach((line, index) => {
        if (/^\s*["']?(source|authority|warrants?|primary|evidence|provenance|cites?|anchor)["']?\s*[:=]/i.test(line) && POLARIS_SURFACE.test(line)) {
          hits.push(`${relative(REPO_ROOT, file)}:${index + 1}: ${line.trim().slice(0, 120)}`);
        }
      });
    }
    expect(hits).toEqual([]);
  });
});
