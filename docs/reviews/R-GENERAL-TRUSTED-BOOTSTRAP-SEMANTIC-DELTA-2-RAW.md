**REVISE**

Bound to sha256 `7d9e3f32674ddb04a4267e65145cedc129f199d0ac5924ca854e22515cc3f7ff`.

All four prior findings are fully disposed:

- State-(1) formation now retains exact phrase/digest/commit/tag and explicitly handles post-A1 selection without downgrade.
- RFC2-13 preserves kernel-recorded facts separately from authorization-bearing policies and owner decisions.
- Owner acts are explicitly warrants, never substantive evidence.
- RFC9-45 no longer invents deployment/recovery authority.

One remaining finding:

- **State-(2) formation after A1 is undefined.** The delta says to keep the current state-(2) definition, which defines state (2) only as a pre-mechanism bootstrap act later correlated. But state (1) may now be created after A1, and future owners must also be able to perform an act directly through A1 without first selecting trusted-bootstrap provenance. Amend state (2) to cover both:
  1. an owner act performed through the A1 ceremony and audit mechanism; and
  2. a prior state-(1) act later correlated through A1.

Without that sentence, a post-A1 owner choosing independently verified provenance has no fully defined state, conflicting with RFC3-16(b) item 9 and future RFC10 mission approval.
