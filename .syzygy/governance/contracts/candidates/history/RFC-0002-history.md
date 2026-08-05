# RFC-0002 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
the four-module package `../rfcs/RFC-0002/` — index and clause map in its
`README.md`; clauses live in `snapshot-and-evaluation-core.md` (RFC2-1..11),
`challenge-lifecycle.md` (RFC2-12..14), `reconciliation-chain.md`
(RFC2-15..22), `rendering-vocabularies.md` (RFC2-23..25). Full review corpus:
`_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0002-observation-evaluation-reconciliation.md`.

Entries are keyed by clause ID. Text inside `*(History: …)*` is copied
verbatim from rev9.

---

## RFC2-1 — source snapshot, item 11

*(History: added at the rev8 final review — the rev8 rework made effective
status an act-record-derived fact, and the input that decides it belongs on
the list that exists to make such inputs impossible to forget.)*

**Compaction note.** The active clause now says only "item numbers are
load-bearing and cited elsewhere — never renumber"; the eleven items
themselves are copied verbatim and unchanged.

## RFC2-4 — degradation-only rule

Rev9 justified the fifth authoritative input (an adopted governance or spec
artifact change) at length; the active clause keeps the enumeration and a
one-clause reason. The dropped reasoning, verbatim:

> the fifth is this RFC's explicit enumeration, matching the resolution routes
> RFC2-24 gives reasons #1, #3 and #7 and the "intent edit" reopening input of
> RFC2-22 — an adoption is not a "recorded decision" in the RFC2-15 dismissal
> sense, and leaving it implicit invited two implementations to differ on
> whether a policy edit may un-Unknown a claim class.

## RFC2-13 — challenge lifecycle

**On making admission mechanical** *(rev9 parenthetical, verbatim):*

> *(Deliberate adjustment: doctrine makes conservative suspension the default
> for an open inferred challenge but names no admitting authority. Making
> admission mechanical and recorded avoids an unbounded `submitted` limbo that
> quietly narrows the suspension default.)*

**On admission authority (owner decision B2).** Rev9 records the split as
*"ruled at acceptance by owner decision B2, amending the drafted
uniform-mechanical position."* The drafted position — uniform mechanical
admission for every challenger — was superseded at acceptance. The
justification for the asymmetry is a security premise and stays in the active
clause.

**On expiry** *(rev9 parenthetical, verbatim):*

> *(Deliberate adjustment from the first draft, which let expiry act at the
> instant; §8 q2, and routed to the acceptance packet.)*

**On the sweep policy** *(rev9 parenthetical, verbatim):*

> *(History: added at acceptance by owner decision B1).*

Rev9's closing sentence on the requirement, dropped from the active clause as
duplicative: *"and 'eligible' degenerates into no-expiry with extra
vocabulary."*

**On provider revocation.** Rev9 notes the ruling was *"moved here from
RFC5-13 so that the challenge lifecycle is complete where it is defined."*

**On the pre-admission window.** The name `challenge-pending`, and its
categorisation as neither a tier nor a sibling surface state, are this RFC's
(rev8/rev9 work); the underlying rendering obligation — that a `submitted`
challenge is disclosed on the claim and suspends nothing — is the clause's
original text.

## RFC2-17 — reservation of the words

The substrate survey behind the reconciliation reservation is archived corpus
and informative only: `06-TRAJECTORY-BRIEF` §2; `04` §3.5. The rule stands
without it.

## RFC2-18 — the reconciliation chain

**On the paired state (answer to §8 q4).** Rev9's rationale for the pairing
obligation, dropped from the active clause (the obligation itself stands):

> [Inferred] Both facts are true and dropping either would be a lie, so the
> binding is unchanged; what the pairing fixes is that "fully reconciled" and
> "gap-ridden" sitting side by side with no stated relation is the single most
> confusing thing a new reader encounters, and a reader who cannot reconcile
> them concludes the surface is broken rather than that intent moved.

**On the record type.** Rejecting a dedicated reconciliation-record type cites
archived corpus `06` §5.2 — informative only.

## RFC2-24 — the Unknown-reason vocabulary

Base of seven reasons from the archived corpus (`07-ORRERY-BRIEF` §6 —
informative only); reasons #9, #10, #11 added during drafting/review and #12
at acceptance. Per-reason amendment narrative, verbatim from the rev9 table
cells (the Condition and Resolution-route text itself is copied unchanged into
the active file):

