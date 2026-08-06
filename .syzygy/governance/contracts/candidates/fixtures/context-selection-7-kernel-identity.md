# Context-selection fixture 7 — kernel identity change

**Status:** DRAFT — a candidate fixture, not part of the rev10 accepted
fixture set (fixtures 1–5). Binds nothing. Repaired 2026-08-05 against the
two stored §20.4 reviews; the repairs are recorded in
`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`.

**Objective.** A governed work item: change how a kernel entity's durable
identity survives a split/merge event, and the continuity links recorded for
it. Risk class: **identity floor** — CC-BAR-5 floor 7 ("kernel identities
and `.syzygy/**` schema migrations are identity-preserving; migrations never
orphan or silently re-mint durable IDs"). A change here can orphan every
historical citation.

**Selection rule trace (RFC11-4).** Identity minting, continuity, and
split/merge are RFC-0001 §3.3 (RFC1-11: "Split and merge mint successors,
never mutations") → the kernel module is mandatory **in full** (it is a
single-file contract; there is no smaller load unit). Identity changes alter
what a claim resolves to at an evaluation → RFC-0002's
`snapshot-and-evaluation-core` (claim identity, evaluation identity) plus the
package README (spanning invariants + the deterministic clause-lookup rule).
Doctrine's `architecture.md` carries the constitutional identity and temporal
model the change must not contradict. The **declared risk class is itself a
craft floor**, so the artifact that owns the floor is mandatory:
`engineering-bar.md` carries CC-BAR-5's floor text, and that text — the
obligation this change may not weaken — is restated nowhere in the selected
RFC set. This last inclusion follows fixture 4's precedent (a declared craft
duty pulls the owning craft policy) and is what takes this packet over
budget; see the disclosure below.

## Required context (mandatory, deterministic)

```
scripts/context_load.py rfcs/RFC-0001-project-graph-identity-state-planes.md \
  rfcs/RFC-0002/README.md rfcs/RFC-0002/snapshot-and-evaluation-core.md \
  doctrine:architecture.md craft:engineering-bar.md
```

Measured: **15,823 words ≈ 21,361 estimated tokens.**

## ⚠️ Above the justification trigger — disclosed, not trimmed

21,285 estimated tokens exceeds the **20,000-token** line at which the
charter §11.4 context-budget table requires explicit justification or task
decomposition. (§11.4's table is cited directly: its intended home, the
candidate knowledge-hygiene craft policy, is not installed, and no
`CC-BUDGET-*` identifier resolves to a governed artifact today.) Recorded as
a justification rather than resolved by trimming, because trimming would drop
mandatory context to improve a number — the failure RFC11-5 forbids.

| Field | Value |
|---|---|
| **Artifact** | This fixture's mandatory selection |
| **Reason** | RFC-0001 is indivisible (8,353 w — justified oversize, recorded in `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`, *not* in RFC-0001 itself, which records no waiver), and an identity change genuinely needs the minting/continuity scheme (RFC1-11), the evaluation identity a claim resolves against, the constitutional temporal model, and the floor text it may not weaken |
| **Scope** | Kernel identity and continuity changes — minting, successor edges, split/merge, and the continuity links recorded across them — **where CC-BAR-5 floor 7 is the declared classifier**. Does **not** cover: the adoption ceremony for such a change (RFC-0003 stays deferred to that packet, as this fixture already rules); `.syzygy/**` schema migrations that do not alter minting; changes to challenge, reconciliation or rendering semantics, which pull further RFC-0002 modules and must be re-measured (scope tightened by RC-12) |
| **Reviewer** | **RC-12, independent reviewer, 2026-08-06.** Ruled `WAIVER SOUND` in `../round-2026-08b/reviews/RC-12-budget-waiver-RAW.md`, over the *selection* — not over the contracts it selects. That review's own verdict was `EXCEPTIONS`; read §5 there on what this signature can and cannot mean while no budget rule is installed |
| **Expiry / revisit trigger** | The **earlier** of (a) the first real kernel identity work item, or (b) **any change that makes RFC-0001 divisible** — a package split, or the focused decomposition review §11.4 already calls for and CG-8 already reports. RC-12 holds (b) to be the operative condition: 53% of this packet is that one file, so if it becomes divisible the justification is void rather than weakened. Mandatory re-review at expiry; this waiver does not auto-renew. Also reversible by one owner ruling — see the alternative below |
| **Decomposition reviewed** | Two splits examined. (a) Drop `craft:engineering-bar.md` if the owner rules that a floor cited to *classify* a change is not text the implementer must hold: the packet returns to **14,485 w ≈ 19,554 est. tokens**, inside the trigger and 446 tokens under it. (b) Drop `RFC-0002/README.md` (an index): **13,949 w ≈ 18,831**. Neither is proposed as the default — (a) removes the only statement of the obligation the change can violate, and (b) removes the deterministic clause-lookup rule that makes a cited `RFC2-n` resolvable without search |

