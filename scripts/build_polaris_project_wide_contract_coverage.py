#!/usr/bin/env python3
"""Generate the Polaris project-wide CC-SPEC-8 coverage matrix.

The accepted RFC 0001-0009 clause denominator comes from the generated
contract index. Mapped clauses come only from the requirement warrants.
Author-judged applicable-but-uncovered clauses are explicit below; every
remaining clause is printed individually as believed not applicable.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_capability_1_spec_dependencies as base
import build_polaris_project_wide_spec_dependencies as dependencies

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
INDEX = os.path.join(
    ROOT, ".syzygy", "governance", "contracts", "candidates", "05-CONTRACT-INDEX.yaml"
)
OUT = os.path.join(
    ROOT,
    "openspec",
    "changes",
    "polaris-project-wide-butlers-model",
    "CONTRACT-COVERAGE.md",
)

INDEX_RE = re.compile(r"^\s+- \{id: (RFC[1-9]-\d+(?:\([a-z]\))?),", re.M)

APPLICABLE_UNCOVERED = {
    "RFC1-3": "The external Butlers repository remains read-only, but this additive spec has no write-surface oracle.",
    "RFC1-6": "Git revisions identify observations; no requirement proves they are never reified as project entities.",
    "RFC1-17": "Multi-capability mapping deduplication becomes relevant to a complete catalog but is not specified here.",
    "RFC1-33": "The RFC-to-spec phase rule is discharged structurally by this candidate and matrix, not a runtime oracle.",
    "RFC5-1": "The inherited human and machine routes bind principals, but this change does not respecify admission.",
    "RFC5-2": "Browser sessions and machine credentials are inherited unchanged from the signed POC runtime.",
    "RFC5-3": "Client-class classification is inherited unchanged from the signed POC runtime.",
    "RFC5-4": "Browser session, Origin, CSRF and DNS-rebinding duties remain inherited parent-POC Unknowns.",
    "RFC5-5": "Machine-client authentication is inherited unchanged from the signed POC runtime.",
    "RFC5-6": "Credential lifecycle behavior is outside this additive project-modeling delta.",
    "RFC5-7": "The concrete bearer mechanism is inherited and not evaluated by a new requirement.",
    "RFC5-8": "Tailnet exposure-mode behavior is inherited and not evaluated by a new requirement.",
    "RFC5-9": "Tailnet transport and device restrictions are inherited and not evaluated by a new requirement.",
    "RFC5-10": "Loopback-by-default behavior is inherited and not evaluated by a new requirement.",
    "RFC5-12": "Observation consent applies to the enlarged content scope; no new runtime consent requirement is introduced.",
    "RFC5-24": "Adapter credential handling is inherited; whether project-shape reads require credentials is unresolved.",
    "RFC5-25": "Admission audit records remain an inherited runtime concern, not covered by this delta.",
    "RFC5-26": "Credential/session revocation remains an inherited runtime concern, not covered by this delta.",
    "RFC6-28": "The cross-surface phase rule is discharged structurally by this candidate and matrix, not a runtime oracle.",
    "RFC7-12": "Exact source text is reachable, but normative-vs-adjudicative restatement discipline lacks a dedicated oracle.",
    "RFC7-38": "The Polaris phase rule is discharged structurally by this candidate and matrix, not a runtime oracle.",
    "RFC7-39": "The POC uses an application route rather than the governed fixed `.syzygy/intent/OVERVIEW.md` entry.",
    "RFC7-40": "Butlers repository-front-door discoverability is not changed by this candidate.",
    "RFC9-15": "The existing Orrery's cross-revision coordinate stability remains outside this Polaris-only change.",
    "RFC9-26": "The shared visual-channel registry remains an inherited POC concern, not a project-modeling requirement.",
}

FAMILY_REASONS = {
    1: "The clause governs a graph entity, lifecycle or relation this additive Polaris capability does not render, store, transition or query.",
    2: "The clause governs inference, challenge, multi-evaluation history or evidence state outside this revision-bound project account.",
    3: "The clause governs governance storage, workspace/project composition or write authority not crossed by this one-project read-only model.",
    4: "The clause governs an external adapter, execution record, work join or mapping behavior not used by the project-shape observer.",
    5: "The clause governs egress or observed-code execution not performed by this local read-only capability.",
    6: "The clause governs selection, URL, drawer or scenario-context behavior not introduced by this project-level reading.",
    7: "The clause governs narrative authoring, draft adoption, portfolio or subproject behavior excluded from this runtime POC addition.",
    8: "The clause governs Trajectory work, accounting, cost or reconciliation behavior unchanged by this Polaris-only addition.",
    9: "The clause governs Orrery geography, lenses, scenes or map release behavior unchanged by this Polaris-only addition.",
}


def natural_key(identifier):
    return base.natkey(identifier)


def clause_family(identifier):
    return int(identifier[3])


def inputs():
    index_text = base.read(INDEX)
    population = INDEX_RE.findall(index_text)
    if len(population) != 324 or len(set(population)) != 324:
        raise ValueError(
            f"accepted clause population must be 324 unique identifiers, got {len(population)}/{len(set(population))}"
        )
    requirements, errors = dependencies.parse(base.read(dependencies.SPEC))
    if errors:
        raise ValueError("spec warrants do not validate: " + " | ".join(errors))
    mapped_by_clause = {}
    for requirement_id, warrants in requirements:
        for clause in warrants["contracts"]:
            mapped_by_clause.setdefault(clause, []).append(requirement_id)
    unknown = set(mapped_by_clause) - set(population)
    if unknown:
        raise ValueError(f"mapped clauses absent from accepted index: {sorted(unknown)}")
    overlap = set(mapped_by_clause) & set(APPLICABLE_UNCOVERED)
    if overlap:
        raise ValueError(f"mapped/uncovered overlap: {sorted(overlap)}")
    explicitly_unaffected = set(population) - set(mapped_by_clause) - set(APPLICABLE_UNCOVERED)
    if len(mapped_by_clause) + len(APPLICABLE_UNCOVERED) + len(explicitly_unaffected) != 324:
        raise ValueError("coverage partition does not reconcile")
    return population, requirements, mapped_by_clause, explicitly_unaffected


def render():
    population, requirements, mapped, unaffected = inputs()
    lines = [
        "# Contract coverage — polaris-project-wide-butlers-model",
        "",
        "> **Candidate.** CC-SPEC-8 matrix for the additive project-wide Polaris capability.",
        "> Clause text remains authoritative; row labels are mapping judgments only.",
        "> No N/A is minted here. Part B2 is the author's believed-not-applicable set",
        "> offered for review; Part B1 remains Unknown pending owner-reviewed N/A or a requirement.",
        "",
        "## Population",
        "",
        f"Accepted RFC 0001-0009 clauses: **{len(population)}**. Mapped: **{len(mapped)}**. "
        f"Applicable but uncovered: **{len(APPLICABLE_UNCOVERED)}**. "
        f"Believed not applicable: **{len(unaffected)}**.",
        "",
        "The three sets are disjoint and generated from `05-CONTRACT-INDEX.yaml`; their totals reconcile to 324.",
        "",
        "## Part A — mapped",
        "",
        "| Clause | Requirements | Observable consequence checked |",
        "|---|---|---|",
    ]
    for clause in sorted(mapped, key=natural_key):
        requirement_ids = ", ".join(sorted(set(mapped[clause]), key=natural_key))
        lines.append(
            f"| {clause} | {requirement_ids} | The named requirements' case, observable, independent oracle and falsifier cover the consequence this capability uses. |"
        )
    lines.extend(
        [
            "",
            "### Part A disclosed partial limbs",
            "",
            "| Clause | Uncovered consequence | Disposition |",
            "|---|---|---|",
            "| RFC4-7 | Owner-act provenance for a production adapter-registry entry | Unknown; the bounded POC manifest is specified, but no registry act is minted here. |",
            "| RFC7-5 | Governed `.syzygy/intent/**` residence and presentation-profile adoption | Unknown; the external-project POC renders an application route. |",
            "| RFC7-33 | Explicit `non-citable` / `presentation-artifact` attributes on every rendering | Unknown; parity is covered, these attributes are not. |",
            "",
            "## Part B1 — applicable, uncovered",
            "",
            "| Clause | Why applicable | Disposition |",
            "|---|---|---|",
        ]
    )
    for clause in sorted(APPLICABLE_UNCOVERED, key=natural_key):
        lines.append(f"| {clause} | {APPLICABLE_UNCOVERED[clause]} | Unknown pending owner-reviewed N/A or added coverage. |")
    lines.extend(
        [
            "",
            "## Part B2 — believed not applicable",
            "",
            "| Clause | Author's reason and method |",
            "|---|---|",
        ]
    )
    for clause in sorted(unaffected, key=natural_key):
        lines.append(f"| {clause} | {FAMILY_REASONS[clause_family(clause)]} Method: clause-by-clause identity sweep against proposal scope and requirement warrants. |")
    lines.extend(
        [
            "",
            "## Verification",
            "",
            "```sh",
            "python3 scripts/build_polaris_project_wide_spec_dependencies.py --check",
            "python3 scripts/build_polaris_project_wide_contract_coverage.py --check",
            "python3 scripts/build_polaris_project_wide_contract_coverage.py --selftest",
            "```",
            "",
            "A fresh reviewer must confirm the mapped consequences, the Part B1 gaps and every Part B2 applicability judgment before sign-off.",
            "",
        ]
    )
    return "\n".join(lines)


def selftest():
    try:
        output = render()
    except ValueError as error:
        print(f"SELFTEST FAILED: {error}")
        return 1
    if "Accepted RFC 0001-0009 clauses: **324**" not in output:
        print("SELFTEST FAILED: denominator missing")
        return 1
    saved = APPLICABLE_UNCOVERED["RFC1-3"]
    try:
        APPLICABLE_UNCOVERED["RFC1-3"] = saved
        APPLICABLE_UNCOVERED["RFC1-5"] = "mutation"
        try:
            inputs()
        except ValueError as error:
            if "overlap" not in str(error):
                print(f"SELFTEST FAILED: wrong overlap error: {error}")
                return 1
        else:
            print("SELFTEST FAILED: mapped/uncovered overlap passed")
            return 1
    finally:
        APPLICABLE_UNCOVERED.pop("RFC1-5", None)
    if output != render():
        print("SELFTEST FAILED: generation is not deterministic")
        return 1
    print("selftest: denominator, disjoint partition mutation and determinism hold")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    output = render()
    if "--check" in argv:
        if not os.path.exists(OUT) or base.read(OUT) != output:
            print("DRIFT: CONTRACT-COVERAGE.md differs from regeneration")
            return 1
        print("Polaris contract coverage matches regeneration — 324 clauses")
        return 0
    with open(OUT, "w", encoding="utf-8") as file_handle:
        file_handle.write(output)
    print("wrote CONTRACT-COVERAGE.md — 324 clauses")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
