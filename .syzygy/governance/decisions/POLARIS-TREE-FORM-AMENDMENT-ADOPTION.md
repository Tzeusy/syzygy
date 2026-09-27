# Polaris tree-form amendment — adoption and SVG direction

On 2026-09-28 the owner adopted the Polaris tree-form amendment, authorized
its implementation, and ruled that sanitized static SVG is inert under
PWB-REQ-006.

- **The owner's words**, answering the three questions in
  [`POLARIS-TREE-FORM-AMENDMENT.md`](POLARIS-TREE-FORM-AMENDMENT.md):
  "1. Adopt and implement the Polaris tree-form amendment", 2. Permitted, 3.
  Adopt now"
- **What it adopts:** the amended REQ-polaris-generation-004 in
  [the understanding amendment's spec](../../../openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md),
  as merged with this record.
  - The effective composition is 31 requirements and 182 scenarios.
  - It was adopted without a fifth review. The review-4 repairs stand as
    drafted.
- **What it authorizes:** the generator implementation under the packet's
  "What implementation means":
  - the draft schema, prompts, validation and draft-preview renderer.
  - It grants no new project read, provider egress or output write beyond
    existing acts, and it emits nothing on `/polaris`.
- **SVG direction:** under PWB-REQ-006, "active" governs the whole output
  list.
  - SVG reduced to an allow-list of shapes, paths, text and styling is inert
    and may be emitted.
  - That means no script, event-handler attribute, animation,
    `foreignObject`, link, or external or unsafe-scheme reference.
  - The sanitizer is a security boundary, and each excluded class is covered
    by a mutation test.
  - The ruling covers the generator's draft preview now. It carries over to
    the Butlers `/polaris` page package.
