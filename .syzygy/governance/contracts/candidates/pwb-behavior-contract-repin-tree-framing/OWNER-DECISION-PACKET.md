# Owner decision packet — PWB behaviour-contract re-pin to the tree-framing sign-off

> **Review status, 2026-10-03.** Round 1 returned `REVISE`
> (`docs/reviews/R-PWB-BEHAVIOR-CONTRACT-REPIN-TREE-FRAMING-RAW.md`): one
> revise finding and six notes. All seven were repaired once in this
> package's prose and builder selftest (`ROUND-1-DISPOSITIONS.md`); the
> patches and the manifest, and so both act arguments, did not change.
> Under the stopping rule set for this bead no second round was
> dispatched, so the repaired bytes carry **no confirmation**. The owner
> decides whether to take them as they stand or to order a round 2 first.
> The banner below is the one the package was drafted with.

> **Candidate — binds nothing.** Drafted 2026-10-03 for bead `syzygy-2g0d`.
> Effect would come from two separate superseding owner acts and one plain
> continuation direction, and from nothing else. Silence, a commit, a
> review, a merged pull request or a passing check performs no act. No
> review has been run against these bytes, so nothing here is offered yet.
> The package is offered only after a fresh-context round returns CONFIRM,
> or CONFIRM WITH EXCEPTIONS with notes only (the 2026-09-26 sitting
> ruling).

## What this is, in one paragraph

The observer registry entry and the secret-classification policy each
declare which PWB specification governs them. On 2026-10-02 the owner
re-pinned both to the `spec.md` signed as `pwb-readability-successor-v1.0`
(`contracts/candidates/pwb-behavior-contract-repin/`). On 2026-10-03 the
version-tagged sign-off `pwb-tree-framing-amendment-v1.0` moved `spec.md`
again, so both declarations are false once more and
`scripts/check_spec_reconciliation.py` R6 reports them as Unknown. This
package re-points both declarations to the current `spec.md`, the one
signed as `pwb-tree-framing-amendment-v1.0`, and names that sign-off. It
changes nothing else in either file. `SEMANTIC-DELTA.md` quotes the
change, `IMPACT-LEDGER.md` lists what depends on it, and `REVIEW-BRIEF.md`
sets the review.

## The three things the owner would be asked for

| # | Kind | What it does |
|---|---|---|
| A | `approve-policy` act, state (1) | Approves the re-pinned policy at its own SHA-256, superseding the 2026-10-02 policy re-pin act for the policy role only |
| B | `adopt-registry-entry` act, state (1) | Adopts the re-pinned registry entry at its own SHA-256, superseding the 2026-10-02 registry re-pin act for the registry role only |
| C | Plain continuation direction | Re-points the body-read gate to the acts of A and B, so Butlers reads continue (see "Read gate") |

A and B are independent: neither binds the other. The phrase forms are
unchanged from the acts they supersede:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: <argument>
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: <argument>
```

Each argument is the SHA-256 of that artifact's proposed bytes, which is
that subject's row of this package's `PWB-EFFECT-REPIN-MANIFEST.txt`. By
design no argument appears in any Markdown file of this package: the
builder derives it from the patch, and the recorder re-derives it at the
act. When this is offered, the argument is read from the manifest row at
the reviewed commit.

**Recommendation: give A, B and C in one sitting.** Each act alone stops
every Butlers read until C is given, and the act-recording change cannot
pass its own tests until C's re-point lands with it.

## Signing path

Unchanged from the 2026-10-02 re-pin, for the same reasons.

**Policy: a digest act.** The Scope A direction
(`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
item 1) covers "the PWB specification deltas, the observer registry entry
and the contract successors queued behind them". A secret-classification
policy is none of these, so the policy keeps its phrase-and-digest act and
a dedicated recorder.

