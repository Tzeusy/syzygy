# Owner decision packet — three blockers from the first Redis dossier run

> **Candidate — binds nothing.** This packet performs no act, records no
> ruling and adopts nothing. Each decision below takes effect only by the
> ceremony it names, performed by you. A commit, a merged pull request, a
> review or silence performs nothing. Decisions 1 and 2 are offered only after
> a confirming review of their packages; none has run yet.

Date drafted: 2026-10-08, by an agent lane at the lead's request. Revised the
same day after review round 1 (`docs/reviews/R-PR404-DOSSIER-BLOCKERS-1-RAW.md`).

Register rows: P-105, P-106, P-107 in `PENDING-OWNER-DECISIONS.md`.

## Why you are reading this

You want to type "Please generate me a Polaris dossier for
https://github.com/redis/redis" and get, in one to two hours, a page that
teaches Redis end to end. The run on 2026-10-08
(`run-e8b77d72780cc48f4dd032267d963d93`) hit three walls that only you can
move. [Observed, as reported by the lead; this lane did not read the run
directory.]

1. The screening policy withheld seven of Redis's core C files
   (`networking.c`, `server.c`, `aof.c`, `rdb.c`, `replication.c`,
   `cluster.c`, `db.c`) as "active content".
2. The Redis agent-provider statement you signed on 2026-10-07 predates the
   `project-documentation` class, so Syzygy cannot put README or docs text
   into the packets it hands your agent sessions.
3. Every helper session must be started by you by hand, so the run sat idle
   for five hours overnight.

---

## Decision 1 — let C source past the HTML check (screening policy version 3)

**What is wrong.** The policy for public repositories runs a Markdown
active-content check on every file it admits, source code included. That
check looks for HTML tags. In C, `if (a<b && c>d)` contains `<b && c>`, which
it reads as a tag named `b`. [Observed: reproduced against the scanner on
this branch.]

