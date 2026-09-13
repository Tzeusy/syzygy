# Owner decision packet — PWB scoped epistemic attributes (lane B)

> **Inert offering.** This packet performs nothing. It presents one decision,
> records nothing, and authorizes no implementation. A commit, a merged pull
> request, a review, a manifest, silence or a general "approved" performs no
> act.

Date: 2026-09-14 (third draft; the first two drafts' reviews returned
REVISE and their dispositions are in `SEMANTIC-DELTA.md` §Review).

Register row: P-68 in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`.

Behavior manifest: `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (this directory),
eleven rows, hashing the eleven PWB behavior artifacts **as they will be
after** the three behavior patches under `proposed/` are applied. Three
rows differ from the tree today; eight equal it.

Behavior manifest SHA-256:
`fc644d010ebfb02351e5e84d2c382d004f5e4f96884959dc407656cb66a0ac9b`

The package also carries one **contract** patch,
`proposed/contract/RFC-0007-rendering-and-surface.md.patch`, which is not a
manifest row: it amends the accepted clause RFC7-33 and can only bind by a
contract successor act of its own (see "Two acts, in order").

This packet wrapper is not an act subject. Its bytes are bound by the
retained review of the package; changing this packet after that review
retires the review.

## Why this is here

You ruled P-67 on 2026-09-13: trim the page first (lane A), then draft the
spec amendment (lane B) once lane A is measured. Lane A is measured and
reviewed: the Polaris page went from 2,132,656 to 1,478,637 bytes (direct)
and from 2,138,506 to 1,484,487 bytes (tailnet mount), which is inside the
2 MiB ceiling with about 612 KB of headroom but still 78,637 / 84,487 bytes
over the 1,400,000-byte working target you set. What remains per item is
the claim tuple and its citations, repeated on every claim even when every
claim in a table carries the same values. The current clauses forbid
stating those values once: PWB-REQ-007 in the spec, and the accepted
contract clause RFC7-33, which requires every distinction as an attribute
"on the rendered unit". This package is the amendment that would allow it,
with the parity and Unknown floors kept.

The first fresh-context review of this package found that the accepted
contract, not only the spec, forbids scoping (RFC7-33), and that scoping
the non-citability attribute would contradict RFC7-33's sub-clause
"Non-citability travels, on every rendering." Both findings are accepted:
the PWB-REQ-014 attributes stay on every unit and are **not** amended, and
the package now carries the RFC7-33 delta the spec change needs. A contract
change is an act escalation trigger, so the package cannot be offered for
sign-off in one act, and the decision below is about direction, not yet a
phrase.

## What the package changes

In the human page only:

- a tuple field whose value is identical, in the machine answer, for every
  claim under one scope may be stated once on that scope; where claims
  differ, each carries the field itself, evaluation identity included;
  Claim identity is never inherited; the machine answer never inherits
  (PWB-REQ-007);
- a scope states what it carries as text on its own element, before its
  claims, so a reader without vision meets each value once where a sighted
  reader does (PWB-REQ-016 is not amended; the delta shows how it holds);
- parity is judged after every oracle expands scopes with its own statement
  of the rule; a scope value that hides a differing member (`scope-hidden`)
  and a scope value some member does not have (`over-asserting-scope`) are
  new, named falsifier and mutant classes (PWB-REQ-020);
- RFC7-33 gains one permission paragraph for the interactive surface,
  excluding the `non-citable` / `presentation-artifact` distinctions, whose
  sub-clause stands in full (contract patch).

## What the package does not change

The machine answer carries every field on every claim, exactly as today.
No field is dropped in any channel; Unknown never folds; a scope never
carries a value some claim under it lacks; one tuple per rendered claim
still enters the parity multiset; PWB-REQ-014's attributes stay on every
unit; anchors, non-authority of Polaris, PWB-REQ-011/015/016/021/022 and
every warrant list are untouched. The full quoted current and proposed text
is in `SEMANTIC-DELTA.md`; the exact bytes are the patches under
`proposed/`.

## What it buys and what it costs

