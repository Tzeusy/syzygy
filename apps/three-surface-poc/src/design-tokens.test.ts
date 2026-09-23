import { describe, expect, it } from 'vitest';

import { DESIGN_TOKENS_CSS, EPISTEMIC_ENCODING } from './design-tokens.js';

function tokenValue(css: string, name: string): string {
  const match = new RegExp(`${name}:\\s*([^;]+);`).exec(css);
  if (match?.[1] === undefined) {
    throw new Error(`token not declared: ${name}`);
  }
  return match[1].trim();
}

function rgb(hex: string): readonly [number, number, number] {
  const parts = /^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(hex);
  if (parts === null) throw new Error(`not an RGB color: ${hex}`);
  return [1, 2, 3].map((i) => Number.parseInt(parts[i] as string, 16) / 255) as unknown as readonly [number, number, number];
}

function linear(channel: number): number {
  return channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4;
}

function luminance(hex: string): number {
  const [r, g, b] = rgb(hex).map(linear);
  return 0.2126 * (r as number) + 0.7152 * (g as number) + 0.0722 * (b as number);
}

function contrast(a: string, b: string): number {
  const values = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return ((values[0] as number) + 0.05) / ((values[1] as number) + 0.05);
}

// sRGB D65 -> CIE L*a*b*, with the CIE 1976 Euclidean distance.
function lab(hex: string): readonly [number, number, number] {
  const [r, g, b] = rgb(hex).map(linear);
  const x = (0.4124564 * (r as number) + 0.3575761 * (g as number) + 0.1804375 * (b as number)) / 0.95047;
  const y = (0.2126729 * (r as number) + 0.7151522 * (g as number) + 0.0721750 * (b as number));
  const z = (0.0193339 * (r as number) + 0.1191920 * (g as number) + 0.9503041 * (b as number)) / 1.08883;
  const f = (v: number): number => v > 0.008856 ? Math.cbrt(v) : 7.787 * v + 16 / 116;
  return [116 * f(y) - 16, 500 * (f(x) - f(y)), 200 * (f(y) - f(z))];
}

function deltaE76(a: string, b: string): number {
  const first = lab(a), second = lab(b);
  return Math.hypot(...first.map((value, i) => value - (second[i] as number)));
}

/**
 * Finds the `.{className} { ... }` rule body in the token stylesheet and
 * resolves its `color: var(--x)` reference to that token's own value.
 * Derived from the live CSS and the live EPISTEMIC_ENCODING table — never a
 * hard-coded list of "which colours are semantic" — so a future encoding
 * entry, or a future colour swap inside an existing one, is caught without
 * editing this file (rule 9: an absence/distinctness claim needs a sweep
 * with a denominator, not an assumption).
 */
function epistemicClassColor(css: string, className: string): string {
  const escaped = className.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
  const ruleMatch = new RegExp(`\\.epistemic\\.${escaped}[^{}]*\\{([^}]*)\\}`).exec(css);
  if (ruleMatch?.[1] === undefined) {
    throw new Error(`no CSS rule found for .${className}`);
  }
  const colorMatch = /color:\s*var\((--[a-z-]+)\)/.exec(ruleMatch[1]);
  if (colorMatch?.[1] === undefined) {
    throw new Error(`.${className} declares no color: var(--x)`);
  }
  return tokenValue(css, colorMatch[1]);
}

/** Same derivation for the global link colour (`a { color: var(--x); ... }`),
 * matched only where `a` is itself a full selector (not part of a compound
 * selector such as `a[aria-current="page"]`, which this regex's
 * `a\s*\{` cannot match). */
function linkColor(css: string): string {
  const ruleMatch = /(?:^|\n)\s*a\s*\{([^}]*)\}/.exec(css);
  if (ruleMatch?.[1] === undefined) {
    throw new Error('no CSS rule found for the bare `a` selector');
  }
  const colorMatch = /color:\s*var\((--[a-z-]+)\)/.exec(ruleMatch[1]);
  if (colorMatch?.[1] === undefined) {
    throw new Error('`a` rule declares no color: var(--x)');
  }
  return tokenValue(css, colorMatch[1]);
}

