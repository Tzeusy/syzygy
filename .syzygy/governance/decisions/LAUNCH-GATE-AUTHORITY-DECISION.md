# Owner decision packet — launch-gate process-policy authority (P-34)

> **This file decides nothing, adopts nothing, approves nothing.** It is
> the exact owner decision required to put the launch-gate instrument into
> force as process policy. Queued in `PENDING-OWNER-DECISIONS.md` as
> **P-34**. Until this decision is recorded, the instrument is a candidate:
> its administrations are evidence the owner may weigh, and nothing more.
>
> *Rewritten 2026-08-11 as a bounded packet (owner charter §6.2). The
> repair chain it used to reproduce — thirteen versions, thirteen reviews —
> is linked, not restated. You should not need to understand a single
> Markdown parser failure to make this decision.*

## Question

Approve `launch-gate-pre-specifications.md` **v2.4** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

*(Repointed 2026-08-13 from v2.0, 2026-08-16 from v2.2, and again 2026-08-16
from v2.3 after the owner ruled arm (c). This packet
once asked for v2.0 after the instrument had moved twice — it would have
routed the owner to bytes nobody offers, which is the defect review RD-8
called "the finding that converts act 1 from a knowing act into a
surprised one." Every v2.0, v2.1, v2.2 and v2.3 digest is superseded and
satisfies nothing.)*

## What the policy governs

```text
the question set (A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1)
the administration protocol — materials, order, who may administer
the closed verdict vocabulary
the verdict formula and its two pass branches
the launch-scope parameters (§8)
the structured administration record and its generated report
the trend log
```

## What it never governs

```text
whether specifications are authored          — that is your launch decision
the content of any artifact under judgment   — the gate judges, it does not author
any acceptance, adoption, or approval        — no verdict is an act (VIS-4)
```

A `READY` verdict authorizes nothing. It is evidence you may weigh when
making a separate launch decision, and a gate administered under an
approved policy is worth exactly as much as the administration behind it.

## What you would be binding

| Artifact | sha256 |
|---|---|
| `launch-gate-pre-specifications.md` (v2.4) | `1852c2c3d31eff3afa0924b6b72e855481ab2516ba8fde5eda7b2ae8772f01e8` |
| `launch-gate-administration.schema.json` | `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` |

The **schema digest is unchanged** across v2.0 through v2.4 — the
amendments changed how the instrument states its rules, not the record
format. That is the fact to check rather than take on trust.

Verify before acting — the digest belongs to the artifact, not to this
page:

```sh
# from the repository root — both artifacts live there, and this packet
# does not. Run from anywhere else and you get "No such file or directory",
# which reads like a missing artifact rather than a wrong directory.
cd "$(git rev-parse --show-toplevel)"
sha256sum launch-gate-pre-specifications.md launch-gate-administration.schema.json
```

## What changed at v2.0, in five lines — and what changed after it

The administration record stops being Markdown. It is JSON validated
against the schema above; the human report is generated from it and never
read back as authority; the verdict is computed and the schema **rejects** a
claimed one. §1, §3, §4 and §8 of the instrument are **byte-identical** to
v1.18 — no question's text moved, the formula is unchanged, and the
parameter block still binds. Full record of every change of meaning:
`../contracts/candidates/round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md`.

**Why a format change rather than another fix:** thirteen consecutive
independent re-reviews of the Markdown record format each found a real
defect, and each repair minted the next. The chronology is
`launch-gate/HISTORY.md` and you do not need it to decide this.

**v2.1 through v2.3, in four more lines.** v2.1 repaired the two `REVISE`
verdicts returned against v2.0; its own two reviews returned `REVISE`
again, converging on one blocking defect, and v2.2 repaired that. v2.2's
two reviews (RD-61/RD-62, 2026-08-16) returned `REVISE` a third time —
**converging again on one defect** — and v2.3 repaired it.

**v2.3's own review pair (RD-65/RD-66) returned 2026-08-16, both `REVISE`**
— the fourth consecutive `REVISE` pair, and the round the pattern stopped
narrowing (a known forgery class re-surfaced at a new site). The owner
weighed that under arm (c) and **ruled arm (c): a structural v2.4 repair.**
v2.4 is the repair; its own pair (RD-67/RD-68) is dispatched in this same
round. Until they return `CONFIRM`, this packet is prepared, not offered.
Deltas:
`../contracts/candidates/round-2026-08g/LAUNCH-GATE-v2.1-SEMANTIC-DELTA.md`,
`…/round-2026-08g/LAUNCH-GATE-v2.2-SEMANTIC-DELTA.md`,
`…/round-2026-08h/LAUNCH-GATE-v2.3-SEMANTIC-DELTA.md` and
`…/round-2026-08h/LAUNCH-GATE-v2.4-SEMANTIC-DELTA.md`.

