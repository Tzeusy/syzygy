# R-PUBLIC-ADMISSION-6 — public-repository admission package
Reviewed commit: 108295996c0139bf2786f8be1208ed5b97148d67
Manifest SHA-256: 9e06e8dd54536f7fa32b866a2cb08e65d2cbe0926e0541baa1263c3c3961053e
Verdict: REVISE

Reviewer: fresh-context subagent, 2026-10-03. I read the package from a
detached worktree at the reviewed commit, read-only, and removed the worktree
afterwards. `git status --short` was empty after every command, so the
selftests wrote nothing into the tree.

Scope read: every file under
`.syzygy/governance/contracts/candidates/public-repo-admission/` except
`reviews/`:
- the packet, the brief and the manifest;
- the three templates;
- `instances/requests/`, `instances/redis/` and `instances/egress-anthropic/`,
  each with its `params.json` and one record.

Also read: `scripts/build_public_repo_admission.py` and
`.syzygy/governance/decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`.
I read the R4 and R5 raws for their findings only.

Governing references read:
- RFC5-14 and RFC5-15 at `rfcs/RFC-0005/consent-egress-secrets.md`:134 and
  :182. `DIRECTIVE-REGISTER.md` rows 336–340 locate them.
- REQ-polaris-generation-025 (`spec.md`:1400).
- The Scope A direction.
- The re-pin act's "at the manifest rows" ceremony.
- `docs/polaris-generation/TARGETS.md`.

To test criterion 10 I also read the code that the egress record and the
derivation script name:
- `packages/polaris-generation-core/src/pipeline.ts`;
- `generation-source.ts`;
- `scripts/derive_generator_sent_text.mjs`;
- the `readerQuestions` call sites in
  `apps/three-surface-poc/src/polaris-generation/`.

I contacted no hosting service and read no target repository body.

## Verified [Observed]

- **Builder modes.**
  - `python3 scripts/build_public_repo_admission.py --check` printed
    "public-repo admission instances: current", rc 0.
  - `--selftest` printed "selftest: 11 of 11 checks held: one positive render
    check (banner replaced) and ten mutants: …", rc 0.
  - `--digests` printed three rows, rc 0.
  - `--manifest-digest` printed
    `9e06e8dd54536f7fa32b866a2cb08e65d2cbe0926e0541baa1263c3c3961053e`, rc 0.
    This equals `sha256sum PUBLIC-REPO-ADMISSION-MANIFEST.txt`.
  - `--bogus` printed "unknown mode --bogus", rc 2.
- **Manifest rows.** Each of the three rows equals `sha256sum` of its record
  and the `--digests` line for that record:
  - egress `373a6ad9…`;
  - redis `a733220d…`;
  - requests `d154165c…`.

  `find instances -type f` returns 6 files: 3 `params.json` and 3 `.md`
  records. The `.md` paths are exactly the three manifest paths. The header
  "3 records" is right.
- **64-hex sweep.** Python `(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])`
  over 14 files: the 12 package files outside `reviews/`, the direction and
  the builder. It found 3 tokens, all in the manifest `.txt`, and 0 in every
  Markdown file.
- **Authority sweep.** I swept the same 14 files for "accepted", "adopted",
  "approved", "signed off", "sign-off" and "was read". Every hit is one of:
  - the state-(1) label `owner-adopted (bootstrap, uncorrelated)`;
  - a reference to another artifact ("adopted generator specification",
    "accepted-contract amendment");
  - the brief's own criterion;
  - "adapter is accepted only when …";
  - a negation.

  Every Markdown banner says the file binds nothing. Packet line 8 says no
  target body was read.
- **Pins.** I compared the text of the pins in the records with
  `TARGETS.md`:
  - `TARGETS.md`:37 `6e83187b8feb273ed4c6cdab5efd8d54901dfab3` equals
    requests.
  - `TARGETS.md`:38 `498ecd0d…` equals redis `8.10.2`.
  - `TARGETS.md`:62–64 `d2c8a4b9…`, `c9d29f6a…` and `e91a340e…` equal redis
    `7.2.4`, `7.4.0` and `8.0.0`.

  All five 40-hex strings match character for character, and again in the
  `ls-remote` block at `TARGETS.md`:115–118.
