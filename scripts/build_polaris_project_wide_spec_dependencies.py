#!/usr/bin/env python3
"""Generate the Polaris project-wide spec dependency declaration.

The output is the CC-IMPACT-1 union of the requirement-level ``warrants``
blocks. Qualified parent requirements are resolved against another OpenSpec
change because this additive capability builds on the signed POC requirements.
"""

import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_capability_1_spec_dependencies as base

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CHANGE_NAME = "polaris-project-wide-butlers-model"
CHANGE = os.path.join(ROOT, "openspec", "changes", CHANGE_NAME)
SPEC = os.path.join(CHANGE, "specs", CHANGE_NAME, "spec.md")
OUT = os.path.join(CHANGE, "GOVERNING-DEPENDENCIES.md")

REQ_RE = re.compile(r"^### Requirement: (PWB-REQ-\d{3}) — ", re.M)
QUALIFIED_PARENT_RE = re.compile(r"^([a-z0-9-]+)/([A-Z0-9-]+-REQ-\d{3})$")


def _parent_exists(parent):
    match = QUALIFIED_PARENT_RE.fullmatch(parent)
    if match is None:
        return False
    change_name, requirement_id = match.groups()
    change_dir = os.path.join(ROOT, "openspec", "changes", change_name, "specs")
    if not os.path.isdir(change_dir):
        return False
    heading = re.compile(
        rf"^### Requirement: {re.escape(requirement_id)}(?:\s+—|\s*$)", re.M
    )
    for current_root, _dirs, files in os.walk(change_dir):
        for name in files:
            if name != "spec.md":
                continue
            path = os.path.join(current_root, name)
            if heading.search(base.read(path)):
                return True
    return False


def parse(spec_text):
    saved = base.REQ_RE
    base.REQ_RE = REQ_RE
    try:
        requirements, errors = base.parse(spec_text)
    finally:
        base.REQ_RE = saved

    qualified = {
        parent
        for _requirement_id, warrants in requirements
        for parent in warrants["parent_requirements"]
        if "/" in parent
    }
    ignored = {
        f"{requirement_id}: parent requirement {parent} does not exist in this specification"
        for requirement_id, warrants in requirements
        for parent in warrants["parent_requirements"]
        if parent in qualified
    }
    errors = [error for error in errors if error not in ignored]
    for parent in sorted(qualified, key=base.natkey):
        if not _parent_exists(parent):
            errors.append(f"qualified parent requirement does not resolve: {parent}")
    return requirements, errors


def render(requirements, spec_digest):
    output = base.render(requirements, spec_digest)
    output = output.replace(
        "# Governing dependencies — project-registration-and-honest-shape-visibility",
        f"# Governing dependencies — {CHANGE_NAME}",
    )
    output = output.replace(
        "build_capability_1_spec_dependencies.py",
        "build_polaris_project_wide_spec_dependencies.py",
    )
    return output


def generate(spec_text):
    requirements, errors = parse(spec_text)
    if errors:
        return None, errors
    digest = hashlib.sha256(spec_text.encode()).hexdigest()
    return render(requirements, digest), []


def selftest():
    good = """\
### Requirement: PWB-REQ-001 — Alpha

body

```yaml
warrants:
  primary: VIS-1
  doctrine: [VIS-1]
  contracts: []
  policies: []
  decisions: []
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-030]
```
"""
    output, errors = generate(good)
    if errors or output is None:
        print(f"SELFTEST FAILED: qualified parent rejected: {errors}")
        return 1
    mutated = good.replace("POC-REQ-030", "POC-REQ-999")
    _output, errors = generate(mutated)
    if not errors or "does not resolve" not in " | ".join(errors):
        print(f"SELFTEST FAILED: missing qualified parent passed: {errors}")
        return 1
    output2, errors2 = generate(good)
    if errors2 or output != output2:
        print("SELFTEST FAILED: generation is not deterministic")
        return 1
    print("selftest: qualified-parent success/failure and determinism hold")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv
    spec_text = base.read(SPEC)
    output, errors = generate(spec_text)
    if errors:
        print("SPEC WARRANTS DO NOT VALIDATE — no declaration was generated:")
        for error in errors:
            print(f"  {error}")
        return 1
    requirements, _errors = parse(spec_text)
    if check:
        if not os.path.exists(OUT) or base.read(OUT) != output:
            print("DRIFT: GOVERNING-DEPENDENCIES.md differs from regeneration")
            return 1
        print(f"Polaris dependencies match regeneration — {len(requirements)} requirement(s)")
        return 0
    with open(OUT, "w", encoding="utf-8") as file_handle:
        file_handle.write(output)
    print(f"wrote GOVERNING-DEPENDENCIES.md — {len(requirements)} requirement(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
