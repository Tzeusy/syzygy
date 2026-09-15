# Owner decision — launch-gate v2.5 / schema 2.1

Date: 2026-09-15
Owner: Tzeusy
Decision identity: LAUNCH-GATE-V2.5-APPROVAL-2026-09-15
Project identity: project:syzygy
Provenance: owner-adopted (bootstrap, uncorrelated)
A1 audit-record identity: explicitly absent

## Owner act and exact scope

[Observed] In interactive chat, in response to the exact reviewed package offered
for local installation, the owner replied verbatim:

```text
approved
```

The offered approval manifest is retained unchanged at
`docs/evidence/launch-gate-v2.5/APPROVAL-MANIFEST.json`.
Its verified SHA-256 is `00836a44a43e80f4c1468b130375d9532becac460f652ca0e1807131b545a738`.
The original local evidence paths in that manifest map by basename to the retained
files in `docs/evidence/launch-gate-v2.5/`; the candidate/source paths retain their
original repository-relative locations. All subject and raw-review hashes were
verified before installation. The manifest is a subject reference, not an earlier
owner act.

This act approves instrument v2.5 and schema 2.1 as the successor process policy
and authorizes local installation of the three exact subjects below, recording
this decision and updating current-state routes. It supersedes the instrument and
schema versions approved by P-34 on 2026-08-16, without changing that prior decision,
its reviewed bytes or its historical effects. The prior files remain in Git history.

| Installed subject | SHA-256 |
|---|---|
| `launch-gate-pre-specifications.md` | `a5b50cba97707ce7caa4f30386c32f98643600eb434af6a2c432d04258ae06c6` |
| `launch-gate-administration.schema.json` | `925955a025adf0b2cb92a7c1454a872f465f1ceb93dd36b74e6fec58ebc7d359` |
| `scripts/validate_launch_administration.py` | `623005464b4c50795c5184a78f90f1b0f7656c8732a34a2bfd3c646213291cf0` |

## What was approved

RD-56 f11: schema 2.1 admits only instrument-bound question identity; the unchecked
per-question hexadecimal alternative is removed. P-53: SPEC_MEDIUM identifies
OpenSpec without the stale absence claim. Validator support selects a full-commit
record's schema at that commit and checks local schema drift against HEAD.

Question text, verdict formula, F5 posture and parameter rows other than SPEC_MEDIUM
remain unchanged. The exact successor source files retain reviewed candidate-era
banners; this record determines their authority, not those immutable banners.

## Reviews and evidence

Policy review: **CONFIRM**, after the missing review-class declaration was
corrected. Structured-record review: **CONFIRM**. Raw outputs are retained unchanged
as `policy-review-2-RAW.md` and `record-review-RAW.md` under the evidence directory.
The first policy **REVISE** also remains in `policy-review-1-RAW.md`.

[Observed] Pre-installation evidence covers 126 validator fixtures, 38 renderer
fixtures, a failing restored-hex mutation, and unchanged replay/render checks of
Administration 1 and the committed full-commit dry run under the exact successor
in a disposable clone. The supporting-code-only canonical battery is retained
separately; it ran with predecessor normative files and is not post-install proof.
Post-installation verification is retained as an additional evidence record.

## Residuals and exclusions

RD-67 abbreviated-commit schema selection and RD-68 invisible-character false-READY
paths remain knowingly excluded and unresolved. Historical replay evidence is
limited to the two named full-commit records, not every schema-2.0-valid record.
No general false-READY-resistance assertion is made.

This act does not authorize remote publication or merge, a new administration,
launch, release, deployment, new source reads, provider egress, or repair of those
excluded findings. It is a human process-policy decision, not a readiness verdict
or evidence that any authorized effect succeeded. Local installation is the sole
new effect scope; no A1 correlation or independent attendance proof is claimed.
