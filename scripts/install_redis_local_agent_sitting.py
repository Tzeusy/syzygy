#!/usr/bin/env python3
"""Record and install the Redis local-agent sitting from the owner's own words.

Candidate tooling. It performs no owner act by itself: every recorder it runs
is given the owner's selection exactly as an answers file states it, and an
act with no answer is not performed. It never infers an act, a variant or an
option. The order and the steps are the post-sitting list of
`.syzygy/governance/contracts/candidates/REDIS-LOCAL-AGENT-SITTING-BRIEF.md`.

  python3 scripts/install_redis_local_agent_sitting.py --answers FILE           # record, then install
  python3 scripts/install_redis_local_agent_sitting.py --answers FILE --check   # what is not yet done
  python3 scripts/install_redis_local_agent_sitting.py --selftest

The answers file is JSON:

  {"date": "YYYY-MM-DD",
   "start_instant": "YYYY-MM-DDTHH:MM:SSZ",            (optional; default now)
   "acts": {
     "v1.1": {"quote": "...", "options": ["n6"]},
     "entry-v1.0": {"quote": "..."},
     "screening-v1" | "rfc5" | "redis-observation" | "redis-no-evidence-drawer" |
     "redis-agent-anthropic" | "redis-agent-openai" | "d9-in-force" |
     "rfc7-20-reading-in-force" | "profile":
         {"opening": "...", "label": "...", "description": "..."},
     "screening-v2": {"variant": "none", "opening": "...", "label": "...", "description": "..."}}}

Each value is the owner's text, one line, recorded verbatim by the recorder.

Before anything is written it requires (exit 2, nothing written otherwise):

- a clean working tree;
- every act a local-agent run needs: screening-v1, redis-observation,
  entry-v1.0, rfc7-20-reading-in-force, profile, and at least one of
  redis-no-evidence-drawer, redis-agent-anthropic and redis-agent-openai
  (v1.1, rfc5, screening-v2 and d9-in-force are optional; screening-v2
  needs rfc5);
- no provider-mode record (route, egress, the fetching Git adapter, the
  requests consent): that sitting has its own installer,
  `install_redis_sitting.py`;
- each recorder present, the dossier-acts recorder frozen on its confirming
  review (PR #370), the screening-v2 recorder frozen when screening-v2 is
  answered, and the in-process reader of PR #367 present for entry-v1.0;
- selection text a battery line can carry: no ": ", " #" or "'".

Then, in order, each step's recorder runs `--record` and then `--check` with
the same arguments; the act's argument is its manifest row, read from the
manifest the owner's option names, never typed:

  1 v1.1           record_versioned_signoff (with its options), the
                   reconciliation regenerated, the route edits of
                   POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-SIGNOFF-ROUTE-EDITS.txt
  3 screening-v1   record_public_source_screening_scope_act
  4 rfc5           record_rfc5_project_documentation_act
  5 screening-v2   record_public_source_screening_scope_v2_act, the variant's row
  6 redis-observation  record_public_repo_admission_acts
  7 entry-v1.0     record_versioned_signoff, public-git-source-acquisition-local-agent
  8 statements     record_dossier_local_agent_acts, one key per answer
  9 profile        record_narrative_profile_adoption
  10 install       the existing installer's rfc5, policy, profile and reconcile
                   steps, this sitting's own registrations, and one battery
                   line per performed act in the status page and the hosted
                   workflow, with the count sentence re-derived (CG-26)
  gate sweep       the gate package's real-tree tests (`GATE_TESTS`): every
                   reader refuses an act a decisions/ file names without being
                   its record, so a record or sitting log carrying a swept stem
                   refuses the run (`--check` runs it too; run that again after
                   adding a sitting log)

Any refusal or failing recorder stops the run and stashes everything it wrote
(`git stash push --include-untracked`), so the tree is clean again and the
partial state is kept for reading. Nothing is committed.
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import install_redis_sitting as base  # noqa: E402

DECISIONS = base.DECISIONS
CAND = base.CAND
STATUS = base.STATUS
WORKFLOW = base.WORKFLOW
Refusal = base.Refusal

SCOPE_MANIFEST = base.SCOPE_MANIFEST
V2_MANIFEST = base.V2_MANIFEST
RFC5_MANIFEST = f"{base.RFC5_PKG}/CONTRACT-AMENDMENT-MANIFEST.txt"
ADMISSION_MANIFEST = f"{CAND}/public-repo-admission/PUBLIC-REPO-ADMISSION-MANIFEST.txt"
DOSSIER_ACTS = f"{CAND}/dossier-local-agent-acts"
DOSSIER_MANIFEST = f"{DOSSIER_ACTS}/DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt"
READER = "packages/polaris-dossier/src/git-object-reader.ts"
V11_ROUTE_EDITS = f"{CAND}/POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-SIGNOFF-ROUTE-EDITS.txt"
V11_REVIEW = "docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-2-RAW.md"
V11_NOTES = f"{CAND}/POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-REVIEW-NOTES.md"
ENTRY_REVIEW = f"{DOSSIER_ACTS}/reviews/R-DOSSIER-LOCAL-AGENT-SITTING-3-RAW.md"
ENTRY_NOTES = f"{DOSSIER_ACTS}/ROUND-3-DISPOSITIONS.md"

#: The admission record of the Redis consent: (label expression in
#: check_governance, record file, manifest constant), as the provider-mode
#: installer registers it (its finding F5).
REDIS_OBSERVATION = base.PERFORMED_COMMON[1]

#: (answer key, recorder, key argument, manifest, row path suffix)
SELECTION_ACTS = (
    ("screening-v1", "record_public_source_screening_scope_act", None, SCOPE_MANIFEST, "POLICY-CANDIDATE.json"),
    ("rfc5", "record_rfc5_project_documentation_act", None, RFC5_MANIFEST, "consent-egress-secrets.md"),
    ("screening-v2", "record_public_source_screening_scope_v2_act", None, V2_MANIFEST, None),
    ("redis-observation", "record_public_repo_admission_acts", "redis-observation", ADMISSION_MANIFEST,
     "redis/OBSERVATION-CONSENT.md"),
)
STATEMENT_ACTS = (
    ("redis-no-evidence-drawer", "instances/redis/NO-EVIDENCE-DRAWER-STATEMENT.md"),
    ("redis-agent-anthropic", "instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md"),
    ("redis-agent-openai", "instances/redis/AGENT-PROVIDER-STATEMENT-OPENAI.md"),
    ("d9-in-force", "instances/in-force/D9-IN-FORCE-RECORD.md"),
    ("rfc7-20-reading-in-force", "instances/in-force/RFC7-20-READING-IN-FORCE-RECORD.md"),
)
STATEMENT_RECORDER = "record_dossier_local_agent_acts"
PROFILE_RECORDER = "record_narrative_profile_adoption"
VERSIONED = "record_versioned_signoff"
DRAWER_OR_PROVIDER = ("redis-no-evidence-drawer", "redis-agent-anthropic", "redis-agent-openai")
REQUIRED = ("screening-v1", "redis-observation", "entry-v1.0", "rfc7-20-reading-in-force", "profile")
KNOWN = {"v1.1", "entry-v1.0", "profile"} | {a[0] for a in SELECTION_ACTS} | {a[0] for a in STATEMENT_ACTS}
V2_VARIANTS = ("none", "manifesto", "architecture", "both")

#: Provider-mode records: their presence means the other sitting was given.
PROVIDER_RECORDS = (
    base.ROUTE_A[1], base.ROUTE_B[1], base.EGRESS_V1[1], base.EGRESS_V2[1],
    base.PERFORMED_COMMON[0][1], base.PERFORMED_COMMON[2][1],
)

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INSTANT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")


# ---- answers ---------------------------------------------------------------

def validate_answers(answers: dict) -> list[str]:
    """Every reason the answers cannot be performed as given; empty when they can."""
    why = []
    date = answers.get("date", "")
    if not DATE_RE.fullmatch(str(date)):
        why.append("date is not YYYY-MM-DD")
    start = answers.get("start_instant")
    if start is not None and not (INSTANT_RE.fullmatch(start) and start.startswith(f"{date}T")):
        why.append("start_instant is not YYYY-MM-DDTHH:MM:SSZ on the date")
    acts = answers.get("acts")
    if not isinstance(acts, dict):
        return why + ["acts is not an object"]
    for key in sorted(set(acts) - KNOWN):
        why.append(f"unknown act {key!r}: this sitting performs only {sorted(KNOWN)}")
    for key in REQUIRED:
        if key not in acts:
            why.append(f"no answer for {key}: a local-agent run needs it, and an act is never inferred")
    if not any(k in acts for k in DRAWER_OR_PROVIDER):
        why.append(f"no answer for any of {list(DRAWER_OR_PROVIDER)}: one is needed")
    if "screening-v2" in acts and "rfc5" not in acts:
        why.append("screening-v2 needs rfc5: its policy maps a class only that amendment defines")
    for key, ans in acts.items():
        if not isinstance(ans, dict):
            why.append(f"{key}: the answer is not an object")
            continue
        fields = ("quote",) if key in ("v1.1", "entry-v1.0") else ("opening", "label", "description")
        for f in fields:
            text = ans.get(f)
            if not isinstance(text, str) or not text.strip():
                why.append(f"{key}: {f} is missing")
            elif "\n" in text or HEX64_RE.search(text):
                why.append(f"{key}: {f} must be one line with no digest")
            elif key not in ("v1.1", "entry-v1.0") and (": " in text or " #" in text or "'" in text):
                why.append(f"{key}: {f} contains ': ', ' #' or a quote, which a battery line cannot carry")
        if key == "screening-v2" and ans.get("variant") not in V2_VARIANTS:
            why.append(f"screening-v2: variant must be one of {list(V2_VARIANTS)}; the owner picks it")
        if key == "v1.1" and not set(ans.get("options", [])) <= {"n6"}:
            why.append("v1.1: the only option is n6")
        if key == "entry-v1.0" and "Extend Scope A" not in ans.get("quote", ""):
            why.append("entry-v1.0: the quote must name the Scope A extension ('Extend Scope A')")
    return why


def instants(answers: dict, n: int) -> list[str]:
    start = answers.get("start_instant")
    # by default the last act is now, not n minutes ahead: an act whose instant is
    # still ahead is not in force, so the gate check below would read it absent
    t = (datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ") if start
         else datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None, microsecond=0)
         - datetime.timedelta(minutes=n - 1))
    out = [(t + datetime.timedelta(minutes=k)).strftime("%Y-%m-%dT%H:%M:%SZ") for k in range(n)]
    if any(not i.startswith(answers["date"] + "T") for i in out):
        raise Refusal(f"the act instants {out[0]}..{out[-1]} leave the date {answers['date']}; "
                      "give a start_instant earlier in the day")
    return out


# ---- the tree --------------------------------------------------------------

def manifest_row(root: pathlib.Path, manifest: str, suffix: str | None, variant: str | None = None) -> str:
    text = (root / manifest).read_text()
    if variant is not None:
        rows = re.findall(rf"^([0-9a-f]{{64}})  \S+  \[variant: {re.escape(variant)}\]$", text, re.M)
    else:
        rows = [d for d, p in re.findall(r"^([0-9a-f]{64})  (\S+)$", text, re.M) if p.endswith(suffix)]
    if len(rows) != 1:
        raise Refusal(f"{manifest}: {len(rows)} rows for {variant or suffix}, expected one")
    return rows[0]


def git(root: pathlib.Path, *a: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True)


def preconditions(root: pathlib.Path, answers: dict) -> list[str]:
    why = []
    if git(root, "status", "--porcelain").stdout.strip():
        why.append("the working tree is not clean; a refusal could not be undone by a stash alone")
    for rec in PROVIDER_RECORDS:
        if (root / DECISIONS / rec).is_file():
            why.append(f"{rec} exists: that is the provider-mode sitting (install_redis_sitting.py)")
    acts = answers["acts"]
    scripts = {VERSIONED, PROFILE_RECORDER} | {s for k, s, *_ in SELECTION_ACTS if k in acts}
    if any(k in acts for k, _ in STATEMENT_ACTS):
        scripts.add(STATEMENT_RECORDER)
    for s in sorted(scripts):
        if not (root / "scripts" / f"{s}.py").is_file():
            why.append(f"scripts/{s}.py is absent (PR #370 carries the statement recorder)")
    rec = root / "scripts" / f"{STATEMENT_RECORDER}.py"
    if rec.is_file() and re.search(r"^FROZEN_SUBJECT: str \| None = None$", rec.read_text(), re.M):
        why.append("the dossier-acts recorder is not frozen: its package has no confirming review")
    v2 = root / "scripts/record_public_source_screening_scope_v2_act.py"
    if "screening-v2" in acts and v2.is_file() and re.search(
            r"^FROZEN_SUBJECT: str \| None = None$", v2.read_text(), re.M):
        why.append("the screening-v2 recorder is not frozen: run its round 7, then --freeze, first")
    if "entry-v1.0" in acts and not (root / READER).is_file():
        why.append(f"{READER} is absent: offer the entry only after PR #367 merges (PR #370 round 3, note 4)")
    if "v1.1" in acts and (root / DECISIONS / "POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.1.md").is_file():
        why.append("v1.1 is already recorded")
    for p in (V11_ROUTE_EDITS, V11_REVIEW, V11_NOTES) if "v1.1" in acts else ():
        if not (root / p).is_file():
            why.append(f"{p} is absent")
    for p in (ENTRY_REVIEW, ENTRY_NOTES, DOSSIER_MANIFEST) if "entry-v1.0" in acts else ():
        if not (root / p).is_file():
            why.append(f"{p} is absent")
    return why + register_check(root)


# ---- the recorders ---------------------------------------------------------

class Step:
    def __init__(self, key: str, label: str, record: list[str], check: list[str], battery: list[str] | None):
        self.key, self.label, self.record, self.check, self.battery = key, label, record, check, battery


def selection_args(ans: dict) -> list[str]:
    return ["--question-opening", ans["opening"], "--selection-label", ans["label"],
            "--selection-description", ans["description"]]


def quoted(argv: list[str]) -> str:
    """The battery form of a command: one line, selection text in single quotes."""
    out = []
    for a in argv:
        out.append(f"'{a}'" if (" " in a or not a) else a)
    return " ".join(out)


def plan(root: pathlib.Path, answers: dict) -> list[Step]:
    """The recorder runs, in the brief's order, for exactly the acts answered."""
    acts, date = answers["acts"], answers["date"]
    order = (["v1.1"] if "v1.1" in acts else []) + \
        [k for k, *_ in SELECTION_ACTS if k in acts] + \
        (["entry-v1.0"] if "entry-v1.0" in acts else []) + \
        [k for k, _ in STATEMENT_ACTS if k in acts] + ["profile"]
    at = dict(zip(order, instants(answers, len(order))))
    py = sys.executable
    steps = []
    for key in order:
        ans = acts[key]
        if key in ("v1.1", "entry-v1.0"):
            pkg, ver, review, notes = (("polaris-dossier-local-agent-mode", "1.1", V11_REVIEW, V11_NOTES)
                                       if key == "v1.1" else
                                       ("public-git-source-acquisition-local-agent", "1.0", ENTRY_REVIEW, ENTRY_NOTES))
            opts = [x for o in ans.get("options", []) for x in ("--option", o)]
            rec = [py, f"scripts/{VERSIONED}.py", "--record", pkg, "--version", ver, "--date", date,
                   "--review", review, "--disposition", notes, "--owner-selection-quote", ans["quote"],
                   "--instant", at[key], *opts]
            chk = ["python3", f"scripts/{VERSIONED}.py", "--check", pkg, "--version", ver]
            # v1.1's battery line is the route edits' block 3, applied with them
            steps.append(Step(key, f"{pkg} v{ver}", rec, chk, None if key == "v1.1" else chk))
            continue
        if key == "profile":
            sel = selection_args(ans)
            rec = [py, f"scripts/{PROFILE_RECORDER}.py", "--record", "--date", date, "--instant", at[key], *sel]
            chk = ["python3", f"scripts/{PROFILE_RECORDER}.py", "--check", "--date", date, *sel]
            steps.append(Step(key, "narrative profile", rec, chk, chk))
            continue
        if key in {k for k, _ in STATEMENT_ACTS}:
            suffix = dict(STATEMENT_ACTS)[key]
            arg = manifest_row(root, DOSSIER_MANIFEST, suffix)
            head, script = [key, arg], STATEMENT_RECORDER
        else:
            _k, script, k_arg, manifest, suffix = next(a for a in SELECTION_ACTS if a[0] == key)
            arg = manifest_row(root, manifest, suffix, ans.get("variant") if key == "screening-v2" else None)
            head = ([k_arg] if k_arg else []) + [arg]
        sel = selection_args(ans)
        rec = [py, f"scripts/{script}.py", "--record", *head, "--date", date, "--instant", at[key], *sel]
        chk = ["python3", f"scripts/{script}.py", "--check", *head, "--date", date, *sel]
        # the policy acts' battery lines are the existing installer's policy step
        steps.append(Step(key, key, rec, chk, None if key.startswith("screening-") else chk))
    return steps


