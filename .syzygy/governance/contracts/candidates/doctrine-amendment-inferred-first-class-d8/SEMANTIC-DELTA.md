# Semantic delta D8 — Inferred as a first-class rendered state

> **Candidate — binds nothing.** Drafted 2026-10-03 for `syzygy-u05.15`
> in the form of `../policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. Doctrine
> amendment is an owner act (VIS-4); this delta is the proposal, never the
> act. The owner's questions and arms live in `OWNER-DECISION-PACKET.md`
> (this directory); where the two differ, the packet's section 1 text is
> the proposed text. Round 1 returned `REVISE`; the repairs are recorded in
> `ROUND-1-DISPOSITIONS.md` and are unconfirmed.

**Artifact(s):** `.syzygy/governance/doctrine/trust-and-evidence.md`
(sha256 `6bf79befec771447b9f70206ee85a406eaffb16b98c8ae1c05f465cd7e486b58`),
`.syzygy/governance/doctrine/vision.md` (sha256
`93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d`) and
`.syzygy/governance/doctrine/architecture.md` (sha256
`d1987f7f630b82eee359e14e89e6422ab74374a2578c218f73d47c80eefcb565`), all
read on 2026-10-03 at `origin/main` `6bb6ef26`.

**Stable IDs affected:** none renumbered, retired or reworded. Insertion
(d2) sits inside VIS-6's body as a sub-bullet; VIS-6's two closed
exceptions and its violation sentence keep every byte. The other insertions
sit in unnumbered sections of `trust-and-evidence.md` and
`architecture.md`. The inserted text cites VIS-4, VIS-6 and VIS-7.

**Change class, per clause** [Inferred: the classification is this
drafter's claim]:

| Clause | Class | Why |
|---|---|---|
| (a) synthesis | Normative, narrowing | Synthesis is lawful today (lines 95–96, RFC7-2(c)); the clause adds obligations (name inputs, regenerate on change, never fill an Unknown). A design compliant before may not be after; none that was non-compliant becomes compliant |
| (b) attributed answer | Normative | Names a record class doctrine does not name and fixes its rendering and its non-authority |
| (c) correspondence | Normative, narrowing over a wider domain | RFC1-16 and RFC4-26 define class (ii) for capability↔code only; the clause names the relation for any cross-surface subject and requires it be counted apart from declared edges. Its authority limit is already doctrine for every subject (`trust-and-evidence.md` lines 118–119) |
| (d) observed-only project | Normative, widened | VIS-6's commit-out names only a project's own plane; after (d) a second destination exists, the observing project's `.syzygy/**`. A design that kept such content nowhere, or that writes into the observed project under P-71-Q5's two acts, is still compliant; a design that commits it to the observing project becomes describable, though still unwritten without its own act |
| (e) self-observation | Normative, narrowing | Removes authority from a record class that does not yet exist |
| (f) figures | Clarifying | VIS-4, RFC2-25's `editorial-draft` state ("stays non-citable even after that act completes") and RFC7-3/RFC7-4 already say it |

**Author:** agent drafting session (lane-b worker) for `syzygy-u05.15`.

**Date:** 2026-10-03

## Current meaning

`trust-and-evidence.md` lines 95–96, quoted exactly:

> - Inferences may be woven into explanatory narrative but must never be
>   indistinguishable from deterministic fact.

Lines 134–137:

> - **Rendering may blend the layers**, provided provenance is available where
>   the claim is consumed (hover, query, API field) and inferred structure stays
>   visually distinct from observed structure.
>   - A speculated future component must never look like an existing one.

Lines 36–49 name two non-evidence warrants, "A recorded human decision" and
"A work warrant"; neither is an answer about intent. Lines 157–180 state
the trust floor; nothing in doctrine names Syzygy observing itself.

`vision.md` lines 232–234 (VIS-6):

> - **Syzygy's databases and views are projections.** Content it authors is
>   committed out to the governed plane, which then becomes the authoritative
>   source.

`architecture.md` lines 23–25:

> - Any other repository in the project is a declared **observed-source
>   repository**, read-only to Syzygy unless separately onboarded as a governed
>   project.

Meaning today: inference may appear in narrative if marked, and has no
authority to establish a status for any subject (lines 118–119); a
capability↔code correspondence is an accepted-contract class (ii) relation
with no defined entry profile; an owner answer about intent has no
doctrinal class; content about a project Syzygy may not write has one VIS-6
destination, that project's own plane, reachable only by acts (P-71-Q5);
and self-observation is unaddressed.

## Proposed meaning

The exact inserted bytes are `OWNER-DECISION-PACKET.md` §1 (a)–(f). In
meaning:

- (a) A surface-composed synthesis is an Inferred claim with named inputs,
  no new facts, never itself an anchored claim, no fresher than its stalest
  input, withdrawn on a broken or superseded input, and never an
  Unknown-filler.
- (b) An owner's answer about intent is a third non-evidence, non-warrant
  class: attributed, dated, withdrawable, committed out, rendered as
  Observed about the record only, beside an Unknown never in its place, and
  adopted intent only by an act. An adjudication of a contradiction is not
  this class.
- (c) An inferred cross-surface link is Inferred, counted apart from
  declared edges, challenge authority only.
- (d) An observed-only project is named (a project with a designated
  governance root and an empty write surface); content Syzygy authors about
  it may be committed to the observing project's `.syzygy/**`, as Syzygy's
  attributed record, never as the project's declaration or text.
- (e) Observation records whose subject is Syzygy's own governance root
  are never the evidence for a claim about Syzygy's own alignment,
  convergence, genome-completeness or release verdict; pipeline-property
  evidence over that subject still counts.
- (f) A machine-drafted presentation draft is an `editorial-draft`: never a
  claim source, before or after a human authors it into presentation.

## What explicitly does NOT change

- The three-label rule, RFC2-25's six closed tiers and three sibling
  surface states, RFC2-24's twelve Unknown reasons and RFC2-10's four
  freshness values: no clause adds a value (packet §2).
- VIS-6's two closed exceptions and its violation sentence: (b) and (d)
  keep content *inside* VIS-6 by committing it out, never by adding an
  exception.
- VIS-5's write roots: nothing is written into an observed project, and no
  write about one is authorized (packet §1 (d), §3).
- The trust floor's four bullets and its closing sentence.
- Every accepted contract, PWB-REQ-012, the POC specification and
  REQ-polaris-generation-031 (packet §6).
- P-71 Q3's ruling (a pure drafter that writes no file), P-71-Q5's act
  route into an observed project, and P-74 Q3's three acts.
- RFC1's deferred portfolio profile (SDR-30); whether (d) needs it is an
  owner question (packet §7 Q-C2).

## Warrant

Pursuit move N15 (`docs/pursuits/2026-09-22-vision-pursuit-data.json`) and
bead `syzygy-u05.15`, both requests to draft only. No owner act authorizes
or adopts anything here.

## Evidence or decision basis

- N15's `why`, quoted in packet §0 [Observed as a quote; its figures are the
  pursuit's, not re-measured].
- The premise check in packet §0, each row citing its clause.
- Owner rulings P-71 Q3, P-71-Q5, P-74 Q3, P-75 Q4 and P-76 Q2
  (`decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`) and A6's
  proving-project order (`decisions/A6-RESOURCE-ENVELOPE-DECISION.md`
  line 25).

## Terms introduced / retired

Introduced in doctrine, if adopted: **synthesis** (a), **attributed owner
answer** (b), **correspondence** (c), **observed-only project** (d),
**self-observation** (e). None is retired. "Synthesis" already occurs in
the generator specifications with a different sense, the generator's
composition of a manifesto (`IMPACT-LEDGER.md` §3); clause (a) is scoped to
prose a *surface* composes, and the reviewer is asked whether that scope is
clear enough. The doctrine README glossary would take the adopted terms in
the same commit (packet §9 step 3).

## Downstream impact

`IMPACT-LEDGER.md` carries the sweep and its dispositions. In short: no
accepted contract is made false; REQ-polaris-generation-031 is consistent
with (b); P-74 Q3's self-observation acts are consistent with (e) and
should follow it; PWB-REQ-012, the POC specification's class (ii)
exclusion and RFC1's inference-profile and portfolio-profile deferrals are
untouched and named as owner questions (packet §7). Application drifts
generated artifacts the battery checks, which the recipe regenerates
(ledger §4).

## Migration / supersession plan

None at doctrine level: no clause makes an existing artifact non-compliant
[Inferred: no surface today renders a synthesis, a correspondence, an
owner answer, a record about an observed-only project or a
self-observation; the ledger's sweep found none in the specification or
decision lanes]. On adoption, each adopted clause enters the
feature-request funnel; derived indexes regenerate per packet §9.

## Review

**Required class:** fresh-context review (CC-REV-1), one round under
`REVIEW-BRIEF.md`; the stopping rule there was set before the round.
**Reviewer:** a fresh agent that did not draft this package.
**Verdict:** recorded verbatim in the raw and in `ROUND-1-DISPOSITIONS.md`.
