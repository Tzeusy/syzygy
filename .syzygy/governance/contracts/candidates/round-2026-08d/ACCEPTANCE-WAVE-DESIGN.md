# Acceptance wave design — round 2026-08d

**Status: candidate process design.** This file records *why* the
foundational package is offered in six waves and *how* the wave gates are
shaped. The gates themselves — exact phrases, exact digest arguments, the
ceremony — live in `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`,
which is the acceptance authority; this file is design rationale and is
never citable as authority. No act has been performed; nothing here adopts
anything (VIS-4).

## 1. Why waves — the defect the all-in-one act carried

The rev10 offer bound all foundational modules under one phrase, so the
owner's only choices were "accept everything, including the parts two
independent reviews returned `REVISE` over" or "accept nothing". Review
RD-8 called routing an owner to a record whose defect inventory was two
rounds stale *"the finding that converts act 1 from a knowing act into a
surprised one."* The round-2026-08d owner work order (§1 point 4; archived
verbatim as `OWNER-WORK-ORDER.md`) directs the decomposition: independently
acceptable waves, each small enough to know, each with its own digest
argument, so a defect discovered in one wave stops that wave and not the
eight contracts that never had it.

## 2. The partition

Membership is generated, never hand-listed: `scripts/build_active_manifest.py`
assigns every `rfcs/**.md` module to exactly one wave, rejects unassigned
files, asserts the partition (union = active manifest, no overlap, no empty
wave), and writes the six wave manifests under `../wave-manifests/`. Each
wave manifest's own sha256 is that wave act's argument; digests are read
from the manifests and are deliberately not restated here.

| Wave | Accepts | Modules |
|---|---|---|
| A | Kernel, evidence, storage, admission, cross-surface selection — RFC 0001, 0002, 0003, 0004, 0005, 0006 | 19 |
| B | The three surfaces: Polaris (RFC 0007), Trajectory (RFC 0008), Orrery (RFC 0009) | 11 |
| C1 | Context packets: identity, provenance, memory — RFC-0011 module 1 + package index | 2 |
| C2 | Context selection policy and budget posture — RFC-0011 module 2 | 1 |
| D1 | Mission Control prevention plane — RFC-0010 modules 1 (identity/approval/lifecycle), 2 (envelope/attention), 3 (budget reservation), 5 (portfolio/consent) + package index | 5 |
| D2 | Mission Control correction plane — RFC-0010 module 4 (effects, recovery, stop) | 1 |

**Why the seams sit where they do.**

- **A before everything**: the six Wave A contracts declare `depends_on`
  edges only inside Wave A. They are the semantic ground every surface and
  every mission clause projects from.
- **B as one wave**: the three surfaces cite each other (RFC-0007 ⇄
  RFC-0009 ⇄ RFC-0008) and nothing later; splitting them buys three
  ceremonies for no independent acceptability.
- **C1 / C2 (owner order §6)**: the packet/provenance contract (what a
  governed context packet *is*, RFC11-1..3, 5..10, 12) is stable and
  reviewable on its own; the selection policy (RFC11-4, 11, 13..16) is the
  part that moved this round and whose acceptance criterion — the blind
  golden fixtures — is external to it. An owner can bind packet identity
  without binding the selection rule set.
- **D1 / D2 (owner order §5)**: the prevention plane (what a mission is,
  what an envelope forbids, what may be reserved) is severable from the
  correction plane (what happens after failure: effects, recovery, stop),
  which is where both `REVISE` reviews concentrated. A defect found in
  post-failure semantics no longer blocks mission identity and envelopes.
- **Package READMEs travel with the first wave of their contract** (C1 and
  D1), so a clause map is never bound later than a clause it maps.

## 3. Ceremony order and cross-wave edges

Every `depends_on` edge points backward under the order
**A → B → D1 → D2 → C1 → C2**:

| Wave | Depends on contracts in | Backward under recommended order? |
|---|---|---|
| A | A only | yes |
| B | A, B | yes |
| D1 | A (0001/2/3/5/6, 0004 via module 3), B (0008) | yes |
| D2 | A (0002/3/4/5) | yes |
| C1 | A, B (0008), **RFC-0010 (D1+D2)** | yes |
| C2 | A (0002), **RFC-0010 (D1+D2)** | yes |

Waves may be performed out of this order, but a wave accepted while a
contract it `depends_on` is still candidate binds text whose reliances
point at unaccepted material — lawful only as a **knowing** acceptance
with that condition stated at the act, and the acceptance record's gate
rows say so. The C-waves are listed before the D-waves in the owner work
order's naming; naming order is not ceremony order, and the dependency
table above is why the ceremony recommendation differs.

## 4. What a wave act does and does not do

- **Binds** the exact bytes of its manifest rows, installed per the
  acceptance record's ceremony (§2 there) into
  `.syzygy/governance/contracts/rfcs/` — a copy, never an edit.
- **Clears specification authoring only.** Every wave's contracts carry a
  binding phase-rule clause (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27,
  RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12): user-observable
  behavior still routes through owner-approved OpenSpec requirements
  before any implementation work is scheduled.
- **Adopts no sibling wave.** No wave implies another; partial acceptance
  is a designed outcome, not a degraded one. The active manifest remains
  the package identity; it is no act's argument.
- **D1 additionally carries RFC10-24**: even fully accepted, no mission
  leaves `awaiting-approval` until the D3 doctrine question (act 5) is
  ruled — acceptance of D1 is acceptance of contract text, never an
  operating license.
- **C2 additionally carries its external criterion**: RFC-0011 module 2
  states it is acceptable only when its selection rules can reproduce the
  blind golden selection fixtures (`../fixtures/`), whose task/answer
  boundary exists for exactly that derivation.

## 5. Supersession

The single-act phrase `ACCEPT COMPACTED FOUNDATIONAL RFCS: <sha>` is
**retired at this round's delivery and satisfies nothing**, on the same
rule that retired the rev9 phrase: an offer superseded must not remain
performable beside its successor. Acts 2 (craft CC-TEST-2), 3 (topology),
4 (overview), and 5 (D3) are unchanged by this restructure and keep their
rows in the acceptance record. `check_governance.py` CG-7a..7e verify the
active manifest, the wave partition, and every wave argument against the
acceptance record on every run.
