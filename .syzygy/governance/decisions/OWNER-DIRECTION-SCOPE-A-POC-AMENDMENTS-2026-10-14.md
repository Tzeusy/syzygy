# Owner direction — Scope A extended to Three-Surface POC specification amendments

Date: 2026-10-14

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14`

Extends: `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` (this
directory). That direction is not edited.

This is a plain owner direction in the shape of
`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`. It binds no
artifact digest, adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers
nothing in `scripts/check_governance.py`. It signs nothing by itself.

## The owner's words

On 2026-10-14, in the lead Claude Code session, the owner answered the
structured questions of register row P-97 (the Three-Surface POC
block-provenance amendment,
`../contracts/candidates/three-surface-poc-block-provenance-amendment/OWNER-DECISION-PACKET.md`).
To its question 2, "By which route?", the owner selected the option
"Extend Scope A to POC".

[Observed: the selection as the lead session relayed it to this lane; the
owner's answer itself is in that session, not in this repository.] The lead
session relayed its meaning as: the 2026-10-02 Scope A version-tag route is
extended to Three-Surface POC specification amendments generally, so P-84
(the POC identity amendment) and P-100 (the POC governing-intent amendment)
also follow it when they clear.

The packet offered "Extend Scope A to this package alone"; the selection
relayed is the wider "to POC". This record carries the wider reading because
that is the one relayed, and says so here rather than smoothing the
difference away.

## The direction

1. **Route.** A Three-Surface POC specification amendment, a package that
   patches `openspec/changes/three-surface-poc-experience/`, may be signed
   by version tag under Scope A, as the PWB specification deltas are: the
   owner's selection of an option naming the package and a `major.minor`
   version is the sign-off, bound by the tag `<package>-v<major>.<minor>`.
   No typed phrase and no digest argument is required.
2. **Everything else in Scope A stands.** A package is offered only after a
   fresh-context round returns CONFIRM, or CONFIRM WITH EXCEPTIONS with
   notes only; the mechanical checks stay; VIS-4 holds.
3. **Covered now.** P-97, signed v1.0 the same day. P-84 and P-100 follow
   this route when they clear their own review; neither is signed by this
   record.

## Bounds

- **Route only.** It authorizes no implementation of any POC amendment.
  Signing a package starts no implementation; each needs its own
  implementation authorization.
- **No other scope.** It does not reach doctrine, accepted contracts,
  craft policy, registry entries, the Capability 1 specification, or any
  specification other than the Three-Surface POC one. Scope B (all
  artifacts) is still not issued. Every act already performed keeps its
  record and digests.
- **Withdrawal.** A later direction may narrow or withdraw this one;
  withdrawal defeats grant.

## What the tooling needed

`scripts/record_versioned_signoff.py` names this record as the `extension`
of each POC package it covers: the dedicated sign-off record carries a
`Scope A extension:` line naming it, the aggregate block's Direction row
names it, and recording or `--check` refuses when this file is missing. Only
P-97 is registered today; P-84 and P-100 take the same field when they are
added. No check, act phrase or `ACT_DIGEST_COPY_FILES` row is added.
