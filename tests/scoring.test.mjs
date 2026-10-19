import assert from 'node:assert/strict';
import { computeResults, pearson, hexDistance, prediger, occVector } from '../js/scoring.js';
import { demoState } from '../js/demo.js';
import { PAGES, CLOSED_ITEMS, MODULES } from '../js/model.js';
import { DATA } from '../js/data.js';

let passed = 0;
const test = (name, fn) => { fn(); passed++; console.log('ok -', name); };

test('item counts match the document', () => {
  assert.equal(CLOSED_ITEMS.length, 149);
  assert.equal(MODULES.find(m => m.id === 'int').items.length, 49);
  assert.equal(DATA.occ.length, 56);
  assert.equal(new Set(CLOSED_ITEMS.map(i => i.id)).size, CLOSED_ITEMS.length);
});

test('both languages have the same structure', () => {
  for (const k of ['b5', 'ctx', 'open', 'anchors', 'sdt', 'adapt']) assert.equal(DATA.ro[k].length, DATA.de[k].length, k);
  for (const t of 'RIASEC') assert.equal(DATA.ro.int[t].length, DATA.de.int[t].length);
});

test('hexagon distances', () => {
  assert.equal(hexDistance('R', 'I'), 1);
  assert.equal(hexDistance('R', 'C'), 1);
  assert.equal(hexDistance('R', 'A'), 2);
  assert.equal(hexDistance('R', 'S'), 3);
});

test('Prediger places pure types on the right sides of the map', () => {
  const pure = t => 'RIASEC'.split('').map(x => (x === t ? 100 : 0));
  assert.ok(prediger(pure('R')).x < 0 && Math.abs(prediger(pure('R')).y) < 1e-9);
  assert.ok(prediger(pure('S')).x > 0);
  assert.ok(prediger(pure('E')).y > 0 && prediger(pure('C')).y > 0);
  assert.ok(prediger(pure('I')).y < 0 && prediger(pure('A')).y < 0);
});

test('pearson handles flat profiles', () => {
  assert.equal(pearson([3, 3, 3], [1, 2, 3]), 0);
  assert.ok(Math.abs(pearson([1, 2, 3], [2, 4, 6]) - 1) < 1e-12);
});

test('demo profile scores as I-C-R technical expert', () => {
  const r = computeResults(demoState());
  assert.equal(r.code.join(''), 'ICR');
  assert.equal(r.consistency, 2);
  assert.equal(r.anchors[0].code, 'TF');
  assert.equal(r.quality.verdict, 'good');
  const top = r.matches.slice(0, 5).map(m => DATA.occ[m.i].code);
  assert.ok(top.every(c => /^[ICR]{3}$/.test(c) || c.startsWith('I') || c.startsWith('C')), top.join(','));
  assert.ok(r.matches[0].index >= 80, String(r.matches[0].index));
  assert.ok(r.b5.C > 3.5 && r.b5.E < 3);
});

test('quality flags careless answering', () => {
  const st = demoState();
  for (const id of Object.keys(st.answers)) st.answers[id] = 3;
  PAGES.forEach((p, i) => { if (p.kind === 'items') st.times[i] = p.items.length * 800; });
  const q = computeResults(st).quality;
  assert.equal(q.verdict, 'caution');
  const keys = q.issues.map(i => i.key);
  for (const k of ['attention', 'uniform', 'speed']) assert.ok(keys.includes(k), k);
});

test('occupation vector weights', () => {
  assert.deepEqual(occVector('ICR'), [0.4, 1, 0.1, 0.1, 0.1, 0.65]);
});

console.log(`\n${passed} tests passed`);
