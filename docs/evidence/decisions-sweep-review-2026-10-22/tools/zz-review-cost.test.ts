// Reviewer's scratch test (R-GP-IMPL-DECISIONS-SWEEP-1), never committed: the cost contract of decisions-sweep.test.ts, applied to a
// sweep that is not loose (the admission family's). Each swept file's text should be folded twice there: its stem spellings and its
// field-line fold. It is used only to ask whether M5 (slack eager) is distinguishable by a deterministic count.
import { afterEach, describe, expect, it, vi } from 'vitest';
import { DECISIONS_DIR, createPackageAdmissionReader, type PackageReaderFs } from './package-reader.js';

const D = DECISIONS_DIR;
function memoryFs(files: Readonly<Record<string, string>>): PackageReaderFs {
  return {
    readdir: async dir => {
      const prefix = `${dir.slice(3)}/`;
      const names = new Set(Object.keys(files).filter(f => f.startsWith(prefix)).map(f => f.slice(prefix.length).split('/')[0]!));
      if (!dir.startsWith('/r/') || names.size === 0) throw new Error('enoent');
      return [...names];
    },
    readFile: async file => { const key = file.slice(3); if (!(key in files)) throw new Error('enoent'); return files[key]!; },
  };
}
describe('reviewer scratch: the admission sweep folds each swept file twice', () => {
  const LONG = 10_000, FILES = 6;
  const prose = 'Owner notes — nothing here names an act; café minutes, kept for the record.\n'.repeat(300);
  const TREE = Object.fromEntries(Array.from({ length: FILES }, (_, i) => [`${D}/NOTES-${i}.md`, `# Notes ${i}\n\n${prose}`]));
  afterEach(() => vi.restoreAllMocks());
  it('folds each swept file\'s text at most twice in the admission sweep (not loose)', async () => {
    const normalize = vi.spyOn(String.prototype, 'normalize');
    expect(await createPackageAdmissionReader({ root: '/r', fs: memoryFs(TREE) }).read()).toEqual([]);
    const folds = normalize.mock.contexts.filter(self => String(self).length > LONG).length;
    console.log(`REVIEW-COUNT admission folds=${folds} files=${FILES}`);
    expect(folds).toBeGreaterThanOrEqual(FILES);
    expect(folds).toBeLessThanOrEqual(2 * FILES);
  });
});
