# RFC 0003 — Project, Workspace and .syzygy/** Manifests

**Status:** Proposed foundational contract. This line is a self-declaration at authoring time (RFC3-16): effective status is established solely by the owner-act record binding this file's exact content digest, and acceptance edits nothing here. Absent such a record, this contract binds nothing.
**Date:** 2026-07-30 (amended through 2026-08-02)
**Serves:** VIS-3, VIS-4, VIS-5, VIS-6, VIS-7; SEC-2, SEC-4; architecture.md (governance-root invariant, two-namespace plane, `.syzygy/` layout, schema ownership split); SDR-7, SDR-28, SDR-29, SDR-30, SDR-32; resolves SDR §5 question 6. Builds on RFC 0001 (§3.1 project/repository/consent semantics, RFC1-28/29) and RFC 0002 (RFC2-1/2, RFC2-23/24 Unknown reasons).

---

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- This RFC governs **what lives on disk and who may write it**: the project
  declaration (`.syzygy/project.yaml`), the platform-level workspace
  manifest, and every `.syzygy/**` directory's authority class.
- **Every field has exactly one writer**, from four classes: owner-adopted,
  Syzygy-drafted (pending owner sign-off), Syzygy-maintained (mechanical),
  and kernel-recorded (facts about someone else's submission). The
  kernel-recorded class pairs with a **fifth governance category,
  `governance/records/`** — the home of challenge submissions, their
  admission/rejection records, and walkthrough execution records; recorded
  facts that authorize nothing and are never adoptable (both halves of
  owner decision B19).
- **No configuration can widen Syzygy's write access.** Syzygy writes only
  `openspec/**` and `.syzygy/**`; a field claiming otherwise is inoperative
  and surfaced as a contradiction.
- The single most consequential clause is **RFC3-16(a)**: any artifact that
  *authorizes* something (a consent, an approval, an adoption stamp, a policy
  that widens what Syzygy may honor) is honored **only if its owner-act
  provenance is verifiable by a mechanism the repo itself can't forge**.
  A file saying "the owner approved this" is a claim, not proof — because
  untrusted fleet workers can commit into the same tree. Until the
  verification mechanism exists (first implementation slice), such artifacts
  render Unknown and their effects are blocked.
- **Consent is per-(project, repository) and per-(project, provider)**,
  recorded, revocable, and revocation degrades claims to Unknown — it never
  erases history.
- The **workspace manifest** (which projects you see, how they're grouped)
  is personal presentation state: deleting it changes nothing true.
- **Nested subprojects are composition by declaration**: a "subproject" is a
  full governed project related by declared edges — never a second
  governance root inside one repo.
- Schema **migrations are explicit, reviewed, identity-preserving acts** —
  never lazy rewrites on read, never a rename of anything a citation
  depends on.

Structure: §3 is the contract (RFC3-1 … RFC3-32, plus lettered sub-clauses
— RFC3-15(a), RFC3-16(a), RFC3-16(b), RFC3-17(a)); §4 violation cases; §8
owner questions, answered ones marked in place.

---

## 1. Summary

The semantic contract for Syzygy's declared surfaces on disk: the **project
declaration** (`.syzygy/project.yaml`), the platform-level **workspace
manifest**, and the authority classes of every `.syzygy/**` namespace. It
fixes field *meanings* and *write authority*, never storage engines or
serialization detail beyond what authority requires. It binds: the
governance root designated by the location of the project declaration
itself; consent as recorded, revocable, per-(project, repository) and
per-provider records whose withdrawal degrades claims to Unknown rather
than erasing history; a workspace manifest that owns only workspace
concerns and is never authoritative for project-internal truth (SDR-29/30),
with explicit asymmetric-relation rendering; identity-preserving, reviewed
migrations for `.syzygy/**`; the hard rule that **no manifest field may
expand the two-namespace write universe**; the `openspec/**` boundary
(SDR-32 spec anchors); and a resolution of the seed's "recursively nested
subprojects" against the one-root invariant: **composition by
declaration** — nesting is a declared cross-project relation between whole
governed Projects, never a sub-root inside one.

---

## 2. Motivation and doctrine grounding

[Observed] Doctrine fixes the shape and defers the contract: a governed
project has exactly one governance root holding the single `openspec/**` +
`.syzygy/**` plane; `project.yaml`'s representation is "RFC material"
(architecture.md, Definitions); the four `governance/` categories are
constitutional minimums whose deeper organization "remains RFC material";
`.syzygy/**` is Syzygy's native, schema-versioned namespace migratable only
through "explicit, reviewable, identity-preserving migrations"
(architecture.md, schema ownership). SDR §5 q6 routes `project.yaml`, the
workspace manifest, and `.syzygy/**` versioning/migration here. SDR-28/29/30
resolve OQ-010's portfolio tension: portfolio truth is derived; the
workspace manifest owns only workspace concerns and is never authoritative
for project-internal truth.

[Inferred] The failure mode this contract guards against is **authority
creep through configuration**: manifests are where write universes quietly
grow, where portfolio state accretes inside Syzygy against VIS-6, and where
a migration silently renames an identifier that a dismissal, consent, or
map anchor depended on. Every clause below makes one of those creeps a
recognizable violation instead of a default.

---

## 3. The contract

Clauses are numbered `RFC3-n` for stable citation. Amend in place; retire
rather than renumber. Parentheticals beginning
*History:* are amendment records — when and why text changed — and carry
no normative force; the clause text around them is the contract.

### 3.1 Manifest principles and write containment

**RFC3-1.** This RFC defines manifests as **semantic contracts**: which
fields exist, what each means, and who may write it. Serialization detail is
bound only where doctrine already binds it: the project declaration is the
file `.syzygy/project.yaml` (name and location fixed by architecture.md's
layout); everything else in this RFC names no file format, storage engine,
or wire encoding. The `.yaml` filename is already a wire-format commitment,
so its **exact dialect** (YAML version, coercion rules, duplicate-key
handling) **is fixed by the first accepted spec that parses it, and is a
conformance item from then on**: two implementations disagreeing on whether
one `project.yaml` parses — and therefore on whether a governance root
exists — is a contradiction routed to the owner, never a
dialect-preference each side may keep. *(History: bound at rev7 review 9, boundary
finding 8; no stack neutrality is spent — the choice was already made by
the filename doctrine fixed.)*

**RFC3-2.** **Every manifest field names exactly one write authority**, from
**four** classes: **owner-adopted** (only the owner adopts the value; Syzygy
may draft, per VIS-4), **Syzygy-drafted** (Syzygy authors, value renders
unadopted until owner sign-off), **Syzygy-maintained** (mechanical
values Syzygy writes under this RFC's own rules, e.g. schema-version stamps
under §3.7), and **kernel-recorded** (values the kernel writes as a factual
record of a **non-owner actor's** submission — see below). No field has two
writers; a field whose authority is not declared by its governing RFC may not
exist.

**The fourth class is `kernel-recorded`** *(History: added at acceptance by owner
decision B19, together with RFC3-15's `records/` category).* It covers a fact
the kernel authors **on someone else's act**: a challenge admission or
rejection record, a submitted withdrawal, a walkthrough execution record. The
writer is
the kernel and the writer is single, so RFC3-2's one-writer rule holds; what
distinguishes the class is that the **content originates outside the kernel and
outside the owner**, and the record therefore asserts *that a submission
occurred*, never that its content is true.

**Which lifecycle transitions mint a record** *(History: pinned at rev7 review 9,
finding S6, so two implementations cannot produce different snapshot
identities over one tree)*: a `records/` fact is minted **only on an actor's
submission** — a challenge submitted (and its admission or rejection), a
withdrawal submitted, a walkthrough run submitted. **Owner resolution acts**
— upholding, dismissing, or expiring a challenge by decision — are Decisions
in `decisions/` (RFC3-15), referenced from the record, never minted into
`records/`. **Kernel-computed expiry** — a challenge lapsing because the
declared bound has passed (RFC2-3, RFC2-13) — is **derived state computed at
each evaluation** from the admission record's instant and the declared
bound; it mints **no record**, because it involves no act: it is
reproducible from snapshot inputs the tree already holds, so minting it
would add a snapshot input (RFC2-1 item 9) that pure recomputation created.

[Inferred] The three original classes did not fit this, and the drafted
workaround — Syzygy-maintained with the challenger's identity carried as an
ordinary field — was sound under the one-writer rule but misdescribed the
authority: "Syzygy-maintained" implies a mechanical value Syzygy derives, and
a challenger's submitted concern is neither mechanical nor Syzygy's. A reader
checking who stands behind the value would get the wrong answer. **A
`kernel-recorded` value is never authorization-bearing**: it records, and
recording authorizes nothing. Anything in this class that *would* authorize —
a resolution policy, a sweep policy, an approval — is by that fact not in this
class and falls under RFC3-16(a) instead.

**RFC3-3.** **Direct-write containment.** No field of any manifest —
project declaration, workspace manifest, or any `.syzygy/**` artifact — may
authorize, imply, or configure a Syzygy direct write outside `openspec/**`
and `.syzygy/**` (VIS-5). Fields naming paths outside the two namespaces
are **read/observation declarations only** (declared source roots, evidence
locations). A field purporting to grant write access elsewhere is
**inoperative** — Syzygy must not honor it — and its presence is surfaced
as a contradiction routed to the owner, never silently ignored or silently
obeyed.

### 3.2 The project declaration — `.syzygy/project.yaml`

**RFC3-4.** **Location is designation.** The project declaration lives at
`.syzygy/project.yaml` in exactly one repository, and that location — not
any field value — is what designates the repository as the Project's
governance root. A repository carries at most one `.syzygy/` plane, at its
root, and is the governance root of at most one Project. A declaration
purporting to designate a *different* repository as root, or a Project
resolving to zero or two roots, is a contradiction per RFC1-1 — routed to
the owner, never repaired silently.

**RFC3-5.** The declaration's top-level field set is **closed** at:

| Field | Meaning | Authority (RFC3-2) |
|---|---|---|
| `schema_version` | The `.syzygy/**` plane schema version (§3.7) | Syzygy-maintained (migration rules only) |
| `project` | Opaque project identifier + display-name label (RFC1-10: rename changes the label, never the identifier) | Owner-adopted |
| `owner` | Attribution of the single accountable owner | Owner-adopted |
| `repositories[]` | Declared membership: per entry an opaque repository identifier (RFC1-2), role (`governance-root` \| `observed-source`), mutable non-identity locator hints (URL, path, default branch), and a consent-record reference | Owner-adopted; Syzygy-drafted entries render unadopted |
| `consents[]` | References to consent records in `governance/decisions/` (RFC3-7); never the records themselves | Owner-adopted (the referenced records are governance acts) |
| `declarations` | References locating the project's declaration artifacts: capability, topology, declared-region, and implementation-mapping artifacts (`governance/` per RFC3-19) and the spec root (`openspec/`, fixed) | Syzygy-drafted, owner-adopted |
| `relations[]` | **Outbound** declared cross-project relations (RFC3-14, RFC3-31): (relation type, counterpart project identifier) | Owner-adopted |
| `profiles[]` | Extension profiles loaded for this project (RFC1-7); never presumed present | Owner-adopted |

Additions to this field set require an amendment to this RFC. Sub-schemas
beneath `declarations` targets belong to RFCs 0004 and 0007–0009.

**RFC3-6.** **Repository entries.** Repository identity is the declared
opaque identifier — never a URL, path, or branch (RFC1-2); locator hints
may change without touching identity. An entry whose consent reference does
not resolve to an in-force consent record is **not observed**: its content
renders Unknown (`unconsented-source-or-provider`, RFC2-24 #6), never an
empty graph read as absence (RFC1-3).

**RFC3-7.** **Consent records** are governance acts stored in
`.syzygy/governance/decisions/`, referenced — never embedded — from the
declaration. Two kinds, matching their doctrine sources:

- **Observation/write consent** (SEC-4): subject is the pair *(observing
  Project, repository)*; scope enumerates what is consented — observe,
  write (governance-root plane only), and, when the execution-profile RFC
  exists, execute (SEC-3). Every observed repository requires one, governed
  root or not.
- **Egress consent** (SEC-2): subject is the pair *(Project, external
  provider)*; content names the permitted provider and the **set** of
  content classes that may be sent. **One record per *(Project, provider)*
  pair, naming the permitted set — never one record per content class**
  (SEC-2's own wording; aligned with RFC5-12/RFC5-14). Model providers are
  such providers. Providers not named require fresh consent. *(History:
  post-draft amendment under review 3's AS-R10, removing an internal inconsistency
  with RFC 0005. The granularity question was **answered at acceptance by
  owner decision B8** — one record per (project, provider); the finer
  per-content-class and the per-repository alternatives were both
  declined — see §8 q3.)*

Every consent record carries attribution, grant timestamp, and scope, and
is individually revertable. Attribution is a stored field and therefore a
*claim* about who granted it; it is honored only under the owner-act
provenance predicate of RFC3-16(a). [Inferred] Scoping observation consent
to the *(Project, repository)* pair, not the bare repository, is required by
§3.9's dual-role rule: consenting to observation by one project must not
silently admit another.

**RFC3-8.** **Revocation and withdrawal.** Revoking consent is a recorded
governance act — narrowing or withdrawal — never deletion of the record.
Effect on **claim values**, always through the next identified evaluation
(RFC2-4): dependent claims render Unknown
(`unconsented-source-or-provider`); inference overlays for a withdrawn
provider are not computed (RFC2-7); prior observation records remain —
immutable, VIS-6, exception (b) — but render with the withdrawal visible
(RFC2-23, "Consent withdrawn"). Effect on **rendering**, immediately at the
revocation record: every subsequent served render of a dependent claim
carries the withdrawal label before and independent of that evaluation
(RFC5-11's rendering obligation). Enforcement — what may be read, egressed,
or launched — stops at the next act, not at the next evaluation (RFC5-11).
Withdrawal never rewrites history and never silently empties a surface.

**RFC3-9.** **Drafting and repair.** On a newly governed or undeclared
project, Syzygy may draft declaration content (membership, declaration
references) as first-pass work [Observed: v1.md, non-code writes]; drafted
values render unadopted and bind nothing until owner sign-off. An
unparseable or invalid `project.yaml` renders every dependent claim Unknown;
Syzygy never auto-repairs it — a repair is a Proposal (RFC1-27) through the
owner gate, and Syzygy never overwrites a governance artifact it did not
author without surfacing the conflict (SEC-4).

### 3.3 The workspace manifest (platform level)

**RFC3-10.** The **workspace manifest** is the owner's platform-level
manifest, living **outside every governed plane** (in Syzygy's own home,
not in any governed repository). It is classified under **VIS-6, exception
(a)** — personal presentation state: it may never affect truth, work,
status, or certificates, and it is never a snapshot input (RFC2-1).
[Inferred] This classification is what makes a platform-level file lawful
at all: the only doctrine-recognized states outside the governed planes are
the two closed VIS-6 exceptions, and the workspace manifest's SDR-29
concerns are presentation-shaped.

**RFC3-11.** Its field set is **closed at SDR-29's list**: local project
membership (which governed projects this workspace shows), grouping and
ordering, saved cross-project views, and owner-specific portfolio
narrative/dashboard preferences. Additions require an amendment to this
RFC. Authority: owner-adopted or Syzygy-maintained-as-preference; never
Syzygy-inferred into semantic content.

**RFC3-12.** **Never authoritative for project-internal truth (SDR-30).**
No kernel fact, claim, gap, consent, capability, or relation may cite the
workspace manifest as its source. Adding or removing a project from the
workspace changes what is *rendered*, never any project's state, consent,
or membership. Portfolio truth is **derived** from governed projects'
own declarations (SDR-28) — the union is computed, rebuildable (VIS-6),
and re-derivable from the planes alone with the workspace manifest deleted.

**RFC3-13.** The workspace manifest **references project identities minted
in project declarations; it never mints one**. An entry whose project
identifier cannot be resolved (repository unreachable, plane absent,
consent withdrawn) renders Unknown with its RFC2-24 reason — never dropped,
never guessed.

**RFC3-14.** **Asymmetric relation semantics.** Cross-project semantic
relationships come only from project declarations (`relations[]`, RFC3-5).
When Project A declares a relation to Project B and B declares no
counterpart:

- rendered **from A's side**: *declared by A, unconfirmed by B* — a
  declared fact about A's intent, never evidence about B;
- rendered **from B's side**: *asserted by A, undeclared here* — visibly
  external, never entering B's own declared state;
- a relation renders **confirmed** only when both projects declare
  compatible counterparts; incompatible mutual declarations render both
  claims side by side, attributed — never silently reconciled and never
  auto-completed by Syzygy or the workspace manifest.

[Inferred] Mutually incompatible declarations are *not* a kernel
contradiction — each lives in its own project's declared scope — so the
honest rendering is both-visible-unconfirmed, routed to the owner as a
finding, not adjudication-blocked.

**The Project→Project dependency relation is named `depends-on`, and the name
collides deliberately.** *(A draft had renamed it to `relies-on-project` to
avoid the collision; the owner reverted that rename at acceptance (B20),
restoring the original `depends-on` having been shown the collision and its
consequence.)* This relation is a **portfolio-profile** relation (RFC1-7),
Project→Project, of **Desired (declared)** semantic class and **owner-adopted**
authority — an assertion of the owner's intent about how two projects stand to
one another. RFC1-25's V0 `depends_on` is a different relation entirely: it is
closed to two endpoint pairs, Work item→Work item (execution class,
scheduler-authoritative) and Code element→Code element (observed class).
RFC1-26 permits profiles to **add** relations but not to **re-type** the closed
set; this relation is an addition, and `depends_on` is not widened to a third
endpoint pair.

**The consequence of the reverted rename is normative, not stylistic.** This
relation and the kernel's `depends_on` differ by exactly one character, in
different semantic classes, with different authorities. **The names therefore do
not separate the senses, and the whole separation is carried by RFC1-25(b)'s
twelve-pair anti-conflation invariant** — which is for that reason a
mechanically checkable rule and a named test-coverage obligation of the first
implementation slice, rather than the prose rule a distinct verb would have
allowed. Any surface, legend, query, or count that unions this relation with
`depends_on`, or treats either as evidence of the other, violates RFC1-25(b);
labelling the union does not cure it. A query author or legend generator
reading only the relation names **will** conflate them, so conformance here
rests on the invariant being tested, not on the reader being careful.
[Inferred — the collision is the owner's decision; its elevation of RFC1-25(b)
from prose to a tested invariant is this RFC's, recorded so the cost of the
naming choice stays attached to the choice.]

### 3.4 Reserved governance categories

**RFC3-15.** The **five** constitutional categories of
`.syzygy/governance/` hold, exclusively — "exclusively" bounding what each
category may contain, and the five-category set itself being closed except
by the two lawful widenings this RFC records: the owner amendment that
minted `records/` (B19, RFC3-15(a)) and the **reservation** of
`declarations/` at RFC3-17, which sits beside the five as an additional
reserved category (drafted default; §8 q4 OPEN) rather than inside any of
them. A plane validator therefore accepts exactly these six names and
rejects a seventh; neither rejecting `declarations/` nor admitting an
unreserved directory is conforming:

| Category | May contain | Install gate |
|---|---|---|
| `doctrine/` | Adopted doctrine artifacts; Syzygy-drafted doctrine for undeclared projects, stamped unadopted | Owner adoption (`ADOPT DOCTRINE` in this repo's bootstrap; explicit owner adoption generally). Amendment: owner-only (VIS-4) |
| `contracts/` | Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts | Owner acceptance (`ACCEPT FOUNDATIONAL RFCS` for the foundational set; owner sign-off per VIS-4 thereafter) |
| `policies/` | Quality, evidence, and security policies — including currency-bound declarations (RFC2-9), the secret-detection policy (SEC-5), deterministic challenge-resolution policies and challenge sweep policies (RFC2-13) | Owner approval; policy versions are snapshot inputs (RFC2-1 item 7) |
| `decisions/` | Recorded owner decisions: adoptions, dismissals (reason + expiry), adjudications, consent records (RFC3-7), overrules | Recording by the owner (or attributed on the owner's behalf); a decision is a warrant, never evidence |
| `records/` | **Kernel-authored durable facts minted on a non-owner actor's submission** (the only minting trigger — see RFC3-2's transition rule; kernel-computed expiry derives at evaluation and mints nothing): **challenge submissions** (RFC1-5, RFC2-12 — the submission is itself a distinct recorded artifact, per RFC3-17(a)), their admission and rejection records and submitted withdrawals (RFC2-13), and **walkthrough execution records** (the fact a comprehension walkthrough ran and what it walked — RFC7-30, RFC9-45). *Never* owner decisions, never policy, never claims — a walkthrough **judgment** (pass/fail and rationale) is an adjudication and lives in `decisions/` | **No install gate — these are recorded facts, not authorizations.** Minted by the kernel under its own rules; the *submission* they record is attributed, and the record itself is neither adopted nor adoptable |

**RFC3-15(a) — Why `records/` exists** *(History: added at acceptance by owner decision
B19).* A challenge admission record is an **identity-bearing snapshot input**
(RFC2-1 item 9) and must therefore be durable — `cache/` and `local/` are
barred to it (RFC3-20/21), since a deletion-safe home for a snapshot input
would let an identity-bearing evaluation input vanish between evaluations. But
it is not doctrine, not a contract, not a policy, and **not an owner
decision** — it is a fact the kernel authors when a challenger submits. Before
this category it fitted none of the four and the RFC named no home, which
meant two conforming implementations would choose differently and at least one
would choose `cache/`. The fifth category is an explicit widening of a
structure this RFC calls constitutional, made by owner amendment rather than by
stretching a category's "exclusively".

**RFC3-16.** **Lifecycle status: a self-declaration inside content, an
effective status outside it.** *(History: rewritten at the rev8 rework, items 2
and 3 — the earlier text imposed one universal
draft/adopted/amended/retired lifecycle on every reserved category,
contradicting RFC3-15's own `records/` row, and made adoption status
in-content in a way that forced a digest-changing edit after every owner
act, contradicting RFC3-16(b) item 3.)*

**Category-appropriate lifecycles — there is no universal one.** Each
governance category carries the lifecycle its content class admits, and
only that:

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
`accepted` written in a file is a claim by whoever wrote the file, not
proof of acceptance.

**Effective status is established by the owner-act record, not by the
stamp — and never by editing the artifact.** The **effective** lifecycle
status of a normative or authorization-bearing artifact is determined by
the existence of an independently verifiable **owner-act record**
(RFC3-16(a)/(b)) binding the act to the artifact's **exact immutable
content digest** (RFC3-16(b) item 3). Consequences that bind:

- **Acceptance and adoption do not edit the artifact.** The content that
  was accepted is the content, at its digest, forever; requiring a
  post-act stamp edit would change the digest and thereby destroy the
  very act it records. An artifact whose content self-declares `draft`
  and whose exact digest carries a verifiable acceptance act **is
  effectively accepted**; the self-declaration is understood as the
  historical state at authoring time.
- **The two must be readable apart.** Every surface and query answer
  distinguishes the self-declared stamp (untrusted content) from the
  effective status (derived from the owner-act record); where they
  disagree, the effective status governs the artifact's force and the
  disagreement itself renders as a disclosed fact, never silently
  reconciled in either direction.
- An artifact with **no** verifiable owner-act record has effective
  status **unadopted** whatever its stamp claims: it binds nothing,
  anchors nothing, and renders unadopted everywhere (v1.md drafting rule;
  RFC2-25 `unadopted-draft` surface state; RFC3-16(a)'s effect rule for
  the stamped-but-unverifiable case).

**Scope.** This clause and the RFC3-16(a) predicate govern
**authorization-bearing and normative artifacts** — the adoptable class,
decisions/consents, and gated presentation artifacts. Kernel records carry
no adoption lifecycle and are outside both (their authority is RFC3-2's
`kernel-recorded` class); `cache/` and `local/` are outside governance
entirely.

**RFC3-16(a).** **The owner-act provenance predicate.** *(History: post-draft
amendment, added under review 3's Blocker AS-R1; lettered as a sub-clause of
RFC3-16 so the RFC3-1 … RFC3-32 range stays closed.)*

An **authorization-bearing governance artifact** is any artifact whose
presence **authorizes a dangerous act, unblocks or widens a claim class,
fixes the meaning of a rendered encoding, or otherwise binds project truth in
a way no downstream status check can falsify**.

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
whether or not it existed when this clause was written — for exactly the
reason recorded at *One predicate, one home* below: a subject fixed by
enumeration leaves whichever class was added or patched last unguarded, and
that is the failure mode this form exists to prevent. A gate reading an
artifact not listed here does not thereby escape the predicate; it applies
it. The classes that follow are therefore **non-exhaustive examples**,
load-bearing as illustration and never as the boundary:

- a **consent record** — observation, write, egress, or execution (RFC3-7;
  RFC5-12);
- an **approval, adjudication, or overrule Decision** (RFC3-15,
  `decisions/`), including the execution-profile approval (RFC5-18(c));
- an **adoption/acceptance stamp** (RFC3-16);
- an **owner-approved policy declaration whose effect is to unblock or widen
  what Syzygy may honor** (RFC3-15, `policies/`) — the marker-adoption
  policy (RFC4-26), the scheduler retention bound (RFC4-16), the
  currency-bound declaration (RFC2-9), the trusted-external-oracle
  declaration (RFC4-13), and the **substrate-to-normalized work-state
  derivation mapping** (RFC8-12) — a mapping row projecting a custom
  substrate status into `ready` or `active` makes the board and the endpoints
  report dispatch-eligible and live work, so a mapping an untrusted writer
  could mint would widen exactly what the surface says remains, is live, and
  is blocked.
- an artifact that **fixes the meaning of a rendered encoding** rather than
  reporting a fact under it — the channel registry from which all legend text
  is generated (RFC9-26) and the layout version registry (RFC9-18). [Inferred]
  This limb is not about widening a claim, which is why enumeration alone
  would have missed it: a forged registry entry leaves every claim, tier, and
  freshness check passing and changes what a *correct* render means, so no
  downstream status check can catch it (VIS-7's trust floor).

**The predicate.** Such an artifact is honored **only when its owner-act
provenance is independently verifiable to Syzygy by a mechanism the governed
tree cannot forge**. Being present, well-formed, and correctly attributed
*in the tree* is not sufficient. The premise, stated honestly: the plane is
in-tree by design (architecture.md, FD-034), and changes materialize through
fleet workers executing scheduled work (architecture.md's worker-
materialization model), so workers routinely commit into it; SEC-3 declares
that actor class **untrusted regardless of who owns the project** for
executed code, and this package **[Inferred]** extends the same
classification to what those workers *commit* — an extension doctrine does
not state in so many words but which follows from the two rules read
together, and which every consuming gate below rests on. A stored
attribution field is therefore a claim by whoever wrote the file, never
evidence of an owner act. This is the same reasoning §6 already used to
reject designating the governance root by field value (a field can dangle or
lie; provenance cannot), extended to the artifacts that authorize the
dangerous acts.

**The mechanism class — chosen, not open.** The owner already chose the
mechanism class at acceptance (decision **A1**, reaffirmed at the rev8
rework): **correlation of the artifact to an owner-attended, Syzygy-mediated
ceremony recorded in an independently kept audit trail** (the RFC5-25 trail —
which must live outside `.syzygy/**` and outside the untrusted actor class's
write reach, or the correlation proves nothing). The floor property that
makes the class acceptable — forgery must require something the governed
tree does not contain — is satisfied by the trail's independence, not by
anything the owner holds. **Owner-held key or attestation custody is not an
open implementation alternative**: A1 explicitly declined to put custody
burden on the owner, and replacing the ceremony+audit model with an
owner-held key or attestation scheme requires a **later owner decision**,
not an implementation choice. Within the chosen class, implementation
remains free on ceremony UI, transport, audit-store technology, and record
encoding. What any conforming mechanism must *bind* is fixed now, at
RFC3-16(b).

**RFC3-16(b) — What an owner act binds: protocol-neutral semantics.**
*(History: added at the rev7 rework — directive item B2 of
`_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`, not owner decision B2.
RFC3-16(a) fixes when provenance is
required and defers the mechanism; this sub-clause fixes what any
conforming mechanism must bind, so that two implementations cannot
diverge on the meaning of "the owner approved this" while both citing the
predicate. It chooses no keys, signatures, or transports.)*

A verifiable owner act binds, at minimum, all of:

1. the **project identity** the act is made within;
2. the **stable identity of the artifact** acted on;
3. the **exact content or revision digest** of the artifact as acted on —
   **approving a path never approves future content at that path**; an
   artifact edited after the act is, for the predicate, an artifact with no
   act;
4. the **act type** (adopt, accept, approve, consent, dismiss, revoke, …)
   from the acting surface's own vocabulary;
5. the **owner attribution** — which owner, where multi-owner projects
   exist;
6. the **act instant**;
7. the **scope** of the act, where the act type carries one (a consent's
   content classes, an oracle's (project, gate class) pair);
8. the act's **supersession/revocation relationship** — what earlier act, if
   any, it replaces. **Revocation is itself an explicit act** with the same
   binding set; no act lapses silently except by an expiry the act itself
   declared;
9. the **identity of the audit record** (RFC5-25 or successor) that the
   correlation mechanism resolves to — always, under the A1 mechanism class
   bound at RFC3-16(a) —
   a trail that lives, normatively, outside `.syzygy/**` and outside the
   untrusted actor class's write reach (RFC5-25's location constraint),
   without which this item's correlation would be forgeable from inside
   the governed tree.

**Bootstrap correlation.** Artifacts adopted before any mechanism exists —
this repository's adopted doctrine and, on acceptance, these RFCs — have
their owner acts recorded as chat-phrase ceremonies plus git commits/tags.
When the mechanism first exists, the owner performs a **one-time recorded
correlation act** binding each already-adopted artifact's exact digest to
its historical act; until then those artifacts render with their gap stated
honestly (the A9 posture), not as verified. **A git tag or commit alone is
never silently sufficient**: the governed tree cannot prove who pushed it;
it may serve as *evidence within* a correlation, never as the mechanism.
[Inferred — the binding set; Observed — the path-vs-content and
untrusted-tree premises from RFC3-16(a).]

**Effect when the predicate fails.** An authorization present in the tree
without verifiable owner-act provenance is **never silently honored and
never silently deleted**. Its **dependent effect is blocked** — the egress is
refused, the run does not launch, the adapter write does not proceed, the
adoption does not bind, the policy does not widen anything — the
**authorization itself renders Unknown**, and the condition **mints a
contradiction routed to owner adjudication**: exactly the posture RFC3-3
takes for an inoperative write-expanding field and RFC3-9 takes for a
governance artifact Syzygy did not author. Blocking is not deletion: the
artifact and its unverifiable state both remain rendered.

**One predicate, one home.** Every consuming gate **cites this clause rather
than restating the obligation**: RFC 0005's egress choke point (RFC5-15) and
execution gate (RFC5-18(c)) cross-check it before acting; RFC5-14's egress
classification policy and RFC5-16's secret-detection policy (also read at
RFC4-12 and RFC3-30) are honored only under it, as are RFC4-13's
trusted-external-oracle route, RFC4-13(b)'s governed checker definitions
(a checker that can unblock positive status fixes the meaning of a
certification), RFC4-16's retention bound and maximum
inter-pass interval, RFC4-26's marker-adoption policy, RFC4-7's adapter
registry entry, RFC2-13's declared challenge-resolution policy, RFC4-23(2)
and RFC8-16's declared staleness bound, RFC9-26's channel registry and
RFC9-18's layout version registry, the walkthrough **release policy**
(RFC9-45), the map walkthrough **judgment** (RFC9-45's leg 2 — the
adjudication Decision that clears or blocks a release gate), and RFC 0007's
owner judgments — RFC7-21's adoption act,
RFC7-25's fresh-reader review verdict, and RFC7-31's comprehension-test
**judgment** (on both surfaces the walkthrough *execution record* is
`kernel-recorded` and authorizes nothing, so it sits outside this
predicate). [Inferred] Stating
the obligation per artifact
class instead would leave whichever class was patched last unguarded — the
failure mode this single-predicate form exists to prevent, and the same
reason the clause's **subject** is the predicate above rather than the
examples beneath it. This list tracks the gates; it does not bound them.

**RFC3-17.** This RFC reserves an additional category,
`.syzygy/governance/declarations/`, as the governance-plane home for the
declaration artifacts RFC 0001 names: capability declarations, declared
topology, declared regions, declared implementation mappings (SDR-4), and
promoted annotations/designations. Doctrine leaves their placement within
`governance/` to RFCs (architecture.md); their internal schemas belong to
RFC 0004 and the surface RFCs. Install gate: owner sign-off (they are
shape-defining, VIS-4); Syzygy-drafted entries stamp unadopted per RFC3-16.

**RFC3-17(a). Where challenges and their admission records live.**
Challenge submissions (RFC1-5, RFC2-12) and their admission-or-rejection
records (RFC2-13) live in **`.syzygy/governance/records/`** — RFC3-15's
fifth constitutional category — under write authority **`kernel-recorded`**
(RFC3-2's fourth class). There is no `governance/challenges/` category; a
conforming implementation may not create one, and may not choose any home
for these artifacts other than `records/`.

*(History: added post-draft; the plane previously named no home for them.
Body rewritten at acceptance under owner decision B19: the original draft
reserved a further category under `Syzygy-maintained` authority, and
reasoned from a then-true premise that RFC3-15 had four categories and
RFC3-2 admitted no fourth class. B19 superseded that premise — RFC3-15 now
has five categories and RFC3-2 four classes — so the original body is
retired and this body states the adopted model. The sub-clause identifier
is retained; nothing else of the original remains normative.)*

**Why `records/` and nothing else.** RFC2-13 makes the admission-or-rejection
record a *kernel fact written to the governed plane*, and RFC2-1 item 9 makes
open challenges with their admission records a **snapshot input** — so the
artifact is identity-bearing, durable, and deletion-unsafe, and it **enters
snapshot identity** exactly as RFC2-1 item 9 requires. `cache/` is barred
outright: RFC3-20 forbids anything there from serving as a snapshot input or
being the only home of a fact. `local/` is barred by RFC3-21 (never
truth-bearing, never a snapshot input). `intent/`, `work/`, and `map/` are
surface namespaces (RFC3-18) and none of the three surfaces owns challenge
state. And the artifact is not doctrine, not an accepted contract, not a
policy, and — decisively — **not a recorded owner decision**: it is an
inference-or-human *objection* whose admission is a mechanical kernel check.
That is RFC3-15's `records/` definition verbatim — a kernel-authored durable
fact minted on a non-owner actor's submission. The one challenge-adjacent
thing `governance/` holds elsewhere is the *resolution policy* in `policies/`
(RFC3-15), which governs how a challenge is resolved and is not the challenge.

**Consequences that bind.** The records are **minted by the kernel, never
owner-authored**; the challenger's inference provenance — or a human
challenger's attribution — is a **field of the record**, never its write
authority (recording a human's challenge is not the human adopting anything).
The records are **immutable once written** (RFC2-6's treatment of kernel
facts); a challenge is never edited to change its verdict. A
`kernel-recorded` value is **never authorization-bearing** (RFC3-2), so
nothing in `records/` is adopted or adoptable — RFC3-15's install-gate column
says the same. **Resolution acts that are owner acts** — a human upholding,
dismissing, or expiring a challenge — are recorded in `decisions/` per
RFC3-15 and *referenced* from the challenge record, never embedded in it.
Because `records/` sits inside `governance/**`, which fleet workers can
write (the untrusted-writer premise stated at RFC3-16(a), extending SEC-3's
actor class), an admission record's authority is the kernel's
recomputation of the RFC2-13 check over the snapshot, never the file's own
say-so. [Observed — home, authority class, and gate column from RFC3-15/RFC3-2
as amended by B19; durability and snapshot-input facts from RFC2-1 and
RFC2-13.]

### 3.5 Surface directories, and `.syzygy/work/**` authority

**RFC3-18.** `intent/`, `work/`, and `map/` are schema-versioned governed
namespaces whose internal contracts belong to RFCs 0007–0009. This RFC
binds only the namespace class: they are part of the plane that stays with
the repository at offboarding (architecture.md), they obey §3.7 versioning
and migration, and nothing in them may become independently authoritative
over kernel semantics (architecture.md, one kernel).

**RFC3-19.** **`.syzygy/work/**` owns approved execution intent before
materialization** (SDR-7; RFC1-28): approved execution-intent Proposals
reside there until their immutable materialization record exists, after
which the scheduler is authoritative for lifecycle and the proposal is
terminal. `work/**` also holds materialization records and Execution
Records (Evidence artifacts, SDR-8). The materialization record's schema
**must pin the exact intent revision cited by the warrant** — RFC 0002's
reconciliation chain binds its verdict to that pinned revision (RFC2-18).
*(Handoff satisfied by the RFC1-29 amendment of 2026-07-30: RFC1-29 now
requires the materialization record to pin "the exact intent revision …
cited by the proposal's warrant", and RFC1-5's materialization-record row
carries it. The obligation is therefore stated once, in RFC 0001; this
clause restates its schema consequence and no longer requests an amendment.
Recorded rather than deleted so the trail survives — review 3, AS-R8.)*

### 3.6 Cache and local state

**RFC3-20.** **`.syzygy/cache/` is rebuildable projection, nothing else**
(VIS-6). The deletion-safety invariant: deleting `cache/` in its entirety,
at any instant, changes no truth, status, work, consent, or authoritative
artifact — everything in it is re-derivable from the artifacts that own
its facts. Nothing in `cache/` may be cited as evidence, serve as a
snapshot input, hold Genome membership, or be the only home of any fact.
Observation records are **not** cache: they are non-rebuildable historical
evidence (VIS-6, exception (b)) and must not live where deletion is declared
safe. Syzygy deletes `cache/` at offboarding (architecture.md).

**RFC3-21.** **`.syzygy/local/` is personal presentation state** — VIS-6,
exception (a): layouts, filters, bookmarks, unpromoted notes. It is never
truth-bearing, never a snapshot input, and may never affect truth, work,
status, or certificates. The **only** path by which its content gains
authority is promotion: an explicit act committing the content out to the
governed plane as an attributed, reasoned annotation or dismissal (VIS-6).
At offboarding Syzygy exports `local/` to the owner; deleting it loses
personal state only, never truth.

### 3.7 Schema versioning and migration of `.syzygy/**`

**RFC3-22.** **Version stamps.** The plane carries one plane-level schema
version (`schema_version` in `project.yaml`); artifact classes with their
own governing RFCs may carry per-class versions. Stamps are Syzygy-
maintained (RFC3-2) and are **snapshot inputs**: an evaluation records the
schema versions it read (RFC2-1), so a migration is visible as a snapshot
difference, never an invisible re-interpretation.

**RFC3-23.** **Migrations are identity-preserving.** A schema migration
may reorganize representation; it may never change any minted identifier,
adoption status, attribution, timestamp, consent scope, dismissal reason
or expiry, or evidence integrity digest, and every pre-migration citation
(claim, dismissal, consent reference, map anchor) must resolve identically
after it (trust-floor link rule). A change that would alter any of these
is a **semantic change**, not a migration, and goes through the changed
artifact's own adoption gate.

**RFC3-24.** **Migration is an explicit, reviewed, revertable act.**
Migrations run only as a deliberate act, never lazily on read — a read
must never mutate the plane (idempotence, RFC2-22). Each executed
migration is attributed to Syzygy, atomic, and individually revertable
(SEC-4), and records what it transformed. Migration definitions fall under
the craft cluster's mandatory independent-review class 5 — "`.syzygy/**`
schema migrations, any identity-affecting store change" (CC-REV-1) — and
under this RFC once accepted: migrating to a schema no accepted contract
defines is a violation.

**RFC3-25.** **Forward and backward behavior.** A Syzygy build reading a
plane whose stamped version is **newer** than it understands must not
write to that plane and must not downgrade it; content it cannot interpret
renders Unknown — never partially parsed and presented as whole (VIS-1;
RFC2-23 partial-snapshot rule). A plane **older** than current is read via
the declared migration path and upgraded only by the explicit act of
RFC3-24. There is no in-place downgrade obligation: reverting a migration
is the version-control revert of its atomic write.

**RFC3-26.** **`openspec/**` is outside Syzygy's migration authority.**
Schema versioning and migration in this section govern `.syzygy/**` only.
`openspec/**` is governed by the constitutional OpenSpec artifact
contract: Syzygy writes it only in OpenSpec-compatible form and may not
reorganize it for its own convenience (architecture.md, schema ownership).

### 3.8 `openspec/**` interoperability

**RFC3-27.** What Syzygy **reads** from `openspec/**`: requirement and
scenario content under the artifact contract's own identity scheme, held
by the kernel as (artifact identity, anchor) references (RFC1-15);
changeset/adoption state as facts; spec structure for rendering. The
kernel never claims ownership of spec content or identity — the artifact
contract is the external authority, and the OpenSpec CLI is a
substitutable adapter beneath a non-substitutable artifact contract.

**RFC3-28.** **Spec anchors (SDR-32).** Adapter contracts must support
resolvable spec anchors — stable references into `openspec/**` that
claims, mappings, and the reconciliation chain can cite. A missing or
unresolvable anchor renders the dependent claim Unknown; it **never**
rejects the project, blocks observation, or is silently re-guessed
(RFC1-15: degrade, never guess). Whether OpenSpec identities survive edit
and rename remains [Unknown] and is RFC 0004's adapter-contract
obligation.

### 3.9 Nested and recursive projects

The seed hypothesis promises "recursively nested subprojects"
[Observed: `_bootstrap/brief/PRODUCT_VISION_SEED.md`], and OQ-010 flags
the conflict with the one-root invariant. Resolution:

**RFC3-29.** **One plane per repository; one root per Project — upheld.**
A repository carries at most one `.syzygy/` plane, at its root (RFC3-4).
There are no directory-scoped sub-roots: a `.syzygy/` directory anywhere
but a repository root designates nothing and is surfaced as a finding.

**RFC3-30.** **Dual roles are lawful and per-pair.** One repository may
simultaneously be the governance root of its own Project and a declared
observed-source repository of one or more other Projects. Role and
consent are properties of the *(Project, repository)* pair (RFC3-7), never
global: Project A observing repository R requires A's own consent record
for R, regardless of R's role elsewhere. An observing Project reads the
observed repository's entire tree — **including its `.syzygy/**` and
`openspec/**` plane — read-only**: A's direct-write universe is A's own
governance root's two namespaces and nothing else (VIS-5); A never
writes, migrates, or "repairs" B's plane.

**Governing policy is a property of the *observing* project's governance
root.** Project A screens, bounds, and classifies everything it ingests
under **A's** policies (`.syzygy/governance/policies/` in A's plane):
A's secret-detection policy (SEC-5; RFC5-16, RFC4-12), A's currency bounds
(RFC2-9), A's retention bound (RFC4-16), A's egress content-class rules
(RFC5-14). Every one of those is an owner-approved declaration widening what
Syzygy may honor, so **each is honored only under RFC3-16(a)** — A's own
plane being the source is necessary and not sufficient, since A's plane is
writable by the untrusted actor class too (SEC-3's class, extended to
committed artifacts by the premise RFC3-16(a) states): a worker-minted policy in
A's own tree weakens A's screening exactly as a permissive policy adopted
from B's would. Content read from an observed-source plane — **including that
plane's `.syzygy/governance/**`** — is **data about B, never governing
policy for A**, and never a snapshot input to A's evaluations in the
policy-version role (RFC2-1 item 7 records *A's* policy versions). This is
the dual of RFC3-32: a parent holds no authoritative state about a child,
and a child or observed source supplies no governing policy to its
observer. The RFC2-9 currency-bound ambiguity resolves identically: **A's
declared bound governs A's claims about B**, whatever bound B declares for
its own claims. [Inferred] The nearest-plane reading would let a compromised B
ship a permissive policy that weakens the screening of B's own content as
it enters A — the source choosing its own scrutiny. *(History: post-draft
amendment under review 3's AS-R7.)*

**RFC3-31.** **Nesting is composition by declaration.** A "subproject" is
a full governed Project with its own governance root, owner consent, and
plane. The parent/child relationship is an ordinary outbound declared
relation (`relations[]`, type `subproject-of` from the child and/or
`contains-project` from the parent), rendered per RFC3-14: one-sided
declarations render unconfirmed/asymmetric; both-sided compatible
declarations render as a confirmed hierarchy. The portfolio and any
recursive rendering are **derived** views over these declarations
(SDR-28) — recursion lives in the rendering, never in the plane. A
declared hierarchy containing a cycle renders the cycle explicitly and
routes to the owner; Syzygy never silently breaks it.

**RFC3-32.** **What a parent may never do:** hold authoritative state
about a child's internals (SDR-30 applies to parent projects exactly as to
the workspace manifest); adopt, dismiss, or consent on the child's behalf;
aggregate a child's Unknowns into a parent-level green (VIS-1). A parent's
views of a child are projections of the child's own declared and observed
state, at the parent's evaluation, with the child's epistemic labels
carried through unchanged.

**"Labels carried through unchanged" is not the whole obligation — RFC6-17
is.** Any parent-level aggregate over a child's facts discloses **RFC6-17's
full composition**: the RFC6-22 equivalence tuple, per-label, per-tier,
per-Unknown-reason and per-freshness-state counts and sibling surface states,
expandable to members. The obligation is **cited here, never restated**,
precisely so the roll-up path cannot drift from the aggregation contract the
way a paraphrase would. Labels-and-Unknowns alone is the narrow reading, and
it is satisfiable while laundering: a parent rendering a child's district as
"Observed ×30" carries every label through unchanged and aggregates no
Unknown into green, and can still be hiding that all thirty are
`reduced-fidelity` and twelve are stale — which is exactly the failure the
tuple exists to catch. RFC7-37 binds the same obligation on the narrative
side.

---

## 4. Violation cases

1. *(RFC3-3)* A `project.yaml` field `write_roots: [docs/]` is honored and
   Syzygy commits a file under `docs/` — the write universe expanded by
   configuration.
2. *(RFC3-4)* Two repositories each contain a `.syzygy/project.yaml`
   claiming the same project identity, and Syzygy picks the fresher one
   instead of routing a contradiction.
3. *(RFC3-6/7)* A repository entry with no resolvable consent record is
   rendered as an empty-but-green region instead of Unknown; or one
   repository's consent for Project A is treated as consent for Project B.
4. *(RFC3-8)* Withdrawing a provider consent deletes the consent record
   and the inference overlays vanish without a rendered reason.
5. *(RFC3-10/12)* A cross-project dependency edge is drawn because both
   projects sit in the same workspace group; deleting the workspace
   manifest changes a project's rendered membership or status.
6. *(RFC3-14)* A declares `depends-on B`, B declares nothing, and the
   portfolio renders a confirmed bidirectional edge; or a declared
   `depends-on` edge is rendered, legended, or queried as if it were
   RFC1-25's observed `depends_on`.
7. *(RFC3-15/16)* A drafted, unadopted doctrine file in
   `governance/doctrine/` is cited as binding; or an accepted RFC is
   installed into `contracts/` with no owner acceptance recorded.
8. *(RFC3-19)* An approved plan item is edited in `.syzygy/work/**` after
   its materialization record exists (also RFC1-29); or a materialization
   record omits the warranted intent revision and the reconciliation chain
   silently evaluates against current intent.
9. *(RFC3-20/21; RFC3-17(a))* An observation record stored under `cache/` is
   lost to a cache purge; or a challenge admission record — a snapshot input
   under RFC2-1 item 9 — is written to `cache/` and a purge silently
   un-suspends every claim it suspended; or a `local/` bookmark list is read
   as a snapshot input.
10. *(RFC3-23/24)* A migration renames capability identifiers "for
    consistency" and the map relocates; or opening the UI silently
    upgrades the plane's schema on read.
11. *(RFC3-25)* A build reading a newer plane writes its older schema back
    — a silent downgrade destroying fields it never understood.
12. *(RFC3-29/30)* A nested `.syzygy/` directory inside `src/` is treated
    as a governance root; or a parent project "fixes" a typo in a child's
    `project.yaml`; or Project A screens content ingested from observed
    source B under **B's** secret-detection policy.
13. *(RFC3-16(a))* A fleet worker commits an egress-consent record naming a
    new provider, plus the matching `consents[]` reference, and the next
    evaluation honors it as in force because the record's attribution field
    says "owner"; or an unverifiable authorization is quietly dropped from
    the plane instead of rendering Unknown and minting a contradiction.

---

## 5. Integration

**Relies on RFC 0001:** project/repository/role/consent entity semantics
(RFC1-1…4); opaque identifiers and label/identity separation (RFC1-10);
the portfolio extension profile as the home of cross-project relation
entities (RFC1-7); Proposal lifecycle and the plan-item resolution
(RFC1-27/28/29). **Relies on RFC 0002:** the Unknown-reason vocabulary
(`unconsented-source-or-provider`, RFC2-24 #6) and failure-state renderings
(RFC2-23) that give consent withdrawal its exact effect; snapshot inputs
(RFC2-1) that make versions and adoption stamps identity-bearing; the
idempotence rule (RFC2-22) behind no-migration-on-read.

**Defect handoff — resolved (retained for the trail):** this RFC reported
that RFC1-29 defined the materialization record without requiring the
pinned warranted intent revision that RFC2-18's reconciliation chain joins
on. **Satisfied by the RFC1-29 amendment of 2026-07-30**, which pins the
exact warranted intent revision in the record itself (and RFC1-5's
materialization-record row with it). No RFC 0001 change is outstanding;
RFC3-19 now restates the consequence rather than requesting the fix
(review 3, AS-R8).

**Provides to RFC 0004:** the consent and anchor semantics its adapter
contracts must honor (RFC3-7/8, RFC3-28); the schema-version stamp as a
snapshot input; the constraint that observation records may not live in
`cache/` (RFC3-20) — their physical home and the snapshot representation
(one tuple vs composite) are RFC 0004 material. **Provides to RFC 0005:**
the consent-record content model behind machine-consumable consent checks
(SEC-2 rendering, RFC2-24 #6); and **RFC3-16(a)**, the owner-act provenance
predicate that RFC 0005's egress choke point (RFC5-15), execution gate
(RFC5-18(c)), egress classification policy (RFC5-14) and secret-detection
policy (RFC5-16) cross-check before acting. **Provides to RFC 0004
(further):** RFC3-16(a) as the authority under which RFC4-13's
trusted-external-oracle route, RFC4-16's retention bound and maximum
inter-pass interval, RFC4-26's marker-adoption policy, RFC4-7's adapter
registry entry, and RFC4-23(2)'s declared staleness bound are honored.
**Provides to RFC 0002:** the same authority under RFC2-9's currency-bound
declaration and RFC2-13's declared challenge-resolution policy, both of which
cite it in their own text (RFC2-9 marks the citation informative until this
RFC is accepted). **Provides to RFCs 0006–0009:** the
namespace authority classes for `intent/`, `work/`, `map/`; the
`declarations/` category; the workspace-manifest boundary every portfolio
rendering must respect; and **the owner-act provenance predicate (RFC3-16(a))**,
which the surface RFCs consume at six gates — RFC7-21's adoption act, RFC7-25's
review verdicts, RFC7-31's comprehension-test judgments, RFC8-16's staleness
bound, and RFC9-26's channel and RFC9-18's layout-version registries. Those last
two are the clearest instances of the predicate's third limb: a forged registry
entry leaves every claim, tier and freshness check passing and changes what a
*correct* render means, so no downstream status check can catch it. **This
enumeration tracks the gates; per RFC3-16(a) it does not bound them.**

---

## 6. Alternatives considered

### 6.1 Nested projects (the OQ-010 conflict) — options

- **(a) Directory-scoped sub-roots** (a `.syzygy/` plane per subdirectory
  inside one repository). Rejected: it breaks "exactly one designated
  governance root … the repository containing the Project's single plane"
  (architecture.md — a doctrine amendment, not an RFC choice); it splits
  the consent record's subject (SEC-4 consent is per-repository); and it
  makes the write universe ambiguous (which plane may write
  `openspec/**`?).
- **(b) Parent-owned subproject registry** (parent plane authoritative for
  children). Rejected: SDR-30 verbatim — no manifest is authoritative for
  another project's internal truth; it would also make child state a fact
  living outside the child's plane, against VIS-6.
- **(c) Composition by declaration — chosen (RFC3-31).** Preserves the
  one-root invariant untouched, reuses the already-required asymmetric
  relation semantics, keeps every project offboardable as a unit, and
  realizes the seed's promise as *rendering depth*, which is where the
  seed's own comprehensibility tension (KNOWN_TENSIONS T15) wanted it
  bounded anyway.
- **(d) Reject nesting outright.** Not taken: it forecloses a named seed
  promise without doctrinal need; under VIS-1 the derived hierarchy is
  cheap and honest. The genuinely foreclosed case — many governed
  subprojects inside one repository — is surfaced as open question 1
  rather than silently buried.

### 6.2 Other roads not taken

- **Workspace manifest as a governed artifact** (committed, adopted,
  versioned). Rejected: it would need a home, and no third namespace
  exists (VIS-5); a Syzygy-owned authoritative store is FR-2's option 2,
  a VIS-6 violation absent a doctrine amendment. Exception (a) fits
  SDR-29's concerns exactly; the cost is examined in open question 2.
- **Embedding consent records in `project.yaml`.** Rejected: consent is a
  governance act needing independent lifecycle (grant, narrow, revoke,
  supersede) and attribution; embedding would give one file two
  authorities per field (violating RFC3-2) and make revocation an edit
  war with membership drafting.
- **Designating the governance root by field value** rather than by the
  declaration's location. Rejected: a field can dangle or lie; the file's
  location cannot — and it makes the zero-root case structurally
  impossible rather than merely detectable.
- **Lazy migration on read.** Rejected: violates idempotence (RFC2-22)
  and SEC-4 attribution — a render pass must never be a write actor.

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
  multiple classes. Aligned to **one record per *(Project, provider)*
  naming the permitted set** (AS-R10). This removes an internal
  contradiction only; the substantive granularity ruling stays open at §8
  q3.

---

## 7. Deliberately deferred

Concrete field grammars, YAML dialect rules, and validation tooling →
implementation under accepted contracts. Snapshot physical representation
and the observation-record storage home → RFC 0004 (constrained by
RFC3-20/22). Machine-client consent verification and the consent surface
rendering mechanics → RFC 0005. Internal schemas of `intent/`, `work/`,
`map/` → RFCs 0007–0009 (namespace class fixed in RFC3-18/19).
Retention/compaction policy for `work/**` execution records (SDR-10
obligations) → RFC 0004 + quality policy. Multi-workspace and multi-user
manifests → deferred with multi-user (v1.md). Cross-project relation
*type vocabulary* beyond
`subproject-of`/`contains-project`/`depends-on`
→ portfolio profile RFC material (RFC1-7).

---

## 8. Open questions for acceptance

1. **Monorepo subprojects (RFC3-29).** Composition by declaration
   requires each governed subproject to be its own repository. An owner
   who wants several governed projects inside one physical repository is
   foreclosed until doctrine amends the root definition. Accept the
   foreclosure (recorded here per the north-star recording rule), or
   direct that a directory-scoped-root amendment be drafted for owner
   adoption?
2. **Workspace manifest classification (RFC3-10).** VIS-6, exception (a)
   means workspace state — including saved cross-project views and the
   portfolio narrative preferences — is exempt from rebuildability and is
   lost if not exported. Acceptable for owner-first V0, or should saved
   cross-project *views* (as distinct from preferences) be re-derivable
   by construction?
3. **Egress consent granularity (RFC3-7).** SEC-2 words egress consent
   per-project; RFC1-3 folds it into per-repository consent records. This
   RFC models egress consent as its own per-(project, provider) record
   kind. Confirm this split, or direct that egress scope ride on each
   repository's consent record (finer-grained, heavier to administer)?
   *(Review 3's AS-R10 aligned RFC5-12's wording to one record per
   *(Project, provider)* naming a set of content classes, removing an
   internal contradiction with RFC5-14. That is a consistency fix only —
   this question is untouched by it and remains the owner's to rule.)*

   > **ANSWERED at acceptance — B8.** **One record per (project, provider)**, naming the permitted content classes inside it. Matches SEC-2's wording; the finer per-content-class granularity is not taken.
4. **The `declarations/` category (RFC3-17).** Confirm reserving a further
   governance category for declaration artifacts, or direct that they be
   distributed among the constitutional minimums (four when this question was
   posed; five since B19) — topology and mappings as `contracts/`? regions as
   `decisions/`? — distribution avoids a new category but blurs each
   category's one-line meaning. *(Posed alongside q6, which asked the
   structurally similar question for challenges.)*

   > **OPEN — partially resolved by B19.** B19 settled the *challenge* half
   > (q6): `records/` and `kernel-recorded` exist by explicit owner widening.
   > B19 did **not** rule on `declarations/` itself — the earlier annotation
   > claiming it did overreached and is corrected here (rev7 rework,
   > directive item A1 — not owner decision A1).
   > Drafted default in force until the owner rules: RFC3-17's reservation of
   > `declarations/` as an additional reserved category **outside** RFC3-15's
   > constitutional five stands as written, reversible by amendment. B19's
   > precedent — widen explicitly rather than stretch a category's
   > "exclusively" — is the pattern either answer should follow.
5. **The owner-act provenance predicate (RFC3-16(a)) — added post-draft
   under review 3's Blocker, scope widened to the predicate thereafter.**
   Honoring an artifact that authorizes a dangerous act, unblocks a claim
   class, or fixes the meaning of a rendered encoding now requires provenance
   the governed tree cannot forge, not merely a well-formed file carrying an
   attribution field. Two things need the owner's word. **(a) The ergonomic
   trade — and its true breadth.** The clause's subject is the predicate, not
   its example list, so the trade is wider than the original four classes:
   beyond consents, approval Decisions and adoption stamps (RFC7-21), it
   reaches the secret-detection and egress-classification policies (RFC5-16,
   RFC5-14), the adapter registry entry (RFC4-7), the declared staleness
   bound and maximum inter-pass interval (RFC4-23(2), RFC4-16(2)), the
   deterministic challenge-resolution policy (RFC2-13), the channel and
   layout-version registries (RFC9-26, RFC9-18), and the owner judgments in
   `decisions/` (RFC7-25, RFC7-31). Each becomes an authenticated owner
   *act*; hand-editing or scripting any of them into the plane stops being
   sufficient, including for the owner's own convenience. That cost is real
   and recurring — confirm it is the trade you want, or direct a narrower
   scope (e.g. the predicate binding only egress and execution
   authorizations, leaving adoption stamps and registries on stored
   attribution). **Narrowing by re-enumerating is the option to weigh
   carefully:** a list is what left the last-patched class unguarded, so a
   narrowing is best expressed as a *narrower predicate*, not a shorter list.
   **(b) The mechanism class.** *(As posed, the clause named two candidate
   classes and deferred the choice; per the A1 answer below, RFC3-16(a) now
   binds the ceremony+audit class and owner-held attestation is no longer an
   implementation option.)* The clause deliberately named only a class —
   correlation to a Syzygy-mediated owner ceremony recorded in the RFC5-25
   audit trail, or an owner-held attestation neither the tree nor Syzygy can
   mint — and deferred the choice to the first implementation slice. Confirm
   the class boundary, or fix a mechanism at acceptance.

   > **ANSWERED at acceptance — A1 / A9.** Mechanism class: **owner-attended ceremony correlated to an independently kept audit trail** (not owner-held attestation). **Binding constraint:** that audit trail must live outside `.syzygy/**` and outside the untrusted actor class's write reach, or the correlation proves nothing. The owner accepted shipping before the mechanism exists, with the gap rendered honestly in the interim.
6. **A governance home for challenges and admission records (RFC3-17(a)).**
   *(Question body preserved as posed; the premises it states — four exclusive
   categories, the original RFC3-17(a) draft home — were true when written and
   are superseded by B19.)* RFC2-13 makes a challenge's admission-or-rejection
   record a *kernel fact* written to the governed plane, and RFC2-1 item 9
   makes open challenges with their admission records a snapshot input —
   durable, identity-bearing, deletion-unsafe. RFC3-15 (as then written)
   declared its four categories exclusive, and a kernel fact that is **not an
   owner decision** fitted none of them. So the plane needed one of two
   things, and only the owner could choose: **(a)** a further reserved
   category — `governance/challenges/`, as RFC3-17(a) then drafted — or
   **(b)** an explicit widening of one of the four, most plausibly
   `decisions/`, on the reading that admission is *an act recorded as a
   fact* — a reading available but costly, since a category holding *recorded
   owner decisions* would also hold records no owner made. **What was never
   open:** `cache/` and `local/` are excluded either way (RFC3-20/21). Which?

   > **ANSWERED at acceptance — B19.** Neither option as posed: the owner
   > widened the constitution itself. Challenge and admission records live in
   > **`records/`** (RFC3-15's fifth category, `kernel-recorded` authority);
   > `governance/challenges/` was never created and RFC3-17(a)'s body was
   > rewritten accordingly (rev7 rework, directive item A1 — not owner
   > decision A1). `cache/` and `local/` remain
   > barred to identity-bearing snapshot inputs.

---

*End of RFC 0003. Clauses RFC3-1 … RFC3-32, with sub-clauses RFC3-15(a),
RFC3-16(a), RFC3-16(b) and RFC3-17(a).*