**Registry entry: offered as a digest act too, though Scope A covers it.**
The body-read gate honors the registry entry only through an owner-act
record bound to the artifact's exact digest.
`body-read-authority.ts` implements RFC3-16(a) and RFC3-16(b) item 3, and
accepted RFC 0003 `governance-homes-and-owner-acts.md` says "Such an
artifact is honored only through an **effective owner act**", and defines
that act as one "bound to the artifact's exact digest under RFC3-16(b)". RFC3-16(b)
item 3 asks for "the **exact content or revision digest** of the artifact
as acted on". A version-tagged sign-off record carries no digest of the
artifact. [Inferred] If the registry were signed by tag, no lawful
re-point would exist: the gate would stay closed until the owner decided
whether a tag on a commit is a "revision digest" under item 3, and the
implementation learned to read such a record.

The Scope A direction's "What this does not do" section says: "The
replacement mechanism and the removal of the digest machinery for the
covered artifacts travel as one governed change after this record. Until
that change lands, the existing phrase-and-digest acts remain the only way
to perform the queued packages." [Observed] Part of that change has
landed: commit `842b624f` (2026-10-02) added
`scripts/record_versioned_signoff.py`, which recorded the very sign-off
this package pins to. [Observed] The part the registry would need has not:
the gate still evaluates the registry role only from an exact-digest act
record. So the tag path is open in principle, as the next paragraph says,
but not yet evaluable by the gate. Keeping the registry on the digest path
keeps all three PWB-REQ-005 authorities in one evaluable form, and makes
direction C a pointer change only.

The Scope A path stays open to the owner: say "sign the registry entry by
version tag instead", and B becomes a version-tagged sign-off of this
package. The cost is that the gate stays closed after it until a separate
contract-reading decision and an implementation change.

## Read gate — what happens, and direction C

[Observed] Today the gate (`apps/three-surface-poc/src/governance-inputs.ts`)
evaluates the policy role against
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
and the registry role against
`decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`.

**After act A or act B, every Butlers body read is refused until direction
C is given and implemented.** That role's evaluation is **invalid**,
because the record it reads binds a digest the artifact no longer hashes
to (`exact-digest-wrong`), and the new record supersedes it. PWB-REQ-005
needs all three authorities, so the gate **admits nothing** and Polaris
renders the shape Unknown. Consent is unaffected. Nothing reads a body in
the meantime, so this fails closed and does not leak.

Direction C, in the shape of the 2026-10-02 re-point
(`decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`),
would be put as:

> Adopting the re-pinned registry entry and policy makes the Butlers read
> gate fail closed, because it still expects the 2026-10-02 re-pin acts.
> Do you direct the implementation to evaluate the two new acts instead?
> This covers only the act pointers, act identities, recording tags,
> supersession targets and tests. No new field is consumed.

