import { execFileSync } from 'node:child_process';

import { parseGitLsTree } from './git-tree.js';
import type { PocProvenance } from './model.js';

export const CODE_LANGUAGE_CLASSIFICATIONS = [
  'typescript',
  'javascript',
  'python',
  'markdown',
  'json',
  'yaml',
  'shell',
  'html',
  'css',
  'sql',
  'toml',
  'other',
] as const;

export type CodeLanguageClassification = (typeof CODE_LANGUAGE_CLASSIFICATIONS)[number];

const EXTENSION_LANGUAGE: Readonly<Record<string, CodeLanguageClassification>> = {
  '.ts': 'typescript',
  '.tsx': 'typescript',
  '.js': 'javascript',
  '.jsx': 'javascript',
  '.mjs': 'javascript',
  '.cjs': 'javascript',
  '.py': 'python',
  '.md': 'markdown',
  '.mdx': 'markdown',
  '.json': 'json',
  '.jsonl': 'json',
  '.yaml': 'yaml',
  '.yml': 'yaml',
  '.sh': 'shell',
  '.bash': 'shell',
  '.html': 'html',
  '.css': 'css',
  '.sql': 'sql',
  '.toml': 'toml',
};

function classifyLanguage(path: string): CodeLanguageClassification {
  const dot = path.lastIndexOf('.');
  const slash = path.lastIndexOf('/');
  if (dot <= slash) {
    return 'other';
  }
  const extension = path.slice(dot).toLowerCase();
  return EXTENSION_LANGUAGE[extension] ?? 'other';
}

export interface CodeStructureFileEntry {
  readonly path: string;
  readonly sizeBytes: number;
  readonly digest: string;
  readonly language: CodeLanguageClassification;
}

/**
 * POC-REQ-001 "One statement of provenance": the observation names its
 * revision once, in the shared `PocProvenance` shape the entities and
 * relationships carry, and no entry restates it. `capturedAt` is the second
 * half of the observation's identity, not a second statement of provenance.
 */
export interface CodeStructureObserved {
  readonly kind: 'observed';
  readonly provenance: PocProvenance;
  readonly capturedAt: string;
  readonly files: readonly CodeStructureFileEntry[];
}

export interface CodeStructureUnknown {
  readonly kind: 'unknown';
  readonly reason: string;
}

export type CodeStructureResult = CodeStructureObserved | CodeStructureUnknown;

export interface ObserveCodeStructureInput {
  readonly repoRoot: string;
  readonly revision: string;
  readonly capturedAt: string;
  /** The provenance record's `source`; the model passes its git provenance source. */
  readonly provenanceSource?: string;
  readonly runGit?: (repoRoot: string, args: readonly string[]) => string;
}

/** Git's output is not valid UTF-8: a path a JS string cannot carry exactly. */
class NonUtf8GitOutput extends Error {}

const STRICT_UTF8 = new TextDecoder('utf-8', { fatal: true });

function defaultRunGit(repoRoot: string, args: readonly string[]): string {
  const bytes = execFileSync('git', ['--no-optional-locks', '-C', repoRoot, ...args], {
    maxBuffer: 256 * 1024 * 1024,
    stdio: ['ignore', 'pipe', 'ignore'],
  });
  try {
    return STRICT_UTF8.decode(bytes);
  } catch {
    throw new NonUtf8GitOutput();
  }
}

const SHA1_OBJECT_ID = /^[0-9a-f]{40}$/;

/**
 * `git ls-tree` reads only tree/blob metadata for the named revision; it
 * never opens blob contents, so this observer structurally cannot leak
 * file bytes (POC-REQ-002). `-z` makes git emit each path unquoted: without
 * it git C-quotes a path holding a special or non-ASCII byte, and the quoted
 * form was recorded as the path (syzygy-bpyt.6.1). The bytes are decoded as
 * strict UTF-8, so a path that is not valid UTF-8 makes the inventory
 * Unknown instead of a replacement-character path that can collide with
 * another. A record the shared parser cannot read, or a listing that is not
 * NUL-terminated, makes the whole inventory Unknown, never a skip.
 */
export function observeCodeStructure(input: ObserveCodeStructureInput): CodeStructureResult {
  const runGit = input.runGit ?? defaultRunGit;
  let raw: string;
  try {
    raw = runGit(input.repoRoot, ['ls-tree', '-r', '-z', '-l', input.revision]);
  } catch (error) {
    if (error instanceof NonUtf8GitOutput) {
      return { kind: 'unknown', reason: 'code-structure observation produced a path that is not valid UTF-8' };
    }
    return {
      kind: 'unknown',
      reason: 'repository or revision was unreadable during code-structure observation',
    };
  }

  const malformed: CodeStructureUnknown = {
    kind: 'unknown',
    reason: 'code-structure observation produced a malformed inventory entry',
  };
  // `-z` ends every record with NUL; a listing that does not is not the format asked for.
  if (raw !== '' && !raw.endsWith('\0')) {
    return malformed;
  }
  const parsed = parseGitLsTree(raw);
  if (parsed.kind === 'malformed') {
    return malformed;
  }
  const files: CodeStructureFileEntry[] = [];
  // Submodule gitlinks (`commit`) are not files of this revision.
  for (const entry of parsed.entries.filter((candidate) => candidate.type === 'blob')) {
    // The digest names its scheme; an id of another object format would make it false.
    if (entry.sizeBytes === undefined || !SHA1_OBJECT_ID.test(entry.objectId)) {
      return malformed;
    }
    files.push({
      path: entry.path,
      sizeBytes: entry.sizeBytes,
      digest: `git-blob-sha1:${entry.objectId}`,
      language: classifyLanguage(entry.path),
    });
  }

  files.sort((a, b) => (a.path < b.path ? -1 : a.path > b.path ? 1 : 0));

  return {
    kind: 'observed',
    provenance: {
      kind: 'git-revision',
      source: input.provenanceSource ?? 'Observed repository',
      revision: input.revision,
    },
    capturedAt: input.capturedAt,
    files,
  };
}
