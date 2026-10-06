import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { createRunDirectory, stateRootViolation } from './state-directory.js';

// REQ-polaris-generation-033: Syzygy writes only to its own state directory for the run, never into
// the clone and never to a location derived from the clone's path.
let base: string;
let clone: string;
beforeEach(() => {
  base = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-state-')));
  clone = path.join(base, 'clone');
  fs.mkdirSync(path.join(clone, '.git'), { recursive: true });
  fs.writeFileSync(path.join(clone, 'README.md'), '# clone\n');
});
afterEach(() => fs.rmSync(base, { recursive: true, force: true }));

/** Every path under `dir`, with its kind and mode: the harness's own record of what was written. */
const sweep = (dir: string): string[] => fs.readdirSync(dir, { recursive: true, withFileTypes: true })
  .map((entry) => {
    const full = path.join(entry.parentPath, entry.name);
    return `${entry.isDirectory() ? 'd' : 'f'} ${(fs.statSync(full).mode & 0o777).toString(8)} ${path.relative(dir, full)}`;
  }).sort();

describe('state root placement', () => {
  it('accepts a state root outside the clone', () => {
    expect(stateRootViolation(path.join(base, 'state'), clone)).toBe(null);
  });

  it('refuses a state root inside the clone', () => {
    expect(stateRootViolation(path.join(clone, '.dossier'), clone)).toMatch(/inside the clone/);
  });

  it('refuses the clone itself as the state root', () => {
    expect(stateRootViolation(clone, clone)).toMatch(/inside the clone/);
  });

  it('refuses a state root inside the clone\'s .git directory', () => {
    expect(stateRootViolation(path.join(clone, '.git', 'dossier'), clone)).toMatch(/inside the clone/);
  });

  it('refuses a state root that contains the clone', () => {
    expect(stateRootViolation(base, clone)).toMatch(/contains the clone/);
  });

  it('refuses a symbolic link that lands inside the clone, judged by where it resolves', () => {
    const link = path.join(base, 'innocent');
    fs.symlinkSync(path.join(clone, 'hidden'), link);
    expect(stateRootViolation(path.join(link, 'state'), clone)).toMatch(/inside the clone/);
  });

  it('refuses a relative state root', () => {
    expect(stateRootViolation('state', clone)).toMatch(/absolute/);
  });

  it('refuses a symbolic link cycle', () => {
    fs.symlinkSync(path.join(base, 'b'), path.join(base, 'a'));
    fs.symlinkSync(path.join(base, 'a'), path.join(base, 'b'));
    expect(stateRootViolation(path.join(base, 'a', 'state'), clone)).toMatch(/cycle/);
  });
});

describe('run directory creation', () => {
  it('writes only the run directory and its configuration, owner-only, and nothing in the clone', () => {
    const cloneBefore = sweep(clone);
    const stateRoot = path.join(base, 'state');
    const result = createRunDirectory(stateRoot, clone, '{}\n', { runId: () => 'run-0123456789abcdef0123456789abcdef' });
    expect(result).toEqual({ created: true, runId: 'run-0123456789abcdef0123456789abcdef', runDir: path.join(stateRoot, 'run-0123456789abcdef0123456789abcdef') });
    expect(sweep(stateRoot)).toEqual([
      'd 700 run-0123456789abcdef0123456789abcdef',
      'f 600 run-0123456789abcdef0123456789abcdef/run.json',
    ]);
    expect(sweep(clone)).toEqual(cloneBefore);
  });

  it('draws a random run id that does not depend on the clone path', () => {
    const stateRoot = path.join(base, 'state');
    const first = createRunDirectory(stateRoot, clone, '{}\n');
    const second = createRunDirectory(stateRoot, clone, '{}\n');
    expect(first.created && first.runId).toMatch(/^run-[0-9a-f]{32}$/);
    expect(second.created && second.runId).toMatch(/^run-[0-9a-f]{32}$/);
    expect(first.created && second.created && first.runId !== second.runId).toBe(true);
    expect(first.created && first.runId.includes('clone')).toBe(false);
  });

  it('never reuses an existing run directory', () => {
    const stateRoot = path.join(base, 'state');
    const id = (): string => 'run-ffffffffffffffffffffffffffffffff';
    expect(createRunDirectory(stateRoot, clone, '{"first":1}\n', { runId: id }).created).toBe(true);
    const again = createRunDirectory(stateRoot, clone, '{"second":2}\n', { runId: id });
    expect(again.created).toBe(false);
    expect(fs.readFileSync(path.join(stateRoot, id(), 'run.json'), 'utf8')).toBe('{"first":1}\n');
  });

  it('refuses a malformed run id', () => {
    const result = createRunDirectory(path.join(base, 'state'), clone, '{}\n', { runId: () => '../escape' });
    expect(result.created).toBe(false);
    expect(fs.existsSync(path.join(base, 'escape'))).toBe(false);
  });

  it('writes nothing when the state root is refused', () => {
    const before = sweep(base);
    const result = createRunDirectory(path.join(clone, 'state'), clone, '{}\n');
    expect(result.created).toBe(false);
    expect(sweep(base)).toEqual(before);
  });
});
