import type { ProjectId, RepositoryId } from './identity.js';
import type { RegistrationResult } from './declaration.js';
import type { CoverageResult } from './coverage.js';

// Stable, literal, opaque identities — pure domain logic. Behavior is
// bound by CAP1-REQ-060 and the cited contract clauses RFC1-10
// (identifiers are opaque; names are labels; renaming changes the label,
// never the identifier), RFC1-2 (a repository's identity is never a URL,
// path, or branch), and RFC3-6 (repository identity is the declared
// opaque identifier; locator hints may change without touching
// identity).

// Locator HINTS for a repository — where it happens to live right now.
// Explicitly non-identity (RFC3-6): every field here may change while
// the identity does not, and nothing in this module or its callers may
// key on any of them.
export interface RepositoryLocator {
  readonly url?: string;
  readonly path?: string;
  readonly branch?: string;
}

// A project presented for serving: the identity and the label travel as
// distinct named fields, so no rendering can mistake one for the other
// (RFC1-10). Renaming rebuilds this with a new `label` and the same
// `identity`.
export interface ProjectPresentation {
  readonly identity: ProjectId;
  readonly label: string;
}

export function presentProject(identity: ProjectId, label: string): ProjectPresentation {
  return { identity, label };
}

// A repository presented for serving: identity beside locator hints.
// Relocation rebuilds this with a new `locator` and the same `identity`.
export interface RepositoryPresentation {
  readonly identity: RepositoryId;
  readonly locator: RepositoryLocator;
}

export function presentRepository(
  identity: RepositoryId,
  locator: RepositoryLocator,
): RepositoryPresentation {
  return { identity, locator };
}

// True when a candidate identity string has the shape of a locator — a
// URL, a filesystem path, or a git ref/branch path (RFC1-2's three named
// prohibitions). Used fail-closed at admission points: a served identity
// equal to a URL or path is CAP1-REQ-060's falsifier, so a candidate
// matching any of these shapes is refused as an identity. This is a
// shape check on the three prohibited families, not a general opacity
// oracle — a string passing it is not thereby proven opaque.
export function isLocatorShaped(candidate: string): boolean {
  // URL: any scheme prefix ('https://', 'git://', 'ssh://', 'file://').
  if (/^[a-zA-Z][a-zA-Z0-9+.-]*:\/\//.test(candidate)) return true;
  // Path: absolute, home-relative, dot-relative, Windows drive, or any
  // separator-bearing string ('a/b' is a path or a ref, never opaque).
  if (/^([/~.]|[a-zA-Z]:[\\/])/.test(candidate)) return true;
  if (candidate.includes('/') || candidate.includes('\\')) return true;
  return false;
}

// One identity-bearing field of a served answer, named so a sweep can
// enumerate and diff them (CAP1-REQ-060's case: rename a fixture project
// and relocate a repository, then diff the identity fields of answers
// before and after — denominator: the identity-field set).
export interface IdentityField {
  readonly field: string;
  readonly value: string;
}

// The identity-field set of a registration answer. Exactly the fields
// that carry identity — the display name is a label and is NOT listed
// here (RFC1-10), so a rename must leave this enumeration byte-identical.
export function registrationIdentityFields(result: RegistrationResult): readonly IdentityField[] {
  if (result.status !== 'registered') {
    return [];
  }
  return [{ field: 'facts.projectId', value: result.facts.projectId }];
}

// The identity-field set of a coverage answer: the project identity plus
// one repository identity per declared repository, in declaration order.
// The denominator is 1 + the repository count — nothing identity-bearing
// is silently absent from the enumeration.
export function coverageIdentityFields(result: CoverageResult): readonly IdentityField[] {
  return [
    { field: 'projectId', value: result.projectId },
    ...result.repositories.map((entry, i) => ({
      field: `repositories[${i}].repositoryId`,
      value: entry.repositoryId,
    })),
  ];
}
