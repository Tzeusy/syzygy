# R-PUBLIC-ADMISSION-2 — public-repository admission package
Reviewed commit: aef2c6add6579f6aff3862158e591bd39e05c843
Verdict: REVISE
Reviewer: fresh-context subagent, 2026-10-03

Scope read: every tracked file under
`.syzygy/governance/contracts/candidates/public-repo-admission/` except
`reviews/` (packet, three templates, `instances/requests/` two records and
`params.json`) and `scripts/build_public_repo_admission.py`, against SEC-2,
SEC-3, SEC-5; RFC5-12…RFC5-17; RFC3-16, RFC3-16(a), RFC3-30; RFC4-1, RFC4-2;
REQ-polaris-generation-001, 017, 025; `ADAPTER-DECLARATIONS.md`; the policy
JSON; the three precedent decisions; `docs/polaris-generation/TARGETS.md` and
`README.md`. `git rev-parse HEAD` equalled the reviewed commit before reading.

Verified [Observed]:
- `python3 scripts/build_public_repo_admission.py --check` prints
  "public-repo admission instances: current", rc 0; `--digests` output equals
  `sha256sum` of both instance files on disk; `--selftest` rc 0.
- On a scratch copy outside the worktree (`git archive HEAD`): editing one
  byte of `OBSERVATION-CONSENT.md` makes `--check` print `STALE` and exit 1;
  a lowercase `{{owner}}` left in a template raises "placeholder left after
  fill". Selftest mutants: see finding 5.
- `git ls-remote https://github.com/psf/requests 'refs/tags/v2.34.2*'` (refs
  only) returns `6e83187b8feb273ed4c6cdab5efd8d54901dfab3` with no peeled line,
  matching the instance and TARGETS.md line 37.
- `python3 scripts/check_governance.py` at this commit: 31 OK, 21 WARN, 0 FAIL;
  no line names a file in this package.
- Round-1 dispositions 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13 and 14 are carried
  out in the bytes (scope population stated once, template lines 31–35 and
  packet line 62–63 agree; subject `project:syzygy`; dependent fields listed,
  packet lines 80–82; "requires exactly one", line 66–67; Q4 lines 114–116;
  review credited at line 157; registry entry in summary line 22; Q7 and
  outline item 5; egress `## Scope` and provenance lines; REQ-010 removed;
  no `pending` in any instance; observation Effect adds dependent-claim
  Unknown). Disposition 9 is carried out in form but misdescribes the policy
  (finding 1). Disposition 4 is carried out with gaps (finding 3).

## Findings

1. **blocking — the outline misstates what the existing policy calls active content, and hides that the unchanged rule would withhold ordinary source files.**
   `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md` lines 19–22: "The
   existing policy withholds active content (executable configuration such as
   TOML, CI workflows and build files outside an inert context). The public
   scope keeps that rule; such files are counted as withheld, never read into
   a prompt." The policy defines active content as a closed list of markup
   *forms*, not file kinds: `activeContentClassification.excludedOutsideInertContexts`
   = `html-element`, `html-comment-or-declaration`, `svg`, `script`,
   `event-handler-attribute`, and three `unsafe-url-scheme-*` entries; its
   only inert contexts are `inertMarkdownContexts` = `inline-code-span`,
   `fenced-code-block`. TOML, CI workflows and build files appear nowhere in
   it (the Butlers `butler.toml` withholdings arise because a form occurs and
   "TOML has no inert context", not because TOML is listed). Consequence the
   owner is not shown [Inferred]: in a `.py`, `.c`, `.ts` or `.tsx` body no
   context is inert, so any `<tag`-shaped string, JSX element or
   `javascript:` literal withholds the whole file — plausibly most of
   Sentry's frontend and some of every target — while TOML or YAML with no
   such form is *not* withheld. Item 2's proposed success rule repeats "no
   active-content form outside an inert context" without defining inert
   contexts for non-Markdown files. Governing: acceptance criterion 6
   (factual claims about existing records true); REQ-polaris-generation-025:
   "Existing project-specific admission, grammar and policy gates SHALL NOT be
   widened by generic schema support or fallback" — the owner must see
   exactly which gate is kept and which replaced; R1 finding 9's repair asked
   for exactly that ("which the public scope replaces (active-content
   handling for non-Markdown files …)"). Repair: describe the rule as the
   policy states it (closed form list, Markdown-only inert contexts), state
   its effect on source-code bodies, and make the choice explicit — keep it
   (and accept withheld code files, counted) or define the public scope's own
   active-content handling for non-Markdown files (e.g. bodies are never
   rendered as HTML, so forms are encoded rather than withheld) — as an owner
   question or an explicit outline item.

