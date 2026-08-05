# Context-selection fixture 4 — security/execution-profile change

**Objective.** A governed work item: amend an execution profile (tighten
an isolation class, add a destructive-operation gate) and prepare the
owner-approval ceremony for the amendment. Risk class: security surface,
authorization-bearing (RFC5-18(c) approval; RFC5-23 lifecycle).

**Selection rule trace (RFC11-4).** Warrant names the profile →
RFC-0005 `execution-profiles` + package README (RFC5-18..23). Profile
amendment approval is an owner act → RFC-0003
`governance-homes-and-owner-acts` + README (RFC3-16(a)/(b)/(c) — under
the two-state model the approval is an owner-adopted bootstrap act until
correlation, and the packet says so). Doctrine floor → `security.md`
(SEC-3 and the execution posture). Craft duty → `security-and-secrets.md`
(secret handling in profile definitions).

## Required context (mandatory, deterministic)

```
scripts/context_load.py rfcs/RFC-0005/README.md \
  rfcs/RFC-0005/execution-profiles.md rfcs/RFC-0003/README.md \
  rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:security.md \
  craft:security-and-secrets.md
```

Measured: **10,866 words ≈ 14,669 estimated tokens** — inside the 15–20k
working target with room.

## Omitted applicable candidates, with reasons

- RFC-0005 `admission-and-boundary` — client admission is untouched; the
  audit-trail clause RFC5-25 that RFC3-16(b) item 9 binds is quoted at
  binding strength inside the governance-homes module the packet carries.
  `consent-egress-secrets` — no consent class or egress route changes.
- RFC-0008 — dispatch consumes profiles by identity; the gate text
  (RFC5-18) travels in the packet; work-surface obligations bind
  elsewhere.
- RFC-0003 `manifests-and-namespace`, RFC-0001/0002/0004/0006/0007/0009 —
  not cited by the warrant's clause set.
- RFC-0010/0011 — no mission context; a profile amendment under a
  mission's envelope would add RFC-0010 via the envelope input rule
  (RFC11-1).

## Why no applicable constraint was lost

The closed isolation and destructive-operation vocabularies (RFC5-21/22),
the profile-contents floor (RFC5-20), the approval gate (RFC5-18(c)) and
lifecycle (RFC5-23), the owner-act binding set (RFC3-16(b), nine items),
and the honest two-state render (RFC3-16(c)) are all mandatory-loaded;
the craft security bar rides along for the definition hygiene. Nothing in
the omitted set is cited by these clauses at binding strength.

## Suggested inferred additions (provenance: index adjacency)

RFC-0005 `admission-and-boundary` (if the ceremony's session/credential
context is in scope); RFC-0002 `rendering-vocabularies`
(`execution-blocked` reason #12 rendering downstream).

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`39c6b21ccdb9ad52…`. Compiler: `context_load.py`, selection rules
rev10-fixtures.

*Re-measured 2026-08-05 (refactor round): figures and packet digest refreshed after this round's recorded corrections to RFC-0003 governance-homes (P-6, +13 w) and the craft banners (P-7, security policy +26 w); selection unchanged. Prior figures/digest are in git history.*

*Re-measured 2026-08-05b by `scripts/check_governance.py` CG-18, which recomputes the digest and the word count from the declared mandatory set rather than trusting the recorded figures. Previous: 10,893 words, digest `a56fb116fa588b9b…`. Selection unchanged; the movement is contract edits landing under a fixture that had no mechanical freshness check until now.*
