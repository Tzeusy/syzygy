# R-POLARIS-DOSSIER-GATE-SOURCES-1
Verdict: REVISE
Reviewed commit: ff8323003a9ea3381920083a473eb90b05e774f0
Subject: PR #377 (syzygy-qkea.21)

Reviewer: fresh-context independent reviewer, 2026-10-07. Scope: `git diff origin/main...ff832300` (13 files, +601/-92; two commits, 2aeaa23c and ff832300). Any later evidence-only commit is out of scope. No external or target repository content was fetched.

## Governing clauses (quoted)

- RFC3-16(a) (`.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:168, located via `DIRECTIVE-REGISTER.md`:277): "An effective owner act is an actual human owner act whose record is current, attributable, scope-matched and bound to the artifact's exact digest under RFC3-16(b)." and "Being present, well-formed, and correctly attributed *in the tree* is not sufficient."
- polaris-dossier-local-agent-mode v1.1 (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md`:11): "Syzygy SHALL refuse to issue a brief unless an in-force, recorded, per-project statement names the operator's agent provider and the content classes it may receive ... its withdrawal SHALL refuse further steps of any run that relies on it." and (:13) "Syzygy SHALL establish that the observation consent, the registry entry, each policy act, any per-project statement, D9 and the owner's reading of RFC7-20 are in force from the record of the owner's act that makes each effective ... never from a status word or a file's presence." and "withdrawal of the observation consent, the registry entry or a policy act refuses every later step of the run."
- The statement record's own withdrawal clause (`dossier-local-agent-acts/instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`, "## Withdrawal"): "Withdrawal is a later owner act naming this record."

## Verification performed

- [Observed] Scratch worktree at ff832300, `npm ci`, `vitest run packages/polaris-dossier packages/polaris-generation-consent`: 23 files, 852 tests passed. `tsc -b` on both packages: clean.
- [Observed] The provider-statement gate is `providerStatementGate(records, agentTool, provider, now)` (`packages/polaris-dossier/src/gate-sources.ts`:160) and filters `r.agentTool === agentTool && r.provider === provider` (:162). `init.ts`:124 passes `config.config.agentTool, config.config.agentProvider`; `reverify.ts`:152 passes `declared.agentTool, declared.agentProvider`. The PR body's "For the reviewer" note (provider only) is stale, as the brief said.
- [Observed] Fixtures come from the real recorders: `renderDossierLocalAgentAct` calls `record_dossier_local_agent_acts.render_act(m.ACT_BY_KEY[key], ...)` and `renderLocalAgentSignoff` calls `record_versioned_signoff.render_record(real_packages()['public-git-source-acquisition-local-agent'], '1.0', ...)` over the installed entry (`packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts`).
- [Observed] Forms match the recorders: file `DOSSIER-LOCAL-AGENT-{stem}-ACT.md`, title `# Owner act — {title}`, identity `{identity_stem}-{date}`, act types and artifact paths are the same in `scripts/record_dossier_local_agent_acts.py` (`ACTS`, lines 157-208 at head) and in `gate-sources.ts`:77-109. The sign-off form (file `PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1.0.md`, title, Package/Version/Tag/Kind/Installed entry, `Act type: adopt-registry-entry`, `Installed entry SHA-256`) matches `record_versioned_signoff.render_record` and `installed_lines`.
- [Observed] A probe test (scratch worktree only, since removed) built the recorded-act world the PR's tests use, then added one decisions file at a time.

## Findings

