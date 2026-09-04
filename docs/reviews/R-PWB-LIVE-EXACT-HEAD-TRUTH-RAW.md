# Raw review — PWB live exact-head truth and spec reconciliation

Review date: 2026-09-05

Review mode: focused `project-review` spec reconciliation plus veracity gate,
using the historical, non-authoritative review prompt
`_bootstrap/review-prompts/01_GENERIC_COHERENCE_AND_ADVERSARIAL.md`; it was
not used as project authority.

Exact subject: Syzygy `cd6c95250772d98c199020c08e25476fbe34bb5b`

Observed project: Butlers
`a3dd1fe08a1d9a11b5e899e0ecf33f03d8eefc96`

Live daemon: process cwd `/home/tze/GitHub/syzygy`, loopback
`127.0.0.1:7478`, tailnet mount `/butlers-syzygy`, with the daemon and both
repositories independently confirmed at the two revisions above.

## Scope and authority boundary

- [Observed] The current PWB spec, design, and proposal bytes match the
  eleven-artifact amended sign-off digests in
  `.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md:65-82`.
- [Observed] The three effect artifacts match the exact SHA-256 values in
  their 2026-09-02 acts. The live model evaluates consent, policy, and registry
  as valid state (1), and exposes the required same-tree-forgeability
  disclosure.
- [Observed] This review read Butlers bodies only from the authorized
  `declared-project-shape-text` population. The independent reference sweep
  used exactly 263 such paths and no implementation-file body.
- [Observed] The supplied shape scan reports all five pillars present and a
  repository assessment of `SHAPED`; the generic mechanical spec tracer is
  inapplicable to the signed pre-ID/Source/Scope spec format and is not treated
  as a PWB finding.
- [Observed] Twenty focused current-head test files pass: 627/627 tests. That
  evidence is useful but does not override the exact live counterexamples
  below.

## PASS

- [Observed] Both real ingresses work against the same daemon: loopback human,
  tailnet human, loopback authenticated machine, and tailnet authenticated
  machine requests each returned HTTP 200. Tailnet navigation links carry the
  `/butlers-syzygy` mount prefix.
- [Observed] PWB-REQ-005's current state-(1) admission path is present. The
  current 213-test authority suite covers the eight valid triples and the
  closed invalid population; live output preserves all three exact states and
  never calls state (1) independently verified.
- [Observed] The live human and machine bytes contain zero matches for all four
  approved secret-detector families and zero occurrences of the exact machine
  credential. This is a detector-bounded result, not proof that an unknown
  secret form cannot exist.
- [Observed] The exact-object reader rejects traversal, non-blob objects, bad
  encodings, unsafe schemes, and active forms; the corresponding current-head
  tests pass. No observed-project code is executed by the PWB observer.
- [Observed] The mechanical PWB-REQ-012 copy contract passes: the current copy
  table and rendered fixture variants have one declared role per text node,
  bounded headings and ledes, and none of the prohibited meta-terms. The live
  usability failure belongs to PWB-REQ-021, not to an invented PWB-REQ-012
  word-count failure.
- [Observed] All 298 live fragment links resolve to exactly one DOM id and the
  document has no duplicate ids. A scan over the independently enumerated 263
  authorized Butlers sources found zero references that cite Polaris or
  `/api/poc` as authority.
- [Observed] PWB-REQ-022's currently applicable absent arm is honest: no run
  record exists, and both channels report `no-run-record` and
  `unknown-never-met` without fabricating a verdict.

## Bidirectional reconciliation

The signed file defines 16 requirements whose identifiers span
PWB-REQ-001…022. Identifiers 008, 009, and 017…019 are not requirements in the
signed artifact; their absence is not counted as an implementation gap.

