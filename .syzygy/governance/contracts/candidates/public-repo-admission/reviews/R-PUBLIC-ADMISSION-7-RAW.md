# R-PUBLIC-ADMISSION-7 — public-repository admission package
Reviewed commit: 7704b4a575acf29de93e3872ff549a856e6395ec
Manifest SHA-256: 51f70c07ed1bb5ea081c08fc2c06dd61b865f0c6888ae3f0faf17e8bf50bc649
Verdict: CONFIRM WITH EXCEPTIONS
Reviewer: fresh-context subagent, 2026-10-03. Read-only, in a detached
scratch worktree at the reviewed commit. `npm ci` was run there. No tracked
file was modified, and no repository body of any target was read. No model
was called. Mutants were run in a separate copy of that worktree with no git
link, and a rebuild confirmed it restored.

## What I ran

- `python3 scripts/build_public_repo_admission.py --check` printed
  `public-repo admission instances: current` and exited 0. It rebuilt
  `packages/polaris-generation-core` itself. Before that build, `node
  scripts/derive_generator_sent_text.mjs --table` failed with
  `ERR_MODULE_NOT_FOUND` on `dist/index.js` in a fresh checkout. The
  script's header says "Build first".
- `node scripts/derive_generator_sent_text.mjs --table` exited 0. Its
  output equals the table embedded at
  `instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`:72–92, all 19
  rows: 4 envelope, 9 `inputs`, 6 port. `--check` compares the two
  byte-for-byte, and I compared the rows by eye.
- `--selftest` exited 0 and printed "selftest: 13 of 13 checks held: one
  positive render check (banner replaced) and twelve mutants …". The
  `unknown mode --bogus` line on stderr comes from its own unknown-mode
  mutant.
- `--digests` exited 0 and printed three rows. `--manifest-digest` printed
  the manifest file's digest. `sha256sum` of each record and of the
  manifest file equals the builder's figures and the manifest rows. The row
  population is three rows over the three `instances/*/*.md` records.
- Every Markdown file of the package outside `reviews/` (8 files), plus the
  answers direction: zero 64-hex tokens, by Python `re` with hex
  look-arounds and again by `grep -cE '[0-9a-fA-F]{64}'`.
- Derivation mutants, run on a copy, each rebuilt with `tsc -b`, results
  below (Finding 1 and Finding 2).

## Acceptance criteria

**1. R4 findings repaired; no R1–R3 regression from the move: yes.**

- R4 F1. Egress :31 now reads "are written only inside a run directory
  … from the start of the run. A run whose runtime cannot be configured to
  keep its state and transcript inside that directory does not start."
  Repaired.
- R4 F2. Packet :127–128: "provider requests, provider replies and run
  records are retained in a run directory". Repaired.
- R4 F3. The class is now given by outline item 5's generator-authored
  request-text rule (`templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md`:66–80):
  "→ `code-content` of `project:syzygy`". Repaired, with the caveat in
  Finding 3.
- R4 F4. Egress :117–127 requires the following: no tools, no instruction
  or memory files, settings, MCP, hooks or environment summary, an empty
  working directory, and an adapter accepted only on a captured request.
  Repaired.
- R4 F5. Egress :31: "the owner discloses the terms document and the
  training-use setting at the offering, and this record promises neither."
  Repaired.
- The move to `instances/egress-anthropic/` regressed nothing. The
  `../../templates/` header path resolves. The observation records keep
  the R1 F1 snapshot-only grant (:37–41) and the R1 F14 Unknown-on-revocation
  (:67–69).

**2. Owner answers: yes.**

- Q1: the provider is "Anthropic, through the Claude Agent SDK (Claude Code
  runtime)" (:19).
- Q2: five classes, `work-history` absent (:25–29).
- Q3: run-directory retention (:31).
- Q4: the subject is `project:syzygy` in all three records.
- Q6: local draft view or run-directory file only, never published
  (:128–132).
- Q7: `project-documentation` is absent.

**3. Scope equals the admitted observations: yes.** Egress :47–48 lists
exactly `(project:syzygy, repository:psf-requests)` and `(project:syzygy,
repository:redis-redis)`. These are the two observation subjects at :17.
Under REQ-polaris-generation-025, "These permissions SHALL remain separately
revocable/renderable and SHALL NOT imply one another". The egress record
conditions egress on an in-force observation consent but grants no read. The
observation records exclude "network egress, which only the separate egress
consent can permit" (:61). So neither consent implies the other.

