# RB-2 — Vision and doctrine review (raw reviewer output, stored verbatim)

## Provenance

- **Review vertical:** RB-2 — vision and doctrine (human-clarity refactor round, 2026-08-05).
- **Reviewer:** fresh-context agent session. Inputs were the charge and the
  clone-visible repository only; **no authoring conversation, no `_bootstrap/**`,
  and nothing under `round-2026-08/` except `SEMANTIC-DELTAS-THIS-ROUND.md`**
  (which the charge assigns) and this output file.
- **Worktree state:** branch `main`, HEAD `9e6f2f7`; `.syzygy/governance/contracts/`,
  `.syzygy/map/`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`, `SECURITY.md`,
  `scripts/`, `.github/` untracked; `.syzygy/governance/doctrine/README.md` modified.
- **Artifacts read in full:** `.syzygy/governance/doctrine/{README,vision,v1,architecture,trust-and-evidence,security}.md`;
  `README.md`; `.syzygy/intent/OVERVIEW.md`; `SECURITY.md`; `PROJECT-STATUS.md`;
  `CONTRIBUTING.md`; `AGENTS.md`; `round-2026-08/SEMANTIC-DELTAS-THIS-ROUND.md`;
  `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-{DRAFT,D3}.md`.
- **Commands run (all read-only):** `git diff HEAD -- .syzygy/governance/doctrine/`,
  `git status --porcelain`, `git tag --list 'doctrine-*'`, `sha256sum` over the two
  D3-anchored doctrine files and the original draft, `python3 scripts/check_governance.py`,
  and Python `re` term sweeps over the six public-surface files (Python `re`, not
  `grep` — the repository records a ugrep silent-pattern hazard).
- **Epistemic labels:** claims below are `[Observed]` where a command or a quoted
  line is the evidence, `[Inferred]` where they rest on my reading, `[Unknown]`
  where I could not verify inside the charge's read boundary.

---

## Findings

### F1 — `PROJECT-STATUS.md` declares "no known blocking defects" while the check it names as its own verification FAILs — a false green on the status surface (**blocking**)

`PROJECT-STATUS.md:50-53` states:

> ## Known blocking defects
>
> None known at this revision.

`PROJECT-STATUS.md:64-69` names `python3 scripts/check_governance.py` as one of the
four commands that verify this page. Running it in this session:

```
FAIL  CG-7b  act-1 argument matches the manifest — 1 argument examined, 1 finding
        .syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md
        offers 08793ddf70f3… but the manifest now hashes to 5c4d67983541…
        — the act would bind a package that no longer exists
