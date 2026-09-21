# Independent fresh-context review 4 — Polaris M2 evidence-currency funnel packet

Read-only review. No file in any repository or worktree was modified; no
state-changing git command, no `bd` write, no daemon, no network, no Butlers
checkout read. The only file written is this one.

## Subject

Worktree `…/scratchpad/m2wt`, branch `agent/syzygy-dov.2`, commit
`68123fcfa6641694217728af8dd3abad408f654b` ("docs: Polaris M2 packet review 3
(REVISE) retained; false PWB-REQ-020 precedent withdrawn [syzygy-dov.2]").
`git status --porcelain` is empty: the reviewed bytes are the committed bytes.
`git diff --name-only a9f671e HEAD` returns six paths, all under `docs/` and
`.syzygy/governance/decisions/`; **zero** paths under `apps/**` or
`packages/**`, so every code citation the packet makes "at `a9f671e`" holds at
this commit unchanged.

Digests computed this session with `wc -c` and `sha256sum`, never transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` | 75475 | `013e7d92e1a3d51c0c8b9f4f4c653b04caa0eec7d2d9aff0ed4f6a4788a5946c` |
| `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json` | 8904 | `8e0e3717b41eaa4296a0cfd5ee3c28a127f4d43d53fe9d39e23559d47619db9a` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 29080 | `c82b839433cbd8423a9c4c8caa46fa472daeaa80d8b2f262e3f0e675500f83b1` |

Retained capture re-hashed this session:
`…/scratchpad/m1/measure/after/polaris-tailnet.html`, 1,484,487 bytes, sha256
`e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` — matches
the packet's and the evidence record's figure exactly. The machine capture
`api-poc.json` beside it (sha256
`a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e`, computed
here; the packet records no digest for it) is the machine channel of the same
render.

The three retained prior raws re-hash to the values the packet records:
`R-…-RAW.md` 39904 / `ff8c8f836e4488de939ae26d5e0a61c12d110c35a5438dd8aab3d5ff4be882bc`;
`R-…-2-RAW.md` 35095 / `545c39259e370a5019ec40c6de210fcd00ce4bb5dedd09cb60f2350bc6367a22`;
`R-…-3-RAW.md` 30943 / `930c4e361a05c677b428afaf4d743af22197984b34623fb49e17fc966d4024ed`.

By verification rule 10 this review binds the bytes named above and nothing
later.

## What re-derived cleanly this session

Every figure in "Measurements on the retained capture" (:171–186) was
re-derived from the capture independently of the packet, by the predicates the
packet names and by a second method where one exists:

- 713 `<span class="claim-tuple"` spans (regex match and literal count agree).
- 713 `data-epistemic-freshness` attribute occurrences, **all** `fresh`;
  one distinct value of the closed four (regex extraction and literal count
  of the attribute name agree, 713 each).
- Tuple shapes by per-span attribute parse: `Observed/report-fact/fresh` ×702,
  `Unknown/unstated/fresh` ×11. Denominator 713.
- 713 `data-evaluation-id` attributes, **1** distinct value
  (`evaluation:pwb-body-read:2026-09-13T13:33:24.295Z`).
- All four freshness glossary sentences occur exactly once, byte-for-byte as
  `polaris-copy.ts`:46–49 defines them.
- 719 ISO-8601 instants in the bytes; 713 inside `data-evaluation-id`;
  **6** in text nodes, at offsets 859145, 859189, 860858, 1477549, 1477638,
  1481753 — identical to the evidence record's list. First at 57.98% (the
  packet's "58.0%").
- 8 `YYYY-MM-DD` strings in text nodes; the two before the first evaluation
  instant at 56.69% and 56.78%, as :195–197 says.
- `data-polaris-item="` 409; bare substring `data-polaris-item` 417; the
  distinct `data-polaris-items` 8. Predicate and both figures check out.
- 278 sources in `projectShape.sources`; 415 `projectShape.items`.
- 2 reading plans defined (`statementSha256` at `polaris-reading-plan.ts`:5
  and :294); exactly 1 `class="excerpt-label"` on the capture.
- `assessCurrency` / `CurrencyBoundDeclaration` occur in exactly three source
  files (`packages/cap1-core/src/staleness.ts` plus `req-042` and `req-062`
  conformance tests); **0** occurrences under `packages/three-surface-poc-core`
  or `apps/three-surface-poc`.
- The only `freshness:` assignments in non-test POC sources are
  `project-shape-model.ts`:185 and :193 (both `FRESH`); the third hit the
  evidence record discloses, `fresh-checkout-demo-main.ts`:286, is a
  pass-through of an existing value, not an assignment — the packet's prose
  is right and the record discloses the hit.
- `horizon` across non-test `packages/*/src` and `apps/*/src`: one hit,
  `polaris.ts`:156, a comment about horizontally scrollable tables.
- `grep -cF` of `CAP1-REQ` and `PWB-REQ` over `DIRECTIVE-REGISTER.md`: 0 and 0.
- No scoped-attributes package on this branch: `git ls-files | grep -ci` → 0,
  `find` → 0. `git show a9f671e:…/PENDING-OWNER-DECISIONS.md | grep -c P-68`
  → 0, last update note "2026-09-13 (later the same day)". :736–739 holds.
- Byte arithmetic: 1,484,487 − 1,400,000 = 84,487; 1,478,637 − 1,400,000 =
  78,637; 2,097,152 − 1,484,487 = 612,665; 2,097,152 − 1,478,637 = 618,515.
  `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
  `result.q3Target.bytes` is 1400000 with shortfalls 78637/84487. :142–161
  is exact.
- Register counts: by the corrected method quoted at :74–77 of the register
  (split on `## ` headings; a row whose first cell is `P-` followed by
  anything but a cell break), **5** acceptance-act rows, **0** in the reading
  aid, **22** open rows (including `P-25(c)` and `P-69`), **27** in all —
  the figures the 2026-09-14 note states.
