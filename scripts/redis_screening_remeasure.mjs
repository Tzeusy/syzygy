#!/usr/bin/env node
// Re-measure, screening only, what the public-source screening scope version 4 (variant `span`) changes for the cited spans of one
// retained Polaris dossier run (syzygy-skpn): the same cited spans, at the same pinned commit, through the same code path
// `syzygy dossier review-packet` uses (`buildFidelityPacket`), once under the version-3 policy bytes the run was screened under and
// once under the policy in force now. Not authority.
//
//   node scripts/redis_screening_remeasure.mjs <run directory> [--headline-revision N] > docs/evidence/redis-screening-v4-remeasure-<date>.json
//   node scripts/redis_screening_remeasure.mjs --selftest     pure predicates over synthetic fixtures
//   node scripts/redis_screening_remeasure.mjs --mutants      one source mutant per predicate; each must fail --selftest (rule 6)
//
// What it does, in order:
// 1. Calls the installed read gate, `reverifyPinnedRevision`, with the gate sources the CLI builds (`createPackageGateSources` over
//    this checkout). A refusal is written out verbatim and nothing is read. It also records `openRun`'s outcome verbatim: the run's
//    declared deadline has passed, so a dossier step would refuse; this script is no dossier step and builds no packet of record.
// 2. For each draft revision with a retained fidelity packet, builds a read-only view of the run directory (symbolic links only, no
//    byte copied) that ends at that revision, and calls `buildFidelityPacket` twice: with the version-3 screen built from the policy
//    bytes whose digest the retained packet names (found in this checkout's Git history by digest), and with the default screen
//    (`loadDossierScreen`, the act chain's policy in force now). Nothing is written to the run directory.
// 3. Checks the version-3 rebuild against the retained packet span by span (a second method for the baseline, rule 2).
// 4. For each body version 4 retains as redacted-span, reads it again through the same pinned reader and screen to name its withheld
//    line numbers, and splits each withheld span into touching a withheld line or its own text matching a detector.
// 5. Reads the retained, validated verdict bound to each retained packet (structured fields only) and sorts its non-passing rows by
//    whether the spans their subject cites are withheld under version 3 and under version 4.
// The output carries counts, paths, line numbers, identifiers and digests only: never a body, a span's text, a quotation or a reason.
// Before writing, every admitted span text of every build is searched for in the output, and any hit refuses (`bodyLeak`).
// No model, agent session or provider is called; the only Git reads are the pinned reader's, after the gate.
import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const FORMAT = 'redis-screening-v4-remeasure/1';
const SCRIPT = fileURLToPath(import.meta.url);
const ROOT = process.env.SYZYGY_REMEASURE_ROOT ?? path.resolve(path.dirname(SCRIPT), '..');
const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');

/** The files the version-4 packet's section "What stays withheld" keeps withheld by design (syzygy-skpn); counted apart, never relaxed. */
export const BY_DESIGN = Object.freeze(['SECURITY.md', 'MANIFESTO', 'TLS.md', 'redis.conf', 'modules/MODULES.md', '00-RELEASENOTES', 'LICENSE.txt']);
const WITHHELD = 'withheld';

// ---- pure predicates (each has a mutant in MUTANTS and a case in selftest) ----

/** P1. The cause bucket of one packet span. `redactionCause` is 'touches-withheld-line' or 'own-text-matches' for a redacted-span. */
export function causeOf(span, redactionCause) {
  switch (span.outcome) {
    case 'admitted': return 'admitted';
    case 'redacted-span': return redactionCause === 'touches-withheld-line' ? 'secret-redacted-span-touching-withheld-line' : 'secret-redacted-span-own-text-matches';
    case 'secret-detector-match': return 'secret-whole-file';
    case 'unknown-extraction-class': return 'unclassified';
    case 'active-content': return 'active-content';
    default: return `other:${span.outcome}`;
  }
}

/** P2. Why a redacted-span span is withheld: it includes a withheld line, or (only otherwise) its own text matched a detector. */
export function redactedCause(withheldLines, startLine, endLine) {
  return withheldLines.some((line) => line >= startLine && line <= endLine) ? 'touches-withheld-line' : 'own-text-matches';
}

