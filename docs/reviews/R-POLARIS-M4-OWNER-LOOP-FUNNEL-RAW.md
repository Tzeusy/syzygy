# R-POLARIS-M4-OWNER-LOOP-FUNNEL-1-RAW

Independent fresh-context review, round 1, of an unreviewed draft.
Read-only session. No repository file was edited; no git state changed.

## Header — what was reviewed, at which bytes

Worktree: `scratchpad/m4wt`, branch `agent/syzygy-dov.4`.
Commit under review: `61bd43b0498393495b71c4e8f43bf9fb51d89596`
(base `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d`, clean tree,
`git status --porcelain` empty).

Reviewed artifacts (`wc -c` and `sha256sum`, computed this session, never
transcribed):

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 83557 | `8a28fadc7765f4715360bae36c8d0fbe312308a4657c42c3db086fe29862d7e4` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 25070 | `ae753f560bfe04a65f49418fcd59d1d390cf36c75a12e902ccdb65764843d11d` |

Captures re-digested this session; every one matched the packet's table:

| Capture | Bytes | sha256 |
|---|---|---|
| `m1/measure/after/polaris-tailnet.html` | 1484487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` |
| `m1/measure/after/polaris-direct.html` | 1478637 | `2fecdd01e1a2ff577567495796ea7e59ab89f1420be6033e23314d26442ea094` |
| `m1/measure/after/api-poc.json` | 5520314 | `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e` |
| `m1/measure/after/api-polaris.json` | 640592 | `ab3b517be1e62a0a7f4cabe73d870f9aa6bea7d2bbbadf0d27a2f00c34eca22e` |
| `capture/home.html` | 38706 | `c2fd6d1af7103e871c26dc65b76cc391fe2765a1c7391ac19ddf1656e57b5fca` |
| `capture/trajectory.html` | 244524 | `fd802531b199084e7145932715150f4977335e49ca6aa168d68d5227c9d6ddde` |
| `capture/orrery.html` | 37048 | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` |
| `capture/api-poc.json` | 5508208 | `8b8d8a3078f085d4d53aa3bcad9d5a06b5b0c064bb8cdc7b3832913a81bc44d0` |

Mechanical gates run this session, from the worktree root:

- `python3 scripts/check_governance.py` → **32 OK, 20 WARN, 0 FAIL (52
  checks)**. Invariant met [Observed].
- Hard wrap: 5 lines exceed 78 columns outside tables, block quotes and
  fences (denominator 1125 lines). Four are single unbreakable path code
  spans; one is the H1. See E1 [Observed].
- Code-span paths: 54 path-shaped spans; 47 resolve on disk; the 7 that do
  not are `openspec/**`, `.syzygy/**`, `/api/poc`, `/polaris/source` and
  three `agent/syzygy-dov.*` branch names — none is a file reference
  [Observed].
- No manifest argument and no truncated signed digest is quoted; no Butlers
  path appears inside a code span (CG-1b clean, and `check_governance.py`
  agrees) [Observed].

---

## Findings

### F1 — blocking — the RFC2-24 route table and the implementation's route table are NOT word for word equal; 7 of 12 differ, and slice 1 as specified would re-open the POC-REQ-060 falsifier it exists to close

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:450` (Gate 2, RFC2-24 bullet)
and `:535–545` (slice 1's mapping table).

**Defect.** The packet states: "The clause's own table carries a
**Resolution route** column whose twelve cells are, word for word, the
twelve values of `UNKNOWN_REASON_ROUTES`." I extracted both tables by
script this session — the RFC table from
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 117–130, the constant from
`packages/three-surface-poc-core/src/project-shape-model.ts` lines 89–102 at
`a9f671e` — and compared them key by key. Denominator 12. **5 identical, 7
different.** The seven:

| Reason | RFC2-24 cell | `UNKNOWN_REASON_ROUTES` |
|---|---|---|
| `missing-declaration` | First-pass drafting for owner sign-off (v1.md) | First-pass drafting for owner sign-off |
| `missing-evidence` | Produce/capture evidence | Produce or capture evidence |
| `no-currency-bound-declared` | Declare the bound in quality policy [Observed — trust-and-evidence.md] | Declare the bound in quality policy |
| `mapping-coverage-absent` | Run/declare the mapping | Run or declare the mapping |
| `challenge-suspended` | Challenge resolution (RFC2-13) | Challenge resolution |
| `source-uncaptured-or-unreachable` | Repair the observer/source; new snapshot | Repair the observer or source; new snapshot |
| `execution-blocked` | **Unblock or authorize the run** (execution profile, consent, environment), then capture in a new snapshot | Unblock or authorize the run, then capture in a new snapshot |

The module's own comment at
`packages/three-surface-poc-core/src/project-shape-model.ts:86–88` says only
that `project-shape-model.test.ts` proves the **key set** equals cap1-core's
`UNKNOWN_REASONS` — it makes no claim about the values, and no test does.

This is not cosmetic. Slice 1's mapping table (`:535–545`) heads its third
column **"Route (RFC2-24's own words)"** and fills it with *Produce/capture
evidence* and *Run/declare the mapping* — the RFC's strings, not the
implementation's. If slice 1 renders those nine disclosures from the RFC's
wording while the existing thirteen render from `UNKNOWN_REASON_ROUTES`, one
surface renders two different route sentences for the same reason. That is
POC-REQ-060's falsifier — "one surface encoding Unknown ... differently from
the declared table" — the exact defect Q1 asks the owner to rule a
non-conformance.

This is also an "all" claim under verification rule 2 with no sweep and no
denominator, and a contract claim under rule 8 whose equality assertion is
not what the clause says.

**Repair.** Delete the word-for-word claim or replace it with the measured
5/12 ÷ 7/12 split and its method. State explicitly that slice 1 draws its
route strings from `UNKNOWN_REASON_ROUTES` (the declared table the page
already renders), and rewrite the mapping table's column heading and its
nine cells to the implementation's strings. If the owner instead wants the
page to render the RFC's wording, that is a separate change to all twelve
values and must be named as one.

---

### F2 — blocking — Q2's load-bearing code claim is false: `routesFor` returns `[]` for an Unknown too, and the type-level prohibition slice 2 proposes would make an existing cap1-core arm unrepresentable

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:72` (Q2, limbs (a) and (b))
and `:587–594` (slice 2, "What the slice does not do, per Q2").

