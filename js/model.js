import { DATA } from './data.js?v=3';

export const TYPES = ['R', 'I', 'A', 'S', 'E', 'C'];
export const OCC = DATA.occ;
const S = DATA.ro;

function rng(seed) {
  return () => {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function shuffle(arr, r) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(r() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// One item of every group per round, groups in a seeded order: same order for every respondent.
function interleave(groups, seed) {
  const r = rng(seed);
  const rounds = Math.max(...groups.map(g => g.length));
  const out = [];
  for (let k = 0; k < rounds; k++) {
    for (const g of shuffle(groups, r)) if (g[k]) out.push(g[k]);
  }
  return out;
}

const intItems = TYPES.map(t => S.int[t].map((_, i) => ({ id: `I_${t}${i + 1}`, mod: 'int', t, i })));
const confItems = TYPES.map(t => S.conf[t].map((_, i) => ({ id: `K_${t}${i + 1}`, mod: 'conf', t, i })));
const ancItems = S.anchors.map((a, ai) => a.items.map((_, j) => ({ id: `A_${a.code}${j + 1}`, mod: 'anc', anchor: a.code, ai, j })));
const b5Items = S.b5.map((b, k) => ({ id: `B_${k + 1}`, mod: 'b5', trait: b.trait, rev: b.rev, k }));
const sdtItems = S.sdt.map((n, ni) => n.items.map((_, j) => ({ id: `N_${ni + 1}${j + 1}`, mod: 'sdt', need: ni, j })));
const ctxItems = S.ctx.map((_, k) => ({ id: `U_${k + 1}`, mod: 'ctx', k }));
const adItems = S.adapt.map((d, di) => d.items.map((_, j) => ({ id: `L_${di + 1}${j + 1}`, mod: 'ad', dim: di, j })));

export const ATTENTION = [
  { id: 'X_1', mod: 'int', att: true, expect: 4, n: 0 },
  { id: 'X_2', mod: 'b5', att: true, expect: 1, n: 1 },
];

function insertAt(list, pos, item) {
  const a = list.slice();
  a.splice(pos, 0, item);
  return a;
}

export const MODULES = [
  { id: 'int', scale: 'like', per: 7, items: insertAt(interleave(intItems, 11), 28, ATTENTION[0]) },
  { id: 'conf', scale: 'conf', per: 8, items: interleave(confItems, 23) },
  { id: 'anc', scale: 'true', per: 8, items: interleave(ancItems, 37), pick: true },
  { id: 'b5', scale: 'desc', per: 7, items: insertAt(b5Items, 12, ATTENTION[1]) },
  { id: 'sdt', scale: 'true', per: 9, items: interleave(sdtItems, 41) },
  { id: 'ctx', scale: 'bi', per: 10, items: ctxItems },
  { id: 'ad', scale: 'strength', per: 6, items: interleave(adItems, 53) },
  { id: 'open', open: true, items: S.open.map((_, k) => ({ id: `G_${k + 1}`, mod: 'open', k })) },
];

export const PAGES = [];
MODULES.forEach((m, mi) => {
  if (m.open) { PAGES.push({ kind: 'open', mod: m.id, mi, first: true }); return; }
  for (let i = 0; i < m.items.length; i += m.per) {
    PAGES.push({ kind: 'items', mod: m.id, mi, scale: m.scale, items: m.items.slice(i, i + m.per), first: i === 0 });
  }
  if (m.pick) PAGES.push({ kind: 'pick', mod: m.id, mi });
});

export const ITEMS = {};
for (const m of MODULES) for (const it of m.items) ITEMS[it.id] = it;
export const ANCHOR_ITEMS = MODULES.find(m => m.id === 'anc').items;
export const CLOSED_ITEMS = MODULES.filter(m => !m.open).flatMap(m => m.items);

export function itemText(it, lang, ui) {
  const D = DATA[lang];
  switch (it.mod === 'int' && it.att ? 'att' : it.mod) {
    case 'att': return ui.attention[it.n];
    case 'int': return D.int[it.t][it.i];
    case 'conf': return D.conf[it.t][it.i];
    case 'anc': return D.anchors[it.ai].items[it.j];
    case 'b5': return it.att ? ui.attention[it.n] : D.b5[it.k].txt;
    case 'sdt': return D.sdt[it.need].items[it.j];
    case 'ctx': return D.ctx[it.k];
    case 'ad': return D.adapt[it.dim].items[it.j];
    case 'open': return D.open[it.k].q;
    default: return '';
  }
}

export function pageComplete(p, st) {
  if (p.kind === 'items') return p.items.every(it => st.answers[it.id] >= 1);
  if (p.kind === 'pick') return (st.picks || []).length === 3;
  return true;
}
