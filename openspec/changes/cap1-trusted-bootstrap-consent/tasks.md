# Candidate acceptance and handoff

> Drafting/review work only is authorized. Unchecked adoption and implementation
> tasks below are gates, not execution instructions for this session.

- [ ] Independently review the exact proposal, two requirement replacements,
  design and applicability/plan handoff under CC-REV-1 and CC-REV-4; retain raw
  verdict and disposition each finding. Freeze the reviewed bytes.
- [ ] Owner adopts the exact normative amendment and associated applicability
  judgments; predecessor artifacts and performed records remain unchanged.
- [ ] Owner separately authorizes the bounded CAP1 consent implementation and
  exact record-encoding/interface scope. No runtime or project-access consent is
  implied. Reconcile syzygy-u2a.1 and existing dependent packets before dispatch.
- [ ] Extend the existing consent and consent-loading tests, capture/system seam
  and parity oracle after authorization. Use synthetic fixture acts with explicit
  labels; never treat fixtures as real owner acts. One behavioral gate species
  per predicate, not a second source-grep gate. Existing tests: consent.test.ts,
  consent-loading.test.ts, CAP1-REQ-011/016/041/045/046 conformance, and the
  held snapshot/coverage/discoverability system seams named in the predecessor
  plan. Determine net test delta at the concrete implementation packet.
- [ ] Verify every named invalid-case variant individually at the pre-read
  boundary; capture intercepted dependent-content reads and literal expected
  refusal/provenance tuples. Mutate grant-without-act, omitted-audit-as-absent,
  failed-state2-downgrade, withdrawal dropping and post-capture re-read predicates
  separately and demonstrate their responsible existing test fails.
- [ ] Verify legacy record refusal, positive explicit bootstrap, correlated
  fixture success, absent provider failure for state (2), grant/withdrawal input
  order, per-project isolation, content-read failure and new-evaluation correlation.
  Compare human/machine output through the independent wire oracle, including
  keyboard-accessible explanation and no effect-success inference.
- [ ] Run focused implementation checks, then the canonical PROJECT-STATUS.md
  battery in a fresh clone at the reviewed implementation commit. Inspect actual
  output/denominators; report retained evidence and exact Tests delta. A candidate
  spec check is not runtime correctness, full coverage, adoption or merge evidence.
