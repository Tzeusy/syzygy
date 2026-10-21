# Owner direction — implementation of the P-108 vocabulary and epistemic-record amendment (2026-10-21)

Date: 2026-10-21 (the owner's answer, 11:58:47 UTC)

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-P108-IMPLEMENTATION-2026-10-21`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in
the family of `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`
and `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md` (this
directory).
- It binds no artifact digest.
- It adds no row to `ACCEPTANCE-ACT-RECORD.md`.
- It registers nothing in `scripts/check_governance.py`.
- It signs nothing and edits no signed byte.

Signing P-108 started no implementation: "each needs its own implementation
authorization" (`OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`, lines
55-57). This record is that authorization for the slices it names, and for
no others.

## The owner's words

[Observed: an owner decision questionnaire dated 2026-10-21, item
`p108-implementation`, answered through its token-gated local web form. The
actor and instants are those the form recorded in its local answers file. The
questionnaire and the answers file sit outside the repository, are local
only, and are never authority; this record quotes what it needs.]

- Actor/channel: owner via questionnaire web form (token-gated, from
  127.0.0.1).
- Answer recorded at: 2026-10-21T11:58:47+00:00. The form was completed at
  2026-10-21T11:59:38+00:00 with the owner's explicit instruction to apply
  the answers now.
- Questionnaire digest: the SHA-256 of the packet as ingested is
  `19b0fd4d7694569697eaa3f5af2e5e28df0d8b7f39513a0e3cb52d9bd593d1ae`. The
  packet's bytes changed between serving and ingest (the ingest adds each
  item's owner-decision record), so no digest is quoted for the served copy.
- Owner edits: none. Post-answer review: none required, a plain selection of
  a presented option.
- Independent review of the item before it was offered: reviewer
  `rev-p108-k7q2m9`, round 2, "Scope verdict: Pass" and "Recommendation
  verdict: Pass" (the item's own adversarial-review record).

The question as put:

> Authorize implementation of P-108 v1.0 (POC-REQ-055 and the POC-REQ-060
> amendment)?

Its "Decision needed":

> Authorize, or hold, implementation of the signed text of
> `three-surface-poc-vocabulary-epistemic-amendment-v1.0` through M9 slices
> 4a, 4b and 8.

The owner selected **A**, whose full option text was:

> A. Authorize 4a, 4b and 8 as signed, on the 2026-10-15 direction's terms.
> Add one lane acceptance condition: the declared marker set includes the
> existing per-row id markers (`data-entity-id`, `data-relationship-id`); a
> test on a fixed fixture asserts each counted marker population equals a
> hard-coded non-zero number; a mutant deleting every marker must fail that
> test

The item's authorization boundary, as the owner answered over it:

> The owner selected this decision scope: implementation of P-108 v1.0's
> signed text through the chosen slices only, on the bounds of
> `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`, plus the
> chosen option's acceptance condition. The answer is recorded by the lead in
> a direction record beside the `sin5` record and placed in the one-at-a-time
> chain after the rows already authorized, under that record's rule that a
> link whose own gate is still open yields the slot to the next link that can
> start. Bead `syzygy-dov.9.2` is split, so 5, 6b and 7 stay blocked and
> `syzygy-dov.10.5` stays blocked behind them. This packet releases no
> artifact mutation or live/external action; the canonical destination
> workflow must obtain and enforce every separate authorization it requires.

The item's explicit exclusions, copied verbatim:

> - slices 5, 6b and 7;
> - a production Inferred constructor (any constructor stays test-only, and
>   the CAP1 conformance suite stays unchanged);
> - the `syzygy-nw3o` amendment;
> - any new Butlers read, content class or provider egress;
> - release or deployment.

## What is authorized

Implementation, under the normal implementation workflow, of exactly the
signed text of `three-surface-poc-vocabulary-epistemic-amendment-v1.0`, as
recorded by `THREE-SURFACE-POC-VOCABULARY-EPISTEMIC-AMENDMENT-SIGNOFF-v1.0.md`
(this directory), through these slices of
`docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md` and no others:

| Slice | What the signed text requires of it | Shared model? |
|---|---|---|
| 4a, shape unification | One record shape for every entity and relationship (POC-REQ-060 as amended) | yes (`packages/three-surface-poc-core`) |
| 4b, the Inferred arm | Inferred as a typed arm, allowed only for an agent's assertion and never counted as Observed | yes (`packages/three-surface-poc-core`, and `packages/cap1-core/src/epistemic.ts`) |
| 8, RFC1-25 names | Every relationship carries an RFC1-25 name in a role pair the table assigns, or a flag saying it is outside the table (POC-REQ-055), with a declared kind-to-class mapping whose truth stays Unknown | yes (`packages/three-surface-poc-core`) |

The design says slice 4a precedes slice 4b. This record sets no other order
inside the three.

[Observed: the packet states, and the design document says, that the four
human pages must stay byte-identical under slice 4a while the `/api/poc`
entity and relationship tuples become supersets of today's, so the machine
answer changes. Bounds below.]

**The added acceptance condition.** Every lane under this record carries the
condition of option A, in the owner's words quoted above. In particular:
- the declared marker set includes the existing per-row id markers
  `data-entity-id` and `data-relationship-id`;
- a test on a fixed fixture asserts that each counted marker population
  equals a hard-coded non-zero number, a literal and never a value imported
  from the module under test;
- a mutant that deletes every marker must fail that test.

[Observed: a rendered `data-relationship-id` marker already exists on the
exact-table rows, `apps/three-surface-poc/src/exact-tables.ts`. The packet
offers this as the reason the condition needs no new marker.] The condition
closes the zero-marker pass that review note 13 of
`docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-2-RAW.md` found, in
practice, without changing the specification. The normative fix is the later
amendment `syzygy-nw3o`, which this record does not authorize and which the
lead drafts under the 2026-10-15 autonomy direction.

## Placement in the shared-model chain

The three slices change the shared model, so they join the one-at-a-time
chain. The chain is the 2026-10-15 chain, extended by the 2026-10-20 record:
P-97 → P-100 → P-86 → P-96 → tree framing, then opening band → container
shape → M12 slices 1-2 (position only) → dismissal → item depth. The three
slices of this record are appended after those rows, as one further link.

The yield-the-slot rule of the 2026-10-20 record applies unchanged: a link
whose own gate is still open yields the slot to the next link that can start,
and takes it back at its listed place once its gate closes. A link of this
record may therefore start while an earlier link is waiting on a gate, and it
never starts while the slot is held.

[Observed: the packet lists, as still open ahead of these slices on
2026-10-21, tree framing `syzygy-73e.20`, P-86 `syzygy-dov.15.2` and P-96
`syzygy-u05.21`. So this authorization queues work and starts none.]

No lane starts on this record until it is on `main`.

## The slice-6 reading, and what is not known

[Inferred: the lead's reading, made 2026-10-21 and surfaced to the owner in
the item; the owner's answer did not rule on it.] Slice 6 splits into 6a and
6b. Slice 6a only adds `data-claim-id` to Trajectory and Orrery with today's
ids; the design says it needs no act for the attribute alone and may land any
time. Under that reading it lands under the improvement-cycles direction
(`THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`), before slice 4. Slice
6b makes the artifact identity the canonical join key; it travels with the
later identity package and is excluded here.

[Unknown: which recorded finding slice 6a traces to. The design names none. If
none does, 6a waits with 6b: the P-75 Q6 ruling in
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` lands a pursuit slice
under the improvement-cycles direction only when it traces to a recorded
finding.]

