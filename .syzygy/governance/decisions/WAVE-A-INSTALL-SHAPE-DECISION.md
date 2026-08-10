# Owner decision packet — Wave A installation shape (P-33, current packet)

> **This file decides nothing.** It is the current packet for **P-33**
> (queued 2026-08-09 from review RD-18's blocking finding B2 and major
> M5); the register row still owns the queue entry. It must be ruled
> **before Wave A is re-offered**: both defects are properties of the
> install ceremony an act would freeze, unrepairable after binding.

## The principle at stake

The accepted contract home must not violate its own closed category
rules. RFC3-15's `contracts/` row says the home holds accepted contract
content **exclusively** — and the ceremony as written copies non-contract
companions (`history/`, `matrix-rows/`, two generated reports, the
manifests) into it. Companions are legitimate as **generated navigation,
historical rationale, and review evidence** — but they are not accepted
contract content, and either the ceremony or the clause must move.

## Question 1 — the `contracts/` containment breach (RD-18 B2)

Options:

- **(1a)** Install companions **outside** `governance/` (e.g. a
  non-governance `contracts-companion/` home) — keeps RFC3-15 pristine;
  backlinks repoint; the governed tree's reading paths cross a directory
  boundary.
- **(1b)** **Widen what the existing `contracts/` category may contain**
  by owner amendment to RFC3-15's `contracts/` cell. *(Restated
  2026-08-10, RD30-06 — an earlier form of this option claimed
  RFC3-15(a) provides this route. It does not: RFC3-15(a) records the
  precedent for minting a **new category** "by owner amendment rather
  than by stretching a category's 'exclusively'", and widening an
  existing cell's contents is exactly the stretching move the clause
  warns against. The option remains lawful — any owner amendment is —
  but its earlier justification was false.)*
- **(1c)** Drop the companion copies from the ceremony and repair the
  modules' backlinks to point at the candidates tree — smallest install,
  but the accepted tree's Tier-2 rationale links then leave the governed
  tree permanently.
- **(1d)** **Mint a new constitutional category for companion material**
  (e.g. `contracts-companion/` *inside* `governance/`) by RFC3-15(a)'s
  own recorded-widening route — the B19 precedent applied as written: a
  new named category with its own row, declared non-normative and
  outside every digest set, rather than a stretched `contracts/` cell.
  *(Added 2026-08-10, RD30-06 — the option the clause's recorded
  precedent actually implies, previously absent from this packet.)*

**Recommendation `[Inferred]` (re-labeled 2026-08-10, RD30-06): (1d)** —
it is the route RFC3-15(a)'s precedent provides for exactly this shape
("widen explicitly rather than stretch a category's 'exclusively'", the
module's own closing guidance), and it keeps the principle intact by
naming what the companions are instead of pretending they are contracts.
The earlier recommendation (1b) rested on a misreading of RFC3-15(a) and
is withdrawn as a recommendation, though (1b) remains an offerable
option.

## Question 2 — the 39-row manifest at the first act (RD-18 M5)

The first wave act installs `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows)
while that act accepts only its own wave's modules — the installed file
reads as an inventory of accepted content, 20 rows early.

Options:

- **(2a)** Defer the active-manifest install to the final wave act — the
  installed tree carries no over-claiming inventory, but loses its
  package-identity record until the last act.
- **(2b)** Install at the first act **with a generator-written banner**
  stating six-wave identity: the manifest is the package identity record,
  each row binds only when its wave's act fires, and the banner names
  which waves are bound (regenerated at each act). *(Reviewer-preferred.)*

**Recommendation `[Inferred]`: (2b)** — the generator owns the banner so
it can never go stale by hand; (2a) trades a labelled record for an
absent one, which VIS-2 disfavors.

## Consequences of not ruling

Wave A cannot be re-offered: RD-18 B2 is a blocking finding against the
act's own ceremony, and drafting either arm without the ruling would
repeat the F-17 pattern (an arm installed while its question was open).

## Earliest required gate

Before the Wave A re-offer (this pass prepares the offer; the ruling
gates it).

## Independent work

All Wave A clause repairs proceed (they are ruling-independent); only the
ceremony text and the RFC3-15 widening wait.
