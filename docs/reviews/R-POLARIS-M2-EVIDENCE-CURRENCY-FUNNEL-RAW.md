# Independent fresh-context review — M2 evidence-currency funnel packet

Reviewed commit: `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` (worktree
`agent/syzygy-dov.2`; `git status --porcelain` shows exactly the two files
under review, both untracked).

Files under review, byte counts and sha256 computed this session by script
(`wc -c`, `sha256sum`):

- `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` — 47846 bytes,
  sha256 8f57109243f4c26c7b7da268a0050cd61f8ed9a7f71b4416b80ef83d1e721f7b
- `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json` — 3896
  bytes, sha256
  98acc654eba4ae11b5e63afe09143e57397580ee1c9e9259064f9944af66f502

Retained capture (read-only), re-derived this session: 1484487 bytes, sha256
e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111 — identical
to both the packet's head matter and the evidence JSON's `capture` block.
Decoded characters 1481819, matching the JSON.

Date: 2026-09-14. Reviewer: fresh context, no author context, read-only.

---

## What re-derived cleanly

Everything in this section I re-computed myself, by at least two methods
where the packet claims two, before reading the packet's number.

**Capture counts.** `data-epistemic-freshness` is `fresh` 713 times and takes
no other value, by three independent methods (attribute regex over the whole
document; literal split on `data-epistemic-freshness=`; a parse of every
`<span class="claim-tuple"` opening tag). Denominator: 713 claim-tuple span
openings, which also equals the count of the literal `class="claim-tuple"`.
Tuple shapes: `Observed`/`report-fact`/`fresh` ×702 and
`Unknown`/`unstated`/`fresh` ×11 — exactly the packet's row, and the 11
Unknown-at-`unstated` claims do carry `fresh`. Distinct `data-evaluation-id`
values: 1 (`evaluation:pwb-body-read:2026-09-13T13:33:24.295Z`), over 713
occurrences.

**Legend sentences.** All four freshness sentences occur exactly once in the
served bytes, inside the one `polaris-claim-states` glossary; I located the
block and read it. Three of the four (`stale`, `broken`, `superseded`) are
rendered by no tuple, so the packet's "3 of 4 unreachable" is exact.

**Instants.** 719 ISO-8601 instants in the bytes; 713 inside
`data-evaluation-id` attribute values; 6 in text nodes after a tag strip.
Offsets 859145, 859189, 860858, 1477549, 1477638, 1481753 — identical to the
evidence JSON's list. First human-visible instant at character 859145 =
58.0% of 1481819. Nothing above 58% carries a date. Confirmed.

**Reading plans.** Two plans are defined (`ARCHITECTURE_READING_PLAN` at
`apps/three-surface-poc/src/polaris-reading-plan.ts`:4, `V1_READING_PLAN` at
:293). By a method the packet does not name — counting the condensed-render
marker `class="excerpt-label"` that `polaris.ts`:506 emits only when
`reading.condensed` — the capture carries exactly 1. The packet's row is
independently confirmed, and its characterisation of the finding as *the
page's silence about the second* is fair: `polaris-reading.ts`:43 returns the
`condensed: false` full text on any guard failure, with no rendered trace.

**Code sweeps.** `assessCurrency` and `CurrencyBoundDeclaration` are
referenced by zero non-test sources under `packages/three-surface-poc-core`
or `apps/three-surface-poc` (`git grep -F` over the tracked tree, plus a
`grep -rlF` file-list sweep over the worktree including untracked and build
outputs). The only freshness value assigned in a non-test POC source is
`FRESH`, at `project-shape-model.ts`:185 and :193, by a Python `re` sweep for
`freshness\s*:` over both `src` trees; the third hit
(`fresh-checkout-demo-main.ts`:286) copies a value off the model rather than
minting one, which the evidence JSON discloses and the packet correctly does
not count. `FRESHNESS_STATES` is read at exactly one index outside cap1-core:
index `0`, at `project-shape-model.ts`:167.

**Every code line:range citation points at what the packet says it does.**
Checked one by one: `staleness.ts`:87–155 is exactly the `assessCurrency`
body; `project-shape-model.ts`:162–166 is exactly the five-line standing-
argument comment, and :167 the `FRESH` constant; `polaris-copy.ts`:45–49 is
the freshness label plus its four sentences; `polaris.ts`:357 is the
freshness `group(...)` call; `model.ts`:100–110 is the `evaluation` block
with `snapshot`, `snapshotLabel`, `inputsDigest`, `asOf` and no horizon
field; `main.ts`:80–81 are the two `observeGitRepository` calls, :113 is
`function buildModel()`, :134 is `const asOf = new Date().toISOString()`,
:187 and :201 are the only two `buildModel()` call sites;
`git-observation.ts`:61 is `rev-parse HEAD`; `walkthrough-preflight.ts`:
212–220 collects the *presented* claims' terms and requires `` `${term} —` ``
in the glossary block, so extra glossary entries are permitted, exactly as
the packet says. A sweep for `horizon` across non-test `packages/*/src` and
`apps/*/src` returns one hit and it is about horizontally scrollable tables.

