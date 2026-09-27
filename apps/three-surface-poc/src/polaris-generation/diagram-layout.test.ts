import { describe, expect, it } from 'vitest';
import { layoutDiagram, wrapLabel } from './diagram-layout.js';

const nodes = (...ids: string[]) => ids.map(id => ({ id }));
const edge = (id: string, from: string, to: string) => ({ id, from, to });
const place = (layout: ReturnType<typeof layoutDiagram>) => layout.nodes.map(({ id, layer, row, x, y }) => [id, layer, row, x, y]);

describe('layered left-to-right diagram layout', () => {
  it('lays a chain out one layer per node with horizontal cubic edges', () => {
    const layout = layoutDiagram(nodes('a', 'b', 'c'), [edge('ab', 'a', 'b'), edge('bc', 'b', 'c')]);
    expect(place(layout)).toEqual([['a', 0, 0, 24, 24], ['b', 1, 0, 344, 24], ['c', 2, 0, 664, 24]]);
    expect(layout.edges.map(e => [e.id, e.back, e.d, e.labelX, e.labelY])).toEqual([
      ['ab', false, 'M 224 52 C 283 52, 283 52, 342 52', 283, 52],
      ['bc', false, 'M 544 52 C 603 52, 603 52, 662 52', 603, 52],
    ]);
    expect([layout.width, layout.height]).toEqual([888, 128]);
  });

  it('fans out into one centred layer, keeping input order', () => {
    const layout = layoutDiagram(nodes('hub', 'x', 'y', 'z'), [edge('hx', 'hub', 'x'), edge('hy', 'hub', 'y'), edge('hz', 'hub', 'z')]);
    expect(place(layout)).toEqual([['hub', 0, 0, 24, 120], ['x', 1, 0, 344, 24], ['y', 1, 1, 344, 120], ['z', 1, 2, 344, 216]]);
    expect(layout.edges.map(e => e.d)).toEqual([
      'M 224 148 C 283 148, 283 52, 342 52',
      'M 224 148 C 283 148, 283 148, 342 148',
      'M 224 148 C 283 148, 283 244, 342 244',
    ]);
    expect([layout.width, layout.height]).toEqual([568, 320]);
  });

  it('takes the longest path, so a skip edge never pulls a node leftwards', () => {
    const layout = layoutDiagram(nodes('a', 'b', 'c'), [edge('ac', 'a', 'c'), edge('ab', 'a', 'b'), edge('bc', 'b', 'c')]);
    expect(layout.nodes.map(n => [n.id, n.layer])).toEqual([['a', 0], ['b', 1], ['c', 2]]);
  });

  it('breaks a cycle at the DFS back edge and draws it as a curve below the layers', () => {
    const layout = layoutDiagram(nodes('a', 'b', 'c'), [edge('ab', 'a', 'b'), edge('bc', 'b', 'c'), edge('ca', 'c', 'a')]);
    expect(place(layout)).toEqual([['a', 0, 0, 24, 24], ['b', 1, 0, 344, 24], ['c', 2, 0, 664, 24]]);
    expect(layout.edges.map(e => [e.id, e.back])).toEqual([['ab', false], ['bc', false], ['ca', true]]);
    expect(layout.edges[2]!.d).toBe('M 764 80 C 764 120, 124 120, 124 82');
    expect(layout.height).toBe(144);
  });

  it('draws a self-loop and a second back edge lower than the first', () => {
    const layout = layoutDiagram(nodes('a', 'b'), [edge('ab', 'a', 'b'), edge('bb', 'b', 'b'), edge('ba', 'b', 'a')]);
    expect(layout.edges.map(e => [e.id, e.back, e.d])).toEqual([
      ['ab', false, 'M 224 52 C 283 52, 283 52, 342 52'],
      ['bb', true, 'M 474 80 C 474 120, 414 120, 414 82'],
      ['ba', true, 'M 444 80 C 444 150, 124 150, 124 82'],
    ]);
    expect(layout.height).toBe(174);
  });

  it('is deterministic and refuses dangling endpoints and duplicate nodes', () => {
    const input = [nodes('a', 'b', 'c', 'd'), [edge('ab', 'a', 'b'), edge('cd', 'c', 'd'), edge('da', 'd', 'a')]] as const;
    expect(layoutDiagram(...input)).toEqual(layoutDiagram(structuredClone(input[0]), structuredClone(input[1])));
    expect(() => layoutDiagram(nodes('a'), [edge('ax', 'a', 'x')])).toThrow('unknown-node');
    expect(() => layoutDiagram(nodes('a', 'a'), [])).toThrow('duplicate-node');
    expect(() => layoutDiagram([], [])).toThrow('empty-diagram');
  });

  it('wraps labels by word, splits long words and ellipsizes overflow', () => {
    expect(wrapLabel('Care observations feed a seasonal plan', 22, 2)).toEqual(['Care observations feed', 'a seasonal plan']);
    expect(wrapLabel('abcdefghij', 4, 3)).toEqual(['abcd', 'efgh', 'ij']);
    expect(wrapLabel('one two three four five six', 9, 2)).toEqual(['one two', 'three…']);
    expect(wrapLabel('  line\nbreak ', 22, 2)).toEqual(['line break']);
  });
});