def run_recorder(root: pathlib.Path, step: Step) -> None:
    for argv, what in ((step.record, "--record"), ([sys.executable] + step.check[1:], "--check")):
        p = subprocess.run(argv, cwd=root, capture_output=True, text=True)
        if p.returncode:
            raise Refusal(f"{step.label} {what} exited {p.returncode}: "
                          f"{(p.stdout + p.stderr).strip()[-600:]}")
    print(f"recorded: {step.label}")


# ---- v1.1 route edits ------------------------------------------------------

def route_blocks(text: str, section: int) -> list[str]:
    part = text.split(f"== {section}.")[1].split("\n== ")[0]
    return re.findall(r"(?ms)^----\n(.*?)\n----$", part)


def sub_once(path: pathlib.Path, old: str, new: str) -> None:
    text = path.read_text()
    if text.count(old) != 1:
        raise Refusal(f"{path.name}: the route-edit anchor occurs {text.count(old)} times, expected once")
    path.write_text(text.replace(old, new))


def v11_route_edits(root: pathlib.Path, date: str) -> None:
    """Blocks 1 to 4 and 6 of the route-edits file; block 5, the count, is re-derived at the end."""
    text = (root / V11_ROUTE_EDITS).read_text().replace("<date>", date)
    status = (root / STATUS).read_text()
    for line in route_blocks(text, 1)[0].split("\n")[:2]:
        if line not in status:
            raise Refusal(f"route edit block 1: the builder did not write {line.strip()!r}")
    old, new = route_blocks(text, 2)
    sub_once(root / "openspec/README.md", old, new)
    anchor = next(ln for ln in status.split("\n")
                  if ln.startswith("python3 scripts/record_versioned_signoff.py --check polaris-dossier-local-agent-mode --version 1.0"))
    sub_once(root / STATUS, anchor + "\n", anchor + "\n" + route_blocks(text, 3)[0] + "\n")
    wf = "        run: python3 scripts/record_versioned_signoff.py --check polaris-dossier-local-agent-mode --version 1.0\n"
    sub_once(root / WORKFLOW, wf, wf + route_blocks(text, 4)[0] + "\n")
    ev = root / "docs/evidence/spec-readability-reconciliation-2026-10-02/README.md"
    ev.write_text(ev.read_text().rstrip("\n") + "\n\n" + route_blocks(text, 6)[0] + "\n")


