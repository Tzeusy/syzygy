import type { EpistemicMarking } from '@syzygy/polaris-generation-core';

/**
 * Deterministic layered left-to-right layout for draft-preview diagrams. No
 * dependency, no randomness: the same nodes and edges in the same order always
 * give the same coordinates.
 *
 * - DFS in node order, following each node's edges in edge order, marks every
 *   edge into a node still on the stack as a back edge (self-loops included).
 *   The remaining forward edges form a DAG.
 * - Each node's layer is its longest forward path from a source.
 * - Within a layer, nodes sort by the mean row of their forward predecessors,
 *   then by input position; each layer is centred vertically.
 * - Forward edges are cubic curves from the source's right side to the target's
 *   left side. Back edges are curves drawn below the layers, each one lower
 *   than the last.
 */

export const NODE_WIDTH = 200;
export const NODE_HEIGHT = 56;
const GAP_X = 120;
const GAP_Y = 40;
const MARGIN = 24;
const BACK_EDGE_DROP = 40;
const BACK_EDGE_STEP = 30;

export interface LayoutNodeInput { readonly id: string }
export interface LayoutEdgeInput { readonly id: string; readonly from: string; readonly to: string }
export interface LaidOutNode { readonly id: string; readonly layer: number; readonly row: number; readonly x: number; readonly y: number }
export interface LaidOutEdge {
  readonly id: string; readonly from: string; readonly to: string; readonly back: boolean;
  readonly d: string; readonly labelX: number; readonly labelY: number;
}
export interface DiagramLayout { readonly width: number; readonly height: number; readonly nodes: readonly LaidOutNode[]; readonly edges: readonly LaidOutEdge[] }

const num = (value: number): string => String(Math.round(value * 10) / 10);

