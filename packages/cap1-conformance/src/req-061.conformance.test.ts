import { describe, expect, it } from 'vitest';
import {
  isInsideGovernedPlane,
  authorizeWrite,
  detectWideningFields,
  reportEffectBoundary,
  GOVERNED_WRITE_NAMESPACES,
  WIDENING_FIELD_NAMES,
  CAPABILITY_1_EXTERNAL_EFFECTS,
} from '@syzygy/cap1-core';

// CAP1-REQ-061 — Write boundary hardening.
//
// Case: Capability 1 observes and presents; its write boundary is the
// governed plane (`openspec/**` and `.syzygy/**`). No source-code edit,
// root-README edit, deployment, scheduler mutation, or other external
// effect. Oracle: governed-plane paths are authorized; paths outside are
// refused; widening fields render as contradictions routed to the owner.
// Oracle independence: expected values are hard-coded below, never
// imported from the vocabulary modules.

describe('CAP1-REQ-061 — write boundary hardening', () => {
  describe('isInsideGovernedPlane classifies paths correctly', () => {
    it('governed paths pass', () => {
      expect(isInsideGovernedPlane('openspec/changes/my-change/spec.md')).toBe(true);
      expect(isInsideGovernedPlane('openspec/')).toBe(true);
      expect(isInsideGovernedPlane('.syzygy/governance/doctrine/VIS.md')).toBe(true);
      expect(isInsideGovernedPlane('.syzygy/')).toBe(true);
    });

    it('external paths fail', () => {
      expect(isInsideGovernedPlane('packages/cap1-core/src/index.ts')).toBe(false);
      expect(isInsideGovernedPlane('README.md')).toBe(false);
      expect(isInsideGovernedPlane('apps/daemon/server.ts')).toBe(false);
      expect(isInsideGovernedPlane('src/main.ts')).toBe(false);
      expect(isInsideGovernedPlane('')).toBe(false);
    });
  });

  describe('authorizeWrite permits governed-plane writes, refuses external', () => {
    it('permits writes inside openspec/', () => {
      const result = authorizeWrite('openspec/changes/delta/spec.md');
      expect(result.permitted).toBe(true);
      if (result.permitted) {
        expect(result.namespace).toBe('openspec/');
      }
    });

    it('permits writes inside .syzygy/', () => {
      const result = authorizeWrite('.syzygy/governance/policies/new-policy.md');
      expect(result.permitted).toBe(true);
      if (result.permitted) {
        expect(result.namespace).toBe('.syzygy/');
      }
    });

    it('refuses writes outside the governed plane', () => {
      const result = authorizeWrite('packages/cap1-core/src/hack.ts');
      expect(result.permitted).toBe(false);
      if (!result.permitted) {
        expect(result.violation).toBe('outside-governed-plane');
        expect(result.path).toBe('packages/cap1-core/src/hack.ts');
      }
    });

    it('refuses root-README writes', () => {
      const result = authorizeWrite('README.md');
      expect(result.permitted).toBe(false);
    });

    it('refuses deployment target writes', () => {
      const result = authorizeWrite('deploy/production/config.yaml');
      expect(result.permitted).toBe(false);
    });
  });

  describe('detectWideningFields catches known widening fields', () => {
    it('detects write_roots as a contradiction routed to owner', () => {
      const violations = detectWideningFields({ write_roots: '/usr/share' });
      expect(violations).toHaveLength(1);
      expect(violations[0]).toEqual({
        fieldName: 'write_roots',
        fieldValue: '/usr/share',
        rendering: 'contradiction',
        routedTo: 'owner',
      });
    });

    it('detects all four known widening field names', () => {
      const fields: Record<string, string> = {
        write_roots: '/tmp',
        writable_paths: '/var/data',
        output_directory: '/opt/output',
        deploy_target: 'production',
      };
      const violations = detectWideningFields(fields);
      expect(violations).toHaveLength(4);
      for (const v of violations) {
        expect(v.rendering).toBe('contradiction');
        expect(v.routedTo).toBe('owner');
      }
    });

    it('ignores fields that are not widening field names', () => {
      const violations = detectWideningFields({
        project_name: 'my-project',
        description: 'A project',
      });
      expect(violations).toHaveLength(0);
    });

    it('falsifier: a widening field must render as contradiction, not be honored', () => {
      const violations = detectWideningFields({ deploy_target: 'staging' });
      expect(violations).toHaveLength(1);
      expect(violations[0]!.rendering).toBe('contradiction');
      expect(violations[0]!.routedTo).toBe('owner');
    });
  });

  describe('effect boundary report', () => {
    it('Capability 1 exposes no external effects', () => {
      expect(CAPABILITY_1_EXTERNAL_EFFECTS).toHaveLength(0);
    });

    it('reports the governed write namespaces', () => {
      const report = reportEffectBoundary({});
      expect(report.capability).toBe('capability-1');
      expect(report.permittedWriteNamespaces).toEqual(['openspec/', '.syzygy/']);
      expect(report.externalEffects).toHaveLength(0);
      expect(report.wideningViolations).toHaveLength(0);
    });

    it('includes widening violations in the report', () => {
      const report = reportEffectBoundary({ deploy_target: 'prod' });
      expect(report.wideningViolations).toHaveLength(1);
      expect(report.wideningViolations[0]!.fieldName).toBe('deploy_target');
    });
  });

  describe('no module in S1–S6 exports a function that performs I/O', () => {
    it('GOVERNED_WRITE_NAMESPACES is exactly two entries: openspec/ and .syzygy/', () => {
      expect(GOVERNED_WRITE_NAMESPACES).toEqual(['openspec/', '.syzygy/']);
      expect(GOVERNED_WRITE_NAMESPACES).toHaveLength(2);
    });

    it('WIDENING_FIELD_NAMES is the closed four', () => {
      expect(WIDENING_FIELD_NAMES).toEqual([
        'write_roots',
        'writable_paths',
        'output_directory',
        'deploy_target',
      ]);
    });
  });
});
