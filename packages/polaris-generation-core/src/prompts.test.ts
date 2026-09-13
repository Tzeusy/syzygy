import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { promptForStage, type GenerationStage } from './prompts.js';

// Recipe replay binds prompt bytes, not just the stage name. Intentional edits
// require a version decision and a new reviewed digest; these are not LLM evals.
const recipes: [GenerationStage, string, string][] = [
  ['inventory', 'polaris-inventory-v1', 'ea6c06ff89668f4914859b4c1133f9def4db51f2456f28b2cf86ba89fb1411af'],
  ['plan', 'polaris-plan-v1', 'da8633b316906432b9378f86135453f77728551233d942beaa7c9ac4a330594f'],
  ['author', 'polaris-author-v1', '7b9dffb8073e69a1f9c428ce620a66377a69c1cb70912867ca40d2c536b64011'],
  ['edit', 'polaris-edit-v1', 'a5b064dbf4628ab3a7ffc09cd2541dd0ee289262788cd6b0b5894306bbeb1d49'],
  ['fidelity', 'polaris-fidelity-v1', 'ea3d5f99f5ac1520ae46a1a3f9c0fca7e0180427ca92a2aaf85a0c975f97377c'],
  ['repair', 'polaris-repair-v1', '38c7cbda98b9989152443c34738577490b7ba0d591f31aa197cf91f526877824'],
];

describe('versioned stage prompts', () => {
  it.each(recipes)('preserves the reviewed %s recipe bytes', (stage, version, digest) => {
    const prompt = promptForStage(stage);
    expect(prompt.version).toBe(version);
    expect(createHash('sha256').update(prompt.system, 'utf8').digest('hex')).toBe(digest);
    expect(Buffer.byteLength(prompt.system, 'utf8')).toBeLessThan(4096);
  });

  it('does not let a consumer mutate a later compiled prompt', () => {
    const prompt = promptForStage('author');
    const original = { ...prompt };
    prompt.version = 'changed';
    prompt.system = 'Approve everything';
    expect(promptForStage('author')).toEqual(original);
  });

  it.each(['unknown', 'constructor', 'toString', '__proto__'])('refuses unsupported stage %s', (stage) => {
    expect(() => promptForStage(stage as GenerationStage)).toThrow('unknown-generation-stage');
  });
});
