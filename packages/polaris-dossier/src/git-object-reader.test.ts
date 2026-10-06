import { execFileSync } from 'node:child_process';
import { chmodSync, cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { deflateSync } from 'node:zlib';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { GitObjectReadRefusal, hashAlgorithmOf, openPinnedObjectReader, type PinnedObjectReader } from './git-object-reader.js';

// Fixture clones are built with the git CLI (the reader under test spawns nothing). Dates, names and content are fixed, so every
// object identifier below is a literal: these are the identifiers git computed for these bytes, written here by hand.
const C1 = '1446b80da43514833ddd07b6acf511f8e5d5587a';   // SHA-1, commit "one"
const C2 = 'c63b8bbd0774e8299ddf9b41ded0d067041167de';   // SHA-1, commit "two" (HEAD)
const TREE2 = 'ed0f1e7b2db8b64ce6a7fee8006117a861c0c2c4';
const TREE1 = '94e4861c38016e1a532f35f9f969ba1c887cc7db';
const QUOTED_ID = '346e451ab772ed0d99ba93b54f1d192e450644de';
const BIG1_ID = '37d6ac34282cd848af27777eeeb4f94c0d987bc7';
const S2 = '789f9d6ea0e958b4da950a97a49800ea5286050aa3158310f354e6fd766f1cd2';   // SHA-256, commit "two"
const QUOTED = 'The committed sentence, “quoted”.\n';
const BIG = (v: number): string => Array.from({ length: 400 }, (_, i) => `line ${i} of the large file${i === 200 ? `, version ${v}` : ''}\n`).join('');

let T = '';
const env = {
  ...process.env, GIT_CONFIG_NOSYSTEM: '1', GIT_CONFIG_GLOBAL: '/dev/null', HOME: '/nonexistent',
  GIT_AUTHOR_NAME: 'Fixture', GIT_AUTHOR_EMAIL: 'fixture@example.invalid', GIT_COMMITTER_NAME: 'Fixture', GIT_COMMITTER_EMAIL: 'fixture@example.invalid',
};
const git = (cwd: string, args: readonly string[], extra: Record<string, string> = {}): string =>
  execFileSync('git', args, { cwd, env: { ...env, ...extra }, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
const at = (date: string): Record<string, string> => ({ GIT_AUTHOR_DATE: date, GIT_COMMITTER_DATE: date });

/** Two commits: the first with every file, the second changing one line of the large file. */
function build(dir: string, format: 'sha1' | 'sha256'): void {
  mkdirSync(dir, { recursive: true });
  git(dir, ['init', '-q', '-b', 'main', `--object-format=${format}`]);
  mkdirSync(path.join(dir, 'src'));
  writeFileSync(path.join(dir, 'README.md'), 'hello\n');
  writeFileSync(path.join(dir, 'src/quoted.txt'), QUOTED);
  writeFileSync(path.join(dir, 'src/run.sh'), '#!/bin/sh\necho hi\n');
  chmodSync(path.join(dir, 'src/run.sh'), 0o755);
  symlinkSync('src/quoted.txt', path.join(dir, 'link'));
  writeFileSync(path.join(dir, 'big.txt'), BIG(1));
  git(dir, ['add', '-A']);
  git(dir, ['commit', '-q', '-m', 'one'], at('2026-10-06T00:00:00Z'));
  writeFileSync(path.join(dir, 'big.txt'), BIG(2));
  git(dir, ['commit', '-q', '-am', 'two'], at('2026-10-06T00:01:00Z'));
}
const copy = (from: string, name: string): string => { const to = path.join(T, name); cpSync(from, to, { recursive: true, verbatimSymlinks: true }); return to; };
const gitDir = (repo: string): string => path.join(repo, '.git');
const looseFile = (repo: string, id: string): string => path.join(repo, '.git/objects', id.slice(0, 2), id.slice(2));
const overwrite = (file: string, bytes: Buffer): void => { chmodSync(file, 0o644); writeFileSync(file, bytes); };
const reader = (repo: string, revision: string): PinnedObjectReader => openPinnedObjectReader({ gitDir: gitDir(repo), revision });
const text = (bytes: Uint8Array): string => Buffer.from(bytes).toString('utf8');
async function refusal(p: Promise<unknown>): Promise<{ reason: string; objectId: string | null; path: string | null; message: string }> {
  try { await p; } catch (e) { if (e instanceof GitObjectReadRefusal) return e.toJSON(); throw e; }
  throw new Error('expected a refusal, got a result');
}

let L = '', OFS = '', REF = '', S = '', SP = '';
/** Offsets of pack entries by object id, and how many are deltas, from `git verify-pack -v` (fixture inspection only). */
const packEntries = (repo: string): { offsets: Map<string, number>; deltas: number } => {
  const dir = path.join(repo, '.git/objects/pack'), idx = execFileSync('ls', [dir], { encoding: 'utf8' }).split('\n').find(n => n.endsWith('.idx'))!;
  const out = git(repo, ['verify-pack', '-v', path.join(dir, idx)]), offsets = new Map<string, number>();
  let deltas = 0;
  for (const line of out.split('\n')) {
    const m = /^([0-9a-f]{40,64}) (\w+) +(\d+) (\d+) (\d+)( \d+ [0-9a-f]+)?$/.exec(line);
    if (m === null) continue;
    offsets.set(m[1]!, Number(m[5]));
    if (m[6] !== undefined) deltas += 1;
  }
  return { offsets, deltas };
};
const packFile = (repo: string): string => {
  const dir = path.join(repo, '.git/objects/pack');
  return path.join(dir, execFileSync('ls', [dir], { encoding: 'utf8' }).split('\n').find(n => n.endsWith('.pack'))!);
};
let ofsEntries: { offsets: Map<string, number>; deltas: number }, refEntries: { offsets: Map<string, number>; deltas: number };
beforeAll(() => {
  T = mkdtempSync(path.join(tmpdir(), 'git-object-reader-'));
  L = path.join(T, 'loose'); build(L, 'sha1');
  writeFileSync(path.join(L, 'src/quoted.txt'), 'An uncommitted working-tree edit.\n');   // the working tree differs from HEAD
  S = path.join(T, 'sha256'); build(S, 'sha256');
  OFS = copy(L, 'ofs'); git(OFS, ['repack', '-q', '-a', '-d', '-f', '--window=10', '--depth=10']); git(OFS, ['prune-packed']);
  REF = copy(L, 'ref'); git(REF, ['-c', 'repack.useDeltaBaseOffset=false', 'repack', '-q', '-a', '-d', '-f', '--window=10', '--depth=10']); git(REF, ['prune-packed']);
  SP = copy(S, 'sha256-packed'); git(SP, ['repack', '-q', '-a', '-d', '-f']); git(SP, ['prune-packed']);
  ofsEntries = packEntries(OFS); refEntries = packEntries(REF);
});
afterAll(() => { if (T !== '') rmSync(T, { recursive: true, force: true }); });

const ALL_PATHS = [
  { path: 'README.md', mode: '100644', id: 'ce013625030ba8dba906f756967f9e9ca394464a' },
  { path: 'big.txt', mode: '100644', id: '86eba436a1086aacef37e390ddc455d5f7c36d76' },
  { path: 'link', mode: '120000', id: 'a9b639a18cee797978c525478961c3ce5ffcddb4' },
  { path: 'src/quoted.txt', mode: '100644', id: QUOTED_ID },
  { path: 'src/run.sh', mode: '100755', id: '4163036efa65bd4a469e752267498f01ea36a55c' },
];

describe('hashAlgorithmOf: the algorithm is the one the consented identifier is written in', () => {
  it('40 hex digits are SHA-1 and 64 are SHA-256; anything else refuses', () => {
    expect(hashAlgorithmOf(C2)).toBe('sha1');
    expect(hashAlgorithmOf(S2)).toBe('sha256');
    for (const bad of ['', C2.toUpperCase(), C2.slice(1), `${C2}0`, S2.slice(1), `${S2}0`, `g${C2.slice(1)}`, ` ${C2}`, 'HEAD', 'main', 'refs/heads/main']) {
      expect(() => hashAlgorithmOf(bad), JSON.stringify(bad)).toThrow(GitObjectReadRefusal);
      expect(() => openPinnedObjectReader({ gitDir: '/nonexistent', revision: bad }), JSON.stringify(bad)).toThrow(/object identifier/);
    }
  });
});

describe('reads at the pinned revision, from loose objects and packs, every object re-hashed', () => {
  it('reads the committed bytes, never the working tree, from loose objects', async () => {
    const [blob] = await reader(L, C2).readBlobs(['src/quoted.txt']);
    expect(blob).toMatchObject({ path: 'src/quoted.txt', mode: '100644', id: QUOTED_ID });
    expect(text(blob!.bytes)).toBe(QUOTED);
    expect(readFileSync(path.join(L, 'src/quoted.txt'), 'utf8')).toBe('An uncommitted working-tree edit.\n');
  });
  it('reads every kind of entry and lists the tree, in tree order', async () => {
    const r = reader(L, C2);
    expect(r.algorithm).toBe('sha1');
    expect(await r.tree()).toBe(TREE2);
    expect(await r.listTree()).toEqual(ALL_PATHS);
    const blobs = await r.readBlobs(['README.md', 'src/run.sh', 'link', 'big.txt']);
    expect(blobs.map(b => [b.mode, text(b.bytes)])).toEqual([['100644', 'hello\n'], ['100755', '#!/bin/sh\necho hi\n'], ['120000', 'src/quoted.txt'], ['100644', BIG(2)]]);
  });
  it('reads at the pinned commit, not at HEAD: commit one has the first version', async () => {
    const [big] = await reader(L, C1).readBlobs(['big.txt']);
    expect(big!.id).toBe(BIG1_ID);
    expect(text(big!.bytes)).toBe(BIG(1));
  });
  it('resolves offset deltas and reference deltas in packs to the same bytes', async () => {
    expect(ofsEntries.offsets.size).toBe(11);
    expect(ofsEntries.deltas).toBeGreaterThan(0);   // the fixture has deltas to resolve
    expect(refEntries.deltas).toBeGreaterThan(0);
    expect(existsSync(looseFile(OFS, QUOTED_ID))).toBe(false);
    for (const repo of [OFS, REF]) for (const rev of [C1, C2]) {
      const blobs = await reader(repo, rev).readBlobs(['big.txt', 'src/quoted.txt', 'README.md']);
      expect(blobs.map(b => text(b.bytes)), `${path.basename(repo)} at ${rev}`).toEqual([BIG(rev === C1 ? 1 : 2), QUOTED, 'hello\n']);
      expect(await reader(repo, rev).listTree()).toHaveLength(5);
    }
  });
  it('reads a SHA-256 clone under its 64-digit identifier, loose and packed', async () => {
    for (const repo of [S, SP]) {
      const r = reader(repo, S2);
      expect(r.algorithm).toBe('sha256');
      const [q] = await r.readBlobs(['src/quoted.txt']);
      expect(text(q!.bytes)).toBe(QUOTED);
      expect(q!.id).toBe('c69f7c3c1175628f676a508c2035936b2f21527dd577deddade1eb25d3091048');
    }
  });
});

describe('the clone\'s .git is untrusted: what an agent can plant there is refused or ignored', () => {
  it('an overwritten loose object, valid but other bytes, refuses with the identifier it was reached by', async () => {
    const repo = copy(L, 'overwritten');
    overwrite(looseFile(repo, QUOTED_ID), deflateSync(Buffer.from('blob 14\0Other bytes.\n\n')));
    expect(await refusal(reader(repo, C2).readBlobs(['src/quoted.txt']))).toEqual({
      reason: 'identifier-mismatch', objectId: QUOTED_ID, path: 'src/quoted.txt',
      message: `the object read as ${QUOTED_ID} hashes to b0e528470923605c7bed3aa46b985fec42f42157`,
    });
    // the other files still read: the refusal is the step's that needed the object
    expect(text((await reader(repo, C2).readBlobs(['README.md']))[0]!.bytes)).toBe('hello\n');
  });
  it('an overwritten tree or commit refuses every read below it', async () => {
    const repo = copy(L, 'overwritten-tree');
    overwrite(looseFile(repo, TREE2), readFileSync(looseFile(repo, TREE1)));
    expect((await refusal(reader(repo, C2).readBlobs(['README.md']))).reason).toBe('identifier-mismatch');
    expect((await refusal(reader(repo, C2).listTree())).objectId).toBe(TREE2);
    overwrite(looseFile(repo, C2), readFileSync(looseFile(repo, C1)));
    expect(await refusal(reader(repo, C2).tree())).toMatchObject({ reason: 'identifier-mismatch', objectId: C2 });
  });
  it('a corrupted loose object refuses as corrupt', async () => {
    const repo = copy(L, 'corrupt-loose');
    const file = looseFile(repo, QUOTED_ID), bytes = readFileSync(file);
    const k = bytes.length - 3;
    bytes[k] = bytes[k]! ^ 0xff;
    overwrite(file, bytes);
    expect(await refusal(reader(repo, C2).readBlobs(['src/quoted.txt']))).toEqual({ reason: 'corrupt-object', objectId: QUOTED_ID, path: 'src/quoted.txt', message: `loose object ${QUOTED_ID} does not inflate` });
    overwrite(file, deflateSync(Buffer.from(`blob 99\0${QUOTED}`)));   // a header whose size is not the body's
    expect((await refusal(reader(repo, C2).readBlobs(['src/quoted.txt']))).message).toBe(`loose object ${QUOTED_ID} has a malformed header`);
  });
  it('a corrupted pack entry refuses, for a whole object and for a delta', async () => {
    for (const [name, id] of [['corrupt-pack-whole', QUOTED_ID], ['corrupt-pack-delta', BIG1_ID]] as const) {
      const repo = copy(OFS, name), file = packFile(repo), bytes = readFileSync(file);
      const k = ofsEntries.offsets.get(id)! + 4;
      bytes[k] = bytes[k]! ^ 0x55;
      overwrite(file, bytes);
      const path_ = id === QUOTED_ID ? 'src/quoted.txt' : 'big.txt';
      expect(await refusal(reader(repo, id === QUOTED_ID ? C2 : C1).readBlobs([path_])), name).toMatchObject({ reason: 'corrupt-object', objectId: id });
    }
  });
  it('a pack entry that declares another size than it inflates to refuses, though its body would hash', async () => {
    const repo = copy(OFS, 'pack-size'), file = packFile(repo), bytes = readFileSync(file), at_ = ofsEntries.offsets.get(QUOTED_ID)!;
    expect([bytes[at_], bytes[at_ + 1]]).toEqual([0xb6, 0x02]);   // blob, 38 bytes: 6 + 2 * 16
    bytes[at_ + 1] = 0x03;   // declares 54
    overwrite(file, bytes);
    expect(await refusal(reader(repo, C2).readBlobs(['src/quoted.txt']))).toMatchObject({ reason: 'corrupt-object', message: `${QUOTED_ID}: pack entry inflates to 38 bytes, not the 54 it declares` });
  });
  it('a replace ref is never honoured: the original bytes are read', async () => {
    const repo = copy(L, 'replaced');
    writeFileSync(path.join(T, 'other.txt'), 'Replacement bytes.\n');
    const other = git(repo, ['hash-object', '-w', path.join(T, 'other.txt')]);
    git(repo, ['replace', QUOTED_ID, other]);
    git(repo, ['replace', '--graft', C2]);   // a parentless replacement commit for HEAD
    expect(git(repo, ['cat-file', 'blob', `${C2}:src/quoted.txt`])).toBe('Replacement bytes.');   // git itself honours it
    const [blob] = await reader(repo, C2).readBlobs(['src/quoted.txt']);
    expect([blob!.id, text(blob!.bytes)]).toEqual([QUOTED_ID, QUOTED]);
  });
  it('an alternates file is never followed: an object only an alternate holds refuses', async () => {
    const shared = path.join(T, 'shared');
    git(T, ['clone', '-q', '--shared', L, shared]);
    expect(readFileSync(path.join(shared, '.git/objects/info/alternates'), 'utf8')).toContain(path.join(L, '.git/objects'));
    expect(git(shared, ['cat-file', '-t', C2])).toBe('commit');   // git reads it through the alternate
    expect(await refusal(reader(shared, C2).tree())).toEqual({
      reason: 'object-missing', objectId: C2, path: null,
      message: `${C2} is in neither a loose object nor a pack of this clone; objects/info/alternates is present and is never followed`,
    });
  });
  it('grafts and a shallow file change nothing read: the walk never goes to a parent', async () => {
    const repo = copy(L, 'grafted');
    writeFileSync(path.join(repo, '.git/info/grafts'), `${C2}\n`);
    writeFileSync(path.join(repo, '.git/shallow'), `${C2}\n`);
    const r = reader(repo, C2);
    expect(await r.tree()).toBe(TREE2);
    expect(await r.listTree()).toEqual(ALL_PATHS);
  });
  it('repository-local configuration, hooks and attributes run nothing and change nothing', async () => {
    const repo = copy(L, 'configured'), marker = path.join(T, 'MARKER');
    const touch = `touch ${marker}`;
    writeFileSync(path.join(repo, '.git/config'), [
      '[core]', '\trepositoryformatversion = 1', `\tfsmonitor = ${touch}`, '\thooksPath = hooks', `\tsshCommand = ${touch}`, `\tpager = ${touch}`,
      '[extensions]', '\tobjectFormat = sha256', '[filter "evil"]', `\tsmudge = ${touch}`, `\ttextconv = ${touch}`, '[alias]', `\tcat-file = !${touch}`, '',
    ].join('\n'));
    writeFileSync(path.join(repo, '.git/info/attributes'), '* filter=evil diff=evil\n');
    mkdirSync(path.join(repo, 'hooks'), { recursive: true });
    for (const hook of ['post-checkout', 'pre-commit', 'reference-transaction', 'fsmonitor-watchman']) {
      for (const dir of [path.join(repo, 'hooks'), path.join(repo, '.git/hooks')]) { writeFileSync(path.join(dir, hook), `#!/bin/sh\n${touch}\n`); chmodSync(path.join(dir, hook), 0o755); }
    }
    const r = reader(repo, C2);
    expect(r.algorithm).toBe('sha1');   // extensions.objectFormat is not consulted
    expect(await r.listTree()).toEqual(ALL_PATHS);
    expect(text((await r.readBlobs(['src/quoted.txt']))[0]!.bytes)).toBe(QUOTED);
    expect(existsSync(marker)).toBe(false);
  });
  it('a .git file pointing elsewhere is never followed', async () => {
    const repo = path.join(T, 'gitfile');
    mkdirSync(repo);
    writeFileSync(path.join(repo, '.git'), `gitdir: ${path.join(L, '.git')}\n`);
    expect(await refusal(reader(repo, C2).tree())).toMatchObject({ reason: 'not-a-git-directory' });
  });
});

describe('the hash algorithm comes from the consented identifier, never from the clone', () => {
  it('a SHA-256 clone under a 40-digit identifier refuses, loose and packed', async () => {
    expect(await refusal(reader(S, C2).tree())).toMatchObject({ reason: 'object-missing', objectId: C2 });
    expect(await refusal(reader(S, S2.slice(0, 40)).tree())).toMatchObject({ reason: 'object-missing', objectId: S2.slice(0, 40) });
    expect(await refusal(reader(SP, S2.slice(0, 40)).tree())).toMatchObject({ reason: 'invalid-pack-index' });
  });
  it('a SHA-1 clone under a 64-digit identifier refuses', async () => {
    expect(await refusal(reader(L, S2).tree())).toMatchObject({ reason: 'object-missing', objectId: S2 });
    expect(await refusal(reader(OFS, S2).tree())).toMatchObject({ reason: 'invalid-pack-index' });
  });
});

describe('paths, types, and no state between calls', () => {
  it('a path that is absent, a directory, a submodule or malformed refuses', async () => {
    const r = reader(L, C2);
    expect(await refusal(r.readBlobs(['missing.txt']))).toMatchObject({ reason: 'path-not-found', path: 'missing.txt' });
    expect(await refusal(r.readBlobs(['README.md/x']))).toMatchObject({ reason: 'path-not-found', path: 'README.md/x' });
    expect(await refusal(r.readBlobs(['src']))).toMatchObject({ reason: 'not-a-blob', path: 'src' });
    const repo = copy(L, 'gitlink');
    git(repo, ['update-index', '--add', '--cacheinfo', `160000,${C1},vendor`]);
    git(repo, ['commit', '-q', '-m', 'three'], at('2026-10-06T00:02:00Z'));
    expect(await refusal(reader(repo, git(repo, ['rev-parse', 'HEAD'])).readBlobs(['vendor']))).toMatchObject({ reason: 'not-a-blob', objectId: C1, path: 'vendor' });
    expect(await reader(repo, git(repo, ['rev-parse', 'HEAD'])).listTree()).toContainEqual({ path: 'vendor', mode: '160000', id: C1 });
    for (const bad of ['', '/README.md', 'src//quoted.txt', './README.md', 'src/../README.md', 'README.md/']) {
      expect(await refusal(r.readBlobs([bad])), JSON.stringify(bad)).toMatchObject({ reason: 'malformed-path' });
    }
  });
  it('a pinned identifier that names a tree or a blob refuses as the wrong type', async () => {
    expect(await refusal(reader(L, TREE2).tree())).toMatchObject({ reason: 'type-mismatch', objectId: TREE2, message: `${TREE2} is a tree, not a commit` });
    expect(await refusal(reader(OFS, QUOTED_ID).tree())).toMatchObject({ reason: 'type-mismatch' });
  });
  it('one refused path refuses the whole call', async () => {
    expect(await refusal(reader(L, C2).readBlobs(['README.md', 'missing.txt']))).toMatchObject({ reason: 'path-not-found' });
  });
  it('re-reads on every call: an object overwritten after a good read refuses the next', async () => {
    const repo = copy(L, 'later'), r = reader(repo, C2);
    expect(text((await r.readBlobs(['src/quoted.txt']))[0]!.bytes)).toBe(QUOTED);
    overwrite(looseFile(repo, QUOTED_ID), deflateSync(Buffer.from('blob 14\0Other bytes.\n\n')));
    expect((await refusal(r.readBlobs(['src/quoted.txt']))).reason).toBe('identifier-mismatch');
  });
  it('the reader imports nothing that can start a process', () => {
    const source = readFileSync(fileURLToPath(new URL('./git-object-reader.ts', import.meta.url)), 'utf8');
    expect(source.match(/^import .*$/gm)).toEqual([
      "import { createHash } from 'node:crypto';",
      "import { lstat, open, readdir, readFile, type FileHandle } from 'node:fs/promises';",
      "import path from 'node:path';",
      "import { inflateSync } from 'node:zlib';",
    ]);
    expect(source).not.toMatch(/child_process|\bspawn(Sync)?\(|(?<![.\w])exec(File)?(Sync)?\(|\bimport\(|\brequire\(|\bprocess\./);
  });
});
