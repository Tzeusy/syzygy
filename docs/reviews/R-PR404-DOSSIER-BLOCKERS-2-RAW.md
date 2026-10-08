# Review — PR 404 Redis dossier blockers owner packet, round 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 897910fcc1a186b91d436796bc6e5330836c60c1
Reviewer: fresh-context

Subject: `.syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`
at the head above, with its register rows P-105 to P-107 and dated note in
`PENDING-OWNER-DECISIONS.md`, its `decisions/README.md` row, and the
candidate files it routes to (`public-source-screening-scope-v3/`,
`dossier-agent-provider-v2/`, `dossier-handoff-options/CLAUSES.md`).
Merge-base with `origin/main` is `3f7572cf` (PR #403's merge). The PR is 21
files: 17 added, 4 modified (`git diff --name-status 3f7572cf 897910fc`).

This raw carries no `Manifest SHA-256` line. It is not a confirming review
of either candidate package under their review-head contracts.

## Round-1 revise findings: repaired

- [Observed] **Finding 1 (owner's 2026-10-03 reading).** Repaired. Packet
  "The rule, quoted" now carries the item: "Your direction of 2026-10-03 (the
  overnight beads loop), item 2: \"It changes nothing about what Syzygy the
  product may do: the product still coordinates no agents.\"" The quotation
  matches `OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md:34-35`. Option C
  now reads "Your reading of whether your 2026-10-03 item 2 reaches an agent
  launching on Syzygy's printed instructions". Option D reads "where Syzygy
  launches, it contradicts your 2026-10-03 item 2 outright, which would need
  superseding". The earlier sentence calling the prohibition development-only
  is gone from the packet. `CLAUSES.md:33-48` keeps the PWB-act citation
  (`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md:80-81`, which resolves) beside the
  owner's reading. It labels the reach to C and D [Inferred] and leaves that
  reading to the owner.
- [Observed] **Finding 2 (option B costs).** Repaired. Packet line 129, B row:
  "**Security cost:** Syzygy's printed command is non-interactive, so a tool
  call nobody approved fails rather than waits, and the tools must be
  pre-approved. The sessions then read untrusted clone text with no one
  present; a brief saying \"clone text is data\" does not stop an
  auto-approved session that obeys injected text. Mitigation: …
  [Inferred]. **Execution cost:** a permission to run Redis's code lapses
  when you leave the authoring session unattended (signed spec), so
  unattended stretches are reading-only." The lapse clause is at
  `polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:15`, as
  `CLAUSES.md:61-65` quotes it. The print-mode mechanism (round-1 note) is
  corrected and anchored to `design.md:57`
  (`` `claude -p "<prompt>"` ``). See finding N4 for a remaining gap.
- [Observed] **Finding 3 (`renderCondition` CSP clause).** Repaired in the
  bytes. Both patches' `renderCondition` (`…json.all.patch:43`) now read:
  "…the page carries a Content-Security-Policy whose default-src is 'none'
  and which carries no script-src, script-src-elem, script-src-attr or
  object-src directive. A consumer that cannot confirm this for a sink scans
  the body as before for that sink, and excludes it whole on a finding". The
  builder selftest gained one mutant per forbidden directive and one without
  `default-src 'none'`, all caught (26 of 26 held). The deployed CSP
  (`draft-preview.ts:18`: `default-src 'none'; style-src 'unsafe-inline';
  base-uri 'none'; form-action 'none'`) carries none of the four directives.
  [Inferred] With `default-src 'none'` and none of those four directives, no
  directive left can admit script into the page itself. `worker-src` falls
  back to `script-src`, and a frame needs an element that encoding forbids.
  The packet's paraphrase now matches (lines 51-53), except for the wording
  noted in N3.
- [Observed] **Finding 4 (affected identifiers).** Repaired.
  `SEMANTIC-DELTA.md:148-184` names REQ-polaris-generation-012 and states the
  reading it relies on: "for an exempt body, REQ-012's \"render … inertly\"
  and \"rendering executes none of that content\" are met by
  `renderCondition` … not by withholding the body". It also names what a
  contradicting reviewer would conclude. It names REQ-033 and REQ-025, and
  says no SEC, VIS or RFC clause is amended. Anchors resolve: base
  `spec.md:641` (the ID line; the body is at `:639`, the scenario at
  `:646-650`), overlay `spec.md:366`, local-agent `spec.md:31` (033's ID
  line; the quoted body sentence is at `:13`), `screen.ts:8-9`, and the
  warrants at base `spec.md:682`. The delta leaves RFC7-13, RFC7-14, RFC7-33
  and RFC7-34 [Unknown]. I read RFC7-14 ("The verbatim leaf",
  `rfcs/RFC-0007/narrative-contract.md:324-329`). It governs verbatim
  rendering of requirement text, not inertness, and states no stricter
  rendering rule [Observed]. RFC7-33 and RFC7-34 are titled "Every
  distinction, machine-readable" and "Non-visual recoverability"
  (`DIRECTIVE-REGISTER.md:412-413`). I did not read their bodies [Inferred
  from titles only: not rendering-inertness clauses].
- [Observed] **Finding 5 (egress and render population).** Repaired. Packet
  line 59, A cost: "Every newly admitted file can also be quoted on pages,
  put in review packets for your sessions, and sent to a provider in
  provider mode; those rules do not change, but the files they reach grow
  [Inferred: small, since your agent already reads the clone]". B: "The same
  growth as A, over fewer files." `IMPACT-LEDGER.md:79-93` anchors both
  populations (`spec.md:320`; `pipeline.ts:265`).

## Round-1 notes: handled

- [Observed] Note 6: the packet now scopes the claim to "the renderers the
  package names" and cites round 1's wider sweep for no other HTML sink.
- [Observed] Note 7: `IMPACT-LEDGER.md:11-16` and `:60-68` add the version
  literal sweep. `git grep -lF 1.3.0-public-source-candidate.1.none` over
  `packages apps scripts .github` at the head returns the same 6 files the
  ledger names.
- [Observed] Note 8: the packet drops the phrase rationale.
  `dossier-agent-provider-v2/SEMANTIC-DELTA.md:93-96` now says "The label
  avoids only that one stem … Only the version-aware form above removes the
  collision". Stems are confirmed at `gate-sources.ts:181`, `:225` and `:230`.
- [Observed] Note 9: the run facts carry "[Observed, as reported by the lead;
  this lane did not read the run directory.]". F1 is anchored to
  `docs/reviews/R-PR403-SCREEN-DOCS-1-RAW.md` (on main; line 42 says
  "Otherwise, ask the owner for a ruling or a statement successor…") and to
  `class-gate.ts`, which exists at the head.