# ---- install ---------------------------------------------------------------

LOCAL_MARK = "_activate_redis_local_agent_performed_registries"
BATTERY_MARK = "_activate_redis_local_agent_battery_copies"
BATTERY_ANCHOR = "\ndef main():\n"
#: Rehearsal 2 (CG-7e): each digest-bound act's battery `--check` line passes
#: its argument, so the status page is a copy file for that act. Existence-gated
#: on the dedicated record, and inserted late so every label constant exists.
BATTERY_COPIES_CODE = f'''

def {BATTERY_MARK}():
    """Install change: the battery's recorder lines pass each recorded local-agent act's argument."""
    pairs = list(DOSSIER_LOCAL_AGENT_ACT_RECORDS.items())
    pairs.append(({REDIS_OBSERVATION[0]}, f"{{DECISIONS}}/{REDIS_OBSERVATION[1]}"))
    # the RFC5-14 constants exist only once that act's chain link is installed; the
    # name is split so this text never carries the chain step's install mark
    rfc5 = globals().get("RFC5_" "CLASS_LABEL")
    if rfc5 is not None:
        pairs.append((rfc5, globals()["RFC5_" "CLASS_ACT"]))
    present = ACT_DIGEST_COPY_FILES.get("PROJECT-STATUS.md", ())
    for label, record in pairs:
        if os.path.isfile(os.path.join(ROOT, record)) and label not in present:
            present = present + (label,)
    ACT_DIGEST_COPY_FILES["PROJECT-STATUS.md"] = present


{BATTERY_MARK}()

'''