| Requirement | Coverage | Spec → implementation and exact live behavior | Implementation → spec divergence |
|---|---|---|---|
| PWB-REQ-001 | **Partial** | Exact revision, capture instant, policy/observer identities, manifest digest, and source stamps exist. The live source population is incomplete: 256 instead of the independently enumerated 263 existing declared paths. | Root discovery is narrowed to Markdown link-target basenames, a rule the signed source-population definition does not state. |
| PWB-REQ-002 | **Partial** | Fixture extraction exists, but the live path-defined baseline-spec denominator is reported Unknown with only 76 of 183 identities modeled. | Body classification is made a prerequisite even for the `baseline-spec` class whose identity is defined wholly by Git-tree path. |
| PWB-REQ-003 | **Partial** | Excluded bodies stay in the source table and detector-bounded sink scans are clean. One post-parse exclusion is absent from the exclusion list/count, so the denominator does not reconcile. | Classification counts are captured before extraction can convert a classified source into a parse-failure exclusion. |
| PWB-REQ-004 | **None in production** | The exact Butlers revision has the spec's own 8-versus-9 domain-butler conflict, but live output says zero contradictions and zero rules. | Production supplies no source-derived declarations or precedence rules; only tests inject them. The signed universal fact population is not closed. |
| PWB-REQ-005 | **Full for the current state-(1) path** | All three exact authorities admit and remain separately disclosed. Invalid/valid fixture and mutation coverage is present. | No contrary live behavior found. |
| PWB-REQ-006 | **Partial** | Exact Git containment and inert-output guards exist. The live machine answer is 4,645,644 bytes against `maxRenderedBytes=2,097,152`, with no recorded breach; parse-time and rendered-output limits have no production enforcement. | The raw-text active-content scanner also treats inert Markdown code-span syntax as an HTML tag and excludes the whole source. |
| PWB-REQ-007 | **Partial** | Tuple fields, reason routes, challenge state, and evaluation identity are present. Four missing classes nevertheless claim Observed denominator zero with empty support. | The implementation treats absence from its already-incomplete manifest as evidence of factual absence. |
| PWB-REQ-010 | **Partial** | The seven group headings occur in the required order before capability detail. Purpose, promises, refusals, architecture, V1 scope/success, and the capability catalog are not actually presented from existing authority. | A static sentence calls the catalog complete in every model state, including the live Unknown/incomplete state. |
| PWB-REQ-011 | **Partial** | Summary/catalog/detail links exist, but every source link terminates at an in-page metadata row; no exact authoritative artifact or verbatim leaf is reachable. | Tests redefine “exact source” as a path/identity/digest row, weaker than the signed artifact/leaf requirement. |
| PWB-REQ-012 | **Full for its mechanical contract** | The exact finite role/word/term/cardinality rules pass. | The roughly 12,064-word rendered-text dump remains a PWB-REQ-021 comprehension problem; it is not evidence of a mechanical copy-rule violation. |
| PWB-REQ-013 | **Partial** | The active proposal is confined to capability detail and visibly subordinate. Its existing baseline authority is misreported as `missing-declaration` rather than `excluded-content`. | `deriveCurrentAuthority` searches modeled items only and does not distinguish a missing path from a present-but-excluded source. |
| PWB-REQ-014 | **Partial** | Human narrative units carry roles, typed anchors, non-citable/presentation attributes; live downstream-authority sweep is zero. The authenticated machine endpoint omits the narrative blocks and attributes. | The “machine form” is embedded only in human HTML and is explicitly excluded from `/api/poc`. |
| PWB-REQ-015 | **Partial** | Three bands and Base-mode order exist. Live contract detail contains no verbatim current requirement/scenario, doctrine, or non-goal text, and the band machine form is absent from the machine endpoint. | The current requirement exists at the exact revision but is lost because its harmless inline-code placeholder triggers whole-body active-content exclusion. |
| PWB-REQ-016 | **Partial** | Native controls, text labels, valid fragment targets, and prior fixture-browser evidence exist. The exact-source path stops at metadata, and the mandatory live nonvisual/keyboard cold-open record is absent. | The prepared walkthrough schedule admits non-Polaris routes despite RFC7-30/PWB-REQ-021's Polaris-only boundary. |
| PWB-REQ-020 | **Partial** | Raw project-model claim markers match between the rendered fixture and serialized model. The complete narrative/band/non-citability machine representation is not served by `/api/poc`, and internally inconsistent denominators are duplicated rather than corrected. | Current parity tests compare `renderPolarisPage(model)` with `JSON.parse(JSON.stringify(model))`; they do not prove that the authenticated endpoint carries the presentation artifact. |
| PWB-REQ-021 | **None / not met** | The supplied owner observation says the current walkthrough was aborted as unusable. No lawful run record or answer set exists. | The live entry is 1,069,549 bytes and produces a roughly 12,064-word rendered-text dump; its DOM contains 302 anchors, 10 disclosure summaries, and 5 explicitly focusable regions. Structural counts cannot substitute for the owner criterion. |
| PWB-REQ-022 | **Full for absence; partial for readiness** | Absence correctly stays Unknown-never-met, and the invalid-act evaluator is extensive. The prepared expectation is still `not-yet-recorded` and is not bound to the live evaluation identity. | The loader accepts any nonempty subset of five routes, including Trajectory/Orrery/materialize, and parses no answer population. |