- [Observed] Note 10: the sub-question now states the cost: "*Cost:* it has
  seen its own earlier verdict, which anchors the next one; this
  repository's own loops use a fresh reviewer each round."
- [Observed] Note 11: 1,543 words (`wc -w`), down from 2,082. That is about
  six to seven minutes, inside AC6. The clause chain moved to `CLAUSES.md`.
  The B row is still one long cell, about 150 words.

## What else was verified (no finding)

- [Observed] Digests (rule 3). I applied each `proposed/*.patch` with
  `patch -o` to the policy at the head and hashed the output. The results,
  `all` → `8f70c736…bd71027` and `non-web` → `44b8aab8…09b2334`, equal the
  two rows of `PUBLIC-SOURCE-SCREENING-SCOPE-V3-MANIFEST.txt:7-8`. They
  differ from round 1's rows, as the `renderCondition` repair requires. The
  base policy hashes `98a87f81…3f49`, the version-2 `none` row. The v2
  provider record hashes `b7a8d099…6df3`, equal to its manifest row. The
  packet quotes no digest. Its words to give name a variant or the record,
  and the act takes the manifest row at the sitting, which matches the
  version-2 phrase form round 1 checked.
- [Observed] Builders: both report `--check` current. `--selftest` held 26
  of 26 (screening v3) and 12 of 12 (provider v2).
- [Observed] Anchors re-derived at this head, after the rebase. Every file:line
  cited in `CLAUSES.md`, the v3 `SEMANTIC-DELTA.md` and `IMPACT-LEDGER.md`,
  and the v2 `SEMANTIC-DELTA.md` that I opened resolves to the quoted or
  described text: `…SCOPE-REVIEW-SIGNOFF-DIRECTION.md:56-60`; local-agent
  `spec.md:13`, `:15`, `:230` and `:320`; `design.md:57`, `:63-71` and
  `:77-80`; `security.md:90-93`; `inventory.ts:208`; `render.ts:276`, `:350`,
  `:372-375` and `:556`; `gate-sources.ts:113-114`, `:181`, `:220-238`,
  `:287-288`, `:291` and `:304`; `RFC5-…-CLASS-AMENDMENT-ACT.md:66`;
  `git-object-reader.ts:164` and `:191`; `screen.ts:85`;
  `public-source-screening.ts:138`; `dossier-render.ts:129`, `:261`, `:409`
  and `:440-452`; `draft-preview.ts:18`, `:24` and `:122`;
  `package-reader.ts:346-356`, `:371` and `:394-418`. The four scripts the
  ledger names (`install_redis_sitting.py`, `simulate_redis_sitting.py`,
  `record_public_source_screening_scope_v2_act.py`, and
  `public-source-classification.ts`) exist.
- [Observed by emulation] I ported `namesPolicy` (`package-reader.ts:80-88`,
  `:367-377`) and the Anthropic provider-statement stems to Python. The port
  returns no hit on the packet, `PENDING-OWNER-DECISIONS.md` or
  `decisions/README.md` at this head. The controls hit: the v2 policy act
  (scope stem and field line) and the v1 provider act (5 stems). The port
  approximates `\p{Default_Ignorable_Code_Point}` with six code points.
