#!/usr/bin/env python3
"""Verify and manifest the Messages API provider-route registry-entry candidate.

Package `contracts/candidates/provider-route-messages-api-entry/`: one
proposed adapter-registry entry, a whole `proposed/*.json` file, for the
Anthropic Messages API route (`@anthropic-ai/sdk` 0.131.0, PR #264). It is a
SUBSTITUTE for the Agent SDK provider entry of the public-admission registry
package (RFC4-1: one adapter per external authority per project), never an
addition. It binds nothing; it takes effect only through its own owner act
over its exact bytes, whose argument is its row of
`MESSAGES-API-ROUTE-REGISTRY-MANIFEST.txt`.

  --check            fail if the entry breaks a predicate, a package Markdown
                     file carries a 64-hex token, or the manifest is stale
  --write            regenerate the manifest (after a --check of the entry)
  --digests          print the proposed file's SHA-256 (the act argument)
  --manifest-digest  print the SHA-256 of the manifest FILE
  --selftest         one mutant per predicate; each must be caught
"""
import copy
import hashlib
import json
import pathlib
import re
import subprocess
import sys

PKG = pathlib.Path(".syzygy/governance/contracts/candidates/provider-route-messages-api-entry")
MANIFEST = "MESSAGES-API-ROUTE-REGISTRY-MANIFEST.txt"
ENTRY = "POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json"
BUTLERS = pathlib.Path(".syzygy/governance/declarations/adapter-registry/"
                       "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json")
INSTALLED = pathlib.Path(".syzygy/governance/declarations/adapter-registry")
#: The sibling Agent SDK entry (PR #255) this one substitutes; checked
#: against its proposed file only while that file exists in the tree.
#: RFC4-9: the role identity persists, a new implementation identity is registered.
SIBLING_ID = "polaris-provider-route-anthropic-agent-sdk"
SIBLING_IMPL = "polaris-generation/provider-agent-sdk"
UPSTREAM = "https://api.anthropic.com"
#: The SDK 0.131.0 environment inputs the entry must declare, each with a fail-closed posture.
ENV_INPUTS = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_CUSTOM_HEADERS",
              "ANTHROPIC_LOG", "ANTHROPIC_BASE_URL")
NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
SIBLING_FILE = pathlib.Path(".syzygy/governance/contracts/candidates/"
                            "public-admission-registry-entries/proposed/"
                            "POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json")
AUTHORITY_KEY = {"observingProject": "project:syzygy", "provider": "provider:anthropic",
                 "authorityType": "model-provider"}
HEX64 = re.compile(r"[0-9a-f]{64}")
#: RFC4-2 items 1-7 as the keys an entry must carry.
REQUIRED = ("observerId", "implementationId", "observerVersion", "implementationVersion",
            "contractId", "contractVersion", "inputClasses", "outputFactClasses",
            "determinismClass", "failureStates", "typedAuthority")
#: The egress record's route conditions, as keys the entry must carry.
ROUTE_KEYS = ("tools", "ambientContext", "telemetry", "stateLocation",
              "acceptanceCheck", "fallback", "egressRecordFit")
#: RFC2-23's six states; "Missing quantity" is the one for absent tokens or cost.
DEGRADATION = {"Observer failed", "Source unreachable", "Partial snapshot",
               "Excluded content", "Consent withdrawn", "Missing quantity"}
#: RFC2-24's closed twelve reasons.
REASONS = {"missing-declaration", "missing-evidence", "no-currency-bound-declared",
           "stale-beyond-currency-bound", "mapping-coverage-absent",
           "unconsented-source-or-provider", "excluded-content",
           "contradicted-pending-adjudication", "challenge-suspended",
           "source-uncaptured-or-unreachable", "reference-unresolvable",
           "execution-blocked"}
CLASSES = {"capture", "derivation-deterministic"}
EGRESS_SOURCE = re.compile(r"record PUBLIC-EGRESS-anthropic .*version \d+\.\d+\.\d+-candidate\.\d+")
EGRESS_BLOB = "57f11a71e944e94f640f1748358e76faba49ae90"
ACCEPTANCE = ("byte for byte", "requestBytes", "in neither fails")
#: Request fields the entry must pin itself, so the acceptance admits no profile-set byte.
PINNED = ("model", "tools", "effort", "thinking", "maxTokensCeiling")
SDK_PIN = ("@anthropic-ai/sdk", "0.131.0")
ENV_VAR = "SYZYGY_POLARIS_PROVIDER_API_KEY"
GATE_RULES = ("permitted()", "explicit upstream", "403")
REQUEST_KEYS = ("provenance", "pinnedVersions", "endpoint", "bodyFields", "generatorBuilt",
                "sdkFixed", "runtimeFixed", "routeFixedByThisEntry", "headers", "probe",
                "absentByConstruction", "unlistedBytes")
FIT_KEYS = ("fitsWithoutNewVersion", "needsReading", "conclusion")
#: The header table of acceptMessagesApiRequest at the cited commit, as values: the
#: entry must equal these, not merely name them (a presence-only check passed a
#: wrong literal in the sibling package's round 3).
EXPECTED_LITERALS = {
    "accept": "application/json", "content-type": "application/json",
    "anthropic-version": "2023-06-01", "user-agent": "Anthropic/JS 0.131.0",
    "accept-language": "*", "sec-fetch-mode": "cors", "x-stainless-lang": "js",
    "x-stainless-package-version": "0.131.0", "x-stainless-retry-count": "0",
    "x-stainless-runtime": "node", "x-stainless-helper-method": "stream",
    "x-stainless-timeout": "600"}
