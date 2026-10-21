// THROWAWAY (untracked): same recorder for '@syzygy/cap1-core/testing'.
import { appendFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { vi } from 'vitest';

const OUT = process.env['DIFF_OUT'] ?? '';

vi.mock('@syzygy/cap1-core/testing', async (importOriginal) => {
  const actual = (await importOriginal()) as Record<string, unknown>;
  const wrapped: Record<string, unknown> = {};
  for (const [name, value] of Object.entries(actual)) {
    if (typeof value === 'function' && /^[a-z]/.test(name)) {
      const fn = (...args: unknown[]) => {
        const text = JSON.stringify(args, (_key, v) => (typeof v === 'function' ? '[fn]' : v));
        appendFileSync(OUT, `${name} ${createHash('sha256').update(text).digest('hex')}\n`);
        return (value as (...a: unknown[]) => unknown)(...args);
      };
      Object.defineProperty(fn, 'length', { value: (value as { length: number }).length });
      wrapped[name] = fn;
    } else {
      wrapped[name] = value;
    }
  }
  return wrapped;
});
