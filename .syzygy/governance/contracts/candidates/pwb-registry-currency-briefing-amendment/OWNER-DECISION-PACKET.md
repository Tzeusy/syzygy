# Owner decision packet — registry currency bounds and briefing ceiling

> **Candidate — binds nothing.** Prepared by agents under the owner's
> 2026-09-21 rulings in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
> which authorize drafting and nothing more. Effect would come from one
> superseding `adopt-registry-entry` owner act over the registry entry, and
> from nothing else. Silence, a commit, a review, a merged pull request or
> a passing check performs no act. This packet labels nothing accepted,
> adopted or in force, and no act record is written here.

## What this package is, in one paragraph

The cross-cutting reading "One registry act, not two" requires that the
declared currency bound (P-69 question 2, arm (a)) and
`maxBriefingResponseBytes` (P-72 question 2) travel as **one** superseding
registry-entry amendment act, gate bead `syzygy-dov.18`. This directory is
that preparation. It proposes new bytes for one artifact —
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
— without editing the bytes the act in force bound. `SEMANTIC-DELTA.md`
says what changes and why; `IMPACT-LEDGER.md` says what depends on it, by
count and denominator; `REVIEW-BRIEF.md` says what an independent reviewer
is to be given. **Two independent reviews have been run**, a first review
and a confirmation of its repairs; both verdicts and every disposition are
in the `## Review` section of `SEMANTIC-DELTA.md`, which names each raw.
Each review is bound to the bytes it names. The 2026-09-22 reconciliation
against the now-present `syzygy-dov.22` candidate changed the proposed ceiling
semantics and therefore retires both reviews for the current candidate bytes.
A fresh exact-byte review is required after the owner choices below are fixed.

## Every value here is the owner's

Fourteen numbers are proposed below. **Not one of them is agent judgment
the project should inherit.** They are carried in the diff only so a
single complete artifact can be reviewed and acted on; each is offered
with one line of reasoning and is expected to be overruled where the owner
sees differently. Changing any of them changes the manifest row and
therefore the act argument, so the decision belongs here, before an act,
not after one.

### The thirteen currency bounds (P-69 question 2, arm (a))

`assessCurrency` in `packages/cap1-core/src/staleness.ts` is the judge;
these rows are its only lawful input. A claim of a class with no row never
leaves Unknown. The proposed groupings run from slowest-moving intent to
fastest-moving fact.

| Claim class | Proposed `maxAgeMs` | Reading | One-line rationale |
|---|---|---|---|
| `project-account-section` | 31536000000 | 365 days | A project's own account of itself is the slowest-moving declaration in the corpus; a year-old section is stale news, not a wrong answer. |
| `principle` | 31536000000 | 365 days | A principle that changed inside a year was not a principle; the bound exists to catch abandonment, not revision. |
| `success-criterion` | 31536000000 | 365 days | Criteria are set with the intent they outlast a release cycle; same reasoning as `principle`. |
| `project-account-statement` | 31536000000 | 365 days | The six account statements are aggregates over `project-account-section`; a tighter bound than their inputs would stale the aggregate while its parts stayed current. |
| `design-contract` | 15552000000 | 180 days | A contract is expected to be stable but is amended deliberately; half a year is roughly two amendment cycles' grace. |
| `baseline-spec` | 15552000000 | 180 days | Specifications move with the work they govern, faster than principles and slower than the tree. |
| `craft-policy` | 15552000000 | 180 days | Same cadence as the two above; grouping them keeps three classes from disagreeing about one review cycle. |
| `catalog-entry` | 7776000000 | 90 days | A catalog is an index over things that move; a quarter-old index entry is worth doubting. |
| `topology-component` | 7776000000 | 90 days | Components appear and are renamed with ordinary engineering work. |
| `project-fact-declaration` | 7776000000 | 90 days | Counts and declared facts are the most falsifiable things here and the cheapest to re-derive. |
| `source-coverage` | 7776000000 | 90 days | Coverage is a statement about a file that may have been edited since; it should not outlive a quarter unexamined. |
| `roster-identity` | 2592000000 | 30 days | People and ownership change without a commit anywhere near the roster; a month is already generous. |
| `project-shape` | 2592000000 | 30 days | The whole-shape aggregate is the headline claim; it should be the first thing to admit age, not the last. |

**The trade-off the owner is being asked to price**, stated rather than
smoothed: a **short** bound makes the surface honest sooner and makes it
say Unknown more often, which is the correct direction under VIS-2 but
costs a page that answers less. A **long** bound keeps answers on the page
and risks presenting a year-old declaration as current. The four tiers
above are one defensible reading of that trade-off and not the only one; a
single uniform bound across all thirteen classes is also coherent and
would be simpler to explain.