This record authorizes neither 6a nor 6b. It records the lead's reading so
that no lane reads this record as the warrant for either.

## Exclusions

Copied from the item, as above, and binding:
- slices 5, 6b and 7;
- a production Inferred constructor, so any constructor stays test-only and
  the CAP1 conformance suite stays unchanged;
- the `syzygy-nw3o` amendment;
- any new Butlers read, content class or provider egress;
- release or deployment.

Per the item, bead `syzygy-dov.9.2` is split so that slices 5, 6b and 7 stay
blocked, and `syzygy-dov.10.5` stays blocked behind them. The deferred-scope
questions D1-D4 of `syzygy-vk3f` stay open; nothing here answers them.

## Bounds

Every bound of `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`
holds for every row here, as the owner's option states. They include: exactly
the signed text; no new Butlers content class, body read or provider egress;
the daemon executes no observed code; every lane reviewed and verified per
craft-and-care, with a rule-6 mutant for each falsifier limb; escalation when
the signed text cannot be built as written; no release, deployment, second
repository, write into Butlers or act-bound byte edit; and withdrawal. That
record states them; this one adds the acceptance condition above and nothing
else.

## What this does not do

- It signs, adopts or accepts nothing (VIS-4), and it amends no
  specification, policy, contract or registry byte.
- It authorizes no production Inferred constructor, so no production code
  path can emit Inferred.
- It does not answer the P-75 Q4 question of when an Inferred constructor
  may be built; that needs its own act.

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
