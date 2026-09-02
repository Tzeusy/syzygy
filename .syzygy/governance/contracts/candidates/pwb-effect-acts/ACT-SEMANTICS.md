# Act semantics — the three PWB effect acts

> Candidate. This file fixes what each offered act binds under RFC3-16(b) so
> the recorder, the reviewer and the owner read one meaning. It performs
> nothing. Effective status arises only from an owner-act record.

Each act is separate: it has its own phrase, its own act-record identity, its
own artifact and its own exact digest. The three are evaluated independently
(PWB-REQ-005); a body read requires all three to be valid. An act may be
performed in any order, alone or together, and each is individually revocable
by a later recorded act.

## Common binding (RFC3-16(b) items 1, 5, 6, 8, 9)

| Item | Value for every act below |
|---|---|
| 1. Project identity | `project:syzygy` |
| 5. Owner attribution | Tzeusy, the sole project owner |
| 6. Act instant | the instant the owner writes the phrase; the recorder records it and never back-dates |
| 8. Supersession / revocation | none: each act is the first act on its artifact and replaces no earlier act |
| 9. A1 audit-record identity | **explicitly absent**; the act is state (1), `owner-adopted (bootstrap, uncorrelated)`, chosen by performing the phrase; no correlation is claimed |

State (1) is selected explicitly by the owner performing an offered phrase.
The recorder writes the provenance state and the A1 absence into the act
record. A record claiming state (2) cannot be produced by this packet.

## Per-act binding (items 2, 3, 4, 7)

| # | 4. Act type | 2. Stable artifact identity | 3. Exact digest | 7. Scope |
|---|---|---|---|---|
| 1 | `consent-observation` | consent record `PWB-CONSENT-2026-08-31` at `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` | `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841` | Observation consent for the pair (`project:syzygy`, `repository:butlers-configured-poc`), content class `declared-project-shape-text`, read-only Git objects in the signed PWB source population; every exclusion the record lists stands |
| 2 | `approve-policy` | policy `polaris-butlers-project-shape-secrets` version `1.0.0-candidate.4` at `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` | `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61` | Approve this exact secret-classification policy as the observing project's policy for that pair and content class, across every ingest boundary the policy names |
| 3 | `adopt-registry-entry` | adapter-registry entry `polaris-butlers-project-shape` version `1.0.0-candidate.3` at `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | `d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7` | Adopt this exact entry in Syzygy's governance plane for that pair with read-only authority and an empty write surface; it admits the observer's declared output classes as deterministic facts only when an authorized implementation exists |

## Exact phrases

```text
CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION: 5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841
APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: 513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61
ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7
```

The argument of each phrase is the SHA-256 of that artifact's bytes, not of
the manifest. The manifest `PWB-EFFECT-ACTS-MANIFEST.txt` exists so the three
digests can be verified as one closed population; it is not itself acted on.

## What the acts warrant and what they never prove

Each act warrants only the use of its exact artifact for its stated scope. None
is evidence that a read occurred, that screening succeeded, that admitted
content is secret-free, or that any derived claim is true (RFC3-16(c)). None
grants PWB implementation authority (task 1.8), write, egress, execution,
deployment, release, recovery, mission, second-repository, autonomous or
multi-user authority. A later A1 correlation may raise any of the three to
state (2) without editing its artifact; an artifact edited after its act is an
artifact with no act.