/** P3. Counts by cause, split into the by-design files and the rest. */
export function tally(spans, causeFor) {
  const byCause = {}, byDesign = {}, other = {}, byPath = {};
  let withheld = 0;
  for (const span of spans) {
    const cause = causeFor(span);
    byCause[cause] = (byCause[cause] ?? 0) + 1;
    if (cause === 'admitted') continue;
    withheld++;
    const into = span.path !== null && BY_DESIGN.includes(span.path) ? byDesign : other;
    into[cause] = (into[cause] ?? 0) + 1;
    const key = span.path ?? '(path withheld)';
    byPath[key] ??= {};
    byPath[key][cause] = (byPath[key][cause] ?? 0) + 1;
  }
  return { total: spans.length, admitted: byCause['admitted'] ?? 0, withheld, byCause, byDesignFiles: byDesign, notByDesign: other, byPath };
}

/** P4. Whether two span lists agree on every field (identity, range, outcome, object, text, citations), and the first disagreement. */
export function compareSpans(a, b) {
  if (a.length !== b.length) return { equal: false, firstDifference: `length ${a.length} versus ${b.length}` };
  for (let i = 0; i < a.length; i++) {
    if (JSON.stringify(a[i]) !== JSON.stringify(b[i])) return { equal: false, firstDifference: `span index ${i} (${a[i].id} versus ${b[i].id})` };
  }
  return { equal: true, firstDifference: null };
}

/** P5. A non-passing verdict row's relation to screening, from the outcomes (v3, v4) of the spans its subject cites. */
export function rowClass(cited) {
  const v3Withheld = cited.filter((span) => span.v3 !== 'admitted');
  if (v3Withheld.length === 0) return 'cites-no-span-withheld-under-v3';
  if (cited.some((span) => span.v4 !== 'admitted')) return 'still-cites-a-span-withheld-under-v4';
  return 'every-cited-span-admitted-under-v4';
}

/** P6. The admitted span texts (12 characters or more after trimming) that occur in `output`; any hit refuses the record. */
export function bodyLeak(output, texts) {
  const hits = [];
  for (const text of texts) {
    const probe = text.trim();
    if (probe.length >= 12 && output.includes(probe)) hits.push(sha256(probe));
  }
  return hits;
}

/** P7. The first candidate whose bytes hash to `digest`, or undefined. */
export function findByDigest(candidates, digest) {
  return candidates.find((candidate) => sha256(candidate.bytes) === digest);
}

// ---- selftest and mutants ----

function selftest() {
  const failures = [];
  const check = (name, actual, expected) => {
    if (JSON.stringify(actual) !== JSON.stringify(expected)) failures.push(`${name}: got ${JSON.stringify(actual)}, expected ${JSON.stringify(expected)}`);
  };
  check('P1 admitted', causeOf({ outcome: 'admitted' }), 'admitted');
  check('P1 redacted touching', causeOf({ outcome: 'redacted-span' }, 'touches-withheld-line'), 'secret-redacted-span-touching-withheld-line');
  check('P1 redacted own text', causeOf({ outcome: 'redacted-span' }, 'own-text-matches'), 'secret-redacted-span-own-text-matches');
  check('P1 whole file', causeOf({ outcome: 'secret-detector-match' }), 'secret-whole-file');
  check('P1 unclassified', causeOf({ outcome: 'unknown-extraction-class' }), 'unclassified');
  check('P1 active', causeOf({ outcome: 'active-content' }), 'active-content');
  check('P1 other', causeOf({ outcome: 'class-not-consented' }), 'other:class-not-consented');
  check('P2 touches start', redactedCause([1, 2], 2, 5), 'touches-withheld-line');
  check('P2 touches end', redactedCause([9], 3, 9), 'touches-withheld-line');
  check('P2 misses', redactedCause([1, 2], 3, 5), 'own-text-matches');
  const spans = [
    { path: 'README.md', outcome: 'admitted' }, { path: 'README.md', outcome: 'redacted-span' }, { path: 'SECURITY.md', outcome: 'unknown-extraction-class' },
    { path: 'src/x.def', outcome: 'unknown-extraction-class' }, { path: null, outcome: 'secret-detector-match' },
  ];
  const t = tally(spans, (span) => causeOf(span, 'touches-withheld-line'));
  check('P3 totals', [t.total, t.admitted, t.withheld], [5, 1, 4]);
  check('P3 by design', t.byDesignFiles, { unclassified: 1 });
  check('P3 not by design', t.notByDesign, { 'secret-redacted-span-touching-withheld-line': 1, unclassified: 1, 'secret-whole-file': 1 });
  check('P3 by path', t.byPath['(path withheld)'], { 'secret-whole-file': 1 });
  const a = [{ id: 'span-1', outcome: 'admitted', text: 'x' }], b = [{ id: 'span-1', outcome: 'admitted', text: 'y' }];
  check('P4 equal', compareSpans(a, a).equal, true);
  check('P4 text differs', compareSpans(a, b).equal, false);
  check('P4 length differs', compareSpans(a, []).equal, false);
  check('P5 none withheld', rowClass([{ v3: 'admitted', v4: 'admitted' }]), 'cites-no-span-withheld-under-v3');
  check('P5 recovered', rowClass([{ v3: 'admitted', v4: 'admitted' }, { v3: 'secret-detector-match', v4: 'admitted' }]), 'every-cited-span-admitted-under-v4');
  check('P5 still withheld', rowClass([{ v3: 'secret-detector-match', v4: 'admitted' }, { v3: 'unknown-extraction-class', v4: 'unknown-extraction-class' }]), 'still-cites-a-span-withheld-under-v4');
  check('P5 no citation', rowClass([]), 'cites-no-span-withheld-under-v3');
  check('P6 leak found', bodyLeak('{"a":"the quick brown fox jumps"}', ['  the quick brown fox\n']).length, 1);
  check('P6 short text ignored', bodyLeak('{"a":"short"}', ['short']).length, 0);
  check('P6 clean', bodyLeak('{"a":1}', ['the quick brown fox']).length, 0);
  const bytes = Buffer.from('policy');
  check('P7 found', findByDigest([{ id: 'x', bytes: Buffer.from('other') }, { id: 'y', bytes }], sha256(bytes))?.id, 'y');
  check('P7 absent', findByDigest([{ id: 'x', bytes: Buffer.from('other') }], sha256(bytes)), undefined);
  return failures;
}

