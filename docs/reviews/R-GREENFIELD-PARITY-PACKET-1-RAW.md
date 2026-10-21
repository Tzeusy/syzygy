# Adversarial review: greenfield-parity owner packet, GP-Q0 to GP-Q8

**What was reviewed:** `/home/tze/GitHub/syzygy/.syzygy/local/questionnaires/2026-10-21-greenfield-parity.md` (586 lines; the path is gitignored, `.gitignore:11`).
**State reviewed:** main at `eba011dfbe254c09a88ccc374b3efe5ff5df1762`; the audit was taken at `dd520e8d`, 39 commits earlier.
**How:** read-only throughout. I made no edits, no bd or git writes and no network calls, and read no Butlers or other observed-repository body. Every count was done with `git ls-files`, `git grep -F` or Python, not ugrep character classes.

## Packet-level findings

These apply to every item.

1. **[Observed] The status-quo rule is applied inconsistently.** Line 11 says "the recommended status-quo arm of a governed change is not put to the owner".
   - GP-Q4 is dropped under that rule.
   - GP-Q8 recommends the status quo ("keep parked") and is still asked.
   - GP-Q3, once its analysis is corrected (below), also comes out at status quo.
   - The rule needs to be applied the same way everywhere, or replaced with "asked because X".
2. **[Observed] No item gives a default if unanswered.** The decision-autonomy escalation format requires one, and for a hard gate it must be the status quo. Each item should say "Default if unanswered: no change".
3. **[Observed] The packet does not meet the acceptance criteria of its own bead.** `syzygy-bpyt.1.1` asks for a packet under `decisions/`, a `PENDING-OWNER-DECISIONS.md` row and a retained `-RAW.md` review. A local ignored file does none of these. Either the bead is amended or the packet is filed before 1.1 closes.
4. **[Observed] Bead `syzygy-bpyt.1.2`'s rationale is contradicted by this packet.** It says: "Agent decides the low-risk ones: rejected; none of the nine is an implementation-plane choice". GP-Q4 is now decided by the agent, and GP-Q3 and GP-Q5 are largely agent-decidable (below). Beads 1.2 and 1.3 need updating to match.
5. **[Observed] Bead counts:**
   - 64 `syzygy-bpyt*` beads, all `open`; 54 non-epic, 8 owner-gated, so 46 are dispatchable, plus `syzygy-0kq`.
   - No bead is closed or in progress.
   - The only bpyt commit since `dd520e8d` is `977c42e1` (docs).
   - The withdrawal clause therefore exposes nothing yet. "50+" is wrong.
6. **[Observed] `.beads/issues.jsonl` is stale.** It holds no bpyt beads. I read bead state from `bd list --all --limit 0 --json` instead.

---

## GP-Q0: confirm the reading of the 2026-10-20 request

**Claims**

- **[Observed]** The direction file labels the reading [Inferred] (lines 27-28). The withdrawal quote at lines 78-80 is exact.
- **[Observed]** "Behavior-preserving" excludes "a refusal string or an exit code" (direction lines 38-41). Two non-gated beads break that definition:
  - `syzygy-bpyt.6.1` is a bug fix (`git ls-tree -z`), so it changes observed output.
  - `syzygy-bpyt.6.2` makes "one fail-closed non-human-principal rule", which changes refusal reasons.
  - So "behavior-preserving" either excludes some of the dispatchable set, or the packet needs a separate class for bug fixes and fail-closed tightening.
- **[Observed] Trust-boundary refactors sit in the non-gated set:**
  - `6.2` (owner-act field rules; labelled consent and defense-in-depth);
  - `7.4` (owner-act gates as check tables; labelled consent and security);
  - `8.4` (package-reader act parsers onto one forms table; labelled consent and security);
  - `6.5` (bounded blob reader per phase policy, which is the PWB body-read path);
  - `3.2` (one descriptor-driven act recorder);
  - `2.2` (frozen act ledger replacing battery re-verifiers).
  
  Under the reading they all proceed without owner sight. The packet never tells the owner that confirming A releases changes to the consent gate, the body-read gate and the governance verifier.
- **[Observed] The POC direction offers a second route that the packet leaves out.** `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` requires a POC bead to "alter the runnable demonstration **or falsify/repair a named product finding**". The packet's [Inferred] bullet quotes only the first half. If the audit's identified findings count as named product findings, many POC beads qualify without any exception. The real question is narrower: do greenfield-parity findings count as product findings?
- **[Observed] Option B mislabels M6 as "tooling, tests and CI".** M6 includes `syzygy-bpyt.9.4`, which splits the governed-plane file `PENDING-OWNER-DECISIONS.md`.
- **[Inferred] Authority leakage.** An [Inferred] reading lives in `.syzygy/governance/decisions/`, the home of owner authorizations, and bead cold-starts cite it as "the owner's direction". The text is honest (it is labelled), but the placement lets it be cited as authority before Q0 is answered.

