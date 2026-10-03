# Impact ledger — PWB anchor-resolution amendment (N9, PWB half)

> **Candidate — binds nothing.** This ledger names what the amendment would
> touch if signed and then authorized. It changes nothing itself.

## Predicate and population

- **Governed subjects.** The eleven PWB behavior artifacts the manifest
  names. Two are patched (`spec.md`, `GOVERNING-DEPENDENCIES.md`); nine are
  byte-identical, and `--check` fails if that stops being true.
- **Implementation files.** [Observed] At `71b4f525`, the tracked files under
  `apps/` and `packages/` (excluding the Polaris generation tree, which this
  bead does not touch) that contain the literal `citable` number 18. The ones
  that build or test the machine narrative are listed below; the others
  render the `non-citable` attribute, which does not change.

## Files a later implementation would touch

Nothing here is authorized. After a sign-off and a fresh implementation
authorization:

- `apps/three-surface-poc/src/polaris-narrative.ts`: compute each anchored
  block's pair and the narrative's pair against the machine answer, keeping
  `citable: false`.
- `apps/three-surface-poc/src/routes.ts`, which serves `/api/poc/polaris`:
  only if the narrative's pair is served on the envelope rather than on the
  narrative object. [Unknown] Which object carries it is an implementation
  choice the spec leaves open.
- A new or extended test beside `polaris-narrative.test.ts`: an independent
  resolver that imports no rendering code, reads only the machine answer's
  bytes and reproduces every pair; plus the rule-6 mutants the oracle names
  (a withheld target identity, a rounded pair, a citable flag set from the
  pair).
- `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`: unchanged in
  intent. It should keep passing, since no unit becomes citable.

[Observed] At this capture the pair would read 883 of 902 for the narrative.
The 19 unresolved anchors name targets the machine answer serves nowhere as a
whole value; [Inferred] each is composed from served fields
(`SEMANTIC-DELTA.md`, evidence). Serving those records with an `identity` of
their own is not part of this delta; until something does, the count stays
below its total and is served that way.

## Packages and fields this collides with

- **`pwb-class-granular-extraction-amendment`** and
  **`pwb-release-label-amendment`** (both pending). Neither touches
  PWB-REQ-014. [Observed] `--check` applies this spec patch with each of
  theirs in both orders and gets identical bytes with valid warrants. Each
  rewrites `GOVERNING-DEPENDENCIES.md`'s `Source:` line, so the later-signed
  package regenerates that patch with `--write`. Both builders now list this
  package as a pending sibling (a one-entry change each), or their own
  `--check` would fail on an unclassified sibling.
- **`three-surface-poc-block-provenance-amendment`** (pending, the POC half
  of N9). Different specification, no shared subject. The two region anchors
  among the 19 unresolved ones target the two block headers that package
  reshapes. [Inferred] If a later change gives those provenance records a
  served identity, those two anchors could resolve; neither package requires
  it.

## At adoption — what the sign-off change must carry

[Observed] by applying the patches in a scratch tree at `71b4f525`:

1. `python3 scripts/build_pwb_anchor_resolution_amendment.py --apply
   --at-adoption`.
2. `scripts/check_spec_reconciliation.py`: PWB-REQ-014's literal scenario
   count moves from 8 to 9 and the PWB total from 51 to 52 (more if a
   sibling lands first); register this package as a successor under the
   `pwb` child, as the tree-framing sign-off was; regenerate `census.json`.
3. `scripts/record_versioned_signoff.py`: add the package to
   `real_packages()`, which lists each signable PWB package by name.
4. `scripts/check_governance.py` CG-7h: register the sign-off as the newest
   link of the PWB successor chain. [Observed] Without it, CG-7h reports 37
   findings, all cascading from the tree-framing manifest's two rows no
   longer matching the spec and its dependency declaration.
5. The class-granular and release-label builders' sibling lists: move this
   package from pending to performed, naming its sign-off record.
6. The register row P-96 closes, and `PROJECT-STATUS.md`'s open-gate row
   goes.

**The behaviour-contract pins.** [Observed] The observer registry entry and
the secret-classification policy each pin a PWB `spec.md` digest
(`governingBehaviorContract`). The reconciliation checker's R6 reports a pin
that differs from the current spec as Unknown, report-only. The pins are
already stale today, behind the tree-framing sign-off, and the pending re-pin
package `pwb-behavior-contract-repin-tree-framing` (P-95) would re-point them
to today's spec. Signing this package moves the spec again, so:

- if this package is signed first, that re-pin package's builder refuses it
  as stale, and it must be redrafted over this sign-off and re-reviewed;
- if the re-pin acts are performed first, signing this package makes both
  pins stale again, and a further re-pin needs its own owner acts.

[Observed] The body-read gate does not read the pin
(`apps/three-surface-poc/src/governance-inputs.ts`, comment above
`PWB_ACT_RECORDS`), so neither order refuses a Butlers read. The cost is a
pin that reads Unknown until the next re-pin.

## Registry entry and policy

None. The amendment reads nothing new from Butlers, adds no route, and moves
no ceiling. The machine narrative grows by one small pair per anchored block
and one for the narrative. [Inferred] At 697 blocks that is about 30 KB
uncompressed, well inside the derived view's machine-JSON ceiling; the
implementation slice measures it.