```
`[Observed]` — full run: `12 OK, 7 WARN, 1 FAIL (20 checks)`.

The round's own register predicted exactly this consequence: SD-1 records
"**Impact:** invalidates the prior act-1 manifest digest `08793ddf…` → manifest
regenerated; new digest-binding review required"
(`SEMANTIC-DELTAS-THIS-ROUND.md:21-23`). The manifest was regenerated; the
acceptance record's offered argument was not repointed. The condition is
blocking by the acceptance record's own logic — act 1 performed today binds a
digest no artifact has.

This is my vertical, not the contracts vertical, because of what the *page* says.
VIS-2 (`doctrine/vision.md:96-106`) forbids any surface declaring a project clean
"without current evidence" and names as a violation "a stale view silently
green." `PROJECT-STATUS.md` renders a green "None known" over a red check it
itself cites. The as-of stamp does not rescue it: the as-of is 2026-08-05 and the
FAIL is present at that revision.

**Repair:** either repoint the acceptance record to `5c4d6798…` (with the
digest-binding confirming review SD-1 already scheduled) and re-run, or state the
defect in the "Known blocking defects" section. Do not leave the row green.

---

### F2 — `OVERVIEW.md` Layer 3 misstates the mechanism VIS-4 names, and resolves the open D4 question on the owner's behalf (**blocking for act 4**)

`.syzygy/intent/OVERVIEW.md:150-153`:

> The loop stays human-triggered: autonomy beyond doctrine's stated bounds is
> licensed only through the mechanism doctrine names (owner adoption of amendment
> D3 plus the candidate Mission contract), never by reinterpretation.

Cited at `OVERVIEW.md:154` to `vision.md ("Not autonomous"; VIS-4)`.

Three defects compound here.

1. **The mechanism is misnamed.** VIS-4 (`vision.md:124-139`) names one mechanism
   and it is not this one: "an accepted adjudication RFC (defining what makes
   adversarial judgment independent…) *and* the owner's explicit doctrine
   amendment." Doctrine names no D3 and no Mission contract anywhere. The
   parenthetical substitutes a pending amendment plus a candidate contract for the
   text of an adopted rule. `[Observed]`
2. **It pre-decides a question both D3 packets hold open.** The rev1 packet
   (`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md:31-44`) argues at length that a
   bounded mission is *not* autonomy beyond VIS-4's stated bounds — which is
   precisely why a doctrine amendment alone is offered — and states that "if the
   owner instead rules that a bounded mission *is* autonomy beyond VIS-4's stated
   bounds, then VIS-4's own terms apply: an accepted adjudication RFC is **also**
   required, this amendment alone is insufficient." The overview asserts the
   second branch as settled fact. It contradicts the packet it summarizes, on the
   one point that packet flags as the owner's to rule. `[Observed]`
3. **The parenthetical is unmarked.** The overview's own header
   (`OVERVIEW.md:10-11`) promises "Anchors marked *candidate* cite contract
   clauses that bind nothing until owner acceptance." This sentence's anchor line
   does mark RFC10-1…16 and D3 as candidate/proposed — but the *sentence itself*
   states the licensing mechanism in the indicative, inside a paragraph that
   otherwise restates adopted doctrine. `[Inferred]`

Severity: act 4 would bind this file's digest. Adopting a presentation artifact
that misdescribes an adopted non-negotiable rule's own mechanism, while
foreclosing an open owner ruling, is the failure mode VIS-3's fresh-reader test
exists to catch. **Repair:** restate VIS-4's mechanism in VIS-4's terms, and state
the D3/D4 relationship as open — one sentence, e.g. "whether a bounded mission
falls inside or beyond VIS-4's stated bounds is an open owner question (D4); if
beyond, VIS-4's two-part mechanism applies."

---

### F3 — Mission vocabulary is presented as settled in the two most-read sentences of the project (**material**)

Bounded missions are pending on two gates at once — candidate RFC-0010 and
proposed doctrine amendment D3, "neither yet accepted" (`README.md:45-47`).
Both files nonetheless place the concept inside their unqualified thesis:

- `README.md:3-5` — the bolded one-sentence definition of the project: "agent
  fleets do **bounded** work to close the difference."
- `README.md:56` — the core-loop diagram node: `F[Fleet execution<br/>human-approved missions]`.
  Doctrine's loop (`architecture.md:244-249`) is "intent → observation → gaps →
  reviewed work → fleet execution → verification"; "human-approved missions" is
  not in it.
- `OVERVIEW.md:20-22` — Layer 1, the 30-second thesis: "Syzygy explains all three
  — and lets humans **govern bounded missions instead of micromanaging tasks**."
  Layer 1 carries no source anchor at all, so the candidate-marking convention
  never engages. `[Observed]`

Compare doctrine's thesis (`vision.md:16-26`), which has three moving parts — three
states kept distinct, compute and show the difference, harness the existing
actuator toolchain — and no mission concept.

Both files qualify the concept *later* (`README.md:43-47`; `OVERVIEW.md:71-75`),
correctly and well. The defect is placement: the thesis line is the part a reader
retains, and it is the part carrying unadopted vocabulary. In `README.md:3-5` the
fix is one word ("bounded" → nothing, or "reviewed", doctrine's own term at
`architecture.md:244`). In Layer 1 the mission clause should either move to Layer 2,
where it is already properly marked, or carry its pending status inline.

---

### F4 — `SECURITY.md`'s SEC-2 row widens the rule's scope; its SEC-3 row drops one of five mandatory profile properties (**material**)

The table is honestly framed — "this table is a faithful summary, and where they
differ, doctrine wins" (`SECURITY.md:19-20`) — which is the right construction and
lowers, but does not remove, the cost of infidelity in a public posture page.

**SEC-2 (`SECURITY.md:25`), scope drift.** Doctrine (`security.md:33-35`): "absent
consent, **the inferred layer** renders Unknown rather than being computed." The
summary: "Absent consent, **the dependent feature** renders Unknown rather than
being computed." "The inferred layer" is a defined artifact
(`trust-and-evidence.md:69-75`; `architecture.md:238-242`); "the dependent
feature" is an open-ended class. The summary states a broader obligation than the
rule it summarizes. `[Observed]`

**SEC-2, dropped permission.** `security.md:35-36` — "Remote backing dependencies
are permitted under the same consent rule" — has no counterpart in the row. An
implementer reading only the public page would read SEC-2 as more prohibitive
than it is. `[Observed]`

**SEC-3 (`SECURITY.md:26`), dropped requirement.** Doctrine enumerates five
profile properties (`security.md:40-42`): "default-deny, isolated credentials,
declared network access, resource limits, **destructive-operation gates**." The
row reproduces four and omits destructive-operation gates, with no ellipsis — the
parenthetical reads as complete. `[Observed]`

**SEC-1 (`SECURITY.md:24`), dropped qualifiers** (minor, listed here for
completeness): the row omits "and an absent browser Origin header is neither
automatically trusted nor treated as a browser-origin violation"
(`security.md:17-18`) — a *permissive* nuance whose absence leaves an
implementer to guess — and "an unauthenticated network-exposed configuration is
never the default" (`security.md:21-22`). It also narrows "endpoints and UI" to
"Endpoints."

**SEC-5 (`SECURITY.md:28`), added quantifier** (minor): doctrine says
"**Observation applies** a declared secret-detection policy"
(`security.md:54-55`); the row says the policy "applies **at every ingest
boundary**." The universal is probably the intended reading, but it is coined
here, not summarized from doctrine.

SEC-4's row is faithful. `[Observed]`

---

### F5 — `OVERVIEW.md` substitutes candidate vocabulary for a frozen doctrine noun, and its three-state restatement drops "doctrine" and swaps "human-guided" for "human-readable" (**material**)

**Vocabulary.** `architecture.md:285-290` freezes technical nouns "at adoption and
stable for citation," **gap** among them, and defines it at `architecture.md:112-114`
as the intent-vs-observed, work-generating delta. Term sweep across the public
surface (Python `re`):

| File | `gap`/`Gap` | `reconcil*` |
|---|---|---|
| `README.md` | 1 (`gaps · contradictions · Unknowns`, the loop diagram — the frozen sense) | 0 |
| `.syzygy/intent/OVERVIEW.md` | 1 (`renders its gap honestly`, `:142` — **not** the frozen sense) | 9 |

`[Observed]`. So the overview never once uses doctrine's frozen word for the
central object of the loop, and uses candidate vocabulary ("reconciliation work",
"reconciliation chain", "reconciliation-pending") nine times in its place —
including at `OVERVIEW.md:43-45`, where "The computed difference becomes
**reconciliation work**" is anchored to "*vision.md (three-state thesis)*"
alongside `candidate: RFC1-22`. The word "reconciliation" does not appear in
`vision.md`. `[Observed]` The candidate anchor is present and honest; the
doctrine anchor next to it is not, and block-level anchoring makes the two
indistinguishable to a reader. Meanwhile `README.md:56` uses "gaps" — so the two
front-door documents describe the same object in two vocabularies.

**Three-state restatement.** `OVERVIEW.md:37-39`: "**Human-readable**
specifications define **desired state**." Doctrine (`vision.md:19-21`): "**desired
state** lives in **human-guided doctrine and specifications**." Two changes in one
sentence: doctrine is dropped from desired state (leaving specs as its only
carrier — which understates doctrine's own constitutional role and conflicts with
the overview's own typed-authority paragraph at `:91-97`), and *human-guided*
becomes *human-readable*. Those are different properties owned by different rules:
human-guided is VIS-4's governance claim, human-readable is VIS-3's legibility
claim. The substitution silently drops VIS-4 from the thesis sentence.
`README.md:21-24` gets this right ("human-guided doctrine and specifications") —
the overview is the file that drifts. `[Observed]`

---

### F6 — `AGENTS.md` and `PROJECT-STATUS.md` route the owner to the D3 packet the round itself found defective, and never mention the revision exists (**material**)

- `PROJECT-STATUS.md:27`, gate 8, owning record: `…/DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`
- `AGENTS.md:48`, act 5, digest source: `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`

Neither surface names `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`. `[Observed]`

That file exists in the same directory and states that the draft it replaces
carries three defects, one of which is that the draft's `vision.md` adoption
instruction **cannot be applied as written**: inserting the parenthetical "after
'The loop is human-triggered;'" strands it between a semicolon and the clause
that follows, joined by no punctuation
(`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md:149`). An owner following
`PROJECT-STATUS.md` to gate 8 today reaches the version whose adoption mechanics
require an unrecorded editorial judgment inside an owner act.

Keeping the original untouched at the gate is correct (it is digest-referenced at
`…-D3.md:6`, and the owner may prefer it). Routing to it *exclusively*, with no
signal that a revision was offered, is not. **Repair:** both rows should name both
packets and say the rev1 exists.

---

### F7 — The rev1 D3 packet — a proposed doctrine amendment authored this round — has no entry in the semantic-delta register (**material**)

`SEMANTIC-DELTAS-THIS-ROUND.md:2-3` claims completeness: "**Every** normative or
authority-adjacent edit this round travels as a recorded delta." SD-1…SD-7 cover
RFC-0003, topology README, nine craft banners, INSTALL-RECORD, the FD-037
extraction and three repoints, the five front-door documents, and the
candidate-package relocation. None covers `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`.
`[Observed]`

The packet is authored this round — it cites `round-2026-08/MISSION-CONTROL-REVIEW.md`
§5.3 as the source of its three repairs (`…-D3.md:12-14`) — and it is a proposed
amendment to adopted doctrine, i.e. the most authority-adjacent artifact class the
register could contain. SD-6 sets the precedent that *new* files get deltas
(PROJECT-STATUS, CONTRIBUTING, SECURITY are new). `[Inferred]` that this is an
omission rather than a deliberate exclusion; either way the register's completeness
claim is currently false as written, and the register is the artifact the round's
review battery is charged with checking against.

---

### F8 — The regeneration north star and the live-fleet-observability mandate are absent from the entire public surface (**material**)

Term sweep over `README.md`, `SECURITY.md`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`,
`.syzygy/intent/OVERVIEW.md` (Python `re`): `[Observed]`

