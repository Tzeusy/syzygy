# Review — PR 404 Redis dossier blockers owner packet
Verdict: REVISE
Reviewed commit: 6aa8b77d2e84ad246dfb5bad5753a5d07179d958
Reviewer: fresh-context

Subject: `.syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`
and the two candidate packages it routes to
(`contracts/candidates/public-source-screening-scope-v3/`,
`contracts/candidates/dossier-agent-provider-v2/`), the register rows P-105
to P-107 and the `decisions/README.md` row. PR base: merge-base with
`origin/main` `56c6c98c56282bcdcd1d332b12281a16d91fe6b9`. The PR's file list
(17 files: 15 added, 2 modified) was read from `gh pr view 404` and matches
`git diff --name-status 56c6c98c 6aa8b77d`.

This raw carries no `Manifest SHA-256` line, so under either package's
review-head contract (`build_public_source_screening_scope_v3.py` docstring;
`REVIEW-BRIEF.md:62` and `dossier-agent-provider-v2/REVIEW-BRIEF.md:48`) it is
**not** a confirming review of either package. The packet's sentence "none
has run yet" stays true after it.

## What was verified (no finding)

- [Observed] Digests (rule 3). I applied each `proposed/*.patch` with
  `patch -o` to the policy at the PR head and hashed the output:
  `all` → `e79b7220…1059b`, `non-web` → `47fb97df…0df3ed`, equal to the two
  rows of `PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt`. The base policy
  hashes `98a87f81…3f49`, which is the version-2 manifest row `none`
  (`public-source-screening-scope-v2/PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt:7`)
  and the argument of the performed version-2 act
  (`ACCEPTANCE-ACT-RECORD.md:1271`). The v2 provider record hashes
  `b7a8d099…6df3`, equal to its manifest row. The v1 provider record still
  hashes `fbbcd3c0…48a7`, the digest bound by
  `DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md:17`.
- [Observed] Both builders: `--check` current; `--selftest` 21 of 21 and
  12 of 12 predicates held.
- [Observed] The policy delta changes only what it says. A JSON walk of base
  against each patched file reports exactly `policyVersion`,
  `publicSourceScope.activeContent.rule`, `.consequence`,
  `.codeContentExemption` (added) and `publicSourceScope.inheritedRules`.
  `detectors` and every other key are unchanged, so no secret detector moves.
  `all` exempts all 25 `sourceExtensions`; `non-web` exempts 18 and omits exactly
  `.cjs .js .jsx .mjs .php .ts .tsx`.