#: Rehearsal 2 (CG-1b): the v1.1 package, signed 2026-10-07, cites the narrative
#: profile's spec at its pre-adoption path, which the profile step moves. Signed
#: bytes are not edited, so the reference is declared and printed under CG-1d's
#: history bucket instead of failing; the declaration names file, target and why.
MOVED_MARK = "SIGNED_PACKAGE_MOVED_TARGETS"
MOVED_CODE = '''#: A signed package's citation of a path that a later act moved. The package's
#: bytes are what its version tag binds, so the citation is history, not a
#: route: classified and printed under CG-1d, never silenced.
SIGNED_PACKAGE_MOVED_TARGETS = {
    (f"{CANDIDATES}/polaris-dossier-local-agent-mode-v1-1/IMPACT-LEDGER.md",
     "openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md"):
        "signed v1.1 bytes; the narrative-profile adoption moved the spec to specs/",
}


'''
MOVED_DEF_ANCHOR = "def cg1_links(paths, res):\n"
MOVED_BRANCH_ANCHOR = "        elif _is_frozen_lane(rel):\n            # CG-1a had no frozen-lane branch"
MOVED_BRANCH = ("        elif (rel, t) in SIGNED_PACKAGE_MOVED_TARGETS:\n"
                "            historical.append(f\"{rel} -> {t} — {SIGNED_PACKAGE_MOVED_TARGETS[(rel, t)]}\")\n")