EXPECTED_SHAPES = {
    "x-stainless-os": "^[A-Za-z]{1,16}$", "x-stainless-arch": "^[a-z0-9_]{1,16}$",
    "x-stainless-runtime-version": "^v\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$",
    "accept-encoding": "^[a-z, ]{1,40}$"}
EXPECTED_RULES = {"x-api-key", "content-length", "host", "connection"}
EXPECTED_CLOSED = sorted(set(EXPECTED_LITERALS) | set(EXPECTED_SHAPES) | EXPECTED_RULES)
HEADERS_ABSENT = ("anthropic-beta", "authorization", "cookie", "claude-cli", "agent-sdk",
                  "x-app", "anthropic-dangerous-direct-browser-access", "x-claude-code-session-id")
HEADER_KEYS = ("pinnedLiterals", "shapes", "valueRules", "closedSet", "unlisted", "machineFingerprint")
#: Files the provenance must pin: the adapter that holds the header table, the gate, the bytes note.
PROVENANCE_FILES = ("packages/polaris-generation-provider/src/messages-api-provider.ts",
                    "packages/polaris-generation-provider/src/egress-gate.ts",
                    "docs/polaris-generation/PROVIDER-EGRESS-BYTES.md")
ACCEPT_CLAUSE = "admits no profile-set byte beyond the values this entry pins"
SHA1 = re.compile(r"[0-9a-f]{40}")