**Missing options:**
- A2: confirm A, but trust-boundary beads (labelled consent or security, plus `2.2` and `3.2`) each go to the owner before dispatch.
- A3: confirm A, plus an explicit class for "bug fixes and fail-closed tightening, each with a disclosed refusal-string diff".

**Result**

- **Scope verdict: Revise.** This is a genuine gate. But it hides two sub-decisions: the POC "named finding" reading, and whether trust-boundary refactors proceed unseen. It also miscounts the dispatchable set.
- **Recommendation verdict: Revise.** A is reasonable for pure refactors. As written it releases consent and body-read refactors without owner sight, and admits bug fixes that its own definition excludes. Recommend A plus A2, with a bug-fix class.
- **Material corrections:**
  - "50+" becomes "46 non-gated plus `syzygy-0kq`; all open; none merged".
  - Quote both halves of the POC direction's rule.
  - Fix option B: M6 includes governed `9.4`.
  - List the trust-boundary beads (`2.2`, `3.2`, `6.2`, `6.5`, `7.4`, `8.4`) the answer releases.
  - Reconcile `6.1` and `6.2` with the "refusal string" exclusion.
  - Add "Default if unanswered: no bpyt bead dispatches".
- **Evidence freshness:** `eba011df`; bd local Dolt read on 2026-10-21. Not inspected: bd remote sync, GitHub PR state, any in-flight worktrees from other sessions.

---

## GP-Q1: an evidence retention rule for `docs/evidence`

**Claims**

- **[Observed] Counts:**
  - 403 tracked files and 20,792,364 bytes at `eba011df`; 388 at `dd520e8d`.
  - All 15 additions landed within about 4.5 hours, which is one burst, not a growth rate.
  - "141 cited by no other tracked file" cannot be reproduced, because no predicate is given. Over the same 388 files I get:
    - 148 by basename substring;
    - 147 by stem;
    - 170 by full path;
    - 218 by "no citer outside `docs/evidence`".
  - None of these is 141 (rule 9: a claim of absence needs a stated predicate and denominator).
- **[Observed] Wrong citation.** "AGENTS.md names a retention posture as an escalation trigger". That sentence is about an act's escalation triggers, and in the acts "retention posture" means product data retention:
  - `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md:90`: "a change to security, privacy, or retention posture beyond the approved secret-classification policy";
  - the CAP1 act, line 39: "privacy or retention obligations";
  - the retained-evaluations retention direction.
  
  The correct governing text is SDR-9 ("Observed **only** when backed by a retained, resolvable gate artifact"), CC-TEST-2 ("only when backed by a retained, resolvable gate artifact") and engineering-bar line 57 ("Evidence retained"). Whether a body that exists only under a tag still counts as "retained, resolvable" interprets owner-approved policy. That is the real reason this is an owner gate.
- **[Observed] `docs/evidence/launch-gate-v2.5/APPROVAL-MANIFEST.json` exists** (4,038 bytes), so the frozen-input example is real.
- **[Observed] The bead underestimates the moves.** `syzygy-bpyt.9.2` expects about 168 movable files, of which 36 need a docs citer repaired, and 184 staying. The 36 repairs mean option A edits docs prose, including pages that `AGENTS.md` and `PROJECT-STATUS.md` cite. The packet's "a later citer of an archived path must cite the tag" understates that.

**Counterexamples and gaps**

- **The CI rule cannot bound growth.** "CI fails on an evidence file that is in none of R0, R1 or the index" never fires, because the generated index (`9.1`) contains every file. The rule bounds nothing unless the index admits only the newest file per family.
- **"Family" is undefined.** Without a mechanical family key, "keep the newest member" is not a predicate.
- **No recurrence is stated.** Nothing says who moves bodies, or when.

**Missing option:** B now, then A once the index has measured the families and classes. The packet treats B as a dead end, but B is A's prerequisite (`9.1`) and gives the measurement A lacks.

**Result**

