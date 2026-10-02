# Owner decision packet — PWB page-level evaluation stamp (lane B, narrowed)

> **DECLINED 2026-10-02.** The owner declined lane B (`decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`). This package is not offered for sign-off, was never applied, and is kept as the record. The text below is the offering as drafted.


> **Inert offering.** This packet performs nothing. It presents one decision,
> records nothing, and authorizes no implementation. A commit, a merged pull
> request, a review, a manifest, silence or a general "approved" performs no
> act.

Date: 2026-10-02. Narrowed from the broader lane B draft under your
2026-10-02 direction. No fresh review has read these bytes yet.

Register row: P-68 in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`.

Behavior manifest: `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (this directory),
eleven rows, hashing the eleven PWB behavior artifacts **as they will be
after** the three behavior patches under `proposed/` are applied. Three rows
differ from the tree today; eight equal it.

Behavior manifest SHA-256:
`68f3eca4624a0a74add9f315e1c682d9a074c3d2da68aa7b2f63c10a93e8cffc`

The package also carries one **contract** patch,
`proposed/contract/RFC-0007-rendering-and-surface.md.patch`, which is not a
manifest row: it amends the accepted clause RFC7-33 and binds through its own
package, `contracts/candidates/rfc7-scoped-values-successor/`.

This packet wrapper is not an act subject. Changing it after a review of the
package retires that review.

## Why this is here

You ruled P-67 on 2026-09-13: trim the page first (lane A), then draft the
spec amendment (lane B). Lane A is measured: the Polaris page went from
2,132,656 to 1,478,637 bytes (direct) and from 2,138,506 to 1,484,487 bytes
(tailnet mount), inside the 2 MiB ceiling and still 78,637 / 84,487 bytes over
the 1,400,000-byte working target you set [Observed,
`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`].

The first lane B draft let any tuple field shared by a table's claims be
stated once. Three fresh reviews of its contract paragraph each found the same
conflict: a claim reached apart from its scope loses the Unknown, draft, stale
or review distinction RFC7-33 requires on the unit. You chose on 2026-10-02 to
narrow lane B to page-invariant values.

## What the package changes

PWB-REQ-007 lets the **evaluation identity** be stated once on a page-level
scope instead of on each of the page's claim tuples, with the rule that the
scope is emitted only when every claim has that identity in the machine
answer, states the value as text on its own element, and overrides nothing.
PWB-REQ-020's parity comparison expands the stamp with its own statement of
the rule, and gains the `stamp-hidden` mutant class. RFC7-33 gains one
paragraph permitting exactly this on the interactive surface (the HTML document
served for a browser) and excluding every epistemic field and the
`non-citable` / `presentation-artifact` pair. The endpoints, exports and any
copy or share function carry the evaluation identity on every claim.

## What the package does not change

- Label, tier, reason, freshness, challenge, review, draft and adoption state
  and Unknown stay on every claim, on every rendering.
- **The two presentation flags are not scoped.** They are the
  `non-citable` / `presentation-artifact` pair, and RFC7-33's sub-clause
  requires them on every unit. Your direction named them with the evaluation
  identity; the package holds them per unit and says so here so you can
  overrule it.
- The machine answer, claim identity and the Unknown reason's route.
- No implementation, read, route, egress or consent is authorized.

## What it buys and what it costs

**The saving is about 50 KB, not the earlier 190 KB** [Inferred]. The funnel
measured 699 `data-evaluation-id` attributes at 49,629 bytes, about 71 bytes
each; the lane A record counts 713 tuples; one stamp costs about 100 bytes.
Stating the identity once removes about 50 KB from the 1,478,637-byte direct
page and from the 1,484,487-byte tailnet page, leaving roughly 1,428,000 and
1,434,000 bytes. **That is still about 28 KB and 34 KB over the 1,400,000-byte
target.** The figure is arithmetic over retained records, not a measurement:
the capture the earlier estimator read is not retained in the repository, so
`scripts/estimate_pwb_scoped_attributes_saving.py` could not be re-run, and no
page has been rendered with a stamp.

The cost is one new rendering rule that three oracles restate (Polaris parity,
the accessibility checker, the shared model's tests) and a contract paragraph
reviewers will read closely. A claim reached apart from the page still names
its evaluation, because the machine answer and every export carry it per claim
and a hand copy of the page carries the stamp's text only if the reader copies
it; the evaluation identity is not a claim's epistemic state, so no
VIS-1/VIS-2 distinction rides on it.

## The decision

**Does the narrowed package realize your 2026-10-02 direction, and should it
go to review and then sign-off?**

**(a) Yes, as drafted.** A fresh-context review reads the bytes. Sign-off is
version-tagged under your 2026-10-02 Scope A direction: the contract successor
first, then this amendment, each by your selection of an option, with no typed
phrase.

**(b) Yes, with named changes.** Name them (for example, scope the
`non-citable` / `presentation-artifact` pair after all, which needs an RFC7-33
sub-clause amendment) and the package is redrafted and reviewed again.

**(c) The target question.** If a saving of about 50 KB is not worth a spec
and contract change, revise the 1,400,000-byte target (the page sits about
612 KB under the response ceiling) and close lane B. This returns to you
whatever you choose in (a), because the page does not reach the target on this
saving alone.

Silence, a partial answer, a commit or a merge performs nothing. The
2026-09-05 package and the current RFC7-33 stand until a sign-off says
otherwise.

## Not yet offered: the sign-off phrase

The behavior act phrase for this manifest would be:

```
SIGN OFF PWB SCOPED-ATTRIBUTES AMENDMENT: 68f3eca4624a0a74add9f315e1c682d9a074c3d2da68aa7b2f63c10a93e8cffc
```

It is registered so that the governance checks see it go stale. It is **not
offered**: no review has read these bytes, and the package is signed through
the version-tagged mechanism, not by this phrase.

## Order

1. The contract successor package amends RFC7-33.
2. This behavior amendment applies the three patches.
3. Only then may an implementation bead open, under its own authorization; its
   measurement of the real page confirms or refutes the estimate above.
