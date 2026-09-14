# R-POLARIS-M5-AGENT-BRIEFING-FUNNEL — review 4 (raw, retained verbatim)

Independent fresh-context review. Read-only: no file in any repo or
worktree was edited, no state-changing git command was run, no `bd`
write, no daemon, no network, no Butlers checkout read. The only file
written is this one.

## Subject and digests

Worktree: `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m5wt`
Branch `agent/syzygy-dov.5`, HEAD **`d41a9d2`** ("docs: Polaris M5 funnel
review 3 retained and repaired [syzygy-dov.5]"). `git status --porcelain`
is empty [Observed].

Bytes and sha256 computed this session with `wc -c` and `sha256sum`,
never transcribed:

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md` | 114004 | `7e9ead37a7c91cdfe54762f985cc2990bf084901d124b3a302f421d93b6dad76` |
| `docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json` | 30020 | `40b3565eb788456c30ba4105f9094b53b5dac341345bd46293e2229d455a1fae` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 28955 | `af01ea97ab2b6f6d63f1f4b4ca65728b1885f0b7d1ac9b598386328a419cfa6e` |
| `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-RAW.md` (review 1) | 34023 | `73b1596137fe2e02f5d6af781e896b33296d8871059715f582cafcb7f14b3aed` |
| `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-2-RAW.md` (review 2) | 41872 | `861cece7952ee7c7a943abfa104a6ae24ba69a96714ea000b342f262b932d6a4` |
| `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-3-RAW.md` (review 3) | 36179 | `f8adfc2b8846686ed69d7f41b0d2bed334b8c95346409e6cda9fa2a8672fecd6` |

The packet's "Review 3 and repairs" section quotes the review-3 raw at
36179 bytes / `f8adfc2b…` and the reviewed bytes at `09b5395` (packet
103078 / `2ec2413a…`; record 26130 / `283b2357…`; register 28297 /
`101f2b19…`). All four re-derive exactly — the raw from the working
tree, the three subjects from `git show 09b5395:` [Observed]. Rule 10
holds: review 3 binds the `09b5395` bytes, this review binds the
`d41a9d2` bytes above, and this raw is a fourth `-RAW.md`, never an
overwrite.

Capture: `scratchpad/m1/measure/after/api-poc.json`, 5,520,314 bytes,
sha256 `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e`
— present at the session scratchpad path the packet names, size and
digest recomputed this session and matching [Observed].

## Method

Everything below was re-derived at `d41a9d2` from source, the two signed
specifications, the doctrine and RFC files, `DIRECTIVE-REGISTER.md`, the
retained capture, `git show main:` for the register and
`git show f35a25f:` for M3. No disposition row was taken on trust. Byte
figures are Python `json.dumps` with `separators=(',',':')`; literal
counts are `str.count` over the decoded text and `bytes.count` over the
raw bytes, agreeing. Line numbers are `sed -n`/`grep -n` over declaration
and closing-brace lines. `grep -F` or Python `re` for anything
load-bearing (rule 1).

## Findings

### J1 — non-blocking — H9's repair is claimed in two places and specified in none: every site that actually defines the `mayNot` registration check still asks for a count, so the id-vocabulary desynchronization H9 named is still uncaught

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:313-320`, `:849-854`,
`:869-870`, `:728`, `:1284-1286`, `:1557`.

**Defect.** Success criterion 4 now reads, of the `mayNot` row `id`
space, "closed by the six 'does not authorize' bullets of the
authorization act, checked by the Gate 3 registration test — **which
after this widening compares the id list, not only the row count**"
(`:317-319`), and the H9 disposition repeats it: "the Gate 3
registration check now compares the id list, not only the row count"
(`:1557`).

No such check is specified anywhere in the packet [Observed, swept this
session: `id list` occurs at exactly two lines, `:319` and `:1557`, both
of them the claim itself]. Every site that actually defines the check
still defines a count:

- Gate 4 slice 2, the only design text for it: "this table's **entry
  count — six** — should be registered wherever `check_governance.py`
  would notice the source act change (a new function alongside
  `_act_subjects()`, or a dedicated fixture asserting the table's **row
  count** against a fresh read of the act file's bullet count under the
  'What this does not authorize' heading)" (`:849-854`).
- Its rule-6 mutant: "Delete one row from the hand-typed table and
  confirm the **row-count** registration check fails" (`:869-870`).
- Gate 6 acceptance item 3: "the registration check tying the hand-typed
  table to the act's own **bullet count**" (`:1284-1285`).
- Gate 3's slice-2 row says only "this table's entries should be
  registered the same way so an amendment to that act is caught"
  (`:728`) — no predicate at all.

The gap H9 identified survives intact. An amendment that replaces one
"does not authorize" bullet with a different one leaves the count at six
and every one of the four checks above green while `mayNot`'s id
vocabulary is stale — which is exactly the case H9 said "a later
amendment would silently desynchronize". The six ids are also nowhere
enumerated: criterion 4 names one (`no-write-to-observed-repository`)
and "its five siblings", and the evidence record carries only
`"mayNot row id (6 values)"`. A registration check cannot compare a list
the packet never writes down.

The act's six bullets are exact as the packet enumerates them
(`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 70-72, 73-74, 75,
76-79, 80-81, 82-84 under the heading at `:68`) [Observed, read this
session], so the enumeration is available; it simply was not made.

**Repair.** Either specify the id-list comparison where the check is
designed — Gate 4 slice 2 (`:849-854`), its rule-6 mutant (`:869-870`)
and Gate 6 item 3 (`:1284-1285`) — and enumerate the six ids once, or
withdraw the "compares the id list" clause from criterion 4 (`:319`) and
from the H9 disposition (`:1557`), marked and dated in place in the
shape the packet already uses. A disposition that claims a repair the
bytes do not carry is the class of defect review 3's own H4 and H6
were.

### J2 — non-blocking — the H2 repair landed in the packet and not in the P-72 row, so the register no longer carries the clause that decides whether Q2's third ceiling is required or discretionary

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:57`, `:582-600`;
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:209`.

**Defect.** Gate 2 now states the kinds-versus-routes reading and holds
the kinds one: "the clause's two sinks are two *kinds* of encoded
output… so `/api/poc/briefing` would be a fourth route and a third
machine-JSON body, not a third kind [Observed]. This packet reads the
clause as counting kinds [Inferred]. **On that reading the briefing
satisfies PWB-REQ-006 under `maxMachineResponseBytes` as it stands, and
minting `maxBriefingResponseBytes` is a discretionary tightening**"
(`:582-593`). Q2's own row carries the same holding and concludes that
on it "the fold-in dissolves" (`:57`). Both re-derive: spec lines
378-379 are "Final encoded human HTML and machine JSON SHALL each have
an explicit byte ceiling", and `boundedResponse`'s three call sites at
`routes.ts` 151, 161 and 175 serve three routes under two ceiling
identities [Observed, read this session].

The P-72 row's Q2 clause does not carry it. The row says only that
minting "widens that interface and the closed `ResponseLimitIdentity`
union under a superseding registry act (escalation trigger, act line
92), and may fold into Q1's delta if the owner reads PWB-REQ-006's
'each' as staled. *Recommended: mint it, and rule the fold-in at the
same time*" (`:209`). Nothing false is said, but the single clause that
most changes the question's weight — that on the packet's own held
reading PWB-REQ-006 compels no third ceiling at all, so Q2 is a
discretionary tightening rather than a compliance step — is absent. An
owner reading the register alone (which is the artifact that queues the
question) cannot recover it, and the packet's own review-3 section says
the owner questions "did not move", which is true of the
recommendations and not of Q2's ground.

**Repair.** Add one clause to the row's Q2 sentence: that the packet
reads PWB-REQ-006's two sinks as kinds [Inferred], on which reading the
briefing already satisfies the clause under `maxMachineResponseBytes`
and the third ceiling is a discretionary tightening, with the fold-in
arising only on the route reading.

### J3 — editorial — the "0 in the packet" absence figure for `707-713` holds only under an ASCII-hyphen predicate the packet does not state, and the packet carries the en-dash form

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:1536`, `:1552`,
`:495`.

**Defect.** The review-3 method paragraph says "`707-713` swept over the
evidence record (2 sites) and the packet (0)" (`:1536`) and the H4
disposition says "Confirmed (2 sites, 0 in the packet)" (`:1552`).

`grep -F "707-713"` returns 0 on the packet at `09b5395` and 2 on it at
`d41a9d2` (both inside these two disposition sentences), but the line
table has carried the value all along spelled with an en dash:
"`polaris.ts` `authorityLine` … | 707–716 (the table's first value,
707–713, ended on a `.map(` continuation; corrected after review 2, G4)"
(`:495`, present unchanged at `09b5395`) [Observed, both spellings
counted this session].

Nothing is wrong at `:495` — the value is correctly marked as withdrawn,
and `authorityLine` does close at 716 (`polaris.ts:707` declaration,
`:713` a `.map(` continuation, `:716` the closing brace, re-derived this
session). The defect is the absence figure: it is published without the
spelling predicate it holds under, which is precisely the false-absence
class AGENTS.md's continuation-form note and verification rule 9 exist
for — an identifier written in two forms, swept in one.

**Repair.** State the predicate ("ASCII hyphen; the en-dash form stands
in the line table's marked withdrawal at `:495`"), or restate the figure
as "0 outside the marked withdrawal".

### J4 — editorial — the P-72 row calls the evidence record the capture

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:209`.

**Defect.** The row opens "The retained lane A capture
(`docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json`) shows
the fourteen orientation fields at 18,710 of 5,520,314 bytes (0.339%)…".

The retained lane A capture is `api-poc.json`, 5,520,314 bytes, sha256
`a89b0e05…`, in the session scratchpad; the cited path is the packet's
evidence **record**, a 30,020-byte sidecar that reports figures computed
from that capture [Observed, both read this session]. The packet itself
keeps the two apart with care, and says so in the Measurements preamble
(`:350-356`): the capture sits at "`scratchpad/m1/measure/after/`, a
path relative to this session's scratchpad directory, not to the
repository". The register is the artifact a reader reaches first and is
the one place the distinction collapses.

**Repair.** "The M5 evidence record (`docs/evidence/…json`), computed
from the retained lane A capture, shows…".

### J5 — editorial — the G12 disposition row still asserts, unmarked, the repair H6 falsified

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:1503`; cf. `:1447`,
`:1554`.

**Defect.** The review-2 table's G12 row reads, unchanged: "Confirmed:
the 80-column prose line wrapped, the F20 row counts it, the capture
path stated as relative to the session scratchpad."

H6 established that the G12(a) wrap split the line into a 50-column and
a 102-column half, that the F20 row's count was wrong for the population
it named, and that four further prose lines were reflow residue. The
F20 row was restated with its predicate and dated (`:1447`) and the H6
row records the whole history (`:1554`) — but the G12 row was not
touched, so a reader working down the review-2 table meets an unmarked
"Confirmed" that the review-3 table two sections later contradicts. The
packet marks superseded wording in place everywhere else; this is the
one row where it did not.

**Repair.** Mark the G12(a) clause in place and date it, in the shape
the packet already uses at `:1447`.

## H1–H9 verification against the current bytes

Each row re-derived from source, the signed specifications, the capture
and `git show`, not from the disposition.

| # | What the repair rests on | Re-derived this session | Status |
|---|---|---|---|
| H1 | the widened type is the envelope every bounded sink serves; the sentence must be true on all three | `responseLimitFailure` built once at `routes.ts:132-134`; `boundedResponse` at `:137-142` with the `JSON.stringify` at `:141`; call sites `html()` `:151` (`maxHumanResponseBytes`), `machineHandle` `:161` and `presentationHandle` `:175` (both `maxMachineResponseBytes`); `ResponseLimitFailure` `:113-124`, `population` `:120-122`, `ResponseLimitIdentity` `:111` a two-literal closed union; PWB-REQ-006's envelope at spec `:381-384`, its "each" sentence at `:378-379` | **REPAIRED** — Q3 (`:61-116`) now carries a **limit-neutral** sentence ("population counts describe the whole evaluation"), names the widened type as shared and enumerates all three sinks with their line numbers and ceiling identities, withdraws the "…not this briefing's subject" wording in place, and re-runs the no-gate argument "over the two sinks PWB-REQ-006 governs" with the "only"-as-closure reading labelled [Inferred] and routed back to the funnel "before any sink's body changes"; slice 3's breach-body paragraph (`:954-964`) and the P-72 row (`:209`) both follow, the row saying "every bounded sink serves, the human pages and `/api/poc` included" |
| H2 | PWB-REQ-006 counts kinds, not routes | spec `:378-379` names two kinds; three bounded routes under two ceiling identities at `routes.ts:151/161/175` | **REPAIRED** — Gate 2 (`:582-600`) states the distinction, holds the kinds reading [Inferred], says the fold-in arises only on the route reading and that the route reading gives Q1's retroactive arm a second argument; Gate 2's earlier "third final-output sink" is now "a third bounded route" (`:580`); Q2 (`:57`) ties its fold-in to the reading; Q1 (`:55`) names `/api/poc/polaris` as "already a second machine-JSON body under the same `maxMachineResponseBytes` ceiling (`routes.ts` lines 161 and 175)". Not carried into the P-72 row — J2 |
| H3 | the Share column's denominator | every per-key byte reproduces exactly; sum 5,521,648 against whole-compact 5,521,960, gap 312; shares exact against the file's 5,520,314 (41.18 / 30.02 / 27.05 / 1.45) and 41.17 / 27.04 against 5,521,960 | **REPAIRED** — the heading now reads "with `ensure_ascii` at its default; Share against the file's own 5,520,314 bytes" (`:360`) and the prose publishes both denominators and the reason they differ (`:385-395`) |
| H4 | the record's two stale `707-713` sites | `authorityLine` `polaris.ts:707` → `:716` (`:713` a `.map(` continuation, `:714` `.join(';')`, `:715` the `return`) | **REPAIRED** — record `line_numbers_reverified_at_a9f671e…actual` and `not_verifiable_this_session[2]` both read 707-716 with the withdrawn value marked and dated in place, in the record's existing shape; `authorityLine_range` and `G4` also 707-716. The "0 in the packet" figure is spelling-dependent — J3 |
| H5 | the one-claim totals are floors; the components reproduce | all ten reproduce to the byte from the capture by the published field paths: `evaluation` 595, `identity.scope` 109, `authority` 1,369, item records 661 (its `claim` sub-object 504) and 812, chain records 1,075 / 844 / 326, source records 1,627 and 1,803; deltas 7,076−5,449 = 1,627 and 5,150−3,347 = 1,803 | **REPAIRED** — `agent_briefing_sets.one_claim_briefing_examples.note` now carries the floors sentence itself, names the unpublished wrapper with its two sizes (439 and 462) and points at the component table |
| H6 | the over-width population | predicate re-run: lines over 78 columns, outside fenced code, excluding lines whose stripped form begins with `\|` or `#`, over all 1,564 lines → **6**, every one a single unbreakable code-span path (`:11`, `:558`, `:647`, `:674`, `:824`, `:1075`). Zero prose lines. F19's invariant also holds: 0 non-fence lines with an odd backtick count | **REPAIRED** — the F20 row (`:1447`) now states the predicate, the `09b5395` population (eleven, five prose) and the post-rewrap count (six, all paths), with the earlier wording withdrawn. The G12 row was not marked — J5 |
| H7 | the P-72 row's missing leaf denominator | `MaterializationPacket` `materialization.ts:20-30` = 9 top-level fields, 11 leaves; `renderMaterializePanel` `materialize-action.ts:55-82`, seven `<dd>` at `:69-75` with `:74` carrying `issueType` + `priority`; rendered = 8 top-level, 9 leaves; machine-only = `targetBeadPrefix` (set `:58` from the constant `:12`), `governingIntent.designPath` (built `materialize-action.ts:35`), state `at`; status line `:61-62` = 1 of 2 state fields | **REPAIRED** — the row now reads "eight of its nine top-level fields, 9 of its 11 leaves, rendered there across seven cells, none on `/api/poc`"; the G2 disposition's list is now true of all six sites |
| H8 | main's last open row versus highest identifier | `git show main:` → the open table's last row is **P-53**; the highest `P-` identifier anywhere on main is **67**; 26 rows on main (21 open + 5 acceptance-act, `P-25(c)` included in the denominator), 27 on the branch with P-72 | **REPAIRED** — the summary reads "main's register's highest allocated identifier is P-67, its last open row P-53 - P-54..P-67 are ruled and recorded in its update notes" (`:1341-1342`); the record's `pending_register_state.main_at_a9f671e_last_row` says the same with the superseded value marked and dated |
| H9 | criterion 4 cannot see the three minted vocabularies | the three exist as described (`dispatchState` two values, the six `mayNot` ids, the chain's one `not-applicable` state); the act's six bullets at `:70-72`, `:73-74`, `:75`, `:76-79`, `:80-81`, `:82-84` | **PARTIAL** — criterion 4 is widened and names the three with their closing sources (`:309-323`), but the registration check it promises ("compares the id list, not only the row count") is specified nowhere: Gate 4 slice 2, its rule-6 mutant, Gate 3's slice-2 row and Gate 6 item 3 all still define a count, and the six ids are never enumerated — **J1** |

Also verified against the disposition text: `python3 scripts/check_governance.py`
ends **"32 OK, 20 WARN, 0 FAIL (52 checks)"** at this commit; CG-1b
examined 4,870 code-span path references with 0 findings (so every
code-span path in these three files resolves and no Butlers path is
backticked in the packet), CG-7e 32 files 0 findings, CG-15 15
quotations 0 findings [Observed, run this session].

## Spot-check that F1–F22 and G1–G12 did not regress

Re-derived at `d41a9d2`, not read from the disposition tables.

| # | Re-derived | Holds |
|---|---|---|
| F1 / G-none | `forbidden` 3 and `prohibit` 1 by both `str.count` and `bytes.count`; `externalRef`, `governingIntent`, `syzygy-poc:work:`, `mayNot` all 0; `materializedBeadId` 1 | yes |
| F2 | `proposedWork.changeId` = `repair-whatsapp-identity-reconciliation`; `currentAuthority.claim.claimId` = `claim:item:baseline-spec:switchboard-identity`; `MATERIALIZATION_EXTERNAL_REF` `materialization.ts:9`; `WORKER_CHANGE_INTENT_ID` `model.ts:42`; `MaterializationGoverningIntent.requirementId` `materialization.ts:15`; the joined entity and its two relationships present | yes, four literals |
| F3 | `no-such-claim` occurs 3 times, each inside its own withdrawal sentence (`:934`, `:1101`, `:1430`); S2 carries no `reason` slot; PWB-REQ-007 quoted at spec `:447-448` | yes |
| F4 | `PwbResourceLimits` `project-shape-observation.ts:65-73`, seven fields; `PWB_RESOURCE_LIMITS` `:75-83`; ceilings `:81` 2,097,152 and `:82` 8,388,608 | yes |
| F5 / G4 | every line-table row re-derived: `machineHandle` 159-162, `POLARIS_SOURCE_PATH` 221/222, machine block 225-238, `browserRequestAllowed` 26-38 (file ends 38), `MATERIALIZE_HUMAN_PATH` 17, `renderMaterializePanel` 55-82, `MaterializationPacket` 20-30, `MaterializationGoverningIntent` 14-18, `buildMaterializationPacket` 43-65, `MaterializationRecord` 67-78 (`createdAt` 71), `buildTrajectoryMaterializationPacket` 31-37, `ResponseLimitIdentity` 111, `ResponseLimitFailure` 113-124 (`population` 120-122), `boundedResponse` 137-142, `PocEpistemic` 44-46, `PocModel` 98-155, `BodyReadAuthorityEvaluation` 315-324, `AuthorityDisclosure` 39-46, `PwbResourceLimits` 65-73/75-83, `authorityLine` 707-716 | **20 of 20 hold**, in the packet and now in the record |
| F6 / G2 / H7 | both denominators at all six sites, including the P-72 row; the three machine-only values named | yes |
| F7 / F8 / F9 | minimal orientation 18,710 (0.3389%) with the `scope` key; classes-plus-claim 148,780 (2.6951%); 415 of 415 item ids match `claim:item:…` with `item` the only second segment | yes, exact |
| F10 | the `switchboard-identity` item record 661 bytes compact, its `claim` sub-object 504 | yes |
| F11 / F12 / H2 | PWB-REQ-006 quoted at `:571-581`; `ResponseLimitIdentity` a two-literal closed union | yes |
| F13 | Gate 5's `mayNot` warrant on PWB-REQ-005's "every human and machine rendering of the authorization basis", labelled [Inferred], L5-F9 fallback | yes |
| F14 | act "What this does not authorize" = six bullets at `:70-72`, `:73-74`, `:75`, `:76-79`, `:80-81`, `:82-84`; escalation triggers `:86-94`, registry-envelope trigger reaching `:92` | yes, all seven ranges exact |
| F15 / G8 | M3's Gate 3 table at `git show f35a25f:` line 739 has **six** slice rows; `model.ts` `proposedWork:` at 707 with `surfaces:` at 710; `routes.ts` 34-96 and 225-238 disjoint; `authorityLine` outside M3's five cited regions | yes |
| F16 / F17 | Q3 and Q4 decided below the table with reasoning shown; owner table is Q1 and Q2; the existing-route arm named in Q1 and declined, labelled [Inferred] | yes |
| F18 | four `[Unknown]` bullets in Collision (`:1248-1261`) matching the record's four `not_verifiable_this_session` entries; the third now carries 707-716 | yes |
| F19 | 0 non-fence lines with an odd backtick count over all 1,564 lines | yes |
| F20 | — | **repaired**, see H6 |
| F21 / F22 | PWB-REQ-020 introduced as "quoted in relevant part" naming the omitted bullets; `ResponseLimitFailure` and `MaterializationRecord` ranges exact; the POC spec path spelled in full at the Q1 and Gate 5 cites | yes |
| G1 | `materializ` = 0 in both signed specs (case-insensitively too), over 17 PWB and 24 POC `### Requirement:` headings; PWB-REQ-013 at spec `:723-740` is Group "Presentation", Form prohibition; the quoted words are `proposed-work.ts:11-12` inside the `:8-19` header comment | yes |
| G3 | 619 tracked files under `openspec/` and `.syzygy/` (`git ls-files -z`); `api/poc/polaris` returns exactly **1** hit, `PENDING-OWNER-DECISIONS.md:209`, the P-72 row; 0 in either signed spec | yes |
| G5 | the ten components reproduce; the totals are floors and now say so in both artifacts | yes |
| G6 | the breach body is `JSON.stringify` of `ResponseLimitFailure` at `routes.ts:141` | yes, and the scope defect H1 found is repaired |
| G7 | RFC2-24's defined clause: `DIRECTIVE-REGISTER.md:258` → `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:92`, table at 119-131; `:44-50` marked as the module summary | yes |
| G9 | `workItems.items` length 7,481, `len(set(ids))` 7,481 | yes |
| G10 / G11 | `targetBeadPrefix` set `materialization.ts:58` from `:12`; `designPath` built `materialize-action.ts:35`; three `renderMaterializePanel` call sites (`trajectory.ts:187`, `materialize-action.test.ts:42` and `:59`) | yes |
| G12 | (b) the capture path's base stated (`:350-356`); (a) now repaired, but the row itself is unmarked — **J5** | (a) partial |

No F1–F22 or G1–G12 finding regressed.

## The questions

| # | Scope truthful? | Genuine gate / genuinely not? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| **Q1** — does `GET /api/poc/briefing` need a spec delta, and to which spec? | Yes. The POC reader note reads exactly "the 'machine answer' is the authenticated `GET /api/poc` response" at spec `:25-26`, singular and definite, under "Reader notes, binding on how this file is read" (`:18`) [Observed]. The `/api/poc/polaris` precedent is real and now fully stated: a second `machine-credentialed` route (`routes.ts:237-238`) and a second machine-JSON body under the same ceiling (`:161`, `:175`), named by no requirement heading, 0 occurrences in either signed spec, 1 occurrence in 619 tracked governed files — this packet's own register row | **Genuine owner gate.** Whether a new route inside a signed spec is a CC-REV-2 spec delta is a determination about digest-bound text; VIS-4 reserves it. The act's bullet "Spec changes route through CC-REV-2's amendment path and a new owner act" (`:78-79`) and the trigger "any scope beyond the signed change" (`:93-94`) both point at the owner | Yes. Three lawful arms, each with its cost; the recommended PWB delta discloses its own queueing cost behind lane B (P-68); arm (c) moots Q1 and Q2 and is declined on stated grounds, labelled [Inferred]; the default is the conservative one and slices 1–2 are explicitly unaffected | Yes, clause by clause: three arms, the same recommendation, the lane-B/P-68 cost, the 8 MiB defect of arm (c), the same default, and the "slices 1–2 may proceed" carried in the row's *when* column. The row compresses arm (c)'s PWB-REQ-020 parity-oracle reason to its ceiling reason only — compression, not contradiction |
| **Q2** — how is the ceiling declared, and does a third amend PWB-REQ-006? | Yes, now. The registry facts are exact (seven fields `:65-73`, ceilings `:81-82`, the closed two-literal union `routes.ts:111`), the trigger is quoted at its line, and H2's kinds-versus-routes reading is stated, held and labelled [Inferred], with the fold-in tied to it | **Genuine owner gate** on either reading: minting a registry field crosses "a change to the constraints or envelope the registry entry declares" (act `:92`) whether or not PWB-REQ-006 requires it | Yes, and the fold-in is disclosed as the owner's call with the cost of each path. The default arm is stated *with* its defect ("a bound that could silently widen release by release"), not smoothed | **Partially.** Seven fields / two ceilings, the interface-and-union widening, the superseding registry act and its line-92 trigger, the fold-in conditional, the same recommendation and the same disclosed default all match — but the kinds-versus-routes holding, which is what makes the third ceiling discretionary rather than compelled, is in the packet and not in the row: **J2** |
| **Q3** (decided) — the breach body's `population` | **Yes**, on the current bytes. The sentence is limit-neutral, the widened type is named as the envelope all three sinks serve with each sink's line and ceiling identity, the briefing-scoped wording is withdrawn in place, and PWB-REQ-006's envelope clause is quoted at `:381-384` and read as a minimum with the label on it | **Genuinely not a hard gate.** `ResponseLimitFailure` is an implementation type in `apps/three-surface-poc/src/routes.ts` bound by no act; the one reading that would make it a gate (PWB-REQ-006's "only" as a closure of the field set) is named, labelled [Inferred], scoped to the two sinks the clause governs, and routed back to the funnel "before any sink's body changes"; and the decision is downstream of Q1 and Q2 so it cannot ship unseen. The restraint — no third `population` arm — is preserved and is the same restraint M2's Q5 and M4's Q2 apply | **Yes.** The limit-neutral sentence is true on a page breach, an `/api/poc` breach and a briefing breach alike, which is the property H1's repair (b) asked for; no sink states a subject it does not have. The pre-existing free-prose `reason: string` on the `unknown` arm (`routes.ts:128`) is named as untouched and is correctly not an Unknown *claim* reason | Yes — the row's Q3 parenthetical now carries the limit-neutral sentence, the shared-envelope fact ("every bounded sink serves, the human pages and `/api/poc` included") and the "only … carrying" minimum reading with its [Inferred] label |
| **Q4** (decided) — sequencing against M4 | Yes. The dependency is conceptual: the oracle reads `PocEpistemic` (`model.ts:44-46`) and the `resolutionRoutes` shape live, not a hand-copied list, so it self-corrects when M4 lands | **Genuinely not a gate.** A sequencing preference between two of the owner's own branches binds nothing and crosses no escalation trigger | Yes, and the one cost — a pre-M4 acceptance fixture documenting free-prose reasons as current behaviour — is accepted in the open with the evidence file told to say so | Yes — "(no ordering enforced against M4)" |

## Closed-vocabulary check

Predicate: every backticked kebab-case token of two to five segments
(`` `([a-z]+(-[a-z]+){1,4})` ``) in the packet, in the evidence record and
in the P-72 row, tested against RFC2-24's twelve read this session from
the defined clause's table (`rendering-vocabularies.md:119-131`, located
through `DIRECTIVE-REGISTER.md:258`). **18 distinct tokens**, all in the
packet, none in the twelve and none offered as an Unknown reason:
`baseline-spec`, `capability-to-intent`, `data-evaluation-id`,
`data-parity-field`, `declared-project-shape-text`, `human-open`,
`intent-to-work`, `machine-credentialed`, `materialize-status`,
`materialize-trigger`, `no-such-claim`, `no-write-to-observed-repository`,
`not-applicable`, `owner-trusted-bootstrap`,
`repair-whatsapp-identity-reconciliation`, `switchboard-identity`,
`three-surface-poc-core`, `topology-component`. `no-such-claim` occurs
three times, each inside a sentence withdrawing it. `not-applicable` is a
chain state, and the packet says in three places that the not-found and
not-applicable disclosures carry no `reason` field (`:911-940`, S2 at
`:1095-1108`, S6 at `:1122-1131`) — the RFC2-24 fact-of-render arm,
correctly applied. A separate sweep of the string `reason` over the
record and the row found only prose uses. **No `reason` value outside
RFC2-24's twelve is minted anywhere in the three artifacts** [Observed].

## Invariants on this review

- Problem scope holds: all four Gate 1 measurements re-derive exactly
  (18,710 / 5,520,314 = 0.3389%; `workItems` 2,273,467 + `codeStructure`
  1,493,219 = 68.2%; no requirement prose on either credentialed route;
  `externalRef`/`governingIntent`/`syzygy-poc:work:` 0; `mayNot` 0 and
  all four `forbidden`/`prohibit` hits in observed bead titles).
- Recommendation holds against the engineering bar: Gate 6's seven
  acceptance items are the M1/M2/M4 shape, and every new guard branch
  carries a rule-6 mutant — with the one exception J1 names.
- No owner trade-off smoothed: every recommendation carries its
  counter-argument, its cost and its default-if-unanswered; both
  withdrawn questions keep their numbers and their reasoning; the two
  readings of PWB-REQ-006 are both stated and the packet's choice is
  labelled.
- No lawful arm called unlawful: all three Q1 arms are presented as
  lawful on the packet's own reading, and the register says the same.
- Labels: substantive claims carry `[Observed]`, `[Inferred]` or
  `[Unknown]`; the four `[Unknown]`s reach the document the owner reads,
  not only the sidecar.
- Contract claims are quoted at defined clauses located through
  `DIRECTIVE-REGISTER.md`, and every quotation checked this session is
  verbatim at its cited lines (PWB-REQ-005 `:202-271`, PWB-REQ-006
  `:370-384`, PWB-REQ-007 `:443-448`, PWB-REQ-013 `:723-740`,
  PWB-REQ-020 `:902-927`, RFC2-24 `:92`, the POC reader note `:25-26`,
  the act `:68-94`).
- Zero/all claims carry a predicate and a denominator run this session:
  619 tracked governed files, 415 item ids, 7,481 work items, 17 + 24
  requirement headings, 1,564 packet lines, 18 kebab tokens, 4,870
  code-span references.
- Digests computed by `sha256sum` and `wc -c`, never transcribed; no
  manifest and no truncated signed digest is quoted in the packet, the
  record or the row (CG-7e and CG-15 both 0 findings); no Butlers path
  is backticked in the packet (CG-1b 0 findings over 4,870 references).
- `python3 scripts/check_governance.py` ends `0 FAIL`.

## Severity counts

- blocking: **0**
- non-blocking: **2** (J1, J2)
- editorial: **3** (J3, J4, J5)

Total 5 findings. Eight of review 3's nine findings are fully repaired
against the current bytes; H9 is partial (J1). No F1–F22 or G1–G12
finding regressed, and F20 and G12(a) — the two review-3 named as
regressed or unrepaired — are now repaired in substance, G12's own
disposition row excepted (J5). The blocking defect H1 found is repaired:
the widened envelope's sentence is limit-neutral and true on all three
bounded sinks, and the no-gate argument is re-run over the two sinks
PWB-REQ-006 governs with the contrary reading routed back to the owner.

Verdict: CONFIRM WITH EXCEPTIONS
