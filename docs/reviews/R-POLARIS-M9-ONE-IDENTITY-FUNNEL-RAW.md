# R-M9-ONE-IDENTITY-FUNNEL-1-RAW

Independent fresh-context review 1 of the M9 one-identity funnel packet.
No prior review exists for these bytes.

## Subject and digests

Worktree `scratchpad/m9wt`, branch `agent/syzygy-dov.9`, HEAD
`206d77549436f9c9b3c5918c978bbfcf5abe5697` (subject: "docs: Polaris M9
one-identity funnel packet, first draft [syzygy-dov.9]"). Baseline of
the packet's own measurements: Syzygy `a9f671e` on main.

Computed this session with `wc -c` and `sha256sum`, never transcribed:

| File | bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` | 93626 | `ae0ec92c4c7f858e85160704b799c21c39b34e86cb9fe7d2b685169e21c09e26` |
| `docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json` | 30164 | `38ef8d5ef25a550a8d511d5fcbe9954ffdf96e4662d942bbb0b0d647dd5be54a` |

Sibling worktrees read read-only at these HEADs: `laneb` `4090f98`,
`m2wt` `f2f37dd`, `m3wt` `6574600`, `m4wt` `63b8e33`, `m5wt` `ba9ca61`,
`m6wt` `83c9f60`, `m7wt` `0c4b4a9`, `m8wt` `8035c8f`.

`python3 scripts/check_governance.py` run in `m9wt` this session; last
last line read, not grepped, reads 32 OK, 20 WARN and 0 FAIL over 52
checks, counts derived rather than asserted. `git status --short` in
`m9wt` is empty at the end of this review; no tracked file and no
`node_modules` entry was modified. No daemon was started, no provider
was called, and no Butlers checkout was read.

Scope note: this review re-derives every substantive figure in the
packet's "Measurements at `a9f671e`" section and the evidence record,
opens every clause the packet quotes at its cited path and line, and
recomputes the collision section against all eight siblings. Findings
are numbered F1…F21.

## Findings

### F1 — blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:266-267`;
`docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json`
(`captures_used.four_page_capture.provenance`).

**Defect.** The packet states one provenance for the four-page capture
— "provenance 2026-09-10 loopback daemon" (packet line 266-267) — and
the evidence record states it for five named files: "[Observed]
owner's loopback daemon, evaluation Butlers 66ed58f / observer a121591,
as-of 2026-09-10", over `home.html`, `polaris-7478.html`,
`trajectory-7478.html`, `orrery-7478.html`, `api-poc.json`. That
provenance is false for two of the five. Read this session out of the
captures' own embedded evaluation blocks:

- `polaris-7478.html` carries `butlers:66ed58f…`, `observer:a12159…`
  and `2026-09-10T01:50:48` — as stated. [Observed]
- `home.html` carries `butlers:7c8743f6…`, `observer:f4589e2…` and
  `2026-09-13T02:03:33`. [Observed]
- `api-poc.json` carries the same `butlers:7c8743f6…` /
  `observer:f4589e2…` snapshot and `asOf` `2026-09-13T02:03:33.040Z`.
  [Observed]
- `trajectory-7478.html` and `orrery-7478.html` embed no snapshot
  label, so their provenance is [Unknown] from the bytes alone; their
  mtimes group with `polaris-7478.html`, not with `home.html`.

The retained `capture/run.sh` and `capture/daemon.log` in the same
directory show what actually produced `home.html` and `api-poc.json`: a
**private** daemon (`npm run poc -- --repo … --port 0 --state-dir …`,
served at `127.0.0.1:41215`), at observed revision `7c8743f6…`, not the
loopback daemon at all. The same run's `capture/polaris.html` is 838
bytes of `{"served":"nothing","failure":"response-limit-breached"…}`,
which is why the drafter had to substitute a `-7478` Polaris page — so
the substitution is visible in the directory and was not carried into
the record.

This matters beyond bookkeeping. The packet's central Q2 measurement —
1,167 epistemic-labelled objects, 1,137 with a tier, 30 without, 18 of
them the nine entities and nine relationships — is computed over that
`api-poc.json`, i.e. over an evaluation two Butlers revisions and three
days away from the one the record names, and mixed in one table with
page figures from a different evaluation. Gate 6 bullet 1 claims every
served figure was taken "over the named retained captures … with the
capture's own provenance stated"; for two of the five files it was not.

**Mitigation, stated for the owner's benefit.** I recomputed the whole
epistemic census over *both* retained `api-poc.json` files (the
`capture/` one and `m1/measure/after/` one). They agree exactly:
1,167 / 1,137 / 12 / 9 / 9, labels Observed 1,146, Unknown 21, Inferred
0, tiers `report-fact` 1,137 and 0 of the other five, freshness `fresh`
1,149, challenge `unchallenged` 1,149, Unknown primary reasons
`excluded-content` 12 and 0 of the other eleven. So no *number* moves.
The defect is the stated provenance, not the arithmetic.

**Repair.** Correct the record and the packet to name each served
figure's actual capture and evaluation: `home.html` and `api-poc.json`
from the private daemon at Butlers `7c8743f6…` / observer `f4589e2…`,
as-of 2026-09-13; `polaris-7478.html` from the loopback daemon at
Butlers `66ed58f…` / observer `a12159…`, as-of 2026-09-10;
`trajectory-7478.html` and `orrery-7478.html` provenance [Unknown] from
the bytes, asserted only from the capture directory's own log. Say in
the packet that the four-page census mixes two evaluations, and say
which figures depend on which.

### F2 — blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1060-1067`.

**Defect.** The packet writes of M7 and M8: "**[Unknown]** in content —
this session has not read them … They are disjoint from M9 by design,
on the orchestrator's assignment; M9's surface is the four rendered
pages, the shared POC model and the cap1-core epistemic tuple, and any
overlap would show up as a conflict at merge rather than as a
governance collision."

The disjointness sentence is an unlabeled substantive claim, and it is
false. Recomputed this session under the packet's own predicate B (code
spans naming an implementation-plane path inside the sibling's "Gate 3
— Topology" section, resolving in that sibling's worktree, fences
stripped), against the packet's own ten-file surface:

| Sibling | HEAD | B spans | B ∩ M9 |
|---|---|---:|---:|
| M7 (`m7wt`) | `0c4b4a9` | 11 | **1** |
| M8 (`m8wt`) | `8035c8f` | 19 | **6** |

M8's six are `model.ts`, `orrery.ts`, `polaris-copy.ts`, `polaris.ts`,
`routes.ts` and `trajectory.ts` — a larger intersection than any
sibling except M4, and it includes
`packages/three-surface-poc-core/src/model.ts`. M8's Gate 3 slice 7 row
reads "`packages/three-surface-poc-core/src/model.ts`, a new seed
module beside it, …". [Observed]

Under the packet's own reasoning this is precisely a governance
collision, not a merge conflict: the packet's collision item 2 says the
2026-08-29 direction's "work-in-progress limit of **one** for
shared-model changes applies across packets, not only within one".
M8 goes further and asks the owner about it directly — M8's Q7 reads
"Slice 7 rewrites the shared `PocModel` type. Does that trigger the
improvement-cycle ceremony the owner's direction sets — work-in-progress
one, review → repair → confirm → owner report before the next cycle?"
That is the same subject as M9's Q6 and M9's stated slice ordering.
[Observed, read in `m8wt` at `8035c8f`]

**Repair.** Delete the disjointness assertion or replace it with the
measured intersection. Either read the two packets and give them rows
in the collision table, or state plainly that they were not read and
that the overlap is therefore [Unknown] — but do not assert
disjointness. Add M8 to collision item 2 (the shared-model queue) and
disclose that M8 Q7 and M9 Q6 put overlapping ceremony questions to the
owner.

### F3 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:409-417` (the ceiling
table).

**Defect.** Two rows of the ceiling table — `/trajectory` (2026-09-10)
254,168 and `/orrery` (2026-09-10) 37,048 — are the byte counts of
`trajectory-7478.html` and `orrery-7478.html`, i.e. measured through
the loopback daemon on 7478. `AGENTS.md` records "Never measure through
the loopback daemon on 7478". The rule's stated scope is measuring
`/polaris`, and the packet's `/polaris` rows are correctly taken from
the lane-A private-daemon capture, so this is narrower than a rule
breach; but the packet's own Q5 recommendation tells each future bead
to re-measure "on a committed clean tree per `AGENTS.md`'s measurement
rule" while two of its own rows are taken the way that rule warns
against, and the packet never says which row came from which daemon.

A related omission: the same retained directory holds
`capture/polaris-7478.html` at **2,090,025** bytes — 7,127 bytes under
the 2 MB ceiling — and `capture/polaris.html`, a 503 breach body
recording `observed` 2,132,656 against `declared` 2,097,152 at Butlers
`7c8743f6…`. Neither appears anywhere in the packet, in a section whose
whole subject is headroom. [Observed]

**Repair.** Label each ceiling row with its daemon and evaluation. Add
the two pre-lane-A Polaris observations, so the owner sees that the
618,515-byte headroom is one evaluation's figure and that the same page
breached the ceiling on a different Butlers revision a week earlier.

### F4 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:156` and the funnel
summary at line 1157.

**Defect.** Gate 1's headline reads "**Ten attribute names carry an
entity identity across the four served pages**", and the evidence
record carries `distinct_names_union = 10`. The union is **eleven**.
Recomputed under the packet's own stated predicate (any attribute whose
value is exactly one of the nine `model.entities` ids) over the four
named captures: home three — `id`, `data-entity-id`, `data-surface-entity`;
Polaris eight — `data-polaris-section`, `data-claim-provenance`,
`data-unknown-disclosure`, `data-argument-ref`,
`data-capability-deep-dive`, `data-depth-dive`, `data-depth-source`,
`data-proposal-capability`;
Orrery two — `id`, `data-entity-id`; Trajectory none. The per-page
counts 3 / 8 / 2 / 0 match the packet's table exactly, and "not one
appears on more than two" is confirmed — the union is 3 + 8 = 11,
because Orrery's two are already home's. [Observed]

**Repair.** Eleven, in Gate 1, the funnel summary and the record.

### F5 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:993`, `1010-1013`, and
Gate 3's table at 519-528.

**Defect.** The collision section intersects siblings with "M9's
ten-file candidate surface, listed in Gate 3". Gate 3 does not list ten
implementation files; it lists **eleven** —
`apps/three-surface-poc/src/exact-tables.ts` appears in the slice 4a
and slice 6 rows and is absent from the intersection surface (as are
four test files, which is defensible).