2. **blocking — the shape puts the provider execution route in a per-target registry entry, which RFC4-1 forbids under the packet's own observation model.**
   `OWNER-DECISION-PACKET.md` lines 59 and 65–67: under "**Per target:**",
   "4. **Registry entry** for the target's source-acquisition observer and the
   provider execution route (REQ-polaris-generation-017). RFC4-1 requires
   exactly one registered adapter per project per external authority." RFC4-1:
   "Every external authority is reached through exactly one registered adapter
   per project; nothing else in Syzygy touches that authority directly." With
   every target observed by `project:syzygy` (lines 26–31, Q4), the provider
   is one external authority of one project, so a provider route registered
   per target is a second, third … adapter for the same authority in the same
   project. The egress template (line 20–21) already speaks of "the
   registered provider execution route", singular. Governing: RFC4-1 as
   quoted; REQ-polaris-generation-017: "External authorities SHALL be
   accessed through their single registered adapter per project, never a
   competing direct route." Repair: move the provider execution route to
   "**Once**" (one registry entry per (project, provider)), keep only the
   source-acquisition observer per target, and say whether the upstream host
   (GitHub, reached by fetch) is itself an external authority with one
   adapter per project or whether each target's observer only reads an
   operator-supplied clone.

3. **note — Q5 omits half the records it governs and the recorder the precedent relied on.**
   `OWNER-DECISION-PACKET.md` lines 118–120: "The secret policy and egress
   consent are honored only under an effective owner act under RFC3-16(a)
   (RFC5-15, RFC5-16, RFC3-30), so each is bound to its record's exact
   digest." RFC3-16(a) lists as in-scope "a **consent record** — observation,
   write, egress, or execution", and RFC-0004 line 39 says "a registry entry
   is honored **only under RFC3-16(a)**"; the observation consent and the
   registry entry are absent from Q5's sentence, and the Scope A remark (lines
   128–130: "does not cover consent or policy records") is silent on registry
   entries, which Scope A item 1 *does* name for PWB ("the observer registry
   entry"). Also, the precedent act (`PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
   lines 39–58) was option selection naming acts "at the manifest rows", with
   the provenance state "explicitly selected by the owner's option selection"
   (line 17–18) and a recorder that "rejects an argument that is not this
   subject's row" (line 57). Q5 names the builder's `--digests` but no
   recorder, no `check_governance.py` registration, and does not say the
   option must select state (1) explicitly. Repair: extend Q5's first
   sentence to all four record kinds, say how per-target registry entries
   are signed, and list the recorder (validating the selected digest against
   regenerated bytes and writing the act record) and the explicit state-(1)
   selection as offering prerequisites.

4. **note — the egress record takes the sole `(project:syzygy, anthropic)` slot and Q4 does not weigh it.**
   `templates/EGRESS-CONSENT-TEMPLATE.md` lines 1, 12, 42–44: "Public-target
   egress consent", Record ID `PUBLIC-EGRESS-{{PROVIDER_ID}}`, "Every other
   source of `project:syzygy` content is outside this consent, including the
   Butlers repository, Syzygy's own repository and any work history". RFC5-12:
   egress consent is "**one record per *(Project, provider)* pair**". Any
   later Anthropic egress of Butlers or Syzygy content (Polaris generation on
   either) must therefore be a new version of this "public-target" record,
   coupling its revocation history to the public targets'. That is a cost of
   Q4's recommendation (lines 110–116), which argues only the policy cost of
   the alternative. Repair: either name the record for the pair (e.g.
   `EGRESS-syzygy-anthropic`) and say other sources are added by later
   versions, or state the coupling in Q4 as a trade-off.