## FINDINGS

### 1. BLOCKER — the manifest omits the entire declared Heart and Soul source population

Classification: **implementation defect**. Veracity: **[Confirmed]**.

[Observed] PWB-REQ-001 closes the source population over the five roots named
by Butlers' root index and the files named by each pillar index
(`spec.md:10-14,69-96`). At the exact Butlers revision, `about/README.md:15-21`
names Heart and Soul's directory as `about/heart-and-soul/` and its start file
as `heart-and-soul/vision.md`; `about/heart-and-soul/README.md:8-17` names six
pillar files.

[Observed] `project-shape-manifest.ts:333-342` looks only at Markdown link
targets and accepts a root only when the target basename is itself one of the
five pillar keys (or the target is a `README.md` under such a basename). The
real root index does not link Heart and Soul's README. The fixture instead
uses invented directory links for all five pillars
(`test-project-shape-fixture.ts:83-100`), so it cannot falsify the real shape.

[Observed] Independent exact-revision enumeration gives 263 existing source
paths: 56 root/pillar-index/named files, 183 baseline specs, and 24 roster
files. The live machine result exposes 256: 49 `about/**`, 183 baseline specs,
24 roster files, and zero Heart and Soul paths. The exact seven-path delta is
the Heart and Soul README plus its six indexed files.

[Observed] The consequence is not merely degraded coverage. Live Polaris
renders all six project-account statements Unknown as `missing-declaration`,
claims Observed denominator zero for project-account sections, principles,
success criteria, and catalog entries with zero supporting anchors, and still
states: “This is one capability within the complete catalog above.” PWB-REQ-010
and VIS-1 do not permit an incomplete manifest to become a confident complete
catalog.

Why it matters: the front door cannot answer why Butlers exists, what it
refuses, how it is built, what V1 ships, or what its capability groups are.
This directly reproduces the product failure the signed PWB change exists to
repair and makes PWB-REQ-021 impossible to pass honestly.

Minimum precise fix: parse the actual root index's declared pillar rows and
directory column at the exact revision; add a real-Butlers exact-head oracle
whose independently enumerated source set includes the seven Heart and Soul
paths; make zero/absence claims depend on a complete manifest and anchor them
to that manifest; condition or remove the static “complete catalog” sentence
when completeness is Unknown.

Supporting evidence: signed `spec.md:10-14,69-96,466-489`; exact Butlers
`about/README.md:15-21,83-94`; exact Butlers
`about/heart-and-soul/README.md:8-17`; implementation
`project-shape-manifest.ts:333-407`; live source groups `49 + 183 + 24 = 256`
with `heart_paths=[]`; independent authorized set `263`.

Contradictory evidence checked: the 18 manifest tests and the broader 627-test
focused suite pass; the fresh-checkout evidence explicitly reports Heart and
Soul Unknown. Those checks use the synthetic directory-link fixture and
therefore do not contradict the exact live omission. Spec and Spine has no
README at this revision and is accounted here through the separate baseline
tree rule; that ambiguity does not explain the seven existing Heart and Soul
files missing from the manifest.

### 2. BLOCKER — the signed conflict requirement has no closed production fact population, and the known live conflict disappears

Classification: **signed-spec contradiction/amendment gate**. Veracity:
**[Confirmed]**.

