# Wave A repair batch (R-A) — semantic delta record

> **Process record for candidate bytes.** Nothing here is accepted. Every
> edit below lands in `rfcs/RFC-0001…0006` as **candidate** text, ratified or
> reverted by the owner at the wave act that binds those digests (VIS-4). This
> file adopts nothing, performs no act, and is never authority.
>
> Subject: the **19 Wave A modules** named by `wave-manifests/WAVE-A-MANIFEST.txt`.
> **14 of the 19 were edited**; the five untouched are
> `RFC-0002/challenge-lifecycle.md`, `RFC-0004/execution-record.md`,
> `RFC-0004/general-contract.md`, `RFC-0005/consent-egress-secrets.md`,
> `RFC-0005/execution-profiles.md` (counts computed from `git diff --stat`
> over the manifest's 19 paths, this session).
>
> **Every edit in this file is digest-moving.** All 14 files sit inside the
> Wave A manifest, so the manifest, its own sha256, and the acceptance
> record's Wave A argument must be regenerated **by script** (not by hand, and
> not by this agent), and a fresh-context review must be bound to the new
> bytes before the wave may be offered (verification rule 10; disposition
> register §7). The one non-digest-moving claim made anywhere below is stated
> as such and named.
>
> Baseline: the round-2026-08d review commit `771965c`, the bytes RD-9, RD-15
> and RD-18 were bound to. Sources of finding text: `RD-9-core-authority-RAW.md`,
> `RD-15-facets-RAW.md`, `RD-18-wave-a-RAW.md`, plus the launch-gate
> administration's C1 finding at the RFC3-15 site. The disposition register's
> tags are navigation; the raw reviews are the authority.

## 0. What this batch did not do

- **No owner decision was pre-empted.** RD-18 **B2** (the `contracts/`
  containment breach) and RD-18 **M5** (the 39-row manifest installed at act 1)
  are **P-33** and are untouched here — neither arm is drafted. RD-15 f3 is
  **P-31**; the *exemption* arm is drafted (§9) because the disposition says
  it may be, and the thirteenth-reason arm is **not** drafted, because owner
  decision A5 closed RFC2-24 at twelve.
- **No clause was renumbered, retired, merged, or reused.** No new numbered
  clause and no new lettered sub-clause was created; every repair is an
  in-place amendment of an existing clause or of package-index prose.
  `verify_final_prespec.py` reports **341 numbered clauses defined**, the same
  figure RD-18 read at the baseline.
- **No manifest, acceptance record, matrix, router, fixture or script was
  touched** — the batch's file boundary is the 19 Wave A modules plus this
  file. Consequences that fall outside it are listed in §11 as handoffs.

---

## 1. RD-18 B1 + launch-gate C1 — the retired phrase inside the bound bytes

| | |
|---|---|
| Clause | **RFC3-15**, `contracts/` row (`RFC-0003/governance-homes-and-owner-acts.md`) |
| Digest-moving | **yes** |

**Old meaning.** The install gate for the `contracts/` category *was* one
named ceremony phrase — `ACCEPT COMPACTED FOUNDATIONAL RFCS: <manifest
digest>` — describing **one** digest-bound act over the foundational set.

**New meaning.** The install gate is *"the digest-bound **acts** defined by the
active acceptance record — that record owns the acts, their exact phrases, and
their arguments, and this clause quotes none of them, so a phrase this clause
named could never outlive its retirement"*. The clause now names **no phrase
and no act count**.

**Why this shape.** The quoted phrase was retired, and the structure is six
wave acts, not one: a clause inside the digest being bound described the
ceremony wrongly at the instant of the ceremony, and RFC3-16(b) item 3 makes
it unfixable afterwards. This is the P-6 defect class recurring — the rev9
phrase was swept out of this exact cell and replaced by the rev10 phrase,
which was then retired without a second sweep. A **phrase-free deferral** is
the only form that cannot recur: the record can retire and mint phrases and
restructure acts without this clause going stale. It is also the repo's own
rule that a figure quoted outside its owning artifact goes stale silently.

**Sweep, with denominator.** Python `re` over all **19** Wave A modules for
`ACCEPT\s+[A-Z ]*FOUNDATIONAL`: **0 hits** after the edit (1 before, this
cell). The repo battery's extended CG-2a check independently reports **0
findings inside `rfcs/**`** and 5 elsewhere, all outside this batch's boundary
(§11).

---

## 2. X1 — stale coverage ranges and self-counts (RD-9 f8, RD-18 M2, m1, m2)

The design applied throughout: **prefer a formulation with no literal range**,
so a future append cannot silently falsify it. Where the range was the
mechanism (a lookup rule), it is restated as bounded ranges plus a **catch-all**,
which is total by construction.

