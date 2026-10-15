# R-IMPL-P97-BLOCK-PROVENANCE-1 — implementation review of syzygy-u05.19
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: ffb3fc5936ff9a5d516ace175f9c8ee2e075d349
Subject: /home/tze/.cache/syzygy-impl-lane/p97-diff.patch

Reviewer: fresh-context CC-REV-1 code review, 2026-10-15.
Subject file sha256 (scripted): `64809f3de198c4b4cbfb58580bbb51689c183ba8ff486abe5a5669131b809c3a`.
Governing references: POC spec.md lines 18-58, 60-126 (POC-REQ-001), 249-316
(POC-REQ-010) at the reviewed commit; OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md
§Bounds; the bead's four acceptance criteria as given in the brief.

## What was checked, and how

- [Observed] Diffed `72a16236..ffb3fc59` in the worktree (19 files, 655+/43-)
  and read every hunk; read `block-provenance-sweep.test.ts` in full at HEAD.
- [Observed] Ran `npx vitest run` (TMPDIR=/home/tze/.cache/syzygy-impl-lane/tmp)
  over the three named test files: 3 files, 30 tests, 30 passed.
- [Observed] Ran `npx vitest run packages/three-surface-poc-core apps/three-surface-poc`:
  120 files (116 passed, 3 skipped, 1 failed), 1947 tests (1943 passed,
  3 skipped, 1 failed). The one failure is environmental (finding 6).
