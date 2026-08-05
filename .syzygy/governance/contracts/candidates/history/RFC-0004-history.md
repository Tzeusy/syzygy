# RFC-0004 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
the four-module package `../rfcs/RFC-0004/` — index, clause map, and lookup
rule at `../rfcs/RFC-0004/README.md`. Entries below are keyed by clause ID;
use the README's clause map to find the module owning any `RFC4-n`. Full
review corpus: `_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0004-observation-sources-evidence-adapters.md`.

`*(History: …)*` text is copied verbatim from the rev9 source. Where the
active file's `[Observed]` label survived but its research-corpus citation was
stripped (charter: no `_bootstrap/` paths in active normative text), the
citation is recorded here under the owning clause so the provenance is not
lost. The research-corpus documents are
`04-OBSERVATION-AND-FLEET-EVENT-BRIEF` and `06-TRAJECTORY-BRIEF` — a
**non-authoritative substrate audit**, findings adopted only where the rev9
text cited them.

---

## §2 — Motivation and doctrine grounding (narrative moved from the active file)

Verbatim, rev9 §2 paragraph 2:

> The research corpus's audit of the actually-installed actuator toolchain
> found the substrate both richer and more forgetful than assumed: no run
> identity, model, runtime, timestamp, or cost is recorded anywhere; gate
> results are LLM assertions with no retained artifact; the squash-merge plus
> post-closure branch deletion path destroys per-commit evidence exactly when
> a work item closes; and `bd gc`/`bd prune` delete closed issues and their
> events on an undeclared horizon [Observed: `04-OBSERVATION-AND-FLEET-EVENT-
> BRIEF` §5; `06-TRAJECTORY-BRIEF` §8.2 — non-authoritative substrate audit,
> findings adopted here where cited]. The owner resolved the resulting scope
> and posture questions: post-hoc telemetry enters V1 (SDR-5), the Execution
> Record is an Evidence artifact and no new doctrine class (SDR-8),
> observation is derivation-first (SDR-31), anchors resolve or render Unknown
> (SDR-32), and fidelity loss is labeled, never papered over (SDR-33). This
> RFC turns those rulings into a binding contract.

The active file retains the SDR ruling list, the doctrine-grounding
[Observed] claims, and the `confident adapter` [Inferred] failure mode; only
the audit detail moved. Each audit finding is separately restated, with its
own [Observed] label, by the clause that depends on it (RFC4-11, RFC4-13,
RFC4-16, RFC4-19, RFC4-23).

---

## RFC4-3

Rev9 citation, stripped from the active label: `[Observed: evidence
definition, trust-and-evidence.md; the distinction is `04` §4's, adopted as
binding]`. The active file keeps `[Observed: trust-and-evidence.md]`. The
"distinct from any instant the source itself claims" distinction is `04` §4's,
adopted as binding.

## RFC4-5

Rev9 adoption note, removed from the active clause header: `[adopted from `06`
§5.2, which proposed it; the wording here is normative]`.

The [Inferred] inward-limb clarification (captured evidence about the past is
not a second source of truth) was added because the limb and RFC4-16(2)'s
capture duty read as opposed without it. The clarification is retained in the
active file — only this origin note moved.

## RFC4-6

Rev9 citation: `[Observed: `04` §4 `work_item_id`/`bead_id` analysis]`,
supporting the substrate-qualified-alias rule.

## RFC4-11

Rev9 citation for the squash-merge fidelity finding: `[Observed: `04`
§5.4(a)]`.

## RFC4-13

Rev9 predicate header, verbatim:

> *Provenance predicate on `gate-backed` (post-draft amendment under review
> 3's AS-R3; routes confirmed and bounded at acceptance by owner decision A2,
> route 4 added by the same decision).*

Route 3, verbatim: *(History: bounded at acceptance.)*

Route 4, verbatim: *(History: added at acceptance, answering RFC 0002 §8 q3;
hardened at the rev7 rework, blocker A5.)*

Origin of the whole predicate — rev9 §6 "Post-draft adjustments (review 3)",
verbatim:

> - **`gate-backed` on retention and format alone** — the draft's original
>   test, which discriminated on the *artifact's* properties (retained,
>   resolvable, revision-bound) and not on any attestation that a gate
>   actually ran. Rejected under AS-R3 and replaced by RFC4-13's
>   three-route provenance predicate. An untrusted fleet worker (SEC-3's
>   actor class, extended to committed artifacts at RFC3-16(a)) could
>   otherwise write a well-formed report naming the exact revision and have it
>   enter at the one tier RFC2-25 lets support a positive status claim —
>   and RFC5-19's "observation, not execution" boundary means the profile
>   floor that would have capped a Syzygy-launched policy-violating run never
>   applies to reading a file off disk. Craft-and-care's CC-TEST-2 already
>   held this line; RFC4-13 was the weaker text. **Cost, deliberately taken:**
>   projects with no confirmable CI lose green status on gates whose artifacts
>   Syzygy cannot attribute; those claims convert to `report-fact`. Route 3
>   (owner-declared trusted external oracle) is the escape hatch. Routed to
>   acceptance as §8 q6.

*(Note: the paragraph above says "three-route"; the fourth route was added at
acceptance by the same owner decision A2 that bounded route 3. The active
contract carries the four-route model.)*

Rev9 citation for the read-only authority boundary: `[Observed: v1.md V0
scope]` — retained in the active file.

## RFC4-13(a)

Verbatim: *(History: added at the rev7 rework, blocker A3: route 2 as
originally worded left the confirmation an unstored act, which RFC8-27 then
read as re-performable "at read time" — making a stored evaluation's meaning
depend on a mutable external system.)*

## RFC4-13(b)

Verbatim: *(History: added at the rev7 rework, blocker A5: route 4 as
originally worded demanded only determinism and re-runnability, which a
checker whose body is `return PASS` satisfies.)*

## RFC4-15

Rev9 citations, stripped from the active labels:

- authority boundary — `[Observed: architecture.md; `06` §5.3]` (the active
  file keeps `architecture.md`);
- the five-of-seven status-vocabulary drift finding — `[Observed: `06` §3.1]`;
- replace-in-place note fields — `[Observed: `04` §5.1]`.

## RFC4-16

Item 2, verbatim: *(History: post-draft amendment under review 3's AS-R16,
taking §8 q4's stricter option.)*

Rev9 §6 origin of that amendment, verbatim:

> - **Deferring the capture-cadence obligation to policy without requiring
>   a declaration** (RFC4-16, under AS-R16). Rejected: honest degradation that
>   can be perpetually deferred bounds nothing. §8 q4's stricter option is
>   taken — the quality policy must *declare* a maximum inter-pass interval
>   tied to the retention bound. Enforcing it by scheduler was **not** taken:
>   the loop stays human-triggered (architecture.md).

Rev9 citations: the substrate-forgetting findings — `[Observed: `06` §8.2]`;
item 3's Unknown-citing-the-retention-event rule — `[adopted from `06` §8.3's
honest-degradation rule]`.

## RFC4-17

Rev9 citation for the load-bearing-join failure analysis: `[Observed: the
failure analysis in `06` §5.3]`.

## RFC4-19

Field-class rename, verbatim from rev9:

> *(The class was labeled `required-where-available` (RA) in the draft;
> renamed under review 3's AS-N3 because "required where available" states no
> obligation. The rule is unchanged.)*

Rev9 citations inside the table, stripped from the active cells: the
work-item-identity row — `[Observed: vision.md anchoring mandate via `04`
§3.1]` (the active cell keeps `vision.md`); the runtime+model row —
`[Observed: `04` §4]`; the prose-fields row — `[Observed: `04` §4]`.

Rev9 §5 note on why RFC 0005's obligations are carried as rows here rather
than as a cross-reference: "RFC 0005's run-envelope obligations (RFC5-18(e)
profile identity and version; RFC5-21 policy-violation recording) are
**carried as named rows of RFC4-19**, not as a gesture in this section — the
envelope's minimum content is stated in one place (review 3, AS-R9)."

## RFC4-20

Rev9 §6 origin of the `indistinguishable-runs` safeguard, verbatim:

> - **A new `reduced-fidelity` cause, `indistinguishable-runs`** (RFC4-24,
>   under AS-R4). The cause list is closed and extendable only by amending
>   this RFC; this is that amendment, recorded here as a deliberate
>   adjustment. It exists because deterministic derivation of run identity
>   from identical inputs is non-unique across distinct-but-identically-keyed
>   dispatches, and the draft stated no behavior for the collision — so as
>   written it was silent, which is the one outcome VIS-1 forbids. The
>   alternative of leaving the collision to §8 q1's ruling was rejected: the
>   safeguard is normative under *either* ruling.

## RFC4-21

Rev9 citations: the rate-table-drift Inferred labeling — `[Observed: `06`
§6]`; the no-composite-effort-number rule — `[Observed: `06` §6, per the
maturity ruling's logic]`.

## RFC4-22

Rev9 citations for the convention-basis rule: `[Observed: `04` §4 `branch`;
`06` §7 links 6–7]`.

## RFC4-23

Rev9 citation for the no-worker-liveness-signal finding: `[Observed: `06`
§3.2a]`.

## RFC4-24

The active cause list retains `indistinguishable-runs`; the rev9 in-list
attribution "added post-draft under review 3's AS-R4" moved here. See RFC4-20
above for the full origin note.

## RFC4-29

Rev9 citations for the substrate-store routing rule: `[Observed: `06` §5.3
routing note; SDR-8]` (the active clause keeps SDR-8).

---

## §5 — Defects found in the foundations (all four resolved; moved from the active file)

Verbatim from rev9 §5, "Defects found in the foundations (reported, not
silently diverged from)":

