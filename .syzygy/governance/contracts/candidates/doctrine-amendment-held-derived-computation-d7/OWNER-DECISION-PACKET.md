# Doctrine amendment packet — D7 (proposed): held derived computation delegates no decision

**Status: DRAFT — not applied, not adopted; binds nothing.** Doctrine
amendment is an owner act (VIS-4). An agent session drafted this packet on
2026-10-03 for `syzygy-u05.14` (vision pursuit 2026-09-22, move N14,
"packet A, the molding half"). The packet edits no doctrine byte, opens no
gate, authorizes no implementation, installs nothing and runs nothing. A
commit, a merged pull request, a review, a closed bead or silence performs
nothing; only the owner's own words in the owner's own session do.

**Review status (2026-10-03).** One fresh-context round returned `REVISE`
(`docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md` line 4) over the bytes at
`fc46ec4`: six revise-level findings and eleven notes. Each was repaired
once, recorded in `ROUND-1-DISPOSITIONS.md` (this directory). Under the
stopping rule set before the round, no round 2 was dispatched: **these
repaired bytes are unconfirmed**, and the owner decides on them as such.

**Identifier.** `D7` is the next unused number in
`../../../decisions/DOCTRINE-AMENDMENT-LOG.md` as of 2026-10-03 [Observed:
the log holds D1, D5 and D6; D3 is the candidate bounded-mission packet in
the parent directory, `contracts/candidates/`, and D4 is the ruling
`../../../decisions/D4-RULING-DECISION.md`]. The number is provisional: if
another doctrine packet is adopted first and takes D7, this one takes the
next free number on adoption. The `D1`–`D8` labels in
`docs/plans/2026-10-03-smooth-example-roadmap.md` are that page's own
decision labels and are unrelated.

**Companions in this directory.** `SEMANTIC-DELTA.md` (the delta in the
template's form), `IMPACT-LEDGER.md` (the blast-radius sweeps with their
predicates and denominators), `REVIEW-BRIEF.md` (the round-1 brief),
`ROUND-1-DISPOSITIONS.md` (each finding and its repair).

---

## 0. The question in one paragraph

The owner's north-star sentence says the rest of a project "will
(eventually) mold itself to fit around that goal" (`vision.md`, "What
changes for the owner"). Doctrine today gives that half no lawful
mechanism: "**Not autonomous.** The loop is human-triggered" (`vision.md`)
and "someone specs a desired shape, then deliberately triggers a
propagate/sync pass" (`architecture.md`) admit only a computation the
owner explicitly asked for, and the owner's P-69 ruling adds "No timer or
background poller on any arm". So every move that wants Syzygy to notice a
change on its own — re-observing after the owner merges, rehearsing a
regeneration, keeping a "what changed" band current — has to argue the
boundary again inside its own slice [Observed: pursuit findings L11-F1 and
L11-F8, `docs/pursuits/2026-09-22-vision-pursuit-data.json`]. This packet
offers to name the boundary once, at the smallest width the pursuit could
find: a closed class of **held derived computation** that may run on a
human act that did not ask for it, and may never run on a clock or watcher
Syzygy owns.

**What it does not do on its own, stated up front.** Accepted contract
RFC2 requires every evaluation that captures a merge fact to run inside a
deliberately triggered pass (section 4). D7 relaxes no contract, so until
RFC2 is separately amended, an unprompted re-observation of a repository
whose history carries a merge — which is most of them — stays unlawful even
after D7. D7 names the boundary; it does not by itself make the pursuit's
headline example run.

