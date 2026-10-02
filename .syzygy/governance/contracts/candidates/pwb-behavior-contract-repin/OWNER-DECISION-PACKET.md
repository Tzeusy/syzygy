# Owner decision packet — PWB behaviour-contract re-pin

> **Candidate — binds nothing.** Drafted 2026-10-02 for bead `syzygy-jloi`.
> Effect would come from two separate superseding owner acts and one plain
> continuation direction, and from nothing else. Silence, a commit, a
> review, a merged pull request or a passing check performs no act. No
> review has been run against these bytes, so nothing here is offered yet.
> The package is offered only after a fresh-context round returns CONFIRM,
> or CONFIRM WITH EXCEPTIONS with notes only (the 2026-09-26 sitting
> ruling).

## What this is, in one paragraph

The observer registry entry and the secret-classification policy each
declare which PWB specification governs them. Both still name the
2026-09-05 `spec.md` and say its act is pending. That act was performed,
and eight later PWB outcomes have moved `spec.md` since, so both
declarations are false. `scripts/check_spec_reconciliation.py` R6 reports
them as Unknown. This package re-points both declarations to the current
`spec.md`, the one signed as `pwb-readability-successor-v1.0`, and names
that sign-off. It changes nothing else in either file. `SEMANTIC-DELTA.md`
quotes the change, `IMPACT-LEDGER.md` lists what depends on it, and
`REVIEW-BRIEF.md` sets the review.

## The three things the owner would be asked for

| # | Kind | What it does |
|---|---|---|
| A | `approve-policy` act, state (1) | Approves the re-pinned policy at its own SHA-256, superseding the 2026-09-05 policy amendment act for the policy role only |
| B | `adopt-registry-entry` act, state (1) | Adopts the re-pinned registry entry at its own SHA-256, superseding the 2026-09-30 currency-and-briefing act for the registry role only |
| C | Plain continuation direction | Re-points the body-read gate to the acts of A and B, so Butlers reads continue (see "Read gate") |

A and B are independent: neither binds the other. The phrase forms are
unchanged from the acts they supersede:

```text
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: <argument>
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: <argument>
```

Each argument is the SHA-256 of that artifact's proposed bytes, which is
that subject's row of `PWB-EFFECT-REPIN-MANIFEST.txt`. By design no
argument appears in any Markdown file of this package: the builder derives
it from the patch, and the recorder re-derives it at the act. When this is
offered, the argument is read from the manifest row at the reviewed
commit.

**Recommendation: give A, B and C in one sitting.** Each act alone stops
every Butlers read until C is given, and the act-recording change cannot
pass its own tests until C's re-point lands with it.

## Signing path