describe('design tokens (N4 S11-F2, S11-F3)', () => {
  it('declares --focus as its own token, distinct in value from the semantic --amber', () => {
    const amber = tokenValue(DESIGN_TOKENS_CSS, '--amber');
    const focus = tokenValue(DESIGN_TOKENS_CSS, '--focus');
    expect(focus).not.toBe(amber);
  });

  it('uses the --focus token (not --amber) for the global focus-visible outline', () => {
    const outlineRule = /:focus-visible\s*\{[^}]*outline:\s*3px solid var\((--[a-z-]+)\)/.exec(
      DESIGN_TOKENS_CSS,
    );
    expect(outlineRule?.[1]).toBe('--focus');
  });

  it('still uses --amber (not --focus) for the semantic .notice accent', () => {
    const noticeRule = /\.notice\s*\{[^}]*border-left:\s*3px solid var\((--[a-z-]+)\)/.exec(
      DESIGN_TOKENS_CSS,
    );
    expect(noticeRule?.[1]).toBe('--amber');
  });

  it('mutation check: aliasing --focus back to --amber would fail the distinctness test', () => {
    const mutated = DESIGN_TOKENS_CSS.replace('--focus: #b98eff;', '--focus: #f1b85b;');
    const amber = tokenValue(mutated, '--amber');
    const focus = tokenValue(mutated, '--focus');
    expect(focus).toBe(amber);
  });

  it(
    'declares --focus distinct, by parsing the live CSS, from every colour any EPISTEMIC_ENCODING ' +
      'class resolves to and from the link colour (repair of S11-F2’s recurrence: the first cut ' +
      'aliased --focus to the --cyan literal, colliding with .epistemic-observed)',
    () => {
      const focus = tokenValue(DESIGN_TOKENS_CSS, '--focus');

      const semanticColors = new Map<string, string>();
      for (const entry of EPISTEMIC_ENCODING) {
        semanticColors.set(`.${entry.className}`, epistemicClassColor(DESIGN_TOKENS_CSS, entry.className));
      }
      semanticColors.set('a (link)', linkColor(DESIGN_TOKENS_CSS));
      semanticColors.set('.notice (--amber)', tokenValue(DESIGN_TOKENS_CSS, '--amber'));

      // Denominator check (rule 9): EPISTEMIC_ENCODING must actually have
      // entries, or the sweep below would vacuously pass with nothing swept.
      expect(EPISTEMIC_ENCODING.length).toBeGreaterThan(0);
      expect(semanticColors.size).toBe(EPISTEMIC_ENCODING.length + 2);

      for (const [source, color] of semanticColors) {
        expect(focus, `--focus (${focus}) must differ from ${source} (${color})`).not.toBe(color);
      }
    },
  );

  it('mutation check: the CSS-derived sweep catches --focus colliding with .epistemic-observed', () => {
    const cyan = tokenValue(DESIGN_TOKENS_CSS, '--cyan');
    const mutated = DESIGN_TOKENS_CSS.replace('--focus: #b98eff;', `--focus: ${cyan};`);
    const focus = tokenValue(mutated, '--focus');
    const observed = epistemicClassColor(mutated, 'epistemic-observed');
    expect(focus).toBe(observed);
  });

  it('hard-coded literal: --focus is #b98eff (distinct from --cyan #78e1d1, --unknown #f3c56f, --amber #f1b85b)', () => {
    expect(tokenValue(DESIGN_TOKENS_CSS, '--focus')).toBe('#b98eff');
  });

  it('declares a single canonical --measure-reading token at 74ch (the value slice 2 wires into polaris.ts to converge its duplicate 66ch/74ch .reading-prose declarations — this token declares the value, it does not by itself resolve the contradiction)', () => {
    expect(tokenValue(DESIGN_TOKENS_CSS, '--measure-reading')).toBe('74ch');
  });

  it('keeps proposal treatment distinct from epistemic Unknown and notice amber, with readable foreground contrast', () => {
    const proposed = tokenValue(DESIGN_TOKENS_CSS, '--proposed');
    expect(deltaE76(proposed, tokenValue(DESIGN_TOKENS_CSS, '--unknown'))).toBeGreaterThanOrEqual(26.7);
    expect(deltaE76(proposed, tokenValue(DESIGN_TOKENS_CSS, '--amber'))).toBeGreaterThanOrEqual(26.7);
    for (const ground of ['--void', '--panel'] as const) {
      expect(contrast(proposed, tokenValue(DESIGN_TOKENS_CSS, ground))).toBeGreaterThanOrEqual(4.5);
    }
    const collision = DESIGN_TOKENS_CSS.replace('--proposed: #aa90ee;', '--proposed: #f3c56f;');
    expect(deltaE76(tokenValue(collision, '--proposed'), tokenValue(collision, '--unknown'))).toBeLessThan(26.7);
  });
});