[Observed] PWB-REQ-004 quantifies over any two admitted artifacts that disagree
about “one project fact” (`spec.md:429-447`). Its own design names the live
counterexample: the root account says eight domain butlers while V1 says nine,
and requires Polaris to expose it (`design.md:8-13`). At the exact Butlers
revision, `about/README.md:103-106` states “3 staffers + 8 domain butlers”;
`about/heart-and-soul/v1.md:207-213` states three staffers and nine domain
butlers. The root index also supplies explicit layer precedence at
`about/README.md:37-50`.

[Observed] Live output nevertheless reports `rulesDeclared=0`,
`contradictedFacts=0`, and “No two admitted declarations disagree.” The root
index has no extraction class (`project-shape-manifest.ts:224-243,321-324`),
and production passes neither `rules` nor `statedDeclarations`
(`model.ts:153-165,595-606`; `main.ts:153-164`). Tests manufacture both through
an injectable seam.

[Inferred] A one-off parser for this known count could repair this example,
but it would not satisfy the signed universal requirement. The signed closed
item grammar (`spec.md:15-62`) defines no project-fact identity, declaration
grammar, or precedence-rule grammar. Implementing an arbitrary new fact
population would change what the signed observer claims to exhaust.

Why it matters: the surface presents a false absence of contradiction for the
specification's named real counterexample. A general implementation cannot be
proven complete against an undefined denominator.

Minimum precise fix: use the amendment path required by
`.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md:81-82` to close the
project-fact and precedence populations (or narrow PWB-REQ-004 to a finite
enumeration), then implement and independently sweep that population. Do not
hard-code a silent winner.

Supporting evidence: signed `spec.md:15-62,429-447`; signed `design.md:8-13`;
exact Butlers `about/README.md:37-50,103-106` and
`about/heart-and-soul/v1.md:207-213`; live zero-rule/zero-contradiction output;
production injection seam `project-shape-model.ts:311-315,493-498`.

Contradictory evidence checked: `project-shape-coverage.ts:189-246` correctly
preserves both declarations and applies only an explicit injected rule, and
its tests pass. That proves the reconciliation function after inputs exist;
it does not discover the real inputs or close their denominator. The specific
8-versus-9 example is locally repairable, but the universal signed wording is
not thereby made exhaustive.

### 3. BLOCKER — live item and exclusion denominators do not reconcile

Classification: **implementation defect**. Veracity: **[Confirmed]**.

[Observed] The exact Git tree contains 183
`openspec/specs/<one-directory>/spec.md` paths. The signed definition says each
such path itself mints one `baseline-spec` item (`spec.md:22,47-48`). The live
model contains all 183 source paths but reports only 76 modeled baseline items,
107 sources with Unknown denominators, and an Unknown class denominator.
`extractBaselineSpec` confirms that this class uses only the path and never the
body (`project-shape-extraction.ts:425-431`), yet the pipeline waits for body
classification before calling it (`content-classification.ts:439-451`).

[Observed] A second independent arithmetic failure is visible on the live
page: “122 of 256 sources readable” and “133 exclusions.” Those partitions sum
to 255. The machine source records contain 122 `classified` and 134 `excluded`
records. `about/lay-and-land/components.md` becomes a parse-failure exclusion
inside coverage, but the public exclusion list and classification counts were
computed earlier and omit it.

[Observed] The code path is exact: `sourceCoverage` converts a classified
extraction failure into an excluded record
(`project-shape-coverage.ts:267-283`), while `buildProjectShape` publishes the
updated coverage sources but the stale pre-extraction
`population.exclusions`/`population.counts`
(`project-shape-model.ts:491-498,503-566`).

Why it matters: PWB-REQ-002/003 require one accounted state per item and a
reconciling denominator. Here a path-defined population is unnecessarily
erased by body policy, and one source has no place in the visible top-level
partition. Agents cannot safely use these counts.

Minimum precise fix: derive path-only identities from the exact Git tree
without body admission; keep their content-dependent detail separately
Unknown when appropriate. Recompute exclusions and classification counts from
the final post-extraction source records, and assert every public partition
sums to the exact source denominator on the real Butlers revision.

Supporting evidence: signed `spec.md:15-29,47-65,115-140,160-189`; exact Git
counts `baseline_specs=183`; live baseline `76 modeled / 107 excluded-source
denominators`; live source records `122 classified / 134 excluded`; live
published exclusions `133`; code paths named above.

