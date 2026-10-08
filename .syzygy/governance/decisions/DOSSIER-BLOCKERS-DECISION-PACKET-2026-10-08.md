# Owner decision packet — three blockers from the first Redis dossier run

> **Candidate — binds nothing.** This packet performs no act, records no
> ruling and adopts nothing. Each decision below takes effect only by the
> ceremony it names, performed by you. A commit, a merged pull request, a
> review or silence performs nothing. Decisions 1 and 2 are offered only after
> a confirming review of their packages; none has run yet.

Date drafted: 2026-10-08, by an agent lane at the lead's request.

Register rows: P-105, P-106, P-107 in `PENDING-OWNER-DECISIONS.md`.

## Why you are reading this

You want to type "Please generate me a Polaris dossier for
https://github.com/redis/redis" and get, in one to two hours, a page that
teaches Redis end to end. The run on 2026-10-08
(`run-e8b77d72780cc48f4dd032267d963d93`) hit three walls that only you can
move:

1. The screening policy withheld Redis's core C files (`networking.c`,
   `server.c`, `aof.c`, `rdb.c`, `replication.c`, `cluster.c`, `db.c`) as
   "active content", so the dossier cannot quote the heart of the server.
2. The Redis agent-provider statement you signed on 2026-10-07 predates the
   `project-documentation` class, so Syzygy cannot put README or docs text into
   the packets it hands your agent sessions.
3. Every helper session (inventory, fidelity review, design review) must be
   started by you by hand, so the run sat idle for five hours overnight.

Each section is one decision: what it is, the options (recommended first),
what yes and no cost, and the exact words to give.

---

## Decision 1 — let C source past the HTML check (screening policy version 3)

**What is wrong.** The policy for public repositories runs a Markdown
active-content check on every file it admits, source code included (the
version-2 text says so and adds "This scope adds no loosening"). That check
looks for HTML tags. In C, `if (a<b && c>d)` contains `<b && c>`, which it
reads as a tag named `b`, and a shell script's backtick reads as an unclosed
code span. [Observed: both reproduced against the scanner on this branch.]

