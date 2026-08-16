# Owner decision packet — Wave A installation shape (P-33)

> **This file decides nothing.** It is the bounded packet for **P-33**, the
> single decision withholding the offer of an already-confirmed Wave A.
>
> *Rewritten 2026-08-13 as a bounded packet after review **RD-49** returned
> `REVISE` with three findings marked BLOCKING, one of which was that an owner
> could not rule from the previous version at all. The arm-by-arm history —
> six arms, a withdrawn recommendation, a false headline — is **not restated
> here**. The measurement and clause derivation behind every figure is
> `../contracts/candidates/round-2026-08g/P33-SEMANTIC-INSTALL-ANALYSIS.md`.*

## Question

When a wave act installs its accepted contract modules, **what else goes into
`.syzygy/governance/contracts/`, and does anything move that an act has
already bound?**

## Current authority

Candidate clause **RFC3-15** (`RFC-0003/governance-homes-and-owner-acts.md`),
the `contracts/` row, quoted exactly:

> | `contracts/` | Accepted load-bearing contracts (RFCs), including normative
> data contracts and external service contracts | …

and its framing sentence:

> The **five** constitutional categories of `.syzygy/governance/` hold,
> **exclusively** … A plane validator therefore accepts exactly these six
> names and **rejects a seventh**.

The install ceremony as currently written copies six classes of companion into
that home. **One of the six is admitted by those words.** A wave manifest is
not an RFC; neither is a history file, a matrix-row file, or a generated
report. Either the ceremony changes or the clause does.

## Two things worth knowing before you read the options

### 1. What actually retires a confirmation

The Wave A act's argument is `sha256` of the **whole** `WAVE-A-MANIFEST.txt`
file. That file is four generated header lines followed by 19 per-module
digest rows. The fourth header line reads:

```text
# This file's own sha256 is the argument of the phrase `ACCEPT FOUNDATIONAL WAVE A: <sha256>`.
```

So the rule is:

> **The argument regenerates — and the confirmation retires — if any listed
> module's digest changes, any row's path changes, or any of the four header
> lines changes, including the line that names the acceptance phrase.**

*(Corrected 2026-08-13, review RD-54 finding 2. An earlier form of this
section said the manifest was "19 per-module digest rows and nothing else"
and concluded that a ceremony-only change retires nothing. **That was false in
the direction the recommendation relied on**: renaming the acceptance phrase
regenerates the header, regenerates the argument, and retires the confirmation
without touching a single module. The acceptance record shows two phrases
already retired, so this is not hypothetical. `[Observed]` — the argument
`8972d963…` recomputes from the whole file, not from the rows alone.)*

The practical consequence for this decision: **choosing where a companion goes,
or declining to install it, still costs nothing — provided the ruling does not
also rename the acceptance phrase.** RFC3-15 and RFC3-20 both live in
`RFC-0003`, a Wave A row, so any arm that amends either clause retires Wave A;
any arm that rewrites the modules' internal path strings retires both.

### 2. What this decision cannot fix

**`contracts/` will not hold `rfcs/` alone under any option here.** A wave act
does not retire the candidate home — the acceptance record says retirement of
`contracts/candidates/` is "a separate" matter — so after the act the category
holds `candidates/` **and** `rfcs/`, and `candidates/` contains every companion
class this decision is about, plus the review lane and seven round trees.

*(Added 2026-08-13, RD-54 finding 1, which is the reason no option below claims
category purity.)* The containment breach RFC3-15 describes is therefore **not
created by the install ceremony**; the ceremony adds to a breach the candidates
tree already constitutes. Full purity needs a *second* decision — where the
candidates tree lives — which is out of P-33's scope as queued and is recorded
below as the follow-on it implies.

## Options

All three options install accepted modules at `contracts/rfcs/` and add no
companion beside them; all three satisfy RFC3-15's `contracts/` cell **as far
as the install ceremony can**, with no amendment. Every figure below is
`[Observed]` unless marked.

### (M) Leave the modules' internal path strings alone — *recommended*

Companions are not installed. Wave membership travels inside the owner-act
record. Rationale, matrix rows and generated reports stay in the candidates
tree, where they are today and where every clone can read them.

```text
accepted bytes moved              0                        [Observed]
Wave A confirmation               survives                  [Inferred]
Wave B confirmation               survives                  [Inferred]
RFC3-15 amendment                 none                      [Observed]
path strings left dangling        88  (45 A, 33 B, 10 deferred)  [Observed]
rendered links broken             0   — none is a Markdown link  [Observed]
in-tree integrity artifact        none — re-verifying the 19 installed
                                  modules requires the digests in the act
                                  record, not a file beside them
re-review required                none                      [Inferred]
```

**What the owner is accepting:** inside the *installed* tree, 88 path strings
in module prose point at files that are not beside them. A reader who follows
one by hand lands nowhere. The same string resolves in any clone of this
repository, and **no clause requires it to resolve**: `[Observed]` 9 hits for
link-obligation language across 6 of the 39 modules; `[Inferred]` each governs
a *rendered* runtime reference, the nearest being RFC6-20, which binds only
where a surface renders a citation as a link. `[Observed]` doctrine's own link
rule (VIS-7) is scoped to rendered internal *project-entity* links across seven
named classes and does not reach a file path in a contract module's prose.

*Also: ceremony step 3 verifies the copy by running `sha256sum -c` against the
wave manifest from inside `contracts/`. Under (M) that file is not there, so
the step must be re-pointed at the candidates tree — a ceremony edit, free
under the corrected rule above provided the phrase is untouched.*

### (M+) As (M), and move the candidates tree out of `governance/`