### The briefing ceiling (P-72 question 2)

| Field | Proposed value | Reading | One-line rationale |
|---|---|---|---|
| `maxBriefingResponseBytes` | 20480 | 20 KiB | The design work that asked for this ceiling measured the two one-claim briefing compositions at 7,076 and 5,150 bytes and recommended 20,480 as roughly 2.9x the larger — deliberate headroom, not a tight budget and not the measured cost. The point of minting a third ceiling is that reusing the 8 MiB machine ceiling would let a briefing grow four hundredfold with nothing to stop it. |

**The trade-off**: 20 KiB is tight enough that the ceiling is a real gate
and loose enough for the fields the briefing is meant to carry. Set it
lower and a legitimate briefing fails closed, which is honest but useless;
set it higher and the ceiling stops being a constraint and becomes
decoration. Note that a breach of a response ceiling serves nothing and
logs nothing — the 503 body of the breaching request is its only trace —
so a ceiling set wrong is discovered by a reader, not by a check.

## Exact owner choices required before review and ceremony

The packet is decision-ready, not decided. The owner must explicitly answer
all three lines below; a general approval or the 2026-09-21 ruling answers none
of them.

1. **Currency bounds:** confirm all thirteen proposed `maxAgeMs` values above,
   or name every replacement value by claim class.
2. **Briefing ceiling:** confirm `maxBriefingResponseBytes = 20480`, or name its
   replacement value.
3. **Single-subject/category join:** confirm or replace this proposed reading:
   the `syzygy-dov.22` derived read-only machine-view member for the briefing
   has one required subject, **one exact project-shape claim identified by its
   full claim id**; any other fields in that response are same-evaluation joins
   independently derivable from the machine answer and do not become additional
   subjects. The ceiling applies to the complete encoded response body.

For line 3, the alternatives are deliberately explicit: the owner may (a)
confirm that reading, (b) name a coarser subject identity and its closed
population, which requires both candidate packages to be regenerated and
reviewed, or (c) decline the briefing member. No default is inferred.

## The act, if the owner chooses to perform it

One act, in the shape of the 2026-09-05 record
`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`:
act type `adopt-registry-entry`, superseding that record for the
`adopt-registry-entry` role only, over the same subject. The phrase form
is unchanged — the words `ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER
REGISTRY ENTRY` followed by the SHA-256 of the artifact being adopted.

### Not yet offered: the argument

**The exact argument is deliberately absent from this file, and from every
Markdown file in this package.** The argument of an `adopt-registry-entry`
act is the SHA-256 of the registry artifact itself. The bytes that hash to
the proposed argument exist nowhere in the tree — they exist only as the
result of applying the patch under `proposed/` to the current bytes,
which is exactly what keeps the act in force unbroken. Writing that
digest beside the act phrase in a Markdown file would put a digest there
that is neither the subject's current hash nor any performed act's
argument, which is the third state the governance battery exists to
reject.

The digest is therefore kept where it can be machine-derived and
machine-checked: the single row of `PWB-EFFECT-AMENDMENT-MANIFEST.txt` in
this directory, written and re-verified by
`scripts/build_pwb_registry_currency_briefing_amendment.py`. It is never
transcribed. To read it, run that script's `--check`, which re-derives the
row from the current subject bytes plus the patch and fails if either has
moved; then read the row. At the act, the recorder validates the owner's
phrase against the bytes then present.

### Why nothing is registered in `check_governance.py` now

Asked and answered precisely, because the repository's standing guidance
is to register an act's phrase and packet copies *before* the packet
exists.

1. **The act phrase needs no new registration.** `ADOPT POLARIS BUTLERS
   PROJECT-SHAPE OBSERVER REGISTRY ENTRY` is already a registered act
   label with this exact subject, through `PWB_EFFECT_ACTS` and its
   amendment row in `PWB_EFFECT_AMENDMENT_ACTS`. This is a *superseding
   act of the same type over the same subject*, so it reuses the label
   rather than minting one. That reuse is the whole reason P-69 question 2
   arm (a) was cheaper than arm (b).
2. **The new amendment row cannot be written yet.** A
   `PWB_EFFECT_AMENDMENT_ACTS` row carries the new act record's path and
   the **act-time performed digest**. Neither exists until the owner
   performs the act. Writing a row now would either name a record that is
   absent or assert a performed digest for an act nobody has performed.
   The row belongs in the adoption change, beside the new record and its
   recorder.
3. **Registering this package in `ACT_DIGEST_COPY_FILES` would be false
   and would fail.** That registry means "this file quotes that act's
   argument and must keep it current". No file here quotes it: the
   manifest is a `.txt` and carries no act label, and no Markdown file in
   this package contains a 64-hex token at all. Registering the manifest
   anyway would compare its proposed digest against the subject's current
   hash — which must differ while this is a candidate — and turn a correct
   candidate package into a standing failure.