Contradictory evidence checked: PWB-REQ-003 intentionally makes a genuinely
body-derived denominator Unknown when its body is excluded; that remains valid
for roster identities and topology parsing. It does not apply to a
`baseline-spec` identity defined wholly by Git-tree path, and it cannot make
`122 + 133 != 256` reconcile. The current coverage tests pass because none
asserts the post-parse exclusion against the published population counts.

### 4. BLOCKER — “exact source” links stop at Syzygy metadata, not the authoritative artifact

Classification: **implementation defect**. Veracity: **[Confirmed]**.

[Observed] PWB-REQ-011 requires summary → catalog → detail → exact
authoritative artifact, and specifically requires exact requirement text to
remain reachable (`spec.md:502-525`). The live HTML has 119 source-reference
links, all `#polaris-source-*` fragments; it has zero non-fragment source links
and zero HTTP(S) artifact links. `sourceRow` renders only path, synthetic source
identity, rule, object-id prefix, digest, and item count
(`polaris.ts:531-548`). It does not expose artifact text or a route that serves
the exact Git object.

[Observed] The test named as the PWB-REQ-011 sweep defines success as landing
on that metadata row and seeing the model's source identity
(`polaris-reachability.test.ts:216-242`). That is an identity ledger, not the
artifact or verbatim leaf the signed requirement names.

[Observed] The failure is owner-visible in the live capability deep dive:
`openspec/specs/switchboard-identity/spec.md` exists at the exact revision, but
“Current authority,” “Requirement and scenario text,” “Governing doctrine,”
and “Declared non-goals” all render Unknown. There is no other source route.

Why it matters: an owner cannot verify a claim, reach one rule, or complete the
RFC7-30/PWB-REQ-021 exactness prompt from Polaris. A digest proves which bytes
were observed; it does not let the reader read those bytes.

Minimum precise fix: provide a keyboard-operable, revision-pinned artifact
route or a bounded verbatim leaf view whose bytes are checked against the
Git-object id/digest, without turning Polaris into authority. Update the oracle
to traverse the real route and compare leaf bytes/identity, not merely an
in-page row. Excluded bodies must remain withheld and explicitly unavailable.

Supporting evidence: signed `spec.md:502-525,675-710,723-748`; live href
population; renderer `polaris.ts:127-132,531-548`; weakened test
`polaris-reachability.test.ts:216-242`; live deep-dive text.

Contradictory evidence checked: every live fragment resolves uniquely, source
rows carry exact revision/object/digest identities, and the source table is
keyboard reachable. Those are valuable provenance properties, but none makes
the authoritative content reachable. External Git URLs are not mandatory;
an owner-local exact-object route could satisfy the same requirement.

### 5. HIGH — current active-content admission makes inert project-shape syntax unavailable

Classification: **act-bound policy gate**. Veracity: **[Confirmed]**.

[Observed] The live final records contain 132 whole-artifact exclusions for
`active-content`, one approved `known-token-formats` detector exclusion, and
one parse-failure exclusion. In particular,
`openspec/specs/switchboard-identity/spec.md:11` at the exact Butlers revision
contains the inert inline-code literal ``telegram:<id>``. The raw-text regex at
`git-object-reader.ts:147-189` treats `<id>` as an HTML tag without excluding
fenced/inline-code contexts, so the entire current requirement is withheld.

[Observed] This is not evidence of a leaked secret. Both live channels pass
the approved detector sweep, and the affected source is retained only as
hash/path/reason metadata. The security posture is conservative.

[Inferred] The resulting availability is nevertheless incompatible with the
current PWB objective: 132 of 256 sources are lost before parsing, including
the exact current requirement needed by PWB-REQ-015/021. Deciding that inert
CommonMark code or escaped literal syntax is admissible changes the effective
content-classification boundary. The implementation authorization explicitly
requires a new owner act before changing security/privacy posture
(`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md:86-94`).

Why it matters: the current policy/implementation combination is safe but
cannot produce the signed comprehension result. Silently weakening the regex
would cross an authority boundary; leaving it unchanged keeps the walkthrough
blocked.

