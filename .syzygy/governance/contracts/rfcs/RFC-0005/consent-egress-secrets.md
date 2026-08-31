---
id: RFC-0005
title: Consent, Egress and Secret Screening — what may leave, what may enter
status_source: owner-act-record
module: consent-egress-secrets
clauses: RFC5-12..RFC5-17 (no gaps, no retirements, no merges)
governs: [consent-classes, consent-records, egress, content-classes, model-providers, secret-screening, ingest-boundaries, exclusions, redaction-classes]
applies_to: [kernel, all-surfaces]
depends_on: [RFC-0001, RFC-0002, RFC-0003]
tags: [sec-2, sec-5, vis-1, egress-choke-point, fail-closed, hash-not-body, rfc3-16a-gate]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — either owner-adopted (bootstrap,
uncorrelated) or Syzygy-verified, with the exact provenance state always
visible (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 2 of 3 of the RFC 0005 contract package. Index, clause map,
lookup rule, package-spanning integration and the package question list:
`README.md`. Rationale, amendment history, alternatives, and answered §8
questions: `../../history/RFC-0005-history.md`.

**Serves:** SEC-2 (egress consent per provider and content class), SEC-5 (secret
handling), VIS-1 (no over-degrading of usable partial evidence),
VIS-7/trust floor (no secret in any surface). Implements owner decision **B8**
(egress-consent granularity). Grounded in FD-009 (remote backing dependencies).

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what may leave the machine and what may enter its stores**.
Read it to answer: *may this content cross a boundary, in either direction?* It
presupposes module 1 — an egress or an ingest is performed for a principal
already admitted under RFC5-3/RFC5-5, and every egress check emits into the
audit trail of RFC5-25.

Four rules carry most of the weight:

- **Consent is four separately revocable classes** — observation, write, egress,
  execution — one class per record instance, so revoking one never silently
  revokes or preserves another (RFC5-12).
- **One egress choke point** (RFC5-15) with a three-part check, all of which must
  pass: consent in force; content class determinable and consented under a
  policy whose own provenance verifies; and the consent record's owner-act
  provenance verifiable under RFC3-16(a).
- **Undeterminable fails closed, in both directions** — a composite whose class
  cannot be determined is refused egress (RFC5-14); content that cannot be
  classified at ingest is excluded, not indexed (RFC5-16).
- **Exclusions are recorded by hash, never by body** (RFC5-17), and the three
  redaction classes map to Unknown differently — a `redacted-span` artifact does
  not blanket-degrade its surviving content.

The untrusted-tree premise runs through this module: the governed tree is
writable by fleet workers (SEC-3's untrusted actor class, extended to committed
artifacts by RFC3-16(a)), so a consent record, a classification policy, and a
secret-detection policy are each honored **only** under RFC3-16(a). Each clause
below states why, because in each case a permissive artifact minted from inside
the tree would defeat the gate while every other field reads as satisfied.

---

## 3. The contract

Clauses are numbered `RFC5-n` for stable citation. Amend in place; retire rather
than renumber. A pointer *(history §RFC5-n)* means amendment narrative, prior
wording, or originating decision text was extracted at the rev10 compaction;
that material is non-normative and the clause text is the contract. Decision
identifiers named inline (B8, FD-009) remain binding provenance here.

### 3.6 Consent classes and consent records

**RFC5-12.** RFC 0001's **Consent record** entity (RFC1-3) carries a closed set
of **consent classes**; one record instance grants exactly one class, so each is
individually revocable and individually renderable:

- **Observation consent** — per repository: Syzygy may read and index it
  (RFC1-3). Absent: no observation, Unknown — never an empty graph read as
  absence.
- **Write consent** — per repository: Syzygy may write its two namespaces and
  reach declared adapter effects (SEC-4). Absent: read-only.
- **Egress consent** — **one record per *(Project, provider)* pair, naming the
  set of permitted content classes** (§3.7; SEC-2's own wording; RFC3-7). Not one
  record per content class. *(Granularity answered at acceptance by owner
  decision B8; the per-repository alternative was declined — history §RFC5-12.)*
- **Execution consent** — per project: the owner's approval Decision for a
  specific execution-profile version (RFC5-18). Absent: no observed code runs.

Every consent record names its class, subject, scope, granting principal, grant
instant, and revocation state. Representation (`project.yaml`, governance-plane
schema) is RFC 0003 material.

**RFC5-13.** Consent revocation is prospective: it stops future acts (RFC5-11)
and renders dependent claims Unknown (`unconsented-source-or-provider`, RFC2-24
#6) at the next evaluation — **while every render served in the interim already
carries the withdrawal label under RFC5-11**, so that interval never presents
withdrawn-source content as current. Immutable artifacts produced under
then-valid consent (observation records, inference overlays, execution records)
remain, rendered with the withdrawal visible (RFC2-23); revocation never rewrites
history. A revoked provider's overlays are never recomputed and admit no **new**
challenges; **challenges already admitted are unaffected by the revocation and
leave the lifecycle only by an RFC2-13 resolution act** — RFC2-13's rule, cited
not set here. This clause's own rule is the revocation side: no recomputation, no
new admissions, no un-suspension as a side effect of the consent record changing.

### 3.7 Egress consent and model providers

**RFC5-14.** Governed-project content leaves owner-controlled infrastructure only
under a recorded egress-consent record naming the **provider** and the permitted
**content classes** (SEC-2). Model providers are such providers. The
content-class vocabulary is closed at this RFC (amend to extend):

| Class | Contents |
|---|---|
| `governance-text` | Doctrine, spec, decision, policy text |
| `code-structure` | Identifiers, paths, symbols, structural graph — no bodies |
| `code-content` | Source and test bodies |
| `work-history` | Work items, run summaries, telemetry, cost data |
| `evidence-content` | Evidence artifact contents (reports, logs) |
| `derived-composites` | Prompts, summaries, embeddings composed from the above |

A composite inherits the **highest** class of any content it embeds;
`derived-composites` consent alone never launders an unconsented class into an
egress. The vocabulary is closed here, but the **declared policy that classifies
concrete content into it** is a governance artifact honored **only under
RFC3-16(a)** — a policy an untrusted writer could mint would classify
`code-content` as `code-structure` and pass RFC5-15's check on a consent record
that is genuinely in force, defeating the choke point without forging a consent
record at all; RFC5-15 accordingly verifies both provenances, not one. Providers
not named require fresh consent; absent consent the inferred layer **is not
computed** and renders Unknown (RFC2-7). Active consents are rendered on the
project's surface (SEC-2).

**Classification is determinable, provenance-tracked, and fails closed.** Content
class is a **property of what enters the choke point, tracked from where the
content originated**, never an attribute the composing step asserts about its own
output: composition **carries embedded classes forward**, so a composite's class
is computed from what it embeds and remains attributable to them. A composite
whose class **cannot be determined fails closed** — the egress is **refused and
the refusal rendered** — exactly as unclassifiable content is excluded rather
than indexed (RFC5-16). The **classification-policy version is a snapshot input**
(RFC2-1 item 7), so what class was asserted under which policy is auditable at
every evaluation. [Inferred] Without the undeterminable case the
highest-embedded-class rule has no floor: a composer that cannot say whether it
emitted `code-structure` or an inlined `code-content` body would default to
whatever it claimed, defeating SEC-2's per-content-class scoping with every
RFC5-15 field nominally satisfied.

**RFC5-15.** Egress enforcement sits at a **single choke point**: every network
transmission of governed-project content passes one consent check naming
(provider, content classes, project) and emits an audit record (RFC5-25). Three
parts must all pass: the consent record is **in force**; the content's class is
**determinable and within the consented set** under a classification policy
carrying an effective owner act under RFC3-16(a) (RFC5-14 — undeterminable fails
closed, and so does a missing or invalid act, since a forged classification
passes this part while telling the truth about the consent record); and the
consent record carries an **effective owner act under RFC3-16(a)**. State (1)
and state (2) are both effective, and the exact state of each act is disclosed.
A consent record present in the governed tree without a valid act does not
authorize an egress, blocks the transmission, and mints a contradiction, because
the tree the consent lives in is writable by fleet workers, SEC-3's untrusted
actor class, extended to committed artifacts by the premise RFC3-16(a) states.
The classification-policy and consent acts warrant only the scoped
classification and egress; they are never evidence that the transmission
succeeded or any transmitted claim is true. A feature that transmits as a side
effect without traversing the choke point is the SEC-2 violation, whatever its
intent. Remote backing dependencies (a remote database, FD-009) are permitted
under the same rule — a backing store the owner does not control is a provider.

### 3.8 Secret handling at ingest boundaries

**RFC5-16.** The declared secret-detection policy (SEC-5,
`.syzygy/governance/policies/`) is applied at **every ingest boundary** —
*before* content enters any Syzygy store, surface, or endpoint. The enumeration
that follows is **illustrative of every ingest boundary, not exhaustive**:
observation capture; evidence intake; adapter reads — **including a cross-project
read of an observed source's entire tree (RFC3-30)**; **workspace-manifest
import** (RFC3-11); execution-run output capture (RFC5-18); telemetry. A path not
on this list is not thereby exempt; if content crosses into a Syzygy store, it
crossed an ingest boundary. **The governing policy is the observing project's
own** (RFC3-30): Project A screens what it ingests from observed source B under
**A's** policy, never B's — content read from B's governance plane is data, never
governing policy for A. Screening is fail-closed: content matching the policy is
excluded; content that **cannot be classified is excluded, not indexed**. The
policy version is a snapshot input (RFC2-1 item 7), so what was screened is part
of every evaluation's identity — and the policy is honored **only under
RFC3-16(a)**, through an effective owner act bound to its exact digest: it is an
owner-approved declaration whose effect is to widen what Syzygy may take in, so
a permissive version an untrusted writer could mint would admit at every ingest
boundary exactly the content SEC-5 requires excluded, and the exclusion counts
would render honest about a screen that never screened. State (1) and state (2)
are both effective, with the exact state disclosed. A missing or invalid act
does not fail open: the ingest is blocked on RFC3-16(a)'s effect rule, never
performed under that policy. The act warrants use of the policy; it is never
evidence that screening succeeded or that admitted content is secret-free.

**RFC5-17.** Exclusions carry **hash-not-body provenance**: an excluded item is
recorded as (content digest, location reference, policy version, redaction
class) — never the content itself, in any store including the audit trail.
Redaction classes are closed: `excluded-artifact` (whole artifact withheld),
`redacted-span` (artifact retained, matching spans replaced by markers with a
count), `unclassifiable-excluded` (fail-closed default). Exclusions render with
counts (RFC2-23 "Excluded content").

**The classes map to Unknown differently** *(a scoping fix, **not** a vocabulary
extension — no new Unknown reason is added and RFC2-24's closure is untouched)*:
`excluded-artifact` and `unclassifiable-excluded` withhold the artifact entirely,
so **every claim that depended on it renders Unknown** (`excluded-content`,
RFC2-24 #7) with the exclusion count shown. `redacted-span` **retains** the
artifact with counted markers: a claim over the **surviving content** may still
stand, **at the tier it otherwise earned**, with the redaction count disclosed on
the claim; only a claim that **depends on a redacted span** renders Unknown
(`excluded-content`). Mapping the whole artifact to a blanket Unknown would
over-degrade usable partial evidence, which VIS-1 no more permits than
over-claiming does.

A secret reproduced in any surface, store, or endpoint is a trust-floor violation
regardless of this clause's observance elsewhere (trust-and-evidence.md floor
bullet 4).

---

## 4. Violation cases — this module

*Package numbering is stable; cases are distributed across modules, never
renumbered. Cases 1–4, 10 and 13 are in module 1, cases 7–9 and 12 in module 3,
case 11 spans two modules and is held in `README.md`.*

5. *(RFC5-14/15)* Source sent to an unnamed model provider; `code-content` embedded
   in a prompt sent under `derived-composites` consent alone; an index synced to a
   third-party service as a feature side effect; a composite whose embedded class
   could not be determined egressing under the class its composer asserted; an
   egress honored on a consent record whose owner-act provenance was never verified
   (RFC3-16(a)).
6. *(RFC5-16/17)* Unclassifiable content indexed "pending review"; an excluded
   secret's body in the audit trail; a connection string in a map tooltip (SEC-5's
   named violation); Project A screening B's tree under B's secret-detection policy;
   a `redacted-span` artifact rendering its entire surviving content Unknown.

---

## 5. Integration — this module

**Relies on RFC 0001:** the Consent record entity (RFC1-3) this class taxonomy
specializes; the Decision entity as approval/revocation warrant.
**Relies on RFC 0002:** snapshot inputs (classification- and secret-policy
versions, RFC2-1 item 7); Unknown reasons #6 and #7 and the failure-state
renderings (RFC2-23); RFC2-7's not-computed inferred layer; the RFC2-13 challenge
lifecycle RFC5-13 cites rather than sets.
**Relies on RFC 0003:** RFC3-16(a), the owner-act provenance predicate the egress
choke point (RFC5-15) cross-checks — stated once there and cited, never restated
here; RFC3-7 (consent record shape); RFC3-11 (workspace-manifest import);
RFC3-30 (cross-project read; the observing-project policy rule).
**Relies on module 1:** RFC5-11 (revocation is effective at the next act, and the
rendering obligation RFC5-13 depends on); RFC5-25 (the audit record every egress
check emits).
**Provides to RFC 0002:** the consent-record semantics behind Unknown reason #6.
**Provides to RFC 0003:** the fields consent records must encode; RFC 0003 owns
physical schema and migration.
**Provides to RFC 0004:** the ingest-boundary screening obligation on every
adapter read (RFC5-16), under the *observing* project's policy (RFC3-30).
**Provides to RFC 0006 and the surfaces (incl. RFC 0008):** the consent-rendering
obligation (SEC-2) and exclusion counts.
**Provides to RFC 0010 and RFC 0011:** the egress choke point (RFC5-15) and
ingest screening (RFC5-16) every governed context packet passes.
**Not this module's:** secret-detection policy *content* and classification-policy
*content* (quality/policy material); wire formats (RFC 0003 / RFC 0006).

---

## 7. Deliberately deferred — this module

Concrete schemas for consent records → RFC 0003. Adapter read-screening mechanics
→ RFC 0004. Secret-detection policy content → quality/evidence policy (craft).
Extension of the closed content-class vocabulary → amendment to RFC5-14, never
by a classification policy.

---

## 8. Owner questions

**None owned by this module.** Question numbers are RFC-level and immutable;
q1, q2, q5 and q6 live in `admission-and-boundary.md`, q3 and q4 in
`execution-profiles.md`. See `README.md` for the package question list.

Owner decision **B8** (egress consent: one record per *(project, provider)*, the
per-repository alternative declined) was the resolution of RFC 0003's §8 q3, not
a question of this RFC; it is binding in RFC5-12 and recorded at
`../../history/RFC-0005-history.md` §RFC5-12.

---

*End of module 2 of the RFC 0005 package. Clauses RFC5-12 … RFC5-17. No retired
numbers, no merged numbers, and no clause identity shared with another module.*