**Defect.** Q2 says: "`routesFor` at `packages/three-surface-poc-core/src/
project-shape-model.ts` lines 150–154 returns `[]` **exactly when** the
label is not Unknown, so the empty array is the correct encoding of 'not
Unknown', not a missing route," and limb (b) concludes "an Unknown
project-shape claim with no modelled route is **unreachable by
construction**."

The code at `a9f671e`, line 151, is:

```
if (state.label !== 'Unknown' || !('reasons' in state)) return [];
```

There are **two** return-`[]` branches, not one. The second fires on an
Unknown that carries no `reasons` field — and cap1-core's `EpistemicState`
(`packages/cap1-core/src/epistemic.ts:50–67`) has exactly such an arm as its
third member:

```
  | {
      readonly label: typeof UNKNOWN;
      readonly basis: 'deferred';
      ...
    };
```

So a routeless Unknown is *modelled today*, in the shared engine, and
`routesFor` gives it an empty array. "Unreachable by construction" is false;
what is true is the narrower, data-only fact that no claim in either
retained evaluation uses that arm (which is what limb (a) actually measured,
and which I confirmed: 0 of 1,137 empty arrays are Unknown, on both
captures).

Three consequences the packet does not carry:

1. Slice 2's "makes the empty array unrepresentable on an Unknown at the
   type level" would make `{label: 'Unknown', basis: 'deferred'}`
   unrepresentable in the POC's claim type — a collision with an accepted
   cap1-core type the slice never names. The deferred arm carries no reason,
   so it cannot borrow a route from RFC2-24's twelve either.
2. The declared copy row that corresponds to this arm is
   `label.deferred` (`apps/three-surface-poc/src/polaris-copy.ts:192`,
   also in `UNREACHED_IN_FIXTURES` at `polaris-copy.test.ts:297`) — the
   packet names `label.no-route` (line 193 / set entry line 299) and not
   this one.
3. L5-M4's premise is therefore stronger than Q2 allows. Q2 tells the owner
   "on this packet's measurement the premise does not hold"; the premise
   holds at the type level and fails only on today's data.

Q2 is also the question the packet frames as "contract-determined ... one
lawful arm and one that mints a vocabulary value a contract closes" and puts
to the owner "for confirmation and disclosure rather than as a free choice"
(`:59–67`). A question whose single lawful arm rests on a false statement of
what the code does may not be put that way.

A fourth, smaller inconsistency rides on the same claim: if a routeless
Unknown were unreachable by construction, the packet's own acceptance
scenario **S5** (`:909–913`) — "WHEN a fixture carries an Unknown whose
reason has no route in the closed table, THEN the page renders the declared
'No route declared' copy ... AND the copy oracle's unreachable-row set no
longer lists that row" — could not be written.

**Repair.** Quote `routesFor`'s actual predicate, both branches. Re-state
limb (b) as a data claim with its denominator, not a construction claim.
Name the `basis: 'deferred'` arm and say what slice 2 does with it — either
the prohibition is narrowed to "Unknown-with-reasons", or the arm gets its
own disclosure, and either way say so before the owner rules. Re-open Q2 as
a genuine choice or re-argue its single-arm framing on corrected facts.

---

### F3 — blocking — the sequencing answer's collision analysis is wrong in both directions, contradicts the packet's own body, and misses a head-on duplicate: M3 slice 3 and M4 slice 3 are the same opening band in the same file

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:77` (Q7) against `:959–1005`
(Collision and sequencing) and the sibling packets read this session.

**Defect, three limbs.**

(a) *Self-contradiction.* Q7 states "The one shared file with M3 is
`apps/three-surface-poc/src/polaris-copy.ts`; the one shared file with M2 is
**none**." The Collision section, three paragraphs later, states "**The one
shared file is** `packages/three-surface-poc-core/src/project-shape-model.ts`"
— about M2. The packet asserts both.

(b) *Under-count, measured.* M2's Gate 3 slice table (`m2wt`, head
`f2f37dd`, `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md:361–366`)
names `packages/three-surface-poc-core/src/model.ts` (slices 2 and 3),
`apps/three-surface-poc/src/routes.ts` (slice 3) and
`apps/three-surface-poc/src/polaris.ts` (slices 1 and 2). M4's own Gate 3
table (`:481–488`) names `model.ts` (slices 1, 2, 4), `routes.ts` (slice 5)
and `polaris.ts` (slices 1, 3). **M2 and M4 share at least four files**, not
none: `model.ts`, `routes.ts`, `polaris.ts`, `project-shape-model.ts`. With
M3 (`m3wt`, head `573abb0`) the shared set is `polaris-copy.ts` **and**
`polaris.ts` (M3 slices 3 and 5 both edit it), not one file.

