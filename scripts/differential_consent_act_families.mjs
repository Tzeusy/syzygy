#!/usr/bin/env node
// Old-versus-new differential of the consent gate's act-record readers (syzygy-bpyt.8.4). Evidence tool, not a check and not authority.
//
//   (in each tree) npm ci && npx tsc -b packages/polaris-generation-consent packages/polaris-dossier
//   node scripts/differential_consent_act_families.mjs --old <tree> --new <tree> --out <file.json> [--workers <n>] [--kinds <k,...>] [--count]
//
// `--old` and `--new` are two Syzygy checkouts with those packages built: the base and the change. Every reader the gate composes over
// owner-act records (the admission, policy-chain, class-act, in-force egress, digest-bound, sign-off and dossier sitting reads, and
// each question the admission records port answers) runs from both trees' compiled packages over the same worlds, at the same
// instants, and the two answers are compared as text: the answer's JSON, or the error the read throws.
//
// A world is the files of `--old` (read through the readers' own file-system port, rooted there for both trees) with in-memory
// overrides: an act record altered, added or deleted, an artifact altered or deleted, or a decisions file added. Nothing on disk is
// written; no observed repository is read. The corpus:
// - three base worlds: the checkout as it is; with the three admission acts this checkout lacks (requests observation, egress
//   version 1 and version 2), rendered by their recorders over the checkout's own instance records; and with the registry
//   git-source act, rendered the same way;
// - for each field-parsed act record (the four admission acts, the four screening-scope policy acts, the RFC5-14 class act and the
//   registry act): each non-blank line on its own with ` [altered]` appended, deleted, duplicated, and fenced;
// - for each act record, field-parsed or byte-exact: named alterations of its head (act type values and duplicates, the fixed
//   recorder lines, the instant line, the supersession field, the identity, the title, the date) and of its prose, the latter being
//   the `PROSE_ALTERATIONS` and `HEAD_FIELD_ALTERATION` corpus of syzygy-bpyt.8.10 (PR #500), copied below because that PR has not
//   merged;
// - each pinned file (the owner-answers direction, the three historical policy acts) altered and deleted, and each act's artifact
//   altered and deleted;
// - one added decisions file per (needle, placement): every stem, path and field stem the families sweep for, in prose, on each
//   swept field line, behind a `>`, spelled loosely, in the file's name, with a withdrawal word in the name, and in the aggregate
//   acceptance record.
// The output names each tree's commit and the sha256 of each tree's package-reader.ts, counts the worlds and the distinct answers,
// and lists every world whose answers differ (there should be none). Answers are stored by sha256 with a short label; a label never
// carries a digest.

import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as fsp from 'node:fs/promises';
import * as os from 'node:os';
import * as path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { Worker, isMainThread, parentPort, workerData } from 'node:worker_threads';

const SCRIPT = fileURLToPath(import.meta.url);
const SCRIPT_REL = 'scripts/differential_consent_act_families.mjs';
const D = '.syzygy/governance/decisions';
const INSTANT_MID = '2026-10-08T09:30:00Z';
const INSTANT_LATE = '2026-10-22T12:00:00Z';
const INSTANTS = [INSTANT_MID, INSTANT_LATE].map(at => [at, Date.parse(at)]);
const MARK = ' [altered]';

const sha256 = text => createHash('sha256').update(text, 'utf8').digest('hex');

// ---------------------------------------------------------------------------------------------------------------------------------
// The readers, run in a worker against one tree's compiled packages.

/** A reader file system over `root` with `overlay` (repository-relative path to text, or null for a deleted file). */
function overlayFs(root, overlay) {
  const keys = Object.entries(overlay);
  return {
    readdir: async dir => {
      const rel = path.relative(root, dir);
      let names;
      try { names = new Set(await fsp.readdir(dir)); } catch (error) {
        if (!keys.some(([key, value]) => value !== null && key.startsWith(`${rel}/`))) throw error;
        names = new Set();
      }
      for (const [key, value] of keys) {
        if (!key.startsWith(`${rel}/`)) continue;
        const rest = key.slice(rel.length + 1), first = rest.split('/')[0];
        if (value === null) { if (!rest.includes('/')) names.delete(first); } else names.add(first);
      }
      return [...names];
    },
    readFile: async file => {
      const rel = path.relative(root, file);
      if (Object.hasOwn(overlay, rel)) { if (overlay[rel] === null) throw Object.assign(new Error(`ENOENT: ${rel}`), { code: 'ENOENT' }); return overlay[rel]; }
      return fsp.readFile(file, 'utf8');
    },
  };
}

const answer = async read => { try { return JSON.stringify(await read()) ?? 'undefined'; } catch (error) { return `throws ${error?.name}: ${error?.message}`; } };