- **Derivation script.** `npm ci`, then `npx tsc -b
  packages/polaris-generation-core` (rc 0), then `node
  scripts/derive_generator_sent_text.mjs` (rc 0). It printed:
  - `envelopeKeys`: `inputs`, `promptVersion`, `responseSchema`,
    `responseSchemaVersion`, `system`.
  - `inputKeys` per stage, which matches the record's per-stage list exactly,
    with "edit — those plus `draft`" and "repair — those plus `findings`"
    expanded.
  - `authoredBySource` `{prompts.ts: promptForStage, provider-draft.ts:
    stageSchema}`.
  - `generateInputFields`: `input`, `permit`, `responseSchema`, `signal`,
    `stage`, `system`.

## Criterion results

1. **R4 repairs.**
   - F1 is repaired. Egress :31 says the runtime state and transcript "are
     written only inside a run directory … from the start of the run. A run
     whose runtime cannot be configured to keep its state and transcript
     inside that directory does not start."
   - F2 is repaired (packet :127–131).
   - F3: R5 superseded it; see criterion 11.
   - F4 is repaired (egress :101–111).
   - F5 is repaired as a disclosure deferred to the offering (:31; packet
     :307–311).

   I checked the R1–R3 blocking findings (R1 F1–4, R2 F1–2, R3 F1) against the
   current bytes. None regressed, except that the R3 F5 line of repair has
   moved; see Finding 1.
2. **Owner answers.**
   - Q1: title and :19.
   - Q2: five classes, no `work-history`.
   - Q3: :31.
   - Q4: subjects.
   - Q5: state (1) on all three records.
   - Q6: egress :112–116 and outline item 4.
   - Q7: class absent.

   All seven are followed. See Finding 5 on Q1's sign-in wording.
3. **Scope equals the admitted observations.** Yes: exactly the two pairs.
   It is consistent with REQ-025: the egress record requires an in-force
   observation consent but grants no read, and each observation record
   excludes network egress (redis :61).
4. **Redis revisions and the fetch.** The pins are right by text.
   `TARGETS.md`:104–118 records the metadata-only `git ls-remote … refs/tags/<tag>
   refs/tags/<tag>^{}` result: no peeled line, so lightweight tags. This is
   labelled [Inferred], which is right. "Fetch each admitted commit alone"
   still holds for four revisions, because each `--depth=1` fetch transfers
   one commit.
