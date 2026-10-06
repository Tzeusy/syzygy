import * as fs from 'node:fs';
import * as path from 'node:path';
import type { StoreInventory } from './git-object-reader.js';

/** Whether the clone holds the consented commit alone (syzygy-qkea.24). The consent's stated form is one consented commit fetched
 * alone into an empty repository, because the agent reads whatever the clone holds; a command printed for the operator proves nothing
 * about the clone actually made, so `init` refuses, before the run starts, a `.git` that holds more than that form leaves there.
 *
 * The check is an allowlist (R-POLARIS-DOSSIER-CLONE-SHAPE-1 findings 1 and 2). `.git` may hold only the entries in `GIT_DIR`, which
 * is what `git init <dir>`, `git -C <dir> fetch --depth=1 <url> <commit>` and `git -C <dir> checkout --detach FETCH_HEAD` leave there:
 * derived 2026-10-07 by running that sequence with git 2.53.0 and its default template (no global or system configuration) for a
 * root commit, a commit with a parent fetched small (loose objects) and one fetched large (a pack), and listing every path. Each entry
 * then holds only what that form puts in it:
 * - HEAD detached at the commit; FETCH_HEAD naming no object but the commit; `shallow` exactly the commit (or absent for a commit
 *   with no parent); `logs/` only `HEAD`, each line naming only the commit or the zero identifier;
 * - `refs/` only directories, so no ref but HEAD; `hooks/` only regular `*.sample` files, which git never runs; `info/` only `exclude`;
 * - `objects/` only fan-out directories of loose objects (two hex digits, then the rest of an identifier), an empty `info/`, and
 *   `pack/` holding `pack-<hex>.pack` and `.idx` in pairs, each with an optional `.rev`; `objects/info/alternates` and
 *   `http-alternates` are refused by name, as is any `.promisor`, `.keep`, `tmp_*` or unpaired pack;
 * - and the store names no identifier but the commit and the trees and blobs under its tree (StoreInventory).
 * So `commondir`, `modules/`, `worktrees/`, `packed-refs`, `ORIG_HEAD`, `info/grafts`, `BISECT_*`, `rebase-*` and every other name
 * are refused. Every entry is examined by `lstat` and a symbolic link anywhere under `.git` is refused, never followed; every file
 * read is opened with O_NOFOLLOW and checked on the open handle, as the object reader opens its files, and bounded; every listing is
 * read one entry at a time against one bound for the whole walk. `config`, `description` and `index` must be regular files and are
 * not read (the reader honours no repository configuration). No process runs.
 * Residuals: the check runs at `init` only, and the clone stays within the agent sessions' write reach afterwards; the store's
 * identifiers are the names it gives (see StoreInventory: a pack entry its `.idx` omits is not named); a git, or a template, that
 * leaves more in `.git` than git 2.53.0's default does is refused, failing closed; and the working tree outside `.git` is not
 * inspected, though the agent reads the checked-out files, so anything placed there, a nested repository included, is not seen. */

export type CloneShape = { readonly ok: true } | { readonly ok: false; readonly reason: string };

const MAX_FILE_BYTES = 1024 * 1024;
/** Directory entries listed over the whole walk of `.git`, loose objects included. */
const MAX_ENTRIES = 1_000_000;
/** What the consented form leaves at the top of `.git` (derived as the header states), and the kind each must be. */
const GIT_DIR: Readonly<Record<string, 'file' | 'directory'>> = {
  FETCH_HEAD: 'file', HEAD: 'file', config: 'file', description: 'file', hooks: 'directory', index: 'file', info: 'directory',
  logs: 'directory', objects: 'directory', refs: 'directory', shallow: 'file',
};
const SHAPE = 'the clone must hold the consented commit alone, fetched into an empty repository (git init, git fetch --depth=1 <url> <commit>, git checkout --detach FETCH_HEAD)';
const OPEN_FLAGS = fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK;

class Refused extends Error {}
const refused = (reason: string): never => { throw new Refused(reason); };
const errno = (cause: unknown): string => (cause as NodeJS.ErrnoException).code ?? 'unknown-error';

