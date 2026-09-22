// N8 slice 1 (syzygy-u05.8) — measure how general the unmodified PWB
// extraction pipeline is, over synthetic corpora in container shapes
// Butlers does not use. This module runs `extractClass` (the literal
// grammar, unchanged) against each fixture in `fixtures/synthetic-corpora.js`
// for every one of the nine extraction classes, and reports each cell's
// outcome honestly: `extracted` with its item count, or `unknown` with the
// pipeline's own failure reason. A cell is never coerced to pass, and an
// unextracted cell is never reported as zero — it carries no count at all,
// only the reason.
//
// `repairKind` records what closing a gap would need, not whether it is
// authorized:
//   - 'profile-row': the class's own extractor never ran the corpus's
//     grammar at all, because `project-shape-extraction.ts` gates that
//     class on one literal basename or path pattern
//     (`posixBasename(path) !== 'vision.md'`, and similarly for the other
//     eight). A future container-shape profile row (N8 slice 2) could admit
//     the path without a code change; the class's own grammar would still
//     need to recognize what is actually there.
//   - 'code-path': the corpus's own target class *is* admitted by the
//     basename gate, but its line/table walker has no rule for this shape
//     (a bullet list where it expects a decimal list, a table where it
//     expects a list, prose where it expects a table). Only new parsing
//     logic closes this gap; no profile row can.
// Every other failing cell (a class whose basename happens to match a
// corpus it was not authored for, so it fails on missing content rather
// than a shape or basename question) carries its raw reason with no
// repair classification — it is not a generality finding.

import { EXTRACTION_CLASSES, type ExtractionClass } from './project-shape-manifest.js';
import { extractClass, type ClassExtraction } from './project-shape-extraction.js';
import { SYNTHETIC_CORPORA, type SyntheticCorpusFixture } from './fixtures/synthetic-corpora.js';

export type RepairKind = 'profile-row' | 'code-path';

export interface ClassCellResult {
  readonly class: ExtractionClass;
  readonly outcome: 'extracted' | 'unknown';
  // Present only when `outcome` is `extracted`; PWB-REQ-002 never yields a
  // partial item set, so count and denominator are the same number.
  readonly count?: number;
  readonly denominator?: number;
  readonly failureReason?: string;
  readonly failureDetail?: string;
  readonly repairKind?: RepairKind;
  readonly repairNote?: string;
}

export interface CorpusRow {
  readonly corpus: SyntheticCorpusFixture;
  readonly cells: readonly ClassCellResult[];
  readonly extractedCount: number;
  readonly unknownCount: number;
  readonly denominator: number;
}

function repairFor(cls: ExtractionClass, corpus: SyntheticCorpusFixture, extraction: Extract<ClassExtraction, { kind: 'failed' }>): { readonly kind: RepairKind; readonly note: string } | undefined {
  if (extraction.failure.reason === 'unsupported-source') {
    return {
      kind: 'profile-row',
      note: `"${cls}" admission is keyed to a literal basename or path pattern in project-shape-extraction.ts, not any shape signal in this corpus; a container-shape profile row could admit the path, but "${cls}"'s own grammar would still need to recognize what is there.`,
    };
  }
  if (cls === corpus.targetClass) {
    return {
      kind: 'code-path',
      note: `the basename admits this source under "${cls}", but its line/table walker has no rule for the "${corpus.shape}" shape; only new parsing logic closes this, not a profile row.`,
    };
  }
  return undefined;
}

export function runSyntheticCorpusCoverage(corpus: SyntheticCorpusFixture): CorpusRow {
  const cells: ClassCellResult[] = EXTRACTION_CLASSES.map((cls) => {
    const extraction = extractClass(cls, corpus.path, corpus.text);
    if (extraction.kind === 'items') {
      return { class: cls, outcome: 'extracted', count: extraction.items.length, denominator: extraction.items.length };
    }
    const repair = repairFor(cls, corpus, extraction);
    return {
      class: cls,
      outcome: 'unknown',
      failureReason: extraction.failure.reason,
      ...(extraction.failure.detail === undefined ? {} : { failureDetail: extraction.failure.detail }),
      ...(repair === undefined ? {} : { repairKind: repair.kind, repairNote: repair.note }),
    };
  });
  const extractedCount = cells.filter((cell) => cell.outcome === 'extracted').length;
  return { corpus, cells, extractedCount, unknownCount: cells.length - extractedCount, denominator: cells.length };
}

export function runAllSyntheticCorpusCoverage(corpora: readonly SyntheticCorpusFixture[] = SYNTHETIC_CORPORA): readonly CorpusRow[] {
  return corpora.map(runSyntheticCorpusCoverage);
}
