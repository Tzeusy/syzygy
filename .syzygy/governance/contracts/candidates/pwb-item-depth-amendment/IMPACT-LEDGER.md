> **Candidate — binds nothing.** This ledger describes proposed impact. It
> performs no act and authorizes no implementation.

# Impact ledger — PWB item depth

Baseline: `66114ac771872898cb9f90c3129076b10ee8f64b`, the clean worktree head
assigned to `syzygy-dov.14.2` on 2026-09-27.

## Discovery method

[Observed] Two methods ran over all **1,542** paths returned by
`git ls-files -z`: **1,538** decoded as UTF-8 and four PNG evidence files were
binary remainders.

1. Python `re` searched decoded files for `PWB-REQ-015\b`, then separately
   parsed continuation and run forms beginning `PWB-REQ-` with slash, comma or
   `..` separators and selected forms whose numeric population contains 015.
2. `git grep -l -F PWB-REQ-015 HEAD --` independently reproduced the **45**
   full-form files.

The continuation/run predicate adds **12** decoded files with no full literal,
for a union of **57** citing files at the baseline. The four binary remainders
were separately enumerated; the fixed-string search reports no match in them.
This package's new files are outside the baseline figure and must not be folded
back into it after drafting.

## Signed subjects

| Subject | Proposed disposition |
|---|---|
| `specs/polaris-project-wide-butlers-model/spec.md` | PWB-REQ-015 amended in place |
| `design.md` | project/capability-detail argument generalized to item detail |
| `CAPABILITY-COVERAGE.md` | row 18 restated for the amended obligation |
| `CONTRACT-COVERAGE-REPAIR-DELTA.md` | RFC7-13 and RFC7-17 coverage consequences restated |
| `GOVERNING-DEPENDENCIES.md` | regenerated source digest only; warrants remain 17 requirements / 96 authorities |
| Remaining six manifest rows | proposed digest equals current bytes |

The package keeps one eleven-row manifest because the 2026-09-05 act made the
behavior population indivisible. Proposed patches never edit current signed
bytes.

## Reached authority

- **PWB-REQ-011 — reached, unchanged.** Its progressive path already starts
  from every catalog category and follows a declared item through each
  available depth. The proposed detail adds an available depth without changing
  its exact-source authority or gates. The separate `.30` package explicitly
  leaves PWB-REQ-015 downstream.
- **PWB-REQ-014 — reached, unchanged.** Item claim identity remains semantic;
  URL, label, path and coordinate remain non-identities. Narrative stays
  non-citable presentation.
- **PWB-REQ-016 — reached, unchanged.** The item-detail path remains textually
  recoverable and keyboard operable; later implementation owes its browser and
  nonvisual sweep.
- **PWB-REQ-020 — reached, unchanged.** The proposal requires the same item
  identity, epistemic tuple and band/proposal distinctions in both channels.
- **RFC7-12…19/26/27/29/33/34 — reached, unchanged.** The amendment applies
  their existing exactness, band, emptiness, proposal, typed-authority, parity
  and operability rules to the complete declared item population. It mints no
  fourth band class or contract exception.

## Candidate and PR overlap

[Observed] Five tracked sibling candidates at the baseline patch the same PWB
`spec.md`: scoped attributes, exact-source render mode, machine views, opening
band and missing-currency disclosure. The builder discovers this population
from patch targets and composes this package before and after each sibling on
every `--check`; all five pairs currently produce identical bytes.

[Observed] Open PR #121 adds the dismissal-expiry PWB-REQ-007 candidate and
PR #124 adds the container-shape PWB-REQ-002 candidate. They are not baseline
files and therefore cannot be permanent builder inputs. Before review, fetch
their current patches and repeat the same two-order composition check.

The owner direction in
`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` fixes
`.21 → .30 → .22 → lane B`; it does not place this package. This candidate
creates no successor-chain link. The owner selects its position before any act
offer, and the package regenerates against the actual predecessor.

Every sibling also rewrites `GOVERNING-DEPENDENCIES.md`'s generated source
digest. Those patches are expected not to compose. Whichever package follows
another regenerates that file and its manifest; this is derived-byte collision,
not semantic precedence.

## Future implementation consumers — unchanged here

| Surface | Later consequence after an act and fresh authorization |
|---|---|
| `packages/three-surface-poc-core/src/project-shape-model.ts` | carry declared item-to-intent relations without inference |
| `apps/three-surface-poc/src/capability-detail.ts` | generalize the one capability derivation to item details and honest absence |
| `apps/three-surface-poc/src/polaris.ts` | link every declared catalog item and render its three bands |
| `apps/three-surface-poc/src/routes.ts`, `surface-links.ts` | locate detail by stable item identity without making URL identity |
| presentation/parity/reachability/accessibility tests | enumerate the full item denominator and both channels |
| response-ceiling measurement | measure direct and tailnet forms before any fan-out ships |

There is no runtime state, retry, replay, cache or concurrency effect in this
candidate. Later implementation must use one shared model/evaluation and must
not read any new body merely to create item detail.

## Failure and regeneration boundary

`scripts/build_pwb_item_depth_amendment.py` fails closed when the patch target
set is not exactly the five subjects above, a patch no longer applies, the
manifest differs, generated dependencies drift, required semantics disappear,
the signed requirement was edited in place, or a sibling composition becomes
order-dependent. `--write` is deterministic over identical inputs; `--check`
is read-only. `--apply` refuses without `--at-adoption` and belongs only inside
a future dedicated owner-act recorder.

Per the repository's CG-26 integration rule, this draft does not independently
edit the coupled PROJECT-STATUS battery, hosted workflow or count sentence.
Those lines are batched once when candidate builders are integrated.