Minimum precise fix: owner decides whether the approved policy should
distinguish inert Markdown code/fence tokens from executable HTML/URLs. If yes,
amend/replace the policy at an exact digest and re-perform its owner act, then
implement a CommonMark-context-aware detector and re-run sentinel/mutation/live
sink sweeps. Preserve whole-artifact exclusion for the actual token-format
match unless separately changed by the owner.

Supporting evidence: policy artifact
`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json:68-143`;
policy act `PWB-SECRET-CLASSIFICATION-POLICY-ACT.md:50-67`; implementation
`git-object-reader.ts:123-189`; exact Butlers requirement line 11; live
exclusion population.

Contradictory evidence checked: PWB-REQ-006 requires active repository content
never to reach an active sink, and the current whole-body refusal satisfies
that safety limb. The approved detector scan and exact-credential scan are
clean. This finding therefore does not classify the current behavior as a
security failure or authorize a code-only relaxation; it classifies the
security/comprehension trade-off as an act-bound gate.

### 6. HIGH — the live machine output exceeds the act-bound output limit and no production code enforces two declared limits

Classification: **implementation defect**. Veracity: **[Confirmed]**.

[Observed] The adopted observer registry declares
`maxParseMillisecondsPerSource=250` and `maxRenderedBytes=2097152`
(`POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json:123-130`). PWB-REQ-006
requires parse-time and rendered-output limits to be deterministic inputs and
requires a breach to stay visible and Unknown (`spec.md:340-362`).

[Observed] The current authenticated `/api/poc` response is 4,645,644 bytes,
2.215 times the declared 2,097,152-byte ceiling. `projectShape.limitBreaches`
is empty. The human HTML is 1,069,549 bytes. Source search finds production
enforcement only for max source count, per-source bytes, total bytes, and index
depth; parse-time and rendered-output values otherwise occur only as constants,
digests, or tests.

Why it matters: the machine channel already violates the natural scope of the
declared output budget, while the missing parse-time arm leaves a declared
resource boundary unenforced. The API is authenticated, but a 4.6 MB response
still defeats the bounded-observer contract and contributes to an unusable
surface.

Minimum precise fix: enforce both remaining limits in the real pipeline. Bound
each parser invocation, and check the actual serialized human and machine
bytes before serving; emit a typed, counted Unknown/breach result without
silently dropping sources. Add exact-boundary and over-boundary tests through
the HTTP routes, including the current Butlers-sized model.

Supporting evidence: signed `spec.md:340-362`; adopted registry lines 123-130;
live byte counts; live empty breach list; production search over
`maxParseMillisecondsPerSource` and `maxRenderedBytes`.

Contradictory evidence checked: the human HTML is below 2 MiB, all source-byte
limits and the index-depth limit have real consumers/tests, and `/api/poc`
requires a credential. Even if “rendered” were read narrowly as HTML only, the
signed requirement still has no production rendered-limit enforcement or
parse-time enforcement; the machine-output scope should be made explicit if
the owner intended to exempt it.

### 7. HIGH — narrative and authority-band parity is not served through the machine endpoint

Classification: **implementation defect**. Veracity: **[Confirmed]**.

[Observed] PWB-REQ-014 requires human and machine forms to carry the
presentation/non-citable claim-block semantics; PWB-REQ-015 requires band
class/order and proposal state in both channels; accepted RFC7-33 requires
those distinctions through machine-queryable endpoints. The HTML embeds a
`polaris-narrative` JSON script with those fields, but
`polaris-narrative.ts:195-199` explicitly says it is not `/api/poc`.
`routes.ts:94-98` serializes only `PocModel`.

[Observed] The exact live authenticated machine answer has no path containing
`narrative`, `deepDive`, `bandClass`, `presentation`, `citable`, or
`claimRole`. The parity test renders HTML in-process and compares it with
`JSON.parse(JSON.stringify(model))` (`polaris-parity-sweep.test.ts:276-280`);
it never requires the endpoint to carry the HTML-only presentation artifact.

Why it matters: an agent using the advertised machine answer cannot recover
the same authority bands, claim-block type, or non-citability warning that a
human page exposes. Raw factual parity is not complete semantic parity.

