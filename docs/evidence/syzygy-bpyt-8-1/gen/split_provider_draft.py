"""Split provider-draft.ts (base bytes) into closed-schema.ts, draft-model.ts and the slimmer provider-draft.ts by line range.
Usage: split_provider_draft.py <base provider-draft.ts> <core src dir>. Every moved line is copied from the base; only the
listed renames, `export` prefixes and the new headers/import lines are written by hand."""
import re, sys, pathlib
base = pathlib.Path(sys.argv[1]).read_text().split('\n')
out = pathlib.Path(sys.argv[2])
L = lambda a, b: base[a - 1:b]          # 1-based inclusive
def one(n, expect):
    line = base[n - 1]
    assert line.startswith(expect), (n, line[:60], expect)
    return line
RENAMES = [('ProviderParagraph', 'DraftParagraph'), ('ProviderBlockSupport', 'FidelityBlockSupport'), ('ProviderBlock', 'DraftBlock'),
           ('ProviderDiagramNode', 'DraftDiagramNode'), ('ProviderDiagramEdge', 'DraftDiagramEdge'), ('ProviderDiagram', 'DraftDiagram'),
           ('ProviderDraft', 'DossierDraft'), ('ProviderInventoryCoverage', 'FidelityInventoryCoverage'), ('ProviderReview', 'FidelityReview')]
def rename(lines):
    res = []
    for line in lines:
        for old, new in RENAMES: line = re.sub(rf'\b{old}\b', new, line)
        res.append(line)
    return res
def export(line, name):
    assert line.startswith(f'const {name}') or line.startswith(f'function {name}'), line[:40]
    return 'export ' + line

# closed-schema.ts: the Schema type (10-15), the primitive parts (28-32) and check (84-124)
assert base[9].startswith('type Schema =') and base[14].startswith('  | { oneOf')
assert base[83].startswith('function check(') and base[123] == '}'
closed = ["import { types } from 'node:util';", "import { SOURCE_ID_MAX_LENGTH, SOURCE_ID_MIN_LENGTH, SOURCE_ID_PATTERN } from './source-model.js';", '',
  '// One closed-schema checker and one handle, shared by the dossier draft model',
  '// (draft-model.ts), the provider stage schemas (provider-draft.ts) and the',
  '// rendered-design review (rendered-design.ts). A schema here admits plain',
  '// strings only: markup-looking text stays inert, and renderers must escape it.',
  'export ' + base[9], *L(11, 15), '',
  '// The string parts declare their arm: importers spread an `enum` into them, and an imported const keeps its declared type.',
  # An imported const keeps its declared type (no narrowing by initializer across modules), so the string parts declare the string arm
  # their importers spread an `enum` into.
  export(one(28, 'const text: Schema =').replace('const text: Schema =', "const text: Extract<Schema, { type: 'string' }> ="), 'text'),
  export(one(29, 'const handle: Schema =').replace('const handle: Schema =', "const handle: Extract<Schema, { type: 'string' }> ="), 'handle'),
  export(one(30, 'const list'), 'list'),
  export(one(31, 'const object'), 'object'), export(one(32, 'const refs'), 'refs'), '',
  'export ' + base[83], *L(85, 124), '']
(out / 'closed-schema.ts').write_text('\n'.join(closed))

