import { createHash } from 'node:crypto';
import { lstat, open, readdir, readFile, type FileHandle } from 'node:fs/promises';
import path from 'node:path';
import { inflateSync } from 'node:zlib';

/** Reads Git objects at one pinned revision of a clone, in process (REQ-polaris-generation-033, the reads sentence; design decision 1).
 *
 * The clone's `.git` directory is within the agent sessions' write reach, so nothing in it is trusted except object bytes that hash to
 * the identifier they were reached by. The reader:
 * - reads only the object store (`objects/` loose files and `objects/pack/` packs), never a ref, the index, the working tree,
 *   `config`, hooks, `objects/info/alternates`, `info/grafts`, `shallow`, `refs/replace/` or a commit-graph, and spawns no process;
 * - takes the hash algorithm from the consented identifier (40 hex digits SHA-1, 64 SHA-256), never `extensions.objectFormat`;
 * - walks down from the pinned commit to its tree and from there to each entry, never to a parent;
 * - on every call, re-reads and recomputes the identifier of every commit, tree and blob on the way down, and refuses
 *   (`GitObjectReadRefusal`) when one differs from the identifier it was reached by, is missing (an object only an alternate or a
 *   replacement could supply is missing), cannot be decoded, or has the wrong type. Nothing verified is kept between calls.
 * Classification and screening of what it returns (REQ-polaris-generation-025) are the caller's. */

export type HashAlgorithm = 'sha1' | 'sha256';
export type GitObjectType = 'commit' | 'tree' | 'blob' | 'tag';
export type GitObjectReadRefusalReason =
  | 'malformed-identifier' | 'not-a-git-directory' | 'malformed-path' | 'object-missing' | 'corrupt-object' | 'identifier-mismatch'
  | 'type-mismatch' | 'malformed-commit' | 'malformed-tree' | 'path-not-found' | 'not-a-blob' | 'invalid-pack-index';

/** A refused read, in human form (`message`) and machine form (`toJSON()`). None of the refused object's content is carried. */
export class GitObjectReadRefusal extends Error {
  constructor(
    readonly reason: GitObjectReadRefusalReason,
    message: string,
    readonly objectId: string | null = null,
    readonly path: string | null = null,
  ) {
    super(message);
    this.name = 'GitObjectReadRefusal';
  }
  toJSON(): { readonly reason: GitObjectReadRefusalReason; readonly objectId: string | null; readonly path: string | null; readonly message: string } {
    return { reason: this.reason, objectId: this.objectId, path: this.path, message: this.message };
  }
}

const refuse = (reason: GitObjectReadRefusalReason, message: string, objectId: string | null = null, at: string | null = null): never => {
  throw new GitObjectReadRefusal(reason, message, objectId, at);
};

/** The algorithm a consented identifier is written in: lowercase hex, 40 digits SHA-1 or 64 SHA-256. Anything else refuses. */
export function hashAlgorithmOf(identifier: string): HashAlgorithm {
  if (/^[0-9a-f]{40}$/.test(identifier)) return 'sha1';
  if (/^[0-9a-f]{64}$/.test(identifier)) return 'sha256';
  return refuse('malformed-identifier', `"${identifier.slice(0, 80)}" is not a 40- or 64-digit lowercase hex object identifier`);
}

export interface TreeEntry {
  readonly path: string;
  readonly mode: string;
  readonly id: string;
}
export interface VerifiedBlob extends TreeEntry {
  readonly bytes: Uint8Array;
}
export interface PinnedObjectReader {
  readonly revision: string;
  readonly algorithm: HashAlgorithm;
  /** The pinned commit's tree identifier, the commit re-hashed. */
  tree(): Promise<string>;
  /** Each path's blob at the pinned revision (a regular file or a symbolic link's target), every object from the commit down
   * re-hashed. One refusal refuses the whole call. */
  readBlobs(paths: readonly string[]): Promise<readonly VerifiedBlob[]>;
  /** Every non-tree entry under the pinned commit's tree, by path in tree order, every tree re-hashed (blobs are not read). */
  listTree(): Promise<readonly TreeEntry[]>;
}

export interface PinnedObjectReaderOptions {
  /** The clone's `.git` directory. A `.git` file (a gitdir pointer) is refused, never followed. */
  readonly gitDir: string;
  /** The consented revision: the full commit identifier the in-force observation consent names. */
  readonly revision: string;
  /** Largest object, inflated, the reader will hold. Default 1 GiB. */
  readonly maxObjectBytes?: number;
}

