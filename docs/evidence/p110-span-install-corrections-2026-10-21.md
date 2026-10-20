# P-110 span install corrections — syzygy-3sjj

[Observed] This implementation report concerns the span installation authorized by
`.syzygy/governance/decisions/OWNER-DIRECTION-SCREENING-V4-SPAN-INSTALL-2026-10-20.md`.
The frozen policy package, its original review and dispositions, the performed v4
act and its policy bytes are preserved. No guide-name expansion is implemented.
This report grants no authority and records no activation, provider dispatch or
read of an observed repository.

## Governing requirements and record encoding

[Observed] REQ-polaris-generation-025, in the adopted
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
says: “redacted-span SHALL retain permitted surviving evidence at its
otherwise-earned tier with disclosed count, making only claims dependent on
removed spans Unknown.” It also says that existing admission, grammar and policy
gates shall not be widened by generic schema support or fallback.

[Observed] REQ-polaris-generation-033, in the adopted local-agent-mode
specification, requires: “Syzygy SHALL recompute the object identifier of every
commit, tree and blob it reads on the path from the pinned commit to each blob
it uses, from the bytes it read, at every step that uses the object.” A substituted
object's content may not be used, quoted, classified as admitted or rendered.
The existing pinned-object reader still owns commit/tree traversal. The corpus
still re-hashes each original body before screening; the new retained-projection
constructor independently checks that body against the original blob identifier.

[Observed] RFC3-16(c), defined in
`.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`, says:
“It may be performed before or after an A1 mechanism exists; after A1 exists,
the act must explicitly select state (1).” It does not prescribe a literal
record trailer. The existing affirmative v4 trailer records the owner's explicit
selection within this meaning. The correction accepts three complete affirmative
record forms already used in the corpus and refuses denials, quoted examples and
rejected suffixes. It changes no act or predicate meaning. Independent bounded
parser review at `efcbb78f28be88043d8dc3edffa6f153cafff724` is `CONFIRM`;
the full installation still requires its own final review.

## Repairs and review dispositions

| Finding | Disposition and evidence |
|---|---|
| Historical policy successor reversal broke three canonical checks | [Observed] The v4 span successor is included in historical reverse replay. The builder's 37-fixture baseline, registry recorder check and reconciliation selftest passed locally; the final clone must repeat the current canonical commands. Mutant M21 restores the original successor failure inside fixture construction; it is not reported as a completed fixture census. |
| Match work was spent before the class gate, and successful-suffix work was unbounded | [Observed] Ordinary first-match and class/whole-file checks precede overlap collection. Both the 10,000-match limit and summed successful match-length budget exclude the whole body on breach. No partial match list is presented as a complete census. M01–M03 exercise the separate decisions. |
| Preliminary core review at f16 found failed URL searches outside the successful-work budget | [Observed] The exact pinned credential URL pattern and flags use equivalent linear recognition for both first and overlap searches, including retained-text screening. The native oracle covers 1,029 bounded bodies, nested/mixed-case prefixes, delimiter/colon edges and JavaScript whitespace; the same compiled matcher is reused. M04 detects the quadratic native first-search by two actual native calls, not elapsed time; M05 checks grammar. The raw `REVISE` remains unchanged. |
| Emptying mixed CR/LF lines changed line identity | [Observed] Safe original line arrays and original UTF-8 offsets travel with retained material. Check/review/render do not reconstruct source coordinates by splitting concatenated emptied lines. M06 and the literal mixed-ending fixtures cover the failure. |
| Review/check exported intermediates still retained raw excluded bytes | [Observed] `PacketBuild.blobs` and `Derived.admitted` carry only marker text, safe retained lines and original coordinates. Direct assertions inspect both exported intermediates. M07/M08 restore the raw-body assignments and fail those assertions. |
| Preliminary parser review at f16 found affirmative wording inside denial/quotation | [Observed] `efcbb78f` constrains the complete affirmative grammar and includes real-evaluator negatives, including the pre-existing negated legacy form. The independent correction rerun matches all twelve expected probes. M19 restores the unanchored parser and fails executed parser/evaluator tests. |
| Inherited source contained literal regex control endpoints | [Observed] Literal NUL/U+001F endpoints were already present at the handed-back `56a761a3` checkpoint. Their normalization to textual Unicode escapes is inherited textual-encoding cleanup, not a newly introduced regression. |
| Review of the new quotation helper found leading U+FEFF was dropped | [Observed] `1ba0cfdd` preserves BOM bytes in both ordinary and redacted ranges. The new literal assertion failed before repair; M22/M23 separately restore each decoding defect. |
| The fresh verifier compared only redacted rows in a mixed request | [Observed] Independent review at `01acff07` reproduced an ordinary self-hashing replacement reaching the local provider stub despite the fresh pinned corpus. `1cdb7480` binds the complete validated request population to the complete fresh population by cardinality and canonical-key multiset, then uses fresh records. M24–M27 and M30 cover ordinary-row substitution, opaque aliases, exclusion reason, fresh-object use and missing membership. The actual `withConsent` adapter test also refuses extra rows and wrong OIDs with zero provider calls. |
| Inventory source restructuring ceased to match the signed egress derivation | [Observed] The existing classified `context.sources` carrier is restored. Both public-admission and public-egress builders report current without regenerating signed records. M28/M29 independently restore the unclassified carrier and make each builder refuse. |
| The first URL native-call assertion compared a regex's canonical source with unescaped pattern text | [Observed] Rule-6 exposed a surviving native-search mutant at `1ba0cfdd`. Test-only `01acff07` repairs the assertion. Both the surviving log and the later explicit assertion failure remain in the task cache. No production URL code changed in that test correction. |