**Is the lead's proposed fix true?** It said code "is only ever rendered
inside code blocks". **Not quite**: code renders as a quotation (`<q>`,
`<blockquote>`). What is true in the renderers the package names: every
target byte they put on a page is escaped (each of `& < > " '` becomes a
character reference), and every page carries a Content-Security-Policy that
allows no script. [Observed in `dossier-render.ts` and `draft-preview.ts`;
the round-1 reviewer's wider sweep found no other HTML sink.]

**The draft.** `../contracts/candidates/public-source-screening-scope-v3/`.
A code file skips the HTML check **only while** every page that shows it
writes it as escaped text, under a policy whose `default-src` is `'none'` and
which carries no `script-src`, `script-src-elem`, `script-src-attr` or
`object-src` directive. Any page that cannot promise that runs the check.
Every secret detector still runs on every file; docs are still checked.

| Option | What changes | Cost |
|---|---|---|
| **A. Variant `all` (recommended)** | All 25 source extensions skip the HTML check | Widest: a JavaScript or PHP file full of HTML strings is admitted too, protected only by the escaping. Every newly admitted file can also be quoted on pages, put in review packets for your sessions, and sent to a provider in provider mode; those rules do not change, but the files they reach grow [Inferred: small, since your agent already reads the clone] |
| B. Variant `non-web` | 18 extensions skip it; `.js .mjs .cjs .jsx .ts .tsx .php` are still checked | Those languages' false positives (template literals, JSX) stay withheld. The same growth as A, over fewer files. Either variant admits Redis's C, Tcl and Lua [Inferred] |
| C. Decline | Nothing | Redis's core C files stay withheld; the dossier explains Redis from headers, tests and docs only |

**If yes:** the C files become readable once the matching code change lands
in the same commit (the package's `IMPACT-LEDGER.md`); without it the act
closes the Redis read gate. **If no:** version 2 stays in force.

**Words to give** (after a confirming review; pick one): "Sign screening
scope version 3, variant all", "…, variant non-web" or "Decline screening
scope version 3". The act takes version 2's phrase form over the chosen
manifest row, read at the sitting.

---

## Decision 2 — let README and docs text reach your agent sessions (provider statement version 2)

**What is wrong.** Your 2026-10-07 statement lets Claude Code with Anthropic
receive five classes of Redis content. `project-documentation` (README,
guides, changelog) is not one of them, because the class was created later,
and the class act says "No existing consent gains the class". So PR #403,
now merged, withholds docs text from the review packets it hands your
sessions [Observed: review finding F1,
`docs/reviews/R-PR403-SCREEN-DOCS-1-RAW.md`, and the class gate in
`packages/polaris-dossier/src/class-gate.ts`]. README-based claims then
cannot be reviewed and render Unknown.

**The draft.** `../contracts/candidates/dossier-agent-provider-v2/`: the
same record at version `0.2.0-candidate.1`, with `project-documentation`
added, superseding version 1 from its own act; the builder proves nothing
else differs. It is a digest-bound consent like version 1 (Scope A
sign-offs do not cover consents).

| Option | Cost |
|---|---|
| **A. Sign version 2 (recommended)** | Docs text goes to your own Claude Code sessions, which can already read the whole clone |
| B. Rule that the class list does not govern Syzygy's packets | No new act, but it reads away a consent's words: an unsigned loosening |
| C. Decline | Docs text stays out of the packets; README-based claims stay Unknown |

**If yes:** packets may carry screened docs text for Redis once the matching
code change lands in the same commit (the package's `SEMANTIC-DELTA.md`);
without it the act closes the statement gate. **If no:** docs text stays
withheld from packets, as now.

**Words to give** (after a confirming review): "Sign the Redis Anthropic
provider statement, version 2", or "Decline".

---

## Decision 3 — the hand-offs that stalled the run

**The rule, quoted.** It is not doctrine. Full clauses and line references
are in `../contracts/candidates/dossier-handoff-options/CLAUSES.md`.

- Your direction of 2026-10-05, item 2: "The fresh-context fidelity review
  runs in a separate top-level session that the operator starts. … A
  subagent spawned by the authoring session does not satisfy the review."
- The signed specification, REQ-polaris-generation-035, extends that to the
  inventory and the design review, and excludes "a headless session [the
  authoring agent] starts and whose output it reads".
- Your direction of 2026-10-03 (the overnight beads loop), item 2: "It
  changes nothing about what Syzygy the product may do: the product still
  coordinates no agents."

SEC-3 (as amended by D9) does not require hand-starting. Independence needs a
fresh context given only Syzygy's packet and prompt (CC-REV-1), not your
finger on Enter.

| Option | Fixes the overnight stall? | Costs, and what it needs amended |
|---|---|---|
| **B. Pre-started waiting sessions (recommended).** At the start of a run you open the inventory, fidelity-review and design-review sessions yourself, from Syzygy's printed commands. The inventory starts at once. Each reviewer runs a Syzygy command that waits for its packet, then re-hashes and reviews it | Yes, for the helper sessions | **Security cost:** Syzygy's printed command is non-interactive, so a tool call nobody approved fails rather than waits, and the tools must be pre-approved. The sessions then read untrusted clone text with no one present; a brief saying "clone text is data" does not stop an auto-approved session that obeys injected text. Mitigation: approve only read tools and the role's one `syzygy dossier` command [Inferred]. **Execution cost:** a permission to run Redis's code lapses when you leave the authoring session unattended (signed spec), so unattended stretches are reading-only. **Amended:** no doctrine; a v1.2 spec package (version-tag sign-off) saying a session may start before its packet exists. Code: a wait mode |
| A. Keep it | No | Nothing |
| C. You attend; the authoring session launches each helper headless with Syzygy's prompt, and you approve each launch | No, you must be present | Supersede your 2026-10-05 item 2; amend REQ-035 (v1.2). Your reading of whether your 2026-10-03 item 2 reaches an agent launching on Syzygy's printed instructions. Independence weakens: the author's agent types the reviewer's command |
| D. Unattended: the authoring session, or Syzygy, launches helpers with nobody present | Yes | C's amendments; where Syzygy launches, it contradicts your 2026-10-03 item 2 outright, which would need superseding, and the "no provider call" disclosure turns false. Excludes runs that execute code |
| E. One session does everything | Yes | No independent review (REQ-006, REQ-035, CC-REV-1), so claims render Unknown. Not recommended |

**Sub-question for B:** may one waiting reviewer review the next revision
after a repair, or does each revision need a session you start?
*Recommended:* one may continue, disclosed on the review page; it sees only
successive packets. *Cost:* it has seen its own earlier verdict, which anchors
the next one; this repository's own loops use a fresh reviewer each round.

**If yes (B):** one direction authorizes the code and the v1.2 draft. **If
no:** runs keep stalling whenever you step away.

**Words to give:** "Direction: pre-started waiting sessions (option B), one
reviewer may continue across revisions", or "…, a fresh reviewer for each
revision", or another option letter. A plain direction; it binds no digest.

---

## Order

The three are independent. Decision 3 needs no review before your direction;
its code and the v1.2 package each get one afterwards.