# draft-model.ts
assert base[32].startswith('const requestedAssetsSchema') and base[33].startswith('const paragraph') and base[37].startswith('const block')
assert base[38].startswith('const epistemic') and base[39].startswith('export const DIAGRAM_KINDS') and base[40].startswith('const disposition')
assert base[44] == '] };' and base[47].startswith('const draft = object({') and base[58] == '});'
assert base[59].startswith('const inventoryCoverage') and base[60].startswith('const blockSupport') and base[61].startswith('const fidelity') and base[63] == '});'
assert base[125].startswith('export interface ProviderParagraph') and base[136].startswith('  | { kind: \'unresolved\'')
assert base[137].startswith('export interface ProviderInventory ') and base[138].startswith('export interface ProviderPlan ')
assert base[139].startswith('export interface ProviderDraft {') and base[153].startswith('export interface ProviderReview ')
assert base[155].startswith('function unique(') and base[159] == '}'
assert base[175].startswith('export function validateRequestedAssets(') and base[180] == '}'
assert base[182].startswith('/** Every block of a tree') and base[185] == '}'
assert base[250].startswith('function draftHandles(') and base[256] == '}'
assert base[357] == '/**' and base[362].startswith('export function validateDraftRecord(') and base[371] == '}'
assert base[373].startswith('export function reviewVerdict(') and base[382] == '}'
assert base[384].startswith('/** Mermaid string text') and base[389] == '}'
assert base[391] == '/**' and base[398].startswith('export function diagramToMermaid(') and base[416] == '}'
model = ["import { check, handle, list, object, refs, text, type Schema } from './closed-schema.js';", '',
  '// The dossier draft model: the draft both the provider pipeline and an operator-agent run render, the fidelity',
  '// review of it, and the requested assets it answers. Intermediate records only: they neither mint identities nor',
  '// implement the authored asset bundle, source admission or semantic review. Coverage lists record what the reviewer',
  '// claims to have checked; they cannot prove entailment or inventory completeness beyond the source denominator.',
  '// Plain strings remain inert, including markup-looking text; renderers must escape them. This schema provides no',
  '// executable markup or external link role.', '',
  base[32], base[33], *L(35, 38), base[38], base[39],
  '/** Package-internal (with `draft` and `fidelity`): the provider stage schemas in provider-draft.ts embed it. */',
  export(base[40], 'disposition'), *L(42, 45),
  export(base[47], 'draft'), *L(49, 59), base[59], base[60], export(base[61], 'fidelity'), *L(63, 64), '',
  *rename(L(126, 137)), *rename(L(140, 154)), '',
  '/** Package-internal, with `treeBlocks` and `draftHandles`: `validateStage` (provider-draft.ts) shares them. */',
  export(base[155], 'unique'), *L(157, 160), '',
  *rename(L(176, 181)), '',
  base[182], export(rename([base[183]])[0], 'treeBlocks'), *rename(L(185, 186)), '',
  export(rename([base[250]])[0], 'draftHandles'), *rename(L(252, 257)), '',
  *rename(L(358, 372)), '', *rename(L(374, 383)), '', *L(385, 390), '', *rename(L(392, 417)), '']
(out / 'draft-model.ts').write_text('\n'.join(model))

# provider-draft.ts: what stays, importing what moved and re-exporting it under the provider names
assert base[1].startswith("import type { DiscoveryStage") and base[2] == '' and base[3].startswith('// Provider-local') and base[8].startswith('// escape them.')
assert base[45].startswith('const inventory = ') and base[46].startswith('const plan = ')
assert base[64].startswith('/** Bounds a discovery claim') and base[76].startswith('const schemaVersions') and base[77] == ''
assert base[78].startswith('export function stageSchema(') and base[81] == '}'
assert base[160].startswith('function same(') and base[173] == '}'
assert base[187].startswith('function draftBlocks(') and base[249] == '}'
assert base[258].startswith('/** Case-folded') and base[349] == '}'
assert base[351].startswith('/** Closed-schema primitives') and base[355].startswith('export const schemaParts')
assert base[418] == '/**' and base[433] == '}'
provider = [base[1],
  "import { check, handle, list, object, refs, text, type Schema } from './closed-schema.js';",
  "import { disposition, draft, draftHandles, fidelity, treeBlocks, unique, validateRequestedAssets, type AssetDisposition, type DossierDraft, type DraftBlock, type DraftDiagram,",
  "  type DraftDiagramEdge, type DraftDiagramNode, type DraftParagraph, type FidelityBlockSupport, type FidelityInventoryCoverage, type FidelityReview, type RequestedAsset } from './draft-model.js';",
  "import { SOURCE_TEXT_MAX_LENGTH } from './source-model.js';",
  '', *L(4, 9),
  '// The draft and review records, and the closed-schema checker every stage shares, live in draft-model.ts and',
  '// closed-schema.ts (the live dossier path imports them there); this module re-exports them under the names the',
  '// provider pipeline uses.',
  "export { SOURCE_ID_MAX_LENGTH, SOURCE_ID_MIN_LENGTH, SOURCE_ID_PATTERN, SOURCE_TEXT_MAX_LENGTH } from './source-model.js';",
  "export { DIAGRAM_KINDS, diagramToMermaid, reviewVerdict, validateDraftRecord, validateRequestedAssets, type AssetDisposition, type DiagramKind, type EpistemicMarking, type RequestedAsset } from './draft-model.js';",
  'export type ProviderParagraph = DraftParagraph;', 'export type ProviderBlock = DraftBlock;', 'export type ProviderDiagramNode = DraftDiagramNode;',
  'export type ProviderDiagramEdge = DraftDiagramEdge;', 'export type ProviderDraft = DossierDraft;', 'export type ProviderDiagram = DraftDiagram;',
  'export type ProviderInventoryCoverage = FidelityInventoryCoverage;', 'export type ProviderBlockSupport = FidelityBlockSupport;', 'export type ProviderReview = FidelityReview;', '',
  base[45], base[46], *L(65, 78), *L(79, 82), '',
  base[137], base[138], '',
  *L(161, 174), '',
  *L(188, 250), '',
  *L(259, 350), '',
  *L(352, 356), '',
  *L(419, 434), '']
(out / 'provider-draft.ts').write_text('\n'.join(provider))
