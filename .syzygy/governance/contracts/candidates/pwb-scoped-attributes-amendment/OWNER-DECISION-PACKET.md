# Owner decision packet — PWB scoped epistemic attributes (lane B)

> **Inert offering.** This packet performs nothing. It presents one decision,
> records nothing, and authorizes no implementation. A commit, a merged pull
> request, a review, a manifest, silence or a general "approved" performs no
> act.

Date: 2026-09-14

Register row: P-68 in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`.

Behavior manifest: `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (this directory),
eleven rows, hashing the eleven PWB behavior artifacts **as they will be
after** `proposed/*.patch` is applied. Three rows differ from the tree
today; eight equal it.

Behavior manifest SHA-256:
`6d9c81b7b399d069d124b6e620776283681bd926875db9d5d0ad4037de33a5a6`

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
stating those values once. This package is the amendment that would allow
it, with the parity and Unknown floors kept.

## What a "yes" changes

In the human page only:

- a tuple field whose value is identical for every claim under one scope
  may be stated once on that scope; a claim whose value differs carries the
  field itself; Claim identity is never inherited (PWB-REQ-007);
- the two non-authority attributes may be stated once per scope; the claim
  role stays on every unit (PWB-REQ-014);
- parity is judged after every oracle expands scopes with its own statement
  of the rule, and a scope value that hides a differing member is a new,
  named falsifier and mutant class (PWB-REQ-020);
- a page that would carry two distinct evaluation identities fails to
  render instead of hoisting either.

## What a "yes" does not change

The machine answer carries every field on every claim, exactly as today.
No field is dropped in any channel; Unknown never folds; one tuple per
rendered claim still enters the parity multiset; anchors, non-authority of
Polaris, PWB-REQ-011/015/016/021/022 and every warrant list are untouched.
The full quoted current and proposed text is in `SEMANTIC-DELTA.md`; the
exact bytes are `proposed/*.patch`.

## What a "yes" buys and what it costs

Estimated saving on the pre-lane-A capture: about 450 KB (roughly 50 KB
evaluation identity, 300 KB tuples, 100 KB attributes), which would put the
page well under the 1.4 MB target [Inferred — the funnel estimate; the
lane A page has not been measured with scopes, and the number is confirmed
only by the implementation bead's measurement]. Cost: the renderer, three
oracles and the mutation sweep change (listed in `IMPACT-LEDGER.md`), and
every human-page reader of tuples must now apply the inheritance rule.

Risk you should weigh: a reader of the raw HTML who does not expand scopes
sees fewer attributes on a claim than the machine form carries. The rule is
stated once in the spec and the page's claim-states lede would restate it;
the oracles, not the reader, are the guarantee.

## The decision

**Question:** should the eleven-artifact package described by the manifest
above become the PWB behavioral authority for this bounded one-repository
POC, superseding the 2026-09-05 package as the third link of the PWB
successor chain?

Recommended: **accept**. The alternative inside the current spec is to cut
items from the page, which the item-per-page contract (P-67 question 3)
rules out, or to leave the page 78–84 KB over the target you set.

To accept, reply with exactly:

```
SIGN OFF PWB SCOPED-ATTRIBUTES AMENDMENT: 6d9c81b7b399d069d124b6e620776283681bd926875db9d5d0ad4037de33a5a6
```

To decline, say so in any words; the 2026-09-05 package stays the authority
and this package is banner-marked declined, never deleted.

## What happens after a "yes"

A dedicated recorder (the 2026-09-05 shape) verifies the phrase against the
manifest bytes, applies `proposed/*.patch` into `openspec/` with the
builder's `--apply --at-adoption`, confirms every manifest row now hashes
the tree, writes the dedicated act record and the aggregate section of
`ACCEPTANCE-ACT-RECORD.md`, and registers the third chain link, in one
change. Only then is an implementation bead opened under the pursuit epic;
its measurement in the lane A shape is what confirms or refutes the
estimate above. Nothing is implemented before the act.