- Every quotation of a governing clause was checked at its cited location and
  is verbatim: VIS-2 (`vision.md`:96–106), VIS-7 (:183–192), RFC2-9
  (`RFC-0002/snapshot-and-evaluation-core.md`:187–207), RFC2-10 (:209–222),
  `architecture.md`:221–229 and :236, `trust-and-evidence.md`:97–104,
  CAP1-REQ-062 (defined at `…/project-registration…/spec.md`:1837),
  PWB-REQ-007 (:439, scenario :470–474, warrants `contracts:` line :480
  listing RFC2-9 and RFC2-10), PWB-REQ-020 (:902, enumeration :906–910,
  Observable :915, Scenario :931, Falsifier :924–926), and the escalation
  triggers of `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`:86–94
  (all three phrases the packet uses).
- Every code citation resolves at this commit: `staleness.ts` five return
  paths at 98/113/128/138/148 over three `state` values, the
  `no-bound-declared` arm at 98–104 carrying no `freshness` field;
  `project-shape-model.ts` comment 162–166, `FRESH` at 167, imports 19–27;
  `model.ts` 100–110 with no evidence or horizon field; `main.ts` 80–81,
  113, 134, 187, 201; `git-observation.ts`:61 `rev-parse HEAD`;
  `walkthrough-preflight.ts` 212–220 (terms of *presented* claims only, so
  extra glossary entries are permitted, as :427–431 says);
  `polaris.ts`:357 (the freshness copy group), 505–513 (the reading block),
  1214–1230; `polaris-reading.ts`:42–44.
