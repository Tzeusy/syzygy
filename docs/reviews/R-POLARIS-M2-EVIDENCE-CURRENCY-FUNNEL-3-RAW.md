# R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-3 — raw review, retained verbatim

Independent fresh-context review 3 of the M2 evidence-currency funnel packet.
Read-only session: no file in any repo or worktree was edited, no git state
changed, no `bd` write, no daemon started, no network, no Butlers checkout
read. The only file written is this one.

## Subject

Worktree: `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m2wt`
Branch: `agent/syzygy-dov.2`
Commit: `e0ecdc88a918f30fc2099ba67600f12c65b83003`
("docs: Polaris M2 packet review 2 (REVISE) retained and repaired; slice 6
added [syzygy-dov.2]")

Reviewed bytes (computed this session with `wc -c` and `sha256sum`, never
transcribed):

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` | 72107 | `c82ea32bedae2eef1b1c93ef169dd5d16082d81804d471e06b6c8b4c63c589f5` |
| `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json` | 8543 | `97214f063029f7bdde1e65f909ff3fe861e41bd8643abde34865690cca07cef5` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 28590 | `2d73a5d7cd9c2c22512ae1cf960a23811e31a5736176749f1b67e6b5f496f859` |
| `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-RAW.md` (review 1) | 39904 | `ff8c8f836e4488de939ae26d5e0a61c12d110c35a5438dd8aab3d5ff4be882bc` |
| `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-2-RAW.md` (review 2) | 35095 | `545c39259e370a5019ec40c6de210fcd00ce4bb5dedd09cb60f2350bc6367a22` |

By verification rule 10 this review binds these bytes and no later ones.

## What re-derived cleanly

Every figure in "Measurements on the retained capture" was re-computed this
session from the retained lane A tailnet capture
(`scratchpad/m1/measure/after/polaris-tailnet.html`, 1,484,487 bytes,
1,481,819 characters — both re-derived) and the retained machine captures
beside it (`api-poc.json`, `api-polaris.json`). All agreed:

- 713 `<span class="claim-tuple">` openings; `data-epistemic-freshness` is
  `fresh` 713 times and takes no other value (three methods: attribute
  regex, literal count, per-tag parse).
- Tuple shapes `Observed|report-fact|fresh|unchallenged` × 702 and
  `Unknown|unstated|fresh|unchallenged` × 11.
- One distinct `data-evaluation-id`, `evaluation:pwb-body-read:2026-09-13T13:33:24.295Z`,
  713 occurrences.
- The four freshness glossary sentences, each exactly once, verbatim as the
  packet quotes them; the `broken` sentence reads "broken — its source
  changed since capture."
- 719 ISO instants in the bytes, 713 inside `data-evaluation-id`, **6**
  visible as text at offsets 859145, 859189, 860858, 1477549, 1477638,
  1481753 — exactly the packet's list and grouping; first at 57.98% ≈ 58.0%.
- `data-polaris-item` substring 417, `data-polaris-items` 8,
  `data-polaris-item="` **409**.
- 2 reading plans defined (`ARCHITECTURE_READING_PLAN`, `V1_READING_PLAN`);
  exactly 1 rendered condensed on the capture (`<p class="excerpt-label">`
  occurs once outside the stylesheet, under
  `data-polaris-section="claim:project-account:architecture"`).
- L4-F1 re-measured: 278 sources in the machine capture; all 15 paths the
  evidence record names as changed are in that population; **9** of 415
  machine items cite one, all 9 `baseline-spec`, all 9 rendering `fresh`,
  all 9 present as rendered rows (0 unmatched). Denominators 415 / 409 /
  278 confirmed. (The pinned-versus-head comparison itself is `[Unknown]`
  to this review — reading Butlers is outside its scope — but the packet's
  method is disclosed and its downstream arithmetic is exact.)
- Code sweeps: `assessCurrency` and `CurrencyBoundDeclaration` occur in
  `packages/cap1-core/src/staleness.ts` and two `packages/cap1-conformance`
  tests, and **0** times under `packages/three-surface-poc-core` or
  `apps/three-surface-poc`; `horizon` returns exactly one non-test hit,
  `polaris.ts`:156, a comment about horizontally scrollable tables; the only
  non-test source that *assigns* a freshness value in either POC tree is
  `project-shape-model.ts` at 185 and 193, both `FRESH`
  (`fresh-checkout-demo-main.ts`:286 reads one through, it does not assign).
- Citations re-read at their defined locations: VIS-2 `vision.md`:96, VIS-7
  `vision.md`:183, RFC2-9 and RFC2-10 at
  `RFC-0002/snapshot-and-evaluation-core.md`:187 and :209 (both quotes
  verbatim, including "A condition genuinely outside the four is disclosed as
  a fact of the render, never dressed as a freshness state"),
  `architecture.md`:221–229 and :236, `trust-and-evidence.md`:97–104,
  CAP1-REQ-062 at Capability 1 spec :1837, PWB-REQ-007's currency scenario at
  spec :470–474 with its `warrants` block at :480 listing `RFC2-9, RFC2-10`,
  PWB-REQ-020's Observable/Case/Falsifier at spec :902–940 (all three quoted
  correctly). `project-shape-model.ts`:162–166 comment, `FRESH` at 167;
  `staleness.ts` `no-bound-declared` return at 98–104 carrying `state`,
  `label`, `reason`, `claimClass` and **no** `freshness`; five return paths
  over three `state` values; `walkthrough-preflight.ts`:212–220 collects the
  *presented* claims' terms and requires `"<term> —"`;
  `polaris-reading.ts`:44 is the digest-mismatch/no-passages return of a
  reason-less `full`; `main.ts` observes at 80–81, `buildModel` at 113, mints
  `asOf` at 134, called at 187 and 201; `git-observation.ts`:61 is
  `rev-parse HEAD`.
- The registry entry declares `inputClasses` including `git-revision`, and
  carries `resourceLimits` and `resourceLimitSemantics` exactly as slice 5
  describes; `maxHumanResponseBytes` is 2097152.
- `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` has an "Escalation triggers"
  section containing "any observation outside the consented content class or
  repository" and "a change to the constraints or envelope the registry
  entry declares"; `PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md` has four
  sections, none an escalation section, and `grep -ci trigger` over it
  returns 0. Every act and decision path the packet cites in a code span
  exists.
- M1 arithmetic: the lane A record's `result.q3Target.bytes` is 1400000 with
  `shortfall.direct` 78637 and `shortfall.tailnet` 84487 — the packet's
  figures exactly; 2,097,152 − 1,484,487 = 612,665 and − 1,478,637 = 618,515.
- Dossier coverage: every M2 move in
  `docs/pursuits/2026-09-13-vision-pursuit.md`:147–170 now has a slice or an
  explicit out-of-scope entry — L4-M1/L4-M2 → slices 2 and 3, L4-M4 → slice 4
  plus slice 2's operator route with the recurring/timer half named in "Out
  of scope, explicitly", L4-M5 → slice 6, S5-M1/L4-M3 → slice 5, L4-M7 →
  slice 1.
- `python3 scripts/check_governance.py` ends **`32 OK, 20 WARN, 0 FAIL
  (52 checks)`**. No Butlers path appears in backticks in the packet. No
  manifest digest or truncated signed digest is quoted; the five sha256
  values the packet carries are full digests of the capture and of the two
  retained reviews and this packet's own prior bytes, not act arguments.

## Findings

### H1 — blocking — slice 3's PWB-REQ-020 precedent is false; the six items *are* rendered, and G5 is not repaired

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:502–516:

> The retained capture already holds the precedent for this Polaris-scoped
> reading: `/api/poc` carries six `project-account-section` items
> (`architecture`, `promises`, `purpose`, `refusals`, `v1-scope`,
> `v1-success`) that the page renders nowhere — 415 machine items against 409
> rendered rows … while `/api/poc/polaris` carries none of them, and the
> parity sweep passes … So the implementation, its sweep and PWB-REQ-020's
> Case … already agree that the population is what Polaris presents, and
> `/api/poc` may carry more.

Re-derived from the same two retained captures this session, all six items
are rendered:

1. `poc.projectShape` carries a second collection, `projectAccount`, with
   six entries keyed `purpose`, `promises`, `refusals`, `architecture`,
   `v1-scope`, `v1-success`. For **all six** keys the `statement` and the
   `anchors` are byte-identical to the `project-account-section` item of the
   same key (compared field-by-field, 6/6 identical).
2. The page renders each of those six as its own section:
   `data-polaris-section="claim:project-account:<key>"` occurs **6** times in
   the capture, one per key, and each claim id `claim:project-account:<key>`
   occurs 5 or more times in the served bytes.
3. The page also renders the class aggregate: a `claim-section` with
   `data-polaris-class="project-account-section"`, its own tuple span
   (`data-claim-id="claim:class:project-account-section"`), three cited
   source anchors, and a coverage-counts block reading **"6 declared; 6
   modeled, 0 Unknown, 0 contradicted; 0 source(s) unreadable."** — so the
   denominator PWB-REQ-020's enumerated population names by word is on the
   page too.
4. `apps/three-surface-poc/src/polaris.ts`:1220–1226 renders them:
   `accountByKey(shape, 'purpose')`, `'promises'`, `'refusals'`,
   `'architecture'`, `'v1-scope'`, `'v1-success'` — the six keys exactly.
5. The parity sweep omits them from the item-row family **by name, with the
   reason written down**:
   `apps/three-surface-poc/src/polaris-parity-sweep.test.ts`:202–209 —
   "the project-account-section items (presented once, as the account's own
   section claims, never as an item table)" — and
   `CLASSES_WITH_ITEM_TABLES` at :186 excludes the class for the same
   reason. `walkthrough-preflight.ts`:113 and
   `polaris-reachability.test.ts`:245 filter it identically.