MOVED_CITER = ".syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-1/IMPACT-LEDGER.md"


def step_moved_targets(root: pathlib.Path, write: bool) -> bool:
    """Declare the v1.1 ledger's citation once the profile spec has left proposed/."""
    moved = (root / base.PROFILE_CHANGE / "specs/polaris-generation/spec.md").is_file() and \
        not (root / base.PROFILE_CHANGE / "proposed/polaris-generation/spec.md").exists()
    citer = root / MOVED_CITER
    if not moved or not citer.is_file() or "polaris-non-governed-narrative-profile/proposed/" not in citer.read_text():
        return False
    path = root / base.CG
    text = path.read_text()
    if MOVED_MARK in text:
        return False
    i = base.once(text, MOVED_DEF_ANCHOR, "moved-target constant")
    text = text[:i] + MOVED_CODE + text[i:]
    j = base.once(text, MOVED_BRANCH_ANCHOR, "moved-target branch")
    text = text[:j] + MOVED_BRANCH + text[j:]
    if write:
        base.J.write(path, text)
    return True


def step_registrations(root: pathlib.Path, write: bool) -> bool:
    """The Redis observation record becomes an act-copy file (provider-mode finding F5).

    The statement records of PR #370 register themselves (existence-gated), and
    the version-tagged entry sign-off quotes no act argument."""
    path = root / base.CG
    text = path.read_text()
    changed = False
    if LOCAL_MARK in text or base.REGISTRATIONS_MARK in text:
        if f'/{REDIS_OBSERVATION[1]}", "manifest")' not in text:
            raise Refusal("registrations are installed for another record set")
    else:
        code = base.registrations_code((REDIS_OBSERVATION,)).replace(base.REGISTRATIONS_MARK, LOCAL_MARK)
        i = base.once(text, base.REGISTRATIONS_ANCHOR, "registrations") + len(base.REGISTRATIONS_ANCHOR)
        text = base.add_exemptions(text[:i] + code + text[i:], base.exemptions_code((REDIS_OBSERVATION,)))
        changed = True
    if changed and write:
        base.J.write(path, text)
    return changed


def step_battery_copies(root: pathlib.Path, write: bool) -> bool:
    """The status page is a copy file for every recorded act whose battery line it carries.

    Runs after the RFC5-14 step: that step treats its constant's name as its install
    mark, so this insertion must neither precede it nor carry the name whole."""
    if base.CHAIN_MARK in BATTERY_COPIES_CODE:
        raise Refusal("the battery-copies code carries the RFC5-14 chain step's install mark")
    path = root / base.CG
    text = path.read_text()
    if BATTERY_MARK in text:
        return False
    i = base.once(text, BATTERY_ANCHOR, "battery copies")
    text = text[:i] + BATTERY_COPIES_CODE.rstrip("\n") + "\n\n" + text[i:]
    if write:
        base.J.write(path, text)
    return True