/** Each reader: its name, whether it takes an instant, and the read over one tree's modules. */
function readers(consent, gate, probe) {
  const statementV1 = gate.STATEMENT_FORMS['redis-redis'][0].form;
  const digestBound = form => (fs, root, now) => consent.readDigestBoundActState({ root, fs, now, form });
  return [
    ['admission', false, (fs, root) => consent.createPackageAdmissionReader({ root, fs }).read()],
    ['policy-reader', false, (fs, root) => consent.createPackagePolicyReader({ root, fs }).read()],
    ['policy-chain', true, (fs, root, now) => consent.readPolicyActChain({ root, fs, now })],
    ['class-act', true, (fs, root, now) => consent.readClassActState({ root, fs, now })],
    ['in-force-egress', true, (fs, root, now) => consent.readInForceEgress({ root, fs, now })],
    ['registry-git-source', true, digestBound(consent.REGISTRY_GIT_SOURCE_ACT_FORM)],
    ['local-agent-signoff', true, (fs, root, now) => consent.readVersionedSignoffState({ root, fs, now, form: consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM })],
    ['dossier-d9', true, digestBound(gate.D9_ACT_FORM)],
    ['dossier-rfc7-20', true, digestBound(gate.RFC7_20_RULING_ACT_FORM)],
    ['dossier-drawer', true, digestBound(gate.DRAWER_FORMS['redis-redis'])],
    ['dossier-statement-v1', true, digestBound(statementV1)],
    ['dossier-provider-v2', true, digestBound(gate.PROVIDER_V2_FORM)],
    ['port', true, async (fs, root, now) => {
      const port = consent.createPackageAdmissionRecordsPort({ root, now: () => now, fs });
      const out = {};
      for (const [name, repositoryId, revision] of [['observation-redis', probe.redisId, probe.redisRevision], ['observation-requests', probe.requestsId, probe.requestsRevision]]) {
        out[name] = await port.check({ kind: 'observation-consent', repositoryId, revision });
      }
      out['egress-redis'] = await port.check({ kind: 'egress-consent', repositoryId: probe.redisId, revision: probe.redisRevision });
      out['public-source-policy'] = await port.check({ kind: 'public-source-policy', repositoryId: probe.redisId, revision: probe.redisRevision });
      out['revisions-redis'] = await port.consentedRevisionsFor(probe.redisId);
      out['ids-redis'] = await port.repositoryIdsFor(probe.redisUrl);
      out['absence-redis'] = await port.consentAbsenceFor(probe.redisUrl);
      return out;
    }],
  ];
}

if (!isMainThread) {
  const { trees, root, probe, drops } = workerData;
  const loaded = await Promise.all(trees.map(async tree => readers(
    await import(pathToFileURL(path.join(tree, 'packages/polaris-generation-consent/dist/index.js')).href),
    await import(pathToFileURL(path.join(tree, 'packages/polaris-dossier/dist/gate-sources.js')).href),
    probe,
  )));
  const dropped = Object.fromEntries(drops.map(rel => [rel, null]));
  parentPort.on('message', async ({ id, overlay, names, instants, reduced }) => {
    const fs = overlayFs(root, reduced ? { ...dropped, ...overlay } : overlay), out = [];
    for (const list of loaded) {
      const answers = [];
      for (const [name, timed, read] of list) {
        if (!names.includes(name)) continue;
        for (const [at, now] of timed ? INSTANTS.filter(([instant]) => instants.includes(instant)) : [[null, null]]) {
          const text = await answer(() => read(fs, root, now));
          answers.push([at === null ? name : `${name}@${at}`, sha256(text), label(text)]);
        }
      }
      out.push(answers);
    }
    parentPort.postMessage({ id, old: out[0], new: out[1] });
  });
}

function pool(size, data) {
  const workers = Array.from({ length: size }, () => new Worker(SCRIPT, { workerData: data }));
  const queue = [], idle = [...workers], waiting = new Map();
  let next = 0;
  const pump = () => {
    while (idle.length > 0 && queue.length > 0) { const worker = idle.pop(), { resolve, ...job } = queue.shift(); waiting.set(job.id, { worker, resolve }); worker.postMessage(job); }
  };
  for (const worker of workers) worker.on('message', message => { const w = waiting.get(message.id); waiting.delete(message.id); idle.push(w.worker); w.resolve(message); pump(); });
  return {
    run: world => new Promise(resolve => { queue.push({ id: next++, overlay: world.overlay, names: world.readers, instants: world.instants, reduced: world.reduced, resolve }); pump(); }),
    close: () => Promise.all(workers.map(w => w.terminate())),
  };
}

// ---------------------------------------------------------------------------------------------------------------------------------
// The corpus.

