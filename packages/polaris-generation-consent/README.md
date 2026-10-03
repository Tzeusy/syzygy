# Polaris generation consent

Consent-backed `permissionIdentity`, `admit` and `permitted` ports for the
generation pipeline. They read public-repo admission records (observation and
egress consent) through an injected `AdmissionRecordReader`, fail closed, and
emit a content-free audit record per check. This package grants nothing: the
real records are owner acts that do not exist yet, so it is coded against an
interface and fixtures.

- A record counts only if it is in force (`inForceAt` set and not in the
  future), has no withdrawal marker (dated or not), and is not replaced by a
  successor that took effect. Two records with one id and version but different
  digests void each other.
- Every source needs an observation grant for its repository and a full commit
  object id; a tag label never counts. Every non-excluded source also needs the
  egress record's repository and content class (an undeterminable class is
  refused), and the generator's own instruction class must be admitted.
- The permission identity digests the records relied on. `admit` and
  `permitted` recompute it and refuse on any change, so withdrawal between
  stages or between admit and send stops the send.
- Every refusal renders as `unconsented-source-or-provider`; `reasons` in the
  audit say which test failed. An audit sink that throws also refuses.
- `withConsent(base, options)` is the intended wiring: it replaces `verifySources`,
  `permissionIdentity`, `admit` and `permitted` together, so the population sent is
  the population consented. `matches(request)` digests every source property
  (bodies and span texts by hash, classification basis, any segment fields); a body
  that one full-file span already carries digests the same with or without the
  duplicate, as the pipeline drops it before `verifySources`.
- The reader's output is validated whole (`parseAdmissionRecords`); a malformed
  record, a non-integer time field, or a clock that is not a safe integer refuses,
  attributed to its own reason. An empty population is refused.
- Each check audits its final outcome once (a reservation refused, failed or
  followed by a failed audit is not recorded as permitted).
- `reserve` is the durable reservation (for example the lifecycle journal's
  `admit`), run only after consent holds.

Not here: the reader over real records (their in-force index is undefined), the
content-class mapping, and the single egress check for any route other than
`permitted`.