- [Observed] `npx tsc --noEmit -p packages/three-surface-poc-core`: exit 0, no output.
- [Observed] Swept readers of the removed fields: `doltRevision` over
  `apps/`+`packages/` `.ts/.js/.html/.json` (21 files; every non-test hit
  reads a projection's or clocks' own `doltRevision`, the local variable in
  `work-items.ts`, or `materialization.ts`'s unrelated `doltRevisionAtCreation`),
  and `git grep` for `codeStructure…revision` / `workItems…doltRevision` over
  the whole tree outside `docs`, `.syzygy`, `openspec` (one hit: finding 3).
  No `.js`/`.html` client asset under the app or core reads `.revision` or
  `doltRevision` (git grep returned nothing).
- [Observed] sha256 of `code-structure.ts`, `work-items.ts` and
  `block-provenance-sweep.test.ts` at HEAD equal the three digests in the
  evidence record's `subject.files`; commit `ffb3fc59` changes only the
  evidence JSON, so the mutant run at `8c804dc1` ran over the reviewed source
  bytes. I did not re-run the 15 mutants (no repository edits); their
  outcomes are taken from the record and checked for plausibility against
  the tests.

## Correctness against the signed text

- [Observed] Code-structure observation now serialises as
  `{kind, provenance, capturedAt, files}`; entries are
  `{path, sizeBytes, digest, language}` with the per-entry `revision` gone.
  `provenance` is `{kind:'git-revision', source: gitProvenance.source, revision}`
  (model.ts passes the same `source` the project entity's git-revision
  provenance carries), so the block record is byte-identical in shape to the
  project entity's element.
- [Observed] Work-item observation now serialises as
  `{kind, beadPrefix, provenance, capturedAt, items}`; items lose `doltRevision`;
  `provenance` is `{kind:'dolt-revision', source:'Beads Dolt database (<prefix>)', revision}`,
  both in the empty and non-empty paths.
- [Observed] `capturedAt` stays on each observation beside the record, as signed.
- [Observed] Every non-test reader of the removed fields in
  `packages/three-surface-poc-core` and `apps/three-surface-poc` was moved to
  `.provenance.revision` (`model.ts` materialization provenance,
  `orrery-projection.ts`, `trajectory-projection.ts`, `reevaluation.ts`,
  `polaris.ts` two sections); the core typechecks and the full app+core
  suites pass apart from finding 6.
- [Observed] Scope: no new read, query, process spawn or egress; the only
  non-observation change is one `PROVENANCE_CLASS` row needed for the
  widened kind union (finding 2). Rendered Polaris text and anchors are
  value-identical (same revision string, now read via `provenance.revision`).

## Findings

1. **note** — the stored subject patch is not the change under review.
   `/home/tze/.cache/syzygy-impl-lane/p97-diff.patch` hashes to
   `64809f3d…` — scripted, equal to `git diff eda0e345 ffb3fc59 | sha256sum`,
   not `git diff 72a16236 ffb3fc59` (`91c666d8…`). origin/main moved to
   `eda0e345` ("regenerate P-98 over the P-99 sign-off; brief round 5")
   after the branch was cut, so the patch carries reverse hunks of five
   governance files the branch never touched, e.g. patch line 1:
   "diff --git a/.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt"
   and patch line 188 "diff --git a/.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md".
   This review covers the 19 files of `72a16236..ffb3fc59`; the five
   governance hunks are outside it and must not be read as reverted by
   this change. Rebase onto current main before merge (the file sets are
   disjoint) and regenerate the patch three-dot if it is retained as the
   review subject.

2. **note** — the record's `kind` is a new value no entity element carries,
   and the shape oracle compares keys only.
   `packages/three-surface-poc-core/src/model.ts:83` adds
   "| 'dolt-revision'" to `PocProvenance['kind']`, and
   `apps/three-surface-poc/src/polaris-narrative.ts:88` adds
   "'dolt-revision': 'work',". The work-item record is therefore in the
   entities' `PocProvenance` type and key set, but its `kind` value occurs in
   no entity or relationship provenance element of any served answer. The
   sweep's shape predicate is key-set only:
   `apps/three-surface-poc/src/block-provenance-sweep.test.ts:60`
   "const allowed = new Set(elements.flatMap((element) => Object.keys(element)));"
   and line 86 "for (const key of keys) if (!shape.allowed.has(key)) …".
   I read "the shape each element … takes" (spec.md:71-72, 259-260) as the
   element's field structure, which this satisfies, and none of the existing
   kinds (`git-revision`, `materialization-record`, …) would honestly name
   a Dolt head; so this is not a defect. It is an interpretation the
   evidence record should state in words, since a stricter reader could say
   a kind value outside the entities' observed domain is "another shape".
   The widened union is type-only for Polaris (no entity is ever built with
   that kind, so no anchor changes class).

3. **note** — one reader of the removed fields is left broken:
   `scripts/measure_machine_channel_provenance.py:118-119`
   "work = row_repeats(poc[\"workItems\"][\"items\"], \"doltRevision\", poc[\"workItems\"][\"doltRevision\"])"
   / "code = row_repeats(poc[\"codeStructure\"][\"files\"], \"revision\", poc[\"codeStructure\"][\"revision\"])".
   On any post-P97 capture this raises `KeyError`. It is a read-only N9
   measurement tool over retained captures, cited only by candidate packages
   and `docs/evidence/n9-machine-channel-provenance-measurement-2026-10-03.json`,
   and not in the battery (git grep: 7 citing files, none a workflow or
   PROJECT-STATUS), so it does not block merge; either make it read
   `provenance.revision` when present (and report 0 row repeats) or record
   in the bead that it measures pre-P97 captures only.

4. **note** — the falsifier set covers every signed limb, with one limb
   folded into another. Mapping the evidence record's 15 mutants against
   spec.md:100-105 and 291-296: REQ-001 revision differs (M01), size (M02),
   digest (M03), no record (M04), another shape (M05), another field holding
   the revision (M06), entry carrying the revision (M07), entry carrying the
   capture instant (M08); REQ-010 revision differs (M09), no record (M10),
   another shape (M11), another field (M12), fact carrying the revision (M13),
   fact carrying the instant outside a database time (M14), sampled field
   differs (M15). The REQ-010 limb "a served work-item observation with no
   Dolt revision" (spec.md:291) has no mutant of its own; M10 (record absent)
   implies it, but a record present with `revision: ''` or the key dropped
   is a distinct implementation mutant. The predicate catches it (line 86-88:
   `lacks shared-shape field revision` / `provenance revision … differs`),
   so adding one mutant would close the mapping exactly. The predicate-level
   falsifier cases in the test file are a genuine second layer (each limb's
   counterexample injected into a copy of a passing answer).

5. **note** — oracle independence and exhaustiveness are sound, with two
   bounded caveats. Expected values: HEAD from `git rev-parse HEAD`, size from
   `statSync`/`readFileSync`, digest from `git hash-object` cross-checked
   against `git rev-parse HEAD:<path>` (lines 147-150), Dolt revision and
   capture instant as hand-typed literals matching the fixture's injected
   inputs (`test-model-fixture.ts:105` "const FIXTURE_DOLT_REVISION = 'dolt-fixture-revision';").
   Denominators: inventory length against `git ls-tree -r --name-only`, item
   ids enumerated, and the observation's own key set pinned exactly. The
   sweep walks every JSON leaf of both observations, which is every
   whole-value field. Caveats: (a) the sweep reads `JSON.stringify(model)`
   (line 116 "const answer = JSON.parse(JSON.stringify(model)) as Obj;")
   rather than the `GET /api/poc` route; `routes.ts:233` serves exactly
   `JSON.stringify(model)` under the ceiling, so this is equivalent today.
   (b) POC-REQ-010's oracle names "the database's own head revision queried
   directly"; the sweep's Dolt is an injected fixture, and only the gated
   `work-items.live.test.ts` queries Dolt directly (revision only, no sweep).
   Acceptable under the Bounds' synthetic-fixture rule; worth one sentence
   in the evidence record.

6. **note** — one full-suite failure, environmental, unrelated to the diff.
   `packages/three-surface-poc-core/src/model.test.ts:199`
   "expect(JSON.stringify(spawned)).toContain('the Beads Dolt database was unreachable or unreadable during work-item observation');"
   failed in my run because TMPDIR sits under `/home/tze`, and `bd`
   discovered `/home/tze/.beads` (present) plus
   `BEADS_DOLT_SERVER_HOST=dolt.parrot-hen.ts.net` in the environment, so the
   "no Beads project" directory observed a real database
   (`workItems.kind: 'observed'`). The diff does not touch the unreachable
   path. [Inferred] It would fail identically at `72a16236` under the same
   TMPDIR; I did not run the base. The lane's rule-7 battery run should name
   its TMPDIR, or the test should isolate `bd` from parent `.beads`.
   Incidentally, that failing body shows the post-P97 shape served end to end:
   "\"workItems\":{\"kind\":\"observed\",\"beadPrefix\":\"bu\",\"provenance\":{\"kind\":\"dolt-revision\",…},\"capturedAt\":…,\"items\":[]}".

7. **note** — the size evidence is fixture-only and its digests are not
   re-derivable. `docs/evidence/p97-block-provenance-implementation-2026-10-15.json:20`
   "The body names its temporary fixture repository path, so its sha256 differs per run";
   line 22 records the before commit abbreviated ("commit": "72a16236") while
   the after commit is full. The acceptance criterion's literal terms (size
   before and after, subject commit, sha256) are met, but rule 11's purpose —
   re-checking the record against the bytes — is not: a reader cannot
   reproduce either sha256. Record the full before commit and either the
   TMPDIR path (so the body is reproducible) or a path-normalised digest.
   A live Butlers machine-body figure (the 2026-09-22 pursuit measured
   ~740 KB of row repeats) would be the meaningful size delta but is not
   required by the brief's criteria.

