# M5 agent-briefing funnel — independent review 1 (raw, retained verbatim)

Reviewer: a fresh-context review session (Claude), no prior review of
this packet exists. Date: 2026-09-14. Read-only: no repository file was
edited and no state-changing command was run; this file is the only
write.

## Subject and digests

Worktree:
`scratchpad/m5wt`, branch `agent/syzygy-dov.5`, HEAD **1afa3d0**
(`git status --short` clean at review time).

| Reviewed file | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md` | 62830 | bd93b4f3dd65c3e57c8d749cceb2e70d150141caf7d24f973f7f725088eeebeb |
| `docs/evidence/polaris-m5-agent-briefing-funnel-2026-09-14.json` | 11502 | 7e733323b7f8b6ebf4a76c775b2ca7f0cf1b534e8fbecb5a0502324058c437e9 |

Measurement input, re-verified this session:

| Capture | Bytes | sha256 |
|---|---:|---|
| lane A "after" `api-poc.json` | 5520314 | a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e |

All three digests computed with `sha256sum` and all three sizes with
`wc -c` this session; none transcribed (rule 3). Every measurement
below was recomputed from the capture with `python3`, not read from
either artifact. `python3 scripts/check_governance.py` at this head
ends **`32 OK, 20 WARN, 0 FAIL (52 checks)`**; a grep of its full
output for `M5`, `m5-agent` and `agent-briefing` returns no finding
naming either reviewed file [Observed].

Line citations below are to the reviewed packet unless another file is
named; code and spec citations are to this worktree at 1afa3d0.

## What I re-derived, and what held

Recorded so a later reader need not redo it. All [Observed] this
session unless marked.

- Capture size and sha256 as stated.
- All nineteen per-top-level-key byte figures and shares in the
  Measurements table, to the byte and to four decimal places; the sum
  5,521,648 and the whole-file compact 5,521,960, so the stated
  312-byte gap is exact.
- `externalRef` 0, `governingIntent` 0, `syzygy-poc:work:` 0,
  `mayNot` 0, `prohibit` 1, `materializedBeadId` 1
  (`str.count` over the decoded text, confirmed a second way by
  `bytes.count` over the raw file — rule 2's second method).
- `projectShape.counts` 278 / 415 / 439 / 9; `authorizationMode`
  `owner-trusted-bootstrap`; all three authority states
  `owner-adopted (bootstrap, uncorrelated)` with
  `independentlyVerified: false`; the three act identities;
  `identity.scope`; `proposedWork.changeId`.
- The restricted `git diff --stat f4589e2..a9f671e` over the nine
  named files returns no rows, and the unrestricted one over `apps`
  and `packages` reports 31 files.
- The route table, and these code citations: `routes.ts` 159-162,
  221 (222 tailnet), 225-238; `browser-origin.ts` ends at 38;
  `materialize-action.ts` 17 and 55-82 and the seven parity fields at
  69-75; `polaris-source.ts` 33 and 41-42;
  `polaris-narrative.ts` 193-198; `project-shape-observation.ts`
  65-73, 75-83, with 2097152 at 81 and 8388608 at 82;
  `authority-disclosure.ts` 39-46; `model.ts` 42, 44-46, 98-155, with
  `proposedWork` at 140; `body-read-authority.ts` 315 and the
  write-surface checks at 677-684; the registry declaration JSON's
  `writeSurface` at 125 and `executeObservedCode` at 128;
  `packages/cap1-daemon/src/server.ts` 188-200.
- Doctrine and contract citations, each quoted text matching the
  cited lines: `vision.md` 39-41, 61-64, 82-94, 122, 141;
  `security.md` 10-23 (the SEC-1 sentence is at line 14) and 39-45;
  RFC8-21 at 79-91; RFC6-14 at 237-249; RFC6-22 at 390-402;
  `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` 68-84 and 86-94.
- The POC reader note at line 26 of
  `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`,
  under a heading that reads "Reader notes, binding on how this file
  is read" — so Q1's premise is sound, and the note is binding, not
  scaffolding.
- The Q1 absence claim, which I confirmed with a denominator the
  packet does not state: the literal `api/poc/polaris` occurs **0**
  times across every tracked file under `openspec/` and **0** times
  under `.syzygy/`, over a population of 17 PWB and 24 POC
  `### Requirement:` headings.
