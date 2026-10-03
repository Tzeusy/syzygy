#!/usr/bin/env python3
"""Perform the install change that follows the Redis sitting's act records.

Candidate tooling. It performs no owner act and writes no act record; it makes
the repository's checks agree with acts the recorders have already written.
`scripts/simulate_redis_sitting.py` runs it in a scratch clone and requires the
end state to be green; the runbook (`docs/polaris-generation/REDIS-SITTING-RUNBOOK.md`)
lists each step with the finding it answers.

Run from the repository root after every recorder has run:

  python3 scripts/install_redis_sitting.py            # install
  python3 scripts/install_redis_sitting.py --check    # report what is not installed
  python3 scripts/install_redis_sitting.py --selftest

It refuses (exit 2, nothing written) unless every required act record exists.
It is idempotent: a second run changes nothing and says so. Each step asserts
that the text it patches carries its anchor exactly once, so a drifted
`check_governance.py` fails loudly instead of being patched in the wrong place.

Steps (finding numbers are the runbook's):

  registrations   F5   performed admission and registry records become registered
                       act-copy files; their `manifest SHA-256:` heading is a
                       checked exemption
  rfc5            F6   the RFC-0005 patch applies to both mirrors; the active
                       manifest row and the directive register are regenerated;
                       the amendment becomes a row-argument contract chain link
  policy          F4,F10  the screening-scope act becomes the policy's chain link (the
                       2026-10-02 re-pin turns to history); the read gate, its
                       tests and the status battery and workflow follow it
  profile         F8,F11  the narrative-profile spec moves from proposed/ to
                       specs/; package prose naming the old path is rewritten;
                       the status page figure follows the recount tool
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECISIONS = ".syzygy/governance/decisions"
CAND = ".syzygy/governance/contracts/candidates"
CG = "scripts/check_governance.py"

#: Act records every sitting must have produced before this runs. The provider
#: route is one of two substitutes (RFC4-1): exactly one of ROUTE_A and ROUTE_B.
REQUIRED_RECORDS = (
    f"{DECISIONS}/PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md",
    f"{DECISIONS}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md",
    f"{DECISIONS}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md",
    f"{DECISIONS}/PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-ACT.md",
    f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md",
    f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md",
    f"{DECISIONS}/POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md",
)
ROUTE_A = ("PUBLIC_REGISTRY_ACTS[0][0]", "PUBLIC-ADMISSION-REGISTRY-PROVIDER-ROUTE-ACT.md", "PUBLIC_REGISTRY_MANIFEST")
ROUTE_B = ("MESSAGES_API_ACTS[0][0]", "PUBLIC-ADMISSION-REGISTRY-MESSAGES-API-ROUTE-ACT.md", "MESSAGES_API_MANIFEST")

#: (label expression, record file, manifest constant) for the records that become
#: registered act-copy files; the provider route is added by `performed()`.
PERFORMED_COMMON = (
    ("PUBLIC_ADMISSION_ACTS[0][0]", "PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md", "PUBLIC_ADMISSION_MANIFEST"),
    ("PUBLIC_ADMISSION_ACTS[1][0]", "PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md", "PUBLIC_ADMISSION_MANIFEST"),
    ("PUBLIC_ADMISSION_ACTS[2][0]", "PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md", "PUBLIC_ADMISSION_MANIFEST"),
    ("PUBLIC_REGISTRY_ACTS[1][0]", "PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-ACT.md", "PUBLIC_REGISTRY_MANIFEST"),
)


def provider_routes(root: pathlib.Path) -> list[tuple[str, str, str]]:
    return [r for r in (ROUTE_A, ROUTE_B) if (root / DECISIONS / r[1]).is_file()]


def performed(root: pathlib.Path) -> tuple[tuple[str, str, str], ...]:
    routes = provider_routes(root)
    if len(routes) != 1:
        raise Refusal(f"exactly one provider route record must exist (the two routes are substitutes, "
                      f"RFC4-1); found {[r[1] for r in routes]}")
    return PERFORMED_COMMON + (routes[0],)


RFC5_PKG = f"{CAND}/rfc5-project-documentation-class"
RFC5_MODULE = "rfcs/RFC-0005/consent-egress-secrets.md"
RFC5_ACT = f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md"
SCOPE_PKG = f"{CAND}/public-source-screening-scope"
SCOPE_MANIFEST = f"{SCOPE_PKG}/PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt"
SCOPE_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md"
REPIN_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md"
AMENDMENT_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md"
POLICY_JSON = ".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"
WORKFLOW = ".github/workflows/governance-docs.yml"
INPUTS_TS = "apps/three-surface-poc/src/governance-inputs.ts"
INPUTS_TEST = "apps/three-surface-poc/src/governance-inputs.test.ts"
PIN_FILES = (INPUTS_TS, INPUTS_TEST,
             "packages/three-surface-poc-core/src/git-object-reader.ts",
             "packages/three-surface-poc-core/src/content-classification.test.ts",
             "packages/three-surface-poc-core/src/project-shape-model.test.ts")
PROFILE_CHANGE = "openspec/changes/polaris-non-governed-narrative-profile"
PROFILE_PKG = f"{CAND}/non-governed-narrative-profile"
STATUS = "PROJECT-STATUS.md"

# ---- text of the check_governance.py insertions ----------------------------

REGISTRATIONS_MARK = "_activate_public_admission_performed_registries"
REGISTRATIONS_ANCHOR = "_activate_public_admission_manifest_copy_registry()\n"
EXEMPTION_DICT = "BARE_DIGEST_HEADING_MANIFEST_EXEMPTIONS = {"


def registrations_code(perf) -> str:
    lines = ["", "",
             f"def {REGISTRATIONS_MARK}():",
             '    """Install change: each performed admission or registry record is an act-copy file."""',
             '    aggregate = f"{DECISIONS}/ACCEPTANCE-ACT-RECORD.md"',
             "    for label, rel in ("]
    for label, record, _manifest in perf:
        lines.append(f'            ({label}, f"{{DECISIONS}}/{record}"),')
    lines += ["    ):",
              "        if not os.path.isfile(os.path.join(ROOT, rel)):",
              "            continue",
              "        labels = ACT_DIGEST_COPY_FILES.get(aggregate, ())",
              "        if label not in labels:",
              "            ACT_DIGEST_COPY_FILES[aggregate] = labels + (label,)",
              "        ACT_DIGEST_COPY_FILES[rel] = (label,)",
              "", "", f"{REGISTRATIONS_MARK}()", ""]
    return "\n".join(lines)


def exemptions_code(perf) -> str:
    return "".join(f'    (f"{{DECISIONS}}/{record}", "manifest"): {manifest},\n'
                   for _l, record, manifest in perf)


CHAIN_MARK = "RFC5_CLASS_LABEL"
CHAIN_CONSTANTS = '''#: The RFC5-14 project-documentation amendment (one module). Its act takes the
#: SHA-256 of the patched module, which is the manifest's one row, not the
#: manifest file's digest, so the link is a row-argument link
#: (`ROW_ARGUMENT_LINK_LABELS`): CG-7h reads the argument from the row.
RFC5_CLASS_LABEL = "AMEND RFC5-14 WITH THE PROJECT-DOCUMENTATION CONTENT CLASS"
RFC5_CLASS_DIR = f"{CANDIDATES}/rfc5-project-documentation-class"
RFC5_CLASS_SUBJECT = f"{RFC5_CLASS_DIR}/CONTRACT-AMENDMENT-MANIFEST.txt"
RFC5_CLASS_ACT = f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md"
RFC5_CLASS_MODULE = ".syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md"
RFC5_CLASS_PATHS = ("rfcs/RFC-0005/consent-egress-secrets.md",)
ROW_ARGUMENT_LINK_LABELS = frozenset({RFC5_CLASS_LABEL})
#: The file whose digest is the act argument of a row-argument link: the
#: installed module, which the manifest row hashes in its proposed form.
ROW_ARGUMENT_SUBJECTS = {RFC5_CLASS_LABEL: RFC5_CLASS_MODULE}


def _activate_rfc5_class_act_copy_registry():
    """Require both record copies and the manifest row once the record exists."""
    if not os.path.isfile(os.path.join(ROOT, RFC5_CLASS_ACT)):
        return
    labels = ACT_DIGEST_COPY_FILES.get(PERFORMED_ACT_RECORD, ())
    if RFC5_CLASS_LABEL not in labels:
        ACT_DIGEST_COPY_FILES[PERFORMED_ACT_RECORD] = labels + (RFC5_CLASS_LABEL,)
    ACT_DIGEST_COPY_FILES[RFC5_CLASS_ACT] = (RFC5_CLASS_LABEL,)
    ACT_DIGEST_COPY_FILES[RFC5_CLASS_SUBJECT] = (RFC5_CLASS_LABEL,)


'''
RFC5_EXEMPTION = ('    (f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md", '
                  '"manifest file"): RFC5_CLASS_SUBJECT,\n')
CHAIN_EDITS = (
    # (anchor, replacement); every anchor must occur exactly once
    ("CONTRACT_SUCCESSOR_CHAIN = (\n    (POLARIS_NO_SIGNAL_LABEL,",
     CHAIN_CONSTANTS + "CONTRACT_SUCCESSOR_CHAIN = (\n    (POLARIS_NO_SIGNAL_LABEL,"),
    ("     CONTRACT_RESTYLE_PATHS),\n)\nfor _label",
     "     CONTRACT_RESTYLE_PATHS),\n    (RFC5_CLASS_LABEL, RFC5_CLASS_SUBJECT, RFC5_CLASS_ACT,\n"
     "     _activate_rfc5_class_act_copy_registry, RFC5_CLASS_PATHS),\n)\nfor _label"),
    ("    for label, subject, _act, _activate, _paths in CONTRACT_SUCCESSOR_CHAIN:\n        out.append((label, subject,",
     "    for label, subject, _act, _activate, _paths in CONTRACT_SUCCESSOR_CHAIN:\n"
     "        out.append((label, ROW_ARGUMENT_SUBJECTS.get(label, subject),"),
    ("            link_digest = current_digest(subject)\n        else:",
     "            link_digest = current_digest(subject)\n"
     "            if label in ROW_ARGUMENT_LINK_LABELS:\n"
     '                rows_ = re.findall(r"^([0-9a-f]{64})  \\S+$", link_body or "", re.M)\n'
     "                link_digest = rows_[0] if len(rows_) == 1 else None\n        else:"),
    ("        if body_digest != link_digest:",
     "        if label not in ROW_ARGUMENT_LINK_LABELS and body_digest != link_digest:"),
)


# ---- helpers ---------------------------------------------------------------

class Refusal(Exception):
    pass


class Journal:
    """Remembers each file before the first write so a refusal restores the tree."""

    def __init__(self):
        self.saved: dict[pathlib.Path, bytes | None] = {}

    def save(self, path: pathlib.Path) -> None:
        if path not in self.saved:
            self.saved[path] = path.read_bytes() if path.is_file() else None

    def write(self, path: pathlib.Path, text: str) -> None:
        self.save(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def restore(self) -> None:
        for path, data in self.saved.items():
            if data is None:
                if path.is_file():
                    path.unlink()
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)


J = Journal()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def once(text: str, anchor: str, what: str) -> int:
    n = text.count(anchor)
    if n != 1:
        raise Refusal(f"{what}: anchor found {n} times, expected exactly once "
                      f"(check_governance.py has drifted; patch by hand and update this script)")
    return text.index(anchor)


def add_exemptions(text: str, lines: str) -> str:
    """Insert exemption rows before the closing brace of the exemptions dict."""
    start = once(text, EXEMPTION_DICT, "heading exemptions")
    end = text.index("\n}\n", start)
    return text[:end + 1] + lines + text[end + 1:]


def missing_records(root: pathlib.Path) -> list[str]:
    missing = [r for r in REQUIRED_RECORDS if not (root / r).is_file()]
    if not provider_routes(root):
        missing.append(f"{DECISIONS}/{ROUTE_A[1]}  (route A)  or  {DECISIONS}/{ROUTE_B[1]}  (route B)")
    return missing


def rfc5_precondition(root: pathlib.Path) -> None:
    record = (root / RFC5_ACT).read_text()
    if len(re.findall(r"^Act instant: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", record, re.M)) != 1:
        raise Refusal("the RFC5-14 act record carries no single 'Act instant:' line; the recorder "
                      "predates act-instant support, so the contract chain link cannot order it "
                      "(runbook finding F12: re-run the recorder from a build that writes it)")


# ---- steps -----------------------------------------------------------------

def step_registrations(root: pathlib.Path, write: bool) -> bool:
    """True when the step changed (or would change) anything."""
    perf = performed(root)
    path = root / CG
    text = path.read_text()
    changed = False
    if REGISTRATIONS_MARK not in text:
        i = once(text, REGISTRATIONS_ANCHOR, "registrations") + len(REGISTRATIONS_ANCHOR)
        text = text[:i] + registrations_code(perf) + text[i:]
        text = add_exemptions(text, exemptions_code(perf))
        changed = True
    else:
        absent = [rec for _l, rec, _m in perf if f'/{rec}", "manifest")' not in text]
        if absent:
            raise Refusal(f"registrations are installed for another record set; {absent} are not "
                          "registered (add them by hand or revert the earlier install)")
    if changed and write:
        J.write(path, text)
    return changed


def step_rfc5(root: pathlib.Path, write: bool) -> bool:
    changed = False
    manifest = (root / RFC5_PKG / "CONTRACT-AMENDMENT-MANIFEST.txt").read_text()
    rows = re.findall(r"^([0-9a-f]{64})  (\S+)$", manifest, re.M)
    if [p for _d, p in rows] != [RFC5_MODULE]:
        raise Refusal(f"rfc5 manifest rows are {[p for _d, p in rows]}, expected exactly [{RFC5_MODULE}]")
    row = rows[0][0]
    patch = root / RFC5_PKG / "proposed/RFC-0005/consent-egress-secrets.md.patch"
    for mirror in ("rfcs", "candidates/rfcs"):
        module = root / ".syzygy/governance/contracts" / mirror / "RFC-0005/consent-egress-secrets.md"
        if sha(module.read_bytes()) == row:
            continue
        changed = True
        if write:
            J.save(module)
            r = subprocess.run(["patch", "-s", "-p0", str(module), "-i", str(patch)], capture_output=True, text=True)
            if r.returncode or sha(module.read_bytes()) != row:
                raise Refusal(f"patch did not produce the manifest row for {module}: {r.stdout}{r.stderr}")
    active = root / CAND / "ACTIVE-CONTRACT-MANIFEST.txt"
    lines = active.read_text().split("\n")
    idx = [i for i, l in enumerate(lines) if l.endswith(f"  {RFC5_MODULE}")]
    if len(idx) != 1:
        raise Refusal(f"active manifest names {RFC5_MODULE} {len(idx)} times, expected once")
    if not lines[idx[0]].startswith(row):
        changed = True
        lines[idx[0]] = f"{row}  {RFC5_MODULE}"
        if write:
            J.write(active, "\n".join(lines))
    cg = root / CG
    text = cg.read_text()
    if CHAIN_MARK not in text:
        changed = True
        for anchor, replacement in CHAIN_EDITS:
            once(text, anchor, "contract chain link")
            text = text.replace(anchor, replacement)
        text = add_exemptions(text, RFC5_EXEMPTION)
        if write:
            J.write(cg, text)
    if changed and write:
        J.save(root / "DIRECTIVE-REGISTER.md")
        subprocess.run([sys.executable, "scripts/build_directive_register.py"], cwd=root,
                       capture_output=True, check=True)
    return changed


def step_profile(root: pathlib.Path, write: bool) -> bool:
    changed = False
    src = root / PROFILE_CHANGE / "proposed/polaris-generation/spec.md"
    dst = root / PROFILE_CHANGE / "specs/polaris-generation/spec.md"
    if src.is_file():
        changed = True
        if write:
            J.save(src)
            J.save(dst)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            for leftover in (src.parent, src.parent.parent):
                if leftover.is_dir() and not any(leftover.iterdir()):
                    leftover.rmdir()
    elif not dst.is_file():
        raise Refusal("the narrative-profile spec is in neither proposed/ nor specs/")
    old_new = (
        ("openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md",
         "openspec/changes/polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md"),
        ("`proposed/polaris-generation/spec.md`", "`specs/polaris-generation/spec.md`"),
    )
    for rel in (f"{PROFILE_PKG}/REVIEW-BRIEF.md", f"{PROFILE_PKG}/SEMANTIC-DELTA.md",
                f"{PROFILE_CHANGE}/GOVERNING-DEPENDENCIES.md", f"{PROFILE_CHANGE}/design.md"):
        p = root / rel
        text = p.read_text()
        new = text
        for a, b in old_new:
            new = new.replace(a, b)
        if new != text:
            changed = True
            if write:
                J.write(p, new)
    # the status page figure follows the recount tool, which this step then runs
    r = subprocess.run([sys.executable, "scripts/count_polaris_effective_scenarios.py"], cwd=root,
                       capture_output=True, text=True)
    m = re.search(r"TOTAL: (\d+) requirements, (\d+) scenarios", r.stdout)
    if not m:
        raise Refusal("the recount tool does not compose the three specs "
                      f"(land the recount fix first): {r.stdout[-200:]}{r.stderr[-200:]}")
    status = root / STATUS
    text = status.read_text()
    figure = re.search(r"(\d+) requirements and (\d+) scenarios in the effective composition", text)
    want = f"{m.group(1)} requirements and {m.group(2)} scenarios in the effective composition"
    if figure is None:
        raise Refusal("PROJECT-STATUS.md has no effective-composition figure")
    if figure.group(0) != want:
        changed = True
        if write:
            J.write(status, text.replace(figure.group(0), want))
    return changed


# ---- policy step (F4/F10) ------------------------------------------------------

_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
          9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
          15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
_TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def number_word(n: int) -> str:
    if n in _WORDS:
        return _WORDS[n]
    if 20 <= n <= 99:
        return _TENS[n // 10] + ("" if n % 10 == 0 else "-" + _WORDS[n % 10])
    raise Refusal(f"battery count {n} is outside the range the status sentence can spell")


def grab(pattern: str, text: str, what: str, flags: int = re.M) -> str:
    found = re.findall(pattern, text, flags)
    if len(found) != 1:
        raise Refusal(f"{what}: expected exactly one match of {pattern!r}, found {len(found)}")
    return found[0]


def replace_all_counted(text: str, old: str, new: str, what: str, minimum: int = 1) -> str:
    n = text.count(old)
    if n < minimum:
        raise Refusal(f"{what}: {old!r} found {n} times, expected at least {minimum}")
    return text.replace(old, new)


CHAIN_ROW_ANCHOR = '''     "2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a"),
)
#: For a chained amendment row'''
OFFERINGS_ANCHOR = '''        f"{CANDIDATES}/pwb-registry-currency-briefing-amendment/PWB-EFFECT-AMENDMENT-MANIFEST.txt": "row",
    },
}'''
REPIN_MANIFEST_ANCHOR = '''        ACT_DIGEST_COPY_FILES[PWB_BEHAVIOR_REPIN_MANIFEST] = (
            PWB_EFFECT_ACTS[1][0], PWB_EFFECT_ACTS[2][0])
'''
REPIN_DIR_ANCHOR = 'PWB_BEHAVIOR_REPIN_MANIFEST = f"{PWB_BEHAVIOR_REPIN_DIR}/PWB-EFFECT-REPIN-MANIFEST.txt"\n'
REPIN_CALL_ANCHOR = "_activate_pwb_behavior_repin_manifest_copy_registry()\n"
POLICY_MARK = "PWB_SCOPE_ACT"


def policy_cg_edits(text: str, old_arg: str) -> str:
    """The screening-scope act becomes the policy's chain link; the re-pin is history."""
    if POLICY_MARK in text:
        return text
    i = once(text, CHAIN_ROW_ANCHOR, "policy chain row") + len(CHAIN_ROW_ANCHOR) - len(")\n#: For a chained amendment row")
    row = ('    # The public-source screening-scope act supersedes the 2026-10-02 re-pin\n'
           '    # act for the policy subject.\n'
           '    (PWB_EFFECT_ACTS[1][0], PWB_EFFECT_ACTS[1][1],\n'
           '     f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md",\n'
           '     f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md",\n'
           f'     "{old_arg}"),\n')
    text = text[:i] + row + text[i:]
    i = once(text, OFFERINGS_ANCHOR, "policy offerings") + len(OFFERINGS_ANCHOR) - 2
    text = text[:i] + (
        '    # The 2026-10-02 policy re-pin was offered as a row of the re-pin manifest;\n'
        '    # its packet by design carries no digest.\n'
        '    f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md": {\n'
        '        PWB_BEHAVIOR_REPIN_MANIFEST: "row",\n'
        '    },\n') + text[i:]
    i = once(text, REPIN_MANIFEST_ANCHOR, "re-pin manifest registry") + len(REPIN_MANIFEST_ANCHOR)
    text = text[:i] + (
        '        # Once the screening-scope act supersedes the policy re-pin, the\n'
        '        # policy row is history (registered by the amendment registries).\n'
        '        if os.path.isfile(os.path.join(ROOT, PWB_SCOPE_ACT)):\n'
        '            ACT_DIGEST_COPY_FILES[PWB_BEHAVIOR_REPIN_MANIFEST] = (\n'
        '                PWB_EFFECT_ACTS[2][0],)\n') + text[i:]
    i = once(text, REPIN_DIR_ANCHOR, "re-pin directory constants") + len(REPIN_DIR_ANCHOR)
    text = text[:i] + (
        'PWB_SCOPE_DIR = f"{CANDIDATES}/public-source-screening-scope"\n'
        'PWB_SCOPE_MANIFEST = f"{PWB_SCOPE_DIR}/PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt"\n'
        'PWB_SCOPE_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md"\n') + text[i:]
    i = once(text, REPIN_CALL_ANCHOR, "re-pin registry call") + len(REPIN_CALL_ANCHOR)
    text = text[:i] + '''

def _activate_pwb_scope_manifest_copy_registry():
    """The screening-scope manifest carries the policy's proposed argument.

    Existence-gated candidate file: a current copy of the policy argument
    while it exists.
    """
    if os.path.isfile(os.path.join(ROOT, PWB_SCOPE_MANIFEST)):
        ACT_DIGEST_COPY_FILES[PWB_SCOPE_MANIFEST] = (PWB_EFFECT_ACTS[1][0],)


_activate_pwb_scope_manifest_copy_registry()
''' + text[i:]
    return add_exemptions(text, '    (PWB_SCOPE_ACT, "manifest"): PWB_SCOPE_MANIFEST,\n')


