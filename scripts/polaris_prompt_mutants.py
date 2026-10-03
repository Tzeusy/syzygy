"""Rule-6 mutant runner for the Polaris prompt and discovery modules (AGENTS.md verification rule 6). Usage, from a clean checkout of the
commit under test: python3 scripts/polaris_prompt_mutants.py OUT.json

Before every mutant: restore every subject from its committed bytes, check
each subject's sha256, and run the unmutated battery, which must pass. Then
replace exactly one occurrence of `old` with `new` (refused unless it occurs
once), run the battery, and restore and re-check every subject. Killed means
the run exited non-zero with at least one failed test. OUT.json carries the
commit, subject and test digests, and each mutant's old/new fragment."""
import json, subprocess, sys, hashlib, re, os
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C='packages/polaris-generation-core/src/'
P=C+'prompts.ts'
D=C+'provider-draft.ts'
V=C+'discovery-provider.ts'
I=C+'index.ts'
TESTS=[C+'dossier-prompts.test.ts',C+'prompts.test.ts',C+'discovery-provider.test.ts',C+'provider-draft.test.ts']
M=[
 # Dossier rules and guidance (instruction bytes).
 (P,'rule-7-unnumbered',"\n7. Thin evidence stays Unknown. Where","\nThin evidence. Where"),
 (P,'rule-5-unnumbered',"\n5. Comparisons. Report","\nComparisons. Report"),
 (P,'rule-6-unnumbered',"\n6. Marked inference. A block","\nMarked inference. A block"),
 (P,'rule-4-paraphrase-allowed',"keeping the link text; no other change is allowed.","keeping the link text; small wording changes are allowed."),
 (P,'rule-4-normalization-dropped'," A quotation matches its source when the two are identical after every run of whitespace, line breaks included, is collapsed to one space and markdown emphasis and link syntax are dropped, keeping the link text; no other change is allowed.",""),
 (P,'rule-4-inferred-as-stated-allowed'," Never present an inferred cost or benefit as stated.",""),
 (P,'rule-4-inferred-unbounded',"may be written as one Inferred: sentence citing the sources of the mechanism it reasons from, and it must agree with every cited source; otherwise it is unresolved","may be inferred"),
 (P,'rule-5-extension-allowed',"Never extend or generalize it, and never add an alternative of your own.","Never extend or generalize it."),
 (P,'rule-6-restatement-dropped'," A faithful restatement or summary of cited sources and child blocks is not inference and carries no prefix.",""),
 (P,'rules-govern-line-dropped'," Where these dossier rules and the instructions above differ, the dossier rules govern.",""),
 (P,'rules-say-maintainers',"the advantages the project's sources claim","the advantages the maintainers claim"),
 (P,'guidance-word',"never by rewording it to sound stated.","never by rewording it."),
 (P,'fidelity-quote-check-dropped',"that every quotation is one contiguous span of a cited source, matching it under rule 4's normalization, with no ellipsis or splice; ",""),
 (P,'fidelity-inferred-half-dropped',"no trade-off half is presented as stated unless a cited source states it, and that an Inferred: half cites the sources it reasons from and agrees with every one of them;","no trade-off half is presented as stated;"),
 (P,'guidance-shared',"  edit: `Dossier edit: never turn","  edit: `Dossier repair: never turn"),
 # The dossier base: named substitutions of the manifesto framing.
 (P,'base-name-kept',"'You are producing one stage of a project-neutral Polaris dossier pipeline.'","'You are producing one stage of a project-neutral Polaris manifesto pipeline.'"),
 (P,'base-adopted-intent-kept',"' Generated content is an editorial draft.'","' Generated content is editorial draft, not adopted intent.'"),
 (P,'base-owner-approval-kept',"\" or accept the author's self-assessment as evidence.\"","\", accept the author's self-assessment as evidence, or grant owner approval.\""),
 (P,'inventory-manifesto-kept',"'Do not draft or plan the dossier,'","'Do not draft or plan the manifesto,'"),
 (P,'author-manifesto-kept',"'Write a coherent, concise dossier following'","'Write a coherent, concise manifesto following'"),
 (P,'replace-once-unchecked',"  if (text.split(from).length !== 2) throw new Error('prompt-derivation');\n",""),
 # Illustrations obey the rules.
 (P,'adv-paraphrased-in-quotes',"which makes large sites build faster than rendering one page at a time.\"';","so large sites build faster than rendering one page at a time.\"';"),
 (P,'trade-off-paraphrased',"rebuilds every page that uses it.\"';","rebuilds the pages that use it.\"';"),
 (P,'inventory-adv-unquoted',"statement: ADVANTAGE, kind: 'other'","statement: 'Pages render in parallel worker threads.', kind: 'other'"),
 (P,'inferred-cost-unmarked',"const INFERRED_COST = 'Inferred: every build","const INFERRED_COST = 'Every build"),
 (P,'inferred-cost-cites-stated-source',"block('b-cost-inferred', INFERRED_COST, ['src-build', 'src-cache'])","block('b-cost-inferred', INFERRED_COST, ['src-readme'])"),
 (P,'inferred-cost-entry-dropped',"  { id: 'e-cost-inferred', sourceIds: ['src-build', 'src-cache'], statement: INFERRED_COST, kind: 'qualification', disposition: produced('trade-offs') },\n",""),
 (P,'dive-unmarked',"block('b-dive', 'Inferred: a build","block('b-dive', 'A build"),
 (P,'restatement-marked-inferred',"block('b-mech', '`renderPage` looks","block('b-mech', 'Inferred: `renderPage` looks"),
 (P,'hop-merged',"\n      leaf('b-flow-2', 'Once every page has rendered, `buildSite` calls `writeOutput`.', 'src-build'),",""),
 (P,'identifier-respelled',"block('b-mech', '`renderPage` looks","block('b-mech', '`render_page` looks"),
 (P,'inventory-identifier-respelled',"calls `writeOutput` once every page has rendered.', kind: 'capability'","calls `write_output` once every page has rendered.', kind: 'capability'"),
 (P,'gap-filled-inventory',"disposition: { kind: 'unresolved', reason: 'No admitted source shows how the output is served.', references: ['src-build'] } },","disposition: produced('end-to-end-workflows') },"),
 (P,'gap-dropped-draft',"unresolved: [{ question: 'How is the built site served?', reason: 'No admitted source shows how the output is served.', references: ['src-build'] }],","unresolved: [],"),
 (P,'edge-label-not-in-text',"label: 'hands each page to', sourceIds","label: 'passes pages to', sourceIds"),
 (P,'edge-cited-outside-flow',"label: 'hands each page to', sourceIds: ['src-build']","label: 'hands each page to', sourceIds: ['src-cache']"),
 (P,'diagram-kind',"kind: 'flow', relationship","kind: 'dependency', relationship"),
 (P,'plan-required-section-dropped',"  sectionPlan('mechanisms', 'The render cache', 'Answers the mechanisms question from e-cache and explains the term source hash (e-term); a deep dive answers when a build is finished.', ['src-cache', 'src-build']),\n",""),
 (P,'review-coverage-row-dropped',"represented('e-adv', 'b-adv'), ",""),
 (P,'review-gap-represented',"{ entryId: 'e-serve', disposition: 'unresolved'","{ entryId: 'e-serve', disposition: 'justified-omission'"),
 # Stage wiring and freezing.
 (P,'edit-illustration-swapped',"  inventory: inventoryIllustration, plan: planIllustration, author: draftIllustration, edit: draftIllustration,","  inventory: inventoryIllustration, plan: planIllustration, author: draftIllustration, edit: planIllustration,"),
 (P,'repair-illustration-cloned',"fidelity: reviewIllustration, repair: draftIllustration,\n});","fidelity: reviewIllustration, repair: structuredClone(draftIllustration),\n});"),
 (P,'edit-json-wrong-stage',"  edit: JSON.stringify(draftIllustration), fidelity:","  edit: JSON.stringify(planIllustration), fidelity:"),
 (P,'freeze-dropped',"    Object.freeze(value);\n",""),
 (P,'freeze-shallow',"    for (const child of Object.values(value)) deepFreeze(child);\n",""),
 (P,'sources-unfrozen',"export const DOSSIER_ILLUSTRATION_SOURCES = deepFreeze([","export const DOSSIER_ILLUSTRATION_SOURCES = (["),
 (P,'discovery-unfrozen',"export const DISCOVERY_STAGE_ILLUSTRATIONS: Readonly<Record<DiscoveryStage, unknown>> = deepFreeze({","export const DISCOVERY_STAGE_ILLUSTRATIONS: Readonly<Record<DiscoveryStage, unknown>> = ({"),
 (P,'json-at-call-time',"${ILLUSTRATION_HEADING}\\n${dossierIllustrationJson[generation]}","${ILLUSTRATION_HEADING}\\n${JSON.stringify(DOSSIER_STAGE_ILLUSTRATIONS[generation])}"),
 (I,'index-export-readded',"  promptForStage, ILLUSTRATION_HEADING,","  promptForStage, ILLUSTRATION_HEADING, DOSSIER_STAGE_ILLUSTRATIONS,"),
 (P,'version-bumped',"version: `polaris-${generation}-dossier-v2`","version: `polaris-${generation}-dossier-v3`"),
 (P,'base-prefix-dropped',"system: `${dossierCommon}\\n\\n${dossierInstructions[generation]}\\n\\n${dossierRules}","system: `${dossierRules}"),
 (P,'illustration-heading',"Copy its structure, never its content, handles or claims;","Copy its structure;"),
 (P,'profile-guard-removed',"  if (profile !== 'manifesto' && profile !== 'dossier') throw new Error('unknown-prompt-profile');\n",""),
 (P,'default-profile-dossier',"profile: PromptProfile = 'manifesto'","profile: PromptProfile = 'dossier'"),
 # #336 re-review: rule 4's explicit clauses, guidance and the corrected illustration.
 (P,'rule-4-elision-allowed',"Quote that span exactly: never elide, splice or add ellipses, and keep","Quote that span, and keep"),
 (P,'rule-4-span-unbounded',"one contiguous span of a cited source, at most two sentences or one list item.","a passage from a cited source."),
 (P,'rule-4-backticks-in-quotes',"identifiers included, without adding backticks.","with identifiers in backticks."),
 (P,'rule-4-double-quotes-anywhere'," Double quotes are used only for such a quotation; everywhere else put commands, identifiers, configuration keys and values in backticks and use no quotation marks.",""),
 (P,'rule-4-advantage-restated'," Quote a stated advantage once: child blocks may explain its mechanism in your own words, citing their sources, but never restate the claim unquoted.",""),
 (P,'rule-4-unstated-advantage-inferable'," An advantage no source states is never written, not even as Inferred:.",""),
 (P,'rule-4-inferred-may-contradict',", and it must agree with every cited source; otherwise",", otherwise"),
 (P,'rule-3-quotes-backticked',"3. Mechanisms. Outside a quotation, name each","3. Mechanisms. Name each"),
 (P,'inventory-term-dropped'," each project-specific or domain term a newcomer would need explained as a term entry;",""),
 (P,'inventory-motives-kept',"'thesis, motives, capabilities', 'thesis, capabilities'","'thesis, motives, capabilities', 'thesis, motives, capabilities'"),
 (P,'plan-order-dropped',": core ideas first, then the end-to-end workflows, then the mechanisms beneath them, then advantages and trade-offs, so each section builds on the last.",", in an order that lets each section build on the last."),
 (P,'author-intro-dropped',"open with a two- or three-sentence introduction that says what the project is and how its central workflow runs, never a copy of the first section's block. ",""),
 (P,'author-glossary-dropped',"Explain each term a newcomer may not know at its first use, in one clause its sources support. ",""),
 (P,'author-scare-quotes-allowed'," Double quotes appear only around a verbatim span of a cited source after The project states:; identifiers, commands, configuration keys and values go in backticks, and there are no scare quotes.",""),
 (P,'author-refusals-unreconciled'," The trade-offs section is a requested section that gathers the costs, not the canned refusals section the instructions above rule out: beside any advantage a trade-off qualifies, keep a one-clause pointer to it.",""),
 (P,'edit-ellipsis-allowed'," shorten it with an ellipsis, add double quotes around anything but a verbatim span of a cited source,",""),
 (P,'fidelity-advantage-check-dropped',"that a stated advantage is quoted once and never restated unquoted, and that no advantage is written that no source states; ",""),
 (P,'fidelity-no-finding-dropped',"; a block with no failure needs no finding.","."),
 (P,'repair-quote-wording-dropped',"for a quotation that does not match its source, quote it verbatim from a cited source, or remove the quotation marks and mark the sentence Inferred: (an advantage no source states is removed instead). ",""),
 (P,'inferred-cost-contradicts-readme',"Inferred: every build looks up each page\\'s source hash in the cache, even when nothing has changed, because","Inferred: a page whose own source is unchanged is not rendered again and can go stale, because"),
 (P,'intro-copies-first-block',"'Brindle builds documentation sites from Markdown. A build hands each page to `renderPage`, which skips a page whose source is unchanged, then writes the output once every page has rendered.'","'Brindle builds documentation sites from Markdown.'"),
 (P,'term-entry-dropped',"  { id: 'e-term', sourceIds: ['src-cache'], statement: 'Source hash: the value `renderPage` looks up in the cache to decide whether a page must be rendered again.', kind: 'term', disposition: produced('mechanisms') },\n",""),
 (P,'review-praise-finding',"  findings: [],","  findings: [{ severity: 'advisory', message: 'The inferred cost is marked.', target: 'b-cost-inferred' }],"),
 (P,'adv-restated-unquoted',"block('b-mech', '`renderPage` looks up the page\\'s source hash in the cache and skips rendering when the hash is unchanged.'","block('b-mech', '`renderPage` looks up the page\\'s source hash in the cache and skips rendering when the hash is unchanged, so large sites build faster.'"),
 (P,'scare-quote-in-block',"leaf('b-flow-1', '`buildSite` reads the content directory","leaf('b-flow-1', '`buildSite` reads the \"content\" directory"),
 # Discovery prompts.
 (P,'map-relevance-out-of-range',"relevance: 9 },","relevance: 11 },"),
 (P,'map-unknown-blob',"{ blobId: 'blob-build', claim:","{ blobId: 'blob-other', claim:"),
 (P,'map-duplicate-blob',"{ blobId: 'blob-build', claim:","{ blobId: 'blob-readme', claim:"),
 (P,'reduce-illustration-duplicate',"ranked: ['blob-readme', 'blob-build', 'blob-cache']","ranked: ['blob-readme', 'blob-build', 'blob-readme']"),
 (P,'map-instruction-word',"Claim only what the excerpt shows, never what the rest of the file might hold.","Claim what the file holds."),
 (P,'map-code-points-dropped',"at most 400 characters (Unicode code points)","at most 400 characters"),
 (P,'map-sources-dropped'," (these usually live in a README, CHANGELOG, design document or architecture decision record)",""),
 (P,'map-comparison-dropped',"purpose, advantage, comparison or trade-off","purpose, advantage or trade-off"),
 (P,'reduce-instruction-word',", choosing only among the blobIds the claims name.","."),
 (P,'reduce-comparisons-dropped',"For advantages, comparisons and trade-offs prefer","For advantages and trade-offs prefer"),
 (P,'map-version-unbumped',"'discovery-map': 'polaris-discovery-map-v3'","'discovery-map': 'polaris-discovery-map-v2'"),
 (P,'reduce-version-unbumped',"'discovery-reduce': 'polaris-discovery-reduce-v2' }","'discovery-reduce': 'polaris-discovery-reduce-v1' }"),
 (P,'discovery-instructions-swapped',"{ 'discovery-map': mapInstructions, 'discovery-reduce': reduceInstructions }","{ 'discovery-map': reduceInstructions, 'discovery-reduce': mapInstructions }"),
 # The quotation check in code lives in quote-fidelity.ts (single checker); its mutants are in docs/evidence/quote-fidelity-mutants-2026-10-04.json.
 # Schemas and reply validation.
 (D,'reduce-schema-version',"'discovery-map': 'v1', 'discovery-reduce': 'v1' };","'discovery-map': 'v1', 'discovery-reduce': 'v2' };"),
 (D,'schema-map-blob-unpatterned',"  blobId: handle, claim: { type: 'string', minLength: 1, maxLength: DISCOVERY_CLAIM_MAX_LENGTH },","  blobId: text, claim: { type: 'string', minLength: 1, maxLength: DISCOVERY_CLAIM_MAX_LENGTH },"),
 (D,'schema-map-maxitems',"}), 0, 200) });\nconst discoveryReduce","}), 0, 2000) });\nconst discoveryReduce"),
 (D,'schema-reduce-unique-dropped',"const discoveryReduce = object({ ranked: { ...list(handle, 0, 200), uniqueItems: true } });","const discoveryReduce = object({ ranked: list(handle, 0, 200) });"),
 (D,'claim-max-raised',"DISCOVERY_CLAIM_MAX_LENGTH = 400;","DISCOVERY_CLAIM_MAX_LENGTH = 4000;"),
 (D,'relevance-max-raised',"DISCOVERY_RELEVANCE_MAX = 10;","DISCOVERY_RELEVANCE_MAX = 11;"),
 (D,'relevance-min-lowered',"relevance: { type: 'number', minimum: 0, maximum","relevance: { type: 'number', minimum: -1, maximum"),
 (D,'number-min-unchecked',"!(value >= schema.minimum && value <= schema.maximum)","!(value <= schema.maximum)"),
 (D,'number-type-unchecked',"if (typeof value !== 'number' || !(value >=","if (!(value >="),
 (D,'number-exclusion-form',"!(value >= schema.minimum && value <= schema.maximum)","(value < schema.minimum || value > schema.maximum)"),
 (D,'reply-stage-guard',"  if (stage !== 'discovery-map' && stage !== 'discovery-reduce') throw new Error('invalid-stage');\n  check(schemas[stage], value);","  check(schemas[stage], value);"),
 (D,'reply-duplicates',"  unique(ids);\n  if (ids.some","  if (ids.some"),
 (D,'reply-unknown-blob',"  if (ids.some(id => !candidates.has(id))) throw new Error('unknown-blob');\n",""),
 (D,'reply-over-selection',"ids.length > call.maxSelected!)) throw new Error('over-selection');","ids.length > call.maxSelected! + 1)) throw new Error('over-selection');"),
 # Envelope, snapshot and request validation.
 (V,'envelope-wrong-prompt',"  const prompt = promptForStage(stage);\n  const schema = stageSchema(stage);","  const prompt = promptForStage('discovery-map');\n  const schema = stageSchema(stage);"),
 (V,'envelope-wrong-schema',"  const prompt = promptForStage(stage);\n  const schema = stageSchema(stage);","  const prompt = promptForStage(stage);\n  const schema = stageSchema('discovery-map');"),
 (V,'map-candidates-widened',"{ candidateIds: mapSnapshot(request).candidateIds }","{ candidateIds: [...mapSnapshot(request).candidateIds, 'blob-other'] }"),
 (V,'reduce-candidates-widened',"{ candidateIds, maxSelected: inputs.maxSelected }","{ candidateIds: [...candidateIds, 'blob-unclaimed'], maxSelected: inputs.maxSelected }"),
 (V,'reduce-cap-widened',"maxSelected: inputs.maxSelected }, 'invalid-reduce-reply')","maxSelected: inputs.maxSelected + 1 }, 'invalid-reduce-reply')"),
 (V,'reduce-cap-reread',"maxSelected: inputs.maxSelected }, 'invalid-reduce-reply')","maxSelected: request.maxSelected }, 'invalid-reduce-reply')"),
 (V,'map-item-spread',"return { blobId: item.blobId as unknown, path: item.path as unknown, excerpt: item.excerpt as unknown };","return { ...item };"),
 (V,'reduce-claim-spread',"return { blobId: claim.blobId as unknown, path: claim.path as unknown, claim: claim.claim as unknown, relevance: claim.relevance as unknown };","return { ...claim };"),
 (V,'reduce-entry-spread',"return { subsystem: entry.subsystem as unknown, blobs: entry.blobs as unknown, claims };","return { ...entry, claims };"),
 (V,'map-envelope-reread',"items: inputs.items });","items: request.items });"),
 (V,'reduce-envelope-reread',"subsystems: inputs.subsystems });","subsystems: request.subsystems });"),
 (V,'map-request-duplicates',"  if (!distinct(candidateIds)) fail();\n  return { inputs: { subsystem","  return { inputs: { subsystem"),
 (V,'map-request-empty-items',"items === undefined || items.length === 0) return fail();","items === undefined) return fail();"),
 (V,'map-request-empty-subsystem',"if (!isText(subsystem) ||","if (typeof subsystem !== 'string' ||"),
 (V,'reduce-request-max-zero',"maxSelected < 1","maxSelected < 0"),
 (V,'reduce-request-no-claims',"if (candidateIds.length === 0 || !distinct(candidateIds)) fail();","if (!distinct(candidateIds)) fail();"),
 (V,'reduce-request-duplicates',"if (candidateIds.length === 0 || !distinct(candidateIds)) fail();","if (candidateIds.length === 0) fail();"),
 (V,'reduce-claim-length-unchecked',"isText(value) && [...value].length <= DISCOVERY_CLAIM_MAX_LENGTH","isText(value)"),
 (V,'reduce-claim-utf16-length',"[...value].length <= DISCOVERY_CLAIM_MAX_LENGTH","value.length <= DISCOVERY_CLAIM_MAX_LENGTH"),
 (V,'reduce-claim-empty-allowed',"const isClaimText = (value: unknown): value is string => isText(value) &&","const isClaimText = (value: unknown): value is string => typeof value === 'string' &&"),
 (V,'reduce-relevance-low',"value >= 0 && value <= DISCOVERY_RELEVANCE_MAX","value >= -1 && value <= DISCOVERY_RELEVANCE_MAX"),
 (V,'reduce-relevance-high',"value <= DISCOVERY_RELEVANCE_MAX;","value <= DISCOVERY_RELEVANCE_MAX + 1;"),
 (V,'reduce-relevance-type-unchecked',"value is number => typeof value === 'number' && value >= 0","value is number => (value as number) >= 0"),
 (V,'reduce-relevance-exclusion-form',"typeof value === 'number' && value >= 0 && value <= DISCOVERY_RELEVANCE_MAX;","typeof value === 'number' && !(value < 0 || value > DISCOVERY_RELEVANCE_MAX);"),
]
PAIR={}
byid={m[1]:m for m in M}
files=sorted({m[0] for m in M}); 
def sh(f): return hashlib.sha256(open(W+'/'+f,'rb').read()).hexdigest()
commit=subprocess.check_output(['git','-C',W,'rev-parse','HEAD'],text=True).strip()
assert subprocess.check_output(['git','-C',W,'status','--porcelain','--',*files,*TESTS],text=True)=='', 'subjects or tests dirty'
origs={f:open(W+'/'+f).read() for f in files}; base={f:sh(f) for f in files}
def restore():
  for f,o in origs.items(): open(W+'/'+f,'w').write(o)
  for f in files: assert sh(f)==base[f], f'restore failed {f}'
