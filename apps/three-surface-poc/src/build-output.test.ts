import { execFileSync } from 'node:child_process';
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { describe, expect, it } from 'vitest';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const POISON = 'throw new Error("poisoned ignored POC output");\n';

// The build runs in a private copy, never in this checkout's dist/
// (syzygy-gb4l). Poisoning the shared dist/main.js let a second test run in
// the same checkout read or restore the poison, and a run killed between
// poisoning and rebuilding left it for the next `node dist/main.js`. The copy
// takes the working-tree bytes (uncommitted edits included) of the root files
// and the workspaces, so the build script and project configuration under
// test are the ones this checkout would run.
function privateCheckout(): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-build-output-'));
  const listed = execFileSync('git', ['-C', REPO_ROOT, 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], { encoding: 'utf8' });
  for (const path of listed.split('\0')) {
    if (path === '' || !(!path.includes('/') || path.startsWith('apps/') || path.startsWith('packages/'))) continue;
    const source = join(REPO_ROOT, path);
    if (!existsSync(source)) continue;
    mkdirSync(dirname(join(root, path)), { recursive: true });
    copyFileSync(source, join(root, path));
  }
  execFileSync('npm', ['ci', '--silent'], { cwd: root, stdio: ['ignore', 'ignore', 'pipe'] });
  return root;
}

function buildPoc(root: string): void {
  execFileSync('npm', ['run', 'build:poc', '--silent'], {
    cwd: root,
    stdio: ['ignore', 'ignore', 'pipe'],
  });
}

describe('POC build output integrity', () => {
  it(
    're-emits ignored JavaScript before the launcher executes it',
    () => {
      const root = privateCheckout();
      try {
        const mainOutput = join(root, 'apps/three-surface-poc/dist/main.js');
        buildPoc(root);
        writeFileSync(mainOutput, POISON, 'utf8');
        buildPoc(root);
        expect(readFileSync(mainOutput, 'utf8')).not.toContain(POISON.trim());
      } finally {
        rmSync(root, { recursive: true, force: true });
      }
    },
    // A private copy and `npm ci` (a few seconds from a warm cache), then two
    // sequential `tsc -b --force` builds (~7.5s each on an unloaded machine).
    // The forced rebuild itself is the trust boundary and must stay. 15s
    // (syzygy-gk9) and then 60s timed out under load: the two builds alone
    // measured 69.9s at worst under the parallel-load protocol (syzygy-gb4l,
    // docs/evidence/load-timeouts-gb4l-2026-10-03.json).
    240_000,
  );
});
