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

- **(1e)** *(added 2026-08-11, owner charter §7 — the typed arm)* **Type
  the cell rather than widen it vaguely**: amend RFC3-15's `contracts/`
  cell to a **closed enumeration of three occupant classes** — accepted
  contract modules (`rfcs/`), integrity-bearing manifests
  (`wave-manifests/`), and one explicitly named **non-normative resolution
  lane** holding `history/`, `matrix-rows/` and the two generated reports,
  each declared outside every digest set and each carrying its own
  "nothing here binds" statement. A closed enumeration is not a stretched
  category.
- **(1f)** *(added 2026-08-11; named so the space is visibly searched, and
  **rejected**)* Let the ceremony rewrite the relative references while
  copying, so accepted bytes stay put and installed links resolve.
  Rejected: the ceremony's own invariant is "Installation, bytes
  unchanged", verified by `sha256sum -c`. An installed byte that differs
  from the accepted byte makes the digest verification meaningless.

**What every arm costs, measured** *(added 2026-08-11 — this table did not
exist when the (1d) recommendation was made, and it changes the answer)*.
Swept over all 39 candidate modules: **19 of 19 Wave A modules and 11 of 11
Wave B modules carry code-span links into `history/`** — 68 references
across the 30 launch-path modules. Any arm that moves the companions
elsewhere requires rewriting all of them.

| Arm | Modules whose bytes move | Wave A confirmation (RD-31b) | Wave B confirmation (RD-32c) |
|---|---|---|---|
| (1a) outside `governance/` | 19 A + 11 B | retired | retired |
| (1b) widen the cell | **1** | retired | **survives** |
| (1c) drop the copies | 19 A + 11 B | retired | retired |
| (1d) mint `contracts-companion/` | **1 + 19 A + 11 B** | retired | retired |
| (1e) typed closed enumeration | **1** | retired | **survives** |

**There is no arm that preserves the current confirmations.** Whichever is
ruled, at least the Wave A exact-package gate re-runs on a regenerated
argument. The arms differ in how many modules move and what the tree means
afterwards.

**Recommendation `[Inferred]` (replaced 2026-08-11, owner charter §7):
(1e)** — it moves one module instead of thirty, retires one confirmation
instead of two, keeps every reference resolving without touching an
accepted reference, and states what the tree contains instead of stretching
a category.

*The 2026-08-10 recommendation of (1d) is withdrawn.* It was reasoned from
RFC3-15(a)'s precedent, which is sound as far as it goes, but it was made
without the reference measurement above: **(1d) is the most expensive arm
in the space** — an RFC3-15 amendment *and* a 68-reference rewrite, because
a category minted at `governance/contracts-companion/` is not where
the `../../history/` reference inside an installed RFC-0002 README
lands. (1b)
remains offerable and is (1e) without the closed enumeration; (1d) remains
offerable at its now-stated cost.

**Honest counter-argument to the recommendation.** (1e) keeps historical
rationale and generated measurements inside the contract home, under a
name. The charter's typing would send them out of it entirely. The reason
(1e) does not is the 68 references, which is a cost argument, not a
principled one. An owner who values the clean type boundary above that cost
should take (1a) or (1c) with the two-wave re-review priced in — and that
is a legitimate ruling, not a mistake.

Supporting measurement, method and denominators:
`../contracts/candidates/round-2026-08f/P33-SEMANTIC-INSTALL-ANALYSIS.md`.

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

*Added 2026-08-11, under the launch posture:* **there is no final wave act
on the offer path.** Waves C1/C2/D1/D2 are deferred, so (2a) does not mean
"install later" — it means "install never, while the posture stands", and
the package-identity record simply would not exist in the governed tree.
That consequence belongs in the ruling rather than being discovered after
it. (`../contracts/candidates/DEFERRED-WAVE-POSTURE.md`)

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