4. **The precedent agrees.** The comparable lane-B package registers its
   *owner packet* and not its manifest, and it can do that only because
   its act's subject is its own in-tree manifest. This act's subject is
   the registry artifact, so that route is not available here.

At adoption, three registrations land together with the act: the new
`PWB_EFFECT_AMENDMENT_ACTS` row, the existence-gated registration of the
new packet's copy files, and the new record's own entry.

## What is still gated, and is not in this package

Performing this act does **not** make anything render differently. Two
further gates are named in the ruling record and neither is prepared here:

- **A plain owner continuation direction** (gate `syzygy-dov.19`). A
  registry amendment crosses an escalation trigger; the implementation
  that would read these fields needs its own authorization. Such a
  direction binds no digest, adds no acceptance-record row and registers
  nothing — which is why it is a separate, much lighter step, and why it
  is deliberately absent from this package rather than folded in.
- **The derived read-only machine view specification package** (gate
  `syzygy-dov.22`, present as the inert candidate
  `.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/`). It
  proposes the *category* and names the briefing member; this
  package declares the *ceiling*. The dependency runs both ways and
  neither half is sufficient alone: **no route is served before its
  ceiling is declared**, and a ceiling whose sentence names a category no
  specification defines would be a ceiling over nothing. If the owner
  performs this act and not that sign-off, the ceiling sits declared and
  unused, which is harmless; if the reverse, the category is defined and
  no route may be served under it.

The P-69 Q7a clarification scenario is a third gate on the M2 implementing
slice and is likewise not this package's.

## Open questions this package did not resolve

Listed rather than answered, because answering any of them would be
deciding something the drafting authorization does not cover.

1. **P-78 question 4 says breaches are "recorded against the two ceilings
   the registry already declares".** After this act there would be three.
   The ruling's sentence was written about M11's arms, where the registry
   is edited on no arm, so it is not in conflict on its own terms — but a
   briefing-route breach under a third ceiling is a case its words did not
   anticipate. Whether M11's breach recording extends to the third ceiling
   is unresolved here.
2. **P-77 question 6 requires every new machine field in the parity sweep
   as its own family with a declared empty human denominator**, and the
   same row says the registry entry is edited on no M10 arm. The fields
   added here are registry fields, not machine-response fields, so on the
   reading this package holds they are outside that sweep. That reading is
   not confirmed.
3. **`status` and `adoptionStatus` in the subject remain candidate
   strings under a performed act.** Both carry the entry's governance
   lifecycle, and both are left byte-identical here. Whether a superseding
   act is the right occasion to move them is an owner question; this
   package deliberately does not move them, because doing so would widen
   the act argument for a reason the ruling never gave.
4. **One existing check will go red at adoption without a defect behind
   it**: `scripts/build_pwb_truth_policy_amendment.py --check` hashes the
   subject's current bytes, which `--apply` moves. The comparable
   convention is that a superseded recorder fails its own `--check` by
   design, but that convention has not been extended to this builder by
   any ruling.
5. **Whether thirteen classes is permanently the complete set.** It is
   complete against today's two source files; nothing mechanically
   prevents a future class from being minted with no row, and the
   `undeclaredClass` sentence is what makes that safe rather than silent.
6. **Whether the proposed single-subject/category join is the owner's.** The
   sibling candidate is now in the tree and proposes `/api/poc/briefing` as a
   closed derived read-only machine-view member, but it remains inert and its
   owner-reserved values remain unresolved. This packet now proposes that the
   member's one required subject is one exact project-shape claim identified by
   its full claim id; same-evaluation joined fields remain derivable context,
   not additional subjects. The owner must confirm or replace that reading in
   both packages before either ceremony is offered. Raised originally as F6;
   this reconciliation changes the proposed bytes and retires both earlier
   reviews.

## How to verify this package before acting

All read-only:

```sh
python3 scripts/build_pwb_registry_currency_briefing_amendment.py --check
python3 scripts/build_pwb_registry_currency_briefing_amendment.py --selftest
python3 scripts/build_pwb_registry_currency_briefing_amendment.py --diff
python3 scripts/check_governance.py
```

`--check` proves the patch still applies to the bytes the act in force
bound and that the manifest row is an exact regeneration over the result.
`--selftest` mutates twenty-three predicates in turn and requires each to
fail closed; the count is the one the command prints. It covers every
assertion `structure_findings` makes and all three `check()` makes on its
own — the patch population under `proposed/`, a patch that changes
nothing, and an absent manifest — so no assertion either function makes is
left to inspection. `--diff` prints the proposed change in full.
