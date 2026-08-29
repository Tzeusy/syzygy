import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const MAIN_OUTPUT = join(REPO_ROOT, 'apps/three-surface-poc/dist/main.js');
const POISON = 'throw new Error("poisoned ignored POC output");\n';

function buildPoc(): void {
  execFileSync('npm', ['run', 'build:poc', '--silent'], {
    cwd: REPO_ROOT,
    stdio: ['ignore', 'ignore', 'pipe'],
  });
}

describe('POC build output integrity', () => {
  it(
    're-emits ignored JavaScript before the launcher executes it',
    () => {
      buildPoc();
      const original = readFileSync(MAIN_OUTPUT, 'utf8');
      writeFileSync(MAIN_OUTPUT, POISON, 'utf8');
      try {
        buildPoc();
        expect(readFileSync(MAIN_OUTPUT, 'utf8')).not.toContain(POISON.trim());
      } finally {
        writeFileSync(MAIN_OUTPUT, original, 'utf8');
      }
    },
    15_000,
  );
});