(c) *The missed collision.* M3's slice 3 is titled "One real Unknown in the
first reading" and its Gate 3 row reads: "`apps/three-surface-poc/src/
polaris.ts` (**the opening band**), `apps/three-surface-poc/src/
polaris-copy.ts` (one new sentence)". Its design paragraph: "**The opening
band** renders, in place and before the first catalog group, the two Unknown
claims the page already carries..." M4's slice 3 is titled "The opening
band" and places "a band ... after the project account and before the first
catalog section". These are two designs for one band, in one function, in
one file, each with its own oracle ("the first occurrence of a rendered
Unknown state precedes the first `data-polaris-group="catalog"`" versus "the
band's total equals the gaps section's total on every fixture"). M4's
collision section discusses only M3's slices 5 and 6 and never mentions M3
slice 3.

Q7's recommendation — "Slices 1–6 may start now" — is derived from this
analysis, so the defect reaches the answer the owner is asked to give.

**Repair.** Re-derive the shared-file set from both sibling packets' Gate 3
tables and publish it with its denominator. Reconcile M3 slice 3 and M4
slice 3 explicitly: one band, one owner, one oracle — or state why two bands
are intended. Remove the "shared file with M2 is none" sentence. Re-issue
the sequencing recommendation on the corrected set.

---

### F4 — blocking — slice 6 writes into the observed repository; the packet says twice that M4 writes nothing there, and reads the same registry fact two opposite ways in Q3 and Q5

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:75` (Q5), `:167–169` ("What M4
is not"), `:411–418` (VIS-5), `:511` (Gate 3, slice 6 act row), `:753–754`.

**Defect.** The materialize action's target is the *observed* repository and
its effect is a write there. At `a9f671e`:

- `apps/three-surface-poc/src/materialize-action.ts:33` —
  `targetRepoRoot: model.project.root` (the observed Butlers root).
- `packages/three-surface-poc-core/src/materialization.ts:12` —
  `MATERIALIZATION_TARGET_BEAD_PREFIX = 'bu'` (not Syzygy's prefix).
- `packages/three-surface-poc-core/src/materialization.ts:186–208` —
  `defaultRunCreate` runs `execFileSync('bd', ['-C', repoRoot, 'create',
  ...])`: a mutation of the observed repository's work-item database.

Against that, the packet says:

- `:167–169` — "Every slice keeps dispatch human-triggered ... and **writes
  nothing to the observed repository**."
- `:753–754` — "**Neither arm writes toward the observed repository.** The
  registry entry's write surface is empty and stays empty." (about slice 7,
  but stated as a property of the packet's posture)
- `:511` — the run "writes only to the work scheduler through the adapter
  the 2026-09-02 act's own prohibition list **already contemplates**."

I read the act. `.syzygy/governance/decisions/
PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 70–72, quoted verbatim:

> - No write, egress, execution, deployment, release, recovery, or mission
>   effect on Butlers or on any other repository. The observer registry entry
>   the owner adopted declares an empty write surface; that remains the bound.

That is a flat prohibition, not a contemplation. And the packet applies the
identical registry fact in opposite directions within four pages: Q3
(`:73`) argues slice 7 needs an act because "`typedAuthority.writeSurface`
is `[]` ... so **nothing may be written toward the observed project**";
Gate 2's VIS-5 paragraph (`:411–418`) argues "This is why the materialize
action **is lawful** — a work-scheduler effect through a typed adapter, with
the observer registry entry declaring `writeSurface: []`".

The registry entry the packet cites is the *project-shape observer*
(`authorityType: "version-control"`, `readAuthority` describing phase A/B
reads only). It declares nothing about a work-scheduler adapter; it is the
wrong instrument for the question, in both directions.

There may well be a good answer — the materialize action was built under the
2026-08-29 POC mode direction, a separate authorization lane from the
2026-09-02 PWB act — but the packet never states the collision, never says
the created Bead lands in the observed repository's tracker, and asks the
owner to "rule the run authorized" on an argument that inverts its own Q3.

**Repair.** State plainly in Q5 that the run creates a work item **in the
observed repository's Beads database** (`bd -C <observed root> create`,
prefix `bu`). Quote the 2026-09-02 act's lines 70–72. Put the reconciliation
— the 2026-08-29 direction as a separate lane, or a continuation naming the
effect — to the owner as the question, rather than asserting it. Correct the
two "writes nothing to the observed repository" sentences, or scope them
to slices 1–5 and 7. Cite the correct adapter for the work-scheduler effect
or say that none is registered.

---

### F5 — blocking — slice 1's acceptance sweep is keyed on a marker that does not exist on two of the three surfaces POC-REQ-060 quantifies over; no population is stated for them

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:567–574` (slice 1, Tests),
`:138–141` (Success 1), `:885–889` (S1), `:1026` (Gate 6 number list).

**Defect.** POC-REQ-060's scope of quantification, quoted correctly by the
packet, is "every epistemic encoding **across the three surfaces**". The
packet's sweep is: "every element carrying `data-unknown-disclosure` must
carry a `data-unknown-reason` ... the sweep reports its denominator (22 on
the retained capture's population)."

Measured this session over the retained captures (predicate:
`data-unknown-disclosure="` attribute occurrences; denominator: the whole
served page):

| Page | `data-unknown-disclosure` | `data-unknown-reason` | `epistemic-unknown` |
|---|---|---|---|
| Polaris (lane A tailnet) | 22 | 16 | — |
| Trajectory (pre-lane-A) | **0** | 0 | 301 |
| Orrery (pre-lane-A) | **0** | 0 | 11 |
| Home (pre-lane-A) | **0** | 0 | 18 |

Trajectory and Orrery render Unknown through the `epistemic-unknown` token
class alone; neither carries a disclosure element at all. So the specified
sweep has denominator 0 on two of the three surfaces and passes vacuously
there, and Gate 6's "22 today, 13 routed" is a one-surface figure offered
for a three-surface invariant (rule 4: check the denominator against the
whole population).

The same gap weakens Q1's problem statement. The packet says "Polaris today
encodes Unknown two ways on one page". Across the three surfaces there are
at least **three** encodings: Polaris's reason-span-plus-`Route:`, Polaris's
bare prose, and Trajectory/Orrery's bare `epistemic-unknown` span with no
disclosure wrapper, reason or route. The third is the largest population by
count (301 + 11) and is never measured. Q1's scope is truthful about what it
measured and silent about two thirds of the requirement's domain.

**Repair.** Measure the Unknown-encoding population on Trajectory and Orrery
and publish both denominators. Re-state Q1's scope over the three surfaces.
Re-specify slice 1's sweep over a marker the three renderers actually share
(or require the three to emit the same marker as part of the slice, which is
what POC-REQ-060 arguably demands) — a sweep that cannot see two surfaces
cannot discharge a three-surface invariant.