8. **note** — the machine answer still holds the revisions whole outside the
   two observations, which the signed text permits. `orrery-projection.ts:116`
   "revision: structure.provenance.revision," and
   `trajectory-projection.ts:108` "doltRevision: workItems.provenance.revision,"
   keep projection-level copies, alongside `project.revision` and entity
   provenance. POC-REQ-001/010 bound "the observation, its own or an entry's"
   fields only (spec.md:73-74, 261-262), so these are in scope neither for
   the requirement nor for this change; listed so a later reader does not
   take them for a missed site.

9. **note** — rule 7 is claimed by the criteria but not evidenced in the
   record. The evidence JSON carries mutant outcomes and size figures but no
   battery transcript or commit-bound result for the PROJECT-STATUS
   battery. My own run (above) is at the reviewed commit in this worktree,
   not a clean clone. Attach the battery result at the merge-candidate
   commit before closing the bead.

## Acceptance criteria

1. Oracle as tests — met ([Observed] 30/30 pass; revision vs `git rev-parse
   HEAD`, sampled size and digest, exhaustive leaf sweep with exactly one
   holder each).
2. Rule-6 mutant per limb — met, with finding 4's folded limb.
   Database-recorded times are exempted only under `items[n].createdAt|updatedAt|closedAt`
   and only for `workItems` (`databaseTimes: []` for code structure), as signed.
3. Exactly the signed text — met ([Observed] no new read, egress, or
   execution; finding 2's union widening is type-only).
4. WIP one / review / rule 7 / size — review is this record; size recorded
   (finding 7); rule-7 battery not yet evidenced (finding 9).
