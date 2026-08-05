# RC-8 — Evidence and security review (fresh context, adversarial)

**Reviewer role:** independent fresh-context security and evidence reviewer.
No authoring history was sought or read. `_bootstrap/**` was not opened.
**Date of review:** 2026-08-05. **Working tree:** clean at review start.

## 0. Method and what was actually examined

Read in full: `.syzygy/governance/doctrine/security.md`,
`.syzygy/governance/doctrine/trust-and-evidence.md`,
`.syzygy/governance/doctrine/README.md`; all four RFC-0002 modules; both
RFC-0003 modules (0003 `manifests-and-namespace.md` partially — RFC3-2,
RFC3-3, RFC3-30 and their neighbourhoods); all five RFC-0004 files; all four
RFC-0005 files; `SECURITY.md`;
`.syzygy/governance/policies/craft-and-care/security-and-secrets.md` and
`…/agent-provenance-and-execution-evidence.md`. Read selectively for
cross-checks: `RFC-0001-project-graph-identity-state-planes.md` (RFC1-19…22,
RFC1-25, RFC1-28…30), `RFC-0010-mission-control-autonomy.md` (RFC10-3…9),
`RFC-0011-context-compiler.md` (secret/egress lines),
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`,
`decisions/OWNER-ANSWERS-2026-08-01.md`,
`policies/craft-and-care/INSTALL-RECORD.md`, `PROJECT-STATUS.md`,
`round-2026-08/ARTIFACT-INVENTORY.md`, `scripts/check_governance.py`
(CG-7a…7d).

**Tooling note honoured.** `grep` here is ugrep; every load-bearing sweep in
this report was run through `python3 -re` over an explicit file list, not
through a bracket class. Two sweeps support universal claims and both are
reproduced below with their exact predicate.

Sweep A — rate limiting. Predicate
`rate[- ]?limit|rate bound|throttl|quota|per-second|requests per|backoff|lockout|brute`,
case-insensitive, over `.syzygy/governance/doctrine/**.md`,
`.syzygy/governance/policies/**.md`,
`.syzygy/governance/contracts/candidates/rfcs/**.md`, and `SECURITY.md`.
**Total hits: 2**, neither a rule:
`rfcs/RFC-0002/challenge-lifecycle.md:165` (a self-observation that there is
"no rate bound anywhere in this contract") and
`rfcs/RFC-0007/narrative-contract.md:298` (the word "quotable"). `[Observed]`

Sweep B — tamper-evidence / append-only. Predicate
`append-only|tamper|write-once|WORM`, case-insensitive, over all 32 RFC
modules. **Four hits, all in `RFC-0004/named-adapters.md` (lines 51, 194, 200,
222)**, and all of them say the *opposite* of an integrity mechanism — three
state that hash-carrying proves non-tampering rather than genuineness, one
requires a digest so "later readers can detect tampering with the stored
capture". **No clause anywhere requires any store to be append-only,
write-once, or tamper-evident.** `[Observed]`

---

## 1. CLAIM / EVIDENCE / WARRANT SEPARATION

### 1.1 The three are genuinely distinct, and the separation is enforced by named rules

This is the strongest part of the corpus. The separation is not a topic
mention; it is carried by four independent mechanisms.

**Definitions.** Evidence is defined at
`.syzygy/governance/doctrine/trust-and-evidence.md:10-12` — "a durable,
identified, integrity-verifiable artifact carrying its source, capture time,
scope, and provenance". The two non-evidence warrants are enumerated
immediately after at `trust-and-evidence.md:25-35`: the recorded human
decision, and the work warrant — with the discriminating sentence "**Status
describes; warrant authorizes**" at `trust-and-evidence.md:34`. A status claim
is defined by trigger, not by prose form, at `trust-and-evidence.md:39-46`
("A claim that meets any of these triggers is a status claim **whatever its
prose form**"), restated as a clause at
`rfcs/RFC-0001-project-graph-identity-state-planes.md:355-359` (RFC1-19).

**Structural enforcement 1 — one edge, one path.** RFC1-25 gives `supports`
as "**The only** path from evidence to positive status"
(`RFC-0001-project-graph-identity-state-planes.md:485`), with an explicit
"evidence-to-status backdoor" prohibition at line 434 and the anti-conflation
rule that "**No edge of any one sense is ever evidence of any other**" at line
519.

**Structural enforcement 2 — warrant is deliberately not an evidence-shaped
object.** `RFC-0001…:207-208`: "**Warrant** is deliberately not reified — it
is a property of the `motivates` edge or of a Decision, never a node." The
warrant edge `motivates` is typed Desired→execution and "Carries doctrine's
four warrant classes" (`RFC-0001…:473`).

**Structural enforcement 3 — the plane rule.** RFC1-22's Execution plane row
(`RFC-0001…:393`) reads "**May never satisfy a desired-state claim** — work is
never proof", and RFC4-18 applies it to the Execution Record explicitly:
"it may support claims about what the fleet did, and it may never satisfy a
desired-state claim" (`rfcs/RFC-0004/execution-record.md:71-73`).

**Structural enforcement 4 — derived objects are not warrants.** RFC1-21:
"A **derived gap is not a work warrant**: it motivates work only through a
confirmation act … because doctrine's warrant list admits a *confirmed*
finding and kernel-derived objects are not authorities"
(`RFC-0001…:371-375`). RFC3-2 carries the same rule for kernel records: "**A
`kernel-recorded` value is never authorization-bearing**: it records, and
recording authorizes nothing"
(`rfcs/RFC-0003/manifests-and-namespace.md:123-124`).

**No place was found where a claim and evidence are conflated, or where an
Execution Record is admitted as satisfying intent.** The one candidate —
RFC4-19's `warrant reference | EA` row, "Absent or unresolvable → Unknown,
never rejection" (`rfcs/RFC-0004/execution-record.md:91`) — is not a
conflation: it is honest description of an unwarranted run, and the
corresponding *gate* lives elsewhere (RFC1-29's orphaned-work contradiction,
`RFC-0001…:658-663`).

### 1.2 The inference-may-challenge-never-establish rule: clause found, and it holds

**Doctrine clause:** `trust-and-evidence.md:77-90` — "**Inference holds no
positive status authority — it holds challenge authority only.**"

**Contract clauses enforcing it, all four found:**

- `rfcs/RFC-0002/snapshot-and-evaluation-core.md:177-184` (RFC2-8, "Authority
  ceiling"): "it may never establish, raise, or independently satisfy a
  positive status claim."
- `rfcs/RFC-0002/rendering-vocabularies.md:159` (RFC2-25,
  `asserted-by-worker` row): "Visible, never green, challengeable, **never a
  status input**", parented to **Inferred**.
- `rfcs/RFC-0002/snapshot-and-evaluation-core.md:163` (RFC2-6): "Inferred
  material never enters it" — the observation record.
- `rfcs/RFC-0001…:392` (RFC1-22, Inferred plane row): "Challenge authority
  only; never establishes or raises a status".

**Leak paths hunted, and what was found.** Six candidate laundering routes
were tested; four are closed by clause and two are open.

*Closed.* (a) Composite content-class assertion — closed by RFC5-14's
"never an attribute the composing step asserts about its own output"
(`rfcs/RFC-0005/consent-egress-secrets.md:139-141`). (b) Adapter-derived run
identity — deterministic derivation, not inference, and collisions are
disclosed (`rfcs/RFC-0004/execution-record.md:113-127`). (c) Code markers
becoming declared mappings — gated at RFC4-26 on RFC3-16(a)
(`rfcs/RFC-0004/fidelity-joins-and-mappings.md:137-142`). (d) Version-skew
defaulting — closed by RFC4-8(c), "never defaulted, guessed, or zero-filled"
(`rfcs/RFC-0004/general-contract.md:169-172`).

*Open — leak 1 (labelled Inferred content inside an Evidence-class snapshot
input).* RFC4-21 permits an Inferred value to be written **into** an Execution
Record: "a cost computed from token counts and a rate table is **Inferred**
(rate tables drift) and labeled with its derivation"
(`rfcs/RFC-0004/execution-record.md:130-133`). Execution Records are Evidence
artifacts (RFC4-18, `…/execution-record.md:66-69`) and are a **deterministic
snapshot input** (`rfcs/RFC-0002/snapshot-and-evaluation-core.md:84-85`,
item 6). The seam rule that forbids Inferred material is written for the
*observation record* only (RFC2-6, RFC2-7) and for *overlays*; no clause
governs an Evidence artifact carrying labelled Inferred fields, and **no
clause requires the Inferred label to survive aggregation**. RFC4-24's
analogous protection exists for `reduced-fidelity` — violation case 11, "a
reduced-fidelity label is dropped in aggregation"
(`rfcs/RFC-0004/fidelity-joins-and-mappings.md:190-191`) — and has no
counterpart for RFC4-21's Inferred cost. Narrow today (cost only, and cost is
not a status claim), but the *shape* is the leak shape: inference captured as
a fact inside a deterministic input, with the label protected by nothing.

*Open — leak 2 (a lower tier declared sufficient for a completion claim).*
See §7.3.

---

## 2. OWNER ACTS AND FORGERY

### 2.1 It is enforced by clauses, not merely narrated — verified

The predicate is a clause with a stated subject, not a list:
`rfcs/RFC-0003/governance-homes-and-owner-acts.md:159-163` (RFC3-16(a)) and
the operative sentence at lines 206-209: "Such an artifact is honored **only
when its owner-act provenance is independently verifiable to Syzygy by a
mechanism the governed tree cannot forge**. Being present, well-formed, and
correctly attributed *in the tree* is not sufficient." Self-declaration is
killed at lines 122-124: "A tree-resident stamp is **never
self-authenticating**: `accepted` written in a file is a claim by whoever
wrote the file, not proof of acceptance." The failure posture is stated —
block the effect, render Unknown, mint a contradiction, never delete
(lines 289-298). The two-state rule is RFC3-16(c) (lines 316-369), with the
render vocabulary fixed at lines 346-348: "**'owner-adopted (bootstrap,
uncorrelated)'**; **never 'verified.'**"

Consuming gates cross-check rather than restate, and are enumerated at
lines 300-314 with the honest caveat "**This list tracks the gates; it does
not bound them.**" The two hardest gates are written as cross-checks:
RFC5-15 (`rfcs/RFC-0005/consent-egress-secrets.md:159-168`) and RFC5-18(c)
(`rfcs/RFC-0005/execution-profiles.md:84-90`). The `[Inferred]` fourth limb of
the predicate is *labelled* Inferred and is accompanied by an instruction to
treat sole-fourth-limb catches as a finding (lines 165-171) — this is unusually
honest drafting and I record it as such.

The interim posture is likewise clause-level, not narrative: RFC10-9
(`rfcs/RFC-0010-mission-control-autonomy.md:203-213`) refuses to let a
state-(1) record launch a mission at all.

**Verdict on the question as posed: yes, enforced by clauses.**

### 2.2 The attack surface — every path found by which a repository-writable artifact could be made to look like an owner act

The corpus is explicit that state (1) is forgeable in principle
(`…/governance-homes-and-owner-acts.md:322-331`; `SECURITY.md:55-58`). The
following are the concrete paths, with the clause that does or does not stop
each.

**A2-1 — Candidate installing itself into the accepted home. NOT blocked by
any mechanism; blocked only by a violation case and by human attention.**
The acceptance transaction at
`candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:84-112` has the
*lead* (an agent with write access to `.syzygy/**`) perform steps 2-5:
verify the digest, copy the 32 modules into
`.syzygy/governance/contracts/rfcs/`, write the act record into
`decisions/ACCEPTANCE-ACT-RECORD.md`, commit, and tag. The owner's only
unforgeable contribution is a chat phrase that never enters the repository.
An agent can perform all five steps unilaterally. The named violation case
exists — `…/governance-homes-and-owner-acts.md:425-426` case 7, "an accepted
RFC is installed into `contracts/` with no owner acceptance recorded" — but
nothing *detects* it: `scripts/check_governance.py` has no check that
`contracts/rfcs/` exists only alongside a corroborated act record, and the act
record is itself agent-writable. Worse, the repository's own navigation routes
authority **by location** (`AGENTS.md`, "Accepted home
`.syzygy/governance/contracts/rfcs/` is created only by act 1"), which is
precisely the signal an agent can mint. The corpus's stated defence is
honesty about the gap, not prevention — which RFC3-16(c) licenses, but the
consequence is that after act 1 the *only* thing distinguishing a real act
from a forged one is a human's memory of typing a phrase.

**A2-2 — Self-declared header stamp.** Fully blocked in the RFC corpus, which
carries a disclaimer paragraph in all 32 modules ("self-declaration at
authoring time … Absent such a record, this contract binds nothing", e.g.
`rfcs/RFC-0005/execution-profiles.md:14-19`) and the machine-readable
`status_source: owner-act-record` frontmatter key. **Not applied uniformly
outside the RFC corpus** — see §3.

**A2-3 — A digest quoted in two places where only one is checked. Partly
blocked; one live instance found.** `scripts/check_governance.py` CG-7d
(lines 601-698) is a genuinely good defence: it checks *every* copy of every
act digest, across every tracked `.md`, against the subject artifact
recomputed at run time, with a 60-character look-behind so a "stale"/"retired"
marker exempts only a line that actually says so. But the regexes require the
**act phrase** and a **full 64-hex** digest on the same line
(`ACT_SUBJECTS`, lines 607-624). A truncated digest quoted **without** the act
phrase is structurally invisible to it. Sweeping every tracked `.md` for
8-63-hex fragments followed by an ellipsis (excluding `reviews/`, `history/`,
`fixtures/`) found two live, unmarked, currently-wrong copies:

- `candidates/round-2026-08/ARTIFACT-INVENTORY.md:14` — "act-1 subject at
  manifest `5c4d6798…`". The manifest currently hashes to
  `f2914fc56cd2aa069b952747b9c78b00dc41d908830887ecd2f1addd37e61fc4`.
- `candidates/round-2026-08/ARTIFACT-INVENTORY.md:23` — bundle manifest
  "(`89279260…`, act-3)". `BUNDLE-MANIFEST.md` currently hashes to
  `7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45`.

Neither carries a retired/stale marker; the same table's act-2 cell
(line 13, `3858820f…`) *is* current, so a reader has no signal that two of
three are stale. That file's header disclaims counts and lifecycle labels
("this inventory asserts none", line 5-7) but says nothing about digests.
This is the exact hazard `AGENTS.md` names — "A derived value quoted for
convenience is a promise" — surviving the very round that built CG-7d to kill
it. `[Observed]`

Secondarily: `candidates/00-README.md:54` offers
`CONFIRM CRAFT AMENDMENT: CC-TEST-2@aa2d6353…` with no stale marker on the
line, and that file is in `ACT_QUOTE_EXEMPT`
(`check_governance.py:634`). Its own header (lines 3-8) does disclaim
globally, so this is mitigated, but a *file-level* exemption plus a
*line-level* unmarked retired offer is a pattern worth not repeating.

**A2-4 — An agent with write access to `.syzygy/**`.** This is the corpus's
own stated premise (`…/governance-homes-and-owner-acts.md:209-221`), extended
`[Inferred]` from SEC-3's executed-code class to workers' *commits*. The
extension is flagged for owner ratification at
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:270-271` (§7 item 2), which
is the right handling. But note the consequence chain: the entire predicate
rests on the RFC5-25 audit trail, and **that trail has no stated integrity
property** — see §8.1. An agent with write access to `.syzygy/**` cannot forge
a correlated act; an agent with write access to *wherever the audit trail
lands* can forge every act in the system, and no clause constrains that store
beyond its location.

**A2-5 — Correlation-by-editing.** Blocked, and blocked well:
`…/governance-homes-and-owner-acts.md:135-139` ("a required post-act stamp
edit would change the digest and thereby destroy the act it records") and
RFC3-16(b) item 3 (line 248-251), with violation case 14 (lines 438-442).

---

## 3. THE SELF-DECLARATION HAZARD

**The rule exists and is named.** `rfcs/RFC-0003/governance-homes-and-owner-acts.md:122-124`
("A tree-resident stamp is **never self-authenticating**") plus the two-must-be-
readable-apart obligation at lines 140-145 and the no-act-means-unadopted rule
at lines 146-150.

**It is not uniformly applied.** The RFC corpus applies it perfectly — 32/32
modules carry the disclaimer and `status_source: owner-act-record`. Outside
the RFC corpus, four classes of artifact carry a bare self-declared status in
their own header with no disclaimer and no RFC3-16(c) render vocabulary. All
were located by scanning the first 20 lines of every `.md` under
`doctrine/`, `policies/`, and `map/` for a status-shaped line:

1. `.syzygy/governance/doctrine/README.md:3` — "> **Status:** Adopted project
   doctrine — owner adoption `ADOPT DOCTRINE`, 2026-07-30." A bare "Adopted",
   in the file's own header, for a state-(1) act. **This is also the only
   place the doctrine's adoption status is written at all**: `security.md`,
   `trust-and-evidence.md`, `vision.md`, `architecture.md` and `v1.md` carry
   **no** stamp, so a reader who opens `security.md` alone has no signal
   either way, and the sibling that supplies the signal is not digest-bound to
   any of them. There is no recorded content digest for any adopted doctrine
   file anywhere in the tracked tree (searched: no `sha256` line names a
   `doctrine/` file). RFC3-16(c) state (1) requires "the **exact content
   digest** of the artifact acted on" (line 322-325). **The adopted doctrine
   does not satisfy the corpus's own state-(1) record shape.**
2. `.syzygy/governance/policies/craft-and-care/*.md:1` (nine files) — "> 
   **Approved** — owner decision D2 (2026-08-01) …". A bare "Approved" in each
   file's own first line. Mitigated by `INSTALL-RECORD.md`, which does carry a
   digest block and act-2 gating, but the nine banners themselves are exactly
   the "`accepted` written in a file" form RFC3-16 names.
3. `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md:17` —
   "**Status:** these policies are owner-approved engineering standards".
4. `PROJECT-STATUS.md:20-22` — "✅ **Adopted**", "✅ **Approved**",
   "✅ **Recorded**". This file *does* carry a strong self-disclaimer at
   lines 3-8 ("must not be the sole source"), which is good practice and
   materially reduces the finding.

**None of these claims "verified"**, so RFC3-16(c)'s hard prohibition
(lines 341-345) is not breached. What is breached is the softer half — "The
truthful render of state (1) is **'owner-adopted (bootstrap, uncorrelated)'**"
(lines 346-348). The corpus's own repository-level renders do not use the
vocabulary the corpus mandates for the state they are in. `SECURITY.md:52-58`
is the one place that gets this right, and it is excellent: "It does not claim
its governance records are independently verified: records in this tree sit
within the write reach of the actors they govern."

---

## 4. CONSENT AND EGRESS

### 4.1 What must happen before data leaves the machine — a named rule exists

`rfcs/RFC-0005/consent-egress-secrets.md:159-168` (RFC5-15): a **single choke
point**, three parts, all must pass — consent in force; content class
determinable and within the consented set under a classification policy whose
**own** owner-act provenance verifies; and the consent record's own
RFC3-16(a) provenance. Plus: "A feature that transmits as a side effect
without traversing the choke point is the SEC-2 violation, whatever its
intent" (line 166-167). The double-provenance requirement (policy *and*
record) is correct and the reasoning for it — a forged classifier defeats the
gate while telling the truth about the consent record — is stated at
lines 130-136. The remote-backing-store limb (FD-009) is folded in at
lines 168-169.

Fail-closed in both directions is a clause, not an aspiration: RFC5-14's
"A composite whose class **cannot be determined fails closed** — the egress is
**refused and the refusal rendered**" (lines 143-147); RFC5-16's ingest side
(lines 184-186). Composite class inheritance is stated as "highest embedded
class", with the anti-laundering rule "`derived-composites` consent alone
never launders an unconsented class into an egress" (lines 128-129).

### 4.2 Scoped, revocable, per-destination — yes. Expiring — **no.**

- **Scoped:** yes, twice over — per class (RFC5-12, one class per record
  instance, lines 78-95) and per (Project, provider) with an enumerated
  content-class set (line 87-90, owner decision B8).
- **Per-destination:** yes — "one record per *(Project, provider)* pair"
  (line 87-88); "Providers not named require fresh consent" (line 135).
- **Revocable:** yes, and unusually well — RFC5-13 (prospective, no history
  rewrite, lines 98-109), RFC5-11's act-versus-claim rule making revocation
  effective at the next act rather than the next evaluation (lines 234-242),
  B4's forced evaluation (lines 253-264), RFC5-26's uniform semantics
  (lines 316-321), and the rule that revocation is *not* a challenge
  resolution (`rfcs/RFC-0002/challenge-lifecycle.md:181-190`).
- **Expiring: no.** RFC5-12's mandatory field list is "class, subject, scope,
  granting principal, grant instant, and revocation state"
  (`…/consent-egress-secrets.md:93-94`) — **no expiry**. Verified by sweeping
  all four RFC-0005 files for `expir`: **one hit**, and it is the *credential*
  record's expiry field (`admission-and-boundary.md:191`), not consent's.
  RFC3-16(b) item 8 makes expiry optional by design ("no act lapses silently
  except by an expiry the act itself declared", line 258-261). The asymmetry
  is stark: dismissals **must** carry an expiry (VIS-6; RFC1-20,
  `RFC-0001…:361-366`); trusted-external-oracle declarations **must** carry an
  expiry (RFC4-13 route 3, `rfcs/RFC-0004/named-adapters.md:164-173`, with the
  reasoning "without scope and expiry, a single declaration silently makes
  everything `gate-backed` forever"); execution consent must be re-approved per
  profile version (RFC5-23, `…/execution-profiles.md:173-176`). **Egress
  consent to a model provider — the single highest-blast-radius consent in the
  system — is the one that never expires and never needs re-affirmation.**
  The identical argument the corpus uses to bound route 3 applies verbatim
  here and was not applied.

### 4.3 Secrets — in evidence, in execution records, in context packets

- **Ingest, universally:** RFC5-16 (`…/consent-egress-secrets.md:173-193`) —
  applied at "**every ingest boundary** … *before* content enters any Syzygy
  store, surface, or endpoint", with the enumeration explicitly declared
  "**illustrative … not exhaustive**" and the closing rule "if content crosses
  into a Syzygy store, it crossed an ingest boundary". This is the right shape
  and closes the enumeration-leaves-the-last-one-unguarded failure.
- **Whose policy:** the *observing* project's, never the observed source's
  (RFC5-16 line 186-188; RFC3-30
  `rfcs/RFC-0003/manifests-and-namespace.md:433-441`; RFC4-12
  `rfcs/RFC-0004/named-adapters.md:118-123`). Correct and non-obvious.
- **In execution records:** `rfcs/RFC-0004/execution-record.md:103` — prose
  fields admitted only through the observing project's policy; "Prompt/transcript
  bodies never enter; a prompt hash may", with the authority correctly
  identified as SEC-5 and RFC5-17 (storage) **not** SEC-2 (egress). The
  storage/egress distinction being called out explicitly is good work.
- **Exclusion provenance:** RFC5-17 hash-not-body, three closed redaction
  classes, "never the content itself, in any store including the audit trail"
  (`…/consent-egress-secrets.md:195-200`), with the `redacted-span`
  partial-survival rule that avoids over-degrading (lines 203-213).
- **In context packets:** `rfcs/RFC-0011-context-compiler.md:166-168` —
  "secret material never enters packets or memory (SEC-5, RFC5-16/17)", and
  packet content crossing an egress boundary passes RFC5-14/15; "a packet is
  not a consent".
- **Craft layer:** CC-SEC-5 and CC-SEC-6
  (`policies/craft-and-care/security-and-secrets.md:71-103`), with the
  strongest single sentence in the policy set at lines 96-99: a necessity
  determination to retain a body is "a **recorded decision under a declared
  policy or an owner decision naming the artifact class** — never a
  per-artifact implementer judgment".

### 4.4 Gaps found in this section

- **Consent has no expiry** (above) — the material gap.
- **Pre-A1 total-blockage is disclosed in the wrong place.** Because RFC5-16's
  secret-detection policy, RFC5-14's classification policy, and observation
  consent itself are all honored **only** under RFC3-16(a), and no artifact can
  satisfy RFC3-16(a) until the A1 ceremony ships, the composed consequence is
  that **no ingest and no egress is lawful at all before A1** — not just
  Mission Control. The owner did knowingly accept this: decision **A9**
  (`decisions/OWNER-ANSWERS-2026-08-01.md:30`) — "a fresh install renders
  contradiction-or-blocked-effect on every consent, adoption and policy until
  it lands", with the carried risk named. But the acceptance record's
  owner-attention list surfaces the hard-precondition consequence for
  **Mission Control only** (§7 item 6,
  `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:278-285`), and RFC10-9
  says "the same pre-A1 posture RFC5-15 and RFC5-18(c) already impose"
  (`RFC-0010…:212`) without saying that observation is in the same posture. A
  reader of the acceptance record alone would not learn that V0 cannot
  *observe* anything until the ceremony ships.

---

## 5. MACHINE CLIENTS

### 5.1 Authenticated — yes. Authorized — yes. Attributable — yes. Rate-limited — **no.**

- **Authenticated:** RFC5-5 (`rfcs/RFC-0005/admission-and-boundary.md:153-158`)
  — "admitted **only** through an explicit machine-client authentication
  mechanism … There is no anonymous machine access on any interface, loopback
  included", with the closed unauthenticated endpoint set (liveness/health +
  auth bootstrap). Classification is by credential, never location (RFC5-3,
  lines 100-106). The two-class closure (lines 108-116) explicitly forecloses a
  third class and explicitly names the CLI, MCP adapters, scripts and fleet
  workers as machine-class "without exception" (lines 160-167). Violation case
  13 (lines 346-349) covers the "it's first-party" excuse.
- **Authorized:** RFC5-6 (lines 171-193) — deny-by-default scoping, "An
  unscoped credential is invalid, not all-powerful"; credentials "never
  self-issued, never minted by another machine credential"; verifier-only
  storage.
- **Attributable:** RFC5-25 (lines 292-300) — every admission, denial, egress,
  run launch, adapter effect, consent act, and credential act emits an audit
  record naming principal, credential/session identity, act, subject, exposure
  mode, instant, outcome. Violation case 10 covers "an authenticated act whose
  principal cannot be recovered from the audit trail" (lines 340-345).
- **Rate-limited: no, nowhere.** Sweep A above: zero rules across doctrine,
  craft policies, `SECURITY.md`, and all 32 RFC modules. RFC5-6's scope list
  includes "trigger evaluations" (line 182-183) with no bound on how often;
  RFC5-5's unauthenticated set includes "the authentication bootstrap itself"
  (line 157-158) with no attempt bound, lockout, or backoff; RFC5-4's
  first-run pairing (line 120-122) likewise. The corpus is *aware* of the
  volumetric class of attack — RFC2-13 reasons explicitly about "a denial-of-
  truth path with **no rate bound anywhere in this contract**"
  (`rfcs/RFC-0002/challenge-lifecycle.md:164-166`) and mitigates it for
  inference-minted challenges with a human admission act — but generalises the
  insight nowhere else. An authenticated machine client with only *read* +
  *trigger-evaluation* scope can pin the kernel indefinitely, and each forced
  evaluation is lawful.

### 5.2 The boundary: can a machine client do what a human owner can?

**No — but the general prohibition is stated only for Missions.** The
strongest sentence in the corpus on this point is RFC10-3: "Holding a
mission-affecting scope permits **submitting** the corresponding act for owner
attendance and nothing more — a machine credential can never itself produce
the owner act the submission awaits"
(`rfcs/RFC-0010-mission-control-autonomy.md:101-104`). RFC10-8's
no-self-widening rule (lines 180-201) and RFC10-5's "an agent's 'condition
cleared' assertion never takes that transition" (lines 136-138) reinforce it.

But **RFC 0005 itself contains no equivalent clause.** RFC5-1 says machine
clients act "on the owner's behalf under their own credentials, never the
owner's" (`admission-and-boundary.md:78-81`) — that is an attribution rule,
not a capability boundary. RFC5-6's scope enumeration is open-ended ("which
projects it may read, whether it may submit proposals, trigger evaluations, or
reach adapter-mediated effects", lines 181-183) with granularity deferred to
"RFC 0003/0006 schema material" (line 185-186). Nothing in RFC 0005 forbids a
scope named `approve-consent` or `adopt-policy`. The boundary is *derivable* —
RFC3-16(a) requires an owner-attended ceremony, so no credential-borne act can
produce owner-act provenance — but it is derived, not stated, and it lives two
contracts away from the credential-scope schema that will be written against
RFC5-6. A specification author reading RFC 0005 alone would find no rule
against minting an owner-act scope.

**Can a machine client *trigger* an owner act?** Yes, and correctly so:
submission is permitted, the act is not (RFC10-3). No path was found by which
a machine client's submission auto-converts into an act.

### 5.3 One escalation chain worth naming

`RFC5-6` requires credential issuance "Only through an owner-attended ceremony
on an already-trusted channel (**an authenticated session**, or the serving
host's own console)" (`admission-and-boundary.md:176-178`). Per owner decision
**B9**, "Session identity is the credential and nothing else" — no device,
no network-layer binding — and the clause itself states the consequence: "an
escaped session credential is a **complete session anywhere**"
(lines 125-131). Composing the two: **a stolen session cookie is sufficient to
mint a durable, scoped machine credential.** Session revocation (required,
lines 136-140) does not touch the minted credential; credential revocation is
a separate act (RFC5-6, line 189) the owner has to know to perform. No clause
requires notifying the owner of credential issuance, requires a second factor
for issuance specifically, or bounds issuance rate. RFC5-4 correctly identifies
lifetime and revocation as "the **only** remaining mitigations" for a session —
but issuance-from-session escapes both, because the artefact it produces
outlives the session.

---

## 6. EXECUTION PROFILES

**What it is:** a declared, versioned artifact in the governed plane
(`rfcs/RFC-0005/execution-profiles.md:82-84`, RFC5-18(b)).

**What it bounds** (RFC5-20, lines 120-140): isolation mechanism class;
filesystem read/write scope ("nothing else is visible"); credential scope,
deny-by-default, host environment stripped, "**no ambient credential is ever
inherited**", references not secret material, **no credential that
authenticates to Syzygy itself**; network policy, default-deny, closed grammar
`none` / `loopback-only` / enumerated destination list with no wildcards and a
mandatory exclusion of Syzygy's own listening interfaces; resource limits on
CPU, memory, disk, wall clock, and process count; destructive-operation gates.

**The floor** (RFC5-21, lines 142-161): three closed isolation classes,
**no "none" class** — "a profile that cannot certify the floor is not a
permissive profile, it is an invalid one". The control-plane exclusion must be
"**enforced by the isolation mechanism and not merely declared**" (line 147-149)
— this is the clause that defeats the obvious DNS-resolves-to-loopback bypass,
and I confirm it does so. Violation set includes undeclared egress, any attempt
to reach Syzygy's control plane, out-of-scope writes, resource-bound breach,
and out-of-purpose credential use; a violating run terminates and its outputs
cap at `report-fact`.

**The five-part gate** (RFC5-18, lines 81-97) with `execution-blocked` as a
*primary* Unknown reason routed to "unblock or authorize the run" rather than
"capture evidence" — and expandable to which of (a)…(e) failed. The reasoning
for why #12 is not an annotation on #2 is at
`rfcs/RFC-0002/rendering-vocabularies.md:126-132`.

**The read-is-not-execution boundary and its trap** (RFC5-19, lines 99-118):
reading an externally produced artifact needs no profile, "**but reading it
confers no tier**" — with the `[Inferred]` explanation of exactly why the
inverse reading would be fatal ("untrusted code writes a report to disk,
Syzygy reads it as 'observation', and the artifact enters at the one tier that
can turn an indicator green without ever passing containment"). This is the
single best-reasoned paragraph in the security package.

**Can it be escalated at runtime? No — by three independent clauses.**
RFC5-23 (lines 173-182): "any amendment mints a new version requiring fresh
owner approval — approval never carries across versions silently"; profile
identity and version are snapshot inputs; running processes are terminated on
revocation; "no project executes under another project's consent". RFC10-8's
no-self-widening (`RFC-0010…:180-201`). RFC5-18(c)'s per-launch provenance
cross-check.

**By whom is it escalated? By the owner, per version, via a Decision whose
provenance the gate cross-checks.** Correct.

**The one gap in this section.** RFC5-22 (lines 163-172) permits a profile to
enable a destructive-operation class as either per-run human-gated or
**standing-approved** — "except that classes touching security posture,
privacy or retention obligations, or normative data contracts are **always
per-run human-gated** … no profile can standing-approve them." The carve-out
is subject-matter-shaped ("touching security posture") while the enable-able
units are operation-class-shaped ("pushing to version-control remotes").
Whether a *particular* standing-approved push touches security posture is a
runtime determination, and **the clause names no decider.** If the running
agent makes it, that is self-certification of exactly the kind VIS-4 forbids
and which RFC2-13 refused for inference-minted challenges
(`challenge-lifecycle.md:160-169`). If the kernel makes it, no clause says how
it classifies. If a policy makes it, that policy is authorization-bearing and
nobody has said so.

---

## 7. EVIDENCE TIERS

### 7.1 The registry — six tiers, closed (RFC2-25, `rfcs/RFC-0002/rendering-vocabularies.md:147-161`)

| Tier | Parent label | What it licenses |
|---|---|---|
| `gate-backed` | Observed | **The only** tier that may support a positive status claim — Aligned, Converged, reconciled, green (line 156) |
| `report-fact` | Observed | Claims about the report only; "Y itself is not thereby Observed" (line 157) |
| `reduced-fidelity` | Observed | Full Observed authority **at its declared granularity only**; finer questions render Unknown, never invented (line 158) |
| `asserted-by-worker` | Inferred | Visible, never green, challengeable, **never a status input** (line 159) |
| `declared-only` | Unknown | Declaration is Observed; satisfaction is Unknown; **both halves must render** (line 160) |
| `suspended` | Unknown | No positive authority while suspended; the basis is never erased (line 161) |

Plus three closed **sibling surface states** outside the registry —
`dismissed-by-decision`, `unadopted-draft`, `editorial-draft` (lines 163-179) —
which *replace* a status rendering; and `challenge-pending`
(`challenge-lifecycle.md:107-127`), which *accompanies* an unchanged one. The
governing meta-rule is at line 148-151: "a tier never becomes a fourth
epistemic label", and "an untier'd claim renders at its bare label".

The `gate-backed` entry predicate is the four-route provenance test of RFC4-13
(`rfcs/RFC-0004/named-adapters.md:151-205`), with the correct floor: "A
retained, well-formed, revision-bound artifact of **unverifiable origin caps
at `report-fact`** … Format, retention, and hash-carrying prove
**non-tampering, not genuineness**" (lines 191-197). Route 3 is bounded by
(project, gate class) scope and a mandatory expiry with its reasoning stated
(lines 164-173). Route 4's governed checker carries the `return PASS`
acceptance test (lines 282-287) and a separation-of-authorship rule — "a
worker **may run** a governed checker over its own change; it may **not
author, select, or amend** the checker definition that certifies that same
change" (lines 274-279). Route 2 is bound to a *captured* confirmation, never
a live re-query (RFC4-13(a), lines 212-240).

### 7.2 Places checked where a lower tier could be treated as sufficient — and found closed

- Execution-record gate rows: `gate-backed` "only under **both** RFC4-13
  predicates", unverifiable origin caps at `report-fact`
  (`rfcs/RFC-0004/execution-record.md:99`). Closed.
- Runs Syzygy launched with no recoverable profile identity: "not attributable
  and its outputs cannot be `gate-backed`" (`…/execution-record.md:101`). Closed.
- Policy-violating runs: cap at `report-fact` (RFC5-21, `execution-profiles.md:153-154`).
  Closed.
- Aggregation of report facts: CC-PROV-4 — "never upgraded by repetition or by
  aggregation across many agreeing reports"
  (`policies/craft-and-care/agent-provenance-and-execution-evidence.md:76-79`).
  Closed.
- Absence claims: RFC4-27 requires an *executed* coverage record; "an
  unexecuted mapping is not evidence of absence"
  (`fidelity-joins-and-mappings.md:145-153`). Closed.
- Reconciliation: `reconciled@E` "a positive status claim requiring gate-backed
  Observed evidence" (`rfcs/RFC-0002/reconciliation-chain.md:175-177`); scheduler
  closure never implies it (RFC2-20, lines 215-222). Closed.

### 7.3 The one place where a lower tier is treated as sufficient

RFC10-6: "The completion predicate declares the **minimum RFC2-25 evidence
tier** it accepts (unstated means, per RFC10-7's narrow reading, the strongest
applicable tier), and the completion render discloses the tier actually
achieved (VIS-2) — 'all work items closed' or worker assertion alone never
satisfies a conforming predicate"
(`rfcs/RFC-0010-mission-control-autonomy.md:146-152`).

The narrow default and the exclusion of `asserted-by-worker` are right. But
the clause **explicitly permits an owner-approved predicate to name
`report-fact` as its accepted minimum**, and a mission reaching `completed`
(`RFC-0010…:127`) is a terminal green state on a surface. RFC2-25 reserves
positive status claims — "Aligned, Converged, reconciled, green" — to
`gate-backed` alone. The two are consistent only if "mission completed" is not
a positive status claim; **no clause states that**, and RFC1-19's definition
of a status claim ("anything that turns an indicator green",
`RFC-0001…:355-357`) points the other way. Tier disclosure at the render is a
mitigation, not the bar. This is the corpus's own §7-item-6-style
knowing-acceptance shape, but it was not surfaced as one.

---

## 8. INTEGRITY

### 8.1 There is no defined integrity mechanism. It is an unmet aspiration, and the gap is **not** rendered Unknown.

Doctrine requires evidence to be "integrity-verifiable"
(`trust-and-evidence.md:10-11`). The corpus repeats the word in five places
(sweep B and the `integrity-verifiab` sweep): `rfcs/RFC-0004/README.md:111`,
`rfcs/RFC-0004/execution-record.md:27` and `:67`,
`rfcs/RFC-0004/named-adapters.md:200`,
`rfcs/RFC-0005/admission-and-boundary.md:297`. In every case it is *asserted as
a property the artifact has*, never *specified as a mechanism the system
provides*.

What actually exists is a **digest field on some artifact classes**:
`RFC-0001…:160-161` (observation record: "evaluation identity + integrity
digest"; evidence artifact: "identifier + integrity digest"),
`rfcs/RFC-0004/named-adapters.md:221-222` (external-confirmation capture: "a
**digest or integrity identity of the response**, so later readers can detect
tampering with the stored capture"), `RFC-0005/consent-egress-secrets.md:196`
(exclusion records by content digest). A digest is an integrity mechanism only
against an adversary who cannot rewrite the digest. **The corpus states the
adversary can.**

The consequences, in order of severity:

- **The audit trail — on which the entire owner-act predicate rests — has no
  integrity property whatsoever.** RFC5-25's *only* stated defence is
  **location**: "outside `.syzygy/**` and outside the untrusted actor class's
  write reach", and it explicitly leaves everything else open — "The trail's
  storage schema and medium remain implementation-slice choices; its exclusion
  from the governed tree and from untrusted write reach does not"
  (`admission-and-boundary.md:302-312`). Sweep B confirms **no clause anywhere
  in the 32 modules requires the trail to be append-only, write-once,
  tamper-evident, externally attested, or replicated.** RFC3-16(a) chose
  ceremony+audit-correlation over owner-held keys precisely to avoid custody
  burden (`governance-homes-and-owner-acts.md:222-237`), and A1's own recorded
  text names the derived constraint as location only
  (`decisions/OWNER-ANSWERS-2026-08-01.md:21`: "the mechanism's defense is
  entirely contingent on that"). It is contingent on *more* than that, and the
  corpus does not say so: a trail that is out-of-tree but append-writable by
  the same host process that fleet workers can reach is out-of-tree and
  forgeable. **This is the deepest single gap in the package**, because every
  RFC3-16(a) gate — egress, execution launch, mission approval, secret policy,
  oracle policy, marker policy, retention bound, currency bound, checker
  definition — resolves through it.
- **Execution Records assert immutability with no mechanism.** RFC4-18: "durable,
  identified, integrity-verifiable, **immutable once recorded** — residing under
  `.syzygy/work/**`" (`execution-record.md:66-69`). `.syzygy/work/**` is inside
  the governed tree, which RFC3-16(a) declares writable by the untrusted actor
  class. "Immutable once recorded" is therefore a *policy about how Syzygy
  writes*, not a property of the store, and nothing renders that distinction.
  RFC2-6's observation-record immutability (`snapshot-and-evaluation-core.md:151`)
  has the same shape and the same store problem.
- **The honest-Unknown obligation is not discharged for this gap.** VIS-2 and
  the corpus's own pattern (RFC2-9's `no-currency-bound-declared`, RFC4-16's
  undeclared retention bound, RFC4-23's undeclared staleness bound) is:
  where a required declaration does not exist, the dependent class renders
  Unknown until it does. There is **no** equivalent for integrity — no Unknown
  reason in RFC2-24's twelve names an unverifiable-integrity condition, no
  clause says "until an integrity mechanism is declared, evidence renders at a
  reduced tier", and `SECURITY.md`'s otherwise-excellent
  "what this project does not claim" section (lines 52-58) names the
  independent-verification gap for *governance records* and not the integrity
  gap for *evidence*. The corpus's cardinal rule — "No evidence yields Unknown
  — never green, never zero (VIS-2)" — is applied everywhere except to the
  property that makes evidence evidence.

The one place the corpus reasons correctly about this is
`named-adapters.md:194-197`: "Format, retention, and hash-carrying prove
**non-tampering, not genuineness**". That insight is applied to *gate
artifacts* and stops there; it is not applied to the audit trail, to Execution
Records, or to the observation record.

---

## 9. ADVERSARIAL SUMMARY — the three most dangerous things a fleet could do

**#1 — Forge every authorization in the system by writing to the audit
trail.** Not by writing into `.syzygy/**` (that is anticipated and blocked at
RFC3-16(a)), but by reaching whatever store the RFC5-25 trail lands in. The
permitting clause is `admission-and-boundary.md:302-312`, which specifies the
trail's **location** and expressly leaves its **schema and medium** to
implementation, with no append-only, tamper-evidence, or attestation
requirement anywhere in the corpus (sweep B). Every RFC3-16(a) gate resolves
through this trail (`governance-homes-and-owner-acts.md:300-314`), so one
writable trail yields: any egress consent, any execution profile approval, any
mission approval, any secret-detection policy, any trusted-oracle declaration —
each of which then reads as fully verified at state (2), the state the corpus
reserves for "independently verified". The forgery is not detectable by any
downstream check, by construction: RFC3-16(a) exists precisely because "no
downstream status check can falsify" these artifacts.

**#2 — Mint a durable machine credential from a stolen session, then outlive
the response.** Permitted by the composition of
`admission-and-boundary.md:176-178` (issuance channel = "an authenticated
session") with `admission-and-boundary.md:123-131` (owner decision B9: no
device binding, "an escaped session credential is a **complete session
anywhere**"). No clause requires owner notification on issuance, a second
factor for issuance specifically, or any issuance rate bound; and session
revocation — the clause's own "**entire** remaining mitigation" — does not
revoke what the session minted. Compounded by the total absence of rate
limiting (sweep A): the unauthenticated bootstrap endpoint (RFC5-5,
line 157-158) and the pairing act (RFC5-4, line 120-122) are both unbounded.

**#3 — Manufacture green at scale through a mission whose completion predicate
accepts `report-fact`, or hold the kernel down while doing it.** Permitted by
`RFC-0010…:146-152`, which lets an owner-approved completion predicate name
`report-fact` as its accepted minimum while RFC2-25 reserves positive status to
`gate-backed` — with no clause saying that "mission completed" is not a status
claim. The volumetric half is permitted by absence: an authenticated machine
client holding only read + trigger-evaluation scope (RFC5-6, lines 181-183) can
force evaluations without bound, and RFC5-11's B4 strengthening
(lines 253-264) makes every revocation *also* force one. The corpus identified
this exact class of attack for challenges — "a denial-of-truth path with no
rate bound anywhere in this contract"
(`challenge-lifecycle.md:164-166`) — and fixed it only there.

Honourable mention (not top three because it is disclosed): a fleet worker
installing the candidate corpus into `contracts/rfcs/` and appending its own
`ACCEPTANCE-ACT-RECORD.md` row. Anticipated as violation case 7
(`governance-homes-and-owner-acts.md:425-426`), rendered honestly by
RFC3-16(c), and undetectable by any current mechanical check.

---

VERDICT: EXCEPTIONS

### Findings

**F1 [Blocking] — The audit trail on which every owner-act gate rests has no
required integrity property.** `rfcs/RFC-0005/admission-and-boundary.md:302-312`
specifies location and expressly defers schema and medium; sweep B confirms no
append-only, write-once, tamper-evidence, or attestation requirement exists
anywhere in the 32 modules. RFC3-16(a) (`…/governance-homes-and-owner-acts.md:206-237`)
makes the entire authorization system contingent on this artifact.
*Minimal fix:* add one sentence to RFC5-25's location paragraph — "The trail
must additionally be **append-only and tamper-evident**: a record, once
written, is not modifiable or deletable by any principal Syzygy admits,
including Syzygy itself, and the trail carries a verifiable chain (per-record
digest linkage or equivalent) that a correlation check validates before
honoring any RFC3-16(b) item 9 binding. Mechanism is an implementation choice;
the property is not." Cite it from RFC3-16(a)'s mechanism-class paragraph.

**F2 [Blocking] — "Integrity-verifiable" is asserted but never specified, and
the gap is not rendered Unknown as VIS-2 requires.** `trust-and-evidence.md:10-11`
vs. `rfcs/RFC-0004/execution-record.md:66-69` (immutability asserted for
`.syzygy/work/**`, a store the corpus itself declares untrusted-writable) and
`rfcs/RFC-0002/snapshot-and-evaluation-core.md:151`. Every other undeclared
required property in the corpus renders its dependents Unknown (RFC2-9,
RFC4-16, RFC4-23); integrity alone does not.
*Minimal fix:* add to RFC4-18 (or RFC 0002 §3) — "Integrity-verifiability is a
**declared property of an evidence class**, naming the mechanism by which a
reader detects modification and the store guarantee it rests on. Until a class
declares it, its artifacts are admissible but **cannot support a positive
status claim**: they cap at `report-fact`." This reuses RFC2-9's exact
mechanism and needs no new Unknown reason.

**F3 [Blocking] — Egress consent never expires.** RFC5-12's mandatory field
list (`rfcs/RFC-0005/consent-egress-secrets.md:93-94`) omits expiry; verified by
sweeping all four RFC-0005 files (one `expir` hit, on credentials). The
corpus's own reasoning for bounding trusted-external-oracle declarations —
"without scope and expiry, a single declaration silently makes everything
`gate-backed` forever, and nothing in this contract would later surface that it
had" (`rfcs/RFC-0004/named-adapters.md:170-173`) — applies verbatim to a
standing model-provider egress grant and was not applied.
*Minimal fix:* add to RFC5-12's field sentence — "and, for **egress** and
**execution** consent, a **declared expiry**; an egress consent with no expiry
is invalid, not indefinite. Renewal is a fresh grant with a fresh record
(RFC5-26)." Values are quality-policy material; the obligation is the clause's.

**F4 [Non-blocking] — No rate bound exists anywhere for machine clients.**
Sweep A: two hits across doctrine, craft policies, `SECURITY.md`, and all 32
modules, neither a rule. Unbounded surfaces: the unauthenticated bootstrap
endpoint (`admission-and-boundary.md:157-158`), first-run pairing (line 120-122),
credential issuance (lines 176-178), and the `trigger evaluations` scope
(lines 181-183) compounded by B4's forced evaluations (lines 253-264). The
corpus reasons about exactly this attack class at
`rfcs/RFC-0002/challenge-lifecycle.md:164-166` and generalises it nowhere.
*Minimal fix:* one clause in RFC 0005 §3.3 — "Every machine-credential scope
carries a **declared rate bound** on the acts it permits; an unbounded scope is
invalid, not unlimited. Unauthenticated bootstrap and pairing endpoints carry a
declared attempt bound with a declared lockout. Values are quality-policy
material; declaring them is this clause's." Extends RFC5-6's existing
deny-by-default shape rather than adding a concept.

**F5 [Non-blocking] — A stolen session mints durable machine credentials that
outlive session revocation.** `admission-and-boundary.md:176-178` (issuance
channel) composed with lines 123-131 (B9: no device binding; escaped session =
complete session anywhere). Session revocation is named the "**entire**
remaining mitigation" but does not reach the credentials the session created.
*Minimal fix:* add to RFC5-6 *Issuance* — "A credential minted through a
session inherits that session's fate: revoking a session revokes every
credential issued during it unless the owner re-attests each, and every
issuance emits an audit record the owner is surfaced (RFC5-25)."

**F6 [Non-blocking] — RFC 0005 states no capability boundary between a machine
credential and an owner act; the rule exists only in RFC10-3.** Compare
`rfcs/RFC-0010-mission-control-autonomy.md:101-104` (explicit, excellent) with
RFC5-6's open-ended scope enumeration (`admission-and-boundary.md:181-186`),
which forbids no scope by name and defers granularity to RFC 0003/0006. A
specification author reading RFC 0005 alone finds no rule against an
`approve-consent` scope.
*Minimal fix:* one sentence in RFC5-6 *Scoping* — "**No scope may authorize an
owner act.** A credential may permit *submitting* an act for owner attendance
(RFC10-3); producing the owner-act provenance RFC3-16(a) requires is outside
every machine-credential scope, present and future."

**F7 [Non-blocking] — RFC5-22's always-human carve-out names no decider.**
`rfcs/RFC-0005/execution-profiles.md:163-172`: enable-able units are
operation-class-shaped, the carve-out is subject-matter-shaped ("touching
security posture, privacy or retention obligations, or normative data
contracts"), and the runtime classification is assigned to nobody. If the
running agent classifies, that is the self-certification RFC2-13 refused for
inference (`challenge-lifecycle.md:160-169`).
*Minimal fix:* append to RFC5-22 — "Whether a given invocation falls in the
always-human class is decided **before** the invocation by the profile's own
declared classification, itself authorization-bearing under RFC3-16(a); where
the classification is ambiguous the invocation is human-gated (narrowest
reading, RFC10-7)."

**F8 [Non-blocking] — RFC10-6 lets a completion predicate accept `report-fact`
where RFC2-25 reserves positive status to `gate-backed`.**
`rfcs/RFC-0010-mission-control-autonomy.md:146-152` vs.
`rfcs/RFC-0002/rendering-vocabularies.md:156` and RFC1-19
(`RFC-0001…:355-357`). No clause states that "mission completed" is not a
status claim; render-time tier disclosure is a mitigation, not the bar.
*Minimal fix:* either (a) add to RFC10-6 — "A mission's `completed` state is a
status claim under RFC1-19; a predicate accepting less than `gate-backed`
renders completion at the achieved tier and **never green**" — or (b) state
explicitly that mission completion is an execution-plane fact outside RFC2-25's
positive-status set. Option (a) is the conservative one.

**F9 [Non-blocking] — Two live stale act-digest copies that CG-7d cannot see.**
`candidates/round-2026-08/ARTIFACT-INVENTORY.md:14` ("act-1 subject at manifest
`5c4d6798…`"; current `f2914fc5…`) and `:23` ("(`89279260…`, act-3)"; current
`7a3b2249…`), both unmarked, in a table whose act-2 cell (line 13) *is*
current. CG-7d's `ACT_SUBJECTS` regexes (`scripts/check_governance.py:607-624`)
require the act phrase and a full 64-hex digest on the same line, so truncated
phrase-less copies are structurally invisible. This is the hazard `AGENTS.md`
names ("A derived value quoted for convenience is a promise") surviving the
round that built CG-7d.
*Minimal fix:* mark both lines retired (a `stale`/`retired` word within 60
characters before the digest satisfies CG-7d's existing carve-out), **and**
extend CG-7d with a second pass that flags any 8-63-hex fragment which is a
prefix of no current act subject and carries no retirement marker.

**F10 [Non-blocking] — Self-declared status stamps outside the RFC corpus do
not use RFC3-16(c)'s render vocabulary, and the adopted doctrine has no
recorded content digest.** `doctrine/README.md:3` ("Adopted project doctrine"),
nine craft banners at `policies/craft-and-care/*.md:1` ("**Approved**"),
`INSTALL-RECORD.md:17`, `PROJECT-STATUS.md:20-22` ("✅ **Adopted**"). None
claims "verified", so RFC3-16(c)'s hard prohibition
(`governance-homes-and-owner-acts.md:341-345`) holds; the softer obligation at
lines 346-348 does not. Separately: no tracked artifact records a content
digest for any file under `doctrine/`, so the doctrine's state-(1) record does
not satisfy RFC3-16(c)'s own shape (line 322-325, "the **exact content
digest**"), and the only stamp lives in a sibling README not bound to the five
doctrine files.
*Minimal fix:* (a) append "(bootstrap, uncorrelated — not independently
verified; RFC3-16(c))" to the four stamp sites; (b) add a scripted
`DOCTRINE-DIGESTS.txt` next to `doctrine/README.md` recording the five files'
sha256 as of the `doctrine-adopted-2026-07-30` tag, and cite it from line 3.

**F11 [Non-blocking] — RFC4-21 permits a labelled Inferred value inside an
Evidence-class snapshot input, with no clause protecting the label through
aggregation.** `rfcs/RFC-0004/execution-record.md:130-133` (rate-derived cost is
Inferred) against RFC4-18's Evidence classification (lines 66-69) and RFC2-1
item 6 (`snapshot-and-evaluation-core.md:84-85`). The seam rule forbidding
Inferred material is written for observation records only (RFC2-6 line 163).
`reduced-fidelity` has label-survival protection (violation case 11,
`fidelity-joins-and-mappings.md:190-191`); Inferred cost has none.
*Minimal fix:* append to RFC4-21 — "An Inferred field inside an Evidence
artifact carries its label into every claim, aggregate, and render derived from
it; dropping the label in aggregation is a violation, on the same rule as
RFC4-24's fidelity labels. No Inferred field may contribute to a figure
rendered at an Observed label."

**F12 [Non-blocking] — The pre-A1 total-blockage consequence is disclosed in
the decisions record but not in the acceptance record's owner-attention list.**
Owner decision A9 (`decisions/OWNER-ANSWERS-2026-08-01.md:30`) accepts it
knowingly for "every consent, adoption and policy"; the acceptance record
surfaces the hard-precondition framing for **Mission Control only**
(`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:278-285`, §7 item 6). The
composed effect of RFC5-15, RFC5-16 and RFC5-18(c) is that V0 cannot *observe*
either, and a reader of the acceptance record alone would not learn it.
*Minimal fix:* extend §7 item 6's first clause to read "Mission approval,
**every egress, every ingest, and every execution launch** are runtime acts —
V0 consequence", citing A9.

---

*End of RC-8. Findings are numbered for disposition; verdict word is
`EXCEPTIONS` and is to be copied exactly.*
