# RB-1 — Fresh engineer / public-clone reader review (RAW)

## Provenance

**Who I am.** A fresh-context reviewer instantiated with no knowledge of this
project's history, authoring conversations, or team. I was given the role of a
technically competent engineer who has just cloned the repository and opens
`README.md`. I sought no authoring context and was given none.

**Constraint compliance.**

- I read **nothing** under `_bootstrap/`. Verified: no tool call in this
  session targeted that tree.
- I read **nothing** under
  `.syzygy/governance/contracts/candidates/round-2026-08/` except to write this
  file. Two grep sweeps returned paths inside that directory in their output; I
  filtered those results out (`| grep -v round-2026-08`) and did not open any
  of the files. One exception I must disclose: `scripts/check_governance.py`
  output printed *filenames and single-line excerpts* from `round-2026-08/`
  (the CG-1d/CG-2b allowlists). I did not act on those excerpts and no finding
  below rests on them.
- I followed only links and paths the documents themselves gave me.

**What I read, in order.**

1. `README.md` (full) — the entry point.
2. `wc -w` on the five root documents; `ls -a`; `git ls-files`.
3. `.syzygy/intent/OVERVIEW.md` (full) — README start-here #1.
4. `PROJECT-STATUS.md` (full) — README start-here #3.
5. `.syzygy/governance/doctrine/vision.md` (full) — README start-here #2.
6. `.syzygy/governance/doctrine/README.md` (full) — reached from the doctrine
   directory link in the README authority table.
7. `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` (full) — #6.
8. `CONTRIBUTING.md` (full) — #7. `SECURITY.md` (full) — #8.
9. `.syzygy/governance/contracts/candidates/README.md` (full) — #4.
10. `.syzygy/governance/policies/craft-and-care/README.md`,
    `engineering-bar.md` banner, `INSTALL-RECORD.md` head — #5.
11. `.syzygy/map/topology-candidates/README.md`, `BUNDLE-MANIFEST.md`.
12. `policy-candidates/TERM-REGISTRY.md` (head).
13. `.github/workflows/governance-docs.yml`.
14. Ran the four validation commands `PROJECT-STATUS.md` §"How to verify this
    page" prescribes, plus the `sha256sum` block in `candidates/README.md`
    §Verify and the one in `BUNDLE-MANIFEST.md`.

**Repository state reviewed.** Working tree at `HEAD = 9e6f2f7`, 2026-08-05.
This matters — see F2.

---

## Findings

### F1 — BLOCKING. The documented verification FAILs, and the status page says there are no blocking defects.

`PROJECT-STATUS.md:50-53` states:

> ## Known blocking defects
> None known at this revision.

Six lines later (`PROJECT-STATUS.md:62-69`) it tells me how to verify the page.
I ran exactly those commands. `scripts/check_governance.py` reports:

```
FAIL  CG-7b  act-1 argument matches the manifest — 1 argument examined, 1 finding
        .syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md
        offers 08793ddf70f3… but the manifest now hashes to 5c4d67983541…
        — the act would bind a package that no longer exists
```

Real exit code **1** (I captured it without a pipe; a naive `| tail` masks it).

I confirmed this independently, by hand, using the procedure
`candidates/README.md:41-47` gives:

```
$ sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt      → all 32 modules OK
$ sha256sum ACTIVE-CONTRACT-MANIFEST.txt
  5c4d6798354135bd860b3a2637c282f535c519bdd1a3cbab67d7555367af6caa
```