**Departure from the pursuit's wording, disclosed.** N14 asked for "one
amendment to VIS-4 and the 'Not autonomous' clause". This packet leaves
every byte of VIS-4 unchanged and amends the "Not autonomous" bullet and
the loop paragraph instead. Reason: VIS-4 governs who adopts shape; the
question here is what a trigger is, and the two passages that define the
trigger are the bullet and the loop paragraph. The new text cites VIS-4's
bounds rather than editing them [Inferred: the drafter's judgment].

## 1. What it amends

Two insertions. No rule is renumbered, retired or reworded; VIS-1 through
VIS-7 and SEC-1 through SEC-5 keep every current byte. Both anchors were
read on 2026-10-03 at the hashes given.

**Order of rulings.** Section 1's text states a reason for its
classification ("delegates no decision, and is for that reason inside
VIS-4's stated bounds"), in the reason-stating style the owner designated
for D3 when ruling P-24 (`decisions/D4-RULING-DECISION.md`). It is lawful
text **only after** the owner rules Q1 "inside". On "beyond", the heading
sentence would be false doctrine and section 1 may not be applied (Q1).

### 1.1 `vision.md` — "What Syzygy is not", the "Not autonomous" bullet

**Anchor (exact current text, `.syzygy/governance/doctrine/vision.md`
lines 105–107 at sha256
`93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d`):**

> - **Not autonomous.** The loop is human-triggered; autonomy beyond VIS-4's
>   stated bounds is licensed only through the mechanism VIS-4 names, never by
>   reinterpretation.

**Insertion point:** after the last line of that bullet (line 107 at the
hash above), as three sub-bullets of it, before the blank line that
precedes `## Non-negotiable rules`.

**Text to insert, verbatim (these exact bytes; two-space indent, matching
the sub-bullets of "Not an enforcement engine — outward"):**

```markdown
  - **Held derived computation delegates no decision, and is for that reason
    inside VIS-4's stated bounds rather than an exception to them.** Without a
    fresh request, Syzygy may observe, compute the difference from its last
    identified evaluation, stage a draft, and hold the result — nothing more —
    when the trigger is a human act, or a hook a human installed by hand that
    fires only on a human act.
  - **A clock or watcher Syzygy owns is never a trigger:** no timer, schedule,
    poller, file or event watcher, or wake Syzygy sets for itself.
  - **Unprompted, Syzygy never notifies anyone, dispatches or reprioritizes
    work, adopts, or sets its own next trigger.** A held result waits until a
    human next looks. It is a new identified evaluation of observed state, or
    data rebuildable from its inputs (VIS-6), and never model output; staging
    commits nothing to any governed tree; and it opens no read, write, egress,
    or execution path that is not separately authorized (VIS-5, SEC-2, SEC-3).
```

### 1.2 `architecture.md` — "Snapshots and the loop", the loop paragraph

**Anchor (exact current text, `.syzygy/governance/doctrine/architecture.md`
lines 329–334 at sha256
`d1987f7f630b82eee359e14e89e6422ab74374a2578c218f73d47c80eefcb565`):**

> **The loop:** intent → observation → gaps → reviewed work → fleet execution →
> verification. It has one upward arrow: verification and runtime evidence may
> open spec-indictment gaps that route to the owner. The loop is
> **human-triggered**: someone specs a desired shape, then deliberately triggers
> a propagate/sync pass. Work-to-code and code-to-deployment belong to the
> orchestration toolchain, outside Syzygy's body.

**Insertion point:** at the end of that paragraph, after "outside Syzygy's
body." and before the blank line that precedes the Mermaid block. This is
deliberately **not** the point candidate D3 inserts at (§1.3).

**Resulting paragraph, exactly (these are the bytes to apply; the first
five lines are unchanged and the sixth line is extended):**

```markdown
**The loop:** intent → observation → gaps → reviewed work → fleet execution →
verification. It has one upward arrow: verification and runtime evidence may
open spec-indictment gaps that route to the owner. The loop is
**human-triggered**: someone specs a desired shape, then deliberately triggers
a propagate/sync pass. Work-to-code and code-to-deployment belong to the
orchestration toolchain, outside Syzygy's body. Held derived computation —
observe, compute the difference, stage, hold — may run outside a deliberate
pass only on the trigger `vision.md` states under "Not autonomous"; it
dispatches no work, adopts nothing, and relaxes no contract that requires a
deliberately triggered pass.
```

### 1.3 Composition with candidate D3 (bounded mission)

Candidate D3 rev1 (`../DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`, not
adopted as of 2026-10-03) touches both passages [Observed, read
2026-10-03]:

- **`architecture.md`:** D3 inserts after "…triggers a propagate/sync
  pass." and before "Work-to-code…"; D7 extends the paragraph after
  "…outside Syzygy's body." Different bytes, so they compose in either
  order, but whichever lands second sees a changed paragraph and therefore
  a changed anchor.
- **`vision.md`:** the text an act 5 would carry is not D3 rev1's §1.2
  parenthetical but the reviewer's reason-stating wording in D3 §6, which
  the owner designated when ruling P-24 (`decisions/D4-RULING-DECISION.md`:
  "the reviewer's reason-stating §1.2 wording is designated as the text act
  5 would carry"). That wording rewrites the bullet into separate sentences;
  D7 appends sub-bullets after the bullet's last line. Different bytes
  again, but the same bullet: if D3 lands first, the bullet's text and line
  numbers change.
- **Rule for the second adoption:** D7's insertion points are defined by
  position — "after the last line of the 'Not autonomous' bullet" and "at
  the end of the loop paragraph" — not by line number. If either anchor's
  bytes have moved since the sha256 above, applying D7 is still a
  mechanical append at the same position, but the changed anchor is a
  changed review subject: re-anchor through a fresh review (rule 10), never
  by applying judgment at the keyboard.
- **Meaning:** D3 governs passes and missions of the loop, each a
  deliberate human act. D7's class runs outside a deliberate pass and
  relaxes no contract that requires one, so the two do not compete
  [Inferred]. D3's own anchors predate the D5/D6 restyles (it quotes
  `vision.md` lines 72–74 at an older digest); that is D3's re-anchoring
  question and is not changed here.

## 2. The trigger test, the permitted list and the prohibitions

Stated here for review; section 1 is the text that would bind, and every
row below is meant to say what section 1 says, no more and no less.

| Element | Lawful | Unlawful |
|---|---|---|
| **Trigger** | a human act the computation was not itself requested by (a commit, opening a page, recording a security act); a hook a human installed by hand that fires only on a human act | a timer, schedule, poller, or file or event watcher Syzygy sets; any wake Syzygy sets for itself; a hook that also fires on agent or machine acts (Q3) |
| **Effects** | observe; compute the difference from the last identified evaluation; stage a draft; hold the result | notify anyone — any message, alert or interrupting badge pushed to a human; dispatch or reprioritize work; adopt, approve, sign or label accepted; set its own next trigger |
| **Where the result lives** | a new identified evaluation of observed state (RFC2's evaluation rules), or derived data in Syzygy's own state that is rebuildable from its inputs (VIS-6), shown when a human next looks | model output in any form; any commit to `openspec/**` or `.syzygy/**` (a commit stays a separately authorized effect); any write outside the two roots (VIS-5); a fact living only inside Syzygy that is neither rebuildable nor an evaluation of observed state (VIS-6) |
| **Paths it opens** | none | any read beyond what consent and the acts in force already admit; any write; egress (SEC-2); execution of observed code (SEC-3) — each stays under its own authorization |
| **Contracts** | — | relaxes none: any computation an accepted contract confines to a deliberately triggered pass stays confined (RFC2, section 4) |

**What "unprompted" means here.** A computation is unprompted when the human
act that triggered it was not a request for that computation. Opening the
page is a request to see the page; under D7 Syzygy may, on that act, also
compute and hold — but only what no contract confines to a deliberate pass.
Today that excludes re-observing a repository whose history carries a merge
(section 4). Clicking a re-observe route is a request and was never in
question.

## 3. Non-expansion: each permitted effect against the ruling that already allows it narrowly

Each row names the nearest precedent and states plainly what D7 adds. D7
is **Normative** (`SEMANTIC-DELTA.md`): the precedents license each
*effect* when requested; D7 adds the *trigger*, and in two rows also a
persistence the precedent did not have. It adds no new effect.

| Permitted effect | Nearest narrow licence | What D7 adds |
|---|---|---|
| **Observe** on a human act that did not ask for it | **RFC5-11** (accepted contract, owner decision B4): "Recording a revocation **triggers a new identified evaluation** rather than waiting for the next human-triggered one" (`contracts/rfcs/RFC-0005/admission-and-boundary.md` lines 320–323). A human security act already triggers an evaluation nobody requested. | Any human act, or a qualifying hook, may trigger it — not only revocation — subject to RFC2 (section 4). |
| **Compute the difference** from the last identified evaluation | **P-79 Q6** (ruled A, 2026-09-21): "the delta is a claim of the current evaluation about two evaluations, carrying both identities, never a freshness value"; the retention direction of 2026-09-23 (`decisions/POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md`) lets the retained record exist. | The difference may be computed on the trigger above instead of on request. Its form is unchanged: a claim of a new evaluation, never a freshness value (RFC2-10). |
| **Stage a draft** | **P-71 Q3**, arm (b) (ruled A, 2026-09-21): "a pure drafter that writes no file"; the M4 funnel's arm text: "the drafter is pure and emits packet *data* on request, writing no file at all; an operator command renders it". VIS-4: agents "may draft them, never adopt them". | The pure drafter's output may be computed without the request **and held** until a human next looks. Arm (b) wrote no file at all; D7's staged draft persists in Syzygy's own state. That persistence is **wider than arm (b)** and rests on VIS-6's projection rule (next row), not on P-71. D7 still commits nothing to any governed tree, so it does not reach arm (a)'s narrow-act effect. |
| **Hold** the result in Syzygy's own state | **VIS-6**'s general rule: "Syzygy's databases and views are projections". P-79 Q4 (ruled A) is a precedent for *where* such state lives — "in the daemon's own state directory, never in an observed repository" — not a licence: what it licenses is the owner's own unpromoted note under VIS-6(a). | The footing is VIS-6's projection rule: a held result must be rebuildable from its inputs, or be an identified evaluation of observed state. D7 does **not** stretch VIS-6(a), which stays the owner's own presentation state, and holds no model output. |

**The prohibitions against current rulings.** Every prohibited effect is
already prohibited or gated today; D7 restates them so that the new trigger
cannot be read as licensing them: notification has no licence anywhere
[Observed: sweep in `IMPACT-LEDGER.md` §2]; dispatch is "human-triggered"
(`THREE-SURFACE-POC-MODE-DIRECTION.md` line 31, `v1.md` "Human-triggered
propagation at full breadth"); adoption is VIS-4; a clock or watcher
trigger is P-69's "No timer or background poller on any arm", the M2
funnel's Q4 arm (b) ("a timer, poll or file watcher inside the daemon",
unauthorized), and RFC4-16's "never an autonomous trigger"
(`contracts/rfcs/RFC-0004/named-adapters.md` lines 432–435).

## 4. Blast radius over P-69 and the other trigger rulings

Full sweeps, predicates and denominators: `IMPACT-LEDGER.md`. The rulings
and clauses that bear on the trigger, each with its outcome under D7:

| Ruling or clause | Text (quoted) | Under D7 |
|---|---|---|
| **P-69** (ruled B, 2026-09-21) | "No timer or background poller on any arm." M2 funnel Q4's ground: "No act found that authorizes a background poller … the 2026-09-02 authorization's 'any scope beyond the signed change' trigger is the hook" | **Unchanged, and now doctrine-backed.** D7's "a clock or watcher Syzygy owns is never a trigger" is P-69's rule stated generally. D7 does not make anything lawful under the 2026-09-02 act; that act's scope still governs new daemon behaviour. |
| **RFC2-19** (accepted contract) | "reconciliation evaluations run inside a deliberately triggered propagate/sync or observation pass, never autonomously on merge events" (`contracts/rfcs/RFC-0002/reconciliation-chain.md` lines 245–247) | **Stays stricter than D7, and binds every D7 trigger, not only the hook.** See the next row. |
| **RFC2 merge chain** (accepted contract, same module) | "**reconciliation-pending** attaches automatically and deterministically at the first evaluation that captures the merge fact (inside RFC2-19's deliberately triggered passes — never on a live merge event)" (`reconciliation-chain.md` lines 155–157) | **Binds D7's headline example.** By section 2's own definition an unprompted computation is not a deliberately triggered pass, so an unprompted evaluation that captures a merge fact contradicts this clause, whether its trigger is a page open or a hook. D7 says it "relaxes no contract that requires a deliberately triggered pass", so under arm A alone such evaluations stay unlawful. Making them lawful needs an RFC2 amendment (a contract act) or an explicit owner ruling on these two clauses, **in addition to** D7. [Inferred: reading of the clauses; a contradiction surfaced, not reconciled.] |
| **RFC4-16** inter-pass interval (accepted contract) | "the loop stays human-triggered (architecture.md), so the contract binds the declaration and the honest rendering when the declared interval was exceeded, never an autonomous trigger" | Unchanged: D7 admits no clock trigger. |
| **RFC5-11** (accepted contract) | quoted in §3 | Unchanged; it is D7's precedent. |
| **P-71 Q3, P-71-Q5** (ruled A, 2026-09-21) | Q3 arm (b) quoted in §3; Q5 "the return path's write into Butlers is foreclosed by the 2026-09-02 act" | Unchanged. D7 writes nothing into any repository. |
| **P-79 Q4, Q6** (ruled A, 2026-09-21) | quoted in §3 | Unchanged. |
| **Bounded-mission interpretation act** (2026-08-31) | "The approval is the human-trigger required by the doctrine; bounded execution inside that approved envelope is not autonomous vision steering." | Unchanged and orthogonal: missions execute inside an approved envelope; D7 holds and executes nothing. |
| **"Autonomous behavior" exclusions in acts in force** (10 files; `IMPACT-LEDGER.md` §1b) | e.g. `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` lines 134–135: "No production release, broad remote access, multi-user support, or autonomous behavior." | Not falsified, but **narrowed in reach**: by naming a class that "delegates no decision", D7 would let a reader argue that held derived computation is not "autonomous behavior" under those exclusions. The guard is that each of those acts also confines new behaviour to its signed scope, so D7 by itself authorizes no implementation under any of them; any D7 behaviour still needs its own implementation authority. |
| **Trusted-bootstrap observation direction** | "This relaxation applies only to read-only repository observation. It does not relax or authorize: - writes to Butlers or any other observed repository; … - autonomous owner acts" | Unchanged. Installing a hook in an observed checkout is a write there; D7 does not authorize it (section 6). |

## 5. Entry criteria for the live fleet observability mandate

`vision.md` ("Eventual mandate: live fleet observability") binds every
roadmap to carry the mandate "with stated entry criteria", and `v1.md`'s
deferral row (line 103; the pursuit's citation `v1.md:82` predates the D6
restyle) says the mandate "keeps it named and sequenced, with entry
criteria, on every roadmap" without naming one [Observed, 2026-10-03].
Because the doctrine places the criteria **on the roadmap**, this packet
does not propose doctrine text for them; it offers them for the owner to
place on a roadmap (Q4). They hold whichever arm the owner takes.

| # | Entry criterion | Why it gates | Test |
|---|---|---|---|
| E1 | A re-observation verb exists: a human can obtain a new identified evaluation without restarting the daemon | Live views annotate observed truth; a truth that only refreshes on restart cannot be annotated live (L11-F1) | a human-triggered route yields a new evaluation identity and names the one it supersedes |
| E2 | The evaluation identity separates observed-project movement from observer movement | A live viewer must tell "the project moved" from "Syzygy moved" (L4-F2) | the two staleness limbs render as separate claims |
| E3 | *Withdrawn in the round-1 repair.* It read "the trigger boundary is on record". A human opening a live view requests what it shows, so watching fleets live needs no unprompted computation and no ruling on this packet. | — | — |
| E4 | Streamed process output can be captured as a durable, identified artifact | The mandate's own evidence rule: streamed output "is Observed only once captured as a durable, identified artifact" | a captured stream has an identity and digest, and is cited by one claim |
| E5 | No live view contributes to a status claim | The mandate's rule: "live views never contribute to status claims" | a parity or mutation check fails when a live-only value reaches a claim |
| E6 | At least one project's shape is observed with Observed claims at a named evaluation | v1.md's stated reason for waiting: "Meaningless without the observed truth it would annotate" | a retained evaluation record names the project, the evaluation and its Observed count |

E3 keeps its number so that no criterion is renumbered. Sequencing (where
on the roadmap) stays the owner's; the criteria above do not order
themselves.

## 6. What adoption would **not** make lawful

Each item below stays outside D7 and needs its own owner step. Nothing here
is run, installed or written by this packet.

1. **Unprompted re-observation of a repository whose history carries a
   merge** — RFC2 (section 4). Needs an RFC2 amendment or an owner ruling
   on those clauses, plus implementation authority for the daemon
   behaviour.
2. **The Butlers-side push trigger (for N2, `syzygy-u05.2`).** A hook in the
   owner's Butlers checkout that calls a loopback re-observe route. Owner
   option only. Before it could run, all of these would be needed, in
   addition to D7:
   - an owner act naming the write, because installing a file under the
     checkout's hooks directory is a write to an observed repository, which
     the trusted-bootstrap observation direction does not authorize and
     P-71-Q5 treats as foreclosed by the 2026-09-02 act;
   - item 1's RFC2 amendment or ruling;
   - an owner ruling that publishing the hook's text is a VIS-5 *proposal*
     artifact rather than materialized implementation code (pursuit move
     L4-M4 names this as a stretch of VIS-5);
   - a SEC-1 machine-client credential for the call, held under SEC-5 (no
     secret in the hook text or the observed repository);
   - a showing that the hook fires **only on a human act** (Q3): git hooks
     in a checkout are shared by every worktree of that repository, so a
     hook in a checkout agents also commit to fires on agent acts and fails
     D7's test.
   The cheaper answer the pursuit itself recorded stays available with no
   amendment: the human-triggered re-observe route N2 already designs.
3. **A regeneration rehearsal** (re-run generation against the current
   corpus, compute the difference from the last adopted output, hold).
   Packet obligation only, for the feature-request funnel after adoption:
   - generation through a model provider is egress; D7 opens none, so the
     rehearsal's provider step stays under SEC-2 and the generator act in
     force, and runs only when that act's consent covers it;
   - D7's held result may never be model output, so a generated draft may
     not be held as Syzygy-only state at all: it must be committed out by a
     separately authorized effect, or only its deterministic parts (input
     corpus digest, difference from the adopted output's inputs) may be
     held;
   - the variant in pursuit move L10-M6 (a fixed question set scored
     against the extracted shape, no provider call) has no egress and fits
     D7 as written once its question set is owner-authored (VIS-4), subject
     to item 1 if it re-observes.
4. **Any timer, poller, watcher or scheduled cadence** — P-69 and D7 both
   forbid it.
5. **Any notification** — forbidden by D7; a future notifying surface needs
   its own doctrine amendment.
6. **Autonomous spec adoption** — VIS-4's mechanism, untouched.

## 7. Why this is not self-licensing under VIS-4 (the D4 question)

VIS-4's two-part mechanism (an accepted adjudication RFC plus the owner's
doctrine amendment) governs "autonomy beyond VIS-4's stated bounds". D3's
packet reads that phrase as delegation of an always-human decision class
(`../DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` lines 37–39), and the owner
ruled on that reading for bounded missions only, finding them inside the
bounds (P-24, `decisions/D4-RULING-DECISION.md`). Held derived computation
delegates no decision: it adopts, approves, dispatches and notifies
nothing, and every result waits for a human.

**This packet's position, which the owner may overrule (Q1):** D7 is a
**Normative** change — it adds a trigger the current text does not admit —
and the class it adds delegates no decision, so it sits **inside** VIS-4's
stated bounds. "Inside the bounds" answers only whether VIS-4's
autonomy-beyond-bounds mechanism is needed; it does not make the change
Clarifying. So a doctrine amendment alone (this packet, an owner act)
suffices, and section 1's text says why in its own words.

**If the owner rules "beyond":** VIS-4's own terms apply — such autonomy
"is licensed only through the mechanism VIS-4 names, never by
reinterpretation". Arm A then needs an accepted adjudication RFC first and
its text must be redrafted, because the heading sentence would be false.
Arm B is unavailable outright, since it is an interpretation and not the
named mechanism. Whether any adjudication RFC could serve: VIS-4 defines
that RFC for the spec-adoption gate ("what makes adversarial judgment
independent, how the ambiguity determination is recorded, and how each
adopted change stays individually revertable"), so whether such an RFC can
answer a trigger question at all is itself **[Unknown]** and would be the
first thing to rule.

## 8. The owner's questions

Four questions, to be answered in this order. "Recommended" is this
packet's view and binds nothing.

**Q1 — Inside or beyond VIS-4's stated bounds?** *Recommended:* inside
(section 7). "Inside" makes arms A, B and C all available. "Beyond" leaves
arm A only after an accepted adjudication RFC and a redraft, removes arm B,
and leaves arm C.

**Q2 — Which arm?**

- **A — Adopt D7 as drafted** (both insertions, section 1), after Q1
  "inside". *Recommended:* the pursuit's point is that the boundary should
  be stated once, in doctrine, where every later slice can cite it; and the
  change is Normative, which is what an amendment is for.
- **B — Rule by interpretation, no doctrine byte.** A dated owner act in the
  shape of `decisions/BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md`
  (2026-08-31), recording that existing doctrine already admits the section
  2 class. **Choosing B is the owner ruling the change Clarifying, contrary
  to this packet's classification**: an interpretation records what the
  text already means, and the packet's position is that today's text does
  not admit the class. If the packet is right, B records as existing
  meaning something the text does not contain — the "reinterpretation" the
  bullet forbids. B is offered because the classification is the owner's
  to make, not the drafter's, and the owner has taken the interpretation
  route before; this packet recommends against it. Cheaper and reversible;
  leaves `vision.md` silent, so a reader of the doctrine alone cannot find
  the boundary.
- **C — No change (decline).** Lawful, and nothing breaks today.
  Consequences, stated plainly: every unprompted computation stays
  unlawful; re-observation stays a request (N2's route, which needs no
  amendment); the hook trigger stays unavailable on every path; the
  regeneration rehearsal runs only on request; each later cadence slice
  keeps arguing the boundary in its own packet; the molding half of the
  north star keeps no named mechanism. The entry criteria (Q4) do not
  depend on this packet and can still be placed on a roadmap.

**Q3 — How strict is the hook test?**

- **Strict** (as drafted): the hook must fire only on a human act.
  *Recommended:* it is what the pursuit asked for and the only reading that
  keeps "human act" true of every trigger.
- **Installation authorizes:** a hand-installed hook is a sufficient human
  act whatever event fires it. Wider; would let agent commits trigger held
  computation in a shared checkout. Choosing it changes "fires only on a
  human act" to "fires on events in a checkout the human chose", and the
  text would need a redraft and a fresh review.

**Q4 — Where do the entry criteria live?** *Recommended:* on the roadmap,
as section 5 offers them, because doctrine says each roadmap carries them.
The alternative is a sentence in `v1.md`'s deferral row naming them, which
would be a second doctrine edit and is not drafted here.

## 9. How adoption would be recorded

Doctrine amendments carry no magic phrase (D3, D5 and D6 precedent). If the
owner rules Q1 "inside" and adopts arm A, in the owner's own words:

1. apply section 1's two insertions as the exact bytes shown, checking each
   anchor against the sha256 above first — if either file has moved, stop
   and re-anchor through a fresh review rather than applying by judgment;
2. add one row `D7` to `../../../decisions/DOCTRINE-AMENDMENT-LOG.md` with
   the owner's words and a link to this packet;
3. regenerate the derived indexes the ledger names (`IMPACT-LEDGER.md` §4)
   and run the canonical battery; nothing else is propagated.

Arm B is recorded as its own decision file; arm C as one register row
closing P-101 with the decline. No arm edits this packet.
