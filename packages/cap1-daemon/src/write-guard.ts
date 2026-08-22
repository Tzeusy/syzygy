import * as fs from 'node:fs';
import * as path from 'node:path';

import { authorizeWrite } from '@syzygy/cap1-core';

// Runtime write guard — CAP1-REQ-061 (write boundary is the governed
// plane), with CAP1-REQ-023 and CAP1-REQ-053 as context (no write
// outside the two direct-write namespaces `openspec/**` and
// `.syzygy/**`; Syzygy never writes the root README or any other
// external location).
//
// Known core defect this module closes (recorded review WARNING): core
// `authorizeWrite` compares the RAW candidate with `startsWith`, so a
// path like `openspec/../README.md` passes the governed-plane check
// while its bytes would land at the repository root. The daemon must
// therefore never call core `authorizeWrite` on an unnormalized path:
// this guard is the one sanctioned runtime write path.
//
// CHOSEN SEMANTICS — judgment is on the NORMALIZED path, never the raw
// candidate. CAP1-REQ-061's oracle is an external filesystem
// comparison: what matters is where bytes actually land, not what the
// candidate string claims. Consequences, spelled out:
//   - `openspec/../README.md` normalizes to `README.md` — inside the
//     authorized root but OUTSIDE the governed plane, so it is refused
//     with core's existing named failure, 'outside-governed-plane'
//     (not as traversal: it never leaves the root).
//   - `openspec/../../escape` normalizes outside the authorized root
//     entirely — refused as 'traversal'.
//   - `.syzygy/../.git/config` normalizes to `.git/config` — refused
//     'outside-governed-plane'.
//   - A dot-segment path that normalizes INTO the governed plane
//     (e.g. `foo/../openspec/x.md` → `openspec/x.md`) is authorized:
//     its effect is byte-identical to the legitimate governed write.
//   - A symlink under the root whose real target leaves the root is a
//     lexical lie the normalizer cannot see; the nearest EXISTING
//     ancestor of the target is resolved with fs.realpathSync and any
//     escape is refused as 'symlink-escape' before any write.
// Fail-closed polarity: every arm that is not affirmatively authorized
// is a refusal; no check failure ever falls through to a write.

export const RUNTIME_WRITE_REFUSALS = [
  'degenerate-input',
  'traversal',
  'symlink-escape',
  'outside-governed-plane',
] as const;

export type RuntimeWriteRefusalName = (typeof RUNTIME_WRITE_REFUSALS)[number];

export type RuntimeWriteAuthorization =
  | {
      readonly authorized: true;
      /** Absolute filesystem path the write will land at (normalized). */
      readonly absolutePath: string;
      /** Root-relative normalized path, POSIX separators — the form core judged. */
      readonly relativePath: string;
      /** Governed namespace that admitted the write (core vocabulary). */
      readonly namespace: string;
    }
  | {
      readonly authorized: false;
      /** The raw candidate as received — preserved for the refusal record. */
      readonly candidatePath: string;
      /** Which check refused. 'outside-governed-plane' is core's own literal. */
      readonly refusedBy: RuntimeWriteRefusalName;
      /** Human-readable account of the refusal; never authority. */
      readonly detail: string;
    };

/** Nearest existing ancestor of an absolute path (always terminates at '/'). */
function nearestExistingAncestor(absolutePath: string): string {
  let current = absolutePath;
  for (;;) {
    if (fs.existsSync(current)) {
      return current;
    }
    const parent = path.dirname(current);
    if (parent === current) {
      return current;
    }
    current = parent;
  }
}

function isWithin(root: string, candidate: string): boolean {
  return candidate === root || candidate.startsWith(root + path.sep);
}

/**
 * Authorize a runtime filesystem write. Normalizes first, then enforces
 * the boundary: root containment, symlink reality, governed plane —
 * in that order. Pure decision; performs no write.
 */
export function authorizeRuntimeWrite(
  authorizedRoot: string,
  candidatePath: string,
): RuntimeWriteAuthorization {
  const root = path.resolve(authorizedRoot);

  const trimmed = candidatePath.trim();
  if (trimmed === '' || trimmed === '.') {
    return {
      authorized: false,
      candidatePath,
      refusedBy: 'degenerate-input',
      detail: 'empty or "." candidate names no file',
    };
  }

  const resolved = path.resolve(root, candidatePath);

  if (resolved === root) {
    return {
      authorized: false,
      candidatePath,
      refusedBy: 'degenerate-input',
      detail: 'candidate normalizes to the authorized root itself, naming no file',
    };
  }

  if (!isWithin(root, resolved)) {
    return {
      authorized: false,
      candidatePath,
      refusedBy: 'traversal',
      detail: `normalized path ${resolved} escapes the authorized root ${root}`,
    };
  }

  // Symlink escape: the lexical containment above can be a lie when a
  // path component under the root is a symlink whose target lives
  // outside it. Resolve the nearest EXISTING ancestor of the target to
  // its real location and require that real location to stay inside
  // the root's own real location.
  const realRoot = fs.existsSync(root) ? fs.realpathSync(root) : root;
  const ancestor = nearestExistingAncestor(resolved);
  const realAncestor = fs.realpathSync(ancestor);
  // Re-append the not-yet-existing tail so the judged path is the
  // write target itself, not just its existing ancestor.
  const tail = path.relative(ancestor, resolved);
  const realTarget = tail === '' ? realAncestor : path.join(realAncestor, tail);
  if (!isWithin(realRoot, realTarget) || realTarget === realRoot) {
    return {
      authorized: false,
      candidatePath,
      refusedBy: 'symlink-escape',
      detail: `real location ${realTarget} leaves the authorized root ${realRoot}`,
    };
  }

  const relativePath = path.relative(root, resolved).split(path.sep).join('/');
  const core = authorizeWrite(relativePath);
  if (!core.permitted) {
    return {
      authorized: false,
      candidatePath,
      refusedBy: core.violation,
      detail: `normalized path ${relativePath} is outside the governed write namespaces`,
    };
  }

  return {
    authorized: true,
    absolutePath: resolved,
    relativePath,
    namespace: core.namespace,
  };
}

/**
 * The ONLY sanctioned runtime write path. Authorizes first; on any
 * refusal returns the named failure WITHOUT touching the filesystem.
 * Writes (creating in-boundary parent directories as needed) only on
 * authorization — so it never partially writes: either the refusal arm
 * comes back and no byte landed, or the authorized arm comes back and
 * the file holds exactly `contents`.
 */
export function guardedWriteFile(
  authorizedRoot: string,
  candidatePath: string,
  contents: string,
): RuntimeWriteAuthorization {
  const decision = authorizeRuntimeWrite(authorizedRoot, candidatePath);
  if (!decision.authorized) {
    return decision;
  }
  fs.mkdirSync(path.dirname(decision.absolutePath), { recursive: true });
  fs.writeFileSync(decision.absolutePath, contents, 'utf8');
  return decision;
}