**4. Redis revisions: yes.** I compared the text of all five commit ids. Each
appears in `docs/polaris-generation/TARGETS.md`: the requests id at :37, and
the Redis ids at :38 and :62–64, with the `ls-remote` lines at :115–118. A
per-commit `git fetch --depth=1 <upstream> <commit>` still holds for four
revisions. The grant (:37–41) covers objects reachable from each admitted
root tree, and objects shared between snapshots are explicitly allowed.

**5. Q7 coherent: yes.** No sentence in any record or the packet promises
README or LICENSE egress. Outline item 5 (:64–65) refuses "all other prose
(README, guides, tutorials, LICENSE files)" until Q7 is resolved. Packet
:94–96 and :197–201 state the cost: T2's licence-history proof cannot run
until (a) is in force.

**6. Manifest: yes, with one uncovered builder claim.** Rows equal
`sha256sum` of each record. The population equals the instance records.
Findings 1 and 2 name the claims that no selftest mutant covers.

**7. Signing path: yes.** Packet :170–173 says the Scope A direction does not
cover these consents, and labels that [Inferred]. The direction's own scope
(:30) names "implementation-phase governed artifacts, namely the PWB …". It
does not mention consents. The precedent's form, an option at manifest rows,
is described from the re-pin act's Ceremony section, as R3 F4 required.

**8. Authority claims: none.**

- No file labels anything accepted, adopted, approved or signed off. The
  hits are "the adopted generator specification" (which is adopted), the
  proposed state string `owner-adopted (bootstrap, uncorrelated)`, the
  packet's question text, and the brief's criterion text.
- Every banner says it binds nothing.
- No file says a body was read.
- No 64-hex token appears in any Markdown file.

**9. Packet accurate about itself: yes, except Finding 1's echo in the R6
row.** I checked the following:

- the file locations (:87–93);
- the round history, with its dated supersession marks;
- that the recorder is drafted and not bound (:176–179). The script exists
  at the reviewed commit with `FROZEN_SUBJECT: str | None = None`;
- that round 7 is pending (:346–350).

Two version strings differ: requests is `0.1.0-candidate.6` and the other
two are `.7`. This is harmless, because each record is versioned on its own.

**10. Every carried field classed once and covered by Scope: yes for the
current code, not structurally.**

[Observed] The real pipeline's first `generate` call carries these fields:

- envelope keys `promptVersion`, `system`, `responseSchemaVersion`,
  `responseSchema` and `inputs`;
- `generate` port keys `input`, `permit`, `responseSchema`, `signal`,
  `stage` and `system`.

The six `await stage(…)` call sites at `pipeline.ts`:393–402 pass the
`inputs` keys `sources`, `sourcePopulation`, `readerQuestions`,
`requestedAssets`, `inventory`, `plan`, `draft` and `findings`. Every one of
these fields has a row, and every `inputs` or envelope row has one of the six
labels. The Scope (:40–57) names all six populations.

These are the rules the screening outline quotes for the Syzygy-authored
classes, at `PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md`:66–75:

- "the `instruction-text` class is the output of `promptForStage`
  (`packages/polaris-generation-core/src/prompts.ts`) and `stageSchema`
  (`packages/polaris-generation-core/src/provider-draft.ts`)"
- "the `envelope-control` class is the version and stage labels those two
  symbols produce"
- "the `run-profile` class is the run's reader questions and requested
  assets, read from the run profile file in the run directory and validated
  by the generator before use"

The egress record does not classify these classes itself. Egress :55–57
says "this consent does not classify it", which meets RFC5-15 part 2's
separate policy act. Target metadata goes to `code-structure` by outline
:81–83, and composites follow egress condition 2: "A composite's class is
computed from what it embeds".

The recurring item from R3 F5, R4 F3, R5 F1 and R6 F1 asked whether Scope
omits a population that requests carry. For the bytes under review, that
item is closed: I found no carried field outside the table or the Scope.

It is not closed structurally, in two respects:

- the table's completeness guarantee depends on how the call sites are
  written (Finding 1);
- the table's labels come from field names, not from content provenance
  (Finding 2). For run-profile, the provenance the outline relies on does
  not exist in the code (Finding 3).

Both fail closed or are deferred to the screening scope's own act, so
neither is blocking here. Both should be fixed when the screening scope is
filled, or the item will recur there.

**11. R6 dispositions hold: yes.**

- F1: Scope now enumerates each population (:40–57). Neither "only
  Syzygy-authored" sentence remains in any package file (Python sweep over
  13 files).
- F2: plan's `sources` row reads `target-metadata` (:82).
- F3: all six port fields are in the table, and :94–96 says which reach the
  wire.