- The register's last row: P-67 is present in
  `PENDING-OWNER-DECISIONS.md` (two occurrences, outside the
  `| P-nn |` table rows, which stop at P-53).
- The minimal-orientation figures reproduce, with a caveat recorded
  as F7 below: 18,710 bytes when the composed object's keys are
  spelled short, 18,719 exactly when they are spelled as the evidence
  file's own field list ("identity.scope" is 9 bytes longer than
  "scope"); 148,780 and 148,815 the same way (+9, +13, +13).

## Findings

### F1 — blocking — `forbidden` is 3 on this capture, not 0

`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:128-131` and the
Measurements table row at `:276`.

**Defect.** Gate 1's fourth headline measurement reads "The literal
`mayNot` occurs 0 times; `forbidden` occurs 0 times on this capture
(3 on the dossier's pre-lane-A capture, all inside Butlers bead titles
that moved with the catalog — not a Syzygy change)", and the table
prints `forbidden | 0 | 3`. Recomputed this session by the packet's own
stated method: **3**, confirmed a second way over the raw bytes. The
packet's own evidence file agrees with me and contradicts the packet —
`literal_substring_counts.this_capture.forbidden` is `3`, and
`dossier_pre_lane_a_capture.forbidden` is `3`. So the packet states a
false [Observed] count and then invents a causal story for a change
that did not occur. All three hits, and the single `prohibit` hit, sit
inside Butlers bead titles in `workItems` (offsets 1541039, 1585658,
3312753 and 1518492), which is what makes the underlying point
survivable.

**Repair.** State 3 on both captures. The honest form of the claim is
that the machine payload names zero prohibitions *of Syzygy's own
authority* — every literal match is an observed Butlers bead title,
not a statement of what the consumer may not do. Drop the "moved with
the catalog" sentence entirely.

### F2 — blocking — the worked example's chain is applicable, and the subject count is four, not three

`:139-155` (the "subject-naming finding"), `:261`, `:633-636`,
`:770-774` (S6), and `agent_briefing_sets.one_claim_briefing_example`
in the evidence file.

**Defect.** The packet's one new measurement, its S6 illustration and
its Gate 4 chain design all rest on the claim that
`claim:baseline-spec:switchboard-identity` touches none of the
hardcoded work-related literals and therefore renders
`chain: not-applicable`. The capture says otherwise, twice:

- `proposedWork.specKey` is `switchboard-identity`, and
  `proposedWork.currentAuthority.claim.claimId` is **exactly**
  `claim:item:baseline-spec:switchboard-identity` — the packet's own
  chosen subject. The packet even prints
  `proposedWork.currentAuthority.kind` / `.key` as
  `baseline-spec` / `switchboard-identity` in its own table at `:291`,
  two hundred lines from the claim it contradicts.
- `MaterializationGoverningIntent.requirementId`
  (`packages/three-surface-poc-core/src/materialization.ts:15`) is the
  fixed literal `'REQ-switchboard-identity-001'` — a **fourth**
  hardcoded-or-observed subject the packet's "three distinct subjects"
  finding never names, and one that names this same claim.

So the packet chose, as its counterexample for "a subject none of the
literals touch", the one subject two of them do touch. The premise
(three literals differ from each other) is true; the conclusion drawn
for this subject does not follow and is falsified by the capture.

**Repair.** Restate the finding as four literals, name
`switchboard-identity` as their join point rather than a
counterexample, choose a genuinely unjoined subject for the
not-applicable illustration and for S6, and re-derive the one-claim
measurement against whichever subject survives.

### F3 — blocking — S2 mints an Unknown reason outside RFC2-24's closed twelve

`:646-648` (Gate 4 slice 3) and `:750-753` (scenario S2).