Estimated saving on the pre-lane-A capture: about 350 KB (roughly 50 KB
evaluation identity and 300 KB tuple fields; the 100 KB attribute share
the funnel counted is no longer in scope) [Inferred — the funnel estimate
minus its attribute share; the lane A page has not been measured with
scopes, and the number is confirmed only by the implementation bead's
measurement]. Applied to the lane A page that would land near 1,130,000
bytes, under the 1,400,000 target with room for the P-60/P-61 Butlers
repairs' 418–443 KB [Inferred]. Cost: the renderer, three oracles and the
mutation sweep change (listed in `IMPACT-LEDGER.md`); every human-page
reader of tuples must now apply the inheritance rule; and an RFC-0007
successor ceremony (recorder, manifest over both contract mirrors, history
entry, governance seam) has to be built first, because no RFC-0007
amendment has ever been performed and the existing seam is hard-coded to
RFC-0008/0009.

Risk you should weigh: a reader of the raw HTML who does not expand scopes
sees fewer tuple fields on a claim than the machine form carries. The rule
is stated once in the spec and the page's claim-states lede would restate
it; the oracles, not the reader, are the guarantee. A screen-reader user
hears each scoped value once, as the scope's own text before the claims it
covers, instead of on every claim; the accessibility checker and the
non-visual cold-open walkthrough PWB-REQ-016 already requires are what
confirm that after implementation.

## The decision

**Question:** which way should lane B go?

**(a) Proceed on the two-act path** (recommended). Build the RFC-0007
successor tooling in the shape of the 2026-09-05 no-signal ceremony; offer
the RFC7-33 contract successor for its own act; then offer this behavior
manifest for the PWB act. Nothing is implemented until both acts are
performed. On the 350 KB estimate holding, this is the only path that
meets the target you set without cutting items [Inferred: the estimate is
unmeasured on the lane A page; if the implementation bead measures
materially less, (a) does not reach the target either and the target
question returns to you].

**(b) Revise the target and close lane B.** The lane A page sits about
612 KB under the response ceiling, and the pending Butlers repairs add at
most 443 KB, so a working target of the ceiling minus that margin holds
without any spec or contract change. Lane B is banner-marked declined and
the register row closes with the new target stated.

**(c) Decline.** The 1,400,000 target stands, the spec and RFC7-33 stand,
and the remainder is met some other way you name, or not met.

Silence, a partial answer, a commit or a merge performs nothing; the
2026-09-05 package stays the PWB authority and RFC7-33 stands as accepted
in every case until an act says otherwise.

## Not yet offered: the sign-off phrase

The behavior act phrase for this manifest would be:

```
SIGN OFF PWB SCOPED-ATTRIBUTES AMENDMENT: fc644d010ebfb02351e5e84d2c382d004f5e4f96884959dc407656cb66a0ac9b
```

It is registered so that the governance checks see it go stale, but it is
**not offered** in this packet: the RFC7-33 contract successor has to be
performed first, and a second fresh-context review has to confirm the
repaired package. If you reply with this phrase now, no recorder exists
that would accept it, and nothing is performed.

## Two acts, in order (what happens after a "yes" to (a))

1. **Contract successor.** A dedicated recorder is built for RFC-0007 in the
   no-signal shape (subject = the module bytes after the contract patch, the
   same bytes in `contracts/rfcs/` and the candidate mirror; a history
   entry; a successor manifest; the governance seam extended from its
   RFC-0008/0009 hard-coding). Its packet offers one phrase binding those
   bytes. Only its act changes RFC7-33.
2. **Behavior amendment.** A dedicated recorder (the 2026-09-05 shape)
   verifies the phrase above against the manifest bytes, applies the three
   behavior patches into `openspec/` with the builder's
   `--apply --at-adoption`, confirms every manifest row now hashes the
   tree, writes the dedicated act record and the aggregate section of
   `ACCEPTANCE-ACT-RECORD.md`, and registers the third chain link, in one
   change.

Only then is an implementation bead opened under the pursuit epic; its
measurement in the lane A shape is what confirms or refutes the estimate
above. If the contract act is performed and the behavior act declined, the
RFC7-33 permission stands unused and the spec still forbids scoping;
nothing renders differently. Nothing is implemented before both acts.
