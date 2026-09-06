# Owner packet — the PWB improvement cycle, reported before the walkthrough

> **Pending. This packet decides nothing and adopts nothing.** It reports
> the state of the Polaris project-wide Butlers (PWB) improvement cycle as
> far as it can be reported before you perform the cold-open walkthrough,
> and it gathers every owner decision that cycle has accumulated so you can
> answer them in one reply. Register rows: **P-60 … P-65** in
> [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md). None depends
> on another; P-60 and P-61 are the two that keep the walkthrough not ready.
>
> Written 2026-09-06 for task 5.3 of the signed PWB task list (bead
> `syzygy-1z3.25`). Task 5.3 asks for the report *after* the walkthrough
> (task 4.6), which has not happened; so this is the accumulated report and
> decision packet before it, and task 5.3 stays open until the walkthrough
> outcome can be added. Nothing here changes any accepted artifact.

## Where the cycle stands, in plain words

The cycle was: an independent review of the live implementation at its
exact head (fifteen findings, 2026-09-05), repairs of only those findings,
and an independent confirmation of the repairs. That has run twice. The
first confirmation (gen-1) found all fifteen repaired and raised nine
residues; the second (gen-2) found the three residues that needed code
repaired and raised four small test-rigor items that ordinary beads now
carry. Both verdicts are **CONFIRM WITH EXCEPTIONS**, copied exactly from
the raw reviews; no third confirmation is needed. The records:

- `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md` (the fifteen findings)
- `docs/reviews/2026-09-06-pwb-recovery-reconciliation-packet.md` and its raw review `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md`
- `docs/reviews/2026-09-06-pwb-recovery-reconciliation-gen2-packet.md` and its raw review `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN2-RAW.md`
- the mutation and fresh-clone evidence under `docs/evidence/`, listed with digests in each packet's evidence index

**Exact revisions.** The confirmed code head is Syzygy commit `9b28663`
(the surface version and evaluation identity it serves are recorded in the
gen-2 packet); the commits on `main` after it are documentation only. The
observed Butlers revision at both the retained demo and the gen-2 review is
`ec8b1f6`. [Observed]

**The walkthrough.** On 2026-09-05 you began the cold-open walkthrough on
the pre-repair head and stopped because Polaris was unusable. No execution
record, judgment or act exists, so the walkthrough is Unknown, never met.
It is not re-offered yet: the mechanical readiness check still says *not
ready* on three limbs, all caused by Butlers content, none by Syzygy code
(P-60 and P-61 below). [Observed, from the fresh-clone demo record]

**Remaining Unknowns, all disclosed on the page.** The V1 whole-source
claim (P-60); the roster and topology denominators (P-61); the whole-shape
claim, because Spec and Spine has no index (P-62); and the walkthrough
itself. Nothing is rendered green that the evidence does not support.

**Amendment gates held open.** No amendment packet is prepared. Each arm
below that names an act would be a new act with its own packet and review;
none has been drafted, and the two signed amendments of 2026-09-05 are not
touched.

**External actions not taken.** No Butlers file was written; no act,
policy, registry or consent changed; no tailnet or serving configuration
changed; the long-running daemon you started earlier was not restarted, so
its revisions must be refreshed before its address is relied on; nothing was
released or exposed beyond the bounded POC.

---

## P-60 — The Butlers V1 page does not parse

**What is there.** One line of the Butlers V1 statement uses a colon where
the signed grammar requires a dash. The parser refuses the whole source, so
the V1 scope and V1 success statements are Unknown, and the readiness check
reports them unbacked.

**Why it matters.** This is one of the two things keeping the walkthrough
not ready. Every other reading of Butlers is unaffected.

**The arms.**

- **(a)** Change that one line in Butlers to the dash form. A Butlers
  commit by you; Syzygy changes nothing.
- **(b)** Amend the grammar to admit the colon form, by a new truth-policy
  act.
- **(c)** Leave it. The V1 claims stay Unknown and the walkthrough stays not
  ready on this limb.

**Recommendation: (a).** One character in the governed project, no act, and
the grammar keeps its single signed form.

**Default if unanswered:** the V1 claims stay Unknown; the walkthrough is
not re-offered on this limb.

---

## P-61 — Roster and topology content is withheld or unparsed

**What is there.** Seven of the thirteen butler.toml roster files and one
Lay and Land page are withheld as active content: the secret policy has no
inert-context profile for TOML, so the files are counted but never read.
The topology table in the components page does not match the table grammar.
Together they empty the catalog and topology populations and leave the
roster denominator Unknown; the readiness check reports two limbs.

**Why it matters.** This is the other thing keeping the walkthrough not
ready, and it is a policy trade-off: the withholding is the secret policy
doing what it was signed to do.

**The arms.**

- **(a)** Repair the Butlers side: make the topology table match the
  grammar, and move the roster declarations the shape needs out of TOML
  into the inert page form. Butlers commits by you; no Syzygy act.
- **(b)** Extend the secret policy's inert-context profile to TOML by a new
  policy act, so those files are read. This widens what Syzygy reads.