- [Observed] The scanner behaviour the packet asserts. Against
  `scanActiveContent` (the built `three-surface-poc-core/dist`; the source files
  `git-object-reader.ts` and `markdown-code-context.ts` do not differ between
  the main checkout's HEAD `3409ef5a` and the PR head):
  `if (a<b && c>d)` → `html-tag` at 2:8; a shell body with an unpaired
  backtick → `malformed-code-context` / `unclosed-inline-span`; plain C and
  paired backticks → no findings (controls).
- [Observed] The rendering sink claim (AC1). I looked for a sink where a
  code-content span is rendered unencoded and found none. Every `${…}`
  interpolation in `dossier-render.ts` that carries body text goes through
  `escape` (`:256`, `:261`, `:409`). `dossier-render-local.ts` (45 lines) escapes
  every string. `draft-preview.ts:122` escapes `source.spans[0]!.text`, and
  `escape` (`:24`) replaces `& < > " '`. The machine view (`dossier-render.ts:440-452`)
  carries `quotations` built at `:260` with offsets and anchors only. The
  other non-test users of span text that a grep for `.spans`, `span.text`,
  `part.text` and `quoteText` returns over `apps/three-surface-poc/src` and
  `packages/` are not HTML sinks:
  `consent-ports.ts:67` hashes the text; `pipeline.ts:265` hands spans to the
  provider-mode call, which is egress; `execution-rule.ts:126-127` carries
  doctrine spans only; `review.ts` writes `packet.json` for the review session,
  which is also egress. The inventory brief (`inventory.ts`) carries no target
  bytes. The packet's correction of the lead's "code blocks" wording is
  accurate: the sinks are `<q>`, `<blockquote>` and `<div>`.
- [Observed] `syzygy-fxro` (AC7). `POLICY_ACT_FORMS` is at
  `package-reader.ts:346-356` and holds two forms. `readPolicyActs` refuses any
  decisions file that `namesPolicy` unless it is a registered form or a pinned
  historical act. The chain is strict: v2 needs v1, a later instant, other bytes,
  and supersession text naming v1's path and digest. The packet and ledger
  state the requirement correctly: a third form in the same install commit,
  and a chain extended to version 3 after version 2.
- [Observed by emulation] The PR's own decisions files do not trip the gates
  they describe. A Python port of `namesPolicy` (`fold`, `stemFolds`,
  `carries`, the field-line rule) returns no hit on the packet,
  `PENDING-OWNER-DECISIONS.md` or `README.md`, and four hits on the v2 act file
  (control). A port of the provider-statement stems (`gate-sources.ts:181`,
  `:230`) returns no hit on the three files and five on the v1 act (control).
  Merging the packet therefore closes neither the read gate nor the statement
  gate. The port approximates `\p{Default_Ignorable_Code_Point}` with six code
  points.
- [Observed] AC5. Neither modified file's base or head SHA-256 appears in any
  of the 2605 tracked files, and neither path is named in a `*MANIFEST*` file
  or in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`. No `-RAW.md` is
  touched. No `.ts/.js/.py/.mjs/.sh` file was added under `.syzygy/**` or
  `openspec/**`; both builders are under `scripts/`. Nothing is labelled
  accepted, and every new governed file opens "Candidate — binds nothing".
  `check_governance.py` at the head reports 32 OK, 21 WARN, 0 FAIL.
- [Observed] Register arithmetic. Using `^\| P-[0-9]+[^ |]*` per `##` section
  I count 5 acceptance-act rows and 34 open rows, 39 in all, as the dated note
  states.
- [Observed] Ceremony (AC4). The decision-1 phrase form `APPROVE POLARIS
  BUTLERS SECRET-CLASSIFICATION POLICY: <row>` matches the performed v2 act
  (`ACCEPTANCE-ACT-RECORD.md:1271`). Option selection over typed words matches
  that act's "given … by option selection, not typed". Decision 2 is correctly
  kept a digest-bound consent: Scope A
  (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` item 1) names spec
  deltas, the registry entry and contract successors, not consents. Decision
  3 is correctly a plain direction.
- [Observed] Quotations checked against their files: SEC-3 `security.md:89-93`;
  the 2026-10-05 direction item 2 (`…SCOPE-REVIEW-SIGNOFF-DIRECTION.md:56-60`);
  REQ-035 (`spec.md:320`); `design.md:70-71` and `:77-80`; `render.ts:349-352`
  and `:531`; `gate-sources.ts:220-238`, `:230` and `:295`; the RFC5 class act
  `:66` "No existing consent gains the class".

## Findings

**Finding 1 — Decision 3 omits the owner's own reading of "No unattended agent coordination"** (revise)

Packet `DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md:161-164`: "That
prohibition is written in the two PWB implementation acts, which are scoped
to development work, not to the product". [Observed] A third governed record
uses the phrase, and the packet does not cite it:
`OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md:31-35`, item 2, "How it
reads AGENTS.md". It reads: "This direction is the owner's explicit exception
for this run only. It changes nothing about what Syzygy the product may do:
the product still coordinates no agents." My sweep was a case-insensitive
grep for `unattended agent` over `.syzygy/` and `openspec/`, which returned 6
files.

The failure: options C and D are framed as needing only "a reading that 'No
unattended agent coordination' does not bind the product". The owner has
already stated, in a direction in force, that the product coordinates no
agents. Option D, where Syzygy launches the helpers, contradicts that owner
sentence. Option C, where the authoring agent launches them, needs a reading
of it. The packet presents the prohibition as development-only. It does not
show the owner the owner's own statement against which that reading must be
judged, so the trade-off is smoothed. Repair: quote item 2 under "The rule,
quoted", and add that statement to the "What it needs amended" cells of D
(and C, if the lead reads it as reaching C).

**Finding 2 — Option B's "Fixes the overnight stall? Yes" omits two costs, one of them a security cost** (revise)

Packet Option B row: "Yes, if you also pre-approve the sessions' tool
permissions, because an interactive session that stops for a permission prompt
also waits for you [Inferred]".

(a) [Observed] The signed spec says an execution-permitted authoring
session's "permission lapses if the owner stops attending the session,
including by leaving it under an automatic-approval or permission-bypass
setting while away, and that the agent then runs no further observed code"
(`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:15`).
For the run to progress overnight, the authoring session must also continue
after each verdict while the owner is away. In a run with an execution
choice, it then loses the permission. The packet records "An
execution-permitted run is excluded by SEC-3 as amended" for D. It is silent
for B, the recommended option, although B has the same limit. [Inferred]

(b) [Inferred] Pre-approving tool permissions for helper sessions that run
unattended over an untrusted public clone is the recommended option's
security cost. Instruction text in the clone (the inventory brief itself warns
about it, `inventory.ts:208`) then meets auto-approved tools with nobody
present. The inventory brief carries SEC-3's rule, but an auto-approved
session that follows injected text is not stopped by a brief. The packet
states this condition only as a functional prerequisite, never as a cost.
AC3 asks for the security cost of the recommended option. Repair: state
both costs in B's row.

Separately, as a note: the design's printed launch command is `claude -p
"<prompt>"` (`design.md:57`). A print-mode session does not "stop for a
permission prompt"; an unapproved tool call fails. The conclusion that
permissions must be pre-approved survives, but the stated mechanism does not.

**Finding 3 — `renderCondition`'s CSP clause is satisfied by a policy that permits scripts** (revise)

Proposed bytes, both variants, `codeContentExemption.renderCondition`: "…and
the page carries a Content-Security-Policy whose default-src is 'none'".
[Observed] A later directive overrides `default-src` for its own fetch type.
A CSP of `default-src 'none'; script-src 'unsafe-inline'` meets the clause as
written and runs inline script. The deployed CSP (`draft-preview.ts:18`)
already relaxes one type: `default-src 'none'; style-src 'unsafe-inline'; …`.
The packet paraphrases the condition as "a Content-Security-Policy that
forbids scripts (`default-src 'none'`)". The bytes the owner would bind do
not say that. Entity encoding remains the primary control, so this is defence
in depth, but the clause is the policy's own guard and is cheap to fix before
review: for example "…whose default-src is 'none' and which carries no
script-src, script-src-elem, script-src-attr or object-src directive", or
name the exact CSP. The packet's paraphrase should then match the bytes.

**Finding 4 — the delta names no affected requirement or contract identifier** (revise)

`SEMANTIC-DELTA.md` (screening v3) contains no `REQ-`, `RFC`, `SEC-` or `VIS-`
identifier [Observed: grep over the package's three Markdown files returned
nothing]. `NORMATIVE-CHANGE-WORKFLOW.md:65-66` asks for "every artifact that
cites, derives from, or depends on the affected identifiers". The exemption
relies on REQ-polaris-generation-012, "Generated pages SHALL render untrusted
source and provider content inertly…", with its scenario "executable markup,
unsafe links…" (`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md:639`,
`:648`). The screens it changes implement REQ-polaris-generation-033's
screening rule (quoted in `screen.ts:7-8`). The delta should name both, and
say that the exemption reads REQ-012 as satisfied by `renderCondition`, so
that a reviewer can contradict the reading. AC2 asks that every affected
identifier be stated.

**Finding 5 — Decision 1's cost column omits the egress population the exemption widens** (revise)

Packet Option A cost: "Widest; a JavaScript or PHP file full of HTML strings
is admitted too, protected only by the escaping". The delta's
`codeContentExemption.egress` correctly says no egress *rule* changes. But
every newly admitted body also becomes eligible for Syzygy's own hand-offs:
review packets carry "the cited spans as Syzygy read them" (REQ-035,
`spec.md:320`), and provider mode sends span text through
`pipeline.ts:265` under the public egress record. [Inferred] The risk is
small, since the agent already reads the clone and the provider already
receives code-content. Still, the bodies Syzygy itself transmits, and the
ones it renders, grow by the same set. The owner is not told this.
One clause in A's and B's cost cells would fix it.

**Finding 6 — Decision 1 states the sink claim as universal while the package's sweep is three files** (note)

Packet: "every byte of a target file that reaches a page goes through one
escape function … [Observed: …]". The package itself says: "[Inferred] the
sink sweep covered the three files … another HTML sink elsewhere is not
excluded by it" (`SEMANTIC-DELTA.md`, "Why"). My wider sweep (above) found no
counterexample. Still, the packet's Observed label is broader than the
evidence it cites (rules 2 and 9). Scope the sentence to the renderers named,
or cite a sweep with a denominator.

**Finding 7 — the impact ledger misses a version pin that fails after the act** (note)

`IMPACT-LEDGER.md` lists, under "The Butlers read gate", the files that name
the policy *path*. [Observed] `packages/three-surface-poc-core/src/git-object-reader.ts:41-44`
pins `policyVersion: '1.3.0-public-source-candidate.1.none'`, and its comment
reads "proven byte-equal in the test". `project-shape-model.test.ts` and
`content-classification.test.ts` also carry the string. The ledger's method
(a grep for the path and two key names) cannot reach a version literal. The
installer derives the set at the sitting, so nothing is lost if it does.
But the ledger presents a list of "Known members" that omits one. Add the
version string to the sweep.

**Finding 8 — the v2 phrase rationale overstates what the wording avoids** (note)

Packet decision 2: "worded so it does not contain version 1's phrase. Version
1's sweep reads that phrase as naming version 1." [Observed] Version 1's
sweep stems also include the artifact basename
`AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`, the heading, and the Record ID
(`gate-sources.ts:181`, `:230`). A v2 act record will carry these whatever its
phrase. The label choice therefore avoids none of the collision on its own;
only the version-aware form fixes it. The packet's next paragraph says so.
The sentence should not suggest the wording is the safeguard.

**Finding 9 — several run facts are unanchored in the packet** (note)

The seven file names, "sat idle for five hours overnight" and "PR #403's
review (finding F1)" carry no path and no label in the packet. The package
labels the first and the third "[Observed, as reported by the lead …]" and
"[Observed, as relayed by the lead …]". The raw "lives on the PR #403
branch". Carry those labels into the packet (rule 8).

**Finding 10 — the sub-question's recommendation omits its cost** (note)

"one session may continue, disclosed on the review page. It never sees the
author's context, only successive packets." [Inferred] A continuing reviewer
has seen its own earlier verdict and the earlier draft, so its second verdict
is anchored on its first. This repository's own repair loops take a fresh
reviewer per round. The disclosure is good; the trade-off should be stated
beside it.

**Finding 11 — readability** (note)

[Observed] 2,082 words (`wc -w`), roughly nine to ten minutes, at the AC6
limit. The passages the owner does not need in order to decide are the two
"Install-time requirement" paragraphs (code line references), the "The rule,
quoted" paragraph's chain through `design.md`, the PWB acts and SEC-3, and
Option D's cell (RFC7-20 and the egress record). Each could move to its
package or to a footnote list, leaving the decision tables and the words to
give.

## Verdict basis

Findings 1 to 5 are revise. Finding 1 omits an owner statement in force that
bears on two options. Finding 2 omits the recommended option's security cost
and a doctrine-derived limit. Finding 3 is a defect in the bytes the owner
would bind. Findings 4 and 5 are AC2 and AC3 gaps. None needs a new
decision, and each is a local repair. Findings 6 to 11 are notes.

Verdict: REVISE
