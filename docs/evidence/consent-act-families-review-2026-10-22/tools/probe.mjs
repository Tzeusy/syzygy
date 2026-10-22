// Reviewer's own counterexample hunt: constructed worlds the PR's corpus lacks, run through both trees' compiled consent readers.
// usage: node probe.mjs <oldTree> <newTree>
import { createHash } from 'node:crypto';
import * as fsp from 'node:fs/promises';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const [oldTree, newTree] = process.argv.slice(2).map(p => path.resolve(p));
const root = oldTree;
const D = '.syzygy/governance/decisions';
const sha = t => createHash('sha256').update(t, 'utf8').digest('hex');

function overlayFs(overlay, dupNames = false) {
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
      const list = [...names];
      return dupNames && rel === D ? [...list, ...list] : list;
    },
    readFile: async file => {
      const rel = path.relative(root, file);
      if (Object.hasOwn(overlay, rel)) { if (overlay[rel] === null) throw Object.assign(new Error(`ENOENT: ${rel}`), { code: 'ENOENT' }); return overlay[rel]; }
      return fsp.readFile(file, 'utf8');
    },
  };
}

const load = async tree => import(pathToFileURL(path.join(tree, 'packages/polaris-generation-consent/dist/index.js')).href);
const [oldC, newC] = [await load(oldTree), await load(newTree)];
if (oldC === newC) throw new Error('both trees resolved to one module');
const NOW = Date.parse('2026-10-22T12:00:00Z');
const answer = async read => { try { return JSON.stringify(await read()); } catch (e) { return `throws ${e?.name}: ${e?.message}`; } };
const readersOf = c => [
  ['admission', (fs) => c.createPackageAdmissionReader({ root, fs }).read()],
  ['policy-reader', (fs) => c.createPackagePolicyReader({ root, fs }).read()],
  ['policy-chain', (fs) => c.readPolicyActChain({ root, fs, now: NOW })],
  ['class-act', (fs) => c.readClassActState({ root, fs, now: NOW })],
  ['in-force-egress', (fs) => c.readInForceEgress({ root, fs, now: NOW })],
  ['registry', (fs) => c.readDigestBoundActState({ root, fs, now: NOW, form: c.REGISTRY_GIT_SOURCE_ACT_FORM })],
  ['signoff', (fs) => c.readVersionedSignoffState({ root, fs, now: NOW, form: c.LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM })],
];
const short = a => (a.startsWith('throws') ? a : (() => { const v = JSON.parse(a); return Array.isArray(v) ? `array(${v.length})` : v.state ? `${v.state}${v.why ? ': ' + v.why.slice(0, 90) : ''}` : 'value'; })());