---

### F6 — blocking — three slices rest on the 2026-08-30 direction's recorded-finding arm, and the packet says twice that Q5 puts that reading to the owner; Q5 asks something else

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:509–510` (Gate 3 act rows for
slices 4 and 5), `:854–869` (Gate 5) against `:75` (Q5).

**Defect.** Slices 4 and 5 are authorized, on the packet's own account, by
"the recorded-finding arm of the 2026-08-30 direction, naming L6-F5 / L6-F1"
— because no requirement in either signed spec reaches the home route or
`model.surfaces` (a sweep I re-ran and confirmed: 24 POC requirements, 17
PWB requirements, 0 whole-word `home` in the POC spec, 6 in the PWB spec all
in the precedence table's `Home` column or the registry home field, 0 hits
for the backticked `surfaces` or `model.surfaces` in either). The trace rule
itself is quoted correctly from
`.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`
lines 55–56.

The packet then says, twice, that this reading is put to the owner:

- `:510` — "Same continuation, on the same recorded-finding arm naming
  L6-F1. **Q5's confirmation is what makes that arm explicit rather than
  assumed**."
- `:869` — "**Q5 puts that reading to the owner.**"

Q5 (`:75`) asks: "Run the return path once (slice 6): is it authorized, and
what may it honestly be expected to produce?" It contains no limb about
whether a vision-pursuit audit finding counts as a "recorded review finding"
under the 2026-08-30 direction, and no limb about slices 4 or 5. No question
in Q1–Q7 carries that reading.

The reading is defensible on the merits — the L6 audit is an audit of the
runnable POC in fresh context producing evidence-cited findings, which is
the direction's own definition of a cycle's step (1) — but the direction's
worked example is a finding in `docs/reviews/`, the L6 findings live in
`docs/pursuits/2026-09-13-vision-pursuit-data.json`, and the direction also
requires each new bead to "alter the runnable demonstration or
falsify/repair a named product finding". That is a live question, and the
packet's own account is that it needs owner confirmation.

**Repair.** Either add the reading as an explicit limb of a question (Q7 is
the natural home, or a new Q8), or drop the two sentences claiming Q5
carries it and state the arm as the packet's own [Inferred] reading with
its risk. As drafted, the owner answering Q1–Q7 as posed authorizes slices 4
and 5 without ever seeing the authorization argument they rest on.

---

### N1 — non-blocking — Orrery's derived id lists are at `model.ts` lines 747–748, not 745–746; the error is repeated three times inside the packet's own re-verification table

`:76` (Q6), `:645` (slice 4), `:340` (source-citation table), and
`docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`
(`derived_vs_handwritten_surfaces`).

At `a9f671e`, `packages/three-surface-poc-core/src/model.ts:747` is
`entityIds: entities.map((entity) => entity.id),` and `:748` is
`relationshipIds: relationships.map((relationship) => relationship.id),`.
Lines 745–746 are `title: 'Orrery',` and the `question:` string.

This lands inside the table the packet offers as its own added value ("Every
one below was re-read at `a9f671e` this session"), which is where a wrong
number costs most.

**Repair.** 747–748, in all four places.

---

### N2 — non-blocking — the two seam citations are off by one at both ends

`:708` ("`model.ts` lines 25–42"), `:75` ("`WORKER_CHANGE_SEAM` (lines
25–32)", "`WORKER_CHANGE_INTENT_ID` (lines 34–42)"), and the evidence JSON's
`"WORKER_CHANGE_SEAM": "29-32 with comment 25-28"` /
`"WORKER_CHANGE_INTENT_ID": "42 with comment 34-41"`.

Actual at `a9f671e`: the seam comment is 26–29 and the const 30–33; the
intent comment is 35–41 and the const 42. Line 25 is blank, line 34 is
blank, and line 33 (`} as const;`) falls outside the packet's range.

**Repair.** 26–33 and 35–42.

---

### N3 — non-blocking — the five relationship ranges use two different conventions, and the correction offered against the dossier is itself wrong

`:338` — "the five Unknown relationships | 562–581, 583–590, 592–599,
601–607, 609–616 | the dossier's '563–598' understates by one line at each
end".

The five object literals at `a9f671e` are 562–581, 582–590, 591–599,
600–608, 609–617 by brace. The packet's first range is by brace and the
other four are id-line-to-provenance-line; neither convention is stated. And
the whole five-block span is **562–617**, so the audit's `563-598` (which is
L2-F2's and L2-M1's evidence line, carried into the dossier) understates the
*end* by nineteen lines, not one.

**Repair.** One convention, stated, and the correct span.

---

### N4 — non-blocking — the `surfaces` literal closes at line 750, not 749

`:339`, `:484`. `surfaces: [` opens at 710 and `],` closes at **750**; the
file ends at 752, so the packet's separate correction of the dossier's
"710–756" overrunning by four lines is right.

---

### N5 — non-blocking — `model.surfaces` is one of five model fields `renderPocPage` reads, not "the home page's only input"; and the evidence JSON's "only other hit" claim is wrong by three

`:76` (Q6) and the evidence JSON's
`home_composition.renderer_model_field_sweep_method`.

Q6's load-bearing inference is "Deleting it deletes the home page's only
input, so deletion and slice 5 are the same change". `renderPocPage`
(`apps/three-surface-poc/src/routes.ts:77–96`) reads `model.surfaces` (78),
`model.project` (87, 89), `model.entities` (89), `model.capabilityId` (89)
and `model.evaluation` (92). Deleting `surfaces` removes the three panels,
not every input; the page's eyebrow, lede, heading, footer and exact tables
survive.

Separately, the evidence JSON says "the only other hit in the file is
`model.projectShape` at line 127, outside `renderPocPage`". A `grep -n
'model\.'` over the file returns hits at 35, 78, 87, 89, 92, 127, **133,
171, 172**. The *field-name set* the packet lists is correct; the hit-count
claim is not.

**Repair.** "the only input for the three surface panels", and correct the
sweep note.

---

### N6 — non-blocking — the "dossier overstates" correction is misattributed and the caveat it supplies is already in both sources

`:706–715` (slice 6) and `:75` (Q5).

The packet says 'M4's **"Why"** says the next evaluation narrows three
edges'. The sentence is in the dossier's **What** bullet
(`docs/pursuits/2026-09-13-vision-pursuit.md:204–206`, "the next evaluation
narrowing three edges from Unknown"); the "Why" bullet says something else.

More substantively, the honest-reporting caveat the packet presents as its
own correction is already recorded in both places it is correcting: the
dossier's own slice (6) reads "report honestly if an edge stays Unknown",
and L5-M7's slice plan reads "Report honestly if an edge stays Unknown: that
is the measurement, not a failure." The packet's *measurement* — that
`work-to-code` (line 588) and `code-to-evidence` (line 597) are
unconditional `unknown()` literals and that no relationship reads
`workerChange` or `testArtifactVerification` — is new, correct and valuable
(I re-ran the identifier sweep: hits at 30, 42, 124, 125, 418, 421, 426,
427, 430, 431, 433, 701, 702; the relationships array is 525–618; zero
overlap). The framing of the dossier as having overstated without caveat is
not.

---

### N7 — non-blocking — the "zero cross-surface deep links" universal is measured over four pages while the adjacent claim is measured over five, and the fifth page carries exactly the link form slice 5 proposes

`:97–107` (Gate 1 measurement 1), `:108–120` (measurement 2), and the
evidence JSON's `href_census.cross_surface_deep_links: 0` with predicate
"counted over all four pages".

The four-page figures all re-derive exactly (home 40 = 36 + 4; Trajectory
304 = 300 + 4; Orrery 23 = 19 + 4; Polaris 1,089 = 699 + 386 + 4). But
measurement 2 widens the population to five pages, adding the retained
exact-source capture — and that page's hrefs were never censused. I swept
it: 6 hrefs, 1 fragment, 5 non-fragment — the four nav links **plus
`/polaris#polaris-source-openspec-specs-switchboard-identity-spec-md`**, a
non-fragment link into another page at a named anchor.