6. Per class, machine items against rendered `data-polaris-item` rows:
   baseline-spec 192/192, topology-component 87/87, catalog-entry 65/65,
   design-contract 32/32, success-criterion 13/13, craft-policy 7/7,
   principle 7/7, roster-identity 6/6, **project-account-section 6/0**. The
   415 − 409 gap is one class rendered in a different *form*, not six facts
   absent from the page.

So the sweep passes because the six facts are in both channels, not because
the machine channel may carry facts the page does not. The packet's
`[Observed]` sentence is false; the reading it supports ("the population is
what Polaris presents, and `/api/poc` may carry more") has no support here;
and the alternative the packet discloses for the owner — "that the six items
are a live PWB-REQ-020 breach today" — is false in the other direction.
The owner is offered two readings of a Case, neither of which is the state of
the system.

This is review 2's G5 not repaired. G5 asked the packet to state which
reading the six items establish; the repair states one and grounds it in a
mis-reading of the capture the packet itself measures. The defect travels:
:98's table note ("the 415 − 409 difference is six `project-account-section`
items `/api/poc` carries and the page does not render, see slice 3"), the
Gate 5 line at :634–637, the evidence record's `pwb_req_020_precedent` block,
and — through Q6 and the handoff — the register's advice that slice 3 may run
now.

Two smaller things in the same paragraph. "while `/api/poc/polaris` carries
none of them" is true but carries no contrast: `/api/poc/polaris` has no
project-shape item population of any class — its top-level keys are `kind`,
`version`, `presentation`, `citable`, `evaluation`, `project`, `narrative`,
and `polaris-narrative.ts`:193–198 says it "is not `/api/poc` and never
becomes part of it". Presenting it as a channel that *excludes* the six
suggests a scoping decision that was never made. And slice 3 proposes serving
the `evidence` block "on `/api/poc` and on `/api/poc/polaris`" (:483–484,
:361) without saying that the second is the presentation-artifact envelope,
not a parity channel.

*Resolves by:* striking the precedent paragraph and replacing it with what
the capture and the code actually show — the six are presented once as the
account's own section claims and the sweep omits them for that stated reason,
quoting `polaris-parity-sweep.test.ts`:204–205 — then arguing slice 3 on the
enumerated-population reading alone, labeled `[Inferred]`, with the
contingency review 1's F2 repair carried (that if the strict reading holds,
slice 3 joins Q6's collision). Correct :98's note to say the difference is a
difference of rendering form. Correct the evidence record. Say what
`/api/poc/polaris` is before proposing to put a field on it.

### H2 — non-blocking — "each of the six key strings occurring 0 times in the served bytes" is a predicate-less figure, and false under its own sentence

:504–507 names the six keys in parentheses (`architecture`, `promises`,
`purpose`, `refusals`, `v1-scope`, `v1-success`) and then says "each of the
six key strings occurring 0 times in the served bytes". Counted on the same
capture, the bare key strings occur 92, 7, 8, 6, 6 and 6 times. The figure is
0 only for the full claim id `claim:item:project-account-section:<key>`,
which the sentence does not name. The evidence record repeats it as
`each_key_string_count_in_served_bytes: 0` with no predicate at all.

This is the defect review 2 raised as G4 — a figure published without the
predicate that would let a reader re-derive it — reappearing one paragraph
after the G4 repair, and it is again the `[Observed]` label I could falsify.

*Resolves by:* "the string `claim:item:project-account-section:<key>`
occurring 0 times in the served bytes for each of the six", and the same
predicate in the JSON key.

### H3 — non-blocking — the P-69 row's Q3 clause reinstates the warrant the packet retired

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:199, Q3 clause:

> recommended **a second identified evaluation**, never folded into the
> pinned evaluation's freshness (RFC2-10, VIS-7)

The packet's Q3 (:47) says the opposite about VIS-7's limb: "The ground is
RFC2-10's evaluation scoping, not render-time drift: the probe is computed
once at build, so folding would not make two reads disagree". VIS-7's
identity test *is* the render-time-drift argument; in the packet it now
reaches only a hypothetical design (a horizon read live at render, :286–287)
that M2 does not propose. An owner ruling Q3 from the register would rule on
a compressed pair of warrants one of which the packet spends a paragraph
setting aside. This is G1's defect one question over, and the register is the
artifact the owner rules from.

*Resolves by:* "(RFC2-10's evaluation scoping; the identity test is not the
ground — see the packet's Q3)".

### H4 — non-blocking — the P-69 row does not disclose that both Q5 arms are lawful

Same line, Q5 clause: "the three unreachable legend states — recommended
**mark in place with the reason and a route, do not delete** (RFC2-10 closes
the vocabulary at four)".

After the G9 repair the packet is explicit that this is the one question with
two lawful arms — :40–41 ("Q5 is a real choice between two lawful arms") and
:49 ("Both arms are lawful: no clause requires a rendered glossary to carry
vocabulary members no claim uses"), which I verified against
`walkthrough-preflight.ts`:212–220 (only *presented* terms must be
explained). The register carries neither sentence, and its parenthetical
reads as the reason deleting is impermissible. G9 was repaired in the packet
and not in the artifact the owner rules from — the same asymmetry as G1/G2,
and the questionnaire invariant's "may not remove a genuine choice" bites on
the register copy.

*Resolves by:* "(both arms lawful; marking keeps RFC2-10's closed vocabulary
visible and lets one copy oracle carry the legend through slice 5, deleting
would make the page silent about three states the contract still defines)".

### H5 — non-blocking — success criterion 5 contradicts slice 6's own test

:132–135:

> A reviewed reading selection whose pinned digest no longer matches renders
> the full declaration *and* a sentence saying the selection was withdrawn
> and why; a test asserts both halves, and a fixture with a matching digest
> renders **neither**.

With a matching digest the reading renders condensed, and
`renderProjectReading` (`polaris.ts`:506–513) still renders the complete
declaration — as `<details class="full-account">`, or, when the plan carries
chapters, as the component-guides section. On the retained capture the one
condensed reading takes the chaptered path: `class="full-account"` occurs 0
times and `data-component-guide` 10 times, all under
`data-polaris-section="claim:project-account:architecture"`. So "renders
neither" is false of the first half. Slice 6's own test sentence (:555–558)
states the right assertion — "the sentence is absent and the condensed form
returns" — so a test written to the acceptance criterion and a test written
to the slice would disagree.

*Resolves by:* "…and a fixture with a matching digest renders the condensed
form and no withdrawal sentence."

### H6 — non-blocking — slice 2's act row answers one escalation trigger and not the other

:385 argues no act is needed for the horizon because the probe "reads a ref
of the already-consented repository, not a Git object of the source
population at any revision, so no body read is added and the trigger is not
crossed". That answers the observation trigger, quoted correctly. The same
"Escalation triggers" section contains a second trigger the probe touches by
shape and the row never reaches: **"a change to the constraints or envelope
the registry entry declares"**. The entry declares `resourceLimits` and
`resourceLimitSemantics` as the observer's input budget (`maxSources` 512,
`maxTotalBytes` 16777216, `maxParsePassesPerSource` 16, each with semantics
prose). A second `rev-parse` per build is a new read by the registered
observer, and a fresh reader's first question is whether it is charged to
that ledger, exempt from it, or outside the declared envelope. The
conclusion very likely survives — usage is not envelope, and :378 already
lists "the registry's `resourceLimits` values" as not touched — but the row
is the load-bearing "no act needed" claim and should say so in one clause
rather than leave the owner to infer it.