- **Permitted:** for the policy and registry roles, the body-read
  expectations name the new act records, act identities and recording
  tags. The records they supersede become the expected supersession
  targets: `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
  and `PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`. Tests change
  to match.
- **Unchanged:** the version anchors (`1.2.0-candidate.1`,
  `1.1.0-candidate.1`), consent, content class, configured repository,
  every exclusion of the acts in force, and the 2026-09-30 direction's bar
  on reading the currency and briefing fields.
- **Not permitted:** consuming `governingBehaviorContract` or any other
  field the implementation does not read today. [Observed] No code under
  `packages/` or `apps/` reads it.

## What the acts would not do

They grant no observation consent. They authorize no write, egress,
execution, deployment, release, recovery, mission, second-repository,
autonomous or multi-user effect, and widen no consent. They edit no
performed record, change no version label, and prove no read, screening,
parse or render result.

## At adoption — the change that records A and B

1. A recorder is written after the confirming review, as
   `record_pwb_behavior_contract_repin_acts.py` was. It is not in this
   package, because it pins the frozen package commit, the packet head and
   the confirming raw. Per act it validates the owner's argument against
   the manifest row and the builder's proposed bytes. It requires the
   subject to hash to the act in force, and it binds the raw by its head
   (`REVIEW-BRIEF.md`, "Recording"). It then applies
   `build_pwb_behavior_contract_repin_tree_framing.py --apply <subject>
   --at-adoption` and writes the dedicated record and one
   `ACCEPTANCE-ACT-RECORD.md` section. Records:
   `PWB-SECRET-CLASSIFICATION-POLICY-TREE-FRAMING-REPIN-ACT.md` and
   `PWB-OBSERVER-REGISTRY-TREE-FRAMING-REPIN-ACT.md`. Act identities:
   `PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-TREE-FRAMING-REPIN-<date>`
   and `PWB-OBSERVER-REGISTRY-ENTRY-TREE-FRAMING-REPIN-<date>`. Tags:
   `pwb-approve-policy-signed-<date>` and
   `pwb-adopt-registry-entry-signed-<date>`; a date already carrying either
   tag needs a distinct suffix.
2. `check_governance.py`: two `PWB_EFFECT_AMENDMENT_ACTS` chain rows
   (each from its 2026-10-02 re-pin record), `PWB_EFFECT_AMENDMENT_OFFERINGS`
   entries naming the 2026-10-02 manifest as the row that offered those
   records, the existence-gated `ACT_DIGEST_COPY_FILES` registration of
   this package's manifest in place of the 2026-10-02 one, `PROJECT-STATUS.md`
   and the aggregate as copies of the new arguments, and the two new
   records' effect-manifest heading exemptions. The rehearsal in
   `IMPACT-LEDGER.md` shows 11 CG-7e findings until this lands.
3. The 2026-10-02 package's builder and recorder, and the 2026-09-30
   registry builder and recorder, learn the later superseding act (they
   read their act's bytes by reversing this package's patch first), or
   leave the battery as superseded recorders do.
   `check_spec_reconciliation.py`'s `pins-after-repin-acts` case depends on
   the first of these.
4. Direction C's implementation re-point, with its tests.
5. `scripts/check_spec_reconciliation.py --check`: R6 reports 0 findings.
   Its selftest case `pins-after-tree-framing-repin-acts` already requires
   this of the proposed bytes.
6. The battery, the hosted workflow and the CG-26 count sentence, changed
   together in one integration edit. This draft leaves all three alone.

**If another PWB `spec.md` change is signed before A and B,** the builder
refuses this package as stale ("is not the current" `spec.md`). It must
then be redrafted over that sign-off, with new patches and a new manifest,
and re-reviewed. A `--write` alone would not move the pin.

## Open questions for the owner

1. **Registry path.** Digest act, as drafted, or version tag (see "Signing
   path")? Drafted: digest act.
2. **Version labels.** As drafted, both labels stay where they are. A bump
   to, say, `1.2.1-candidate.1` and `1.1.1-candidate.1` would change both
   arguments, the gate's scope anchors and its `policyVersion`
   expectation (`governance-inputs.ts`), the core constants
   `policyVersion` in `git-object-reader.ts` and `observerVersion` in
   `project-shape-observation.ts`, two tests that read `policyVersion`
   from the file, and the hard-coded labels in four test files (`git grep
   -l -F` for either label over the `*.test.ts` files under `packages/`
   and `apps/`). Direction C would then have to cover all of these, not only
   the anchors. Drafted: no bump.
3. **The pin will go stale again.** This is the second re-pin in two days,
   and the 2026-10-02 packet predicted it. Every PWB outcome that moves
   `spec.md` reopens R6 for both artifacts and costs two acts, a direction
   and a gate re-point. A structural change is possible, for example
   pinning a signed package lineage rather than one digest, or folding the
   pin into each PWB sign-off. Either would change what the artifacts
   declare and how the gate is evaluated, so it needs its own drafted
   package. Drafted: none, disclosed; the owner may ask for one.
