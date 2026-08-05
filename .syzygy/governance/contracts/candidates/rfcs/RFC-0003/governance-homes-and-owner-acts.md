---
id: RFC-0003
title: Project, Workspace and .syzygy/** Manifests — governance homes and owner acts
module: governance-homes-and-owner-acts
status_source: owner-act-record
clauses: "RFC3-15, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-17, RFC3-17(a) (every other RFC3-n lives in manifests-and-namespace.md)"
governs: [governance-homes, lifecycles, owner-acts, provenance, challenge-records]
applies_to: [kernel, workspace, all-surfaces]
depends_on: [RFC-0001, RFC-0002, RFC-0004, RFC-0005]
tags: [governance-categories, owner-act-provenance, adoption-lifecycle, kernel-records, bootstrap-correlation]
---

# RFC 0003 — Project, Workspace and .syzygy/** Manifests
## Module: governance homes and owner acts (RFC3-15 … RFC3-17(a))

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Package:** one of two modules of RFC 0003; see `README.md` for the clause-set
map and lookup rule. The manifest field contracts, workspace manifest,
namespace classes, migration rules and nesting resolution are in
`manifests-and-namespace.md` — cited here by clause ID.

**Serves:** VIS-4, VIS-6, VIS-7; SEC-2, SEC-3, SEC-4, SEC-5; architecture.md
(the `governance/` constitutional minimums, schema ownership split); SDR-4.
Builds on RFC 0001 (RFC1-5, RFC1-27) and RFC 0002 (RFC2-1 snapshot inputs,
RFC2-6, RFC2-13, RFC2-25). Rationale, amendment history and answered
questions: `../../history/RFC-0003-history.md`.

---

## 0. Scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module fixes **where governance artifacts live, what lifecycle each
class admits, and what makes an owner act real**. It is the part of RFC 0003
that other RFCs cite most: every gate in the corpus that honors a consent, an
approval, an adoption stamp, a policy, or a registry cites **RFC3-16(a)** from
here rather than restating the obligation.

- **§1.1** the five constitutional `governance/` categories, closed except by
  recorded owner widening (RFC3-15, RFC3-15(a)).
- **§1.2** category-appropriate lifecycles; the self-declared stamp versus
  effective status; **RFC3-16(a)** the owner-act provenance predicate — an
  artifact that *authorizes* something is honored only if its provenance is
  verifiable by a mechanism the governed tree cannot forge, because untrusted
  fleet workers commit into that tree; **RFC3-16(b)** what any conforming
  mechanism must bind; **RFC3-16(c)** the two provenance states an owner-act
  record may hold, which is what keeps a bootstrap act from being rendered as
  independently verified.
- **§1.3** the reserved `declarations/` category and the home of challenge
  submissions and their admission records (RFC3-17, RFC3-17(a)).
- **§2** violation cases; **§5** the open owner question carried here (q4).

Clause identities are package-wide: this module holds RFC3-15, RFC3-15(a),
RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-17 and RFC3-17(a). No
numbers are retired or merged anywhere in the package.

---

## 1. The contract

Clauses are numbered `RFC3-n` for stable citation. Amend in place; retire
rather than renumber.

### 1.1 Reserved governance categories

**RFC3-15.** The **five** constitutional categories of `.syzygy/governance/`
hold, exclusively — "exclusively" bounding what each category may contain,
and the five-category set itself being closed except by the two lawful
widenings this RFC records: the owner amendment that minted `records/` (B19,
RFC3-15(a)) and the **reservation** of `declarations/` at RFC3-17, which sits
beside the five as an additional reserved category (drafted default; §5 q4
OPEN) rather than inside any of them. A plane validator therefore accepts
exactly these six names and rejects a seventh; neither rejecting
`declarations/` nor admitting an unreserved directory is conforming:

| Category | May contain | Install gate |
|---|---|---|
| `doctrine/` | Adopted doctrine artifacts; Syzygy-drafted doctrine for undeclared projects, stamped unadopted | Owner adoption (`ADOPT DOCTRINE` in this repo's bootstrap; explicit owner adoption generally). Amendment: owner-only (VIS-4) |
| `contracts/` | Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts | Owner acceptance (for the foundational set, the digest-bound act defined by the active acceptance record — `ACCEPT COMPACTED FOUNDATIONAL RFCS: <manifest digest>`; owner sign-off per VIS-4 thereafter) |
| `policies/` | Quality, evidence, and security policies — including currency-bound declarations (RFC2-9), the secret-detection policy (SEC-5), deterministic challenge-resolution policies and challenge sweep policies (RFC2-13) | Owner approval; policy versions are snapshot inputs (RFC2-1 item 7) |
| `decisions/` | Recorded owner decisions: adoptions, dismissals (reason + expiry), adjudications, consent records (RFC3-7), overrules | Recording by the owner (or attributed on the owner's behalf); a decision is a warrant, never evidence |
| `records/` | **Kernel-authored durable facts minted on a non-owner actor's submission** (the only minting trigger — see RFC3-2's transition rule; kernel-computed expiry derives at evaluation and mints nothing): **challenge submissions** (RFC1-5, RFC2-12 — the submission is itself a distinct recorded artifact, per RFC3-17(a)), their admission and rejection records and submitted withdrawals (RFC2-13), and **walkthrough execution records** (the fact a comprehension walkthrough ran and what it walked — RFC7-30, RFC9-45). *Never* owner decisions, never policy, never claims — a walkthrough **judgment** (pass/fail and rationale) is an adjudication and lives in `decisions/` | **No install gate — these are recorded facts, not authorizations.** Minted by the kernel under its own rules; the *submission* they record is attributed, and the record itself is neither adopted nor adoptable |

**RFC3-15(a) — Why `records/` exists** (owner decision **B19**). A challenge
admission record is an **identity-bearing snapshot input** (RFC2-1 item 9)
and must therefore be durable; `cache/` and `local/` are barred to it
(RFC3-20/21), since a deletion-safe home for a snapshot input would let an
identity-bearing evaluation input vanish between evaluations. But it is not
doctrine, not a contract, not a policy, and **not an owner decision**. The
fifth category is an explicit widening of a structure this RFC calls
constitutional, made by owner amendment rather than by stretching a
category's "exclusively" — the precedent any future widening follows.

### 1.2 Lifecycle status and owner-act provenance

**RFC3-16.** **Lifecycle status: a self-declaration inside content, an
effective status outside it.**

**Category-appropriate lifecycles — there is no universal one.** Each
governance category carries the lifecycle its content class admits, and only
that:

| Content class | Lifecycle | Notes |
|---|---|---|
| `doctrine/`, `contracts/`, `policies/`, `declarations/` (normative artifacts) | draft → adopted/accepted → amended → retired | The adoptable class; RFC3-16(a) governs every act |
| `decisions/` and consent records | active → superseded / revoked / expired | A decision is **made**, never "adopted"; supersession and revocation are themselves recorded acts |
| `records/` (kernel records) | immutable recorded fact; plus withdrawal, supersession, or derived expiry where its governing contract defines them (RFC2-13) | **No adoption lifecycle exists for this class** — nothing here is adopted or adoptable (RFC3-15) |
| Governed presentation artifacts (e.g. the Polaris narrative, RFC 0007) | draft → adopted/published → superseded | Non-authoritative content with an adoption gate on publication |
| `cache/`, `local/` | none | No governance lifecycle; rebuildable / personal (RFC3-20/21) |

**The self-declared stamp.** An artifact of an adoptable or gated class
carries its **self-declared lifecycle status** as machine-readable content,
captured in the snapshot "with adoption status as a fact, not formatting"
(RFC2-1 item 2). A tree-resident stamp is **never self-authenticating**:
`accepted` written in a file is a claim by whoever wrote the file, not proof
of acceptance.

**Effective status is read from the owner-act record, not from the stamp —
and never by editing the artifact.** The **effective** lifecycle status of a
normative or authorization-bearing artifact is determined by an **owner-act
record** (RFC3-16(a)/(b)) binding the act to the artifact's **exact immutable
content digest** (RFC3-16(b) item 3). That record's own verification state is
**two-valued and never conflated** — *owner-adopted (bootstrap act)* or
*Syzygy-verified (effective act)*, per **RFC3-16(c)**, which fixes what each
state does and does not license Syzygy to claim. Consequences that bind:

- **Acceptance and adoption do not edit the artifact.** The accepted content
  is the content, at its digest, forever; a required post-act stamp edit
  would change the digest and thereby destroy the act it records. An artifact
  self-declaring `draft` whose exact digest carries an owner-act record **is
  effectively accepted**, to the extent RFC3-16(c) licenses for that record's
  state; the self-declaration is read as the state at authoring time.
- **The two must be readable apart.** Every surface and query answer
  distinguishes the self-declared stamp (untrusted content) from the
  effective status (derived from the owner-act record); where they disagree,
  the effective status governs the artifact's force and the disagreement
  renders as a disclosed fact, never silently reconciled in either direction.
- An artifact with **no** owner-act record at all has effective status
  **unadopted** whatever its stamp claims: it binds nothing, anchors nothing,
  and renders unadopted everywhere (v1.md drafting rule; RFC2-25
  `unadopted-draft`; RFC3-16(a)'s effect rule for the stamped-but-unverifiable
  case).

**Scope.** This clause and the RFC3-16(a) predicate govern
**authorization-bearing and normative artifacts** — the adoptable class,
decisions/consents, and gated presentation artifacts. Kernel records carry no
adoption lifecycle and are outside both (their authority is RFC3-2's
`kernel-recorded` class); `cache/` and `local/` are outside governance
entirely.

**RFC3-16(a). The owner-act provenance predicate.** An
**authorization-bearing governance artifact** is any artifact whose presence
**authorizes a dangerous act, unblocks or widens a claim class, fixes the
meaning of a rendered encoding, or otherwise binds project truth in a way no
downstream status check can falsify**.

[Inferred] The fourth limb is deliberately the vaguest and is retained for
that reason: the first three were derived from failures already found, and a
predicate that reaches only the failures already found is an enumeration
wearing a predicate's clothes. Where the fourth limb is the *only* one that
catches an artifact, the honest reading is that the artifact's class has not
yet been thought about properly — treat that as a finding, not as settled
coverage.

**That predicate is the scope; the list below is not.** An artifact
satisfying the predicate is in scope whether or not it appears among the
examples, whether or not the RFC introducing it cites this clause, and
whether or not it existed when this clause was written — a subject fixed by
enumeration leaves whichever class was added or patched last unguarded, the
failure mode this form exists to prevent. A gate reading an artifact not
listed here does not escape the predicate; it applies it. The classes that
follow are **non-exhaustive examples**, load-bearing as illustration and never
as the boundary:

- a **consent record** — observation, write, egress, or execution (RFC3-7;
  RFC5-12);
- an **approval, adjudication, or overrule Decision** (RFC3-15,
  `decisions/`), including the execution-profile approval (RFC5-18(c));
- an **adoption/acceptance stamp** (RFC3-16);
- an **owner-approved policy declaration whose effect is to unblock or widen
  what Syzygy may honor** (RFC3-15, `policies/`) — the marker-adoption policy
  (RFC4-26), the scheduler retention bound (RFC4-16), the currency-bound
  declaration (RFC2-9), the trusted-external-oracle declaration (RFC4-13),
  and the **substrate-to-normalized work-state derivation mapping**
  (RFC8-12) — a mapping row projecting a custom substrate status into `ready`
  or `active` makes the board and the endpoints report dispatch-eligible and
  live work, so a mapping an untrusted writer could mint would widen exactly
  what the surface says remains, is live, and is blocked.
- an artifact that **fixes the meaning of a rendered encoding** rather than
  reporting a fact under it — the channel registry from which all legend text
  is generated (RFC9-26) and the layout version registry (RFC9-18).
  [Inferred] This limb is not about widening a claim, which is why
  enumeration alone would have missed it: a forged registry entry leaves
  every claim, tier, and freshness check passing and changes what a *correct*
  render means, so no downstream status check can catch it (VIS-7's trust
  floor).

**The predicate.** Such an artifact is honored **only when its owner-act
provenance is independently verifiable to Syzygy by a mechanism the governed
tree cannot forge**. Being present, well-formed, and correctly attributed *in
the tree* is not sufficient. The premise, stated honestly: the plane is
in-tree by design (architecture.md, FD-034), and changes materialize through
fleet workers executing scheduled work (architecture.md's
worker-materialization model), so workers routinely commit into it; SEC-3
declares that actor class **untrusted regardless of who owns the project**
for executed code, and this package **[Inferred]** extends the same
classification to what those workers *commit* — an extension doctrine does
not state in so many words but which follows from the two rules read
together, and which every consuming gate rests on. A stored attribution field
is therefore a claim by whoever wrote the file, never evidence of an owner
act. This is the same reasoning that rejected designating the governance root
by field value (a field can dangle or lie; provenance cannot), extended to
the artifacts that authorize the dangerous acts.

**The mechanism class — chosen, not open.** The owner already chose the
mechanism class at acceptance (decision **A1**, reaffirmed at the rev8
rework): **correlation of the artifact to an owner-attended, Syzygy-mediated
ceremony recorded in an independently kept audit trail** (the RFC5-25 trail —
which must live outside `.syzygy/**` and outside the untrusted actor class's
write reach, or the correlation proves nothing). The floor property that
makes the class acceptable — forgery must require something the governed tree
does not contain — is satisfied by the trail's independence, not by anything
the owner holds. **Owner-held key or attestation custody is not an open
implementation alternative**: A1 explicitly declined to put custody burden on
the owner, and replacing the ceremony+audit model with an owner-held key or
attestation scheme requires a **later owner decision**, not an implementation
choice. Within the chosen class, implementation remains free on ceremony UI,
transport, audit-store technology, and record encoding. What any conforming
mechanism must *bind* is fixed now, at RFC3-16(b).

**RFC3-16(b). What an owner act binds: protocol-neutral semantics.**
RFC3-16(a) fixes when provenance is required; this sub-clause fixes what any
conforming mechanism must bind, so two implementations cannot diverge on the
meaning of "the owner approved this" while both citing the predicate. It
chooses no keys, signatures, or transports. A verifiable owner act binds, at
minimum, all of:

1. the **project identity** the act is made within;
2. the **stable identity of the artifact** acted on;
3. the **exact content or revision digest** of the artifact as acted on —
   **approving a path never approves future content at that path**; an
   artifact edited after the act is, for the predicate, an artifact with no
   act;
4. the **act type** (adopt, accept, approve, consent, dismiss, revoke, …)
   from the acting surface's own vocabulary;
5. the **owner attribution** — which owner, where multi-owner projects exist;
6. the **act instant**;
7. the **scope** of the act, where the act type carries one (a consent's
   content classes, an oracle's (project, gate class) pair);
8. the act's **supersession/revocation relationship** — what earlier act, if
   any, it replaces. **Revocation is itself an explicit act** with the same
   binding set; no act lapses silently except by an expiry the act itself
   declared;
9. the **identity of the audit record** (RFC5-25 or successor) that the
   correlation mechanism resolves to — always, under the A1 mechanism class
   bound at RFC3-16(a) — a trail that lives, normatively, outside
   `.syzygy/**` and outside the untrusted actor class's write reach
   (RFC5-25's location constraint), without which this item's correlation
   would be forgeable from inside the governed tree.

**Bootstrap correlation.** Artifacts adopted before any mechanism exists —
this repository's adopted doctrine and, on acceptance, these RFCs — have
their owner acts recorded as chat-phrase ceremonies plus git commits/tags.
When the mechanism first exists, the owner performs a **one-time recorded
correlation act** binding each already-adopted artifact's exact digest to its
historical act; until then those artifacts render with their gap stated
honestly (the A9 posture), not as verified. Rendering is the only effect
this paragraph adds; what a state-(1) record *suffices for* splits by role
(RFC3-16(c)): an artifact consumed as a **constraint** binds at full
strength — refusing to apply a constraint over uncorrelated provenance
would widen, not narrow — while an artifact consumed as an **authorization
for an effect** (a consent, an autonomy envelope, a write-expanding policy)
has not satisfied the RFC3-16(a) predicate on a state-(1) record alone, and
*Effect when the predicate fails* governs that effect until the correlation
act (RFC10-9 is the worked example). **A git tag or commit alone is
never silently sufficient**: the governed tree cannot prove who pushed it; it
may serve as *evidence within* a correlation, never as the mechanism.
[Inferred — the binding set; Observed — the path-vs-content and
untrusted-tree premises from RFC3-16(a).]

**Effect when the predicate fails.** An authorization present in the tree
without verifiable owner-act provenance is **never silently honored and never
silently deleted**. Its **dependent effect is blocked** — the egress is
refused, the run does not launch, the adapter write does not proceed, the
adoption does not bind, the policy does not widen anything — the
**authorization itself renders Unknown**, and the condition **mints a
contradiction routed to owner adjudication**: exactly the posture RFC3-3
takes for an inoperative write-expanding field and RFC3-9 takes for a
governance artifact Syzygy did not author. Blocking is not deletion: the
artifact and its unverifiable state both remain rendered.

**One predicate, one home.** Every consuming gate **cites this clause rather
than restating the obligation**. The gates today: RFC5-15 and RFC5-18(c)
cross-check it before acting; honored only under it are RFC5-14, RFC5-16
(also read at RFC4-12 and RFC3-30), RFC4-13, RFC4-13(b) (a governed checker
that can unblock positive status fixes the meaning of a certification),
RFC4-16, RFC4-26, RFC4-7, RFC2-13, RFC4-23(2), RFC8-16, RFC9-26, RFC9-18,
RFC9-45's walkthrough release policy and its leg-2 map walkthrough
**judgment**, and RFC 0007's owner judgments RFC7-21, RFC7-25 and RFC7-31. On
both walkthrough surfaces the *execution record* is `kernel-recorded` and
authorizes nothing, so it sits outside this predicate. [Inferred] Stating the
obligation per artifact class instead would leave whichever class was patched
last unguarded — the failure mode this single-predicate form exists to
prevent, and the same reason the clause's **subject** is the predicate rather
than the examples beneath it. **This list tracks the gates; it does not bound
them.**

**RFC3-16(c). Owner-adopted bootstrap act versus Syzygy-verified effective
act.** An owner-act record exists in exactly one of **two provenance
states**. Both are first-class and real; they are **never conflated**:

**(1) Owner-adopted (bootstrap act).** An owner act performed *before* the
independent A1 correlation mechanism of RFC3-16(a) exists, preserved as the
**exact owner phrase**, the **exact content digest** of the artifact acted
on, and the **git commit and tag** that record it. This is a **human/social
governance fact**: the owner and the humans working with them may lawfully
govern development by it, and the artifact's effective status *for human
governance* is read from that record. It is durable historical evidence — it
is **not** independently verifiable to Syzygy. Every tree-resident record
lies within the untrusted actor class's write reach (RFC3-16(a)'s premise),
**including a committed acceptance-act record under
`.syzygy/governance/decisions/`**; a same-tree committed record is therefore
never, by itself, the independently verified effective status.

**(2) Syzygy-verified (effective act).** A bootstrap act correlated through
the independent A1 mechanism (RFC3-16(a)) — an owner-attended,
Syzygy-mediated ceremony correlated to an audit trail living outside
`.syzygy/**` and outside the untrusted actor class's write reach, binding
RFC3-16(b)'s nine items. **Only this state supports the claim "independently
verified."**

Consequences that bind:

- Syzygy **never claims independent verification for an uncorrelated
  bootstrap act** — not on any surface, in any query answer, in any
  certificate, and not by implication from the presence of a committed
  record.
- Provenance **renders the correlation gap honestly** (the A9 posture). The
  truthful render of state (1) is **"owner-adopted (bootstrap,
  uncorrelated)"**; **never "verified."**
- The **one-time recorded correlation act** of RFC3-16(b)'s *Bootstrap
  correlation* paragraph **upgrades state (1) to state (2) without editing
  the artifact**: it binds the same exact digest, so correlation adds
  provenance and changes no content (RFC3-16's rule that acts never edit what
  they act on).
- **A git commit or tag alone is never sufficient for either state**: the
  governed tree cannot prove who pushed it; it may serve as *evidence within*
  a bootstrap record or within a correlation, never as the mechanism
  (RFC3-16(b)). An artifact with **no owner-act record at all** is in neither
  state and is effectively unadopted whatever its stamp claims (RFC3-16).
- Nothing here weakens RFC3-16(a): an authorization-bearing artifact resting
  on a state-(1) record has not satisfied the predicate, and RFC3-16(a)'s
  *Effect when the predicate fails* governs its dependent effects. The
  constraint half of the same split — a state-(1) artifact consumed as a
  constraint binds at full strength — is stated in RFC3-16(b)'s *Bootstrap
  correlation* paragraph; the two halves are one rule read from either end.

[Inferred — the two-state distinction and its render vocabulary; Observed —
the untrusted-tree premise (RFC3-16(a)), the A1 mechanism class and A9
interim posture, and the never-sufficient rule for commits and tags
(RFC3-16(b)).]

### 1.3 The `declarations/` category, and where challenge records live

**RFC3-17.** This RFC reserves an additional category,
`.syzygy/governance/declarations/`, as the governance-plane home for the
declaration artifacts RFC 0001 names: capability declarations, declared
topology, declared regions, declared implementation mappings (SDR-4), and
promoted annotations/designations. Doctrine leaves their placement within
`governance/` to RFCs (architecture.md); their internal schemas belong to RFC
0004 and the surface RFCs. Install gate: owner sign-off (they are
shape-defining, VIS-4); Syzygy-drafted entries stamp unadopted per RFC3-16.

**RFC3-17(a). Where challenges and their admission records live.** Challenge
submissions (RFC1-5, RFC2-12) and their admission-or-rejection records
(RFC2-13) live in **`.syzygy/governance/records/`** — RFC3-15's fifth
constitutional category — under write authority **`kernel-recorded`**
(RFC3-2's fourth class). There is no `governance/challenges/` category; a
conforming implementation may not create one, and may not choose any home for
these artifacts other than `records/`.

**Why `records/` and nothing else** (full reasoning: history RFC3-17(a)).
RFC2-13 makes the admission-or-rejection record a *kernel fact written to the
governed plane* and RFC2-1 item 9 makes it a **snapshot input**, so it is
identity-bearing, durable and deletion-unsafe: `cache/` and `local/` are
barred (RFC3-20/21), `intent/`/`work/`/`map/` are surface namespaces (RFC3-18)
and no surface owns challenge state, and the artifact is not doctrine, not a
contract, not a policy, and — decisively — **not a recorded owner decision**.
The one challenge-adjacent thing `governance/` holds elsewhere is the
*resolution policy* in `policies/`, which is not the challenge.

**Consequences that bind.** The records are **minted by the kernel, never
owner-authored**; the challenger's inference provenance — or a human
challenger's attribution — is a **field of the record**, never its write
authority. They are **immutable once written** (RFC2-6); a challenge is never
edited to change its verdict. A `kernel-recorded` value is **never
authorization-bearing** (RFC3-2), so nothing in `records/` is adopted or
adoptable. **Resolution acts that are owner acts** — upholding, dismissing,
or expiring a challenge — are recorded in `decisions/` (RFC3-15) and
*referenced* from the challenge record, never embedded in it. Because
`records/` sits inside `governance/**`, which fleet workers can write (the
untrusted-writer premise at RFC3-16(a), extending SEC-3's actor class), an
admission record's authority is the kernel's recomputation of the RFC2-13
check over the snapshot, never the file's own say-so. [Observed — home,
authority class and gate column from RFC3-15/RFC3-2 as amended by B19;
durability and snapshot-input facts from RFC2-1 and RFC2-13.]

---

## 2. Violation cases

*(Cases for the manifest, workspace, namespace, migration and nesting clauses
are in `manifests-and-namespace.md` §3. Original numbering is preserved
package-wide; this module carries 7, 13, 14 and the challenge-record limb of
9.)*

7. *(RFC3-15/16)* A drafted, unadopted doctrine file is cited as binding; or
   an accepted RFC is installed into `contracts/` with no owner acceptance
   recorded.
9. *(RFC3-17(a); RFC3-20)* A challenge admission record — a snapshot input
   under RFC2-1 item 9 — is written to `cache/` and a purge silently
   un-suspends every claim it suspended. *(The observation-record and
   `local/` limbs of case 9 are carried at `manifests-and-namespace.md` §3
   under RFC3-20/21.)*
13. *(RFC3-16(a))* A fleet worker commits an egress-consent record naming a
    new provider plus the matching `consents[]` reference, and the next
    evaluation honors it because the record's attribution field says "owner";
    or an unverifiable authorization is quietly dropped from the plane
    instead of rendering Unknown and minting a contradiction.
14. *(RFC3-16(c))* An artifact carrying only a bootstrap-act record — phrase,
    digest, commit and tag, no correlation — renders as "verified"; or the
    committed acceptance-act record in `governance/decisions/` is treated as
    itself the independent verification; or a correlation act is performed by
    editing the artifact's stamp, changing the digest the act was made against.

---

## 3. Integration

**Relies on RFC 0001:** the challenge entity and materialization-record rows
(RFC1-5); the Proposal gate this module's failure posture mirrors (RFC1-27).
**Relies on RFC 0002:** snapshot inputs (RFC2-1 items 2, 7 and 9) that make
adoption stamps, policy versions and open challenges identity-bearing;
kernel-fact immutability (RFC2-6); the challenge admission check and
resolution policy (RFC2-13); the `unadopted-draft` surface state (RFC2-25).

**Relies on the package's other module:** RFC3-2's four write-authority
classes (the `kernel-recorded` class this module's `records/` category
pairs with); the consent records stored under `decisions/` (RFC3-7); the
cache/local bars (RFC3-20/21); the surface namespaces (RFC3-18); and the
inoperative-field and unauthored-artifact postures RFC3-16(a)'s failure rule
mirrors (RFC3-3, RFC3-9).

**Provides to every downstream RFC, 0004–0011:** the owner-act provenance
predicate **RFC3-16(a)**, its binding set **RFC3-16(b)**, and the two
provenance states **RFC3-16(c)** — consuming gates are enumerated at *One
predicate, one home*, and **that enumeration tracks the gates and does not
bound them**, so a new gate in any RFC applies the predicate whether or not
it appears there. **To RFCs 0004 and 0006–0009 in particular:** the
`declarations/` category as the governance-plane home for capability,
topology, region and implementation-mapping artifacts (RFC3-17), whose
internal schemas those RFCs own.

---

## 4. Deliberately deferred

The internal schemas of the declaration artifacts homed at RFC3-17 → RFC 0004
and the surface RFCs. The ceremony UI, transport, audit-store technology and
record encoding of the A1 mechanism → first implementation slice, bounded by
RFC3-16(b)'s binding set. The one-time bootstrap correlation act's operational
procedure → the implementation slice that first provides the mechanism;
RFC3-16(c) fixes what it must achieve, not how it runs.

---

## 5. Open questions for acceptance

*(Package-wide numbering is immutable. q1 and q2 are carried by
`manifests-and-namespace.md`; q3, q5 and q6 are answered and recorded in
history §8. No question is renumbered.)*

**q4. The `declarations/` category (RFC3-17) — OPEN.** Confirm reserving a
further governance category for declaration artifacts, or direct that they be
distributed among the constitutional minimums (five since B19) — topology and
mappings as `contracts/`? regions as `decisions/`? Distribution avoids a new
category but blurs each category's one-line meaning. B19 settled only the
*challenge* half of the original pairing (q6) and did **not** rule on
`declarations/`. **Drafted default in force until the owner rules:**
RFC3-17's reservation of `declarations/` **outside** RFC3-15's constitutional
five stands as written, reversible by amendment. B19's precedent — widen
explicitly rather than stretch a category's "exclusively" — is the pattern
either answer should follow.

---

*End of module. Clauses RFC3-15, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b),
RFC3-16(c), RFC3-17 and RFC3-17(a). Every other number in RFC3-1 … RFC3-32 is
in `manifests-and-namespace.md`; no number is retired or merged.*
