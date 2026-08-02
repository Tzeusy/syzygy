# Craft-and-care installation record

**Installed:** 2026-08-02, at the rev7 rework (Pass C1), from
`_bootstrap/rfc-phase/craft-and-care/` (the bootstrap-phase record, kept
unchanged as review evidence).

**Approval provenance:** the cluster was approved by the owner as decision
**D2** (2026-08-01, acceptance walkthrough — `_bootstrap/rfc-phase/OWNER-ANSWERS.md`).
Amendment **B21** (relaxing SDR-21's "one action back to home" to
RFC9-10(c)'s availability wording) is applied in
`performance-and-visual-discipline.md` (CC-VIZ-5) with its supersession note
in place. Review evidence: fresh-context reviews 4 and 7
(`_bootstrap/rfc-phase/reviews/`), raw output stored unchanged, dispositions
recorded.

**Status:** these policies are owner-approved engineering standards and this
directory is their canonical home. They **bind implementation work only from
foundational-RFC acceptance**, because they consume RFC clause IDs
(RFC9-47's gate list, RFC4-13's tiers, RFC2-25's vocabulary) that bind
nothing until the owner writes `ACCEPT FOUNDATIONAL RFCS`. Nothing here is
retroactively weakened by that sequencing; it is the ordinary
policy-cites-contract dependency.

**Content digests (sha256) at installation:**

```
75b5c203eafac911cca3f7285575f9b67b43cf3b21624b5fed81da8e634b74ac  agent-provenance-and-execution-evidence.md
a1521d3fc9ba7cc7d11855018b11b8fa888addfd68fb0f82d50b8016412bedda  engineering-bar.md
891d082057330bb4312d30c479e4e25f2f6ae9e354c0c2d68d932da2a396f038  interfaces-and-dependencies.md
7c844a0e962ded1eaee6d6ed3830d6b8d5c8cfbb1c821e361fbaba802dca5965  observability-and-operations.md
3b06ba9f28225ef938aed801b5e7afc3948e9db8b1837f27dcec88618cb78bb9  performance-and-visual-discipline.md
4328fe52bd9252fd3341d54c53dbddbca078b7252c87348f0fd1b849cce52039  README.md
220c45e31712bcb9c16d77289cba76a6b8b9cb48913bcec9d0d665a9c0910475  review-and-documentation.md
d5fecdf5f07edbfc530af98f813d3560922f549c85394173f88bada45ac9209c  security-and-secrets.md
aa2d6353de88e64a99a8faebc9ba6ea9c91f2ebe38cd5196e7ea1e1587b52821  testing-and-verification.md
```

**Amendment record:** `testing-and-verification.md` was amended once after
installation (2026-08-02, rev7 review 9 finding S1): CC-TEST-2's
emitter-distinct capture predicate is now explicitly scoped to RFC4-13
routes 1–2, with routes 3 (owner-declared trusted oracle) and 4 (governed
checker, RFC4-13(b)) named as the owner-created exceptions carrying their
own guards. Digest above reflects the amended content; the pre-amendment
digest was `543f611d585d8aecfebd04f18cf95d4fe0ad44ea22b4a6ba121f468ec87e579e`.
The amendment applies existing owner decisions (A2; RFC 0002 §8 q3) and is
confirmed only by its **own owner act** — `CONFIRM CRAFT AMENDMENT:
CC-TEST-2@aa2d6353de88e64a99a8faebc9ba6ea9c91f2ebe38cd5196e7ea1e1587b52821`
— never implicitly by the RFC gate; no new decision is minted here.

(Regenerate anytime with `sha256sum *.md` in this directory; the values
above were captured at install time and exclude this record itself.)

**Owner-act provenance note (RFC3-16(a) posture):** like every
authorization-bearing artifact adopted before the provenance mechanism
exists, this installation's authority rests on the recorded D2 ceremony and
will be bound by the one-time bootstrap correlation act (RFC3-16(b)) when
the mechanism ships. Until then its gap is stated here, not hidden.