1. **REVISE — a withdrawal that names the provider statement by its own Record ID or Subject is not seen; the gate stays `ok` (criterion 1).**
   Evidence: `gate-sources.ts`:83 sets the sweep stems to `dossier-local-agent-<stem>` and the act identity stem (`agent-provider-redis-anthropic`, `agent-provider-redis-openai`). The record's ID is `AGENT-PROVIDER-redis-redis-anthropic`, which folds to `agent-provider-redis-redis-anthropic` and does not contain `agent-provider-redis-anthropic`. `namesDigestBoundAct` (package-reader.ts, unchanged in logic) checks the stems, the full artifact path, and the `Artifact identity`/`Act identity` field lines only. It does not check `Record ID` or `Subject` lines, which `namesAdmission` does check for admissions.
   Probe [Observed]: with both statement acts recorded, adding `decisions/WITHDRAW.md` = "The owner withdraws the agent-provider statement `AGENT-PROVIDER-redis-redis-anthropic`." left `providerStatementGate(..., 'claude-code', 'anthropic', NOW)` at `{"state":"ok","record":"AGENT-PROVIDER-redis-redis-anthropic@0.1.0-candidate.1"}`. A file reading "Subject: `(project:syzygy, repository:redis-redis, agent-provider:anthropic)` withdrawn." also left it `ok`. By contrast, the drawer record (`NO-EVIDENCE-DRAWER-redis-redis` contains the stem `no-evidence-drawer-redis`), the D9 record and the RFC7-20 record (their Record IDs equal the identity stems) are each refused when named by Record ID (probe: drawer unstated, `rfc720Ruling` refused).
   So the statements are the one class where naming the record in the way the record itself says withdrawal works ("a later owner act naming this record") does not defeat the grant. The spec (:11) says "its withdrawal SHALL refuse further steps of any run that relies on it".
   [Inferred] The sweep is documented as a backstop for withdrawal forms nobody has defined, and no withdrawal recorder exists yet. Naming a record by its Record ID is still the most likely form a withdrawal will take.
   Proposed repair: add each statement's `recordId` (and, ideally, its Subject tuple) to the form's stems or to a field-line needle list. [Observed] A sweep of the `decisions/` tree at ff832300 for `AGENT-PROVIDER-redis-redis` returns no hit, so the real-tree test stays green. Add a test that withdraws each statement by Record ID and by Subject.

2. **REVISE — the registry sign-off cannot be withdrawn by its tag (its act identity), and a test pins that a withdrawal naming it stays `ok` (criteria 1 and 6).**
   Evidence: `LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.stems` is only `['public-git-source-acquisition-local-agent-signoff']` (`package-reader.ts`:638), plus the installed path. The act identity the reader returns is the tag `public-git-source-acquisition-local-agent-v1.0`, and the recorder calls that tag "the binding". The tag is not swept.
   Probe [Observed]: "The owner withdraws the sign-off tagged public-git-source-acquisition-local-agent-v1.0." left `registryEntry()` at `{"state":"ok","record":"public-git-source-acquisition-local-agent-v1.0"}`. The PR's own test `gate-acts.test.ts`:188-195 writes "... and the public-git-source-acquisition-local-agent sign-off." and asserts `registryEntry().state` is `'ok'` (:195). The withdrawal arms that do refuse need the literal `...-signoff` stem in a filename (`start-gates.test.ts`, `...-SIGNOFF-REVOCATION.md`) or the full installed path (`gate-acts.test.ts`, `WITHDRAW-ENTRY.md`).
   [Observed] The tag cannot simply be added as a stem: `decisions/PENDING-OWNER-DECISIONS.md`:1115 (P-104) quotes it, so the whole read would refuse. [Observed] `record_versioned_signoff.py` defines no withdrawal form ("a later edit is a new version, never a retirement of the earlier one"). The spec still requires that "withdrawal of ... the registry entry ... refuses every later step".
   Proposed repair: sweep the tag (and the package key followed by "sign-off" in any spelling) in every decisions file except the P-104 register row. Route that exemption through `CITATION_ALLOWLIST` at the register's exact bytes, or exempt `PENDING-OWNER-DECISIONS.md` the way the aggregate record is (field lines only). Then change the assertion at `gate-acts.test.ts`:195 to expect `refused`. Without that, the test certifies a fail-open.

3. **NOTE — the registry gate admits a changed reader silently. This is recorded for the owner's pending question, not adjudicated (criterion 4).**
   [Observed] `readVersionedSignoffState` binds the v1.0 record's package, version, tag, kind, installed path, act type, verdict (CONFIRM or CONFIRM WITH EXCEPTIONS) and instant, plus the installed entry's SHA-256. `registryEntryUsable` (`gate-sources.ts`:239-258) then checks only `implementationId === 'polaris-dossier/git-object-reader'` and a non-blank `implementationVersion`.
   [Observed] Nothing binds the bytes of `packages/polaris-dossier/src/git-object-reader.ts`. 8422119c changed that file (+16/-5 lines). The entry's own `implementationStatus` says "any change to it is a new implementation version and a new version of this entry". The owner's open question (`REDIS-LOCAL-AGENT-SITTING-BRIEF.md`:263-283) asks whether "as merged" means the reader at PR #367's merge or the reader on `main` when signed.
   Whatever the answer, this gate would admit the 8422119c reader, and any later reader edit, under a v1.0 sign-off. The brief already says so at :276-280. Should the owner answer (a), or want post-sign-off drift caught, a reader-bytes digest in the entry (or a pinned digest in the gate) is the mechanism. That is an entry change and needs a new version.

