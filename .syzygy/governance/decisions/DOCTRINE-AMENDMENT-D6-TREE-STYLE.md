# Doctrine amendment D6 — tree style and diagrams

> **Status:** Adopted 2026-09-27 by the owner ("Adopt D6"); in force as doctrine amendment D6.
> The owner adopts by saying so plainly, as with D1 and D5.

D6 restyles all six doctrine files to CC-REV-8 without changing what any rule
requires, permits, or forbids.

## What changes

- **Answer first.** Each file and each section opens with a one- or
  two-sentence answer.
- **Rules become shallow trees.** Each rule's bold lead-in is followed by a
  one-line statement of the rule. Below that come its conditions, then its
  examples and *Violation* line.
- **Eight diagrams, where structure beats prose.**
  - vision.md: the three states, the difference, and the actuator toolchain.
  - v1.md: V0 → V1 → deferred.
  - architecture.md: the write plane, snapshot → evaluation → record, the
    loop, and the kernel with its three surfaces.
  - security.md: SEC-1's client classes.
  - trust-and-evidence.md: how a claim gets its label.
- **Each diagram only draws what its section's text already says.**

## What stays fixed

- every `VIS-n`/`SEC-n` identifier and rule title, in its bold lead-in form;
- VIS-1's ranks 1–5, VIS-6's exceptions (a) and (b), and the trust floor's
  bullet order;
- every cited section heading;
- D3's two anchor sentences.

## Review

VIS-3 requires a fresh-reader review.

- **Review 1** —
  [`DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-1-RAW.md`](DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-1-RAW.md),
  verdict **REVISE**. Rule bodies showed no drift; the findings sat in the new
  openings and diagrams.
  - The four material findings are all repaired:
    - B1: "Syzygy and its agents" is restored in VIS-4.
    - B2: VIS-5 reads "affects … only through typed, explicitly authorized
      adapters" in both its opening and its bullet.
    - B3: the plane diagram no longer implies the governance root skips
      consent.
    - B4: security.md's opening no longer invents a trust-earning path.
  - Every minor finding (B5–B16) and diagram finding (D1, D3, D5, D6, D8) is
    repaired with the reviewer's suggested wording or an equivalent fix.
- **Review 2** —
  [`DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-2-RAW.md`](DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-2-RAW.md),
  verdict **REVISE**. Review 1's findings were resolved, except item 11 and
  B16, which were partly resolved.
  - The one material finding is repaired. N1: "Reading is unrestricted"
    became "Reading reaches declared sources anywhere in the project; direct
    writing is confined to two roots" in vision.md and architecture.md.
  - Every minor finding (N2–N8) is repaired with the reviewer's suggested
    wording, including item 11's "Three further points apply to V0".
- **Review 3** —
  [`DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-3-RAW.md`](DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-3-RAW.md),
  verdict **CONFIRM WITH EXCEPTIONS**. Every earlier finding is resolved. Its
  notes M1–M4 (one grammar fix, one summary hedge, one repeated phrase, reflow)
  are notes only. Under the notes-only stopping rule they clear these bytes,
  and they are left for the next doctrine edit rather than repaired here, since
  a repair would retire this confirmation.
