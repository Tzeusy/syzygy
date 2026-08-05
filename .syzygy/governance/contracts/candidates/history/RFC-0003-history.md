# RFC-0003 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
the `../rfcs/RFC-0003/` package — `manifests-and-namespace.md`
(RFC3-1…RFC3-14, RFC3-18…RFC3-32) and `governance-homes-and-owner-acts.md`
(RFC3-15…RFC3-17(a) and every lettered sub-clause), indexed by its
`README.md`. Full review corpus: `_bootstrap/rfc-phase/reviews/`. Frozen rev9
source: `_bootstrap/rfc-phase/rfcs/RFC-0003-project-workspace-manifests.md`.

Extracted `*(History: …)*` text is copied **verbatim**. Narrative moved out of
a clause (as opposed to an amendment record) is labeled `[moved narrative]`.

---

## RFC3-1

*(History: bound at rev7 review 9, boundary finding 8; no stack neutrality is
spent — the choice was already made by the filename doctrine fixed.)*

## RFC3-2

*(History: added at acceptance by owner decision B19, together with RFC3-15's
`records/` category.)* — on the introduction of the fourth write-authority
class `kernel-recorded`.

*(History: pinned at rev7 review 9, finding S6, so two implementations cannot
produce different snapshot identities over one tree)* — on the
"which lifecycle transitions mint a record" rule.

[moved narrative — the [Inferred] rationale for why a fourth class was needed;
the rule it justifies (`kernel-recorded` is never authorization-bearing)
remains in the active clause]:

> [Inferred] The three original classes did not fit this, and the drafted
> workaround — Syzygy-maintained with the challenger's identity carried as an
> ordinary field — was sound under the one-writer rule but misdescribed the
> authority: "Syzygy-maintained" implies a mechanical value Syzygy derives,
> and a challenger's submitted concern is neither mechanical nor Syzygy's. A
> reader checking who stands behind the value would get the wrong answer.

## RFC3-4

[moved narrative — the rejected alternative is summarized in the active file's
§5 and its reasoning is reused at RFC3-16(a); see §6 below, "Designating the
governance root by field value".]

## RFC3-7

*(History: post-draft amendment under review 3's AS-R10, removing an internal
inconsistency with RFC 0005. The granularity question was **answered at
acceptance by owner decision B8** — one record per (project, provider); the
finer per-content-class and the per-repository alternatives were both
declined — see §8 q3.)*

## RFC3-14

*(A draft had renamed it to `relies-on-project` to avoid the collision; the
owner reverted that rename at acceptance (B20), restoring the original
`depends-on` having been shown the collision and its consequence.)*

## RFC3-15(a)

*(History: added at acceptance by owner decision B19).*

[moved narrative — the pre-B19 problem statement; the durability rule and the
"widen explicitly rather than stretch a category" precedent remain in the
active sub-clause]:

> Before this category it fitted none of the four and the RFC named no home,
> which meant two conforming implementations would choose differently and at
> least one would choose `cache/`.

## RFC3-16

*(History: rewritten at the rev8 rework, items 2 and 3 — the earlier text
imposed one universal draft/adopted/amended/retired lifecycle on every
reserved category, contradicting RFC3-15's own `records/` row, and made
adoption status in-content in a way that forced a digest-changing edit after
every owner act, contradicting RFC3-16(b) item 3.)*

[rev10 amendment record] The effective-status paragraph was sharpened at the
rev10 rework under directive §2 / OD-R10-5 (adversarial finding F1): effective
status is now stated as *read from the owner-act record*, whose own
verification state is two-valued per the new **RFC3-16(c)**. No obligation
changed; the "no owner-act record → effectively unadopted" rule is unchanged
and the "acceptance never edits the artifact" rule is unchanged.

## RFC3-16(a)

*(History: post-draft amendment, added under review 3's Blocker AS-R1;
lettered as a sub-clause of RFC3-16 so the RFC3-1 … RFC3-32 range stays
closed.)*

[moved narrative — the §6.3 account of what the draft's original posture was
and why it was rejected is reproduced under §6 below.]

## RFC3-16(b)

*(History: added at the rev7 rework — directive item B2 of
`_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`, not owner decision B2.
RFC3-16(a) fixes when provenance is required and defers the mechanism; this
sub-clause fixes what any conforming mechanism must bind, so that two
implementations cannot diverge on the meaning of "the owner approved this"
while both citing the predicate. It chooses no keys, signatures, or
transports.)*

The framing sentences of that parenthetical were promoted into the active
sub-clause's opening at rev10; the provenance note (directive item B2, **not**
owner decision B2) is preserved here.