*Resolves by:* one sentence in the slice-2 act row: the probe's head
resolution is a `git-revision` read, charged to no source-body limit and
changing no declared `resourceLimits` value, so the envelope trigger is not
crossed either.

### H7 — editorial — slice 6's size is stated two ways

:15–19 "**medium** for slices 1–4 and 6"; :535 "### Slice 6 — A lapsed
reviewed selection announces itself (**small**; no act)"; :916 "Size: medium
(slices 1-4, 6)". Pick one.

### H8 — editorial — a line citation crosses two files

:385, "exactly as `git-observation.ts` already does at lines 61 and 80–81".
`rev-parse HEAD` is at `git-observation.ts`:61; lines 80–81 of that file are
the `worktreeMetadataDigest` and `clean` fields. The 80–81 meant are
`main.ts`:80–81, cited correctly at :235. Same class as G13.

### H9 — editorial — `assessCurrency`'s line span is two short

:73 and :583 give the function as "lines 87–155". It opens at 87 and its
closing brace is at 157 (the `current` return spans 150–156). Inherited from
the dossier (`2026-09-13-vision-pursuit.md`:159); the dossier is not this
packet's to correct, the packet's own sentence is.

### H10 — editorial — an evidence-record key inverts the relation it names

`docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json`,
`dates_in_rendered_text.above_58_percent`, holds the two hits at 56.69% and
56.78% — which are *before* 58%, as the packet's prose correctly says ("two
`YYYY-MM-DD` strings occur earlier"). A later reader taking the key at its
word reads the finding backwards. Rename to
`before_first_evaluation_instant`.