**Quoted clauses.** I read VIS-2 at `.syzygy/governance/doctrine/vision.md`:96,
VIS-7 at :183, RFC2-9 at
`.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:187,
RFC2-10 at :209, `architecture.md`:221–229 and :236,
`trust-and-evidence.md`:97–104, and CAP1-REQ-062 at line 1837 of the
Capability 1 spec. Every quoted fragment is verbatim at its named location,
including the escalation-trigger fragment "a change to the constraints or
envelope the registry entry declares", which a naive single-line `grep -F`
misses because the act hard-wraps it across two lines — it is there,
verbatim, in the Escalation-triggers section of
`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`. Line numbers check out.

**PWB-REQ-007 carries a currency scenario — confirmed, and it is stronger
than the packet claims.** PWB-REQ-007 begins at line 439 and ends at line
486; the scenario "Missing current evidence remains explicit Unknown" is at
470–474, verbatim as quoted, and the Observable at 458 reads exactly
"invalid/missing currency stays Unknown and aggregates expand to members". A
case-insensitive sweep of the whole PWB spec for `currenc|freshness|stale|
superseded` finds freshness and currency language nowhere else in a
requirement body — PWB-REQ-007 is the sole owner. The packet does not
mention that PWB-REQ-007's own `warrants` block (line 480) names `RFC2-9` and
`RFC2-10` among its contracts. That is the single most direct refutation of
the standing argument Q1 puts to the owner — the digest-bound requirement
governing these very tuples declares itself warranted by the clause the code
comment says does not apply — and it is missing from Q1's case. See F20.

**Lane B, on `origin/agent/syzygy-dov.17`.** The package is absent from main
at `a9f671e` (`git ls-files | grep -i scoped-attributes` → 0). On the branch
it is exactly 9 files under
`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`.
Its `proposed/spec.md.patch` does rewrite the PWB-REQ-007 region, does insert
the scope-hoist paragraph, does rewrite the Case, Observable, Oracle,
Oracle-independence and Falsifier bullets, and does carry an
"over-asserting scope" falsifier — all as the packet says. The fragment the
packet quotes, "whose value is the same for every claim under one enclosing
scope", is verbatim. `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` states in its own
head that "Rows hash the PROPOSED bytes: current bytes with proposed/*.patch
applied", which confirms the packet's collision argument. The headline saving
188,902 bytes tailnet is verbatim in the branch's `OWNER-DECISION-PACKET.md`
and in `docs/evidence/pwb-laneb-strict-scope-estimate-2026-09-14.json`, whose
`hoistedPerField` block shows `data-epistemic-freshness: 713` — i.e. the
estimate does hoist freshness for every tuple. The packet's second collision
point is therefore not merely plausible but demonstrated: slice 5 would
invalidate a component of the figure already in front of the owner as P-68.

**Governance hygiene.** `python3 scripts/check_governance.py` run read-only
in the worktree: 32 OK, 20 WARN, 0 FAIL (52 checks). The default `clone`
scope includes untracked files (`corpus_paths`, line 330), so the packet was
in the examined corpus. No Butlers repository path appears in backticks: I
enumerated every backticked token in the packet and every one resolves to a
Syzygy path, a Syzygy route, or a code identifier. Digests: one full 64-hex
sha256 (the capture), plus short git revisions `a9f671e` and `2e3bac97790b`,
which are git object ids and not truncated act-argument digests — nothing
CG-15 reaches.

**Hard prohibitions.** I checked each of the six recommendations, answered as
recommended, against AGENTS.md's hard-prohibitions list. None authorizes
implementation code inside `openspec/**` or `.syzygy/**` (slice 5 edits a
JSON *declaration*, not code); none opens a deferred wave, Mission Control,
release, remote access or multi-user support; none adds a repository body
read (slice 2's probe is a ref resolution, correctly labeled `[Inferred]`);
none adds unattended agent coordination — Q4's recommendation is the arm that
refuses it; none adopts doctrine, accepts a contract or labels anything
accepted on the owner's behalf; none opens a second PWB spec package. The
act table names the authorizing act per slice and says "**None found**" where
none exists (row 4b). That part of the invariant is met. Two caveats are
recorded as F10 and F6.

---

## Findings

### F1 — blocking — the headroom claim against the M1 target is false

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:105–107 (and again at
:615).

> And it is not a re-opening of the page-size question: the horizon band and
> the marked legend add bytes measured in hundreds, against the ~479 KB of
> headroom the M1 ruling's target leaves.

and

> (the M1 ruling's 1.4 MB target is still the ceiling this work must not
> spend).

The M1 ruling's Q3 row states the target verbatim: "the page at Butlers head
under 1.4 MB on both host forms and under 1,000 bytes per new item after lane
B". The capture this packet measures is 1,484,487 bytes tailnet and (per the
lane B estimate record, same commit) 1,478,637 direct. The M1 ruling's target
therefore leaves **negative** headroom today: the page is 84,487 bytes over
it on the tailnet form and 78,637 over on the direct form, which is precisely
what the queued P-68 row says in its own first sentence.

The "~479 KB" figure belongs to a different authority and is stale: it is
headroom under the 2 MiB *response ceiling* measured before lane A, and
AGENTS.md records it as already earmarked ("leaving ~479 KB for the
P-60/P-61 repairs' 418–443 KB"). After lane A the ceiling headroom is
2,097,152 − 1,484,487 = 612,665 bytes, which is the ~612 KB P-68 quotes. So
the sentence conflates target with ceiling, quotes a superseded number, and
omits that most of the real headroom is spoken for by the pending Butlers
repairs. It carries no `[Observed]`/`[Inferred]` label.

The claim is load-bearing in the rhetorical sense: it is the sentence that
disposes of the page-size objection to M2 in front of an owner who ruled the
1.4 MB target eight days earlier.

*Resolves by:* replacing with the derived figures — the page is 84,487 bytes
over the ruled 1.4 MB target on the tailnet form and about 612 KB under the
2 MiB response ceiling, of which 418–443 KB is reserved for the Butlers
P-60/P-61 repairs; M2 adds hundreds of bytes and neither closes nor
materially widens the target gap, which is lane B's subject. Label it
`[Observed]` and state the arithmetic.

### F2 — blocking — PWB-REQ-020 is paraphrased into its opposite

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:398–400.

> the block may carry more than the page renders, which PWB-REQ-020 permits
> (it makes the human population recoverable *from* the machine one, not
> equal to it)

PWB-REQ-020's Observable, at line 915 of the digest-bound spec, is "both
populations contain equivalent multisets"; its Scenario, at line 933, is
"**THEN** the complete human fact multiset **equals** the machine fact
multiset"; its Falsifier ends "...or associated with a different evaluation
**in either channel**". The requirement states equality in both directions
and names either channel as a falsifying side. The packet's parenthetical
asserts the opposite as the requirement's own permission, unlabeled, and
Gate 5 then rests slice 3's "no spec delta" on it ("Slice 3 adds machine
fields, which PWB-REQ-020's direction of recoverability already permits",
:460–461).

The practical conclusion may still be right — a declared currency bound is
plausibly not a "project-shape identity, statement, source anchor, coverage
state, denominator, contradiction, body-read authority state or
walkthrough-judgment state or disclosure", and so outside the enumerated
parity population. But that is a different argument, and it is the one the
packet must make. As written, verification rule 8 is not met: the claim is
anchored to a clause that says the reverse. And if the correct reading is
that the extra machine fields *are* in the parity population, slice 3
acquires a spec delta and lands in Q6's collision, which changes the answer
to Q6.

*Resolves by:* quoting PWB-REQ-020's Observable and Scenario as they stand,
then arguing the narrower point — that the parity population is the
enumerated marker classes, that every horizon fact the page renders will
carry the same claim id in the machine answer and vice versa, and that the
`evidence` block's non-fact fields (bounds, digests) sit outside it. Note
AGENTS.md's own recorded lesson that PWB-REQ-020 parity is checked per tuple
against the machine claim by id **and both id sets**.

### F3 — non-blocking — slice 1's `broken` marker names a route that Q3 forecloses

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:330–333.

> - `broken` — its source changed since capture. *Not reachable at this
>   evaluation: this evaluation observes one pinned revision and does not
>   compare it to the repository's current state. Route: the evidence
>   horizon, reported separately below.*

Q3's recommended answer is "A second identified evaluation, **never a
freshness value**", and success criterion S3 (:499–503) requires that "no
`data-epistemic-freshness` value anywhere on the page is derived from it".
If both are answered as recommended, the evidence horizon never makes
`broken` reachable — so the route this marker offers the reader does not lead
anywhere. The copy-oracle invariant at :349–353 would then keep the `broken`
marker in place permanently, while the marker's own text promises a route
that resolves it.

This is an internal contradiction between two slices in the same packet, and
it is reader-visible copy, so it is not merely presentational.

*Resolves by:* giving `broken` the same treatment Q1's other-way branch gives
`stale` — state that `broken` is unreachable by design under the current
evaluation model and name what would change that (a design in which the model
carries evidence from a prior revision, which M2 explicitly does not build),
or withdraw the "Route:" clause for `broken` alone.

### F4 — non-blocking — Q3's strongest counter-argument is unstated

Q3 (:43) asks whether the horizon may be "folded into the pinned evaluation's
freshness field (for example by rendering changed sources as `broken`)", and
rejects it because "a horizon read from the live repository would make two
reads of one evaluation disagree".

That reasoning holds only for a horizon read **at render time**. The packet's
own slice 2 design computes the probe "once, at build, and carried on the
model — never read at render" (:376–378). A build-time probe result carried
on an immutable model does not make two reads of one evaluation disagree,
whichever field it populates. So the identity argument does not by itself
exclude arm (b).

Against arm (b) the packet must instead reach RFC2-10's evaluation-scoping of
freshness, and it must engage the fact that `broken`'s own definition — in
this page's legend, verbatim at `polaris-copy.ts`:48 and in the served bytes
— is "its source changed since capture", which is exactly the condition the
probe detects. RFC2-10 reserves render-disclosure for "a condition genuinely
outside the four"; the owner is entitled to see the argument that this
condition is not outside the four but is the fourth's definition.

*Resolves by:* restating Q3's case on the correct ground (a changed source
is a fact of a *different* evaluation, and RFC2-10's identity test binds
freshness to the evaluation that produced the claim, so a value sourced from
a second evaluation would be a freshness state no run of the first could
reproduce), and saying out loud that `broken`'s legend text describes the
probe's condition, which is why the recommendation also requires F3's copy
change.

### F5 — non-blocking — Q4's first warrant overstates a hard prohibition

Q4 (:44):

> **Arm (a), no timer.** AGENTS.md's hard prohibitions include unattended
> agent coordination, and a timer is exactly how `asOf` came to advance
> without an observation in the first place (L4-F4).

AGENTS.md's prohibition is "No unattended agent coordination". A timer or
watcher inside a single daemon that re-runs one observation is not agent
coordination on any natural reading, and the packet offers no clause that
makes it one. Also, a timer that mints a *new identified evaluation* is not
the VIS-2 violation the sentence gestures at — L4-F4 is the opposite defect,
`asOf` advancing with **no** new observation, which a timer-driven
re-observation would fix rather than cause.

The recommendation survives on its second, sound warrant, which the same cell
states: "**No act found that authorizes a timer**". A background poller is
new unauthorized daemon behaviour, and the 2026-09-02 authorization's
"any scope beyond the signed change" trigger is the right hook.

*Resolves by:* dropping the unattended-coordination sentence and leading with
"no act authorizes a background poller; the operator route rides the
2026-09-05 continuation", plus the design argument (a human-triggered
re-evaluation keeps re-observation an operator fact) which is already there
and is sufficient.

### F6 — non-blocking — the consent act's scope sentence is misquoted

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:310:

> the consent act's subject is the repository, not a revision

`decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md` §Effect says the consent
is for the pair (`project:syzygy`, `repository:butlers-configured-poc`) and
the one content class `declared-project-shape-text`, and then: "Scope:
read-only Git objects selected by the signed PWB source population **at the
Butlers revision the POC observes**." The act does name a revision, in the
scope sentence, and the probe resolves a head the POC by construction does
not yet observe.

The conclusion — that no act is needed — is very likely still right: the
escalation trigger is "any observation outside the consented content class or
repository", the probe reads a ref and no body, in the same repository, and
`git-observation.ts` already resolves `HEAD` on that repository at startup.
But the stated warrant is not what the act says.

*Resolves by:* restating as "the escalation trigger is scoped to the content
class and the repository; the probe reads a ref, not a Git object of the
source population, in the already-consented repository" and keeping the
`[Inferred]` label already present.

### F7 — non-blocking — no freshness value is specified for the undeclared-bound arm

Slice 5 (:429–434) maps `assessCurrency`'s arms onto the tuple:

> `current` → `fresh`; `age-exceeds-bound` → Unknown with
> `stale-beyond-currency-bound` and freshness `stale`; `no-bound-declared` →
> Unknown with `no-currency-bound-declared`; `future-dated-instant` and
> `unreadable-instant` → Unknown, fail closed

I read the function. The `no-bound-declared` return (`staleness.ts`:97–103)
carries **no `freshness` field at all** — unlike the three `stale` returns,
which all set `freshness: 'stale'`. Meanwhile PWB-REQ-007 requires the
complete tuple including freshness on every claim, and RFC2-10 closes the
vocabulary at four with "no implementation may mint, spell, or force-fit a
freshness value it does not carry".

So what does a claim of an *undeclared* class render for freshness? Not
`fresh` (that is the defect M2 exists to remove), not `stale` (the engine
declines to say so and the semantics differ), not a fifth value (RFC2-10
forbids it), and not absent (PWB-REQ-007 forbids it). This is unresolved, it
is not among the six questions, and it is the arm most likely to be reached
first — every class is undeclared until its bound is acted.

*Resolves by:* naming the gap in slice 5 and either answering it in the
design (e.g. `stale` with a distinct primary reason, which CAP1-REQ-062's
second clause arguably implies) or adding it to the owner's batch, since
forcing an engine that deliberately returns no freshness into a mandatory
four-value field is exactly the kind of choice RFC2-10 says must not be
"chosen by whoever implements the render first".

### F8 — non-blocking — "exactly one new boundary" is not what the tree shows

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:293–298:

> Boundaries crossed: exactly one new one. `packages/three-surface-poc-core`
> does not import from `packages/cap1-core` today for freshness; slice 5
> makes it do so. … (`FRESHNESS_STATES` is exported from
> `cap1-core/src/staleness.ts` and `project-shape-model.ts` already imports
> it, line 20)

The parenthetical refutes the sentence it qualifies. `project-shape-model.ts`
imports `FRESHNESS_STATES` and `FreshnessState` from `@syzygy/cap1-core` at
line 20 today — that is the freshness vocabulary, imported for freshness.
Slice 5 crosses **no new boundary**; it adds one symbol to an existing import
edge. Gate 3's job is to state the shape truthfully, and here it overstates
the architectural novelty of the change.

*Resolves by:* "Boundaries crossed: none new. The
`three-surface-poc-core → cap1-core` edge already carries the freshness
vocabulary (`project-shape-model.ts`:20); slice 5 adds the judge that owns
it." This makes the packet's own "narrowing, not a widening" point stronger,
not weaker.

### F9 — non-blocking — the dossier's strongest M2 finding is absent

`jq '.ranked_moves[] | select(.id=="M2")'` lists M2's `evidence_findings` as
S5-F1, L4-F1, L4-F2, L4-F3, L4-F4, L4-F5. The dossier's M2 section states
L4-F1 as "135 of 402 rows say fresh about bytes that have changed (L4-F1
[Observed], measured two ways)" and the summary at :77 adds "71 of 271
sources changed since the rendered evaluation".

A grep of the packet for `L4-F` returns L4-F2, L4-F3, L4-F4, L4-F5 and L4-F6.
**L4-F1 appears nowhere** — not re-measured against the post-lane-A capture,
not retired, not mentioned. It is the finding that turns the problem from
"one value where four are promised" (a vocabulary defect) into "the page
asserts currency about bytes that no longer exist" (an honesty defect), and
it is the empirical basis for the horizon slice the packet asks the owner to
authorize. Its absence understates the problem scope relative to the dossier
the packet says it implements.

*Resolves by:* re-measuring L4-F1 against the retained capture and Butlers
head (or stating `[Unknown]` with the reason it could not be re-derived —
AGENTS.md records that the daemon serves only the registered locator, so a
scratch-clone re-measurement is not available) and carrying it into Gate 1.

### F10 — non-blocking — slice 5 amends digest-bound bytes without naming the prohibition

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:418–424 says "The
registry entry gains, beside `resourceLimits` and `resourceLimitSemantics`, a
`currencyBounds` array…". I confirmed those two keys exist inside the single
entry of
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
and that the file's digest is bound by
`decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` (act type
`adopt-registry-entry`, exact digest
0765f4d534afad9003463790113fd433d250550091df783c1ff372d227643e4f).

AGENTS.md's hard prohibitions include "Never edit an artifact after an act
has bound its digest." The packet never names that prohibition and never
states the mechanism it relies on. The mechanism *is* sound and is exactly
the precedent Q2 cites: the 2026-09-05 act supersedes the 2026-09-02 act
"for the `adopt-registry-entry` role only" while "that record, its digest,
its tag and the bytes it bound remain immutable history". But a reader taking
the slice-5 text at face value would edit bound bytes in place.

*Resolves by:* one sentence in slice 5 — the amended entry is prepared and
adopted by a fresh superseding act in the 2026-09-05 shape; the superseded
record, its digest and the bytes it bound are never edited.

### F11 — non-blocking — a rule is asserted with no clause and no label

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:584–585:

> Only one PWB behavior-amendment package may be open at a time, and that one
> is open.

No clause is cited and no label is carried. AGENTS.md says "An OpenSpec
change is one coherent category overlapping no other change" — which is about
changes, not about how many amendment packages may be in flight. The reason
the packet actually gives (a second package drafted against the same
pre-amendment bytes could not be performed after the first, because its
manifest would name a digest the spec no longer hashes to) is sound and I
verified its premise in the lane B manifest head — but that is an
`[Inferred]` consequence of manifest mechanics, not a stated rule.

*Resolves by:* label it `[Inferred]` and let the manifest-digest reasoning
stand as the whole of the argument, or cite the clause if one exists.

### F12 — non-blocking — the staleness clause is applied past its subject

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:271–274 quotes
`trust-and-evidence.md`:97–104 — an observation record's "staleness must be
visible on the primary surface, not buried in drill-down" — and concludes:
"The current first instant at 58.0% depth is the drill-down this forbids."

The clause's subject is "An **observation record** … may still be displayed
**after its evaluation is superseded**, but its staleness must be visible…".
It governs the display of a superseded record. The capture renders a current,
unsuperseded evaluation; its instant sitting at 58% depth is a legibility
defect (and the packet's own success criterion 4 is a good answer to it) but
it is not the condition this clause forbids. The sentence carries no label.

*Resolves by:* label the step `[Inferred]` and argue it as an extension —
once the horizon exists, a changed-source count *is* the staleness this
clause puts on the primary surface, which is a better fit and strengthens
slice 2.

### F13 — editorial — the lane B hunk header is misread

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:557–560: "inserts a new
paragraph into PWB-REQ-007 immediately after line 450 and rewrites its Case,
Observable, Oracle, Oracle-independence and Falsifier bullets [Observed: the
patch hunk header names lines 450–472]".

The patch's first hunk header is `@@ -450,22 +450,55 @@`, which covers old
lines 450–471, and the insertion follows the blank line 452, not 450. Line
**472** — the `WHEN` bullet the packet quotes elsewhere as its key finding —
falls between the two hunks (`@@ -473,11 +506,20 @@` begins at 473) and is
touched by neither. A bracketed `[Observed]` claim should survive
re-derivation; this one does not.

*Resolves by:* "the first hunk covers lines 450–471 and the second 473–483;
the scenario at 470–474 is context in both, so the currency scenario M2 relies
on is byte-unchanged by lane B" — which is a stronger statement of the same
point.

### F14 — editorial — the instant grouping is off by one line

`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:134–136: "The six
human-visible instants sit at 58.0% (the revision/committed/captured
`<small>` line, three of them), 99.7% … and 100.0%".

Offsets 859145 and 859189 are on that line. Offset 860858 is 1,713 characters
later, inside a different `<p><small>` — the Authority disclosure paragraph
(`data-authority-evaluation`), whose `authority-evaluation-id` code span
carries the instant; there is a `</small></p>` between them, which I checked.
Two on that line, not three.

*Resolves by:* "58.0–58.1% (two on the revision/committed/captured `<small>`
line and one in the authority disclosure just below it)".

### F15 — editorial — four arms or five

:429 says "The four arms `assessCurrency` already implements"; Gate 6 item 4
at :625 says "each of `assessCurrency`'s five arms". The function has five
return paths (`no-bound-declared`; `stale` with basis `unreadable-instant`,
`future-dated-instant`, `age-exceeds-bound`; `current`) across three `state`
values. Pick one and say which unit is being counted — the mutation-evidence
obligation in Gate 6 depends on it.

### F16 — editorial — the register cannot have located two of the four citations

:181–182: "Locations were resolved through `DIRECTIVE-REGISTER.md` and then
read." `grep -c` over `DIRECTIVE-REGISTER.md` returns **0** for `CAP1-REQ`
and **0** for `PWB-REQ`; its own head declares 764 identifiers in 8 families,
and the spec families are not among them. VIS and RFC identifiers are there
(VIS-2 at :34, VIS-7 at :39, RFC2-9 at :243, RFC2-10 at :244). The sentence
is true for two of the four Gate-2 citations and cannot be true for
CAP1-REQ-062 or PWB-REQ-007.

*Resolves by:* "VIS and RFC locations were resolved through
`DIRECTIVE-REGISTER.md`; the register carries no spec-requirement family, so
CAP1-REQ-062 and PWB-REQ-007 were located by heading sweep in their own
spec files." This matters beyond pedantry: AGENTS.md routes clause-finding
through the register, and a future reader should know it stops at the
governed plane.

### F17 — editorial — packet and evidence file disagree on a count

:153–154 says `assessCurrency` and `CurrencyBoundDeclaration` are "referenced
in exactly three files"; the evidence JSON's `assessCurrency_files` lists
four, the extra being `packages/cap1-core/dist/staleness.d.ts`. That path
does not exist in this worktree (no build output present), so I could not
reproduce the fourth row. Say "three source files; a built declaration file
mirrors one of them when `dist/` is present", or drop the dist row from the
JSON.

### F18 — editorial — a measurement row needs its predicate

:130, "`data-polaris-item` occurrences | 409 | the page". 409 is the count of
the *attribute* `data-polaris-item="…"`. A plain substring count of
`data-polaris-item` over the same bytes returns **417**, because 8
occurrences are the distinct attribute `data-polaris-items`. Both numbers are
right about different predicates; only one is stated. Per the project's own
lesson that a figure without its predicate cannot be re-derived, name it:
"`data-polaris-item="` attribute occurrences".

### F19 — editorial — P-68 is not on the packet's own baseline

:550–554 correctly states that the nine lane B package files are "**not
present on main at `a9f671e`**" and that the branch is
`agent/syzygy-dov.17`. It then treats P-68 as a queued register row ("owner
decision P-68", ":53 P-68, queued and unruled"). I confirmed the P-68 row
exists only on `origin/agent/syzygy-dov.17`'s
`decisions/PENDING-OWNER-DECISIONS.md`; main at `a9f671e` has no P-68 and its
last update note is P-67. A reader following the packet's baseline to
`PENDING-OWNER-DECISIONS.md` finds nothing. Say so in the same parenthesis
that already handles the package files.

### F20 — editorial — Q1's case omits the evidence that settles it

Noted above under "What re-derived cleanly". PWB-REQ-007's `warrants` block
at line 480 of the digest-bound spec names `RFC2-9` and `RFC2-10` among its
contracts. The standing argument Q1 asks the owner to rule on is that RFC2-9
does not reach these claims ("RFC2-9 bounds evidence currency, and these are
declaration facts at one revision", `project-shape-model.ts`:165–166). The
requirement that governs these exact tuples declares itself warranted by
RFC2-9. Quoting that line would move Q1 from an interpretive contest to a
near-mechanical reading, and the owner should have it.

---

## Per-question assessment

| Q | Scope stated truthfully? | Genuine hard owner gate? | Recommendation follows from cited evidence? |
|---|---|---|---|
| **Q1** — does the standing "evaluation is the currency" argument satisfy RFC2-9, or is a bound required? | **Yes.** The code comment is at `project-shape-model.ts`:162–166 exactly as cited, RFC2-9 is quoted verbatim from its defined location, and the 713/713 constant is re-derived three ways. F16 is a citation-route quibble only. | **Yes.** RFC2-9 makes a bound declaration an authorization-bearing artifact honored only under the owner-act predicate, so no agent may settle it; and the answer decides whether today's render is a disclosed non-conformance under VIS-7. | **Yes**, and under-argued — the recommendation is correct on the quoted clause, and F20 names the further evidence (PWB-REQ-007's own warrants naming RFC2-9) that the packet leaves out. |
| **Q2** — where does the bound live, and under which act? | **Yes.** `resourceLimits` and `resourceLimitSemantics` do sit in the entry; the 2026-09-05 `adopt-registry-entry` act, its supersession-for-one-role pattern and the continuation direction all exist as described. | **Yes.** Only the owner performs an act, and choosing between reusing a registered phrase and minting a new act type is an owner ceremony question, not engineering judgment. | **Yes.** Arm (a)'s cost argument is verified against the act record; arm (b)'s costs (a new `_act_subjects()` registration, recorder and review) match AGENTS.md's recorded recorder contract. F10 is a missing sentence, not a wrong answer. |
| **Q3** — is the horizon a second evaluation or a freshness value? | **Partly.** The identity-test framing is accurate for a render-time read but the packet's own design computes at build, so the stated dichotomy is not the real one (F4). RFC2-10's closed-vocabulary quote is verbatim. | **Weak.** On the packet's own reasoning arm (b) is release-blocking, i.e. there is one lawful answer. This reads as a contract-determined engineering decision disclosed to the owner rather than an owner gate. Disclosing it is fine; presenting it as a choice is not, because arm (b) as framed is an invitation to authorize a VIS-7 violation. | **Yes**, but the packet reaches the right answer partly by the wrong route (F4) and then contradicts it in slice 1's copy (F3). |
| **Q4** — how is re-observation triggered? | **Yes**, with one overstated warrant (F5) and one misquoted act scope (F6). The materialize-route precedent and the `main.ts` call sites are verified exactly. | **Weak.** The packet itself finds no act authorizing arm (b), so arm (b) is not the owner's to pick without a further act — which makes this closer to a disclosure than a gate. It is legitimately batched because the operator route is new daemon surface. | **Yes.** The conclusion stands on the second warrant alone; the first should go. |
| **Q5** — mark the unreachable legend entries or delete them? | **Yes.** Three unreachable of four re-derived; RFC2-10's "Four values, closed" is verbatim; the preflight claim is exact — `walkthrough-preflight.ts`:212–220 collects only *presented* terms, so extra glossary entries are permitted. | **Weak.** This is owner-facing copy constrained by an accepted contract; the reasoning admits essentially one answer. It earns its place in the batch only because it is what the page says while Q1 is unruled — which the packet says well. | **Yes**, subject to F3: the `broken` marker's stated route does not exist under Q3's recommended answer. |
| **Q6** — sequencing against the lane B package. | **Yes**, and this is the packet's strongest section. Every claim re-derived on the branch: the 9 files, their absence from main, the PWB-REQ-007 rewrite, the "over-asserting scope" falsifier, the 188,902-byte figure, and — decisively — `hoistedPerField.data-epistemic-freshness: 713` in the lane B estimate record. F13 and F19 are citation slips, not scope errors. | **Yes.** It orders two owner decisions against each other and conditions a queued ruling (P-68) the owner has not yet made. | **Yes.** "No M2 spec package until P-68 is ruled" follows directly from the manifest binding proposed bytes, which the manifest head states in its own words. The conditional recommendation to record the freshness-hoist caveat in `syzygy-dov.17`'s notes is well earned by the estimate record. **Caveat:** F2 — if PWB-REQ-020 does not permit machine⊃human, slice 3 acquires a delta and the "no M2 spec package" answer changes. |

## Cross-cutting

**Labeling.** 17 `[Observed]` and 1 `[Inferred]` across 693 lines. The
`[Observed]` labels I could test all hold except F13's. But several
substantive claims carry no label at all, and they are disproportionately the
ones that failed re-derivation or rest on inference: F1 (headroom), F2
(PWB-REQ-020 permission), F6 (consent subject), F11 (one-package rule), F12
(staleness clause). No label I checked *overstates* in the
`[Inferred]`→`[Observed]` direction; the defect is absence, not inflation.
The one `[Inferred]` present (:310, the ref-only read) is correctly placed
and is the right call.

**Act routing.** Correct as far as it goes: four slices ride
`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`
(2026-09-05, a plain owner direction binding no digest, which I read), slice
5 takes two owner steps, and row 4b says "**None found**" for a timer. The
one hole is F6/F5's warrant quality, not the routing itself.

**Hard prohibitions.** None of the six recommendations, answered as
recommended, authorizes anything AGENTS.md forbids. Checked individually
above.

---

Verdict: REVISE

The packet is unusually well-evidenced — I re-derived every capture count,
every code sweep, every code line:range citation and every quoted clause, and
they hold, including the two claims most likely to be wrong (that
PWB-REQ-007 already carries the currency scenario, and that lane B's saving
estimate hoists the very field slice 5 would de-uniformise, which the branch's
own estimate record confirms at `hoistedPerField.data-epistemic-freshness:
713`). Q1, Q2 and Q6 are genuine owner gates, truthfully scoped, with
recommendations that follow; Q3, Q4 and Q5 are contract-determined decisions
legitimately disclosed but presented as choices whose losing arm is unlawful
on the packet's own reasoning, which is a framing to fix rather than a defect
of substance. I withhold CONFIRM for two reasons, both cheap to repair and
both false statements about an authority put in front of the owner: F1 tells
the owner there is ~479 KB of headroom under a target the page is in fact
84,487 bytes over, using a stale figure belonging to a different ceiling and
already earmarked for the Butlers repairs; and F2 states as PWB-REQ-020's own
permission the exact opposite of its Observable and Scenario, and then rests
Gate 5's "no spec delta" — and therefore Q6's answer — on it. Repair those
two, resolve the `broken`-route contradiction (F3) and the undeclared-class
freshness hole (F7), label the five unlabeled inferences, and this becomes a
CONFIRM without any change to the six recommended answers.