- **Scope verdict: Revise.** This is a genuine owner question, but for the SDR-9 / CC-TEST-2 "retained, resolvable" reason, not for "retention posture". The 141 figure has no predicate.
- **Recommendation verdict: Revise.** A's CI rule is vacuous, "family" is undefined and the 36 citer repairs are not disclosed. Prefer B now and decide A from the index's measured families.
- **Material corrections:**
  - Replace the escalation-trigger citation with SDR-9, CC-TEST-2 and engineering-bar line 57.
  - State the uncited predicate and re-derive the count at `eba011df`.
  - Define "family" mechanically.
  - Make the CI rule bite: a non-newest file in a family fails unless it is R0 or R1.
  - Disclose the 36 docs citer repairs.
  - Replace "about 15 in one day" with the actual burst.
  - Add a default if unanswered.
- **Evidence freshness:** `eba011df` and `dd520e8d` tree blobs, read with a scratch reader (`/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/treeblobs.py`). Not inspected: the remote, any branch-local evidence not yet merged, and historical digest citers of moved bodies.

---

## GP-Q2: retire the spent governed estate

**Claims**

- **[Observed]** 248 tracked files across the eleven round directories (08:26, b:29, c:32, d:27, e:54, f:21, g:21, h:12, i:10, j:7, k:9), plus 21 in `history/`. These match the packet.
- **[Observed] The keep-in-place list is incomplete.** Things that read or cite rounds a–g from outside them:
  - **The acceptance record:** `ACCEPTANCE-ACT-RECORD.md` cites `round-2026-08e/reviews/RD-31b-wave-a-RAW.md` and `RD-32c-wave-b-RAW.md`.
  - **In-force CC-SPEC and CC-IMPACT policy files** cite:
    - `round-2026-08f` RD-51 raw;
    - `round-2026-08g`'s `SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`, `DISPOSITION-REGISTER`, FIXTURE-2 and `FIXTURE-2-ANSWER-KEY`;
    - `round-2026-08i` files.
  - **Open P-21** cites `round-2026-08c`'s `CONTRACT-RELATION-CLOSURE-REPORT.md`.
  - **`check_governance.py` reads:**
    - from 08: `FINAL-OWNER-ACCEPTANCE-RECORD.md` and `OWNER-ROUND-CHARTER.md`;
    - from 08c: `FINAL-OWNER-ACCEPTANCE-PACKET.md`;
    - from 08d: `OWNER-WORK-ORDER.md`;
    - from 08e: `VALIDATOR-AUTHORITY-INVENTORY.md`, `WAVE-A-CLOSURE-REPORT.md` and `WAVE-B-CLOSURE-REPORT.md`;
    - from 08g: `FINAL-OWNER-AND-SPEC-CLOSURE-PREFLIGHT.md`.
  - **Other tools:** `check_quotations.py` reads an 08c RD-6 raw, and `GOVERNANCE-SUBSTRATE-LOCK.yaml` names 08b.
  - **CI:** `governance-docs.yml:399,402` reads 08f `DRY-RUN-ADMINISTRATION.json`. `ROUND-ESTATE.md` says `DRY-RUN-ADMINISTRATION.md` is also byte-compared by CI.
- **[Observed] Performed candidate packages are runtime inputs.** The packet does not mention this. Examples:
  - `package-reader.ts` reads `public-repo-admission/instances` and `public-egress-v2`.
  - `gate-sources.ts` reads `dossier-local-agent-acts/instances`, including `D9-IN-FORCE-RECORD.md`, and `dossier-agent-provider-v2`.
  - `public-git-source-acquisition-local-agent` and `public-source-screening-scope(-v3)` are read by `public-source-classification.ts` and the POC's `public-source-screening.ts`.
  
  Archiving those directories breaks the consent gate.
- **[Observed] The dedupe failure has a stale pointer behind it.** `ROUND-ESTATE.md` says "Nothing here may be deleted or relocated by an agent… the open question is queued in decisions/DOCUMENTATION-ESTATE-DECISION-PACKET.md". That packet holds only P-54 to P-59 and P-66, all ruled 2026-09-07. The packet never cites those rulings, though several are on point:
  - P-56 (b) kept a spent file in place rather than editing a decision record "to buy a tidier root listing".
  - P-66 (b) declined "a standalone amendment act for prose that binds nothing", adding "the next audit should not re-raise it".
  - P-55 (b) declined the OpenSpec archive step.
  
  GP-Q2 re-raises a question the owner has ruled on, without showing that what changed since then justifies it.
- **[Observed] The "56%" in option C includes the RFC mirror** (that is GP-Q3), so the two items double-count.
- **[Inferred]** The dependency on `2.2` is right, but `2.2` must verify the act-listed files from the tag, not from the tree. It is a consequential governance-verifier rewrite that GP-Q0-A releases without owner sight.

