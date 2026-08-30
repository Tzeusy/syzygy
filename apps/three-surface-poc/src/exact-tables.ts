import { escapeHtml } from '@syzygy/cap1-daemon';
import type { PocEntity, PocModel, PocRelationship } from '@syzygy/three-surface-poc-core';

export function epistemicText(item: Pick<PocEntity | PocRelationship, 'epistemic'>): string {
  return item.epistemic.label === 'Observed' ? item.epistemic.basis : item.epistemic.reason;
}

function provenanceList(item: PocEntity | PocRelationship): string {
  if (item.provenance.length === 0) {
    return '<span class="provenance-none">No positive provenance; this relationship remains Unknown.</span>';
  }
  return `<ul class="provenance">${item.provenance
    .map(
      (provenance) => `<li data-parity-provenance>
        <span data-parity-field="provenance-kind">${escapeHtml(provenance.kind)}</span>
        <code data-parity-field="provenance-source">${escapeHtml(provenance.source)}</code>
        <code data-parity-field="provenance-revision">${escapeHtml(provenance.revision)}</code>
        ${provenance.digest === undefined ? '' : `<code data-parity-field="provenance-digest">${escapeHtml(provenance.digest)}</code>`}
      </li>`,
    )
    .join('')}</ul>`;
}

export function entityRows(model: PocModel): string {
  return model.entities
    .map(
      (entity) => `<tr id="${escapeHtml(entity.id)}" data-entity-id="${escapeHtml(entity.id)}">
        <td><span class="kind" data-parity-field="entity-kind">${escapeHtml(entity.kind)}</span></td>
        <td><code data-parity-field="entity-id">${escapeHtml(entity.id)}</code><br><strong data-parity-field="entity-title">${escapeHtml(entity.title)}</strong><br><small data-parity-field="entity-detail">${escapeHtml(entity.detail)}</small></td>
        <td><span class="epistemic epistemic-${entity.epistemic.label.toLowerCase()}" data-parity-field="epistemic-label">${escapeHtml(entity.epistemic.label)}</span><br><small data-parity-field="epistemic-explanation">${escapeHtml(epistemicText(entity))}</small></td>
        <td>${provenanceList(entity)}</td>
      </tr>`,
    )
    .join('');
}

export function relationshipRows(model: PocModel): string {
  return model.relationships
    .map(
      (relationship) => `<tr id="${escapeHtml(relationship.id)}" data-relationship-id="${escapeHtml(relationship.id)}">
        <td><span class="kind" data-parity-field="relationship-kind">${escapeHtml(relationship.kind)}</span></td>
        <td><code data-parity-field="relationship-id">${escapeHtml(relationship.id)}</code><br><a data-parity-field="relationship-from" href="#${escapeHtml(relationship.from)}">${escapeHtml(relationship.from)}</a><br>→ <a data-parity-field="relationship-to" href="#${escapeHtml(relationship.to)}">${escapeHtml(relationship.to)}</a></td>
        <td><span data-parity-field="relationship-statement">${escapeHtml(relationship.statement)}</span></td>
        <td><span class="epistemic epistemic-${relationship.epistemic.label.toLowerCase()}" data-parity-field="epistemic-label">${escapeHtml(relationship.epistemic.label)}</span><br><small data-parity-field="epistemic-explanation">${escapeHtml(epistemicText(relationship))}</small></td>
        <td>${provenanceList(relationship)}</td>
      </tr>`,
    )
    .join('');
}

export function exactTablesSection(model: PocModel): string {
  return `<section class="tables" aria-label="Exact graph tables">
      <h2 id="entities">Exact entities</h2>
      <div class="table-wrap"><table><thead><tr><th>Kind</th><th>Entity</th><th>Epistemic state</th><th>Provenance</th></tr></thead><tbody>${entityRows(model)}</tbody></table></div>
      <h2 id="relationships">Exact relationships</h2>
      <div class="table-wrap"><table><thead><tr><th>Kind</th><th>Path</th><th>Claim</th><th>Epistemic state</th><th>Provenance</th></tr></thead><tbody>${relationshipRows(model)}</tbody></table></div>
    </section>`;
}
