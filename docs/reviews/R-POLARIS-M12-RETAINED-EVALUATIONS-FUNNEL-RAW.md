# Review 1 (raw) — Polaris M12 retained-evaluations funnel packet

Independent fresh-context review. Read-only; no tracked file in any repo or
worktree was modified. This file is the only file written.

## Header

| Item | Value |
|---|---|
| Worktree | `…/scratchpad/m12wt`, branch `agent/syzygy-dov.12` |
| HEAD reviewed | `a55fe3a` (`docs: Polaris M12 retained-evaluations funnel packet [syzygy-dov.12]`) |
| Baseline the packet measures at | `a9f671e` |
| `git status --short` at finish | empty |
| `python3 scripts/check_governance.py` (tail line, read) | `32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted` |

Reviewed artifacts, sizes and digests computed this session with `wc -c` and
`sha256sum` (never transcribed):

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md` | 136105 | `d65c7860608bf8f1520c27ff71501bd9e8861c840aeec0177e2a70e0f58ab924` |
| `docs/evidence/polaris-m12-retained-evaluations-funnel-2026-09-15.json` | 31585 | `9765554e546c159b676df90b702984211cd9e7c2ac5c1361c52222cb3b28485f` |

`wc -l` of the packet: 1736 (matches the evidence record's `artifacts` block).

Sibling worktree heads read this session, all matching the packet's table:
`laneb` 4090f98, `m2wt` f2f37dd, `m3wt` 6574600, `m4wt` 63b8e33, `m5wt`
ba9ca61, `m6wt` 83c9f60, `m7wt` f97baf4, `m8wt` bce9039, `m9wt` 65de02b,
`m10wt` 95f31cb, `m11wt` bbd6837.

**Not run, and why.** `npm run build:poc` and `npm test` were not run: the
commit under review adds two documentation files and changes no code
(`git show --stat a55fe3a`: 2 files, 2577 insertions, both under `docs/`),
so no claim in the packet depends on a build or a suite. No daemon was
started, no provider was called, no Butlers checkout and nothing under
`.worktrees/` was read, and the retained capture's credential file was never
opened.

**Overall.** This is a strong packet. Every heavy measurement I could
re-derive did re-derive exactly, including the whole collision matrix (33
cells, plus the twelve-row frequency table), the write-verb sweep with its
eight-bucket partition summing to 56, the twelve-term specification sweep to
the matching line number, the 553-file act-corpus sweep, and the claim
population's 1,149 / 1,148 / 2-tuple / 177,031-byte figures. The doctrine,
RFC and specification quotations are exact at the cited lines with no unmarked
elision. One defect is blocking, and it is a quotation defect at the one
place where the packet rules against the dossier rather than asking.

## Findings

### F1 — blocking — the dossier's prerequisite line is misquoted, and the elided words are the evidence against the packet's own ruling

`docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md:76` (and again at
`:47` in the "One re-split" paragraph, and in the evidence record's
`dossier.prerequisiteLine`).

The packet writes: *The dossier gives M12 a `prerequisite` value of "none for
retention and delta; owner act for the note; spec amendment for dismissal".*

The dossier's actual line, `docs/pursuits/2026-09-13-vision-pursuit.md`
lines 415–416, read at source at `a9f671e`:

> - **Prerequisite.** None for retention and delta; owner act for the note
>   (retention posture); spec amendment for dismissal.

Two words — **(retention posture)** — are removed with no ellipsis and no
note. They are not incidental: they are the dossier naming the continuation
act's retention-posture trigger by the trigger's own noun. The packet then
rules, in "Decided in this packet, not put to the owner" (`:86`):

> what is not open is that the dossier's "none" was reached without the
> trigger list being read [Observed for the act text and the dossier value;
> Inferred for the consequence].

The `[Observed]` half of that label is attached to "the dossier value", and
the dossier value as published in the packet is not the dossier's value. On
the full line the ruling does not stand: the dossier did read retention
posture into this move — it attached the trigger to the *note's* owner act
rather than to slice 1's retention. That is a narrower and arguable
difference, and it is exactly the kind of difference the packet elsewhere
insists on preserving.

This matters because it is the packet's single strongest claim against the
dossier, it is presented as decided rather than asked, and the owner reading
the packet alone cannot see the words that qualify it.

**Repair.** Quote line 415–416 in full, with the parenthetical. Restate the
correction as what the evidence supports: the dossier attached the
retention-posture trigger to the note's owner act and gave "none" for
retention and delta, and whether the trigger reaches slice 1's derived record
is Q1. Drop the claim about what was or was not read, or relabel it
`[Inferred]` and mark it as a reading of another author's intent. The
evidence record's `dossier.prerequisiteLine` field must carry the full line
for the same reason.

### F2 — non-blocking — the `claim:item:` prefix figure is a tuple count published as an identity count, and the six figures do not sum to 1,148

`…FUNNEL.md:519-521`; evidence `measurements.claimPopulation.byIdentityPrefix`.

Packet: "By identity prefix: 278 `claim:source:`, **416** `claim:item:`, 439
`claim:fact:`, 9 `claim:class:`, 6 `claim:project-account:` and 1
`claim:project-shape`, summing to **1,148**."

Re-derived over `…/scratchpad/capture/api-poc.json` with the packet's own
predicate (recursive walk, every object carrying both `claimId` and
`epistemic`), counting **distinct identities**: `claim:source:` 278,
`claim:item:` **415**, `claim:fact:` 439, `claim:class:` 9,
`claim:project-account:` 6, `claim:project-shape` 1 — total 1,148.

The published six sum to 1,149, not 1,148. 416 is the count of item **claim
objects**; the one duplicated identity the packet itself discovers
(`projectShape.items[].claim` / `proposedWork.currentAuthority.claim`) is an
item claim, so the distinct-identity figure is one lower. This is the
per-tuple-never-per-id trap the packet cites AGENTS.md about, landing in the
packet's own table.

**Repair.** Publish 415 under "by identity prefix" and 416 under a separate
"by prefix, tuple instances" row; the arithmetic then closes at 1,148 and
1,149 respectively. Q1's own sentence (`:20`) reads as objects and is
internally consistent as it stands.

### F3 — non-blocking — "all five `claimId` sites" under-enumerates: there are six interpolating sites

`…FUNNEL.md:20` (Q1) and `:110-112`; evidence
`measurements.claimPopulation.claimIdConstructionSites = [367,375,383,403,430]`.

`packages/three-surface-poc-core/src/project-shape-model.ts` carries twelve
`claimId:` lines. Six interpolate: **367** (`claim:source:${coverage.path}`),
**375** (`claim:item:${item.class}:${item.key}`), **383**
(`claim:fact:${fact.fact}`), **403** (`claim:class:${coverage.class}`),
**430** and **447** (both `claim:project-account:${key}`). Line 447 is the
Unknown arm of `projectAccountOf` and is missing from the packet's list and
from the evidence record's array; the remaining six are the fixed literal
`'claim:project-shape'`.

The conclusion survives — line 447 interpolates the same closed-vocabulary
account key and no revision — but "all five" is a completeness claim with the
wrong denominator (verification rule 9).

**Repair.** Say six, and cite 447 beside 430.

### F4 — non-blocking — "1,148 carry an identity interpolated from observed-project text … exactly 1 is a fixed literal" overstates, on the packet's own load-bearing Q1 measurement

`…FUNNEL.md:20`.

Q1's argument for treating slice 1 as a retention-posture change rests on the
record holding "derived observed-project metadata: a claim identity per
claim", quantified as 1,148 of 1,149 interpolated from observed-project text
against exactly 1 fixed literal.

Re-derived: at least **31** of the 1,148 identities are composed wholly from
closed vocabularies fixed in Syzygy's own source and contain no observed text
at all —

- 9 `claim:class:<class>` from `EXTRACTION_CLASSES`
  (`packages/three-surface-poc-core/src/project-shape-manifest.ts`);
- 9 `claim:fact:count:<class>` from the same constant;
- 6 `claim:project-account:<key>` and 6 `claim:fact:project-account:<key>`
  from `PROJECT_ACCOUNT_KEYS`, a six-value literal at
  `packages/three-surface-poc-core/src/project-shape-extraction.ts` line 46;
- plus the 1 the packet already names.

The genuinely observed-derived population is 278 source paths, 415 item keys
and 9 catalog headings, with the remaining fact identities split as above
(`claim:fact:` decomposes 415 `item:`, 9 `count:`, 9 `catalog-count:`, 6
`project-account:`).

The Q1 conclusion is not reversed — 278 repository-relative paths in a
durable file is plenty of substance for the question — but the packet asks
the owner to weigh a number, and the number is ~31 too high in the direction
that favours its own recommendation.

**Repair.** Split the figure: observed-derived identities vs. identities
composed from Syzygy's own closed vocabularies, with the constant named.

### F5 — non-blocking — the challenge sweep's rejected predicate does not reproduce as stated, and "the 15-line difference was entirely in the non-test population" is false

`…FUNNEL.md:582-590` and `:1601-1603` (Gate 6); evidence
`measurements.challengeSweep.rejectedPredicate` / `rejectedPredicateLines`.

Denominator 246 `.ts` files under `apps/` and `packages/` re-derives exactly,
and the accepted predicate re-derives exactly: **50** lines, **25** test,
**25** non-test, with the packet's non-test partition (drawer 10,
project-shape-model 7, polaris-copy 4, polaris 3, walkthrough-preflight 1)
and its test partition (req-040 9, polaris-epistemic-tuples 6,
polaris-first-reading 4, project-shape-model.test 4, polaris-narrative 1,
polaris-proposed-work 1) both matching line for line.

The rejected predicate does not. Measured four ways over the same population,
with the packet's `challenge-suspended` exclusion applied:

| Predicate | Lines |
|---|---:|
| `\bchallenge\b` case-**sensitive**, with exclusion | **35** |
| `\bchallenge\b` case-insensitive, with exclusion | 36 |
| `\bchallenge\b` case-insensitive, no exclusion | 44 |
| `\bchallenge\b` case-sensitive, no exclusion | 43 |

The packet and the evidence record both state the predicate as
case-insensitive; only the case-sensitive form yields 35.

The distribution claim is wrong in a way that matters more. The 15-line
difference splits **7 non-test / 8 test**, not "entirely in the non-test
population" (stated in the Measurements and repeated in Gate 6). Worse, 5 of
the 7 non-test lines are in `packages/cap1-core/src/drawer.ts` — the
unrelated Capability 1 lifecycle the packet itself excludes from the seam —
so only **2** of the 15 (`project-shape-model.ts` lines 83 and 84) fall
inside the seam L2-M8 proposes to extend. The full difference set:

- test: `polaris-epistemic-tuples.test.ts:42`,
  `polaris-first-reading.test.ts:88`, `req-040.conformance.test.ts:163,196,
  225,227`, `project-shape-model.test.ts:19,351`;
- non-test: `drawer.ts:59,60,114,138,174`, `project-shape-model.ts:83,84`.

The packet's substantive point — that the word-boundary predicate misses
`CHALLENGE_STATES` and `ChallengeState` and so would misdescribe the seam —
is correct and survives.

**Repair.** State the rejected predicate as case-sensitive, and replace
"entirely in the non-test population" with the 7/8 split and the observation
that 2 of the 15 are the constant and the type.

### F6 — non-blocking — "586.3 is an upper bound on a post-trim renderer" is contradicted by the post-trim captures already in hand

`…FUNNEL.md:22` (Q3), `:747-753` (Measurements), evidence
`measurements.ceiling.rowsLabel` and `retainedPageIsPreTrim`.

The packet's per-tuple figures re-derive exactly on the pre-trim capture
(`…/scratchpad/capture/polaris-7478.html`, 2,090,025 bytes): **699** spans
matching `<span class="claim-tuple" … </span>`, total **409,829** bytes, mean
**586.3**, min **559**, max **661**.

The limiting sentence does not. Measured on the lane A *after* captures in
the same scratch tree the headroom figures are taken from
(`…/scratchpad/m1/measure/after/polaris-direct.html`, 1,478,637 bytes, and
`…/polaris-tailnet.html`, 1,484,487 bytes — both matching the evidence
record the packet cites): **713** spans, total **418,122**, mean **586.4**,
min 559, max 661, identical on both host forms. The post-trim per-tuple cost
is 0.1 bytes *higher*, not lower: lane A's trim removed narrative JSON and
list markup, not tuple spans.

The arithmetic is unaffected (612,665 / 1,172.8 still floors to 522), and the
row figure carries its `[Inferred]` label correctly. But the conservatism is
claimed, not measured, and the measurement that refutes it was available.

**Repair.** Either measure the post-trim page and publish 586.4, or drop
"upper bound" and say the per-tuple cost is stable across the trim.

### F7 — non-blocking — "M12's surface is the 15 existing files of Gate 3" does not describe the 15, and the packet never enumerates them

`…FUNNEL.md:1447`.

The collision predicates' denominator is named as Gate 3's existing-file set.
It is not. Gate 3's topology table names 12 existing files, two of which —
`apps/three-surface-poc/src/polaris-parity-sweep.test.ts` and
`apps/three-surface-poc/src/walkthrough-preflight.ts` — are **not** on the
surface; and the surface carries three files Gate 3's table never names —
`packages/three-surface-poc-core/src/body-read-authority.ts`,
`packages/three-surface-poc-core/src/walkthrough-judgment.ts` and
`packages/cap1-daemon/src/write-guard.ts` (plus
`project-shape-observation.ts` and `walkthrough-readiness.ts`, which appear
only in Gate 3's "Not touched by any slice" prose).

The 15 are enumerated only in the evidence record
(`collision.m12_surface`). Re-running all three predicates against that list
over the eleven sibling worktrees at the heads named reproduces **every cell**
of the collision table exactly — A, B-full, B-basename, the bolded
basename-only files on each row, the "moves 7 of 11 rows" claim (M1 lane B
0→1, M2 4→5, M5 3→4, M6 0→1, M7 1→2, M8 7→9, M9 2→6, with M3, M4, M10 and
M11 static), the two false absences under B-full, and the twelve-row
per-file frequency table including the three 0/11 files. So the figures are
right; only the prose's account of their denominator is wrong, and a reader
holding the packet alone cannot rebuild it.

**Repair.** Enumerate the 15 in the packet, or cite the evidence record's
`collision.m12_surface` by key.

### F8 — non-blocking — the twelve-file drift claim's denominator is under-specified, and one file it could be read to include did change

`…FUNNEL.md:41-46`.

"Every one of the **twelve** files M12's evidence cites is byte-identical
between those two commits … [the twelve are the nine implementation files and
three governance files named in Gate 0 and the Measurements]."

That parenthetical does not identify a set. Gate 0 names no implementation
file and six decisions plus a registry, a policy, two RFCs and a craft
policy; the Measurements name far more than nine implementation files,
including `apps/three-surface-poc/src/polaris.ts`,
`apps/three-surface-poc/src/routes.ts`, `packages/cap1-core/src/drawer.ts`
and `packages/cap1-daemon/src/credentials.ts`. `polaris.ts` **is** in
`git diff --name-only f4589e2 a9f671e` (146 rows, run this session).

Reconstructed as the twelve distinct files of the "Line numbers re-verified
at `a9f671e`" table — `main.ts`, `body-read-authority.ts`,
`walkthrough-judgment.ts`, `project-shape-manifest.ts`,
`project-shape-observation.ts`, `walkthrough-readiness.ts`,
`project-shape-model.ts`, `materialization.ts`, `materialize-action.ts`,
`vision.md`, `architecture.md` and the PWB `spec.md` — the claim is **true**:
0 of the twelve appear in the 146-row diff. I also checked every file the
dossier's M12 prose section and the five JSON objects (L2-M6/M7/M8, L2-F4,
L2-F5) cite, including `drawer.ts`, `facets.ts` and `pwb-mutation.ts`: none
appears in the diff, so the substantive conclusion — no M12 dossier citation
is stale because of drift — holds.

**Repair.** Name the twelve, or scope the sentence to the re-verification
table.

### F9 — editorial — `canonicalJson` import site mis-cited

`…FUNNEL.md:434`: "one import (336 of `project-shape-observation.ts`)". The
import is at line **36** (`canonicalJson,` inside the import list); line 336
is inside `resourceLimitsDigest`. The seven-occurrence total and the three
digest sites (`project-shape-observation.ts` 337 and 635,
`walkthrough-readiness.ts` 126) re-derive exactly, as does the definition at
333 with its head comment at 331–332.

### F10 — editorial — the M10 cross-reference contradicts itself

`…FUNNEL.md:952`: "**Q2 of the M10 packet** establishes that `inputsDigest`
is *insensitive* to the project shape … cited by **M10's Q1** at its packet
line 35". Read read-only at `95f31cb`: M10 line 35 is Q1 and is where the
insensitivity and the `model.test.ts` assertion are established; M10 line 36
is Q2, which asks about `Content-Encoding: gzip` and the response ceiling.
The first clause should say Q1.

### F11 — editorial — `MATERIALIZE_ATTRIBUTION` comment anchored one line late

`…FUNNEL.md:822` and `:1215`: the words "Fixed, never user-supplied — this
action is human-triggered but not human-identified" are attributed to
`apps/three-surface-poc/src/materialize-action.ts` lines 28–29. They are at
line **27**; 28–29 are the `export const MATERIALIZE_ATTRIBUTION = …`
declaration the comment describes. The packet's own rule 8 discipline
elsewhere is exact; this one is not.

### F12 — editorial — `vision.md:176-179` is called "the expiry sentence" and marked "exact"

`…FUNNEL.md:637` (re-verification table). The expiry sentence spans lines
**175–177**; the cited 176–179 opens mid-sentence and runs past the end of
exception (a) into exception (b)'s first two lines. The verdict column says
"exact, all three" for that row. It is L2-M6's span, not the packet's, but
the row's verdict overstates it — the same class of thing the packet
correctly flags one row above for `materialization.ts:78-145`.

## Q1–Q6 assessment

| Q | Scope truthful? | Genuine hard human gate? | Recommendation follows from the evidence? | All lawful arms named? |
|---|---|---|---|---|
| Q1 retention posture = escalation trigger? | Yes on the act text (continuation act 150–156 quoted whole and exact). **But see F1**: the dossier-comparison half of the framing rests on a misquotation, and the packet rules ("what is not open…") where it should ask | **Yes.** The act's own noun is "retention"; whether "beyond" reaches derived state is a reading only the owner may fix. Not ordinary engineering | Yes, and unusually well: the recommendation is fail-closed, the counter-argument is named "strong", and two narrower arms are offered. Nothing is smoothed | Yes — trigger it; rule it inside on the same-posture reading; rule it inside on the disclosure-limited reading; plus the stated default (slice 1 and 2 do not ship). No arm is called unlawful |
| Q2 what may a record hold, how long | Yes. VIS-6(b) at 177–179 is exact; the 177,031 / 203,379 byte figures re-derive to the byte | **Yes.** "Immutable" against a discard policy is a doctrine tension a delegate must not resolve; the packet says so in terms ("a delegate deciding how much of the project's history to destroy") | Yes, though the recommendation (unbounded) and the default (one prior evaluation) diverge — deliberately and disclosed, with the operational counter-argument stated | Yes — unbounded; cap by count with the discard counted; keep exactly one prior; cap by bytes. Four arms, default named |
| Q3 may the band spend M1's headroom | Yes. Every ceiling and headroom figure re-derives from the lane A record and the two subtractions are correct. **F6** qualifies the per-tuple limiting sentence | **Partly.** This is a budget allocation across two open moves, which is the owner's; the honesty constraint (no silently truncated band) is not open and the packet treats it as settled, correctly | Yes. The recommendation is the cheapest honest arm and the packet names M1's objection as the counter-argument rather than burying it | Yes — full band with declared cap and disclosed remainder; machine channel only (held behind M10's Q6, which the packet says); counts-only with a route. Default named |
| Q4 may a note be promoted by writing out | Yes, and carefully: the act's prohibition is quoted at 70–72 and is exact, and the packet does **not** rule that no future act could authorize it | **Yes.** An act in force forbids the write in terms and the registry bytes are digest-bound; only the owner can move either | Yes. "Do not build promotion in this move, and put the act question to the owner" follows from the act text, the digest binding and the 0-of-278 measurement | Yes — (a) new act plus CC-REV-2 over `writeSurface` plus a new registry act; (b) unpromoted stage 1 only; (c) promote into Syzygy's own `.syzygy/local/`, with its own objection stated; (d) do not build. The counter-argument to (b) is given |
| Q5 dismissal: implementation or amendment | Yes. PWB-REQ-007 at 443–446 and its Case line at 454–456 are exact; `CHALLENGE_STATES` at 83 with the comment at 81–82 is exact | **Yes.** Widening a closed vocabulary a signed requirement quantifies over is a CC-REV-2 matter by construction | Yes, and the packet explicitly declines to call the dismissal lawful or unlawful — only that the path is not conformance | Yes — amendment plus act; a sibling claim beside the tuple (with its VIS-6(a) objection named); do not build. The doctrinal bound on every arm is quoted, not argued |
| Q6 which evaluation owns a delta claim | Yes. architecture.md 221–229 is quoted whole and exact; M2's line 47 is quoted correctly and read read-only | **Yes.** It is a doctrinal question about what a claim may assert, and M2 reached the same fork and ruled its own — the packet flags the coupling without re-asking M2's question | Yes. The recommendation is the arm that mints no identity and keeps the pinned tuples byte-identical, with the strongest counter-argument stated and labelled a construction | Yes — claim of the current evaluation about two; a third identified evaluation; a non-normative rendering artifact. Default named |

**Defaults.** All six defaults are stated and all six fail closed (nothing
ships, or the smallest claim ships). None is unlawful on the material I
checked.

**Hidden owner questions in "Decided in this packet".** Eight of the nine
items in that section are measurement-backed corrections a delegate may
properly make (the M10 dependency, the tuple-only band, the duplicate
identity, the appenders, the persistence absence, the M11 test-assertion
carry-over, the two narrowed spans, the no-bead/no-row instruction). The
ninth is F1: the ruling on what the dossier's author did or did not read is
not a delegate's to make on the evidence given, and the evidence given is
incomplete. The four-slice re-split of a three-slice dossier move is
disclosed at `:50` with its reason and is properly a delegate's call.

**No lawful arm is called unlawful anywhere in the six rows**, and I found no
place where a trade-off is smoothed into consensus language — the
counter-arguments are the strongest part of the packet.

## Gate 5 — requirement-and-scenario test

Every requirement and scenario the packet cites exists at the cited line and
covers the consequence claimed:

| Cited | At `a9f671e` | Covers the slice's consequence? |
|---|---|---|
| PWB-REQ-007 heading, spec 439 | exact | — |
| PWB-REQ-007 text 443–446; Case 453–456; Oracle 459–463 | exact, verbatim | Yes for slice 2's join key ("two evaluations of the same semantic subjects"; "verify stable semantic identity across the two evaluation instances") and for slice 4's closed vocabulary |
| Scenario "Missing current evidence remains explicit Unknown" 470–474 | exact; AND limb as quoted | Partly — the packet says so itself: no scenario's WHEN limb names a rendered delta, and it discloses that residue |
| POC-REQ-032, POC spec 574; scenario "Unknown disclosed in the narrative" 599–604 | exact | Yes for the no-history named Unknown |
| PWB-REQ-020, spec 902; text 906–910; scenario "Complete model has wire parity" 928–933 ("the check reports both denominators") | exact | Yes for parity |
| PWB-REQ-014, spec 759; text 763–773; "Each anchor SHALL retain…" 770–771; "Personal view state SHALL remain outside the truth model" 772–773; "explicitly non-normative framing" 764–765; Case 778–782; Oracle 791–792; scenario 799 | exact, all | Yes as a *constraint* on slice 3; the packet states plainly that no requirement warrants the feature |
| PWB-REQ-022 text 1032–1035; Observable 985; twin scenario 1136–1141 | exact | Disclosed as the one specified retained record, in the opposite direction |
| PWB 322–327 "Later correlation preserves prior authorization history" | exact, quoted whole | Yes — and the packet's reading ("not a requirement that any evaluation be written to durable storage") is right |
| RFC2-26, `RFC-0002/rendering-vocabularies.md` heading 194, clause 196–221 | exact, both paragraphs, no elision | — |
| RFC5-11, `RFC-0005/admission-and-boundary.md` heading 242, clause 244–252 | exact, whole | Yes — a dismissal is on the claims side |
| VIS-6 167–181 (182 blank); VIS-2 96–106; VIS-1 82–94; SEC-4 47–52; SEC-5 54–60; architecture 56–57, 217–219, 221–229, 231–235 | exact, all; ellipses marked | — |
| Improvement-cycles direction 55–56; mode direction 18–19; impl act 59–63 (elision disclosed) and 70–72; continuation act 150–156 | exact, all | — |

**The slice 1 absence, re-run independently.** Twelve terms,
case-insensitive Python `re`, denominator 1,008 + 1,152 = **2,160** lines
over the two `spec.md` files. Every per-term count in the packet's table
re-derives exactly, including the hit line numbers: `retain` 0/15,
`retention` 0/0, `delta` 0/1 (PWB 823), `\bsince\b` 0/0, `annotat` 0/0,
`dismiss` 0/0, `expir` 0/1 (PWB 242), `\bnotes?\b` 1 (POC 18)/0, `history`
1 (POC 715)/5 (PWB 287, 322, 1092, 1103, 1136), `append-only` 0/0,
`previous` 0/2 (PWB 324, 1138), `changed` 0/3 (PWB 791, 922, 925). The five
PWB `history` hits are the two scenarios and three predicate/mutation lines,
as stated. `.syzygy/governance/records/` is absent: `.syzygy/governance/`
holds five directories (`contracts`, `decisions`, `declarations`, `doctrine`,
`policies`) and `git ls-files .syzygy/governance/records` returns 0. The
absence claim and its PWB-REQ-022 disclosure are both sound.

**No digest-bound byte is proposed for edit.** I checked the registry entry
(`"writeSurface": []` at line 125, status banner at line 4), the
classification policy (`rawBodyHandling` 178–184, five `"never"` members),
both `spec.md` files and the act records: all are quoted and none is edited.
`git show --stat a55fe3a` confirms the commit touches two `docs/` files only.

## Measurement table

| Claim | Re-derived? | My figure |
|---|---|---|
| `main.ts:134` is `const asOf = new Date().toISOString();` | yes | exact |
| `buildModel` declared at 113; `asOf` used at 148, 168, 175 | yes | exact |
| `buildModel()` called at exactly 2 sites (187, 201) | substance yes, **predicate no** | 2 call sites; but the stated literal predicate "`buildModel()` occurring in `main.ts`" returns **3** lines (113 is `function buildModel(): …`). Denominator 253 lines correct. Minor; folded into no finding beyond this row |
| `buildButlersPocModel(`: 3 non-test, 33 in tests, 36 total | yes | exact (model.ts:369 def, main.ts:171, test-model-fixture.ts:133) |
| Write sweep: 157 `.ts`, 81 non-test, 56 matching lines | yes | exact |
| Partition 11/31/2/3/2/1/6 = 56, "other" empty | yes | exact, exhaustive |
| 3 state-dir write sites at credentials 223–227, materialization 128–134, test-artifact 73–79, dir `0o700` file `0o600` | yes | exact |
| 0 of the 56 writes an evaluation/observation/claim state/judgment | yes | confirmed by reading all 56 |
| Retained capture state dir: 1 entry, 64 bytes, 0600 in 0700 | yes | exact (listed by name; contents not read) |
| `appendEvaluation` 757–767, head comment 754–756 | yes | exact, quoted whole correctly |
| `appendJudgmentEvaluation` 813–824, comment 810–812, mutation-point 818 | yes | exact |
| 11 sites, 2 definitions, 9 in tests, 0 in the package index | yes | 5 + 6; 4 + 5 in tests; index 0/0 |
| Neither history is persisted | yes | neither reads or writes a file; neither called outside its own test |
| `canonicalJson` at 333 (comment 331–332), 7 occurrences, 3 digest sites | yes | exact — but the import is at **36**, not 336 (F9) |
| Footer built at `routes.ts:92`, `polaris.ts:1630`, `polaris-source.ts:140` | yes | exact; those are the only three `footer:` sites interpolating `model.evaluation.snapshot`/`asOf` |
| `snapshot` composed at `model.ts:689`; `inputsDigest` at 381–389 (five keys), surfaced at 691 | yes | exact |
| Rendered snapshot 262 chars, instant 24 chars, four `\|`-joined fields | yes | exact (measured on the retained page; no digest value reproduced here) |
| Claim objects 1,149 / distinct 1,148 / 1 identity twice | yes | exact; the duplicate is at `projectShape.items[].claim` and `proposedWork.currentAuthority.claim`, with equal tuple and equal evaluation id |
| Exactly 2 distinct (epistemic, challenge) tuples: 1,137 + 12 | yes | exact |
| Canonical map 177,031 bytes; with routes 203,379; redundancy 26,348 | yes | exact to the byte |
| By identity prefix summing to 1,148 | **no** | 415 item, not 416; the published six sum to 1,149 (F2) |
| 1,148 identities interpolated from observed-project text, 1 fixed literal | **no** | ≥31 come from closed internal vocabularies (F4) |
| Five `claimId` construction sites, none interpolating a revision | **partly** | six sites (447 omitted); none interpolates a revision (F3) |
| `ProjectShapeClaim` 120–131; `claimId` doc comment 121–122 | yes | exact |
| `CHALLENGE_STATES` 83, `ChallengeState` 84, comment 81–82, field 129, producer 177 | yes | exact |
| L2-M8's `:89-102` is `UNKNOWN_REASON_ROUTES`, seam is 81–84 and 129 | yes | exact — the correction is right |
| Challenge sweep: 246 files, 50 lines, 25/25 split, full partition | yes | exact, both partitions line for line |
| Word-boundary predicate returns 35; difference entirely non-test | **no** | 35 only case-**sensitively**; the 15 split 7 non-test / 8 test, 5 of the 7 unrelated (F5) |
| `.syzygy/local/` and `.syzygy/cache/`: 0 of 556 tracked | yes | exact; `.syzygy` holds `governance`, `intent`, `map` |
| Repository tracks 1,216 files | yes | 1,216 at `a9f671e` (1,218 at `a55fe3a`, the two packet files) |
| 0 of 278 observed paths begin `.syzygy`; 0 carry segment `local`; 3 top-level segments; remainder [Unknown] | yes | exact, and the [Unknown] limiting sentence is honest |
| Ceilings 2,097,152 (line 81) / 8,388,608 (line 82) | yes | exact |
| Headroom 612,665 tailnet / 618,515 direct / 2,868,294 machine | yes | exact; both subtractions correct; lane A trim 654,019 and the 78,637 / 84,487 shortfalls against 1.4 MB also check |
| 699 tuple spans, mean 586.3, min 559, max 661, total 409,829 | yes | exact — but the "upper bound" gloss is wrong (F6) |
| 1,172.6 bytes/row; ~522 rows; `[Inferred]` | yes | 522; label correct |
| `state-dir.system.test.ts:294`; 19 `readdirSync` sites in 8 files; exactly one asserts a state directory's contents; spawns `apps/syzygy/dist/main.js` via harness 29–31 / 126–139 | yes | exact, all |
| PWB `tasks.md`: 138 lines, 35 boxes, 32 checked, open 4.6 / 5.2 / 5.3 | yes | exact |
| Register: 26 rows `^\| P-`, highest P-67, `P-7[0-9]` returns 0 | yes | exact; the P-79 forecast is consistent with the eleven siblings holding P-68…P-78, and the packet writes no row |
| Spec sizes: PWB 17 req / 31 scenarios / 1,152 lines; POC 24 / 24 / 1,008 | yes | exact |
| Act-corpus sweep: 538 + 24 + 7 = 553; 0 manifest rows, 0 act records; 8 of 15 in `pwb-truth-policy-amendment/IMPACT-LEDGER.md`; 1 in the 2026-09-09 mutation record; ledger's basename absent from both sibling manifests | yes | exact, every figure |
| `main.ts` 2 repo-wide, `index.ts` 4; other thirteen unique | yes | exact |
| Collision: A / B-full / B-basename on all 11 rows; 7 rows move; M1 lane B and M6 false zeros; 12-row frequency table; three 0/11 files | yes | **every cell exact**, against the evidence record's 15-file list (F7) |
| Twelve M12-cited files byte-identical `f4589e2`..`a9f671e` | yes for the re-verification table's twelve | 0 of 12 in the 146-row diff; denominator prose under-specified (F8) |
| Dossier: 552 / 5,014 / 4,596 lines, M12 at 403 | yes | exact |
| Dossier prerequisite line as quoted | **no** | "(retention posture)" elided unmarked (F1) |
| `materialization.ts:78-145` cited, record block 80–141 | yes | exact — 78 closes the interface, 141 closes `clearMaterializationRecordFile` |
| L2-F4's 0 functional hits for annotation / dismissal / presentationState / bookmark | yes | 3 incidental `annotation` comments (`drawer.ts` 24, 281; `facets.ts` 19), 0 for the other three |
| `READINESS_ARMS` closed at ten | yes | exact |
| Every code-span path resolves | yes | the 11 that do not are the ones the packet declares absent (`.syzygy/local/`, `.syzygy/cache/`, `.syzygy/governance/records/`, `project-shape-claim.ts`), the three proposed new modules, a gitignored build artifact and two globs/placeholders |
| ≤78 columns outside fences and tables | yes | 7 over-length lines, every one a line an unbreakable code span forces; no code span is broken across a line |
| No truncated signed digest, no manifest quotation, no Butlers path in backticks | yes | none found |
| `check_governance.py` ends `0 FAIL` | yes | tail line read, not grepped |

## Severity counts

blocking 1 · non-blocking 7 · editorial 4

Verdict: REVISE