- [Observed] AC7. The modified files are `PENDING-OWNER-DECISIONS.md`,
  `decisions/README.md`, `docs/README.md` and
  `scripts/check_docs_review_campaign_partition.py`. Neither the base nor the
  head SHA-256 of any of them appears in any of the 2613 tracked files at the
  head. None is named in a `*MANIFEST*` file or in
  `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`. The only `-RAW.md` in
  the diff is the round-1 raw, which is added, not edited. `cmp` against the
  scratchpad copy reports no difference, so it is byte-identical. No file
  labels anything accepted or approved (case-insensitive grep for
  accepted/adopted/approved/in force over the packet and the three
  packages). Every hit is conditional ("once version 2 alone is in force")
  or names a proposed field. `check_governance.py` at the head reports 32 OK,
  21 WARN, 0 FAIL. The only PR file in its output is the round-1 raw, under
  CG-1f frozen-lane WARN. `check_docs_review_campaign_partition.py --check
  docs/README.md` passes: 380 files, 84 campaigns, 0 unmatched, 0 overlaps,
  and the second method matches.
- [Observed] Register arithmetic. Counting `^\| P-[0-9]+[^ |]*` per `##`
  section at the head gives 5 acceptance-act rows and 34 open rows, 39 in
  all, as the note states. `origin/main` has no row numbered P-105 to P-109.

## Findings

**N1 — The register says "no review has run", but round 1 has run** (low)

`PENDING-OWNER-DECISIONS.md:1026-1027`: "It binds nothing, and no review has
run on either candidate package." Rows P-105 (`:1126`) and P-106 (`:1127`):
"No review has run; offered only after a confirming one." [Observed] Round
1's subject names both packages (raw lines 6-9), and the raw is in this PR.
These sentences were true at round 1's commit. At this head they are false.
The packet's own banner gets it right: "none has run yet", where "none"
means a confirming review. Repair: "no confirming review has run".

**N2 — The dated note names the pre-rebase base** (note)

`PENDING-OWNER-DECISIONS.md:1031`: "on this branch over `origin/main`
`56c6c98c`". [Observed] The branch now sits on `3f7572cf`. The register is
byte-identical between the two commits, so the 39 count still holds. The
note now names a base that is not this branch's base. Either re-date it or
leave it and note the rebase.

**N3 — "The HTML check" is narrower than the bytes it paraphrases** (low)

Packet lines 34, 51 and 59, and row P-105: "skip the HTML check" and "the
Markdown HTML check". The bytes exempt the body from "the active-content
scan … [and] the malformed-code-context exclusion" (`…all.patch:42`).
[Observed] `scanActiveContent` (`git-object-reader.ts:164-172`, `:193-215`)
also reports `unsafe-url-scheme` (`javascript:`, `vbscript:`, `data:`,
`file:`), `event-handler-attribute`, `html-comment-or-declaration`,
`obfuscated-link-destination`, `script-element`, `svg-element` and
`malformed-code-context`. All of these stop applying to an exempt body.
[Inferred] `renderCondition` ("never mint a link, element, attribute, script
or handler") covers them, so the risk is small. The owner still reads a
narrower exemption than the one they would bind. A JavaScript file with an
`onclick=` string or a `javascript:` URL is admitted under `all` as well. A
related wording issue: line 52 says "under a policy whose `default-src` is
`'none'`", in a decision about a screening *policy*. Write
"Content-Security-Policy". Repair: "skips the active-content check (HTML
tags, script and unsafe links)", or similar.

**N4 — B's "Yes, for the helper sessions" does not say what the overnight run still needs from the authoring session** (low)

Packet line 129, B row, column 2: "Yes, for the helper sessions". [Inferred]
For the run to progress while the owner is away, the authoring session must
also continue unattended after each verdict. That needs its own tool calls
pre-approved, or it stalls at a prompt just as the helpers would. It is also
the session with the widest tools (it drafts, and runs `syzygy dossier`
steps), and it reads the same untrusted clone. The row states the security
cost only for the helper sessions and the execution lapse only for the
authoring session. It never says whether B by itself makes an overnight run
progress, or what approval posture the authoring session needs for that.
This is not a revise: the scope "for the helper sessions" is honest, and the
lapse sentence implies unattendance. One clause would close the gap: "the
authoring session must also run unattended, with the same cost".

**N5 — One consequence claim is unlabeled** (note)

Packet lines 83-84: "README-based claims then cannot be reviewed and render
Unknown." [Observed] The package states the same thing as [Inferred]
(`dossier-agent-provider-v2/SEMANTIC-DELTA.md:54-57`). Carry the label
(rule 8, epistemic labelling).

## Verdict basis

All five round-1 revise findings are repaired, with the new text quoted
above. Round 1's six notes are handled. Every digest recomputes, both
builders pass `--check` and their selftests, every cited line resolves at
the rebased head, and no act-bound bytes or raw are edited. N1 and N3 are
small factual and paraphrase errors. N4 is a gap in a trade-off. N2 and N5
are notes. None changes a decision, an option, or a phrase to give.

Verdict: CONFIRM WITH EXCEPTIONS
