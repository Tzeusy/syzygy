#!/usr/bin/env python3
"""Estimate what the candidate PWB scoped-attributes amendment would save on a
retained /polaris capture, under the strict rule the candidate states for
PWB-REQ-007: a field is carried once on an enclosing scope only when every
claim under that scope has the same value in the machine answer; a scope
states its values as text once; claim identity and an Unknown reason's route
never move. Read-only over the capture files named on the command line; it
prints one JSON document naming each input by byte count and SHA-256.

Method. Every `<span class="claim-tuple">` is a claim's tuple. Its scope is
its nearest enclosing table or list element (`container` mode), or its
nearest enclosing section (`section` mode) falling back to the container.
For each scope and each of the seven tuple attributes, the field is hoisted
only when all tuples under the scope carry one value and the scope holds
more than one tuple. Bytes removed are the hoisted attributes' exact bytes
plus the hoisted text segments of the tuple's visible text (label, tier,
freshness, challenge joined by " · "; an Unknown reason's parenthetical stays
with the label). Bytes added, per scope that hoists anything, are one scope
marker attribute, the hoisted attributes once, and one caption element
stating the hoisted text once. Net saving = removed - added. The figure is an
estimate of one lawful implementation, not a measurement of a rendered page:
label it [Inferred] wherever it is quoted.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser

FIELDS = [
    "data-epistemic-label",
    "data-epistemic-tier",
    "data-epistemic-primary-reason",
    "data-epistemic-secondary-reasons",
    "data-epistemic-freshness",
    "data-challenge-state",
    "data-evaluation-id",
]
TEXT_FIELDS = {
    "data-epistemic-label": 0,
    "data-epistemic-tier": 1,
    "data-epistemic-freshness": 2,
    "data-challenge-state": 3,
}
CONTAINERS = {"table", "ul", "ol", "dl"}
VOID = {"br", "img", "input", "meta", "link", "hr", "wbr", "source"}


class TupleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.stack: list[tuple[str, dict[str, str | None], int]] = []
        self.tuples: list[dict] = []
        self.current: dict | None = None
        self.serial = 0

    def handle_starttag(self, tag, attrs):
        self.serial += 1
        node = (tag, dict(attrs), self.serial)
        self.stack.append(node)
        if tag == "span" and node[1].get("class") == "claim-tuple":
            self.current = {"attrs": node[1], "text": "", "ancestors": list(self.stack[:-1])}
        if tag in VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        top = self.stack[-1] if self.stack else None
        if self.current is not None and tag == "span" and top and top[0] == "span" and top[1].get("class") == "claim-tuple":
            self.tuples.append(self.current)
            self.current = None
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data

    def handle_entityref(self, name):
        if self.current is not None:
            self.current["text"] += f"&{name};"

    def handle_charref(self, name):
        if self.current is not None:
            self.current["text"] += f"&#{name};"


def scope_of(ancestors, mode: str) -> str:
    if mode == "section":
        for tag, attrs, serial in reversed(ancestors):
            if tag == "section" or "data-polaris-section" in attrs:
                return f"{tag}#{serial}"
    for tag, _attrs, serial in reversed(ancestors):
        if tag in CONTAINERS:
            return f"{tag}#{serial}"
    return "body"


def estimate(html: str, mode: str) -> dict:
    parser = TupleParser()
    parser.feed(html)
    groups: dict[str, list[dict]] = defaultdict(list)
    for item in parser.tuples:
        groups[scope_of(item["ancestors"], mode)].append(item)
    removed_attr = removed_text = added = 0
    scopes = 0
    hoisted: Counter = Counter()
    for members in groups.values():
        hoist = [f for f in FIELDS if len(members) > 1 and len({m["attrs"].get(f) for m in members}) == 1]
        if not hoist:
            continue
        scopes += 1
        value = {f: members[0]["attrs"].get(f) or "" for f in hoist}
        text_once = " · ".join(value[f] for f in FIELDS if f in TEXT_FIELDS and f in hoist)
        added += len(' data-claim-scope="1"') + sum(len(f' {f}="{value[f]}"') for f in hoist)
        added += len('<p class="claim-scope"></p>') + len(text_once)
        for member in members:
            for f in hoist:
                removed_attr += len(f' {f}="{member["attrs"].get(f) or ""}"')
                hoisted[f] += 1
            parts = member["text"].split(" · ")
            if len(parts) == 4:
                kept = [parts[i] for f, i in TEXT_FIELDS.items() if f not in hoist]
                removed_text += len(member["text"]) - len(" · ".join(kept))
    return {
        "mode": mode,
        "tuples": len(parser.tuples),
        "scopes": len(groups),
        "scopesHoistingSomething": scopes,
        "attributeBytesRemoved": removed_attr,
        "textBytesRemoved": removed_text,
        "scopeBytesAdded": added,
        "netSavingBytes": removed_attr + removed_text - added,
        "hoistedPerField": {f: hoisted[f] for f in FIELDS},
    }


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print("usage: estimate_pwb_scoped_attributes_saving.py <capture.html>...", file=sys.stderr)
        return 2
    out = {"rule": "strict: a scope carries a field only when every claim under it has that value", "captures": []}
    for path in argv:
        raw = open(path, "rb").read()
        html = raw.decode("utf-8")
        out["captures"].append({
            "path": path.rsplit("/", 1)[-1],
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "estimates": [estimate(html, "container"), estimate(html, "section")],
        })
    json.dump(out, sys.stdout, indent=1)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