5. **Q7.** Coherent.
   - No record or packet sentence promises README or LICENSE egress.
   - Outline item 5 sends them to "indeterminate, refused egress".
   - Packet :193–199 states the cost (T2's licence proof blocked).
6. **Manifest.** Rows and population are verified above. Finding 7 names the
   residual coverage gaps.
7. **Signing path.** Sound.
   - The Scope A direction names "the PWB specification deltas, the observer
     registry entry and the contract successors queued behind them", and
     names no consents.
   - The packet labels its conclusion [Inferred] (:170–173).
   - Its account of the re-pin act's "at the manifest rows" form matches
     that act.
8. **Authority claims.** None found (sweep above).
9. **Packet self-accuracy.** One inaccuracy; see Finding 6.
10. **Sent-content model.**
    - The envelope fields, the per-stage `inputs` fields and the two symbols
      equal the script's output.
    - The instruction-text class is set by a policy rule (outline item 5),
      not by the consent. That satisfies RFC5-15 part 2 and RFC5-14's "never
      an attribute the composing step asserts about its own output".
    - The model is not closed. Every request carries bytes that fall in none
      of the four admitted categories, and the record's Scope admits neither
      them nor the instruction text. See Findings 1–3.
11. **R5 dispositions.**
    - F1 is not repaired; see Finding 1.
    - F2 holds: :31 "the owner discloses the terms document and the
      training-use setting at the offering"; packet R4 row 5 is corrected.
    - F3 holds: selftest output above; `stale()` :167–169 now unions every
      `instances/*/` directory.
    - F4 holds: `TARGETS.md`:104–118.
    - F5 holds: egress :112–116 "shown only on the local daemon's generated
      editorial draft view or as a static file in the run directory, and is
      never published"; outline :49–52.
    - F6 holds: packet :218–220 and :267–268 are dated at the sentence, and
      :91 reads "next candidate draft".

## Findings

**Finding 1 — the egress record's Scope admits only target spans and their composites, so it excludes the instruction text and the run-profile fields that every request carries** (blocking)

The Scope section of `instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`
(:40–50; template `EGRESS-CONSENT-TEMPLATE.md` has the same text) reads:

> "Only content read under an in-force observation consent for one of these
> `(project:syzygy, repository)` pairs: … carried in a request's `inputs` as
> source spans, or as validated stage artifacts computed from them
> (composites, RFC5-14). Every other source of `project:syzygy` content is
> outside this consent, including the Butlers repository, the rest of
> Syzygy's own repository and any work history, and stays unsent."

The round-5 repair deleted the clause "together with the generator's own
instruction text …" from Scope (`git diff a445e253 HEAD`). It moved the
instruction text into a new descriptive section ("What a request carries",
:52–88) and a condition (:92–96). The Scope, the grant itself, now reads
"Only content read under an in-force observation consent". The text of
`promptForStage` and `stageSchema` was not read under any observation consent.
It is part of "Syzygy's own repository", which Scope says "stays unsent". The
phrase "the rest of Syzygy's own repository" presupposes an admitted part that
Scope never names.

Scope also excludes several other `inputs` fields [Observed] that the record's
own carried list, and the script's output, put in every request:

- `readerQuestions` and `requestedAssets`, in every stage
  (`pipeline.ts`:393–402). Today they are operator-supplied literals in
  Syzygy's code, for example `pipeline-demo.ts`:81 `['Why does it exist?', …]`
  and `self-corpus.ts`:130. `TARGETS.md` calls the public-target ones "seven
  frozen questions" of the run profile. They are not target spans, not
  composites computed from target spans, not instruction-text symbols and not
  runtime-fixed bytes.
- `sourcePopulation`, in inventory, and plan's `sources`, which `pipeline.ts`:394
  sets to `sourcePopulation`, not to spans. This field carries every frozen
  source's id, `classificationBasis`, the `excluded` flag and the Syzygy-side
  exclusion `reason`. That includes ids and reasons of *excluded* sources
  (`pipeline.ts`:237–238). It is not a source span and not a validated stage
  artifact.

Two sentences in the package then state a falsehood about the code:
- Egress :77: "The first two bullets are the only Syzygy-authored content a
  request carries."
- Outline item 5 (`PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md`:71): "it is the only
  Syzygy-authored text a request carries".

The reader questions and requested-asset ids are Syzygy-authored as well. The
same rule's catch-all (:74–75, "anything else the rules do not determine →
indeterminate, refused egress visibly") therefore classifies them as
indeterminate.

Clauses violated:
- RFC5-12: the scope of an egress record must cover what is sent.
- RFC5-15 part 2: "the content's class is **determinable and within the
  consented set** under a classification policy carrying an effective owner
  act".
- RFC5-14: "A composite whose class **cannot be determined fails closed**".
- REQ-polaris-generation-025: "Indeterminate classification SHALL refuse
  egress visibly".
- Brief criterion 10: "Name any byte not covered".

Consequence: the same as R5 F1. An implementation that honours Scope and the
outline literally refuses every request. One that sends them sends content the
signed record says "stays unsent". This is the fourth round on this item (R3
F5, R4 F3, R5 F1).

Repair:
1. Make Scope enumerate every population the "What a request carries" section
   lists, by name: target spans and composites, the instruction-text symbols,
   the run-profile fields and the source-population metadata.
2. Give the run-profile fields and the source-population metadata a class
   rule in outline item 5. Name their origin, for example a run-profile file
   at a path, and say whether the ids and exclusion reasons of excluded
   sources may leave at all (RFC5-17's hash-not-body posture is the nearest
   precedent).
3. Correct the two "only Syzygy-authored" sentences.

**Finding 2 — the record's description of `inputs.sources` is wrong for the plan stage** (note)

Egress :72–73: "`sources` are admitted target spans; `sourcePopulation` lists
each source's id, classification basis and exclusion reason, without a body".
`pipeline.ts`:394 passes `sources: sourcePopulation` to the plan stage, so
plan's `sources` carries no spans. `sourcePopulation` also carries the
`excluded` boolean (:238), which the sentence omits. Script field names cannot
detect this, because the key name is the same; it shows only in the call
site.

Clause: brief criterion 10 ("Do the … per-stage `inputs` fields … equal the
script's output"). The field names equal the output; the stated contents do
not.

Repair: describe plan's `sources` as the source population.

**Finding 3 — the `generate` port-field sentence omits three of the six fields the script reports** (note)

Egress :57–59: "The `generate` port also receives a dispatch permit and an
abort signal; neither is part of the envelope and neither is sent." The
script's `generateInputFields` is `input, permit, responseSchema, signal,
stage, system`. `pipeline.ts`:330 passes `stage: name` and separate copies of
`system` and `responseSchema` beside the encoded `input`. The sentence does
not say whether `stage` (a Syzygy-authored stage name) is sent, or whether
`system` is sent once or twice. The closing sentence (:85–88, "any other byte
… is refused") fails closed on it, so this is a completeness note, not an
open channel.

Clause: brief criterion 10.

Repair: list all six port fields and say which reach the wire.

**Finding 4 — "Each audit record names the prompt and schema versions sent" is not what the pipeline records today** (note)

Egress :81–82. [Observed] `pipeline.ts`: the stage receipt pushes
`promptVersion` but no `responseSchemaVersion`. `AttemptInput` (:33–46) carries
an `inputDigest` but neither version. The schema version is recoverable only
through the envelope digest. The sentence reads as a statement of fact. The
record should either state it as a condition on the route, as other route
requirements are stated, or name the record (RFC5-25) that carries both.

Clause: brief criterion 10; AGENTS.md epistemic discipline (an unlabelled
claim about the code).

**Finding 5 — the provider field fixes a sign-in mode that the packet lists as [Unknown]** (note)

The egress title and :19 read "signed in with the owner's existing Claude
account". Packet :307–311 says "Whether the owner's personal runs may use a
subscription login is [Unknown] … an API key is supported", and the
retention line (:31) already allows "the account or key used for the run". The
packet says choosing Route B regenerates the record (:304–306). It does not
say that Route A with an API key would also make the signed provider field
false.

Clause: brief criteria 2 and 9; RFC5-14 (the record names the provider route
precisely).

Repair: either drop the sign-in clause from the provider field, or add to
"Open before an offering" that an API-key run regenerates the record.

**Finding 6 — the packet says the recorder and the check registration are prepared after the confirming review, but the reviewed commit already contains both** (note)

Packet :173–177: "Before the first offering: a recorder … and the act labels
and packet copies registered in `scripts/check_governance.py` …; both are
prepared after the confirming review, against the confirmed commit." The brief
(:97–98) says the same. Commit `9470b0fa` ("admission recorder and candidate
registration") is an ancestor of the reviewed commit. It adds
`scripts/record_public_repo_admission_acts.py` (588 lines, `FROZEN_SUBJECT`
None until confirmation, `CONFIRMATION_REVIEW_REL` hard-coded to this raw's
path) and 36 lines of `check_governance.py`. They are out of scope for this
review, and I did not review them. The packet's statement that they do not yet
exist is inaccurate about itself.

Clause: brief criterion 9.

Repair: say they are drafted, not yet bound, and get their own check.

**Finding 7 — residual builder claims without a mutant** (note)

`scripts/build_public_repo_admission.py`:
- The stale-manifest mutant (:130, `replace("1", "2", 1)`) still alters only
  the header count "1 records", never a digest row. Whole-file comparison
  catches both, so this is wording only. R5 F3(d) named it, and the
  disposition is silent on it.
- The comment at :135 says both refusals "exit 1 and print nothing". The
  selftest asserts the exit code only, and the refusal message goes to stderr.
  Nothing asserts that stdout is empty.

Clause: AGENTS.md verification rule 6; brief criterion 6.

## Summary

One blocking finding (1) and six notes. Finding 1 is in an act argument's
grant. The round-5 repair moved the instruction text out of Scope and into
description and condition, so the record's own Scope now excludes it. The
run-profile fields and the source-population metadata, which every request
carries, are covered by no category and are declared non-existent by two "only
Syzygy-authored" sentences.

These all check out:
- manifest, digests and row population;
- pins;
- scope population;
- owner answers;
- Q7;
- signing-path reasoning;
- authority and 64-hex sweeps;
- R5 F2–F6.
