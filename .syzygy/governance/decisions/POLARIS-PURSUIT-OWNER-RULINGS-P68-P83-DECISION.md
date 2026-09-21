# Polaris pursuit moves M2–M16 and lane B — the owner's rulings on P-68…P-83 (2026-09-21)

> **Status: ruled and being applied.** The sixteen register rows P-68…P-83
> (fifteen feature-request funnel packets under `docs/design/`, one per
> pursuit move M2–M16, plus the lane B direction question) were answered by
> the owner on 2026-09-21 in a local questionnaire packet
> (`.syzygy/local/`, git-ignored; its eight raw adversarial reviews are
> retained beside it and are never edited). Every one of the packet's
> seventeen items (P-71 carried a second item, `P-71-Q5`) had passed
> independent review before it was put to the owner, and the owner took the
> recommended option on each with no edits. This record owns the rulings;
> each funnel packet remains the question it was ruled on. Where this file
> and the owner's own words differ, the words win, and they are quoted
> below. Nothing here is an act: no digest is bound, no specification,
> policy or registry byte changes, and no acceptance-record row is added. It
> is a plain owner direction in the shape of the P-60…P-65 and P-67 rulings
> (`PWB-CYCLE-OWNER-RULINGS-DECISION.md`,
> `POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`). Where a ruling below
> says a slice "proceeds now", it proceeds under the act the funnel packet
> named for it — nothing here widens any act.

## The owner's reply, verbatim

Each item's decision block in the local packet was recorded by the owner
walking the packet in the Claude Code CLI on 2026-09-21 as
`Status: Agreed`, `Owner edits: None`, choosing the recommended option.
The owner then wrote, in chat, 2026-09-21:

> I've walked through the user-questionnaire dossier. Are we ready to
> proceed with beads crystallization now?

and, to the reply that the answers first had to be routed here as a dated
owner direction and then crystallized into beads in two classes (ready
under acts in force; blocked on a named gate):

> Yes please go ahead

Evidence snapshot the items were reviewed and answered at: Syzygy
`b7a29f2` (main, clean apart from the co-lead's in-flight `AGENTS.md` and
an untracked OpenSpec change directory). The funnel packets' own evidence
records (`docs/evidence/polaris-m*-funnel-*.json`) were computed at
`a9f671e` and earlier, as each packet states.

## The seventeen rulings

Each row is its own decision; agreement to one is not approval of another.
"A" is the recommended arm in every case, as presented, except P-69 where
the packet's recommendation was its arm B. Slice numbers are the funnel
packet's own; "ready" means schedulable now under the act the packet names,
"blocked" means it waits on the named gate bead, which is an owner act or a
CC-REV-2 package that binds nothing until the owner signs it.