The acceptance record offers the stale digest in **four** places:
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15` (the ceremony row
itself), `:118`, `:213`, `:215`.

Consequences a fresh reader can see:

1. The single most consequential open act in the project — act 1, gate 4 of 12
   — currently has a ceremony phrase that **cannot be validly performed**. If
   the owner typed the phrase as written, they would bind a package digest that
   does not exist.
2. `.github/workflows/governance-docs.yml:31-33` runs `check_governance.py` on
   every push to `main`. CI is therefore **red on `main`** today, and nothing in
   the front door says so.
3. `PROJECT-STATUS.md:50` asserts a clean bill in the same file that hands me
   the command proving otherwise. That is precisely the "confident state
   substituted for a real one" failure `VIS-1` and `VIS-2` exist to forbid,
   committed by the project's own status page.

Severity is blocking because the defect is in the gate the whole repository is
organized around, and because the project's own currency discipline
(`PROJECT-STATUS.md:6-8`, "regenerated or corrected in the same change whenever
a gate fires") is what should have caught it.

**Note on the manifest:** the 32 module digests are internally consistent
(32/32 OK). The mismatch is only between the manifest's own sha256 and the
digest quoted in the acceptance record — so the fix is a re-quote plus a
digest-binding re-review, not a corpus repair. That distinction is legible to
me only because I ran both commands; neither document states it.

---

### F2 — BLOCKING (as a clone). Six of the README's ten start-here targets do not exist at `HEAD`.

I am charged with reading this as a public clone. At `HEAD 9e6f2f7`,
`git ls-files` returns **37 tracked files**. The working tree I was given
contains 177. The difference is the entire front door and most of what it
points at:

| README target | line | tracked at HEAD? |
|---|---|---|
| `PROJECT-STATUS.md` | 12, 90 | **UNTRACKED** |
| `CONTRIBUTING.md` | 97, 118 | **UNTRACKED** |
| `SECURITY.md` | 98 | **UNTRACKED** |
| `.syzygy/governance/contracts/candidates/` | 76, 91 | **UNTRACKED** |
| `.syzygy/map/topology-candidates/` | 77 | **UNTRACKED** |
| `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` | 116 | **UNTRACKED** |
| `.syzygy/intent/OVERVIEW.md` | 86 | tracked |
| `.syzygy/governance/doctrine/vision.md` | 88 | tracked |
| `PENDING-OWNER-DECISIONS.md` | 95 | tracked |

`README.md` itself is tracked but **modified** — a clone gets a *different*
README from the one I reviewed. `scripts/` and `.github/` are untracked
entirely, so the CI workflow and `check_governance.py` are not in a clone
either.

This is a commit-state defect, not a prose defect, and I flag it as such: the
authored content is present in the working tree and I reviewed it there.
But the charge is public-clone legibility, and today a real clone gets a front
door whose "start here" list is 60% 404s. The project has itself made this the
bar — `CONTRIBUTING.md:59-66`, "Public-clone validation is part of done… run
the validation commands in `PROJECT-STATUS.md`" — and in a clone at HEAD, all
four of those commands reference files that do not exist.

**What "done" requires:** the front door and everything it links must land in
one commit. A partial landing (README without `PROJECT-STATUS.md`, or the
authority table without `candidates/`) is strictly worse than the current
state, because it converts a small repo into a repo that lies about its own
contents.

---

### F3 — MATERIAL. The only clone-visible open-decision register is materially stale, and misdirects to `_bootstrap/`.

`PENDING-OWNER-DECISIONS.md` is README start-here #6 and self-describes
(`:3-10`) as the explicit, clone-visible open queue, "regenerated or corrected
in the same change whenever a listed decision is made." It carries
`As-of: 2026-08-04, HEAD adddc34` while `PROJECT-STATUS.md:3` is as-of
2026-08-05. Four of its sixteen rows now misdescribe the tree — I checked each:

- **P-6** (`:35`) says the retired phrase `ACCEPT FOUNDATIONAL RFCS` "survives
  inside the act-1 digest set (`rfcs/RFC-0003/governance-homes-and-owner-acts.md:87`)."
  Verified absent: `grep -rn "ACCEPT FOUNDATIONAL RFCS" candidates/rfcs/` → no
  hits. `check_governance.py` CG-2a agrees (166 files, 0 findings).
- **P-7** (`:36`) says "every canonical craft-policy file opens with 'this copy
  is the bootstrap-phase record' — false at the canonical home, inverting
  authority." Verified repaired: `craft-and-care/README.md:1` and
  `engineering-bar.md:1` now read "**This directory … is the canonical home of
  these policies.** The bootstrap-phase copy is preserved separately."
  CG-5 agrees (10 files, 0 findings).
- **P-8** (`:37`) says `INSTALL-RECORD.md:20` conditions craft binding on the
  retired phrase, "unsatisfiable as written." Verified repaired:
  `INSTALL-RECORD.md:22-25` now names `ACCEPT COMPACTED FOUNDATIONAL RFCS:
  <manifest digest>` and states the rev9 phrase "is retired and satisfies
  nothing."
- **P-9** (`:38`) says "candidate contracts, topology, acceptance record,
  validation scripts, and the owner-decision ledger are all founder-local."
  All five are now in the working tree under `.syzygy/` and `scripts/`.
- **P-11** (`:45`) lists installing "the public front door (README, AGENTS.md
  replacement, PROJECT-STATUS, CONTRIBUTING, SECURITY)" as pending — while I
  am reading all five of them.

Worse than staleness: five rows point *exclusively* into git-excluded
`_bootstrap/**` for their owning record — P-1…P-5 all cite
`_bootstrap/rfc-phase/final-prespec/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
(`:21-25`), and P-12/P-14/P-15 likewise. A tracked, readable copy of that
acceptance record sits at
`.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`.
So the register sends me to an unreadable path when a readable one exists two
directories away. P-14 does this for the license packet specifically, while
`README.md:116` correctly links the tracked
`.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md`. Two clone-visible
documents disagree about where the same record lives.

The file's own disclosure (`:12-15`) is honest about the `_bootstrap/` problem
in general. It does not save it: the disclosure explains *why* a pointer might
not resolve; it does not excuse pointing at a dead path when a live one exists.

`check_governance.py` CG-10 surfaces this as a WARN — "pending register as-of
reported… reported for human currency judgement, never auto-verified." That is
an honest design, but it means the staleness is invisible to anyone reading
only exit codes, and the register is nobody's automated responsibility.

---

### F4 — MATERIAL. Every pointer on the default path names the superseded D3 draft.

Two files exist:

```
213 lines  candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md
 78 lines  candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md
```

`…-D3.md:3-15` says it is a "**minimally revised** replacement for
`DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` (sha256 `30efb7c5…`)" and that
"**three defects were found in the original draft** … All three are repaired
below."

I then checked who points where. Every clone-visible pointer names the
**older, defective** file:

- `PROJECT-STATUS.md:27` (gate 8) → `…-DRAFT.md`
- `AGENTS.md` (pending-gates table, act 5) → `…-DRAFT.md`
- `candidates/README.md:31` (the layout table) → `…-DRAFT.md`
- `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:19` (the act-5 row itself)
  → "`DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`'s two verbatim insertions"
- `PENDING-OWNER-DECISIONS.md:25` (P-5) → the `_bootstrap/` copy of `…-DRAFT.md`

`grep -rn "BOUNDED-MISSION-D3"` across the clone-visible tree returns **zero**
citations outside `round-2026-08/`. The rev1 is an orphan.

Two failures compound here. First, the layout table in `candidates/README.md`
claims to enumerate the directory and omits a top-level file. Second, a reader
who does what the acceptance record tells them — read the act-5 subject before
the owner rules on it — reads the version its own successor says is defective.
Leaving the original "untouched at the owner's gate" (`…-D3.md:7-8`) is a
defensible archival choice; leaving it as the *only advertised* version is not.

---

### F5 — MATERIAL. The owner-approved engineering bar is not readable from a clone.

`PROJECT-STATUS.md:21` marks gate 2 ✅ **Approved**, and `README.md:75` lists
craft-and-care as start-here #5 under "Owner-approved (D2)". Opening it,
`craft-and-care/README.md:14-22`:

> This cluster **adopts the canonical engineering bar by reference**: the
> `th-engineering` skill package … is Syzygy's baseline engineering standard.
> [Observed — `~/.claude/skills/th-engineering/subskills/`…]
>
> The cluster **does not restate** the canonical bar. Every file below records
> only Syzygy-specific **overrides and additions**. Where a file is silent, the
> canonical bar applies unmodified.

`~/.claude/skills/…` is a path on one machine. As a fresh cloner I cannot read
it, and the cluster explicitly declines to restate it. So the substantive
majority of an authority the project marks **approved and binding-on-act** is
unavailable to me, and "where a file is silent, the canonical bar applies"
means I cannot even bound how much I am missing.

The `[Observed]` label is honest about provenance and does not help: an
`[Observed]` citation to an unreachable artifact is, from a clone, indistinguishable
from `[Unknown]`. `PENDING-OWNER-DECISIONS.md:38` (P-9) names this as "the
tier-3 engineering baseline is machine-local" — so it is known — but P-9's
other legs have been resolved into the tracked tree while this one has not,
and no clone-visible document says which of P-9's legs remain open.

---

### F6 — MATERIAL. Adopted doctrine's first substantive sentence cites a "README glossary" that does not exist.

`vision.md:16` — the opening line of the Thesis, the most-read sentence in
adopted doctrine:

> Syzygy (see README glossary) is a specification-driven software control plane…

and again at `vision.md:39` ("the public actuator toolchain (README glossary)")
and `v1.md:98` ("the public ai-bootstrap toolchain (README glossary)").

The root `README.md` has eight headings — Why it exists, The four experiences,
The core loop, What is authoritative here, Start here, What is not implemented,
License — and **no glossary**. `grep -i glossar README.md` → 0 hits. Verified
across all five root documents and `OVERVIEW.md`: 0 hits.

The intended target is almost certainly
`.syzygy/governance/doctrine/README.md:15`, "## Glossary (read first)", which
does define Syzygy, Owner, governed project, the two namespaces,
Polaris/Trajectory/Orrery, the substrate tools, and the rule identifiers. But
adopted doctrine says "README glossary", the reader is holding the README, and
the README does not point to the doctrine glossary either.

Concrete casualty: "the public actuator toolchain" (`vision.md:38-40`) and "the
public ai-bootstrap toolchain" (`v1.md:98`) are load-bearing scope terms — they
are how doctrine distinguishes owner-first from owner-only — and neither is
defined anywhere I could reach on the default path. `ai-bootstrap` appears
nowhere in README, OVERVIEW, or the doctrine glossary.

This is a `VIS-7` concern by its own terms ("every rendered internal
project-entity link resolves to its identified target"), and `VIS-3`'s
fresh-reader test is the mechanism that should have caught it.

---

### F7 — MATERIAL. `RFCn-m` clause identifiers are unexplained on the default reading path.

`OVERVIEW.md` is start-here #1 — the first document after the README, and the
document explicitly designed for a fresh reader ("what it is, in one reading").
Sweeping it for identifiers, a reader in the first ten minutes meets:

```
RFC1-21 RFC1-22 RFC2-3 RFC2-4 RFC2-15 RFC2-17…21 RFC3-3 RFC3-16(a)/(b)
RFC4-13 RFC5-25 RFC6-13 RFC7-3 RFC8-28 RFC10-1…16
```

— fourteen distinct clause-ID forms, plus `SDR §1–2` (`:77`), plus `D1`/`D2`/`D3`.

Nothing on the path `README → OVERVIEW → doctrine/README → vision` explains
that `RFCn-m` denotes clause *m* of `RFC-000n`. The doctrine glossary
(`doctrine/README.md:45-49`) explains `VIS-n`, `SEC-n`, and their disjointness
from `V0`/`V1` — and stops there. The only place the convention *is* stated is
`AGENTS.md` ("Cite by identifier — `VIS-2`, `SEC-4`, `SDR-9`, `CC-REV-3`,
`RFC10-9`. Identifiers are stable…"), which `README.md:100-101` explicitly
scopes to agents and labels "not project truth".

`OVERVIEW.md:157-183` (Layer 4) partially rescues this — it maps RFC-0001…0011
to their subjects — but it arrives *after* every clause citation and never
explains the hyphenated clause form. `RFC3-16` in particular is used three
times (`:3`, `:144`, and in the topology README) as the rule that "this stamp
is a self-declaration; effective status lives in the owner-act record" — a
genuinely important idea a fresh reader cannot look up, because they cannot
tell which file `RFC3-16` lives in.

The charge sets a target of ~10 foundational terms on the default path.
`OVERVIEW.md:86-88` self-reports ten ("desired / observed / execution state,
reconciliation work, kernel, surface, capability, Unknown, mission, owner") and
that count is fair for *prose* terms — the prose vocabulary is genuinely well
controlled. The identifier vocabulary is what blows the budget, and it is not
counted.

Related, minor: `OVERVIEW.md:88` says "the full vocabulary lives in the term
registry" with no link. `OVERVIEW.md:177` gives "term registry,
`contracts/candidates/policy-candidates/`" — a directory, not the file. The
file is `TERM-REGISTRY.md` (30 entries, 8,722 words, banner: "Status:
CANDIDATE. This file binds nothing.") — two hops and a guess from where the
term is first promised.

---

### F8 — MATERIAL. `verify_final_prespec.py` prints "PASS — all checks clean" directly beneath two unmet budgets.

Running the first command in `PROJECT-STATUS.md`'s verification block:

```
note: rfcs/RFC-0001-…md: 8353 words over the 7,000 ceiling — JUSTIFIED: …
note: total 99080 exceeds the 35–50k target band plus new RFCs;
      owner-facing justification required (charter)

PASS — all checks clean
```

The corpus is **~2× the top of its own declared target band**, and the script
says an owner-facing justification is *required* — i.e. owed and not yet
supplied. The summary line then says "all checks clean."

`check_governance.py` handles the same facts better: CG-8 reports them as a
WARN with all seven over-budget artifacts enumerated and an explicit
"report-only — §11.4 triggers are decomposition prompts, not failures".

`AGENTS.md` warns agents to "Read a check's *output*, not its exit code." Here
the trap is one level deeper: the output's own summary line is the misleading
part. For a project whose first rule is "comprehensible truth, never
comprehensible fiction," a green summary printed under an unmet, self-declared
budget is the wrong default. Either the note should suppress "clean," or the
line should read "PASS — 2 budget notes outstanding."

I am not asserting the corpus size is wrong; `RFC-0001`'s justification
(dictionary-shaped, 23% closed vocabulary, no honest split) reads plausibly.
The finding is that the summary line hides a live obligation.

---

### F9 — MINOR. `BUNDLE-MANIFEST.md` gives verification instructions for a directory that does not exist.

`.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md:24`:

> Verify anytime with `sha256sum -c` against this block (from `topology/`).

`.syzygy/map/topology` does not exist (verified: `ls` → No such file or
directory), and by `README.md:77` and the acceptance ceremony it *must not*
exist until act 3. The correct cwd is `topology-candidates/`. Run from there,
the bundle verifies cleanly — **9/9 files OK**, which I confirmed. So the
bundle is sound and only the instruction is wrong; a reader who follows it
literally concludes the bundle is unverifiable.

---

### F10 — MINOR. The `candidates/` landing page is a 28-entry directory with two competing READMEs.

`README.md:91-92` sends a fresh reader to
`.syzygy/governance/contracts/candidates/` as start-here #4. That directory
lists 28 entries including `00-README.md` *and* `README.md`. The latter is the
good one — a clear NOT-ACCEPTED banner, a layout table, a verify block. The
former is rev10 packet history. GitHub will render `README.md`, so the web
reader is fine; a reader in a terminal (`ls`) sees two and has no cue which is
current. `candidates/README.md:30` does disclose that `00-README.md` and
`01`–`10-*` are "the rev10 packet's own delivery reports, kept as packet
history" — which resolves it, but only after you have already picked the right
README to open.

---

### F11 — MINOR. A process-round prompt sits at the repository root.

`syzygy_fable_human_clarity_refactor_round_prompt.md` (untracked, but not
git-ignored, and `check_governance.py` counts it inside its declared "clone"
scope of 177 files, citing it at CG-12b as "owner-supplied round charter,
quoted verbatim"). If the front door lands as-is, the second-most prominent
root file after the README is a working prompt for one refactor round. It
belongs under `round-2026-08/` or `_bootstrap/`, not at the root of a public
clone.

---

## Test A — 30 seconds, README alone

**Verdict: passes on all four questions, with one real gap.**

**What Syzygy is** — answered, `README.md:3-5`:

> "A specification-driven control plane for software projects: humans define
> what should be true, evidence shows what is true, and agent fleets do bounded
> work to close the difference — with the difference always rendered honestly."

**Why it exists** — answered, `README.md:16-19`:

> "A day of agent-fleet work too often ends with oversized diffs, scattered
> completions, and no coherent account of what changed or whether it matched
> intent. Underspecification surfaces at the most expensive moment — after
> deployment."

**Current stage** — answered, `README.md:7-12`:

> "**Current stage: pre-specification project-shape normalization.** This
> repository contains **no application code, no behavioral specifications, and
> no implementation backlog — deliberately.**"

**Where to read next** — answered, `README.md:84-101`, an ordered eight-item
"Start here" list beginning with the overview and reaching status, contracts,
policy, pending decisions, contributing, and security.

**The gap.** After 30 seconds I know what Syzygy *does* and cannot state what
it *is as a thing*. Is it a service I run? A CLI? A file format? A web app? A
library I import? The README's only answer is by negation at `:105` — "no
daemon, no UI, no graph store, no adapter, no 3D view, no endpoint" — from
which I reverse-engineer that it is intended to be a daemon with a UI and a
graph store. That inference should not be the reader's job. One sentence in
"Why it exists" naming the intended form factor would close it.

**Prior knowledge required.** Three terms land unexplained: "agent fleets"
(`:4`) — assumed; "specification-driven" (`:3`) — assumed; and the word
*Syzygy* itself is never glossed in the README (its astronomical meaning —
alignment of three bodies: vision, specification, code — is at
`doctrine/README.md:17-19`, which the README's start-here list does not name;
it links only `vision.md`). Given F6, this is a two-way miss: the README does
not point at the glossary, and the glossary's owner (doctrine) points back at a
README glossary that does not exist.

**Word budget.** `wc -w README.md` = **751** (≤ 1,200 ✓). `wc -w AGENTS.md` =
**1,376** (≤ 1,500 ✓). Both pass with margin.

---

## Test B — 10 minutes, following the start-here order

Restated in my own words, from the documents only.

**Desired vs observed vs execution state.** Three kinds of fact that the system
refuses to let collapse into each other. *Desired* is what a human has said
should be true — doctrine and, later, behavioral specifications; it changes only
when a human changes it. *Observed* is what is actually true of the artifact —
the code, the tests, what CI recorded, what the running system does — and it
counts only when backed by a durable, identified, integrity-verifiable
artifact. *Execution* is the audit trail of work: what was scheduled, what an
agent ran, what merged, when. The whole design turns on the third being kept
strictly apart from the second. "A ticket is closed" and "a PR merged" are
facts about *execution*; neither is a fact about whether the software now does
what was asked. The system computes the difference between desired and
observed, and that difference — not the ticket queue — is what becomes work.

**Polaris, Trajectory, Orrery, Mission Control.** The first three are *views*,
not systems. One kernel — a temporal project graph plus an evaluation engine —
computes every truth exactly once, and these three project it: **Polaris**
answers "what is this project supposed to be" (intent), **Trajectory** answers
"what is being done, by whom, under what authority, and what merged without yet
being reconciled" (work), **Orrery** answers "where does everything live and in
what state" (a spatial map where Unknown is a first-class color, and, by
amendment D1, historical state is included). None of the three is independently
authoritative — if two disagreed, that would be a bug in the projection, not a
disagreement between truths. **Mission Control** is deliberately *not* a fourth
one: it sits a level up, at the workspace, and answers "what bounded delegated
missions are running across all my projects." It is also the least settled of
the four — it depends on a candidate contract (RFC-0010) and a doctrine
amendment (D3) that has not been adopted. All four names are working codenames.

**Why merged work is not proof.** Because merging is an event in execution
state and satisfaction is a claim about observed state, and the second does not
follow from the first. Concretely: an agent can merge a change that compiles,
passes review, and does not do what the spec asked. So every merged change
enters a reconciliation chain and stays visibly **reconciliation-pending** until
someone checks it against *the exact revision of the intent that warranted it*
— not the current intent, the one that authorized the work. That check has four
terminal answers, and they are rendered differently on purpose:
reconciled-with-evidence, Unknown(reason), unsatisfied, and
contradiction-raised. The consequence the documents state plainly, and which I
think is the actual thesis: a fleet-built project showing a wall of pending
states is **producing correct output**, not failing. Status only turns positive
through gate-backed evidence whose provenance was verified and captured inside
the identity of the snapshot it was computed from.

**What Syzygy may write.** Two namespaces, and nothing may extend them:
`openspec/**` and `.syzygy/**`. It may *read* declared implementation and
evidence sources anywhere. Everything else — git commits and tags, the issue
tracker, CI, runtime systems — it touches only through typed, explicitly
authorized adapters governed by each of those systems' own contracts, and those
stores are never Syzygy-owned content. It never writes implementation code.
The subtlety I want to record because it is easy to misread: Syzygy *may*
generate code-shaped proposals (a target schema, a migration plan) and commit
**the proposal document** into `.syzygy/**` — what it may never do is apply,
commit, or merge the proposal's *contents* into a code tree. Turning a proposal
into code is exclusively a worker's action against scheduled work. A second
subtlety, from `CONTRIBUTING.md:32-37`: this is a rule about *the product*, not
about people working on this repository — humans and agents here edit the
README, CI, and skills freely.

**What is not implemented.** Everything. No daemon, no UI, no graph store, no
adapter, no endpoint, no 3D view — and no chosen language, framework, or
database, because picking a stack is itself gated on accepting a contract. No
`openspec/` directory exists. No implementation backlog exists and none may be
created. What exists is: adopted doctrine (2026-07-30, git tag
`doctrine-adopted-2026-07-30`, which I verified exists, amendment D1 in force),
owner-approved engineering policy (decision D2), 33 recorded surface decisions,
and a candidate corpus of 32 contract modules across RFC 0001–0011 that **no
owner act has accepted**.

**A restatement I could not complete from the default path.** "Reconciliation
work" and "warrant" I can restate. "Snapshot identity" — `OVERVIEW.md:108-110`
says every status is computed at an identified evaluation, "(source snapshot,
as-of instant)", and that between evaluations claims can only degrade. I can
restate the *rule*, but not what a source snapshot actually is or what
identifies it; that is cited to `architecture.md` and to candidate `RFC2-3`,
neither of which is on the start-here path. This is a soft edge, not a defect:
the overview is explicitly layered and points at its authority. I record it
because the "between evaluations, claims only degrade; improvement requires new
evidence" rule is one of the more counterintuitive commitments in the design,
and it is the one I would most want a fresh reader to be able to check.

---

## Discoverability and reading order

**Coherent.** README → OVERVIEW → doctrine → status works, and the layering is
genuinely good: the overview's four layers (30-second thesis / five-minute
argument / technical model / authority drill-down) let me stop at any depth
without being misled, and every claim block carries a source anchor with
*candidate* anchors marked as such. That marking is the single best legibility
decision in the corpus — I never once had to guess whether something binds.

The four things I was asked to find, I found:

| Sought | Found at | Notes |
|---|---|---|
| Current gate state | `PROJECT-STATUS.md:16-38` — 12 rows, ✅/⏳/⛔, each with an owning record | Clear. But see F1 — its "no blocking defects" line is wrong. |
| Pending owner decisions | `PENDING-OWNER-DECISIONS.md`, P-1…P-16 | Found immediately; stale (F3). |
| Candidate contracts | `candidates/README.md` + `rfcs/` + `ACTIVE-CONTRACT-MANIFEST.txt` | Banner is unambiguous; landing page is cluttered (F10). |
| How to validate | `PROJECT-STATUS.md:62-69`, `candidates/README.md:41-47`, `CONTRIBUTING.md:59-66` | Three consistent, runnable blocks. All ran. One FAILs (F1). |

**Dangling or misleading pointers**, consolidated:

- `vision.md:16`, `vision.md:39`, `v1.md:98` → "README glossary", nonexistent (F6).
- `PENDING-OWNER-DECISIONS.md:21-25,46,48,49` → `_bootstrap/**` paths where
  tracked equivalents now exist (F3).
- `BUNDLE-MANIFEST.md:24` → "from `topology/`", nonexistent (F9).
- `craft-and-care/README.md:20` → `~/.claude/skills/th-engineering/subskills/`,
  machine-local (F5).
- Five files → `…-BOUNDED-MISSION-DRAFT.md` where a repaired `…-D3.md` exists (F4).
- `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15,118,213,215` → a manifest
  digest that no longer matches (F1).

I want to record the counterweight honestly, because it changes my verdict:
`check_governance.py` CG-1a/CG-1b examined 41 markdown links and 539 code-span
path references and found **zero** unresolved. The dangling pointers above are
all of a kind the checker cannot see — prose references ("README glossary"),
directory-name drift inside a shell instruction, machine-local absolute paths,
and semantic staleness. That is a fair boundary for a link checker, but it means
the repository's automated link health is materially better than its actual
pointer health, and nothing measures the gap.

---

## Jargon inventory

Terms met on the default path (README → OVERVIEW → doctrine) that are **not**
explained where first used or one link away:

| Term | First met | Resolution |
|---|---|---|
| `RFCn-m` clause form (14 distinct) | `OVERVIEW.md:45` | **None on path.** Only in `AGENTS.md`, which the README scopes to agents (F7). |
| "actuator toolchain" | `vision.md:38` | **None.** Cites a nonexistent README glossary (F6). |
| "ai-bootstrap toolchain" | `v1.md:98` | **None.** Same dead citation. |
| "term registry" | `OVERVIEW.md:88` | Unlinked; a directory at `:177`; the file is `TERM-REGISTRY.md`, two hops. |
| "Project Genome" | `vision.md:206` | Cites `architecture.md`; off the start-here path but correctly attributed. |
| "genome-complete" | `vision.md:97` | Cites `architecture.md`. Acceptable. |
| "snapshot identity" | `OVERVIEW.md:108` | Cites `architecture.md` + candidate `RFC2-3`. Acceptable but see Test B. |
| "attention items" | `OVERVIEW.md:151` | Defined inline ("declared exceptions"). ✓ |
| "warrant" | `OVERVIEW.md:56` | Inferable from context; defined in `trust-and-evidence.md`. Marginal. |
| `SDR §1–2` | `OVERVIEW.md:77` | Expanded 89 lines later at `:166`. Marginal. |
| `D1` / `D2` / `D3` | `README.md:46,73,75` | `D1` and `D2` resolve (`doctrine/README.md:9`, `INSTALL-RECORD.md`); `D3` resolves via `PROJECT-STATUS.md:27` — to the wrong file (F4). |
| `P-n` | `PENDING-OWNER-DECISIONS.md:19` | Self-defining table. ✓ |
| `T-nn` | `TERM-REGISTRY.md:18` | Defined inline. ✓ Off the default path. |
| `CC-*` | `AGENTS.md` | Not on the default reader path at all. Fine. |
| `VIS-n` / `SEC-n` | `README.md:30` | `doctrine/README.md:45-49`, one link away. ✓ |

Prose vocabulary is disciplined and close to the ~10-term target. The failure is
concentrated in **identifier** vocabulary, which no document budgets or explains
for non-agents (F7).

---

## Current-state legibility

**Strong, and the single best thing about this repository.** After reading, I
can state without hedging what is adopted (doctrine + D1), owner-approved
(craft-and-care, D2), recorded (SDR-1…33), candidate (32 contract modules,
topology bundle, overview, policy additions), proposed (D3), and nonexistent
(`openspec/`, `contracts/rfcs/`, all code). Four independent mechanisms carry
that: the README authority table's Status column, `PROJECT-STATUS.md`'s 12-row
gate table, candidate-home banners on every candidate file, and the overview's
per-claim *candidate* anchors. `check_governance.py` CG-4 and CG-6 enforce two
of them mechanically (candidate banners present; accepted homes absent).

**Could any document mislead me into thinking something is implemented or
accepted?** On implementation: **no.** `README.md:103-109` ("Everything." — no
daemon, no UI, no store, no stack, and an explicit statement that any document
appearing to claim alignment or regeneration capability "is wrong by doctrine"),
`OVERVIEW.md:80-84`, `PROJECT-STATUS.md:12-15`, `SECURITY.md:5-6`, and
`CONTRIBUTING.md:5-9` all say it independently and consistently. I found no
document that overstates capability, and I looked. `vision.md:204-218` even
labels the regeneration ideal as "north star, not present doctrine" with an
explicit `[Unknown]` on achievability. This is unusually disciplined.

**On acceptance: two ways, both found above.** First, the D3 pointer problem
(F4) — every path leads to a draft whose successor says it is defective, and
nothing tells me a successor exists. Second, and more seriously, the act-1
digest mismatch (F1): `PROJECT-STATUS.md:33-35` and `AGENTS.md` both correctly
tell me no act has been performed and that `ACCEPTANCE-ACT-RECORD.md`'s absence
is the correct state — but neither tells me the act as currently written cannot
be performed. That is a state the documents describe as "candidate, awaiting
owner act" when the truer description is "candidate, and the act is presently
broken."

**Third-order.** `PENDING-OWNER-DECISIONS.md` (F3) misled me in the opposite
direction — it told me four defects were open that the tree shows repaired. I
lost real time verifying P-6, P-7, and P-8 against the working tree before
concluding the register was stale rather than the repairs illusory. A register
that over-reports open defects is far less dangerous than one that under-reports
them, and I weight it accordingly — but "where this file and an owning record
disagree, the record wins and this file is stale" (`:6-7`) puts the burden of
that reconciliation on every reader, forever.

---

## Summary of severities

| # | Severity | Finding |
|---|---|---|
| F1 | **blocking** | Act-1 digest mismatch; documented verification FAILs, exit 1, CI red; `PROJECT-STATUS.md:50` claims no blocking defects |
| F2 | **blocking (clone)** | 6 of 10 README start-here targets untracked at `HEAD 9e6f2f7`; front door must land atomically |
| F3 | material | `PENDING-OWNER-DECISIONS.md` stale on P-6/7/8/9/11/14; misdirects to `_bootstrap/` where tracked copies exist |
| F4 | material | Superseded D3 draft is the only advertised one; repaired `…-D3.md` cited nowhere |
| F5 | material | Owner-approved engineering bar adopted by reference from a machine-local path; unreadable from a clone |
| F6 | material | Adopted doctrine cites a "README glossary" that does not exist (3 sites); "actuator toolchain" undefined anywhere reachable |
| F7 | material | 14 `RFCn-m` clause-ID forms unexplained on the default path; convention lives only in agent-scoped `AGENTS.md` |
| F8 | material | `verify_final_prespec.py` prints "PASS — all checks clean" beneath an unmet 2× corpus budget and an outstanding justification |
| F9 | minor | `BUNDLE-MANIFEST.md:24` verification cwd names a nonexistent `topology/` (bundle itself verifies 9/9) |
| F10 | minor | `candidates/` landing: 28 entries, two READMEs |
| F11 | minor | Round-prompt file at repository root |

---

## Verdict

**EXCEPTIONS**

The corpus is sound and, on the dimension it cares most about — never claiming
more than it can evidence — it is the most disciplined pre-specification
repository I could reasonably expect to read. Test A passes in 30 seconds on all
four questions; Test B passes on all six, in my own words, from the documents
alone. Current-state legibility is excellent and mechanically enforced.

I withhold ACCEPT for two reasons, both concrete and both fixable without
touching the argument. First (F1), the act the entire repository is organized
around cannot presently be performed: the acceptance record offers a manifest
digest that no longer matches, the project's own verification command says so,
and the status page says there are no blocking defects. Second (F2), as a public
clone at `HEAD` this front door is 60% dangling — which matters more than usual
here, because `CONTRIBUTING.md:59` makes clone-reconstructability part of the
project's own definition of done.

The material findings F3–F8 share one shape worth naming: **the repository's
pointer hygiene is verified where it is machine-checkable (0 findings across 580
links and path references) and unmanaged where it is not** — prose citations,
cwd instructions inside shell blocks, machine-local absolute paths, supersession
between two files with near-identical names, and semantic staleness in a
hand-maintained register. Every finding in F3–F8 lives in that gap. That is the
risk I would carry forward even after F1 and F2 are closed.