**Counterexample:** option B's premise ("rounds that no act names … except the two live inputs") is false. The acceptance record and in-force policies name files in 08e, 08f and 08g, and checkers read files in 08, 08c, 08d, 08e and 08g.

**Missing option:** keep every byte in place and add one generated sweep-exclusion predicate (driven by `ROUND-ESTATE.md`) to agent routing and governance sweeps. This gets most of the "sweeps and agents keep paying" benefit with no act, which matches P-56 and P-66.

**Result**

- **Scope verdict: Revise.** This is a genuine gate (it touches act-listed and act-preserved files). But the keep list misses at least the acceptance-record raws, the in-force policy citations, P-21's evidence, checker inputs and runtime-read performed packages. It also omits the P-55, P-56 and P-66 precedents and the stale `ROUND-ESTATE` pointer.
- **Recommendation verdict: Revise.** A is unsafe as scoped: performed packages are runtime consent inputs. B rests on a false premise. The no-move exclusion option is missing and probably dominates, given the owner's recorded preference.
- **Material corrections:**
  - Enumerate every citer and reader with a stated predicate, including checker inputs, runtime readers, the acceptance record, in-force policies, open P-rows and CI.
  - Drop performed packages from scope, or list each runtime reader.
  - Cite P-55, P-56 and P-66 and say what changed.
  - Fix the stale `ROUND-ESTATE` pointer (an agent can do this).
  - Remove the "56%" double count with GP-Q3.
  - Add the exclusion-predicate option and a default.
- **Evidence freshness:** `eba011df`. Not inspected: workflows on branches other than main, and external consumers of round paths such as published links.

---

## GP-Q3: one copy of each installed RFC

**Claims**

- **[Observed]** 30 installed and 39 candidate files; all 30 pairs byte-identical (810,512 bytes); the 9 extras are all RFC-0010 and RFC-0011. Confirmed.
- **[Observed] Option C's con is false.** The tree cannot drift silently:
  - `check_governance.py`, around lines 5049-5067, fails on an incomplete or differing mirror pair.
  - CG-7h at `eba011df` reports "30 installed/candidate mirror pairs" in its population, with 0 findings.
  - The bound manifest `general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt`, line 4, reads "# Installed and candidate-mirror bytes are required to match exactly."
- **[Observed] The packet omits P-33 shape (M)** (`WAVE-A-INSTALL-SHAPE-DECISION.md`, ruled 2026-08-16). Installed modules resolve 88 path strings through the candidates tree. CG-1i, "installed-tree path strings (P-33 shape (M))", reports FAIL when an installed module has no candidate twin; it is WARN today with 0 findings over 39 references. Deleting the candidate copies reverses an owner ruling and breaks CG-1i's promise.
- **[Observed] Two performed acts bind the two-copy shape:**
  - `CONTRACT-READABILITY-RESTYLE-ADOPTION-ACT.md:33`: "the installed and candidate mirrors take the same bytes";
  - `RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md:66`: the act "applies the package patch to both mirrors".
- **[Observed]** "Tooling still probes two homes" and "no drift class" are not wins for A, because RFC-0010 and RFC-0011 stay candidate-only either way. Option B is the status quo, since the CI check already exists.
- **[Inferred]** The tag name `rfcs-as-installed-2026-09-01` is misleading: installed bytes changed after that date through the restyle and RFC5 acts.

**Result**

- **Scope verdict: Revise.** This is only an owner gate if A is pursued, because A reverses P-33 (M) and needs successors to two acts' mirror language. The background omits P-33, CG-1i, the bound "required to match exactly" line and the existing CI drift check.
- **Recommendation verdict: Reject.** A's case rests on a false con for C ("silent drift is possible") and misstated pros. Corrected, the analysis favours keeping both copies. That is the status quo, which the packet's own rule says an agent decides.
- **Material corrections:**
  - Delete "silent drift is possible". CG-7h fails on drift today.
  - Merge B into C.
  - Cite P-33 (M) and CG-1i.
  - Quote the bound manifest line 4 and the restyle and RFC5 act lines.
  - Drop "no drift class" and "tooling still probes two homes".
  - Rename or date the tag correctly.
  - Re-decide as not asked (status quo) or present A honestly as reversing P-33.
- **Evidence freshness:** `eba011df`, including a `check_governance.py` run this session (CG-1i WARN with 0 findings; CG-7h OK at 317 predicates). Not inspected: other generators' fallback behaviour if a twin is absent (beyond CG-1i).

---

