import { describe, expect, it } from 'vitest';

import { DESIGN_TOKENS_CSS } from './design-tokens.js';

function tokenValue(css: string, name: string): string {
  const match = new RegExp(`${name}:\\s*([^;]+);`).exec(css);
  if (match?.[1] === undefined) {
    throw new Error(`token not declared: ${name}`);
  }
  return match[1].trim();
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
    const mutated = DESIGN_TOKENS_CSS.replace('--focus: #78e1d1;', '--focus: #f1b85b;');
    const amber = tokenValue(mutated, '--amber');
    const focus = tokenValue(mutated, '--focus');
    expect(focus).toBe(amber);
  });

  it('declares a single canonical --measure-reading token at 74ch, resolving the 66ch/74ch reading-column contradiction', () => {
    expect(tokenValue(DESIGN_TOKENS_CSS, '--measure-reading')).toBe('74ch');
  });
});