export function openPinnedObjectReader(options: PinnedObjectReaderOptions): PinnedObjectReader {
  const algorithm = hashAlgorithmOf(options.revision);
  const revision = options.revision, maxObjectBytes = options.maxObjectBytes ?? 2 ** 30;
  const step = async <T>(body: (walk: Walk) => Promise<T>): Promise<T> => {
    const store = await ObjectStore.open(options.gitDir, algorithm, maxObjectBytes);
    try { return await body(new Walk(store, revision)); } finally { await store.close(); }
  };
  return {
    revision, algorithm,
    tree: () => step(walk => walk.rootTree()),
    readBlobs: paths => step(async walk => {
      const out: VerifiedBlob[] = [];
      for (const p of paths) out.push(await walk.blob(p));
      return out;
    }),
    listTree: () => step(async walk => walk.list(await walk.rootTree(), '')),
  };
}

const HEX = { sha1: 40, sha256: 64 } as const;

/** One call's walk from the pinned commit. Trees verified during the call are reused within it, never across calls. */
class Walk {
  private readonly trees = new Map<string, readonly RawEntry[]>();
  constructor(private readonly store: ObjectStore, private readonly revision: string) {}

  async rootTree(): Promise<string> {
    const body = await this.store.verified(this.revision, 'commit', null);
    const text = Buffer.from(body).toString('latin1');
    const tree = new RegExp(`^tree ([0-9a-f]{${HEX[this.store.algorithm]}})\n`).exec(text);
    return tree === null ? refuse('malformed-commit', `commit ${this.revision} does not open with a tree line in the consented hash`, this.revision) : tree[1]!;
  }

  async blob(target: string): Promise<VerifiedBlob> {
    const segments = target.split('/');
    if (target === '' || segments.some(s => s === '' || s === '.' || s === '..' || s.includes('\0'))) {
      refuse('malformed-path', `"${target}" is not a relative path of non-empty segments`, null, target);
    }
    let tree = await this.rootTree();
    for (const [i, name] of segments.entries()) {
      const at = segments.slice(0, i + 1).join('/');
      const entry = (await this.tree(tree, at)).find(e => e.name === name);
      if (entry === undefined) return refuse('path-not-found', `${at} is not in the tree at ${this.revision}`, tree, target);
      const last = i === segments.length - 1;
      if (!last) {
        if (entry.mode !== '40000') return refuse('path-not-found', `${at} is not a directory at ${this.revision}`, entry.id, target);
        tree = entry.id;
        continue;
      }
      if (entry.mode === '40000' || entry.mode === '160000') return refuse('not-a-blob', `${target} is a ${entry.mode === '40000' ? 'directory' : 'submodule'}, not a file`, entry.id, target);
      return { path: target, mode: entry.mode, id: entry.id, bytes: await this.store.verified(entry.id, 'blob', target) };
    }
    return refuse('malformed-path', `"${target}" names nothing`, null, target);
  }

  async list(tree: string, prefix: string): Promise<TreeEntry[]> {
    const out: TreeEntry[] = [];
    for (const e of await this.tree(tree, prefix === '' ? null : prefix)) {
      const p = prefix === '' ? e.name : `${prefix}/${e.name}`;
      if (e.mode === '40000') out.push(...await this.list(e.id, p));
      else out.push({ path: p, mode: e.mode, id: e.id });
    }
    return out;
  }

  private async tree(id: string, at: string | null): Promise<readonly RawEntry[]> {
    const known = this.trees.get(id);
    if (known !== undefined) return known;
    const entries = parseTree(await this.store.verified(id, 'tree', at), id, this.store.algorithm);
    this.trees.set(id, entries);
    return entries;
  }
}

interface RawEntry { readonly mode: string; readonly name: string; readonly id: string }
function parseTree(body: Uint8Array, id: string, algorithm: HashAlgorithm): RawEntry[] {
  const width = HEX[algorithm] / 2, buf = Buffer.from(body), out: RawEntry[] = [];
  let at = 0;
  while (at < buf.length) {
    const space = buf.indexOf(0x20, at), nul = space < 0 ? -1 : buf.indexOf(0, space);
    if (space < 0 || nul < 0 || nul + 1 + width > buf.length) refuse('malformed-tree', `tree ${id} has a truncated entry`, id);
    const mode = buf.toString('latin1', at, space), name = buf.toString('utf8', space + 1, nul);
    if (!/^[0-7]{5,6}$/.test(mode) || name === '' || name.includes('/')) refuse('malformed-tree', `tree ${id} has a malformed entry`, id);
    out.push({ mode, name, id: buf.toString('hex', nul + 1, nul + 1 + width) });
    at = nul + 1 + width;
  }
  return out;
}

