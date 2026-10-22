// Guidance byte identity (rev-510): the old brief's computed DOSSIER_GUIDANCE, the old author prompt's cut done here
// independently, and the new constant, each by length and sha256. Usage: node guidance.mjs <old root> <new root>
import { createHash } from 'node:crypto';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';
const [oldRoot, newRoot] = process.argv.slice(2);
const sha = (s) => createHash('sha256').update(s).digest('hex');
const load = (root, rel) => import(pathToFileURL(path.join(root, rel)).href);
const oldBrief = await load(oldRoot, 'packages/polaris-dossier/dist/brief.js');
const newBrief = await load(newRoot, 'packages/polaris-dossier/dist/brief.js');
const oldPrompts = await load(oldRoot, 'packages/polaris-generation-core/dist/prompts.js');
const newPrompts = await load(newRoot, 'packages/polaris-generation-core/dist/prompts.js');
const cut = (prompts) => {
  const p = prompts.promptForStage('author', 'dossier');
  const start = p.system.indexOf('This run produces a dossier:');
  const end = p.system.indexOf(`\n\n${prompts.ILLUSTRATION_HEADING}`);
  return { version: p.version, text: p.system.slice(start, end), systemSha: sha(p.system) };
};
const oc = cut(oldPrompts), nc = cut(newPrompts);
const row = (name, version, text) => ({ name, version, bytes: Buffer.byteLength(text), sha256: sha(text) });
console.log(JSON.stringify([
  row('old brief DOSSIER_GUIDANCE (computed at load)', oldBrief.DOSSIER_GUIDANCE_VERSION, oldBrief.DOSSIER_GUIDANCE),
  row('old author prompt, cut here', oc.version, oc.text),
  row('new brief DOSSIER_GUIDANCE (literal)', newBrief.DOSSIER_GUIDANCE_VERSION, newBrief.DOSSIER_GUIDANCE),
  row('new author prompt, cut here', nc.version, nc.text),
  { name: 'author prompt system unchanged old->new', equal: oc.systemSha === nc.systemSha },
  { name: 'new literal === old computed', equal: newBrief.DOSSIER_GUIDANCE === oldBrief.DOSSIER_GUIDANCE },
  { name: 'other brief exports unchanged', equal: JSON.stringify(Object.keys(oldBrief).sort()) === JSON.stringify(Object.keys(newBrief).sort()), old: Object.keys(oldBrief).length, new: Object.keys(newBrief).length },
], null, 1));
