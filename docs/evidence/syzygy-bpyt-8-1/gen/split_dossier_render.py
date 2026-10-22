"""Split dossier-render.ts (its bytes at origin/main 0d4d5098) into dossier-site.ts (the pages every run shares, and the operator-agent entry) and a
dossier-render.ts that keeps the provider-run view and the XOR entry. Usage: split_dossier_render.py <dossier-render.ts at 0d4d5098> <dir>.
Every moved line is copied from the base; only the listed renames and the hand-written heads, signatures and seams differ."""
import re, sys, pathlib
base = pathlib.Path(sys.argv[1]).read_text().split('\n')
out = pathlib.Path(sys.argv[2])
L = lambda a, b: base[a - 1:b]
def at(n, expect):
    assert base[n - 1].startswith(expect), (n, base[n - 1][:70], expect)
    return base[n - 1]
RENAMES = [('ProviderParagraph', 'DraftParagraph'), ('ProviderBlock', 'DraftBlock'), ('ProviderDiagram', 'DraftDiagram'), ('ProviderDraft', 'DossierDraft'),
           ('View', 'DossierView'), ('Stop', 'DossierStop')]
def rename(lines):
    res = []
    for line in lines:
        for old, new in RENAMES: line = re.sub(rf'(?<![\w.]){old}(?![\w])', new, line)
        res.append(line)
    return res
def replace_once(line, old, new):
    assert line.count(old) == 1, (line[:80], old)
    return line.replace(old, new)

# --- anchors in the input bytes
at(1, "import { createHash }"); at(3, "import { DESIGN_TOKENS_CSS }"); at(11, "import { renderDiagramSvg }"); at(14, "import { assertInertSvg }")
at(16, '/**'); at(17, ' * Multi-page static dossier (gap #8) from the pipeline\'s final output. It'); at(55, ' *'); at(56, ' * A stopped run')
at(65, ' * entry page names'); at(66, ' *'); at(67, ' * An operator-agent run'); at(76, ' * policy state, and the source pages'); at(77, ' * the disclosure stay. A provider run'); at(79, ' */')
at(81, '// Test seam: exported type the tests name'); at(82, 'export interface DossierRenderInput {'); at(93, '}'); at(95, 'interface RenderedDossier {'); at(110, '// Test seam: exported for the tests'); at(134, '}')
at(136, 'type StopReason'); at(148, '}'); at(150, 'interface Stop {'); at(151, 'interface View {'); at(157, '}')
at(159, 'const DRAFT_STAGES'); at(163, '};'); at(165, '/** The renderable view of a result'); at(166, 'function viewOf('); at(198, '}')
at(200, 'export function renderDossier('); at(201, '  const { result, local } = input;'); at(202, '  if ((result === undefined) === (local === undefined))')
at(203, '  const view: View = result !== undefined'); at(204, '    : { draft: local!.draft'); at(205, '  const { draft, stop } = view;')
at(215, '  const quoteFlags = new Map'); at(216, '  if (result !== undefined) {'); at(217, '    for (const finding of [...(result.status'); at(220, '  }')
at(472, '  return { files, manifest };'); at(473, '}'); at(474, '/** The encoding half'); at(476, 'renderDossier.pageSinkContract = PAGE_SINK_CONTRACT;')

site_doc = [base[15], ' * Multi-page static dossier (gap #8), from the view of a run: a provider pipeline\'s final output (`dossier-render.ts` builds',
  ' * its view) or an operator-agent run\'s inputs (`renderLocalDossier`). It', *L(18, 55), *L(67, 76),
  ' * the disclosure stay.', ' *',
  ' * This module imports nothing from the parked provider island, so the `syzygy` CLI, which injects `renderLocalDossier` into the',
  ' * dossier render step, never loads it (`packages/polaris-generation-core/src/island-boundary.test.ts`).', base[78]]
