import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel } from '@syzygy/three-surface-poc-core';

import { POLARIS_COPY } from './polaris-copy.js';
import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
  REJECTING_AUTHORITY,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

// ---------------------------------------------------------------------------
// Hand-typed oracle (PWB-REQ-012). Nothing below is imported from the
// renderer or the copy table: the role set, the word limits, the prohibited
// vocabulary and the word counter are all restated here.

const ROLES = ['project-fact', 'epistemic-disclosure', 'action-label', 'scope-instruction'] as const;
const HEADING_WORD_LIMIT = 6;
const LEDE_WORD_LIMIT = 20;
const PROHIBITED = /\b(page|document|reading|section|movement|presentation)\b/i;
const VOID_TAGS = new Set(['br', 'hr', 'img', 'meta', 'link', 'input', 'wbr', 'source']);

interface Violation {
  readonly rule: 'unclassified' | 'unknown-role' | 'multiply-classified' | 'heading-too-long' | 'lede-too-long' | 'prohibited-term' | 'scope-instruction-count' | 'scope-instruction-role' | 'action-label-count' | 'disclosure-role';
  readonly text: string;
}

interface CopyString {
  readonly role: string | undefined;
  readonly text: string;
}

interface Frame {
  readonly tag: string;
  readonly role: string | undefined;
  readonly kind: 'heading' | 'lede' | 'notice' | undefined;
  readonly interactive: boolean;
  text: string;
  actionLabels: number;
}

function decode(text: string): string {
  return text
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, '&');
}

function attr(attrs: string, name: string): string[] {
  return [...attrs.matchAll(new RegExp(`\\s${name}="([^"]*)"`, 'g'))].map((match) => match[1] as string);
}

/** Words are whitespace-separated tokens carrying at least one letter or digit. */
function countWords(text: string): number {
  return text.split(/\s+/).filter((token) => /[\p{L}\p{N}]/u.test(token)).length;
}

/** A plain stack extractor over the served HTML: every text node outside the
 * head, style and script elements, with the role of its innermost declaring
 * ancestor, plus the per-element checks the requirement names. */
function sweep(html: string): { strings: CopyString[]; violations: Violation[] } {
  const body = html
    .replace(/<head>[\s\S]*?<\/head>/g, '')
    .replace(/<style[^>]*>[\s\S]*?<\/style>/g, '')
    .replace(/<script[^>]*>[\s\S]*?<\/script>/g, '');
  const strings: CopyString[] = [];
  const violations: Violation[] = [];
  const stack: Frame[] = [];
  let pocBound = 0;
  const tokens = body.matchAll(/<!--[\s\S]*?-->|<![^>]*>|<\/([A-Za-z][\w-]*)\s*>|<([A-Za-z][\w-]*)([^>]*)>|([^<]+)/g);
  for (const token of tokens) {
    const [whole, closing, opening, rawAttrs, text] = token;
    if (whole.startsWith('<!')) continue;
    if (opening !== undefined) {
      const tag = opening.toLowerCase();
      const attrs = rawAttrs ?? '';
      const roleValues = attr(attrs, 'data-copy-role');
      let role = stack.length === 0 ? undefined : (stack[stack.length - 1] as Frame).role;
      if (roleValues.length > 1 || roleValues.some((value) => /\s/.test(value))) {
        violations.push({ rule: 'multiply-classified', text: roleValues.join(' ') });
      }
      if (roleValues.length >= 1) {
        role = roleValues[0];
        if (!(ROLES as readonly string[]).includes(role as string)) {
          violations.push({ rule: 'unknown-role', text: role as string });
        }
      }
      if (attr(attrs, 'data-scope').includes('poc-bound')) {
        pocBound += 1;
        if (roleValues[0] !== 'scope-instruction') violations.push({ rule: 'scope-instruction-role', text: attrs.trim() });
      }
      const classes = attr(attrs, 'class').join(' ');
      if (/\b(claim-tuple|unknown-disclosure)\b/.test(classes) && roleValues[0] !== 'epistemic-disclosure') {
        violations.push({ rule: 'disclosure-role', text: attrs.trim() });
      }
      const kind = /^h[1-6]$/.test(tag) ? 'heading' : /\blede\b|-lede\b/.test(classes) ? 'lede' : /\bnotice\b/.test(classes) ? 'notice' : undefined;
      const frame: Frame = { tag, role, kind, interactive: tag === 'a' || tag === 'button', text: '', actionLabels: 0 };
      if (roleValues[0] === 'action-label') {
        for (const ancestor of stack) if (ancestor.interactive) ancestor.actionLabels += 1;
        if (frame.interactive) frame.actionLabels += 1;
      }
      if (!VOID_TAGS.has(tag) && !attrs.trimEnd().endsWith('/')) stack.push(frame);
      continue;
    }
    if (closing !== undefined) {
      const frame = stack.pop();
      if (frame === undefined || frame.tag !== closing.toLowerCase()) {
        throw new Error(`malformed markup: closing ${closing} against ${frame?.tag ?? 'nothing'}`);
      }
      const content = frame.text.replace(/\s+/g, ' ').trim();
      if (frame.kind === 'heading' && countWords(content) > HEADING_WORD_LIMIT) violations.push({ rule: 'heading-too-long', text: content });
      if (frame.kind === 'lede' && countWords(content) > LEDE_WORD_LIMIT) violations.push({ rule: 'lede-too-long', text: content });
      if (frame.kind !== undefined && PROHIBITED.test(content)) violations.push({ rule: 'prohibited-term', text: content });
      if (frame.interactive && frame.actionLabels > 1) violations.push({ rule: 'action-label-count', text: content });
      const parent = stack[stack.length - 1];
      if (parent !== undefined) parent.text += ` ${frame.text}`;
      continue;
    }
    if (text !== undefined) {
      const decoded = decode(text);
      const parent = stack[stack.length - 1];
      if (parent !== undefined) parent.text += decoded;
      const trimmed = decoded.replace(/\s+/g, ' ').trim();
      if (trimmed === '') continue;
      const role = parent?.role;
      strings.push({ role, text: trimmed });
      if (role === undefined) violations.push({ rule: 'unclassified', text: trimmed });
    }
  }
  if (stack.length !== 0) throw new Error(`malformed markup: ${stack.length} unclosed element(s)`);
  if (pocBound > 1) violations.push({ rule: 'scope-instruction-count', text: String(pocBound) });
  return { strings, violations };
}

