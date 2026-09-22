# Owner direction — retention posture for retained Polaris evaluation records

Date: 2026-09-23

Owner: Tzeusy

Decision ID: `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIR-2026-09-23`

Gate bead: `syzygy-dov.28`. Warrant for the question: row **P-79**, arm A,
of `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` (this directory).
Offering: `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md`
(this directory), which remains the question and is not edited.

A plain owner direction in the shape of
`POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md`: it binds no artifact
digest, needs no manifest or recorder script, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing in `check_governance.py`.

## The owner's words

The owner asked, in the Claude Code CLI on 2026-09-23, to be walked through
the pending owner decisions "with /th-projects questionnaire", and answered
three structured questions on this packet. The selected option labels,
byte-for-byte:

| Question as put | Owner's answer |
|---|---|
| Envelope: the six top-level keys as listed? | "Six keys as drafted (Recommended)" |
| When does the on-disk total disclosure start? | "From slice 1 (Recommended)" |
| Issue the direction? | "Issue now, with these answers" |

The third option was presented as: "I record a dated plain owner direction
in decisions/ citing your answers in this session; slice 1 becomes lawful
within its bounds." The owner did not reply with the packet's suggested
issuing line; the selection above is the issuing instruction, and this
record quotes it rather than substituting that line for it.

Repository state at recording: Syzygy `origin/main` at `57863cc`.

## The direction, as issued

The packet's proposed direction text, unchanged except that its date
placeholder is filled. The owner's two answers above take the drafter's
envelope and disclosure-timing readings (packet §"What is the drafter's and
not yours", items 1 and 2) as the owner's own.

```
OWNER DIRECTION — RETENTION POSTURE FOR RETAINED POLARIS EVALUATION
RECORDS

Date: 2026-09-23
Owner: Tzeusy
Continues: decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md and
decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md, whose
retention-posture escalation trigger this direction answers and does not
widen.

1. WHAT IS AUTHORIZED. The Three-Surface POC daemon may retain, in its
   own state directory, one durable record per identified evaluation.
   Per claim, that record holds exactly three things: the claim
   identity, the epistemic tuple, and the challenge state. Once per
   record it holds the schema name, the evaluation identity (snapshot,
   snapshot label, inputs digest, as-of instant), the observer revision,
   the observed project's revision, and the two counts (claim objects
   and distinct claim identities). Nothing else.

2. WHAT IT MAY NEVER HOLD. No source body or body bytes of any kind; no
   support anchor; no resolution route; no credential or secret
   material; no content the approved secret-classification policy
   excludes or cannot classify. The approved policy's retention clause
   is unchanged by this direction and remains binding.

3. WHERE IT LIVES. The daemon's own state directory only, under the same
   directory and file modes the existing records there use. Never in an
   observed repository. Never in openspec/** or .syzygy/**. No record is
   committed out to any governed plane.

4. HOW LONG IT LIVES. Unbounded. No record is pruned, discarded,
   overwritten or rewritten. A record under an evaluation identity that
   already exists with different content is refused, not replaced.

5. DISCLOSURE. From the first build that retains a record, the surface
   renders the number of retained records and their total on-disk bytes;
   when the claim-state delta band lands, that total renders beside it.
   Retention is never silent.

6. HONESTY OBLIGATIONS CARRIED IN. A retained record is an observation
   record under VIS-6(b): immutable, evaluation-identified, and marked
   stale once superseded. No judgment over a retained record is computed
   against a wall clock; every one is computed at an evaluation's own
   as-of instant. An absent history and an unreadable history are
   distinct states and neither renders as "no change".

7. WHAT THIS DOES NOT AUTHORIZE. No dismissal and no widening of the
   challenge vocabulary — that is a specification amendment needing its
   own semantic delta, review and act. No promotion of an owner note, no
   annotation, and no write of any kind into an observed repository or
   into any governed plane; the observer registry entry's empty write
   surface stands. No new served route, no listing or download of a
   retained record, and no new or relaxed response ceiling. No second
   repository, no wider content class, no consent amendment, no egress,
   no observed-code execution, no deployment, release or mission effect,
   no doctrine or contract change, no autonomous adoption. Every
   exclusion of the 2026-09-02 authorization and its 2026-09-05
   continuation is retained unchanged.

8. WHAT THIS IS NOT. This direction binds no artifact digest, amends no
   specification, policy or registry byte, adds no row to the
   acceptance-act record and registers nothing. It is a warrant, not
   evidence: it proves no read, no write, no render and no result.

9. WITHDRAWAL. This direction may be narrowed or withdrawn at any time
   by a later direction. Withdrawal defeats grant: on withdrawal the
   daemon retains no further record, and what to do with records already
   written is a question for that later direction.
```

## The recorder's reading of scope

`[Inferred]` — the recorder's, not the owner's.

- The six envelope key names — `schema`, `evaluation` (holding `snapshot`,
  `snapshotLabel`, `inputsDigest`, `asOf`), `observerRevision`,
  `projectRevision`, `claimCount`, `identityCount` — are now the owner's
  choice, not the drafter's, so invariant I3 asserts over an owner value.
  Changing them needs a later direction.
- The packet's twelve invariants (I1–I12) remain the drafter's acceptance
  floor for the implementing bead; the owner did not adopt them as
  authorization text, and they are not part of the direction.
- The delta band's row cap (P-79 Q3) is untouched and is chosen at slice 2.
- Slice 1 of `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md` is
  lawful within §§1–7 above, under the 2026-09-05 continuation act, and is
  otherwise gated as that act and its bead say. Slice 2 is gated on its own
  bead order.