- F4: :97–98: "the schema version is bound through that digest".
- F5: the sign-in clause is gone from :1 and :19, and sign-in is listed
  under "Open before an offering" (:329–333).
- F6: packet :176–179: "Both are drafted … and are not yet bound".
- F7: the stale-manifest mutant now flips the first hex digit of a digest
  row (builder :157–161), and both refusals assert
  `out.getvalue() == ""` (:213).

## Findings

**Finding 1 — "a field with no class makes the derivation fail" holds only for call sites written in one textual form; a stage called another way drops silently out of the table** (note)

Egress :68–70 and template :64–66 read: "a field with no class makes the
derivation fail. Each field has exactly one class." Packet :306 (R6 row 1)
says the derivation "fails (exit 2) on a field with no class". Outline :79–80
says: "A field with no class in the table is a build failure, not a
default."

[Observed] `derive_generator_sent_text.mjs` captures the runtime envelope
only for the first stage (inventory, :39 and :108). For every other stage it
reads `inputs` keys with the regex `` /await stage\('(\w+)', \{([^}]*)\}\)/g ``
over the source text (:53, :78). A stage that the regex does not match
contributes no rows and raises no failure: `inputKeys[stage] ?? []` (:97). I
ran two mutants on a copy, each rebuilt:

- M1: the plan call rewritten as `const planInputs = { …,
  operatorNote: frozen.requestId }; … stage('plan', planInputs)`. Exit 0.
  The plan stage disappears from every row, and `operatorNote` appears in no
  row.
- M7: the author call rewritten with a double-quoted stage name and a new
  key `projectId: frozen.projectId`. Exit 0. Author drops out of the stage
  lists, and `projectId` is in no row.

`--check` reports both as stale, because the table changed. `--write` would
regenerate a table that omits a field the request carries, and the record
would still say every field has a class. The selftest's "field with no class"
mutant only deletes one entry from `INPUT_CLASS`. It does not exercise a
call-site form the regex misses. This answers the brief's criterion 6 ("Name
any builder or manifest claim that no selftest mutant covers").

The outcome fails closed, which is why this is a note: egress :101–103 and
condition 1 refuse "a field outside the table" at the egress check, so the
omission would be refused and would not leak. The signed sentence is still
broader than the mechanism.

