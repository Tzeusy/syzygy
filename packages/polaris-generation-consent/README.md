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
- `matches(request)` binds a run to the source population the ports were built
  for; wire it into `verifySources`.
- `reserve` is the durable reservation (for example the lifecycle journal's
  `admit`), run only after consent holds.

Not here: the reader over real records (their in-force index is undefined), the
content-class mapping, and the single egress check for any route other than
`permitted`.