def battery_lines(record: str, new_arg: str, date: str) -> tuple[str, str]:
    """The scope recorder's --check line needs the owner's selection text, read back from the record."""
    opening = " ".join(grab(r'that opened "(.+?)" by selecting', record, "question opening", re.S).split())
    rows = re.findall(r'^\| "(.*)" \| "(.*)" \|$', record, re.M)
    if len(rows) != 1:
        raise Refusal(f"the scope act record carries {len(rows)} selection table rows, expected one")
    label, desc = rows[0]
    for s in (opening, label, desc):
        if ": " in s or " #" in s or "'" in s:
            raise Refusal("the owner's selection text contains ': ', ' #' or a quote, which a plain YAML "
                          "workflow line and the battery splitter cannot carry; add the --check line "
                          "to PROJECT-STATUS.md and the workflow by hand")
    cmd = (f"python3 scripts/record_public_source_screening_scope_act.py --check {new_arg} --date {date} "
           f"--question-opening '{opening}' --selection-label '{label}' --selection-description '{desc}'")
    return cmd, "python3 scripts/record_public_source_screening_scope_act.py --selftest"


def edit_battery(status: str, workflow: str, check_cmd: str, selftest_cmd: str) -> tuple[str, str]:
    if "record_public_source_screening_scope_act.py --check" in status:
        return status, workflow
    drop_b = "python3 scripts/build_pwb_behavior_contract_repin.py --check"
    drop_r = "python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy "
    lines = status.split("\n")
    keep = []
    for ln in lines:
        if ln.startswith(drop_b) or ln.startswith(drop_r):
            continue
        keep.append(ln)
        if ln.startswith("python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest"):
            keep.append(check_cmd + "   # screening-scope policy act: record, aggregate block and applied subject")
            keep.append(selftest_cmd)
    if len(keep) != len(lines):
        raise Refusal("status battery: expected to drop exactly two lines and add two")
    status = "\n".join(keep)
    skip = 0
    wlines = workflow.split("\n")
    out = []
    i = 0
    while i < len(wlines):
        ln = wlines[i]
        if ln.strip() in ("- name: build_pwb_behavior_contract_repin --check",
                          "- name: record_pwb_behavior_contract_repin_acts --check policy"):
            i += 3 if i + 2 < len(wlines) and wlines[i + 2].strip() == "" else 2
            skip += 1
            continue
        out.append(ln)
        if ln.strip() == "run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest":
            out += ["", "      - name: record_public_source_screening_scope_act --check",
                    f"        run: {check_cmd}", "",
                    "      - name: record_public_source_screening_scope_act --selftest",
                    f"        run: {selftest_cmd}"]
        i += 1
    if skip != 2:
        raise Refusal(f"workflow: expected to drop two steps, dropped {skip}")
    workflow = "\n".join(out)
    m = re.search(r"\bThe ([a-z]+(?:-[a-z]+)*) checks above are the same ([a-z]+(?:-[a-z]+)*)\b", status)
    if not m:
        raise Refusal("PROJECT-STATUS.md carries no 'The N checks above are the same N' sentence")
    block = re.search(r"## How to verify this page.*?```sh\n(.*?)```", status, re.S).group(1)
    n = len([ln for ln in block.split("\n") if ln.startswith("python3 ")])
    word = number_word(n)
    status = status.replace(m.group(0), f"The {word} checks above are the same {word}")
    return status, workflow


