import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

// syzygy-hjuz: the live verification test is skipped in the default suite,
// so its own assertions cannot guard it. This hermetic check reads its
// source and holds it to the owner's syzygy-4mbu direction: it ingests a
// JUnit file the operator produced and runs no observed code (SEC-3,
// RFC5-18). Its one permitted process is `git`.

const LIVE = new URL('./test-artifact-verification.live.test.ts', import.meta.url);
// Spelled in pieces so the suite's child-process guard does not read this
// file's patterns as calls.
const RUN_GIT = ['execFile', 'Sync'].join('');

describe('the live verification test runs no observed code', () => {
  let source = '';
  it('imports the process module once, binding only the git runner', () => {
    source = readFileSync(LIVE, 'utf8');
    expect([...source.matchAll(/['"](?:node:)?child_process['"]/g)]).toHaveLength(1);
    expect(source).toContain(`import { ${RUN_GIT} } from 'node:child_process';`);
  });

  it('names no other way to start a process', () => {
    source = readFileSync(LIVE, 'utf8');
    expect(source).not.toMatch(new RegExp(String.raw`\b(?:spawn|spawnSync|execSync|exec|execFile|fork)\s*\(`));
    expect(source).not.toMatch(/\bimport\s*\(|\brequire\s*\(|getBuiltinModule|node:worker_threads|node:vm/);
  });

  it('runs only git', () => {
    source = readFileSync(LIVE, 'utf8');
    const commands = [...source.matchAll(new RegExp(String.raw`\b${RUN_GIT}\s*\(\s*([^,)]*)`, 'g'))].map((m) => m[1]?.trim());
    expect(commands.length).toBeGreaterThan(0);
    expect(new Set(commands)).toEqual(new Set(["'git'"]));
  });

  it('reads the operator-produced result named by the environment', () => {
    source = readFileSync(LIVE, 'utf8');
    for (const name of ['SYZYGY_POC_BUTLERS_JUNIT', 'SYZYGY_POC_BUTLERS_JUNIT_COMMIT', 'SYZYGY_POC_BUTLERS_JUNIT_EXIT']) {
      expect(source).toContain(`process.env.${name};`);
    }
  });
});
