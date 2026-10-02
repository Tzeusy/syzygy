> **DECLINED 2026-10-02.** The owner declined lane B (`decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`). This package is not offered for sign-off, was never applied, and is kept as the record. The text below is the offering as drafted.

> **Candidate — binds nothing.** This packet offers a contract amendment for
> the owner's decision. It performs no act, adopts nothing and authorizes no
> implementation. The change takes effect only through an owner act that
> names the manifest digest below in `ACCEPTANCE-ACT-RECORD.md`.

# Owner decision packet — RFC-0007 scoped-values amendment

Status: candidate, **not yet offered**. A fresh-context review has not
confirmed these bytes. Sign-off is version-tagged
(`scripts/record_versioned_signoff.py`, under the owner's 2026-10-02 Scope A
direction); the phrase below is registered only so the governance checks see
it go stale. If you reply with the phrase now, nothing is performed.

## What this decides

Step 1 of lane B's two-act path (`syzygy-dov.17`, your 2026-10-02 choice
"Proceed two-act"). RFC7-33 requires every distinction as a machine-readable
attribute on the rendered unit. The scoped-attributes behavior amendment
(`pwb-scoped-attributes-amendment/`) cannot be signed while RFC7-33 forbids
what it permits, so this contract change comes first.

## What the package changes

One accepted module, `rfcs/RFC-0007/rendering-and-surface.md`, gains:

- a parenthetical in RFC7-33's attribute sentence ("save the page-level
  evaluation stamp the paragraph below permits on the interactive surface");
- one paragraph, "Page-level evaluation stamp on the interactive surface": on
  the interactive surface only (the HTML document served for a browser), the
  evaluation identity RFC7-16 requires on every claim tuple MAY be stated once,
  as text on its own element and marked machine-readably as a scope. A scope
  is valid only if every claim under it would carry that same evaluation
  identity, never overrides a claim's own, and carries nothing else: no label,
  tier, reason, freshness, challenge, review, draft or adoption state, no
  Unknown, no claim identity and no `non-citable` / `presentation-artifact`.
  The machine-queryable endpoints, every plain-text or exported rendering and
  any copy, share or export function carry the evaluation identity on every
  claim.

## What it does not change

- Non-citability (`non-citable` / `presentation-artifact`) is excluded from
  the permission; its sub-clause stands in full.
- No clause identity, clause lead, front matter or heading moves; the builder
  verifies all three, and `verify_final_prespec.py`, CG-13 and CG-17 pass on
  the patched tree.
- No specification changes. The permission is unused until the behavior
  amendment is signed, and the spec still forbids scoping until then.
- No implementation is authorized.

## The decision

**Does this package, as drafted, realize the RFC7-33 permission lane B needs?**

**(a) Yes — as drafted.** Fresh-context review runs per `REVIEW-BRIEF.md`;
findings are repaired; the sign-off phrase is offered once a round confirms
the exact bytes.

**(b) Yes, with named changes.** Name the sentence you want different; the
package is redrafted and reviewed again, and the digest below is retired.

**(c) No.** The permission is declined; lane B's behavior amendment cannot
proceed and RFC7-33 stands as accepted.

Silence, a partial answer, a commit or a merge performs nothing.

## Not yet offered: the sign-off phrase

The contract act phrase for this manifest would be:

```
SIGN OFF RFC-0007 SCOPED-VALUES AMENDMENT: 338ce1dba36347fa8351e161b705c8d85b13825a385b28abaf422e35bcefeacd
```

It is registered so that the governance checks see it go stale; it is **not
offered** until a review confirms these bytes.

## Order and effect of the act

1. `scripts/record_rfc7_scoped_values_successor.py --record --phrase "<the
   phrase verbatim>"` verifies the pins and the package, writes the dedicated
   act record in the decisions directory and the aggregate section.
2. `scripts/build_rfc7_scoped_values_successor.py --apply --at-adoption`
   installs the patched bytes into `contracts/rfcs/` and the candidate
   mirror, in the same change that adds the link to
   `CONTRACT_SUCCESSOR_CHAIN` after the restyle link.

The behavior amendment is then a separate act, regenerated over the tree this
one leaves.
