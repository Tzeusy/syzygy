import { rmSync } from 'node:fs';

export interface CleanupRemoveOptions {
  readonly maxAttempts?: number;
  readonly remove?: (path: string) => void;
}

const RETRYABLE_CODES = new Set(['EBUSY', 'EMFILE', 'ENFILE', 'ENOTEMPTY']);

/** Remove a temporary fixture with a small, bounded retry window. CI can
 * briefly observe ENOTEMPTY while a child Git process releases its last
 * directory entry; an unbounded retry would hide a real cleanup failure. */
export function removeFixtureDirectory(path: string, options: CleanupRemoveOptions = {}): void {
  const maxAttempts = options.maxAttempts ?? 4;
  const remove = options.remove ?? (() => rmSync(path, { recursive: true, force: true, maxRetries: 1, retryDelay: 25 }));
  let attempts = 0;
  while (true) {
    try {
      remove(path);
      return;
    } catch (cause: unknown) {
      const code = cause !== null && typeof cause === 'object' && 'code' in cause ? String((cause as { code?: unknown }).code) : '';
      if (!RETRYABLE_CODES.has(code) || attempts >= maxAttempts) throw cause;
      attempts += 1;
    }
  }
}