**Defect.** Both specify the unresolvable-selector response as
`{kind: 'unknown', reason: 'no-such-claim', subject: <selector>}`.
RFC2-24 (in
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`,
clause at 92-117, table at 119-131) closes the Unknown-reason
vocabulary at twelve values; `no-such-claim` is not among them
(nearest is #11 `reference-unresolvable`). The clause is explicit in
terms: "no implementation may mint, spell, or force-fit a ... value
the list does not carry", and it supplies the remedy for exactly this
condition — "A condition genuinely not among the twelve is disclosed
as a **fact of the render** — named, expandable, routed to its
resolving action — never dressed as a reason."

Three governing texts converge, one of them quoted by the packet
itself:

- PWB-REQ-007 (spec 443-450): "Unknown reasons SHALL use RFC2-24
  values verbatim and expose their resolution routes"; its Falsifier
  fires on "a tuple field is absent/out of vocabulary, a reason has no
  route". The packet cites PWB-REQ-007 exactly once, and only as
  "PWB-REQ-007-adjacent identity rules" (`:670-671`); it never reads
  the clause.
- RFC6-14, quoted by the packet at `:444-449`: every claim instance in
  a machine answer carries its epistemic state verbatim from the RFC
  0002 vocabulary. The packet's own gloss — "it re-labels nothing" —
  is false of S2.
- The packet's own success criterion 4 (`:186-188`): "Zero new
  epistemic or closed-vocabulary values exist anywhere in the
  implementation that RFC2-10, RFC2-24, RFC2-25 or PWB-REQ-004's
  closed population do not already carry."

**Repair.** Either resolve the condition to #11 with its route, or
disclose it as a fact of the render in a carrier that is not a
`reason` slot. Restate S2 accordingly and keep criterion 4, or state
plainly which vocabulary the packet is asking the owner to widen and
put that to the owner as a question.

### F4 — blocking — `PwbResourceLimits` has seven fields, not two

`:52` (Q2).

**Defect.** Q2 opens "`PwbResourceLimits`
(`packages/three-surface-poc-core/src/project-shape-observation.ts`
lines 65-73) has **exactly two fields**, `maxHumanResponseBytes`
(2,097,152) and `maxMachineResponseBytes` (8,388,608), both
digest-bound inside the registry entry". Lines 65-73 are the whole
interface and carry **seven**: `maxSources`, `maxBytesPerSource`,
`maxTotalBytes`, `maxIndexDepth`, `maxParsePassesPerSource`, and the
two named. The cited range contradicts the stated count at the cited
lines (rule 4), and an "exactly N" claim is the family rule 2
governs.

This is material, not cosmetic: the owner weighing Q2 is being shown a
two-field type where the real object is a seven-field, registry-declared
resource envelope, which changes what "mint a new field in the registry
entry" costs.

**Repair.** "has exactly two response-ceiling fields among seven".

### F5 — blocking — the line-number re-verification table is itself unreliable

The table at `:302-318`, plus `:52`, `:123-124` and `:650-652`.

**Defect.** The packet's central methodological claim is that it
re-derived every line number and corrected the dossier's imprecision:
"every line number below is current at `a9f671e`". Four cited ranges
are wrong, and two of the four are rows of the correction table
itself:

| Packet says | Actual at 1afa3d0 | Where |
|---|---|---|
| `boundedResponse`, `routes.ts` 111-121 | **137-142** (111 is the `ResponseLimitIdentity` type) | `:52` (Q2) and `:650-652` (Gate 4) |
| `buildTrajectoryMaterializationPacket`, `materialize-action.ts` 30-34 | **31-37** | `:123-124` |
| `MaterializationPacket`, `materialization.ts` 24-29 | **20-30** | table row `:312` |
| `buildMaterializationPacket`, `materialization.ts` 41-64 | **43-65** | table row `:313` |

The `boundedResponse` citation is load-bearing twice — it is the
warrant for Q2's "the function is generic over which
`ResponseLimitIdentity` it is passed" and for slice 3's ceiling
design — and it points at neither the function nor its body.

**Repair.** Correct all four and re-derive every row of the table
mechanically rather than by hand; a table that exists to correct
someone else's citations has to be re-derivable itself (rule 3).

### F6 — blocking — the dispatch packet has nine fields, the page renders seven, so "byte-identical" parity is unachievable and three values would be machine-only

Success criterion 2 at `:173-179`, the parity test at `:545-550`,
scenario S4 at `:760-763`, and the design-bar paragraph at `:694-696`.

**Defect.** `MaterializationPacket`
(`packages/three-surface-poc-core/src/materialization.ts:20-30`)
carries nine fields. `renderMaterializePanel`
(`apps/three-surface-poc/src/materialize-action.ts:69-75`) renders
seven `data-parity-field` values, and its governing-intent cell
renders `requirementId` and `proposalPath` only. So the page never
renders:

- `targetBeadPrefix` (declared at `materialization.ts:12`),
- `governingIntent.designPath` (declared at `materialization.ts:14-18`),
- and, for slice 1's own `state` arm, `at` — the status line at
  `materialize-action.ts:61-62` carries the bead id and nothing else.

A grep for `targetBeadPrefix` and `designPath` across `trajectory.ts`
and `materialize-action.ts` returns one hit, the build-site assignment
at `materialize-action.ts:35` [Observed].

Three consequences, all stated wrongly in the packet:

1. Criterion 2's "byte-identical to what the Trajectory panel renders,
   asserted by a parity test" cannot hold: two packet fields are not
   rendered at all, and the seven that are are HTML-escaped text, not
   the packet's bytes.
2. S4's "every one of the packet's **seven** fields" is the wrong
   denominator — 7 of 9 (rule 4).
3. Under the packet's **own** bidirectional reading of PWB-REQ-020 at
   `:414-419` ("or the Falsifier's 'missing... in either channel'
   fires"), three machine-side values with no human counterpart fire
   that Falsifier. This contradicts Gate 4's "The dispatch packet's
   *existing* rendering (the Trajectory panel) is unchanged in
   appearance; slice 1 only refactors where its data comes from"
   (`:694-696`) and is the one place in the packet where
   machine-more-than-page is created rather than avoided.

**Repair.** State the denominator as 7 of 9 plus the state arm; either
render the remaining values on the panel (which makes slice 1 a human-
surface change, not a pure refactor) or name the asymmetry, say why
PWB-REQ-020's Falsifier does not reach it, and label that reading
[Inferred].

### F7 — non-blocking — the one-claim figure is not re-derivable and the two artifacts disagree

`:261`, `:655-658`; evidence file
`agent_briefing_sets.one_claim_briefing_example`.

**Defect.** The packet says 2,829 bytes / 0.051%; its own evidence file
says 2,804 / 0.0508%. Neither is reproducible from the enumerated field
list, which is the only method given. Composing the packet's own
enumeration from the capture — evaluation identity, consent scope, full
authority block, the claim's tuple, one chain marker and empty Unknown
and exclusion arms — I get **3,198** bytes; adding "its one matching
source", which the packet's row explicitly includes, gives **4,835**
(the matching source record alone is 1,627 bytes compact). The figure
carries Q2's "roughly sevenfold headroom" argument, so it is not
decorative.

**Repair.** Publish the composition as exact field paths, or state the
figure as an estimate and drop the sevenfold claim.

### F8 — non-blocking — the cross-capture comparison is a key-naming artifact, not a measurement

`:94-100` and the two "dossier's own figure" rows at `:258` and
`:260`.

**Defect.** The packet reports 18,719 bytes on this capture against the
dossier's 18,710 on the pre-lane-A one, and reads the 9-byte
difference as real ("the two captures' ... shares differ ... because
the two revisions' bead and file counts differ"). Composing the same
fourteen fields from **this** capture with short key names yields
exactly **18,710**; spelling the keys as the evidence file's own field
list ("identity.scope" for "scope") yields exactly **18,719**. The
delta is 9 bytes of key name. The same holds for the second row:
148,780 short, and 148,780 + 9 + 13 + 13 = 148,815 when
"projectShape.classes" and "projectShape.claim" are spelled out.

**Repair.** Either compose both captures with one key spelling, or drop
the cross-capture byte comparison and keep only the share comparison,
which is the part the argument needs.

### F9 — non-blocking — the worked-example selector matches no claim in the population

`:261`, `:622`, `:655-656`; evidence file, same object.

**Defect.** Every `claim.claimId` in `projectShape.items` on this
capture has the form `claim:item:<class>:<key>` — 415 of 415, with
`item` the only second segment present [Observed, swept this session].
The packet's selector is `claim:baseline-spec:switchboard-identity`,
which matches **0**. Since slice 3's only selector form is
`for=claim:<claimId>` (`:622`), the packet's own worked example would
resolve to the S2 Unknown rather than to a briefing.

**Repair.** Use `claim:item:baseline-spec:switchboard-identity`, or
state that the selector is a shorthand slice 3 must resolve and design
that resolution step.

### F10 — non-blocking — the 511-byte item record does not reproduce

`:114-117`.

**Defect.** "the one `switchboard-identity` item in
`projectShape.items` carries a 511-byte record of class, key, state,
one anchor ... and the claim tuple". Measured: **661** bytes compact,
694 pretty-printed; the `claim` sub-object alone is 504 and the
non-claim remainder 148. No stated or obvious method yields 511.

**Repair.** Recompute, or drop the number — the sentence's point (the
record carries no requirement id and no statement text) does not need
it and is true.

### F11 — non-blocking — PWB-REQ-006 is never cited, and it governs two of the four questions

Gate 2 (`:320-467`) and Gate 5 (`:698-740`); denominator: six distinct
PWB-REQ identifiers appear anywhere in the packet — 004, 005, 007,
013, 014, 020 — and 006 is not one of them [Observed, swept].

**Defect.** PWB-REQ-006 (spec 340-386) is the requirement that says
"The registry SHALL declare **one** evaluation-wide resource envelope
... Final encoded human HTML and machine JSON SHALL **each** have an
explicit byte ceiling", that specifies the breach envelope's contents
("evaluation identity, limit identity, declared value, observed value
and population counts"), and whose Case sweeps "both final-output
sinks". Q2 proposes a third ceiling and slice 3 adds a third sink; Q3
proposes changing the breach body. Both questions land inside this
requirement, and the packet reaches them through a code comment in
`routes.ts` instead.

**Consequence for Q2.** The packet frames the ceiling as a registry
act alone. A third declared ceiling plausibly also stales
PWB-REQ-006's two-sink Case, which would fold it into Q1's spec delta
rather than making it a separate second act — a materially different
cost than the "two-step act" the handoff describes at `:964-969`.

**Repair.** Read PWB-REQ-006 into Gate 2, and re-ask Q2 with the
spec-amendment question attached.

### F12 — non-blocking — Q2's "without new code" is false, and the restraint is applied asymmetrically

`:52` (Q2) against `:53` (Q3).

**Defect.** Q2 recommends minting `maxBriefingResponseBytes` on the
ground that "a declared, digest-bound number is the only form of
'ceiling' `boundedResponse` ... already enforces **without new code** —
the function is generic over which `ResponseLimitIdentity` it is
passed". `ResponseLimitIdentity` (`routes.ts:111`) is a closed union of
exactly two string literals. Minting a third ceiling widens that union
**and** the `PwbResourceLimits` interface: new code, and a
closed-vocabulary widening. Q3, one row later, declines to "widen a
closed type on this packet's own authority" for `population`. The two
rows apply opposite restraint to the same kind of act without the
packet noticing, which is an owner trade-off smoothed away rather than
surfaced.

**Repair.** State the widening plainly in Q2 and either defend it or
put the asymmetry to the owner.

### F13 — non-blocking — Gate 5's warrant for slice 2 is circular, and the reading is unlabelled

`:704-708`, with the supporting reading at `:414-419`.

**Defect.** "PWB-REQ-020 already *requires* `mayNot` to render on both
channels once it exists, per Gate 2's reading; adding the field is
conformance with a Case this requirement's own text already reaches,
not an amendment to it." PWB-REQ-020 is a parity invariant over what
Polaris presents. It constrains a disclosure that exists; it is silent
on whether a new disclosure class may be minted. The question that
actually decides whether slice 2 needs an act — may the implementation
mint a disclosure no requirement names? — is never asked. Separately,
the claim that `mayNot` rows are "a form of 'body-read authority
state' disclosure under this Case's own enumeration" is an inference
about the scope of a digest-bound clause and carries no [Inferred]
label.

**Repair.** Label the reading, and either ask the minting question or
say why it does not arise.

### F14 — non-blocking — slice 2's enumeration of the act's prohibitions is three bullets short

`:581-586`, with the registration proposal at `:592-597`.

**Defect.** The packet enumerates the "What this does not authorize"
bullets of `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 68-84 and
lists six items drawn from three of the six bullets. Omitted whole:

- line 75, "No production release, broad remote access, or multi-user
  support";
- lines 76-79, "No edit to any act-bound artifact ... Spec changes
  route through CC-REV-2's amendment path and a new owner act" —
  which is, incidentally, the clause Q1 turns on;
- lines 82-84, "No independent verification: this authorization ... is
  a state-(1) human direction."

Slice 2 proposes a hand-typed **closed** table of exactly these
bullets, registered against "the act file's bullet count", so the
packet's own enumeration would seed that table at half strength and
the registration check would then lock the wrong count in.

**Repair.** Enumerate all six bullets, and state the count the
registration fixture must assert.

### F15 — non-blocking — the collision analysis reads 2 of 8 M4 slices and 1 of 6 M2 slices

`:776-846`, read against the sibling packets in
`scratchpad/m4wt` and `scratchpad/m2wt` (read-only).

**Defect.** The section asserts "**No line range overlaps**" for M2 and
"**No file lines actually collide**" for M4. Both are stated
unqualified over an under-enumerated population (rule 9). Unexamined
slices that touch M5's own regions:

- **M4 slice 8 (deferred), "Packet per claim; the queue", edits
  `packages/three-surface-poc-core/src/materialization.ts` lines 9-65**
  — the same artifact M5 slice 1 exposes, and the direct successor to
  M5's own multi-subject finding. Never mentioned.
- M4 slice 4 edits `model.ts` lines 710-750. In this worktree
  `buildModel`'s returned `proposedWork:` is line 707 and the
  `surfaces:` array opens at line **710** — three lines from where M5
  slice 1 inserts `dispatch`. Adjacent, not overlapping, but not
  checked.
- M4 slice 5 edits `routes.ts` lines 34-96, where M5 slice 3 adds a
  route. Not checked.
- The M3 row names only `polaris.ts` 346-361 of M3's five cited
  regions (306-307, 346-361, 506-510, 1307, 1328-1329).

**What I confirmed on the packet's behalf.** The conclusion appears to
survive: `authorityLine`, the function M5 slice 2 edits, is at
`apps/three-surface-poc/src/polaris.ts:707-713`, outside all five M3
regions; and `model.ts` is at the same commit in the m4wt and m5wt
worktrees, so the 707/710 adjacency is real and is not a
merge-blocking overlap [Observed].

**Repair.** State the denominator (slices examined of slices existing)
and add M4 slice 8, which is the one with a genuine semantic
relationship to M5 slice 1.

### F16 — non-blocking — Q3 and Q4 are not genuine hard human gates

`:53` and `:54`.

**Defect.** Q3 asks how `ResponseLimitFailure.population` should read
on a briefing breach. That type lives in
`apps/three-surface-poc/src/routes.ts`, is bound by no act, and
PWB-REQ-006 requires only "population counts";
the row's own default concedes "no type change either way". Q4 asks
in which order two of the owner's own branches should land, and
answers "no ordering is enforced". Neither needs an owner act; both are
ordinary engineering and planning judgment presented as owner
questions, which spends the scarcest resource the funnel exists to
protect. Q1 and Q2 are genuine — Q1 crosses "any scope beyond the
signed change" and Q2 crosses "a change to the constraints or envelope
the registry entry declares", both literal escalation triggers at act
lines 86-94 [Observed].

Two related omissions in Q3: AGENTS.md records that a response-ceiling
breach "serves nothing and logs nothing" — the 503 body is the only
trace — which is exactly the fact that decides how much the proposed
prose sentence is worth, and it is not cited.

**Repair.** Decide Q3 and Q4 in the packet with the reasoning shown,
and put two questions to the owner rather than four.

### F17 — non-blocking — a lawful, cheaper arm for Q1 is never named

`:51`, against the rejected alternatives at `:668-678`.

**Defect.** Q1 offers two arms, both of which amend a signed
specification. A third arm exists and moots the question: serve the
briefing **on the route that already exists** — `GET /api/poc` with a
selector query parameter, or as a field on the model — which mints no
route, raises no reader-note question, needs no new
`ResponseLimitIdentity`, and therefore clears Q1, Q2 and Q3 together.
The packet rejects folding the briefing into `/api/poc/polaris`
(correctly: that route is a presentation artifact, confirmed at
`polaris-narrative.ts:193-198`) but never considers `/api/poc` itself.
The trade-off against it is real and statable — the whole point of the
move is that an agent should not pay for the whole body — but a
parameterised route need not serve the whole body, and the owner is
entitled to weigh that before being asked to amend a signed spec.

**Repair.** Name the arm and state why it is or is not preferred.

### F18 — non-blocking — zero [Unknown] labels in the document the owner reads

11 `[Observed`, 1 `[Inferred`, **0** `[Unknown` across the packet
[Observed, counted].

**Defect.** The evidence file carries four `not_verifiable_this_session`
entries, including whether M3's `polaris.ts` edits would textually
conflict with slice 2 — the very question F15 is about. None of the
four appears in the packet as [Unknown]; the closest is an unlabelled
hedge, "re-check the exact function boundaries once either lands"
(`:801-803`). VIS-2's "no evidence yields Unknown" governs the artifact
the owner reads, not only its sidecar.

**Repair.** Carry the four forward into the packet as labelled
Unknowns.

### F19 — editorial — ten code spans are broken across a line break

Lines 25/26, 135/136, 346/347, 381/382, 478/479, 574/575, 646/647,
732/733, 755/756, 892/893 (each pair carries an odd backtick count;
detected by parity outside fences).

**Defect.** AGENTS.md's guardrail is explicit: "Never let a reflow
break a code span", because half a filename on each line is invisible
to every basename sweep. The worst case is 892-893, which splits
`` `tsc -b packages/three-surface-poc-core` `` so the package path
appears in no single line; 755-756 splits the two route paths in S3.

**Repair.** Reflow so each code span is whole on one line.

### F20 — editorial — nine over-width lines outside tables and fences

Lines 2, 11, 224, 302, 376, 422, 445, 576, 795 exceed 78 columns.
Lines 376, 422, 445 and 576 are single unbreakable paths and are
acceptable; 2 and 224 are headings; 302 is 81; **795 is ordinary prose
at 114 columns** and is the one to fix.

### F21 — editorial — PWB-REQ-020 is introduced as "quoted in full" and is not

`:400-412`.

**Defect.** Only the SHALL, the Observable and the Falsifier appear.
The Case, the Oracle, the Oracle-independence bullet and the
**Mutation proof** bullet are omitted, and the two surviving bullets
are re-punctuated with a leading em dash the source does not carry. The
omitted Mutation-proof bullet is the one Gate 6 item 4 leans on
("independently inject a missing, duplicated, changed, collapsed and
wrong-evaluation marker ... report both channel denominators").

**Repair.** Say "quoted in relevant part", as the packet correctly does
for its other long quotations.

### F22 — editorial — four remaining citation imprecisions

- `ResponseLimitFailure.population` cited as `routes.ts` 113-121
  (`:53`); the interface is 113-124 and `population` is 120-122, so
  the range names neither and omits the `unknown` arm.
- The materialization record cited as `materialization.ts` 67-76
  (`:525-526`); the interface is 67-78, with `createdAt` at 71.
- `browserRequestAllowed` cited as `browser-origin.ts` 24-38
  (`:104-105`); the declaration is at 26, the doc comment starts at 24
  and the file ends at 38 — acceptable, recorded for completeness.
- The POC reader note cited as a bare "line 26" three times (`:51`,
  `:62`, `:732`) with no file. The line is correct in
  `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`;
  name it, since the change directory holds four files.

## The four questions

| # | Scope truthful? | Genuine hard human gate? | Recommendation follows from the evidence? | All lawful arms named? |
|---|---|---|---|---|
| Q1 — spec delta for a new machine-credentialed route | **Partly.** The premise holds: the reader note at spec line 26 is definitional and binding, and `api/poc/polaris` occurs 0 times across `openspec/` and `.syzygy/` over 41 requirement headings (confirmed with a denominator the packet does not state, F22/absence). But the framing rests on the four bad citations of F5 | **Yes.** "any scope beyond the signed change" and "No edit to any act-bound artifact ... Spec changes route through CC-REV-2's amendment path and a new owner act" are both literal, at act lines 76-79 and 93-94 | **Partly.** The PWB-vs-POC arms are both stated with their costs, and the lane-B queueing consequence is surfaced honestly against the recommendation's own arm — good practice. It does not survive F17's unnamed third arm | **No.** Serving the briefing on the existing `/api/poc` behind a selector mints no route and moots Q1, Q2 and Q3 together (F17) |
| Q2 — how the briefing's ceiling is declared | **No.** "exactly two fields" is false — seven (F4); "without new code" is false — `ResponseLimitIdentity` is a closed two-literal union (F12) | **Yes.** "a change to the constraints or envelope the registry entry declares", act line 92 | **Partly.** The direction is right, but the cost is understated: PWB-REQ-006 declares *one* envelope and *two* output ceilings, so a third may fold into Q1's delta rather than being a separate second act (F11) | **Mostly.** The default arm (test-only bound) is stated with its defect disclosed. No arm is called unlawful |
| Q3 — the breach body's `population` | **Yes**, as far as it goes; PWB-REQ-006, which specifies the envelope's contents, is not cited (F11) | **No.** `ResponseLimitFailure` is an implementation type bound by no act; PWB-REQ-006 asks only for "population counts"; the row's own default is "no type change either way" (F16) | **Yes**, on the merits — the disclosure sentence is lawful and the restraint is right | **Yes**, and neither arm is called unlawful. But the restraint here contradicts Q2's (F12) |
| Q4 — sequencing against M4 | **Yes** | **No.** A sequencing preference between two of the owner's own branches, answered "no ordering is enforced" (F16) | **Yes.** The oracle-self-corrects argument is sound and the rework claim checks out | **Yes** |

**Any lawful arm called unlawful?** No. The packet nowhere declares a
lawful option forbidden, and its one self-imposed rule ("a new route in
a signed spec is a spec delta") is correctly attributed to its own
reading rather than to an authority.

**Any owner trade-off smoothed into consensus?** Two. F12, where Q2's
"without new code" hides a closed-vocabulary widening that Q3 refuses
one row later; and F13, where slice 2's need for an act is settled by a
circular reading of PWB-REQ-020 instead of by asking whether a
disclosure no requirement names may be minted at all.

## Invariants on this review

No manifest row, act argument or truncated signed digest is quoted; no
Butlers repository path appears in a code span; the three digests above
are full sha256 values of unbound working files, computed this session;
every substantive claim is labelled or is a directly quoted source;
every zero/all/exactly claim above carries its predicate and
denominator; prose is wrapped at 78 columns with no code span broken
across a line.

## Severity counts

- blocking: **6** (F1, F2, F3, F4, F5, F6)
- non-blocking: **12** (F7, F8, F9, F10, F11, F12, F13, F14, F15,
  F16, F17, F18)
- editorial: **4** (F19, F20, F21, F22)
- total: **22**

The packet's structure, its gate discipline, its honest surfacing of
the lane-B queueing cost against its own recommendation, and its
correction of the dossier's `POLARIS_SOURCE_PATH` citations are all
sound work, and most of its measurement table reproduces to the byte.
The blocking findings are concentrated in the places a reader would
trust most: a headline count that contradicts its own evidence file, a
worked example whose subject falsifies the analysis it illustrates, a
minted vocabulary value in a scenario, an "exactly two" that is seven, a
correction table with four wrong corrections, and a parity criterion
that cannot hold at the stated denominator.

Verdict: REVISE
