# Raw review — PWB P-63 arm A Polaris human-page trim (syzygy-1z3.27)

Independent fresh-context reviewer (a separate Claude session, spawned with no
access to the author's conversation) over commit
`4217818143ec1e05cc3c9f2bde80379336c0f98c` on `agent/syzygy-1z3.27` and the
then-uncommitted `docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json`.
Output stored verbatim below (raw reviewer output; never edited). The author's
dispositions are recorded in the evidence file above (`review.dispositions`), in the
follow-up commit `509b749d9af6eb6d889c2b319fa061fa350330e7` and in bead `syzygy-1z3.27`, not here.

---

Independent review of 4217818 (syzygy-1z3.27, P-63 arm A) — verdict CONFIRMED WITH FINDINGS; full report follows.

## Verdict
CONFIRMED WITH FINDINGS — no blocker. The trim does what the bead asks and the measurement reproduces independently; two should-fix items (one before close, one code hardening) and several notes.

## Independent measurement [Observed]
Private daemons (`--port 0 --state-dir <scratch>`, loopback 7478 never contacted), Butlers `03f9ae74a` clean. "After" served from the worktree at 4217818; "before" served from a fresh local `git clone` of the Syzygy repo checked out at 301ba69 with `tsc -b apps/three-surface-poc` (an unauthentic observer revision fails the consent act, so `git archive` copies render `pwb-unobserved-not-admitted`, 83 KB).

| form | before | after | saving |
|---|---|---|---|
| direct | 2,047,721 | 1,612,761 | 434,960 |
| tailnet Host | 2,053,361 | 1,618,401 | 434,960 |

Byte-identical to the evidence file; 434,960 ≥ 430,080 (420×1024). Evidence arithmetic (savings, headroom 43,791→478,751, 25,119 spare over 453,632) all checks. Invariants between my own before/after tailnet captures: multisets of `data-claim-id` (529), `data-anchor-id` (713), `id` (329), `data-polaris-item` (242), `data-polaris-source` (270), `data-narrative-block` (521), `data-claim-provenance`, `data-unknown-disclosure` (30), `data-polaris-section`, `href` (874), `data-parity-field` — all EQUAL; Unknown claim-id set 19=19 EQUAL; claim tuples sans evaluation id EQUAL; narrative JSON 521 blocks / 713 anchors equal after scrubbing per-run identities; 498 fragment hrefs, 0 dangling both; 376 internal hrefs all mount-prefixed both; visible text (20,495 tokens) differs in 13 tokens, all hex identities/timestamps. `data-copy-role`/`data-claim-role` declarations 2,395→1,917 (the two dropped cell roles per item row less the nine region roles; designed).

## Findings

1. **should-fix** — `apps/three-surface-poc/src/polaris-source.ts:49-50` `sourceRouteIdentities` silently drops an identity containing `'`. [Observed] via a throwaway script against `dist/polaris-source.js` using the real `escapeHtml` (`packages/cap1-daemon/src/routes-human.ts:111`): `encodeURIComponent` leaves `'` raw, `escapeHtml` turns it into `&#39;`, and the capture `[^"&]*` stops at `&` so the whole pattern fails to match — 9 identities in, 8 out; `&`, `#`, `%`, `+`, `@`, `<>"`, space and non-ASCII all round-trip under both mounts. The entity-unescape chain after the capture is dead code (no `&` can be captured). The retired carriers (`data-source-route` + `decodeAttr`; preflight's `encode(identity)`) handled `'`. Consequence: `exactRequirement` would fail closed, but `sourcePaths` and `probeSourceRoutes` would silently skip such an identity. Exposure today is latent — [Observed] 0 of Butlers' tracked paths contain `'` — but this helper is now the sole reader inside a preflight guard and has no unit test of its own. Fix: capture `[^"]*`, unescape entities, take the `identity` param, then `decodeURIComponent`; add a round-trip test with `' & # % + @`.

2. **should-fix (acceptance 1)** — `docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json` is untracked (`git status`), so "retained in docs/evidence/" is not yet true; commit before close. Also `syzygy.before.surfaceVersion` and `after.surfaceVersion` are both `null` while the note calls the surface version "the stable anchor" — record it or drop the note. The embedded `measurementScript` carries a session-specific scratchpad path.

3. **note** — evidence `captures.*.api-polaris.json` (37 bytes) is an HTTP **401** body `{"admitted":false,"served":"nothing"}` [Observed]; `apiEnvelopeUnchanged: true` therefore rests on an unauthenticated response, not the machine envelope. The claim holds by inspection (the diff touches no API path) but the evidence should say so rather than imply a measured envelope.

4. **note** — worktree has an uncommitted `AGENTS.md` change (+20/−5, notes-to-self about this bead, mtime 22:45) not in the subject commit; I did not make it. Commit or discard deliberately.

5. **note (tests)** — no assertion was weakened beyond the designed change. `polaris-narrative.test.ts:205-207` drops the four cite-attribute equalities and replaces them with "the cite carries exactly `data-anchor-id`" plus the `blockId#a` prefix; the machine-side equivalents (anchor set vs independent oracle, captured label/tier/reason, every cite in the block's anchor set, count equality) remain. `polaris-capability-detail.test.ts:335` `not.toContain(`#${digest}`)` is near-vacuous (`#sha256:bbbb…` matches no render path I found) but the machine-form loop at :338-339 is the real guard and is unchanged. `polaris-source-route.test.ts:204-210` now compares href to `sourceRouteHref(decode(href))` — close to tautological, though it does prove decode is the exact inverse for fixture identities containing `@ : / #`. `walkthrough-preflight.test.ts:75` previously read the attribute undecoded; the new reader decodes — an improvement.

6. **note (roles/readers)** — Hoisting `FACT` onto the class-table region (`polaris.ts:540`) is semantically neutral for the copy sweep: `polaris-copy.test.ts` attributes text to the innermost declaring ancestor, so key-cell text stays `project-fact` and tuple text stays `epistemic-disclosure` (the span declares its own; the cell holds nothing else). Screen readers: `data-*` carry no AT semantics and the region's `role/tabindex/aria-labelledby` are unchanged [Inferred]. `narrativeUnits`' `countNested` nets out `<td>` anchored blocks inside the framing region. The sources table region is not hoisted; its `<tr>` still carries the role. Note the parity sweep keys on literal `<tbody>` and reachability on `region.inner.startsWith('<table>')` (`polaris-parity-sweep.test.ts:491`, `polaris-reachability.test.ts:346`); the hoist correctly targets the div, not the table — the AGENTS.md note records this trap.

7. **note (readers/spec)** — [Observed] `git grep` at 301ba69: the eight retired attributes appear only in the eight files this diff touches; after the change no reader remains in apps/, packages/, scripts/, docs/, .syzygy/ or openspec/ (only the P-63 evidence file names them). PWB-REQ-014 (`openspec/changes/polaris-project-wide-butlers-model/specs/.../spec.md:759`) names no cite attribute; it binds `presentation-artifact`/`non-citable`, one claim role per unit, and the anchor record fields — all still emitted (`claimRoleAttrs`, narrative JSON). `docs/PWB-IMPLEMENTATION-PLAN.md:914` ("no `data-anchor-*`" on non-status-bearing blocks) still holds.

8. **note (gates)** — `npx vitest run apps/three-surface-poc`: 34 files passed / 1 skipped, 342 tests passed / 1 skipped, exit 0 [Observed]; `polaris-accessibility.browser.test.ts` ran (9 passed). `npm run typecheck` exit 0. There is no `lint` script in package.json. Rule 6: [Observed] the diff adds no new guard (no new `problems.push`); the rewritten check at `walkthrough-preflight.ts:177` is the same guard with a new reader, and existing assertions (`expect(new Set(linked)).toEqual(admitted)`, preflight pass) would fail if it returned nothing [Inferred; no mutation run]. The evidence's uncharacterised "2 failures that did not reproduce" deserves a bead.

Acceptance criteria 1–4 are met on the evidence and my reproduction except the retention gap in finding 2; criterion 5 is this review. Non-goals honoured [Observed]: no registry/spec/policy, roster-registry or Butlers change in the diff. Nothing left in the worktree; scratch artefacts and private daemons are cleaned up.
