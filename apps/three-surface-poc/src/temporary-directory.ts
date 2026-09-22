import { rmSync } from 'node:fs';

export interface TemporaryDirectoryCleanupOptions {
  /** Total remove calls, including the first attempt. */
  readonly maxAttempts?: number;
  readonly remove?: (path: string) => void;
}

const RETRYABLE_CODES = new Set(['EBUSY', 'EMFILE', 'ENFILE', 'ENOTEMPTY']);

/** Remove a temporary directory with a small, bounded retry window. Child
 * processes can briefly retain a directory entry after they exit; retrying
 * only those transient filesystem errors keeps that race from masking the
 * operation that created the directory without hiding permanent failures. */
export function removeTemporaryDirectory(
  path: string,
  options: TemporaryDirectoryCleanupOptions = {},
): void {
  const maxAttempts = options.maxAttempts ?? 4;
  if (!Number.isInteger(maxAttempts) || maxAttempts < 1) {
    throw new RangeError(`maxAttempts must be a positive integer; received ${maxAttempts}`);
  }
  const remove = options.remove ?? (() => rmSync(path, {
    recursive: true,
    force: true,
    maxRetries: 1,
    retryDelay: 25,
  }));
  let attempts = 0;
  while (attempts < maxAttempts) {
    attempts += 1;
    try {
      remove(path);
      return;
    } catch (cause: unknown) {
      const code = cause !== null && typeof cause === 'object' && 'code' in cause
        ? String((cause as { code?: unknown }).code)
        : '';
      if (!RETRYABLE_CODES.has(code) || attempts >= maxAttempts) throw cause;
    }
  }
}
