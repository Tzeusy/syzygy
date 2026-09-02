<!-- Owner authorization, recorded verbatim. Never edit below the line.
     Act family: implementation authorization (same family as
     decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md). It rests on
     the owner-signed polaris-project-wide-butlers-model amendment
     (decisions/PWB-STATE1-AMENDMENT-ACT.md, eleven artifacts bound at their
     exact digests) and on the three separate effect acts performed
     2026-09-02 (decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md,
     decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md,
     decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md), all verified present at
     recording.
     Authorization dated 2026-09-02 by the owner; recorded 2026-09-02 by the
     session the owner instructed, at repository state e136eeb.
     This authorization closes PWB task 1.8. It is a plain owner direction in
     the sense of PROCESS-GLOSSARY.md, not a digest-bound act: it binds no
     artifact bytes and adds no row to the acceptance-act record.
     The owner's words are quoted byte-for-byte; the scope reading that
     follows them is the recorder's and is labeled as such. -->

# OWNER AUTHORIZATION — POLARIS PROJECT-WIDE BUTLERS MODEL IMPLEMENTATION

Date: 2026-09-02
Owner: Tzeusy
Repository state at recording: `e136eeb`
Closes: task 1.8 of `openspec/changes/polaris-project-wide-butlers-model/tasks.md`

## The exchange, verbatim

After recording the three effect acts, the recording session reported to the
owner (quoted exactly):

> **One gate remains**: PWB implementation authorization (task 1.8). Until you
> grant it, no Butlers body read and no PWB implementation may start. When
> you want it, I can prepare that packet the same way.

The owner replied, in full:

> Authorized

`[Observed]` The reply is the owner's, in the owner's own session, in direct
response to the message above. No packet was prepared for this gate; the
owner chose to grant it directly, as they did for the Capability 1
implementation authorization and the Three-Surface POC direction.

## What the recorder reads this as

`[Inferred]` The word answers the one question put to the owner, so it is
read as the separate implementation authorization that task 1.8 requires,
and nothing wider. Concretely, the owner authorizes:

1. **Implementation planning and implementation** of the signed
   `polaris-project-wide-butlers-model` change — tasks §2 through §5 of its
   `tasks.md` — as one bounded improvement cycle of the Three-Surface POC.
2. **The first repository-body read of the one configured Butlers
   repository**, limited to the content class
   `declared-project-shape-text` named in the observation consent, and only
   after the implementation has itself evaluated all three effect acts under
   PWB-REQ-005 and found each valid. The acts are warrants; they are not
   evidence that any read succeeded or that any body is safe.
3. Code in the ordinary implementation plane only — `apps/**`,
   `packages/**`, tooling, root manifests — never inside `openspec/**` or
   `.syzygy/**`, under the in-force craft policies and the vendored
   `th-engineering` standards, exactly as the Capability 1 authorization
   requires.
4. A bounded Beads backlog derived only from the signed `tasks.md`, with
   POC shared-model work-in-progress limit one, review → repair → confirm
   → owner report before any next cycle.

## What this does not authorize

- No write, egress, execution, deployment, release, recovery, or mission
  effect on Butlers or on any other repository. The observer registry entry
  the owner adopted declares an empty write surface; that remains the bound.
- No second repository, no wider content class, no reading of Butlers
  content the secret-classification policy excludes or cannot classify.
- No production release, broad remote access, or multi-user support.
- No edit to any act-bound artifact: the eleven signed PWB artifacts, the
  three effect-act subjects, the six signed `three-surface-poc-experience`
  artifacts, or the seven adopted Capability 1 artifacts. Spec changes route
  through CC-REV-2's amendment path and a new owner act.
- No doctrine or contract change; no autonomous intent adoption; no
  Syzygy-authored implementation code; no unattended agent coordination.
- No independent verification: this authorization, like the three effect
  acts, is a state-(1) human direction. A later Syzygy-verified state is a
  separate act.

## Escalation triggers

Stop and return to the owner before proceeding if implementation would need
any of: a change to doctrine or an accepted contract; an amendment to the
signed PWB specification; a change to security, privacy, or retention
posture beyond the approved secret-classification policy; a change to the
constraints or envelope the registry entry declares; any observation outside
the consented content class or repository; or any scope beyond the signed
change.

## Owner correction

`[Unknown]` Whether the owner intended any narrower or wider reading than
the four points above. The owner may narrow or withdraw this authorization
at any time by a later direction; the recorder's reading stands only until
then, and withdrawal defeats grant.