The only option that actually leaves `contracts/` holding `rfcs/` alone.
RFC3-15's scope stops at `.syzygy/governance/`, so a home outside it needs no
amendment, and the wave-manifest rows are candidates-root-relative, so the
manifests' bytes — and therefore both arguments — do not move.

```text
accepted bytes moved              0                         [Observed]
both confirmations                survive                   [Inferred]
RFC3-15 amendment                 none                      [Observed]
contract-category purity          FULL — the only option achieving it
path strings left dangling        88, as (M)
cost                              every artifact citing `contracts/candidates/…`
                                  by path is repointed. Population not yet
                                  measured                  [Unknown]
```

**What the owner is accepting:** an unmeasured repointing cost across the
repository, in exchange for the one thing (M) cannot deliver. *(Added
2026-08-13, RD-54 finding 1. Its cost is honestly `[Unknown]` — it was
identified after the measurement pass, and quoting a number here that nobody
computed is the failure this packet exists to avoid.)*

### (T) Rewrite the strings so the installed tree is self-contained

As (M), plus every internal reference repointed at its new location.

```text
accepted bytes moved              all 30 modules (19 A + 11 B)  [Observed]
Wave A confirmation               RETIRES                       [Inferred]
Wave B confirmation               RETIRES                       [Inferred]
RFC3-15 amendment                 none
path strings left dangling        0
re-review required                one full exact-package review per wave
```

**What the owner is accepting:** the two `CONFIRM` verdicts already obtained
(RD-31b, RD-32c) stop covering anything, and each wave must be re-reviewed on
a regenerated argument before it can be offered. *"All 30", not "up to 30":
every module in both waves carries at least one such reference — 19 of 19 and
11 of 11, measured.*

## Recommendation `[Inferred]`

**(M).**

The reasoning is not digest preservation for its own sake. It is that
**every option here leaves the contract category in the same condition** — the
candidates tree sits inside it under all three, and only (M+) changes that, at
an unmeasured cost. None of the three requires an RFC3-15 amendment. So (M)
and (T) do **not** trade cleanliness against economy; they trade one thing
only:

> Must a path string inside an installed module resolve from inside the
> installed tree?

Answering *yes* costs two confirmations and two full re-reviews. What it buys
is that 87 inert strings — none of them rendered, none of them required by any
clause, all of them resolvable in the source repository — resolve one more
place.

**Where this departs from the charter's steer, and why.** The owner charter
directs preferring the clean typed layout *unless* confirmation preservation is
explicitly chosen over installed-tree self-containment. That instruction
assumed typing and preservation were in tension. **They are not** — the
measurement shows the clean typed layout is reachable without moving an
accepted byte. What remains is self-containment alone, and that is the narrower
thing the charter reserves for the owner to choose explicitly. **This is that
choice**, stated in one sentence rather than distributed across seven arms.

**Honest counter-argument.** An owner who holds that an accepted tree must be
readable on its own terms — that a governance home containing pointers to
nowhere is a defect regardless of what any clause requires — should take (T),
and should not regard the re-review as waste. The confirmations were obtained
once and can be obtained again; the installed tree is read for years. That is a
legitimate ruling and not a mistake. `[Inferred]` sits on the weighting, not on
the measurement.

## The manifest question — separate, and not bundled

The first wave act would install `ACTIVE-CONTRACT-MANIFEST.txt`, whose **39
rows span all six waves** while the act accepts 19 modules. That is not a
membership record; it is an inventory, and 20 rows of it would be over-claims.
Under the deferred posture C1/C2/D1/D2 are off the offer path, so **9 rows
would over-claim permanently**, not temporarily.

The two manifests are different artifacts and want different homes:

| Artifact | Is | Belongs |
|---|---|---|
| `WAVE-x-MANIFEST.txt` | **Accepted membership** — the argument the act binds | With the owner-act record. It *is* the argument |
| `ACTIVE-CONTRACT-MANIFEST.txt` | **Candidate package identity** | The candidates tree |
| An installed effective-state view | **Generated** from the acts performed | Generated, never hand-written |

**Recommendation `[Inferred]`: install neither package-wide manifest into the
accepted tree.** Wave membership rides with its act, which is exactly scoped
and needs no banner to be honest about what it covers.

*A previously recommended alternative — install the 39-row manifest with a
generator-written banner naming which waves are bound — is withdrawn. It
presumed machinery that does not exist (`build_active_manifest.py` contains no
banner logic), and it contradicted the containment fix it was paired with.*

## Which digest would change

| Under | Digest change |
|---|---|
| **(M)** | **None.** No file in any wave manifest is edited |
| **(T)** | `WAVE-A-MANIFEST.txt` and `WAVE-B-MANIFEST.txt` both regenerate, because up to 30 of their 30 rows change |

## Exact next transaction

There is no ceremony phrase — this is a recorded owner decision, not a
digest-binding act. Record here, dated, in your own words:

```text
P-33 RULED — Wave A installation shape
companion install shape:      M
package-wide manifest:        not installed
```

**Ruled 2026-08-16.** Owner, via an adversarially-reviewed questionnaire
packet, direct conversational response — chose **(M)**: leave the accepted
modules' internal path strings alone; install no companion package
apparatus; install neither package-wide manifest. Full record:
`PENDING-OWNER-DECISIONS.md` (row `P-33`, 2026-08-16 resolved section) and
the owner's local decision packet.

Then the register row P-33 closes, the ceremony is drafted to match, and
**Wave A becomes offerable** — under (M) on the argument `8972d963…` that
RD-31b already confirmed; under (T) after a fresh exact-package review of the
regenerated argument.

## Earliest required gate

**Before the Wave A offer.** Both defects are properties of the install
ceremony an act would freeze, and are unrepairable after binding. Wave A's
clause content is unaffected either way; only the ceremony and the reference
strings wait on this ruling.