Clauses: AGENTS.md verification rule 6, and brief criteria 6 and 10 ("Name
any … sentence not covered").

Suggested disposition: before a later version, fail the derivation when the
number of `stage(` call sites differs from the number matched, or capture
every stage's envelope at run time instead of parsing text. Add a mutant for
that. Narrow the sentence to what is checked.

Also: three port rows (`input`, `permit`, `signal`) carry "the envelope",
"dispatch permit" and "abort signal", none of which is one of the six
classes. So "Each field has exactly one class" (:70) is literally false for
them. Two are never sent, and `input` is the container of classed fields.
This is harmless in effect, but the sentence should say "each sent field".

**Finding 2 — table classes are field-name labels, not provenance; content under a classed name keeps its label** (note)

[Observed] The script classes by field name (`ENVELOPE_CLASS`, `INPUT_CLASS`,
:64–66) and by the call-site expression for `sources` (:77–88). It never
looks at what a field holds.

- M8b mutant: `sourcePopulation` gains `path`, `evaluationId` and every
  admitted source's `spans` (body text). Exit 0, and the table is
  byte-identical, so `inputs.sourcePopulation` is still labelled
  `target-metadata`, "with no body".
- M9 mutant: `context.sources` becomes `frozen.sources`, the full source
  records. Exit 0, and the table is unchanged.

RFC5-14 says: "Content class is a **property of what enters the choke point,
tracked from where the content originated**, never an attribute the
composing step asserts about its own output". REQ-polaris-generation-025
says: "composition SHALL preserve embedded classifications and origins
rather than trust its own output label."

The record's conditions still require classification under the screening
policy at the egress check (condition 1, :107–112; condition 2, :113–114).
So the table describes and gates by field name, and does not replace
provenance-based classification. That is why this is a note.

Scope :40–41, however, reads "Exactly the populations in the generated table
below, in the classes the table gives". A reader could take this to mean the
table's label settles the class. That would be the composing step asserting
the class.

Suggested disposition: say in the disposition record that the table is a
field-level gate, and that classes are decided at the egress check from
origin under the screening scope. When the screening scope is filled, its
rule should classify by origin, not by field name.

**Finding 3 — the run-profile rule names a file and a validation that the generator does not have; `readerQuestions` is typed `unknown`** (note — an open owner ruling; no signed bytes assume its answer)

Outline :73–75 reads: "the run's reader questions and requested assets, read
from the run profile file in the run directory and validated by the
generator before use".

[Observed] In `packages/polaris-generation-core/src/pipeline.ts`:

- :27 declares `readonly readerQuestions: unknown;`;
- :191 validates only `requestedAssets`;
- :239 forwards `frozen.readerQuestions` unchanged into every stage.

No code under `packages/`, `apps/` or `scripts/` reads a run-profile file.
The only producers are literals in `self-corpus.ts`:130 and
`pipeline-demo.ts`. As coded, `readerQuestions` can hold any JSON value,
including text of non-admitted origin (for example Butlers or other Syzygy
content). Under the run-profile label it would then be called `code-content`
of `project:syzygy`. That is a class taken from the field's name, not its
origin (RFC5-14, quoted in Finding 2).

The egress record calls run-profile "text authored by Syzygy" (:54–55). The
packet calls it "operator-authored question text" (:334). R6 Finding 1's
repair item 2 asked the drafter to "Name their origin, for example a
run-profile file at a path". The outline names a file but no path, and the
code has neither the file nor the validation.

Why this is not blocking:

- The packet presents the run-profile class as an open owner ruling under
  "Open before an offering" (:334–337).
- The egress record does not assume an answer. It defers to the screening
  scope's rule ("this consent does not classify it", :57).
- The outline is a template with its own later act and review.

What needs to happen: before the screening scope is filled, give the run
profile a path, validate `readerQuestions` in the generator (a closed shape
of short strings, run through the secret detectors), and say in the packet
that the generator does not validate it today. "Text authored by Syzygy"
should read "authored by Syzygy's operator".

**Finding 4 — the excluded-sources sentence names paths that the code does not send and calls reasons "closed" that the code does not close; the signed record already carries the recommended answer** (note — an open owner ruling, disclosed as encoded in the record)

Egress :52–53 reads: "Excluded sources' metadata may leave: it names no
content, and a repository's paths are tree metadata (`code-structure`) of a
public target." Packet :338–339 reads: "The record lets ids, closed reasons
and paths of excluded sources leave."

[Observed] `sourcePopulation` (`pipeline.ts`:237–238) carries `sourceId`,
`classificationBasis`, `excluded` and `reason` only. It carries no path.
Excluded sources have no spans (`generation-source.ts`, `unquotable-source`
guard), so no `anchorId` carries their path either. `exclusion.reason` is
typed `string`, and validation requires only that it is non-empty, so
"closed" is a property the screening scope must impose: the code does not
enforce it. REQ-polaris-generation-025: "Exclusion provenance SHALL contain
only permitted digest/location/policy/redaction metadata, never excluded
bytes."

On the ruling: here the signed bytes do encode the recommended answer
("accept"). The packet says so plainly ("The record lets …"), so performing
the act over this record is itself the owner's ruling. That is why I treat it
as a disclosed ruling and not as a hidden assumption.

The packet omits what the alternative costs. Sending admitted sources'
metadata only needs a change to `pipeline.ts`:237, because the pipeline
sends the whole population today, plus a regenerated record. The packet
states that cost for Route B but not here.

Suggested disposition:

- In the disposition record, state that paths of excluded sources are not
  sent today.
- In the screening scope, state that `reason` must come from a closed list.
- In the packet's open item, state that the alternative needs a code change
  and a regeneration.

**Finding 5 — the admitted-pairs list renders as peers of the population bullets** (note)

Egress :43–48 and template :39–44: the bullet "**target-content** and
**composite**: … for one of these `(project:syzygy, repository)` pairs, …:"
is followed by a blank line and two unindented `-` items. GFM renders those
as items of the same list, at the same level as the population bullets. The
intended reading still recovers from "of the same pairs' sources" (:51), so
this is cosmetic. It sits in signed bytes, so an indent at the next version
would make the scope list unambiguous.

## Summary

All five findings are notes. Findings 3 and 4 are open owner rulings that the
packet already presents. Finding 3's answer is not assumed by any signed
bytes. Finding 4's answer is encoded in the record, and the packet says so,
so the act over the record is the ruling.

Criteria 1–9 and 11 hold. Criterion 10 holds for the current code: every
field a request carries has a row with one population label, and Scope names
each population.

The recurring carried-content blocker is closed as to population coverage at
this commit. It is not structurally closed:

- coverage depends on the call-site text form (Finding 1);
- labels follow field names, not origin (Finding 2);
- the run-profile origin the outline relies on does not exist (Finding 3).

These must be settled in the screening scope's own draft and review. If they
are not, the item will return there.
