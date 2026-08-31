# Owner direction — trust-based bootstrap observation

Date: 2026-08-31

Owner: Tzeusy

Decision ID: `TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31`

The owner responded to the blocked external-audit requirement:

> “`name or authorize an external device/account/service where you can write
> approvals, Syzygy can verify them, and tze/Codex/Docker cannot write.` lte's
> relax this requirement for now. I'm OK with this being a general principle
> that isn't strictly enforced, rely on trust rather than systemic blockage
> here”

## Direction

Independent, externally correlated owner-act provenance remains the preferred
trust principle, but its absence must not systemically block the bounded,
read-only Polaris observation of the configured Butlers repository.

For read-only repository observation, an exact digest-bound owner bootstrap
act may be trusted while it is still uncorrelated. The human and machine views
must disclose that basis; they may not call it independently verified.

This direction accepts the recorded risk that a same-tree writer can forge
bootstrap records. The POC relies on the owner’s trust in the reviewed Syzygy
revision, exact consent, secret policy and read-only adapter entry instead of
claiming that the repository can prove its own authorization.

## Boundary

This relaxation applies only to read-only repository observation. It does not
relax or authorize:

- writes to Butlers or any other observed repository;
- external egress or model-provider disclosure;
- observed-code execution, credential access or environment access;
- deployment, release, certification or a positive security claim;
- autonomous owner acts, mission effects or multi-user authority; or
- omission of secret screening, provenance disclosure, Unknown handling,
  exact Git-object containment or human/machine parity.

SEC-5 remains outcome-binding: no secret may appear in any model, cache, log,
surface, endpoint or record. A secret exposure remains a trust-floor violation
even though the policy’s owner act is trusted rather than independently
correlated.

This direction does not retroactively authorize the body reads recorded in
`docs/reviews/R-POLARIS-PRECONDITION-READ-BOUNDARY-INCIDENT.md`.

## Application gate

This decision authorizes drafting and review of the exact semantic delta. It
does not edit the accepted RFCs, the signed PWB requirement or the three gate
artifacts. Those exact bytes must be offered together for owner sign-off before
implementation or another Butlers project-shape body read.