| Site | Old | New | Digest-moving |
|---|---|---|---|
| `RFC-0005/README.md` lookup rule (**RD-18 M2**, RD-9 f8 first item) | `1–11`→m1; `12–17`→m2; `18–23`→m3; `24–26`→m1, claimed *"contiguous and exhaustive over RFC5-1…RFC5-27"* — **false**: RFC5-27 resolved to no module | `12–17`→m2; `18–23`→m3; **every other number → module 1**; totality now holds by construction, with RFC5-27 named as the case the old rule dropped | yes |
| `RFC-0003/manifests-and-namespace.md` module heading | *"(RFC3-1…RFC3-14, RFC3-18…RFC3-32)"* — excluded RFC3-33, which the module holds | *"(every `RFC3-n` except RFC3-15…RFC3-17 and the lettered sub-clauses)"* | yes |
| same file, §0 clause-identity line | *"holds RFC3-1…RFC3-14 and RFC3-18…RFC3-32"* | *"holds **every `RFC3-n` number other than** RFC3-15, RFC3-16, RFC3-17 and their lettered sub-clauses"* | yes |
| `RFC-0003/governance-homes-and-owner-acts.md` closing line | *"Every other number in RFC3-1 … RFC3-32 is in `manifests-and-namespace.md`"* | *"Every other `RFC3-n` number, **whatever the package's range grows to**, is in `manifests-and-namespace.md`"* | yes |
| `RFC-0003/README.md` deterministic lookup rule | *"Every other number in RFC3-1 … RFC3-33"* — correct today, stale on any append | same sentence, range-free | yes |
| `RFC-0004/README.md` closing line (**RD-18 m2**) | *"Clauses RFC4-1 … RFC4-29"* — the package ends at RFC4-30 | the range is stated **once**, in the front matter, and the closing line points at it rather than restating it | yes |

**Why range-free rather than corrected ranges.** Three of these six were
already wrong at the baseline and a fourth would have gone wrong at the next
append. Correcting the numbers leaves the class alive; removing the
restatement retires it. The `RFC-0003/README.md` row is the one edit in this
section that repaired **no** error — it is a durability edit, and it is
recorded here rather than claimed editorial, because "the same lookup rule,
one form later" is still a change to bytes an act binds.

**Not changed, deliberately.** `RFC-0002/README.md`'s and
`RFC-0005/README.md`'s *closing* range statements, and the coverage-matrix
ranges inside RFC1-33 / RFC2-26 / RFC3-33 / RFC4-30 / RFC5-27, are correct at
these bytes and are named by no finding; editing them would move digests for
no defect. They are the population the register's X1 note hands to R-SCR for a
recomputing check. **RFC6-28 is the exception** — see §8.

---

## 3. X2 — the ungated reviewed N/A judgment (RD-9 f11), six clauses

| | |
|---|---|
| Clauses | **RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28** — one per Wave A package |
| Digest-moving | **yes**, in all six files |

**Old meaning.** Each phase rule admitted an *"explicit, reviewed N/A
judgment"* as an alternative to an OpenSpec requirement, and said nothing
about where that judgment lives or what makes it count. An N/A judgment is
not doctrine, not a contract, not a policy and not a kernel record, so it was
homeless; and nothing stated its gate, although it authorizes implementation
without a requirement.

**New meaning — the exact standardized sentence, byte-identical in all six:**

> **The reviewed N/A judgment's home and gate.** A reviewed N/A judgment is a
> recorded owner judgment homed in `decisions/` (RFC3-15), and it is honored
> only where its owner-act provenance is verifiable under RFC3-16(a). Where
> that provenance does not verify, the judgment maps nothing: the consequence
> remains unmapped and renders Unknown, never covered (RFC3-16(a)'s effect
> rule; VIS-2).

*(Wave B's three clauses — RFC7-38, RFC8-32, RFC9-52 — take the same sentence
from the R-B batch; quoted here verbatim so the two batches can be checked
against each other by string comparison.)*

**Why.** RFC3-16(a) already reaches the judgment on its own terms — it *"binds
project truth in a way no downstream status check can falsify"*, and the
clause is emphatic that a satisfying artifact is in scope whether or not it is
listed. So the gate was not absent, only unstated; the home genuinely was
unresolved, and `decisions/` is the category whose contents are *recorded owner
judgments*. The third limb matters most: an unverifiable N/A judgment must
leave the consequence **unmapped and Unknown**, never quietly covered — VIS-2
applied to the coverage matrix itself.

**Sweep, with denominator.** Whitespace-normalized string search for the
sentence over all **19** Wave A modules: **6 sites, one per phase clause, zero
elsewhere, zero near-misses**.

**Staging consequence, stated plainly.** RFC 0001 declares `depends_on: []`
and its §5 stages every RFC3-n citation as informative until RFC 0003 is
accepted. RFC1-33's new limb therefore names no honored home and no verifiable
gate until RFC 0003 binds. Rather than give the kernel a dependency it has
never had, §5 now names RFC1-33 in its staged-example list and states the
consequence outright: until RFC 0003 is bound, the judgment RFC1-33 governs
**cannot be honored at all** — the conservative direction, and moot in
practice because RFC 0003 binds in the same act. [Inferred]

