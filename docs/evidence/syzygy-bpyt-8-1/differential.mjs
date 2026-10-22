// syzygy-bpyt.8.1 (GP-Q0 extras): old-versus-new differential of what the bead's changes could alter, with altered prose.
// Usage: node differential.mjs <old tree> <new tree>   (both built with `tsc -b`; prints JSON)
//   localRender     old renderDossier({ local, sources, topics? }) vs new renderLocalDossier(...), operator-agent fixtures
//   providerRender  old vs new renderDossier({ result, ... }) over complete, stopped, quote-finding and altered-prose runs
//   brief           old vs new renderBrief over brief inputs with altered prose, and the guidance constants
//   validators      old vs new validators (package root) over valid and broken records
//   compiledModules old vs new dist JavaScript of every changed module whose change is to imports or types only
// Fixtures come from the new tree's synthetic pipeline (fixture text only; no repository is read).
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [OLD, NEW] = process.argv.slice(2).map((tree) => path.resolve(tree));
const load = (tree, file) => import(pathToFileURL(path.join(tree, file)).href);
const commit = (tree) => execFileSync('git', ['-C', tree, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
const sha = (text) => createHash('sha256').update(text, 'utf8').digest('hex');
const APP = 'apps/three-surface-poc/dist/polaris-generation';
const DOSSIER = 'packages/polaris-dossier/dist';
const CORE = 'packages/polaris-generation-core/dist';

const oldRender = await load(OLD, `${APP}/dossier-render.js`);
const newRender = await load(NEW, `${APP}/dossier-render.js`);
const newSite = await load(NEW, `${APP}/dossier-site.js`);
const { runSyntheticProject, syntheticProjects } = await load(NEW, `${APP}/pipeline-demo.js`);

/** A render's outcome as one comparable string: every file in order, or the refusal. */
const outcome = (render) => {
  try { return JSON.stringify([...render().files].sort(([a], [b]) => (a < b ? -1 : 1))); } catch (error) { return `refused: ${error.message}`; }
};
function compare(cases, renderOld, renderNew) {
  const rows = cases.map(([name, input]) => {
    const before = outcome(() => renderOld(input)), after = outcome(() => renderNew(input));
    return { name, identical: before === after, refused: before.startsWith('refused: ') ? before : null, outputSha256: sha(after) };
  });
  return { fixtures: rows.length, identical: rows.filter((row) => row.identical).length, distinctOutputs: new Set(rows.map((row) => row.outputSha256)).size, rows };
}

// --- prose alteration: every text a draft carries, rewritten with markup, entities and both quote kinds
const alter = (text) => `${[...text].reverse().join('')} <b>&amp; "x" 'y'</b>`;
function alteredDraft(draft) {
  const walk = (value, key) => {
    if (typeof value === 'string') return ['text', 'title', 'label', 'relationship', 'reason'].includes(key) ? alter(value) : value;
    if (Array.isArray(value)) return value.map((item) => walk(item, key));
    if (value === null || typeof value !== 'object') return value;
    return Object.fromEntries(Object.entries(value).map(([k, v]) => [k, walk(v, k)]));
  };
  return walk(structuredClone(draft), '');
}

// --- fixture runs
const runs = [];
for (const project of syntheticProjects) {
  runs.push({ name: `${project.id}/complete`, run: await runSyntheticProject(project) });
  for (const budget of [{ maxCalls: 1 }, { maxCalls: 2 }, { maxCalls: 4 }, { maxUsageUnits: 7 }]) runs.push({ name: `${project.id}/stopped-${JSON.stringify(budget)}`, run: await runSyntheticProject(project, budget) });
}
const complete = runs.filter(({ name }) => name.endsWith('/complete'));

// --- operator-agent inputs, built from each complete run's checked draft
const paragraphs = (draft) => [draft.introduction, ...draft.sections.flatMap((s) => s.paragraphs.flatMap((b) => [b, ...b.children])),
  ...draft.deepDives.flatMap((d) => d.paragraphs.flatMap((b) => [b, ...b.children]))];
const anchorOf = (source, fragment = null) => ({ targetClass: 'evidence-artifact-identifier-with-integrity-digest', identifier: source.objectId,
  algorithm: 'sha1', fragment, targetState: source.revision, pathLabel: source.path });
function localInput(run, { prose = (t) => t, draftLayer = 'editorial', markings = ['inferred'], withPages = false, missingBlock = false } = {}) {
  const draft = prose === alter ? alteredDraft(run.result.draft) : structuredClone(run.result.draft);
  const quotable = run.sources.filter((s) => !s.exclusion.excluded && s.classificationBasis === 'body' && s.spans.length > 0);
  const first = quotable[0];
  const blocks = new Map(paragraphs(draft).map((p, i) => {
    const marking = markings[i % markings.length];
    const quote = first.spans[0].text.slice(0, 24);
    return [p.id, { marking, unknownReason: marking === 'unknown' ? 'no-evidence' : null, basis: prose('the fixture labels it'),
      executions: i % 3 === 0 ? [{ id: `exec/${i}`, command: prose('npm test') }] : [],
      segments: [{ kind: 'prose', text: p.text }, { kind: 'quotation', sourceId: first.sourceId, start: 0, end: Buffer.byteLength(quote), text: quote, anchor: anchorOf(first, { start: 0, end: Buffer.byteLength(quote) }) },
        ...(i % 4 === 1 ? [{ kind: 'withheld', reason: 'excluded-content' }] : [])] }];
  }));
  if (missingBlock) blocks.delete(draft.introduction.id);
  const item = (id, n) => ({ id, marking: n % 2 ? 'unknown' : 'inferred', unknownReason: n % 2 ? 'no-evidence' : null, title: prose(`Item ${n}`), text: prose(`What item ${n} records.`), details: [prose(`detail ${n}`)], sourceIds: [first.sourceId] });
  return {
    sources: run.sources,
    local: {
      draft, withheldTitle: prose('Dossier of the fixture at abc123'),
      draftLayer: draftLayer === 'editorial'
        ? { state: 'editorial-draft', ruling: 'RULING@1', inferenceProvenance: { modelIdentity: prose('fixture-model'), modelVersion: null, declaredBy: 'operator', label: 'Inferred' } }
        : { state: 'unknown', reason: 'unconsented-source-or-provider', why: [prose('no ruling is in force')] },
      blocks,
      glossary: [item('glossary/term-a', 0), item('glossary/term-b', 1)],
      disclosure: [{ id: 'disclosure/a', text: prose('Syzygy read the pinned revision.'), label: 'Observed' }, { id: 'disclosure/b', text: prose('A plain statement.'), label: null }],
      sourceAnchors: new Map(quotable.map((s) => [s.sourceId, anchorOf(s)])),
      pages: withPages ? [{ path: 'understanding.html', title: prose('Understanding'), intro: prose('What the agent understood.'),
        groups: [{ id: 'understanding', heading: prose('Items'), note: prose('Each item is Inferred.'), items: [item('understanding/1', 0), item('understanding/2', 1)], empty: prose('No items.') },
          { id: 'empty', heading: prose('Empty'), note: prose('None.'), items: [], empty: prose('Nothing here.') }] }] : [],
      reviewStatus: [{ id: 'review-status/design', text: prose('Rendered-design review: not run.'), label: 'Unknown' }],
    },
  };
}
const localCases = [];
for (const { name, run } of complete) {
  localCases.push([`${name}/as-is`, localInput(run)]);
  localCases.push([`${name}/altered-prose`, localInput(run, { prose: alter })]);
  localCases.push([`${name}/altered-prose+pages`, localInput(run, { prose: alter, withPages: true })]);
  localCases.push([`${name}/mixed-markings`, localInput(run, { markings: ['inferred', 'unknown', 'non-normative', 'observed'] })]);
  localCases.push([`${name}/draft-layer-unknown`, localInput(run, { draftLayer: 'unknown', withPages: true })]);
  localCases.push([`${name}/altered-prose+draft-layer-unknown`, localInput(run, { prose: alter, draftLayer: 'unknown' })]);
  const topics = { how: ['mechanisms'], judgment: ['trade-offs'], 'component-depth': ['mechanisms'] };
  localCases.push([`${name}/topics`, { ...localInput(run), topics }]);
  localCases.push([`${name}/refused-missing-block`, localInput(run, { missingBlock: true })]);
}

// --- provider inputs
const providerCases = [];
for (const { name, run } of runs) {
  providerCases.push([name, { result: run.result, sources: run.sources, requestedAssets: run.requestedAssets }]);
  if (run.result.status === 'awaiting-rendered-review') {
    providerCases.push([`${name}/altered-prose`, { result: { ...run.result, draft: alteredDraft(run.result.draft) }, sources: run.sources }]);
    const blockId = run.result.draft.sections[0].paragraphs[0].id;
    providerCases.push([`${name}/pipeline-quote-finding`, { result: { ...run.result, quoteFindings: [{ blockId, kind: 'not-in-cited-source' }] }, sources: run.sources }]);
    providerCases.push([`${name}/quote-findings-not-an-array`, { result: { ...run.result, quoteFindings: undefined }, sources: run.sources }]);
  } else {
    providerCases.push([`${name}/no-requested-assets`, { result: run.result, sources: run.sources }]);
  }
}
providerCases.push(['neither-result-nor-local', { sources: complete[0].run.sources }]);
providerCases.push(['both-result-and-local', { result: complete[0].run.result, ...localInput(complete[0].run) }]);

// --- brief
const brief = async (tree) => ({ brief: await load(tree, `${DOSSIER}/brief.js`), config: await load(tree, `${DOSSIER}/run-config.js`),
  rule: await load(tree, `${DOSSIER}/execution-rule.js`), doctrine: await load(tree, `${DOSSIER}/doctrine-quote.js`), record: await load(tree, `${DOSSIER}/run-record.js`) });
const oldBrief = await brief(OLD), newBrief = await brief(NEW);
const NOW = Date.UTC(2026, 9, 7, 12, 0, 0);
const REV = '498ecd0d6d007db11ddb3aea9428552598a78622';
async function briefInputs(m) {
  const sec3 = m.doctrine.readSec3(NEW);
  if (!sec3.ok) throw new Error(sec3.reason);
  const rule = await m.rule.decideExecutionRule({ role: 'authoring', runDir: '/r', runId: `run-${'a'.repeat(32)}`, pinnedRevision: REV, operatorIsOwner: true, sec3: sec3.sec3, now: NOW,
    d9: async () => ({ state: 'ok', record: 'FIXTURE-ACT' }), launched: () => 'absent', permitting: { enabled: false } });
  const config = (over) => {
    const parsed = m.config.parseRunConfig(JSON.stringify({ operator: 'Fixture Operator', agentTool: 'claude-code', agentToolVersion: '2.1.0', agentProvider: 'anthropic', model: 'fixture-model',
      deadline: 'PT1H', agentTokenBudget: 100_000, maxRepairCycles: 3, maxQuestions: 2, audience: 'an operator', operatorIsOwner: true, ...over }));
    if (!parsed.ok) throw new Error(`fixture configuration refused: ${JSON.stringify(parsed)}`);
    return parsed.config;
  };
  const subject = (url, label) => ({
    repository: { url, repositoryId: 'fixture-repo' }, clone: { path: '/srv/clones/fixture', declaredBy: 'operator', label: 'Inferred', use: 'read' },
    pinnedRevision: { commit: REV, label, consentRecord: 'FIXTURE-CONSENT@1', pinnedAt: '2026-10-07T10:00:00.000Z' },
    startGates: { registryEntry: 'REGISTRY-ACT-FIXTURE', screeningPolicy: 'POLICY-ACT-FIXTURE' },
    governed: { kind: 'non-governed', because: ['the fixture states that no kernel evidence drawer exists'] }, providerStatement: null,
    workItem: { identity: null, reason: m.record.NO_WORK_ITEM_REASON },
  });
  const base = { runId: `run-${'a'.repeat(32)}`, issuedAt: NOW, schemaSha256: '0'.repeat(64), executionRule: rule };
  return [
    ['as-is', { ...base, subject: subject('https://example.org/fixture/repo', 'v1'), declared: config({}), revisionLabel: '1.0.0' }],
    ['altered-prose', { ...base, subject: subject('https://example.org/<b>&"x"/repo', '<v2> & "q"'), declared: config({ operator: 'O <b>&amp; "x"', audience: 'a <i>reader</i> & \'friend\'' }), revisionLabel: '<label> & "two"' }],
    ['no-revision-label', { ...base, subject: subject('https://example.org/fixture/repo', 'v1'), declared: config({ agentTokenBudget: 5_000, maxQuestions: 0, maxRepairCycles: 0 }), revisionLabel: null }],
  ];
}
const briefRows = [];
for (const [name, input] of await briefInputs(newBrief)) {
  const before = oldBrief.brief.renderBrief(input), after = newBrief.brief.renderBrief(input);
  briefRows.push({ name, identical: before === after, outputSha256: sha(after), carriesGuidance: after.includes(newBrief.brief.DOSSIER_GUIDANCE) });
}

// --- validators
const oldCore = await load(OLD, `${CORE}/index.js`), newCore = await load(NEW, `${CORE}/index.js`), newLive = await load(NEW, `${CORE}/live.js`);
const verdict = (fn) => { try { return `ok: ${JSON.stringify(fn())}`; } catch (error) { return `refused: ${error.message}`; } };
const draft0 = complete[0].run.result.draft;
const broken = (mutate) => { const copy = structuredClone(draft0); mutate(copy); return copy; };
const draftRecords = [
  ['valid', draft0], ['valid-other-project', complete[1].run.result.draft], ['altered-prose', alteredDraft(draft0)],
  ['missing-title', broken((d) => { delete d.title; })], ['extra-field', broken((d) => { d.extra = 1; })],
  ['empty-text', broken((d) => { d.introduction.text = ''; })], ['text-too-long', broken((d) => { d.introduction.text = 'x'.repeat(8001); })],
  ['bad-handle', broken((d) => { d.introduction.id = '-bad'; })], ['handle-too-long', broken((d) => { d.introduction.id = 'a'.repeat(101); })],
  ['duplicate-ref', broken((d) => { d.introduction.sourceIds = [d.introduction.sourceIds[0], d.introduction.sourceIds[0]]; })],
  ['unknown-disposition', broken((d) => { d.sections[0].disposition = { kind: 'maybe' }; })], ['not-an-object', 'draft'], ['null', null],
  ['array-for-object', broken((d) => { d.introduction = []; })], ['bad-diagram-kind', broken((d) => { if (d.diagrams[0]) d.diagrams[0].kind = 'pie'; else d.diagrams = [{}]; })],
];
const assetRecords = [['dossier-assets', oldCore.DOSSIER_REQUESTED_ASSETS], ['synthetic-assets', complete[0].run.requestedAssets], ['empty', []],
  ['bad-kind', [{ id: 'how', kind: 'poem', required: true }]], ['missing-required', [{ id: 'how', kind: 'section' }]], ['duplicate', [...complete[0].run.requestedAssets, complete[0].run.requestedAssets[0]]]];
const reviews = [['complete-review', complete[0].run.result.review], ['other-review', complete[1].run.result.review], ['empty', {}], ['null', null],
  ['bad-verdict', (() => { const r = structuredClone(complete[0].run.result.review); if (r?.blockSupport?.[0]) r.blockSupport[0].verdict = 'maybe'; return r; })()]];
const stageRecords = runs.flatMap(({ name, run }) => run.result.artifacts.map((a, i) => [`${name}/${i}-${a.stage}`, a.stage, a.value]))
  .concat([['inventory-broken', 'inventory', { entries: 'none' }], ['plan-broken', 'plan', {}], ['author-altered', 'author', alteredDraft(draft0)]]);
const diagrams = [draft0, complete[1].run.result.draft, alteredDraft(draft0)].flatMap((d, i) => d.diagrams.map((g, j) => [`draft-${i}/diagram-${j}`, g]));
const validatorRows = [
  ...draftRecords.map(([name, v]) => ['validateDraftRecord', name, () => oldCore.validateDraftRecord(v), () => newCore.validateDraftRecord(v)]),
  ...assetRecords.map(([name, v]) => ['validateRequestedAssets', name, () => oldCore.validateRequestedAssets(v), () => newCore.validateRequestedAssets(v)]),
  ...reviews.map(([name, v]) => ['reviewVerdict', name, () => oldCore.reviewVerdict(v), () => newCore.reviewVerdict(v)]),
  ...stageRecords.map(([name, stage, v]) => ['validateStage', name, () => oldCore.validateStage(stage, v), () => newCore.validateStage(stage, v)]),
  ...diagrams.map(([name, g]) => ['diagramToMermaid', name, () => oldCore.diagramToMermaid(g), () => newCore.diagramToMermaid(g)]),
].map(([fn, name, before, after]) => { const a = verdict(before), b = verdict(after); return { fn, name, identical: a === b, outcomeSha256: sha(b), refused: b.startsWith('refused: ') ? b : null }; });
const sameObjects = ['validateDraftRecord', 'validateRequestedAssets', 'reviewVerdict', 'diagramToMermaid', 'OWNER_TOPICS', 'SOURCE_ID_PATTERN', 'DIAGRAM_KINDS']
  .map((name) => ({ name, rootIsLive: newCore[name] === newLive[name] && newCore[name] !== undefined }));

// --- compiled modules whose change is to imports or types only
const IMPORT_ONLY = [
  ...['check', 'class-gate', 'close', 'credential-probe', 'design-review', 'draft-schema', 'execution-choice', 'inventory', 'render', 'reverify', 'review',
    'run-config', 'run-record', 'screen', 'status', 'waiting-sessions'].map((m) => `${DOSSIER}/${m}.js`),
  ...['diagram-layout', 'dossier-render-local', 'draft-preview'].map((m) => `${APP}/${m}.js`),
  ...['admitted-input', 'dossier-profile', 'generation-source', 'local-render', 'reader-questions'].map((m) => `${CORE}/${m}.js`),
];
const ts = createRequire(path.join(NEW, 'package.json'))('typescript');
/** The module's statements other than its import declarations and `export … from` re-exports, and each of those with its specifier. */
const split = (text) => {
  const file = ts.createSourceFile('m.js', text, ts.ScriptTarget.Latest, true, ts.ScriptKind.JS);
  const isImport = (s) => ts.isImportDeclaration(s) || (ts.isExportDeclaration(s) && s.moduleSpecifier !== undefined);
  const printer = ts.createPrinter({ removeComments: true });
  const kept = file.statements.filter((s) => !isImport(s));
  return { body: kept.map((s) => s.getFullText(file)).join(''), code: kept.map((s) => printer.printNode(ts.EmitHint.Unspecified, s, file)).join('\n'),
    imports: file.statements.filter(isImport).map((s) => s.getText(file).replace(/\s+/gu, ' ')) };
};
const compiled = IMPORT_ONLY.map((file) => {
  const a = fs.readFileSync(path.join(OLD, file), 'utf8'), b = fs.readFileSync(path.join(NEW, file), 'utf8');
  const live = b.replaceAll("'@syzygy/polaris-generation-core/live'", "'@syzygy/polaris-generation-core'");
  const before = split(a), after = split(b);
  return { file, identicalRaw: a === b, identicalAfterLiveSpecifier: a === live, identicalOutsideImportStatements: before.body === after.body,
    identicalCodeOutsideImportStatements: before.code === after.code,
    ...(a === live ? {} : { importsOld: before.imports, importsNew: after.imports }) };
});

const guidance = { oldVersion: oldBrief.brief.DOSSIER_GUIDANCE_VERSION, newVersion: newBrief.brief.DOSSIER_GUIDANCE_VERSION,
  identical: oldBrief.brief.DOSSIER_GUIDANCE === newBrief.brief.DOSSIER_GUIDANCE, sha256: sha(newBrief.brief.DOSSIER_GUIDANCE), bytes: Buffer.byteLength(newBrief.brief.DOSSIER_GUIDANCE) };
const self = fs.readFileSync(new URL(import.meta.url), 'utf8');
const summarize = (rows) => ({ fixtures: rows.length, identical: rows.filter((row) => row.identical).length });
console.log(JSON.stringify({
  format: 'syzygy-bpyt-8-1-differential/1', differentialSha256: sha(self),
  old: { tree: OLD, commit: commit(OLD) }, new: { tree: NEW, commit: commit(NEW) },
  localRender: compare(localCases, (input) => oldRender.renderDossier(input), (input) => newSite.renderLocalDossier(input)),
  providerRender: compare(providerCases, (input) => oldRender.renderDossier(input), (input) => newRender.renderDossier(input)),
  brief: { guidance, ...summarize(briefRows), distinctOutputs: new Set(briefRows.map((row) => row.outputSha256)).size, rows: briefRows },
  validators: { ...summarize(validatorRows), distinctOutcomes: new Set(validatorRows.map((row) => row.outcomeSha256)).size,
    refusals: validatorRows.filter((row) => row.refused !== null).length, sameObjects, rows: validatorRows },
  compiledModules: { modules: compiled.length, identicalAfterLiveSpecifier: compiled.filter((row) => row.identicalAfterLiveSpecifier).length,
    identicalOutsideImportStatements: compiled.filter((row) => row.identicalOutsideImportStatements).length,
    identicalCodeOutsideImportStatements: compiled.filter((row) => row.identicalCodeOutsideImportStatements).length, rows: compiled },
}, null, 2));
