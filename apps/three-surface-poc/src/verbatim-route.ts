// PWB-REQ-011's transient exact-requirement route (as amended 2026-09-05).
//
// When the current requirement leaf belongs to a baseline
// `openspec/specs/*/spec.md` exact Git object already in the signed,
// admitted population, Polaris may transiently encode that requirement and
// its scenarios verbatim — after the unchanged authority, exact-object,
// whole-body secret, inert-content and identity checks have all admitted the
// same object. The reader below is that route: it is derived from the model
// being rendered, decides per leaf from the shape's own records, reads the
// exact object id once per render, screens the transient body with the same
// approved detectors and active-content scan the pipeline uses, and stores,
// logs and caches nothing. Any failed gate is a typed refusal that leaves the
// text Unknown with its reason and discloses no body bytes; the selection of
// requirement blocks and the identity check happen in `resolveVerbatim`.
//
// Why the route screens the body itself: phase B classifies baseline specs
// path-only (their item identity is the directory name, so the pipeline
// deliberately never reads their bodies). The evaluation therefore holds no
// whole-body secret or inert-content verdict for them, and this route runs
// those unchanged checks on the bytes it reads before any of them may be
// encoded. No new consent is granted here: the object is already a member of
// the signed population under the one consented content class.
import { execFileSync } from 'node:child_process';

import {
  PWB_RESOURCE_LIMITS,
  PWB_SECRET_POLICY,
  compileDetectors,
  deniedPathReason,
  detectSecrets,
  gitBlobObjectId,
  scanActiveContent,
  type PocModel,
  type PwbResourceLimits,
  type SecretClassificationPolicy,
} from '@syzygy/three-surface-poc-core';

import type { VerbatimLeafReader, VerbatimRefusal } from './capability-detail.js';

/** Reads one blob by exact object id, or `undefined` when Git cannot. */
export type GitBlobReader = (objectId: string) => Uint8Array | undefined;

export function gitBlobReaderFor(repoRoot: string): GitBlobReader {
  return (objectId) => {
    try {
      return new Uint8Array(execFileSync('git', ['cat-file', 'blob', objectId], { cwd: repoRoot, maxBuffer: 64 * 1024 * 1024 }));
    } catch {
      return undefined;
    }
  };
}

function refusal(refused: VerbatimRefusal['refused'], detail: string): VerbatimRefusal {
  return { refused, detail };
}

/**
 * The route, or `undefined` when the evaluation observed no shape (no
 * population, no gate to consult, so the leaf stays outside the consented
 * class exactly as before).
 */
export function verbatimRouteReader(
  model: PocModel,
  readBlob: GitBlobReader,
  policy: SecretClassificationPolicy = PWB_SECRET_POLICY,
  limits: PwbResourceLimits = PWB_RESOURCE_LIMITS,
): VerbatimLeafReader | undefined {
  const shape = model.projectShape;
  if (shape.kind !== 'observed') return undefined;
  const detectors = compileDetectors(policy);
  return (leaf) => {
    // 1. Authority: only a source the P1-gated evaluation admitted into the
    //    signed population, under the baseline-spec rule, at this revision.
    const source = shape.sources.find((candidate) => candidate.path === leaf.path);
    if (source === undefined) {
      return refusal('unconsented-source-or-provider', `${leaf.path} is not a source of this evaluation's signed population; nothing was read.`);
    }
    if (source.rule !== 'baseline-spec-tree') {
      return refusal('unconsented-source-or-provider', `${leaf.path} is not a baseline spec (${source.rule}); the exact-requirement route applies to baseline specs only.`);
    }
    if (leaf.revision !== shape.identity.revision) {
      return refusal('reference-unresolvable', `${leaf.path} is bound to ${leaf.revision.slice(0, 12)} but this evaluation observed ${shape.identity.revision.slice(0, 12)}; nothing was read.`);
    }
    if (source.identity !== leaf.identity) {
      return refusal('reference-unresolvable', `${leaf.path}'s captured identity is not this evaluation's exact object; nothing was read.`);
    }
    if (source.record.outcome === 'excluded') {
      return refusal('excluded-content', `${leaf.path} was excluded by policy in this evaluation (${source.record.exclusion.redactionClass}); nothing was read.`);
    }
    if (source.record.outcome !== 'classified') {
      return refusal('source-uncaptured-or-unreachable', `${leaf.path}'s body was not admitted in this evaluation (${source.record.outcome}); nothing was read.`);
    }
    if (source.anchor.kind !== 'blob') {
      return refusal('reference-unresolvable', `${leaf.path} is ${source.anchor.kind} at this revision; there is no exact object to read.`);
    }
    const denied = deniedPathReason(leaf.path);
    if (denied !== undefined) {
      return refusal('excluded-content', `${leaf.path} is denied by the classification policy (${denied}); nothing was read.`);
    }
    // 2. Exact object: the bytes Git serves must be that object.
    const bytes = readBlob(source.anchor.objectId);
    if (bytes === undefined) return undefined;
    const format = source.anchor.objectId.length === 64 ? 'sha256' : 'sha1';
    if (gitBlobObjectId(bytes, format) !== source.anchor.objectId) {
      return refusal('reference-unresolvable', `${leaf.path}: the bytes served do not hash to this evaluation's exact object; nothing was rendered.`);
    }
    if (bytes.byteLength > limits.maxBytesPerSource) {
      return refusal('excluded-content', `${leaf.path} exceeds the per-source envelope (${bytes.byteLength} > ${limits.maxBytesPerSource} bytes); nothing was rendered.`);
    }
    // 3. Whole-body secret and inert-content checks, the pipeline's own,
    //    over the transient text; the refusal names the detector or form,
    //    never the bytes.
    if (bytes.includes(0)) return refusal('excluded-content', `${leaf.path} is not text; nothing was rendered.`);
    let text: string;
    try {
      text = new TextDecoder('utf-8', { fatal: true }).decode(bytes);
    } catch {
      return refusal('excluded-content', `${leaf.path} is not UTF-8 text; nothing was rendered.`);
    }
    const detector = detectSecrets(detectors, text);
    if (detector !== undefined) {
      return refusal('excluded-content', `${leaf.path} matched the classification policy's ${detector} detector (${policy.policyId} ${policy.policyVersion}); nothing was rendered.`);
    }
    const active = scanActiveContent(text);
    if (active.length > 0) {
      const forms = [...new Set(active.map((finding) => finding.form))].join(', ');
      return refusal('excluded-content', `${leaf.path} carries active content (${forms}); nothing was rendered.`);
    }
    // 4. Identity and requirement selection follow in `resolveVerbatim`.
    return bytes;
  };
}