def step_rfc5(root: pathlib.Path, write: bool) -> bool:
    if not (root / base.RFC5_ACT).is_file():
        if (root / base.V2_ACT).is_file():
            raise Refusal("the screening-v2 act exists without the RFC5-14 act it needs")
        return False
    base.rfc5_precondition(root)
    return base.step_rfc5(root, write)


def battery_text(status: str, workflow: str, lines: list[tuple[str, str]]) -> tuple[str, str]:
    """Add each (name, command) not yet published, to both lists, and re-derive the count."""
    head = re.search(r"## How to verify this page.*?```sh\n", status, re.S)
    if head is None:
        raise Refusal(f"{STATUS} carries no battery block")
    end = status.index("```", head.end())
    block = status[head.end():end]
    add_s, add_w = "", ""
    for name, cmd in lines:
        if cmd in block:
            continue
        add_s += f"{cmd}   # {name}\n"
        add_w += f"\n      - name: {name}\n        run: {cmd}\n"
    status = status[:end] + add_s + status[end:]
    workflow = workflow.rstrip("\n") + "\n" + add_w if add_w else workflow
    block = re.search(r"## How to verify this page.*?```sh\n(.*?)```", status, re.S).group(1)
    n = len([ln for ln in block.split("\n") if ln.startswith("python3 ")])
    m = re.search(r"\bThe ([a-z]+(?:-[a-z]+)*) checks above are the same ([a-z]+(?:-[a-z]+)*)\b", status)
    if m is None:
        raise Refusal(f"{STATUS} carries no 'The N checks above are the same N' sentence")
    word = base.number_word(n)
    status = status.replace(m.group(0), f"The {word} checks above are the same {word}")
    return status, workflow


def step_battery(root: pathlib.Path, write: bool, steps: list[Step]) -> bool:
    lines = [(f"{s.label} --check", quoted(s.battery)) for s in steps if s.battery]
    if (root / base.RFC5_ACT).is_file():
        lines.append(("rfc5 --selftest", "python3 scripts/record_rfc5_project_documentation_act.py --selftest"))
    status, workflow = (root / STATUS).read_text(), (root / WORKFLOW).read_text()
    ns, nw = battery_text(status, workflow, lines)
    if (ns, nw) == (status, workflow):
        return False
    if write:
        base.J.write(root / STATUS, ns)
        base.J.write(root / WORKFLOW, nw)
    return True


def install(root: pathlib.Path, write: bool, steps: list[Step]) -> list[str]:
    pending = []
    for name, fn in (("registrations", step_registrations), ("rfc5", step_rfc5),
                     ("battery-copies", step_battery_copies),
                     ("policy", base.step_policy), ("profile", base.step_profile),
                     ("moved", step_moved_targets), ("reconcile", base.step_reconcile)):
        if fn(root, write):
            pending.append(name)
    if step_battery(root, write, steps):
        pending.append("battery")
    return pending


# ---- the gate's own sweeps (syzygy-s6xo) -----------------------------------

#: Every gate reader refuses an act that a decisions/ file names without being
#: its record: a withdrawal, or a form the reader does not define. A record,
#: aggregate row or sitting log that carries a swept stem therefore refuses the
#: act it was meant to record, silently, at the next run. The stems, their
#: folding and the aggregate record's field-line exemption live in the gate
#: package (`package-reader.ts`, the forms in `gate-sources.ts`); this check
#: runs that package's real-tree tests rather than copying the list, so the two
#: cannot drift. Each test asserts the state the records on this checkout
#: establish, so a swept stem fails it as `refused`.
GATE_TESTS = ("packages/polaris-generation-consent/src/real-tree.test.ts",
              "packages/polaris-dossier/src/gate-acts.test.ts")


def gate_sweep(root: pathlib.Path) -> str | None:
    """None when the gate's readers accept every decisions/ file on this tree; else why."""
    absent = [t for t in GATE_TESTS if not (root / t).is_file()]
    if absent:
        return f"{absent} absent: the gate's real-tree tests (PR #377) must be on this tree"
    p = subprocess.run(["npx", "vitest", "run", *GATE_TESTS, "--reporter=dot"],
                       cwd=root, capture_output=True, text=True)
    if p.returncode:
        return ("the gate's real-tree tests fail, so a decisions/ file names a swept stem or the "
                f"records disagree with the gate: {(p.stdout + p.stderr).strip()[-1200:]}")
    return None


P104 = "| P-104 |"


def register_check(root: pathlib.Path) -> list[str]:
    """The sitting resolves P-104 in place in the register; it never moves to DECISION-HISTORY.md,
    where the registry gate refuses it."""
    why = []
    pending = root / DECISIONS / "PENDING-OWNER-DECISIONS.md"
    rows = [ln for ln in pending.read_text(encoding="utf-8").splitlines() if ln.startswith(P104)] if pending.is_file() else []
    if len(rows) != 1:
        why.append(f"PENDING-OWNER-DECISIONS.md carries {len(rows)} P-104 rows, not exactly one")
    history = root / DECISIONS / "DECISION-HISTORY.md"
    if history.is_file() and P104 in history.read_text(encoding="utf-8"):
        why.append("DECISION-HISTORY.md carries a P-104 row: P-104 is resolved in place, never moved")
    return why


# ---- run -------------------------------------------------------------------