export function layoutDiagram(nodes: readonly LayoutNodeInput[], edges: readonly LayoutEdgeInput[]): DiagramLayout {
  if (nodes.length === 0) throw new Error('empty-diagram');
  const index = new Map<string, number>();
  nodes.forEach((node, i) => {
    if (index.has(node.id)) throw new Error('duplicate-node');
    index.set(node.id, i);
  });
  const ends = edges.map(edge => {
    const from = index.get(edge.from), to = index.get(edge.to);
    if (from === undefined || to === undefined) throw new Error('unknown-node');
    return { from, to };
  });
  const outgoing = nodes.map(() => [] as number[]);
  ends.forEach((end, e) => outgoing[end.from]!.push(e));

  const back = edges.map(() => false);
  const state = nodes.map(() => 0); // 0 unvisited, 1 on stack, 2 done
  const visit = (u: number): void => {
    state[u] = 1;
    for (const e of outgoing[u]!) {
      const v = ends[e]!.to;
      if (state[v] === 1) back[e] = true;
      else if (state[v] === 0) visit(v);
    }
    state[u] = 2;
  };
  nodes.forEach((_, i) => { if (state[i] === 0) visit(i); });

  const layer = nodes.map(() => 0);
  const indegree = nodes.map(() => 0);
  ends.forEach((end, e) => { if (!back[e]) indegree[end.to]!++; });
  const ready = nodes.flatMap((_, i) => indegree[i] === 0 ? [i] : []);
  let placed = 0;
  while (ready.length > 0) {
    ready.sort((a, b) => a - b);
    const u = ready.shift()!;
    placed++;
    for (const e of outgoing[u]!) {
      if (back[e]) continue;
      const v = ends[e]!.to;
      layer[v] = Math.max(layer[v]!, layer[u]! + 1);
      if (--indegree[v]! === 0) ready.push(v);
    }
  }
  if (placed !== nodes.length) throw new Error('layout-cycle'); // unreachable: back edges break every cycle

  const layerCount = Math.max(...layer) + 1;
  const row = nodes.map(() => 0);
  const members: number[][] = Array.from({ length: layerCount }, () => []);
  for (let l = 0; l < layerCount; l++) {
    const inLayer = nodes.flatMap((_, i) => layer[i] === l ? [i] : []);
    const barycenter = (i: number): number => {
      const rows = ends.flatMap((end, e) => !back[e] && end.to === i ? [row[end.from]!] : []);
      return rows.length === 0 ? Number.POSITIVE_INFINITY : rows.reduce((a, b) => a + b, 0) / rows.length;
    };
    const keyed = inLayer.map(i => ({ i, key: barycenter(i) }));
    keyed.sort((a, b) => a.key === b.key ? a.i - b.i : a.key < b.key ? -1 : 1);
    keyed.forEach(({ i }, r) => { row[i] = r; });
    members[l] = keyed.map(({ i }) => i);
  }
  const maxRows = Math.max(...members.map(m => m.length));
  const columnHeight = (count: number): number => count * NODE_HEIGHT + (count - 1) * GAP_Y;
  const contentHeight = columnHeight(maxRows);
  const laidNodes: LaidOutNode[] = nodes.map((node, i) => {
    const offset = (contentHeight - columnHeight(members[layer[i]!]!.length)) / 2;
    return { id: node.id, layer: layer[i]!, row: row[i]!, x: MARGIN + layer[i]! * (NODE_WIDTH + GAP_X), y: MARGIN + offset + row[i]! * (NODE_HEIGHT + GAP_Y) };
  });

  const contentBottom = MARGIN + contentHeight;
  let backCount = 0;
  const laidEdges: LaidOutEdge[] = edges.map((edge, e) => {
    const from = laidNodes[ends[e]!.from]!, to = laidNodes[ends[e]!.to]!;
    if (!back[e]) {
      const x1 = from.x + NODE_WIDTH, y1 = from.y + NODE_HEIGHT / 2, x2 = to.x - 2, y2 = to.y + NODE_HEIGHT / 2;
      const dx = (x2 - x1) / 2;
      return { id: edge.id, from: edge.from, to: edge.to, back: false,
        d: `M ${num(x1)} ${num(y1)} C ${num(x1 + dx)} ${num(y1)}, ${num(x2 - dx)} ${num(y2)}, ${num(x2)} ${num(y2)}`,
        labelX: (x1 + x2) / 2, labelY: (y1 + y2) / 2 };
    }
    const depth = contentBottom + BACK_EDGE_DROP + backCount++ * BACK_EDGE_STEP;
    const self = from.id === to.id;
    const sx = from.x + NODE_WIDTH / 2 + (self ? 30 : 0), sy = from.y + NODE_HEIGHT;
    const tx = to.x + NODE_WIDTH / 2 - (self ? 30 : 0), ty = to.y + NODE_HEIGHT + 2;
    return { id: edge.id, from: edge.from, to: edge.to, back: true,
      d: `M ${num(sx)} ${num(sy)} C ${num(sx)} ${num(depth)}, ${num(tx)} ${num(depth)}, ${num(tx)} ${num(ty)}`,
      labelX: (sx + tx) / 2, labelY: (sy + ty + 6 * depth) / 8 };
  });
  const lowestBackEdge = backCount === 0 ? contentBottom + 24 : contentBottom + BACK_EDGE_DROP + (backCount - 1) * BACK_EDGE_STEP;
  return {
    width: MARGIN * 2 + layerCount * NODE_WIDTH + (layerCount - 1) * GAP_X,
    height: Math.ceil(lowestBackEdge + MARGIN),
    nodes: laidNodes,
    edges: laidEdges,
  };
}

/** Greedy word wrap; words longer than a line are split; overflow ends in `…`. */
export function wrapLabel(text: string, maxChars: number, maxLines: number): string[] {
  const words = text.replace(/\s+/gu, ' ').trim().split(' ').flatMap(word => {
    const chars = [...word];
    const parts: string[] = [];
    for (let i = 0; i < chars.length; i += maxChars) parts.push(chars.slice(i, i + maxChars).join(''));
    return parts;
  });
  const lines: string[] = [];
  for (const word of words) {
    const last = lines[lines.length - 1];
    if (last !== undefined && [...last].length + 1 + [...word].length <= maxChars) lines[lines.length - 1] = `${last} ${word}`;
    else lines.push(word);
  }
  if (lines.length <= maxLines) return lines.length === 0 ? [''] : lines;
  const kept = lines.slice(0, maxLines);
  const last = [...kept[maxLines - 1]!];
  kept[maxLines - 1] = `${last.slice(0, Math.max(0, maxChars - 1)).join('')}…`;
  return kept;
}

