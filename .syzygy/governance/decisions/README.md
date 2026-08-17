# Decisions — what lives here, and which question each file answers

> **Navigation, never authority.** This page routes; it decides nothing and
> records nothing. Every file it names owns its own content, and where this
> page disagrees with one of them, **that file wins and this page is stale.**
>
> Written 2026-08-13 to close review finding RD-50 f7: `README.md` sends a
> reader to this directory as a destination, and the directory had no door.

## The four questions this directory answers

| You want to know | Ask | Short answer today |
|---|---|---|
| **Has the owner decided this?** | the **recorded decisions** below | Doctrine, craft, SDR-1…37, and the 2026-08-16 rulings are recorded. The rest is not |
| **Has an act been performed?** | `ACCEPTANCE-ACT-RECORD.md` | **Yes — four, all 2026-08-17:** Wave A, Wave B, and craft acts 6 + 7 (CC-SPEC, CC-IMPACT). The record file exists since the first act and owns every performed act |
| **Which decisions are pending?** | [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md) | **20** rows in the open section, plus **5** open acceptance-act rows *(measured 2026-08-17, after the acts, by the predicate the generators use: every `## ` section except those headed `Resolved`, minus any row whose final cell leads with `**Executed.**`; P-1's row stays open for the deferred C/D waves)*. The launch-critical ones link a bounded packet; the rest are queue entries only |
| **Which decisions were resolved, and how?** | [`DECISION-HISTORY.md`](DECISION-HISTORY.md) | The resolved rows — the nine 2026-08-16 rulings and the 2026-08-17 act dispositions (P-41/P-42 executed, P-22/P-28 ratified) — and the register's chronology |
| **Where is the history?** | [`launch-gate/HISTORY.md`](launch-gate/HISTORY.md), [`DECISION-HISTORY.md`](DECISION-HISTORY.md), and the round trees under `contracts/candidates/` | Deliberately off the default path |

A **decision** is recorded prose the owner writes. An **act** is a formal
transaction with a ceremony phrase and a digest-bound argument. They are not
the same thing, and this directory holds both kinds of record. See
[`PROCESS-GLOSSARY.md`](../../../PROCESS-GLOSSARY.md).

## 1. Recorded decisions — binding

These carry rulings the owner has actually made.

| File | Holds |
|---|---|
| [`SURFACE-DECISION-RECORD.md`](SURFACE-DECISION-RECORD.md) | **SDR-1…37** — the standing body of prior owner rulings (SDR-34…37 record the 2026-08-16 P-31/P-36/P-37/P-40 rulings). The largest single source of settled ground |
| [`OWNER-ANSWERS-2026-08-01.md`](OWNER-ANSWERS-2026-08-01.md) | The owner's answers to the 2026-08-01 question set |
| [`DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`](DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md) | Doctrine amendment **D1**, in force |
| [`WAVE-A-INSTALL-SHAPE-DECISION.md`](WAVE-A-INSTALL-SHAPE-DECISION.md) | **P-33 ruled 2026-08-16** — install shape (M), recorded in the packet's own template |
| [`LAUNCH-GATE-AUTHORITY-DECISION.md`](LAUNCH-GATE-AUTHORITY-DECISION.md) | **P-34 ruled 2026-08-16** — launch-gate v2.4 approved as process policy, arm (a), residuals disclosed |
| [`PROJECT-OPERATING-CONSTRAINTS-DECISION.md`](PROJECT-OPERATING-CONSTRAINTS-DECISION.md) | **P-35 ruled 2026-08-16** — the operating-constraints table, Unknowns kept |
| [`HUMAN-ENTRY-DECISION.md`](HUMAN-ENTRY-DECISION.md) | **P-38 ruled 2026-08-16** — human entry as drafted (option a) |
| `../policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` `openspec` block | **P-39 ruled 2026-08-16** — OpenSpec pinned at 1.9.0 |

Doctrine itself (VIS-1…7, SEC-1…5) is adopted and lives in
[`../doctrine/`](../doctrine/), not here.

## 2. Owner acts — four performed 2026-08-17

```text
ACCEPTANCE-ACT-RECORD.md      exists — created by the Wave A act, 2026-08-17
```

[`ACCEPTANCE-ACT-RECORD.md`](ACCEPTANCE-ACT-RECORD.md) owns the four acts
performed 2026-08-17: Wave A, then Wave B, then craft acts 6 + 7 (CC-SPEC
and CC-IMPACT, one sitting). Entries are appended, never edited. As of
2026-08-17, nine offered acts remain unperformed. The acts themselves — their exact phrases and
arguments — are owned by
[`../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md),
never by this directory and never by this page.

## 3. Pending decisions — one bounded packet each

The queue is [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md). The
launch-critical rows each have a prepared packet here:

| `P-nn` | Question | Packet |
|---|---|---|
| **P-12** | The knowledge-hygiene craft policy | [`KNOWLEDGE-HYGIENE-DECISION.md`](KNOWLEDGE-HYGIENE-DECISION.md) |
| **P-14** | Which license? | [`LICENSE-DECISION-PACKET.md`](LICENSE-DECISION-PACKET.md) |

Packets whose question the owner has since ruled or executed (P-41's
`SPECIFICATION-ACCEPTANCE-DECISION.md` and P-42's
`SHAPE-TO-SPEC-IMPACT-DECISION.md` — acts 6 and 7 performed 2026-08-17 —
P-31's
`MERGED-UNRECONCILED-DECISION.md`, P-36's `UNKNOWNS-AND-GAPS-DECISION.md`,
P-37's `PROJECT-SHAPE-FACETS-DECISION.md`, P-39's
`OPENSPEC-FORM-AND-VERSION-DECISION.md`, P-40's
`SPECIFICATION-GRANULARITY-DECISION.md`, and the four files listed under
"Recorded decisions" above) remain in this directory as the record or the
context of their ruling — see
[`DECISION-HISTORY.md`](DECISION-HISTORY.md) for what each ruling was.

Rows without a packet in this table are queue entries only, and the register
row is the whole of what exists for them.

## 4. History — kept, and off the default path

| Where | Holds |
|---|---|
| [`DECISION-HISTORY.md`](DECISION-HISTORY.md) | Resolved decision rows and the register's as-of chronology |
| [`launch-gate/HISTORY.md`](launch-gate/HISTORY.md) | The launch-gate repair chain |
| [`launch-gate/TREND-LOG.md`](launch-gate/TREND-LOG.md) | One row per administration |
| [`PROCESS-LESSONS.md`](PROCESS-LESSONS.md) | The incidents behind the verification rules. **Read before writing or trusting a check** |
| `../contracts/candidates/round-*/` | Each pass's reports and its raw review lane |

Raw review bytes are **preserved and never edited**, and are never default
context. You should be able to make every decision above without opening any
of them.

## What this directory is not

It is not a changelog, not a backlog, and not a place to record work. Open
questions belong in the register as owner decisions; process housekeeping
belongs in `bd`.

---

### A note on this file's own lawfulness

Candidate clause **RFC3-15** says the `decisions/` category holds *"Recorded
owner decisions: adoptions, dismissals (reason + expiry), adjudications,
consent records (RFC3-7), overrules"* — **exclusively**. This README is
navigation, not a recorded owner decision, so under a strict reading of that
clause it does not belong here.

It is written anyway, on explicit owner instruction, and the tension is
recorded rather than hidden. Two facts bear on it: RFC3-15 is a **candidate**
and binds nothing today, and the tree already contains `doctrine/README.md`
and `launch-gate/README.md` on the same footing.

**This is the same question as P-33**, at smaller scale — whether a
constitutional category may hold a navigation lane beside the content it
names. Whatever the owner rules for `contracts/` should govern this file too,
and if the ruling excludes navigation lanes, this file moves. That
consequence is recorded in the P-33 analysis so the ruling is made knowing it.