Whether that counts as "cross-surface" is arguable (the exact-source route
is a Polaris sub-route, so the link is Polaris → Polaris). What is not
arguable is that the product already contains one working instance of the
deep-link-into-an-anchor mechanism slice 5's "every row a deep link into the
surface that owns it" proposes, and the packet's motif sentence — "Not one
link on any surface points at anything on another surface" — reads as a
universal over a population it did not measure.

**Repair.** State the predicate and the page population on the motif claim,
and census the fifth page. Naming the existing instance would strengthen
slice 5, not weaken it.

---

### N8 — non-blocking — the `walkthroughJudgment.outcome` correction is attributed to the dossier, which never names the field

`:323–325`. The path correction is right —
`walkthroughJudgment` has keys `['kind', 'evaluation']` in both captures and
`walkthroughJudgment.outcome` is `undefined`, while
`walkthroughJudgment.evaluation.outcome` carries the four values quoted. But
`grep -n walkthroughJudgment docs/pursuits/2026-09-13-vision-pursuit.md`
returns **no lines**. The wrong path is in the audit finding L5-F10's
evidence list, inside the pursuit *data* JSON.

**Repair.** Attribute it to L5-F10.

---

### N9 — non-blocking — Q6's "713 claim tuples" appears in no evidence record and carries no predicate

`:76`. The figure re-derives (`data-claim-id="` occurs **713** times on the
lane A tailnet capture, denominator: the whole page), but the evidence JSON
has no entry for it, and the packet states it bare. Note also that L6-F5,
the finding Q6 rests on, says 699 — the pre-lane-A figure — so the two
numbers in circulation for the same quantity differ by 14 and neither is
labelled with its capture.

**Repair.** Record the figure, its marker and its capture in the evidence
file; note the 699 → 713 movement.

---

### N10 — non-blocking — the registry file cited [Observed] for the write surface carries a candidate status string, and is the wrong instrument for the work-scheduler question

`:411–418`. `.syzygy/governance/declarations/adapter-registry/
POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` has top-level
`"status": "candidate-amendment-no-effect-until-owner-act"`. The five
`typedAuthority` values the packet quotes are exact
(`writeSurface: []`, `databaseAccess: []`, `networkAccess: []`,
`executeObservedCode: false`, `workingTreeRead: false`) and sit inside
`entries[0]`, not at top level. The packet cites the file without saying
which act made the entry effective — AGENTS.md's own recorded pattern is
that a bound file's banner can be permanently wrong, so a reader needs the
act named. See also F4 limb on authority type.

---

### N11 — non-blocking — "a third array state", "a fourth vocabulary" and "three vocabularies" are counts with no enumeration

`:72` (Q2). L5-M4's design has two legal states (a populated route, or the
explicit `none-modelled` value), which is the same count as slice 2's own
design (non-empty on Unknown, empty on Observed). And "a page that already
has three [vocabularies]" names no three and no denominator. These are
rhetorical figures in a question the packet asks the owner to treat as
contract-determined.

---

### N12 — non-blocking — "three paragraphs on" is the next paragraph

`:446`. The "fact of the render" sentence is at
`rendering-vocabularies.md:111–114`, inside the paragraph that begins at
line 98 — the one immediately following the RFC2-24 declaration at 92–96.
Both quoted fragments are otherwise verbatim; the first elides the clause's
continuation (", and covers Unknown states only — ...") without an ellipsis.

---

### N13 — non-blocking — v1.md's artifact phrase spans lines 119–120