site = [base[0], '', base[2], '', 'import {',
  '  DOSSIER_FORMAT, OWNER_TOPICS, PAGE_SINK_CONTRACT, checkDraftQuotes, diagramToMermaid, isDossierPagePath, parseDossierManifest, readerCost, reviewVerdict, scanDossierPage, sourceTextById, withoutReviewStatusRegion,',
  '  generationSpanRange, validateGenerationSources,',
  '  type DossierDraft, type DossierManifest, type DraftBlock, type DraftDiagram, type DraftParagraph, type EpistemicMarking, type GenerationSource, type LocalPageItem,',
  '  type LocalRenderInput, type LocalSegment, type OwnerTopic, type QuoteFinding,',
  "} from '@syzygy/polaris-generation-core/live';", *L(11, 14), '', *site_doc, '',
  'export ' + base[94], *L(96, 135),
  'export ' + rename([base[149]])[0],
  '/** What a run\'s pages render from: its draft and what its pipeline recorded about it. An operator-agent run records nothing beyond',
  ' * its draft (`localView`). */',
  'export ' + rename([base[150]])[0], *rename(L(152, 156)),
  '  /** The pipeline\'s quotation findings, checked again here against the draft; null for an operator-agent run, whose labels are the',
  '   * caller\'s. */',
  '  readonly quoteFindings: readonly QuoteFinding[] | null;',
  base[156], '',
  '/** What every run\'s pages share: the source population, and the owner topics by draft id. */',
  'interface DossierSiteInput {', *L(87, 90), '}', '',
  '/** What `renderLocalDossier` takes: an operator-agent run\'s inputs, which `packages/polaris-dossier` derives at its render step. */',
  'interface LocalDossierRenderInput extends DossierSiteInput {', '  readonly local: LocalRenderInput;', '}', '',
  '/** An operator-agent run\'s view: its checked draft, and nothing a provider pipeline\'s stages record. */',
  'export const localView = (local: LocalRenderInput): DossierView => ({',
  '  draft: local.draft, drafted: true, review: null, inventory: null, stop: null, deferredSections: new Set(), notGenerated: [], quoteFindings: null,',
  '});', '',
  '/** Every file of a run\'s site from its view. `local` is present exactly for an operator-agent run. */',
  'export function renderDossierSite(input: DossierSiteInput & { readonly local?: LocalRenderInput }, view: DossierView): RenderedDossier {',
  '  const { local } = input;',
  *rename(L(205, 214)),
  base[214],
  '  if (view.quoteFindings !== null) {',
  replace_once(base[216], "...(result.status === 'awaiting-rendered-review' && Array.isArray(result.quoteFindings) ? result.quoteFindings : [])", '...view.quoteFindings'),
  *L(218, 220),
  *rename(L(221, 473)), '',
  '/** An operator-agent run\'s site: what the `syzygy` CLI injects into the dossier render step. */',
  'export function renderLocalDossier(input: LocalDossierRenderInput): RenderedDossier {',
  '  return renderDossierSite(input, localView(input.local));',
  '}',
  base[473], base[474], 'renderLocalDossier.pageSinkContract = PAGE_SINK_CONTRACT;', '']
(out / 'dossier-site.ts').write_text('\n'.join(site))

# --- dossier-render.ts: the provider-run view and the XOR entry
view_of = rename(L(165, 198))
i_ready = next(i for i, l in enumerate(view_of) if l.startswith('    return { draft: validateDraftRecord(result.draft)'))
view_of[i_ready] = replace_once(view_of[i_ready], 'notGenerated: [] };', 'notGenerated: [],\n      quoteFindings: Array.isArray(result.quoteFindings) ? result.quoteFindings : [] };')
i_last = next(i for i, l in enumerate(view_of) if l.startswith('  return { draft, drafted: draftAt >= 0'))
view_of[i_last] = replace_once(view_of[i_last], 'notGenerated };', 'notGenerated, quoteFindings: [] };')
render = ["import { PAGE_SINK_CONTRACT, validateDraftRecord, validateRequestedAssets, type DossierDraft, type GenerationSource, type LocalRenderInput, type OwnerTopic, type PipelineResult, type RequestedAsset } from '@syzygy/polaris-generation-core';",
  "import { DossierRenderError, localView, renderDossierSite, type DossierStop, type DossierView, type RenderedDossier } from './dossier-site.js';", '',
  '// The `./dossier-render` subpath keeps every name it exported before the renderer moved to `dossier-site.ts`.',
  "export { DossierRenderError, sourceRoute } from './dossier-site.js';", '',
  '/**', ' * The multi-page dossier (`dossier-site.ts`) from the generation pipeline\'s final output, complete or stopped.', ' *',
  *L(56, 65), ' *',
  ' * An operator-agent run\'s inputs (`local`, syzygy-qkea.10) render here exactly as `renderLocalDossier` renders them. The `syzygy`',
  ' * CLI injects that function itself, so it never loads this module or the provider island it imports. A provider run\'s output is',
  ' * unchanged (`dossier-render-provider-golden.test.ts`).', ' */', '',
  *L(81, 93), '',
  *L(136, 148), '',
  *L(159, 163), '',
  *view_of, '',
  base[199], base[200], base[201],
  '  return renderDossierSite(input, result !== undefined ? viewOf(input, result) : localView(local!));',
  '}', *L(474, 476), '']
(out / 'dossier-render.ts').write_text('\n'.join(render))