## Independent review verdicts

> **Two reviews are required, against the version being approved, before
> this decision is offerable.** The owner charter (§5.6, §14) commissions a
> policy-semantics review — *did this version weaken any readiness question
> or formula?* — and a structured-record review — *can malformed or
> contradictory data produce a false READY, and does the generated report
> faithfully present the canonical record?*
>
> **Status 2026-08-16: ten completed reviews across v2.0–v2.4, ten `REVISE`
> verdicts.** The owner ruled arm (c) after the v2.3 pair; v2.4 is that
> structural repair, and its pair — RD-67 (policy) and RD-68 (machinery), the
> ninth and tenth reviews — both returned `REVISE` on 2026-08-16 against
> frozen commit `4dd6e20`. The structural repair that was genuinely
> structural (RD-66 f1's mechanical forgery sweep) **held**; the two new
> BLOCKING findings are the *other* two class defects, instance-patched this
> round and recurring at new addresses. **P-34's approve/decline now returns
> to the owner** with that fifth-`REVISE` evidence — this packet remains
> **prepared, not offered**.

| Review | Subject | Verdict (copied exactly) |
|---|---|---|
| Policy semantics | **v2.0** instrument | `REVISE` — RD-48, 2026-08-11, frozen commit `e2efda6` |
| Structured record | **v2.0** schema, validator, renderer | `REVISE` — RD-47, 2026-08-11, frozen commit `e2efda6` |
| Policy semantics | **v2.1** instrument | `REVISE` — RD-55, 2026-08-13 |
| Structured record | **v2.1** schema, validator, renderer | `REVISE` — RD-56, 2026-08-13 |
| Policy semantics | **v2.2** instrument | `REVISE` — RD-61, 2026-08-16, frozen commit `918574c` |
| Structured record | **v2.2** schema, validator, renderer | `REVISE` — RD-62, 2026-08-16, frozen commit `918574c` |
| Policy semantics | **v2.3** instrument | `REVISE` — RD-65, 2026-08-16, frozen commit `494acab` |
| Structured record | **v2.3** schema, validator, renderer | `REVISE` — RD-66, 2026-08-16, frozen commit `494acab` |
| Policy semantics | **v2.4** — the version this packet binds | `REVISE` — RD-67, 2026-08-16, frozen commit `4dd6e20` |
| Structured record | **v2.4** | `REVISE` — RD-68, 2026-08-16, frozen commit `4dd6e20` |

**Ten reviews, ten `REVISE` verdicts, across five versions (v2.0–v2.4).**
Each pair was dispatched separately in fresh context, neither seeing the
other's output. The v2.3 pair verified the repair account fairly (RD-65:
**nothing weakened** v2.2→v2.3, six of RD-61's eleven repaired; RD-66: eight
of RD-62's thirteen repaired) but both returned `REVISE`, converging on the
*class* — RD-66's forgery class (RD-47 f2 → RD-56 f2 → RD-62 f1) at
`prior_record.path`, RD-65's at the schema's `HEAD` binding. The owner ruled
arm (c): a **structural** v2.4 repair aimed at that class.

**The v2.4 pair (RD-67/RD-68) returned `REVISE`/`REVISE` — the fifth
consecutive pair — and the result is specific.** The one repair that was
genuinely structural, RD-66 f1's mechanical forgery sweep over every string
leaf, **held**: RD-68 drove 1,620 leaf/spelling combinations through it and
found **no live forgery in v2.4's bytes**. But the *other* two class defects,
instance-patched this round, recurred at new addresses — both as fresh
BLOCKING false-`READY` paths:

- **RD-67 f1** — RD-61 f1's forbidden-verdict-word→eligible-`READY` class:
  the schema types `repository_commit` `^[0-9a-f]{7,40}$`, but the validator
  reads the schema at the record's commit only for a *full 40-hex* value, so
  an **abbreviated** commit (the repo's own `[:7]` house style) falls through
  to reading the schema at `HEAD` — a widening committed at `HEAD` then admits
  a forbidden word on an A–D row into an eligible `READY FOR`, zero errors.
- **RD-68 f1** — RD-66 f2's invisible-character→eligible-`READY` class: the
  strip covers categories `Cf/Cc/Mn` + `Lo` fillers, but `U+2800` (Braille
  blank) is category `So`, one category beyond the strip; a wholly-unfalsified
  record padded with it validates zero-error and reaches `READY FOR`.

Both were independently reproduced this session. RD-67 names the mechanism
for the third round running: *"a repair closes the named instance and
restates the result as a class property the machinery does not hold."* And
RD-68 f3 found — confirmed here — that **this session's own v2.4 delta
claimed a mutation-test (the `Mn` strip) it had not performed**; that false
claim is corrected by erratum at its source. The full disposition of all nine
v2.4 findings is
`../contracts/candidates/round-2026-08h/reviews/DISPOSITION-REGISTER.md`; the
raws are `RD-67-launch-policy-v2.4-RAW.md` and
`RD-68-launch-machinery-v2.4-RAW.md`. Tracked as `syzygy-6j8`, which stays
open.

Both reviewers are the **same model family as the corpus authors**, so
under the charter each supports repair and neither is the formal launch
administration. Raw bytes:
`../contracts/candidates/round-2026-08f/reviews/RD-47-launch-record-schema-RAW.md`
and `…/RD-48-launch-policy-v2.0-RAW.md`; the repair account, including
which findings are open and why, is that directory's
`DISPOSITION-REGISTER.md`.

**What they found, in one line each.** RD-48: **no readiness question,
row-level verdict word, or trend column was dropped, renamed, or made
unreachable** — the weakening question the charter asked is answered *no*.
It nonetheless found two structural discrepancies: the *computed* formula
carries a sixth core conjunct that §4 does not state (a strengthening,
grounded in §3's E3 rule, but not a term the instrument carries), and the
gate-level verdict word `NOT READY` has no home in §1–§8 although the tool
emits it. RD-47 found five material defects in the validator's decision
path, of which the load-bearing one is that the schema audit never requires
an object schema to close, so deleting a single `additionalProperties`
re-opens the claimed-verdict route the v2.0 design rests on.

**Those v2.0 findings were repaired at v2.1, whose own reviews then returned
`REVISE`, repaired in turn at v2.2 (`REVISE`), v2.3 (`REVISE`), and the
owner-authorized structural v2.4, whose reviews (RD-67/RD-68) returned
`REVISE` on 2026-08-16.** What has never happened, across five versions and
ten reviews, is a review that returned anything other than `REVISE`.

## Known residuals

Carried from the delta's disclosed limits — each measured, none
generalized:

1. The validator reads the instrument's own §8 prose in **one** place, to
   bind E4's fixed cases. Bounded and fail-closed, and disclosed rather
   than claimed absent.
2. The JSON Schema interpreter is a documented **subset**. Its safety
   property is that it rejects any keyword it does not implement; it is not
   the reference implementation.
3. Presence tests on free-text fields are **content-blind** by design. A
   reviewer who writes a plausible false evidence quote defeats this tool,
   and no version of it has claimed otherwise.
4. **No administration has been performed under any v2.x version.** The
   verdict path is fixture-proven, not field-proven. The only administration
   on record anywhere is the 2026-08-09 pilot, at v1.3, which returned
   `GATE VERDICT: NOT READY`.
5. F5 (assurance independence) is **not** a conjunct of the formula. Every
   administration so far has been by the corpus authors' model family.
   Promoting F5 to a conjunct is an owner option — see below.

## Your options

> **Arm (c) was ruled 2026-08-16; v2.4 is the structural repair, and its
> pair RD-67/RD-68 has now reported — both `REVISE`, the fifth consecutive
> pair.** The decision **returns to you**, refreshed with that evidence.
> Arm (c)'s own reasoning applies: a fifth `REVISE` is *"itself further
> evidence on convergence, to be weighed against (a) rather than absorbed."*
> The new evidence has a specific shape — the one genuinely structural repair
> (the mechanical forgery sweep) held and no live forgery exists in v2.4's
> bytes, but the two class defects that got *instance* patches this round both
> recurred as fresh BLOCKING false-`READY` paths (RD-67 f1, RD-68 f1). The
> arms below carry `[Observed]` status as of the v2.4 verdicts.

**(a) Approve v2.4 as process policy, residuals disclosed.** This now means
approving bytes whose independent reading returned `REVISE` — with **two
demonstrated false-`READY` paths** (an abbreviated-commit schema read, and a
`So`-category invisible), both bounded and both listed rather than hidden. A
lawful owner choice whose cost is stated plainly: the standard a formal
administration runs under would be one two known holes are documented in. The
holes are not in the launch-scope parameters or the questions — they are in
the validator's guarding of them — so an administration could still be run and
its result read with the residuals in hand. Weigh this against the fact that
five rounds have not driven the `REVISE` count to zero.

**(b) Approve v2.4 with F5 promoted to a conjunct.** Same as (a), plus: a
`Not met` F5 blocks a READY verdict. This would block a pass on any
administration run by this corpus's own model family — the strictest
available reading of assurance independence, and a real constraint on who
can administer the gate. It does **not** close the two false-`READY` paths;
it constrains who may administer, not what the validator guards.

**(c-again) Authorize a bounded v2.5 repair, then re-review.** Both blocking
findings are bounded and few-line repairable *if done structurally* — bind the
schema read to the schema's own `^[0-9a-f]{7,40}$` pattern (or narrow the
schema to 40 hex so the two agree by construction), and handle invisibles by
an **allowlist of visible substance** rather than a category blocklist that
the next unlisted category defeats. The case *for*: the structural approach
demonstrably worked where it was actually applied (the forgery sweep held).
The case *against*: this is a sixth cycle, and arm (c)'s own reasoning warns
that treating each `REVISE` as an automatic next round is what the owner
reserved this judgment to avoid. If chosen, it is a fresh owner work
authorization, not a standing one — the session will not loop to v2.5 without
it.

**(c) [ruled and completed] Authorize one more repair round (v2.4), then
re-review.** **⇒ Owner ruling 2026-08-16: this arm was chosen, and the round
is now complete.** The eleven open v2.3 findings were repaired with RD-66's
structural fixtures at the core, a v2.4 semantic delta written, and a
fresh-context re-review dispatched. The owner weighed the fourth `REVISE`
under this arm — rather than absorbing it as an automatic round — and
authorized the cycle because RD-66 handed over a *structural* fix, not another
instance patch: drive the forgery test through **every** schema-declared
string field mechanically. **The outcome (RD-67/RD-68, both `REVISE`, above):
that one structural fix held and no live forgery exists in v2.4's bytes, but
the two class defects that were instance-patched this round recurred.** The
standing risk this arm named — *"a class defect resurfaces at a site the v2.4
fixtures again do not enumerate"* — is exactly what landed. That is why the
returning decision is (a)/(b)/(d) or a **freshly-authorized** (c-again), never
an automatic next round.

*(The observable history that arm (c) weighed:* **the review pair had been
taken four times and returned `REVISE` all four.** Earlier rounds' findings
were narrower each time — v2.2's were confined to v2.2's own additions — but
the v2.3 pair broke that trend: RD-66's blocking finding is the RD-47 f2 /
RD-56 f2 / RD-62 f1 forgery class reproduced at a new address, and RD-65's
finding 3 is RD-61 f1's eligible-`READY FOR` outcome surviving at a new
address. This packet said, before the pair ran, that "if it returns `REVISE`
a fourth time, that is itself the answer to whether this instrument
converges, and it should be weighed against arm (a) rather than absorbed as
another round." That fourth `REVISE` landed, the owner weighed it, and ruled
(c) — the structural fix that targets the recurrence directly. The session
did not pre-empt that choice; the repair followed the ruling, not the other
way round.)*

**(d) Decline.** The gate stays a candidate. Administrations remain
evidence you may weigh; no formal administration can be said to have been
run under approved policy, and the readiness standard's "the launch-gate
instrument is owner-approved" conjunct stays unsatisfied. *(That conjunct is
stated without a version number deliberately — naming one here is how this
page came to ask for v2.0 two versions after v2.0.)*

## The lawful transaction

There is no ceremony phrase for this decision and none is needed — it is a
recorded owner decision, not a digest-binding act. To approve, record in
this file, dated and signed in your own words:

```text
APPROVED — launch-gate as process policy, at the version whose digest is below
instrument sha256: <the digest you verified>
schema sha256:     <the digest you verified>
F5 promoted to a conjunct: yes / no
```

Then the queue row P-34 closes, and the formal administration becomes
runnable — by a reviewer outside this corpus's model family, or a human,
which is a requirement of the instrument and not of this packet.

## Earliest required gate

Before the **formal launch administration**. Not before the Wave A or Wave
B acts: the contract acts do not depend on this policy, and this policy
does not gate them.
