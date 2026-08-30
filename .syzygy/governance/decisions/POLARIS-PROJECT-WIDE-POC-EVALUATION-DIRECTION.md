# Owner direction — project-wide Polaris POC evaluation

Date: 2026-08-31

Owner: Tzeusy

Decision identifier: `POLARIS-DIR-2026-08-31`

The owner directed: **“Update Polaris to focus on 'succesfully modeling all
of Butlers' as part of the evaluation criteria for our POC”**.

This follows the owner's cold-open walkthrough findings that the current page
talks only about one WhatsApp feature, does not explain Butlers, and uses
LLM-like language where simple, concise communication is needed.

## What this direction changes

The bounded Three-Surface POC now evaluates Polaris on whether it models and
explains the full declared shape of the one configured Butlers project. A
self-selected capability slice is not sufficient project-level coverage.

“All of Butlers” is bounded by Butlers' own declared project shape. Missing,
unreadable, contradictory or unmodeled declarations remain visible and count
in the denominator; they do not authorize invented positive facts.

## What this direction does not change

- The POC remains limited to one configured Butlers repository.
- The existing WhatsApp capability slice may remain as drill-down content; it
  is not the project-level narrative.
- The signed `three-surface-poc-experience` artifacts remain unchanged at
  their recorded digests.
- This direction authorizes amendment authoring. The resulting candidate
  specification still requires a separate owner sign-off before
  implementation.
- Production release, deployment, multi-user support, broad remote access,
  autonomous intent adoption and Syzygy-authored implementation code remain
  prohibited.
