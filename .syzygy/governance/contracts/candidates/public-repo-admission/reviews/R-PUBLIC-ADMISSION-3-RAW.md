# R-PUBLIC-ADMISSION-3 — public-repository admission package
Reviewed commit: fda60876bf679fadce6254a6849278b8750405bc
Verdict: REVISE
Reviewer: fresh-context subagent, 2026-10-03

Scope read: every file under
`.syzygy/governance/contracts/candidates/public-repo-admission/` except
`reviews/` (packet, three templates, `instances/requests/` two records and
`params.json`) and `scripts/build_public_repo_admission.py`; R1 and R2 raws
for the dispositions only. Governing references read: SEC-2
(`doctrine/security.md`); RFC5-12…RFC5-17; RFC3-16, RFC3-16(a); RFC3-30;
RFC4-1, RFC4-7 and the RFC-0004 §0 reader map; REQ-polaris-generation-001,
017, 025 (base spec; the understanding amendment overlays none of the three);
the policy JSON; the re-pin act, the Butlers observation consent act, the
2026-10-02 owner-instructions record, the Scope A direction;
`docs/polaris-generation/TARGETS.md` and `README.md` "Start here".
`git rev-parse HEAD` equalled the reviewed commit before reading.

Verified [Observed]:
- `--check`: "public-repo admission instances: current", rc 0. `--selftest`:
  "5 of 5 mutants caught", rc 0. `--digests` equals `sha256sum` of both
  instance files. `--bogus`: "unknown mode --bogus", rc 2.
- Rule-6 mutants on a scratch copy (`git archive HEAD` into the session
  scratchpad, outside the worktree), each run under `--selftest`:
  - M1 `raise KeyError(...)` → `return m.group(0)`: rc 1.
  - M2 `if "{{" in out:` → `if False:`: rc 1, "placeholder left after fill not caught".
  - M3 `lambda m: m.group(1) + head` → `lambda m: m.group(0)`: rc 1.
  - M4 `if n != 1:` → `if False:`: rc 1, "missing header not caught".
  - M5 `p.read_text() != text` → `False`: rc 1, "stale instance not caught".
  - Each of the five predicates main() relies on is guarded; `--check` uses
    the same `stale()` the selftest drives. Unguarded but harmless: M6
    (`not p.exists() or ` removed: rc 0, but a missing instance then raises
    FileNotFoundError, failing closed); M7 (common/entry merge order) and M8
    (`count=0`) are equivalent mutants on current inputs.
- `git ls-remote https://github.com/psf/requests 'refs/tags/v2.34.2*'` →
  `6e83187b8feb273ed4c6cdab5efd8d54901dfab3`, matching the instance and
  TARGETS.md line 37.
- `python3 scripts/check_governance.py`: 31 OK, 21 WARN, 0 FAIL; no line
  names a file in this package.
- Quotes checked against their clauses and true: RFC3-30 (packet 30–31),
  RFC4-1 (packet 52–53), RFC5-14's `derived-composites` sentence (106–108),
  RFC5-14 class definitions (158–159), the policy's `classificationSuccess`
  fragment (outline 13–14), `inertContextRule` paraphrase (outline 28–30),
  `rawBodyHandling` all `never` (outline 32–34), REQ-025's
  separately-revocable sentence (82–83), RFC-0004 "honored only under
  RFC3-16(a)" (135; §0 line 39 and RFC4-7 line 191), Butlers observation
  act bound to its record's exact digest (133–134), policy owning project
  and Butlers subject `project:syzygy` / `repository:butlers-configured-poc`
  (27–28), generator specification adopted (PROJECT-STATUS.md;
  `POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`), SEC-2 states no
  retention field (110–111), the kit's "Start here" step 4 proposes route and
  retention (111–112).

R2 dispositions in the bytes:
- 1 carried out (outline item 3), with one omission (finding 3).
- 2 carried out (packet items 2 and 5; item 5 labelled [Inferred]).
- 3 carried out (Q5 names all four record kinds, state (1), the recorder);
  the precedent is misdescribed (finding 4).
- 4 carried out (Q4 lines 124–128).
- 5 carried out for selftest and modes (above); `--check` still ignores
  instance files no `params.json` entry produces (finding 9).
