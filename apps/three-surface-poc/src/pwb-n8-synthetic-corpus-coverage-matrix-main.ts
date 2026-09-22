// N8 slice 1 (syzygy-u05.8) — "Measure generality" evidence generator.
//
// Runs the unmodified PWB extraction pipeline in-process against three
// synthetic corpora (packages/three-surface-poc-core/src/fixtures/
// synthetic-corpora.ts) and writes the resulting per-class coverage matrix
// to docs/evidence/. Zero egress: every corpus is a literal string constant
// already compiled into @syzygy/three-surface-poc-core; this script opens
// no network connection, reads no real repository, and requests no new
// consent. It does not modify the pipeline to make any fixture pass —
// an unextracted cell is retained honestly as Unknown, never coerced to
// zero or to a pass.
//
//   npm run poc:pwb-n8-coverage-matrix   # writes docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-<date>.json

import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { EXTRACTION_CLASSES, SYNTHETIC_CORPORA, runAllSyntheticCorpusCoverage, type CorpusRow } from '@syzygy/three-surface-poc-core';

// dist/pwb-n8-synthetic-corpus-coverage-matrix-main.js -> apps/three-surface-poc/dist -> apps/three-surface-poc -> apps -> repo root
const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));

function parseArgs(argv: readonly string[]): { readonly date: string } {
  let date = new Date().toISOString().slice(0, 10);
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] === '--date' && argv[index + 1] !== undefined) {
      date = argv[index + 1] as string;
      index += 1;
    }
  }
  return { date };
}

interface RecordedCell {
  readonly class: string;
  readonly outcome: 'extracted' | 'unknown';
  readonly count?: number;
  readonly denominator?: number;
  readonly failureReason?: string;
  readonly failureDetail?: string;
  readonly repairKind?: 'profile-row' | 'code-path';
  readonly repairNote?: string;
}

interface RecordedCorpus {
  readonly id: string;
  readonly description: string;
  readonly shape: string;
  readonly targetClass: string;
  readonly path: string;
  readonly text: string;
  readonly denominator: number;
  readonly extractedCount: number;
  readonly unknownCount: number;
  readonly cells: readonly RecordedCell[];
}

function recordCorpus(row: CorpusRow): RecordedCorpus {
  return {
    id: row.corpus.id,
    description: row.corpus.description,
    shape: row.corpus.shape,
    targetClass: row.corpus.targetClass,
    path: row.corpus.path,
    text: row.corpus.text,
    denominator: row.denominator,
    extractedCount: row.extractedCount,
    unknownCount: row.unknownCount,
    cells: row.cells.map((cell) => ({
      class: cell.class,
      outcome: cell.outcome,
      ...(cell.count === undefined ? {} : { count: cell.count }),
      ...(cell.denominator === undefined ? {} : { denominator: cell.denominator }),
      ...(cell.failureReason === undefined ? {} : { failureReason: cell.failureReason }),
      ...(cell.failureDetail === undefined ? {} : { failureDetail: cell.failureDetail }),
      ...(cell.repairKind === undefined ? {} : { repairKind: cell.repairKind }),
      ...(cell.repairNote === undefined ? {} : { repairNote: cell.repairNote }),
    })),
  };
}