`:719–723`, `:1103–1105`. The packet cites "v1.md lines 116–119" for "the
named workflows and the commits/sessions that used them"; the phrase runs
119–120. The criterion sentence it also quotes ("a workflow written solely
to satisfy this criterion does not count") is at 118–119, both verbatim.

---

### N14 — non-blocking — the capture provenance table leaves Orrery's byte size as an em dash

`:36`. Every other row carries a size; the evidence JSON records 37,048 and
`wc -c` confirms it. A provenance table that exists to record sizes should
not have a blank.

---

### E1 — editorial — five lines exceed 78 columns

Lines 1, 416, 466, 790, 812. Four are single unbreakable path code spans
(the adapter-registry JSON path, the RFC-0002 module path, and the two spec
paths) and one is the H1. AGENTS.md forbids reflowing a code span, so no
repair is available for four of the five; the H1 could be shortened.

### E2 — editorial — Butlers repository paths appear in the disclosure table in plain prose

`:250–258`. Nine rows name observed-repository paths uncoded.
`check_governance.py` passes (CG-1b bars backticked Butlers paths only), and
the evidence JSON deliberately genericizes the same rows to "source claim,
one excluded source". The asymmetry between packet and evidence record is
worth one sentence so a later reader does not read the JSON as a different
measurement.

---

## Figures table — every measured figure re-derived

Method column states the predicate; denominator column states the
population. All computed this session by script over the retained captures
and `git show a9f671e:<path>`; nothing transcribed.

| # | Packet value | Re-derived | Method | Denominator | Verdict |
|---|---|---|---|---|---|
| 1 | Objects carrying `resolutionRoutes` = 1,149 | 1,149 | recursive walk collecting objects with the key | machine answer | ✓ |
| 2 | …empty 1,137 / non-empty 12 | 1,137 / 12 | same walk | 1,149 | ✓ |
| 3 | Of the 1,137 empty, Unknown = 0 | 0 | `epistemic.label` histogram | 1,137 | ✓ |
| 4 | Of the 12 non-empty, Unknown = 12 | 12 | same | 12 | ✓ |
| 5 | Distinct non-empty route rows = 1 (`excluded-content`) | 1, exactly that row, 12 occurrences | dedupe of route objects | 12 | ✓ |
| 6 | Same eleven figures on the pre-lane-A capture | identical, value for value | same script, both files | both machine captures | ✓ |
| 7 | Decomposition 439 + 415 + 278 + 6 + 9 + 1 + 1 | exactly those parent paths | parent-path histogram | 1,149 | ✓ |
| 8 | `relationships` = 9, Unknown = 5, carrying routes = 0 | 9 / 5 / 0, same five ids | direct array read, both captures | 9 | ✓ |
| 9 | 22 disclosures, 13 routed, 9 not | 22 / 13 / 9, zero mixed | element-inner test for `data-unknown-reason="` and literal `Route:` | 22 | ✓ |
| 10 | Every offset, depth and reason in the 22-row table | all 22 rows match exactly | same sweep | 1,481,819 chars | ✓ |
| 11 | Literal `Route:` = 18; `data-unknown-reason="` = 16 (14 + 2) | 18; 16 (14 `excluded-content`, 2 `missing-declaration`) | string count and `re.finditer`, agreeing | whole page | ✓ |
| 12 | `<h2>` 7, `<h3>` 39 | 7 / 39 | tag sweep | whole page | ✓ |
| 13 | "Unknown, by reason" = 6th h3 of 7th h2, char 1,474,935, 99.5% | 1,474,935; h2 #7 of 7; h3 #6 of 10 | heading-text match, section partition | 1,481,819 | ✓ |
| 14 | `data-polaris-gaps` = 1 value "1"; 1 gap row `polaris-gap-excluded-content`, "12 claim(s)" | all four exactly | attribute and id sweep | whole page | ✓ |
| 15 | "One capability in depth" span 811,016–852,703 = 41,687 = 2.8% | 41,687; 2.8% | h2 offsets | 1,481,819 | ✓ |
| 16 | `<details>` 359, `<form>` 0, `<button>` 1 (`type="button"`) | 359 / 0 / 1, type `button` | tag sweep | whole page | ✓ |
| 17 | Polaris hrefs 1,089 = 699 + 386 + 4 | 1,089 = 699 frag + 386 source + 4 nav | href sweep, prefix-bucketed after query strip | whole page | ✓ |
| 18 | Home 40 = 36 (10 distinct) + 4 | 40 = 36 (10 distinct) + 4 | same | whole page | ✓ |
| 19 | Trajectory 304 = 300 + 4 | 304 = 300 (300 distinct) + 4 | same | whole page | ✓ |
| 20 | Orrery 23 = 19 + 4 | 23 = 19 (10 distinct) + 4 | same | whole page | ✓ |
| 21 | "zero cross-surface deep links" | 0 over the four surfaces; **1 non-nav cross-page anchor link on the fifth (exact-source) page** | same sweep, extended to the fifth page | 4 pages vs 5 pages | **partial — see N7** |
| 22 | One `<form>` and one `<button type="submit">` over five pages | 1 form (Trajectory), 1 submit button (Trajectory) | tag sweep, five captures | 5 pages | ✓ |
| 23 | Materialize panel at 242,386 of 244,506, 2,120 chars, 99.1% | 242,386; 2,120 to end; 99.1% | `<section class="materialize-panel">` offset | 244,506 | ✓ |
| 24 | Home 38,706 bytes / 38,682 chars; panels 6,438 = 16.6%; tables 24,612 = 63.6% | all four exactly | offsets 7,632 / 14,070 / end | 38,682 | ✓ |
| 25 | Home: `data-surface-entity` 17, entity/relationship ids 9/9, `epistemic-unknown` 18, `<h1>` and 5 `<h2>` literals | all exactly | attribute and tag sweep | whole page | ✓ |
| 26 | Return-path state: 4 field values, identical in both captures | all four exactly, identical | JSON read, both captures | both | ✓ |
| 27 | `walkthroughJudgment.outcome` is one level deeper | confirmed: keys are `kind`, `evaluation` | JSON read | both | ✓ (misattributed, N8) |
| 28 | Lane A churn: 0 rows for `routes.ts`, `trajectory.ts`, `packages/three-surface-poc-core/`; `polaris.ts` +25/−6; 146 files total | 0 / 0 / 0; +25/−6; 146 | `git diff --numstat f4589e2..a9f671e` | 146 files | ✓ |
| 29 | 1,484,487 / 1,478,637 bytes; 84,487 / 78,637 over 1,400,000; 612,665 / 618,515 under 2,097,152 | all four arithmetic results exact; `q3Target.bytes` = 1,400,000 and shortfalls 84,487 / 78,637 in the lane A record | `wc -c`, arithmetic, evidence file read | — | ✓ |
| 30 | POC reqs 24, PWB reqs 17; `home` 0 in POC, 6 in PWB (all precedence/registry); `surfaces`/`model.surfaces` 0 in both | 24 / 17 / 0 / 6 (lines 247, 277, 510, 511, 518, 523) / 0 / 0 | `grep -c '^### Requirement'`, `grep -owic`, literal search | both spec files | ✓ |
| 31 | "documentation portal" 11 hits over 8 files, 1 definition + 7 citers | 11 / 8, file list matches the packet's description exactly | `grep -rnF` over `.syzygy/governance/` | that tree | ✓ |
| 32 | Register: last numbered row P-53, no P-6x **row**, last note P-67 | last row P-53; `^\| P-6x` returns 0 rows; P-66/P-67 appear only in update notes (9 `P-6[0-9]` matches, none a table row) | `git show a9f671e:` + anchored grep | the register on main | ✓ |
| 33 | RFC2-24's twelve cells equal `UNKNOWN_REASON_ROUTES` word for word | **5 of 12 identical, 7 differ** | table extraction and key-by-key compare | 12 | **✗ F1** |
| 34 | `routesFor` returns `[]` exactly when the label is not Unknown | **two branches**; also returns `[]` for an Unknown with no `reasons` | read of line 151 + `EpistemicState` arms | — | **✗ F2** |
| 35 | 9 rendered Unknowns carry no closed reason and no route | 9, exactly the ids listed (4 entities + 5 relationships; machine answer confirms 4 of 9 entities Unknown) | element-inner sweep + machine cross-check | 22 / 9 | ✓ |
| 36 | Every empty route array belongs to an Observed claim | true on both captures | label histogram | 1,137 | ✓ (data only — see F2) |
| 37 | `label.no-route` at `polaris-copy.ts:193`, used at `polaris.ts` 466 and 473, listed at `polaris-copy.test.ts:299` | all four exact; 0 occurrences of the literal on the capture | file reads + string count | — | ✓ |
| 38 | `model.surfaces` line span 710–749 | opens 710, closes **750**; file ends 752 | file read | 752 lines | **✗ N4** |
| 39 | Orrery's derived lists at 745–746 | **747–748** | file read | — | **✗ N1** |
| 40 | Trajectory / Orrery disclosure populations | **not stated in the packet**; measured 0 and 0 (301 and 11 `epistemic-unknown`) | attribute sweep | each page | **gap — F5** |

Every other line-number citation in the packet's re-verification table
(`:332–351`) was re-read at `a9f671e` and holds: `PocRelationship` 80–88,
`PocSurface` 90–96, `unknown()` 305–307, `workerChange` 418–423,
`testArtifactVerification` 431–437, carried at 701–702,
`UNKNOWN_REASON_ROUTES` 89–102, `ResolutionRoute` 115–118, field at 128,
`routesFor` 150–154, `MATERIALIZE_HUMAN_PATH` 17, panel 55–81 with the form
at 78, `MATERIALIZATION_EXTERNAL_REF` 9–10, `requirementId` literal type at
15, `buildMaterializationPacket` 43–65, `TestArtifactRecord` 11–19 and 73,
the SEC-3 comment 3–7, `surfacePanel` 34–55, `renderPocPage` 77–96,
`gapReasonCounts` 922–931, `gapsList` 933–948 with `foremost` at 938,
`gapId` 136 and the linking at 145, `governance-inputs.ts` 36–41 and 48–52.

Every contract quotation was checked against its defined clause and is
verbatim: RFC2-24 at `rendering-vocabularies.md:92` and the "fact of the
render" sentence at 111–114; VIS-1 at `vision.md:82` (quoted text at 88–92);
VIS-2 at 96; VIS-4 at 122; VIS-5 at 141; the unnumbered escape-property
paragraph at 61–64, quoted in full; the success sentence at 234–236;
POC-REQ-060 at spec 927 with its scenario; PWB-REQ-020 at 902; PWB-REQ-004
at 487; the 2026-08-29 direction's demonstration list at 18–22 and
invariants at 26–32; the 2026-08-30 direction's trace rule at 55–56; the
2026-09-02 act's "does not authorize" list at 68–84 and escalation triggers
at 86–94; v1.md at 30–31 and 116–120.

---

## Q1–Q7 assessment

| Q | Problem scope truthful? | Genuine owner gate? | Recommendation follows from the evidence? | Lawful arms complete? |
|---|---|---|---|---|
| Q1 | **Partly.** The 9-of-22 figure is exact and the four entity / five relationship decomposition is confirmed. But the scope is Polaris-only while POC-REQ-060 quantifies over three surfaces, and the two unmeasured surfaces carry a *third* encoding (bare `epistemic-unknown`, 301 + 11 occurrences) the packet never names (F5). | **Yes.** Whether a `PocRelationship` is an "Unknown claim instance" is genuinely unsettled and the packet says so and labels it [Unknown] — good. Ruling a rendered population in breach of an in-force requirement is the owner's. | **Yes on the falsifier; no on the remedy as written.** The two-encodings argument holds. The proposed remedy renders RFC wording beside the implementation's different wording for the same reason, which re-opens the falsifier (F1). | **Yes, and unusually well.** The "answered the other way" branch at `:1116–1124` states the divergence, names where it would be written down, and refuses to smooth it. This is the packet's best passage. |
| Q2 | **No.** The measurement is exact; the code claim it rests on is false. `routesFor` has a second `[]` branch and `EpistemicState` carries a `basis: 'deferred'` Unknown arm, so a routeless Unknown is modelled today (F2). | **Weakened.** Presented as contract-determined with one lawful arm, "for confirmation and disclosure rather than as a free choice". That framing cannot stand on a false statement of the code. | **No.** "Unreachable by construction" does not follow; neither does "forbid the empty array on an Unknown at the type level", which would make an existing cap1-core arm unrepresentable. | **No.** The deferred arm is a third arm the packet does not offer, and `label.deferred` — the declared copy row that fits it — is never named. The packet's own S5 scenario contradicts limb (b). |
| Q3 | **Yes.** The write-root analysis is right, the two reasons the packet "found and neither move stated" are real, and the empty write surface is quoted accurately. | **Yes — the clearest gate in the packet.** A new write effect into `.syzygy/governance/decisions/` about another project is squarely the owner's. | **Yes.** Arm (a) with a narrow act, arm (b) as a lawful partial, arm (c) decline — and the recommendation to build the pure drafter regardless (`:1111–1114`) is sound and cost-free. | **Yes.** Three arms, each lawful, each costed. No smoothing. |
| Q4 | **Yes.** `data-polaris-gap` occurs once, id `polaris-gap-excluded-content`, text "12 claim(s)" — confirmed. The observation that a four-reason filter has no negative case in today's evaluation is exactly right and is the kind of thing a funnel should find. | **Yes, and honestly labelled as a real choice between two lawful arms** — the only question so labelled. | **Yes.** Reusing the tested `foremost` ordering at `polaris.ts:938` rather than minting a second closed constant follows from the evidence and from the project's own drift lessons. | **Yes.** Both arms stated, the owner's reason for preferring the filter stated in the owner's terms ("if the band must never show a reason they cannot act on"), no consensus smoothing. |
| Q5 | **No.** The *expectation* half is excellent and newly measured (the two unconditional literals, the seam-scoping comments, the zero-overlap identifier sweep). The *authorization* half omits that the run writes a work item into the observed repository's tracker, and inverts the registry reading it applies in Q3 (F4). | **Yes for the expectation; the authorization limb is put as settled when it is not.** | **The expectation recommendation follows and is valuable** — ruling in advance that one edge narrowing and two staying Unknown is a pass is exactly VIS-2 applied. **The authorization recommendation does not follow** from the act text quoted. | **No.** The arm "this needs a continuation naming the work-scheduler effect" is never offered. The packet's two "writes nothing to the observed repository" sentences foreclose it rhetorically. |
| Q6 | **Yes on the defect.** `model.surfaces` does declare 4 entities for Polaris; the page does render 415 items and 713 `data-claim-id` markers; Orrery's lists are already derived. | **Marginal.** Deleting versus deriving a payload field no requirement governs is close to engineering judgment. It is defensible as a gate only because nothing specifies the field — which the packet establishes well. | **Mostly.** The conclusion (derive, don't delete) is right; the step "deleting it deletes the home page's only input" is false and is the step that makes deletion and slice 5 "the same change" (N5). The "already derived" catch is a genuine improvement on L6-M4. | **Yes** — both arms of the move are carried, and the cost of deletion is named rather than assumed away. |
| Q7 | **No.** The register analysis is exact and carefully predicated (last numbered row P-53, no P-6x *row*, last note P-67) and the branch-staleness risk is declared [Unknown]. The collision analysis is wrong in both directions and misses M3 slice 3 entirely (F3). | **Yes.** Ordering four packages against each other is the owner's. | **No.** "Slices 1–6 may start now" is derived from a shared-file set that under-counts M2 by four files and M3 by one, and from a reading that misses a duplicate feature. | **Incomplete.** The arm "M3 slice 3 and M4 slice 3 are one band and one of them must yield" is never offered. |