> 1. **RFC1-29 / RFC2-18 mismatch — resolved (retained for the trail).** This
>    RFC reported that RFC2-18 required the reconciliation snapshot to include
>    "the exact intent revision … as pinned in the immutable materialization
>    record" while RFC1-29 defined that record as only (proposal identity →
>    work-item identity set). **Satisfied by the RFC1-29 amendment of
>    2026-07-30**: the materialization record now pins the exact warranted
>    intent revision, and RFC1-5's materialization-record row carries it, so
>    this RFC's warrant reference (RFC4-19) rests on a field RFC 0001
>    requires. No RFC 0001 or RFC 0002 change is outstanding on this item
>    (review 3, AS-R8).
> 2. **RFC1-5 "Verification run … run identity + input snapshot identity" —
>    resolved (retained for the trail).** As reported: external CI runs
>    identify the *revision under test*, not a Syzygy source snapshot, so read
>    literally no external run could ever qualify, and this RFC interpreted
>    "input snapshot identity" as the identified revision(s) the run claims to
>    describe (RFC2-11's binding). RFC1-5's Verification run row now states
>    that reading directly — "run identity + **identity of the revision(s)
>    under test (the run's claimed subject, RFC2-11)**" [Observed — RFC1-5 as
>    of 2026-08-01]. No RFC 0001 change is outstanding on this item.
> 3. **RFC1-5 execution-run identity "minted by the actuator toolchain via
>    adapter" — resolved (retained for the trail).** As reported: no run
>    identity exists in the installed toolchain [Observed: `04` §5.3], and a
>    toolchain-only reading would leave these records identity-less until
>    instrumentation lands — contradicting SDR-31 — so RFC4-19 read "via
>    adapter" as licensing a deterministic adapter-derived identity, queryably
>    labeled `derived`. RFC1-5's Execution run row now carries that licence
>    upstream — "**Toolchain-emitted run identity where one exists, else
>    adapter-derived deterministically and labeled `derived`**" [Observed —
>    RFC1-5 as of 2026-08-01]. No RFC 0001 change is outstanding on this item;
>    what the owner still rules is *whether* to derive at all (§8 q1), not
>    whether RFC 0001 permits it.
> 4. **RFC1-6 delegates "first-class VCS entities" to RFC 0004 — resolved
>    (retained for the trail).** As reported: RFC1-5 closes the V0-core
>    vocabulary, which only an RFC 0001 amendment can reopen, so the
>    delegation as written granted a power RFC1-5 reserves (no conflict
>    materialized — this RFC declines the delegation, §6). RFC1-6 now closes
>    the grant in its own text: first-class VCS entities "enter only through
>    an amendment to this RFC informed by RFC 0004's findings — RFC 0004
>    itself declines to mint them; **RFC1-5's closure is reopened by amendment
>    here, never by delegation**" [Observed — RFC1-6 as of 2026-08-01]. No
>    RFC 0001 change is outstanding on this item.

The active file's §5 retains the resolution statement and backlinks here.
Defect 4's live consequence — this RFC mints no VCS node types — is retained
in the active §6.

---

## §6 — Alternatives considered (moved wholesale)

Verbatim from rev9 §6:

> - **A new doctrine-level "captured execution evidence" class** (the research
>   corpus's FRC-04-3 recommendation). Rejected by SDR-8, followed here: the
>   Execution Record is an Evidence kind; the immutability and identity rules
>   the proposed class wanted are delivered by RFC4-18/19 without a doctrine
>   amendment or a new frozen noun.
> - **Requiring toolchain instrumentation for V1** (FRC-04-5 option ii as a
>   dependency). Rejected by SDR-31: derivation-first is the invariant;
>   enrichment is a named roadmap. The reverse — derivation-only forever —
>   is equally rejected: it would freeze model, cost, and liveness at Unknown
>   permanently and forfeit the co-evolution the owner controls.
> - **Primary run-record storage in the substrate's typed event store**
>   (`bd --type event`). Rejected: Syzygy-authored durable records inside a
>   scheduler-owned, GC-governed store invert the authority split (SDR-7/8)
>   and put the fleet account under a retention horizon Syzygy does not own
>   (RFC4-16). Permitted only as outward-limb pointers/enrichment.
> - **Accepting worker report assertions as gate-backed Observed** because the
>   report is machine-formatted. Rejected: the emit script formats the claim,
>   it does not verify it; an LLM assertion is Inferred, never Observed
>   [Observed: trust-and-evidence.md] — SDR-9 and RFC2-25 already draw the
>   line this RFC enforces at the observer.
> - **Hardcoding the scheduler status vocabulary** in the adapter. Rejected:
>   the substrate's statuses are configurable and already drift from the
>   toolchain's own docs; reading the vocabulary from the tool is the only
>   form that survives substitution (RFC4-9).
> - **Autonomous event-time capture daemons** to beat the squash-merge and gc
>   horizons. Rejected: the loop is human-triggered [Observed:
>   architecture.md]; the honest alternative is capture-before-horizon inside
>   triggered passes plus labeled reduced fidelity when the horizon won
>   (RFC4-16, RFC4-24).
> - **First-class VCS entities** (commit/ref nodes). Declined: commits and
>   PRs serve every current need as evidence artifacts and join fields
>   (RFC1-6, RFC1-25); adding node types would reopen RFC1-5's closed
>   vocabulary for no query this RFC needs.

The three "Post-draft adjustments (review 3)" entries are reproduced above
under their owning clauses: `gate-backed` on retention and format alone →
RFC4-13; the new `indistinguishable-runs` cause → RFC4-20; deferring the
capture-cadence obligation → RFC4-16.

The last alternative (first-class VCS entities) is the one the active §6
keeps a sentence of, because RFC1-6's delegation is only readable against this
declension.

---

## §8 — Answered owner questions (numbering preserved in the active file)

### q1 — Adapter-derived run identity (RFC4-19)

Rev9 question text, verbatim:

> 1. **Adapter-derived run identity (RFC4-19).** Where the toolchain emits no
>    run identity, this RFC has the adapter derive one deterministically,
>    labeled `derived`. The alternative — run identity renders Unknown and
>    records join on (work item, capture) only — is more austere and makes
>    multi-attempt accounting near-impossible. Confirm derivation, or direct
>    austerity? **The collision safeguard is not part of this question.**
>    RFC4-20's rule — a derivation collision renders `reduced-fidelity` with
>    cause `indistinguishable-runs` and the run count Unknown, never a silent
>    single record — is normative *whichever way this is ruled* (review 3,
>    AS-R4); ruling austerity narrows what is derived, it does not remove the
>    obligation to disclose what could not be distinguished.

Answer, verbatim:

> > **ANSWERED at acceptance — B11.** **Derive, and disclose collisions.** Run
> > identity is derived from what the adapter can see; where two runs collide,
> > the surface renders an `indistinguishable-runs` marker with an Unknown
> > count. Austerity (Unknown identity) is not taken — but the collision
> > safeguard is normative either way: **never a silent single record**.

### q5 — Defect resolutions (§5)

Rev9 question text, verbatim:

> 5. **Defect resolutions (§5) — all closed; confirmation, not a decision.**
>    Every defect this RFC reported against RFC 0001 has since been fixed in
>    RFC 0001's own text: the RFC1-29 pinned-intent-revision gap by the
>    amendment of 2026-07-30 (§5 defect 1, AS-R8), and the RFC1-5
>    verification-run wording, the RFC1-5 execution-run identity licence, and
>    the RFC1-6 delegation overreach in the drafts under review (§5 defects
>    2–4). **No RFC 0001 touch-up remains outstanding, and this item blocks
>    nothing at `ACCEPT FOUNDATIONAL RFCS`.** What is left is confirmation:
>    the interpretations this RFC stated are now RFC 0001's normative wording,
>    so accepting the pair accepts them as the reading of record. Confirm —
>    or, if any of the four upstream amendments reads as having gone further
>    than the defect it closes, name which.

Answer, verbatim:

> > **CONFIRMED at acceptance — all §5 defects closed.** *Recorded here because
> > a stale confirmation is how a fixed defect becomes a live question:* during
> > packet assembly the lead raised a decision item from this question's
> > earlier wording ("what remains for an RFC 0001 touch-up") **without
> > checking RFC 0001's current text**. All three reported defects were already
> > fixed. The item was **retired, and the retirement recorded rather than
> > deleted** — it is the same failure as a stale defect report, one layer up,
> > and the clearest evidence for why the defect-freshness sweep exists.

### q6 — The `gate-backed` provenance predicate (RFC4-13)

Rev9 question text, verbatim:

> 6. **The `gate-backed` provenance predicate (RFC4-13) — added post-draft
>    under review 3's AS-R3.** `gate-backed` now requires a qualifying
>    provenance route, not merely a retained revision-bound artifact. **The
>    cost is real:** a project whose CI Syzygy cannot independently confirm,
>    or whose gate artifacts are written by the worker that ran them, loses
>    green status on those gates — the claims convert to `report-fact` ("an
>    artifact asserting Y exists"), which per RFC2-25 supports nothing
>    positive. Some currently-plausible green renderings become honest
>    non-green. **Route 3 — an owner-declared trusted-external-oracle
>    policy — is the escape hatch**, and its existence should be confirmed
>    rather than assumed: it lets the owner declare an oracle whose artifacts
>    Syzygy honors at `gate-backed` without independent confirmation, at the
>    owner's risk and under RFC3-16(a). Confirm the predicate and the escape
>    hatch, or direct a narrower closure (e.g. routes 1 and 2 only, no owner
>    override)?

Answer, verbatim:

> > **ANSWERED at acceptance — A2.** All **three** admission routes confirmed,
> > with route 3 **bounded**: an owner-declared trusted oracle is scoped to a
> > named (project, gate class) pair and carries an **expiry**; unscoped or
> > expired, it backs nothing. A **fourth route** is added by the same
> > decision — a deterministic, re-runnable diff-satisfies-clause check, for
> > doc-only and governance-only work. See RFC4-13.

### q2, q3, q4 — still open

Retained in the active file at §8. q4 is a confirmation request over a draft
resolution (review 3, AS-R16), not an answered decision; the interval value it
requires remains an undeclared open default, alongside the retention,
staleness, and currency bounds.

---

## Compaction notes (rev10)

- No clause was merged, retired, or renumbered. The active range is
  RFC4-1…RFC4-29 with sub-clauses RFC4-13(a) and RFC4-13(b), no gaps.
- Eight clauses are byte-identical to rev9 after whitespace normalization —
  RFC4-1, RFC4-4, RFC4-7, RFC4-9, RFC4-18, RFC4-25, RFC4-26, RFC4-27 —
  verified by mechanical comparison against the frozen source in the
  compaction session, not asserted. RFC4-28 is verbatim except for one rev9
  line-break artifact (`branch/worktree/` + newline + `commit/PR/merge`) that
  was joined. The remaining 22 clauses were sharpened by removing amendment
  narrative and research-corpus paths only; a keyword sweep over
  must / must not / never / only / forbidden / inadmissible / violation found
  identical counts in every clause, the single exception being one `only`
  inside RFC4-13(b)'s `*(History: …)*` parenthetical, which is preserved
  verbatim above.
- The RFC4-19 envelope table, the RFC4-2 declaration set, the RFC4-13 four
  routes, the RFC4-13(a)/(b) artifact lists, and the RFC4-24 closed cause list
  were copied, not paraphrased.
- Rev9 §3's preamble sentence about `*History:*` parentheticals ("Parentheticals
  beginning *History:* are amendment records … and carry no normative force")
  was dropped from the active file because no such parenthetical remains there
  — they are all in this file.
