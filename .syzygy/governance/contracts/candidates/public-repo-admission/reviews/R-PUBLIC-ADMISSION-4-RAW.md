# R-PUBLIC-ADMISSION-4 — public-repository admission package
Reviewed commit: dc5cf98d3603c6bbed35cb551ef825bf6aef9b8c
Verdict: REVISE
Reviewer: fresh-context subagent, 2026-10-03

Scope read: every file under
`.syzygy/governance/contracts/candidates/public-repo-admission/` except
`reviews/` (the packet, three templates, `instances/requests/` with two
records and `params.json`), `scripts/build_public_repo_admission.py`, and
`.syzygy/governance/decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`.
I read the R3 raw for its findings only. Governing references read: RFC5-12…RFC5-15
(`consent-egress-secrets.md`); RFC4-1 and the RFC-0004 §0 line 38–39;
REQ-polaris-generation-025 (spec line 1400); the policy JSON
(`accessBoundary`, `rawBodyHandling`, `classificationSuccess`,
`inertContextRule`, `excludedOutsideInertContexts`, path-deny lists); the
re-pin act (Ceremony section); `POLARIS-RESPONSE-CEILING-READING-DIRECTION.md`
(shape); `PROJECT-STATUS.md` row on the PWB machine-view amendment;
`docs/polaris-generation/TARGETS.md` line 37. `git rev-parse HEAD` equalled
the reviewed commit before I read anything.

Verified [Observed]:
- `--check`: "public-repo admission instances: current", rc 0.
  `--selftest`: "6 of 6 mutants caught (banner kept, unfilled field,
  placeholder in value, missing banner, stale instance, orphan record)", rc 0.
  The `--digests` output equals `sha256sum` of both instance files
  (`c30488d7…` egress, `6637b379…` observation). `--bogus`: "unknown mode
  --bogus", rc 2.
- `git ls-remote https://github.com/psf/requests 'refs/tags/v2.34.2*'` →
  `6e83187b8feb273ed4c6cdab5efd8d54901dfab3`. This matches the observation
  instance and TARGETS.md line 37.