/** One source mutant per predicate: each replaces one fragment of this file; `--selftest` of the mutated copy must fail. */
export const MUTANTS = Object.freeze([
  { id: 'P1-redacted-bucket', old: "redactionCause === 'touches-withheld-line' ? 'secret-redacted-span-touching-withheld-line'", new: "redactionCause !== 'touches-withheld-line' ? 'secret-redacted-span-touching-withheld-line'" },
  { id: 'P2-range-end', old: 'line >= startLine && line <= endLine', new: 'line >= startLine && line < endLine' },
  { id: 'P3-by-design', old: 'BY_DESIGN.includes(span.path) ? byDesign : other', new: 'BY_DESIGN.includes(span.path) ? other : byDesign' },
  { id: 'P4-compare', old: 'if (JSON.stringify(a[i]) !== JSON.stringify(b[i]))', new: 'if (a[i].id !== b[i].id)' },
  { id: 'P5-every', old: "if (cited.some((span) => span.v4 !== 'admitted'))", new: "if (cited.every((span) => span.v4 !== 'admitted'))" },
  { id: 'P6-trim', old: 'const probe = text.trim();', new: 'const probe = text;' },
  { id: 'P7-digest', old: 'candidates.find((candidate) => sha256(candidate.bytes) === digest)', new: 'candidates.find((candidate) => sha256(candidate.bytes) !== digest)' },
]);

function runMutants() {
  const source = fs.readFileSync(SCRIPT, 'utf8');
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'redis-remeasure-mutants-'));
  const results = [];
  try {
    for (const mutant of MUTANTS) {
      // The fragment must occur exactly once outside this table: the table itself quotes it once.
      const occurrences = source.split(mutant.old).length - 1;
      if (occurrences !== 2) { results.push({ ...mutant, outcome: `fragment occurs ${occurrences} times, expected 2` }); continue; }
      const at = source.indexOf(mutant.old);
      const mutated = source.slice(0, at) + mutant.new + source.slice(at + mutant.old.length);
      const file = path.join(dir, `${mutant.id}.mjs`);
      fs.writeFileSync(file, mutated);
      const run = spawnSync(process.execPath, [file, '--selftest'], { encoding: 'utf8' });
      results.push({ ...mutant, outcome: run.status === 0 ? 'survived' : 'killed', exitStatus: run.status });
    }
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
  return { scriptSha256: sha256(source), mutants: results };
}

// ---- measurement ----