| Row | Ruled | What it means | Applied by (beads, all under `syzygy-dov`) |
|---|---|---|---|
| **P-68** (lane B) | **A** — proceed: an RFC-0007 successor ceremony, then the contract act, then the PWB behavior act, then implement. | This answer authorizes no act and no implementation. Next lawful steps, each a separate dated owner act: implementation-plane tooling for an RFC-0007 successor (no governed bytes edited); the held PWB-REQ-007 qualifier applied and a further review over the post-review-4 repairs; then the contract act offered; then the PWB behavior act. The package's sign-off phrase is offered only at that point. | `syzygy-dov.17` (notes updated); its manifest disposition gates `.2.2`, `.26`, `.13.2`, `.15.1`. |
| **P-69** (M2) | **B** — Q7 discloses the missing RFC2-9 bound outside the freshness slot, the claim stays Unknown; Q7a = instrument (i), a CC-REV-2 clarification scenario to PWB-REQ-007, gated behind its own sign-off and act before slice 5; Q1–Q6 as the packet recommends. | Slices 1–4 and 6 ready under the 2026-09-05 continuation act. Slice 5 (the declared bound) waits for a registry-entry amendment act, a continuation act, P-68's ruling before any M2 spec package, and the Q7a scenario's sign-off and act; until then no claim renders the disclosure route. No timer or background poller on any arm. | Ready `.2.1`; blocked `.2.2` on gates `.18` (registry act), `.19` (continuation act), `.20` (Q7a scenario), `.17`. |
| **P-70** (M3) | **A** — the M3 bundle as recommended; Q2's freshness half follows P-69's answer (disclosure route). | Slices 1–4 after M2 slices 1–4 under the continuation act, in parallel with lane B; slices 5–6 after them. No M3 slice opens a PWB specification package. | `.3.1` (after `.2.1`), `.3.2` (after `.3.1`). |
| **P-71** (M4) | **A** — Q1 non-conformance repaired via slice 1; Q2 no mint; Q3 arm (b), a pure drafter that writes no file; Q4 every reason, owner-actionable first; Q6 true by construction; Q7 slices 3–5 routed through one CC-REV-2 scenario for the opening-band aggregate. | Slices 1–2 after M3 slice 5 under the continuation act; slice 3 only after the three-way opening-band reconciliation and the scenario's sign-off; slices 4–5 behind the same scenario; slice 7's drafter writes no file; slice 8 waits on its own acts and is not filed. The write-surface language of the 2026-09-02 act is not amended. | `.4.1` (after `.3.2`); blocked `.4.2` on gate `.21`. |
| **P-71-Q5** (M4 slice 6) | **A** — Reading B: the return path's write into Butlers is foreclosed by the 2026-09-02 act; slice 6 does not run. | No write into Butlers or any repository. The route may stay wired but is not run; a future run needs (1) a dated owner act naming the write, (2) a registry-entry amendment act taking `writeSurface` from empty to the named path, in that order, then a fresh implementation authorization. | No bead; recorded in `.4.1`'s description. |
| **P-72** (M5) | **A** — Q1 one PWB semantic delta naming a closed "derived read-only machine view" category covering the machine Polaris route and the briefing; Q2 mint `maxBriefingResponseBytes` under a superseding registry act, the fold-in ruled now. | The delta is drafted (binds nothing until sign-off) and the registry act prepared; slice 3 waits for both. Slices 1–2 ready now under the continuation act. No route is served before its ceiling is declared. Q2 and P-69 Q2(a) travel as one superseding registry act. | Ready `.5.1`; blocked `.5.2` on gates `.22` (machine-view delta), `.18`. |
| **P-73** (M6) | **A** — Q1 implementation; Q2 defer the support discriminant; Q3 fail closed; Q4 regenerate the example with a separated illustrative block; Q5 install line plus fresh-install battery assertion in `build:poc`; Q6 the generator implementation act covers slices 1, 2, 3, 5; slice 4 once its CC-REV-2 scenario for the edit-stage deletion is signed off. | Slices 1, 2, 3, 5 under `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`, implementation-plane files only; no schema, prompt or kit file inside a bound package is edited; no provider egress or new source read. **This record is the direction naming slice 4**: it proceeds only after that scenario is signed off (drafting may start at once and binds nothing). | Ready `.6.1`, `.6.2`; blocked `.6.3` on gate `.23`. |
| **P-76** (M7) | **A** — Q1 `git-tree-entry` admitted as the fifth RFC7-10 class; Q2 an observing project reading its own tree, recorded here, needs no consent record, registry entry or act; Q3 folded into P-72's delta as a second declared category; Q4 P-71's arm (b); Q5 an implementation of REQ-008 conditioned on retaining the replay prohibition for in-flight or uncertain identities. | Slice 1 may claim RFC7-10 conformance now that Q1 is recorded; slice 3 is bounded to Syzygy's own tracked governed corpus with zero egress; slice 4's route waits for P-72's delta and registry act and its drafter writes no file; slice 6 limb (b) lands with the replay prohibition retained and its evidence record re-digested; slices 2, 5, 6(a) under the generator act. No provider egress. | Ready `.7.1`; blocked `.7.2` on gates `.22`, `.18`. |
| **P-75** (M9) | **A** — Q1 one CC-REV-2 package against the three-surface spec only, started after lane B's manifest is disposed of; Q2 PWB-REQ-007 reaches only the project-shape plane; Q3 the seven outside kinds sit outside the closed table, repaired by a new requirement in slice 3's delta plus disclosure, never at the bound site; Q4 `Inferred` added as a typed landing zone with no production constructor; Q5 the byte order slice 1, 2, 6a, 4's 18 tuples, 5's ribbon last at one-capability scale; **Q6 general**: any pursuit slice tracing to a recorded finding lands under `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`'s second limb, not confined to M9. | Slices 1–2 ready under the improvement-cycles direction; slice 3's delta is drafted only after P-68's manifest is disposed of and binds nothing until sign-off; slices 4–8 after that sign-off; slice 5 never at catalog fan-out without re-measurement. The bound coverage-matrix row is edited on no arm. Q6's general reading is what P-74 Q7, P-77 Q4 and P-83 Q3 rest on. | Ready `.9.1`; gate `.26` (after `.17`); blocked `.9.2` on `.26`. |
| **P-74** (M8) | **A** — Q1 ride the existing act for slices 1, 3, 4, 6, 7, hold 2 and 5; Q2 one registry-entry amendment act before slice 5's fifth limb only, the first four limbs thread a profile parameter with current constants as default; Q3 three acts scoped to a test-only self-observation (consent record, second registry entry, secret-policy extension) before slice 6 runs; Q4 configuration after admission, PWB-REQ-005's population stays 195; Q5 derive the name, keep the claim role non-normative, file the anchored-fact promotion separately; Q6 delete the tagline and render nothing until a profile supplies owner-declared framing with disclosure; Q7 yes, one shared-model change under WIP one. | Slices 1, 3, 4, 6 (design) and 7 under the PWB implementation act as continued 2026-09-05. **Slice 7 occupies the shared-model WIP-one slot first** and nothing else touches `PocModel` while it is open. Slice 5's fifth limb waits for the registry act; slice 6 runs only after the three acts exist, each separate and dated; slice 2 is held behind the loaded profile. The consent record, the registry entry and PWB-REQ-005 are edited on no arm. | Ready `.8.1` (slice 7, WIP-one), `.8.2`; `.8.3` (limbs 1–4); blocked `.8.4` on gate `.24`, `.8.5` on `.8.4`, `.8.6` on gate `.25`. |
| **P-77** (M10) | **A** — Q1 a response-identity digest over the canonically serialized body with an enumerated 25-path exclusion set, an implementation of POC-REQ-004; Q2 compression needs a dated owner act on the ceiling reading before it ships; Q3 `machine-credentialed`; Q4 trace under the improvement-cycles direction's second limb per P-75 Q6; Q5 a sibling join key, never an anchor identity, behind M9; Q6 every new machine field added to the parity sweep as its own family with a declared empty human denominator. | The digest field takes the shared-model WIP-one slot **in turn after M8 slice 7**; the route table and conditional GET after it; the schema document additionally after P-72's delta; compression lands nowhere before its act; the join key behind M9's identity slices. The registry entry is edited on no arm. | `.10.1` (after `.8.1`), `.10.2`; blocked `.10.3` on gate `.22`, `.10.4` on gate `.27`, `.10.5` on `.9.2`. |
| **P-78** (M11) | **A** — Q1 machine form `machine-credentialed`, human form on the existing `human-open` pages; Q2 a stderr line is not an emission to the requester, slice 1 logs the breach with population counts; Q3 an implementation of PWB-REQ-006's two quoted sentences, no delta; Q4 no new limit, breaches recorded against the two ceilings the registry already declares; Q5 in `pageShell`, above the fold, under 400 bytes. | Slices 1 and 4 now; slice 3 flips PWB-REQ-021 readiness with no registry or specification edit; the human breach line lands with its byte cost recorded; slice 2's machine route waits for P-72's category ruling. The registry entry is edited on no arm. | Ready `.11.1`; blocked `.11.2` on gate `.22`. |
| **P-79** (M12) | **A** — Q1 yes, a retention-posture change needing an owner act before slice 1; Q2 claim identity plus epistemic tuple and challenge state only, unbounded, on-disk total rendered beside the delta; Q3 the band capped at a declared row count, remainder a counted routed Unknown; Q4 no promotion, the stage-1 unpromoted note only (VIS-6(a) personal presentation state), write act deferred; Q5 dismissal is an amendment — CC-REV-2 delta plus a new act before any dismissal touches a tuple; Q6 the delta is a claim of the current evaluation about two evaluations, carrying both identities, never a freshness value. | Nothing in M12 is ready: slices 1–2 wait for the retention act; the note follows slice 1 and lives in the daemon's own state directory, never in an observed repository; slice 4 waits for the dismissal delta, its sign-off and act. No registry, act or specification byte is edited by this answer. | Blocked `.12.1` on gate `.28`; `.12.2` on `.12.1`; `.12.3` on gate `.29`. |
| **P-80** (M13) | **A** — Q1 arm (b), progressive enhancement over native `<details>`, the complete population always served, the checker holding the RFC9-13 hidden-count invariant; Q2 yes, hoist the source record into columns, no delta; Q3 an engineering decision inside the existing act, every interpolated form added to the copy oracle's population as its own string; Q4 stateless; Q5 slices 1, 2, 4 trip no trigger, slices 3 and 5 are reading (ii). | **This record is the direction naming slices 3 and 5.** Slices 1–4 proceed; slice 5 is designed only after lane B lands or is closed, ships stateless, and its hidden-count invariant gets a rule-6 mutant before it lands. The bound coverage row is edited on no arm. | Ready `.13.1`; blocked `.13.2` on `.17`. |
| **P-81** (M14) | **A** — Q1 yes for the 77 non-baseline sources with a render mode, never for the 9 withheld (seven TOML butler manifests, one frontend page, one excluded artifact), gated behind a CC-REV-2 scenario to PWB-REQ-011 and the act that follows sign-off; Q2 a scroll anchor with the whole spec still served, landing with slice 1; Q3 one legend sentence in `POLARIS_COPY`; Q4 machine figures Observed, sums Inferred, the 417-minus-415 delta Unknown; Q5 draft the PWB-REQ-015 delta only. | Slices 3–4 now; slice 5 drafts a delta that binds nothing and whose implementation needs a fresh authorization; slices 1–2 land together after the scenario's act, with the 9 withheld sources still refused and the parity sweep extended over the anchor parameter. No source outside the consented content class is read. | Ready `.14.1`, `.14.2` (drafting); blocked `.14.3` on gate `.30`. |
| **P-82** (M15) | **A** — Q1 arm (b), draft the delta only; Q2 design `partially-extracted` inside it, build only after sign-off and a fresh authorization; Q3 design the `unenumerated-heading` reason as surface-flag (a counted, routed Unknown); Q4 design the root-independence flags in the same delta. | One CC-REV-2 semantic delta to PWB-REQ-002 under `NORMATIVE-CHANGE-WORKFLOW.md`, sequenced behind lane B's open manifest; no extraction, manifest or coverage code changes; no Butlers source read beyond the consented class. | `.15.1` (after `.17`). |
| **P-83** (M16) | **A** — build Q1 (the sweep re-run on a scratch worktree, new dated evidence beside the 2026-09-04 record), Q2 (branded `Html`, byte-identical), Q3 (assistive-technology equivalent plus marker, fixture-guarded, under P-75 Q6's general ruling), Q4 (mechanical split, landed alone); design only Q5 (SVG diagrams as a feature-request candidate); Q6 split — build the token/type-scale cleanup with a grep guard and record the theme sentence in `docs/POLARIS-READING-LAYOUT.md`, design the light palette and the curation generalization. | Six improvement-cycle beads under `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`; design halves re-enter through feature-request before any build. No spec, doctrine, registry or act byte is touched. | `.16.1` … `.16.6`, all ready. |

## Cross-cutting readings this record fixes

- **One registry act, not two.** P-69 Q2(a) (the declared currency bound)
  and P-72 Q2 (`maxBriefingResponseBytes`) are prepared as one superseding
  registry-entry amendment act (gate bead `syzygy-dov.18`). Preparing the
  packet is agent work; performing it is the owner's.
- **The shared-model WIP-one order.** M8 slice 7 (`syzygy-dov.8.1`) takes
  the slot first; M10's response-identity digest (`syzygy-dov.10.1`)
  takes it next. Nothing else touches `PocModel` while either is open.
- **P-75 Q6 is general.** Any pursuit slice tracing to a recorded finding
  lands under the improvement-cycles direction's second limb. P-74 Q7,
  P-77 Q4 and P-83 Q3 were answered on that reading.
- **Three slices are named by this record and by nothing else:** M6 slice
  4 (P-73 Q6, still behind its scenario's sign-off), and M13 slices 3 and
  5 (P-80 Q5, reading (ii)).
- **One slice is closed rather than filed:** M4 slice 6 (P-71-Q5). No
  agent runs the return path into Butlers on this record.
- **The machine-view delta (gate `syzygy-dov.22`) is the widest gate**:
  M5 slice 3, M7 slice 4, M10's schema document and M11's machine status
  route all wait on it, and the second declared category (P-76 Q3) travels
  inside it.

## Crystallization, in one sentence

Fifty-six beads [Observed — created 2026-09-21, ids listed in the table]:
thirteen gate beads `syzygy-dov.18`…`.30`, each an owner act or a CC-REV-2
package that binds nothing until signed, and forty-three slice beads under
the move beads, of which twenty are ready under acts in force and the rest
depend on a named gate; `bd ready` is the live answer to which, and this
table is not.