---

## 4. RFC-0001 — kernel repairs

### 4.1 RD-9 f1 — the profile-minting seam (RFC1-7, RFC1-9)

**Old meaning.** RFC1-7 required a profile-defining RFC to name *"the minting
authority of every identity it adds, under RFC1-9's discipline"* — and nothing
else. RFC1-9 required every identity-bearing class to name its authority **in
RFC1-5**, a closed table no profile entity can appear in. Result: a profile
entity was either in violation of RFC1-9 on its face, or admitted by a
delegation RFC1-9 did not acknowledge; and no clause assigned it an RFC1-22
state plane, leaving RFC6-19 class 1 unsatisfiable for it.

**New meaning.** RFC1-7 now requires the profile-defining RFC to name, for
every identity it adds, **(i)** exactly one minting authority — deterministic
derivation from declared inputs where that authority is the kernel — and
**(ii)** exactly one RFC1-22 **state plane** for every source-state assertion
the profile adds; and states that these namings are what discharge RFC1-9's
`in RFC1-5` locator for profile classes, **without widening RFC1-5's closure**.
RFC1-9 carries the matching sentence from its own end.

**Why.** Two clauses, one seam, read from both ends — the shape RFC3-16(b)/(c)
uses elsewhere in this corpus. The alternative (listing profile entities in
RFC1-5) would break RFC1-5's closure, which RFC1-7 exists to avoid.

### 4.2 RD-9 f3 — RFC1-1's unrealizable zero-roots contradiction

**Old meaning.** Zero governance roots minted a contradiction *"in the
workspace's own evaluation context"* — a construct **no clause in the corpus
defines** (RD-9's sweep: all 39 `rfcs/**` files, one hit, RFC1-1's own), and
one RFC3-10/RFC3-12 arguably forbid.

**New meaning.** Zero roots renders Unknown (`missing-declaration`) at the
workspace with **no kernel contradiction minted**, and the clause says why: an
evaluation is identified by a Project's `(source snapshot, as-of instant)` and
nothing else (RFC2-3), and the workspace manifest is barred from being a
snapshot input, so no evaluation context exists in which such a contradiction
could live. The two-roots case is unchanged and still mints a contradiction.
The opening sentence was adjusted so it no longer calls both cases
contradictions.

**Why.** This is the honest half the corpus already implements: RFC3-13
renders such an entry Unknown with its RFC2-24 reason and mints nothing. The
alternative repair — defining a workspace-level evaluation with its own
snapshot — would need a new construct in RFC 0003 and a reconciliation with
RFC3-10's *"never a snapshot input"*, which is a larger change than the defect
warrants. **No greenness risk either way**; the Unknown rendering is identical.

### 4.3 RD-9 f4 + RD-18 M1 — `supersedes` and `succeeds` (one design, RFC1-25)

**Old meaning.** `supersedes` delegated its endpoint pairs to RFC1-31's prose,
where two of six lifecycle groups are indeterminate — so RFC1-25(d)'s claim
that the table **is** the enumeration was false for that row. `succeeds`
listed one endpoint pair (*"Successor identity → predecessor identity"*,
naming no entity kind) while carrying **two** semantic classes split by
subject class, which per-pair resolution — RFC1-25(d)'s only discharge
mechanism — cannot separate; and its class cell's value was not in RFC1-25's
closed class vocabulary.

**New meaning.**
- `supersedes` **enumerates its pairs**: (Decision→Decision), (Consent
  record→Consent record), (Policy→Policy), (Observation record→Observation
  record), (Proposal→Proposal), and states the answer for the two groups that
  contribute **none** — declared classes are amended in place under the same
  identifier and mint no successive version; work-item versioning is
  scheduler-owned execution state mirrored under RFC1-9, never a kernel-minted
  edge.
- `succeeds` becomes **same-class pairs** naming entity kinds — the four
  declared classes plus (Contradiction→Contradiction) — with semantic class
  **"Matches endpoint"** (a value the vocabulary already carries) and the
  per-pair resolution moved into the Rule cell: declared-class pairs resolve to
  **Desired (declared)**; the Contradiction pair resolves to **Derived**,
  computed at the minting evaluation and a fact only when recorded inside that
  evaluation's observation record (RFC1-18(b)).

**Why one design.** The two rows share a defect and a fix: `supersedes` was
solved correctly one row earlier and `succeeds` was left generic. Both now
resolve under RFC1-25(d) without a subject-class dispatch that clause does not
authorize. **No relation is added and none is re-typed**, so RFC1-26's closure
is untouched — the rows now say explicitly what RFC1-25(d)'s reading of the
table already implied. The truth conditions RFC1-18(b) depends on (a derived
`succeeds` edge is a fact only inside an observation record) are preserved
verbatim.