const dist = (rel) => import(pathToFileURL(path.join(ROOT, rel)).href);
const git = (...args) => execFileSync('git', ['-C', ROOT, ...args], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
const gitBytes = (...args) => execFileSync('git', ['-C', ROOT, ...args], { maxBuffer: 64 * 1024 * 1024 });
const readJson = (file) => JSON.parse(fs.readFileSync(file, 'utf8'));
const isObj = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);
const list = (value) => (Array.isArray(value) ? value : []);
const spanKey = (file, start, end) => JSON.stringify([file, start, end]);

/** A read-only view of `run` that ends at draft revision `revision`: symbolic links to the run's own files, no byte copied. */
function runView(run, revision, base) {
  const view = path.join(base, `rev-${revision}`, path.basename(run));
  fs.mkdirSync(view, { recursive: true });
  for (const entry of fs.readdirSync(run, { withFileTypes: true })) {
    if (entry.name === 'drafts' || entry.name === 'checks') {
      fs.mkdirSync(path.join(view, entry.name));
      for (let n = 0; n <= revision; n++) fs.symlinkSync(path.join(run, entry.name, `rev-${n}.json`), path.join(view, entry.name, `rev-${n}.json`));
    } else fs.symlinkSync(path.join(run, entry.name), path.join(view, entry.name));
  }
  return view;
}

/** The headline of one revision's measurement, every figure read from it; the readiness sentence is Inferred. */
function headlineOf(r, latest) {
  const v3 = r.rebuiltV3.spans, v4 = r.rebuiltV4.spans, verdict = r.retainedVerdict;
  const sum = (o) => Object.values(o).reduce((a, b) => a + b, 0);
  const still = verdict?.nonPassingRowsByClass['still-cites-a-span-withheld-under-v4'] ?? 0;
  const freed = verdict?.nonPassingRowsByClass['every-cited-span-admitted-under-v4'] ?? 0;
  const unrelated = verdict?.nonPassingRowsByClass['cites-no-span-withheld-under-v3'] ?? 0;
  return {
    draftRevision: r.draftRevision, latestDraftRevision: latest, label: 'Observed',
    citedSpans: v3.total,
    withheldV3: v3.withheld, withheldV3EqualsRetainedPacket: r.rebuiltV3.spansEqualRetainedPacket.equal && r.retainedPacket.spans.withheld === v3.withheld,
    withheldV4: v4.withheld,
    withheldV4ByCause: {
      secretWholeFile: v4.byCause['secret-whole-file'] ?? 0,
      secretRedactedSpanTouchingWithheldLine: v4.byCause['secret-redacted-span-touching-withheld-line'] ?? 0,
      secretRedactedSpanOwnTextMatches: v4.byCause['secret-redacted-span-own-text-matches'] ?? 0,
      unclassified: v4.byCause['unclassified'] ?? 0,
      activeContent: v4.byCause['active-content'] ?? 0,
      other: sum(Object.fromEntries(Object.entries(v4.byCause).filter(([k]) => k.startsWith('other:')))),
    },
    withheldV4InByDesignFiles: sum(v4.byDesignFiles), withheldV4OutsideByDesignFiles: sum(v4.notByDesign),
    readmeSpans: r.readme.v3.total, readmeAdmittedV3: r.readme.v3.admitted, readmeAdmittedV4: r.readme.admittedUnderV4,
    readiness: {
      label: 'Inferred',
      retainedVerdictNonPassingRows: verdict?.nonPassingRows ?? null,
      rowsStillCitingASpanWithheldUnderV4: still, rowsWhoseCitedSpansAreAllAdmittedUnderV4: freed, rowsCitingNoSpanWithheldUnderV3: unrelated,
      statement: verdict === null ? 'Unknown: no validated verdict is bound to this revision\'s retained packet'
        : `[Inferred] Readiness is not reached by the screening change alone. Of the ${verdict.nonPassingRows} non-passing rows of the retained verdict, ${still} still cite at least one span version 4 withholds (${verdict.stillWithheldRowsCitingNoByDesignFile} of them only outside the by-design files), so a fresh review over this draft would still lack bytes for them; ${freed} cite only spans version 4 now admits and could pass on a fresh review, which only a new review session can say; ${unrelated} cite no span version 3 withheld. A ready verdict needs every row passing, so it needs the draft to re-cite those claims to admitted spans, or a reviewer to judge them from admitted spans alone. The by-design files stay withheld; this record proposes no relaxation.`,
    },
  };
}