## GP-Q4: keep the two generated reports committed (not asked)

**Claims**

- **[Observed]** `05-CONTRACT-INDEX.yaml` is 50,795 bytes and `CONTEXT-BUDGET-REPORT.md` is 23,596 bytes. Neither file's current sha256 appears in any tracked file, in full or as a 12-character prefix. They have 97 and 85 path citers.
- **[Observed] The real constraint is not stated.** Both reports are inputs:
  - `05-CONTRACT-INDEX.yaml` is read by `build_capability_1_views.py:47`, `build_polaris_project_wide_contract_coverage.py:22`, `pwb_requirement_amendment.py:63` and at least six PWB builders.
  - `CONTEXT-BUDGET-REPORT.md` is read by `check_governance.py` at lines 5655, 10722 and 10815.
  
  "Readers lose a browsable index" understates it: removing them breaks the generators and the checker.
- **[Inferred]** Greenfield-parity rule 2 requires the justifying constraint for excess to be written down. It belongs in the audit's delta row for these reports, not only here.
- **[Unknown]** Historical digests of these files. I swept current digests only, so I cannot rule out a raw review binding an earlier version (see the AGENTS "zero digest citers does not mean never bound" lesson).

**Result**

- **Scope verdict: Pass.** The status quo is agent-decidable and changes nothing governed. Listing it for challenge is correct.
- **Recommendation verdict: Revise.** Keep committed, but for the real reason: the files are generator and checker inputs. Record that constraint in the audit row. Update bead `1.2`'s rationale, which says no item is agent-decidable.
- **Material corrections:**
  - Add the input-consumer list as the decisive reason.
  - Note the 97 and 85 path citers.
  - Record the constraint in the audit row (greenfield rule 2).
  - Correct `1.2`'s rationale.
  - Label historical-digest citers [Unknown], or sweep them.
- **Evidence freshness:** `eba011df`. Not inspected: historical digests of either file in raw reviews.

---

## GP-Q5: move the ten scripts under `.syzygy/**` into `scripts/`

**Claims**

- **[Observed]** Exactly ten code files sit under `.syzygy/**` (eight in `candidates/scripts/` and two in `round-2026-08j/`). Basename citers range from 3 to 96 files. There are no basename collisions in the top-level `scripts/`.
- **[Observed] "Never by an act record or manifest" is literally true but incomplete.**
  - All ten scripts are governing rows in `docs/evidence/polaris-generator-approval-offer-2026-09-12.json` (sha `48216b06…`).
  - That record is digest-cited by three POLARIS-GENERATOR acts and `ACCEPTANCE-ACT-RECORD.md`, and registered at `check_governance.py:2550`.
  - Its 585 rows are a baseline snapshot. 150 have already drifted, including `build_budget_report`, `build_contract_index` and `verify_final_prespec`.
  - So a move does not break the act, but the packet should say so.
- **[Observed] Agents already edit these scripts without acts:** commits `db364fba`, `3311f0a3` and `aacab441` on 2026-10-03. Moving them to obey an `AGENTS.md` hard prohibition is compliance work and agent-decidable. A governed-prose citer repointed in the process still needs its review round (AGENTS note on candidate-package prose).
- **[Observed] Generated views embed paths that point at a top-level `scripts/`:**
  - `scripts/build_task_router.py`, `scripts/build_dependency_index.py`, `scripts/build_contract_index.py` and `scripts/build_active_manifest.py`;
  - the WAVE-A, WAVE-B and ACTIVE manifests, line 3, name `scripts/build_active_manifest.py`, which does not resolve today.
  
  A move to top-level `scripts/<same basename>` makes those strings resolve. Option A's `scripts/contracts/` does not.
- **[Observed]** `CONTEXT-BUDGET-REPORT.md` lines 215-216 embed full `.syzygy/.../build_budget_report.py` command lines. The exclusion "no generated view's bytes change" forces those commands to stay stale or point at a shim.
- **[Observed] Option B's con is overstated.** CG-1 already has `SIGNED_PACKAGE_MOVED_TARGETS` and the CG-1d moved-path bucket for bound routes to paths that moved.
- **[Inferred] Shims fail the stated goal.** Option A's three-line shims break engineering-bar bias 1 (no same-repo compatibility shims) and leave executable code under `.syzygy/`, so A does not "make the tree obey the rule".
- **[Observed] The packet contradicts itself on the two round sweeps.** It says "GP-Q2 covers them", but GP-Q2-A keeps rounds h–k in place, `round-2026-08j` included. Under the recommended answer to GP-Q2 they never move.