[Observed] The initial eight retained `R-P110-…-RAW.md` files preserve two preliminary
`REVISE` slices, the parser correction `CONFIRM` slice, the later Important
fresh-population finding and their four probe records byte for byte. They are
bounded evidence for their named subjects, not a final implementation verdict. Original copies and digests remain under
`/home/tze/.cache/syzygy-p110-install-final-review-2026-10-20/`.

## Trusted and untrusted source boundaries

[Observed] Ordinary `GenerationSource` records keep the existing body/blob
identifier check. A redacted projection explicitly distinguishes its marker body
from the original blob. Surviving spans carry both safe-body offsets and original
Git byte/line coordinates. Markers carry no quotation anchor. Full-body and
retained-body digests, policy identity, original extent and withheld-line metadata
are disclosed; no withheld-line digest or withheld raw byte is carried.

[Observed] The gated producer passes its loaded screen capability to
`verifiedRedactedBody`. That constructor re-hashes the original blob, runs the
screen and checks that every retained line and offset agrees with the original
bytes. It returns only safe retained material. Its in-process capability cannot
be minted by JSON. The source factory accepts only that verified projection and
freezes the resulting redacted records. There is no new persistent attestation,
key, trust flag or cache.

[Observed] `validateGenerationSourceTransport` checks the closed transport shape
without granting fidelity. The exported fidelity-bearing validator, quotation
source map, exact-text helper, dossier fidelity evaluator and source-subject
report refuse unverified redacted records. JSON round trips lose the in-process
capability. Pipeline replay requires a fresh verified source population from the
existing `verifySources` port. Both complete populations must validate, have
equal cardinality and match as canonical-key multisets before any stage dispatch.
Ordinary full-body duplicate spans use the same compaction on both sides. Only
validated excluded rows with no body, anchor or object identifier may normalize
their opaque identifier/path aliases; exclusion reasons and multiplicity stay
bound. The pipeline uses the fresh records, retaining only those opaque aliases
needed by the frozen consent population. A bare `true` cannot verify a
redacted request. `screenedRepoCorpusVerifier` repeats policy/admission checks,
original Git reads, blob hashing and screening through the existing gated corpus
path; mismatch or refusal returns false.

[Observed] The concrete forgery falsifiers are an arbitrary safe replacement
body, altered withheld metadata, an altered policy identity, a wrong original
OID, a forged projection passed to the constructor, and JSON presented directly
to a pure consumer. Focused tests refuse them before dispatch. M09–M13 and M18
exercise identity, retained-content, trust and replay decisions separately.
M14–M17 exercise marker output, original offsets, quotation gaps and rendered
surviving spans. The later mixed-population regression uses the actual corpus
reader, fresh verifier and consent adapter against a synthetic pinned repository.
It rejects a self-hashing ordinary secret replacement, a wrong OID, missing and
extra rows, altered retained content and altered exclusion reasons with zero
provider calls. Its positive control accepts both ordinary full-body compaction
and body-free opaque aliases, while substituting fresh branded records.

