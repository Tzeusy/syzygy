/** Whether the subject is governed (REQ-polaris-generation-033, SEC-2), decided from the admitted project input and Syzygy's own path
 * listing of the tree at the pinned revision.
 *
 * Governed when any one holds: the project input records a kernel evidence drawer; or the listing holds an `openspec/**`
 * specification, a capability declaration or declared topology. A path listing cannot tell whether a declaration is adopted, so every
 * path under a `.syzygy/` tree counts, adopted or not (R3-F9: "the scenario wording 'an adopted capability declaration' is not the
 * test"). This reading counts a path segment `openspec` or `.syzygy` at any depth and in any letter case, which is never less strict
 * than a root-only, exact-case match. Non-governed only when the project input states that no drawer exists and no such path is
 * listed. When the project input does not state it, the subject is `unstated` and needs the per-project statement as a governed one
 * does. */

/** What the admitted project input (REQ-polaris-generation-001) states about a kernel evidence drawer for the subject. */
export type DrawerStatement =
  | { readonly stated: true; readonly drawer: 'present' | 'absent'; readonly record: string }
  | { readonly stated: false; readonly why: string };

export type GovernedKind = 'governed' | 'non-governed' | 'unstated';

export interface GovernedDecision {
  readonly kind: GovernedKind;
  /** Whether the per-project provider statement is required before a brief. */
  readonly statementRequired: boolean;
  readonly drawer: DrawerStatement;
  readonly governingPaths: { readonly openspec: number; readonly syzygy: number; readonly firstPaths: readonly string[] };
  readonly because: readonly string[];
}

const FIRST_PATHS = 5;

export function governedSubject(drawer: DrawerStatement, paths: readonly string[]): GovernedDecision {
  const segmentsOf = (p: string): readonly string[] => p.toLowerCase().split('/');
  const openspec = paths.filter(p => segmentsOf(p).includes('openspec'));
  const syzygy = paths.filter(p => segmentsOf(p).includes('.syzygy'));
  const governing = [...new Set([...openspec, ...syzygy])];
  const because: string[] = [];
  if (drawer.stated && drawer.drawer === 'present') because.push(`the project input ${drawer.record} records a kernel evidence drawer`);
  if (openspec.length > 0) because.push(`the pinned tree lists ${openspec.length} path(s) under an openspec/ directory`);
  if (syzygy.length > 0) because.push(`the pinned tree lists ${syzygy.length} path(s) under a .syzygy/ directory, counted adopted or not`);
  const governed = because.length > 0;
  let kind: GovernedKind;
  if (governed) kind = 'governed';
  else if (drawer.stated) {
    kind = 'non-governed';
    because.push(`the project input ${drawer.record} states that no kernel evidence drawer exists, and the pinned tree lists no openspec/ or .syzygy/ path`);
  } else {
    kind = 'unstated';
    because.push(`the project input does not state whether a kernel evidence drawer exists (${drawer.why})`);
  }
  return {
    kind,
    statementRequired: kind !== 'non-governed',
    drawer,
    governingPaths: { openspec: openspec.length, syzygy: syzygy.length, firstPaths: governing.slice(0, FIRST_PATHS) },
    because,
  };
}
