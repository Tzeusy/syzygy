# Owner decision packet — PWB anchor-resolution amendment (N9, PWB half)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts four questions to the owner; only the owner's
> answer binds anything (VIS-4). Register row: P-96.

**Status:** drafted 2026-10-03 under bead `syzygy-u05.9`. One fresh-context
review round covers this package and its POC sibling; its verdict and
dispositions are recorded in `ROUND-1-DISPOSITIONS.md` beside this file once
the round has run.

## What you would be signing

One amendment to PWB-REQ-014 in the signed PWB specification. Read
`SEMANTIC-DELTA.md` for the full account. In short:

- **One anchor shape.** Every anchor the machine narrative serves carries the
  same fields, and its identity names the block it belongs to. [Observed]
  Today's 902 anchors already do, so this writes down existing behaviour
  rather than asking for new work.
- **A resolution count.** Each anchored block, and the narrative as a whole,
  carries `anchorsResolved`: how many of its anchors resolve against the
  machine answer, out of how many. [Observed] At Butlers `32f38feb` the
  narrative would read 883 of 902. The 19 that do not resolve point at
  records the machine answer serves without an identity of their own.
- **Still never authority.** Every narrative unit stays `non-citable`, at 902
  of 902 as at 0 of 902.

**What the bead asked for and this package does not do.** The bead said
"compute citable from the 934 resolved anchors instead of hardcoding false".
Signed PWB-REQ-014 and accepted RFC7-3 both forbid that; question 2 asks
whether you want to change the contract.

**What signing does not do.** It starts no implementation. Building the
count needs a fresh implementation authorization after sign-off.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | Signed by version tag under Scope A. The sign-off change applies the patches and carries the reconciliation updates listed in `IMPACT-LEDGER.md`. |
| Decline | PWB-REQ-014 stays as signed; the narrative serves no count. |
| Revise | Name what to change; a new version gets a new review round. |

## Question 2 — should citability ever follow from resolved anchors? (not drafted)

This is an open question, explicitly not drafted here. Answering "yes" starts
a contract amendment, which is a separate owner act; it does not change this
package.

[Observed] RFC7-3, at
`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` line 111,
says no citation anywhere in Syzygy "may resolve to a Polaris narrative,
section, claim block, rendering, or editorial draft as its authority". RFC7-4
says "Non-authority is total."

**The drafter's reasoning [Inferred].** An anchor that resolves proves the
narrative points at something real. It does not make the narrative's sentence
true, and it does not make the narrative the place a fact lives. The fact
already lives in the record the anchor resolves to, which is citable in its
own right. A reader who wants to cite should cite that record, and the anchor
tells them where it is. Making the block citable would give a second home to
the same fact, which is what RFC7-3 exists to prevent (its own note:
"a second source of doctrine cannot form if nothing may cite it").

| Option | Meaning |
|---|---|
| **Keep RFC7-3 as accepted** (recommended) | Nothing further. The count in question 1 is the honest machine signal. |
| Commission an RFC7-3/RFC7-4 amendment | A contract successor is drafted and reviewed on its own, and signed by its own act. PWB-REQ-014's `non-citable` rule would then need a further spec delta. |

## Question 3 — the deep-dive's second source-reference shape

[Observed] On the same route, the capability deep-dive's `intent.leaf` record
names its source with `path`, `revision` and `identity`, not with the anchor
shape. It occurs once at this capture. It is governed by PWB-REQ-015's
exact-intent band, not by the anchor set, so this package leaves it alone.

| Option | Meaning |
|---|---|
| **Leave it** (recommended) | One instance, and its identity already equals a block anchor's target identity. |
| Commission a PWB-REQ-015 delta | That record takes the anchor shape too, in a separate package. |

## Question 4 — show the count on the page?

The amended text says Polaris "need not render" the pair, because it is a
narrative attribute and not a project-shape claim, and PWB-REQ-020 compares
only project-shape claims.

| Option | Meaning |
|---|---|
| **Machine only** (recommended) | As drafted. |
| Render it too | A further delta extends PWB-REQ-020 to compare it across both views. |

## Order against the pending PWB packages

The class-granular and release-label packages are also pending
against this specification. They touch other requirements, and all three spec
patches compose in either order. Each rewrites the dependency declaration's
one digest line, so whichever you sign later is regenerated over the earlier
one first. That is mechanical and needs no answer from you.

**Against the behaviour-contract re-pin (P-95).** Every signed PWB spec change
leaves the observer registry entry's and the policy's spec pins pointing at
the old spec. Signing this package before the P-95 acts means the P-95 package
is redrafted over it; signing it after means the pins go stale again and need
another re-pin. Neither order stops Butlers reads, because the read gate does
not read the pin. If you plan to sign both, signing this one first saves one
round of re-pin acts. (`IMPACT-LEDGER.md` has the detail.)