async function measure(runArg, headlineRevision) {
  const run = path.resolve(runArg);
  const runId = path.basename(run);
  const now = Date.now();
  const { createPackageGateSources, reverifyPinnedRevision, buildFidelityPacket, buildDossierScreen, loadDossierScreen, openPinnedObjectReader } = await dist('packages/polaris-dossier/dist/index.js');
  const { collectBlocks, collectCitations } = await dist('packages/polaris-dossier/dist/check.js');
  const { openRun } = await dist('packages/polaris-dossier/dist/inventory.js');
  const { POLICY_PATH, readClassActState } = await dist('packages/polaris-generation-consent/dist/index.js');
  const sources = createPackageGateSources({ root: ROOT, now: () => now });

  const syzygy = { commit: git('rev-parse', 'HEAD').trim(), treeClean: git('status', '--porcelain', '--untracked-files=no').trim() === '', scriptPath: 'scripts/redis_screening_remeasure.mjs', scriptSha256: sha256(fs.readFileSync(SCRIPT)) };
  const runRecordBytes = fs.readFileSync(path.join(run, 'run.json'));
  const runRecord = JSON.parse(runRecordBytes.toString('utf8'));
  const header = {
    format: FORMAT,
    label: 'Observed',
    measuredAt: new Date(now).toISOString(),
    syzygy,
    measuredOn: {
      runId, runRecordSha256: sha256(runRecordBytes),
      repository: runRecord.subject?.repository?.url ?? null, pinnedCommit: runRecord.subject?.pinnedRevision?.commit ?? null,
      pinnedLabel: runRecord.subject?.pinnedRevision?.label ?? null, consentRecordAtPin: runRecord.subject?.pinnedRevision?.consentRecord ?? null,
      screeningPolicyAtStart: runRecord.subject?.startGates?.screeningPolicy ?? null,
    },
  };

  // 1. The read gate.
  const gate = await reverifyPinnedRevision(run, sources, now);
  const opened = await openRun(run, sources, now, 'no step runs');
  const openRunOutcome = opened.ok ? { ok: true } : { ok: false, stage: opened.stage, reason: opened.reason, ...(opened.reasons ? { reasons: opened.reasons } : {}) };
  if (!gate.ok) return { exit: 3, record: { ...header, gate: { call: 'reverifyPinnedRevision', ok: false, reasons: gate.reasons, refusals: gate.refusals }, openRun: openRunOutcome, measured: false } };
  const subject = gate.record.subject;
  const gateRecord = { call: 'reverifyPinnedRevision', ok: true, consentRecord: gate.consentRecord, revision: gate.revision, governed: gate.governed.kind, providerStatement: gate.providerStatement, contentClasses: gate.contentClasses };

  // The screens: version 3 from the bytes the retained packets name, and the one in force now.
  const packets = fs.readdirSync(path.join(run, 'reviews')).filter((name) => /^fidelity-packet-[0-9a-f]{64}$/.test(name)).map((name) => {
    const bytes = fs.readFileSync(path.join(run, 'reviews', name, 'packet.json'));
    const doc = JSON.parse(bytes.toString('utf8'));
    return { dir: name, sha256: sha256(bytes), namedSha256: name.slice('fidelity-packet-'.length), doc };
  }).sort((x, y) => x.doc.draft.revision - y.doc.draft.revision);
  const v3Digests = [...new Set(packets.map((packet) => packet.doc.screeningPolicy.sha256))];
  if (v3Digests.length !== 1) throw new Error(`the retained packets name ${v3Digests.length} policy digests, not one`);
  const commits = git('log', '--format=%H', '--', POLICY_PATH).trim().split('\n');
  const candidates = commits.map((commit) => { try { return { commit, bytes: gitBytes('show', `${commit}:${POLICY_PATH}`) }; } catch { return { commit, bytes: Buffer.alloc(0) }; } });
  const v3Found = findByDigest(candidates, v3Digests[0]);
  if (v3Found === undefined) throw new Error('no commit of this checkout holds the policy bytes the retained packets name');
  const classAct = await readClassActState({ root: ROOT, now });
  const v3Load = buildDossierScreen(new Uint8Array(v3Found.bytes), classAct.state === 'ok');
  if (!v3Load.ok) throw new Error(`the version-3 screen does not build: ${v3Load.why}`);
  const v4Load = await loadDossierScreen(ROOT, now);
  if (!v4Load.ok) return { exit: 3, record: { ...header, gate: gateRecord, openRun: openRunOutcome, screenInForce: { ok: false, why: v4Load.why }, measured: false } };
  const v4 = v4Load.screen;
  const screens = {
    v3: { policyId: v3Load.screen.policyId, policyVersion: v3Load.screen.policyVersion, sha256: v3Load.screen.policySha256, foundAtCommit: v3Found.commit, projectDocumentationClassified: v3Load.screen.projectDocumentation, secretRedaction: v3Load.screen.secretRedaction, built: 'buildDossierScreen over those bytes, the class act state read now' },
    v4: { policyId: v4.policyId, policyVersion: v4.policyVersion, sha256: v4.policySha256, projectDocumentationClassified: v4.projectDocumentation, secretRedaction: v4.secretRedaction, built: 'loadDossierScreen: the act chain\'s policy in force now (the default review-packet path)' },
  };

  const reader = openPinnedObjectReader({ gitDir: path.join(subject.clone.path, '.git'), revision: subject.pinnedRevision.commit });
  const tree = new Map((await reader.listTree()).map((entry) => [entry.path, entry]));
  const base = fs.mkdtempSync(path.join(os.tmpdir(), 'redis-remeasure-view-'));
  const texts = [];
  const revisions = [];
  const redactedBodies = {};
  try {
    for (const retained of packets) {
      const revision = retained.doc.draft.revision;
      const view = runView(run, revision, base);
      const openedView = { run: view, runId, subject, contentClasses: gate.contentClasses };
      const builtV3 = await buildFidelityPacket(openedView, { sources, now: () => now, loadScreen: async () => v3Load });
      const builtV4 = await buildFidelityPacket(openedView, { sources, now: () => now });
      if (!builtV3.ok || !builtV4.ok) throw new Error(`draft revision ${revision}: the packet does not build (${builtV3.ok ? builtV4.reason : builtV3.reason})`);
      for (const span of [...builtV3.spans, ...builtV4.spans, ...retained.doc.spans]) if (typeof span.text === 'string') texts.push(span.text);

      // The withheld lines of each body version 4 retains as redacted-span, read again through the same reader and screen.
      const redactedPaths = [...new Set(builtV4.spans.filter((span) => span.redaction !== undefined).map((span) => span.path))];
      const withheldOf = new Map();
      if (redactedPaths.length > 0) {
        for (const blob of await reader.readBlobs(redactedPaths)) {
          const screened = v4.screenTargetBody(new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(blob.bytes), blob.path);
          if (screened.kind !== 'redacted') throw new Error(`${blob.path} screened ${screened.kind} on the second read`);
          withheldOf.set(blob.path, screened.withheld);
          redactedBodies[blob.path] = { objectId: tree.get(blob.path).id, contentSha256: screened.contentSha256, lines: screened.retainedLines.length, withheldLines: screened.withheld, detectorIds: screened.detectorIds };
        }
      }
      const v4Cause = (span) => causeOf(span, span.outcome === 'redacted-span' ? redactedCause(withheldOf.get(span.path), span.startLine, span.endLine) : undefined);
      const v3Cause = (span) => causeOf(span);
      const oracle = compareSpans(builtV3.spans, retained.doc.spans);
      const v3 = tally(builtV3.spans, v3Cause), v4t = tally(builtV4.spans, v4Cause), retainedTally = tally(retained.doc.spans, v3Cause);
      const readme = (spans, causeFor) => tally(spans.filter((span) => span.path === 'README.md'), causeFor);

      // 5. The retained verdict bound to this packet, structured fields only.
      const v3ByKey = new Map(builtV3.spans.map((span) => [spanKey(span.path, span.startLine, span.endLine), span.outcome]));
      const v4ByKey = new Map(builtV4.spans.map((span) => [spanKey(span.path, span.startLine, span.endLine), span]));
      const cited = (doc) => collectCitations(doc).flatMap(({ value }) => {
        const key = spanKey(value.path, value.startLine, value.endLine);
        return v3ByKey.has(key) ? [{ v3: v3ByKey.get(key), v4: v4ByKey.get(key).outcome, v4Cause: v4Cause(v4ByKey.get(key)), path: value.path }] : [];
      });
      const blockCites = new Map(collectBlocks(builtV4.draft.doc).map((block) => [block.value.id, cited({ citations: list(block.value.citations), evidence: list(block.value.evidence) })]));
      const entryCites = new Map(list(builtV4.inventory.doc.entries).filter(isObj).map((entry) => [entry.id, cited(entry)]));
      const verdicts = fs.readdirSync(path.join(run, 'reviews', 'checks')).filter((name) => /^fidelity-verdict-\d+\.json$/.test(name)).map((name) => ({ name, check: readJson(path.join(run, 'reviews', 'checks', name)) }))
        .filter(({ check }) => check.outcome === 'validated' && check.packet?.sha256 === retained.namedSha256).sort((x, y) => x.check.number - y.check.number);
      let verdictRecord = null;
      if (verdicts.length > 0) {
        const { check } = verdicts[verdicts.length - 1];
        const verdictBytes = fs.readFileSync(path.join(run, check.verdict.file));
        const verdict = JSON.parse(verdictBytes.toString('utf8'));
        const rows = [];
        for (const row of list(verdict.blockSupport)) if (row.verdict !== 'supported') rows.push({ kind: 'blockSupport', value: row.verdict, cites: blockCites.get(row.blockId) });
        for (const row of list(verdict.inventoryCoverage)) if (row.disposition !== 'represented' && row.disposition !== 'justified-omission') rows.push({ kind: 'inventoryCoverage', value: row.disposition, cites: entryCites.get(row.entryId) });
        for (const row of list(verdict.inventoryAccuracy)) if (row.accuracy !== 'accurate') rows.push({ kind: 'inventoryAccuracy', value: row.accuracy, cites: entryCites.get(row.entryId) });
        for (const row of list(verdict.findings)) if (row.severity === 'blocking') rows.push({ kind: 'finding', value: row.subject, cites: blockCites.get(row.target) ?? entryCites.get(row.target) });
        const sorted = {};
        const stillBy = {};
        const byClass = {};
        let stillOnlyOutsideByDesign = 0;
        for (const row of rows) {
          const cls = row.cites === undefined ? 'target-not-found' : rowClass(row.cites);
          const key = `${row.kind}:${row.value}`;
          sorted[key] ??= {};
          sorted[key][cls] = (sorted[key][cls] ?? 0) + 1;
          byClass[cls] = (byClass[cls] ?? 0) + 1;
          if (cls === 'still-cites-a-span-withheld-under-v4') {
            const still = row.cites.filter((span) => span.v4 !== 'admitted');
            const causes = new Set(still.map((span) => (BY_DESIGN.includes(span.path) ? `by-design:${span.v4Cause}` : `${span.path === 'README.md' ? 'README.md' : 'not-by-design'}:${span.v4Cause}`)));
            for (const cause of causes) stillBy[cause] = (stillBy[cause] ?? 0) + 1;
            if (still.every((span) => !BY_DESIGN.includes(span.path))) stillOnlyOutsideByDesign++;
          }
        }
        const counts = (key, field) => list(verdict[key]).reduce((acc, row) => ({ ...acc, [row[field]]: (acc[row[field]] ?? 0) + 1 }), {});
        verdictRecord = {
          verdictFile: check.verdict.file, verdictSha256: sha256(verdictBytes), recordedSha256: check.verdict.sha256, checkFile: `reviews/checks/${verdicts[verdicts.length - 1].name}`,
          readinessDeclared: verdict.readiness, label: 'Inferred', declaredBy: 'the review session',
          rows: { blockSupport: counts('blockSupport', 'verdict'), inventoryCoverage: counts('inventoryCoverage', 'disposition'), inventoryAccuracy: counts('inventoryAccuracy', 'accuracy'), findings: counts('findings', 'severity') },
          nonPassingRows: rows.length,
          nonPassingRowsByClass: byClass,
          nonPassingRowsByScreening: sorted,
          stillWithheldRowsByCause: stillBy,
          stillWithheldRowsCitingNoByDesignFile: stillOnlyOutsideByDesign,
          rowRule: 'a row is non-passing as review.ts derivedBlocking reads it (support not supported; coverage neither represented nor justified-omission; accuracy not accurate; a blocking finding, its target resolved as a block or entry id); its cited spans are its subject\'s own citations in the draft or inventory; a row counts once per cause it cites in stillWithheldRowsByCause',
        };
      }
      revisions.push({
        draftRevision: revision, inventoryRevision: builtV4.inventory.revision,
        draftSha256: builtV4.draft.sha256, inventorySha256: builtV4.inventory.sha256,
        retainedPacket: { dir: `reviews/${retained.dir}`, sha256: retained.sha256, digestMatchesName: retained.sha256 === retained.namedSha256, spans: retainedTally },
        rebuiltV3: { packetSha256: builtV3.sha256, spans: v3, spansEqualRetainedPacket: oracle },
        rebuiltV4: { packetSha256: builtV4.sha256, spans: v4t },
        readme: {
          v3: readme(builtV3.spans, v3Cause), v4: readme(builtV4.spans, v4Cause),
          admittedUnderV4: builtV4.spans.filter((span) => span.path === 'README.md' && span.outcome === 'admitted').length,
          withheldUnderV4: builtV4.spans.filter((span) => span.path === 'README.md' && span.outcome !== 'admitted').map((span) => ({ id: span.id, startLine: span.startLine, endLine: span.endLine, outcome: span.outcome })),
        },
        retainedVerdict: verdictRecord,
      });
    }
  } finally { fs.rmSync(base, { recursive: true, force: true }); }

  const record = {
    ...header,
    subject: {
      what: 'the cited spans of each draft revision of this run that has a retained fidelity packet, with the inventory of record, at the pinned commit',
      runRecordSha256: header.measuredOn.runRecordSha256, pinnedCommit: subject.pinnedRevision.commit,
      revisions: revisions.map((r) => ({ draftRevision: r.draftRevision, draftSha256: r.draftSha256, inventoryRevision: r.inventoryRevision, inventorySha256: r.inventorySha256, retainedPacketSha256: r.retainedPacket.sha256, citedSpans: r.rebuiltV4.spans.total })),
      policies: { v3Sha256: screens.v3.sha256, v4Sha256: screens.v4.sha256 },
    },
    method: [
      'screening only: no model, agent session or provider egress; no packet written, no verdict checked, nothing written to the run directory',
      'the read gate is reverifyPinnedRevision with the CLI\'s gate sources over this checkout, called before any object read; openRun\'s own outcome is recorded beside it',
      'each packet is built by buildFidelityPacket (the review-packet code path) over a symbolic-link view of the run that ends at that draft revision; v3 with loadScreen injected as buildDossierScreen over the v3 policy bytes found by digest in this checkout\'s history, v4 with the default loadDossierScreen',
      'the v3 rebuild is compared field by field with the retained packet of the same revision (spansEqualRetainedPacket), a second method for the baseline',
      'redacted-span spans are split by spanTouchesWithheld\'s reading over the withheld lines of a second read of the same blob through the same reader and screen',
      'readiness rows are the retained validated verdict bound to the retained packet, read for structured fields only',
    ],
    gate: gateRecord, openRun: openRunOutcome, screens, byDesignFiles: BY_DESIGN, redactedBodiesUnderV4: redactedBodies, revisions, measured: true,
    scriptChecks: { atCommit: syzygy.commit, selftestFailures: selftest(), rule6: runMutants() },
  };
  const chosen = revisions.find((r) => r.draftRevision === (headlineRevision ?? revisions[revisions.length - 1].draftRevision));
  if (chosen === undefined) throw new Error(`no retained packet for draft revision ${headlineRevision}`);
  record.headline = headlineOf(chosen, revisions[revisions.length - 1].draftRevision);
  const output = `${JSON.stringify(record, null, 2)}\n`;
  const leaks = bodyLeak(output, texts);
  if (leaks.length > 0) throw new Error(`the record would carry ${leaks.length} span text(s); nothing is written`);
  return { exit: 0, record };
}

const args = process.argv.slice(2);
if (args[0] === '--selftest' && args.length === 1) {
  const failures = selftest();
  for (const failure of failures) process.stderr.write(`FAIL ${failure}\n`);
  process.stdout.write(failures.length === 0 ? 'selftest: all cases pass\n' : `selftest: ${failures.length} failure(s)\n`);
  process.exit(failures.length === 0 ? 0 : 1);
} else if (args[0] === '--mutants' && args.length === 1) {
  const result = runMutants();
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  process.exit(result.mutants.every((mutant) => mutant.outcome === 'killed') ? 0 : 1);
} else if ((args.length === 1 || (args.length === 3 && args[1] === '--headline-revision' && /^(0|[1-9][0-9]*)$/.test(args[2]))) && !args[0].startsWith('--')) {
  const { exit, record } = await measure(args[0], args.length === 3 ? Number(args[2]) : undefined);
  process.stdout.write(`${JSON.stringify(record, null, 2)}\n`);
  process.exit(exit);
} else {
  process.stderr.write('usage: node scripts/redis_screening_remeasure.mjs <run directory> [--headline-revision N] | --selftest | --mutants\n');
  process.exit(2);
}