Minimum precise fix: serve a versioned Polaris presentation envelope from an
authenticated machine route (as a separate field or endpoint) while keeping
it non-authoritative and outside truth inputs. Compare the live endpoint's
complete multisets to independently parsed DOM units, including band,
claim-role, non-citable, and presentation-artifact fields.

Supporting evidence: signed `spec.md:618-704,761-792`; accepted
`RFC-0007/rendering-and-surface.md:205-239`; implementation
`polaris-narrative.ts:193-205`, `routes.ts:81-98`; exact live API key/path
sweep.

Contradictory evidence checked: raw project-shape claims, authority states,
judgment fields, and 389 presented claim ids are present in the model, and the
current parity suite reports no differences for those families. The embedded
HTML script is machine-readable. This narrows the finding to the required
machine endpoint's missing presentation semantics rather than claiming all
human/machine facts differ.

### 8. BLOCKER — the prepared cold-open path is not bound to this evaluation and is not Polaris-only

Classification: **implementation defect**. Veracity: **[Confirmed]**.

[Observed] PWB-REQ-021 and RFC7-30 require a fresh reader to use Polaris only,
reach exact intent, and answer the complete prompt population
(`spec.md:805-831`; `RFC-0007/rendering-and-surface.md:134-160`). The prepared
schedule instead allows `/`, `/trajectory`, `/orrery`, and
`/trajectory/materialize` alongside `/polaris`, and the evaluator accepts any
nonempty subset because it checks only that each recorded path belongs to that
wider list (`walkthrough-inputs.ts:39-53`; `walkthrough-judgment.ts:574-580`).

[Observed] The expected run evaluation identity is the literal placeholder
`not-yet-recorded`, not the live model's evaluation/snapshot identity. The
owner packet says a later recording session will write a run record and then
edit the implementation expectation table to the same new slug
(`OWNER-WALKTHROUGH-PACKET.md:71-79`). The run parser records no answer fields
at all (`walkthrough-judgment.ts:273-389`), even though PWB-REQ-021's retained
record must contain the complete answers.

[Observed] The actual current state is honest absence: no run record, no
judgment, `unknown-never-met`. The supplied owner observation says the attempted
walkthrough was aborted because the page was unusable; it is not a PWB-REQ-022
execution record or judgment and must not be substituted.

Why it matters: the packet cannot be used unchanged to prove the exact
Polaris-only evaluation under review. A future state-(1) act could bind a
well-formed record carrying the placeholder and a non-Polaris subset while the
evaluator calls the pair lawful. That would make the authority gate exact over
the wrong behavioral subject.

Minimum precise fix: hold the owner walkthrough. After the truth/source fixes,
derive a stable run identity from the exact immutable evaluation and surface
version, restrict the traversal population to Polaris and its exact-source
routes, and retain all nine answer fields. Validate PWB-REQ-021 completeness as
a separate comprehension precondition so PWB-REQ-022's closed act-invalid
denominator is not silently changed; if the team instead changes that closed
denominator, use the signed-spec amendment path. Then perform a new owner run
and separate judgment.

Supporting evidence: signed `spec.md:723-748,805-925`; accepted
`RFC-0007/rendering-and-surface.md:134-190`; implementation
`walkthrough-inputs.ts:33-53,62-89`; parser/evaluator
`walkthrough-judgment.ts:273-389,543-580`; owner packet lines 71-102; live
absent result.

Contradictory evidence checked: the 102 judgment tests exercise both valid
states, 84 present-invalid cases, two absent cases, failed-state-(2) behavior,
and history; the loader's current real-tree test correctly pins absence. Those
tests use the same placeholder and route expectations, and therefore do not
establish binding to this live evaluation or compliance with Polaris-only
navigation. No current false success is claimed; the defect is readiness for a
future success claim.

## QUESTIONS FOR OWNER

1. **PWB-REQ-004 fact scope.** Should the signed universal “one project fact”
   language be amended to a finite, explicit project-fact and precedence
   grammar? Recommendation: **yes**. The current exact conflict must be covered,
   but a one-off hard-code would leave the universal denominator unprovable.
2. **Inert markup under the approved policy.** Should inline/fenced code such as
   ``telegram:<id>`` be admitted for inert parsing while raw executable
   HTML/unsafe URLs remain excluded? Recommendation: **yes, through a new
   exact-digest policy act**, followed by context-aware implementation and the
   existing security mutation/sink gates. The current review does not authorize
   that relaxation.