def stash(root: pathlib.Path, why: str) -> None:
    p = git(root, "stash", "push", "--include-untracked", "-m", f"local-agent sitting refused: {why[:80]}")
    print("the partial state is stashed (git stash list); the tree is clean again"
          if p.returncode == 0 else f"stash failed, the tree holds the partial state: {p.stderr.strip()}")


def record_and_install(root: pathlib.Path, answers: dict) -> int:
    why = validate_answers(answers)
    if not why:
        why = preconditions(root, answers)
    if why:
        print("REFUSED (nothing written):")
        for w in why:
            print(f"  {w}")
        return 2
    base.J = base.Journal()
    try:
        steps = plan(root, answers)
        for step in steps:
            run_recorder(root, step)
            if step.key == "v1.1":
                p = subprocess.run([sys.executable, "scripts/check_spec_reconciliation.py", "--regenerate"],
                                   cwd=root, capture_output=True, text=True)
                if p.returncode:
                    raise Refusal(f"check_spec_reconciliation --regenerate: {(p.stdout + p.stderr)[-400:]}")
                v11_route_edits(root, answers["date"])
                print("v1.1: reconciliation regenerated, route edits applied")
        pending = install(root, True, steps)
    except (Refusal, subprocess.SubprocessError, OSError, ValueError) as exc:
        print(f"REFUSED: {exc}")
        stash(root, str(exc))
        return 2
    print("installed: " + (", ".join(pending) if pending else "nothing to do"))
    again = install(root, False, steps)
    if again:
        print(f"NOT IDEMPOTENT: a second pass would still change {again}")
        return 1
    swept = gate_sweep(root)
    if swept:
        print(f"REFUSED: {swept}")
        stash(root, "the gate's real-tree tests fail")
        return 2
    print("gate sweep: the gate's readers accept every decisions/ file")
    print("next: add any sitting log, re-run --check (it re-runs the gate sweep), run the battery "
          "(PROJECT-STATUS.md, How to verify this page) and commit; nothing was committed")
    return 0


def check(root: pathlib.Path, answers: dict) -> int:
    """Read-only: each answered act's recorder --check, then what the install would still change."""
    why = validate_answers(answers)
    if why:
        print("answers invalid:\n  " + "\n  ".join(why))
        return 2
    base.J = base.Journal()
    failing = []
    try:
        steps = plan(root, answers)
        for s in steps:
            # version 2 supersedes version 1 for the policy role: v1's --check then
            # fails by design ("the policy on disk is not the argued bytes")
            if s.key == "screening-v1" and "screening-v2" in answers["acts"]:
                continue
            p = subprocess.run([sys.executable] + s.check[1:], cwd=root, capture_output=True, text=True)
            if p.returncode:
                failing.append(s.label)
        pending = install(root, False, steps)
    except Refusal as exc:
        print(f"REFUSED: {exc}")
        return 2
    swept = gate_sweep(root)
    register = register_check(root)
    print("recorder checks failing: " + (", ".join(failing) or "none"))
    print("not installed: " + (", ".join(pending) or "none"))
    print("gate sweep: " + (swept or "the gate's readers accept every decisions/ file"))
    print("register: " + ("; ".join(register) or "P-104 stays one row of PENDING-OWNER-DECISIONS.md"))
    return 1 if failing or pending or swept or register else 0


# ---- selftest --------------------------------------------------------------

def sample_answers() -> dict:
    sel = {"opening": "Sign it at its manifest row?", "label": "Sign it", "description": "Sign it as the brief recommends."}
    return {"date": "2026-10-07", "start_instant": "2026-10-07T09:00:00Z", "acts": {
        "v1.1": {"quote": "1.1 signed off with N6; N1 and N2 as recommended.", "options": ["n6"]},
        "screening-v1": dict(sel), "rfc5": dict(sel), "screening-v2": dict(sel, variant="none"),
        "redis-observation": dict(sel), "entry-v1.0": {"quote": "Extend Scope A to this entry and sign v1.0"},
        "redis-no-evidence-drawer": dict(sel), "d9-in-force": dict(sel), "rfc7-20-reading-in-force": dict(sel),
        "profile": dict(sel)}}


