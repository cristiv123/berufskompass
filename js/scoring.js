import { TYPES, OCC, MODULES, PAGES, ITEMS, ATTENTION } from './model.js';
import { DATA } from './data.js';

const S = DATA.ro;

export const mean = arr => {
  const v = arr.filter(x => typeof x === 'number' && !Number.isNaN(x));
  return v.length ? v.reduce((a, b) => a + b, 0) / v.length : null;
};
export const to100 = m => (m == null ? null : ((m - 1) / 4) * 100);

export function pearson(x, y) {
  const mx = mean(x), my = mean(y);
  let num = 0, dx = 0, dy = 0;
  for (let i = 0; i < x.length; i++) {
    num += (x[i] - mx) * (y[i] - my);
    dx += (x[i] - mx) ** 2;
    dy += (y[i] - my) ** 2;
  }
  return dx === 0 || dy === 0 ? 0 : num / Math.sqrt(dx * dy);
}

export function hexDistance(a, b) {
  const d = Math.abs(TYPES.indexOf(a) - TYPES.indexOf(b));
  return Math.min(d, 6 - d);
}

// Prediger (1982): x = things(−) … people(+), y = ideas(−) … data(+), on centered scores.
export function prediger(vec) {
  const m = mean(vec);
  const [R, I, A, S_, E, C] = vec.map(v => v - m);
  return { x: A + 2 * S_ + E - C - 2 * R - I, y: 1.73 * (E + C - I - A) };
}

export function occVector(code) {
  const w = [1, 0.65, 0.4];
  return TYPES.map(t => (code.includes(t) ? w[code.indexOf(t)] : 0.1));
}

export function band(v, lo, hi) {
  return v == null ? null : v < lo ? 'low' : v > hi ? 'high' : 'mid';
}

export function computeResults(st) {
  const a = st.answers || {};
  const val = id => (typeof a[id] === 'number' ? a[id] : null);
  const scaleOf = (mod, pred) => MODULES.find(m => m.id === mod).items.filter(it => !it.att && pred(it));

  const int = {}, conf = {};
  for (const t of TYPES) {
    int[t] = to100(mean(scaleOf('int', it => it.t === t).map(it => val(it.id))));
    conf[t] = to100(mean(scaleOf('conf', it => it.t === t).map(it => val(it.id))));
  }
  const intVec = TYPES.map(t => int[t] ?? 0);
  const confVec = TYPES.map(t => conf[t] ?? 0);

  const order = TYPES.slice().sort((x, y) => (int[y] - int[x]) || (conf[y] - conf[x]) || (TYPES.indexOf(x) - TYPES.indexOf(y)));
  const code = order.slice(0, 3);
  const differentiation = Math.max(...intVec) - Math.min(...intVec);
  const consistency = hexDistance(code[0], code[1]);
  const elevation = mean(intVec);
  const map = prediger(intVec);

  const thrI = mean(intVec), thrC = mean(confVec);
  const quadrants = {};
  for (const t of TYPES) {
    const hi = int[t] >= thrI, hc = conf[t] >= thrC;
    quadrants[t] = hi && hc ? 'own' : hi ? 'conquer' : hc ? 'skill' : 'off';
  }

  const picks = new Set(st.picks || []);
  const anchors = S.anchors.map(an => {
    const items = scaleOf('anc', it => it.anchor === an.code);
    const ratings = items.map(it => val(it.id) ?? 0);
    const picked = items.filter(it => picks.has(it.id)).length;
    return { code: an.code, score: (ratings.reduce((s, x) => s + x, 0) + 4 * picked) / 3, mean: mean(ratings), picked };
  }).sort((x, y) => y.score - x.score);

  const b5 = {};
  for (const trait of ['E', 'A', 'C', 'N', 'O']) {
    b5[trait] = mean(scaleOf('b5', it => it.trait === trait).map(it => {
      const v = val(it.id);
      return v == null ? null : it.rev ? 6 - v : v;
    }));
  }
  b5.ES = b5.N == null ? null : 6 - b5.N;

  const needs = S.sdt.map((_, ni) => mean(scaleOf('sdt', it => it.need === ni).map(it => val(it.id))));
  const ctx = S.ctx.map((_, k) => val(`U_${k + 1}`));
  const adapt = S.adapt.map((_, di) => mean(scaleOf('ad', it => it.dim === di).map(it => val(it.id))));

  const matches = OCC.map((o, i) => {
    const v = occVector(o.code);
    const rI = pearson(intVec, v), rC = pearson(confVec, v);
    const index = Math.round(((0.7 * rI + 0.3 * rC + 1) / 2) * 100);
    return { i, code: o.code, rI, rC, index, pos: prediger(v.map(x => x * 100)) };
  }).sort((x, y) => y.index - x.index);

  return {
    int, conf, code, order, differentiation, consistency, elevation, map, thrI, thrC, quadrants,
    anchors, b5, needs, ctx, adapt, matches, quality: quality(st),
  };
}

export function quality(st) {
  const a = st.answers || {};
  const issues = [];
  for (const att of ATTENTION) {
    if (typeof a[att.id] === 'number' && a[att.id] !== att.expect) issues.push({ key: 'attention', serious: true, n: att.n });
  }
  let uniform = 0;
  for (const p of PAGES) {
    if (p.kind !== 'items' || p.mod === 'ctx') continue;
    const vals = p.items.filter(it => !it.att).map(it => a[it.id]).filter(v => typeof v === 'number');
    if (vals.length >= 5 && vals.every(v => v === vals[0])) uniform++;
  }
  if (uniform >= 2) issues.push({ key: 'uniform', serious: true, n: uniform });

  const times = st.times || {};
  let ms = 0, count = 0;
  PAGES.forEach((p, idx) => {
    if (p.kind === 'items' && times[idx] > 0) { ms += times[idx]; count += p.items.length; }
  });
  const secPerItem = count ? ms / 1000 / count : null;
  if (secPerItem != null && secPerItem < 1.8) issues.push({ key: 'speed', serious: true, n: secPerItem });

  const raw = mean(MODULES.find(m => m.id === 'b5').items.filter(it => !it.att).map(it => a[it.id]));
  if (raw != null && (raw >= 3.8 || raw <= 2.2)) issues.push({ key: 'acquiescence', serious: false, n: raw });

  const verdict = issues.some(i => i.serious) ? 'caution' : issues.length ? 'notes' : 'good';
  return { verdict, issues, secPerItem, raw };
}

export { ITEMS };