const PACK_TYPES: Readonly<Record<number, GitObjectType>> = { 1: 'commit', 2: 'tree', 3: 'blob', 4: 'tag' };
const OFS_DELTA = 6, REF_DELTA = 7, MAX_DELTA_CHAIN = 10_000;

interface PackIndex { readonly name: string; readonly ids: Buffer; readonly offsets: readonly number[]; readonly count: number }

/** The clone's own object store, read once per call: loose objects first, then packs in name order. Nothing else under `.git`. */
class ObjectStore {
  private readonly handles = new Map<string, FileHandle>();
  private constructor(
    private readonly objects: string,
    readonly algorithm: HashAlgorithm,
    private readonly packs: readonly PackIndex[],
    private readonly maxObjectBytes: number,
    private readonly alternatesPresent: boolean,
  ) {}

  static async open(gitDir: string, algorithm: HashAlgorithm, maxObjectBytes: number): Promise<ObjectStore> {
    let isDir = false;
    try { isDir = (await lstat(gitDir)).isDirectory(); } catch { isDir = false; }
    if (!isDir) refuse('not-a-git-directory', `${gitDir} is not a directory; a gitdir pointer file is never followed`);
    const objects = path.join(gitDir, 'objects'), packDir = path.join(objects, 'pack');
    let names: string[] = [];
    try { names = (await readdir(packDir)).filter(n => n.endsWith('.idx')).sort(); } catch { names = []; }
    const packs: PackIndex[] = [];
    for (const name of names) packs.push(parseIndex(await readFile(path.join(packDir, name)), name.slice(0, -4), algorithm));
    let alternatesPresent = false;
    try { alternatesPresent = (await lstat(path.join(objects, 'info', 'alternates'))).isFile(); } catch { alternatesPresent = false; }
    return new ObjectStore(objects, algorithm, packs, maxObjectBytes, alternatesPresent);
  }

  async close(): Promise<void> {
    for (const h of this.handles.values()) await h.close();
    this.handles.clear();
  }

  /** The body of object `id`, which must be of `type` and hash, with its header, to `id` under the consented algorithm. */
  async verified(id: string, type: GitObjectType, at: string | null): Promise<Uint8Array> {
    const object = await this.raw(id, at);
    const actual = createHash(this.algorithm).update(`${object.type} ${object.body.length}\0`).update(object.body).digest('hex');
    if (actual !== id) refuse('identifier-mismatch', `the object read as ${id} hashes to ${actual}`, id, at);
    if (object.type !== type) refuse('type-mismatch', `${id} is a ${object.type}, not a ${type}`, id, at);
    return object.body;
  }

  private async raw(id: string, at: string | null): Promise<{ readonly type: GitObjectType; readonly body: Uint8Array }> {
    let deflated: Buffer | null = null;
    try { deflated = await readFile(path.join(this.objects, id.slice(0, 2), id.slice(2))); } catch { deflated = null; }
    if (deflated !== null) return this.loose(deflated, id, at);
    for (const pack of this.packs) {
      const offset = lookup(pack, id, this.algorithm);
      if (offset !== null) return this.packed(pack, offset, id, at, 0);
    }
    const why = this.alternatesPresent ? '; objects/info/alternates is present and is never followed' : '';
    return refuse('object-missing', `${id} is in neither a loose object nor a pack of this clone${why}`, id, at);
  }

  private loose(deflated: Buffer, id: string, at: string | null): { readonly type: GitObjectType; readonly body: Uint8Array } {
    let inflated: Buffer;
    try { inflated = inflateSync(deflated, { maxOutputLength: this.maxObjectBytes + 64 }); } catch { return refuse('corrupt-object', `loose object ${id} does not inflate`, id, at); }
    const nul = inflated.indexOf(0);
    const header = /^(commit|tree|blob|tag) (0|[1-9][0-9]*)$/.exec(nul < 0 ? '' : inflated.toString('latin1', 0, nul));
    if (header === null || Number(header[2]) !== inflated.length - nul - 1) return refuse('corrupt-object', `loose object ${id} has a malformed header`, id, at);
    return { type: header[1] as GitObjectType, body: inflated.subarray(nul + 1) };
  }