**Result**

- **Scope verdict: Revise.** The eight `candidates/scripts/` moves are agent-decidable compliance. No act binds their bytes, and agents already edit them. Only the two `08j` sweeps touch act-preserved ground, and the packet's routing of them to GP-Q2 contradicts GP-Q2's recommendation.
- **Recommendation verdict: Revise.** Move without shims to top-level `scripts/<same basename>`, so embedded view strings and the WAVE manifest headers resolve. Classify bound routes through CG-1d / `SIGNED_PACKAGE_MOVED_TARGETS`. Regenerate the views rather than freezing stale command lines.
- **Material corrections:**
  - Re-class the eight moves as agent work.
  - Disclose the approval-offer governing rows and their existing drift.
  - Correct B's CG-1 con.
  - Drop the shims (bias 1).
  - Retarget to top-level `scripts/`.
  - Replace "no generated view's bytes change" with "views regenerate and pass `--check`".
  - Resolve the `08j` contradiction: decide those two separately or leave them in place.
- **Evidence freshness:** `eba011df`. Not inspected: local tooling outside the repository that invokes the old paths.

---

## GP-Q6: how the consent gate recognizes a performed act

**Claims**

- **[Observed]** `gate-sources.ts:77-110`'s docstring says an act counts only when its record is "byte for byte what `render_act` writes". The sitting template starts at line 93; the provider-v2 template is at line 211 (a second recorder, `record_dossier_agent_provider_v2_act.py`).
- **[Observed] The gate already recognizes acts two ways.** The packet frames the question as byte-exact versus a future parser.
  - Byte-exact re-rendering (`fromTemplate`) covers only:
    - the five dossier sitting acts;
    - the provider-v2 act;
    - the versioned sign-off (`registrySignoffTemplate`, `package-reader.ts:695`).
  - Field parsing (`parseAct` at `package-reader.ts:105`, and `readDigestBoundActState` falling to `recorderLines` when `form.template === undefined`, line 662) covers:
    - the admission observation and egress acts (`ADMISSION_ACT_FORMS`, line 35);
    - the policy acts (`POLICY_ACT_FORMS`, line 346);
    - the registry act (`REGISTRY_GIT_SOURCE_ACT_FORM`, line 573).
  - So "a parser would need two paths" is already true. The packet's own [Inferred] weakness ("a record with valid fields and altered prose would count") already applies to the observation and egress consents. The owner is not told.
- **[Observed] "A second TypeScript renderer is exported from `@syzygy/polaris-generation-consent/testing`" is false.** `recorder-fixtures.testkit.ts` renders by `spawnSync('python3', …)`, running the real recorders. It is the independent oracle, not a copy. Each ported template therefore exists twice (Python and TypeScript), not three times, so option C's "three template copies" is wrong.
- **[Observed]** `gate-acts.test.ts:602-606` compares each TypeScript form to the Python output for every key.
- **[Observed]** `record_dossier_local_agent_acts.py` (sha `700bb00e…`) has one version and no digest citers. It is a performed recorder with battery `--check` lines (`PROJECT-STATUS.md:465-469`) that re-verify the sitting's acts, including D9's in-force record.
- **[Inferred] What option A actually costs:**
  1. A edits a performed recorder, which bead `3.2` says stays frozen ("Performed recorders stay frozen"), yet A is sequenced after `3.2`.
  2. A shared runtime template file moves the form's anchor into a data file. The parity test becomes circular, because both sides read the same file. That removes the independent oracle that makes byte-exactness worth having.
  3. A overlaps `syzygy-bpyt.8.4`, which converges the package-reader parsers onto one forms table and is labelled consent and security, and which GP-Q0-A releases without owner sight.

**Trust-boundary view:** fail-closed is preserved today by an independent oracle. A weakens that oracle. B (sidecar) is a third model, not a replacement for the second. The only change that touches security posture is any change to what counts as a performed act. That is option B, plus any convergence (`8.4`) that moves the sitting acts onto field parsing.

**Missing options:**
- D: generate the TypeScript template constants at build time from the Python recorder, with a `--check` in the battery. The Python-spawning oracle test stays independent.
- E: status quo, which is two copies held by an independent oracle. That is a justified excess under greenfield rule 2.

**Result**