5. **note — the selftest does not exercise the predicates the docstring and criterion 4 rely on.**
   `scripts/build_public_repo_admission.py` line 12: "--selftest  mutate a
   field and an unfilled placeholder; both must be caught". The selftest
   (lines 52–67) tests an unfilled field and a missing header; it never
   mutates an instance or a field value, and never reaches the
   "placeholder left after fill" branch (line 37). Scratch-copy mutants
   [Observed]: (a) line 37 replaced by `if False:` — selftest passes;
   (b) `path.read_text() != text` replaced by `False` (staleness check
   disabled) — selftest passes, `--check` passes on a stale tree; (c) the
   header lambda replaced by `m.group(0)` (template banner kept) — selftest
   passes (it asserts only `endswith("v 2\n")`). Also, an unknown mode
   (`--bogus`) exits 0 having done nothing, `--check` ignores instance files
   no `params.json` entry produces, and the builder is wired into no battery
   step. Governing: AGENTS.md verification rule 6, "Mutate the input and
   confirm the check fails, per predicate". Repair: make the docstring match;
   add fixtures for the placeholder-left branch, the header replacement
   (assert the instance head) and the staleness comparison (run `--check`
   logic over a temp tree with one mutated byte); reject unknown modes.

6. **note — the outline is silent on raw-body handling, which Q3 and Polaris rendering would change.**
   `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md` lines 23–26 name
   `"externalEgress": "never"` as "the substantive change". The same policy
   object sets `rawBodyHandling` `storage`, `logging`, `rendering`,
   `machineResponse` all `"never"` and `accessBoundary.networkEgress: false`.
   Q3's recommendation (packet lines 104–107) retains "provider replies and
   run records" — which, if they carry prompts, carry bodies — and a page
   that quotes source verbatim renders bodies. Repair: state in the outline
   which `rawBodyHandling` and `accessBoundary` fields the public scope
   changes (or that it changes none, with the consequence for run records
   and quotation), so item 4 is not the only visible widening.

7. **note — observation template: hard-coded supersession, fetch population, and "effective".**
   `templates/OBSERVATION-CONSENT-TEMPLATE.md` line 27: "Proposed revocation
   state: active; supersedes no earlier consent" is literal, not a field, so
   the later record that adds revisions for a target (Redis needs three,
   TARGETS.md lines 60–69) cannot be generated truthfully; the egress template
   parametrizes it as `{{SUPERSEDES}}`. Lines 37–38: "The operator fetches
   those objects into a local clone" — an ordinary fetch transfers ancestor
   commits the grant (lines 33–35) excludes; say a shallow single-commit fetch
   or that the transferred excess is never read. Lines 40–41: "screened under
   `project:syzygy`'s public-source screening scope" lacks "effective",
   whereas REQ-polaris-generation-025 says "Missing/invalid policy authority
   SHALL block ingestion" and the egress template (line 48) says "effective".
   Repair: add a `{{SUPERSEDES}}` field, state the fetch form, add
   "effective … ; without it nothing is ingested".

8. **note — Q7 does not mention licence files, on which T2's changed-source proof depends.**
   `OWNER-DECISION-PACKET.md` lines 137–147 and outline lines 34–37 route all
   prose not spec/design to indeterminate under option (b). TARGETS.md lines
   54–69 make Redis's licence change across three revisions the portability
   proof ("must change every place the page states or implies the licence").
   A `LICENSE` file is not "Doctrine, spec, decision, policy text" (RFC5-14)
   on its face, so under (b) it would be unsent and the T2 proof could not run
   until (a) lands. Repair: name licence files in Q7 and say whether (b)
   blocks T2.

9. **note — sibling package patches the same policy file.**
   `OWNER-DECISION-PACKET.md` lines 152–153: "It does not touch … the
   self-observation package on PR #120." True, but PR #120 carries
   `proposed/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json.patch`,
   a patch to the same digest-bound policy this package's item 1 extends
   [Observed, `gh pr view 120` file list]. The outline's "drafted against
   that policy's then-current bytes" covers it implicitly. Repair: say
   explicitly that whichever policy act lands second is re-drafted and
   re-reviewed against the other's bytes.
