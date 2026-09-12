# Generator RFC5/6/8/9 consequence reconciliation

Candidate coverage evidence, not approved specification coverage, effective N/A,
implementation proof or complete independent contract decomposition.

The companion JSON preserves 565 prior locator units: RFC5 115, RFC6 71,
RFC8 105 and RFC9 274. Current installed source digests and every locator quote
were checked. Two methods agree: whitespace-normalized clause/lettered-limb
matching and independent whitespace-regex matching against the current module.
The 565 clause/key pairs are distinct. Requirement text, scenario names and
support-document hashes are retained separately from consequence rows.

Prior consequence paraphrases are locators, not authority. For example the old
RFC5-15 absent/invalid-consent paraphrase is broader than the new requirement's
correct distinction between absent permission and an invalid purported act.
Read the current clause and normative requirement rather than adopting that
legacy paraphrase. Reconciliation does not invent a unique test per sentence;
a scenario plus explicit normative/support text can cover several consequences.

## Directly mapped behavior

| Contract consumers | Candidate requirements and support | Evidence limit |
|---|---|---|
| RFC5 principal/client/session/machine admission and exposure | 021; SECURITY-CONTRACT and EFFECT-HOST-DESIGN | Actual protected host/browser tests remain unperformed |
| RFC5 consent, egress classification, ingest/exclusion | 001/016/022/025; SOURCE-POLICY | Separate actual project/provider/policy acts still required |
| RFC5 audit, adapter credential isolation and revocation | 022; EFFECT-HOST-DESIGN | Recorder trust boundary is specified, not provisioned or verified |
| RFC6 selections, resolution, URL/context and return paths | 026; NAVIGATION-CONTRACT | Actual end-to-end navigation remains unimplemented |
| RFC6 shared facts, complete drawer, aggregation and machine parity | 027; NAVIGATION-CONTRACT | Single-view smoke tests would not prove the full tuple |
| RFC8 scheduler ownership, materialization and lifecycle | 013/020; OWNER-FLOW | Existing POC demonstration is not established as reusable implementation |
| RFC8 normalized work and paired chain fields | 028; WORK-STATE-CONTRACT and EXECUTION-PHASES | Unsupported profile case refuses admission; no-signal predicate remains unimplemented |
| RFC8 history, retention, fidelity, joins and independent measures | 011/018/029; WORK-STATE-CONTRACT | No live telemetry/reconciliation computation authority is implied |

The JSON's 247 candidate-mapping rows are traceability proposals with exact
requirement/scenario/support references, not 247 independent implementation
passes. No exact approved reusable generator or computed-embed implementation
was established in this bounded review; approvedReuse is therefore null. This
is not a global claim that the repository has no useful implementation.

## Concrete remaining changes

1. **External machine-auth mechanism:** EFFECT-HOST-DESIGN specifies scoped
   credentials/verifiers but does not choose the external CLI mechanism from
   RFC5-7. Its recorder peer-credential protocol answers another interface.
   Select a permitted mechanism explicitly (for example per-client random bearer
   tokens over loopback, hashed server-side), and bind the request transport and
   refusal scenario to it. Preserve attended issuance and distinct browser mode.

2. **Indeterminate state plane:** RFC8-1 requires a work item whose plane cannot
   be determined to remain counted and render Unknown. NAVIGATION-CONTRACT's
   known-plane identity field alone does not specify this failure behavior.
   Add the explicit outcome to requirement 013 or 027 and a scenario with an
   indeterminate-plane item: retained, countable, visibly Unknown and no guessed
   plane. Do not add a new kernel plane or turn the receipt into observed truth.

3. **Computed visual capability boundary:** 270 non-phase RFC9 consequences
   remain conditional computed-asset obligations. ASSET-CONTRACT correctly
   refuses unsupported embeddings, but its general inheritance sentence is not
   per-consequence support evidence. State which computed visual kinds the first
   renderer actually offers and map that selection's consumer/renderer boundary.
   A supported embed needs its exact source renderer/evaluation/registry/legend,
   geography and applicable nonvisual/interaction evidence. If the first version
   supports no computed embed, explicitly reject that kind and retain unresolved
   requested assets; obtain the applicable reviewed scope disposition instead
   of implying support. Meaningful curated architecture/workflow diagrams remain
   required where useful and are not a request to implement full Orrery.

4. **Small explicit scope dispositions:** 25 RFC5 observed-code launcher/profile
   units, one RFC6 workspace selection unit and seven RFC8 personal-intake/
   inherited-incidental-work units need precise consumer applicability. The
   generator prohibits observed-code execution and does not presently introduce
   personal idea/milestone intake or incidental inherited work. Record those
   exact non-consumed consequences for review; do not build new sandbox/fleet
   features merely to satisfy an overbroad inherited locator. Imported execution
   record/profile fidelity, own-provider cancellation and actual work provenance
   remain required. If any of these behaviors is offered, its predicate applies.

The 13 phase-gate units are approval/coverage deliverables; they are not runtime
features and this report is not their owner act. The existing RFC7 workspace/
portfolio N/A proposal does not automatically dispose of other contract units.

## Staging conclusion

The repaired Phase A/B/C separation can proceed through actual approval without
waiting for unsupported normalized-work mappings to be implemented in pure
mechanics. The final owner flow, supported live profile, two real projects and
meaning-changing source regeneration remain mandatory. Refusing every real run
or computed asset required by a proving case cannot establish completion.

Review source: `docs/evidence/polaris-generator-rfc5-6-8-9-coverage-2026-09-12.json`.
