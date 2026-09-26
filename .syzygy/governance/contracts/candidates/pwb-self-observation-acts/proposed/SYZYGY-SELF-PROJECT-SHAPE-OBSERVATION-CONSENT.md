# Syzygy self project-shape observation consent (test-only)

Date: 2026-09-26 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `PWB-SELF-CONSENT-2026-09-26`

Record version: `1.0.0-candidate.1`

Consent class: observation

Observation content class: `declared-project-shape-text`

Subject: `(project:syzygy, repository:syzygy)`

Current locator: the root of the Syzygy checkout that runs the conformance
test, resolved from that checkout's own Git metadata at test time
(configuration, not repository identity)

Purpose: test-only. This consent exists for one conformance fixture that
measures the project-shape pipeline against this repository's own tracked
tree (M8 slice 6). Nothing observed under it is served to any reader.

Status: **candidate; no effect until the owner acts on this exact digest**
(self-declared stamp; effective status comes only from an owner-act record,
RFC3-16)

Proposed revocation state: active; supersedes no earlier consent

## Where the grant comes from

No owner statement is quoted here, because none has been given for this
pair. The owner's 2026-09-21 ruling on P-74 question 3 (recorded in
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`)
chose three separate, dated acts scoped to a test-only self-observation
before the fixture may run. That ruling asks for this record; it does not
grant it. If the owner performs the act over this record's exact digest,
the act itself is the grant.

## Scope

The consent covers read-only reads of exact Git objects in this repository,
at the one fixed Git revision a conformance fixture names, selected by the
observation the second adapter-registry entry for this pair declares
(observer `polaris-syzygy-self-project-shape`) and screened by the
secret-classification policy's self-observation scope.

Everything read is used only inside the conformance test process. The
rendered page and machine answer the test builds are in-memory values the
test inspects; they are never served, cached, logged, written to disk or
written to a walkthrough record.

The scope excludes:

- any repository other than this one, including the Butlers repository,
  whose consent is a separate record this one neither widens nor narrows;
- the working tree, untracked or ignored files, and any revision other than
  the one the fixture names;
- data stores, credential stores, secret APIs and the process environment;
- credential files and arbitrary implementation-file bodies;
- executing any code in this repository as part of the observation, and
  network egress;
- any write to this repository; and
- any route, cache, log line, stored evaluation or walkthrough record.

The grant has no silent expiry. The owner may narrow or revoke it through a
later recorded act; revocation does not erase prior observation records.

## Provenance state and effect

[Observed] This candidate names the owner, date, subject, content class and
scope. It has no effect until the owner acts on its exact digest. It is one
of three separate acts the P-74 question 3 ruling requires; the other two
(the policy's self-observation scope and the second registry entry) are
separate artifacts with separate acts, and a body read under this pair
requires all three to be valid.

If acted on, its provenance state is **owner-adopted (bootstrap,
uncorrelated)**, state (1) under RFC3-16(c), only if the human act
explicitly selects state (1) and records the A1 audit-record identity as
absent. That state authorizes only this read-only, test-only observation,
must remain visible as uncorrelated, and is never "independently verified".
The act is a warrant to observe within this scope; it is never evidence
that any read occurred, that screening succeeded, or that any derived claim
is true.
