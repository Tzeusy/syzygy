// Export surfaces (rev-510): every exported name (value or type) of each public entry, by the TypeScript checker over src, plus
// runtime identity of /live bindings against the root. Usage: node exports.mjs <repo root> <out.json>
import { createRequire } from 'node:module';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';
const [root, out] = process.argv.slice(2);
const require = createRequire(path.join(root, 'package.json'));
const ts = require('typescript');
const entries = {
  'core .': 'packages/polaris-generation-core/src/index.ts',
  'core ./live': 'packages/polaris-generation-core/src/live.ts',
  'app ./dossier-render': 'apps/three-surface-poc/src/polaris-generation/dossier-render.ts',
  'app ./dossier-site': 'apps/three-surface-poc/src/polaris-generation/dossier-site.ts',
  'consent .': 'packages/polaris-generation-consent/src/index.ts',
  'consent consent-ports': 'packages/polaris-generation-consent/src/consent-ports.ts',
  'dossier .': 'packages/polaris-dossier/src/index.ts',
  'core provider-draft': 'packages/polaris-generation-core/src/provider-draft.ts',
  'core dossier-evaluation': 'packages/polaris-generation-core/src/dossier-evaluation.ts',
  'dossier brief': 'packages/polaris-dossier/src/brief.ts',
  'app draft-preview': 'apps/three-surface-poc/src/polaris-generation/draft-preview.ts',
  'core local-render': 'packages/polaris-generation-core/src/local-render.ts',
};
const files = Object.values(entries).map(f => path.join(root, f)).filter(f => fs.existsSync(f));
const program = ts.createProgram(files, { module: ts.ModuleKind.NodeNext, moduleResolution: ts.ModuleResolutionKind.NodeNext, target: ts.ScriptTarget.ES2022, strict: true, skipLibCheck: true, noEmit: true });
const checker = program.getTypeChecker();
const result = {};
for (const [name, rel] of Object.entries(entries)) {
  const sf = program.getSourceFile(path.join(root, rel));
  if (!sf) { result[name] = null; continue; }
  const sym = checker.getSymbolAtLocation(sf);
  const names = checker.getExportsOfModule(sym).map(s => {
    const target = s.flags & ts.SymbolFlags.Alias ? checker.getAliasedSymbol(s) : s;
    const value = !!(target.flags & ts.SymbolFlags.Value);
    return `${s.name}${value ? '' : ' (type)'}`;
  }).sort();
  result[name] = names;
}
const coreRoot = await import(pathToFileURL(path.join(root, 'packages/polaris-generation-core/dist/index.js')).href);
let identity = null;
if (fs.existsSync(path.join(root, 'packages/polaris-generation-core/dist/live.js'))) {
  const live = await import(pathToFileURL(path.join(root, 'packages/polaris-generation-core/dist/live.js')).href);
  const keys = Object.keys(live);
  identity = { liveRuntimeNames: keys.length, sameObject: keys.filter(k => live[k] === coreRoot[k]).length, differ: keys.filter(k => live[k] !== coreRoot[k]) };
  const site = await import(pathToFileURL(path.join(root, 'apps/three-surface-poc/dist/polaris-generation/dossier-site.js')).href);
  const render = await import(pathToFileURL(path.join(root, 'apps/three-surface-poc/dist/polaris-generation/dossier-render.js')).href);
  identity.renderReexportsSame = { DossierRenderError: render.DossierRenderError === site.DossierRenderError, sourceRoute: render.sourceRoute === site.sourceRoute };
  identity.pageSinkContracts = { renderDossier: render.renderDossier.pageSinkContract, renderLocalDossier: site.renderLocalDossier.pageSinkContract };
}
fs.writeFileSync(out, JSON.stringify({ result, identity, rootRuntimeNames: Object.keys(coreRoot).length }, null, 1));
console.log(JSON.stringify(Object.fromEntries(Object.entries(result).map(([k, v]) => [k, v === null ? null : v.length]))), JSON.stringify(identity), Object.keys(coreRoot).length);
