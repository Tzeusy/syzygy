#!/usr/bin/env node
// What the PWB P1 body-read authority gate decides for the screening-scope version 4 act record, as committed and under the census's
// alterations (syzygy-bpyt.8.10). Evidence tool, not a check and not authority.
//
//   npx tsc -b apps/three-surface-poc
//   node scripts/probe_pwb_gate_on_altered_policy_act.mjs TREE --out <file.json>
//
// The gate's own loader (`loadBodyReadAuthorityInputs` in apps/three-surface-poc/src/governance-inputs.ts) reads the governance tree at
// TREE's HEAD commit, as production does at the observer revision (`production-reobserve.ts`), and `evaluateBodyReadAuthority` decides.
// The probe hands the loader a blob reader that returns the altered record for the one object `<HEAD>:<record>` and reads every other
// object from git, the record at its recording tag included. The alterations are the census's (PROSE_ALTERATIONS and
// HEAD_FIELD_ALTERATION from @syzygy/polaris-generation-consent/testing). The record names the sha256 of every built file it could have
// loaded from the three `dist` directories, which git does not track. It reads only TREE's Syzygy governance tree, never an observed
// repository, and writes only --out.

import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const SCRIPT = 'scripts/probe_pwb_gate_on_altered_policy_act.mjs';
const INSTANT = '2026-10-22T12:00:00Z';
const DISTS = ['apps/three-surface-poc/dist', 'packages/three-surface-poc-core/dist', 'packages/polaris-generation-consent/dist'];
const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');

const [tree, flag, out] = process.argv.slice(2);
if (tree === undefined || flag !== '--out' || out === undefined) {
  process.stderr.write('usage: node scripts/probe_pwb_gate_on_altered_policy_act.mjs TREE --out <file.json>\n');
  process.exit(2);
}
const root = path.resolve(tree);
const git = (...args) => execFileSync('git', ['-C', root, ...args], { encoding: 'utf8' }).trim();
const dist = rel => import(pathToFileURL(path.join(root, rel)).href);
const { loadBodyReadAuthorityInputs, defaultReadGitBlob, PWB_ACT_RECORDS, pwbAuthorityExpectations } = await dist('apps/three-surface-poc/dist/governance-inputs.js');
const { evaluateBodyReadAuthority } = await dist('packages/three-surface-poc-core/dist/body-read-authority.js');
const { PROSE_ALTERATIONS, HEAD_FIELD_ALTERATION } = await dist('packages/polaris-generation-consent/dist/testing.js');

const head = git('rev-parse', '--verify', 'HEAD^{commit}');
const record = PWB_ACT_RECORDS.policy;
const tag = pwbAuthorityExpectations(INSTANT).authorities.policy.recordingTag;
const tagCommit = git('rev-parse', '--verify', `refs/tags/${tag}^{commit}`);
if (tagCommit === head) throw new Error('the recording tag names HEAD itself, so the probe cannot alter HEAD\'s record alone');
const committed = defaultReadGitBlob(root, `${head}:${record}`);
const text = new TextDecoder('utf-8', { fatal: true }).decode(committed);

const state = s => (s.kind === 'valid' ? { kind: s.kind, provenance: s.provenance } : s.kind === 'invalid' ? { kind: s.kind, caseId: s.caseId } : { kind: s.kind, what: s.what });
const cases = [['as committed', t => t], ...PROSE_ALTERATIONS, ['date-field-altered', HEAD_FIELD_ALTERATION]];
const results = [];
for (const [name, alter] of cases) {
  const altered = alter(text);
  if (name !== 'as committed' && altered === text) { results.push({ case: name, applies: false }); continue; }
  const bytes = new TextEncoder().encode(altered);
  const readGitBlob = (repoRoot, object) => (object === `${head}:${record}` ? bytes.slice() : defaultReadGitBlob(repoRoot, object));
  const evaluation = evaluateBodyReadAuthority(loadBodyReadAuthorityInputs({
    repoRoot: root, governanceRevision: head, evaluationId: `evaluation:probe:${name}`, evaluationInstant: INSTANT, readGitBlob,
  }));
  results.push({ case: name, applies: true, recordSha256: sha256(bytes), admits: evaluation.admits, policy: state(evaluation.policy), consent: state(evaluation.consent), registry: state(evaluation.registry) });
  process.stderr.write(`${name}: admits ${evaluation.admits}, policy ${JSON.stringify(state(evaluation.policy))}\n`);
}

const walk = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(e => (e.isDirectory() ? walk(path.join(dir, e.name)) : [path.join(dir, e.name)]));
const built = DISTS.map(dir => {
  const files = walk(path.join(root, dir)).filter(f => f.endsWith('.js')).map(f => path.relative(root, f)).sort();
  const rows = files.map(f => `${sha256(fs.readFileSync(path.join(root, f)))}  ${f}\n`).join('');
  return { dir, jsFiles: files.length, sha256OfSha256sumListing: sha256(rows) };
});
const document = {
  schema: 'pwb-gate-altered-policy-act-probe/1',
  bead: 'syzygy-bpyt.8.10',
  text: 'Evidence record, not authority: the PWB P1 body-read authority gate evaluated over the screening-scope version 4 act record as committed and with each census alteration. Generated by the script named here; do not edit.',
  script: { path: SCRIPT, sha256: sha256(execFileSync('git', ['-C', root, 'show', `HEAD:${SCRIPT}`])) },
  measuredOn: { commit: head, treeClean: git('status', '--porcelain', '--untracked-files=no') === '', node: process.version, evaluationInstant: INSTANT, built,
    builtNote: 'each dir: the sha256 of a `sha256sum`-format listing (digest, two spaces, path from TREE, newline) of every .js file under it, sorted by path' },
  record: { path: record, sha256: sha256(committed), recordingTag: tag, tagCommit, blobAtTagEqualsHead: git('rev-parse', `${tagCommit}:${record}`) === git('rev-parse', `${head}:${record}`) },
  results,
};
fs.writeFileSync(out, `${JSON.stringify(document, null, 1)}\n`);