- 6 carried out for `rawBodyHandling`; `accessBoundary` is not addressed
  (finding 2).
- 7 carried out (`{{SUPERSEDES}}`, `--depth=1` by commit, "effective").
- 8 carried out (Q7 lines 165–167).
- 9 carried out (packet 174–177; outline 65–69).

## Findings

1. **blocking — the egress record's retention line and the screening outline's storage rule contradict each other about whether source bodies are kept.**
   `instances/requests/EGRESS-CONSENT-ANTHROPIC.md:31` (from `params.json:19`),
   with the same wording in packet Q3 lines 112–115: "provider replies and run
   records are retained in `project:syzygy`'s state directory, outside git;
   source bodies are not retained beyond the run's local clone". Outline item 4,
   `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md:37–39`: "storage —
   permitted only in a run's directory under `project:syzygy`'s state
   directory, outside git (provider requests, replies and run records quote
   source; packet Q3)". A stored provider request is a prompt, and a prompt
   carries the `code-content` bodies it sends, so source bodies *are*
   retained beyond the local clone, in the run directory. The retention
   sentence also leaves out provider requests. The owner signs both records,
   and answering Q3 on its recommendation approves a retention statement
   that the paired policy permits breaking. Governing: RFC5-14, "Governed-project content
   leaves owner-controlled infrastructure only under a recorded
   egress-consent record naming the **provider** and the permitted
   **content classes**", plus the kit's own retention field, which this
   record adopts as the record's condition. RFC3-30 puts the "retention
   bound (RFC4-16)" under the observing project's policy, so the two records
   must agree. Repair: pick one statement and use it in Q3, the egress
   retention field and outline item 4. Either "provider requests (which embed
   sent bodies), replies and run records are retained in the run directory,
   outside git, until <bound>", or "requests are not stored; replies and run
   records keep only spans the policy admits". Name the bound or say it is
   unbounded.