export interface RenderableNode extends LayoutNodeInput { readonly label: string; readonly epistemic: EpistemicMarking }
export interface RenderableEdge extends LayoutEdgeInput { readonly label: string; readonly epistemic: EpistemicMarking }

/**
 * Renders a laid-out diagram as static SVG. Every piece of text passes through
 * `escape`; every attribute value is a number, a path, or an id/class built here.
 * The caller must still pass the result through `assertInertSvg`.
 */
export function renderDiagramSvg(
  diagram: { readonly nodes: readonly RenderableNode[]; readonly edges: readonly RenderableEdge[] },
  index: number,
  escape: (value: string) => string,
): string {
  const layout = layoutDiagram(diagram.nodes, diagram.edges);
  const markerId = `arrow-${index}`;
  const connected = new Set(diagram.edges.flatMap(edge => [edge.from, edge.to]));
  const shown = (label: string, marking: EpistemicMarking, maxChars: number, maxLines: number): string[] => {
    const lines = wrapLabel(label, maxChars, maxLines);
    if (marking === 'unknown') lines[lines.length - 1] = `${lines[lines.length - 1]} ?`;
    return lines;
  };
  const textLines = (lines: readonly string[], x: number, firstBaseline: number, lineHeight: number): string =>
    `<text x="${num(x)}" y="${num(firstBaseline)}" text-anchor="middle">${lines.map((line, i) => `<tspan x="${num(x)}" dy="${i === 0 ? 0 : lineHeight}">${escape(line)}</tspan>`).join('')}</text>`;
  const nodes = diagram.nodes.map((node, i) => {
    const at = layout.nodes[i]!;
    const lines = shown(node.label, node.epistemic, 22, 2);
    const baseline = at.y + NODE_HEIGHT / 2 + 5 - (lines.length - 1) * 8;
    const note = connected.has(node.id) ? '' : `<text class="note" x="${num(at.x + NODE_WIDTH / 2)}" y="${num(at.y + NODE_HEIGHT + 18)}" text-anchor="middle">No relationship supplied</text>`;
    return `<g class="node ${node.epistemic}"><title>${escape(node.label)} (${node.epistemic})</title><rect x="${num(at.x)}" y="${num(at.y)}" width="${NODE_WIDTH}" height="${NODE_HEIGHT}" rx="6"/>${textLines(lines, at.x + NODE_WIDTH / 2, baseline, 16)}${note}</g>`;
  }).join('');
  const edges = diagram.edges.map((edge, i) => {
    const at = layout.edges[i]!;
    const lines = shown(edge.label, edge.epistemic, 18, 2);
    const widest = Math.max(...lines.map(line => [...line].length));
    const boxWidth = widest * 7.4 + 12, boxHeight = lines.length * 15 + 6;
    const top = at.labelY - boxHeight / 2;
    return `<g class="edge ${edge.epistemic}${at.back ? ' back' : ''}"><title>${escape(edge.label)} (${edge.epistemic})</title><path d="${at.d}" marker-end="url(#${markerId})"/><rect class="edge-label" x="${num(at.labelX - boxWidth / 2)}" y="${num(top)}" width="${num(boxWidth)}" height="${num(boxHeight)}" rx="3"/>${textLines(lines, at.labelX, top + 15, 15)}</g>`;
  }).join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${layout.width} ${layout.height}" width="${layout.width}" height="${layout.height}" role="img" aria-labelledby="diagram-title-${index}" aria-describedby="diagram-text-${index}"><defs><marker id="${markerId}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z"/></marker></defs>${edges}${nodes}</svg>`;
}
