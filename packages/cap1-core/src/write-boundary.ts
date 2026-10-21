import { GOVERNED_WRITE_NAMESPACES, isInsideGovernedPlane } from './entry.js';

// Write boundary hardening — pure domain logic, no I/O, no clock.
// Behavior is bound by CAP1-REQ-061 and the cited contract clauses
// RFC7-43 (Capability 1's write boundary is the governed plane; no
// source-code edit, root-README edit, deployment, scheduler mutation,
// or other external effect) and RFC1-22 (the Proposed state plane:
// never desired, never observed; may not anchor the map).
//
// TEST SUPPORT, exported only from the `@syzygy/cap1-core/testing` entry
// (see testing.ts), never from the package barrel. No production module
// calls anything here: Capability 1 performs no governed write, and
// CAP1-REQ-061's write-universe oracle is external (the cap1-system
// effect observer and write-boundary system test). This is the reference
// model the req-061 conformance file pins for the widening-field clause
// (a field purporting to widen the write universe is inoperative and
// renders as a contradiction routed to the owner); the daemon does not
// call it. `authorizeWrite` judges an already-normalized, root-relative
// path by raw `startsWith`: a caller holding an unnormalized path must
// normalize first (`openspec/../README.md` passes the prefix test).

export const WIDENING_FIELD_NAMES = [
  'write_roots',
  'writable_paths',
  'output_directory',
  'deploy_target',
] as const;

export interface WideningFieldViolation {
  readonly fieldName: string;
  readonly fieldValue: string;
  readonly rendering: 'contradiction';
  readonly routedTo: 'owner';
}

export function detectWideningFields(
  extraFields: Readonly<Record<string, string>>,
): readonly WideningFieldViolation[] {
  return Object.entries(extraFields)
    .filter(([name]) => (WIDENING_FIELD_NAMES as readonly string[]).includes(name))
    .map(([name, value]) => ({
      fieldName: name,
      fieldValue: value,
      rendering: 'contradiction' as const,
      routedTo: 'owner' as const,
    }));
}

export type WriteAuthorization =
  | { readonly permitted: true; readonly namespace: string }
  | { readonly permitted: false; readonly path: string; readonly violation: 'outside-governed-plane' };

export function authorizeWrite(path: string): WriteAuthorization {
  for (const ns of GOVERNED_WRITE_NAMESPACES) {
    if (path.startsWith(ns)) {
      return { permitted: true, namespace: ns };
    }
  }
  return { permitted: false, path, violation: 'outside-governed-plane' };
}

export const CAPABILITY_1_EXTERNAL_EFFECTS = [] as const;

export interface EffectBoundaryReport {
  readonly capability: 'capability-1';
  readonly permittedWriteNamespaces: readonly string[];
  readonly externalEffects: typeof CAPABILITY_1_EXTERNAL_EFFECTS;
  readonly wideningViolations: readonly WideningFieldViolation[];
}

export function reportEffectBoundary(
  extraFields: Readonly<Record<string, string>>,
): EffectBoundaryReport {
  return {
    capability: 'capability-1',
    permittedWriteNamespaces: [...GOVERNED_WRITE_NAMESPACES],
    externalEffects: CAPABILITY_1_EXTERNAL_EFFECTS,
    wideningViolations: detectWideningFields(extraFields),
  };
}