  private async packed(pack: PackIndex, offset: number, id: string, at: string | null, depth: number): Promise<{ readonly type: GitObjectType; readonly body: Uint8Array }> {
    if (depth > MAX_DELTA_CHAIN) refuse('corrupt-object', `${id} has a delta chain longer than ${MAX_DELTA_CHAIN}`, id, at);
    const fh = await this.handle(pack);
    const head = await readAt(fh, offset, 32 + HEX[this.algorithm] / 2);
    let c = head[0]!, i = 1, size = c & 0x0f, shift = 4;
    const kind = (c >> 4) & 7;
    while (c & 0x80) {
      if (i >= head.length) refuse('corrupt-object', `${id}: pack entry header too long in ${pack.name}`, id, at);
      c = head[i++]!; size += (c & 0x7f) * 2 ** shift; shift += 7;
    }
    if (size > this.maxObjectBytes) refuse('corrupt-object', `${id}: pack entry declares ${size} bytes`, id, at);
    if (kind in PACK_TYPES) return { type: PACK_TYPES[kind]!, body: await this.inflateAt(fh, offset + i, size, id, at) };
    let base: { readonly type: GitObjectType; readonly body: Uint8Array };
    if (kind === OFS_DELTA) {
      c = head[i++]!;
      let back = c & 0x7f;
      while (c & 0x80) {
        if (i >= head.length) refuse('corrupt-object', `${id}: delta offset too long in ${pack.name}`, id, at);
        c = head[i++]!; back = (back + 1) * 128 + (c & 0x7f);
      }
      if (back <= 0 || back > offset - 12) refuse('corrupt-object', `${id}: delta base offset out of range in ${pack.name}`, id, at);
      base = await this.packed(pack, offset - back, id, at, depth + 1);
    } else if (kind === REF_DELTA) {
      const width = HEX[this.algorithm] / 2, baseId = head.toString('hex', i, i + width);
      i += width;
      base = await this.rawForDelta(baseId, id, at, depth);
    } else {
      return refuse('corrupt-object', `${id}: pack entry of unknown type ${kind} in ${pack.name}`, id, at);
    }
    return { type: base.type, body: applyDelta(base.body, await this.inflateAt(fh, offset + i, size, id, at), id, at, this.maxObjectBytes) };
  }

  private async rawForDelta(baseId: string, id: string, at: string | null, depth: number): Promise<{ readonly type: GitObjectType; readonly body: Uint8Array }> {
    for (const pack of this.packs) {
      const offset = lookup(pack, baseId, this.algorithm);
      if (offset !== null) return this.packed(pack, offset, id, at, depth + 1);
    }
    let deflated: Buffer | null = null;
    try { deflated = await readFile(path.join(this.objects, baseId.slice(0, 2), baseId.slice(2))); } catch { deflated = null; }
    if (deflated !== null) return this.loose(deflated, baseId, at);
    return refuse('object-missing', `${id}: delta base ${baseId} is not in this clone`, id, at);
  }

  private async inflateAt(fh: FileHandle, start: number, size: number, id: string, at: string | null): Promise<Buffer> {
    const end = (await fh.stat()).size;
    for (let window = size + (size >> 3) + 1024; ; window *= 2) {
      const chunk = await readAt(fh, start, Math.min(window, end - start));
      try {
        const out = inflateSync(chunk, { maxOutputLength: size + 1 });
        if (out.length !== size) refuse('corrupt-object', `${id}: pack entry inflates to ${out.length} bytes, not the ${size} it declares`, id, at);
        return out;
      } catch (e) {
        if (e instanceof GitObjectReadRefusal) throw e;
        if ((e as { code?: string }).code !== 'Z_BUF_ERROR' || start + window >= end) refuse('corrupt-object', `${id}: pack entry does not inflate`, id, at);
      }
    }
  }

  private async handle(pack: PackIndex): Promise<FileHandle> {
    let fh = this.handles.get(pack.name);
    if (fh === undefined) {
      try { fh = await open(path.join(this.objects, 'pack', `${pack.name}.pack`), 'r'); } catch { return refuse('invalid-pack-index', `${pack.name}.idx has no readable pack`); }
      this.handles.set(pack.name, fh);
    }
    return fh;
  }
}