def repo_blob(commit, path):
    """The blob id of `path` at `commit`, or None when the commit is not in the local store."""
    try:
        return subprocess.run(["git", "rev-parse", f"{commit}:{path}"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def sha(data):
    return hashlib.sha256(data).hexdigest()


def proposed(root=PKG):
    return sorted((root / "proposed").glob("*.json"))


def findings_for(name, doc, butlers_contract, sibling=None):
    out = []
    if doc.get("status") != "candidate-entry-no-effect-until-owner-act":
        out.append(f"{name}: status is not the candidate label")
    if len(doc.get("entries", [])) != 1:
        return out + [f"{name}: not exactly one entry"]
    e = doc["entries"][0]
    for k in REQUIRED:
        if k not in e:
            out.append(f"{name}: missing RFC4-2 declaration {k}")
    ta = e.get("typedAuthority", {})
    rc = e.get("routeConditions", {})
    rb = e.get("requestBytes", {})
    outputs = {c.get("class") for c in e.get("outputFactClasses", [])}
    inputs = {c.get("class") for c in e.get("inputClasses", [])}
    if e.get("implementationVersion") is not None:
        out.append(f"{name}: implementationVersion must stay null until implemented")
    if ta.get("writeSurface") != []:
        out.append(f"{name}: writeSurface must be empty")
    if ta.get("workingTreeRead") is not False:
        out.append(f"{name}: workingTreeRead must be false")
    if ta.get("executeObservedCode") is not False:
        out.append(f"{name}: executeObservedCode must be false")
    if ta.get("authorityType") != "model-provider":
        out.append(f"{name}: authorityType is not model-provider")
    if e.get("subject") != {"observingProject": "project:syzygy", "provider": "provider:anthropic"}:
        out.append(f"{name}: subject is not (project:syzygy, provider:anthropic)")
    if e.get("determinismClass") not in CLASSES:
        out.append(f"{name}: determinismClass outside RFC4-2")
    by_class = e.get("determinismByOutputClass", {})
    if set(by_class) != outputs or not set(by_class.values()) <= CLASSES:
        out.append(f"{name}: determinismByOutputClass does not cover each output class once")
    if e.get("contractVersion") != butlers_contract:
        out.append(f"{name}: contractVersion differs from the adopted Butlers entry's")
    if e.get("adoptionStatus") != "candidate-entry-unadopted":
        out.append(f"{name}: adoptionStatus is not candidate-entry-unadopted")
    for key, state in e.get("failureStates", {}).items():
        if not isinstance(state, dict):
            continue
        if "degradationState" in state and state["degradationState"] not in DEGRADATION:
            out.append(f"{name}: failure state {key} names a degradation state outside the set")
        if "degradationState" not in state and "executionFact" not in state:
            out.append(f"{name}: failure state {key} names neither a degradation state nor an execution fact")
        reason = state.get("unknownReason", "")
        if not any(reason == r or reason.startswith(r + " ") or f" {r}" in reason for r in REASONS):
            out.append(f"{name}: failure state {key} names a reason outside RFC2-24")
    if "determinismClassNote" not in e:
        out.append(f"{name}: scalar determinismClass is unexplained")
    if not isinstance(e.get("snapshotInputMapping"), dict):
        out.append(f"{name}: snapshotInputMapping is not a per-class mapping")
    else:
        unmapped = inputs - set(e["snapshotInputMapping"])
        if unmapped:
            out.append(f"{name}: snapshotInputMapping omits input classes {sorted(unmapped)}")
    if e.get("supersession") is None:
        out.append(f"{name}: supersession statement missing")
    for k in ROUTE_KEYS:
        if k not in rc:
            out.append(f"{name}: routeConditions lacks {k}")
    if ta.get("toolInvocation") != []:
        out.append(f"{name}: toolInvocation must be empty")
    pin = e.get("runtimePin", {})
    if (pin.get("package"), pin.get("version")) != SDK_PIN or pin.get("bundledCli") is not None:
        out.append(f"{name}: runtimePin is not the measured SDK version")
    if not EGRESS_SOURCE.search(rc.get("source", "")) or EGRESS_BLOB not in rc.get("source", ""):
        out.append(f"{name}: routeConditions.source names no egress record ID, version and blob")
    if ACCEPT_CLAUSE not in rc.get("acceptanceCheck", ""):
        out.append(f"{name}: acceptanceCheck does not end on the clause admitting no profile-set byte beyond the pins")
    if not all(w in rc.get("acceptanceCheck", "") for w in ACCEPTANCE):
        out.append(f"{name}: acceptanceCheck does not require generator parts byte for byte and the listed bytes")
    if not str(rc.get("fallback", "")).startswith("none"):
        out.append(f"{name}: fallback must be none")
    fit = rc.get("egressRecordFit", {})
    for k in FIT_KEYS:
        if not fit.get(k):
            out.append(f"{name}: egressRecordFit lacks {k}")
    if "Agent SDK" not in " ".join(fit.get("needsReading", [])):
        out.append(f"{name}: egressRecordFit does not disclose the record's Agent SDK route wording")
    for k in REQUEST_KEYS:
        if k not in rb:
            out.append(f"{name}: requestBytes lacks {k}")
    for k in PINNED:
        if k not in rb.get("routeFixedByThisEntry", {}):
            out.append(f"{name}: routeFixedByThisEntry does not pin {k}")
    fixed = rb.get("routeFixedByThisEntry", {})
    if fixed.get("model") != "claude-opus-5-5":
        out.append(f"{name}: model is not pinned to claude-opus-5-5")
    if not str(fixed.get("effort", "")).startswith("high"):
        out.append(f"{name}: effort is not pinned to high")
    if not str(fixed.get("tools", "")).startswith("absent"):
        out.append(f"{name}: tools must be absent")
    if "64000" not in str(fixed.get("maxTokensCeiling", "")) or "[Inferred" not in str(fixed.get("maxTokensCeiling", "")):
        out.append(f"{name}: maxTokensCeiling is not the labelled 64000 proposal")
    thinking = str(fixed.get("thinking", ""))
    if not ("off" in thinking and "adaptive" in thinking and "not a permitted" in thinking):
        out.append(f"{name}: thinking is not pinned to off or adaptive with other values refused")
    if (rb.get("pinnedVersions", {}).get("package"), rb.get("pinnedVersions", {}).get("version")) != SDK_PIN:
        out.append(f"{name}: requestBytes pins other versions than runtimePin")
    hd = rb.get("headers", {})
    if not isinstance(hd, dict) or any(k not in hd for k in HEADER_KEYS):
        out.append(f"{name}: headers lacks one of {HEADER_KEYS}")
    else:
        if hd["pinnedLiterals"] != EXPECTED_LITERALS:
            out.append(f"{name}: headers.pinnedLiterals differ from the cited table")
        if hd["shapes"] != EXPECTED_SHAPES:
            out.append(f"{name}: headers.shapes differ from the cited table")
        if set(hd["valueRules"]) != EXPECTED_RULES:
            out.append(f"{name}: headers.valueRules cover other headers than the cited table")
        if hd["closedSet"] != EXPECTED_CLOSED:
            out.append(f"{name}: headers.closedSet is not the closed header set")
        rules = hd["valueRules"]
        if "configured credential" not in rules.get("x-api-key", "") or "never recorded" not in rules.get("x-api-key", ""):
            out.append(f"{name}: x-api-key rule does not bind the configured credential and say it is never recorded")
        if "there is no open class" not in hd["unlisted"]:
            out.append(f"{name}: headers.unlisted admits an open class of headers")
        listed = json.dumps(hd["pinnedLiterals"]) + json.dumps(hd["closedSet"])
        for h in HEADERS_ABSENT:
            if h in listed:
                out.append(f"{name}: headers list admits {h}")
    for k in ("model", "max_tokens", "output_config"):
        if k not in str(rb.get("bodyFields", "")):
            out.append(f"{name}: bodyFields does not name {k}")
    if "no tools" not in str(rb.get("bodyFields", "")):
        out.append(f"{name}: bodyFields does not exclude tools")
    prov = rb.get("provenance", {})
    if not isinstance(prov, dict) or not SHA1.fullmatch(str(prov.get("commit", ""))):
        out.append(f"{name}: provenance names no 40-hex commit")
    else:
        files = prov.get("files", [])
        if sorted(f.get("path") for f in files) != sorted(PROVENANCE_FILES):
            out.append(f"{name}: provenance files are not the adapter, the gate and the bytes note")
        for f in files:
            if not SHA1.fullmatch(str(f.get("blob", ""))):
                out.append(f"{name}: provenance blob for {f.get('path')} is not 40-hex")
            elif repo_blob(prov["commit"], str(f.get("path"))) not in (None, f["blob"]):
                out.append(f"{name}: provenance blob for {f.get('path')} is not the file at the commit")
    if not str(rb.get("probe", "")).startswith("none"):
        out.append(f"{name}: the route sends no probe")
    if "requestBytes" not in ta.get("readAuthority", ""):
        out.append(f"{name}: readAuthority does not point at requestBytes")
    if len(ta.get("networkAccess", [])) != 1:
        out.append(f"{name}: provider networkAccess must be exactly one destination")
    if "model-identity" not in outputs:
        out.append(f"{name}: outputFactClasses lacks model-identity")
    if "runtime-version-and-configuration" not in inputs:
        out.append(f"{name}: inputClasses lacks runtime-version-and-configuration")
    if "api-key-credential" not in inputs or "owner-sign-in-credential" in inputs:
        out.append(f"{name}: credential must be the API key class only")
    cred = ta.get("credential", {})
    if not str(cred.get("kind", "")).startswith("API key only"):
        out.append(f"{name}: credential is not API key only")
    if cred.get("source", "").count(ENV_VAR) != 1 or "one environment variable" not in cred.get("source", ""):
        out.append(f"{name}: credential is not read from one named environment variable")
    named = re.search(r"one environment variable, ([A-Z0-9_]+)", cred.get("source", ""))
    if (named is None or named.group(1).startswith("ANTHROPIC_")
            or "ambient-environment" not in cred.get("source", "")):
        out.append(f"{name}: credential variable is not outside the ANTHROPIC_ prefix the adapter refuses")
    for k in ("neverLogged", "disclosure", "refresh"):
        if k not in cred:
            out.append(f"{name}: credential lacks {k}")
    if "never written" not in cred.get("neverLogged", ""):
        out.append(f"{name}: credential does not say the key is never logged")
    gate = ta.get("runtimeEgressGate", {})
    rules = " ".join(gate.get("rules", []))
    for w in GATE_RULES:
        if w not in rules:
            out.append(f"{name}: runtimeEgressGate rules lack {w}")
    if "writeSurfaceArgument" not in ta:
        out.append(f"{name}: writeSurface is not argued")
    if "[Unknown]" not in " ".join(e.get("unknowns", [])):
        out.append(f"{name}: unknowns lists no Unknown")
    sub = e.get("routeSubstitution", {})
    if sub.get("substitutes") != SIBLING_IMPL:
        out.append(f"{name}: routeSubstitution does not name the Agent SDK implementation it substitutes")
    if e.get("observerId") != SIBLING_ID or sub.get("sharedRoleIdentity") != SIBLING_ID:
        out.append(f"{name}: the role identity is not the sibling's (RFC4-9: the role persists)")
    if e.get("implementationId") == SIBLING_IMPL or not e.get("implementationId"):
        out.append(f"{name}: no new implementation identity is registered (RFC4-9)")
    if sub.get("authorityKey") != AUTHORITY_KEY:
        out.append(f"{name}: routeSubstitution.authorityKey differs from the shared authority")
    if "RFC4-1" not in sub.get("rule", "") or "never an addition" not in sub.get("rule", "") or "RFC4-9" not in sub.get("rule", ""):
        out.append(f"{name}: routeSubstitution does not say it is an RFC4-9 substitute, never an addition")
    if "the role identity persists, a new implementation identity is registered" not in sub.get("rfc4-9", ""):
        out.append(f"{name}: routeSubstitution does not quote RFC4-9")
    if not sub.get("onlyOneAdoptable") or not sub.get("ifTheOtherWasAdoptedFirst"):
        out.append(f"{name}: routeSubstitution lacks onlyOneAdoptable or what retires the other")
    env = ta.get("sdkEnvironmentInputs", {})
    listed = {v.get("name"): v for v in env.get("variables", []) if isinstance(v, dict)}
    for var in ENV_INPUTS:
        if var not in listed:
            out.append(f"{name}: sdkEnvironmentInputs omits {var}")
        elif "unset" not in listed[var].get("posture", "") and "refuse" not in listed[var].get("posture", ""):
            out.append(f"{name}: sdkEnvironmentInputs gives {var} no fail-closed posture")
    if "ambient-environment" not in env.get("enforcement", "") or "[Inferred]" not in env.get("enforcement", ""):
        out.append(f"{name}: sdkEnvironmentInputs does not label its enforcement point")
    if "sdk-environment-variables" not in inputs or "sdk-environment-variables" not in e.get("snapshotInputMapping", {}):
        out.append(f"{name}: the SDK environment is not a declared, mapped input class")
    net = ta.get("networkAccess", [])
    if len(net) == 1 and not net[0].startswith(UPSTREAM + "/v1/messages, POST only"):
        out.append(f"{name}: networkAccess does not name the exact https destination")
    if f"upstream must equal {UPSTREAM}" not in rules:
        out.append(f"{name}: runtimeEgressGate does not bind the upstream to {UPSTREAM}")
    words = NUMBER_WORDS.get(len(fit.get("needsReading", [])))
    if words is None or f"{words} wordings" not in fit.get("conclusion", ""):
        out.append(f"{name}: egressRecordFit conclusion does not count the wordings in needsReading")
    rf = " ".join(rb.get("runtimeFixed", []))
    if "fetch" not in rf or "not pinned" not in rf:
        out.append(f"{name}: runtimeFixed does not disclose the Node fetch headers and the unpinned Node")
    if sibling is not None:
        se = sibling["entries"][0]
        if se.get("subject") != e.get("subject"):
            out.append(f"{name}: subject differs from the sibling entry's")
        if se.get("typedAuthority", {}).get("authorityType") != ta.get("authorityType"):
            out.append(f"{name}: authorityType differs from the sibling entry's")
        if se.get("observerId") != e.get("observerId"):
            out.append(f"{name}: the role identity differs from the sibling entry's")
        if se.get("implementationId") == e.get("implementationId"):
            out.append(f"{name}: implementationId equals the sibling's")
        if se.get("contractVersion") != e.get("contractVersion"):
            out.append(f"{name}: contractVersion differs from the sibling entry's")
    return out


def manifest_text(root=PKG):
    rows = sorted((f"{root.as_posix()}/proposed/{p.name}", sha(p.read_bytes())) for p in proposed(root))
    return ("# MESSAGES API PROVIDER ROUTE REGISTRY ENTRY MANIFEST\n"
            "# Candidate; this file and its row bind nothing by themselves.\n"
            f"# {len(rows)} artifact; each row hashes the proposed file's exact bytes and is\n"
            "# the argument of one owner act. A substitute for the Agent SDK entry; the\n"
            "# two are never both adopted (RFC4-1).\n"
            + "".join(f"{s}  {p}\n" for p, s in rows))


def check(root=PKG, butlers=BUTLERS, installed=INSTALLED, sibling_file=SIBLING_FILE):
    out = []
    contract = json.loads(butlers.read_text())["entries"][0]["contractVersion"]
    sibling = json.loads(sibling_file.read_text()) if sibling_file.is_file() else None
    files = proposed(root)
    if len(files) != 1 or files[0].name != ENTRY:
        out.append(f"expected the one proposed entry {ENTRY}, found {[p.name for p in files]}")
    for p in files:
        try:
            doc = json.loads(p.read_text())
        except ValueError as exc:
            out.append(f"{p.name}: not JSON ({exc})")
            continue
        out += findings_for(p.name, doc, contract, sibling)
        if (installed / p.name).exists():
            out.append(f"{p.name}: candidate bytes already sit in the installed home")
    for md in sorted(root.glob("*.md")):
        if HEX64.search(md.read_text()):
            out.append(f"{md.name}: carries a 64-hex token")
    m = root / MANIFEST
    if not m.is_file() or m.read_text() != manifest_text(root):
        out.append(f"{MANIFEST}: stale or missing")
    return out


def selftest():
    import tempfile
    contract = json.loads(BUTLERS.read_text())["entries"][0]["contractVersion"]
    prov = json.loads((PKG / "proposed" / ENTRY).read_text())
    pe = prov["entries"][0]

    def sibdoc(**over):
        base = {"observerId": SIBLING_ID, "implementationId": SIBLING_IMPL, "subject": pe["subject"],
                "contractVersion": pe["contractVersion"], "typedAuthority": {"authorityType": "model-provider"}}
        base.update(over)
        return {"entries": [base]}
    sib = sibdoc()
    assert not findings_for("p", prov, contract, sib)
    muts = []

    def mut(name, fn, needle, sibling=sib):
        d = copy.deepcopy(prov)
        fn(d["entries"][0], d)
        muts.append((name, any(needle in f for f in findings_for("m", d, contract, sibling))))

    mut("status upgraded", lambda e, d: d.update(status="adopted"), "status")
    mut("adoptionStatus adopted", lambda e, d: e.update(adoptionStatus="adopted"), "adoptionStatus")
    mut("invented version", lambda e, d: e.update(implementationVersion="1.0.0"), "implementationVersion")
    mut("write surface granted", lambda e, d: e["typedAuthority"].update(writeSurface=["x"]), "writeSurface")
    mut("observed code executed", lambda e, d: e["typedAuthority"].update(executeObservedCode=True), "executeObservedCode")
    mut("working tree read", lambda e, d: e["typedAuthority"].update(workingTreeRead=True), "workingTreeRead")
    mut("authority type changed", lambda e, d: e["typedAuthority"].update(authorityType="vcs"), "authorityType")
    mut("subject changed", lambda e, d: e.update(subject={"observingProject": "project:x", "provider": "provider:anthropic"}), "subject")
    mut("wrong determinism class", lambda e, d: e.update(determinismClass="live"), "determinismClass")
    mut("per-class determinism dropped", lambda e, d: e.pop("determinismByOutputClass"), "determinismByOutputClass")
    mut("contract version drift", lambda e, d: e.update(contractVersion="sha256:0"), "contractVersion")
    mut("two entries", lambda e, d: d["entries"].append(e), "not exactly one")
    mut("network widened", lambda e, d: e["typedAuthority"]["networkAccess"].append("elsewhere"), "networkAccess")
    mut("supersession dropped", lambda e, d: e.pop("supersession"), "supersession")
    mut("snapshot mapping dropped", lambda e, d: e.pop("snapshotInputMapping"), "snapshotInputMapping")
    mut("input class unmapped", lambda e, d: e["snapshotInputMapping"].pop("run-budget"), "omits input classes")
    mut("degradation state invented", lambda e, d: next(v for v in e["failureStates"].values() if isinstance(v, dict) and "degradationState" in v).update(degradationState="Fine"), "degradation state")
    mut("reason outside RFC2-24", lambda e, d: next(v for v in e["failureStates"].values() if isinstance(v, dict)).update(unknownReason="made-up"), "RFC2-24")
    mut("state names neither state nor fact", lambda e, d: e["failureStates"].update(x={"unknownReason": "excluded-content"}), "neither a degradation state")
    for k in REQUIRED:
        mut(f"declaration {k} dropped", lambda e, d, k=k: e.pop(k), "missing RFC4-2")
    for k in ROUTE_KEYS:
        mut(f"route condition {k} dropped", lambda e, d, k=k: e["routeConditions"].pop(k), "routeConditions")
    mut("tool invocation allowed", lambda e, d: e["typedAuthority"].update(toolInvocation=["bash"]), "toolInvocation")
    mut("SDK pin drift", lambda e, d: e["runtimePin"].update(version="0.131.1"), "runtimePin")
    mut("bundled CLI invented", lambda e, d: e["runtimePin"].update(bundledCli="2.1.288"), "runtimePin")
    mut("request bytes pin other version", lambda e, d: e["requestBytes"]["pinnedVersions"].update(version="0.131.1"), "other versions")
    mut("egress record unnamed", lambda e, d: e["routeConditions"].update(source="instances/egress-anthropic"), "egress record ID")
    mut("egress blob dropped", lambda e, d: e["routeConditions"].update(source=e["routeConditions"]["source"].replace(EGRESS_BLOB, "")), "egress record ID")
    mut("egress version dropped", lambda e, d: e["routeConditions"].update(source="record PUBLIC-EGRESS-anthropic, any version " + EGRESS_BLOB), "egress record")
    mut("fallback allowed", lambda e, d: e["routeConditions"].update(fallback="the Agent SDK route"), "fallback")
    mut("acceptance admits any byte", lambda e, d: e["routeConditions"].update(acceptanceCheck="any byte passes"), "acceptanceCheck")
    mut("fit conclusion dropped", lambda e, d: e["routeConditions"]["egressRecordFit"].pop("conclusion"), "egressRecordFit lacks")
    mut("fit hides the Agent SDK wording", lambda e, d: e["routeConditions"]["egressRecordFit"].update(needsReading=["none"]), "Agent SDK route wording")
    mut("model identity dropped", lambda e, d: e["outputFactClasses"].pop(3) and e["determinismByOutputClass"].pop("model-identity"), "model-identity")
    mut("runtime version input dropped", lambda e, d: e["inputClasses"].remove(next(c for c in e["inputClasses"] if c["class"] == "runtime-version-and-configuration")), "runtime-version")
    mut("sign-in credential admitted", lambda e, d: e["inputClasses"].append({"class": "owner-sign-in-credential", "identityScheme": "x"}), "credential must be the API key class")
    mut("credential not API key only", lambda e, d: e["typedAuthority"]["credential"].update(kind="API key or subscription login"), "API key only")
    mut("credential env var unnamed", lambda e, d: e["typedAuthority"]["credential"].update(source="the environment"), "named environment variable")
    mut("credential second env var", lambda e, d: e["typedAuthority"]["credential"].update(source=e["typedAuthority"]["credential"]["source"] + " or " + ENV_VAR), "named environment variable")
    mut("credential logging unsaid", lambda e, d: e["typedAuthority"]["credential"].pop("neverLogged"), "credential lacks")
    mut("credential logged", lambda e, d: e["typedAuthority"]["credential"].update(neverLogged="written to the log"), "never logged")
    mut("gate consent rule dropped", lambda e, d: e["typedAuthority"]["runtimeEgressGate"].update(rules=[r.replace("permitted()", "") for r in e["typedAuthority"]["runtimeEgressGate"]["rules"]]), "runtimeEgressGate rules lack")
    mut("gate refusal dropped", lambda e, d: e["typedAuthority"]["runtimeEgressGate"].update(rules=[r.replace("403", "200") for r in e["typedAuthority"]["runtimeEgressGate"]["rules"]]), "runtimeEgressGate rules lack")
    mut("gate dropped", lambda e, d: e["typedAuthority"].pop("runtimeEgressGate"), "runtimeEgressGate rules lack")
    mut("write surface unargued", lambda e, d: e["typedAuthority"].pop("writeSurfaceArgument"), "not argued")
    mut("unknowns emptied", lambda e, d: e.update(unknowns=[]), "lists no Unknown")
    mut("readAuthority stops pointing at requestBytes", lambda e, d: e["typedAuthority"].update(readAuthority="none"), "readAuthority")
    for k in REQUEST_KEYS:
        mut(f"requestBytes {k} dropped", lambda e, d, k=k: e["requestBytes"].pop(k), "requestBytes lacks")
    for k in PINNED:
        mut(f"{k} unpinned", lambda e, d, k=k: e["requestBytes"]["routeFixedByThisEntry"].pop(k), "does not pin")
    mut("model changed", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(model="claude-sonnet-5-5"), "model is not pinned")
    mut("effort changed", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(effort="max"), "effort is not pinned")
    mut("tools present", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(tools="[]"), "tools must be absent")
    mut("max_tokens ceiling unlabelled", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(maxTokensCeiling="64000"), "maxTokensCeiling")
    mut("max_tokens ceiling changed", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(maxTokensCeiling="[Inferred] 128000"), "maxTokensCeiling")
    mut("thinking budget admitted", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(thinking="off, adaptive or enabled with budget_tokens"), "thinking is not pinned")
    mut("thinking adaptive dropped", lambda e, d: e["requestBytes"]["routeFixedByThisEntry"].update(thinking="off; any other value is not a permitted configuration"), "thinking is not pinned")
    def hdr(e):
        return e["requestBytes"]["headers"]
    mut("beta header admitted", lambda e, d: hdr(e)["pinnedLiterals"].update({"anthropic-beta": "x"}), "pinnedLiterals differ")
    mut("beta header in closed set", lambda e, d: hdr(e)["closedSet"].append("anthropic-beta"), "closedSet")
    mut("agent sdk user agent", lambda e, d: hdr(e)["pinnedLiterals"].update({"user-agent": "claude-cli/2.1.288 (agent-sdk)"}), "pinnedLiterals differ")
    mut("literal value drifts", lambda e, d: hdr(e)["pinnedLiterals"].update({"anthropic-version": "2024-01-01"}), "pinnedLiterals differ")
    mut("literal dropped", lambda e, d: hdr(e)["pinnedLiterals"].pop("sec-fetch-mode"), "pinnedLiterals differ")
    mut("sdk version literal drifts", lambda e, d: hdr(e)["pinnedLiterals"].update({"x-stainless-package-version": "0.131.1"}), "pinnedLiterals differ")
    mut("shape loosened", lambda e, d: hdr(e)["shapes"].update({"x-stainless-os": ".*"}), "shapes differ")
    mut("shape dropped", lambda e, d: hdr(e)["shapes"].pop("x-stainless-arch"), "shapes differ")
    mut("value rule dropped", lambda e, d: hdr(e)["valueRules"].pop("host"), "valueRules")
    mut("value rule added", lambda e, d: hdr(e)["valueRules"].update({"cookie": "any"}), "valueRules")
    mut("api key rule unbound", lambda e, d: hdr(e)["valueRules"].update({"x-api-key": "any non-empty value"}), "x-api-key rule")
    mut("closed set widened", lambda e, d: hdr(e)["closedSet"].append("x-extra"), "closedSet")
    mut("closed set narrowed", lambda e, d: hdr(e)["closedSet"].remove("host"), "closedSet")
    mut("open header class admitted", lambda e, d: hdr(e).update(unlisted="transport headers are not checked"), "open class")
    for k in ("pinnedLiterals", "shapes", "valueRules", "closedSet", "unlisted", "machineFingerprint"):
        mut(f"headers key {k} dropped", lambda e, d, k=k: hdr(e).pop(k), "headers lacks")
    mut("headers back to a list", lambda e, d: e["requestBytes"].update(headers=["x-api-key"]), "headers lacks")
    mut("body fields drop tools exclusion", lambda e, d: e["requestBytes"].update(bodyFields="max_tokens, messages, model, output_config, stream, system"), "exclude tools")
    mut("body fields drop output_config", lambda e, d: e["requestBytes"].update(bodyFields="max_tokens, model, no tools"), "output_config")
    mut("acceptance admits profile-set bytes", lambda e, d: e["routeConditions"].update(acceptanceCheck=e["routeConditions"]["acceptanceCheck"].replace("admits no profile-set byte beyond the values this entry pins", "")), "admitting no profile-set")
    mut("credential variable under the refused prefix", lambda e, d: e["typedAuthority"]["credential"].update(source=e["typedAuthority"]["credential"]["source"].replace(ENV_VAR, "ANTHROPIC_API_KEY")), "ANTHROPIC_")
    mut("ambient guard unsaid", lambda e, d: e["typedAuthority"]["credential"].update(source=e["typedAuthority"]["credential"]["source"].replace("ambient-environment", "")), "ANTHROPIC_")
    mut("provenance commit dropped", lambda e, d: e["requestBytes"]["provenance"].pop("commit"), "40-hex commit")
    mut("provenance commit not hex", lambda e, d: e["requestBytes"]["provenance"].update(commit="main"), "40-hex commit")
    mut("provenance file dropped", lambda e, d: e["requestBytes"]["provenance"]["files"].pop(), "provenance files")
    mut("provenance blob not hex", lambda e, d: e["requestBytes"]["provenance"]["files"][0].update(blob="abc"), "40-hex")
    if repo_blob(prov["entries"][0]["requestBytes"]["provenance"]["commit"], PROVENANCE_FILES[0]) is not None:
        mut("provenance blob of another file", lambda e, d: e["requestBytes"]["provenance"]["files"][0].update(blob="0" * 40), "not the file at the commit")
        mut("provenance blob of the next commit", lambda e, d: e["requestBytes"]["provenance"]["files"][1].update(blob=e["requestBytes"]["provenance"]["files"][0]["blob"]), "not the file at the commit")
    mut("probe admitted", lambda e, d: e["requestBytes"].update(probe="after some failures a HEAD probe"), "no probe")
    mut("substitution unnamed", lambda e, d: e["routeSubstitution"].update(substitutes="something-else"), "substitutes")
    mut("role identity forked", lambda e, d: e.update(observerId="a-second-role"), "role identity is not the sibling's")
    mut("shared role identity unsaid", lambda e, d: e["routeSubstitution"].pop("sharedRoleIdentity"), "role identity is not the sibling's")
    mut("implementation identity reused", lambda e, d: e.update(implementationId=SIBLING_IMPL), "no new implementation identity")
    mut("RFC4-9 not quoted", lambda e, d: e["routeSubstitution"].pop("rfc4-9"), "quote RFC4-9")
    mut("RFC4-9 not cited", lambda e, d: e["routeSubstitution"].update(rule=e["routeSubstitution"]["rule"].replace("RFC4-9", "the rule")), "RFC4-9 substitute")
    mut("retirement unsaid", lambda e, d: e["routeSubstitution"].pop("ifTheOtherWasAdoptedFirst"), "what retires")
    mut("authority key drifts", lambda e, d: e["routeSubstitution"]["authorityKey"].update(provider="provider:other"), "authorityKey")
    mut("substitute said to be an addition", lambda e, d: e["routeSubstitution"].update(rule="a second adapter beside the first"), "substitute, never an addition")
    mut("only-one-adoptable dropped", lambda e, d: e["routeSubstitution"].pop("onlyOneAdoptable"), "onlyOneAdoptable")
    mut("subject differs from the sibling's", lambda e, d: None, "differs from the sibling", sibling=sibdoc(subject={"x": 1}))
    mut("authority type differs from the sibling's", lambda e, d: None, "authorityType differs", sibling=sibdoc(typedAuthority={"authorityType": "vcs"}))
    mut("sibling role renamed", lambda e, d: None, "role identity differs", sibling=sibdoc(observerId="renamed"))
    mut("sibling implementation id equals ours", lambda e, d: None, "implementationId equals", sibling=sibdoc(implementationId=pe["implementationId"]))
    mut("contract version differs from the sibling's", lambda e, d: None, "contractVersion differs from the sibling", sibling=sibdoc(contractVersion="sha256:0"))
    for var in ENV_INPUTS:
        mut(f"SDK environment input {var} dropped", lambda e, d, var=var: e["typedAuthority"]["sdkEnvironmentInputs"].update(variables=[v for v in e["typedAuthority"]["sdkEnvironmentInputs"]["variables"] if v["name"] != var]), "omits")
        mut(f"SDK environment input {var} left open", lambda e, d, var=var: [v.update(posture="allowed") for v in e["typedAuthority"]["sdkEnvironmentInputs"]["variables"] if v["name"] == var], "fail-closed posture")
    mut("SDK environment enforcement unlabelled", lambda e, d: e["typedAuthority"]["sdkEnvironmentInputs"].update(enforcement="enforced"), "enforcement point")
    mut("SDK environment class dropped", lambda e, d: e["inputClasses"].remove(next(c for c in e["inputClasses"] if c["class"] == "sdk-environment-variables")), "declared, mapped input class")
    mut("SDK environment mapping dropped", lambda e, d: e["snapshotInputMapping"].pop("sdk-environment-variables"), "declared, mapped input class")
    mut("destination without scheme", lambda e, d: e["typedAuthority"].update(networkAccess=["the Anthropic API host, POST /v1/messages only"]), "exact https destination")
    mut("destination over http", lambda e, d: e["typedAuthority"].update(networkAccess=[e["typedAuthority"]["networkAccess"][0].replace("https://", "http://")]), "exact https destination")
    mut("destination another host", lambda e, d: e["typedAuthority"].update(networkAccess=[e["typedAuthority"]["networkAccess"][0].replace("api.anthropic.com", "example.org")]), "exact https destination")
    mut("upstream rule dropped", lambda e, d: e["typedAuthority"]["runtimeEgressGate"].update(rules=[r for r in e["typedAuthority"]["runtimeEgressGate"]["rules"] if "upstream must equal" not in r]), "bind the upstream")
    mut("upstream rule names another host", lambda e, d: e["typedAuthority"]["runtimeEgressGate"].update(rules=[r.replace("upstream must equal https://api.anthropic.com", "upstream must equal http://x") for r in e["typedAuthority"]["runtimeEgressGate"]["rules"]]), "bind the upstream")
    mut("fit conclusion counts two", lambda e, d: e["routeConditions"]["egressRecordFit"].update(conclusion=e["routeConditions"]["egressRecordFit"]["conclusion"].replace("three wordings", "two wordings")), "count the wordings")
    mut("fit needsReading gains an item", lambda e, d: e["routeConditions"]["egressRecordFit"]["needsReading"].append("Agent SDK extra"), "count the wordings")
    mut("fit needsReading loses an item", lambda e, d: e["routeConditions"]["egressRecordFit"]["needsReading"].pop(), "count the wordings")
    mut("Node fetch headers undisclosed", lambda e, d: e["requestBytes"].update(runtimeFixed=["none"]), "Node fetch")
    mut("Node pinned by claim", lambda e, d: e["requestBytes"].update(runtimeFixed=["Node's built-in fetch sets accept-language"]), "Node fetch")
    for hname in EXPECTED_LITERALS:
        mut(f"literal {hname} drifts", lambda e, d, hname=hname: e["requestBytes"]["headers"]["pinnedLiterals"].update({hname: "x"}), "pinnedLiterals differ")
        mut(f"literal {hname} dropped", lambda e, d, hname=hname: e["requestBytes"]["headers"]["pinnedLiterals"].pop(hname), "pinnedLiterals differ")
    mut("timeout back to optional", lambda e, d: e["requestBytes"]["headers"]["valueRules"].update({"x-stainless-timeout": "optional"}), "valueRules")
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t) / "pkg"
        (root / "proposed").mkdir(parents=True)
        inst = pathlib.Path(t) / "installed"
        inst.mkdir()
        for p in proposed():
            (root / "proposed" / p.name).write_bytes(p.read_bytes())
        (root / MANIFEST).write_text(manifest_text(root))
        nosib = pathlib.Path(t) / "none.json"
        muts.append(("clean temp package passes", check(root, BUTLERS, inst, nosib) == []))
        victim = next(iter(proposed(root)))
        keep = victim.read_text()
        victim.write_text("{not json")
        muts.append(("proposed file not JSON", any("not JSON" in f for f in check(root, BUTLERS, inst, nosib))))
        victim.write_text(keep)
        victim.rename(victim.with_suffix(".moved"))
        muts.append(("proposed entry missing", any("expected the one" in f for f in check(root, BUTLERS, inst, nosib))))
        victim.with_suffix(".moved").rename(victim)
        (root / "proposed" / "EXTRA.json").write_text("{}")
        muts.append(("extra proposed entry", any("expected the one" in f for f in check(root, BUTLERS, inst, nosib))))
        (root / "proposed" / "EXTRA.json").unlink()
        (root / "X.md").write_text("a" * 64)
        muts.append(("hex token in package prose", any("64-hex" in f for f in check(root, BUTLERS, inst, nosib))))
        (root / "X.md").unlink()
        (root / MANIFEST).write_text(manifest_text(root).replace("1", "2", 1))
        muts.append(("stale manifest", any("stale" in f for f in check(root, BUTLERS, inst, nosib))))
        (root / MANIFEST).write_text(manifest_text(root))
        (inst / victim.name).write_text("{}")
        muts.append(("candidate installed early", any("installed home" in f for f in check(root, BUTLERS, inst, nosib))))
        (inst / victim.name).unlink()
        clash = pathlib.Path(t) / "sibling.json"
        clash.write_text(json.dumps({"status": "x", "entries": [{"observerId": SIBLING_ID, "subject": {"x": 1}, "typedAuthority": {"authorityType": "model-provider"}}]}))
        muts.append(("sibling file on disk is cross-checked", any("differs from the sibling" in f for f in check(root, BUTLERS, inst, clash))))
    bad = [n for n, ok in muts if not ok]
    for n, ok in muts:
        print(("ok   " if ok else "FAIL ") + n)
    print(f"selftest: {len(muts) - len(bad)} of {len(muts)} predicates held")
    return 1 if bad else 0


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return selftest()
    if mode == "--write":
        bad = [f for f in check() if MANIFEST not in f]
        if bad:
            print("\n".join(bad), file=sys.stderr)
            return 1
        (PKG / MANIFEST).write_text(manifest_text())
        print(f"wrote {PKG / MANIFEST}")
        return 0
    if mode in ("--check", "--digests", "--manifest-digest"):
        bad = check()
        if bad:
            for f in bad:
                print("FINDING", f)
            return 1
        if mode == "--digests":
            for p in proposed():
                print(f"{sha(p.read_bytes())}  {p}")
        elif mode == "--manifest-digest":
            print(sha((PKG / MANIFEST).read_bytes()))
        else:
            print("messages-api provider route entry: current")
        return 0
    print(f"unknown mode {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