- `python3 scripts/check_governance.py` ends **`32 OK, 20 WARN, 0 FAIL (52
  checks)`**. No finding names the packet, the evidence record or the P-69
  row. (One CG dangling-reference WARN names review 1's raw pointing at a
  lane B evidence file that lives on another branch; a retained raw is not
  editable and this is not the packet's defect.)
- No Butlers path appears in backticks in the packet (`grep` for
  `` `about/ ``, `` `roster/ ``, `` `openspec/specs/ `` → no hits). No act
  manifest or truncated signed digest is quoted. Every code-span path
  resolves; the ones that do not resolve literally are basename shorthands
  (`main.ts`, `polaris.ts`), `decisions/…` relative to
  `.syzygy/governance/`, or files the packet expressly says live only on
  `agent/syzygy-dov.17`.

**H1 re-derived from the captures, independently.** The packet's repaired
paragraph (:509–526) checks out on every count it states:

- `projectShape.items` has exactly 6 entries of class
  `project-account-section`, keys `architecture`, `v1-scope`, `v1-success`,
  `purpose`, `promises`, `refusals`.
- `data-polaris-section="claim:project-account:<key>"` occurs **exactly once
  per key**, 6 in total (and 6 of the 44 `data-polaris-section=` attributes
  on the page carry a `claim:project-account:` value).
- `claim:item:project-account-section:<key>` occurs **0 times** for each of
  the six; the bare substring `claim:item:project-account-section` also
  occurs 0 times on the page.
- Each item's `statement` and `anchors` are **byte-identical** (Python `==`
  on the parsed JSON values) to the same-keyed `projectAccount` entry's,
  6 of 6.
- `polaris.ts`:1220 passes `withItems: false` to `classBlock` for that class,
  and `classBlock` (:597–606) emits no item table when it is false — the
  mechanism behind the 415 − 409 = 6 gap.
- `polaris-parity-sweep.test.ts`:202–209 reads, verbatim at 205–206,
  "the project-account-section items (presented once, as the account's / own
  section claims, never as an item table)", and :209 omits them from
  `presentedClaimPopulation` by claim id. The packet's quotation is exact and
  its citation span contains it.
- `polaris-narrative.ts`:193–198 reads "It is not `/api/poc` and never becomes
  part of it." The packet's `"not `/api/poc`"` and `"never … part of it"` are
  exact with the elision marked.

So the H1 repair is sound in everything it asserts about section rendering and
the 0-count string. One residual overstatement in the same paragraph is J6
below.

## Findings

### J1 — blocking — slice 2 calls the horizon count "a project fact", which is a closed population under PWB-REQ-004 that the packet never reaches; the slice-2 "No act" row and Gate 5's "no spec delta" rest on it

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:445–447:

> and it is a `presentation-artifact` under PWB-REQ-014 only where it frames;
> the count itself is a project fact with a claim id, so PWB-REQ-020 parity
> applies to it like any other.

"Project fact" is a defined, **closed** population in the digest-bound spec.
PWB-REQ-004, at
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`:491–498:

> The POC SHALL admit project facts only from this closed population:
> `item:<class>:<declared-key>` and `count:<class>` for each of PWB-REQ-002's
> nine extraction classes; `catalog-count:<catalog-key>` for each of the nine
> literal V1 catalog headings; and `project-account:<key>` for `purpose`,
> `promises`, `refusals`, `architecture`, `v1-scope` and `v1-success`. Every
> declaration SHALL be emitted by the extractor assigned to an admitted source;
> an injected or unrecognized fact, class, key, catalog or account key SHALL
> mint nothing.

A changed-source count produced by a `rev-parse` probe is in none of those four
forms and is emitted by no extractor assigned to an admitted source. Read at
the packet's own word, slice 2 mints a project fact outside the closed
population — which is an amendment to the signed PWB specification, and
"an amendment to the signed PWB specification" is the second escalation trigger
at `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`:89–90. That would flip
the slice-2 act row at :385 from "**No**" to "yes", contradict Gate 5's
"Slices 1–4 and 6: no spec delta" (:636), and put slice 2 inside Q6's
collision instead of outside it — the opposite of the recommended handoff's
"Run slice 2 next" (:970).

The conclusion very likely survives, and the packet already names the lawful
route twice without connecting it: RFC2-10's "A condition genuinely outside the
four is disclosed as a fact of the render" (quoted at :326–327, relied on at
:639–640), and PWB-REQ-014 itself, whose three claim roles are "anchored
project fact, explicitly non-normative framing, or **epistemically labeled
claim**" (:763–765) — the third role fits a probe claim with its own tuple and
requires no membership in PWB-REQ-004's population and no anchor into an
admitted Butlers source. That PWB-REQ-004 is the governing clause is not
exotic: it is the requirement that closes exactly the population slice 2 adds
to, and it appears nowhere in the packet — not in Gate 0's specification row
(:59, which lists PWB-REQ-007, 006, 016, 020, 021), not in Gate 3, not in
Gate 5. A grep of the packet for `PWB-REQ-004` returns zero hits.

This is the decisive clause for the load-bearing "no act, no delta" answer on
the one slice that adds a new rendered claim, and the packet's own sentence
puts the claim on the wrong side of it.

*Resolves by:* (a) restate :445–447 in PWB-REQ-014's vocabulary — the probe's
count is an **epistemically labeled claim** and a disclosed fact of the render
(RFC2-10), not an admitted project fact under PWB-REQ-004; and (b) add one
clause to Gate 5 and to the slice-2 act row quoting PWB-REQ-004:491–498 and
saying why the probe mints nothing inside it, so the "no spec delta" answer
rests on the clause that governs it rather than on silence. If the owner or a
reviewer reads it the other way, slice 2 acquires a spec delta and joins Q6's
collision — state that condition the way :505–509 already states slice 3's.

### J2 — non-blocking — the probe's own claim renders `fresh` with no declared bound: the defect M2 exists to remove, reintroduced by the slice the packet recommends running now

:451–455 renders the horizon band as

> … [Observed · report-fact · fresh · unchallenged, probe
> `evaluation:pwb-currency-probe:…`] · What this means

Under Q1's recommended ruling — "A bound is required … RFC2-9 is
unconditional" (:45) — and Q7's — every class with no declared bound renders
Unknown with `no-currency-bound-declared` (:51, :606–614) — the probe's own
claim class has no declared currency bound either, so the tuple slice 2 ships
is the same unearned `fresh` that Gate 1 calls the defect. After slice 5 it
would flip to Unknown/`stale` on the page's most prominent new claim unless
the registry's `currencyBounds` array carries a row for the probe class; slice
5's description of that array ("one row per claim class, each with `claimClass`
and `maxAgeMs`", :571–575) never names it, and the Gate 6 acceptance list does
not require it.

This is not an unlawful design — it is an undisclosed consequence of the
recommended sequence, on the one claim whose whole purpose is to be trusted
about currency.

*Resolves by:* one sentence in slice 2 saying what freshness the probe claim
carries before slice 5 and after it, and one row in slice 5's `currencyBounds`
sketch for the probe class (or an explicit statement that the probe is a render
disclosure carrying no freshness value, which is the J1-consistent answer).

### J3 — non-blocking — Q7's recommendation is never weighed against the RFC2-10 sentence the packet quotes for Q3

:326–327 quotes RFC2-10 verbatim and relies on it twice:

> A condition genuinely outside the four is disclosed as a fact of the render,
> never dressed as a freshness state.

Q7 recommends rendering an undeclared class's claims with freshness `stale`
(:51, :606–614). "No currency bound is declared" is precisely a condition
outside the four — the packet says so itself ("the engine deliberately declines
to say `stale`", :604) — so the recommendation is, on the packet's own quoted
clause, a candidate for "dressed as a freshness state". The packet names the
squeeze (cannot be `fresh`, cannot be omitted per PWB-REQ-007, cannot be a
fifth value) and labels the recommendation `[Inferred]`, which is honest, but
it never puts the one clause that cuts against its answer in front of the
owner, while using that same clause as the ground for Q3 and slice 2 twenty
lines earlier. An owner ruling Q7 from this packet rules without the strongest
counter-argument in view — and Q7 is a question the packet correctly says
"RFC2-10 says no implementer may make".

*Resolves by:* one clause in Q7 and in slice 5 quoting :326–327 against the
recommendation and saying why `stale` plus a distinct primary reason is still
preferred to the alternative (amend the engine so it carries a value), or
promoting that alternative.

### J4 — non-blocking — success criterion 2 and S1 require a route for every unreachable value; slice 1's `superseded` marker carries none, and the copy oracle does not check for one

:121–124:

> 2. Every freshness sentence in the rendered glossary is either reachable at
>    that evaluation or carries, in the rendered text, the reason it is not and
>    the route that would make it reachable. A copy-oracle test fails if a
>    sentence is neither.

S1 repeats it (:673–675): "carries the reason it is unreachable **and the
route** that would make it reachable".

Slice 1's marker text at :418–419 is reason only:

> `superseded` — a later evaluation replaced it. *Not reachable at this
> evaluation: the model carries no claim from an earlier evaluation.*

The `broken` marker (:411–417) is borderline by design after review 1's F3 —
it names what would change ("only a model that carries evidence across
revisions, which M2 does not build") while deliberately refusing a route. And
the copy-oracle test as specified (:433–437) checks only that an unreachable
value's sentence carries a marker and a rendered value's does not; it never
checks for a route, so it cannot fail on this. This is the H5 class — an
acceptance criterion contradicting the slice's own text — one slice over, and
this time the oracle that is supposed to enforce the criterion does not test it.

*Resolves by:* weaken criterion 2 and S1 to "the reason it is not reachable
and, where one exists, the route", which is what slice 1 actually designs; or
give `superseded` a route and keep the criterion. Either way say which the
oracle enforces.

### J5 — non-blocking — "whenever" overstates `applyReadingPlan`'s two reasons; 11 of its 13 full-declaration returns would stay silent under slice 6

:546–552, labeled `[Observed, both files at `a9f671e`]`:

> `applyReadingPlan` (`apps/three-surface-poc/src/polaris-reading.ts` line 44)
> returns the full declaration with `condensed: false` **whenever** the pinned
> statement digest no longer matches the observed bytes or the plan has no
> passages, and the return carries no reason

Counted this session, `polaris-reading.ts` has **13** `return full` statements,
at lines 44, 48, 49, 50, 51, 53, 61, 64, 72, 79, 88, 99 and 103. Line 44 is the
digest/no-passages pair the packet names; the other eleven are structural
guards on passages, figures and chapters (non-integer or overlapping offsets,
a passage not starting or ending at a newline, a multi-line heading, a
malformed flow fence, relationship spans outside their body, an empty or
oversized figure or chapter list, a chapter heading not followed by a blank
line, a final chapter not reaching the end of the text). Every one of them
produces the same undisclosed full rendering slice 6 exists to end, and slice
6's proposed field carries only two values (`digest-mismatch` or
`no-passages`), so a plan failing any structural guard keeps the silence.

The failure is small in practice — a reviewed plan should pass the structural
guards — but the sentence is an `[Observed]` claim I can falsify by count, and
the reason enum it drives is incomplete against the function it models.

*Resolves by:* "returns the full declaration with `condensed: false` at
thirteen guard returns — the pinned-digest mismatch and the empty-passage list
at line 44, and eleven structural guards on passages, figures and chapters —
and none of them carries a reason", plus a third reason value
(`plan-malformed`) or an explicit statement that the structural guards are out
of slice 6's scope and stay silent.

### J6 — non-blocking — "Every fact is in both channels" is false at the spec's own fact granularity; what is shared is the statement and the anchors, not the identity

:523–524, closing the H1 repair:

> Every fact is in both channels; the gap is one of rendering form.

and :509–510: "the 415 machine items against 409 rendered item rows are **not
six facts absent from the page**".

Re-derived from the machine capture: `projectShape.facts` carries **439**
reconciled fact keys, and among them are twelve distinct project-account keys —
`item:project-account-section:{architecture,purpose,promises,refusals,v1-scope,v1-success}`
**and** `project-account:{…the same six…}`. They are six *pairs*, not six
renderings of one fact: PWB-REQ-004:491–498 names `item:<class>:<declared-key>`
and `project-account:<key>` as separate members of the closed population, and
PWB-REQ-004:525–530 maps their families separately. The six
`claim:item:project-account-section:<key>` claim ids occur **0 times** in the
served HTML (verified above), so six admitted fact identities are carried by
the machine channel and by no form of the page.

Nothing here breaches PWB-REQ-020, whose invariant runs one way — "Every
project-shape identity, statement, source anchor … **Polaris presents** SHALL
be recoverable … in the machine answer" (:906–910) — and whose sweep the
implementation omits them from by an explicit exclusion list
(`polaris-parity-sweep.test.ts`:209), on the same footing as the reconciled
`facts` population. So the packet's conservative decision — not to lean on this
as a precedent — is right. But the sentence that states it is wrong in the
direction a re-deriving reader will catch: the shared thing is the statement
and the anchor set (byte-identical, 6 of 6, as :521 says), not the fact
identity.

*Resolves by:* "Every one of the six statements and anchor sets is in both
channels under the account's own claim id; what the machine carries and the
page does not is six *claim identities*, which PWB-REQ-020's human-to-machine
direction permits and the parity sweep omits by name."

### J7 — editorial — the H9 repair replaced an accurate line span with an inaccurate one

:73 and :589–590 now give `assessCurrency` as `packages/cap1-core/src/staleness.ts`
lines **87–157**, after review 3's H9 called the previous "87–155" two short.
Counted at this commit, the function opens at 87 and its closing brace is at
**155**; `git diff e0ecdc8 HEAD -- packages/cap1-core/src/staleness.ts` is
empty, so the file is byte-identical to the one review 3 read. Line 156 is
blank and 157 opens an unrelated comment block about superseded observations.
The original span was correct and the repair moved it two lines past the
function.

Harmless to every conclusion — but it is a repair that made a true citation
false on the strength of a review finding that was itself wrong, which is the
H1/G5 pattern in miniature and worth not propagating.

*Resolves by:* restore "lines 87–155" in both places, and note in the review-3
disposition row that H9 was not a defect.

### J8 — editorial — the P-69 row mischaracterizes review 2's three blocking findings

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:199, the sources
cell: "review 2 of the repaired packet, verdict copied exactly: REVISE — **three
blocking register/packet mismatches**, all repaired after it". G1 and G2 were
register/packet mismatches; G3 ("S9 had no slice", packet :902) was a
packet-internal gap with no register component. The register row is the artifact
the owner reads first about what the reviews found.

*Resolves by:* "three blocking findings — two register/packet mismatches and a
scenario with no slice".

## H1–H10 verification

| # | Severity (rev 3) | Claimed | Verified at this commit |
|---|---|---|---|
| H1 | blocking | repaired | **REPAIRED.** Re-derived from both channels of the retained capture: 6 items of class `project-account-section`; `data-polaris-section="claim:project-account:<key>"` once per key (6 total); `claim:item:project-account-section:<key>` 0 times for each of the six and 0 for the bare substring; statements and anchors byte-identical 6 of 6; `polaris.ts`:1220 `withItems: false` is the mechanism; the sweep quote at `polaris-parity-sweep.test.ts`:205–206 is verbatim and the cited span contains it; the `/api/poc/polaris` quotes match `polaris-narrative.ts`:196–197. The withdrawn false precedent is gone from the packet (:509–524), Gate 5 (:641–645) and the evidence record (`project_account_section_items`, with the old `pwb_req_020_precedent` block removed and its withdrawal noted). One residual overstatement in the same paragraph: **J6**. |
| H2 | non-blocking | repaired | **REPAIRED.** :515 names the counted string; the evidence key is now `string_claim_item_project_account_section_key_count_in_served_bytes`. Both re-derive to 0. |
| H3 | non-blocking | repaired | **REPAIRED.** Register :199 Q3 clause now reads "(RFC2-10's evaluation scoping; VIS-7's identity test is not the ground — see the packet's Q3)", matching packet :47. |
| H4 | non-blocking | repaired | **REPAIRED.** Register :199 Q5 clause now states both arms lawful with the marking rationale, matching packet :49. |
| H5 | non-blocking | repaired | **REPAIRED.** Criterion 5 (:132–135) now ends "a fixture with a matching digest renders the condensed form and no withdrawal sentence", agreeing with slice 6's test (:562–567). |
| H6 | non-blocking | repaired | **REPAIRED.** The slice-2 act row (:385) now carries the envelope-trigger clause, quoting "a change to the constraints or envelope the registry entry declares" — verbatim at `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`:91–92 — and answers it. |
| H7 | editorial | repaired | **REPAIRED.** "medium" at :15, :542 and :950; no "small" remains for slice 6. |
| H8 | editorial | repaired | **REPAIRED.** :385 now cites `git-observation.ts` line 61 and `main.ts` lines 80–81 separately; both verified. |
| H9 | editorial | repaired | **REPAIRED AS STATED, BUT THE STATEMENT IS WRONG.** 87–157 is now in both places; the function actually spans 87–155 at unchanged bytes. See **J7**. |
| H10 | editorial | repaired | **REPAIRED.** The evidence key is `before_first_evaluation_instant`, holding the 56.69% and 56.78% hits, which are indeed before the 57.98% first instant. |

## Q1–Q7

Packet cells at :45–51; register clauses at `PENDING-OWNER-DECISIONS.md`:199.
Compared clause by clause, including the Q3 and Q5 parentheticals.

| Q | Problem scope truthful? | Genuine owner gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | Yes. The constant, its comment (`project-shape-model.ts`:162–166) and RFC2-9's unconditional sentence all verified; PWB-REQ-007's `contracts:` warrants line (:480) does list RFC2-9 and RFC2-10. | Yes — a conformance ruling only the owner can make, and the packet keeps the implementation's own reading on the table rather than smoothing it. | Yes. RFC2-9:187–189 is unconditional and rule 8 forbids treating an implementation's reading as the clause. | Yes. The register compresses ("a bound is required and the current rendering is a disclosed non-conformance until one is declared") and omits only the packet's instruction that Q5's marking say so out loud — no clause differs. |
| Q2 | Yes. The registry entry, the 2026-09-05 amendment act and the continuation act all exist at the cited paths. | Yes — act-shape. | Yes; arm (b)'s cost (a new `_act_subjects()` registration, recorder and review) is stated, not asserted. | Yes, clause for clause, including both named act shapes and the arm-(b) contrast. |
| Q3 | Yes, and the ground is now RFC2-10's evaluation scoping with the render-time-drift argument kept only as the non-ground (:464–471). | Confirmation, correctly labeled ("Disclosed for confirmation: on this packet's reasoning the folding arm is unlawful"). No lawful arm is called unlawful. | Yes. | Yes — the parenthetical now names RFC2-10's evaluation scoping and says the identity test is not the ground. |
| Q4 | Yes. "No act found" is the honest form; the trigger phrase is quoted verbatim from the act. | Confirmation and disclosure, correctly labeled; arm (b) is called *unauthorized*, never unlawful. | Yes; the withdrawn unattended-coordination warrant is gone from both packet and register (0 occurrences of "unattended" in the register). | Yes — "(no act found that authorizes a background poller; none needed for the operator route)". |
| Q5 | Yes; `walkthrough-preflight.ts`:212–220 confirms only presented terms need explaining. | Yes — a real choice between two arms the packet now calls lawful. | Yes, with the reasons kept and the losing arm's merit stated ("worse, not unlawful"). One internal snag about the promised *route*: **J4**. | Yes — the register now carries both-arms-lawful and the marking rationale. |
| Q6 | Yes. P-68's absence from this branch re-derived three ways. | Yes — sequencing. | Yes. | Yes, including the five no-act slices by name and the conditional lane B estimate. |
| Q7 | Yes. The `no-bound-declared` arm at `staleness.ts`:98–104 carries no `freshness` field; PWB-REQ-007:443–446 requires it; RFC2-10:213–214 forbids minting. | Yes — a vocabulary ruling RFC2-10 says no implementer may make. | Partly. The recommendation is labeled `[Inferred]` and the alternative disclosed, but the RFC2-10 sentence that cuts against it is never weighed: **J3**. | Yes, clause for clause, including the `[Inferred]` label and the "slice 5 renders no undeclared class until Q7 is ruled" condition. |

## Regression spot-check (F1–F20, G1–G14)

No confirmed repair regressed in the current bytes. Specifically re-checked:
F1 (byte arithmetic and its source, exact), F2 (PWB-REQ-020 Observable,
Scenario and Falsifier verbatim), F3 (`broken` marker names no route to the
horizon), F4/G7 (Q3's ground restated, drift kept as non-ground), F5/G1
(unattended-coordination sentence withdrawn in packet, 0 occurrences in the
register), F6/G6 (trigger attributed to the implementation-authorization act by
path and section, quoted correctly), F8 (`project-shape-model.ts`:19–27 shows
the `@syzygy/cap1-core` edge already exists), F14/G13 (all six instant offsets
match), F17 (three source files), F18 (409 / 417 / 8 with the predicate),
G4 (the two earlier `YYYY-MM-DD` strings at 56.69% and 56.78%), G11 (the
1,400,000 figure's source named and the decimal convention stated), G14 ("one
constant" in the register row).

## Cross-cutting

- **Labels.** Every substantive claim I sampled carries `[Observed]`,
  `[Inferred]` or an explicit "None found"; the two projections (added bytes,
  the lane B figure) are `[Inferred]`; "No act found" is used instead of "no
  act exists". VIS-2's Unknown discipline is respected.
- **Trade-offs.** The PWB model's own currency argument is quoted, not
  paraphrased away; Q5's losing arm is given its merit; the Q1-the-other-way
  outcome is written out as a coherent position (:993–1001) rather than
  dismissed. No consensus smoothing found.
- **Zero/all claims.** Each carries a predicate and a denominator, and each one
  I could re-derive from the retained captures or the tree re-derived exactly.
  The two I could not re-derive under this review's read constraints are the
  L4-F1 re-measurement figures (15 of 278 sources, 9 of 415 items, 9 of 409
  rows, 0 unmatched, 0 mismatches of 278), which require reading the Butlers
  repository at two revisions; the evidence record names both methods and the
  self-check, and I verified the 278 and 415 denominators from the machine
  capture. Flagging only as a scope limit of this review, not as a defect.
- **Digests.** Computed, never transcribed, by the packet and by this review.
- **Hard prohibitions.** No implementation code is proposed inside `openspec/**`
  or `.syzygy/**`; slice 5 prepares new registry bytes and a superseding act
  rather than editing digest-bound bytes (:576–582); nothing is labeled
  accepted on the owner's behalf; the candidate banner is intact.

## Summary

One blocking finding, five non-blocking, two editorial.

The H1 repair is sound — every claim in the repaired paragraph re-derived
exactly from the two retained captures and the test source, and the false
precedent is gone from the packet, Gate 5 and the evidence record. H2–H8 and
H10 are repaired; H9 is repaired as stated but the statement it repaired to is
wrong (J7). The seven questions match the register clause by clause, including
the Q3 and Q5 parentheticals that reviews 2 and 3 found broken.

The blocking finding is not a false measurement — it is a missing clause. The
packet's Gate 5 answer for slice 2 ("no spec delta", "no act") is the
load-bearing permission in the recommended handoff, and the clause that
governs it — PWB-REQ-004's closed project-fact population — appears nowhere in
the packet, while the packet's own design sketch calls the new horizon count
"a project fact". The lawful reading is available in two clauses the packet
already quotes; it simply has to be stated, because on the packet's present
wording slice 2 mints a fact the signed spec closes out.

Verdict: REVISE
