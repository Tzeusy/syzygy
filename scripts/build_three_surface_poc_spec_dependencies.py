#!/usr/bin/env python3
"""Generate the three-surface-poc-experience spec-level dependency
declaration (CC-IMPACT-1).

Same contract as build_capability_1_spec_dependencies.py, pointed at the
candidate POC change: the specification-level declaration is the
GENERATED union of every requirement's fenced ``warrants`` YAML block —
one machine-readable home, no second hand-maintained list.

    build_three_surface_poc_spec_dependencies.py            write the union file
    build_three_surface_poc_spec_dependencies.py --check    fail on drift, write nothing
    build_three_surface_poc_spec_dependencies.py --selftest mutation fixtures

Identifiers only — no clause prose. Totals are computed, never
transcribed (verification rule 3).
"""

import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_capability_1_spec_dependencies as base

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CHANGE = os.path.join(ROOT, "openspec", "changes", "three-surface-poc-experience")
SPEC = os.path.join(CHANGE, "specs", "three-surface-poc-experience", "spec.md")
OUT = os.path.join(CHANGE, "GOVERNING-DEPENDENCIES.md")

REQ_RE = re.compile(r"^### Requirement: (POC-REQ-\d{3}) — ", re.M)
TITLE = "three-surface-poc-experience"


def parse(spec_text):
    saved = base.REQ_RE
    base.REQ_RE = REQ_RE
    try:
        return base.parse(spec_text)
    finally:
        base.REQ_RE = saved


def render(reqs, spec_digest):
    out = base.render(reqs, spec_digest)
    out = out.replace(
        "# Governing dependencies — project-registration-and-honest-shape-visibility",
        f"# Governing dependencies — {TITLE}")
    out = out.replace("the CC-IMPACT-1", "the candidate change's CC-IMPACT-1")
    out = out.replace("build_capability_1_spec_dependencies.py",
                      "build_three_surface_poc_spec_dependencies.py")
    return out


def generate(spec_text):
    reqs, errors = parse(spec_text)
    if errors:
        return None, errors
    digest = hashlib.sha256(spec_text.encode()).hexdigest()
    return render(reqs, digest), []


def main(argv):
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv

    spec_text = base.read(SPEC)
    out, errors = generate(spec_text)
    if errors:
        print("SPEC WARRANTS DO NOT VALIDATE — no declaration was generated:")
        for e in errors:
            print(f"  {e}")
        return 1

    reqs, _ = parse(spec_text)
    n_auth = out.split(" distinct authorities")[0].rsplit(" ", 1)[-1]
    if check:
        if not os.path.exists(OUT) or base.read(OUT) != out:
            print("DRIFT: GOVERNING-DEPENDENCIES.md differs from regeneration")
            return 1
        print(f"three-surface POC spec dependencies match regeneration — "
              f"{len(reqs)} requirement(s), {n_auth} distinct authorities")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"wrote GOVERNING-DEPENDENCIES.md — {len(reqs)} requirement(s), "
          f"{n_auth} distinct authorities")
    return 0


GOOD = base.GOOD.replace("CAP1-REQ-", "POC-REQ-")


def selftest():
    """Mutation fixtures over the POC-adapted parser (verification rule 6)."""
    failures = []

    def expect_ok(name, text):
        out, errors = generate(text)
        if errors or out is None:
            failures.append(f"{name}: expected clean, got {errors}")

    def expect_fail(name, text, needle):
        _, errors = generate(text)
        if not errors:
            failures.append(f"{name}: mutation passed the check")
        elif needle not in " | ".join(errors):
            failures.append(f"{name}: failed for the wrong reason: {errors}")

    expect_ok("well-formed", GOOD)
    expect_fail("duplicate-id",
                GOOD.replace("POC-REQ-002 — Beta", "POC-REQ-001 — Beta", 1),
                "duplicate requirement identifier")
    expect_fail("cap1-headers-rejected", base.GOOD,
                "no `### Requirement:")
    expect_fail("phantom-parent",
                GOOD.replace("parent_requirements: [POC-REQ-001]",
                             "parent_requirements: [POC-REQ-099]", 1),
                "does not exist in this specification")
    expect_fail("no-headers", "no requirements here\n",
                "no `### Requirement:")

    out, _ = generate(GOOD)
    out2, _ = generate(GOOD)
    if out != out2:
        failures.append("determinism: two runs differ")
    if "three-surface-poc-experience" not in (out or ""):
        failures.append("rendering: POC title missing from output")

    n_cases = 7
    if failures:
        print(f"SELFTEST FAILED ({len(failures)}/{n_cases}):")
        for f in failures:
            print(f"  {f}")
        return 1
    print(f"selftest: {n_cases}/{n_cases} fixtures behave "
          f"(1 clean, 4 mutations rejected, determinism + title hold)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
