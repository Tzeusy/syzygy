import { describe, expect, it } from 'vitest';
import { unconsentedClass, unconsentedText } from './class-gate.js';

// R-PR403-SCREEN-DOCS-1 finding 1: the class gate on agent-bound artifacts. Expected values are literals from the policy's consentRule
// ("a consent record that does not list project-documentation does not permit its egress") and the choices `class-gate.ts` writes down.

describe('the content-class gate', () => {
  it.each<[string, 'code-content' | 'project-documentation' | undefined, readonly string[] | null, string | undefined]>([
    ['a listed class', 'project-documentation', ['code-content', 'project-documentation'], undefined],
    ['an unlisted class', 'project-documentation', ['code-content'], 'project-documentation'],
    ['code-content unlisted', 'code-content', ['project-documentation'], 'code-content'],
    ['an empty statement', 'code-content', [], 'code-content'],
    ['no statement, project-documentation', 'project-documentation', null, 'project-documentation'],
    ['no statement, code-content', 'code-content', null, undefined],
    ['no class, with a statement', undefined, ['code-content', 'project-documentation'], 'unclassified'],
    ['no class, no statement', undefined, null, 'unclassified'],
  ])('decides %s', (_name, contentClass, consented, withheld) => {
    expect(unconsentedClass(contentClass, consented)).toBe(withheld);
  });

  it('states the reason with the class and whether the run relies on a statement', () => {
    expect(unconsentedText('project-documentation', null)).toBe('withheld from every agent-bound artifact: the run relies on no per-project statement, so no consent record lists project-documentation');
    expect(unconsentedText('project-documentation', ['code-content'])).toBe('withheld from every agent-bound artifact: the per-project statement the run relies on does not list project-documentation');
  });
});
