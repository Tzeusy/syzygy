# RFC-0005 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
the package `../rfcs/RFC-0005/` — `README.md` (index and clause map),
`admission-and-boundary.md` (RFC5-1..RFC5-11, RFC5-24..RFC5-26),
`consent-egress-secrets.md` (RFC5-12..RFC5-17), `execution-profiles.md`
(RFC5-18..RFC5-23). Full review corpus: `_bootstrap/rfc-phase/reviews/`. Frozen
rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0005-authentication-consent-execution-profiles.md`.

Entries are keyed by clause ID (and by `q<n>` for §8 questions). Extracted
`*(History: …)*` text and answered-question text are copied **verbatim**.

---

## §0 / §1 — reader's summary and summary (rev9 wording)

The rev9 file carried both a "Reader's summary (non-normative)" and a separate
"§1 Summary". They stated the same content at two lengths; at rev10 they became
the package reader map in `README.md` plus a per-module scope section. No obligation lived in either — the
rev9 reader's summary itself said: *"Plain-language orientation. If this section
and a clause ever disagree, the clause wins."*

Rev9 summary sentence dropped as duplicative of §3.2/§3.3 and the q1 scope
ruling: *"It is **contract shape only**: mechanism *classes* are enumerated
(token, mutual TLS, signed request, OS-mediated peer identity;
process/namespace/VM isolation), no product or stack is chosen; the one
enumerated choice left open for acceptance is the machine-client mechanism (§8
q1)."* — retained in compressed form in `README.md`'s reader map and in full
effect at RFC5-7.

## §2 (rev9) — motivation narrative

Moved sentence, retained here for provenance of the RFC 0002 coupling:

> RFC 0002 already depends on this RFC for the consent semantics behind Unknown
> reason #6 and for "execution profiles gating fresh verification evidence"
> [Observed: RFC 0002, Integration].

The package states the dependency once, in `README.md` §5 Integration.

---

## RFC5-3 / RFC5-5 — rev10 scoping addition (not a history extraction)

New at rev10 under `REV9-FINAL-PRESPEC-DIRECTIVE.md` §2 and owner direction
record OD-R10-5. The directive text authorising it:

> Also close or explicitly scope any RFC 0005 machine-client question that
> becomes foundational to the official CLI/MCP clients. It is acceptable to
> leave the concrete credential technology open, but the
> browser-versus-machine-client contract and authentication requirement must be
> closed enough to specify Mission Control truthfully.

Nothing in RFC5-3 or RFC5-5 was weakened, replaced, or removed; the rev9 clause
text is retained in full and the exhaustiveness statement is additive. Rev9
RFC5-3 and RFC5-5 were silent on whether a later contract could add a third
client class — the rev10 addition closes that silence rather than reversing a
prior ruling.

## RFC5-4 — session identity (owner decision B9)

Rev9 parenthetical, verbatim:

> *(ruled at acceptance by owner decision B9, answering §8 q2.)*

Rev9 wording of the declining sentence, verbatim:

> This is the strictest reading of SEC-1's "by credential presented, never by
> network location", and it declines the overlay-network device-identity
> exception §8 q2 offered rather than taking it.

The consequence (declared maximum session lifetime; immediate owner-initiated
revocation as the **entire** remaining mitigation) remains normative in the
active RFC5-4 and was not moved here. See also §q2 below.

## RFC5-11 — the rendering obligation and the forced evaluation

Rev9 amendment marker, verbatim:

> **The rendering obligation** (RFC5-11, amended in place) *— post-draft
> amendment under review 3's AS-R6.*

Rev9 parenthetical on the strengthened form, verbatim:

> *(strengthened at acceptance by owner decision B4, taking the stronger form §8
> q6 offered.)*

Rev9 reconciliation essay, moved here; its operative conclusion ("the security
act *schedules* an evaluation, it does not mutate a claim") is retained in the
active clause:

> **This does not weaken RFC2-4, and the distinction matters.** A security act
> still changes no claim's value directly; it **schedules an evaluation**, and
> the value changes inside that evaluation over a new snapshot that carries the
> revocation record as an authoritative input — exactly the permitted
> improvement route RFC2-4 names. What the draft got right is preserved: nothing
> is recomputed outside an evaluation. What it left open was the *duration* of
> the inconsistency, and the answer "until someone happens to evaluate" is the
> state that teaches a reader to distrust the surface — a claim sitting green
> under a withdrawal label for an unbounded time is worse than either honest end
> state.

## RFC5-12 — egress-consent granularity (owner decision B8)

Rev9 parenthetical, verbatim:

> *(History: post-draft amendment under review 3's AS-R10, aligning this bullet
> to RFC5-14's model and keeping RFC3-7's record shape single. The granularity
> question was **answered at acceptance by owner decision B8** — one record per
> (project, provider); the per-repository alternative was declined — see RFC
> 0003 §8 q3.)*

Rev9 bullet also cited `architecture.md onboarding` beside RFC1-3 on the
observation-consent bullet; the active clause cites RFC1-3 only.

## RFC5-14 — classification determinability

Rev9 amendment marker, verbatim:

> *(post-draft amendment under review 3's AS-R5, giving egress the secret rule's
> spine — RFC5-16/17).*

Rev9 [Inferred] wording of the no-floor argument, whose conclusion is retained
in the active clause:

> [Inferred] Without the undeterminable case the highest-embedded-class rule has
> no floor: a step that concatenates identifiers (`code-structure`, consented)
> with an inlined function body (`code-content`, not consented) and cannot say
> which it produced would default to whatever it claimed, and SEC-2's
> per-content-class scoping would be defeated with every RFC5-15 field nominally
> satisfied.

## RFC5-16 — ingest-boundary enumeration and observer policy

Rev9 parenthetical, verbatim:

> *(Enumeration scope and the observer-policy rule: post-draft amendments under
> review 3's AS-R14 and AS-R7.)*

## RFC5-17 — redaction classes and Unknown mapping

Rev9 parenthetical, verbatim:

> *(post-draft amendment under review 3's AS-R12; a scoping fix, **not** a
> vocabulary extension — no new Unknown reason is added, and RFC2-24's closure
> is untouched)*

## RFC5-18 — the execution-blocked reason (owner decision A5)

Rev9 parenthetical and superseded-position essay, verbatim:

> *(History: amended at acceptance by owner decision A5, answering this RFC's §8
> q3 and RFC 0002 §8 q1 together.)* The draft rendered this as `missing-evidence`
> with the blocked execution disclosed as a bare fact of the render, on the
> reasoning that RFC2-24's secondary-annotation vocabulary is closed to the
> primary list and blocked execution was not in it. That reasoning was sound and
> its conclusion was the wrong half of the fork: because the secondary vocabulary
> **is** the primary list, there was no lawful value to annotate with, so the
> honest fix was to amend the list rather than to route around it — which is what
> RFC2-24's own text directs ("the honest move is to amend this list, never to
> annotate outside it"). `missing-evidence` also misdescribed the remedy: it
> sends a reader to capture evidence when the capture path itself is what is
> blocked.

## RFC5-19 — trust distinction; tier clarification

Rev9 clarification marker, verbatim:

> *(clarified post-draft under review 3's AS-R3).*

Rev9 [Inferred] wording, whose conclusion is retained in the active clause:

> [Inferred] Read the other way, this clause would let the profile floor be
> sidestepped entirely — untrusted code writes a report to disk, Syzygy reads it
> as "observation", and the artifact enters at the one tier that can turn an
> indicator green without ever passing the containment that exists for exactly
> that actor.

Superseded owner ruling, preserved: FD-018 ruled "trust assumed" for the owner's
own projects. FD-029 amended it to A6-b (opt-in profiles: isolated credentials,
declared network, resource limits, destructive-op gates), and adopted SEC-3 binds
observed code as untrusted regardless of project ownership. The active RFC5-19
follows the adopted rule, not the superseded ruling.

## RFC5-20 — Syzygy's own interfaces excluded from network policy

Rev9 amendment marker, verbatim:

> *(post-draft amendment under review 3's AS-R2)*

## RFC5-21 — relocation of out-of-purpose credential use

Rev9 parenthetical, verbatim:

> *(relocated here from RFC5-22's enable-able classes under review 3's AS-R13:
> it contradicts RFC5-20's per-credential stated-purpose enumeration, so it can
> never be a capability an owner standing-approves — out-of-purpose credential
> use is a broken contract, not an enabled feature)*

## RFC5-22 — the removed class

Rev9 parenthetical, verbatim:

> *(**Consuming a credential beyond its stated purpose** was listed here in the
> draft and has been moved to RFC5-21's violation set under review 3's AS-R13 —
> it terminates the run and caps its outputs at `report-fact`. It is not an
> enable-able class at any approval level: RFC5-20 requires every injected
> credential to carry a stated purpose, so "use it beyond that purpose" is a
> contradiction of the profile's own declaration, not a capability.)*

## RFC5-24 — injection prohibition widened

Rev9 amendment marker, verbatim:

> *(post-draft amendment under review 3's AS-R2; the draft forbade only adapter
> credentials)*

## RFC5-25 — where the audit trail lives (owner decision A1)

Rev9 parenthetical, verbatim:

> *(History: bound here at the rev7 rework, review 9 finding F1, promoting the
> derived constraint recorded at owner decision A1 from a §8 annotation to
> clause text.)*

The location constraint itself — the audit trail lives **outside `.syzygy/**`
and outside the untrusted actor class's write reach** — is normative and stays
in the active clause verbatim. It is the anchor of RFC 0003's A1 correlation
mechanism.

---

## §6 (rev9) — Alternatives considered, moved wholesale

Three of these remain load-bearing and are summarised in one sentence each in
`../rfcs/RFC-0005/README.md` §6 (6.1, 6.7, 6.8). All eight are preserved here
verbatim.

- **6.1 Network-perimeter trust** (loopback or tailnet membership as identity).
  Rejected — SEC-1 forbids it explicitly; DNS rebinding and arbitrary local
  processes make "local" an attacker class, not a trust class. Tailnet identity
  is retained only for the device-restriction requirement (RFC5-9), never client
  classification.
- **6.2 One monolithic consent record per project.** Rejected — a single grant
  conflates observation, write, egress, and execution, so revoking one revokes
  all or (worse) none; per-class records keep each revocable and renderable
  independently. Cost: more records; accepted.
- **6.3 A "none" isolation class for trusted projects.** Rejected — SEC-3 binds
  "regardless of who owns the project," and its named violation is precisely
  ambient-credential inheritance for convenience. The permissive-profile path
  (RFC5-19) preserves owner autonomy inside the floor.
- **6.4 Following FD-018 literally ("trust assumed" for own projects).**
  Rejected — FD-029 amended it and adopted doctrine supersedes the earlier
  ruling; the owner's actual trade-off is preserved as the recorded, revocable
  permissive profile, not as an ambient exemption.
- **6.5 Routing revocation through evaluations only.** Rejected — it would let a
  revoked credential act until someone triggers an evaluation. RFC5-11's
  acts/claims split keeps RFC 0002's determinism for truth while making
  enforcement immediate.
- **6.6 Choosing the machine-client mechanism now.** Declined — all four
  enumerated classes satisfy RFC5-6, the choice is reversible beneath the
  contract, and stack-neutrality is a bootstrap boundary; acceptance may fix one
  or admit several (§8 q1).
- **6.7 Act-timed re-render on revocation** — path (a) of review 3's AS-R6:
  making a recorded revocation itself force a degrade-to-Unknown *as an act*,
  immediately, outside any evaluation. **Rejected; path (b), the rendering
  obligation (RFC5-11), was taken instead.** Path (a) would let a security event
  change a claim's *value* outside an identified evaluation, which is precisely
  the coupling RFC5-11's act/claim split exists to prevent and which RFC2-4's
  degradation-only, per-snapshot fixed point forbids: truth would become a
  function of when a revocation happened to be recorded, and two runs of one
  evaluation could disagree (VIS-7). Path (b) obtains the security outcome — no
  withdrawn-source content is ever presented as current — by binding the
  *render*, which is not a truth computation. **Cost, deliberately taken and
  stated in RFC5-11:** a residual window exists in which the claim's value is
  still the pre-revocation one, labelled but not yet recomputed; it closes at the
  next evaluation, whose timing the human-triggered loop owns. Routed to
  acceptance as §8 q6 where the owner may take the stronger form.
- **6.8 Patching authorization authenticity per artifact class.** Declined in
  favor of citing RFC 0003's single predicate (RFC3-16(a)) from this RFC's gates.
  Restating the obligation locally at RFC5-12, RFC5-15 and RFC5-18 in different
  words would let the three drift, and would leave any artifact class added later
  unguarded — review 3's named risk 1. One predicate, one home, cited from every
  consuming gate.

---

## Acceptance questions — answered items, moved out of the active contract

Question numbers are RFC-level and immutable (q1…q6). Each answered item keeps a
one-paragraph stub in its owning module; the question as posed and the answer
verbatim live here.

### q2 — Overlay-network device identity for browser sessions (ANSWERED, B9)

The question as posed, verbatim:

> 2. **Overlay-network device identity for browser sessions — a deliberate
>    trade, not a default.** RFC5-9 lets overlay ("tailnet") device identity
>    satisfy the *device-restriction* requirement while still requiring a
>    Syzygy session. The question is whether the **owner-attended pairing act
>    may be waived on the overlay**, letting device identity bootstrap the
>    session. **The trade, stated plainly:** waiving it means a
>    **network-layer identity establishes a Syzygy session**, which softens
>    RFC5-3's and SEC-1's "by credential presented, never by network
>    location" — the very principle §3.2 is built on. It would be a
>    controlled and recorded exception (owner-declared, revocable, on an
>    owner-controlled overlay with device identity and TLS), not an
>    unbounded one; but it is an exception to a doctrine rule, and doctrine
>    rules are the owner's to except. Against that: waiving removes a
>    per-device attended step the owner performs once, on a network the
>    owner already controls. **This RFC proposes no resolution** — the
>    author must not select it (review 3, AS-N4). Rule it either way at
>    acceptance, and the ruling is recorded as the exception it is.

The answer, verbatim:

> > **ANSWERED at acceptance — B9.** The exception is **declined**. Session
> > identity is the credential and nothing else — no device or network-layer
> > binding. Consequence, now binding in RFC5-4: a declared maximum session
> > lifetime (undeclared = no persistence beyond the process) and an immediate
> > owner-initiated revocation capability are the **entire** remaining
> > mitigation.

That consequence is **normative and lives in the active RFC5-4**, not here.

### q3 — Execution-blocked Unknown reason (ANSWERED, A5)

The answer, verbatim:

> > **ANSWERED at acceptance — A5, together with RFC 0002 §8 q1: option B.**
> > RFC2-24 is amended with a **twelfth primary reason**,
> > `execution-blocked`, whose resolution route — unblock or authorize the
> > run — differs from "produce/capture evidence." RFC5-18 is amended to
> > render it. **Option A is superseded.**

The question as posed, verbatim:

> *The question as posed, retained so the trade is legible.* RFC2-24 states
> that the **secondary**-annotation vocabulary is closed and is the *same*
> list as the primary one, so a secondary "blocked execution" was never
> available. **Option A** (the drafted position): render blocked execution
> Unknown — `missing-evidence`, with the blocked execution disclosed as a
> named, expandable **fact of the render**. *Consequence:* the vocabulary
> stays small, but the resolution route a reader sees on the reason itself is
> "produce/capture evidence," which is the **wrong action** for this case —
> the right one is reachable only through the disclosed fact beside it.
> **Option B** (taken): amend RFC2-24 with a further **primary** reason.
> *Consequence:* the reason routes correctly and RFC6-14 carries a value that
> means what it says; the price is a twelfth reason, an amendment to a
> vocabulary deliberately kept small, and a reason whose condition is a
> *governance* block rather than an evidence state — which is also true of
> #3, #6 and #7, so the vocabulary already mixes both kinds.

### q6 — Revocation rendering versus re-evaluation (ANSWERED, B4)

The question as posed, verbatim:

> 6. **Revocation rendering versus re-evaluation (RFC5-11) — the residual
>    window.** Review 3's AS-R6 found that revocation stopped *acts*
>    immediately while dependent claims kept rendering as current until the
>    next human-triggered evaluation. **The drafted fix binds the render**:
>    from the revocation record onward, every served render of a dependent
>    claim carries the withdrawal label, while the claim's *value* is
>    recomputed only at the next evaluation (preserving RFC2-4 and the
>    act/claim split — see §6.7 for why the act-timed re-render was
>    rejected). **What the owner is accepting:** a window of unbounded
>    duration in which a labelled claim still carries its pre-revocation
>    value. **Stronger forms available:** (i) recording a revocation
>    *triggers* an evaluation; (ii) the quality policy declares a **maximum
>    interval between a revocation and the re-evaluation that clears it**,
>    with the claim degrading to Unknown once exceeded. Both cost more than
>    labelling; (ii) is the lighter of the two and composes with RFC4-16's
>    declared-interval pattern. Accept the drafted form, or direct (i) or
>    (ii)?

The answer, verbatim:

> > **ANSWERED at acceptance — B4.** The **stronger form** is taken: revocation
> > forces a new identified evaluation rather than waiting for the next
> > human-triggered one. RFC2-4 is unweakened — the security act *schedules* an
> > evaluation, it does not mutate a claim.

That consequence is **normative and lives in the active RFC5-11**, not here.

### q1, q4, q5 — still OPEN, retained in the active contract

q1 (machine-client mechanism), q4 (destructive-op class closure), q5 (rotation
overlap default) remain open. q1 and q5 are carried in
`../rfcs/RFC-0005/admission-and-boundary.md` §8, q4 in
`../rfcs/RFC-0005/execution-profiles.md` §8; `README.md` §8 indexes all six.
q1 gained
a rev10 **scope ruling** (directive §2 / OD-R10-5) which classifies it as "must
close before V0 implementation; does not block specification" and states that
the browser-versus-machine-client contract is closed. The scope ruling **does
not answer** q1 and selects no mechanism.
