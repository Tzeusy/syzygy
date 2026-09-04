# Owner packet — the Polaris cold-open walkthrough (task 4.6)

Status: candidate packet. It binds nothing. It asks you for one thing you
alone can do: read Polaris cold and say, in your own words, what Butlers is.
Your judgment on that reading is an owner act; this packet prepares the
ground for it and performs nothing.

## What you are being asked, in one paragraph

Start the proof-of-concept daemon, open the Polaris page, and read it the
way someone who has never seen the Butlers repository would — keyboard only,
no mouse, no peeking at the repository or at Syzygy's own documents first.
Then answer nine prompts in your own words and tell me which pages you
visited. I write that down as the execution record. Separately, you decide
whether the walkthrough met its criterion and say why; that decision becomes
a judgment file, and you perform one act on that file's exact digest. Until
both exist, Syzygy reports the walkthrough as Unknown, never met.

## Before you start

- Do not read the Butlers repository or Syzygy's plan, spec or review files
  first. The point is a cold read (VIS-3's independence standard).
- Use the keyboard only: Tab and Shift+Tab to move, Enter to follow a link,
  the skip link at the top of each page to jump to content. This run is the
  keyboard-only run PWB-REQ-016 requires.
- Start the daemon from a checkout of `main` in a terminal:

```text
npm run poc -- --repo /home/tze/GitHub/butlers
```

  It prints the address (a loopback port) and the observed Butlers revision.
  Open the address in a browser and press Tab to reach the Polaris link.

## The nine prompts

Answer each one in your own words from Polaris alone. Where you cannot
answer, say so — "Polaris did not tell me" is a valid, useful answer.

From RFC7-30, the cold-open comprehension walkthrough:

1. Why does Butlers exist?
2. What does it promise?
3. What does it refuse to be? Name at least one non-goal and reach the text
   of its rule.
4. What are its major capabilities, and how do they fit together?
5. Where does exactness live? Reach one verbatim requirement, and say where
   you found it.
6. What is one thing the project does not currently know about itself — one
   Unknown or contradiction — and how did the surface show it to you?

From PWB-REQ-021, the two project-wide additions plus the strength prompt:

7. Explain Butlers' major architecture and its capability groups.
8. What are its V1 success criteria?
9. Pick one fact Polaris states. How strongly does Polaris claim to know it,
   and what would make that claim stronger?

## What to send back

Reply in the chat with:

- your nine answers, in your own words;
- the pages you visited, in order (for example: home, then Polaris, then
  back to Polaris);
- a sentence confirming you used the keyboard only, or saying where you did
  not;
- anything that confused you or felt wrong. Those become recorded findings
  for the review cycle, whatever the verdict.

## What happens next, and who does what

1. **I write the execution record** from your reply, at the fixed path
   .syzygy/governance/records/PWB-WALKTHROUGH-001.md, with the identity
   PWB-WALKTHROUGH-001, the surface version, an evaluation slug for the
   daemon run you read, the keyboard-only flag and your traversed paths. It
   holds only your answers and those fields. I commit it, and I set the
   same evaluation slug in the implementation's expectation table so the
   daemon can evaluate the pair.
2. **You decide the verdict.** The criterion is
   polaris-cold-open-comprehension. It is met when every prompt was
   answered from Polaris without a confident error the surface caused, and
   you could explain Butlers as a whole, reach exact intent, and point at a
   visible Unknown. It is not met otherwise. Tell me "met" or "not met" and
   your reasons in a few sentences.
3. **I draft the judgment file** from your words at
   .syzygy/governance/decisions/PWB-COLD-OPEN-WALKTHROUGH-JUDGMENT-001.md:
   date, judging party (you), the verdict, the exact run record it judges
   (identity plus SHA-256), and your rationale. I compute its SHA-256 and
   offer you one phrase of the form
   ADOPT POLARIS COLD-OPEN WALKTHROUGH JUDGMENT: followed by that digest.
4. **You perform the act** by writing that exact phrase back. It is a
   state-(1) act — owner-trusted, uncorrelated, same-tree forgeable from
   Syzygy's perspective; its digest detects later drift, not authorship or
   attendance — the same trust model as the three observation acts of
   2026-09-02. No A1 audit trail exists and the record says so explicitly.
5. **I record it**: a dedicated act record at
   .syzygy/governance/decisions/PWB-COLD-OPEN-WALKTHROUGH-JUDGMENT-ACT.md,
   the recording tag pwb-adopt-walkthrough-judgment-signed-001 on that
   commit, the act phrase registered with the governance checks, and the
   aggregate acceptance record appended. From then on the daemon and the
   Polaris page show your verdict as recorded human judgment in state (1).

## What the act does and does not do

It warrants Syzygy honouring your judgment on this one walkthrough against
this one criterion. It is not evidence that comprehension succeeded — the
verdict stays your recorded judgment, never an observation and never a
score. It authorizes nothing else: no release, no deployment, no further
reads, no change to doctrine, contracts or the signed specification. A
"not met" verdict is as valid an act as "met"; it records findings and
sends the surface back to the repair cycle.

## What is already in place

The evaluator for the pair (PWB-REQ-022's 84 present-invalid cases, two
absent cases, both valid states, no fallback from a failed state (2)) and
the daemon-side loader for the two governance homes are implemented and
tested; with no record on disk the daemon reports the judgment as absent
and Unknown. Nothing in this packet was performed by an agent on your
behalf.