The omission is not neutral. Recomputed with `exact-tables.ts` added,
M4's predicate-B intersection is **eight**, not seven, and the packet's
sentence "That is M9's entire surface bar `page-shell.ts`,
`materialize-action.ts` and `epistemic.ts`" is then exactly right about
the residue but wrong about the count. `exact-tables.ts` is the file
M9's slice 6a needs (it is where `data-entity-id` is emitted today), so
this is the collision most likely to bite. [Observed]

Everything else in the collision table re-derives exactly under both
predicates, at the HEADs the packet names: M1 1/1/0/0, M2 11/4/7/4,
M3 13/4/9/2, M4 22/8/13/7, M5 9/3/5/3, M6 13/0/9/0, lane B 1/0/—/0,
and the named per-sibling file lists are correct. [Observed]

**Repair.** Make the surface eleven files, recompute, and say M4 shares
eight.

### F6 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:339`, `380`, `423-424`,
and the record's `figures_that_differ_from_the_dossier`.

**Defect.** The packet defines the dossier once, at line 3, as
`docs/pursuits/2026-09-13-vision-pursuit.md`, then attributes four
verbatim quotations to "the dossier" that do not occur in that file:

- "25-row table" (line 380)
- "30 of them (all 9 entities, all 9 relationships and their kin) carry
  NO tier field at all" (line 339)
- "14,804" and "~12 KB recovered, 2.8% of the P-63 trim" (lines
  423-424)

Swept this session over `docs/`, `.syzygy/` and `openspec/` with
`grep -rn -F`: all four strings occur only in
`docs/pursuits/2026-09-13-vision-pursuit-data.json` and its
`-harvest.json` twin, plus the M9 packet and its own record. They are
absent from the dossier `.md`, whose M9 section (lines 337-364) says
only "1 of 8 edge kinds matches RFC1-25" and carries no band-byte
figure and no tier parenthetical at all. [Observed; denominator: all
tracked files under those three trees]

The figures themselves are real and correctly quoted from the JSON
files; the citation is to the wrong artifact, so a reader checking the
packet against the named dossier finds nothing. The dossier is not
edited, which is correct.

**Repair.** Name `docs/pursuits/2026-09-13-vision-pursuit-data.json`
(or the harvest twin) where those four quotations are cited, and define
the pursuit *record set* at line 3 rather than the single `.md`.

### F7 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:380-381`.

**Defect.** The packet's correction is itself an under-swept absence
claim. It reads: "**The dossier's '25-row table' undercounts by one and
its enumeration omits `succeeds`**". The enumeration in
`2026-09-13-vision-pursuit-data.json:4360` omits **four** RFC1-25
tokens, not one: `calls`, `exposes`, `accesses(mode)` and `succeeds`.
Recomputed this session: RFC1-25's table (header at RFC-0001 line 494,
last data row at 521) carries 26 data rows and 30 backticked first-
column tokens; the JSON enumeration lists 25 comma-separated entries
covering 26 tokens. [Observed]

This is the shape rule 9 names: a "the only omission is X" claim needs
a set difference, not a spot check. The load-bearing intersection is
unaffected and I confirm it: the POC's eight kinds against the 30
tokens intersect at exactly `{contains}`, 1 of 8, over 9 relationships
(`contains` 1, `governed-by` 1, `mapped-to` 2, `materializes-as` 1,
`changes` 1, `verified-by` 1, `satisfies-at-runtime` 1,
`coverage-unknown` 1). [Observed]

**Repair.** "omits `calls`, `exposes`, `accesses(mode)` and
`succeeds`", with the set difference as the predicate.

### F8 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:403-431` (the observed-
band decomposition and everything derived from it).

**Defect.** The table states one predicate — the `data-band="reality"`
section through its depth-matched closing tag — and that predicate
re-derives the whole-band figure exactly: **14,820** bytes, identical
on both Polaris captures, and 11 headings at **2,130** bytes.
[Observed] Two of the four part rows have no stated predicate, and the
two that exist are measured on **inconsistent conventions**:

- "9 provenance citation spans 4,309" = the nine
  `<span class="citation">…</span>` elements **including their tags**.
  Re-derived exactly. [Observed]
- "9 entity detail spans 905" = the **inner text only** of the nine
  `<span data-claim-provenance="…">` elements. With their tags they are
  **1,534** bytes. [Observed]
- "the relationship list 5,077" = the `<ul>` **inside** the
  relationships section. The whole `<section class="relationships">`,
  which is what would move, is **5,680** bytes (h3 189 + lede 243 +
  wrapper 171 + the list). [Observed]

So the packet's "Dropping the details and citations recovers **5,214**
bytes; also moving the relationship list … brings the total to
**10,291**" understates both recoveries: the actual figures under a
consistent "delete the element" predicate are **5,843** and **11,523**.
The error is in the conservative direction and does not change slice
7's conclusion (nine added tuples at the measured mean cost 5,278, so
the net moves from −64/+5,013 to +565/+6,245, still no reliable
dividend), but Gate 6 bullet 1 asserts "**Every count in this packet
carries its predicate and its denominator**" and two of these four do
not.

**Repair.** State the per-part predicate; measure all four with tags;
restate 5,843 / 11,523 and the derived net.