[Observed] The local-agent path constructs the projection during each existing
fresh pinned-object derivation. Agent-written draft prose in render and close
continues to use the whole-text screen. Pure generic JSON render/evaluation and
preview commands have no exact-source capability; redacted JSON is refused
there. A caller must reconstruct sources through its gated producer before
using those pure consumers. No new source-read fallback is provided.

## Impact-ledger consumer assessment

| Consumer named by the ledger | Assessment |
|---|---|
| Policy act forms, Butlers gate pins, recorder fixtures and current battery | [Observed] The inherited install supplies the fourth act form, successor chain, v4 pins and v4 recorder/check lines. The corrective parser tests include missing/untagged authority refusal. No tag is created in this worker lane. |
| `check_governance.py` copy registration | [Observed] The inherited install registers the existence-gated v4 manifest/record copies. The frozen package and original act bytes are not regenerated. |
| `install_redis_sitting.py` | [Observed] The inherited v4 step requires the complete recorded v4 subject and current consumers, supports idempotent/check modes and refuses partial installation. Its 126-predicate selftest passes locally. It is not run as an installation by this worker. |
| `simulate_redis_sitting.py` | [Observed] The simulator now rehearses only the span row after v3 all, using the exact frozen recorder form and matching owner words. Skip, non-web predecessor and absent predecessor arms do not record. Its synthetic command-capture selftest passes; M20 disables the v4 consumer and fails it. The end-to-end historical sitting simulation is not claimed as run. |
| `check_spec_reconciliation.py` and `build_pwb_behavior_contract_repin.py` | [Observed] Reconciliation uses historical subject replay; the v4 successor correction preserves that replay. The original three canonical failures are specifically covered by the local commands and the final battery. |
| `checkoutPolicyActPort` | [Observed] It already reads the full policy act chain and class act at the current clock. The closed fourth form extends that shared reader; it does not select form zero or trust a policy label. |
| `walkthrough-inputs.ts`, `test-walkthrough-judgment-fixture.ts` | [Observed] These carry the policy path in other-act-bound-artifact populations. Their path identity remains unchanged; no policy-version parser needs alteration. |
| `build_public_source_screening_scope.py` | [Observed] This is the preserved v1 proposal builder. Its patch/check remains relative to its predecessor; current v4 bytes are not its v1 base and its historical proposal is not regenerated. It is not a current install consumer. |
| `build_pwb_behavior_contract_repin_tree_framing.py` | [Observed] It imports the historical replay helpers corrected for v4 and separately reverses its tree-framing patch. Its current check/selftest remain in the canonical battery. |
| `build_pwb_effect_acts_packet.py` | [Observed] Its own documentation distinguishes historical manifest mismatch from its current-byte selftest. The old effect packet stays immutable; current policy validity is decided by the owning later recorder checks. |
| `build_pwb_truth_policy_amendment.py` | [Observed] Its `SUPERSEDED_ROWS` keeps the old policy effect row at the digest offered once the later re-pin act exists. The canonical check preserves historical bytes; v4 is not written into that old packet. |
| `record_public_source_screening_scope_v2_act.py` | [Observed] It is the frozen historical transaction recorder. A later policy does not authorize rewriting its act or replaying it against a different base. Its selftest remains synthetic. |
| `packages/polaris-generation-consent/README.md` and consent ports | [Observed] The README routes through the shared act-chain reader; no reader logic is defined by its older examples. `sourceKey` spreads all metadata and span properties before hashing text, so the new redaction/original-coordinate fields are included in population binding. `withConsent` returns the base verification result after `matches`, retaining a freshly verified population as well as existing boolean refusals. Consent/admit/permitted gates are unchanged. |
| Target body review/check/corpus, provider pipeline, quotation fidelity, dossier evaluation and both renderers | [Observed] These carry only verified retained material, original coordinates, counts and markers. The trust boundaries and falsifiers are above. Complete code gates and the canonical battery still bind only the final integrated clone commit. |

## Evidence and remaining gates

[Observed] Vitest collection over all eight changed test files grew from 253
cases at the handed-back `56a761a3b575f7616a533249834cfa07f8fef16b` to 274 at
`1cdb74805f09d647a9ba42a7dc9db124b53c7709`, a net increase of 21. This
includes the one foreign recorder-template test preserved by reconciliation;
worker additions account for the other twenty. Existing test bodies also gained
literal edge/failure assertions and bounded matrices rather than separate cases.
Both collections and a separate per-file sum agree; this is a collection count,
not a claim that collecting executed those tests. The task cache retains
`test-growth-collection.json`, both collection outputs and command logs.

