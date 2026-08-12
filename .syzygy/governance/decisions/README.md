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
| **Has the owner decided this?** | the **recorded decisions** below | A few things are recorded. Most are not |
| **Has an act been performed?** | `ACCEPTANCE-ACT-RECORD.md` | **No.** The file does not exist, and that absence is correct |
| **Which decisions are pending?** | [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md) | 31 open rows. Each links a bounded packet |
| **Where is the history?** | [`launch-gate/HISTORY.md`](launch-gate/HISTORY.md), and the round trees under `contracts/candidates/` | Deliberately off the default path |

A **decision** is recorded prose the owner writes. An **act** is a formal
transaction with a ceremony phrase and a digest-bound argument. They are not
the same thing, and this directory holds both kinds of record. See
[`PROCESS-GLOSSARY.md`](../../../PROCESS-GLOSSARY.md).

## 1. Recorded decisions — binding

These carry rulings the owner has actually made.

| File | Holds |
|---|---|
| [`SURFACE-DECISION-RECORD.md`](SURFACE-DECISION-RECORD.md) | **SDR-1…33** — the standing body of prior owner rulings. The largest single source of settled ground |
| [`OWNER-ANSWERS-2026-08-01.md`](OWNER-ANSWERS-2026-08-01.md) | The owner's answers to the 2026-08-01 question set |
| [`DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`](DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md) | Doctrine amendment **D1**, in force |

Doctrine itself (VIS-1…7, SEC-1…5) is adopted and lives in
[`../doctrine/`](../doctrine/), not here.

## 2. Owner acts — none performed

```text
ACCEPTANCE-ACT-RECORD.md      does not exist
```

**Its absence is the point.** It is created by the first act, so its presence
would mean an act had been performed. Thirteen acts are prepared and open;
none has fired. The acts themselves — their exact phrases and arguments — are
owned by
[`../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`](../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md),
never by this directory and never by this page.

## 3. Pending decisions — one bounded packet each

The queue is [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md). The
launch-critical rows each have a prepared packet here:

| `P-nn` | Question | Packet |
|---|---|---|
| **P-33** | Where do accepted contract modules and their companions install? | [`WAVE-A-INSTALL-SHAPE-DECISION.md`](WAVE-A-INSTALL-SHAPE-DECISION.md) |
| **P-34** | Is the launch-gate instrument owner-approved process policy? | [`LAUNCH-GATE-AUTHORITY-DECISION.md`](LAUNCH-GATE-AUTHORITY-DECISION.md) |
| **P-35** | What are the project's operating constraints? | [`PROJECT-OPERATING-CONSTRAINTS-DECISION.md`](PROJECT-OPERATING-CONSTRAINTS-DECISION.md) |
| **P-36** | `Unknown` versus `Gap` — one word or two? | [`UNKNOWNS-AND-GAPS-DECISION.md`](UNKNOWNS-AND-GAPS-DECISION.md) |
| **P-37** | Which project-shape facets exist, and who owns the vocabulary? | [`PROJECT-SHAPE-FACETS-DECISION.md`](PROJECT-SHAPE-FACETS-DECISION.md) |
| **P-38** | Human entry point and per-repository discoverability | [`HUMAN-ENTRY-DECISION.md`](HUMAN-ENTRY-DECISION.md) |
| **P-39** | Which OpenSpec form and version? | [`OPENSPEC-FORM-AND-VERSION-DECISION.md`](OPENSPEC-FORM-AND-VERSION-DECISION.md) |
| **P-40** | One specification per what? | [`SPECIFICATION-GRANULARITY-DECISION.md`](SPECIFICATION-GRANULARITY-DECISION.md) |
| **P-41** | The specification-acceptance craft amendment | [`SPECIFICATION-ACCEPTANCE-DECISION.md`](SPECIFICATION-ACCEPTANCE-DECISION.md) |
| **P-12** | The knowledge-hygiene craft policy | [`KNOWLEDGE-HYGIENE-DECISION.md`](KNOWLEDGE-HYGIENE-DECISION.md) |
| **P-14** | Which license? | [`LICENSE-DECISION-PACKET.md`](LICENSE-DECISION-PACKET.md) |

Rows without a packet in this table are queue entries only, and the register
row is the whole of what exists for them.

**Not every pending row is ready to be ruled.** Some need research first,
some are waiting on a review, and some are acts rather than decisions. The
grouping is
[`../contracts/candidates/round-2026-08g/CAPABILITY-1-OWNER-DECISION-INDEX.md`](../contracts/candidates/round-2026-08g/CAPABILITY-1-OWNER-DECISION-INDEX.md).

## 4. History — kept, and off the default path

| Where | Holds |
|---|---|
| [`launch-gate/HISTORY.md`](launch-gate/HISTORY.md) | The launch-gate repair chain, v1.3 → v2.0. Thirteen versions, thirteen reviews |
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
