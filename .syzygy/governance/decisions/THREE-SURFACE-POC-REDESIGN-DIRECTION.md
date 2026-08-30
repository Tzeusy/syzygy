# Owner direction — Three-Surface POC surface redesign

Date: 2026-08-30

Owner: Tzeusy

Baseline: `94e95470f98c1b3334d4a3f4ad25e548e51ae3a1`

Recorded from direction the owner gave directly in session on 2026-08-30,
after a first look at the running POC page. This refines the
2026-08-29 Three-Surface POC direction
(`THREE-SURFACE-POC-MODE-DIRECTION.md`); it does not replace it. Every
invariant, prohibition, and budget in that record remains in force, including
the eight-item cap — this redesign lands by repurposing the existing surface
work item, not by adding items.

The owner's direction, in three parts:

1. **Three surfaces, one design language, three distinct visual
   approaches.** The current single page with three list panels and exact
   tables is far from the vision. Polaris, Trajectory, and Orrery must share
   one unified design language while presenting very differently:
   - **Polaris** as a long-form white-paper over several pages, in the style
     of a published artifact document;
   - **Trajectory** as an issue-tracker visualization — kanban boards with
     time visualizations;
   - **Orrery** as a spatial code navigation platform — a 3D-city rendering
     that maps locations to verticals in the code.

2. **Trajectory's work-item data source is Beads on Dolt.** The
   authoritative work-item artifact is the Beads database hosted on Dolt,
   read over the project's registered bead-prefix (for Butlers: `bu`). The
   Dolt database — not the passive JSONL export — is the source of truth;
   observations record the Dolt revision they read at.

3. **Code-structure observation and client-side rendering are in scope,
   as prerequisites.** Code-structure observation of Butlers (beyond the
   first slice's five configured files) and client-side rendering in the POC
   app are both in scope for this POC, and building them out is a
   prerequisite for the surface builds.

Unchanged from the 2026-08-29 record: desired, execution, and observed state
remain distinct; no evidence means Unknown; activity or merge is never
intent satisfaction; human and machine views consume one shared fact model;
every positive claim has resolvable provenance; work dispatch is
human-triggered; Syzygy writes no implementation code in observed projects;
no production release, deployment, broad remote access, or multi-user
support; observation captures hashes, structure, and metadata with
provenance — not indexed file contents.

No RFC, OpenSpec change, launch packet, questionnaire, acceptance ceremony,
or review round is created for this direction.