---

## 5. RFC-0002 — dependency honesty, closures, dismissal

### 5.1 RD-9 f6 — RFC 0002's three-way self-contradiction about RFC 0003/0004/0005

**Old meaning.** The same citations were simultaneously a **dependency**
(front matter), a **reliance** (§5), and **not a dependency of the contract's
meaning** (§5's forward-reference paragraph). Read literally, an act binding
RFC 0002 before RFC 0003 would leave currency-bound declarations honored
without owner-act provenance — the widening RFC2-13 and RFC3-16(a) exist to
prevent.

**New meaning.** §5's paragraph now separates the two cases: RFC4-n, RFC5-n
and the surface RFCs stay **informative until accepted**; this package's
citations of RFC 0003 are **load-bearing**, and the paragraph names them —
RFC3-2, RFC3-15, the RFC3-16 family, RFC3-17(a) (measured this session: those
four families are the entire RFC3-n citation set across the package's five
modules). It then states the binding-order consequence: **this package does
not bind unless RFC 0003 is bound by the same act or an earlier one.**
RFC2-9's parenthetical changes from *"(RFC3-16(a), informative until RFC 0003
is accepted)"* to a load-bearing citation pointing at that rule.

**Why this arm.** RD-9 f6 offered two: make RFC 0003 load-bearing, or drop the
edges and remove the conditionals. The second silently widens the gate the
moment RFC 0002 binds alone; the first is the posture the clauses already
assume. The wave design binds RFC 0002 and RFC 0003 in the same act, so the
new sentence constrains nothing that was going to happen — it removes a
reading under which the act would have meant less than it appears to.

**Front-matter consistency, same finding class.**
`RFC-0002/rendering-vocabularies.md` cites RFC3-15/RFC3-16(a) (now also
through X2) but declared `depends_on: [RFC-0001, RFC-0005]`; it now declares
RFC-0003 and carries a matching *Relies on RFC 0003* entry in its §5. All
three edges stay inside Wave A, so RD-18's verified *"every `depends_on` edge
of these contracts stays inside the wave"* claim still holds (§10).

### 5.2 RD-15 f6 — freshness and degradation closed in a clause, not a reader map

**Old meaning.** Freshness (`fresh`/`stale`/`broken`/`superseded`, RFC2-10) and
the six degradation states (RFC2-23) were **carried verbatim on machine
answers, counted per value in aggregates, and release-blocking on
disagreement** — while the only closure claim for either sat in module 4's §0
reader map, which is explicitly subordinate to its clauses.

**New meaning.** RFC2-10 states *"**Four values, closed**"* and RFC2-23 is
retitled *"**Six degradation states, closed**, each with its rendering
obligation"*, both carrying the mint/spell/force-fit prohibition and the
fact-of-the-render escape in the form RFC2-24/RFC2-25 already use. Both state
their own reason for closure — RFC2-10's from RFC6-14/17/22-23, RFC2-23's from
RFC4-2 item 6, which requires adapters to map internal errors onto these
states by declaration.

**Why.** RFC2-24's own argument for closure transfers verbatim: a value in no
vocabulary can be neither carried verbatim nor checked for parity, "and
leaving it unstated is how the value gets chosen by whoever implements the
render first." The reader map already said these were closed; only the clause
can make that true.

### 5.3 RD-15 f8 — dismissal is not erasure (RFC2-15)

**Old meaning.** For challenge suspension the corpus protects the underlying
facts explicitly (RFC2-14, *"Suspension is not erasure"*). Dismissal — the
**human** ruling that replaces a status rendering — had reason, expiry and
never-green obligations, and **no basis-visibility guarantee**.

**New meaning.** RFC2-15 gains a *"Dismissal is not erasure"* limb in RFC2-14's
shape: the dismissed gap's own status and Unknown reason stay visible beside
the dismissal on the **primary surface** for as long as the dismissal stands;
rendering the dismissal alone is a violation of the clause.

**Why.** The asymmetry the finding names is the whole point — a human ruling
could displace facts an inferred challenge may not. It also makes expiry
legible: a reader can see what returns when the dismissal lapses. Doctrine
already licenses suppression *as* dismissal (never as resolved or green), and
this limb changes nothing about that.

---

## 6. RFC-0003 — staging, reliances, and the `records/` enumeration

### 6.1 RD-18 M4 — no staging language anywhere in the package

