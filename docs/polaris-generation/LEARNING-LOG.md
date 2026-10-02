# Polaris learning log — how to build something great

Learning how to build a great manifesto site is half the point of this work,
not a side effect. This log keeps what we learn about that craft: what makes
a project page excellent, what our own attempts got wrong, and what it changes
in the generator, prompts, renderer or guidance.

It is working notes, not authority. Lessons that harden into rules move into
[AUTHORING.md](AUTHORING.md), the prompts or a validator, and the entry says
where they went. Tasks live in [TRACKER.md](TRACKER.md).

**Entry shape:** date · the lesson in one sentence · evidence (labelled) ·
what it changes · status (open / applied → where).

---

## 2026-10-03 — Studying the reference sites

First look at the three targets' own pages, before any generation run.
Observed with a web fetch of each page on 2026-10-03; structure only.

### L1. The thesis is one sentence, and it comes first

`requests.readthedocs.io` opens with "**Requests** is an elegant and simple
HTTP library for Python, built for human beings." — after the title and
version, before anything else [Observed]. Redis's get-started page opens with
one sentence naming what it is and five things people use it as [Observed].

- **Changes:** the plan pass must produce a one-sentence thesis as its first
  output, and the reader test should check that a reader can quote it after
  ten seconds.
- **Status:** open.

### L2. Show, then tell

requests puts a working, eight-line interactive session ("Behold, the power
of Requests") immediately after the thesis, then links to "similar code, sans
Requests" — a before/after argument made with code, not adjectives
[Observed]. The claim "elegant and simple" is never argued in prose; the
example argues it.

- **Changes:** the plan pass should look for the project's most persuasive
  concrete artifact (a snippet, a command, a diagram) and place it right after
  the thesis. An adjective in the thesis needs an artifact that earns it.
- **Status:** open.

### L3. The page routes by reader intent, in the reader's words

requests splits everything below the fold into four guides introduced by who
they are for — "If you are looking for information on a specific function…
this part of the documentation is for you" [Observed]. Redis routes by use
case ("Data structure store", "Vector database", "AI agents and chatbots") and
by deployment choice [Observed]. Sentry's developer docs route by subsystem
with a one-line purpose per card ("The monolith that is powering Sentry")
[Observed].

- **Changes:** reading depths (REQ-polaris-generation-004) should be labelled
  by reader intent, not by our internal tiers. Sentry's one line per subsystem
  is the shape a component deep dive's entry should take.
- **Status:** open.

### L4. Great pages are short at the top and deep below

Sentry's developer landing page is about 300 words [Inferred, from the fetch
summary]; requests' front page is one sentence, one example, one feature list
and a table of contents. Depth lives one click away, not on the first screen.

- **Changes:** this argues for a byte and word budget on the first reading
  level, with deep dives as separate pages. The Butlers page does the
  opposite (next entry).
- **Status:** open — feeds the performance-budget question in the tracker.

### L5. Personality is allowed

requests ends its table of contents with "There are no more guides. You are
now guideless. Good luck." [Observed]. A manifesto has a voice.

- **Changes:** the voice brief in the author pass should take the project's
  own voice from its sources rather than flatten it into neutral reference
  prose — while never inventing claims (the edit pass keeps qualifications).
- **Status:** open.

## Lessons carried from the Butlers page

These come from the 2026-09-22 vision pursuit
([report](../pursuits/2026-09-22-vision-pursuit.md), "Systemic themes" 1, 5
and 6).

### L6. Honesty applied per claim becomes noise

On the Butlers page, 718 identical epistemic tuples were about 53% of the
9,403 words readable in flow; the legend arrived at word 445, after hundreds
of uses [Observed in that report]. Every claim was labelled; the page became
hard to read.

- **Changes:** state the epistemic label once per region and mark only the
  exceptions (pursuit move N5). Honesty and readability are not a trade-off if
  the label lives at the right scope.
- **Status:** open.

### L7. A catalogue is not a manifesto

The Butlers page was 1.23× its sources' length with zero synthesis and zero
Inferred claims [Observed in that report]. Reproducing every declared item
faithfully answers "what exists" but never "why it matters".

- **Changes:** the generator's job is argument (REQ-polaris-generation-002)
  with the catalogue reachable as evidence, not the catalogue with prose on
  top. Compare L1–L4.
- **Status:** open.

### L8. One repository measures nothing about generality

Every measurement of the generator so far is on one repository; a profile
that passed its own census still failed on Syzygy's own document shapes
[Observed in that report].

- **Changes:** this is why the [open-source targets](TARGETS.md) exist.
- **Status:** applied → TARGETS.md.