/** A regular file's text, null when absent; opened without following a link and checked on the open handle, and bounded. */
function readRegular(gitDir: string, file: string): string | null {
  const rel = path.relative(gitDir, file);
  let fd: number;
  try { fd = fs.openSync(file, OPEN_FLAGS); } catch (cause) {
    if (errno(cause) === 'ENOENT') return null;
    if (errno(cause) === 'ELOOP') return refused(`${rel} is a symbolic link; nothing under .git is followed`);
    return refused(`${rel} cannot be read (${errno(cause)})`);
  }
  try {
    const stats = fs.fstatSync(fd);
    if (!stats.isFile()) return refused(`${rel} is not a regular file`);
    if (stats.size > MAX_FILE_BYTES) return refused(`${rel} is larger than ${MAX_FILE_BYTES} bytes`);
    const buf = Buffer.alloc(MAX_FILE_BYTES + 1);
    let length = 0;
    for (let n = 1; n > 0 && length < buf.length; length += n) n = fs.readSync(fd, buf, length, buf.length - length, null);
    if (length > MAX_FILE_BYTES) return refused(`${rel} is larger than ${MAX_FILE_BYTES} bytes`);
    return buf.subarray(0, length).toString('latin1');
  } finally { fs.closeSync(fd); }
}

/** A directory's entries, each `lstat`ed, read one at a time against the walk's bound; a symbolic link is refused. */
function listing(gitDir: string, dir: string, budget: { left: number; readonly max: number }): { readonly name: string; readonly stats: fs.Stats }[] {
  const out: { name: string; stats: fs.Stats }[] = [];
  let handle: fs.Dir;
  try { handle = fs.opendirSync(dir); } catch (cause) { return refused(`${path.relative(gitDir, dir) || '.git'} cannot be listed (${errno(cause)})`); }
  try {
    for (let entry = handle.readSync(); entry !== null; entry = handle.readSync()) {
      budget.left -= 1;
      if (budget.left < 0) refused(`.git holds more than ${budget.max} entries`);
      const rel = path.relative(gitDir, path.join(dir, entry.name));
      const stats = fs.lstatSync(path.join(dir, entry.name));
      if (stats.isSymbolicLink()) refused(`${rel} is a symbolic link; nothing under .git is followed`);
      out.push({ name: entry.name, stats });
    }
  } finally { handle.closeSync(); }
  return out.sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
}

/** Every identifier-shaped token in `text` is one of `allowed`. */
const namesOnly = (text: string, width: number, allowed: readonly string[]): string | undefined =>
  (text.match(new RegExp(`\\b[0-9a-f]{${width}}\\b`, 'gu')) ?? []).find(id => !allowed.includes(id));

/** The `.git` allowlist, which reads no object: every entry is one the consented form leaves, holding only what it leaves there. */
export function cloneGitDirShape(gitDir: string, commit: string, bounds: { readonly maxEntries?: number } = {}): CloneShape {
  try {
    checkGitDir(gitDir, commit, bounds.maxEntries ?? MAX_ENTRIES);
    return { ok: true };
  } catch (cause) {
    if (cause instanceof Refused) return { ok: false, reason: `${cause.message}; ${SHAPE}` };
    throw cause;
  }
}