- **#3 `no-currency-bound-declared`** — *Added:* doctrine states this case
  separately from staleness, and its resolution is a governance act, not fresh
  evidence [Observed — trust-and-evidence.md]
- **#6 `unconsented-source-or-provider`** — *Renamed* from "unconsented
  repository/provider" to include model providers explicitly
- **#9 `challenge-suspended`** — *Added:* a challenge is neither a
  contradiction nor missing evidence — the deterministic basis exists and stays
  visible; folding it into #8 would misroute resolution (adjudication vs
  challenge lifecycle)
- **#10 `source-uncaptured-or-unreachable`** — *Added:* the closed snapshot
  rule names this outcome and its diagnosis differs from #2 — the input was
  never in the evaluation, versus present-but-unevidenced
- **#11 `reference-unresolvable`** — *Added post-draft:* driven by four
  independent findings — RFC 0006 §5 (defect note) and its §8 q3, RFC 0007 §5
  item 2, RFC 0008 §5 defect 5's cross-reference, and this review's K-R18. #1
  implies no declaration ever existed and #10 implies a capture failure, so
  both misroute the diagnosis; the same routing argument justifies #9 and #10.
  Flagged for owner confirmation at §8 q1(a) — the owner may strike it at
  acceptance
- **#12 `execution-blocked`** — *Added at acceptance by owner decision (A5).*
  Chosen over annotating #2 with a secondary: a reason names what would resolve
  it, and "go capture evidence" misdescribes the remedy when the capture path
  is the thing that is blocked. Because the secondary vocabulary **is** this
  list, the pre-acceptance drafting had no lawful value to annotate with —
  RFC5-18's "secondary reason" had no referent, which is why this addition and
  not the annotation is the honest fix

Rev9's closure sentence, dropped as duplicative in the active preamble:
*"leaving it unstated is how the value gets chosen by whoever implements the
render first."* (Retained in the active file.)

## RFC2-25 — the rendering-tier registry

**`editorial-draft`** *(History: minted at acceptance by owner decision B10,
discharging RFC 0007 §5 defect 1.)*

**`asserted-by-worker`** — rev9 cites the T-F9/R-11 disposition for "never a
status input"; the disposition record is in the archived review corpus.

## §5 — integration

Rev9 additionally cited SDR §5 q2–3 alongside SDR-2 for durable identity
minting, and repeated that the temporal/epistemic contract "is self-standing
without" sibling drafts. Both are preserved in substance in the active §5.

## §6 — Alternatives considered (moved wholesale)

- **Fourth label for worker assertions.** Rejected: the three-label rule is
  exclusive by adopted doctrine; the reviewer already caught this drift
  (T-F9); tier-within-Inferred preserves honesty and the closed labels.
  *(Load-bearing — one sentence retained in the active §6.)*