## Repair verification — G1–G14 and the three partial F findings

Each checked against the current bytes at `e0ecdc8`.

| # | Claimed | Verified | Evidence |
|---|---|---|---|
| G1 | repaired | **REPAIRED** | Register :199 Q4 now reads "(no act found that authorizes a background poller; none needed for the operator route)"; the unattended-coordination clause is gone and matches packet :48 |
| G2 | repaired | **REPAIRED** | Register :199 Q6 now reads "slices 1–4 and 6 (legend marking, horizon probe, an `evidence` block on the machine payload, `asOf` guard, lapsed-selection announcement)" — the packet's five no-act slices exactly, slice 3 restored. (The row still omits slice 3's `[Inferred]` contingency, which H1 makes material) |
| G3 | repaired | **REPAIRED** | Slice 6 now has a Gate 3 topology row (:363), an act row (:388, "No"), a Gate 4 design sketch with its test and rule-6 mutant (:535–560), success criterion 5 (:132–135, but see H5), funnel-summary lines (:916, :920), a handoff mention (:931) and Gate 6 item 4's binding (:821). Every citation in the sketch re-read: `polaris-reading.ts`:44, `polaris.ts`:506–510 |
| G4 | repaired | **REPAIRED** | :193–197 restated as "No instant of this evaluation appears in rendered text above 58% of the page", predicate named, the two earlier `YYYY-MM-DD` strings disclosed. Re-derived: 6 visible ISO instants, first at char 859,145 (57.98%); 8 `YYYY-MM-DD` text hits, the two earliest at 840,110 and 841,381, both inside the same cited filename |
| G5 | repaired | **NOT REPAIRED** | See H1. The packet states a reading and supports it with a false `[Observed]` claim about the retained capture; all six items are rendered, as the account's own section claims, and the sweep omits them for that stated reason |
| G6 | repaired | **REPAIRED** | :385 now attributes the trigger to `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, "Escalation triggers", and says the consent act has no trigger section. Both verified: the phrase is in that section; the consent act has four sections and 0 occurrences of "trigger" |
| G7 | repaired | **REPAIRED** | :464–471 now leads with Q3's ground (a changed source is a fact of a different evaluation; RFC2-10 binds freshness to the evaluation that produced the claim) and keeps the 10:00/14:00 argument only as the one that does *not* decide it |
| G8 | repaired | **REPAIRED** | :403–408 the `stale` marker now reads "no claim's freshness is judged against a currency bound — the model assigns a constant", with slice 5 as the route — true until slice 5 lands and false exactly when it does |
| G9 | repaired | **REPAIRED in the packet** | :36–41 now scopes the one-lawful-arm sentence to Q3 and Q4 and says "Q5 is a real choice between two lawful arms"; :49 states both arms lawful with the recommendation's reasons. Not carried into the register — H4 |
| G10 | repaired | **REPAIRED** | Both places: :51 and :600–603 now read "puts an unbounded class under the same invariant as out-of-bound evidence … both render Unknown, with distinct reasons … and assigns neither a freshness value". Clause re-read at Capability 1 spec :1837 |
| G11 | repaired | **REPAIRED** | :145–155 names the source ("the lane A record's `q3Target.bytes` fixes it at 1,400,000, and that decimal figure is used here") and applies the same convention to the 418–443 KB reservation. `q3Target.bytes` = 1400000 with `shortfall` direct 78637 / tailnet 84487, matching exactly; all four ceiling differences re-derived. (:199 still writes 639,806 bytes as "625 KB" on the binary convention, in a different paragraph — not worth a finding, but one convention throughout would be cheaper) |
| G12 | repaired | **REPAIRED** | :157 now carries `[Inferred: a projection about unbuilt code]`; :783–786 gives the lane B figure with "in the lane B package on `agent/syzygy-dov.17` only [Observed there, not on this branch]" |
| G13 | repaired | **REPAIRED** | All three re-derived: the currency scenario at spec :470–474 (heading 470, WHEN 472), the import at `project-shape-model.ts`:19–27, the `no-bound-declared` return at `staleness.ts`:98–104. Two fresh instances of the same class at H8 and H9 |
| G14 | repaired | **REPAIRED** | Register :199 now reads "from one constant in `packages/three-surface-poc-core/src/project-shape-model.ts`"; verified — one `FRESH` at :167, assigned at :185 and :193 |
| F4 | completed | **COMPLETE** | Q3's cell (:47) and slice 2 (:464–471) now carry the same ground; the drift argument survives only as the stated non-ground in both places |
| F5 | completed | **COMPLETE** | Withdrawn in the packet at :48 and now also absent from the register row |
| F6 | completed | **COMPLETE** | The trigger's words are quoted and bound to the act that contains them (see G6) |

Net: 13 REPAIRED, 1 NOT REPAIRED (G5), 3 partial F findings completed. G13's
class recurs twice in new material.

## Per-question assessment

| Q | Scope stated truthfully? | Genuine owner gate? | Recommendation follows? |
|---|---|---|---|
| **Q1** conformance of the constant | **Yes.** Re-derived: the comment at `project-shape-model.ts`:162–166, `FRESH` at 167 assigned at 185/193, RFC2-9 verbatim at RFC-0002:187, PWB-REQ-007's `warrants` at spec :480 listing `RFC2-9, RFC2-10`, 713/713 `fresh` three ways | **Yes** — a conformance ruling only the owner can make; the other arm is stated and its consequence (the spec's own currency scenario becomes unreachable by design) is disclosed at :958–966 | **Yes.** Rule 8 applied correctly: the clause is quoted from its defined location and an implementation comment is not admitted as a reading of it |
| **Q2** where the bound lives | **Yes.** Both named acts exist; the registry entry carries `resourceLimits` and `resourceLimitSemantics` exactly as the sketch assumes; `adopt-registry-entry` precedent is real | **Yes** — act-shape choice, and the two-step ceremony is the owner's | **Yes.** Cost of arm (b) stated concretely (a `_act_subjects()` registration, a recorder, a review) and not smoothed away |
| **Q3** horizon as a second evaluation | **Yes in the packet**, after G7. The register clause re-adds VIS-7 as a warrant the packet retires — H3 | **Disclosed for confirmation, not a free gate** — correctly labeled as such at :37–39 and inside the cell | **Yes.** The abandoned ground is named as abandoned rather than deleted, which is the honest handling |
| **Q4** how re-observation is triggered | **Yes.** The trigger is quoted from the act that contains it; the registry declares `git-revision`; no act authorizing a poller was found and the absence is stated as "none found", not as a prohibition | **Disclosed for confirmation** — arm (b) is unauthorized rather than unlawful, and the packet says exactly that | **Yes**, with the envelope trigger unanswered — H6 |
| **Q5** delete or mark the three states | **Yes** in the packet after G9; the preflight finding is verified at `walkthrough-preflight.ts`:212–220. The register does not carry the both-arms-lawful framing — H4 | **Yes** — and now correctly shaped: a real choice between two lawful arms | **Yes.** Reasons are stated as reasons (reader, one copy oracle across slice 5), not as compulsion |
| **Q6** sequencing and the honest target | **Partly.** The lane B facts are `[Unknown]` to this review (the package is absent from this branch; `git ls-files` and `find` both return 0 paths, as the packet says at :726–732). The half that is checkable — that slice 3 may run now — rests on H1's false precedent | **Yes** — a sequencing ruling against a queued decision | **Yes for the spec-package half** (no M2 spec text; PWB-REQ-007's currency scenario already requires slice 5's behaviour, re-read at spec :470–474). **Not yet for the slice-3 half** until H1 is repaired |
| **Q7** freshness of an undeclared class | **Yes.** `staleness.ts`:98–104 re-read: `state`, `label`, `reason`, `claimClass`, no `freshness`. PWB-REQ-007 requires the complete tuple; RFC2-10's "Four values, closed" and "no implementation may mint, spell, or force-fit a freshness value it does not carry" quoted verbatim | **Yes** — RFC2-10 says in terms that leaving it unstated "is how the value gets chosen by whoever implements the render first", so it is not an implementer's call | **Yes.** Labeled `[Inferred]`, the alternative (a Capability 1 amendment via CC-REV-2) is stated with its route, and the packet says slice 5 is not implementable for any class until it is ruled |

## Cross-cutting

- Epistemic labels: every substantive claim I checked carries
  `[Observed]`, `[Inferred]` or `[Unknown]`, and the `[Inferred]` labels sit
  on the right sentences (the Q7 recommendation, the one-package rule, the
  trust-and-evidence extension, the byte projection after G12). The one
  `[Observed]` I could falsify is H1's, with H2 beside it.
- Rules 2 and 9: the "0 references" sweeps carry denominators and methods and
  re-derived exactly; the "0 times in the served bytes" figure does not carry
  its predicate (H2).
- Rule 3: digests are computed, not transcribed, in both the packet and the
  evidence record.
- Rule 8: every contract claim I checked is anchored to a defined clause and
  quoted from it. PWB-REQ-020 is quoted correctly; what fails at H1 is the
  *fact* the packet applies the clause to, not the clause.
- Rule 10 is stated correctly in both repair sections, and the packet says in
  terms that its current bytes are uncovered until this review.
- CG-1b / CG-15: no Butlers path in backticks; no act argument or truncated
  signed digest quoted.
- Code-span paths resolve. The `decisions/…` spans are relative to
  `.syzygy/governance/`, the convention the packet uses consistently; all
  four exist.
- `python3 scripts/check_governance.py` → `32 OK, 20 WARN, 0 FAIL (52 checks)`.

## Summary

One blocking finding, five non-blocking, four editorial. The packet is in
much better shape than review 2 left it: thirteen of fourteen G findings are
genuinely repaired against the current bytes, the three partial F findings
are complete, slice 6 is properly scoped with a topology row, an act row, a
sketch, a test, a mutant and a criterion, the register row now matches the
packet on Q4, Q6 and the constant count, and every measurement in the packet
re-derived exactly from the retained captures.

The one blocking finding is the same paragraph review 2 raised as G5. Asked
to say which reading the six `project-account-section` items establish, the
repair chose a reading and supported it with a claim about the capture that
the capture contradicts: the six are rendered, their statements and anchors
are byte-identical to the six account entries the page renders as its own
sections, the class aggregate carries a denominator of 6, and the parity
sweep omits them from the item-row family for that exact reason, in a comment
that says so. Slice 3's argument, Q6's advice that it may run now, and the
register row that repeats it all stand on that sentence. It cannot go to the
owner as it is.

Verdict: REVISE