4. **NOTE — readers are laxer than the recorders' output in fields RFC3-16(b) makes load-bearing (criterion 2).**
   `readDigestBoundActState` checks title, Date, Act identity, Act type, Artifact identity, Project identity, Exact digest, Recorded at and Supersession. It does not require the `Owner: Tzeusy`, `Provenance state`, `Scope` or `A1 audit-record identity ... explicitly absent` lines that `render_act` always writes (record_dossier_local_agent_acts.py lines 332-352). `readVersionedSignoffState` likewise ignores `Owner`, `Provenance state`, `Scope` and A1, which `installed_lines` writes. The `installed_lines` docstring in `scripts/record_versioned_signoff.py` states that "RFC3-16(b) makes a record that omits item 9 invalid."
   [Inferred] The impact is low, because a forger who can write the record can write these lines too. It is still a laxer parse than the output form. Repair: `one()` each of those lines with its exact recorder text, or record the gap as accepted.

5. **NOTE — mutant coverage gaps (criterion 6). No mutant record is on the branch; the PR says one will follow.**
   [Inferred, from reading the tests against `boundMismatch` (`package-reader.ts`:571-590) and `providerStatement`]:
   - The whole-artifact `| File | SHA-256 |` count clause (a second table hidden in a fence) is never exercised alone. The "twice" fixture adds an unfenced table, which `at.length !== 1` already kills.
   - The `|---|---|` separator check has no test.
   - An extra third row is untested, so `rows.length !== bound.length` weakened to `<` would survive.
   - A duplicated `Record ID`/`Subject` line in a statement or drawer record is untested (`field` requires exactly one).
   - `withdrawn` is hard-coded `false` at `gate-sources.ts`:154. Withdrawal therefore reaches the gate only as `act: null` through the sweep, so the gate's "is withdrawn" arm is unreachable from the package source. That is acceptable fail-closed, but the disclosure reads "has no owner act binding its bytes", not "withdrawn".
   Repair: add these fixtures, and include them in the forthcoming rule-6 record with old/new fragments.

6. **NOTE — fail-closed spots checked and found holding (criterion 1) [Observed via the PR's tests and my run].**
   - With no record: D9 and the reading are not established, the drawer is unstated, the statements are `[]` and the registry is absent.
   - Bound doctrine or direction bytes edited or missing: refused.
   - Table missing a row, or naming another file: refused.
   - Record edited after its act: refused, or `act: null`.
   - Before the act's instant: absent.
   - Wrong subject, statement, record id, version, tool, second tool line or provider: unstated, or `act: null`.
   - Sign-off with wrong title, version, tag, package, kind, installed path, act type, verdict, instant or fence placement: refused.
   - Installed entry edited or missing: refused.
   - Repository other than `redis-redis` (including `__proto__`): unstated / `[]`.
   Findings 1 and 2 are the exceptions.

7. **NOTE — act-state labelling and the real-tree pin hold (criterion 5).**
   [Observed] No PR byte labels any sitting act accepted or in force. `gate-sources.ts` comments describe D9 as "adopted by the owner's words, logged in the doctrine amendment log with no digest", which matches the record's own Adoption line. `gate-acts.test.ts`:84-91 pins every source absent or not established on the real checkout, and it passed in my run.
   Two consequences:
   - That test, and `real-tree.test.ts`'s new `registry sign-off` arm (not refused), will fail on the commit that records the sitting. The sitting commit must update them, and it should be named in the sitting's install steps.
   - [Inferred] If a future sitting log in `decisions/` lists the act identity stems (for example `D9-IN-FORCE-OPERATOR-AGENT`), every gate refuses. That is fail-closed, but it is worth a line in the installer's checklist, the same lesson as the P-104 row.

8. **NOTE — scope matching for statements (criterion 3) holds [Observed].**
   The record must carry exactly one `Agent tool:` line that opens with the form's tool name, a Subject naming the provider, and the form's Record ID (`gate-sources.ts`:138-155). The gate matches the exact (tool, provider) pair, case-sensitively, at both init and reverify. Tests cover the cross pairs (`gate-acts.test.ts` "consent to one tool with one provider"; `gate-parts.test.ts` reverse pairing and case variants; `start-gates.test.ts` Codex/Anthropic at init and Codex/OpenAI vs Claude Code at reverify). `reverify.ts`:129 also refuses when the run record's declared tool/provider differ from the brief record's.