2. **note — the outline does not say how the public scope treats `accessBoundary` or `sourceAdmission`'s path-deny rules.**
   `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md:9–11` says "The
   existing secret detectors apply unchanged", and line 44 says "Every other
   scope stays as it is". The policy also sets
   `accessBoundary.networkEgress: false` and carries `sourceAdmission`
   denied basenames, prefixes and suffixes (`.env`, `id_rsa`, `.pem`, `.key`
   …) plus `gitObjectsOnly: true`. Those are not detectors. Item 2's
   success rule also drops the existing rule's first conjunct ("its
   normalized path is admitted by its current discovery phase"). So a
   reader cannot tell whether a committed `id_rsa` in a target is excluded
   by path, or whether the public scope's egress conflicts with
   `networkEgress: false`. R2 finding 6 asked for "`rawBodyHandling` and
   `accessBoundary`"; only the first was done. Governing:
   REQ-polaris-generation-025, "Existing project-specific admission, grammar
   and policy gates SHALL NOT be widened by generic schema support or
   fallback". Repair: add an item stating, for the public scope, the
   `accessBoundary` values (or that `networkEgress` governs only Syzygy's
   observer and provider egress travels the RFC5-15 choke point), that the
   path-deny lists and `gitObjectsOnly` apply unchanged, and what admits a
   path (the observation consent's revision objects).

3. **note — the "closed list" in outline item 3 is missing one of its eight entries.**
   `templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md:20–23`: "a closed list
   of markup forms (`excludedOutsideInertContexts`: HTML elements, HTML
   comments and declarations, SVG, script, event-handler attributes, unsafe
   URL schemes in Markdown destinations and autolinks)". The policy's array
   has eight entries, and the list omits `unsafe-url-scheme-in-html-attribute`.
   The R2 row 1 disposition (packet line 205) says the item "quotes the
   policy's closed markup list". Governing: acceptance criterion 6.
   Repair: add "and in HTML attributes", or quote the eight identifiers.

4. **note — Q5 credits the re-pin precedent with features its record does not show.**
   Packet lines 136–138 say "the 2026-10-02 policy re-pin act was given by
   option selection over an exact SHA-256 digest". Lines 143–147 say "As in
   that precedent, each option states the provenance state it selects —
   state (1) …". The option the owner selected,
   verbatim in `decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md:44–46`
   and `decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md:24–26`,
   reads: "Perform both acts at the manifest rows and give direction C; …".
   It names manifest rows, not a digest. It does not state a provenance
   state; the act record asserts that state (1) was "explicitly selected by
   the owner's option selection" (line 17–18). The rest of the question text
   is "[Unknown beyond these words and the parenthetical below]" (owner
   instructions line 20). So naming the digest and the state in the option
   is an improvement on the precedent, not a repeat of it. Repair: "was given by option
   selection binding each act to its manifest row's digest"; "Unlike that
   precedent's option text, each option here names the record, its digest
   and state (1) explicitly". Q5 should also list the
   `check_governance.py` `_act_subjects()` / `ACT_DIGEST_COPY_FILES`
   registration as an offering prerequisite (repository recorder convention).

5. **note — the egress scope literally excludes the generator's own instruction text, which every prompt carries.**
   `templates/EGRESS-CONSENT-TEMPLATE.md:42–44` (instance 45–47): "Every
   other source of `project:syzygy` content is outside this consent,
   including the Butlers repository, Syzygy's own repository and any work
   history, and stays unsent." Every prompt is a `derived-composites`
   (packet line 106), composed from target content plus pass instructions
   authored in Syzygy's repository (`docs/polaris-generation/AUTHORING.md`
   and the generator's prompts). SEC-2 covers "anything derived from" governed
   content, "including prompts". Read literally, the record refuses every
   run. Read loosely, an implementation decides alone which Syzygy bytes
   count. Governing: RFC5-14, "Content class is a **property of what enters
   the choke point, tracked from where the content originated**". Repair:
   state that the generator's own instruction text is in scope or out of
   scope. If it is in scope, name its class (e.g. `governance-text`) and its
   source paths. If it is out of scope, say why it is not governed-project
   content.

6. **note — the R1 row 9 disposition now describes the outline wrongly.**
   Packet line 197: "Outline: active content withheld as in the existing
   policy; egress named as the change". Since R2 the outline replaces the
   active-content rule for non-Markdown files (outline 24–31: "This is a
   change the act approves, not a carry-over"). Repair: append
   "(superseded by R2 row 1)" to the row.

7. **note — the observation template prejudges the question item 5 leaves open.**
   `templates/OBSERVATION-CONSENT-TEMPLATE.md:43–44`: "Reads are selected by
   the registered source-acquisition observer for this pair". Packet lines
   75–79: "Whether this is one entry per target or one shared Git-hosting
   adapter is decided when it is drafted". Repair: "by `project:syzygy`'s
   registered source-acquisition observer".

8. **note — Q6 recommends a route that does not exist.**
   Packet lines 152–153: "only on the local daemon's draft route".
   [Observed] `apps/three-surface-poc/src/routes.ts` contains no "draft".
   `renderDraftPreview` is called only from `self-corpus.ts`,
   `pipeline-demo-main.ts` and tests. Repair: "only as a local editorial
   draft (today a demo output file; a daemon route if one is later
   authorized)".

9. **note — builder residue.**
   `scripts/build_public_repo_admission.py:116–119`: `--digests` prints the
   digest of the *regenerated* text without checking that the on-disk file
   matches. Packet Q5 lines 142–143 say the digest "is what an option would
   name". A stale tree would therefore offer a digest of bytes that are not
   on disk. `stale()` (97–99) also ignores instance files no `params.json`
   entry produces (R2 finding 5, not dispositioned). Repair: have
   `--digests` refuse when `stale()` is non-empty, and flag unlisted `*.md`
   under each instance directory.

10. **note — two citations attribute slightly more than their clauses say.**
    Packet line 60: "RFC5-12 allows 'one record per *(Project, provider)*
    pair'". The clause fixes the granularity ("Not one record per content
    class"); it does not merely allow it. Q4 line 125 repeats "allows".
    Packet lines 81–83 credit REQ-025 for "Each numbered item is its own
    record with its own act", but the quoted sentence governs the consent
    "permissions". Separate acts for the policy and the registry entries
    come from REQ-025's "separate effective classification-policy and consent
    acts", RFC5-16 and RFC4-7. Repair: "RFC5-12 fixes one record per …"; cite
    the policy and registry sources beside REQ-025.