## Omitted applicable candidates, with reasons

- RFC-0002 `challenge-lifecycle`, `reconciliation-chain`,
  `rendering-vocabularies` — these *consume* identity, they do not define
  it; loaded only if the change alters challenge, reconciliation, or
  rendering semantics. Moved to suggested below.
- RFC-0003 `governance-homes-and-owner-acts` + README — **an explicit
  departure from the load map's reader map**, which lists governance-homes
  for a "kernel implementer" (`06-CONTEXT-LOAD-MAP.md`). The reader map
  describes the kernel *implementation* role; this work item drafts the
  identity-scheme change and performs no owner act, so the registry's act
  machinery is deferred to the adoption task — fixture 3's rule, applied to
  the kernel ("when the adoption ceremony becomes the task, that packet
  loads it"). Suggested below, so the departure is visible rather than
  silent.
- RFC-0003 `manifests-and-namespace` — storage namespace, not entity
  identity.
- RFC-0004/0005/0008 — evidence capture, execution, and work-state contracts
  consume kernel identities; none defines minting or continuity.
- Surface RFCs (RFC-0006/0007/0009) — identity is kernel; surfaces project
  it and never fork its semantics (CC-DEP-6, "one kernel").
- RFC-0010/0011 — no mission and no packet compilation in this task.
- doctrine `vision.md`, `v1.md`, `security.md`, `trust-and-evidence.md`,
  `README.md` — the constitutional identity and temporal model this change
  must not contradict lives in `architecture.md`, which is loaded;
  `trust-and-evidence.md` governs the claim/evidence seam, and this change
  alters what an identity resolves to, not what warrants a claim. No
  doctrine file is left unaccounted for.
- Craft policies other than `engineering-bar.md` —
  `interfaces-and-dependencies.md` carries CC-DEP-2/3, the design duties
  floor 7 points at, but CC-DEP-2 defers the identity scheme itself to
  RFC-0001 ("per the scheme RFC 0001 will fix"), which is mandatory-loaded
  in full; suggested below. The remaining policies bind observability,
  performance, provenance, review, secrets, and testing duties this drafting
  task does not exercise.
- Topology bundle (`.syzygy/map/topology-candidates/**`) — candidate
  material that binds nothing; no placement changes. Named so the absence is
  a decision.
- `history/**`, `_bootstrap/**` — historical lane, never a default reading
  path, never authority.

## Why no applicable constraint was lost

The minting rule and its successor-edge semantics (RFC1-11, with the
`succeeds` relation's derived/declared split), the identity classes the
change re-shapes (RFC-0001 §3.3), the evaluation identity a claim resolves
against (RFC-0002 `snapshot-and-evaluation-core`), the constitutional
identity/temporal model (`architecture.md`), and the floor the change may
not weaken (CC-BAR-5 floor 7) are all mandatory-loaded. RFC-0001 and
RFC-0002 each travel with their governing phase rule (RFC11-4's
mandatory-inclusion rule): RFC-0001 is a single file carrying its own, and
the selected RFC-0002 README carries the package's — no loaded contract's
boundary rule is missing.

**Index cross-check, with its limit stated.** Every RFC clause the warrant
cites resolves through `05-CONTRACT-INDEX.yaml` into the mandatory or
suggested set. The index's `governance_sources`
list was empty when this fixture was first written (it enumerated packet
copies removed in the tracked-home move); the generator was repointed at the
canonical homes later in the same round, so the projection now carries the
doctrine and craft sources and this cross-check resolves against it. The
doctrine and craft selections above were additionally verified against the
files directly.

## Suggested inferred additions (provenance: index adjacency)

RFC-0003 `governance-homes-and-owner-acts` + README (5,334 words) — needed
the moment the change's adoption ceremony, rather than its design, is the
task. `craft:interfaces-and-dependencies.md` (1,059 words) — CC-DEP-2/3,
the storage/interface duties floor 7 references, for the implementer who
will carry the scheme into a `.syzygy/**` migration. RFC-0002
`challenge-lifecycle` + `reconciliation-chain` (4,708 words) — only if the
identity change alters what a challenge or reconciliation chain resolves to.

## Packet digest

sha256 over the mandatory files concatenated in listed order:
`994da8548bb350dc…` (recompute: `cat <mandatory files> | sha256sum`).
Compiler: `context_load.py`, selection rules rev10-fixtures.

**Digest-source pinning.** This digest and the totals above are computed over
the **canonical-home bytes** as of 2026-08-05: `doctrine:` resolves to
`.syzygy/governance/doctrine/`, `craft:` to
`.syzygy/governance/policies/craft-and-care/`, `rfcs/` to this package. No
packet copies of doctrine or craft exist under this root any more, so there
is exactly one resolution and no silent source swap. A packet pins the exact
source digests it compiled from precisely so that a later change — a D3
adoption amending `architecture.md`, a craft amendment such as CC-TEST-2, or
any corpus edit — **invalidates this packet rather than silently changing
what it meant**. A stale digest is the correct, visible outcome. (Live
proof: three accepted-set fixtures no longer reproduce their stated digests
after the P-6 and P-7 fixes — see the fixture report.)

## Verification checklist (§15)

- [x] **All mandatory context included** — the minting/continuity contract,
      the evaluation identity, the constitutional model, and the floor text
- [x] **Unrelated modules excluded** — **29 of 32** RFC modules absent
      (3 loaded; count computed from `05-CONTRACT-INDEX.yaml`'s module list,
      not estimated)
- [x] **Stable output for identical inputs** — same argument list, same
      totals; re-run with arguments reversed returns the same total
- [x] **Budget respected or waiver emitted** — **not respected: 21,285 est.
      tokens breaches the 20,000 trigger**; justification emitted above,
      reviewer unassigned, two decomposition options measured
- [x] **Omissions recorded** — every applicable candidate above is
      enumerated with a reason, including all doctrine files, all craft
      policies, topology, and the historical lane
- [ ] **No generated summary replaces exact authority** — *not verifiable by
      the script.* The fixture names files; nothing checks that a consumer
      read the clause rather than an index or its own summary. See the
      fixture report's §5.

**Reviewer note.** This is the largest defensible mandatory set among the
three candidate fixtures, and it is driven by RFC-0001's indivisibility: the
kernel is one 8,353-word file with no honest split (the oversize waiver is
recorded in `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`; RFC-0001 itself
records none). Any task touching identity therefore starts at ~11,300
estimated tokens before a second module loads. That is a **structural
property of the corpus**, not a selection defect — and it is why the floor
text, at 1,282 words, is what tips this packet over a line.

*Re-measured 2026-08-05b by `scripts/check_governance.py` CG-18, which recomputes the digest and the word count from the declared mandatory set rather than trusting the recorded figures. Previous: 15,767 words, digest `4de5ebff52463686…`. Selection unchanged; the movement is contract edits landing under a fixture that had no mechanical freshness check until now.*