**Old meaning.** RFC 0003 carried **14** non-shape-parallel citations into
RFC 0007–0011 and **zero** staging language (RD-18's sweep). Most are
self-staged by their own clause text (RFC3-16(a)'s *"the list below is not [the
scope]"*, the gate inventory's *"this list tracks the gates; it does not bound
them"*) — but one sits inside a **normative containment enumeration**.

**New meaning.** Three additions:
1. RFC3-15's `records/` cell marks its third item in the cell itself:
   walkthrough execution records exist *"only where those contracts are
   accepted and active"*, so until then **the category admits no member of
   that class and a conforming validator rejects one**.
2. Each module's integration section carries a *Forward references are
   informative* paragraph naming what is staged and what is load-bearing, and
   pointing at the `records/` cell as the one citation standing inside a
   normative enumeration.
3. `RFC-0003/README.md` carries the package-level statement, marked as
   navigational, pointing at the two module statements.

**Why the cell and not only the paragraph.** RFC3-15 is the clause a conforming
plane validator is built from. A validator author at position 1 must not have
to decide, from a citation to nothing, whether to admit an artifact class. The
model copied is RFC1-7's mission-profile limb — a reliance made conditional on
the act that will bind it — which RD-18 named as the shape the corpus should
copy.

### 6.2 RD-9 f12 — declared dependencies the integration section disclaims

**Old meaning.** `governance-homes-and-owner-acts.md` declared
`depends_on: [RFC-0001, RFC-0002, RFC-0004, RFC-0005]` while its §3 named
reliances on RFC 0001, RFC 0002 and the sibling module only.

**New meaning.** §3 gains *"**Relies on RFC 0005:** RFC5-25's out-of-tree
location constraint … on which RFC3-16(a)'s chosen mechanism class rests"* —
a genuine reliance, since a trail inside the untrusted write reach makes the
correlation prove nothing — and a *"**Not a reliance:** RFC 0004"* paragraph
recording that every RFC4-n citation in the module sits inside RFC3-16(a)'s
non-exhaustive examples or its gate inventory (verification rule 5: a citation
is not a reliance). `RFC-0004` is dropped from the module's front matter.

**Left alone, deliberately.** `manifests-and-namespace.md` keeps its RFC-0004
edge; its two RFC4-n citations (RFC4-12, RFC4-16) sit in an enumeration of the
observing project's policy classes, and no finding examined them. The package
README's aggregate edge is unchanged for the same reason. Flagged in §11 for
the fresh review rather than repaired by inference.

---

## 7. RFC-0004 and RFC-0005 — small clause repairs

| Finding | Clause | Old → new | Digest-moving |
|---|---|---|---|
| **RD-18 m4** | RFC4-13 (`named-adapters.md`) | *"(CC-TEST-2, **amended** at the rev7 rework to name routes 3 and 4 …)"* — present-tense assertion that an amendment confirmed by a separate, later owner act already exists → *"whose rev7 amendment … **is confirmed by its own owner act** — until that act, CC-TEST-2 stands in its unamended form"* | yes |
| **RD-9 f9** | RFC5-5 (`admission-and-boundary.md`) | The closed unauthenticated-endpoint set carried **no interface qualifier**, while SEC-1 permits unauthenticated reachability *only on loopback* → the set is now **interface-qualified**: on non-loopback modes the two endpoints are reachable only behind that mode's device restriction (RFC5-9), and the bootstrap endpoint **never issues a credential outside RFC5-6's owner-attended ceremony** on either interface | yes |

**Why RFC5-5 matters despite small residual risk.** RFC5-9 and RFC5-10 already
constrain the modes, so the exposure was narrow — but the contract did not say
so, and a conforming implementation could have served credential bootstrap on
a LAN address on the clause's plain text. The repair states the qualification
rather than relying on a neighbouring clause to supply it (verification rule
8's discipline applied forward).

---

## 8. RFC-0006 — the drawer, the parity tuple, and the outcome set

Nine findings land in this one module; it is the batch's largest delta.

### 8.1 RD-9 f2 — RFC6-19 class 7's coverage boundary was anchored to a clause that does not define it

**Old.** *"the **coverage boundary** (what the producing evaluation could and
could not observe, **RFC4-2**)"*. RFC4-2 is the adapter's mandatory
**declaration set** — seven static items — and the string `coverage` appears
**0 times** in the file that owns RFC4-1…RFC4-9 (RD-9's sweep, re-run this
session: still 0).

**New.** The coverage boundary is defined as the **union of two defined
constructs**: the producing evaluation's executed **mapping coverage records**
(RFC4-27, deterministic facts inside the observation record per RFC2-6) and,
where the snapshot was partial, its **explicitly declared captured scope**
(RFC2-23). *"never a free-standing judgment about what the evaluation 'could
observe'"*.

**Why.** A mandatory drawer fact must rest on a defined clause, not on prose
near one (verification rule 8). RFC4-27 and RFC2-23 are what the corpus
actually has, and both are in Wave A.

### 8.2 RD-9 f5 + RD-15 f4 — the parity tuple omitted the facets three clauses claim it checks

**Old.** RFC6-22's equivalence tuple and RFC6-23's disagreement list named
label, tier, reason, freshness, sibling surface states, scenario context and
counts — and **not** `challenge-pending`, the normalized work state, or the
chain state. Meanwhile RFC2-13 promises `challenge-pending` is *"parity-checkable
under RFC6-22/23"*, and RFC8-12 and RFC-0008 §6 each justify their closed
vocabularies by RFC6-22/23 making disagreement release-blocking. Two surfaces
could disagree on an item's chain state without triggering anything.

**New.** RFC6-22's tuple gains the `challenge-pending` disclosure and the chain
state and normalized work state *where those are carried*; RFC6-23's list gains
the same three; and RFC6-17's disclosed composition gains per-value counts of
chain state and normalized work state plus the `challenge-pending` disclosure —
so an aggregate can no longer satisfy RFC6-17 *in full* while disclosing
nothing about reconciliation. RFC6-22 now states why: *"a facet outside this
tuple is checked by nothing."*

**Why "where those are carried".** RFC6-19 class 8 requires the fields only
*where work bears on the selection*; an unconditional tuple entry would demand
a work state for an entity no work touches.

### 8.3 RD-9 f5 (second limb) + RD-18 M3 — class 8's field count, citations, and staging

**Old.** Class 8 named *"normalized work state (RFC8-12) and chain state
(RFC8-28), carried as **two fields**"* and then added *"and the selection's
reconciliation state (RFC2-18, RFC2-19)"* — three items against a committed
count of two, with chain state routed to **Wave B** (RFC8-28) although it is
**defined in Wave A** at RFC2-18. RFC 0006 carried no staging paragraph at
all (sweep: 3 of 19 Wave A modules had one; RFC 0006 was not among them).

**New.** Two fields, stated as (i) and (ii): **chain state defined at RFC2-18**
(values enumerated) and read under RFC2-19's V0 staging — *this is* the
selection's reconciliation state, and uncomputed reconciliation renders Unknown,
never green; and (ii) the **normalized work state (RFC8-12 — a forward
reference, informative until RFC 0008 is accepted: until then the field is not
required, its absence renders as absence, and nothing may be substituted for
it)**. RFC8-28 is named as Trajectory's rendering, likewise staged.

**Why the limb states its own condition.** An implementer at position 1 must be
able to tell whether the obligation is inert or binding-but-unsatisfiable. The
staging paragraph in §5 answers it generally; the limb answers it where the
obligation is read.

### 8.4 RD-9 f7 + RD-18 m5 — `depends_on` and the missing staging paragraph

**Old.** `depends_on: [RFC-0001, RFC-0002]` while RFC6-19 normatively cited
RFC4-2 (class 7), RFC8-12/RFC8-28 (class 8), and the Status paragraph cited
RFC3-16; §5 enumerated reliances on RFC 0001 and RFC 0002 only, and the file
contained **0** occurrences of `informative`.

**New.** `depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004]`, with matching
*Relies on RFC 0003* (RFC3-16's owner-act record behind Status; RFC3-16(a) and
RFC3-15 behind RFC6-28's N/A judgment) and *Relies on RFC 0004* (RFC4-27
behind the coverage boundary) entries, plus a **Forward references are
informative** paragraph naming RFC8-12, RFC8-28, RFC9-14 and RFC9-41.

**Deliberate divergence from RD-9 f7's literal repair, recorded.** RD-9 f7 also
asked for **RFC-0008** in `depends_on`. This batch does **not** add it, and the
reason is a conflict between two findings of the same round: RD-18 verified —
and the acceptance record's Wave A row asserts — that *every `depends_on` edge
of these contracts stays inside the wave*, and RD-18 m5 explicitly notes the
correction it asks for keeps that true. An RFC-0006 → RFC-0008 edge would be
the wave's **only** cross-wave dependency, would falsify a record claim this
batch may not edit, and would weaken the "independently acceptable at position
1" property RD-18 credits to Wave A. The substance of f7 is discharged instead
by the staged citation in §8.3 and the staging paragraph — which is what a
non-dependency forward reference *is* in this corpus. **This is a judgment
call, and the fresh review should test it.**

### 8.5 RD-15 f1 — the outcome set was single-valued but never disjoint

**Old.** RFC6-5 declared a closed set of nine outcomes with *"exactly one
outcome"*, and at least four pairs overlapped on their face
(`resolved`/`unknown`, `retired`/`unconsented`, `resolved-absent`/`excluded`,
`unresolvable`/`incompatible-scenario`). Sweep over RFC6-1…RFC6-28:
`precedence` 0, `mutually exclusive` 0, `disjoint` 0. RFC6-7 asserts
determinism over that domain; RFC6-23 makes the resulting disagreement
release-blocking.

**New.** A **fail-closed total ordering** over eight of the nine values —
`excluded` · `unconsented` · `incompatible-scenario` · `unresolvable` ·
`retired` · `resolved-absent` · `unknown` · `resolved` — with the outcome
being the **first** whose condition holds. Policy states rank above identity
states, which rank above claim state.

**`not-applicable` is deliberately outside the ordering.** Its own row makes it
legitimate *per surface only*, which cannot be reconciled with RFC6-7's
cross-surface determinism if it competes with the kernel outcomes. The clause
now says it **never displaces the kernel outcome**: a surface with no
projection renders `not-applicable` *in place of its own projection* while the
kernel outcome and the drawer fact set stand, and it is those that RFC6-7
binds. This resolves an ambiguity the finding did not name but the repair
would otherwise have created.

### 8.6 RD-15 f2 + RD-9 f10 — Unknown reasons: multi-cause collapse and secondary annotations

**Old.** RFC6-5's `unknown` row: *"Carry **exactly one** RFC2-24 reason"* —
stated at *reference* level, while RFC2-24's "exactly one primary" is at
*claim-instance* level and RFC6-19 class 2 confirms an entity has several
governing claims. An entity Unknown for two causes had no lawful rendering.
Separately, RFC2-24 permits secondary annotations and **nothing** in RFC 0006
said whether they travel, render, or count — so two conforming surfaces could
produce different per-reason counts while both satisfying RFC6-17, which
RFC6-23 would then class as release-blocking.

**New.**
- RFC6-5 `unknown` row: carry **each governing claim instance's primary reason
  with its resolution route**, and any secondary annotations beside it —
  *"never collapsed to a single reference-level reason"*.
- RFC6-14: secondary annotations **travel with the primary, verbatim and
  marked as secondary**; an answer carrying the primary alone has dropped part
  of the epistemic state.
- RFC6-17: per-Unknown-reason counts are computed over **primary reasons
  only** — one claim instance contributes exactly one — with secondaries
  disclosed separately and never folded in.

**Why this split.** It is the only assignment that leaves RFC6-17's counts
deterministic while keeping RFC2-24's secondaries carried rather than
discarded — the reason RFC2-24 closed the secondary vocabulary in the first
place.

### 8.7 RD-15 f11 — an aggregate's own epistemic state

**Old.** RFC6-14 required *"Every entity, claim instance, **and aggregate**"*
to carry label + tier + reason + freshness — none of which RFC 0002 defines for
aggregates. Read literally it licensed a headline label over mixed membership,
VIS-1's named violation, as long as a composition was disclosed beside it.

**New.** RFC6-14 covers entities and claim instances; **an aggregate carries no
epistemic state of its own** — no aggregate-level label, tier, reason or
freshness — and carries its members' composition per RFC6-17 instead. The
clause states why: those four are defined for claim instances, not for sets.

### 8.8 RD-15 f10 — a selectable entity with no URL form

**Old.** RFC6-2 made selectable every profile entity loaded *"for the project
**or workspace**"*, while RFC6-8 pins a selection inside a **project identity**
with no workspace limb, and §7 defers workspace-level URLs to the portfolio
profile. A workspace-loaded entity was therefore selectable with no URL,
against RFC6-12 and VIS-7's link rule.

**New.** RFC6-2 is scoped to profiles loaded **for the project**, and states
that workspace-level entities are deferred with the portfolio profile (§7),
naming the reason. The alternative — giving RFC6-8 a workspace-identity limb —
would pre-empt SDR-29/30's deferred portfolio design.

### 8.9 X1 at RFC6-28

RFC6-28's scope read *"every observable consequence of **RFC6-1…RFC6-27**"* —
a self-excluding literal range, the exact shape RD-10 F1 found **blocking** in
RFC7-38. It now reads *"every observable consequence of **every clause of this
contract other than this one**"*. Same extension at these bytes; immune to
append. Recorded as a semantic-delta entry, not as an editorial claim, because
it changes what a future amendment's clauses fall under.

---

## 9. P-31 (RD-15 f3) — the drafted exemption arm, awaiting a ruling

| | |
|---|---|
| Clause | **RFC2-19** (`RFC-0002/reconciliation-chain.md`) |
| Disposition | `owner-decision(P-31)` — **the exemption arm only** is drafted, per the register's recommendation |
| Digest-moving | **yes** |

**The defect.** V0's flagship output — merged-but-unreconciled work rendering
*"reconciliation evidence absent / Unknown"* — is bound to **no RFC2-24
reason**, and RFC2-24 forbids minting, spelling or force-fitting one
downstream. Reason #2 `missing-evidence` describes a claim whose evidence was
sought and not found, which misdescribes a verdict never sought.

**What was drafted.** An **RFC8-12-shaped exemption**: the
`reconciliation-pending` state and its V0 rendering are **chain-state-local** —
never stamped with, counted among, or absorbed by an aggregate of RFC2-24
Unknown reasons, and never contributing to a project's Unknown-reason totals —
with the condition disclosed as a **fact of the render** in RFC2-24's own
terms: named, counted in its own right, expandable, routed to its resolving
action (run a reconciliation evaluation). The rendering still carries the
durable identity, the merge fact, and the warranted intent revision.

**How it is marked.** The clause carries a blockquoted **`[P-31 — drafted arm,
awaiting an owner ruling.]`** note stating both routes, why the thirteenth
reason is an owner act (A5 closed the list at twelve), that the paragraph is
candidate text ratified or reverted at the act, and that it is **deleted** if
the owner directs the thirteenth reason instead.

**Why the exemption is drafted here rather than described.** The owner rules
better on a written arm than on a description of one, and the exemption stays
entirely inside RFC 0002's own bytes — it reopens no closed list and pre-empts
nothing. RFC2-24 is **not** edited by this batch.

**Why RFC8-12 is cited without becoming a dependency.** It is cited as the
precedent shape the corpus already carries; the clause is self-standing without
it, and RFC 0002's staging paragraph covers the surface RFCs.

---

## 10. What this batch preserved, checked

- **Wave containment.** Every `depends_on` edge of all 19 modules still names
  a contract in RFC-0001…RFC-0006. The batch's three front-matter changes —
  RFC-0006 `+RFC-0003, +RFC-0004`; RFC-0002/rendering-vocabularies `+RFC-0003`;
  RFC-0003/governance-homes `−RFC-0004` — are all in-wave or removals.
- **Clause identity.** 341 numbered clauses defined, no duplicate definition,
  no clause outside its module's declared set, no renumbering, no new number.
- **Citation resolution.** Every `RFCn-m` cited in the corpus resolves to a
  defined clause (`verify_final_prespec.py`, this session).
- **Mission staging.** The RFC1-7 mission-profile limb and its
  *"loadable only where the Mission contracts … are accepted and active"*
  wording are **untouched**; no new RFC-0010/0011 reference was introduced
  anywhere in Wave A by this batch.

## 11. Handoffs — consequences outside this batch's boundary

1. **Regeneration, by script only.** `WAVE-A-MANIFEST.txt`,
   `ACTIVE-CONTRACT-MANIFEST.txt`, the acceptance record's Wave A argument,
   `05-CONTRACT-INDEX.yaml`, `CONTRACT-DEPENDENCY-INDEX.md` (the three
   `depends_on` changes move it), and `CONTEXT-BUDGET-REPORT.md` all drift from
   these bytes. All are outside this batch's file boundary; `--check` on the
   contract index, dependency index and budget report reports DRIFT as
   expected.
2. **RFC-0001's oversize justification.** The module grew from 8,556 to ~9,053
   words. It remains in `verify_final_prespec.py`'s `JUSTIFIED_OVERSIZE` list,
   but the justification text speaks of a *"floor established by two compaction
   passes"* — R-SCR/R-REC should decide whether that justification and the
   compaction report still describe the artifact honestly.
3. **CG-2a's five remaining retired-phrase sites** (`02-OWNER-DIRECTION-RECORD.md`,
   two archived round reviews, and two lines of a root-level prompt file) are
   R-REC/R-SCR territory; **zero** remain under `rfcs/**`.