- **(c)** Accept a roster denominator that stays Unknown, and re-offer the
  walkthrough with that Unknown disclosed once P-60 lands.

**Recommendation: (a) for the topology table, (c) for the roster.** The
table is a grammar mismatch and cheap to fix. Widening the policy to read
configuration files is a security posture change that deserves its own act
if you want it; until then an honest Unknown is the intended behaviour.

**Default if unanswered:** both populations stay empty or Unknown; the
walkthrough is not re-offered on these limbs.

---

## P-62 — Spec and Spine has no index

**What is there.** The Butlers root index points Spec and Spine at its
openspec directory, and that directory has no index page. The pillar is
recorded as index-missing, so the whole-shape claim is Unknown. Since the
gen-2 repair the page says exactly this, names the missing index path and
offers the route.

**Why it matters.** It does not block the walkthrough, but the top claim on
the page stays Unknown until one of the arms happens.

**The arms.**

- **(a)** Add the index page in Butlers. A Butlers commit by you.
- **(b)** Amend the discovery rule by act so a home without an index counts
  as declared without one.
- **(c)** Keep the permanent Unknown, now that the page explains it.

**Recommendation: (a).** It matches the other four pillars and needs no
act.

**Default if unanswered:** the whole-shape claim stays Unknown, with its
cause on the page.

---

## P-63 — The human page is close to its byte ceiling

**What is there.** The registry caps the human page at two megabytes. After
the gen-2 disclosure lines the page has about 49 kilobytes of headroom
directly and about 44 kilobytes through the tailnet mount, 2.1 percent of
the ceiling. [Observed at Butlers `ec8b1f6`]

**Why it matters.** Butlers grows. When the page crosses the ceiling the
limit ledger records a breach and the page degrades honestly, but the
walkthrough would then be read on a degraded page.

**The arms.**

- **(a)** Direct a presentation trim, implementation only: the exhaustive
  inventories that the 2026-09-05 review already asked to collapse are the
  obvious candidate. No act.
- **(b)** Raise the ceiling by a registry amendment act.
- **(c)** Leave it and let the ledger report the breach when it comes.

**Recommendation: (a), then (b) only if a trim cannot buy enough.** A trim
serves the reader as well as the ceiling and needs no act.

**Default if unanswered:** the page keeps serving until it crosses the
ceiling, then reports the breach.

---

## P-64 — Say in the record guidance that the exact-source route is lawful

**What is there.** The gen-1 review confirmed that following an *Exact
source* link during the walkthrough is already a lawful traversal under
PWB-REQ-021 and is in the schedule. The walkthrough packet's guidance does
not say so in your words, and the reviewer asked that it should.

**The arms.**

- **(a)** Give one sentence, in your words, that following the exact-source
  link is a permitted step; an agent adds it to the candidate walkthrough
  packet, which binds nothing.
- **(b)** Leave the guidance as it is.

**Recommendation: (a).** It is one sentence and removes a doubt the reader
would otherwise carry into the walkthrough.

**Default if unanswered:** the route stays lawful and unmentioned.

---

## P-65 — Close the repair epic now, or hold it for the test-rigor beads

**What is there.** The gen-2 review left four small items: three places
where a new test could be tricked by a wrong route or a filtered pillar
(beads `syzygy-1z3.24.10`), one stale live-test pin (`syzygy-1z3.24.11`),
and a note that one retained mutation record cannot be re-run from its
bytes (now a guardrail). None changes what the page says today. The
walkthrough bead depends on the repair epic `syzygy-1z3.24`, so the epic's
state decides whether the walkthrough can be offered at all.

**The arms.**

- **(a)** Close the epic now, with those beads carried as ordinary work
  under the POC backlog.
- **(b)** Hold the epic open until the beads close with their own rule-6
  evidence.

**Recommendation: (a).** The reviewer recommends it too; the repairs are
independently confirmed and the residue is test rigor, not behaviour.

**Default if unanswered:** the epic stays open and the walkthrough stays
formally blocked on it even after P-60 and P-61 land.

> **Updated 2026-09-06, later the same day.** Both beads this question
> weighed have closed: the three gates now have isolating counterexamples
> and the live test is re-pinned, with a fragment-bearing rule-6 record
> (`docs/evidence/pwb-recon-gen2-gate-mutation-run-2026-09-06.json`, 6 of
> 6 killed). Arms (a) and (b) therefore converge on the same state; the
> ruling to close the epic is still the owner's, and the text above is kept
> as written.

---

## What was repaired without a decision

The state-(1) trust-gap sentence that PWB-REQ-005 requires on both surfaces
was, at gen-1, visible only to machine readers. Gen-2 repaired it; the page
now renders it once per authority on both mounts, confirmed live. No
decision is needed; it is listed so the six gen-1 items are all accounted
for.

## What happens after your reply

Butlers edits are yours to make; when P-60 and P-61 have landed in Butlers,
an agent re-runs the fresh-clone demo, and if readiness reports *ready* the
walkthrough is re-offered from `contracts/candidates/pwb-walkthrough/`.
Any arm that names an act gets its own packet first. Task 5.3 is then
completed with the walkthrough outcome added to this report.
