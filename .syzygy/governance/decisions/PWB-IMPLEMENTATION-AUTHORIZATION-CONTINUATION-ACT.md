<!-- Owner direction, recorded verbatim. Never edit below the line.
     Act family: implementation authorization (same family as
     decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md, which it continues,
     and decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md). It
     rests on the three separate 2026-09-05 acts of the PWB truth-and-policy
     packet (decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md,
     decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md,
     decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md), each verified
     current, tagged and pushed at recording, and on the unchanged 2026-09-02
     observation consent (decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md).
     Direction dated 2026-09-05 by the owner; recorded 2026-09-05 by the
     session the owner instructed, at repository state 382798a on branch
     agent/syzygy-1z3.24.3.
     This direction closes bead syzygy-8i7. It is a plain owner direction in
     the sense of PROCESS-GLOSSARY.md, not a digest-bound act: it binds no
     artifact bytes, adds no row to the acceptance-act record and registers
     nothing in CG-7e. The owner's words are quoted byte-for-byte; the scope
     reading that follows them is the recorder's and is labeled as such. -->

# OWNER DIRECTION — CONTINUATION OF PWB IMPLEMENTATION AUTHORIZATION FOR THE 2026-09-05 AMENDMENT

Date: 2026-09-05
Owner: Tzeusy
Repository state at recording: `382798a` (branch `agent/syzygy-1z3.24.3`)
Continues: `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02)
Closes: bead `syzygy-8i7`

## Why a continuation was needed

`[Observed]` The 2026-09-02 implementation authorization names escalation
triggers that stop implementation before "an amendment to the signed PWB
specification; a change to security, privacy, or retention posture beyond
the approved secret-classification policy; a change to the constraints or
envelope the registry entry declares". The three 2026-09-05 acts changed
exactly those three things. The owner decision packet
(`contracts/candidates/pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md`,
§"What all three acts still do not authorize") states that the acts "do not
authorize implementation automatically" and that the owner "must separately
continue implementation authorization across its signed-spec, policy and
registry escalation triggers".

## Verification before the question was put

`[Observed]` At the time the question was put and again at recording, on
branch `agent/syzygy-1z3.24.3` at `382798a` (equal to `origin`):

| Act | Dedicated record | Tag | Recorder `--check` |
|---|---|---|---|
| Decision 1, behavior amendment | `decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md` | `pwb-truth-readiness-amendment-signed-2026-09-05` at `2a3310a` | passes |
| Decision 2, secret-policy amendment | `decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` | `pwb-approve-policy-signed-2026-09-05` at `156b689` | passes |
| Decision 3, observer-registry amendment | `decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` | `pwb-adopt-registry-entry-signed-2026-09-05` at `382798a` | passes |

All three tags are on `origin`. `scripts/check_governance.py` reported 0 FAIL
at `382798a`, with CG-7e reporting 0 findings over 27 files and the
`--selftest` fixtures all passing. The 2026-09-02 observation consent
(`decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`) is unchanged; the packet
offered no consent amendment and none was performed.

## The exchange, verbatim

After recording Decision 3, the recording session put one question to the
owner (quoted exactly):

> **Continuation of PWB implementation authorization.** The 2026-09-02
> authorization stopped at signed-spec, security-policy and registry-envelope
> changes. Today's three acts changed exactly those. Do you continue
> implementation authorization to cover the amended semantics as signed
> today, for the one configured Butlers repository and content class
> `declared-project-shape-text`, with every original exclusion retained: no
> release, deployment, Butlers write, second repository, wider content class,
> egress, observed-code execution, mission or multi-user authority?
>
> Reply `Continue PWB implementation authorization for the 2026-09-05
> amendment` to grant it. Any other wording, or silence, continues nothing.
> If granted I will record it, merge the branch to main via PR, and unblock
> only the amended PWB implementation tasks.

The owner replied, in full:

> Continue PWB implementation authorization for the 2026-09-05 amendment

`[Observed]` The reply is the owner's, in the owner's own session, in direct
response to the question above, and is byte-identical to the offered
wording. No packet was prepared for this gate; it is a plain direction, as
the 2026-09-02 authorization was.

## What the recorder reads this as

`[Inferred]` The reply answers the one question put to the owner, so it is
read as the continuation of the 2026-09-02 implementation authorization
across the three named escalation triggers, and nothing wider. Concretely,
the owner continues authorization so that:

1. **The amended semantics signed on 2026-09-05 are the implementation
   target.** The eleven artifacts bound by
   `contracts/candidates/pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`
   replace the 2026-09-02 package as the behavioral authority the
   implementation must satisfy: the closed project-fact and precedence
   grammar, inert inline and fenced Markdown code admitted while genuine
   active content stays excluded, the deterministic parse and output
   resource envelope, the one transient verbatim baseline requirement, and
   PWB-REQ-021 readiness kept separate from PWB-REQ-022 validity.
2. **The amended policy and registry entry are the effect artifacts the
   implementation evaluates.** Under PWB-REQ-005 the implementation must
   evaluate the 2026-09-05 policy and registry acts (their dedicated records
   above) together with the unchanged 2026-09-02 consent, and may re-point
   its governance inputs from the 2026-09-02 policy and registry records to
   the 2026-09-05 successor records. The superseded records, their digests
   and their tags remain immutable history and must never be edited.
3. **Scope is otherwise unchanged from 2026-09-02.** The same one configured
   Butlers repository, the same content class `declared-project-shape-text`,
   the same ordinary implementation plane (`apps/**`, `packages/**`,
   tooling, root manifests; never `openspec/**` or `.syzygy/**`), the same
   bounded Beads backlog and review, repair, confirm, owner-report cycle.
4. **The amendment branch may now be merged.** The handoff boundary "do not
   merge the amendment branch or implement its semantics before all three
   acts and explicit authorization continuation" is satisfied by this
   direction; merging `agent/syzygy-1z3.24.3` into `main` through a pull
   request is within it. Frozen PR #5 and its terminal review stop are not
   affected.

This continuation unblocks only the amended PWB implementation beads that
depend on `syzygy-8i7` through `syzygy-1z3.24.3`.

## What this does not authorize

Every exclusion of the 2026-09-02 authorization is retained unchanged:

- No write, egress, observed-code execution, deployment, release, recovery,
  or mission effect on Butlers or on any other repository. The amended
  registry entry still declares an empty write surface.
- No second repository, no wider content class, no consent amendment, and no
  reading of Butlers content the amended policy excludes or cannot classify.
- No production release, broad remote access, multi-user support, or
  autonomous behavior.
- No edit to any act-bound artifact, including the eleven 2026-09-05 signed
  artifacts, the amended policy and registry subjects, and every superseded
  2026-09-02 record. Further spec changes route through CC-REV-2's amendment
  path and a new owner act.
- No doctrine or contract change; no autonomous intent adoption; no
  Syzygy-authored implementation code; no unattended agent coordination.
- No independent verification: this direction, like the three acts it rests
  on, is a state-(1) human direction. A later Syzygy-verified state is a
  separate act.
- No proof of any read, screening, parse, render, answer or comprehension
  result. The acts and this direction are warrants, not evidence.

## Escalation triggers

Stop and return to the owner before proceeding if implementation would need
any of: a change to doctrine or an accepted contract; a further amendment to
the signed PWB specification beyond the 2026-09-05 package; a change to
security, privacy, or retention posture beyond the 2026-09-05 approved
secret-classification policy; a change to the constraints or envelope the
2026-09-05 registry entry declares; any observation outside the consented
content class or repository; or any scope beyond the signed change.

## Owner correction

`[Unknown]` Whether the owner intended any narrower or wider reading than
the four points above. The owner may narrow or withdraw this continuation
at any time by a later direction; the recorder's reading stands only until
then, and withdrawal defeats grant.