4. **`manifests-and-namespace.md`'s RFC-0004 edge** and the RFC-0003 package
   README's aggregate edge were left as found (§6.2) — flagged for the fresh
   review, not repaired by inference.
5. **X2's Wave B twins.** RFC7-38, RFC8-32 and RFC9-52 must carry the §3
   sentence byte-for-byte; it is quoted there for exactly that comparison.
6. **P-33 arms are undrafted** (RD-18 B2, M5), and **P-31 needs a ruling before
   the Wave A re-offer** — the register's own recommendation.

---

*End of the Wave A (R-A) semantic delta. Fourteen of nineteen modules edited;
all edits digest-moving; nothing accepted, nothing installed, no act
performed.*


---

## 12. Addendum, 2026-08-10 — the per-consequence paragraph mirrored in (main session)

Wave B's repair of RD-10 F7 carried a secondary limb the Wave A batch did not
have in scope (RD-9 f11 never raised it): **"Rows are per observable
consequence, not per clause"** — a clause with five observable consequences
and one mapped requirement is not covered, and the matrix must disclose the
consequences it enumerates. Wave B's three phase clauses gained that
paragraph; Wave A's six did not, opening a divergence between shape-parallel
clauses. Per the Wave B delta's handoff 4, the main session closed it by
mirroring rather than removal: the paragraph was inserted, byte-identical
(whitespace-normalized), immediately after the §3 standardized sentence in
all six Wave A phase clauses (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27,
RFC6-28). Verified after insertion: a corpus-wide sweep (every `.md` under
`rfcs/`) finds the paragraph at exactly **nine** sites — the six above plus
Wave B's three — as **one** whitespace-normalized variant. Digest-moving in
all six files; the wave manifests are regenerated after this addendum, and
the fresh exact-package review binds to the post-mirror bytes.
