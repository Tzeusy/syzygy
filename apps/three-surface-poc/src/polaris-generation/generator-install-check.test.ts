import { execFile } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { promisify } from 'node:util';
import { afterEach, describe, expect, it } from 'vitest';

// The install preflight of `poc:dossier` and `poc:generator-demo` (syzygy-bpyt.6.13, review
// R-GP-IMPL-SUPPORT-LEAF-1 N5): a checkout that pulled a new workspace package without running
// `npm ci` must be refused here, with the instruction, not later at the first import. Each case
// runs the script in a fixture directory holding some of the entries a real install has.
const run = promisify(execFile);
const SCRIPT = fileURLToPath(new URL('../../../../scripts/check_generator_install.mjs', import.meta.url));
const REFUSAL = 'Generator dependencies are missing. Run npm ci from the repository root, then retry.\n';
const ENTRIES = {
  tsc: ['node_modules', '.bin', 'tsc'],
  'polaris-generation-core': ['node_modules', '@syzygy', 'polaris-generation-core'],
  support: ['node_modules', '@syzygy', 'support'],
} as const;
type Entry = keyof typeof ENTRIES;

const cleanups: string[] = [];
afterEach(() => { for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true }); });

function checkoutWith(entries: readonly Entry[]): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-install-check-'));
  cleanups.push(root);
  for (const entry of entries) {
    const path = join(root, ...ENTRIES[entry]);
    mkdirSync(entry === 'tsc' ? dirname(path) : path, { recursive: true });
    if (entry === 'tsc') writeFileSync(path, '');
  }
  return root;
}

async function check(directory: string): Promise<{ readonly exit: number; readonly stderr: string }> {
  try {
    const { stderr } = await run(process.execPath, [SCRIPT], { cwd: directory });
    return { exit: 0, stderr };
  } catch (error) {
    const failure = error as { code?: number; stderr?: string };
    return { exit: failure.code ?? -1, stderr: failure.stderr ?? '' };
  }
}

describe('the generator install check', () => {
  it('passes a checkout holding tsc, the generation core and the support package', async () => {
    expect(await check(checkoutWith(['tsc', 'polaris-generation-core', 'support']))).toEqual({ exit: 0, stderr: '' });
  });

  it.each([
    ['support', ['tsc', 'polaris-generation-core']],
    ['polaris-generation-core', ['tsc', 'support']],
    ['tsc', ['polaris-generation-core', 'support']],
    ['every entry', []],
  ] as const)('refuses a checkout without %s, with the instruction to run npm ci', async (_missing, present) => {
    expect(await check(checkoutWith(present))).toEqual({ exit: 1, stderr: REFUSAL });
  });

  it('passes this checkout, so the fixture entries are the ones a real install has', async () => {
    expect(await check(fileURLToPath(new URL('../../../../', import.meta.url)))).toEqual({ exit: 0, stderr: '' });
  });
});