async function readAt(fh: FileHandle, offset: number, length: number): Promise<Buffer> {
  const buf = Buffer.alloc(Math.max(0, length));
  const { bytesRead } = await fh.read(buf, 0, buf.length, offset);
  return buf.subarray(0, bytesRead);
}

/** A version-2 pack index whose identifiers are as wide as the consented algorithm's; any other shape refuses (an index in
 * another hash does not fit the size equation). */
function parseIndex(idx: Buffer, name: string, algorithm: HashAlgorithm): PackIndex {
  const width = HEX[algorithm] / 2;
  const bad = (why: string): never => refuse('invalid-pack-index', `${name}.idx is not a version-2 ${algorithm} pack index: ${why}`);
  if (idx.length < 8 + 1024 || idx.readUInt32BE(0) !== 0xff744f63 || idx.readUInt32BE(4) !== 2) bad('bad header');
  const count = idx.readUInt32BE(8 + 255 * 4), idsAt = 8 + 1024, offsetsAt = idsAt + count * (width + 4), largeAt = offsetsAt + count * 4;
  if (largeAt > idx.length) bad('truncated');
  const small = Array.from({ length: count }, (_, k) => idx.readUInt32BE(offsetsAt + k * 4));
  const large = small.filter(o => o & 0x80000000).length;
  if (idx.length !== largeAt + large * 8 + 2 * width) bad(`size ${idx.length} fits no ${count}-entry index`);
  const offsets = small.map(o => (o & 0x80000000 ? Number(idx.readBigUInt64BE(largeAt + (o & 0x7fffffff) * 8)) : o));
  return { name, ids: idx.subarray(idsAt, idsAt + count * width), offsets, count };
}

function lookup(pack: PackIndex, id: string, algorithm: HashAlgorithm): number | null {
  const width = HEX[algorithm] / 2, want = Buffer.from(id, 'hex');
  let lo = 0, hi = pack.count - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1, cmp = Buffer.compare(pack.ids.subarray(mid * width, (mid + 1) * width), want);
    if (cmp === 0) return pack.offsets[mid]!;
    if (cmp < 0) lo = mid + 1; else hi = mid - 1;
  }
  return null;
}

function applyDelta(base: Uint8Array, delta: Buffer, id: string, at: string | null, maxObjectBytes: number): Buffer {
  let i = 0;
  const varint = (): number => {
    let value = 0, shift = 0, c: number;
    do {
      if (i >= delta.length) refuse('corrupt-object', `${id}: truncated delta header`, id, at);
      c = delta[i++]!; value += (c & 0x7f) * 2 ** shift; shift += 7;
    } while (c & 0x80);
    return value;
  };
  const sourceSize = varint(), targetSize = varint();
  if (sourceSize !== base.length) refuse('corrupt-object', `${id}: delta expects a ${sourceSize}-byte base, got ${base.length}`, id, at);
  if (targetSize > maxObjectBytes) refuse('corrupt-object', `${id}: delta declares ${targetSize} bytes`, id, at);
  const out = Buffer.alloc(targetSize);
  let o = 0;
  while (i < delta.length) {
    const op = delta[i++]!;
    if (op & 0x80) {
      let from = 0, n = 0;
      for (let b = 0; b < 4; b += 1) if (op & (1 << b)) from += delta[i++]! * 2 ** (8 * b);
      for (let b = 0; b < 3; b += 1) if (op & (0x10 << b)) n += delta[i++]! * 2 ** (8 * b);
      if (n === 0) n = 0x10000;
      if (i > delta.length || from + n > base.length || o + n > targetSize) refuse('corrupt-object', `${id}: delta copy out of range`, id, at);
      out.set(base.subarray(from, from + n), o); o += n;
    } else if (op !== 0) {
      if (i + op > delta.length || o + op > targetSize) refuse('corrupt-object', `${id}: delta insert out of range`, id, at);
      delta.copy(out, o, i, i + op); i += op; o += op;
    } else {
      refuse('corrupt-object', `${id}: delta opcode 0 is reserved`, id, at);
    }
  }
  if (o !== targetSize) refuse('corrupt-object', `${id}: delta yields ${o} bytes, not the ${targetSize} it declares`, id, at);
  return out;
}