- **Scope verdict: Revise.** Only option B, and `8.4`'s convergence of the sitting acts, is a genuine owner gate on security posture. A and D are engineering choices. The background misstates the renderer count and hides the existing field-parsed path for observation and egress consent.
- **Recommendation verdict: Revise.** A edits a frozen performed recorder and turns the parity oracle circular. Prefer D, or E (status quo, decided without asking). If the owner is asked anything, ask whether observation and egress consent should move to byte-exact recognition, and whether `8.4` may touch the sitting acts.
- **Material corrections:**
  - Remove "second TypeScript renderer" and "three template copies".
  - Disclose that `parseAct` and `recorderLines` already gate the observation, egress, policy and registry acts.
  - Note that A conflicts with `3.2`'s "performed recorders stay frozen" and that a shared template makes the parity test circular.
  - Add options D and E.
  - Name the overlap with `8.4`.
  - Add a default.
- **Evidence freshness:** `eba011df`. Not inspected: performed act records under `decisions/` (only the code that reads them), and the running gate's behaviour against real records.

---

## GP-Q7: the dossier's execution-permitting arm

**Claims (verbatim where load-bearing)**

- **[Observed] SEC-3** (`security.md:61-111`):
  - "The one permitted case — the owner's attended agent session… the session is on the owner's own host; the owner started it and attends it…; and the owner has recorded a choice for that one run, naming what the instruction covers. A standing or per-project record does not qualify."
  - "Syzygy never gives the instruction to a session it started or to one left running unattended".
  - Its cost bullet: "Nothing contains it, so it gives none of a profile's guarantees."
