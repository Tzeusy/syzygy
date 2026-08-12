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

## The one thing worth knowing before you read the options

The Wave A act's argument is `sha256(WAVE-A-MANIFEST.txt)`, and that manifest
is **19 per-module digest rows and nothing else**. So:

> **A confirmation retires if and only if the arm edits a file that is a row
> in a wave manifest.** The ceremony text is in no manifest.

RFC3-15 and RFC3-20 both live in `RFC-0003`, which **is** a Wave A row. So
*any arm that amends either clause retires Wave A's confirmation* — and any arm
that rewrites the modules' internal path strings retires both.

**Choosing where a companion goes, or declining to install it, costs nothing.**

## Options

Both options put accepted modules at `contracts/rfcs/` and nothing else in
`contracts/`; both are typed, and both satisfy RFC3-15 **with no amendment**.
They differ on one axis only.

### (M) Leave the modules' internal path strings alone — *recommended*

Companions are not installed. Wave membership travels inside the owner-act
record. Rationale, matrix rows and generated reports stay in the candidates
tree, where they are today and where every clone can read them.

```text
accepted bytes moved              0
Wave A confirmation               survives
Wave B confirmation               survives
RFC3-15 amendment                 none
code-span path strings dangling   87   (44 Wave A, 33 Wave B, 10 deferred)
rendered links broken             0    — none of the 87 is a Markdown link
re-review required                none
```

**What the owner is accepting:** inside the *installed* tree, 87 backtick path
strings point at files that are not beside them. A reader who follows one by
hand lands nowhere. The same string resolves in any clone of this repository,
and no clause requires it to resolve — swept over all 39 modules, 9 hits for
link-obligation language, all of them runtime rendering clauses about product
surfaces.

### (T) Rewrite the strings so the installed tree is self-contained

Same homes, plus every internal reference repointed at its new location.

```text
accepted bytes moved              up to 30 modules (19 Wave A + 11 Wave B)
Wave A confirmation               RETIRES
Wave B confirmation               RETIRES
RFC3-15 amendment                 none, unless a history home is minted
                                  under governance/ — that amends the
                                  closure sentence, not just a row
code-span path strings dangling   0
re-review required                one full exact-package review per wave
```

**What the owner is accepting:** the two `CONFIRM` verdicts already obtained
(RD-31b, RD-32c) stop covering anything, and each wave must be re-reviewed on
a regenerated argument before it can be offered.

## Recommendation `[Inferred]`

**(M).**

The reasoning is not digest preservation for its own sake. It is that the
**typed layout is available under both options at no cost** — `contracts/`
holding `rfcs/` and nothing else is what makes either arm lawful, and it
requires no amendment either way. So the two options do **not** trade
cleanliness against economy. They trade one thing only:

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
companion install shape:      M / T
package-wide manifest:        not installed / installed
```

Then the register row P-33 closes, the ceremony is drafted to match, and
**Wave A becomes offerable** — under (M) on the argument `8972d963…` that
RD-31b already confirmed; under (T) after a fresh exact-package review of the
regenerated argument.

## Earliest required gate

**Before the Wave A offer.** Both defects are properties of the install
ceremony an act would freeze, and are unrepairable after binding. Wave A's
clause content is unaffected either way; only the ceremony and the reference
strings wait on this ruling.
