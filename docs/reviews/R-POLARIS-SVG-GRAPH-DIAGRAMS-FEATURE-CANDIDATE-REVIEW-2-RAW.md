REVISE

Reviewed commit: `674cfaa4e81a022ecaadf742f027f874a0883276`
Candidate SHA-256: `303958396129b66810c50cfc1dec042077201f46b6905bf408529d3986294f54`

## Blocking finding — Review 1 was not retained verbatim

`docs/design/POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE.md:480-482` claims that Review 1 raw output is retained verbatim at `docs/reviews/R-POLARIS-SVG-GRAPH-DIAGRAMS-FEATURE-CANDIDATE-RAW.md`.

The 78-line file at that path is instead a rewritten, reordered, and condensed reconstruction of the delivered Review 1 output. It adds synthesized structure, paraphrases the findings and confirmed aspects, and omits delivered material including the PR-readiness section.

This violates CC-REV-6 and the candidate’s exact-review gate at lines `468-471`. A synthesis cannot be labeled or relied upon as verbatim raw evidence.

Preserve the committed reconstruction as historical bytes. Add the actual Review 1 response unchanged under a distinct `-RAW.md` filename, route the candidate’s Review 1 reference to it, and describe the existing reconstruction honestly. The corrected exact head then requires confirmation.

## Semantic repairs confirmed

- **F1 repaired:** lines `120-145` separate model `relationshipInstanceId`, RFC1-25(d) `typedRelationId`, and presentation `label`; `edgeKey` derives from the relationship-instance identity. The `chain` and `diamond` fixtures require multiple same-class instances to survive SVG, text, and parity.

- **F2 repaired:** lines `149-155` make hierarchy relationship instances the sole truth carrier. Nodes carry no parent input, edges carry no hierarchy boolean, and parent/root values are derived. The `hierarchy-authority` fixture covers disagreement, missing endpoints, and false roots.

- **F3 repaired:** lines `329-369` separate complete semantic text, additive SVG/legend bytes, and the authoritative whole-response ceiling. Density and ceiling fixtures measure the populations before and after fallback and reject truncated or success-shaped ceiling failures.

The OWNER HOLD, inert SVG boundary, complete visible text equivalent, no-JS/keyboard/focus/zoom/reflow/motion requirements, deterministic non-identity layout, literal-fence boundary, and ordered owner/specification/security/implementation gates remain sound.

## Commands and results

- Clean branch `agent/syzygy-dov.16.5`; exact HEAD `674cfaa4e81a022ecaadf742f027f874a0883276`.
- Change scope: one modified design candidate and one added purported raw-review file.
- `git diff HEAD^ HEAD --check`: passed.
- `python3 scripts/check_governance.py`: `32 OK, 20 WARN, 0 FAIL`.
- Final worktree status: clean.

## PR readiness

Not ready. Retain and route the actual Review 1 output verbatim, correct the false retention claim without overwriting the committed reconstruction, and obtain fresh exact-head confirmation. No implementation is authorized; all owner, requirement-mapping, authority, retention/security, and implementation gates remain.
