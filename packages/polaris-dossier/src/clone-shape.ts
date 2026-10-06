import * as fs from 'node:fs';
import * as path from 'node:path';
import type { StoreInventory } from './git-object-reader.js';

/** Whether the clone holds the consented commit alone (syzygy-qkea.24). The consent's stated form is one consented commit fetched
 * alone into an empty repository, because the agent reads whatever the clone holds; a command printed for the operator proves nothing
 * about the clone actually made, so `init` refuses, before the run starts, a clone that:
 * - has any ref but HEAD: a file anywhere under `refs/`, a ref line in `packed-refs`, a linked worktree, or a pseudo-ref
 *   (`FETCH_HEAD`, `ORIG_HEAD` and the like) naming any object but the pinned commit; HEAD must be detached at that commit;
 * - is not shallow at exactly that commit: `shallow` must hold that one identifier, or, for a commit with no parent, may be absent;
 * - names in its object store any identifier but the pinned commit and the trees and blobs under its tree (StoreInventory).
 * Every file here is read as the object reader reads: by `lstat` first, a symbolic link or special file refused and never followed,
 * each file bounded; no process runs. Residuals: the check runs at `init` only, and the clone stays within the agent sessions' write
 * reach afterwards; and the store's identifiers are the names it gives (see StoreInventory). */

export type CloneShape = { readonly ok: true } | { readonly ok: false; readonly reason: string };

const MAX_FILE_BYTES = 1024 * 1024;
const MAX_REF_ENTRIES = 10_000;
const PSEUDO_REF = /^[A-Z][A-Z_]*_HEAD$|^AUTO_MERGE$/;

type Read = { readonly text: string } | { readonly reason: string } | null;

/** A regular file's text, null when absent; a link, a directory or a special file, or a file over the bound, is a reason. */
function readRegular(gitDir: string, file: string): Read {
  let stats: fs.Stats;
  try { stats = fs.lstatSync(file); } catch (cause) {
    if ((cause as NodeJS.ErrnoException).code === 'ENOENT') return null;
    return { reason: `${path.relative(gitDir, file)} cannot be read (${(cause as NodeJS.ErrnoException).code ?? 'unknown-error'})` };
  }
  if (!stats.isFile()) return { reason: `${path.relative(gitDir, file)} is not a regular file; nothing under .git is read through a symbolic link` };
  if (stats.size > MAX_FILE_BYTES) return { reason: `${path.relative(gitDir, file)} is larger than ${MAX_FILE_BYTES} bytes` };
  return { text: fs.readFileSync(file, 'latin1') };
}

/** The refs check, which reads no object: HEAD detached at `commit`, and no other ref. */
export function cloneRefShape(gitDir: string, commit: string): CloneShape {
  const refuse = (reason: string): CloneShape => ({ ok: false, reason: `${reason}; the clone must hold the consented commit alone, fetched into an empty repository (git init, git fetch --depth=1 <url> <commit>, git checkout --detach FETCH_HEAD)` });

  const head = readRegular(gitDir, path.join(gitDir, 'HEAD'));
  if (head === null || 'reason' in head) return refuse(head === null ? 'HEAD is absent' : head.reason);
  if (head.text.replace(/\n$/u, '') !== commit) return refuse(`HEAD is not detached at ${commit}`);

  const refs = path.join(gitDir, 'refs');
  const pending = [refs];
  let seen = 0;
  while (pending.length > 0) {
    const dir = pending.pop()!;
    let stats: fs.Stats;
    try { stats = fs.lstatSync(dir); } catch (cause) {
      if ((cause as NodeJS.ErrnoException).code === 'ENOENT' && dir === refs) break;
      return refuse(`${path.relative(gitDir, dir)} cannot be read (${(cause as NodeJS.ErrnoException).code ?? 'unknown-error'})`);
    }
    if (!stats.isDirectory()) return refuse(`${path.relative(gitDir, dir)} is a ref or not a directory, and the clone may hold no ref but HEAD`);
    for (const name of fs.readdirSync(dir).sort()) {
      seen += 1;
      if (seen > MAX_REF_ENTRIES) return refuse(`refs/ holds more than ${MAX_REF_ENTRIES} entries`);
      pending.push(path.join(dir, name));
    }
  }

  const packed = readRegular(gitDir, path.join(gitDir, 'packed-refs'));
  if (packed !== null) {
    if ('reason' in packed) return refuse(packed.reason);
    const ref = packed.text.split('\n').find(row => row !== '' && !row.startsWith('#'));
    if (ref !== undefined) return refuse('packed-refs holds a ref, and the clone may hold no ref but HEAD');
  }

  try {
    if (fs.lstatSync(path.join(gitDir, 'worktrees')).isDirectory() && fs.readdirSync(path.join(gitDir, 'worktrees')).length > 0) {
      return refuse('the clone has a linked worktree, whose HEAD is another ref');
    }
  } catch (cause) {
    if ((cause as NodeJS.ErrnoException).code !== 'ENOENT') return refuse(`worktrees cannot be read (${(cause as NodeJS.ErrnoException).code ?? 'unknown-error'})`);
  }

  const width = commit.length;
  for (const name of fs.readdirSync(gitDir).filter(n => PSEUDO_REF.test(n)).sort()) {
    const pseudo = readRegular(gitDir, path.join(gitDir, name));
    if (pseudo === null) continue;
    if ('reason' in pseudo) return refuse(pseudo.reason);
    const named = pseudo.text.match(new RegExp(`\\b[0-9a-f]{${width}}\\b`, 'gu')) ?? [];
    if (named.some(id => id !== commit)) return refuse(`${name} names an object other than ${commit}`);
  }
  return { ok: true };
}

/** The shallow and object-store checks, from the store's inventory: shallow at exactly `commit`, and nothing beyond its tree. */
export function cloneStoreShape(gitDir: string, commit: string, inventory: StoreInventory): CloneShape {
  const refuse = (reason: string): CloneShape => ({ ok: false, reason: `${reason}; the clone must hold the consented commit alone, fetched into an empty repository (git init, git fetch --depth=1 <url> <commit>, git checkout --detach FETCH_HEAD)` });
  const shallow = readRegular(gitDir, path.join(gitDir, 'shallow'));
  if (shallow !== null && 'reason' in shallow) return refuse(shallow.reason);
  const rows = shallow === null ? [] : shallow.text.split('\n').filter(row => row !== '');
  if (inventory.parents.length > 0 || shallow !== null) {
    if (rows.length !== 1 || rows[0] !== commit) {
      return refuse(shallow === null
        ? `the clone is not shallow, and ${commit} has ${inventory.parents.length} parent(s)`
        : `the clone is shallow at ${rows.length} commit(s), not at ${commit} alone`);
    }
  }
  if (inventory.beyondCount > 0) {
    return refuse(`the object store names ${inventory.beyondCount} object(s) that are neither ${commit} nor under its tree (first: ${inventory.beyond.slice(0, 3).join(', ')})`);
  }
  return { ok: true };
}