## RFC3-16(c)

**New at rev10.** Added under directive §2 / OD-R10-5 to repair adversarial
finding F1 — the acceptance-semantic contradiction between
`FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` §2 ("That committed act record *is*
the effective status") and RFC3-16 / RFC3-16(a) / RFC3-16(b), which require an
independently verifiable owner-act record and say in terms that a
pre-mechanism act renders "not as verified".

Lettered (not numbered 33) so the RFC3-1 … RFC3-32 range stays closed — the
same device used for RFC3-15(a), RFC3-16(a), RFC3-16(b) and RFC3-17(a).

The owner's repair direction, as recorded at OD-R10-5: distinguish
`owner-adopted bootstrap act` (human/social governance fact — phrase + digest
+ commit/tag; the human may govern development by it) from
`Syzygy-verified effective act` (the bootstrap act after one-time correlation
through the independent A1 mechanism). Until correlation: Syzygy must not
claim independent verification; provenance renders the gap honestly; **git
commits or tags alone remain never sufficient** (preserved owner decision).
Weakening nothing.

## RFC3-17(a)

*(History: added post-draft; the plane previously named no home for them.
Body rewritten at acceptance under owner decision B19: the original draft
reserved a further category under `Syzygy-maintained` authority, and reasoned
from a then-true premise that RFC3-15 had four categories and RFC3-2 admitted
no fourth class. B19 superseded that premise — RFC3-15 now has five
categories and RFC3-2 four classes — so the original body is retired and this
body states the adopted model. The sub-clause identifier is retained; nothing
else of the original remains normative.)*

[moved narrative — the full "Why `records/` and nothing else" reasoning; the
active sub-clause keeps a compressed form with every exclusion named]:

> RFC2-13 makes the admission-or-rejection record a *kernel fact written to
> the governed plane*, and RFC2-1 item 9 makes open challenges with their
> admission records a **snapshot input** — so the artifact is
> identity-bearing, durable, and deletion-unsafe, and it **enters snapshot
> identity** exactly as RFC2-1 item 9 requires. `cache/` is barred outright:
> RFC3-20 forbids anything there from serving as a snapshot input or being
> the only home of a fact. `local/` is barred by RFC3-21 (never
> truth-bearing, never a snapshot input). `intent/`, `work/`, and `map/` are
> surface namespaces (RFC3-18) and none of the three surfaces owns challenge
> state. And the artifact is not doctrine, not an accepted contract, not a
> policy, and — decisively — **not a recorded owner decision**: it is an
> inference-or-human *objection* whose admission is a mechanical kernel
> check. That is RFC3-15's `records/` definition verbatim — a kernel-authored
> durable fact minted on a non-owner actor's submission. The one
> challenge-adjacent thing `governance/` holds elsewhere is the *resolution
> policy* in `policies/` (RFC3-15), which governs how a challenge is resolved
> and is not the challenge.

## RFC3-19

*(Handoff satisfied by the RFC1-29 amendment of 2026-07-30: RFC1-29 now
requires the materialization record to pin "the exact intent revision … cited
by the proposal's warrant", and RFC1-5's materialization-record row carries
it. The obligation is therefore stated once, in RFC 0001; this clause
restates its schema consequence and no longer requests an amendment. Recorded
rather than deleted so the trail survives — review 3, AS-R8.)*

Companion narrative from rev9 §5, moved here in full:

> **Defect handoff — resolved (retained for the trail):** this RFC reported
> that RFC1-29 defined the materialization record without requiring the
> pinned warranted intent revision that RFC2-18's reconciliation chain joins
> on. **Satisfied by the RFC1-29 amendment of 2026-07-30**, which pins the
> exact warranted intent revision in the record itself (and RFC1-5's
> materialization-record row with it). No RFC 0001 change is outstanding;
> RFC3-19 now restates the consequence rather than requesting the fix
> (review 3, AS-R8).

## RFC3-30

*(History: post-draft amendment under review 3's AS-R7.)* — on the
"governing policy is a property of the observing project's governance root"
paragraph.

---

## §6 — Alternatives considered (moved wholesale from rev9 §6)

### 6.1 Nested projects (the OQ-010 conflict) — options

- **(a) Directory-scoped sub-roots** (a `.syzygy/` plane per subdirectory
  inside one repository). Rejected: it breaks "exactly one designated
  governance root … the repository containing the Project's single plane"
  (architecture.md — a doctrine amendment, not an RFC choice); it splits the
  consent record's subject (SEC-4 consent is per-repository); and it makes
  the write universe ambiguous (which plane may write `openspec/**`?).
- **(b) Parent-owned subproject registry** (parent plane authoritative for
  children). Rejected: SDR-30 verbatim — no manifest is authoritative for
  another project's internal truth; it would also make child state a fact
  living outside the child's plane, against VIS-6.
- **(c) Composition by declaration — chosen (RFC3-31).** Preserves the
  one-root invariant untouched, reuses the already-required asymmetric
  relation semantics, keeps every project offboardable as a unit, and
  realizes the seed's promise as *rendering depth*, which is where the seed's
  own comprehensibility tension (KNOWN_TENSIONS T15) wanted it bounded
  anyway.
- **(d) Reject nesting outright.** Not taken: it forecloses a named seed
  promise without doctrinal need; under VIS-1 the derived hierarchy is cheap
  and honest. The genuinely foreclosed case — many governed subprojects
  inside one repository — is surfaced as open question 1 rather than silently
  buried.

### 6.2 Other roads not taken

- **Workspace manifest as a governed artifact** (committed, adopted,
  versioned). Rejected: it would need a home, and no third namespace exists
  (VIS-5); a Syzygy-owned authoritative store is FR-2's option 2, a VIS-6
  violation absent a doctrine amendment. Exception (a) fits SDR-29's concerns
  exactly; the cost is examined in open question 2.
- **Embedding consent records in `project.yaml`.** Rejected: consent is a
  governance act needing independent lifecycle (grant, narrow, revoke,
  supersede) and attribution; embedding would give one file two authorities
  per field (violating RFC3-2) and make revocation an edit war with
  membership drafting.
- **Designating the governance root by field value** rather than by the
  declaration's location. Rejected: a field can dangle or lie; the file's
  location cannot — and it makes the zero-root case structurally impossible
  rather than merely detectable. *(Load-bearing: RFC3-16(a) extends this
  exact reasoning to authorization-bearing artifacts, and a one-sentence form
  is retained in the active file at RFC3-4 and §5.)*
- **Lazy migration on read.** Rejected: violates idempotence (RFC2-22) and
  SEC-4 attribution — a render pass must never be a write actor.

### 6.3 Post-draft adjustments (review 3)

- **Treating an in-tree authorization as self-authenticating** — the draft's
  original posture, in which a consent record's, Decision's, or stamp's
  stored attribution field was sufficient to honor it. Rejected under review
  3's Blocker (AS-R1) and replaced by **RFC3-16(a)**. The draft already
  demanded an owner-attended ceremony for machine *credentials* (RFC5-6)
  while the higher-authority artifacts — what may egress, what may execute,
  what is adopted — carried attribution as a stored field only; an untrusted
  fleet worker with ordinary commit access to the in-tree plane could
  therefore mint its own authorization. The alternative of **patching each
  artifact class separately** (a provenance sentence in RFC3-7, another in
  RFC5-12, another in RFC3-16) was considered and rejected: it leaves
  whichever class is added next unguarded. One predicate, one home, cited
  from every consuming gate. **Cost, deliberately taken:** the owner must
  perform an authenticated act — not merely commit a file — for every
  consent, approval, and adoption; batch-editing governance artifacts in an
  editor stops being sufficient. Routed to acceptance as §8 q5.
- **Egress-consent granularity wording** (RFC3-7). The draft's "per content
  class" phrasing in RFC5-12 contradicted RFC5-14's single record naming
  multiple classes. Aligned to **one record per *(Project, provider)* naming
  the permitted set** (AS-R10). This removes an internal contradiction only;
  the substantive granularity ruling stays open at §8 q3.

---

## §8 — Answered open questions (moved from rev9 §8, with their answers)

Questions q1, q2 and q4 remain **open** and are retained in the active file.
Numbering is preserved throughout: no question was renumbered.

### q3 — Egress consent granularity (RFC3-7)

> SEC-2 words egress consent per-project; RFC1-3 folds it into per-repository
> consent records. This RFC models egress consent as its own per-(project,
> provider) record kind. Confirm this split, or direct that egress scope ride
> on each repository's consent record (finer-grained, heavier to administer)?
> *(Review 3's AS-R10 aligned RFC5-12's wording to one record per
> *(Project, provider)* naming a set of content classes, removing an internal
> contradiction with RFC5-14. That is a consistency fix only — this question
> is untouched by it and remains the owner's to rule.)*

> **ANSWERED at acceptance — B8.** **One record per (project, provider)**,
> naming the permitted content classes inside it. Matches SEC-2's wording;
> the finer per-content-class granularity is not taken.

Carried into the active file at RFC3-7.

### q5 — The owner-act provenance predicate (RFC3-16(a))

> **added post-draft under review 3's Blocker, scope widened to the predicate
> thereafter.** Honoring an artifact that authorizes a dangerous act,
> unblocks a claim class, or fixes the meaning of a rendered encoding now
> requires provenance the governed tree cannot forge, not merely a
> well-formed file carrying an attribution field. Two things need the owner's
> word. **(a) The ergonomic trade — and its true breadth.** The clause's
> subject is the predicate, not its example list, so the trade is wider than
> the original four classes: beyond consents, approval Decisions and adoption
> stamps (RFC7-21), it reaches the secret-detection and egress-classification
> policies (RFC5-16, RFC5-14), the adapter registry entry (RFC4-7), the
> declared staleness bound and maximum inter-pass interval (RFC4-23(2),
> RFC4-16(2)), the deterministic challenge-resolution policy (RFC2-13), the
> channel and layout-version registries (RFC9-26, RFC9-18), and the owner
> judgments in `decisions/` (RFC7-25, RFC7-31). Each becomes an authenticated
> owner *act*; hand-editing or scripting any of them into the plane stops
> being sufficient, including for the owner's own convenience. That cost is
> real and recurring — confirm it is the trade you want, or direct a narrower
> scope (e.g. the predicate binding only egress and execution
> authorizations, leaving adoption stamps and registries on stored
> attribution). **Narrowing by re-enumerating is the option to weigh
> carefully:** a list is what left the last-patched class unguarded, so a
> narrowing is best expressed as a *narrower predicate*, not a shorter list.
> **(b) The mechanism class.** *(As posed, the clause named two candidate
> classes and deferred the choice; per the A1 answer below, RFC3-16(a) now
> binds the ceremony+audit class and owner-held attestation is no longer an
> implementation option.)* The clause deliberately named only a class —
> correlation to a Syzygy-mediated owner ceremony recorded in the RFC5-25
> audit trail, or an owner-held attestation neither the tree nor Syzygy can
> mint — and deferred the choice to the first implementation slice. Confirm
> the class boundary, or fix a mechanism at acceptance.

> **ANSWERED at acceptance — A1 / A9.** Mechanism class: **owner-attended
> ceremony correlated to an independently kept audit trail** (not owner-held
> attestation). **Binding constraint:** that audit trail must live outside
> `.syzygy/**` and outside the untrusted actor class's write reach, or the
> correlation proves nothing. The owner accepted shipping before the
> mechanism exists, with the gap rendered honestly in the interim.

Carried into the active file at RFC3-16(a) ("The mechanism class — chosen,
not open") and, at rev10, at RFC3-16(c), which names the two provenance
states the A9 interim posture implies.

### q6 — A governance home for challenges and admission records (RFC3-17(a))

> *(Question body preserved as posed; the premises it states — four exclusive
> categories, the original RFC3-17(a) draft home — were true when written and
> are superseded by B19.)* RFC2-13 makes a challenge's
> admission-or-rejection record a *kernel fact* written to the governed
> plane, and RFC2-1 item 9 makes open challenges with their admission records
> a snapshot input — durable, identity-bearing, deletion-unsafe. RFC3-15 (as
> then written) declared its four categories exclusive, and a kernel fact
> that is **not an owner decision** fitted none of them. So the plane needed
> one of two things, and only the owner could choose: **(a)** a further
> reserved category — `governance/challenges/`, as RFC3-17(a) then drafted —
> or **(b)** an explicit widening of one of the four, most plausibly
> `decisions/`, on the reading that admission is *an act recorded as a fact*
> — a reading available but costly, since a category holding *recorded owner
> decisions* would also hold records no owner made. **What was never open:**
> `cache/` and `local/` are excluded either way (RFC3-20/21). Which?

> **ANSWERED at acceptance — B19.** Neither option as posed: the owner
> widened the constitution itself. Challenge and admission records live in
> **`records/`** (RFC3-15's fifth category, `kernel-recorded` authority);
> `governance/challenges/` was never created and RFC3-17(a)'s body was
> rewritten accordingly (rev7 rework, directive item A1 — not owner decision
> A1). `cache/` and `local/` remain barred to identity-bearing snapshot
> inputs.

Carried into the active file at RFC3-15, RFC3-15(a) and RFC3-17(a).

---

## Reader's summary (rev9 §0) — superseded

Rev9 opened with a plain-language "Reader's summary". It is replaced in the
active file by §0 "Scope and reader map", which keeps the same
clause-wins-over-summary rule and the same identification of RFC3-16(a) as
the single most consequential clause. Nothing normative lived in either.