[Observed] Remote work discovered during implementation is preserved by merge
`3c8e1c00017380d888f7ba25438f32bea9a96ce7`: the foreign correction commits
remain in history, their mutation receipt is unchanged and their recorder-template
parser test is retained. The merge kept the already-verified production and
existing test blobs from `01acff07`; its resolution receipt is retained under
`/home/tze/.cache/syzygy-approved-installs-2026-10-20/p110-remote-reconcile/`.
The later `1cdb7480` production correction is separately named in its mutation
follow-up rather than attributed to that older checkpoint.

[Observed] A byte comparison checked all 17 frozen policy/package/act/review
subjects against the handed-back checkpoint, with no changes. A second comparison
checked all 1,329 tracked `.syzygy/` and `openspec/` files against the reconciled
merge, also with no changes. Independent Git diff checks agree. The original and
signed policy/egress records were not regenerated. The task cache retains the
per-file digests and both comparison outcomes.

[Observed] Local focused checks at the consumer checkpoint passed 434 tests in
twelve files and typecheck; the parser/authority set passed 262 tests. The BOM
correction passed 23 source tests and the final redaction set passed 26 tests.
The complete-population correction passed 75 focused tests across three files
and typecheck; both derived-carried-content builders report current. These sets
overlap and are not added as a total. The exact commands, failures,
mutations and log digests remain under
`/home/tze/.cache/syzygy-3sjj-install-2026-10-20/`.
`p110-span-install-correction-mutations-2026-10-21.json` names the exact
`01acff07c828c1adaaf1bc9c92ba87cb4d4abf2b` subject, source digests and all
23 old/new fragments. Twenty-one Vitest mutants fail executed behavior
assertions, one simulator mutant fails its executed selftest predicate, and the
historical successor mutant restores the canonical fixture-construction refusal.
Its separately named follow-up binds seven mutants to
`1cdb74805f09d647a9ba42a7dc9db124b53c7709`: five fail executed population
behavior assertions and two make the respective carried-content builder refuse.
All 23 original and seven follow-up mutations were restored byte for byte. This
is evidence at two specified checkpoints, not one thirty-mutant final-head run.

[Unknown] The full integrated-head code gates, canonical clean-clone battery,
final independent review, hosted CI, recording tag and private admission remain
pending at this report's preparation. The lead retains responsibility for
integration, push/merge routing, tag and private admission. No claim here treats
a focused check or old-head review as a complete installation approval.

## Final-integration citation correction

[Observed] The first complete clone run at `da08266afda81c1493ab61cc2c870cde3b61f336`
passed the 105 canonical checks and the tag-orientation command. Its full unit
run failed four tests in three files: 4,742 passed and five skipped out of 4,751.
The added pending-register sentence named the policy act in both its link label
and URL, triggering the existing closed policy-record sweep. Independent review
records this Important finding as `REVISE` in
`docs/reviews/R-P110-DOC-POLICY-SWEEP-DA08266A-1-RAW.md`; its seven-probe raw
preserves the isolated cause, both single-occurrence counterexamples and the
unknown-withdrawal refusal. The earlier bounded final-document assessment is
superseded for this issue. The failed full-run receipts remain in the task cache;
they are not treated as a successful final-head run.

[Observed] The correction routes that sentence through the owning
`ACCEPTANCE-ACT-RECORD.md`, retaining the dated approval, existing implementation
direction and historical offering. The policy reader, citation allowlist, act,
policy and implementation are unchanged. All 149 tests in the three affected
files pass on this exact working-text correction; individual assertion counts
agree with the report total. That focused control is not a final-commit battery.
The corrected committed head must receive independent confirmation and repeat
the complete clone and hosted gates before merge.

[Observed] Independent committed-head correction review at
`171e036b969776cb044c00553ad68b6325ccabbf` returns `CONFIRM WITH EXCEPTIONS`
in `docs/reviews/R-P110-CITATION-CORRECTION-171E-1-RAW.md`. The same three
files pass 149/149 tests, and seven actual reader/chain probes preserve both the
restored valid policy chain and unknown-withdrawal refusal. Application/package
code, scripts and the 17 protected subjects remain unchanged. This bounded
confirmation and its probe record are retained verbatim before the complete
corrected-head clone and hosted rerun; final merge attestation remains held.
