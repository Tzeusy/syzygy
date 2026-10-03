# Semantic delta D7 — held derived computation delegates no decision

> **Candidate — binds nothing.** Drafted 2026-10-03 for `syzygy-u05.14`
> in the form of `../policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. Doctrine
> amendment is an owner act (VIS-4); this delta is the proposal, never the
> act. The owner's questions and arms live in `OWNER-DECISION-PACKET.md`
> (this directory); where the two differ, the packet's section 1 text is
> the proposed text. Round 1 returned `REVISE`; the repairs are recorded in
> `ROUND-1-DISPOSITIONS.md` and are unconfirmed.

**Artifact(s):** `.syzygy/governance/doctrine/vision.md` (sha256
`93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d`) and
`.syzygy/governance/doctrine/architecture.md` (sha256
`d1987f7f630b82eee359e14e89e6422ab74374a2578c218f73d47c80eefcb565`), both
read on 2026-10-03 at `origin/main` `66d42d09`.

**Stable IDs affected:** none renumbered, retired or reworded. The
insertions sit under the unnumbered "Not autonomous" bullet of `vision.md`
("What Syzygy is not") and in the unnumbered loop paragraph of
`architecture.md` ("Snapshots and the loop"). The inserted text cites
VIS-4 (its stated bounds), VIS-5, VIS-6, SEC-2 and SEC-3; none of their
bytes change.

**Change class:** **Normative.** Under today's text an unrequested
re-observation on a human act (other than a recorded revocation, RFC5-11)
has no doctrinal footing and every packet so far has treated it as
unavailable; after D7 a closed class of unrequested computation is lawful.
Someone who complied before still complies, but a design that was
non-compliant (a computation run on page open and held for the next look)
becomes compliant — the template's "widened" case. It is not Clarifying:
the current text does not *already* admit the class in a way that was
merely misreadable; D7 adds a trigger. The packet's further position that
the class sits *inside* VIS-4's stated bounds answers a different question
(whether VIS-4's autonomy-beyond-bounds mechanism is needed) and does not
make the change Clarifying (`OWNER-DECISION-PACKET.md` §7). An owner who
chose the packet's arm B would be ruling the change Clarifying instead.
[Inferred: the classification is this drafter's claim.]

**Author:** agent drafting session (lane-b worker) for `syzygy-u05.14`.

**Date:** 2026-10-03

## Current meaning

`vision.md` lines 105–107, quoted exactly:

> - **Not autonomous.** The loop is human-triggered; autonomy beyond VIS-4's
>   stated bounds is licensed only through the mechanism VIS-4 names, never by
>   reinterpretation.

`architecture.md` lines 329–334, quoted exactly:

> **The loop:** intent → observation → gaps → reviewed work → fleet execution →
> verification. It has one upward arrow: verification and runtime evidence may
> open spec-indictment gaps that route to the owner. The loop is
> **human-triggered**: someone specs a desired shape, then deliberately triggers
> a propagate/sync pass. Work-to-code and code-to-deployment belong to the
> orchestration toolchain, outside Syzygy's body.

Meaning today: every computation in the loop runs because a human
deliberately asked for it. Doctrine names no computation that may run on a
human act that did not ask for it, and names no trigger class at all other
than a deliberate request. The owner's P-69 ruling ("No timer or background
poller on any arm") and RFC2-19 ("never autonomously on merge events")
apply that reading in their own scopes.

## Proposed meaning

The current text stays, verbatim. Three sub-bullets are added under the
`vision.md` bullet, and the `architecture.md` paragraph's last line is
extended by one sentence. Exact bytes, reproduced from
`OWNER-DECISION-PACKET.md` §1.1 and §1.2 so this delta is complete on its
own:

`vision.md`, after the bullet's last line (line 107):

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

`architecture.md`, the resulting paragraph:

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

Meaning after: a closed class of four effects may run on a human act that
did not request it, or on a hand-installed hook that fires only on human
acts; never on a clock or watcher Syzygy owns; never with a notify,
dispatch, reprioritize, adopt or self-trigger effect; never holding model
output or anything that is not rebuildable or an identified evaluation of
observed state; never opening a read, write, egress or execution path; and
never where an accepted contract requires a deliberately triggered pass.
The text is lawful only on an owner ruling that the class sits inside
VIS-4's stated bounds (packet Q1), since its heading states that reason.

## What explicitly does NOT change

- **VIS-4**: shape-defining changes still need owner sign-off; agents
  still draft and never adopt; the spec-adoption gate and its two-part
  opening mechanism are untouched; the always-human classes are untouched.
- **VIS-5**: the write universe stays `openspec/**` and `.syzygy/**`;
  staging commits nothing even there; no hook is installed by Syzygy.
- **VIS-6**: exception (a) stays the owner's own presentation state;
  exception (b) stays observation records; nothing new is held that is not
  a projection or an identified evaluation of observed state, and no model
  output is held.
- **SEC-1 … SEC-5**: no read, egress, execution, credential or exposure
  rule moves.
- **The loop**: dispatch, propagation and reconciliation stay
  human-triggered. `v1.md`'s "Human-triggered propagation at full
  breadth" is untouched.
- **RFC2-19 and the RFC2 merge chain** (`reconciliation-chain.md` lines
  155–157 and 245–247): stay as written and stricter than D7. Every
  evaluation that captures a merge fact still runs inside a deliberately
  triggered pass, whatever D7's trigger (`OWNER-DECISION-PACKET.md` §4).
- **RFC4-16, RFC5-11**: untouched.
- **P-69**: its no-timer rule stands on every arm; D7 states it generally.
- **P-71 Q3, P-71-Q5, P-79 Q4, P-79 Q6**: untouched; the 2026-09-02
  implementation authorization's scope and escalation triggers are
  untouched, so any new daemon behaviour still needs its own authority.
- **The "autonomous behavior" exclusions of acts in force** (ledger §1b):
  not edited; D7 authorizes no implementation under any of them.
- **The trusted-bootstrap observation direction's exclusions** (writes to
  observed repositories, egress, autonomous owner acts): untouched.
- **The live fleet observability mandate**: no doctrine text; entry
  criteria are offered for a roadmap (`OWNER-DECISION-PACKET.md` §5).
- **Candidate D3** (bounded mission): it edits the same bullet and
  paragraph at different bytes; the second adoption needs a re-anchored
  review (`OWNER-DECISION-PACKET.md` §1.3). Its substance is untouched.

## Warrant

Vision pursuit 2026-09-22, ranked move N14 ("Doctrine amendment packet A,
the molding half"), released for drafting by the owner's closure of the
pursuit HOLD gate `syzygy-dca`; bead `syzygy-u05.14` notes (2026-10-03):
"Scope: draft the doctrine amendment packet only, for owner adoption or
rejection; no doctrine byte edited, nothing adopted (VIS-4)." That is a
warrant to draft, not to adopt.

## Evidence or decision basis

- Pursuit dossier `docs/pursuits/2026-09-22-vision-pursuit.md`, section
  "N14"; data file `docs/pursuits/2026-09-22-vision-pursuit-data.json`,
  findings L11-F1, L11-F8, L10-F3, L4-F2 and moves L11-M5, L10-M6, L4-M4.
- Owner rulings P-69, P-71, P-79:
  `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
  (sha256 `a59294d4a19eb9b5542fb2f13425521484bc3009a76ca991cfbd736266b71079`
  at `66d42d09`).
- RFC5-11 (`contracts/rfcs/RFC-0005/admission-and-boundary.md`, sha256
  `a742a77fb14ee415d705f31d2e8733a94a51cffd6ccd5dca2f5d0cc1e3f533e0`) and
  RFC2-19 with the merge chain (`contracts/rfcs/RFC-0002/reconciliation-chain.md`,
  sha256 `7d7f876bd03c5a1e7b5120f1e452b82d85483430e2355068ab03138845f38bb5`).
- `decisions/D4-RULING-DECISION.md` (P-24) and
  `decisions/BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md` (2026-08-31)
  for the VIS-4-bounds position, the reason-stating style and arm B.

Every basis is a tracked file reachable from the clone.

## Terms introduced / retired

One term introduced: **held derived computation** — the closed class of
four effects (observe, compute the difference from the last identified
evaluation, stage a draft, hold the result) run on a lawful trigger. It
does not collide with an existing term [Observed: the literal
`held derived computation` occurs in no tracked file at `66d42d09`; checked
by `git grep -i -F` and by Python `str.lower().count` over every tracked
file, 0 and 0]. "Unprompted" is used in its plain sense and defined in the
packet (§2), not entered as a term. Entering the term in
`../policy-candidates/TERM-REGISTRY.md` is a post-adoption step (that
registry is candidate material). No term is retired.

## Downstream impact

Method and full tables: `IMPACT-LEDGER.md` (this directory) — a Python
regex trigger sweep over 1,536 tracked files, confirmed by `git grep -l`
(95 hit files both ways at `66d42d09`), every authority-lane hit read and
dispositioned; a wrap-tolerant re-run; an "autonomous behavior" sweep over
212 authority files (10 hits); a notification sweep over 229 files; and a
derived-reader sweep over 417 source files. Summary: no doctrine, contract,
decision or specification sentence is made false by arm A; RFC2-19 and the
RFC2 merge chain stay stricter and confine D7's headline example; the
"autonomous behavior" exclusions are narrowed in reach, not falsified; two
derived indexes regenerate after application; four non-authority
observations are routed, not repaired.

## Migration / supersession plan

On adoption (Q1 "inside", arm A) and only then, in one change:

1. apply the two insertions as the exact bytes above, after re-checking
   both anchors' sha256;
2. add row D7 to `decisions/DOCTRINE-AMENDMENT-LOG.md`;
3. regenerate the derived indexes that read doctrine bytes
   (`IMPACT-LEDGER.md` §4) and run the canonical battery;
4. nothing is superseded: no artifact leaves a reading path.

Arms B and C edit no doctrine byte and need no migration. No digest-bound
artifact is touched on any arm [Observed: neither doctrine digest above
appears in any performed act's manifest; the only tracked citers of either
digest are three files of one review-evidence package,
`docs/evidence/polaris-understanding-reconciliation-2026-09-28/`, whose
review inputs record the vision.md digest as the bytes reviewed then — a
record of history that application would not falsify (rule 10)].

## Review

**Required class:** Normative — full fresh-context review per CC-REV-1;
owner adoption (VIS-4).
**Reviewer:** one fresh-context agent with no access to the drafting
session; brief in `REVIEW-BRIEF.md`.
**Verdict:** round 1 `REVISE` (`docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md`
line 4), repaired once per `ROUND-1-DISPOSITIONS.md`; no round 2 under the
stopping rule, so the repaired bytes are unconfirmed.