**Policy: a digest act.** The Scope A direction
(`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
item 1) covers "the PWB specification deltas, the observer registry entry
and the contract successors queued behind them". A secret-classification
policy is none of these, so the policy keeps its phrase-and-digest act and
a dedicated recorder.

**Registry entry: offered as a digest act too, though Scope A covers it.**
The direction would let the registry entry be signed by a version tag. But
the body-read gate honors the registry entry only through an owner-act
record bound to the artifact's exact digest. `body-read-authority.ts`
implements RFC3-16(a) and RFC3-16(b) item 3, and accepted RFC 0003
`governance-homes-and-owner-acts.md` says "Such an artifact is honored
only through an **effective owner act**", and defines that act as one
"bound to the artifact's exact digest under RFC3-16(b)". A version-tagged sign-off record carries no
digest. [Inferred] If the registry were signed by tag, no lawful re-point
would exist: the gate would stay closed until the owner decided whether a
tag on a commit satisfies RFC3-16(b) item 3, and the implementation
learned to read such a record. Keeping the registry on the digest path
keeps all three PWB-REQ-005 authorities in one evaluable form, and makes
direction C a pointer change only.

The Scope A path stays open to the owner: say "sign the registry entry by
version tag instead", and B becomes a version-tagged sign-off of this
package. The cost is that the gate stays closed after it until a separate
contract-reading decision and an implementation change.

## Read gate — what happens, and direction C

[Observed] Today the gate (`apps/three-surface-poc/src/governance-inputs.ts`)
evaluates the policy role against
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` and the
registry role against
`decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`.

After act A or act B, that role's evaluation is **invalid**, because the
record it reads binds a digest the artifact no longer hashes to
(`exact-digest-wrong`), and the new record supersedes it. PWB-REQ-005
needs all three authorities, so the gate **admits nothing: every Butlers
body read is refused** and Polaris renders the shape Unknown. Consent is
unaffected. Nothing reads a body in the meantime, so this fails closed and
does not leak.

Direction C, in the shape of the 2026-09-30 re-point
(`decisions/OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md`),
would be put as:

> Adopting the re-pinned registry entry and policy makes the Butlers read
> gate fail closed, because it still expects the 2026-09-30 registry act
> and the 2026-09-05 policy act. Do you direct the implementation to
> evaluate the two new acts instead? This covers only the act pointers,
> act identities, recording tags, supersession targets and tests. No new
> field is consumed.

- **Permitted:** for the policy and registry roles, the body-read
  expectations name the new act records, act identities and recording
  tags. The records they supersede become the expected supersession
  targets: `PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` and
  `PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`. Tests change
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

1. A recorder, to be named record_pwb_behavior_contract_repin_acts.py, is
   written after the confirming review, as
   `record_pwb_registry_currency_amendment.py` was. It is not in this
   package, because it pins the frozen package commit, the packet head and
   the confirming raw. Per act it validates the owner's argument against
   the manifest row and the builder's proposed bytes. It requires the
   subject to hash to the act in force, and it binds the raw by its head
   (`REVIEW-BRIEF.md`, "Recording"). It then applies
   `build_pwb_behavior_contract_repin.py --apply <subject> --at-adoption`
   and writes the dedicated record and one `ACCEPTANCE-ACT-RECORD.md`
   section. Records:
   `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md` and
   `PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`. Act identities:
   `PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-BEHAVIOR-CONTRACT-REPIN-<date>`
   and `PWB-OBSERVER-REGISTRY-ENTRY-BEHAVIOR-CONTRACT-REPIN-<date>`. Tags:
   `pwb-approve-policy-signed-<date>` and
   `pwb-adopt-registry-entry-signed-<date>`.
2. `check_governance.py`: two `PWB_EFFECT_AMENDMENT_ACTS` chain rows
   (policy from the 2026-09-05 amendment record, registry from the
   2026-09-30 record), their `PWB_EFFECT_AMENDMENT_OFFERINGS` entries, and
   the existence-gated `ACT_DIGEST_COPY_FILES` registration of this
   package's manifest.
3. `build_pwb_truth_policy_amendment.py`: a `SUPERSEDED_ROWS` entry for
   the policy, gated on the new policy record.
   `build_pwb_registry_currency_briefing_amendment.py` and
   `record_pwb_registry_currency_amendment.py` learn the later superseding
   act, or leave the battery as superseded recorders do.
4. Direction C's implementation re-point, with its tests.
5. `scripts/check_spec_reconciliation.py --check`: R6 reports 0 findings.
   Its selftest case `pins-after-repin-acts` already requires this of the
   proposed bytes.
6. The battery, the hosted workflow and the CG-26 count sentence, changed
   together in one integration edit. This draft leaves all three alone.

## Open questions for the owner

1. **Registry path.** Digest act, as drafted, or version tag (see "Signing
   path")? Drafted: digest act.
2. **Version labels.** As drafted, both labels stay where they are. A bump
   to, say, `1.2.1-candidate.1` and `1.1.1-candidate.1` would change both
   arguments, the gate's scope anchors and two tests that read
   `policyVersion` from the file. Direction C would then also cover the
   anchors. Drafted: no bump.
3. **Later spec movement.** The pin names one `spec.md`. The next PWB
   outcome that moves `spec.md` makes R6 report both pins again, and each
   repair needs these two acts again. Folding the registry and policy into
   the PWB versioned package was not attempted here, since it would change
   the gate's evaluation model. Drafted: none, disclosed.