- **[Observed] D9 is currently established for the gate.** The in-force record's bound digests match the current `security.md` (`766c953d…`) and `v1.md` (`88675bc7…`). The record's sha `41fdfaea…` equals the act argument. `PROJECT-STATUS.md:289` names D9 (2026-10-06).
- **[Observed] REQ-polaris-generation-033** (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:31`):
  - "Syzygy cannot observe who ran the command, or that the operator is the owner: the authoring agent, which runs the neighbouring commands, could run that command itself or write its record into the state directory, and only the skill and agent texts forbid it."
  - Its scenario "Execution permitted under the amendment" requires, when all conditions hold, that "the authoring brief says the agent may build and run the observed project". The off flag is therefore a real gap against a signed scenario. That is the actual spec basis for A, and the packet does not quote it.
- **[Observed]** `execution-rule.ts`:
  - line 16: `PERMITTING_ARM_ENABLED = false`;
  - line 15: "Off until S4 (syzygy-qkea.5) is merged and the flag is switched on.";
  - line 13: "Syzygy cannot see who typed the choice or whether the owner attends, so both are the operator's declaration, labelled Inferred."
  - The arm's 604 lines are confirmed.
- **[Observed] The launched-run exclusion is fail-open and only at one door:**
  - `cli.ts:365` refuses `allow-execution` for launched runs via `isLaunchedRun` (`launched.ts:31-37`), which returns `false` on any read or parse error (`catch { return false; }`).
  - The marker lives in the run directory, which the authoring session writes to.
  - `brief` (`cli.ts:227-236`) never checks `isLaunchedRun`. Launched runs issue their brief through that same command (`polaris.ts:306`), and neither `brief.ts` nor `execution-rule.ts` mentions launch.
  - So with the flag on, a launched run whose choice record exists (written directly, which REQ-033 says is possible, or after the marker is corrupted) gets a permitting brief.
  - The only remaining barrier is the author prompt's text, "build, test and run nothing from the clone" (`polaris.ts:328`).
  - The candidate REQ-044 (one-command run; unsigned, P-111), which would require refusal of both `allow-execution` and brief permission for launched runs, is not in force.
- **[Observed] The credential probe passes vacuously.** `credential-probe.ts:107-128` sets `CONFIGURED_ADAPTER_CREDENTIALS = []`. An explicitly declared empty list passes with `checked: 0`; only an unset environment fails. "The adapter-credential probe passes" is a weaker guarantee than the packet implies.
- **[Observed] The craft policy still forbids execution.** CC-SEC-3 (`security-and-secrets.md:63-82`) still reads "Until the execution-profile RFC is accepted: no observed-project code executes, period". The D9 packet's owner answer (Q4 A) chose a conforming CC-SEC-3 amendment after D9, with doctrine prevailing meanwhile. That amendment has not been made. DECISION-HISTORY P-103 also records RFC5-12's "Absent: no observed code runs" with the RFC 0005 amendment (c) still queued.
- **[Observed]** The 2026-10-15 direction, line 133: "It does not let any session execute observed code (SEC-3; REQ-polaris-generation-044 as drafted)." Quoted correctly.
- **[Inferred] The packet's boundary cannot be enforced as written.** "No execution happens until the owner records allow-execution for a specific run" is enforceable only by the honour system REQ-033 itself describes. The packet presents it as a control.

**What counts as a performed act here:** `allow-execution` is an operator-declared per-run record, not an owner act. Syzygy cannot authenticate it. Turning the arm on makes that unauthenticated record the switch for observed-code execution. SEC-3 permits this only for a session the owner started and attends, and the code cannot verify that.

**Missing options:**
- A-conditional: switch on only after all three hold:
  - the CC-SEC-3 conforming amendment, or an explicit owner waiver recorded as such;
  - a fail-closed launched check inside brief issuance (an unreadable or absent marker on a launched-shaped run refuses);
  - the honour-system and vacuous-probe limits disclosed in the brief and the UI.
- Hold: keep the flag off until those land, with a dated revisit.

B as an indefinite deviation from a signed scenario is not a legitimate end state. B is legitimate only as "Hold, with a named trigger".

**Result**

- **Scope verdict: Revise.** Owner confirmation is right, because this activates a security posture. But the background overstates the safeguards: the honour-system choice, a vacuous probe and a fail-open launched check that is missing from brief issuance. It also omits the outstanding CC-SEC-3 conforming amendment and RFC5-12 (c).
- **Recommendation verdict: Revise.** Recommend A-conditional, or Hold until its conditions land. As written, A would let a Syzygy-started session receive permission if the marker is unreadable or the choice record is written directly, against SEC-3's "never gives the instruction to a session it started".
- **Material corrections:**
  - Quote SEC-3's permitted case and its "never … a session it started" sentence.
  - Quote REQ-033's "cannot observe who ran the command" and its permitting scenario as the spec basis.
  - Disclose that `isLaunchedRun` is fail-open and that `brief` does not check it.
  - Disclose `CONFIGURED_ADAPTER_CREDENTIALS = []` and the vacuous pass.
  - Add the CC-SEC-3 amendment, or an explicit waiver, as a precondition.
  - Add the Hold option and a default of "flag stays off".
  - Recast "no execution happens until…" as an honour-system limit, not a control.
- **Evidence freshness:** `eba011df`, code and spec read directly. Not inspected: live CLI or daemon runs, the actual file permissions of the run directory, and Claude Code / Codex sandbox behaviour.

---

## GP-Q8: the parked provider island

**Claims**

- **[Observed] Two dates, but the owner chose "parked" on only one:**
  - On 2026-10-05, "parked: not offered for sign-off, not deleted" is owner-selected draft text.
  - On 2026-10-15 the owner declined the offered "Keep parked" option and answered in free text: "Syzygy should run *our local codex or claude cli binary* like a subprocess … no custom SDK or API tooling". "Provider routes stay parked and are no longer pursued… Nothing is deleted." is the drafter's direction text.
  
  "'Parked' was the owner's chosen word on two dates" is false for 10-15. The owner's own words lean toward B ("no custom SDK or API tooling").
- **[Observed] Spec basis.** The generation spec still carries provider-mode requirements, which is the audit's justification (delta row 21).
- **[Observed] Recommendation A is status quo, yet asked** (see packet-level finding 1).
- **[Inferred] `syzygy-bpyt.8.1` proceeds whatever is chosen, which is correct.** It decouples imports, edits no behaviour and is useful under A or B. The preface's "anything touching … parked code is asked here" contradicts this. Say that 8.1 is the exception and why.

**Missing option:** D, keep the code but exclude the island from the default typecheck and test projects, or move it to a parked workspace. This removes the "4.8k lines keep being typechecked and tested" cost without a spec amendment.

B should be presented fairly. It is the option closest to the owner's 10-15 free text, and its "un-park cost" is bounded by the tag.

**Result**

- **Scope verdict: Revise.** This is a genuine gate only for B and C, which amend the spec or create a standing gap. The "two dates" claim is false, and the preface conflicts with 8.1 proceeding.
- **Recommendation verdict: Revise.** A is defensible, but its stated reason misquotes the owner. Option D is missing and is cheaper than A's standing cost. B is understated given "no custom SDK or API tooling".
- **Material corrections:**
  - Correct "the owner's chosen word on two dates": 10-05 only; on 10-15 the owner declined "Keep parked" and wrote "no custom SDK or API tooling".
  - Add option D.
  - Reconcile the preface with 8.1.
  - Either drop the item (status-quo rule) or state why it is asked.
  - Add a default.
- **Evidence freshness:** `eba011df`; direction files read directly. Not inspected: the island's current line count beyond the audit's figure (not re-measured), and the remote PRs #258 and #264.