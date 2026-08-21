import type { ProjectId } from './identity.js';

// Human project entry — pure domain logic, no I/O, no clock. Behavior
// is bound by CAP1-REQ-020…023 and the cited contract clauses RFC7-40
// (one fixed Syzygy-owned entry path per project; the path is a
// publication location, never an identity), RFC7-41 (entry routes to
// authority, never itself authority; every rendering carries nonCitable
// and artifactClass attributes), RFC7-42 (absent/unreadable/stale/
// contradictory entry renders honestly — absent is a finding, not an
// Unknown), and RFC7-43 (entry behavior writes nothing outside the
// governed plane).

// The one fixed entry path, verbatim (CAP1-REQ-020).
export const HUMAN_ENTRY_PATH = '.syzygy/intent/OVERVIEW.md' as const;

// The two governed write namespaces (CAP1-REQ-023).
export const GOVERNED_WRITE_NAMESPACES = ['openspec/', '.syzygy/'] as const;

export function isInsideGovernedPlane(path: string): boolean {
  return GOVERNED_WRITE_NAMESPACES.some((ns) => path.startsWith(ns));
}

// The route served for a project's human entry (CAP1-REQ-020).
export interface EntryRoute {
  readonly path: typeof HUMAN_ENTRY_PATH;
  readonly isIdentity: false;
}

export function serveEntryRoute(_projectId: ProjectId): EntryRoute {
  return { path: HUMAN_ENTRY_PATH, isIdentity: false };
}

// Authority citations carried on every rendering (CAP1-REQ-021).
export interface AuthorityCitation {
  readonly identifier: string;
  readonly kind: 'doctrine' | 'contract' | 'decision' | 'specification';
}

// The content state, a discriminated union over `state` (CAP1-REQ-022).
export type EntryContent =
  | { readonly state: 'present'; readonly text: string }
  | { readonly state: 'absent' }
  | { readonly state: 'unreadable'; readonly reason: string }
  | {
      readonly state: 'stale';
      readonly authorityText: string;
      readonly entryText: string;
    }
  | {
      readonly state: 'contradictory';
      readonly authorityText: string;
      readonly entryText: string;
      readonly authorityId: string;
    };

// The assessment, a discriminated union (CAP1-REQ-022). The absent
// case is a FINDING — the spec says "renders as a finding", not an
// Unknown. This is the load-bearing distinction: absence of the entry
// file is something the system CAN detect (it looked and found nothing),
// so it is a finding, not an Unknown.
export type EntryAssessment =
  | { readonly kind: 'available' }
  | { readonly kind: 'finding'; readonly detail: string }
  | { readonly kind: 'unknown-with-reason'; readonly reason: string }
  | {
      readonly kind: 'disagreement-disclosed';
      readonly authorityText: string;
      readonly entryText: string;
      readonly authorityId: string;
      readonly authorityWins: true;
    };

export function assessEntry(
  content: EntryContent,
  _authorities: readonly AuthorityCitation[],
): EntryAssessment {
  switch (content.state) {
    case 'present':
      return { kind: 'available' };
    case 'absent':
      return { kind: 'finding', detail: 'entry-absent' };
    case 'unreadable':
      return { kind: 'unknown-with-reason', reason: content.reason };
    case 'stale':
      return {
        kind: 'disagreement-disclosed',
        authorityText: content.authorityText,
        entryText: content.entryText,
        authorityId: 'staleness',
        authorityWins: true,
      };
    case 'contradictory':
      return {
        kind: 'disagreement-disclosed',
        authorityText: content.authorityText,
        entryText: content.entryText,
        authorityId: content.authorityId,
        authorityWins: true,
      };
  }
}

// The rendered entry, carrying the non-citable and artifact-class
// attributes (CAP1-REQ-021).
export interface EntryRendering {
  readonly nonCitable: true;
  readonly artifactClass: 'presentation-artifact';
  readonly content: EntryContent;
  readonly authorities: readonly AuthorityCitation[];
  readonly assessment: EntryAssessment;
}

export function renderEntry(
  content: EntryContent,
  authorities: readonly AuthorityCitation[],
): EntryRendering {
  return {
    nonCitable: true,
    artifactClass: 'presentation-artifact',
    content,
    authorities,
    assessment: assessEntry(content, authorities),
  };
}