// ---------------------------------------------------------------------------

type Variant = 'unevaluated' | 'rejected' | 'observed' | 'observed-with-secret' | 'observation-failed';
const VARIANTS: readonly Variant[] = ['unevaluated', 'rejected', 'observed', 'observed-with-secret', 'observation-failed'];

function modelFor(variant: Variant): PocModel {
  switch (variant) {
    case 'unevaluated':
      return buildFixtureModel(cleanups);
    case 'rejected':
      return buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'observed':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'observed-with-secret':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET) } });
    case 'observation-failed': {
      const inner = projectShapeFixtureGit();
      const failing = (args: readonly string[]): Uint8Array => {
        if (args[0] === 'ls-tree') throw new Error('fixture: tree listing refused');
        return inner(args);
      };
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: failing } });
    }
  }
}

describe('Polaris copy roles (PWB-REQ-012)', () => {
  it('renders the five shape states with every string classified once, within the word bounds, free of the prohibited vocabulary, with one POC-bound scope instruction and at most one action label per control', () => {
    const shapeKinds = new Set<string>();
    for (const variant of VARIANTS) {
      const model = modelFor(variant);
      shapeKinds.add(model.projectShape.kind);
      const html = renderPolarisPage(model);
      const { strings, violations } = sweep(html);
      expect(violations, `${variant}: ${JSON.stringify(violations.slice(0, 5))}`).toEqual([]);
      expect(strings.length).toBeGreaterThan(40);
      // Exactly one POC-bound scope instruction, and it is the capability one.
      const pocBound = [...html.matchAll(/<[^>]*data-scope="poc-bound"[^>]*>/g)];
      expect(pocBound.length).toBe(1);
      expect(pocBound[0]?.[0]).toContain('data-polaris-capability-scope');
      expect(pocBound[0]?.[0]).toContain('data-copy-role="scope-instruction"');
      // The four roles are all in use on every variant.
      const rolesUsed = new Set(strings.map((entry) => entry.role));
      for (const role of ROLES) expect(rolesUsed.has(role), `${variant} lacks ${role}`).toBe(true);
    }
    // The fixtures reach all four shape kinds, so the sweep covers every arm.
    expect([...shapeKinds].sort()).toEqual(['not-admitted', 'not-evaluated', 'observation-failed', 'observed']);
  });

  it('keeps no group lede and no connective prose between groups: each group header is one heading', () => {
    const html = renderPolarisPage(modelFor('observed'));
    const headers = [...html.matchAll(/<header class="group"[^>]*>([\s\S]*?)<\/header>/g)].map((match) => (match[1] as string).trim());
    expect(headers.length).toBe(7);
    for (const header of headers) {
      expect(header).toMatch(/^<h2 id="polaris-group-[a-z0-9-]+" data-copy-role="project-fact" data-claim-role="non-normative-framing" data-presentation-artifact data-non-citable>[^<]+<\/h2>$/);
    }
    expect(html).not.toContain('group-lede');
  });

  it('flags meta-narration: the counterexample fixture fails every rule the sweep enforces', () => {
    const counterexample = `<main>
      <header class="group"><h2>This section of the page walks the reader through the presentation</h2></header>
      <p>An unclassified sentence about what the reader is about to read.</p>
      <p data-copy-role="narrative">A role outside the closed set.</p>
      <p data-copy-role="project-fact epistemic-disclosure">Two roles on one string.</p>
      <p class="lede" data-copy-role="project-fact">One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one.</p>
      <p class="notice" data-copy-role="epistemic-disclosure">A notice about this document.</p>
      <p data-scope="poc-bound" data-copy-role="scope-instruction">First bound.</p>
      <p data-scope="poc-bound" data-copy-role="project-fact">Second bound with the wrong role.</p>
      <a href="#x"><span data-copy-role="action-label">Open</span> <span data-copy-role="action-label">Close</span></a>
      <span class="claim-tuple" data-copy-role="project-fact">Unknown · unstated · fresh</span>
    </main>`;
    const { violations } = sweep(counterexample);
    const rules = new Set(violations.map((violation) => violation.rule));
    expect([...rules].sort()).toEqual([
      'action-label-count',
      'disclosure-role',
      'heading-too-long',
      'lede-too-long',
      'multiply-classified',
      'prohibited-term',
      'scope-instruction-count',
      'scope-instruction-role',
      'unclassified',
      'unknown-role',
    ]);
    expect(violations.filter((violation) => violation.rule === 'prohibited-term').length).toBe(2);
    // A clean fragment produces nothing.
    expect(sweep('<main><h2 data-copy-role="project-fact">What Butlers is</h2><p data-copy-role="project-fact">A fact.</p></main>').violations).toEqual([]);
  });

  it('keeps the copy table closed and rendered: unique ids, roles and kinds from the closed sets, and every row present with its role in some rendered state', () => {
    const ids = POLARIS_COPY.map((row) => row.id);
    expect(new Set(ids).size).toBe(ids.length);
    const kinds = ['heading', 'lede', 'notice', 'sentence', 'label'];
    for (const row of POLARIS_COPY) {
      expect(ROLES).toContain(row.role);
      expect(kinds).toContain(row.kind);
      if (row.kind === 'heading') expect(countWords(row.text), row.id).toBeLessThanOrEqual(HEADING_WORD_LIMIT);
      if (row.kind === 'lede') expect(countWords(row.text), row.id).toBeLessThanOrEqual(LEDE_WORD_LIMIT);
      if (row.kind !== 'sentence' && row.kind !== 'label') expect(row.text, row.id).not.toMatch(PROHIBITED);
    }
    const rendered: CopyString[] = [];
    for (const variant of VARIANTS) rendered.push(...sweep(renderPolarisPage(modelFor(variant))).strings);
    // Rows the five fixtures cannot reach, restated by hand so a newly
    // reachable row must be removed from here rather than silently pass.
    const UNREACHED_IN_FIXTURES = new Set<string>([
      'label.declarations-kept',
      'label.deferred',
      'label.limit-breaches',
      'label.no-route',
      'label.secondary-reasons',
      'label.exclusive-with',
      'sentence.no-competitor',
      'sentence.no-intent-declared',
      'sentence.separate-futures',
      'sentence.missing-statement',
      'sentence.no-body-read',
    ]);
    for (const row of POLARIS_COPY) {
      const present = rendered.some((entry) => entry.role === row.role && (entry.text === row.text || entry.text.startsWith(row.text) || entry.text.includes(row.text)));
      if (UNREACHED_IN_FIXTURES.has(row.id)) {
        expect(present, `${row.id} is now reachable; drop it from UNREACHED_IN_FIXTURES`).toBe(false);
      } else {
        expect(present, `${row.id} ("${row.text}") never rendered with role ${row.role}`).toBe(true);
      }
    }
  });
});
