# Capability 1 — owner decision index

> **SUPERSEDED 2026-08-17 — historical.** Written for the 2026-08-14
> sitting; the owner then ruled eight of the decisions below on
> 2026-08-16 (P-31, P-33, P-34, P-35, P-36, P-37, P-38, P-39, P-40) and
> the P-41/P-42 review cycle closed 2026-08-17. Nothing here is current.
> The live open queue is `decisions/PENDING-OWNER-DECISIONS.md`; the
> resolved record is `decisions/DECISION-HISTORY.md`.

> **An index, not a packet.** This page decides nothing, recommends nothing,
> and reproduces no review history. It answers one question: **which of the
> open decisions can actually be made right now, and which cannot yet.**
>
> It replaces the single combined packet's implied model — that the owner
> sits down once and settles everything — which review **RD-52** found false
> and returned `REVISE` over. The decisions have genuinely different
> readiness, and presenting them as one list made the unready ones look like
> hesitation rather than unfinished work.
>
> Where this page and a packet disagree, **the packet wins and this page is
> stale.** The queue itself is
> [`../../../decisions/PENDING-OWNER-DECISIONS.md`](../../../decisions/PENDING-OWNER-DECISIONS.md).

## Read this first

Nothing below is urgent in the sense of blocking today's work, because
**nothing is being built.** What the ordering buys is that each decision is
made once, knowing what it costs, rather than discovered mid-act.

**One decision gates more than any other: P-33.** It is the sole obstacle to
*offering* Wave A, and Wave B follows Wave A. Everything in group 4 sits
behind it.

## 1. Rulable now — the packet contains everything needed

| `P-nn` | Question | Packet | Note |
|---|---|---|---|
| **P-36** | `Unknown` versus `Gap` — one word or two? | [`UNKNOWNS-AND-GAPS-DECISION.md`](../../../decisions/UNKNOWNS-AND-GAPS-DECISION.md) | Capability 1's acceptance criteria use both words |
| **P-37** | Which project-shape facets exist, and who owns the vocabulary? | [`PROJECT-SHAPE-FACETS-DECISION.md`](../../../decisions/PROJECT-SHAPE-FACETS-DECISION.md) | The facet vocabulary is drafted **nowhere**; the ruling also picks its drafting site |
| **P-38** | Human entry point and per-repository discoverability | [`HUMAN-ENTRY-DECISION.md`](../../../decisions/HUMAN-ENTRY-DECISION.md) | On the E3 path; Wave B ratifies |
| **P-40** | One specification per what? | [`SPECIFICATION-GRANULARITY-DECISION.md`](../../../decisions/SPECIFICATION-GRANULARITY-DECISION.md) | Gates the CC-SPEC/CC-IMPACT freeze in group 3 |
| **P-31** | The merged-but-unreconciled `Unknown` reason | *register row only — a bounded packet is owed* | The exemption arm **is drafted**, as RFC2-19(a), disclosed in place as awaiting this ruling. Ruling wanted at or before the Wave A act so the arm is ratified knowingly |

**P-33 is not in this group.** Its packet is being re-derived and re-reviewed
this round; it moves here only if that review permits. See group 3.

## 2. Pre-work required — the owner cannot rule until someone does the work

| `P-nn` | Question | What is missing |
|---|---|---|
| **P-39** | Which OpenSpec form and version? | **Nobody has compared the versions.** The choice needs the installed version, the current official upstream version, and the format/migration differences between them, each read from a current public source on a stated date. Ruling without that pins a version chosen from a stale packet |
| **P-35** | What are the project's operating constraints? | **Only the owner has the facts** — operators, hours per week, independent-review capacity, provider budget, maximum concurrent workstreams, proving project, time horizon, scope-reduction triggers. The packet is a form to fill in, and honest `Unknown` is a legitimate answer to any line |

P-35 is unusual: it is not a decision between prepared options, it is a
request for facts that only exist in the owner's head. It gates the formal
administration's A6 and F5 verdicts, and nothing else on the launch path.

## 3. Review, then act — do not approve an unrepaired `REVISE`

Each of these has a subject that an independent reviewer has asked to change.
**Approving one as it stands means approving something its own review said was
not ready.** That is a lawful owner choice, and the packets say so plainly,
but it should be a knowing one.

| `P-nn` | Subject | Review state |
|---|---|---|
| **P-34** | Launch-gate instrument as process policy | **RD-47 `REVISE`, RD-48 `REVISE`** — both obtained 2026-08-11, findings unrepaired. Repair is this round's Workstream B; re-review is required after |
| **P-41** | Specification-acceptance craft amendment | **RD-51 `REVISE`** — reviewed jointly with P-42. Freeze follows the P-40 ruling |
| **P-42** | Shape-to-spec impact craft amendment | **RD-51 `REVISE`** — same review. Additionally, the blind propagation fixture has **never been administered** |
| **P-33** | Wave A installation shape | **RD-49 `REVISE`**, three findings marked BLOCKING. Its section G answers "could an owner rule from this packet alone?" with **"No."** |

P-41 and P-42 must converge **together**. They currently define overlapping
dependency relationships inconsistently, which is what RD-51 found, and
freezing one without the other reintroduces the disagreement.

## 4. Later acts — not decisions to settle now

These are **acts**, not decisions. They have ceremony phrases and digest-bound
arguments, and each waits on something above.

| Act | Waits on |
|---|---|
| **Wave A** | P-33 ruled, then the offer. The argument is **already confirmed** — `VERDICT: CONFIRM`, RD-31b |
| **Wave B** | Wave A. Also already confirmed — RD-32c. Nothing else withholds it |
| **Craft amendments** (P-12, P-41, P-42) | Their own reviews, then the `CONFIRM CRAFT AMENDMENT` route |
| **Topology, overview, D3** | Independent of the launch path |
| **The formal launch decision** | The formal administration, which needs P-34, which needs group 3 |

Calling any of these "a decision to settle now" would be wrong twice: an act
is not a decision, and none of them is reachable today.

## What this index deliberately omits

- **Every recommendation.** They live in the packets, labelled `[Inferred]`,
  beside their costs and their honest counter-arguments.
- **All review history.** Seven `REVISE` verdicts and one `CONFIRM WITH
  EXCEPTIONS` are named above by their outcome only. The raw bytes are kept
  and are not default context.
- **Any claim of completeness about the queue.** The queue holds **31 open
  rows**; this page covers the **launch-critical** ones. The rest are open,
  real, and off Capability 1's path.
