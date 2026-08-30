import { execFileSync } from 'node:child_process';

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
  readonly revision: string;
}

export interface CodeStructureObserved {
  readonly kind: 'observed';
  readonly revision: string;
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
  readonly runGit?: (repoRoot: string, args: readonly string[]) => string;
}

function defaultRunGit(repoRoot: string, args: readonly string[]): string {
  return execFileSync('git', ['--no-optional-locks', '-C', repoRoot, ...args], {
    encoding: 'utf8',
    maxBuffer: 256 * 1024 * 1024,
    stdio: ['ignore', 'pipe', 'ignore'],
  });
}

const LS_TREE_LINE = /^([0-7]{6}) (blob|tree|commit) ([0-9a-f]{40})\s+(\d+|-)\t(.+)$/;

/**
 * `git ls-tree` reads only tree/blob metadata for the named revision; it
 * never opens blob contents, so this observer structurally cannot leak
 * file bytes (POC-REQ-002).
 */
export function observeCodeStructure(input: ObserveCodeStructureInput): CodeStructureResult {
  const runGit = input.runGit ?? defaultRunGit;
  let raw: string;
  try {
    raw = runGit(input.repoRoot, ['ls-tree', '-r', '-l', input.revision]);
  } catch {
    return {
      kind: 'unknown',
      reason: 'repository or revision was unreadable during code-structure observation',
    };
  }

  const files: CodeStructureFileEntry[] = [];
  for (const line of raw.split('\n')) {
    if (line.trim() === '') {
      continue;
    }
    const match = LS_TREE_LINE.exec(line);
    if (match === null || match[2] !== 'blob') {
      continue;
    }
    const sizeText = match[4] ?? '-';
    const path = match[5] ?? '';
    if (sizeText === '-' || path === '') {
      return {
        kind: 'unknown',
        reason: 'code-structure observation produced a malformed inventory entry',
      };
    }
    files.push({
      path,
      sizeBytes: Number(sizeText),
      digest: `git-blob-sha1:${match[3]}`,
      language: classifyLanguage(path),
      revision: input.revision,
    });
  }

  files.sort((a, b) => (a.path < b.path ? -1 : a.path > b.path ? 1 : 0));

  return {
    kind: 'observed',
    revision: input.revision,
    capturedAt: input.capturedAt,
    files,
  };
}