- **Keeping the research's seven Unknown reasons unchanged.** Rejected: three
  doctrine-named conditions (undeclared bound, challenge suspension,
  uncaptured source) would be forced into reasons with the wrong resolution
  routes, breaking the rule that makes a grey map diagnosis, not breakage. A
  fourth condition — a broken internal anchor over a captured source (#11) —
  was added post-draft on the same argument, and is flagged for owner
  confirmation (§8 q1(a)).
- **A dedicated reconciliation-record type.** Rejected: the verdict is an
  ordinary claim instance of an ordinary evaluation; a new type would
  duplicate observation-record semantics and invite a second store (`06` §5.2).
- **Auto-triggering reconciliation on merge events.** Rejected: the loop is
  human-triggered by doctrine; automatic evaluation is unattended computation
  over possibly-unconsented, possibly-stale inputs.
- **Evaluating reconciliation against current intent** as the chain's binding
  verdict (kept available as a separate *claim within the same evaluation*,
  RFC2-18). Rejected: post-merge spec drift would retroactively falsify
  finished work, conflating gap (new delta) with unsatisfied warrant (work
  never satisfied what warranted it). *(Load-bearing — one sentence retained
  in the active §6.)*

## §7 — deferrals

The captured-execution-evidence deferral carries the lineage tag
**FRC-04-3 / FR-T5** in rev9; the position (follow SDR-8, take no position on
a doctrine amendment) is unchanged in the active file.

## §8 — acceptance questions (all five answered; moved wholesale)

Question text is verbatim from rev9; the `> **ANSWERED**` blocks are verbatim.

### q1 — Reason granularity (RFC2-24)

> 1. **Reason granularity (RFC2-24).** Two sub-questions on the closure.
>    **(a) Reason #11 `reference-unresolvable` is a post-draft amendment**
>    added under review, driven by four independent findings (RFC 0006 §5 and
>    its §8 q3, RFC 0007 §5 item 2, RFC 0008 §5 defect 5, and review 2's
>    K-R18): a captured source whose declaration exists but whose cited
>    internal anchor no longer resolves has no honest home among #1–#10.
>    Confirm the eleventh reason, or strike it and direct that the case map to
>    an existing reason. **(b)** Should #10 split observer-failure from
>    source-unreachable (two resolution owners: Syzygy's observer vs the
>    project's source)? One reason is proposed because both resolve through
>    "repair, then new snapshot." *(Two further vocabulary strains are
>    deliberately left unamended and remain open, and neither is currently
>    answered by adding a reason here. **Blocked execution:** RFC5-18 renders
>    it Unknown — `missing-evidence`, with the blocked execution disclosed as a
>    fact of the render rather than as a reason, since the secondary-annotation
>    closure stated in RFC2-24 admits no value outside this list; RFC 0005 §8
>    q3 poses the alternative — a further **primary** reason
>    `execution-blocked` — and should be answered together with this question,
>    because a primary addition is an amendment to this closure. **A substrate
>    value outside a declared derivation mapping:** RFC8-14 does **not** map it
>    to `missing-declaration` — it renders the raw substrate status with the
>    state-local absence value `state-undetermined`, which RFC8-14 declares is
>    not an RFC2-24 reason, is never stamped with one, and is never counted
>    among a project's Unknown-reason totals. RFC 0008 §8 q7 is the live
>    question on that field: confirm `state-undetermined`, or direct that the
>    case take an RFC2-24 reason instead — which would make a board-state field
>    claim-bearing and let its counts enter this vocabulary's totals.)*
>
>    > **ANSWERED at acceptance — A5.** The list grows to **twelve**: #12
>    > `execution-blocked` added, #11 `reference-unresolvable` retained. This
>    > settles RFC 0005 §8 q3 (a **primary** reason, not a secondary
>    > annotation) and RFC 0008 §8 q7 (unmapped substrate status stays #1
>    > `missing-declaration`) together, as the coupling required.

**Compaction note on q1(b).** A5 does not name the observer-failure /
source-unreachable split explicitly; it closes the list **at twelve** with #10
intact, which resolves (b) as "not split". The active RFC2-24 states this as
"#10 not split" rather than leaving it ambiguous. Flagged in the compaction
report as the one inference drawn from an answer's scope.

### q2 — Challenge expiry (RFC2-13)

> 2. **Challenge expiry (RFC2-13).** The doctrine constraint first, because it
>    narrows the choice: **automatic expiry-at-instant is not available.** An
>    admitted challenge that un-suspended its claim the moment a declared
>    expiry passed would *improve* a claim over an unchanged snapshot by pure
>    passage of the as-of instant — precisely what RFC2-4 and architecture.md's
>    degradation-only rule forbid (dismissal expiry is safe only because it runs
>    the other way, degrading). The owner's real choice is therefore two-way:
>    **expiry as eligibility**, as now drafted — an expiry-eligible challenge
>    keeps suspending until a recorded human act or a pre-declared deterministic
>    policy sweep resolves it as `expired`, that act entering a new snapshot —
>    or **no expiry at all**, challenges living until resolved, since resolution
>    is already a permitted new-snapshot input. Proposed: eligibility. It keeps
>    the hygiene benefit at the price of one recorded act per lapsed challenge;
>    the alternative costs nothing but leaves stale suspensions standing.
>
>    > **ANSWERED at acceptance — B1.** Expiry stays **eligibility only**, and
>    > a **declared sweep policy is now required** wherever expiry is declared;
>    > an undeclared sweep is not a permissive default — eligible challenges
>    > continue to suspend. The sweep policy is authorization-bearing under
>    > RFC3-16(a).

### q3 — Reconciliation evidence class

> 3. **Reconciliation evidence class:** is gate-backed Observed (RFC2-25) too
>    strict for `reconciled@E` on doc-only or governance-only work, where the
>    "gate" is a deterministic diff-satisfies-clause check rather than a test
>    run? Proposed reading: the check's retained output *is* the gate artifact.
>
>    > **ANSWERED at acceptance.** Yes — a **deterministic, re-runnable
>    > diff-satisfies-clause check** is a lawful `gate-backed` route for
>    > doc-only and governance-only work, added as RFC4-13 **route 4**. Coupled
>    > to A2 as flagged. *(Rev7 rework, directive item A5 — not owner decision
>    > A5: route 4 now requires a **governed checker** — a lawfully adopted
>    > checker definition plus an execution artifact binding exact inputs and
>    > revisions, RFC4-13(b); determinism alone no longer suffices.)*

### q4 — Binding to the warranted intent revision (RFC2-18)

> 4. **Binding to the warranted intent revision** (RFC2-18) means a project can
>    be simultaneously fully-reconciled and gap-ridden after an intent edit. Is
>    that rendering acceptable at V1, or must Trajectory always co-render the
>    current-revision claim (which RFC2-18 now places inside the *same*
>    evaluation, not a second one)?
>
>    > **ANSWERED at acceptance.** The warranted-revision binding **stands**;
>    > the two claims must render as **one paired state** naming both halves
>    > and what separates them, never as two independent aggregates. See
>    > RFC2-18.

### q5 — Challenge admission (RFC2-13)

> 5. **Challenge admission (RFC2-13).** The first draft named no authority for
>    `submitted → admitted | rejected`. It is now a **deterministic kernel
>    check of the mechanically checkable floor criteria**, recorded in the
>    governed plane, with `submitted` challenges rendered on the affected claim
>    but suspending nothing, and a required declared bound on admission
>    latency. Two things for the owner. **(a)** Confirm this, or require
>    **human admission** instead — safer against inference self-certification,
>    at the price of an owner touch per challenge and a longer non-suspending
>    window. **(b)** Note explicitly what "deterministic" does and does not
>    mean here, since (a) asks you to confirm a *mechanism* and the two senses
>    are easy to conflate. The **act** of admitting is an act recorded as a
>    fact, not a computation: "specific falsifiable concern" and "individually
>    resolvable" involve judgment even when checked only for presence, so two
>    admitters can differ on the same challenge and **no re-computation
>    adjudicates between them** — the act itself is not subject to the VIS-7
>    identity test. The **state** that act produces *is* deterministic relative
>    to the snapshot, because the admission record is a snapshot input (RFC2-1
>    item 9): re-running an evaluation over the same snapshot reproduces the
>    same admission state, and VIS-7 holds over evaluations as usual. RFC2-13
>    now states both senses in the same words. Nothing downstream may assume
>    that reproducing an admission state is evidence the admission was the only
>    one available.
>
>    > **ANSWERED at acceptance — B2, amending the drafted uniform-mechanical
>    > position.** Admission is **split by who minted the challenge**: an
>    > attributed human's challenge is admitted by the deterministic kernel
>    > check alone within the declared latency bound; a challenge minted by the
>    > **declared inference process** additionally requires a **recorded human
>    > admission act**. Rationale: admission checks *presence*, never merit, so
>    > a uniform mechanical rule leaves an inference process able to suspend
>    > claims at machine volume with no rate bound anywhere in the contract.
>    > See RFC2-13.

## End marker

> (End marker added 2026-08-02 at the rev7 confirming review's flag — this RFC
> previously ended without one; nothing normative changed.)

## Archived-corpus citations dropped from the active file

All informative only, retained here for traceability: `06-TRAJECTORY-BRIEF` §7
link 11 and `DISPOSITIONS-03` residual risk 1 (the "no substrate provides the
reconciliation evaluation" observation, §1); `06` §2 and `04` §3.5 (RFC2-17
substrate survey); `07-ORRERY-BRIEF` §6 (RFC2-24 seven-reason base and the
Unknown rendering rule); `06` §5.2 (§6 record-type alternative);
T-F9 / R-11 dispositions (RFC2-25 `asserted-by-worker`).
