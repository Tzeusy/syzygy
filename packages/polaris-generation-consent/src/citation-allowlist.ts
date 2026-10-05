/** Decisions files, by path under the decisions directory and the sha256 of their exact bytes, whose exact tooling citations the
 * withdrawal sweeps set aside (`sweepText` in `package-reader.ts`). Every other decisions file is swept whole: a stem counts anywhere,
 * inside a script name or a package path too. Each entry is reviewed with its bytes, and its reason says what the file cites and why
 * it is no withdrawal. Change one byte of the file and the entry stops matching: when `real-tree.test.ts` then refuses, reword the
 * file or add a reviewed entry for the new bytes; never widen a filter. Seeded empty: no file on main refused when this landed. */
export const CITATION_ALLOWLIST: ReadonlyMap<string, { readonly sha256: string; readonly reason: string }> = new Map([]);