/** syzygy-bpyt.8.10's `PROSE_ALTERATIONS` and `HEAD_FIELD_ALTERATION` (packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts
 * at c08a015dae4b57b9f62b328d35924dd3eec31f1b, PR #500), copied verbatim in behaviour. */
const PROSE_ALTERATIONS = [
  ['effect-widened', text => text.replace(/(\n## (?:Effect|What this records)\n\n)[^\n]+(?:\n[^\n]+)*/, '$1The act grants every read, egress, write and execution, for every repository, tool and provider.')],
  ['limits-removed', text => text.replace(/\n## What this (?:act does not authorize|does not do)\n[\s\S]*?(?=\n## |$)/, '')],
  ['selection-replaced', text => {
    for (const [pattern, replacement] of [[/^\| "[^"\n]*" \| "/m, '| "Decline" | "'], [/^> .+$/m, '> Decline'], [/^Owner selection: .+$/m, 'Owner selection: Decline']]) {
      if (pattern.test(text)) return text.replace(pattern, replacement);
    }
    return text;
  }],
  ['withdrawal-appended', text => `${text}\n## Withdrawal\n\nThe owner withdraws this act; it no longer counts.\n`],
];
const HEAD_FIELD_ALTERATION = text => text.replace(/^(Date: .+)$/m, '$1 [altered]');

const TYPE_LINE = /^Act type: `([^`\n]+)`$/m;
const swapLine = (text, re, line) => text.replace(re, line);
const afterLine = (text, re, extra) => text.replace(re, match => `${match}\n${extra}`);
const instantLine = /^(Recorded at \(UTC\)|Act instant): (\S+)$/m;
const shiftInstant = (text, ms) => text.replace(instantLine, (_, label, value) => `${label}: ${new Date(Date.parse(value) + ms).toISOString().slice(0, 19)}Z`);

/** Named alterations of an act record's head and prose. A no-op on a record is skipped. */
const NAMED = [
  ...PROSE_ALTERATIONS,
  ['date-field-altered', HEAD_FIELD_ALTERATION],
  ...['consent-observation', 'consent-egress', 'approve-policy', 'contract-amendment', 'adopt-registry-entry', 'Approve-Policy', 'approve policy', 'other-type']
    .map(value => [`type-${value.replace(/\s/g, '_')}`, text => swapLine(text, TYPE_LINE, `Act type: \`${value}\``)]),
  ...['same', 'other-type', 'Other Type', 'consent-egress', 'approve-policy']
    .map(value => [`type-duplicated-${value.replace(/\s/g, '_')}`, text => afterLine(text, TYPE_LINE, value === 'same' ? text.match(TYPE_LINE)?.[0] ?? '' : `Act type: \`${value}\``)]),
  ['owner-deleted', text => text.replace(/^Owner: .*\n/m, '')],
  ['owner-other', text => text.replace(/^Owner: .*$/m, 'Owner: someone-else')],
  ['a1-deleted', text => text.replace(/^A1 audit-record identity.*\n/m, '')],
  ['provenance-tail-dropped', text => text.replace(/^(Provenance state: `owner-adopted \(bootstrap, uncorrelated\)`).*$/m, '$1')],
  ['provenance-tail-other', text => text.replace(/^(Provenance state: `owner-adopted \(bootstrap, uncorrelated\)`).*$/m, '$1 — state (2),')],
  ['provenance-other', text => text.replace(/^Provenance state: `[^`\n]*`/m, 'Provenance state: `owner-adopted (other)`')],
  ['provenance-duplicated', text => text.replace(/^(Provenance state: .*)$/m, '$1\n$1')],
  ['provenance-deleted', text => text.replace(/^Provenance state: .*\n/m, '')],
  ['provenance-fenced', text => text.replace(/^(Provenance state: .*)$/m, '```\n$1\n```')],
  ['instant-label-recorded', text => text.replace(/^Act instant: /m, 'Recorded at (UTC): ')],
  ['instant-label-act', text => text.replace(/^Recorded at \(UTC\): /m, 'Act instant: ')],
  ['instant-duplicated', text => text.replace(instantLine, '$&\n$&')],
  ['instant-plus-one-second', text => shiftInstant(text, 1000)],
  ['instant-next-day', text => shiftInstant(text, 86_400_000)],
  ['instant-commented', text => text.replace(instantLine, '<!-- $& -->')],
  ['supersession-duplicated', text => text.replace(/^(Supersession \/ revocation: .*)$/m, '$1\n\n$1')],
  ['supersession-deleted', text => text.replace(/^Supersession \/ revocation: .*\n(?:[^\n]+\n)*/m, '')],
  ['supersession-fenced', text => text.replace(/^(Supersession \/ revocation: .*)$/m, '```\n$1\n```')],
  ['identity-other-date', text => text.replace(/^(Act identity: `[^`\n]*-)\d{4}-\d{2}-\d{2}`$/m, '$12026-01-01`')],
  ['identity-duplicated', text => text.replace(/^(Act identity: .*)$/m, '$1\n$1')],
  ['artifact-other', text => text.replace(/^Artifact identity: `[^`\n]*`$/m, 'Artifact identity: `.syzygy/governance/other.md`')],
  ['project-other', text => text.replace(/^Project identity: `[^`\n]*`$/m, 'Project identity: `project:other`')],
  ['digest-duplicated', text => text.replace(/^(Exact digest \(SHA-256\): .*)$/m, '$1\n$1')],
  ['date-invalid', text => text.replace(/^Date: \d{4}-\d{2}-\d{2}$/m, 'Date: 2026-02-30').replace(instantLine, (_, label, value) => `${label}: 2026-02-30${value.slice(10)}`)],
  ['date-moved-last', text => { const m = /^Date: .*\n/m.exec(text); return m === null ? text : `${text.replace(m[0], '')}\n${m[0]}`; }],
  ['title-trailing-space', text => text.replace(/^(# .*)$/m, '$1 ')],
  ['title-other', text => text.replace(/^# .*$/m, '# Owner act — another form')],
  ['head-field-quoted', text => text.replace(/^(Act identity: .*)$/m, '> $1')],
];

const BYTE_EXACT_NAMED = new Set(['title-trailing-space', 'title-other', 'date-field-altered']);

/** The per-line operators for a field-parsed record. */
const LINE_OPERATORS = [
  ['append', (lines, i) => { const copy = [...lines]; copy[i] += MARK; return copy; }],
  ['delete', (lines, i) => { const copy = [...lines]; copy.splice(i, 1); return copy; }],
  ['duplicate', (lines, i) => { const copy = [...lines]; copy.splice(i, 0, lines[i]); return copy; }],
  ['fence', (lines, i) => { const copy = [...lines]; copy.splice(i, 1, '```', lines[i], '```'); return copy; }],
];

/** The placements of a needle in an added decisions file (or in the aggregate record). */
const PLACEMENTS = [
  ['prose', n => [['ZZ-PROBE.md', `# Probe\n\nSee ${n}.\n`]]],
  ...['Artifact identity', 'Act identity', 'Record ID', 'Subject'].map(label => [`field-${label.replace(/\s/g, '_')}`, n => [['ZZ-PROBE.md', `# Probe\n\n${label}: \`${n}\`\n`]]]),
  ...['Artifact identity', 'Act identity', 'Subject'].map(label => [`quoted-field-${label.replace(/\s/g, '_')}`, n => [['ZZ-PROBE.md', `# Probe\n\n> ${label}: \`${n}\`\n`]]]),
  ['bulleted-bold-field', n => [['ZZ-PROBE.md', `# Probe\n\n- **Act identity:** \`${n}\`\n`]]],
  ['loose-spelling', n => [['ZZ-PROBE.md', `# Probe\n\nSee ${n.slice(0, 1)}\`${n.slice(1).replace(/:/g, ' : ').replace(/,/g, ' , ')}.\n`]]],
  ['upper-underscored', n => [['ZZ-PROBE.md', `# Probe\n\nSee ${n.toUpperCase().replace(/-/g, '_')}.\n`]]],
  ['soft-hyphenated', n => [['ZZ-PROBE.md', `# Probe\n\nSee ${n.replace(/-/g, '­-')}.\n`]]],
  ['in-subdirectory', n => [['sub/ZZ-PROBE.md', `# Probe\n\nSee ${n}.\n`]]],
  ['in-name', n => [[`ZZ-${n.replace(/[^A-Za-z0-9-]+/g, '-').slice(-60)}.md`, '# Probe\n\nNothing here.\n']]],
  ['in-name-withdrawal', n => [[`ZZ-${n.replace(/[^A-Za-z0-9-]+/g, '-').slice(-50)}-WITHDRAWAL.md`, '# Probe\n\nNothing here.\n']]],
  ['in-aggregate-prose', n => [['ACCEPTANCE-ACT-RECORD.md', null, `\nSee ${n}.\n`]]],
  ['in-aggregate-field', n => [['ACCEPTANCE-ACT-RECORD.md', null, `\nAct identity: \`${n}\`\n`]]],
];

function git(tree, ...args) { return execFileSync('git', ['-C', tree, ...args], { encoding: 'utf8' }).trim(); }

function render(root, module, call) {
  const run = spawnSync('python3', ['-c', `import sys; sys.path.insert(0, 'scripts'); import ${module} as m\nsys.stdout.write(${call})`], { cwd: root, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
  return run.stdout;
}

function walk(dir, prefix = '') {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => (entry.isDirectory() ? walk(path.join(dir, entry.name), `${prefix}${entry.name}/`) : [`${prefix}${entry.name}`]));
}
const ALL_READERS = ['admission', 'policy-reader', 'policy-chain', 'class-act', 'in-force-egress', 'registry-git-source', 'local-agent-signoff', 'dossier-d9', 'dossier-rfc7-20', 'dossier-drawer', 'dossier-statement-v1', 'dossier-provider-v2', 'port'];

async function corpus(root, consent, gate, allowlist) {
  const read = rel => fs.readFileSync(path.join(root, rel), 'utf8');
  const exists = rel => fs.existsSync(path.join(root, rel));
  const at = form => `${D}/${form.file}`;
  const admission = Object.fromEntries(consent.ADMISSION_ACT_FORMS.map(form => [form.file, form]));
  const form = file => admission[file];
  const SEL = "m.Selection('opening', 'label', 'description')";
  const admissionAct = (key, file, date, instant) => {
    const module = key === 'egress-anthropic-v2' ? 'record_public_egress_v2_act' : 'record_public_repo_admission_acts';
    return render(root, module, `m.render_act(m.ACT_BY_KEY['${key}'], '${sha256(read(form(file).artifact))}', '${date}', 'b'*64, 'c'*40, 'CONFIRM', ${SEL}, 'f'*64, '${instant}')`);
  };
  const synthetic = {
    [`${D}/PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md`]: admissionAct('requests-observation', 'PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md', '2026-10-08', '2026-10-08T10:00:00Z'),
    [`${D}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md`]: admissionAct('egress-anthropic', 'PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md', '2026-10-08', '2026-10-08T09:00:00Z'),
    [`${D}/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md`]: admissionAct('egress-anthropic-v2', 'PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md', '2026-10-09', '2026-10-09T09:00:00Z'),
  };
  const registry = consent.REGISTRY_GIT_SOURCE_ACT_FORM;
  const registryAct = render(root, 'record_public_admission_registry_entries_acts', `m.render_act(m.ACT_BY_KEY['git-source-acquisition'], '${sha256(read(registry.artifact))}', '2026-10-08', 'b'*64, 'c'*40, 'CONFIRM', ${SEL}, 'f'*64, '2026-10-08T11:00:00Z')`);
  const BASES = {
    checkout: {},
    'admission-acts': { ...synthetic },
    'registry-act': { [at(registry)]: registryAct },
    'all-acts': { ...synthetic, [at(registry)]: registryAct },
  };
  for (const [rel] of Object.entries(synthetic)) if (exists(rel)) throw new Error(`${rel} exists here: the corpus renders it only where the checkout lacks it`);
  if (exists(at(registry))) throw new Error(`${at(registry)} exists here`);

  const statementV1 = gate.STATEMENT_FORMS['redis-redis'][0].form;
  const textOf = (base, rel) => (Object.hasOwn(BASES[base], rel) ? BASES[base][rel] : read(rel));
  /** Each act record: its key, path, base world, how its form reads it, and its artifact. */
  // A subject world runs the readers that read the subject's record; the readers that read it only as another file in their sweep run
  // over the probes, which put each of their needles into a file of its own.
  const SUBJECTS = [
    ...consent.ADMISSION_ACT_FORMS.map(f => ({ key: `admission:${f.file}`, path: at(f), base: 'admission-acts', model: 'field-parsed', artifact: f.artifact, readers: ['admission'] })),
    ...consent.POLICY_ACT_FORMS.map(f => ({ key: `policy:${f.file}`, path: at(f), base: 'checkout', model: 'field-parsed', artifact: consent.POLICY_PATH, readers: ['policy-reader', 'policy-chain'] })),
    { key: 'class:RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md', path: `${D}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`, base: 'admission-acts', model: 'field-parsed', artifact: '.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md', readers: ['class-act', 'admission'] },
    { key: `registry:${registry.file}`, path: at(registry), base: 'registry-act', model: 'field-parsed', artifact: registry.artifact, readers: ['registry-git-source'] },
    { key: `signoff:${consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.file}`, path: at(consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM), base: 'checkout', model: 'byte-exact', artifact: consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.installed, readers: ['local-agent-signoff'] },
    ...[[gate.D9_ACT_FORM, ['dossier-d9']], [gate.RFC7_20_RULING_ACT_FORM, ['dossier-rfc7-20']], [statementV1, ['dossier-statement-v1', 'dossier-provider-v2']], [gate.PROVIDER_V2_FORM, ['dossier-provider-v2', 'dossier-statement-v1']]]
      .map(([f, names]) => ({ key: `dossier:${f.file}`, path: at(f), base: 'checkout', model: 'byte-exact', artifact: f.artifact, readers: names })),
  ].filter(s => Object.hasOwn(BASES[s.base], s.path) || exists(s.path));

  const worlds = [];
  const add = (kind, subject, operator, base, overlay, readers = ALL_READERS, instants = INSTANTS.map(([instant]) => instant), reduced = true) =>
    worlds.push({ kind, subject, operator, base, overlay: { ...BASES[base], ...overlay }, readers, instants, reduced });
  for (const base of Object.keys(BASES)) { add('base', null, 'none', base, {}, ALL_READERS, undefined, false); add('base-reduced', null, 'none', base, {}); }
  for (const s of SUBJECTS) {
    const text = textOf(s.base, s.path);
    if (s.model === 'field-parsed') {
      const lines = text.split('\n');
      for (const [i, line] of lines.entries()) {
        if (line.trim() === '') continue;
        for (const [name, op] of LINE_OPERATORS) add('line', s.key, `${name}:${i + 1}`, s.base, { [s.path]: op(lines, i).join('\n') }, s.readers);
      }
    }
    const seen = new Set([text]);
    for (const [name, alter] of NAMED) {
      // A byte-exact record that its template does not render back takes tens of seconds to refuse (the line slots backtrack,
      // syzygy-bpyt.8.10), and both trees refuse it in the same unchanged call: only the title alterations, which refuse before the
      // template, and one template refusal per record, at one instant, run.
      if (s.model === 'byte-exact' && !BYTE_EXACT_NAMED.has(name)) continue;
      const altered = alter(text);
      if (seen.has(altered)) continue;
      seen.add(altered);
      add('named', s.key, name, s.base, { [s.path]: altered }, s.readers.slice(0, s.model === 'byte-exact' && name === 'date-field-altered' ? 1 : undefined),
        s.model === 'byte-exact' && name === 'date-field-altered' ? [INSTANT_LATE] : undefined);
    }
    add('record', s.key, 'deleted', s.base, { [s.path]: null }, s.readers);
  }
  const artifacts = new Map();
  for (const s of SUBJECTS) artifacts.set(s.artifact, { base: s.base, readers: [...new Set([...(artifacts.get(s.artifact)?.readers ?? []), ...s.readers])] });
  for (const [artifact, { base, readers: names }] of artifacts) {
    add('artifact', artifact, 'byte-appended', base, { [artifact]: `${textOf(base, artifact)}\n` }, names);
    add('artifact', artifact, 'deleted', base, { [artifact]: null }, names);
  }
  const pins = [`${D}/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`, ...['PWB-SECRET-CLASSIFICATION-POLICY-ACT.md', 'PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md', 'PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md'].map(f => `${D}/${f}`)];
  for (const pin of pins) {
    const names = pin.includes('PUBLIC-REPO-ADMISSION') ? ['admission'] : ['policy-reader', 'policy-chain'];
    add('pin', pin, 'byte-appended', 'admission-acts', { [pin]: `${read(pin)}\n` }, names);
    add('pin', pin, 'deleted', 'admission-acts', { [pin]: null }, names);
  }

  // Every needle a family sweeps for: the admission stems and paths, the policy and scope stems and the policy path, the class stem and
  // module, and each digest-bound and sign-off form's stems, field stems and artifact.
  const forms = [registry, gate.D9_ACT_FORM, gate.RFC7_20_RULING_ACT_FORM, gate.DRAWER_FORMS['redis-redis'], statementV1, gate.PROVIDER_V2_FORM];
  const needles = [...new Set([
    'public-repo-admission', 'public-egress-v2', 'public-obs-', 'public-egress-anthropic', 'public-egress-',
    '.syzygy/governance/contracts/candidates/public-repo-admission/instances', ...consent.ADMISSION_ACT_FORMS.map(f => f.artifact),
    '.syzygy/governance/contracts/candidates/public-repo-admission/', '.syzygy/governance/contracts/candidates/public-egress-v2/',
    'public-source-scope', 'pwb-secret-classification-policy', consent.POLICY_PATH,
    'rfc5-project-documentation', '.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md',
    ...forms.flatMap(f => [...f.stems, ...(f.fieldStems ?? []), f.artifact]),
    ...consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.stems, consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.installed,
  ])];
  const aggregate = read(`${D}/ACCEPTANCE-ACT-RECORD.md`);
  for (const needle of needles) {
    for (const [name, place] of PLACEMENTS) {
      const overlay = {};
      for (const [file, text, appended] of place(needle)) overlay[`${D}/${file}`] = text ?? `${aggregate}${appended}`;
      add('probe', needle, name, 'all-acts', overlay, ALL_READERS.filter(n => n !== 'port'), [INSTANT_LATE]);
    }
  }
  // The reduced tree: the decisions files any reader names (every form's record, its exempt records and its bound files, the pins, the
  // aggregate record, the allowlisted files and the README); every other decisions file is left out, so a read sweeps a few hundred
  // kilobytes, not the whole directory. Base worlds run over the whole tree too.
  const named = f => [at(f), ...(f.exemptRecords ?? []).map(e => `${D}/${e.file}`), ...(f.bound ?? [])];
  const keep = new Set([
    ...consent.ADMISSION_ACT_FORMS.map(at), ...consent.POLICY_ACT_FORMS.map(at), ...pins, `${D}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`,
    at(registry), at(consent.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM), ...forms.flatMap(named),
    ...Object.values(gate.STATEMENT_FORMS).flat().flatMap(st => [st.form, st.successor].filter(Boolean)).flatMap(named),
    `${D}/ACCEPTANCE-ACT-RECORD.md`, `${D}/README.md`, ...[...allowlist.keys()].map(rel => `${D}/${rel}`),
  ]);
  const drops = walk(path.join(root, D)).map(rel => `${D}/${rel}`).filter(rel => !keep.has(rel));
  return { worlds, subjects: SUBJECTS, needles, drops, kept: [...keep].filter(exists).sort(), bases: Object.fromEntries(Object.entries(BASES).map(([k, v]) => [k, Object.keys(v)])) };
}

// ---------------------------------------------------------------------------------------------------------------------------------
// Labels: what an answer says, without its digests or texts.

function label(text) {
  if (text.startsWith('throws ')) return text;
  const value = JSON.parse(text);
  const one = v => {
    if (Array.isArray(v)) return `[${v.map(r => (typeof r === 'string' ? 'item' : r.recordId !== undefined ? `${r.recordId}@${r.version} ${r.inForceAt === null ? 'unbound' : 'bound'}` : r.actIdentity ?? (r.label !== undefined ? 'revision' : '?'))).join(', ')}]`;
    if (v === null || typeof v !== 'object') return String(v);
    if ('state' in v) return v.state === 'ok' ? `ok ${v.final?.identity ?? v.act?.identity ?? v.recordId ?? ''}${v.acts !== undefined ? ` over ${v.acts.length}` : ''}`.trim() : `${v.state}: ${v.why}`;
    if ('satisfied' in v) return v.satisfied ? `satisfied ${v.record}` : `unsatisfied: ${v.why}`;
    return Object.entries(v).map(([k, sub]) => `${k}=${one(sub)}`).join('; ');
  };
  return one(value).replace(/\b[0-9a-f]{40,64}\b/g, '<hex>');
}

async function main(argv) {
  const arg = flag => (argv.includes(flag) ? argv[argv.indexOf(flag) + 1] : undefined);
  const oldTree = arg('--old'), newTree = arg('--new'), out = arg('--out');
  if (oldTree === undefined || newTree === undefined || out === undefined) {
    process.stderr.write('usage: node scripts/differential_consent_act_families.mjs --old <tree> --new <tree> --out <file.json> [--workers <n>]\n');
    return 2;
  }
  const trees = [path.resolve(oldTree), path.resolve(newTree)], root = trees[0];
  const consent = await import(pathToFileURL(path.join(root, 'packages/polaris-generation-consent/dist/index.js')).href);
  const gate = await import(pathToFileURL(path.join(root, 'packages/polaris-dossier/dist/gate-sources.js')).href);
  const instance = rel => fs.readFileSync(path.join(root, rel), 'utf8');
  const firstRow = text => /^\| `[^`\n]+` \| `([0-9a-f]{40})` \|$/m.exec(text)[1];
  const repo = text => /^Subject: `\(project:syzygy, repository:([a-z0-9-]+)\)`$/m.exec(text)[1];
  const redis = instance(`${consent.INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`), requests = instance(`${consent.INSTANCES_DIR}/requests/OBSERVATION-CONSENT.md`);
  const probe = { redisId: repo(redis), redisRevision: firstRow(redis), redisUrl: /^Upstream: (\S+)/m.exec(redis)[1], requestsId: repo(requests), requestsRevision: firstRow(requests) };

  const { CITATION_ALLOWLIST } = await import(pathToFileURL(path.join(root, 'packages/polaris-generation-consent/dist/citation-allowlist.js')).href);
  const built = await corpus(root, consent, gate, CITATION_ALLOWLIST), kinds = arg('--kinds')?.split(',');
  const { subjects, needles, bases, drops, kept } = built, worlds = kinds === undefined ? built.worlds : built.worlds.filter(w => kinds.includes(w.kind));
  if (argv.includes('--count')) {
    const count = {};
    for (const w of built.worlds) count[w.kind] = (count[w.kind] ?? 0) + 1;
    process.stdout.write(`${JSON.stringify({ worlds: built.worlds.length, byKind: count, subjects: subjects.map(x => x.key) })}\n`);
    return 0;
  }
  const workers = Number(arg('--workers') ?? Math.max(1, Math.min(os.availableParallelism() - 2, 8)));
  const started = Date.now(), runs = pool(workers, { trees, root, probe, drops });
  let done = 0;
  const results = await Promise.all(worlds.map(async world => {
    const result = await runs.run(world);
    done += 1;
    if (done % 250 === 0) process.stderr.write(`${done}/${worlds.length} worlds, ${Math.round((Date.now() - started) / 1000)} s\n`);
    return result;
  }));
  await runs.close();

  const rows = [], mismatches = [], vectors = new Map(), perReader = new Map();
  for (const [k, world] of worlds.entries()) {
    const { old: before, new: after } = results[k];
    const vectorSha = sha256(before.map(([name, sha]) => `${name} ${sha}`).join('\n'));
    for (const [j, [name, sha, said]] of before.entries()) {
      const [, otherSha, otherSaid] = after[j];
      if (otherSha !== sha) mismatches.push({ world: k, kind: world.kind, subject: world.subject, operator: world.operator, reader: name, old: { sha256: sha, label: said }, new: { sha256: otherSha, label: otherSaid } });
      const answers = perReader.get(name) ?? new Map();
      const entry = answers.get(sha) ?? { sha256: sha, label: said, worlds: 0 };
      entry.worlds += 1;
      answers.set(sha, entry);
      perReader.set(name, answers);
    }
    const v = vectors.get(vectorSha) ?? { sha256: vectorSha, worlds: 0, first: k };
    v.worlds += 1;
    vectors.set(vectorSha, v);
    rows.push({ world: k, kind: world.kind, base: world.base, subject: world.subject, operator: world.operator, answers: vectorSha, same: before.every(([, sha], j) => after[j][1] === sha) });
  }
  const readerNames = [...new Set(results.flatMap(r => r.old.map(([name]) => name)))];
  const document = {
    schema: 'consent-act-family-differential/1',
    bead: 'syzygy-bpyt.8.4',
    text: 'Evidence record, not authority: the consent gate\'s act-record readers before and after the act-family convergence, over one corpus. Generated by the script named here; do not edit.',
    script: { path: SCRIPT_REL, sha256: sha256(fs.readFileSync(SCRIPT, 'utf8')) },
    trees: trees.map((tree, i) => ({
      role: i === 0 ? 'old' : 'new',
      commit: git(tree, 'rev-parse', 'HEAD'),
      clean: git(tree, 'status', '--porcelain', '--untracked-files=no') === '',
      packageReaderSha256: sha256(fs.readFileSync(path.join(tree, 'packages/polaris-generation-consent/src/package-reader.ts'), 'utf8')),
    })),
    corpusRoot: 'old',
    instants: INSTANTS.map(([at]) => at),
    pool: { workers, node: process.version, wallSeconds: Math.round((Date.now() - started) / 1000) },
    readers: readerNames,
    bases,
    reducedTree: { kept, dropped: drops.length },
    subjects: subjects.map(({ key, path: p, base, model, readers: names }) => ({ key, path: p, base, model, readers: names })),
    needles: needles.length,
    operators: { line: LINE_OPERATORS.map(([n]) => n), named: NAMED.map(([n]) => n), placements: PLACEMENTS.map(([n]) => n) },
    totals: {
      worlds: worlds.length,
      byKind: Object.fromEntries([...new Set(worlds.map(w => w.kind))].map(kind => [kind, worlds.filter(w => w.kind === kind).length])),
      answersCompared: results.reduce((n, r) => n + r.old.length, 0),
      mismatches: mismatches.length,
      distinctAnswerVectors: vectors.size,
      worldsWithDistinctVector: [...vectors.values()].filter(v => v.worlds === 1).length,
      distinctAnswersPerReader: Object.fromEntries([...perReader].map(([name, answers]) => [name, answers.size])),
    },
    mismatches,
    answersPerReader: Object.fromEntries([...perReader].map(([name, answers]) => [name, [...answers.values()].sort((a, b) => b.worlds - a.worlds)])),
    worlds: rows,
  };
  fs.writeFileSync(out, `${JSON.stringify(document, null, 1)}\n`);
  process.stderr.write(`${worlds.length} worlds, ${document.totals.answersCompared} answers compared, ${mismatches.length} mismatches, ${vectors.size} distinct answer vectors\n`);
  return mismatches.length === 0 ? 0 : 1;
}

if (isMainThread) process.exitCode = await main(process.argv.slice(2));