function checkGitDir(gitDir: string, commit: string, maxEntries: number): void {
  const width = commit.length;
  const zero = '0'.repeat(width);
  const budget = { left: maxEntries, max: maxEntries };
  const at = (...parts: string[]): string => path.join(gitDir, ...parts);

  // Alternates first, by name, whatever kind of entry they are: either lends the store another repository's objects.
  for (const name of ['alternates', 'http-alternates']) {
    try { fs.lstatSync(at('objects', 'info', name)); } catch (cause) {
      if (errno(cause) === 'ENOENT' || errno(cause) === 'ENOTDIR') continue;
      refused(`objects/info/${name} cannot be read (${errno(cause)})`);
    }
    refused(`objects/info/${name} exists, and would lend the clone another repository's objects`);
  }

  for (const { name, stats } of listing(gitDir, gitDir, budget)) {
    const kind = GIT_DIR[name];
    if (kind === undefined) refused(`.git holds ${name}, which the consented form never leaves there`);
    if (kind === 'file' ? !stats.isFile() : !stats.isDirectory()) refused(`${name} is not a ${kind === 'file' ? 'regular file' : 'directory'}`);
  }

  const head = readRegular(gitDir, at('HEAD'));
  if (head === null) refused('HEAD is absent');
  if (head!.replace(/\n$/u, '') !== commit) refused(`HEAD is not detached at ${commit}`);

  const fetchHead = readRegular(gitDir, at('FETCH_HEAD'));
  if (fetchHead !== null && namesOnly(fetchHead, width, [commit]) !== undefined) refused(`FETCH_HEAD names an object other than ${commit}`);

  const pending = [at('refs')];
  while (pending.length > 0) {
    const dir = pending.pop()!;
    if (!fs.existsSync(dir) && dir === at('refs')) break;
    for (const { name, stats } of listing(gitDir, dir, budget)) {
      if (!stats.isDirectory()) refused(`${path.relative(gitDir, path.join(dir, name))} is a ref or not a directory, and the clone may hold no ref but HEAD`);
      pending.push(path.join(dir, name));
    }
  }

  const only = (dir: string, allowed: (name: string, stats: fs.Stats) => boolean, what: string): void => {
    if (!fs.existsSync(at(dir))) return;
    for (const { name, stats } of listing(gitDir, at(dir), budget)) {
      if (!allowed(name, stats)) refused(`${dir}/${name} is not ${what}`);
    }
  };
  only('hooks', (name, stats) => stats.isFile() && name.endsWith('.sample'), 'a sample hook, the only kind the consented form leaves');
  only('info', (name, stats) => stats.isFile() && name === 'exclude', 'info/exclude, the only entry the consented form leaves there');
  only('logs', (name, stats) => stats.isFile() && name === 'HEAD', 'logs/HEAD, the only log the consented form leaves');
  const log = fs.existsSync(at('logs')) ? readRegular(gitDir, at('logs', 'HEAD')) : null;
  if (log !== null) {
    const other = namesOnly(log, width, [commit, zero]);
    if (other !== undefined) refused(`logs/HEAD names ${other}, an object other than ${commit}`);
  }

  const fanOut = /^[0-9a-f]{2}$/u;
  const loose = new RegExp(`^[0-9a-f]{${width - 2}}$`, 'u');
  const packFile = new RegExp(`^pack-[0-9a-f]{${width}}\\.(pack|idx|rev)$`, 'u');
  for (const { name, stats } of listing(gitDir, at('objects'), budget)) {
    if (name === 'info' && stats.isDirectory()) {
      const held = listing(gitDir, at('objects', 'info'), budget);
      if (held.length > 0) refused(`objects/info holds ${held[0]!.name}, and the consented form leaves it empty`);
    } else if (name === 'pack' && stats.isDirectory()) {
      const stems = new Map<string, Set<string>>();
      for (const file of listing(gitDir, at('objects', 'pack'), budget)) {
        const match = packFile.exec(file.name);
        if (match === null || !file.stats.isFile()) refused(`objects/pack/${file.name} is not a pack, index or reverse index the consented form leaves`);
        const stem = file.name.slice(0, -(match![1]!.length + 1));
        stems.set(stem, (stems.get(stem) ?? new Set()).add(match![1]!));
      }
      for (const [stem, kinds] of stems) {
        if (!kinds.has('pack') || !kinds.has('idx')) refused(`objects/pack/${stem} is not a .pack with its .idx`);
      }
    } else if (fanOut.test(name) && stats.isDirectory()) {
      for (const file of listing(gitDir, at('objects', name), budget)) {
        if (!loose.test(file.name) || !file.stats.isFile()) refused(`objects/${name}/${file.name} is not a loose object`);
      }
    } else {
      refused(`objects/${name} is not an entry the consented form leaves in the object store`);
    }
  }
}

/** The shallow and object-store checks, from the store's inventory: shallow at exactly `commit`, and nothing beyond its tree. */
export function cloneStoreShape(gitDir: string, commit: string, inventory: StoreInventory): CloneShape {
  try {
    const shallow = readRegular(gitDir, path.join(gitDir, 'shallow'));
    const rows = shallow === null ? [] : shallow.split('\n').filter(row => row !== '');
    if ((inventory.parents.length > 0 || shallow !== null) && (rows.length !== 1 || rows[0] !== commit)) {
      refused(shallow === null
        ? `the clone is not shallow, and ${commit} has ${inventory.parents.length} parent(s)`
        : `the clone is shallow at ${rows.length} commit(s), not at ${commit} alone`);
    }
    if (inventory.beyondCount > 0) {
      refused(`the object store names ${inventory.beyondCount} object(s) that are neither ${commit} nor under its tree (first: ${inventory.beyond.slice(0, 3).join(', ')})`);
    }
    return { ok: true };
  } catch (cause) {
    if (cause instanceof Refused) return { ok: false, reason: `${cause.message}; ${SHAPE}` };
    throw cause;
  }
}