def selftest() -> int:
    ok: list[tuple[str, bool]] = []
    good = sample_answers()
    ok.append(("the brief's accept-all answers validate", validate_answers(good) == []))

    def refused(mutate, needle):
        a = json.loads(json.dumps(good))
        mutate(a)
        return any(needle in w for w in validate_answers(a))
    for key in REQUIRED:
        ok.append((f"an absent {key} is refused, never inferred",
                   refused(lambda a, k=key: a["acts"].pop(k), f"no answer for {key}")))
    ok.append(("no drawer statement and no provider statement is refused",
               refused(lambda a: a["acts"].pop("redis-no-evidence-drawer"), "one is needed")))
    ok.append(("screening-v2 without rfc5 is refused", refused(lambda a: a["acts"].pop("rfc5"), "needs rfc5")))
    ok.append(("an unpicked v2 variant is refused", refused(lambda a: a["acts"]["screening-v2"].pop("variant"), "variant")))
    ok.append(("an unknown act is refused", refused(lambda a: a["acts"].update({"egress": {}}), "unknown act")))
    ok.append(("an unknown v1.1 option is refused", refused(lambda a: a["acts"]["v1.1"].update(options=["n7"]), "only option")))
    ok.append(("an entry quote without the Scope A extension is refused",
               refused(lambda a: a["acts"]["entry-v1.0"].update(quote="Sign it"), "Scope A")))
    ok.append(("a selection a battery line cannot carry is refused",
               refused(lambda a: a["acts"]["profile"].update(label="Adopt: yes"), "battery line")))
    ok.append(("a digest in the owner's words is refused",
               refused(lambda a: a["acts"]["profile"].update(label="a" * 64), "no digest")))
    ok.append(("a missing date is refused", refused(lambda a: a.pop("date"), "date")))
    ok.append(("an instant off the date is refused",
               refused(lambda a: a.update(start_instant="2026-10-08T09:00:00Z"), "start_instant")))
    ins = instants(good, 3)
    ok.append(("instants increase by a minute from the start", ins == ["2026-10-07T09:00:00Z",
                                                                       "2026-10-07T09:01:00Z", "2026-10-07T09:02:00Z"]))
    try:
        instants(dict(good, start_instant="2026-10-07T23:59:30Z"), 3)
        ok.append(("instants that leave the date are refused", False))
    except Refusal:
        ok.append(("instants that leave the date are refused", True))
    unstarted = dict(good, date=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"))
    unstarted.pop("start_instant")
    try:
        last = instants(unstarted, 3)[-1]
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        ok.append(("by default no act instant lies ahead of now", last <= now))
    except Refusal:
        # within two minutes of midnight UTC the default leaves the date and is refused
        ok.append(("by default no act instant lies ahead of now", True))
    ok.append(("a battery command quotes multi-word text only",
               quoted(["python3", "x.py", "--check", "--selection-label", "Sign it"])
               == "python3 x.py --check --selection-label 'Sign it'"))
    st = ("## How to verify this page\n\n```sh\npython3 a.py\n```\n\n"
          "The one checks above are the same one the hosted workflow runs.\n")
    wf = "jobs:\n  x:\n    steps:\n      - name: a\n        run: python3 a.py\n"
    ns, nw = battery_text(st, wf, [("b --check", "python3 b.py --check 'x y'")])
    ok.append(("a battery line lands in both lists and the count is re-derived",
               "python3 b.py --check 'x y'   # b --check\n```" in ns and "The two checks above are the same two" in ns
               and nw.endswith("      - name: b --check\n        run: python3 b.py --check 'x y'\n")))
    ok.append(("adding the same battery line twice changes nothing",
               battery_text(ns, nw, [("b --check", "python3 b.py --check 'x y'")]) == (ns, nw)))
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        (root / "m.txt").write_text(f"# x\n{'a' * 64}  p/one.md\n{'b' * 64}  p/two.md\n"
                                    f"{'c' * 64}  p/pol.json  [variant: none]\n")
        ok.append(("a manifest row is read by its path", manifest_row(root, "m.txt", "two.md") == "b" * 64))
        ok.append(("a variant row is read by its variant", manifest_row(root, "m.txt", None, "none") == "c" * 64))
        try:
            manifest_row(root, "m.txt", "three.md")
            ok.append(("an absent row is refused", False))
        except Refusal:
            ok.append(("an absent row is refused", True))
        (root / DECISIONS).mkdir(parents=True)
        (root / DECISIONS / base.EGRESS_V2[1]).write_text("x")
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        why = preconditions(root, good)
        ok.append(("a provider-mode record is refused", any("provider-mode" in w for w in why)))
        ok.append(("a dirty tree is refused", any("not clean" in w for w in why)))
        ok.append(("absent recorders are refused", any("is absent" in w for w in why)))
        ok.append(("the entry without the reader of PR #367 is refused", any("#367" in w for w in why)))
        ok.append(("a tree without the gate's real-tree tests fails the gate sweep",
                   "absent" in (gate_sweep(root) or "")))
        ok.append(("a register with no P-104 row is refused", any("0 P-104 rows" in w for w in why)))
        (root / DECISIONS / "PENDING-OWNER-DECISIONS.md").write_text("| P-104 | open |\n")
        ok.append(("one P-104 row in the register and none in the history passes", register_check(root) == []))
        (root / DECISIONS / "DECISION-HISTORY.md").write_text("| P-104 | moved |\n")
        ok.append(("a P-104 row moved into DECISION-HISTORY.md is refused",
                   any("never moved" in w for w in register_check(root))))
        ok.append(("a refusal of the answers writes nothing",
                   record_and_install(root, {"date": "x", "acts": {}}) == 2
                   and sorted(p.name for p in root.iterdir()) == [".git", ".syzygy", "m.txt"]))
    failed = [n for n, g in ok if not g]
    for n, g in ok:
        print(("ok   " if g else "FAIL ") + n)
    print(f"selftest: {len(ok) - len(failed)} of {len(ok)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--answers")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.answers:
        ap.error("--answers is required")
    answers = json.loads(pathlib.Path(a.answers).read_text())
    root = pathlib.Path(a.root)
    return check(root, answers) if a.check else record_and_install(root, answers)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