No owner walkthrough verdict should be requested yet. The current absence is
the correct state until the blocking truth and route defects are repaired and a
new exact evaluation is available.

## Veracity ledger

| Prior claim tested | Classification | Invalidating or narrowing evidence |
|---|---|---|
| “The 627 passing focused tests establish PWB conformance.” | **[Incorrect]** | The manifest fixture uses directory links unlike real Butlers; live exact-head source, denominator, conflict, route, and size counterexamples remain. |
| “Every internal link resolves, therefore exact-source reachability passes.” | **[Overstated]** | 298/298 fragments resolve, but all source paths terminate at metadata rows and no authoritative artifact/leaf route exists. |
| “Zero live contradictions means the sources agree.” | **[Incorrect]** | Exact root and V1 authority state eight versus nine domain butlers; the design itself names this conflict. |
| “The active-content exclusions are proof that secret material was caught.” | **[Overstated]** | 132 are active-content classifications, only one is a token-format detector match, and live sink scans are clean. The policy boundary remains owner-controlled. |
| “The page violates PWB-REQ-012 because it is verbose.” | **[Incorrect]** | The signed mechanical role/heading/lede/term checks pass. The roughly 12,064-word rendered-text usability failure is governed by the owner-judged PWB-REQ-021 criterion. |
| “The current absent judgment is itself a defect.” | **[Incorrect]** | PWB-REQ-022 requires absence to render Unknown-never-met; live behavior does exactly that. The defects are the surface and prepared future-run binding. |

## Evidence gaps

| Unknown | Why material | Evidence sought | Owner | Blocking? | Investigation | Revisit trigger |
|---|---|---|---|---|---|---|
| Full live browser keyboard/AX/contrast result over the 256-source page | Existing browser evidence uses a compact fixture; the live DOM has 302 anchors, 10 disclosure summaries, and 5 explicitly focusable regions, but the sequentially reachable population was not measured. | Browser-derived live focus trace, AX tree, activation sweep, and contrast denominators at the repaired exact head. | Implementation/review cycle | No additional blocker; exact-source and walkthrough failures already block. | Run the existing independent CDP checker against both loopback and tailnet live URLs after repair. | New exact review head. |
| Whether `maxRenderedBytes` was intended to exempt authenticated JSON | The machine response is already 2.215× the limit, while the registry does not explicitly name channel scope. | Owner/spec clarification or an amended limit definition, plus route-level tests. | Owner if semantics change; implementer otherwise | Yes for claiming PWB-REQ-006 complete. | Resolve before altering the act-bound registry envelope. | Owner decision or signed amendment. |
| Complete secret absence beyond the approved detector vocabulary | Content-blind scans can only prove zero approved-pattern and exact-credential matches. | A new policy/detector act if broader classes are required. | Owner | No; current result is correctly detector-scoped. | Do not inspect unrelated sensitive stores or bodies. | Policy change request. |

## VERDICT

**REVISE**

The exact live head cannot be confirmed. PWB-REQ-005's authority gate and
PWB-REQ-022's absence behavior are sound, but the current surface omits its
primary authority corpus, asserts unsupported zero/completeness claims, hides
the specification's named live contradiction, publishes non-reconciling
denominators, does not reach exact artifacts, exceeds an act-bound output
limit, omits required presentation semantics from the machine endpoint, and is
not ready for a lawful Polaris-only cold-open run.

## TOP THREE DOWNSTREAM RISKS

1. **Comprehensible fiction becomes an owner decision input.** Missing Heart
   and Soul facts, false zero classes, “complete catalog,” and zero conflicts
   can cause the owner to reason from an incomplete model while the page looks
   structurally rigorous.
2. **A future walkthrough act binds the wrong subject.** The placeholder
   evaluation identity and non-Polaris route population could make an exact
   owner act valid over a record that did not test the signed criterion.
3. **Machine consumers amplify inconsistent truth.** A 4.6 MB endpoint exposes
   stale partitions and omits narrative authority semantics; automated agents
   can ingest the confident counts without the human page's full warnings.