**Is the lead's proposed fix true?** The proposal was "a code file is only ever
rendered inside code blocks, so the HTML check adds nothing". The rendering
part is **not quite true**: code is rendered as a quotation (`<q>`) or a block
quotation (`<blockquote>`), not a code block. What *is* true, and what the
draft relies on instead: every byte of a target file that reaches a page goes
through one escape function that turns each of `& < > " '` into a character
reference, and every page carries a Content-Security-Policy that forbids
scripts (`default-src 'none'`). [Observed: `dossier-render.ts:261` and `:409`,
`draft-preview.ts:24`, `:18` and `:122`; details and the sweep's limits in the
package's `SEMANTIC-DELTA.md`.] So the HTML check protects nothing a page could
render, while it hides most of the C source.

**The draft.** `../contracts/candidates/public-source-screening-scope-v3/`.
It adds one exemption: a code file is admitted without the HTML check, **only
while** every page that shows it escapes it as above; any page that cannot
promise that runs the check as before. Every secret detector still runs on
every file. README and docs files are still checked. Nothing else in the
policy moves (the builder fails if anything does).

| Option | What changes | Cost |
|---|---|---|
| **A. Variant `all` (recommended)** | All 25 source extensions skip the HTML check | Widest; a JavaScript or PHP file full of HTML strings is admitted too, protected only by the escaping |
| B. Variant `non-web` | 18 extensions skip it; `.js .mjs .cjs .jsx .ts .tsx .php` are still checked | Defence in depth for languages that embed HTML; their false positives (template literals, JSX) stay withheld. Redis is C, Tcl and Lua, so either variant admits its core files [Inferred] |
| C. Decline | Nothing | Redis's core C files stay withheld; the dossier explains Redis from headers, tests and docs only |

**If yes:** the C files become readable once the install change lands (see
below). **If no:** version 2 stays in force and nothing changes.

**Words to give** (after a confirming review; you pick one row, never both):

- "Sign screening scope version 3, variant all" — or "…, variant non-web" — or
  "Decline screening scope version 3".

The recorder writes the act with the phrase
`APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY: <row>`, where `<row>` is
the chosen variant's row of `PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt`,
read at the sitting. This packet carries no digest by design.

**Install-time requirement (`syzygy-fxro`) — the Redis gate closes without
it.** The public-target read gate knows exactly two policy acts, version 1 and
version 2 (`POLICY_ACT_FORMS` in
`packages/polaris-generation-consent/src/package-reader.ts:346-356`). It
refuses the read when any other decisions file names the policy. So the same
commit that installs the version-3 act must add a third form and extend the
chain (version 3 needs version 2, later, over other bytes). The same install
also teaches both screens (`packages/polaris-dossier/src/screen.ts:66`,
`apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:108`)
to honour the exemption, swaps the version-2 recorder's battery line for the
version-3 one, and re-pins the Butlers gate, as after every policy act. The act
alone admits nothing. The list is in the package's `IMPACT-LEDGER.md`.

---

## Decision 2 — let README and docs text reach your agent sessions (provider statement version 2)

**What is wrong.** Your 2026-10-07 statement says Claude Code with Anthropic
may receive five classes of Redis content. `project-documentation` (README,
guides, changelog) is not one of them, because the class was created after the
statement was drafted, and the class act says "No existing consent gains the
class". PR #403's review (finding F1) therefore stopped Syzygy from putting
docs text into the inventory and review packets it hands your sessions.
Without it the fidelity review cannot check claims drawn from the README, and
those claims render Unknown.

**The draft.** `../contracts/candidates/dossier-agent-provider-v2/`. It is the
same record, with the same Record ID, at version `0.2.0-candidate.1`, with
`project-documentation` added to its classes. It supersedes version 1
prospectively from its own act. The builder proves nothing else differs from
version 1. A new package was needed because the version-1 recorder freezes its
package. This is a digest-bound consent act, like version 1, and not a
version-tag sign-off: the Scope A direction covers specification deltas,
registry entries and contract successors, not consents.

| Option | Cost |
|---|---|
| **A. Sign version 2 (recommended)** | Docs text goes to your own Claude Code sessions, which can already read the whole clone; the statement already says so |
| B. Rule instead that the class list does not govern Syzygy's packets | No new act, but it reads away a consent's words; a later reviewer would be right to call it a loosening without one |
| C. Decline | Docs text stays out of the packets; README-based claims stay Unknown |

**If yes:** after the install change (below), packets may carry screened docs
spans for Redis. **If no:** PR #403 ships without docs in packets.

**Words to give** (after a confirming review): "Sign the Redis Anthropic
provider statement, version 2", or "Decline".

The recorder will take a new phrase. The draft suggests `CONSENT TO ANTHROPIC
AGENT PROVIDER VERSION 2 FOR REDIS: <row>`, worded so it does not contain
version 1's phrase. Version 1's sweep reads that phrase as naming version 1.

**Install-time requirement.** The statement gate knows only version 1
(`packages/polaris-dossier/src/gate-sources.ts:220-238`). It refuses when two
statements are in force for one pair (`:295`). Its withdrawal sweep would read
a version-2 act record, which names the same Record ID, as naming version 1
(`:230`). The install must add a version-aware form in which version 2 ends
version 1's term. PR #403's class gating must then read the version in force.
The full list is in the package's `SEMANTIC-DELTA.md`.

---

## Decision 3 — the hand-offs that stalled the run

**The rule, quoted.** It is not doctrine. It comes from two places:

- Your direction of 2026-10-05, item 2
  (`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`): "The
  fresh-context fidelity review runs in a separate top-level session that the
  operator starts. … A subagent spawned by the authoring session does not
  satisfy the review." It names the fidelity review only.
- The signed specification, REQ-polaris-generation-035
  (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:320`),
  which extends it to the inventory and the design review: each "SHALL each be
  produced in a separate top-level agent session that the operator starts"; "a
  subagent spawned by the authoring session, a process the authoring session's
  agent launches, including a headless session it starts and whose output it
  reads, … SHALL NOT satisfy the inventory or a review."

The design says why: "The loop is therefore attended at each hand-over, and no
agent coordinates another" (`design.md:70-71`). The headless form was ruled out
by the lead, not by you (`design.md:77-80`), as "brush[ing] against 'No
unattended agent coordination'". That prohibition is written in the two PWB
implementation acts, which are scoped to development work, not to the product
(`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md:80-81`). SEC-3 as amended by D9 does
not require hand-starting. It forbids only giving the *run-the-code*
instruction to "a session it started or to one left running unattended", and
it says "Work the session hands to its own subagents is part of the session"
(`doctrine/security.md:90-93`). Helper sessions never get that instruction.

**What independence needs, separately from who presses Enter:** a fresh
context, given only Syzygy's packet and Syzygy's fixed prompt, never
instructions the author wrote (CC-REV-1; REQ-polaris-generation-006).

| Option | Fixes the overnight stall? | What it needs amended |
|---|---|---|
| **B. Pre-started waiting sessions (recommended).** At the start of a run you open the inventory, fidelity-review and design-review sessions yourself, from Syzygy's printed commands. The inventory starts work at once (it never sees the draft). Each reviewer runs a new Syzygy command that waits until its packet exists, then re-hashes and reviews it. | Yes, if you also pre-approve the sessions' tool permissions, because an interactive session that stops for a permission prompt also waits for you [Inferred] | No doctrine. [Inferred] REQ-035's words are met (you start every session, in a new terminal, with Syzygy's prompt), but `design.md:63-71` describes starting a session at the hand-over, so a v1.2 spec package (version-tag sign-off) should say a session may be started before its packet exists. Code: a wait mode and an early `session-prompt` |
| A. Keep it | No | Nothing |
| C. You attend; the authoring session launches the helpers (headless, with Syzygy's prompt) and you approve each launch | No, you must be present | Your direction item 2 superseded; REQ-035 amended (v1.2); design. Independence weakens: the author's agent types the reviewer's command line |
| D. Unattended: the authoring session, or Syzygy itself, launches the helpers with nobody present | Yes | C's amendments, plus a reading that "No unattended agent coordination" does not bind the product. If Syzygy launches them, it becomes the party sending content to a provider: the run disclosure "Syzygy made no provider call" (`render.ts:531`) turns false, and the egress record and the RFC7-20 reading come into play. An execution-permitted run is excluded by SEC-3 as amended |
| E. One session does everything | Yes | REQ-006 and REQ-035, your item 2, and CC-REV-1 (an owner-approved craft policy). The review stops being independent, so claims cannot be judged "supported" and would render Unknown (`render.ts:349-352`). Not recommended |

**Sub-question for B (if you pick it):** may one waiting reviewer review the
next draft revision after a repair, or must each revision get a session you
started for it? *Recommended:* one session may continue, disclosed on the
review page. It never sees the author's context, only successive packets.

**If yes (B):** one owner direction now authorizes the code and the v1.2
draft. The v1.2 sign-off follows by version tag. **If no:** runs keep stalling
whenever you step away.

**Words to give:** "Direction: pre-started waiting sessions (option B), one
reviewer may continue across revisions" — or name another option letter. This
is a plain owner direction. It binds no digest, and it is recorded as a
direction file in this directory.

---

## Order and what follows

The three are independent. Decisions 1 and 2 each need a confirming review of
their package first; the lead dispatches it. Each then needs its own recorder
and an install change in the same commit as the act record. Until those
land, each act would close a gate rather than open one: decision 1 closes the
read gate (`syzygy-fxro`), and decision 2 closes the statement gate.
Decision 3 needs no review before your direction; its code and the v1.2
package each get one afterwards.