function main(): void {
  const { date } = parseArgs(process.argv.slice(2));
  const rows = runAllSyntheticCorpusCoverage();

  const allCells = rows.flatMap((row) => row.cells);
  const totalCells = allCells.length;
  const totalExtracted = allCells.filter((cell) => cell.outcome === 'extracted').length;
  const repairKindCounts = {
    'profile-row': allCells.filter((cell) => cell.repairKind === 'profile-row').length,
    'code-path': allCells.filter((cell) => cell.repairKind === 'code-path').length,
    unclassified: allCells.filter((cell) => cell.outcome === 'unknown' && cell.repairKind === undefined).length,
  };

  const record = {
    subject: 'N8 slice 2 (syzygy-u05.8) — repairFor narrowing re-run of the synthetic second-project corpus coverage matrix',
    bead: 'syzygy-u05.8',
    releasedBy: 'syzygy-dca (owner gate, closed)',
    dossier: 'docs/pursuits/2026-09-22-vision-pursuit.md §N8',
    predecessor: 'docs/evidence/pwb-n8-synthetic-corpus-coverage-matrix-2026-09-23.json (N8 slice 1, PR #63)',
    generatedAt: new Date().toISOString(),
    generator: 'apps/three-surface-poc/src/pwb-n8-synthetic-corpus-coverage-matrix-main.ts',
    method:
      'In-process run of the unmodified extractClass literal grammar (packages/three-surface-poc-core/src/project-shape-extraction.ts) against the same three synthetic corpora compiled into the package as fixtures. Zero egress: no network call, no real repository read, no new consent. The pipeline was not changed to make any fixture pass; an unextracted cell is retained as Unknown with its own failure reason, never coerced to zero.',
    slice2Change:
      "Only packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts's repairFor classifier changed (per the confirmed slice-1 review's advisory): a target-class failure is labeled repairKind:'code-path' only when its failure reason is 'malformed-list' or 'malformed-row' (a genuine shape mismatch), never for 'missing-heading', 'ambiguous-leading-label', or any other reason on that class, which are fixture-authoring defects rather than pipeline-generality findings. project-shape-extraction.ts and project-shape-manifest.ts (the actual grammar and admission gates) are unchanged.",
    slice2Result:
      "[Observed] This re-run's 27-cell matrix is unchanged from slice 1's, cell for cell: all three real corpora's own target-class failures were already 'malformed-list'/'malformed-row', which the narrowing still classifies 'code-path', so the narrowing is a defensive correctness fix with no visible movement in this matrix. It is validated instead by two new ad hoc test fixtures in synthetic-corpus-coverage.test.ts (never added to SYNTHETIC_CORPORA) that trigger 'missing-heading' and 'ambiguous-leading-label' on the 'principle' target class and assert repairKind is undefined, which the pre-narrowing classifier would have labeled 'code-path'.",
    slice2GovernanceStop:
      "[Observed] The slice's other half, 'container-shape rows' (admitting a new container shape via a profile row), was investigated and not built: project-shape-extraction.ts's per-class basename/heading/shape gates (e.g. principle -> vision.md, H2 'Non-Negotiable Rules', top-level decimal list) are the literal PWB-REQ-002 \"Reader definitions\" text in openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md, and the admission basenames are proven byte-equal to the act-bound registry/policy JSON in project-shape-manifest.test.ts. Admitting a new container shape is therefore a governed-plane change needing a PWB-REQ-002 spec amendment (CC-REV-2) plus a registry/policy amendment act, not an implementation-plane change; it stays undone here.",
    classes: EXTRACTION_CLASSES,
    denominator: {
      corpora: SYNTHETIC_CORPORA.length,
      classesPerCorpus: EXTRACTION_CLASSES.length,
      totalCells,
    },
    summary: {
      totalCells,
      extractedCells: totalExtracted,
      unknownCells: totalCells - totalExtracted,
      repairKindCounts,
    },
    corpora: rows.map(recordCorpus),
  };

  const outPath = join(REPO_ROOT, 'docs', 'evidence', `pwb-n8-synthetic-corpus-coverage-matrix-${date}.json`);
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, `${JSON.stringify(record, null, 2)}\n`, 'utf8');

  process.stdout.write(`pwb-n8-synthetic-corpus-coverage-matrix: wrote ${outPath}\n`);
  process.stdout.write(`  ${totalExtracted}/${totalCells} cells extracted across ${SYNTHETIC_CORPORA.length} corpora x ${EXTRACTION_CLASSES.length} classes\n`);
  for (const row of rows) {
    process.stdout.write(`  ${row.corpus.id}: ${row.extractedCount}/${row.denominator} classes extracted (target class "${row.corpus.targetClass}")\n`);
  }
  process.stdout.write(`  repair kinds over unknown cells: profile-row=${repairKindCounts['profile-row']}, code-path=${repairKindCounts['code-path']}, unclassified=${repairKindCounts.unclassified}\n`);
}

main();