const read = rel => fs.readFileSync(path.join(root, rel), 'utf8');
const policyV1 = `${D}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`;
const policyV4 = `${D}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V4-ACT.md`;
const classAct = `${D}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`;
const redisAct = `${D}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`;
const histAct = `${D}/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`;
const agg = `${D}/ACCEPTANCE-ACT-RECORD.md`;
const POLICY = oldC.POLICY_PATH;
const MODULE = '.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md';
const v1Id = /^Act identity: `([^`\n]+)`$/m.exec(read(policyV1))[1];

const WORLDS = [];
const add = (name, overlay, opts = {}) => WORLDS.push({ name, overlay, ...opts });
add('base', {});
for (const [lab, sp] of [['tab', 'Act\tidentity'], ['nbsp', 'Act identity'], ['ideographic', 'Act　identity'], ['bom', 'Act﻿identity'], ['ls', 'Act identity'], ['fullwidth', 'Ａｃｔ identity']]) {
  add(`label-${lab}-policy-id`, { [`${D}/ZZ.md`]: `${sp}: ${v1Id}\n` });
  add(`label-${lab}-class-module`, { [`${D}/ZZ.md`]: `${sp}: ${MODULE}\n` });
  add(`label-${lab}-policy-path-agg`, { [agg]: `${read(agg)}\n${sp}: ${POLICY}\n` });
}
add('quoted-artifact-policy-path-agg', { [agg]: `${read(agg)}\n> Artifact identity: \`${POLICY}\`\n` });
add('recordid-policy-path-agg', { [agg]: `${read(agg)}\nRecord ID: ${POLICY}\n` });
add('subject-class-module-agg', { [agg]: `${read(agg)}\nSubject: ${MODULE}\n` });
add('recordid-class-stem-agg', { [agg]: `${read(agg)}\nRecord ID: rfc5-project-documentation\n` });
add('quoted-recordid-admission-agg', { [agg]: `${read(agg)}\n> Record ID: PUBLIC-OBS-REDIS-2026-10-03\n` });
add('bold-bullet-star-policy', { [`${D}/ZZ.md`]: `* **Act identity:** ${v1Id}\n` });
add('double-quote-policy', { [`${D}/ZZ.md`]: `>> Act identity: ${v1Id}\n` });
add('name-REVOKE-upper-sub', { [`${D}/sub/PWB_SECRET_CLASSIFICATION_POLICY_REVOKE.md`]: '# x\n' });
add('name-withdraw-nostem', { [`${D}/PWB-SECRET-WITHDRAW.md`]: '# x\n' });
add('policy-v1-copy-sub', { [`${D}/archive/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`]: read(policyV1) });
add('policy-hist-copy-sub', { [`${D}/archive/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`]: read(histAct) });
add('redis-act-copy-sub', { [`${D}/archive/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`]: read(redisAct) });
add('class-act-copy-sub', { [`${D}/archive/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`]: read(classAct) });
add('hist-edited', { [histAct]: `${read(histAct)} ` });
add('hist-edited-and-naming-file', { [histAct]: `${read(histAct)} `, [`${D}/AA.md`]: 'public-source-scope\n' });
add('policy-v4-bad-and-naming-file', { [policyV4]: read(policyV4).replace(/^Date: /m, 'Date:  '), [`${D}/ZZ.md`]: 'public-source-scope\n' });
add('policy-v1-bad-and-hist-edited', { [policyV1]: read(policyV1).replace(/^Date: /m, 'Date:  '), [histAct]: `${read(histAct)} ` });
add('class-bad-and-module-gone', { [classAct]: read(classAct).replace(/^Date: /m, 'Date:  '), [MODULE]: null });
add('class-act-type-cap', { [classAct]: read(classAct).replace(/^Act type: `contract-amendment`$/m, 'Act type: `Contract-Amendment`') });
add('class-date-invalid', { [classAct]: read(classAct).replace(/^Date: \d{4}-\d{2}-\d{2}$/m, 'Date: 2026-02-30').replace(/^(Act instant): (\S+)$/m, (_, l, v) => `${l}: 2026-02-30${v.slice(10)}`) });
add('policy-v1-date-feb29-nonleap', { [policyV1]: read(policyV1).replace(/^Date: \d{4}-\d{2}-\d{2}$/m, 'Date: 2026-02-29') });
add('policy-file-not-json', { [POLICY]: '{not json' });
add('policy-file-not-json-and-naming', { [POLICY]: '{not json', [`${D}/ZZ.md`]: 'public-source-scope\n' });
add('decisions-dup-readdir', {}, { dup: true });
add('decisions-dup-readdir-naming', { [`${D}/ZZ.md`]: `${MODULE}\n` }, { dup: true });
add('admission-supersession-dup', { [redisAct]: read(redisAct).replace(/^(Supersession \/ revocation: .*)$/m, '$1\n\n$1') });
add('class-recorder-lines-gone', { [classAct]: read(classAct).replace(/^Owner: .*\n/m, '').replace(/^A1 audit-record identity.*\n/m, '') });
add('policy-quoted-agg-act-id', { [agg]: `${read(agg)}\n> Act identity: ${v1Id}\n` });
add('policy-quoted-file-act-id', { [`${D}/ZZ.md`]: `> Act identity: ${v1Id}\n` });
add('policy-file-artifact-stem-only', { [`${D}/ZZ.md`]: 'Artifact identity: pwb-secret-classification-policy\n' });
add('policy-file-recordid-stem', { [`${D}/ZZ.md`]: 'Record ID: pwb-secret-classification-policy\n' });

let mismatches = 0, n = 0;
const vectors = new Set();
for (const w of WORLDS) {
  const fsx = overlayFs(w.overlay, w.dup === true);
  const outs = [];
  for (const [[name, oldRead], [, newRead]] of readersOf(oldC).map((r, i) => [r, readersOf(newC)[i]])) {
    const a = await answer(() => oldRead(fsx)), b = await answer(() => newRead(fsx));
    n += 1;
    if (a !== b) { mismatches += 1; console.log(`MISMATCH ${w.name} ${name}\n  old: ${a.slice(0, 300)}\n  new: ${b.slice(0, 300)}`); }
    outs.push(`${name}=${short(a)}`);
  }
  vectors.add(outs.join('|'));
  console.log(`${w.name}: ${outs.join('; ')}`);
}
console.log(`${WORLDS.length} worlds, ${n} answers compared, ${mismatches} mismatches, ${vectors.size} distinct short-label vectors`);