- `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52
  checks)".
- The policy's `excludedOutsideInertContexts` has eight entries. Outline item 3
  names all eight. The `accessBoundary` fields named in outline item 4 match
  the JSON's seven keys, all `false`. `rawBodyHandling` is `never` for all
  five sinks. `.pem` is in `deniedPathSuffixes`, and `.env` and `id_rsa` are
  in `deniedPathBasenames`.
- Q5's account of the precedent matches the re-pin act's Ceremony section,
  lines 30–58: the packet "by design carries no digest"; the option names both
  acts "at the manifest rows"; "the recorder rejects an argument that is not
  this subject's row"; state (1) is at lines 17–18.
- Q6: `PROJECT-STATUS.md` line 234 records that the performed PWB
  machine-view amendment names "the generated editorial draft view
  (`/polaris/draft/<runId>`)" and "Authorizes no implementation". The packet's
  "named … but not yet implemented" is therefore true.
- RFC4-1 quote at packet 52–53 matches `general-contract.md` line 74.
  RFC-0004 "honored **only under RFC3-16(a)**" matches line 39. The REQ-025
  quote at packet 82–83 matches spec line 1400.
- The direction file has the plain-direction shape of the ceiling-reading
  precedent: owner's words verbatim in a table, "binds no artifact digest,
  adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers nothing", and "It
  performs no act". It labels the Q1 consequences [Inferred] and the
  transcript question [Unknown].

R3 dispositions in the bytes:
- 1: carried out. Q3, the egress retention field and outline item 4 all place
  sent spans in the run directory. The Q1 answer's transcript clause reopens
  the same class of defect (finding 1).
- 2: carried out (outline item 2 path rules; item 4, every `accessBoundary`
  field).
- 3: carried out (eight entries).
- 4: carried out (Q5 rewritten from the Ceremony section; manifest, recorder
  and `check_governance.py` registration listed).
- 5: partly carried out. Instruction text is now in scope, but no content
  class is named (finding 3).
- 6, 7, 8, 9, 10: carried out (R1 row 9 marked; observation template line
  40–42 defers to the source-acquisition entry; Q6 names the prospective view
  and the local-file fallback; builder refuses stale `--digests` and reports
  orphans; "fixes" at packet 59 and 134; RFC3-16(a) credited at 84).

Owner answers in the instances:
- Q1: egress title, Provider field and `params.json:16` read "Anthropic,
  through the Claude Agent SDK (Claude Code runtime)". The subject is
  `(project:syzygy, provider:anthropic)`. Both direction conditions are
  present: tools disabled (instance 60–62) and transcript retention
  (instance 31). Followed.
- Q2: five classes, `work-history` absent. Followed.
- Q3: run directory, outside git, not in logs or machine responses. Followed,
  except finding 1.
- Q4: `project:syzygy` observes `repository:psf-requests`. Followed.
- Q5, Q6, Q7: packet text and outline items 4 and 5 agree. No instance field
  depends on them beyond the provenance line, which states state (1).
  Followed.

## Findings

1. **blocking — the egress record lets the runtime hold requests and replies outside the run directory, contradicting the Q3 answer, the direction and the paired screening outline.**
   `instances/requests/EGRESS-CONSENT-ANTHROPIC.md:31` (from
   `params.json:19`): "Whether the runtime can be configured not to persist a
   transcript is Unknown until the adapter is built; until then any
   transcript it writes elsewhere is moved into the run directory before the
   run completes."
   A session transcript carries every request and reply, and so carries the
   source spans sent. This sentence approves storing those spans outside the
   run directory (wherever the runtime writes) for the length of the run. If
   a run fails or is killed, "before the run completes" never happens, and
   the spans stay there with no bound.
   - **Q3 answer** (decisions file line 30): "Requests, replies and run records stay in a per-run directory under Syzygy's state directory, never in git, logs or machine responses."
   - **Direction item 2** (line 44–45): "any session transcript the runtime persists locally is retained material, kept in the run directory under Q3."
   - **Outline item 4** (`templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md:46–48`): "storage — permitted only in a run's directory under `project:syzygy`'s state directory, outside git".

   R3 finding 1 was blocking for the same kind of disagreement between the
   retention line and the paired storage rule. The owner, signing this record,
   would approve a storage path that the Q3 answer and the outline both rule
   out.
   Repair: replace the sentence with a fail-closed condition, e.g. "any
   transcript the runtime persists is written inside the run directory; a run
   whose runtime cannot be so configured does not start". If transient
   storage elsewhere is really intended, it needs its own owner answer and a
   matching line in outline item 4. Keep the Unknown about whether
   persistence can be turned off.

2. **note — Q3's recommendation sentence is garbled.**
   `OWNER-DECISION-PACKET.md:119–121`: "*Recommended:* provider replies and
   run records are provider requests, provider replies and run records are
   retained in a run directory …". This was introduced by the R3 repair
   (`63ab6cf`). The owner answered a separately worded CLI question
   (decisions file line 30), so the garble did not shape the answer.
   Governing: acceptance criterion 3 (a reader must be able to tell what the
   recommendation says). Repair: delete the first "provider replies and run
   records are". The fix is to the packet's own recommendation text, not to
   the question as put.

3. **note — the generator's own instruction text is admitted to scope but given no content class, so every request would be refused or classed by the composer.**
   `instances/requests/EGRESS-CONSENT-ANTHROPIC.md:45–47`: "together with
   the generator's own instruction text (its stage prompts and response
   schemas, authored in Syzygy's repository), which every request carries."
   Outline item 5 classifies only target content. Generator prompts are not
   "Doctrine, spec, decision, policy text", and if they live in source files
   they are `project:syzygy` `code-content`.
   - **RFC5-14**: "Content class is a **property of what enters the choke point, tracked from where the content originated**, never an attribute the composing step asserts about its own output".
   - **RFC5-14**: "a composite whose class cannot be determined is refused egress".

   R3 finding 5's repair asked for the class and source paths when the text is
   in scope. Only the scope half was done.
   Repair: name the class, for example `code-content` of `project:syzygy`
   restricted to the generator's prompt and schema paths. Name those paths, or
   the rule that selects them, in the record or in outline item 5.

4. **note — the tools-disabled condition is not enough for the "model sees only what each request carries" claim on this route [Inferred].**
   `instances/requests/EGRESS-CONSENT-ANTHROPIC.md:60–62`: "The route
   invokes no tools … so the model sees only what each request carries."
   Depending on configuration, a Claude Code / Agent SDK runtime can add
   context the generator did not compose:
   - instruction and memory files it loads from the user's and working directory's settings;
   - environment details such as working directory and git status;
   - MCP servers declared in settings;
   - non-essential network traffic (telemetry, error reports) to destinations other than the consented provider.

   If it runs inside Syzygy's checkout, those files are `project:syzygy`
   content outside this record's scope. The owner's Q1 option already warned
   that "the egress check and audit record need extra work".
   - **RFC5-15**: "every network transmission of governed-project content passes one consent check naming (provider, content classes, project)".

   Repair: add a condition, or an adapter acceptance criterion named in the
   record. The runtime loads no filesystem settings, memory or MCP
   configuration. Its working directory is the run directory. Non-essential
   traffic is disabled. The egress check and audit record see the request as
   the runtime sends it, not as the generator composed it.

5. **note — "the provider's own retention is as its terms state" no longer says which terms.**
   `instances/requests/EGRESS-CONSENT-ANTHROPIC.md:31`: "The provider's own
   retention is as its terms state, disclosed rather than promised." Under the
   Q1 recommendation these were API terms. Packet line 124–125 still says
   "whatever its API terms say". The chosen option says "Uses your existing
   subscription". Subscription and commercial API accounts may be governed by
   different terms, with different retention and model-training settings
   [Inferred]. "Disclosed" then discloses nothing.
   Governing: the kit's retention field as adopted by this record (packet Q3,
   README "Start here" step 4: an egress decision "must also name the
   destination route and retention for sent" content). Repair: name the
   account type and the terms document that governs it. Record the
   training-use setting in force as a disclosed fact at offering. Add a packet
   note that Q3's "API terms" predates the Q1 answer.

6. **note — the direction says the packet "remains the question", but the same commit edited it.**
   Decisions file lines 9–11: "The packet remains the question; its drafts
   are regenerated to follow these answers." `dc5cf98` changed packet lines
   87–89 and added the "Answered 2026-10-03" block (97–101). The precedent
   direction says "The packet remains the question and is not edited." The
   edits are additive and accurate, and the questions themselves are
   unchanged. Repair: none required. Optionally: "The packet's questions
   remain as put; it gains a pointer to this direction."