def step_policy(root: pathlib.Path, write: bool) -> bool:
    record = (root / SCOPE_ACT).read_text()
    repin = (root / REPIN_ACT).read_text()
    old_arg = grab(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`$", repin, "re-pin digest")
    new_arg = grab(r"^([0-9a-f]{64})  ", (root / SCOPE_MANIFEST).read_text(), "scope manifest row")
    identity = grab(r"^Act identity: `([^`]+)`$", record, "act identity")
    tag = grab(r"recording tag: `([^`]+)`", record, "recording tag")
    date = grab(r"^Date: (\d{4}-\d{2}-\d{2})$", record, "act date")
    new_ver = json.loads((root / POLICY_JSON).read_text())["policyVersion"]
    reader = (root / "packages/three-surface-poc-core/src/git-object-reader.ts").read_text()
    old_ver = grab(r"policyVersion: '([^']+)'", reader, "reader policy version") if "policyVersion: '" in reader else new_ver
    inputs = (root / INPUTS_TS).read_text()
    changed = False
    # check_governance supersession
    cg = root / CG
    text = cg.read_text()
    new_text = policy_cg_edits(text, old_arg)
    if new_text != text:
        changed = True
        if write:
            J.write(cg, new_text)
    # the read gate and its tests follow the act
    if SCOPE_ACT.split("/")[-1] not in inputs:
        changed = True
        if write:
            old_id = grab(r"actIdentity: '(PWB-SECRET-CLASSIFICATION-POLICY-[^']+)'", inputs, "gate policy identity")
            old_tag = grab(r"recordingTag: '(pwb-approve-policy-[^']+)'", inputs, "gate policy tag")
            for rel in PIN_FILES:
                p = root / rel
                s = p.read_text()
                for a, b in ((old_id, identity), (old_tag, tag), (old_ver, new_ver)):
                    if a in s:
                        s = s.replace(a, b)
                J.write(p, s)
            s = (root / INPUTS_TS).read_text()
            s = replace_all_counted(s, f"policy: '{REPIN_ACT}'", f"policy: '{SCOPE_ACT}'", "gate policy record")
            s = replace_all_counted(s, f"policy: '{AMENDMENT_ACT}'", f"policy: '{REPIN_ACT}'", "gate superseded record")
            marker = "export const PWB_ACT_RECORDS:"
            s = s.replace(marker, f"// The policy act is the {date} public-source screening-scope act, superseding the\n"
                                  f"// 2026-10-02 policy re-pin act; the registry act is still its 2026-10-02 re-pin act.\n"
                                  + marker, 1)
            J.write(root / INPUTS_TS, s)
            t = (root / INPUTS_TEST).read_text()
            t = re.sub(r"const EVALUATION_INSTANT = '[^']+';", f"const EVALUATION_INSTANT = '{date}T00:00:00Z';", t)
            J.write(root / INPUTS_TEST, t)
    # the status battery and the hosted workflow
    check_cmd, selftest_cmd = battery_lines(record, new_arg, date)
    status = (root / STATUS).read_text()
    workflow = (root / WORKFLOW).read_text()
    ns, nw = edit_battery(status, workflow, check_cmd, selftest_cmd)
    if (ns, nw) != (status, workflow):
        changed = True
        if write:
            J.write(root / STATUS, ns)
            J.write(root / WORKFLOW, nw)
    return changed


STEPS = (("registrations", step_registrations), ("rfc5", step_rfc5), ("policy", step_policy), ("profile", step_profile))


def run(root: pathlib.Path, write: bool) -> int:
    global J
    J = Journal()
    missing = missing_records(root)
    if missing:
        print("REFUSED: required act records are missing (nothing written):")
        for m in missing:
            print(f"  {m}")
        return 2
    try:
        rfc5_precondition(root)
        pending = []
        for name, fn in STEPS:
            if fn(root, write):
                pending.append(name)
    except Refusal as exc:
        J.restore()
        print(f"REFUSED: {exc} (tree restored)")
        return 2
    if write:
        print("installed: " + (", ".join(pending) if pending else "nothing to do (already installed)"))
        return 0
    print("not installed: " + (", ".join(pending) if pending else "none"))
    return 1 if pending else 0


# ---- selftest ----------------------------------------------------------------

def selftest() -> int:
    ok: list[tuple[str, bool]] = []
    both = {"a": PERFORMED_COMMON + (ROUTE_A,), "b": PERFORMED_COMMON + (ROUTE_B,)}
    ok.append(("registrations code defines and calls its function",
               registrations_code(both["a"]).count(REGISTRATIONS_MARK) == 2))
    for route, perf in both.items():
        ok.append((f"route {route}: every performed record is registered once",
                   all(registrations_code(perf).count(rec) == 1 for _l, rec, _m in perf)))
        ok.append((f"route {route}: exemptions cover every performed record",
                   all(exemptions_code(perf).count(rec) == 1 for _l, rec, _m in perf)))
    sample = "X = 1\n" + EXEMPTION_DICT + "\n    (1, 2): 3,\n}\nY = 2\n"
    got = add_exemptions(sample, "    (4, 5): 6,\n")
    ok.append(("exemption rows land inside the dict", got.index("(4, 5)") < got.index("}\nY")
               and got.index("(1, 2)") < got.index("(4, 5)")))
    jr = Journal()
    with tempfile.TemporaryDirectory() as t0:
        f1 = pathlib.Path(t0) / "a.txt"
        f2 = pathlib.Path(t0) / "new.txt"
        f1.write_text("old")
        jr.write(f1, "new")
        jr.write(f2, "created")
        jr.restore()
        ok.append(("a journal restores a changed file and removes a created one",
                   f1.read_text() == "old" and not f2.exists()))
    ok.append(("every required record is a performed record or the rfc5 act",
               {pathlib.PurePosixPath(r).name for r in REQUIRED_RECORDS}
               == {rec for _l, rec, _m in PERFORMED_COMMON}
               | {pathlib.PurePosixPath(RFC5_ACT).name, pathlib.PurePosixPath(SCOPE_ACT).name,
                  "POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md"}))
    ok.append(("number words round-trip the spelled range",
               [number_word(n) for n in (7, 19, 20, 69, 70, 73)]
               == ["seven", "nineteen", "twenty", "sixty-nine", "seventy", "seventy-three"]))
    try:
        number_word(100)
        ok.append(("a count past ninety-nine is refused", False))
    except Refusal:
        ok.append(("a count past ninety-nine is refused", True))
    rec = ('that opened "Q one" by selecting the\n| "L" | "D d" |\n')
    cmd, _st = battery_lines(rec, "a" * 64, "2026-10-04")
    ok.append(("battery line carries the owner's selection text",
               "--question-opening 'Q one' --selection-label 'L' --selection-description 'D d'" in cmd))
    try:
        battery_lines('that opened "Q: x" by selecting the\n| "L" | "D" |\n', "a" * 64, "2026-10-04")
        ok.append(("selection text a workflow line cannot carry is refused", False))
    except Refusal:
        ok.append(("selection text a workflow line cannot carry is refused", True))
    st = ("## How to verify this page\n```sh\n"
          "python3 scripts/build_pwb_behavior_contract_repin.py --check   # x\n"
          "python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy abc --date d\n"
          "python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest\n```\n"
          "The three checks above are the same three the hosted workflow runs.\n")
    wf = ("      - name: build_pwb_behavior_contract_repin --check\n"
          "        run: python3 scripts/build_pwb_behavior_contract_repin.py --check\n\n"
          "      - name: record_pwb_behavior_contract_repin_acts --check policy\n"
          "        run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy abc --date d\n\n"
          "      - name: record_pwb_behavior_contract_repin_acts --selftest\n"
          "        run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest\n")
    ns, nw = edit_battery(st, wf, "python3 scripts/record_public_source_screening_scope_act.py --check z",
                          "python3 scripts/record_public_source_screening_scope_act.py --selftest")
    ok.append(("battery edit drops two lines, adds two, and respells the count",
               "The three checks above are the same three" in ns and ns.count("python3 ") == 3
               and nw.count("run: python3") == 3 and "--check policy" not in ns + nw))
    ok.append(("battery edit is idempotent", edit_battery(ns, nw, "x", "y") == (ns, nw)))
    try:
        once("a b a", "a", "x")
        ok.append(("a repeated anchor is refused", False))
    except Refusal:
        ok.append(("a repeated anchor is refused", True))
    try:
        once("a b", "z", "x")
        ok.append(("an absent anchor is refused", False))
    except Refusal:
        ok.append(("an absent anchor is refused", True))
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        ok.append(("an empty tree is refused for every record and for the provider route",
                   missing_records(root)[:len(REQUIRED_RECORDS)] == list(REQUIRED_RECORDS)
                   and len(missing_records(root)) == len(REQUIRED_RECORDS) + 1))
        ok.append(("refusal writes nothing", run(root, True) == 2 and not any(root.iterdir())))
        act = root / RFC5_ACT
        act.parent.mkdir(parents=True)
        for good, name in (("Act instant: 2026-10-04T10:00:00Z\n", "single instant"),
                           ("", "no instant"),
                           ("Act instant: 2026-10-04T10:00:00Z\nAct instant: 2026-10-04T11:00:00Z\n", "two instants"),
                           ("Act instant: 2026-10-04 10:00\n", "malformed instant")):
            act.write_text("# x\n" + good)
            try:
                rfc5_precondition(root)
                passed = True
            except Refusal:
                passed = False
            ok.append((f"act instant precondition: {name}", passed == (name == "single instant")))
    failed = [n for n, g in ok if not g]
    for n, g in ok:
        print(("ok   " if g else "FAIL ") + n)
    print(f"selftest: {len(ok) - len(failed)} of {len(ok)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    return run(pathlib.Path(a.root), write=not a.check)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