- `Genome` / `genome` — **0 occurrences across all five files.**
- `north star` — **0.**
- `fleet observability` — **0.**
- `regenerat` — 2, both non-load-bearing: `README.md:109` ("No claim of …
  regeneration capability is made anywhere") and `PROJECT-STATUS.md:8`
  ("regenerated or corrected").

Doctrine gives the regeneration ideal a full section titled "The north star
(honestly labeled)" (`vision.md:204-218`), and it is *directional*, not merely
negated: "decisions should nudge projects toward it, and a decision that
materially forecloses it must record that foreclosure — the unrecorded
foreclosure is the violation." The Project Genome is the corpus that ideal acts
on (`architecture.md:122-156`), and "genome-complete" is one of the three status
claims VIS-2 names by name (`vision.md:96-98`).

The public surface therefore states the *disclaimer* ("no regeneration capability
is claimed") without ever stating the *thing being disclaimed*. `OVERVIEW.md`,
whose subtitle is "what it is, in one reading," contains no Genome and no north
star at all. A fresh reader completing the whole public surface would not learn
that the regeneration ideal exists, that it exerts direction on decisions, or
that foreclosing it silently is a doctrine violation.

The fleet-observability mandate is the same shape: `vision.md:220-230` requires
that "**every roadmap** must carry it as a named, sequenced item with stated entry
criteria; removing it, or leaving it unsequenced, violates doctrine." No public
document carries a roadmap today, so no roadmap violates the rule `[Inferred]` —
but nothing on the surface preserves the obligation either, and `v1.md:82` files
it under "Deferred, with rationale" with a rationale rather than sequenced entry
criteria. Pre-existing and untouched by this round; recorded so it is not lost
when the first roadmap is drafted.

This finding is an omission, not an infidelity. It is material because the charge's
own definition of the north star has four elements and the public surface carries
two of them clearly (three-state thesis, no-evidence-means-Unknown), one partially
(comprehensible truth — see F10), and one not at all.

---

### F9 — `OVERVIEW.md` announces four things and enumerates a different four (**minor, but it defeats the section's purpose**)

`OVERVIEW.md:61-75`, heading "**One kernel, four experiences**":

> Three project surfaces **and a machine query plane** of equal standing project
> it; none is independently authoritative:

followed by exactly four bullets — Polaris, Trajectory, Orrery, **Mission Control**.
The machine query plane is announced and then never enumerated; the fourth slot is
filled by the one item the same passage says is "**not** a fourth project truth
surface." `[Observed]`

The "equal standing" claim is well grounded — `vision.md:38-42` makes agents a
first-class consumer "from day one" via machine-queryable endpoints, and
`v1.md:34-36` makes those endpoints V0-mandatory. That makes the omission a
drafting slip rather than an overreach, and it costs the overview a genuinely
doctrinal point (two consumers of equal standing) in the sentence meant to deliver
it. `README.md:36-42` has the same "four experiences" framing with no query-plane
sentence, so the two files also disagree about what the fourth thing is.

---

### F10 — Smaller fidelity drifts in restatements (**minor**, grouped)

1. **`README.md:30-31`** — "**Comprehensible truth, never comprehensible fiction**
   (doctrine VIS-1). A simpler presentation is never bought with a less true one."
   VIS-1's name is "Comprehensible truth **first**; never comprehensible fiction"
   (`vision.md:82`), and its operative content is a five-rank ordering — truth and
   observation determinism; comprehension; momentum; breadth and fidelity;
   reproducibility of derived convenience — with "lower ranks are spent before
   higher ones; rank 1 is never spent" (`vision.md:82-88`). The README's gloss
   captures the simplification clause and drops the ordering, which is the part
   that makes VIS-1 decidable in a trade-off. Nothing stated is wrong.
2. **`README.md:26`** — "Scheduled or **merged** work is never treated as proof."
   Doctrine's word is "completed" (`vision.md:23-25`); `OVERVIEW.md:41-44` keeps
   all three ("scheduled, completed, or merged"). Set-swap, not a weakening.
3. **"never zero"** (`README.md:32`, `OVERVIEW.md:24`, `AGENTS.md` epistemic
   discipline) — VIS-2 says "never green"; "never zero" appears nowhere in
   doctrine `[Observed]`. It is a sound entailment of VIS-1's "may never
   substitute a confident state for an Unknown one," it is used consistently in
   all three places, and I would keep it — recorded only because the charge asks
   for word-by-meaning comparison and this is a coined phrase carried inside a
   doctrine citation.
4. **`OVERVIEW.md:98-100`** — "**Conflicts between authorities** surface as
   contradictions." `architecture.md:107-109` defines a contradiction as
   irreconcilable authoritative claims "whether the claims come from different
   typed authorities **or from one**." The overview narrows a frozen term to the
   cross-authority case, and omits its primary consequence — that it "renders the
   affected conclusion Unknown" — which `CONTRIBUTING.md:77-80` does state
   correctly.
5. **`OVERVIEW.md:108-110`** — "**between evaluations** claims can only degrade."
   The charitable reading (from one evaluation to the next) is correct doctrine;
   the literal reading contradicts VIS-2's "the wall clock never silently changes
   a displayed status" (`vision.md:102-104`). The following clause disambiguates,
   so this is a wording risk, not an error. Suggest "**from one evaluation to the
   next**."
6. **`OVERVIEW.md:138-141`** — "Fleet workers are untrusted even inside the
   writable plane," anchored at `:144` to a source list including `SEC-3`. SEC-3
   says *observed-project code* is untrusted (`security.md:39-45`); it says
   nothing about fleet workers. The proposition is candidate-RFC content
   (RFC3-3/RFC5-25, also listed) and is fine; the doctrine anchor beside it is not
   load-bearing for that sentence. This is the general weakness of block-level
   anchoring: a reader cannot tell which of six cited sources backs which of five
   sentences.
7. **`…-D3.md:204-206`, adoption mechanics item 5** — "Re-run the doctrine's
   fresh-reader review **over the amended 'Not autonomous' bullet and loop
   paragraph**." VIS-3's test is over the *artifact* — a reader "who must be able
   to restate **the artifact's** intent and constraints correctly"
   (`vision.md:108-116`) — not over the amended passages. Narrowing the scope of a
   VIS-3 review inside an owner-act instruction is worth one word's repair
   ("over `vision.md` and `architecture.md` as amended").

---

## Charge item 3 — doctrine-cluster integrity this round: **verified clean**

The register (SD-5, `SEMANTIC-DELTAS-THIS-ROUND.md:65-73`) claims only
citation-cell repoints touched doctrine. Verified two ways `[Observed]`:

`git status --porcelain -- .syzygy/governance/doctrine/` returns exactly one line,
`M .syzygy/governance/doctrine/README.md`. The other five doctrine files —
`vision.md`, `v1.md`, `architecture.md`, `trust-and-evidence.md`, `security.md` —
are untouched this round.

`git diff HEAD` on that one file is a single-line replacement at
`doctrine/README.md:9`, inside the D1 row's **Authority** cell only:

```
- … ratifying the packet at `_bootstrap/rfc-phase/DOCTRINE-AMENDMENT-MAP-HISTORICAL.md`; scope made unconditional …
+ … ratifying the packet at `../decisions/DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md` (extracted under FD-037; original authored in the bootstrap record); scope made unconditional …
```

The **What changed** cell, the date, the id, and the "(not owner decision A2)"
disclaimer are byte-identical. The edit repoints a citation from a git-excluded
path to a tracked one and adds a provenance parenthetical. **SD-5's "Editorial —
citation targets only; zero rule text touched" is confirmed for the doctrine
cluster.** The new target `.syzygy/governance/decisions/DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`
exists in the worktree; `git tag --list 'doctrine-*'` returns
`doctrine-adopted-2026-07-30` as AGENTS.md and PROJECT-STATUS.md claim.

**One limit on this verification:** SD-5 also claims the extracted decision files
are "byte-verbatim extractions" of bootstrap originals. Confirming that requires
reading `_bootstrap/**`, which the charge forbids. That claim is **[Unknown]** to
this review and must be confirmed by a reviewer with that access.

**Prose hygiene, both directions** `[Inferred]`: I found no contract detail leaked
into the doctrine cluster. `architecture.md` defers consistently and by name —
"representation … is RFC material" (`:210-211`), "the exact envelope fields"
question is likewise deferred in the D3 rev1, "schemas and deeper organization …
remain RFC material" (`:60-63`), "Bound values are craft/RFC material; the
obligation to declare is not" (`trust-and-evidence.md:23-24`). That last
formulation is the cluster's best hygiene device and it is used repeatedly. The
`.syzygy/` layout block (`architecture.md:41-58`) is the closest call — a literal
directory tree in a constitutional document — but it is load-bearing for VIS-5's
two-namespace rule and the file marks the deeper levels as RFC material
immediately after. Leakage in the other direction (doctrine detail into
presentation) is not a hygiene problem here; the presentation problems are the
*infidelities* recorded in F2–F5 and F10, not excess detail.

---

## Charge item 4 — D3 packets

**Both packets are honestly framed as owner-only** `[Observed]`. Each opens with
"**Status: DRAFT — not applied**" / "not applied, not adopted", cites VIS-4 as the
adopting authority in its first sentence, states plainly that the owner may adopt,
amend, or decline, and confirms act 5 carries no magic phrase. The rev1 goes
further and states the operative consequence of *declining* in plain language
(`…-D3.md:25-29`) — the disclosure most amendment packets omit.

**The insertions are minimal** `[Observed]`. Two sentences amended in place, no
rule renumbered, no rule retired, VIS-1…7 and SEC-1…5 otherwise untouched. I
verified the rev1's anchors against the live files:

| Anchor claimed | Verified |
|---|---|
| `architecture.md` lines 246–248, sha256 `e19d255f…` | ✅ exact — lines 246–248 are the quoted sentence; `sha256sum` matches |
| `vision.md` lines 72–74, sha256 `816ad50c…` | ✅ exact — lines 72–74 are the "Not autonomous." bullet; `sha256sum` matches |
| original draft sha256 `30efb7c5…` (`…-D3.md:6`) | ✅ matches |

Anchoring an amendment to a line range **and** a content digest, then having all
three digests reproduce, is the strongest provenance discipline I saw anywhere in
this round.

**VIS-4 compatibility** `[Inferred]`. The rev1's position — that a bounded mission
clarifies the *trigger grain* of an already-human-triggered loop rather than
opening autonomy beyond VIS-4's bounds — is coherent and correctly hedged: it
labels itself "this packet's position", names the owner's power to overrule, and
states what follows under the other ruling (an accepted adjudication RFC is *also*
required, and RFC-0010 serves only after acceptance **and** explicit designation,
`…-D3.md:38-44`). §4's sequencing analysis (`:160-189`) then does the work the
original draft omitted, including naming its own recommendation as "agent
recommendation, not a ruling." I have no exception to the packet's own reasoning.
The exception is that `OVERVIEW.md` states the *opposite* branch as settled — F2.

**Does the revision change meaning beyond its stated fixes?** No `[Observed]`.
Comparing the two insertion texts clause by clause:

- The doctrine-level *at-minimum* envelope set is preserved one-for-one:
  objective → objective; budgets → "resource and time bounds"; risk limits → risk
  limits; protected surfaces → "the surfaces and change classes it may not touch";
  stop conditions → "stop and completion conditions" (which *adds* completion,
  a strengthening in the safe direction).
- What leaves doctrine is only the original's second half — "tools, required gates
  and reviews, evidence obligations, and the completion predicate" — and the
  removal is non-load-bearing because the final sentence retains "**every gate
  that would otherwise apply** — a mission is authority to proceed inside the
  gates, never authority to skip one," which is the guarantee those items were
  carrying. The stated reason (a mirrored contract field-set creates a second
  normative home that silently diverges) is correct typed-authority reasoning.
- The `vision.md` change 4 — adding the gate-preservation clause to the second
  file — is correctly self-flagged as "**a judgment call, not a repair**" with an
  explicit note that striking it does not weaken the amendment. That is the right
  way to disclose a discretionary addition inside an owner-act artifact.
- `…-D3.md:213` declines to state its own digest, "since any edit to this file
  after a digest is stated would produce an artifact whose act binds a digest it
  no longer has" — consistent with the repository's never-edit-after-the-act rule.

The §3 change table is a complete and accurate account of the differences I found.
My only exceptions to the packets are F6 (routing) and F7 (register), both of which
are defects in artifacts *around* the packets, not in the packets.

---

## Charge item 5 — memorability test (transcript)

**Protocol and its honest limit.** I closed every file and wrote the three
sentences below before reopening `vision.md`. The limit worth recording: I had read
`vision.md` earlier in this same session, so this measures recall over roughly a
dozen intervening documents, not cold recall by a reader who has never seen it. A
genuinely fresh reader would score lower. `[Observed]` that no file was open while
writing; `[Inferred]` that the result approximates the memorability property being
tested.

**Written from memory:**

> 1. Syzygy keeps three states semantically distinct — desired state in
>    human-guided doctrine and specifications, observed state in code, tests, CI
>    and runtime evidence, and execution state in work-scheduler records — computes
>    and shows the difference, and harnesses the existing agent toolchain to close
>    it; showing the truth is the soul of the product.
> 2. Comprehensible truth comes first and never comprehensible fiction:
>    presentation may be simplified, content never; and where there is no
>    evidence the answer is Unknown, never green — judged at an identified
>    evaluation, never by an ambient clock.
> 3. Humans steer the vision and agents shape within it; Syzygy never writes code
>    and writes directly only within `openspec/**` and `.syzygy/**`; and full
>    regeneration of a codebase from its Project Genome is the north star that
>    exerts direction on decisions — explicitly not a present capability.

**Checked against `vision.md`. Divergences:**

| # | What I wrote | What doctrine says | Verdict |
|---|---|---|---|
| 1 | "harnesses the existing **agent** toolchain" | "harnesses the existing **actuator** toolchain" (`:25-26`) | Wrong word, right concept |
| 2 | — | **"an observatory (V0) and harness (proof-of-concept at V0, full at V1)"** (`:16-18`) | **Missed entirely.** The identity statement — what Syzygy *is* — did not survive recall at all |
| 3 | "Comprehensible truth comes first" | Correct, incl. the "first" the README drops (F10.1) | ✅ |
| 4 | — | VIS-1's **ranks 3, 4, 5** — momentum; breadth of scope and fidelity; reproducibility of derived convenience (`:84-88`) | **Missed.** I retained the top two ranks and the never-spend-rank-1 rule, and lost the currency the ordering actually spends |
| 5 | "never green" | "nor turn anything green" (`:97`) | ✅ — and I did *not* reproduce the public surface's "never zero", which is not doctrine (F10.3) |
| 6 | VIS-5 two namespaces, never writes code | `:141-165` | ✅ |
| 7 | Regeneration north star, "not a present capability" | `:204-218` — including "a decision that materially forecloses it must record that foreclosure" | Retained the ideal and its honest label; **lost the recording obligation**, which is the operative part |
| 8 | — | **"Eventual mandate: live fleet observability"** — "not complete until its owner can watch agent fleets work live"; every roadmap must name and sequence it (`:220-230`) | **Missed entirely** |
| 9 | — | VIS-6 (derived, two closed exceptions) and VIS-7 (the observatory itself must be trustworthy) | Missed — defensible in a three-sentence budget |
| 10 | — | Falsifiability: if after sustained real use the owner still learns projects the old way, "**the thesis — not the scope — is judged wrong**" (`:240-245`) | Missed. Memorable when read; did not survive |

**Result — this is the test outcome, not commentary.** The three-state thesis,
comprehensible truth, no-evidence-means-Unknown, and regeneration-as-north-star
all survived recall, in doctrine's own words and with their qualifiers attached.
That is the charge's four-element north star, and on that measure `vision.md` is
memorable and the answer is yes.

Two losses are diagnostic rather than incidental, and both correlate with F8:
**the observatory/harness identity** and **the live-fleet-observability mandate**
are the two things doctrine states most vividly that the public surface never
repeats — 0 occurrences of "north star", "Genome", or "fleet observability" across
all five public files. What the surface reinforces, I kept; what only doctrine says
once, I lost. That is the argument for F8 stated as evidence rather than as
opinion: the public surface is currently the memory aid for four doctrinal ideas
and for none of the rest.

One further observation from the exercise: what I recalled *most* precisely were
the clauses carrying a named violation example ("*Violation:* rendering that region
green because its neighbors are green"). VIS-1 and VIS-2 both have them; the fleet
mandate does not.

---

## Summary of severities

| Id | Finding | Severity |
|---|---|---|
| F1 | `PROJECT-STATUS.md` "None known" over a FAILing CG-7b | **blocking** |
| F2 | `OVERVIEW.md` misstates VIS-4's mechanism; pre-decides D4 | **blocking** (for act 4) |
| F3 | Mission vocabulary unqualified in README + Layer-1 thesis | material |
| F4 | `SECURITY.md` SEC-2 scope drift; SEC-3 drops a fifth profile property | material |
| F5 | `OVERVIEW.md` frozen-noun substitution; three-state restatement drift | material |
| F6 | Status/AGENTS route act 5 to the defective D3 draft only | material |
| F7 | D3 rev1 packet missing from the semantic-delta register | material |
| F8 | Regeneration north star + Genome + fleet mandate absent from public surface | material |
| F9 | `OVERVIEW.md` "four experiences" enumeration inconsistent | minor |
| F10 | Seven smaller restatement drifts (grouped) | minor |

**What is clean and should be said plainly:** the adopted doctrine cluster is
untouched in meaning by this round and SD-5 verifies exactly as claimed; the D3
packets are minimal, digest-anchored, honestly hedged, and correctly owner-gated;
`CONTRIBUTING.md`'s VIS-5 scoping ("a product rule, not a contributor rule",
`:32-37`) is a genuine repair and is doctrinally correct; `SECURITY.md`'s
"doctrine wins" construction (`:19-20`) is the right shape for every summary table
in this repository and should be copied; and `README.md`'s authority table
correctly labels every candidate as candidate.

---

## Verdict

**EXCEPTIONS**

Recorded exceptions: **F1 and F2 are blocking** and must clear before,
respectively, `PROJECT-STATUS.md` is relied on / act 1 is offered, and act 4 binds
`OVERVIEW.md`'s digest. F3–F8 are material and should be repaired in this round.
F9–F10 are minor. The doctrine cluster itself and the D3 packets take no
exception.