**Smoothing check.** I found no place where an owner trade-off is smoothed
into consensus language, and several where the packet deliberately preserves
one (Q1's other-way branch, Q4's "the owner may prefer the filter; say so",
Q6's note that deletion has a cost the move does not name, Q2's disclosure
framing). The defects above are errors of fact and of analysis, not of
candour.

**Lawful-arm check.** No lawful arm is called unlawful. Two arms are
*missing* rather than mislabelled: the `basis: 'deferred'` treatment in Q2
(F2) and the continuation-act arm in Q5 (F4). One arm is foreclosed by an
incorrect factual premise rather than argued against: Q2's `none-modelled`.

**Act coverage.** Slice 7's act requirement (arm (a)) and slice 8's two acts
are correctly identified, and the DEFERRED-WAVE-POSTURE constraint on citing
RFC10-7 is carried faithfully from L5-M5. The gap is slice 6 (F4) and the
unasked recorded-finding reading behind slices 4, 5 and 7 (F6).

---

## Counts

| Severity | Count |
|---|---|
| blocking | 6 |
| non-blocking | 14 |
| editorial | 2 |

## What the packet does well, for the record

The machine-channel measurement is the strongest part: every one of the
eleven route figures re-derived exactly, on both captures, and the packet's
correction of the dossier's reading — that the 1,137 empty arrays are the
*correct* encoding of Observed and that the routeless Unknowns are somewhere
else entirely — is a real and non-obvious finding. So is the discovery that
`work-to-code` and `code-to-evidence` are unconditional literals with the
seam deliberately scoped away from them; that single measurement changes
what the return-path run can honestly promise, and the packet found it by
reading the code rather than trusting the move. The dossier-citation
re-verification table caught three real errors in its source. The Q1
other-way branch is a model of how to write an owner question.

Verdict: REVISE
