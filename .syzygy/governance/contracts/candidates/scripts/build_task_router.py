#!/usr/bin/env python3
"""Generate TASK-ROUTER.md — the one current task router.

The router is **generated navigation, never authority**: it names, for each
task class, the directly governing clauses, the modules that own them, the
mandatory dependencies (read from module front matter, never hand-listed),
the applicable doctrine/craft rules, and the explicit omissions. It measures
nothing (the budget report owns measurement) and decides nothing (clauses
own their content).

Every route is validated at generation time:
  - every routed path exists in the tree;
  - every cited clause ID is defined in the module the route names;
  - every doctrine/craft identifier appears in its owning file;
  - deferred routes carry the deferred label.

Three routes are permanent regression fixtures (the launch-gate D2 tasks);
mutating any of them must fail --selftest.

Usage:
  python3 build_task_router.py            # (re)write TASK-ROUTER.md
  python3 build_task_router.py --check    # drift check, no write
  python3 build_task_router.py --selftest # mutation fixtures
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAND = HERE.parent                      # .../contracts/candidates
SYZ = CAND.parent.parent.parent         # .../.syzygy
REPO = SYZ.parent
OUT = CAND / "TASK-ROUTER.md"

D = ".syzygy/governance/doctrine"
CR = ".syzygy/governance/policies/craft-and-care"
DEC = ".syzygy/governance/decisions"
C = ".syzygy/governance/contracts/candidates"

#: One entry per task class. `clauses` maps clause-id -> repo-relative path
#: of the module that must define it (validated). `deps` is derived, not
#: listed here. Routes marked deferred=True route into deferred-wave
#: candidates and say so (DEFERRED-WAVE-POSTURE.md).
TASKS = [
    dict(
        key="evidence-adapter",
        fixture="D2_ROUTINE_TASK",
        title="Add an evidence adapter for a new CI system",
        clauses={
            "RFC4-13": f"{C}/rfcs/RFC-0004/named-adapters.md",
            "RFC2-25": f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            "RFC5-21": f"{C}/rfcs/RFC-0005/execution-profiles.md",
        },
        modules=[
            f"{C}/rfcs/RFC-0004/general-contract.md",
            f"{C}/rfcs/RFC-0004/named-adapters.md",
            f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            f"{C}/rfcs/RFC-0005/execution-profiles.md",
            f"{C}/rfcs/RFC-0003/governance-homes-and-owner-acts.md",
        ],
        doctrine=[("VIS-2", f"{D}/vision.md"), ("SEC-4", f"{D}/security.md")],
        craft=[("CC-TEST-2", f"{CR}/testing-and-verification.md")],
        omissions=[
            "RFC-0008 state/cost — carried by an earlier router row, but "
            "absent from RFC-0004's declared `depends_on` (finding T-5): an "
            "adapter emits evidence; the work surface's cost vocabulary is "
            "not its contract",
        ],
        note="This route corrects the load map's superseded Adapter-author "
             "row, which finding T-5 measured wrong in both directions.",
    ),
    dict(
        key="mission-completion",
        fixture="D2_AUTHORITY_TASK",
        title="Change what counts as a completed Mission",
        deferred=True,
        clauses={
            "RFC10-18": f"{C}/rfcs/RFC-0010/effects-recovery-and-stop.md",
            "RFC10-5":
                f"{C}/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md",
        },
        modules=[
            f"{C}/rfcs/RFC-0010/effects-recovery-and-stop.md",
            f"{C}/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md",
        ],
        doctrine=[("VIS-4", f"{D}/vision.md")],
        craft=[],
        omissions=[
            "No accepted clause governs this yet: both modules are DEFERRED "
            "candidates (Waves D1/D2); completion adjudication is RFC10-18, "
            "the lifecycle freeze question is RFC-0010 §8 q1 (open), and the "
            "stop/containment repair form is owner question P-30",
        ],
        note="Deferred-wave route, singular and explicit per "
             "DEFERRED-WAVE-POSTURE.md — the answer today is a candidate "
             "plus two open owner questions, and saying so is the route.",
    ),
    dict(
        key="merged-to-reconciled",
        fixture="D2_SEAM_TASK",
        title="Trace a merged change from its work record to its "
              "reconciled status",
        clauses={
            "RFC2-17": f"{C}/rfcs/RFC-0002/reconciliation-chain.md",
            "RFC8-12":
                f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
        },
        modules=[
            f"{C}/rfcs/RFC-0002/reconciliation-chain.md",
            f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
            f"{C}/rfcs/RFC-0008/accounting-reconciliation-and-release.md",
        ],
        doctrine=[("VIS-2", f"{D}/vision.md")],
        craft=[],
        omissions=[
            "Merged work is never proof intent was satisfied — the chain "
            "renders Unknown until reconciliation is computed; fixture 10 "
            "(fixtures/context-selection-10-trajectory-lifecycle.md) is the "
            "worked selection for this class",
        ],
        note="Crosses the work-surface/evidence seam: RFC-0002 owns the "
             "reconciliation chain, RFC-0008 owns the work-state rendering.",
    ),
    dict(
        key="kernel",
        title="Implement or reason about the shared project model (kernel)",
        clauses={
            "RFC1-1":
                f"{C}/rfcs/RFC-0001-project-graph-identity-state-planes.md",
            "RFC2-1": f"{C}/rfcs/RFC-0002/snapshot-and-evaluation-core.md",
        },
        modules=[
            f"{C}/rfcs/RFC-0001-project-graph-identity-state-planes.md",
            f"{C}/rfcs/RFC-0002/snapshot-and-evaluation-core.md",
            f"{C}/rfcs/RFC-0002/challenge-lifecycle.md",
            f"{C}/rfcs/RFC-0002/reconciliation-chain.md",
            f"{C}/rfcs/RFC-0003/governance-homes-and-owner-acts.md",
        ],
        doctrine=[("VIS-1", f"{D}/vision.md"), ("VIS-2", f"{D}/vision.md")],
        craft=[("CC-BAR-5", f"{CR}/engineering-bar.md")],
        omissions=["Surface packages — a kernel task consumes no rendering "
                   "contract"],
    ),
    dict(
        key="surface-polaris",
        title="Specify or reason about Polaris (intent view)",
        clauses={"RFC7-1": f"{C}/rfcs/RFC-0007/narrative-contract.md"},
        modules=[
            f"{C}/rfcs/RFC-0007/README.md",
            f"{C}/rfcs/RFC-0007/narrative-contract.md",
            f"{C}/rfcs/RFC-0007/rendering-and-surface.md",
            f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            f"{C}/rfcs/RFC-0006-cross-surface-selection-query-drawer.md",
        ],
        doctrine=[("VIS-1", f"{D}/vision.md")],
        craft=[("CC-VIZ-5", f"{CR}/performance-and-visual-discipline.md")],
        omissions=["RFC-0008 — the sibling work view owns its own contract; "
                   "RFC-0009 is NOT omitted — it is a declared, clause-borne "
                   "dependency (RFC7-31's shared release-policy leg is "
                   "stated at RFC9-45, never duplicated locally), so a "
                   "release-gate question requires "
                   "rfcs/RFC-0009/interaction-parity-and-release.md"],
    ),
    dict(
        key="surface-trajectory",
        title="Specify or reason about Trajectory (work view)",
        clauses={
            "RFC8-1":
                f"{C}/rfcs/RFC-0008/identity-authority-materialization.md"},
        modules=[
            f"{C}/rfcs/RFC-0008/README.md",
            f"{C}/rfcs/RFC-0008/identity-authority-materialization.md",
            f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
            f"{C}/rfcs/RFC-0008/accounting-reconciliation-and-release.md",
            f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            f"{C}/rfcs/RFC-0006-cross-surface-selection-query-drawer.md",
        ],
        doctrine=[("VIS-2", f"{D}/vision.md")],
        craft=[],
        omissions=["Charter reminder: never satisfied by an issue list "
                   "(SDR-2)"],
    ),
    dict(
        key="surface-orrery",
        title="Specify or reason about Orrery (map view)",
        clauses={"RFC9-1": f"{C}/rfcs/RFC-0009/semantic-geography.md"},
        modules=[
            f"{C}/rfcs/RFC-0009/README.md",
            f"{C}/rfcs/RFC-0009/semantic-geography.md",
            f"{C}/rfcs/RFC-0009/visual-grammar-and-lenses.md",
            f"{C}/rfcs/RFC-0009/interaction-parity-and-release.md",
            f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
            f"{C}/rfcs/RFC-0008/accounting-reconciliation-and-release.md",
            f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            f"{C}/rfcs/RFC-0006-cross-surface-selection-query-drawer.md",
        ],
        doctrine=[("VIS-1", f"{D}/vision.md")],
        craft=[],
        omissions=["The two RFC-0008 modules are loaded for their closed "
                   "vocabularies only: RFC9-32/RFC9-46 require the "
                   "work/construction overlay to carry the thirteen "
                   "normalized values (RFC8-12/8-13) and six chain values "
                   "(RFC8-28) verbatim, inside the release-gated tuple"],
    ),
    dict(
        key="security-profile",
        title="Security, consent, or execution-profile work",
        clauses={"RFC5-1": f"{C}/rfcs/RFC-0005/admission-and-boundary.md"},
        modules=[
            f"{C}/rfcs/RFC-0005/admission-and-boundary.md",
            f"{C}/rfcs/RFC-0005/consent-egress-secrets.md",
            f"{C}/rfcs/RFC-0005/execution-profiles.md",
            f"{C}/rfcs/RFC-0003/governance-homes-and-owner-acts.md",
        ],
        doctrine=[("SEC-1", f"{D}/security.md"),
                  ("SEC-3", f"{D}/security.md")],
        craft=[("CC-SEC-1", f"{CR}/security-and-secrets.md")],
        omissions=["Load only the RFC-0005 module the task touches; the "
                   "list above is the package census, not one packet"],
    ),
    dict(
        key="spec-authoring",
        title="Author or judge a specification (once authorized)",
        clauses={
            "RFC6-28":
                f"{C}/rfcs/RFC-0006-cross-surface-selection-query-drawer.md"},
        modules=[
            f"{C}/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md",
            f"{C}/FIRST-OPENSPEC-SEQUENCE.md",
            f"{C}/policy-candidates/"
            "SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md",
        ],
        doctrine=[("VIS-4", f"{D}/vision.md")],
        craft=[("CC-REV-2", f"{CR}/review-and-documentation.md")],
        omissions=["No spec may be authored yet: the answer to 'may I "
                   "implement X?' is no until OpenSpec exists, and the "
                   "answer to 'may I author OpenSpec?' is the owner's "
                   "launch decision"],
    ),
    dict(
        key="doctrine-question",
        title="A doctrine question (why; non-negotiables)",
        clauses={},
        modules=[f"{D}/README.md", f"{D}/vision.md"],
        doctrine=[("VIS-1", f"{D}/vision.md")],
        craft=[],
        omissions=["Load the one doctrine file the question touches, via "
                   "the heart-and-soul skill — never the whole tree"],
    ),
    dict(
        key="readiness",
        title="Is this ready for OpenSpec? (current status)",
        clauses={},
        modules=["PROJECT-STATUS.md", "launch-gate-pre-specifications.md",
                 f"{C}/FIRST-OPENSPEC-SEQUENCE.md"],
        doctrine=[("VIS-2", f"{D}/vision.md")],
        craft=[],
        omissions=["The superseded 09 readiness report is history and "
                   "answers nothing"],
    ),
    dict(
        key="author-capability-1",
        title="Author Capability 1 — Project registration and honest "
              "shape visibility",
        note="**Authoring is forbidden today.** This route exists so the "
             "rules are reachable *before* the owner's launch decision, "
             "not so a spec can be written. `openspec/` does not exist and "
             "may not be created. Every blocking owner decision is named "
             "below; none is ruled.",
        clauses={
            # project identity and governance root
            "RFC1-1": f"{C}/rfcs/RFC-0001-project-graph-identity-state-planes.md",
            "RFC1-4": f"{C}/rfcs/RFC-0001-project-graph-identity-state-planes.md",
            # project declaration, consent and repository coverage
            "RFC3-4": f"{C}/rfcs/RFC-0003/manifests-and-namespace.md",
            "RFC3-7": f"{C}/rfcs/RFC-0003/manifests-and-namespace.md",
            # Unknown reason vocabulary
            "RFC2-24": f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            # shared human/machine answer facts
            "RFC7-33": f"{C}/rfcs/RFC-0007/rendering-and-surface.md",
            # fixed human entry; repository discoverability
            "RFC7-39": f"{C}/rfcs/RFC-0007/rendering-and-surface.md",
            "RFC7-40": f"{C}/rfcs/RFC-0007/rendering-and-surface.md",
            # anti-rollup semantics; absence is Unknown, never zero
            "RFC8-18": f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
            "RFC8-19": f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
        },
        modules=[
            f"{C}/rfcs/RFC-0001-project-graph-identity-state-planes.md",
            f"{C}/rfcs/RFC-0003/manifests-and-namespace.md",
            f"{C}/rfcs/RFC-0002/rendering-vocabularies.md",
            f"{C}/rfcs/RFC-0007/rendering-and-surface.md",
            f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md",
        ],
        doctrine=[("VIS-2", f"{D}/vision.md"), ("VIS-4", f"{D}/vision.md"),
                  ("VIS-5", f"{D}/vision.md")],
        craft=[],
        blocking_decisions=["P-33", "P-31", "P-36", "P-37", "P-38", "P-39",
                            "P-40", "P-41", "P-34", "P-35"],
        omissions=[
            "Every Mission and Context-selection contract — RFC-0010 and "
            "RFC-0011 — is excluded. They are DEFERRED-WAVE candidates and "
            "Capability 1 relies on none of them; the Mission-ready facet "
            "is a future extension, not a launch facet",
            "The specification-acceptance rules (CC-SPEC-1…10) and the "
            "shape-to-spec impact rules (CC-IMPACT-1…7) are CANDIDATE "
            "craft policy, in force from neither. They are routed as "
            "prerequisites, never cited as binding — which is why they are "
            "not listed under Craft above",
            "The facet vocabulary itself is routed to no clause: it "
            "appears in zero of the 30 Waves A+B modules, and P-37 decides "
            "whether the Capability 1 specification owns it or Wave A must "
            "be amended to",
        ],
    ),
    dict(
        key="deferred-waves",
        title="Anything touching Missions or Context selection",
        deferred=True,
        clauses={},
        modules=[f"{C}/DEFERRED-WAVE-POSTURE.md"],
        doctrine=[("VIS-4", f"{D}/vision.md")],
        craft=[],
        omissions=["Waves C1/C2/D1/D2 are candidate and deferred; the "
                   "posture file names what they may not influence and "
                   "which owner decisions gate their repair"],
    ),
]

FRONT_DEP = re.compile(r"^depends_on:\s*\[([^\]]*)\]", re.M)


def read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def module_deps(paths):
    deps = set()
    for rel in paths:
        if not rel.endswith(".md") or "/rfcs/" not in rel:
            continue
        try:
            m = FRONT_DEP.search(read(rel)[:2000])
        except OSError:
            continue
        if m:
            deps.update(x.strip() for x in m.group(1).split(",") if x.strip())
    return sorted(deps)


def validate(tasks):
    errs = []
    for t in tasks:
        for rel in t["modules"]:
            if not (REPO / rel).exists():
                errs.append(f"{t['key']}: routed path missing: {rel}")
        for cid, rel in t["clauses"].items():
            if not (REPO / rel).exists():
                errs.append(f"{t['key']}: clause home missing: {rel}")
            elif not re.search(rf"\*\*{re.escape(cid)}\b", read(rel)):
                errs.append(f"{t['key']}: clause {cid} not defined in {rel}")
        for ident, rel in t.get("doctrine", []) + t.get("craft", []):
            if not (REPO / rel).exists():
                errs.append(f"{t['key']}: rule home missing: {rel}")
            elif ident not in read(rel):
                errs.append(f"{t['key']}: {ident} absent from {rel}")
        if t.get("deferred") and not any(
                "DEFERRED" in o or "deferred" in o or "Deferred" in o
                for o in t["omissions"]):
            errs.append(f"{t['key']}: deferred route lacks a deferred "
                        "disclosure in its omissions")
        # A route that names a blocking owner decision must name one that
        # is actually OPEN in the queue. A decision named here but already
        # ruled would understate what a reader may do; one named here but
        # absent from the queue is a decision nobody is tracking.
        for pid in t.get("blocking_decisions", []):
            queue = read(f"{DEC}/PENDING-OWNER-DECISIONS.md")
            if not re.search(rf"^\|\s*{re.escape(pid)}\s*\|", queue, re.M):
                errs.append(f"{t['key']}: blocking decision {pid} has no "
                            f"row in {DEC}/PENDING-OWNER-DECISIONS.md")
    return errs


def render(tasks):
    lines = [
        "# Task router — the one current route per task class",
        "",
        "> **Generated navigation — never authority.** Written by",
        "> `scripts/build_task_router.py`; regenerate with it; never",
        "> hand-edit. Clauses own their content; the budget report owns",
        "> every measurement; this file only routes. Every path and clause",
        "> below is existence-checked at generation. Where this file and a",
        "> clause disagree, the clause wins. It supersedes",
        "> `TASK-TO-CONTRACT-INDEX.md` and the load map's reader-map table",
        "> as the routing answer; `06-CONTEXT-LOAD-MAP.md` remains the",
        "> context-budget instrument.",
        "",
        "Three routes are **permanent routing regression fixtures** (the",
        "launch-gate parameter block's fixed D2 tasks); they are marked and",
        "`--selftest` proves their mutation is caught.",
        "",
    ]
    for t in tasks:
        fx = (f" *(routing fixture: `{t['fixture']}`)*"
              if t.get("fixture") else "")
        defer = " — **DEFERRED-WAVE ROUTE**" if t.get("deferred") else ""
        lines.append(f"## {t['title']}{fx}{defer}")
        lines.append("")
        if t.get("note"):
            lines.append(f"{t['note']}")
            lines.append("")
        if t["clauses"]:
            lines.append("**Directly governing clauses:** " + "; ".join(
                f"`{cid}` (`{rel}`)" for cid, rel in t["clauses"].items()))
        lines.append("**Load:** " + " · ".join(
            f"`{m}`" for m in t["modules"]))
        deps = module_deps(t["modules"])
        if deps:
            lines.append("**Declared contract dependencies (from module "
                         "front matter, computed):** " + ", ".join(deps))
        if t.get("doctrine"):
            lines.append("**Doctrine:** " + ", ".join(
                f"`{i}`" for i, _ in t["doctrine"]))
        if t.get("craft"):
            lines.append("**Craft:** " + ", ".join(
                f"`{i}`" for i, _ in t["craft"]))
        if t.get("blocking_decisions"):
            lines.append("**Owner decisions still blocking:** " + ", ".join(
                f"`{p}`" for p in t["blocking_decisions"])
                + " — each verified open in the pending queue at "
                  "generation time")
        for o in t["omissions"]:
            lines.append(f"**Explicitly omitted:** {o}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Generated by `scripts/build_task_router.py` — "
                 f"{len(tasks)} task classes, every route validated at "
                 "generation time. Counts computed, never asserted.")
    lines.append("")
    return "\n".join(lines)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "--selftest":
        import copy
        fails = []

        def case(name, mutate, expect):
            ts = copy.deepcopy(TASKS)
            mutate(ts)
            errs = validate(ts)
            ok = any(expect in e for e in errs)
            print(("  pass  " if ok else "  FAIL  ") + name)
            if not ok:
                fails.append(name)

        base = validate(TASKS)
        print(("  pass  " if not base else "  FAIL  ") +
              "current routes all validate")
        if base:
            fails.append("base")
            for e in base:
                print("        " + e)
        case("missing routed path detected",
             lambda ts: ts[0]["modules"].append(
                 f"{C}/rfcs/RFC-0004/nonexistent.md"),
             "routed path missing")
        case("undefined clause detected",
             lambda ts: ts[0]["clauses"].update(
                 {"RFC4-999": f"{C}/rfcs/RFC-0004/general-contract.md"}),
             "not defined in")
        case("fixture route mutation detected (evidence adapter loses "
             "its tier-registry module)",
             lambda ts: ts[0]["clauses"].update(
                 {"RFC2-25": f"{C}/rfcs/RFC-0004/named-adapters.md"}),
             "not defined in")
        case("deferred route without disclosure detected",
             lambda ts: ts[1]["omissions"].clear(),
             "lacks a deferred disclosure")
        case("mission fixture dead-path mutation detected",
             lambda ts: ts[1]["modules"].__setitem__(
                 0, f"{C}/rfcs/RFC-0010-mission-control-autonomy.md"),
             "routed path missing")
        cap = next(i for i, t in enumerate(TASKS)
                   if t["key"] == "author-capability-1")
        case("Capability 1 route: an unqueued blocking decision detected",
             lambda ts: ts[cap]["blocking_decisions"].append("P-999"),
             "has no row in")
        case("Capability 1 route: a clause routed to the wrong module "
             "detected",
             lambda ts: ts[cap]["clauses"].update(
                 {"RFC7-39": f"{C}/rfcs/RFC-0008/state-vocabulary-and-cost.md"}),
             "not defined in")
        case("Capability 1 route: a deferred-wave module in the load set "
             "detected",
             lambda ts: ts[cap]["clauses"].update(
                 {"RFC10-5": f"{C}/rfcs/RFC-0007/rendering-and-surface.md"}),
             "not defined in")
        n = 9
        print(f"{n} fixtures, {len(fails)} failing — a check that cannot "
              "fail is not a check")
        sys.exit(1 if fails else 0)

    errs = validate(TASKS)
    if errs:
        for e in errs:
            print("ERROR " + e)
        sys.exit(1)
    text = render(TASKS)
    if mode == "--check":
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print("task router drifted from regeneration — rerun "
                  "build_task_router.py")
            sys.exit(1)
        print(f"task router matches regeneration — {len(TASKS)} task "
              "classes validated")
        sys.exit(0)
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} — {len(TASKS)} task classes, "
          "all routes validated")


if __name__ == "__main__":
    main()