def run():
  r=subprocess.run(['npx','vitest','run',*TESTS],cwd=W,capture_output=True,text=True)
  txt=re.sub(r'\x1b\[[0-9;]*m','',r.stdout+r.stderr)
  m=re.search(r'Tests\s+(.*?)\((\d+)\)',txt)
  failed=int(re.search(r'(\d+) failed',m.group(1)).group(1)) if m and 'failed' in m.group(1) else 0
  return r.returncode,failed,int(m.group(2)) if m else 0,sorted(set(re.findall(r'FAIL .*?> (.*)',txt)))  # every failed test, untruncated
out=[]
try:
  for f,mid,old,new in M:
    restore()
    rc,failed,total,_=run()
    assert rc==0 and failed==0 and total>0, f'baseline not green before {mid}: rc={rc} failed={failed} total={total}'
    edits=[(f,old,new)]+([(byid[PAIR[mid]][0],byid[PAIR[mid]][2],byid[PAIR[mid]][3])] if mid in PAIR else [])
    cur={g:origs[g] for g in files}; ok=True
    for g,o,n in edits:
      if cur[g].count(o)!=1: ok=False; print(mid,'NOT APPLIED',cur[g].count(o)); break
      cur[g]=cur[g].replace(o,n)
    if not ok: out.append({'file':f,'id':mid,'old':old,'new':new,'outcome':'not-applied'}); continue
    for g in files:
      if cur[g]!=origs[g]: open(W+'/'+g,'w').write(cur[g])
    rc,failed,total,names=run()
    killed=rc!=0 and failed>0
    rec={'file':f,'id':mid,'old':old,'new':new}
    if mid in PAIR: rec['alsoApplied']={'id':PAIR[mid],'file':byid[PAIR[mid]][0],'old':byid[PAIR[mid]][2],'new':byid[PAIR[mid]][3]}
    rec.update({'outcome':'killed' if killed else 'survived','baselineGreen':True,'failedTests':failed,'totalTests':total,'killedBy':names})
    out.append(rec); restore()
    print(mid,'killed' if killed else 'SURVIVED',failed,names[:2],flush=True)
finally:
  restore()
json.dump({'commit':commit,'subjects':base,'tests':{t:sh(t) for t in TESTS},'mutants':out},open(sys.argv[1],'w'),indent=2)