### F9 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:756`.

**Defect.** Slice 6a costs "Trajectory's **299** rendered cards at
roughly 40 bytes each". 299 is the `class="wi-card"` count of
`capture/trajectory.html` — the **private-daemon** Trajectory, which
the evidence record does not name among its five capture files. The
capture the record and the packet do name, `trajectory-7478.html`,
renders **310**. [Observed, both counted this session] Every other
Trajectory figure in the packet (315 hrefs, 311 ids, 311 fragment
hrefs, 254,168 bytes) is taken from the `-7478` file, so one figure in
the set silently comes from a different observation.

**Repair.** 310, from the named capture; or name the other capture and
say why it was used.

### F10 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:94-96` and `526`
(Gate 3 slice 6 row), against `1015-1018`.

**Defect.** Internal contradiction about whether slice 6 touches the
shared model. Line 94 says "Slices 2, 4, 6 and 8 all change the shared
model file `packages/three-surface-poc-core/src/model.ts`", and the
collision section repeats it ("claimed by M2, M4, M5 and M9's slices 2,
4, 6 and 8"). Gate 3's slice 6 row lists `trajectory.ts`, `orrery.ts`,
`exact-tables.ts`, `routes.ts`, `materialize-action.ts` and **not**
`model.ts`. One of the two is wrong, and the answer decides whether
slice 6 takes a WIP-one shared-model slot. (Slice 6b — making the
artifact identity the canonical join key — plausibly does touch the
model, so the Gate 3 row looks like the error.)

**Repair.** Reconcile; if slice 6b touches `model.ts`, put it in the
Gate 3 row and keep the four-slice queue.

### F11 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:589-590`.

**Defect.** A quotation inside quotation marks that is not verbatim.
The packet writes: POC-REQ-053's oracle shape is "resolution per
enumerated element over the exhausted population; zero dangling links
over the exhausted population decides" (spec lines 899-908). The clause
sits at lines 903-904 of
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
and reads: "**Oracle**: HTTP/anchor resolution per enumerated element;
zero dangling links over the exhausted population decides." Two words
are dropped and a
four-word phrase is relocated into the first clause, with no elision
mark. [Observed]

Rule 8 wants the clause quoted as it stands. The substance survives
intact.

**Repair.** Quote it as written, or paraphrase outside quotation marks.

### F12 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:929-933`.

**Defect.** An `[Observed]` label on a claim the same sentence
contradicts. Gate 5 concludes: "It establishes [Observed] that **no
slice of M9 maps to an approved requirement-and-scenario pair that
squarely names its consequence**; that slice 4a's nearest requirement
is a stretch of POC-REQ-060 on one reading and a **squarely-fitting**
PWB-REQ-007 on the other; …". On Q2's second arm, by the packet's own
account, one slice does map squarely. "Squarely" is in any case a
judgment, not an observation.

**Repair.** Qualify the blanket claim to Q2's recommended arm, or drop
"squarely" from it and let the per-row table carry the nuance.

### F13 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:38` (Q4) against `548`
(Gate 3's act row for slice 4b).

**Defect.** Q4 asks "Should the POC be able to construct `Inferred` at
all?" and is presented as one of six owner gates. On its **recommended**
answer — add the typed arm, no production constructor — the packet's own
act table says no act is reached: "A typed-but-unconstructible arm
reaches no trigger." So on the recommendation Q4 is not a human gate at
all; it is a typing decision inside the implementation plane. The
genuine gate is only the constructible limb, which the act row already
carries.

This does not make Q4 improper to ask — the owner may prefer the second
arm — but the packet should not present as a gate a question whose
recommended answer it has already shown needs no act.

**Repair.** Recast Q4 as "if and when an agent asserts, may the POC
construct Inferred?", and say that the recommended arm proceeds under
the improvement-cycles direction without a new act.

### F14 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:35` (Q1), `37` (Q3), and
the Gate 5 table at `942-952`.

**Defect.** A lawful arm is named once and then dropped. RFC2-26's own
text offers two routes for an unmapped observable consequence: an
approved requirement-and-scenario pair, **or** "a reviewed N/A judgment
proving it purely structural with no independently testable behavior",
homed in `decisions/` and honored through an effective owner act. The
packet names that route only in the slice-1 row of the Gate 5 table,
and reads it as probably unreachable there. It is not offered as an arm
of Q1 or Q3, although slices 6a and 8 (a data attribute carrying an id
the page already renders; a rename with no rendered-truth change) are
exactly the "purely structural" shape the clause contemplates, and an
N/A judgment package is a materially cheaper owner act than a CC-REV-2
spec amendment.

**Repair.** Add "a reviewed N/A judgment package under `decisions/`,
for the structural slices only" as a third lawful arm of Q1, and say
for each slice whether the packet thinks it reachable.

### F15 — non-blocking

Five citation slips, all checked at source this session. None changes a
conclusion; together they matter because the packet opens by declaring a
strict line-number convention ("the line on which the cited text
*begins*", lines 20-24).

1. Line 38 (Q4): "`.syzygy/governance/doctrine/trust-and-evidence.md`
   states that an LLM assertion is Inferred" — no line, no quotation,
   and no clause identifier, for the doctrine sentence Q4 rests on. It
   is at that file's line 16: "An LLM assertion is **Inferred, never
   Observed**". [Observed]
2. Line 40 (Q6): two quotations share one cite, "(line 41)". "the agent
   reports each completed cycle to the owner before starting the next"
   is at line 41; "derived only from recorded findings" is at line 36.
   [Observed]
3. Line 546: "the PWB implementation act's line 78 adds 'and a new
   owner act'". The cited words begin at line 79; the sentence
   containing them begins at 78. [Observed]
4. Line 937: RFC2-26's scope sentence "This clause binds the whole RFC
   0002 package, not this module alone" is cited "(line 220)"; it
   begins at line 219 of
   `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`.
   [Observed]
5. Line 667: "CC-SPEC-8's matrix banner says 'the clause text is the
   authority, and nothing here restates a clause normatively' (lines
   7-8)". Those bytes are
   `openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md`
   lines 7-8 — the artifact's own head banner, not CC-SPEC-8's text.
   The constraint is real; the attribution is to the wrong artifact,
   which is the distinction rule 8 draws. [Observed]

**Repair.** Fix each cite; quote CC-SPEC-8 at its own clause or cite
the banner as the matrix's own.

### F16 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1058` and `1169`.

**Defect.** The two P-number sentences agree with each other and with
the register — and both overlook two peers. Recounted this session with
the predicate `^| P-`: the register at `a9f671e` carries 26 rows (the
brief's 21 open + 5 acted), ending at P-53; `m9wt`'s register is
unchanged at 26 rows ending P-53; each of `laneb`, `m2wt`, `m3wt`,
`m4wt`, `m5wt`, `m6wt` carries exactly one added row, P-68…P-73 in
order; `m7wt` and `m8wt` carry **none**. [Observed] So P-74 is the next
free number *today*, but M7 and M8 are first drafts in the same batch
with no row yet, and either landing first makes M9 P-75 or P-76.

**Repair.** Say "the next free row after the six siblings' P-68…P-73,
subject to M7's and M8's rows landing first" rather than forecasting a
literal number.

### F17 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:200-203`.

**Defect.** The home-page caveat is quoted as "POC, not product status.
Desired, execution, and observed state remain distinct." and closed
with a period. `apps/three-surface-poc/src/routes.ts:80` continues:
"Merge is not verification. Missing evidence is rendered Unknown." The
elision is unmarked. [Observed] The two dropped sentences are on the
packet's side of the argument, which makes the omission harmless and
the unmarked elision unnecessary.

**Repair.** Add the ellipsis or quote the line whole.

### F18 — non-blocking

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:1005-1043` (the
collision section).

**Defect.** The collision section intersects *files* and never
*questions*, so two live overlaps with sibling owner questions go
undisclosed:

- M3's Q1 (`m3wt` at `6574600`) asks whether POC-REQ-060's "epistemic
  encoding" reaches only the two declared badge spans. M9's slice 3
  proposes an amendment to POC-REQ-060 extending it "to the *record
  shape*, not the encoding alone". The amendment presupposes an answer
  to M3's open question, on the same clause. [Observed]
- M2's Q1 and Q6 (`m2wt` at `f2f37dd`) are over PWB-REQ-007's currency
  limb and its sequencing against lane B's package, which "rewrites the
  same clause region of PWB-REQ-007". M9's Q2 asks about PWB-REQ-007's
  *scope*. Three open questions now sit over one requirement.
  [Observed]

**Repair.** Add a question-level row to the collision section naming
M3 Q1 (POC-REQ-060), M2 Q1/Q6 (PWB-REQ-007), M8 Q7 (shared-model
ceremony, per F2), and say which of M9's questions presuppose them.

### F19 — editorial

Clause extents overrun by one line into the following blank line:
`.syzygy/governance/doctrine/vision.md` VIS-3 cited "lines 108-121"
(clause ends 120) and VIS-4 "lines 122-140" (ends 139). VIS-1 (82-94),
VIS-2 (96-106) and VIS-7 (183-193) are exact. [Observed]

Also: Gate 6 bullet 11's "**0 of 1,206** non-fence lines". Under a
strict non-fence count with the file's trailing newline not counted as
a line I get **1,205**; with it, 1,206. Everything else in that bullet
re-derives exactly: 0 odd-backtick non-fence lines, 2 lines over 78
columns outside tables/quotes/headings/fences (both single code-span
paths, at 365 and 833), **233** distinct code spans, **58**
slash-bearing, **19** non-resolving, and the enumerated nineteen are
exactly the nineteen the packet lists. [Observed]

### F20 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:336` (and 225).

"the five edges of intent → work → code → evidence → runtime are among
them". That chain holds **four** edges (`materializes-as`, `changes`,
`verified-by`, `satisfies-at-runtime`); the fifth Unknown relationship
is `coverage-unknown`, capability → `region:unmapped-code`, which is
not on the chain. [Observed, all nine relationships read from the
machine capture] The load-bearing part — all eighteen entity and
relationship claims carry the two-member union — is confirmed exactly:
`{basis,label}` ×9 is 5 entities + 4 relationships and `{label,reason}`
×9 is 4 entities + 5 relationships, as the packet's table states.

### F21 — editorial

`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md:837-838`.

"[Observed: `openspec/changes/` holds five directories, and none is a
three-surface amendment]". `ls -d openspec/changes/*/` returns **six**:
`archive/`, `polaris-manifesto-generation/`,
`polaris-manifesto-understanding-amendment/`,
`polaris-project-wide-butlers-model/`,
`project-registration-and-honest-shape-visibility/`,
`three-surface-poc-experience/`. `archive/` holds only `README.md`, so
the exclusion is harmless and the conclusion holds — but an `[Observed]`
absence claim should state its exclusion. [Observed]

The composition rule the packet invokes is honoured: `AGENTS.md`'s
overlay rule binds the Polaris *generation* requirement lookup
(`polaris-manifesto-generation/` composed with
`polaris-manifesto-understanding-amendment/`), and M9 composes no
requirement from a base plus an overlay. [Observed]

## What I checked and found sound

Recorded so the owner can see the size of the verified core, not only
the defects.

- **No digest-bound byte is proposed for edit.** The six signed
  three-surface artifacts (sign-off act table, lines 42-49; `tasks.md`
  excluded at 51-53) and the eleven signed PWB artifacts (project-wide
  act table, 34-46) were read at source; neither set intersects any
  slice-touched path in Gate 3, and slice 3 is a candidate amendment
  package by construction. Lane B's
  `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (read read-only in `laneb` at
  `4090f98`) carries exactly those eleven PWB paths, zero three-surface
  paths, and the line "All rows take effect together or none do"
  verbatim — so the packet's Q1 collision analysis is exactly right.
  [Observed] No manifest row and no truncated signed digest is
  reproduced in the packet, in its record, or in this review.
- **The three mutation-record claims re-derive.** Both `subjects`
  digests of
  `docs/evidence/pwb-p3-8-reachability-mutation-run-2026-09-04.json`
  differ from their files' current bytes (computed, not transcribed;
  neither value reproduced here), and the two 2026-09-05 records name
  `model.ts` as a mutation target with no `subjects` block. [Observed]
- **Every served figure in the census tables re-derives exactly** under
  the packet's stated predicates, subject to F1's provenance caveat:
  hrefs 40 / 1,061 / 315 / 23 = 1,439 with 1,051 fragments, 372 source
  routes, 16 surface roots and **0** claim-level cross-surface links;
  one `<nav class="site-nav">` block per page with 4 hrefs in each;
  post-lane-A Polaris 1,089 hrefs, still 0; `data-claim-id` 699/689 and
  713/703 on the two Polaris captures and 0 on the other three pages;
  the three-state word sweep (desired 1, observed state 1, execution
  state 0, three-state 0); the corrected `\sid="` uniqueness figures
  (350/350, 344/344, 311/311, 24/24, 23/23, zero non-unique fragment
  targets on every page) and the `\bid="` artefact that produced the
  discarded finding. [Observed]
- **Every ceiling arithmetic step re-derives**: 618,515 and 612,665 of
  headroom against 2,097,152 (`…OBSERVER-CANDIDATE.json` line 270,
  read); 713 claim-tuple spans at 418,122 bytes, mean 586.4, min 559,
  max 661, 28.28% of the page — exact to the byte once measured in
  UTF-8 rather than characters; break-even 618,515/415 = 1,490;
  3 × 586 = 1,758 per item × 415 = 729,570 > 618,515, so the
  tuple-reusing ribbon does not fit; 300 × 415 = 124,500, which does.
  [Observed]
- **Every clause the packet quotes is exact at its cited line**, bar
  F11 and F15: RFC1-25 (RFC-0001:463), RFC1-26 (636-642, whole),
  RFC2-26 (196-221 under the heading at 194, both paragraphs, verbatim
  and correctly rewrapped), VIS-1/2/3/4/7, POC-REQ-052 (851, text 855),
  its scenario (872-877), POC-REQ-053 (890, text 894, scenario
  910-914), POC-REQ-060 (927, text 931-934, scenario 948-953),
  POC-REQ-061 (972-973), POC-REQ-031 (537), PWB-REQ-007 (439, text 443,
  scenario 470-474), the PWB Purpose (5) and its nine declared-item
  classes (15-26), CONTRACT-COVERAGE.md line 89 and line 3, Part B2's
  heading (232) and preamble (238-241), the sign-off act's "mints no
  per-clause N/A judgment" (32-34) and line 39, the project-wide act's
  line 31, the PWB implementation act's line 76 and triggers (88-94),
  the continuation act's line 110 and 112-113, and the
  improvement-cycles direction's 34, 41, 46-54, 50 and 55-56. RFC6-12
  is at CONTRACT-COVERAGE.md 369 and RFC6-24 at 371, exactly as the
  packet's correction says. [Observed]
- **Gate 5's population and absences hold**: 24 requirements
  (`^### Requirement:`) and 24 scenarios (`^#### Scenario:`), one each,
  ids POC-REQ-001…061 as enumerated; `Inferred` occurs **0** times in
  the whole specification. [Observed]
- **The source-line re-verification table is correct in every row**:
  `PocEpistemic` at model.ts 44-46 (dossier's 43-45 off by one),
  `EPISTEMIC_LABELS` at vocabulary.ts 65 (dossier's 64-65 off by one),
  `realityBand` at polaris.ts 1173 (dossier's 1156-1171 stale),
  `codeStructureSection` 255-274 and `workItemsSection` 276-295,
  `renderTrajectoryPage` 136 with its eyebrow at 192, orrery eyebrow
  157, `polaris-copy.ts` 35 and 41, RFC-0001 463. Also confirmed:
  `PocRelationship.kind` is `string` at model.ts 82, `PocSurface` at
  90-96 with no state field, `PocEntity`'s nine kinds at 64-73,
  `EpistemicState`'s three arms at cap1-core/epistemic.ts 50-67 with
  the Inferred arm at 52, `ProjectShapeClaim` at
  project-shape-model.ts 120-131, `closedReason`'s thrown invariant at
  142-148, `observedClaim` 184 and `unknownClaim` 188 with its optional
  `tier`, `internalHrefs`'s fragment-only predicate at
  polaris-reachability.test.ts 101 used by the case at 189,
  `withMountPrefix` at page-shell.ts 20 and the nav at 23,
  `boundedResponse` at routes.ts 137-141, the caveat at routes.ts 80,
  `surface-routes.test.ts` cases at 38 and 123, `cross-cutting.test.ts`
  imports at 4-9, `exact-tables.ts` 28 and 41. [Observed]
- **The `Inferred` sweep re-derives exactly**: 27 / 45 / 21 non-test
  modules, 0 / 2 / 2 non-test hits, at `polaris-copy.ts:35,41`,
  `vocabulary.ts:65`, `epistemic.ts:36`. [Observed]
- **The prerequisite line is fairly tested.** The dossier's
  prerequisite sentence (dossier lines 357-358) is quoted verbatim, and
  the three-way verdict is sound: the third clause genuinely does not
  survive, because the three RFC6 clauses sit in a Part B2 whose own
  preamble and whose signing act both say they render Unknown pending
  owner-reviewed N/A. There is no owner deferral to reopen. [Observed]
- **The discarded duplicate-id finding is recorded rather than
  deleted**, with the `\b`-versus-`\s` cause named — verification
  rule 1 working, and the right way to handle a false first pass.
- **Conventions.** No backticked observed-repository path; no act
  argument, manifest row or truncated signed digest reproduced;
  `check_governance.py` ends `0 FAIL`.

## The six questions

| # | Scope truthful? | Genuine human gate? | Recommendation follows? | All lawful arms named? |
|---|---|---|---|---|
| Q1 | Yes. The two specifications are separately signed and separately digest-bound, and lane B's manifest does occupy the PWB side — all three verified at source | **Yes.** Only the owner may sign a CC-REV-2 delta (VIS-4); which specification it binds is not an engineering choice | Yes. Every consequence M9 renders is a three-surface consequence, and the counter-argument (Q2's second reading) is stated as real rather than dismissed | **No** — the RFC2-26 reviewed-N/A package is a third lawful arm for the structural slices and is named only in a Gate 5 row (F14) |
| Q2 | Yes, and unusually well: both readings are stated fairly, and the second is followed to its uncomfortable end — "the served payload is in breach today, on 18 of 1,167 … a disclosure owed" | **Yes.** A requirement's scope is the owner's to read; the answer moves slice 4 between "enhancement" and "repair owed" | Yes. The nine declared-item classes really do exclude every kind the POC's nine entities carry | Yes. Two arms plus a stated default |
| Q3 | Yes. Line 89's mapping to POC-REQ-052 is verbatim as quoted, and POC-REQ-052's text really is anti-fabrication, not vocabulary closure | **Yes.** Whether RFC1-26 reaches a bounded POC's local rendering vocabulary is a contract reading | Yes, including the part that cannot be repaired: the signed row stands | **No** — same gap as Q1; slice 8 is the clearest "purely structural" candidate for the N/A route (F14) |
| Q4 | Partly. The measurement is exact; the framing overstates the gate | **Only on one limb.** On the recommended arm the packet's own act table says no trigger is reached, so the recommended answer needs no act (F13) | Yes, and the counter-argument ("dead code with a test suite") is given full weight | Yes. Two arms plus a default |
| Q5 | Yes, subject to F3: the headroom figure is sound and correctly sourced, but two ceiling rows and the omitted 2,090,025-byte and breach observations are not disclosed | **Borderline.** Allocation order is engineering; the trade-off against a margin the P-60/P-61 repairs are counting on is genuinely the owner's | Yes. VIS-1's rank ordering is applied correctly and the "does not fit" arithmetic re-derives | Yes. Two arms plus a default |
| Q6 | Yes. The 24/24 sweep is exact and the direction's second limb is quoted verbatim | **Yes.** Whether the pursuit is a continuation or a new cycle owing a report is the owner's reading of their own direction | Yes | Yes. Two arms plus a default |

**Defaults.** All six state a default-if-unanswered; every one is
conservative (hold the slice, draft no delta, land nothing
byte-adding), and none of them authorizes anything. No lawful arm is
called unlawful anywhere in the packet. No owner trade-off is smoothed
into consensus language — the counter-arguments are the strongest part
of this packet, and two of them (Q2's breach disclosure, Q5's earmarked
margin) argue against the packet's own recommendation.

## Measurement table

"Re-derived" means recomputed this session from source or from the
retained capture under the packet's stated predicate.

| Claim | Re-derived? | My figure |
|---|---|---|
| RFC1-25 table: 26 data rows, 30 tokens, `succeeds` at line 521 | yes | 26 rows (496-521), 30 tokens, `succeeds` at 521 |
| Intersection with the POC's 8 kinds = 1 | yes | `{contains}`, 1 of 8, over 9 relationships |
| Dossier enumeration omits `succeeds` | **no** | omits `calls`, `exposes`, `accesses(mode)`, `succeeds` — four (F7) |
| 1,167 epistemic-labelled served objects | yes | 1,167, identical on both retained `api-poc.json` files |
| 1,137 with tier / 30 without | yes | 1,137 / 30 |
| The 30 = 18 entities+relationships + 12 Unknown shape claims | yes | 9 `{basis,label}` + 9 `{label,reason}` + 12 `{freshness,label,reasons}` |
| Labels 1,146 / 0 / 21; tier `report-fact` 1,137, 0 of 6 others | yes | exact |
| `excluded-content` 12, 0 of the other 11; fresh 1,149; unchallenged 1,149 | yes | exact |
| Served payload obtained without a 7478 daemon | **no** | Polaris/api figures from a private daemon; `-7478` pages from the loopback daemon; record's provenance wrong for 2 of 5 files (F1) |
| "Three epistemic record shapes" not reproducible; 2 types / 5 arms / 4 signatures | yes | 2 declared types, 5 arms, 4 emitted key signatures |
| 618,515 / 612,665 bytes of headroom | yes | exact against 2,097,152 (registry line 270) |
| 713 tuple spans, 418,122 bytes, mean 586.4, min 559, max 661, 28.3% | yes | exact (UTF-8 bytes) |
| Ribbon break-even 1,490/item; 1,758 does not fit; ~300 does | yes | 729,570 > 618,515 > 124,500 |
| P-63 trim 434,960 bytes | yes | as `AGENTS.md` records |
| Reality band 14,820 bytes; identical on both captures; 11 headings 2,130 | yes | exact |
| 9 citation spans 4,309 | yes | exact (with tags) |
| 9 entity detail spans 905 | predicate unstated | 905 as inner text; 1,534 with tags (F8) |
| Relationship list 5,077 | predicate unstated | 5,077 as the `<ul>`; 5,680 as the section (F8) |
| Recoverable 5,214 / 10,291 | **no** | 5,843 / 11,523 under a consistent predicate (F8) |
| `CONTRACT-COVERAGE.md` line 89 verbatim | yes | exact |
| Part B2 heading 232, preamble 238-241 verbatim | yes | exact |
| Sign-off act "mints no per-clause N/A judgment" 32-34 | yes | exact |
| RFC6-12 at 369, not 371; 371 is RFC6-24 | yes | exact |
| PWB-REQ-007 line 443 verbatim; nine declared-item classes | yes | exact; 9 classes, none a POC entity kind |
| 24 requirements / 24 scenarios; `Inferred` 0 in the spec | yes | exact |
| 1,439 hrefs, 0 claim-level cross-surface; 16 roots in 4 nav blocks | yes | exact |
| `data-claim-id` 699/689, 713/703, 0 elsewhere, 0 naming an entity id | yes | exact |
| desired 1, observed state 1, execution state 0, three-state 0 | yes | exact |
| Ten attribute names carry an entity identity | **no** | eleven (per-page 3/8/2/0 exact) (F4) |
| `Inferred` 0/27, 2-in-1-of-45, 2-of-21 | yes | exact, same four sites |
| Corrected `\sid=` id uniqueness, 0 non-unique targets on 4 pages | yes | exact |
| Trajectory 299 rendered cards | **no** | 310 on the named capture (F9) |
| Collision table (A/A∩/B/B∩) for M1-M6 and lane B | yes | every cell exact at the named HEADs |
| M4 shares seven of M9's files | **no** | eight, once `exact-tables.ts` is in the surface (F5) |
| M2 names `polaris.ts` 0 times | yes | 0 |
| Lane B manifest: 11 PWB artifacts, "all rows together", 0 three-surface | yes | exact |
| M7/M8 disjoint from M9 | **no** | M8 shares 6 under predicate B, incl. `model.ts` (F2) |
| Register rows P-68…P-73, one per sibling worktree; m9wt ends P-53 | yes | exact; m7wt and m8wt carry none (F16) |
| Mutation-record digests differ from current bytes | yes | both differ |
| 233 code spans, 58 with `/`, 19 non-resolving, 2 over 78 columns, 0 odd backticks | yes | exact; non-fence line count 1,205 vs 1,206 (F19) |
| `check_governance.py` ends `0 FAIL` | yes | `32 OK, 20 WARN, 0 FAIL (52 checks)` |

## Closing note

This is an unusually careful first draft. Twenty-eight of the thirty-
three measurement rows above re-derive to the byte, the clause
quotations are near-uniformly exact, the counter-arguments are honest
enough to argue against the packet's own recommendations, and the
discarded duplicate-id finding is recorded rather than buried. The two
blocking findings are both about provenance rather than arithmetic:
what the served captures actually are (F1), and a disjointness claim
about two sibling packets that the sibling worktrees falsify (F2).
Neither requires re-doing the analysis; both require saying accurately
where the evidence came from and what the neighbours are doing.

Verification rule 10 applies: this review is bound to the two files at
the digests above. Any edit retires it, and the repairs are uncovered
until a second fresh-context review confirms them.

Verdict: REVISE
