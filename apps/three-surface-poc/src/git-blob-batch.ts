// One `git cat-file --batch` process for many blobs (syzygy-svoj). The
// governance loader and the self-corpus reader each read a hundred or more
// blobs; spawning one `git cat-file blob` per object cost about a second
// alone and several under load. This reads exactly the objects it is given,
// in one process, and parses the output strictly: a missing, ambiguous or
// non-blob object is a per-object error the caller handles as it handled a
// failed single read, and any malformed, short or trailing output fails the
// whole batch.

import { isolatedGit } from './polaris-generation/isolated-git.js';

export type GitBlobBatch = ReadonlyMap<string, Uint8Array | Error>;
export type ReadGitBlobs = (repoRoot: string, objects: readonly string[]) => GitBlobBatch;

const FULL_OBJECT_ID = /^(?:[0-9a-f]{40}|[0-9a-f]{64})$/;
const FOUND_HEADER = /^([0-9a-f]{40}|[0-9a-f]{64}) ([a-z]+) (0|[1-9][0-9]*)$/;
const NEWLINE = 0x0a;

export function readGitBlobsBatch(repoRoot: string, objects: readonly string[]): GitBlobBatch {
  const unique = [...new Set(objects)];
  if (unique.length === 0) return new Map();
  for (const object of unique) {
    if (object === '' || /[\n\r\0]/.test(object)) throw new Error('git blob batch: an object name must be one non-empty line');
  }
  const output = isolatedGit(repoRoot, ['cat-file', '--batch'], unique.map((object) => `${object}\n`).join(''));
  return parseGitCatFileBatch(unique, new Uint8Array(output.buffer, output.byteOffset, output.byteLength));
}

/** Parses `git cat-file --batch` output for `objects`, requested in this order. */
export function parseGitCatFileBatch(objects: readonly string[], output: Uint8Array): GitBlobBatch {
  const decoder = new TextDecoder('utf-8', { fatal: true });
  const results = new Map<string, Uint8Array | Error>();
  let offset = 0;
  for (const object of objects) {
    const newline = output.indexOf(NEWLINE, offset);
    if (newline < 0) throw new Error(`git blob batch: output ends before the header for ${object}`);
    const header = decoder.decode(output.subarray(offset, newline));
    offset = newline + 1;
    if (header === `${object} missing` || header === `${object} ambiguous`) {
      results.set(object, new Error(`git object ${header.slice(object.length + 1)}: ${object}`));
      continue;
    }
    const found = FOUND_HEADER.exec(header);
    if (found === null) throw new Error(`git blob batch: unexpected header for ${object}`);
    const [, objectId, type, sizeText] = found as unknown as [string, string, string, string];
    if (FULL_OBJECT_ID.test(object) && objectId !== object) throw new Error(`git blob batch: answered ${objectId} for ${object}`);
    const size = Number(sizeText);
    // The body must be followed by the newline git writes after it; a short
    // or oversized size reaches past it (or past the end) and fails here.
    if (output[offset + size] !== NEWLINE) throw new Error(`git blob batch: short read for ${object}`);
    const body = output.slice(offset, offset + size);
    offset += size + 1;
    results.set(object, type === 'blob' ? body : new Error(`git object is a ${type}, not a blob: ${object}`));
  }
  if (offset !== output.length) throw new Error('git blob batch: output continues past the last requested object');
  return results;
}
